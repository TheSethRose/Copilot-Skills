# OpenCode Multi-Agent Orchestration Skill

> Master multi-agent orchestration with OpenCode - spawn specialized AI sub-agents, coordinate workflows, and build powerful agent-driven development pipelines.

## Overview

This skill teaches Copilot how to use **OpenCode's multi-agent architecture** - the key superpower for coordinating specialized AI agents to handle complex development tasks.

**Key Capabilities:**
- 🤖 Spawn and manage specialized sub-agents
- 🔄 Orchestrate multi-stage workflows
- 🛡️ Safe analysis with read-only agents
- ⚡ Parallel agent coordination
- 🎯 Domain-specific agent creation
- 📋 Pre-built workflow patterns

## What is OpenCode?

OpenCode is a multi-agent orchestration framework that lets you:

1. **Primary Agents** - Main assistants you switch between (Tab key)
   - `@build` - Full development access (write/edit/bash)
   - `@plan` - Read-only analysis (safe exploration)

2. **Subagents** - Specialized helpers invoked with @mention
   - `@general` - Multi-step research and code search
   - Custom agents - Code review, testing, docs, debugging

3. **Tool Permissions** - Granular control over agent capabilities
   - `write` - Create new files
   - `edit` - Modify existing files
   - `bash` - Execute commands

## Quick Start

### View Workflow Patterns

```bash
# Show all orchestration patterns
bash .github/copilot-skills/opencode/scripts/orchestrate-agents.sh all

# Specific pattern
bash .github/copilot-skills/opencode/scripts/orchestrate-agents.sh refactor
```

### Agent Reference

```bash
# Show all agents
bash .github/copilot-skills/opencode/scripts/agent-reference.sh all

# Compare capabilities
bash .github/copilot-skills/opencode/scripts/agent-reference.sh compare
```

### Create Custom Agent

```bash
# Generate template
bash .github/copilot-skills/opencode/scripts/generate-agent.sh code-reviewer subagent
```

## Multi-Agent Workflow Patterns

### 1. Safe Refactoring
```
@plan create refactoring plan for auth module
@test-writer write tests for current auth behavior
@build execute refactoring with test validation
```

**Why this works:**
- @plan analyzes without risk
- @test-writer creates safety net
- @build implements with confidence

### 2. Feature Development
```
@plan design user profile architecture
@build implement profile components
@test-writer add comprehensive tests
@docs-generator create feature documentation
```

**Why this works:**
- Sequential workflow builds context
- Each agent specializes
- Complete lifecycle coverage

### 3. Code Analysis Pipeline
```
@general find all authentication files
@plan analyze the auth flow
@code-reviewer review for security issues
```

**Why this works:**
- @general does multi-step search
- @plan maps architecture
- @code-reviewer focused analysis

### 4. Debugging Workflow
```
@general search for similar timeout issues
@debug-helper investigate session logs
@build implement the fix
```

**Why this works:**
- Research similar problems first
- Investigate before coding
- Informed implementation

## Custom Agent Archetypes

### Code Reviewer (Read-Only)
```json
{
  "mode": "subagent",
  "temperature": 0.1,
  "tools": { "write": false, "edit": false, "bash": false }
}
```
**Focus**: Quality, security, best practices

### Test Writer (Write + Bash)
```json
{
  "mode": "subagent",
  "temperature": 0.7,
  "tools": { "write": true, "edit": false, "bash": true }
}
```
**Focus**: Test generation, coverage

### Docs Generator (Write + Edit)
```json
{
  "mode": "subagent",
  "temperature": 0.8,
  "tools": { "write": true, "edit": true, "bash": false }
}
```
**Focus**: Documentation, examples

### Debug Helper (Bash Only)
```json
{
  "mode": "subagent",
  "temperature": 0.3,
  "tools": { "write": false, "edit": false, "bash": true }
}
```
**Focus**: Investigation, logs

### Refactoring Assistant (Edit Only)
```json
{
  "mode": "subagent",
  "temperature": 0.5,
  "tools": { "write": false, "edit": true, "bash": false }
}
```
**Focus**: Code improvements, patterns

## Bundled Scripts

### 1. generate-agent.sh
Creates configuration templates for custom agents.

```bash
bash .github/copilot-skills/opencode/scripts/generate-agent.sh [name] [mode]

# Examples
bash .github/copilot-skills/opencode/scripts/generate-agent.sh code-reviewer subagent
bash .github/copilot-skills/opencode/scripts/generate-agent.sh senior-dev primary
```

**Output:**
- JSON configuration for `opencode.config.json`
- Prompt template for agent behavior
- Tool permission recommendations
- Usage examples

### 2. orchestrate-agents.sh
Shows multi-agent workflow patterns.

```bash
bash .github/copilot-skills/opencode/scripts/orchestrate-agents.sh [pattern]

# Patterns
orchestrate-agents.sh analysis       # Code analysis pipeline
orchestrate-agents.sh refactor       # Safe refactoring
orchestrate-agents.sh feature        # Feature development
orchestrate-agents.sh debug          # Debugging workflow
orchestrate-agents.sh documentation  # Docs generation
orchestrate-agents.sh review         # Code review
orchestrate-agents.sh test           # Testing workflow
orchestrate-agents.sh all            # All patterns
```

