# Copilot Skills Architecture - Developer Guide

This project implements a **skills-based architecture for GitHub Copilot** that mirrors Anthropic's Claude Skills. The goal: organize domain-specific knowledge into discoverable, composable skills that keep AI context lean and focused.

## Project Architecture

### The Core Problem We're Solving
Monolithic instruction files bloat AI context and make it hard to maintain. This project enables modular, reusable skills stored as markdown + scripts in `.github/copilot-skills/`, discoverable through an index, and loaded only when relevant.

### Five Constitutional Principles

All implementation decisions derive from these principles (defined in `.specify/memory/constitution.md`):

1. **Progressive Disclosure** - Information loads in layers: metadata → core instructions → detailed references. Each file must be independently useful.
2. **File-Based Organization** - Skills are self-contained directories with `SKILL.md` core file + YAML frontmatter (name, description, version, tags, dependencies).
3. **Dynamic Discovery Through Metadata** - `.github/copilot-skills/index.md` registry enables AI agents to find relevant skills without parsing full documentation.
4. **Deterministic Execution with Scripts** - Complex operations include bundled scripts (in `scripts/` subdirectories) that produce consistent results regardless of context.
5. **Composability and Cross-Skill References** - Skills may reference each other for complex workflows; dependencies declared in metadata; boundaries clear to prevent circular references.

## Skill File Structure

### Essential Pattern (Every skill MUST follow this)

```
.github/copilot-skills/
├── index.md                      # Registry of all skills
├── {skill-name}/
│   ├── SKILL.md                  # Core file (YAML frontmatter + markdown)
│   ├── {detail-file}.md          # Optional: forms.md, reference.md, etc.
│   └── scripts/
│       └── {operation}.{ext}     # Bundled executable (python, bash, js, etc.)
```

### SKILL.md Template

```markdown
---
name: "Descriptive Skill Name"
description: "What this skill enables developers to do"
version: "1.0.0"
tags: ["domain", "keywords"]
dependencies: ["library1", "tool2"]
---

# Skill Name

## Overview
[Why this skill exists]

## Core Capabilities
- [What developers can do with this skill]
- [Common use case]

## Quick Start
[One quick example - minimal code/command]

## Bundled Scripts
- `script.py` - Description of what it does and typical invocation

## Detailed References
For [topic], see [linked-file.md]
```

### Key Principles for Skill Authoring

- **Metadata is critical** - Copilot uses the name and description to decide relevance. Be specific, not generic.
- **Keep SKILL.md scannable** - Core file should be understood in <3 minutes. Move complex examples/region-specific logic to linked files.
- **Scripts provide determinism** - Don't ask Copilot to reimplement logic. Bundle it as executable. Examples:
  - `.github/copilot-skills/pdf-handling/scripts/extract_form_fields.py`
  - `.github/copilot-skills/compliance-tracking/scripts/check-license-status.js`
- **Detail files are lazy-loaded** - `forms.md`, `reference.md`, `calculations.md` are only read when Copilot needs that specific knowledge.
- **Explicit cross-skill refs** - If Skill A depends on Skill B, document it in metadata and link explicitly. Prevents circular dependencies.

## Developer Workflows

### Creating a New Skill

