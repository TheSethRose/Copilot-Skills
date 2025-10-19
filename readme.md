# Copilot Skills

## Overview

**Copilot Skills** is a system for organizing domain knowledge into reusable, discoverable skills that keep AI agents focused and efficient.

Instead of one large instruction file, this design uses **progressive disclosure** — loading only what’s needed, when it’s needed. Agents discover skills automatically, read the core docs in about three minutes, and load details on demand.

This repository includes:
- ✅ **Skill System** – Self-contained knowledge modules with scripts
- ✅ **Progressive Disclosure** – Metadata → Core → Details layers
- ✅ **Constitutional Framework** – Five architectural principles every skill follows
- ✅ **Automation Tools** – Scripts for building, validating, and managing skills
- ✅ **Reference Skills** – Examples from Anthropic, Obra, and the community

**Status**: Fully implemented and production-ready, with working examples and templates.

---

## Quick Start

### Understand the System
```bash
# 1. Read the main architecture guide
cat .github/copilot-skills/README.md

# 2. Review the 5 canonical principles
cat .specify/memory/constitution.md

# 3. Check available skills
cat .github/copilot-instructions.md  # See keyword routing map
````

### Create a Skill

```bash
# 1. Copy the prompt template
cp .github/copilot-skills/templates/skill-prompt.template.md \
   .github/prompts/{skill-name}.skill.prompt.md

# 2. Copy the instructions template
cp .github/copilot-skills/templates/instructions.template.md \
   .github/instructions/{skill-name}.instructions.md

# 3. Create folder for scripts/detail files (if needed)
mkdir -p .github/copilot-skills/{skill-name}/scripts

# 4. Add scripts for deterministic operations (if needed)
# 5. Register in keyword routing map (.github/copilot-instructions.md)
# 6. Validate against the 5 principles
```

---

## Architecture

### Three-Part System

**1. Skill Definitions** (`.github/copilot-skills/{skill-name}/`)

* `SKILL.md` – Core documentation with YAML frontmatter
* `patterns.md`, `reference.md` – Optional detail files
* `scripts/` – Deterministic tools for execution

**2. Skill Prompts** (`.github/prompts/{skill-name}.skill.prompt.md`)

* Tell the AI when to use the skill
* Explain how to run it step-by-step
* Enable `/skill-{name}` commands in Copilot

**3. Instructions Files** (`.github/instructions/{skill-name}.instructions.md`)

* Auto-loaded context for file patterns or keywords
* Default behaviors and quality guidelines
* Common workflows and examples

**4. Management System** (`.github/copilot-skills/`)

* `README.md` – Full system documentation
* `scripts/` – Automation utilities
* `templates/` – Scaffolding for new skills
* `{skill-name}/` – Bundled scripts and detail files

---

### Progressive Disclosure

Information loads in layers:

```
AI Agent Encounters Task
    ↓
    ├→ Check keyword routing map
    │   (Keywords trigger skill suggestion)
    ├→ Load prompt (workflow)
    ├→ Load detail files (patterns.md, reference.md)
    └→ Run scripts/ (execute deterministically)
```

---

## Five Constitutional Principles

All skills must follow these rules (`.specify/memory/constitution.md`):

### 1. Progressive Disclosure

Information appears in small, useful layers, each readable in under 3 minutes.

```
Layer 1: Keyword routing map – Discover
Layer 2: Skill prompt – Understand workflow
Layer 3: Detail files – Learn specifics (patterns.md, reference.md)
Layer 4: Scripts – Execute deterministically
```

### 2. File-Based Structure

Each skill is self-contained with a standard layout.

```
copilot-skills/
└── {skill-name}/
    ├── SKILL.md
    ├── patterns.md (optional)
    ├── reference.md (optional)
    ├── forms.md (optional)
    └── scripts/
```

**Example frontmatter:**

```yaml
---
name: "Skill Name"
description: "Short purpose"
version: "1.0.0"
tags: ["keyword1", "keyword2"]
dependencies: ["tool1", "tool2"]
---
```

### 3. Dynamic Discovery

Skills register in keyword routing map (`.github/copilot-instructions.md`) so AI agents can find them automatically.

| Skill          | Keywords       | Suggest    | Location                  |
| -------------- | -------------- | ---------- | ------------------------- |
| PDF Handling   | pdf, document  | `/pdf-handling` | `.github/prompts/pdf-handling.skill.prompt.md` |

### 4. Deterministic Execution

All scripts must produce consistent, reproducible output.

* Output to terminal only
* No file creation
* Respect `.gitignore`
* Include usage examples
* Compatible with Bash, Python, etc.

### 5. Composability

Skills can depend on others, but never in loops.

```yaml
dependencies:
  - "git-ops"
  - "pdf-handling"
