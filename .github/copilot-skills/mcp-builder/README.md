---
name: mcp-builder
description: Guide for creating high-quality MCP (Model Context Protocol) servers with agent-centric tool design
version: "1.0.0"
tags: ["mcp", "model-context-protocol", "agent-tools", "api-integration", "llm"]
dependencies: ["python", "node", "typescript"]
license: Adapted from Anthropic's mcp-builder skill
---

# MCP Server Development Guide

## Overview

Create high-quality MCP (Model Context Protocol) servers that enable LLMs to effectively interact with external services through well-designed, agent-centric tools.

**Keywords**: mcp, model context protocol, mcp server, agent tools, llm integration, api integration, fastmcp, tool design

## Core Principles

### Agent-Centric Design

**Build for Workflows, Not Just API Endpoints:**
- Don't simply wrap existing API endpoints - build thoughtful workflow tools
- Consolidate related operations (e.g., `schedule_event` that checks availability AND creates)
- Focus on tools that enable complete tasks, not just individual API calls
- Consider what workflows agents actually need to accomplish

**Optimize for Limited Context:**
- Agents have constrained context windows - make every token count
- Return high-signal information, not exhaustive data dumps
- Provide "concise" vs "detailed" response format options
- Default to human-readable identifiers over technical codes (names over IDs)
- Consider the agent's context budget as a scarce resource

**Design Actionable Error Messages:**
- Error messages should guide agents toward correct usage patterns
- Suggest specific next steps: "Try using filter='active_only' to reduce results"
- Make errors educational, not just diagnostic
- Help agents learn proper tool usage through clear feedback

**Follow Natural Task Subdivisions:**
- Tool names should reflect how humans think about tasks
- Group related tools with consistent prefixes for discoverability
- Design tools around natural workflows, not just API structure

**Use Evaluation-Driven Development:**
- Create realistic evaluation scenarios early
- Let agent feedback drive tool improvements
- Prototype quickly and iterate based on actual agent performance

## Four-Phase Development Process

### Phase 1: Deep Research and Planning

#### 1.1 Study MCP Protocol Documentation
Fetch latest MCP specification:
```
https://modelcontextprotocol.io/llms-full.txt
```

#### 1.2 Study Framework Documentation

**Load reference files:**
- MCP Best Practices: `reference/mcp_best_practices.md`

**For Python:**
- Python SDK: `https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md`
- Python Guide: `reference/python_mcp_server.md`

**For TypeScript:**
- TypeScript SDK: `https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md`
- TypeScript Guide: `reference/node_mcp_server.md`

#### 1.3 Study API Documentation Exhaustively

Read ALL available API documentation:
- Official API reference documentation
- Authentication and authorization requirements
- Rate limiting and pagination patterns
- Error responses and status codes
- Available endpoints and their parameters
- Data models and schemas

#### 1.4 Create Comprehensive Implementation Plan

**Tool Selection:**
- List the most valuable endpoints/operations to implement
- Prioritize tools that enable the most common and important use cases
- Consider which tools work together to enable complex workflows

**Shared Utilities and Helpers:**
- Identify common API request patterns
- Plan pagination helpers
- Design filtering and formatting utilities
- Plan error handling strategies

**Input/Output Design:**
- Define input validation models (Pydantic for Python, Zod for TypeScript)
- Design consistent response formats (e.g., JSON or Markdown)
- Provide configurable levels of detail (e.g., Detailed or Concise)
- Plan for large-scale usage (thousands of users/resources)
- Implement character limits and truncation strategies (e.g., 25,000 tokens)

**Error Handling Strategy:**
- Plan graceful failure modes
- Design clear, actionable, LLM-friendly, natural language error messages
- Consider rate limiting and timeout scenarios
- Handle authentication and authorization errors

### Phase 2: Implementation

#### 2.1 Set Up Project Structure

**For Python:**
```
mcp_server.py           # Single file or
mcp_server/
  __init__.py
  tools.py
  utils.py
```

**For Node/TypeScript:**
```
src/
  index.ts
  tools/
  utils/
package.json
tsconfig.json
```

#### 2.2 Implement Core Infrastructure First

Create shared utilities before implementing tools:
- API request helper functions
- Error handling utilities
- Response formatting functions (JSON and Markdown)
- Pagination helpers
- Authentication/token management

#### 2.3 Implement Tools Systematically

For each tool in the plan:

**Define Input Schema:**
```python
# Python (Pydantic)
from pydantic import BaseModel

class ToolInput(BaseModel):
    required_param: str
    optional_param: str = None
```

```typescript
// TypeScript (Zod)
import { z } from "zod";

const ToolInput = z.object({
  requiredParam: z.string(),
  optionalParam: z.string().optional()
});
```

**Write Comprehensive Documentation:**
- One-line summary of what the tool does
- Detailed explanation of purpose and functionality
- Explicit parameter types with examples
- Complete return type schema
- Usage examples (when to use, when not to use)
- Error handling documentation

**Implement Tool Logic:**
- Use shared utilities to avoid code duplication
- Follow async/await patterns for all I/O
- Implement proper error handling
- Support multiple response formats (JSON and Markdown)
- Respect pagination parameters
- Check character limits and truncate appropriately

