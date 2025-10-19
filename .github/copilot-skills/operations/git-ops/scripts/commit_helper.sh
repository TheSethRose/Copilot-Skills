#!/usr/bin/env bash
#
# commit_helper.sh - Generate conventional commit messages
#
# Purpose: Analyze staged changes and generate structured commit messages
#          following Conventional Commits specification
#
# Usage:
#   commit_helper.sh [OPTIONS]
#
# Options:
#   --type TYPE        Commit type (feat, fix, docs, etc.)
#   --scope SCOPE      Commit scope
#   --breaking         Mark as breaking change
#   --issue NUMBER     Reference issue number
#   --auto-commit      Automatically commit after generation
#
# Examples:
#   commit_helper.sh
#   commit_helper.sh --type feat --scope auth
#   commit_helper.sh --breaking --issue 123
#

set -euo pipefail

# Colors
BLUE='\033[0;34m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Configuration
COMMIT_TYPE=""
COMMIT_SCOPE=""
IS_BREAKING=false
ISSUE_NUMBER=""
AUTO_COMMIT=false

# Parse options
while [[ $# -gt 0 ]]; do
    case $1 in
        --type)
            COMMIT_TYPE="$2"
            shift 2
            ;;
        --scope)
            COMMIT_SCOPE="$2"
            shift 2
            ;;
        --breaking)
            IS_BREAKING=true
            shift
            ;;
        --issue)
            ISSUE_NUMBER="$2"
            shift 2
            ;;
        --auto-commit)
            AUTO_COMMIT=true
            shift
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

log_info() {
    echo -e "${BLUE}ℹ${NC} $1"
}

log_success() {
    echo -e "${GREEN}✓${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

log_error() {
    echo -e "${RED}✗${NC} $1"
}

check_staged_changes() {
    if [[ -z $(git diff --cached --name-only) ]]; then
        log_error "No staged changes found. Use 'git add' first."
        exit 1
    fi
}

analyze_changes() {
    log_info "Analyzing staged changes..."
    echo
    
    # Get changed files
    local changed_files=$(git diff --cached --name-only)
    local file_count=$(echo "$changed_files" | wc -l | tr -d ' ')
    
    echo "Files changed: $file_count"
    echo "$changed_files" | head -5
    if [[ $file_count -gt 5 ]]; then
        echo "... and $((file_count - 5)) more"
    fi
    echo
    
    # Get stats
    git diff --cached --stat
    echo
}

infer_commit_type() {
    local changes=$(git diff --cached)
    
    # Check for test files
    if echo "$changes" | grep -q "test_\|spec_\|\.test\.\|\.spec\."; then
        echo "test"
        return
    fi
    
    # Check for documentation
    if echo "$changes" | grep -q "\.md\|\.txt\|docs/\|README"; then
        echo "docs"
        return
    fi
    
    # Check for new files (likely feat)
    if git diff --cached --diff-filter=A --name-only | grep -q .; then
        echo "feat"
        return
    fi
    
    # Check for deletions (likely refactor or chore)
    if git diff --cached --diff-filter=D --name-only | grep -q .; then
        echo "refactor"
        return
    fi
    
    # Default to fix for modifications
    echo "fix"
}

infer_scope() {
    local files=$(git diff --cached --name-only)
    
    # Try to extract common directory
    local common_dir=$(echo "$files" | awk -F'/' '{print $1}' | sort | uniq -c | sort -rn | head -1 | awk '{print $2}')
    
    if [[ -n "$common_dir" ]] && [[ "$common_dir" != "." ]]; then
        echo "$common_dir"
    fi
}

generate_summary() {
    # Get first line of each file's diff
    local summaries=$(git diff --cached -U0 | grep "^+" | grep -v "^+++" | head -5)
    
    # Count additions and deletions
    local stats=$(git diff --cached --shortstat)
    
    echo "$stats"
}

prompt_for_details() {
    local field="$1"
    local default="$2"
    
    if [[ -n "$default" ]]; then
        read -p "$field [$default]: " value
        echo "${value:-$default}"
    else
        read -p "$field: " value
        echo "$value"
    fi
}

generate_commit_message() {
    log_info "Generating commit message..."
    echo
    
    # Infer type if not provided
    if [[ -z "$COMMIT_TYPE" ]]; then
        local inferred_type=$(infer_commit_type)
        COMMIT_TYPE=$(prompt_for_details "Commit type (feat/fix/docs/style/refactor/test/chore)" "$inferred_type")
    fi
    
    # Infer scope if not provided
    if [[ -z "$COMMIT_SCOPE" ]]; then
        local inferred_scope=$(infer_scope)
        if [[ -n "$inferred_scope" ]]; then
            read -p "Commit scope [$inferred_scope] (optional, press Enter to skip): " scope_input
            COMMIT_SCOPE="${scope_input:-$inferred_scope}"
        else
            read -p "Commit scope (optional, press Enter to skip): " COMMIT_SCOPE
        fi
    fi
    
    # Get summary
    read -p "Brief description: " description
    
    # Get detailed explanation
    echo "Detailed explanation (press Ctrl+D when done):"
    detailed=$(cat)
    
    # Build commit message
    local message=""
    
    # First line: type(scope): description
    if [[ -n "$COMMIT_SCOPE" ]]; then
        message="${COMMIT_TYPE}(${COMMIT_SCOPE}): ${description}"
    else
        message="${COMMIT_TYPE}: ${description}"
    fi
    
    # Add body if provided
    if [[ -n "$detailed" ]]; then
        message="${message}

${detailed}"
    fi
    
    # Add change stats
    local stats=$(generate_summary)
    message="${message}

${stats}"
    
    # Add issue reference
    if [[ -n "$ISSUE_NUMBER" ]]; then
        message="${message}

Refs: #${ISSUE_NUMBER}"
    fi
    
    # Add breaking change note
    if [[ "$IS_BREAKING" == "true" ]]; then
        message="${message}

BREAKING CHANGE: This commit introduces breaking changes."
    fi
    
    echo "$message"
}

preview_commit() {
    local message="$1"
    
    echo
    log_info "Generated commit message:"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "$message"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo
}

execute_commit() {
    local message="$1"
    
    if [[ "$AUTO_COMMIT" == "true" ]]; then
        git commit -m "$message"
        log_success "Commit created successfully"
        return 0
    fi
    
    read -p "Create commit? [y/N] " -n 1 -r
    echo
    
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        git commit -m "$message"
        log_success "Commit created successfully"
        
        # Show the commit
        echo
        git log -1 --stat
    else
        log_info "Commit cancelled. Message saved to .git/COMMIT_EDITMSG"
        echo "$message" > .git/COMMIT_EDITMSG
    fi
}

main() {
    log_info "Conventional Commit Helper"
    echo
    
    # Check for staged changes
    check_staged_changes
    
    # Show what's being committed
    analyze_changes
    
    # Generate commit message
    commit_message=$(generate_commit_message)
    
    # Preview
    preview_commit "$commit_message"
    
    # Execute or save
    execute_commit "$commit_message"
}

main "$@"
