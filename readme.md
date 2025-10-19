# Extending GitHub Copilot with Copilot Skills
*Published Oct 18, 2025*

Copilot is powerful, but real projects need more than autocomplete—they need structure, context, and repeatable workflows. Introducing **Copilot Skills**, a new way to give GitHub Copilot specialized capabilities using simple markdown files and scripts inside your repository.

Inspired by Anthropic’s **Claude Skills**, Copilot Skills bring the same ideas—progressive disclosure, composable knowledge, and deterministic tools—into GitHub’s native environment. Using the `.github/copilot-skills/` directory, you can now organize your project’s procedural knowledge into discoverable skills that Copilot can reference when it matters most.

---

## Why Copilot Skills

Large language models like Copilot excel at generating code and completing patterns, but they can’t hold an entire project’s institutional knowledge in memory. Copilot Skills fix that by storing expertise in files that Copilot can read, reference, and suggest from—just like a human developer browsing documentation.

A skill is simply a folder that contains a `SKILL.md` file (plus any linked docs or scripts). Each skill teaches Copilot how to perform a particular kind of work—like handling PDFs, generating reports, or managing compliance logic.

By structuring skills this way, you can give Copilot modular, reusable knowledge that’s easy to share across teams and repositories.

---

## Anatomy of a Copilot Skill

Every skill lives in `.github/copilot-skills/` and includes a core file named `SKILL.md` that defines what the skill does. The file starts with YAML frontmatter containing key metadata:

- **name** – the skill’s title  
- **description** – what it enables Copilot to do  
- **version** – optional, for version tracking  
- **dependencies** – libraries or tools required  

At startup, Copilot can scan the skill index file (`.github/copilot-skills/index.md`) to discover which skills exist and when they should be used.

Here’s what a directory might look like:

```

.github/
├── copilot-instructions.md
├── copilot-skills/
│   ├── index.md
│   ├── pdf-handling/
│   │   ├── SKILL.md
│   │   ├── forms.md
│   │   ├── reference.md
│   │   └── scripts/
│   │       └── extract_form_fields.py
│   ├── financial-reporting/
│   ├── database-migration/
│   └── compliance-tracking/

````

This setup keeps every skill self-contained and easy to maintain.

---

## Progressive Disclosure

Each skill loads in layers:

1. **Index Metadata** – the skill name, path, and short description live in `.github/copilot-skills/index.md`.  
2. **Core Instructions** – the main `SKILL.md` file provides essential context.  
3. **Linked References** – optional supporting files (like `forms.md` or `reference.md`) add detail only when needed.  
4. **Executable Scripts** – bundled tools that let Copilot suggest deterministic operations, like running `extract_form_fields.py`.

This approach lets Copilot stay efficient by referencing only what’s relevant to the current task, instead of loading everything at once.

---

## Example: PDF Handling Skill

A **PDF Handling** skill might include metadata, core instructions, references, and scripts for text extraction or form filling.

```markdown
---
name: "PDF Handling"
description: "Extract text, fill forms, and manipulate PDF documents"
version: "1.0"
dependencies: ["pypdf2", "pdfplumber"]
---

# PDF Handling Skill

This skill teaches Copilot how to read and manipulate PDFs, extract form fields, and generate structured data.

### Capabilities
- Extract text and tables
- Parse and fill PDF forms
- Handle password-protected files gracefully

For form-specific instructions, see [forms.md](./forms.md).  
For library references, see [reference.md](./reference.md).
````

Linked scripts can provide deterministic workflows—for example:

```bash
python .github/copilot-skills/pdf-handling/scripts/extract_form_fields.py input.pdf
```

---

## How Copilot Uses Skills

Copilot interacts with skills in three main ways:

1. **Automatic Discovery**
   When you start a task like “extract form fields from a PDF,” Copilot scans `index.md`, finds the PDF Handling skill, and references its `SKILL.md`.

2. **Explicit Reference**
   You can mention a skill directly:
   “Using the PDF Handling skill, extract all fields from form.pdf.”

3. **Progressive Loading**
   For more complex workflows—like filling a government form—Copilot can read linked files (`forms.md`, `reference.md`) only when they’re needed.

This system keeps Copilot’s context window lean while giving it deep, structured guidance on demand.

---

## Authoring Your Own Skills

Creating a skill is straightforward:

1. **Start with Metadata**
   Write clear names and descriptions. Copilot relies on them to decide when a skill applies.

2. **Structure for Clarity**
   Keep `SKILL.md` focused on core concepts. Move detailed examples or region-specific logic into linked files.

3. **Include Executable Scripts**
   Scripts provide reliable, reusable actions. Copilot can suggest running them rather than reproducing code inline.

