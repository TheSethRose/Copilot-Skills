# Copilot Skills: Progressive Disclosure for GitHub Copilot
*Published Oct 18, 2025 | Updated Oct 18, 2025*

GitHub Copilot is powerful for code completion, but production projects need more—they need structured domain knowledge, repeatable workflows, and automated validation. **Copilot Skills** brings Anthropic's Claude Skills architecture to GitHub Copilot through an integrated system of markdown documentation, executable scripts, and prompt-based workflows.

This repository demonstrates a complete skills system with:
- 📚 **Progressive Disclosure** - Load domain knowledge in layers (metadata → core → details)
- 🔧 **Executable Automation** - Scripts to create, validate, and manage skills
- 💬 **Prompt-Based Workflows** - Commands like `/skills.create` and `/skill-{name}` for discovery
- ✅ **Constitution Compliance** - Automated validation against architectural principles
- 🔄 **Agent Context Integration** - Skills automatically register with Copilot's context

---

## Why Skills Matter

Large language models excel at code patterns but can't hold entire codebases or domain knowledge in context. Copilot Skills solve this through **progressive disclosure**—loading information in layers only when needed.

### The Three-Part Architecture

1. **Skill Files** (`.github/copilot-skills/{skill-name}/`)
   - `SKILL.md` - Core instructions with YAML metadata
   - `patterns.md`, `reference.md` - Detail files loaded on demand
   - `scripts/` - Bundled tools for deterministic execution

2. **Skill Prompts** (`.github/prompts/skill-{skill-name}.prompt.md`)
   - Tells Copilot WHEN to use the skill (relevance detection)
   - Tells Copilot HOW to load progressively (file ordering)
   - Enables `/skill-{name}` commands for explicit invocation

3. **Management Commands** (`.github/prompts/skills.*.prompt.md`)
   - `/skills.create` - Create new skills with validation
   - `/skills.discover` - Search for relevant skills
   - `/skills.use` - Load a skill into context

This mirrors the `.specify/` infrastructure used for feature development, bringing the same level of automation to domain knowledge management.

---

## Complete Directory Structure

```
.github/
├── copilot-instructions.md              # Main workspace instructions
├── prompts/                             # Command definitions
│   ├── skills.create.prompt.md          # /skills.create command
│   ├── skill-hello-skill.prompt.md      # /skill-hello-skill command
│   ├── speckit.*.prompt.md              # Feature development (/speckit.specify, etc.)
│   └── cleanup.prompt.md                # /cleanup command
├── copilot-skills/                      # Skills registry
│   ├── index.md                         # Skills discovery index
│   ├── README.md                        # System overview
│   ├── AUTHORING.md                     # Skill creation guide
│   ├── GOVERNANCE.md                    # Constitutional principles
│   ├── MAINTENANCE.md                   # Updating and deprecation
│   ├── TROUBLESHOOTING.md               # Common issues
│   ├── EXAMPLES.md                      # Example skills catalog
│   ├── templates/                       # Skill scaffolding
│   │   ├── SKILL.template.md
│   │   ├── detail-file.template.md
│   │   └── skill-prompt.template.md
│   ├── scripts/                         # Automation tools
│   │   ├── bash/
│   │   │   └── common.sh                # Shared shell utilities
│   │   └── python/
│   │       ├── yaml_validator.py        # Frontmatter validation
│   │       └── skill_schema.yaml        # YAML schema definition
│   └── hello-skill/                     # Example skill (demo only)
│       ├── SKILL.md                     # Core instructions
│       ├── patterns.md                  # Detail file (patterns)
│       ├── reference.md                 # Detail file (API docs)
│       └── scripts/
│           └── hello-example.py         # Bundled script
└── .specify/                            # Feature development system
    ├── memory/
    │   └── constitution.md              # Five constitutional principles
    ├── templates/
    │   ├── spec.template.md
    │   ├── plan.template.md
    │   └── tasks.template.md
    └── scripts/
        └── bash/
            └── common.sh
```

---

## The Five Constitutional Principles

All skills must adhere to these principles (defined in `.specify/memory/constitution.md`):

### 1. Progressive Disclosure
Information loads in layers: metadata → core instructions → detailed references. Each file must be independently useful and scannable in <3 minutes.

