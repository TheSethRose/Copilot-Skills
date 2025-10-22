# Context7 Skill

Access up-to-date documentation for 48,148+ libraries using Context7's MCP server.

## 🎯 What You Can Do

✅ Learn any library quickly with current docs  
✅ Compare multiple libraries before choosing  
✅ Fix bugs from breaking API changes  
✅ Update skills with fresh documentation  
✅ Never rely on outdated training data again  

---

## Overview

Context7 is an open-source documentation service that provides **always-current** library documentation through an MCP (Model Context Protocol) server. Instead of relying on potentially outdated training data, Context7 fetches fresh documentation directly from source repositories.

**Package**: `@upstash/context7-mcp`  
**Repository**: https://github.com/upstash/context7  
**License**: Open Source  
**Libraries**: 48,148+ and counting

## Quick Start

### 1. Install MCP Server

Add to your MCP configuration file (e.g., `mcp.json` for VS Code):

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

### 2. Start Using in Copilot Chat

**That's it!** Just ask natural questions:

```
"Show me how to use React hooks for state management"
→ Copilot auto-fetches current React docs

"Compare FastAPI vs Django for building APIs"
→ Copilot fetches current docs for both

"Get Prisma documentation about relationships"
→ Copilot fetches latest Prisma docs
```

## How It Works

## 🔧 MCP Tools Documentation

Context7 provides exactly **2 tools**:

### Tool 1: `resolve-library-id`

**What it does**: Find the exact Context7 library ID for any library name

**Parameters**:
```typescript
libraryName: string  // What you're looking for
                     // Examples: "react", "next.js", "fastapi", "prisma"
```

**Returns**:
```typescript
{
  libraryId: string,      // e.g., "/facebook/react"
  name: string,           // Display name
  description: string,    // What the library does
  trustScore: number,     // 0-10 reliability (7+ = good)
  codeSnippets: number,   // How many examples available
  versions?: string[]     // Available versions if any
}
```

**How Copilot Uses It**:
```
YOU: "Get React documentation"
        ↓
COPILOT CALLS: resolve-library-id("react")
        ↓
COPILOT GETS: {
  libraryId: "/facebook/react",
  trustScore: 9.5,
  codeSnippets: 637000,
  versions: ["v18.2.0", "v17.0.2", ...]
}
        ↓
COPILOT USES: /facebook/react for next tool call
```

---

### Tool 2: `get-library-docs`

**What it does**: Fetch current documentation for a specific library

**Parameters**:
```typescript
context7CompatibleLibraryID: string  // From resolve-library-id
                                      // Examples: "/facebook/react"
                                      //           "/vercel/next.js"
                                      //           "/openai/openai-python/v1_68_0"

topic?: string                        // What you want to know (optional)
                                      // Examples: "hooks", "routing", "authentication"
                                      // Be specific for best results

tokens?: number                       // How much documentation (optional)
                                      // Default: 5000
                                      // Min: 1000, Max: 15000
```

**Returns**:
```typescript
string  // Formatted documentation text with code examples
```

**How Copilot Uses It**:
```
YOU: "Get React documentation about hooks"
        ↓
COPILOT CALLS: resolve-library-id("react")
               → Gets: /facebook/react
        ↓
COPILOT CALLS: get-library-docs(
  "/facebook/react",
  "hooks useState useEffect",  // Be specific!
  5000                         // Default is fine
)
        ↓
COPILOT GETS: [Current React hooks documentation with examples]
        ↓
COPILOT SHOWS YOU: The docs with explanations
```

---

### Your Workflow

```
You ask a question
    ↓
Copilot uses resolve-library-id("library name")
    ↓
Copilot uses get-library-docs(libraryId, topic, tokens)
    ↓
You get accurate, up-to-date information
```

### Key Points

**✅ DO:**
- Be specific with topics: "JWT authentication middleware" not "auth"
- Check trustScore (7-10 = reliable)
- Use default 5000 tokens (usually enough)

**❌ DON'T:**
- Use vague library names: "react auth" not helpful, use "react"
- Request excessive tokens (15000 wastes resources)
- Skip the resolve step (IDs must be exact format)

## Real-World Examples

### Example: Learning a New Framework

```
YOU: "I need to learn SvelteKit. Show me routing and data loading"

COPILOT:
1. Resolves "sveltekit" → /sveltejs/kit (Trust: 9.1)
2. Fetches docs about routing and data loading
3. Shows you current best practices with examples

RESULT: You learn current SvelteKit patterns (not outdated ones)
```

### Example: Fixing Breaking Changes

