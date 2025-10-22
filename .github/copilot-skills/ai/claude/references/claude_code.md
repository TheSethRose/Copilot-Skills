# Claude - Claude Code

**Pages**: 53

---

## Agent Skills

**URL**: https://docs.claude.com/en/docs/claude-code/skills

**Contents**:
- ​Prerequisites
- ​What are Agent Skills?
- ​Create a Skill
  - ​Personal Skills
  - ​Project Skills
  - ​Plugin Skills
- ​Write SKILL.md
- ​Add supporting files

**Examples**:

```text
mkdir -p ~/.claude/skills/my-skill-name
```

```text
mkdir -p .claude/skills/my-skill-name
```

```text
---
name: Your Skill Name
description: Brief description of what this Skill does and when to use it
---

# Your Skill Name

## Instructions
Provide clear, step-by-step guidance for Claude.

## Examples
Show concrete examples of using this Skill.
```

---

## Analytics

**URL**: https://docs.claude.com/en/docs/claude-code/analytics

**Contents**:
- ​Access analytics
  - ​Required roles
- ​Available metrics
  - ​Lines of code accepted
  - ​Suggestion accept rate
  - ​Activity
  - ​Spend
  - ​Team insights

---

## CLI reference

**URL**: https://docs.claude.com/en/docs/claude-code/cli-reference

**Contents**:
- ​CLI commands
- ​CLI flags
  - ​Agents flag format
- ​See also

**Examples**:

```text
claude --agents '{
  "code-reviewer": {
    "description": "Expert code reviewer. Use proactively after code changes.",
    "prompt": "You are a senior code reviewer. Focus on code quality, security, and best practices.",
    "tools": ["Read", "Grep", "Glob", "Bash"],
    "model": "sonnet"
  },
  "debugger": {
    "description": "Debugging specialist for errors and test failures.",
    "prompt": "You are an expert debugger. Analyze errors, identify root causes, and provide fixes."
  }
}'
```

---

## Checkpointing

**URL**: https://docs.claude.com/en/docs/claude-code/checkpointing

**Contents**:
- ​How checkpoints work
  - ​Automatic tracking
  - ​Rewinding changes
- ​Common use cases
- ​Limitations
  - ​Bash command changes not tracked
  - ​External changes not tracked
  - ​Not a replacement for version control

**Examples**:

```text
rm file.txt
mv old.txt new.txt
cp source.txt dest.txt
```

---

## Claude Code GitHub Actions

**URL**: https://docs.claude.com/en/docs/claude-code/github-actions

**Contents**:
- ​Why use Claude Code GitHub Actions?
- ​What can Claude do?
  - ​Claude Code Action
- ​Setup
- ​Quick setup
- ​Manual setup
- ​Upgrading from Beta
  - ​Essential changes

Create a custom GitHub App (Recommended for 3P Providers)

Configure cloud provider authentication

Create workflow files

Google Vertex AI workflow

**Examples**:

```text
- uses: anthropics/claude-code-action@beta
  with:
    mode: "tag"
    direct_prompt: "Review this PR for security issues"
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
    custom_instructions: "Follow our coding standards"
    max_turns: "10"
    model: "claude-3-5-sonnet-20241022"
```

```text
- uses: anthropics/claude-code-action@v1
  with:
    prompt: "Review this PR for security issues"
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
    claude_args: |
      --system-prompt "Follow our coding standards"
      --max-turns 10
      --model claude-sonnet-4-5-20250929
```

```text
name: Claude Code
on:
  issue_comment:
    types: [created]
  pull_request_review_comment:
    types: [created]
jobs:
  claude:
    runs-on: ubuntu-latest
    steps:
      - uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          # Responds to @claude mentions in comments
```

---

## Claude Code GitLab CI/CD

**URL**: https://docs.claude.com/en/docs/claude-code/gitlab-ci-cd

**Contents**:
- ​Why use Claude Code with GitLab?
- ​How it works
- ​What can Claude do?
- ​Setup
  - ​Quick setup
  - ​Manual setup (recommended for production)
- ​Example use cases
  - ​Turn issues into MRs

**Examples**:

```text
stages:
  - ai

claude:
  stage: ai
  image: node:24-alpine3.21
  # Adjust rules to fit how you want to trigger the job:
  # - manual runs
  # - merge request events
  # - web/API triggers when a comment contains '@claude'
  rules:
    - if: '$CI_PIPELINE_SOURCE == "web"'
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
  variables:
    GIT_STRATEGY: fetch
  before_script:
    - apk update
    - apk add --no-cache git curl bash
    - npm install -g @anthropic-ai/claude-code
  script:
   
...
```

