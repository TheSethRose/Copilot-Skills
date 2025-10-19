# Examples: Skill Discovery, Progressive Loading & Script Execution

This document demonstrates complete workflows showing how the Copilot Skills Architecture works end-to-end.

---

## Complete Example 1: Developer Discovering and Using a Skill

### Scenario

Developer is working on a task: **"I need to extract form fields from a PDF and then fill in values"**

### Step 1: Discover the Skill

**What the developer does**:
```
Open VS Code
→ Go to Explorer
→ Navigate to .github/copilot-skills/index.md
→ Read the registry
→ Search for "PDF" or "form"
```

**What they see in index.md**:
```markdown
### PDF Handling
**Path**: `.github/copilot-skills/pdf-handling/SKILL.md`
**Description**: Extract text, fill forms, and manipulate PDF documents
**When to use**: PDF parsing, form extraction, document generation
**Tags**: `documents`, `pdf`, `forms`
```

**Result**: Developer finds the PDF Handling skill!

---

### Step 2: Load SKILL.md (Progressive Layer 1)

**What the developer does**:
```
Click path in index.md
→ Opens .github/copilot-skills/pdf-handling/SKILL.md
→ Takes 2-3 minutes to read
```

**What they see**:
- **Overview**: "Extract text, fill forms, and manipulate PDF documents"
- **Core Capabilities**: 
  - Extract text content from PDFs
  - Parse form fields and values
  - Fill PDF forms programmatically
  - Extract tables and structured data
- **Quick Start**: A simple example of reading PDF text
- **Patterns**: Three pattern types (text extraction, form parsing, form filling)
- **Bundled Scripts**: Reference to `extract_form_fields.py` and `fill_pdf_form.py`
- **Detailed References**: Links to `forms.md`, `reference.md`, `patterns.md`

**Result**: Developer understands the skill and what it can do. SKILL.md is complete enough for basic understanding.

---

### Step 3: Navigate to Detail File (Progressive Layer 2)

**What the developer does**:
```
Read in SKILL.md: "For form-specific patterns, see forms.md"
→ Click link to forms.md
→ Read form-specific section
```

**What they see in forms.md**:
```markdown
# PDF Form Handling

## Form Field Extraction
Use the bundled script...

## Filling Forms Programmatically
[Detailed patterns for different form types]

## Common Form Types
- Government forms (W-2, 1099)
- Medical forms
- Application forms
```

**Result**: Developer gets specific guidance for forms. This detail file focused on forms doesn't require reading reference.md or patterns.md.

---

### Step 4: Run Bundled Script (Layer 3)

**What the developer does**:
```
Read in forms.md: "Use script: extract_form_fields.py"
→ Open terminal
→ Run script with their PDF
```

**Command**:
```bash
python .github/copilot-skills/pdf-handling/scripts/extract_form_fields.py myform.pdf --format json
```

**Output**:
```json
{
  "success": true,
  "fields": [
    {"name": "applicant_name", "type": "text", "value": ""},
    {"name": "applicant_email", "type": "email", "value": ""},
    {"name": "submit", "type": "button", "value": "Submit"}
  ],
  "error": null
}
```

**Result**: Deterministic extraction! Developer now knows exactly which fields exist and can proceed with filling.

---

### Step 5: Reference Detail File if Needed (Layer 3, different path)

**What the developer does** (optional):
```
Read in SKILL.md: "For complete API reference, see reference.md"
→ Click link to reference.md
→ Look up specific PDF library API
```

**Result**: Deep API reference available if needed, but developer didn't need it for this task!

---

## Complete Example 2: Skill Author Creating a New Skill

### Scenario

**Goal**: Create a "Database Migration" skill for generating safe database migrations with rollback support.

---

### Phase 1: Planning (5 minutes)

**Questions to answer**:

```
Q: What domain does this skill cover?
A: Database migrations (schema changes, data migrations, rollback safety)

Q: What can developers do with this skill?
A: 
- Generate type-safe migrations
- Review migration changes
- Execute migrations with rollback support
- Validate schema compatibility

Q: When should developers use this skill?
A: "Generate migration", "database schema change", "create migration script"

Q: What dependencies does it need?
A: ["prisma", "typescript", "database drivers"]

Q: Should it include scripts?
A: Yes - deterministic migration generation is critical
```

---

### Phase 2: Create Directory Structure (2 minutes)

```bash
mkdir -p .github/copilot-skills/database-migration/scripts
touch .github/copilot-skills/database-migration/SKILL.md
```

---

### Phase 3: Write SKILL.md (10 minutes)

**File: `.github/copilot-skills/database-migration/SKILL.md`**

```yaml
---
name: "Database Migration"
description: "Generate type-safe database migrations with rollback support and change review"
version: "1.0.0"
created: "2025-10-18"
tags: ["database", "migrations", "schema"]
dependencies: ["prisma", "typescript"]
---

# Database Migration

## Overview
[Core description of what the skill enables]

## Core Capabilities
- Generate type-safe migrations from schema changes
- Create rollback instructions automatically
- Validate schema compatibility
- Preview migration changes

## Quick Start
[Minimal example of common task]

## Common Patterns
- Pattern 1: Add column safely
- Pattern 2: Rename table with data mapping
- Pattern 3: Create indexed field

## Bundled Scripts
- `generate-migration.py` - Generate migration files

## Detailed References
- See [patterns.md](./patterns.md) for detailed migration patterns
- See [reference.md](./reference.md) for Prisma migration API reference
```

