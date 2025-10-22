# Context7 API Reference

Complete technical reference for Context7 MCP server and API.

## MCP Server Installation

### Package Information
- **Package**: `@upstash/context7-mcp`
- **NPM**: `npx -y @upstash/context7-mcp@latest`
- **Repository**: https://github.com/upstash/context7
- **License**: Open source

### Installation Methods

#### Local Server (Recommended)
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

#### Remote Server (SSE)
```json
{
  "mcpServers": {
    "context7": {
      "serverUrl": "https://mcp.context7.com/sse"
    }
  }
}
```

#### HTTP Server
```json
{
  "mcpServers": {
    "context7": {
      "type": "http",
      "url": "https://mcp.context7.com/mcp",
      "tools": ["get-library-docs", "resolve-library-id"]
    }
  }
}
```

#### With API Key
```json
{
  "mcpServers": {
    "context7": {
      "type": "http",
      "url": "https://mcp.context7.com/mcp",
      "headers": {
        "CONTEXT7_API_KEY": "ctx7sk_your_api_key_here"
      },
      "tools": ["get-library-docs", "resolve-library-id"]
    }
  }
}
```

## MCP Tools

### 1. resolve-library-id

**Purpose**: Resolves a package/product name to a Context7-compatible library ID.

**Critical**: You MUST call this before `get-library-docs` UNLESS the user explicitly provides a library ID in format `/org/project` or `/org/project/version`.

#### Parameters
- `libraryName` (string, required) - Library name to search for

#### Returns
```typescript
{
  libraryId: string,          // e.g., "/vercel/next.js"
  name: string,               // Display name
  description: string,        // Brief description
  trustScore: number,         // 0-10 authority indicator
  codeSnippets: number,       // Available example count
  versions?: string[]         // Available versions if any
}
```

#### Selection Criteria
1. **Name similarity** - Exact matches prioritized
2. **Description relevance** - Matches query intent
3. **Trust score** - 7-10 considered authoritative
4. **Documentation coverage** - Higher snippet count = better

#### Example Usage
```typescript
// Search for library
const results = await resolve_library_id("next.js");

// Results array includes multiple matches
// Select best match based on trust score and relevance
const best = results.find(r => r.trustScore >= 9);
```

---

### 2. get-library-docs

**Purpose**: Fetches up-to-date documentation for a library.

#### Parameters
- `context7CompatibleLibraryID` (string, required)
  - Exact ID from `resolve-library-id`
  - Format: `/org/project` or `/org/project/version`
  - Example: `/vercel/next.js` or `/openai/openai-node/v5_19_1`

- `topic` (string, optional)
  - Focus documentation on specific area
  - Example: "routing", "hooks", "authentication"
  - Be specific for best results

- `tokens` (number, optional, default: 5000)
  - Maximum tokens to return
  - Minimum: 1000 (auto-increased if lower)
  - Default was 10000, now 5000 in latest version
  - Higher values = more context but more cost

#### Returns
```typescript
string // Formatted documentation text with code examples
```

#### Example Usage
```typescript
// Basic usage
const docs = await get_library_docs(
  "/vercel/next.js",
  "app router layouts and nested routes",
  5000
);

// Version-specific
const docsV5 = await get_library_docs(
  "/openai/openai-node/v5_19_1",
  "streaming chat completions",
  8000
);
```

## API Endpoints (Direct Access)

### Base URL
```
https://api.context7.com
```

### Search Libraries
```http
GET /v1/search?q={query}
```

**Parameters:**
- `q` (string, required) - Search query

**Response:**
```json
{
  "results": [
    {
      "id": "/vercel/next.js",
      "name": "Next.js",
      "description": "The React Framework",
      "trustScore": 9.5,
      "codeSnippets": 547000
    }
  ]
}
```

### Get Documentation
```http
GET /v1/{libraryId}?tokens={tokens}&topic={topic}&type={type}
```

**Parameters:**
- `libraryId` (path, required) - Library ID without leading slash
- `tokens` (query, optional, default: 5000) - Max tokens
- `topic` (query, optional) - Focus topic
- `type` (query, optional, default: "code") - Documentation type

