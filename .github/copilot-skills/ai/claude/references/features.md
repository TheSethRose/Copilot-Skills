# Claude - Features

**Pages**: 18

---

## Bash tool - Claude Docs

**URL**: https://docs.claude.com/en/docs/agents-and-tools/tool-use/bash-tool

---

## Bash tool

**URL**: https://docs.claude.com/en/docs/agents-and-tools/tool-use/bash-tool

**Contents**:
- ​Overview
- ​Model compatibility
- ​Use cases
- ​Quick start
- ​How it works
- ​Parameters
- ​Example: Multi-step automation
- ​Implement the bash tool

Set up a bash environment

Handle command execution

Process Claude's tool calls

Implement safety measures

Command execution timeout

Maintain session state

**Examples**:

```text
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    tools=[
        {
            "type": "bash_20250124",
            "name": "bash"
        }
    ],
    messages=[
        {"role": "user", "content": "List all Python files in the current directory."}
    ]
)
```

```text
// Run a command
{
  "command": "ls -la *.py"
}

// Restart the session
{
  "restart": true
}
```

```python
# User request
"Install the requests library and create a simple Python script that fetches a joke from an API, then run it."

# Claude's tool uses:
# 1. Install package
{"command": "pip install requests"}

# 2. Create script
{"command": "cat > fetch_joke.py << 'EOF'\nimport requests\nresponse = requests.get('https://official-joke-api.appspot.com/random_joke')\njoke = response.json()\nprint(f\"Setup: {joke['setup']}\")\nprint(f\"Punchline: {joke['punchline']}\")\nEOF"}

# 3. Run script
{"command
...
```

---

## Building with extended thinking

**URL**: https://docs.claude.com/en/docs/build-with-claude/extended-thinking

**Contents**:
- ​Supported models
- ​How extended thinking works
- ​How to use extended thinking
  - ​Summarized thinking
  - ​Streaming thinking
- ​Extended thinking with tool use
  - ​Preserving thinking blocks
  - ​Interleaved thinking

Example: Passing thinking blocks with tool results

Tool use without interleaved thinking

Tool use with interleaved thinking

System prompt caching (preserved when thinking changes)

Messages caching (invalidated when thinking changes)

Example: Working with redacted thinking blocks

**Examples**:

```text
{
  "content": [
    {
      "type": "thinking",
      "thinking": "Let me analyze this step by step...",
      "signature": "WaUjzkypQ2mUEVM36O2TxuC06KN8xyfbJwyem2dw3URve/op91XWHOEBLLqIOMfFG/UvLEczmEsUjavL...."
    },
    {
      "type": "text",
      "text": "Based on my analysis..."
    }
  ]
}
```

```text
curl https://api.anthropic.com/v1/messages \
     --header "x-api-key: $ANTHROPIC_API_KEY" \
     --header "anthropic-version: 2023-06-01" \
     --header "content-type: application/json" \
     --data \
'{
    "model": "claude-sonnet-4-5",
    "max_tokens": 16000,
    "thinking": {
        "type": "enabled",
        "budget_tokens": 10000
    },
    "messages": [
        {
            "role": "user",
            "content": "Are there an infinite number of prime numbers such that n mod 4 == 3?"

...
```

```text
curl https://api.anthropic.com/v1/messages \
     --header "x-api-key: $ANTHROPIC_API_KEY" \
     --header "anthropic-version: 2023-06-01" \
     --header "content-type: application/json" \
     --data \
'{
    "model": "claude-sonnet-4-5",
    "max_tokens": 16000,
    "stream": true,
    "thinking": {
        "type": "enabled",
        "budget_tokens": 10000
    },
    "messages": [
        {
            "role": "user",
            "content": "What is 27 * 453?"
        }
    ]
}'
```

---

## Code execution tool

**URL**: https://docs.claude.com/en/docs/agents-and-tools/tool-use/code-execution-tool

**Contents**:
- ​Model compatibility
- ​Quick start
- ​How code execution works
- ​How to use the tool
  - ​Execute Bash commands
  - ​Create and edit files directly
  - ​Upload and analyze your own files
    - ​Upload and analyze files

**Examples**:

```text
curl https://api.anthropic.com/v1/messages \
    --header "x-api-key: $ANTHROPIC_API_KEY" \
    --header "anthropic-version: 2023-06-01" \
    --header "anthropic-beta: code-execution-2025-08-25" \
    --header "content-type: application/json" \
    --data '{
        "model": "claude-sonnet-4-5",
        "max_tokens": 4096,
        "messages": [
            {
                "role": "user",
                "content": "Calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"

...
```

