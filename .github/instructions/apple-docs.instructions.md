# Apple Docs - Auto-Loaded Instructions

**Auto-loads for:** `**/*.swift`, `**/*.swiftui`, `**/Package.swift`

## Default Behaviors

When working in Swift files, this skill provides:
- Quick access to Apple's official API documentation
- Symbol lookup for Swift/SwiftUI components
- Framework exploration capabilities

## Common Patterns

### Looking Up Swift Symbols

When you see unfamiliar Swift code:
```swift
let task = Task { ... }
```

Use: `bash .github/copilot-skills/documentation/apple-docs/scripts/get-symbol.sh swift/task`

### Finding SwiftUI Components

When building UI:
```swift
Button("Press Me") { ... }
```

Use: `bash .github/copilot-skills/documentation/apple-docs/scripts/get-symbol.sh swiftui/button`

### Exploring Frameworks

When starting a new feature, explore available APIs:
```bash
bash .github/copilot-skills/documentation/apple-docs/scripts/search-framework.sh swiftui "navigation"
```

## Quality Guidelines

### Code Style
- Follow Swift naming conventions (PascalCase for types, camelCase for variables)
- Use descriptive names that match Apple's API patterns
- Leverage type inference where appropriate

### SwiftUI Patterns
- Use declarative view composition
- Prefer built-in modifiers over custom solutions
- Check documentation for availability across platforms

### Documentation References
- Always check symbol availability for target platforms
- Reference Apple docs when using advanced APIs
- Link to specific symbols in code comments when helpful

## Workflow Integration

### During Development
1. Encounter unfamiliar API
2. Run `get-symbol.sh` to fetch docs
3. Review usage and examples
4. Implement correctly

### Code Review
1. Question API usage
2. Verify with `search-framework.sh`
3. Check platform availability
4. Suggest alternatives if needed

## Best Practices

**✅ Do:**
- Use scripts to verify API availability
- Check documentation before Stack Overflow
- Search frameworks before creating custom solutions
- Cache frequently used documentation locally

**❌ Don't:**
- Assume API availability across all platforms
- Skip checking documentation for unfamiliar symbols
- Implement custom solutions for built-in functionality
- Make rapid API requests without caching

## Common Use Cases

### Case 1: Implementing New Feature
```bash
# Find relevant SwiftUI components
bash .github/copilot-skills/documentation/apple-docs/scripts/search-framework.sh swiftui "picker"

# Get detailed docs
bash .github/copilot-skills/documentation/apple-docs/scripts/get-symbol.sh swiftui/picker
```

### Case 2: Debugging Swift Code
```bash
# Look up Swift collection methods
bash .github/copilot-skills/documentation/apple-docs/scripts/search-framework.sh swift "array"

# Check specific method
bash .github/copilot-skills/documentation/apple-docs/scripts/get-symbol.sh swift/array/map
```

### Case 3: Platform-Specific Code
```bash
# Search for availability info
bash .github/copilot-skills/documentation/apple-docs/scripts/get-symbol.sh swiftui/button --json | jq '.metadata.platforms'
```

## Error Messages

### "Framework not found"
- Verify framework name is correct (lowercase)
- Check `list-frameworks.sh` for available options
- Try alternative framework names

### "Symbol not found"
- Check symbol path format: `framework/symbol`
- Use search to find correct path
- Verify symbol exists in that framework

### "Network error"
- Check internet connection
- Wait and retry (rate limiting)
- Use cached results if available

## Going Deeper: Combining with Web Search

This skill provides **official API documentation**. For richer learning:

### When to Search the Web
- Learning new language features
- Understanding design patterns
- Finding real-world examples
- Reading release notes
- Watching tutorials

### Recommended Web Resources
- **Swift.org**: https://www.swift.org/blog/
- **WWDC Videos**: https://developer.apple.com/videos/
- **Apple Developer News**: https://developer.apple.com/news/
- **GitHub**: Search for example implementations
- **Stack Overflow**: Common patterns and solutions

### Combined Workflow
```bash
# Step 1: Get official docs
bash .github/copilot-skills/documentation/apple-docs/scripts/get-symbol.sh swiftui/button

# Step 2: If you need more context, search the web for:
#   - "SwiftUI Button tutorial"
#   - "SwiftUI Button best practices"
#   - "SwiftUI Button examples"

# Step 3: Find implementation examples on GitHub
#   - Search: "swiftui button example"
```

## Related Workflows

- **API Design**: Reference Apple patterns when designing interfaces
- **Code Review**: Verify API usage against documentation
- **Learning**: Explore frameworks to discover new capabilities
- **Debugging**: Look up error-prone APIs for correct usage
