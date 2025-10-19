# Opencode - Tools

**Pages**: 2

---

## Custom Tools | opencode

**URL**: https://opencode.ai/docs/custom-tools

**Contents**:
- Custom Tools
- Creating a tool
  - Location
  - Structure
  - Arguments
- Context
- Multiple tools per file

Create tools the LLM can call in opencode.

Custom tools are functions you create that the LLM can call during conversations. They work alongside opencode’s built-in tools like read, write, and bash.

Tools are defined as TypeScript or JavaScript files.

The easiest way to create tools is using the tool() helper which provides type-safety and validation.

The filename becomes the tool name. The above creates a database tool.

You can use tool.schema, which is just Zod, to define argument types.

You can also import Zod directly and return a plain object:

Tools receive context about the current session:

You can also export multiple tools from a single file. Each export becomes a separate tool with the name <filename>_<exportname>:

This creates two tools: math_add and math_multiply.

**Examples**:

```python
import { tool } from "@opencode-ai/plugin"
export default tool({  description: "Query the project database",  args: {    query: tool.schema.string().describe("SQL query to execute"),  },  async execute(args) {    // Your database logic here    return `Executed query: ${args.query}`  },})
```

```text
args: {  query: tool.schema.string().describe("SQL query to execute")}
```

```python
import { z } from "zod"
export default {  description: "Tool description",  args: {    param: z.string().describe("Parameter description"),  },  async execute(args, context) {    // Tool implementation    return "result"  },}
```

---

## Tools | opencode

**URL**: https://opencode.ai/docs/tools

**Contents**:
- Tools
- Configure
  - Global
  - Per agent
- Built-in
  - bash
  - edit
  - write

Manage the tools an LLM can use.

Tools allow the LLM to perform actions in your codebase. OpenCode comes with a set of built-in tools, but you can extend it with custom tools or MCP servers.

By default, all tools are enabled and don’t need permission to run. But you can configure this and control the permissions through your config.

You can configure tools globally or per agent. Agent-specific configs override global settings.

By default, all tools are set to true. To disable a tool, set it to false.

Disable or enable tools globally using the tools option.

You can also use wildcards to control multiple tools at once. For example, to disable all tools from an MCP server:

Override global tool settings for specific agents using the tools config in the agent definition.

For example, here the plan agent overrides the global config to disable write and bash tools.

You can also configure tools for agents in Markdown.

Learn more about configuring tools per agent.

Here are all the built-in tools available in OpenCode.

Execute shell commands in your project environment.

This tool allows the LLM to run terminal commands like npm install, git status, or any other shell command.

Modify existing files using exact string replacements.

This tool performs precise edits to files by replacing exact text matches. It’s the primary way the LLM modifies code.

Create new files or overwrite existing ones.

Use this to allow the LLM to create new files. It will overwrite existing files if they already exist.

Read file contents from your codebase.

This tool reads files and returns their contents. It supports reading specific line ranges for large files.

Search file contents using regular expressions.

Fast content search across your codebase. Supports full regex syntax and file pattern filtering.

Find files by pattern matching.

Search for files using glob patterns like **/*.js or src/**/*.ts. Returns matching file paths sorted by modification time.

List files and directo

*[Content truncated - see full docs]*

**Examples**:

```text
{  "$schema": "https://opencode.ai/config.json",  "tools": {    "write": false,    "bash": false,    "webfetch": true  }}
```

```text
{  "$schema": "https://opencode.ai/config.json",  "tools": {    "mymcp_*": false  }}
```

```text
{  "$schema": "https://opencode.ai/config.json",  "tools": {    "write": true,    "bash": true  },  "agent": {    "plan": {      "tools": {        "write": false,        "bash": false      }    }  }}
```

---
