#!/usr/bin/env bash
#
# {{SCRIPT_NAME}}.sh - {{SCRIPT_DESCRIPTION}}
#
# Part of the {{SKILL_NAME}} skill.
#
# Usage:
#   {{SCRIPT_NAME}}.sh {{USAGE_ARGS}}
#
# Examples:
#   {{EXAMPLE_1}}
#   {{EXAMPLE_2}}
#
# Exit codes:
#   0 - Success
#   1 - General error
#   2 - Invalid arguments

set -euo pipefail

# Script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Load common utilities if available
if [[ -f "$SCRIPT_DIR/../common.sh" ]]; then
    source "$SCRIPT_DIR/../common.sh"
fi

# Default values
VERBOSE=false

#######################################
# Print usage information
# Globals:
#   None
# Arguments:
#   None
# Outputs:
#   Usage message to stdout
#######################################
usage() {
    cat << EOF
Usage: $(basename "$0") {{USAGE_ARGS}}

{{SCRIPT_DESCRIPTION}}

Arguments:
    {{ARG_NAME}}        {{ARG_DESCRIPTION}}

Options:
    -v, --verbose      Enable verbose output
    -h, --help         Show this help message

Examples:
    {{EXAMPLE_1}}
    {{EXAMPLE_2}}

Part of the {{SKILL_NAME}} skill.
EOF
}

#######################################
# Main logic
# Globals:
#   VERBOSE
# Arguments:
#   $@ - All command line arguments
# Returns:
#   0 on success, non-zero on error
#######################################
main() {
    local {{ARG_NAME}}=""
    
    # Parse arguments
    while [[ $# -gt 0 ]]; do
        case $1 in
            -v|--verbose)
                VERBOSE=true
                shift
                ;;
            -h|--help)
                usage
                exit 0
                ;;
            *)
                if [[ -z "${{ARG_NAME}}" ]]; then
                    {{ARG_NAME}}="$1"
                    shift
                else
                    echo "Error: Unknown argument '$1'" >&2
                    usage >&2
                    exit 2
                fi
                ;;
        esac
    done
    
    # Validate required arguments
    if [[ -z "${{ARG_NAME}}" ]]; then
        echo "Error: Missing required argument: {{ARG_NAME}}" >&2
        usage >&2
        exit 2
    fi
    
    # Main logic here
    {{MAIN_LOGIC}}
    
    if [[ "$VERBOSE" == "true" ]]; then
        echo "✓ Success: {{SUCCESS_MESSAGE}}" >&2
    fi
    
    return 0
}

# Run main function
main "$@"
