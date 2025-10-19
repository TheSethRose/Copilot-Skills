# Maintenance: Skill Updates & Version Management

This document describes how to maintain, update, and manage the lifecycle of skills in the Copilot Skills Architecture.

---

## Skill Lifecycle

Each skill progresses through states: DRAFT → ACTIVE → DEPRECATED → ARCHIVED

See [GOVERNANCE.md](./GOVERNANCE.md) for detailed lifecycle documentation.

---

## Updating an Active Skill

### 1. Making Changes

Update SKILL.md, detail files, and scripts as needed:

```bash
# Edit files
vim .github/copilot-skills/{skill-name}/SKILL.md
vim .github/copilot-skills/{skill-name}/scripts/script.py

# Test changes (if applicable)
python .github/copilot-skills/{skill-name}/scripts/script.py --test
```

### 2. Increment Version

In SKILL.md frontmatter:

```yaml
---
version: "1.0.0"  # Change this
created: "2025-10-18"  # Don't change
---
```

**Version Increments**:
- PATCH: Bug fixes, documentation improvements
  - `1.0.0` → `1.0.1`
- MINOR: New capabilities (backward compatible)
  - `1.0.0` → `1.1.0`
- MAJOR: Breaking changes
  - `1.0.0` → `2.0.0`

### 3. Update Last Updated Date

```yaml
---
version: "1.0.1"
created: "2025-10-18"
last_updated: "2025-10-20"
---
```

### 4. Commit and Create PR

```bash
git add .github/copilot-skills/{skill-name}/
git commit -m "chore: Update {skill-name} to v1.0.1

- Added new capability
- Fixed script bug
- Improved documentation"

git push origin feature-branch
# Create PR with title: "fix: Update {skill-name} to v1.0.1"
```

### 5. Review and Merge

Reviewers verify:
- Version increment is appropriate
- Changes don't break Constitutional Principles
- Scripts still produce deterministic output
- Links still work

---

## Deprecating a Skill

When a skill is being replaced:

### 1. Update SKILL.md

```yaml
---
name: "Old Skill Name"
description: "DEPRECATED: Use New Skill Name instead"
status: "DEPRECATED"
deprecation_date: "2025-10-18"
migration_version: "1.2.0"
migration_guidance: "See [../new-skill/SKILL.md](../new-skill/SKILL.md) for replacement"
---

# Old Skill Name (DEPRECATED)

⚠️ **This skill is deprecated as of October 18, 2025**

Please use the [New Skill Name](../new-skill/SKILL.md) instead.

## Migration Guide

If you were using [Old Skill], here's how to migrate:

1. [Step 1 of migration]
2. [Step 2 of migration]
```

### 2. Update index.md

```markdown
### Old Skill Name (DEPRECATED)

⚠️ Deprecated as of Oct 18, 2025. Please use [New Skill Name](../new-skill/SKILL.md) instead.

**Migration**: See [deprecation guide](./old-skill/SKILL.md#migration-guide)
```

### 3. Version Bump

Use MINOR or MAJOR version bump:

```yaml
version: "1.2.0"  # Deprecation is a significant change
```

### 4. Communicate

Notify users through:
- PR description
- Changelog entry
- Git commit message

### 5. Keep in Index

Leave skill in index for 2+ releases with deprecation notice. Example timeline:

```
Release v1.0: Old Skill is ACTIVE
Release v1.1: Old Skill deprecated, migration guide added
Release v1.2: Old Skill deprecated (still discoverable)
Release v1.3: Old Skill archived (moved to archive/)
```

---

## Archiving a Skill

After deprecation grace period (typically 2+ releases):

### 1. Create Archive Directory

```bash
mkdir -p .github/copilot-skills/archive
```

### 2. Move Skill

```bash
mv .github/copilot-skills/old-skill .github/copilot-skills/archive/old-skill
```

### 3. Remove from index.md

Delete the skill entry from `.github/copilot-skills/index.md`

### 4. Add Archive Reference

```markdown
## Archived Skills

Archived skills are no longer actively maintained. See `.github/copilot-skills/archive/` for historical reference.

- Old Skill Name (v1.2.0, archived 2025-12-01)
```

### 5. Commit

