#!/bin/bash
# OpenCode Agent Manager
# Complete lifecycle management: create, test, list, remove, modify agents
# All agents automatically added to ~/.config/opencode/opencode.json

set -e

OPENCODE_CONFIG="$HOME/.config/opencode/opencode.json"
ACTION="${1:-}"
AGENT_NAME="${2:-}"
AGENT_PURPOSE="${3:-A specialized AI assistant}"

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

# Ensure config directory exists
mkdir -p "$(dirname "$OPENCODE_CONFIG")"

show_help() {
    cat <<'EOF'
╔════════════════════════════════════════════════════════════════╗
║   OpenCode Agent Manager - Full Lifecycle Management          ║
╚════════════════════════════════════════════════════════════════╝

Usage: generate-agent.sh [command] [agent-name] [purpose]

Commands:
  create [name] [purpose]    Create and register new agent
  test [name] [message]      Test agent with message
  list                       List all agents
  remove [name]              Delete agent from config
  edit [name]                Edit agent prompt file
  show [name]                Show agent configuration

Examples:
  generate-agent.sh create hello-world "Prints Hello World"
  generate-agent.sh test hello-world "Say hello and your name"
  generate-agent.sh list
  generate-agent.sh remove hello-world

Configuration: $HOME/.config/opencode/opencode.json
Subagents: .github/copilot-skills/frameworks/opencode/subagents/{agent-name}.txt
EOF
}

# Create or ensure config file exists
ensure_config() {
    if [ ! -f "$OPENCODE_CONFIG" ]; then
        cat > "$OPENCODE_CONFIG" <<'EOL'
{
  "agent": {}
}
EOL
    fi
}

# Generate intelligent agent configuration
generate_config() {
    local name="$1"
    local purpose="$2"
    local prompt_path="$(pwd)/.github/copilot-skills/frameworks/opencode/subagents/${name}.txt"
    local purpose_lower=$(echo "$purpose" | tr '[:upper:]' '[:lower:]')
    
    # Auto-detect settings based on purpose
    if [[ $purpose_lower == *"autonomous"* ]] || [[ $purpose_lower == *"one-shot"* ]] || [[ $purpose_lower == *"auto"* ]]; then
        local temp="0.8" write="true" edit="true" bash="true"
    elif [[ $purpose_lower == *"skill"* ]] || [[ $purpose_lower == *"generator"* ]]; then
        local temp="0.8" write="true" edit="true" bash="true"
    elif [[ $purpose_lower == *"review"* ]] || [[ $purpose_lower == *"quality"* ]]; then
        local temp="0.1" write="false" edit="false" bash="false"
    elif [[ $purpose_lower == *"test"* ]]; then
        local temp="0.7" write="true" edit="false" bash="true"
    elif [[ $purpose_lower == *"doc"* ]]; then
        local temp="0.8" write="true" edit="true" bash="false"
    elif [[ $purpose_lower == *"debug"* ]]; then
        local temp="0.3" write="false" edit="false" bash="true"
    elif [[ $purpose_lower == *"refactor"* ]]; then
        local temp="0.5" write="false" edit="true" bash="false"
    elif [[ $purpose_lower == *"scrape"* ]] || [[ $purpose_lower == *"fetch"* ]] || [[ $purpose_lower == *"crawl"* ]]; then
        local temp="0.5" write="true" edit="false" bash="true"
    else
        local temp="0.7" write="false" edit="false" bash="false"
    fi
    
    cat <<EOF
{
  "mode": "subagent",
  "model": "github-copilot/claude-haiku-4.5",
  "temperature": $temp,
  "prompt": "{file:$prompt_path}",
  "tools": {
    "write": $write,
    "edit": $edit,
    "bash": $bash
  }
}
EOF
}

# Generate agent prompt
generate_prompt() {
    local name="$1"
    local purpose="$2"
    
    cat <<EOF
---
description: $purpose
mode: subagent
model: github-copilot/claude-haiku-4.5
temperature: 0.7
tools:
  write: false
  edit: false
  bash: false
---

You are an OpenCode agent.

## Your Identity
- Name: **$name**
- Purpose: $purpose

## Your Core Task
$purpose

## Guidelines
- Be concise and focused
- Perform your designated task
- Provide clear feedback
- Follow OpenCode best practices

## Output Format
Be direct and clear in responses.
EOF
}

# Add agent to config
add_to_config() {
    local name="$1"
    local purpose="$2"
    
    ensure_config
    
    # Check if agent already exists
    if grep -q "\"$name\"" "$OPENCODE_CONFIG"; then
        echo -e "${YELLOW}⚠  Agent '$name' already exists${NC}"
        return 1
    fi
    
    # Generate config and add to JSON
    local config=$(generate_config "$name" "$purpose")
    
    # Use jq to add agent if available, otherwise use sed
    if command -v jq &>/dev/null; then
        jq --arg name "$name" --argjson cfg "$config" '.agent[$name] = $cfg' "$OPENCODE_CONFIG" > "${OPENCODE_CONFIG}.tmp"
        mv "${OPENCODE_CONFIG}.tmp" "$OPENCODE_CONFIG"
    else
        # Fallback: simple sed insertion
        sed -i.bak "s/\"agent\": {/\"agent\": {\n    \"$name\": $config,/" "$OPENCODE_CONFIG"
        rm -f "${OPENCODE_CONFIG}.bak"
    fi
    
    echo -e "${GREEN}✓${NC} Agent added to config"
}

