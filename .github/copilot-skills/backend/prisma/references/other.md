# Prisma - Other

**Pages**: 103

---

## 2 docs tagged with "deployment" | Prisma Documentation

**URL**: https://www.prisma.io/docs/tags/deployment

**Contents**:
- 2 docs tagged with "deployment"
- Guides
- Migrate data using the expand and contract pattern

Welcome to the Guides section! Here you'll find practical, step-by-step guides to help you accomplish specific tasks with Prisma products, including Prisma ORM, Prisma Accelerate, Prisma Postgres, and more.

Learn how to perform data migrations using the expand and contract pattern with Prisma ORM

---

## 2 docs tagged with "migration" | Prisma Documentation

**URL**: https://www.prisma.io/docs/tags/migration

**Contents**:
- 2 docs tagged with "migration"
- Guides
- Migrate data using the expand and contract pattern

Welcome to the Guides section! Here you'll find practical, step-by-step guides to help you accomplish specific tasks with Prisma products, including Prisma ORM, Prisma Accelerate, Prisma Postgres, and more.

Learn how to perform data migrations using the expand and contract pattern with Prisma ORM

---

## 3 docs tagged with "Monorepo" | Prisma Documentation

**URL**: https://www.prisma.io/docs/tags/monorepo

**Contents**:
- 3 docs tagged with "Monorepo"
- Comprehensive Guide to Using Prisma ORM with Next.js
- How to use Prisma ORM in a pnpm workspaces monorepo
- How to use Prisma ORM with Turborepo

Learn best practices, monorepo strategies, and dynamic usage techniques for Prisma ORM in Next.js applications.

Learn step-by-step how to integrate Prisma ORM in a pnpm workspaces monorepo to build scalable and modular applications efficiently.

Learn step-by-step how to integrate Prisma ORM with Turborepo to build modular, scalable monorepo architectures efficiently.

---

## 3 docs tagged with "Vercel" | Prisma Documentation

**URL**: https://www.prisma.io/docs/tags/vercel

**Contents**:
- 3 docs tagged with "Vercel"
- How to use Prisma ORM with Next.js
- How to use Prisma ORM with Nuxt
- How to use Prisma ORM with Turborepo

Learn how to use Prisma ORM in a Next.js app and deploy it to Vercel

A step-by-step guide to setting up and using Prisma ORM and Prisma Postgres with the Prisma Nuxt module and deploying to Vercel.

Learn step-by-step how to integrate Prisma ORM with Turborepo to build modular, scalable monorepo architectures efficiently.

---

## 3 docs tagged with "best-practices" | Prisma Documentation

**URL**: https://www.prisma.io/docs/tags/best-practices

**Contents**:
- 3 docs tagged with "best-practices"
- Comprehensive Guide to Using Prisma ORM with Next.js
- Guides
- Migrate data using the expand and contract pattern

Learn best practices, monorepo strategies, and dynamic usage techniques for Prisma ORM in Next.js applications.

Welcome to the Guides section! Here you'll find practical, step-by-step guides to help you accomplish specific tasks with Prisma products, including Prisma ORM, Prisma Accelerate, Prisma Postgres, and more.

Learn how to perform data migrations using the expand and contract pattern with Prisma ORM

---

## 3rd-Party Integrations for Prisma Postgres | Prisma Documentation

**URL**: https://www.prisma.io/docs/postgres/integrations

**Contents**:
- Tools & Integrations
- In this section​
- Netlify
- Vercel
- Firebase Studio
- MCP server
- Viewing data
- VS Code

Learn how Prisma Postgres works with popular 3rd-party platforms such as Vercel, Netlify, and Firebase Studio.

The Netlify extension for Prisma Postgres connects your Netlify sites with Prisma Postgres instances. Once connected, the extension will automatically set the DATABASE_URL environment variable on your deployed Netlify sites.

The Vercel Marketplace integration for Prisma Postgres connects your Vercel projects with Prisma Postgres instances. Once connected, the integration will automatically set the following environment variables on your deployed Vercel app:

If you want to explore Prisma Postgres without leaving your browser, you can try it out the via Google's Firebase Studio, a fully-fledged online IDE:

You can view and edit your data in Prisma Postgres using either Prisma Studio or 3rd party database editors.

The Prisma VS Code extension provides a management UI for Prisma Postgres and superpowers for Copilot agent mode.

---

## 4 docs tagged with "Next.js" | Prisma Documentation

**URL**: https://www.prisma.io/docs/tags/next-js

**Contents**:
- 4 docs tagged with "Next.js"
- Comprehensive Guide to Using Prisma ORM with Next.js
- How to embed Prisma Studio in a Next.js app
- How to use multiple databases in a single app
- How to use Prisma ORM with Next.js

Learn best practices, monorepo strategies, and dynamic usage techniques for Prisma ORM in Next.js applications.

Learn how to embed Prisma Studio directly in your Next.js application for database management

Learn how to use multiple Prisma Clients in a single app to connect to multiple databases, handle migrations, and deploy your application to Vercel.

Learn how to use Prisma ORM in a Next.js app and deploy it to Vercel

---

## AI | Prisma Documentation

**URL**: https://www.prisma.io/docs/ai

**Contents**:
- Build faster with Prisma + AI
  - Get started​
  - AI Coding Tools​
        - Cursor
        - Windsurf
        - Github Copilot
        - ChatGPT
  - MCP server​

In the era of AI, where code is increasingly written by agents, ensuring clarity, type safety, and reliable infrastructure is essential. With 5+ years of leadership in the TypeScript ecosystem, Prisma ORM and Prisma Postgres provide the proven foundation for AI-assisted development.

Run the following command to bootstrap your database with a prompt:

Prisma ORM and Prisma Postgres integrate seamlessly with your AI coding tools. Check out our documentation with tips and tricks for working with Prisma in various AI editors.

Define project-specific rules and use your schema as context to generate accurate queries and code.

Automate your database workflows by generating schemas, queries, and seed data in this AI-powered editor.

Get Prisma-aware code suggestions, run CLI commands from chat, and query the Prisma docs.

Learn how to connect the Prisma MCP server to ChatGPT to manage your databases with natural language.

With Prisma’s MCP server, your AI tool can take database actions on your behalf: Provisioning a new Prisma Postgres instance, creating database backups and executing SQL queries are just a few of its capabilities.

**Examples**:

```bash
npx prisma init --prompt "Create a habit tracker application"
```

```json
{  "mcpServers": {    "Prisma-Remote": {      "command": "npx",      "args": ["-y", "mcp-remote", "https://mcp.prisma.io/mcp"]    }  }}
```

```bash
npx -y mcp-remote https://mcp.prisma.io/mcp
```

---

## A mental model for Prisma Migrate | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/mental-model

**Contents**:
- Mental model
- What are database migrations?​
  - Patterns for evolving database schemas​
- What is Prisma Migrate?​
- How Prisma Migrate tracks the migration state​
- Requirements when working with Prisma Migrate​
- Evolve your database schema with Prisma Migrate​
  - Prisma Migrate in a development environment (local)​

This guide provides a conceptual overview of database migrations using Prisma Migrate when working with relational databases. It covers: what database migrations are, their value, and what Prisma Migrate is and how you can evolve your database schema with Prisma Migrate in different environments.

If you are working with MongoDB, use prisma db push to evolve your schema.

Database migrations are a controlled set of changes that modify and evolve the structure of your database schema. Migrations help you transition your database schema from one state to another. For example, within a migration you can create or remove tables and columns, split fields in a table, or add types and constraints to your database.

This section describes general schema migration patterns for evolving database schemas.

The two main schema migration patterns are:

For simplicity, we chose the terminology above to describe the different patterns for evolving database schemas. Other tools and libraries may use different terminology to describe the different patterns.

The migration files (SQL) should ideally be stored together with your application code. They should also be tracked in version control and shared with the rest of the team working on the application.

Migrations provide state management which helps you to track the state of the database.

Migrations also allow you to replicate the state of a database at a specific point in time which is useful when collaborating with other members of the team, e.g. switching between different branches.

For further information on database migrations, see the Prisma Data Guide.

Prisma Migrate is a database migration tool that supports the model/ entity-first migration pattern to manage database schemas in your local environment and in production.

The workflow when using Prisma Migrate in your project would be iterative and look like this:

Local development environment (Feature branch)

Preview/ staging environment(Feature pull request)

Produc

*[Content truncated - see full docs]*

---

## About migration histories | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/migration-histories

**Contents**:
- About migration histories
- Migration history​
- Do not edit or delete migrations that have been applied​
- Committing the migration history to source control​

This page explains how Prisma ORM uses migration histories to track changes to your schema.

Your migration history is the story of the changes to your data model, and is represented by:

A prisma/migrations folder with a sub-folder and migration.sql file for each migration:

The migrations folder is the source of truth for the history of your data model.

A _prisma_migrations table in the database, which is used to check:

If you change or delete a migration (not recommended), the next steps depend on whether you are in a development environment (and therefore using migrate dev) or a production / testing environment (and therefore using migrate deploy).

In general, you should not edit or delete a migration that has already been applied. Doing so can lead to inconsistencies between development and production environment migration histories, which may have unforeseen consequences — even if the change does not appear to break anything at first.

The following scenario simulates a change that creates a seemingly harmless inconsistency:

A change that does not appear to break anything after a migrate reset can hide problems - you may end up with a bug in production that you cannot replicate in development, or the other way around - particularly if the change concerns a highly customized migration.

If Prisma Migrate reports a missing or edited migration that has already been applied, we recommend fixing the root cause (restoring the file or reverting the change) rather than resetting.

You must commit the entire prisma/migrations folder to source control. This includes the prisma/migrations/migration_lock.toml file, which is used to detect if you have attempted to change providers.

Source-controlling the schema.prisma file is not enough - you must include your migration history. This is because:

**Examples**:

```text
migrations/  └─ 20210313140442_init/    └─ migration.sql  └─ 20210313140442_added_job_title/    └─ migration.sql
```

```sql
-- AlterTable ALTER TABLE "Post" ALTER COLUMN "content" SET DATA TYPE VARCHAR(560);
```

```text
6 migrations found in prisma/migrationsWARNING The following migrations have been modified since they were applied:20210310143435_change_type
```

---

## Accelerate: Caching | Prisma Documentation

**URL**: https://www.prisma.io/docs/accelerate/caching

**Contents**:
- Caching queries in Prisma Accelerate

Prisma Accelerate provides global caching for read queries using TTL, Stale-While-Revalidate (SWR), or a combination of both. It's included as part of Prisma Postgres, but can also be used with your own database by enabling Accelerate in the and configuring it with your database.

This content has moved — learn more on the updated Caching in Accelerate page.

---

## Accelerate: Evaluating | Prisma Documentation

**URL**: https://www.prisma.io/docs/accelerate/evaluating

**Contents**:
- Evaluating
- How Accelerate's connection pool optimizes performance under load​
- Evaluating Prisma Accelerate connection pooling performance​
- Evaluating Prisma Accelerate caching performance​

Prisma Accelerate optimizes database interactions through advanced connection pooling and global edge caching. Its connection pooler is available in 16 regions and helps applications load-balance and scale database requests based on demand.

Considering the information above, we recommend evaluating Accelerate with high volume to see it perform under load.

Prisma Accelerate employs a dynamic, serverless connection pooling infrastructure. When a request is made, a connection pool is quickly provisioned for the project in the region assigned while configuring Prisma Accelerate. This connection pool remains active, serving many additional requests while reusing established database connections. The connection pool will disconnect after a period of inactivity, so it’s important to evaluate Prisma Accelerate with a consistent stream of traffic.

Optimized Query Performance: The serverless connection pooler adapts to the query load, ensuring the database connections are managed efficiently during peak demand.

Prisma Accelerate’s connection pooler cannot improve the performance of queries in the database. In scenarios where query performance is an issue, we recommend optimizing the Prisma query, applying indexes, or utilizing Accelerate’s edge caching.

Maximize Connection Reuse: Executing a consistent volume of queries helps maintain active instances of Accelerate connection poolers. This increases connection reuse, ensuring faster response times for subsequent queries.

By understanding and harnessing this mechanism, you can ensure that your database queries perform consistently and efficiently at scale.

Below you will find an example of how to evaluate Prisma Accelerate using a sample model:

Prisma Accelerate’s edge cache is also optimized for a high volume of queries. The cache automatically optimizes for repeated queries. As a result, the cache hit rate will increase as the query frequency does. Adding a query result to the cache is also non-blocking, so a short b

*[Content truncated - see full docs]*

**Examples**:

```prisma
model Notes {  id        Int       @id @default(autoincrement())  title     String  createdAt DateTime  @default(now())  updatedAt DateTime? @updatedAt}
```

```typescript
import { PrismaClient } from '@prisma/client'import { withAccelerate } from '@prisma/extension-accelerate'const prisma = new PrismaClient().$extends(withAccelerate())function calculateStatistics(numbers: number[]): {  average: number  p50: number  p75: number  p99: number} {  if (numbers.length === 0) {    throw new Error('The input array is empty.')  }  // Sort the array in ascending order  numbers.sort((a, b) => a - b)  const sum = numbers.reduce((acc, num) => acc + num, 0)  const count = numb
...
```

```typescript
import { PrismaClient } from '@prisma/client'import { withAccelerate } from '@prisma/extension-accelerate'const prisma = new PrismaClient().$extends(withAccelerate())function calculateStatistics(numbers: number[]): {  average: number  p50: number  p75: number  p99: number} {  if (numbers.length === 0) {    throw new Error('The input array is empty.')  }  // Sort the array in ascending order  numbers.sort((a, b) => a - b)  const sum = numbers.reduce((acc, num) => acc + num, 0)  const count = numb
...
```

---

## Accelerate: FAQ | Prisma Documentation

**URL**: https://www.prisma.io/docs/accelerate/faq

**Contents**:
- Accelerate FAQ
- When should I enable static IP for Prisma Accelerate?​
- Why do I sometimes see unexpected cache behavior?​
- What is the pricing of Accelerate?​
- VS Code does not recognize the $extends method​
- What regions are Accelerate's cache nodes available in?​
- What regions is Accelerate's connection pool available in?​
- How does Accelerate know what region to fetch the cache from?​

Enable static IP for Accelerate when your security setup requires IP allowlisting or if you're implementing firewalls that only permit access from trusted IPs, ensuring controlled and secure database connections.

Learn more on how to enable static IP for Accelerate in the Platform Console.

A static IP address is an IPv4 or an IPv6 address that is fixed. Unlike dynamic IP addresses, which can change unpredictably, traffic from static IP addresses can be easily identified.

ℹ️ To enable static IP support for Accelerate within your existing or new project environment, your workspace will need to be on our Pro or Business plans. Take a look at the pricing page for more information.

Accelerate's cache performs best when it observes a higher load from a project. Many cache operations, such as committing data to cache and refreshing stale data, happen asynchronously. When benchmarking Accelerate, we recommend doing so with loops or a load testing approach. This will mimic higher load scenarios better and reduce outliers from low frequency operations.

Prisma operations are sent to Accelerate over HTTP. As a result, the first request to Accelerate must establish an HTTP handshake and may have additional latency as a result. We're exploring ways to reduce this initial request latency in the future.

You can find more details on our Accelerate pricing page

If you add the Prisma Client extension for Accelerate to an existing project that is currently open in VS Code, the editor might not immediately recognize the $extends method.

This might be an issue with the TypeScript server not yet recognizing the regenerated Prisma Client. To resolve this, you need to restart TypeScript.

VS Code should now recognize the $extends method.

Accelerate runs on Cloudflare's network and cache hits are served from Cloudflare's 300+ locations. You can find the regions where Accelerate's cache nodes are available here: https://www.cloudflare.com/network/.

When no cache strategy is specifie

*[Content truncated - see full docs]*

**Examples**:

```ts
await prisma.$transaction(async (tx) => {  await tx.user.deleteMany({ where: { name: "John Doe" } });  await tx.user.createMany({ data });});
```

```ts
await prisma.$transaction([  prisma.user.deleteMany({ where: { name: "John Doe" } }),  prisma.user.createMany({ data }),]);
```

---

## Accelerate: Feedback | Prisma Documentation

**URL**: https://www.prisma.io/docs/accelerate/feedback

**Contents**:
- Feedback

You can submit any feedback about Accelerate in our Discord server.

---

## Accelerate: Local development | Prisma Documentation

**URL**: https://www.prisma.io/docs/accelerate/local-development

**Contents**:
- Local development for Prisma Accelerate
- Using Prisma Accelerate client extension in development and production​
- Using Prisma Accelerate locally in an edge function​

Prisma Accelerate efficiently scales production traffic with integrated connection pooling and a global database cache.

In development environments, you may want to use a local database to minimize expenses. Furthermore, you may consider extending Prisma Client with the Accelerate client extension once so that you can use a local database in development and a hosted database with Accelerate’s connection pooling and caching enabled. This eliminates the need for conditional logic to switch clients between development and production.

This guide will explain how to use Prisma Accelerate client extension in a development environment with a local database.

Accelerate does not work with a local database. However, in a development environment, you can still use Prisma Client with the Accelerate client extension. This setup will not provide Accelerate's connection pooling and caching features.

The following steps outline how to use Prisma ORM and Prisma Accelerate with a local PostgreSQL database.

Update the DATABASE_URL environment variable with your local database's connection string:

Generate a Prisma Client:

Note: The --no-engine flag should only be used in preview and production environments. The command generates Prisma Client artifacts without a Query Engine file, which requires an Accelerate connection string.

Set up Prisma Client with the Accelerate client extension:

The extended instance of Prisma Client will use the local database. Hence, Prisma Accelerate will not be used in your development environment to respond to your Prisma Client queries.

If an Accelerate connection string is used as the DATABASE_URL environment variable, Prisma Client will route your queries through Accelerate.

When using an edge function, e.g., Vercel's edge runtime, for your development environment, update your Prisma Client import as follows:

