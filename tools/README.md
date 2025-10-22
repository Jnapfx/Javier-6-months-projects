# Repository Tools

This directory contains automated tools and reports for maintaining repository quality and organization.

## Structure

### `/scripts/`
Contains Python scripts for automated repository analysis and validation:

- `security_audit.py` - Scans for sensitive information and security issues
- `structure_validation.py` - Validates repository structure and naming conventions  
- `validate_links.py` - Checks for broken links in documentation
- `setup-git-hooks.sh` - Sets up Git hooks for code quality maintenance

### `/reports/`
Contains generated reports from repository analysis tools:

- `security_audit_report.md` - Security scan results and recommendations
- `structure_validation_report.md` - Repository structure analysis
- `link_validation_report.md` - Link validation results
- `binary_files_audit.md` - Large file analysis
- `file_naming_audit.md` - File naming convention review
- `git_branch_cleanup_analysis.md` - Git branch cleanup recommendations
- `quality_assurance_summary.md` - Overall quality assessment
- `REPOSITORY_SETTINGS.md` - Repository configuration documentation

## Usage

Run scripts from the repository root:

```bash
python3 tools/scripts/security_audit.py
python3 tools/scripts/structure_validation.py
python3 tools/scripts/validate_links.py
```

Reports are automatically generated in the `reports/` directory when scripts are executed.