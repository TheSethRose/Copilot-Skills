# Lazycommit Algorithm Reference

Detailed breakdown of how lazycommit analyzes diffs and generates commit messages.

## Phase 1: Detect Changes

### Input
User says: "commit", "auto commit", "generate commit", etc.

### Process
```bash
# Step 1: Check what's staged
git status --short

# Step 2: If nothing staged, stage everything
if [ nothing staged ]; then
  git add .
fi

# Step 3: Get list of changed files
git diff --cached --name-only

# Step 4: Get statistics per file
git diff --cached --numstat

# Step 5: Get full diff for analysis
git diff --cached
```

### Output
- List of changed files
- Count of files changed
- Additions/deletions per file
- Complete unified diff

## Phase 2: Build Diff Context

### Input
- File list
- Numstat data
- Full diff

### Process

#### 2a. Analyze File Types
```
For each changed file:
  - Extract file extension
  - Determine language (TypeScript, Python, Shell, etc.)
  - Note if config file (.env, .json, package.json, etc.)
  - Note if test file (*test.ts, *spec.ts, etc.)
```

#### 2b. Summarize Changes
```
Count by type:
  - Feature files: src/features/*.ts
  - Test files: **/*.test.ts
  - Config files: config/*.json
  - Documentation: *.md
  - Dependencies: package.json, requirements.txt, etc.
```

#### 2c. Calculate Scope
```
Primary scope = most changed directory
  - If 3+ files in src/auth/ → scope is "auth"
  - If 2+ files in src/api/ → scope is "api"
  - If config files → scope is "config"
  - If deps file → scope is "deps"

Multi-scope? Use most significant
  Precedence: auth > api > ui > db > config > chore
```

#### 2d. Determine Type
```
Look for patterns:
  - New files + additions → feat
  - Deletions in code → fix or refactor
  - Test files only → test
  - Deps updated → chore
  - Docs only → docs
  - .prettier, .eslint, config → style or chore
  
Heuristic: More lines added than removed → likely "feat" or "fix"
```

### Output
- Scope (e.g., "auth", "api", "deps")
- Type (feat, fix, test, chore, docs, etc.)
- File summary
- Change magnitude (small, medium, large)

## Phase 3: Generate AI Prompt

### Input
- File list and summary
- Numstat
- Full diff (or truncated if >10KB)
- Analysis from Phase 2

### Prompt Template
```
Based on the following git diff, generate a concise commit message.
The message MUST follow the Conventional Commits format: <type>(<scope>): <subject>

Rules:
- Use imperative mood (add, not added)
- Lowercase start of subject
- No period at end of subject
- Subject under 90 characters (ideal: <50)
- Only output the commit message, no explanations

Changed files:
{file_list}

Statistics:
{numstat}

Diff:
{full_diff_or_truncated}
```

### Processing
1. Send prompt to Claude
2. Claude analyzes diff
3. Claude generates conventional commit message
4. Extract message (single line)
5. Validate format

## Phase 4: Validate Generated Message

### Checks
```
✓ Starts with valid type (feat, fix, docs, etc.)
✓ Has scope in parentheses
✓ Has colon after scope
✓ Subject starts with lowercase or verb
✓ No period at end
✓ Single line (no body)
✓ Length <90 characters
```

### If Invalid
Regenerate with stricter prompt or retry

### Output
Clean, validated commit message

## Phase 5: User Confirmation

### Display
```
Generated commit message:
  feat(auth): add password reset flow

Accept? (y/n) / Edit (e) / Regenerate (r)
```

### Branches
- **Accept (y)**: Proceed to commit
- **Edit (e)**: Ask user for new message
- **Regenerate (r)**: Go back to Phase 3

## Phase 6: Execute Commit

### Input
- Approved commit message

### Process
```bash
git commit -m "feat(auth): add password reset flow"
```

### Output
```
✓ Committed as: feat(auth): add password reset flow

Next: Push? (y/n)
```

