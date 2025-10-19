---
description: "Auto-loaded context for MCP server development and agent-centric tool design"
applyTo: "**/*{mcp,MCP,server,model-context-protocol,fastmcp,tool}*"
---

# MCP Builder - Automatic Context Instructions

**Related Prompt:** `/mcp-builder`  
**Related Skill:** `.github/copilot-skills/mcp-builder/README.md`

**Triggers:** mcp, model context protocol, mcp server, agent tools, llm integration, api integration, fastmcp, tool design

## Context: MCP Server Development

When working with MCP-related files or when user queries contain MCP server keywords, this context is automatically activated.

## Default Behaviors

### When user mentions "mcp server" or "build mcp"
1. Suggest `/mcp-builder` skill prompt
2. Load agent-centric design principles
3. Reference framework-specific documentation
4. Use evaluation-driven development approach

### When user mentions "tool design" or "agent tools"
1. Focus on workflow-oriented tools (not just API wrappers)
2. Optimize for context efficiency
3. Design actionable error messages
4. Follow natural task subdivisions

### When user mentions "python mcp" or "fastmcp"
1. Load Python-specific patterns
2. Reference FastMCP or Python SDK documentation
3. Use Pydantic for input validation
4. Follow Python project structure conventions

### When user mentions "typescript mcp" or "node mcp"
1. Load TypeScript-specific patterns
2. Reference MCP TypeScript SDK documentation
3. Use Zod for input validation
4. Follow Node/TypeScript project conventions

## Quality Guidelines

### ✅ Do
- Build workflow tools, not just API endpoint wrappers
- Consolidate related operations into single tools
- Return high-signal information (concise by default)
- Use human-readable identifiers (names over IDs)
- Design actionable, educational error messages
- Validate all inputs with schemas (Pydantic/Zod)
- Handle rate limiting and pagination gracefully
- Test with realistic agent scenarios
- Provide configurable detail levels (concise/detailed)
- Keep responses under 25,000 tokens
- Group related tools with consistent prefixes

### ❌ Don't
- Simply wrap API endpoints without workflow consideration
- Return exhaustive data dumps (respect context limits)
- Use cryptic error messages
- Skip input validation
- Ignore rate limits or pagination
- Hard-code configuration values
- Mix workflow concerns in single tool
- Create tools with unclear purposes
- Return massive unformatted responses
- Use technical IDs when names are available

## Agent-Centric Design Principles

### Workflow-Oriented Tools

**Good Tool Design:**
```python
@mcp.tool()
def schedule_meeting(input: MeetingInput) -> str:
    """Check availability and schedule meeting in one step."""
    # 1. Check availability
    # 2. Create meeting
    # 3. Return confirmation
```

**Poor Tool Design:**
```python
@mcp.tool()
def check_availability(input: AvailabilityInput) -> str:
    """Only checks - doesn't schedule."""
    
@mcp.tool()
def create_meeting(input: MeetingInput) -> str:
    """Only creates - doesn't check."""
```

### Context Optimization

**Concise Response (Default):**
```python
return f"Found 3 results: {names_only}"
```

**Detailed Response (When Requested):**
```python
if detail_level == "detailed":
    return json.dumps(full_data, indent=2)
```

### Actionable Errors

**Good Error Message:**
```
"Search returned too many results (500+). Try adding filters: 
 - Use 'status=active' to show only active items
 - Use 'limit=50' to reduce results
 - Narrow your search query"
```

**Poor Error Message:**
```
"Error: ResultSet exceeds maximum size"
```

## Common Patterns

### Python MCP Server Structure

```python
from mcp import FastMCP
from pydantic import BaseModel

mcp = FastMCP("server-name")

# Input validation
class ToolInput(BaseModel):
    required_param: str
    optional_param: str = None

# Tool implementation
@mcp.tool()
def tool_name(input: ToolInput) -> str:
    """Clear description of what tool does."""
    try:
        result = api_call(input.required_param)
        return format_response(result, concise=True)
    except APIError as e:
        return f"Operation failed: {e}. Try [specific suggestion]"

if __name__ == "__main__":
    mcp.run()
```

### TypeScript MCP Server Structure

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { z } from "zod";

const server = new Server({
  name: "server-name",
  version: "1.0.0"
});

// Input validation
const ToolInput = z.object({
  requiredParam: z.string(),
  optionalParam: z.string().optional()
});

// Tool implementation
server.tool("tool_name", {
  description: "Clear description of what tool does",
  parameters: ToolInput
}, async (params) => {
  try {
    const result = await apiCall(params.requiredParam);
    return formatResponse(result, { concise: true });
  } catch (error) {
    return `Operation failed: ${error}. Try [specific suggestion]`;
  }
});
```

## Response Formatting

### Concise Format (Default)
```python
def format_concise(items):
    """Return high-signal summary."""
    return f"Found {len(items)} items: {', '.join(names)}"
```

### Detailed Format (Optional)
```python
def format_detailed(items):
    """Return full information."""
    return json.dumps(items, indent=2)
```

### Markdown Format (Rich Output)
```python
def format_markdown(items):
    """Return formatted markdown."""
    lines = ["# Results\n"]
    for item in items:
        lines.append(f"- **{item.name}**: {item.description}")
    return "\n".join(lines)
```

## Error Handling

### Graceful Failures
```python
try:
    result = api_call()
    return format_response(result)
except RateLimitError:
    return "Rate limit reached. Wait 60 seconds and try again."
except AuthError:
    return "Authentication failed. Check your API key."
except NetworkError as e:
    return f"Network error: {e}. Check your connection."
```

### Validation Errors
```python
try:
    input = ToolInput(**params)
except ValidationError as e:
    return f"Invalid input: {e}. Required: [list requirements]"
```

## Testing and Evaluation

### Create Realistic Scenarios
```python
# Test common workflows
test_cases = [
    "Search for active projects",
    "Create new item with details",
    "Update existing resource",
    "Handle large result sets",
    "Deal with rate limits"
]
```

### Measure Success
- Agent completes task without confusion
- Error messages lead to correct actions
- Token usage is reasonable
- Response time is acceptable
- Edge cases handled gracefully

## Reference Documentation

Load these files for detailed guidance:
- **Best Practices**: `.github/copilot-skills/mcp-builder/reference/mcp_best_practices.md`
- **Python Guide**: `.github/copilot-skills/mcp-builder/reference/python_mcp_server.md`
- **TypeScript Guide**: `.github/copilot-skills/mcp-builder/reference/node_mcp_server.md`

## Next Steps

When building MCP servers:
1. Use `/mcp-builder` prompt for guided workflow
2. Study agent-centric design principles
3. Load framework-specific documentation
4. Create implementation plan before coding
5. Build shared utilities first
6. Implement tools systematically
7. Test with realistic agent scenarios
8. Iterate based on agent feedback

## Related Skills

- **Git Ops** - Version control for MCP projects
- **Create** - Scaffold new MCP server projects
- **Generate Copilot Instructions** - Document MCP server usage
- **Cleanup** - Remove build artifacts and temporary files
