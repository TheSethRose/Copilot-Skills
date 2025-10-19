# Document Project - Project Documentation Generator

---
name: "Document Project"
description: "Generate clear, structured documentation for any codebase"
version: "1.0.0"
tags: ["documentation", "markdown", "project-docs", "meta"]
dependencies: []
---

Generate comprehensive project documentation by analyzing codebases, proposing appropriate docs, and building a `/docs` folder with quality markdown files.

## Quick Links

- **Slash Command**: `/document-project`
- **Skill Prompt**: `.github/prompts/document-project.prompt.md`
- **Instructions**: `.github/instructions/document-project.instructions.md`
- **Scripts**: `.github/copilot-skills/document-project/scripts/`

## What This Skill Does

**Document Project** analyzes your repository and generates appropriate documentation:

1. **Analyzes** codebase structure (language, framework, type)
2. **Proposes** relevant documentation files
3. **Confirms** with you before creating anything
4. **Generates** markdown files in `/docs` folder
5. **Validates** output quality and links from README

## Key Features

- 🔍 **Smart Analysis** - Detects project type, language, framework automatically
- 📚 **Template-Based** - Uses minimal, standard, or open-source templates
- ✅ **Safe Generation** - Dry-run mode previews before creating files
- 🎯 **Quality Focused** - Validates markdown syntax, links, formatting
- 🔗 **Well-Integrated** - Links documentation from main README
- 🚫 **Self-Aware** - Never documents the Copilot Skills system itself

## When to Use

- Starting a new project and need documentation structure
- Existing project lacks documentation
- Want to standardize docs across multiple repos
- Need to generate API reference from code
- Open-sourcing a project (CONTRIBUTING, LICENSE, CODE_OF_CONDUCT)

## The 5-Phase Workflow

### 1. Analyze (Automatic)
Detects:
- Project type (library, app, CLI, service)
- Primary language and framework
- Open-source vs closed-source
- Existing documentation

### 2. Propose (Smart Suggestions)
Suggests one of three templates:

**Minimal** (2-3 files)
- README.md
- docs/getting-started.md
- docs/usage.md

**Standard** (5-6 files)
- Above + architecture, API reference, troubleshooting

**Open-Source** (9-10 files)
- Above + CONTRIBUTING, LICENSE, CODE_OF_CONDUCT, development guide

### 3. Confirm (Your Control)
You decide:
- Which files to create
- Which files to update
- What to skip

### 4. Generate (Quality Output)
Creates:
- `/docs` folder structure
- Markdown files with proper formatting
- Code examples in project language
- Consistent tone and style

### 5. Integrate (Completion)
Finalizes:
- Links docs from main README
- Validates all markdown
- Shows summary of changes
- Suggests Git commit message

## Documentation Templates

### Minimal Template
```
project-root/
├── README.md (updated)
└── docs/
    ├── getting-started.md
    └── usage.md
```

### Standard Template
```
project-root/
├── README.md (updated)
└── docs/
    ├── getting-started.md
    ├── usage.md
    ├── architecture.md
    ├── api-reference.md
    └── troubleshooting.md
```

### Open-Source Template
```
project-root/
├── README.md (updated)
├── CONTRIBUTING.md
├── LICENSE
├── CODE_OF_CONDUCT.md
└── docs/
    ├── getting-started.md
    ├── usage.md
    ├── architecture.md
    ├── api-reference.md
    ├── development.md
    └── troubleshooting.md
```

## Bundled Scripts

### 1. analyze_project.sh
Analyzes repository structure and outputs project metadata.

**Usage**:
```bash
bash scripts/analyze_project.sh /path/to/project
```

**Output** (JSON):
```json
{
  "project_type": "library",
  "language": "python",
  "framework": "none",
  "visibility": "open-source",
  "has_docs": false,
  "suggested_template": "open-source"
}
```

### 2. propose_docs.py
Suggests documentation files based on project analysis.

**Usage**:
```bash
python scripts/propose_docs.py --project-type library --dry-run
```

