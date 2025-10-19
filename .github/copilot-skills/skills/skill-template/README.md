# Skill Template System

---
name: "Skill Template"
description: "Reference implementation and examples for creating new Copilot Skills"
version: "1.0.0"
created: "2025-10-19"
tags: ["template", "reference", "examples", "meta"]
dependencies: []
---

This is a **reference skill** demonstrating the Copilot Skills Architecture.

## What This Directory Contains

- **`scripts/`** - Example bundled scripts showing proper patterns
  - `example-script.py` - Python utility template with argument parsing
  - `helper.sh` - Shell script template with error handling

## Skill Structure Pattern

Real skills in this architecture follow this structure:

```
.github/
├── copilot-skills/{skill-name}/
│   ├── scripts/              # Optional: bundled utilities
│   └── *.md                  # Optional: detail files (patterns.md, reference.md, etc.)
├── prompts/
│   └── {skill-name}.skill.prompt.md    # Primary skill definition
└── instructions/
    └── {skill-name}.instructions.md    # Auto-loaded context rules
```

## Three-Part System

### 1. Skill Prompt (`.github/prompts/{skill-name}.skill.prompt.md`)
- **Purpose**: Defines WHEN and HOW to use the skill
- **Contains**: Workflows, examples, progressive disclosure instructions
- **Enables**: `/skill-{name}` slash command in Copilot
- **Template**: `.github/copilot-skills/templates/skill-prompt.template.md`

### 2. Instructions File (`.github/instructions/{skill-name}.instructions.md`)
- **Purpose**: Auto-loaded context for file patterns or keywords
- **Contains**: Default behaviors, quality guidelines, common workflows
- **Triggers**: File glob patterns or keyword mentions
- **Template**: `.github/copilot-skills/templates/instructions.template.md`

### 3. Skill Directory (`.github/copilot-skills/{skill-name}/`)
- **Purpose**: Store bundled scripts and detail files
- **Contains**: 
  - `scripts/` - Executable utilities (optional)
  - `patterns.md` - Usage patterns (optional)
  - `reference.md` - Deep technical reference (optional)
  - Other domain-specific detail files

## Example Skills

### Minimal Skill (git-ops)
```
.github/
├── copilot-skills/git-ops/
│   └── scripts/                    # Only scripts, no detail files
├── prompts/git-ops.skill.prompt.md
└── instructions/git-ops.instructions.md
```

### Rich Skill (pdf-handling)
```
.github/
├── copilot-skills/pdf-handling/
│   ├── forms.md                    # Detail file: form patterns
│   ├── reference.md                # Detail file: API reference
│   └── scripts/
├── prompts/pdf-handling.skill.prompt.md
└── instructions/pdf-handling.instructions.md
```

## Bundled Scripts

This template includes example scripts demonstrating best practices:

### Python Script Example
```bash
python .github/copilot-skills/skill-template/scripts/example-script.py --input "value"
```

**Demonstrates**:
- Argument parsing with `argparse`
- Validation and error handling
- JSON output format
- Helpful usage documentation

### Shell Script Example
```bash
bash .github/copilot-skills/skill-template/scripts/helper.sh "argument"
```

**Demonstrates**:
- Parameter validation
- Error handling with exit codes
- Structured output
- Usage documentation

## Creating a New Skill

### Step 1: Use Templates
```bash
# Copy skill prompt template
cp .github/copilot-skills/templates/skill-prompt.template.md \
   .github/prompts/my-skill.skill.prompt.md

# Copy instructions template
cp .github/copilot-skills/templates/instructions.template.md \
   .github/instructions/my-skill.instructions.md
```

### Step 2: Create Skill Directory (if needed)
```bash
# Only if you need bundled scripts or detail files
mkdir -p .github/copilot-skills/my-skill/scripts
```

### Step 3: Fill in Templates
1. Edit `.github/prompts/my-skill.skill.prompt.md`
   - Define WHEN to use the skill
   - Define HOW to use it step-by-step
   - Add examples and workflows

2. Edit `.github/instructions/my-skill.instructions.md`
   - Set `applyTo` glob pattern for auto-loading
   - List trigger keywords
   - Define default behaviors and quality guidelines

3. Add bundled scripts (optional)
   - Use script templates as starting point
   - Output to terminal only (no file generation)
   - Document usage in prompt file

### Step 4: Register Skill
Add entry to keyword routing map in `.github/copilot-instructions.md`:
```markdown
#### My Skill
**Keywords:** keyword1, keyword2, phrase example
**Suggest:** `/my-skill`
**Auto-context:** `.github/instructions/my-skill.instructions.md`
**Skill:** `.github/prompts/my-skill.skill.prompt.md`
```

## Five Constitutional Principles

All skills must follow these principles (see `.specify/memory/constitution.md`):

1. **Progressive Disclosure** - Load core first, details on demand
2. **File-Based Organization** - Skills are prompt + instructions + bundled scripts
3. **Dynamic Discovery** - Keyword routing map enables AI to find skills
4. **Deterministic Execution** - Scripts produce consistent terminal output
5. **Composability** - Skills reference each other with clear boundaries

## Script Guidelines

### Output Requirements
- **Terminal output only** - No file generation
- **Structured format** - JSON when applicable
- **Deterministic** - Same input = same output
- **Documented** - Usage in prompt file

### Error Handling
- Validate inputs before processing
- Provide helpful error messages
- Use appropriate exit codes
- Handle edge cases gracefully

### Examples
See scripts in this directory:
- `scripts/example-script.py` - Python patterns
- `scripts/helper.sh` - Shell patterns

## Related Templates

- **Skill Prompt**: `.github/copilot-skills/templates/skill-prompt.template.md`
- **Instructions**: `.github/copilot-skills/templates/instructions.template.md`
- **Detail File**: `.github/copilot-skills/templates/detail-file.template.md`
- **Python Script**: `.github/copilot-skills/templates/script.template.py`
- **Shell Script**: `.github/copilot-skills/templates/script.template.sh`

---

**Version**: 1.0.0 | **Last Updated**: October 19, 2025
