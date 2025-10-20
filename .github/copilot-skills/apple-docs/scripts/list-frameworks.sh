#!/usr/bin/env bash
#
# list-frameworks.sh - List all available Apple frameworks
#
# Usage: bash list-frameworks.sh [--json] [--help]
#
# Options:
#   --json    Output raw JSON
#   --help    Show this help message
#
# Exit codes:
#   0 - Success
#   1 - Error

set -euo pipefail

API_BASE="https://developer.apple.com/tutorials/data"
ENDPOINT="documentation/technologies.json"

# Parse arguments
OUTPUT_JSON=false

while [[ $# -gt 0 ]]; do
  case $1 in
    --json)
      OUTPUT_JSON=true
      shift
      ;;
    --help)
      cat << 'EOF'
list-frameworks.sh - List all available Apple frameworks

Usage:
  bash list-frameworks.sh [--json] [--help]

Options:
  --json    Output raw JSON
  --help    Show this help message

Examples:
  # List all frameworks
  bash list-frameworks.sh

  # Get raw JSON
  bash list-frameworks.sh --json

  # Filter with jq
  bash list-frameworks.sh --json | jq '.[] | select(.title | contains("Swift"))'

Exit Codes:
  0 - Success
  1 - Error (network, API, parsing)
EOF
      exit 0
      ;;
    *)
      echo "Error: Unknown option: $1" >&2
      echo "Use --help for usage information" >&2
      exit 1
      ;;
  esac
done

# Fetch frameworks
URL="${API_BASE}/${ENDPOINT}"

if ! response=$(curl -s -f -H "User-Agent: Mozilla/5.0" -H "Referer: https://developer.apple.com/documentation" "$URL" 2>&1); then
  echo "Error: Failed to fetch frameworks from Apple API" >&2
  echo "URL: $URL" >&2
  exit 1
fi

# Check if jq is available
if ! command -v jq &> /dev/null; then
  echo "Error: jq is required but not installed" >&2
  echo "Install with: brew install jq" >&2
  exit 1
fi

# Output
if $OUTPUT_JSON; then
  echo "$response"
else
  echo "=== Available Apple Frameworks ==="
  echo ""
  echo "$response" | jq -r '
    .sections[]?.groups[]?.technologies[]? 
    | "• \(.title) (\(.destination.identifier))"
  ' | sort
  echo ""
  total=$(echo "$response" | jq '[.sections[]?.groups[]?.technologies[]?] | length')
  echo "Total: $total frameworks"
fi
