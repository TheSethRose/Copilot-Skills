# Skill Compliance Checklist

**Purpose**: Validate new skills against the 5 Constitutional Principles before merging to main branch

**Reference**: [Constitution](../../.specify/memory/constitution.md)

---

## Before Starting

- Skill name: ________________
- Skill path: `.github/copilot-skills/[skill-name]/`
- Date: ________________
- Reviewer: ________________

---

## Constitutional Principle I: Progressive Disclosure

**Requirement**: Information must load in layers (metadata → SKILL.md → detail files)

- [ ] SKILL.md is scannable in under 3 minutes (~1000 words max)
- [ ] SKILL.md includes clear "Detailed References" section linking to detail files
- [ ] Detail files (e.g., forms.md, reference.md) each focus on single topic
- [ ] Detail files can be read independently without reading other detail files
- [ ] SKILL.md provides enough guidance that users know which detail file to open
- [ ] YAML frontmatter is complete and accurate (name, description, version, tags, dependencies)

**Status**: ☐ PASS ☐ FAIL ☐ NEEDS REVISION

**Notes**: 

---

## Constitutional Principle II: File-Based Organization

**Requirement**: Skills are self-contained directories with clear file structure

- [ ] Skill directory exists: `.github/copilot-skills/[skill-name]/`
- [ ] Directory contains SKILL.md (required)
- [ ] Directory contains detail files with meaningful names (e.g., forms.md, reference.md, patterns.md)
- [ ] Detail files exist for every topic mentioned in SKILL.md "Detailed References"
- [ ] Scripts (if any) are in `scripts/` subdirectory
- [ ] No extraneous files in skill directory (only .md, .py, .sh, .js, .json)
- [ ] No cross-linking between unrelated skills (only composability references)

**Status**: ☐ PASS ☐ FAIL ☐ NEEDS REVISION

**Notes**: 

---

## Constitutional Principle III: Dynamic Discovery Through Metadata

**Requirement**: Metadata enables AI agents to find relevant skills without parsing full documentation

- [ ] Skill is registered in `.github/copilot-skills/index.md`
- [ ] Index entry includes: name, path, description, when_to_use, tags
- [ ] Description is specific enough to indicate skill purpose (not vague like "handling")
- [ ] When_to_use clearly distinguishes this skill from others (e.g., "PDF forms" not just "documents")
- [ ] Tags are relevant keywords (not generic; 3-5 tags)
- [ ] No duplicate descriptions or overlapping when_to_use guidance

**Status**: ☐ PASS ☐ FAIL ☐ NEEDS REVISION

**Notes**: 

---

## Constitutional Principle IV: Deterministic Execution with Scripts

**Requirement**: Complex operations include bundled scripts for consistent results

- [ ] Scripts (if any) have clear documentation in SKILL.md
- [ ] Scripts document expected arguments and flags
- [ ] Scripts document output format (JSON, plain text, etc.)
- [ ] Scripts handle errors gracefully with informative messages
- [ ] Scripts are executable (correct permissions on Unix systems)
- [ ] Script output format is deterministic (same input → same output)
- [ ] Scripts can be run from project root without side effects

**Status**: ☐ PASS ☐ FAIL ☐ NEEDS REVISION

**Notes**: 

---

## Constitutional Principle V: Composability and Cross-Skill References

**Requirement**: Skills may reference each other; boundaries clear, dependencies explicit

- [ ] Dependencies on other skills (if any) are declared in YAML frontmatter
- [ ] Cross-skill references include relative paths (e.g., `../pdf-handling/SKILL.md`)
- [ ] Skill scope is clearly bounded (one domain, not multiple unrelated topics)
- [ ] No circular dependency chains (A→B→C→A)
- [ ] Complex workflows using multiple skills are documented in detail files or examples
- [ ] Skill can stand alone without assuming other skills exist

**Status**: ☐ PASS ☐ FAIL ☐ NEEDS REVISION

**Notes**: 

---

## Additional Quality Checks

### Documentation Quality

- [ ] All markdown is valid (no broken links, proper formatting)
- [ ] Code examples are syntactically correct
- [ ] YAML frontmatter parses correctly
- [ ] Relative links work correctly (use `./ ` for files in same directory)

**Status**: ☐ PASS ☐ FAIL

### Code Examples

- [ ] Examples show realistic usage patterns
- [ ] Examples avoid hardcoded paths (use skill-relative paths)
- [ ] Examples include error cases or edge scenarios

**Status**: ☐ PASS ☐ FAIL

### Metadata Accuracy

- [ ] Name matches directory name (kebab-case)
- [ ] Version follows semantic versioning (MAJOR.MINOR.PATCH)
- [ ] Dependencies list is complete and accurate
- [ ] Tags are lowercase, no spaces

**Status**: ☐ PASS ☐ FAIL

---

## Sign-Off

**Overall Status**: ☐ APPROVED ☐ APPROVED WITH MINOR REVISIONS ☐ NEEDS MAJOR REVISIONS

**Comments**:

**Approved by**: ___________________ **Date**: ___________

---

## Revision Tracking

| Revision | Date | Changes | Approved By |
|----------|------|---------|-------------|
| 1.0      | [date] | Initial version | - |
| | | | |
| | | | |

