# Copilot Skills Architecture - Interaction Contracts

**Date**: October 18, 2025  
**Status**: Phase 1 Design  
**Purpose**: Define how Copilot interacts with the skills system

## Contract 1: Skill Discovery

### User Story 1 - Copilot Discovers Available Skills

**Trigger**: User starts a task that might benefit from a skill

**Copilot Action Sequence**:
```
1. User describes task (e.g., "I need to extract form fields from this PDF")
2. Copilot reads .github/copilot-skills/index.md
3. Copilot scans SkillMetadata entries for matching keywords/description
4. Copilot identifies "pdf-handling" skill as relevant
5. Copilot loads .github/copilot-skills/pdf-handling/SKILL.md
6. Copilot presents core capabilities and suggests next steps
```

**Expected Behavior**:
- Index.md is readable and scannable
- Skill descriptions are specific enough to determine relevance
- Tags enable keyword matching
- SKILL.md loads successfully

**Input**:
- Task description from user (natural language)
- `.github/copilot-skills/index.md` file (SkillsRegistry)

**Output**:
- Identified skill name and path
- Core capabilities from SKILL.md
- Suggested next steps (documentation, scripts, examples)

**Contract Details**:
```
GET .github/copilot-skills/index.md
PARSE SkillMetadata entries
MATCH task keywords against:
  - skill.name
  - skill.description
  - skill.tags
  - skill.when_to_use
RETURN: Top matching skill (if confidence > threshold)
```

**Acceptance Criteria**:
- [ ] Copilot can read index.md within 1 API call
- [ ] Skill descriptions contain enough context for matching
- [ ] Ambiguous tasks return multiple suggestions
- [ ] Skills ranked by relevance (description match > tag match)

---

## Contract 2: Progressive Loading

### User Story 2 - Load Skill Details Progressively

**Trigger**: Copilot identified a skill, user wants to proceed

**Copilot Action Sequence**:
```
Level 1 (Initial):
  1. Copilot has loaded SKILL.md
  2. Copilot displays: Overview + Core Capabilities + Quick Start

Level 2 (Detailed):
  When user says "How do I fill a form?":
  1. Copilot scans SKILL.md for detail file references
  2. Finds reference: "See [forms.md](./forms.md) for form-specific operations"
  3. Copilot loads .github/copilot-skills/{skill-name}/forms.md
  4. Copilot provides focused guidance on form filling

Level 3 (Reference):
  When user says "Show me the API":
  1. Copilot finds: "API reference in [reference.md](./reference.md)"
  2. Loads reference.md
  3. Shows complete API documentation

Level 4 (Execution):
  When user says "Run the extract script":
  1. Copilot finds script in SKILL.md documentation
  2. Suggests command: python .github/copilot-skills/pdf-handling/scripts/extract_form_fields.py
  3. Shows expected output format
```

**Expected Behavior**:
- Each file is independently useful
- SKILL.md contains no more than 100 lines
- Detail files are topic-specific (not mixed concerns)
- Links are explicit and path-correct

**Input**:
- User request (natural language like "how do I...", "show me the API")
- Current skill context (already loaded SKILL.md)
- Requested detail level

**Output**:
- Loaded detail file content
- Focused guidance for user's specific question
- Links to next-level documentation

**Contract Details**:
```
GIVEN: Loaded SKILL.md file
WHEN: User requests specific detail (e.g., "forms", "API", "examples")
THEN:
  1. Scan SKILL.md for reference links (e.g., [forms.md](./forms.md))
  2. Extract matching file path
  3. Load file from .github/copilot-skills/{skill-name}/{file}
  4. Return relevant section to user
```

**Acceptance Criteria**:
- [ ] SKILL.md is scannable within 3 minutes (hard limit: 100 lines)
- [ ] Each detail file has clear section headers
- [ ] Links in SKILL.md use relative paths
- [ ] Each detail file can be read independently
- [ ] Cross-references to other skills are explicit

---

## Contract 3: Script Execution

### User Story 3 - Execute Deterministic Operations

**Trigger**: User asks Copilot to perform an operation (extract, calculate, transform)

**Copilot Action Sequence**:
```
1. User: "Extract form fields from document.pdf"
2. Copilot: Checks SKILL.md for script documentation
3. Found: "Use extract_form_fields.py script for reliable extraction"
4. Command shown: python .github/copilot-skills/pdf-handling/scripts/extract_form_fields.py document.pdf --format json
5. Copilot runs script (if user approves)
6. Script output: { "success": true, "fields": [...] }
7. Copilot presents results to user
```

**Expected Behavior**:
- Scripts are documented with input/output contracts
- Scripts accept command-line arguments
- Scripts produce consistent output for same input
- Error handling is clear and informative

**Input**:
- Task parameters (file name, options, flags)
- Referenced script path
- Execution context (current working directory)

**Output**:
- Script exit code (0 = success, non-zero = error)
- stdout: Results in documented format
- stderr: Detailed error messages if failure

