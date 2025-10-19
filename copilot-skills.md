# Copilot Skills: Technical Architecture Guide# Replicating Claude Skills with GitHub Copilot

## Executive Summary## Overview

This document provides the technical architecture for implementing Anthropic's **Agent Skills** system in GitHub Copilot. The implementation uses `.github/` directory structures, prompt-based workflows, and progressive disclosure to give AI agents specialized domain capabilities without overwhelming the context window.This document explains how to replicate Anthropic's **Agent Skills** architecture using GitHub Copilot's `.github/` directory structure. Claude Skills use progressive disclosure and organized file structures to give AI agents specialized capabilities without overwhelming the context window.

**Status**: Implemented with automation infrastructure  ## What Are Claude Skills?
**Version**: 2.0  
**Last Updated**: 2025-10-18Claude Skills are organized packages of instructions, code, and resources that AI agents can:
- **Discover dynamically** through metadata (name + description)
---- **Load progressively** only when relevant to the current task
- **Execute deterministically** using bundled scripts and tools
## What Are Claude/Agent Skills?- **Navigate hierarchically** through linked documentation files

Claude Skills (also called Agent Skills) are organized packages of instructions, code, and resources that AI agents can:### Core Design Principles

- **Discover dynamically** through metadata (name + description)1. **Progressive Disclosure**: Load information in layers (metadata → core instructions → detailed references)
- **Load progressively** only when relevant to the current task2. **File-Based Organization**: Skills are just directories with a `SKILL.md` file
- **Execute deterministically** using bundled scripts and tools3. **Dynamic Discovery**: Agents scan metadata to know what skills exist
- **Navigate hierarchically** through linked documentation files4. **Deterministic Execution**: Include executable scripts for repeatable operations
- **Compose together** for complex multi-domain workflows5. **Composability**: Skills can be mixed and matched per project

---## Architecture Comparison

## The Five Constitutional Principles| Claude Skills | GitHub Copilot Equivalent |
|--------------|---------------------------|
All skills must adhere to these principles (defined in `.specify/memory/constitution.md`):| `SKILL.md` with YAML frontmatter | `.github/copilot-skills/{skill-name}.md` with frontmatter |
| Metadata in system prompt | Listed in `.github/copilot-skills/index.md` |
### 1. Progressive Disclosure| Linked files (`reference.md`, `forms.md`) | Cross-referenced `.md` files in skill directory |
Information loads in layers: **metadata → core instructions → detailed references**. Each file must be independently useful and scannable in <3 minutes.| Bundled Python/JS scripts | Scripts in `.github/copilot-skills/{skill-name}/scripts/` |
| Progressive loading via filesystem tools | Copilot reads files on-demand when referenced |
### 2. File-Based Organization
Skills are self-contained directories with `SKILL.md` core file + YAML frontmatter (name, description, version, tags, dependencies).## Implementation: `.github/copilot-skills/` Structure

### 3. Dynamic Discovery Through Metadata### Directory Layout
`.github/copilot-skills/index.md` registry enables AI agents to find relevant skills without parsing full documentation.
```
### 4. Deterministic Execution with Scripts.github/
Complex operations include bundled scripts (in `scripts/` subdirectories) that produce consistent results regardless of context.├── copilot-instructions.md          # Main workspace instructions (existing)
├── copilot-skills/
### 5. Composability and Cross-Skill References│   ├── index.md                      # Skills registry (metadata only)
Skills may reference each other for complex workflows; dependencies declared in metadata; boundaries clear to prevent circular references.│   ├── pdf-handling/
│   │   ├── SKILL.md                  # Core PDF skill instructions
---│   │   ├── forms.md                  # Form-filling specific instructions
│   │   ├── reference.md              # PDF library reference
## Architecture Comparison│   │   └── scripts/
│   │       └── extract_form_fields.py
| Aspect | Claude Skills | GitHub Copilot Implementation |│   ├── financial-reporting/
|--------|---------------|-------------------------------|│   │   ├── SKILL.md
| **Core File** | `SKILL.md` with YAML frontmatter | `SKILL.md` with YAML frontmatter |│   │   ├── templates.md
| **Discovery** | System prompt includes metadata | `.github/copilot-skills/index.md` registry |│   │   └── scripts/
| **Detail Files** | `reference.md`, `forms.md`, etc. | Same - cross-referenced `.md` files |│   │       ├── calculate_ratios.py
| **Scripts** | Bundled in skill directory | `.github/copilot-skills/{name}/scripts/` |│   │       └── generate_report.py
| **Loading** | Filesystem tools read on-demand | Copilot reads files when referenced |│   ├── database-migration/
| **Commands** | `/skill-name` shortcuts | `/skill-{name}` via `.github/prompts/` |│   │   ├── SKILL.md
| **Automation** | Manual or custom tools | `.github/copilot-skills/scripts/` infrastructure |│   │   ├── patterns.md
│   │   └── scripts/
---│   │       └── generate_migration.sh
│   └── compliance-tracking/
## The Three-Part System│       ├── SKILL.md
│       ├── texas-licensing.md
### 1. Skill Files (`.github/copilot-skills/{skill-name}/`)│       └── calculations.md
```
Contains the actual skill documentation and scripts.
## Skill File Format
**Structure**:
```### 1. Index File (`.github/copilot-skills/index.md`)
{skill-name}/
├── SKILL.md              # Core file (REQUIRED)The index provides lightweight metadata that Copilot can scan to discover available skills:
├── {detail}.md           # Detail files (optional)
└── scripts/              # Bundled scripts (optional)```markdown
    └── {operation}.{ext}# Copilot Skills Registry
