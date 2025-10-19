# PDF Document Handling

---
name: "PDF Document Handling"
description: "Extract text and tables, create new PDFs, merge/split documents, handle forms programmatically"
version: "1.0.0"
created: "2025-10-18"
tags: ["documents", "pdf", "forms", "text-extraction", "tables"]
dependencies: ["pypdf", "pdfplumber", "reportlab", "qpdf"]
source: "Adapted from Anthropic's PDF skill"
---

This skill provides comprehensive PDF manipulation using Python libraries (`pypdf`, `pdfplumber`, `reportlab`) and command-line tools (`qpdf`, `pdftotext`).

## When to Use This Skill

- Extract text or tables from PDF documents
- Merge multiple PDFs or split a PDF into separate files
- Create new PDF documents programmatically
- Fill out or extract data from PDF forms
- Analyze document structure and metadata
- Convert between PDF and other formats

## User Input

```text
$ARGUMENTS
```

## Relevance Keywords

Use this skill when the user mentions:
- PDF, PDFs, or PDF documents
- Form fields, form filling, or fillable PDFs
- Text extraction from documents
- Table extraction or parsing
- Merge PDF, combine PDF, or concatenate PDF
- Split PDF or extract pages
- Create PDF or generate PDF
- Watermark, rotate pages, or PDF metadata
- Government forms or applications
- Password-protected PDFs

## Progressive Loading Strategy

### Always Load First
1. `.github/copilot-skills/pdf-handling/SKILL.md` - Core capabilities and quick start

### Load When User Asks About
- **Forms, form filling, field extraction** → `.github/copilot-skills/pdf-handling/forms.md`
- **API details, advanced features, JavaScript libraries** → `.github/copilot-skills/pdf-handling/reference.md`

### Suggest Scripts When
- User needs to extract form fields → `scripts/extract_form_field_info.py`
- User needs to fill a form → `scripts/fill_fillable_fields.py`
- User needs to check field positions → `scripts/check_bounding_boxes.py`
- User has scanned PDF → `scripts/convert_pdf_to_images.py`

## Instructions

When this skill is invoked:

1. **Read SKILL.md first** to understand core capabilities
   - Location: `.github/copilot-skills/pdf-handling/SKILL.md`
   - Focus on: Overview, Core Capabilities, Quick Start

2. **Configure Python environment** (if not already configured)
   - Use `configure_python_environment` tool
   - Pass the workspace root path

3. **Install required dependencies** (before any Python operations)
   - Required packages: `pypdf`, `pdfplumber`, `reportlab`, `pandas`
   - Optional for Excel output: `openpyxl`
   - Optional for OCR: `pytesseract`, `pdf2image`
   - Use `install_python_packages` tool with package list
   - Installation command shown in SKILL.md:
     ```bash
     pip install pypdf pdfplumber reportlab pandas openpyxl
     ```

4. **Determine user's specific need**:
   - Text extraction → Show `pdfplumber` examples from SKILL.md
   - Table extraction → Show `pdfplumber` table examples
   - Document merging → Show `pypdf` merge pattern
   - Document splitting → Show `pypdf` split pattern
   - Form filling → Load `forms.md` for detailed instructions
   - PDF creation → Show `reportlab` examples

5. **For form-related tasks**:
   - Always load `forms.md` first
   - Follow the step-by-step process in forms.md
   - Suggest extracting field names before filling
   - Use bundled scripts for field inspection

6. **For complex scenarios**:
   - Load `reference.md` for advanced API details
   - Check reference.md for JavaScript alternatives
   - Reference troubleshooting section for errors

7. **When suggesting bundled scripts**:
   - Scripts provide deterministic operations
   - Always show usage example with correct Python path
   - Mention output format
   - Ensure dependencies are installed first

## Common Task Patterns

### Task: Extract text from PDF
**Response**:
1. Configure Python environment
2. Install dependencies: `["pypdf", "pdfplumber"]`
3. Show `pdfplumber` quick start from SKILL.md
4. For layout-sensitive PDFs, mention `layout=True` option
5. For scanned PDFs, suggest OCR approach (additional deps needed)

### Task: Extract tables
**Response**:
1. Configure Python environment
2. Install dependencies: `["pdfplumber", "pandas", "openpyxl"]`
3. Show `pdfplumber` table extraction from SKILL.md
4. Suggest saving to Excel with pandas
5. Mention table settings for complex layouts

### Task: Fill out a form
**Response**:
1. Load `forms.md` immediately
2. Show step 1: Extract field names using script
3. Show step 2: Fill fields programmatically
4. Mention form-specific patterns (government forms, etc.)

### Task: Merge/split PDFs
**Response**:
- Show `pypdf` merge or split pattern from SKILL.md
- For command-line, show `qpdf` alternative
- Mention page range syntax

### Task: Create PDF from scratch
**Response**:
- Show `reportlab` quick start from SKILL.md
- For complex layouts, mention Platypus framework
- Suggest looking at reference.md for templates

## Error Handling Guidance

When user encounters errors:

**"Cannot extract text"**
→ Check if PDF is scanned, suggest OCR approach

**"Permission denied"**
→ Check if encrypted, show `decrypt()` pattern

**"Tables extracted incorrectly"**
→ Show custom table settings from SKILL.md error handling section

**"Memory error"**
→ Suggest page-by-page processing pattern

## Output Format

**For quick tasks**:
Show relevant code snippet from SKILL.md with context

**For form filling**:
```
To fill this form, follow these steps:

1. Extract field names:
   [Show script command]

2. Review the fields:
   [Show expected output]

3. Fill the form:
   [Show fill pattern from forms.md]

For more details, see .github/copilot-skills/pdf-handling/forms.md
```

**For complex tasks**:
```
This requires [capability]. Here's the approach:

1. [Step 1 with code]
2. [Step 2 with code]

For advanced options, see .github/copilot-skills/pdf-handling/reference.md
```

## Dependencies Installation Workflow

**CRITICAL**: Always install dependencies BEFORE running any Python code or scripts.

### Workflow Order:
1. Configure Python environment first (if needed)
2. Install dependencies
3. Run Python code or scripts

### Required Dependencies:
```bash
pip install pypdf pdfplumber reportlab pandas openpyxl
```

### Optional Dependencies:
For OCR (scanned PDFs):
```bash
pip install pytesseract pdf2image
```

### Using Tools:
1. `configure_python_environment` - Set up Python environment
2. `install_python_packages` - Install required packages
   - Pass list: `["pypdf", "pdfplumber", "reportlab", "pandas", "openpyxl"]`
3. `run_in_terminal` or create scripts - Execute Python code

## Best Practices to Emphasize

1. Use `pdfplumber` for text/tables, `pypdf` for manipulation
2. Always check `is_encrypted` before operations
3. For forms: extract field names first
4. Process large files page-by-page
5. Validate table extraction results

## Integration with Other Skills

This skill may reference:
- **Database skills** - For storing extracted table data
- **File handling skills** - For batch processing multiple PDFs
- **Compliance skills** - For government form validation

## Examples

Show examples from SKILL.md based on task type. Don't reinvent patterns—reference the skill files.
