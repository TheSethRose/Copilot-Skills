#!/bin/bash
# View scraping progress and status

PROGRESS_FILE=".github/copilot-skills/docs-to-skill/progress.json"

if [ ! -f "$PROGRESS_FILE" ]; then
    echo "❌ Progress file not found: $PROGRESS_FILE"
    exit 1
fi

python3 << PYTHON_EOF
import json
from datetime import datetime

with open("$PROGRESS_FILE", "r") as f:
    progress = json.load(f)

print("\n" + "="*80)
print("📊 COPILOT SKILLS SCRAPING PROGRESS")
print("="*80)

# Count statuses
statuses = {"pending": 0, "in-progress": 0, "success": 0, "failed": 0}
for fw in progress["frameworks"]:
    statuses[fw["status"]] = statuses.get(fw["status"], 0) + 1

print(f"\n✅ Success:     {statuses['success']:2d}/{progress['total_frameworks']}")
print(f"❌ Failed:      {statuses['failed']:2d}/{progress['total_frameworks']}")
print(f"⏳ In Progress: {statuses['in-progress']:2d}/{progress['total_frameworks']}")
print(f"⏹️  Pending:    {statuses['pending']:2d}/{progress['total_frameworks']}")

print("\n" + "-"*80)
print("Framework Status Details:")
print("-"*80)

for fw in progress["frameworks"]:
    status_icon = "✅" if fw["status"] == "success" else \
                  "❌" if fw["status"] == "failed" else \
                  "⏳" if fw["status"] == "in-progress" else "⏹️"
    
    print(f"\n{status_icon} {fw['name']:20s} | {fw['status']:12s}")
    
    if fw["last_attempt"]:
        print(f"   Last attempt: {fw['last_attempt']}")
    
    if fw["error"]:
        print(f"   Error: {fw['error']}")

print("\n" + "="*80 + "\n")
PYTHON_EOF