**Headers:**
- `Authorization: Bearer ctx7sk_...` (optional, for API key)
- `X-Client-IP` (optional, for tracking)
- `X-Context7-Source: mcp-server` (automatic from MCP)

**Response:**
```
Plain text documentation with code examples
```

## Configuration Details

### Supported Platforms

Context7 MCP works with:
- **Claude Desktop** - Via MCP config
- **VS Code Copilot** - Via mcp.json
- **Cursor** - Via MCP settings
- **Windsurf** - Via MCP config
- **Augment Code** - Via UI + command
- **Zed** - Via settings.json
- **BoltAI** - Via plugin config
- **Copilot Coding Agent** - Via GitHub settings
- **Docker** - Via container

### Environment Variables

```bash
# Optional API key
CONTEXT7_API_KEY=ctx7sk_your_key

# Optional HTTPS proxy
https_proxy=http://proxy.example.com:8080
HTTPS_PROXY=http://proxy.example.com:8080
```

### Server Configuration

#### Transport Types
- `stdio` (default) - Standard input/output
- `http` - HTTP server on port 3000
- `sse` - Server-Sent Events

#### HTTP Server Options
```bash
# Run with custom port
npx @upstash/context7-mcp --transport http --port 3001
```

## Error Handling

### Common Errors

**401 Unauthorized**
```
Unauthorized. Please check your API key.
API keys should start with 'ctx7sk'
```

**404 Not Found**
```
The library you are trying to access does not exist.
Please try with a different library ID.
```

**429 Rate Limited**
```
Rate limited due to too many requests.
Please try again later.
```

**Library Not Finalized**
```
Documentation not found or not finalized for this library.
Use 'resolve-library-id' to get a valid Context7-compatible library ID.
```

### Error Recovery

```typescript
try {
  const docs = await get_library_docs(libraryId, topic, tokens);
} catch (error) {
  if (error.status === 404) {
    // Library doesn't exist
    // Try resolve-library-id with different search term
  } else if (error.status === 429) {
    // Rate limited
    // Implement exponential backoff
  } else {
    // Other error
    // Log and retry
  }
}
```

## Library ID Formats

### Standard Format
```
/org/project
```

**Examples:**
- `/vercel/next.js`
- `/openai/openai-python`
- `/shadcn/ui`
- `/supabase/supabase`

### Versioned Format
```
/org/project/version
```

**Examples:**
- `/openai/openai-node/v4_104_0`
- `/openai/openai-node/v5_19_1`
- `/vercel/next.js/v14.3.0-canary.87`

### Website Documentation
```
/websites/domain
```

**Examples:**
- `/websites/platform_openai`
- `/websites/docs_rs-openai-api-rs-latest-openai_api_rs`
- `/websites/tailwindcss`

## Token Management

### Token Limits

| Purpose | Recommended Tokens | Min | Max |
|---------|-------------------|-----|-----|
| Quick lookup | 2000-3000 | 1000 | - |
| Standard research | 5000 (default) | 1000 | - |
| Deep dive | 8000-10000 | 1000 | - |
| Comprehensive | 15000+ | 1000 | - |

**Note:** Values below 1000 are automatically increased to 1000.

### Token Optimization

```typescript
// Start small
let docs = await get_library_docs(id, topic, 2000);

// If insufficient, increase
if (docs.length < expectedLength) {
  docs = await get_library_docs(id, topic, 5000);
}

// For comprehensive research
docs = await get_library_docs(id, topic, 10000);
```

## Trust Scores

### Interpretation

| Score | Reliability | Recommendation |
|-------|-------------|----------------|
| 9-10 | Highly authoritative | Use with confidence |
| 7-8 | Reliable | Good choice |
| 5-6 | Moderate | Verify examples |
| 3-4 | Low confidence | Use caution |
| 0-2 | Unreliable | Seek alternatives |

### Factors Affecting Trust

- **Official repository** - Higher scores
- **Documentation quality** - Well-maintained
- **Community size** - Popular projects
- **Update frequency** - Recently updated
- **Code snippet coverage** - More examples

## Coverage Metrics

