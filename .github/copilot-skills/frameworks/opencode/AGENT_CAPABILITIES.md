# OpenCode Agent Capabilities Analysis

## Question
Do OpenCode agents have the ability to:
1. Work on files in the same directory as the main agent?
2. Run tools and MCP Servers?

---

## Answer: ✅ YES - Fully Supported

OpenCode agents have **complete access** to the working directory, all configured tools, and can invoke MCP Servers. This is a core architectural feature.

---

## File Access Capabilities

### ✅ Yes - Agents Can Work on Project Files

**How it works:**
- All agents (primary and subagents) operate within the **same working directory**
- Agents inherit the project context and file system access from the parent session
- Both primary agents (@build, @plan) and custom subagents can read and modify files

**Built-in File Tools Available to All Agents:**

| Tool | Purpose | Control |
|------|---------|---------|
| **read** | Read file contents (supports line ranges) | Can be disabled per agent |
| **write** | Create new files or overwrite existing | Can be disabled per agent |
| **edit** | Modify files with exact string replacements | Can be disabled per agent |
| **search** | Search file contents with regex | Can be disabled per agent |
| **find** | Search for files by glob patterns | Can be disabled per agent |
| **list** | List files and directories | Can be disabled per agent |

### File Access Control Per Agent

You can restrict file access **per agent** using the tools configuration:

```json
{
  "agent": {
    "code-reviewer": {
      "mode": "subagent",
      "tools": {
        "write": false,
        "edit": false,
        "bash": false
      }
    },
    "documentation-writer": {
      "mode": "subagent",
      "tools": {
        "write": true,
        "edit": true,
        "bash": false
      }
    }
  }
}
```

**Example: Our Generated Agents**

Our `generate-agent.sh` script intelligently sets these:

```
Code Reviewer (read-only):
  write: false, edit: false, bash: false

Test Writer (can create tests):
  write: true, edit: false, bash: true

Docs Generator (can write docs):
  write: true, edit: true, bash: false

Debug Helper (can run bash):
  write: false, edit: false, bash: true
```

---

## Tool Capabilities

### ✅ Yes - Agents Can Run Tools

**OpenCode Provides Built-in Tools:**

1. **bash** - Execute shell commands
   ```bash
   ! npm test
   ! git status
   ! python script.py
   ```

2. **edit** - Modify existing files with precise replacements
   ```
   Agents can target specific lines and replace exact text
   ```

3. **write** - Create new files
   ```
   Agents can generate new files in the project
   ```

4. **read** - Read files and specific line ranges
   ```
   Agents analyze code before making changes
   ```

5. **search** - Fast regex-based search
   ```
   Agents can find patterns across codebase
   ```

6. **find** - File discovery by glob patterns
   ```
   Agents can locate files matching criteria
   ```

### Tool Access Configuration

**Global Configuration:**
```json
{
  "tools": {
    "write": true,
    "edit": true,
    "bash": true,
    "search": true,
    "find": true,
    "list": true
  }
}
```

**Per-Agent Overrides:**
```json
{
  "agent": {
    "plan": {
      "tools": {
        "write": false,
        "edit": false,
        "bash": false
      }
    }
  }
}
```

---

## MCP Server Integration

### ✅ Yes - Agents Can Use MCP Servers

**What is MCP?**
- Model Context Protocol servers
- Custom tools and integrations
- Extend OpenCode with domain-specific capabilities

**How Agents Access MCP Tools:**

MCP servers expose tools that agents can call:

```json
{
  "agent": {
    "database-expert": {
      "mode": "subagent",
      "tools": {
        "database_query": true,
        "database_migrate": false,
        "custom_analysis": true
      }
    }
  }
}
```

**MCP Wildcard Control:**
```json
{
  "tools": {
    "database_*": true,      // Enable all database tools
    "custom_*": false         // Disable custom namespace
  }
}
```

**Benefits:**
- Agents can access specialized tools via MCP
- Tools are contextual to agent purpose
- Fine-grained permission control
- Multiple MCP servers can coexist

---

## Agent-to-Agent Collaboration

### Primary Agents → Subagents

Primary agents can **delegate to subagents** and they share context:

```
@build (primary) 
  ↓ delegates to
@test-writer (subagent) 
  ↓ can access all files in working directory
  ↓ can run configured tools
  ↓ returns results to @build
```

### Workflow Example

```
User: @build implement auth feature

@build agent:
  1. Reads existing auth code
  2. Creates plan
  3. Delegates to @test-writer for tests
  4. Delegates to @code-reviewer for review
  5. Executes implementation
  6. All agents share the same working directory
```

---

## Real-World Capabilities

### What Our Generated Agents Can Do

**Agent: code-reviewer**
```
✓ Read files (analyze code)
✓ Search patterns (find issues)
✗ Cannot write files
✗ Cannot run bash
→ Safe analysis-only agent
```

**Agent: test-writer**
```
✓ Read files (understand code)
✓ Write files (create tests)
✓ Run bash (execute tests, npm commands)
✗ Cannot edit existing files
→ Can generate new test files and run them
```

**Agent: docs-generator**
```
✓ Read files
✓ Write files
✓ Edit files
✗ Cannot run bash
→ Can create/modify documentation
```

---

## Tool Execution Context

### Session Context
Each agent receives:
- Current working directory
- Project file structure
- Git history (if available)
- Environment variables
- Session history

### File References
In the TUI, you can reference files:
```
@plan analyze the auth in @src/auth.ts

This automatically includes the file content in the conversation
```

### Bash Command Results
Results are included in agent context:
```
! git log --oneline

The output is added to conversation as a tool result
```

---

## Safety & Permissions Model

### Conservative by Default

**@plan agent (restricted):**
```json
{
  "tools": {
    "write": false,
    "edit": false,
    "bash": false
  }
}
```
→ Can analyze code without making changes

**@build agent (full access):**
```json
{
  "tools": {
    "write": true,
    "edit": true,
    "bash": true
  }
}
```
→ Can implement features, run tests, execute commands

### Per-Agent Customization

Our `generate-agent.sh` intelligently assigns permissions:

```
Purpose contains "review" → read-only
Purpose contains "test" → write + bash
Purpose contains "doc" → write + edit
Purpose contains "debug" → bash only
```

---

## Summary: Yes, Agents Have Full Capabilities

| Capability | Support | Notes |
|------------|---------|-------|
| Access working directory files | ✅ Full | Same directory as parent agent |
| Read files | ✅ Full | All agents by default |
| Write/Create files | ✅ Configurable | Per-agent control |
| Edit existing files | ✅ Configurable | Per-agent control |
| Execute bash commands | ✅ Configurable | Per-agent control |
| Search files | ✅ Full | Regex and glob patterns |
| Find files | ✅ Full | Pattern matching |
| Use custom tools | ✅ Full | Via MCP servers |
| Use MCP Servers | ✅ Full | Custom integrations |
| Delegate to subagents | ✅ Full | Share context |
| Fine-grained permissions | ✅ Full | Per agent + global |

---

## Conclusion

✅ **OpenCode agents are fully capable of:**
1. Working on files in your project directory
2. Running tools and commands
3. Integrating with MCP servers
4. Collaborating with other agents
5. Operating with fine-grained permission controls

This makes them ideal for creating **specialized workflows** where different agents handle different aspects of development while maintaining security through permission controls.

