# Troubleshooting: Common Issues with Skills Architecture

This guide helps you resolve common issues when using, creating, or maintaining Copilot Skills.

---

## Discovery Issues

### Problem: "I can't find a skill in index.md"

**Symptoms**: You're looking for a skill (e.g., "PDF handling") but it's not in `.github/copilot-skills/index.md`

**Solutions**:
1. **Check spelling**: Is the skill name exactly matching index.md? (Case-sensitive)
2. **Check status**: Is the skill ACTIVE? Deprecated/archived skills aren't listed
3. **Check path**: Does the skill directory actually exist? `ls .github/copilot-skills/`
4. **Search tags**: Use Ctrl+F in index.md to search by keywords (tags) not just skill name

**Prevention**: Keep index.md updated when adding/removing skills

---

### Problem: "Copilot doesn't recognize my skill"

**Symptoms**: You mention a task but Copilot doesn't suggest your skill

**Solutions**:
1. **Check metadata**: Is your skill's description specific? Generic descriptions like "utilities" won't match well
2. **Check tags**: Are tags relevant to the task? ("pdf", "forms", not "doc")
3. **Check that skill is ACTIVE**: Only ACTIVE skills appear in index.md
4. **Clear Copilot context**: Try asking again or rephrasing the task

**Prevention**: Use specific descriptions and tags that match common task keywords

---

## Progressive Loading Issues

### Problem: "Detail file links are broken"

**Symptoms**: Click link in SKILL.md and file doesn't open, or opens wrong file

**Solutions**:
1. **Check relative paths**: Links should use `./ ` for same directory
   - ✅ `[forms.md](./forms.md)` → correct
   - ❌ `[forms.md](../hello-skill/forms.md)` → wrong if in hello-skill
2. **Check file exists**: Does the file actually exist in that location?
   - `ls .github/copilot-skills/{skill-name}/forms.md`
3. **Check spelling**: Match the filename exactly (case-sensitive on Unix)
4. **Use absolute paths**: If relative paths don't work, use absolute paths from repo root
   - `.github/copilot-skills/{skill-name}/forms.md`

**Prevention**: Validate all links using link checker or manual verification before merging

---

### Problem: "Detail file is too long / hard to understand"

**Symptoms**: Detail file (forms.md, reference.md) is 3000+ words or confusing

**Solutions**:
1. **Break into multiple files**: If detail file covers 2+ topics, split into separate files
   - `forms.md` → Government forms only
   - `patterns.md` → General patterns
   - `reference.md` → API reference
2. **Add table of contents**: For long files, add `## Table of Contents` at top
3. **Add clear introductions**: Each detail file should start with "This file covers..."
4. **Use headings effectively**: Use H2 and H3 headings to organize content

**Prevention**: Keep detail files focused (single topic), 500-1500 words each

---

### Problem: "I can't read this detail file without reading the other one"

**Symptoms**: `forms.md` says "For API reference, see `reference.md`" - detail files aren't independent

**Solutions**:
1. **Combine files**: If files are too tightly coupled, consider combining them
2. **Duplicate necessary context**: Repeat key information in both files
3. **Move to SKILL.md**: If information is needed by both, move to core SKILL.md
4. **Rethink file division**: Maybe the topics need different organization

**Prevention**: Use detail file independence checklist (`.specify/checklists/detail-file-independence.md`)

---

## Script Execution Issues

### Problem: "Script won't run"

**Symptoms**: `python script.py` fails with "command not found" or "permission denied"

**Solutions**:
1. **Check path**: Run from project root, not script directory
   - ✅ `python .github/copilot-skills/hello-skill/scripts/hello-example.py`
   - ❌ `python hello-example.py` (wrong directory)
2. **Check Python version**: Script requires Python 3.6+
   - Check: `python --version` or `python3 --version`
3. **Check dependencies**: Script might need libraries
   - Check imports at top of script
   - Install: `pip install -r requirements.txt` (if exists)
4. **Check permissions**: Unix scripts need execute permissions
   - Fix: `chmod +x script.sh`

**Prevention**: Document Python version and dependencies in SKILL.md

---

### Problem: "Script returns an error"

**Symptoms**: Script runs but outputs error message or non-zero exit code

**Solutions**:
1. **Check arguments**: Are you passing required arguments?
   - Script: `python script.py --name "value" --format json`
   - Read SKILL.md for required arguments
2. **Check argument format**: Are values in correct format?
   - `--name` might need string: `--name "value"` not `--name value`
3. **Check for special characters**: If value contains spaces/quotes, quote it
   - ✅ `--name "Alice Cooper"`
   - ❌ `--name Alice Cooper`
4. **Check error message**: Script error should explain the issue
   - Read error carefully and fix the issue
   - Run with `--verbose` for more details (if supported)

**Prevention**: Document common errors in SKILL.md "Error Handling" section

---

### Problem: "Script produces different output each time (not deterministic)"

**Symptoms**: Running same script with same input gives different results

**Solutions**:
1. **Check for randomness**: Does script use `random()` or `shuffle()`?
   - Should use `random.seed()` for consistency
2. **Check for timestamps**: Are timestamps included? (Usually acceptable)
   - If time varies, results will vary
3. **Check for external data**: Does script fetch data from internet or files?
   - Should cache or use consistent source
