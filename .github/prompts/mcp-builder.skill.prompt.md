# MCP Server Builder Assistant

---
description: "Guide for creating high-quality MCP (Model Context Protocol) servers with agent-centric design"
---

# MCP Server Development

Build high-quality MCP (Model Context Protocol) servers that enable LLMs to effectively interact with external services through well-designed tools.

## When to Use This Skill

Use this skill when:
- Building MCP servers to integrate external APIs
- Designing tools for AI agent workflows
- Creating Python MCP servers (FastMCP/SDK)
- Creating TypeScript/Node MCP servers (MCP SDK)
- Optimizing tool design for LLM context efficiency
- Implementing agent-centric API integrations

**Keywords**: mcp, model context protocol, mcp server, agent tools, llm integration, api integration, fastmcp, tool design

## Workflow

### Step 1: Deep Research and Planning

#### 1.1 Understand Agent-Centric Design Principles

**Build for Workflows, Not Just API Endpoints:**
- Don't simply wrap API endpoints - build workflow tools
- Consolidate related operations (e.g., `schedule_event` checks availability AND creates)
- Focus on tools that enable complete tasks
- Consider what workflows agents need to accomplish

**Optimize for Limited Context:**
- Agents have constrained context windows - make every token count
- Return high-signal information, not exhaustive dumps
- Provide "concise" vs "detailed" response options
- Default to human-readable identifiers (names over IDs)
- Treat context budget as a scarce resource

**Design Actionable Error Messages:**
- Guide agents toward correct usage patterns
- Suggest specific next steps: "Try using filter='active_only'"
- Make errors educational, not just diagnostic
- Help agents learn proper tool usage

**Follow Natural Task Subdivisions:**
- Tool names reflect how humans think about tasks
- Group related tools with consistent prefixes
- Design around workflows, not just API structure

**Use Evaluation-Driven Development:**
- Create realistic evaluation scenarios early
- Let agent feedback drive improvements
- Prototype quickly and iterate based on performance

#### 1.2 Study MCP Protocol Documentation

Fetch latest documentation:
```
https://modelcontextprotocol.io/llms-full.txt
```

#### 1.3 Study Framework Documentation

**Load reference files:**
- MCP Best Practices: `.github/copilot-skills/mcp-builder/reference/mcp_best_practices.md`

**For Python:**
- Python SDK: `https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md`
- Python Guide: `.github/copilot-skills/mcp-builder/reference/python_mcp_server.md`

**For TypeScript:**
- TypeScript SDK: `https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md`
- TypeScript Guide: `.github/copilot-skills/mcp-builder/reference/node_mcp_server.md`

#### 1.4 Study API Documentation Exhaustively

Read ALL available API documentation:
- Official API reference
- Authentication/authorization requirements
- Rate limiting and pagination
- Error responses and status codes
- Available endpoints and parameters
- Data models and schemas

#### 1.5 Create Implementation Plan

**Tool Selection:**
- List most valuable endpoints/operations
- Prioritize common and important use cases
- Consider tools that work together

**Shared Utilities:**
- Common API request patterns
- Pagination helpers
- Filtering and formatting utilities
- Error handling strategies

**Input/Output Design:**
- Input validation (Pydantic/Zod)
- Consistent response formats (JSON/Markdown)
- Configurable detail levels (Detailed/Concise)
- Character limits and truncation (25,000 token max)

**Error Handling:**
- Graceful failure modes
- Clear, actionable, LLM-friendly error messages
- Rate limiting and timeout handling
- Authentication error handling

### Step 2: Implementation

#### 2.1 Set Up Project Structure

**Python:**
```bash
# Single file or module structure
mcp_server.py
# Or organized:
mcp_server/
  __init__.py
  tools.py
  utils.py
```

**TypeScript:**
```bash
# Standard structure
src/
  index.ts
  tools/
  utils/
package.json
tsconfig.json
```

#### 2.2 Implement Core Infrastructure First

Create shared utilities:
- API request helpers
- Error handling utilities
- Response formatting (JSON/Markdown)
- Pagination helpers
- Authentication/token management

#### 2.3 Implement Tools Systematically

For each tool:

**Define Input Schema:**
```python
# Python (Pydantic)
from pydantic import BaseModel

class ToolInput(BaseModel):
    param: str
    optional: str = None
```

```typescript
// TypeScript (Zod)
import { z } from "zod";

const ToolInput = z.object({
  param: z.string(),
  optional: z.string().optional()
});
```

**Implement Tool Function:**
- Validate inputs
- Make API calls with error handling
- Format response appropriately
- Handle edge cases

**Add Documentation:**
- Clear description of what tool does
- Parameter descriptions
- Example usage
- Error conditions

#### 2.4 Test Each Tool

- Test with valid inputs
- Test error conditions
- Test edge cases (empty results, rate limits)
- Verify response formatting

### Step 3: Quality Assurance

#### 3.1 Create Evaluation Scenarios

Build realistic test cases:
- Common workflow scenarios
- Edge cases and error conditions
- Performance tests (large datasets)
- Token efficiency tests

#### 3.2 Test with LLM Agents

- Run evaluation scenarios
- Collect agent feedback
- Identify confusing error messages
- Find missing workflows

#### 3.3 Iterate Based on Results

- Refine error messages
- Adjust response formats
- Add missing tools
- Optimize context usage

### Step 4: Documentation and Deployment

#### 4.1 Write Comprehensive Documentation

- README with setup instructions
- Tool usage examples
- Configuration options
- Troubleshooting guide

#### 4.2 Prepare for Distribution

**Python:**
```bash
# Package structure
setup.py
README.md
requirements.txt
```

**TypeScript:**
```bash
# NPM package
package.json
README.md
dist/
```

#### 4.3 Test Installation

- Fresh environment testing
- Dependency verification
- Configuration validation

## Examples

### Example 1: Python MCP Server Tool

```python
from mcp import FastMCP
from pydantic import BaseModel

mcp = FastMCP("my-server")

class SearchInput(BaseModel):
    query: str
    limit: int = 10

@mcp.tool()
def search_items(input: SearchInput) -> str:
    """Search for items matching query."""
    try:
        results = api.search(input.query, limit=input.limit)
        return format_results(results, concise=True)
    except APIError as e:
        return f"Search failed: {e}. Try narrowing your query."
```

### Example 2: TypeScript MCP Server Tool

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { z } from "zod";

const SearchInput = z.object({
  query: z.string(),
  limit: z.number().default(10)
});

server.tool("search_items", {
  description: "Search for items matching query",
  parameters: SearchInput
}, async ({ query, limit }) => {
  try {
    const results = await api.search(query, limit);
    return formatResults(results, { concise: true });
  } catch (error) {
    return `Search failed: ${error}. Try narrowing your query.`;
  }
});
```

## Detail Files

- **mcp_best_practices.md**: Core guidelines for all MCP servers
- **python_mcp_server.md**: Python-specific patterns and examples
- **node_mcp_server.md**: TypeScript/Node patterns and examples
- **scripts/**: Validation and testing utilities

## Notes

- MCP servers run as stdio or SSE transports
- Tools should be atomic and focused
- Error messages must be LLM-friendly and actionable
- Response formatting critical for context efficiency
- Always validate inputs with schemas
- Handle rate limiting and pagination gracefully

## Related Skills

- **Git Ops** - Version control for MCP server development
- **Create** - Project scaffolding for new MCP servers
- **Generate Copilot Instructions** - Document MCP server usage