```text
@claude implement this feature based on the issue description
```

```text
@claude suggest a concrete approach to cache the results of this API call
```

---

## Claude Code

**URL**: https://docs.claude.com/en/release-notes/claude-code

---

## Claude Code on Amazon Bedrock - Claude Docs

**URL**: https://docs.claude.com/en/docs/claude-code/amazon-bedrock

---

## Claude Code on Amazon Bedrock

**URL**: https://docs.claude.com/en/docs/claude-code/amazon-bedrock

**Contents**:
- ​Prerequisites
- ​Setup
  - ​1. Enable model access
  - ​2. Configure AWS credentials
    - ​Advanced credential configuration
      - Example configuration
      - Configuration settings explained
  - ​3. Configure Claude Code

**Examples**:

```text
aws configure
```

```text
export AWS_ACCESS_KEY_ID=your-access-key-id
export AWS_SECRET_ACCESS_KEY=your-secret-access-key
export AWS_SESSION_TOKEN=your-session-token
```

```text
aws sso login --profile=<your-profile-name>

export AWS_PROFILE=your-profile-name
```

---

## Claude Code on Google Vertex AI

**URL**: https://docs.claude.com/en/docs/claude-code/google-vertex-ai

**Contents**:
- ​Prerequisites
- ​Region Configuration
- ​Setup
  - ​1. Enable Vertex AI API
  - ​2. Request model access
  - ​3. Configure GCP credentials
  - ​4. Configure Claude Code
  - ​5. Model configuration

**Examples**:

```text
# Set your project ID
gcloud config set project YOUR-PROJECT-ID

# Enable Vertex AI API
gcloud services enable aiplatform.googleapis.com
```

```text
# Enable Vertex AI integration
export CLAUDE_CODE_USE_VERTEX=1
export CLOUD_ML_REGION=global
export ANTHROPIC_VERTEX_PROJECT_ID=YOUR-PROJECT-ID

# Optional: Disable prompt caching if needed
export DISABLE_PROMPT_CACHING=1

# When CLOUD_ML_REGION=global, override region for unsupported models
export VERTEX_REGION_CLAUDE_3_5_HAIKU=us-east5

# Optional: Override regions for other specific models
export VERTEX_REGION_CLAUDE_3_5_SONNET=us-east5
export VERTEX_REGION_CLAUDE_3_7_SONNET=us-east5
export V
...
```

```text
export ANTHROPIC_MODEL='claude-opus-4-1@20250805'
export ANTHROPIC_SMALL_FAST_MODEL='claude-haiku-4-5@20251001'
```

---

## Claude Code on the web

**URL**: https://docs.claude.com/en/docs/claude-code/claude-code-on-the-web

**Contents**:
- ​What is Claude Code on the web?
- ​Who can use Claude Code on the web?
- ​Getting started
- ​How it works
- ​Moving tasks between web and terminal
  - ​From web to terminal
- ​Cloud environment
  - ​Default image

**Examples**:

```text
check-tools
```

```text
API_KEY=your_api_key
DEBUG=true
```

```text
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/scripts/install_pkgs.sh"
          }
        ]
      }
    ]
  }
}
```

---

## Claude Code settings

**URL**: https://docs.claude.com/en/docs/claude-code/settings

**Contents**:
- ​Settings files
  - ​Available settings
  - ​Permission settings
  - ​Sandbox settings
  - ​Settings precedence
  - ​Key points about the configuration system
  - ​System prompt availability
  - ​Excluding sensitive files

**Examples**:

```text
{
  "permissions": {
    "allow": [
      "Bash(npm run lint)",
      "Bash(npm run test:*)",
      "Read(~/.zshrc)"
    ],
    "deny": [
      "Bash(curl:*)",
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secrets/**)"
    ]
  },
  "env": {
    "CLAUDE_CODE_ENABLE_TELEMETRY": "1",
    "OTEL_METRICS_EXPORTER": "otlp"
  }
}
```

```text
{
  "sandbox": {
    "enabled": true,
    "autoAllowBashIfSandboxed": true,
    "excludedCommands": ["docker"],
    "network": {
      "allowUnixSockets": [
        "/var/run/docker.sock"
      ],
      "allowLocalBinding": true
    }
  },
  "permissions": {
    "deny": [
      "Read(.envrc)",
      "Read(~/.aws/**)"
    ]
  }
}
```

```text
{
  "permissions": {
    "deny": [
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secrets/**)",
      "Read(./config/credentials.json)",
      "Read(./build)"
    ]
  }
}
```

