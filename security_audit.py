#!/usr/bin/env python3
"""
Security Audit Script for GitHub Repository Cleanup
Scans all files for potential sensitive information (passwords, API keys, etc.)
"""

import os
import re
import subprocess
from pathlib import Path

class SecurityAuditor:
    def __init__(self, repo_root="."):
        self.repo_root = Path(repo_root)
        self.sensitive_patterns = {
            'password': [
                r'password\s*[=:]\s*["\']?([^"\'\s]+)["\']?',
                r'pwd\s*[=:]\s*["\']?([^"\'\s]+)["\']?',
                r'passwd\s*[=:]\s*["\']?([^"\'\s]+)["\']?',
            ],
            'api_key': [
                r'api[_-]?key\s*[=:]\s*["\']?([^"\'\s]+)["\']?',
                r'apikey\s*[=:]\s*["\']?([^"\'\s]+)["\']?',
                r'secret[_-]?key\s*[=:]\s*["\']?([^"\'\s]+)["\']?',
            ],
            'token': [
                r'token\s*[=:]\s*["\']?([^"\'\s]+)["\']?',
                r'access[_-]?token\s*[=:]\s*["\']?([^"\'\s]+)["\']?',
                r'auth[_-]?token\s*[=:]\s*["\']?([^"\'\s]+)["\']?',
            ],
            'database': [
                r'db[_-]?password\s*[=:]\s*["\']?([^"\'\s]+)["\']?',
                r'database[_-]?url\s*[=:]\s*["\']?([^"\'\s]+)["\']?',
                r'connection[_-]?string\s*[=:]\s*["\']?([^"\'\s]+)["\']?',
            ],
            'aws': [
                r'aws[_-]?access[_-]?key[_-]?id\s*[=:]\s*["\']?([^"\'\s]+)["\']?',
                r'aws[_-]?secret[_-]?access[_-]?key\s*[=:]\s*["\']?([^"\'\s]+)["\']?',
            ],
            'private_key': [
                r'-----BEGIN\s+(RSA\s+)?PRIVATE\s+KEY-----',
                r'-----BEGIN\s+OPENSSH\s+PRIVATE\s+KEY-----',
            ],
            'email_credentials': [
                r'smtp[_-]?password\s*[=:]\s*["\']?([^"\'\s]+)["\']?',
                r'email[_-]?password\s*[=:]\s*["\']?([^"\'\s]+)["\']?',
            ]
        }
        
        self.exclude_patterns = [
            r'\.git/',
            r'__pycache__/',
            r'\.pyc$',
            r'\.jpg$',
            r'\.png$',
            r'\.gif$',
            r'\.pdf$',
            r'\.zip$',
            r'\.exe$',
            r'\.dmg$',
            r'\.iso$',
        ]
        
        self.findings = []
        
    def should_exclude_file(self, file_path):
        """Check if file should be excluded from scanning"""
        file_str = str(file_path)
        for pattern in self.exclude_patterns:
            if re.search(pattern, file_str):
                return True
        return False
    
    def scan_file(self, file_path):
        """Scan a single file for sensitive information"""
        if self.should_exclude_file(file_path):
            return
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except (UnicodeDecodeError, PermissionError, IsADirectoryError):
            try:
                with open(file_path, 'r', encoding='latin-1') as f:
                    content = f.read()
            except Exception:
                return  # Skip files that can't be read
        
        lines = content.split('\n')
        
        for category, patterns in self.sensitive_patterns.items():
            for pattern in patterns:
                for line_num, line in enumerate(lines, 1):
                    matches = re.finditer(pattern, line, re.IGNORECASE)
                    for match in matches:
                        # Skip obvious false positives
                        if self.is_false_positive(line, match.group()):
                            continue
                            
                        self.findings.append({
                            'file': str(file_path),
                            'line': line_num,
                            'category': category,
                            'pattern': pattern,
                            'match': match.group(),
                            'context': line.strip()
                        })
    
    def is_false_positive(self, line, match):
        """Check if a match is likely a false positive"""
        false_positive_indicators = [
            'example',
            'placeholder',
            'your_password_here',
            'your_api_key_here',
            'xxx',
            '***',
            'password123',
            'test',
            'demo',
            'sample',
            'template',
            'TODO',
            'FIXME',
            'replace_with',
            'enter_your',
            'your_key_here',
            'fake',
            'dummy',
        ]
        
        line_lower = line.lower()
        match_lower = match.lower()
        
        for indicator in false_positive_indicators:
            if indicator in line_lower or indicator in match_lower:
                return True
        
        # Skip very short matches that are likely not real secrets
        if len(match.strip('"\'')) < 8:
            return True
            
        return False
    
    def scan_repository(self):
        """Scan all files in the repository"""
        print("Starting security audit...")
        
        # Get all files in repository
        all_files = []
        for root, dirs, files in os.walk(self.repo_root):
            # Skip .git directory
            if '.git' in dirs:
                dirs.remove('.git')
            
            for file in files:
                file_path = Path(root) / file
                all_files.append(file_path)
        
        print(f"Scanning {len(all_files)} files...")
        
        for file_path in all_files:
            self.scan_file(file_path)
        
        print(f"Security audit complete. Found {len(self.findings)} potential issues.")
    
    def check_git_history(self):
        """Check git history for accidentally committed secrets"""
        print("Checking git history for potential secrets...")
        
        try:
            # Get all commit hashes
            result = subprocess.run(
                ['git', 'log', '--pretty=format:%H'],
                capture_output=True,
                text=True,
                cwd=self.repo_root
            )
            
            if result.returncode != 0:
                print("Could not access git history")
                return
            
            commits = result.stdout.strip().split('\n')[:50]  # Check last 50 commits
            
            git_findings = []
            
            for commit in commits:
                if not commit:
                    continue
                    
                # Get commit diff
                diff_result = subprocess.run(
                    ['git', 'show', commit, '--name-only'],
                    capture_output=True,
                    text=True,
                    cwd=self.repo_root
                )
                
                if diff_result.returncode == 0:
                    # Check for sensitive file patterns in commit
                    files = diff_result.stdout.strip().split('\n')
                    for file in files:
                        if any(pattern in file.lower() for pattern in [
                            '.env', 'secret', 'password', 'key', 'credential'
                        ]):
                            git_findings.append({
                                'commit': commit[:8],
                                'file': file,
                                'type': 'sensitive_filename'
                            })
            
            if git_findings:
                print(f"Found {len(git_findings)} potential issues in git history")
                for finding in git_findings:
                    print(f"  Commit {finding['commit']}: {finding['file']}")
            else:
                print("No obvious sensitive files found in recent git history")
                
        except Exception as e:
            print(f"Error checking git history: {e}")
    
    def generate_report(self):
        """Generate security audit report"""
        report = f"""
# Security Audit Report

## Summary
- Files scanned: Multiple files across repository
- Potential security issues found: {len(self.findings)}

## Findings by Category
"""
        
        if not self.findings:
            report += "\n✅ No potential security issues found!\n"
        else:
            # Group findings by category
            by_category = {}
            for finding in self.findings:
                category = finding['category']
                if category not in by_category:
                    by_category[category] = []
                by_category[category].append(finding)
            
            for category, findings in by_category.items():
                report += f"\n### {category.replace('_', ' ').title()} ({len(findings)} issues)\n"
                for finding in findings:
                    report += f"- **{finding['file']}** (line {finding['line']}): `{finding['context']}`\n"
        
        report += """
## Recommendations

1. **Review all flagged items** - Some may be false positives, but verify each one
2. **Remove any real secrets** - Replace with environment variables or secure storage
3. **Add sensitive patterns to .gitignore** - Prevent future accidental commits
4. **Use environment variables** - For configuration that varies by environment
5. **Consider git-secrets** - Tool to prevent committing secrets

## Next Steps

- [ ] Review each flagged item
- [ ] Remove or replace any real sensitive information
- [ ] Update .gitignore if needed
- [ ] Consider implementing pre-commit hooks for security scanning
"""
        
        return report

def main():
    auditor = SecurityAuditor()
    auditor.scan_repository()
    auditor.check_git_history()
    
    report = auditor.generate_report()
    
    # Save report
    with open('security_audit_report.md', 'w') as f:
        f.write(report)
    
    print(report)
    
    # Return exit code based on findings
    return len(auditor.findings)

if __name__ == "__main__":
    exit_code = main()
    exit(exit_code)