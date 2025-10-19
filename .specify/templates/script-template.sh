#!/bin/bash
# [Script Name]
#
# [One paragraph describing what this script does]
#
# Usage:
#     bash {script-name}.sh "arg1_value" "arg2_value"
#     bash {script-name}.sh "arg1_value" "arg2_value" --format json
#
# Arguments:
#     $1: [Description of first argument]
#     $2: [Description of second argument]
#
# Flags:
#     --format: Output format (json or text, default: text)
#     --verbose: Enable verbose logging
#
# Output:
#     Results as JSON or plain text based on --format flag
#
# Exit Codes:
#     0: Success
#     1: Argument validation error
#     2: Processing error
#
# Error Handling:
#     - Missing required arguments: Exit code 1, error message to stderr
#     - Invalid argument values: Exit code 1, error message to stderr
#     - Processing failure: Exit code 2, error message to stderr

set -e  # Exit on error

# Configuration
SCRIPT_NAME=$(basename "$0")
FORMAT="text"  # Default format
VERBOSE=false

# Parse arguments
if [ $# -lt 2 ]; then
    echo "Error: Missing required arguments" >&2
    echo "Usage: $SCRIPT_NAME <arg1> <arg2> [--format json|text] [--verbose]" >&2
    exit 1
fi

ARG1="$1"
ARG2="$2"
shift 2

# Parse optional flags
while [ $# -gt 0 ]; do
    case "$1" in
        --format)
            if [ $# -lt 2 ]; then
                echo "Error: --format requires a value" >&2
                exit 1
            fi
            FORMAT="$2"
            shift 2
            ;;
        --verbose)
            VERBOSE=true
            shift
            ;;
        *)
            echo "Error: Unknown flag: $1" >&2
            exit 1
            ;;
    esac
done

# Validate arguments
if [ -z "$ARG1" ] || [ -z "$ARG2" ]; then
    echo "Error: Arguments cannot be empty" >&2
    exit 1
fi

if [ "$VERBOSE" = true ]; then
    echo "[DEBUG] arg1=$ARG1" >&2
    echo "[DEBUG] arg2=$ARG2" >&2
    echo "[DEBUG] format=$FORMAT" >&2
fi

# Process
if ! result=$(process_input "$ARG1" "$ARG2" 2>&1); then
    echo "Error: Processing failed: $result" >&2
    exit 2
fi

# Output
if [ "$FORMAT" = "json" ]; then
    # Output as JSON
    cat <<EOF
{
  "success": true,
  "data": {
    "result": "$result"
  },
  "error": null
}
EOF
else
    # Output as plain text
    echo "Result: $result"
fi

exit 0


# Helper functions

function process_input() {
    # Process the input arguments
    #
    # Args:
    #     $1: First argument
    #     $2: Second argument
    #
    # Returns:
    #     Processed result (echoed to stdout)
    #
    # Exit codes:
    #     0: Success
    #     1: Validation error
    
    local arg1="$1"
    local arg2="$2"
    
    # Validate
    if [ -z "$arg1" ] || [ -z "$arg2" ]; then
        echo "Error: Arguments cannot be empty" >&2
        return 1
    fi
    
    # Process (example: concatenate)
    local result="${arg1} and ${arg2}"
    echo "$result"
    return 0
}

function log_error() {
    # Log error message to stderr
    echo "[ERROR] $*" >&2
}

function log_debug() {
    # Log debug message to stderr (only if verbose)
    if [ "$VERBOSE" = true ]; then
        echo "[DEBUG] $*" >&2
    fi
}