### 2. File-Based Organization
Skills are self-contained directories with `SKILL.md` core file + YAML frontmatter (name, description, version, tags, dependencies).

### 3. Dynamic Discovery Through Metadata
`.github/copilot-skills/index.md` registry enables AI agents to find relevant skills without parsing full documentation.

### 4. Deterministic Execution with Scripts
Complex operations include bundled scripts (in `scripts/` subdirectories) that produce consistent results regardless of context.

### 5. Composability and Cross-Skill References
Skills may reference each other for complex workflows; dependencies declared in metadata; boundaries clear to prevent circular references.

---

## How Copilot Discovers and Uses Skills

### Automatic Discovery
```
User: "I need to extract form fields from a PDF"
→ Copilot checks .github/copilot-skills/index.md
→ Finds PDF Handling skill relevant
→ Loads pdf-handling/SKILL.md
→ Suggests using bundled script
```

### Explicit Reference via Commands
```
User types: /skill-pdf-handling
→ Copilot reads .github/prompts/skill-pdf-handling.prompt.md
→ Prompt instructs to load .github/copilot-skills/pdf-handling/SKILL.md
→ Shows capabilities and quick start
→ Loads detail files (forms.md, reference.md) on demand
```

### Progressive Loading
```
User: "Fill out this government tax form"
→ Loads pdf-handling/SKILL.md (core instructions)
→ Sees reference to forms.md
→ Loads pdf-handling/forms.md on demand (form-specific patterns)
→ Later, if needed, loads reference.md (library API details)
```

---

## Creating Your First Skill

### Option 1: Use the Management Command
```
1. Type: /skills.create in Copilot Chat
2. Follow the guided prompts
3. Copilot generates:
   - .github/copilot-skills/{skill-name}/SKILL.md
   - .github/prompts/skill-{skill-name}.prompt.md
   - Entry in .github/copilot-skills/index.md
4. Review and edit generated files
5. Validate with: /skills.validate {skill-name}
```

### Option 2: Manual Creation
```bash
# 1. Create skill directory
mkdir -p .github/copilot-skills/my-skill/scripts

# 2. Copy template
cp .github/copilot-skills/templates/SKILL.template.md \
   .github/copilot-skills/my-skill/SKILL.md

# 3. Edit SKILL.md with your content

# 4. Create prompt file
cp .github/copilot-skills/templates/skill-prompt.template.md \
   .github/prompts/skill-my-skill.prompt.md

# 5. Register in index.md
# Add entry to .github/copilot-skills/index.md

# 6. Validate (when script available)
.github/copilot-skills/scripts/bash/validate-skill.sh my-skill
```

---

## Skill File Format

### SKILL.md with YAML Frontmatter

