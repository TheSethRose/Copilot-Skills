#!/bin/bash
# OpenCode Agent Quick Reference
# Shows capabilities and use cases for each agent type

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
RED='\033[0;31m'
NC='\033[0m'

show_agent() {
    local name="$1"
    local type="$2"
    local model="$3"
    local tools="$4"
    local use_cases="$5"
    
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}$name${NC} ${YELLOW}($type)${NC}"
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}Model:${NC} $model"
    echo -e "${BLUE}Tools:${NC} $tools"
    echo ""
    echo -e "${YELLOW}Use Cases:${NC}"
    echo -e "$use_cases"
    echo ""
}

show_comparison() {
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}Tool Access Comparison${NC}"
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    printf "%-20s %-10s %-10s %-10s\n" "Agent" "Write" "Edit" "Bash"
    echo "────────────────────────────────────────────────────────────"
    printf "%-20s ${GREEN}%-10s${NC} ${GREEN}%-10s${NC} ${GREEN}%-10s${NC}\n" "@build" "✓" "✓" "✓"
    printf "%-20s ${RED}%-10s${NC} ${RED}%-10s${NC} ${RED}%-10s${NC}\n" "@plan" "✗" "✗" "✗"
    printf "%-20s ${RED}%-10s${NC} ${RED}%-10s${NC} ${GREEN}%-10s${NC}\n" "@general" "✗" "✗" "✓"
    printf "%-20s ${RED}%-10s${NC} ${RED}%-10s${NC} ${RED}%-10s${NC}\n" "@code-reviewer" "✗" "✗" "✗"
    printf "%-20s ${GREEN}%-10s${NC} ${RED}%-10s${NC} ${GREEN}%-10s${NC}\n" "@test-writer" "✓" "✗" "✓"
    printf "%-20s ${GREEN}%-10s${NC} ${GREEN}%-10s${NC} ${RED}%-10s${NC}\n" "@docs-generator" "✓" "✓" "✗"
    echo ""
}

if [ "$1" = "--help" ] || [ "$1" = "-h" ]; then
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}OpenCode Agent Quick Reference${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo "Usage: $0 [agent-name]"
    echo ""
    echo "Built-in agents:"
    echo "  build          - Primary development agent (full access)"
    echo "  plan           - Primary planning agent (read-only)"
    echo "  general        - Subagent for research"
    echo ""
    echo "Custom agent examples:"
    echo "  code-reviewer  - Code quality analysis"
    echo "  test-writer    - Test generation"
    echo "  docs-generator - Documentation creation"
    echo "  debug-helper   - Debugging assistance"
    echo ""
    echo "Special options:"
    echo "  compare        - Compare tool access"
    echo "  all            - Show all agents"
    echo ""
    exit 0
fi

AGENT="${1:-all}"

case "$AGENT" in
    build|all)
        show_agent \
            "@build" \
            "Primary Agent" \
            "claude-sonnet-4" \
            "write ✓ | edit ✓ | bash ✓" \
            "• Full development work
• File creation and modification
• System commands
• Primary implementation tasks
• Complete feature development

${YELLOW}When to use:${NC}
- Implementing features
- Making code changes
- Running build/test commands
- Final execution after planning"
        [ "$AGENT" != "all" ] && exit 0
        ;;
esac

case "$AGENT" in
    plan|all)
        show_agent \
            "@plan" \
            "Primary Agent" \
            "claude-haiku-4" \
            "write ✗ | edit ✗ | bash ✗" \
            "• Code analysis without changes
• Architecture review
• Planning refactoring
• Suggesting improvements
• Safe exploration

${YELLOW}When to use:${NC}
- Before making changes
- Understanding codebase
- Creating implementation plans
- Risk-free analysis
- Tab to switch from @build"
        [ "$AGENT" != "all" ] && exit 0
        ;;
esac

case "$AGENT" in
    general|all)
        show_agent \
            "@general" \
            "Subagent" \
            "claude-sonnet-4" \
            "write ✗ | edit ✗ | bash ✓" \
            "• Multi-step research
• Code search across repos
• Complex investigations
• Pattern finding
• gh_grep operations

