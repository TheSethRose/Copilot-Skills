# Feature Specification: Copilot Skills Architecture

**Feature Branch**: `skill-architecture`  
**Created**: October 18, 2025  
**Status**: Draft  
**Input**: Implement a skills-based architecture for GitHub Copilot that replicates Claude Skills with progressive disclosure, file-based organization, dynamic discovery, and deterministic script execution

## Clarifications

### Session 2025-10-18

- Q: How does Copilot discover and trigger skill loading? → A: Through context-aware matching (user mentions task keywords → Copilot scans index.md metadata → Copilot infers relevant skills + user can explicitly reference skills by name)
- Q: What is the skill lifecycle and versioning strategy? → A: Skills use semantic versioning (MAJOR.MINOR.PATCH) independently per skill; lifecycle states are DRAFT → ACTIVE → DEPRECATED → ARCHIVED
- Q: How do we prevent circular skill dependencies? → A: Explicit cross-skill references documented in metadata; manual PR review validates dependency graph (no A→B→C→A cycles)
- Q: What is the scalability limit for index.md? → A: Initial architecture supports 5-20 skills per workspace; scalable to 50+ skills; index remains flat unless metadata filtering becomes necessary
- Q: What are canonical terminology choices? → A: Capitalize "Skills" when referring to the architecture; use "skill" lowercase for individual instances; prefer "detail files" over synonyms; "bundled scripts" refers to scripts in `.github/copilot-skills/{skill}/scripts/`

---

## User Scenarios & Testing *(mandatory)*

### User Story 1 - AI Agent Discovers Available Skills (Priority: P1)

A developer working on a workspace wants GitHub Copilot to understand what specialized capabilities (skills) are available for their project without cluttering the main instructions with all domain-specific details.

**Why this priority**: This is the foundational capability. Without skill discovery, users must still provide all information upfront, defeating the purpose of the skills system.

**Independent Test**: A developer can open `.github/copilot-skills/index.md`, see a list of available skills with clear descriptions and paths, and reference them in a task. Copilot should recognize when a skill is relevant to the current task.

**Acceptance Scenarios**:

1. **Given** a project with skills registered in `.github/copilot-skills/index.md`, **When** a user mentions a task (e.g., "extract form fields from a PDF"), **Then** Copilot identifies the relevant skill (PDF Handling) and loads the appropriate SKILL.md file
2. **Given** a workspace with multiple skills, **When** a user explicitly references a skill by name, **Then** Copilot loads the correct SKILL.md with its full capabilities
3. **Given** the index.md file exists, **When** a user opens it, **Then** they see a clear registry listing all available skills with descriptions and paths

---

### User Story 2 - Load Skill Details Progressively (Priority: P1)

Once a skill is identified as relevant, the user should access increasingly detailed information without overwhelming their context: core capabilities first, then specific patterns, then API references.

**Why this priority**: Progressive disclosure is the core design principle that makes the skills system efficient. Without it, all skill files become as large as the original monolithic instructions.

**Independent Test**: A user can load a SKILL.md file and understand the core capabilities, then navigate to linked detail files (forms.md, reference.md) when deeper information is needed. Each file is independently useful.

**Acceptance Scenarios**:

1. **Given** a skill's SKILL.md file, **When** a user reads it, **Then** they understand core capabilities and common operations without reading 50KB of reference material
2. **Given** a SKILL.md file with references to linked files (e.g., "see forms.md for details"), **When** a user needs specific guidance, **Then** they can open the linked file which provides focused information
3. **Given** a skill with multiple detail files (forms.md, reference.md, patterns.md), **When** a user loads SKILL.md, **Then** they know which file to open for their specific use case

---

### User Story 3 - Execute Deterministic Skill Operations (Priority: P2)

For skills that involve calculations, data transformations, or complex operations, developers should be able to run bundled scripts to ensure consistent results regardless of context.