```text
curl https://api.anthropic.com/v1/messages \
    --header "x-api-key: $ANTHROPIC_API_KEY" \
    --header "anthropic-version: 2023-06-01" \
    --header "anthropic-beta: code-execution-2025-08-25" \
    --header "content-type: application/json" \
    --data '{
        "model": "claude-sonnet-4-5",
        "max_tokens": 4096,
        "messages": [{
            "role": "user",
            "content": "Check the Python version and list installed packages"
        }],
        "tools": [{
            "
...
```

```text
curl https://api.anthropic.com/v1/messages \
    --header "x-api-key: $ANTHROPIC_API_KEY" \
    --header "anthropic-version: 2023-06-01" \
    --header "anthropic-beta: code-execution-2025-08-25" \
    --header "content-type: application/json" \
    --data '{
        "model": "claude-sonnet-4-5",
        "max_tokens": 4096,
        "messages": [{
            "role": "user",
            "content": "Create a config.yaml file with database settings, then update the port from 5432 to 3306"
        }
...
```

---

## Computer use tool

**URL**: https://docs.claude.com/en/docs/agents-and-tools/tool-use/computer-use-tool

**Contents**:
- ​Overview
- ​Model compatibility
- ​Security considerations
- Computer use reference implementation
- ​Quick start
- ​How computer use works
  - ​The computing environment
- ​How to implement computer use

1. Provide Claude with the computer use tool and a user prompt

2. Claude decides to use the computer use tool

3. Extract tool input, evaluate the tool on a computer, and return results

4. Claude continues calling computer use tools until it's completed the task

Claude Sonnet 3.5 v2 (deprecated)

Set up your computing environment

Implement action handlers

Process Claude's tool calls

Implement the agent loop

Screenshot capture failure

Action execution failure

Use appropriate display resolution

Implement proper screenshot handling

Validate actions before execution

Log actions for debugging

**Examples**:

```text
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-sonnet-4-5",  # or another compatible model
    max_tokens=1024,
    tools=[
        {
          "type": "computer_20250124",
          "name": "computer",
          "display_width_px": 1024,
          "display_height_px": 768,
          "display_number": 1,
        },
        {
          "type": "text_editor_20250124",
          "name": "str_replace_editor"
        },
        {
          
...
```

```javascript
async def sampling_loop(
    *,
    model: str,
    messages: list[dict],
    api_key: str,
    max_tokens: int = 4096,
    tool_version: str,
    thinking_budget: int | None = None,
    max_iterations: int = 10,  # Add iteration limit to prevent infinite loops
):
    """
    A simple agent loop for Claude computer use interactions.

    This function handles the back-and-forth between:
    1. Sending user messages to Claude
    2. Claude requesting to use tools
    3. Your app executing those t
...
```

```text
"betas": ["computer-use-2025-01-24"]
```

---

## Embeddings

**URL**: https://docs.claude.com/en/docs/build-with-claude/embeddings

**Contents**:
- ​Before implementing embeddings
- ​How to get embeddings with Anthropic
- ​Available Models
- ​Getting started with Voyage AI
  - ​Voyage Python library
  - ​Voyage HTTP API
  - ​AWS Marketplace
- ​Quickstart example

Why do Voyage embeddings have superior quality?

What embedding models are available and which should I use?

Which similarity function should I use?

What is the relationship between characters, words, and tokens?

When and how should I use the input_type parameter?

What quantization options are available?

How can I truncate Matryoshka embeddings?

**Examples**:

```text
export VOYAGE_API_KEY="<your secret key>"
```

```text
pip install -U voyageai
```

```text
import voyageai

vo = voyageai.Client()
# This will automatically use the environment variable VOYAGE_API_KEY.
# Alternatively, you can use vo = voyageai.Client(api_key="<your secret key>")

texts = ["Sample text 1", "Sample text 2"]

result = vo.embed(texts, model="voyage-3.5", input_type="document")
print(result.embeddings[0])
print(result.embeddings[1])
```

---

## Extended thinking tips

**URL**: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/extended-thinking-tips

**Contents**:
- ​Before diving in
  - ​Technical considerations for extended thinking
- ​Prompting techniques for extended thinking
  - ​Use general instructions first, then troubleshoot with more step-by-step instructions
  - ​Multishot prompting with extended thinking
  - ​Maximizing instruction following with extended thinking
  - ​Using extended thinking to debug and steer Claude’s behavior
  - ​Making the best of long outputs and longform thinking

Complex STEM problems

Constraint optimization problems

