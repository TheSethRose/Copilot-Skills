# Copilot Skills Architecture

## Overview

**Copilot Skills** is a complete system for organizing domain knowledge into discoverable, composable skills that keep AI agents focused and context-efficient.

Rather than monolithic instructions files, this architecture uses **progressive disclosure** — loading information in layers only when needed. AI agents discover relevant skills automatically, read core documentation in ~3 minutes, and load details on demand.

This repository demonstrates:
- ✅ **Skill System** - Self-contained knowledge modules with bundled scripts
- ✅ **Progressive Disclosure** - Metadata → Core → Details layers
- ✅ **Constitutional Framework** - 5 architectural principles all skills follow
- ✅ **Automation Tools** - Scripts for creating, validating, and managing skills
- ✅ **Reference Implementations** - Example skills from Anthropic, Obra, and community

**Status**: Complete working implementation with reference skills and production-ready templates.

---

## Quick Start

### Understand the System
```bash
# 1. Read the main architecture guide
cat .github/copilot-skills/README.md

# 2. Review the 5 canonical principles
cat .specify/memory/constitution.md

# 3. Check available skills
cat .github/copilot-skills/index.md
```

### Create a Skill

```bash
# 1. Create structure
mkdir -p .github/copilot-skills/{skill-name}/scripts

# 2. Use template
cp .github/copilot-skills/templates/SKILL.template.md \
   .github/copilot-skills/{skill-name}/SKILL.md

# 3. Create prompt
cp .github/copilot-skills/templates/skill-prompt.template.md \
   .github/prompts/{skill-name}.skill.prompt.md

# 4. Add bundled scripts for deterministic operations

# 5. Register in .github/copilot-skills/index.md

# 6. Validate compliance with 5 principles
```

---

## Architecture

### Three-Part System

**1. Skill Definitions** (`.github/copilot-skills/{skill-name}/`)
- `SKILL.md` - Core documentation with YAML frontmatter
- `patterns.md`, `reference.md` - Detail files (loaded on demand)
- `scripts/` - Bundled tools producing deterministic output

**2. Skill Prompts** (`.github/prompts/{skill-name}.skill.prompt.md`)
- Instructs AI WHEN to use the skill (use cases)
- Instructs AI HOW to execute step-by-step (workflow)
- Enables `/skill-{name}` slash commands in Copilot

**3. Management System** (`.github/copilot-skills/`)
- `index.md` - Registry and dynamic discovery
- `README.md` - Complete architecture documentation
- `scripts/` - Automation tools
- `templates/` - Scaffolding for new skills

### Progressive Disclosure Pattern

Information loads only when needed:

```
AI Agent Encounters Task
    ↓
    ├→ Check .github/copilot-skills/index.md
    │   (1 line: "Skill X - Does Y")
    │
    ├→ Relevant? Load .github/prompts/skill-x.prompt.md
    │   (Workflow instructions)
    │
    ├→ Need details? Load .github/copilot-skills/skill-x/SKILL.md
    │   (~100 lines core doc)
    │
    ├→ Need deep dive? Load patterns.md, reference.md
    │   (Detailed patterns and API reference)
    │
    └→ Need to execute? Run scripts/
        (Deterministic tools)
```

---

## Five Constitutional Principles

All skills must follow these (canonical source: `.specify/memory/constitution.md`):

### 1. Progressive Disclosure
Information loads in layers. Each layer independently useful and scannable in <3 minutes.

```
Layer 1: index.md entry (1 line) — Discover
Layer 2: SKILL.md (core, ~100 lines) — Understand
Layer 3: patterns.md (deep) — Learn details
Layer 4: reference.md (API) — Look up specifics
Layer 5: scripts/ (executable) — Do the work
```

### 2. File-Based Organization
Skills are self-contained directories with standardized structure.

```
copilot-skills/
└── {skill-name}/
    ├── SKILL.md (with YAML frontmatter)
    ├── patterns.md (optional)
    ├── reference.md (optional)
    ├── forms.md (optional)
    └── scripts/
        ├── tool1.sh
        ├── tool2.py
        └── ...
```