**Why this priority**: Ensures correctness and consistency for complex operations. Secondary because many skills may not require scripts, but important for domain-specific logic.

**Independent Test**: A user can run a bundled script (e.g., `.github/copilot-skills/compliance-tracking/scripts/check-license-status.js`) and get consistent, documented results that match the skill's documented patterns.

**Acceptance Scenarios**:

1. **Given** a skill with bundled scripts, **When** a user runs a script documented in SKILL.md, **Then** the script executes correctly and produces deterministic results
2. **Given** multiple places in code that need the same calculation, **When** developers reference the bundled script, **Then** they get consistent results across the codebase
3. **Given** a script in `.github/copilot-skills/{skill-name}/scripts/`, **When** the script is documented in SKILL.md, **Then** users understand what the script does and how to invoke it

---

### User Story 4 - Integrate Skills into Project Workflow (Priority: P3)

The main project instructions should reference the skills system so developers understand that specialized capabilities exist in a skills registry rather than being part of the main instructions.

**Why this priority**: Completes the system by connecting the skills architecture to normal workflows. Important for adoption but not blocking.

**Independent Test**: A developer can read `.github/copilot-instructions.md` and understand that skills-based architecture exists, where skills are located, and when to reference them.

**Acceptance Scenarios**:

1. **Given** a main copilot-instructions.md file, **When** a developer reads the section on skills, **Then** they understand skills exist in `.github/copilot-skills/` and how to use them
2. **Given** domain-specific tasks (PDF handling, compliance, financial reporting), **When** main instructions mention relevant skills, **Then** developers know where to find specialized guidance

---

### Edge Cases

- What happens when a skill references a linked file that doesn't exist? (Broken links should be documented/validated during skill authoring; link checker tool recommended for PR review)
- How should skills handle version compatibility? (Each skill declares its own semantic version and dependencies; breaking changes require MAJOR version bump with migration guidance)
- What if two skills have conflicting capabilities? (Skills should have clear scope boundaries defined in metadata; overlapping capabilities are acceptable if scopes are distinct; PR review validates boundary clarity)
- Can skills reference other skills? (Yes, cross-skill references are supported for complex workflows; documented in "dependencies" metadata field; circular references prevented through manual PR review)
- What is the hard limit on skill count per workspace? (Initial architecture: 5-20 skills; scalable to 50+ skills; at 50+ skills, consider hierarchical categories in index or automated filtering)
- How do we handle skill deprecation? (Skills transitioning to DEPRECATED state include migration guidance in metadata and remain discoverable in index for 2+ releases; then moved to ARCHIVED)

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST support organizing specialized instructions into discrete skill directories under `.github/copilot-skills/`
- **FR-002**: System MUST provide a `.github/copilot-skills/index.md` registry file listing all available skills with metadata (name, description, path, tags)
- **FR-003**: Each skill MUST include a `SKILL.md` file with YAML frontmatter containing metadata (name, description, version, tags, dependencies)
- **FR-004**: System MUST support progressive disclosure through linked documentation files (e.g., forms.md, reference.md) referenced from SKILL.md
- **FR-005**: Skill files MUST include clear sections for core capabilities, quick start, common patterns, and references to detailed files
- **FR-006**: System MUST support bundled executable scripts in `.github/copilot-skills/{skill-name}/scripts/` directory
- **FR-007**: Scripts MUST be documented in SKILL.md with usage examples and expected outputs
- **FR-008**: System MUST support cross-skill references for complex workflows combining multiple skills; circular dependencies are documented in skill metadata and validated during PR review
- **FR-009**: Skill metadata MUST include dependencies list (libraries, tools, or other skills required)
- **FR-010**: Main copilot-instructions.md file MUST reference the skills system and provide guidance on when to use specific skills
- **FR-011**: Skill index MUST be easily scannable showing skill name, description, and path for quick discovery (scannable in <2 minutes per SC-001)
- **FR-012**: System MUST support semantic versioning (MAJOR.MINOR.PATCH) per skill with independent version tracking and migration guidance for breaking changes (MAJOR version)
- **FR-013**: System MUST handle skill lifecycle states (DRAFT, ACTIVE, DEPRECATED, ARCHIVED) with clear status markers in metadata and PR-enforced validation

