---
description: Review codebase and clean up unnecessary files before committing
---

# Cleanup Codebase

This command reviews the current codebase and removes unnecessary files to prepare for a clean commit.

## User Input

```text
$ARGUMENTS
```

## Instructions

### 1. Identify Files to Review

Scan for common unnecessary files and patterns:

**Temporary files**:
- `*.tmp`, `*.temp`, `*.bak`, `*.backup`
- `*~`, `.*.swp`, `.*.swo`
- Files ending in `-e`, `-backup`, `-old`

**Duplicate files**:
- Files with similar names (e.g., `file.md` and `file-copy.md`)
- Multiple versions (e.g., `v1/`, `v2/`, `old/`)
- Backup copies in same directory

**Empty directories**:
- Directories with no files (except `.gitkeep`)
- Scaffold directories never populated

**Development artifacts**:
- `node_modules/` (should be in .gitignore)
- `__pycache__/`, `*.pyc` (should be in .gitignore)
- `.DS_Store` files
- Editor temp files (`.vscode/`, `.idea/` if not shared)

**Uncommitted changes**:
- Files staged but not committed
- Untracked files that should be ignored

**Documentation files**:
- Documentation in root directory (should be in `/docs/`)
- Duplicate documentation files
- Obsolete documentation (old reports, summaries)
- Files ending in `_REPORT.md`, `_SUMMARY.md`, `_NOTES.md`

### 2. Review Each Category

For each file found, determine:

1. **Is it tracked by git?**
   ```bash
   git ls-files --error-unmatch <file> 2>/dev/null
   ```

2. **Is it in .gitignore?**
   ```bash
   git check-ignore <file>
   ```

3. **Should it be kept?**
   - Required for build/run
   - Part of project documentation
   - Referenced by other files
   - Contains unique content

### 3. Create Cleanup Plan

Generate a table:

| File | Status | Reason | Action |
|------|--------|--------|--------|
| `temp.log` | Untracked | Temporary log file | DELETE |
| `old-notes.md` | Tracked | Obsolete notes | DELETE + git rm |
| `.DS_Store` | Untracked | macOS artifact | DELETE + add to .gitignore |
| `node_modules/` | Untracked | Should be ignored | DELETE + verify in .gitignore |

### 4. Get User Confirmation

**Present the plan**:
```
Found 12 files to clean up:
- 5 temporary files
- 3 duplicate files
- 2 empty directories
- 2 files that should be .gitignored

Review the plan above. Proceed with cleanup? (yes/no/review)
```

**Wait for response**:
- `yes` or `proceed` → Execute cleanup
- `no` or `stop` → Abort, no changes
- `review` → Show detailed list, ask again

### 5. Execute Cleanup

For each file to delete:

**If untracked**:
```bash
rm <file>
```

**If tracked by git**:
```bash
git rm <file>
git commit -m "chore: Remove obsolete file <file>"
```

**If should be .gitignored**:
1. Delete the file
2. Add pattern to .gitignore
3. Stage .gitignore

### 6. Organize Documentation

Check for documentation files in root directory:

**Scan for documentation patterns**:
```bash
find . -maxdepth 1 -type f -name "*README*" -o -name "*REPORT*" -o -name "*SUMMARY*" -o -name "*NOTES*" -o -name "*GUIDE*"
```

**Organization rules**:
- Project root: Keep only `readme.md` (or `README.md`)
- Feature specs: Keep in `specs/{feature-id}/` directories
- General docs: Move to `/docs/`
- Examples: Keep in `/examples/`

**Files to move to `/docs/`**:
- Implementation reports/summaries
- Guides and tutorials
- Architecture documentation (unless in specs/)
- Historical documentation

**Ask before moving**:
- Show which files will be moved
- Preview destination paths
- Confirm no broken links

### 7. Verify .gitignore Coverage

**Analyze codebase technology stack**:
1. Check for `package.json` → Node.js patterns needed
2. Check for `*.py` files → Python patterns needed
3. Check for `.venv/`, `venv/` → Virtual environment present
4. Check for `.github/` → GitHub-specific patterns
5. Check for `tests/` → Test artifact patterns

**Required patterns by detected technology**:

**Python** (if .py files exist):
```
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
.venv/
venv/
ENV/
env/
*.egg-info/
.pytest_cache/
.coverage
htmlcov/
dist/
build/
```

**Bash/Shell** (if .sh files exist):
```
*.swp
*.swo
*~
```

**Node.js** (if package.json exists):
```
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
.npm
dist/
build/
```

**Universal patterns** (always needed):
```
.DS_Store
.DS_Store?
._*
Thumbs.db
*.tmp
*.bak
*.log
.vscode/
.idea/
```

**Verify and update**:
1. Read current .gitignore
2. Compare with required patterns
3. Add missing critical patterns
4. Remove redundant patterns
5. Organize by category with comments

### 8. Report Results

