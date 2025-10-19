# Example Skills

This folder contains cloned repositories of real-world skills implementations from both Anthropic's official skills and community-contributed skills. These serve as reference examples for implementing the Copilot Skills Architecture.

## Official Skills (Anthropic)

### [anthropics-skills/](./anthropics-skills)

The official Anthropic skills repository containing production-quality skills across multiple categories:

**Document Skills**
- `document-skills/docx` - Word document manipulation
- `document-skills/pdf` - PDF extraction, creation, merging, form handling
- `document-skills/pptx` - PowerPoint presentation creation and editing
- `document-skills/xlsx` - Excel spreadsheet creation and analysis

**Design & Creative**
- `algorithmic-art` - Generative art with p5.js
- `canvas-design` - Visual art design for PNG and PDF
- `slack-gif-creator` - Animated GIF creation

**Development**
- `artifacts-builder` - Claude.ai HTML artifacts with React/Tailwind
- `mcp-server` - MCP server creation guide
- `webapp-testing` - Web application testing with Playwright

**Communication**
- `brand-guidelines` - Anthropic brand application
- `internal-comms` - Internal communication templates

**Skill Creation**
- `skill-creator` - Interactive skill builder

## Community Skills

### [obra-superpowers/](./obra-superpowers)

A comprehensive skills library for Claude Code featuring 20+ battle-tested skills:
- TDD (Test-Driven Development) patterns
- Debugging methodologies
- Collaboration patterns
- `/brainstorm`, `/write-plan`, `/execute-plan` commands
- Skills search functionality

**Repository**: https://github.com/obra/superpowers

### [superpowers-skills/](./superpowers-skills)

Community-editable skills repository for the superpowers project:
- Additional skills contributed by the community
- Patterns and templates
- Integration examples

**Repository**: https://github.com/obra/superpowers-skills

### [tfriedel-claude-office-skills/](./tfriedel-claude-office-skills)

Professional Office document workflows for Claude Code CLI:
- PPTX (PowerPoint) automation
- DOCX (Word) document creation
- XLSX (Excel) spreadsheet management
- PDF operations

**Repository**: https://github.com/tfriedel/claude-office-skills

## How to Use These Examples

### Analyze Skill Structure
Examine how skills are organized in these repos:
```
skill-name/
├── README.md           # Skill documentation
├── skill.md           # Skill definition (if present)
├── requirements.txt   # Dependencies
├── examples/          # Usage examples
└── scripts/           # Executable scripts
```

### Reference Implementations
Use these as reference when implementing skills for the Copilot Skills Architecture:
- Study the documentation structure
- Examine how capabilities are documented
- Review how examples are provided
- Analyze script patterns and organization

### Cross-Reference
When creating `.github/copilot-skills/`, follow the patterns established by:
- Anthropic's official structure for standardization
- Community approaches for alternative patterns
- Office skills for domain-specific examples

## Key Patterns to Learn

1. **Progressive Disclosure**: How detailed information is organized in layers
2. **Script Organization**: How executable utilities are bundled and documented
3. **Dependency Management**: How requirements are declared
4. **Example Provision**: How usage examples are demonstrated
5. **README Structure**: How skills document capabilities to end users

## Next Steps

When implementing skills in `.github/copilot-skills/`:
1. Reference the directory structure from these examples
2. Adapt documentation patterns for your domain
3. Include example scripts similar to patterns here
4. Maintain metadata standards established by official skills

## Notes

- These are shallow clones (`--depth 1`) to keep repository size minimal
- For full history, run `git fetch --unshallow` in any of these directories
- See [awesome-claude-skills.md](../awesome-claude-skills.md) for original repository references
