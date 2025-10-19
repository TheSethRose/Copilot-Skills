---
description: Guidance for creating high-quality Copilot Skills following constitutional principles and VS Code best practices
---

# Create Skill - Instructions

When working with skill creation files or when queries contain skill-related keywords, use this context.

## Constitutional Principles (Required for All Skills)

### 1. Progressive Disclosure
Information organized in layers: **metadata → core workflow → optional details**

**Checklist**:
- ✓ YAML frontmatter with: description, model (optional), tools (optional)
- ✓ Core workflow scannable in <3 minutes
- ✓ Detail files are optional, not required to use skill
- ✓ Each layer independent and self-contained

**Anti-pattern**: Requiring users to read all documentation before using skill

### 2. File-Based Organization
Skills are organized as **files in specific locations**, not in databases or external systems.

**Structure**:
```
.github/
├── prompts/{skill-name}.prompt.md         # Always required
├── instructions/{skill-name}.instructions.md  # Always required
└── copilot-skills/{skill-name}/           # Optional
    ├── README.md
    ├── scripts/                           # Optional
    ├── patterns.md                        # Optional
    └── reference.md                       # Optional
```

**Required Paths**:
- Prompt: `.github/prompts/{skill-name}.prompt.md`
- Instructions: `.github/instructions/{skill-name}.instructions.md`

**Anti-pattern**: Storing skill definitions in external APIs or databases

### 3. Dynamic Discovery
Skills are **discoverable by AI agents via keywords and file patterns**.

**Implementation**:
- Keywords defined in prompt file YAML
- Entry in `.github/copilot-instructions.md` (keyword routing map)
- File patterns in instructions file `description:` field
- Clear use cases in prompt

**Example routing map entry**:
```markdown
#### Skill Name
**Keywords**: keyword1, keyword2, keyword3
**Suggest**: `/skill-name`
**Auto-context**: `.github/instructions/skill-name.instructions.md`
**Skill**: `.github/copilot-skills/skill-name/README.md`
```

**Anti-pattern**: Skills that can't be found without manual documentation

### 4. Deterministic Execution
Scripts produce **consistent, parseable terminal output only**.

**Requirements**:
- ✓ Scripts output to stdout/stderr only (NO file generation)
- ✓ Consistent output format (JSON recommended)
- ✓ Error handling with clear exit codes (0=success, 1=error)
- ✓ Help documentation (`--help`, `-h` flags)
- ✓ Input validation before processing

**Example Python script**:
```python
#!/usr/bin/env python3
import argparse, json, sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Input value")
    args = parser.parse_args()
    
    try:
        result = {"status": "success", "input": args.input}
        print(json.dumps(result, indent=2))
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
```

**Anti-pattern**: Scripts that generate files, modify state, or produce non-deterministic output

### 5. Composability
Skills have **clear boundaries and explicit dependencies**.

