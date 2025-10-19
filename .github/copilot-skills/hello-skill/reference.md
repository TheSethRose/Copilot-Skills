# Hello Skill - Reference

Complete reference documentation for the Hello Skill, demonstrating design philosophy and implementation patterns for the Copilot Skills Architecture.

## Architecture Philosophy

### Core Principles

The Hello Skill is built on the 5 Constitutional Principles:

1. **Progressive Disclosure**
   - SKILL.md provides quick understanding (~3 minutes)
   - Detail files (patterns.md, reference.md) provide deep dives
   - Scripts demonstrate deterministic operations
   - Information loads in layers as needed

2. **File-Based Organization**
   - Hello Skill is a directory: `.github/copilot-skills/hello-skill/`
   - Contains SKILL.md (core) + detail files + scripts/
   - Clear file structure enables easy navigation
   - Each file has clear purpose

3. **Dynamic Discovery Through Metadata**
   - YAML frontmatter in SKILL.md contains:
     - `name`: "Hello Skill"
     - `description`: Clear, specific purpose
     - `tags`: ["example", "discovery", "tutorial"]
   - Index.md lists skill with metadata
   - AI agents use metadata to determine relevance

4. **Deterministic Execution with Scripts**
   - `hello-example.py` script runs consistently
   - Same input → Same output always
   - Error handling is predictable
   - Usage documented in SKILL.md

5. **Composability and Cross-Skill References**
   - Hello Skill can stand alone
   - References to related skills use relative paths
   - Dependencies declared in metadata
   - Clear scope boundaries

---

## Design Decisions

### Why This Structure?

**Question**: Why separate SKILL.md, patterns.md, and reference.md?

**Answer**: Progressive Disclosure
- SKILL.md (quick): "Here's what this skill does and how to start"
- patterns.md (intermediate): "Here are the patterns we support"
- reference.md (deep): "Here's the complete design and philosophy"

Developers starting can skip patterns.md and reference.md. Developers going deep can read them independently without rereading SKILL.md.

### Why YAML Frontmatter?

**Question**: Why use YAML frontmatter instead of inline metadata?

**Answer**: Machine Readability
- Parseable by tools and AI agents
- Enables automated indexing and validation
- Consistent format across all skills
- Used by Anthropic's official skills

### Why Bundled Scripts?

**Question**: Why include scripts instead of just documentation?

**Answer**: Determinism
- Documentation can be misinterpreted
- Scripts enforce consistent behavior
- Same logic used everywhere
- Reduces bugs from reimplementation

### Why tags in Metadata?

**Question**: Why include tags if skills are organized by directory?

**Answer**: Discovery and Filtering
- Tags enable semantic search
- "compliance" tag helps find all compliance-related skills
- "tutorial" tag finds learning resources
- AI agents can match keywords to tags

---

## Implementation Details

### Metadata Structure

```yaml
---
name: "Hello Skill"                                      # Display name
description: "Example skill demonstrating discovery..." # One sentence
version: "1.0.0"                                         # Semantic version
created: "2025-10-18"                                    # Creation date
tags: ["example", "discovery", "tutorial"]               # Search keywords
dependencies: []                                         # Required libraries
---
```

**Validation Rules**:
- `name`: Must match directory name in kebab-case
- `description`: Must be < 100 characters, specific not vague
- `version`: Must follow MAJOR.MINOR.PATCH format
- `tags`: 3-5 tags, lowercase, no spaces
- `dependencies`: Array of strings (can be empty)

### Markdown Structure

Standard sections in SKILL.md:

```markdown
# Heading (matches name from metadata)

## Overview
[Why this skill exists]

## Core Capabilities
[Bulleted list of what developers can do]

## Quick Start
[One minimal example]

## Common Patterns
[2-4 pattern descriptions]

## Bundled Scripts
[If applicable: scripts and their usage]

## Detailed References
[Links to detail files]

## Error Handling
[Common issues and solutions]

## Related Skills
[Links to related skills]
```

### Detail File Structure

Standard sections in detail files (patterns.md, reference.md):

```markdown
# Hello Skill - [Topic Name]

## Introduction
[Why this topic matters]

## [Section 1]
[Detailed explanation with examples]

## [Section 2]
[Detailed explanation with examples]

## [Subsections]
[Use H3 for subsections]

## Next Steps
[How to continue learning]
```

**Key Rule**: Each detail file stands independently
- Can be read first without reading other files
- Contains necessary context
- Doesn't refer to "previous sections" in other files

---

## Script Patterns

### Python Script Template

```python
#!/usr/bin/env python3
"""
[One-line description]

Longer description of what this script does and when to use it.

Usage:
    python script.py --input "value" --format json

Arguments:
    --input: Description of input argument
    --format: Description of format argument

Output:
    {
      "success": true/false,
      "data": <result_object>,
      "error": null or error message
    }
"""

import json
import argparse
import sys

def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="[Description]")
    parser.add_argument("--input", required=True, help="[Help text]")
    parser.add_argument("--format", default="json", help="[Help text]")
    
    args = parser.parse_args()
    
    try:
        result = process(args.input, args.format)
        output = {"success": True, "data": result, "error": None}
        print(json.dumps(output, indent=2))
        return 0
    except Exception as e:
        output = {"success": False, "data": None, "error": str(e)}
        print(json.dumps(output, indent=2), file=sys.stderr)
        return 1

def process(input_val, format_type):
    """Process the input and return result."""
    # Implementation
    return input_val

if __name__ == "__main__":
    sys.exit(main())
```

### Shell Script Template