```

---

## Project Structure

*(kept intact, just cleaned and aligned)*

```
copilot-skills/
├── .github/
│   ├── copilot-instructions.md       # Keyword routing map
│   ├── prompts/                      # Skill workflows
│   │   └── {skill-name}.skill.prompt.md
│   ├── instructions/                 # Auto-loaded context
│   │   └── {skill-name}.instructions.md
│   ├── copilot-skills/               # Bundled scripts + details
│   │   ├── README.md
│   │   ├── templates/
│   │   ├── scripts/
│   │   └── {skill-name}/
│   └── .specify/memory/constitution.md
├── examples/
├── .gitignore
├── readme.md
└── ...
```

---

## Development Patterns

### Bundled Scripts

Scripts are deterministic tools that:

* Output to terminal only
* Respect `.gitignore`
* Produce the same results every time
* Work in any repo context
* Include clear examples

Example:

```bash
bash .github/copilot-skills/{skill-name}/scripts/tool.sh --option value
```

### Respecting .gitignore

All scripts ignore:

* `.env`, `*.log`, `node_modules/`, `__pycache__/`, `.venv/`, etc.
* IDE and build artifacts
* Temporary or example files

This prevents leaks, noise, and irrelevant analysis.

### Templates for Speed

Templates make new skills easy to create:

```bash
.github/copilot-skills/templates/SKILL.template.md
.github/copilot-skills/templates/skill-prompt.template.md
.github/copilot-skills/templates/detail-file.template.md
.github/copilot-skills/templates/script.template.{sh,py}
```

---

## What This Repository Is

✅ A reference for progressive disclosure
✅ A framework for organizing domain knowledge
✅ A system for reusable AI skills
✅ A portable template for any team or agent

## What This Repository Is Not

❌ A deployable app
❌ A source-code project
❌ A CI/CD or build system

---

## Success Metrics

* AI finds the right skill in under 2 minutes
* SKILL.md readable in under 3 minutes
* Context use cut by 60%
* 95% of tasks use two or fewer skills
* New skills built in under 30 minutes
* Output always deterministic
* All `.gitignore` rules respected
* Skills composable and referenceable

---

## Key Resources

| File                                | Purpose                |
| ----------------------------------- | ---------------------- |
| `.github/copilot-instructions.md`   | Main AI guidance + keyword routing |
| `.github/copilot-skills/README.md`  | Full architecture documentation |
| `.specify/memory/constitution.md`   | Canonical 5 principles |
| `examples/`                         | Third-party skills     |
| `.github/copilot-skills/templates/` | Quick-start templates  |
| `.github/prompts/`                  | Skill workflows        |
| `.github/instructions/`             | Auto-loaded context    |

---

## Contributing

To add a skill:

1. Copy templates from `.github/copilot-skills/templates/`
2. Create `.github/prompts/{skill-name}.skill.prompt.md`
3. Create `.github/instructions/{skill-name}.instructions.md`
4. Create `.github/copilot-skills/{skill-name}/` for scripts/details (if needed)
5. Ensure scripts print to terminal only
6. Follow all 5 principles
7. Register in keyword routing map (`.github/copilot-instructions.md`)
8. Test and document usage
9. Submit a PR with skill, prompt, instructions, and docs

---

## Learning Path

**Beginner**

1. Read this README
2. Check keyword routing map in `.github/copilot-instructions.md`
3. Try a skill command (e.g., `/pdf-handling`)
4. Explore its scripts/
5. Review the 5 principles

**Intermediate**

1. Study `.github/copilot-skills/README.md`
2. Compare multiple skills
3. Read `.github/copilot-instructions.md`
4. Review prompts in `/prompts/`
5. Understand progressive disclosure

**Advanced**

1. Copy templates
2. Write SKILL.md and prompt
3. Add scripts that output deterministically
4. Register and validate

---

## Principles in Action

**Problem:** AI agents drown in large instruction files
**Solution:** Break knowledge into discoverable, layered skills

**Before**

```
One 500-line instruction file:
- Hard to scan
- High context cost
- Poor relevance
```

**After**

```
Keyword routing map → skill discovery
prompt.md → workflow
detail files (patterns.md, reference.md) → specifics
scripts/ → deterministic actions
```

---

## References

* IEEE/ACM: Progressive Disclosure Patterns
* Anthropic Claude Skills: Reference implementation
* Model Context Protocol (MCP): Composition model
* Documentation Architecture: Information layering