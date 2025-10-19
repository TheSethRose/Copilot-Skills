---
name: git-ops
description: Safe git operations including commits, branches, merges, worktrees, and GitHub workflows
version: "2.0.0"
tags: ["git", "github", "version-control", "worktrees", "branches"]
dependencies: ["git", "gh"]
---

# Git Operations

## Overview

Comprehensive git operations toolkit with safety-first approach, including isolated worktrees and branch finishing workflows.

**Keywords**: git, commit, merge, rebase, push, pull, branch, checkout, stash, conflict, github, pull request, PR, worktree, isolated workspace

## Core Capabilities

### Basic Operations
- **Commit**: Safe commit process with validation
- **Branch**: Create and manage feature branches
- **Merge**: Merge branches with conflict detection
- **Rebase**: Rebase with safety checks
- **Push/Pull**: Remote synchronization with validation

### Advanced Workflows
- **Worktrees**: Isolated workspaces for parallel development
- **Finish Branch**: Complete development with multiple options
- **Conflict Resolution**: Guided merge conflict resolution
- **Undo Operations**: Safe ways to revert changes

### Safety Features
- **Pre-flight Checks**: Status verification before operations
- **Backup Creation**: Automatic backups for risky operations
- **Dry Run Mode**: Preview changes before execution
- **Force Protection**: Require explicit confirmation for destructive operations

## Git Worktrees

### Overview

Git worktrees create isolated workspaces sharing the same repository, allowing work on multiple branches simultaneously without switching contexts.

**Core Principle**: Systematic directory selection + safety verification = reliable isolation

### Directory Selection Process

Follow this priority order:

1. **Check Existing Directories**
   ```bash
   ls -d .worktrees 2>/dev/null     # Preferred (hidden)
   ls -d worktrees 2>/dev/null      # Alternative
   ```
   If found, use that directory. If both exist, `.worktrees` wins.

2. **Check Project Documentation**
   Look for preferences in `CLAUDE.md`, `.github/copilot-instructions.md`, or README

3. **Ask User**
   If no directory exists and no preference specified:
   - `.worktrees/` (project-local, hidden)
   - `worktrees/` (project-local, visible)
   - `~/.config/copilot-skills/worktrees/<project-name>/` (global location)

### Safety Verification

**For Project-Local Directories** (`.worktrees` or `worktrees`):

**MUST verify .gitignore before creating worktree:**

```bash
# Check if directory pattern in .gitignore
grep -q "^\.worktrees/$" .gitignore || grep -q "^worktrees/$" .gitignore
```

**If NOT in .gitignore:**
1. Add appropriate line to .gitignore
2. Commit the change immediately
3. Proceed with worktree creation

**Why Critical**: Prevents accidentally committing worktree contents to repository.

**For Global Directory** (`~/.config/copilot-skills/worktrees`):
- No .gitignore verification needed - outside project entirely

### Worktree Creation Steps

#### 1. Detect Project Name
```bash
project=$(basename "$(git rev-parse --show-toplevel)")
```

#### 2. Create Worktree
```bash
# Determine full path based on location choice
case $LOCATION in
  .worktrees|worktrees)
    path="$LOCATION/$BRANCH_NAME"
    ;;
  ~/.config/copilot-skills/worktrees/*)
    path="~/.config/copilot-skills/worktrees/$project/$BRANCH_NAME"
    ;;
esac

# Create worktree with new branch
git worktree add "$path" -b "$BRANCH_NAME"
cd "$path"
```

#### 3. Run Project Setup

Auto-detect and run appropriate setup:

```bash
# Node.js
if [ -f package.json ]; then npm install; fi

# Rust
if [ -f Cargo.toml ]; then cargo build; fi

# Python
if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
if [ -f pyproject.toml ]; then poetry install; fi

# Go
if [ -f go.mod ]; then go mod download; fi

# Ruby
if [ -f Gemfile ]; then bundle install; fi
```

#### 4. Verify Clean Baseline

Run tests to ensure worktree starts clean:

```bash
# Examples - use project-appropriate command
npm test
cargo test
pytest
go test ./...
bundle exec rspec
```

**If tests fail**: Report failures, ask whether to proceed or investigate.
**If tests pass**: Report ready.

#### 5. Report Location

```
Worktree ready at <full-path>
Tests passing (<N> tests, 0 failures)
Ready to implement <feature-name>
```

### Worktree Management

```bash
# List all worktrees
git worktree list

# Remove worktree
git worktree remove <path>

# Prune stale worktree administrative data
git worktree prune

# Move worktree to new location
git worktree move <source> <destination>

# Lock worktree (prevent removal)
git worktree lock <path>

# Unlock worktree
git worktree unlock <path>
```

## Finishing a Development Branch

### Overview

Guide completion of development work by presenting clear options and handling chosen workflow.

**Core Principle**: Verify tests → Present options → Execute choice → Clean up

### The Process

#### Step 1: Verify Tests

**Before presenting options, verify tests pass:**

```bash
# Run project's test suite
npm test     # Node.js
cargo test   # Rust
pytest       # Python
go test ./...  # Go
bundle exec rspec  # Ruby
```

**If tests fail:**
```
Tests failing (<N> failures). Must fix before completing:

[Show failures]

Cannot proceed with merge/PR until tests pass.
```

**Stop. Don't proceed to Step 2.**