---

### Phase 4: Create Detail Files (15 minutes)

**File: `.github/copilot-skills/database-migration/patterns.md`**
- Pattern 1: Adding columns safely
- Pattern 2: Renaming tables with data mapping
- Pattern 3: Creating indexed fields
- Pattern 4: Handling enum changes

**File: `.github/copilot-skills/database-migration/reference.md`**
- Prisma migration syntax
- PostgreSQL compatibility
- Rollback procedures

---

### Phase 5: Create Bundled Scripts (10 minutes)

**File: `.github/copilot-skills/database-migration/scripts/generate-migration.py`**

```python
#!/usr/bin/env python3
"""Generate database migration script"""

def main():
    # Generates deterministic migration files
    # Same schema change → same migration generated
    pass
```

---

### Phase 6: Register in index.md (2 minutes)

**Add to `.github/copilot-skills/index.md`**:

```markdown
### Database Migration
**Path**: `.github/copilot-skills/database-migration/SKILL.md`
**Description**: Generate type-safe database migrations with rollback support and change review
**When to use**: Schema changes, data migrations, database updates
**Tags**: `database`, `migrations`, `schema`
```

---

### Phase 7: Validate with Compliance Checklist (5 minutes)

Run `.specify/checklists/skill-compliance-checklist.md`:
- ✅ Progressive Disclosure: SKILL.md readable in <3 minutes
- ✅ File-Based Organization: Directory structure correct
- ✅ Dynamic Discovery: Metadata clear in index.md
- ✅ Deterministic Execution: Script produces consistent output
- ✅ Composability: Clear boundaries, no circular dependencies

**Status**: ✅ APPROVED

---

### Phase 8: Create PR and Merge

```bash
git add .github/copilot-skills/database-migration/
git commit -m "feat: Add database-migration skill

- Generate type-safe database migrations
- Automatic rollback instructions
- Schema compatibility validation
- Bundled script for deterministic generation"

git push origin feature/add-database-migration-skill
# Create PR, get review, merge
```

---

## Complete Example 3: Progressive Disclosure in Action

### User Opens hello-skill Index Entry

```
Metadata layer (10 seconds):
"Example skill demonstrating discovery, progressive loading, 
and bundled script patterns"

Time: 10 seconds
```

---

### User Opens SKILL.md

```
Core capabilities layer (3 minutes):
- Demonstrate skill discovery workflow
- Show YAML frontmatter metadata format
- Link to detail files for deeper information
- Reference bundled scripts for deterministic operations
- Explain progressive disclosure pattern

Time: 3 minutes total (cumulative)
```

---

### User Opens patterns.md

```
Pattern details layer (5 minutes):
- Pattern 1: Reference Skill (No Scripts)
- Pattern 2: Skill with Utilities (Scripts)
- Pattern 3: Complex Multi-Topic Skill

Time: 8 minutes total (cumulative)
```

---

### User Opens reference.md

```
Deep reference layer (10 minutes):
- Architecture philosophy
- Design decisions
- Implementation details
- Validation checklist

Time: 18 minutes total (cumulative)
```

---

### Key Insight

**Without Progressive Disclosure** (monolithic):
- Single 18,000 word document
- User reads it all whether they need it or not
- Context bloat

**With Progressive Disclosure** (skills):
- User reads 1,500 word SKILL.md first (3 minutes)
- If they need patterns: Read 2,000 word patterns.md (+5 minutes)
- If they need reference: Read 5,000 word reference.md (+10 minutes)
- Total: User reads only what they need (3-18 minutes as needed)

**Context Savings**: 60%+ reduction on average

---

## Complete Example 4: Cross-Skill Workflow

### Task

**Developer**: "I need to generate a financial report as a PDF with branded styling"

---

### Solution Using Skill Composition

**Step 1**: Developer mentions task  
**Step 2**: Copilot recognizes it needs multiple skills:
1. Financial Reporting skill → Generate report data
2. PDF Building skill → Convert to PDF
3. Brand Guidelines skill → Apply styling

**Step 3**: Developer navigates skills in sequence:
1. Open `financial-reporting/SKILL.md`
2. Generate report data using script
3. Open `pdf-building/SKILL.md`
4. Convert report to PDF
5. Open `brand-guidelines/SKILL.md`
6. Apply styling and branding

**Result**: Complex workflow using 3 coordinated skills, each focused on single domain

---

## Skills Architecture Benefits Demonstrated

### From Example 1 (Discovery):
✅ Developers find skills quickly through metadata  
✅ Index.md enables fast scanning  
✅ Clear descriptions help match task to skill  

### From Example 2 (Creation):
✅ Following templates, new skills created in <1 hour  
✅ Compliance checklist ensures quality  
✅ Structure is consistent across all skills  

### From Example 3 (Progressive Loading):
✅ Developers read only what they need  
✅ SKILL.md sufficient for most use cases  
✅ Detail files available when needed  
✅ 60%+ context savings vs. monolithic  

### From Example 4 (Composition):
✅ Complex workflows use multiple skills  
✅ Clear boundaries prevent skill bloat  
✅ Skills can work together for sophisticated features  

---

**Last Updated**: October 18, 2025  
**Version**: 1.0.0
