# Copilot Skills Architecture

Organize domain-specific knowledge into discoverable, composable skills that keep AI context lean and focused.

## What Is the Skills Architecture?

The Copilot Skills Architecture is a modular system for organizing specialized knowledge in GitHub repositories. Instead of one monolithic `copilot-instructions.md` file, skills are:

- **Discoverable**: Listed in `.github/copilot-skills/index.md` with clear metadata
- **Progressive**: Information loads in layers (index → SKILL.md → detail files → scripts)
- **Deterministic**: Bundled scripts provide consistent, reusable operations
- **Composable**: Skills reference each other for complex workflows
- **Independently tested**: Each skill can be validated against constitutional principles

## Core Principles (5 Constitutional Principles)

1. **Progressive Disclosure** - Layer information: metadata → core → details. Each file independently useful.
2. **File-Based Organization** - Skills are directories with SKILL.md + detail files + scripts/
3. **Dynamic Discovery** - `.github/copilot-skills/index.md` enables AI to find relevant skills
4. **Deterministic Execution** - Bundled scripts produce consistent results
5. **Composability** - Skills reference each other; explicit dependencies; clear boundaries

See [`.specify/memory/constitution.md`](../../.specify/memory/constitution.md) for full details.

## Quick Start

### Discovering Skills

1. Open `.github/copilot-skills/index.md`
2. Scan the registry for skills relevant to your task
3. Click the skill path to open its SKILL.md
4. Read core capabilities (~3 minutes)
5. Link to detail files when you need deeper information

### Using a Skill

```
User: "I need to extract form fields from a PDF"
→ Copilot scans .github/copilot-skills/index.md
→ Finds "PDF Handling" skill
→ Loads .github/copilot-skills/pdf-handling/SKILL.md
→ Suggests bundled script in scripts/ directory
```

### Creating a New Skill

1. Create directory: `.github/copilot-skills/{skill-name}/`
2. Write SKILL.md with YAML frontmatter (see [AUTHORING.md](./AUTHORING.md) for template)
3. Add detail files for deep topics (forms.md, reference.md, etc.)
4. Add bundled scripts in scripts/ if needed
5. Register in index.md
6. Run skill compliance checklist (`.specify/checklists/skill-compliance-checklist.md`)

See [AUTHORING.md](./AUTHORING.md) for step-by-step guidance.

## Directory Structure

```
.github/copilot-skills/
├── index.md                  # Skills registry (start here)
├── README.md                 # This file
├── AUTHORING.md              # Guide for creating new skills
├── GOVERNANCE.md             # PR review process and skill lifecycle
├── MAINTENANCE.md            # Skill updates and version management
├── TROUBLESHOOTING.md        # Common issues and solutions
├── EXAMPLES.md               # Example workflows showing skill composition
│
├── skill-template/           # Example skill showing structure
│   ├── SKILL.md              # Core skill file with YAML frontmatter
│   ├── patterns.md           # Detail file: pattern examples
│   ├── reference.md          # Detail file: comprehensive reference
│   └── scripts/
│       ├── example-script.py # Python script example
│       └── helper.sh         # Shell script example
│
└── [other-skills]/           # Additional skills follow same pattern
    ├── SKILL.md
    ├── [detail-file].md
    └── scripts/
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
Executable scripts (Python, Shell, JavaScript, etc.) in a skill's `scripts/` subdirectory. Used for deterministic operations documented in SKILL.md.

### Skills Registry
The `.github/copilot-skills/index.md` file listing all available skills with lightweight metadata, enabling AI to discover relevant skills without parsing full documentation.

## Progressive Disclosure: 4-Layer Model

Skills use a 4-layer information architecture:

1. **Layer 1: Index Metadata** (30 seconds)
   - Skill name, description, when_to_use, tags
   - Enables AI to determine relevance

2. **Layer 2: SKILL.md** (3 minutes)
   - Core capabilities, quick start examples, patterns
   - Sufficient for most common use cases
   - Links to detail files for specific topics

3. **Layer 3: Detail Files** (5-15 minutes)
   - Deep dives into specific topics (forms.md, reference.md, calculations.md)
   - Each file focuses on single topic
   - Only read when specific guidance needed

4. **Layer 4: Scripts** (On-demand)
   - Bundled executables for deterministic operations
   - Input/output contracts documented in SKILL.md
   - Used when consistent results needed across codebase

**Benefits**: 
- First-time users get oriented in 3 minutes
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

The main Copilot instructions reference the skills system:
- Link to `.github/copilot-skills/index.md` for skill discovery
- Explain when to reference specific skills
- Show example skill-based workflows

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

1. **For developers**: Read `.github/copilot-skills/index.md` to see available skills
2. **For skill authors**: See [AUTHORING.md](./AUTHORING.md) for step-by-step guide
3. **For skill reviews**: See [GOVERNANCE.md](./GOVERNANCE.md) for PR checklist
4. **For maintenance**: See [MAINTENANCE.md](./MAINTENANCE.md) for updates and versioning
5. **Troubleshooting**: See [TROUBLESHOOTING.md](./TROUBLESHOOTING.md) for common issues

---

**Last Updated**: October 18, 2025  
**Version**: 1.0.0  
**Maintained by**: [Project Team]
