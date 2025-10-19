# Skill Template Assistant

---
name: "Skill Template Assistant"
description: "Guide for creating new Copilot Skills using templates and best practices"
version: "1.0.0"
created: "2025-10-19"
tags: ["template", "meta", "skill-creation", "examples"]
dependencies: []
scripts:
  - ".github/copilot-skills/skill-template/scripts/example-script.py"
  - ".github/copilot-skills/skill-template/scripts/helper.sh"
---

This command helps you create new Copilot Skills using the three-part architecture system.

## When to Use This Skill

- Creating a new skill from templates
- Understanding the skill architecture patterns
- Learning how to structure bundled scripts
- Reviewing example implementations
- Validating skill structure follows constitutional principles

## User Input

```text
$ARGUMENTS
```

## Instructions

### Step 1: Understand What User Wants

Parse the user's request:
- **Create new skill**: Guide through template copying and customization
- **Understand architecture**: Load `.github/copilot-skills/skill-template/README.md`
- **See examples**: Reference existing skills (git-ops, pdf-handling)
- **Script patterns**: Show bundled script examples

### Step 2: Load Relevant Context

For creating new skills:
1. Read `.github/copilot-skills/skill-template/README.md` for structure overview
2. Reference `.github/copilot-skills/templates/` for available templates
3. Check `.specify/memory/constitution.md` for constitutional principles

For understanding patterns:
1. Show example from git-ops (minimal skill with scripts)
2. Show example from pdf-handling (rich skill with detail files)
3. Explain three-part system (prompt + instructions + directory)

### Step 3: Guide Skill Creation

If creating new skill, walk through:

#### A. Copy Templates
```bash
# Create prompt file
cp .github/copilot-skills/templates/skill-prompt.template.md \
   .github/prompts/{skill-name}.skill.prompt.md

# Create instructions file
cp .github/copilot-skills/templates/instructions.template.md \
   .github/instructions/{skill-name}.instructions.md
```

#### B. Create Directory (if needed)
```bash
# Only if bundled scripts or detail files are needed
mkdir -p .github/copilot-skills/{skill-name}/scripts
```

#### C. Customize Templates

**In prompt file** (`.github/prompts/{skill-name}.skill.prompt.md`):
- Fill in YAML frontmatter (name, description, tags, dependencies)
- Define "When to Use This Skill" scenarios
- Write step-by-step instructions for AI agent
- Add examples and workflows
- Document bundled scripts (if any)

**In instructions file** (`.github/instructions/{skill-name}.instructions.md`):
- Set `applyTo` glob pattern for auto-triggering
- List trigger keywords
- Define core principles and default behaviors
- Add quality guidelines (Do/Don't)
- Document common workflows
- Reference bundled scripts

#### D. Add Bundled Scripts (optional)

If skill needs executable tools:
1. Copy script templates from `.github/copilot-skills/templates/`
2. Implement script logic (terminal output only)
3. Document usage in prompt file
4. Add example invocations

#### E. Register in Index

### Step 4: Register Skill

Add entry to keyword routing map in `.github/copilot-instructions.md`:
```markdown
#### {Skill Name}
**Keywords:** {keyword1}, {keyword2}, {phrase example}
**Suggest:** `/{skill-name}`
**Auto-context:** `.github/instructions/{skill-name}.instructions.md`
**Skill:** `.github/prompts/{skill-name}.skill.prompt.md`
```

### Step 4: Validate Against Constitutional Principles

Check that the new skill follows all five principles:

1. **Progressive Disclosure**
   - ✅ Prompt file defines when/how to load detail files
   - ✅ Detail files are loaded on-demand, not all at once
   - ✅ Each layer is independently scannable

2. **File-Based Organization**
   - ✅ Skill has prompt file in `.github/prompts/`
   - ✅ Skill has instructions file in `.github/instructions/`
   - ✅ Bundled scripts (if any) in `.github/copilot-skills/{skill-name}/scripts/`

3. **Dynamic Discovery**
   - ✅ Registered in keyword routing map (`.github/copilot-instructions.md`)
   - ✅ Keywords/triggers defined for auto-suggestion
   - ✅ Related skills cross-referenced

4. **Deterministic Execution**
   - ✅ Scripts output to terminal only
   - ✅ Same input produces same output
   - ✅ No file generation from scripts

5. **Composability**
   - ✅ Dependencies listed in YAML frontmatter
   - ✅ Related skills documented
   - ✅ Clear boundaries and scope

### Step 5: Provide Next Steps

After skill creation:
1. Test the skill with `/skill-{name}` command
2. Verify auto-loading by editing files matching `applyTo` pattern
3. Run bundled scripts to ensure they work
4. Update `.github/copilot-instructions.md` if needed (add to keyword routing map)

## Example Skills Reference

### Minimal Skill: git-ops
- **Prompt**: `.github/prompts/git-ops.skill.prompt.md`
- **Instructions**: `.github/instructions/git-ops.instructions.md`
- **Scripts**: `.github/copilot-skills/git-ops/scripts/`
- **Pattern**: Workflow skill with bundled utilities

### Rich Skill: pdf-handling
- **Prompt**: `.github/prompts/pdf-handling.skill.prompt.md`
- **Instructions**: `.github/instructions/pdf-handling.instructions.md`
- **Detail Files**: 
  - `.github/copilot-skills/pdf-handling/forms.md`
  - `.github/copilot-skills/pdf-handling/reference.md`
- **Scripts**: `.github/copilot-skills/pdf-handling/scripts/`
- **Pattern**: Reference skill with multiple detail layers

## Bundled Script Patterns

### Python Script Template
```bash
python .github/copilot-skills/skill-template/scripts/example-script.py --input "value"
```

**Shows**:
- Argument parsing with `argparse`
- JSON output format
- Error handling
- Usage documentation

### Shell Script Template
```bash
bash .github/copilot-skills/skill-template/scripts/helper.sh "argument"
```

**Shows**:
- Parameter validation
- Exit codes
- Structured output
- Usage help

## Common Patterns

### Pattern 1: Workflow Skill
**Use when**: Skill guides user through multi-step processes
**Structure**: Prompt + Instructions + Scripts (optional)
**Example**: git-ops, cleanup

### Pattern 2: Reference Skill
**Use when**: Skill provides domain knowledge and API reference
**Structure**: Prompt + Instructions + Detail Files
**Example**: pdf-handling, copilot-instructions-generator

### Pattern 3: Utility Skill
**Use when**: Skill primarily provides executable tools
**Structure**: Prompt + Instructions + Scripts
**Example**: Skills with heavy automation

## Troubleshooting

### Skill not auto-loading
- Check `applyTo` pattern in instructions file
- Verify file being edited matches glob pattern
- Test with explicit `/skill-{name}` command first

### Scripts not executing
- Verify script is executable: `chmod +x script.sh`
- Check script path in prompt YAML frontmatter
- Test script independently in terminal

### Progressive disclosure not working
- Ensure prompt file defines when to load each detail file
- Check that detail files are referenced, not bundled in prompt
- Verify prompt instructs AI to load on-demand

## Metadata

From README.md frontmatter:
- **Name**: Skill Template
- **Description**: Reference implementation for creating new Copilot Skills
- **Tags**: template, reference, examples, meta
- **Dependencies**: None

## Integration with Copilot

This prompt enables:
- `/skill-template` command to access skill creation guidance
- Reference for developers creating new skills
- Examples of proper skill structure
- Validation against constitutional principles

## Notes

- This is a meta-skill about creating skills
- Not meant for end-user workflows
- Primarily for skill authors and maintainers
- Examples scripts are fully functional and demonstrate best practices
