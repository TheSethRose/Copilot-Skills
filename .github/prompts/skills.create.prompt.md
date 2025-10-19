---
name: Create Skill
description: Interactive wizard to create a new skill with guided workflow
---

# Create New Skill

This command guides you through creating a new skill using the interactive creation wizard.

## User Input

```text
$ARGUMENTS
```

## Instructions

1. **Parse user input** for skill name and optional description:
   - If user provides "Skill Name" - use as skill name, prompt for description
   - If user provides "skill-name: Description" - use both
   - If no input - prompt for both interactively

2. **Invoke create-skill.sh script**:
   ```bash
   .github/copilot-skills/scripts/bash/create-skill.sh \
     --name "$SKILL_NAME" \
     --description "$DESCRIPTION" \
     --interactive
   ```

3. **Handle script output**:
   - If script exits with 0: Report success with path to created skill
   - If script exits with non-zero: Report error message from script
   - Display next steps: how to add detail files, bundled scripts

4. **Validation**:
   - Script will automatically validate the created skill
   - If validation fails, suggest fixes based on error messages

## Examples

### Example 1: With name only
```
User: /skills.create "PDF Handling"
→ Prompts for: description, tags, dependencies
→ Creates: .github/copilot-skills/pdf-handling/SKILL.md
→ Updates: .github/copilot-skills/index.md
```

### Example 2: With full description
```
User: /skills.create "Database Migration: Generate type-safe migrations for Prisma"
→ Prompts for: tags, dependencies
→ Creates skill with provided name and description
```

### Example 3: Fully interactive
```
User: /skills.create
→ Prompts for: name, description, tags, dependencies
→ Creates complete skill
```

## Script Behavior

The `create-skill.sh` script will:
1. Validate skill name format (lowercase-with-dashes)
2. Check if skill already exists (error if duplicate)
3. Prompt for metadata (if --interactive flag set)
4. Load SKILL.template.md and substitute placeholders
5. Create directory structure (.github/copilot-skills/{skill-name}/)
6. Write SKILL.md with YAML frontmatter
7. Create scripts/ subdirectory
8. Update index.md with new skill entry
9. Run validate-skill.sh for compliance check
10. Output success message with next steps

## Success Output

When successful, display:
```
✅ Created skill: {Skill Name}
   Path: .github/copilot-skills/{skill-name}/SKILL.md
   
Next steps:
1. Edit SKILL.md to add detailed capabilities
2. Create bundled scripts in {skill-name}/scripts/
3. Add detail files for progressive disclosure
4. Run /skills.validate {skill-name} to verify compliance
```

## Error Handling

If creation fails:
- Show specific error message from script
- Suggest remediation steps
- Offer to retry with corrected input

## Notes

- Skill names must be lowercase-with-dashes (e.g., "pdf-handling")
- Human-readable names in frontmatter can have spaces (e.g., "PDF Handling")
- Script automatically converts names to correct format
- All created skills are validated against constitution before completion