**Examples**:

```text
Think through this math problem step by step: 
1. First, identify the variables
2. Then, set up the equation
3. Next, solve for x
...
```

```text
Please think about this math problem thoroughly and in great detail. 
Consider multiple approaches and show your complete reasoning.
Try different methods if your first approach doesn't work.
```

```text
I'm going to show you how to solve a math problem, then I want you to solve a similar one.

Problem 1: What is 15% of 80?

<thinking>
To find 15% of 80:
1. Convert 15% to a decimal: 15% = 0.15
2. Multiply: 0.15 × 80 = 12
</thinking>

The answer is 12.

Now solve this one:
Problem 2: What is 35% of 240?
```

---

## Fine-grained tool streaming

**URL**: https://docs.claude.com/en/docs/agents-and-tools/tool-use/fine-grained-tool-streaming

**Contents**:
- ​How to use fine-grained tool streaming
- ​Handling invalid JSON in tool responses

**Examples**:

```text
curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: fine-grained-tool-streaming-2025-05-14" \
  -d '{
    "model": "claude-sonnet-4-5",
    "max_tokens": 65536,
    "tools": [
      {
        "name": "make_file",
        "description": "Write text to a file",
        "input_schema": {
          "type": "object",
          "properties": {
            "filename": {
 
...
```

```text
Chunk 1: '{"'
Chunk 2: 'query": "Ty'
Chunk 3: 'peScri'
Chunk 4: 'pt 5.0 5.1 '
Chunk 5: '5.2 5'
Chunk 6: '.3'
Chunk 8: ' new f'
Chunk 9: 'eatur'
...
```

```text
Chunk 1: '{"query": "TypeScript 5.0 5.1 5.2 5.3'
Chunk 2: ' new features comparison'
```

---

## How to implement tool use

**URL**: https://docs.claude.com/en/docs/agents-and-tools/tool-use/implement-tool-use

**Contents**:
- ​Choosing a model
- ​Specifying client tools
  - ​Tool use system prompt
  - ​Best practices for tool definitions
- ​Controlling Claude’s output
  - ​Forcing tool use
  - ​JSON output
  - ​Model responses with tools

Example simple tool definition

Example of a good tool description

Example poor tool description

Complete parallel tool use example

Complete test script for parallel tools

System prompts for parallel tool use

User message prompting

Example API response with a `tool_use` content block

Example of successful tool result

Example of tool result with images

Example of empty tool result

Example of tool result with documents

<search_quality_reflection> tags

Parallel tool calls not working

**Examples**:

```text
{
  "name": "get_weather",
  "description": "Get the current weather in a given location",
  "input_schema": {
    "type": "object",
    "properties": {
      "location": {
        "type": "string",
        "description": "The city and state, e.g. San Francisco, CA"
      },
      "unit": {
        "type": "string",
        "enum": ["celsius", "fahrenheit"],
        "description": "The unit of temperature, either 'celsius' or 'fahrenheit'"
      }
    },
    "required": ["location"]
  }
}
```

```javascript
In this environment you have access to a set of tools you can use to answer the user's question.
{{ FORMATTING INSTRUCTIONS }}
String and scalar parameters should be specified as is, while lists and objects should use JSON format. Note that spaces for string values are not stripped. The output is not expected to be valid XML and is parsed with regular expressions.
Here are the functions available in JSONSchema format:
{{ TOOL DEFINITIONS IN JSON SCHEMA }}
{{ USER SYSTEM PROMPT }}
{{ TOOL CONFIGU
...
```

```text
{
  "name": "get_stock_price",
  "description": "Retrieves the current stock price for a given ticker symbol. The ticker symbol must be a valid symbol for a publicly traded company on a major US stock exchange like NYSE or NASDAQ. The tool will return the latest trade price in USD. It should be used when the user asks about the current or most recent price of a specific stock. It will not provide any other information about the stock or company.",
  "input_schema": {
    "type": "object",
    "p
...
```

---

## Memory tool

**URL**: https://docs.claude.com/en/docs/agents-and-tools/tool-use/memory-tool

**Contents**:
- ​Use cases
- ​How it works
  - ​Example: How memory tool calls work
- ​Supported models
- ​Getting started
- ​Basic usage
- ​Tool commands
  - ​view

**Examples**:

```text
"Help me respond to this customer service ticket."
```

```text
"I'll help you respond to the customer service ticket. Let me check my memory for any previous context."
```

```text
{
  "type": "tool_use",
  "id": "toolu_01C4D5E6F7G8H9I0J1K2L3M4",
  "name": "memory",
  "input": {
    "command": "view",
    "path": "/memories"
  }
}
```

