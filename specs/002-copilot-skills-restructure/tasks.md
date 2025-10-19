# Tasks: Copilot Skills System Restructure

**Feature**: 002-copilot-skills-restructure
**Input**: Design documents from `/specs/002-copilot-skills-restructure/`
**Prerequisites**: plan.md, spec.md
**Branch**: `002-copilot-skills-restructure`

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`
- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions
All paths relative to repository root `/Users/sethrose/Developer/Tests/copilot-skills/`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure for scripts

- [X] T001 Create scripts directory structure: `.github/copilot-skills/scripts/bash/` and `.github/copilot-skills/scripts/python/`
- [X] T002 Create templates directory: `.github/copilot-skills/templates/`
- [X] T003 Create prompts directory: `.github/prompts/` (if not exists)
- [X] T004 [P] Create tests directory: `tests/copilot-skills/` with subdirectories `fixtures/` and `scripts/`
- [X] T005 [P] Copy or symlink `.specify/scripts/bash/common.sh` to `.github/copilot-skills/scripts/bash/common.sh`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core utilities and templates that ALL user stories depend on

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T006 Create YAML schema for SKILL.md frontmatter in `.github/copilot-skills/scripts/python/skill_schema.yaml`
- [X] T007 Implement YAML validator in `.github/copilot-skills/scripts/python/yaml_validator.py`
- [X] T008 Create SKILL.md template with placeholders in `.github/copilot-skills/templates/SKILL.template.md`
- [X] T009 [P] Create detail file template in `.github/copilot-skills/templates/detail-file.template.md`
- [X] T010 [P] Create Python script template in `.github/copilot-skills/templates/script.template.py`
- [X] T011 [P] Create Bash script template in `.github/copilot-skills/templates/script.template.sh`
- [X] T012 Enhance common.sh with skill-specific functions (log_skill_event, validate_skill_name, get_skill_path) in `.github/copilot-skills/scripts/bash/common.sh`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Create New Skill with Guided Workflow (Priority: P1) 🎯 MVP

**Goal**: Developer can run one script to interactively create a compliant skill

**Independent Test**: Run `create-skill.sh`, follow prompts, verify generated skill passes validation

### Implementation for User Story 1

- [ ] T013 [P] [US1] Create prompt file `.github/prompts/skills.create.prompt.md` with instructions for /skills.create command
- [ ] T014 [US1] Implement `create-skill.sh` main script in `.github/copilot-skills/scripts/bash/create-skill.sh`
- [ ] T015 [US1] Add interactive prompting for skill metadata (name, description, tags, dependencies)
- [ ] T016 [US1] Add template substitution logic (replace {{placeholders}} with user input)
- [ ] T017 [US1] Add directory creation logic (create `.github/copilot-skills/{skill-name}/` and `scripts/` subdirectory)
- [ ] T018 [US1] Add SKILL.md generation with YAML frontmatter
- [ ] T019 [US1] Add index.md update logic (append new skill entry to `.github/copilot-skills/index.md`)
- [ ] T020 [US1] Add validation check at end (call validate-skill.sh before completing)
- [ ] T021 [US1] Add error handling and rollback on failure
- [ ] T022 [US1] Add success message with next steps

**Checkpoint**: At this point, User Story 1 should be fully functional - developers can create skills via script

---

## Phase 4: User Story 2 - Validate Skill Compliance (Priority: P1)

**Goal**: Developer can check if their skill follows the constitution before PR

**Independent Test**: Run `validate-skill.sh hello-skill`, verify it reports pass/fail with violations

### Implementation for User Story 2

- [ ] T023 [P] [US2] Create prompt file `.github/prompts/skills.validate.prompt.md` with instructions for /skills.validate command
- [ ] T024 [US2] Implement `validate-skill.sh` main script in `.github/copilot-skills/scripts/bash/validate-skill.sh`
- [ ] T025 [US2] Add YAML frontmatter validation (check required fields: name, description, version, tags, dependencies)
- [ ] T026 [US2] Add file reference checking (verify all linked files in SKILL.md exist)
- [ ] T027 [US2] Add index registration check (verify skill is listed in index.md)
- [ ] T028 [US2] Add progressive disclosure validation (check SKILL.md has Overview, Capabilities, Quick Start, References sections)
- [ ] T029 [US2] Add bundled script documentation check (verify scripts/ directory and files are documented in SKILL.md)
- [ ] T030 [US2] Add constitution principle checks (metadata clarity, file-based organization, cross-reference validity)
- [ ] T031 [US2] Add violation reporting with specific line numbers and remediation suggestions
- [ ] T032 [US2] Add exit code handling (0 on pass, 1 on fail)
- [ ] T033 [US2] Load constitution checklist from `.specify/checklists/skill-compliance-checklist.md` for validation rules

**Checkpoint**: At this point, User Stories 1 AND 2 should both work - create and validate skills independently

---

## Phase 5: User Story 3 - Update Agent Context on Skill Changes (Priority: P2)

**Goal**: Copilot automatically knows about new skills without manual edits

**Independent Test**: Create new skill, run `update-agent-context.sh`, verify `.github/copilot-instructions.md` updated

### Implementation for User Story 3

- [ ] T034 [P] [US3] Create prompt file `.github/prompts/skills.discover.prompt.md` with instructions for /skills.discover command
- [ ] T035 [US3] Implement `update-agent-context.sh` in `.github/copilot-skills/scripts/bash/update-agent-context.sh`
- [ ] T036 [US3] Add git diff detection (find new/modified skills since last update)
- [ ] T037 [US3] Add skill metadata extraction (read YAML frontmatter from changed skills)
- [ ] T038 [US3] Add agent context file detection (find `.github/copilot-instructions.md` or equivalent)
- [ ] T039 [US3] Add marker-based section update (preserve manual edits between <!-- SKILLS:BEGIN --> and <!-- SKILLS:END --> markers)
- [ ] T040 [US3] Add skill entry formatting (create markdown list with skill name, description, path, when-to-use)
- [ ] T041 [US3] Add idempotency check (safe to run multiple times, no duplicates)
- [ ] T042 [US3] Add dry-run mode (`--dry-run` flag to preview changes)
- [ ] T043 [US3] Add backup creation before modifying agent context file

**Checkpoint**: All three MVP stories should now be independently functional

---

## Phase 6: User Story 4 - Generate Skill from Prompt (Priority: P3)

**Goal**: Developer describes a skill in natural language, AI generates initial structure

**Independent Test**: Run `generate-from-prompt.sh`, provide description, verify draft skill created

### Implementation for User Story 4

- [ ] T044 [P] [US4] Create prompt file `.github/prompts/skills.generate.prompt.md` with AI instructions for skill generation
- [ ] T045 [P] [US4] Create generation system prompt in `.github/copilot-skills/prompts/generate-skill.prompt.md`
- [ ] T046 [US4] Implement `generate-from-prompt.sh` in `.github/copilot-skills/scripts/bash/generate-from-prompt.sh`
- [ ] T047 [US4] Implement `skill_generator.py` AI backend in `.github/copilot-skills/scripts/python/skill_generator.py`
- [ ] T048 [US4] Add natural language parsing (extract capabilities, patterns, use cases from description)
- [ ] T049 [US4] Add AI prompt construction (format request for SKILL.md content generation)
- [ ] T050 [US4] Add AI provider integration (GitHub Copilot CLI or OpenAI API fallback)
- [ ] T051 [US4] Add draft skill directory creation (`drafts/{skill-name}/` to avoid polluting main skills)
- [ ] T052 [US4] Add generated content validation (ensure output has required sections)
- [ ] T053 [US4] Add review workflow instructions (tell developer how to review and promote to main skills)
- [ ] T054 [US4] Add optional promotion command (`--promote` flag to move from drafts/ to .github/copilot-skills/)

**Checkpoint**: All user stories (1-4) should now be independently functional

---

## Phase 7: Discovery & Additional Tooling

**Purpose**: Additional utilities that enhance but don't block user stories

- [ ] T055 [P] Implement `list-skills.sh` in `.github/copilot-skills/scripts/bash/list-skills.sh`
- [ ] T056 [P] Add search functionality (filter skills by tag, name, description)
- [ ] T057 [P] Add skill inspection (show metadata, linked files, bundled scripts for a given skill)
- [ ] T058 [P] Add JSON output mode for programmatic use (`--json` flag)
- [ ] T059 [P] Create prompt file `.github/prompts/skills.use.prompt.md` for loading skills into context
- [ ] T060 [P] Create prompt file `.github/prompts/skills.update.prompt.md` for modifying existing skills

---

## Phase 8: Testing & Quality

**Purpose**: Ensure all scripts work correctly and follow best practices

- [ ] T061 [P] Create valid skill fixture in `tests/copilot-skills/fixtures/valid-skill/`
- [ ] T062 [P] Create invalid skill fixture in `tests/copilot-skills/fixtures/invalid-skill/` (missing frontmatter)
- [ ] T063 [P] Write bats test for create-skill.sh in `tests/copilot-skills/scripts/test_create_skill.bats`
- [ ] T064 [P] Write bats test for validate-skill.sh in `tests/copilot-skills/scripts/test_validate_skill.bats`
- [ ] T065 [P] Write bats test for update-agent-context.sh in `tests/copilot-skills/scripts/test_update_context.bats`
- [ ] T066 [P] Write integration test for full workflow in `tests/copilot-skills/scripts/test_integration.bats`
- [ ] T067 Add CI/CD workflow file `.github/workflows/validate-skills.yml` for automated PR checks
- [ ] T068 Add README.md in `.github/copilot-skills/scripts/` explaining script usage

---

## Phase 9: Documentation & Migration

**Purpose**: Update docs and migrate existing skills to new tooling

- [ ] T069 [P] Update AUTHORING.md to reference new scripts and workflows
- [ ] T070 [P] Update README.md with /skills.* command examples
- [ ] T071 [P] Update GOVERNANCE.md with validation requirements
- [ ] T072 [P] Update TROUBLESHOOTING.md with script debugging tips
- [ ] T073 Test hello-skill against validate-skill.sh and fix any violations
- [ ] T074 Test skill-template against validate-skill.sh and fix any violations
- [ ] T075 Create quickstart guide in `.github/copilot-skills/QUICKSTART.md` for new users
- [ ] T076 Add script usage examples to EXAMPLES.md

---

## Dependencies Between User Stories

```
Phase 1 (Setup) → Phase 2 (Foundation) → Phase 3+ (User Stories in parallel)
                                        ↓
                            ┌───────────┼───────────┬───────────┐
                            ↓           ↓           ↓           ↓
                          US1         US2         US3         US4
                      (Create)   (Validate)    (Update)   (Generate)
                            ↓           ↓           ↓           ↓
                            └───────────┴───────────┴───────────┘
                                        ↓
                            Phase 7+ (Enhancement)