```
YOU: "My OpenAI code broke. I'm using v5. Show me chat completions"

COPILOT:
1. Resolves "openai" (you mention v5)
2. Gets /openai/openai-python docs for v5
3. Shows what changed from v4

RESULT: You see exactly what to fix for v5
```

### Example: Making a Technology Decision

```
YOU: "Should I use Prisma or Drizzle for my Next.js app?
Show me type safety, migrations, and ease of use"

COPILOT:
1. Resolves both libraries
2. Fetches docs for both
3. Compares current APIs and features

RESULT: You make informed decision based on current facts
```

### Example: Understanding Anthropic's Claude API

```
YOU: "Get Anthropic Claude documentation about models and vision capabilities"

COPILOT:
1. Resolves "anthropic" or "claude"
2. Fetches current Anthropic SDK docs
3. Shows available models (Claude 3.5, etc.)
4. Explains vision API, streaming, batch processing

RESULT: You understand current Claude capabilities with examples
```

**Or more specific:**
```
YOU: "Get Anthropic Claude documentation about streaming responses 
and token counting for cost optimization"

COPILOT:
1. Fetches Anthropic docs focused on streaming and tokens
2. Shows current implementation patterns
3. Provides cost estimation examples

RESULT: You know exactly how to build efficient Claude applications
```

---

## What This Skill Does

✅ **Resolves library names** to Context7-compatible IDs  
✅ **Fetches current documentation** with code examples  
✅ **Supports 48K+ libraries** across all languages  
✅ **Provides trust scores** for reliability assessment  
✅ **Enables skill enhancement** by updating with latest docs  

## Core Workflows

### Workflow 1: Learn New Library

**Time**: 2-3 minutes

```
Ask Copilot:
"Get [Library] documentation about [specific topic]"

Examples:
- "Get FastAPI docs on request validation"
- "Show me Django ORM relationships"
- "Latest React 18 features"
```

### Workflow 2: Update Existing Skill

**Time**: 15-30 minutes per skill

```
1. Find outdated content in skill files
2. Ask Copilot: "Get [Library] documentation about [topic]"
3. Update patterns.md and reference.md
4. Test examples
5. Commit: "chore: update with Context7 docs"
```

### Workflow 3: Compare Libraries

**Problem**: Choosing between similar libraries

**Solution**:
1. Resolve all candidates
2. Compare trust scores and snippet counts
3. Fetch focused docs for top 2-3
4. Evaluate API patterns
5. Make informed decision

**Time**: 10-15 minutes

---

### Workflow 4: Troubleshoot Breakage

**Problem**: Code worked last month, now fails

**Solution**:
1. Get current docs for the library
2. Compare with your implementation
3. Identify deprecated parameters/methods
4. Update code to current API
5. Test and verify

**Time**: 5-10 minutes

## MCP Tools

### resolve-library-id

**Purpose**: Find Context7-compatible library IDs

**Parameters**:
- `libraryName` (string) - Library to search for

**Returns**:
- Library ID (e.g., `/vercel/next.js`)
- Trust score (0-10)
- Code snippet count
- Description
- Available versions

**Example**:
```typescript
resolve-library-id("react-query")
// Returns: /tanstack/query with trust score 9.3
```

---

### get-library-docs

**Purpose**: Retrieve focused documentation

**Parameters**:
- `context7CompatibleLibraryID` (string, required)
- `topic` (string, optional) - Focus area
- `tokens` (number, optional, default: 5000) - Max tokens

**Returns**: Formatted documentation with code examples

**Example**:
```typescript
get-library-docs(
  "/vercel/next.js",
  "middleware for authentication",
  5000
)
```

## Key Features

### Trust Scores

Context7 provides 0-10 trust scores for each library:

| Score | Meaning | Action |
|-------|---------|--------|
| 9-10 | Official, well-maintained | Use confidently |
| 7-8 | Reliable | Good choice |
| 5-6 | Moderate | Verify examples |
| 3-4 | Low quality | Use caution |
| 0-2 | Unreliable | Avoid |

### Code Snippet Coverage

Higher snippet counts indicate better documentation:

- **100K+**: Exceptional (e.g., OpenAI: 382K)
- **10K-100K**: Excellent (e.g., MongoDB: 131K)
- **1K-10K**: Very good
- **100-1K**: Good
- **<100**: Limited

### Version Support

Get docs for specific library versions:

```typescript
// Latest version
"/openai/openai-node"

// Specific version
"/openai/openai-node/v5_19_1"
```

## Best Practices

### ✅ Do