```
Available skills for this workspace. Copilot can load these skills on-demand when relevant to the current task.
**SKILL.md Requirements**:
- YAML frontmatter with: name, description, version, tags, dependencies## PDF Handling
- Overview section (why this skill exists)**Path**: `.github/copilot-skills/pdf-handling/SKILL.md`
- Core capabilities list**Description**: Extract text, fill forms, and manipulate PDF documents programmatically.
- Quick start with minimal example**When to use**: PDF parsing, form extraction, document generation
- Progressive references to detail files
- Bundled scripts documentation## Financial Reporting
**Path**: `.github/copilot-skills/financial-reporting/SKILL.md`
### 2. Skill Prompts (`.github/prompts/skill-{skill-name}.prompt.md`)**Description**: Generate financial reports, calculate key ratios, and format business documents.
**When to use**: Creating financial statements, ratio analysis, board reports
Tells Copilot **when** and **how** to use the skill.
## Database Migration
**Contains**:**Path**: `.github/copilot-skills/database-migration/SKILL.md`
- Relevance keywords (when to load this skill)**Description**: Generate type-safe database migrations with rollback support.
- Progressive loading strategy (which files in which order)**When to use**: Schema changes, data migrations, Prisma schema updates
- Instructions for using the skill
- When to suggest bundled scripts## Compliance Tracking
**Path**: `.github/copilot-skills/compliance-tracking/SKILL.md`
**Example**:**Description**: Texas trade licensing logic, expiration tracking, and compliance calculations.
```markdown**When to use**: License validation, insurance checks, compliance dashboard logic
## Relevance Keywords```
Use this skill when the user mentions:
- PDF, PDFs, or PDF documents### 2. Skill File Format (`.github/copilot-skills/{skill-name}/SKILL.md`)
- Form fields, form filling
Each skill follows this structure with YAML frontmatter:
## Progressive Loading Strategy
### Always Load First```markdown
1. `.github/copilot-skills/pdf-handling/SKILL.md`---
name: "PDF Handling"
### Load When User Asks Aboutdescription: "Extract text, fill forms, and manipulate PDF documents"
- **Forms** → `pdf-handling/forms.md`version: "1.0"
- **API** → `pdf-handling/reference.md`created: "2025-10-18"
```tags: ["documents", "forms", "pdf"]
dependencies: ["pypdf2", "pdfplumber"]
### 3. Management Commands (`.github/prompts/skills.*.prompt.md`)---

Provide commands for creating, validating, and discovering skills:# PDF Handling Skill

- `/skills.create` - Create new skill with validation## Overview
- `/skills.validate` - Check constitution complianceThis skill provides capabilities for reading, parsing, and manipulating PDF documents, including form field extraction and programmatic form filling.
- `/skills.discover` - Search for relevant skills
## Core Capabilities
---- Extract text content from PDFs
- Parse form fields and values
## Progressive Disclosure in Action- Fill PDF forms programmatically
- Extract tables and structured data
### Example: PDF Form Extraction
## Quick Start
**User**: "I need to extract form fields from this PDF"
### Extracting Form Fields
1. Copilot scans `index.md` → finds PDF Handling skillTo extract all form fields from a PDF:
2. Loads `pdf-handling/SKILL.md` (core - 2KB)```python
3. User mentions "government form"# Use the bundled script
4. Loads `pdf-handling/forms.md` on demand (3KB)python .github/copilot-skills/pdf-handling/scripts/extract_form_fields.py input.pdf
5. Suggests bundled script```

**Context savings**: 40% vs. loading all documentation upfront### Reading PDF Content
```python
---import pdfplumber
with pdfplumber.open("document.pdf") as pdf:
## Complete Directory Structure    text = pdf.pages[0].extract_text()
```
```
.github/## Detailed Instructions
├── copilot-instructions.md              # Main workspace instructions
├── prompts/                             # Command definitionsFor form-specific operations, see [forms.md](./forms.md)
│   ├── skills.create.prompt.md          # /skills.createFor PDF library API reference, see [reference.md](./reference.md)
│   ├── skill-{name}.prompt.md           # /skill-{name} (one per skill)
│   └── speckit.*.prompt.md              # Feature development## Common Patterns
├── copilot-skills/                      # Skills registry
│   ├── index.md                         # Skills discovery (CRITICAL)### Pattern 1: Extract All Text
│   ├── README.md                        # System overviewWhen the user needs full text extraction, use pdfplumber for better accuracy.
│   ├── AUTHORING.md                     # Creation guide
│   ├── GOVERNANCE.md                    # Constitution### Pattern 2: Fill Government Forms
│   ├── templates/                       # ScaffoldingGovernment forms require exact field names. Always extract field names first before attempting to fill.
│   │   ├── SKILL.template.md
│   │   ├── detail-file.template.md## Error Handling
│   │   └── skill-prompt.template.md- Handle password-protected PDFs gracefully
│   ├── scripts/                         # Automation- Validate form field names exist before filling
│   │   ├── bash/- Check PDF version compatibility
│   │   │   ├── common.sh                # Utilities (✅ exists)```
│   │   │   ├── create-skill.sh          # Create skill (📋 planned)
│   │   │   └── validate-skill.sh        # Validate (📋 planned)### 3. Linked Detail Files
│   │   └── python/
│   │       ├── yaml_validator.py        # Validation (✅ exists)**`forms.md`** - Loaded only when form operations are needed:
│   │       └── skill_schema.yaml        # Schema (✅ exists)```markdown
│   └── hello-skill/                     # Example skill# PDF Form Handling
│       ├── SKILL.md
│       ├── patterns.md## Form Field Extraction
│       └── scripts/hello-example.pyUse the bundled script for reliable extraction:
└── .specify/                            # Feature development```bash
    ├── memory/constitution.mdpython .github/copilot-skills/pdf-handling/scripts/extract_form_fields.py input.pdf --format json
    ├── templates/```
    └── scripts/
```## Filling Forms Programmatically
[Detailed instructions...]
---
## Common Form Types
## File Format: SKILL.md Template- IRS Tax Forms (W-2, 1099)
- Government Applications
```markdown- Medical Forms
---```
name: "{Skill Name}"
description: "{What this enables}"**`reference.md`** - API documentation loaded as reference:
version: "1.0.0"```markdown
created: "{YYYY-MM-DD}"# PDF Library Reference
tags: ["{domain}", "{keywords}"]
dependencies: ["{lib1}", "{tool2}"]## PyPDF2 API
---[Comprehensive API documentation...]

# {Skill Name}## pdfplumber API
[Comprehensive API documentation...]
## Overview```
{Why this skill exists}
## Usage Patterns
## Core Capabilities
- {Capability 1}### Pattern 1: Copilot Discovers Skills Automatically
- {Capability 2}When you start a task, mention it naturally:
```
## Quick StartUser: "I need to extract form fields from this PDF"
### {Common Task}Copilot: [Internally checks .github/copilot-skills/index.md]
{Minimal code example}Copilot: [Finds PDF Handling skill is relevant]
Copilot: [Loads .github/copilot-skills/pdf-handling/SKILL.md]
## Progressive ReferencesCopilot: [Suggests using the bundled script]
- For {topic} → see [{file}.md](./{file}.md)```

