# Governance: Skills Architecture Lifecycle & Review Process

This document defines how skills are reviewed, validated, versioned, and maintained in the Copilot Skills Architecture.

---

## Skill Lifecycle States

Each skill progresses through well-defined states:

### DRAFT
**Description**: Skill is being authored or waiting for initial review  
**Characteristics**: Not yet in index.md, not discoverable, may be incomplete  
**Transition**: → ACTIVE (after compliance review passes)  
**Duration**: Until ready for merge

### ACTIVE
**Description**: Skill is in use, meets all Constitutional Principles, discoverable in index.md  
**Characteristics**: Listed in index.md, used by developers, receives updates  
**Transition**: → DEPRECATED (when replaced or no longer needed)  
**Duration**: As long as skill is actively used

### DEPRECATED
**Description**: Skill is being phased out in favor of a newer version or different approach  
**Characteristics**: Listed in index.md with deprecation notice, migration guidance provided, remains discoverable for 2+ releases  
**Transition**: → ARCHIVED (after grace period)  
**Duration**: 2+ releases (e.g., v1.0 → v1.1 → v1.2 before archiving)

### ARCHIVED
**Description**: Skill is no longer maintained; kept for historical reference only  
**Characteristics**: Not listed in active index.md, available in archive directory, not discoverable  
**Transition**: (terminal state)  
**Duration**: Indefinite (never deleted, only archived)

---

## Semantic Versioning for Skills

Each skill maintains its own version independent of other skills.

### Version Format
`MAJOR.MINOR.PATCH`

- **MAJOR**: Breaking changes (e.g., API changes, removed capabilities)
- **MINOR**: New capabilities (backward compatible)
- **PATCH**: Bug fixes, documentation improvements

### Examples

- `1.0.0` → `1.1.0`: Add new capability (backward compatible)
- `1.0.0` → `1.0.1`: Fix script bug
- `1.0.0` → `2.0.0`: Remove deprecated capability (breaking change)

### Versioning Rules

1. Start new skills at `1.0.0`
2. MAJOR version bumps require migration guidance
3. Deprecated capabilities must provide replacement patterns
4. Each version must pass compliance checklist

---

## Pull Request Review Process

### PR Template

When submitting a skill (new or updated), use this PR title and description format:

**Title**: `feat: Add {skill-name} skill` or `fix: Update {skill-name} skill`

**Description**:
```markdown
## Skill: [Skill Name]

### Summary
One paragraph describing the skill and its purpose.

### Core Capabilities
- Capability 1
- Capability 2
- Capability 3

### When to Use
Link keyword patterns or task descriptions for when this skill is relevant.

### Changes
- [ ] SKILL.md created with complete metadata
- [ ] Detail files created (list files)
- [ ] Bundled scripts created (if applicable)
- [ ] Registered in index.md
- [ ] Compliance checklist reviewed

### Compliance Checklist
Link to completed checklist from `.specify/checklists/skill-compliance-checklist.md`
```

### Reviewer Checklist

Reviewers must verify:

- [ ] **Constitutional Principle I: Progressive Disclosure**
  - SKILL.md is scannable in < 3 minutes
  - Detail files are linked appropriately
  - Each detail file focuses on single topic
  - Detail files can be read independently

- [ ] **Constitutional Principle II: File-Based Organization**
  - Directory structure is correct
  - All referenced files exist
  - No extraneous files
  - File naming is consistent

- [ ] **Constitutional Principle III: Dynamic Discovery**
  - Skill is registered in index.md
  - Metadata is complete (name, description, when_to_use, tags)
  - Description is distinct from other skills
  - Tags are relevant

- [ ] **Constitutional Principle IV: Deterministic Execution**
  - Scripts handle errors gracefully
  - Scripts produce consistent output (deterministic)
  - Scripts are documented in SKILL.md with usage examples
  - Scripts can run from project root

- [ ] **Constitutional Principle V: Composability**
  - Dependencies are declared in metadata
  - Cross-skill references use relative paths
  - No circular dependencies
  - Skill scope is clear and bounded

- [ ] **Quality Checks**
  - Markdown is valid (no broken links)
  - YAML frontmatter parses correctly
  - Code examples are syntactically correct
  - All links are relative and functional

### Approval Criteria

PR is approved when:
1. All 5 Constitutional Principles verified ✓
2. Quality checks pass ✓
3. At least one maintainer approval ✓
4. Compliance checklist completed ✓

---

## Skill Maintenance

### Update Process

1. **Make changes** to skill files (SKILL.md, detail files, scripts)
2. **Increment version** in YAML frontmatter
3. **Document changes** in commit message
4. **Run compliance checklist** to validate
5. **Open PR** with title `fix: Update {skill-name} to vX.Y.Z`
6. **Get approval** from maintainer
7. **Merge** and update `Last Updated` date in SKILL.md

### Deprecation Process

When a skill is being phased out:

1. **Update SKILL.md** with deprecation notice:
   ```yaml
   ---
   name: "Old Skill Name"
   status: "DEPRECATED"
   deprecation_date: "2025-10-18"
   migration_guidance: "Use New Skill Name instead. See [../new-skill/SKILL.md](../new-skill/SKILL.md)"
   ---

   ## ⚠️ DEPRECATION NOTICE
   This skill is deprecated as of October 18, 2025. Please use the [New Skill Name](../new-skill/SKILL.md) instead.
   ```

