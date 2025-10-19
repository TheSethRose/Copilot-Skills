# Implementation Plan: Copilot Skills System Restructure


**Branch**: `002-copilot-skills-restructure`**Branch**: `002-copilot-skills-restructure` | **Date**: 2025-10-18 | **Spec**: [spec.md](./spec.md)

**Date**: 2025-10-18**Input**: Feature specification from `/specs/002-copilot-skills-restructure/spec.md`

**Status**: Phase 0 Ready

## Summary

## What We Discovered

Restructure `.github/copilot-skills/` to match `.specify/` infrastructure by adding **agent prompts** and executable scripts. The `.specify/` system works because prompts like `/speckit.plan`, `/speckit.specify`, and `/speckit.implement` appear in Copilot's chat palette and tell agents HOW to use the infrastructure.

The `.specify/` system works because it has **agent prompts** (`.github/prompts/speckit.*.prompt.md`) that:

1. Appear in Copilot's chat palette when users type `/spec`**Current gap**: `.github/copilot-skills/` has documentation but no prompts. Copilot can't discover or execute skill workflows.

2. Tell agents HOW to use the infrastructure

3. Invoke executable scripts to automate workflows**Solution**: Add `.github/prompts/skills.*.prompt.md` files that guide agents through skill creation, validation, and usage - just like speckit prompts guide feature development.

4. Validate outputs against project rules

## Prompt Architecture (Key Component)

**Current gap**: `.github/copilot-skills/` has documentation but NO prompts, so Copilot can't discover or use the system.

The `.specify/` system exposes commands through `.github/prompts/speckit.*.prompt.md` files. When a user types `/spec` in Copilot Chat, these prompts appear in the palette:

## What We're Building

- `/speckit.specify` - Create feature specification

Add agent prompts and executable infrastructure to match `.specify/` pattern:- `/speckit.plan` - Generate implementation plan

- `/speckit.tasks` - Break plan into actionable tasks

```- `/speckit.implement` - Execute implementation

.github/prompts/- `/speckit.analyze` - Analyze existing code

├── skills.create.prompt.md      # /skills.create - Interactive wizard- `/speckit.checklist` - Generate quality checklists

├── skills.validate.prompt.md    # /skills.validate - Constitution check- `/speckit.clarify` - Request clarification

├── skills.use.prompt.md         # /skills.use - Load and apply skill- `/speckit.constitution` - Check constitution compliance

├── skills.discover.prompt.md    # /skills.discover - Search skills

├── skills.update.prompt.md      # /skills.update - Modify existing skill**We need equivalent prompts for skills**:

└── skills.generate.prompt.md    # /skills.generate - AI-assisted creation

```

.github/copilot-skills/scripts/.github/prompts/

├── bash/├── skills.create.prompt.md       # Interactive skill creation (/skills.create)

│   ├── create-skill.sh          # Backend for /skills.create├── skills.validate.prompt.md     # Constitution compliance check (/skills.validate)

│   ├── validate-skill.sh        # Backend for /skills.validate├── skills.use.prompt.md          # Load and apply skill (/skills.use)

│   ├── update-agent-context.sh  # Register skills with Copilot├── skills.discover.prompt.md     # Search available skills (/skills.discover)

│   ├── generate-from-prompt.sh  # Backend for /skills.generate├── skills.update.prompt.md       # Modify existing skill (/skills.update)

│   └── list-skills.sh           # Backend for /skills.discover└── skills.generate.prompt.md     # AI-assisted skill generation (/skills.generate)

└── python/```

    ├── yaml_validator.py        # YAML frontmatter validation

    └── skill_generator.py       # AI generation backendEach prompt file contains:

```1. **Instructions** for the AI agent on what to do

2. **Script invocations** to call `.github/copilot-skills/scripts/`

## Files Created3. **Validation rules** to ensure output quality

4. **User interaction patterns** for gathering input

1. **spec.md** - Feature specification (problem, solution, requirements)

2. **plan.md** - Implementation plan with 3 phases:## Technical Context

   - Phase 0: Research prompt architecture and tooling

   - Phase 1: Design data models and contracts**Language/Version**: Bash 4.0+ (primary), Python 3.8+ (YAML processing, AI generation)  

   - Phase 2: Break down into implementation tasks**Primary Dependencies**: yq (YAML parsing), jq (JSON processing), git, GitHub Copilot CLI (optional)  

3. **KEY-INSIGHT.md** - Why prompts are the missing piece**Storage**: Filesystem (.github/copilot-skills/), git for versioning  

**Testing**: bats (Bash Automated Testing System), integration tests with real skills  

## Constitution Check**Target Platform**: macOS/Linux development environments, CI/CD (GitHub Actions)

