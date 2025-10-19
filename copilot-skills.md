# Replicating Claude Skills with GitHub Copilot

## Overview

This document explains how to replicate Anthropic's **Agent Skills** architecture using GitHub Copilot's `.github/` directory structure. Claude Skills use progressive disclosure and organized file structures to give AI agents specialized capabilities without overwhelming the context window.

## What Are Claude Skills?

Claude Skills are organized packages of instructions, code, and resources that AI agents can:
- **Discover dynamically** through metadata (name + description)
- **Load progressively** only when relevant to the current task
- **Execute deterministically** using bundled scripts and tools
- **Navigate hierarchically** through linked documentation files

### Core Design Principles

1. **Progressive Disclosure**: Load information in layers (metadata → core instructions → detailed references)
2. **File-Based Organization**: Skills are just directories with a `SKILL.md` file
3. **Dynamic Discovery**: Agents scan metadata to know what skills exist
4. **Deterministic Execution**: Include executable scripts for repeatable operations
5. **Composability**: Skills can be mixed and matched per project

## Architecture Comparison

| Claude Skills | GitHub Copilot Equivalent |
|--------------|---------------------------|
| `SKILL.md` with YAML frontmatter | `.github/copilot-skills/{skill-name}.md` with frontmatter |
| Metadata in system prompt | Listed in `.github/copilot-skills/index.md` |
| Linked files (`reference.md`, `forms.md`) | Cross-referenced `.md` files in skill directory |
| Bundled Python/JS scripts | Scripts in `.github/copilot-skills/{skill-name}/scripts/` |
| Progressive loading via filesystem tools | Copilot reads files on-demand when referenced |

## Implementation: `.github/copilot-skills/` Structure

### Directory Layout

```
.github/
├── copilot-instructions.md          # Main workspace instructions (existing)
├── copilot-skills/
│   ├── index.md                      # Skills registry (metadata only)
│   ├── pdf-handling/
│   │   ├── SKILL.md                  # Core PDF skill instructions
│   │   ├── forms.md                  # Form-filling specific instructions
│   │   ├── reference.md              # PDF library reference
│   │   └── scripts/
│   │       └── extract_form_fields.py
│   ├── financial-reporting/
│   │   ├── SKILL.md
│   │   ├── templates.md
│   │   └── scripts/
│   │       ├── calculate_ratios.py
│   │       └── generate_report.py
│   ├── database-migration/
│   │   ├── SKILL.md
│   │   ├── patterns.md
│   │   └── scripts/
│   │       └── generate_migration.sh
│   └── compliance-tracking/
│       ├── SKILL.md
│       ├── texas-licensing.md
│       └── calculations.md
```

## Skill File Format

### 1. Index File (`.github/copilot-skills/index.md`)

The index provides lightweight metadata that Copilot can scan to discover available skills:

```markdown
# Copilot Skills Registry

Available skills for this workspace. Copilot can load these skills on-demand when relevant to the current task.

## PDF Handling
**Path**: `.github/copilot-skills/pdf-handling/SKILL.md`
**Description**: Extract text, fill forms, and manipulate PDF documents programmatically.
**When to use**: PDF parsing, form extraction, document generation

## Financial Reporting
**Path**: `.github/copilot-skills/financial-reporting/SKILL.md`
**Description**: Generate financial reports, calculate key ratios, and format business documents.
**When to use**: Creating financial statements, ratio analysis, board reports

## Database Migration
**Path**: `.github/copilot-skills/database-migration/SKILL.md`
**Description**: Generate type-safe database migrations with rollback support.
**When to use**: Schema changes, data migrations, Prisma schema updates

## Compliance Tracking
**Path**: `.github/copilot-skills/compliance-tracking/SKILL.md`
**Description**: Texas trade licensing logic, expiration tracking, and compliance calculations.
**When to use**: License validation, insurance checks, compliance dashboard logic
```

### 2. Skill File Format (`.github/copilot-skills/{skill-name}/SKILL.md`)

