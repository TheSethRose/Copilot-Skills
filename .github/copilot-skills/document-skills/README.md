---
name: document-skills
description: Comprehensive toolkit for document operations across PDF, DOCX, PPTX, and XLSX formats
version: "1.0.0"
tags: ["pdf", "docx", "pptx", "xlsx", "documents", "forms", "extraction"]
dependencies: ["pypdf", "python-docx", "python-pptx", "openpyxl"]
license: Collection of document manipulation skills
---

# Document Skills

## Overview

Comprehensive toolkit for manipulating documents in multiple formats: PDF, DOCX, PPTX, and XLSX.

**Keywords**: pdf, document, docx, pptx, xlsx, word, powerpoint, excel, extract, merge, split, form, table, spreadsheet

## Document Format Support

This skill is a collection of specialized document manipulation capabilities:

### PDF Operations (Primary)
**Status**: Fully implemented
**Location**: Sub-skill at `.github/copilot-skills/pdf-handling/`

Comprehensive PDF manipulation including:
- **Form Filling**: Fill PDF forms programmatically
- **Field Extraction**: Extract form field information and structure
- **Text Extraction**: Extract text content from PDFs
- **Table Extraction**: Extract tables and structured data
- **Merging/Splitting**: Combine or separate PDF documents
- **Conversion**: Convert PDFs to images
- **Validation**: Analyze PDF structure and validate forms

### DOCX Operations
**Status**: Planned
**Future Capabilities**:
- Create Word documents from templates
- Extract content and formatting
- Modify existing documents
- Convert to/from other formats

### PPTX Operations
**Status**: Planned
**Future Capabilities**:
- Generate PowerPoint presentations
- Apply brand styling to slides
- Extract content from presentations
- Modify existing slides

### XLSX Operations
**Status**: Planned
**Future Capabilities**:
- Read and write Excel spreadsheets
- Perform calculations
- Format cells and data
- Extract data for analysis

## PDF Operations (Detailed)

### Core Capabilities

#### Form Handling
- **Fill Forms**: `fill_pdf_form_with_annotations.py`, `fill_fillable_fields.py`
- **Extract Fields**: `extract_form_field_info.py`
- **Check Fields**: `check_fillable_fields.py`
- **Validate Forms**: Analyze form structure and field types

#### Content Extraction
- **Text Extraction**: Extract all text content
- **Table Extraction**: Identify and extract tabular data
- **Structure Analysis**: Understand PDF document structure
- **Metadata Extraction**: Get document properties

#### Document Manipulation
- **Merge PDFs**: Combine multiple PDFs into one
- **Split PDFs**: Separate pages into individual files
- **Page Operations**: Extract, reorder, or delete pages
- **Watermarks**: Add watermarks or overlays

#### Conversion and Analysis
- **PDF to Images**: Convert pages to PNG/JPEG
- **Structure Validation**: Check PDF validity
- **Bounding Box Analysis**: Analyze element positioning
- **Form Validation**: Verify form field structure

### Bundled Scripts

All scripts are in `.github/copilot-skills/pdf-handling/scripts/`:

```bash
# Extract form field information
python extract_form_field_info.py <file>

# Fill PDF form fields
python fill_fillable_fields.py <file> <fields>

# Fill forms with annotations
python fill_pdf_form_with_annotations.py <file> <data>

# Convert PDF to images
python convert_pdf_to_images.py <file>

# Analyze PDF structure
python analyze_pdf.py <file>

# Check fillable fields
python check_fillable_fields.py <file>

# Check bounding boxes
python check_bounding_boxes.py <file>

# Create validation image
python create_validation_image.py <file>
```

### Python Libraries

#### pypdf - Core PDF Manipulation
```python
from pypdf import PdfReader, PdfWriter

# Read PDF
reader = PdfReader("document.pdf")
print(f"Pages: {len(reader.pages)}")

# Extract text
text = ""
for page in reader.pages:
    text += page.extract_text()

# Merge PDFs
writer = PdfWriter()
for pdf_file in ["doc1.pdf", "doc2.pdf"]:
    writer.append(pdf_file)
with open("merged.pdf", "wb") as output:
    writer.write(output)
```