YAML frontmatter example:
```yaml
---
name: "Skill Name"
description: "One-sentence purpose"
version: "1.0.0"
tags: ["keyword1", "keyword2"]
dependencies: ["tool1", "tool2"]
---
```

### 3. Dynamic Discovery
Skills register in `.github/copilot-skills/index.md` for automatic discovery by AI agents.

| Skill | Description | Tags | Location |
|-------|-------------|------|----------|
| Template Skill | Skill X does Y | tag1, tag2 | `copilot-skills/skill-x/` |

### 4. Deterministic Execution
Scripts in `scripts/` produce consistent, reproducible output.

- Output to **terminal only** (no file generation)
- Self-contained and reproducible
- Respect `.gitignore` patterns automatically
- Documented with usage examples in SKILL.md
- Compatible with bash, Python, or other languages

### 5. Composability
Skills can reference each other with explicit dependencies. No circular references.

```yaml
dependencies:
  - "git-ops"          # Can depend on other skills
  - "pdf-handling"
```

---

## Project Structure

```
copilot-skills/
├── .github/
│   ├── copilot-instructions.md          # Main AI guidance
│   ├── copilot-skills/                  # Skills system
│   │   ├── index.md                     # Skill registry & discovery
│   │   ├── README.md                    # Architecture documentation
│   │   ├── templates/                   # Scaffolding for new skills
│   │   │   ├── SKILL.template.md
│   │   │   ├── skill-prompt.template.md
│   │   │   ├── detail-file.template.md
│   │   │   ├── script.template.sh
│   │   │   └── script.template.py
│   │   ├── scripts/                     # Automation tools
│   │   │   ├── bash/
│   │   │   └── python/
│   │   └── {skill-name}/                # Individual skills
│   │       ├── SKILL.md
│   │       ├── patterns.md
│   │       ├── reference.md
│   │       └── scripts/
│   ├── prompts/                         # Skill workflows
│   │   ├── {skill-name}.skill.prompt.md
│   │   ├── cleanup.skill.prompt.md
│   │   ├── create.skill.prompt.md
│   │   └── ...
│   └── .specify/
│       └── memory/
│           └── constitution.md          # Canonical 5 principles
├── examples/                            # Third-party skill collections
│   ├── anthropics-skills/               # Anthropic's official skills
│   ├── obra-superpowers/                # Obra community patterns
│   ├── superpowers-skills/              # General patterns
│   └── tfriedel-claude-office-skills/   # Office document skills
├── .gitignore                           # Respected by all scripts
├── readme.md                            # This file
├── copilot-skills.md                    # Technical deep-dive
└── [other resources]
```

---

## Development Patterns

### Bundled Scripts

Scripts are deterministic tools that:
- Output to terminal only (never create files)
- Respect `.gitignore` patterns automatically
- Produce consistent, reproducible results
- Work in any repository context
- Have clear, documented usage

Example usage:
```bash
bash .github/copilot-skills/{skill-name}/scripts/tool.sh --option value

# Output is displayed to terminal
# Output can be parsed by AI agents as data source
```

### Respecting .gitignore

All scripts automatically exclude:
- **Environment**: `.env`, `.env.*`, `*.log`
- **Dependencies**: `node_modules/`, `__pycache__/`, `.venv/`, `build/`, `dist/`
- **IDE Files**: `.vscode/`, `.idea/`, `*.iml`
- **Build Artifacts**: `*.pyc`, `*.egg-info/`, `package-lock.json`
- **Project-Specific**: `examples/`, `drafts/`, `*.bak`, `*.tmp`

This prevents:
- Accidentally documenting environment variables
- Analyzing third-party code
- Cluttering instructions with generated files
- Security risks from exposed secrets

### Templates for Reusability

Creating new skills is fast with provided templates:

```bash
# SKILL.md template
.github/copilot-skills/templates/SKILL.template.md

# Skill prompt template
.github/copilot-skills/templates/skill-prompt.template.md

# Detail file templates
.github/copilot-skills/templates/detail-file.template.md

# Script templates
.github/copilot-skills/templates/script.template.sh
.github/copilot-skills/templates/script.template.py
```

---

## What This Repository IS

