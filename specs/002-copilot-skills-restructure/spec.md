# Feature Specification: Copilot Skills System Restructure

**Feature ID**: 002-copilot-skills-restructure  
**Status**: Planning  
**Created**: 2025-10-18  
**Author**: AI Agent

## Problem Statement

The current `.github/copilot-skills/` system is documentation-heavy but lacks the operational infrastructure that makes `.specify/` effective. The system needs:

1. **Executable automation** - Scripts to create, validate, and manage skills
2. **Guided workflows** - Prompts and templates for skill authoring
3. **Validation tooling** - Automated compliance checking against constitution
4. **Integration hooks** - Scripts to update agent context when skills are added/modified
5. **Development lifecycle** - Clear processes for skill creation, testing, and deployment

Currently, `.github/copilot-skills/` has:
- ✅ Documentation (AUTHORING.md, GOVERNANCE.md, etc.)
- ✅ Templates (skill-template/)
- ✅ Example skills (hello-skill/)
- ❌ No executable scripts for skill management
- ❌ No prompt-based workflows
- ❌ No automated validation
- ❌ No agent context integration

## Goals

### Primary Goals
1. **Parity with .specify infrastructure** - Copilot skills should have the same level of tooling automation
2. **Zero-friction skill creation** - Run one script, answer prompts, get validated skill
3. **Automated compliance** - Constitution checking built into every workflow
4. **Agent-aware updates** - Skills automatically register with Copilot's context

### Secondary Goals
5. **Skill discovery tools** - CLI to search, inspect, and test skills
6. **Migration utilities** - Convert existing documentation into skills
7. **CI/CD integration** - GitHub Actions to validate skills on PR

## Non-Goals
- Changing the fundamental skills architecture (metadata, SKILL.md format, progressive disclosure)
- Replacing the constitution or core principles
- Building a web UI for skill management

## User Stories

### Story 1: Create New Skill with Guided Workflow
**As a** developer  
**I want to** run a script that guides me through creating a new skill  
**So that** I don't need to manually copy templates and remember the structure

**Acceptance Criteria**:
- Run `.github/copilot-skills/scripts/create-skill.sh` from repo root
- Script prompts for: skill name, description, tags, dependencies, linked files
- Script generates: `{skill-name}/SKILL.md` with frontmatter, index entry, script stubs
- Script validates against constitution before completing
- Script updates `.github/copilot-skills/index.md`

### Story 2: Validate Skill Compliance
**As a** skill author  
**I want to** check if my skill follows the constitution  
**So that** I catch errors before creating a PR

**Acceptance Criteria**:
- Run `.github/copilot-skills/scripts/validate-skill.sh {skill-name}`
- Script checks: YAML frontmatter completeness, file references exist, index registration
- Script validates: metadata clarity, progressive disclosure structure, script documentation
- Script outputs: Pass/fail with specific violations listed
- Exit code 0 on pass, 1 on fail

### Story 3: Update Agent Context on Skill Changes
**As a** developer  
**I want** Copilot to know about new skills automatically  
**So that** I don't manually update `.github/copilot-instructions.md`

**Acceptance Criteria**:
- Run `.github/copilot-skills/scripts/update-agent-context.sh`
- Script detects new/modified skills since last run
- Script appends skill metadata to `.github/copilot-instructions.md` in designated section
- Script preserves manual additions between markers
- Script is idempotent (safe to run multiple times)

### Story 4: Generate Skill from Prompt
**As a** developer with domain knowledge  
**I want to** describe a skill in natural language  
**So that** AI generates the initial structure for me

**Acceptance Criteria**:
- Run `.github/copilot-skills/scripts/generate-skill-from-prompt.sh`
- Script accepts: natural language description of capabilities
- Script uses AI to generate: SKILL.md structure, suggested tags, common patterns section
- Script creates draft skill in `drafts/{skill-name}/`
- Developer reviews and promotes to `.github/copilot-skills/` when ready