```bash
git add .github/copilot-skills/
git commit -m "chore: Archive old-skill skill

Reason: Deprecated in favor of new-skill
Last version: v1.2.0
Archive date: 2025-12-01"
```

---

## Rolling Back Changes

If changes need to be reverted:

### Option 1: Revert Commit

```bash
git revert <commit-hash>
git push
```

Revert creates a new commit undoing changes (safer).

### Option 2: Direct Revert to Previous Version

```bash
git checkout <previous-commit> .github/copilot-skills/{skill-name}/
git add .github/copilot-skills/{skill-name}/
git commit -m "chore: Revert {skill-name} to v1.0.0

Reason: Breaking changes in v1.0.1"
```

---

## Testing Changes Before Merge

### For Scripts

```bash
# Test new or updated script
python .github/copilot-skills/{skill-name}/scripts/script.py --test

# Test with sample data
python .github/copilot-skills/{skill-name}/scripts/script.py \
  --input "sample_value" \
  --format json
```

### For Documentation

```bash
# Check markdown is valid
# Use a markdown linter or VS Code Markdown Preview

# Check links work
# Manually click links in SKILL.md and detail files
```

---

## Performance Considerations

### Script Performance

Monitor script execution time:

```bash
# Time script execution
time python .github/copilot-skills/{skill-name}/scripts/script.py --arg "value"

# If exceeding 10 seconds, consider optimization
```

### Documentation Size

Keep SKILL.md scannable:

```bash
# Check word count
wc -w .github/copilot-skills/{skill-name}/SKILL.md

# Should be 500-1500 words (target: <1000)
```

---

## Communicating Changes

### Commit Message Template

```
{type}: {skill-name} {description}

{Detailed explanation}

Type: feat (new), fix (bug), chore (maintenance), docs (documentation)

Example:
fix: pdf-handling script error on password-protected files

- Fixed script to properly handle password-protected PDFs
- Added better error message when password is required
- Updated version to v1.0.1
- Updated documentation with examples
```

### PR Description Template

```markdown
## Skill Update: {Skill Name}

### Summary
One paragraph explaining the change.

### Changes
- Item 1
- Item 2

### Version
Old version: 1.0.0
New version: 1.0.1
Change type: fix/feature/breaking

### Testing
- [x] Scripts tested and produce consistent output
- [x] Documentation links verified
- [x] Compliance checklist passed

### Migration (if applicable)
If this is a breaking change, include migration steps for users.
```

---

## Quarterly Maintenance

### Monthly Review

1. Check all skills are still relevant
2. Fix broken links
3. Update any broken scripts
4. Address user issues

### Quarterly Review (Every 3 months)

1. Review all ACTIVE skills for quality
2. Identify skills ready for DEPRECATED
3. Plan new skills
4. Update templates based on learnings
5. Run compliance checklist on all skills

---

## Emergency Maintenance

### Critical Issues

If a skill has critical issues:

1. Create emergency branch
2. Fix issue immediately
3. Update version
4. Create PR with "URGENT" label
5. Expedite review and merge
6. Communicate issue to users

### Example: Security Fix

```bash
# Create emergency branch
git checkout -b emergency/fix-sql-injection

# Fix issue
vim .github/copilot-skills/database-migration/SKILL.md
vim .github/copilot-skills/database-migration/scripts/generate-migration.py

# Version bump (patch)
# Update version: 1.0.0 → 1.0.1

# Commit and push
git add .github/copilot-skills/database-migration/
git commit -m "URGENT fix: database-migration SQL injection vulnerability

Security issue: Scripts were vulnerable to SQL injection
Impact: All users of v1.0.0
Action: Update to v1.0.1 immediately"

git push origin emergency/fix-sql-injection

# Create PR with URGENT label and contact maintainers
```

---

## Documentation Updates

When updating documentation:

1. Update SKILL.md core capabilities if changed
2. Update detail files (forms.md, reference.md, etc.)
3. Update AUTHORING.md if new patterns discovered
4. Update GOVERNANCE.md if new processes established
5. Update this MAINTENANCE.md file as processes evolve

---

## Questions or Issues?

See [TROUBLESHOOTING.md](./TROUBLESHOOTING.md) for common issues.

---

**Last Updated**: October 18, 2025  
**Version**: 1.0.0
