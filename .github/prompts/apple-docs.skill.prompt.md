---
name: "Apple Docs"
description: "Access Apple's Swift, SwiftUI, and iOS documentation via JSON API"
version: "1.0.0"
tags: ["swift", "swiftui", "apple", "ios", "macos", "documentation"]
dependencies: ["jq", "curl"]
---

# Apple Docs

**Purpose**: Access Apple's official documentation for Swift, SwiftUI, and iOS frameworks using their JSON API.

## When to Use This Skill

Use this skill when:
- Looking up Swift language features
- Finding SwiftUI component documentation
- Researching iOS/macOS APIs
- Checking symbol definitions
- Exploring Apple framework capabilities

**Keywords**: swift, swiftui, apple, ios, macos, documentation, symbol, framework

## Quick Start

### 1. List Available Frameworks

```bash
bash .github/copilot-skills/apple-docs/scripts/list-frameworks.sh
```

### 2. Search Within a Framework

```bash
# Search Swift documentation
bash .github/copilot-skills/apple-docs/scripts/search-framework.sh swift "async await"

# Search SwiftUI documentation
bash .github/copilot-skills/apple-docs/scripts/search-framework.sh swiftui "button"
```

### 3. Get Symbol Documentation

```bash
# Get specific symbol docs
bash .github/copilot-skills/apple-docs/scripts/get-symbol.sh swift/array

# Get SwiftUI component docs
bash .github/copilot-skills/apple-docs/scripts/get-symbol.sh swiftui/button
```

## Available Scripts

### `list-frameworks.sh`
Lists all available Apple frameworks from the technologies catalog.

**Usage:**
```bash
bash .github/copilot-skills/apple-docs/scripts/list-frameworks.sh [options]
```

**Options:**
- `--json` - Output raw JSON
- `--help` - Show help message

**Output:** List of frameworks with titles and identifiers

---

### `search-framework.sh`
Search for symbols within a specific framework.

**Usage:**
```bash
bash .github/copilot-skills/apple-docs/scripts/search-framework.sh <framework> <query> [options]
```

**Arguments:**
- `<framework>` - Framework name (e.g., "swift", "swiftui")
- `<query>` - Search query

**Options:**
- `--json` - Output raw JSON
- `--limit N` - Maximum results (default: 10)
- `--help` - Show help message

**Output:** Matching symbols with titles, descriptions, and paths

---

### `get-symbol.sh`
Get detailed documentation for a specific symbol.

**Usage:**
```bash
bash .github/copilot-skills/apple-docs/scripts/get-symbol.sh <path> [options]
```

**Arguments:**
- `<path>` - Symbol path (e.g., "swift/array", "swiftui/button")

**Options:**
- `--json` - Output raw JSON
- `--help` - Show help message

**Output:** Symbol documentation including description, platforms, and usage

## Common Workflows

### Find SwiftUI Components

```bash
# List all SwiftUI views
bash .github/copilot-skills/apple-docs/scripts/search-framework.sh swiftui "view"

# Find layout containers
bash .github/copilot-skills/apple-docs/scripts/search-framework.sh swiftui "stack"
```

### Research Swift Language Features

```bash
# Find async/await documentation
bash .github/copilot-skills/apple-docs/scripts/search-framework.sh swift "async"

# Look up collections
bash .github/copilot-skills/apple-docs/scripts/search-framework.sh swift "array"
```

### Get Detailed Symbol Docs

```bash
# Get Button component documentation
bash .github/copilot-skills/apple-docs/scripts/get-symbol.sh swiftui/button

# Get Array documentation
bash .github/copilot-skills/apple-docs/scripts/get-symbol.sh swift/array
```

## API Endpoints

Scripts use Apple's official JSON API:
- **Base URL**: `https://developer.apple.com/tutorials/data/`
- **Technologies**: `documentation/technologies.json`
- **Framework**: `documentation/{framework}.json`
- **Symbol**: `documentation/{framework}/{symbol}.json`

## Output Format

All scripts output structured data to terminal:
- Human-readable format by default
- `--json` flag for raw JSON
- Exit codes: 0 (success), 1 (error)

## Error Handling

Scripts handle common errors:
- Network failures
- Invalid framework names
- Missing symbols
- API rate limiting

## Best Practices

**✅ Do:**
- Use specific framework names (swift, swiftui)
- Search with clear, focused queries
- Check exit codes in scripts
- Use `--json` for programmatic parsing

**❌ Don't:**
- Make rapid API calls (rate limiting)
- Assume symbols exist without checking
- Use this for non-Apple documentation

## Examples

### Example 1: Find All Button Types in SwiftUI

```bash
bash .github/copilot-skills/apple-docs/scripts/search-framework.sh swiftui "button" --limit 20
```

### Example 2: Get Swift Concurrency Documentation

```bash
bash .github/copilot-skills/apple-docs/scripts/get-symbol.sh swift/task
bash .github/copilot-skills/apple-docs/scripts/get-symbol.sh swift/actor
```

### Example 3: Explore Layout Options

```bash
bash .github/copilot-skills/apple-docs/scripts/search-framework.sh swiftui "layout"
bash .github/copilot-skills/apple-docs/scripts/search-framework.sh swiftui "geometry"
```

## Troubleshooting

### Network Errors
```bash
# Check connection
curl -I https://developer.apple.com/tutorials/data/documentation/technologies.json

# Retry with delay
sleep 2 && bash .github/copilot-skills/apple-docs/scripts/list-frameworks.sh
```

### No Results Found
- Try broader search terms
- Check framework name spelling
- Verify symbol path format

### Rate Limiting
- Add delays between requests
- Cache results locally
- Use `--json` for efficient parsing

## Related Skills

- `/swift` - Swift language patterns (if available)
- `/ios` - iOS development workflows (if available)
- `/create-skill` - Create new Apple framework skills

## More Information

- **Scripts**: `.github/copilot-skills/apple-docs/scripts/`
- **Apple Developer**: https://developer.apple.com/documentation/
- **API Source**: Reverse-engineered from apple-doc-mcp project
