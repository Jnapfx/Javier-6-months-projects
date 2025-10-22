#!/usr/bin/env python3
"""
Link Validation Script for GitHub Repository Cleanup
Scans all README files for broken internal and external links
"""

import os
import re
import subprocess
from pathlib import Path
from urllib.parse import urlparse
import urllib.request
import time

class LinkValidator:
    def __init__(self, repo_root="."):
        self.repo_root = Path(repo_root)
        self.broken_links = []
        self.valid_links = []
        self.internal_links = []
        self.external_links = []
        
    def find_readme_files(self):
        """Find all README files in the repository"""
        readme_files = []
        for pattern in ["README.md", "readme.md", "Readme.md"]:
            readme_files.extend(self.repo_root.rglob(pattern))
        return readme_files
    
    def extract_links(self, file_path):
        """Extract all markdown links from a file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            try:
                with open(file_path, 'r', encoding='latin-1') as f:
                    content = f.read()
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
                return []
        
        # Find markdown links [text](url) and reference links [text]: url
        link_patterns = [
            r'\[([^\]]*)\]\(([^)]+)\)',  # [text](url)
            r'\[([^\]]*)\]:\s*(.+)',     # [text]: url
        ]
        
        links = []
        for pattern in link_patterns:
            matches = re.findall(pattern, content)
            for text, url in matches:
                links.append({
                    'text': text.strip(),
                    'url': url.strip(),
                    'file': str(file_path)
                })
        
        return links
    
    def is_internal_link(self, url):
        """Check if a link is internal to the repository"""
        # Remove fragments and queries
        clean_url = url.split('#')[0].split('?')[0]
        
        # Check for relative paths or paths starting with ./
        if (not clean_url.startswith('http') and 
            not clean_url.startswith('mailto:') and
            not clean_url.startswith('tel:')):
            return True
        return False
    
    def validate_internal_link(self, link):
        """Validate internal repository links"""
        url = link['url']
        file_path = Path(link['file'])
        
        # Remove fragments
        clean_url = url.split('#')[0]
        if not clean_url:  # Just a fragment link
            return True
        
        # Resolve relative path
        if clean_url.startswith('./'):
            target_path = file_path.parent / clean_url[2:]
        elif clean_url.startswith('/'):
            target_path = self.repo_root / clean_url[1:]
        else:
            target_path = file_path.parent / clean_url
        
        # Check if target exists
        if target_path.exists():
            return True
        
        # Check if it's a directory and index file exists
        if target_path.is_dir():
            for index_file in ['README.md', 'readme.md', 'index.html', 'index.md']:
                if (target_path / index_file).exists():
                    return True
        
        return False
    
    def validate_external_link(self, url):
        """Validate external HTTP/HTTPS links"""
        try:
            req = urllib.request.Request(
                url, 
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            )
            with urllib.request.urlopen(req, timeout=10) as response:
                return response.status < 400
        except Exception:
            return False
    
    def validate_all_links(self):
        """Validate all links in all README files"""
        readme_files = self.find_readme_files()
        print(f"Found {len(readme_files)} README files to validate")
        
        all_links = []
        for readme_file in readme_files:
            links = self.extract_links(readme_file)
            all_links.extend(links)
        
        print(f"Found {len(all_links)} total links to validate")
        
        # Separate internal and external links
        for link in all_links:
            if self.is_internal_link(link['url']):
                self.internal_links.append(link)
            else:
                self.external_links.append(link)
        
        print(f"Internal links: {len(self.internal_links)}")
        print(f"External links: {len(self.external_links)}")
        
        # Validate internal links
        print("\nValidating internal links...")
        for link in self.internal_links:
            if self.validate_internal_link(link):
                self.valid_links.append(link)
            else:
                self.broken_links.append({**link, 'type': 'internal'})
                print(f"BROKEN INTERNAL: {link['url']} in {link['file']}")
        
        # Validate external links (with rate limiting)
        print("\nValidating external links...")
        for i, link in enumerate(self.external_links):
            if i > 0 and i % 10 == 0:  # Rate limiting
                time.sleep(2)
            
            if link['url'].startswith(('mailto:', 'tel:')):
                self.valid_links.append(link)
                continue
                
            if self.validate_external_link(link['url']):
                self.valid_links.append(link)
            else:
                self.broken_links.append({**link, 'type': 'external'})
                print(f"BROKEN EXTERNAL: {link['url']} in {link['file']}")
    
    def generate_report(self):
        """Generate a validation report"""
        total_links = len(self.valid_links) + len(self.broken_links)
        
        report = f"""
# Link Validation Report

## Summary
- Total links found: {total_links}
- Valid links: {len(self.valid_links)}
- Broken links: {len(self.broken_links)}
- Success rate: {(len(self.valid_links)/total_links*100):.1f}% if total_links > 0 else 0

## Broken Links
"""
        
        if self.broken_links:
            for link in self.broken_links:
                report += f"- **{link['type'].upper()}**: `{link['url']}` in `{link['file']}`\n"
        else:
            report += "No broken links found! ✅\n"
        
        return report

def main():
    validator = LinkValidator()
    validator.validate_all_links()
    report = validator.generate_report()
    
    # Save report
    with open('link_validation_report.md', 'w') as f:
        f.write(report)
    
    print(report)
    
    # Return exit code based on results
    return len(validator.broken_links)

if __name__ == "__main__":
    exit_code = main()
    exit(exit_code)