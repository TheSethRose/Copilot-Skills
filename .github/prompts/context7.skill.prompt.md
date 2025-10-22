---
description: Access up-to-date documentation for 48,000+ libraries via Context7 API or MCP
---

# Context7

**Purpose**: Quickly access current documentation for any library using Context7's massive documentation database.

## When to Use This Skill

Use this skill when:
- Learning a new library or framework
- Needing up-to-date documentation (not outdated docs)
- Building with unfamiliar APIs
- Enhancing other skills with current library docs
- Working with any of 48,148+ supported libraries

**Keywords**: context7, up-to-date docs, latest documentation, library documentation, current docs, resolve library

## Quick Reference

### Using Context7 MCP (Recommended)

```typescript
// Available via #context7 tool in Copilot
// 1. Resolve library ID
#context7 resolve-library-id "next.js"

// 2. Get documentation
#context7 get-library-docs "/vercel/next.js" "routing and middleware"
```

### Using Context7 API

```bash
# Search for a library
curl https://api.context7.com/v1/libraries/search?q=nextjs

# Get documentation
curl https://api.context7.com/v1/libraries/{library_id}/docs \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{"topic": "routing", "tokens": 5000}'
```

## Core Workflows

### Workflow 1: Find Library Documentation

**When:** You need docs for a specific library

**Steps:**
1. Identify the library name (e.g., "Next.js", "React", "FastAPI")
2. Use `resolve-library-id` to find the Context7 ID
3. Review matches - look for high trust scores (7-10)
4. Select the most relevant library ID

**Example:**
```
User: "I need Next.js documentation"
→ Call resolve-library-id "next.js"
→ Get results with trust scores
→ Select /vercel/next.js (trust: 9.5)
```

### Workflow 2: Get Targeted Documentation

**When:** You need specific information from docs

**Steps:**
1. Have the library ID from Workflow 1
2. Specify your topic/question clearly
3. Call `get-library-docs` with topic
4. Set appropriate token limit (default: 5000)

**Example:**
```typescript
get-library-docs(
  libraryID: "/vercel/next.js",
  topic: "app router file conventions and layouts",
  tokens: 8000
)
```

### Workflow 3: Enhance Existing Skills

**When:** A skill would benefit from current docs

**Steps:**
1. Identify which library documentation would help
2. Fetch relevant docs using Context7
3. Integrate patterns into skill's `patterns.md`
4. Add references to skill's `reference.md`
5. Update skill prompt with new capabilities

**Example - Enhancing OpenAI skill:**
```python
# Before enhancement
# Outdated GPT-4 examples

# After Context7 enhancement
# Latest GPT-5, o3, reasoning models
# Current API parameters (verbosity, reasoning_effort)
# Up-to-date pricing and features
```

### Workflow 4: Compare Library Options

**When:** Choosing between similar libraries

**Steps:**
1. Resolve multiple library IDs
2. Compare trust scores and snippet counts
3. Fetch docs for top candidates
4. Compare API patterns and features
5. Make informed decision

**Example:**
```
Comparing React UI libraries:
→ @shadcn (9.5 trust, 244 snippets)
→ @radix-ui (9.3 trust, 179 snippets)  
→ @chakra-ui (trust varies by version)
```

## Available via MCP

Context7 provides two MCP tools:

### 1. resolve-library-id
**Purpose:** Find Context7-compatible library IDs

**Parameters:**
- `libraryName` (string) - Library to search for

**Returns:**
- Library ID (e.g., `/vercel/next.js`)
- Description
- Trust score (0-10)
- Code snippet count
- Available versions

**Selection criteria:**
- Name similarity (prioritize exact matches)
- Trust score (7-10 = authoritative)
- Documentation coverage (higher snippet count)
- Description relevance

### 2. get-library-docs
**Purpose:** Retrieve focused documentation

**Parameters:**
- `context7CompatibleLibraryID` (string) - From resolve-library-id
- `topic` (string, optional) - Focus area
- `tokens` (number, optional) - Max tokens (default: 5000)

**Returns:**
- Targeted documentation
- Code examples
- API references
- Best practices

## Context7 Stats

- **48,148+ libraries** indexed
- **Trust scores** - Reliability indicator (0-10)
- **Code snippets** - Working examples count
- **Multi-language** - Python, JavaScript, TypeScript, Go, Rust, etc.
- **Auto-updated** - Fresh from source repositories

## Common Use Cases

### Use Case 1: Learning New Framework
```
Problem: Need to learn SvelteKit quickly
Solution:
1. resolve-library-id "sveltekit"
2. get-library-docs "/sveltejs/kit" "routing and data loading"
3. Review patterns and examples
4. Build with confidence
```

### Use Case 2: API Migration
```
Problem: Migrating from deprecated API version
Solution:
1. resolve-library-id "library-name/v2"
2. get-library-docs with "migration guide" topic
3. Compare old vs new patterns
4. Update codebase systematically
```

### Use Case 3: Troubleshooting
```
Problem: API call failing with new library version
Solution:
1. Check library version in resolve results
2. get-library-docs for specific API endpoint
3. Compare your code with current examples
4. Fix incompatibilities
```

## Best Practices

✅ **Do:**
- Always check trust scores (prefer 7-10)
- Use specific topics for focused results
- Compare snippet counts for coverage
- Verify version compatibility
- Cache commonly used docs

❌ **Don't:**
- Skip the resolve step (IDs are specific)
- Use vague topics (be specific)
- Ignore trust scores (low = unreliable)
- Request excessive tokens (wastes resources)
- Forget to check for newer versions

## Integration Patterns

### Pattern 1: Skill Enhancement
```markdown
## Updating a Skill with Context7

1. Identify outdated information in skill
2. Call resolve-library-id for relevant library
3. Get current documentation with specific topics
4. Update patterns.md with new examples
5. Refresh reference.md with latest APIs
6. Test updated examples
7. Commit with message: "chore: update with Context7 docs"
```

### Pattern 2: Quick Reference
```bash
# Add to any skill's patterns.md:

## Updated with Context7 (Date)

Latest patterns fetched from Context7:
- Library: {library-name}
- Version: {version}
- Trust Score: {score}
- Last Updated: {date}

[Current patterns here]
```

## Library ID Formats

Context7 uses specific ID formats:

```
Format: /org/project
Example: /vercel/next.js

Format: /org/project/version  
Example: /openai/openai-node/v4_104_0

Format: /websites/domain
Example: /websites/platform_openai
```

## Troubleshooting

**"Library not found"**
- Try alternative spellings
- Search by organization name
- Check if library is too niche
- Browse similar libraries

**"Low trust score"**
- Verify it's the official library
- Check snippet count (low = limited docs)
- Consider alternatives with higher trust
- Use with caution

**"Too many results"**
- Be more specific in search
- Include version if known
- Use full library name
- Check organization name

## Related Skills

- **docs-to-skill** - Convert documentation into skills
- **openai** - Enhanced with Context7 docs
- **ai-sdk** - Can be updated via Context7
- **All framework skills** - Benefit from current docs

## Reference Documentation

See `.github/copilot-skills/documentation/context7/`:
- `patterns.md` - Common usage patterns
- `reference.md` - Complete API reference
- `examples/` - Real-world integration examples

## Resources

- **Context7 Website**: https://context7.com
- **MCP Tools**: Available as #context7 in Copilot
- **API Docs**: https://api.context7.com/docs
- **Library Count**: 48,148+ and growing

---

**Pro Tip**: Use Context7 to keep ALL your skills up-to-date! Outdated docs are the enemy of good code.
