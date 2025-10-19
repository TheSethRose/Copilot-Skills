#!/usr/bin/env bash
#
# conflict_resolver.sh - Interactive conflict resolution assistant
#
# Purpose: Guide users through merge/rebase conflicts with structured options
#          and validation
#
# Usage:
#   conflict_resolver.sh [OPTIONS]
#
# Options:
#   --summary          Show conflict summary and exit
#   --strategy STRAT   Auto-apply strategy (ours/theirs)
#   --validate         Validate conflict markers are resolved
#
# Examples:
#   conflict_resolver.sh
#   conflict_resolver.sh --summary
#   conflict_resolver.sh --strategy theirs
#

set -euo pipefail

# Colors
BLUE='\033[0;34m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Configuration
SHOW_SUMMARY_ONLY=false
AUTO_STRATEGY=""
VALIDATE_ONLY=false

# Parse options
while [[ $# -gt 0 ]]; do
    case $1 in
        --summary)
            SHOW_SUMMARY_ONLY=true
            shift
            ;;
        --strategy)
            AUTO_STRATEGY="$2"
            shift 2
            ;;
        --validate)
            VALIDATE_ONLY=true
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

check_conflicts() {
    # Check if we're in a merge/rebase
    local merge_head=false
    local rebase_head=false
    
    if [[ -f .git/MERGE_HEAD ]]; then
        merge_head=true
    fi
    
    if [[ -d .git/rebase-merge ]] || [[ -d .git/rebase-apply ]]; then
        rebase_head=true
    fi
    
    if [[ "$merge_head" == "false" ]] && [[ "$rebase_head" == "false" ]]; then
        log_error "No merge or rebase in progress"
        exit 1
    fi
    
    # Get conflicted files
    local conflicts=$(git diff --name-only --diff-filter=U)
    
    if [[ -z "$conflicts" ]]; then
        log_success "No conflicts found"
        exit 0
    fi
    
    echo "$conflicts"
}

show_conflict_summary() {
    log_info "Conflict Summary"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo
    
    local conflicts=$(check_conflicts)
    local count=$(echo "$conflicts" | wc -l | tr -d ' ')
    
    echo "Total conflicted files: $count"
    echo
    
    echo "$conflicts" | while read -r file; do
        echo "📄 $file"
        
        # Count conflict markers
        local marker_count=$(grep -c "^<<<<<<< " "$file" 2>/dev/null || echo "0")
        echo "   Conflicts: $marker_count"
        
        # Show conflict hunks
        if [[ $marker_count -gt 0 ]] && [[ $marker_count -le 3 ]]; then
            echo "   Preview:"
            grep -A 5 "^<<<<<<< " "$file" | head -20 | sed 's/^/   /'
        fi
        echo
    done
}

validate_resolution() {
    log_info "Validating conflict resolution..."
    
    local conflicts=$(git diff --name-only --diff-filter=U)
    
    if [[ -z "$conflicts" ]]; then
        log_success "All conflicts resolved"
        return 0
    fi
    
    log_error "Still have unresolved conflicts:"
    echo "$conflicts"
    return 1
}

check_conflict_markers() {
    local file="$1"
    
    if grep -q "^<<<<<<< " "$file" 2>/dev/null; then
        log_error "File still contains conflict markers: $file"
        return 1
    fi
    
    if grep -q "^=======$" "$file" 2>/dev/null; then
        log_error "File still contains conflict markers: $file"
        return 1
    fi
    
    if grep -q "^>>>>>>> " "$file" 2>/dev/null; then
        log_error "File still contains conflict markers: $file"
        return 1
    fi
    
    log_success "No conflict markers in: $file"
    return 0
}