#### pdf2image - Convert to Images
```python
from pdf2image import convert_from_path

images = convert_from_path("document.pdf")
for i, image in enumerate(images):
    image.save(f"page_{i}.png", "PNG")
```

#### reportlab - Generate PDFs
```python
from reportlab.pdfgen import canvas

c = canvas.Canvas("output.pdf")
c.drawString(100, 750, "Hello World")
c.save()
```

### Common Workflows

#### Extract Form Fields
```python
from pypdf import PdfReader

reader = PdfReader("form.pdf")
fields = reader.get_fields()

for field_name, field_data in fields.items():
    field_type = field_data.get('/FT', 'Unknown')
    field_value = field_data.get('/V', 'No value')
    print(f"{field_name} ({field_type}): {field_value}")
```

#### Fill PDF Form
```python
from pypdf import PdfReader, PdfWriter

reader = PdfReader("form.pdf")
writer = PdfWriter()

writer.append_pages_from_reader(reader)
writer.update_page_form_field_values(
    writer.pages[0],
    {
        "Name": "John Doe",
        "Email": "john@example.com",
        "Date": "2025-10-19"
    }
)

with open("filled.pdf", "wb") as output:
    writer.write(output)
```

#### Merge Multiple PDFs
```python
from pypdf import PdfWriter

writer = PdfWriter()
for pdf_file in ["doc1.pdf", "doc2.pdf", "doc3.pdf"]:
    writer.append(pdf_file)

with open("merged.pdf", "wb") as output:
    writer.write(output)
```

#### Split PDF by Pages
```python
from pypdf import PdfReader, PdfWriter

reader = PdfReader("input.pdf")
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    writer.add_page(page)
    with open(f"page_{i}.pdf", "wb") as output:
        writer.write(output)
```

## Detail Files

For PDF operations specifically:
- **forms.md**: PDF form handling patterns and examples (at `pdf-handling/forms.md`)
- **reference.md**: Advanced PDF techniques and libraries (at `pdf-handling/reference.md`)
- **scripts/**: Bundled Python tools for PDF operations (at `pdf-handling/scripts/`)

## Dependencies

### PDF Operations
```bash
pip install pypdf pdf2image pillow reportlab
```

### DOCX Operations (Future)
```bash
pip install python-docx
```

### PPTX Operations (Future)
```bash
pip install python-pptx
```

### XLSX Operations (Future)
```bash
pip install openpyxl pandas
```

## Best Practices

### PDF Operations
- Validate document structure before operations
- Handle errors gracefully (corrupted files, missing fields)
- Test output files are valid and openable
- Respect document security settings
- Extract data in structured formats
- Preserve formatting when possible
- Use type-safe field names

### Error Handling
```python
try:
    reader = PdfReader("document.pdf")
except Exception as e:
    print(f"Failed to read PDF: {e}")
    # Handle error appropriately
```

### Form Field Validation
```python
def validate_form_fields(pdf_path, required_fields):
    """Validate that PDF has required form fields."""
    reader = PdfReader(pdf_path)
    fields = reader.get_fields()
    
    if not fields:
        return False, "PDF has no form fields"
    
    missing = set(required_fields) - set(fields.keys())
    if missing:
        return False, f"Missing fields: {missing}"
    
    return True, "All required fields present"
```

## Progressive Disclosure

For additional PDF handling details:
1. **Core operations**: This README
2. **Form handling**: `pdf-handling/forms.md`
3. **Advanced techniques**: `pdf-handling/reference.md`
4. **Bundled tools**: `pdf-handling/scripts/`

For other document formats:
- DOCX, PPTX, XLSX capabilities coming soon
- Check back for updates to document-skills

## Related Skills

- **PDF Handling** - Specialized PDF operations (primary implemented sub-skill)
- **Brand Guidelines** - Apply brand styling to documents
- **Cleanup** - Remove temporary document artifacts
- **Git Ops** - Version control for document changes
