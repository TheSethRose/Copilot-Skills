# Generate Instructions

---
description: "Generate AI instruction files by analyzing codebase patterns and conventions"
---

Generate `.github/copilot-instructions.md` files that guide AI agents to be immediately productive by analyzing your codebase.

## When to Use This Skill

- Creating AI instruction files for new projects
- Updating existing instructions when architecture changes
- Discovering undocumented patterns and conventions
- Generating context for AI agents (Copilot, Cursor, Claude)
- Documenting project-specific workflows
- Analyzing multi-component architectures
- Consolidating multiple AI convention files

**Keywords**: generate instructions, copilot-instructions, discover patterns, codebase analysis, create instructions, AI instructions

## Instructions

### Phase 0: Respect .gitignore Patterns

**CRITICAL**: Before any analysis, identify files and directories to exclude:

1. **Read `.gitignore` file** (if it exists) and note all patterns
2. **Never analyze, reference, or document**:
   - Environment files (`.env`, `.env.*`, `*.log`)
   - Dependencies (`node_modules/`, `__pycache__/`, `.venv/`, `venv/`, `build/`, `dist/`)
   - IDE directories (`.vscode/`, `.idea/`, `*.iml`)
   - Build artifacts (`*.pyc`, `*.egg-info/`, `package-lock.json`, `yarn.lock`)
   - Temporary files (`*.swp`, `*.swo`, `*~`, `*.bak`, `*.tmp`)
   - OS files (`.DS_Store`, `Thumbs.db`)
   - Any directories/files listed in `.gitignore`

3. **The bundled scripts automatically exclude these patterns**, but when you perform manual analysis:
   - Skip reading files in ignored directories
   - Don't reference ignored files in examples
   - Don't include ignored patterns in documentation
   - Don't analyze code from third-party dependencies

