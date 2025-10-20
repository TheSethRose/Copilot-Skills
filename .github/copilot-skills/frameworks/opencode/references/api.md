# Opencode - Api

**Pages**: 1

---

## TUI | opencode

**URL**: https://opencode.ai/docs/tui

**Contents**:
- TUI
- File references
- Bash commands
- Commands
  - compact
  - details
  - editor
  - exit

Using the OpenCode terminal user interface.

OpenCode provides an interactive terminal interface or TUI for working on your projects with an LLM.

Running OpenCode starts the TUI for the current directory.

Or you can start it for a specific working directory.

Once you’re in the TUI, you can prompt it with a message.

You can reference files in your messages using @. This does a fuzzy file search in the current working directory.

You can also use @ to reference files in your messages.

The content of the file is added to the conversation automatically.

Start a message with ! to run a shell command.

The output of the command is added to the conversation as a tool result.

When using the OpenCode TUI, you can type / followed by a command name to quickly execute actions. For example:

Most commands also have keybind using ctrl+x as the leader key, where ctrl+x is the default leader key. Learn more.

Here are all available slash commands:

Compact the current session. Alias: /summarize

Toggle tool execution details.

Open external editor for composing messages. Uses the editor set in your EDITOR environment variable. Learn more.

Exit OpenCode. Aliases: /quit, /q

Export current conversation to Markdown and open in your default editor. Uses the editor set in your EDITOR environment variable. Learn more.

Show the help dialog.

Create or update AGENTS.md file. Learn more.

List available models.

Start a new session. Alias: /clear

Redo a previously undone message. Only available after using /undo.

Any file changes will also be restored.

Internally, this uses Git to manage the file changes. So your project needs to be a Git repository.

List and switch between sessions. Aliases: /resume, /continue

Share current session. Learn more.

List available themes.

Undo last message in the conversation. Removes the most recent user message, all subsequent responses, and any file changes.

Any file changes made will also be reverted.

Internally, this uses Git to manage th

*[Content truncated - see full docs]*

**Examples**:

```text
opencode /path/to/project
```

```text
Give me a quick summary of the codebase.
```

```javascript
How is auth handled in @packages/functions/src/api/index.ts?
```

---
