# Contributing to Copilot Skills Architecture

First off, thank you for considering contributing to Copilot Skills Architecture! 🎉

This document provides guidelines for contributing to this project. Following these guidelines helps maintain quality and makes the contribution process smooth for everyone.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Process](#development-process)
- [Style Guidelines](#style-guidelines)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

This project adheres to a code of conduct that we expect all contributors to follow:

- **Be respectful** and inclusive
- **Be collaborative** and supportive
- **Be constructive** with feedback
- **Focus on what is best** for the community

## How Can I Contribute?

### 🐛 Reporting Bugs

Before submitting a bug report:
- Check the [existing issues](https://github.com/TheSethRose/copilot-skills/issues)
- Verify the bug exists in the latest version

When reporting bugs, include:
- Clear, descriptive title
- Steps to reproduce
- Expected vs actual behavior
- Screenshots if applicable
- Your environment (OS, VS Code version, etc.)

### 💡 Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- Use a clear, descriptive title
- Provide detailed description of the proposed feature
- Explain why this enhancement would be useful
- Include examples of how it would work

### 🆕 Creating New Skills

The best way to contribute is by creating new skills! Use the built-in creator:

```
/create-skill
```

Or manually:

1. **Copy templates**
   ```bash
   cp .github/copilot-skills/templates/skill-prompt.template.md \
      .github/prompts/{skill-name}.prompt.md
   
   cp .github/copilot-skills/templates/instructions.template.md \
      .github/instructions/{skill-name}.instructions.md
   ```

2. **Create skill directory** (if needed for scripts/details)
   ```bash
   mkdir -p .github/copilot-skills/{skill-name}/scripts
   ```

3. **Follow the 5 Constitutional Principles**:
   - ✅ Progressive Disclosure
   - ✅ File-Based Organization
   - ✅ Dynamic Discovery
   - ✅ Deterministic Execution
   - ✅ Composability

4. **Register in keyword routing map**
   - Add entry to `.github/copilot-instructions.md`

5. **Document your skill**
   - Add README.md in skill directory
   - Include usage examples
   - Document all scripts

## Development Process

### Setting Up Development Environment

1. **Fork the repository**
   ```bash
   # Click "Fork" on GitHub
   ```

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR-USERNAME/copilot-skills.git
   cd copilot-skills
   ```

3. **Create a branch**
   ```bash
   git checkout -b feature/your-skill-name
   # or
   git checkout -b fix/bug-description
   ```

4. **Make your changes**
   - Follow the style guidelines below
   - Test your skill thoroughly
   - Update documentation

5. **Commit your changes**
   ```bash
   git commit -m "feat(skills): add xyz skill"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-skill-name
   ```

7. **Create a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your branch
   - Fill out the PR template

### Testing Your Skill

Before submitting:

1. **Test the workflow**
   ```
   /your-skill-name
   ```

2. **Verify scripts**
   ```bash
   # Test all scripts in scripts/ directory
   bash .github/copilot-skills/{skill-name}/scripts/script.sh --help
   ```

3. **Check constitutional compliance**
   - ✓ Progressive disclosure structure
   - ✓ Files in correct locations
   - ✓ Scripts output to terminal only
   - ✓ Clear dependencies
   - ✓ Proper keywords registered

4. **Validate markdown**
   ```bash
   # Use the document-project skill
   bash .github/copilot-skills/document-project/scripts/validate_docs.sh \
        .github/copilot-skills/{skill-name}/
   ```

## Style Guidelines

### File Naming

- **Skills**: `kebab-case` (e.g., `pdf-handling`, `git-ops`)
- **Prompts**: `{skill-name}.prompt.md`
- **Instructions**: `{skill-name}.instructions.md`
- **Scripts**: Descriptive names with extension (e.g., `analyze_project.sh`)

### YAML Frontmatter

All prompt and instruction files must have YAML frontmatter:

**Prompt files**:
```yaml
---
description: Brief description of what this skill does
model: Claude Sonnet 4  # Optional
tools: ['search', 'usages', 'fetch']  # Optional
---
```

**Instruction files**:
```yaml
---
description: Auto-loaded context description
---
```

### Markdown Style

- Use ATX-style headings (`#`, `##`, `###`)
- One blank line before and after headings
- Code blocks must have language tags
- Use relative links for internal docs
- Keep lines under 120 characters where reasonable

### Script Guidelines

**All scripts must**:
- Output to stdout/stderr only (no file generation)
- Include usage/help documentation
- Have proper error handling
- Exit with meaningful codes (0=success, 1=error)
- Be executable (`chmod +x`)
- Include shebang line

**Example**:
```bash
#!/bin/bash
set -euo pipefail

usage() {
    echo "Usage: $0 <arg>"
    echo "Description of what script does"
    exit 1
}

[[ $# -eq 0 ]] && usage
[[ "$1" == "-h" || "$1" == "--help" ]] && usage

# Script logic here
echo "Output to terminal only"
exit 0
```

## Commit Messages

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- `feat`: New skill or feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Formatting, missing semicolons, etc.
- `refactor`: Code restructuring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Scopes

- `skills`: Skill-related changes
- `docs`: Documentation
- `scripts`: Script changes
- `templates`: Template updates

### Examples

```bash
feat(skills): add database-migrations skill

Add new skill for managing database schema changes with support
for PostgreSQL, MySQL, and SQLite.

Closes #123

---

fix(skills): correct pdf-handling form field extraction

Fixed issue where nested form fields were not properly extracted.

---

docs: update README with new skill examples

Added examples for the create-skill workflow and improved
quick start section.
```

## Pull Request Process

### Before Submitting

- [ ] Code follows style guidelines
- [ ] All tests pass (if applicable)
- [ ] Documentation is updated
- [ ] Commit messages follow convention
- [ ] Constitutional principles satisfied
- [ ] Scripts tested and working
- [ ] No merge conflicts

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] New skill
- [ ] Bug fix
- [ ] Documentation update
- [ ] Enhancement

## Skill Details (if applicable)
- **Name**: skill-name
- **Purpose**: What problem does it solve?
- **Archetype**: Minimal / Domain Knowledge / Rich Reference / Meta

## Constitutional Compliance
- [ ] Progressive Disclosure
- [ ] File-Based Organization
- [ ] Dynamic Discovery
- [ ] Deterministic Execution
- [ ] Composability

## Testing
Describe how you tested your changes

## Screenshots/Examples
If applicable

## Checklist
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] Commit messages follow convention
- [ ] All tests pass
- [ ] No merge conflicts
```

### Review Process

1. **Automated checks** run on your PR
2. **Maintainer review** (usually within 48 hours)
3. **Feedback** and requested changes (if needed)
4. **Approval** and merge

### After Your PR is Merged

- Delete your branch
- Update your fork
- Celebrate! 🎉

## Areas for Contribution

We especially welcome contributions in these areas:

### 🆕 New Skills

- Database operations (migrations, queries, backups)
- Testing frameworks (unit, integration, e2e)
- Deployment and CI/CD
- API development
- Security scanning
- Performance optimization

### 📚 Documentation

- Improved examples
- Video tutorials
- Blog posts
- Translations

### 🔧 Tooling

- Validation scripts
- Skill generators
- VS Code extension
- CLI tools

### 🐛 Quality

- Bug fixes
- Performance improvements
- Better error messages
- Test coverage

## Questions?

- 💬 [GitHub Discussions](https://github.com/TheSethRose/copilot-skills/discussions)
- 🐛 [GitHub Issues](https://github.com/TheSethRose/copilot-skills/issues)
- 📖 [Architecture Guide](.github/copilot-skills/README.md)

## Recognition

Contributors will be recognized in:
- GitHub contributors page
- Release notes
- README acknowledgments

---

**Thank you for contributing to Copilot Skills Architecture!** 🙏

Every contribution, no matter how small, makes this project better for the entire AI-assisted development community.