```bash
#!/bin/bash
# [One-line description]
#
# Description of what this script does and when to use it.
#
# Usage:
#     bash script.sh "argument"
#
# Arguments:
#     $1: Description of first argument
#     $2: Description of second argument
#
# Output:
#     Descriptive output or structured format

set -e  # Exit on error

# Validate arguments
if [ $# -lt 1 ]; then
    echo "Error: Missing required argument" >&2
    exit 1
fi

input="$1"

# Process
output=$(process_input "$input")

# Output result
echo "$output"
exit 0

function process_input() {
    local input="$1"
    echo "Processed: $input"
}
```

### Script Input/Output Contract

Every script MUST document:

1. **Arguments**: What parameters it accepts
2. **Flags**: What optional flags it supports
3. **Output Format**: What it returns (JSON, plain text, etc.)
4. **Error Handling**: How it signals errors
5. **Exit Codes**: What return codes mean what
6. **Side Effects**: What it modifies (if anything)

Example:

```
Script: hello-example.py

Arguments:
  --name (required): Name to greet

Flags:
  --format (optional, default "json"): Output format (json or text)
  --timestamp (optional, default false): Include timestamp in output

Output Format (JSON):
  {
    "success": true,
    "message": "Hello, {name}!",
    "data": { "greeting": "...", "timestamp": "..." },
    "error": null
  }

Output Format (Text):
  Hello, {name}!

Error Handling:
  - Missing --name: Returns error message, exit code 1
  - Invalid format: Returns error message, exit code 1
  - Unexpected error: Returns error message, exit code 1

Exit Codes:
  0: Success
  1: Argument error or processing error
```

---

## Validation Checklist

Use this checklist to validate Hello Skill (and all other skills):

### Structure
- [ ] Directory exists: `.github/copilot-skills/hello-skill/`
- [ ] SKILL.md exists with YAML frontmatter
- [ ] Detail files exist and are referenced in SKILL.md
- [ ] Scripts exist and are documented in SKILL.md
- [ ] All markdown is valid syntax

### Metadata
- [ ] Name matches directory name (kebab-case)
- [ ] Description is specific and < 100 characters
- [ ] Version follows MAJOR.MINOR.PATCH
- [ ] Tags are lowercase, relevant, 3-5 total
- [ ] Dependencies list is complete

### Content Quality
- [ ] SKILL.md scannable in < 3 minutes
- [ ] Detail files each focus on single topic
- [ ] Detail files can be read independently
- [ ] Code examples are syntactically correct
- [ ] All links are relative and functional

### Progressive Disclosure
- [ ] Quick start in SKILL.md is minimal
- [ ] Detailed References section links to detail files
- [ ] No duplication between files
- [ ] Each layer adds value without requiring previous layers

### Scripts
- [ ] Scripts have proper documentation header
- [ ] Scripts document arguments and flags
- [ ] Scripts document output format
- [ ] Scripts handle errors gracefully
- [ ] Scripts are executable (correct permissions)
- [ ] Scripts produce deterministic results

---

## Extension Points

### Adding More Detail Files

To extend Hello Skill:

1. Create new `.md` file (e.g., `troubleshooting.md`)
2. Link from SKILL.md in Detailed References section
3. Ensure file is independent and > 500 words
4. Follow same structure as existing detail files

### Adding More Scripts

To extend Hello Skill:

1. Create new script in `scripts/` directory
2. Document in SKILL.md under Bundled Scripts
3. Follow input/output contract pattern
4. Test that script is deterministic

---

## Common Mistakes & How to Avoid Them

### Mistake 1: Detail Files That Cross-Reference

❌ **Bad**:
```markdown
# patterns.md
For the reference implementation, see [reference.md](./reference.md)
```

✅ **Good**:
```markdown
# patterns.md
Here are the three pattern types...
[Complete explanation without referencing other files]
```

### Mistake 2: SKILL.md That's Too Long

❌ **Bad**: 50KB SKILL.md with comprehensive API reference

✅ **Good**: 3KB SKILL.md with links to reference.md (10KB)

### Mistake 3: Scripts Without Documentation

❌ **Bad**:
```python
def process(x):
    return x * 2
```

✅ **Good**:
```python
"""
Doubles the input value.

Arguments:
    --input: Number to double

Output:
    JSON: {"success": true, "data": 20}
"""
```

### Mistake 4: Vague Metadata

❌ **Bad**:
```yaml
name: "Tools"
description: "Helper utilities"
tags: ["misc"]
```

✅ **Good**:
```yaml
name: "License Status Checker"
description: "Calculate license expiration status and compliance warnings"
tags: ["compliance", "licensing", "status"]
```

---

## Extending the Architecture

### For Single Workspace

Hello Skill demonstrates the foundational architecture for a single GitHub repository's Copilot workspace. All skills live in `.github/copilot-skills/` with index.md as the registry.

### For Multiple Workspaces (Future)

The architecture could extend to:
- Shared skill library (published npm package of skills)
- Skill marketplace (discover community skills)
- Automated skill generation (from templates)
- Skill versioning system (manage breaking changes)

---

## References

- **Constitution**: `.specify/memory/constitution.md`
- **Authoring Guide**: `./AUTHORING.md`
- **Governance**: `./GOVERNANCE.md`
- **Compliance Checklist**: `.specify/checklists/skill-compliance-checklist.md`
- **Skill Template**: `.github/copilot-skills/skill-template/SKILL.md`

---

**Version**: 1.0.0 | **Last Updated**: October 18, 2025 | **Maintainer**: Architecture Team
