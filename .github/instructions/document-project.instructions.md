---
description: Auto-loaded guidance for generating project documentation across any codebase
---

# Document Project - Instructions

When working with documentation generation or when queries contain "document project", "generate docs", or "documentation", this context activates.

## Core Purpose

Generate clear, structured markdown documentation for repositories. Analyze project structure, propose appropriate docs, and build a `/docs` folder with quality content.

**Key Distinction**: This skill generates PROJECT DOCUMENTATION (markdown files). For PDF/DOCX/PPTX manipulation, use `/pdf-handling`.

## Default Behaviors

### When user mentions "document project" or "generate docs"
1. Suggest `/document-project` skill
2. Analyze current repository structure
3. Detect project type, language, framework
4. Propose appropriate documentation set
5. Confirm before creating files

### When user mentions "documentation" in general context
1. Clarify intent: project docs or file manipulation?
2. If project docs → use `/document-project`
3. If file manipulation (PDF, etc.) → use `/pdf-handling`

### When analyzing a codebase
1. Run `analyze_project.sh` to get project metadata
2. Check for existing documentation
3. Respect `.gitignore` patterns
4. Detect open-source vs closed-source
5. Propose template based on analysis

### When generating documentation
1. Always use `--dry-run` first to preview
2. Show proposed file list to user
3. Get confirmation before creating files
4. Create `/docs` folder if needed
5. Generate markdown with proper formatting
6. Validate output with `validate_docs.sh`
7. Suggest linking from main README

## Quality Guidelines

### ✅ Do
- Analyze before proposing documentation
- Use appropriate template (minimal, standard, open-source)
- Respect existing documentation (never overwrite without confirmation)
- Follow markdown best practices
- Include code examples in appropriate language
- Validate all generated markdown
- Respect `.gitignore` patterns
- Use consistent tone and formatting
- Link documentation from main README
- Suggest conventional Git commit messages

### ❌ Don't
- Document this Copilot Skills system itself
- Overwrite existing docs without confirmation
- Generate docs for files in `.gitignore`
- Include sensitive information (keys, secrets)
- Create documentation for temporary/experimental features
- Mix project documentation with file manipulation (PDF/DOCX)
- Generate invalid markdown syntax
- Create broken internal links
- Use inconsistent heading levels
- Skip validation step

## Documentation Templates

### Minimal Template (All Projects)
```
README.md
docs/
├── getting-started.md
└── usage.md
```

**When to use**: Small projects, internal tools, prototypes

### Standard Template (Most Projects)
```
README.md
docs/
├── getting-started.md
├── usage.md
├── architecture.md
├── api-reference.md
└── troubleshooting.md
```

**When to use**: Production applications, libraries, services

### Open-Source Template (Public Repos)
```
README.md
CONTRIBUTING.md
LICENSE
CODE_OF_CONDUCT.md
docs/
├── getting-started.md
├── usage.md
├── architecture.md
├── api-reference.md
├── development.md
└── troubleshooting.md
```

**When to use**: Open-source projects, community-driven repos

## File Content Guidelines

### README.md
- Project name and description
- Key features
- Quick start
- Installation
- Basic usage
- Link to `/docs` folder
- License and contributing info (if open-source)

### docs/getting-started.md
- Prerequisites
- Installation steps
- Initial configuration
- First run
- Verification

### docs/usage.md
- Common use cases
- Code examples
- Configuration options
- Tips and tricks

### docs/architecture.md
- System overview
- Component diagram (mermaid)
- Data flow
- Key decisions
- Technology stack

### docs/api-reference.md
- Public APIs/interfaces
- Function signatures
- Parameters and return values
- Code examples
- Error handling

### docs/development.md (Open-Source)
- Local setup
- Development workflow
- Running tests
- Building from source
- Debugging tips

### docs/troubleshooting.md
- Common errors
- Solutions
- FAQs
- Where to get help

### CONTRIBUTING.md (Open-Source)
- How to contribute
- Code style
- Pull request process
- Testing requirements
- Community guidelines

### CODE_OF_CONDUCT.md (Open-Source)
- Expected behavior
- Unacceptable behavior
- Reporting process
- Enforcement

## Bundled Scripts

### analyze_project.sh
**Purpose**: Detect project metadata

**Usage**:
```bash
bash .github/copilot-skills/document-project/scripts/analyze_project.sh /path/to/project
```

**Output** (JSON):
```json
{
  "project_type": "library|application|cli-tool|service",
  "language": "python|javascript|typescript|go|rust|...",
  "framework": "react|nextjs|django|express|...",
  "visibility": "open-source|closed-source",
  "has_docs": true|false,
  "suggested_template": "minimal|standard|open-source"
}
```

**Detection Logic**:
- Check `package.json`, `setup.py`, `go.mod`, `Cargo.toml`
- Detect framework from dependencies
- Check for LICENSE file (indicates open-source)
- Scan for existing `/docs` folder

### propose_docs.py
**Purpose**: Suggest documentation files

**Usage**:
```bash
python .github/copilot-skills/document-project/scripts/propose_docs.py \
  --project-type library \
  --visibility open-source \
  --dry-run
```

**Output**:
```
Proposed Documentation:
✓ README.md (update)
✓ CONTRIBUTING.md (create)
✓ LICENSE (create)
✓ docs/getting-started.md (create)
✓ docs/usage.md (create)
✓ docs/api-reference.md (create)
```