```markdown
---
name: "PDF Document Handling"
description: "Extract text, fill forms, and manipulate PDF documents"
version: "1.0.0"
created: "2025-10-18"
tags: ["documents", "forms", "pdf", "text-extraction"]
dependencies: ["pypdf2", "pdfplumber"]
---

# PDF Document Handling Skill

## Overview
This skill provides capabilities for reading, parsing, and manipulating PDF documents, including form field extraction and programmatic form filling.

## Core Capabilities
- Extract text content from PDFs
- Parse form fields and values
- Fill PDF forms programmatically
- Extract tables and structured data
- Handle password-protected files

## Quick Start

### Extracting Form Fields
Use the bundled script:
```bash
python .github/copilot-skills/pdf-handling/scripts/extract_form_fields.py input.pdf
```

### Reading PDF Content
```python
import pdfplumber
with pdfplumber.open("document.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```

## Progressive References
- For form-filling patterns → see [forms.md](./forms.md)
- For library API details → see [reference.md](./reference.md)

## Common Patterns
[Document patterns with code examples]

## Error Handling
[Common errors and solutions]
```

---

## Available Commands

### Skill Management
- `/skills.create` - Create a new skill with guided workflow
- `/skills.discover` - Search for skills by keywords
- `/skills.validate` - Check skill compliance with constitution
- `/skills.use <name>` - Load a skill into context

### Individual Skills
- `/skill-hello-skill` - Load the demo skill
- `/skill-{name}` - Load any registered skill by name

### Feature Development (via `.specify/`)
- `/speckit.specify` - Create a feature specification
- `/speckit.plan` - Generate implementation plan
- `/speckit.tasks` - Break plan into tasks
- `/speckit.implement` - Execute implementation
- `/speckit.analyze` - Analyze codebase context

### Utilities
- `/cleanup` - Clean up repository (remove temp files, organize docs)

---

## Example Skills from the Community

This repository includes examples from:

### 1. Anthropic's Official Skills (`examples/anthropics-skills/`)
- **document-skills/** - DOCX, PDF, PPTX, XLSX manipulation
- **mcp-builder/** - Model Context Protocol server creation
- **skill-creator/** - Meta-skill for creating new skills
- **slack-gif-creator/** - Animated GIF generation for Slack
- **canvas-design/** - SVG design with custom fonts
- **brand-guidelines/** - Brand-compliant document generation

### 2. Obra's Superpowers (`examples/obra-superpowers/`)
- Commands: `/brainstorm`, `/write-plan`, `/execute-plan`
- Skills for: TDD, code review, debugging, git worktrees

### 3. Community Skills (`examples/superpowers-skills/`)
- Architecture, collaboration, debugging, testing patterns

### 4. Office Skills (`examples/tfriedel-claude-office-skills/`)
- DOCX, PDF, PPTX, XLSX manipulation with local tools

See [`examples/README.md`](./examples/README.md) for details.

---

## Project Organization

```
├── readme.md                        # This file
├── copilot-skills.md                # Technical architecture explanation
├── docs/                            # Project documentation
│   ├── QUICK_REFERENCE.md           # Quick lookup guide
│   ├── COMPLETION_REPORT.md         # Implementation status
│   └── speckit.md                   # Feature development guide
├── specs/                           # Feature specifications
│   ├── 001-skill-architecture/      # Initial design
│   └── 002-copilot-skills-restructure/ # Infrastructure upgrade
├── examples/                        # Community skill examples
│   ├── anthropics-skills/
│   ├── obra-superpowers/
│   ├── superpowers-skills/
│   └── tfriedel-claude-office-skills/
├── tests/                           # Test infrastructure
│   └── copilot-skills/
└── .github/                         # The skills system (see structure above)
    ├── copilot-instructions.md
    ├── copilot-skills/
    └── prompts/
```

---

## Success Metrics

- ✅ Developers identify and load the correct skill in <2 minutes
- ✅ Each SKILL.md scannable in <3 minutes
- ✅ Progressive disclosure reduces context usage by 60% vs. monolithic approach
- ✅ 95% of common task scenarios handled by loading ≤2 skills
- ✅ New skills can be authored in <30 minutes with templates

---

## Next Steps

1. **Explore the example skill**: Type `/skill-hello-skill` to see how skills work
2. **Browse the catalog**: Check `.github/copilot-skills/index.md`
3. **Read the principles**: See `.specify/memory/constitution.md`
4. **Study examples**: Explore `examples/anthropics-skills/`
5. **Create your first skill**: Type `/skills.create` and follow prompts

---

## Resources

- **Architecture Documentation**: [`copilot-skills.md`](./copilot-skills.md)
- **Skill Authoring Guide**: [`.github/copilot-skills/AUTHORING.md`](./.github/copilot-skills/AUTHORING.md)
- **Constitutional Principles**: [`.specify/memory/constitution.md`](./.specify/memory/constitution.md)
- **Feature Specifications**: [`specs/001-skill-architecture/`](./specs/001-skill-architecture/)
- **Quick Reference**: [`docs/QUICK_REFERENCE.md`](./docs/QUICK_REFERENCE.md)

---

## Contributing

Skills are designed to be shared across teams and repositories. To contribute:

1. Create a skill following the templates in `.github/copilot-skills/templates/`
2. Validate against the constitution (5 principles)
3. Test with `/skills.validate {skill-name}`
4. Submit a PR with both the skill files and prompt file
5. Include examples and bundled scripts for deterministic operations

---

## License

This repository structure and documentation is provided as a reference implementation. Individual skills in `examples/` retain their original licenses. See respective LICENSE files.

---

**Questions?** Check [`.github/copilot-skills/TROUBLESHOOTING.md`](./.github/copilot-skills/TROUBLESHOOTING.md) or review the feature specifications in [`specs/`](./specs/).
