# Document Operations Assistant

---
description: "Comprehensive toolkit for manipulating documents in multiple formats: PDF, DOCX, PPTX, XLSX"
---

# Document Skills

Perform operations on various document formats including PDF manipulation, Word document processing, PowerPoint editing, and Excel spreadsheet handling.

## When to Use This Skill

Use this skill when:
- Processing, generating, or analyzing PDF documents
- Extracting text, tables, or data from documents
- Creating or modifying Word documents (DOCX)
- Working with PowerPoint presentations (PPTX)
- Manipulating Excel spreadsheets (XLSX)
- Converting between document formats
- Merging, splitting, or organizing documents
- Filling PDF forms or extracting form data

**Keywords**: pdf, document, docx, pptx, xlsx, word, powerpoint, excel, extract, merge, split, form, table, spreadsheet

## Workflow

### Step 1: Identify Document Type and Operation

Determine what type of document and what operation:
- **PDF**: Extract, merge, split, fill forms, extract tables
- **DOCX**: Create, modify, extract content
- **PPTX**: Generate, edit, apply styling
- **XLSX**: Read, write, calculate, format

### Step 2: Choose Appropriate Sub-Skill

Based on document type, use the corresponding sub-skill:

#### PDF Operations (`/pdf-handling`)
- Extract text and tables from PDFs
- Merge or split PDF documents
- Fill PDF forms programmatically
- Convert PDFs to images
- Extract form field information
- Validate PDF structure

#### DOCX Operations
- Create Word documents from templates
- Extract content and formatting
- Modify existing documents
- Convert to/from other formats

#### PPTX Operations
- Generate PowerPoint presentations
- Apply brand styling to slides
- Extract content from presentations
- Modify existing slides

#### XLSX Operations
- Read and write Excel spreadsheets
- Perform calculations
- Format cells and data
- Extract data for analysis

### Step 3: Execute Operation

Use appropriate tools and libraries:
```bash
# PDF operations (Python)
python .github/copilot-skills/pdf-handling/scripts/extract_form_field_info.py input.pdf

# Or use library directly
from pypdf import PdfReader, PdfWriter
```

### Step 4: Validate Results

Verify operation success:
- Check output file exists and is valid
- Verify extracted data is complete
- Test filled forms display correctly
- Validate conversions maintain fidelity

## Examples

### Example 1: Extract PDF Form Fields
```bash
python .github/copilot-skills/pdf-handling/scripts/extract_form_field_info.py form.pdf
```

### Example 2: Fill PDF Form
```python
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject

reader = PdfReader("form.pdf")
writer = PdfWriter()

# Fill fields
writer.append_pages_from_reader(reader)
writer.update_page_form_field_values(
    writer.pages[0], 
    {"FieldName": "Value"}
)

with open("filled.pdf", "wb") as output:
    writer.write(output)
```

### Example 3: Extract Text from PDF
```python
from pypdf import PdfReader

reader = PdfReader("document.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text()
```

## Sub-Skills

This skill is a collection of specialized document skills:

### PDF Handling (`/pdf-handling`)
**Location**: `.github/prompts/pdf-handling.skill.prompt.md`
**Detail**: `.github/copilot-skills/pdf-handling/README.md`
**Scripts**: `.github/copilot-skills/pdf-handling/scripts/`

Comprehensive PDF manipulation including:
- Form filling and field extraction
- Text and table extraction
- Merging and splitting
- PDF to image conversion
- Structure validation

### DOCX Operations
**Future**: Word document processing
**Capabilities**: Create, modify, extract from Word documents

### PPTX Operations
**Future**: PowerPoint presentation handling
**Capabilities**: Generate, edit, style presentations

### XLSX Operations
**Future**: Excel spreadsheet manipulation
**Capabilities**: Read, write, calculate, format spreadsheets

## Detail Files

For PDF operations specifically:
- **forms.md**: PDF form handling patterns
- **reference.md**: Advanced PDF techniques and libraries
- **scripts/**: Bundled Python tools for PDF operations

## Notes

- PDF operations require `pypdf` library: `pip install pypdf`
- For image conversion: `pip install pdf2image pillow`
- Form operations may require `reportlab` for complex scenarios
- Always validate document structure before operations
- Handle errors gracefully (corrupted files, missing fields)

## Related Skills

- **Brand Guidelines** - Apply brand styling to documents
- **Git Ops** - Version control for document changes
- **Cleanup** - Remove temporary document artifacts
