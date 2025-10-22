#!/bin/bash
#
# Git Hooks Setup Script
# This script installs and configures Git hooks for code quality maintenance
#

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo "${BLUE}Git Hooks Setup Script${NC}"
echo "=========================="

# Check if we're in a Git repository
if [ ! -d ".git" ]; then
    echo "${RED}Error: Not in a Git repository${NC}"
    echo "Please run this script from the root of your Git repository."
    exit 1
fi

# Create hooks directory if it doesn't exist
if [ ! -d ".git/hooks" ]; then
    echo "${YELLOW}Creating .git/hooks directory...${NC}"
    mkdir -p .git/hooks
fi

# Function to install a hook
install_hook() {
    local hook_name="$1"
    local hook_file=".git/hooks/$hook_name"
    
    if [ -f "$hook_file" ]; then
        echo "${YELLOW}Hook $hook_name already exists${NC}"
        read -p "Overwrite? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo "Skipping $hook_name"
            return
        fi
    fi
    
    echo "${GREEN}Installing $hook_name hook...${NC}"
    # Hook content would be copied here
    # For now, just make it executable if it exists
    if [ -f "$hook_file" ]; then
        chmod +x "$hook_file"
        echo "✓ $hook_name hook installed and made executable"
    fi
}

# Install hooks
echo "${BLUE}Installing Git hooks...${NC}"

# Check if hooks already exist and install them
hooks=("pre-commit" "commit-msg" "pre-push")

for hook in "${hooks[@]}"; do
    if [ -f ".git/hooks/$hook" ]; then
        chmod +x ".git/hooks/$hook"
        echo "${GREEN}✓ $hook hook is ready${NC}"
    else
        echo "${YELLOW}⚠ $hook hook not found${NC}"
    fi
done

# Set up Git configuration for better commit messages
echo "${BLUE}Configuring Git settings...${NC}"

# Set up commit template if it doesn't exist
if [ ! -f ".gitmessage" ]; then
    cat > .gitmessage << 'EOF'
# <type>[optional scope]: <description>
#
# [optional body]
#
# [optional footer(s)]
#
# Types:
#   feat:     A new feature
#   fix:      A bug fix
#   docs:     Documentation only changes
#   style:    Changes that do not affect the meaning of the code
#   refactor: A code change that neither fixes a bug nor adds a feature
#   test:     Adding missing tests or correcting existing tests
#   chore:    Changes to the build process or auxiliary tools
#   perf:     A code change that improves performance
#   ci:       Changes to CI configuration files and scripts
#   build:    Changes that affect the build system or external dependencies
#   revert:   Reverts a previous commit
EOF
    
    git config commit.template .gitmessage
    echo "${GREEN}✓ Commit message template configured${NC}"
fi

# Configure other useful Git settings
git config core.autocrlf input
git config push.default simple
git config pull.rebase false

echo "${GREEN}✓ Git configuration updated${NC}"

# Create hooks documentation if it doesn't exist
if [ ! -f ".github/GIT_HOOKS_SETUP.md" ]; then
    echo "${YELLOW}Creating hooks documentation...${NC}"
    mkdir -p .github
    echo "# Git Hooks Documentation" > .github/GIT_HOOKS_SETUP.md
    echo "See the installed hooks in .git/hooks/ directory" >> .github/GIT_HOOKS_SETUP.md
fi

echo ""
echo "${GREEN}Git hooks setup completed!${NC}"
echo ""
echo "${BLUE}Next steps:${NC}"
echo "1. Review the installed hooks in .git/hooks/"
echo "2. Read the documentation in .github/GIT_HOOKS_SETUP.md"
echo "3. Test the hooks with a sample commit"
echo "4. Use 'git commit --no-verify' to bypass hooks if needed"
echo ""
echo "${YELLOW}Note: Hooks are local to this repository and not tracked by Git${NC}"
echo "Share this setup script with team members to maintain consistency."