# Copilot Instructions

⚡ **CRITICAL: For ANY file operation (C.R.U.D., search, grep, etc.), ALWAYS use Kit first:**

**Before reading, searching, or modifying ANY file:**
```bash
# Find what you're looking for
kit symbols . --format json | jq '.[] | select(.name == "FUNCTION_NAME")'  # Find function
kit grep . "SEARCH_TERM" --directory "src"                                # Search in directory
kit usages . "SYMBOL_NAME"                                               # Find usages

# Get file context before editing
kit context . src/file.ts 42                                             # Get code around line
kit chunk-symbols . src/file.ts                                          # Split file by functions

# Understand related code
kit file-tree . --path src/pages                                         # View structure
cat .kit-analysis/summary.md                                             # See most complex files
```

**Why:** Kit is 25-36x faster than grep, excludes node_modules automatically, and gives structured output.

**This is MANDATORY for every task.** Do not skip Kit.

---

## Orchestration Default

- Treat every user query as an orchestration task: decide which specialist agents in `/.github/agents/` to involve before replying.
- Prefer breaking work into targeted subagents when tasks can be split; call them via the `runSubagent` tool and merge their outputs into one concise answer.
- If no suitable agent exists or delegation adds no value, proceed directly but mention that delegation was considered.
- Keep added narration minimal and honor all existing workflows (Kit-first, patching rules, testing, quirks).

## Project Overview

**DiscoverAnnaTX** is a production-ready local business directory with AI-powered business review generation. It's a full-stack TypeScript application combining React frontend with Node.js/Express backend, featuring Redis-backed async job processing for website scraping and AI analysis.

**Current Phase:** AI review system operational with BullMQ job queue, Puppeteer web scraping, OpenRouter Claude/Gemini AI integration, and Stripe monetization (3 revenue streams: Category Sponsorship $299.99/mo, 50 Lead Credits $99.99, 10 Lead Credits $49.99)

## Technology Stack

**Frontend:** React 18.3, TypeScript 5.6, Vite 6, Tailwind CSS v4, Radix UI (23+ components)
**Backend:** Node.js (Bun), Express, Better Auth, Prisma 6.19.0, PostgreSQL 16
**AI Processing:** OpenRouter API (Gemini 2.5 Flash, Sherlock), OpenAI SDK v6.8.1, Puppeteer 24.29.1, JSDOM
**Job Queue:** BullMQ 5.63.2 (Redis-backed async), ioredis 5.8.2, Redis persistence (AOF)
**Payments:** Stripe (checkout sessions, webhooks, subscriptions)
**Utilities:** React Hook Form, Zod validation, React Router v6, Lucide icons, Turndown (HTML→Markdown)

## Project Structure

```
src/                          # Frontend (React)
├── components/               # Reusable UI (Button, Card, etc)
├── pages/                    # Route components
├── config/                   # anna.config.ts - directory branding
├── contexts/                 # AuthContext for global state
├── hooks/                    # useIsMobile, custom hooks
├── lib/                      # database-client.ts (API), utils.ts

server/                       # Backend (Express + BullMQ)
├── index.ts                  # Express app, routes
├── auth.ts                   # Better Auth config
├── prisma.ts                 # Prisma client
├── services/
│   ├── review-worker.ts      # BullMQ Worker (async review processing)
│   ├── website-scraper.ts    # Puppeteer + AI extraction
│   └── listing-reviewer.ts   # Nightly cron job
├── review/
│   ├── buildReview.ts        # Change detection + review building
│   ├── normalizeScrapedData.ts # Data validation & formatting
│   └── sourceTrackingUtils.ts  # Cross-page data tracking
├── lib/
│   ├── apply-feedback-transform.ts # Claude field transformation
│   ├── stripe-helpers.ts     # Stripe integration
├── jobs/
│   ├── queue-config.ts       # Redis connection config
│   ├── review-queue.ts       # BullMQ Queue
│   └── verification-job.ts   # Expiry cleanup
└── review-worker-entrypoint.ts

prisma/
├── schema.prisma             # Database schema
├── migrations/               # Migration files
└── seed.ts                   # Development seeding
```

## Development Workflows

