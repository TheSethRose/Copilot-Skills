#!/usr/bin/env bash
#
# analyze_repo.sh - Analyze codebase and generate/update Copilot instructions
#
# Purpose: Systematically scan repository to discover patterns, workflows,
#          architecture, and integration points for AI agent guidance
#
# Usage:
#   analyze_repo.sh [OPTIONS]
#
# Options:
#   --output FILE      Save to specific path (default: .github/copilot-instructions.md)
#   --merge            Merge with existing instructions
#   --dry-run          Preview changes without saving
#   --verbose          Detailed analysis output
#   --detect-only      Only detect patterns, don't generate instructions
#
# Examples:
#   analyze_repo.sh
#   analyze_repo.sh --merge --dry-run
#   analyze_repo.sh --verbose --output custom-instructions.md
#

set -euo pipefail

# Colors
BLUE='\033[0;34m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Configuration
OUTPUT_FILE="${GITHUB_WORKSPACE:-.}/.github/copilot-instructions.md"
MERGE_MODE=false
DRY_RUN=false
VERBOSE=false
DETECT_ONLY=false

# Files/directories to always exclude (matches .gitignore patterns)
EXCLUDE_PATTERNS=(
    "node_modules"
    "__pycache__"
    ".venv"
    "venv"
    "ENV"
    "env"
    ".pytest_cache"
    ".coverage"
    "htmlcov"
    ".tox"
    "build"
    "dist"
    "*.egg-info"
    ".DS_Store"
    ".env"
    ".env.*"
    "*.log"
    ".vscode"
    ".idea"
    "*.pyc"
    "*.pyo"
    "*.pyd"
    "*.so"
    "*.swp"
    "*.swo"
    "*~"
    "package-lock.json"
    "yarn.lock"
    "*.bak"
    "*.tmp"
    "examples"
    "drafts"
)

# Build exclude args for find/grep commands
build_exclude_args() {
    local args=""
    for pattern in "${EXCLUDE_PATTERNS[@]}"; do
        args="$args -not -path '*/$pattern/*' -not -name '$pattern'"
    done
    echo "$args"
}

# Parse options
while [[ $# -gt 0 ]]; do
    case $1 in
        --output)
            OUTPUT_FILE="$2"
            shift 2
            ;;
        --merge)
            MERGE_MODE=true
            shift
            ;;
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --verbose)
            VERBOSE=true
            shift
            ;;
        --detect-only)
            DETECT_ONLY=true
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

log_error() {
    echo -e "${RED}✗${NC} $1"
}

verbose_log() {
    if [[ "$VERBOSE" == "true" ]]; then
        echo -e "${BLUE}→${NC} $1"
    fi
}

# Detect project type
detect_project_type() {
    local project_type=""
    local languages=()
    
    # Check for package.json (Node.js)
    if [[ -f "package.json" ]]; then
        project_type="node"
        languages+=("JavaScript")
        
        # Check for TypeScript
        if [[ -f "tsconfig.json" ]] || grep -q '"typescript"' package.json; then
            languages+=("TypeScript")
        fi
    fi
    
    # Check for Python
    if [[ -f "setup.py" ]] || [[ -f "pyproject.toml" ]] || [[ -f "requirements.txt" ]]; then
        [[ -z "$project_type" ]] && project_type="python"
        languages+=("Python")
    fi
    
    # Check for Go
    if [[ -f "go.mod" ]]; then
        [[ -z "$project_type" ]] && project_type="go"
        languages+=("Go")
    fi
    
    # Check for Java/Gradle
    if [[ -f "build.gradle" ]] || [[ -f "pom.xml" ]]; then
        [[ -z "$project_type" ]] && project_type="java"
        languages+=("Java")
    fi
    
    # Check for monorepo patterns
    if [[ -d "packages" ]] || [[ -d "apps" ]] || grep -q '"workspaces"' package.json 2>/dev/null; then
        project_type="${project_type}-monorepo"
    fi
    
    echo "${project_type:-unknown}"
}

