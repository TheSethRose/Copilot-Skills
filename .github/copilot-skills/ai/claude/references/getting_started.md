# Claude - Getting Started

**Pages**: 21

---

## Admin API overview

**URL**: https://docs.claude.com/en/api/administration-api

**Contents**:
- ​How the Admin API works
- ​Organization roles and permissions
- ​Key concepts
  - ​Organization Members
  - ​Organization Invites
  - ​Workspaces
  - ​Workspace Members
  - ​API Keys

What permissions are needed to use the Admin API?

Can I create new API keys through the Admin API?

What happens to API keys when removing a user?

Can organization admins be removed via the API?

How long do organization invites last?

Are there limits on workspaces?

What's the Default Workspace?

How do organization roles affect Workspace access?

Which roles can be assigned in workspaces?

Can organization admin or billing members' workspace roles be changed?

What happens to workspace access when organization roles change?

**Examples**:

```text
# List organization members
curl "https://api.anthropic.com/v1/organizations/users?limit=10" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY"

# Update member role
curl "https://api.anthropic.com/v1/organizations/users/{user_id}" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY" \
  --data '{"role": "developer"}'

# Remove member
curl --request DELETE "https://api.anthropic.com/v1/organizations/users/{user_id}" 
...
```

```text
# Create invite
curl --request POST "https://api.anthropic.com/v1/organizations/invites" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY" \
  --data '{
    "email": "[email protected]",
    "role": "developer"
  }'

# List invites
curl "https://api.anthropic.com/v1/organizations/invites?limit=10" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY"

# Delete invite
curl --request DELETE "https://api.anthropic.com/v
...
```

```text
# Create workspace
curl --request POST "https://api.anthropic.com/v1/organizations/workspaces" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY" \
  --data '{"name": "Production"}'

# List workspaces
curl "https://api.anthropic.com/v1/organizations/workspaces?limit=10&include_archived=false" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY"

# Archive workspace
curl --request POST "https://api.anthropic.com/v1/or
...
```

---

## Agent SDK overview

**URL**: https://docs.claude.com/en/api/agent-sdk/overview

**Contents**:
- ​Installation
- ​SDK Options
- ​Why use the Claude Agent SDK?
- ​What can you build with the SDK?
- ​Core Concepts
  - ​Authentication
  - ​Full Claude Code Feature Support
  - ​System Prompts

**Examples**:

```text
npm install @anthropic-ai/claude-agent-sdk
```

---

## Agent Skills

**URL**: https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview

**Contents**:
- ​Why use Skills
- ​Using Skills
- ​How Skills work
  - ​Three types of Skill content, three levels of loading
  - ​Level 1: Metadata (always loaded)
  - ​Level 2: Instructions (loaded when triggered)
  - ​Level 3: Resources and code (loaded as needed)
  - ​The Skills architecture

**Examples**:

```text
---
name: PDF Processing
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
---
```

```python
# PDF Processing

## Quick start

Use pdfplumber to extract text from PDFs:

```python
import pdfplumber