Generally, edge function environments lack native support for existing APIs enabling TCP-based database connections. Prisma Accelerate

*[Content truncated - see full docs]*

**Examples**:

```.env
DATABASE_URL="postgres://username:password@127.0.0.1:5432/localdb"
```

```bash
npx prisma generate
```

```typescript
import { PrismaClient } from '@prisma/client'import { withAccelerate } from '@prisma/extension-accelerate'const prisma = new PrismaClient().$extends(withAccelerate())
```

---

## Accelerate: limitations | Prisma Documentation

**URL**: https://www.prisma.io/docs/accelerate/known-limitations

**Contents**:
- Known limitations about Prisma Accelerate
- Cannot cache raw queries​
- Not compatible with the fluent API​
- Not compatible with extremely heavy or long-running queries​
- Not compatible with direct IPv4 addresses in MongoDB connection strings​
  - Example​

Below are descriptions of known limitations when using Accelerate. If you encounter any additional ones, please share them with us via Discord.

At the moment, it is not possible to cache the responses of raw queries.

Client Extensions (which are used in Accelerate) currently do not correctly forward the fluent API types. We hope to get a fix into Client Extensions soon.

Accelerate is designed to work with high-performance, low-latency queries. It is not intended for use with extremely heavy or long-running queries that may cause performance issues or resource contention. While limits are configurable, we recommend optimizing your queries to ensure they fit within the recommended guidelines.

For queries that cannot be optimized or pared down, we recommend one of two solutions:

Use the read replica extension: The Prisma ORM read replica extension allows you to set up two different connections: a primary and a replica. You can set up your Accelerate connection as the primary and then a direct connection as the replica. Any queries that are resource-intensive or long-running can then be routed to the replica, while the primary (your Accelerate connection) will handle normal queries. Please note that this solution requires you to both set up a direct connection and requires the full generated Prisma Client (i.e. without --no-engine).

Separate analytics queries: Our preferred solution is to separate your analytics queries into a separate application. This separate application can then use a direct connection so that it can run heavy queries without impacting the performance or cost of your Accelerate-powered application.

If you have a use case that requires running extremely heavy or long-running queries and Prisma Accelerate, please reach out to us.

Accelerate does not support direct IPv4 addresses in MongoDB connection strings. When an IPv4 address is provided, Accelerate converts it to an IPv6 format to route through its NAT gateway. This conversion may cause t

*[Content truncated - see full docs]*

---

## Add Prisma ORM Easily to Your Nuxt Apps | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/more/help-and-troubleshooting/prisma-nuxt-module

**Contents**:
- Using the Nuxt Prisma Module
- Features​
- Getting started​
- Using a different database provider​
  - Using a database without existing data​
  - Using a database with pre-existing data​
- Usage​
  - Option A: usePrismaClient composable​

The Nuxt Prisma module simplifies the integration of Prisma ORM into your Nuxt applications.

Prisma ORM is a database library that lets you model your database schema, provides auto-generated migrations and lets you query the database in an intuitive and type-safe way.

This module provides several features to streamline the setup and usage of Prisma ORM in a Nuxt application, making it easier to interact with your database.

Create a new Nuxt Project:

Navigate to project directory and install @prisma/nuxt using the Nuxt CLI:

If you're using pnpm, make sure to hoist Prisma dependencies. Follow the Prisma studio steps for detailed instructions.

Start the development server:

Starting the development server will:

The database migrates automatically the first time you start the module if there isn't a migrations folder. After that, you need to run npx prisma migrate dev manually in the CLI to apply any schema changes. Running the npx prisma migrate dev command manually makes it easier and safer to manage migrations and also to troubleshoot any migration-related errors.

You can now use Prisma ORM in your project. If you accepted the prompt to add Prisma Studio, you can access Prisma Studio through the Nuxt Devtools. See the usage section to learn how to use Prisma Client in your app.

The @prisma/nuxt module works with any database provider that Prisma ORM supports. You can configure the getting started example to use a database of your choice. The steps would be different for a database without existing data and a database with pre-existing data.

To configure the getting started example to use a PostgreSQL database without any existing data:

To configure the getting started example to use a PostgreSQL database that already has data in it:

If you're using Nuxt server components, you can use the global instance of the Prisma Client in your .server.vue files:

After running through the initial setup prompts, this module creates the lib/prisma.ts file which contai

*[Content truncated - see full docs]*

**Examples**:

```terminal
npm create nuxt test-nuxt-app
```

```terminal
cd test-nuxt-appnpx nuxi@latest module add @prisma/nuxt
```

```terminal
npm run dev
```

---

## Additional Resources for Prisma ORM. | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/more

**Contents**:
- More resources for Prisma ORM
- In this section​
- Under the hood
- Upgrade guides
- AI tools
- Comparing Prisma ORM
- Development environment
- Help articles

This page explains the release process of Prisma ORM, how it's versioned and how to deal with breaking changes that might happen throughout releases.

---

## Additional Resources for Prisma Postgres | Prisma Documentation

**URL**: https://www.prisma.io/docs/postgres/more

**Contents**:
- More resources for Prisma Postgres
- In this section​
- Troubleshooting
- FAQ

Explore additional topics related to Prisma Postgres, including known limitations, troubleshooting guides, and frequently asked questions.

This guide helps resolve common issues when working with Prisma Postgres.

Common questions about how Prisma Postgres works, how queries are billed, and how it integrates with the Prisma ORM.

---

## Comparing Prisma Accelerate to other connection pooling options | Prisma Documentation

**URL**: https://www.prisma.io/docs/accelerate/compare

**Contents**:
- Compare Accelerate
- What makes Accelerate unique?​
- Accelerate global cache​
- Accelerate connection pool​
  - Management​
  - Performance​
  - Database Support​

Prisma Accelerate supports products that serve a global audience, with a global caching system and connection pool that spans multiple regions, providing consistent access to data with low latency no matter where your user (or your database) is located in the world.

The managed connection pool is designed to support serverless infrastructure, capable of handling high volumes of connections and adapting to traffic spikes with ease.

Explore how Prisma Accelerate compares to other global cache and connection pool solutions on the market, and discover what sets it apart.

Prisma Accelerate is chosen and loved by many for a number of key reasons which make Accelerate unique:

Prisma Accelerate offers a powerful global cache, so you can serve data to your users at the edge — the closest point to where the users are located — no matter where your database is hosted. This not only speeds up the experience for users, but also reduces read load on your database as well by avoiding roundtrips.

Why are these important?

Since Accelerate extends the Prisma client, you can control caching policies directly from your codebase with just an extra line of code. Integration is seamless. Here is an example using the stale-while-revalidating caching strategy:

Query level cache policies are critical for serious applications, so that you can control which queries are cached, and the characteristics of the policy. You may want certain data in your app to be cached for several days, other data to be cached for a just a few minutes, and other data to be not cached at all. This is only possible with Prisma Accelerate.

Authenticating with an API key can be a helpful security measure, allowing you to decouple database credentials from application secrets. Easily rotate API keys as often as you like, without needing any credential changes in your database

Automatic cache updates means that the cache is automatically updated when a change in the database occurs. With Accelerate, you are in 

*[Content truncated - see full docs]*

**Examples**:

```jsx
await prisma.user.findMany({  cacheStrategy: {    swr: 60,  },});
```

---

## Comprehensive Guide to Using Prisma ORM with Next.js | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/more/help-and-troubleshooting/nextjs-help

**Contents**:
- Comprehensive Guide to Using Prisma ORM with Next.js
- Best practices for using Prisma Client in development​
  - Avoid multiple Prisma Client instances​
    - Why this happens​
    - Recommended solution​
- Setting Up Prisma ORM in a Monorepo​
  - Challenges of using Prisma ORM in monorepos​
    - Key issues​

Prisma ORM and Next.js form a powerful combination for building modern, server-side rendered, and API-driven web applications. This guide consolidates various tips and strategies to help you maximize their potential. Whether you’re looking for best practices, monorepo setup guidance, or strategies for dynamic usage, we’ve got you covered.

When developing a Next.js application, one common issue is accidentally creating multiple instances of the Prisma Client. This often occurs due to Next.js’s hot-reloading feature in development.

Next.js’s hot-reloading feature reloads modules frequently to reflect code changes instantly. However, this can lead to multiple instances of Prisma Client being created, which consumes resources and might cause unexpected behavior.

To avoid this, create a single Prisma Client instance by using a global variable:

Using this approach ensures that only one instance of Prisma Client exists, even during hot-reloading in development.

Monorepos allow multiple projects to share code and dependencies, making them a popular choice for modern development. However, using Prisma ORM in a monorepo can present challenges related to dependency resolution and schema management.

Centralize the Prisma Schema: Place the schema.prisma file in a shared package, such as @myorg/db, to ensure consistency.

Use a custom output directory for generated client: Define a custom output directory for the generated Prisma Client to maintain consistency across packages.

Install dependencies in the root: To prevent version conflicts, install Prisma ORM at the root of the monorepo. If individual packages need direct access to Prisma (e.g., for local client generation), install it within those packages as well. You can use a monorepo tool like Turborepo, following its best practices, or adopt a similar strategy to keep dependencies synchronized across your app.

Use NPM Scripts for Generation:

This approach keeps your Prisma Schema and generated client in sync across 

*[Content truncated - see full docs]*

**Examples**:

```typescript
// lib/prisma.tsimport { PrismaClient } from "@prisma/client";const globalForPrisma = global as unknown as { prisma: PrismaClient };export const prisma =  globalForPrisma.prisma || new PrismaClient();if (process.env.NODE_ENV !== "production") globalForPrisma.prisma = prisma;
```

```json
{    "scripts": {      "prisma:generate": "prisma generate --schema=./packages/db/schema.prisma"    }  }
```

```typescript
// lib/prismaDynamic.tsimport { PrismaClient } from "@prisma/client";type TenantConfig = {  databaseUrl: string;};export function createPrismaClient(config: TenantConfig): PrismaClient {  return new PrismaClient({    datasources: {      db: {        url: config.databaseUrl,      },    },  });}
```

---

## Console: Maturity levels | Prisma Documentation

**URL**: https://www.prisma.io/docs/platform/maturity-levels

**Contents**:
- Maturity levels
  - Early Access​
  - Preview​
  - General Availability​

Prisma releases updates to Prisma Data Platform multiple times per week, as opposed to the Prisma ORM that we release on a set schedule every few weeks. This is why we consider the lifecycle and process for maturing features in Prisma Data Platform differently.

You can check out the releases and maturity process for the Prisma ORM for further details.

You can find information about releases across all Prisma tools and products in the changelog.

If a feature on the Prisma Data Platform is labeled as Early Access:

As always, your feedback in our Discord is invaluable to shape the design of the features. This will help us ensure that they can solve your problems in the best way possible.

If a feature on the Prisma Data Platform is labeled as Preview:

We recommend testing the product in a staging environment and welcome any feedback in our Discord. This will assist us in improving the product for its final release.

If a feature in the Prisma Data Platform is Generally Available:

---

## Console: Support | Prisma Documentation

**URL**: https://www.prisma.io/docs/platform/support

**Contents**:
- Support
- Support​
  - Community support​
  - Standard support​
  - Premium support​
  - Dedicated support​
- Deleting your PDP account​

Your feedback is invaluable, and we encourage you to share your experiences with us on Discord.

Your support options are based on your workspace's active plan. For more details, take a look at our pricing page.

Reach out to us in our Discord.

Dedicated contact person.

If you want to delete your PDP account, email us at support@prisma.io specifying the email id or GitHub handle with which you signed up.

To ensure that you're not accidentally disabling any infrastructure powering one of your applications, we require that you disable Accelerate in all environments of all your projects that live in the account to be deleted. Additionally there should be no active subscriptions in the account to be deleted. Please cancel any active subscriptions before requesting account deletion.

---

## Customizing migrations | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-migrate/workflows/customizing-migrations

**Contents**:
- Customizing migrations
- How to edit a migration file​
  - Example: Rename a field​
  - Example: Use the expand and contract pattern to evolve the schema without downtime​
  - Example: Change the direction of a 1-1 relation​

This guide does not apply for MongoDB. Instead of migrate dev, db push is used for MongoDB.

In some scenarios, you need to edit a migration file before you apply it. For example, to change the direction of a 1-1 relation (moving the foreign key from one side to another) without data loss, you need to move data as part of the migration - this SQL is not part of the default migration, and must be written by hand.

This guide explains how to edit migration files and gives some examples of use cases where you may want to do this.

To edit a migration file before applying it, the general procedure is the following:

Make a schema change that requires custom SQL (for example, to preserve existing data)

Create a draft migration using:

Modify the generated SQL file.

Apply the modified SQL by running:

By default, renaming a field in the schema results in a migration that will:

To actually rename a field and avoid data loss when you run the migration in production, you need to modify the generated migration SQL before applying it to the database. Consider the following schema fragment - the biograpy field is spelled wrong.

To rename the biograpy field to biography:

Rename the field in the schema:

Run the following command to create a draft migration that you can edit before applying to the database:

Edit the draft migration as shown, changing DROP / DELETE to a single RENAME COLUMN:

For SQL Server, you should use the stored procedure sp_rename instead of ALTER TABLE RENAME COLUMN.

Save and apply the migration:

You can use the same technique to rename a model - edit the generated SQL to rename the table rather than drop and re-create it.

Making schema changes to existing fields, e.g., renaming a field can lead to downtime. It happens in the time frame between applying a migration that modifies an existing field, and deploying a new version of the application code which uses the modified field.

You can prevent downtime by breaking down the steps required to alter

*[Content truncated - see full docs]*

**Examples**:

```terminal
npx prisma migrate dev --create-only
```

```terminal
npx prisma migrate dev
```

```prisma
model Profile {  id       Int    @id @default(autoincrement())  biograpy String  userId   Int    @unique  user     User   @relation(fields: [userId], references: [id])}
```

---

## Data model | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-schema/data-model

**Contents**:
- Data model
- In this section​
- Models
- Relations
- Indexes
- Views
- Database mapping
- Multi-schema

The data model definition part of the Prisma schema defines your application models (also called Prisma models). Models:

Prisma ORM allows configuration of database indexes, unique constraints and primary key constraints. This is in General Availability in versions 4.0.0 and later. You can enable this with the extendedIndexes Preview feature in versions 3.5.0 and later.

Database views allow you to name and store queries. In relational databases, views are stored SQL queries that might include columns in multiple tables, or calculated values such as aggregates. In MongoDB, views are queryable objects where the contents are defined by an aggregation pipeline on other collections.

The Prisma schema includes mechanisms that allow you to define names of certain database objects. You can:

Not all database functions and features of Prisma ORM's supported databases have a Prisma Schema Language equivalent. Refer to the database features matrix for a complete list of supported features.

---

## Data modeling with Prisma | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/overview/introduction/data-modeling

**Contents**:
- Data modeling
- What is data modeling?​
- Data modeling without Prisma ORM​
  - Data modeling on the database level​
    - Relational databases​
    - MongoDB​
  - Data modeling on the application level​
  - Data modeling with ORMs​

The term data modeling refers to the process of defining the shape and structure of the objects in an application, these objects are often called "application models". In relational databases (like PostgreSQL), they are stored in tables . When using document databases (like MongoDB), they are stored in collections.

Depending on the domain of your application, the models will be different. For example, if you're writing a blogging application, you might have models such as blog, author, article. When writing a car-sharing app, you probably have models like driver, car, route. Application models enable you to represent these different entities in your code by creating respective data structures.

When modeling data, you typically ask questions like:

Data modeling typically needs to happen on (at least) two levels:

The way that the application models are represented on both levels might differ due to a few reasons:

In relational databases, models are represented by tables. For example, you might define a users table to store information about the users of your application. Using PostgreSQL, you'd define it as follows:

A visual representation of the users table with some random data might look as follows:

It has the following columns:

In MongoDB databases, models are represented by collections and contain documents that can have any structure:

Prisma Client currently expects a consistent model and normalized model design. This means that:

In addition to creating the tables that represent the entities from your application domain, you also need to create application models in your programming language. In object-oriented languages, this is often done by creating classes to represent your models. Depending on the programming language, this might also be done with interfaces or structs.

There often is a strong correlation between the tables in your database and the models you define in your code. For example, to represent records from the aforementioned users tab

*[Content truncated - see full docs]*

**Examples**:

```sql
CREATE TABLE users (  user_id SERIAL PRIMARY KEY NOT NULL,  name VARCHAR(255),  email VARCHAR(255) UNIQUE NOT NULL,  isAdmin BOOLEAN NOT NULL DEFAULT false);
```

```js
{  _id: '607ee94800bbe41f001fd568',  slug: 'prisma-loves-mongodb',  title: 'Prisma <3 MongoDB',  body: "This is my first post. Isn't MongoDB + Prisma awesome?!"}
```

```js
class User {  constructor(user_id, name, email, isAdmin) {    this.user_id = user_id    this.name = name    this.email = email    this.isAdmin = isAdmin  }}
```

---

## Data validation with CHECK constraints (PostgreSQL) | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/more/help-and-troubleshooting/check-constraints

**Contents**:
- Data validation with CHECK constraints (PostgreSQL)
- Overview​
- Prerequisites​
- 1. Create a new database and project directory​
- 2. Adding a table with a single check constraint on a single column​
- 3. Adding a table with a multi-column check constraint​
- 4. Adding a table with multiple check constraints​
- 5. Adding a check constraint to an existing table​

This page explains how to configure check constraints in a PostgreSQL database. A check constraint is a condition that must be satisfied before a value can be saved to a table - for example, the discounted price of a product must always be less than the original price.

Check constraints can be added when you create the table (using CREATE TABLE) or to a table that already exists (using ALTER TABLE). This guide covers all four combinations.

At the end of the guide, you'll introspect your database, generate a Prisma Client, and write a simple Node.js script to validate the constraints.

