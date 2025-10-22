# Claude - Agent Skills

**Pages**: 2

---

## Skill authoring best practices

**URL**: https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices

**Contents**:
- ​Core principles
  - ​Concise is key
  - ​Set appropriate degrees of freedom
  - ​Test with all models you plan to use
- ​Skill structure
  - ​Naming conventions
  - ​Writing effective descriptions
  - ​Progressive disclosure patterns

**Examples**:

```text
## Extract PDF text

Use pdfplumber for text extraction:

```python
import pdfplumber

with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```
```

```text
## Extract PDF text

PDF (Portable Document Format) files are a common file format that contains
text, images, and other content. To extract text from a PDF, you'll need to
use a library. There are many libraries available for PDF processing, but we
recommend pdfplumber because it's easy to use and handles most cases well.
First, you'll need to install it using pip. Then you can use the code below...
```

```text
## Code review process

1. Analyze the code structure and organization
2. Check for potential bugs or edge cases
3. Suggest improvements for readability and maintainability
4. Verify adherence to project conventions
```

---

## Skill authoring best practices - Claude Docs

**URL**: https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices

---