${YELLOW}When to use:${NC}
- Finding relevant code
- Searching for patterns
- Investigating issues
- Research tasks
- @mention from any agent"
        [ "$AGENT" != "all" ] && exit 0
        ;;
esac

case "$AGENT" in
    code-reviewer|all)
        show_agent \
            "@code-reviewer" \
            "Subagent (Custom)" \
            "claude-sonnet-4" \
            "write ✗ | edit ✗ | bash ✗" \
            "• Code quality analysis
• Security review
• Best practices checking
• Bug detection
• Performance review

${YELLOW}When to use:${NC}
- PR reviews
- Security audits
- Code quality checks
- Before merging
- Architecture validation"
        [ "$AGENT" != "all" ] && exit 0
        ;;
esac

case "$AGENT" in
    test-writer|all)
        show_agent \
            "@test-writer" \
            "Subagent (Custom)" \
            "claude-sonnet-4" \
            "write ✓ | edit ✗ | bash ✓" \
            "• Unit test generation
• Integration test creation
• Test coverage analysis
• Edge case identification
• Running test suites

${YELLOW}When to use:${NC}
- Adding test coverage
- TDD workflows
- Testing new features
- Regression testing
- Before refactoring"
        [ "$AGENT" != "all" ] && exit 0
        ;;
esac

case "$AGENT" in
    docs-generator|all)
        show_agent \
            "@docs-generator" \
            "Subagent (Custom)" \
            "claude-sonnet-4" \
            "write ✓ | edit ✓ | bash ✗" \
            "• API documentation
• README generation
• Code comments
• Usage examples
• Markdown docs

${YELLOW}When to use:${NC}
- Documenting APIs
- Creating guides
- Updating READMEs
- Adding examples
- Onboarding docs"
        [ "$AGENT" != "all" ] && exit 0
        ;;
esac

case "$AGENT" in
    debug-helper|all)
        show_agent \
            "@debug-helper" \
            "Subagent (Custom)" \
            "claude-sonnet-4" \
            "write ✗ | edit ✗ | bash ✓" \
            "• Log analysis
• Stack trace interpretation
• State investigation
• Root cause analysis
• Debugging strategies

${YELLOW}When to use:${NC}
- Investigating bugs
- Analyzing errors
- Tracing execution
- Understanding failures
- Pre-fix analysis"
        [ "$AGENT" != "all" ] && exit 0
        ;;
esac

case "$AGENT" in
    compare)
        show_comparison
        exit 0
        ;;
esac

if [ "$AGENT" = "all" ]; then
    show_comparison
    
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}Agent Selection Guide${NC}"
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo -e "${YELLOW}Primary Agents${NC} (Tab to switch):"
    echo "  Use @build when you need to make changes"
    echo "  Use @plan when you want safe, read-only analysis"
    echo ""
    echo -e "${YELLOW}Subagents${NC} (@mention to invoke):"
    echo "  @general      - When you need to search/research"
    echo "  @code-reviewer - When you need quality analysis"
    echo "  @test-writer  - When you need tests"
    echo "  @docs-generator - When you need documentation"
    echo "  @debug-helper - When you need debugging help"
    echo ""
    echo -e "${YELLOW}Best Practices:${NC}"
    echo "  1. Start with @plan for exploration"
    echo "  2. Use specialized subagents for specific tasks"
    echo "  3. Switch to @build for implementation"
    echo "  4. Chain agents for complex workflows"
    echo ""
fi

if [ "$AGENT" != "all" ] && \
   [ "$AGENT" != "build" ] && \
   [ "$AGENT" != "plan" ] && \
   [ "$AGENT" != "general" ] && \
   [ "$AGENT" != "code-reviewer" ] && \
   [ "$AGENT" != "test-writer" ] && \
   [ "$AGENT" != "docs-generator" ] && \
   [ "$AGENT" != "debug-helper" ] && \
   [ "$AGENT" != "compare" ]; then
    echo -e "${YELLOW}⚠️  Unknown agent: $AGENT${NC}"
    echo "Run $0 --help to see available agents"
    exit 1
fi
