#!/usr/bin/env python3
"""
YAML Validator for SKILL.md Frontmatter

Validates YAML frontmatter in SKILL.md files against the schema defined in skill_schema.yaml.
Can be called from bash scripts or used as a standalone validator.
"""

import sys
import re
import yaml
from pathlib import Path
from typing import Dict, List, Any, Tuple

# Schema definition (embedded for portability)
SCHEMA = {
    "required": ["name", "description", "version", "tags", "dependencies"],
    "optional": ["created", "updated", "author", "license"],
    "field_types": {
        "name": str,
        "description": str,
        "version": str,
        "tags": list,
        "dependencies": list,
        "created": str,
        "updated": str,
        "author": str,
        "license": str,
    },
    "validation_rules": {
        "name": {
            "min_length": 3,
            "max_length": 100,
            "pattern": r"^[A-Z][A-Za-z0-9\s-]+$",
        },
        "description": {
            "min_length": 10,
            "max_length": 500,
        },
        "version": {
            "pattern": r"^\d+\.\d+\.\d+$",
        },
        "tags": {
            "min_items": 1,
            "max_items": 10,
            "item_pattern": r"^[a-z0-9-]+$",
        },
        "dependencies": {
            "min_items": 0,
            "max_items": 20,
            "item_pattern": r"^[a-zA-Z0-9_.-]+$",
        },
    },
}


def extract_frontmatter(content: str) -> Tuple[Dict[str, Any], List[str]]:
    """
    Extract YAML frontmatter from markdown content.
    
    Returns:
        Tuple of (frontmatter_dict, errors_list)
    """
    errors = []
    
    # Check for frontmatter delimiters
    if not content.startswith("---\n"):
        errors.append("Missing opening '---' delimiter for YAML frontmatter")
        return {}, errors
    
    # Find closing delimiter
    end_pos = content.find("\n---\n", 4)
    if end_pos == -1:
        errors.append("Missing closing '---' delimiter for YAML frontmatter")
        return {}, errors
    
    # Extract YAML content
    yaml_content = content[4:end_pos]
    
    try:
        frontmatter = yaml.safe_load(yaml_content)
        if not isinstance(frontmatter, dict):
            errors.append(f"Frontmatter must be a dictionary, got {type(frontmatter).__name__}")
            return {}, errors
        return frontmatter, errors
    except yaml.YAMLError as e:
        errors.append(f"Invalid YAML syntax: {str(e)}")
        return {}, errors


def validate_required_fields(frontmatter: Dict[str, Any]) -> List[str]:
    """Check that all required fields are present."""
    errors = []
    for field in SCHEMA["required"]:
        if field not in frontmatter:
            errors.append(f"Missing required field: '{field}'")
    return errors


def validate_field_types(frontmatter: Dict[str, Any]) -> List[str]:
    """Validate that field values are of the correct type."""
    errors = []
    for field, value in frontmatter.items():
        if field in SCHEMA["field_types"]:
            expected_type = SCHEMA["field_types"][field]
            if not isinstance(value, expected_type):
                errors.append(
                    f"Field '{field}' should be {expected_type.__name__}, got {type(value).__name__}"
                )
    return errors


def validate_field_rules(frontmatter: Dict[str, Any]) -> List[str]:
    """Validate field values against specific rules."""
    errors = []
    
    for field, value in frontmatter.items():
        if field not in SCHEMA["validation_rules"]:
            continue
        
        rules = SCHEMA["validation_rules"][field]
        
        # String length validation
        if isinstance(value, str):
            if "min_length" in rules and len(value) < rules["min_length"]:
                errors.append(
                    f"Field '{field}' must be at least {rules['min_length']} characters, got {len(value)}"
                )
            if "max_length" in rules and len(value) > rules["max_length"]:
                errors.append(
                    f"Field '{field}' must be at most {rules['max_length']} characters, got {len(value)}"
                )
            if "pattern" in rules and not re.match(rules["pattern"], value):
                errors.append(
                    f"Field '{field}' does not match required pattern: {rules['pattern']}"
                )
        
        # Array validation
        if isinstance(value, list):
            if "min_items" in rules and len(value) < rules["min_items"]:
                errors.append(
                    f"Field '{field}' must have at least {rules['min_items']} items, got {len(value)}"
                )
            if "max_items" in rules and len(value) > rules["max_items"]:
                errors.append(
                    f"Field '{field}' must have at most {rules['max_items']} items, got {len(value)}"
                )
            if "item_pattern" in rules:
                pattern = rules["item_pattern"]
                for i, item in enumerate(value):
                    if not isinstance(item, str) or not re.match(pattern, item):
                        errors.append(
                            f"Field '{field}'[{i}] ('{item}') does not match required pattern: {pattern}"
                        )
    
    return errors


def validate_skill_frontmatter(file_path: str) -> Tuple[bool, List[str]]:
    """
    Validate SKILL.md frontmatter against schema.
    
    Args:
        file_path: Path to SKILL.md file
    
    Returns:
        Tuple of (is_valid, errors_list)
    """
    errors = []
    
    # Read file
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        errors.append(f"File not found: {file_path}")
        return False, errors
    except Exception as e:
        errors.append(f"Error reading file: {str(e)}")
        return False, errors
    
    # Extract frontmatter
    frontmatter, extract_errors = extract_frontmatter(content)
    errors.extend(extract_errors)
    
    if not frontmatter:
        return False, errors
    
    # Validate
    errors.extend(validate_required_fields(frontmatter))
    errors.extend(validate_field_types(frontmatter))
    errors.extend(validate_field_rules(frontmatter))
    
    return len(errors) == 0, errors


def main():
    """CLI entry point."""
    if len(sys.argv) < 2:
        print("Usage: yaml_validator.py <path-to-SKILL.md>", file=sys.stderr)
        sys.exit(1)
    
    file_path = sys.argv[1]
    is_valid, errors = validate_skill_frontmatter(file_path)
    
    if is_valid:
        print(f"✓ VALID: {file_path}")
        sys.exit(0)
    else:
        print(f"✗ INVALID: {file_path}", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