# Detect frameworks
detect_frameworks() {
    local frameworks=()
    
    if [[ -f "package.json" ]]; then
        [[ $(grep -c '"react"' package.json) -gt 0 ]] && frameworks+=("React")
        [[ $(grep -c '"vue"' package.json) -gt 0 ]] && frameworks+=("Vue")
        [[ $(grep -c '"express"' package.json) -gt 0 ]] && frameworks+=("Express")
        [[ $(grep -c '"next"' package.json) -gt 0 ]] && frameworks+=("Next.js")
        [[ $(grep -c '"nestjs"' package.json) -gt 0 ]] && frameworks+=("NestJS")
    fi
    
    if [[ -f "pyproject.toml" ]] || [[ -f "requirements.txt" ]]; then
        grep -q "django" requirements.txt 2>/dev/null && frameworks+=("Django")
        grep -q "flask" requirements.txt 2>/dev/null && frameworks+=("Flask")
        grep -q "fastapi" requirements.txt 2>/dev/null && frameworks+=("FastAPI")
    fi
    
    printf '%s\n' "${frameworks[@]}"
}

# Detect testing frameworks
detect_test_framework() {
    if [[ -f "package.json" ]]; then
        grep -q '"jest"' package.json && echo "Jest" && return
        grep -q '"vitest"' package.json && echo "Vitest" && return
        grep -q '"mocha"' package.json && echo "Mocha" && return
    fi
    
    if [[ -f "pyproject.toml" ]] || [[ -f "requirements.txt" ]]; then
        grep -q "pytest" requirements.txt 2>/dev/null && echo "pytest" && return
        grep -q "unittest" requirements.txt 2>/dev/null && echo "unittest" && return
    fi
    
    echo "none"
}

# Detect code formatting tools
detect_formatters() {
    local formatters=()
    
    [[ -f ".prettierrc" ]] || [[ -f "prettier.config.js" ]] && formatters+=("Prettier")
    [[ -f ".eslintrc" ]] && formatters+=("ESLint")
    [[ -f ".pylintrc" ]] && formatters+=("Pylint")
    [[ -f "black.toml" ]] && formatters+=("Black")
    [[ -f ".golangci.yml" ]] && formatters+=("golangci-lint")
    
    printf '%s\n' "${formatters[@]}"
}

# Extract npm/yarn scripts
extract_scripts() {
    if [[ -f "package.json" ]]; then
        jq -r '.scripts | to_entries[] | "\(.key): \(.value)"' package.json 2>/dev/null || true
    fi
}

# Detect commit patterns from git history
detect_commit_patterns() {
    if [[ -d ".git" ]]; then
        # Check last 100 commits for patterns
        local commits=$(git log --oneline -100 2>/dev/null | awk '{print $1}' | while read commit; do
            git show --format=%B -s "$commit" 2>/dev/null | head -1
        done)
        
        # Check for conventional commits
        if echo "$commits" | grep -qE '^(feat|fix|docs|style|refactor|test|chore)(\(.+\))?:'; then
            echo "conventional-commits"
        fi
    fi
}

# Analyze directory structure
analyze_structure() {
    local structure_info=""
    
    structure_info+="$(printf '%-20s %s\n' "Root directories:" "")"
    ls -d */ 2>/dev/null | head -10 | while read dir; do
        structure_info+="$(printf '  - %s\n' "${dir%/}")"
    done
    
    # Check for specific patterns
    [[ -d "src" ]] && structure_info+="$(printf '  ✓ src/ directory\n')"
    [[ -d "tests" ]] || [[ -d "test" ]] && structure_info+="$(printf '  ✓ tests/ directory\n')"
    [[ -d ".github" ]] && structure_info+="$(printf '  ✓ .github/ (CI/CD)\n')"
    [[ -d "docs" ]] && structure_info+="$(printf '  ✓ docs/ (documentation)\n')"
    
    echo "$structure_info"
}

# Detect integration points
detect_integrations() {
    local integrations_json="[]"
    local exclude_args=$(build_exclude_args)
    
    # Database detection (exclude ignored directories)
    if eval "find . -type f \( -name '*.json' -o -name '*.txt' -o -name '*.toml' \) $exclude_args -exec grep -l 'mongoose\|prisma\|sequelize\|psycopg2' {} \;" 2>/dev/null | grep -q .; then
        integrations_json=$(echo "$integrations_json" | jq '. += [{"type": "database", "detected": true}]')
    fi
    
    # API patterns (exclude ignored directories)
    if eval "find . -type f \( -name '*.ts' -o -name '*.js' -o -name '*.py' \) $exclude_args -exec grep -l 'axios\|fetch\|requests\|http' {} \;" 2>/dev/null | grep -q .; then
        integrations_json=$(echo "$integrations_json" | jq '. += [{"type": "external_api", "detected": true}]')
    fi
    
    # Auth patterns (exclude ignored directories)
    if eval "find . -type f \( -name '*.json' -o -name '*.ts' -o -name '*.js' \) $exclude_args -exec grep -l 'jwt\|oauth\|passport\|auth' {} \;" 2>/dev/null | grep -q .; then
        integrations_json=$(echo "$integrations_json" | jq '. += [{"type": "authentication", "detected": true}]')
    fi
    
    echo "$integrations_json"
}

