# Apple Docs Skill

Access Apple's official Swift, SwiftUI, and iOS documentation via their JSON API.

## Overview

This skill provides terminal-based access to Apple's developer documentation without HTML scraping. It uses Apple's official JSON API endpoints to fetch framework information, search symbols, and retrieve detailed documentation.

## Architecture

**Type**: Domain Knowledge Skill  
**Scripts**: 3 bash scripts (terminal output only)  
**Dependencies**: curl, jq

### Files

```
.github/
├── prompts/apple-docs.skill.prompt.md         # Skill workflow
├── instructions/apple-docs.instructions.md     # Auto-loaded context
└── copilot-skills/apple-docs/
    ├── README.md                               # This file
    └── scripts/
        ├── list-frameworks.sh                  # List all frameworks
        ├── search-framework.sh                 # Search within framework
        └── get-symbol.sh                       # Get symbol documentation
```

## Constitutional Compliance

### ✅ 1. Progressive Disclosure
- **Metadata**: YAML frontmatter in prompt
- **Core**: Quick start + 3 scripts
- **Details**: Optional README + API reference

### ✅ 2. File-Based Organization
- Prompt: `.github/prompts/apple-docs.skill.prompt.md`
- Instructions: `.github/instructions/apple-docs.instructions.md`
- Scripts: `.github/copilot-skills/apple-docs/scripts/`

### ✅ 3. Dynamic Discovery
- **Keywords**: swift, swiftui, apple, ios, macos, documentation
- **File Patterns**: `**/*.swift`, `**/*.swiftui`, `**/Package.swift`
- **Routing Map**: Registered in copilot-instructions.md

### ✅ 4. Deterministic Execution
- All scripts output to terminal only
- Consistent JSON structure with `--json` flag
- Exit codes: 0 (success), 1 (error)
- Error messages to stderr

### ✅ 5. Composability
- **Clear Scope**: Apple documentation only
- **Dependencies**: curl, jq (system tools)
- **No Overlaps**: Distinct from web scraping skills
- **Explicit**: Scripts don't generate files

## API Endpoints

Scripts use Apple's official JSON API:

```
Base: https://developer.apple.com/tutorials/data/

Endpoints:
- documentation/technologies.json          # All frameworks
- documentation/{framework}.json           # Framework data
- documentation/{framework}/{symbol}.json  # Symbol details
```

## Script Details

### 1. list-frameworks.sh

Lists all available Apple frameworks.

**Usage:**
```bash
bash .github/copilot-skills/apple-docs/scripts/list-frameworks.sh [--json]
```

**Output:**
```
=== Available Apple Frameworks ===

• Foundation (doc://com.apple.documentation/documentation/foundation)
• Swift (doc://com.apple.documentation/documentation/swift)
• SwiftUI (doc://com.apple.documentation/documentation/swiftui)
• UIKit (doc://com.apple.documentation/documentation/uikit)
...

Total: 200+ frameworks
```

### 2. search-framework.sh

Search for symbols within a specific framework.

**Usage:**
```bash
bash .github/copilot-skills/apple-docs/scripts/search-framework.sh <framework> <query> [--limit N]
```

**Examples:**
```bash
# Find buttons in SwiftUI
bash .github/copilot-skills/apple-docs/scripts/search-framework.sh swiftui "button"

# Search Swift arrays
bash .github/copilot-skills/apple-docs/scripts/search-framework.sh swift "array" --limit 20
```

**Output:**
```
=== Search Results: swiftui / button ===

• Button
  Path: documentation/swiftui/button
  Kind: struct

• ButtonStyle
  Path: documentation/swiftui/buttonstyle
  Kind: protocol

Found: 2 results (limit: 10)
```

### 3. get-symbol.sh

Get detailed documentation for a specific symbol.

**Usage:**
```bash
bash .github/copilot-skills/apple-docs/scripts/get-symbol.sh <path> [--json]
```

**Examples:**
```bash
# Get Button docs
bash .github/copilot-skills/apple-docs/scripts/get-symbol.sh swiftui/button

# Get Array docs
bash .github/copilot-skills/apple-docs/scripts/get-symbol.sh swift/array
```

**Output:**
```
=== Symbol Documentation: swiftui/button ===

Title: Button
Kind: struct

Platforms:
  • iOS 13.0
  • macOS 10.15
  • tvOS 13.0
  • watchOS 6.0

Description:
  A control that initiates an action.

Topics:
  • Creating a Button
  • Styling a Button
  • Managing Button State

Documentation URL:
  https://developer.apple.com/documentation/swiftui/button
```

