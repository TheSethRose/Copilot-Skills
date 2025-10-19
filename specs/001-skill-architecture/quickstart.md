# Quick Start: Creating Your First Copilot Skill

**Estimated Time**: 20-30 minutes  
**Prerequisites**: GitHub repository with `.github/` directory, basic Markdown knowledge  
**Example**: We'll create a simple "hello-skill" to demonstrate the pattern

---

## Step 1: Create Skill Directory Structure

```bash
# Create the skill directory
mkdir -p .github/copilot-skills/hello-skill/scripts

# Navigate to skill directory
cd .github/copilot-skills/hello-skill
```

Your structure should look like:
```
.github/copilot-skills/
└── hello-skill/
    ├── SKILL.md           (create next)
    └── scripts/           (optional, for later)
```

---

## Step 2: Create SKILL.md with Metadata

Create `.github/copilot-skills/hello-skill/SKILL.md`:

```markdown
---
name: "hello-skill"
description: "A beginner-friendly skill demonstrating basic patterns"
version: "1.0.0"
created: "2025-10-18"
tags: ["example", "getting-started"]
dependencies: []
---

# Hello Skill

## Overview

This is a simple skill to demonstrate the Copilot Skills Architecture pattern.
Use this skill when learning how to create new skills or teaching others.

## Core Capabilities

- Understand skill structure
- Learn YAML frontmatter format
- Organize documentation progressively
- Create reusable skill templates

## Quick Start

### Understanding the Pattern

Every skill follows the same structure:
1. **SKILL.md** (this file) - Core concepts and quick start
2. **Detail files** (optional) - Specific topics like forms.md, reference.md
3. **scripts/** (optional) - Bundled executable implementations

### Your First Skill Task

When creating a new skill:

1. Copy this template structure
2. Replace metadata in frontmatter
3. Write clear, specific descriptions
4. Add detail files only if needed
5. Update the registry in `index.md`

## Common Patterns

### Pattern 1: Simple Reference Skill

For reference materials with no scripts (like brand-guidelines):
- SKILL.md with overview + reference content
- No detail files needed
- No scripts required

### Pattern 2: Skills with Utilities

For skills that have bundled scripts:
- SKILL.md with overview + usage examples
- Scripts in scripts/ directory
- Document each script clearly

### Pattern 3: Complex Skills

For skills with multiple topics:
- SKILL.md with overview (50-80 lines max)
- Detail files: forms.md, reference.md, patterns.md
- Scripts in scripts/ directory

## Error Handling

- Broken links to detail files: Update SKILL.md with correct path
- Missing scripts: Add script or remove documentation
- Metadata unclear: Update description to be more specific

## Next Steps

1. ✅ You've created the basic structure
2. 📝 [Add more details](#step-3-add-detail-files-optional)
3. 🔧 [Create scripts](#step-4-add-scripts-optional)
4. 📋 [Register the skill](#step-5-register-in-index-md)
5. ✔️ [Verify compliance](#step-6-verify-compliance)
```

---

## Step 3: Add Detail Files (Optional)

If your skill needs deeper documentation, create detail files. For our hello-skill example, create `.github/copilot-skills/hello-skill/patterns.md`:

```markdown
# Skill Authoring Patterns

## Pattern 1: Skill with Quick Reference

**When to use**: Informational skills without complex implementations

**Structure**:
```
skill-name/
├── SKILL.md              # Overview + quick reference (50-80 lines)
└── reference.md          # Detailed information (200+ lines)
```

**Example**: brand-guidelines, internal-comms

---

## Pattern 2: Skill with Utilities

**When to use**: Skills with bundled scripts for common operations

**Structure**:
```
skill-name/
├── SKILL.md              # Overview + usage examples (80-100 lines)
├── reference.md          # API documentation (200+ lines)
└── scripts/
    ├── operation-1.py    # Bundled script
    └── helper.sh         # Supporting script
```

**Example**: pdf-handling, xlsx-handling

---

## Pattern 3: Complex Multi-Topic Skill

**When to use**: Skills covering multiple distinct topics

**Structure**:
```
skill-name/
├── SKILL.md              # Overview only (40-50 lines)
├── topic-1.md            # First subtopic (200+ lines)
├── topic-2.md            # Second subtopic (200+ lines)
├── patterns.md           # Common patterns (150+ lines)
└── scripts/
    └── operation.py
```

**Example**: database-migration, compliance-tracking

---

## Choosing Your Pattern

| Criteria | Use Pattern 1 | Use Pattern 2 | Use Pattern 3 |
|----------|---------------|---------------|---------------|
| **Topics to cover** | 1-2 | 1-2 | 3+ |
| **Has scripts** | No | Yes | Yes |
| **Documentation size** | <150 lines | <250 lines | 500-1000 lines |
| **Complexity** | Low | Medium | High |

---

## Anti-Patterns to Avoid

❌ **Too large SKILL.md**: Keep under 100 lines, split into detail files  
❌ **Mixed topics**: Each detail file should cover ONE topic  
❌ **Missing documentation**: Every script must be documented in SKILL.md  
❌ **Unclear metadata**: Descriptions should be specific enough for AI matching  
❌ **Broken links**: All cross-references must have valid paths
```