```

**Critical Path**: Phase 1 → Phase 2 → US1 (Create) → US2 (Validate)

**MVP Scope**: Complete through Phase 5 (US1, US2, US3) for basic workflow

**Parallel Opportunities**:
- US1, US2, US3, US4 can be developed independently after Phase 2
- Within each user story, tasks marked [P] can run in parallel
- All Phase 7, 8, 9 tasks can run in parallel with each other

---

## Implementation Strategy

### MVP First (Phases 1-5)
1. **Week 1**: Setup + Foundation (T001-T012)
2. **Week 2**: User Story 1 - Create workflow (T013-T022)
3. **Week 3**: User Story 2 - Validation (T023-T033)
4. **Week 4**: User Story 3 - Agent context (T034-T043)

**Deliverable**: Functional create → validate → register workflow

### Iteration 2 (Phases 6-9)
5. **Week 5**: User Story 4 - AI generation (T044-T054)
6. **Week 6**: Discovery tools (T055-T060)
7. **Week 7**: Testing (T061-T068)
8. **Week 8**: Documentation (T069-T076)

**Deliverable**: Complete tooling with AI assistance, tests, and docs

---

## Task Counts

- **Phase 1 (Setup)**: 5 tasks
- **Phase 2 (Foundation)**: 7 tasks
- **Phase 3 (US1)**: 10 tasks
- **Phase 4 (US2)**: 11 tasks
- **Phase 5 (US3)**: 10 tasks
- **Phase 6 (US4)**: 11 tasks
- **Phase 7 (Discovery)**: 6 tasks
- **Phase 8 (Testing)**: 8 tasks
- **Phase 9 (Documentation)**: 8 tasks

**Total**: 76 tasks

**Parallel opportunities**: 32 tasks marked [P]

**MVP scope**: 43 tasks (Phases 1-5)
