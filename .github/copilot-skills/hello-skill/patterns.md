# Hello Skill - Patterns

This detail file demonstrates three pattern types for organizing skills in the Copilot Skills Architecture.

## Pattern Type 1: Reference Skill (No Scripts)

**When to use**: Guidance, best practices, architectural patterns, learning materials

**Structure**:
```
skill-name/
├── SKILL.md          # Core: capabilities, quick start
├── reference.md      # API documentation, technical details
├── patterns.md       # Common patterns (this file)
└── examples.md       # Code examples
```

**Characteristics**:
- Focus on providing guidance and reference material
- No bundled scripts (or minimal scripts)
- Multiple detail files for different audiences
- SKILL.md is brief quickstart, detail files provide depth

**Examples in the wild**:
- Design pattern skills
- Architecture guidance skills
- Technology tutorial skills
- Best practices skills

**How developers use it**:
1. Read SKILL.md (quick understanding)
2. Link to reference.md for deep dives
3. Link to examples.md to see patterns in action
4. Follow guidance in their own code

---

## Pattern Type 2: Skill with Utilities (Scripts)

**When to use**: Operations needing determinism, calculations, data transformations, automation

**Structure**:
```
skill-name/
├── SKILL.md          # Core: capabilities, quick start
├── forms.md          # Use-case specific guidance
└── scripts/
    ├── operation-1.py
    ├── operation-2.py
    └── helper.sh
```

**Characteristics**:
- Bundles executable scripts for deterministic operations
- Scripts documented in SKILL.md
- Detail files explain when/why to use scripts
- Emphasis on repeatable, consistent results

**Examples in the wild**:
- Compliance tracking (calculate license status consistently)
- Financial calculations (compute ratios, generate reports)
- Data extraction (parse files deterministically)
- Database migrations (generate migration scripts)

**How developers use it**:
1. Read SKILL.md to understand operations
2. Run bundled script for deterministic result
3. Link to forms.md when they need domain-specific guidance
4. Scripts ensure same logic applies everywhere

**Example: License Status Calculation**
```bash
# Always get consistent result
node .github/copilot-skills/compliance/scripts/check-license-status.js \
  --license-id "TX-123456" \
  --expiration "2025-12-31"

# Output:
# {
#   "success": true,
#   "status": "VALID",
#   "days_until_expiration": 74,
#   "warning_days": 30,
#   "needs_renewal": false
# }
```

---

## Pattern Type 3: Complex Multi-Topic Skill

**When to use**: Domain spans multiple related topics, each requiring substantial explanation

**Structure**:
```
skill-name/
├── SKILL.md              # Core: overview, quick start
├── topic-1.md            # Detail: subtopic A (500+ words)
├── topic-2.md            # Detail: subtopic B (500+ words)
├── topic-3.md            # Detail: subtopic C (500+ words)
└── scripts/
    ├── operation-for-topic-1.py
    ├── operation-for-topic-2.py
    └── helper-script.sh
```