apply_strategy() {
    local strategy="$1"
    local file="$2"
    
    case "$strategy" in
        ours)
            log_info "Accepting 'ours' for: $file"
            git checkout --ours "$file"
            git add "$file"
            log_success "Applied strategy: ours"
            ;;
        theirs)
            log_info "Accepting 'theirs' for: $file"
            git checkout --theirs "$file"
            git add "$file"
            log_success "Applied strategy: theirs"
            ;;
        *)
            log_error "Unknown strategy: $strategy"
            return 1
            ;;
    esac
}

show_conflict_diff() {
    local file="$1"
    
    echo
    log_info "Conflict details for: $file"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    
    # Show both versions
    echo
    echo "=== OURS (current branch) ==="
    git show :2:"$file" 2>/dev/null || echo "(binary file or unavailable)"
    
    echo
    echo "=== THEIRS (incoming branch) ==="
    git show :3:"$file" 2>/dev/null || echo "(binary file or unavailable)"
    
    echo
    echo "=== CURRENT STATE WITH MARKERS ==="
    cat "$file"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
}

interactive_resolve() {
    local file="$1"
    
    while true; do
        echo
        log_info "Resolving: $file"
        echo
        echo "Options:"
        echo "  1) Accept ours (current branch)"
        echo "  2) Accept theirs (incoming branch)"
        echo "  3) View conflict details"
        echo "  4) Edit manually (opens in editor)"
        echo "  5) Skip this file"
        echo "  q) Quit"
        echo
        
        read -p "Choose option [1-5/q]: " -n 1 -r
        echo
        
        case $REPLY in
            1)
                apply_strategy "ours" "$file"
                return 0
                ;;
            2)
                apply_strategy "theirs" "$file"
                return 0
                ;;
            3)
                show_conflict_diff "$file"
                ;;
            4)
                ${EDITOR:-vim} "$file"
                
                if check_conflict_markers "$file"; then
                    git add "$file"
                    log_success "File marked as resolved"
                    return 0
                else
                    log_warning "File still has conflict markers"
                fi
                ;;
            5)
                log_info "Skipped: $file"
                return 0
                ;;
            q|Q)
                log_info "Quitting conflict resolution"
                exit 0
                ;;
            *)
                log_error "Invalid option"
                ;;
        esac
    done
}

continue_operation() {
    echo
    log_info "All conflicts resolved. Ready to continue."
    echo
    
    # Determine operation type
    if [[ -f .git/MERGE_HEAD ]]; then
        echo "To complete merge:"
        echo "  git commit"
    elif [[ -d .git/rebase-merge ]] || [[ -d .git/rebase-apply ]]; then
        echo "To continue rebase:"
        echo "  git rebase --continue"
    fi
    
    echo
    read -p "Continue automatically? [y/N] " -n 1 -r
    echo
    
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        if [[ -f .git/MERGE_HEAD ]]; then
            git commit --no-edit
            log_success "Merge completed"
        elif [[ -d .git/rebase-merge ]] || [[ -d .git/rebase-apply ]]; then
            git rebase --continue
            log_success "Rebase continued"
        fi
    fi
}

main() {
    log_info "Git Conflict Resolver"
    echo
    
    # Check for conflicts
    local conflicts=$(check_conflicts)
    
    # Handle specific modes
    if [[ "$SHOW_SUMMARY_ONLY" == "true" ]]; then
        show_conflict_summary
        exit 0
    fi
    
    if [[ "$VALIDATE_ONLY" == "true" ]]; then
        validate_resolution
        exit $?
    fi
    
    # Auto-strategy mode
    if [[ -n "$AUTO_STRATEGY" ]]; then
        echo "$conflicts" | while read -r file; do
            apply_strategy "$AUTO_STRATEGY" "$file"
        done
        
        if validate_resolution; then
            continue_operation
        fi
        exit 0
    fi
    
    # Interactive mode
    show_conflict_summary
    
    echo "$conflicts" | while read -r file; do
        interactive_resolve "$file"
    done
    
    # Final validation
    if validate_resolution; then
        continue_operation
    else
        log_warning "Some conflicts remain unresolved"
        exit 1
    fi
}

main "$@"
