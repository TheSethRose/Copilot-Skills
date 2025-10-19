# Data Model: Copilot Skills Architecture

**Specification**: [spec.md](./spec.md)  
**Date**: October 18, 2025  
**Status**: Phase 1 Design Complete

## Entity Definitions

### 1. Skill

**Purpose**: Self-contained package of instructions, patterns, and scripts for a specialized domain

**Core Attributes**:
- `name` (string, kebab-case): Unique identifier, e.g., "pdf-handling", "compliance-tracking"
- `description` (string, <100 chars): One-sentence purpose and when to use
- `version` (semantic): Current skill version (MAJOR.MINOR.PATCH)
- `tags` (array of strings): Domain keywords for discovery, e.g., ["documents", "pdf", "forms"]
- `dependencies` (array of strings): Required tools, libraries, or other skills
- `path` (string): Location in `.github/copilot-skills/{skill-name}/`
- `created_date` (date): When skill was first authored
- `last_updated` (date): Most recent modification

**State**:
- DRAFT: Not yet reviewed or validated
- ACTIVE: In use, meets compliance requirements
- DEPRECATED: Replaced by newer version, migration guidance provided
- ARCHIVED: No longer maintained

**Validation Rules**:
- Name MUST be unique within project
- Description MUST be clear enough for AI agents to determine relevance
- Version MUST follow semantic versioning
- Dependencies MUST be declared and available
- Files MUST comply with constitution Principles I-V

**Relationships**:
- Has many: `DetailFile` (forms.md, reference.md, patterns.md)
- Has many: `ExecutableScript` (scripts/ directory contents)
- References many: Skill (for composability)
- Referenced by: SkillsRegistry (index.md entry)

**File Location**: `.github/copilot-skills/{skill-name}/SKILL.md`

**Example**:
```yaml
---
name: "pdf-handling"
description: "Extract text, fill forms, and manipulate PDF documents"
version: "1.0.0"
created: "2025-10-18"
tags: ["documents", "pdf", "forms"]
dependencies: ["pypdf2", "pdfplumber"]
---
```

---

### 2. Skills Registry

**Purpose**: Discoverable index of all available skills in the project workspace

**Core Attributes**:
- `skills` (array of SkillMetadata): All registered skills with lightweight metadata
- `last_updated` (date): When registry was last refreshed

**SkillMetadata (Registry Entry)**:
- `name` (string): Skill name
- `path` (string): Absolute path to SKILL.md
- `description` (string): Purpose of the skill
- `when_to_use` (string): Specific scenarios and keywords
- `tags` (array): Search keywords

**Validation Rules**:
- Registry MUST be scannable in under 3 minutes (max 50-70 skills per registry)
- All entries MUST have valid paths to existing SKILL.md files
- Descriptions MUST be distinct (no duplicate purposes)
- Registry MUST be updated when skills added/removed/modified

**Discovery Mechanism**:
1. User reads `.github/copilot-skills/index.md`
2. Scans entries for relevant skill
3. Opens referenced SKILL.md
4. Begins skill interaction

**Relationships**:
- Contains many: SkillMetadata entries
- References: Active, ACTIVE, and DEPRECATED skills only (exclude DRAFT, ARCHIVED)

**File Location**: `.github/copilot-skills/index.md`

**Example Format**:
```markdown
# Copilot Skills Registry

## PDF Handling
**Path**: `.github/copilot-skills/pdf-handling/SKILL.md`
**Description**: Extract text, fill forms, and manipulate PDF documents
**When to use**: PDF parsing, form extraction, document generation
```

---

### 3. Detail File

**Purpose**: Focused documentation for specific aspects of a skill

**Core Attributes**:
- `name` (string): Filename (e.g., forms.md, reference.md, patterns.md)
- `topic` (string): Specific subtopic covered
- `parent_skill` (string): Reference to parent Skill
- `content_length` (string): Estimated reading time/size