---

## Common workflows

**URL**: https://docs.claude.com/en/docs/claude-code/common-workflows

**Contents**:
- ​Understand new codebases
  - ​Get a quick codebase overview
  - ​Find relevant code
- ​Fix bugs efficiently
- ​Refactor code
- ​Use specialized subagents
- ​Use Plan Mode for safe code analysis
  - ​When to use Plan Mode

Navigate to the project root directory

Ask for a high-level overview

Dive deeper into specific components

Ask Claude to find relevant files

Get context on how components interact

Understand the execution flow

Share the error with Claude

Ask for fix recommendations

Identify legacy code for refactoring

Get refactoring recommendations

Apply the changes safely

Verify the refactoring

View available subagents

Use subagents automatically

Explicitly request specific subagents

Create custom subagents for your workflow

Identify untested code

Generate test scaffolding

Add meaningful test cases

Summarize your changes

Generate a PR with Claude

Identify undocumented code

Generate documentation

Add an image to the conversation

Ask Claude to analyze the image

Use images for context

Get code suggestions from visual content

Reference a single file

Reference a directory

Reference MCP resources

Provide context and ask Claude to think

Refine the thinking with follow-up prompts

Continue the most recent conversation

Continue in non-interactive mode

Show conversation picker

Understand Git worktrees

Create a new worktree

Run Claude Code in each worktree

Run Claude in another worktree

Manage your worktrees

Use text format (default)

Use streaming JSON format

Create a commands directory in your project

Create a Markdown file for each command

Use your custom command in Claude Code

Create a command file with the $ARGUMENTS placeholder

Use the command with an issue number

Create a commands directory in your home folder

Create a Markdown file for each command

Use your personal custom command

**Examples**:

```text
cd /path/to/project
```

```text
> give me an overview of this codebase
```

```text
> explain the main architecture patterns used here
```

---

## Connect Claude Code to tools via MCP

**URL**: https://docs.claude.com/en/docs/claude-code/mcp

**Contents**:
- ​What you can do with MCP
- ​Popular MCP servers
  - Development & Testing Tools
  - Project Management & Documentation
  - Databases & Data Management
  - Payments & Commerce
  - Design & Media
  - Infrastructure & DevOps

Add the server that requires authentication

Use the /mcp command within Claude Code

Add an MCP server from JSON

Verify the server was added

Import servers from Claude Desktop

Select which servers to import

Verify the servers were imported

List available resources

Reference a specific resource

Multiple resource references

Discover available prompts

Execute a prompt without arguments

Execute a prompt with arguments

**Examples**:

```text
# Basic syntax
claude mcp add --transport http <name> <url>

# Real example: Connect to Notion
claude mcp add --transport http notion https://mcp.notion.com/mcp

# Example with Bearer token
claude mcp add --transport http secure-api https://api.example.com/mcp \
  --header "Authorization: Bearer your-token"
```

```text
# Basic syntax
claude mcp add --transport sse <name> <url>

# Real example: Connect to Asana
claude mcp add --transport sse asana https://mcp.asana.com/sse

# Example with authentication header
claude mcp add --transport sse private-api https://api.company.com/sse \
  --header "X-API-Key: your-key-here"
```

```text
# Basic syntax
claude mcp add --transport stdio <name> <command> [args...]

# Real example: Add Airtable server
claude mcp add --transport stdio airtable --env AIRTABLE_API_KEY=YOUR_KEY \
  -- npx -y airtable-mcp-server
```

---

## Data usage

**URL**: https://docs.claude.com/en/docs/claude-code/data-usage

**Contents**:
- ​Data policies
  - ​Data training policy
  - ​Development Partner Program
  - ​Feedback using the /bug command
  - ​Data retention
- ​Data flow and dependencies
  - ​Cloud execution
- ​Telemetry services

---

## Development containers

**URL**: https://docs.claude.com/en/docs/claude-code/devcontainer

**Contents**:
- ​Key features
- ​Getting started in 4 steps
- ​Configuration breakdown
- ​Security features
- ​Customization options
- ​Example use cases
  - ​Secure client work
  - ​Team onboarding

---

## Development containers - Claude Docs

**URL**: https://docs.claude.com/en/docs/claude-code/devcontainer

---

## Enterprise network configuration

**URL**: https://docs.claude.com/en/docs/claude-code/network-config

**Contents**:
- ​Proxy configuration
  - ​Environment variables
  - ​Basic authentication
