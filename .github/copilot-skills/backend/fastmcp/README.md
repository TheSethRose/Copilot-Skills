# FastMCP Skill

**FastMCP** - Pythonic framework for building production-ready Model Context Protocol (MCP) servers and clients.

## What is This?

This skill provides comprehensive documentation and guidance for working with FastMCP, the standard framework for building MCP applications in Python.

## Skill Structure

```
.github/copilot-skills/backend/fastmcp/
├── README.md                    # This file
├── docs/                        # Complete FastMCP documentation (from official repo)
│   ├── getting-started/         # Installation, quickstart, welcome
│   ├── python-sdk/              # Complete API reference (100+ modules)
│   ├── clients/                 # Client usage and auth
│   ├── servers/                 # Server configuration
│   ├── deployment/              # Production deployment
│   ├── patterns/                # Best practices
│   ├── tutorials/               # Step-by-step guides
│   └── integrations/            # Third-party integrations
```

## How to Use

### 1. Quick Reference
Check `/fastmcp` in Copilot Chat for:
- Common code patterns
- Tool/resource/prompt examples
- Client usage
- Authentication setup

### 2. Browse Documentation
Full documentation in `docs/`:
- **Getting Started**: `docs/getting-started/` - Installation and quickstart
- **API Reference**: `docs/python-sdk/` - Complete FastMCP API
- **Clients**: `docs/clients/` - Client usage and authentication
- **Deployment**: `docs/deployment/` - Production deployment guides
- **Patterns**: `docs/patterns/` - Best practices and common patterns

### 3. Auto-Loaded Context
Instructions automatically load when editing:
- `**/*.py` - Any Python file
- `**/mcp_*.py` - MCP-related Python files
- `**/*_server.py` - Server files
- `**/fastmcp_*.py` - FastMCP-specific files

## Key Features

### Tools
Expose functions LLMs can call:
```python
@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b
```

### Resources
Provide data sources LLMs can read:
```python
@mcp.resource("config://settings")
def get_settings() -> str:
    """Return application settings"""
    return "key=value"
```

### Prompts
Create reusable LLM prompt templates:
```python
@mcp.prompt
def code_review(language: str, code: str) -> str:
    """Generate code review prompt"""
    return f"Review this {language} code:\n\n{code}"
```

### Clients
Interact with MCP servers:
```python
import asyncio
from fastmcp import Client

async def main():
    async with Client("http://localhost:8000/mcp") as client:
        result = await client.call_tool("add", {"a": 2, "b": 3})
        print(result)

asyncio.run(main())
```

## Enterprise Features

- **Authentication**: Google, GitHub, Azure, Auth0, WorkOS, OAuth
- **Transports**: stdio, HTTP/SSE, custom
- **Middleware**: Request/response processing
- **Testing**: Built-in test utilities
- **Deployment**: FastMCP Cloud, Docker, custom infrastructure
- **Logging**: Structured logging and monitoring

## Documentation Organization

### By Topic
- **Getting Started** → `docs/getting-started/`
- **Core Concepts** → `docs/python-sdk/` (servers, tools, resources, prompts)
- **Client Usage** → `docs/clients/`
- **Authentication** → `docs/clients/auth/`
- **Deployment** → `docs/deployment/`
- **Best Practices** → `docs/patterns/`
- **Examples** → `docs/tutorials/`

### By Use Case
- **Build Server** → `getting-started/quickstart.mdx`
- **Add Tools** → `python-sdk/` (search for "tool")
- **Add Resources** → `python-sdk/` (search for "resource")
- **Add Prompts** → `python-sdk/` (search for "prompt")
- **Connect Client** → `clients/client.mdx`
- **Authenticate** → `clients/auth/`
- **Deploy** → `deployment/`
- **Test** → `patterns/` (search for "test")

## Quick Links

- **Official Site**: https://gofastmcp.com/
- **GitHub**: https://github.com/jlowin/fastmcp
- **FastMCP Cloud**: https://fastmcp.cloud
- **MCP Protocol**: https://modelcontextprotocol.io/
- **Installation**: `pip install fastmcp`

## Common Commands

```bash
# Install
pip install fastmcp

# Run server (stdio)
python my_server.py

# Run server (HTTP)
python my_server.py --transport http --port 8000

# Or use CLI
fastmcp run my_server.py

# Development mode (auto-reload)
fastmcp dev my_server.py

# Deploy to FastMCP Cloud
fastmcp deploy my_server.py

# View logs
fastmcp logs my-server

# List deployments
fastmcp ls
```

## Related Skills

- **MCP Builder** (`/mcp-builder`) - General MCP server development
- **Python** (`/python`) - Python language features
- **FastAPI** (`/fastapi`) - FastAPI integration patterns

## Updates

Documentation synchronized from official FastMCP repository:
- **Source**: https://github.com/jlowin/fastmcp/tree/main/docs
- **Last Updated**: October 21, 2025
- **Version**: FastMCP 2.0

For the latest documentation, refer to the official site or the `docs/` directory in this skill.