**Summary**:
```
✅ Cleanup complete

Removed:
- 5 temporary files
- 3 duplicate files
- 2 empty directories

Organized:
- 4 documentation files moved to /docs/

Updated:
- .gitignore (added 8 patterns, organized by category)

Next steps:
- Review changes: git status
- Check moved files: git diff --cached
- Commit cleanup: git commit -m "chore: Clean up repository and organize documentation"
```

## Safety Rules

**Never delete without confirmation**:
- Always show the plan first
- Wait for user approval
- Provide undo instructions

**Never delete**:
- Files in git history (use git rm only)
- Files with unique content
- Configuration files
- Documentation files
- Test fixtures (unless confirmed obsolete)

**Always check**:
- File references in other files
- Import statements
- Links in documentation
- Script dependencies

**For documentation organization**:
- Scan all .md files for links to files being moved
- Update relative paths after moving
- Check for broken links after move
- Verify images/assets still resolve

## Documentation Organization Rules

### Files to Keep in Root
- `readme.md` or `README.md` - Main project README
- `LICENSE`, `CONTRIBUTING.md` - Standard project files
- `.github/` specific files (workflows, prompts)

### Files to Move to `/docs/`
- `*_REPORT.md`, `*_SUMMARY.md`, `*_NOTES.md`
- Implementation guides
- Architecture documentation (unless in `specs/`)
- Tutorials and how-to guides
- Historical documentation

### Files to Keep in `/specs/{id}/`
- Feature specifications (`spec.md`, `plan.md`, `tasks.md`)
- Research documents (`research.md`, `data-model.md`)
- Feature-specific documentation
- Implementation reports for that feature

### Link Update Strategy
After moving files:
1. Find all references: `grep -r "old-path" .`
2. Update relative paths
3. Test links work
4. Commit with descriptive message

## .gitignore Validation Strategy

### Detection Process
1. **Scan for technology markers**:
   - `.py` files → Python
   - `.sh` files → Bash
   - `package.json` → Node.js
   - `Cargo.toml` → Rust
   - `.go` files → Go

2. **Check for frameworks**:
   - `.github/` → GitHub Actions
   - `tests/` → Testing framework
   - `docs/` → Documentation

3. **Look for tool configs**:
   - `.eslintrc*` → ESLint
   - `.prettierrc*` → Prettier
   - `pytest.ini` → Pytest

### Pattern Organization
Organize .gitignore with clear sections:
```
# Python
__pycache__/
*.pyc

# Bash/Shell  
*.swp
*~

# Node.js
node_modules/

# OS Files
.DS_Store
Thumbs.db

# Editor
.vscode/
.idea/

# Project Specific
/drafts/
*.tmp
```

## Example Usage

### Scenario 1: Before feature branch merge
```
User: /cleanup
→ Scans for temporary files
→ Finds: temp.log, notes-backup.md, .DS_Store
→ Shows plan
→ User approves
→ Removes files
→ Updates .gitignore
```

### Scenario 2: After refactoring
```
User: /cleanup
→ Scans for old files
→ Finds: old-implementation/, backup/
→ Shows plan with file contents preview
→ User reviews and approves
→ Removes directories
→ Reports success
```

### Scenario 3: Repository initialization
```
User: /cleanup
→ Scans repository
→ Finds: node_modules/, __pycache__/
→ These should be .gitignored
→ Removes directories
→ Verifies .gitignore coverage
→ Suggests additional patterns
```

### Scenario 4: Documentation organization
```
User: /cleanup
→ Scans for documentation files
→ Finds: IMPLEMENTATION_REPORT.md, SETUP_GUIDE.md in root
→ Should be in /docs/
→ Shows move plan with link verification
→ User approves
→ Moves to /docs/
→ Updates any broken links
```

### Scenario 5: .gitignore validation
```
User: /cleanup
→ Detects Python (.py files) and Bash (.sh files)
→ Checks .gitignore coverage
→ Missing: __pycache__/, *.pyc, *.swp
→ Adds missing patterns
→ Organizes .gitignore with category comments
```

## Output Format

**Initial Scan**:
```
🔍 Scanning codebase...

Found 12 items to review:
  📄 Temporary files: 5
  📋 Duplicate files: 3
  📁 Empty directories: 2
  🚫 Should be .gitignored: 2

Generating cleanup plan...
```

**Cleanup Plan**:
```
| File | Status | Reason | Action |
|------|--------|--------|--------|
| temp.log | Untracked | Temporary log | DELETE |
| old.md | Tracked | Obsolete | git rm + commit |
```

**After Execution**:
```
✅ Cleanup complete

Removed 12 items:
  - 5 temporary files
  - 3 duplicate files  
  - 2 empty directories
  - 2 ignored artifacts

Organized documentation:
  - 4 files moved to /docs/
  - 0 broken links detected

Updated .gitignore:
  - Added 8 patterns (Python, Bash, Universal)
  - Organized by category
  - Removed 2 redundant patterns

Repository is clean and ready for commit! 🎉
```

## Integration

This command works well before:
- Committing feature branches
- Creating pull requests
- Merging to main
- Releasing versions
- Archiving projects

Use in combination with:
- `git status` - Check what's changed
- `git diff` - Review changes
- `/speckit.implement` - Before completion