**Project Type**: CLI tooling + documentation system  

✅ **All 5 principles satisfied**:**Performance Goals**: <5s skill creation, <2s validation, <1s agent context update  

- Progressive Disclosure: Enhanced by automation**Constraints**: No external dependencies except yq/jq (widely available), idempotent operations  

- File-Based Organization: Scripts enforce structure**Scale/Scope**: 10-50 skills per repository, <100 lines per script for maintainability

- Dynamic Discovery: Prompts enable discoverability

- Deterministic Execution: Meta-tooling for bundled scripts## Constitution Check

- Composability: Validation checks cross-references

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

## Phase 0 Research Tasks

### Principle I: Progressive Disclosure ✅

Next step: Execute research tasks in plan.md**Compliance**: Scripts will enhance, not replace, the layered documentation approach. Automation enables faster creation of properly structured skills with metadata → core → details hierarchy intact.



1. Analyze existing speckit prompt file format### Principle II: File-Based Organization ✅

2. Document script integration patterns**Compliance**: Scripts generate and validate the required directory structure (SKILL.md + frontmatter, linked files, scripts/). Templates enforce filesystem conventions.

3. Research agent context update mechanism

4. Evaluate YAML processing tools### Principle III: Dynamic Discovery Through Metadata ✅

5. Design testing strategy (bats framework)**Compliance**: `update-agent-context.sh` automates index.md updates when skills are added. Validation ensures index entries are complete and scannable.

6. Prototype AI-assisted skill generation

### Principle IV: Deterministic Execution with Scripts ✅

**Output**: `research.md` with concrete decisions for all unknowns**Compliance**: This feature *strengthens* this principle by providing scripts to create and validate bundled scripts within skills. Meta-tooling for deterministic execution.



## How to Continue### Principle V: Composability and Cross-Skill References ✅

**Compliance**: Validation scripts will check cross-references exist and detect circular dependencies. Creation scripts prompt for dependency declarations.

```bash

# Option 1: Manual research**GATE STATUS**: ✅ PASS - All constitution principles are strengthened by this infrastructure

# Read .github/prompts/speckit.*.prompt.md files

# Create research.md with findings## Project Structure



# Option 2: Use speckit (when ready)### Documentation (this feature)

# /speckit.implement --phase=0  # Execute research tasks

``````

specs/[###-feature]/

## Success Criteria├── plan.md              # This file (/speckit.plan command output)

├── research.md          # Phase 0 output (/speckit.plan command)

After implementation, developers can:├── data-model.md        # Phase 1 output (/speckit.plan command)

- Type `/skills.create "My Skill"` → Copilot guides through creation├── quickstart.md        # Phase 1 output (/speckit.plan command)

- Type `/skills.validate` → Instant constitution compliance check├── contracts/           # Phase 1 output (/speckit.plan command)

- Type `/skills.discover "pdf"` → Find relevant skills└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)

- Type `/skills.use pdf-handling` → Load skill into context```

- Zero manual file creation, automated validation, instant discoverability

### Source Code (repository root)

**This makes `.github/copilot-skills/` as powerful as `.specify/`** 🚀

```
.github/
├── prompts/
│   ├── skills.create.prompt.md    # /skills.create - Interactive creation wizard
│   ├── skills.validate.prompt.md  # /skills.validate - Constitution checker
│   ├── skills.use.prompt.md       # /skills.use - Load and apply skill
│   ├── skills.discover.prompt.md  # /skills.discover - Search skills
│   ├── skills.update.prompt.md    # /skills.update - Modify existing skill
│   └── skills.generate.prompt.md  # /skills.generate - AI-assisted generation
├── copilot-skills/
│   ├── scripts/
│   │   ├── bash/
│   │   │   ├── common.sh              # Shared utilities (logging, YAML helpers, git ops)
│   │   │   ├── create-skill.sh        # Backend for /skills.create
│   │   │   ├── validate-skill.sh      # Backend for /skills.validate
│   │   │   ├── update-agent-context.sh # Register skills with Copilot
│   │   │   ├── generate-from-prompt.sh # Backend for /skills.generate
│   │   │   └── list-skills.sh         # Backend for /skills.discover
│   │   └── python/
│   │       ├── yaml_validator.py      # YAML frontmatter schema validation
│   │       └── skill_generator.py     # AI generation backend
│   ├── templates/
│   ├── SKILL.template.md          # Skill file with {{placeholders}}
│   ├── detail-file.template.md    # Template for linked files
│   ├── script.template.py         # Python script template
│   └── script.template.sh         # Bash script template
├── [existing: index.md, AUTHORING.md, GOVERNANCE.md, etc.]
└── [existing skills: hello-skill/, skill-template/]

tests/
├── scripts/
│   ├── test_create_skill.bats     # Test skill creation workflow
│   ├── test_validate_skill.bats   # Test validation logic
│   └── test_integration.bats      # End-to-end workflow tests
└── fixtures/
    ├── valid-skill/               # Example valid skill for testing
    └── invalid-skill/             # Example invalid skill for testing
```

