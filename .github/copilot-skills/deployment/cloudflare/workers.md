# Cloudflare Workers - Complete Guide

## Overview

Cloudflare Workers is a serverless platform that runs JavaScript at the edge on Cloudflare's global network.

**Getting Started**: https://developers.cloudflare.com/workers/get-started/

## Installation & Setup

```bash
# Install Wrangler CLI
npm install -D wrangler

# Login
wrangler login

# Create new project
npm create cloudflare@latest my-worker
cd my-worker

# Start development
npm run dev

# Deploy
wrangler deploy
```

## Basic Worker

```javascript
// index.js
export default {
  fetch(request) {
    return new Response('Hello, Worker!');
  }
};
```

## TypeScript Worker

```typescript
// src/index.ts
interface Env {
  DB: D1Database;
  BUCKET: R2Bucket;
  API_KEY: string;
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    try {
      const url = new URL(request.url);
      
      if (url.pathname === '/api/data') {
        const { results } = await env.DB
          .prepare('SELECT * FROM data')
          .all();
        return Response.json(results);
      }
      
      return new Response('Not Found', { status: 404 });
    } catch (error) {
      return new Response(`Error: ${error}`, { status: 500 });
    }
  }
};
```

## Routing & Matching

```javascript
export default {
  async fetch(request) {
    const url = new URL(request.url);
    const path = url.pathname;

    // Route by path
    if (path === '/api/users') {
      return handleUsers(request);
    }
    
    // Route by method
    if (request.method === 'POST') {
      return handlePost(request);
    }
    
    // Route by header
    if (request.headers.get('X-Custom-Header')) {
      return new Response('Custom header found');
    }
    
    return new Response('Not Found', { status: 404 });
  }
};

async function handleUsers(request) {
  return Response.json({ users: [] });
}

async function handlePost(request) {
  const data = await request.json();
  return Response.json({ received: data });
}
```

## Environment Variables & Secrets

```toml
# wrangler.toml
name = "my-worker"
type = "javascript"

[env.development]
vars = { ENVIRONMENT = "development" }

[env.production]
vars = { ENVIRONMENT = "production" }
```

```javascript
export default {
  async fetch(request, env) {
    const apiKey = env.API_KEY;
    const environment = env.ENVIRONMENT;
    return new Response(`Environment: ${environment}`);
  }
};
```

### Set Secrets

```bash
wrangler secret put API_KEY
# Paste your API key when prompted

wrangler secret put --env production API_KEY
```

## Database Integration (D1)

```javascript
export default {
  async fetch(request, env) {
    const db = env.DB;

    // Query
    const { results } = await db
      .prepare('SELECT * FROM users WHERE id = ?1')
      .bind(123)
      .all();

    // Insert
    const insert = await db
      .prepare('INSERT INTO users (name, email) VALUES (?1, ?2)')
      .bind('John', 'john@example.com')
      .run();

    // Update
    await db
      .prepare('UPDATE users SET name = ?1 WHERE id = ?2')
      .bind('Jane', 123)
      .run();

    // Delete
    await db
      .prepare('DELETE FROM users WHERE id = ?1')
      .bind(123)
      .run();

    return Response.json(results);
  }
};
```

## Object Storage (R2)

```javascript
export default {
  async fetch(request, env) {
    const bucket = env.MY_BUCKET;

    // Upload
    await bucket.put('path/to/file.txt', 'content');
    await bucket.put('large.bin', largeBuffer, {
      customMetadata: { author: 'me' }
    });

    // Download
    const object = await bucket.get('path/to/file.txt');
    const text = await object.text();

    // List
    const listed = await bucket.list({ prefix: 'images/' });
    listed.objects.forEach(obj => console.log(obj.key));

    // Delete
    await bucket.delete('path/to/file.txt');

    return new Response('Done');
  }
};
```

## Key-Value Store (KV)

```javascript
export default {
  async fetch(request, env) {
    const kv = env.MY_KV;

    // Set
    await kv.put('key', 'value');
    await kv.put('cache', JSON.stringify(data), {
      expirationTtl: 3600 // 1 hour
    });

    // Get
    const value = await kv.get('key');
    const data = JSON.parse(await kv.get('cache'));

    // Delete
    await kv.delete('key');

    // List
    const list = await kv.list({ prefix: 'user:' });

    return Response.json({ value });
  }
};
```

## Request/Response Handling

```javascript
export default {
  async fetch(request) {
    // Read request body
    const json = await request.json();
    const text = await request.text();
    const buffer = await request.arrayBuffer();
    const formData = await request.formData();

    // Response with headers
    return new Response('Hello', {
      status: 200,
      headers: {
        'Content-Type': 'text/plain',
        'Cache-Control': 'max-age=3600',
        'X-Custom-Header': 'value'
      }
    });
  }
};
```

## Error Handling

```javascript
export default {
  async fetch(request, env) {
    try {
      const result = await fetch('https://api.example.com/data');
      
      if (!result.ok) {
        throw new Error(`API error: ${result.status}`);
      }
      
      return result;
    } catch (error) {
      console.error('Worker error:', error);
      
      return new Response(
        JSON.stringify({ error: error.message }),
        { 
          status: 500,
          headers: { 'Content-Type': 'application/json' }
        }
      );
    }
  }
};
```

## Scheduled Events (Cron)

```toml
# wrangler.toml
[triggers]
crons = ["0 0 * * *"]  # Daily at midnight UTC
```

```javascript
export default {
  async fetch(request) {
    return new Response('Hello');
  },

  async scheduled(event, env, ctx) {
    console.log('Running scheduled event');
    
    // Do background work
    ctx.waitUntil(
      fetch('https://example.com/webhook')
    );
  }
};
```

## Reference

- **API Reference**: https://developers.cloudflare.com/workers/runtime/apis/
- **Best Practices**: https://developers.cloudflare.com/workers/platform/limits/
- **Examples**: https://github.com/cloudflare/worker-examples
