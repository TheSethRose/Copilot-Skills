# Detail File Independence Checklist

**Purpose**: Validate that detail files in skills can be read independently without reading other detail files

**Reference**: Constitutional Principle I: Progressive Disclosure - Each file must be independently useful.

---

## Skill: [Skill Name]

- Reviewer: ________________  
- Date: ________________

---

## Detail Files to Validate

List all detail files in this skill:

- [ ] File: ________________________ (e.g., reference.md, forms.md, patterns.md)
- [ ] File: ________________________
- [ ] File: ________________________

---

## Independence Validation

For **EACH detail file**, verify the following:

### File 1: [Filename]

#### 1. Standalone Readability
- [ ] **Document provides sufficient context** - Reader understands the topic without reading other files
- [ ] **No references to "previous sections" in other files** - All context is self-contained
- [ ] **Introductory paragraphs explain the topic clearly** - No assumptions about reader's prior knowledge
- [ ] **All technical terms are defined or linked** - Or are universally understood

#### 2. Complete Information
- [ ] **Reader gets actionable guidance** - Not just pointers to other files
- [ ] **Examples are self-contained** - Example code doesn't depend on examples in other files
- [ ] **Process steps are complete** - Not "see part 1 for details"
- [ ] **Troubleshooting is specific to this topic** - Not "see error handling in reference.md"

#### 3. No Circular References
- [ ] **Doesn't say "See patterns.md for patterns"** - That would be circular
- [ ] **Doesn't say "For details, see reference.md"** - That's referencing, not independent use
- [ ] **Cross-references are enrichment, not requirements** - Reader gains value even without following links

#### 4. Structure Consistency
- [ ] **Follows standard section structure** - Introduction, content sections, conclusion
- [ ] **Uses appropriate heading levels** - H1 for title, H2 for sections, H3 for subsections
- [ ] **Markdown formatting is consistent** - Bold, code blocks, lists used appropriately
- [ ] **Length is appropriate** - 500+ words for substantial topics, sufficient to be useful

#### 5. Links and References
- [ ] **Links are explanatory, not required** - "See X for more details" not "Follow this link to understand"
- [ ] **All links use relative paths** - `.` paths within same directory
- [ ] **Links are labeled descriptively** - Not just `[see more]`
- [ ] **Links actually exist** - Validate by following them

**Status**: ☐ PASS ☐ FAIL ☐ NEEDS REVISION

**Issues**: (list any problems found)

---

### File 2: [Filename]

#### 1. Standalone Readability
- [ ] **Document provides sufficient context**
- [ ] **No references to "previous sections" in other files**
- [ ] **Introductory paragraphs explain the topic clearly**
- [ ] **All technical terms are defined or linked**

#### 2. Complete Information
- [ ] **Reader gets actionable guidance**
- [ ] **Examples are self-contained**
- [ ] **Process steps are complete**
- [ ] **Troubleshooting is specific to this topic**

#### 3. No Circular References
- [ ] **Doesn't say "See [other file] for [its topic]"**
- [ ] **Doesn't require reading other files first**
- [ ] **Cross-references are enrichment, not requirements**

#### 4. Structure Consistency
- [ ] **Follows standard section structure**
- [ ] **Uses appropriate heading levels**
- [ ] **Markdown formatting is consistent**
- [ ] **Length is appropriate** (500+ words)

#### 5. Links and References
- [ ] **Links are explanatory, not required**
- [ ] **All links use relative paths**
- [ ] **Links are labeled descriptively**
- [ ] **Links actually exist**

**Status**: ☐ PASS ☐ FAIL ☐ NEEDS REVISION

**Issues**: (list any problems found)

---

### File 3: [Filename]

#### 1. Standalone Readability
- [ ] **Document provides sufficient context**
- [ ] **No references to "previous sections" in other files**
- [ ] **Introductory paragraphs explain the topic clearly**
- [ ] **All technical terms are defined or linked**

#### 2. Complete Information
- [ ] **Reader gets actionable guidance**
- [ ] **Examples are self-contained**
- [ ] **Process steps are complete**
- [ ] **Troubleshooting is specific to this topic**

#### 3. No Circular References
- [ ] **Doesn't say "See [other file] for [its topic]"**
- [ ] **Doesn't require reading other files first**
- [ ] **Cross-references are enrichment, not requirements**

#### 4. Structure Consistency
- [ ] **Follows standard section structure**
- [ ] **Uses appropriate heading levels**
- [ ] **Markdown formatting is consistent**
- [ ] **Length is appropriate** (500+ words)

#### 5. Links and References
- [ ] **Links are explanatory, not required**
- [ ] **All links use relative paths**
- [ ] **Links are labeled descriptively**
- [ ] **Links actually exist**

**Status**: ☐ PASS ☐ FAIL ☐ NEEDS REVISION

**Issues**: (list any problems found)

---

## Overall Assessment

### Independence Test Results

| File | Readable Standalone? | Complete Information? | No Circular Refs? | Status |
|------|---|---|---|---|
| [File 1] | ☐ Yes ☐ No | ☐ Yes ☐ No | ☐ Yes ☐ No | ☐ PASS ☐ FAIL |
| [File 2] | ☐ Yes ☐ No | ☐ Yes ☐ No | ☐ Yes ☐ No | ☐ PASS ☐ FAIL |
| [File 3] | ☐ Yes ☐ No | ☐ Yes ☐ No | ☐ Yes ☐ No | ☐ PASS ☐ FAIL |

### Overall Status

**All files pass independence validation**: ☐ YES ☐ NO

If NO, list issues requiring revision:

1. ________________________________
2. ________________________________
3. ________________________________

---

## Sign-Off

**Reviewed by**: ___________________ **Date**: ___________

**Status**: ☐ APPROVED ☐ APPROVED WITH MINOR REVISIONS ☐ NEEDS MAJOR REVISIONS

**Comments**:

---

## Quick Independence Test

As a final check, have someone who doesn't know the skill:

1. Pick one detail file at random
2. Read it without reading other files
3. Answer: "Did you understand the topic and learn something useful?"

If YES → Detail files are independent ✓  
If NO → Detail files need revision

**Tester Name**: ___________________ **Result**: ☐ YES ☐ NO