**Core Commands:**
- `bun run dev` - Start Vite frontend (localhost:5173) with HMR
- `bun run dev:server` - Start Express backend (localhost:3010)
- `bun run dev:all` - Run frontend + backend concurrently
- `bun run server/review-worker-entrypoint.ts` - Start Review Worker (for AI processing)
- `bun run build` - TypeScript check + production build
- `bun run lint` - Run ESLint
- `bun run build` - TypeScript check + production build
- `bun clean` - Remove node_modules and cache

**CRUD & Feature Implementation Tools (Use These Commands):**

**Phase 1: Research (Before Coding)**
```bash
kit symbols . --format json | jq '.[] | select(.name == "buildReview")'  # Find symbol
kit usages . "buildReview"                                              # See usage impact
kit grep . "review" --directory "server"                               # Find similar code
cat .kit-analysis/summary.md                                           # Identify risk areas
```

**Phase 2: Understand (Get Context)**
```bash
kit context . src/file.ts 42                                           # Code around line
kit chunk-symbols . server/services/website-scraper.ts                 # Split into functions
kit file-tree . --path src/pages                                       # View structure
```

**Phase 3: Implement (Check Patterns)**
```bash
kit symbols . --format json | jq '.[] | select(.kind == "function")'   # Get function patterns
kit grep . "async function" --pattern "*.ts" --directory "server"      # Find similar style
```

**Phase 4: Verify (After Editing)**
```bash
kit grep . "YOUR_NEW_FUNCTION"                                         # Confirm it exists
kit grep . "TODO|FIXME" --directory "src"                             # Check for stubs
```

**Refresh Index:**
```bash
uv run --with cased-kit python .github/scripts/kit/bootstrap.py        # After major changes
```

**Database Commands:**
- `bun run prisma:migrate` - Create/run migrations
- `bun run prisma:seed` - Seed with development data
- `bun run prisma:studio` - Prisma Studio GUI (localhost:5555)
- `bun run prisma:reset` - Drop + recreate database

**Docker & Services:**
- `docker-compose up -d` - Start Redis + PostgreSQL
- `docker-compose logs -f redis` - Monitor Redis
- `docker exec -it discover-redis redis-cli` - Redis CLI

**Copy & Content Generation:**
- `bun scripts/utils/copywriter.ts --query "your request"` - Generate optimized UI copy
- See `docs/copywriter-cli.md` for detailed usage and examples
- Use this for: CTAs, buttons, headers, error messages, empty states, and any UI copy
- The tool is tuned specifically for local business directories with UX best practices built-in

**AI Review Processing:**
- Queue single review: `curl -X POST http://localhost:3010/api/reviews/scan/{businessId}`
- Bulk queue: `curl -X POST http://localhost:3010/api/reviews/queue-all`
- Monitor in admin dashboard "AI Reviews" tab

**Stripe Setup (Local):**
- Set test keys in `.env`: `STRIPE_SECRET_KEY`, `STRIPE_PRICE_*` IDs
- Use Stripe test card: `4242 4242 4242 4242` (any future expiry, any CVC)
- Optional: `stripe listen --forward-to localhost:3010/api/stripe` for webhooks

**AI Configuration:**
- `OPENROUTER_API_KEY=sk-or-v1-...` - OpenRouter API key
- `OPENROUTER_MODEL=google/gemini-2.5-flash` - Primary AI model
- Fallback: `google/gemini-2.5-flash`

## Code Patterns & Conventions

**Naming:**
- Files: kebab-case (e.g., `ListingViewPage.tsx`, `listing-location-map.tsx`)
- Components/Classes: PascalCase exports
- Functions/variables: camelCase
- Database fields: snake_case

**Component Pattern:**
```typescript
interface ComponentProps {
  prop1: string;
  prop2?: number;
}

export const Component: React.FC<ComponentProps> = ({ prop1, prop2 }) => {
  return <div>{/* content */}</div>;
};
```

**API Calls:**
- Frontend uses `db.getBusinesses()`, `db.loginUser()` from `src/lib/database-client.ts`
- These call backend REST endpoints in `server/index.ts`
- TypeScript interfaces in `database-client.ts` define all data shapes

**Form Validation:**
- React Hook Form for state management
- Zod schemas for validation (`zod` already imported in contexts)

// ...existing code...
// ...existing code...
**Styling:**
- Tailwind CSS v4 utility classes only
- Design tokens in `src/index.css` (colors, fonts, animations)
- Fonts: Poppins (headings), Inter (body)
- Colors: Primary purple, Secondary amber, Accent teal

