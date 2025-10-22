# Context7 - Common Patterns

**Quick Reference**: See `.github/copilot-skills/context7/reference.md` for complete tool documentation.

---

## 🔧 Tool Parameters Reference

### resolve-library-id

```
INPUT:    libraryName (string)
          "react", "next.js", "fastapi", etc.

OUTPUT:   libraryId, name, description, 
          trustScore (0-10), codeSnippets count, 
          versions array
```

### get-library-docs

```
INPUT:    context7CompatibleLibraryID (string, required)
          "/facebook/react", "/vercel/next.js", etc.
          
          topic (string, optional)
          "hooks", "routing", "authentication", etc.
          
          tokens (number, optional, default: 5000)
          Min: 1000, Max: 15000

OUTPUT:   string (formatted documentation with examples)
```

---

### The Two Tools You Have

Context7 gives you **two powerful tools** in Copilot:

1. **`resolve-library-id`** - Find the exact Context7 ID for any library
2. **`get-library-docs`** - Fetch current documentation for that library

### Real-World Usage in Chat

Here's exactly how to use it:

```
YOU: "I need to learn about React hooks"

COPILOT DOES:
1. Calls: resolve-library-id("react")
   ↓ Gets: /facebook/react (Trust: 9.5, 637K snippets)

2. Calls: get-library-docs("/facebook/react", "hooks useState useEffect", 5000)
   ↓ Gets: Current React hooks documentation with examples

COPILOT RESPONDS: [Shows you the latest React hooks patterns]
```

### Three Ways to Trigger Context7

**Option A: Let Copilot figure it out**
```
"Show me how to use async/await with Prisma"
→ Copilot auto-resolves and fetches docs
```

**Option B: Hint with library name**
```
"Using Next.js, how do I create API routes?"
→ Copilot resolves next.js and fetches docs about API routes
```

**Option C: Give the exact ID (if you know it)**
```
"Get docs for /vercel/next.js about middleware"
→ Copilot skips resolve and goes straight to fetching
```

### What You Get Back

When you ask for docs, Copilot returns:

✅ **Current API documentation** - Not outdated training data  
✅ **Code examples** - Real, working patterns  
✅ **Best practices** - How professionals use the library  
✅ **Version info** - What version the docs are from  
✅ **Related APIs** - Connected features and methods  

### Topic Specificity

The real power is specifying **what you want to know**:

❌ **Too vague:**
```
topic: "everything"
→ Returns too much, hard to use
```

✅ **Better:**
```
topic: "state management and hooks"
→ Returns exactly what you need
```

✅ **Best:**
```
topic: "hooks for state management with patterns"
→ Returns focused features with examples
```

### Token Levels

Tokens control documentation length:

- **2000 tokens** = Quick overview (30 seconds)
- **5000 tokens** = Standard full docs (2-3 min) - DEFAULT
- **10000 tokens** = Deep dive (5+ min)
- **15000 tokens** = Comprehensive (10+ min)

---

## Pattern 1: Resolve Library ID

Find the exact Context7 ID for any library name.

**Tool**: `resolve-library-id`

**Input**: Library name (e.g., "react", "next.js", "fastapi")

**Output**: 
- Library ID (e.g., "/facebook/react")
- Trust score (0-10)
- Code snippet count
- Available versions

**When to use**: Before calling get-library-docs, to get the exact library ID


## Pattern 2: Get Library Documentation

Fetch current docs for a specific library.

**Tool**: `get-library-docs`

**Inputs**:
- `context7CompatibleLibraryID` (required) - Library ID from resolve-library-id
- `topic` (optional) - What you want to know (be specific!)
- `tokens` (optional) - How much docs (default: 5000)

**Output**: Formatted documentation text with examples

**When to use**: After you have a library ID, to fetch current documentation

**Best practices**:
- Be specific with topics
- Start with 5000 tokens (default)
- Increase tokens only if you need more depth

---

## Pattern 3: Choosing Between Similar Libraries

Compare multiple libraries to pick the best one for your project.

### In Copilot Chat