**Characteristics**:
- Single skill address multiple related topics
- Each detail file stands alone (doesn't reference other detail files)
- Topic-specific scripts in scripts/ directory
- SKILL.md links to appropriate detail file for each use case

**Examples in the wild**:
- PDF Handling
  - Topic 1: Text extraction patterns
  - Topic 2: Form filling patterns
  - Topic 3: Table extraction patterns
- Financial Reporting
  - Topic 1: Report templates
  - Topic 2: Calculation formulas
  - Topic 3: Output formatting
- Document Processing
  - Topic 1: Word documents
  - Topic 2: Excel spreadsheets
  - Topic 3: PowerPoint presentations

**How developers use it**:
1. Read SKILL.md to understand broad capabilities
2. Choose specific topic based on task
3. Read topic-specific detail file (e.g., topic-1.md)
4. Run corresponding script if needed
5. Never need to read other topic files

**Example: PDF Handling Skills**
```markdown
# PDF Handling Skill

## Core Capabilities
- Extract text content
- Parse form fields
- Extract tables

## Quick Start
See the appropriate detail file:
- [Text Extraction](./text-extraction.md) - Extract readable text from PDFs
- [Form Handling](./form-handling.md) - Extract and fill PDF forms
- [Tables](./tables.md) - Extract tables as structured data
```

---

## Pattern Type Comparison

| Aspect | Reference Only | With Scripts | Multi-Topic |
|--------|---|---|---|
| **Use case** | Guidance, learning | Calculations, operations | Complex domains |
| **Files** | SKILL.md + reference files | SKILL.md + scripts/ | SKILL.md + topic files + scripts/ |
| **Scripts** | No | Yes | Yes |
| **Detail files** | Multiple | One or two | Multiple (one per topic) |
| **Read time** | SKILL.md: 3 min | SKILL.md: 3 min | SKILL.md: 3 min per topic |
| **Example** | Architecture patterns | License checker | PDF handling |

---

## When to Create Each Pattern

### Create "Reference Only" When:
- ✅ Providing guidance or best practices
- ✅ Teaching a concept or technology
- ✅ No need for deterministic operations
- ✅ Multiple reference materials needed

### Create "With Scripts" When:
- ✅ Operations need to be deterministic
- ✅ Same logic used across codebase
- ✅ Calculation or data transformation needed
- ✅ Reproducible results important

### Create "Multi-Topic" When:
- ✅ Domain spans 2+ related sub-domains
- ✅ Each sub-domain needs detailed explanation
- ✅ Different audiences use different topics
- ✅ Clear topic boundaries exist

---

## Detail File Organization

### Within Each Pattern

**Reference Files** (names):
- `reference.md` - API reference, technical details
- `patterns.md` - Common usage patterns (this file)
- `examples.md` - Code examples and walkthroughs
- `troubleshooting.md` - Common issues and solutions

**Topic Files** (names):
- `{topic-name}.md` - One file per topic
- `calculation.md` - Calculation logic and formulas
- `templates.md` - Template files and formats
- `forms.md` - Form-specific patterns

### Key Principle: Independence

Each detail file MUST stand independently:
- ✅ Can be read without reading other files
- ✅ Contains sufficient context
- ✅ Doesn't say "see the previous section" referring to another file

### Bad Example:
```markdown
# Forms

For form field extraction, see the Text Extraction section of text-extraction.md first.
Then follow the patterns in this section...
```

### Good Example:
```markdown
# Forms

## Form Field Extraction

Form fields in PDFs are named data elements defined in the PDF structure.
[Complete explanation of form fields...]

When you want to extract form fields:
1. [Step 1...]
2. [Step 2...]
```

---

## Skill Naming by Pattern

Choose descriptive names:

| Pattern | Skill Name | Why |
|---------|-----------|-----|
| Reference | `architecture-patterns` | Describes what you learn |
| Reference | `typescript-best-practices` | Topic + guidance approach |
| With Scripts | `license-status-checker` | What script does |
| With Scripts | `compliance-tracking` | Domain + operation |
| Multi-Topic | `pdf-handling` | Domain name |
| Multi-Topic | `document-processing` | Umbrella domain |

---

## Example: Building a New "Financial Reporting" Skill

### Which Pattern?

Analysis:
- Multiple topics (templates, calculations, formatting)
- Script needed for calculations (determinism important)
- Different audiences (accountants, executives, developers)

**Decision**: Multi-Topic Pattern (Pattern Type 3)

### Structure

```
financial-reporting/
├── SKILL.md                    # Overview
├── templates.md                # Detail: Report templates
├── calculations.md             # Detail: Financial formulas  
├── formatting.md               # Detail: Output formatting
└── scripts/
    ├── calculate-ratios.py     # Calculate financial ratios deterministically
    └── generate-report.py      # Generate formatted report
```

### SKILL.md Quick Start

```markdown
## Quick Start

Choose your task:

**Generate a standard financial report** → See [templates.md](./templates.md)
```

This structure ensures:
1. New developers find SKILL.md in 3 minutes
2. Templates audience reads templates.md only
3. Finance audience reads calculations.md only
4. Scripts ensure consistent calculations everywhere

---

## Next Steps

- Study `skill-template/` for complete working example
- Read `SKILL.md` files in other skills
- Follow AUTHORING.md guide to create your skill using these patterns

---

**Version**: 1.0.0 | **Last Updated**: October 18, 2025