4. **Check sorting**: Are results sorted consistently? (Different order = different output)
   - Ensure lists are sorted before output

**Prevention**: Document determinism in SKILL.md; test script repeatedly with same input

---

## Skill Creation Issues

### Problem: "I'm not sure if my skill follows the Constitutional Principles"

**Solutions**:
1. **Run compliance checklist**: `.specify/checklists/skill-compliance-checklist.md`
2. **Check each principle**:
   - Progressive Disclosure: Is SKILL.md readable in <3 minutes?
   - File-Based Organization: Are files organized correctly?
   - Dynamic Discovery: Does index.md have clear metadata?
   - Deterministic Execution: Do scripts give consistent results?
   - Composability: Are boundaries clear? Any circular dependencies?
3. **Compare with examples**: Review `hello-skill/` and `skill-template/`
4. **Ask for review**: Get feedback before merging

**Prevention**: Use checklist early in skill creation, not just at end

---

### Problem: "Where should I put this content?"

**Symptoms**: You have documentation but not sure whether it should go in SKILL.md, forms.md, reference.md, etc.

**Solutions**:

| Content Type | Location | Size |
|---|---|---|
| Core capabilities | SKILL.md | <1000 words |
| Quick start examples | SKILL.md | <100 words |
| 3-5 common patterns | SKILL.md | <400 words |
| Full API reference | reference.md | 500+ words |
| Form-specific patterns | forms.md | 500+ words |
| Code examples | examples.md | Multiple examples |
| Troubleshooting | troubleshooting.md | Issue descriptions |

**Rule of thumb**:
- SKILL.md = "What can I do?" (quick overview)
- Detail files = "How do I do it?" (deep dive)

**Prevention**: Use AUTHORING.md Step 3 guidance

---

## Documentation Quality Issues

### Problem: "My SKILL.md is taking too long to read"

**Symptoms**: Takes >5 minutes to read SKILL.md; too much detail

**Solutions**:
1. **Move examples to detail files**: Keep only core capabilities in SKILL.md
2. **Move API reference**: Create reference.md for full API docs
3. **Move edge cases**: Document in troubleshooting.md or detail files
4. **Use bullet points**: Replace paragraphs with short bullet list
5. **Use table of contents**: Help readers find relevant section quickly

**Prevention**: Test readability - have someone new to skill read it and time them

---

### Problem: "My links don't work when I share the skill"

**Symptoms**: Links work locally but break when sharing or in different viewer

**Solutions**:
1. **Use relative paths**: Not absolute paths
   - ✅ `./forms.md` or `../other-skill/SKILL.md`
   - ❌ `/Users/username/...` or `file:///...`
2. **No file extensions in GitHub markdown**:
   - ✅ `[Link](./forms)` (GitHub adds .md automatically)
   - ❌ `[Link](./forms.md)` (might not work)
3. **Use standard markdown**: Some viewers don't support all markdown extensions
4. **Test in GitHub**: Check links work on GitHub, not just locally

**Prevention**: Test all links before merging

---

## Metadata Issues

### Problem: "My skill metadata isn't clear"

**Symptoms**: Description is vague or tags don't help with discovery

**Solutions**:

| Issue | Bad Example | Good Example |
|---|---|---|
| Vague description | "Handle documents" | "Extract text and fill PDF forms" |
| Generic tags | `["misc", "tools"]` | `["pdf", "forms", "documents"]` |
| Name too long | "Universal Document Processing Utility" | "pdf-handling" |

**Prevention**: Test metadata with team - do they understand what skill does?

---

### Problem: "Two skills have overlapping purposes"

**Symptoms**: "PDF handling" and "document processing" seem to do similar things

**Solutions**:
1. **Define clear boundaries**: Each skill should have distinct scope
   - "PDF handling" = PDF-specific operations
   - "document processing" = Cross-format document workflows
2. **Choose one owner**: Avoid duplicate skills
3. **Cross-reference**: If skills relate, link them in detail files
4. **Combine if too similar**: Consider merging overlapping skills

**Prevention**: Check index.md for similar skills before creating new one

---

## General Questions

### "How often should I update my skill?"

**Answer**: Update when:
- Bug fixes needed (PATCH version)
- New capabilities added (MINOR version)
- Security issues found (PATCH or MAJOR)
- Documentation improvements (PATCH or no version bump)

Typically: monthly maintenance review, quarterly full review

### "What if users report issues with my script?"

**Answer**:
1. Understand the issue (ask for reproduction steps)
2. Fix in SKILL.md or script
3. Update version
4. Add to troubleshooting or error handling
5. Communicate fix to users
6. Consider preventing issue in future (better docs, validation)

### "Can I delete a skill?"

**Answer**: No, archive it instead:
1. Mark as DEPRECATED
2. Keep in index.md with deprecation notice for 2+ releases
3. Move to archive/ directory
4. Never delete - keep for historical reference

---

## Getting Help

**For creation questions**: See [AUTHORING.md](./AUTHORING.md)  
**For governance questions**: See [GOVERNANCE.md](./GOVERNANCE.md)  
**For architecture questions**: See [README.md](./README.md)  
**For maintenance questions**: See [MAINTENANCE.md](./MAINTENANCE.md)

---

**Last Updated**: October 18, 2025  
**Version**: 1.0.0
