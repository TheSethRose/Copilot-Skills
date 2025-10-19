# Key Insight: Why .specify/ Works

## The Discovery

The `.specify/` system is discoverable and usable because it has **prompt files** that appear in GitHub Copilot's chat palette.

When a user types `/spec` in Copilot Chat, they see:
- `/speckit.specify`
- `/speckit.plan`
- `/speckit.tasks`
- `/speckit.implement`
- `/speckit.analyze`
- etc.

These prompts are defined in `.github/prompts/speckit.*.prompt.md` files.

## Why `.github/copilot-skills/` Doesn't Work

Current state:
- ✅ Documentation exists (AUTHORING.md, GOVERNANCE.md, README.md)
- ✅ Examples exist (hello-skill, skill-template)
- ✅ Scripts folder exists but is empty
- ❌ **NO PROMPTS** - Copilot can't discover the system
- ❌ No way to invoke `/skills.create` or `/skills.validate`
- ❌ Users must manually read docs and create files

## The Solution

Add prompt files that mirror the speckit pattern:

```
.github/prompts/
├── speckit.*.prompt.md     # Existing - feature development
└── skills.*.prompt.md      # NEW - skill management
```

Each `skills.*.prompt.md` file:
1. Tells Copilot WHAT to do (instructions)
2. Invokes scripts in `.github/copilot-skills/scripts/` (automation)
3. Validates output against constitution (quality)
4. Guides user through interactive workflow (UX)

## Architecture Pattern

```
User types: /skills.create "PDF Handling"
     ↓
Copilot reads: .github/prompts/skills.create.prompt.md
     ↓
Prompt instructs: Run .github/copilot-skills/scripts/bash/create-skill.sh
     ↓
Script generates: .github/copilot-skills/pdf-handling/SKILL.md
     ↓
Script updates: .github/copilot-skills/index.md (register new skill)
     ↓
Copilot reports: "Created skill at .github/copilot-skills/pdf-handling/"
```

## Why This Matters

Without prompts:
- System is documentation-only
- Requires manual file creation
- No discoverability
- High friction

With prompts:
- System is executable
- Automated workflows
- Discoverable via `/skills` prefix
- Zero friction

**This is the missing piece that makes `.specify/` work.**
