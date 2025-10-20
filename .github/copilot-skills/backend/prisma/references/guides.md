# Prisma - Guides

**Pages**: 46

---

## 2 docs tagged with "database" | Prisma Documentation

**URL**: https://www.prisma.io/docs/tags/database

**Contents**:
- 2 docs tagged with "database"
- Guides
- Migrate data using the expand and contract pattern

Welcome to the Guides section! Here you'll find practical, step-by-step guides to help you accomplish specific tasks with Prisma products, including Prisma ORM, Prisma Accelerate, Prisma Postgres, and more.

Learn how to perform data migrations using the expand and contract pattern with Prisma ORM

---

## About the shadow database | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/shadow-database

**Contents**:
- About the shadow database
- How the shadow database works​
  - Detecting schema drift​
  - Generating new migrations​
- Manually configuring the shadow database​
- Cloud-hosted shadow databases must be created manually​
- Shadow database user permissions​

The shadow database is a second, temporary database that is created and deleted automatically* each time you run prisma migrate dev and is primarily used to detect problems such as schema drift or potential data loss of the generated migration.

migrate diff command also requires a shadow database when diffing against a local migrations directory with --from-migrations or --to-migrations.

The shadow database is not required in production, and is not used by production-focused commands such as prisma migrate resolve and prisma migrate deploy.

A shadow database is never used for MongoDB as migrate dev is not used there.

When you run prisma migrate dev to create a new migration, Prisma Migrate uses the shadow database to:

To detect drift in development, Prisma Migrate:

If Prisma Migrate does not detect schema drift, it moves on to generating new migrations.

Note: The shadow database is not responsible for checking if a migration file has been edited or deleted. This is done using the checksum field in the _prisma_migrations table.

If Prisma Migrate detects schema drift, it outputs detailed information about which parts of the database have drifted. The following example output could be shown when the development database has been modified manually: The Color enum is missing the expected variant RED and includes the unexpected variant TRANSPARENT:

Assuming Prisma Migrate did not detect schema drift, it moves on to generating new migrations from Prisma schema changes. To generate new migrations, Prisma Migrate:

In some cases it might make sense (e.g. when creating and dropping databases is not allowed on cloud-hosted databases) to manually define the connection string and name of the database that should be used as the shadow database for migrate dev. In such a case you can:

Important: Do not use the exact same values for url and shadowDatabaseUrl as that might delete all the data in your database.

Some cloud providers do not allow you to drop and create datab

*[Content truncated - see full docs]*

**Examples**:

```text
[*] Changed the `Color` enum  [+] Added variant `TRANSPARENT`  [-] Removed variant `RED`
```

```prisma
datasource db {  provider          = "postgresql"  url               = env("DATABASE_URL")  shadowDatabaseUrl = env("SHADOW_DATABASE_URL")}
```

```prisma
datasource db {  provider          = "postgresql"  url               = env("DATABASE_URL")  shadowDatabaseUrl = env("SHADOW_DATABASE_URL")}
```

---

## Build a Nuxt app with Prisma ORM and Prisma Postgres | Prisma Documentation

**URL**: https://www.prisma.io/docs/guides/nuxt

**Contents**:
- How to use Prisma ORM with Nuxt
- Prerequisites​
- 1. Create a New Nuxt Project and set up the Prisma Nuxt module​
- 2. Setup Prisma ORM by running the development server locally​
- 4. Update the application code​
- 5. Create a Prisma Postgres instance​
- 6. Set up Prisma Postgres in your Nuxt app​
- 7. Deploy to Vercel​

This guide explains how to set up a Nuxt application, configure Prisma Postgres using the Prisma Nuxt module, and deploy the project to Vercel for production.

Here's what you'll learn:

To follow this guide, ensure you have the following:

Initialize a new Nuxt project, select npm as the package manager and initialize git:

We recommend using npm as it is the most stable option with the @prisma/nuxt module.

Navigate into the project directory and install the @prisma/nuxt module:

Install the Prisma Accelerate client extension as it's required to use Prisma Postgres:

Add the @prisma/nuxt module with the following configuration to your nuxt.config.ts file:

After configuring your Nuxt project with the Prisma module, the next step is to set up Prisma ORM. This process begins by starting the development server, which automatically configures Prisma with a SQLite database.

Run the following command to start the development server:

After running this command, you will be prompted to run a database migration with Prisma Migrate:

Confirm that you want to migrate your database and create your initial tables by hitting Y on your keyboard.

Once the setup flow has terminated, it:

The database migrates automatically the first time you start the module if there isn't a migrations folder. After that, you need to run npx prisma migrate dev manually in the CLI to apply any schema changes. Running the npx prisma migrate dev command manually makes it easier and safer to manage migrations and also to troubleshoot any migration-related errors.

When the Prisma setup is complete, the development server should start on https://localhost:3000.

Next, stop the server, as we need to make some code changes.

With Prisma configured, the next step is to update your application code to fetch and display data from your database.

In the root directory of your project, create a folder named components.

Inside the components folder, create a file named User.server.vue. This server componen

*[Content truncated - see full docs]*

**Examples**:

```terminal
npm create nuxt hello-world
```

```terminal
cd hello-worldnpm i @prisma/nuxt
```

```terminal
npm i @prisma/extension-accelerate
```

---

## Caching queries in Prisma Postgres | Prisma Documentation

**URL**: https://www.prisma.io/docs/postgres/database/caching

**Contents**:
- Caching queries in Prisma Postgres
- Cache strategies​
- Time-to-live (TTL)​
  - Invalidate the TTL and keep your cached query results up-to-date​
- Stale-While-Revalidate (SWR)​
  - Invalidate the SWR and keep your cached query results up-to-date​
- Selecting a cache strategy​
  - Cache strategy using TTL​

Prisma Postgres supports built-in query caching to reduce database load and improve query performance. You can configure cache behavior using the cacheStrategy option available in all read queries.

This feature is powered by an internal caching layer enabled through Prisma Accelerate, but you do not need to interact with Accelerate directly unless you're using your own database.

For all read queries in Prisma Client, you can define the cacheStrategy parameter that configures cache behavior. The cache strategy allows you to define two main characteristics of the cache:

Time-to-Live (TTL) determines how long cached data is considered fresh. By specifying the ttl in seconds, you can control the duration for which data in the cache remains valid. When a read query is executed, if the cached response is within the ttl limit, Prisma Client retrieves the data from the cache without querying the database. If the cached data is not available or has expired, Prisma Client queries the database and stores the results in the cache for future requests.

Use ttl in cacheStrategy and specify the TTL of the query in seconds:

With a specified TTL of 60 seconds, the majority of requests will result in a cache hit throughout the TTL duration:

TTL is useful for reducing database load and latency for data that does not require frequent updates.

If your application requires real-time or near-real-time data, cache invalidation ensures that users see the most current data, even when using a large ttl (Time-To-Live). By invalidating your cache, you can bypass extended caching periods to show live data whenever it's needed.

For example, if a dashboard displays customer information and a customer’s contact details change, TTL (Time-To-Live) settings ensure the cache automatically expires after a set duration. This allows the system to refresh only the updated data at the next access, ensuring support staff always see the latest information without manually refreshing the cache.

However

*[Content truncated - see full docs]*

**Examples**:

```javascript
await prisma.user.findMany({  cacheStrategy: {    ttl: 60,  },});
```

```ts
await prisma.user.findMany({    cacheStrategy: {      ttl: 60,      tags: ["findMany_users"],    },});// This is how you would invalidate the cached query above.await prisma.$accelerate.invalidate({    tags: ["findMany_users"],});
```

```javascript
await prisma.user.findMany({  cacheStrategy: {    swr: 60,  },});
```

---

## Connection pooling in Prisma Postgres | Prisma Documentation

**URL**: https://www.prisma.io/docs/postgres/database/connection-pooling

**Contents**:
- Connection pooling
  - Connection pooling in Prisma Postgres​
  - Configuring the connection pool size​
  - Configuring the connection pool timeout​
- Configuring query limits​
  - Query timeout limit​
  - Interactive transactions query timeout limit​
  - Response size limit​

Prisma Postgres provides built-in connection pooling by default, enabled by Prisma Accelerate. By using Prisma Postgres, you get the benefits of connection pooling without having to configure anything. The efficient management of database connections allows the database to process more queries without exhausting the available database connections, making your application more scalable.

In some cases, however, it may be beneficial to further configure connection pooling in order to optimize the performance of your application.

This document focuses on the connection pooling features of Prisma Postgres. For more information about the internal connection pool of Prisma ORM specifically, see our ORM connection pooling documentation.

Currently, Prisma Postgres allows a maximum of 10 concurrent database connections per Prisma Schema. This limit is typically sufficient due to Prisma Postgres's efficient unikernel-based architecture, which minimizes the need for large connection pools.

If you're using your own database with Prisma Accelerate, the connection limits differ:

You can compare plans on the Prisma pricing page.

If you're not using Prisma Postgres, you can configure the connection pool size for Prisma ORM by specifying it in the connection string.

For Prisma Postgres, the connection limit is currently fixed at 10 and cannot be changed.

If you're using Prisma Accelerate with your own database, you can configure the connection pool size through the Connection limit setting in your project on the Accelerate setup page.

The connection pool timeout is the maximum number of seconds that a query will block while waiting for a connection from Prisma Postgres's internal connection pool. This occurs if the number of concurrent requests exceeds the connection limit, resulting in queueing of additional requests until a free connection becomes available. An exception is thrown if a free connection does not become available within the pool timeout. The connection pool t

*[Content truncated - see full docs]*

**Examples**:

```env
postgresql://user:password@localhost:5432/db?connection_limit=10&pool_timeout=20
```

```ts
await prisma.$transaction(  async (tx) => {    // Your queries go here  },  {    timeout: 30000, // 30s  });
```

---

## Database drivers | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/overview/databases/database-drivers

**Contents**:
- Database drivers
- Default built-in drivers​
- Driver adapters​
  - Database driver adapters​
  - Serverless driver adapters​
  - Community-maintained database driver adapters​
- How to use driver adapters​
- Notes about using driver adapters​

One of Prisma Client's components is the Query Engine (which is implemented in Rust). The Query Engine is responsible for transforming Prisma Client queries into SQL statements. It connects to your database via TCP using built-in drivers that don't require additional setup.

As of v6.15.0, Prisma ORM can be used without Rust engines in production applications. Learn more here.

When enabled, your Prisma Client will be generated without a Rust-based query engine binary:

Note that driver adapters are required if you want to use Prisma ORM without Rust engines.

You can read about the performance and DX improvements of this change on our blog.

Prisma Client can connect and run queries against your database using JavaScript database drivers using driver adapters. Adapters act as translators between Prisma Client and the JavaScript database driver.

Prisma Client will use the Query Engine to transform the Prisma Client query to SQL and run the generated SQL queries via the JavaScript database driver.

There are two different types of driver adapters:

Note: Driver adapters enable edge deployments of applications that use Prisma ORM.