---

## Memory tool - Claude Docs

**URL**: https://docs.claude.com/en/docs/agents-and-tools/tool-use/memory-tool

---

## Streaming refusals

**URL**: https://docs.claude.com/en/docs/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals

**Contents**:
- ​API response format
- ​Reset context after refusal
- ​Implementation guide
- ​Current refusal types
- ​Best practices
- ​Migration notes

**Examples**:

```text
{
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "Hello.."
    }
  ],
  "stop_reason": "refusal"
}
```

```text
# Stream request and check for refusal
response=$(curl -N https://api.anthropic.com/v1/messages \
  --header "anthropic-version: 2023-06-01" \
  --header "content-type: application/json" \
  --header "x-api-key: $ANTHROPIC_API_KEY" \
  --data '{
    "model": "claude-sonnet-4-5",
    "messages": [{"role": "user", "content": "Hello"}],
    "max_tokens": 256,
    "stream": true
  }')

# Check for refusal in the stream
if echo "$response" | grep -q '"stop_reason":"refusal"'; then
  echo "Response re
...
```

---

## Streaming refusals - Claude Docs

**URL**: https://docs.claude.com/en/docs/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals

---

## Text editor tool

**URL**: https://docs.claude.com/en/docs/agents-and-tools/tool-use/text-editor-tool

**Contents**:
- ​Model compatibility
- ​When to use the text editor tool
- ​Use the text editor tool
  - ​Text editor tool commands
    - ​view
    - ​str_replace
    - ​create
    - ​insert

Provide Claude with the text editor tool and a user prompt

Claude uses the tool to examine files or directories

Execute the view command and return results

Claude uses the tool to modify files

Execute the edit and return results

Claude provides its analysis and explanation

Example view commands

Example str_replace command

Example create command

Example insert command

Example undo_edit command

Initialize your editor implementation

Handle editor tool calls

Implement security measures

Process Claude's responses

Multiple matches for replacement

No matches for replacement

Provide clear context

Be explicit about file paths

Create backups before editing

Handle unique text replacement carefully

**Examples**:

```text
curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-sonnet-4-5",
    "max_tokens": 1024,
    "tools": [
      {
        "type": "text_editor_20250728",
        "name": "str_replace_based_edit_tool",
        "max_characters": 10000
      }
    ],
    "messages": [
      {
        "role": "user",
        "content": "There'\''s a syntax error in my primes.py fi
...
```

```text
// Example for viewing a file
{
  "type": "tool_use",
  "id": "toolu_01A09q90qw90lq917835lq9",
  "name": "str_replace_editor",
  "input": {
    "command": "view",
    "path": "primes.py"
  }
}

// Example for viewing a directory
{
  "type": "tool_use",
  "id": "toolu_02B19r91rw91mr917835mr9",
  "name": "str_replace_editor",
  "input": {
    "command": "view",
    "path": "src/"
  }
}
```

```text
{
  "type": "tool_use",
  "id": "toolu_01A09q90qw90lq917835lq9",
  "name": "str_replace_editor",
  "input": {
    "command": "str_replace",
    "path": "primes.py",
    "old_str": "for num in range(2, limit + 1)",
    "new_str": "for num in range(2, limit + 1):"
  }
}
```

---

## Token-efficient tool use

**URL**: https://docs.claude.com/en/docs/agents-and-tools/tool-use/token-efficient-tool-use

**Examples**:

```text
curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: token-efficient-tools-2025-02-19" \
  -d '{
    "model": "claude-3-7-sonnet-20250219",
    "max_tokens": 1024,
    "tools": [
      {
        "name": "get_weather",
        "description": "Get the current weather in a given location",
        "input_schema": {
          "type": "object",
          "properties": {

...
```

---

## Vision

**URL**: https://docs.claude.com/en/docs/build-with-claude/vision

**Contents**:
- ​How to use vision
- ​Before you upload
  - ​Basics and Limits
  - ​Evaluate image size
  - ​Calculate image costs
  - ​Ensuring image quality
- ​Prompt examples
  - ​About the prompt examples

Example: Multiple images

Example: Multiple images with a system prompt

Example: Four images across two conversation turns

What image file types does Claude support?

Can Claude read image URLs?

Is there a limit to the image file size I can upload?

How many images can I include in one request?

Does Claude read image metadata?

Can I delete images I've uploaded?

Where can I find details on data privacy for image uploads?

What if Claude's image interpretation seems wrong?

Can Claude generate or edit images?

