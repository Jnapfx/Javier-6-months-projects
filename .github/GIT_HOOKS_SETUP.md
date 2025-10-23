# Git Hooks Configuration

This repository includes custom Git hooks to maintain code quality and enforce best practices.

## Installed Hooks

### Pre-commit Hook
**File:** `.git/hooks/pre-commit`

**Purpose:** Runs quality checks before each commit

**Checks performed:**
- Detects temporary files (.tmp, .bak, .DS_Store, etc.)
- Identifies large files (>10MB) and suggests Git LFS
- Scans for potential secrets (passwords, API keys, tokens)
- Validates Python syntax for .py files
- Warns about directories missing README.md files

**Usage:** Automatically runs when you execute `git commit`

### Commit Message Hook
**File:** `.git/hooks/commit-msg`

**Purpose:** Enforces conventional commit message format

**Format required:**
```
<type>[optional scope]: <description>

Types: feat, fix, docs, style, refactor, test, chore, perf, ci, build, revert
```

**Examples:**
- `feat: add user authentication system`
- `fix(api): resolve login endpoint error`
- `docs: update installation instructions`
- `refactor: simplify data processing logic`

**Rules:**
- Description must be at least 10 characters
- First line should be ≤72 characters
- Description should start with lowercase
- No trailing period

### Pre-push Hook
**File:** `.git/hooks/pre-push`

**Purpose:** Final quality checks before pushing to remote

**Checks performed:**
- Warns when pushing to protected branches (main/master)
- Alerts about large numbers of unpushed commits
- Performs final security scan for sensitive information
- Reports repository size and warns if >100MB
- Checks for essential documentation (README.md, LICENSE)

## Managing Hooks

### Enabling/Disabling Hooks

To temporarily disable a hook:
```bash
# Rename the hook file
mv .git/hooks/pre-commit .git/hooks/pre-commit.disabled
```

To re-enable:
```bash
# Rename back
mv .git/hooks/pre-commit.disabled .git/hooks/pre-commit
```

### Bypassing Hooks

For emergency commits (use sparingly):
```bash
# Skip pre-commit and commit-msg hooks
git commit --no-verify -m "emergency fix"

# Skip pre-push hook
git push --no-verify
```

### Updating Hooks

Hooks are stored in `.git/hooks/` and are not tracked by Git. To update:

1. Modify the hook file directly
2. Ensure it remains executable: `chmod +x .git/hooks/hook-name`
3. Test with a dummy commit/push

### Sharing Hooks with Team

Since hooks in `.git/hooks/` aren't tracked, consider:

1. **Template approach:** Store hook templates in a tracked directory
2. **Setup script:** Create a script to copy hooks to `.git/hooks/`
3. **Git templates:** Use `git config init.templateDir` for new repositories

## Troubleshooting

### Hook Not Running
- Check if file is executable: `ls -la .git/hooks/`
- Make executable: `chmod +x .git/hooks/hook-name`
- Verify shebang line: `#!/bin/sh`

### Hook Failing
- Run hook manually to see detailed output
- Check for syntax errors in the hook script
- Ensure required tools are installed (python3, etc.)

### Performance Issues
- Hooks should complete quickly (<5 seconds)
- Consider optimizing checks for large repositories
- Use `--no-verify` for time-sensitive commits

## Best Practices

1. **Keep hooks fast:** Aim for <5 second execution time
2. **Provide clear feedback:** Use colored output and helpful messages
3. **Allow bypassing:** Always provide `--no-verify` option for emergencies
4. **Test thoroughly:** Test hooks with various scenarios
5. **Document changes:** Update this file when modifying hooks

## Configuration

### Customizing Checks

Edit the hook files directly to:
- Adjust file size limits
- Modify secret detection patterns
- Change commit message requirements
- Add project-specific validations

### Environment Variables

Some hooks respect these environment variables:
- `SKIP_HOOKS=1` - Skip all custom validations
- `HOOK_DEBUG=1` - Enable verbose output

## Security Considerations

- Hooks run with your user permissions
- Never include sensitive information in hook scripts
- Be cautious with hooks from untrusted sources
- Regularly review hook contents for security

## Support

For issues with Git hooks:
1. Check this documentation
2. Review hook output for specific error messages
3. Test hooks in isolation
4. Consider temporarily disabling problematic hooks