You can connect to your database using a Node.js-based driver from Prisma Client using a database driver adapter. Prisma maintains the adapters for the following drivers:

Database providers, such as Neon and PlanetScale, allow you to connect to your database using other protocols besides TCP, such as HTTP and WebSockets. These database drivers are optimized for connecting to your database in serverless and edge environments.

Prisma ORM maintains the following serverless driver adapters:

You can also build your own driver adapter for the database you're using. The following is a list of community-maintained driver adapters:

Refer to the following pages to learn more about how to use the specific driver adapters with the specific database providers:

In v6.6.0, we introduced a simplified version for instantiating Prisma Client when using

*[Content truncated - see full docs]*

**Examples**:

```prisma
generator client {  provider   = "prisma-client-js" // or "prisma-client"  output     = "../src/generated/prisma"  engineType = "client"           // no Rust engine}
```

```typescript
import { createClient } from '@libsql/client'import { PrismaLibSQL } from '@prisma/adapter-libsql'import { PrismaClient } from '@prisma/client'// Old way of using driver adapters (before 6.6.0)const driver = createClient({  url: env.LIBSQL_DATABASE_URL,  authToken: env.LIBSQL_DATABASE_TOKEN,})const adapter = new PrismaLibSQL(driver)const prisma = new PrismaClient({ adapter })
```

```typescript
import { PrismaLibSQL } from '@prisma/adapter-libsql'import { PrismaClient } from '../prisma/prisma-client'const adapter = new PrismaLibSQL({  url: env.LIBSQL_DATABASE_URL,  authToken: env.LIBSQL_DATABASE_TOKEN,})const prisma = new PrismaClient({ adapter })
```

---

## Database features matrix | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/reference/database-features

**Contents**:
- Database features matrix
- Relational database features​
  - Constraints​
  - Referential Actions (Delete and Update behaviors for foreign key references)​
  - Indexes​
  - Misc​
- NoSQL database features​
  - MongoDB​

This page gives an overview of the features which are provided by the databases that Prisma ORM supports. Additionally, it explains how each of these features can be used in Prisma ORM with pointers to further documentation.

This section describes which database features exist on the relational databases that are currently supported by Prisma ORM. The Prisma schema column indicates how a certain feature can be represented in the Prisma schema and links to its documentation. Note that database features can be used in Prisma Client even though they might not yet be representable in the Prisma schema.

These features are only for relational databases. Supported features for NoSQL databases, like MongoDB, can be found below.

* Caveats apply when using the UNIQUE constraint with Microsoft SQL Server † Only supported in MySQL in version 8 and higher. ‡ Only supported in PostgreSQL.

* RESTRICT is not supported in Microsoft SQL Server.

Algorithm specified via USING:

This section describes which database features exist on the NoSQL databases that are currently supported by Prisma ORM.

The following table lists common MongoDB features and describes the level of support offered by Prisma ORM:

---

## Databases | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/overview/databases

**Contents**:
- Databases
- In this section​
- Database drivers
- PostgreSQL
- MySQL/MariaDB
- SQLite
- MongoDB
- Microsoft SQL Server

Learn about the different databases Prisma ORM supports.

Default built-in drivers

The PostgreSQL data source connector connects Prisma ORM to a PostgreSQL database server.

The MySQL data source connector connects Prisma ORM to a MySQL or MariaDB database server.

The SQLite data source connector connects Prisma ORM to a SQLite database file. These files always have the file ending .db (e.g.: dev.db).

This guide discusses the concepts behind using Prisma ORM and MongoDB, explains the commonalities and differences between MongoDB and other database providers, and leads you through the process for configuring your application to integrate with MongoDB using Prisma ORM.

This guide discusses the concepts behind using Prisma ORM and CockroachDB, explains the commonalities and differences between CockroachDB and other database providers, and leads you through the process for configuring your application to integrate with CockroachDB.

Prisma and PlanetScale together provide a development arena that optimizes rapid, type-safe development of data access applications, using Prisma's ORM and PlanetScale's highly scalable MySQL-based platform.

This guide discusses the concepts behind using Prisma ORM and Supabase, explains the commonalities and differences between Supabase and other database providers, and leads you through the process for configuring your application to integrate with Supabase.

This guide explains how to:

This guide discusses the concepts behind using Prisma ORM and Turso, explains the commonalities and differences between Turso and other database providers, and leads you through the process for configuring your application to integrate with Turso.

This page discusses the concepts behind using Prisma ORM and Cloudflare D1, explains the commonalities and differences between Cloudflare D1 and other database providers, and leads you through the process for configuring your application to integrate with Cloudflare D1.

---

## Databases supported by Prisma ORM | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/reference/supported-databases

**Contents**:
- Supported databases
- Self-hosted databases​
- Managed databases​

Prisma ORM currently supports the following databases.

See also: System requirements.

An asterisk (*) indicates that the version number is not relevant; either all versions are supported, there is not a public version number, etc.

Note that a fixed version of SQLite is shipped with every Prisma ORM release.

---

## Direct connections (TCP) | Prisma Documentation

**URL**: https://www.prisma.io/docs/postgres/database/direct-connections

**Contents**:
- Direct connections
- Overview​
- How to connect to Prisma Postgres via direct TCP​
- Connection string​
  - Format​
  - SSL mode​
- Billing​
- Temporary limitations​

Prisma Postgres is the perfect choice for your applications, whether you connect to it via Prisma ORM or any other ORM, database library / tool of your choice. If you use it with Prisma ORM, Prisma Postgres comes with built-in connection pooling and an integrated caching layer (powered by Prisma Accelerate).

If you connect to it via another tool, you can do so with a direct connection string following the conventional PostgreSQL format.

In order to get a direct connection string, you need to:

When you connect to Prisma Postgres via direct TCP, your connection string looks as follows:

The USER and PASSWORD values are provided when you generate credentials for your Prisma Postgres instance in the . Here is an example with sample values:

SSL mode is required when connecting to Prisma Postgres via direct TCP, so you need to append sslmode=require to your TCP connection string.

When using direct TCP to connect to a Prisma Postgres instance, every SQL query is counted as a billable operation. Learn more on our pricing page.

Prisma Postgres closes idle connections after an extended period of time. If that happens in your application, you can re-open a new connection. (Most database clients re-connect automatically.)

While direct connections are in Early Access, the following connection limits apply:

While direct connections are in Early Access, the following timeouts apply:

User permissions are limited to read, write and schema changes. It is not possible to create separate databases, manage users and roles, or perform other administrative actions.

Prisma Postgres can be accessed securely via a TCP tunnel using the @prisma/ppg-tunnel package, an authentication proxy designed for local database workflows. This package establishes a secure connection to Prisma Postgres through a local TCP server, enabling secure access while automatically handling traffic routing and authentication.

This is a Early Access feature of Prisma Postgres. It is not recommended for prod

*[Content truncated - see full docs]*

**Examples**:

```bash
DATABASE_URL="postgres://USER:PASSWORD@db.prisma.io:5432/?sslmode=require"
```

```bash
DATABASE_URL="postgres://2f9881cc7eef46f094ac913df34c1fb441502fe66cbe28cc48998d4e6b20336b:sk_QZ3u8fMPFfBzOID4ol-mV@db.prisma.io:5432/?sslmode=require"
```

```terminal
export DATABASE_URL="prisma+postgres://accelerate.prisma-data.net/?api_key=API_KEY"
```

---

## How to embed Prisma Studio in a Next.js app with Prisma Postgres | Prisma Documentation

**URL**: https://www.prisma.io/docs/guides/embed-studio-nextjs

**Contents**:
- How to embed Prisma Studio in a Next.js app
- Prerequisites​
- 1. Setting up Next.js​
- 2. Setting up Prisma ORM and Prisma Postgres​
  - 2.1. Install Prisma dependencies​
  - 2.2. Initialize Prisma with Prisma Postgres​
  - 2.3. Define your database schema​
  - 2.4. Apply the schema to your database​

Prisma Studio can be embedded directly into your Next.js application using the @prisma/studio-core package. This guide walks you through the setup so you can manage your database from within your app instead of running Prisma Studio separately.

After completing the guide, you'll have a Next.js app with Prisma Studio embedded, allowing you to browse and edit your database directly from your application interface:

Embedding Prisma Studio can be useful in scenarios such as:

Embeddable Prisma Studio is free and licensed under Apache 2.0.

✔️ Free to use in production ⚠️ Prisma branding must remain visible and unchanged 🔐 To remove branding or learn about upcoming partner-only features, reach out at partnerships@prisma.io

Currently, Embedded Prisma Studio supports Prisma Postgres, with additional databases coming soon.

First, create a new Next.js project from the directory where you want to build your app:

You will be prompted to answer a few questions about your project. Select all of the defaults.

For reference, those are:

Then, navigate to the project directory:

Install the required Prisma packages:

Initialize Prisma in your project and create a Prisma Postgres database:

You'll need to answer a few questions while setting up your Prisma Postgres database. Select the region closest to your location and a memorable name for your database like "My __________ Project"

The prisma init --db command creates:

Open prisma/schema.prisma and replace the content with:

Generate the Prisma Client and apply the schema:

This creates the tables in your Prisma Postgres database and generates the Prisma Client.

Create a seed file to add some sample data. Create a seed.ts file in the prisma folder and add the following code:

Add a seed script to your package.json:

Now that you have Prisma ORM and Prisma Postgres set up, you can embed Prisma Studio in your Next.js app.

Install the @prisma/studio-core package that provides the embeddable components:

If you encounter a d

*[Content truncated - see full docs]*

**Examples**:

```terminal
npx create-next-app@latest nextjs-studio-embed
```

```terminal
cd nextjs-studio-embed
```

```terminal
npm install prisma tsx --save-devnpm install @prisma/extension-accelerate @prisma/client
```

---

## How to migrate from Drizzle to Prisma ORM | Prisma Documentation

**URL**: https://www.prisma.io/docs/guides/migrate-from-drizzle

**Contents**:
- How to migrate from Drizzle to Prisma ORM
- Introduction​
- Prerequisites​
- Overview of the migration process​
- Step 1. Install the Prisma CLI​
- Step 2. Introspect your database​
  - 2.1. Set up Prisma ORM​
  - 2.2. Connect your database​

This guide shows you how to migrate your application from Drizzle to Prisma ORM. We'll use a sample project based off of the Drizzle Next.js example to demonstrate the migration steps. You can find the example used for this guide on GitHub.

You can learn how Prisma ORM compares to Drizzle on the Prisma ORM vs Drizzle page.

Before starting this guide, make sure you have:

this migration guide uses Neon PostgreSQL as the example database, but it equally applies to any other relational database that are supported by Prisma ORM.

You can learn how Prisma ORM compares to Drizzle on the Prisma ORM vs Drizzle page.

Note that the steps for migrating from Drizzle to Prisma ORM are always the same, no matter what kind of application or API layer you're building:

These steps apply, no matter if you're building a REST API (e.g. with Express, koa or NestJS), a GraphQL API (e.g. with Apollo Server, TypeGraphQL or Nexus) or any other kind of application that uses Drizzle for database access.