4. **Document Dependencies and Patterns**
   List required packages, and show Copilot how to solve common problems through code snippets and patterns.

Here’s a compliance tracking example:

````markdown
---
name: "Texas Trade Compliance"
description: "License validation, expiration tracking, and compliance calculations for Texas service trades"
version: "1.0"
dependencies: ["prisma", "date-fns"]
---

# Texas Trade Compliance Skill

Calculates license status, tracks insurance, and raises warnings 30 days before expiration.

### Core Logic
```typescript
function calculateLicenseStatus(expiresOn: Date | null, today: Date) {
  if (!expiresOn) return 'MISSING';
  if (expiresOn < today) return 'EXPIRED';
  return 'VALID';
}
````

See [texas-licensing.md](./texas-licensing.md) and [calculations.md](./calculations.md) for details.

````

---

## Integrating Skills with Copilot Instructions

Reference your skills in `.github/copilot-instructions.md` so developers and Copilot can find them easily:

```markdown
## Skills System

This project uses modular Copilot Skills for domain-specific knowledge.  
Skills are stored in `.github/copilot-skills/`.

When working on:
- PDFs → use the PDF Handling skill  
- Financial reports → use the Financial Reporting skill  
- Database migrations → use the Database Migration skill  
- Compliance → use the Texas Trade Compliance skill
````

---

## Advantages of the Skills Model

| Approach                                   | Context Usage              | Maintainability | Discoverability      |
| ------------------------------------------ | -------------------------- | --------------- | -------------------- |
| **Monolithic** (one big instructions file) | Always loaded              | Hard to update  | Hard to navigate     |
| **Skills-based** (modular)                 | Loads only what’s relevant | Easy to update  | Clear and searchable |

This modular design improves both token efficiency and developer workflow. Copilot only loads the knowledge it needs for the current task, reducing clutter and confusion.

---

## Migration Guide

To move from a single-file setup to skills:

1. Identify distinct knowledge domains in your current Copilot instructions.
2. Create a new folder under `.github/copilot-skills/` for each domain.
3. Write `SKILL.md` with metadata, examples, and linked references.
4. Add scripts for deterministic operations.
5. Register each skill in `index.md`.
6. Update your main instructions to point to the skills directory.
7. Test and refine until Copilot reliably references the right skills.

---

## Advanced Patterns

* **Cross-skill references:**
  Skills can link to one another for connected workflows, like compliance-driven schema migrations.

* **Skill composition:**
  Copilot can combine multiple skills—for example, generating a compliance report PDF by loading both the Compliance and PDF Handling skills.

* **Version management:**
  Track updates in YAML frontmatter to ensure reproducibility.

---

## Key Differences from Claude Skills

| Feature                 | Claude Skills     | Copilot Skills             |
| ----------------------- | ----------------- | -------------------------- |
| **Automatic discovery** | System-level scan | Manual via index or prompt |
| **Dynamic loading**     | Automatic         | Based on user context      |
| **Script execution**    | Direct execution  | Suggested commands         |
| **Context management**  | AI-managed        | Developer-guided           |

Because Copilot doesn’t have full filesystem navigation, explicit linking and clear metadata are crucial. Mentioning skill names in prompts (“Using the compliance skill…”) helps Copilot surface relevant knowledge faster.

---

## Example Use Cases

### 1. Onboarding a New Developer

A developer joins the project and needs to understand compliance rules.
They open `.github/copilot-skills/index.md`, find “Texas Trade Compliance,” and explore linked files to see logic, examples, and code patterns.

### 2. Adding a New Feature

While building invoice PDF generation, the developer opens `pdf-handling/SKILL.md`. Copilot suggests the right script and templates based on the documented pattern.

### 3. Fixing a Bug

When correcting a license expiration formula, the developer checks `compliance-tracking/SKILL.md` and linked calculation files. Copilot recommends a fix consistent with the documented logic.

---

## Getting Started

* [ ] Create `.github/copilot-skills/` directory
* [ ] Add `index.md` with metadata
* [ ] Identify your first 2–3 skills
* [ ] Write `SKILL.md` with clear metadata and examples
* [ ] Add any supporting scripts
* [ ] Reference skills from `copilot-instructions.md`
* [ ] Test and refine

---

## The Future of Copilot Skills

Copilot Skills make project knowledge modular, searchable, and reusable—without overwhelming the context window.
They help teams capture and share their best practices in code, documentation, and scripts that Copilot can actually use.

As Copilot evolves, we expect richer integrations: automatic skill discovery, contextual loading, and perhaps even self-maintaining skills that update as your codebase grows.

For now, skills give you a simple, powerful way to teach Copilot your project’s unique workflow.

---

**We’re excited to see what you build with Copilot Skills.**
Start by creating your first skill today in `.github/copilot-skills/`.