## Technical Requirements

### Architecture
- Mirror `.specify/scripts/` structure in `.github/copilot-skills/scripts/`
- Reuse common shell utilities from `.specify/scripts/bash/common.sh`
- Follow same error handling and logging patterns
- Use YAML parsing for frontmatter validation (yq or python)

### File Structure
```
.github/copilot-skills/
├── scripts/
│   ├── bash/
│   │   ├── common.sh              # Shared utilities
│   │   ├── create-skill.sh        # Interactive skill creation
│   │   ├── validate-skill.sh      # Constitution compliance checker
│   │   ├── update-agent-context.sh # Register skills with Copilot
│   │   ├── generate-from-prompt.sh # AI-assisted skill generation
│   │   └── list-skills.sh         # Discovery and inspection
├── prompts/
│   ├── create-skill.prompt.md     # Guidance for skill creation
│   ├── validate-skill.prompt.md   # Constitution checking prompt
│   └── generate-skill.prompt.md   # AI generation instructions
├── templates/
│   ├── SKILL.template.md          # Template with placeholders
│   ├── detail-file.template.md    # Template for reference.md, forms.md, etc.
│   └── script.template.py         # Template for bundled scripts
└── [existing structure: index.md, AUTHORING.md, skills/, etc.]
```

### Dependencies
- **bash** 4.0+ - Shell scripting
- **yq** or **python pyyaml** - YAML parsing
- **git** - Version control operations
- **jq** - JSON processing for agent context
- **GitHub Copilot CLI** (optional) - For AI-assisted generation

## Success Metrics

1. **Creation time** - New skill creation takes <5 minutes (vs. 30 minutes manually)
2. **Compliance rate** - 100% of skills pass validation on first try after using scripts
3. **Discovery time** - Developers find relevant skills in <2 minutes using list-skills.sh
4. **Agent awareness** - Copilot suggests correct skill within first 3 responses for relevant tasks

## Implementation Phases

### Phase 0: Infrastructure Setup (Research & Design)
- Analyze `.specify/scripts/bash/` patterns for reuse
- Design YAML frontmatter validation schema
- Design agent context update mechanism
- Create script execution contracts

### Phase 1: Core Scripts
- `common.sh` - Shared utilities
- `create-skill.sh` - Interactive creation
- `validate-skill.sh` - Compliance checking
- `update-agent-context.sh` - Agent integration

### Phase 2: AI-Assisted Generation
- `generate-from-prompt.sh` - Natural language to skill
- Prompt engineering for skill generation
- Draft review workflow

### Phase 3: Discovery & Tooling
- `list-skills.sh` - Search and inspection
- `test-skill.sh` - Skill execution testing
- Documentation updates

### Phase 4: CI/CD Integration
- GitHub Actions workflow
- PR validation checks
- Automated index updates

## Open Questions

1. **YAML parsing** - Should we use yq (external dep) or python (already available)?
2. **Agent context format** - JSON in markers or markdown with structured comments?
3. **Script language** - Bash for consistency or Python for better YAML handling?
4. **AI provider** - Use GitHub Copilot CLI or OpenAI API for generation?
5. **Migration strategy** - Convert existing hello-skill to use new tooling immediately?

## Dependencies

- Existing `.specify/` infrastructure for pattern reference
- Existing `.github/copilot-skills/` documentation and templates
- Constitution compliance checklist in `.specify/checklists/skill-compliance-checklist.md`

## Risks

1. **Script complexity** - Bash scripts may become unmaintainable; consider Python alternative
2. **YAML parsing** - External dependencies (yq) may not be available in all environments
3. **Agent context pollution** - Automated updates could add too much to copilot-instructions.md
4. **Validation strictness** - Too strict validation may frustrate rapid prototyping

## Out of Scope

- Web-based skill editor
- Skill marketplace or sharing beyond git
- Runtime skill loading/unloading (handled by Copilot already)
- Skill versioning beyond semantic versioning in frontmatter
