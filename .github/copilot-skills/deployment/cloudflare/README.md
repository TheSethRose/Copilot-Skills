# Cloudflare - Quick Reference

**Official Docs**: https://developers.cloudflare.com/

## Product Categories

### Compute
- **Workers** - Serverless edge computing
- **Pages** - Jamstack hosting
- **Durable Objects** - Persistent state
- **Containers** - Dockerized Workers

### Storage & Databases
- **R2** - Object storage (S3-compatible)
- **D1** - Serverless SQLite database
- **KV** - Distributed key-value store
- **Queues** - Message queue service

### Security
- **Cloudflare One / Zero Trust** - Identity and access
- **WAF** - Web Application Firewall
- **DDoS Protection** - Layer 3-7 protection
- **API Shield** - API security
- **Bot Management** - Bot detection

### Networking
- **DNS** - Authoritative DNS
- **Load Balancing** - Global load balancing
- **Argo Smart Routing** - Optimized routing
- **Tunnel** - Secure connectivity

### AI & Data
- **Workers AI** - Edge ML inference
- **AI Gateway** - AI application platform
- **Vectorize** - Vector embeddings
- **Hyperdrive** - Database acceleration

### Performance & Analytics
- **Cache** - Global CDN caching
- **Analytics** - Real-time insights
- **Web Analytics** - Web traffic analytics
- **Speed Test** - Performance testing

## Common Tasks

### Get Started
1. Sign up at https://dash.cloudflare.com/
2. Create a Cloudflare account
3. Add your domain
4. Install Wrangler: `npm install -D wrangler`

### Create a Worker
```bash
npm create cloudflare@latest my-app
cd my-app
npm run dev
npm run deploy
```

### Deploy Static Site (Pages)
```bash
# Connect GitHub repo or
wrangler pages deploy dist/
```

### Access Dashboard
https://dash.cloudflare.com/

### View Documentation
https://developers.cloudflare.com/

## Key Endpoints

- **Workers Dashboard**: https://dash.cloudflare.com/?to=/:account/workers/view
- **D1 Database**: https://dash.cloudflare.com/?to=/:account/d1/database/
- **R2 Storage**: https://dash.cloudflare.com/?to=/:account/r2/buckets/
- **Zero Trust**: https://one.dash.cloudflare.com/

## Environment Setup

```toml
# wrangler.toml
name = "my-app"
type = "javascript"
account_id = "your_account_id"
workers_dev = true
compatibility_date = "2024-10-21"

[env.development]
routes = [{ pattern = "dev.example.com/*", zone_name = "example.com" }]

[env.production]
routes = [{ pattern = "example.com/*", zone_name = "example.com" }]
```

## CLI Commands

```bash
# Authentication
wrangler login
wrangler logout

# Development
wrangler dev          # Local server
wrangler tail         # Stream logs
wrangler test         # Run tests

# Deployment
wrangler deploy       # Deploy worker
wrangler deploy --env production

# Database
wrangler d1 create my-db
wrangler d1 list
wrangler d1 execute my-db --command "SELECT * FROM users"

# R2
wrangler r2 bucket create my-bucket
wrangler r2 bucket list

# KV
wrangler kv:key list --namespace-id=abc123
wrangler kv:key put key value --namespace-id=abc123

# Pages
wrangler pages project create my-project
wrangler pages deploy dist/
wrangler pages rollback
```

## Resources

- **Docs**: https://developers.cloudflare.com/
- **API Docs**: https://developers.cloudflare.com/api/
- **Community**: https://community.cloudflare.com/
- **Status**: https://www.cloudflarestatus.com/
- **GitHub**: https://github.com/cloudflare
- **Blog**: https://blog.cloudflare.com/
