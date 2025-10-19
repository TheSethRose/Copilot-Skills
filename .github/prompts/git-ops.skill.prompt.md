# Git Operations Assistant

---
name: "Git Operations Assistant"
description: "Safely perform git operations including commits, branches, merges, and GitHub remote interactions"
version: "1.0.0"
created: "2025-10-19"
tags: ["git", "github", "version-control", "repository", "safety"]
dependencies: ["git", "gh"]
scripts:
  - ".github/copilot-skills/git-ops/scripts/git_safe_exec.sh"
  - ".github/copilot-skills/git-ops/scripts/commit_helper.sh"
  - ".github/copilot-skills/git-ops/scripts/conflict_resolver.sh"
---

This command guides you through safe git operations with automatic safety checks and backups.

## When to Use This Skill

- Inspect repository state and history
- Stage and commit changes with meaningful messages
- Create and manage feature branches
- Create isolated worktrees for parallel development
- Merge or rebase with conflict detection
- Finish development branches with multiple completion options
- Push/pull with upstream validation
- Safely revert commits or recover from errors
- Handle complex workflows (conflicts, rebases, cherry-picks, worktrees)

## Safety Rules

1. **Never delete branches or files** without explicit user confirmation
2. **Never force push or hard reset** unless user adds explicit override
3. Always perform `git status` + `git diff` before mutating actions
4. For multi-step commands, show preview before execution
5. Create automatic backups before critical operations (via script flags)
6. Validate working tree cleanliness before complex operations
7. Use `--dry-run` flags when available

## User Input

```text
$ARGUMENTS
```

## Instructions

1. **Parse user intent** from input:
   - If user provides git command - execute with safety checks
   - If user requests conflict help - run conflict resolver
   - If user wants commit message - run commit helper
   - If user provides branch/merge info - handle merge workflow
   - If user wants isolated workspace - create worktree workflow
   - If user wants to finish branch - branch completion workflow

2. **Invoke appropriate script**:
   ```bash
   # For git operations
   bash .github/copilot-skills/git-ops/scripts/git_safe_exec.sh \
     --backup $COMMAND

   # For commit messages
   bash .github/copilot-skills/git-ops/scripts/commit_helper.sh \
     --type $TYPE --scope $SCOPE

   # For conflict resolution
   bash .github/copilot-skills/git-ops/scripts/conflict_resolver.sh \
     --summary
   ```

3. **Handle script output**:
   - Display all terminal output directly to agent
   - Show git status and diffs as output
   - Display preview of changes with diff output
   - Show conflict details and resolution options
   - Output commit message previews before creation

4. **Safety First**:
   - Always run with --dry-run first for new operations
   - Show preview of changes before execution
   - Display confirmation prompts to user
   - Create backup branches before risky operations

## Examples

### Example 1: Safe commit
```
User: Commit changes with message about adding auth
→ Runs git_safe_exec.sh with --backup
→ Shows working tree status
→ Displays staged changes diff
→ Outputs current status and operation result
→ Shows git log after commit
```

### Example 2: Create feature branch
```
User: Create a feature branch for user profiles
→ Runs git_safe_exec.sh --backup
→ Shows branch creation
→ Displays current branch status
→ Outputs branch list
```

### Example 3: Generate commit message
```
User: Help write commit message for these changes
→ Runs commit_helper.sh
→ Analyzes staged changes
→ Outputs detected type and scope
→ Shows change statistics
→ Previews generated message in terminal
```

### Example 4: Resolve merge conflicts
```
User: Help resolve merge conflicts
→ Runs conflict_resolver.sh --summary
→ Shows conflicted files in terminal
→ Displays conflict details
→ Outputs options for resolution
→ Shows status after resolution
```

### Example 5: Safe force push
```
User: Force push feature branch
→ Runs git_safe_exec.sh --force --dry-run
→ Shows commits to be pushed
→ Displays warning about force push
→ Outputs preview of changes
→ Requires confirmation before proceeding
```

## Script Behavior

### git_safe_exec.sh
1. Checks repository state
2. Verifies working tree cleanliness
3. Creates backup branch if --backup flag set
   - Show preview of operation (diff, status output)
5. Requires confirmation before executing
6. Executes git command
7. Displays result and status

### commit_helper.sh
1. Analyzes staged changes
2. Infers commit type from file changes
3. Allows user input for type, scope, description
4. Generates conventional commit message
5. Displays preview in terminal
6. Optionally creates commit

