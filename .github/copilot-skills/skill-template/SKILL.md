---
name: "{Skill Name}"
description: "{One-sentence purpose}"
version: "1.0.0"
created: "YYYY-MM-DD"
tags: ["keyword1", "keyword2", "keyword3"]
dependencies: ["tool1", "tool2"]
---

# {Skill Name}

**NOTE**: This is a template. The actual skill definition should be in `.github/prompts/{skill-name}.skill.prompt.md`.

This directory contains only:
- `scripts/` - Bundled executable tools for this skill

The skill prompt file (`.github/prompts/{skill-name}.skill.prompt.md`) should contain:
1. YAML frontmatter with metadata (name, description, version, tags, dependencies)
2. "When to Use This Skill" section
3. Detailed instructions for the AI agent
4. Examples and workflows
5. Configuration and troubleshooting

See existing skills for reference:
- `.github/prompts/generate-copilot-instructions.skill.prompt.md`
- `.github/prompts/git-ops.skill.prompt.md`
- `.github/prompts/pdf-handling.skill.prompt.md`

## Core Capabilities

- Demonstrate YAML frontmatter metadata format
- Show how to structure core capabilities sections
- Link to detail files for deeper information
- Reference bundled scripts for deterministic operations
- Explain progressive disclosure pattern

## Quick Start

### Reading This Skill

1. Start here with core capabilities (~2 minutes to read)
2. Navigate to linked detail files when you need specifics:
   - [patterns.md](./patterns.md) - Three pattern types explained
   - [reference.md](./reference.md) - Complete API reference (deep dive)

### Using Bundled Scripts

This skill includes example scripts to demonstrate script patterns:

```bash
# Run the Python example
python .github/copilot-skills/skill-template/scripts/example-script.py --input "value"

# Run the Shell example
bash .github/copilot-skills/skill-template/scripts/helper.sh "argument"
```

Both scripts demonstrate:
- Argument parsing and validation
- Consistent error handling
- Structured output format (JSON where applicable)
- Documentation of expected input/output

## Core Patterns

### Pattern 1: Reference Skill
When a skill focuses on providing reference material and guidance for a specific domain. Includes SKILL.md with patterns, YAML frontmatter, and linked reference files.

**Example**: PDF Handling skill - guides users through PDF operations, links to API reference and form patterns

### Pattern 2: Skill with Utilities
When a skill provides guidance plus utility scripts that perform deterministic operations. Includes SKILL.md + scripts/ with executable tools.

**Example**: Compliance Tracking skill - explains licensing logic, provides bundled scripts for status calculation

### Pattern 3: Complex Multi-Topic Skill
When a skill spans multiple related topics, each requiring detailed explanation. Uses layered detail files (forms.md, calculations.md, reference.md).

**Example**: Financial Reporting skill - combines templates, calculations, and API references for different report types

## Skill Metadata Explained

The YAML frontmatter at the top of this file contains:

| Field | Purpose | Example |
|-------|---------|---------|
| `name` | Display name of the skill | "PDF Handling" |
| `description` | One sentence: what developers can do | "Extract text, fill forms, and manipulate PDFs" |
| `version` | Semantic version (MAJOR.MINOR.PATCH) | "1.0.0" |
| `created` | Date skill was authored | "2025-10-18" |
| `tags` | Search keywords for discovery | ["documents", "pdf", "forms"] |
| `dependencies` | Required libraries or tools | ["pypdf2", "pdfplumber"] |

## Bundled Scripts

Scripts in the `scripts/` directory provide deterministic, reusable operations documented in SKILL.md.

**Location**: `.github/copilot-skills/{skill-name}/scripts/`

**Examples**:
- `example-script.py` - Python utility (see scripts/ directory)
- `helper.sh` - Shell utility (see scripts/ directory)

**Input/Output Contract**: Scripts should document:
- Expected arguments/flags
- Output format (JSON, plain text, etc.)
- Error handling and exit codes

## Detailed References

- For pattern examples and variations, see [patterns.md](./patterns.md)
- For complete API reference and technical details, see [reference.md](./reference.md)

## Error Handling

When using this template:
- Verify all referenced files exist (index.md, SKILL.md, patterns.md, reference.md)
- Check that bundled scripts are executable
- Validate YAML frontmatter syntax
- Test relative links work correctly

## Related Skills

This template skill is standalone but demonstrates patterns used across:
- Document processing skills (PDF, Excel, PowerPoint handling)
- Domain-specific skills (compliance tracking, financial reporting)
- Tool integration skills (database migrations, API interactions)

---

**Version**: 1.0.0 | **Last Updated**: October 18, 2025
