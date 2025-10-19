---
description: "Auto-loaded context for generating copilot-instructions.md files from codebase analysis"
applyTo: "**/{.github/copilot-instructions.md,.cursor/instructions.md,AI_INSTRUCTIONS.md,INSTRUCTIONS.md}"
---

# Generate Instructions - Automatic Context Instructions

**Related Prompt:** `/generate-instructions`  
**Related Skill:** `.github/copilot-skills/copilot-instructions-generator/SKILL.md`

**Triggers:** generate instructions, copilot-instructions, discover patterns, AI instructions, cursor instructions, create instructions, codebase analysis

## Context: AI Instructions Generation and Codebase Analysis

When working with AI instruction files or when user queries contain analysis/generation keywords, this context is automatically activated.

## Default Behaviors

### When user mentions "generate instructions" or "copilot-instructions"
1. Suggest `/generate-instructions` skill prompt
2. Load `.github/copilot-skills/copilot-instructions-generator/SKILL.md`
3. Use bundled scripts for automated analysis
4. Generate structured output based on project patterns

### When user mentions "update instructions" or "refresh AI context"
1. Analyze changes since last generation
2. Preserve manual customizations
3. Merge new patterns with existing instructions
4. Maintain instruction file structure

### When editing existing instruction files
1. Preserve YAML frontmatter format
2. Follow instruction file conventions
3. Respect applyTo pattern syntax
4. Maintain cross-references to skills/prompts

## Quality Guidelines

### ✅ Do
- Analyze project structure before generating
- Respect `.gitignore` patterns (exclude external code)
- Detect framework and language conventions
- Include code style patterns (naming, formatting)
- Reference external documentation when relevant
- Preserve manual edits during updates
- Use consistent section structure
- Include decision-making guidance

### ❌ Don't
- Generate instructions for third-party code (node_modules, venv, etc.)
- Include sensitive information (API keys, credentials)
- Create overly generic instructions
- Duplicate framework documentation
- Ignore existing project conventions
- Generate without analyzing first
- Overwrite manual customizations

## Instruction File Structure

### Standard Sections

1. **Project Overview**
   - What this project is/does
   - Architecture style (monorepo, microservices, etc.)
   - Key technologies and frameworks

2. **Code Patterns**
   - Naming conventions
   - File organization
   - Import/export patterns
   - Error handling style

3. **Development Workflow**
   - How to run the project
   - Testing approach
   - Build/deployment process
   - Common commands

4. **Quality Standards**
   - Code style rules
   - Testing requirements
   - Documentation expectations
   - Security considerations

5. **Domain Knowledge**
   - Business logic patterns
   - Data models
   - API conventions
   - Integration patterns

## Analysis Checklist

When analyzing a codebase, check for:

### Project Metadata
- [ ] Package manager (npm, pip, cargo, etc.)
- [ ] Framework/library versions
- [ ] Language version requirements
- [ ] Development dependencies

### Code Organization
- [ ] Directory structure patterns
- [ ] Module/package organization
- [ ] Test file locations
- [ ] Configuration file locations

### Conventions
- [ ] Naming patterns (camelCase, snake_case, etc.)
- [ ] File naming (index, main, app, etc.)
- [ ] Import statement style
- [ ] Error handling patterns

### Tooling
- [ ] Linters (eslint, pylint, clippy)
- [ ] Formatters (prettier, black, rustfmt)
- [ ] Testing frameworks (jest, pytest, cargo test)
- [ ] Build tools (webpack, vite, cargo)

### Documentation
- [ ] README structure
- [ ] Inline comment style
- [ ] API documentation
- [ ] Changelog format

## Bundled Scripts

The copilot-instructions-generator skill provides these scripts:

```bash
# Analyze repository structure and patterns
.github/copilot-skills/copilot-instructions-generator/scripts/analyze_repo.sh

# Discover coding conventions automatically
.github/copilot-skills/copilot-instructions-generator/scripts/discover_conventions.sh

# Validate existing instruction files
.github/copilot-skills/copilot-instructions-generator/scripts/validate_instructions.sh
```

All scripts output to terminal (no files generated) for AI parsing.

## Example Instruction Patterns

### Framework Detection

**If React project detected:**
```markdown
## React Patterns
- Use functional components with hooks
- Prefer named exports for components
- Place components in src/components/
- Use TypeScript for type safety
```

**If Django project detected:**
```markdown
## Django Patterns
- Follow MVT architecture strictly
- Place apps in apps/ directory
- Use class-based views for CRUD
- Keep business logic in models
```

### Code Style Detection

**If project uses TypeScript:**
```markdown
## TypeScript Standards
- Enable strict mode
- Use interfaces for object shapes
- Prefer type inference when obvious
- Export types alongside implementation
```

**If project uses Python with type hints:**
```markdown
## Python Type Hints
- Use type hints for all public functions
- Import types from typing module
- Use Optional for nullable values
- Run mypy for type checking
```

## Update Strategy

When updating existing instructions:

1. **Preserve Manual Sections**
   - Check for user-written content
   - Mark auto-generated sections
   - Merge rather than replace

2. **Detect Changes**
   - Compare current patterns with previous analysis
   - Highlight new conventions
   - Flag deprecated patterns

3. **Maintain References**
   - Keep skill/prompt cross-references
   - Update file paths if moved
   - Preserve external documentation links

## Common Patterns to Detect

### Naming Conventions
- Component names: `PascalCase`, `kebab-case`
- Function names: `camelCase`, `snake_case`
- File names: `index.js`, `__init__.py`, `mod.rs`
- Test files: `*.test.js`, `test_*.py`, `*_test.go`

### Error Handling
- Try/catch blocks
- Result<T, E> types
- Error boundary components
- Custom error classes

### Testing Patterns
- Test file location (same directory, tests/ folder)
- Test naming (describe/it, test_*, TestCase)
- Mocking strategy (jest.mock, unittest.mock, mockall)
- Assertion style (expect, assert, should)

## Next Steps

When generating instructions:
1. Use `/generate-instructions` prompt for guided workflow
2. Run analysis scripts to gather data
3. Review generated instructions for accuracy
4. Add domain-specific guidance manually
5. Validate with `.github/copilot-skills/scripts/validate_architecture.sh`

## Related Skills

- **Code analysis** - For pattern detection and convention discovery
- **Documentation generation** - For creating comprehensive guides
- **Project setup** - For understanding project structure