## Key Heuristics

### Scope Selection Priority
1. **Package**: If package.json changed → "deps" or "build"
2. **Directory**: If 3+ files in same dir → that dir name
3. **Feature**: If feat files → feature name
4. **Test**: If all test files → "test"
5. **Config**: If config files → "config"

### Type Detection
```
More additions than deletions?
  └─ New tests? → test
  └─ New feature? → feat
  └─ Dep update? → chore
  └─ Doc? → docs
  └─ Other? → feat (default)

More deletions than additions?
  └─ Bug fix? → fix
  └─ Refactor? → refactor
  └─ Cleanup? → chore

Equal or mixed?
  └─ Has bug fix markers? → fix
  └─ Performance improvement? → perf
  └─ Code style? → style
  └─ Tests? → test
  └─ Other? → refactor (default)
```

### Subject Generation
```
Pattern:
  <verb> <object> [detail]

Examples:
  add password reset flow
  fix null pointer in auth
  remove deprecated API endpoint
  improve login validation
  update TypeScript config
  refactor validation middleware
  bump React to 18.3
```

### Scope Rules
```
Keep scope <20 characters
Use single word if possible
  ✓ auth, api, ui, db, deps
  ✗ authentication, user-service

Use directory name if clear
  src/auth/ → scope: auth
  src/pages/admin/ → scope: admin

Use feature name if feature-specific
  Feature branch: feature/dark-mode → scope: dark-mode
```

## Algorithm Pseudocode

```python
def generate_commit_message(changes):
  # Phase 1: Detect
  files = get_staged_files()
  if not files:
    git.add_all()
    files = get_all_files()
  
  numstat = get_numstat(files)
  full_diff = get_full_diff()
  
  # Phase 2: Analyze
  scope = analyze_scope(files, numstat)
  type = detect_type(files, numstat, full_diff)
  file_summary = summarize_files(files)
  
  # Phase 3: Generate
  prompt = build_prompt(file_summary, numstat, full_diff)
  message = claude(prompt)
  
  # Phase 4: Validate
  validated = validate_conventional_format(message)
  if not validated:
    message = claude(prompt + " (strict format required)")
  
  # Phase 5: Confirm
  result = show_confirm_prompt(message)
  while result == "regenerate":
    message = claude(prompt + " (generate different message)")
    result = show_confirm_prompt(message)
  
  if result == "edit":
    message = get_user_input("Enter message: ")
  
  # Phase 6: Execute
  if result == "accept":
    git.commit(message)
    return success(message)
  
  return cancelled()
```

## Performance Considerations

### Diff Size Handling
- **<1KB**: Include full diff in prompt
- **1-5KB**: Include full diff
- **5-10KB**: Include full diff with truncation notice
- **>10KB**: Include summary + key sections + truncation notice

### Multi-file Changes
- Up to 10 files: List all
- 11-30 files: Group by directory
- 31+ files: Group by type + directory

### Token Efficiency
- Numstat: ~50 tokens (very efficient)
- Small diff: ~200-500 tokens
- Large diff: ~2000 tokens (truncated to ~1000)

## Common Patterns Generated

### Feature
```
feat(auth): add two-factor authentication
feat(ui): add dark mode toggle
feat(api): add rate limiting
feat(db): add caching layer
```

### Bug Fix
```
fix(auth): handle expired session tokens
fix(api): prevent null pointer exception
fix(ui): fix button alignment issue
fix(db): handle connection timeouts
```

### Chore
```
chore(deps): upgrade typescript to 5.4
chore(build): update webpack config
chore(ci): add github actions workflow
chore(docs): update readme
```

### Refactor
```
refactor(api): extract validation logic
refactor(ui): componentize form inputs
refactor(db): simplify query builder
refactor(auth): consolidate auth middleware
```

---

**This algorithm exactly mimics lazycommit behavior for maximum compatibility.**
