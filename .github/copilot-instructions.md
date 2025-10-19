# Copilot Instructions

This repository is a Copilot Skills Architecture system — not a typical application. It provides a framework for organizing domain knowledge into discoverable, composable skills that keep AI agents focused and context-efficient.

## What is This Repository?

Purpose: Framework and examples for implementing the Copilot Skills Architecture in any GitHub repository.

Core Insight: LLMs excel at coding but struggle with organization. This system provides structured domain knowledge through progressive disclosure—loading information only when needed, keeping context lean.

## Three-Part Architecture

1. **Skill Prompts** (`.github/prompts/{skill-name}.skill.prompt.md`)
   - YAML frontmatter with metadata (name, description, version, tags, dependencies)
   - "When to Use This Skill" section describing use cases
   - Detailed instructions for AI agents on HOW to execute the skill
   - Examples, workflows, configuration, and troubleshooting
   - These are the canonical skill definitions used by `/skill-{name}` commands

2. **Skill Scripts** (`.github/copilot-skills/{skill-name}/scripts/`)
   - Bundled executable tools (bash, Python) for the skill
   - Self-contained and deterministic
   - Output to terminal only (no file generation)
   - Referenced by the skill prompt file

3. **Skills Registry** (`.github/copilot-skills/index.md`)
   - Searchable index of all available skills
   - Points to prompt files for discovery
   - Enables dynamic skill loading

## Five Constitutional Principles

All skills must follow these (see `.specify/memory/constitution.md`):

1. **Progressive Disclosure** - Information in skill prompt loads: metadata → use cases → instructions → examples
2. **File-Based Organization** - Skills are prompt files with YAML frontmatter + scripts directory
3. **Dynamic Discovery** - `.github/copilot-skills/index.md` registry enables AI to find skills
4. **Deterministic Execution** - Bundled scripts in `scripts/` produce consistent terminal output (no file generation)
5. **Composability** - Skills reference each other with explicit dependencies in frontmatter

## Current Skills

- Hello Skill - Example demonstrating architecture
- Skill Template - Boilerplate for new skills
- PDF Document Handling - Extract/create PDFs, forms, tables
- Git Operations Assistant - Safe git operations, branching, conflicts
- Copilot Instructions Generator - Analyze codebases, generate instructions

## Working with Skills

### Discover Skills
1. Check `.github/copilot-skills/index.md` for relevant skill
2. Click path to open `SKILL.md` (~3 min read)
3. Reference detail files for deeper knowledge
4. Run bundled scripts from `scripts/` directory

## Working with Skills

### Discover Skills
1. Check `.github/copilot-skills/index.md` for relevant skill
2. Index points to `.github/prompts/{skill-name}.skill.prompt.md`
3. Read skill prompt (~3-5 min) for full instructions
4. Run bundled scripts from `.github/copilot-skills/{skill-name}/scripts/`

### Create New Skill
```bash
# 1. Create scripts directory
mkdir -p .github/copilot-skills/{skill-name}/scripts

# 2. Create skill prompt with YAML frontmatter
# File: .github/prompts/{skill-name}.skill.prompt.md

# 3. Add bundled scripts in scripts/ directory

# 4. Register in .github/copilot-skills/index.md

# 5. Test the skill with real usage
```

## Key Files

- `.github/copilot-skills/index.md` - Skills registry (START HERE)
- `.github/prompts/{skill-name}.skill.prompt.md` - Skill definitions
- `.github/copilot-skills/{skill-name}/scripts/` - Bundled tools
- `.specify/memory/constitution.md` - Canonical principles
- `readme.md` - Project rationale and examples

## Code Patterns

### Skill Metadata (YAML frontmatter)
```yaml
---
name: "Skill Name"
description: "One-sentence purpose"
version: "1.0.0"
tags: ["keyword1", "keyword2"]
dependencies: ["tool1", "tool2"]
---
```

### Bundled Scripts
- Output to terminal only (no file generation)
- Self-contained and deterministic
- Clear error messages with exit codes
- Documented in SKILL.md with usage examples

### Progressive Disclosure
```
Index Entry (2 lines) → SKILL.md (~100 lines) → Detail Files (deep) → Scripts (executable)
```

## Best Practices

- Keep skills focused (one domain per skill)
- Layer information (metadata → core → details)
- Test bundled scripts output to terminal only
- Reference specific examples, not generic advice
- Validate new skills against constitutional principles
- Use semantic versioning for skill versions
- Declare all dependencies in YAML frontmatter

## This is NOT a Software Application

Do not treat this as a typical codebase:
- No "build", "run", or "deploy" commands for the repository itself
- Skills are documentation + scripts, not application code
- No test framework or CI/CD for the repository
- Purpose is to demonstrate reusable skill patterns
- Each skill may have scripts, but the repo doesn't "execute"

## Examples Directory

Third-party skill collections in `examples/`:
- `anthropics-skills/` - Anthropic's official agent skills
- `obra-superpowers/` - Advanced development workflows
- `superpowers-skills/` - Problem-solving patterns
- `tfriedel-claude-office-skills/` - Office document handling

These demonstrate different approaches and serve as reference implementations.