**Output:**
- Step-by-step agent coordination
- Example commands
- Best practices
- When to use each pattern

### 3. agent-reference.sh
Quick reference for agent capabilities.

```bash
bash .github/copilot-skills/opencode/scripts/agent-reference.sh [agent]

# Examples
agent-reference.sh all              # All agents
agent-reference.sh build            # Build agent details
agent-reference.sh compare          # Tool access comparison
```

**Output:**
- Agent capabilities
- Tool permissions
- Use cases
- Model information
- Temperature recommendations

## Best Practices

### Agent Selection Strategy

1. **Start with @plan** - Risk-free analysis
2. **Delegate specialists** - Let experts handle their domain
3. **Chain sequentially** - Build context progressively
4. **Use @general for research** - Multi-step investigation
5. **@build for execution** - Final implementation

### Tool Permission Guidelines

| Scenario | Write | Edit | Bash | Use Case |
|----------|-------|------|------|----------|
| Analysis | ✗ | ✗ | ✗ | Code review, planning |
| Research | ✗ | ✗ | ✓ | Investigation, search |
| Testing | ✓ | ✗ | ✓ | Test generation |
| Documentation | ✓ | ✓ | ✗ | Docs, examples |
| Refactoring | ✗ | ✓ | ✗ | Code improvements |
| Full development | ✓ | ✓ | ✓ | Implementation |

### Temperature Settings

- **0.1-0.3**: Code review, debugging (precision)
- **0.5-0.7**: Implementation, refactoring (balanced)
- **0.8-1.0**: Documentation, brainstorming (creativity)

## Documentation

Comprehensive OpenCode documentation is organized in `references/`:

- **agents.md** - Agent types, configuration, orchestration
- **tools.md** - Tool integrations, MCP, custom tools
- **api.md** - OpenCode API reference
- **other.md** - TUI, commands, themes, rules

## Integration with Other Skills

### MCP Builder (`/mcp-builder`)
Create custom MCP servers for OpenCode tool integration.

```
@build with custom database tools
→ Use /mcp-builder to create MCP server
→ Add to OpenCode config
→ @build now has database access
```

### Git Ops (`/git-ops`)
Safe Git workflows with @plan review.

```
@plan review changes before commit
@code-reviewer check for issues
@build commit and push
```

## Real-World Examples

### Example 1: Secure API Development
```bash
@plan design the authentication API
@code-reviewer review security patterns
@build implement the API
@test-writer create security tests
@docs-generator document the API endpoints
```

### Example 2: Legacy Code Refactoring
```bash
@general find all usages of deprecated function
@plan create migration strategy
@test-writer add tests for current behavior
@build execute the refactoring
@code-reviewer verify no regressions
```

### Example 3: Bug Investigation
```bash
@general search for similar error messages
@debug-helper analyze stack trace and logs
@plan identify root cause
@build implement fix
@test-writer add regression tests
```

## File Structure

```
.github/copilot-skills/opencode/
├── README.md                    # This file
├── patterns.md                  # Common code patterns
├── reference.md                 # Documentation overview
├── references/                  # Organized docs
│   ├── agents.md               # Agent architecture
│   ├── tools.md                # Tool integration
│   ├── api.md                  # API reference
│   └── other.md                # Additional features
├── scripts/                     # Orchestration helpers
│   ├── generate-agent.sh       # Agent template generator
│   ├── orchestrate-agents.sh   # Workflow patterns
│   └── agent-reference.sh      # Agent capabilities
└── assets/                      # (Empty - for templates)
```

## Skill Files

- **Skill Prompt**: `.github/prompts/opencode.skill.prompt.md`
- **Instructions**: `.github/instructions/opencode.instructions.md`
- **Auto-loads when**: Editing Python/TypeScript/JavaScript, agent configs

## Contributing

To add new workflow patterns:

1. Add pattern to `orchestrate-agents.sh`
2. Document in this README
3. Test the workflow
4. Submit PR with examples

To add new agent archetypes:

1. Create example in `generate-agent.sh`
2. Document tool permissions
3. Add temperature recommendations
4. Include use cases

## Resources

- **Official OpenCode**: https://opencode.ai/docs
- **Agent Architecture**: `references/agents.md`
- **Skill Prompt**: `.github/prompts/opencode.skill.prompt.md`
- **Auto-Instructions**: `.github/instructions/opencode.instructions.md`

---

## The OpenCode Superpower 🚀

**Key Insight**: Instead of one AI doing everything, OpenCode lets you create **specialized agent teams**:

```
@plan (architect) → designs safely
@test-writer (QA) → ensures quality
@build (engineer) → implements features
@docs-generator (tech writer) → documents everything
@code-reviewer (senior dev) → reviews code
```

Each agent focuses on what they do best. Chain them together for **modular, composable AI assistance** that scales with complexity.

**This is the future of AI-assisted development** - not one assistant, but a coordinated team of specialists.
