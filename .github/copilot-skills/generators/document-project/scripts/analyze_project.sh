#!/bin/bash
set -euo pipefail

# analyze_project.sh - Detect project metadata for documentation
# Output: JSON with project type, language, framework, visibility

usage() {
    cat << EOF
Usage: $0 <project-path>

Analyzes a project and outputs metadata for documentation generation.

Arguments:
    project-path    Path to the project root directory

Output: JSON with project metadata

Example:
    bash analyze_project.sh /path/to/project

EOF
    exit 1
}

[[ $# -eq 0 ]] && usage
[[ "$1" == "-h" || "$1" == "--help" ]] && usage

PROJECT_PATH="$1"

if [[ ! -d "$PROJECT_PATH" ]]; then
    echo "Error: Directory not found: $PROJECT_PATH" >&2
    exit 1
fi

# Initialize variables
PROJECT_TYPE="unknown"
LANGUAGE="unknown"
FRAMEWORK="none"
VISIBILITY="closed-source"
HAS_DOCS=false
SUGGESTED_TEMPLATE="minimal"

# Detect language and framework
detect_language() {
    if [[ -f "$PROJECT_PATH/package.json" ]]; then
        LANGUAGE="javascript"
        
        # Check for TypeScript
        if grep -q '"typescript"' "$PROJECT_PATH/package.json" 2>/dev/null; then
            LANGUAGE="typescript"
        fi
        
        # Detect framework
        if grep -q '"next"' "$PROJECT_PATH/package.json" 2>/dev/null; then
            FRAMEWORK="nextjs"
            PROJECT_TYPE="application"
        elif grep -q '"react"' "$PROJECT_PATH/package.json" 2>/dev/null; then
            FRAMEWORK="react"
            PROJECT_TYPE="application"
        elif grep -q '"express"' "$PROJECT_PATH/package.json" 2>/dev/null; then
            FRAMEWORK="express"
            PROJECT_TYPE="service"
        elif grep -q '"bin"' "$PROJECT_PATH/package.json" 2>/dev/null; then
            PROJECT_TYPE="cli-tool"
        else
            PROJECT_TYPE="library"
        fi
        
    elif [[ -f "$PROJECT_PATH/setup.py" ]] || [[ -f "$PROJECT_PATH/pyproject.toml" ]]; then
        LANGUAGE="python"
        
        # Check for frameworks
        if [[ -f "$PROJECT_PATH/manage.py" ]]; then
            FRAMEWORK="django"
            PROJECT_TYPE="application"
        elif grep -q "flask" "$PROJECT_PATH/setup.py" 2>/dev/null || \
             grep -q "flask" "$PROJECT_PATH/pyproject.toml" 2>/dev/null; then
            FRAMEWORK="flask"
            PROJECT_TYPE="application"
        elif grep -q "console_scripts" "$PROJECT_PATH/setup.py" 2>/dev/null; then
            PROJECT_TYPE="cli-tool"
        else
            PROJECT_TYPE="library"
        fi
        
    elif [[ -f "$PROJECT_PATH/go.mod" ]]; then
        LANGUAGE="go"
        
        # Check for CLI tools (Cobra, etc.)
        if grep -q "cobra" "$PROJECT_PATH/go.mod" 2>/dev/null; then
            FRAMEWORK="cobra"
            PROJECT_TYPE="cli-tool"
        elif [[ -f "$PROJECT_PATH/main.go" ]] && grep -q "func main()" "$PROJECT_PATH/main.go" 2>/dev/null; then
            if grep -q "http\\.ListenAndServe" "$PROJECT_PATH/main.go" 2>/dev/null; then
                PROJECT_TYPE="service"
            else
                PROJECT_TYPE="application"
            fi
        else
            PROJECT_TYPE="library"
        fi
        
    elif [[ -f "$PROJECT_PATH/Cargo.toml" ]]; then
        LANGUAGE="rust"
        
        # Check for binary vs library
        if grep -q "\\[\\[bin\\]\\]" "$PROJECT_PATH/Cargo.toml" 2>/dev/null; then
            PROJECT_TYPE="cli-tool"
        else
            PROJECT_TYPE="library"
        fi
    fi
}

# Detect visibility (open-source vs closed-source)
detect_visibility() {
    # Check for LICENSE file
    if [[ -f "$PROJECT_PATH/LICENSE" ]] || \
       [[ -f "$PROJECT_PATH/LICENSE.md" ]] || \
       [[ -f "$PROJECT_PATH/LICENSE.txt" ]]; then
        VISIBILITY="open-source"
    fi
    
    # Check for public repository indicators
    if [[ -f "$PROJECT_PATH/CONTRIBUTING.md" ]] || \
       [[ -f "$PROJECT_PATH/CODE_OF_CONDUCT.md" ]]; then
        VISIBILITY="open-source"
    fi
}

# Check for existing documentation
check_existing_docs() {
    if [[ -d "$PROJECT_PATH/docs" ]] && [[ -n "$(ls -A "$PROJECT_PATH/docs" 2>/dev/null)" ]]; then
        HAS_DOCS=true
    fi
}

# Suggest template based on analysis
suggest_template() {
    if [[ "$VISIBILITY" == "open-source" ]]; then
        SUGGESTED_TEMPLATE="open-source"
    elif [[ "$PROJECT_TYPE" == "library" ]] || [[ "$PROJECT_TYPE" == "service" ]]; then
        SUGGESTED_TEMPLATE="standard"
    else
        SUGGESTED_TEMPLATE="minimal"
    fi
}

# Run detection
detect_language
detect_visibility
check_existing_docs
suggest_template

# Output JSON
cat << EOF
{
  "project_type": "$PROJECT_TYPE",
  "language": "$LANGUAGE",
  "framework": "$FRAMEWORK",
  "visibility": "$VISIBILITY",
  "has_docs": $HAS_DOCS,
  "suggested_template": "$SUGGESTED_TEMPLATE"
}
EOF

exit 0
