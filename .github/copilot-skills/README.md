# Copilot Skills Architecture

Organize domain-specific knowledge into discoverable, composable skills that keep AI context lean and focused.

## What Is the Skills Architecture?

The Copilot Skills Architecture is a modular system for organizing specialized knowledge in GitHub repositories. Skills follow a three-part architecture:

- **Discoverable**: Keyword routing map in `.github/copilot-instructions.md` enables AI to find skills
- **Progressive**: Information loads in layers (routing map → prompt → detail files → scripts)
- **Deterministic**: Bundled scripts provide consistent, reusable operations
- **Composable**: Skills reference each other for complex workflows
- **Independently tested**: Each skill can be validated against constitutional principles

## Core Principles (5 Constitutional Principles)

1. **Progressive Disclosure** - Layer information: routing map → prompt → details. Each file independently useful.
2. **File-Based Organization** - Skills are prompt + instructions + bundled scripts (three-part system)
3. **Dynamic Discovery** - Keyword routing map in `.github/copilot-instructions.md` enables AI to find relevant skills
4. **Deterministic Execution** - Bundled scripts produce consistent results
5. **Composability** - Skills reference each other; explicit dependencies; clear boundaries

See [`.specify/memory/constitution.md`](../../.specify/memory/constitution.md) for full details.

## Quick Start

### Discovering Skills

1. Check keyword routing map in `.github/copilot-instructions.md`
2. Look for keywords matching your task
3. Use suggested `/skill-{name}` command
4. Follow the skill prompt workflow
5. Load detail files when you need deeper information

### Using a Skill

```
User: "I need to extract form fields from a PDF"
→ Copilot checks keyword routing map
→ Finds "PDF" triggers PDF Handling skill
→ Suggests `/pdf-handling` command
→ Loads .github/prompts/pdf-handling.skill.prompt.md
→ Suggests bundled script in scripts/ directory
```

### Creating a New Skill

1. Copy templates from `.github/copilot-skills/templates/`
2. Create `.github/prompts/{skill-name}.skill.prompt.md`
3. Create `.github/instructions/{skill-name}.instructions.md`
4. Create directory `.github/copilot-skills/{skill-name}/` if needed for scripts/detail files
5. Add entry to keyword routing map in `.github/copilot-instructions.md`
6. Run skill compliance checklist (`.specify/checklists/skill-compliance-checklist.md`)

See [AUTHORING.md](./AUTHORING.md) for step-by-step guidance.

## Directory Structure

```
.github/
├── copilot-instructions.md     # Main routing + keyword map
├── prompts/                    # Skill prompt files
│   ├── git-ops.skill.prompt.md
│   ├── pdf-handling.skill.prompt.md
│   └── skill-template.skill.prompt.md
├── instructions/               # Auto-loaded context
│   ├── git-ops.instructions.md
│   ├── pdf-handling.instructions.md
│   └── skill-template.instructions.md
└── copilot-skills/            # Bundled scripts + detail files
    ├── README.md              # This file
    ├── templates/             # Templates for new skills
    ├── skill-template/        # Reference implementation
    │   ├── README.md          # Structure overview
    │   └── scripts/
    │       ├── example-script.py
    │       └── helper.sh
    ├── git-ops/              # Example: scripts only
    │   └── scripts/
    ├── pdf-handling/         # Example: scripts + detail files
    │   ├── forms.md
    │   ├── reference.md
    │   └── scripts/
    └── [other-skills]/
```

## Key Concepts

### Skill
A self-contained package of instructions, patterns, and scripts for a specialized domain. Located in `.github/copilot-skills/{skill-name}/` with a SKILL.md core file.

### Skill Metadata
YAML frontmatter at the top of SKILL.md containing name, description, version, tags, and dependencies:

```yaml
---
name: "PDF Handling"
description: "Extract text, fill forms, and manipulate PDF documents"
version: "1.0.0"
tags: ["documents", "pdf", "forms"]
dependencies: ["pypdf2", "pdfplumber"]
---
```

