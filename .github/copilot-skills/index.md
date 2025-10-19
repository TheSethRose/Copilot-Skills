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

### PDF Document Handling
**Path**: `.github/copilot-skills/pdf-handling/SKILL.md`
**Description**: Extract text and tables, create new PDFs, merge/split documents, handle forms programmatically.
**When to use**: PDF parsing, form extraction, table extraction, document generation, form filling (government forms, applications), text extraction, PDF manipulation, watermarks, password protection.
**Tags**: `documents`, `pdf`, `forms`, `text-extraction`, `tables`, `reportlab`, `pypdf`, `pdfplumber`
**Detail Files**: `forms.md` (form filling), `reference.md` (advanced API)
**Scripts**: `extract_form_field_info.py`, `fill_fillable_fields.py`, `convert_pdf_to_images.py`, `check_bounding_boxes.py`

### Git Operations Assistant
**Path**: `.github/copilot-skills/git-ops/SKILL.md`
**Description**: Safely perform git operations including commits, branches, merges, and GitHub remote interactions.
**When to use**: Git operations, version control, branching, merging, rebasing, conflict resolution, GitHub PR creation, commit management, repository recovery, git safety, force push, history rewriting.
**Tags**: `git`, `github`, `version-control`, `repository`, `safety`, `merge`, `rebase`, `conflict-resolution`
**Detail Files**: `safety.md` (safety guidelines and best practices)
**Scripts**: `git_safe_exec.sh`, `commit_helper.sh`, `conflict_resolver.sh`

### Copilot Instructions Generator
**Path**: `.github/copilot-skills/copilot-instructions-generator/SKILL.md`
**Description**: Analyze codebases and generate or update .github/copilot-instructions.md files for AI agent guidance.
**When to use**: Creating AI instruction files, updating instructions after architecture changes, discovering undocumented patterns, consolidating multiple AI convention files, analyzing project structure, generating onboarding documentation.
**Tags**: `copilot`, `instructions`, `analysis`, `ai-agents`, `codebase`, `documentation`, `patterns`, `discovery`
**Detail Files**: `analysis.md` (detection algorithms), `config.md` (configuration guide), `patterns.md` (pattern examples)
**Scripts**: `analyze_repo.sh`, `discover_conventions.sh`, `validate_instructions.sh`

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
