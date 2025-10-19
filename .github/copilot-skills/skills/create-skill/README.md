# Create Skill - Comprehensive Skill Creation System

---
name: "Create Skill"
description: "Guided workflow for creating high-quality, constitutional-compliant Copilot Skills"
version: "1.0.0"
tags: ["skill-creation", "meta", "architecture", "scaffolding", "validation"]
---

This directory contains the **Create Skill** meta-skill—a comprehensive system for building new Copilot Skills through a structured 5-phase workflow.

## Quick Links

- **Slash Command**: `/create-skill` - Start the guided workflow
- **Chatmode**: `/switch skill-creator` - Enter Skill Architect mode
- **Detailed Guide**: `.github/instructions/create-skill.instructions.md`
- **Skill Prompt**: `.github/prompts/create-skill.prompt.md`
- **Architecture**: `.github/copilot-skills/README.md`

## What is Create Skill?

**Create Skill** is a meta-skill designed to help you build other skills. It provides:

1. **5-Phase Guided Workflow** - Discovery → Design → Validation → Implementation → Integration
2. **Constitutional Compliance** - Automatic validation of all 5 architectural principles
3. **Template Generation** - Create correct file structures in proper locations
4. **Best Practice Guidance** - Learn from existing skills in `.github/copilot-skills/`
5. **Integration Support** - Register skills in the routing map and test end-to-end

## How to Use

### Option 1: Guided Command
```bash
# Start in chat
/create-skill
```
Responds with interactive discovery questions and guides you through all 5 phases.

### Option 2: Expert Mode
```bash
# Enter Skill Architect mode
/switch skill-creator
```
Switch to this chatmode for deeper expertise and more detailed guidance.

### Option 3: Reference Documentation
See `.github/instructions/create-skill.instructions.md` for comprehensive guidelines.

## The 5-Phase Workflow

### 📋 Phase 1: Discovery
**Goal**: Understand the skill's purpose, scope, and requirements

You'll be asked:
1. What problem does this skill solve?
2. What's in-scope vs out-of-scope?
3. Who will use this skill?
4. How should this skill be triggered? (keywords, file patterns)
5. How often will it be used?
6. Simple or complex workflow?

**Output**: Clear understanding of skill intent and boundaries

### 🏗️ Phase 2: Design
**Goal**: Define skill architecture and structure

Decisions made:
- **Archetype**: Minimal, Domain Knowledge, Rich Reference, or Meta
- **File Structure**: What files do you need?
- **Dependencies**: What tools/skills are required?
- **Workflows**: What are the 2-5 primary user workflows?
- **Scripts**: Do you need bundled utilities?
- **Examples**: What are concrete use cases?

**Output**: Architectural blueprint for the skill

### ✅ Phase 3: Validation
**Goal**: Verify constitutional compliance

Checks performed:
- ✅ Progressive Disclosure - Metadata, scannable workflow, optional details
- ✅ File-Based Organization - Correct paths and structure
- ✅ Dynamic Discovery - Keywords, routing map, file patterns
- ✅ Deterministic Execution - Scripts output only, parseable, error handling
- ✅ Composability - Clear boundaries, explicit dependencies

**Output**: Validation report showing compliance status

### ⚙️ Phase 4: Implementation
**Goal**: Generate all skill files

Files created:
- `.github/prompts/{name}.prompt.md` - Skill prompt with workflows
- `.github/instructions/{name}.instructions.md` - Auto-load context
- `.github/copilot-skills/{name}/` - Skill directory (if needed)
- Scripts in `scripts/` subdirectory (if needed)
- Detail files like `patterns.md`, `reference.md` (if needed)

**Output**: Production-ready skill files in correct locations

### 🔗 Phase 5: Integration
**Goal**: Register and test the skill

Actions:
- Update keyword routing map in `.github/copilot-instructions.md`
- Validate YAML metadata and file paths
- Test all workflows end-to-end
- Document examples in skill README
- Commit to Git with conventional format

**Output**: Fully integrated, tested skill ready for use

## Skill Archetypes

Choose based on complexity:

### Type 1: Minimal Command Skill
- **Example**: `cleanup`
- **Files**: 2 (prompt + instructions)
- **Scripts**: None
- **Complexity**: Low (~30 minutes)
- **When**: Simple, single-purpose operations

### Type 2: Domain Knowledge Skill
- **Example**: `git-ops`, `pdf-handling`
- **Files**: 5-10
- **Scripts**: 2-5 bundled utilities
- **Complexity**: Medium (~1-2 hours)
- **When**: Complex domain with automation

### Type 3: Rich Reference Skill
- **Example**: `mcp-builder`, `brand-guidelines`
- **Files**: 15+
- **Scripts**: 5+ utilities
- **Complexity**: High (~2-3 hours)
- **When**: Deep technical domain with sub-areas

### Type 4: Meta Skill
- **Example**: `generate-instructions`, `create-skill`
- **Files**: 20+
- **Scripts**: Analysis, validation, generation
- **Complexity**: Very High (~3+ hours)
- **When**: Operating on skills system itself

## Constitutional Principles

All skills MUST satisfy these 5 principles:

### 1. Progressive Disclosure
Information organized in layers: metadata → core → details
- YAML frontmatter with all metadata fields
- Core workflow scannable in <3 minutes
- Detail files optional, not required
- Each layer independent and self-contained

