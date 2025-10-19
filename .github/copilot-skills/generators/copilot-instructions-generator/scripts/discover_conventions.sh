#!/usr/bin/env bash
#
# discover_conventions.sh - Find and parse existing AI instruction files
#
# Purpose: Scan repository for existing AI guidance files and consolidate them
#
# Usage:
#   discover_conventions.sh [OPTIONS]
#
# Options:
#   --parse             Parse and display content
#   --compare           Compare multiple files
#   --consolidate       Prepare consolidation into single file
#
# Examples:
#   discover_conventions.sh
#   discover_conventions.sh --parse
#   discover_conventions.sh --consolidate
#

set -euo pipefail

# Colors
BLUE='\033[0;34m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Configuration
PARSE_MODE=false
COMPARE_MODE=false
CONSOLIDATE_MODE=false

# Parse options
while [[ $# -gt 0 ]]; do
    case $1 in
        --parse)
            PARSE_MODE=true
            shift
            ;;
        --compare)
            COMPARE_MODE=true
            shift
            ;;
        --consolidate)
            CONSOLIDATE_MODE=true
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
}

# Find all convention files
find_convention_files() {
    local files=()
    
    # Standard locations (only if they exist and aren't in ignored dirs)
    [[ -f ".github/copilot-instructions.md" ]] && files+=(".github/copilot-instructions.md")
    [[ -f ".agent.md" ]] && files+=(".agent.md")
    [[ -f "AGENT.md" ]] && files+=("AGENT.md")
    [[ -f "AGENTS.md" ]] && files+=("AGENTS.md")
    [[ -f ".claude.md" ]] && files+=(".claude.md")
    [[ -f "CLAUDE.md" ]] && files+=("CLAUDE.md")
    [[ -f ".cursorrules" ]] && files+=(".cursorrules")
    [[ -f ".windsurfrules" ]] && files+=(".windsurfrules")
    [[ -f ".clinerules" ]] && files+=(".clinerules")
    
    # Directory-based conventions (exclude .vscode, .idea, node_modules, etc.)
    if [[ -d ".cursor/rules" ]]; then
        while IFS= read -r file; do
            files+=("$file")
        done < <(find .cursor/rules -type f -not -path '*/node_modules/*' -not -path '*/.venv/*' -not -path '*/venv/*' 2>/dev/null || true)
    fi
    
    if [[ -d ".windsurf/rules" ]]; then
        while IFS= read -r file; do
            files+=("$file")
        done < <(find .windsurf/rules -type f -not -path '*/node_modules/*' -not -path '*/.venv/*' -not -path '*/venv/*' 2>/dev/null || true)
    fi
    
    if [[ -d ".clinerules" ]]; then
        while IFS= read -r file; do
            files+=("$file")
        done < <(find .clinerules -type f -not -path '*/node_modules/*' -not -path '*/.venv/*' -not -path '*/venv/*' 2>/dev/null || true)
    fi
    
    # Check README for AI sections (skip if in examples/ or drafts/)
    if [[ -f "README.md" ]] && ! echo "README.md" | grep -q 'examples/\|drafts/'; then
        if grep -q "Copilot\|Claude\|Agent\|AI" README.md 2>/dev/null; then
            files+=("README.md (partial)")
        fi
    fi
    
    printf '%s\n' "${files[@]}"
}

# Display file summary
display_summary() {
    local file="$1"
    
    if [[ ! -f "$file" ]]; then
        return
    fi
    
    local size=$(wc -l < "$file" 2>/dev/null || echo "?")
    local mtime=$(stat -f "%Sm" -t "%Y-%m-%d" "$file" 2>/dev/null || echo "unknown")
    
    echo "  📄 $file"
    echo "     Lines: $size | Modified: $mtime"
}

# Parse and extract content
parse_file() {
    local file="$1"
    
    echo
    echo "════════════════════════════════════════════════"
    echo "File: $file"
    echo "════════════════════════════════════════════════"
    echo
    
    if [[ -f "$file" ]]; then
        head -50 "$file"
        
        local total_lines=$(wc -l < "$file" 2>/dev/null || echo "0")
        if [[ $total_lines -gt 50 ]]; then
            echo
            echo "... ($((total_lines - 50)) more lines)"
        fi
    else
        echo "File not found: $file"
    fi
    
    echo
}

