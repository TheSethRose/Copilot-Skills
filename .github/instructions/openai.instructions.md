# OpenAI Instructions

**Auto-loaded when**: `**/*.js, **/*.ts, **/*.tsx, **/*.jsx, **/*.py, **/openai*`

## Default Behaviors

When working with OpenAI code:

1. **Never hardcode API keys** - Always use environment variables
2. **Handle rate limits** - Implement exponential backoff retry logic
3. **Stream long responses** - Use streaming for better UX
4. **Monitor tokens** - Be aware of token costs
5. **Error handling** - Always wrap API calls in try-catch
6. **Use latest models** - gpt-4o, gpt-4o-mini, or gpt-5 for best results
7. **Safety identifiers** - Use `safety_identifier` (not deprecated `user`)
8. **Optimize caching** - Use `prompt_cache_key` for better performance
9. **Reasoning models** - o3/o4-mini don't support `stop` parameter
10. **Service tiers** - Use `service_tier` for priority processing

## Common Workflows

### Initialize OpenAI Client

```python
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
```

```typescript
import OpenAI from "openai";

const client = new OpenAI({
    apiKey: process.env.OPENAI_API_KEY
});
```

### Basic Chat Completion

```python
# Latest recommended approach (Oct 2024)
response = client.chat.completions.create(
    model="gpt-4o",  # or gpt-4o-mini, gpt-5
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ],
    temperature=0.7,
    max_tokens=100,
    safety_identifier="hashed_user_id",  # New: replaces 'user'
    service_tier="auto"  # New: default, flex, or priority
)

print(response.choices[0].message.content)
```

### Using Reasoning Models

```python
# For complex reasoning tasks
response = client.chat.completions.create(
    model="gpt-5",  # or o3, o4-mini
    messages=[
        {"role": "user", "content": "Solve: If x + 5 = 12, what is x?"}
    ],
    verbosity="low",  # low, medium, or high
    reasoning_effort="medium",  # control thinking depth
    temperature=1.0
    # Note: NO 'stop' parameter on o3/o4-mini
)

print(response.choices[0].message.content)
```

### Streaming Responses

```python
with client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Tell me a story"}],
    stream=True
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```

### Error Handling

```python
from openai import RateLimitError, APIError

try:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Hello"}]
    )
except RateLimitError:
    # Wait and retry
    import time
    time.sleep(60)
except APIError as e:
    print(f"API error: {e}")
```

### Using Assistants

```python
# Create assistant
assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You are a math tutor.",
    model="gpt-4"
)

# Create thread
thread = client.beta.threads.create()

# Add message
client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="What is 2+2?"
)

# Run assistant
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id
)
```

### Embeddings for Search

```python
# Get embedding for text
embedding = client.embeddings.create(
    input="Hello world",
    model="text-embedding-3-small"
)

vector = embedding.data[0].embedding

# Later: compare vectors for similarity
from numpy import dot
from numpy.linalg import norm

similarity = dot(vector1, vector2) / (norm(vector1) * norm(vector2))
```

### Vision Analysis

```python
response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Describe this image"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://example.com/image.jpg",
                        "detail": "low"  # or "high"
                    }
                }
            ]
        }
    ]
)
```

### Function Calling

```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get weather for location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"},
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
                },
                "required": ["location"]
            }
        }
    }
]

response = client.chat.completions.create(
    model="gpt-4",
    tools=tools,
    messages=[{"role": "user", "content": "What's the weather in NYC?"}]
)

# Check if tool was called
if response.choices[0].message.tool_calls:
    for tool_call in response.choices[0].message.tool_calls:
        print(f"Tool: {tool_call.function.name}")
        print(f"Args: {tool_call.function.arguments}")
```

### Structured Output

```python
from pydantic import BaseModel

class Event(BaseModel):
    name: str
    date: str
    attendees: int

response = client.beta.chat.completions.parse(
    model="gpt-4-turbo",
    messages=[{"role": "user", "content": "Extract event details"}],
    response_format=Event
)

event = response.choices[0].message.parsed
print(event.name)
```

## Quality Guidelines

### ✅ Do

- Store API keys in environment variables
- Implement retry logic for rate limits
- Use streaming for better performance
- Monitor token usage
- Validate model names before use
- Cache embeddings appropriately
- Handle all error types
- Set temperature appropriately (0-2)
- Use max_tokens to limit costs

### ❌ Don't

- Commit API keys to version control
- Ignore rate limit errors
- Make unbounded requests
- Use deprecated models
- Hardcode configuration
- Ignore streaming opportunities
- Skip error handling
- Use production key in development

## Environment Setup

```bash
# Set API key
export OPENAI_API_KEY="sk-..."

# Or in .env file
echo "OPENAI_API_KEY=sk-..." > .env

# Python - load from .env
from dotenv import load_dotenv
load_dotenv()
```

## Token Estimation

```python
import tiktoken

encoding = tiktoken.encoding_for_model("gpt-4")
tokens = len(encoding.encode("Your text here"))
```

## Debugging

```python
# Enable debug logging
import logging
logging.basicConfig(level=logging.DEBUG)

# Or with OpenAI SDK
import httpx
client = OpenAI(
    http_client=httpx.Client(
        verify=False  # Only for debugging!
    )
)
```

## Testing

```python
# Mock responses for testing
from unittest.mock import patch, MagicMock

with patch("openai.ChatCompletion.create") as mock:
    mock.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content="test"))]
    )
    # Your test code
```

## Reference Documentation

- **API Docs**: https://platform.openai.com/docs
- **Models**: https://platform.openai.com/docs/models
- **GitHub**: https://github.com/openai/openai-python
- **Cookbook**: https://cookbook.openai.com/

## Related Skills

- `/claude` – Alternative LLM platform
- `/langchain` – Framework for LLM chains
- `/ai-sdk` – TypeScript AI toolkit
- `/fastapi` – Python backend for API endpoints
- `/fastmcp` – MCP server integration