**Requirements**:
- ✓ Dependencies explicitly listed (if any)
- ✓ Clear scope (what it does vs. doesn't do)
- ✓ No duplicate functionality from existing skills
- ✓ Explicit cross-skill references (not implicit)

**Anti-pattern**: Hidden dependencies, overlapping functionality, unclear scope

## VS Code File Formats

### Prompt File (`.prompt.md`)
```yaml
---
description: Brief description of what this skill does
model: Claude Sonnet 4  # Optional
tools: ['search', 'usages', 'fetch']  # Optional
---

# Skill Name

Content here...
```

**Supported YAML fields**:
- `description` - Brief description (required)
- `model` - AI model (optional)
- `tools` - Available tools (optional)

### Instructions File (`.instructions.md`)
```yaml
---
description: Auto-loaded context description
---

# Skill Name - Instructions

Content here...
```

**Supported YAML fields**:
- `description` - Auto-load context description (required)

### Chat Mode File (`.chatmode.md`)
```yaml
---
description: Description shown in chat mode dropdown
tools: ['search', 'usages', 'fetch']  # Optional
model: Claude Sonnet 4  # Optional
---

# Chat Mode Name

Content here...
```

**Supported YAML fields**:
- `description` - Display name in dropdown (required)
- `tools` - Available tools (optional)
- `model` - AI model (optional)

## Skill Archetypes

### Type 1: Minimal Command Skill
- **Example**: cleanup, brand-guidelines
- **Files**: 2 (prompt + instructions)
- **Scripts**: None
- **Complexity**: Low (~30 minutes)
- **When**: Simple, single-purpose operations
- **Structure**: Just workflows and basic guidance

### Type 2: Domain Knowledge Skill
- **Example**: git-ops, pdf-handling
- **Files**: 5-10
- **Scripts**: 2-5 bundled utilities
- **Complexity**: Medium (~1-2 hours)
- **When**: Complex domain with automation
- **Structure**: Workflows + scripts + examples

### Type 3: Rich Reference Skill
- **Example**: mcp-builder, document-skills
- **Files**: 15+
- **Scripts**: 5+ utilities
- **Complexity**: High (~2-3 hours)
- **When**: Deep technical domain with sub-areas
- **Structure**: Full documentation + scripts + patterns + references

### Type 4: Meta Skill
- **Example**: generate-instructions, create-skill
- **Files**: 20+
- **Scripts**: Analysis, validation, generation
- **Complexity**: Very High (~3+ hours)
- **When**: Operating on the skills system itself
- **Structure**: Full architecture + validation

## File Naming Conventions

| Type | Pattern | Example | Result |
|------|---------|---------|--------|
| Prompt | `{name}.prompt.md` | `git-ops.prompt.md` | Slash command `/git-ops` |
| Instructions | `{name}.instructions.md` | `git-ops.instructions.md` | Auto-load context |
| Chat Mode | `{name}.chatmode.md` | `skill-creator.chatmode.md` | Mode "Skill Creator" |

**Names**: Use `kebab-case` (lowercase with hyphens)

## Testing Workflows

### Verify File Paths
```bash
test -f .github/prompts/{name}.prompt.md
test -f .github/instructions/{name}.instructions.md
```

### Verify YAML Format
```bash
# Should output valid YAML
head -5 .github/prompts/{name}.prompt.md
```

### Test Scripts
```bash
# Make executable
chmod +x .github/copilot-skills/{name}/scripts/*.sh

# Test help
.github/copilot-skills/{name}/scripts/script.sh --help

# Test error handling
.github/copilot-skills/{name}/scripts/script.sh --invalid
```

## Quality Guidelines

### Do
- ✓ Follow all 5 constitutional principles rigorously
- ✓ Start with minimal skill (add complexity later)
- ✓ Test workflows before finalizing
- ✓ Document examples clearly
- ✓ Validate no overlap with existing skills
- ✓ Use proper YAML only (no custom fields)
- ✓ Include `applyTo` patterns if auto-loading
- ✓ Create helpful error messages

### Don't
- ✗ Create skills without clear use cases
- ✗ Skip validation phase
- ✗ Generate files from scripts
- ✗ Use unsupported YAML fields
- ✗ Create overlapping functionality
- ✗ Use inconsistent naming conventions
- ✗ Leave workflows untested
- ✗ Include external dependencies without justification

## Common Workflows

### Create Minimal Skill (30 minutes)
1. Define name (kebab-case)
2. Create `.github/prompts/{name}.prompt.md`
3. Create `.github/instructions/{name}.instructions.md`
4. Update `.github/copilot-instructions.md` (keyword routing map)
5. Validate and commit

### Create Domain Knowledge Skill (1-2 hours)
1. Define name and scope
2. Create prompt + instructions
3. Create `.github/copilot-skills/{name}/` directory
4. Create 2-5 bundled scripts
5. Create README.md with examples
6. Validate all 5 principles
7. Update routing map
8. Test end-to-end
9. Commit

### Create Rich Reference Skill (2-3 hours)
1. Define name, scope, sub-domains
2. Create prompt + instructions
3. Create skill directory
4. Create 5+ bundled scripts
5. Create detail files (patterns.md, reference.md)
6. Create examples directory
7. Comprehensive validation
8. Update routing map
9. Extensive testing
10. Commit

## Conventional Commits

When committing skill changes, use:

```bash
feat(skills): add {skill-name} skill
feat(skills): enhance {skill-name} with {feature}
fix(skills): correct {skill-name} behavior
docs(skills): update {skill-name} examples
refactor(skills): reorganize {skill-name} structure
```

Examples:
```bash
git commit -m "feat(skills): add database-migrations skill"
git commit -m "feat(skills): enhance git-ops with worktree support"
git commit -m "docs(skills): add mcp-builder examples"
```

## Reference Resources

- **Architecture Overview**: `.github/copilot-skills/README.md`
- **Constitutional Principles**: `.specify/memory/constitution.md`
- **Templates**: `.github/copilot-skills/templates/`
- **Existing Skills**: Browse `.github/copilot-skills/` for examples
- **Routing Map**: `.github/copilot-instructions.md`

---

**Key Principle**: Skills are living documentation modules. They should be clear, focused, well-tested, and constitutionally compliant.