**Features**:
- `--dry-run`: Preview without creating files
- `--minimal`: Force minimal template
- `--force`: Skip confirmations

### 3. validate_docs.sh
Validates generated markdown for quality.

**Usage**:
```bash
bash scripts/validate_docs.sh /path/to/docs
```

**Checks**:
- Valid markdown syntax
- No broken internal links
- Proper heading hierarchy
- Code blocks have language tags
- Consistent formatting

### 4. docs_schema.yaml
Defines documentation templates and structure.

**Contents**:
- Template definitions (minimal, standard, open-source)
- File descriptions
- Required vs optional files
- Content guidelines

## Examples

### Example 1: Python Library

**Command**: `/document-project`

**Analysis**:
- Type: Library
- Language: Python
- Framework: setuptools
- Visibility: Open-source (has LICENSE)

**Generated**:
- README.md (enhanced with badges, installation)
- CONTRIBUTING.md (PR process, code style)
- LICENSE (MIT)
- docs/getting-started.md (pip install, imports)
- docs/usage.md (code examples)
- docs/api-reference.md (function signatures)
- docs/development.md (venv setup, testing)

### Example 2: Next.js App

**Command**: `/document-project`

**Analysis**:
- Type: Web application
- Language: TypeScript
- Framework: Next.js 14
- Visibility: Closed-source

**Generated**:
- docs/getting-started.md (env vars, npm install)
- docs/usage.md (page routing, components)
- docs/architecture.md (folder structure, API routes)
- docs/troubleshooting.md (common errors)

### Example 3: Go CLI Tool

**Command**: `/document-project`

**Analysis**:
- Type: CLI tool
- Language: Go
- Framework: Cobra
- Visibility: Open-source

**Generated**:
- Full open-source template
- Command reference (from `--help`)
- Installation from source
- Homebrew formula example

## Quality Standards

### Markdown Formatting
- Proper heading hierarchy (H1 → H2 → H3)
- Code blocks with language tags
- Working internal links
- Consistent list formatting

### Content Quality
- Clear and concise
- Accurate technical details
- Up-to-date examples
- Appropriate for audience

### What Gets Documented
✅ Public APIs and interfaces  
✅ Setup and configuration  
✅ Common use cases  
✅ Architecture decisions  
✅ Contributing guidelines (if open-source)

### What Doesn't
❌ Internal implementation details  
❌ Temporary/experimental features  
❌ Sensitive information  
❌ Files in `.gitignore`  
❌ This Copilot Skills system

## Integration with Other Skills

- `/git-ops` - Commit documentation changes
- `/cleanup` - Remove temporary doc artifacts
- `/pdf-handling` - Different skill for PDF manipulation

## Workflow Options

### Interactive (Default)
```
/document-project
> Full analysis and proposal
> Confirmation for each file
> Generates approved docs
```

### Quick Minimal
```
/document-project --minimal
> Creates basic docs only
> No confirmation
> Fast setup
```

### Dry Run
```
/document-project --dry-run
> Shows what would be created
> No files written
> Safe preview
```

## Files in This Directory

```
document-project/
├── README.md (this file)
├── docs_schema.yaml
├── scripts/
│   ├── analyze_project.sh
│   ├── propose_docs.py
│   └── validate_docs.sh
└── examples/
    ├── python-library.md
    ├── nextjs-app.md
    └── go-cli.md
```

## Getting Started

1. Navigate to your project
2. Run `/document-project`
3. Review proposed documentation
4. Confirm what to create
5. Review generated files
6. Commit with `/git-ops`

## Self-Awareness Rule

This skill generates documentation for **user projects**, NOT for:
- The Copilot Skills system
- Skill architecture files
- This skill's own implementation
- Other skills

The skills system has its own documentation in:
- `.github/copilot-instructions.md`
- `.github/copilot-skills/README.md`

## Support

- 💬 Questions? Use `/document-project` command
- 📖 Need details? See `.github/instructions/document-project.instructions.md`
- 🔍 See examples? Check `examples/` directory

---

**Ready to document your project?** Run `/document-project` and let's build clear, comprehensive documentation together!