Prisma ORM lends itself really well for incremental adoption. This means, you don't have migrate your entire project from Drizzle to Prisma ORM at once, but rather you can step-by-step move your database queries from Drizzle to Prisma ORM.

The first step to adopt Prisma ORM is to install the Prisma CLI in your project:

Before you can introspect your database, you need to set up your Prisma schema and connect Prisma to your database. Run the following command in the root of your project to create a basic Prisma schema file:

This command created a new directory called prisma with the following files for you:

You may already have a .env file. If so, the prisma init command will append lines to it rather than creating a new file.

The Prisma schema currently looks as follows:

If you're using VS Code, be sure to install the Prisma VS Code extension for syntax highlighting, formatting, auto-completion and a lot more cool features.

If you're not using PostgreSQL, you need to adjust the pro

*[Content truncated - see full docs]*

**Examples**:

```terminal
npm install prisma --save-dev && npm install @prisma/client
```

```terminal
npx prisma init --output ../generated/prisma
```

```prisma
// This is your Prisma schema file,// learn more about it in the docs: https://pris.ly/d/prisma-schemadatasource db {  provider = "postgresql"  url      = env("DATABASE_URL")}generator client {  provider = "prisma-client-js"}
```

---

## How to migrate from Mongoose to Prisma ORM | Prisma Documentation

**URL**: https://www.prisma.io/docs/guides/migrate-from-mongoose

**Contents**:
- How to migrate from Mongoose to Prisma ORM
- Introduction​
- Prerequisites​
- 1. Prepare for migration​
  - 1.1. Understand the migration process​
  - 1.2. Set up Prisma configuration​
- 2. Migrate the database schema​
  - 2.1. Introspect your database​

This guide shows you how to migrate your application from Mongoose to Prisma ORM. We'll use an extended version of the Mongoose Express example as a sample project to demonstrate the migration steps.

You can learn how Prisma ORM compares to Mongoose on the Prisma ORM vs Mongoose page.

Before starting this guide, make sure you have:

The steps for migrating from Mongoose to Prisma ORM are always the same, no matter what kind of application or API layer you're building:

These steps apply whether you're building a REST API (e.g., with Express, Koa, or NestJS), a GraphQL API (e.g., with Apollo Server, TypeGraphQL, or Nexus), or any other kind of application that uses Mongoose for database access.

Create a new Prisma schema file:

This command creates:

The Prisma schema currently looks as follows:

For an optimal development experience when working with Prisma ORM, refer to editor setup to learn about syntax highlighting, formatting, auto-completion, and many more cool features.

Update the DATABASE_URL in the .env file with your MongoDB connection string:

MongoDB is a schemaless database. To incrementally adopt Prisma ORM in your project, ensure your database is populated with sample data. Prisma ORM introspects a MongoDB schema by sampling data stored and inferring the schema from the data in the database.

Run Prisma's introspection to create the Prisma schema from your existing database:

This will create a schema.prisma file with your database schema.

MongoDB doesn't support relations between different collections. However, you can create references between documents using the ObjectId field type or from one document to many using an array of ObjectIds in the collection. The reference will store id(s) of the related document(s). You can use the populate() method that Mongoose provides to populate the reference with the data of the related document.

Update the 1-n relationship between posts <-> users as follows:

Your schema should now look like this:

Then, 

*[Content truncated - see full docs]*

**Examples**:

```terminal
npx prisma init --datasource-provider mongodb --output ../generated/prisma
```

```prisma
// This is your Prisma schema file,// learn more about it in the docs: https://pris.ly/d/prisma-schemadatasource db {  provider = "mongodb"  url      = env("DATABASE_URL")}generator client {  provider = "prisma-client-js"}
```

```env
DATABASE_URL="mongodb://USER:PASSWORD@HOST:PORT/DATABASE"
```

---

## How to migrate from Sequelize to Prisma ORM | Prisma Documentation

**URL**: https://www.prisma.io/docs/guides/migrate-from-sequelize

**Contents**:
- How to migrate from Sequelize to Prisma ORM
- Introduction​
- Prerequisites​
- 1. Prepare for migration​
  - 1.1. Understand the migration process​
  - 1.2. Set up Prisma configuration​
- 2. Migrate the database schema​
  - 2.1. Introspect your database​

This guide shows you how to migrate your application from Sequelize to Prisma ORM. We'll use an extended version of the Sequelize Express example as a sample project to demonstrate the migration steps.

This migration guide uses PostgreSQL as the example database, but it equally applies to any other relational database that's supported by Prisma ORM. You can learn how Prisma ORM compares to Sequelize on the Prisma ORM vs Sequelize page.

Before starting this guide, make sure you have:

The steps for migrating from Sequelize to Prisma ORM are always the same, no matter what kind of application or API layer you're building:

These steps apply whether you're building a REST API (e.g., with Express, Koa, or NestJS), a GraphQL API (e.g., with Apollo Server, TypeGraphQL, or Nexus), or any other kind of application that uses Sequelize for database access.

Create a new Prisma schema file:

This command created a new directory called prisma with the following files for you:

The Prisma schema currently looks as follows:

If you're using VS Code, be sure to install the Prisma VS Code extension for syntax highlighting, formatting, auto-completion and a lot more cool features.

Update the DATABASE_URL in the .env file with your database connection string:

Run Prisma's introspection to create the Prisma schema from your existing database:

This will create a schema.prisma file with your database schema.

To continue using Prisma Migrate to evolve your database schema, you will need to baseline your database.

First, create a migrations directory and add a directory inside with your preferred name for the migration. In this example, we will use 0_init as the migration name:

Next, generate the migration file with prisma migrate diff. Use the following arguments:

The command will mark 0_init as applied by adding it to the _prisma_migrations table.

You now have a baseline for your current database schema. To make further changes to your database schema, you can update your Pris

*[Content truncated - see full docs]*

**Examples**:

```terminal
npx prisma init --output ../generated/prisma
```

```prisma
// This is your Prisma schema file,// learn more about it in the docs: https://pris.ly/d/prisma-schemadatasource db {  provider = "postgresql"  url      = env("DATABASE_URL")}generator client {  provider = "prisma-client-js"}
```

```env
DATABASE_URL="postgresql://USER:PASSWORD@HOST:PORT/DATABASE"
```

---

## How to migrate from TypeORM to Prisma ORM | Prisma Documentation

**URL**: https://www.prisma.io/docs/guides/migrate-from-typeorm

**Contents**:
- How to migrate from TypeORM to Prisma ORM
- Introduction​
- Prerequisites​
- 2. Prepare for migration​
  - 2.1. Understand the migration process​
  - 2.2. Set up Prisma configuration​
- 3. Migrate the database schema​
  - 3.1. Introspect your database​

This guide shows you how to migrate your application from TypeORM to Prisma ORM. We'll use an extended version of the TypeORM Express example as a sample project to demonstrate the migration steps.

This migration guide uses PostgreSQL as the example database, but it equally applies to any other relational database that's supported by Prisma ORM. You can learn how Prisma ORM compares to TypeORM on the Prisma ORM vs TypeORM page.

Before starting this guide, make sure you have:

The steps for migrating from TypeORM to Prisma ORM are always the same, no matter what kind of application or API layer you're building:

These steps apply whether you're building a REST API (e.g., with Express, Koa, or NestJS), a GraphQL API (e.g., with Apollo Server, TypeGraphQL, or Nexus), or any other kind of application that uses TypeORM for database access.

Create a new Prisma schema file:

Update the DATABASE_URL in the .env file with your database connection string:

Run Prisma's introspection to create the Prisma schema from your existing database:

This will create a schema.prisma file with your database schema.

Create and apply a baseline migration to mark the current state of your database:

Install the Prisma Client package:

Generate Prisma Client:

Start replacing your TypeORM queries with Prisma Client. Here's an example of how to convert some common queries:

Update your Express controllers to use Prisma Client. For example, here's how to update the CreateUserAction:

Test all migrated endpoints to ensure they work as expected:

Now that you've migrated to Prisma ORM, you can:

For more information:

Continue your Prisma journey by connecting with our active community. Stay informed, get involved, and collaborate with other developers:

**Examples**:

```terminal
npx prisma init --output ../generated/prisma
```

```env
DATABASE_URL="postgresql://USER:PASSWORD@HOST:PORT/DATABASE"
```

```terminal
npx prisma db pull
```

---

## How to use AI SDK with Prisma and Next.js for chat applications | Prisma Documentation

**URL**: https://www.prisma.io/docs/guides/ai-sdk-nextjs

**Contents**:
- How to use AI SDK with Prisma and Next.js for chat applications
- Introduction​
- Prerequisites​
- 1. Set up your project​
- 2. Install and Configure Prisma​
  - 2.1. Install dependencies​
  - 2.2. Define your Prisma Schema​
  - 2.3. Configure the Prisma Client generator​

Prisma ORM streamlines database access with type-safe queries, and when paired with Next.js and AI SDK, it creates a powerful foundation for building AI-powered chat applications with persistent storage.

In this guide, you'll learn to build a chat application using AI SDK with Next.js and Prisma ORM to store chat sessions and messages in a Prisma Postgres database. You can find a complete example of this guide on GitHub.

To get started, you'll need to create a new Next.js project.

It will prompt you to customize your setup. Choose the defaults:

Navigate to the project directory:

To get started with Prisma, you'll need to install a few dependencies:

Once installed, initialize Prisma in your project:

You'll need to answer a few questions while setting up your Prisma Postgres database. Select the region closest to your location and a memorable name for your database like "My Next.js AI SDK Project"

In the prisma/schema.prisma file, add the following models:

This creates three models: Session, Message, and MessageRole.

Now, run the following command to create the database tables and generate the Prisma Client:

Create a /lib directory and a prisma.ts file inside it. This file will be used to create and export your Prisma Client instance.

Set up the Prisma client like this:

We recommend using a connection pooler (like Prisma Accelerate) to manage database connections efficiently.

If you choose not to use one, avoid instantiating PrismaClient globally in long-lived environments. Instead, create and dispose of the client per request to prevent exhausting your database connections.

Install the AI SDK package:

To use AI SDK, you'll need to obtain an API key from OpenAI.

You need to create a route handler to handle the AI SDK requests. This handler will process chat messages and stream AI responses back to the client.

Set up the basic route handler:

To save chat sessions and messages to the database, we need to:

Create a new file at lib/save-chat.ts to save

*[Content truncated - see full docs]*

**Examples**:

```terminal
npx create-next-app@latest ai-sdk-prisma
```

```terminal
cd ai-sdk-prisma
```

```terminal
npm install prisma tsx --save-devnpm install @prisma/extension-accelerate @prisma/client
```

---

## How to use Prisma ORM and Prisma Postgres with Astro | Prisma Documentation

**URL**: https://www.prisma.io/docs/guides/astro

**Contents**:
- How to use Prisma ORM with Astro
- Introduction​
- Prerequisites​
- 1. Set up your project​
- 2. Install and Configure Prisma​
  - 2.1. Install dependencies​
  - 2.2. Define your Prisma Schema​
  - 2.3. Configure the Prisma Client generator​