# Remove agent from config
remove_from_config() {
    local name="$1"
    
    ensure_config
    
    if ! grep -q "\"$name\"" "$OPENCODE_CONFIG"; then
        echo -e "${RED}✗${NC} Agent '$name' not found"
        return 1
    fi
    
    if command -v jq &>/dev/null; then
        jq --arg name "$name" 'del(.agent[$name])' "$OPENCODE_CONFIG" > "${OPENCODE_CONFIG}.tmp"
        mv "${OPENCODE_CONFIG}.tmp" "$OPENCODE_CONFIG"
    else
        # Fallback pattern matching
        sed -i.bak "/\"$name\":/,/},/d" "$OPENCODE_CONFIG"
        rm -f "${OPENCODE_CONFIG}.bak"
    fi
    
    echo -e "${GREEN}✓${NC} Agent removed from config"
}

# Create agent
cmd_create() {
    local name="$1"
    local purpose="${2:-A specialized AI assistant}"
    
    if [ -z "$name" ]; then
        echo -e "${RED}✗${NC} Agent name required"
        return 1
    fi
    
    # Sanitize name
    name=$(echo "$name" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9_-]//g')
    
    echo -e "${BLUE}Creating agent: ${CYAN}$name${NC}"
    echo ""
    
    # Create subagents directory in opencode skill
    mkdir -p .github/copilot-skills/frameworks/opencode/subagents
    
    # Generate prompt file in opencode/subagents
    generate_prompt "$name" "$purpose" > ".github/copilot-skills/frameworks/opencode/subagents/${name}.txt"
    echo -e "${GREEN}✓${NC} Created .github/copilot-skills/frameworks/opencode/subagents/${name}.txt"
    
    # Add to config
    add_to_config "$name" "$purpose"
    
    echo ""
    echo -e "${GREEN}✓${NC} Agent ready to use!"
    echo -e "  Test: ${CYAN}opencode run --agent $name \"<your message>\"${NC}"
}

# Test agent
cmd_test() {
    local name="$1"
    local message="${2:-Say hello and tell me your name}"
    
    if [ -z "$name" ]; then
        echo -e "${RED}✗${NC} Agent name required"
        return 1
    fi
    
    echo -e "${BLUE}Testing agent: ${CYAN}$name${NC}"
    echo -e "${YELLOW}Message:${NC} $message"
    echo ""
    
    opencode run --agent "$name" "$message"
}

# List agents
cmd_list() {
    ensure_config
    
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}Registered Agents${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    
    if command -v jq &>/dev/null; then
        jq -r '.agent | to_entries[] | "\(.key): \(.value.description // "No description")"' "$OPENCODE_CONFIG"
    else
        grep -o '"[^"]*"[[:space:]]*:' "$OPENCODE_CONFIG" | grep -v "agent\|model\|prompt\|tools\|write\|edit\|bash\|mode\|temperature\|description" | sed 's/[":]*//g' | sort -u
    fi
    
    echo ""
}

# Remove agent
cmd_remove() {
    local name="$1"
    
    if [ -z "$name" ]; then
        echo -e "${RED}✗${NC} Agent name required"
        return 1
    fi
    
    echo -e "${YELLOW}Removing agent: ${CYAN}$name${NC}"
    
    # Remove from config
    remove_from_config "$name"
    
    # Optionally remove prompt file
    if [ -f ".github/copilot-skills/frameworks/opencode/subagents/${name}.txt" ]; then
        rm ".github/copilot-skills/frameworks/opencode/subagents/${name}.txt"
        echo -e "${GREEN}✓${NC} Removed .github/copilot-skills/frameworks/opencode/subagents/${name}.txt"
    fi
    
    echo -e "${GREEN}✓${NC} Agent deleted"
}

# Show agent config
cmd_show() {
    local name="$1"
    
    if [ -z "$name" ]; then
        echo -e "${RED}✗${NC} Agent name required"
        return 1
    fi
    
    ensure_config
    
    echo -e "${BLUE}Agent: ${CYAN}$name${NC}"
    echo ""
    
    if command -v jq &>/dev/null; then
        jq ".agent.$name" "$OPENCODE_CONFIG"
    else
        echo "Config location: $OPENCODE_CONFIG"
    fi
}

# Main
if [ "$1" = "--help" ] || [ "$1" = "-h" ] || [ -z "$1" ]; then
    show_help
    exit 0
fi

case "$ACTION" in
    create)
        if [ -z "$AGENT_NAME" ]; then
            echo -e "${RED}✗${NC} Agent name required"
            exit 1
        fi
        cmd_create "$AGENT_NAME" "$AGENT_PURPOSE"
        ;;
    test)
        if [ -z "$AGENT_NAME" ]; then
            echo -e "${RED}✗${NC} Agent name required"
            exit 1
        fi
        cmd_test "$AGENT_NAME" "$AGENT_PURPOSE"
        ;;
    list)
        cmd_list
        ;;
    remove)
        if [ -z "$AGENT_NAME" ]; then
            echo -e "${RED}✗${NC} Agent name required"
            exit 1
        fi
        cmd_remove "$AGENT_NAME"
        ;;
    show)
        if [ -z "$AGENT_NAME" ]; then
            echo -e "${RED}✗${NC} Agent name required"
            exit 1
        fi
        cmd_show "$AGENT_NAME"
        ;;
    edit)
        if [ -z "$AGENT_NAME" ]; then
            echo -e "${RED}✗${NC} Agent name required"
            exit 1
        fi
        ${EDITOR:-nano} ".github/copilot-skills/frameworks/opencode/subagents/${AGENT_NAME}.txt"
        ;;
    *)
        if [ -n "$ACTION" ]; then
            echo -e "${RED}✗${NC} Unknown command: $ACTION"
        fi
        show_help
        exit 0
        ;;
esac