## Testing

Test each script:

```bash
# Test list
bash .github/copilot-skills/apple-docs/scripts/list-frameworks.sh

# Test search
bash .github/copilot-skills/apple-docs/scripts/search-framework.sh swift "array"

# Test symbol
bash .github/copilot-skills/apple-docs/scripts/get-symbol.sh swiftui/button

# Test JSON output
bash .github/copilot-skills/apple-docs/scripts/get-symbol.sh swift/task --json | jq .
```

## Integration

### Keyword Routing Map

Add to `.github/copilot-instructions.md`:

```markdown
#### Swift / SwiftUI / Apple Documentation
**Keywords:** swift, swiftui, apple, ios, macos, documentation, symbol, framework, api
**Suggest:** `/apple-docs`
**Auto-context:** `.github/instructions/apple-docs.instructions.md` (when editing **/*.swift, **/*.swiftui, **/Package.swift)
**Skill:** `.github/copilot-skills/apple-docs/README.md`
```

### Usage in Chat

```
User: "How do I use SwiftUI buttons?"
AI: Let me look that up using the apple-docs skill...
    [runs: bash .github/copilot-skills/apple-docs/scripts/get-symbol.sh swiftui/button]
    [parses output and provides answer with documentation link]
```

## Maintenance

### Dependencies

Ensure these are installed:
```bash
# Check curl (usually pre-installed)
which curl

# Install jq if missing
brew install jq
```

### API Changes

If Apple changes their API:
1. Check `https://developer.apple.com/tutorials/data/` availability
2. Update endpoint URLs in scripts
3. Test all three scripts
4. Update documentation

### Rate Limiting

Apple's API has rate limiting. If you encounter errors:
- Add delays between requests (`sleep 1`)
- Cache results locally
- Use `--json` for efficient parsing

## Troubleshooting

### "jq: command not found"
```bash
brew install jq
```

### "Failed to fetch framework"
- Check internet connection
- Verify framework name (lowercase)
- Try with `curl` directly: `curl https://developer.apple.com/tutorials/data/documentation/swift.json`

### "No results found"
- Try broader search terms
- Check framework spelling
- Use `list-frameworks.sh` to see available options

## Going Deeper: Web Search + API Reference

This skill is **perfect for quick API reference**, but Apple's documentation ecosystem is vast.

### When to Combine Web Search

**This Skill Best For:**
- ✅ Quick symbol documentation
- ✅ API signatures and availability
- ✅ Platform compatibility
- ✅ Related methods and properties

**Web Search Best For:**
- 🔍 Tutorials and guides
- 🔍 Design patterns and best practices
- 🔍 Real-world code examples
- 🔍 Release notes and what's new
- 🔍 Performance optimization

### Recommended Web Resources

```markdown
**Official Sources:**
- Swift.org Blog: https://www.swift.org/blog/
- WWDC Videos: https://developer.apple.com/videos/
- Apple Developer News: https://developer.apple.com/news/
- Apple Sample Code: https://developer.apple.com/sample-code/

**Community:**
- GitHub: Real-world implementations
- Stack Overflow: Common patterns and solutions
- Swift Forums: https://forums.swift.org/
- Reddit: r/swift, r/swiftui

**Learning:**
- Hacking with Swift: https://www.hackingwithswift.com/
- Swift Playgrounds: Built-in learning app
```

### Example: Complete Workflow

**Goal:** Build a custom button in SwiftUI

**Step 1: Get API Reference** (This Skill)
```bash
bash .github/copilot-skills/apple-docs/scripts/get-symbol.sh swiftui/button
bash .github/copilot-skills/apple-docs/scripts/search-framework.sh swiftui "buttonstyle" --limit 5
```

**Step 2: Learn Best Practices** (Web Search)
```
Search: "SwiftUI custom button best practices"
- Tutorials on button styling
- ButtonStyle protocol usage
- Accessibility guidelines
```

**Step 3: Find Examples** (GitHub)
```
Search: "swiftui custom button example"
- Real project implementations
- Design patterns
- Production code
```

**Step 4: Verify Details** (Back to This Skill)
```bash
bash .github/copilot-skills/apple-docs/scripts/get-symbol.sh swiftui/buttonstyle
```

## Credits

API endpoints reverse-engineered from:
- [apple-doc-mcp](https://github.com/MightyDillah/apple-doc-mcp) by MightyDillah
- Apple Developer Documentation structure

## License

MIT License - Scripts are original implementations using public API endpoints.