Prisma ORM offers type-safe database access, and Astro is built for performance. Together with Prisma Postgres, you get a fast, content-first stack with zero cold starts and end-to-end speed.

In this guide, you'll learn to integrate Prisma ORM with a Prisma Postgres database in an Astro project from scratch. You can find a complete example of this guide on GitHub.

Create a new Astro project:

To get started with Prisma, you'll need to install a few dependencies:

Once installed, initialize Prisma in your project:

You'll need to answer a few questions while setting up your Prisma Postgres database. Select the region closest to your location and a memorable name for your database like "My Astro Project"

In the prisma/schema.prisma file, add the following models and change the generator to use the prisma-client provider:

This creates two models: User and Post, with a one-to-many relationship between them.

Now, run the following command to create the database tables and generate the Prisma Client:

Let's add some seed data to populate the database with sample users and posts.

Create a new file called seed.ts in the prisma/ directory:

Now, tell Prisma how to run this script by updating your package.json:

And open Prisma Studio to inspect your data:

First, create an env.d.ts file in your src directory to provide TypeScript definitions for environment variables:

Inside of /src, create a lib directory and a prisma.ts file inside it. This file will be used to create and export your Prisma Client instance.

Set up the Prisma client like this:

We recommend using a connection pooler (like Prisma Accelerate) to manage database connections efficiently.

If you choose not to use one, avoid instantiating PrismaClient globally in long-lived environments. Instead, create and dispose of the client per request to prevent exhausting your database connections.

An API route is the best way to fetch data from your database in an Astro app.

Create a new file called api/users.t

*[Content truncated - see full docs]*

**Examples**:

```terminal
npx create-astro@latest
```

```terminal
npm install prisma tsx --save-devnpm install @prisma/extension-accelerate @prisma/client
```

```terminal
npm install prisma tsx --save-devnpm install @prisma/client
```

---

## How to use Prisma ORM and Prisma Postgres with Auth.js and Next.js | Prisma Documentation

**URL**: https://www.prisma.io/docs/guides/authjs-nextjs

**Contents**:
- How to use Prisma ORM with Auth.js and Next.js
- Introduction​
- Prerequisites​
- 1. Set up your project​
- 2. Install and configure Prisma​
  - 2.1. Install dependencies​
  - 2.2. Define your Prisma Schema​
  - 2.3. Configure the Prisma Client generator​

Auth.js is a flexible, open-source authentication library designed to simplify adding authentication to your Next.js applications.

In this guide, you'll wire Auth.js into a brand-new Next.js app and persist users in a Prisma Postgres database. You can find a complete example of this guide on GitHub.

Create a new Next.js application:

It will prompt you to customize your setup. Choose the defaults:

Navigate to the project directory:

To get started with Prisma, you'll need to install a few dependencies:

Once installed, initialize Prisma in your project:

You'll need to answer a few questions while setting up your Prisma Postgres database. Select the region closest to your location and a memorable name for your database like "My Auth.js Project"

In the prisma/schema.prisma file, swap the provider to prisma-client and add the runtime vercel-edge to the generator:

Add the following models to the schema.prisma file, these models are provided by Auth.js:

This creates the following models:

Account: Stores OAuth provider information (access tokens, refresh tokens, provider account IDs) and enables users to sign in with multiple providers while maintaining a single user record.

Session: Tracks authenticated user sessions with a unique session token, user ID, and expiration time to maintain authentication state across requests.

User: The core model storing user information (name, email, profile image). Users can have multiple accounts from different providers and multiple active sessions.

VerificationToken: Stores temporary tokens for email verification, password reset, and other security operations with expiration times.

Now, run the following command to create the database tables and generate the Prisma Client:

Create a new folder in the root called lib and create a new file called prisma.ts in it. This file will contain the Prisma Client:

Install the Auth.js dependencies:

For this guide, you'll be setting up OAuth with Github. For this, you'll need 3 environ

*[Content truncated - see full docs]*

**Examples**:

```terminal
npx create-next-app@latest authjs-prisma
```

```terminal
cd authjs-prisma
```

```terminal
npm install prisma tsx --save-devnpm install @prisma/extension-accelerate @prisma/client
```

---

## How to use Prisma ORM and Prisma Postgres with Bun | Prisma Documentation

**URL**: https://www.prisma.io/docs/guides/bun

**Contents**:
- How to use Prisma in Bun
- Introduction​
- Prerequisites​
- 1. Setting up your Bun project​
- 2. Installing and configuring Prisma​
  - 2.1. Install dependencies​
  - 2.2. Initialize Prisma ORM with Prisma Postgres​
  - 2.3. Configure environment variables for driver adapters​

Bun is a fast JavaScript runtime that includes a bundler, test runner, and package manager. In this guide, you will set up a Bun project with Prisma ORM and a Prisma Postgres database. You will configure Prisma driver adapters, create a simple HTTP server, and build a Bun executable for deployment.

First, create a directory for your project and navigate to it:

Then, initialise a new Bun project:

This creates a basic Bun project that includes a package.json file and an index.ts file.

Install the required Prisma packages and other dependencies:

Initialize Prisma ORM with Prisma Postgres in your project:

You'll need to answer a few questions while setting up your Prisma Postgres database. Select the region closest to your location and a memorable name for your database like "My Bun Project"

This command creates:

We are going to use the node-postgres driver adapter to perform queries to our database.

When using the node-postgres driver adapter with Prisma Postgres, you need to add a DIRECT_URL environment variable. This provides a direct connection to your PostgreSQL database.

To get your direct connection string:

Update your .env file to include both URLs:

Open prisma/schema.prisma and update it to use driver adapters with Bun runtime:

Create a db.ts file in your project root to configure PrismaClient with the node-postgres adapter:

Create a seed script in the prisma folder to populate your database with sample data:

Create a prisma.config.ts file to configure Prisma's seed command:

Then add the following content to the file:

Generate the Prisma client and apply your schema to the database:

Because you are using the node-postgres driver adapter, you will need to generate the PrismaClient again. The client automatically produced by migrate dev is optimized for Prisma Postgres, but the adapter requires a client built specifically for the driver:

Run the seed script to populate your database:

Replace the index.ts file contents with the following code t

*[Content truncated - see full docs]*

**Examples**:

```terminal
mkdir bun-prismacd bun-prisma
```

```terminal
bun init -y
```

```terminal
bun add -d prismabun add @prisma/client @prisma/adapter-pg dotenv
```

---

## How to use Prisma ORM and Prisma Postgres with Hono | Prisma Documentation

**URL**: https://www.prisma.io/docs/guides/hono

**Contents**:
- How to use Prisma with Hono
- Introduction​
- Prerequisites​
- 1. Set up your project​
- 2. Install and configure Prisma​
  - 2.1. Install dependencies​
  - 2.2. Define your Prisma Schema​
  - 2.3. Configure the Prisma Client generator​

Prisma ORM offers type-safe database access, and Hono is built for fast, lightweight web apps. Together with Prisma Postgres, you get a fast, lightweight backend, that can be deployed through Node.js, Cloudflare, or many other runtimes.

In this guide, you'll learn to integrate Prisma ORM with a Prisma Postgres database in a Hono backend application. You can find a complete example of this guide on GitHub.

Create a new Hono project:

To get started with Prisma, you'll need to install a few dependencies:

Once installed, initialize Prisma in your project:

You'll need to answer a few questions while setting up your Prisma Postgres database. Select the region closest to your location and a memorable name for your database like "My Hono Project"

In the prisma/schema.prisma file, add the following models and change the generator to use the prisma-client provider:

This creates two models: User and Post, with a one-to-many relationship between them.

Now, run the following command to create the database tables and generate the Prisma Client:

Let's add some seed data to populate the database with sample users and posts.

Create a new file called seed.ts in the prisma/ directory:

Now, tell Prisma how to run this script by updating your package.json:

And open Prisma Studio to inspect your data:

Inside of /src, create a lib directory and a prisma.ts file inside it. This file will be used to create and export your Prisma Client instance. Set up the Prisma client like this:

We recommend using a connection pooler (like Prisma Accelerate) to manage database connections efficiently.

If you choose not to use one, in long-lived environments (for example, a Node.js server) instantiate a single PrismaClient and reuse it across requests to avoid exhausting database connections. In serverless environments or when using a pooler (for example, Accelerate), creating a client per request is acceptable.

By default, Hono does not load any environment variables from a .env. dotenv ha

*[Content truncated - see full docs]*

**Examples**:

```terminal
npm create hono@latest
```

```terminal
npm install prisma --save-devnpm install @prisma/extension-accelerate @prisma/client dotenv
```

```terminal
npm install prisma --save-devnpm install @prisma/client dotenv
```

---

## How to use Prisma ORM and Prisma Postgres with Next.js 15 and Vercel | Prisma Documentation

**URL**: https://www.prisma.io/docs/guides/nextjs

**Contents**:
- How to use Prisma ORM with Next.js
- Introduction​
- Prerequisites​
- 1. Set up your project​
- 2. Install and Configure Prisma​
  - 2.1. Install dependencies​
  - 2.2. Define your Prisma Schema​
  - 2.3. Configure the Prisma Client generator​

This guide shows you how to use Prisma with Next.js 15, a fullstack React framework. You'll learn how to create a Prisma Postgres instance, set up Prisma ORM with Next.js, handle migrations, and deploy your application to Vercel.

You can find a deployment-ready example on GitHub.

From the directory where you want to create your project, run create-next-app to create a new Next.js app that you will be using for this guide.

You will be prompted to answer a few questions about your project. Select all of the defaults.

For reference, those are:

Then, navigate to the project directory:

To get started with Prisma, you'll need to install a few dependencies:

Once installed, initialize Prisma in your project:

You'll need to answer a few questions while setting up your Prisma Postgres database. Select the region closest to your location and a memorable name for your database like "My __________ Project"

In the prisma/schema.prisma file, add the following models:

This creates two models: User and Post, with a one-to-many relationship between them.

Now, run the following command to create the database tables and generate the Prisma Client:

Add some seed data to populate the database with sample users and posts.

Create a new file called seed.ts in the prisma/ directory:

Now, tell Prisma how to run this script by updating your package.json:

Before starting the development server, note that if you are using Next.js v15.2.0 or v15.2.1, do not use Turbopack as there is a known issue. Remove Turbopack from your dev script by updating your package.json

This change is not needed on any versions before or after.

Finally, run prisma db seed to seed your database with the initial data we defined in the seed.ts file.

And open Prisma Studio to inspect your data:

Now that you have a database with some initial data, you can set up Prisma Client and connect it to your database.

At the root of your project, create a new lib directory and add a prisma.ts file to it.

Now, add

*[Content truncated - see full docs]*

**Examples**:

```terminal
npx create-next-app@latest nextjs-prisma
```

```terminal
cd nextjs-prisma
```

```terminal
npm install prisma tsx --save-devnpm install @prisma/extension-accelerate @prisma/client
```