- ​Custom CA certificates
- ​mTLS authentication
- ​Network access requirements
- ​Additional resources

**Examples**:

```text
# HTTPS proxy (recommended)
export HTTPS_PROXY=https://proxy.example.com:8080

# HTTP proxy (if HTTPS not available)
export HTTP_PROXY=http://proxy.example.com:8080

# Bypass proxy for specific requests - space-separated format
export NO_PROXY="localhost 192.168.1.1 example.com .example.com"
# Bypass proxy for specific requests - comma-separated format
export NO_PROXY="localhost,192.168.1.1,example.com,.example.com"
# Bypass proxy for all requests
export NO_PROXY="*"
```

```text
export HTTPS_PROXY=http://username:password@proxy.example.com:8080
```

```text
export NODE_EXTRA_CA_CERTS=/path/to/ca-cert.pem
```

---

## Get started with Claude Code hooks

**URL**: https://docs.claude.com/en/docs/claude-code/hooks-guide

**Contents**:
- ​Hook Events Overview
- ​Quickstart
  - ​Prerequisites
  - ​Step 1: Open hooks configuration
  - ​Step 2: Add a matcher
  - ​Step 3: Add the hook
  - ​Step 4: Save your configuration
  - ​Step 5: Verify your hook

**Examples**:

```text
jq -r '"\(.tool_input.command) - \(.tool_input.description // "No description")"' >> ~/.claude/bash-command-log.txt
```

```text
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '\"\\(.tool_input.command) - \\(.tool_input.description // \"No description\")\"' >> ~/.claude/bash-command-log.txt"
          }
        ]
      }
    ]
  }
}
```

```text
cat ~/.claude/bash-command-log.txt
```

---

## Headless mode

**URL**: https://docs.claude.com/en/docs/claude-code/headless

**Contents**:
- ​Overview
- ​Basic usage
- ​Configuration Options
- ​Multi-turn conversations
- ​Output Formats
  - ​Text Output (Default)
  - ​JSON Output
  - ​Streaming JSON Output

**Examples**:

```text
claude -p "Stage my changes and write a set of commits for them" \
  --allowedTools "Bash,Read" \
  --permission-mode acceptEdits
```

```text
# Continue the most recent conversation
claude --continue "Now refactor this for better performance"

# Resume a specific conversation by session ID
claude --resume 550e8400-e29b-41d4-a716-446655440000 "Update the tests"

# Resume in non-interactive mode
claude --resume 550e8400-e29b-41d4-a716-446655440000 "Fix all linting issues" --no-interactive
```

```typescript
claude -p "Explain file src/components/Header.tsx"
# Output: This is a React component showing...
```

---

## Headless mode - Claude Docs

**URL**: https://docs.claude.com/en/docs/claude-code/headless

---

## Hooks reference

**URL**: https://docs.claude.com/en/docs/claude-code/hooks

**Contents**:
- ​Configuration
  - ​Structure
  - ​Project-Specific Hook Scripts
  - ​Plugin hooks
- ​Hook Events
  - ​PreToolUse
  - ​PostToolUse
  - ​Notification

**Examples**:

```text
{
  "hooks": {
    "EventName": [
      {
        "matcher": "ToolPattern",
        "hooks": [
          {
            "type": "command",
            "command": "your-command-here"
          }
        ]
      }
    ]
  }
}
```

```text
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/path/to/prompt-validator.py"
          }
        ]
      }
    ]
  }
}
```

```text
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/check-style.sh"
          }
        ]
      }
    ]
  }
}
```

---

## Identity and Access Management

**URL**: https://docs.claude.com/en/docs/claude-code/iam

**Contents**:
- ​Authentication methods
  - ​Claude API authentication
  - ​Cloud provider authentication
- ​Access control and permissions
  - ​Permission system
  - ​Configuring permissions
    - ​Permission modes
    - ​Working directories

---

## Interactive mode

**URL**: https://docs.claude.com/en/docs/claude-code/interactive-mode

**Contents**:
- ​Keyboard shortcuts
  - ​General controls
  - ​Multiline input
  - ​Quick commands
- ​Vim editor mode
  - ​Mode switching
  - ​Navigation (NORMAL mode)
  - ​Editing (NORMAL mode)

**Examples**:

```text
! npm test
! git status
! ls -la
```

---

## Interactive mode - Claude Docs

**URL**: https://docs.claude.com/en/docs/claude-code/interactive-mode

---

## JetBrains IDEs

**URL**: https://docs.claude.com/en/docs/claude-code/jetbrains

