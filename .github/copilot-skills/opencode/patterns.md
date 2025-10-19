# Opencode - Common Patterns

Quick reference for common opencode patterns and usage.

## Code Patterns

### 1. OpenCode provides an interactive terminal interface or TUI for working on your projects with an LLM.

```
opencode
```

### 2. OpenCode provides an interactive terminal interface or TUI for working on your projects with an LLM.

```
opencode
```

### 3. OpenCode provides an interactive terminal interface or TUI for working on your projects with an LLM.

```
opencode
```

### 4. When using the OpenCode TUI, you can type / followed by a command name to quickly execute actions. F

```
/
```

### 5. You can add external tools to OpenCode using the Model Context Protocol, or MCP. OpenCode supports b

```
mcp
```

### 6. You can add external tools to OpenCode using the Model Context Protocol, or MCP. OpenCode supports b

```
mcp
```

### 7. You can add external tools to OpenCode using the Model Context Protocol, or MCP. OpenCode supports b

```
mcp
```

### 8. AGENTS.mdIf you are unsure how to do something, use `gh_grep` to search code examples from github.

```
If you are unsure how to do something, use `gh_grep` to search code examples from github.
```

## Examples

### Example 1

```javascript
@general help me search for this function
```

### Example 2

```python
import { tool } from "@opencode-ai/plugin"
export default tool({  description: "Query the project database",  args: {    query: tool.schema.string().describe("SQL query to execute"),  },  async execute(args) {    // Your database logic here    return `Executed query: ${args.query}`  },})
```


## Categories

See organized documentation in `references/`:

- `references/agents.md` - Agents
- `references/api.md` - Api
- `references/other.md` - Other
- `references/tools.md` - Tools
