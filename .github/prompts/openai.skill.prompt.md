---
description: OpenAI API - GPT-4, GPT-3.5, embeddings, vision, and assistants
---

# OpenAI

**Purpose**: Build AI-powered applications with OpenAI's API and models.

## When to Use This Skill

Use this skill when:
- Calling GPT-4, GPT-3.5, or other language models
- Working with embeddings and vector search
- Building AI assistants with the Assistants API
- Implementing vision capabilities with images
- Using text-to-speech or speech-to-text
- Working with function calling or structured outputs

**Keywords**: openai, gpt, gpt-4, embeddings, assistants, api, ai, llm, chat completion

## Quick Reference

### Basic Chat Completion

```python
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are helpful."},
        {"role": "user", "content": "Hello!"}
    ]
)

print(response.choices[0].message.content)
```

### Using Node.js/TypeScript

```typescript
import OpenAI from "openai";

const client = new OpenAI();

const completion = await client.chat.completions.create({
    model: "gpt-4",
    messages: [
        { role: "system", content: "You are helpful." },
        { role: "user", content: "Hello!" }
    ]
});

console.log(completion.choices[0].message.content);
```

### Embeddings

```python
response = client.embeddings.create(
    input="The quick brown fox",
    model="text-embedding-3-small"
)

embedding = response.data[0].embedding
print(len(embedding))  # 1536 dimensions
```

### Function Calling

```python
response = client.chat.completions.create(
    model="gpt-4",
    tools=[
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "Get weather",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {"type": "string"}
                    }
                }
            }
        }
    ],
    messages=[{"role": "user", "content": "What's the weather?"}]
)
```

### Vision with Images

```python
response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {"type": "image_url", "image_url": {"url": "https://...jpg"}}
            ]
        }
    ]
)
```

## Core Features

### Latest Models (Oct 2024)
- **GPT-5** - Latest flagship with advanced reasoning
- **o3, o4-mini** - Specialized reasoning models
- **GPT-4o** - Multi-modal (text, vision, audio)
- **GPT-4o-mini** - Cost-effective multi-modal
- **Computer-Use Preview** - UI automation (Beta)
- **GPT-4 Turbo** - High performance
- **GPT-3.5 Turbo** - Fast and affordable

### APIs
- **Chat Completions** - Conversational AI
- **Assistants** - Persistent AI agents
- **Embeddings** - Semantic search (3-small, 3-large)
- **Vision** - Image understanding
- **Audio** - Whisper (STT) & TTS
- **Images** - DALL-E generation
- **Batch** - Async processing (50% cheaper)

### Advanced Features
- **Structured Outputs** - JSON schema enforcement
- **Function Calling** - Tool integration
- **Reasoning Controls** - verbosity & reasoning_effort
- **Service Tiers** - Priority processing options
- **Safety Monitoring** - Enhanced abuse detection
- **Fine-tuning** - Custom model training

## Reference Documentation

Complete docs in `.github/copilot-skills/ai/openai/references/`:
- `getting-started.md` - Setup and authentication
- `chat-completions.md` - Chat API guide
- `assistants.md` - Assistants API
- `embeddings.md` - Vector embeddings
- `vision.md` - Image understanding
- `function-calling.md` - Tool use patterns
- `models.md` - Available models

## How to Use

1. **Get API Key**: https://platform.openai.com/account/api-keys
2. **Install SDK**: `pip install openai` or `npm install openai`
3. **Initialize client**: Set up with your API key
4. **Make requests**: Use chat completions or other APIs
5. **Handle responses**: Parse choices and manage tokens

## Setup

### Python

```bash
pip install openai
```

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")
# or set OPENAI_API_KEY env var
```

### Node.js

```bash
npm install openai
```

```typescript
import OpenAI from "openai";

const client = new OpenAI({
    apiKey: "sk-..."
});
```

## Pricing & Rate Limits

- Pay as you go (per token)
- Rate limits based on tier
- Monitor usage at: https://platform.openai.com/account/usage

## Best Practices

- ✅ Never commit API keys
- ✅ Use environment variables
- ✅ Handle rate limits with retries
- ✅ Cache embeddings when possible
- ✅ Use streaming for long responses
- ✅ Monitor token usage

## Related Skills

- `/claude` – Alternative LLM with different capabilities
- `/langchain` – Framework for building with LLMs
- `/ai-sdk` – TypeScript toolkit for AI applications
- `/fastapi` – Backend framework for API endpoints
- `/fastmcp` – MCP server for tool integration

## Related Resources

- Official Site: https://openai.com
- API Docs: https://platform.openai.com/docs
- Pricing: https://openai.com/pricing
- Community: https://community.openai.com
