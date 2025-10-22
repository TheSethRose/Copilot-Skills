---
description: "Auto-loaded context for Context7 API and MCP usage"
applyTo: "**/*{context7,Context7,library-docs,up-to-date-docs}*"
---

# Context7 - Automatic Context Instructions

**Related Prompt:** `/context7`  
**Related Skill:** `.github/copilot-skills/documentation/context7/`

**Triggers:** context7, up-to-date docs, latest documentation, library documentation, resolve library, get docs

## Context: Up-to-Date Library Documentation

When working with library documentation or when user queries mention getting current docs, this context is automatically activated.

## Core Principles

### Always Use Current Documentation
- **Never rely on outdated docs** from training data
- **Always check Context7 first** for library information
- **Verify versions** - libraries change rapidly
- **Trust scores matter** - prefer 7-10 range

### Progressive Documentation Retrieval
1. **Start broad** - Resolve library ID first
2. **Get specific** - Request docs with focused topics
3. **Iterate** - Refine topic if results aren't helpful
4. **Cache** - Remember frequently used patterns

## Default Behaviors

### When user mentions "need docs for {library}"
1. Suggest `/context7` skill prompt
2. Call `resolve-library-id` with library name
3. Show top 3-5 matches with trust scores
4. Ask user to confirm which library
5. Fetch docs with relevant topic

### When user mentions "latest {library} features"
1. Resolve library ID
2. Check for version information
3. Get docs with topic "new features" or "changelog"
4. Highlight recent updates
5. Compare with older versions if available

### When enhancing a skill
1. Identify which libraries the skill covers
2. Resolve IDs for each library
3. Fetch current documentation
4. Update `patterns.md` with latest examples
5. Refresh `reference.md` with current APIs
6. Note the update date and Context7 source

### When user asks "which library should I use"
1. Resolve multiple candidate libraries
2. Compare trust scores
3. Compare snippet counts (coverage indicator)
4. Fetch brief docs for top candidates
5. Present comparison table
6. Recommend based on use case + trust + coverage

## Quality Guidelines

### ✅ Do
- Always call `resolve-library-id` before getting docs
- Use specific topics for focused results
- Check trust scores (7-10 = reliable)
- Compare snippet counts for coverage
- Verify version compatibility
- Update skills regularly with Context7
- Cache commonly accessed docs
- Note Context7 as source in skill updates

### ❌ Don't
- Skip the resolve step (IDs must be exact)
- Use vague topics like "everything"
- Ignore low trust scores (<5)
- Request excessive tokens (>10k without reason)
- Mix up library IDs (format matters)
- Forget to check for newer versions
- Rely on training data over Context7
- Update skills without testing examples

## MCP Tool Usage

### resolve-library-id Pattern

```typescript
// Good - Specific library name
resolve-library-id("next.js")
resolve-library-id("fastapi")
resolve-library-id("shadcn")

// Less effective - Too vague
resolve-library-id("ui library")
resolve-library-id("database")
```

**Response handling:**
```typescript
// Always show user:
// 1. Library name
// 2. Trust score
// 3. Snippet count
// 4. Description
// Then let them choose or auto-select highest trust
```

### get-library-docs Pattern

```typescript
// Good - Focused topic
get-library-docs(
  "/vercel/next.js",
  "app router layouts and nested routes",
  5000  // Default token count
)

// Less effective - Too broad
get-library-docs(
  "/vercel/next.js",
  "everything",
  15000  // Wasteful - use specific topics
)

// Note: Minimum tokens is 1000 (auto-increased if lower)
// Default is 5000
// Higher values provide more context but consume more tokens
```

**Topic crafting:**
- Be specific: "authentication with middleware"
- Not generic: "security"
- Include context: "React server components with data fetching"
- Not vague: "components"

## Common Workflows

### Workflow: Learn New Library

```bash
# 1. Find library
User: "I need to learn Prisma ORM"
→ resolve-library-id("prisma")
→ Review matches, select /prisma/prisma

# 2. Get overview
→ get-library-docs("/prisma/prisma", "getting started", 3000)
→ Present: setup, basic usage, key concepts

# 3. Deep dive
User: "How do I do migrations?"
→ get-library-docs("/prisma/prisma", "migrations", 4000)
→ Present: migration patterns, commands, best practices
```

### Workflow: Update Skill

```bash
# Example: Updating Next.js skill
# 1. Check current skill content
→ Read .github/copilot-skills/nextjs/patterns.md

# 2. Identify outdated information
→ Note: Using Pages Router examples, missing App Router

# 3. Fetch current docs
→ resolve-library-id("next.js")
→ get-library-docs("/vercel/next.js", "app router patterns", 8000)

# 4. Update skill files
→ Update patterns.md with App Router examples
→ Refresh reference.md with current API
→ Add note: "Updated with Context7 docs (Oct 2024)"

# 5. Test examples
→ Verify new patterns work
→ Check for breaking changes
```