```
YOU: "I need to pick a UI component library. 
Compare shadcn/ui vs Radix UI vs Chakra UI"

COPILOT DOES:
1. resolve-library-id("shadcn")
   → /shadcn/ui (Trust: 9.5, 244K snippets)
2. resolve-library-id("radix ui")
   → /radix-ui/react (Trust: 9.3, 179K snippets)
3. resolve-library-id("chakra ui")
   → /chakra-ui/react (Trust: 8.5, varies)

4. get-library-docs("/shadcn/ui", "component styling composability", 4000)
5. get-library-docs("/radix-ui/react", "accessibility primitives", 4000)
6. get-library-docs("/chakra-ui/react", "theming system", 4000)

RESULT: [Comparison showing pros/cons of each]
```

### Real Decision Scenarios

**Picking a database ORM:**
```
"Compare Prisma vs Drizzle vs Sequelize. 
Show me type safety, migrations, and query performance"

→ Copilot fetches latest docs for all three
→ You see current features and trade-offs
```

**Choosing an auth library:**
```
"Should I use NextAuth, Better Auth, or Supabase Auth?
Show me setup, providers, and session management"

→ Gets docs for all three
→ Shows API differences
→ Recommends based on your needs
```

**Backend framework decision:**
```
"Compare FastAPI vs Django vs Flask for a REST API project"

→ Gets performance, ease, community for each
→ Shows current v4 vs v5 differences
```

**Use when**: 
- Starting new project
- Switching libraries
- Evaluating technology choices
- Need data-driven decisions

**Pro tip**: Ask Copilot to "recommend" after the comparison - it'll use trust scores + snippet counts to suggest the best choice

---

## Pattern 3: Version-Specific Documentation

Fetch docs for a specific library version using the versioned ID.

**Use case**: Your project is locked to v5, but you need to know v5-specific features

**How**:
1. Call `resolve-library-id("library-name")` to see available versions
2. Use the versioned ID in `get-library-docs`
   - Example: `/openai/openai-python/v1_68_0` (instead of latest)
3. Get docs for your specific version

**When to use**: 
- Locked to specific version
- Debugging version-specific bugs
- Comparing versions (v4 vs v5 differences)

---

## Pattern 4: Skill Enhancement Workflow

Update an existing skill with current documentation from Context7.

**Workflow**:
1. Identify outdated content in skill files
2. Resolve library: `resolve-library-id("library-name")`
3. Fetch docs with specific topics: `get-library-docs(libraryID, topic)`
4. Update skill's `patterns.md` and `reference.md`
5. Test updated examples
6. Commit with note: "chore: update with Context7 docs"

**When to use**: Keeping skills current with library updates

---

## Pattern 5: Specific Topic Retrieval

Be very specific with your topic parameter for best results.

**Topic specificity levels**:

❌ Vague:
```
topic: "everything"
```

✓ Better:
```
topic: "authentication and middleware"
```

✓ Best:
```
topic: "JWT token validation in middleware"
```

**Rule**: The more specific, the better the results

---

## Pattern 6: Troubleshooting with Context7

Debug issues by checking current API.

```typescript
// Problem: Code worked last month, now broken
// Solution: Check if API changed

// 1. Get current docs
const current = await get_library_docs(
  "/openai/openai-python",
  "chat completions API parameters",
  5000
## Pattern 6: Troubleshooting with Context7

Fix bugs caused by breaking API changes.

**Workflow**:
1. Get current docs for the library
2. Compare with your code
3. Identify deprecated parameters or methods
4. Update code based on current API

**When to use**: Code broke after library update, fixing version-specific issues

---

## Pattern 7: Batch Library Research

Research multiple related libraries to compare options.

**Workflow**:
1. List libraries to compare (e.g., 3-5 options)
2. Call `resolve-library-id` for each
3. Compare trust scores and snippet counts
4. Get docs for top candidates
5. Make data-driven decision

**When to use**: Planning new project, choosing between options, evaluating stack

---

## Pattern 8: Trust Score Validation

Verify library authenticity before use.

```typescript
async function validateLibrary(name: string) {
  const results = await resolve_library_id(name);
  
  // Filter by trust score
  const reliable = results.filter(lib => lib.trustScore >= 7);
  
  if (reliable.length === 0) {
    console.warn(`⚠️  No reliable docs found for ${name}`);
    console.log("Consider:");
    console.log("1. Check spelling");
    console.log("2. Search alternative name");
    console.log("3. Use official website docs");
    return null;
  }
  
  // Show best match
  const best = reliable[0];
  console.log(`✓ Found: ${best.name}`);
  console.log(`  Trust: ${best.trustScore}/10`);
  console.log(`  Coverage: ${best.snippets} examples`);
  console.log(`  ID: ${best.id}`);
  
  return best;
}

