# Better-Auth - Guides

**Pages**: 6

---

## Browser Extension Guide | Better Auth

**URL**: https://www.better-auth.com/docs/guides/browser-extension-guide

**Contents**:
- Browser Extension Guide
- Setup & Installations
- Configure tsconfig
- Create the client auth instance
- Configure the manifest
- You're now ready!
- Bundle your extension
- Configure the server auth instance

get started, concepts, and plugins

Search documentation...

In this guide, we'll walk you through the steps of creating a browser extension using Plasmo with Better Auth for authentication.

If you would like to view a completed example, you can check out the browser extension example.

The Plasmo framework does not provide a backend for the browser extension. This guide assumes you have a backend setup of Better Auth and are ready to create a browser extension to connect to it.

Initialize a new Plasmo project with TailwindCSS and a src directory.

Then, install the Better Auth package.

To start the Plasmo development server, run the following command.

Configure the tsconfig.json file to include strict mode.

For this demo, we have also changed the import alias from ~ to @ and set it to the src directory.

Create a new file at src/auth/auth-client.ts and add the following code.

We must ensure the extension knows the URL to the Better Auth backend.

Head to your package.json file, and add the following code.

You have now set up Better Auth for your browser extension.

Add your desired UI and create your dream extension!

To learn more about the client Better Auth API, check out the client documentation.

Here's a quick example 😎

To get a production build, run the following command.

Head over to chrome://extensions and enable developer mode.

Click on "Load Unpacked" and navigate to your extension's build/chrome-mv3-dev (or build/chrome-mv3-prod) directory.

To see your popup, click on the puzzle piece icon on the Chrome toolbar, and click on your extension.

Learn more about bundling your extension here.

First, we will need your extension URL.

An extension URL formed like this: chrome-extension://YOUR_EXTENSION_ID.

You can find your extension ID at chrome://extensions.

Head to your server's auth file, and make sure that your extension's URL is added to the trustedOrigins list.

If you're developing multiple extensions or need to support different browser 

*[Content truncated - see full docs]*

**Examples**:

```text
pnpm create plasmo --with-tailwindcss --with-src
```

```text
pnpm create plasmo --with-tailwindcss --with-src
```

```text
pnpm add better-auth
```

---

## Create your first plugin | Better Auth

**URL**: https://www.better-auth.com/docs/guides/your-first-plugin

**Contents**:
- Create your first plugin
- Plan your idea
- Server plugin first
  - Creating the server plugin
  - Defining a schema
  - Authorization logic
- Client Plugin
- Initiate your plugin!

get started, concepts, and plugins

Search documentation...

In this guide, we’ll walk you through the steps of creating your first Better Auth plugin.

This guide assumes you have setup the basics of Better Auth and are ready to create your first plugin.

Before beginning, you must know what plugin you intend to create.

In this guide, we’ll create a birthday plugin to keep track of user birth dates.

Better Auth plugins operate as a pair: a server plugin and a client plugin. The server plugin forms the foundation of your authentication system, while the client plugin provides convenient frontend APIs to interact with your server implementation.

You can read more about server/client plugins in our documentation.

Go ahead and find a suitable location to create your birthday plugin folder, with an index.ts file within.

In the index.ts file, we’ll export a function that represents our server plugin. This will be what we will later add to our plugin list in the auth.ts file.

Although this does nothing, you have technically just made yourself your first plugin, congratulations! 🎉

In order to save each user’s birthday data, we must create a schema on top of the user model.

By creating a schema here, this also allows Better Auth’s CLI to generate the schemas required to update your database.

You can learn more about plugin schemas here.

For this example guide, we’ll set up authentication logic to check and ensure that the user who signs-up is older than 5. But the same concept could be applied for something like verifying users agreeing to the TOS or anything alike.

To do this, we’ll utilize Hooks, which allows us to run code before or after an action is performed.

In our case we want to match any requests going to the signup path:

And for our logic, we’ll write the following code to check the if user’s birthday makes them above 5 years old.

We’ve now successfully written code to ensure authorization for users above 5!

We’re close to the finish line! 🏁

Now t

*[Content truncated - see full docs]*

**Examples**:

```python
import { createAuthClient } from "better-auth/client";
import type { BetterAuthPlugin } from "better-auth";

export const birthdayPlugin = () =>
  ({
    id: "birthdayPlugin",
  } satisfies BetterAuthPlugin);
```

```python
import { createAuthClient } from "better-auth/client";
import type { BetterAuthPlugin } from "better-auth";

export const birthdayPlugin = () =>
  ({
    id: "birthdayPlugin",
  } satisfies BetterAuthPlugin);
```

