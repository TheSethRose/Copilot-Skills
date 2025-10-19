---
description: {{SKILL_DESCRIPTION}}
---

# {{SKILL_NAME}}

{{OVERVIEW_OF_WHAT_THIS_SKILL_DOES}}

## When to Use This Skill

{{LIST_OF_SCENARIOS_WHEN_THIS_SKILL_IS_RELEVANT}}

## How to Load This Skill

When this skill is relevant, follow these steps:

1. **Read the core skill file**: `.github/copilot-skills/{{SKILL_DIR_NAME}}/SKILL.md`
   - This contains the Overview, Core Capabilities, Quick Start
   - Use this for general understanding and basic usage

2. **For {{DETAIL_TOPIC_1}}**: Read `.github/copilot-skills/{{SKILL_DIR_NAME}}/{{DETAIL_FILE_1}}.md`
   - {{WHEN_TO_USE_THIS_DETAIL_FILE}}

3. **For {{DETAIL_TOPIC_2}}**: Read `.github/copilot-skills/{{SKILL_DIR_NAME}}/{{DETAIL_FILE_2}}.md`
   - {{WHEN_TO_USE_THIS_DETAIL_FILE}}

## Progressive Disclosure

Follow the **progressive disclosure** pattern:

1. **First mention**: Load only SKILL.md (core file)
2. **User asks for {{DETAIL_TOPIC_1}}**: Load {{DETAIL_FILE_1}}.md
3. **User asks for {{DETAIL_TOPIC_2}}**: Load {{DETAIL_FILE_2}}.md
4. **User wants to run scripts**: Reference scripts in `{{SKILL_DIR_NAME}}/scripts/`

**Do not load all files at once** - this defeats the purpose of progressive disclosure.

## Bundled Scripts

{{IF_HAS_SCRIPTS}}
The {{SKILL_DIR_NAME}} skill includes scripts in `.github/copilot-skills/{{SKILL_DIR_NAME}}/scripts/`:
{{LIST_SCRIPTS_WITH_DESCRIPTIONS}}

When user wants to run scripts:
1. Read the SKILL.md section on bundled scripts
2. Show the script invocation command
3. Explain the script's purpose and expected output
{{END_IF}}

## Example Usage

### User asks: "{{EXAMPLE_QUESTION_1}}"
1. Load: `.github/copilot-skills/{{SKILL_DIR_NAME}}/SKILL.md`
2. {{ACTION_TO_TAKE}}
3. {{FOLLOW_UP_ACTION}}

### User asks: "{{EXAMPLE_QUESTION_2}}"
1. Load: `.github/copilot-skills/{{SKILL_DIR_NAME}}/{{RELEVANT_DETAIL_FILE}}.md`
2. {{ACTION_TO_TAKE}}
3. {{FOLLOW_UP_ACTION}}

## Metadata

From SKILL.md frontmatter:
- **Name**: {{SKILL_NAME}}
- **Description**: {{DESCRIPTION}}
- **Tags**: {{TAGS_LIST}}
- **Dependencies**: {{DEPENDENCIES_LIST}}

## Integration with Copilot

This prompt enables:
- `/skill-{{SKILL_DIR_NAME}}` command to load the skill
- Automatic relevance detection (when user mentions keywords: {{RELEVANCE_KEYWORDS}})
- Progressive loading of detail files based on conversation context
- Reference to bundled scripts when execution is needed

## Notes

{{ADDITIONAL_NOTES_ABOUT_THIS_SKILL}}