---

## How to use Prisma ORM and Prisma Postgres with React Router 7 | Prisma Documentation

**URL**: https://www.prisma.io/docs/guides/react-router-7

**Contents**:
- How to use Prisma ORM with React Router 7
- Introduction​
- Prerequisites​
- 1. Set up your project​
- 2. Install and Configure Prisma​
  - 2.1. Install dependencies​
  - 2.2. Define your Prisma Schema​
  - 2.3. Configure the Prisma Client generator​

This guide shows you how to use Prisma ORM with React Router 7, a multi-strategy router that can be as minimal as declarative routing or as full-featured as a fullstack framework.

You'll learn how to set up Prisma ORM and Prisma Postgres with React Router 7 and handle migrations. You can find a deployment-ready example on GitHub.

From the directory where you want to create your project, run create-react-router to create a new React Router app that you will be using for this guide.

You'll be prompted to select the following, select Yes for both:

Now, navigate to the project directory:

To get started with Prisma, you'll need to install a few dependencies:

Once installed, initialize Prisma in your project:

You'll need to answer a few questions while setting up your Prisma Postgres database. Select the region closest to your location and a memorable name for your database like "My React Router 7 Project"

In the prisma/schema.prisma file, add the following models and change the generator to use the prisma-client provider:

This creates two models: User and Post, with a one-to-many relationship between them.

Now, run the following command to create the database tables and generate the Prisma Client:

Add some seed data to populate the database with sample users and posts.

Create a new file called seed.ts in the prisma/ directory:

Now, tell Prisma how to run this script by updating your package.json:

And open Prisma Studio to inspect your data:

Inside of your app directory, create a new lib directory and add a prisma.ts file to it. This file will be used to create and export your Prisma Client instance.

Set up the Prisma client like this:

We recommend using a connection pooler (like Prisma Accelerate) to manage database connections efficiently.

If you choose not to use one, avoid instantiating PrismaClient globally in long-lived environments. Instead, create and dispose of the client per request to prevent exhausting your database connections.

You'll use t

*[Content truncated - see full docs]*

**Examples**:

```terminal
npx create-react-router@latest react-router-7-prisma
```

```terminal
cd react-router-7-prisma
```

```terminal
npm install prisma tsx --save-devnpm install @prisma/extension-accelerate @prisma/client
```

---

## How to use Prisma ORM and Prisma Postgres with SolidStart | Prisma Documentation

**URL**: https://www.prisma.io/docs/guides/solid-start

**Contents**:
- How to use Prisma ORM with SolidStart
- Introduction​
- Prerequisites​
- 1. Set up your project​
- 2. Install and Configure Prisma​
  - 2.1. Install dependencies​
  - 2.2. Define your Prisma Schema​
  - 2.3. Configure the Prisma Client generator​

Prisma ORM streamlines database access with type-safe queries and a smooth developer experience. SolidStart, a modern framework for building reactive web apps with SolidJS, pairs well with Prisma and Postgres to create a clean and scalable full-stack architecture.

In this guide, you'll learn how to integrate Prisma ORM with a Prisma Postgres database in a SolidStart project from scratch. You can find a complete example of this guide on GitHub.

Begin by creating a new SolidStart app. In your terminal, run:

Use the following options when prompted:

Next, navigate into your new project, install dependencies, and start the development server:

Once the dev server is running, open http://localhost:3000 in your browser. You should see the SolidStart welcome screen.

Clean up the default UI by editing the app.tsx file and replacing its content with the following code:

To get started with Prisma, you'll need to install a few dependencies:

Once installed, initialize Prisma in your project:

You'll need to answer a few questions while setting up your Prisma Postgres database. Select the region closest to your location and a memorable name for your database like "My SolidStart Project"

In the prisma/schema.prisma file, add the following models and change the generator to use the prisma-client provider:

This creates two models: User and Post, with a one-to-many relationship between them.

Now, run the following command to create the database tables and generate the Prisma Client:

Let's add some seed data to populate the database with sample users and posts.

Create a new file called seed.ts in the prisma/ directory:

Now, tell Prisma how to run this script by updating your package.json:

And open Prisma Studio to inspect your data:

At the root of your project, create a new lib folder and a prisma.ts file inside it:

Add the following code to create a Prisma Client instance:

We recommend using a connection pooler (like Prisma Accelerate) to manage database connections 

*[Content truncated - see full docs]*

**Examples**:

```terminal
npm init solid@latest
```

```terminal
cd my-solid-prisma-appnpm installnpm run dev
```

```typescript
import "./app.css";export default function App() {  return (    <main>      <h1>SolidStart + Prisma</h1>    </main>  );}
```

---

## How to use Prisma ORM and Prisma Postgres with SvelteKit | Prisma Documentation

**URL**: https://www.prisma.io/docs/guides/sveltekit

**Contents**:
- How to use Prisma ORM with SvelteKit
- Introduction​
- Prerequisites​
- 1. Set up your project​
- 2. Install and Configure Prisma​
  - 2.1. Install dependencies​
  - 2.2. Define your Prisma Schema​
  - 2.3. Configure the Prisma Client generator​

Prisma ORM simplifies database access with type-safe queries, and when paired with SvelteKit, it creates a robust and scalable full-stack architecture.

In this guide, you'll learn to integrate Prisma ORM with a Prisma Postgres database in a SvelteKit project from scratch. You can find a complete example of this guide on GitHub.

You'll be using Svelte CLI instead of npx create svelte@latest. This CLI provides a more interactive setup and built-in support for popular tooling like ESLint and Prettier

Create a new Svelte project:

It will prompt you to customize your setup. Here are the options you'll choose:

Once the setup completes, navigate into your project and start the development server:

That's it! Svelte makes it a very simple process to get up and running. At this point, your project is ready to integrate Prisma and connect to a Prisma Postgres database.

To get started with Prisma, you'll need to install a few dependencies:

Once installed, initialize Prisma in your project:

You'll need to answer a few questions while setting up your Prisma Postgres database. Select the region closest to your location and a memorable name for your database like "My SvelteKit Project"

In the prisma/schema.prisma file, add the following models and change the generator to use the prisma-client provider:

This creates two models: User and Post, with a one-to-many relationship between them.

Now, run the following command to create the database tables and generate the Prisma Client:

Add some seed data to populate the database with sample users and posts.

Create a new file called seed.ts in the prisma/ directory:

Now, tell Prisma how to run this script by updating your package.json:

And open Prisma Studio to inspect your data:

Inside your /src/lib directory, rename index.ts to prisma.ts. This file will be used to create and export your Prisma Client instance.

Files in src/lib can be accessed from anywhere using the $lib alias.

The DATABASE_URL is stored in the .env fil

*[Content truncated - see full docs]*

**Examples**:

```terminal
npx sv create sveltekit-prisma
```

```terminal
cd sveltekit-prismanpm run dev
```

```terminal
npm install prisma tsx --save-devnpm install @prisma/extension-accelerate @prisma/client
```

---

## How to use Prisma ORM and Prisma Postgres with TanStack Start | Prisma Documentation

**URL**: https://www.prisma.io/docs/guides/tanstack-start

**Contents**:
- How to use Prisma ORM with TanStack Start
- Introduction​
- Prerequisites​
- 1. Set up your project​
- 2. Install and Configure Prisma​
  - 2.1. Install dependencies​
  - 2.2. Define your Prisma Schema​
  - 2.3. Configure the Prisma Client generator​

Prisma ORM simplifies database interactions, and TanStack Start offers a robust framework for building modern React applications. Together with Prisma Postgres, they provide a seamless full-stack development experience with type-safe queries and efficient data management.

This guide will walk you through integrating Prisma ORM with a Prisma Postgres database in a TanStack Start project from scratch.

To begin, create a new TanStack Start project.

For the purpose of this guide, we're using the same setup instructions that you can find in the TanStart Start docs.

In the directory where you'd like to create your project, run the following commands:

This will create a new folder called tanstack-start-prisma, navigate into it, and initialize a new Node.js project.

Open the directory in your IDE and create a tsconfig.json file with the following configuration:

We also need a .gitignore file, so let's set that up now:

Next, install TanStack Router and Vinxi, as TanStack Start currently requires them:

We also need React, the Vite React plugin, and TypeScript:

Update your package.json to use Vinxi's CLI. Add "type": "module" and modify the scripts to use Vinxi's CLI:

Then, create and configure TanStack Start's app.config.ts file:

For TanStack Start to function, we need 5 files in ~/app/:

You can create them with these commands:

router.tsx configures the application's main router with route definitions and settings:

You should be seeing an error about routeTree.gen.ts not existing. This is expected. It will be generated when you run TanStack Start for the first time.

ssr.tsx allows us to know what routes and loaders we need to execute when the user hits a given route:

client.tsx initializes the client-side logic to handle routes in the browser:

routes/__root.tsx defines the root route and global HTML layout for the entire application:

routes/index.tsx is the home page of the application:

This will generate the routeTree.gen.ts file and resolve any routing e

*[Content truncated - see full docs]*

**Examples**:

```terminal
mkdir tanstack-start-prismacd tanstack-start-prismanpm init -y
```

```json
{  "compilerOptions": {    "jsx": "react-jsx",    "moduleResolution": "Bundler",    "module": "ESNext",    "target": "ES2022",    "skipLibCheck": true,    "strictNullChecks": true  }}
```

```txt
node_modules.envapp/generated
```

---

## How to use Prisma ORM in a pnpm workspaces monorepo | Prisma Documentation

**URL**: https://www.prisma.io/docs/guides/use-prisma-in-pnpm-workspaces

**Contents**:
- How to use Prisma ORM in a pnpm workspaces monorepo
  - What you'll learn:​
- 1. Prepare your project and configure pnpm workspaces​
- 2. Setup the shared database package​
  - 2.1. Initialize the package and install dependencies​
  - 2.2. Setup Prisma ORM in your database package​
- 3. Set up and integrate your frontend application​
  - 3.1. Bootstrap a Next.js application​

Prisma is a powerful ORM for managing your database, and when combined with pnpm Workspaces, you can maintain a lean and modular monorepo architecture. In this guide, we’ll walk through setting up Prisma in its own package within a pnpm Workspaces monorepo, enabling maintainable type sharing and efficient database management across your apps.

Before integrating Prisma, you need to set up your project structure. Start by creating a new directory for your project (for example, my-monorepo) and initialize a Node.js project:

Next, create a pnpm-workspace.yaml file to define your workspace structure and pin the Prisma version:

Add the following configuration to pnpm-workspace.yaml:

The catalogs help you pin a certain version of prisma across your repositories. You can learn more about them here. Explictly pin the lastest version of prisma in the pnpm-workspace.yaml file. At the time of writing, this is version 6.3.1.

Finally, create directories for your applications and shared packages:

This section covers creating a standalone database package that uses Prisma. The package will house all database models and the generated Prisma Client, making it reusable across your monorepo.

Navigate to the packages/database directory and initialize a new package:

Add Prisma as a development dependency in your package.json using the pinned catalog:

Then, add additional dependencies:

Then install the Prisma Client extension required to use Prisma Postgres:

This guide uses Prisma Postgres. If you plan to use a different database, you can omit the @prisma/extension-accelerate package.

Initalize a tsconfig.json file for your database package:

Initialize Prisma ORM with an instance of Prisma Postgres in the database package by running the following command:

Enter a name for your project and choose a database region.

We're going to be using Prisma Postgres in this guide. If you're not using a Prisma Postgres database, you won't need to add the --db flag.

Edit the schema.prism

*[Content truncated - see full docs]*

**Examples**:

```terminal
mkdir my-monorepocd my-monorepopnpm init
```

```terminal
touch pnpm-workspace.yaml
```

```yaml
packages:  - "apps/*"  - "packages/*"catalogs:  prisma:    prisma: latest
```

---

## How to use Prisma ORM with Cloudflare D1 | Prisma Documentation

**URL**: https://www.prisma.io/docs/guides/cloudflare-d1

**Contents**:
- How to use Prisma ORM with Cloudflare D1
- Introduction​
- Prerequisites​
- 1. Create a new Cloudflare Worker and initialize Prisma ORM​
- 2. Configure Prisma schema​
- 3. Install dependencies​
- 4. Create a D1 database​
- 5. Set up database migrations​

This guide shows you how to use Prisma ORM with Cloudflare D1, a serverless SQL database that runs on Cloudflare's edge network. You'll learn how to set up Prisma ORM with D1, handle migrations, and deploy your application to Cloudflare Workers. You can find a deployment-ready example on GitHub.

Before starting this guide, make sure you have:

Run the following command to create a new Cloudflare Worker project:

Then navigate into the newly created directory:

And initialize Prisma ORM in the project:

And install the Prisma ORM CLI as a development dependency:

In your Prisma schema, set the provider of the datasource to sqlite. If you just bootstrapped the Prisma schema with prisma init, also be sure to add the following User model to it:

Next, install the required packages:

Also, be sure to use a version of the Wrangler CLI that's above wrangler@^3.39.0, otherwise the --remote flag that's used in the next sections won't be available.

Run the following command to create a new D1 database:

The __YOUR_D1_DATABASE_NAME__ is a placeholder that should be replaced with the name you want to give your D1 database. For example, you can use prisma-d1-example.

This command will authenticate you with Cloudflare and ask you to select a Cloudflare account. After that, it will create a new D1 database and output the database ID and name:

Copy the terminal output and add the content to your wrangler.jsonc file. This file is used to configure your Cloudflare Worker and its bindings.

To connect your Workers with the D1 instance, add the following binding to your wrangler.jsonc:

The __YOUR_D1_DATABASE_NAME__ and __YOUR_D1_DATABASE_ID__ in the snippet above are placeholders that should be replaced with the database name and ID of your own D1 instance.

If you weren't able to grab the database ID from the terminal output, you can also find it in the Cloudflare Dashboard or by running npx wrangler d1 list and npx wrangler d1 info __YOUR_D1_DATABASE_NAME__ in your terminal.

We

*[Content truncated - see full docs]*

**Examples**:

```bash
npm create cloudflare@latest d1-tutorial -- --type=hello-world --ts=true --git=true --deploy=false
```

```bash
cd d1-tutorial
```

```bash
npx prisma init --datasource-provider sqlite
```

---

## How to use Prisma ORM with Turborepo | Prisma Documentation

**URL**: https://www.prisma.io/docs/guides/turborepo

**Contents**:
- How to use Prisma ORM with Turborepo
    - What you'll learn:​
  - Prerequisites​
- 1. Set up your project​
- 2. Add a new database package to the monorepo​
  - 2.1 Create the package and install Prisma​
  - 2.2. Initialize Prisma and define models​
    - The importance of generating Prisma types in a custom directory​

Prisma is a powerful ORM for managing databases, and Turborepo simplifies monorepo workflows. By combining these tools, you can create a scalable, modular architecture for your projects.

This guide will show you how to set up Prisma as a standalone package in a Turborepo monorepo, enabling efficient configuration, type sharing, and database management across multiple apps.

To set up a Turborepo monorepo named turborepo-prisma, run the following command:

You'll be prompted to select your package manager, this guide will use npm:

After the setup, choose a package manager for the project. Navigate to the project root directory and install Turborepo as a development dependency:

For more information about installing Turborepo, refer to the official Turborepo guide.

Create a database package within the packages directory. Then, create a package.json file for the package by running:

Define the package.json file as follows:

Next, install the required dependencies to use Prisma ORM. Use your preferred package manager:

If using Prisma Postgres, install the @prisma/extension-accelerate package:

Inside the database directory, initialize prisma by running:

This will create several files inside packages/database:

In the packages/database/prisma/schema.prisma file, add the following models:

It is recommended to add ../generated/prisma to the .gitignore file because it contains platform-specific binaries that can cause compatibility issues across different environments.

In the schema.prisma file, we specify a custom output path where Prisma will generate its types. This ensures Prisma's types are resolved correctly across different package managers.

In this guide, the types will be generated in the database/generated/prisma directory.

Let's add some scripts to the package.json inside packages/database:

Let's also add these scripts to turbo.json in the root and ensure that DATABASE_URL is added to the environment:

Migrate your prisma.schema and generate types

Navi

*[Content truncated - see full docs]*

**Examples**:

```terminal
npx create-turbo@latest turborepo-prisma
```

```terminal
cd turborepo-prismanpm install turbo --save-dev
```

```terminal
cd turborepo-prismayarn add turbo --dev --ignore-workspace-root-check
```

---

## How to use multiple databases in a single app | Prisma Documentation

**URL**: https://www.prisma.io/docs/guides/multiple-databases

**Contents**:
- How to use multiple databases in a single app
- Introduction​
- Prerequisites​
- 1. Set up a Next.js project​
- 2. Set up your databases and Prisma Clients​
  - 2.1. Create a Prisma Postgres instance to contain user data​
  - 2.2. Create a Prisma Postgres instance for post data​
  - 2.3. Add helper scripts and migrate the schemas​

This guide shows you how to use multiple databases using Prisma ORM in a single Next.js app. You will learn how to connect to two different Prisma Postgres databases, manage migrations, and deploy your application to Vercel. This approach is useful for multi-tenant applications or when you need to separate concerns when managing connections to multiple databases.

Before you begin, make sure that you have the following:

Create a new Next.js app using create-next-app from your desired directory:

You will be prompted to answer a few questions about your project. Select all of the defaults.

For completeness, those are:

Then, navigate to the project directory:

In this section, you will create two separate Prisma Postgres instances—one for user data and one for post data. You will also configure the Prisma schema and environment variables for each.

First, install Prisma as a development dependency:

Install the Prisma Client extension that is required to use Prisma Postgres:

If you are not using a Prisma Postgres database, you won't need the @prisma/extension-accelerate package.

You have installed the required dependencies for the project.

Initialize Prisma with a Prisma Postgres instance by running:

If you are not using a Prisma Postgres database, do not use the --db flag. Instead, create two PostgreSQL database instances and add their connection URLs to the .env file as PPG_USER_DATABASE_URL and PPG_POST_DATABASE_URL.

Follow the prompts to name your project and choose a database region.

The prisma@latest init --db command:

Rename the prisma folder to prisma-user-database:

Edit your .env file to rename DATABASE_URL to PPG_USER_DATABASE_URL:

Open prisma-user-database/schema.prisma file and update it to define a User model. Also, set the environment variable and specify a custom output directory for the generated Prisma Client:

Your user database schema is now ready.

Repeat the initialization for the post database:

After following the prompts, rename the

*[Content truncated - see full docs]*

**Examples**:

```terminal
npx create-next-app@latest my-multi-client-app
```

```terminal
cd my-multi-client-app
```

```terminal
npm install -D prisma
```

---

## Local development with Prisma Postgres (Early Access) | Prisma Documentation

**URL**: https://www.prisma.io/docs/postgres/database/local-development

**Contents**:
- Local development with Prisma Postgres
- Setting up local development for Prisma Postgres​
  - 1. Launching local Prisma Postgres​
  - 2. Applying migrations and seeding data​
  - 3. Running your application locally​
- Using different local Prisma Postgres instances​
- Stopping Prisma Postgres instances​
- Removing Prisma Postgres instances​

Prisma Postgres is a production-grade, cloud-native database and is ideal for staging and production environments. For rapid iteration and isolated testing, you can run a local Prisma Postgres instance (powered by PGlite) via the prisma dev command. This page explains how to install and launch a local Prisma Postgres database.

Local Prisma Postgres is in Preview and is being actively developed.

Follow these steps to set up local Prisma Postgres for development.

Please ensure you're running Node.js 20 or later, as it's required for local Prisma Postgres.

Navigate into your project and start the local Prisma Postgres server using the following command:

This starts a local Prisma Postgres server that you can connect to using Prisma ORM or another tool. The output of the command looks like this:

If you want to connect via Prisma ORM, hit h on your keyboard, copy the DATABASE_URL and store it in your .env file. This will be used to connect to the local Prisma Postgres server:

The DATABASE_URL is a connection string that Prisma uses to connect to the local Prisma Postgres server and is compatible with the Prisma Postgres extension:

This ensures no additional code changes are needed when switching from local Prisma Postgres to Prisma Postgres in production.

Keep the local Prisma Postgres server running in the background while you work on your application.

Then in a separate terminal tab, run the prisma migrate dev command to create the database and run the migrations:

Make sure the local Prisma Postgres server is running before running the prisma migrate dev command.

If you must use a different port, append --port <number> (for example, npx prisma migrate dev --port 5422) and update your DATABASE_URL (or other connection settings) to match.

This will create the database and run the migrations.

If you have a seeder script to seed the database, you should also run it in this step.

Start your application's development server. You can now perform queries against

*[Content truncated - see full docs]*

**Examples**:

```terminal
npx prisma dev
```

```no-copy
$ npx prisma dev✔  Great Success! 😉👍   Your  prisma dev  server default is ready and listening on ports 63567-63569.╭──────────────────────────────╮│[q]uit  [h]ttp url  [t]cp urls│╰──────────────────────────────╯
```

```bash
DATABASE_URL="prisma+postgres://localhost:51213/?api_key=__API_KEY__"
```

---

## MongoDB database connector | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/overview/databases/mongodb

**Contents**:
- Prisma ORM MongoDB database connector
- What is MongoDB?​
- Commonalities with other database providers​
- Differences to consider​
  - Performance considerations for large collections​
    - Problem​
    - Solution​
- How to use Prisma ORM with MongoDB​

This guide discusses the concepts behind using Prisma ORM and MongoDB, explains the commonalities and differences between MongoDB and other database providers, and leads you through the process for configuring your application to integrate with MongoDB using Prisma ORM.

To connect Prisma ORM with MongoDB, refer to our Getting Started documentation.

MongoDB is a NoSQL database that stores data in BSON format, a JSON-like document format designed for storing data in key-value pairs. It is commonly used in JavaScript application development because the document model maps easily to objects in application code, and there is built in support for high availability and horizontal scaling.