In order to follow this guide, you need:

Start by creating a project directory for the files that you'll create throughout this guide. Open terminal or command line and run the following commands:

Next, make sure that your PostgreSQL database server is running. Authenticate the default postgres user:

Windows (command line):

Then execute the following command in your terminal to create a new database called CheckDemo:

Windows (command line):

Tip: Remember the trailing ;! postgres=# postgres-#

You can validate that the database was created by running the \dt command which lists all tables (relations) in your database (right now there are none):

Windows (command line):

In this section, you'll create a new table with a single check constraint on a single column in the CheckDemo database.

Create a new file named single-column-check-constraint.sql and add the following code to it:

Now run the SQL statement against your database to create a new table called product:

Windows (command line):

Congratulations, you just created a table called product in the database. The table has one column called price, which has a single check constraint that ensures price of a product is:

Run the following command to see the a list of check constraints that apply to the product table:

You will see the following output, which includes a list of all check constraints:

Note that PostgreSQL will 

*[Content truncated - see full docs]*

**Examples**:

```text
mkdir check-democd check-demo
```

```text
sudo -u postgres
```

```text
psql -U postgres
```

---

## Debugging & troubleshooting | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-client/debugging-and-troubleshooting

**Contents**:
- Debugging & troubleshooting
- In this section​
- Debugging
- Handling exceptions and errors
- Troubleshooting binary size and deployment issues

Prisma Optimize helps you generate insights and provides recommendations that can help you make your database queries faster:

Optimize aims to help developers of all skill levels write efficient database queries, reducing database load and making applications more responsive.

You can enable debugging output in Prisma Client and Prisma CLI via the DEBUG environment variable. It accepts two namespaces to print debugging output:

In order to handle different types of errors you can use instanceof to check what the error is and handle it accordingly.

If you encounter large bundle sizes, slow builds, or deployment errors related to Prisma’s Rust engine binaries, for example, in serverless or edge environments, the issue may be caused by the default native Rust query engine that ships with Prisma Client.

---

## Deploy a Node.js application with Prisma | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-client/deployment

**Contents**:
- Deployment
- In this section​
- Deploy Prisma ORM
- Traditional servers
- Serverless functions
- Edge functions
- Module bundlers
- Deploying database changes

This section describes how to deploy Node.js applications that use Prisma Client and TypeScript to various platforms.

If Prisma ORM's Rust engine binaries cause large bundle sizes, slow builds, or deployment issues (for example, in serverless or edge environments), you can use it without them using this configuration of your generator block:

Prisma ORM without Rust binaries has been Generally Available since v6.16.0.

Note that you need to use a driver adapter in this case.

When using this architecture:

This setup can simplify deployments in:

Learn more in the docs here.

Curious why we moved away from the Rust engine? Take a look at why we transitioned from Rust binary engines to an all-TypeScript approach for a faster, lighter Prisma ORM in this blog post.

Projects using Prisma Client can be deployed to many different cloud platforms. Given the variety of cloud platforms and different names, it's noteworthy to mention the different deployment paradigms, as they affect the way you deploy an application using Prisma Client.

To apply pending migrations to staging, testing, or production environments, run the migrate deploy command as part of your CI/CD pipeline:

There are two scenarios where you might consider deploying migrations directly from a local environment to a production environment.

The following describes some caveats you might face when deploying to different AWS platforms.

Prisma Client depends on the query engine that is running as a binary on the same host as your application.

**Examples**:

```prisma
generator client {  provider   = "prisma-client-js" // or "prisma-client"  engineType = "client"}
```

---

## Development and production | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-migrate/workflows/development-and-production

**Contents**:
- Development and production
- Development environments​
  - Create and apply migrations​
  - Reset the development database​
  - Customizing migrations​
  - Team development​
- Production and testing environments​
  - Advisory locking​

This page explains how to use Prisma Migrate commands in development and production environments.

In a development environment, use the migrate dev command to generate and apply migrations:

migrate dev is a development command and should never be used in a production environment.

The migrate dev command will prompt you to reset the database in the following scenarios:

You can also reset the database yourself to undo manual changes or db push experiments by running:

migrate reset is a development command and should never be used in a production environment.

¹ For MySQL and MongoDB this refers to the database, for PostgreSQL and SQL Server to the schema, and for SQLite to the database file.

Note: For a simple and integrated way to re-create data in your development database as often as needed, check out our seeding guide.

Sometimes, you need to modify a migration before applying it. For example:

The --create-only command allows you to create a migration without applying it:

To apply the edited migration, run prisma migrate dev again.

Refer to Customizing migrations for examples.

See: Team development with Prisma Migrate .

In production and testing environments, use the migrate deploy command to apply migrations:

Note: migrate deploy should generally be part of an automated CI/CD pipeline, and we do not recommend running this command locally to deploy changes to a production database.

Compares applied migrations against the migration history and warns if any migrations have been modified:

Applies pending migrations

The migrate deploy command:

Prisma Migrate makes use of advisory locking when you run production commands such as:

This safeguard ensures that multiple commands cannot run at the same time - for example, if you merge two pull requests in quick succession.

Advisory locking has a 10 second timeout (not configurable), and uses the default advisory locking mechanism available in the underlying provider:

Prisma Migrate's implementation of adv

*[Content truncated - see full docs]*

**Examples**:

```terminal
npx prisma migrate dev
```

```terminal
npx prisma migrate reset
```

```terminal
npx prisma migrate dev --create-only
```

---

## Enable Static IP for Prisma Accelerate | Prisma Documentation

**URL**: https://www.prisma.io/docs/accelerate/static-ip

**Contents**:
- Static IP
- Enable static IP in Accelerate​
  - 1. When enabling Accelerate for your project environment:​
  - 2. For projects already using Accelerate:​

You can enable static IP for Accelerate when your security setup requires IP allowlisting or if you're implementing firewalls that only permit access from trusted IPs, ensuring controlled and secure database connections.

To enable static IP support for Accelerate within an existing or a new project environment, your workspace will need to be on our Pro or Business plans. Take a look at the pricing page for more information.

You can opt-in to use static IP for Accelerate in the Platform Console in two ways:

Enabling static IP for Accelerate will provide you with a list of static IPv4 and IPv6 addresses.

Once you have these addresses, configure your database firewall to allow incoming connections only from these IPs and any other trusted IPs that need access to your database.

Since you cannot enable static IP for an existing Accelerate-enabled environment, we recommend opting for static IP when enabling Accelerate in a new environment. Use the same database URL as your existing Accelerate environment to instantly access static IP support for Accelerate.

---

## Fields & types | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-client/special-fields-and-types

**Contents**:
- Fields & types
- Working with Decimal​
- Working with BigInt​
  - Overview​
  - Serializing BigInt​
- Working with Bytes​
- Working with DateTime​
      - Jan 01, 1998; 00 h 00 min and 000 ms​

This section covers various special fields and types you can use with Prisma Client.

Decimal fields are represented by the Decimal.js library. The following example demonstrates how to import and use Prisma.Decimal:

You can also perform arithmetic operations:

Prisma.Decimal uses Decimal.js, see Decimal.js docs to learn more.

The use of the Decimal field is not currently supported in MongoDB.

BigInt fields are represented by the BigInt type (Node.js 10.4.0+ required). The following example demonstrates how to use the BigInt type:

Prisma Client returns records as plain JavaScript objects. If you attempt to use JSON.stringify on an object that includes a BigInt field, you will see the following error:

To work around this issue, use a customized implementation of JSON.stringify:

Bytes fields are represented by the Uint8Array type. The following example demonstrates how to use the Uint8Array type:

Note that before Prisma v6, Bytes were represented by the Buffer type:

Learn more in the upgrade guide to v6.

There currently is a bug that doesn't allow you to pass in DateTime values as strings and produces a runtime error when you do. DateTime values need to be passed as Date objects (i.e. new Date('2024-12-04') instead of '2024-12-04').

When creating records that have fields of type DateTime, Prisma Client accepts values as Date objects adhering to the ISO 8601 standard.

Consider the following schema:

Here are some examples for creating new records:

See: Working with Json fields

See: Working with scalar lists / arrays

See: Working with composite IDs and compound unique constraints

**Examples**:

```ts
import { PrismaClient, Prisma } from '@prisma/client'const newTypes = await prisma.sample.create({  data: {    cost: new Prisma.Decimal(24.454545),  },})
```

```ts
import { PrismaClient, Prisma } from '@prisma/client'const newTypes = await prisma.sample.create({  data: {    cost: new Prisma.Decimal(24.454545).plus(1),  },})
```

```ts
import { PrismaClient, Prisma } from '@prisma/client'const newTypes = await prisma.sample.create({  data: {    revenue: BigInt(534543543534),  },})
```

---

## General | Prisma Console | Prisma Documentation

**URL**: https://www.prisma.io/docs/platform/about

**Contents**:
- General
- Overview​
- Concepts​
  - User account​
  - Workspace​
    - Optimize​
      - Accessing the Optimize dashboard​
      - Generating an Optimize API key​

The enables you to manage and configure your projects that use Prisma Data Platform (PDP) products, and helps you integrate them into your application:

The Console workflows are based on four main concepts:

Here is a visual illustration of how these concepts relate to each other:

A user account is the prerequisite for any interactions with PDP products. You can use it to manage your workspaces (and their projects). A user account can be invited to collaborate on workspaces created by other users as well.

If you need to delete your user account, go here.

You can create several workspaces. A workspace is an isolated space to host projects. A workspace can have multiple user accounts associated with it so that multiple users can collaborate on the the projects in the workspace.

In each workspace, you can:

You can access Optimize within your workspace.

To access the Optimize dashboard in your desired workspace:

To obtain the Optimize API key:

You now have your Optimize API key.

In each workspace, you can create several projects. A project typically represents an application (a product or service). You typically have one Prisma schema per project.

In each project, you can:

The number of project you can create in a workspace depends on the subscription plan configured in that workspace.

An environment is an isolated space used to provision PDP products for a specific project. Environments typically correspond to development stages, such as Development, Staging, or Production. Every new project begins with a default environment named Production. The default environment ensures that the project always has at least one active environment. It cannot be deleted unless another environment is designated as the default.

In each environment, you can:

The number of environments you can create in a project depends on the subscription plan configured in your workspace.

The Database tab in the left panel of a project environment lets you configure and manage connectio

*[Content truncated - see full docs]*

---

## Getting started with npx create-db | Prisma Documentation

**URL**: https://www.prisma.io/docs/postgres/introduction/npx-create-db

**Contents**:
- npx create-db
- Prerequisites​
  - Option 1: Using the web interface (recommended)​
    - Key features:​
    - Getting started:​
  - Option 2: Using the CLI​
    - Option 1: Quick start with default settings​
    - Option 2: Choose a region interactively​

create-db is an open-source CLI tool that provisions temporary Prisma Postgres databases with a single command.

To use npx create-db, you need:

A Prisma Data Platform account is not required to create a temporary database. However, if you want to keep a database permanently, you can claim it (details below).

The create-db web application provides a browser-based interface for creating and managing your databases.

You can create a database using one of the following options:

Run the following command in your terminal:

If you want to select a region manually:

To view all options and regions:

Here is an example output:

