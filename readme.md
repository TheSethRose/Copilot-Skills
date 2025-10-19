# Copilot Skills Architecture

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/TheSethRose/copilot-skills?style=social)](https://github.com/TheSethRose/copilot-skills)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**A framework for organizing domain knowledge into reusable, discoverable skills that keep AI agents focused and context-efficient.**

Instead of massive instruction files, this system uses **progressive disclosure** — loading only what's needed, when it's needed. AI agents discover skills automatically through keywords, read core workflows in under 3 minutes, and load detailed information on demand.

## ✨ Features

- 🎯 **Progressive Disclosure** – Information loads in layers (metadata → core → details)
- 🔍 **Dynamic Discovery** – AI agents find skills automatically via keyword routing
- 📦 **Self-Contained Skills** – Each skill includes docs, workflows, and bundled scripts
- ⚖️ **Constitutional Framework** – 5 architectural principles ensure quality and consistency
- 🔧 **Deterministic Execution** – Scripts output to terminal only, no side effects
- 🧩 **Composable** – Skills reference each other with explicit dependencies
- 📚 **Battle-Tested** – Includes reference implementations from Anthropic, Obra, and community

**Status**: ✅ Production-ready with 10+ working skills and comprehensive documentation

---

## 📑 Table of Contents

- [Quick Start](#-quick-start)
- [Documentation](#-documentation)
- [Architecture](#️-architecture)
- [Five Constitutional Principles](#five-constitutional-principles)
- [Project Structure](#project-structure)
- [Development Patterns](#development-patterns)
- [What This Is](#what-this-repository-is)
- [Success Metrics](#success-metrics)
- [Contributing](#-contributing)
- [License](#-license)
- [Support](#-support)

---

## 🚀 Quick Start

### Using Skills in VS Code

1. **Clone this repository**
   ```bash
   git clone https://github.com/TheSethRose/copilot-skills.git
   cd copilot-skills
   ```

2. **Explore available skills**
   ```bash
   # View the keyword routing map
   cat .github/copilot-instructions.md
   ```

3. **Use a skill in Copilot Chat**
   ```
   # In VS Code Copilot Chat
   /pdf-handling
   /git-ops
   /create-skill
   /document-project
   ```

### Creating Your First Skill

Use the built-in skill creator:

```
# In VS Code Copilot Chat
/create-skill

# Or switch to expert mode
/switch Skill Creator
```

Follow the 5-phase guided workflow:
1. 📋 **Discovery** – Answer questions about your skill's purpose
2. 🏗️ **Design** – Get architectural recommendations
3. ✅ **Validation** – Verify constitutional compliance
4. ⚙️ **Implementation** – Generate all required files
5. 🔗 **Integration** – Register and test the skill

### Manual Skill Creation

```bash
# 1. Copy the prompt template
cp .github/copilot-skills/templates/skill-prompt.template.md \
   .github/prompts/{skill-name}.skill.prompt.md

# 2. Copy the instructions template
cp .github/copilot-skills/templates/instructions.template.md \
   .github/instructions/{skill-name}.instructions.md

# 3. Create folder for scripts/detail files (if needed)
mkdir -p .github/copilot-skills/{skill-name}/scripts

# 4. Add scripts for deterministic operations (if needed)
# 5. Register in keyword routing map (.github/copilot-instructions.md)
# 6. Validate against the 5 principles
```

---

## 📖 Documentation

### Core Documentation

| Document | Purpose |
|----------|---------|
| [Architecture Guide](.github/copilot-skills/README.md) | Complete system architecture and design patterns |
| [Constitutional Principles](.specify/memory/constitution.md) | The 5 canonical principles all skills must follow |
| [Keyword Routing Map](.github/copilot-instructions.md) | Main AI guidance and skill discovery |
| [Templates](.github/copilot-skills/templates/) | Quick-start templates for new skills |

### Available Skills

#### Core Skills
- **[PDF Handling]((.github/copilot-skills/pdf-handling/)** – PDF manipulation, form filling, extraction
- **[Git Operations](.github/copilot-skills/git-ops/)** – Version control, commits, merge conflicts
- **[Document Project](.github/copilot-skills/document-project/)** – Generate project documentation
- **[Create Skill](.github/copilot-skills/create-skill/)** – Build new skills with guided workflow
- **[MCP Builder](.github/copilot-skills/mcp-builder/)** – Model Context Protocol server development

#### Utility Skills
- **Cleanup** – Remove stale files and temporary artifacts
- **Brand Guidelines** – Apply consistent branding
- **Generate Instructions** – Auto-generate copilot-instructions.md

### Example Collections

Check the [`examples/`](examples/) directory for third-party skill collections:
- [Anthropic Skills](examples/anthropics-skills/) – Official reference implementations
- [Obra Superpowers](examples/obra-superpowers/) – Advanced development workflows
- [Community Skills](examples/superpowers-skills/) – Community-contributed patterns

---

## 🏗️ Architecture

### Three-Part System

**1. Skill Definitions** (`.github/copilot-skills/{skill-name}/`)

* `SKILL.md` – Core documentation with YAML frontmatter
* `patterns.md`, `reference.md` – Optional detail files
* `scripts/` – Deterministic tools for execution

**2. Skill Prompts** (`.github/prompts/{skill-name}.skill.prompt.md`)

* Tell the AI when to use the skill
* Explain how to run it step-by-step
* Enable `/skill-{name}` commands in Copilot

**3. Instructions Files** (`.github/instructions/{skill-name}.instructions.md`)

* Auto-loaded context for file patterns or keywords
* Default behaviors and quality guidelines
* Common workflows and examples

**4. Management System** (`.github/copilot-skills/`)

* `README.md` – Full system documentation
* `scripts/` – Automation utilities
* `templates/` – Scaffolding for new skills
* `{skill-name}/` – Bundled scripts and detail files

---

### Progressive Disclosure

Information loads in layers:

```
AI Agent Encounters Task
    ↓
    ├→ Check keyword routing map
    │   (Keywords trigger skill suggestion)
    ├→ Load prompt (workflow)
    ├→ Load detail files (patterns.md, reference.md)
    └→ Run scripts/ (execute deterministically)
```

---

## Five Constitutional Principles

All skills must follow these rules (`.specify/memory/constitution.md`):

### 1. Progressive Disclosure

Information appears in small, useful layers, each readable in under 3 minutes.

```
Layer 1: Keyword routing map – Discover
Layer 2: Skill prompt – Understand workflow
Layer 3: Detail files – Learn specifics (patterns.md, reference.md)
Layer 4: Scripts – Execute deterministically
```

### 2. File-Based Structure

Each skill is self-contained with a standard layout.

```
copilot-skills/
└── {skill-name}/
    ├── SKILL.md
    ├── patterns.md (optional)
    ├── reference.md (optional)
    ├── forms.md (optional)
    └── scripts/
```

**Example frontmatter:**

```yaml
---
name: "Skill Name"
description: "Short purpose"
version: "1.0.0"
tags: ["keyword1", "keyword2"]
dependencies: ["tool1", "tool2"]
---
```

### 3. Dynamic Discovery

Skills register in keyword routing map (`.github/copilot-instructions.md`) so AI agents can find them automatically.

| Skill          | Keywords       | Suggest    | Location                  |
| -------------- | -------------- | ---------- | ------------------------- |
| PDF Handling   | pdf, document  | `/pdf-handling` | `.github/prompts/pdf-handling.skill.prompt.md` |

### 4. Deterministic Execution

All scripts must produce consistent, reproducible output.

* Output to terminal only
* No file creation
* Respect `.gitignore`
* Include usage examples
* Compatible with Bash, Python, etc.

### 5. Composability

Skills can depend on others, but never in loops.

```yaml
dependencies:
  - "git-ops"
  - "pdf-handling"
```

---

## Project Structure

*(kept intact, just cleaned and aligned)*

```
copilot-skills/
├── .github/
│   ├── copilot-instructions.md       # Keyword routing map
│   ├── prompts/                      # Skill workflows
│   │   └── {skill-name}.skill.prompt.md
│   ├── instructions/                 # Auto-loaded context
│   │   └── {skill-name}.instructions.md
│   ├── copilot-skills/               # Bundled scripts + details
│   │   ├── README.md
│   │   ├── templates/
│   │   ├── scripts/
│   │   └── {skill-name}/
│   └── .specify/memory/constitution.md
├── examples/
├── .gitignore
├── readme.md
└── ...
```

---

## Development Patterns

### Bundled Scripts

Scripts are deterministic tools that:

* Output to terminal only
* Respect `.gitignore`
* Produce the same results every time
* Work in any repo context
* Include clear examples

Example:

```bash
bash .github/copilot-skills/{skill-name}/scripts/tool.sh --option value
```

### Respecting .gitignore

All scripts ignore:

* `.env`, `*.log`, `node_modules/`, `__pycache__/`, `.venv/`, etc.
* IDE and build artifacts
* Temporary or example files

This prevents leaks, noise, and irrelevant analysis.

### Templates for Speed

Templates make new skills easy to create:

```bash
.github/copilot-skills/templates/SKILL.template.md
.github/copilot-skills/templates/skill-prompt.template.md
.github/copilot-skills/templates/detail-file.template.md
.github/copilot-skills/templates/script.template.{sh,py}
```

---

## What This Repository Is

**Copilot Skills Architecture** is:

✅ A **framework** for organizing AI agent knowledge into reusable modules  
✅ A **reference implementation** of progressive disclosure patterns  
✅ A **template system** for creating new skills quickly  
✅ A **collection** of battle-tested skills for common development tasks  
✅ A **methodology** for keeping AI context focused and efficient  
✅ **Portable** across teams, projects, and AI agents

## What This Repository Is Not

❌ Not a deployable application with a runtime  
❌ Not source code for a specific product  
❌ Not a CI/CD or build system  
❌ Not tied to any specific AI model or platform  
❌ Not a replacement for proper code documentation

**Think of it as**: A design pattern library for AI agent interactions, similar to how design systems work for UI components.

---

## 📊 Success Metrics

This system is designed to achieve:

- ⚡ **Discovery**: AI finds the right skill in <2 minutes
- 📖 **Readability**: Core workflow scannable in <3 minutes  
- 🎯 **Efficiency**: Context usage reduced by 60%+
- 🔧 **Simplicity**: 95% of tasks use ≤2 skills
- 🚀 **Speed**: New skills created in <30 minutes
- ⚙️ **Reliability**: Scripts produce deterministic output
- 🔒 **Safety**: All `.gitignore` rules respected
- 🧩 **Composability**: Skills reference each other clearly

---

## 🔑 Key Resources

| Resource | Description |
|----------|-------------|
| [📘 Copilot Instructions](.github/copilot-instructions.md) | Main AI guidance and keyword routing map |
| [🏗️ Architecture Guide](.github/copilot-skills/README.md) | Complete system architecture |
| [⚖️ Constitutional Principles](.specify/memory/constitution.md) | The 5 canonical principles |
| [📝 Templates](.github/copilot-skills/templates/) | Quick-start templates |
| [🎯 Skill Prompts](.github/prompts/) | Workflow definitions |
| [📚 Instructions](.github/instructions/) | Auto-loaded context |
| [💡 Examples](examples/) | Third-party skill collections |

---

## 🤝 Contributing

We welcome contributions! Here's how to get involved:

### Adding a New Skill

1. **Use the skill creator** (recommended)
   ```
   /create-skill
   ```

2. **Or create manually**
   ```bash
   # Copy templates
   cp .github/copilot-skills/templates/skill-prompt.template.md \
      .github/prompts/{skill-name}.prompt.md
   
   cp .github/copilot-skills/templates/instructions.template.md \
      .github/instructions/{skill-name}.instructions.md
   
   # Create skill directory (if needed)
   mkdir -p .github/copilot-skills/{skill-name}/scripts
   ```

3. **Follow the 5 constitutional principles**
   - Progressive Disclosure
   - File-Based Organization
   - Dynamic Discovery
   - Deterministic Execution
   - Composability

4. **Register in keyword routing map**
   - Add entry to `.github/copilot-instructions.md`

5. **Submit a pull request**
   - Include skill prompt, instructions, and documentation
   - Add tests/examples if applicable
   - Update this README with new skill

### Contribution Guidelines

- **Code Style**: Follow existing patterns in the repository
- **Documentation**: Update relevant docs with your changes
- **Testing**: Test your skill end-to-end before submitting
- **Commits**: Use conventional commit format (`feat(skills): add xyz skill`)
- **PRs**: One skill per PR, include motivation and examples

### Areas for Contribution

- 🆕 New skills for common development tasks
- 📚 Improved documentation and examples
- 🐛 Bug fixes and quality improvements
- 🌍 Translations and internationalization
- 🔧 Tooling and automation improvements

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Anthropic** – For the Claude Skills reference implementation and progressive disclosure patterns
- **Obra** – For Superpowers skills and advanced development workflows  
- **VS Code Team** – For the extensible Copilot platform
- **Community Contributors** – For sharing skills and improvements

---

## 📞 Support

- 💬 **Discussions**: [GitHub Discussions](https://github.com/TheSethRose/copilot-skills/discussions)
- 🐛 **Issues**: [GitHub Issues](https://github.com/TheSethRose/copilot-skills/issues)
- 📖 **Documentation**: See [Architecture Guide](.github/copilot-skills/README.md)
- 🌟 **Star this repo** if you find it useful!

---

## 🗺️ Roadmap

- [ ] More built-in skills (database, testing, deployment)
- [ ] Skill marketplace and discovery platform
- [ ] VS Code extension for skill management
- [ ] Automated skill validation CI/CD
- [ ] Multi-language support (beyond English)
- [ ] Performance metrics and analytics
- [ ] Skill composition tools

---

<p align="center">
  <strong>Built with ❤️ for the AI-assisted development community</strong>
</p>

<p align="center">
  <a href="#copilot-skills-architecture">Back to Top ↑</a>
</p>

## Learning Path

**Beginner**

1. Read this README
2. Check keyword routing map in `.github/copilot-instructions.md`
3. Try a skill command (e.g., `/pdf-handling`)
4. Explore its scripts/
5. Review the 5 principles

**Intermediate**

1. Study `.github/copilot-skills/README.md`
2. Compare multiple skills
3. Read `.github/copilot-instructions.md`
4. Review prompts in `/prompts/`
5. Understand progressive disclosure

**Advanced**

1. Copy templates
2. Write SKILL.md and prompt
3. Add scripts that output deterministically
4. Register and validate

---

## Principles in Action

**Problem:** AI agents drown in large instruction files
**Solution:** Break knowledge into discoverable, layered skills

**Before**

```
One 500-line instruction file:
- Hard to scan
- High context cost
- Poor relevance
```

**After**

```
Keyword routing map → skill discovery
prompt.md → workflow
detail files (patterns.md, reference.md) → specifics
scripts/ → deterministic actions
```

---

## References

* IEEE/ACM: Progressive Disclosure Patterns
* Anthropic Claude Skills: Reference implementation
* Model Context Protocol (MCP): Composition model
* Documentation Architecture: Information layering