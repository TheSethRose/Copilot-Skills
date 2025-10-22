# Cloudflare Instructions

**Auto-loaded when**: `**/*.js, **/*.ts, **/*.tsx, **/*.jsx, **/*.toml, **/wrangler.toml`

## Default Behaviors

When working with Cloudflare code:

1. **Use Wrangler CLI** - The official tool for development
2. **TypeScript Recommended** - Type-safe development
3. **Environment Variables** - Use `wrangler.toml` for config
4. **Error Handling** - Always catch and handle errors
5. **Async/Await** - Workers are async by default

## Common Workflows

### Local Development

```bash
# Install Wrangler
npm install -D wrangler

# Create new project
npm create cloudflare@latest

# Local development server
npm run dev

# Deploy
wrangler deploy
```

### Worker Development

```javascript
export default {
  async fetch(request, env, ctx) {
    try {
      // Your code here
      return new Response('Success');
    } catch (error) {
      return new Response(`Error: ${error.message}`, { 
        status: 500 
      });
    }
  }
};
```

### Environment Configuration (wrangler.toml)

```toml
name = "my-worker"
type = "javascript"
account_id = "xxx"
workers_dev = true
route = "example.com/*"
zone_id = "xxx"

[env.production]
route = "example.com/*"

[build]
command = "npm run build"
cwd = "./src"
```

### Using D1 Database

```javascript
export default {
  async fetch(request, env) {
    const db = env.DB;
    
    // Query
    const { results } = await db
      .prepare('SELECT * FROM users WHERE id = ?')
      .bind(1)
      .all();
    
    // Insert
    await db
      .prepare('INSERT INTO users (name) VALUES (?)')
      .bind('John')
      .run();
    
    return Response.json(results);
  }
};
```

### Using R2 Storage

```javascript
export default {
  async fetch(request, env) {
    const bucket = env.MY_BUCKET;
    
    // Upload
    await bucket.put('path/file.txt', 'content');
    
    // Download
    const file = await bucket.get('path/file.txt');
    
    // Delete
    await bucket.delete('path/file.txt');
    
    // List
    const files = await bucket.list();
    
    return new Response('Done');
  }
};
```

### Using Durable Objects

```javascript
export class Counter {
  state: DurableObjectState;
  
  constructor(state: DurableObjectState) {
    this.state = state;
  }
  
  async fetch(request: Request) {
    let value = await this.state.storage.get('count') || 0;
    value++;
    await this.state.storage.put('count', value);
    return new Response(value.toString());
  }
}
```

### Scheduled Events (Cron)

```javascript
export default {
  async fetch(request) {
    return new Response('Hello');
  },
  
  async scheduled(event, env, ctx) {
    // Runs on schedule defined in wrangler.toml
    console.log('Scheduled event:', event.cron);
  }
};
```

## Quality Guidelines

### ✅ Do

- Use type definitions (TypeScript)
- Handle errors gracefully
- Return proper HTTP status codes
- Set appropriate headers
- Use environment variables for secrets
- Test locally before deploying
- Follow Cloudflare best practices
- Use KV for caching when possible

### ❌ Don't

- Hardcode secrets or API keys
- Ignore error handling
- Make blocking calls without timeout
- Deploy without testing
- Use deprecated APIs
- Ignore rate limits
- Block event handling

## Testing

```javascript
// Test with Vitest
import { describe, it, expect } from 'vitest';
import worker from './index.ts';

describe('Worker', () => {
  it('returns hello world', async () => {
    const response = await worker.fetch(
      new Request('http://localhost/'),
      { /* env */ }
    );
    expect(response.status).toBe(200);
  });
});
```

## Debugging

```bash
# Stream logs
wrangler tail

# Tail with filters
wrangler tail --format json --status ok

# Local debugging
npm run dev
# Then check browser console
```

## Performance Tips

1. **Minimize CPU time** - Keep functions fast
2. **Use caching** - Leverage KV and Cache API
3. **Stream responses** - For large data
4. **Batch operations** - Reduce API calls
5. **Monitor metrics** - Use Analytics

## Deployment

```bash
# Deploy to production
wrangler deploy

# Deploy specific environment
wrangler deploy --env production

# Rollback
wrangler rollback
```

## Reference Documentation

Complete documentation available in:
- `.github/copilot-skills/deployment/cloudflare/references/` - Organized by topic
- https://developers.cloudflare.com/ - Official docs
- https://developers.cloudflare.com/workers/ - Workers guide

## Related Skills

- **Git Ops** - Version control for Cloudflare projects
- **TypeScript** - Type-safe development
- **JavaScript** - Core language