MongoDB stores data in collections that do not need a schema to be defined in advance, as you would need to do with tables in a relational database. The structure of each collection can also be changed over time. This flexibility can allow rapid iteration of your data model, but it does mean that there are a number of differences when using Prisma ORM to work with your MongoDB database.

Some aspects of using Prisma ORM with MongoDB are the same as when using Prisma ORM with a relational database. You can still:

MongoDB's document-based structure and flexible schema means that using Prisma ORM with MongoDB differs from using it with a relational database in a number of ways. These are some areas where there are differences that you need to be aware of:

Defining IDs: MongoDB documents have an _id field (that often contains an ObjectID). Prisma ORM does not support fields starting with _, so this needs to be mapped to a Prisma ORM field using the @map attribute. For more information, see Defining IDs in MongoDB.

Migrating existing data to match your Prisma schema: In relational databases, all your data must match your schema. If you change the type of a particular field in your schema when you migrate, all the data must also be updated to match. In contrast, MongoDB does not enforce a

*[Content truncated - see full docs]*

**Examples**:

```prisma
model User {  id    String @id @default(auto()) @map("_id") @db.ObjectId  email String}
```

```prisma
model User {  id          String  @id @default(auto()) @map("_id") @db.ObjectId  email       String  phoneNumber String?}
```

```prisma
model User {  id          String @id @default(auto()) @map("_id") @db.ObjectId  email       String  phoneNumber String @default("000-000-0000")}
```

---

## MySQL database connector | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/overview/databases/mysql

**Contents**:
- MySQL/MariaDB
- Example​
- Using the mariadb driver​
  - 1. Install the dependencies​
  - 2. Instantiate Prisma Client using the driver adapter​
- Connection details​
  - Connection URL​
    - Base URL and path​

The MySQL data source connector connects Prisma ORM to a MySQL or MariaDB database server.

By default, the MySQL connector contains a database driver responsible for connecting to your database. You can use a driver adapter (Preview) to connect to your database using a JavaScript database driver from Prisma Client.

To connect to a MySQL database server, you need to configure a datasource block in your Prisma schema:

The fields passed to the datasource block are:

