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

1. **Skill Definitions** (`.github/copilot-skills/{skill-name}/`)
   - `SKILL.md` - Core documentation with YAML metadata
   - Detail files (`patterns.md`, `reference.md`) - Progressive disclosure layers
   - `scripts/` - Bundled tools for deterministic operations

2. **Skill Prompts** (`.github/prompts/{skill-name}.skill.prompt.md`)
   - Defines WHEN a skill is relevant (use cases)
   - Defines HOW to use it step-by-step (workflow)
   - Enables `/skill-{name}` slash commands in Copilot

3. **Management System** (`.github/copilot-skills/`)
   - `index.md` - Registry of all available skills
   - `README.md` - System architecture overview
   - `scripts/` - Tools for creating, validating, analyzing skills
   - `templates/` - Scaffolding for new skills

## Five Constitutional Principles

**All skills must follow these principles** (see `.specify/memory/constitution.md`):

1. **Progressive Disclosure** - Metadata → core → details. Each layer independent, scannable in <3 min
2. **File-Based Organization** - Skills are directories with SKILL.md + YAML frontmatter + bundled scripts
3. **Dynamic Discovery** - `.github/copilot-skills/index.md` enables AI to find skills automatically
4. **Deterministic Execution** - Scripts in `scripts/` produce consistent terminal output (no file generation)
5. **Composability** - Skills reference each other with explicit dependencies, clear boundaries

## Available Skills

Check `.github/copilot-skills/index.md` for the complete registry of available skills.

## Working with Skills

### Discover Skills
```
1. Check .github/copilot-skills/index.md
2. Find relevant skill
3. Read skill SKILL.md (~3 min)
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

See `.github/copilot-skills/index.md` to find which scripts each skill provides.

### Create New Skill
```bash
# 1. Create directory
mkdir -p .github/copilot-skills/{skill-name}/scripts

# 2. Copy template
cp .github/copilot-skills/templates/SKILL.template.md \
   .github/copilot-skills/{skill-name}/SKILL.md

# 3. Create skill prompt
cp .github/copilot-skills/templates/skill-prompt.template.md \
   .github/prompts/{skill-name}.skill.prompt.md

# 4. Add bundled scripts (terminal output only)

# 5. Register in index
# Add entry to .github/copilot-skills/index.md

# 6. Validate compliance
# Ensure follows 5 constitutional principles
```

## Project Structure

```
.github/
├── copilot-instructions.md              # This file
├── copilot-skills/                      # Skills system
│   ├── index.md                         # Skills registry
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
└── .specify/
    └── memory/
        └── constitution.md              # Canonical principles

.gitignore                               # Respects .gitignore patterns
examples/                                # Third-party skill collections
readme.md                                # Project overview (UPDATE THIS)
copilot-skills.md                        # Technical deep-dive
```

## Key Files to Understand

- **.github/copilot-instructions.md** - This file - Main guidance for AI agents
- **.github/copilot-skills/index.md** - Skills discovery registry
- **.github/copilot-skills/README.md** - Complete architecture explanation
- **.specify/memory/constitution.md** - Canonical 5 principles
- **readme.md** - High-level project overview
- **copilot-skills.md** - Technical architecture details

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
index.md (1 line)
→ .skill.prompt.md (workflow)
→ SKILL.md (core, ~100 lines)
→ patterns.md, reference.md (details)
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

- **Architecture**: `copilot-skills.md`
- **Overview**: `readme.md`
- **Skills Registry**: `.github/copilot-skills/index.md`
- **Principles**: `.specify/memory/constitution.md`
- **Examples**: `examples/` directory