**Contents**:
- ​Supported IDEs
- ​Features
- ​Installation
  - ​Marketplace Installation
  - ​Auto-Installation
- ​Usage
  - ​From Your IDE
  - ​From External Terminals

**Examples**:

```text
claude
> /ide
```

---

## LLM gateway configuration

**URL**: https://docs.claude.com/en/docs/claude-code/llm-gateway

**Contents**:
- ​LiteLLM configuration
  - ​Prerequisites
  - ​Basic LiteLLM setup
    - ​Authentication methods
      - Static API key
      - Dynamic API key with helper
    - ​Unified endpoint (recommended)
    - ​Provider-specific pass-through endpoints (alternative)

**Examples**:

```text
# Set in environment
export ANTHROPIC_AUTH_TOKEN=sk-litellm-static-key

# Or in Claude Code settings
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "sk-litellm-static-key"
  }
}
```

```text
#!/bin/bash
# ~/bin/get-litellm-key.sh

# Example: Fetch key from vault
vault kv get -field=api_key secret/litellm/claude-code

# Example: Generate JWT token
jwt encode \
  --secret="${JWT_SECRET}" \
  --exp="+1h" \
  '{"user":"'${USER}'","team":"engineering"}'
```

```text
{
  "apiKeyHelper": "~/bin/get-litellm-key.sh"
}
```

---

## Legal and compliance

**URL**: https://docs.claude.com/en/docs/claude-code/legal-and-compliance

**Contents**:
- ​Legal agreements
  - ​License
  - ​Commercial agreements
- ​Compliance
  - ​Healthcare compliance (BAA)
- ​Security and trust
  - ​Trust and safety
  - ​Security vulnerability reporting

---

## MCP connector

**URL**: https://docs.claude.com/en/docs/agents-and-tools/mcp-connector

**Contents**:
- ​Key features
- ​Limitations
- ​Using the MCP connector in the Messages API
- ​MCP server configuration
  - ​Field descriptions
- ​Response content types
  - ​MCP Tool Use Block
  - ​MCP Tool Result Block

**Examples**:

```text
curl https://api.anthropic.com/v1/messages \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: mcp-client-2025-04-04" \
  -d '{
    "model": "claude-sonnet-4-5",
    "max_tokens": 1000,
    "messages": [{"role": "user", "content": "What tools do you have available?"}],
    "mcp_servers": [
      {
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse",
        "name": "ex
...
```

```text
{
  "type": "url",
  "url": "https://example-server.modelcontextprotocol.io/sse",
  "name": "example-mcp",
  "tool_configuration": {
    "enabled": true,
    "allowed_tools": ["example_tool_1", "example_tool_2"]
  },
  "authorization_token": "YOUR_TOKEN"
}
```

```text
{
  "type": "mcp_tool_use",
  "id": "mcptoolu_014Q35RayjACSWkSj4X2yov1",
  "name": "echo",
  "server_name": "example-mcp",
  "input": { "param1": "value1", "param2": "value2" }
}
```

---

## Manage Claude's memory - Claude Docs

**URL**: https://docs.claude.com/en/docs/claude-code/memory

---

## Manage Claude's memory

**URL**: https://docs.claude.com/en/docs/claude-code/memory

**Contents**:
- ​Determine memory type
- ​CLAUDE.md imports
- ​How Claude looks up memories
- ​Quickly add memories with the # shortcut
- ​Directly edit memories with /memory
- ​Set up project memory
- ​Organization-level memory management
- ​Memory best practices

**Examples**:

```text
See @README for project overview and @package.json for available npm commands for this project.

# Additional Instructions
- git workflow @docs/git-instructions.md
```

```text
# Individual Preferences
- @~/.claude/my-project-instructions.md
```

```text
This code span will not be treated as an import: `@anthropic-ai/claude-code`
```

---

## Manage costs effectively

**URL**: https://docs.claude.com/en/docs/claude-code/costs

**Contents**:
- ​Track your costs
  - ​Using the /cost command
  - ​Additional tracking options
- ​Managing costs for teams
  - ​Rate limit recommendations
- ​Reduce token usage
- ​Background token usage
- ​Tracking version changes and updates

**Examples**:

```text
Total cost:            $0.55
Total duration (API):  6m 19.7s
Total duration (wall): 6h 33m 10.2s
Total code changes:    0 lines added, 0 lines removed
```

```text
# Summary instructions

When you are using compact, please focus on test output and code changes
```

```text
claude doctor
```

---

## Migrate to Claude Agent SDK

**URL**: https://docs.claude.com/en/docs/claude-code/sdk/migration-guide

