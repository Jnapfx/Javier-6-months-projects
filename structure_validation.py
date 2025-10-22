#!/usr/bin/env python3
"""
Final Structure Validation Script for GitHub Repository Cleanup
Validates repository structure, naming conventions, and completeness
"""

import os
import re
from pathlib import Path

class StructureValidator:
    def __init__(self, repo_root="."):
        self.repo_root = Path(repo_root)
        self.required_folders = [
            'mock_interviews',
            'ai_utilization', 
            'troubleshooting_debugging',
            'coding_practice'
        ]
        self.validation_results = {
            'required_folders': {},
            'naming_conventions': [],
            'readme_files': [],
            'temporary_files': [],
            'structure_issues': []
        }
        
    def validate_required_folders(self):
        """Check if all required technical development folders exist"""
        print("Validating required folder structure...")
        
        for folder in self.required_folders:
            folder_path = self.repo_root / folder
            if folder_path.exists() and folder_path.is_dir():
                self.validation_results['required_folders'][folder] = 'EXISTS'
                print(f"✅ {folder} - Found")
            else:
                self.validation_results['required_folders'][folder] = 'MISSING'
                print(f"❌ {folder} - Missing")
    
    def validate_naming_conventions(self):
        """Check folder and file naming conventions"""
        print("\nValidating naming conventions...")
        
        # Check for proper naming patterns
        proper_pattern = re.compile(r'^[a-z0-9_]+$')
        
        for item in self.repo_root.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                if not proper_pattern.match(item.name):
                    issue = f"Folder '{item.name}' doesn't follow lowercase_with_underscores convention"
                    self.validation_results['naming_conventions'].append(issue)
                    print(f"⚠️  {issue}")
                else:
                    print(f"✅ {item.name} - Proper naming")
    
    def check_temporary_files(self):
        """Check for temporary files that should be removed"""
        print("\nChecking for temporary files...")
        
        temp_patterns = [
            r'\.DS_Store$',
            r'^~\$',
            r'\.tmp$',
            r'\.temp$',
            r'Thumbs\.db$',
            r'\.swp$',
            r'\.swo$'
        ]
        
        temp_files_found = []
        
        for root, dirs, files in os.walk(self.repo_root):
            # Skip .git directory
            if '.git' in dirs:
                dirs.remove('.git')
                
            for file in files:
                file_path = Path(root) / file
                for pattern in temp_patterns:
                    if re.search(pattern, file):
                        temp_files_found.append(str(file_path))
                        break
        
        if temp_files_found:
            self.validation_results['temporary_files'] = temp_files_found
            print(f"❌ Found {len(temp_files_found)} temporary files:")
            for temp_file in temp_files_found[:10]:  # Show first 10
                print(f"   - {temp_file}")
            if len(temp_files_found) > 10:
                print(f"   ... and {len(temp_files_found) - 10} more")
        else:
            print("✅ No temporary files found")
    
    def validate_readme_files(self):
        """Check for README files in major directories"""
        print("\nValidating README file coverage...")
        
        major_dirs = []
        for item in self.repo_root.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                major_dirs.append(item)
        
        missing_readmes = []
        existing_readmes = []
        
        for dir_path in major_dirs:
            readme_found = False
            for readme_name in ['README.md', 'readme.md', 'Readme.md']:
                readme_path = dir_path / readme_name
                if readme_path.exists():
                    readme_found = True
                    existing_readmes.append(str(readme_path))
                    break
            
            if not readme_found:
                missing_readmes.append(str(dir_path))
        
        self.validation_results['readme_files'] = {
            'existing': existing_readmes,
            'missing': missing_readmes
        }
        
        print(f"✅ Found README files in {len(existing_readmes)} directories")
        if missing_readmes:
            print(f"❌ Missing README files in {len(missing_readmes)} directories:")
            for missing in missing_readmes:
                print(f"   - {missing}")
    
    def validate_root_files(self):
        """Check for essential root-level files"""
        print("\nValidating root-level files...")
        
        essential_files = {
            'README.md': False,
            'Readme.md': False,
            'LICENSE': False,
            '.gitignore': False
        }
        
        for file_name in essential_files.keys():
            file_path = self.repo_root / file_name
            if file_path.exists():
                essential_files[file_name] = True
                print(f"✅ {file_name} - Found")
        
        # Check if at least one README variant exists
        readme_exists = any([
            essential_files.get('README.md', False),
            essential_files.get('Readme.md', False)
        ])
        
        if not readme_exists:
            print("❌ No root README file found")
            self.validation_results['structure_issues'].append("Missing root README file")
        
        if not essential_files.get('LICENSE', False):
            print("⚠️  LICENSE file not found")
            self.validation_results['structure_issues'].append("Missing LICENSE file")
        
        if not essential_files.get('.gitignore', False):
            print("⚠️  .gitignore file not found")
            self.validation_results['structure_issues'].append("Missing .gitignore file")
    
    def check_file_sizes(self):
        """Check for unusually large files"""
        print("\nChecking for large files...")
        
        large_files = []
        size_limit = 50 * 1024 * 1024  # 50MB
        
        for root, dirs, files in os.walk(self.repo_root):
            if '.git' in dirs:
                dirs.remove('.git')
                
            for file in files:
                file_path = Path(root) / file
                try:
                    if file_path.stat().st_size > size_limit:
                        size_mb = file_path.stat().st_size / (1024 * 1024)
                        large_files.append((str(file_path), f"{size_mb:.1f}MB"))
                except (OSError, PermissionError):
                    continue
        
        if large_files:
            print(f"⚠️  Found {len(large_files)} large files (>50MB):")
            for file_path, size in large_files:
                print(f"   - {file_path} ({size})")
        else:
            print("✅ No unusually large files found")
    
    def generate_validation_report(self):
        """Generate comprehensive validation report"""
        
        # Count issues
        total_issues = 0
        total_issues += len([f for f in self.validation_results['required_folders'].values() if f == 'MISSING'])
        total_issues += len(self.validation_results['naming_conventions'])
        total_issues += len(self.validation_results['temporary_files'])
        total_issues += len(self.validation_results['readme_files']['missing'])
        total_issues += len(self.validation_results['structure_issues'])
        
        report = f"""
# Final Structure Validation Report

## Summary
- Total validation issues found: {total_issues}
- Repository structure compliance: {'✅ PASS' if total_issues == 0 else '❌ NEEDS ATTENTION'}

## Required Folders Status
"""
        
        for folder, status in self.validation_results['required_folders'].items():
            status_icon = "✅" if status == "EXISTS" else "❌"
            report += f"- {status_icon} **{folder}**: {status}\n"
        
        if self.validation_results['naming_conventions']:
            report += f"\n## Naming Convention Issues ({len(self.validation_results['naming_conventions'])})\n"
            for issue in self.validation_results['naming_conventions']:
                report += f"- ❌ {issue}\n"
        else:
            report += "\n## Naming Conventions\n- ✅ All folders follow proper naming conventions\n"
        
        if self.validation_results['temporary_files']:
            report += f"\n## Temporary Files Found ({len(self.validation_results['temporary_files'])})\n"
            for temp_file in self.validation_results['temporary_files'][:10]:
                report += f"- ❌ {temp_file}\n"
            if len(self.validation_results['temporary_files']) > 10:
                report += f"- ... and {len(self.validation_results['temporary_files']) - 10} more files\n"
        else:
            report += "\n## Temporary Files\n- ✅ No temporary files found\n"
        
        readme_missing = self.validation_results['readme_files']['missing']
        if readme_missing:
            report += f"\n## Missing README Files ({len(readme_missing)})\n"
            for missing in readme_missing:
                report += f"- ❌ {missing}\n"
        else:
            report += "\n## README File Coverage\n- ✅ All major directories have README files\n"
        
        if self.validation_results['structure_issues']:
            report += f"\n## Structure Issues ({len(self.validation_results['structure_issues'])})\n"
            for issue in self.validation_results['structure_issues']:
                report += f"- ❌ {issue}\n"
        
        report += """
## Recommendations

### If Issues Found:
1. **Create missing required folders** - Ensure all technical development folders exist
2. **Fix naming conventions** - Use lowercase_with_underscores for folder names
3. **Remove temporary files** - Clean up .DS_Store, .tmp, and other temporary files
4. **Add missing README files** - Each major directory should have documentation
5. **Add essential root files** - Ensure LICENSE and .gitignore exist

### If No Issues:
- ✅ Repository structure meets professional standards
- ✅ Ready for public evaluation and review
- ✅ All cleanup requirements have been satisfied

## Next Steps
- [ ] Address any issues identified above
- [ ] Re-run validation after fixes
- [ ] Consider the repository ready for professional presentation
"""
        
        return report
    
    def run_full_validation(self):
        """Run complete structure validation"""
        print("=" * 60)
        print("GITHUB REPOSITORY STRUCTURE VALIDATION")
        print("=" * 60)
        
        self.validate_required_folders()
        self.validate_naming_conventions()
        self.check_temporary_files()
        self.validate_readme_files()
        self.validate_root_files()
        self.check_file_sizes()
        
        print("\n" + "=" * 60)
        print("VALIDATION COMPLETE")
        print("=" * 60)
        
        return self.generate_validation_report()

def main():
    validator = StructureValidator()
    report = validator.run_full_validation()
    
    # Save report
    with open('structure_validation_report.md', 'w') as f:
        f.write(report)
    
    print(report)
    
    # Return exit code based on issues found
    total_issues = 0
    total_issues += len([f for f in validator.validation_results['required_folders'].values() if f == 'MISSING'])
    total_issues += len(validator.validation_results['naming_conventions'])
    total_issues += len(validator.validation_results['temporary_files'])
    total_issues += len(validator.validation_results['readme_files']['missing'])
    total_issues += len(validator.validation_results['structure_issues'])
    
    return total_issues

if __name__ == "__main__":
    exit_code = main()
    exit(exit_code)