---

## Step 4: Add Scripts (Optional)

If your skill needs executable scripts, create `.github/copilot-skills/hello-skill/scripts/hello.py`:

```python
#!/usr/bin/env python3
"""
Hello Skill - Simple example script

Usage:
  python .github/copilot-skills/hello-skill/scripts/hello.py "Your Name"

Output:
  JSON with greeting message
"""

import json
import sys

def main():
    if len(sys.argv) < 2:
        print(json.dumps({
            "success": False,
            "errors": ["Usage: hello.py <name>"]
        }))
        sys.exit(1)
    
    name = sys.argv[1]
    result = {
        "success": True,
        "greeting": f"Hello, {name}! Welcome to Copilot Skills.",
        "skill_name": "hello-skill"
    }
    
    print(json.dumps(result, indent=2))
    sys.exit(0)

if __name__ == "__main__":
    main()
```

Update SKILL.md to document the script:

```markdown
## Using the Hello Script

### Basic Usage

```bash
python .github/copilot-skills/hello-skill/scripts/hello.py "Your Name"
```

### Output

```json
{
  "success": true,
  "greeting": "Hello, Your Name! Welcome to Copilot Skills.",
  "skill_name": "hello-skill"
}
```

### Error Handling

If you forget the name argument:
```bash
$ python .github/copilot-skills/hello-skill/scripts/hello.py

{
  "success": false,
  "errors": ["Usage: hello.py <name>"]
}
```
```

---

## Step 5: Register in index.md

Update `.github/copilot-skills/index.md` to include your skill:

```markdown
# Copilot Skills Registry

Available skills for this workspace.

## Hello Skill

**Path**: `.github/copilot-skills/hello-skill/SKILL.md`  
**Description**: A beginner-friendly skill demonstrating basic patterns  
**When to use**: Learning skill creation, teaching architecture patterns  
**Keywords**: example, getting-started, template

---

[Add other skills here...]
```

---

## Step 6: Verify Compliance

Before committing, check that your skill meets the 5 core principles:

### ✅ Checklist

- [ ] **I. Progressive Disclosure**: SKILL.md < 100 lines? Detail files for deeper topics?
- [ ] **II. File-Based Organization**: Organized as skill-name/ with SKILL.md? Scripts in scripts/?
- [ ] **III. Dynamic Discovery**: Registered in index.md? Clear description and tags?
- [ ] **IV. Deterministic Execution**: Scripts documented with usage examples? Input/output contracts clear?
- [ ] **V. Composability**: Cross-references documented? Dependencies declared?

### ✅ Quality Checks

- [ ] No template files or placeholders remaining
- [ ] All links use relative paths (e.g., `[forms.md](./forms.md)`)
- [ ] Metadata (name, description, tags) is specific and clear
- [ ] YAML frontmatter is valid syntax
- [ ] Scripts have help text and error handling

---

## Step 7: Test Discovery

Open `.github/copilot-skills/index.md` and verify your skill is listed. Your Copilot session should now be able to:

1. **Discover** your skill when you mention relevant tasks
2. **Load** the SKILL.md file with core concepts
3. **Navigate** to detail files if needed
4. **Execute** bundled scripts if defined

---

## Common Questions

### Q: How many detail files should I create?

**A**: As many as needed to cover distinct topics. Common patterns:
- Simple skills: Just SKILL.md (no detail files)
- Medium skills: SKILL.md + 1-2 detail files (forms.md, reference.md)
- Complex skills: SKILL.md + 3-4 detail files + examples/

### Q: Can I reference other skills?

**A**: Yes! Use markdown links in detail files:
```markdown
For PDF creation, see [pdf-handling skill](../pdf-handling/SKILL.md)
```

### Q: What if my skill is too large?

**A**: Split into multiple skills. One skill = one topic/domain.

### Q: How do I update a skill?

**A**: Create a new branch, update files, increment version in SKILL.md, open PR.

### Q: Can I have nested detail files?

**A**: Not recommended. Keep structure flat for simplicity:
```
skill-name/
├── SKILL.md
├── topic-1.md
├── topic-2.md
└── scripts/
```

Instead of:
```
skill-name/
├── SKILL.md
└── details/
    ├── topic-1.md
    └── topic-2.md
```

---

## Next: Create Your Real Skill

You're ready! Use this structure for your actual skill:

1. Copy hello-skill pattern
2. Replace with your domain (pdf-handling, compliance, etc.)
3. Add specific documentation and scripts
4. Update index.md
5. Open a PR
6. Get reviewed for compliance
7. Merge and celebrate! 🎉

---

## Resources

- **Spec**: [spec.md](./spec.md)
- **Data Model**: [data-model.md](./data-model.md)
- **Example Skills**: See `examples/` folder in repo root
  - Anthropic official: `examples/anthropics-skills/`
  - Community patterns: `examples/obra-superpowers/`
  - Office skills: `examples/tfriedel-claude-office-skills/`
- **Constitution**: `.specify/memory/constitution.md`
