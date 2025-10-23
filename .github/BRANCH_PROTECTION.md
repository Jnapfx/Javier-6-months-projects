# Branch Protection Guidelines

This document outlines recommended branch protection rules for maintaining code quality and preventing accidental changes to important branches.

## Current Branch Structure

- `main` - Primary branch containing stable, production-ready code
- `backup-local-changes` - Backup branch for local changes

## Recommended Branch Protection Rules

### For Main Branch

These settings should be configured on the GitHub repository settings:

#### Required Status Checks
- ✅ Require status checks to pass before merging
- ✅ Require branches to be up to date before merging
- Status checks to require:
  - Code quality checks (if CI/CD is set up)
  - Security scans
  - Documentation updates

#### Pull Request Requirements
- ✅ Require pull request reviews before merging
- Number of required reviewers: 1 (for personal projects) or 2+ (for team projects)
- ✅ Dismiss stale pull request approvals when new commits are pushed
- ✅ Require review from code owners (if CODEOWNERS file exists)

#### Additional Restrictions
- ✅ Restrict pushes that create files larger than 100MB
- ✅ Require signed commits (recommended for security)
- ✅ Include administrators in these restrictions

#### Branch Deletion Protection
- ✅ Prevent force pushes to main branch
- ✅ Prevent deletion of main branch

## Local Git Hooks Integration

The installed Git hooks complement branch protection by:

1. **Pre-commit Hook**: Prevents committing problematic code
2. **Commit-msg Hook**: Enforces consistent commit message format
3. **Pre-push Hook**: Warns before pushing to protected branches

## Setting Up Branch Protection (GitHub)

### Via GitHub Web Interface

1. Go to repository Settings
2. Click "Branches" in the left sidebar
3. Click "Add rule" next to "Branch protection rules"
4. Enter branch name pattern: `main`
5. Configure the following settings:

```
☑️ Require pull request reviews before merging
   ☑️ Required number of reviewers: 1
   ☑️ Dismiss stale pull request approvals when new commits are pushed
   
☑️ Require status checks to pass before merging
   ☑️ Require branches to be up to date before merging
   
☑️ Require signed commits
☑️ Require linear history
☑️ Include administrators
☑️ Restrict pushes that create files larger than 100MB
```

### Via GitHub CLI (if available)

```bash
# Enable branch protection for main branch
gh api repos/:owner/:repo/branches/main/protection \
  --method PUT \
  --field required_status_checks='{"strict":true,"contexts":[]}' \
  --field enforce_admins=true \
  --field required_pull_request_reviews='{"required_approving_review_count":1,"dismiss_stale_reviews":true}' \
  --field restrictions=null
```

## Workflow Recommendations

### For Personal Projects
1. Create feature branches for new work
2. Use pull requests even for personal changes (good practice)
3. Ensure all commits pass local Git hooks
4. Merge via pull requests to maintain history

### For Team Projects
1. **Never push directly to main**
2. Create descriptive branch names: `feature/user-auth`, `fix/login-bug`
3. Use draft pull requests for work-in-progress
4. Require at least one review before merging
5. Use "Squash and merge" for clean history

## Branch Naming Conventions

### Recommended Patterns
- `feature/description` - New features
- `fix/description` - Bug fixes
- `hotfix/description` - Critical fixes
- `docs/description` - Documentation updates
- `refactor/description` - Code refactoring
- `test/description` - Test additions/updates

### Examples
- `feature/user-authentication`
- `fix/login-endpoint-error`
- `docs/update-readme`
- `refactor/simplify-data-processing`

## Emergency Procedures

### Hotfix Process
1. Create hotfix branch from main: `git checkout -b hotfix/critical-fix main`
2. Make minimal necessary changes
3. Test thoroughly
4. Create pull request with "HOTFIX" label
5. Get expedited review
6. Merge and deploy immediately

### Bypassing Protection (Emergency Only)
```bash
# Temporarily disable hooks (local only)
git commit --no-verify -m "emergency: critical security fix"
git push --no-verify
```

**Note**: Repository-level branch protection cannot be bypassed without admin access.

## Monitoring and Compliance

### Regular Audits
- Review branch protection settings monthly
- Check for any bypassed protections in audit logs
- Verify all team members understand the workflow

### Metrics to Track
- Number of direct pushes to main (should be 0)
- Pull request review coverage
- Time from PR creation to merge
- Number of failed status checks

## Troubleshooting

### Common Issues

**"Required status checks failed"**
- Check CI/CD pipeline status
- Ensure all tests pass locally
- Verify branch is up to date with main

**"Pull request review required"**
- Request review from team member
- Address any review comments
- Ensure reviewer has appropriate permissions

**"Branch protection rule violations"**
- Check which rule is being violated
- Follow the proper workflow (create PR instead of direct push)
- Contact repository admin if rule needs adjustment

## Additional Resources

- [GitHub Branch Protection Documentation](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/about-protected-branches)
- [Git Flow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
- [Conventional Commits](https://www.conventionalcommits.org/)

## Configuration Checklist

- [ ] Main branch protection enabled
- [ ] Pull request reviews required
- [ ] Status checks configured
- [ ] Force push prevention enabled
- [ ] Branch deletion protection enabled
- [ ] Git hooks installed locally
- [ ] Team members trained on workflow
- [ ] Emergency procedures documented
- [ ] Regular audit schedule established