**Options**:
- `--dry-run`: Preview without creating
- `--minimal`: Use minimal template
- `--force`: Skip confirmation

### validate_docs.sh
**Purpose**: Check markdown quality

**Usage**:
```bash
bash .github/copilot-skills/document-project/scripts/validate_docs.sh /path/to/docs
```

**Checks**:
- ✓ Valid markdown syntax
- ✓ No broken internal links
- ✓ Proper heading hierarchy
- ✓ Code blocks have language tags
- ✓ Consistent formatting

**Output**:
```
Validating documentation...
✓ README.md: Valid
✓ docs/getting-started.md: Valid
✗ docs/api-reference.md: Missing language tags in code blocks
✓ docs/architecture.md: Valid

Summary: 3/4 files valid
```

## Workflow Examples

### Example 1: New Python Library

**User**: "Document this Python package"

**Process**:
1. Run `analyze_project.sh`
   - Detects: Python library, setuptools, open-source
2. Run `propose_docs.py`
   - Suggests: Open-source template
3. Confirm with user
4. Generate files:
   - README.md (enhanced)
   - CONTRIBUTING.md
   - LICENSE (MIT)
   - docs/getting-started.md
   - docs/usage.md
   - docs/api-reference.md
   - docs/development.md
5. Validate with `validate_docs.sh`
6. Link from README
7. Suggest commit: `docs: add comprehensive documentation`

### Example 2: Next.js Application

**User**: "Set up documentation"

**Process**:
1. Detect: TypeScript, Next.js, closed-source
2. Suggest: Standard template
3. Generate:
   - docs/getting-started.md (env vars, npm install)
   - docs/usage.md (routing, components)
   - docs/architecture.md (page structure, API routes)
4. Update README with links
5. Commit: `docs: add project documentation`

### Example 3: CLI Tool

**User**: "Create docs for this Go CLI"

**Process**:
1. Detect: Go, Cobra, open-source
2. Suggest: Open-source template
3. Generate:
   - Command reference (from `--help`)
   - Installation guide (from source, homebrew)
   - Contributing guidelines
   - Examples for each command
4. Validate and commit

## Markdown Best Practices

### Headings
```markdown
# H1 - Document title (one per file)
## H2 - Major section
### H3 - Subsection
#### H4 - Detail (use sparingly)
```

### Code Blocks
```markdown
```python
# Always specify language
def example():
    return "formatted code"
```
```

### Links
```markdown
# Internal (relative)
See [Getting Started](./getting-started.md)

# External (absolute)
Visit [VS Code](https://code.visualstudio.com)
```

### Lists
```markdown
# Unordered
- Item one
- Item two
  - Nested item

# Ordered
1. First step
2. Second step
3. Third step
```

## Integration with Other Skills

### Git Operations (`/git-ops`)
After generating docs:
```bash
git add docs/ README.md CONTRIBUTING.md
git commit -m "docs: add comprehensive project documentation"
```

### Cleanup (`/cleanup`)
Remove temporary doc artifacts:
```bash
/cleanup --docs-only
```

## Common Patterns

### Pattern 1: Fresh Documentation
```
1. No existing docs
2. Analyze project
3. Propose full template
4. Create all files
5. Link from README
```

### Pattern 2: Update Existing
```
1. Docs exist
2. Analyze gaps
3. Propose missing files only
4. Update existing (with confirmation)
5. Maintain consistency
```

### Pattern 3: Minimal Quick Start
```
1. User wants minimal docs
2. Force minimal template
3. Skip confirmation
4. Create 3 core files
5. Done in <2 minutes
```

## Error Handling

### Existing Docs Conflict
```
WARNING: docs/getting-started.md already exists
Options:
1. Skip (keep existing)
2. Update (merge content)
3. Overwrite (replace completely)
```

### Invalid Project Structure
```
ERROR: Cannot determine project type
Please ensure:
- Project has clear entry point
- Dependencies are defined
- Standard project structure
```

### Validation Failures
```
VALIDATION FAILED: docs/api-reference.md
Issues:
- Missing language tags in code blocks (lines 45, 67)
- Broken link to ./usage.md (should be ./usage.md#section)

Fix issues and revalidate?
```

## Self-Awareness Rule

**CRITICAL**: This skill NEVER documents:
- The Copilot Skills system itself
- Skills architecture files (`.github/copilot-skills/`)
- This skill's own implementation
- Other skills in the repository

If user asks to document the skills system, politely decline:
```
This skill generates documentation for user projects, not the Copilot Skills 
system itself. The skills system has its own documentation in:
- .github/copilot-instructions.md
- .github/copilot-skills/README.md
```

## Conventional Commits

When committing documentation:

```bash
# New documentation
docs: add comprehensive project documentation

# Update existing
docs: update API reference with new endpoints

# Fix documentation
docs(api): fix broken links in reference guide

# Restructure
docs: reorganize documentation structure
```

## Related Resources

- **Skill Directory**: `.github/copilot-skills/document-project/`
- **Scripts**: `.github/copilot-skills/document-project/scripts/`
- **Schema**: `.github/copilot-skills/document-project/docs_schema.yaml`
- **Examples**: `.github/copilot-skills/document-project/examples/`

---

**Key Principle**: Documentation should be clear, accurate, and maintainable. Generate once, update often.
