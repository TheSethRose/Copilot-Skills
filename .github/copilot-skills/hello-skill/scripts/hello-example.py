#!/usr/bin/env python3
"""
Hello Skill Example Script

Generates a personalized greeting message demonstrating bundled script patterns
for the Copilot Skills Architecture.

Usage:
    python hello-example.py --name "Alice"
    python hello-example.py --name "Bob" --format text
    python hello-example.py --name "Charlie" --timestamp

Arguments:
    --name (required): The name to greet
    --format (optional, default "json"): Output format (json or text)
    --timestamp (optional): Include timestamp in output

Output Format (JSON):
    {
        "success": true,
        "message": "Hello, {name}!",
        "data": {
            "greeting": "Hello, {name}!",
            "formatted_at": "2025-10-18T10:30:00Z"
        },
        "error": null
    }

Output Format (text):
    Hello, {name}!

Exit Codes:
    0: Success
    1: Argument or processing error
"""

import json
import argparse
import sys
from datetime import datetime


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Generate personalized greeting message"
    )
    parser.add_argument("--name", required=True, help="Name to greet")
    parser.add_argument(
        "--format",
        choices=["json", "text"],
        default="json",
        help="Output format (default: json)",
    )
    parser.add_argument(
        "--timestamp",
        action="store_true",
        help="Include ISO 8601 timestamp in output",
    )

    args = parser.parse_args()

    try:
        # Process the greeting
        result = create_greeting(args.name, args.timestamp)

        # Output in requested format
        if args.format == "json":
            output = {
                "success": True,
                "message": f"Hello, {args.name}!",
                "data": result,
                "error": None,
            }
            print(json.dumps(output, indent=2))
        else:  # text format
            print(f"Hello, {args.name}!")
            if args.timestamp:
                print(f"Generated at: {result['formatted_at']}")

        return 0

    except Exception as e:
        error_output = {
            "success": False,
            "message": f"Error greeting {args.name}",
            "data": None,
            "error": str(e),
        }

        if args.format == "json":
            print(json.dumps(error_output, indent=2), file=sys.stderr)
        else:
            print(f"Error: {e}", file=sys.stderr)

        return 1


def create_greeting(name, include_timestamp=False):
    """
    Create greeting message object.

    Args:
        name: Name to greet
        include_timestamp: Whether to include timestamp

    Returns:
        Dictionary with greeting information

    Raises:
        ValueError: If name is empty or invalid
    """
    if not name or not isinstance(name, str):
        raise ValueError("Name must be a non-empty string")

    if len(name.strip()) == 0:
        raise ValueError("Name cannot be only whitespace")

    result = {"greeting": f"Hello, {name}!"}

    if include_timestamp:
        result["formatted_at"] = datetime.utcnow().isoformat() + "Z"

    return result


if __name__ == "__main__":
    sys.exit(main())
