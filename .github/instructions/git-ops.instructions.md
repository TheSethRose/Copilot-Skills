---
description: "Auto-loaded context for Git version control operations: commits, merges, rebases, and GitHub workflows"
applyTo: "**/{.git,.gitignore,.gitattributes,.github}/**"
---

# Git Operations - Automatic Context Instructions

**Related Prompt:** `/git-ops`  
**Related Skill:** `.github/copilot-skills/git-ops/SKILL.md`

**Triggers:** git, commit, merge, rebase, push, pull, branch, checkout, stash, conflict, github, pull request, PR, force push

## Context: Git Version Control Operations

When working with Git-related files or when user queries contain version control keywords, this context is automatically activated.

## Core Principles

### Safety First
- **Always check status** before destructive operations
- **Create backups** before force operations or history rewrites
- **Verify branch** before pushing or merging
- **Preview changes** with `--dry-run` flags when available

### Professional Workflow
- **Atomic commits** - One logical change per commit
- **Descriptive messages** - Use conventional commit format
- **Feature branches** - Never commit directly to main/master
- **Pull before push** - Always sync with remote first

## Default Behaviors

### When user mentions "commit"
1. Suggest `/git-ops` skill prompt
2. Run `git status` to show current state
3. Use conventional commit format: `type(scope): message`
4. Validate commit message length and format
5. Check for common mistakes (large files, secrets, debug code)

### When user mentions "merge" or "rebase"
1. Suggest `/git-ops` skill prompt
2. Check current branch (prevent accidental main branch operations)
3. Verify working directory is clean
4. Show merge/rebase preview
5. Prepare conflict resolution strategy

### When user mentions "push" or "force"
1. Suggest `/git-ops` skill prompt with safety warnings
2. Load `.github/copilot-skills/git-ops/safety.md` for force push guidelines
3. Verify remote branch state
4. Use `--force-with-lease` instead of `--force`
5. Confirm push target is correct

### When user mentions "conflict"
1. Suggest `/git-ops` skill prompt
2. Show conflict files with `git status`
3. Use bundled script: `.github/copilot-skills/git-ops/scripts/conflict_resolver.sh`
4. Explain merge markers and resolution strategies

### When user mentions "worktree" or "isolated workspace"
1. Suggest `/git-ops` skill prompt with worktree workflow
2. Check for existing worktree directories (.worktrees/ or worktrees/)
3. Verify .gitignore includes worktree directory (for project-local)
4. Create worktree with new branch
5. Run project setup (npm install, cargo build, etc.)
6. Verify clean test baseline before work begins

### When user mentions "finish branch" or "complete work"
1. Suggest `/git-ops` skill prompt with branch finishing workflow
2. Verify tests pass before offering options
3. Present 4 completion options: merge locally, create PR, keep as-is, discard
4. Execute chosen workflow
5. Clean up worktree if appropriate

## Quality Guidelines

### ✅ Do
- Check `git status` before any operation
- Use `git log --oneline` to understand history
- Create feature branches from latest main
- Write meaningful commit messages
- Pull before pushing
- Use `--force-with-lease` instead of `--force`
- Verify `.gitignore` patterns before committing
- Use `git diff --staged` to review before commit

### ❌ Don't
- Commit secrets, API keys, or passwords
- Force push to shared branches
- Rebase public history
- Commit directly to main/master
- Use `git add .` without reviewing changes
- Create massive commits (split into logical pieces)
- Ignore merge conflicts
- Commit broken code

## Conventional Commit Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, no logic change)
- `refactor:` - Code refactoring
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks

### Examples
```bash
feat(pdf): add table extraction capability
fix(git-ops): resolve merge conflict detection bug
docs(readme): update installation instructions
refactor(skills): reorganize directory structure
```

## Common Workflows

### Create Feature Branch
```bash
git checkout main
git pull origin main
git checkout -b feature/your-feature-name
```

### Create Isolated Worktree
```bash
# Check for existing worktree directories
ls -d .worktrees 2>/dev/null || ls -d worktrees 2>/dev/null

# Verify .gitignore includes worktree directory
grep -q "^\.worktrees/$" .gitignore || echo ".worktrees/" >> .gitignore

# Create worktree with new branch
git worktree add .worktrees/feature-name -b feature/feature-name

# Navigate to worktree
cd .worktrees/feature-name

# Run project setup
if [ -f package.json ]; then npm install; fi
if [ -f Cargo.toml ]; then cargo build; fi
if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
if [ -f pyproject.toml ]; then poetry install; fi

# Verify clean test baseline
npm test  # or cargo test, pytest, go test
```

### Safe Commit Process
```bash
git status                    # Check what's changed
git diff                      # Review changes
git add <specific-files>      # Stage intentionally
git diff --staged             # Review staged changes
git commit -m "type(scope): message"
git push origin feature/your-feature-name
```

### Finish Development Branch
```bash
# Step 1: Verify tests pass
npm test  # or appropriate test command

# Step 2: Choose completion option
# Option 1: Merge locally
git checkout main
git pull
git merge feature/your-feature-name
npm test  # verify on merged result
git branch -d feature/your-feature-name

# Option 2: Create PR
git push -u origin feature/your-feature-name
gh pr create --title "feat: Description" --body "Summary of changes"

# Option 3: Keep as-is (no action)

# Option 4: Discard (requires confirmation)
git checkout main
git branch -D feature/your-feature-name

# Step 3: Clean up worktree (if used)
git worktree remove .worktrees/feature-name
```

### Resolve Merge Conflicts
```bash
git status                    # See conflicted files
git diff                      # Review conflicts
# Edit files to resolve conflicts
git add <resolved-files>
git commit                    # Complete merge
```

### Undo Operations
```bash
git reset HEAD~1              # Undo last commit (keep changes)
git reset --hard HEAD~1       # Undo last commit (discard changes)
git checkout -- <file>        # Discard file changes
git clean -fd                 # Remove untracked files
```

### List and Manage Worktrees
```bash
git worktree list             # Show all worktrees
git worktree remove <path>    # Remove worktree
git worktree prune            # Clean up stale worktree data
```

## Bundled Scripts

The git-ops skill provides helper scripts:

```bash
# Safe git execution with validation
.github/copilot-skills/git-ops/scripts/git_safe_exec.sh <command>

# Interactive commit helper
.github/copilot-skills/git-ops/scripts/commit_helper.sh

# Conflict resolution assistant
.github/copilot-skills/git-ops/scripts/conflict_resolver.sh
```

## Next Steps

When working with Git:
1. Use `/git-ops` prompt for guided workflows
2. Check `.github/copilot-skills/git-ops/SKILL.md` for core capabilities
3. For safety guidelines, see `.github/copilot-skills/git-ops/safety.md`
4. Run bundled scripts for automated validation

## Related Skills

- **GitHub operations** - For PR creation, issue management, CI/CD
- **Code review** - For reviewing changes before commit
- **Branch management** - For advanced branching strategies