### 2. File-Based Organization
Skills are files, not databases or APIs
- Skill prompt: `.github/prompts/{name}.prompt.md`
- Instructions: `.github/instructions/{name}.instructions.md`
- Optional directory: `.github/copilot-skills/{name}/`
- Scripts: `.github/copilot-skills/{name}/scripts/`

### 3. Dynamic Discovery
AI agents find skills via keywords and patterns
- Keywords in YAML metadata
- Entry in keyword routing map
- File patterns in `applyTo:` field
- Clear use cases documented

### 4. Deterministic Execution
Scripts produce consistent, parseable terminal output
- Output to stdout/stderr only (NO file generation)
- Consistent format (JSON recommended)
- Error handling with exit codes
- Help documentation (`--help`, `-h`)

### 5. Composability
Skills have clear boundaries and explicit dependencies
- Dependencies listed in metadata
- Clear scope (what it does vs. doesn't)
- No duplicate functionality
- Explicit cross-skill references

## Getting Started

1. **Run the command**: `/create-skill` in chat
2. **Answer discovery questions** about your skill's intent
3. **Follow the guided phases** - Design, Validate, Implement, Integrate
4. **Review generated files** in your editor
5. **Test workflows** end-to-end
6. **Commit to Git** with conventional format

## Reference Examples

To see how real skills are structured, browse existing examples:

```
.github/copilot-skills/
├── git-ops/                    # Domain Knowledge Skill
│   ├── scripts/                # 3 bundled scripts
│   └── README.md               # Overview
├── pdf-handling/               # Rich Reference Skill  
│   ├── forms.md                # Detail file
│   ├── reference.md            # Detail file
│   ├── scripts/                # 9+ scripts
│   └── README.md               # Overview
├── mcp-builder/                # Rich Reference Skill
│   ├── reference/              # Reference docs
│   ├── scripts/                # Multiple scripts
│   └── README.md               # Overview
└── skill-template/             # Minimal Skill
    ├── scripts/                # Example scripts
    └── README.md               # Overview
```

## Common Patterns

### Create Minimal Skill (2 files)
```
1. Define name (kebab-case)
2. Create .github/prompts/{name}.prompt.md
3. Create .github/instructions/{name}.instructions.md
4. Update keyword routing map
5. Commit to Git
```

### Create Domain Knowledge Skill (5-10 files)
```
1. Define name and scope
2. Create prompt + instructions (as above)
3. Create .github/copilot-skills/{name}/
4. Create 2-5 bundled scripts
5. Create README.md with examples
6. Validate constitutional compliance
7. Update routing map
8. Test end-to-end
9. Commit to Git
```

### Create Rich Reference Skill (15+ files)
```
1. Define name, scope, sub-domains
2. Create prompt + instructions
3. Create skill directory structure
4. Create 5+ bundled scripts
5. Create detail files (patterns.md, reference.md)
6. Create examples directory
7. Comprehensive validation
8. Update routing map
9. Extensive testing
10. Commit to Git
```

## Quality Checklist

Before finalizing a skill:

**Documentation** ✓
- [ ] YAML frontmatter complete
- [ ] Use cases concrete and testable
- [ ] Workflows numbered and actionable
- [ ] Examples use real file paths

**Code Quality** ✓
- [ ] Scripts have error handling
- [ ] Scripts have help documentation
- [ ] Scripts output to terminal only
- [ ] Input validation

**Integration** ✓
- [ ] Keyword routing map updated
- [ ] YAML metadata valid
- [ ] File paths correct
- [ ] No conflicts with existing skills

**Testing** ✓
- [ ] All workflows tested
- [ ] Scripts run without errors
- [ ] Auto-loading triggers work
- [ ] Examples accurate

**Constitutional** ✓
- [ ] All 5 principles satisfied
- [ ] Files in correct locations
- [ ] No duplicate functionality
- [ ] Clear dependencies

## Related Resources

- **Architecture Guide**: `.github/copilot-skills/README.md`
- **Constitutional Principles**: `.specify/memory/constitution.md`
- **Skill Templates**: `.github/copilot-skills/templates/`
- **Detailed Instructions**: `.github/instructions/create-skill.instructions.md`
- **Skill Prompt**: `.github/prompts/create-skill.prompt.md`

## Next Steps

After creating a skill:

1. ✅ **Test thoroughly** - Run all workflows end-to-end
2. 📚 **Document well** - Add examples and references
3. 👥 **Get feedback** - Share with team
4. 🔄 **Iterate** - Improve based on usage
5. 🌍 **Share** - Consider contributing to community

## Key Files

| File | Purpose |
|------|---------|
| `.github/chatmodes/skill-creator.chatmode.md` | Chatmode for expert guidance |
| `.github/prompts/create-skill.prompt.md` | Skill prompt with workflows |
| `.github/instructions/create-skill.instructions.md` | Auto-loaded context guidelines |
| `.github/copilot-skills/README.md` | Architecture overview |
| `.specify/memory/constitution.md` | Constitutional principles |

## Support

- 💬 Questions? Use `/create-skill` command
- 🧑‍🏫 Want to learn? Switch to `/switch skill-creator` mode
- 📖 Need details? See `.github/instructions/create-skill.instructions.md`
- 🔍 See examples? Browse `.github/copilot-skills/`

---

**Ready to create a skill?** Start with `/create-skill` and let me guide you through the process!
