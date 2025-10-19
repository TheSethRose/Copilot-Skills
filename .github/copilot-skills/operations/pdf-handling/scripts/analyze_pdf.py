#!/usr/bin/env python3
"""
PDF Analysis Script - Bundled with PDF Handling Skill
Comprehensive PDF analysis: text extraction, table parsing, metadata extraction

Part of: .github/copilot-skills/pdf-handling/
Usage: python analyze_pdf.py <path_to_pdf>

Dependencies: pypdf, pdfplumber, pandas, openpyxl
Install: pip install pypdf pdfplumber pandas openpyxl
"""

from pypdf import PdfReader
import pdfplumber
import pandas as pd
from pathlib import Path

def analyze_pdf(pdf_path):
    """Comprehensive PDF analysis"""
    pdf_path = Path(pdf_path)
    print(f"📄 Analyzing: {pdf_path.name}\n")
    
    # ====================
    # 1. BASIC METADATA (using pypdf)
    # ====================
    print("="*60)
    print("METADATA & DOCUMENT INFO")
    print("="*60)
    
    reader = PdfReader(pdf_path)
    print(f"Pages: {len(reader.pages)}")
    
    if reader.metadata:
        meta = reader.metadata
        print(f"Title: {meta.title or 'N/A'}")
        print(f"Author: {meta.author or 'N/A'}")
        print(f"Subject: {meta.subject or 'N/A'}")
        print(f"Creator: {meta.creator or 'N/A'}")
    
    print(f"Encrypted: {reader.is_encrypted}")
    
    # ====================
    # 2. TEXT EXTRACTION (using pdfplumber for better accuracy)
    # ====================
    print("\n" + "="*60)
    print("TEXT EXTRACTION (First Page Preview)")
    print("="*60)
    
    with pdfplumber.open(pdf_path) as pdf:
        first_page_text = pdf.pages[0].extract_text()
        # Show first 500 characters
        preview = first_page_text[:500] + "..." if len(first_page_text) > 500 else first_page_text
        print(preview)
    
    # ====================
    # 3. TABLE EXTRACTION
    # ====================
    print("\n" + "="*60)
    print("TABLE EXTRACTION")
    print("="*60)
    
    all_tables = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            tables = page.extract_tables()
            if tables:
                print(f"\nPage {i+1}: Found {len(tables)} table(s)")
                for j, table in enumerate(tables):
                    if table:
                        print(f"  Table {j+1}: {len(table)} rows × {len(table[0]) if table else 0} columns")
                        all_tables.append({
                            'page': i+1,
                            'table_num': j+1,
                            'data': table
                        })
    
    print(f"\n📊 Total tables found: {len(all_tables)}")
    
    # ====================
    # 4. SAVE TABLES TO EXCEL
    # ====================
    if all_tables:
        print("\n" + "="*60)
        print("SAVING TABLES TO EXCEL")
        print("="*60)
        
        output_path = pdf_path.parent / f"{pdf_path.stem}_tables.xlsx"
        
        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
            for table_info in all_tables:
                table_data = table_info['data']
                page_num = table_info['page']
                table_num = table_info['table_num']
                
                # Convert to DataFrame
                if len(table_data) > 1:
                    # Use first row as headers if available
                    df = pd.DataFrame(table_data[1:], columns=table_data[0])
                else:
                    df = pd.DataFrame(table_data)
                
                # Create sheet name (max 31 chars for Excel)
                sheet_name = f"P{page_num}_T{table_num}"[:31]
                df.to_excel(writer, sheet_name=sheet_name, index=False)
                print(f"  ✓ Saved table from Page {page_num} to sheet '{sheet_name}'")
        
        print(f"\n✅ All tables saved to: {output_path}")
    
    # ====================
    # 5. FULL TEXT EXTRACTION TO FILE
    # ====================
    print("\n" + "="*60)
    print("EXTRACTING FULL TEXT")
    print("="*60)
    
    output_text_path = pdf_path.parent / f"{pdf_path.stem}_extracted.txt"
    
    with pdfplumber.open(pdf_path) as pdf:
        full_text = ""
        for i, page in enumerate(pdf.pages):
            full_text += f"\n\n{'='*60}\n"
            full_text += f"PAGE {i+1}\n"
            full_text += f"{'='*60}\n\n"
            full_text += page.extract_text()
    
    with open(output_text_path, 'w', encoding='utf-8') as f:
        f.write(full_text)
    
    print(f"✅ Full text extracted to: {output_text_path}")
    print(f"   Total characters: {len(full_text):,}")
    
    # ====================
    # SUMMARY
    # ====================
    print("\n" + "="*60)
    print("ANALYSIS COMPLETE")
    print("="*60)
    print(f"✓ Pages analyzed: {len(reader.pages)}")
    print(f"✓ Tables extracted: {len(all_tables)}")
    print(f"✓ Text extracted: {len(full_text):,} characters")
    print(f"\nOutput files:")
    print(f"  - {output_text_path.name}")
    if all_tables:
        excel_path = pdf_path.parent / f"{pdf_path.stem}_tables.xlsx"
        print(f"  - {excel_path.name}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python analyze_pdf.py <path_to_pdf>")
        print("\nExample:")
        print("  python analyze_pdf.py document.pdf")
        sys.exit(1)
    
    pdf_file = sys.argv[1]
    
    if not Path(pdf_file).exists():
        print(f"Error: File not found: {pdf_file}")
        sys.exit(1)
    
    try:
        analyze_pdf(pdf_file)
    except Exception as e:
        print(f"\n❌ Error analyzing PDF: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
