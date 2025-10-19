---
name: "PDF Document Handling"
description: "Extract text and tables, create new PDFs, merge/split documents, handle forms programmatically"
version: "1.0.0"
created: "2025-10-18"
tags: ["documents", "pdf", "forms", "text-extraction", "tables"]
dependencies: ["pypdf", "pdfplumber", "reportlab", "qpdf"]
source: "Adapted from Anthropic's PDF skill"
---

# PDF Document Handling

## Overview

This skill provides comprehensive PDF manipulation capabilities using Python libraries (`pypdf`, `pdfplumber`, `reportlab`) and command-line tools (`qpdf`, `pdftotext`). Use this skill for extracting text and tables, creating new PDFs, merging/splitting documents, and handling PDF forms.

**When to use this skill**:
- Extract text or tables from PDF documents
- Merge multiple PDFs or split a PDF into separate files
- Create new PDF documents programmatically
- Fill out PDF forms (government forms, applications)
- Add watermarks, rotate pages, or extract images
- Handle password-protected PDFs

## Core Capabilities

- **Text Extraction** - Extract plain text or structured content
- **Table Extraction** - Parse tables into structured data (CSV, Excel)
- **Document Merging** - Combine multiple PDFs into one
- **Document Splitting** - Extract pages into separate files
- **PDF Creation** - Generate new PDFs from scratch
- **Form Filling** - Programmatically fill PDF form fields
- **Metadata Operations** - Read/write PDF metadata
- **Security** - Add/remove passwords and encryption

## Quick Start

### Extract Text from PDF

```python
from pypdf import PdfReader

# Read PDF and extract text
reader = PdfReader("document.pdf")
print(f"Total pages: {len(reader.pages)}")

# Extract text from all pages
text = ""
for page in reader.pages:
    text += page.extract_text()
print(text)
```

### Extract Tables to Excel

```python
import pdfplumber
import pandas as pd

with pdfplumber.open("report.pdf") as pdf:
    tables = []
    for page in pdf.pages:
        for table in page.extract_tables():
            if table:  # Not empty
                df = pd.DataFrame(table[1:], columns=table[0])
                tables.append(df)
    
    # Combine and save
    if tables:
        combined = pd.concat(tables, ignore_index=True)
        combined.to_excel("output.xlsx", index=False)
```

### Merge Multiple PDFs

```python
from pypdf import PdfWriter, PdfReader

writer = PdfWriter()
for pdf_file in ["doc1.pdf", "doc2.pdf", "doc3.pdf"]:
    reader = PdfReader(pdf_file)
    for page in reader.pages:
        writer.add_page(page)

with open("merged.pdf", "wb") as output:
    writer.write(output)
```

### Create a New PDF

```python
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

c = canvas.Canvas("hello.pdf", pagesize=letter)
width, height = letter
c.drawString(100, height - 100, "Hello World!")
c.save()
```

## Progressive References

- **For form filling** → See [forms.md](./forms.md) - Government forms, field extraction, programmatic filling
- **For library APIs** → See [reference.md](./reference.md) - Advanced features, JavaScript libraries, troubleshooting

## Bundled Scripts

Scripts located in `scripts/` directory:

- `extract_form_fields.py` - Extract all form fields from a PDF to JSON
  ```bash
  python scripts/extract_form_fields.py input.pdf > fields.json
  ```

- `fill_form.py` - Fill PDF form from JSON data
  ```bash
  python scripts/fill_form.py input.pdf data.json output.pdf
  ```

- `merge_pdfs.py` - Merge multiple PDFs (CLI wrapper)
  ```bash
  python scripts/merge_pdfs.py doc1.pdf doc2.pdf doc3.pdf -o merged.pdf
  ```

## Common Patterns

### Pattern 1: Extract Text with Layout Preservation

When extracting text from PDFs with complex layouts (multi-column, tables), use `pdfplumber` instead of `pypdf`:

```python
import pdfplumber

with pdfplumber.open("document.pdf") as pdf:
    for page in pdf.pages:
        # Preserve layout structure
        text = page.extract_text(layout=True)
        print(text)
```

