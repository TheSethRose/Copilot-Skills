#!/usr/bin/env bash
#
# git_safe_exec.sh - Safe git command execution wrapper
#
# Purpose: Execute git commands with automatic safety checks and backups
#
# Usage:
#   git_safe_exec.sh [OPTIONS] <command> [args...]
#
# Options:
#   --dry-run          Show what would be executed without running
#   --backup           Create backup branch before executing
#   --no-confirm       Skip confirmation prompt
#   --force            Override safety checks (DANGEROUS)
#
# Examples:
#   git_safe_exec.sh commit -m "feat: Add feature"
#   git_safe_exec.sh --backup rebase main
#   git_safe_exec.sh --dry-run push origin main
#

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
DRY_RUN=false
CREATE_BACKUP=false
REQUIRE_CONFIRM=true
FORCE_MODE=false

# Parse options
while [[ $# -gt 0 ]]; do
    case $1 in
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --backup)
            CREATE_BACKUP=true
            shift
            ;;
        --no-confirm)
            REQUIRE_CONFIRM=false
            shift
            ;;
        --force)
            FORCE_MODE=true
            shift
            ;;
        *)
            break
            ;;
    esac
done

# Remaining args are the git command
GIT_COMMAND="$@"

# Utility functions
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

confirm() {
    if [[ "$REQUIRE_CONFIRM" == "false" ]] || [[ "$DRY_RUN" == "true" ]]; then
        return 0
    fi
    
    echo -e "${YELLOW}?${NC} $1"
    read -p "Proceed? [y/N] " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        log_info "Operation cancelled by user"
        exit 0
    fi
}

check_git_repo() {
    if ! git rev-parse --git-dir > /dev/null 2>&1; then
        log_error "Not in a git repository"
        exit 1
    fi
}

check_working_tree() {
    if [[ -n $(git status --porcelain) ]]; then
        log_warning "Working tree has uncommitted changes:"
        git status --short
        echo
        
        if [[ "$FORCE_MODE" != "true" ]]; then
            confirm "Continue with uncommitted changes?"
        fi
    fi
}

create_backup_branch() {
    if [[ "$CREATE_BACKUP" != "true" ]]; then
        return 0
    fi
    
    local current_branch=$(git rev-parse --abbrev-ref HEAD)
    local backup_name="backup-$(date +%Y%m%d-%H%M%S)-${current_branch}"
    
    log_info "Creating backup branch: $backup_name"
    
    if [[ "$DRY_RUN" != "true" ]]; then
        git branch "$backup_name"
        log_success "Backup created: $backup_name"
        
        # Store backup info
        mkdir -p "$BACKUP_DIR"
        echo "$backup_name" >> "$BACKUP_DIR/backups.txt"
    else
        log_info "[DRY-RUN] Would create branch: $backup_name"
    fi
}

show_preview() {
    local cmd="$1"
    
    log_info "Preview of operation: git $cmd"
    echo
    
    # Show relevant info based on command
    case "$cmd" in
        commit*)
            log_info "Staged changes:"
            git diff --cached --stat
            echo
            git diff --cached
            ;;
        push*)
            log_info "Commits to be pushed:"
            local remote=$(echo "$cmd" | awk '{print $2}')
            local branch=$(echo "$cmd" | awk '{print $3}')
            if [[ -n "$remote" ]] && [[ -n "$branch" ]]; then
                git log "$remote/$branch"..HEAD --oneline 2>/dev/null || true
            fi
            ;;
        merge*|rebase*)
            log_info "Current branch status:"
            git status --short --branch
            ;;
        *)
            log_info "Current repository status:"
            git status --short
            ;;
    esac
    echo
}

execute_command() {
    local cmd="$1"
    
    if [[ "$DRY_RUN" == "true" ]]; then
        log_info "[DRY-RUN] Would execute: git $cmd"
        return 0
    fi
    
    log_info "Executing: git $cmd"
    
    # Execute and capture output
    if output=$(git $cmd 2>&1); then
        log_success "Command completed successfully"
        if [[ -n "$output" ]]; then
            echo "$output"
        fi
        return 0
    else
        log_error "Command failed with exit code $?"
        echo "$output"
        return 1
    fi
}

# Main execution flow
main() {
    if [[ -z "$GIT_COMMAND" ]]; then
        log_error "No git command specified"
        echo "Usage: $0 [OPTIONS] <command> [args...]"
        exit 1
    fi
    
    log_info "Git Safe Execution Wrapper"
    echo
    
    # Step 1: Verify we're in a git repo
    check_git_repo
    
    # Step 2: Check working tree state
    check_working_tree
    
    # Step 3: Create backup if requested
    create_backup_branch
    
    # Step 4: Show preview
    show_preview "$GIT_COMMAND"
    
    # Step 5: Confirm action
    confirm "Execute: git $GIT_COMMAND"
    
    # Step 6: Execute
    if execute_command "$GIT_COMMAND"; then
        echo
        log_success "Operation completed successfully"
        
        # Show post-execution status
        log_info "Current status:"
        git status --short --branch
    else
        echo
        log_error "Operation failed"
        exit 1
    fi
}

main "$@"
