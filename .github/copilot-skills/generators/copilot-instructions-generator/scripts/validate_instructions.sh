#!/usr/bin/env bash
#
# validate_instructions.sh - Validate generated Copilot instructions
#
# Purpose: Check that instructions meet quality standards (conciseness,
#          specificity, no generic advice, actionable content)
#
# Usage:
#   validate_instructions.sh [OPTIONS]
#
# Options:
#   --file FILE         Validate specific file
#   --strict            Enforce strict guidelines
#
# Examples:
#   validate_instructions.sh
#   validate_instructions.sh --file .github/copilot-instructions.md
#   validate_instructions.sh --strict
#

set -euo pipefail

# Colors
BLUE='\033[0;34m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Configuration
INSTRUCTION_FILE=".github/copilot-instructions.md"
STRICT_MODE=false
ISSUES=0
WARNINGS=0

# Parse options
while [[ $# -gt 0 ]]; do
    case $1 in
        --file)
            INSTRUCTION_FILE="$2"
            shift 2
            ;;
        --strict)
            STRICT_MODE=true
            shift
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Utility functions
log_info() {
    echo -e "${BLUE}ℹ${NC} $1"
}

log_success() {
    echo -e "${GREEN}✓${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
    ((WARNINGS++))
}

log_error() {
    echo -e "${RED}✗${NC} $1"
    ((ISSUES++))
}

# Check file exists
check_file_exists() {
    if [[ ! -f "$INSTRUCTION_FILE" ]]; then
        log_error "File not found: $INSTRUCTION_FILE"
        exit 1
    fi
    log_success "Found: $INSTRUCTION_FILE"
}

# Check conciseness
check_conciseness() {
    local line_count=$(wc -l < "$INSTRUCTION_FILE")
    
    if [[ $line_count -gt 200 ]]; then
        log_error "Too verbose ($line_count lines, target: <150)"
        return 1
    elif [[ $line_count -gt 150 ]]; then
        log_warning "Somewhat verbose ($line_count lines, target: <150)"
        return 0
    else
        log_success "Good length ($line_count lines)"
        return 0
    fi
}

# Check for generic advice
check_generic_advice() {
    local generic_patterns=(
        "write.*tests"
        "handle.*errors"
        "use.*best.*practices"
        "follow.*convention"
        "always.*check"
        "make.*sure"
        "remember.*to"
    )
    
    local found_generic=false
    
    for pattern in "${generic_patterns[@]}"; do
        if grep -qi "$pattern" "$INSTRUCTION_FILE"; then
            log_warning "Found generic advice: '$pattern'"
            found_generic=true
        fi
    done
    
    if [[ "$found_generic" == "false" ]]; then
        log_success "No generic advice patterns detected"
        return 0
    fi
    return 1
}

# Check for specific examples
check_specific_examples() {
    local example_count=$(grep -c '`[^`]*`' "$INSTRUCTION_FILE" || echo "0")
    
    if [[ $example_count -eq 0 ]]; then
        log_error "No code examples or file paths referenced"
        return 1
    elif [[ $example_count -lt 3 ]]; then
        log_warning "Few examples ($example_count, target: 5+)"
        return 0
    else
        log_success "Good example count ($example_count)"
        return 0
    fi
}

# Check for broken file references
check_file_references() {
    local broken_refs=0
    
    # Extract file paths from backticks (using basic grep, not -P)
    while IFS= read -r line; do
        # Extract paths like `src/file.ts` or `.github/config.json`
        # Look for backticks with paths (simple pattern match)
        local files=$(echo "$line" | grep -o '\`[^`]*\`' | tr -d '`' | grep -E '^\.?/' || true)
        
        while IFS= read -r file; do
            if [[ -n "$file" ]] && [[ ! -f "$file" ]] && [[ ! -d "$file" ]]; then
                log_warning "Broken reference: $file"
                ((broken_refs++))
            fi
        done <<< "$files"
    done < "$INSTRUCTION_FILE"
    
    if [[ $broken_refs -eq 0 ]]; then
        log_success "All file references valid"
        return 0
    else
        log_warning "Found $broken_refs broken file references"
        return 1
    fi
}

# Check for actionable content
check_actionable_content() {
    local sections_found=0
    
    # Look for key sections
    [[ $(grep -c "^##" "$INSTRUCTION_FILE") -gt 0 ]] && ((sections_found++))
    [[ $(grep -c "^###" "$INSTRUCTION_FILE") -gt 0 ]] && ((sections_found++))
    
    if [[ $sections_found -lt 3 ]]; then
        log_warning "Few sections ($sections_found, target: 5+)"
        return 0
    fi
    
    # Check for action verbs
    if grep -qi "run\|execute\|add\|create\|modify\|configure" "$INSTRUCTION_FILE"; then
        log_success "Contains actionable directives"
        return 0
    else
        log_warning "May lack actionable directives"
        return 1
    fi
}

# Check structure quality
check_structure() {
    local has_intro=false
    local has_stack=false
    local has_workflow=false
    
    [[ $(grep -i "project\|overview" "$INSTRUCTION_FILE" | wc -l) -gt 0 ]] && has_intro=true
    [[ $(grep -i "technology\|framework\|language" "$INSTRUCTION_FILE" | wc -l) -gt 0 ]] && has_stack=true
    [[ $(grep -i "workflow\|build\|test\|run" "$INSTRUCTION_FILE" | wc -l) -gt 0 ]] && has_workflow=true
    
    if [[ "$has_intro" == "true" ]] && [[ "$has_stack" == "true" ]] && [[ "$has_workflow" == "true" ]]; then
        log_success "Good structural organization"
        return 0
    else
        log_warning "Missing key sections (intro: $has_intro, stack: $has_stack, workflow: $has_workflow)"
        return 1
    fi
}

# Main execution
main() {
    log_info "Copilot Instructions Validator"
    echo
    
    # Check file exists
    check_file_exists
    echo
    
    # Run validations
    log_info "Running quality checks..."
    echo
    
    check_conciseness
    check_generic_advice
    check_specific_examples
    check_file_references
    check_actionable_content
    check_structure
    
    echo
    echo "────────────────────────────────"
    echo "Validation Summary"
    echo "────────────────────────────────"
    echo "Issues: $ISSUES"
    echo "Warnings: $WARNINGS"
    echo
    
    if [[ $ISSUES -eq 0 ]]; then
        log_success "Instructions meet quality standards"
        exit_code=0
    elif [[ $ISSUES -le 2 ]]; then
        log_warning "Instructions acceptable with minor issues"
        exit_code=0
    else
        log_error "Instructions need review"
        exit_code=1
    fi
    
    exit $exit_code
}

main "$@"
