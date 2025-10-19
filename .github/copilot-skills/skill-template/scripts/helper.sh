#!/bin/bash
# Helper script demonstrating Shell script patterns for skills
#
# Usage:
#     bash helper.sh "argument"
#
# Arguments:
#     $1: Input value to process
#
# Output:
#     Processed result or error message

set -e

# Validate arguments
if [ $# -lt 1 ]; then
    echo "Error: Missing required argument" >&2
    echo "Usage: $0 <input>" >&2
    exit 1
fi

input="$1"

# Example processing
output=$(echo "$input" | tr '[:lower:]' '[:upper:]')

# Output result
echo "Processed: $output"
exit 0
