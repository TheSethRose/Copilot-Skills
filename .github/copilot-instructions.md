# Copilot Instructions

This repository demonstrates a **Copilot Skills Architecture system** — a framework for organizing domain knowledge into discoverable, composable skills that keep AI agents focused and context-efficient.

This is NOT a traditional application to build/run. It's a **meta-system** for creating and managing reusable skills.

## What This Repository Is

A complete implementation of the Copilot Skills Architecture featuring:

- **Skill Files** - Self-contained documentation + bundled scripts (`.github/copilot-skills/`)
- **Skill Prompts** - AI-executable workflows (`.github/prompts/`)
- **Constitutional Framework** - 5 architectural principles all skills follow
- **Reference Implementations** - Example skills from Anthropic, Obra, and the community
- **Automation Tools** - Scripts for creating, validating, and managing skills

## Core Architecture

### Three-Part System

1. **Skill Prompts** (`.github/prompts/{skill-name}.skill.prompt.md`)
   - Defines WHEN a skill is relevant (use cases)
   - Defines HOW to use it step-by-step (workflow)
   - Enables `/skill-{name}` slash commands in Copilot

2. **Instructions Files** (`.github/instructions/{skill-name}.instructions.md`)
   - Auto-loaded context for file patterns or keywords
   - Default behaviors and quality guidelines
   - Common workflows and examples

3. **Skill Directories** (`.github/copilot-skills/{skill-name}/`)
   - Optional: Detail files (`patterns.md`, `reference.md`) for progressive disclosure
   - Optional: `scripts/` - Bundled tools for deterministic operations
   - `README.md` for reference implementations

4. **Management System** (`.github/copilot-skills/`)
   - `README.md` - System architecture overview
   - `scripts/` - Tools for creating, validating, analyzing skills
   - `templates/` - Scaffolding for new skills

## Five Constitutional Principles

**All skills must follow these principles** (see `.specify/memory/constitution.md`):

1. **Progressive Disclosure** - Metadata → core → details. Each layer independent, scannable in <3 min
2. **File-Based Organization** - Skills are prompt + instructions + bundled scripts
3. **Dynamic Discovery** - Keyword routing map enables AI to find skills automatically
4. **Deterministic Execution** - Scripts in `scripts/` produce consistent terminal output (no file generation)
5. **Composability** - Skills reference each other with explicit dependencies, clear boundaries

## Available Skills

Check the **Keyword Routing Map** below for the complete registry of available skills.

## 🧠 Context-Aware Routing System

This repository implements a **Claude-style skills framework** with automatic context loading and skill suggestion.

### Architecture Layers

| Layer | Purpose | Load Behavior | Analogy |
|-------|---------|---------------|---------|
| **`.github/instructions/`** | Auto-triggered context rules | Automatic when file patterns or keywords match | Claude's "background skills" |
| **`.github/prompts/`** | Callable skill modules | Manual via `/skill-name` or contextual suggestion | Claude's "explicit skills" |
| **`.github/chatmodes/`** | Persona definitions | Manual via `/switch mode` | Tone/role switching |
| **`copilot-instructions.md`** | Global routing + repo policy | Always active | Top-level agent brain |
| **`.github/copilot-skills/`** | Internal tooling layer | Reference for maintainers | Developer toolkit |

### Keyword Routing Map

When user queries contain these keywords, **suggest the corresponding skill**:

#### PDF & Document Operations
**Keywords:** PDF, pdf, report, export, document, form, fillable, extract text, merge pdf, split pdf, watermark, table extraction
**Suggest:** `/pdf-handling`
**Auto-context:** `.github/instructions/pdf-handling.instructions.md` (when editing PDF-related files)
**Skill:** `.github/copilot-skills/pdf-handling/SKILL.md`

#### Git & Version Control
**Keywords:** git, commit, merge, rebase, push, pull, branch, checkout, stash, conflict, github, pull request, PR, force push
**Suggest:** `/git-ops`
**Auto-context:** `.github/instructions/git-ops.instructions.md` (when editing .git/, .gitignore, .github/)
**Skill:** `.github/copilot-skills/git-ops/SKILL.md`

#### Project Creation & Scaffolding
**Keywords:** create, new project, initialize, setup, scaffold, boilerplate, template, starter
**Suggest:** `/create`
**Auto-context:** `.github/instructions/create.instructions.md` (when editing package.json, requirements.txt, etc.)
**Skill:** `.github/copilot-skills/skill-template/SKILL.md`

#### Cleanup & Maintenance
**Keywords:** cleanup, remove, delete, unused, stale, orphan, tidy
**Suggest:** `/cleanup`
**Skill:** `.github/prompts/cleanup.skill.prompt.md`

#### Copilot Instructions Generation
**Keywords:** analyze codebase, generate instructions, copilot-instructions, discover patterns
**Suggest:** `/generate-copilot-instructions`
**Skill:** `.github/copilot-skills/copilot-instructions-generator/SKILL.md`

#### Brand Guidelines & Visual Identity
**Keywords:** branding, brand colors, typography, visual identity, styling, brand guidelines, corporate design, Anthropic brand
**Suggest:** `/brand-guidelines`
**Auto-context:** `.github/instructions/brand-guidelines.instructions.md` (when editing brand/style/design files)
**Skill:** `.github/copilot-skills/brand-guidelines/README.md`

#### Document Operations (Multi-Format)
**Keywords:** document, docx, pptx, xlsx, word, powerpoint, excel, spreadsheet, document processing
**Suggest:** `/document-skills`
**Auto-context:** `.github/instructions/document-skills.instructions.md` (when editing document files)
**Skill:** `.github/copilot-skills/document-skills/README.md`
**Note:** PDF operations use specialized `/pdf-handling` sub-skill

