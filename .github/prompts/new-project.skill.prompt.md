# New Project Setup Assistant

---
description: "Guide for creating new projects with proper scaffolding, dependencies, and configuration"
---

# New Project Creation

Set up new projects with language/framework-specific best practices, proper structure, and essential tooling.

## When to Use This Skill

- Starting a new project from scratch
- Scaffolding a new application or library
- Setting up proper project structure
- Configuring development environment
- Initializing version control and tooling

**Keywords**: new project, create project, initialize, setup, scaffold, boilerplate, template, starter, project setup

## Workflow

### Step 1: Determine Project Type

Ask user what type of project they want to create:
- **Web Application** (React, Next.js, Vue, etc.)
- **Backend Service** (Node.js, Python, Go, Rust)
- **CLI Tool** (Python, Rust, Go, Node.js)
- **Library/Package** (for distribution)
- **Mobile App** (React Native, Flutter)
- **Desktop App** (Electron, Tauri)

### Step 2: Choose Language/Framework

Based on project type, suggest appropriate options:
- Node.js: Express, Fastify, Nest.js
- Python: Flask, Django, FastAPI
- Rust: Actix, Axum, Rocket
- Go: Gin, Echo, Fiber

### Step 3: Initialize Project

Run appropriate initialization commands:

```bash
# Node.js/TypeScript
npm create vite@latest my-app -- --template react-ts
# or
npx create-next-app@latest my-app --typescript

# Python
mkdir my-project && cd my-project
python -m venv venv
source venv/bin/activate
touch requirements.txt

# Rust
cargo new my-project
cd my-project

# Go
mkdir my-project && cd my-project
go mod init github.com/username/my-project
```

### Step 4: Create Essential Files

Always create:
1. **README.md** - Project description, setup instructions, usage
2. **.gitignore** - Language-specific ignore patterns
3. **LICENSE** - Open source license (MIT, Apache, GPL)
4. **.editorconfig** - Editor consistency
5. **.env.example** - Example environment variables
6. **tests/** - Test directory structure

### Step 5: Set Up Development Tools

Configure:
- **Linting**: ESLint, Pylint, Clippy
- **Formatting**: Prettier, Black, rustfmt
- **Testing**: Jest, pytest, cargo test
- **Type Checking**: TypeScript, mypy
- **Pre-commit Hooks**: husky, pre-commit

### Step 6: Initialize Git

```bash
git init
git add .
git commit -m "chore: initial project setup"
```

### Step 7: Create Initial Structure

Set up directory structure based on project type:

**Web App:**
```
src/
  components/
  pages/
  utils/
  styles/
tests/
public/
```

**Backend Service:**
```
src/
  routes/
  controllers/
  models/
  middleware/
  utils/
tests/
```

**CLI Tool:**
```
src/
  commands/
  utils/
tests/
```

### Step 8: Document Setup Instructions

Add to README.md:
- Installation steps
- Development commands
- Testing instructions
- Deployment process

## Examples

### Example 1: React App with TypeScript
```bash
npm create vite@latest my-app -- --template react-ts
cd my-app
npm install
npm install --save-dev @typescript-eslint/eslint-plugin prettier
echo "node_modules/" > .gitignore
git init
```

### Example 2: Python CLI Tool
```bash
mkdir my-cli && cd my-cli
python -m venv venv
source venv/bin/activate
touch requirements.txt README.md .gitignore LICENSE
mkdir -p src/my_cli tests
echo "venv/" >> .gitignore
git init
```

### Example 3: Rust Web Service
```bash
cargo new my-service
cd my-service
cargo add actix-web tokio serde
mkdir -p src/routes src/models
git add .
git commit -m "chore: initial project setup"
```

## Quality Checklist

Before completing, verify:
- [ ] README.md with setup instructions exists
- [ ] .gitignore with proper patterns exists
- [ ] LICENSE file included (if applicable)
- [ ] Package manager files created (package.json, Cargo.toml, etc.)
- [ ] Tests directory structure created
- [ ] Development tools configured (linter, formatter)
- [ ] .env.example for environment variables
- [ ] Git repository initialized
- [ ] Initial commit made

## Notes

- Always use latest stable versions of tools
- Follow language/framework community conventions
- Include security best practices from start
- Set up CI/CD early (GitHub Actions, etc.)
- Document development workflow clearly

## Related Skills

- **Git Ops** - Version control setup and workflows
- **Cleanup** - Remove unnecessary boilerplate
- **MCP Builder** - For creating MCP server projects specifically