**If tests pass**: Continue to Step 2.

#### Step 2: Determine Base Branch

```bash
# Try common base branches
git merge-base HEAD main 2>/dev/null || \
git merge-base HEAD master 2>/dev/null || \
git merge-base HEAD develop 2>/dev/null
```

Or ask: "This branch split from main - is that correct?"

#### Step 3: Present Options

Present exactly these 4 options:

```
Implementation complete. What would you like to do?

1. Merge back to <base-branch> locally
2. Push and create a Pull Request
3. Keep the branch as-is (I'll handle it later)
4. Discard this work

Which option?
```

**Don't add explanation** - keep options concise.

#### Step 4: Execute Choice

**Option 1: Merge Locally**

```bash
# Switch to base branch
git checkout <base-branch>

# Pull latest
git pull

# Merge feature branch
git merge <feature-branch>

# Verify tests on merged result
<test command>

# If tests pass
git branch -d <feature-branch>
```

Then: Cleanup worktree (Step 5)

**Option 2: Push and Create PR**

```bash
# Push branch
git push -u origin <feature-branch>

# Create PR
gh pr create --title "<title>" --body "$(cat <<'EOF'
## Summary
<2-3 bullets of what changed>

## Test Plan
- [ ] <verification steps>

## Related Issues
Closes #<issue-number>
EOF
)"
```

Then: Cleanup worktree (Step 5)

**Option 3: Keep As-Is**

Report: "Keeping branch <name>. Worktree preserved at <path>."

**Don't cleanup worktree.**

**Option 4: Discard**

**Confirm first:**
```
This will permanently delete:
- Branch <name>
- All commits: <commit-list>
- Worktree at <path>

Type 'discard' to confirm.
```

Wait for exact confirmation.

If confirmed:
```bash
git checkout <base-branch>
git branch -D <feature-branch>
```

Then: Cleanup worktree (Step 5)

#### Step 5: Cleanup Worktree

**For Options 1, 2, 4:**

Check if in worktree:
```bash
git worktree list | grep $(git branch --show-current)
```

If yes:
```bash
# Exit worktree first
cd $(git rev-parse --show-toplevel)

# Remove worktree
git worktree remove <worktree-path>
```

**For Option 3**: Keep worktree.

### Completion Options Quick Reference

| Option | Merge | Push | Keep Worktree | Cleanup Branch |
|--------|-------|------|---------------|----------------|
| 1. Merge locally | ✓ | - | - | ✓ |
| 2. Create PR | - | ✓ | ✓ | - |
| 3. Keep as-is | - | - | ✓ | - |
| 4. Discard | - | - | - | ✓ (force) |

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
- `perf:` - Performance improvements
- `ci:` - CI/CD changes

### Examples
```bash
feat(worktrees): add isolated workspace creation
fix(git-ops): resolve merge conflict detection bug
docs(readme): update worktree usage instructions
refactor(skills): reorganize git operations structure
chore(deps): update git version requirement
```

## Bundled Scripts

Located in `.github/copilot-skills/git-ops/scripts/`:

```bash
# Safe git execution with validation
./git_safe_exec.sh [--dry-run] [--backup] <command>

# Interactive commit helper
./commit_helper.sh [--type <type>] [--scope <scope>]

# Conflict resolution assistant
./conflict_resolver.sh [--summary] [--interactive]
```

All scripts output to terminal (no file generation) for AI parsing.

## Best Practices

### Worktree Usage
- ✅ Use `.worktrees/` for project-local (hidden from file browsers)
- ✅ Verify .gitignore before creating project-local worktrees
- ✅ Run project setup (npm install, etc.) in new worktrees
- ✅ Verify clean test baseline before starting work
- ✅ Clean up worktrees after merging/completing work
- ❌ Don't commit worktree directories to repository
- ❌ Don't skip test verification in new worktrees
- ❌ Don't create worktrees without .gitignore safety check

### Branch Finishing
- ✅ Always verify tests pass before presenting options
- ✅ Present exactly 4 options (merge, PR, keep, discard)
- ✅ Get typed confirmation for discard option
- ✅ Verify tests on merged result (Option 1)
- ✅ Clean up worktrees for Options 1, 2, 4
- ❌ Don't proceed with failing tests
- ❌ Don't merge without verifying tests on result
- ❌ Don't automatically cleanup worktrees (check option first)
- ❌ Don't force-push without explicit request

### General Safety
- ✅ Check `git status` before any operation
- ✅ Use `git diff --staged` to review before commit
- ✅ Pull before pushing
- ✅ Use `--force-with-lease` instead of `--force`
- ✅ Create feature branches from latest main
- ❌ Don't commit secrets, API keys, or passwords
- ❌ Don't force push to shared branches
- ❌ Don't rebase public history
- ❌ Don't commit directly to main/master

## Progressive Disclosure

For additional details:
- **Safety Guidelines**: Advanced safety patterns and recovery procedures
- **Conflict Resolution**: Deep dive into merge conflict strategies
- **GitHub Integration**: PR templates, code review workflows
- **Advanced Worktrees**: Complex worktree scenarios and troubleshooting

## Related Skills

- **GitHub Operations** - PR creation, issue management, CI/CD
- **Code Review** - Review changes before commit
- **Branch Management** - Advanced branching strategies
- **Cleanup** - Remove stale branches and worktrees
