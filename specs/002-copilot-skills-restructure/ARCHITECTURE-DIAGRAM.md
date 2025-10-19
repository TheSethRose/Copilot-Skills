# Architecture Diagram: How Prompts Enable Skills

## Current State (Doesn't Work)

```
Developer
    ↓
  Reads documentation
    ↓
  Manually creates files
    ↓
  Manually updates index.md
    ↓
  Manually validates against constitution
    ↓
  High friction, error-prone
```

## Target State (With Prompts)

```
Developer types: /skills.create "PDF Handling"
         ↓
GitHub Copilot reads: .github/prompts/skills.create.prompt.md
         ↓
Prompt contains:
  - Instructions for AI agent
  - Script to invoke: .github/copilot-skills/scripts/bash/create-skill.sh
  - Validation rules
  - User interaction flow
         ↓
Script executes:
  1. Prompt for metadata (description, tags, dependencies)
  2. Generate directory: .github/copilot-skills/pdf-handling/
  3. Create SKILL.md with frontmatter from template
  4. Create scripts/ subdirectory
  5. Update index.md with new skill entry
  6. Run validate-skill.sh for constitution check
  7. Run update-agent-context.sh to register with Copilot
         ↓
Copilot reports: "Created PDF Handling skill at .github/copilot-skills/pdf-handling/"
         ↓
Developer: Zero friction, fully automated, constitution-compliant ✅
```

## Prompt-to-Script Flow

```
┌─────────────────────────────────────────────────────────────┐
│ User: /skills.create "PDF Handling"                         │
└─────────────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────────┐
│ Copilot reads: .github/prompts/skills.create.prompt.md      │
│                                                               │
│ ---                                                           │
│ name: Create Skill                                            │
│ description: Interactive skill creation wizard                │
│ ---                                                           │
│                                                               │
│ # Instructions                                                │
│ 1. Parse user input for skill name and description           │
│ 2. Invoke create-skill.sh with parameters                    │
│ 3. Validate output against constitution                      │
│ 4. Report success or errors to user                          │
│                                                               │
│ # Script Invocation                                           │
│ .github/copilot-skills/scripts/bash/create-skill.sh \        │
│   --name "$SKILL_NAME" \                                      │
│   --description "$DESCRIPTION" \                              │
│   --interactive                                               │
└─────────────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────────┐
│ Script: create-skill.sh                                       │
│                                                               │
│ 1. Source common.sh (logging, YAML helpers)                  │
│ 2. Validate skill name (no spaces, lowercase-with-dashes)    │
│ 3. Check if skill already exists                             │
│ 4. Prompt for metadata (if --interactive)                    │
│ 5. Load SKILL.template.md                                    │
│ 6. Replace {{placeholders}} with actual values               │
│ 7. Create directory structure                                │
│ 8. Write SKILL.md with frontmatter                           │
│ 9. Update index.md with new entry                            │
│ 10. Run validate-skill.sh for sanity check                   │
│ 11. Run update-agent-context.sh to register                  │
│ 12. Output JSON: {"status": "success", "path": "..."}        │
└─────────────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────────┐
│ Copilot interprets JSON output                               │
│                                                               │
│ If success:                                                   │
│   "✅ Created PDF Handling skill at                          │
│    .github/copilot-skills/pdf-handling/SKILL.md"             │
│                                                               │
│ If error:                                                     │
│   "❌ Failed to create skill: [error message]"               │
│   "Suggestions: [remediation steps]"                          │
└─────────────────────────────────────────────────────────────┘
```

## Why This Pattern Works

1. **Discoverability**: Prompts appear in `/skills` autocomplete
2. **Automation**: Scripts handle repetitive tasks
3. **Validation**: Constitution checking built-in
4. **Consistency**: Templates ensure uniform structure
5. **Zero friction**: One command replaces 10+ manual steps
6. **Error handling**: Scripts catch problems early
7. **Integration**: Agent context automatically updated

## Comparison with .specify/

| Feature | .specify/ | .github/copilot-skills/ (after) |
|---------|-----------|----------------------------------|
| Prompts | ✅ /speckit.* | ✅ /skills.* |
| Scripts | ✅ .specify/scripts/bash/ | ✅ .github/copilot-skills/scripts/bash/ |
| Templates | ✅ .specify/templates/ | ✅ .github/copilot-skills/templates/ |
| Validation | ✅ Constitution checking | ✅ Constitution checking |
| Agent context | ✅ Auto-update | ✅ Auto-update |
| Testing | ✅ bats tests | ✅ bats tests |

**Both systems follow the same proven pattern** 🎯
