#!/bin/bash
# OpenCode Multi-Agent Orchestration Helper
# Provides patterns and examples for coordinating multiple agents

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
NC='\033[0m'

show_header() {
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
}

show_pattern() {
    local title="$1"
    local agents="$2"
    local description="$3"
    
    echo -e "${CYAN}Pattern: ${GREEN}$title${NC}"
    echo -e "${YELLOW}Agents:${NC} $agents"
    echo -e "$description"
    echo ""
}

show_workflow() {
    local step="$1"
    local agent="$2"
    local action="$3"
    
    echo -e "  ${MAGENTA}$step.${NC} ${CYAN}@$agent${NC} $action"
}

if [ "$1" = "--help" ] || [ "$1" = "-h" ] || [ -z "$1" ]; then
    show_header "OpenCode Multi-Agent Orchestration"
    
    echo "Usage: $0 [pattern]"
    echo ""
    echo "Available patterns:"
    echo "  analysis       - Code analysis pipeline"
    echo "  refactor       - Safe refactoring workflow"
    echo "  feature        - Feature development cycle"
    echo "  debug          - Debugging workflow"
    echo "  documentation  - Documentation generation"
    echo "  review         - Code review process"
    echo "  test           - Testing workflow"
    echo "  all            - Show all patterns"
    echo ""
    echo "Examples:"
    echo "  $0 analysis"
    echo "  $0 refactor"
    echo "  $0 all"
    echo ""
    exit 0
fi

PATTERN="$1"

case "$PATTERN" in
    analysis|all)
        show_header "Code Analysis Pipeline"
        show_pattern \
            "Code Analysis" \
            "@general → @plan → @code-reviewer" \
            "Multi-stage analysis with specialized agents"
        
        echo -e "${YELLOW}Workflow:${NC}"
        show_workflow "1" "general" "Search codebase for relevant files"
        show_workflow "2" "plan" "Analyze architecture and dependencies"
        show_workflow "3" "code-reviewer" "Review code quality and issues"
        echo ""
        
        echo -e "${YELLOW}Example Command:${NC}"
        echo -e "  ${GREEN}@general find all authentication related files${NC}"
        echo -e "  ${GREEN}@plan analyze the authentication flow${NC}"
        echo -e "  ${GREEN}@code-reviewer review auth.ts for security issues${NC}"
        echo ""
        
        [ "$PATTERN" != "all" ] && exit 0
        ;;
esac

case "$PATTERN" in
    refactor|all)
        show_header "Safe Refactoring Workflow"
        show_pattern \
            "Refactor" \
            "@plan → @test-writer → @build" \
            "Plan-first refactoring with test coverage"
        
        echo -e "${YELLOW}Workflow:${NC}"
        show_workflow "1" "plan" "Create refactoring plan without changes"
        show_workflow "2" "test-writer" "Write tests for existing behavior"
        show_workflow "3" "build" "Execute refactoring with test validation"
        echo ""
        
        echo -e "${YELLOW}Example Command:${NC}"
        echo -e "  ${GREEN}@plan create a refactoring plan for the auth module${NC}"
        echo -e "  ${GREEN}@test-writer write tests covering current auth behavior${NC}"
        echo -e "  ${GREEN}@build refactor auth module following the plan${NC}"
        echo ""
        
        [ "$PATTERN" != "all" ] && exit 0
        ;;
esac

case "$PATTERN" in
    feature|all)
        show_header "Feature Development Cycle"
        show_pattern \
            "Feature Development" \
            "@plan → @build → @test-writer → @docs-generator" \
            "Complete feature lifecycle with documentation"
        
        echo -e "${YELLOW}Workflow:${NC}"
        show_workflow "1" "plan" "Design feature architecture"
        show_workflow "2" "build" "Implement feature code"
        show_workflow "3" "test-writer" "Create comprehensive tests"
        show_workflow "4" "docs-generator" "Generate documentation"
        echo ""
        
        echo -e "${YELLOW}Example Command:${NC}"
        echo -e "  ${GREEN}@plan design a user profile feature${NC}"
        echo -e "  ${GREEN}@build implement the user profile components${NC}"
        echo -e "  ${GREEN}@test-writer add tests for user profiles${NC}"
        echo -e "  ${GREEN}@docs-generator document the profile feature${NC}"
        echo ""
        
        [ "$PATTERN" != "all" ] && exit 0
        ;;
esac

case "$PATTERN" in
    debug|all)
        show_header "Debugging Workflow"
        show_pattern \
            "Debug" \
            "@general → @debug-helper → @build" \
            "Systematic debugging approach"
        
        echo -e "${YELLOW}Workflow:${NC}"
        show_workflow "1" "general" "Search for similar issues in codebase"
        show_workflow "2" "debug-helper" "Investigate logs and state"
        show_workflow "3" "build" "Implement fix"
        echo ""
        
        echo -e "${YELLOW}Example Command:${NC}"
        echo -e "  ${GREEN}@general search for authentication timeout issues${NC}"
        echo -e "  ${GREEN}@debug-helper analyze the session management logs${NC}"
        echo -e "  ${GREEN}@build fix the session timeout bug${NC}"
        echo ""
        
        [ "$PATTERN" != "all" ] && exit 0
        ;;
