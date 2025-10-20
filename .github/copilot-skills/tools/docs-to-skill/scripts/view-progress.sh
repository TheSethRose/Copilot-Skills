#!/bin/bash
# View scraping progress
# Usage: view-progress.sh [framework-name]
# If framework-name provided, show only that framework
# Otherwise, show all frameworks

FRAMEWORK="$1"

python3 << PYTHON
import json
import os
import sys

if not os.path.exists('.github/copilot-skills/docs-to-skill/progress.json'):
    print("❌ No progress file found")
    exit(1)

with open('.github/copilot-skills/docs-to-skill/progress.json', 'r') as f:
    data = json.load(f)

framework_arg = "$FRAMEWORK"

if framework_arg:
    # Show single framework
    fw = next((f for f in data['frameworks'] if f['name'] == framework_arg), None)
    if not fw:
        print(f"❌ Framework '{framework_arg}' not found")
        exit(1)
    
    icon = "✅" if fw['status'] == 'success' else "❌" if fw['status'] == 'failed' else "⏳"
    status = fw['status'].upper()
    print(f"\n{icon} {fw['name'].upper()}")
    print(f"   Status: {status}")
    print(f"   URL: {fw['url']}")
    if fw['error']:
        print(f"   Error: {fw['error']}")
    print()
else:
    # Show all frameworks
    print("\n📊 Scraping Progress Tracker")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    completed = sum(1 for fw in data['frameworks'] if fw['status'] == 'success')
    failed = sum(1 for fw in data['frameworks'] if fw['status'] == 'failed')
    pending = sum(1 for fw in data['frameworks'] if fw['status'] == 'pending')
    
    print(f"\nStatus: {completed} ✅  {failed} ❌  {pending} ⏳\n")
    
    for fw in data['frameworks']:
        icon = "✅" if fw['status'] == 'success' else "❌" if fw['status'] == 'failed' else "⏳"
        status_text = fw['status'].upper()
        print(f"  {icon} {fw['name']:<20} {status_text:<10}")
        if fw['error']:
            print(f"      Error: {fw['error']}")
    
    print("\n" + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print()

PYTHON