## Frontend Design & Best Practices

We follow a Component-Driven Development (CDD) approach using the **Shadcn/ui** philosophy (Radix UI Primitives + Tailwind CSS).

**Key Principles:**
- **Component Ownership:** We own our component code (copied into `src/components/ui`), allowing full control and customization.
- **Mobile-First:** Design and develop for mobile screens first, then scale up.
- **Accessibility (A11y):** All components must be accessible (keyboard nav, ARIA roles, contrast). We use Radix primitives to ensure this.
- **Styling:** Use Tailwind utility classes. Avoid "class hell" by using `cn()` utility for conditional classes and component composition.

For a comprehensive guide on our frontend architecture, styling, UX principles, and accessibility standards, please refer to:
**[Frontend Design Overview](../docs/developer/frontend-design-overview.md)**

## Codebase Quirks & Important Notes
// ...existing code...

Before making changes to any file, check for "Note:" comments in the code. These document critical implementation details and quirks that affect how the code should be modified. Key quirks include:

### Frontend Quirks

1. **Verification Status (infoVerified) is Admin-Only**
   - Files: `src/pages/ListingViewPage.tsx`, `src/pages/EditListingPage.tsx`, `src/pages/DashboardPage.tsx`, `src/components/ListingForm.tsx`
   - Quirk: Business verification status (`infoVerified` field) is managed exclusively through admin endpoints, not through the listing form or user-facing toggles.
   - Impact: Never add verification toggle to the business listing form or allow users to change this field directly.
   - Implementation: Always use dedicated admin endpoints to set/unset verification status.

2. **City API Accepts State Code, Not UUID**
   - File: `src/components/admin/modals/AddCityModal.tsx`
   - Quirk: The API is designed to accept stateId (UUID format), but currently uses state code as a workaround.
   - Impact: When integrating with real backend, update this to send proper UUID for state.

### Backend Quirks

3. **Route Registration Order Matters**
   - File: `server/index.ts`
   - Quirk: Any special/named routes under `/api/businesses` (like `/api/businesses/search`) must be registered BEFORE the `/api/businesses/:id` dynamic route.
   - Impact: If not ordered correctly, special routes get captured by the `:id` route handler.
   - Implementation: Always register specific routes first, dynamic routes last.

4. **Scraped Data is Already Flattened**
   - File: `server/review/buildReview.ts`
   - Quirk: Scraped data from the website scraper is already a flat `ScrapedData` object, not source-tracked in the flat structure.
   - Impact: When processing scraper results, don't expect nested source tracking. Cross-page source metadata is handled separately in `sourceTrackedField`.
   - Implementation: Work directly with the flat structure. Access source tracking via `sourceTrackedField` interface separately.

### AI & Async Processing Quirks

5. **OpenRouter API Used, Not Direct Anthropic Claude**
   - File: `server/lib/apply-feedback-transform.ts`
   - Quirk: The system uses OpenRouter API (third-party proxy) instead of Anthropic SDK directly.
   - AI Providers: Primary = `google/gemini-2.5-flash-lite`, Fallback = `openrouter/sherlock-think-alpha`.
   - Impact: Must set `OPENROUTER_API_KEY` (not Anthropic key), use OpenRouter-compatible OpenAI SDK.
   - Implementation: Environment variable is `OPENROUTER_API_KEY`. SDK: OpenAI v6.8.1 with `baseURL=https://openrouter.ai/api/v1`.

6. **BullMQ Worker Concurrency Limit**
   - File: `server/services/review-worker.ts`
   - Quirk: Worker processes max 3 reviews simultaneously per instance.
   - Impact: If you need higher throughput, run multiple worker instances (via Docker Compose scaling).
   - Implementation: Concurrency set to 3. Each job locks for 2 minutes max. Failed jobs retry 3x with 5s delay.

7. **Review Reroll Has Two Mechanisms**
   - Files: `server/index.ts` - `/api/reviews/:id/reroll-field` vs `/api/reviews/:id/reroll-change`
   - Quirk: `reroll-field` transforms field value directly; `reroll-change` requeues full scrape with feedback metadata.
   - Impact: Use `reroll-field` for quick UI feedback transformations, `reroll-change` for website re-scraping.
   - Implementation: `reroll-field` is synchronous (immediate), `reroll-change` is async (full queue job).