esac

case "$PATTERN" in
    documentation|all)
        show_header "Documentation Generation"
        show_pattern \
            "Documentation" \
            "@plan → @docs-generator → @code-reviewer" \
            "Comprehensive documentation workflow"
        
        echo -e "${YELLOW}Workflow:${NC}"
        show_workflow "1" "plan" "Analyze code structure and APIs"
        show_workflow "2" "docs-generator" "Generate documentation"
        show_workflow "3" "code-reviewer" "Review docs for accuracy"
        echo ""
        
        echo -e "${YELLOW}Example Command:${NC}"
        echo -e "  ${GREEN}@plan outline the API documentation structure${NC}"
        echo -e "  ${GREEN}@docs-generator create API docs for all endpoints${NC}"
        echo -e "  ${GREEN}@code-reviewer verify documentation accuracy${NC}"
        echo ""
        
        [ "$PATTERN" != "all" ] && exit 0
        ;;
esac

case "$PATTERN" in
    review|all)
        show_header "Code Review Process"
        show_pattern \
            "Review" \
            "@plan → @code-reviewer → @test-writer" \
            "Thorough review with test recommendations"
        
        echo -e "${YELLOW}Workflow:${NC}"
        show_workflow "1" "plan" "Understand change context and scope"
        show_workflow "2" "code-reviewer" "Review for quality and issues"
        show_workflow "3" "test-writer" "Suggest additional test coverage"
        echo ""
        
        echo -e "${YELLOW}Example Command:${NC}"
        echo -e "  ${GREEN}@plan summarize changes in this PR${NC}"
        echo -e "  ${GREEN}@code-reviewer review the authentication changes${NC}"
        echo -e "  ${GREEN}@test-writer suggest tests for edge cases${NC}"
        echo ""
        
        [ "$PATTERN" != "all" ] && exit 0
        ;;
esac

case "$PATTERN" in
    test|all)
        show_header "Testing Workflow"
        show_pattern \
            "Testing" \
            "@plan → @test-writer → @build" \
            "Test-driven development cycle"
        
        echo -e "${YELLOW}Workflow:${NC}"
        show_workflow "1" "plan" "Design test strategy"
        show_workflow "2" "test-writer" "Write comprehensive tests"
        show_workflow "3" "build" "Run tests and fix failures"
        echo ""
        
        echo -e "${YELLOW}Example Command:${NC}"
        echo -e "  ${GREEN}@plan create test strategy for payment processing${NC}"
        echo -e "  ${GREEN}@test-writer write unit and integration tests${NC}"
        echo -e "  ${GREEN}@build run tests and fix any failures${NC}"
        echo ""
        
        [ "$PATTERN" != "all" ] && exit 0
        ;;
esac

if [ "$PATTERN" = "all" ]; then
    show_header "Agent Coordination Best Practices"
    
    echo -e "${YELLOW}Key Principles:${NC}"
    echo ""
    echo -e "${GREEN}1. Use @plan first${NC}"
    echo "   Plan agents analyze without making changes"
    echo "   Creates safe space for exploration"
    echo ""
    echo -e "${GREEN}2. Delegate specialized tasks${NC}"
    echo "   Let each agent focus on their expertise"
    echo "   @test-writer for tests, @docs-generator for docs"
    echo ""
    echo -e "${GREEN}3. Chain agents sequentially${NC}"
    echo "   Build workflows: analyze → plan → execute → verify"
    echo "   Each step builds on previous context"
    echo ""
    echo -e "${GREEN}4. Use @general for research${NC}"
    echo "   Multi-step search and investigation"
    echo "   Great for finding patterns across codebase"
    echo ""
    echo -e "${GREEN}5. Keep @build for final execution${NC}"
    echo "   @build has full tool access"
    echo "   Use after planning and preparation"
    echo ""
    
    show_header "Quick Reference"
    echo -e "${CYAN}@general${NC}      - Research and multi-step search"
    echo -e "${CYAN}@plan${NC}         - Read-only analysis and planning"
    echo -e "${CYAN}@build${NC}        - Full access implementation"
    echo -e "${CYAN}@code-reviewer${NC} - Quality and security review"
    echo -e "${CYAN}@test-writer${NC}  - Test generation"
    echo -e "${CYAN}@docs-generator${NC} - Documentation creation"
    echo -e "${CYAN}@debug-helper${NC} - Investigation and tracing"
    echo ""
fi

if [ "$PATTERN" != "all" ] && \
   [ "$PATTERN" != "analysis" ] && \
   [ "$PATTERN" != "refactor" ] && \
   [ "$PATTERN" != "feature" ] && \
   [ "$PATTERN" != "debug" ] && \
   [ "$PATTERN" != "documentation" ] && \
   [ "$PATTERN" != "review" ] && \
   [ "$PATTERN" != "test" ]; then
    echo -e "${YELLOW}⚠️  Unknown pattern: $PATTERN${NC}"
    echo "Run $0 --help to see available patterns"
    exit 1
fi