```javascript
//...
export const birthdayPlugin = () =>
  ({
    id: "birthdayPlugin",
    schema: {
      user: {
        fields: {
          birthday: {
            type: "date", // string, number, boolean, date
            required: true, // if the field should be required on a new record. (default: false)
            unique: false, // if the field should be unique. (default: false)
            references: null // if the field is a reference to another table. (default: null)
          },
        },
      }
...
```

---

## Migrating from Auth0 to Better Auth | Better Auth

**URL**: https://www.better-auth.com/docs/guides/auth0-migration-guide

**Contents**:
- Migrating from Auth0 to Better Auth
- Before You Begin
  - Connect to your database
  - Enable Email and Password (Optional)
  - Setup Social Providers (Optional)
  - Add Plugins (Optional)
  - Generate Schema
  - Install Dependencies

get started, concepts, and plugins

Search documentation...

In this guide, we'll walk through the steps to migrate a project from Auth0 to Better Auth — including email/password with proper hashing, social/external accounts, two-factor authentication, and more.

This migration will invalidate all active sessions. This guide doesn't currently show you how to migrate Organizations but it should be possible with additional steps and the Organization Plugin.

Before starting the migration process, set up Better Auth in your project. Follow the installation guide to get started.

You'll need to connect to your database to migrate the users and accounts. You can use any database you want, but for this example, we'll use PostgreSQL.

And then you can use the following code to connect to your database.

Enable the email and password in your auth config and implement your own logic for sending verification emails, reset password emails, etc.

See Email and Password for more configuration options.

Add social providers you have enabled in your Auth0 project in your auth config.

You can add the following plugins to your auth config based on your needs.

Admin Plugin will allow you to manage users, user impersonations and app level roles and permissions.

Two Factor Plugin will allow you to add two-factor authentication to your application.

Username Plugin will allow you to add username authentication to your application.

If you're using a custom database adapter, generate the schema:

or if you're using the default adapter, you can use the following command:

Install the required dependencies for the migration:

Create a new file called migrate-auth0.ts in the scripts folder and add the following code:

Instead of using the Management API, you can use Auth0's bulk user export functionality and pass the exported JSON data directly to the auth0Users array. This is especially useful if you need to migrate password hashes and complete user data, which are not available through

*[Content truncated - see full docs]*

**Examples**:

```text
npm install pg
```

```text
npm install pg
```

```python
import { Pool } from "pg";

export const auth = betterAuth({
    database: new Pool({ 
        connectionString: process.env.DATABASE_URL 
    }),
})
```

---

## Migrating from Clerk to Better Auth | Better Auth

**URL**: https://www.better-auth.com/docs/guides/clerk-migration-guide

**Contents**:
- Migrating from Clerk to Better Auth
- Before You Begin
  - Connect to your database
  - Enable Email and Password (Optional)
  - Setup Social Providers (Optional)
  - Add Plugins (Optional)
  - Generate Schema
  - Export Clerk Users

get started, concepts, and plugins

Search documentation...

In this guide, we'll walk through the steps to migrate a project from Clerk to Better Auth — including email/password with proper hashing, social/external accounts, phone number, two-factor data, and more.

This migration will invalidate all active sessions. This guide doesn't currently show you how to migrate Organization but it should be possible with additional steps and the Organization Plugin.

Before starting the migration process, set up Better Auth in your project. Follow the installation guide to get started. And go to

You'll need to connect to your database to migrate the users and accounts. You can use any database you want, but for this example, we'll use PostgreSQL.

And then you can use the following code to connect to your database.

Enable the email and password in your auth config and implement your own logic for sending verification emails, reset password emails, etc.

See Email and Password for more configuration options.

Add social providers you have enabled in your Clerk project in your auth config.

You can add the following plugins to your auth config based on your needs.

Admin Plugin will allow you to manage users, user impersonations and app level roles and permissions.

Two Factor Plugin will allow you to add two-factor authentication to your application.

Phone Number Plugin will allow you to add phone number authentication to your application.

Username Plugin will allow you to add username authentication to your application.

If you're using a custom database adapter, generate the schema:

or if you're using the default adapter, you can use the following command:

Go to the Clerk dashboard and export the users. Check how to do it here. It will download a CSV file with the users data. You need to save it as exported_users.csv and put it in the root of your project.

Create a new file called migrate-clerk.ts in the scripts folder and add the following code:

Make sure to repla

*[Content truncated - see full docs]*

**Examples**:

```text
npm install pg
```

```text
npm install pg
```

```python
import { Pool } from "pg";

export const auth = betterAuth({
    database: new Pool({ 
        connectionString: process.env.DATABASE_URL 
    }),
})
```

---

## Migrating from NextAuth.js to Better Auth | Better Auth

**URL**: https://www.better-auth.com/docs/guides/next-auth-migration-guide

