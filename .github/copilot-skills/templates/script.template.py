#!/usr/bin/env python3
"""
{{SCRIPT_NAME}} - {{SCRIPT_DESCRIPTION}}

Part of the {{SKILL_NAME}} skill.

Usage:
    {{SCRIPT_NAME}}.py {{USAGE_ARGS}}

Examples:
    {{EXAMPLE_1}}
    {{EXAMPLE_2}}
"""

import sys
import argparse
from pathlib import Path
from typing import Optional, List


def main(args: List[str]) -> int:
    """
    Main entry point for the script.
    
    Args:
        args: Command line arguments
    
    Returns:
        Exit code (0 for success, non-zero for error)
    """
    parser = argparse.ArgumentParser(
        description="{{SCRIPT_DESCRIPTION}}",
        epilog="Part of the {{SKILL_NAME}} skill"
    )
    
    # Add arguments
    parser.add_argument(
        "{{ARG_NAME}}",
        help="{{ARG_DESCRIPTION}}"
    )
    parser.add_argument(
        "--option",
        "-o",
        help="Optional parameter",
        default=None
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose output"
    )
    
    parsed_args = parser.parse_args(args)
    
    try:
        # Main logic here
        {{MAIN_LOGIC}}
        
        if parsed_args.verbose:
            print(f"✓ Success: {{SUCCESS_MESSAGE}}", file=sys.stderr)
        
        return 0
        
    except Exception as e:
        print(f"✗ Error: {str(e)}", file=sys.stderr)
        if parsed_args.verbose:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
