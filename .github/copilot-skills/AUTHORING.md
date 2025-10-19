# Authoring Guide: Creating New Copilot Skills

This guide walks you through creating a new skill from scratch, step by step.

**Estimated time**: 20-30 minutes for a complete skill

**Prerequisites**: Understand the 5 Constitutional Principles (see [../README.md](./README.md))

---

## Step 1: Plan Your Skill (5 minutes)

### Answer These Questions

**What domain does this skill cover?**
- Single, well-defined domain (e.g., "PDF handling", not "document processing")
- If your domain spans multiple topics, consider creating separate skills

**What can developers do with this skill?**
- List 3-5 core capabilities (e.g., "extract text from PDFs", "fill PDF forms", "validate PDF structure")
- Be specific, not vague

**When should developers use this skill?**
- What keywords or task types would trigger this skill? (e.g., "PDF extraction", "form filling", "PDF validation")
- How is it different from related skills?

**What dependencies does it need?**
- List libraries, tools, or other skills this skill depends on
- Example: `["pypdf2", "pdfplumber"]`

**Should it include scripts?**
- Complex operations that need determinism? → Yes, include scripts
- Simple reference material? → No scripts needed

### Example Planning Session

```
Skill: PDF Handling

Domain: PDF document manipulation
Capabilities:
  - Extract text from PDFs
  - Parse form fields
  - Fill PDF forms programmatically
  - Extract tables and structured data

When to use:
  Keywords: "extract PDF text", "fill form", "parse form fields"
  Different from: General document skills (this is PDF-specific)

Dependencies: pypdf2, pdfplumber

Scripts needed? Yes - for form field extraction and filling
```

---

## Step 2: Create Skill Directory Structure (2 minutes)

Create the directory and main file:

```bash
mkdir -p .github/copilot-skills/{skill-name}/scripts
touch .github/copilot-skills/{skill-name}/SKILL.md
```

Replace `{skill-name}` with your skill name in **kebab-case** (lowercase with hyphens).

**Example**: `pdf-handling`, `compliance-tracking`, `financial-reporting`

---

## Step 3: Write SKILL.md (10-15 minutes)

This is the core file that developers read. Keep it scannable in under 3 minutes.

### YAML Frontmatter

Copy this template and fill in your values:

```yaml
---
name: "Your Skill Name"
description: "One sentence: what developers can do with this skill"
version: "1.0.0"
created: "YYYY-MM-DD"
tags: ["tag1", "tag2", "tag3"]
dependencies: ["library1", "tool2"]
---
```

**Guidelines**:
- `name`: Display name (Title Case)
- `description`: One sentence, <100 characters. Example: "Extract text, fill forms, and manipulate PDF documents"
- `version`: Start with "1.0.0" (follow semantic versioning for updates)
- `tags`: 3-5 lowercase keywords (no spaces)
- `dependencies`: List all required libraries/tools

### Core Sections

After frontmatter, write these sections:

#### 1. Overview (50-100 words)

**Why this skill exists and what it enables**

```markdown
## Overview

This skill provides capabilities for reading, parsing, and manipulating PDF documents. It enables developers to:
- Extract text content and structured data
- Parse form fields and values
- Fill PDF forms programmatically
- Work with encrypted PDFs
```

#### 2. Core Capabilities (Bulleted list)

**What developers can accomplish with this skill**

```markdown
## Core Capabilities

- Extract text content from PDFs
- Parse form fields and values
- Fill PDF forms programmatically
- Extract tables and structured data
- Handle password-protected PDFs
```

#### 3. Quick Start (One minimal example)

**Get started in 2-3 minutes**

```markdown
## Quick Start

### Extracting Text from a PDF

```python
import pdfplumber

with pdfplumber.open("document.pdf") as pdf:
    for page in pdf.pages:
        print(page.extract_text())
```
```

#### 4. Common Patterns (2-4 pattern examples)

**Show developers how to accomplish typical tasks**

```markdown
## Common Patterns

### Pattern 1: Extract All Text
When you need full document text extraction, use pdfplumber for better accuracy than PyPDF2.

### Pattern 2: Parse Form Fields
Always extract field names first before attempting to fill. Government forms require exact field matches.

### Pattern 3: Handle Encrypted PDFs
Use pdfplumber's encryption handling. See [reference.md](./reference.md) for password handling patterns.
```

#### 5. Bundled Scripts (if applicable)

**Document scripts that do deterministic operations**

```markdown
## Bundled Scripts

This skill includes the following scripts for deterministic operations:

- `extract_form_fields.py` - Extract all form fields from a PDF and return as JSON
  
**Usage**:
```bash
python .github/copilot-skills/pdf-handling/scripts/extract_form_fields.py input.pdf --format json
```

**Output format**:
```json
{
  "success": true,
  "fields": [
    {"name": "field_name", "value": "field_value", "type": "text"}
  ],
  "error": null
}
```
```

