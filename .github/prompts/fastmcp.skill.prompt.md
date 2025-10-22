---
description: FastMCP - Pythonic framework for building production-ready Model Context Protocol (MCP) servers and clients
---

# FastMCP

**Purpose**: Build MCP servers and clients with minimal boilerplate using Python's FastMCP framework.

## When to Use This Skill

Use this skill when:
- Building MCP servers to expose tools, resources, or prompts to LLMs
- Creating MCP clients to interact with MCP servers
- Deploying MCP servers locally, to FastMCP Cloud, or custom infrastructure
- Implementing enterprise authentication (Google, GitHub, Azure, Auth0, WorkOS)
- Working with FastAPI integration for MCP servers
- Testing and debugging MCP implementations

**Keywords**: fastmcp, mcp, model context protocol, mcp server, mcp client, python mcp, llm tools, llm integration

## Quick Reference

### Minimal MCP Server

```python
from fastmcp import FastMCP

mcp = FastMCP("My Server")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    mcp.run()  # stdio transport by default
```

### MCP Server with HTTP Transport

```python
from fastmcp import FastMCP

mcp = FastMCP("My Server")

@mcp.tool
def greet(name: str) -> str:
    """Greet someone by name"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(transport="http", port=8000)
```

### Adding Resources

```python
@mcp.resource("config://settings")
def get_settings() -> str:
    """Return application settings"""
    return "key=value\nfoo=bar"
```

### Adding Prompts

```python
@mcp.prompt
def code_review(language: str, code: str) -> str:
    """Generate a code review prompt"""
    return f"Review this {language} code:\n\n{code}"
```

### MCP Client Usage

```python
import asyncio
from fastmcp import Client

async def main():
    async with Client("https://example.com/mcp") as client:
        # Call a tool
        result = await client.call_tool(
            name="greet",
            arguments={"name": "World"}
        )
        print(result)

asyncio.run(main())
```

## Core Concepts

### Tools
Functions that LLMs can call to perform actions:
- Decorated with `@mcp.tool`
- Automatically generate JSON schemas from type hints
- Support sync and async functions

### Resources
Data sources that LLMs can read:
- Decorated with `@mcp.resource("uri://path")`
- Provide context to LLM conversations
- Can be static or dynamic

### Prompts
Reusable templates for LLM interactions:
- Decorated with `@mcp.prompt`
- Accept parameters for customization
- Return formatted prompts

### Transports
Connection methods for servers:
- **stdio**: Local connections (default)
- **http**: Remote connections via HTTP/SSE
- **Custom**: Build your own transport layer

## Reference Documentation

Complete documentation in `.github/copilot-skills/backend/fastmcp/docs/`:

**Getting Started**:
- `getting-started/welcome.mdx` - Overview and introduction
- `getting-started/installation.mdx` - Setup instructions
- `getting-started/quickstart.mdx` - First server tutorial

**Python SDK**:
- `python-sdk/` - Complete API reference (100+ modules)

**Clients**:
- `clients/client.mdx` - Client usage
- `clients/transports.mdx` - Transport options
- `clients/auth/` - Authentication methods

**Deployment**:
- `deployment/` - Production deployment guides

**Patterns**:
- `patterns/` - Best practices and common patterns

**Servers**:
- `servers/` - Server configuration and examples

## How to Use

1. **Check documentation**: Browse `.github/copilot-skills/backend/fastmcp/docs/`
2. **Use examples above**: Copy and adapt code patterns
3. **Ask questions**: "How do I authenticate with Google?" or "Show me resource examples"
4. **Reference API**: Check `python-sdk/` for detailed API documentation

## Common Workflows

### Create New Server
```bash
# Install
pip install fastmcp

# Create server file
# (use patterns above)

# Run locally
python my_server.py

# Or use FastMCP CLI
fastmcp run my_server
```

### Deploy to FastMCP Cloud
```bash
fastmcp deploy my_server.py
```

### Test Server
```bash
fastmcp dev my_server.py
```

## Enterprise Features

- **Authentication**: Google, GitHub, Azure, Auth0, WorkOS, OAuth
- **Middleware**: Custom request/response processing
- **Logging**: Built-in structured logging
- **Testing**: Test utilities and frameworks
- **Monitoring**: Health checks and metrics

## Related Skills

- `/claude` – LLM platform that uses MCP servers
- `/openai` – Alternative LLM integration via MCP
- `/langchain` – Framework for composing AI chains
- `/fastapi` – Alternative backend framework
- `/mcp-builder` – Building custom MCP servers

## Related Resources

- Official docs: https://gofastmcp.com/
- GitHub: https://github.com/jlowin/fastmcp
- FastMCP Cloud: https://fastmcp.cloud
- MCP Protocol: https://modelcontextprotocol.io/
