#!/usr/bin/env python3
"""
Example Python script demonstrating bundled script patterns.

Usage:
    python example-script.py --input "value" --format json

Arguments:
    --input: The input data to process
    --format: Output format ('json' or 'text', default: 'json')

Output:
    JSON with structure: {"success": bool, "data": any, "error": str|null}
"""

import json
import argparse
import sys


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Example script demonstrating bundled patterns"
    )
    parser.add_argument("--input", required=True, help="Input value to process")
    parser.add_argument(
        "--format",
        choices=["json", "text"],
        default="json",
        help="Output format (default: json)",
    )

    args = parser.parse_args()

    try:
        # Example processing
        result = process_input(args.input)

        # Output in requested format
        output = {"success": True, "data": result, "error": None}

        if args.format == "json":
            print(json.dumps(output, indent=2))
        else:
            print(f"Success! Result: {result}")

        return 0

    except Exception as e:
        error_output = {"success": False, "data": None, "error": str(e)}

        if args.format == "json":
            print(json.dumps(error_output, indent=2), file=sys.stderr)
        else:
            print(f"Error: {e}", file=sys.stderr)

        return 1


def process_input(value: str) -> str:
    """Process the input value."""
    # Example: just return uppercase version
    return value.upper()


if __name__ == "__main__":
    sys.exit(main())
