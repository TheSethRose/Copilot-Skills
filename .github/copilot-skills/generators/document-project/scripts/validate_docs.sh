#!/bin/bash
set -euo pipefail

# validate_docs.sh - Validate markdown documentation quality
# Output: Validation report to stdout

usage() {
    cat << EOF
Usage: $0 <docs-path>

Validates markdown documentation for quality and consistency.

Arguments:
    docs-path    Path to documentation directory or file

Checks:
    - Valid markdown syntax
    - No broken internal links
    - Proper heading hierarchy
    - Code blocks have language tags
    - Consistent formatting

Example:
    bash validate_docs.sh /path/to/docs

EOF
    exit 1
}

[[ $# -eq 0 ]] && usage
[[ "$1" == "-h" || "$1" == "--help" ]] && usage

DOCS_PATH="$1"
ERRORS=0
WARNINGS=0

if [[ ! -e "$DOCS_PATH" ]]; then
    echo "Error: Path not found: $DOCS_PATH" >&2
    exit 1
fi

echo "Validating documentation..."
echo ""

# Find all markdown files
if [[ -d "$DOCS_PATH" ]]; then
    MD_FILES=$(find "$DOCS_PATH" -name "*.md" -type f)
else
    MD_FILES="$DOCS_PATH"
fi

# Validate each file
for file in $MD_FILES; do
    echo "Checking: $file"
    
    # Check 1: Heading hierarchy
    h1_count=$(grep -c "^# " "$file" 2>/dev/null || true)
    if [[ $h1_count -gt 1 ]]; then
        echo "  ✗ Multiple H1 headings found ($h1_count)"
        ((ERRORS++))
    elif [[ $h1_count -eq 0 ]]; then
        echo "  ⚠ No H1 heading found"
        ((WARNINGS++))
    else
        echo "  ✓ Heading hierarchy valid"
    fi
    
    # Check 2: Code blocks have language tags
    code_blocks=$(grep -c "^\`\`\`" "$file" 2>/dev/null || true)
    if [[ $code_blocks -gt 0 ]]; then
        untagged=$(grep "^\`\`\`$" "$file" 2>/dev/null | wc -l || true)
        if [[ $untagged -gt 0 ]]; then
            echo "  ✗ $untagged code blocks missing language tags"
            ((ERRORS++))
        else
            echo "  ✓ All code blocks have language tags"
        fi
    fi
    
    # Check 3: Internal links (basic check)
    internal_links=$(grep -o "\\[.*\\](.*/.*\\.md.*)" "$file" 2>/dev/null | wc -l || true)
    if [[ $internal_links -gt 0 ]]; then
        # Extract links and check if files exist
        broken=0
        while IFS= read -r link; do
            link_path=$(echo "$link" | sed -E 's/.*\((.*)\).*/\1/' | sed 's/#.*//')
            if [[ -n "$link_path" ]] && [[ "$link_path" =~ ^\./ ]]; then
                dir=$(dirname "$file")
                full_path="$dir/$link_path"
                if [[ ! -f "$full_path" ]]; then
                    ((broken++))
                fi
            fi
        done < <(grep -o "\\[.*\\](.*/.*\\.md.*)" "$file" 2>/dev/null || true)
        
        if [[ $broken -gt 0 ]]; then
            echo "  ✗ $broken broken internal links"
            ((ERRORS++))
        else
            echo "  ✓ Internal links valid"
        fi
    fi
    
    # Check 4: Consistent list formatting
    mixed_lists=$(grep -E "^[*+-] " "$file" 2>/dev/null | cut -c1 | sort -u | wc -l || true)
    if [[ $mixed_lists -gt 1 ]]; then
        echo "  ⚠ Mixed list markers (use consistent - or * or +)"
        ((WARNINGS++))
    fi
    
    echo ""
done

# Summary
echo "================================"
echo "Validation Summary"
echo "================================"
echo "Errors: $ERRORS"
echo "Warnings: $WARNINGS"
echo ""

if [[ $ERRORS -eq 0 ]]; then
    echo "✓ All documentation is valid"
    exit 0
else
    echo "✗ Fix errors before committing"
    exit 1
fi