### Code Snippet Counts

| Range | Coverage Level | Implications |
|-------|---------------|--------------|
| 100K+ | Exceptional | Comprehensive documentation |
| 10K-100K | Excellent | Very well documented |
| 1K-10K | Very Good | Good coverage |
| 100-1K | Good | Core features covered |
| <100 | Limited | May lack details |

**Top Libraries by Coverage:**
- OpenAI Platform: 382K+ snippets
- MongoDB: 131K snippets
- Next.js: 548K tokens indexed
- Tailwind: 235K+ tokens

## Best Practices

### Query Optimization

✅ **Do:**
```typescript
// Specific library name
resolve_library_id("next.js")

// Focused topic
get_library_docs(id, "app router file conventions", 5000)

// Organization + project
resolve_library_id("vercel next.js")
```

❌ **Don't:**
```typescript
// Too vague
resolve_library_id("ui library")

// Too broad
get_library_docs(id, "everything", 15000)

// Missing resolve step
get_library_docs("/some/library")  // Without resolving first
```

### Caching Strategy

```typescript
const cache = new Map();
const CACHE_TTL = 1000 * 60 * 60; // 1 hour

async function getCachedDocs(id, topic, tokens) {
  const key = `${id}:${topic}:${tokens}`;
  const cached = cache.get(key);
  
  if (cached && Date.now() - cached.ts < CACHE_TTL) {
    return cached.docs;
  }
  
  const docs = await get_library_docs(id, topic, tokens);
  cache.set(key, { docs, ts: Date.now() });
  return docs;
}
```

### Rate Limiting

```typescript
import pLimit from 'p-limit';

const limit = pLimit(3); // Max 3 concurrent requests

const results = await Promise.all(
  libraries.map(lib =>
    limit(() => get_library_docs(lib.id, "overview", 3000))
  )
);
```

## Troubleshooting

### TLS/Certificate Issues

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": [
        "-y",
        "--node-options=--experimental-fetch",
        "@upstash/context7-mcp"
      ]
    }
  }
}
```

### VM Module Issues

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": [
        "-y",
        "--node-options=--experimental-vm-modules",
        "@upstash/context7-mcp@1.0.6"
      ]
    }
  }
}
```

### Docker Issues

```dockerfile
FROM node:18-alpine
WORKDIR /app
RUN npm install -g @upstash/context7-mcp
CMD ["context7-mcp"]
```

## Advanced Usage

### Direct Library ID in Prompts

If you already know the library ID, include it in your prompt:

```
Implement authentication with Supabase.
Use library /supabase/supabase for API and docs.
```

The `/library/id` syntax tells the MCP server to skip resolve and go directly to fetching docs.

### HTTPS Proxy Support

Context7 respects standard proxy environment variables:

```bash
export https_proxy=http://proxy.company.com:8080
export HTTPS_PROXY=http://proxy.company.com:8080

# Then run MCP server
npx @upstash/context7-mcp
```

### Custom Headers

```json
{
  "mcpServers": {
    "context7": {
      "type": "http",
      "url": "https://mcp.context7.com/mcp",
      "headers": {
        "CONTEXT7_API_KEY": "ctx7sk_...",
        "X-Custom-Header": "value"
      }
    }
  }
}
```

## Library Statistics

- **Total Libraries**: 48,148+
- **Continuously Updated**: Auto-sync from source repos
- **Multi-Language Support**: Python, JavaScript, TypeScript, Go, Rust, Java, C#, PHP, Ruby, etc.
- **Source Types**: GitHub repos, npm packages, PyPI, official websites
- **Documentation Types**: README, API docs, guides, examples

## Related Resources

- **Website**: https://context7.com
- **GitHub**: https://github.com/upstash/context7
- **NPM**: https://www.npmjs.com/package/@upstash/context7-mcp
- **MCP Hub**: https://smithery.ai/server/@upstash/context7-mcp
- **Issues**: https://github.com/upstash/context7/issues

## Version History

- **Latest**: Check npm for current version
- **Stability**: Production-ready
- **Breaking Changes**: Check GitHub releases
- **Migration Guides**: See repository CHANGELOG
