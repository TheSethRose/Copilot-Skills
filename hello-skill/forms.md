# Hello Skill - Forms

This detail file demonstrates form-specific patterns and use cases for the Hello Skill, showing how detail files can focus on particular domains.

## Introduction

While the Hello Skill is simple, this detail file demonstrates how more complex skills can dedicate specific files to particular use cases. In a real skill like "PDF Handling", this file would cover form extraction and filling patterns.

---

## Use Case 1: Government Forms

### Form Field Naming Conventions

Government forms follow specific naming conventions:

- Field names are often prefixed with form number: `form_1040_line_1`
- Multi-page forms use page numbers: `form_1040_page_1_line_1`
- Date fields often end with `_date`: `application_submission_date`
- Yes/No fields use `_yes` and `_no` suffixes

### Pattern: Extract Government Form Fields

When working with government forms:

```
1. First, extract all field names to see what's available
2. Map form fields to your application's data model
3. Validate field names match exactly (case-sensitive)
4. Fill fields in a consistent order
5. Validate completed form before submission
```

### Example: IRS Form W-2

```
Form fields:
  box1: Employee's wages, tips, other compensation
  box2: Federal income tax withheld
  box3: Social security wages
  ssn: Employee's social security number
```

When filling:
1. Extract form structure first
2. Map to payroll data
3. Fill in order: SSN, name, then amount fields
4. Validate totals match expectations

---

## Use Case 2: Medical Forms

### Healthcare Form Characteristics

Medical forms often have:

- Patient demographic fields (name, DOB, SSN)
- Insurance information sections
- Checkboxes for medical history
- Signature fields
- Date fields in various formats

### Pattern: Handle Signature Fields

Signature fields in PDFs:

- Appear as rectangular regions (not text fields)
- Can be filled with images or drawn signatures
- Often have timestamp requirements
- May require additional validation

### Example: Consent Form

```
Structure:
  patient_name: Text field
  patient_dob: Date field
  signature: Signature field
  date_signed: Date field
  witness_name: Text field
  witness_signature: Signature field
```

Filling process:
1. Fill demographics
2. Add image signature (if digital)
3. Timestamp signature
4. Have witness countersign if required

---

## Use Case 3: Application Forms

### Application Form Patterns

Generic application forms typically include:

- Contact information (name, email, phone)
- Employment history (company, dates, role)
- Education (school, degree, graduation date)
- References (name, contact information)
- Certification or acceptance section

### Pattern: Validate Application Completeness

Before submitting an application form:

1. Check all required fields are filled
2. Validate date fields have proper format
3. Verify email addresses are valid
4. Confirm phone numbers are complete
5. Check file attachments if required

### Example: Job Application Form

```
Structure:
  applicant_name: Text
  email: Email
  phone: Phone
  current_employer: Text
  employment_start_date: Date
  employment_end_date: Date
  education_school: Text
  education_degree: Text
  education_graduation: Date
  references_name_1: Text
  references_email_1: Email
```

Validation:
- Name: Not empty, < 100 characters
- Email: Valid email format
- Phone: Valid phone format (handle area codes)
- Dates: Valid date, in expected range
- References: At least 2 references provided

---

## Common Form Issues and Solutions

### Issue 1: Field Name Mismatches

**Problem**: Script looks for "ssn" but field is "social_security_number"

**Solution**:
1. Extract all available fields: `extract_form_fields.py input.pdf --list-all`
2. Print field names to verify exact spelling
3. Update your mapping with exact names
4. Use field_name variable to avoid hardcoding

### Issue 2: Date Format Inconsistencies

**Problem**: Some fields expect MM/DD/YYYY, others expect YYYY-MM-DD

**Solution**:
1. Document expected format for each field
2. Parse input date, convert to expected format
3. Test with sample data before batch processing
4. Consider using a date formatting utility

### Issue 3: Multi-Page Forms

**Problem**: How to fill fields across multiple pages?