**Structure Decision**: Mirror `.specify/scripts/bash/` structure for consistency. Place Python helpers in separate directory for clear language boundaries. Keep tests adjacent to scripts they validate.

## Complexity Tracking

*Fill ONLY if Constitution Check has violations that must be justified*

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| N/A | No violations | All principles strengthened by this feature |

## Phase 0: Research & Discovery

**Goal**: Resolve all unknowns from Technical Context and establish prompt architecture patterns.

### Research Tasks

1. **Prompt File Format Analysis**
   - Study existing `speckit.*.prompt.md` files in `.github/prompts/`
   - Document the structure: frontmatter, instructions, script invocations
   - Identify required sections: user input handling, validation, error reporting
   - **Output**: `research.md` section "Prompt File Anatomy"

2. **Script Integration Patterns**
   - Analyze how speckit prompts invoke `.specify/scripts/bash/` scripts
   - Document parameter passing, error handling, output formatting
   - Study `setup-plan.sh` for JSON output patterns
   - **Output**: `research.md` section "Prompt-to-Script Integration"

3. **Agent Context Update Mechanism**
   - Research how `.specify/scripts/bash/update-agent-context.sh` works
   - Understand detection of AI agent type (Copilot, Claude, Cursor, etc.)
   - Document preservation of manual edits between markers
   - **Output**: `research.md` section "Agent Context Management"

4. **YAML Processing Best Practices**
   - Evaluate `yq` vs `jq` vs Python for YAML frontmatter validation
   - Research schema validation tools (yamllint, pykwalify)
   - Performance benchmarks for skill validation (<2s constraint)
   - **Output**: `research.md` section "YAML Tooling Decision"

5. **Testing Strategy for Bash Scripts**
   - Research `bats` (Bash Automated Testing System) patterns
   - Study `.specify/scripts/` test coverage approaches
   - Document fixtures and mocking strategies for filesystem operations
   - **Output**: `research.md` section "Testing Approach"

6. **AI-Assisted Skill Generation**
   - Research GitHub Copilot CLI capabilities for generation tasks
   - Evaluate prompt engineering patterns for skill content generation
   - Prototype: Generate SKILL.md from natural language description
   - **Output**: `research.md` section "AI Generation Feasibility"

### Research Deliverables

Create `research.md` with sections:
- **Prompt File Anatomy** - Structure, required fields, examples
- **Prompt-to-Script Integration** - How prompts invoke scripts, parameter passing
- **Agent Context Management** - How to update Copilot's context when skills change
- **YAML Tooling Decision** - Chosen tools and rationale
- **Testing Approach** - bats patterns, fixtures, integration tests
- **AI Generation Feasibility** - Can we auto-generate skills from descriptions?

**Success Criteria**: All "NEEDS CLARIFICATION" items from Technical Context resolved with concrete decisions.

## Phase 1: Design & Contracts

**Prerequisites**: `research.md` complete, all unknowns resolved

### Design Artifacts

1. **data-model.md** - Skill metadata schema, file structure entities
2. **contracts/prompt-api.md** - Interface contract for each `/skills.*` command
3. **contracts/script-api.md** - CLI interface for each script in `scripts/bash/`
4. **quickstart.md** - Developer guide for using the prompt system

### Agent Context Update

Run `.specify/scripts/bash/update-agent-context.sh copilot` to register new technologies:
- yq/jq (YAML processing)
- bats (testing framework)
- GitHub Copilot CLI (generation)

**Output**: Updated `.github/copilot-instructions.md` or equivalent agent context file

## Phase 2: Task Breakdown

**Prerequisites**: Phase 1 complete, constitution re-validated

Generate `tasks.md` using `/speckit.tasks` command. Tasks should cover:
- Prompt file creation (6 files)
- Script implementation (6+ bash scripts)
- Template creation (4+ templates)
- Test suite (integration + unit tests)
- Documentation updates (AUTHORING.md, README.md)
- Example usage scenarios

**Output**: `tasks.md` with actionable implementation tasks

## Next Steps

1. **Run Phase 0 research** - Execute research tasks above
2. **Create research.md** - Consolidate findings
3. **Proceed to Phase 1** - Design data models and contracts
4. **Generate tasks** - Break down into implementation tasks using `/speckit.tasks`

**Command to continue**: `/speckit.tasks` (after Phase 1 complete)

