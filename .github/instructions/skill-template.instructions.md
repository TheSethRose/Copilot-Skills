---
description: "Auto-loaded context for skill creation and template usage"
applyTo: "**/{.github/copilot-skills,templates,skill-template}/**"
---

# Skill Template - Automatic Context Instructions

**Related Prompt:** `/skill-template`  
**Related Skill:** `.github/copilot-skills/skill-template/`

**Triggers:** create skill, new skill, skill template, skill architecture, skill structure, skill patterns

## Context: Skill Creation and Architecture

When working with skill-related files or when user queries contain skill creation keywords, this context is automatically activated.

## Core Principles

### Three-Part System
- **Prompt File** - Defines WHEN and HOW to use skill (`.github/prompts/`)
- **Instructions File** - Auto-loaded context rules (`.github/instructions/`)
- **Skill Directory** - Bundled scripts and detail files (`.github/copilot-skills/`)

### Five Constitutional Principles
- **Progressive Disclosure** - Load core first, details on demand
- **File-Based Organization** - Skills are discoverable files
- **Dynamic Discovery** - Index enables AI to find skills
- **Deterministic Execution** - Scripts produce consistent output
- **Composability** - Skills reference each other clearly

## Default Behaviors

### When user mentions "create skill" or "new skill"
1. Suggest `/skill-template` skill prompt
2. Guide through template copying process
3. Validate structure follows constitutional principles
4. Help register in keyword routing map

### When user mentions "skill architecture" or "skill patterns"
1. Suggest `/skill-template` skill prompt
2. Load `.github/copilot-skills/skill-template/README.md` for overview
3. Reference existing skills as examples (git-ops, pdf-handling)

### When user asks about "bundled scripts" or "script templates"
1. Suggest `/skill-template` skill prompt
2. Show example scripts in `.github/copilot-skills/skill-template/scripts/`
3. Reference script templates in `.github/copilot-skills/templates/`

## Quality Guidelines

### ✅ Do
- Use templates from `.github/copilot-skills/templates/`
- Follow three-part system (prompt + instructions + directory)
- Validate against five constitutional principles
- Register new skills in keyword routing map (`.github/copilot-instructions.md`)
- Use progressive disclosure (load on-demand, not all at once)
- Make scripts deterministic (terminal output only)
- Document trigger keywords in instructions file
- Cross-reference related skills

### ❌ Don't
- Create skills without using template system
- Bundle all content in single file
- Generate files from scripts (terminal output only)
- Skip registration in keyword routing map
- Ignore progressive disclosure pattern
- Create circular dependencies between skills
- Forget to set `applyTo` pattern in instructions

## Skill Structure Template

```
.github/
├── copilot-skills/{skill-name}/
│   ├── scripts/              # Optional: bundled utilities
│   │   ├── script1.py
│   │   └── script2.sh
│   ├── patterns.md           # Optional: usage patterns detail file
│   ├── reference.md          # Optional: API reference detail file
│   └── {other}.md            # Optional: domain-specific details
├── prompts/
│   └── {skill-name}.skill.prompt.md    # Primary skill definition
└── instructions/
    └── {skill-name}.instructions.md    # Auto-loaded context
```

## Common Workflows

### Create New Skill from Templates
```bash
# Copy prompt template
cp .github/copilot-skills/templates/skill-prompt.template.md \
   .github/prompts/my-skill.skill.prompt.md

# Copy instructions template
cp .github/copilot-skills/templates/instructions.template.md \
   .github/instructions/my-skill.instructions.md

# Create skill directory (if needed)
mkdir -p .github/copilot-skills/my-skill/scripts

# Edit templates with skill-specific content
# Register in keyword routing map (.github/copilot-instructions.md)
```

### Create Bundled Script
```bash
# Copy script template
cp .github/copilot-skills/templates/script.template.py \
   .github/copilot-skills/my-skill/scripts/my-script.py

# Or for shell script
cp .github/copilot-skills/templates/script.template.sh \
   .github/copilot-skills/my-skill/scripts/my-script.sh

# Make executable
chmod +x .github/copilot-skills/my-skill/scripts/my-script.sh

# Document in prompt file YAML frontmatter and usage section
```

### Validate Skill Structure
```bash
# Check files exist
ls .github/prompts/my-skill.skill.prompt.md
ls .github/instructions/my-skill.instructions.md
ls .github/copilot-skills/my-skill/

# Check registration in keyword routing map
grep "my-skill" .github/copilot-instructions.md

# Test skill command
# Use /skill-my-skill in Copilot chat
```

## Bundled Scripts

The skill-template provides example scripts:

```bash
# Python example script
python .github/copilot-skills/skill-template/scripts/example-script.py --input "value"

# Shell example script
bash .github/copilot-skills/skill-template/scripts/helper.sh "argument"
```

## Next Steps

When creating skills:
1. Use `/skill-template` prompt for guided creation
2. Check `.github/copilot-skills/skill-template/README.md` for structure details
3. Reference `.github/copilot-skills/templates/` for all available templates
4. Review `.specify/memory/constitution.md` for constitutional principles
5. Look at existing skills (git-ops, pdf-handling) as examples
6. Register in keyword routing map (`.github/copilot-instructions.md`)

## Related Skills

- **generate-copilot-instructions** - For analyzing codebases and creating instructions
- **git-ops** - Example minimal skill with scripts only
- **pdf-handling** - Example rich skill with detail files