**Contract Details**:
```
SCRIPT CONTRACT:
  Input: Command line args + files
  Output: JSON with { success: bool, data: {}, errors: [] }
  Usage: python .github/copilot-skills/{skill-name}/scripts/{script} [args]
  
EXAMPLE:
  Input: python .../extract_form_fields.py form.pdf --format json
  Output: { "success": true, "fields": [{"name": "field1", "value": "..."}] }
  Error: { "success": false, "errors": ["File not found", "Invalid PDF"] }
```

**Acceptance Criteria**:
- [ ] Scripts are documented in SKILL.md with usage examples
- [ ] Scripts have clear help text (`--help` flag)
- [ ] Output format is documented (JSON/CSV/plain text)
- [ ] Error messages are specific and actionable
- [ ] Scripts run from project root

---

## Contract 4: Cross-Skill Navigation

### User Story 4 - Compose Skills for Complex Workflows

**Trigger**: User needs multiple skills for complex operation

**Copilot Action Sequence**:
```
User: "I need to extract data from a PDF, convert to Excel, and format with our brand colors"

Copilot:
  1. Recognizes multi-skill task
  2. Loads: pdf-handling skill
  3. Loads: xlsx skill (from reference in pdf-handling detail file)
  4. Loads: brand-guidelines skill
  5. Sequences operations:
     - PDF: extract data → outputs JSON
     - XLSX: create spreadsheet from JSON
     - Brand: apply styling and colors
  6. Provides step-by-step workflow
```

**Expected Behavior**:
- Skills document dependencies and cross-references
- Links between skills are explicit
- Skill composition is possible without conflicts
- Skills declare dependencies in metadata

**Input**:
- Current skill context
- Cross-reference found in detail file
- Referenced skill name/path

**Output**:
- Loaded referenced skill
- Connection between skills explained
- Suggested workflow sequence

**Contract Details**:
```
SKILL REFERENCE FORMAT:
  "For Excel export, see [xlsx-handling skill](../xlsx-handling/SKILL.md)"
  
DEPENDENCY DECLARATION:
  dependencies: ["pdf-handling", "xlsx-handling"]
  
COMPOSITION PATTERN:
  Step 1: Use pdf-handling skill to extract
  Step 2: Output format matches xlsx-handling input
  Step 3: Load xlsx-handling to format
  Step 4: Apply brand styling
```

**Acceptance Criteria**:
- [ ] Cross-skill references use consistent markdown link format
- [ ] Skills declare hard dependencies in metadata
- [ ] No circular dependencies possible (manual review)
- [ ] Skill composition workflow is clear and documented

---

## Contract 5: Registry Updates

### Maintenance - Adding/Updating Skills

**Process**:
```
1. Author creates new skill directory: .github/copilot-skills/{skill-name}/
2. Creates SKILL.md with YAML frontmatter and content
3. Adds detail files as needed
4. Creates scripts/ directory with implementations
5. Updates .github/copilot-skills/index.md with entry
6. Opens PR for review

PR Review Checklist:
  - [ ] YAML frontmatter valid and complete
  - [ ] Metadata clear and specific
  - [ ] Skills comply with 5 constitution principles
  - [ ] Detail files focused on single topic
  - [ ] Scripts documented with usage examples
  - [ ] index.md updated with SkillMetadata
  - [ ] No circular dependencies
```

**Expected Behavior**:
- Registry stays current with new skills
- Old skills marked as DEPRECATED when replaced
- Breaking changes documented in version notes
- Registration process is straightforward

**Input**:
- New skill files and structure
- Updated index.md entry
- Version notes (if applicable)

**Output**:
- Merged skill into main branch
- Skill discoverable in next session
- Version history maintained

**Contract Details**:
```
SKILL REGISTRATION:
  1. Create directory: .github/copilot-skills/{kebab-case-name}/
  2. Required: SKILL.md with YAML frontmatter
  3. Optional: detail files (forms.md, reference.md, patterns.md)
  4. Optional: scripts/ directory
  5. Update: index.md with SkillMetadata entry
  6. Compliance: All 5 constitution principles checked
  
VERSION MANAGEMENT:
  - Patch (1.0.0 → 1.0.1): Bug fixes, clarifications
  - Minor (1.0.0 → 1.1.0): New detail files, new scripts, new patterns
  - Major (1.0.0 → 2.0.0): Breaking changes, principle violations fixed
```

**Acceptance Criteria**:
- [ ] New skill discoverable in index.md within 5 minutes
- [ ] All files follow consistent structure
- [ ] Metadata is specific enough for AI discovery
- [ ] No template files or placeholders remain

---

## Implementation Notes

### For Copilot Interaction

1. **File Reading**: All contracts assume Copilot can read Markdown files from `.github/copilot-skills/` directory
2. **Path Resolution**: Use relative paths within skill directories
3. **JSON Parsing**: Scripts output JSON for structured data extraction
4. **Error Handling**: Graceful degradation if files missing (suggest creating)
5. **Context Efficiency**: Progressive loading minimizes context window usage

### For Future Tooling

If tooling is added (CLI, GitHub Actions, VSCode extension), these contracts define the interface:
- Skill discovery API: Read index.md, parse SkillMetadata
- Progressive loading API: Follow markdown links
- Script execution API: Run scripts with documented contracts
- Composition API: Load multiple skills with dependency resolution