- **Always resolve first** - Get proper library ID before fetching docs
- **Check trust scores** - Prefer 7-10 for reliability
- **Be specific with topics** - "authentication with JWT" not "auth"
- **Cache frequently used docs** - Reduce API calls
- **Note Context7 as source** - When updating skills
- **Test updated examples** - Verify they work

### ❌ Don't

- **Skip resolve step** - IDs must be exact
- **Use vague topics** - "everything" wastes tokens
- **Ignore low trust scores** - <5 may be unreliable
- **Request excessive tokens** - Start with 5000, increase if needed
- **Forget version compatibility** - Check which version docs are from

## Common Use Cases

### Learning New Framework

```bash
# Example: Learning SvelteKit
1. resolve-library-id "sveltekit"
   → /sveltejs/kit (Trust: 9.1)

2. get-library-docs "/sveltejs/kit" "routing and layouts" 5000
   → Get core routing concepts

3. get-library-docs "/sveltejs/kit" "data loading" 5000
   → Get data fetching patterns

4. Start building with current knowledge
```

### API Migration

```bash
# Example: Migrating to new OpenAI API
1. resolve-library-id "openai python"
   → /openai/openai-python/v1_68_0

2. get-library-docs (id) "chat completions migration" 8000
   → Get migration guide

3. Compare old vs new patterns
4. Update codebase systematically
```

### Skill Maintenance

```bash
# Example: Updating React skill
1. Read current skill: .github/copilot-skills/react/patterns.md
2. Identify outdated hooks/patterns
3. resolve-library-id "react"
4. get-library-docs "/facebook/react" "hooks best practices" 10000
5. Update patterns.md with current examples
6. Add note: "Updated with Context7 docs (Oct 2024)"
7. Test examples
```

## Integration Patterns

### Pattern: Enhance Existing Skill

```markdown
## Skill Enhancement Checklist

- [ ] Identify which libraries skill covers
- [ ] Resolve each library via Context7
- [ ] Fetch current documentation for key topics
- [ ] Update patterns.md with latest examples
- [ ] Refresh reference.md with current APIs
- [ ] Add Context7 source attribution
- [ ] Test all updated examples
- [ ] Update skill metadata (date, version)
- [ ] Commit changes
```

### Pattern: Quick Reference Update

```markdown
## Quick Update Template

1. **Check current content**
   - Read existing skill files
   - Note outdated information

2. **Fetch updates**
   - Resolve library IDs
   - Get focused docs for changed areas

3. **Update files**
   - patterns.md: New usage examples
   - reference.md: Current API specs
   - README.md: Version notes

4. **Document changes**
   ```markdown
   ## Updates (Date)
   
   Updated with Context7 docs:
   - Library: {name} ({version})
   - Trust Score: {score}
   - Changes: {summary}
   ```
```

## Library ID Formats

Context7 uses three ID formats:

### Standard
```
/org/project
```
Examples: `/vercel/next.js`, `/openai/openai-python`

### Versioned
```
/org/project/version
```
Examples: `/openai/openai-node/v5_19_1`

### Website
```
/websites/domain
```
Examples: `/websites/platform_openai`

## Error Handling

### Common Issues

**"Library not found"**
- Try alternative spellings
- Include organization name
- Search by full project name

**"Low trust score"**
- Verify it's official library
- Check if alternative exists with higher score
- Proceed with caution if necessary

**"Documentation not finalized"**
- Library may be too new
- Try alternative library
- Check back later

## Statistics

- **48,148+ libraries** indexed
- **Multi-language** support
- **Auto-updated** from sources
- **Open source** MCP server
- **Production-ready** stability

## File Structure

```
.github/copilot-skills/context7/
├── patterns.md          # 10 common usage patterns
├── reference.md         # Complete API documentation
└── README.md            # This file
```

## Related Skills

- **docs-to-skill** - Convert docs into skills
- **openai** - Enhanced with Context7
- **ai-sdk** - Updated via Context7
- **All framework skills** - Can benefit

## Resources

- **Website**: https://context7.com
- **GitHub**: https://github.com/upstash/context7
- **NPM**: https://www.npmjs.com/package/@upstash/context7-mcp
- **Issues**: https://github.com/upstash/context7/issues
- **MCP Hub**: https://smithery.ai/server/@upstash/context7-mcp

## Contributing

To improve this skill:
1. Test patterns with real libraries
2. Document edge cases
3. Add new workflow examples
4. Update with Context7 changes
5. Submit feedback via GitHub

## License

Context7 is open source. This skill documentation follows the same principles.

---

**💡 Pro Tip**: Use Context7 to keep ALL your skills current! Outdated documentation is the enemy of good code.
