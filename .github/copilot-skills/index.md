# Copilot Skills Registry

> Discover available skills for this workspace. Each skill provides specialized capabilities that you can reference in your development workflow.

## How to Use This Registry

1. **Scan the registry below** to find skills relevant to your task
2. **Click the skill path** to open the SKILL.md file
3. **Read the core capabilities** in SKILL.md (takes ~3 minutes)
4. **Link to detail files** when you need deeper information (forms.md, reference.md, patterns.md)
5. **Run bundled scripts** for deterministic operations documented in SKILL.md

---

## Available Skills

### Hello Skill
**Path**: `.github/copilot-skills/hello-skill/SKILL.md`
**Description**: Example skill demonstrating discovery, progressive loading, and bundled script patterns for the Copilot Skills Architecture.
**When to use**: Learning how the skills system works; reference for understanding the discovery workflow and progressive disclosure pattern.
**Tags**: `example`, `discovery`, `tutorial`

### Skill Template
**Path**: `.github/copilot-skills/skill-template/SKILL.md`
**Description**: Boilerplate template for creating new skills with YAML frontmatter, core capabilities, detail files, and bundled scripts.
**When to use**: Reference when creating new skills; copy SKILL.md template and customize for your domain.
**Tags**: `example`, `template`, `architecture`

---

## Skill Metadata Fields

Each skill registration includes:
- **Path**: Location of the SKILL.md file
- **Description**: One-sentence purpose (what developers can do with this skill)
- **When to use**: Specific task types or keywords that trigger this skill's relevance
- **Tags**: Search keywords for discovery

## Adding New Skills

When creating a new skill:
1. Create directory: `.github/copilot-skills/{skill-name}/`
2. Create SKILL.md with YAML frontmatter
3. Add entry to this registry
4. Run skill compliance checklist from `.specify/checklists/skill-compliance-checklist.md`

See [AUTHORING.md](./AUTHORING.md) for step-by-step guidance.

---

**Last Updated**: October 18, 2025  
**Registry Version**: 1.0.0