Each skill follows this structure with YAML frontmatter:

```markdown
---
name: "PDF Handling"
description: "Extract text, fill forms, and manipulate PDF documents"
version: "1.0"
created: "2025-10-18"
tags: ["documents", "forms", "pdf"]
dependencies: ["pypdf2", "pdfplumber"]
---

# PDF Handling Skill

## Overview
This skill provides capabilities for reading, parsing, and manipulating PDF documents, including form field extraction and programmatic form filling.

## Core Capabilities
- Extract text content from PDFs
- Parse form fields and values
- Fill PDF forms programmatically
- Extract tables and structured data

## Quick Start

### Extracting Form Fields
To extract all form fields from a PDF:
```python
# Use the bundled script
python .github/copilot-skills/pdf-handling/scripts/extract_form_fields.py input.pdf
```

### Reading PDF Content
```python
import pdfplumber
with pdfplumber.open("document.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```

## Detailed Instructions

For form-specific operations, see [forms.md](./forms.md)
For PDF library API reference, see [reference.md](./reference.md)

## Common Patterns

### Pattern 1: Extract All Text
When the user needs full text extraction, use pdfplumber for better accuracy.

### Pattern 2: Fill Government Forms
Government forms require exact field names. Always extract field names first before attempting to fill.

## Error Handling
- Handle password-protected PDFs gracefully
- Validate form field names exist before filling
- Check PDF version compatibility
```

### 3. Linked Detail Files

**`forms.md`** - Loaded only when form operations are needed:
```markdown
# PDF Form Handling

## Form Field Extraction
Use the bundled script for reliable extraction:
```bash
python .github/copilot-skills/pdf-handling/scripts/extract_form_fields.py input.pdf --format json
```

## Filling Forms Programmatically
[Detailed instructions...]

## Common Form Types
- IRS Tax Forms (W-2, 1099)
- Government Applications
- Medical Forms
```

**`reference.md`** - API documentation loaded as reference:
```markdown
# PDF Library Reference

## PyPDF2 API
[Comprehensive API documentation...]

## pdfplumber API
[Comprehensive API documentation...]
```

## Usage Patterns

### Pattern 1: Copilot Discovers Skills Automatically
When you start a task, mention it naturally:
```
User: "I need to extract form fields from this PDF"
Copilot: [Internally checks .github/copilot-skills/index.md]
Copilot: [Finds PDF Handling skill is relevant]
Copilot: [Loads .github/copilot-skills/pdf-handling/SKILL.md]
Copilot: [Suggests using the bundled script]
```

### Pattern 2: Explicit Skill Reference
You can explicitly reference a skill:
```
User: "Using the PDF handling skill, extract all fields from form.pdf"
```

### Pattern 3: Progressive Loading
```
User: "Fill out this government PDF form"
Copilot: [Loads pdf-handling/SKILL.md]
Copilot: [Sees reference to forms.md for form-specific instructions]
Copilot: [Loads pdf-handling/forms.md for detailed form-filling steps]
```

## Best Practices for Authoring Skills

### 1. Start with Metadata
Write clear, specific names and descriptions. This is what Copilot uses to decide relevance.

```yaml
---
name: "Texas Trade Licensing"  # ✅ Specific
description: "Calculate license status, expiration warnings, and compliance checks for Texas service trades"  # ✅ Descriptive

# vs

name: "Licensing"  # ❌ Too vague
description: "Handle licenses"  # ❌ Not descriptive enough
---
```

### 2. Structure for Progressive Disclosure
Keep `SKILL.md` lean with core concepts. Move details to linked files:
```markdown
## Common Operations
- License validation
- Expiration checking
- Compliance calculations

For Texas-specific license requirements, see [texas-licensing.md](./texas-licensing.md)
For calculation formulas, see [calculations.md](./calculations.md)
```

### 3. Include Executable Scripts
When operations should be deterministic:
```markdown
## Calculating License Expiration Status

Use the bundled script for consistent results:
```bash
node .github/copilot-skills/compliance-tracking/scripts/check-license-status.js
```

This ensures the same logic is applied across different contexts.
```

### 4. Document Dependencies
List required libraries/tools so Copilot knows what's available:
```yaml
dependencies: ["prisma", "date-fns", "zod"]
```

### 5. Provide Code Patterns
Show Copilot how to accomplish common tasks:
```markdown
## Pattern: Validating Trade License

```typescript
// Standard pattern for license validation
const status = calculateLicenseStatus(license.expiresOn, new Date());
if (status === 'EXPIRED') {
  // Show compliance warning
}
```
```

## Example: Service Industry SaaS Skills

### Compliance Tracking Skill
```markdown
---
name: "Texas Trade Compliance"
description: "License validation, expiration tracking, and compliance calculations for Texas service trades"
version: "1.0"
tags: ["compliance", "licensing", "texas", "regulations"]
dependencies: ["prisma", "date-fns"]
---

# Texas Trade Compliance Skill

## Overview
Handles all compliance-related logic for Texas service industry businesses, including license validation, insurance tracking, and expiration warnings.

## Core Capabilities
- Calculate license status (VALID, EXPIRED, MISSING)
- Determine which trades require state licenses
- Generate compliance warnings 30 days before expiration
- Validate insurance policy coverage

## License Status Logic

```typescript
// Standard pattern used throughout the codebase
function calculateLicenseStatus(expiresOn: Date | null, today: Date): Status {
  if (!expiresOn) return 'MISSING';
  if (expiresOn < today) return 'EXPIRED';
  return 'VALID';
}
```

## Trade Categories

### REQUIRES_STATE_LICENSE
These trades MUST have a license recorded during onboarding:
- PLUMBING
- ELECTRICAL
- HVAC
- PEST_CONTROL
- LOCKSMITH
- SECURITY_SYSTEM_INSTALL

### LOCAL_OR_OPTIONAL
These trades have optional licensing or local permits:
- LAWN_CARE
- LANDSCAPING
- ROOFING
[... see full list in texas-licensing.md]

## Detailed References
- [Texas-specific license requirements](./texas-licensing.md)
- [Expiration calculation formulas](./calculations.md)
```

## Integration with Main Copilot Instructions

Your main `.github/copilot-instructions.md` should reference the skills system:

```markdown
# Project Instructions

[... your existing instructions ...]

## Skills System

This project uses a skills-based architecture for specialized knowledge. Skills are located in `.github/copilot-skills/`.

To discover available skills, check `.github/copilot-skills/index.md`.

When working on tasks related to:
- PDF handling → Reference the PDF handling skill
- Financial reports → Reference the financial reporting skill
- Database changes → Reference the database migration skill
- Compliance logic → Reference the Texas trade compliance skill

Skills contain executable scripts and detailed patterns. Load skills progressively as needed for the current task.
```

## Advantages Over Monolithic Instructions

| Approach | Context Usage | Maintainability | Discoverability |
|----------|---------------|-----------------|-----------------|
| **Monolithic** (all in copilot-instructions.md) | Always loads everything | Hard to update specific domains | Mixed together, hard to find |
| **Skills-based** (this approach) | Loads only relevant skills | Each skill is independent | Clear registry with metadata |

### Token Efficiency Example

**Monolithic approach**: 50KB instructions loaded every time (includes PDF, finance, compliance, DB patterns)

**Skills approach**: 
- Base: 5KB (copilot-instructions.md + index.md metadata)
- Task 1 (PDF work): +10KB (pdf-handling skill)
- Task 2 (Compliance): +8KB (compliance skill)
- Task 3 (Finance report): +12KB (financial-reporting skill)

Only the relevant skill is loaded per task.

## Migration Strategy

### Phase 1: Identify Skill Candidates
Review your current instructions for distinct domains:
- Document processing
- Domain-specific business logic
- Specialized calculations
- Framework-specific patterns

### Phase 2: Create Skill Files
Extract each domain into a skill:
1. Create directory structure
2. Write SKILL.md with metadata
3. Move domain-specific content
4. Add any executable scripts
5. Link to detailed reference files

### Phase 3: Update Index
Add metadata entry to `index.md` for each skill.

### Phase 4: Reference from Main Instructions
Update copilot-instructions.md to point to the skills system.

### Phase 5: Test and Iterate
- Try tasks that should trigger each skill
- Observe if Copilot loads the right skills
- Refine metadata descriptions for better matching

## Advanced Patterns

### Cross-Skill References
Skills can reference each other:
```markdown
## Database Schema Changes
When updating compliance-related schema, also reference the [Texas Trade Compliance skill](../compliance-tracking/SKILL.md) for business logic implications.
```

### Skill Composition
Combine multiple skills for complex workflows:
```markdown
## Generating Compliance Reports (PDF)
1. Load Texas Trade Compliance skill for license data
2. Load Financial Reporting skill for formatting
3. Load PDF Handling skill for output generation
```

### Version Management
Track skill versions in frontmatter:
```yaml
version: "2.1"
changelog:
  - "2.1: Added electronic signature support"
  - "2.0: Refactored for pdfplumber"
  - "1.0: Initial release"
```

## Limitations & Considerations

### Differences from Claude Skills

| Feature | Claude Skills | GitHub Copilot |
|---------|---------------|----------------|
| **Automatic discovery** | Yes (Bash tool reads files) | Manual (user mentions or obvious context) |
| **Dynamic loading** | Yes (code execution tools) | Partial (loads when file is opened/referenced) |
| **Script execution** | Direct via code execution | Copilot suggests running scripts |
| **Context management** | Automatic via progressive disclosure | Relies on user navigation + file references |

### GitHub Copilot Adaptations

Since Copilot doesn't have automatic filesystem navigation:
1. **Explicit references**: Link to files explicitly in SKILL.md
2. **Contextual cues**: Mention skill names in task descriptions
3. **Index scanning**: User can open index.md to see available skills
4. **File navigation**: Open skill files when starting related work

### Best Results
- Open `.github/copilot-skills/index.md` at the start of a session
- Mention skill names in your prompts: "Using the compliance skill..."
- Keep SKILL.md files focused and scannable
- Use clear, searchable section headers

## Example Use Cases

### Use Case 1: New Developer Onboarding
New developer needs to understand compliance logic:
1. Opens `.github/copilot-skills/index.md`
2. Finds "Texas Trade Compliance" skill
3. Opens `compliance-tracking/SKILL.md`
4. Sees core patterns and links to detailed references
5. Can ask Copilot questions with skill context loaded

### Use Case 2: Adding New Feature
Developer building invoice PDF generation:
1. Opens `pdf-handling/SKILL.md`
2. Sees bundled script for PDF generation
3. Copilot suggests using established patterns
4. References `templates.md` for invoice layout
5. Uses `scripts/generate_pdf.py` for consistent output

### Use Case 3: Bug Fix
Developer fixing license expiration calculation:
1. Opens `compliance-tracking/SKILL.md`
2. Sees standard calculation function
3. Loads `calculations.md` for formula details
4. Copilot suggests fixes aligned with documented patterns
5. Runs bundled test script to verify

## Getting Started Checklist

- [ ] Create `.github/copilot-skills/` directory
- [ ] Create `index.md` skills registry
- [ ] Identify 2-3 skill candidates from existing code
- [ ] Create first skill with SKILL.md + frontmatter
- [ ] Add executable script if applicable
- [ ] Add entry to index.md
- [ ] Reference skills system in main copilot-instructions.md
- [ ] Test by opening index and asking Copilot about a skill
- [ ] Iterate on metadata descriptions for better relevance

## Resources

- [Claude Skills Engineering Blog](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- [Claude Skills Documentation](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
- [Claude Skills Cookbook](https://github.com/anthropics/claude-cookbooks/tree/main/skills)
- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)

---

**Last Updated**: October 18, 2025
**Version**: 1.0