with pdfplumber.open("document.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```

For advanced form filling, see [FORMS.md](FORMS.md).
```

```text
pdf-skill/
├── SKILL.md (main instructions)
├── FORMS.md (form-filling guide)
├── REFERENCE.md (detailed API reference)
└── scripts/
    └── fill_form.py (utility script)
```

---

## Agent Skills - Claude Docs

**URL**: https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview

---

## Building with Claude

**URL**: https://docs.claude.com/en/docs/overview

**Contents**:
- ​What you can do with Claude
- ​Enterprise considerations
- ​Implementing Claude
- ​Start building with Claude

Design your integration

---

## Claude Code overview - Claude Docs

**URL**: https://docs.claude.com/en/docs/claude-code/overview

---

## Claude Code overview

**URL**: https://docs.claude.com/en/docs/claude-code/overview

**Contents**:
- ​Get started in 30 seconds
- ​What Claude Code does for you
- ​Why developers love Claude Code
- ​Next steps
- Quickstart
- Common workflows
- Troubleshooting
- IDE setup

**Examples**:

```text
# Install Claude Code
npm install -g @anthropic-ai/claude-code

# Navigate to your project
cd your-awesome-project

# Start coding with Claude
claude
# You'll be prompted to log in on first use
```

---

## Enterprise deployment overview

**URL**: https://docs.claude.com/en/docs/claude-code/third-party-integrations

**Contents**:
- ​Provider comparison
- ​Cloud providers
- Amazon Bedrock
- Google Vertex AI
- ​Corporate infrastructure
- Enterprise Network
- LLM Gateway
- ​Configuration overview

**Examples**:

```text
# Enable Bedrock
export CLAUDE_CODE_USE_BEDROCK=1
export AWS_REGION=us-east-1

# Configure corporate proxy
export HTTPS_PROXY='https://proxy.example.com:8080'
```

```text
# Enable Bedrock
export CLAUDE_CODE_USE_BEDROCK=1

# Configure LLM gateway
export ANTHROPIC_BEDROCK_BASE_URL='https://your-llm-gateway.com/bedrock'
export CLAUDE_CODE_SKIP_BEDROCK_AUTH=1  # If gateway handles AWS auth
```

```text
# Enable Vertex
export CLAUDE_CODE_USE_VERTEX=1
export CLOUD_ML_REGION=us-east5
export ANTHROPIC_VERTEX_PROJECT_ID=your-project-id

# Configure corporate proxy
export HTTPS_PROXY='https://proxy.example.com:8080'
```

---

## Features overview

**URL**: https://docs.claude.com/en/docs/build-with-claude/overview

**Contents**:
- ​Core capabilities
- ​Tools

---

## Get started with Agent Skills in the API

**URL**: https://docs.claude.com/en/docs/agents-and-tools/agent-skills/quickstart

**Contents**:
- ​Prerequisites
- ​What are Agent Skills?
- ​Step 1: List available Skills
- ​Step 2: Create a presentation
- ​Step 3: Download the created file
- ​Try more examples
  - ​Create a spreadsheet
  - ​Create a Word document

**Examples**:

```text
import anthropic

client = anthropic.Anthropic()

# List Anthropic-managed Skills
skills = client.beta.skills.list(
    source="anthropic",
    betas=["skills-2025-10-02"]
)

for skill in skills.data:
    print(f"{skill.id}: {skill.display_title}")
```

```text
import anthropic

client = anthropic.Anthropic()

# Create a message with the PowerPoint Skill
response = client.beta.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [
            {
                "type": "anthropic",
                "skill_id": "pptx",
                "version": "latest"
            }
        ]
    },
    messages=[{
        "role": "user",
        "con
...
```

```text
# Extract file ID from response
file_id = None
for block in response.content:
    if block.type == 'tool_use' and block.name == 'code_execution':
        # File ID is in the tool result
        for result_block in block.content:
            if hasattr(result_block, 'file_id'):
                file_id = result_block.file_id
                break

if file_id:
    # Download the file
    file_content = client.beta.files.download(
        file_id=file_id,
        betas=["files-api-2025-04-14"]
    )
...
```

---

## Get started with Agent Skills in the API - Claude Docs

**URL**: https://docs.claude.com/en/docs/agents-and-tools/agent-skills/quickstart

---

## Get started with Claude

**URL**: https://docs.claude.com/en/docs/get-started

**Contents**:
- ​Prerequisites
- ​Call the API
- ​Next steps
- Features Overview
- Client SDKs
- Claude Cookbook

Make your first API call

**Examples**:

```text
export ANTHROPIC_API_KEY='your-api-key-here'
```

```text
curl https://api.anthropic.com/v1/messages \
  -H "Content-Type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-sonnet-4-5",
    "max_tokens": 1000,
    "messages": [
      {
        "role": "user", 
        "content": "What should I search for to find the latest developments in renewable energy?"
      }
    ]
  }'
```

```text
{
  "id": "msg_01HCDu5LRGeP2o7s2xGmxyx8",
  "type": "message", 
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "Here are some effective search strategies to find the latest renewable energy developments:\n\n## Search Terms to Use:\n- \"renewable energy news 2024\"\n- \"clean energy breakthrough\"\n- \"solar/wind/battery technology advances\"\n- \"green energy innovations\"\n- \"climate tech developments\"\n- \"energy storage solutions\"\n\n## Best Sources to Chec
...
```

---

## Guides to common use cases

**URL**: https://docs.claude.com/en/docs/about-claude/use-case-guides/overview

**Contents**:
- Ticket routing
- Customer support agent
- Content moderation
- Legal summarization

---

## Intro to Claude

**URL**: https://docs.claude.com/en/docs/intro

**Contents**:
- ​Get started
- Get started
- Learn about Claude
- Prompt Library
- ​Develop with Claude
- Developer Console
- API Reference
- Claude Cookbook

---

## Models overview

**URL**: https://docs.claude.com/en/docs/about-claude/models/overview

**Contents**:
- ​Choosing a model
  - ​Latest models comparison
- ​Prompt and output performance
- ​Migrating to Claude 4.5
- ​Get started with Claude
- Intro to Claude
- Quickstart
- Claude Console

---

## Overview

**URL**: https://docs.claude.com/en/release-notes/overview

**Contents**:
- Claude Developer Platform Updates
- Claude Apps Updates
- System Prompt Updates

---

## Overview

**URL**: https://docs.claude.com/en/api/overview

**Contents**:
- ​Accessing the API
- ​Authentication
- ​Content types
- ​Request size limits
- ​Response Headers
- ​Examples

**Examples**:

```text
curl https://api.anthropic.com/v1/messages \
     --header "x-api-key: $ANTHROPIC_API_KEY" \
     --header "anthropic-version: 2023-06-01" \
     --header "content-type: application/json" \
     --data \
'{
    "model": "claude-sonnet-4-5",
    "max_tokens": 1024,
    "messages": [
        {"role": "user", "content": "Hello, world"}
    ]
}'
```

---

## Prompt engineering overview

**URL**: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview

**Contents**:
- ​Before prompt engineering
- Prompt generator
- ​When to prompt engineer
- ​How to prompt engineer
- ​Prompt engineering tutorial
- GitHub prompting tutorial
- Google Sheets prompting tutorial

Prompting vs. finetuning

---

## Quickstart

**URL**: https://docs.claude.com/en/docs/claude-code/quickstart

**Contents**:
- ​Before you begin
- ​Step 1: Install Claude Code
  - ​NPM Install
  - ​Native Install
- ​Step 2: Log in to your account
- ​Step 3: Start your first session
- ​Step 4: Ask your first question
- ​Step 5: Make your first code change

Be specific with your requests

Use step-by-step instructions

Let Claude explore first

Save time with shortcuts

**Examples**:

```text
npm install -g @anthropic-ai/claude-code
```

```text
brew install --cask claude-code
```

```text
curl -fsSL https://claude.ai/install.sh | bash
```

---

## Tool use with Claude

**URL**: https://docs.claude.com/en/docs/agents-and-tools/tool-use/overview

**Contents**:
- ​How tool use works
  - ​Client tools
  - ​Server tools
- ​Tool use examples
- ​Pricing
- ​Next Steps
- Calculator Tool
- Customer Service Agent

Provide Claude with tools and a user prompt

Claude decides to use a tool

Execute the tool and return results

Claude uses tool result to formulate a response

Provide Claude with tools and a user prompt

Claude executes the server tool

Claude uses the server tool result to formulate a response

Multiple tool example

Chain of thought tool use

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
        "name": "get_weather",
        "description": "Get the current weather in a given location",
        "input_schema": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
         
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
    "max_tokens": 1024,
    "tools": [{
        "name": "get_weather",
        "description": "Get the current weather in a given location",
        "input_schema": {
            "type": "object",
            "properties": {
                "location": {
    
...
```

```text
{
  "id": "msg_01Aq9w938a90dw8q",
  "model": "claude-sonnet-4-5",
  "stop_reason": "tool_use",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "I'll check the current weather in San Francisco for you."
    },
    {
      "type": "tool_use",
      "id": "toolu_01A09q90qw90lq917835lq9",
      "name": "get_weather",
      "input": {"location": "San Francisco, CA", "unit": "celsius"}
    }
  ]
}
```

---

## 

**URL**: https://docs.claude.com/en/resources/overview

**Contents**:
- Quickstarts
- Courses
- Cookbook
- Prompt library
- API primer for Claude ingestion
- Claude 3 Model Card
- Claude Sonnet 3.7 System Card
- Claude 4 System Card

---