### Detail File
Markdown files in a skill directory (e.g., forms.md, reference.md) providing focused information on specific topics. Each stands independently and can be read without reading others.

### Bundled Script
Executable scripts (Python, Shell, JavaScript, etc.) in a skill's `scripts/` subdirectory. Used for deterministic operations documented in skill prompts.

### Keyword Routing Map
The keyword routing map in `.github/copilot-instructions.md` listing all available skills with trigger keywords, enabling AI to discover relevant skills automatically.

## Progressive Disclosure: 3-Layer Model

Skills use a 3-layer information architecture:

1. **Layer 1: Keyword Routing** (30 seconds)
   - Skill name, keywords, triggers in `.github/copilot-instructions.md`
   - Enables AI to determine relevance and suggest skill

2. **Layer 2: Skill Prompt** (3 minutes)
   - Workflow, use cases, step-by-step instructions in `.github/prompts/`
   - Sufficient for most common use cases
   - Directs to detail files for specific topics

3. **Layer 3: Detail Files & Scripts** (5-15 minutes, on-demand)
   - Deep dives into specific topics (forms.md, reference.md, calculations.md)
   - Bundled executables for deterministic operations
   - Only loaded when specific guidance needed

**Benefits**: 
- First-time users get oriented in 3 minutes via prompt
- Advanced users find detailed information when needed
- Context window stays lean (don't load what you don't need)

## Skill Composition: Complex Workflows

Skills can reference other skills to enable complex workflows:

```
Task: "Generate a financial report as a PDF with branded styling"

Workflow:
1. Load Financial Reporting skill
   → Generates report data (templates, calculations)
2. Load PDF Building skill
   → Converts data to PDF format
3. Load Brand Guidelines skill
   → Applies styling and fonts

Result: Composed workflow using 3 coordinated skills
```

**Guidelines**:
- Declare dependencies in SKILL.md metadata
- Use relative paths for cross-skill references
- Prevent circular dependencies (manual PR review validates)

## Success Metrics

By implementing the skills architecture, we achieve:

- **Discoverability**: Developers identify & load correct skill in <2 minutes
- **Efficiency**: Each SKILL.md scannable in <3 minutes
- **Context Savings**: 60% reduction in context usage vs. monolithic approach
- **Coverage**: 95% of common tasks handled by loading ≤2 skills
- **Authoring**: New skills created in <30 minutes using templates

## Integration Points

### In `.github/copilot-instructions.md`

The main Copilot instructions contain the skills system:
- Keyword routing map for skill discovery
- Explain when to reference specific skills
- Show three-part architecture (prompt + instructions + directory)

### In `.specify/templates/`

Templates for creating new features, specs, and tasks reference the skills architecture:
- Skill authoring workflow
- Spec templates for new skills
- PR checklist for skill review

### In `.specify/checklists/`

Compliance checklist ensures all skills meet constitutional principles:
- Progressive disclosure validation
- Metadata clarity check
- Script determinism verification

## Common Patterns from Examples

### From Anthropic Official Skills
- Metadata-first design (name + description drive discovery)
- Layered documentation (core + detail files)
- Executable scripts for determinism
- Tagged categorization by domain

### From Community Skills
- Skills as commands (e.g., `/brainstorm`, `/write-plan`)
- Cross-skill workflows (skills reference each other)
- Skill composition for complex tasks

## Next Steps

1. **For developers**: Check keyword routing map in `.github/copilot-instructions.md` to see available skills
2. **For skill authors**: Use `/skill-template` command or see `.github/copilot-skills/skill-template/README.md`
3. **For skill reviews**: See [GOVERNANCE.md](./GOVERNANCE.md) for PR checklist
4. **For maintenance**: See [MAINTENANCE.md](./MAINTENANCE.md) for updates and versioning
5. **Troubleshooting**: See [TROUBLESHOOTING.md](./TROUBLESHOOTING.md) for common issues

---

**Last Updated**: October 18, 2025  
**Version**: 1.0.0  
**Maintained by**: [Project Team]
