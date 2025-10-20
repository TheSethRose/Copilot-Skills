#!/bin/bash
# OpenCode Project Setup
# Initializes an OpenCode project with config and test runs

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

show_help() {
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}OpenCode Project Setup${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo "Usage: $0 [command] [args]"
    echo ""
    echo "Commands:"
    echo "  init                Initialize OpenCode project"
    echo "  test <agent-name>   Test an agent"
    echo "  add-agent <name>    Add existing agent to config"
    echo ""
    exit 0
}

init_project() {
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}OpenCode Project Initialization${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    
    if [ ! -f "opencode.config.json" ]; then
        echo "Creating opencode.config.json..."
        cat > opencode.config.json <<'EOF'
{
  "$schema": "https://opencode.ai/config.json",
  "agent": {}
}
EOF
        echo -e "${GREEN}✓${NC} Created opencode.config.json"
    else
        echo -e "${YELLOW}⚠${NC}  opencode.config.json already exists"
    fi
    
    echo ""
    echo -e "${GREEN}✓ Project initialized${NC}"
    echo ""
}

test_agent() {
    local AGENT_NAME="$1"
    
    if [ -z "$AGENT_NAME" ]; then
        echo -e "${YELLOW}⚠${NC}  Agent name required"
        exit 1
    fi
    
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}Testing Agent: $AGENT_NAME${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    
    if [ ! -f "opencode.config.json" ]; then
        echo -e "${YELLOW}⚠${NC}  opencode.config.json not found"
        echo "Run: $0 init"
        exit 1
    fi
    
    echo "Running agent test..."
    opencode run --agent "$AGENT_NAME" "Please respond with your name and purpose"
    
    echo ""
    echo -e "${GREEN}✓ Agent test completed${NC}"
    echo ""
}

if [ "$1" = "--help" ] || [ "$1" = "-h" ] || [ -z "$1" ]; then
    show_help
fi

case "$1" in
    init)
        init_project
        ;;
    test)
        test_agent "$2"
        ;;
    *)
        echo -e "${YELLOW}Unknown command: $1${NC}"
        show_help
        ;;
esac
