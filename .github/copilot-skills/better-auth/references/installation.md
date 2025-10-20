# Better-Auth - Installation

**Pages**: 2

---

## Better Auth Fastify Integration Guide | Better Auth

**URL**: https://www.better-auth.com/docs/integrations/fastify

**Contents**:
- Better Auth Fastify Integration Guide
  - Prerequisites
  - Authentication Handler Setup
  - Trusted origins
  - Configuring CORS
  - On this page

get started, concepts, and plugins

Search documentation...

This guide provides step-by-step instructions for configuring both essential handlers and CORS settings.

A configured Better Auth instance is required before proceeding. If you haven't set this up yet, please consult our Installation Guide.

Verify the following requirements before integration:

Configure Better Auth to process authentication requests by creating a catch-all route:

When a request is made from a different origin, the request will be blocked by default. You can add trusted origins to the auth instance.

Secure your API endpoints with proper CORS configuration:

**Examples**:

```text
npm install fastify @fastify/cors
```

```text
npm install fastify @fastify/cors
```

```python
import Fastify from "fastify";
import { auth } from "./auth"; // Your configured Better Auth instance

const fastify = Fastify({ logger: true });

// Register authentication endpoint
fastify.route({
  method: ["GET", "POST"],
  url: "/api/auth/*",
  async handler(request, reply) {
    try {
      // Construct request URL
      const url = new URL(request.url, `http://${request.headers.host}`);
      
      // Convert Fastify headers to standard Headers object
      const headers = new Headers();
...
```

---

## Installation | Better Auth

**URL**: https://www.better-auth.com/docs/installation

**Contents**:
- Installation
  - Install the Package
  - Set Environment Variables
  - Create A Better Auth Instance
  - Configure Database
  - Create Database Tables
  - Authentication Methods
  - Mount Handler

get started, concepts, and plugins

Search documentation...

Let's start by adding Better Auth to your project:

If you're using a separate client and server setup, make sure to install Better Auth in both parts of your project.

Create a .env file in the root of your project and add the following environment variables:

Random value used by the library for encryption and generating hashes. You can generate one using the button below or you can use something like openssl.

Create a file named auth.ts in one of these locations:

You can also nest any of these folders under src/, app/ or server/ folder. (e.g. src/lib/auth.ts, app/lib/auth.ts).

And in this file, import Better Auth and create your auth instance. Make sure to export the auth instance with the variable name auth or as a default export.

Better Auth requires a database to store user data. You can easily configure Better Auth to use SQLite, PostgreSQL, or MySQL, and more!

Alternatively, if you prefer to use an ORM, you can use one of the built-in adapters.

If your database is not listed above, check out our other supported databases for more information, or use one of the supported ORMs.

Better Auth includes a CLI tool to help manage the schema required by the library.

If you're using Kysely, you can apply the migration directly with migrate command below. Use generate only if you plan to apply the migration manually.

see the CLI documentation for more information.

If you instead want to create the schema manually, you can find the core schema required in the database section.

Configure the authentication methods you want to use. Better Auth comes with built-in support for email/password, and social sign-on providers.

You can use even more authentication methods like passkey, username, magic link and more through plugins.

To handle API requests, you need to set up a route handler on your server.

Create a new file or route in your framework's designated catch-all route handler. This route should h

*[Content truncated - see full docs]*

**Examples**:

```text
npm install better-auth
```

```text
npm install better-auth
```

```text
BETTER_AUTH_SECRET=
```

---