✅ A reference implementation of progressive disclosure
✅ A working system for organizing domain knowledge
✅ A framework for creating and sharing reusable skills
✅ A complete template other teams can copy
✅ Portable across projects and compatible with multiple AI agents (Copilot, Claude, Cursor, Windsurf, etc.)

## What This Repository IS NOT

❌ A software application to build/deploy
❌ A typical project with application source code
❌ A framework or library to depend on
❌ A CI/CD or build system

---

## Success Metrics

- ✅ AI agents identify relevant skill in <2 minutes
- ✅ Each SKILL.md scannable in <3 minutes
- ✅ Progressive disclosure reduces context usage by 60%
- ✅ 95% of common tasks using ≤2 skills
- ✅ New skills authored in <30 minutes with templates
- ✅ Bundled scripts produce consistent terminal output
- ✅ All analysis respects .gitignore patterns
- ✅ Skills composable and referenceable

---

## Key Resources

| Resource | Purpose |
|----------|---------|
| `.github/copilot-instructions.md` | Main AI guidance for this repository |
| `.github/copilot-skills/README.md` | Complete architecture and system documentation |
| `.github/copilot-skills/index.md` | Skill registry and discovery |
| `.specify/memory/constitution.md` | 5 canonical constitutional principles |
| `copilot-skills.md` | Technical deep-dive and rationale |
| `examples/` | Third-party skill collections for reference |
| `.github/copilot-skills/templates/` | Templates for creating new skills quickly |

---

## Contributing

Skills are designed for sharing across teams and repositories.

To contribute:
1. Create skill in `.github/copilot-skills/{skill-name}/` using templates
2. Create skill prompt in `.github/prompts/{skill-name}.skill.prompt.md`
3. Validate all scripts output to terminal only, no file generation
4. Ensure compliance with all 5 constitutional principles
5. Add entry to `.github/copilot-skills/index.md`
6. Test bundled scripts work reliably
7. Include examples and edge cases
8. Submit PR with complete skill + prompt + documentation

---

## How to Learn the System

**Beginner**: Start here

1. Read this readme
2. Review `.github/copilot-skills/index.md` (see what's available)
3. Read one skill's SKILL.md (~5 min)
4. Look at its scripts/ directory
5. Understand the 5 principles in `.specify/memory/constitution.md`

**Intermediate**: Understand the architecture

1. Read `.github/copilot-skills/README.md` (complete docs)
2. Review multiple skills to see patterns
3. Read `.github/copilot-instructions.md` (how AI uses this)
4. Study a skill prompt in `.github/prompts/`
5. Understand why progressive disclosure matters

**Advanced**: Create new skills

1. Copy templates from `.github/copilot-skills/templates/`
2. Create your skill following the 5 principles
3. Write SKILL.md with clear examples
4. Create companion .skill.prompt.md
5. Add bundled scripts that output to terminal
6. Register in index.md
7. Validate compliance

---

## Principles in Action

**Problem**: AI agents get lost in complex codebases
**Solution**: Progressive disclosure — load info in layers only when needed

**Before (monolithic instructions)**:
```
File: .github/copilot-instructions.md (500+ lines)
- Everything in one file
- Overwhelming to read
- High context overhead
- Agents struggle to find relevant info
```

**After (progressive disclosure)**:
```
.github/copilot-skills/index.md
  ↓ (Agent sees 1 line per skill)
.github/prompts/{skill}.prompt.md
  ↓ (Agent learns workflow)
.github/copilot-skills/{skill}/SKILL.md
  ↓ (Agent understands core concept)
.github/copilot-skills/{skill}/patterns.md
  ↓ (Agent learns details only if needed)
.github/copilot-skills/{skill}/scripts/
  ↓ (Agent executes deterministic tools)
```

---

## References

- **IEEE/ACM**: Progressive Disclosure UI Patterns
- **Anthropic Claude Skills**: Reference implementation
- **Model Context Protocol (MCP)**: Composition patterns
- **Documentation Architecture**: Information layering best practices

---

**This is a reference implementation of the Copilot Skills Architecture for progressive disclosure of domain knowledge to AI agents.**

For questions, see `.github/copilot-skills/README.md` or review the complete specifications in the repository.

Start with: `.github/copilot-skills/index.md` → `.github/copilot-skills/README.md` → `.specify/memory/constitution.md`