**Contents**:
- ​Overview
- ​What’s Changed
- ​Migration Steps
  - ​For TypeScript/JavaScript Projects
  - ​For Python Projects
- ​Breaking changes
  - ​Python: ClaudeCodeOptions renamed to ClaudeAgentOptions
  - ​System prompt no longer default

**Examples**:

```text
npm uninstall @anthropic-ai/claude-code
```

```text
npm install @anthropic-ai/claude-agent-sdk
```

```python
// Before
import { query, tool, createSdkMcpServer } from "@anthropic-ai/claude-code";

// After
import {
  query,
  tool,
  createSdkMcpServer,
} from "@anthropic-ai/claude-agent-sdk";
```

---

## Model Context Protocol (MCP)

**URL**: https://docs.claude.com/en/docs/mcp

**Contents**:
- ​Build your own MCP products
- MCP Documentation
- ​MCP in Anthropic products
- MCP in the Messages API
- MCP in Claude Code
- MCP in Claude.ai
- MCP in Claude Desktop

---

## Model configuration

**URL**: https://docs.claude.com/en/docs/claude-code/model-config

**Contents**:
- ​Available models
  - ​Model aliases
  - ​Setting your model
- ​Special model behavior
  - ​default model setting
  - ​opusplan model setting
  - ​Extended context with [1m]
- ​Checking your current model

**Examples**:

```text
# Start with Opus
claude --model opus

# Switch to Sonnet during session
/model sonnet
```

```text
{
    "permissions": {
        ...
    },
    "model": "opus"
}
```

```text
# Example of using a full model name with the [1m] suffix
/model anthropic.claude-sonnet-4-5-20250929-v1:0[1m]
```

---

## Model configuration - Claude Docs

**URL**: https://docs.claude.com/en/docs/claude-code/model-config

---

## Monitoring

**URL**: https://docs.claude.com/en/docs/claude-code/monitoring-usage

**Contents**:
- ​Quick Start
- ​Administrator Configuration
- ​Configuration Details
  - ​Common Configuration Variables
  - ​Metrics Cardinality Control
  - ​Dynamic Headers
    - ​Settings Configuration
    - ​Script Requirements

**Examples**:

```text
# 1. Enable telemetry
export CLAUDE_CODE_ENABLE_TELEMETRY=1

# 2. Choose exporters (both are optional - configure only what you need)
export OTEL_METRICS_EXPORTER=otlp       # Options: otlp, prometheus, console
export OTEL_LOGS_EXPORTER=otlp          # Options: otlp, console

# 3. Configure OTLP endpoint (for OTLP exporter)
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317

# 4. Set authentication (if required)
export OTEL_EXPORTER_OTLP_HEADERS="Aut
...
```

```text
{
  "env": {
    "CLAUDE_CODE_ENABLE_TELEMETRY": "1",
    "OTEL_METRICS_EXPORTER": "otlp",
    "OTEL_LOGS_EXPORTER": "otlp",
    "OTEL_EXPORTER_OTLP_PROTOCOL": "grpc",
    "OTEL_EXPORTER_OTLP_ENDPOINT": "http://collector.company.com:4317",
    "OTEL_EXPORTER_OTLP_HEADERS": "Authorization=Bearer company-token"
  }
}
```

```text
{
  "otelHeadersHelper": "/bin/generate_opentelemetry_headers.sh"
}
```

---

## Optimize your terminal setup

**URL**: https://docs.claude.com/en/docs/claude-code/terminal-config

**Contents**:
  - ​Themes and appearance
  - ​Line breaks
    - ​Set up Shift+Enter (VS Code or iTerm2):
    - ​Set up Option+Enter (VS Code, iTerm2 or macOS Terminal.app):
  - ​Notification setup
    - ​iTerm 2 system notifications
    - ​Custom notification hooks
  - ​Handling large inputs

---

## Output styles

**URL**: https://docs.claude.com/en/docs/claude-code/output-styles

**Contents**:
- ​Built-in output styles
- ​How output styles work
- ​Change your output style
- ​Create a custom output style
- ​Comparisons to related features
  - ​Output Styles vs. CLAUDE.md vs. —append-system-prompt
  - ​Output Styles vs. Agents
  - ​Output Styles vs. Custom Slash Commands

**Examples**:

```text
---
name: My Custom Style
description:
  A brief description of what this style does, to be displayed to the user
---

# Custom Style Instructions

You are an interactive CLI tool that helps users with software engineering
tasks. [Your custom instructions here...]

## Specific Behaviors

[Define how the assistant should behave in this style...]
```

