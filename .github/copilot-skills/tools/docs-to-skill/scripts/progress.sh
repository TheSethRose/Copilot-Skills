#!/bin/bash
# View scraping progress manifest

MANIFEST_FILE=".github/copilot-skills/docs-to-skill/manifest.json"

if [ ! -f "$MANIFEST_FILE" ]; then
    echo "❌ Manifest file not found: $MANIFEST_FILE"
    exit 1
fi

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║           📊 SKILL GENERATION PROGRESS TRACKER                 ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

python3 << 'PYTHON_EOF'
import json

with open('.github/copilot-skills/docs-to-skill/manifest.json', 'r') as f:
    manifest = json.load(f)['manifest']

summary = manifest['summary']
print(f"Status: {summary['completed']} ✅ | {summary['failed']} ❌ | {summary['pending']} ⏳")
print()

# Group by status
completed = [fw for fw in manifest['ui_components'] if fw['status'] == 'completed']
failed = [fw for fw in manifest['ui_components'] if fw['status'] == 'failed']
pending = [fw for fw in manifest['ui_components'] if fw['status'] == 'pending']

if completed:
    print("✅ COMPLETED:")
    for fw in completed:
        print(f"   • {fw['name']}")
    print()

if failed:
    print("❌ FAILED:")
    for fw in failed:
        error = fw['error'] if fw['error'] else 'Unknown error'
        print(f"   • {fw['name']}: {error}")
    print()

if pending:
    print("⏳ PENDING:")
    for fw in pending:
        print(f"   • {fw['name']}")
    print()

print(f"Progress: [{('█' * summary['completed'] + '░' * (summary['pending'] + summary['failed']))[:10]}] {summary['completed']}/{len(manifest['ui_components'])}")
PYTHON_EOF

echo ""
