---
description: Multi-agent orchestration framework for spawning and managing AI sub-agents
---

# OpenCode

**Purpose**: Master multi-agent orchestration with OpenCode - spawn specialized AI sub-agents, coordinate workflows, and build powerful agent-driven development pipelines.

## When to Use This Skill

Use this skill when:
- **Orchestrating multiple AI agents** for complex tasks
- **Delegating specialized work** to purpose-built sub-agents
- Building **multi-stage workflows** (analyze → plan → execute → verify)
- Creating **safe analysis pipelines** with read-only agents
- Implementing **parallel agent coordination** for large projects
- Setting up **custom agents** for domain-specific tasks
- Learning OpenCode's agent architecture and best practices

**Keywords**: opencode, multi-agent, sub-agent, orchestration, delegation, agent workflow, @mention, primary agent, subagent, agent coordination

## Quick Reference

### 🤖 Built-In Agents

**Primary Agents** (switch with Tab key):
- **@build** - Full development access (write/edit/bash)
  - Feature implementation
  - Code modifications
  - System commands
  
- **@plan** - Read-only analysis (safe exploration)
  - Code review without changes
  - Architecture planning
  - Risk-free exploration

**Subagents** (invoke with @mention):
- **@general** - Multi-step research and code search
  - Search patterns across codebase
  - Complex investigations
  - Uses `gh_grep` for GitHub searches

### 🔧 Multi-Agent Orchestration Patterns

**Pattern 1: Safe Refactoring**
```bash
@plan create refactoring plan for auth module
@test-writer write tests for current auth behavior
@build execute refactoring with test validation
```

**Pattern 2: Feature Development**
```bash
@plan design user profile architecture
@build implement profile components
@test-writer add comprehensive tests
@docs-generator create feature documentation
```

**Pattern 3: Code Analysis Pipeline**
```bash
@general find all authentication files
@plan analyze the auth flow
@code-reviewer review for security issues
```

**Pattern 4: Debugging Workflow**
```bash
@general search for similar timeout issues
@debug-helper investigate session logs
@build implement the fix
```

### 🎯 Creating Custom Agents

**Generate agent template:**
```bash
bash .github/copilot-skills/opencode/scripts/generate-agent.sh code-reviewer subagent
```

**Agent configuration structure:**
```json
{
  "agent": {
    "code-reviewer": {
      "mode": "subagent",
      "model": "anthropic/claude-sonnet-4-20250514",
      "temperature": 0.1,
      "prompt": "{file:./prompts/code-reviewer.txt}",
      "tools": {
        "write": false,
        "edit": false,
        "bash": false
      }
    }
  }
}
```

**Common agent archetypes:**
- **Code Reviewer** (read-only) - Quality, security, best practices
- **Test Writer** (write + bash) - Test generation, coverage analysis
- **Docs Generator** (write + edit) - Documentation, examples, guides
- **Debug Helper** (bash only) - Log analysis, investigation
- **Refactoring Assistant** (edit only) - Code improvements

### 📋 Tool Access Matrix

| Agent | Write | Edit | Bash | Use Case |
|-------|-------|------|------|----------|
| @build | ✓ | ✓ | ✓ | Full development |
| @plan | ✗ | ✗ | ✗ | Safe analysis |
| @general | ✗ | ✗ | ✓ | Research |
| @code-reviewer | ✗ | ✗ | ✗ | Review |
| @test-writer | ✓ | ✗ | ✓ | Testing |
| @docs-generator | ✓ | ✓ | ✗ | Documentation |

### 🔄 Agent Coordination Helpers

**View orchestration patterns:**
```bash
# Show all workflow patterns
bash .github/copilot-skills/opencode/scripts/orchestrate-agents.sh all

# Show specific pattern
bash .github/copilot-skills/opencode/scripts/orchestrate-agents.sh refactor
```

**Quick agent reference:**
```bash
# Show all agents
bash .github/copilot-skills/opencode/scripts/agent-reference.sh all

# Show specific agent
bash .github/copilot-skills/opencode/scripts/agent-reference.sh build

# Compare tool access
bash .github/copilot-skills/opencode/scripts/agent-reference.sh compare
```

### Code Examples

**Example 1: Invoke subagent**
```javascript
@general help me search for this function
```

**Example 2: Custom tool integration**
```typescript
import { tool } from "@opencode-ai/plugin"

export default tool({
  description: "Query the project database",
  args: {
    query: tool.schema.string().describe("SQL query to execute"),
  },
  async execute(args) {
    // Your database logic here
    return `Executed: ${args.query}`
  },
})
```

