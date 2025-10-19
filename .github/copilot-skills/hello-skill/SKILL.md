---
name: "Hello Skill"
description: "Example skill demonstrating discovery, progressive loading, and bundled script patterns"
version: "1.0.0"
created: "2025-10-18"
tags: ["example", "discovery", "tutorial"]
dependencies: []
---

# Hello Skill

## Overview

This is an example skill designed to demonstrate how the Copilot Skills Architecture enables discovery and progressive loading of specialized knowledge. It shows the complete pattern that developers should follow when creating new skills.

## Core Capabilities

- Demonstrate skill discovery workflow
- Show YAML frontmatter metadata format
- Link to detail files for deeper information
- Execute bundled scripts for deterministic operations
- Model progressive disclosure (metadata → SKILL.md → detail files → scripts)

## Quick Start

### Discovering This Skill

1. Developer reads `.github/copilot-skills/index.md`
2. Finds "Hello Skill" entry with description
3. Opens `./SKILL.md` (this file)
4. Understands core capabilities in < 3 minutes
5. Links to detail files when more information needed

### Running the Bundled Script

This skill includes an example script:

```bash
python .github/copilot-skills/hello-skill/scripts/hello-example.py --name "World"
```

**Output**:
```json
{
  "success": true,
  "message": "Hello, World!",
  "data": {
    "greeting": "Hello, World!",
    "timestamp": "2025-10-18T10:30:00Z"
  },
  "error": null
}
```

## Common Patterns

### Pattern 1: Skill with Simple Reference

A skill that provides guidance and reference material without scripts:

```
skill-directory/
├── SKILL.md              # Core file, <3 min read
├── reference.md          # API reference
└── patterns.md           # Common patterns
```

**Example**: General guidance skills, best practices, architectural patterns

### Pattern 2: Skill with Utility Scripts

A skill that provides guidance plus bundled scripts for deterministic operations:

```
skill-directory/
├── SKILL.md              # Core file
├── forms.md              # Specific use cases
├── reference.md          # API reference
└── scripts/
    ├── utility.py        # Python script
    └── helper.sh         # Shell script
```

**Example**: Compliance tracking, data extraction, calculations

### Pattern 3: Complex Skill with Multiple Topics

A skill spanning related topics, each requiring detailed explanation:

```
skill-directory/
├── SKILL.md              # Core, links to detail files
├── topic-1.md            # Detail on first topic
├── topic-2.md            # Detail on second topic
├── topic-3.md            # Detail on third topic
└── scripts/
    ├── operation-1.py    # Script for topic 1
    └── operation-2.py    # Script for topic 2
```

**Example**: PDF handling (forms + text extraction + tables), financial reporting (templates + calculations + formatting)

## Metadata Explained

The YAML frontmatter enables AI agents to discover and understand this skill:

```yaml
---
name: "Hello Skill"
description: "Example skill demonstrating discovery, progressive loading, and bundled script patterns"
version: "1.0.0"
created: "2025-10-18"
tags: ["example", "discovery", "tutorial"]
dependencies: []
---
```

| Field | Purpose | Our Value |
|-------|---------|-----------|
| `name` | Display name | "Hello Skill" |
| `description` | What developers can do | "Example demonstrating discovery..." |
| `version` | Current version | "1.0.0" |
| `tags` | Search keywords | ["example", "discovery", "tutorial"] |
| `dependencies` | Required libraries | [] (none) |

## Bundled Scripts

This skill includes utility scripts for deterministic operations:

### Example Script: hello-example.py

**Location**: `.github/copilot-skills/hello-skill/scripts/hello-example.py`

**Purpose**: Generate a personalized greeting message with consistent format

**Usage**:
```bash
python .github/copilot-skills/hello-skill/scripts/hello-example.py --name "Alice"
```

**Arguments**:
- `--name` (required): The name to greet

**Output Format**:
```json
{
  "success": true,
  "message": "Hello, {name}!",
  "data": {
    "greeting": "Hello, {name}!",
    "timestamp": "ISO 8601 timestamp"
  },
  "error": null
}
```

**Error Handling**:
- Missing `--name` argument → Returns error status with message
- Returns non-zero exit code on failure

## Detailed References

- For specific pattern implementations, see [patterns.md](./patterns.md)
- For complete reference and design philosophy, see [reference.md](./reference.md)

## Progressive Disclosure: 4-Layer Example

This skill demonstrates the 4-layer progressive disclosure model:

**Layer 1: Index Metadata** (30 seconds)
```markdown
**Description**: Example skill demonstrating discovery...
**When to use**: Learning about skill architecture
```

**Layer 2: SKILL.md** (This file, ~3 minutes)
- Core Capabilities
- Quick Start
- Common Patterns
- Links to detail files

**Layer 3: Detail Files** (5-15 minutes)
- `patterns.md` → Detailed pattern examples
- `reference.md` → Complete design reference

**Layer 4: Scripts** (On-demand)
- `hello-example.py` → Deterministic operation
- Usage documented in SKILL.md

## Error Handling

- **Script fails**: Check arguments are correct. See "Arguments" section above.
- **Wrong Python version**: Use Python 3.6+
- **Module import errors**: Check dependencies are installed

## Related Skills

This skill demonstrates patterns used in all other skills:
- [skill-template](../skill-template/SKILL.md) - Complete template for new skills
- [PDF Handling](../pdf-handling/SKILL.md) - Real-world example (when available)

---

**Version**: 1.0.0 | **Last Updated**: October 18, 2025 | **Status**: Example Skill
