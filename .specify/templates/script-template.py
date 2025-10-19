#!/usr/bin/env python3
"""
[Script Name]

[One paragraph describing what this script does]

Usage:
    python {script-name}.py --arg1 "value" --arg2 "value" --format json

Arguments:
    --arg1 (required): [Description of what arg1 does]
    --arg2 (optional, default "default_value"): [Description of what arg2 does]

Flags:
    --format (optional, default "json"): Output format (json or text)
    --verbose (optional): Enable verbose logging

Output Format (JSON):
    {
        "success": true|false,
        "data": <result_object>,
        "error": null|<error_string>
    }

Output Format (text):
    [Human-readable result]

Exit Codes:
    0: Success
    1: Argument validation error
    2: Processing error

Error Handling:
    - Missing required argument: Exit code 1, clear error message
    - Invalid argument value: Exit code 1, suggest valid values
    - Processing failure: Exit code 2, provide debugging info
"""

import json
import argparse
import sys
import logging


def setup_logging(verbose):
    """Configure logging based on verbosity level."""
    level = logging.DEBUG if verbose else logging.WARNING
    logging.basicConfig(
        level=level,
        format="%(levelname)s: %(message)s",
    )


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="[Script description for help text]"
    )
    
    # Required arguments
    parser.add_argument(
        "--arg1",
        required=True,
        help="[Description of arg1]"
    )
    
    # Optional arguments
    parser.add_argument(
        "--arg2",
        default="default_value",
        help="[Description of arg2 (default: default_value)]"
    )
    
    # Output format
    parser.add_argument(
        "--format",
        choices=["json", "text"],
        default="json",
        help="Output format (default: json)"
    )
    
    # Verbose flag
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )
    
    args = parser.parse_args()
    setup_logging(args.verbose)
    
    try:
        # Validate arguments
        logging.debug(f"Arguments: arg1={args.arg1}, arg2={args.arg2}")
        
        # Process
        result = process_input(args.arg1, args.arg2)
        
        # Output
        if args.format == "json":
            output = {
                "success": True,
                "data": result,
                "error": None
            }
            print(json.dumps(output, indent=2))
        else:  # text
            print(f"Result: {result}")
        
        return 0
    
    except ValueError as e:
        # Validation error
        error_output = {
            "success": False,
            "data": None,
            "error": str(e)
        }
        
        if args.format == "json":
            print(json.dumps(error_output, indent=2), file=sys.stderr)
        else:
            print(f"Error: {e}", file=sys.stderr)
        
        return 1
    
    except Exception as e:
        # Processing error
        error_output = {
            "success": False,
            "data": None,
            "error": f"Processing failed: {str(e)}"
        }
        
        if args.format == "json":
            print(json.dumps(error_output, indent=2), file=sys.stderr)
        else:
            print(f"Fatal error: {e}", file=sys.stderr)
        
        logging.exception("Unexpected error during processing")
        return 2


def process_input(arg1, arg2):
    """
    Process the input arguments.
    
    Args:
        arg1: [Description of arg1 parameter]
        arg2: [Description of arg2 parameter]
    
    Returns:
        Processed result object
    
    Raises:
        ValueError: If arguments are invalid
        Exception: If processing fails
    """
    # Validate inputs
    if not arg1 or not isinstance(arg1, str):
        raise ValueError("arg1 must be a non-empty string")
    
    if len(arg1.strip()) == 0:
        raise ValueError("arg1 cannot be only whitespace")
    
    # Process
    result = {
        "arg1_processed": arg1.strip(),
        "arg2_value": arg2,
        "output": f"Processed {arg1} with {arg2}"
    }
    
    return result


if __name__ == "__main__":
    sys.exit(main())