**Example 3: Agent prompt template**
```markdown
---
description: Reviews code for quality and best practices
mode: subagent
model: anthropic/claude-sonnet-4-20250514
temperature: 0.1
tools:
  write: false
  edit: false
  bash: false
---

You are a code review specialist. Focus on:
- Code quality and best practices
- Potential bugs and edge cases
- Performance implications
- Security considerations

Provide constructive feedback without making direct changes.
```

## Reference Documentation

This skill includes comprehensive OpenCode documentation in `.github/copilot-skills/opencode/references/`:

- **agents.md** - Complete guide to agent types, configuration, and orchestration
- **tools.md** - Tool integrations, MCP, custom tool creation
- **api.md** - OpenCode API reference and configuration
- **other.md** - Additional features (TUI, commands, themes, rules)

### Key Documentation Sections

**Multi-Agent Architecture:**
- Primary vs. subagent differences
- Tool access permissions
- Agent switching (Tab key)
- @mention delegation

**Creating Custom Agents:**
- Configuration structure
- Prompt templates
- Tool permissions
- Temperature settings

**Workflow Patterns:**
- Sequential agent chains
- Parallel coordination
- Safe refactoring flows
- Analysis pipelines

## How to Use

### For Multi-Agent Orchestration

**1. Start with planning:**
```bash
@plan analyze the authentication system
```

**2. Delegate specialized tasks:**
```bash
@test-writer add tests for auth
@docs-generator document the auth API
```

**3. Execute with @build:**
```bash
@build implement the changes
```

### For Creating Custom Agents

**1. Generate template:**
```bash
bash .github/copilot-skills/opencode/scripts/generate-agent.sh my-agent subagent
```

**2. Customize the prompt**
Create `prompts/my-agent.txt` with specialized instructions

**3. Add to config**
Update `opencode.config.json` with agent configuration

**4. Test the agent:**
```bash
@my-agent [your request]
```

### For Workflow Patterns

**View available patterns:**
```bash
bash .github/copilot-skills/opencode/scripts/orchestrate-agents.sh all
```

**Get pattern details:**
```bash
bash .github/copilot-skills/opencode/scripts/orchestrate-agents.sh refactor
```

### For Agent Reference

**See all agents:**
```bash
bash .github/copilot-skills/opencode/scripts/agent-reference.sh all
```

**Compare capabilities:**
```bash
bash .github/copilot-skills/opencode/scripts/agent-reference.sh compare
```

## 🎯 Best Practices

### Agent Selection Strategy

1. **Use @plan first** - Analyze without risk of changes
2. **Delegate to specialists** - Let each agent focus on their expertise
3. **Chain sequentially** - Build workflows that build on previous context
4. **Use @general for research** - Multi-step investigation and search
5. **Keep @build for execution** - Final implementation with full access

### Tool Permission Guidelines

- **write=false** for analysis, review, planning
- **edit=true** for refactoring, documentation updates
- **bash=true** for testing, investigation, research
- **All false** for pure analysis (most conservative)
- **All true** only for @build (full access)

### Temperature Settings

- **0.1-0.3** for code review, debugging (precision)
- **0.5-0.7** for implementation, refactoring (balanced)
- **0.8-1.0** for documentation, brainstorming (creativity)

## Bundled Scripts

This skill includes three powerful scripts for agent orchestration:

### 1. generate-agent.sh
Creates new custom agent templates
```bash
bash .github/copilot-skills/opencode/scripts/generate-agent.sh [name] [mode]
```

### 2. orchestrate-agents.sh
Shows multi-agent workflow patterns
```bash
bash .github/copilot-skills/opencode/scripts/orchestrate-agents.sh [pattern]
```

### 3. agent-reference.sh
Quick reference for agent capabilities
```bash
bash .github/copilot-skills/opencode/scripts/agent-reference.sh [agent]
```

## Related Skills

- `/create-skill` - Create new Copilot skills for other tools
- `/mcp-builder` - Build MCP servers for OpenCode tool integration
- `/git-ops` - Git workflows (useful with @plan for safe reviews)

## More Information

- **Official Documentation**: https://opencode.ai/docs
- **Agent Architecture**: `.github/copilot-skills/opencode/references/agents.md`
- **Generated**: 2025-10-19
- **Total Pages**: 20 documentation pages scraped
- **Bundled Scripts**: 3 orchestration helpers included

---

**🚀 Key Superpower**: Use OpenCode to **spawn specialized sub-agents** that handle specific tasks. Chain them together for powerful workflows: `@plan` → `@test-writer` → `@build` → `@docs-generator`. Each agent focuses on their specialty, giving you modular, composable AI assistance.

