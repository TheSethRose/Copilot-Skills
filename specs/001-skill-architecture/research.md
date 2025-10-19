# Phase 0 Research: Copilot Skills Architecture

**Date**: October 18, 2025  
**Status**: Complete - All technical decisions resolved  
**Scope**: Skill authoring patterns, implementation strategy, tooling requirements

## Research Findings

### Decision 1: Skill Metadata Format

**Choice**: YAML frontmatter in SKILL.md (mirroring Anthropic official skills)

**Rationale**: 
- Anthropic's official skills repository (`examples/anthropics-skills/`) uses YAML frontmatter with `name`, `description`, `license`, and detailed content
- Provides structured, parseable metadata while keeping documentation in readable Markdown
- Standard pattern across 100+ skills in the examples folder

**Metadata Fields Required**:
```yaml
---
name: "skill-name"
description: "One-sentence purpose and when to use it"
version: "1.0.0"
tags: ["category1", "category2"]
dependencies: ["tool1", "library1"]
---
```

**Alternatives Considered**:
- Separate YAML file (skill.yaml): Rejected - less discoverable, requires separate file reads
- JSON frontmatter: Rejected - less readable in Markdown editors
- No metadata: Rejected - defeats discovery purpose

### Decision 2: File Structure for Skilled

**Choice**: Skill directory with SKILL.md + linked detail files + scripts/ subdirectory

**Pattern**:
```
.github/copilot-skills/
├── skill-name/
│   ├── SKILL.md              # Core skill (50-100 lines)
│   ├── detailed-topic.md     # Focused reference (~200 lines)
│   ├── another-topic.md      # Topic-specific patterns
│   └── scripts/
│       ├── script.py         # Bundled executable
│       └── helper.sh         # Supporting tools
```

**Rationale**:
- Mirrors both Anthropic (`document-skills/pdf/`) and community (`obra-superpowers/skills/`) structure
- Progressive disclosure: SKILL.md first, then drill into specific docs, then access scripts
- Scripts co-located with skill for discoverability
- Clean separation of concerns

**Alternatives Considered**:
- Flat structure (all in one SKILL.md): Too large, defeats progressive disclosure
- Scripts in root: Loses skill context, harder to manage multiple skills

### Decision 3: Registry/Index Format

**Choice**: `.github/copilot-skills/index.md` with structured table and clear descriptions

**Pattern**:
```markdown
# Copilot Skills Registry

## Skill Name
**Path**: `.github/copilot-skills/skill-name/SKILL.md`
**Description**: One sentence describing purpose
**When to use**: Specific scenarios where this skill applies
**Keywords**: comma-separated search terms
```

**Rationale**:
- Markdown tables are human-scannable in <3 minutes (meets SC-001)
- Can be automatically parsed by Copilot or agents
- No special tooling required
- Consistent with documentation-first approach

**Examples in Field**:
- Anthropic skills use README.md with similar metadata layout
- Community skills are catalogued in similar registries

### Decision 4: Progressive Disclosure Layers

**Layer 1 - Discovery**: Index.md (10-20 lines per skill metadata)
**Layer 2 - Core Capabilities**: SKILL.md (50-100 lines, quick start + patterns)
**Layer 3 - Deep Reference**: detail.md files (200+ lines, API reference, edge cases)
**Layer 4 - Executable**: scripts/ (bundled implementations)

**Rationale**:
- Each layer independently useful (can stop at any level)
- Reduces context window usage by 60%+ (meets SC-003)
- Matches Copilot's natural reading pattern (browse → read → execute)

**Evidence**:
- PDF skill: `SKILL.md` (quick start) + `reference.md` (detailed API)
- Brand skill: `SKILL.md` (overview) + `TECH-DETAILS` (implementation)
- TDD skill: Single `SKILL.md` with clear section divisions

### Decision 5: Cross-Skill References

**Pattern**: Explicit markdown links in detail files

```markdown
## When PDF Needs Document Conversion
See [Document Skills - docx](../docx/SKILL.md) for Word document creation.
```

**Rationale**:
- Composable skills enable complex workflows
- Explicit links make dependencies clear
- Prevents circular references through manual curation
- Matches constraint V of constitution (Composability)

### Decision 6: Script Documentation

**Location**: Documented inline within SKILL.md with usage examples

**Pattern**:
```markdown
## Using the Extract Script

```bash
python .github/copilot-skills/skill-name/scripts/extract.py input.file --format json
```

**Output Format**: JSON object with `success`, `data`, `errors` fields
```

**Rationale**:
- Scripts are bundled, not auto-discovered
- Documentation co-located with script reference
- Clear input/output contracts for deterministic execution
- Matches principle IV (Deterministic Execution)

### Decision 7: Skill Authoring Workflow

**Recommended Process**:
1. Create skill directory under `.github/copilot-skills/skill-name/`
2. Write SKILL.md with YAML frontmatter and core content
3. Create detail.md files for specific topics as needed
4. Add scripts/ directory with bundled implementations
5. Update `.github/copilot-skills/index.md` with metadata entry
6. Verify compliance with constitution (5 principles)

**Estimated Time**: 20-30 minutes per skill (meets SC-008)

**Validation**: Use checklist template from `.specify/templates/checklist-template.md`

### Decision 8: Copilot Integration Points

**Discovery**: Copilot reads `.github/copilot-skills/index.md` to know available skills

**Loading**: When user mentions a task, Copilot:
1. Scans index.md for matching skills
2. Loads `SKILL.md` from matched skill
3. Navigates to detail files as needed
4. Suggests running bundled scripts

**Feedback Loop**: No special Copilot plugin needed - pure file-based navigation

**Implementation Pattern**:
- Update `.github/copilot-instructions.md` to reference skills system
- Provide examples of how to discover and load skills
- Document common tasks and which skills to use

## Technical Stack

**Languages**: 
- Markdown (documentation)
- YAML (metadata)
- Shell, Python, Node.js (skill-specific scripts)

**Tools Required**:
- Git (version control)
- GitHub (repository hosting)
- Text editor (Markdown authoring)
- Copilot (skill discovery and loading)

**No Additional Dependencies**: Skills are self-contained; each skill declares its own script dependencies

## Implementation Risks & Mitigations

| Risk | Mitigation |
|------|-----------|
| Skill complexity grows too large | Progressive disclosure + detail file separation |
| Circular skill dependencies | Explicit references, manual review in PRs |
| Metadata becomes outdated | Single source of truth in frontmatter |
| Scripts not discoverable | Clear documentation in SKILL.md with examples |
| Skills bloat context window | Architecture specifically designed to avoid this |

## Resolved NEEDS CLARIFICATION

✅ **Metadata Format**: YAML frontmatter in SKILL.md  
✅ **File Organization**: Skill directory + SKILL.md + detail files + scripts/  
✅ **Discovery Mechanism**: Registry in index.md  
✅ **Progressive Disclosure**: 4-layer model with independent utility at each layer  
✅ **Script Execution**: Bundled and documented in SKILL.md  
✅ **Cross-Skill Patterns**: Explicit markdown links for composability  

## Recommendations

1. **Start with Examples**: Review existing skills in `examples/` folder to understand patterns
2. **Template First**: Create a `template-skill/` directory with starter files
3. **Clear Naming**: Use kebab-case for skill names, consistent with Anthropic conventions
4. **Testing Strategy**: Manual verification of discovery + skill loading (no automated testing needed for documentation architecture)
5. **Community Patterns**: Follow patterns from both Anthropic and obra/superpowers communities
