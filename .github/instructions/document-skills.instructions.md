---
description: "Auto-loaded context for document operations across PDF, DOCX, PPTX, and XLSX formats"
applyTo: "**/*{pdf,PDF,docx,DOCX,pptx,PPTX,xlsx,XLSX,document,form}*"
---

# Document Skills - Automatic Context Instructions

**Related Prompt:** `/document-skills`  
**Related Skills:** 
- `/pdf-handling` - `.github/copilot-skills/pdf-handling/README.md`
- DOCX, PPTX, XLSX (future sub-skills)

**Triggers:** pdf, document, docx, pptx, xlsx, word, powerpoint, excel, extract, merge, split, form, table, spreadsheet

## Context: Multi-Format Document Operations

When working with document files or when user queries contain document-related keywords, this context is automatically activated.

## Default Behaviors

### When user mentions "PDF" or "pdf"
1. Suggest `/pdf-handling` skill prompt (specialized sub-skill)
2. Load `.github/copilot-skills/pdf-handling/README.md` for operations
3. Reference form handling in `forms.md` if form-related
4. Use bundled scripts in `pdf-handling/scripts/`

### When user mentions "form" or "fill"
1. Suggest `/pdf-handling` specifically for forms
2. Load `pdf-handling/forms.md` for form patterns
3. Use `fill_pdf_form_with_annotations.py` or `fill_fillable_fields.py`
4. Extract field info with `extract_form_field_info.py`

### When user mentions "extract" or "table"
1. Check if PDF extraction needed
2. Use appropriate extraction scripts
3. Validate output format
4. Handle text vs structured data differently

### When user mentions "Word" or "DOCX"
1. Suggest document-skills with DOCX focus
2. Note: Full DOCX skill coming soon
3. Use `python-docx` library patterns

### When user mentions "PowerPoint" or "PPTX"
1. Suggest document-skills with PPTX focus
2. Reference brand-guidelines for styling
3. Use `python-pptx` library patterns

### When user mentions "Excel" or "XLSX"
1. Suggest document-skills with XLSX focus
2. Use `openpyxl` or `pandas` for operations
3. Handle data validation and formatting

## Quality Guidelines

### ✅ Do
- Validate document structure before operations
- Handle errors gracefully (corrupted files, missing fields)
- Use appropriate libraries for each format
- Test output files are valid and openable
- Respect document security settings
- Extract data in structured formats
- Preserve formatting when possible
- Use type-safe field names

### ❌ Don't
- Assume all PDFs have forms
- Ignore PDF security restrictions
- Generate invalid document structures
- Mix document formats without conversion
- Lose formatting during extraction
- Hard-code field names without validation
- Process corrupted files without error handling
- Ignore document metadata

## Common Libraries

### PDF Operations
```python
# pypdf - Core PDF manipulation
from pypdf import PdfReader, PdfWriter

# pdf2image - Convert PDF to images
from pdf2image import convert_from_path

# reportlab - Generate PDFs from scratch
from reportlab.pdfgen import canvas
```

### DOCX Operations
```python
# python-docx - Word document handling
from docx import Document
```

### PPTX Operations
```python
# python-pptx - PowerPoint handling
from pptx import Presentation
```

### XLSX Operations
```python
# openpyxl - Excel handling
from openpyxl import load_workbook

# pandas - Data manipulation
import pandas as pd
```

## Bundled Scripts (PDF)

The pdf-handling sub-skill provides these scripts:

```bash
# Extract form field information
python .github/copilot-skills/pdf-handling/scripts/extract_form_field_info.py <file>

# Fill PDF form fields
python .github/copilot-skills/pdf-handling/scripts/fill_fillable_fields.py <file> <fields>

# Convert PDF to images
python .github/copilot-skills/pdf-handling/scripts/convert_pdf_to_images.py <file>

# Analyze PDF structure
python .github/copilot-skills/pdf-handling/scripts/analyze_pdf.py <file>

# Check fillable fields
python .github/copilot-skills/pdf-handling/scripts/check_fillable_fields.py <file>
```

All scripts output to terminal (no files generated) for AI parsing.

## Common Workflows

### Extract PDF Form Fields
```python
from pypdf import PdfReader

reader = PdfReader("form.pdf")
fields = reader.get_fields()

for field_name, field_data in fields.items():
    print(f"{field_name}: {field_data.get('/V', 'No value')}")
```

### Fill PDF Form
```python
from pypdf import PdfReader, PdfWriter

reader = PdfReader("form.pdf")
writer = PdfWriter()

writer.append_pages_from_reader(reader)
writer.update_page_form_field_values(
    writer.pages[0],
    {"FieldName": "Value"}
)

with open("filled.pdf", "wb") as output:
    writer.write(output)
```

### Merge PDFs
```python
from pypdf import PdfWriter

writer = PdfWriter()
for pdf_file in ["doc1.pdf", "doc2.pdf"]:
    writer.append(pdf_file)

with open("merged.pdf", "wb") as output:
    writer.write(output)
```

### Extract Text
```python
from pypdf import PdfReader

reader = PdfReader("document.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text()
```

## Next Steps

When working with documents:
1. Use `/document-skills` prompt for general guidance
2. Use `/pdf-handling` for PDF-specific operations
3. Check `pdf-handling/forms.md` for form handling
4. Check `pdf-handling/reference.md` for advanced techniques
5. Run bundled scripts for automated operations

## Related Skills

- **PDF Handling** - Specialized PDF operations (primary sub-skill)
- **Brand Guidelines** - Apply brand styling to documents
- **Cleanup** - Remove temporary document artifacts
- **Git Ops** - Version control for document changes