4. **Why this matters**:
   - Prevents documenting sensitive environment variables
   - Avoids analyzing third-party code (not your project's patterns)
   - Focuses on actual project code, not generated files
   - Keeps instructions relevant to maintainable code

### Phase 1: Discover Existing Conventions

1. **Search for existing AI guidance files**:
   ```bash
   bash .github/copilot-skills/copilot-instructions-generator/scripts/discover_conventions.sh --parse
   ```
   Look for: `.github/copilot-instructions.md`, `AGENT.md`, `CLAUDE.md`, `.cursorrules`, `.windsurfrules`

2. **Display findings directly**:
   - Show all discovered files and their content
   - Parse and display their guidance
   - Identify what patterns are already documented

3. **Check for existing file**:
   - If `.github/copilot-instructions.md` exists → proceed to Phase 2 (merge mode)
   - If multiple convention files exist → consolidate them
   - If none exist → generate fresh instructions

### Phase 2: Automated Analysis (Script-Driven)

1. **Run comprehensive codebase analysis**:
   ```bash
   bash .github/copilot-skills/copilot-instructions-generator/scripts/analyze_repo.sh \
     --output .github/copilot-instructions.md \
     --verbose
   ```

2. **Parse terminal output for analysis results**:
   - Display detected project type, frameworks, test framework
   - Extract key findings: project structure, workflows, patterns
   - Read all results from terminal output (no files generated)

3. **Interpret extracted data from terminal**:
   - Project type: Node.js/Python/Go/Java/monorepo
   - Frameworks detected: React, Vue, Express, Django, FastAPI, etc.
   - Testing framework: Jest, pytest, Mocha, Vitest
   - Code formatters: Prettier, ESLint, Black, golangci-lint
   - Extracted scripts/commands from package.json or Makefile
   - Detected patterns: Conventional Commits, feature-based folders, test co-location

### Phase 3: Agent Intelligence (Deep Analysis)

Use agent knowledge to enhance automated findings by investigating:

**Important**: Only analyze files NOT listed in `.gitignore`. Skip `node_modules/`, `.env`, build artifacts, etc.

1. **Project Architecture Understanding**:
   - Read key files: `README.md`, `package.json`, `setup.py`, `go.mod`
   - Identify service boundaries (monorepo packages, microservices)
   - Map component relationships and data flows
   - Document "why" behind architectural decisions

2. **Developer Workflows**:
   - Search for workflow patterns in `.github/workflows/`, `Makefile`, `scripts/`
   - Extract actual build, test, debug, deploy commands
   - Document non-obvious workflow steps
   - Find environment setup requirements

3. **Project-Specific Conventions**:
   - Scan file structure for organization patterns
   - Find naming conventions (kebab-case, PascalCase, snake_case)
   - Identify folder-based patterns (feature/, components/, utils/)
   - Document error handling approaches
   - Find API response/request patterns

4. **Integration Points**:
   - Search for external dependencies in lock files and import statements
   - Identify database connections (Prisma, TypeORM, SQLAlchemy patterns)
   - Find API integration patterns (fetch, axios, requests)
   - Detect authentication/authorization approach (JWT, OAuth, session-based)
   - Locate third-party service integrations

### Phase 4: Intelligent Content Generation

1. **If `.github/copilot-instructions.md` exists (merge mode)**:
   ```bash
   bash .github/copilot-skills/copilot-instructions-generator/scripts/analyze_repo.sh \
     --merge --dry-run --verbose
   ```
   - Show proposed changes
   - Preserve valuable hand-written context
   - Update outdated sections with fresh analysis
   - Keep special warnings/notes intact
   - Merge new patterns with existing guidance

2. **Generate concise, actionable content**:
   - **Avoid**: Generic advice ("write tests", "handle errors")
   - **Include**: Specific examples from THIS codebase
   - **Reference**: Actual file paths and real patterns discovered
   - **Document**: Only discoverable patterns, not aspirational practices
   - **Target length**: 50-100 lines (concise but complete)

3. **Structure generated instructions**:
   ```markdown
   # Copilot Instructions
   
   ## Project Overview
   [High-level architecture from agent analysis + script findings]
   
   ## Technology Stack
   [From script: frameworks, languages, test tools]
   
   ## Project Structure
   [Directory organization with key locations]
   
   ## Development Workflows
   [Extracted commands + agent discovery of workflow steps]
   
   ## Code Patterns & Conventions
   [Naming, organization, error handling, API patterns]
   
   ## Key Components
   [Service boundaries, module responsibilities]
   
   ## Integration Points
   [Databases, APIs, external services]
   
   ## Getting Started
   [Setup commands, first task hints]
   ```

### Phase 5: Quality Validation

1. **Run validator**:
   ```bash
   bash .github/copilot-skills/copilot-instructions-generator/scripts/validate_instructions.sh \
     --file .github/copilot-instructions.md
   ```

2. **Display validation results from terminal**:
   - Show all quality metrics displayed in terminal output
   - Report issues and warnings
   - Verify conciseness, specificity, examples present
   - Validate file references aren't broken

3. **Verify quality standards**:
   - ✓ Conciseness: 50-100 lines
   - ✓ Actionable: specific commands and examples
   - ✓ Discoverable: only patterns observed in codebase
   - ✓ References: real file paths and code patterns
   - ✓ No generic: project-specific content only

## Combined Workflow Examples

### Example 1: Generate Fresh Instructions
```
User: Generate Copilot instructions for this repository

1. Run discover_conventions.sh → show existing files
2. Run analyze_repo.sh → display script findings
3. Agent reads key files (README, package.json, main source)
4. Agent analyzes architecture, workflows, patterns
5. Combine both: script data + agent intelligence
6. Generate .github/copilot-instructions.md
7. Run validation → display results
8. Show generated file and pass/fail status
```

### Example 2: Update Existing Instructions
```
User: Update Copilot instructions after refactoring

1. Check existing .github/copilot-instructions.md
2. Run analyze_repo.sh --merge --dry-run → show changes
3. Agent reviews what changed (new services, patterns)
4. Agent preserves valuable existing context
5. Merge fresh analysis with preserved wisdom
6. Apply updates
7. Validate quality
8. Show diff and confirmation
```

### Example 3: Consolidate Multiple Convention Files
```
User: I have .claude.md, .cursorrules, and AGENT.md

1. discover_conventions.sh --parse → show all files
2. Agent reads all convention files
3. Extract unique insights from each
4. Consolidate into single authoritative file
5. Create unified .github/copilot-instructions.md
6. Reference original files in comments
7. Validate consolidated version
```

### Example 4: Deep Analysis Mode
```
User: Thoroughly analyze this codebase architecture

1. Run full analysis with --verbose
2. Display all script-detected patterns
3. Agent deep-dives into:
   - Read all package.json/setup.py/go.mod files
   - Trace import patterns and service boundaries
   - Analyze all GitHub workflows
   - Find error handling and logging patterns
   - Identify API request/response shapes
4. Extract essential knowledge summary
5. Generate comprehensive instructions
6. Display what agent discovered beyond script
```

## Script Behavior

The analysis automation provides:
1. **Project Type Detection** - Node.js, Python, Go, Java, monorepo patterns
2. **Framework Identification** - React, Vue, Express, Django, FastAPI, etc.
3. **Test Framework Discovery** - Jest, pytest, Mocha, Vitest, etc.
4. **Tool Detection** - Prettier, ESLint, Black, golangci-lint, etc.
5. **Script Extraction** - Build, test, run commands from package.json/Makefile
6. **Pattern Recognition** - Conventional Commits, folder structure, test location
7. **Integration Detection** - Database, API, auth patterns
8. **Convention Scanning** - Existing AGENT.md, .cursorrules files

## Terminal Output Format

All analysis results display directly to terminal (no files created):

```
ℹ Convention File Discovery
[Lists found files if any exist]

ℹ Copilot Instructions Generator - Repository Analysis
→ Detected project type: typescript-monorepo
→ Detected frameworks: React, Express
→ Detected test framework: Jest

Analysis Results:
─────────────────────────────────────────
Project Type: TypeScript Monorepo
Languages: TypeScript, JavaScript
Frameworks: React, Express
Testing: Jest
Patterns Detected:
  ✓ Conventional Commits
  ✓ Feature-based folder structure
  ✓ Test co-location
─────────────────────────────────────────

✓ Repository analysis complete
```

## Success Output

Display generated instructions with:
```
✓ Analysis Complete

## Project Overview
[Generated overview with detected services/components]

## Technology Stack
- TypeScript, React, Express
- Testing: Jest (70% coverage)
- Formatting: Prettier + ESLint
- Database: PostgreSQL (Prisma ORM)

## Development Workflows
- npm run dev          # Start development server
- npm run test         # Run Jest tests
- npm run build        # Production build
- npm run lint         # Check code quality

## Code Patterns & Conventions
- Conventional Commits (feat:, fix:, docs:, refactor:)
- Feature-based folder structure: src/features/{Feature}/*.tsx
- Test co-location: {Module}.test.ts alongside {Module}.ts

## Key Components
- packages/auth/      - Authentication service
- packages/api/       - REST API layer
- packages/web/       - React frontend
- packages/common/    - Shared utilities

✓ Validation: PASS (concise, specific, actionable)
```

## Error Handling

If analysis fails:
- Show specific error from script
- Display what WAS successfully detected
- Suggest remediation (run with --verbose, check .copilot-analysis-config.json)
- Offer to retry or proceed with partial analysis

## Options

- `--merge` - Merge with existing instructions (if file exists)
- `--validate` - Run quality validation after generation
- `--discover` - Find and display all existing convention files
- `--detect-only` - Only detect patterns, show findings, don't generate file
- `--verbose` - Show detailed analysis output
- `--dry-run` - Preview changes without modifying files

## Data Available to Agent

Terminal output provides:
- Project type and language detection results
- Detected frameworks and dependencies (with versions)
- Extracted npm scripts or make targets
- Detected code organization patterns
- Integration points and external services
- Existing convention files and their content
- Validation pass/fail status and specific issues
- Analysis report JSON (can be parsed for details)

Agent can use this plus file reading to generate superior instructions that understand:
- Why the architecture is structured this way
- How all components communicate
- What workflows are essential
- Which patterns are project-specific
- Where to find examples of good code
- What conventions to follow for new work

## Configuration

### Automatic Exclusions

The analyzer automatically respects `.gitignore` patterns and excludes:

- **Dependencies**: `node_modules/`, `__pycache__/`, `.venv/`, `venv/`, `build/`, `dist/`
- **Environment files**: `.env`, `.env.*`, `*.log`
- **IDE directories**: `.vscode/`, `.idea/`
- **Build artifacts**: `*.pyc`, `*.egg-info/`, `package-lock.json`, `yarn.lock`
- **Temporary files**: `*.swp`, `*.swo`, `*~`, `*.bak`, `*.tmp`
- **Project-specific**: `examples/`, `drafts/`

This prevents accidental analysis of sensitive environment variables, third-party code, and generated files.

### Optional Configuration

Create `.copilot-analysis-config.json` for customization:

```json
{
  "projectName": "My Project",
  "description": "Override auto-detected description",
  "patterns": {
    "detectConventionalCommits": true,
    "scanTestPatterns": true,
    "analyzeWorkflows": true,
    "detectIntegrations": true
  },
  "preserve": {
    "sections": ["Custom Warnings", "Security Notes"],
    "patterns": ["DO NOT modify.*legacy"]
  },
  "exclude": {
    "additionalDirectories": ["custom-ignored/"],
    "additionalFiles": ["*.custom"]
  }
}
```

## Troubleshooting

### Script Not Found

```bash
# Ensure scripts are executable
chmod +x .github/copilot-skills/copilot-instructions-generator/scripts/*.sh
```

### Analysis Incomplete

If analysis misses important patterns:

```bash
# Run verbose analysis to see what was detected
bash scripts/analyze_repo.sh --verbose

# Check exclude patterns in config
cat .copilot-analysis-config.json

# Add specific patterns manually
vim .github/copilot-instructions.md

# Re-run after adding patterns
bash scripts/analyze_repo.sh --merge
```

### Validation Fails

If validation reports issues:
- Check for broken file references
- Verify instructions are concise (<150 lines ideal)
- Add specific examples from codebase
- Remove generic advice
- Run with `--verbose` to see detailed checks

