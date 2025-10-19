---
description: Generate clear, structured documentation for any codebase
---

# Document Project

**Slash Command**: `/document-project`  
**Purpose**: Analyze codebases and generate comprehensive project documentation

## When to Use This Skill

Use `/document-project` when you need to:

- 📚 Generate documentation for an existing codebase
- 🔍 Analyze project structure and propose appropriate docs
- 📝 Create a `/docs` folder with structured content
- 🔄 Update `README.md`, `CONTRIBUTING.md`, or `LICENSE`
- 🎯 Ensure consistent documentation across repositories

**Note**: This skill documents repositories, NOT document file manipulation (PDF/DOCX). For that, see `/pdf-handling`.

## Quick Start

Run `/document-project` to begin. The workflow:

1. **Analyze** - Detect project type, language, framework
2. **Propose** - Suggest relevant documentation files
3. **Confirm** - You choose what to create
4. **Generate** - Build `/docs` folder with approved files
5. **Integrate** - Link from main README

## The 5-Phase Workflow

### Phase 1: Analyze Codebase

The skill detects:
- Project type (library, application, CLI tool, etc.)
- Primary language and framework
- Visibility (open-source vs closed-source)
- Existing documentation
- `.gitignore` patterns

**Script**: `analyze_project.sh` outputs JSON with project metadata

### Phase 2: Propose Documentation

Based on analysis, suggests appropriate files:

**Minimal Set** (all projects):
- `README.md` - Project overview
- `docs/getting-started.md` - Setup instructions
- `docs/usage.md` - Basic usage examples

**Standard Set** (most projects):
- Above, plus:
- `docs/architecture.md` - System design
- `docs/api-reference.md` - API documentation
- `docs/troubleshooting.md` - Common issues

**Open-Source Set** (public repos):
- Above, plus:
- `CONTRIBUTING.md` - Contribution guidelines
- `LICENSE` - Software license
- `CODE_OF_CONDUCT.md` - Community standards
- `docs/development.md` - Developer setup

**Script**: `propose_docs.py --dry-run` shows proposal without creating files

### Phase 3: User Confirmation

You review the proposal and choose:
- Which files to create
- Which files to update
- What to skip

**Interactive**: Yes/No for each suggested file

### Phase 4: Create Documentation

The skill:
- Creates `/docs` folder if needed
- Generates approved markdown files
- Follows consistent formatting
- Respects existing content
- Uses project-appropriate tone

**Dry-run available**: Preview content before committing

### Phase 5: Integration

Final steps:
- Links new docs from main `README.md`
- Validates markdown formatting
- Shows summary of changes
- Suggests Git commit message

**Script**: `validate_docs.sh` checks quality

## Documentation Templates

Templates defined in `docs_schema.yaml`:

### Minimal Template
```yaml
minimal:
  - README.md
  - docs/getting-started.md
  - docs/usage.md
```

### Standard Template
```yaml
standard:
  - README.md
  - docs/getting-started.md
  - docs/usage.md
  - docs/architecture.md
  - docs/api-reference.md
  - docs/troubleshooting.md
```

### Open-Source Template
```yaml
open-source:
  - README.md
  - CONTRIBUTING.md
  - LICENSE
  - CODE_OF_CONDUCT.md
  - docs/getting-started.md
  - docs/usage.md
  - docs/architecture.md
  - docs/api-reference.md
  - docs/development.md
  - docs/troubleshooting.md
```

## File Structure

Generated documentation follows this structure:

```
project-root/
├── README.md (updated)
├── CONTRIBUTING.md (optional)
├── LICENSE (optional)
├── CODE_OF_CONDUCT.md (optional)
└── docs/
    ├── getting-started.md
    ├── usage.md
    ├── architecture.md
    ├── api-reference.md
    ├── development.md
    └── troubleshooting.md
```

## Examples

### Example 1: Python Library

**Detected**:
- Type: Library
- Language: Python
- Framework: None
- Visibility: Open-source

**Proposed**:
- Standard set + open-source additions
- API reference for all public functions
- Development setup with virtualenv

### Example 2: Next.js Application

**Detected**:
- Type: Web application
- Language: TypeScript
- Framework: Next.js
- Visibility: Closed-source

**Proposed**:
- Standard set only
- Architecture showing page routing
- Environment variable documentation

### Example 3: CLI Tool

**Detected**:
- Type: Command-line tool
- Language: Go
- Framework: Cobra
- Visibility: Open-source

**Proposed**:
- Open-source set
- Command reference with flags
- Installation from source

## Quality Guidelines

### Documentation Standards

**Tone**:
- Clear and concise
- Professional but approachable
- Consistent across files
- Appropriate for audience

**Formatting**:
- Proper markdown syntax
- Code blocks with language tags
- Consistent heading levels
- Working internal links

**Content**:
- Accurate technical details
- Up-to-date examples
- No outdated information
- Respects `.gitignore`

### What Gets Documented

**✅ Include**:
- Public APIs and interfaces
- Setup and installation
- Configuration options
- Common use cases
- Architecture decisions
- Contributing guidelines (if open-source)

**❌ Exclude**:
- Internal implementation details
- Temporary or experimental features
- Sensitive information (keys, secrets)
- Files in `.gitignore`
- This skills system itself

## Bundled Scripts

### analyze_project.sh
```bash
# Usage
bash .github/copilot-skills/document-project/scripts/analyze_project.sh /path/to/project

# Output (JSON)
{
  "project_type": "library",
  "language": "python",
  "framework": "none",
  "visibility": "open-source",
  "has_docs": false,
  "suggested_template": "open-source"
}
```

### propose_docs.py
```bash
# Preview proposal
python .github/copilot-skills/document-project/scripts/propose_docs.py \
  --project-type library \
  --dry-run

# Output: List of suggested files with descriptions
```

### validate_docs.sh
```bash
# Validate markdown
bash .github/copilot-skills/document-project/scripts/validate_docs.sh /path/to/docs

# Checks:
# - Markdown syntax
# - Broken links
# - Heading hierarchy
# - Code block languages
```

## Workflow Options

### Option 1: Full Interactive
```
/document-project
> Analyzes codebase
> Proposes docs
> You approve each file
> Generates approved docs
```

### Option 2: Quick Minimal
```
/document-project --minimal
> Creates basic docs only
> No confirmation needed
> Fast setup
```

### Option 3: Dry Run
```
/document-project --dry-run
> Shows what would be created
> No files written
> Safe preview
```

## Related Skills

- `/git-ops` - Commit documentation changes
- `/pdf-handling` - PDF document manipulation (different from this)
- `/cleanup` - Remove temporary doc artifacts
- `/generate-instructions` - Create copilot-instructions.md

## Notes

- **Self-awareness**: This skill does NOT document itself or the Copilot Skills system
- **Preservation**: Existing docs are never overwritten without confirmation
- **Respect**: Follows `.gitignore` patterns
- **Quality**: All generated markdown is validated before completion
- **Flexibility**: Templates are customizable via `docs_schema.yaml`

---

**Ready to document your project?** Run `/document-project` and let's build clear, comprehensive documentation together.