Once you have the output, take the Prisma ORM-optimized connection string (prisma+postgres://...) and add it to your .env file as DATABASE_URL:

You can now follow the Prisma Postgres quickstart guide to connect your Prisma project to this database.

If you're using other tools or libraries, use the standard PostgreSQL connection string (postgresql://...) with any PostgreSQL-compatible client, such as psql, pgAdmin, node-postgres, or an ORM of your choice. Detailed instructions are available in the guide for connecting via direct PostgreSQL connection string.

By default, databases created with npx create-db are temporary and will be automatically deleted after 24 hours.

You can prevent this by claiming the database using the claim URL shown in the CLI output:

To claim your database and make it permanent:

When you claim a database:

Here are the CLI flags for the npx create-db command:

To view all CLI options use the --help or -h flag:

**Examples**:

```terminal
npx create-db@latest
```

```terminal
npx create-db@latest --interactive
```

```terminal
npx create-db@latest -i
```

---

## Help articles | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/more/help-and-troubleshooting

**Contents**:
- Help articles
- Help articles​
- Dataguide
- Autocompletion in GraphQL resolvers with JavaScript
- Modeling and querying many-to-many relations
- Converting Implicit many-to-many relation to Explicit many-to-many relation
- Using Prisma ORM with Next.js
- Solve package error with vercel/pkg

This section provides a number of common problems that developers might encounter when using Prisma ORM and provides short, practical solutions to resolve them.

Learn how databases work, how to choose the right one, and how to use databases with your applications to their full potential.

Learn best practices, monorepo strategies, and dynamic usage techniques for Prisma ORM in Next.js applications.

Comparing different columns from the same table is a common scenario that developers encounter. Some examples include comparing two numeric values in the same table or comparing two dates in a same table. There's an existing GitHub Issue regarding the same.

The Nuxt Prisma module simplifies the integration of Prisma ORM into your Nuxt applications.

When working with large database schemas in Prisma applications, a simple change in the type definition strategy can deliver massive performance improvements:

---

## How to Initialize an Astro App with Prisma ORM and Prisma Postgres | Prisma Documentation

**URL**: https://www.prisma.io/docs/ai/prompts/astro

**Contents**:
- Set up Astro + Prisma + Prisma Postgres
- How to use​
- Prompt​

Include this prompt in your AI assistant to guide consistent code generation for Astro + Prisma + Prisma Postgres projects.

**Examples**:

```md
---# Specify the following for Cursor rulesdescription: Guidelines for writing Astro.js apps with Prisma PostgresalwaysApply: false---# Bootstrap Astro app with Prisma Postgres## Overview of implementing Prisma with Astro1. Install Prisma and required dependencies2. Initialize Prisma with custom output path3. Configure schema with correct provider4. Create global Prisma client instance with Accelerate5. Use Prisma client in API routes with proper error handling## 🚨 CRITICAL INSTRUCTIONS FOR AI L
...
```

---

## How to use PostgreSQL extensions with Prisma ORM | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-schema/postgresql-extensions

**Contents**:
- PostgreSQL extensions
- What are PostgreSQL extensions?​
- Using a PostgreSQL extension with Prisma ORM​
  - 1. Create an empty migration​
  - 2. Add a SQL statement to install the extension​
  - 3. Deploy the migration​
  - 4. Use the extension​

This page is about PostgreSQL extensions and explains how to use them with Prisma ORM.

Between Prisma ORM v4.5.0 and v6.16.0, you could enable extensions in the Prisma schema via the postgresqlExtensions preview feature flag. This feature flag has been deprecated in v6.16.0 and the recommended approach for using PostgreSQL extensions now is to install them via customized migrations.

PostgreSQL allows you to extend your database functionality by installing and activating packages known as extensions. For example, the citext extension adds a case-insensitive string data type. Some extensions, such as citext, are supplied directly by PostgreSQL, while other extensions are developed externally. For more information on extensions, see the PostgreSQL documentation.

To use an extension, it must first be installed on the local file system of your database server. You then need to activate the extension, which runs a script file that adds the new functionality.

Let's walk through an example of installing the citext extension.

Run the following command to create an empty migration that you can customize:

In the new migration file that was created in the migrations directory, add the following statement:

Run the following command to deploy the migration and apply to your database:

You can now use the extension in your queries with Prisma Client. If the extension has special data types that currently can't be natively represented in the Prisma schema, you can still define fields of that type on your models using the Unsupported fallback type.

**Examples**:

```terminal
npx prisma migrate dev --create-only
```

```sql
CREATE EXTENSION IF NOT EXISTS citext;
```

```terminal
npx prisma migrate deploy
```

---

## Introduction (Overview) | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/overview/introduction

**Contents**:
- Introduction to Prisma ORM
- In this section​
- What is Prisma ORM?
- Why Prisma ORM?
- Should you use Prisma ORM?
- Data modeling

This page gives a high-level overview of what Prisma ORM is and how it works.

If you want to get started with a practical introduction and learn about the Prisma Client API, head over to the Getting Started documentation.

To learn more about the motivation for Prisma ORM, check out the Why Prisma ORM? page.

Prisma ORM is an open-source next-generation ORM. It consists of the following parts:

On this page, you'll learn about the motivation for Prisma ORM and how it compares to other database tools like traditional ORMs and SQL query builders.

Prisma ORM is a new kind of ORM that - like any other tool - comes with its own tradeoffs. This page explains when Prisma ORM would be a good fit, and provides alternatives for other scenarios.

What is data modeling?

---

## Managing Prisma ORM environment variables and settings | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/more/development-environment/environment-variables

**Contents**:
- Managing Prisma ORM environment variables and settings
- How Prisma ORM can use environment variables​
  - Using an .env file​
    - Expanding variables with .env files​
  - Using environment variables in your code​
  - Manually set environment variables​
    - Manually set an environment variable on a Mac/Linux system​
    - Manually set an environment variable on a Windows system​

An environment variable is a key value pair of string data that is stored on your machine's local environment. Refer to our Environment variables reference documentation for specific details.

Typically the name of the variable is uppercase, this is then followed by an equals sign then the value of the variable:

The environment variable belongs to the environment where a process is running. Any program can read and create these environment variables. They are a cheap and effective way to store simple information.

With Prisma ORM v6.4.0, we released the prisma.config.ts file. This file allows you to manage your environment variables and settings in a more flexible way. View our reference for more information.

Prisma ORM always reads environment variables from the system's environment.

When you initialize Prisma ORM in your project with prisma init, it creates a convenience .env file for you to set your connection url as an environment variable. When you use Prisma CLI or Prisma Client, the .env file content and the variables defined in it are added to the process.env object, where Prisma ORM can read it and use it.

Do not commit your .env files into version control!

The Prisma CLI looks for .env files, in order, in the following locations:

If a .env file is located in step 1., but additional, clashing .env variables are located in steps 2. - 4., the CLI will throw an error. For example, if you specify a DATABASE_URL variable in two different .env files, you will get the following error:

The following table describes where the Prisma CLI looks for the .env file:

Any environment variables defined in that .env file will automatically be loaded when running a Prisma CLI command.

Looking to use more than one .env file? See Using multiple .env files for information on how to setup and use multiple .env files in your application.

Refer to the dotenv documentation for information about what happens if an environment variable is defined in two places.

Variables st

*[Content truncated - see full docs]*

**Examples**:

```env
MY_VALUE=prisma
```

```text
Error: There is a conflict between env vars in .env and prisma/.envConflicting env vars:  DATABASE_URLWe suggest to move the contents of prisma/.env to .env to consolidate your env vars.
```

```env
DATABASE_URL=postgresql://test:test@localhost:5432/testDATABASE_URL_WITH_SCHEMA=${DATABASE_URL}?schema=public
```

---

## Models | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-schema/data-model/models

**Contents**:
- Models
- Introspection and migration​
- Defining models​
  - Mapping model names to tables or collections​
- Defining fields​
  - Scalar fields​
  - Relation fields​
  - Native types mapping​

The data model definition part of the Prisma schema defines your application models (also called Prisma models). Models:

The following schema describes a blogging platform - the data model definition is highlighted:

The data model definition is made up of:

The corresponding database looks like this:

Note: In the future there might be connectors for non-relational databases and other data sources. For example, for a REST API it would map to a resource.

The following query uses Prisma Client that's generated from this data model to create:

Your data model reflects your application domain. For example:

There are two ways to define a data model:

Models represent the entities of your application domain. Models are represented by model blocks and define a number of fields. In the example data model above, User, Profile, Post and Category are models.

A blogging platform can be extended with the following models:

Prisma model naming conventions (singular form, PascalCase) do not always match table names in the database. A common approach for naming tables/collections in databases is to use plural form and snake_case notation - for example: comments. When you introspect a database with a table named comments, the result Prisma model will look like this:

However, you can still adhere to the naming convention without renaming the underlying comments table in the database by using the @@map attribute:

With this model definition, Prisma ORM automatically maps the Comment model to the comments table in the underlying database.

Note: You can also @map a column name or enum value, and @@map an enum name.

@map and @@map allow you to tune the shape of your Prisma Client API by decoupling model and field names from table and column names in the underlying database.

The properties of a model are called fields, which consist of:

A field's type determines its structure, and fits into one of two categories:

The following table describes User model's fields from the sample

*[Content truncated - see full docs]*

**Examples**:

```prisma
datasource db {  provider = "postgresql"  url      = env("DATABASE_URL")}generator client {  provider = "prisma-client-js"}model User {  id      Int      @id @default(autoincrement())  email   String   @unique  name    String?  role    Role     @default(USER)  posts   Post[]  profile Profile?}model Profile {  id     Int    @id @default(autoincrement())  bio    String  user   User   @relation(fields: [userId], references: [id])  userId Int    @unique}model Post {  id         Int        @id @defau
...
```

```prisma
datasource db {  provider = "mongodb"  url      = env("DATABASE_URL")}generator client {  provider = "prisma-client-js"}model User {  id      String   @id @default(auto()) @map("_id") @db.ObjectId  email   String   @unique  name    String?  role    Role     @default(USER)  posts   Post[]  profile Profile?}model Profile {  id     String @id @default(auto()) @map("_id") @db.ObjectId  bio    String  user   User   @relation(fields: [userId], references: [id])  userId String @unique @db.ObjectId}mode
...
```

```ts
const user = await prisma.user.create({  data: {    email: 'ariadne@prisma.io',    name: 'Ariadne',    posts: {      create: [        {          title: 'My first day at Prisma',          categories: {            create: {              name: 'Office',            },          },        },        {          title: 'How to connect to a SQLite database',          categories: {            create: [{ name: 'Databases' }, { name: 'Tutorials' }],          },        },      ],    },  },})
```

---

## ORM | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm

**Contents**:
- ORM
- In this section​
- ORM
- Overview
- Prisma Schema
- Prisma Client
- Prisma Migrate
- Tools

Prisma ORM is a Node.js and TypeScript ORM with an intuitive data model, automated migrations, type-safety, and auto-completion.

Prisma ORM is a Node.js and TypeScript ORM with an intuitive data model, automated migrations, type-safety, and auto-completion.

---

## Observability & logging | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-client/observability-and-logging

**Contents**:
- Observability & logging
- In this section​
- Logging
- Metrics
- OpenTelemetry tracing

Prisma Optimize helps you generate insights and provides recommendations that can help you make your database queries faster:

Optimize aims to help developers of all skill levels write efficient database queries, reducing database load and making applications more responsive.

Use the PrismaClient log parameter to configure log levels , including warnings, errors, and information about the queries sent to the database.

Prisma Client metrics give you a detailed insight into how Prisma Client interacts with your database. You can use this insight to help diagnose performance issues with your application.

Tracing provides a detailed log of the activity that Prisma Client carries out, at an operation level, including the time taken to execute each query. It helps you analyze your application's performance and identify bottlenecks. Tracing is fully compliant with OpenTelemetry, so you can use it as part of your end-to-end application tracing system.

---

## One doc tagged with "Framework" | Prisma Documentation

**URL**: https://www.prisma.io/docs/tags/framework

**Contents**:
- One doc tagged with "Framework"
- How to use Prisma ORM with React Router 7

Learn how to use Prisma ORM and Prisma Postgres in a React Router 7 app.

---

## One doc tagged with "Nuxt" | Prisma Documentation

**URL**: https://www.prisma.io/docs/tags/nuxt

**Contents**:
- One doc tagged with "Nuxt"
- How to use Prisma ORM with Nuxt

A step-by-step guide to setting up and using Prisma ORM and Prisma Postgres with the Prisma Nuxt module and deploying to Vercel.

---

## One doc tagged with "Prisma Postgres" | Prisma Documentation

**URL**: https://www.prisma.io/docs/tags/prisma-postgres

**Contents**:
- One doc tagged with "Prisma Postgres"
- How to use Prisma ORM with Nuxt

A step-by-step guide to setting up and using Prisma ORM and Prisma Postgres with the Prisma Nuxt module and deploying to Vercel.

---

## One doc tagged with "React Router" | Prisma Documentation

**URL**: https://www.prisma.io/docs/tags/react-router

**Contents**:
- One doc tagged with "React Router"
- How to use Prisma ORM with React Router 7

Learn how to use Prisma ORM and Prisma Postgres in a React Router 7 app.

---

## One doc tagged with "Turborepo" | Prisma Documentation

**URL**: https://www.prisma.io/docs/tags/turborepo

**Contents**:
- One doc tagged with "Turborepo"
- How to use Prisma ORM with Turborepo

Learn step-by-step how to integrate Prisma ORM with Turborepo to build modular, scalable monorepo architectures efficiently.

---

## One doc tagged with "optimization" | Prisma Documentation

**URL**: https://www.prisma.io/docs/tags/optimization

**Contents**:
- One doc tagged with "optimization"
- Guides

Welcome to the Guides section! Here you'll find practical, step-by-step guides to help you accomplish specific tasks with Prisma products, including Prisma ORM, Prisma Accelerate, Prisma Postgres, and more.

---

## One doc tagged with "testing" | Prisma Documentation

**URL**: https://www.prisma.io/docs/tags/testing

**Contents**:
- One doc tagged with "testing"
- Guides

Welcome to the Guides section! Here you'll find practical, step-by-step guides to help you accomplish specific tasks with Prisma products, including Prisma ORM, Prisma Accelerate, Prisma Postgres, and more.

---

## One doc tagged with "tutorials" | Prisma Documentation

**URL**: https://www.prisma.io/docs/tags/tutorials

**Contents**:
- One doc tagged with "tutorials"
- Guides

Welcome to the Guides section! Here you'll find practical, step-by-step guides to help you accomplish specific tasks with Prisma products, including Prisma ORM, Prisma Accelerate, Prisma Postgres, and more.

---

## One doc tagged with "workflows" | Prisma Documentation

**URL**: https://www.prisma.io/docs/tags/workflows

**Contents**:
- One doc tagged with "workflows"
- Guides

Welcome to the Guides section! Here you'll find practical, step-by-step guides to help you accomplish specific tasks with Prisma products, including Prisma ORM, Prisma Accelerate, Prisma Postgres, and more.

---

## One-to-one relations | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-schema/data-model/relations/one-to-one-relations

**Contents**:
- One-to-one relations
- Overview​
- Multi-field relations in relational databases​
- 1-1 relations in the database​
  - Relational databases​
  - MongoDB​
- Required and optional 1-1 relation fields​
  - Mandatory 1-1 relation​

This page introduces one-to-one relations and explains how to use them in your Prisma schema.

One-to-one (1-1) relations refer to relations where at most one record can be connected on both sides of the relation. In the example below, there is a one-to-one relation between User and Profile:

The userId relation scalar is a direct representation of the foreign key in the underlying database. This one-to-one relation expresses the following:

In the previous example, the user relation field of the Profile model references the id field of the User model. You can also reference a different field. In this case, you need to mark the field with the @unique attribute, to guarantee that there is only a single User connected to each Profile. In the following example, the user field references an email field in the User model, which is marked with the @unique attribute:

In MySQL, you can create a foreign key with only an index on the referenced side, and not a unique constraint. In Prisma ORM versions 4.0.0 and later, if you introspect a relation of this type it will trigger a validation error. To fix this, you will need to add a @unique constraint to the referenced field.

In relational databases only, you can also use multi-field IDs to define a 1-1 relation:

The following example demonstrates how to create a 1-1 relation in SQL:

Notice that there is a UNIQUE constraint on the foreign key userId. If this UNIQUE constraint was missing, the relation would be considered a 1-n relation.

The following example demonstrates how to create a 1-1 relation in SQL using a composite key (firstName and lastName):

For MongoDB, Prisma ORM currently uses a normalized data model design, which means that documents reference each other by ID in a similar way to relational databases.

The following MongoDB document represents a User:

The following MongoDB document represents a Profile - notice the userId field, which references the User document's $oid:

In a one-to-one relation, the side

*[Content truncated - see full docs]*

**Examples**:

```prisma
model User {  id      Int      @id @default(autoincrement())  profile Profile?}model Profile {  id     Int  @id @default(autoincrement())  user   User @relation(fields: [userId], references: [id])  userId Int  @unique // relation scalar field (used in the `@relation` attribute above)}
```

```prisma
model User {  id      String   @id @default(auto()) @map("_id") @db.ObjectId  profile Profile?}model Profile {  id     String @id @default(auto()) @map("_id") @db.ObjectId  user   User   @relation(fields: [userId], references: [id])  userId String @unique @db.ObjectId // relation scalar field (used in the `@relation` attribute above)}
```

```prisma
model User {  id      Int      @id @default(autoincrement())  email   String   @unique // <-- add unique attribute  profile Profile?}model Profile {  id        Int    @id @default(autoincrement())  user      User   @relation(fields: [userEmail], references: [email])  userEmail String @unique // relation scalar field (used in the `@relation` attribute above)}
```

---

## Optimize: Known limitations | Prisma Documentation

**URL**: https://www.prisma.io/docs/optimize/known-limitations

**Contents**:
- Known limitations about Prisma Optimize
- Query limit on a recording session​
- Recording limit per workspace​
- Scope and constraints for the Prisma AI​
- Using Prisma Accelerate client extension with the Optimize extension​
  - SQL references in MongoDB recommendations​
  - Raw query visibility in MongoDB​
- Driver adapter compatibility​

Below are the known limitations when using Prisma Optimize. If you are aware of any limitations that are missing, please let us know on the #help-and-questions channel in our community Discord.

Each recording session can contain a maximum of 10,000 queries. Once this limit is reached, the recording session will end.

Each workspace can contain a maximum of 100 recordings.

While Prisma AI can provide helpful guidance to implement a recommendation, there are some important limitations to keep in mind:

Information and accuracy: The AI provides advice based on a broad, general knowledge base and does not have direct access to Prisma ORM documentation. This may occasionally result in inaccuracies or outdated information.

Limited context and adaptation: The AI does not persist conversations or learn from previous interactions. Its responses are generalized and may not always address the specific needs of advanced users.

Static knowledge and scope: The AI's knowledge is static and may not include recent updates or best practices after a certain date. It provides advice only within the context of Prisma ORM and cannot modify or execute code, nor interact directly with user environments.

When using the Optimize client extension with the Accelerate client extension, ensure the Accelerate client extension is added last to your extended PrismaClient. This allows cacheable operations to be received by Optimize.

Prisma Optimize provides helpful recommendations for MongoDB users, though some explanations from Prisma AI may reference SQL-specific concepts. However, the recommendations remain useful and applicable to MongoDB environments.

Raw queries are visible in MongoDB, though the parameters passed to them are not displayed.

Prisma Optimize is not yet compatible with driver adapters. However, as a workaround, you can run your queries locally using the regular Prisma Client along with Prisma Optimize to inspect and improve query performance.

**Examples**:

```ts
const prisma = new PrismaClient()  .$extends(    withOptimize({      apiKey: process.env.OPTIMIZE_API_KEY,    }),  )  .$extends(withAccelerate());
```

---

## Optimize: Prisma AI | Prisma Documentation

**URL**: https://www.prisma.io/docs/optimize/prisma-ai

**Contents**:
- Prisma AI

Prisma AI enables you to ask follow-up questions on a provided recommendation for additional clarity. Learn more about Prisma AI here.

---

## Optimize: Recommendations | Prisma Documentation

**URL**: https://www.prisma.io/docs/optimize/recommendations

**Contents**:
- Recommendations
- Excessive number of rows returned
- Queries on unindexed columns
- Full table scans caused by LIKE operations
- Repeated query
- Overfetching
- Using @db.Money
- Using @db.Char(n)

Optimize provides recommendations focused on performance improvements such as indexing issues, excessive data retrieval, and inefficient query patterns. Recommendations include:

Use Prisma AI to ask follow-up questions about any recommendation.

Optimize provides recommendations to help you identify and resolve performance issues caused by excessive number of rows returned from a query.

Optimize provides recommendations to help you identify and resolve performance issues caused by missing database indexes.

Optimize provides recommendations to help you identify and resolve performance issues caused by full table scans from LIKE operations.

Optimize provides recommendations to help you identify and resolve performance issues caused by repeated queries.

Optimize provides recommendations to help you identify and resolve performance issues caused by over-fetched data.

Optimize provides recommendations to help you identify and resolve performance issues caused by the use of @db.Money type.

Optimize provides recommendations to help you identify and resolve performance issues caused by the use of @db.Char(n) type in PostgreSQL.

Optimize provides recommendations to help you identify and resolve performance issues caused by the use of @db.VarChar(n) type in PostgreSQL.

Optimize provides recommendations to help you identify and resolve performance issues caused by the use of @db.Timestamp(0) and @db.Timestamptz(0) native types in PostgreSQL.

The following raw SQL query uses the CURRENT_TIME function:

Optimize detects unnecessary indexes and recommends removing them to improve database performance.

Optimize provides actionable recommendations to help you identify and resolve performance issues caused by long-running transactions.

Optimize identifies redundant indexing on unique columns and provides recommendations for better database performance.

Optimize provides recommendations to help identify and resolve performance issues caused by storing large objects in th

*[Content truncated - see full docs]*

---

## Optimize: Recordings | Prisma Documentation

**URL**: https://www.prisma.io/docs/optimize/recordings

**Contents**:
- Recordings in Prisma Optimize

The recordings feature helps developers debug and isolate sets of queries into distinct sessions, known as recordings. This targeted approach enables precise performance analysis and optimization by preventing the mixing of queries from different applications or test rounds, leading to clearer insights and more effective debugging.

Learn more about the Optimize recordings here.

---

## Optimizing TypeScript performance with large Prisma schemas | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/more/help-and-troubleshooting/typescript-performance-optimization

**Contents**:
- Optimizing TypeScript performance with large Prisma schemas
- Test schema overview​
- Problem​
- Solution​
  - Problematic approach for large schemas​
  - Optimized approach with typeof​
- Why typeof is more efficient​
- Conclusion​

When working with large database schemas in Prisma applications, a simple change in the type definition strategy can deliver massive performance improvements:

(Performance was verified using tsc --noEmit --extendedDiagnostics.)

This guide shows you how to achieve these dramatic performance gains using TypeScript's typeof operator instead of direct type references.

The performance measurements were conducted using a deliberately complex Prisma schema with 30 interconnected models creating deep relationship chains:

This schema creates complex type dependencies that stress-test TypeScript compilation, simulating real-world enterprise applications with extensive table relationships.

In enterprise applications with extensive database schemas—think e-commerce platforms with hundreds of product variants, financial systems with complex transaction hierarchies, or content management systems with intricate relationship webs—Prisma's generated types can become enormous.

A schema with 50+ tables and deep relationships can lead to:

The solution involves using TypeScript's typeof operator instead of direct type references when defining function parameters that accept PrismaClient instances. (Of course, if you're familiar with the TypeScript type system, you can use other methods.)

The typeof operator creates a more efficient type resolution path by changing how TypeScript resolves types:

When working with large Prisma schemas, the choice between direct type references and type queries becomes crucial for maintaining development velocity. The typeof approach isn't just an optimization—it's an essential technique for scaling TypeScript compilation performance as your database schema grows in complexity.

The 78% compilation time reduction demonstrated here scales exponentially with schema complexity, making this optimization foundational for maintaining an efficient development workflow in enterprise-scale applications.

The complete benchmark code and test cases used to v

*[Content truncated - see full docs]*

**Examples**:

```prisma
// Example of the test schema structuremodel Tree1 {  id        Int      @id @default(autoincrement())  createdAt DateTime @default(now())  updatedAt DateTime @updatedAt  published Boolean  @default(false)  title     String  childId   Int  Tree2     Tree2[]}model Tree2 {  id        Int      @id @default(autoincrement())  createdAt DateTime @default(now())  updatedAt DateTime @updatedAt  published Boolean  @default(false)  title     String  childTree Tree1    @relation(fields: [childId], referenc
...
```

