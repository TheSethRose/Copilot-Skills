---
description: "Auto-loaded context for project creation and scaffolding: initialization, setup, and boilerplate generation"
applyTo: "**/{package.json,requirements.txt,Cargo.toml,go.mod,pom.xml,build.gradle,Gemfile,composer.json}"
---

# New Project Creation - Automatic Context Instructions

**Related Prompt:** `/new-project`  
**Related Skill:** `.github/copilot-skills/skill-template/SKILL.md`

**Triggers:** new project, create project, initialize, setup, scaffold, boilerplate, template, starter, project setup

## Context: Project Creation and Scaffolding

When working with project configuration files or when user queries contain creation/initialization keywords, this context is automatically activated.

## Core Principles

### Project Setup Philosophy
- **Convention over configuration** - Follow ecosystem standards
- **Minimal boilerplate** - Only include what's necessary
- **Clear structure** - Organize files logically from day one
- **Documentation first** - README, .gitignore, and LICENSE before code

### Quality Indicators
- Clean directory structure
- Proper dependency management
- Version control configured
- Development environment documented
- CI/CD pipeline ready

## Default Behaviors

### When user mentions "new project" or "create project"
1. Suggest `/new-project` skill prompt for guided setup
2. Detect project type from context or ask explicitly
3. Check for existing project files to avoid conflicts
4. Use language/framework-specific best practices

### When user mentions "initialize" or "setup"
1. Suggest appropriate initialization commands:
   - Node.js: `npm init` or `pnpm create`
   - Python: `pip install -e .` or `poetry init`
   - Rust: `cargo init`
   - Go: `go mod init`
2. Create essential project files (.gitignore, README.md, LICENSE)
3. Set up development tools (linters, formatters, pre-commit hooks)

### When user mentions "scaffold" or "template"
1. Reference `.github/copilot-skills/skill-template/SKILL.md` for skill creation
2. Use framework-specific scaffolding tools:
   - React: `create-react-app`, `vite`
   - Next.js: `create-next-app`
   - Django: `django-admin startproject`
   - Flask: Manual structure with blueprints
3. Apply framework conventions and best practices

## Language-Specific Defaults

### Python Projects
```bash
# Structure
project/
├── README.md
├── requirements.txt  # or pyproject.toml
├── .gitignore
├── src/
│   └── project/
│       ├── __init__.py
│       └── main.py
└── tests/
    └── test_main.py
```

**Essential files:**
- `requirements.txt` or `pyproject.toml` for dependencies
- `setup.py` or `pyproject.toml` for packaging
- `.gitignore` with Python-specific patterns
- `README.md` with installation and usage instructions

**Tools:**
- Virtual environment: `python -m venv venv`
- Package manager: `pip`, `poetry`, or `pipenv`
- Linting: `ruff`, `pylint`, or `flake8`
- Formatting: `black` or `ruff format`
- Testing: `pytest`

### Node.js Projects
```bash
# Structure
project/
├── README.md
├── package.json
├── .gitignore
├── src/
│   └── index.js
└── tests/
    └── index.test.js
```

**Essential files:**
- `package.json` with scripts and dependencies
- `.gitignore` with `node_modules/`
- `README.md` with setup instructions
- `tsconfig.json` if using TypeScript

**Tools:**
- Package manager: `npm`, `yarn`, or `pnpm`
- Linting: `eslint`
- Formatting: `prettier`
- Testing: `jest`, `vitest`, or `mocha`

### Rust Projects
```bash
# Structure
project/
├── Cargo.toml
├── README.md
├── .gitignore
├── src/
│   └── main.rs
└── tests/
    └── integration_test.rs
```

**Created by:** `cargo init` or `cargo new`

**Tools:**
- Package manager: `cargo` (built-in)
- Linting: `cargo clippy`
- Formatting: `cargo fmt`
- Testing: `cargo test`

## Quality Guidelines

### ✅ Do
- Create `.gitignore` before any code
- Write README.md with setup instructions
- Include LICENSE file (MIT, Apache, GPL)
- Set up virtual environment or dependency isolation
- Add editor config (.editorconfig, .vscode/)
- Include example environment file (.env.example)
- Set up pre-commit hooks for code quality
- Create tests directory structure early

### ❌ Don't
- Commit node_modules/, venv/, or build artifacts
- Use outdated project templates
- Skip documentation
- Hardcode configuration values
- Ignore security dependencies
- Create monolithic file structures
- Forget CI/CD configuration

## Essential Files Checklist

Every new project should include:

```
✅ README.md          - Project description, setup, usage
✅ .gitignore         - Language-specific ignore patterns
✅ LICENSE            - Open source license (if applicable)
✅ .editorconfig      - Editor consistency
✅ .env.example       - Example environment variables
✅ tests/             - Test directory structure
✅ docs/              - Additional documentation
✅ .github/workflows/ - CI/CD pipelines (optional)
```

## Common Templates

### Minimal Python CLI Project
```bash
mkdir project && cd project
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install --upgrade pip
touch requirements.txt README.md .gitignore
mkdir -p src/project tests
```

### Minimal Node.js Project
```bash
mkdir project && cd project
npm init -y
npm install --save-dev eslint prettier jest
touch README.md .gitignore .eslintrc.json .prettierrc
mkdir -p src tests
```

### Minimal Rust Project
```bash
cargo new project
cd project
# cargo automatically creates structure with git
```

## Framework-Specific Commands

### React/Vite
```bash
npm create vite@latest my-app -- --template react-ts
cd my-app
npm install
```

### Next.js
```bash
npx create-next-app@latest my-app --typescript --tailwind --app
cd my-app
npm install
```

### Django
```bash
django-admin startproject myproject
cd myproject
python manage.py startapp myapp
```

### Flask
```bash
mkdir myproject && cd myproject
python -m venv venv
source venv/bin/activate
pip install flask
mkdir app templates static tests
```

## Next Steps

When creating projects:
1. Use `/new-project` prompt for guided project setup
2. Check `.github/copilot-skills/skill-template/SKILL.md` for skill structure reference
3. Follow language/framework conventions
4. Set up development tools before writing code
5. Create tests directory early

## Related Skills

- **Skill creation** - For creating new Copilot skills
- **Configuration** - For setting up linters, formatters, CI/CD
- **Testing setup** - For configuring test frameworks
