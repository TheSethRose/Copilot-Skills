# OpenAI - Quick Reference

**Official Docs**: https://platform.openai.com/docs/

## API Overview

### Base URL
```
https://api.openai.com/v1
```

### Authentication
All requests require the `Authorization: Bearer sk-...` header with your API key.

## Models

### Latest Models

| Model | Capabilities | Context | Training |
|-------|--------------|---------|----------|
| gpt-4-turbo | Text, vision, function calling | 128K tokens | Apr 2024 |
| gpt-4 | Text, function calling | 8K tokens | Apr 2023 |
| gpt-3.5-turbo | Text, function calling | 16K tokens | Apr 2024 |
| text-embedding-3-large | Embeddings | - | Jan 2024 |
| text-embedding-3-small | Embeddings | - | Jan 2024 |

## Endpoints

### Chat Completions
```
POST /chat/completions
```

Request:
```json
{
  "model": "gpt-4",
  "messages": [
    {"role": "system", "content": "You are helpful"},
    {"role": "user", "content": "Hello"}
  ],
  "temperature": 0.7,
  "max_tokens": 100
}
```

### Embeddings
```
POST /embeddings
```

Request:
```json
{
  "input": "The text to embed",
  "model": "text-embedding-3-small"
}
```

### Images (DALL-E)
```
POST /images/generations
```

Request:
```json
{
  "prompt": "A red car",
  "model": "dall-e-3",
  "size": "1024x1024",
  "quality": "hd",
  "n": 1
}
```

## SDK Installation

### Python
```bash
pip install openai
```

### Node.js
```bash
npm install openai
```

### cURL
```bash
curl https://api.openai.com/v1/chat/completions \
  -H "Authorization: Bearer sk-..." \
  -H "Content-Type: application/json" \
  -d '{...}'
```

## Pricing (as of Oct 2024)

### Chat Completions (per 1K tokens)
- GPT-4 Turbo: $0.01 (input), $0.03 (output)
- GPT-4: $0.03 (input), $0.06 (output)
- GPT-3.5 Turbo: $0.0005 (input), $0.0015 (output)

### Embeddings (per 1M tokens)
- text-embedding-3-small: $0.02
- text-embedding-3-large: $0.13

## Rate Limits

Vary by account tier. Check dashboard for your limits:
https://platform.openai.com/account/rate-limits

## Common Response Codes

| Code | Meaning |
|------|---------|
| 200 | Success |
| 400 | Bad request |
| 401 | Authentication error |
| 429 | Rate limited |
| 500 | Server error |

## CLI Tools

### Using OpenAI CLI
```bash
pip install openai

# Set API key
export OPENAI_API_KEY="sk-..."

# Chat
openai api chat.completions.create \
  -m gpt-4 \
  -g user "Hello"
```

## Dashboard Links

- **API Keys**: https://platform.openai.com/account/api-keys
- **Usage**: https://platform.openai.com/account/usage/overview
- **Billing**: https://platform.openai.com/account/billing/overview
- **Models**: https://platform.openai.com/docs/models