### conflict_resolver.sh
1. Detects merge/rebase in progress
2. Lists all conflicted files
3. Shows conflict details for each file
4. Offers interactive resolution options
5. Validates conflict markers removed
6. Displays resolution status

## Terminal Output Format

Output includes:
```
ℹ Git Safe Execution Wrapper

⚠ Working tree has uncommitted changes:
 M src/auth.ts
 A tests/auth.test.ts

ℹ Preview of operation: git commit -m "feat: Add auth"

[Shows current status, diff, or command output as appropriate]

✓ Operation completed successfully
ℹ Current status:
## main
 A tests/auth.test.ts
```

## Success Output

When successful, display all:
- ✓ Confirmation of operation
- Current git status (branch, files)
- Relevant diff output
- Updated branch list if applicable
- Current repository status
- Command output and results

## Error Handling

If operation fails:
- Show specific git error message
- Display error with context
- Suggest recovery steps
- Show git status if applicable
- Offer backup recovery options

## Safety Rules

- **Never delete branches** without explicit user confirmation
- **Never force push** unless user explicitly requests
- **Always create backups** before history-modifying operations
- **Always preview** changes before execution
- **Create backups** before critical operations via script flags
- **Use safe alternatives** (revert not hard reset, force-with-lease not force)

## Options

### git_safe_exec.sh
- `--dry-run` - Preview changes without executing
- `--backup` - Create backup branch before operation
- `--no-confirm` - Skip confirmation prompt
- `--force` - Override safety checks (DANGEROUS)
- `--log FILE` - Custom log file path

### commit_helper.sh
- `--type TYPE` - Specify commit type (feat, fix, docs, etc.)
- `--scope SCOPE` - Specify scope
- `--breaking` - Mark as breaking change
- `--issue NUMBER` - Reference issue number
- `--auto-commit` - Automatically create commit

### conflict_resolver.sh
- `--summary` - Show conflict summary and exit
- `--strategy STRAT` - Auto-apply strategy (ours/theirs)
- `--validate` - Validate conflicts are resolved

## Output Data Available

Agent can read directly from terminal:
- Git status and branch information
- File diffs and staged changes
- Commit history and logs
- Branch lists and remote info
- Conflict details and resolution options
- Safety warnings and confirmations
- Generated commit messages
- Backup branch information

## Common Workflows

### Create Isolated Worktree
```bash
# 1. Check existing worktree directories
ls -d .worktrees 2>/dev/null || ls -d worktrees 2>/dev/null

# 2. Verify .gitignore (for project-local)
grep -q "^\.worktrees/$" .gitignore || echo ".worktrees/" >> .gitignore

# 3. Create worktree with new branch
git worktree add .worktrees/feature-name -b feature/feature-name

# 4. Navigate and setup
cd .worktrees/feature-name
npm install  # or cargo build, pip install, etc.

# 5. Verify clean test baseline
npm test
```

### Feature Development
```bash
bash scripts/git_safe_exec.sh --backup checkout -b feature/user-auth
bash scripts/commit_helper.sh --type feat --scope auth
bash scripts/git_safe_exec.sh --backup push -u origin feature/user-auth
```

### Finish Development Branch
```bash
# 1. Verify tests pass
npm test  # or appropriate test command

# 2. Present 4 options to user:
#    1. Merge locally
#    2. Create PR
#    3. Keep as-is
#    4. Discard

# 3a. If Option 1 (Merge locally):
git checkout main
git pull
git merge feature/feature-name
npm test
git branch -d feature/feature-name
git worktree remove .worktrees/feature-name  # if using worktree

# 3b. If Option 2 (Create PR):
git push -u origin feature/feature-name
gh pr create --title "feat: Description" --body "Summary"

# 3c. If Option 3 (Keep as-is):
# No action - keep branch and worktree

# 3d. If Option 4 (Discard):
# Confirm first, then:
git checkout main
git branch -D feature/feature-name
git worktree remove .worktrees/feature-name  # if using worktree
```

### Safe Rebase
```bash
bash scripts/git_safe_exec.sh --backup rebase main
# Handle conflicts if needed with conflict_resolver.sh
bash scripts/git_safe_exec.sh --backup push --force-with-lease
```

### Merge with Conflict Resolution
```bash
bash scripts/git_safe_exec.sh --backup merge feature/branch
bash scripts/conflict_resolver.sh --summary
bash scripts/git_safe_exec.sh commit -m "Merge: Resolve conflicts"
```

## Notes


- All output displayed to terminal for agent to read
- No file reports or logs generated
- All confirmations interactive
- Safe alternatives always preferred over dangerous operations

```
