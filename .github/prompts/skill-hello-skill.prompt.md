---
description: Load and apply the Hello Skill for demonstration and learning purposes
---

# Hello Skill

This skill demonstrates the skills architecture with a simple example. Use this as a reference when creating new skills.

## When to Use This Skill

- User asks about how skills work
- User wants to see an example skill
- User is learning the skills system
- User needs a template for creating new skills

## How to Load This Skill

When this skill is relevant, follow these steps:

1. **Read the core skill file**: `.github/copilot-skills/hello-skill/SKILL.md`
   - This contains the Overview, Core Capabilities, Quick Start
   - Use this for general understanding and basic usage

2. **For specific patterns**: Read `.github/copilot-skills/hello-skill/patterns.md`
   - This contains detailed pattern examples
   - Use when user needs specific implementation patterns

3. **For API reference**: Read `.github/copilot-skills/hello-skill/reference.md`
   - This contains detailed API documentation
   - Use when user needs specific function signatures or parameters

## Progressive Disclosure

Follow the **progressive disclosure** pattern:

1. **First mention**: Load only SKILL.md (core file)
2. **User asks for patterns**: Load patterns.md (detail file)
3. **User asks for API details**: Load reference.md (detail file)
4. **User wants to run scripts**: Reference scripts in `hello-skill/scripts/`

**Do not load all files at once** - this defeats the purpose of progressive disclosure.

## Bundled Scripts

The hello-skill includes example scripts in `.github/copilot-skills/hello-skill/scripts/`:
- `hello-example.py` - Demonstrates a bundled script pattern

When user wants to run scripts:
1. Read the SKILL.md section on bundled scripts
2. Show the script invocation command
3. Explain the script's purpose and output

## Example Usage

### User asks: "Show me how skills work"
1. Load: `.github/copilot-skills/hello-skill/SKILL.md`
2. Explain: The 5 constitutional principles
3. Demonstrate: Progressive disclosure with this skill

### User asks: "What patterns does hello-skill demonstrate?"
1. Load: `.github/copilot-skills/hello-skill/patterns.md`
2. Show: Specific pattern examples from the file
3. Explain: When to use each pattern

### User asks: "What's the API for hello-skill?"
1. Load: `.github/copilot-skills/hello-skill/reference.md`
2. Show: Function signatures and parameters
3. Provide: Code examples from reference

## Metadata

From SKILL.md frontmatter:
- **Name**: Hello Skill
- **Description**: A demonstration skill showing the architecture
- **Tags**: example, demo, learning
- **Dependencies**: None (pure demonstration)

## Integration with Copilot

This prompt enables:
- `/skill-hello-skill` command to load the skill
- Automatic relevance detection (when user mentions "hello skill" or "skill example")
- Progressive loading of detail files based on conversation context
- Reference to bundled scripts when execution is needed

## Notes

- This skill is intentionally simple for demonstration
- Use it as a template when creating new skills
- The 3-file structure (SKILL.md + 2 detail files) is the recommended pattern
- Bundled scripts show how to provide deterministic execution