### Pattern 2: Handle Password-Protected PDFs

Always check if a PDF is encrypted before attempting operations:

```python
from pypdf import PdfReader

reader = PdfReader("encrypted.pdf")
if reader.is_encrypted:
    reader.decrypt("password")

# Now you can extract text
text = reader.pages[0].extract_text()
```

### Pattern 3: Split PDF by Page Range

Extract specific page ranges into new PDFs:

```python
from pypdf import PdfReader, PdfWriter

reader = PdfReader("document.pdf")

# Extract pages 1-5 (0-indexed: 0-4)
writer = PdfWriter()
for i in range(0, 5):
    writer.add_page(reader.pages[i])

with open("pages_1-5.pdf", "wb") as output:
    writer.write(output)
```

### Pattern 4: Extract and Process Tables

Parse tables and perform data transformations:

```python
import pdfplumber
import pandas as pd

with pdfplumber.open("financial_report.pdf") as pdf:
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            if table:
                # Convert to DataFrame
                df = pd.DataFrame(table[1:], columns=table[0])
                
                # Clean data (example: remove $ and commas)
                for col in df.columns:
                    if df[col].dtype == 'object':
                        df[col] = df[col].str.replace('$', '').str.replace(',', '')
                
                print(df)
```

## Command-Line Quick Reference

| Task | Command |
|------|---------|
| Extract text | `pdftotext document.pdf output.txt` |
| Extract with layout | `pdftotext -layout document.pdf output.txt` |
| Merge PDFs | `qpdf --empty --pages file1.pdf file2.pdf -- merged.pdf` |
| Split pages | `qpdf input.pdf --pages . 1-5 -- output.pdf` |
| Remove password | `qpdf --password=pwd --decrypt input.pdf output.pdf` |
| Extract images | `pdfimages -j input.pdf prefix` |

## Error Handling

### Common Issues

**Issue**: "Cannot extract text from PDF"
- **Cause**: PDF is scanned (image-based)
- **Solution**: Use OCR with `pytesseract` and `pdf2image`

**Issue**: "Permission denied" or encryption errors
- **Cause**: PDF is password-protected
- **Solution**: Use `reader.decrypt("password")` before operations

**Issue**: Tables extracted incorrectly
- **Cause**: Complex table structure or formatting
- **Solution**: Use `pdfplumber` with custom table settings:
  ```python
  table_settings = {
      "vertical_strategy": "lines",
      "horizontal_strategy": "lines"
  }
  tables = page.extract_tables(table_settings=table_settings)
  ```

**Issue**: Memory errors with large PDFs
- **Cause**: Loading entire PDF into memory
- **Solution**: Process page-by-page:
  ```python
  for i, page in enumerate(reader.pages):
      # Process one page at a time
      text = page.extract_text()
      # Do something with text
      # Page is garbage collected after loop iteration
  ```

## Installation

```bash
# Python libraries
pip install pypdf pdfplumber reportlab pandas

# Command-line tools (macOS)
brew install poppler qpdf

# Command-line tools (Ubuntu/Debian)
sudo apt-get install poppler-utils qpdf

# For OCR (optional)
pip install pytesseract pdf2image
brew install tesseract  # or apt-get install tesseract-ocr
```

## Best Practices

1. **Text Extraction**: Use `pdfplumber` for complex layouts, `pypdf` for simple text
2. **Form Filling**: Always extract field names first (see forms.md)
3. **Large Files**: Process page-by-page to avoid memory issues
4. **Error Handling**: Always check `is_encrypted` before operations
5. **Table Extraction**: Validate extracted tables, handle empty cells
6. **Security**: Never commit PDFs with sensitive data to git

## See Also

- [forms.md](./forms.md) - PDF form filling and field extraction
- [reference.md](./reference.md) - Advanced features and API reference
- [Anthropic's Original PDF Skill](../../examples/anthropics-skills/document-skills/pdf/)
