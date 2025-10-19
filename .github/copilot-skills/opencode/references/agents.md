# Opencode - Agents

**Pages**: 1

---

## Agents | opencode

**URL**: https://opencode.ai/docs/agents

**Contents**:
- Agents
- Types
  - Primary agents
  - Subagents
- Built-in
  - Build
  - Plan
  - General

Configure and use specialized agents.

Agents are specialized AI assistants that can be configured for specific tasks and workflows. They allow you to create focused tools with custom prompts, models, and tool access.

Use the plan agent to analyze code and review suggestions without making any code changes.

You can switch between agents during a session or invoke them with the @ mention.

There are two types of agents in OpenCode; primary agents and subagents.

Primary agents are the main assistants you interact with directly. You can cycle through them using the Tab key, or your configured switch_agent keybind. These agents handle your main conversation and can access all configured tools.

You can use the Tab key to switch between primary agents during a session.

OpenCode comes with two built-in primary agents, Build and Plan. We’ll look at these below.

Subagents are specialized assistants that primary agents can invoke for specific tasks. You can also manually invoke them by @ mentioning them in your messages.

OpenCode comes with one built-in subagent, General. We’ll look at this below.

OpenCode comes with two built-in primary agents and one built-in subagent.

Build is the default primary agent with all tools enabled. This is the standard agent for development work where you need full access to file operations and system commands.

A restricted agent designed for planning and analysis. We use a permission system to give you more control and prevent unintended changes. By default, all of the following are set to ask:

This agent is useful when you want the LLM to analyze code, suggest changes, or create plans without making any actual modifications to your codebase.

A general-purpose agent for researching complex questions, searching for code, and executing multi-step tasks. Use when searching for keywords or files and you’re not confident you’ll find the right match in the first few tries.

For primary agents, use the Tab key to cycle through them during 

*[Content truncated - see full docs]*

**Examples**:

```javascript
@general help me search for this function
```

```text
{  "$schema": "https://opencode.ai/config.json",  "agent": {    "build": {      "mode": "primary",      "model": "anthropic/claude-sonnet-4-20250514",      "prompt": "{file:./prompts/build.txt}",      "tools": {        "write": true,        "edit": true,        "bash": true      }    },    "plan": {      "mode": "primary",      "model": "anthropic/claude-haiku-4-20250514",      "tools": {        "write": false,        "edit": false,        "bash": false      }    },    "code-reviewer": {      "d
...
```

```text
---description: Reviews code for quality and best practicesmode: subagentmodel: anthropic/claude-sonnet-4-20250514temperature: 0.1tools:  write: false  edit: false  bash: false---
You are in code review mode. Focus on:
- Code quality and best practices- Potential bugs and edge cases- Performance implications- Security considerations
Provide constructive feedback without making direct changes.
```

---
