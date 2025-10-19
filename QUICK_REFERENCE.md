# Quick Reference: Copilot Skills Architecture

**TL;DR** - Fast answers to common questions

---

## ⚡ Quick Start (30 seconds)

**Q: How do I find a skill?**  
A: Open `.github/copilot-skills/index.md`, search for your task, click the path to SKILL.md

**Q: How do I create a skill?**  
A: Read `.github/copilot-skills/AUTHORING.md` and copy `.specify/templates/SKILL.md`

**Q: How do I run a script?**  
A: `python .github/copilot-skills/{skill}/scripts/{script}.py --arg "value"`

---

## 🎯 Navigation

### Finding Things

| Need | Go To |
|------|-------|
| Skill names & descriptions | `.github/copilot-skills/index.md` |
| How to create a skill | `.github/copilot-skills/AUTHORING.md` |
| How to review a skill | `.github/copilot-skills/GOVERNANCE.md` |
| How to update a skill | `.github/copilot-skills/MAINTENANCE.md` |
| Troubleshooting | `.github/copilot-skills/TROUBLESHOOTING.md` |
| Examples & workflows | `.github/copilot-skills/EXAMPLES.md` |
| Architecture deep dive | `.github/copilot-skills/README.md` |

### Templates

| Need | Use |
|------|-----|
| Create a new skill | Copy `.specify/templates/SKILL.md` |
| Write a Python script | Copy `.specify/templates/script-template.py` |
| Write a Shell script | Copy `.specify/templates/script-template.sh` |

### Checklists

| Task | Use |
|------|-----|
| Validate new skill | `.specify/checklists/skill-compliance-checklist.md` |
| Validate detail files | `.specify/checklists/detail-file-independence.md` |

---

## 📋 Common Tasks (2-5 minutes each)

### Task 1: I need to find a skill for PDF handling

```
1. Open .github/copilot-skills/index.md
2. Search for "pdf" or "forms" (Ctrl+F)
3. Click path to SKILL.md
4. Read overview (2 min)
5. Click detail file if needed
```

### Task 2: I want to create a new skill

```
1. Read .github/copilot-skills/AUTHORING.md (10 min)
2. Copy .specify/templates/SKILL.md
3. Fill in metadata and sections
4. Create detail files
5. Run .specify/checklists/skill-compliance-checklist.md
6. Submit PR
```

### Task 3: I want to use a bundled script

```
1. Read SKILL.md "Bundled Scripts" section
2. Copy command from documentation
3. Run: python .github/copilot-skills/{skill}/scripts/{script}.py --arg "value"
4. Get deterministic result
```

### Task 4: A skill needs updating

```
1. Read .github/copilot-skills/MAINTENANCE.md
2. Make changes
3. Update version (patch/minor/major)
4. Commit with version bump message
5. Create PR for review
```

### Task 5: A skill has issues

```
1. Check .github/copilot-skills/TROUBLESHOOTING.md
2. Follow solution for your issue
3. If not resolved, open issue with details
```

---

## 📊 Architecture at a Glance

**5 Principles**:
1. **Progressive Disclosure** - Layer: metadata → SKILL.md → detail files → scripts
2. **File-Based** - Skills live in `.github/copilot-skills/{skill-name}/`
3. **Discoverable** - Index.md has metadata for all skills
4. **Deterministic** - Scripts produce same output for same input
5. **Composable** - Skills work together for complex workflows

**File Structure**:
```
.github/copilot-skills/
├── index.md                    # Registry
├── README.md / AUTHORING.md   # Guides
├── {skill-name}/
│   ├── SKILL.md               # Core
│   ├── {detail}.md            # Optional
│   └── scripts/
│       └── {script}.py|.sh    # Scripts
```

---

## ⚙️ Skill Lifecycle

| Stage | Status | Action |
|-------|--------|--------|
| Creating | DRAFT | Write skill, validate |
| Active | ACTIVE | In index.md, being used |
| Ending | DEPRECATED | Keep in index, show migration |
| Archived | ARCHIVED | Move to archive/, no longer listed |

---

## 🔗 Key Links

**For Developers Using Skills**:
- Start: `.github/copilot-skills/index.md`
- Learn: `.github/copilot-skills/EXAMPLES.md`
- Help: `.github/copilot-skills/TROUBLESHOOTING.md`

**For Skill Authors**:
- Create: `.github/copilot-skills/AUTHORING.md`
- Validate: `.specify/checklists/skill-compliance-checklist.md`
- Review: `.github/copilot-skills/GOVERNANCE.md`

**For Maintainers**:
- Manage: `.github/copilot-skills/MAINTENANCE.md`
- Govern: `.github/copilot-skills/GOVERNANCE.md`
- Deep Dive: `.github/copilot-skills/README.md`

---

## 💡 Tips & Tricks

### Tip 1: Scanning Quickly
- SKILL.md is designed to be readable in <3 minutes
- Read just the "Core Capabilities" section if short on time
- Detail files are optional

### Tip 2: Using Scripts
- Always check the SKILL.md documentation for script usage
- Scripts follow standard input → output format
- All scripts return JSON with `{"success": true/false, "data": ..., "error": ...}`

### Tip 3: Creating Skills
- Use the templates in `.specify/templates/` as starting point
- Follow the "When to Create a Skill" section in AUTHORING.md
- Run compliance checklist before submitting

### Tip 4: Getting Context
- Index.md + SKILL.md = 80% of what you need (quick answer)
- Add detail files only if you need specific information (5-15 more min)
- Total time saved vs. monolithic docs: 60%+

---

## ❌ What NOT to Do

- ❌ Don't create a skill without reading AUTHORING.md first
- ❌ Don't put everything in SKILL.md (use detail files)
- ❌ Don't skip the compliance checklist
- ❌ Don't create overlapping skills without checking index.md
- ❌ Don't delete skills (archive them instead)
- ❌ Don't modify scripts without testing determinism

---

## 🚨 Emergency Help

| Issue | Solution |
|-------|----------|
| Can't find a skill | Check index.md tags (Ctrl+F) |
| Script won't run | Check SKILL.md for usage & paths |
| Broken links | See TROUBLESHOOTING.md "Broken Links" section |
| Unclear documentation | See TROUBLESHOOTING.md "Documentation Quality" |
| Questions | Check EXAMPLES.md for workflows first |

---

## 📞 Support

- **Questions about skills**: Check `.github/copilot-skills/README.md`
- **Creating skills**: Check `.github/copilot-skills/AUTHORING.md`
- **Broken things**: Check `.github/copilot-skills/TROUBLESHOOTING.md`
- **Architecture decisions**: Check `/IMPLEMENTATION_SUMMARY.md`

---

**Last Updated**: October 18, 2025  
**Version**: 1.0.0

**Total time to master**: 30 min (this guide) + 30 min (one example skill)
