---
description: Guided workflow for creating high-quality, constitutional-compliant Copilot Skills
---

# Create Skill

**Slash Command**: `/create-skill`  
**Chatmode**: `/switch Skill Creator`  
**Detailed Guide**: `.github/instructions/create-skill.instructions.md`

## When to Use This Skill

- 🆕 Build a new skill from scratch
- 📐 Design skill architecture
- ✅ Validate constitutional compliance
- 🔄 Refactor documentation into a skill
- 🧪 Test skill patterns

## Quick Start

Run `/create-skill` to begin. You'll be guided through 5 phases:

1. **📋 Discovery** - Answer questions about your skill's purpose
2. **🏗️ Design** - Get architectural recommendations
3. **✅ Validation** - Verify all 5 constitutional principles
4. **⚙️ Implementation** - Generate all required files
5. **🔗 Integration** - Register and test the skill

## The 5 Constitutional Principles

Every skill MUST satisfy all 5:

### 1. Progressive Disclosure
- Metadata → core workflow → optional details
- Workflow scannable in <3 minutes
- Detail files optional, not required

### 2. File-Based Organization
- Prompt: `.github/prompts/{name}.prompt.md`
- Instructions: `.github/instructions/{name}.instructions.md`
- Optional directory: `.github/copilot-skills/{name}/`

### 3. Dynamic Discovery
- Keywords enable AI to find skills
- Entry in keyword routing map
- File patterns for auto-loading

### 4. Deterministic Execution
- Scripts output to terminal only (no file generation)
- Consistent, parseable output
- Error handling with exit codes
- Help documentation included

### 5. Composability
- Clear scope and boundaries
- Explicit dependencies
- No overlapping functionality
- Referenced skills are explicit

## Discovery Questions

You'll be asked:

1. **Intent**: What problem does this skill solve?
2. **Scope**: What's in-scope vs out-of-scope?
3. **Users**: Who will use this?
4. **Triggers**: How should this be discovered?
5. **Frequency**: How often will it be used?
6. **Complexity**: Simple or complex workflows?

## Skill Archetypes

**Minimal** (git-ops, cleanup)
- 2 files, 0 scripts, ~30 min
- Simple, single-purpose

**Domain Knowledge** (pdf-handling)
- 5-10 files, 2-5 scripts, ~1-2 hours
- Complex domain with automation

**Rich Reference** (mcp-builder)
- 15+ files, 5+ scripts, ~2-3 hours
- Deep technical domain

**Meta** (create-skill)
- 20+ files, validation scripts, ~3+ hours
- Operating on skills system

## File Locations

```
.github/
├── prompts/{skill-name}.prompt.md
├── instructions/{skill-name}.instructions.md
└── copilot-skills/{skill-name}/
    ├── README.md
    ├── scripts/
    ├── patterns.md (optional)
    └── reference.md (optional)
```

## Naming Conventions

- Skill names: `kebab-case` (lowercase with hyphens)
- Slash commands: `/skill-name`
- Chat modes: "Title Case"

Example: `database-migrations.prompt.md` → `/database-migrations`

## Quality Checklist

**Documentation** ✓
- YAML frontmatter complete
- Use cases concrete
- Workflows numbered and actionable
- Examples use real file paths

**Code** ✓
- Scripts have error handling
- Scripts have help documentation
- Scripts output to terminal only
- Input validation

**Integration** ✓
- Keyword routing map updated
- YAML metadata valid
- File paths correct
- No conflicts with existing skills

**Testing** ✓
- All workflows tested end-to-end
- Scripts run without errors
- Triggers work correctly
- Examples accurate

**Constitutional** ✓
- All 5 principles satisfied
- Files in correct locations
- No duplicate functionality
- Clear dependencies

## Getting Started

1. Type: `/create-skill`
2. Answer discovery questions
3. Follow the guided phases
4. Review generated files
5. Test workflows
6. Commit to Git

## More Information

See `.github/instructions/create-skill.instructions.md` for comprehensive guidelines including:
- Detailed file format specifications
- VS Code YAML requirements
- Testing procedures
- Script design patterns
- Conventional commit formats

---

**Ready?** Start with `/create-skill` and we'll guide you through creating a skill that serves your team for years.
