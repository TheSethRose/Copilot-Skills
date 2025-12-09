---
description: "Auto-loaded context for lazycommit skill: AI-powered commit message generation with diff analysis"
applyTo: "**/{commit,lazycommit,lazy-commit}*"
---

# Lazycommit Skill - Automatic Context Instructions

**Related Prompt:** `/lazycommit`  
**Related Skill:** `.github/copilot-skills/lazycommit/`

**Triggers:** commit, auto commit, generate commit, write commit message, make a commit, stage and commit, lazy commit

## Context: AI-Powered Commit Message Generation

When working with commits or when user queries contain commit-related keywords, this context is automatically activated.

## Core Principles

### Mimic Lazycommit Behavior
- **Stage**: Detect staged changes (or stage all if nothing staged)
- **Analyze**: Build diff context with file summary and numstat
- **Generate**: Use Claude to create conventional commit message
- **Confirm**: Show message and let user approve/edit/regenerate
- **Execute**: Commit only after user approval

### Conventional Commits Format
```
<type>(<scope>): <subject>
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `chore`

Subject: imperative mood, lowercase, no period, <90 chars

### Quality Standards
- **Single-line messages** (unless user requests body)
- **Descriptive scope** (e.g., `auth`, `api`, `ui`, `deps`)
- **Clear intent** (what changed and why it matters)
- **Follows conventions** consistently

## Default Behaviors

### When user says "commit" or "auto commit"
1. Check `git status --short` for staged changes
2. If nothing staged: run `git add .`
3. Get list of changed files: `git diff --cached --name-only`
4. Generate prompt with: file list, numstat, and full diff (truncated if >10KB)
5. Ask Claude to generate conventional commit message
6. Automatically commit: `git commit -m "message"`
7. Display the committed message to user

### When user says "generate commit message"
1. Same as "commit" workflow
2. Generates and automatically commits the message

### When user says "make a commit"
1. Same as "commit"
2. Full workflow end-to-end

### When user requests "stage and commit"
1. Explicitly stage all changes
2. Generate and commit in one flow

## Quality Guidelines

### ✅ Do
- Use conventional commit format consistently
- Keep scope short and specific (<20 chars)
- Use imperative mood in subject
- Analyze diff to understand context
- Commit automatically after generating message
- Stage all changes when none are staged
- Display commit confirmation to user

### ❌ Don't
- Modify files automatically
- Break conventional commits format
- Use past tense ("added" instead of "add")
- Add explanations in message (that's what commit body is for)
- Use generic messages ("update", "fix bugs", "changes")
- Stage files user didn't intend to commit

## Commit Message Examples

### Good Messages
```
feat(auth): add password reset flow
fix(db): handle null connection gracefully
docs(readme): add installation instructions
refactor(api): extract validation middleware
chore(deps): upgrade typescript to 5.4
perf(cache): implement redis caching layer
test(auth): add login endpoint tests
```

### Bad Messages
```
update files
fix bugs
changes
updated auth
fixed the thing
misc updates
```

## Diff Analysis Pattern

When building prompt for Claude:

1. **File Summary**
   ```
   Changes:
   - src/auth/login.ts
   - src/auth/session.ts
   - types.ts
   ```

2. **Numstat** (additions/deletions)
   ```
   12	5	src/auth/login.ts
   8	3	src/auth/session.ts
   2	1	types.ts
   ```

3. **Full Diff** (if <5KB, else summary)
   ```
   diff --git a/src/auth/login.ts b/src/auth/login.ts
   ... full or partial diff ...
   ```

## Common Workflows

### Commit All Changes
```
User: "Commit this"
→ Stage all changes
→ Analyze diff
→ Generate message
→ Commit automatically
→ Display confirmation
```

### Commit and Push
```
User: "Commit and push"
→ Commit (same as above)
→ Git push (with -u for new branch)
```

## Integration with Other Skills

- **git-ops**: Lazycommit generates commits; git-ops handles branches, merges, rebasing
- **code-review**: Lazycommit commits implementation of review feedback
- **feature-planning**: Lazycommit commits planned features after development

## Success Metrics

✅ Conventional format always followed  
✅ Scope accurately reflects changed files  
✅ Subject describes change clearly  
✅ Message <90 characters (ideal <50)  
✅ Commit executed automatically  
✅ Commit confirmation displayed to user  
✅ All staged changes analyzed  

## Next Steps

When working with commits:
1. Use `/lazycommit` prompt for guided workflows
2. Check `.github/copilot-skills/lazycommit/` for scripts and utilities
3. Reference `.github/prompts/lazycommit.prompt.md` for full skill details
4. Use conventional commits consistently across team

## Related Skills

- **git-ops** - For branch management, merging, rebasing, worktrees
- **code-review** - For committing review feedback
- **feature-planning** - For planning before committing implementation