### Key Entities

- **Skill**: A self-contained package of instructions, patterns, and executable scripts for a specialized domain
  - Attributes: name, description, version (semantic: MAJOR.MINOR.PATCH), tags, dependencies, location (path), lifecycle state (DRAFT/ACTIVE/DEPRECATED/ARCHIVED)
  - Lifecycle: DRAFT (under review) → ACTIVE (production) → DEPRECATED (use alternative) → ARCHIVED (no longer supported)
  - Related to: Skills Registry, Detail Files, Scripts

- **Skills Registry**: The index file listing all available skills with lightweight metadata for discovery
  - Attributes: skill name, description, path, tags, when-to-use guidance, lifecycle state
  - Scalability: Supports 5-20 skills natively; scalable to 50+ with optional hierarchical filtering
  - Relationships: Links to individual Skill files; entries for ACTIVE and DEPRECATED skills only (DRAFT excluded until ready, ARCHIVED excluded from primary index)

- **Detail Files**: Focused documentation files linked from core SKILL.md
  - Examples: forms.md, reference.md, patterns.md, calculations.md
  - Attributes: topic, content, relationships to SKILL.md, optional status (each independently readable)
  - Relationships: Belongs to single Skill; may reference other detail files or cross-skill patterns

- **Executable Scripts**: Deterministic operations bundled with skills
  - Attributes: language, purpose, inputs, outputs, documentation, return contract (e.g., JSON with success/errors/data)
  - Determinism: Same inputs → same outputs regardless of context (required per FR-007)
  - Relationships: Referenced in SKILL.md, located in scripts/ subdirectory, validates per acceptance contract

- **Project Instructions**: Main `.github/copilot-instructions.md` that coordinates the skills system
  - Attributes: overview of skills system, link to index.md, guidance on discovery patterns
  - Relationships: References Skills Registry, provides skill discovery heuristics for Copilot context matching

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Developers can identify and load the correct skill for their task in under 2 minutes (discoverable through index.md)
- **SC-002**: Each skill's SKILL.md file is scannable in under 3 minutes to understand core capabilities
- **SC-003**: Progressive disclosure reduces initial context window usage by 60% compared to monolithic instructions (e.g., 5KB base + 10KB loaded skill vs. 50KB monolithic)
- **SC-004**: All skills have clear metadata that enables AI agents to determine relevance without ambiguity
- **SC-005**: Scripts produce consistent, deterministic results documented in the corresponding SKILL.md
- **SC-006**: Cross-skill workflows can be composed by following references in linked files without manual navigation
- **SC-007**: 95% of common task scenarios can be handled by loading 1-2 skills max
- **SC-008**: New skills can be created following the architecture pattern in under 30 minutes

## Assumptions

- Copilot can navigate file references and open linked .md files (no automatic filesystem traversal required)
- Copilot uses context-aware matching: when user mentions a task (e.g., "extract form fields from PDF"), Copilot infers relevant skills and scans index.md metadata to confirm relevance
- Users will explicitly mention skill names or provide context clues about what they're working on (both automatic and explicit discovery supported)
- Skills are organized for a single project/workspace (not shared across projects in v1)
- Project is using GitHub (has `.github/` directory structure)
- Users have basic familiarity with markdown and file structure
- Skill authoring is enabled by templates and governance (PR review validates compliance with 5 constitution principles)
- Skills follow semantic versioning (MAJOR.MINOR.PATCH) with independent per-skill versioning
- Skill lifecycle states (DRAFT → ACTIVE → DEPRECATED → ARCHIVED) are tracked in metadata and enforced during PR review
