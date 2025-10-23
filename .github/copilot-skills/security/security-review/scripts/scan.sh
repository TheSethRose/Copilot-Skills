#!/bin/bash
#
# Security Review Scan Script
# Main entry point for security vulnerability scanning
#

set -euo pipefail

# Colors
RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Default values
SCAN_PATH="."
CATEGORY="all"
SEVERITY="all"
FRAMEWORK="auto"
FORMAT="terminal"
OUTPUT=""
EXIT_CODE=0
EXCLUDE=""

# Help message
show_help() {
    cat << EOF
Security Review Scanner

Usage: bash scan.sh [OPTIONS]

Options:
  --path PATH          Project path to scan (default: current directory)
  --category CAT       Category: injection, auth, secrets, crypto, xss, dependencies, all
  --severity SEV       Severity: critical, high, medium, low, all
  --framework FW       Framework: nextjs, fastapi, express, django, auto
  --format FMT         Output format: terminal, json, markdown
  --output FILE        Output file path
  --exit-code N        Exit with code N if findings detected
  --exclude PATTERN    Exclude paths (glob pattern, comma-separated)
  --help               Show this help message

Examples:
  # Full scan
  bash scan.sh --path .

  # Check for secrets only
  bash scan.sh --path . --category secrets

  # Critical findings only, JSON output
  bash scan.sh --severity critical --format json --exit-code 1

  # Exclude test files
  bash scan.sh --exclude "**/*test*,**/node_modules/**"

Categories:
  injection      - SQL, Command, NoSQL, LDAP, XPath, XXE injection
  auth           - Authentication and authorization issues
  secrets        - Hardcoded secrets and credentials
  crypto         - Weak cryptography and key management
  validation     - Input validation and sanitization
  logic          - Business logic flaws and race conditions
  config         - Configuration security issues
  dependencies   - Vulnerable dependencies (CVEs)
  execution      - Code execution vulnerabilities
  xss            - Cross-site scripting
  all            - All categories

EOF
}

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --path)
            SCAN_PATH="$2"
            shift 2
            ;;
        --category)
            CATEGORY="$2"
            shift 2
            ;;
        --severity)
            SEVERITY="$2"
            shift 2
            ;;
        --framework)
            FRAMEWORK="$2"
            shift 2
            ;;
        --format)
            FORMAT="$2"
            shift 2
            ;;
        --output)
            OUTPUT="$2"
            shift 2
            ;;
        --exit-code)
            EXIT_CODE="$2"
            shift 2
            ;;
        --exclude)
            EXCLUDE="$2"
            shift 2
            ;;
        --help)
            show_help
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            show_help
            exit 1
            ;;
    esac
done

# Validate scan path
if [[ ! -d "$SCAN_PATH" ]]; then
    echo -e "${RED}Error: Path not found: $SCAN_PATH${NC}"
    exit 1
fi

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo -e "${BLUE}🔒 Security Review Scanner${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📁 Scanning: $SCAN_PATH"
echo "📊 Category: $CATEGORY"
echo "⚠️  Severity: $SEVERITY"
echo "🎯 Framework: $FRAMEWORK"
echo "📝 Format: $FORMAT"
echo ""

# Detect framework if auto
if [[ "$FRAMEWORK" == "auto" ]]; then
    echo "🔍 Detecting framework..."
    
    if [[ -f "$SCAN_PATH/next.config.js" ]] || [[ -f "$SCAN_PATH/next.config.ts" ]]; then
        FRAMEWORK="nextjs"
        echo "  ✓ Detected: Next.js"
    elif [[ -f "$SCAN_PATH/requirements.txt" ]] && grep -q "fastapi" "$SCAN_PATH/requirements.txt" 2>/dev/null; then
        FRAMEWORK="fastapi"
        echo "  ✓ Detected: FastAPI"
    elif [[ -f "$SCAN_PATH/package.json" ]] && grep -q "express" "$SCAN_PATH/package.json" 2>/dev/null; then
        FRAMEWORK="express"
        echo "  ✓ Detected: Express"
    elif [[ -f "$SCAN_PATH/manage.py" ]]; then
        FRAMEWORK="django"
        echo "  ✓ Detected: Django"
    else
        FRAMEWORK="generic"
        echo "  ℹ Using generic rules"
    fi
    echo ""
fi

# Initialize counters
TOTAL_FINDINGS=0
CRITICAL=0
HIGH=0
MEDIUM=0
LOW=0

# TODO: Implement actual scanning logic
# This is a placeholder that demonstrates the structure

echo "🔍 Scanning in progress..."
echo ""

# Placeholder: Simulate scanning
echo -e "${YELLOW}⚠️  This is a placeholder script${NC}"
echo "Actual scanning logic will be implemented with:"
echo "  - Pattern matching for vulnerabilities"
echo "  - Language-specific parsers"
echo "  - Framework-aware rules"
echo "  - Dependency CVE checking"
echo ""

# Example finding (placeholder)
if [[ "$CATEGORY" == "all" ]] || [[ "$CATEGORY" == "secrets" ]]; then
    echo -e "${RED}🔴 CRITICAL${NC}"
    echo ""
    echo "[1] Potential Hardcoded Secret"
    echo "  File: (example placeholder)"
    echo "  Line: (would show actual line number)"
    echo "  Pattern: API key-like string detected"
    echo "  CWE: CWE-798 - Use of Hard-coded Credentials"
    echo "  OWASP: A02:2021 – Cryptographic Failures"
    echo ""
    echo "  🔧 Remediation:"
    echo "  Move secrets to environment variables"
    echo "  Example: API_KEY = os.environ.get('API_KEY')"
    echo ""
    CRITICAL=$((CRITICAL + 1))
    TOTAL_FINDINGS=$((TOTAL_FINDINGS + 1))
fi

# Summary
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📊 Summary:"
echo "  🔴 Critical: $CRITICAL"
echo "  🟠 High: $HIGH"
echo "  🟡 Medium: $MEDIUM"
echo "  🟢 Low: $LOW"
echo "  📝 Total: $TOTAL_FINDINGS"
echo ""

if [[ $TOTAL_FINDINGS -eq 0 ]]; then
    echo -e "${GREEN}✅ No security issues found${NC}"
else
    echo -e "${YELLOW}⚠️  Security issues detected${NC}"
    echo ""
    echo "Next steps:"
    echo "  1. Review findings above"
    echo "  2. Check patterns.md for examples"
    echo "  3. Fix critical/high severity first"
    echo "  4. Re-run scan to verify"
fi

echo ""
echo "📚 Resources:"
echo "  - Full docs: .github/copilot-skills/security/security-review/README.md"
echo "  - Patterns: .github/copilot-skills/security/security-review/patterns.md"
echo "  - Run: /security-review"
echo ""

# Exit with appropriate code
if [[ $TOTAL_FINDINGS -gt 0 ]] && [[ $EXIT_CODE -ne 0 ]]; then
    exit "$EXIT_CODE"
fi

exit 0
