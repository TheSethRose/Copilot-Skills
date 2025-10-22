#!/usr/bin/env bash
#
# get-symbol.sh - Get detailed documentation for a specific Apple symbol
#
# Usage: bash get-symbol.sh <path> [--json] [--help]
#
# Arguments:
#   <path>    Symbol path (e.g., "swift/array", "swiftui/button")
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

# Defaults
OUTPUT_JSON=false

# Parse arguments
if [[ $# -eq 0 ]] || [[ "$1" == "--help" ]]; then
  cat << 'EOF'
get-symbol.sh - Get detailed documentation for a specific Apple symbol

Usage:
  bash get-symbol.sh <path> [--json]

Arguments:
  <path>    Symbol path (e.g., "swift/array", "swiftui/button")

Options:
  --json    Output raw JSON
  --help    Show this help message

Examples:
  # Get Button documentation
  bash get-symbol.sh swiftui/button

  # Get Array documentation
  bash get-symbol.sh swift/array

  # Get raw JSON
  bash get-symbol.sh swift/task --json

  # Extract platforms
  bash get-symbol.sh swiftui/button --json | jq '.metadata.platforms'

Path Format:
  - Use lowercase framework names
  - Separate with forward slash
  - Examples: swift/array, swiftui/vstack, foundation/url

Exit Codes:
  0 - Success
  1 - Error (network, API, parsing)
EOF
  exit 0
fi

SYMBOL_PATH="$1"
shift

while [[ $# -gt 0 ]]; do
  case $1 in
    --json)
      OUTPUT_JSON=true
      shift
      ;;
    *)
      echo "Error: Unknown option: $1" >&2
      exit 1
      ;;
  esac
done

# Build URL
URL="${API_BASE}/documentation/${SYMBOL_PATH}.json"

if ! response=$(curl -s -f -H "User-Agent: Mozilla/5.0" -H "Referer: https://developer.apple.com/documentation" "$URL" 2>&1); then
  echo "Error: Failed to fetch symbol: $SYMBOL_PATH" >&2
  echo "URL: $URL" >&2
  echo "" >&2
  echo "Tips:" >&2
  echo "  • Check path format: framework/symbol (lowercase)" >&2
  echo "  • Try searching first: bash search-framework.sh <framework> <query>" >&2
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
  echo "=== Symbol Documentation: $SYMBOL_PATH ==="
  echo ""
  
  # Title and kind
  title=$(echo "$response" | jq -r '.metadata.title // "Unknown"')
  kind=$(echo "$response" | jq -r '.metadata.symbolKind // .metadata.role // "Unknown"')
  echo "Title: $title"
  echo "Kind: $kind"
  echo ""
  
  # Platforms
  echo "Platforms:"
  echo "$response" | jq -r '
    .metadata.platforms[]? 
    | "  • \(.name) \(.introducedAt)\(if .beta then " (Beta)" else "" end)"
  ' || echo "  • All platforms"
  echo ""
  
  # Abstract/Description
  echo "Description:"
  abstract=$(echo "$response" | jq -r '.abstract[]?.text // ""' | tr '\n' ' ')
  if [[ -n "$abstract" ]]; then
    echo "  $abstract"
  else
    echo "  (No description available)"
  fi
  echo ""
  
  # Topics (if available)
  topics=$(echo "$response" | jq -r '.topicSections[]?.title // empty' 2>/dev/null || true)
  if [[ -n "$topics" ]]; then
    echo "Topics:"
    echo "$response" | jq -r '.topicSections[] | "  • \(.title)"'
    echo ""
  fi
  
  # URL
  url=$(echo "$response" | jq -r '.metadata.url // ""')
  if [[ -n "$url" ]]; then
    echo "Documentation URL:"
    echo "  https://developer.apple.com$url"
  fi
fi
