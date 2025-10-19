# Implementation Plan: Copilot Skills System Restructure

**Branch**: `002-copilot-skills-restructure` | **Date**: 2025-10-18 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/002-copilot-skills-restructure/spec.md`

## Summary

Restructure `.github/copilot-skills/` to match `.specify/` infrastructure by adding **agent prompts** and executable scripts. The `.specify/` system works because prompts like `/speckit.plan`, `/speckit.specify`, and `/speckit.implement` appear in Copilot's chat palette and tell agents HOW to use the infrastructure.

**Current gap**: `.github/copilot-skills/` has documentation but no prompts. Copilot can't discover or execute skill workflows.

**Solution**: Add `.github/prompts/skills.*.prompt.md` files that guide agents through skill creation, validation, and usage - just like speckit prompts guide feature development.

## Prompt Architecture (Key Component)

The `.specify/` system exposes commands through `.github/prompts/speckit.*.prompt.md` files. When a user types `/spec` in Copilot Chat, these prompts appear in the palette:

- `/speckit.specify` - Create feature specification
- `/speckit.plan` - Generate implementation plan
- `/speckit.tasks` - Break plan into actionable tasks
- `/speckit.implement` - Execute implementation
- `/speckit.analyze` - Analyze existing code
- `/speckit.checklist` - Generate quality checklists
- `/speckit.clarify` - Request clarification
- `/speckit.constitution` - Check constitution compliance

**We need equivalent prompts for skills**:

```
.github/prompts/
├── skills.create.prompt.md       # Interactive skill creation (/skills.create)
├── skills.validate.prompt.md     # Constitution compliance check (/skills.validate)
├── skills.use.prompt.md          # Load and apply skill (/skills.use)
├── skills.discover.prompt.md     # Search available skills (/skills.discover)
├── skills.update.prompt.md       # Modify existing skill (/skills.update)
└── skills.generate.prompt.md     # AI-assisted skill generation (/skills.generate)
```

Each prompt file contains:
1. **Instructions** for the AI agent on what to do
2. **Script invocations** to call `.github/copilot-skills/scripts/`
3. **Validation rules** to ensure output quality
4. **User interaction patterns** for gathering input

## Technical Context

**Language/Version**: Bash 4.0+ (primary), Python 3.8+ (YAML processing, AI generation)  
**Primary Dependencies**: yq (YAML parsing), jq (JSON processing), git, GitHub Copilot CLI (optional)  
**Storage**: Filesystem (.github/copilot-skills/), git for versioning  
**Testing**: bats (Bash Automated Testing System), integration tests with real skills  
**Target Platform**: macOS/Linux development environments, CI/CD (GitHub Actions)
**Project Type**: CLI tooling + documentation system  
**Performance Goals**: <5s skill creation, <2s validation, <1s agent context update  
**Constraints**: No external dependencies except yq/jq (widely available), idempotent operations  
**Scale/Scope**: 10-50 skills per repository, <100 lines per script for maintainability

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Principle I: Progressive Disclosure ✅
**Compliance**: Scripts will enhance, not replace, the layered documentation approach. Automation enables faster creation of properly structured skills with metadata → core → details hierarchy intact.

### Principle II: File-Based Organization ✅
**Compliance**: Scripts generate and validate the required directory structure (SKILL.md + frontmatter, linked files, scripts/). Templates enforce filesystem conventions.

### Principle III: Dynamic Discovery Through Metadata ✅
**Compliance**: `update-agent-context.sh` automates index.md updates when skills are added. Validation ensures index entries are complete and scannable.

### Principle IV: Deterministic Execution with Scripts ✅
**Compliance**: This feature *strengthens* this principle by providing scripts to create and validate bundled scripts within skills. Meta-tooling for deterministic execution.

### Principle V: Composability and Cross-Skill References ✅
**Compliance**: Validation scripts will check cross-references exist and detect circular dependencies. Creation scripts prompt for dependency declarations.

**GATE STATUS**: ✅ PASS - All constitution principles are strengthened by this infrastructure

## Project Structure

### Documentation (this feature)

```
specs/[###-feature]/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)

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

