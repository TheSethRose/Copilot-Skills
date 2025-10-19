<!--
[SYNC IMPACT REPORT - v1.0.0]
- NEW CONSTITUTION: Copilot Skills Architecture project
- Initial ratification for skill-architecture feature initiative
- Five core principles established for skills-based AI instruction design
- Governance framework for skill authoring, discovery, and progressive disclosure
- All templates reviewed for compatibility
-->

# Copilot Skills Architecture Constitution

## Core Principles

### I. Progressive Disclosure

Information MUST be organized in layers: metadata → core instructions → detailed references. Skills MUST be loadable at multiple levels of detail without forcing users to consume all documentation at once. Each file (SKILL.md, reference.md, forms.md) MUST be independently useful.

**Rationale**: Protects against context window bloat while maintaining completeness. Enables AI agents to load only relevant information for the current task.

### II. File-Based Organization

Skills MUST be organized as self-contained directories under `.github/copilot-skills/{skill-name}/`. Each skill MUST contain a `SKILL.md` core file with YAML frontmatter (name, description, version, tags, dependencies). Linked files (e.g., forms.md, reference.md) MUST be cross-referenced from the core file.

**Rationale**: Provides a discoverable, filesystem-first approach that mirrors Claude Skills. Enables deterministic file loading and clear skill boundaries.

### III. Dynamic Discovery Through Metadata

Skills MUST be discoverable through `.github/copilot-skills/index.md` registry. Registry entries MUST include: skill name, description, path, tags, and "when to use" guidance. Index MUST be human-readable and scannable in under 3 minutes.

**Rationale**: Allows AI agents to discover relevant skills without parsing full documentation. Reduces friction for skill selection and context management.

### IV. Deterministic Execution with Scripts

Operations requiring consistent results (calculations, data transformations, complex logic) MUST include bundled executable scripts in `.github/copilot-skills/{skill-name}/scripts/`. Scripts MUST be documented in the corresponding SKILL.md with usage examples and expected outputs. Scripts produce same result regardless of context.

**Rationale**: Ensures correctness and consistency across the codebase. Prevents logic drift when operations are implemented differently in multiple places.

### V. Composability and Cross-Skill References

Skills MAY reference other skills for complex workflows. Cross-references MUST be explicit with linked files showing which skills to load. Skill boundaries MUST be clearly defined to prevent circular dependencies. Dependencies MUST be declared in skill metadata.

**Rationale**: Enables flexible skill combinations while maintaining clear architecture. Prevents ambiguous or circular skill relationships.

## Skill Authoring Standards

**Metadata Requirements**: Every skill MUST declare name, description, version (semantic versioning), tags (domain keywords), and dependencies (libraries, tools, or other skills).

**File Structure**: Core skill files (SKILL.md) MUST include sections for overview, core capabilities, quick start, common patterns, error handling, and references to detail files. Detail files MUST focus on specific topics (forms, calculations, API reference).

**Documentation Quality**: Skill metadata MUST be clear enough for AI agents to determine relevance. "When to use" guidance MUST distinguish this skill from others. Code examples MUST be complete and testable.

## Project Instructions Integration

The main `.github/copilot-instructions.md` MUST reference the skills system and guide users on skill discovery and usage. Project instructions MUST avoid duplicating skill-specific content; instead, link to relevant skills by name.

## Governance

**Principle Enforcement**: All skills MUST adhere to the five core principles above. Skill PRs MUST include checklist verification of compliance.

**Version Management**: Constitution uses semantic versioning. MAJOR bumps on principle redefinition/removal, MINOR for new principles/sections, PATCH for clarifications.

**Amendment Procedure**: Constitution changes MUST be documented with rationale. Material amendments (MAJOR/MINOR) MUST include migration guidance for existing skills. Amendments MUST be ratified before implementation.

**Compliance Review**: Skill authors MUST verify compliance with this constitution during authoring. Code reviewers MUST confirm principles are followed before merge.

**Runtime Guidance**: See `.specify/memory/` and skill examples in `examples/` for implementation patterns.

**Version**: 1.0.0 | **Ratified**: 2025-10-18 | **Last Amended**: 2025-10-18