---

## Plugin marketplaces - Claude Docs

**URL**: https://docs.claude.com/en/docs/claude-code/plugin-marketplaces

---

## Plugin marketplaces

**URL**: https://docs.claude.com/en/docs/claude-code/plugin-marketplaces

**Contents**:
- ​Overview
  - ​Prerequisites
- ​Add and use marketplaces
  - ​Add GitHub marketplaces
  - ​Add Git repositories
  - ​Add local marketplaces for development
  - ​Install plugins from marketplaces
  - ​Verify marketplace installation

**Examples**:

```text
/plugin marketplace add owner/repo
```

```text
/plugin marketplace add https://gitlab.com/company/plugins.git
```

```text
/plugin marketplace add ./my-marketplace
```

---

## Plugins

**URL**: https://docs.claude.com/en/docs/claude-code/plugins

**Contents**:
- ​Quickstart
  - ​Prerequisites
  - ​Create your first plugin
  - ​Plugin structure overview
- ​Install and manage plugins
  - ​Prerequisites
  - ​Add marketplaces
  - ​Install plugins

Create the marketplace structure

Create the plugin directory

Create the plugin manifest

Create the marketplace manifest

Install and test your plugin

Set up your development structure

Create the marketplace manifest

Iterate on your plugin

**Examples**:

```text
mkdir test-marketplace
cd test-marketplace
```

```text
mkdir my-first-plugin
cd my-first-plugin
```

```text
mkdir .claude-plugin
cat > .claude-plugin/plugin.json << 'EOF'
{
"name": "my-first-plugin",
"description": "A simple greeting plugin to learn the basics",
"version": "1.0.0",
"author": {
"name": "Your Name"
}
}
EOF
```

---

## Plugins reference

**URL**: https://docs.claude.com/en/docs/claude-code/plugins-reference

**Contents**:
- ​Plugin components reference
  - ​Commands
  - ​Agents
  - ​Skills
  - ​Hooks
  - ​MCP servers
- ​Plugin manifest schema
  - ​Complete schema

**Examples**:

```text
---
description: What this agent specializes in
capabilities: ["task1", "task2", "task3"]
---

# Agent Name

Detailed description of the agent's role, expertise, and when Claude should invoke it.

## Capabilities
- Specific task the agent excels at
- Another specialized capability
- When to use this agent vs others

## Context and examples
Provide examples of when this agent should be used and what kinds of problems it solves.
```

```text
skills/
├── pdf-processor/
│   ├── SKILL.md
│   ├── reference.md (optional)
│   └── scripts/ (optional)
└── code-reviewer/
    └── SKILL.md
```

```text
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/format-code.sh"
          }
        ]
      }
    ]
  }
}
```

---

## Remote MCP servers

**URL**: https://docs.claude.com/en/docs/agents-and-tools/remote-mcp-servers

**Contents**:
- ​Connecting to remote MCP servers
- ​Remote MCP server examples
  - Development & Testing Tools
  - Project Management & Documentation
  - Databases & Data Management
  - Payments & Commerce
  - Design & Media
  - Infrastructure & DevOps

---

## Sandboxing

**URL**: https://docs.claude.com/en/docs/claude-code/sandboxing

**Contents**:
- ​Overview
- ​Why sandboxing matters
- ​How it works
  - ​Filesystem isolation
  - ​Network isolation
  - ​OS-level enforcement
- ​Getting started
  - ​Enable sandboxing

**Examples**:

```text
{
  "sandbox": {
    "httpProxyPort": 8080,
    "socksProxyPort": 8081,
  }
}
```

```text
npx @anthropic-ai/sandbox-runtime <command-to-sandbox>
```

---

## Security

**URL**: https://docs.claude.com/en/docs/claude-code/security

**Contents**:
- ​How we approach security
  - ​Security foundation
  - ​Permission-based architecture
  - ​Built-in protections
  - ​User responsibility
- ​Protect against prompt injection
  - ​Core protections
  - ​Privacy safeguards

---

## Security - Claude Docs

**URL**: https://docs.claude.com/en/docs/claude-code/security

---

## Set up Claude Code

**URL**: https://docs.claude.com/en/docs/claude-code/setup

**Contents**:
- ​System requirements
  - ​Additional dependencies
- ​Standard installation
- ​Windows setup
- ​Alternative installation methods
  - ​Global npm installation
  - ​Native binary installation (Beta)
  - ​Local installation

**Examples**:

```text
npm install -g @anthropic-ai/claude-code
```

```text
cd your-awesome-project
claude
```

