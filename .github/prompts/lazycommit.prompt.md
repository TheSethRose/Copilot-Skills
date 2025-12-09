---
name: lazycommit
description: AI-powered commit creation that mimics lazycommit behavior. Automatically stages changes, analyzes diffs, summarizes context, and generates high-quality conventional commits. Activates when user says "commit", "auto commit", "generate commit message", etc.
---

# Lazycommit Skill

**AI-powered commit message generation that analyzes staged changes and creates conventional commits automatically.**

## When to Activate

Use this skill when the user:
- Asks to commit ("commit this", "commit and push", "make a commit")
- Wants automated commit messages ("generate commit", "write commit message")
- Requests lazy commit ("lazy commit", "auto commit", "stage and commit")
- Has made changes ready to commit

## What It Does

### 1. Detect Changes
- Check git status for staged changes
- If nothing staged: stage all changes with `git add .`
- Identify changed files
- Capture full diff for analysis

### 2. Build Context
- Summarize file changes (names, count)
- Include diff numstat (additions/deletions per file)
- Full diff for context (truncated if very large)
- Language/file type hints for better analysis

### 3. Generate Commit Message
- Use lazycommit-style prompt with staged diff
- Generate concise conventional commit message
- Output: single-line, imperative mood, no explanations
- Example: `feat(auth): add password reset flow`

### 4. Get User Confirmation
- Show generated message to user
- Options: Accept / Edit / Regenerate
- Let user refine if needed

### 5. Execute Commit
- Commit with user-approved message
- Show commit output
- Optionally offer to push

## Workflow

### Step 1: Stage Changes
```bash
# Check current status
git status --short

# Stage everything if needed
git add .

# Get staged files
git diff --cached --name-only
```

### Step 2: Build Diff Summary
```bash
# Numstat (files with +/- counts)
git diff --cached --numstat

# Full diff for analysis
git diff --cached
```

### Step 3: Generate and Commit
Construct prompt with diff context and ask Claude to generate a conventional commit message, then immediately commit with that message:
```
Based on the following git diff, generate a concise commit message.
The message must follow Conventional Commits format.
Do NOT add explanations, headers, or markdown. Only output the commit message.

<staged diff here>
```

### Step 4: Execute Commit
- Commit with generated message automatically
- Show commit output
- Display the committed message

## Example Interactions

### Simple Commit
```
User: "Commit this"

Skill:
  ✓ Checking staged changes...
  ✓ 3 files changed: src/auth/login.ts, src/auth/session.ts, types.ts
  ✓ Building diff summary...
  ✓ Generating commit message...
  ✓ Committing...

  ✓ Committed as: feat(auth): improve login validation
```

### Auto Commit With Stage
```
User: "Auto commit everything"

Skill:
  ✓ No staged changes. Staging all...
  ✓ 5 files staged
  ✓ Analyzing changes...
  ✓ Generating commit message...
  ✓ Committing...

  ✓ Committed as: feat(dashboard): add analytics widgets and charts
```



## Commit Message Quality

### Conventional Commit Format
```
<type>(<scope>): <subject>

<body (optional)>

<footer (optional)>
```

### Types
- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation
- **style**: Formatting, no logic changes
- **refactor**: Code restructuring
- **perf**: Performance improvements
- **test**: Test additions/changes
- **chore**: Dependencies, config, tooling

### Guidelines
- Subject: imperative mood ("add", not "added")
- Subject: lowercase start (except names)
- Subject: no period at end
- Subject: <50 characters ideal, <90 max
- Keep scope short and specific
- Body: wrap at 72 characters (if used)

### Examples
```
feat(auth): add two-factor authentication
fix(db): handle connection timeouts gracefully
chore(deps): upgrade typescript to 5.4
docs(readme): add installation instructions
refactor(api): extract validation logic
perf(cache): implement redis caching layer
test(auth): add login endpoint tests
style(button): fix spacing and alignment
```

## Rules & Safety

✅ **Use conventional commit format consistently**
✅ **Keep scope short and specific (<20 chars)**
✅ **Analyze diff to understand context**
✅ **Commit automatically after generating message**
✅ **Display the committed message after commit completes**

❌ **Don't modify files automatically**
❌ **Don't break conventional commits format**
❌ **Don't use past tense ("added" instead of "add")**
❌ **Don't add explanations in message (that's what commit body is for)**
❌ **Don't use generic messages ("update", "fix bugs", "changes")**

## Integration

Works well with:
- **git-ops**: Handles commits; git-ops handles branch management
- **code-review**: Commits feedback implementation
- **feature-planning**: Commits planned features after development

## Success Criteria

- ✅ All staged changes analyzed
- ✅ Conventional commit message generated
- ✅ Message committed automatically
- ✅ Commit output displayed to user
- ✅ Output follows lazycommit format exactly

---

**Ready to commit?** Just ask: "Commit this" and the skill handles the rest!