1. **Use the feature specification process** (see `.specify/memory/constitution.md` and `.github/prompts/speckit.*.prompt.md`)
2. **Study existing skills** in `examples/` (Anthropic's official skills + community implementations)
3. **Create directory** `.github/copilot-skills/{skill-name}/`
4. **Write SKILL.md** with YAML frontmatter, core capabilities, quick start, patterns, and linked file references
5. **Add bundled scripts** in `scripts/` subdirectory if the skill needs deterministic operations
6. **Register in index.md** - Add entry with name, description, path, tags, and "when to use" guidance
7. **Reference from main copilot-instructions.md** - Help developers discover the skill

### Testing a Skill

- **Index discoverability**: Can Copilot find the skill by reading `.github/copilot-skills/index.md`?
- **Metadata clarity**: Is the "when to use" guidance distinct from other skills?
- **Progressive loading**: Does each linked file stand alone? Can you read SKILL.md without the detail files?
- **Script determinism**: Do bundled scripts produce consistent outputs? Are invocations documented?

### Example: PDF Handling Skill

```
.github/copilot-skills/pdf-handling/
├── SKILL.md               # Core: capabilities, quick start, error handling
├── forms.md               # Detail: form-filling specifics (IRS forms, gov apps, etc.)
├── reference.md           # Detail: PyPDF2 & pdfplumber API docs
└── scripts/
    └── extract_form_fields.py
        # Deterministic extraction; CLI usage documented in SKILL.md
```

When a developer says "extract form fields from this PDF," Copilot:
1. Scans `index.md` → finds PDF Handling skill is relevant
2. Reads `SKILL.md` → suggests using the bundled script
3. On demand, reads `forms.md` → for form-type-specific patterns
4. On demand, reads `reference.md` → for library API details

## Project Organization

### Key Directories

- **`.github/copilot-skills/`** - Where all skills live. This is the canonical source of truth for domain knowledge.
- **`.specify/`** - Feature specification infrastructure. Contains templates for specs, plans, tasks, and research.
- **`specs/`** - Feature-specific documentation (e.g., `specs/001-skill-architecture/`)
- **`examples/`** - Reference implementations from Anthropic and community
- **`docs/`** - Project-wide documentation (architecture, conventions)

### Configuration & Governance

- **`.specify/memory/constitution.md`** - The five principles and governance rules. All skills must adhere.
- **`.specify/templates/`** - Templates for specs, plans, tasks, checklists
- **`.specify/memory/`** - Project constitution and shared context

## Integration with Copilot

### How Copilot Discovers Skills

**Automatic Discovery**
```
User: "I need to extract form fields from a PDF"
→ Copilot checks .github/copilot-skills/index.md
→ Finds PDF Handling skill relevant
→ Loads pdf-handling/SKILL.md
→ Suggests using bundled script
```

**Explicit Reference**
```
User: "Using the PDF handling skill, extract all fields from form.pdf"
→ Copilot loads .github/copilot-skills/pdf-handling/SKILL.md directly
```

**Progressive Loading**
```
User: "Fill out this government tax form"
→ Loads pdf-handling/SKILL.md (core)
→ Sees reference to forms.md
→ Loads pdf-handling/forms.md on demand (specific form patterns)
→ Later, if needed, loads reference.md (API docs)
```

### What Copilot MUST NOT Do

- **Don't inline skill content into prompts** - Reference files by path. Let Copilot load as needed.
- **Don't create duplicate logic** - If a skill has a bundled script, have Copilot suggest it instead of reimplementing.
- **Don't mix skills with main instructions** - Link to skills from `.github/copilot-instructions.md`, don't copy content.

## Common Patterns from Examples

### From Anthropic's Official Skills

- **Metadata-first design** - Name and description are what AI agents rely on for discovery
- **Layered documentation** - Core SKILL.md stays focused; detail files are deep dives
- **Executable scripts** - Many skills include Python/JavaScript/Bash scripts for deterministic operations
- **Tagged categorization** - Skills tagged by domain (e.g., `["documents", "forms", "pdf"]`)

### From Community Skills (obra/superpowers)

- **Commands as skills** - `/brainstorm`, `/write-plan`, `/execute-plan` are implemented as loadable skills
- **Cross-skill workflows** - Skills reference each other; hooks enable integration
- **Skill composition** - Users can combine multiple skills for complex tasks

## Success Metrics (from specification)

- Developers identify and load the correct skill in <2 minutes
- Each SKILL.md scannable in <3 minutes
- Progressive disclosure reduces context usage by 60% vs. monolithic approach
- 95% of common task scenarios handled by loading ≤2 skills
- New skills can be authored in <30 minutes

## When to Create a Skill

Create a new skill when:
- A domain of knowledge is substantial enough to warrant its own documentation
- Multiple developers or Copilot interactions will reference the same patterns
- The skill can be independently tested and deployed
- Clear boundaries exist between this skill and others

**Don't create a skill for:**
- One-off utilities or single functions
- Aspirational patterns not yet proven in the codebase
- Content better suited to per-project README

## Next Steps for AI Agents

1. **Read `.github/copilot-skills/index.md`** to see what skills exist
2. **Review constitution.md** to understand the five principles
3. **Study `examples/anthropics-skills/`** to see official patterns
4. **Check `specs/001-skill-architecture/`** for feature details (spec.md, plan.md, research.md)
5. **When implementing**: follow the SKILL.md template, use bundled scripts for determinism, link progressively