```text
$env:CLAUDE_CODE_GIT_BASH_PATH="C:\Program Files\Git\bin\bash.exe"
```

---

## Slash commands

**URL**: https://docs.claude.com/en/docs/claude-code/slash-commands

**Contents**:
- ​Built-in slash commands
- ​Custom slash commands
  - ​Syntax
    - ​Parameters
  - ​Command types
    - ​Project commands
    - ​Personal commands
  - ​Features

**Examples**:

```text
/<command-name> [arguments]
```

```text
# Create a project command
mkdir -p .claude/commands
echo "Analyze this code for performance issues and suggest optimizations:" > .claude/commands/optimize.md
```

```text
# Create a personal command
mkdir -p ~/.claude/commands
echo "Review this code for security vulnerabilities:" > ~/.claude/commands/security-review.md
```

---

## Status line configuration

**URL**: https://docs.claude.com/en/docs/claude-code/statusline

**Contents**:
- ​Create a custom status line
- ​How it Works
- ​JSON Input Structure
- ​Example Scripts
  - ​Simple Status Line
  - ​Git-Aware Status Line
  - ​Python Example
  - ​Node.js Example

**Examples**:

```javascript
{
  "statusLine": {
    "type": "command",
    "command": "~/.claude/statusline.sh",
    "padding": 0 // Optional: set to 0 to let status line go to edge
  }
}
```

```text
{
  "hook_event_name": "Status",
  "session_id": "abc123...",
  "transcript_path": "/path/to/transcript.json",
  "cwd": "/current/working/directory",
  "model": {
    "id": "claude-opus-4-1",
    "display_name": "Opus"
  },
  "workspace": {
    "current_dir": "/current/working/directory",
    "project_dir": "/original/project/directory"
  },
  "version": "1.0.80",
  "output_style": {
    "name": "default"
  },
  "cost": {
    "total_cost_usd": 0.01234,
    "total_duration_ms": 45000,
    "total_
...
```

```text
#!/bin/bash
# Read JSON input from stdin
input=$(cat)

# Extract values using jq
MODEL_DISPLAY=$(echo "$input" | jq -r '.model.display_name')
CURRENT_DIR=$(echo "$input" | jq -r '.workspace.current_dir')

echo "[$MODEL_DISPLAY] 📁 ${CURRENT_DIR##*/}"
```

---

## Subagents

**URL**: https://docs.claude.com/en/docs/claude-code/sub-agents

**Contents**:
- ​What are subagents?
- ​Key benefits
- Context preservation
- Specialized expertise
- Reusability
- Flexible permissions
- ​Quick start
- ​Subagent configuration

Open the subagents interface

Select 'Create New Agent'

**Examples**:

```text
> Use the code-reviewer subagent to check my recent changes
```

```text
claude --agents '{
  "code-reviewer": {
    "description": "Expert code reviewer. Use proactively after code changes.",
    "prompt": "You are a senior code reviewer. Focus on code quality, security, and best practices.",
    "tools": ["Read", "Grep", "Glob", "Bash"],
    "model": "sonnet"
  }
}'
```

```text
---
name: your-sub-agent-name
description: Description of when this subagent should be invoked
tools: tool1, tool2, tool3  # Optional - inherits all tools if omitted
model: sonnet  # Optional - specify model alias or 'inherit'
---

Your subagent's system prompt goes here. This can be multiple paragraphs
and should clearly define the subagent's role, capabilities, and approach
to solving problems.

Include specific instructions, best practices, and any constraints
the subagent should follow.
```

---

## Troubleshooting

**URL**: https://docs.claude.com/en/docs/claude-code/troubleshooting

**Contents**:
- ​Common installation issues
  - ​Windows installation issues: errors in WSL
  - ​Linux and Mac installation issues: permission or command not found errors
    - ​Recommended solution: Native Claude Code installation
    - ​Alternative solution: Migrate to local installation
- ​Permissions and authentication
  - ​Repeated permission prompts
  - ​Authentication issues

**Examples**:

```text
# Load nvm if it exists
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
```

```text
source ~/.nvm/nvm.sh
```

```text
export PATH="$HOME/.nvm/versions/node/$(node -v)/bin:$PATH"
```

---

## Visual Studio Code

**URL**: https://docs.claude.com/en/docs/claude-code/vs-code

**Contents**:
- ​VS Code Extension (Beta)
  - ​Features
  - ​Requirements
  - ​Installation
  - ​Updating
  - ​How It Works
  - ​Using Third-Party Providers (Vertex and Bedrock)
    - ​Environment Variables

---