### Workflow: Compare Libraries

```bash
# Example: Choosing UI library
User: "Should I use Radix UI or Chakra UI?"

# 1. Resolve both
→ resolve-library-id("radix-ui")
→ resolve-library-id("chakra-ui")

# 2. Compare metrics
Radix UI: Trust 9.3, 179 snippets
Chakra UI: Trust varies, check versions

# 3. Get focused docs
→ get-library-docs("/radix-ui/react", "accessibility patterns", 4000)
→ get-library-docs("/chakra-ui/react", "theming system", 4000)

# 4. Present comparison
→ Show API differences
→ Highlight use case fit
→ Recommend based on needs
```

## Trust Score Interpretation

| Score | Meaning | Action |
|-------|---------|--------|
| 9-10 | Highly authoritative | Use with confidence |
| 7-8 | Reliable | Good choice |
| 5-6 | Moderate | Verify examples |
| 3-4 | Low confidence | Use caution |
| 0-2 | Unreliable | Seek alternatives |

## Snippet Count Guidelines

| Count | Coverage | Implications |
|-------|----------|--------------|
| 1000+ | Excellent | Comprehensive docs |
| 500-1000 | Very good | Well documented |
| 100-500 | Good | Core features covered |
| 50-100 | Moderate | Basic coverage |
| <50 | Limited | May lack details |

## Library ID Formats

```
Standard format:
/org/project

Examples:
/vercel/next.js
/openai/openai-python
/shadcn/ui

With version:
/org/project/version

Examples:
/openai/openai-node/v4_104_0
/vercel/next.js/v14.3.0

Website docs:
/websites/domain

Examples:
/websites/platform_openai
/websites/docs_rs-openai-api-rs-latest-openai_api_rs
```

## Error Handling

**"Library not found"**
```typescript
// Try variations
resolve-library-id("nextjs")  // No results
resolve-library-id("next.js")  // ✓ Found
resolve-library-id("next")     // Multiple results

// Search by org
resolve-library-id("vercel next")  // ✓ Better
```

**"Ambiguous results"**
```typescript
// Too generic
resolve-library-id("ui")  // 100+ results

// More specific
resolve-library-id("shadcn ui")  // ✓ Focused
resolve-library-id("radix ui")   // ✓ Clear
```

**"Low trust score"**
```typescript
// Verify it's official
if (trustScore < 5) {
  // Check if alternative exists
  // Verify against official source
  // Use with caution
}
```

## Integration with Other Skills

### Enhancing Existing Skills

When updating any skill, consider Context7:

1. **Identify libraries used** in the skill
2. **Resolve each library** via Context7
3. **Fetch current patterns** for each
4. **Update skill files** with latest info
5. **Document Context7 usage** in skill
6. **Test updated examples**

### Skills That Benefit Most

High-value targets for Context7 enhancement:

- **Frontend frameworks** - React, Vue, Svelte, Next.js
- **Backend frameworks** - FastAPI, Express, Django
- **UI libraries** - Tailwind, shadcn, Radix, Chakra
- **AI/ML** - OpenAI, Anthropic, LangChain, Vercel AI SDK
- **Database** - Prisma, Supabase, MongoDB
- **Testing** - Cypress, Playwright, Vitest
- **Build tools** - Vite, Webpack, Turbopack

## Bundled Scripts

Context7 skill provides helper scripts:

```bash
# Check if library exists in Context7
.github/copilot-skills/documentation/context7/scripts/check-library.sh "next.js"

# Compare trust scores of multiple libraries
.github/copilot-skills/documentation/context7/scripts/compare-libraries.sh "react" "vue" "svelte"

# Bulk update skills with Context7
.github/copilot-skills/documentation/context7/scripts/update-skills.sh
```

## Next Steps

When working with Context7:
1. Use `/context7` prompt for guided workflows
2. Check `.github/copilot-skills/documentation/context7/patterns.md` for common patterns
3. Reference `.github/copilot-skills/documentation/context7/reference.md` for API details
4. Run bundled scripts for automation

## Related Skills

- **docs-to-skill** - Convert Context7 docs into skills
- **All library skills** - Can be enhanced with Context7
- **create-skill** - Use Context7 for skill research

## Best Practices Summary

🎯 **Golden Rules:**
1. Always resolve before fetching docs
2. Trust scores 7+ are reliable
3. Be specific with topics
4. Update skills regularly
5. Note Context7 as source
6. Test all examples
7. Cache common queries
8. Verify version compatibility

With Context7, you always have the **latest, most accurate documentation** at your fingertips! 🚀