**Add Tool Annotations:**
- `readOnlyHint`: true (for read-only operations)
- `destructiveHint`: false (for non-destructive operations)
- `idempotentHint`: true (if repeated calls have same effect)
- `openWorldHint`: true (if interacting with external systems)

#### 2.4 Follow Language-Specific Best Practices

**For Python:** Load `reference/python_mcp_server.md` and ensure:
- Using MCP Python SDK with proper tool registration
- Pydantic v2 models with `model_config`
- Type hints throughout
- Async/await for all I/O operations
- Proper imports organization
- Module-level constants (CHARACTER_LIMIT, API_BASE_URL)

**For Node/TypeScript:** Load `reference/node_mcp_server.md` and ensure:
- Using `server.registerTool` properly
- Zod schemas with `.strict()`
- TypeScript strict mode enabled
- No `any` types - use proper types
- Explicit Promise<T> return types
- Build process configured (`npm run build`)

### Phase 3: Review and Refine

#### 3.1 Code Quality Review

Review the code for:
- **DRY Principle**: No duplicated code between tools
- **Composability**: Shared logic extracted into functions
- **Consistency**: Similar operations return similar formats
- **Error Handling**: All external calls have error handling
- **Type Safety**: Full type coverage (Python type hints, TypeScript types)
- **Documentation**: Every tool has comprehensive docstrings/descriptions

#### 3.2 Test and Build

**Important:** MCP servers are long-running processes. Running them directly will cause your process to hang indefinitely.

**Safe ways to test:**
- Use the evaluation harness (recommended)
- Run the server in tmux to keep it outside your main process
- Use a timeout when testing: `timeout 5s python server.py`

**For Python:**
- Verify syntax: `python -m py_compile your_server.py`
- Check imports work correctly by reviewing the file
- Use evaluation harness to test (it manages the server)

**For Node/TypeScript:**
- Run `npm run build` and ensure it completes without errors
- Verify dist/index.js is created
- Use evaluation harness to test

#### 3.3 Use Quality Checklist

Verify implementation quality:
- Python: see "Quality Checklist" in `reference/python_mcp_server.md`
- Node/TypeScript: see "Quality Checklist" in `reference/node_mcp_server.md`

### Phase 4: Create Evaluations

Create comprehensive evaluations to test effectiveness.

Load `reference/evaluation.md` for complete evaluation guidelines.

#### 4.1 Create 10 Evaluation Questions

Follow the process outlined in the evaluation guide:
1. **Tool Inspection**: List available tools and understand their capabilities
2. **Content Exploration**: Use READ-ONLY operations to explore available data
3. **Question Generation**: Create 10 complex, realistic questions
4. **Answer Verification**: Solve each question yourself to verify answers

#### 4.2 Evaluation Requirements

Each question must be:
- **Independent**: Not dependent on other questions
- **Read-only**: Only non-destructive operations required
- **Complex**: Requiring multiple tool calls and deep exploration
- **Realistic**: Based on real use cases humans would care about
- **Verifiable**: Single, clear answer that can be verified by string comparison
- **Stable**: Answer won't change over time

#### 4.3 Output Format

Create an XML file with this structure:
```xml
<evaluation>
  <qa_pair>
    <question>Complex question requiring multiple tool calls?</question>
    <answer>Verifiable answer</answer>
  </qa_pair>
  <!-- More qa_pairs... -->
</evaluation>
```

## Reference Files

Load these resources as needed during development:

### Core MCP Documentation (Load First)
- **MCP Protocol**: `https://modelcontextprotocol.io/llms-full.txt` - Complete specification
- **MCP Best Practices**: `reference/mcp_best_practices.md` - Universal guidelines

### SDK Documentation (Load During Phase 1/2)
- **Python SDK**: `https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md`
- **TypeScript SDK**: `https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md`

### Language-Specific Implementation Guides (Load During Phase 2)
- **Python Guide**: `reference/python_mcp_server.md` - Complete Python/FastMCP guide
- **TypeScript Guide**: `reference/node_mcp_server.md` - Complete TypeScript guide

### Evaluation Guide (Load During Phase 4)
- **Evaluation**: `reference/evaluation.md` - Complete evaluation creation guide

## Bundled Scripts

Scripts for validation and testing:
```bash
# Run in scripts/ directory
./validate_server.sh <server_path>
./test_evaluation.sh <server_path> <eval_file>
```

## Best Practices Summary

1. **Design for workflows**, not just API endpoints
2. **Optimize for context** - return high-signal information
3. **Make errors actionable** - guide agents to correct usage
4. **Use evaluation-driven development** - test with real scenarios
5. **Follow framework patterns** - use SDK features properly
6. **Validate all inputs** - use Pydantic/Zod schemas
7. **Handle errors gracefully** - all external calls have error handling
8. **Document thoroughly** - clear descriptions for every tool
9. **Test realistically** - use evaluation harness with complex scenarios
10. **Iterate based on feedback** - let agent usage drive improvements

## Related Skills

- **Git Ops** - Version control for MCP server development
- **Create** - Project scaffolding for new MCP servers
- **Generate Copilot Instructions** - Document MCP server usage
- **Cleanup** - Remove build artifacts