8. **Feedback Metadata Stored in rawJson**
   - File: `server/services/review-worker.ts`
   - Quirk: User feedback for reroll operations stored in `listing_review.rawJson.rerollMetadata`.
   - Impact: When rebuilding review, worker checks for rerollMetadata and applies feedback to target field.
   - Implementation: Field: 'fieldName', userFeedback: 'instruction', requestedBy: 'userId', requestedAt: timestamp.

### Database Quirks

9. **Seed Script Silently Handles Duplicate Users**
   - Files: `prisma/seed.ts`, `scraper-worker/prisma/seed.ts`
   - Quirk: The seed script may encounter existing users and silently skips them instead of failing.
   - Impact: Running seed multiple times is safe. Duplicates are handled gracefully.
   - Implementation: Don't add error handling for "user already exists" when running seed.

### Build & Configuration Quirks

10. **Bun 1.3.x Uses Text Format Lock File**
    - Files: `bunfig.toml`, `Dockerfile`
    - Quirk: Bun version 1.3.x defaults to text-based bun.lock format (not binary).
    - Impact: The lock file is human-readable in version control.
    - Implementation: No special handling needed. Document for team members used to binary lock files.

11. **Redis Connection Must Match Environment**
    - File: `server/jobs/queue-config.ts`
    - Quirk: Redis connection reads from environment: REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, REDIS_DB.
    - Impact: Local dev uses `localhost`, Docker uses `redis` (service name).
    - Implementation: Ensure REDIS_HOST is set correctly before starting worker. Default fallback: redis:6379

## Directory Configuration

Located in `src/config/anna.config.ts`:
- Brand name, logo, accent color
- Categories taxonomy (15+ default)
- Custom fields schema (text, select, number, URL, phone, email, textarea)
- Site branding and metadata

To create a new directory: `pnpm run new:directory`

## Routing & Pages

- `/` → **HomePage** (business search & featured)
- `/login` → **LoginPage**
- `/register` → **RegisterPage**
- `/submit-business` → **SubmitBusinessPage**
- `/admin` → **AdminDashboard** (submissions, business management)
- `/about` → **AboutPage**
- `/contact` → **ContactPage**

## Component Responsibilities

**Pages:**
- **HomePage:** Search, featured businesses, category/city filters, pagination
- **LoginPage/RegisterPage:** Email/password authentication
- **SubmitBusinessPage:** Business submission form with Zod validation
- **AdminDashboard:** Manage submissions (approve/reject), toggle business featured/verified status
- **AboutPage/ContactPage:** Static informational pages

**Components:**
- **Navbar:** Navigation with auth state display
- **FilterSidebar:** Category and state/city filter UI
- **BusinessCard:** Display individual business (rating, verified badge, map link)
- **FeaturedBanner:** Rotating featured business banner
- **Button/Input:** Styled form elements

**Contexts:**
- **AuthContext:** Global user state (user, login(), logout(), register())

## Database Schema (Key Tables)

**Business** - Listings (name, phone, email, address, category, featured, verified, etc)
- `verifiedUntil` - Verified Badge subscription expiry
- `featuredUntil` - Boosted Placement expiry (30 days)
- `sponsor` - Boolean for Sponsor Slot status

**User** - Admin/regular users (email, password, role)

**Review** - User reviews for businesses
**ListingReview** - Staging area for scraped data requiring approval
**BusinessSubmission** - User-submitted business listings pending approval
**City/State/Category** - Taxonomy and location data

**StripeSubscription** - Active subscriptions (kind, status, listingId)

**StripeEvent** - Webhook events for idempotent processing

See `prisma/schema.prisma` for full schema.

## AI Review System

**Non-Blocking Async Architecture:**
- Admin queues reviews via `/api/reviews/scan/:businessId` or `/api/reviews/queue-all`
- API creates database row + enqueues BullMQ job, returns immediately
- Worker processes in background (concurrency: 3 per instance)
- Results appear in admin dashboard when ready (status='ready')