#### MCP Server Development
**Keywords:** mcp, model context protocol, mcp server, agent tools, llm integration, api integration, fastmcp, tool design
**Suggest:** `/mcp-builder`
**Auto-context:** `.github/instructions/mcp-builder.instructions.md` (when editing MCP-related files)
**Skill:** `.github/copilot-skills/mcp-builder/README.md`

### Escalation Hierarchy

When responding to user queries, follow this decision tree:

1. **Check for matching keywords** → Suggest relevant skill prompt
2. **Check file context** → Load corresponding `.instructions.md` if available
3. **Prefer specialized prompts** before generic code generation
4. **If ambiguous** → Ask user to clarify or list matching skills
5. **If no skill matches** → Use general coding knowledge with repo conventions

### Response Priority

```
1. Skill prompt (explicit, callable) > Generic response
2. Instruction context (auto-loaded) > No context
3. Specialized domain knowledge > General knowledge
4. Bundled scripts > Ad-hoc code generation
```

### Chat Mode Support

Users can switch personas for different interaction styles:

- **`/switch dev`** → Dev Mode: terse, code-first responses (`.github/chatmodes/dev.chatmode.md`)
- **`/switch doc`** → Doc Mode: detailed, educational responses (`.github/chatmodes/doc.chatmode.md`)
- **`/switch default`** → Default Mode: balanced explanations

## Working with Skills

### Discover Skills
```
1. Check keyword routing map in this file
2. Use `/skill-{name}` command to load skill
3. Read skill prompt for workflow
4. Load detail files (patterns.md, reference.md) as needed
5. Use bundled scripts or examples
```

### Run Bundled Scripts

Each skill has a `scripts/` directory with bundled tools:

```bash
# Example: Run a skill's bundled script
bash .github/copilot-skills/{skill-name}/scripts/{script}.sh [options]

# Scripts output to terminal only (no files generated)
# Output can be parsed by AI agents as a data source
```

Check the keyword routing map above or skill prompt files to find which scripts each skill provides.

### Create New Skill
```bash
# 1. Create directory
mkdir -p .github/copilot-skills/{skill-name}/scripts

# 2. Copy skill prompt template
cp .github/copilot-skills/templates/skill-prompt.template.md \
   .github/prompts/{skill-name}.skill.prompt.md

# 3. Copy instructions template
cp .github/copilot-skills/templates/instructions.template.md \
   .github/instructions/{skill-name}.instructions.md

# 4. Add bundled scripts (terminal output only)

# 5. Register in keyword routing map
# Add entry to keyword routing map in this file

# 6. Validate compliance
# Ensure follows 5 constitutional principles
```

## Project Structure

```
.github/
├── copilot-instructions.md              # This file
├── copilot-skills/                      # Skills system
│   ├── README.md                        # Architecture overview
│   ├── templates/                       # Scaffolding
│   ├── scripts/                         # Automation tools
│   ├── copilot-instructions-generator/  # Skill: generate instructions
│   ├── git-ops/                         # Skill: git operations
│   ├── pdf-handling/                    # Skill: PDF manipulation
│   └── skill-template/                  # Template for new skills
├── prompts/                             # Skill execution workflows
│   ├── generate-copilot-instructions.skill.prompt.md
│   ├── git-ops.skill.prompt.md
│   ├── pdf-handling.skill.prompt.md
│   └── [other skill prompts]
├── instructions/                        # Auto-loaded context rules
│   ├── generate-copilot-instructions.instructions.md
│   ├── git-ops.instructions.md
│   ├── pdf-handling.instructions.md
│   └── [other instruction files]
└── .specify/
    └── memory/
        └── constitution.md              # Canonical principles

.gitignore                               # Respects .gitignore patterns
examples/                                # Third-party skill collections
readme.md                                # Project overview
```

## Key Files to Understand

- **.github/copilot-instructions.md** - This file - Main guidance for AI agents
- **.github/copilot-skills/README.md** - Complete architecture explanation
- **.specify/memory/constitution.md** - Canonical 5 principles
- **readme.md** - High-level project overview

## Development Workflows

### Respecting .gitignore

Scripts automatically exclude per `.gitignore`:
- `.env`, `.env.*`, `*.log` (environment/secrets)
- `node_modules/`, `__pycache__/`, `.venv/` (dependencies)
- `.vscode/`, `.idea/` (IDE files)
- Build artifacts, example directories, temporary files

This prevents analyzing third-party code or sensitive files.

### Bundled Scripts

- Output to **terminal only** (no file generation)
- Self-contained and deterministic
- Respect `.gitignore` patterns
- Documented in SKILL.md with usage examples

## Code Patterns

### Skill YAML Metadata
```yaml
---
name: "Skill Name"
description: "One-sentence purpose"
version: "1.0.0"
tags: ["keyword1", "keyword2"]
dependencies: ["tool1", "tool2"]
---
```

### Progressive Disclosure
```
Keyword routing map (suggest skill)
→ .skill.prompt.md (workflow)
→ detail files (patterns.md, reference.md)
→ scripts/ (tools)
```

## This Is NOT

- ❌ A software application to build or run
- ❌ A typical repository with source code
- ❌ A framework or library to depend on
- ❌ A CI/CD system or deployment pipeline

## This IS

- ✅ A meta-system for creating reusable skills
- ✅ A framework for organizing domain knowledge
- ✅ A demonstration of progressive disclosure
- ✅ Portable skills for multiple AI agents

## Resources

- **Overview**: `readme.md`
- **Architecture**: `.github/copilot-skills/README.md`
- **Principles**: `.specify/memory/constitution.md`
- **Examples**: `examples/` directory

