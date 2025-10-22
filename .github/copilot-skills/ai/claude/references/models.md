# Claude - Models

**Pages**: 3

---

## Claude 4 prompt engineering best practices

**URL**: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices

**Contents**:
- ​General principles
  - ​Be explicit with your instructions
  - ​Add context to improve performance
  - ​Be vigilant with examples & details
  - ​Long-horizon reasoning and state tracking
    - ​Context awareness and multi-window workflows
    - ​Multi-context window workflows
    - ​State management best practices

Example: Creating an analytics dashboard

Example: Formatting preferences

Example: State tracking

Example: Explicit instructions

**Examples**:

```text
Create an analytics dashboard
```

```text
Create an analytics dashboard. Include as many relevant features and interactions as possible. Go beyond the basics to create a fully-featured implementation.
```

```text
NEVER use ellipses
```

---

## Pricing - Claude Docs

**URL**: https://docs.claude.com/en/docs/about-claude/pricing

---

## Pricing

**URL**: https://docs.claude.com/en/docs/about-claude/pricing

**Contents**:
- ​Model pricing
- ​Third-party platform pricing
- ​Feature-specific pricing
  - ​Batch processing
  - ​Long context pricing
  - ​Tool use pricing
  - ​Specific tool pricing
    - ​Bash tool

**Examples**:

```text
{
  "usage": {
    "input_tokens": 250000,
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0,
    "output_tokens": 500
  }
}
```

```text
"usage": {
  "input_tokens": 105,
  "output_tokens": 6039,
  "cache_read_input_tokens": 7123,
  "cache_creation_input_tokens": 7345,
  "server_tool_use": {
    "web_search_requests": 1
  }
}
```

```text
"usage": {
  "input_tokens": 25039,
  "output_tokens": 931,
  "cache_read_input_tokens": 0,
  "cache_creation_input_tokens": 0,
  "server_tool_use": {
    "web_fetch_requests": 1
  }
}
```

---
