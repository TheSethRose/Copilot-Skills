---
description: "Auto-loaded context for cleanup operations: removing unused files, dependencies, and stale resources"
applyTo: "**/{node_modules,__pycache__,.pytest_cache,dist,build,*.pyc,*.log,*.tmp}/**"
---

# Cleanup Operations - Automatic Context Instructions

**Related Prompt:** `/cleanup`

**Triggers:** cleanup, remove, delete, unused, stale, orphan, tidy, clean up

## Context: Cleanup and Maintenance Operations

When working with files that match cleanup patterns or when user queries contain cleanup keywords, this context is automatically activated.

## Default Behaviors

### When user mentions "cleanup" or "unused"
1. Suggest `/cleanup` skill prompt for guided cleanup workflow
2. Analyze project for common cleanup targets
3. Respect `.gitignore` patterns (never delete ignored files without confirmation)
4. Create safety checkpoints before destructive operations

### When user mentions "dependencies" or "node_modules"
1. Check for unused dependencies in package.json, requirements.txt, etc.
2. Suggest removal of unused packages
3. Warn about breaking changes before removal
4. Update lockfiles after changes

### When user mentions "cache" or "build artifacts"
1. Identify safe-to-delete cache directories
2. Preserve development environment configurations
3. Keep `.gitignore` patterns up to date

## Quality Guidelines

### ✅ Do
- Always ask for confirmation before deleting files
- Show what will be deleted before executing
- Use dry-run flags when available
- Backup important files before cleanup
- Update `.gitignore` after cleanup
- Clean incrementally (one type at a time)

### ❌ Don't
- Delete files matching `.gitignore` without explicit confirmation
- Remove dependencies without checking usage
- Clean production builds without backup
- Delete configuration files
- Remove version control history
- Clean without showing file list first

## Common Cleanup Targets

### Safe to Remove (Usually)
```bash
# Build artifacts
dist/
build/
*.egg-info/
target/

# Cache directories
__pycache__/
.pytest_cache/
.mypy_cache/
.ruff_cache/
node_modules/.cache/
.next/
.nuxt/

# Log files
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Temporary files
*.tmp
*.temp
.DS_Store
Thumbs.db
```

### Verify Before Removing
```bash
# Dependencies (check usage first)
node_modules/
venv/
.venv/

# Generated files (may be needed)
package-lock.json (if using yarn)
yarn.lock (if using npm)
```

### Never Remove Without Explicit Request
```bash
# Source code
src/
lib/

# Configuration
.env
.env.local
config/

# Version control
.git/
.gitignore

# Documentation
README.md
docs/
```

## Cleanup Commands

### Node.js Projects
```bash
# Remove node_modules
rm -rf node_modules/

# Clear npm cache
npm cache clean --force

# Remove build artifacts
rm -rf dist/ build/ .next/

# Reinstall dependencies
npm install
```

### Python Projects
```bash
# Remove Python cache
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -type f -name "*.pyc" -delete

# Remove build artifacts
rm -rf dist/ build/ *.egg-info/

# Clear pip cache
pip cache purge
```

### General Cleanup
```bash
# Remove log files
find . -type f -name "*.log" -delete

# Remove temporary files
find . -type f -name "*.tmp" -delete
find . -type f -name "*.temp" -delete

# Remove OS-specific files
find . -name ".DS_Store" -delete
find . -name "Thumbs.db" -delete
```

## Dependency Analysis

### Check for Unused Dependencies

**Node.js:**
```bash
# Using depcheck
npx depcheck

# Using npm-check
npx npm-check
```

**Python:**
```bash
# Using pip-autoremove
pip install pip-autoremove
pip-autoremove <package-name> --list

# Manual check
pip list --not-required
```

## Safety Checklist

Before running cleanup operations:

- [ ] Check git status (`git status`)
- [ ] Ensure working directory is clean or changes are committed
- [ ] Review files to be deleted
- [ ] Verify no important files in cleanup path
- [ ] Backup critical configuration if needed
- [ ] Test in development environment first
- [ ] Have rollback plan ready

## Next Steps

When performing cleanup:
1. Use `/cleanup` prompt for guided workflow
2. Review all deletions before executing
3. Commit `.gitignore` updates after cleanup
4. Test application after cleanup
5. Update documentation if project structure changes

## Related Skills

- **Git operations** - For committing cleanup changes
- **Dependency management** - For updating package files
- **Project maintenance** - For ongoing cleanup strategies