**Examples**:

```text
# For URL-based images, you can use the URL directly in your JSON request
    
    # For base64-encoded images, you need to first encode the image
    # Example of how to encode an image to base64 in bash:
    BASE64_IMAGE_DATA=$(curl -s "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg" | base64)
    
    # The encoded data can now be used in your API calls
```

```text
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{
    "model": "claude-sonnet-4-5",
    "max_tokens": 1024,
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "image",
            "source": {
              "type": "base64",
              "media_type": "image/jpeg",
              "data": "'"$BASE64_IMAGE_DATA"'"
            }

...
```

```text
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{
    "model": "claude-sonnet-4-5",
    "max_tokens": 1024,
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "image",
            "source": {
              "type": "url",
              "url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.j
...
```

---

## Web fetch tool

**URL**: https://docs.claude.com/en/docs/agents-and-tools/tool-use/web-fetch-tool

**Contents**:
- ​Supported models
- ​How web fetch works
- ​How to use web fetch
  - ​Tool definition
    - ​Max uses
    - ​Domain filtering
    - ​Content limits
    - ​Citations

**Examples**:

```text
curl https://api.anthropic.com/v1/messages \
    --header "x-api-key: $ANTHROPIC_API_KEY" \
    --header "anthropic-version: 2023-06-01" \
    --header "anthropic-beta: web-fetch-2025-09-10" \
    --header "content-type: application/json" \
    --data '{
        "model": "claude-sonnet-4-5",
        "max_tokens": 1024,
        "messages": [
            {
                "role": "user",
                "content": "Please analyze the content at https://example.com/article"
            }
        ],
...
```

```text
{
  "type": "web_fetch_20250910",
  "name": "web_fetch",

  // Optional: Limit the number of fetches per request
  "max_uses": 10,

  // Optional: Only fetch from these domains
  "allowed_domains": ["example.com", "docs.example.com"],

  // Optional: Never fetch from these domains
  "blocked_domains": ["private.example.com"],

  // Optional: Enable citations for fetched content
  "citations": {
    "enabled": true
  },

  // Optional: Maximum content length in tokens
  "max_content_tokens": 1000
...
```

```text
{
  "role": "assistant",
  "content": [
    // 1. Claude's decision to fetch
    {
      "type": "text",
      "text": "I'll fetch the content from the article to analyze it."
    },
    // 2. The fetch request
    {
      "type": "server_tool_use",
      "id": "srvtoolu_01234567890abcdef",
      "name": "web_fetch",
      "input": {
        "url": "https://example.com/article"
      }
    },
    // 3. Fetch results
    {
      "type": "web_fetch_tool_result",
      "tool_use_id": "srvtoolu_0123
...
```

---

## Web search tool

**URL**: https://docs.claude.com/en/docs/agents-and-tools/tool-use/web-search-tool

**Contents**:
- ​Supported models
- ​How web search works
- ​How to use web search
  - ​Tool definition
    - ​Max uses
    - ​Domain filtering
    - ​Localization
  - ​Response

**Examples**:

```text
curl https://api.anthropic.com/v1/messages \
    --header "x-api-key: $ANTHROPIC_API_KEY" \
    --header "anthropic-version: 2023-06-01" \
    --header "content-type: application/json" \
    --data '{
        "model": "claude-sonnet-4-5",
        "max_tokens": 1024,
        "messages": [
            {
                "role": "user",
                "content": "What's the weather in NYC?"
            }
        ],
        "tools": [{
            "type": "web_search_20250305",
            "name": "
...
```

```text
{
  "type": "web_search_20250305",
  "name": "web_search",

  // Optional: Limit the number of searches per request
  "max_uses": 5,

  // Optional: Only include results from these domains
  "allowed_domains": ["example.com", "trusteddomain.org"],

  // Optional: Never include results from these domains
  "blocked_domains": ["untrustedsource.com"],

  // Optional: Localize search results
  "user_location": {
    "type": "approximate",
    "city": "San Francisco",
    "region": "California",
    
...
```

```text
{
  "role": "assistant",
  "content": [
    // 1. Claude's decision to search
    {
      "type": "text",
      "text": "I'll search for when Claude Shannon was born."
    },
    // 2. The search query used
    {
      "type": "server_tool_use",
      "id": "srvtoolu_01WYG3ziw53XMcoyKL4XcZmE",
      "name": "web_search",
      "input": {
        "query": "claude shannon birth date"
      }
    },
    // 3. Search results
    {
      "type": "web_search_tool_result",
      "tool_use_id": "srvtool
...
```

---
