# Lazycommit Skill

AI-powered commit message generation that analyzes staged changes and creates conventional commits automatically. Mimics lazycommit behavior exactly.

## Files

- **`.github/prompts/lazycommit.prompt.md`** - Main skill definition with workflows and examples
- **`.github/instructions/lazycommit.instructions.md`** - Auto-loaded context and best practices
- **`reference.md`** - Detailed reference for commit message generation algorithm
- **`patterns.md`** - Common commit patterns and examples
- **`scripts/` (optional)** - Helper scripts for diff analysis and message generation

## Quick Start

### Activate the Skill
```bash
# User says any of:
"Commit this"
"Auto commit"
"Generate commit message"
"Make a commit"
"Stage and commit"
```

### What Happens
1. Detects staged changes (or stages all if needed)
2. Analyzes diff for context
3. Generates conventional commit message
4. Shows message to user
5. After approval: commits

### Example Flow
```
User: "Commit this"

Skill:
  ✓ Analyzing staged changes...
  ✓ 3 files changed
  ✓ Building diff summary...
  ✓ Generating commit message...

Generated:
  feat(auth): improve login validation

Accept? (y/n)

User: y
  ✓ Committed successfully
```

## File Organization

```
.github/
├── prompts/
│   └── lazycommit.prompt.md          # Main skill definition
├── instructions/
│   └── lazycommit.instructions.md    # Auto-loaded context
└── copilot-skills/lazycommit/
    ├── README.md                      # This file
    ├── reference.md                   # Algorithm details
    ├── patterns.md                    # Commit examples
    └── scripts/ (optional)
        └── analyze-diff.sh            # Diff analysis helper
```

## Constitutional Principles

✅ **Progressive Disclosure**
- Prompt file: main workflow in <3 minutes
- Reference.md: detailed algorithm (optional)
- Patterns.md: examples and templates (optional)

✅ **File-Based Organization**
- Prompt: `.github/prompts/lazycommit.prompt.md`
- Instructions: `.github/instructions/lazycommit.instructions.md`
- Skill directory: `.github/copilot-skills/lazycommit/`

✅ **Dynamic Discovery**
- Keywords: "commit", "auto commit", "generate commit", etc.
- Auto-loaded instructions via applyTo pattern
- Entry in copilot-instructions.md keyword map

✅ **Deterministic Execution**
- Scripts output to terminal only
- Consistent, parseable output
- No file generation
- Error handling with clear messages

✅ **Composability**
- Clear scope: commit message generation only
- Works with git-ops for branch management
- No overlapping functionality
- Explicit dependencies listed

## Conventional Commit Format

```
<type>(<scope>): <subject>

<body (optional)>

<footer (optional)>
```

### Types
- **feat**: New feature
- **fix**: Bug fix  
- **docs**: Documentation
- **style**: Formatting (no logic changes)
- **refactor**: Code restructuring
- **perf**: Performance improvements
- **test**: Test additions/updates
- **chore**: Dependencies, config, tooling

### Subject Guidelines
- Imperative mood ("add", not "added")
- Lowercase start
- No period at end
- <90 characters (ideal: <50)

### Examples
```
feat(auth): add two-factor authentication
fix(db): handle connection timeouts gracefully
chore(deps): upgrade typescript to 5.4
docs(readme): add installation instructions
refactor(api): extract validation middleware
perf(cache): implement redis caching
test(auth): add login endpoint tests
```

## Workflow Steps

### 1. Detect Changes
```bash
git status --short
git add .  # if nothing staged
git diff --cached --name-only
git diff --cached
```

### 2. Build Context
- File summary with names and count
- Numstat (additions/deletions per file)
- Full diff (truncated if >10KB)
- Language hints based on file types

### 3. Generate Message
Prompt Claude with diff context, asking for single-line conventional commit message

### 4. Get Confirmation
- Show message to user
- Options: Accept / Edit / Regenerate

### 5. Execute Commit
```bash
git commit -m "feat(auth): improve login validation"
```

## Integration Points

### With git-ops
- **lazycommit**: Generates commits
- **git-ops**: Manages branches, merges, rebasing, worktrees

### With code-review
- Review feedback → implementation → lazycommit → commit with message

### With feature-planning
- Plan feature → implement → lazycommit → commit with message

## Success Criteria

- ✅ All staged changes analyzed
- ✅ Conventional commit format used
- ✅ User shown message before commit
- ✅ User can accept, edit, or regenerate
- ✅ Message committed successfully
- ✅ Behavior matches lazycommit exactly

## Key Rules

✅ **Always show message before committing**
✅ **Never commit without user confirmation**
✅ **Never modify files automatically**
✅ **Always use conventional commits format**
✅ **Keep messages concise and clear**

❌ **Never auto-commit without prompt**
❌ **Never skip user confirmation**
❌ **Never break conventional format**

## Related Documentation

- **Prompt**: `.github/prompts/lazycommit.prompt.md` - Full workflow definition
- **Instructions**: `.github/instructions/lazycommit.instructions.md` - Best practices
- **Reference**: `reference.md` - Algorithm details
- **Patterns**: `patterns.md` - Commit examples
- **Git-ops**: `.github/copilot-skills/git-ops/` - Branch management skill

## Quick Commands

When user asks to commit:

```
1. Check status:
   git status --short

2. Stage if needed:
   git add .

3. Get diff:
   git diff --cached

4. Analyze:
   Build context from file list + numstat + diff

5. Generate:
   Prompt Claude with lazycommit format

6. Confirm:
   Show message to user, get approval

7. Commit:
   git commit -m "message"
```

---

**Use this skill whenever user mentions commit, auto-commit, or commit-related tasks.**