**Review Processing Pipeline:**
1. **Website Scraping** - Puppeteer visits main + identified pages
2. **AI Extraction** - Vision + text extraction (email, phone, name, description, category)
3. **Data Normalization** - Format validation, field cleaning
4. **Change Detection** - Unified builder compares current vs scraped, generates change IDs
5. **Confidence Scoring** - Per-field confidence (0-100) based on data quality
6. **Feedback Filtering** - Removes user-rejected suggestions from rejectedChange table
7. **Database Update** - Stores review with status='ready', changes, rawJson, normalizedJson

**Key Files:**
- `server/services/review-worker.ts` - BullMQ worker + async processing
- `server/services/website-scraper.ts` - Puppeteer + 3 AI extraction methods
- `server/review/buildReview.ts` - Unified change detection & review building
- `server/lib/apply-feedback-transform.ts` - Claude field transformation (reroll-field)

**Feedback Mechanisms:**
- `reroll-field` (POST) - Transform ONE field value with user feedback (synchronous)
- `reroll-change` (POST) - Requeue for full scrape with feedback metadata (async)

## API Endpoints (Backend)

**Listings:**
- `GET /api/businesses` - Search/filter with pagination
- `GET /api/businesses/:id` - Get single listing
- `POST /api/businesses` - Create listing
- `PATCH /api/businesses/:id` - Update listing
- `DELETE /api/businesses/:id` - Delete listing

**AI Reviews:**
- `POST /api/reviews/scan/:businessId` - Queue single review scan
- `POST /api/reviews/queue-all` - Bulk queue (30+ days old)
- `GET /api/reviews/admin/all` - Get all reviews with filters
- `GET /api/reviews/admin/stats` - Review statistics
- `POST /api/reviews/:id/approve` - Approve all changes
- `POST /api/reviews/:id/reject` - Reject all changes
- `POST /api/reviews/:id/approve-change` - Approve single field
- `POST /api/reviews/:id/reject-change` - Reject single field
- `POST /api/reviews/:id/reroll-field` - Transform field with feedback
- `POST /api/reviews/:id/reroll-change` - Requeue with feedback metadata
- `GET /api/reviews/:businessId/latest` - Get latest review for business

**Billing/Stripe:**
- `POST /api/billing/checkout` - Create Stripe checkout session
- `GET /api/billing/success` - Sync subscription after checkout
- `GET /api/billing/subscriptions` - List user's active subscriptions
- `POST /api/billing/customer-portal` - Stripe customer portal link
- `POST /api/stripe` - Webhook handler (requires signature)
- `POST /api/billing/cron` - Daily cron job for expiration

**Analytics:**
- `POST /api/views/pv` - Track listing views

## Stripe Integration

**Revenue Streams:**
1. **Verified Badge** ($99/year) - Sets `verifiedUntil` timestamp, enables boosted/sponsor tiers
2. **Boosted Placement** ($79/month) - Sets `featuredUntil` for 30-day active period, max 3 per (city, category)
3. **Sponsor Slot** ($300/month) - Sets `sponsor` flag, exclusive 1 per (city, category)

**Webhook Events Handled:**
- `checkout.session.completed` - Creates subscription in database
- `customer.subscription.updated` - Updates expiry dates
- `customer.subscription.deleted` - Clears subscription flags

**Key Functions** (`server/lib/stripe-helpers.ts`):
- `applyEffect(kind, listingId)` - Set Business flags when subscription starts
- `clearEffect(kind, listingId)` - Remove flags when subscription ends
- `expireFeaturedListings()` - Cron job to clear expired featured flags

## Multi-City Architecture

Subdomains route to different cities: `{city}-{state}.localhost:5173`
- Parse via `parseSubdomain()` in `src/lib/utils.ts`
- All listings filtered by active city context
- Same codebase runs all cities

## Authentication

**Better Auth Configuration:**
- Session-based authentication via `better-auth`
- Default demo: `admin@sethrose.dev` / `admin123`
- Role-based access: 'admin' vs 'user'
- Global auth state in AuthContext

## Type Safety

- TypeScript strict mode enabled
- Interfaces defined in `src/lib/database-client.ts`
- All API responses typed
- Zod for runtime validation on forms
- No `any` types without justification

## Quality Standards

- **Linting:** ESLint must pass (`pnpm run lint`)
- **Type Checking:** TypeScript check before build (`pnpm run build`)
- **Code Style:** Prettier config in `eslint.config.js`
- **Accessibility:** Radix UI for semantic HTML + ARIA
- **Performance:** Lazy routes, optimized images, Vite HMR

