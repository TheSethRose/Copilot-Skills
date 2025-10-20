#!/usr/bin/env bash
#
# search-framework.sh - Search for symbols within an Apple framework
#
# Usage: bash search-framework.sh <framework> <query> [--json] [--limit N] [--help]
#
# Arguments:
#   <framework>  Framework name (e.g., "swift", "swiftui")
#   <query>      Search query
#
# Options:
#   --json       Output raw JSON
#   --limit N    Maximum results (default: 10)
#   --help       Show this help message
#
# Exit codes:
#   0 - Success
#   1 - Error

set -euo pipefail

API_BASE="https://developer.apple.com/tutorials/data"

# Defaults
OUTPUT_JSON=false
LIMIT=10

# Parse arguments
if [[ $# -eq 0 ]] || [[ "$1" == "--help" ]]; then
  cat << 'EOF'
search-framework.sh - Search for symbols within an Apple framework

Usage:
  bash search-framework.sh <framework> <query> [--json] [--limit N]

Arguments:
  <framework>  Framework name (e.g., "swift", "swiftui")
  <query>      Search query

Options:
  --json       Output raw JSON
  --limit N    Maximum results (default: 10)
  --help       Show this help message

Examples:
  # Search Swift documentation
  bash search-framework.sh swift "async await"

  # Search SwiftUI with limit
  bash search-framework.sh swiftui "button" --limit 20

  # Get raw JSON
  bash search-framework.sh swift "array" --json

Exit Codes:
  0 - Success
  1 - Error (network, API, parsing)
EOF
  exit 0
fi

FRAMEWORK="$1"
QUERY="$2"
shift 2

while [[ $# -gt 0 ]]; do
  case $1 in
    --json)
      OUTPUT_JSON=true
      shift
      ;;
    --limit)
      LIMIT="$2"
      shift 2
      ;;
    *)
      echo "Error: Unknown option: $1" >&2
      exit 1
      ;;
  esac
done

# Fetch framework data
URL="${API_BASE}/documentation/${FRAMEWORK}.json"

if ! response=$(curl -s -f -H "User-Agent: Mozilla/5.0" -H "Referer: https://developer.apple.com/documentation" "$URL" 2>&1); then
  echo "Error: Failed to fetch framework: $FRAMEWORK" >&2
  echo "URL: $URL" >&2
  exit 1
fi

# Check if jq is available
if ! command -v jq &> /dev/null; then
  echo "Error: jq is required but not installed" >&2
  echo "Install with: brew install jq" >&2
  exit 1
fi

# Search and filter
QUERY_LOWER=$(echo "$QUERY" | tr '[:upper:]' '[:lower:]')

if $OUTPUT_JSON; then
  echo "$response" | jq --arg query "$QUERY_LOWER" --argjson limit "$LIMIT" '
    .references 
    | to_entries[] 
    | select(
        (.value.title // "" | ascii_downcase | contains($query)) or
        (.value.abstract[]?.text // "" | ascii_downcase | contains($query))
      )
    | .value
  ' | jq -s ".[:$LIMIT]"
else
  echo "=== Search Results: $FRAMEWORK / $QUERY ==="
  echo ""
  
  results=$(echo "$response" | jq --arg query "$QUERY_LOWER" --argjson limit "$LIMIT" -r '
    [.references 
    | to_entries[] 
    | select(
        (.value.title // "" | ascii_downcase | contains($query)) or
        (.value.abstract[]?.text // "" | ascii_downcase | contains($query))
      )
    | .value] | .[:$limit] | .[] |
    "• \(.title // "Unknown")\n  Path: \(.url)\n  Kind: \(.kind // "N/A")\n"
  ')
  
  if [[ -z "$results" ]]; then
    echo "No results found for: $QUERY"
    echo ""
    echo "Try:"
    echo "  • Broader search terms"
    echo "  • Different framework name"
    echo "  • Check spelling"
  else
    echo "$results"
    count=$(echo "$results" | grep -c "^•" || true)
    echo "Found: $count results (limit: $LIMIT)"
  fi
fi
