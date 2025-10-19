---
description: "Auto-loaded context for PDF document operations: parsing, generation, form handling, and text extraction"
applyTo: "**/*{pdf,PDF,report,Report,document,form}*"
---

# PDF Handling - Automatic Context Instructions

**Related Prompt:** `/pdf-handling`  
**Related Skill:** `.github/copilot-skills/pdf-handling/SKILL.md`

**Triggers:** PDF, pdf, report, export, document, form, fillable, extract text, merge pdf, split pdf, watermark, table extraction

## Context: PDF Document Operations

When working with files matching the patterns above, or when user queries contain PDF-related keywords, this context is automatically activated.

## Preferred Libraries

### Python (Recommended)
- **`pypdf`** (formerly PyPDF2) - Reading, merging, splitting PDFs
- **`pdfplumber`** - Text and table extraction with high accuracy
- **`reportlab`** - PDF generation and creation
- **`pdfrw`** - Form field manipulation and filling

### Command Line Tools
- **`qpdf`** - PDF transformation and repair
- **`pdftotext`** - Fast text extraction
- **`pdftk`** (legacy) - PDF manipulation toolkit

## Default Behaviors

### When user mentions "PDF" or "extract"
1. Suggest `/pdf-handling` skill prompt
2. Check if required libraries are installed
3. Prefer `pdfplumber` for text extraction (better accuracy than pypdf)
4. Handle password-protected PDFs with appropriate warnings

### When user mentions "form" or "fillable"
1. Suggest `/pdf-handling` skill prompt
2. Load `.github/copilot-skills/pdf-handling/forms.md` for detailed form handling
3. Prefer `pdfrw` for form field operations
4. Warn about XFA forms (not supported by most Python libraries)

### When user mentions "create" or "generate"
1. Suggest `/pdf-handling` skill prompt
2. Use `reportlab` for programmatic PDF creation
3. Consider HTML → PDF conversion for complex layouts (weasyprint, wkhtmltopdf)

## Quality Guidelines

### ✅ Do
- Validate PDF exists before processing
- Handle corrupted PDFs gracefully with try/except blocks
- Extract text page-by-page to manage memory with large files
- Preserve PDF metadata when merging/splitting
- Use context managers (`with open()`) for file operations

### ❌ Don't
- Load entire large PDFs into memory at once
- Assume all PDFs have selectable text (may be scanned images)
- Modify original files without creating backups
- Ignore PDF version compatibility issues
- Forget to handle password-protected PDFs

## Quick Start Template

```python
import pdfplumber

# Extract text from PDF
def extract_text(pdf_path: str) -> str:
    """Extract all text from a PDF file."""
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

# Extract tables from PDF
def extract_tables(pdf_path: str) -> list:
    """Extract all tables from a PDF file."""
    with pdfplumber.open(pdf_path) as pdf:
        tables = []
        for page in pdf.pages:
            tables.extend(page.extract_tables())
    return tables
```

## Error Handling Patterns

```python
from pypdf import PdfReader
from pypdf.errors import PdfReadError

def safe_pdf_read(pdf_path: str) -> PdfReader | None:
    """Safely attempt to read a PDF file."""
    try:
        return PdfReader(pdf_path)
    except PdfReadError as e:
        print(f"Error reading PDF: {e}")
        print("PDF may be corrupted or password-protected.")
        return None
    except FileNotFoundError:
        print(f"File not found: {pdf_path}")
        return None
```

## Next Steps

When working with PDFs:
1. Use `/pdf-handling` prompt for guided workflows
2. Check `.github/copilot-skills/pdf-handling/SKILL.md` for core capabilities
3. For advanced form handling, see `.github/copilot-skills/pdf-handling/forms.md`
4. For API reference, see `.github/copilot-skills/pdf-handling/reference.md`

## Related Skills

- **Document handling** - For DOCX, XLSX, PPTX operations
- **Data extraction** - For parsing structured data from documents
- **Report generation** - For creating formatted output documents