**Types**:
- **forms.md**: Form-filling specific instructions and patterns
- **reference.md**: API documentation, complete library reference
- **patterns.md**: Common usage patterns, examples, best practices
- **calculations.md**: Domain-specific calculations, formulas
- **templates.md**: Templates or starting points for common tasks
- **examples/**: Directory with runnable examples

**Validation Rules**:
- MUST be referenced from parent SKILL.md with markdown link
- MUST focus on single topic (avoid mixing patterns + reference)
- MUST be independently readable without reading other detail files
- MUST have clear section structure (headings, examples)

**Relationships**:
- Belongs to: One Skill
- References: Zero or more other DetailFiles or Skills
- Contains: Code examples, tables, diagrams

**File Location**: `.github/copilot-skills/{skill-name}/{topic}.md`

**Example Structure**:
```markdown
# PDF Form Handling

## Form Field Extraction
[Specific instructions...]

## Filling Forms Programmatically
[Patterns and examples...]

## Common Form Types
- IRS Tax Forms
- Government Applications
- Medical Forms
```

---

### 4. Executable Script

**Purpose**: Bundled, deterministic implementation of skill operations

**Core Attributes**:
- `name` (string): Script filename (e.g., extract_form_fields.py)
- `language` (string): Implementation language (Python, Shell, JavaScript, etc.)
- `purpose` (string): What this script does
- `input_contract` (object): Expected inputs, types, validation
- `output_contract` (object): Expected outputs, format (typically JSON)
- `parent_skill` (string): Skill this script belongs to
- `documentation_ref` (string): Reference in parent SKILL.md

**Input Contract**:
- Arguments: Command-line arguments expected
- Environment: Required environment variables
- Files: Input files required
- Validation: Input validation rules

**Output Contract**:
- Format: JSON, CSV, plain text, etc.
- Fields: Expected fields in output
- Error handling: How errors are reported (typically in stderr + exit code)

**Validation Rules**:
- MUST be documented in parent SKILL.md with usage examples
- MUST be executable from project root: `python .github/copilot-skills/{skill-name}/scripts/{script.py}`
- MUST produce deterministic output for same input
- MUST have clear error messages on failure
- MUST include help text: `--help` or `-h` flag

**Relationships**:
- Belongs to: One Skill
- Referenced by: Parent SKILL.md (documentation)

**File Location**: `.github/copilot-skills/{skill-name}/scripts/{script-name}`

**Example**:
```python
#!/usr/bin/env python3
"""Extract form fields from PDF."""

# Input Contract:
# - input_file: Path to PDF
# - --format: Output format (json, csv)
# 
# Output Contract:
# - JSON: { "fields": [...], "success": true }

def main():
    # Implementation...
```

---

## Entity Relationships

```
SkillsRegistry (index.md)
  ├─ contains many SkillMetadata entries
  └─ references: Skill

Skill (.github/copilot-skills/{skill-name}/SKILL.md)
  ├─ has many DetailFile (forms.md, reference.md, patterns.md)
  ├─ has many ExecutableScript (scripts/)
  ├─ references many Skill (composability)
  └─ referenced by SkillsRegistry

DetailFile ({topic}.md)
  ├─ belongs to Skill
  ├─ references many Skill (cross-skill patterns)
  └─ contains code examples, tables, diagrams

ExecutableScript (scripts/{name})
  ├─ belongs to Skill
  ├─ documented by Skill
  └─ has input/output contracts
```

---

## File Structure Schema

```
.github/
├── copilot-instructions.md           # Main workspace instructions
└── copilot-skills/
    ├── index.md                       # SkillsRegistry (this file)
    │
    ├── {skill-name}/                  # Skill entity
    │   ├── SKILL.md                   # Core skill file (required)
    │   ├── {topic-1}.md               # DetailFile (optional)
    │   ├── {topic-2}.md               # DetailFile (optional)
    │   ├── examples/                  # DetailFile variant (optional)
    │   │   ├── example-1.md
    │   │   └── example-2.md
    │   └── scripts/                   # ExecutableScript directory
    │       ├── {script-1}.py          # ExecutableScript
    │       ├── {script-2}.sh          # ExecutableScript
    │       └── helper.js              # ExecutableScript
    │
    ├── {skill-2}/
    │   ├── SKILL.md
    │   ├── reference.md
    │   └── scripts/
    │       └── operation.py
    │
    └── {skill-n}/
        └── ...
```

---

## Data Lifecycle

### Skill Creation (PR Process)

1. **Author creates branch**: Feature branch named `NNN-skill-{skill-name}`
2. **Writes SKILL.md**: With YAML frontmatter and core content
3. **Adds detail files**: As needed (forms.md, reference.md, etc.)
4. **Writes scripts**: In scripts/ directory with documentation
5. **Updates index.md**: Adds SkillMetadata entry
6. **Opens PR**: For review
7. **Validation**: Check compliance with 5 constitution principles
8. **Merge**: Activates skill for project

### Skill Updates

1. **Author updates branch**: New PR for skill changes
2. **Updates SKILL.md**: Changes content
3. **Updates version**: Increment appropriately (MAJOR/MINOR/PATCH)
4. **Updates dependencies**: If new tools/libraries required
5. **Maintains backwards compatibility**: Or documents breaking changes
6. **Merges**: Version is incremented

### Skill Deprecation

1. **Mark state**: Change SKILL.md metadata to `deprecated: true`
2. **Add migration guide**: Document replacement skill
3. **Keep in registry**: Users can still find old skill
4. **Maintain for 2 releases**: Then archive
5. **Archive**: Move to `archived/` subdirectory

---

## Success Criteria Mapping

| Data Model Aspect | Success Criterion |
|-------------------|-------------------|
| SkillsRegistry index.md | SC-001: Discoverable in <2 minutes |
| Skill SKILL.md | SC-002: Scannable in <3 minutes |
| DetailFile progressive loading | SC-003: 60% context reduction |
| SkillMetadata clarity | SC-004: AI agents determine relevance |
| ExecutableScript determinism | SC-005: Consistent results |
| Cross-Skill references | SC-006: Composable workflows |
| Registry comprehensiveness | SC-007: 95% of tasks use 1-2 skills |
| Skill structure simplicity | SC-008: New skill in <30 minutes |