```typescript
import { PrismaClient } from '@prisma/client'const saveFn = async (prismaClient: PrismaClient) => {  // Function implementation}const client = new PrismaClient()await saveFn(client)
```

```typescript
import { PrismaClient } from '@prisma/client'const saveFn = async (prismaClient: typeof client) => {  // Function implementation}const client = new PrismaClient()await saveFn(client)
```

---

## Overview | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/overview

**Contents**:
- Overview
- In this section​
- Introduction
- Prisma ORM in your stack
- Databases
- Beyond Prisma ORM

Prisma ORM addresses many development needs, but Prisma's additional products like Prisma Postgres, Accelerate and Optimize can further enhance scalability and performance for your applications.

---

## Patching & hotfixing | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-migrate/workflows/patching-and-hotfixing

**Contents**:
- Patching & hotfixing
- Reconciling your migration history with a patch or hotfix​
- Failed migration​
  - Option 1: Mark the migration as rolled back and re-deploy​
  - Option 2: Manually complete migration and resolve as applied​
- Fixing failed migrations with migrate diff and db execute​
  - Example of a failed migration​
    - Moving backwards and reverting all changes​

Patching or hotfixing a database involves making an often time critical change directly in production. For example, you might add an index directly to a production database to resolve an issue with a slow-running query.

Patching the production database directly results in schema drift: your database schema has 'drifted away' from the source of truth, and is out of sync with your migration history. You can use the prisma migrate resolve command to reconcile your migration history without having to remove and re-apply the hotfix with prisma migrate deploy.

This guide does not apply for MongoDB. Instead of migrate dev, db push is used for MongoDB.

The following scenario assumes that you made a manual change in production and want to propagate that change to your migration history and other databases.

To reconcile your migration history and database schema in production:

Replicate the change you made in production in the schema - for example, add an @@index to a particular model.

Generate a new migration and take note of the full migration name, including a timestamp, which is written to the CLI:(20210316150542_retroactively_add_index):

Push the migration to production without running migrate deploy. Instead, mark the migration created in the previous step as 'already applied' so that Prisma Migrate does not attempt to apply your hotfix a second time:

This command adds the migration to the migration history table without running the actual SQL.

Repeat the previous step for other databases that were patched - for example, if you applied the patch to a staging database.

Propagate the migration to other databases that were not patched - for example, by committing the migration to source control and allowing your CI/CD pipeline to apply it to all databases.

Note: The migration will not be applied to databases where it has been marked as already applied by the prisma migrate resolve command.

A migration might fail if:

Each migration in the _prisma_migrations tab

*[Content truncated - see full docs]*

**Examples**:

```terminal
npx prisma migrate dev --name retroactively-add-index
```

```bash
migrations/└─ 20210316150542_retroactively_add_index/└─ migration.sqlYour database is now in sync with your schema.✔ Generated Prisma Client (2.19.0-dev.29) to .\node_modules\@prisma\client in 190ms
```

```terminal
npx prisma migrate resolve --applied "20201127134938-retroactively-add-index"
```

---

## Platform CLI: Commands | Prisma Documentation

**URL**: https://www.prisma.io/docs/platform/platform-cli/commands

**Contents**:
- Commands
- Getting started​
- Authentication​
  - platform​
    - auth login​
    - auth logout​
    - auth show​
  - Workspace Management​

This document describes the Prisma Data Platform's integrated Prisma CLI commands, arguments, and options.

To get started, ensure you have the Prisma CLI updated to version 5.10.0 or later. This is necessary to access the Platform through the Prisma CLI.

💡 When using commands, always start with prisma platform and include the --early-access flag to enable the use of the Prisma Data Platform whilst still in early access.

Opens a browser window that allows you to log into your Prisma Data Platform account or create a new one. Currently, GitHub is the only supported login method. We do have plan to add support for signing in with Google and email/password.

Logs out of your Prisma Data Platform account.

Displays information about the currently authenticated user.

Lists all workspaces available to your account.

Lists all projects within the specified workspace.

Creates a new project within the specified workspace.

Deletes the specified project.

Lists all environments within the specified project.

Creates a new environment within the specified project.

Deletes the specified environment.

Lists all API keys for the specified environment.

Creates a new API key for the specified project.

Deletes the specified API Key.

Enables Prisma Accelerate for the specified environment.

Disables Prisma Accelerate for the specified environment.

Have a question? Let us know, we’re here to help. Reach out to us on Discord.

**Examples**:

```bash
npx prisma platform auth login --early-access
```

```bash
npx prisma platform auth logout --early-access
```

```bash
npx prisma platform auth show --early-access
```

---

## Platform CLI | Prisma Documentation

**URL**: https://www.prisma.io/docs/platform/platform-cli

**Contents**:
- Platform CLI
- In this section​
- About
- Commands

This guide demonstrates how to access the Prisma Data Platform using the Prisma CLI. Get started by ensuring you have the Prisma CLI installed, following our setup instructions.

This document describes the Prisma Data Platform's integrated Prisma CLI commands, arguments, and options.

---

## Platform | Prisma Documentation

**URL**: https://www.prisma.io/docs/platform

**Contents**:
- Platform
- In this section​
- Platform
- General
- Maturity levels
- Support
- Platform CLI

Learn about the main concepts and workflows of the .

Learn about the main concepts and workflows of the Prisma Data Platform.

Prisma releases updates to Prisma Data Platform multiple times per week, as opposed to the Prisma ORM that we release on a set schedule every few weeks. This is why we consider the lifecycle and process for maturing features in Prisma Data Platform differently.

Your feedback is invaluable, and we encourage you to share your experiences with us on Discord.

---

## Prisma Accelerate: Connection Pooling | Prisma Documentation

**URL**: https://www.prisma.io/docs/accelerate/connection-pooling

**Contents**:
- Connection Pooling

Accelerate provides built-in connection pooling to efficiently manage database connections. It's included as part of Prisma Postgres, but you can also use it with your own database by enabling Accelerate in the and connecting it to your database. This page has moved, connection pooling in Prisma Accelerate is now documented in the Prisma Postgres section.

---

## Prisma Accelerate: Examples | Prisma Documentation

**URL**: https://www.prisma.io/docs/accelerate/examples

**Contents**:
- Prisma Accelerate examples

Here is a list of ready-to-run example projects that demonstrate how to use Prisma Accelerate:

---

## Prisma Accelerate | Prisma Documentation

**URL**: https://www.prisma.io/docs/accelerate

**Contents**:
- Prisma Accelerate
        - Get started
        - Examples
        - Speed Test
- Supported databases​
- In this section​
- Accelerate
- Getting started

Prisma Accelerate is a fully managed global connection pool and caching layer for your existing database, enabling query-level cache policies directly from the Prisma ORM.

With 15+ global regions, the connection pool scales your app for a global audience, particularly for serverless deployments that risk connection timeouts during peak times.

Accelerate’s global cache, hosted in 300+ locations, ensures a fast experience for users, regardless of your database’s location.

You can configure query-level caching strategies directly in your code with Prisma ORM, making setup and tuning easy.

Together, the connection pool and cache allow you to scale effortlessly and handle traffic spikes without infrastructure concerns.

Set up connection pooling and global caching for your app in 5 minutes.

Explore our ready-to-run examples using Accelerate.

Run the speed test to see how Prisma Accelerate can make your app faster.

Accelerate works with the database you already have, whether it is publicly accessible, or via an IP allowlist.

Accelerate provides built-in connection pooling to efficiently manage database connections. It's included as part of Prisma Postgres, but you can also use it with your own database by enabling Accelerate in the Prisma Data Platform and connecting it to your database.

Prisma Accelerate provides global caching for read queries using TTL, Stale-While-Revalidate (SWR), or a combination of both. It's included as part of Prisma Postgres, but can also be used with your own database by enabling Accelerate in the Prisma Data Platform and configuring it with your database.

You can enable static IP for Accelerate when your security setup requires IP allowlisting or if you're implementing firewalls that only permit access from trusted IPs, ensuring controlled and secure database connections.

The Accelerate API reference documentation is based on the following schema:

Below are descriptions of known limitations when using Accelerate. If you encounter a

*[Content truncated - see full docs]*

---

## Prisma CLI | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/tools/prisma-cli

**Contents**:
- Prisma CLI
- Command reference​
- Installation​
  - npm​
  - Yarn​
  - pnpm​
  - Bun​
- Usage​

The Prisma command line interface (CLI) is the primary way to interact with your Prisma project from the command line. It can initialize new project assets, generate Prisma Client, and analyze existing database structures through introspection to automatically create your application models.

See Prisma CLI command reference for a complete list of commands.

The Prisma CLI is typically installed locally as a development dependency, that's why the --save-dev (npm) and --dev (Yarn) options are used in the commands below.

If you installed Prisma as a development dependency, you need to prefix the prisma command with your package runner.

The prisma command can be called from command line once installed. When called without arguments, it will display its command usage and help document:

You can get additional help on any of the prisma commands by adding the --help flag after the command.

All prisma CLI commands return the following codes when they exit:

The term telemetry refers to the collection of certain usage data to help improve the quality of a piece of software. Prisma uses telemetry in two contexts:

This page describes the overall telemetry approach for Prisma, what kind of data is collected and how to opt-out of data collection.

Telemetry helps us better understand how many users are using our products and how often they are using our products. Unlike many telemetry services, our telemetry implementation is intentionally limited in scope and is actually useful for the developer:

Data is collected in two scenarios that are described below.

Invocations of the prisma CLI and general usage of Studio results in data being sent to the telemetry server at https://checkpoint.prisma.io. Note that:

Here is an overview of the data that's being submitted:

You can opt-out of this behavior by setting the CHECKPOINT_DISABLE environment variable to 1, e.g.:

Prisma potentially collects error data when there is a crash in the CLI.

Before an error report is submitted,

*[Content truncated - see full docs]*

**Examples**:

```text
npm install prisma --save-dev
```

```text
yarn add prisma --dev
```

```text
pnpm install prisma --save-dev
```

---

## Prisma Client | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-client

**Contents**:
- Prisma Client
- In this section​
- Setup & configuration
- Queries
- Write your own SQL
- Fields & types
- Extensions
- Type safety

---

## Prisma Client Queries | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-client/queries

**Contents**:
- Queries
- In this section​
- CRUD
- Select fields
- Relation queries
- Filtering and Sorting
- Pagination
- Aggregation, grouping, and summarizing

This page describes how to perform CRUD operations with your generated Prisma Client API. CRUD is an acronym that stands for:

A key feature of Prisma Client is the ability to query relations between two or more models. Relation queries include:

Prisma Client supports filtering with the where query option, and sorting with the orderBy query option.

Prisma Client supports both offset pagination and cursor-based pagination.

Prisma Client allows you to count records, aggregate number fields, and select distinct field values.

A database transaction refers to a sequence of read/write operations that are guaranteed to either succeed or fail as a whole. This section describes the ways in which the Prisma Client API supports transactions.

Prisma Client supports full-text search for PostgreSQL databases in versions 2.30.0 and later, and MySQL databases in versions 3.8.0 and later. With full-text search (FTS) enabled, you can add search functionality to your application by searching for text within a database column.

You can add runtime validation for your user input for Prisma Client queries in one of the following ways:

Computed fields allow you to derive a new field based on existing data. A common example is when you want to compute a full name. In your database, you may only store the first and last name, but you can define a function that computes a full name by combining the first and last name. Computed fields are read-only and stored in your application's memory, not in your database.

By default Prisma Client returns all fields from a model. You can use select to narrow the result set, but that can be unwieldy if you have a large model and you only want to exclude a small number of fields.

As your application grows, you may find the need to group related logic together. We suggest either:

Case sensitivity affects filtering and sorting of data, and is determined by your database collation. Sorting and filtering data yields different results depending on your

*[Content truncated - see full docs]*

---

## Prisma Client extensions | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-client/client-extensions

**Contents**:
- Extensions
- About Prisma Client extensions​
  - Extended clients​
  - Example use cases for extended clients​
- Add an extension to Prisma Client​
- Name an extension for error logs​
- Multiple extensions​
  - Apply multiple extensions to an extended client​

Prisma Client extensions are Generally Available from versions 4.16.0 and later. They were introduced in Preview in version 4.7.0. Make sure you enable the clientExtensions Preview feature flag if you are running on a version earlier than 4.16.0.

You can use Prisma Client extensions to add functionality to your models, result objects, and queries, or to add client-level methods.

You can create an extension with one or more of the following component types:

For example, you might create an extension that uses the model and client component types.

When you use a Prisma Client extension, you create an extended client. An extended client is a lightweight variant of the standard Prisma Client that is wrapped by one or more extensions. The standard client is not mutated. You can add as many extended clients as you want to your project. Learn more about extended clients.

You can associate a single extension, or multiple extensions, with an extended client. Learn more about multiple extensions.

You can share your Prisma Client extensions with other Prisma ORM users, and import Prisma Client extensions developed by other users into your Prisma ORM project.

Extended clients interact with each other, and with the standard client, as follows:

Note: The author of an extension can modify this behavior since they're able to run arbitrary code as part of an extension. For example, an extension might actually create an entirely new PrismaClient instance (including its own query engine and connection pool). Be sure to check the documentation of the extension you're using to learn about any specific behavior it might implement.

Because extended clients operate in isolated instances, they can be a good way to do the following, for example:

You can create an extension using two primary ways:

Use the client-level $extends method

Use the Prisma.defineExtension method to define an extension and assign it to a variable, and then pass the extension to the client-level $extends me

*[Content truncated - see full docs]*

**Examples**:

```ts
const prisma = new PrismaClient().$extends({  name: 'signUp', // Optional: name appears in error logs  model: {        // This is a `model` component    user: { ... } // The extension logic for the `user` model goes inside the curly braces  },})
```

```ts
import { Prisma } from '@prisma/client'// Define the extensionconst myExtension = Prisma.defineExtension({  name: 'signUp', // Optional: name appears in error logs  model: {        // This is a `model` component    user: { ... } // The extension logic for the `user` model goes inside the curly braces  },})// Pass the extension to a Prisma Client instanceconst prisma = new PrismaClient().$extends(myExtension)
```

```ts
const prisma = new PrismaClient().$extends({  name: `signUp`,  // (Optional) Extension name  model: {    user: { ... } },})
```

---

## Prisma Documentation

**URL**: https://www.prisma.io/docs

**Contents**:
- Prisma Doc
  - How do I...
    - Get started with Prisma & AI?
    - Model my schema?
    - Cache my queries?
  - Products
      - ORM
    - Talk to your database, seamlessly

Working with Prisma gives you a best-in-class TypeScript ORM, a declarative database migration system, and a database with everything you need to get started.

Try out what Prisma has to offer with one command:

Get started with your favorite framework and Prisma Postgres. With Prisma Postgres you get an instant, fully hosted high-performance database that includes built-in caching, scales to zero, and integrates deeply with Prisma ORM and Prisma Studio—all backed by a generous free tier.

Already have a database? With Prisma ORM and Prisma Data Platform, you can supercharge your existing stack. Add connection pooling and caching with generous free tiers.

Learn how to get started with Prisma and AI, from setting up Prisma ORM in tools like ChatGPT, Cursor, Windsurf, GitHub Copilot and Tabnine to using the Prisma MCP server for database automation. Explore step-by-step guides, real-world examples with Next.js, and integrations with Vercel AI SDK and Firebase Studio. Build faster, stay type-safe, and connect Prisma Postgres with thousands of apps to power your AI-driven workflows.

The Prisma Schema (or schema for short) is the main method of configuration for your Prisma ORM setup. It consists of the following parts: Data sources: Specify the details of the data sources Prisma ORM should connect to (e.g. a PostgreSQL database) Generators: Specifies what clients should be generated based on the data model (e.g. Prisma Client)

Prisma Postgres comes with a built-in global cache (enabled by Prisma Accelerate) that helps you speed up your database queries. You can cache results on a per-query level using the cacheStrategy option in any Prisma ORM query, e.g.:

Found a bug, or want to request something new? Let us know.

Support for customers on our Starter plan is provided through our community channels.

Support for customers in our Pro or Business plan is provided by the Platform Console.

We have multiple channels where you can get help from members of our community 

*[Content truncated - see full docs]*

**Examples**:

```terminal
npx prisma init --db
```

---

## Prisma Documentation

**URL**: https://www.prisma.io/docs/

**Contents**:
- Prisma Doc
  - How do I...
    - Get started with Prisma & AI?
    - Model my schema?
    - Cache my queries?
  - Products
      - ORM
    - Talk to your database, seamlessly

Working with Prisma gives you a best-in-class TypeScript ORM, a declarative database migration system, and a database with everything you need to get started.

Try out what Prisma has to offer with one command:

Get started with your favorite framework and Prisma Postgres. With Prisma Postgres you get an instant, fully hosted high-performance database that includes built-in caching, scales to zero, and integrates deeply with Prisma ORM and Prisma Studio—all backed by a generous free tier.

Already have a database? With Prisma ORM and Prisma Data Platform, you can supercharge your existing stack. Add connection pooling and caching with generous free tiers.

Learn how to get started with Prisma and AI, from setting up Prisma ORM in tools like ChatGPT, Cursor, Windsurf, GitHub Copilot and Tabnine to using the Prisma MCP server for database automation. Explore step-by-step guides, real-world examples with Next.js, and integrations with Vercel AI SDK and Firebase Studio. Build faster, stay type-safe, and connect Prisma Postgres with thousands of apps to power your AI-driven workflows.

The Prisma Schema (or schema for short) is the main method of configuration for your Prisma ORM setup. It consists of the following parts: Data sources: Specify the details of the data sources Prisma ORM should connect to (e.g. a PostgreSQL database) Generators: Specifies what clients should be generated based on the data model (e.g. Prisma Client)