## Common Tasks

**Add New Listing Field:**
1. Add to schema in `prisma/schema.prisma`
2. Run `pnpm run prisma:migrate`
3. Update Business interface in `src/lib/database-client.ts`
4. Update form in submission/edit pages

**Add New Business Category:**
1. Update `src/config/anna.config.ts` categories array
2. Seed database: `pnpm run prisma:seed`

**Debug Database:**
1. `pnpm run prisma:studio` opens GUI at localhost:5555
2. View/edit data directly

**Deploy:**
1. Build: `pnpm run build:prod`
2. Start server: `pnpm run start:server`
3. Frontend: Vite static output in `dist/`

## Key Utilities

**src/lib/utils.ts:**
- `cn()` - Tailwind class merger
- `parseSubdomain()` - Extract city/state
- `getCurrentCity()` - Get active city context
- `formatPhoneNumber()`, `truncateText()` - Text formatting
- `isValidEmail()`, `isValidPhone()` - Validation
- `debounce()` - Search input debouncing

## External Services

- **Google Maps** - API via `@googlemaps/js-api-loader` (embedded in Location card)
- **Stripe** - Payments via `stripe` SDK
- **Better Auth** - Authentication library

## Environment Variables (.env)

```bash
# Database
DATABASE_URL=postgresql://...

# Redis & BullMQ Job Queue
REDIS_HOST=redis                # Docker: "redis", Local: "localhost"
REDIS_PORT=6379
REDIS_PASSWORD=                 # Optional
REDIS_DB=0

# AI Configuration (OpenRouter)
OPENROUTER_API_KEY=sk-or-v1-...
OPENROUTER_MODEL=google/gemini-2.5-flash

# Stripe (test mode during dev)
STRIPE_SECRET_KEY=sk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...
STRIPE_PRICE_VERIFIED=price_...
STRIPE_PRICE_BOOST=price_...
STRIPE_PRICE_SPONSOR=price_...

# Google Maps
VITE_GOOGLE_MAPS_API_KEY=...

# App URLs
VITE_API_URL=http://localhost:3010
APP_URL=http://localhost:5173
```

## Debugging Tips

**HMR Issues:**
- Restart dev server: `bun run dev`

**TypeScript Errors:**
- Run `bun run build` to check compilation
- ESLint catches type issues: `bun run lint`

**Cache/Build Issues:**
```bash
bun clean
bun install
bun run build
```

## Next Steps

1. **Setup:** `bun install` to install dependencies
2. **Database:** `docker-compose up -d` for PostgreSQL + Redis
3. **Migrations:** `bun run prisma:migrate` to run migrations
4. **Seeding:** `bun run prisma:seed` for development data
5. **Development:** `bun run dev:all` (both frontend + backend)
6. **Environment:** Set `.env` with:
   - `OPENROUTER_API_KEY=sk-or-v1-...` for AI features
   - `REDIS_HOST=redis` for Docker (or `localhost` for local Redis)
   - Stripe test keys if testing payments
7. **Kit Analysis:** `uv run --with cased-kit python .github/scripts/kit/bootstrap.py` (auto-loads codebase index for LLM context)
8. **Redis:** Verify `docker-compose` includes Redis service for BullMQ
9. **Stripe:** Create test products in Stripe Dashboard for 3 revenue streams

## Kit Integration for LLM Context

Kit provides intelligent code analysis infrastructure for Claude and other LLMs:

**How It Works:**
1. `.kit-analysis/` directory contains pre-computed symbol index, file tree, and summary
2. `.github/instructions/kit-analysis.instructions.md` auto-loads this data for LLMs
3. When you ask Claude questions about the codebase, it reads the cached data first for instant symbol lookups
4. Result: **25-36x faster code understanding** with accurate file locations and relationships

**Key Files for LLM Usage:**
- `.kit-analysis/symbols.json` - When asking "Where is function X?", LLM checks this first
- `.kit-analysis/file_tree.json` - For project structure questions
- `.kit-analysis/summary.md` - Statistics on complex/frequently-used files

**Refresh Analysis When:**
- Adding many new functions/classes (>50 symbols)
- Major refactoring or restructuring
- Weekly maintenance
- After merging large PRs

```bash
uv run --with cased-kit python .github/scripts/kit/bootstrap.py
```