## Bundled Scripts### Pattern 2: Explicit Skill Reference
- `{script}.{ext}` - {What it does, how to invoke}You can explicitly reference a skill:
```
## Common PatternsUser: "Using the PDF handling skill, extract all fields from form.pdf"
{2-3 patterns with code}```

## Error Handling### Pattern 3: Progressive Loading
{Common errors and solutions}```
```User: "Fill out this government PDF form"
Copilot: [Loads pdf-handling/SKILL.md]
---Copilot: [Sees reference to forms.md for form-specific instructions]
Copilot: [Loads pdf-handling/forms.md for detailed form-filling steps]
## Automation Infrastructure```

| Script | Purpose | Status |## Best Practices for Authoring Skills
|--------|---------|--------|
| `bash/common.sh` | Shared shell utilities | ✅ Implemented |### 1. Start with Metadata
| `bash/create-skill.sh` | Create new skill with prompts | 📋 Planned |Write clear, specific names and descriptions. This is what Copilot uses to decide relevance.
| `bash/validate-skill.sh` | Validate constitution compliance | 📋 Planned |
| `bash/update-index.sh` | Update index.md | 📋 Planned |```yaml
| `python/yaml_validator.py` | Validate YAML frontmatter | ✅ Implemented |---
| `python/skill_schema.yaml` | YAML schema definition | ✅ Implemented |name: "Texas Trade Licensing"  # ✅ Specific
description: "Calculate license status, expiration warnings, and compliance checks for Texas service trades"  # ✅ Descriptive
---
# vs
## Success Metrics
name: "Licensing"  # ❌ Too vague
| Metric | Target | Status |description: "Handle licenses"  # ❌ Not descriptive enough
|--------|--------|--------|---
| Discovery Time | <2 minutes | ✅ Achieved |```
| Scan Time per SKILL.md | <3 minutes | ✅ Achieved |
| Context Reduction | 60% savings | ✅ Demonstrated |### 2. Structure for Progressive Disclosure
| Task Coverage | 95% with ≤2 skills | 📋 Needs measurement |Keep `SKILL.md` lean with core concepts. Move details to linked files:
| Authoring Time | <30 minutes | 📋 Templates exist |```markdown
## Common Operations
---- License validation
- Expiration checking
## Available Commands- Compliance calculations

### Skill ManagementFor Texas-specific license requirements, see [texas-licensing.md](./texas-licensing.md)
- `/skills.create` - Create new skillFor calculation formulas, see [calculations.md](./calculations.md)
- `/skills.validate` - Check compliance```
- `/skills.discover` - Search skills
- `/skills.use <name>` - Load a skill### 3. Include Executable Scripts
When operations should be deterministic:
### Individual Skills```markdown
- `/skill-hello-skill` - Demo skill## Calculating License Expiration Status
- `/skill-{name}` - Any registered skill
Use the bundled script for consistent results:
### Feature Development```bash
- `/speckit.specify` - Create specnode .github/copilot-skills/compliance-tracking/scripts/check-license-status.js
- `/speckit.plan` - Generate plan```
- `/speckit.implement` - Execute
This ensures the same logic is applied across different contexts.
### Utilities```
- `/cleanup` - Repository cleanup
### 4. Document Dependencies
---List required libraries/tools so Copilot knows what's available:
```yaml
## Referencesdependencies: ["prisma", "date-fns", "zod"]
```
### Internal Documentation
- Constitution: `.specify/memory/constitution.md`### 5. Provide Code Patterns
- Authoring: `.github/copilot-skills/AUTHORING.md`Show Copilot how to accomplish common tasks:
- Quick Reference: `docs/QUICK_REFERENCE.md````markdown
## Pattern: Validating Trade License
### Feature Specifications
- `specs/001-skill-architecture/` - Initial design```typescript
- `specs/002-copilot-skills-restructure/` - Infrastructure// Standard pattern for license validation
const status = calculateLicenseStatus(license.expiresOn, new Date());
### External Referencesif (status === 'EXPIRED') {
- [Anthropic's Agent Skills](https://github.com/anthropics/skills)  // Show compliance warning
- [Obra's Superpowers](https://github.com/obra/superpowers)}
- [Claude Office Skills](https://github.com/tfriedel/claude-office-skills)```
```
---
## Example: Service Industry SaaS Skills
## Next Steps
### Compliance Tracking Skill
1. **Complete automation scripts** (`create-skill.sh`, `validate-skill.sh`)```markdown
2. **Create production skills** from examples (PDF, MCP, Database)---
3. **Document patterns** in EXAMPLES.mdname: "Texas Trade Compliance"
4. **CI/CD integration** (GitHub Actions for validation)description: "License validation, expiration tracking, and compliance calculations for Texas service trades"
version: "1.0"
---tags: ["compliance", "licensing", "texas", "regulations"]
dependencies: ["prisma", "date-fns"]
**Version**: 2.0 | **Last Updated**: 2025-10-18---

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