As of v5.4.0, you can use Prisma ORM with database drivers from the JavaScript ecosystem (instead of using Prisma ORM's built-in drivers). You can do this by using a driver adapter.

For MySQL and MariaDB, mariadb is one of the most popular drivers in the JavaScript ecosystem.

This section explains how you can use it with Prisma ORM and the @prisma/adapter-mariadb driver adapter.

First, install Prisma ORM's driver adapter for mariadb:

Now, when you instantiate Prisma Client, you need to pass an instance of Prisma ORM's driver adapter to the PrismaClient constructor:

Here's an overview of the components needed for a MySQL connection URL:

Here is an example of the structure of the base URL and the path using placeholder values in uppercase letters:

The following components make up the base URL of your database, they are always required:

You must percentage-encode special characters.

A connection URL can also take arguments. Here is the same example from above with placeholder values in uppercase letters for three arguments:

The following arguments can be used:

As an example, if you want to set the connection pool size to 5 and configure a timeout for queries of 3 seconds, you can use the following arguments:

You can add various parameters to the connection URL if your database server uses SSL. Here's an overview of the possible parameters:

sslcert=<PATH>: Path to the server certificate. This is the root certificate used by the database server to sign the client certificate. You need to provide 

*[Content truncated - see full docs]*

**Examples**:

```prisma
datasource db {  provider = "mysql"  url      = env("DATABASE_URL")}
```

```terminal
npm install @prisma/adapter-mariadb
```

```ts
import { PrismaMariaDb } from '@prisma/adapter-mariadb';import { PrismaClient } from './generated/prisma';const adapter = new PrismaMariaDb({  host: "localhost",  port: 3306,  connectionLimit: 5});const prisma = new PrismaClient({ adapter });
```

---

## Native database functions | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-migrate/workflows/native-database-functions

**Contents**:
- Native database functions
- How to install a PostgreSQL extension as part of a migration​

In PostgreSQL, some native database functions are part of optional extensions. For example, in PostgreSQL versions 12.13 and earlier the gen_random_uuid() function is part of the pgcrypto extension.

To use a PostgreSQL extension, you must install it on the file system of your database server and then activate the extension. If you use Prisma Migrate, this must be done as part of a migration.

Do not activate extensions outside a migration file if you use Prisma Migrate. The shadow database requires the same extensions. Prisma Migrate creates and deletes the shadow database automatically, so the only way to activate an extension is to include it in a migration file.

In Prisma ORM versions 4.5.0 and later, you can activate the extension by declaring it in your Prisma schema with the postgresqlExtensions preview feature:

You can then apply these changes to your database with Prisma Migrate. See How to migrate PostgreSQL extensions for details.

In earlier versions of Prisma ORM, you must instead add a SQL command to your migration file to activate the extension. See How to install a PostgreSQL extension as part of a migration.

This section describes how to add a SQL command to a migration file to activate a PostgreSQL extension. If you manage PostgreSQL extensions in your Prisma Schema with the postgresqlExtensions preview feature instead, see How to migrate PostgreSQL extensions.

The following example demonstrates how to install the pgcrypto extension as part of a migration:

Add the field with the native database function to your schema:

If you include a cast operator (such as ::TEXT), you must surround the entire function with parentheses:

Use the --create-only flag to generate a new migration without applying it:

Open the generated migration.sql file and enable the pgcrypto module:

Each time you reset the database or add a new member to your team, all required functions are part of the migration history.

**Examples**:

```prisma
generator client {  provider        = "prisma-client-js"  previewFeatures = ["postgresqlExtensions"]}datasource db {  provider   = "postgresql"  url        = env("DATABASE_URL")  extensions = [pgcrypto]}
```

```prisma
model User {  id String @id @default(dbgenerated("gen_random_uuid()")) @db.Uuid}
```

```prisma
@default(dbgenerated("(gen_random_uuid()::TEXT)"))
```

---

## One doc tagged with "guides" | Prisma Documentation

**URL**: https://www.prisma.io/docs/tags/guides

**Contents**:
- One doc tagged with "guides"
- Guides

Welcome to the Guides section! Here you'll find practical, step-by-step guides to help you accomplish specific tasks with Prisma products, including Prisma ORM, Prisma Accelerate, Prisma Postgres, and more.

---

## Partner Database Provisioning & User Claim Flow | Prisma Documentation

**URL**: https://www.prisma.io/docs/guides/management-api

**Contents**:
- Partner Database Provisioning & User Claim Flow
- Introduction​
- Core concepts​
- How to become a partner​
- Get OAuth credentials​
- Provisioning a database as a Partner​
- Database claim flow​
  - Overview: How the claim flow works​

This guide walks you through how to use the Prisma Postgres Management API, to power experiences like the npx create-db command.

You'll learn how to provision a Prisma Postgres database on your workspace as a partner, and how to transfer it to another user's workspace so they can "claim" the database. We'll cover how the process is secured using OAuth2, and by the end, you'll understand the full flow and how to integrate it into your own product experience.

This guide references the actual implementation in the npx create-db CLI and Cloudflare Workers as real world examples. The repo for the npx create-db is here, which can be used as a reference for how to use the Management API in your own projects.

The two Cloudflare Workers in this guide are just reference examples. You would typically build this logic into your own backend or serverless functions.

Similarly, the npx create-db CLI is a simple demo. In your product, you can trigger the same API calls from your own UI or onboarding flows to create a seamless experience for your users.

Before diving into implementation, let's clarify the main concepts involved in the Management API integration:

To use the Prisma Postgres Management API, you first need to set up as a partner:

For a complete list of available endpoints and details on request/response formats, see the Prisma Management API documentation.

To obtain a client ID and client secret, you need go through this flow:

On the next screen, you can access and save the client ID and client secret for your OAuth app.

To provision a new Prisma Postgres database for your users as a partner, follow these steps:

Once a database is provisioned, you may want to transfer ownership to your user at a later point so they can manage it in their own Prisma workspace and go beyond the free database usage limits. This is done via the claim flow, which consists of three main steps:

When a user wants to claim a database, your app will:

This ensures the transfer is secu

*[Content truncated - see full docs]*

**Examples**:

```ts
const prismaResponse = await fetch('https://api.prisma.io/v1/projects', {  method: 'POST',  headers: {    'Content-Type': 'application/json',    Authorization: `Bearer <YOUR_SERVICE_TOKEN>`,  },  body: JSON.stringify({ region, name }),});
```

```ts
const authParams = new URLSearchParams({  client_id: YOUR_CLIENT_ID,  redirect_uri: 'https://your-app.com/auth/callback', // Your callback endpoint  response_type: 'code',  scope: 'workspace:admin', // The scope of the OAuth2 authorization  state: generateState(), // Securely track the session});const authUrl = `https://auth.prisma.io/authorize?${authParams.toString()}`;// Redirect the user to authUrl
```

```ts
const tokenResponse = await fetch('https://auth.prisma.io/token', {  method: 'POST',  headers: { 'Content-Type': 'application/x-www-form-urlencoded' },  body: new URLSearchParams({    grant_type: 'authorization_code',    code: code, // The code received from the callback    redirect_uri: 'https://your-app.com/auth/callback', // Must match the redirect_uri used in step 1    client_id: YOUR_CLIENT_ID,    client_secret: YOUR_CLIENT_SECRET,  }).toString(),});const tokenData = await tokenResponse.jso
...
```

---

## Prisma Guides | Prisma Documentation

**URL**: https://www.prisma.io/docs/guides

**Contents**:
- Guides
- Available Guides​
- Web Frameworks
- Development Tools
- Integration Solutions
- Database Management
- Prisma Postgres for Platforms
- Connection Pooling Guides

Welcome to the Guides section! Here you'll find practical, step-by-step guides to help you accomplish specific tasks with Prisma products, including Prisma ORM, Prisma Accelerate, Prisma Postgres, and more.

Browse through our guides below or use the search to find specific topics.

---

## Prisma Migrate | Database, Schema, SQL Migration Tool | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-migrate

**Contents**:
- Prisma Migrate
- In this section​
- Getting started
- Understanding Prisma Migrate
- Workflows

This page explains how to get started with migrating your schema in a development environment using Prisma Migrate.

---

## Prisma Postgres database features | Prisma Documentation

**URL**: https://www.prisma.io/docs/postgres/database

**Contents**:
- Database
- In this section​
- Caching
- Connection pooling
- Backups
- Postgres extensions
- Local development
- Direct connections

Learn how Prisma Postgres implements foundational database features such as built-in caching, connection pooling, backups, and secure access. These features are powered by Prisma Postgres infrastructure and designed to optimize application performance and reliability.

Prisma Postgres supports built-in query caching to reduce database load and improve query performance. You can configure cache behavior using the cacheStrategy option available in all read queries.

Prisma Postgres provides built-in connection pooling by default, enabled by Prisma Accelerate. By using Prisma Postgres, you get the benefits of connection pooling without having to configure anything. The efficient management of database connections allows the database to process more queries without exhausting the available database connections, making your application more scalable.

Prisma Postgres is a production-grade, cloud-native database and is ideal for staging and production environments. For rapid iteration and isolated testing, you can run a local Prisma Postgres instance (powered by PGlite) via the prisma dev command. This page explains how to install and launch a local Prisma Postgres database.

The serverless driver for Prisma Postgres is a lightweight and minimal client library that can talk to Prisma Postgres using raw SQL. You can use it via the @prisma/ppg npm package.

---

## Prisma Postgres introduction | Prisma Documentation

**URL**: https://www.prisma.io/docs/postgres/introduction

**Contents**:
- Introduction to Prisma Postgres
- In this section​
- Getting started
- npx create-db
- Import from existing database
- Management API
- Overview

Get familiar with Prisma Postgres and its core concepts. This section covers what Prisma Postgres is and how to begin using it with minimal setup.

create-db is an open-source CLI tool that provisions temporary Prisma Postgres databases with a single command.

If you have an existing database and want to import your data into Prisma Postgres, you can use one of our guides:

Prisma Postgres is a managed PostgreSQL database service that easily lets you create a new database, interact with it through Prisma ORM, and build applications that start small and cheap but can scale to millions of users.

---

## Prisma Studio for Prisma Postgres | Prisma Documentation

**URL**: https://www.prisma.io/docs/postgres/database/prisma-studio

**Contents**:
- Prisma Studio
- Overview​

Prisma Postgres comes with Prisma Studio built-in. You can use it in several ways:

If you want to use Prisma Studio with another database than Prisma Postgres, check the docs here.

---

## Prisma Studio in VS Code | Prisma Documentation

**URL**: https://www.prisma.io/docs/postgres/database/prisma-studio/studio-in-vs-code

**Contents**:
- Studio in VS Code
- Overview​
- Usage​

You can use Prisma Studio directly in VS Code via the Prisma VS Code extension.

---

## SQL Server on Docker | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/overview/databases/sql-server/sql-server-docker

**Contents**:
- SQL Server on Docker
- Connection URL credentials​

To run a Microsoft SQL Server container image with Docker:

Install and set up Docker

Run the following command in your terminal to download the Microsoft SQL Server 2019 image:

Create an instance of the container image, replacing the value of SA_PASSWORD with a password of your choice:

Follow Microsoft's instructions to connect to SQL Server and use the sqlcmd tool, replacing the image name and password with your own.

From the sqlcmd command prompt, create a new database:

Run the following command to check that your database was created successfully:

Based on this example, your credentials are:

**Examples**:

```terminal
docker pull mcr.microsoft.com/mssql/server:2019-latest
```

```terminal
docker run --name sql_container -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=myPassword' -p 1433:1433 -d mcr.microsoft.com/mssql/server:2019-latest
```

```terminal
CREATE DATABASE quickstartGO
```

---

## SQL Server on Windows | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/overview/databases/sql-server/sql-server-local

**Contents**:
- SQL Server on Windows (local)
- Enable TCP/IP​
- Enable authentication with SQL logins (Optional)​
  - Enable the sa login​

To run a Microsoft SQL Server locally on a Windows machine:

If you do not have access to an instance of Microsoft SQL Server, download and set up SQL Server 2019 Developer.

Download and install SQL Server Management Studio.

Use Windows Authentication to log in to Microsoft SQL Server Management Studio (expand the Server Name dropdown and click <Browse for more...> to find your database engine):

Prisma Client requires TCP/IP to be enabled. To enable TCP/IP:

Open SQL Server Configuration Manager. (Search for "SQL Server Configuration Manager" in the Start Menu, or open the Start Menu and type "SQL Server Configuration Manager".)

In the left-hand panel, click SQL Server Network Configuration > Protocols for MSSQLSERVER

Right-click TCP/IP and choose Enable.

If you want to use a username and password in your connection URL rather than integrated security, enable mixed authentication mode as follows:

Right-click on your database engine in the Object Explorer and click Properties.

In the Server Properties window, click Security in the left-hand list and tick the SQL Server and Windows Authentication Mode option, then click OK.

Right-click on your database engine in the Object Explorer and click Restart.

To enable the default sa (administrator) SQL Server login:

In SQL Server Management Studio, in the Object Explorer, expand Security > Logins and double-click sa.

On the General page, choose a password for the sa account (untick Enforce password policy if you do not want to enforce a policy).

On the Status page, under Settings > Login, tick Enabled, then click OK.

You can now use the sa account in a connection URL and when you log in to SQL Server Management Studio.

Note: The sa user has extensive permissions. You can also create your own login with fewer permissions.

---

## SQLite database connector | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/overview/databases/sqlite

**Contents**:
- SQLite
- Example​
- Using the better-sqlite3 driver​
  - 1. Install the dependencies​
  - 2. Instantiate Prisma Client using the driver adapter​
  - 3. Configure timestamp format for backward compatibility​
- Type mapping between SQLite to Prisma schema​
  - Native type mapping from Prisma ORM to SQLite​

The SQLite data source connector connects Prisma ORM to a SQLite database file. These files always have the file ending .db (e.g.: dev.db).

By default, the SQLite connector contains a database driver responsible for connecting to your database. You can use a driver adapter (Preview) to connect to your database using a JavaScript database driver from Prisma Client.

To connect to a SQLite database file, you need to configure a datasource block in your Prisma schema:

The fields passed to the datasource block are:

As of v5.4.0, you can use Prisma ORM with database drivers from the JavaScript ecosystem (instead of using Prisma ORM's built-in drivers). You can do this by using a driver adapter.

For SQLite, better-sqlite3 is one of the most popular drivers in the JavaScript ecosystem.

This section explains how you can use it with Prisma ORM and the @prisma/adapter-better-sqlite3 driver adapter.

First, install Prisma ORM's driver adapter for better-sqlite3:

Now, when you instantiate Prisma Client, you need to pass an instance of Prisma ORM's driver adapter to the PrismaClient constructor:

When using driver adapters with SQLite, you can configure how DateTime values are stored in the database using the timestampFormat option.

By default, driver adapters store DateTime values as ISO 8601 strings, which is the most convenient format for SQLite since SQLite date/time functions expect ISO 8601 by default.

However, if you need 100% backward compatibility with Prisma ORM's native SQLite driver (for example, when migrating an existing database), you should use the unixepoch-ms format, which stores timestamps as the number of milliseconds since the Unix epoch:

The timestampFormat option is available for both @prisma/adapter-better-sqlite3 and @prisma/adapter-libsql driver adapters.

When to use each format:

The SQLite connector maps the scalar types from the data model to native column types as follows:

Alternatively, see Prisma schema reference for type mappings organ

*[Content truncated - see full docs]*

**Examples**:

```prisma
datasource db {  provider = "sqlite"  url      = "file:./dev.db"}
```

```terminal
npm install @prisma/adapter-better-sqlite3
```

```ts
import { PrismaBetterSQLite3 } from '@prisma/adapter-better-sqlite3';import { PrismaClient } from './generated/prisma';const adapter = new PrismaBetterSQLite3({  url: "file:./prisma/dev.db"});const prisma = new PrismaClient({ adapter });
```

---

## Set up PostgreSQL on Neon with Prisma Accelerate's Connection Pool | Prisma Documentation

**URL**: https://www.prisma.io/docs/guides/neon-accelerate

**Contents**:
- Set up Neon with Accelerate Connection Pool
- Introduction​
- Prerequisites​
- 1. Set up Prisma ORM​
- 2. Introspect your database​
- 3. Install the Accelerate extension​
- 4. Set up Accelerate in the Prisma Console​
- 5. Generate Prisma Client​

This guides teaches you how to add connection pooling to a PostgreSQL database hosted on Neon using Prisma Accelerate.

Prisma Accelerate is a robust and mature connection pooler enabling your database to function properly during traffic spikes and high load scenarios. Check out this video demonstrating how it performs in a load test or learn why connection pooling is important.

To successfully complete this guide, you need a connection string for a PostgreSQL instance hosted on Neon. It typically looks similar to this:

If you already have a project using Prisma ORM, you can skip the first two steps and jump ahead to Step 3. Install the Accelerate extension.

Start by installing the Prisma CLI in your project:

Then, run the following command to initialize a new project:

This will create a new prisma directory with a schema.prisma file and add a .env file with the DATABASE_URL environment variable.

Update the file and set the DATABASE_URL to your Neon connection string:

Next, run the following command to introspect your database and create your data model:

This command reads your database schema and creates new models in your schema.prisma file that match the tables in your database.

If you want to use Prisma Migrate in the future, you also need to baseline your database.

Install the Prisma Client extension for Accelerate:

This is needed to access Prisma Accelerate's connection pool.

To set up Accelerate in the Prisma Console, follow these steps:

Once you went through these steps, you'll be redirected to another page where you need to the click the Generate API key button.

You'll then be shown a new connection URL which enables you to connect to Prisma Accelerate's connection pool. This needs to be set as the new DATABASE_URL in your .env file:

If you want to use Prisma Migrate with Prisma Accelerate, you can set the directUrl field on the datasource block:

Accordingly, you'll need to set the DIRECT_URL in your .env file:

With your Prisma schema in pl

*[Content truncated - see full docs]*

**Examples**:

```bash
postgresql://neondb_owner:[YOUR-PASSWORD]@ep-lingering-hat-a2e7tkt3.eu-central-1.aws.neon.tech/neondb?sslmode=require
```

```text
npm install prisma --save-dev
```

```text
npx prisma init
```

---

## Workflows | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-migrate/workflows

**Contents**:
- Workflows
- In this section​
- Seeding
- Prototyping your schema
- Baselining a database
- Customizing migrations
- Data migrations
- Squashing migrations

This guide describes how to seed your database using Prisma Client and Prisma ORM's integrated seeding functionality. Seeding allows you to consistently re-create the same data in your database and can be used to:

The Prisma CLI has a dedicated command for prototyping schemas: db push

Baselining is the process of initializing a migration history for a database that:

This guide does not apply for MongoDB.

This guide has been moved to our new guides section. You can find the guide there.

This guide describes how to squash multiple migration files into a single migration.

This guide describes how to generate a down migration SQL file that reverses a given migration file.

Patching or hotfixing a database involves making an often time critical change directly in production. For example, you might add an index directly to a production database to resolve an issue with a slow-running query.

Prisma Migrate uses the Prisma schema to determine what features to create in the database. However, some database features cannot be represented in the Prisma schema , including but not limited to:

This page explains how to use Prisma Migrate commands in development and production environments.

This guide has been moved to the guides section. You can find the guide there.

Prisma Migrate translates the model defined in your Prisma schema into features in your database.

In PostgreSQL, some native database functions are part of optional extensions. For example, in PostgreSQL versions 12.13 and earlier the genrandomuuid() function is part of the pgcrypto extension.

This guide describes how to resolve issues with Prisma Migrate in a development environment, which often involves resetting your database. For production-focused troubleshooting, see:

---