// Usage
const lib = await validateLibrary("react-query");
if (lib) {
  const docs = await get_library_docs(lib.id, "queries", 5000);
}
```

**Use when**: Working with unfamiliar libraries or verifying sources.

**See also**: Trust score interpretation in `reference.md`.

---

## Pattern 9: Caching Strategy

Optimize repeated lookups with caching.

```typescript
// Simple cache implementation
const cache = new Map<string, any>();
const CACHE_TTL = 1000 * 60 * 60; // 1 hour

async function getCachedDocs(
  libraryId: string,
  topic: string,
  tokens: number = 5000
) {
  const key = `${libraryId}:${topic}`;
  
  // Check cache
  const cached = cache.get(key);
  if (cached && Date.now() - cached.timestamp < CACHE_TTL) {
    console.log("📦 Using cached docs");
    return cached.docs;
  }
  
  // Fetch fresh docs
  console.log("🌐 Fetching from Context7");
  const docs = await get_library_docs(libraryId, topic, tokens);
  
  // Cache result
  cache.set(key, {
    docs,
    timestamp: Date.now()
  });
  
  return docs;
}

// Usage
const docs1 = await getCachedDocs("/vercel/next.js", "routing");  // Fresh
const docs2 = await getCachedDocs("/vercel/next.js", "routing");  // Cached ✓
```

**Use when**: Frequently accessing the same documentation.

**See also**: Performance optimization in `reference.md`.

---

## Pattern 10: Website Documentation

Access documentation from websites (not just packages).

```typescript
// Some docs are indexed from websites
const platformDocs = await resolve_library_id("openai platform");

// Results might include:
// - /websites/platform_openai (Trust: 7.5, Snippets: 382K)

// Get comprehensive docs
const docs = await get_library_docs(
  "/websites/platform_openai",
  "chat completions API with function calling",
  8000
);

// This gives you the actual platform documentation
// Not just package docs!
```

**Use when**: Need official platform docs vs just package API.

**See also**: Website vs package docs in `reference.md`.

---

## Quick Pattern Finder

| Need | Pattern | Time to implement |
|------|---------|-------------------|
| Learn new library | Pattern 1 | 2 min |
| Specific version | Pattern 2 | 3 min |
| Compare options | Pattern 3 | 10 min |
| Update skill | Pattern 4 | 30 min |
| Focused lookup | Pattern 5 | 1 min |
| Debug issue | Pattern 6 | 5 min |
| Research stack | Pattern 7 | 15 min |
| Verify source | Pattern 8 | 3 min |
| Optimize performance | Pattern 9 | 20 min |
| Platform docs | Pattern 10 | 2 min |

## Best Practices

### Topic Crafting

```typescript
// ❌ Too broad
"everything", "all features", "documentation"

// ✓ Specific
"authentication middleware", "database migrations", "error handling"

// ✓✓ Very targeted
"JWT authentication with refresh tokens", 
"Prisma schema relations and cascading deletes",
"Custom error pages with getServerSideProps"
```

### Token Allocation

```typescript
// Quick lookup: 2000-3000 tokens
get_library_docs(id, topic, 2500);

// Standard research: 5000 tokens
get_library_docs(id, topic, 5000);

// Deep dive: 8000-10000 tokens
get_library_docs(id, topic, 10000);

// Maximum: 15000 tokens (rarely needed)
get_library_docs(id, topic, 15000);
```

### Selection Criteria

When choosing from multiple results:
1. **Trust score** (higher = better)
2. **Snippet count** (more = better coverage)
3. **Name match** (exact > partial)
4. **Description relevance** (matches use case)

## Next Steps

1. **Choose a pattern** matching your use case
2. **Adapt the code** for your specific library
3. **Check reference.md** for API details
4. **Test locally** before integrating
5. **Cache results** for repeated use

## Integration Tips

- Use Context7 MCP tools in Copilot with `#context7`
- Always resolve before fetching docs
- Check trust scores (7+ recommended)
- Be specific with topics
- Cache frequently accessed docs
- Update skills regularly
- Document Context7 as source
