# OpenAI Chat Completions API

**Docs**: https://platform.openai.com/docs/api-reference/chat/create

## Overview

The Chat Completions API is the primary way to interact with OpenAI models. It accepts messages and returns a model response.

## Request Format

```python
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are helpful"},
        {"role": "user", "content": "Hello"},
        {"role": "assistant", "content": "Hi there!"},
        {"role": "user", "content": "How are you?"}
    ],
    temperature=0.7,
    max_tokens=100,
    top_p=1.0,
    frequency_penalty=0,
    presence_penalty=0
)
```

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| model | string | - | Model to use (required) |
| messages | array | - | Messages to complete (required) |
| temperature | float | 1 | Randomness (0-2) |
| max_tokens | integer | - | Max output tokens |
| top_p | float | 1 | Nucleus sampling |
| frequency_penalty | float | 0 | Repetition penalty (-2 to 2) |
| presence_penalty | float | 0 | Diversity penalty (-2 to 2) |
| stop | string/array | - | Stop sequences |
| n | integer | 1 | Number of completions |
| stream | boolean | false | Stream response |
| tools | array | - | Function tools (JSON schema) |
| tool_choice | string/object | auto | Which tool to use |

## Message Roles

- **system** - Sets behavior/context (typically first)
- **user** - Input from user
- **assistant** - Previous model response
- **tool** - Tool/function output

## Response Format

```python
{
    "id": "chatcmpl-8Pe1...",
    "object": "chat.completion",
    "created": 1699564193,
    "model": "gpt-4",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "Hello! How can I help?"
            },
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 20,
        "completion_tokens": 10,
        "total_tokens": 30
    }
}
```

## Examples

### Simple Request

```python
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "Say this is a test"}
    ]
)

print(response.choices[0].message.content)
# Output: This is a test
```

### Multi-turn Conversation

```python
messages = []

# First turn
messages.append({"role": "user", "content": "What's Python?"})
response = client.chat.completions.create(
    model="gpt-4",
    messages=messages
)
assistant_msg = response.choices[0].message.content
messages.append({"role": "assistant", "content": assistant_msg})

# Second turn
messages.append({"role": "user", "content": "How do I learn it?"})
response = client.chat.completions.create(
    model="gpt-4",
    messages=messages
)
print(response.choices[0].message.content)
```

### With Temperature Control

```python
# Creative (high temperature)
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Write a haiku"}],
    temperature=1.5  # More random
)

# Deterministic (low temperature)
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "What is 2+2?"}],
    temperature=0.1  # More focused
)
```

### Streaming

```python
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Tell a story"}],
    stream=True
)

for chunk in response:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
```

### Multiple Completions

```python
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Suggest a name"}],
    n=3,  # Get 3 options
    temperature=1.5
)

for i, choice in enumerate(response.choices):
    print(f"{i+1}. {choice.message.content}")
```

### With Stop Sequences

```python
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "List 5 things"}],
    stop=["6."]  # Stop before item 6
)
```

## Temperature Guidance

| Value | Behavior | Use Case |
|-------|----------|----------|
| 0 | Deterministic | Factual, consistent |
| 0.5-0.7 | Balanced | Most use cases |
| 1.0 | Moderate randomness | Creative tasks |
| 1.5+ | Very creative | Brainstorming |

## Finish Reasons

- `stop` - Max tokens or stop sequence reached
- `length` - Max tokens hit
- `function_call` - Model called a function
- `content_filter` - Content filtered
- `null` - Still streaming

## Best Practices

1. **System prompt** - Set behavior with system message
2. **Few-shot examples** - Show examples in messages
3. **Temperature** - Lower for facts, higher for creativity
4. **Max tokens** - Limit output length
5. **Stop sequences** - Trim unnecessary output
6. **Error handling** - Retry on rate limits

## Pricing

Based on tokens used:
- Input tokens: Cost per 1K tokens
- Output tokens: Cost per 1K tokens (usually 2x input)

Monitor at: https://platform.openai.com/account/usage/overview
