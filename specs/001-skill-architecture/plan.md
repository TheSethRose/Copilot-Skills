# Implementation Plan: Copilot Skills Architecture

**Branch**: `001-skill-architecture` | **Date**: October 18, 2025 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `specs/001-skill-architecture/spec.md`

**Status**: ✅ **PHASE 1 COMPLETE** - Ready for Phase 2 (task breakdown)

## Summary

Implement a skills-based architecture for GitHub Copilot that mirrors Anthropic's Claude Skills, enabling AI agents to discover, load progressively, and execute specialized domain capabilities without context window bloat. Uses file-based organization (`.github/copilot-skills/`) with YAML frontmatter metadata, Markdown documentation, and bundled scripts for deterministic execution.

**Key Design Decisions**:
1. **Metadata Format**: YAML frontmatter in SKILL.md (proven pattern from Anthropic official skills)
2. **File Structure**: Skill directory with SKILL.md + detail files + scripts/ subdirectory
3. **Discovery**: Registry in `.github/copilot-skills/index.md` with lightweight metadata
4. **Progressive Disclosure**: 4-layer model (index → SKILL.md → detail files → scripts)
5. **Composability**: Explicit cross-skill references for complex workflows
6. **Authoring**: 20-30 minutes per skill using consistent patterns

## Technical Context

<!--
  ACTION REQUIRED: Replace the content in this section with the technical details
  for the project. The structure here is presented in advisory capacity to guide
  the iteration process.
-->

**Language/Version**: Markdown (documentation architecture) + YAML (skill metadata)  
**Primary Dependencies**: GitHub (`.github/` directory structure), GitHub Copilot (for skill discovery and loading)  
**Storage**: File-based (`.github/copilot-skills/` directory structure with Markdown and scripts)  
**Testing**: Manual verification of skill discovery, progressive disclosure, deterministic script execution  
**Target Platform**: GitHub repositories (web-based, version control integration)
**Project Type**: Documentation architecture / organizational pattern (not software build)  
**Performance Goals**: Skill index scannable in <3 minutes, SKILL.md file load <1 minute, context reduction by 60%  
**Constraints**: No implementation framework required, pure file-based organization, Copilot must understand file structure  
**Scale/Scope**: Initial architecture supports 5-20 skills per workspace, scalable to 50+ skills with hierarchical organization

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

**Constitution Version**: 1.0.0 | **Principles Applicable**: All 5 core principles

### Gate Evaluation

- ✅ **I. Progressive Disclosure**: Feature spec explicitly requires layered information loading (metadata → SKILL.md → detail files)
- ✅ **II. File-Based Organization**: Architecture is fundamentally file-based (`.github/copilot-skills/` directory structure with discrete skill directories)
- ✅ **III. Dynamic Discovery**: Spec includes skill discovery through index.md registry with clear metadata
- ✅ **IV. Deterministic Execution**: Scripts bundled in skills for consistent, repeatable operations documented in SKILL.md
- ✅ **V. Composability**: Cross-skill references explicitly supported for complex workflows

**Gate Status**: ✅ **PASS** - Feature fully aligns with all constitution principles. No conflicts or violations identified.

**Compliance Markers**: 
- Skill authoring standards (metadata requirements, file structure, documentation quality) MUST be enforced
- All PR reviews for new skills MUST verify compliance with 5 core principles
- Runtime guidance available in `.specify/memory/` and `examples/` folder

## Project Structure

### Documentation (this feature)

```
specs/001-skill-architecture/
├── spec.md              # Feature specification
├── plan.md              # This file (implementation plan)
├── research.md          # Phase 0: Technical research and decisions ✅ COMPLETE
├── data-model.md        # Phase 1: Entity definitions and relationships ✅ COMPLETE
├── quickstart.md        # Phase 1: Getting started guide ✅ COMPLETE
├── contracts/           # Phase 1: Interaction contracts ✅ COMPLETE
│   └── interaction-contracts.md
├── checklists/
│   └── requirements.md  # Quality checklist
└── tasks.md             # Phase 2 output (next: /speckit.tasks command)
```

### Implementation (repository root)

```
.github/
├── copilot-instructions.md      # Main project instructions (update to reference skills)
└── copilot-skills/              # Skills directory (will be created)
    ├── index.md                 # Skills registry
    ├── {skill-name}/            # Individual skill directories
    │   ├── SKILL.md
    │   ├── {detail}.md
    │   └── scripts/
    └── ...
```

### Examples Reference

```
examples/
├── anthropics-skills/           # Official Anthropic patterns
├── obra-superpowers/            # Community development skills
├── superpowers-skills/          # Community-editable skills
└── tfriedel-claude-office-skills/  # Office document workflows
```
<!--
  ACTION REQUIRED: Replace the placeholder tree below with the concrete layout
  for this feature. Delete unused options and expand the chosen structure with
  real paths (e.g., apps/admin, packages/something). The delivered plan must
  not include Option labels.
-->

```
# [REMOVE IF UNUSED] Option 1: Single project (DEFAULT)
src/
├── models/
├── services/
├── cli/
└── lib/

tests/
├── contract/
├── integration/
└── unit/

# [REMOVE IF UNUSED] Option 2: Web application (when "frontend" + "backend" detected)
backend/
├── src/
│   ├── models/
│   ├── services/
│   └── api/
└── tests/

frontend/
├── src/
│   ├── components/
│   ├── pages/
│   └── services/
└── tests/

# [REMOVE IF UNUSED] Option 3: Mobile + API (when "iOS/Android" detected)
api/
└── [same as backend above]

ios/ or android/
└── [platform-specific structure: feature modules, UI flows, platform tests]
```

**Structure Decision**: [Document the selected structure and reference the real
directories captured above]

## Complexity Tracking

*Fill ONLY if Constitution Check has violations that must be justified*

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |

