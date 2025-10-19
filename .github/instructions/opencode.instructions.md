# OpenCode Instructions

**Auto-loaded when**: Working with files matching: `**/*.py, **/*.ts, **/*.js, **/agents/**, **/workflows/**`

## Default Behaviors

When working with OpenCode projects:

1. **Multi-Agent First**: Consider using specialized agents for specific tasks
2. **Safe Planning**: Start with @plan for analysis before making changes
3. **Tool Permissions**: Respect agent tool access (write/edit/bash restrictions)
4. **Agent Delegation**: Use @mention to invoke subagents for specialized work
5. **Sequential Workflows**: Chain agents logically (analyze → plan → execute → verify)

## Agent Orchestration Patterns

### Default Agent Selection

- **For analysis/planning**: Use @plan (read-only, safe)
- **For implementation**: Use @build (full access)
- **For research**: Delegate to @general (multi-step search)
- **For review**: Create/use @code-reviewer subagent
- **For testing**: Create/use @test-writer subagent
- **For docs**: Create/use @docs-generator subagent

### Workflow Templates

**Refactoring:**
```
@plan → @test-writer → @build
```

**Feature Development:**
```
@plan → @build → @test-writer → @docs-generator
```

**Code Review:**
```
@plan → @code-reviewer → @test-writer
```

**Debugging:**
```
@general → @debug-helper → @build
```

## Common Workflows

### Creating Custom Agents

1. Generate template:
   ```bash
   bash .github/copilot-skills/opencode/scripts/generate-agent.sh [name] [mode]
   ```

2. Create prompt file in `prompts/[name].txt`

3. Add configuration to `opencode.config.json`

4. Test with `@[name] [request]`

### Agent Configuration

**Tool Permission Guidelines:**
- Analysis agents: all tools = false
- Test agents: write + bash = true
- Doc agents: write + edit = true
- Build agent: all tools = true

**Temperature Guidelines:**
- 0.1-0.3: Code review, debugging
- 0.5-0.7: Implementation, refactoring
- 0.8-1.0: Documentation, brainstorming

### Tool Integration (MCP)

OpenCode supports Model Context Protocol for external tools:
- Add MCP servers to config
- Use built-in tools (gh_grep, file operations)
- Create custom tools with `@opencode-ai/plugin`

## Quality Guidelines

### Agent Usage
- ✅ Start with @plan for exploration
- ✅ Delegate to specialized subagents
- ✅ Use @build only for final execution
- ✅ Chain agents for complex workflows
- ⚠️ Don't bypass tool permission restrictions
- ⚠️ Don't use @build for read-only tasks

### Code Practices
- ✅ Follow OpenCode API patterns
- ✅ Use type-safe configurations
- ✅ Include agent descriptions
- ✅ Test agent prompts thoroughly
- ⚠️ Avoid overly broad agent permissions
- ⚠️ Don't create redundant agents

## Quick Reference

### Built-in Agents
- **@build** (primary): Full development access
- **@plan** (primary): Read-only analysis
- **@general** (subagent): Research and search

### Helper Scripts
```bash
# Generate agent template
bash .github/copilot-skills/opencode/scripts/generate-agent.sh [name] [mode]

# View orchestration patterns
bash .github/copilot-skills/opencode/scripts/orchestrate-agents.sh [pattern]

# Agent reference
bash .github/copilot-skills/opencode/scripts/agent-reference.sh [agent]
```

## Resources

- Skill prompt: `.github/prompts/opencode.skill.prompt.md`
- References: `.github/copilot-skills/opencode/references/`
- Official docs: https://opencode.ai/