# Compare files
compare_files() {
    local files=()
    
    while IFS= read -r file; do
        [[ -f "$file" ]] && files+=("$file")
    done < <(find_convention_files)
    
    if [[ ${#files[@]} -eq 0 ]]; then
        log_warning "No convention files found"
        return
    fi
    
    if [[ ${#files[@]} -eq 1 ]]; then
        log_info "Only one convention file found: ${files[0]}"
        return
    fi
    
    echo
    echo "Comparing ${#files[@]} convention files:"
    echo "════════════════════════════════════════════════"
    echo
    
    # Create temp files for comparison
    local temp_dir=$(mktemp -d)
    trap "rm -rf $temp_dir" EXIT
    
    # Extract text from each file, normalize
    for file in "${files[@]}"; do
        local outfile="$temp_dir/$(basename "$file" | tr '/' '_')"
        grep -v "^#\|^---\|^$" "$file" 2>/dev/null | sort | uniq > "$outfile" || true
    done
    
    # Find common content
    echo "Common patterns:"
    echo "─────────────────"
    
    # Find lines that appear in multiple files
    find "$temp_dir" -type f -exec cat {} \; | sort | uniq -c | sort -rn | awk '$1 > 1 {$1=""; print}' | head -20
    
    echo
    echo "Unique to each file:"
    echo "────────────────────"
    
    for file in "${files[@]}"; do
        local name=$(basename "$file")
        local outfile="$temp_dir/$(basename "$file" | tr '/' '_')"
        local count=$(wc -l < "$outfile" 2>/dev/null || echo "0")
        echo "  $name: $count unique lines"
    done
}

# Prepare consolidation
prepare_consolidation() {
    local files=()
    
    while IFS= read -r file; do
        [[ -f "$file" ]] && files+=("$file")
    done < <(find_convention_files)
    
    if [[ ${#files[@]} -eq 0 ]]; then
        log_warning "No convention files found to consolidate"
        return
    fi
    
    log_info "Found ${#files[@]} convention files to consolidate"
    echo
    
    # Create consolidated output
    local output_file=".github/copilot-instructions-consolidated.md"
    
    {
        echo "# Consolidated Copilot Instructions"
        echo
        echo "This file consolidates AI guidance from multiple sources:"
        echo
        
        for file in "${files[@]}"; do
            echo "## From: $file"
            echo
            cat "$file" 2>/dev/null || echo "(file not readable)"
            echo
            echo "────────────────────────────────────────────"
            echo
        done
        
        echo "## Consolidation Notes"
        echo
        echo "This file was generated by consolidating the following sources:"
        printf '%s\n' "${files[@]}" | sed 's/^/- /'
        echo
        echo "Generated: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
        
    } > "$output_file"
    
    log_success "Created: $output_file"
    log_info "Review and edit consolidation, then replace individual files"
}

# Main execution
main() {
    log_info "Convention File Discovery"
    echo
    
    # Find all convention files
    echo "Scanning for AI convention files..."
    local files_found=false
    
    while IFS= read -r file; do
        display_summary "$file"
        files_found=true
    done < <(find_convention_files)
    
    if [[ "$files_found" == "false" ]]; then
        log_warning "No convention files found"
        exit 0
    fi
    
    echo
    
    # Handle modes
    if [[ "$PARSE_MODE" == "true" ]]; then
        log_info "Parsing convention files..."
        
        while IFS= read -r file; do
            parse_file "$file"
        done < <(find_convention_files)
    fi
    
    if [[ "$COMPARE_MODE" == "true" ]]; then
        compare_files
    fi
    
    if [[ "$CONSOLIDATE_MODE" == "true" ]]; then
        prepare_consolidation
    fi
    
    log_success "Convention discovery complete"
}

main "$@"