**Solution**:
1. Some form fields have page context: `page_2_field_name`
2. Track current page context
3. Fill pages in order
4. Validate all pages filled before submitting

---

## Best Practices for Form Handling

### 1. Always Extract Field Names First

Before filling a form:
```
python extract_form_fields.py input.pdf --format json > fields.json
cat fields.json | jq '.fields[] | .name' | sort
```

This shows:
- All available fields
- Exact field names (case-sensitive)
- Field data types
- Which fields are required

### 2. Validate Data Before Filling

Check that your data matches expected formats:

```python
def validate_before_filling(form_data, field_definitions):
    errors = []
    for field_name, field_definition in field_definitions.items():
        if field_definition['required'] and not form_data.get(field_name):
            errors.append(f"Required field missing: {field_name}")
        
        if field_definition['type'] == 'email':
            if not is_valid_email(form_data[field_name]):
                errors.append(f"Invalid email: {field_name}")
    
    return errors
```

### 3. Use Consistent Date Formats

Convert dates to expected format early:

```python
from datetime import datetime

def parse_and_format_date(date_str, target_format):
    # Parse input date (try multiple formats)
    for fmt in ['%Y-%m-%d', '%m/%d/%Y', '%m-%d-%Y']:
        try:
            dt = datetime.strptime(date_str, fmt)
            return dt.strftime(target_format)
        except ValueError:
            continue
    raise ValueError(f"Could not parse date: {date_str}")
```

### 4. Handle Optional Fields Gracefully

Not all forms require all fields:

```python
def fill_form(pdf_path, form_data):
    available_fields = extract_fields(pdf_path)
    
    for field_name, value in form_data.items():
        if field_name in available_fields:
            fill_field(pdf_path, field_name, value)
        else:
            log_warning(f"Field not found: {field_name}")
```

### 5. Validate After Filling

Always verify forms are complete before submission:

```python
def validate_filled_form(pdf_path, required_fields):
    filled_values = extract_filled_values(pdf_path)
    
    missing = []
    for field in required_fields:
        if not filled_values.get(field):
            missing.append(field)
    
    if missing:
        raise ValueError(f"Missing fields: {missing}")
    
    return True
```

---

## Form Processing Workflow

### Step-by-Step Process

1. **Analyze Form**
   - Extract all field names
   - Identify data types
   - Note required vs. optional
   - Document any custom formats

2. **Prepare Data**
   - Map your data to form fields
   - Validate formats match expectations
   - Handle missing data gracefully

3. **Fill Form**
   - Open PDF
   - Iterate through form_data
   - Fill each field
   - Handle errors for missing fields

4. **Validate Result**
   - Extract filled values
   - Confirm all required fields filled
   - Check for data entry errors
   - Verify form renders correctly

5. **Output**
   - Save filled PDF
   - Log what was filled
   - Report any warnings
   - Store metadata about process

### Example Pseudocode

```python
def process_form(template_pdf, form_data_json):
    # 1. Analyze
    fields = extract_form_fields(template_pdf)
    validate_schema(form_data_json, fields)
    
    # 2. Prepare
    normalized_data = normalize_data(form_data_json, fields)
    validation_errors = validate_data(normalized_data, fields)
    if validation_errors:
        return {"success": False, "errors": validation_errors}
    
    # 3. Fill
    output_pdf = fill_pdf_form(template_pdf, normalized_data)
    
    # 4. Validate
    filled_values = extract_filled_values(output_pdf)
    post_validation_errors = validate_result(filled_values, fields)
    if post_validation_errors:
        return {"success": False, "errors": post_validation_errors}
    
    # 5. Output
    return {
        "success": True,
        "output_file": output_pdf,
        "fields_filled": len(normalized_data),
        "metadata": {...}
    }
```

---

## Related Detail Files

- For API reference and functions, see `reference.md`
- For complete design documentation, see `patterns.md`

---

**Version**: 1.0.0 | **Last Updated**: October 18, 2025
