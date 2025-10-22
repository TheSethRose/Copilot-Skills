---
description: Cloudflare developer platform - Workers, Pages, R2, D1, and global edge infrastructure
---

# Cloudflare

**Purpose**: Build serverless applications and secure infrastructure on Cloudflare's global edge network.

## When to Use This Skill

Use this skill when:
- Building Cloudflare Workers or Pages applications
- Working with Cloudflare APIs and SDKs
- Setting up DNS, security, or performance features
- Deploying edge functions or static sites
- Working with D1 (databases), R2 (storage), or Durable Objects
- Implementing Zero Trust security

**Keywords**: cloudflare, workers, pages, wrangler, edge computing, api, deployment, dns, security

## Quick Reference

### Create a Cloudflare Worker

```javascript
export default {
  fetch(request) {
    return new Response('Hello, world!');
  }
};
```

### Deploy with Wrangler

```bash
npm install -D wrangler
wrangler deploy
```

### Cloudflare Pages

```bash
wrangler pages deploy dist/
```

### D1 Database Query

```javascript
export default {
  async fetch(request, env) {
    const { results } = await env.DB.prepare(
      'SELECT * FROM users'
    ).all();
    return Response.json(results);
  }
};
```

### R2 Storage Upload

```javascript
export default {
  async fetch(request, env) {
    await env.BUCKET.put('file.txt', 'content');
    return new Response('Uploaded');
  }
};
```

## Core Products

### Compute
- **Workers** - Serverless JavaScript/WebAssembly at the edge
- **Pages** - Deploy static sites and functions
- **Durable Objects** - Persistent state for Workers

### Storage
- **R2** - S3-compatible object storage
- **D1** - Serverless SQL database
- **KV** - Distributed key-value storage

### Security & Network
- **Zero Trust** - Replace VPNs with policies
- **WAF** - Web Application Firewall
- **DDoS Protection** - Automatic protection
- **DNS** - Fast, secure DNS resolution

### AI & Performance
- **Workers AI** - Run ML models at the edge
- **Analytics** - Real-time analytics
- **Cache** - Global CDN caching

## Reference Documentation

Complete docs in `.github/copilot-skills/deployment/cloudflare/references/`:
- `getting-started.md` - Setup and quickstart
- `workers.md` - Workers development
- `pages.md` - Static site deployment
- `databases.md` - D1 and storage
- `security.md` - Zero Trust and WAF
- `api.md` - Complete API reference

## How to Use

1. **Ask about features**: "How do I use Cloudflare Workers?"
2. **Check patterns**: Look at code examples in references
3. **Search docs**: Browse reference files for specific topics
4. **Deploy**: Use Wrangler CLI commands shown in examples

## Common Workflows

### Setup Local Development

```bash
npm create cloudflare@latest my-app
cd my-app
npm run dev
```

### Deploy Worker

```bash
wrangler deploy
```

### Access Environment Variables

```javascript
export default {
  async fetch(request, env) {
    const apiKey = env.API_KEY;
    // Use your secret
  }
};
```

## Enterprise Features

- **Cloudflare for SaaS** - Multi-tenant hosting
- **Custom Domains** - White-label your app
- **Advanced Analytics** - Deep insights
- **Access Control** - Zero Trust policies

## Related Resources

- Official Site: https://cloudflare.com
- Developer Docs: https://developers.cloudflare.com
- Wrangler CLI: https://github.com/cloudflare/wrangler
- Community: https://community.cloudflare.com