2. **Update index.md** to mark skill as DEPRECATED:
   ```markdown
   ### Old Skill Name (DEPRECATED)
   ⚠️ Deprecated as of Oct 18, 2025. [Migrate to New Skill Name](../new-skill/SKILL.md)
   ```

3. **Keep in index.md** for 2+ releases (or defined grace period)
4. **Archive** after grace period ends (move to `.github/copilot-skills/archive/`)

### Archival Process

1. **Create archive directory** (if not exists): `.github/copilot-skills/archive/`
2. **Move skill directory** to archive: `mv .github/copilot-skills/old-skill .github/copilot-skills/archive/old-skill`
3. **Remove from index.md**
4. **Add reference in index.md**:
   ```markdown
   ## Archived Skills
   See `.github/copilot-skills/archive/` for skills no longer actively maintained.
   ```

---

## Naming Conventions

### Directory Names
- **Format**: kebab-case (lowercase with hyphens)
- **Examples**: `pdf-handling`, `compliance-tracking`, `financial-reporting`
- **Rule**: Must match skill name in YAML frontmatter

### File Names
- **Detail files**: lowercase, descriptive: `forms.md`, `reference.md`, `patterns.md`, `examples.md`, `calculations.md`
- **Scripts**: meaningful, descriptive: `extract_form_fields.py`, `check-license-status.js`, `process-batch.sh`

### Metadata Tags
- **Format**: lowercase, no spaces, comma-separated
- **Examples**: `["documents", "pdf", "forms"]` or `["compliance", "licensing", "texas"]`
- **Rule**: 3-5 tags per skill

---

## Conflict Resolution

### Overlapping Skills

If two skills have overlapping capabilities:

1. **Define clear scopes** - Each skill should have distinct boundaries
   - Example: `pdf-handling` (generic PDF operations) vs `form-filling` (form-specific operations)
2. **Document cross-references** - Link from each skill to related skill
3. **Clarify in PR** - Explain why overlap is acceptable/beneficial

### Circular Dependencies

If Skill A depends on Skill B and Skill B depends on Skill A:

1. **Reject circular dependency** - Require refactoring
2. **Options**:
   - Create third skill for shared functionality (A→C, B→C)
   - Move shared code to one skill, remove from other
   - Separate concerns so dependencies flow in one direction only

---

## Constitutional Principle Validation

### Principle I: Progressive Disclosure
**Test**: Can a developer read SKILL.md in < 3 minutes and understand core capabilities?
- Measure: Time to read SKILL.md
- Target: < 3 minutes
- Pass criteria: Yes

### Principle II: File-Based Organization
**Test**: Does the skill follow the required directory and file structure?
- Check: Directory exists, SKILL.md exists, scripts/ exists (if applicable)
- Pass criteria: All present and properly organized

### Principle III: Dynamic Discovery
**Test**: Can AI agents find this skill from index.md metadata?
- Check: Registered in index.md with complete metadata
- Pass criteria: Name, description, when_to_use, tags all present and distinct

### Principle IV: Deterministic Execution
**Test**: Do bundled scripts produce consistent results?
- Test: Run script multiple times with same input
- Pass criteria: Output is identical across runs

### Principle V: Composability
**Test**: Are dependencies explicit and are there circular references?
- Check: Dependencies listed in metadata, cross-references are one-directional
- Pass criteria: No circular dependencies found

---

## Documentation

### Required Documentation

Every skill MUST have:
1. SKILL.md with complete YAML frontmatter
2. At least one detail file (reference.md or forms.md or patterns.md)
3. Entry in index.md

### Optional Documentation

Skills MAY have:
1. Additional detail files (examples.md, calculations.md, troubleshooting.md)
2. Bundled scripts with complete documentation
3. Video walkthrough or demo (future enhancement)

---

## Governance Meetings

### Quarterly Review
- Review all ACTIVE skills for quality and relevance
- Identify skills ready for DEPRECATED status
- Plan new skills needed
- Update templates based on learnings

### Ad-Hoc Reviews
- Emergency: Critical bug or security issue
- Skills that receive complaints or issues
- Skills with circular dependencies discovered

---

## Timeline Example: Complete Skill Lifecycle

```
Oct 18, 2025: Skill created (DRAFT)
             ↓
Oct 18, 2025: Compliance review passed
             ↓
Oct 19, 2025: Merged to main (ACTIVE) - v1.0.0
             ↓
Dec 2025:    Minor update (New capability) - v1.1.0
             ↓
Jan 2026:    Deprecation decision made
             ↓
Feb 2026:    DEPRECATED marked (v1.2.0) - Migration guidance added
             ↓
Apr 2026:    Archived (2 releases after deprecation)
             ↓
[Indefinite]: Available in archive/ for reference
```

---

## References

- **Constitutional Principles**: `.specify/memory/constitution.md`
- **Compliance Checklist**: `.specify/checklists/skill-compliance-checklist.md`
- **Authoring Guide**: `./AUTHORING.md`
- **Skill Template**: `.github/copilot-skills/skill-template/SKILL.md`

---

**Version**: 1.0.0 | **Last Updated**: October 18, 2025