**Contents**:
- Migrating from NextAuth.js to Better Auth
- Before You Begin
  - Mapping Existing Columns
    - User Schema
    - Session Schema
    - Account Schema
  - Update the Route Handler
  - Update the Client

get started, concepts, and plugins

Search documentation...

In this guide, we’ll walk through the steps to migrate a project from NextAuth.js to Better Auth, ensuring no loss of data or functionality. While this guide focuses on Next.js, it can be adapted for other frameworks as well.

Before starting the migration process, set up Better Auth in your project. Follow the installation guide to get started.

Instead of altering your existing database column names, you can map them to match Better Auth's expected structure. This allows you to retain your current database schema.

Map the following fields in the user schema:

Map the following fields in the session schema:

Make sure to have createdAt and updatedAt fields on your session schema.

Map these fields in the account schema:

Remove the session_state, type, and token_type fields, as they are not required by Better Auth.

Note: If you use ORM adapters, you can map these fields in your schema file.

Make sure to have createdAt and updatedAt fields on your account schema.

In the app/api/auth folder, rename the [...nextauth] file to [...all] to avoid confusion. Then, update the route.ts file as follows:

Create a file named auth-client.ts in the lib folder. Add the following code:

Update your social login functions to use Better Auth. For example, for Discord:

Replace useSession calls with Better Auth’s version. Example:

Use the auth instance to get session data on the server:

To protect routes with middleware, refer to the Next.js middleware guide.

Congratulations! You’ve successfully migrated from NextAuth.js to Better Auth. For a complete implementation with multiple authentication methods, check out the demo repository.

Better Auth offers greater flexibility and more features—be sure to explore the documentation to unlock its full potential.

Supabase Migration Guide

**Examples**:

```javascript
export const auth = betterAuth({
    // Other configs
    session: {
        fields: {
            expiresAt: "expires", // Map your existing `expires` field to Better Auth's `expiresAt`
            token: "sessionToken" // Map your existing `sessionToken` field to Better Auth's `token`
        }
    },
});
```

```javascript
export const auth = betterAuth({
    // Other configs
    session: {
        fields: {
            expiresAt: "expires", // Map your existing `expires` field to Better Auth's `expiresAt`
            token: "sessionToken" // Map your existing `sessionToken` field to Better Auth's `token`
        }
    },
});
```

```javascript
export const auth = betterAuth({
    // Other configs
    account: {
        fields: {
            accountId: "providerAccountId",
            refreshToken: "refresh_token",
            accessToken: "access_token",
            accessTokenExpiresAt: "access_token_expires",
            idToken: "id_token",
        }
    },
});
```

---

## Optimizing for Performance | Better Auth

**URL**: https://www.better-auth.com/docs/guides/optimizing-for-performance

**Contents**:
- Optimizing for Performance
- Caching
  - Cookie Cache
  - Framework Caching
- SSR Optimizations
- Database optimizations
    - Recommended fields to index
  - On this page

get started, concepts, and plugins

Search documentation...

In this guide, we’ll go over some of the ways you can optimize your application for a more performant Better Auth app.

Caching is a powerful technique that can significantly improve the performance of your Better Auth application by reducing the number of database queries and speeding up response times.

Calling your database every time useSession or getSession is invoked isn’t ideal, especially if sessions don’t change frequently. Cookie caching handles this by storing session data in a short-lived, signed cookie similar to how JWT access tokens are used with refresh tokens.

To turn on cookie caching, just set session.cookieCache in your auth config:

Read more about cookie caching.

Here are examples of how you can do caching in different frameworks and environments:

Since Next v15, we can use the "use cache" directive to cache the response of a server function.

Learn more about NextJS use cache directive here.

In Remix, you can use the cache option in the loader function to cache responses on the server. Here’s an example:

You can read a nice guide on Loader vs Route Cache Headers in Remix here.

In SolidStart, you can use the query function to cache data. Here’s an example:

Learn more about SolidStart query function here.

With React Query you can use the useQuery hook to cache data. Here’s an example:

Learn more about React Query use cache directive here.

If you're using a framework that supports server-side rendering, it's usually best to pre-fetch the user session on the server and use it as a fallback on the client.

Optimizing database performance is essential to get the best out of Better Auth.

We intend to add indexing support in our schema generation tool in the future.

**Examples**:

```python
import { betterAuth } from "better-auth";

export const auth = betterAuth({
  session: {
    cookieCache: {
      enabled: true,
      maxAge: 5 * 60, // Cache duration in seconds
    },
  },
});
```

```python
import { betterAuth } from "better-auth";

export const auth = betterAuth({
  session: {
    cookieCache: {
      enabled: true,
      maxAge: 5 * 60, // Cache duration in seconds
    },
  },
});
```

```javascript
export async function getUsers() {
    'use cache'
    const { users } = await auth.api.listUsers();
    return users
}
```

---
