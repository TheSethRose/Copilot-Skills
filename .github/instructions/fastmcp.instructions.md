# FastMCP Instructions

**Auto-loaded when**: `**/*.py, **/mcp_*.py, **/*_server.py, **/fastmcp_*.py`

## Default Behaviors

When working with FastMCP code:

1. **Use Type Hints**: Always include type hints for tool parameters and return values
2. **Document Functions**: Add docstrings to all tools, resources, and prompts
3. **Async When Possible**: Prefer async functions for I/O operations
4. **Error Handling**: Implement proper error handling in tools
5. **Follow MCP Patterns**: Use FastMCP decorators (`@mcp.tool`, `@mcp.resource`, `@mcp.prompt`)

## Common Workflows

### Creating a New MCP Server

```python
from fastmcp import FastMCP

# 1. Initialize server
mcp = FastMCP("Server Name")

# 2. Add tools
@mcp.tool
def my_tool(param: str) -> str:
    """Tool description"""
    return f"Result: {param}"

# 3. Run server
if __name__ == "__main__":
    mcp.run()  # or mcp.run(transport="http", port=8000)
```

### Adding Resources

```python
@mcp.resource("data://config")
def get_config() -> str:
    """Return configuration data"""
    return "config_content"
```

### Adding Prompts

```python
@mcp.prompt
def analyze_code(language: str, code: str) -> str:
    """Generate code analysis prompt"""
    return f"Analyze this {language} code:\n\n{code}"
```

### Creating MCP Clients

```python
import asyncio
from fastmcp import Client

async def main():
    async with Client("http://localhost:8000/mcp") as client:
        result = await client.call_tool(
            name="my_tool",
            arguments={"param": "value"}
        )
        print(result)

asyncio.run(main())
```

## Quality Guidelines

### ✅ Do

- Use type hints for all parameters and return values
- Add descriptive docstrings to tools/resources/prompts
- Handle errors gracefully in tool implementations
- Use async/await for I/O operations
- Test tools independently before integration
- Use FastMCP's built-in authentication for security
- Deploy with FastMCP CLI for production

### ❌ Don't

- Skip type hints (they generate JSON schemas automatically)
- Forget docstrings (LLMs read them to understand tools)
- Use blocking I/O in async functions
- Expose sensitive data without authentication
- Hardcode configuration values
- Run production servers without proper error handling

## Code Patterns

### Tool with Validation

```python
from pydantic import BaseModel, Field

class SearchParams(BaseModel):
    query: str = Field(..., min_length=1)
    limit: int = Field(10, ge=1, le=100)

@mcp.tool
def search(params: SearchParams) -> list[str]:
    """Search with validated parameters"""
    # Implementation
    return results
```

### Resource with Dynamic Content

```python
@mcp.resource("logs://recent")
async def get_recent_logs() -> str:
    """Fetch recent application logs"""
    # Async I/O operation
    logs = await fetch_logs_async()
    return "\n".join(logs)
```

### Prompt with Context

```python
@mcp.prompt
def debug_error(error_message: str, stack_trace: str) -> str:
    """Generate debugging prompt with context"""
    return f"""Debug this error:

Error: {error_message}

Stack Trace:
{stack_trace}

Suggest potential fixes and root causes."""
```

## Authentication Patterns

### OAuth with Google

```python
from fastmcp.server.auth import GoogleAuthProvider

mcp = FastMCP(
    "Secure Server",
    auth_provider=GoogleAuthProvider(
        client_id="your-client-id",
        client_secret="your-secret"
    )
)
```

### Bearer Token Auth

```python
from fastmcp.server.auth import BearerAuthProvider

mcp = FastMCP(
    "API Server",
    auth_provider=BearerAuthProvider(
        token="your-secret-token"
    )
)
```

## Testing

```python
import pytest
from fastmcp import FastMCP

@pytest.fixture
def mcp_server():
    mcp = FastMCP("Test Server")
    
    @mcp.tool
    def add(a: int, b: int) -> int:
        return a + b
    
    return mcp

def test_add_tool(mcp_server):
    result = mcp_server.call_tool("add", {"a": 2, "b": 3})
    assert result == 5
```

## Deployment

### Local Development

```bash
# Run with auto-reload
fastmcp dev my_server.py

# Run in production mode
fastmcp run my_server.py --port 8000
```

### FastMCP Cloud

```bash
# Deploy to FastMCP Cloud (free for personal)
fastmcp deploy my_server.py

# View logs
fastmcp logs my-server

# Manage deployments
fastmcp ls
```

### Docker

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY my_server.py .
CMD ["python", "my_server.py"]
```

## Reference Documentation

Complete documentation available in:
- `.github/copilot-skills/backend/fastmcp/docs/getting-started/` - Getting started guides
- `.github/copilot-skills/backend/fastmcp/docs/python-sdk/` - Complete API reference
- `.github/copilot-skills/backend/fastmcp/docs/clients/` - Client usage
- `.github/copilot-skills/backend/fastmcp/docs/patterns/` - Best practices
- `.github/copilot-skills/backend/fastmcp/docs/deployment/` - Deployment guides

## Troubleshooting

### Server Won't Start
- Check port availability
- Verify FastMCP installation: `pip show fastmcp`
- Check for syntax errors in decorators

### Tool Not Found
- Ensure function is decorated with `@mcp.tool`
- Check tool name matches exactly
- Verify server is running

### Authentication Errors
- Verify auth provider configuration
- Check client credentials
- Review auth provider documentation in `docs/clients/auth/`

### Type Errors
- Add proper type hints to all parameters
- Use Pydantic models for complex types
- Check return type annotations

## AI Integration Patterns

### With Claude API

```python
import anthropic
from fastmcp import FastMCP

mcp = FastMCP("Claude Tools Server")
client = anthropic.Anthropic()

@mcp.tool
def analyze_with_claude(text: str) -> str:
    """Analyze text using Claude"""
    response = client.messages.create(
        model="claude-3-sonnet-20250219",
        max_tokens=1024,
        messages=[{"role": "user", "content": f"Analyze: {text}"}]
    )
    return response.content[0].text

@mcp.resource("ai://model-info")
def get_model_info() -> str:
    """Get available Claude model information"""
    return "Claude 3 Sonnet, Claude 3 Opus, Claude 3 Haiku"
```

### With OpenAI API

```python
from openai import OpenAI
from fastmcp import FastMCP

mcp = FastMCP("OpenAI Tools Server")
client = OpenAI()

@mcp.tool
async def call_gpt(prompt: str) -> str:
    """Call GPT with a prompt"""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

@mcp.tool
def generate_embedding(text: str) -> list[float]:
    """Generate embeddings for text"""
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding
```

### LLM Tool Discovery Pattern

```python
@mcp.prompt
def describe_available_tools() -> str:
    """Describe all available MCP tools for LLMs"""
    tools_description = """
    Available tools:
    1. analyze_with_claude - Use Claude for analysis tasks
    2. call_gpt - Use GPT for complex reasoning
    3. search_database - Query application database
    4. fetch_api - Call external APIs
    """
    return tools_description
```

## Related Skills

- `/claude` – LLM integration with MCP servers
- `/openai` – OpenAI integration patterns
- `/langchain` – Chain composition with MCP
- `/mcp-builder` – Advanced MCP server patterns
- `/fastapi` – Alternative Python backend