Prisma Postgres comes with a built-in global cache (enabled by Prisma Accelerate) that helps you speed up your database queries. You can cache results on a per-query level using the cacheStrategy option in any Prisma ORM query, e.g.:

Found a bug, or want to request something new? Let us know.

Support for customers on our Starter plan is provided through our community channels.

Support for customers in our Pro or Business plan is provided by the Platform Console.

We have multiple channels where you can get help from members of our community 

*[Content truncated - see full docs]*

**Examples**:

```terminal
npx prisma init --db
```

---

## Prisma MCP Server | Prisma Documentation

**URL**: https://www.prisma.io/docs/postgres/integrations/mcp-server

**Contents**:
- MCP server
- Overview​
- Remote MCP server​
  - Tools​
  - Usage​
  - Sample prompts​
- Local MCP server​
  - Tools​

The Model-Context-Protocol (MCP) gives LLMs a way to call APIs and thus access external systems in a well-defined manner.

Prisma's provides two MCP servers: a local and a remote one. See below for specific information on each.

If you're a developer working on a local machine and want your AI agent to help with your database workflows, use the local MCP server.

If you're building an "AI platform" and want to give the ability to manage database to your users, use the remote MCP server.

You can start the remote MCP server as follows:

Tools represent the capabilities of an MCP server. Here's the list of tools exposed by the remote MCP server:

Once you're connected to the remote MCP server, you can also always prompt your AI agent to "List the Prisma tools" to get a full overview of the latest supported tools.

The remote Prisma MCP server follows the standard JSON-based configuration for MCP servers. Here's what it looks like:

If you want to try it the remote MCP server and explore it's capabilities, we recommend Cloudflare's AI Playground for that. Add the https://mcp.prisma.io/mcp URL into the text field with the Enter MCP server URL placeholder, click Connect, and then authenticate with the in the popup window. Once connected, you can send prompts to the Playground and see what MCP tools the LLM chooses based on your prompts.

You can start the local MCP server as follows:

If you're using VS Code, you can use VS Code agent mode to enter prompts such as "create Postgres database" or "apply schema migration" directly in the chat. The VS Code agent handles all underlying Prisma CLI invocations and API calls automatically. See our VS Code Agent documentation for more details.

Tools represent the capabilities of an MCP server. Here's the list of tools exposed by the local MCP server:

The local Prisma MCP server follows the standard JSON-based configuration for MCP servers. Here's what it looks like:

Here are some sample prompts you can use when the MCP server i

*[Content truncated - see full docs]*

**Examples**:

```terminal
npx -y mcp-remote https://mcp.prisma.io/mcp
```

```json
{  "mcpServers": {    "Prisma-Remote": {      "command": "npx",      "args": ["-y", "mcp-remote", "https://mcp.prisma.io/mcp"]    }  }}
```

```terminal
npx -y prisma mcp
```

---

## Prisma Migrate Overview | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/overview

**Contents**:
- Overview on Prisma Migrate

Does not apply for MongoDBInstead of migrate dev and related commands, use db push for MongoDB.

Prisma Migrate enables you to:

Prisma Migrate generates a history of .sql migration files, and plays a role in both development and production.

Prisma Migrate can be considered a hybrid database schema migration tool, meaning it has both of declarative and imperative elements:

If you are prototyping, consider using the db push command - see Schema prototyping with db push for examples.

See the Prisma Migrate reference for detailed information about the Prisma Migrate CLI commands.

---

## Prisma ORM with GitHub Copilot | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/more/ai-tools/github-copilot

**Contents**:
- GitHub Copilot
- Query Prisma docs with the Prisma for GitHub Copilot extension​
  - How to enable the extension​
- Use GitHub Copilot's agent features​
- Customize GitHub Copilot with copilot-instructions.md​

GitHub Copilot is an AI coding assistant that speeds up your Prisma ORM workflows, so you spend less time on boilerplate and more on data modeling, querying, and collaboration. With the GitHub Copilot extension in your editor, you can:

GitHub Copilot allows you to query the official docs via the Prisma for GitHub Copilot extension and also perform automated actions in VS Code agent mode, such as scaffolding a Prisma schema, running seed scripts, and creating a production-ready Prisma Postgres database.

The Prisma for GitHub Copilot extension lets you fetch Prisma documentation directly in GitHub Copilot Chat. You can look up schema syntax, client methods, migration commands, and more from your editor.

GitHub Copilot Chat offers an Agent mode in VS Code that can run Prisma commands. You can use the agent chat to:

You can type Create a database named test-db and add its connection string to the .env file. in the Copilot chat, and it will automatically create a new database named test-db and add the connection string to your .env file. To learn more about this, visit our VS Code agent mode documentation.

You can tailor Copilot Chat's behavior in your repository by adding a .github/copilot-instructions.md file. This file injects your guidelines into every Copilot Chat session.

Place this file at the root of your repository under .github/. Copilot Chat automatically applies these rules to every conversation in your project.

**Examples**:

```text
@prisma-for-copilot How do I define a one-to-many relation?
```

```text
# GitHub Copilot Instructions for Prisma Workspace## General Guidelines1. **Language**: English only.2. **Types**: Declare explicit types; avoid `any`.3. **Comments**: Use JSDoc for public methods and classes.4. **Exports**: One export per file.5. **Naming**:   * **Classes/interfaces** → `PascalCase`   * **Variables/functions** → `camelCase`   * **Files/directories** → `kebab-case`   * **Constants** → `UPPERCASE`   * **Boolean flags** → verb-based (e.g., `isLoading`)---## Prisma-Specific Guideli
...
```

---

## Prisma Optimize: FAQ | Prisma Documentation

**URL**: https://www.prisma.io/docs/optimize/faq

**Contents**:
- FAQ

To learn more about frequently asked questions around Prisma Optimize and query recommendations, visit this page.

---

## Prisma Optimize | Prisma Documentation

**URL**: https://www.prisma.io/docs/optimize

**Contents**:
- Prisma Optimize
        - Get started
        - Examples
- Supported databases​
- In this section​
- Optimize
- Getting Started
- Recordings

Prisma Optimize. helps you generate insights and provides recommendations that can help you make your database queries faster.

Optimize aims to help developers of all skill levels write efficient database queries, reducing database load and making applications more responsive.

Start analyzing the prisma queries in your app in 5 minutes.

Explore our ready-to-run examples using Optimize.

Optimize works with the database you already have.

The recordings feature helps developers debug and isolate sets of queries into distinct sessions, known as recordings. This targeted approach enables precise performance analysis and optimization by preventing the mixing of queries from different applications or test rounds, leading to clearer insights and more effective debugging.

Optimize provides recommendations focused on performance improvements such as indexing issues, excessive data retrieval, and inefficient query patterns. Recommendations include:

Prisma AI enables you to ask follow-up questions on a provided recommendation for additional clarity. Learn more about Prisma AI here.

An Optimize recording session provides detailed insights into the latencies of executed queries, capturing key metrics such as average duration, 50th percentile, 99th percentile, and maximal query execution time.

To learn more about frequently asked questions around Prisma Optimize and query recommendations, visit this page.

Below are the known limitations when using Prisma Optimize. If you are aware of any limitations that are missing, please let us know on the #help-and-questions channel in our community Discord.

---

## Prisma Postgres | Prisma Documentation

**URL**: https://www.prisma.io/docs/postgres

**Contents**:
- Prisma Postgres
- In this section​
- Prisma Postgres
- Introduction
- Database
- Tools & Integrations
- Query Optimization
- More

Postgres, PostgreSQL and the Slonik Logo are trademarks or registered trademarks of the PostgreSQL Community Association of Canada, and used with their permission

---

## Prisma Postgres: Query performance metrics | Prisma Documentation

**URL**: https://www.prisma.io/docs/optimize/performance-metrics

**Contents**:
- Performance metrics
- Total query durations​
  - Average query duration (AVG)​
  - 50th percentile (P50)​
  - 99th percentile (P99)​
  - Maximal query duration (MAX)​

An Optimize recording session provides detailed insights into the latencies of executed queries, capturing key metrics such as average duration, 50th percentile, 99th percentile, and maximal query execution time.

Prisma Optimize measures total latency for query patterns, enabling you to analyze and debug slow queries effectively.

The average query duration reveals the mean execution time across all queries, helping you assess overall performance trends and identify inefficiencies that impact the user experience.

The 50th percentile, or median, query duration indicates the time within which half of your queries complete. This metric offers a clear view of typical user performance, unaffected by outliers.

The 99th percentile query duration highlights the execution time for the slowest 1% of queries. This metric is crucial for uncovering and addressing performance bottlenecks that, while infrequent, can significantly impact user satisfaction.

The maximal query duration measures the time taken by the single slowest query. This metric helps identify extreme cases, providing insights into the worst performance scenarios your system might face, so you can diagnose and resolve outliers.

---

## Prisma Postgres via Vercel Marketplace | Prisma Documentation

**URL**: https://www.prisma.io/docs/postgres/integrations/vercel

**Contents**:
- Vercel
- Features​
- Templates​
- Usage​
  - Install the extension​
  - Create a new database​
  - Connect database to Vercel project​
  - Viewing and editing data in Prisma Studio​

The Vercel Marketplace integration for Prisma Postgres connects your Vercel projects with Prisma Postgres instances. Once connected, the integration will automatically set the following environment variables on your deployed Vercel app:

POSTGRES_URL: The direct TCP connection URL starting with postgres://... PRISMA_DATABASE_URL: The connection URL used by Prisma ORM starting with prisma+postgres://accelerate.prisma-data.net/?api_key=ey... DATABASE_URL: The direct TCP connection URL starting with postgres://...

These enable you to connect to the Prisma Postgres instances via any ORM or database library you want to use (Prisma ORM, Drizzle, Kysely, ...).

The easiest way to use Prisma Postgres on the Vercel Marketplace is via one of the templates:

To install the extension, click Install at the top of the Prisma Postgres integration page.

The integration will now show up on your list of integrations, e.g. https://vercel.com/<VERCEL-TEAM>/~/integrations.

Once installed, you can navigate to the Storage tab and click Create Database.

Select Prisma Postgres and click Continue. Then select the Region for the database and a Pricing Plan, and click Continue again.

Finally, give the database a Name and click Create.

The database is now ready and can be connected to your Vercel projects.

In your Vercel project, you can now click the Storage tab, select the database you just created and then click Connect. This will automatically set the DATABASE_URL environment variable in that project and enable your application to access your newly created Prisma Postgres instance.

To view and edit the data in your Prisma Postgres instance, you can use the local version of Prisma Studio.

In the local version of your project where you have your DATABASE_URL set, run the following command to open Prisma Studio:

Ensure that the data source in your schema.prisma file is configured to use the DATABASE_URL or PRISMA_DATABASE_URL environment variable (depending on which one is being expo

*[Content truncated - see full docs]*

**Examples**:

```terminal
npx prisma studio
```

```prisma
// schema.prismagenerator client {  provider = "prisma-client-js"}datasource db {  provider = "postgresql"  url      = env("DATABASE_URL")}
```

```js
{  // ...  "scripts": {    // ...    "postinstall": "prisma generate --no-engine"  }  //}
```

---

## Prisma Schema Location and Configuration | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-schema/overview/location

**Contents**:
- Schema location
- Prisma Schema location​
- Multi-file Prisma schema​
  - Usage​
  - Tips for multi-file Prisma Schema​
  - Examples​

The default name for the Prisma Schema is a single file schema.prisma in your prisma folder. When your schema is named like this, the Prisma CLI will detect it automatically.

The Prisma CLI looks for the Prisma Schema in the following locations, in the following order:

The location specified by the --schema flag, which is available when you introspect, generate, migrate, and studio:

The location specified in the package.json file (version 2.7.0 and later):

The Prisma CLI outputs the path of the schema that will be used. The following example shows the terminal output for prisma db pull:

If you prefer splitting your Prisma schema into multiple files, you can have a setup that looks as follows:

Multi-file Prisma schemas are Generally Available since v6.7.0. Before that, they could be used via the prismaSchemaFolder Preview feature flag.

When using a multi-file Prisma schema, you must always explicitly specify the location of the directory that contains the .prisma file with your datasource block.

You can do this in either of three ways:

pass the the --schema option to your Prisma CLI command (e.g. prisma migrate dev --schema ./prisma)

set the prisma.schema field in package.json:

set the schema property in prisma.config.ts:

We recommend using the Prisma Config file to specify the location of your Prisma schema. This is the most flexible way to specify the location of your Prisma schema alongside other configuration options.

All examples above assume that your datasource block is defined in a .prisma file inside the prisma directory.

You also must place the migrations directory next to the .prisma file that defines the datasource block.

For example, assuming schema.prisma defines the datasource, here's how how need to place the migrations folder:

We've found that a few patterns work well with this feature and will help you get the most out of it:

Our fork of dub by dub.co is a great example of a real world project adapted to use a multi-file Prisma Sche

*[Content truncated - see full docs]*

**Examples**:

```terminal
prisma generate --schema=./alternative/schema.prisma
```

```json
"prisma": {  "schema": "db/schema.prisma"}
```

```no-lines
Environment variables loaded from .envPrisma Schema loaded from prisma/schema.prismaIntrospecting based on datasource defined in prisma/schema.prisma …✔ Introspected 4 models and wrote them into prisma/schema.prisma in 239msRun prisma generate to generate Prisma Client.
```

---

## Prisma Studio | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/tools/prisma-studio

**Contents**:
- Prisma Studio
- Models (tables or collections)​
  - Open and close models​
  - Icons of data types in models​
  - Keyboard shortcuts in models​
- Edit data​
  - In-line editing​
  - Batch editing​

Prisma Studio is a visual editor for the data in your database. Note that Prisma Studio is not open source but you can still create issues in the prisma/studio repo.

Run npx prisma studio in your terminal.

When you first open Prisma Studio, you will see a data table layout with a sidebar showing a list of all models defined in your Prisma schema file.

The term model refers to the data model definitions that you add to the Prisma schema file. Depending on the database that you use, a model definition, such as model User, refers to a table in a relational database (PostgreSQL, MySQL, SQL Server, SQLite, CockroachDB) or a collection in MongoDB. For more information, see Defining models.

You can select a model and its data opens in a new tab. In this example, the User model is selected.

To open another model, locate the model in the sidebar and click on it.

To close a model, click the the X button in the model tab. If there are multiple models open, you can also click "Close all" to close all models.

The data type for each field is indicated with an icon in the header.

The table below lists all data types and their identifying icon.

When you open a model, a number of keyboard shortcuts are available to browse and manipulate the data in the model.

Note With Prisma Studio open, you can open the keyboard shortcuts modal by pressing Cmd ⌘+/ on macOS or Ctrl+/ on Windows.

Prisma Studio offers two mechanisms for editing existing data: in-line editing and side panel editing.

To edit data in-line, double-click a cell to enter edit mode. Doing so will place your cursor in the cell and allow you to edit the data. Data can be copied and pasted into cells.

All changes (add, edit, or delete) must be confirmed before they will take effect. Confirm added and edited records with the Save change button. When you select records and click Delete records, confirm the deletion in a dialog box.

You can accumulate multiple added records and edited cells, which you can then final

*[Content truncated - see full docs]*

**Examples**:

```terminal
Error in request:  PrismaClientKnownRequestError: Failed to validate the query Error occurred during query validation & transformation
```

---

## Prisma VS Code extension | Prisma Documentation

**URL**: https://www.prisma.io/docs/postgres/integrations/vscode

**Contents**:
- VS Code
- Overview​
- Database management UI​
  - Workflows​
  - Usage​
- Prisma Studio built-in​
- Prisma MCP server​
- Agent mode​

Visual Studio Code is one of the most popular code editors, offering speed, flexibility, and a vast extension ecosystem. With over 2.5M installs and 350K monthly active users, the Prisma VS Code extension is a powerful tool when you're building applications with Prisma Postgres using VS Code as your editor.

The Prisma VS Code extension includes a dedicated UI to manage Prisma Postgres instances (local and remote).

The UI enables the following workflows:

To manage Prisma Postgres instances via the UI in the Prisma VS Code extension:

Beyond managing your database instances, the Prisma VS Code extension embeds Prisma Studio directly in your editor making it easy to perform create, update, delete steps on your database from right inside of VS Code. Follow these easy steps to get started.

Prisma provides its own Model Context Protocol (MCP) server that lets you manage Prisma Postgres databases, model database schemas and chat through migrations.

You can add the Prisma MCP server to VS Code using the one-click installation by clicking on the following link:

INSTALL PRISMA MCP SERVER

This will prompt you to open VS Code. Once opened, you'll be guided to install the Prisma MCP server directly into your VS Code configuration.

If your browser blocks the link, you can set it up manually by creating a .vscode/mcp.json file in your workspace and adding:

Learn more about the MCP server in our MCP server documentation.

VS Code includes an agent mode (powered by GitHub Copilot) that automatically performs code changes and executes Prisma CLI commands based on your prompts.

The Prisma VS Code extension enables support for VS Code agent mode.

VS Code agent mode can perform the following tasks:

The latest version of the Prisma VS Code extension fully supports agent mode. Since extensions update automatically, no manual action is required to enable it.

We recommend you to use the latest version of Prisma ORM.

To use the agent mode:

Currently, the agent mode uses your d

*[Content truncated - see full docs]*

**Examples**:

```json
{  "servers": {    "Prisma-Local": {      "command": "npx",      "args": ["-y", "prisma", "mcp"]    },    "Prisma-Remote": {      "command": "npx",      "args": ["-y", "mcp-remote", "https://mcp.prisma.io/mcp"]    }  }}
```

---

## Prisma schema | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-schema

**Contents**:
- Prisma schema
- In this section​
- Overview
- Data model
- Introspection
- PostgreSQL extensions

You can introspect your database using the Prisma CLI in order to generate the data model in your Prisma schema. The data model is needed to generate Prisma Client.

This page is about PostgreSQL extensions and explains how to use them with Prisma ORM.

---

## Prototyping your schema | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-migrate/workflows/prototyping-your-schema

**Contents**:
- Prototyping your schema
- Choosing db push or Prisma Migrate​
- Can I use Prisma Migrate and db push together?​
- Prototyping a new schema​
- Prototyping with an existing migration history​

The Prisma CLI has a dedicated command for prototyping schemas: db push

db push uses the same engine as Prisma Migrate to synchronize your Prisma schema with your database schema. The db push command:

Introspects the database to infer and executes the changes required to make your database schema reflect the state of your Prisma schema.

By default, after changes have been applied to the database schema, generators are triggered (for example, Prisma Client). You do not need to manually invoke prisma generate.

If db push anticipates that the changes could result in data loss, it will:

db push works well if:

See Schema prototyping with db push for an example of how to use db push in this way.

db push is not recommended if:

Yes, you can use db push and Prisma Migrate together in your development workflow . For example, you can:

The following scenario demonstrates how to use db push to synchronize a new schema with an empty database, and evolve that schema - including what happens when db push detects that a change will result in data loss.

Create a first draft of your schema:

Use db push to push the initial schema to the database:

Create some example content:

Make an additive change - for example, create a new required field:

db push will fail because you cannot add a required field to a table with existing content unless you provide a default value.

Reset all data in your database and re-apply migrations.

Note: Unlike Prisma Migrate, db push does not generate migrations that you can modify to preserve data, and is therefore best suited for prototyping in a development environment.

Continue to evolve your schema until it reaches a relatively stable state.

Initialize a migration history:

The steps taken to reach the initial prototype are not preserved - db push does not generate a history.

Push your migration history and Prisma schema to source control (e.g. Git).

At this point, the final draft of your prototyping is preserved in a migration and can 

*[Content truncated - see full docs]*

**Examples**:

```prisma
generator client {  provider = "prisma-client-js"}datasource db {  provider = "postgresql"  url      = env("DATABASE_URL")}model User {  id       Int      @id @default(autoincrement())  name     String  jobTitle String  posts    Post[]  profile  Profile?}model Profile {  id       Int    @id @default(autoincrement())  biograpy String // Intentional typo!  userId   Int    @unique  user     User   @relation(fields: [userId], references: [id])}model Post {  id         Int        @id @default(autoinc
...
```

```terminal
npx prisma db push
```

```ts
const add = await prisma.user.create({  data: {    name: 'Eloise',    jobTitle: 'Programmer',    posts: {      create: {        title: 'How to create a MySQL database',        content: 'Some content',      },    },  },})
```

---

## Query optimization with Prisma Postgres | Prisma Documentation

**URL**: https://www.prisma.io/docs/postgres/query-optimization

**Contents**:
- Query optimization for Prisma Postgres
- In this section​
- Setup
- Recordings
- Recommendations
- Prisma AI
- Performance metrics

Understand how Prisma Postgres helps you optimize query performance using the Prisma Optimize toolkit. This section covers setup, recommendations, recording queries, performance metrics, and using Prisma AI for guided improvements.

The recordings feature helps developers debug and isolate sets of queries into distinct sessions, known as recordings. This targeted approach enables precise performance analysis and optimization by preventing the mixing of queries from different applications or test rounds, leading to clearer insights and more effective debugging.

Prisma AI enables you to ask follow-up questions on a provided recommendation for additional clarity.

An Optimize recording session provides detailed insights into the latencies of executed queries, capturing key metrics such as average duration, 50th percentile, 99th percentile, and maximal query execution time.

---

## Relations | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-schema/data-model/relations

**Contents**:
- Relations
- Relations in the database​
  - Relational databases​
  - MongoDB​
    - @db.ObjectId on IDs and relation scalar fields​
- Relations in Prisma Client​
  - Create a record and nested records​
  - Retrieve a record and include related records​

A relation is a connection between two models in the Prisma schema. For example, there is a one-to-many relation between User and Post because one user can have many blog posts.

The following Prisma schema defines a one-to-many relation between the User and Post models. The fields involved in defining the relation are highlighted:

At a Prisma ORM level, the User / Post relation is made up of:

At a Prisma ORM level, a connection between two models is always represented by a relation field on each side of the relation.

The following entity relationship diagram defines the same one-to-many relation between the User and Post tables in a relational database:

In SQL, you use a foreign key to create a relation between two tables. Foreign keys are stored on one side of the relation. Our example is made up of:

In the Prisma schema, the foreign key / primary key relationship is represented by the @relation attribute on the author field:

Note: Relations in the Prisma schema represent relationships that exist between tables in the database. If the relationship does not exist in the database, it does not exist in the Prisma schema.

For MongoDB, Prisma ORM currently uses a normalized data model design, which means that documents reference each other by ID in a similar way to relational databases.

The following document represents a User (in the User collection):

The following list of Post documents (in the Post collection) each have a authorId field which reference the same user:

This data structure represents a one-to-many relation because multiple Post documents refer to the same User document.

If your model's ID is an ObjectId (represented by a String field), you must add @db.ObjectId to the model's ID and the relation scalar field on the other side of the relation:

Prisma Client is generated from the Prisma schema. The following examples demonstrate how relations manifest when you use Prisma Client to get, create, and update records.

The following query creates 

*[Content truncated - see full docs]*

**Examples**:

```prisma
model User {  id    Int    @id @default(autoincrement())  posts Post[]}model Post {  id       Int  @id @default(autoincrement())  author   User @relation(fields: [authorId], references: [id])  authorId Int // relation scalar field  (used in the `@relation` attribute above)  title String}
```

```prisma
model User {  id    String @id @default(auto()) @map("_id") @db.ObjectId  posts Post[]}model Post {  id       String @id @default(auto()) @map("_id") @db.ObjectId  author   User   @relation(fields: [authorId], references: [id])  authorId String @db.ObjectId // relation scalar field  (used in the `@relation` attribute above)  title String}
```

```prisma
author     User        @relation(fields: [authorId], references: [id])
```

---

## Seeding | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-migrate/workflows/seeding

**Contents**:
- Seeding
- How to seed your database in Prisma ORM​
- Integrated seeding with Prisma Migrate​
- Example seed scripts​
  - Seeding your database with TypeScript or JavaScript​
  - Seeding your database via raw SQL queries​
  - Seeding your database via any language (with a Bash script)​
  - User-defined arguments​

This guide describes how to seed your database using Prisma Client and Prisma ORM's integrated seeding functionality. Seeding allows you to consistently re-create the same data in your database and can be used to:

Prisma ORM's integrated seeding functionality expects a command in the "seed" key in the "prisma" key of your package.json file. This can be any command, prisma db seed will just execute it. In this guide and as a default, we recommend writing a seed script inside your project's prisma/ folder and starting it with the command.

With TypeScript,ts-node does transpiling and typechecking by default; typechecking can be disabled with the following flag --transpile-only.

Example: "seed": "ts-node --transpile-only prisma/seed.ts"

This can be useful to reduce memory usage (RAM) and increase execution speed of the seed script.

Database seeding happens in two ways with Prisma ORM: manually with prisma db seed and automatically in prisma migrate reset and (in some scenarios) prisma migrate dev.

With prisma db seed, you decide when to invoke the seed command. It can be useful for a test setup or to prepare a new development environment, for example.

Prisma Migrate also integrates seamlessly with your seeds, assuming you follow the steps in the section below. Seeding is triggered automatically when Prisma Migrate resets the development database.

Prisma Migrate resets the database and triggers seeding in the following scenarios:

When you want to use prisma migrate dev or prisma migrate reset without seeding, you can pass the --skip-seed flag.

Here we suggest some specific seed scripts for different situations. You are free to customize these in any way, but can also use them as presented here:

Create a new file named seed.ts. This can be placed anywhere within your project's folder structure. The example below places it in the /prisma folder.

In the seed.ts file, import Prisma Client, initialize it and create some records. As an example, take the following P

*[Content truncated - see full docs]*

**Examples**:

```json
"prisma": {  "seed": "ts-node prisma/seed.ts"},
```

```json
"prisma": {  "seed": "node prisma/seed.js"},
```

```prisma
model User {  id    Int    @id @default(autoincrement())  email String @unique  name  String  posts Post[]}model Post {  id        Int     @id @default(autoincrement())  title     String  content   String  published Boolean  user      User    @relation(fields: [userId], references: [id])  userId    Int}
```

---

## Should you use Prisma ORM as a Node.js/TypeScript ORM? | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/overview/introduction/should-you-use-prisma

**Contents**:
- Should you use Prisma ORM?
- Prisma ORM likely is a good fit for you if ...​
  - ... you are building a server-side application that talks to a database​
  - ... you care about productivity and developer experience​
  - ... you are working in a team​
  - ... you want a tool that holistically covers your database workflows​
  - ... you value type-safety​
  - ... you want to write raw, type-safe SQL​

Prisma ORM is a new kind of ORM that - like any other tool - comes with its own tradeoffs. This page explains when Prisma ORM would be a good fit, and provides alternatives for other scenarios.

This is the main use case for Prisma ORM. Server-side applications typically are API servers that expose data operations via technologies like REST, GraphQL or gRPC. They are commonly built as microservices or monolithic apps and deployed via long-running servers or serverless functions. Prisma ORM is a great fit for all of these application and deployment models.

Refer to the full list of databases (relational, NoSQL, and NewSQL) that Prisma ORM supports.

Productivity and developer experience are core to how we're building our tools. We're looking to build developer-friendly abstractions for tasks that are complex, error-prone and time-consuming when performed manually.

No matter if you're a SQL newcomer or veteran, Prisma ORM will give you a significant productivity boost for the most common database workflows.

Here are a couple of the guiding principles and general practices we apply when designing and building our tools:

Prisma ORM shines especially when used in collaborative environments.

The declarative Prisma schema provides an overview of the current state of the database that's easy to understand for everyone. This is a major improvement to traditional workflows where developers have to dig through migration files to understand the current table structure.

Prisma Client's minimal API surface enables developers to pick it up quickly without much learning overhead, so onboarding new developers to a team becomes a lot smoother.

The Prisma Migrate workflows are designed in a way to cover database schema changes in collaborative environments. From the initial schema creation up to the point of deploying schema changes to production and resolving conflicts that were introduced by parallel modifications, Prisma Migrate has you covered.

Prisma ORM is a lot more tha

*[Content truncated - see full docs]*

---

## Tags | Prisma Documentation

**URL**: https://www.prisma.io/docs/tags

**Contents**:
- Tags
- A​
- B​
- C​
- D​
- E​
- F​
- G​

---

## Testing with Prisma ORM | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-client/testing

**Contents**:
- Testing
- Unit testing
- Integration testing

This section describes how to approach testing an application that uses Prisma Client.

Unit testing aims to isolate a small portion (unit) of code and test it for logically predictable behaviors. It generally involves mocking objects or server responses to simulate real world behaviors. Some benefits to unit testing include:

Integration tests focus on testing how separate parts of the program work together. In the context of applications using a database, integration tests usually require a database to be available and contain data that is convenient to the scenarios intended to be tested.

---

## Tips to use Cursor with Prisma ORM | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/more/ai-tools/cursor

**Contents**:
- Cursor
- Prisma MCP server​
- Defining project-specific rules with .cursorrules​
- Using Cursor's context-aware capabilities​
  - Add Prisma docs llm.txt file as @Docs context​
  - Adding additional Prisma documentation​
  - Using schema as context​
- Generating Prisma Schema​

Cursor is an AI-powered code editor designed to boost productivity by automating repetitive coding tasks. When paired with Prisma, a robust and type-safe toolkit for database workflows, it becomes a powerful solution for managing and optimizing database schemas, queries, and data seeding.

This guide provides detailed instructions for effectively using Prisma with Cursor to:

While this guide is focused on Cursor, these patterns should work with any AI editor. Let us know on X if you'd like us to create guides for your preferred tool!

Prisma provides its own Model Context Protocol (MCP) server that lets you manage Prisma Postgres databases, model database schemas and chat through migrations. Learn more about how you can add it to Cursor here. You can also add the Prisma MCP server to Cursor using the one-click installation by clicking on the following link:

This will prompt you to open the Cursor app in your browser. Once opened, you'll be guided to install the Prisma MCP server directly into your Cursor configuration.

The .cursorrules file in Cursor allows you to enforce best practices and development standards tailored to your Prisma projects. By defining clear and consistent rules, you can ensure that Cursor generates clean, maintainable, and project-specific code with minimal manual adjustments.

To implement these rules, create a .cursorrules file in the root of your project. Below is an example configuration:

Example .cursorrules file

This file ensures consistent and maintainable code generation, reducing manual intervention while improving project quality.

Cursor's context-aware capabilities let you add specific websites, files, folders or documentation to enhance its understanding of your project. By adding your schema.prisma file as context, you enable Cursor to generate more accurate queries, tests, and seed data based on your database schema.

To improve Cursor's understanding of Prisma-related suggestions in your project, include the /llms.txt mark

*[Content truncated - see full docs]*

**Examples**:

```text
You are a senior TypeScript/JavaScript programmer with expertise in Prisma, clean code principles, and modern backend development.Generate code, corrections, and refactorings that comply with the following guidelines:TypeScript General GuidelinesBasic Principles- Use English for all code and documentation.- Always declare explicit types for variables and functions.  - Avoid using "any".  - Create precise, descriptive types.- Use JSDoc to document public classes and methods.- Maintain a single ex
...
```

```text
"Create a Prisma schema for a SaaS app using PostgreSQL as a provider with `User`, `Organization`, and `Subscription` models, ensuring all models include `createdAt` and `updatedAt` DateTime fields with defaults, a soft-delete `deletedAt` field, and proper relationships between entities."
```

```prisma
generator client {  provider = "prisma-client-js"}datasource db {  provider = "postgresql"  url      = env("DATABASE_URL")}model User {  id            Int           @id @default(autoincrement())  email         String        @unique  name          String  password      String  createdAt     DateTime      @default(now())  updatedAt     DateTime      @updatedAt  deletedAt     DateTime?  organization  Organization  @relation(fields: [organizationId], references: [id])  organizationId Int  role      
...
```

---

## Tips to use Windsurf with Prisma ORM | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/more/ai-tools/windsurf

**Contents**:
- Windsurf
- Prisma MCP server​
  - Add Prisma MCP server via Windsurf Plugins​
- Defining project-specific rules with .windsurfrules​
- Using Windsurf's context-aware capabilities​
  - Including Additional Prisma Resources​
    - Reference the resource in your requests:​
    - Request persistent awareness:​

Windsurf Editor is an AI-powered code editor designed to boost productivity by automating repetitive coding tasks. When paired with Prisma, a robust and type-safe toolkit for database workflows, it becomes a powerful solution for managing and optimizing database schemas, queries, and data seeding.

This guide provides detailed instructions for effectively using Prisma with Windsurf to:

While this guide is focused on Windsurf, these patterns should work with any AI editor. Let us know on X if you'd like us to create guides for your preferred tool!

Prisma provides its own Model Context Protocol (MCP) server that lets you manage Prisma Postgres databases, model database schemas, and even chat through migrations.

You can add the Prisma MCP server via Windsurf MCP Plugin Store.

New MCP plugins can be added from the Plugin Store, which you can access by clicking on the Plugins icon in the top right menu in the Cascade panel, or from the Windsurf Settings > Cascade > Plugins section. Just search for Prisma in the Plugin Store and install the Prisma plugin.

You can also add the Prisma MCP server manually. Learn more about how you can add the MCP server manually to Windsurf here.

The .windsurfrules file in Windsurf allows you to enforce best practices and development standards tailored to your Prisma project. By defining clear and consistent rules, you can ensure that Windsurf generates clean, maintainable, and project-specific code with minimal manual adjustments.

To implement these rules, create a .windsurfrules file in the root of your project. Below is an example configuration:

This file ensures consistent and maintainable code generation, reducing manual intervention while improving project quality.

Windsurf's context-awareness features let you leverage both your project files and external resources to enhance the AI's understanding of your project. By including your Prisma schema and relevant documentation in the context, you enable Windsurf to generate more a

*[Content truncated - see full docs]*

**Examples**:

```text
You are a senior TypeScript/JavaScript programmer with expertise in Prisma, clean code principles, and modern backend development.Generate code, corrections, and refactorings that comply with the following guidelines:TypeScript General GuidelinesBasic Principles- Use English for all code and documentation.- Always declare explicit types for variables and functions.  - Avoid using "any".  - Create precise, descriptive types.- Use JSDoc to document public classes and methods.- Maintain a single ex
...
```

```terminal
Generate a migration script using best practices from prisma.io/docs.
```

```terminal
Always use the Prisma Changelog at prisma.io/changelog for Prisma updates in this project.
```

---

## Tools | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/tools

**Contents**:
- Tools
- In this section​
- Prisma CLI
- Prisma Studio

The Prisma command line interface (CLI) is the primary way to interact with your Prisma project from the command line. It can initialize new project assets, generate Prisma Client, and analyze existing database structures through introspection to automatically create your application models.

Prisma Studio is a visual editor for the data in your database. Note that Prisma Studio is not open source but you can still create issues in the prisma/studio repo.

---

## Troubleshooting: Prisma Accelerate | Prisma Documentation

**URL**: https://www.prisma.io/docs/accelerate/troubleshoot

**Contents**:
- Troubleshooting Prisma Accelerate issues
- P6009 (ResponseSizeLimitExceeded)​
  - Possible causes for P6009​
    - Transmitting images/files in response​
    - Over-fetching of data​
    - Fetching a large volume of data​
- P6004 (QueryTimeout)​
  - Possible causes for P6004​

When working with Prisma Accelerate, you may encounter errors often highlighted by specific error codes during development and operations. It is important to understand the meaning of these errors, why they occur, and how to resolve them in order to ensure the smooth operation of your applications. This guide aims to provide insights and steps to troubleshoot specific error codes encountered with Prisma Accelerate.

This error is triggered when the response size from a database query exceeds the configured query response size limit. We've implemented this restriction to safeguard your application performance, as retrieving data over 5MB can significantly slow down your application due to multiple network layers. Typically, transmitting more than 5MB of data is common when conducting ETL (Extract, Transform, Load) operations. However, for other scenarios such as transactional queries, real-time data fetching for user interfaces, bulk data updates, or aggregating large datasets for analytics outside of ETL contexts, it should generally be avoided. These use cases, while essential, can often be optimized to work within the configured query response size limit, ensuring smoother performance and a better user experience.

This error may arise if images or files stored within your table are being fetched, resulting in a large response size. Storing assets directly in the database is generally discouraged because it significantly impacts database performance and scalability. In addition to performance, it makes database backups slow and significantly increases the cost of storing routine backups.

Suggested solution: Configure the query response size limit to be larger. If the limit is still exceeded, consider storing the image or file in a BLOB store like Cloudflare R2, AWS S3, or Cloudinary. These services allow you to store assets optimally and return a URL for access. Instead of storing the asset directly in the database, store the URL, which will substantially reduce 

*[Content truncated - see full docs]*

**Examples**:

```jsx
export const prisma = new PrismaClient({  datasourceUrl: process.env.DIRECT_DB_CONNECTION,})export const prismaAccelerate = new PrismaClient({  datasourceUrl: process.env.ACCELERATE_CONNECTION,}).$extends(withAccelerate())
```

```text
We were unable to process your request. Please refresh and try again.
```

---

## Troubleshooting | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-migrate/workflows/troubleshooting

**Contents**:
- Troubleshooting
- Handling migration history conflicts​
    - Causes of migration history conflict in a development environment​
    - Fixing a migration history conflict in a development environment​
- Schema drift​
    - Causes of schema drift in a development environment​
    - Fixing schema drift in a development environment​
- Failed migrations​

This guide describes how to resolve issues with Prisma Migrate in a development environment, which often involves resetting your database. For production-focused troubleshooting, see:

This guide does not apply for MongoDB. Instead of migrate dev, db push is used for MongoDB.

A migration history conflict occurs when there are discrepancies between the migrations folder in the file system and the _prisma_migrations table in the database.

In a development environment, switching between feature branches can result in a history conflict because the _prisma_migrations table contains migrations from branch-1, and switching to branch-2 might cause some of those migrations to disappear.

Note: You should never purposefully delete or edit a migration, as this might result in discrepancies between development and production.

If Prisma Migrate detects a migration history conflict when you run prisma migrate dev, the CLI will ask to reset the database and reapply the migration history.

Database schema drift occurs when your database schema is out of sync with your migration history - the database schema has 'drifted away' from the source of truth.

Schema drift can occur if:

Note: The shadow database is required to detect schema drift, and can therefore only be done in a development environment.

If you made manual changes to the database that you do not want to keep, or can easily replicate in the Prisma schema:

Replicate the changes in the Prisma schema and generate a new migration:

If you made manual changes to the database that you want to keep, you can:

Introspect the database:

Prisma will update your schema with the changes made directly in the database.

Generate a new migration to include the introspected changes in your migration history:

Prisma Migrate will prompt you to reset, then applies all existing migrations and a new migration based on the introspected changes. Your database and migration history are now in sync, including your manual changes.

A migr

*[Content truncated - see full docs]*

**Examples**:

```terminal
npx prisma migrate reset
```

```terminal
npx prisma migrate dev
```

```terminal
npx prisma db pull
```

---

## Type safety | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-client/type-safety

**Contents**:
- Type safety
- Importing generated types​
- What are generated types?​
  - Generated UncheckedInput types​
- Type utilities​

The generated code for Prisma Client contains several helpful types and utilities that you can use to make your application more type-safe. This page describes patterns for leveraging them.

Note: If you're interested in advanced type safety topics with Prisma ORM, be sure to check out this blog post about improving your Prisma Client workflows with the new TypeScript satisfies keyword.

You can import the Prisma namespace and use dot notation to access types and utilities. The following example shows how to import the Prisma namespace and use it to access and use the Prisma.UserSelect generated type:

See also: Using the Prisma.UserCreateInput generated type

Generated types are TypeScript types that are derived from your models. You can use them to create typed objects that you pass into top-level methods like prisma.user.create(...) or prisma.user.update(...), or options such as select or include.

For example, select accepts an object of type UserSelect. Its object properties match those that are supported by select statements according to the model.

The first tab below shows the UserSelect generated type and how each property on the object has a type annotation. The second tab shows the original schema from which the type was generated.

In TypeScript the concept of type annotations is when you declare a variable and add a type annotation to describe the type of the variable. See the below example.

Both of these variable declarations have been given a type annotation to specify what primitive type they are, number and string respectively. Most of the time this kind of annotation is not needed as TypeScript will infer the type of the variable based on how its initialized. In the above example myAge was initialized with a number so TypeScript guesses that it should be typed as a number.

Going back to the UserSelect type, if you were to use dot notation on the created object userEmail, you would have access to all of the fields on the User model that can be int

*[Content truncated - see full docs]*

**Examples**:

```ts
import { Prisma } from '@prisma/client'// Build 'select' objectconst userEmail: Prisma.UserSelect = {  email: true,}// Use select objectconst createUser = await prisma.user.create({  data: {    email: 'bob@prisma.io',  },  select: userEmail,})
```

```ts
type Prisma.UserSelect = {    id?: boolean | undefined;    email?: boolean | undefined;    name?: boolean | undefined;    posts?: boolean | Prisma.PostFindManyArgs | undefined;    profile?: boolean | Prisma.ProfileArgs | undefined;}
```

```prisma
model User {  id      Int      @id @default(autoincrement())  email   String   @unique  name    String?  posts   Post[]  profile Profile?}
```

---

## Understanding Prisma Migrate | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate

**Contents**:
- Understanding Prisma Migrate
- In this section​
- Overview
- Mental model
- About migration histories
- About the shadow database
- Limitations and known issues

Does not apply for MongoDBInstead of migrate dev and related commands, use db push for MongoDB.

This guide provides a conceptual overview of database migrations using Prisma Migrate when working with relational databases. It covers: what database migrations are, their value, and what Prisma Migrate is and how you can evolve your database schema with Prisma Migrate in different environments.

This page explains how Prisma ORM uses migration histories to track changes to your schema.

The shadow database is a second, temporary database that is created and deleted automatically\ each time you run prisma migrate dev and is primarily used to detect problems* such as schema drift or potential data loss of the generated migration.

The following limitations apply to Prisma Migrate.

---

## Use Prisma Postgres in Firebase Studio | Prisma Documentation

**URL**: https://www.prisma.io/docs/postgres/integrations/idx

**Contents**:
- Firebase Studio

If you want to explore Prisma Postgres without leaving your browser, you can try it out the via Google's Firebase Studio, a fully-fledged online IDE:

---

## Using the Prisma MCP Server with ChatGPT | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/more/ai-tools/chatgpt

**Contents**:
- ChatGPT
- Features of the Prisma MCP server​
- Prerequisites​
- Enable Developer mode in ChatGPT​
- Add the remote Prisma MCP server​
- Using the remote Prisma MCP server​

ChatGPT is a large language model-based chatbot developed by OpenAI. You can extend its capabilities by connecting it to external tools, such as the Prisma MCP server, to interact with your Prisma Postgres databases.

This guide explains how to add the remote Prisma MCP server to ChatGPT, allowing you to create and manage your databases using natural language prompts.

This feature is still in development by OpenAI and might look or work a little differently over time. Some users may not have access to it yet.

If you notice that something has changed or doesn't match this guide, please open an issue or submit a pull request to update our docs.

Here is an end to end demo of setting up the remote Prisma MCP server and using it in ChatGPT:

By connecting the Prisma MCP server to ChatGPT, you can perform a variety of database management tasks directly from the chat interface. Here are some of the key features available:

To use the Prisma MCP server with ChatGPT, you need access to ChatGPT's Developer Mode. This feature is available on specific ChatGPT plans. For the most up-to-date information on supported plans, please refer to the official OpenAI documentation.

You will be redirected to authenticate with your Prisma Data Platform account and choose your desired workspace. After successful authentication, you will be redirected back to ChatGPT.

Once Developer Mode is enabled and the Prisma MCP server is added, you can use it in your chats.

Now you can use natural language prompts to manage your database. For example:

**Examples**:

```text
Create a DB called pet-app for me near Paris
```

---

## Viewing data | Prisma Documentation

**URL**: https://www.prisma.io/docs/postgres/integrations/viewing-data

**Contents**:
- Viewing data
- Viewing and editing data in Prisma Studio​
- Connecting to Prisma Postgres instance with 3rd party database editors​
  - 1. Create a TCP tunnel to access Prisma Postgres directly​
  - 2a. Connect to Prisma Postgres using TablePlus​
  - 2b. Connect to Prisma Postgres using DataGrip​
  - 2c. Connect to Prisma Postgres using DBeaver​
  - 2d. Connect to Prisma Postgres using Postico​

You can view and edit your data in Prisma Postgres using either Prisma Studio or 3rd party database editors.

With Prisma Postgres, a hosted version of Prisma Studio is available for you in of your project. In your project environment in the , select the Studio tab in the left-hand navigation to view and edit your data:

You can also run Prisma Studio locally by running:

This should start a live server in http://localhost:5555 where you can visit and interact with your database.

You can connect to your Prisma Postgres instance using third party database editors like pgAdmin, TablePlus, Postico etc using @prisma/ppg-tunnel package. See the example below to connect using TablePlus.

If you already have a .env file in your current directory with DATABASE_URL set, the tunnel CLI will automatically pick it up, no need to manually export it. However, if you haven't set up a .env file, you'll need to set the DATABASE_URL environment variable explicitly.

In your terminal, to set the environment variable DATABASE_URL referring to your Prisma Postgres instance which you want to connect to (be sure to replace the API_KEY placeholder with the API key value of your Prisma Postgres instance):

If you explicitly set DATABASE_URL in your terminal, that value will take precedence over the one in your .env file.

Run the following command to connect to your Prisma Postgres instance via @prisma/ppg-tunnel package:

Copy the port from the output above, you will need it in the next step.

Keep this tunnel process running while you are using the database editor to maintain the connection.

Based on the database editor you are using, you can connect to your Prisma Postgres instance using the details you obtained from the output of the @prisma/ppg-tunnel package. To add the connection string in TablePlus:

Based on the database editor you are using, you can connect to your Prisma Postgres instance using the details you obtained from the output of the @prisma/ppg-tunnel package. To add t

*[Content truncated - see full docs]*

**Examples**:

```terminal
npx prisma studio
```

```terminal
export DATABASE_URL="prisma+postgres://accelerate.prisma-data.net/?api_key=API_KEY"
```

```terminal
export DATABASE_URL="prisma+postgres://accelerate.prisma-data.net/?api_key=API_KEY"
```

---

## What is Prisma ORM? (Overview) | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/overview/introduction/what-is-prisma

**Contents**:
- What is Prisma ORM?
- How does Prisma ORM work?​
  - The Prisma schema​
  - The Prisma schema data model​
    - Functions of Prisma schema data models​
    - Getting a data model​
  - Accessing your database with Prisma Client​
    - Generating Prisma Client​

Prisma ORM is an open-source next-generation ORM. It consists of the following parts:

Prisma Client: Auto-generated and type-safe query builder for Node.js & TypeScript

Prisma Migrate: Migration system

Prisma Studio: GUI to view and edit data in your database.

Prisma Studio is the only part of Prisma ORM that is not open source. You can only run Prisma Studio locally.

Prisma Client can be used in any Node.js (supported versions) or TypeScript backend application (including serverless applications and microservices). This can be a REST API, a GraphQL API, a gRPC API, or anything else that needs a database.

Every project that uses a tool from the Prisma ORM toolkit starts with a Prisma schema. The Prisma schema allows developers to define their application models in an intuitive data modeling language. It also contains the connection to a database and defines a generator:

Note: The Prisma schema has powerful data modeling features. For example, it allows you to define "Prisma-level" relation fields which will make it easier to work with relations in the Prisma Client API. In the case above, the posts field on User is defined only on "Prisma-level", meaning it does not manifest as a foreign key in the underlying database.

In this schema, you configure three things:

On this page, the focus is on the data model. You can learn more about Data sources and Generators on the respective docs pages.

The data model is a collection of models. A model has two major functions:

There are two major workflows for "getting" a data model into your Prisma schema:

Once the data model is defined, you can generate Prisma Client which will expose CRUD and more queries for the defined models. If you're using TypeScript, you'll get full type-safety for all queries (even when only retrieving the subsets of a model's fields).

The first step when using Prisma Client is installing the @prisma/client and prisma npm packages:

Then, you can run prisma generate:

The prisma generate com

*[Content truncated - see full docs]*

**Examples**:

```prisma
datasource db {  provider = "postgresql"  url      = env("DATABASE_URL")}generator client {  provider = "prisma-client-js"}model Post {  id        Int     @id @default(autoincrement())  title     String  content   String?  published Boolean @default(false)  author    User?   @relation(fields: [authorId], references: [id])  authorId  Int?}model User {  id    Int     @id @default(autoincrement())  email String  @unique  name  String?  posts Post[]}
```

```prisma
datasource db {  provider = "mongodb"  url      = env("DATABASE_URL")}generator client {  provider = "prisma-client-js"}model Post {  id        String  @id @default(auto()) @map("_id") @db.ObjectId  title     String  content   String?  published Boolean @default(false)  author    User?   @relation(fields: [authorId], references: [id])  authorId  String  @db.ObjectId}model User {  id    String  @id @default(auto()) @map("_id") @db.ObjectId  email String  @unique  name  String?  posts Post[]}
```

```terminal
npm install prisma --save-devnpm install @prisma/client
```

---

## Why Prisma ORM? Comparison with SQL query builders & ORMs | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/overview/introduction/why-prisma

**Contents**:
- Why Prisma ORM?
- TLDR​
- Problems with SQL, traditional ORMs and other database tools​
  - Raw SQL: Full control, low productivity​
  - SQL query builders: High control, medium productivity​
  - Traditional ORMs: Less control, better productivity​
- Application developers should care about data – not SQL​
- Prisma ORM makes developers productive​

On this page, you'll learn about the motivation for Prisma ORM and how it compares to other database tools like traditional ORMs and SQL query builders.

Working with relational databases is a major bottleneck in application development. Debugging SQL queries or complex ORM objects often consume hours of development time.

Prisma ORM makes it easy for developers to reason about their database queries by providing a clean and type-safe API for submitting database queries which returns plain old JavaScript objects.

Prisma ORM's main goal is to make application developers more productive when working with databases. Here are a few examples of how Prisma ORM achieves this:

The remaining parts of this page discuss how Prisma ORM compares to existing database tools.

The main problem with the database tools that currently exist in the Node.js and TypeScript ecosystem is that they require a major tradeoff between productivity and control.

With raw SQL (e.g. using the native pg or mysql Node.js database drivers) you have full control over your database operations. However, productivity suffers as sending plain SQL strings to the database is cumbersome and comes with a lot of overhead (manual connection handling, repetitive boilerplate, ...).

Another major issue with this approach is that you don't get any type safety for your query results. Of course, you can type the results manually but this is a huge amount of work and requires major refactorings each time you change your database schema or queries to keep the typings in sync.

Furthermore, submitting SQL queries as plain strings means you don't get any autocompletion in your editors.

A common solution that retains a high level of control and provides better productivity is to use a SQL query builder (e.g. knex.js). These sort of tools provide a programmatic abstraction to construct SQL queries.

The biggest drawback with SQL query builders is that application developers still need to think about their data in terms

*[Content truncated - see full docs]*

---

## Write Your Own SQL in Prisma Client | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-client/using-raw-sql

**Contents**:
- Write your own SQL
- Writing type-safe queries with Prisma Client and TypedSQL​
  - What is TypedSQL?​
- Raw queries​
  - Alternative approaches to raw SQL queries in relational databases​
  - Alternative approaches to raw queries in document databases​

While the Prisma Client API aims to make all your database queries intuitive, type-safe, and convenient, there may still be situations where raw SQL is the best tool for the job.

This can happen for various reasons, such as the need to optimize the performance of a specific query or because your data requirements can't be fully expressed by Prisma Client's query API.

In most cases, TypedSQL allows you to express your query in SQL while still benefiting from Prisma Client's excellent user experience. However, since TypedSQL is statically typed, it may not handle certain scenarios, such as dynamically generated WHERE clauses. In these cases, you will need to use $queryRaw or $executeRaw, or their unsafe counterparts.

TypedSQL is available in Prisma ORM 5.19.0 and later. For raw database access in previous versions, see our raw queries documentation.

TypedSQL is a new feature of Prisma ORM that allows you to write your queries in .sql files while still enjoying the great developer experience of Prisma Client. You can write the code you're comfortable with and benefit from fully-typed inputs and outputs.

With TypedSQL, you can:

TypedSQL is particularly useful for:

By using TypedSQL, you can write efficient, type-safe database queries without sacrificing the power and flexibility of raw SQL. This feature allows you to seamlessly integrate custom SQL queries into your Prisma-powered applications, ensuring type safety and improving developer productivity.

For a detailed guide on how to get started with TypedSQL, including setup instructions and usage examples, please refer to our TypedSQL documentation.

Prior to version 5.19.0, Prisma Client only supported raw SQL queries that were not type-safe and required manual mapping of the query result to the desired type.

While not as ergonomic as TypedSQL, these queries are still supported and are useful when TypedSQL queries are not possible either due to features not yet supported in TypedSQL or when the query is dynam

*[Content truncated - see full docs]*

---