# Generate instruction file
generate_instructions() {
    local project_type="$1"
    local frameworks="$2"
    local test_framework="$3"
    
    cat > "$OUTPUT_FILE" <<'EOF'
# Copilot Instructions

This file guides AI agents (Copilot, Claude, etc.) to work effectively in this codebase.

## Project Overview

EOF

    # Add detected information
    echo "**Project Type**: $project_type" >> "$OUTPUT_FILE"
    echo "**Frameworks**: $frameworks" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
    
    cat >> "$OUTPUT_FILE" <<'EOF'
## Technology Stack

EOF

    detect_formatters | while read formatter; do
        echo "- $formatter" >> "$OUTPUT_FILE"
    done
    
    [[ "$test_framework" != "none" ]] && echo "- **Testing**: $test_framework" >> "$OUTPUT_FILE"
    
    cat >> "$OUTPUT_FILE" <<'EOF'

## Project Structure

EOF

    analyze_structure >> "$OUTPUT_FILE"
    
    cat >> "$OUTPUT_FILE" <<'EOF'

## Development Workflows

### Build & Run

EOF

    extract_scripts | while read script; do
        echo "- \`$script\`" >> "$OUTPUT_FILE"
    done
    
    cat >> "$OUTPUT_FILE" <<'EOF'

## Code Patterns & Conventions

EOF

    if detect_commit_patterns | grep -q "conventional"; then
        echo "- **Commits**: Conventional Commits format (feat, fix, docs, etc.)" >> "$OUTPUT_FILE"
    fi
    
    cat >> "$OUTPUT_FILE" <<'EOF'

## Key Resources

- **Documentation**: See \`docs/\` directory
- **Tests**: Located in \`tests/\` or \`__tests__/\` directories
- **Configuration**: Check root config files (.env.example, config/)

EOF

    log_success "Generated $OUTPUT_FILE"
}
# Display analysis results to terminal
display_analysis() {
    local project_type="$1"
    local frameworks_list="$2"
    local test_framework="$3"
    
    echo
    echo "Analysis Results:"
    echo "─────────────────────────────────────────"
    echo "Project Type: $project_type"
    echo "Languages: $(detect_frameworks | head -1 || echo 'Unknown')"
    echo "Frameworks: $frameworks_list"
    echo "Testing Framework: $test_framework"
    echo
    
    # Show detected patterns
    if detect_commit_patterns | grep -q "conventional"; then
        echo "Patterns Detected:"
        echo "  ✓ Conventional Commits"
    fi
    
    echo "─────────────────────────────────────────"
}
# Main execution
main() {
    log_info "Copilot Instructions Generator - Repository Analysis"
    echo
    
    # Check if we're in a git repo
    if ! git rev-parse --git-dir > /dev/null 2>&1; then
        log_warning "Not in a git repository, analysis may be incomplete"
    fi
    
    # Detect project type
    log_info "Analyzing repository structure..."
    local project_type=$(detect_project_type)
    verbose_log "Detected project type: $project_type"
    
    # Detect frameworks
    local frameworks_list=$(detect_frameworks | paste -sd, -)
    [[ -z "$frameworks_list" ]] && frameworks_list="(none detected)"
    verbose_log "Detected frameworks: $frameworks_list"
    
    # Detect test framework
    local test_framework=$(detect_test_framework)
    verbose_log "Detected test framework: $test_framework"
    
    # Display analysis results to terminal
    display_analysis "$project_type" "$frameworks_list" "$test_framework"
    
    if [[ "$DETECT_ONLY" == "true" ]]; then
        log_success "Analysis complete (detection-only mode)"
        exit 0
    fi
    
    # Generate instructions
    if [[ "$DRY_RUN" == "true" ]]; then
        log_info "[DRY-RUN] Would generate: $OUTPUT_FILE"
        echo
        echo "Preview:"
        echo "────────────────────────────────────"
        generate_instructions "$project_type" "$frameworks_list" "$test_framework" | head -30
        echo "────────────────────────────────────"
    else
        generate_instructions "$project_type" "$frameworks_list" "$test_framework"
    fi
    
    echo
    log_success "Repository analysis complete"
}

main "$@"
