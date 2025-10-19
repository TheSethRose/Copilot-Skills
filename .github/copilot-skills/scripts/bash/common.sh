#!/usr/bin/env bash
# Common functions and variables for all scripts

# Get repository root, with fallback for non-git repositories
get_repo_root() {
    if git rev-parse --show-toplevel >/dev/null 2>&1; then
        git rev-parse --show-toplevel
    else
        # Fall back to script location for non-git repos
        local script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
        (cd "$script_dir/../../.." && pwd)
    fi
}

# Get current branch, with fallback for non-git repositories
get_current_branch() {
    # First check if SPECIFY_FEATURE environment variable is set
    if [[ -n "${SPECIFY_FEATURE:-}" ]]; then
        echo "$SPECIFY_FEATURE"
        return
    fi

    # Then check git if available
    if git rev-parse --abbrev-ref HEAD >/dev/null 2>&1; then
        git rev-parse --abbrev-ref HEAD
        return
    fi

    # For non-git repos, try to find the latest feature directory
    local repo_root=$(get_repo_root)
    local specs_dir="$repo_root/specs"

    if [[ -d "$specs_dir" ]]; then
        local latest_feature=""
        local highest=0

        for dir in "$specs_dir"/*; do
            if [[ -d "$dir" ]]; then
                local dirname=$(basename "$dir")
                if [[ "$dirname" =~ ^([0-9]{3})- ]]; then
                    local number=${BASH_REMATCH[1]}
                    number=$((10#$number))
                    if [[ "$number" -gt "$highest" ]]; then
                        highest=$number
                        latest_feature=$dirname
                    fi
                fi
            fi
        done

        if [[ -n "$latest_feature" ]]; then
            echo "$latest_feature"
            return
        fi
    fi

    echo "main"  # Final fallback
}

# Check if we have git available
has_git() {
    git rev-parse --show-toplevel >/dev/null 2>&1
}

check_feature_branch() {
    local branch="$1"
    local has_git_repo="$2"

    # For non-git repos, we can't enforce branch naming but still provide output
    if [[ "$has_git_repo" != "true" ]]; then
        echo "[specify] Warning: Git repository not detected; skipped branch validation" >&2
        return 0
    fi

    if [[ ! "$branch" =~ ^[0-9]{3}- ]]; then
        echo "ERROR: Not on a feature branch. Current branch: $branch" >&2
        echo "Feature branches should be named like: 001-feature-name" >&2
        return 1
    fi

    return 0
}

get_feature_dir() { echo "$1/specs/$2"; }

# Find feature directory by numeric prefix instead of exact branch match
# This allows multiple branches to work on the same spec (e.g., 004-fix-bug, 004-add-feature)
find_feature_dir_by_prefix() {
    local repo_root="$1"
    local branch_name="$2"
    local specs_dir="$repo_root/specs"

    # Extract numeric prefix from branch (e.g., "004" from "004-whatever")
    if [[ ! "$branch_name" =~ ^([0-9]{3})- ]]; then
        # If branch doesn't have numeric prefix, fall back to exact match
        echo "$specs_dir/$branch_name"
        return
    fi

    local prefix="${BASH_REMATCH[1]}"

    # Search for directories in specs/ that start with this prefix
    local matches=()
    if [[ -d "$specs_dir" ]]; then
        for dir in "$specs_dir"/"$prefix"-*; do
            if [[ -d "$dir" ]]; then
                matches+=("$(basename "$dir")")
            fi
        done
    fi

    # Handle results
    if [[ ${#matches[@]} -eq 0 ]]; then
        # No match found - return the branch name path (will fail later with clear error)
        echo "$specs_dir/$branch_name"
    elif [[ ${#matches[@]} -eq 1 ]]; then
        # Exactly one match - perfect!
        echo "$specs_dir/${matches[0]}"
    else
        # Multiple matches - this shouldn't happen with proper naming convention
        echo "ERROR: Multiple spec directories found with prefix '$prefix': ${matches[*]}" >&2
        echo "Please ensure only one spec directory exists per numeric prefix." >&2
        echo "$specs_dir/$branch_name"  # Return something to avoid breaking the script
    fi
}

get_feature_paths() {
    local repo_root=$(get_repo_root)
    local current_branch=$(get_current_branch)
    local has_git_repo="false"

    if has_git; then
        has_git_repo="true"
    fi

    # Use prefix-based lookup to support multiple branches per spec
    local feature_dir=$(find_feature_dir_by_prefix "$repo_root" "$current_branch")

    cat <<EOF
REPO_ROOT='$repo_root'
CURRENT_BRANCH='$current_branch'
HAS_GIT='$has_git_repo'
FEATURE_DIR='$feature_dir'
FEATURE_SPEC='$feature_dir/spec.md'
IMPL_PLAN='$feature_dir/plan.md'
TASKS='$feature_dir/tasks.md'
RESEARCH='$feature_dir/research.md'
DATA_MODEL='$feature_dir/data-model.md'
QUICKSTART='$feature_dir/quickstart.md'
CONTRACTS_DIR='$feature_dir/contracts'
EOF
}

check_file() { [[ -f "$1" ]] && echo "  ✓ $2" || echo "  ✗ $2"; }
check_dir() { [[ -d "$1" && -n $(ls -A "$1" 2>/dev/null) ]] && echo "  ✓ $2" || echo "  ✗ $2"; }

#######################################
# SKILL-SPECIFIC FUNCTIONS
#######################################

#######################################
# Log a skill-related event with timestamp
# Globals:
#   None
# Arguments:
#   $1 - Log level (INFO, WARN, ERROR, SUCCESS)
#   $2 - Message to log
# Outputs:
#   Formatted log message to stderr
#######################################
log_skill_event() {
    local level="$1"
    local message="$2"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    local color=""
    local reset="\033[0m"
    
    case "$level" in
        INFO)    color="\033[0;36m" ;;  # Cyan
        WARN)    color="\033[0;33m" ;;  # Yellow
        ERROR)   color="\033[0;31m" ;;  # Red
        SUCCESS) color="\033[0;32m" ;;  # Green
        *)       color="" ;;
    esac
    
    echo -e "${color}[${level}]${reset} ${timestamp} - ${message}" >&2
}

#######################################
# Validate skill name format
# Arguments:
#   $1 - Skill name to validate
# Returns:
#   0 if valid, 1 if invalid
#######################################
validate_skill_name() {
    local skill_name="$1"
    
    # Check if empty
    if [[ -z "$skill_name" ]]; then
        log_skill_event "ERROR" "Skill name cannot be empty"
        return 1
    fi
    
    # Check length (3-100 characters)
    if [[ ${#skill_name} -lt 3 || ${#skill_name} -gt 100 ]]; then
        log_skill_event "ERROR" "Skill name must be between 3 and 100 characters"
        return 1
    fi
    
    # Check format: lowercase-with-dashes
    if [[ ! "$skill_name" =~ ^[a-z0-9-]+$ ]]; then
        log_skill_event "ERROR" "Skill name must be lowercase with hyphens (a-z, 0-9, -)"
        return 1
    fi
    
    # Check doesn't start or end with hyphen
    if [[ "$skill_name" =~ ^- || "$skill_name" =~ -$ ]]; then
        log_skill_event "ERROR" "Skill name cannot start or end with a hyphen"
        return 1
    fi
    
    # Check for consecutive hyphens
    if [[ "$skill_name" =~ -- ]]; then
        log_skill_event "ERROR" "Skill name cannot contain consecutive hyphens"
        return 1
    fi
    
    return 0
}

#######################################
# Get absolute path to a skill directory
# Arguments:
#   $1 - Skill name (lowercase-with-dashes)
# Outputs:
#   Absolute path to skill directory
# Returns:
#   0 if skill exists, 1 if not found
#######################################
get_skill_path() {
    local skill_name="$1"
    local repo_root=$(get_repo_root)
    local skill_path="$repo_root/.github/copilot-skills/$skill_name"
    
    if [[ -d "$skill_path" ]]; then
        echo "$skill_path"
        return 0
    else
        log_skill_event "ERROR" "Skill not found: $skill_name"
        return 1
    fi
}

#######################################
# Check if a skill already exists
# Arguments:
#   $1 - Skill name (lowercase-with-dashes)
# Returns:
#   0 if skill exists, 1 if not found
#######################################
skill_exists() {
    local skill_name="$1"
    local repo_root=$(get_repo_root)
    local skill_path="$repo_root/.github/copilot-skills/$skill_name"
    
    [[ -d "$skill_path" ]]
}

#######################################
# Convert human-readable name to skill directory name
# Arguments:
#   $1 - Human-readable name (e.g., "PDF Handling")
# Outputs:
#   Skill directory name (e.g., "pdf-handling")
#######################################
name_to_skill_dir() {
    local name="$1"
    echo "$name" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/--*/-/g' | sed 's/^-//;s/-$//'
}

#######################################
# Get the skills root directory
# Outputs:
#   Absolute path to .github/copilot-skills/
#######################################
get_skills_root() {
    local repo_root=$(get_repo_root)
    echo "$repo_root/.github/copilot-skills"
}

#######################################
# List all installed skills
# Outputs:
#   List of skill directory names, one per line
#######################################
list_skills() {
    local skills_root=$(get_skills_root)
    
    if [[ ! -d "$skills_root" ]]; then
        return 1
    fi
    
    find "$skills_root" -mindepth 1 -maxdepth 1 -type d -exec basename {} \; | \
        grep -v "^scripts$" | \
        grep -v "^templates$" | \
        grep -v "^prompts$" | \
        sort
}