#### 6. Detailed References

**Link to detail files for deeper information**

```markdown
## Detailed References

- For form-specific operations and form types, see [forms.md](./forms.md)
- For complete API reference and library documentation, see [reference.md](./reference.md)
- For code examples and edge cases, see [examples.md](./examples.md)
```

#### 7. Error Handling (optional)

**Document common errors and recovery**

```markdown
## Error Handling

- **PDF parsing fails**: Check PDF version compatibility. See reference.md for version support.
- **Form fields not found**: Validate field names exactly match PDF field names. Use extract_form_fields.py script to find correct names.
- **Password-protected PDFs**: Provide password to pdfplumber. See forms.md for encrypted PDF patterns.
```

---

## Step 4: Create Detail Files (10-20 minutes)

If your SKILL.md references detail files (forms.md, reference.md), create them now.

### Detail File Guidelines

**Each detail file should**:
- Focus on ONE specific topic
- Be readable standalone (don't require reading other files first)
- Be 500+ words (substantial, not stub)
- Use clear section headings
- Include code examples

### Example Detail Files

#### forms.md - Form-Specific Operations

```markdown
# PDF Form Handling

## Form Field Extraction
[Detailed instructions for extracting form fields]

## Filling Forms Programmatically
[Patterns for filling different form types]

## Common Form Types
- IRS Tax Forms (W-2, 1099)
- Government Applications
- Medical Forms
```

#### reference.md - API Reference

```markdown
# PDF Library Reference

## PyPDF2 API
[Complete API documentation for PyPDF2]

## pdfplumber API
[Complete API documentation for pdfplumber]

## Version Compatibility
[Notes on library version compatibility]
```

#### examples.md - Code Examples

```markdown
# PDF Handling Examples

## Example 1: Extract text from specific pages
[Complete working example]

## Example 2: Fill a government form
[Complete working example]

## Example 3: Extract tables as CSV
[Complete working example]
```

---

## Step 5: Add Bundled Scripts (if applicable) (5-10 minutes)

If your SKILL.md includes bundled scripts, create them in `scripts/` directory.

### Script Best Practices

**Python Scripts** (`.github/copilot-skills/{skill-name}/scripts/{name}.py`):

```python
#!/usr/bin/env python3
"""
Script description and what it does.

Usage:
    python script.py --input "value" --format json

Arguments:
    --input: Required input parameter
    --format: Output format (json, text, etc.)

Output:
    JSON with structure: {"success": bool, "data": any, "error": str|null}
"""

import json
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="[Script purpose]")
    parser.add_argument("--input", required=True, help="Input value")
    parser.add_argument("--format", choices=["json", "text"], default="json")
    
    args = parser.parse_args()
    
    try:
        result = process(args.input)
        output = {"success": True, "data": result, "error": None}
        print(json.dumps(output, indent=2))
        return 0
    except Exception as e:
        output = {"success": False, "data": None, "error": str(e)}
        print(json.dumps(output, indent=2), file=sys.stderr)
        return 1

def process(value):
    # Your logic here
    return value

if __name__ == "__main__":
    sys.exit(main())
```

**Shell Scripts** (`.github/copilot-skills/{skill-name}/scripts/{name}.sh`):

```bash
#!/bin/bash
# Script description and what it does
#
# Usage:
#     bash script.sh "argument"
#
# Arguments:
#     $1: Input value

set -e

if [ $# -lt 1 ]; then
    echo "Error: Missing required argument" >&2
    exit 1
fi

input="$1"
# Your logic here
echo "Result: $input"
exit 0
```

### Script Requirements

- Argument parsing and validation
- Deterministic output (same input → same output)
- Error handling with meaningful messages
- Exit codes (0 = success, non-zero = failure)
- Clear documentation in script header
- Relative paths (no hardcoding, work from project root)

### Script Execution Contract

Every bundled script MUST document its input/output contract so Copilot and developers understand how to use it correctly.

#### Contract Template

```
Script: {name}.py or {name}.sh

Purpose: [One sentence describing what it does]

Arguments:
  --arg1 (required): Description of arg1
  --arg2 (optional, default "value"): Description of arg2

Flags:
  --format (optional, default "json"): Output format choices

Input Validation:
  - arg1 must be non-empty string
  - arg2 must be valid email

Output Format (JSON):
  {
    "success": true|false,
    "data": {...},
    "error": null|"error message"
  }

Output Format (text):
  [Human readable output]

Exit Codes:
  0: Success
  1: Argument validation error
  2: Processing error

Error Messages:
  - [Error description]: When does this occur?

Examples:
  # Example 1: Success
  python script.py --arg1 "value1" --arg2 "value2"
  → {"success": true, "data": {...}, "error": null}

  # Example 2: Error
  python script.py --arg1 ""
  → {"success": false, "data": null, "error": "arg1 cannot be empty"}

Determinism:
  Same input always produces same output (no randomness, timestamps acceptable only if documented)

Performance:
  Typical runtime: [X seconds]
  Max file size: [if applicable]
```

#### Where to Document

Include the contract in your SKILL.md file under the "Bundled Scripts" section:

```markdown
## Bundled Scripts

### script-name.py

**Purpose**: Generate a personalized greeting message

**Usage**:
```bash
python .github/copilot-skills/hello-skill/scripts/hello-example.py --name "Alice"
```

**Contract**:
- Arguments: --name (required), --format (optional, default "json")
- Output: JSON with structure {"success": bool, "message": str, "data": obj, "error": null|str}
- Exit codes: 0 = success, 1 = error
- Determinism: Same input → same output

**Example**:
```bash
python hello-example.py --name "Bob"
# Output:
# {
#   "success": true,
#   "message": "Hello, Bob!",
#   "data": {"greeting": "Hello, Bob!"},
#   "error": null
# }
```
```

---

## Step 6: Register in index.md (2 minutes)

Add your skill to `.github/copilot-skills/index.md`:

```markdown
### Your Skill Name
**Path**: `.github/copilot-skills/your-skill-name/SKILL.md`
**Description**: One sentence describing what developers can do
**When to use**: Specific task types or keywords that trigger this skill
**Tags**: `tag1`, `tag2`, `tag3`
```

---

## Step 7: Validate with Compliance Checklist (5 minutes)

Run the skill compliance checklist to ensure your skill meets all Constitutional Principles:

1. Open `.specify/checklists/skill-compliance-checklist.md`
2. Work through each section:
   - ✅ Progressive Disclosure
   - ✅ File-Based Organization
   - ✅ Dynamic Discovery
   - ✅ Deterministic Execution
   - ✅ Composability
3. Mark items as passing or note revisions needed
4. Get sign-off from maintainer

---

## Step 8: Open a Pull Request (Optional - Full Workflow)

When ready for review and merging:

1. Commit your skill directory and files
2. Push to feature branch
3. Open PR with title: `feat: Add {skill-name} skill`
4. PR description includes:
   - Skill name and purpose
   - Core capabilities (bullet list)
   - Examples of when to use
   - Link to compliance checklist
5. Reviewers use `.specify/checklists/skill-compliance-checklist.md` to validate
6. Merge once approved and all checks pass

---

## Quick Reference: File Checklist

Before considering your skill complete:

- [ ] Directory created: `.github/copilot-skills/{skill-name}/`
- [ ] SKILL.md created with complete YAML frontmatter
- [ ] SKILL.md includes: Overview, Core Capabilities, Quick Start, Common Patterns, Detailed References
- [ ] Detail files created (forms.md, reference.md, examples.md) as referenced in SKILL.md
- [ ] Each detail file is 500+ words and stands alone
- [ ] Bundled scripts created in `scripts/` (if applicable)
- [ ] Scripts document input/output contracts
- [ ] Scripts handle errors and use deterministic logic
- [ ] Skill registered in `.github/copilot-skills/index.md`
- [ ] Skill name matches directory name (kebab-case)
- [ ] All markdown links work correctly (relative paths)
- [ ] Compliance checklist reviewed and passing

---

## Common Mistakes to Avoid

❌ **Generic descriptions** - "handles documents" (too vague)  
✅ **Specific descriptions** - "Extract form fields and fill PDF forms programmatically"

❌ **SKILL.md > 3 minutes to read** - Too much detail in core file  
✅ **SKILL.md < 3 minutes** - Move details to forms.md, reference.md

❌ **Detail files that depend on each other** - "See the previous section in X.md"  
✅ **Self-contained detail files** - Each explains its topic completely

❌ **Undocumented scripts** - "See the code"  
✅ **Well-documented scripts** - Usage, arguments, output documented in SKILL.md

❌ **No error handling** - Scripts crash on bad input  
✅ **Robust scripts** - Validate inputs, return structured error messages

---

## Examples to Study

Learn from existing skills:

- **Anthropic Official Skills** - `.examples/anthropics-skills/` (Metadata-first design)
- **Community Skills** - `.examples/obra-superpowers/skills/` (Command patterns, composition)
- **Skill Template** - `.github/copilot-skills/skill-template/` (Use as reference)

---

## Getting Help

**Questions about Constitutional Principles?** Read [../README.md](./README.md)

**Questions about YAML or Markdown syntax?** See [GOVERNANCE.md](./GOVERNANCE.md)

**Issues with your skill?** Check [TROUBLESHOOTING.md](./TROUBLESHOOTING.md)

**Need a detailed review?** See [GOVERNANCE.md](./GOVERNANCE.md) for PR checklist

---

**Version**: 1.0.0 | **Last Updated**: October 18, 2025
