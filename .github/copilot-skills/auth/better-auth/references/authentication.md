# Better-Auth - Authentication

**Pages**: 64

---

## API | Better Auth

**URL**: https://www.better-auth.com/docs/concepts/api

**Contents**:
- API
- Calling API Endpoints on the Server
  - Body, Headers, Query
  - Getting headers and Response Object
    - Getting headers
    - Getting Response Object
  - Error Handling
  - On this page

get started, concepts, and plugins

Search documentation...

When you create a new Better Auth instance, it provides you with an api object. This object exposes every endpoint that exists in your Better Auth instance. And you can use this to interact with Better Auth server side.

Any endpoint added to Better Auth, whether from plugins or the core, will be accessible through the api object.

To call an API endpoint on the server, import your auth instance and call the endpoint using the api object.

Unlike the client, the server needs the values to be passed as an object with the key body for the body, headers for the headers, and query for query parameters.

Better Auth API endpoints are built on top of better-call, a tiny web framework that lets you call REST API endpoints as if they were regular functions and allows us to easily infer client types from the server.

When you invoke an API endpoint on the server, it will return a standard JavaScript object or array directly as it's just a regular function call.

But there are times when you might want to get the headers or the Response object instead. For example, if you need to get the cookies or the headers.

To get the headers, you can pass the returnHeaders option to the endpoint.

The headers will be a Headers object, which you can use to get the cookies or the headers.

To get the Response object, you can pass the asResponse option to the endpoint.

When you call an API endpoint on the server, it will throw an error if the request fails. You can catch the error and handle it as you see fit. The error instance is an instance of APIError.

**Examples**:

```python
import { betterAuth } from "better-auth";
import { headers } from "next/headers";

export const auth = betterAuth({
    //...
})

// calling get session on the server
await auth.api.getSession({
    headers: await headers() // some endpoints might require headers
})
```

```python
import { betterAuth } from "better-auth";
import { headers } from "next/headers";

export const auth = betterAuth({
    //...
})

// calling get session on the server
await auth.api.getSession({
    headers: await headers() // some endpoints might require headers
})
```

```text
await auth.api.getSession({
    headers: await headers()
})

await auth.api.signInEmail({
    body: {
        email: "[email protected]",
        password: "password"
    },
    headers: await headers() // optional but would be useful to get the user IP, user agent, etc.
})

await auth.api.verifyEmail({
    query: {
        token: "my_token"
    }
})
```

---

## Admin | Better Auth

**URL**: https://www.better-auth.com/docs/plugins/admin

**Contents**:
- Admin
- Installation
  - Add the plugin to your auth config
  - Migrate the database
  - Add the client plugin
- Usage
  - Create User
  - List Users

get started, concepts, and plugins

Search documentation...

The Admin plugin provides a set of administrative functions for user management in your application. It allows administrators to perform various operations such as creating users, managing user roles, banning/unbanning users, impersonating users, and more.

To use the Admin plugin, add it to your auth config.

Run the migration or generate the schema to add the necessary fields and tables to the database.

See the Schema section to add the fields manually.

Next, include the admin client plugin in your authentication client instance.

Before performing any admin operations, the user must be authenticated with an admin account. An admin is any user assigned the admin role or any user whose ID is included in the adminUserIds option.

Allows an admin to create a new user.

Allows an admin to list all users in the database.

All properties are optional to configure. By default, 100 rows are returned, you can configure this by the limit property.

All properties are optional to configure. By default, 100 rows are returned, you can configure this by the limit property.

The listUsers function supports various filter operators including eq, contains, starts_with, and ends_with.

The listUsers function supports pagination by returning metadata alongside the user list. The response includes the following fields:

To paginate results, use the total, limit, and offset values to calculate:

Fetching the second page with 10 users per page:

Changes the role of a user.

Changes the password of a user.

Update a user's details.

Bans a user, preventing them from signing in and revokes all of their existing sessions.

Removes the ban from a user, allowing them to sign in again.

Lists all sessions for a user.

Revokes a specific session for a user.

Revokes all sessions for a user.

This feature allows an admin to create a session that mimics the specified user. The session will remain active until either the browser sess

*[Content truncated - see full docs]*

**Examples**:

```python
import { betterAuth } from "better-auth"
import { admin } from "better-auth/plugins"

export const auth = betterAuth({
    // ... other config options
    plugins: [
        admin() 
    ]
})
```

```python
import { betterAuth } from "better-auth"
import { admin } from "better-auth/plugins"

export const auth = betterAuth({
    // ... other config options
    plugins: [
        admin() 
    ]
})
```

```text
npx @better-auth/cli migrate
```

---

## Astro Integration | Better Auth

**URL**: https://www.better-auth.com/docs/integrations/astro

**Contents**:
- Astro Integration
  - Mount the handler
- Create a client
- Auth Middleware
  - Astro Locals types
  - Middleware
  - Getting session on the server inside .astro file
  - On this page

get started, concepts, and plugins

Search documentation...

Better Auth comes with first class support for Astro. This guide will show you how to integrate Better Auth with Astro.

Before you start, make sure you have a Better Auth instance configured. If you haven't done that yet, check out the installation.

To enable Better Auth to handle requests, we need to mount the handler to a catch all API route. Create a file inside /pages/api/auth called [...all].ts and add the following code:

You can change the path on your better-auth configuration but it's recommended to keep it as /api/auth/[...all]

Astro supports multiple frontend frameworks, so you can easily import your client based on the framework you're using.

If you're not using a frontend framework, you can still import the vanilla client.

To have types for your Astro locals, you need to set it inside the env.d.ts file.

To protect your routes, you can check if the user is authenticated using the getSession method in middleware and set the user and session data using the Astro locals with the types we set before. Start by creating a middleware.ts file in the root of your project and follow the example below:

You can use Astro.locals to check if the user has session and get the user data from the server side. Here is an example of how you can get the session inside an .astro file:

**Examples**:

```python
import { auth } from "~/auth";
import type { APIRoute } from "astro";

export const ALL: APIRoute = async (ctx) => {
	// If you want to use rate limiting, make sure to set the 'x-forwarded-for' header to the request headers from the context
	// ctx.request.headers.set("x-forwarded-for", ctx.clientAddress);
	return auth.handler(ctx.request);
};
```

```python
import { auth } from "~/auth";
import type { APIRoute } from "astro";

export const ALL: APIRoute = async (ctx) => {
	// If you want to use rate limiting, make sure to set the 'x-forwarded-for' header to the request headers from the context
	// ctx.request.headers.set("x-forwarded-for", ctx.clientAddress);
	return auth.handler(ctx.request);
};
```

```python
import { createAuthClient } from "better-auth/client"
export const authClient =  createAuthClient()
```

---

## Autumn Billing | Better Auth

**URL**: https://www.better-auth.com/docs/plugins/autumn

**Contents**:
- Autumn Billing
  - Get help on Autumn's Discord
- Features
  - Setup Autumn Account
  - Install Autumn SDK
  - Add AUTUMN_SECRET_KEY to your environment variables
  - Add the Autumn plugin to your auth config
  - Add <AutumnProvider />

get started, concepts, and plugins

Search documentation...

Autumn is open source infrastructure to run SaaS pricing plans. It sits between your app and Stripe, and acts as the database for your customers' subscription status, usage metering and feature permissions.

We're online to help you with any questions you have.

First, create your pricing plans in Autumn's dashboard, where you define what each plan and product gets access to and how it should be billed. In this example, we're handling the free and pro plans for an AI chatbot, which comes with a number of messages per month.

If you're using a separate client and server setup, make sure to install the plugin in both parts of your project.

You can find it in Autumn's dashboard under "Developer".

Autumn will auto-create your customers when they sign up, and assign them any default plans you created (eg your Free plan). You can choose who becomes a customer: individual users, organizations, both, or something custom like workspaces.

Client side, wrap your application with the AutumnProvider component, and pass in the baseUrl that you define within better-auth's authClient.

Call attach to redirect the customer to a Stripe checkout page when they want to purchase the Pro plan.

If their payment method is already on file, AttachDialog will open instead to let the customer confirm their new subscription or purchase, and handle the payment.

Make sure you've pasted in your Stripe test secret key in the Autumn dashboard.

The AttachDialog component can be used directly from the autumn-js/react library (as shown in the example above), or downloaded as a shadcn/ui component to customize.

Integrate your client and server pricing tiers logic with the following functions:

Server-side, you can access Autumn's functions through the auth object.

Opens a billing portal where the customer can update their payment method or cancel their plan.

Cancel a product or subscription.

Pass in an expand param into useCustomer t

*[Content truncated - see full docs]*

**Examples**:

```text
npm install autumn-js
```

```text
npm install autumn-js
```

```text
AUTUMN_SECRET_KEY=am_sk_xxxxxxxxxx
```

---

## Basic Usage | Better Auth

**URL**: https://www.better-auth.com/docs/basic-usage

**Contents**:
- Basic Usage
- Email & Password
  - Sign Up
  - Sign In
  - Server-Side Authentication
- Social Sign-On
  - Sign in with social providers
- Signout

get started, concepts, and plugins

Search documentation...

Better Auth provides built-in authentication support for:

But also can easily be extended using plugins, such as: username, magic link, passkey, email-otp, and more.

To enable email and password authentication:

To sign up a user you need to call the client method signUp.email with the user's information.

By default, the users are automatically signed in after they successfully sign up. To disable this behavior you can set autoSignIn to false.

To sign a user in, you can use the signIn.email function provided by the client.

Always invoke client methods from the client side. Don't call them from the server.

To authenticate a user on the server, you can use the auth.api methods.

If the server cannot return a response object, you'll need to manually parse and set cookies. But for frameworks like Next.js we provide a plugin to handle this automatically

Better Auth supports multiple social providers, including Google, GitHub, Apple, Discord, and more. To use a social provider, you need to configure the ones you need in the socialProviders option on your auth object.

To sign in using a social provider you need to call signIn.social. It takes an object with the following properties:

You can also authenticate using idToken or accessToken from the social provider instead of redirecting the user to the provider's site. See social providers documentation for more details.

To signout a user, you can use the signOut function provided by the client.

you can pass fetchOptions to redirect onSuccess

Once a user is signed in, you'll want to access the user session. Better Auth allows you to easily access the session data from both the server and client sides.

Better Auth provides a useSession hook to easily access session data on the client side. This hook is implemented using nanostore and has support for each supported framework and vanilla client, ensuring that any changes to the session (such as signing out

*[Content truncated - see full docs]*

**Examples**:

```python
import { betterAuth } from "better-auth"

export const auth = betterAuth({
    emailAndPassword: {    
        enabled: true
    } 
})
```

```python
import { betterAuth } from "better-auth"

export const auth = betterAuth({
    emailAndPassword: {    
        enabled: true
    } 
})
```

```python
import { authClient } from "@/lib/auth-client"; //import the auth client

const { data, error } = await authClient.signUp.email({
        email, // user email address
        password, // user password -> min 8 characters by default
        name, // user display name
        image, // User image URL (optional)
        callbackURL: "/dashboard" // A URL to redirect to after the user verifies their email (optional)
    }, {
        onRequest: (ctx) => {
            //show loading
        },
      
...
```

---

## Bearer Token Authentication | Better Auth

**URL**: https://www.better-auth.com/docs/plugins/bearer

**Contents**:
- Bearer Token Authentication
- Installing the Bearer Plugin
- How to Use Bearer Tokens
  - 1. Obtain the Bearer Token
  - 2. Configure the Auth Client
  - 3. Make Authenticated Requests
  - 4. Per-Request Token (Optional)
  - 5. Using Bearer Tokens Outside the Auth Client

get started, concepts, and plugins

Search documentation...

The Bearer plugin enables authentication using Bearer tokens as an alternative to browser cookies. It intercepts requests, adding the Bearer token to the Authorization header before forwarding them to your API.

Use this cautiously; it is intended only for APIs that don't support cookies or require Bearer tokens for authentication. Improper implementation could easily lead to security vulnerabilities.

Add the Bearer plugin to your authentication setup:

After a successful sign-in, you'll receive a session token in the response headers. Store this token securely (e.g., in localStorage):

You can also set this up globally in your auth client:

You may want to clear the token based on the response status code or other conditions:

Set up your auth client to include the Bearer token in all requests:

Now you can make authenticated API calls:

You can also provide the token for individual requests:

The Bearer token can be used to authenticate any request to your API, even when not using the auth client:

And in the server, you can use the auth.api.getSession function to authenticate requests:

requireSignature (boolean): Require the token to be signed. Default: false.

**Examples**:

```python
import { betterAuth } from "better-auth";
import { bearer } from "better-auth/plugins";

export const auth = betterAuth({
    plugins: [bearer()]
});
```

```python
import { betterAuth } from "better-auth";
import { bearer } from "better-auth/plugins";

export const auth = betterAuth({
    plugins: [bearer()]
});
```

```javascript
const { data } = await authClient.signIn.email({
    email: "[email protected]",
    password: "securepassword"
}, {
  onSuccess: (ctx)=>{
    const authToken = ctx.response.headers.get("set-auth-token") // get the token from the response headers
    // Store the token securely (e.g., in localStorage)
    localStorage.setItem("bearer_token", authToken);
  }
});
```

---

## CLI | Better Auth

**URL**: https://www.better-auth.com/docs/concepts/cli

**Contents**:
- CLI
- Generate
  - Options
- Migrate
  - Options
- Init
  - Options
- Info

get started, concepts, and plugins

Search documentation...

Better Auth comes with a built-in CLI to help you manage the database schemas, initialize your project, generate a secret key for your application, and gather diagnostic information about your setup.

The generate command creates the schema required by Better Auth. If you're using a database adapter like Prisma or Drizzle, this command will generate the right schema for your ORM. If you're using the built-in Kysely adapter, it will generate an SQL file you can run directly on your database.

The migrate command applies the Better Auth schema directly to your database. This is available if you're using the built-in Kysely adapter. For other adapters, you'll need to apply the schema using your ORM's migration tool.

The init command allows you to initialize Better Auth in your project.

The info command provides diagnostic information about your Better Auth setup and environment. Useful for debugging and sharing when seeking support.

The command displays:

Sensitive data like secrets, API keys, and database URLs are automatically replaced with [REDACTED] for safe sharing.

The CLI also provides a way to generate a secret key for your Better Auth instance.

Error: Cannot find module X

If you see this error, it means the CLI can't resolve imported modules in your Better Auth config file. We are working on a fix for many of these issues, but in the meantime, you can try the following:

**Examples**:

```text
npx @better-auth/cli@latest generate
```

```text
npx @better-auth/cli@latest generate
```

```text
npx @better-auth/cli@latest migrate
```

---

## Captcha | Better Auth

**URL**: https://www.better-auth.com/docs/plugins/captcha

**Contents**:
- Captcha
- Installation
  - Add the plugin to your auth config
  - Add the captcha token to your request headers
- How it works
- Plugin Options
  - On this page

get started, concepts, and plugins

Search documentation...

The Captcha Plugin integrates bot protection into your Better Auth system by adding captcha verification for key endpoints. This plugin ensures that only human users can perform actions like signing up, signing in, or resetting passwords. The following providers are currently supported:

This plugin works out of the box with Email & Password authentication. To use it with other authentication methods, you will need to configure the endpoints array in the plugin options.

Add the captcha token to your request headers for all protected endpoints. This example shows how to include it in a signIn request:

The plugin acts as a middleware: it intercepts all POST requests to configured endpoints (see endpoints in the Plugin Options section).

it validates the captcha token on the server, by calling the captcha provider's /siteverify.

**Examples**:

```python
import { betterAuth } from "better-auth";
import { captcha } from "better-auth/plugins";

export const auth = betterAuth({
    plugins: [ 
        captcha({ 
            provider: "cloudflare-turnstile", // or google-recaptcha, hcaptcha, captchafox
            secretKey: process.env.TURNSTILE_SECRET_KEY!, 
        }), 
    ], 
});
```

```python
import { betterAuth } from "better-auth";
import { captcha } from "better-auth/plugins";

export const auth = betterAuth({
    plugins: [ 
        captcha({ 
            provider: "cloudflare-turnstile", // or google-recaptcha, hcaptcha, captchafox
            secretKey: process.env.TURNSTILE_SECRET_KEY!, 
        }), 
    ], 
});
```

```text
await authClient.signIn.email({
    email: "[email protected]",
    password: "secure-password",
    fetchOptions: { 
        headers: { 
            "x-captcha-response": turnstileToken, 
            "x-captcha-user-remote-ip": userIp, // optional: forwards the user's IP address to the captcha service
        }, 
    }, 
});
```

---

## Client | Better Auth

**URL**: https://www.better-auth.com/docs/concepts/client

**Contents**:
- Client
- Installation
- Create Client Instance
- Usage
  - Hooks
  - Fetch Options
  - Handling Errors
    - Error Codes

get started, concepts, and plugins

Search documentation...

Better Auth offers a client library compatible with popular frontend frameworks like React, Vue, Svelte, and more. This client library includes a set of functions for interacting with the Better Auth server. Each framework's client library is built on top of a core client library that is framework-agnostic, so that all methods and hooks are consistently available across all client libraries.

If you haven't already, install better-auth.

Import createAuthClient from the package for your framework (e.g., "better-auth/react" for React). Call the function to create your client. Pass the base URL of your auth server. If the auth server is running on the same domain as your client, you can skip this step.

If you're using a different base path other than /api/auth, make sure to pass the whole URL, including the path. (e.g., http://localhost:3000/custom-path/auth)

Once you've created your client instance, you can use the client to interact with the Better Auth server. The client provides a set of functions by default and they can be extended with plugins.

In addition to the standard methods, the client provides hooks to easily access different reactive data. Every hook is available in the root object of the client and they all start with use.

The client uses a library called better fetch to make requests to the server.

Better fetch is a wrapper around the native fetch API that provides a more convenient way to make requests. It's created by the same team behind Better Auth and is designed to work seamlessly with it.

You can pass any default fetch options to the client by passing fetchOptions object to the createAuthClient.

You can also pass fetch options to most of the client functions. Either as the second argument or as a property in the object.

Most of the client functions return a response object with the following properties:

The error object contains the following properties:

If the action accepts

*[Content truncated - see full docs]*

**Examples**:

```text
npm i better-auth
```

```text
npm i better-auth
```

```python
import { createAuthClient } from "better-auth/client"
export const authClient = createAuthClient({
    baseURL: "http://localhost:3000" // The base URL of your auth server
})
```

---

## Community Plugins | Better Auth

**URL**: https://www.better-auth.com/docs/plugins/community-plugins

**Contents**:
- Community Plugins
  - On this page

get started, concepts, and plugins

Search documentation...

This page showcases a list of recommended community made plugins.

We encourage you to create custom plugins and maybe get added to the list!

To create your own custom plugin, get started by reading our plugins documentation. And if you want to share your plugin with the community, please open a pull request to add it to this list.

---

## Comparison | Better Auth

**URL**: https://www.better-auth.com/docs/comparison

**Contents**:
- Comparison
  - vs Other Auth Libraries
  - vs Self-Hosted Auth Servers
  - vs Managed Auth Services
  - vs Rolling Your Own
  - On this page

get started, concepts, and plugins

Search documentation...

Comparison is the thief of joy.

Here are non detailed reasons why you may want to use Better Auth over other auth libraries and services.

---

## Contributing to BetterAuth | Better Auth

**URL**: https://www.better-auth.com/docs/reference/contributing

**Contents**:
- Contributing to BetterAuth
- Getting Started
- Development Setup
  - 1. Fork the repository
  - 2. Clone your fork
  - 3. Install dependencies
  - 4. Prepare ENV files
- Making changes

get started, concepts, and plugins

Search documentation...

Thank you for your interest in contributing to Better Auth! This guide is a concise guide to contributing to Better Auth.

Before diving in, here are a few important resources:

To get started with development:

Make sure you have Node.JS installed, preferably on LTS.

Visit https://github.com/better-auth/better-auth

Click the "Fork" button in the top right.

Make sure you have pnpm installed!

Copy the example env file to create your new .env file.

Once you have an idea of what you want to contribute, you can start making changes. Here are some steps to get started:

Start the development server:

To start the docs server:

Make your changes to the codebase.

Write tests if needed. (Read more about testing here)

Update documentation. (Read more about documenting here)

We welcome contributions to support more frameworks:

We use Vitest for testing. Place test files next to the source files they test:

The test instance helper now includes improved async context support for managing user sessions:

Don't hesitate to ask for help! You can:

Thank you for contributing to Better Auth!

**Examples**:

```text
# Replace YOUR-USERNAME with your GitHub username
git clone https://github.com/YOUR-USERNAME/better-auth.git
cd better-auth
```

```text
# Replace YOUR-USERNAME with your GitHub username
git clone https://github.com/YOUR-USERNAME/better-auth.git
cd better-auth
```

```text
pnpm install
```

---

## Convex Integration | Better Auth

**URL**: https://www.better-auth.com/docs/integrations/convex

**Contents**:
- Convex Integration
- Prerequisites
  - Create a Convex project
  - Run convex dev
- Installation of Convex + Better Auth
  - Installation
    - Install packages
    - Register the component

get started, concepts, and plugins

Search documentation...

This documentation comes from the Convex documentation, for more information, please refer to their documentation.

To use Convex + Better Auth, you'll first need a Convex project. If you don't have one, run the following command to get started.

Check out the Convex docs to learn more about Convex.

Running the CLI during setup will initialize your Convex deployment if it doesn't already exist, and keeps generated types current through the process. Keep it running.

The following documentation assumes you're using Next.js.

If you're not using Next.js, please refer to the installation guide by Convex.

For a complete example, check out Convex + Better Auth example with Next.js in this Github repository.

Install the component, a pinned version of Better Auth, and ensure the latest version of Convex.

This component requires Convex 1.25.0 or later.

Register the Better Auth component in your Convex project.

Add a convex/auth.config.ts file to configure Better Auth as an authentication provider.

Generate a secret for encryption and generating hashes. Use the command below if you have openssl installed, or use the button to generate a random value instead. Or generate your own however you like.

Add your site URL to your Convex deployment.

Add environment variables to the .env.local file created by npx convex dev. It will be picked up by your framework dev server.

Create a Better Auth instance and initialize the component.

Create a Better Auth client instance for interacting with the Better Auth server from your client.

Register Better Auth route handlers on your Convex deployment.

Set up route handlers to proxy auth requests from your framework server to your Convex deployment.

Wrap your app with the ConvexBetterAuthProvider component.

You're now ready to start using Better Auth with Convex.

To use Better Auth's server methods in server rendering, server functions, or any other Next.js server code

*[Content truncated - see full docs]*

**Examples**:

```text
npm create convex@latest
```

```text
npm create convex@latest
```

```text
npx convex dev
```

---

## Cookies | Better Auth

**URL**: https://www.better-auth.com/docs/concepts/cookies

**Contents**:
- Cookies
  - Cookie Prefix
  - Custom Cookies
  - Cross Subdomain Cookies
  - Secure Cookies
  - On this page

get started, concepts, and plugins

Search documentation...

Cookies are used to store data such as session tokens, OAuth state, and more. All cookies are signed using the secret key provided in the auth options.

By default, Better Auth cookies follow the format ${prefix}.${cookie_name}. The default prefix is "better-auth". You can change the prefix by setting cookiePrefix in the advanced object of the auth options.

All cookies are httpOnly and secure when the server is running in production mode.

If you want to set custom cookie names and attributes, you can do so by setting cookieOptions in the advanced object of the auth options.

By default, Better Auth uses the following cookies:

Plugins may also use cookies to store data. For example, the Two Factor Authentication plugin uses the two_factor cookie to store the two-factor authentication state.

Sometimes you may need to share cookies across subdomains. For example, if you authenticate on auth.example.com, you may also want to access the same session on app.example.com.

The domain attribute controls which domains can access the cookie. Setting it to your root domain (e.g. example.com) makes the cookie accessible across all subdomains. For security, follow these guidelines:

By default, cookies are secure only when the server is running in production mode. You can force cookies to be always secure by setting useSecureCookies to true in the advanced object in the auth options.

**Examples**:

```python
import { betterAuth } from "better-auth"

export const auth = betterAuth({
    advanced: {
        cookiePrefix: "my-app"
    }
})
```

```python
import { betterAuth } from "better-auth"

export const auth = betterAuth({
    advanced: {
        cookiePrefix: "my-app"
    }
})
```

```python
import { betterAuth } from "better-auth"

export const auth = betterAuth({
    advanced: {
        cookies: {
            session_token: {
                name: "custom_session_token",
                attributes: {
                    // Set custom cookie attributes
                }
            },
        }
    }
})
```

---

## Database | Better Auth

**URL**: https://www.better-auth.com/docs/concepts/database

**Contents**:
- Database
- Adapters
- CLI
  - Running Migrations
  - Generating Schema
- Secondary Storage
  - Implementation
- Core Schema

get started, concepts, and plugins

Search documentation...

Better Auth requires a database connection to store data. The database will be used to store data such as users, sessions, and more. Plugins can also define their own database tables to store data.

You can pass a database connection to Better Auth by passing a supported database instance in the database options. You can learn more about supported database adapters in the Other relational databases documentation.

Better Auth comes with a CLI tool to manage database migrations and generate schema.

The cli checks your database and prompts you to add missing tables or update existing ones with new columns. This is only supported for the built-in Kysely adapter. For other adapters, you can use the generate command to create the schema and handle the migration through your ORM.

Better Auth also provides a generate command to generate the schema required by Better Auth. The generate command creates the schema required by Better Auth. If you're using a database adapter like Prisma or Drizzle, this command will generate the right schema for your ORM. If you're using the built-in Kysely adapter, it will generate an SQL file you can run directly on your database.

See the CLI documentation for more information on the CLI.

If you prefer adding tables manually, you can do that as well. The core schema required by Better Auth is described below and you can find additional schema required by plugins in the plugin documentation.

Secondary storage in Better Auth allows you to use key-value stores for managing session data, rate limiting counters, etc. This can be useful when you want to offload the storage of this intensive records to a high performance storage or even RAM.

To use secondary storage, implement the SecondaryStorage interface:

Then, provide your implementation to the betterAuth function:

Better Auth uses seconds for the TTL value in set(). If your storage expects milliseconds, multiply by 1000 when p

*[Content truncated - see full docs]*

**Examples**:

```text
npx @better-auth/cli migrate
```

```text
npx @better-auth/cli migrate
```

```text
npx @better-auth/cli generate
```

---

## Device Authorization | Better Auth

**URL**: https://www.better-auth.com/docs/plugins/device-authorization

**Contents**:
- Device Authorization
- Try It Out
- Installation
  - Add the plugin to your auth config
  - Migrate the database
  - Add the client plugin
- How It Works
- Basic Usage

get started, concepts, and plugins

Search documentation...

RFC 8628 CLI Smart TV IoT

The Device Authorization plugin implements the OAuth 2.0 Device Authorization Grant (RFC 8628), enabling authentication for devices with limited input capabilities such as smart TVs, CLI applications, IoT devices, and gaming consoles.

You can test the device authorization flow right now using the Better Auth CLI:

This will demonstrate the complete device authorization flow by:

The CLI login command is a demo feature that connects to the Better Auth demo server to showcase the device authorization flow in action.

Add the device authorization plugin to your server configuration.

Run the migration or generate the schema to add the necessary tables to the database.

See the Schema section to add the fields manually.

Add the device authorization plugin to your client.

The device flow follows these steps:

To initiate device authorization, call device.code with the client ID:

After displaying the user code, poll for the access token:

Example polling implementation:

The user authorization flow requires two steps:

Users must be authenticated before they can approve or deny device authorization requests. If not authenticated, redirect them to the login page with a return URL.

Create a page where users can enter their code:

Users must be authenticated to approve or deny device authorization requests:

You can validate client IDs to ensure only authorized applications can use the device flow:

Customize how device and user codes are generated:

The device flow defines specific error codes:

Here's a complete example for a CLI application based on the actual demo:

expiresIn: The expiration time for device codes. Default: "30m" (30 minutes).

interval: The minimum polling interval. Default: "5s" (5 seconds).

userCodeLength: The length of the user code. Default: 8.

deviceCodeLength: The length of the device code. Default: 40.

generateDeviceCode: Custom function to generate dev

*[Content truncated - see full docs]*

**Examples**:

```text
npx @better-auth/cli login
```

```text
npx @better-auth/cli login
```

```python
import { betterAuth } from "better-auth";
import { deviceAuthorization } from "better-auth/plugins"; 

export const auth = betterAuth({
  // ... other config
  plugins: [ 
    deviceAuthorization({ 
      // Optional configuration
      expiresIn: "30m", // Device code expiration time
      interval: "5s",    // Minimum polling interval
    }), 
  ], 
});
```

---

## Dodo Payments | Better Auth

**URL**: https://www.better-auth.com/docs/plugins/dodopayments

**Contents**:
- Dodo Payments
  - Get support on Dodo Payments' Discord
- Features
  - Get started with Dodo Payments
- Installation
- Usage
  - Creating a Checkout Session
  - Accessing the Customer Portal

get started, concepts, and plugins

Search documentation...

Dodo Payments is a global Merchant-of-Record platform that lets AI, SaaS and digital businesses sell in 150+ countries without touching tax, fraud, or compliance. A single, developer-friendly API powers checkout, billing, and payouts so you can launch worldwide in minutes.

This plugin is maintained by the Dodo Payments team. Have questions? Our team is available on Discord to assist you anytime.

You need a Dodo Payments account and API keys to use this integration.

Run the following command in your project root:

Add these to your .env file:

Create or update src/lib/auth.ts:

Set environment to live_mode for production.

Create or update src/lib/auth-client.ts:

The webhooks plugin processes real-time payment events from Dodo Payments with secure signature verification. The default endpoint is /api/auth/dodopayments/webhooks.

Generate a webhook secret for your endpoint URL (e.g., https://your-domain.com/api/auth/dodopayments/webhooks) in the Dodo Payments Dashboard and set it in your .env file:

If you encounter any issues, please refer to the Dodo Payments documentation for troubleshooting steps.

**Examples**:

```text
npm install @dodopayments/better-auth dodopayments better-auth zod
```

```text
npm install @dodopayments/better-auth dodopayments better-auth zod
```

```text
DODO_PAYMENTS_API_KEY=your_api_key_here
DODO_PAYMENTS_WEBHOOK_SECRET=your_webhook_secret_here
```

---

## Dub | Better Auth

**URL**: https://www.better-auth.com/docs/plugins/dub

**Contents**:
- Dub
- Installation
  - Install the plugin
  - Install the Dub SDK
  - Configure the plugin
- Usage
  - Lead Tracking
  - OAuth Linking

get started, concepts, and plugins

Search documentation...

Dub is an open source modern link management platform for entrepreneurs, creators, and growth teams.

This plugins allows you to track leads when a user signs up using a Dub link. It also adds OAuth linking support to allow you to build integrations extending Dub's linking management infrastructure.

First, install the plugin:

Next, install the Dub SDK on your server:

Add the plugin to your auth config:

By default, the plugin will track sign up events as leads. You can disable this by setting disableLeadTracking to true.

The plugin supports OAuth for account linking.

First, you need to setup OAuth app in Dub. Dub supports OAuth 2.0 authentication, which is recommended if you build integrations extending Dub’s functionality Learn more about OAuth.

Once you get the client ID and client secret, you can configure the plugin.

And in the client, you need to use the dubAnalyticsClient plugin.

To link account with Dub, you need to use the dub.link.

You can pass the following options to the plugin:

The Dub client instance.

Disable lead tracking for sign up events.

Event name for sign up leads.

Custom lead track function.

Dub OAuth configuration.

Client ID for Dub OAuth.

Client secret for Dub OAuth.

Enable PKCE for Dub OAuth.

**Examples**:

```text
npm install @dub/better-auth
```

```text
npm install @dub/better-auth
```

```text
npm install dub
```

---

## Elysia Integration | Better Auth

**URL**: https://www.better-auth.com/docs/integrations/elysia

**Contents**:
- Elysia Integration
  - Mount the handler
  - CORS
  - Macro
  - On this page

get started, concepts, and plugins

Search documentation...

This integration guide is assuming you are using Elysia with bun server.

Before you start, make sure you have a Better Auth instance configured. If you haven't done that yet, check out the installation.

We need to mount the handler to Elysia endpoint.

To configure cors, you can use the cors plugin from @elysiajs/cors.

You can use macro with resolve to provide session and user information before pass to view.

This will allow you to access the user and session object in all of your routes.

**Examples**:

```python
import { Elysia } from "elysia";
import { auth } from "./auth";

const app = new Elysia().mount(auth.handler).listen(3000);

console.log(
  `🦊 Elysia is running at ${app.server?.hostname}:${app.server?.port}`,
);
```

```python
import { Elysia } from "elysia";
import { auth } from "./auth";

const app = new Elysia().mount(auth.handler).listen(3000);

console.log(
  `🦊 Elysia is running at ${app.server?.hostname}:${app.server?.port}`,
);
```

```python
import { Elysia } from "elysia";
import { cors } from "@elysiajs/cors";

import { auth } from "./auth";

const app = new Elysia()
  .use(
    cors({
      origin: "http://localhost:3001",
      methods: ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
      credentials: true,
      allowedHeaders: ["Content-Type", "Authorization"],
    }),
  )
  .mount(auth.handler)
  .listen(3000);

console.log(
  `🦊 Elysia is running at ${app.server?.hostname}:${app.server?.port}`,
);
```

---

## Email | Better Auth

**URL**: https://www.better-auth.com/docs/concepts/email

**Contents**:
- Email
- Email Verification
  - Adding Email Verification to Your App
  - Triggering Email Verification
    - 1. During Sign-up
    - 2. Require Email Verification
    - 3. Manually
  - Verifying the Email

get started, concepts, and plugins

Search documentation...

Email is a key part of Better Auth, required for all users regardless of their authentication method. Better Auth provides email and password authentication out of the box, and a lot of utilities to help you manage email verification, password reset, and more.

Email verification is a security feature that ensures users provide a valid email address. It helps prevent spam and abuse by confirming that the email address belongs to the user. In this guide, you'll get a walk through of how to implement token based email verification in your app. To use otp based email verification, check out the OTP Verification guide.

To enable email verification, you need to pass a function that sends a verification email with a link.

and a request object as the second parameter.

You can initiate email verification in several ways:

To automatically send a verification email at signup, set emailVerification.sendOnSignUp to true.

This sends a verification email when a user signs up. For social logins, email verification status is read from the SSO.

With sendOnSignUp enabled, when the user logs in with an SSO that does not claim the email as verified, Better Auth will dispatch a verification email, but the verification is not required to login even when requireEmailVerification is enabled.

If you enable require email verification, users must verify their email before they can log in. And every time a user tries to sign in, sendVerificationEmail is called.

This only works if you have sendVerificationEmail implemented and if the user is trying to sign in with email and password.

if a user tries to sign in without verifying their email, you can handle the error and show a message to the user.

You can also manually trigger email verification by calling sendVerificationEmail.

If the user clicks the provided verification URL, their email is automatically verified, and they are redirected to the callbackURL.

For manual ver

*[Content truncated - see full docs]*

**Examples**:

```python
import { betterAuth } from 'better-auth';
import { sendEmail } from './email'; // your email sending function

export const auth = betterAuth({
    emailVerification: {
        sendVerificationEmail: async ({ user, url, token }, request) => {
            await sendEmail({
                to: user.email,
                subject: 'Verify your email address',
                text: `Click the link to verify your email: ${url}`
            })
        }
    }
})
```

```python
import { betterAuth } from 'better-auth';
import { sendEmail } from './email'; // your email sending function

export const auth = betterAuth({
    emailVerification: {
        sendVerificationEmail: async ({ user, url, token }, request) => {
            await sendEmail({
                to: user.email,
                subject: 'Verify your email address',
                text: `Click the link to verify your email: ${url}`
            })
        }
    }
})
```

```python
import { betterAuth } from 'better-auth';

export const auth = betterAuth({
    emailVerification: {
        sendOnSignUp: true
    }
})
```

---

## Email OTP | Better Auth

**URL**: https://www.better-auth.com/docs/plugins/email-otp

**Contents**:
- Email OTP
- Installation
  - Add the plugin to your auth config
  - Add the client plugin
- Usage
  - Send an OTP
  - Check an OTP (optional)
  - Sign In with OTP

get started, concepts, and plugins

Search documentation...

The Email OTP plugin allows user to sign in, verify their email, or reset their password using a one-time password (OTP) sent to their email address.

Add the emailOTP plugin to your auth config and implement the sendVerificationOTP() method.

Use the sendVerificationOtp() method to send an OTP to the user's email address.

Use the checkVerificationOtp() method to check if an OTP is valid.

To sign in with OTP, use the sendVerificationOtp() method to send a "sign-in" OTP to the user's email address.

Once the user provides the OTP, you can sign in the user using the signIn.emailOtp() method.

If the user is not registered, they'll be automatically registered. If you want to prevent this, you can pass disableSignUp as true in the options.

To verify the user's email address with OTP, use the sendVerificationOtp() method to send an "email-verification" OTP to the user's email address.

Once the user provides the OTP, use the verifyEmail() method to complete email verification.

To reset the user's password with OTP, use the forgetPassword.emailOTP() method to send a "forget-password" OTP to the user's email address.

Once the user provides the OTP, use the checkVerificationOtp() method to check if it's valid (optional).

Then, use the resetPassword() method to reset the user's password.

To override the default email verification, pass overrideDefaultEmailVerification: true in the options. This will make the system use an email OTP instead of the default verification link whenever email verification is triggered. In other words, the user will verify their email using an OTP rather than clicking a link.

sendVerificationOTP: A function that sends the OTP to the user's email address. The function receives an object with the following properties:

otpLength: The length of the OTP. Defaults to 6.

expiresIn: The expiry time of the OTP in seconds. Defaults to 300 seconds.

sendVerificationOnSignUp: A boolean valu

*[Content truncated - see full docs]*

**Examples**:

```python
import { betterAuth } from "better-auth"
import { emailOTP } from "better-auth/plugins"

export const auth = betterAuth({
    // ... other config options
    plugins: [
        emailOTP({ 
            async sendVerificationOTP({ email, otp, type }) { 
                if (type === "sign-in") { 
                    // Send the OTP for sign in
                } else if (type === "email-verification") { 
                    // Send the OTP for email verification
                } else { 
           
...
```

```python
import { betterAuth } from "better-auth"
import { emailOTP } from "better-auth/plugins"

export const auth = betterAuth({
    // ... other config options
    plugins: [
        emailOTP({ 
            async sendVerificationOTP({ email, otp, type }) { 
                if (type === "sign-in") { 
                    // Send the OTP for sign in
                } else if (type === "email-verification") { 
                    // Send the OTP for email verification
                } else { 
           
...
```

```python
import { createAuthClient } from "better-auth/client"
import { emailOTPClient } from "better-auth/client/plugins"

export const authClient = createAuthClient({
    plugins: [
        emailOTPClient()
    ]
})
```

---

## Email & Password | Better Auth

**URL**: https://www.better-auth.com/docs/authentication/email-password

**Contents**:
- Email & Password
- Enable Email and Password
- Usage
  - Sign Up
  - Sign In
  - Sign Out
  - Email Verification
    - Require Email Verification

get started, concepts, and plugins

Search documentation...

Email and password authentication is a common method used by many applications. Better Auth provides a built-in email and password authenticator that you can easily integrate into your project.

If you prefer username-based authentication, check out the username plugin. It extends the email and password authenticator with username support.

To enable email and password authentication, you need to set the emailAndPassword.enabled option to true in the auth configuration.

If it's not enabled, it'll not allow you to sign in or sign up with email and password.

To sign a user up, you can use the signUp.email function provided by the client.

These are the default properties for the sign up email endpoint, however it's possible that with additional fields or special plugins you can pass more properties to the endpoint.

To sign a user in, you can use the signIn.email function provided by the client.

These are the default properties for the sign in email endpoint, however it's possible that with additional fields or special plugins you can pass different properties to the endpoint.

To sign a user out, you can use the signOut function provided by the client.

you can pass fetchOptions to redirect onSuccess

To enable email verification, you need to pass a function that sends a verification email with a link. The sendVerificationEmail function takes a data object with the following properties:

and a request object as the second parameter.

On the client side you can use sendVerificationEmail function to send verification link to user. This will trigger the sendVerificationEmail function you provided in the auth configuration.

Once the user clicks on the link in the email, if the token is valid, the user will be redirected to the URL provided in the callbackURL parameter. If the token is invalid, the user will be redirected to the URL provided in the callbackURL parameter with an error message in the query str

*[Content truncated - see full docs]*

**Examples**:

```python
import { betterAuth } from "better-auth";

export const auth = betterAuth({
  emailAndPassword: { 
    enabled: true, 
  }, 
});
```

```python
import { betterAuth } from "better-auth";

export const auth = betterAuth({
  emailAndPassword: { 
    enabled: true, 
  }, 
});
```

```javascript
const { data, error } = await authClient.signUp.email({    name: "John Doe", // required    email: "[email protected]", // required    password: "password1234", // required    image: "https://example.com/image.png",    callbackURL: "https://example.com/callback",});
```

---

## Express Integration | Better Auth

**URL**: https://www.better-auth.com/docs/integrations/express

**Contents**:
- Express Integration
  - Mount the handler
  - Cors Configuration
  - Getting the User Session
  - On this page

get started, concepts, and plugins

Search documentation...

This guide will show you how to integrate Better Auth with express.js.

Before you start, make sure you have a Better Auth instance configured. If you haven't done that yet, check out the installation.

Note that CommonJS (cjs) isn't supported. Use ECMAScript Modules (ESM) by setting "type": "module" in your package.json or configuring your tsconfig.json to use ES modules.

To enable Better Auth to handle requests, we need to mount the handler to an API route. Create a catch-all route to manage all requests to /api/auth/* in case of ExpressJS v4 or /api/auth/*splat in case of ExpressJS v5 (or any other path specified in your Better Auth options).

Don’t use express.json() before the Better Auth handler. Use it only for other routes, or the client API will get stuck on "pending".

After completing the setup, start your server. Better Auth will be ready to use. You can send a GET request to the /ok endpoint (/api/auth/ok) to verify that the server is running.

To add CORS (Cross-Origin Resource Sharing) support to your Express server when integrating Better Auth, you can use the cors middleware. Below is an updated example showing how to configure CORS for your server:

To retrieve the user's session, you can use the getSession method provided by the auth object. This method requires the request headers to be passed in a specific format. To simplify this process, Better Auth provides a fromNodeHeaders helper function that converts Node.js request headers to the format expected by Better Auth (a Headers object).

Here's an example of how to use getSession in an Express route:

**Examples**:

```python
import express from "express";
import { toNodeHandler } from "better-auth/node";
import { auth } from "./auth";

const app = express();
const port = 3005;

app.all("/api/auth/*", toNodeHandler(auth)); // For ExpressJS v4
// app.all("/api/auth/*splat", toNodeHandler(auth)); For ExpressJS v5 

// Mount express json middleware after Better Auth handler
// or only apply it to routes that don't interact with Better Auth
app.use(express.json());

app.listen(port, () => {
	console.log(`Example app list
...
```

```python
import express from "express";
import { toNodeHandler } from "better-auth/node";
import { auth } from "./auth";

const app = express();
const port = 3005;

app.all("/api/auth/*", toNodeHandler(auth)); // For ExpressJS v4
// app.all("/api/auth/*splat", toNodeHandler(auth)); For ExpressJS v5 

// Mount express json middleware after Better Auth handler
// or only apply it to routes that don't interact with Better Auth
app.use(express.json());

app.listen(port, () => {
	console.log(`Example app list
...
```

```python
import express from "express";
import cors from "cors"; // Import the CORS middleware
import { toNodeHandler, fromNodeHeaders } from "better-auth/node";
import { auth } from "./auth";

const app = express();
const port = 3005;

// Configure CORS middleware
app.use(
  cors({
    origin: "http://your-frontend-domain.com", // Replace with your frontend's origin
    methods: ["GET", "POST", "PUT", "DELETE"], // Specify allowed HTTP methods
    credentials: true, // Allow credentials (cookies, author
...
```

---

## FAQ | Better Auth

**URL**: https://www.better-auth.com/docs/reference/faq

**Contents**:
- FAQ
  - Auth client not working
  - getSession not working
  - Adding custom fields to the users table
  - Difference between getSession and useSession
  - Common TypeScript Errors
  - Can I remove `name`, `image`, or `email` fields from the user table?
  - On this page

get started, concepts, and plugins

Search documentation...

This page contains frequently asked questions, common issues, and other helpful information about Better Auth.

---

## Generic OAuth | Better Auth

**URL**: https://www.better-auth.com/docs/plugins/generic-oauth

**Contents**:
- Generic OAuth
- Installation
  - Add the plugin to your auth config
  - Add the client plugin
- Usage
  - Initiate OAuth Sign-In
  - Linking OAuth Accounts
  - Handle OAuth Callback

get started, concepts, and plugins

Search documentation...

The Generic OAuth plugin provides a flexible way to integrate authentication with any OAuth provider. It supports both OAuth 2.0 and OpenID Connect (OIDC) flows, allowing you to easily add social login or custom OAuth authentication to your application.

To use the Generic OAuth plugin, add it to your auth config.

Include the Generic OAuth client plugin in your authentication client instance.

The Generic OAuth plugin provides endpoints for initiating the OAuth flow and handling the callback. Here's how to use them:

To start the OAuth sign-in process:

To link an OAuth account to an existing user:

The plugin mounts a route to handle the OAuth callback /oauth2/callback/:providerId. This means by default ${baseURL}/api/auth/oauth2/callback/:providerId will be used as the callback URL. Make sure your OAuth provider is configured to use this URL.

When adding the plugin to your auth config, you can configure multiple OAuth providers. Each provider configuration object supports the following options:

providerId: A unique string to identify the OAuth provider configuration.

discoveryUrl: (Optional) URL to fetch the provider's OAuth 2.0/OIDC configuration. If provided, endpoints like authorizationUrl, tokenUrl, and userInfoUrl can be auto-discovered.

authorizationUrl: (Optional) The OAuth provider's authorization endpoint. Not required if using discoveryUrl.

tokenUrl: (Optional) The OAuth provider's token endpoint. Not required if using discoveryUrl.

userInfoUrl: (Optional) The endpoint to fetch user profile information. Not required if using discoveryUrl.

clientId: The OAuth client ID issued by your provider.

clientSecret: The OAuth client secret issued by your provider.

scopes: (Optional) An array of scopes to request from the provider (e.g., ["openid", "email", "profile"]).

redirectURI: (Optional) The redirect URI to use for the OAuth flow. If not set, a default is constructed based on your app's b

*[Content truncated - see full docs]*

**Examples**:

```python
import { betterAuth } from "better-auth"
import { genericOAuth } from "better-auth/plugins"

export const auth = betterAuth({
    // ... other config options
    plugins: [ 
        genericOAuth({ 
            config: [ 
                { 
                    providerId: "provider-id", 
                    clientId: "test-client-id", 
                    clientSecret: "test-client-secret", 
                    discoveryUrl: "https://auth.example.com/.well-known/openid-configuration", 
          
...
```

```python
import { betterAuth } from "better-auth"
import { genericOAuth } from "better-auth/plugins"

export const auth = betterAuth({
    // ... other config options
    plugins: [ 
        genericOAuth({ 
            config: [ 
                { 
                    providerId: "provider-id", 
                    clientId: "test-client-id", 
                    clientSecret: "test-client-secret", 
                    discoveryUrl: "https://auth.example.com/.well-known/openid-configuration", 
          
...
```

```python
import { createAuthClient } from "better-auth/client"
import { genericOAuthClient } from "better-auth/client/plugins"

export const authClient = createAuthClient({
    plugins: [
        genericOAuthClient()
    ]
})
```

---

## Have I Been Pwned | Better Auth

**URL**: https://www.better-auth.com/docs/plugins/have-i-been-pwned

**Contents**:
- Have I Been Pwned
- Installation
  - Add the plugin to your auth config
- Usage
- Config
- Security Notes
  - On this page

get started, concepts, and plugins

Search documentation...

The Have I Been Pwned plugin helps protect user accounts by preventing the use of passwords that have been exposed in known data breaches. It uses the Have I Been Pwned API to check if a password has been compromised.

When a user attempts to create an account or update their password with a compromised password, they'll receive the following default error:

You can customize the error message:

**Examples**:

```python
import { betterAuth } from "better-auth"
import { haveIBeenPwned } from "better-auth/plugins"

export const auth = betterAuth({
    plugins: [
        haveIBeenPwned()
    ]
})
```

```python
import { betterAuth } from "better-auth"
import { haveIBeenPwned } from "better-auth/plugins"

export const auth = betterAuth({
    plugins: [
        haveIBeenPwned()
    ]
})
```

```text
{
  "code": "PASSWORD_COMPROMISED",
  "message": "Password is compromised"
}
```

---

## Hono Integration | Better Auth

**URL**: https://www.better-auth.com/docs/integrations/hono

**Contents**:
- Hono Integration
  - Mount the handler
  - Cors
  - Middleware
  - Cross-Domain Cookies
  - Client-Side Configuration
  - On this page

get started, concepts, and plugins

Search documentation...

Before you start, make sure you have a Better Auth instance configured. If you haven't done that yet, check out the installation.

We need to mount the handler to Hono endpoint.

To configure cors, you need to use the cors plugin from hono/cors.

Important: CORS middleware must be registered before your routes. This ensures that cross-origin requests are properly handled before they reach your authentication endpoints.

You can add a middleware to save the session and user in a context and also add validations for every route.

This will allow you to access the user and session object in all of your routes.

By default, all Better Auth cookies are set with SameSite=Lax. If you need to use cookies across different domains, you’ll need to set SameSite=None and Secure=true. However, we recommend using subdomains whenever possible, as this allows you to keep SameSite=Lax. To enable cross-subdomain cookies, simply turn on crossSubDomainCookies in your auth config.

If you still need to set SameSite=None and Secure=true, you can adjust these attributes globally through cookieOptions in the createAuth configuration.

You can also customize cookie attributes individually by setting them within cookies in your auth config.

When using the Hono client (@hono/client) to make requests to your Better Auth-protected endpoints, you need to configure it to send credentials (cookies) with cross-origin requests.

This configuration is necessary when:

The credentials: "include" option tells the fetch client to send cookies even for cross-origin requests. This works in conjunction with the CORS configuration on your server that has credentials: true.

Note: Make sure your CORS configuration on the server matches your client's domain, and that credentials: true is set in both the server's CORS config and the client's fetch config.

**Examples**:

```python
import { Hono } from "hono";
import { auth } from "./auth";
import { serve } from "@hono/node-server";

const app = new Hono();

app.on(["POST", "GET"], "/api/auth/*", (c) => {
	return auth.handler(c.req.raw);
});

serve(app);
```

```python
import { Hono } from "hono";
import { auth } from "./auth";
import { serve } from "@hono/node-server";

const app = new Hono();

app.on(["POST", "GET"], "/api/auth/*", (c) => {
	return auth.handler(c.req.raw);
});

serve(app);
```

```python
import { Hono } from "hono";
import { auth } from "./auth";
import { serve } from "@hono/node-server";
import { cors } from "hono/cors";
 
const app = new Hono();

app.use(
	"/api/auth/*", // or replace with "*" to enable cors for all routes
	cors({
		origin: "http://localhost:3001", // replace with your origin
		allowHeaders: ["Content-Type", "Authorization"],
		allowMethods: ["POST", "GET", "OPTIONS"],
		exposeHeaders: ["Content-Length"],
		maxAge: 600,
		credentials: true,
	}),
);

app.on(["P
...
```

---

## Hooks | Better Auth

**URL**: https://www.better-auth.com/docs/concepts/hooks

**Contents**:
- Hooks
- Before Hooks
  - Example: Enforce Email Domain Restriction
  - Example: Modify Request Context
- After Hooks
  - Example: Send a notification to your channel when a new user is registered
- Ctx
  - Request Response

get started, concepts, and plugins

Search documentation...

Hooks in Better Auth let you "hook into" the lifecycle and execute custom logic. They provide a way to customize Better Auth's behavior without writing a full plugin.

We highly recommend using hooks if you need to make custom adjustments to an endpoint rather than making another endpoint outside of Better Auth.

Before hooks run before an endpoint is executed. Use them to modify requests, pre validate data, or return early.

This hook ensures that users can only sign up if their email ends with @example.com:

To adjust the request context before proceeding:

After hooks run after an endpoint is executed. Use them to modify responses.

When you call createAuthMiddleware a ctx object is passed that provides a lot of useful properties. Including:

This utilities allows you to get request information and to send response from a hook.

Use ctx.json to send JSON responses:

Use ctx.redirect to redirect users:

Throw errors with APIError for a specific status code and message:

The ctx object contains another context object inside that's meant to hold contexts related to auth. Including a newly created session on after hook, cookies configuration, password hasher and so on.

The newly created session after an endpoint is run. This only exist in after hook.

The returned value from the hook is passed to the next hook in the chain.

The response headers added by endpoints and hooks that run before this hook.

Access BetterAuth’s predefined cookie properties:

You can access the secret for your auth instance on ctx.context.secret

The password object provider hash and verify

Adapter exposes the adapter methods used by Better Auth. Including findOne, findMany, create, delete, update and updateMany. You generally should use your actually db instance from your orm rather than this adapter.

These are calls to your db that perform specific actions. createUser, createSession, updateSession...

This may be useful to use

*[Content truncated - see full docs]*

**Examples**:

```python
import { betterAuth } from "better-auth";
import { createAuthMiddleware, APIError } from "better-auth/api";

export const auth = betterAuth({
    hooks: {
        before: createAuthMiddleware(async (ctx) => {
            if (ctx.path !== "/sign-up/email") {
                return;
            }
            if (!ctx.body?.email.endsWith("@example.com")) {
                throw new APIError("BAD_REQUEST", {
                    message: "Email must end with @example.com",
                });
      
...
```

```python
import { betterAuth } from "better-auth";
import { createAuthMiddleware, APIError } from "better-auth/api";

export const auth = betterAuth({
    hooks: {
        before: createAuthMiddleware(async (ctx) => {
            if (ctx.path !== "/sign-up/email") {
                return;
            }
            if (!ctx.body?.email.endsWith("@example.com")) {
                throw new APIError("BAD_REQUEST", {
                    message: "Email must end with @example.com",
                });
      
...
```

```python
import { betterAuth } from "better-auth";
import { createAuthMiddleware } from "better-auth/api";

export const auth = betterAuth({
    hooks: {
        before: createAuthMiddleware(async (ctx) => {
            if (ctx.path === "/sign-up/email") {
                return {
                    context: {
                        ...ctx,
                        body: {
                            ...ctx.body,
                            name: "John Doe",
                        },
                  
...
```

---

## JWT | Better Auth

**URL**: https://www.better-auth.com/docs/plugins/jwt

**Contents**:
- JWT
- Installation
  - Add the plugin to your auth config
  - Migrate the database
- Usage
- JWT
  - Retrieve the token
  - Verifying the token

get started, concepts, and plugins

Search documentation...

The JWT plugin provides endpoints to retrieve a JWT token and a JWKS endpoint to verify the token.

This plugin is not meant as a replacement for the session. It's meant to be used for services that require JWT tokens. If you're looking to use JWT tokens for authentication, check out the Bearer Plugin.

Run the migration or generate the schema to add the necessary fields and tables to the database.

See the Schema section to add the fields manually.

Once you've installed the plugin, you can start using the JWT & JWKS plugin to get the token and the JWKS through their respective endpoints.

There are multiple ways to retrieve JWT tokens:

Add the jwtClient plugin to your auth client configuration:

Then use the client to get JWT tokens:

This is the recommended approach for client applications that need JWT tokens for external API authentication.

To get the token, call the /token endpoint. This will return the following:

Make sure to include the token in the Authorization header of your requests if the bearer plugin is added in your auth configuration.

When you call getSession method, a JWT is returned in the set-auth-jwt header, which you can use to send to your services directly.

The token can be verified in your own service, without the need for an additional verify call or database check. For this JWKS is used. The public key can be fetched from the /api/auth/jwks endpoint.

Since this key is not subject to frequent changes, it can be cached indefinitely. The key ID (kid) that was used to sign a JWT is included in the header of the token. In case a JWT with a different kid is received, it is recommended to fetch the JWKS again.

If you are making your system oAuth compliant (such as when utilizing the OIDC or MCP plugins), you MUST disable the /token endpoint (oAuth equivalent /oauth2/token) and disable setting the jwt header (oAuth equivalent /oauth2/userinfo).

Disables the /jwks endpoint and use

*[Content truncated - see full docs]*

**Examples**:

```python
import { betterAuth } from "better-auth"
import { jwt } from "better-auth/plugins"

export const auth = betterAuth({
    plugins: [ 
        jwt(), 
    ] 
})
```

```python
import { betterAuth } from "better-auth"
import { jwt } from "better-auth/plugins"

export const auth = betterAuth({
    plugins: [ 
        jwt(), 
    ] 
})
```

```text
npx @better-auth/cli migrate
```

---

## Last Login Method | Better Auth

**URL**: https://www.better-auth.com/docs/plugins/last-login-method

**Contents**:
- Last Login Method
- Installation
  - Add the plugin to your auth config
  - Add the client plugin to your auth client
- Usage
  - Getting the Last Used Method
  - UI Integration Example
- Database Persistence

get started, concepts, and plugins

Search documentation...

The last login method plugin tracks the most recent authentication method used by users (email, OAuth providers, etc.). This enables you to display helpful indicators on login pages, such as "Last signed in with Google" or prioritize certain login methods based on user preferences.

Once installed, the plugin automatically tracks the last authentication method used by users. You can then retrieve and display this information in your application.

The client plugin provides several methods to work with the last login method:

Here's how to use the plugin to enhance your login page:

By default, the last login method is stored only in cookies. For more persistent tracking and analytics, you can enable database storage.

Set storeInDatabase to true in your plugin configuration:

The plugin will automatically add a lastLoginMethod field to your user table. Run the migration to apply the changes:

When database storage is enabled, the lastLoginMethod field becomes available in user objects:

When storeInDatabase is enabled, the plugin adds the following field to the user table:

You can customize the database field name:

The last login method plugin accepts the following options:

storeInDatabase: boolean

customResolveMethod: (ctx: GenericEndpointContext) => string | null

By default, the plugin tracks these authentication methods:

The plugin automatically detects the method from these endpoints:

The plugin automatically inherits cookie settings from Better Auth's centralized cookie system. This solves the problem where the last login method wouldn't persist across:

When you enable crossSubDomainCookies or crossOriginCookies in your Better Auth config, the plugin will automatically use the same domain, secure, and sameSite settings as your session cookies, ensuring consistent behavior across your application.

If you have custom OAuth providers or authentication methods, you can use the customResolveMethod

*[Content truncated - see full docs]*

**Examples**:

```python
import { betterAuth } from "better-auth"
import { lastLoginMethod } from "better-auth/plugins"

export const auth = betterAuth({
    // ... other config options
    plugins: [
        lastLoginMethod() 
    ]
})
```

```python
import { betterAuth } from "better-auth"
import { lastLoginMethod } from "better-auth/plugins"

export const auth = betterAuth({
    // ... other config options
    plugins: [
        lastLoginMethod() 
    ]
})
```

```python
import { createAuthClient } from "better-auth/client"
import { lastLoginMethodClient } from "better-auth/client/plugins"

export const authClient = createAuthClient({
    plugins: [
        lastLoginMethodClient() 
    ]
})
```

---

## MS SQL | Better Auth

**URL**: https://www.better-auth.com/docs/adapters/mssql

**Contents**:
- MS SQL
- Example Usage
- Schema generation & migration
- Additional Information
  - On this page

get started, concepts, and plugins

Search documentation...

Microsoft SQL Server is a relational database management system developed by Microsoft, designed for enterprise-level data storage, management, and analytics with robust security and scalability features. Read more here.

Make sure you have MS SQL installed and configured. Then, you can connect it straight into Better Auth.

For more information, read Kysely's documentation to the MssqlDialect.

The Better Auth CLI allows you to generate or migrate your database schema based on your Better Auth configuration and plugins.

MS SQL Schema Generation

MS SQL Schema Migration

MS SQL is supported under the hood via the Kysely adapter, any database supported by Kysely would also be supported. (Read more here)

If you're looking for performance improvements or tips, take a look at our guide to performance optimizations.

Other Relational Databases

**Examples**:

```python
import { betterAuth } from "better-auth";
import { MssqlDialect } from "kysely";
import * as Tedious from 'tedious'
import * as Tarn from 'tarn'

const dialect = new MssqlDialect({
  tarn: {
    ...Tarn,
    options: {
      min: 0,
      max: 10,
    },
  },
  tedious: {
    ...Tedious,
    connectionFactory: () => new Tedious.Connection({
      authentication: {
        options: {
          password: 'password',
          userName: 'username',
        },
        type: 'default',
      },
     
...
```

```python
import { betterAuth } from "better-auth";
import { MssqlDialect } from "kysely";
import * as Tedious from 'tedious'
import * as Tarn from 'tarn'

const dialect = new MssqlDialect({
  tarn: {
    ...Tarn,
    options: {
      min: 0,
      max: 10,
    },
  },
  tedious: {
    ...Tedious,
    connectionFactory: () => new Tedious.Connection({
      authentication: {
        options: {
          password: 'password',
          userName: 'username',
        },
        type: 'default',
      },
     
...
```

```text
npx @better-auth/cli@latest generate
```

---

## Magic link | Better Auth

**URL**: https://www.better-auth.com/docs/plugins/magic-link

**Contents**:
- Magic link
- Installation
  - Add the server Plugin
  - Add the client Plugin
- Usage
  - Sign In with Magic Link
  - Verify Magic Link
- Configuration Options

get started, concepts, and plugins

Search documentation...

Magic link or email link is a way to authenticate users without a password. When a user enters their email, a link is sent to their email. When the user clicks on the link, they are authenticated.

Add the magic link plugin to your server:

Add the magic link plugin to your client:

To sign in with a magic link, you need to call signIn.magicLink with the user's email address. The sendMagicLink function is called to send the magic link to the user's email.

If the user has not signed up, unless disableSignUp is set to true, the user will be signed up automatically.

When you send the URL generated by the sendMagicLink function to a user, clicking the link will authenticate them and redirect them to the callbackURL specified in the signIn.magicLink function. If an error occurs, the user will be redirected to the callbackURL with an error query parameter.

If no callbackURL is provided, the user will be redirected to the root URL.

If you want to handle the verification manually, (e.g, if you send the user a different URL), you can use the verify function.

sendMagicLink: The sendMagicLink function is called when a user requests a magic link. It takes an object with the following properties:

and a request object as the second parameter.

expiresIn: specifies the time in seconds after which the magic link will expire. The default value is 300 seconds (5 minutes).

disableSignUp: If set to true, the user will not be able to sign up using the magic link. The default value is false.

generateToken: The generateToken function is called to generate a token which is used to uniquely identify the user. The default value is a random string. There is one parameter:

When using generateToken, ensure that the returned string is hard to guess because it is used to verify who someone actually is in a confidential way. By default, we return a long and cryptographically secure string.

storeToken: The storeToken function is

*[Content truncated - see full docs]*

**Examples**:

```python
import { betterAuth } from "better-auth";
import { magicLink } from "better-auth/plugins";

export const auth = betterAuth({
    plugins: [
        magicLink({
            sendMagicLink: async ({ email, token, url }, request) => {
                // send email to user
            }
        })
    ]
})
```

```python
import { betterAuth } from "better-auth";
import { magicLink } from "better-auth/plugins";

export const auth = betterAuth({
    plugins: [
        magicLink({
            sendMagicLink: async ({ email, token, url }, request) => {
                // send email to user
            }
        })
    ]
})
```

```python
import { createAuthClient } from "better-auth/client";
import { magicLinkClient } from "better-auth/client/plugins";
export const authClient = createAuthClient({
    plugins: [
        magicLinkClient()
    ]
});
```

---

## Multi Session | Better Auth

**URL**: https://www.better-auth.com/docs/plugins/multi-session

**Contents**:
- Multi Session
- Installation
  - Add the plugin to your auth config
  - Add the client Plugin
- Usage
  - List all device sessions
  - Set active session
  - Revoke a session

get started, concepts, and plugins

Search documentation...

The multi-session plugin allows users to maintain multiple active sessions across different accounts in the same browser. This plugin is useful for applications that require users to switch between multiple accounts without logging out.

Add the client plugin and Specify where the user should be redirected if they need to verify 2nd factor

Whenever a user logs in, the plugin will add additional cookie to the browser. This cookie will be used to maintain multiple sessions across different accounts.

To list all active sessions for the current user, you can call the listDeviceSessions method.

To set the active session, you can call the setActive method.

To revoke a session, you can call the revoke method.

When a user logs out, the plugin will revoke all active sessions for the user. You can do this by calling the existing signOut method, which handles revoking all sessions automatically.

You can specify the maximum number of sessions a user can have by passing the maximumSessions option to the plugin. By default, the plugin allows 5 sessions per device.

**Examples**:

```python
import { betterAuth } from "better-auth"
import { multiSession } from "better-auth/plugins"

export const auth = betterAuth({
    plugins: [ 
        multiSession(), 
    ] 
})
```

```python
import { betterAuth } from "better-auth"
import { multiSession } from "better-auth/plugins"

export const auth = betterAuth({
    plugins: [ 
        multiSession(), 
    ] 
})
```

```python
import { createAuthClient } from "better-auth/client"
import { multiSessionClient } from "better-auth/client/plugins"

export const authClient = createAuthClient({
    plugins: [
        multiSessionClient()
    ]
})
```

---

## MySQL | Better Auth

**URL**: https://www.better-auth.com/docs/adapters/mysql

**Contents**:
- MySQL
- Example Usage
- Schema generation & migration
- Additional Information
  - On this page

get started, concepts, and plugins

Search documentation...

MySQL is a popular open-source relational database management system (RDBMS) that is widely used for building web applications and other types of software. It provides a flexible and scalable database solution that allows for efficient storage and retrieval of data. Read more here: MySQL.

Make sure you have MySQL installed and configured. Then, you can connect it straight into Better Auth.

For more information, read Kysely's documentation to the MySQLDialect.

The Better Auth CLI allows you to generate or migrate your database schema based on your Better Auth configuration and plugins.

MySQL Schema Generation

MySQL Schema Migration

MySQL is supported under the hood via the Kysely adapter, any database supported by Kysely would also be supported. (Read more here)

If you're looking for performance improvements or tips, take a look at our guide to performance optimizations.

Other Social Providers

**Examples**:

```python
import { betterAuth } from "better-auth";
import { createPool } from "mysql2/promise";

export const auth = betterAuth({
  database: createPool({
    host: "localhost",
    user: "root",
    password: "password",
    database: "database",
    timezone: "Z", // Important to ensure consistent timezone values
  }),
});
```

```python
import { betterAuth } from "better-auth";
import { createPool } from "mysql2/promise";

export const auth = betterAuth({
  database: createPool({
    host: "localhost",
    user: "root",
    password: "password",
    database: "database",
    timezone: "Z", // Important to ensure consistent timezone values
  }),
});
```

```text
npx @better-auth/cli@latest generate
```

---

## NestJS Integration | Better Auth

**URL**: https://www.better-auth.com/docs/integrations/nestjs

**Contents**:
- NestJS Integration
- Installation
- Basic Setup
  - 1. Disable Body Parser
  - 2. Import AuthModule
  - 3. Route Protection
- Full Documentation
  - On this page

get started, concepts, and plugins

Search documentation...

This guide will show you how to integrate Better Auth with NestJS.

Before you start, make sure you have a Better Auth instance configured. If you haven't done that yet, check out the installation.

The NestJS integration is community maintained. If you encounter any issues, please open them at nestjs-better-auth.

Install the NestJS integration library:

Currently the library has beta support for Fastify, if you experience any issues with it, please open an issue at nestjs-better-auth.

Disable NestJS's built-in body parser to allow Better Auth to handle the raw request body:

Import the AuthModule in your root module:

Global by default: An AuthGuard is registered globally by this module. All routes are protected unless you explicitly allow access.

Use the Session decorator to access the user session:

For comprehensive documentation including decorators, hooks, global guards, and advanced configuration, visit the NestJS Better Auth repository.

**Examples**:

```text
npm install @thallesp/nestjs-better-auth
```

```text
npm install @thallesp/nestjs-better-auth
```

```python
import { NestFactory } from "@nestjs/core";
import { AppModule } from "./app.module";

async function bootstrap() {
  const app = await NestFactory.create(AppModule, {
    bodyParser: false, // Required for Better Auth
  });
  await app.listen(process.env.PORT ?? 3000);
}
bootstrap();
```

---

## Nitro Integration | Better Auth

**URL**: https://www.better-auth.com/docs/integrations/nitro

**Contents**:
- Nitro Integration
- Create a new Nitro Application
  - Prisma Adapter Setup
  - Install & Configure Better Auth
  - Update Prisma Schema
- Mount The Handler
  - CORS
  - Auth Guard/Middleware

get started, concepts, and plugins

Search documentation...

Better Auth can be integrated with your Nitro Application (an open source framework to build web servers).

This guide aims to help you integrate Better Auth with your Nitro application in a few simple steps.

Start by scaffolding a new Nitro application using the following command:

This will create the nitro-app directory and install all the dependencies. You can now open the nitro-app directory in your code editor.

This guide assumes that you have a basic understanding of Prisma. If you are new to Prisma, you can check out the Prisma documentation.

The sqlite database used in this guide will not work in a production environment. You should replace it with a production-ready database like PostgreSQL.

For this guide, we will be using the Prisma adapter. You can install prisma client by running the following command:

prisma can be installed as a dev dependency using the following command:

Generate a schema.prisma file in the prisma directory by running the following command:

You can now replace the contents of the schema.prisma file with the following:

Ensure that you update the DATABASE_URL in your .env file to point to the location of your database.

Run the following command to generate the Prisma client & sync the database:

Follow steps 1 & 2 from the installation guide to install Better Auth in your Nitro application & set up the environment variables.

Once that is done, create your Better Auth instance within the server/utils/auth.ts file.

Use the Better Auth CLI to update your Prisma schema with the required models by running the following command:

The --config flag is used to specify the path to the file where you have created your Better Auth instance.

Head over to the prisma/schema.prisma file & save the file to trigger the format on save.

After saving the file, you can run the npx prisma db push command to update the database schema.

You can now mount the Better Auth handler in you

*[Content truncated - see full docs]*

**Examples**:

```text
npx giget@latest nitro nitro-app --install
```

```text
npx giget@latest nitro nitro-app --install
```

```text
npm install @prisma/client
```

---

## OAuth | Better Auth

**URL**: https://www.better-auth.com/docs/concepts/oauth

**Contents**:
- OAuth
- Configuring Social Providers
- Usage
  - Sign In
  - Link account
  - Get Access Token
  - Get Account Info Provided by the provider
  - Requesting Additional Scopes

get started, concepts, and plugins

Search documentation...

Better Auth comes with built-in support for OAuth 2.0 and OpenID Connect. This allows you to authenticate users via popular OAuth providers like Google, Facebook, GitHub, and more.

If your desired provider isn't directly supported, you can use the Generic OAuth Plugin for custom integrations.

To enable a social provider, you need to provide clientId and clientSecret for the provider.

Here's an example of how to configure Google as a provider:

To sign in with a social provider, you can use the signIn.social function with the authClient or auth.api for server-side usage.

To link an account to a social provider, you can use the linkAccount function with the authClient or auth.api for server-side usage.

To get the access token for a social provider, you can use the getAccessToken function with the authClient or auth.api for server-side usage. When you use this endpoint, if the access token is expired, it will be refreshed.

To get provider specific account info you can use the accountInfo function with the authClient or auth.api for server-side usage.

Sometimes your application may need additional OAuth scopes after the user has already signed up (e.g., for accessing GitHub repositories or Google Drive). Users may not want to grant extensive permissions initially, preferring to start with minimal permissions and grant additional access as needed.

You can request additional scopes by using the linkSocial method with the same provider. This will trigger a new OAuth flow that requests the additional scopes while maintaining the existing account connection.

Make sure you're running Better Auth version 1.2.7 or later. Earlier versions (like 1.2.2) may show a "Social account already linked" error when trying to link with an existing provider for additional scopes.

The scope of the access request. For example, email or profile.

Custom redirect URI for the provider. By default, it uses /api/auth/callback/${

*[Content truncated - see full docs]*

**Examples**:

```python
import { betterAuth } from "better-auth";

export const auth = betterAuth({
  // Other configurations...
  socialProviders: {
    google: {
      clientId: "YOUR_GOOGLE_CLIENT_ID",
      clientSecret: "YOUR_GOOGLE_CLIENT_SECRET",
    },
  },
});
```

```python
import { betterAuth } from "better-auth";

export const auth = betterAuth({
  // Other configurations...
  socialProviders: {
    google: {
      clientId: "YOUR_GOOGLE_CLIENT_ID",
      clientSecret: "YOUR_GOOGLE_CLIENT_SECRET",
    },
  },
});
```

```text
// client-side usage
await authClient.signIn.social({
  provider: "google", // or any other provider id
})
```

---

## OAuth Proxy | Better Auth

**URL**: https://www.better-auth.com/docs/plugins/oauth-proxy

**Contents**:
- OAuth Proxy
- Installation
  - Add the plugin to your auth config
  - Add redirect URL to your OAuth provider
- How it works
- Options
  - On this page

get started, concepts, and plugins

Search documentation...

A proxy plugin, that allows you to proxy OAuth requests. Useful for development and preview deployments where the redirect URL can't be known in advance to add to the OAuth provider.

For the proxy server to work properly, you’ll need to pass the redirect URL of your main production app registered with the OAuth provider in your social provider config. This needs to be done for each social provider you want to proxy requests for.

The plugin adds an endpoint to your server that proxies OAuth requests. When you initiate a social sign-in, it sets the redirect URL to this proxy endpoint. After the OAuth provider redirects back to your server, the plugin then forwards the user to the original callback URL.

When the OAuth provider returns the user to your server, the plugin automatically redirects them to the intended callback URL.

To share cookies between the proxy server and your main server it uses URL query parameters to pass the cookies encrypted in the URL. This is secure as the cookies are encrypted and can only be decrypted by the server.

This plugin requires skipping the state cookie check. This has security implications and should only be used in dev or staging environments. If baseURL and productionURL are the same, the plugin will not proxy the request.

currentURL: The application's current URL is automatically determined by the plugin. It first checks for the request URL if invoked by a client, then it checks the base URL from popular hosting providers, and finally falls back to the baseURL in your auth config. If the URL isn’t inferred correctly, you can specify it manually here.

productionURL: If this value matches the baseURL in your auth config, requests will not be proxied. Defaults to the BETTER_AUTH_URL environment variable.

**Examples**:

```python
import { betterAuth } from "better-auth"
import { oAuthProxy } from "better-auth/plugins"

export const auth = betterAuth({
    plugins: [ 
        oAuthProxy({ 
            productionURL: "https://my-main-app.com", // Optional - if the URL isn't inferred correctly
            currentURL: "http://localhost:3000", // Optional - if the URL isn't inferred correctly
        }), 
    ] 
})
```

```python
import { betterAuth } from "better-auth"
import { oAuthProxy } from "better-auth/plugins"

export const auth = betterAuth({
    plugins: [ 
        oAuthProxy({ 
            productionURL: "https://my-main-app.com", // Optional - if the URL isn't inferred correctly
            currentURL: "http://localhost:3000", // Optional - if the URL isn't inferred correctly
        }), 
    ] 
})
```

```javascript
export const auth = betterAuth({
   plugins: [
       oAuthProxy(),
   ], 
   socialProviders: {
        github: {
            clientId: "your-client-id",
            clientSecret: "your-client-secret",
            redirectURI: "https://my-main-app.com/api/auth/callback/github"
        }
   }
})
```

---

## OIDC Provider | Better Auth

**URL**: https://www.better-auth.com/docs/plugins/oidc-provider

**Contents**:
- OIDC Provider
- Installation
  - Mount the Plugin
  - Migrate the Database
  - Add the Client Plugin
- Usage
  - Register a New Client
    - Simple Example

get started, concepts, and plugins

Search documentation...

The OIDC Provider Plugin enables you to build and manage your own OpenID Connect (OIDC) provider, granting full control over user authentication without relying on third-party services like Okta or Azure AD. It also allows other services to authenticate users through your OIDC provider.

This plugin is in active development and may not be suitable for production use. Please report any issues or bugs on GitHub.

Add the OIDC plugin to your auth config. See OIDC Configuration on how to configure the plugin.

Run the migration or generate the schema to add the necessary fields and tables to the database.

See the Schema section to add the fields manually.

Add the OIDC client plugin to your auth client config.

Once installed, you can utilize the OIDC Provider to manage authentication flows within your application.

To register a new OIDC client, use the oauth2.register method.

This endpoint supports RFC7591 compliant client registration.

Once the application is created, you will receive a client_id and client_secret that you can display to the user.

For first-party applications and internal services, you can configure trusted clients directly in your OIDC provider configuration. Trusted clients bypass database lookups for better performance and can optionally skip consent screens for improved user experience.

The OIDC Provider includes a UserInfo endpoint that allows clients to retrieve information about the authenticated user. This endpoint is available at /oauth2/userinfo and requires a valid access token.

The UserInfo endpoint returns different claims based on the scopes that were granted during authorization:

The getAdditionalUserInfoClaim function receives the user object, requested scopes array, and the client, allowing you to conditionally include claims based on the scopes granted during authorization. These additional claims will be included in both the UserInfo endpoint response and the ID to

*[Content truncated - see full docs]*

**Examples**:

```python
import { betterAuth } from "better-auth";
import { oidcProvider } from "better-auth/plugins";

const auth = betterAuth({
    plugins: [oidcProvider({
        loginPage: "/sign-in", // path to the login page
        // ...other options
    })]
})
```

```python
import { betterAuth } from "better-auth";
import { oidcProvider } from "better-auth/plugins";

const auth = betterAuth({
    plugins: [oidcProvider({
        loginPage: "/sign-in", // path to the login page
        // ...other options
    })]
})
```

```text
npx @better-auth/cli migrate
```

---

## One-Time Token Plugin | Better Auth

**URL**: https://www.better-auth.com/docs/plugins/one-time-token

**Contents**:
- One-Time Token Plugin
- Installation
  - Add the plugin to your auth config
  - Add the client plugin
- Usage
  - 1. Generate a Token
  - 2. Verify the Token
- Options

get started, concepts, and plugins

Search documentation...

The One-Time Token (OTT) plugin provides functionality to generate and verify secure, single-use session tokens. These are commonly used for across domains authentication.

To use the One-Time Token plugin, add it to your auth config.

Next, include the one-time-token client plugin in your authentication client instance.

Generate a token using auth.api.generateOneTimeToken or authClient.oneTimeToken.generate

This will return a token that is attached to the current session which can be used to verify the one-time token. By default, the token will expire in 3 minutes.

When the user clicks the link or submits the token, use the auth.api.verifyOneTimeToken or authClient.oneTimeToken.verify method in another API route to validate it.

This will return the session that was attached to the token.

These options can be configured when adding the oneTimeToken plugin:

generateToken: A custom token generator function that takes session object and a ctx as paramters.

storeToken: Optional. This option allows you to configure how the token is stored in your database.

Note: It will not affect the token that's sent, it will only affect the token stored in your database.

**Examples**:

```python
import { betterAuth } from "better-auth";
import { oneTimeToken } from "better-auth/plugins/one-time-token";

export const auth = betterAuth({
    plugins: [
      oneTimeToken()
    ]
    // ... other auth config
});
```

```python
import { betterAuth } from "better-auth";
import { oneTimeToken } from "better-auth/plugins/one-time-token";

export const auth = betterAuth({
    plugins: [
      oneTimeToken()
    ]
    // ... other auth config
});
```

```python
import { createAuthClient } from "better-auth/client"
import { oneTimeTokenClient } from "better-auth/client/plugins"

export const authClient = createAuthClient({
    plugins: [
        oneTimeTokenClient()
    ]
})
```

---

## Open API | Better Auth

**URL**: https://www.better-auth.com/docs/plugins/open-api

**Contents**:
- Open API
- Installation
  - Add the plugin to your auth config
  - Navigate to /api/auth/reference to view the Open API reference
- Usage
  - Generated Schema
  - Using Scalar with Multiple Sources
- Configuration

get started, concepts, and plugins

Search documentation...

This is a plugin that provides an Open API reference for Better Auth. It shows all endpoints added by plugins and the core. It also provides a way to test the endpoints. It uses Scalar to display the Open API reference.

This plugin is still in the early stages of development. We are working on adding more features to it and filling in the gaps.

Each plugin endpoints are grouped by the plugin name. The core endpoints are grouped under the Default group. And Model schemas are grouped under the Models group.

The Open API reference is generated using the OpenAPI 3.0 specification. You can use the reference to generate client libraries, documentation, and more.

The reference is generated using the Scalar library. Scalar provides a way to view and test the endpoints. You can test the endpoints by clicking on the Try it out button and providing the required parameters.

To get the generated Open API schema directly as JSON, you can do auth.api.generateOpenAPISchema(). This will return the Open API schema as a JSON object.

If you're using Scalar for your API documentation, you can add Better Auth as an additional source alongside your main API:

When using Hono with Scalar for OpenAPI documentation, you can integrate Better Auth by adding it as a source:

path - The path where the Open API reference is served. Default is /api/auth/reference. You can change it to any path you like, but keep in mind that it will be appended to the base path of your auth server.

disableDefaultReference - If set to true, the default Open API reference UI by Scalar will be disabled. Default is false.

This allows you to display both your application's API and Better Auth's authentication endpoints in a unified documentation interface.

theme - Allows you to change the theme of the OpenAPI reference page. Default is default.

**Examples**:

```python
import { betterAuth } from "better-auth"
import { openAPI } from "better-auth/plugins"

export const auth = betterAuth({
    plugins: [ 
        openAPI(), 
    ] 
})
```

```python
import { betterAuth } from "better-auth"
import { openAPI } from "better-auth/plugins"

export const auth = betterAuth({
    plugins: [ 
        openAPI(), 
    ] 
})
```

```python
import { auth } from "~/lib/auth"

const openAPISchema = await auth.api.generateOpenAPISchema()
console.log(openAPISchema)
```

---

## Organization | Better Auth

**URL**: https://www.better-auth.com/docs/plugins/organization

**Contents**:
- Organization
- Installation
  - Add the plugin to your auth config
  - Migrate the database
  - Add the client plugin
- Usage
- Organization
  - Create an organization

get started, concepts, and plugins

Search documentation...

Organizations simplifies user access and permissions management. Assign roles and permissions to streamline project management, team coordination, and partnerships.

Run the migration or generate the schema to add the necessary fields and tables to the database.

See the Schema section to add the fields manually.

Once you've installed the plugin, you can start using the organization plugin to manage your organization's members and teams. The client plugin will provide you with methods under the organization namespace, and the server api will provide you with the necessary endpoints to manage your organization and give you an easier way to call the functions on your own backend.

By default, any user can create an organization. To restrict this, set the allowUserToCreateOrganization option to a function that returns a boolean, or directly to true or false.

To check if an organization slug is taken or not you can use the checkSlug function provided by the client. The function takes an object with the following properties:

You can customize organization operations using hooks that run before and after various organization-related activities. Better Auth provides two ways to configure hooks:

Control organization lifecycle operations:

The legacy organizationCreation hooks are still supported but deprecated. Use organizationHooks.beforeCreateOrganization and organizationHooks.afterCreateOrganization instead for new projects.

Control member operations within organizations:

Control invitation lifecycle:

Control team operations (when teams are enabled):

All hooks support error handling. Throwing an error in a before hook will prevent the operation from proceeding:

To list the organizations that a user is a member of, you can use useListOrganizations hook. It implements a reactive way to get the organizations that the user is a member of.

Or alternatively, you can call organization.list if you don't want 

*[Content truncated - see full docs]*

**Examples**:

```python
import { betterAuth } from "better-auth"
import { organization } from "better-auth/plugins"

export const auth = betterAuth({
    plugins: [ 
        organization() 
    ] 
})
```

```python
import { betterAuth } from "better-auth"
import { organization } from "better-auth/plugins"

export const auth = betterAuth({
    plugins: [ 
        organization() 
    ] 
})
```

```text
npx @better-auth/cli migrate
```

---

## Other Relational Databases | Better Auth

**URL**: https://www.better-auth.com/docs/adapters/other-relational-databases

**Contents**:
- Other Relational Databases
- Core Dialects
- Kysely Organization Dialects
- Kysely Community dialects
  - On this page

get started, concepts, and plugins

Search documentation...

Better Auth supports a wide range of database dialects out of the box thanks to Kysely.

Any dialect supported by Kysely can be utilized with Better Auth, including capabilities for generating and migrating database schemas through the CLI.

You can see the full list of supported Kysely dialects here.

---

## Other Social Providers | Better Auth

**URL**: https://www.better-auth.com/docs/authentication/other-social-providers

**Contents**:
- Other Social Providers
- Installation
  - Add the plugin to your auth config
  - Add the client plugin
- Example usage
  - Instagram Example
  - Coinbase Example
  - On this page

get started, concepts, and plugins

Search documentation...

Better Auth provides out of the box support for a Generic OAuth Plugin which allows you to use any social provider that implements the OAuth2 protocol or OpenID Connect (OIDC) flows.

To use a provider that is not supported out of the box, you can use the Generic OAuth Plugin.

To use the Generic OAuth plugin, add it to your auth config.

Include the Generic OAuth client plugin in your authentication client instance.

Read more about installation and usage of the Generic Oauth plugin here.

**Examples**:

```python
import { betterAuth } from "better-auth"
import { genericOAuth } from "better-auth/plugins"

export const auth = betterAuth({
    // ... other config options
    plugins: [
        genericOAuth({ 
            config: [ 
                { 
                    providerId: "provider-id", 
                    clientId: "test-client-id", 
                    clientSecret: "test-client-secret", 
                    discoveryUrl: "https://auth.example.com/.well-known/openid-configuration", 
           
...
```

```python
import { betterAuth } from "better-auth"
import { genericOAuth } from "better-auth/plugins"

export const auth = betterAuth({
    // ... other config options
    plugins: [
        genericOAuth({ 
            config: [ 
                { 
                    providerId: "provider-id", 
                    clientId: "test-client-id", 
                    clientSecret: "test-client-secret", 
                    discoveryUrl: "https://auth.example.com/.well-known/openid-configuration", 
           
...
```

```python
import { createAuthClient } from "better-auth/client"
import { genericOAuthClient } from "better-auth/client/plugins"

const authClient = createAuthClient({
    plugins: [
        genericOAuthClient()
    ]
})
```

---

## Passkey | Better Auth

**URL**: https://www.better-auth.com/docs/plugins/passkey

**Contents**:
- Passkey
- Installation
  - Add the plugin to your auth config
  - Migrate the database
  - Add the client plugin
- Usage
  - Add/Register a passkey
  - Sign in with a passkey

get started, concepts, and plugins

Search documentation...

Passkeys are a secure, passwordless authentication method using cryptographic key pairs, supported by WebAuthn and FIDO2 standards in web browsers. They replace passwords with unique key pairs: a private key stored on the user's device and a public key shared with the website. Users can log in using biometrics, PINs, or security keys, providing strong, phishing-resistant authentication without traditional passwords.

The passkey plugin implementation is powered by SimpleWebAuthn behind the scenes.

To add the passkey plugin to your auth config, you need to import the plugin and pass it to the plugins option of the auth instance.

rpID: A unique identifier for your website. 'localhost' is okay for local dev

rpName: Human-readable title for your website

origin: The URL at which registrations and authentications should occur. http://localhost and http://localhost:PORT are also valid. Do NOT include any trailing /

authenticatorSelection: Allows customization of WebAuthn authenticator selection criteria. Leave unspecified for default settings.

Run the migration or generate the schema to add the necessary fields and tables to the database.

See the Schema section to add the fields manually.

To add or register a passkey make sure a user is authenticated and then call the passkey.addPasskey function provided by the client.

Setting throw: true in the fetch options has no effect for the register and sign-in passkey responses — they will always return a data object containing the error object.

To sign in with a passkey you can use the signIn.passkey method. This will prompt the user to sign in with their passkey.

You can list all of the passkeys for the authenticated user by calling passkey.listUserPasskeys:

You can delete a passkey by calling passkey.delete and providing the passkey ID.

The plugin supports conditional UI, which allows the browser to autofill the passkey if the user has already registered a

*[Content truncated - see full docs]*

**Examples**:

```python
import { betterAuth } from "better-auth"
import { passkey } from "better-auth/plugins/passkey"

export const auth = betterAuth({
    plugins: [ 
        passkey(), 
    ], 
})
```

```python
import { betterAuth } from "better-auth"
import { passkey } from "better-auth/plugins/passkey"

export const auth = betterAuth({
    plugins: [ 
        passkey(), 
    ], 
})
```

```text
npx @better-auth/cli migrate
```

---

## Phone Number | Better Auth

**URL**: https://www.better-auth.com/docs/plugins/phone-number

**Contents**:
- Phone Number
- Installation
  - Add Plugin to the server
  - Migrate the database
  - Add the client plugin
- Usage
  - Send OTP for Verification
  - Verify Phone Number

get started, concepts, and plugins

Search documentation...

The phone number plugin extends the authentication system by allowing users to sign in and sign up using their phone number. It includes OTP (One-Time Password) functionality to verify phone numbers.

Run the migration or generate the schema to add the necessary fields and tables to the database.

See the Schema section to add the fields manually.

To send an OTP to a user's phone number for verification, you can use the sendVerificationCode endpoint.

After the OTP is sent, users can verify their phone number by providing the code.

When the phone number is verified, the phoneNumberVerified field in the user table is set to true. If disableSession is not set to true, a session is created for the user. Additionally, if callbackOnVerification is provided, it will be called.

To allow users to sign up using their phone number, you can pass signUpOnVerification option to your plugin configuration. It requires you to pass getTempEmail function to generate a temporary email for the user.

In addition to signing in a user using send-verify flow, you can also use phone number as an identifier and sign in a user using phone number and password.

Updating phone number uses the same process as verifying a phone number. The user will receive an OTP code to verify the new phone number.

Then verify the new phone number with the OTP code.

If a user session exist the phone number will be updated automatically.

By default, the plugin creates a session for the user after verifying the phone number. You can disable this behavior by passing disableSession: true to the verify method.

To initiate a request password reset flow using phoneNumber, you can start by calling requestPasswordReset on the client to send an OTP code to the user's phone number.

Then, you can reset the password by calling resetPassword on the client with the OTP code and the new password.

sendPasswordResetOTP: A function that sends the OTP code to t

*[Content truncated - see full docs]*

**Examples**:

```python
import { betterAuth } from "better-auth"
import { phoneNumber } from "better-auth/plugins"

const auth = betterAuth({
    plugins: [ 
        phoneNumber({  
            sendOTP: ({ phoneNumber, code }, request) => { 
                // Implement sending OTP code via SMS
            } 
        }) 
    ] 
})
```

```python
import { betterAuth } from "better-auth"
import { phoneNumber } from "better-auth/plugins"

const auth = betterAuth({
    plugins: [ 
        phoneNumber({  
            sendOTP: ({ phoneNumber, code }, request) => { 
                // Implement sending OTP code via SMS
            } 
        }) 
    ] 
})
```

```text
npx @better-auth/cli migrate
```

---

## Plugins | Better Auth

**URL**: https://www.better-auth.com/docs/concepts/plugins

**Contents**:
- Plugins
- Using a Plugin
- Creating a Plugin
  - What can a plugin do?
- Create a Server plugin
  - Endpoints
  - Schema
  - Hooks

get started, concepts, and plugins

Search documentation...

Plugins are a key part of Better Auth, they let you extend the base functionalities. You can use them to add new authentication methods, features, or customize behaviors.

Better Auth comes with many built-in plugins ready to use. Check the plugins section for details. You can also create your own plugins.

Plugins can be a server-side plugin, a client-side plugin, or both.

To add a plugin on the server, include it in the plugins array in your auth configuration. The plugin will initialize with the provided options.

Client plugins are added when creating the client. Most plugin require both server and client plugins to work correctly. The Better Auth auth client on the frontend uses the createAuthClient function provided by better-auth/client.

We recommend keeping the auth-client and your normal auth instance in separate files.

To get started, you'll need a server plugin. Server plugins are the backbone of all plugins, and client plugins are there to provide an interface with frontend APIs to easily work with your server plugins.

If your server plugins has endpoints that needs to be called from the client, you'll also need to create a client plugin.

To create a server plugin you need to pass an object that satisfies the BetterAuthPlugin interface.

The only required property is id, which is a unique identifier for the plugin. Both server and client plugins can use the same id.

You don't have to make the plugin a function, but it's recommended to do so. This way you can pass options to the plugin and it's consistent with the built-in plugins.

To add endpoints to the server, you can pass endpoints which requires an object with the key being any string and the value being an AuthEndpoint.

To create an Auth Endpoint you'll need to import createAuthEndpoint from better-auth.

Better Auth uses wraps around another library called Better Call to create endpoints. Better call is a simple ts web framework m

*[Content truncated - see full docs]*

**Examples**:

```python
import { betterAuth } from "better-auth";

export const auth = betterAuth({
    plugins: [
        // Add your plugins here
    ]
});
```

```python
import { betterAuth } from "better-auth";

export const auth = betterAuth({
    plugins: [
        // Add your plugins here
    ]
});
```

```python
import { createAuthClient } from "better-auth/client";

const authClient =  createAuthClient({
    plugins: [
        // Add your client plugins here
    ]
});
```

---

## Polar | Better Auth

**URL**: https://www.better-auth.com/docs/plugins/polar

**Contents**:
- Polar
- Features
- Installation
- Preparation
  - Configuring BetterAuth Server
  - Configuring BetterAuth Client
- Configuration Options
  - Required Options

get started, concepts, and plugins

Search documentation...

Polar is a developer first payment infrastructure. Out of the box it provides a lot of developer first integrations for payments, checkouts and more. This plugin helps you integrate Polar with Better Auth to make your auth + payments flow seamless.

This plugin is maintained by Polar team. For bugs, issues or feature requests, please visit the Polar GitHub repo.

Go to your Polar Organization Settings, and create an Organization Access Token. Add it to your environment.

The Polar plugin comes with a handful additional plugins which adds functionality to your stack.

You will be using the BetterAuth Client to interact with the Polar functionalities.

When createCustomerOnSignUp is enabled, a new Polar Customer is automatically created when a new User is added in the Better-Auth Database.

All new customers are created with an associated externalId, which is the ID of your User in the Database. This allows us to skip any Polar to User mapping in your Database.

To support checkouts in your app, simply pass the Checkout plugin to the use-property.

When checkouts are enabled, you're able to initialize Checkout Sessions using the checkout-method on the BetterAuth Client. This will redirect the user to the Product Checkout.

Checkouts will automatically carry the authenticated User as the customer to the checkout. Email-address will be "locked-in".

If authenticatedUsersOnly is false - then it will be possible to trigger checkout sessions without any associated customer.

This plugin supports the Organization plugin. If you pass the organization ID to the Checkout referenceId, you will be able to keep track of purchases made from organization members.

A plugin which enables customer management of their purchases, orders and subscriptions.

The portal-plugin gives the BetterAuth Client a set of customer management methods, scoped under authClient.customer.

The following method will redirect the user to the Po

*[Content truncated - see full docs]*

**Examples**:

```text
pnpm add better-auth @polar-sh/better-auth @polar-sh/sdk
```

```text
pnpm add better-auth @polar-sh/better-auth @polar-sh/sdk
```

```text
# .env
POLAR_ACCESS_TOKEN=...
```

---

## PostgreSQL | Better Auth

**URL**: https://www.better-auth.com/docs/adapters/postgresql

**Contents**:
- PostgreSQL
- Example Usage
- Schema generation & migration
- Use a non-default schema
- Additional Information
  - On this page

get started, concepts, and plugins

Search documentation...

PostgreSQL is a powerful, open-source relational database management system known for its advanced features, extensibility, and support for complex queries and large datasets. Read more here.

Make sure you have PostgreSQL installed and configured. Then, you can connect it straight into Better Auth.

For more information, read Kysely's documentation to the PostgresDialect.

The Better Auth CLI allows you to generate or migrate your database schema based on your Better Auth configuration and plugins.

PostgreSQL Schema Generation

PostgreSQL Schema Migration

In most cases, the default schema is public. To have Better Auth use a non-default schema (e.g., auth) for its tables, set the PostgreSQL user's default schema before generating or migrating:

alternatively, append the option to your connection URI, for example:

URL-encode if needed: ?option=-c%20search_path%3Dauth.

Ensure the target schema exists and the database user has the required permissions.

PostgreSQL is supported under the hood via the Kysely adapter, any database supported by Kysely would also be supported. (Read more here)

If you're looking for performance improvements or tips, take a look at our guide to performance optimizations.

**Examples**:

```python
import { betterAuth } from "better-auth";
import { Pool } from "pg";

export const auth = betterAuth({
  database: new Pool({
    connectionString: "postgres://user:password@localhost:5432/database",
  }),
});
```

```python
import { betterAuth } from "better-auth";
import { Pool } from "pg";

export const auth = betterAuth({
  database: new Pool({
    connectionString: "postgres://user:password@localhost:5432/database",
  }),
});
```

```text
npx @better-auth/cli@latest generate
```

---

## Rate Limit | Better Auth

**URL**: https://www.better-auth.com/docs/concepts/rate-limit

**Contents**:
- Rate Limit
- Configuring Rate Limit
  - Connecting IP Address
  - Rate Limit Window
  - Storage
- Handling Rate Limit Errors
  - Schema
  - On this page

get started, concepts, and plugins

Search documentation...

Better Auth includes a built-in rate limiter to help manage traffic and prevent abuse. By default, in production mode, the rate limiter is set to:

Server-side requests made using auth.api aren't affected by rate limiting. Rate limits only apply to client-initiated requests.

You can easily customize these settings by passing the rateLimit object to the betterAuth function.

Rate limiting is disabled in development mode by default. In order to enable it, set enabled to true:

In addition to the default settings, Better Auth provides custom rules for specific paths. For example:

In addition, plugins also define custom rules for specific paths. For example, twoFactor plugin has custom rules:

These custom rules ensure that sensitive operations are protected with stricter limits.

Rate limiting uses the connecting IP address to track the number of requests made by a user. The default header checked is x-forwarded-for, which is commonly used in production environments. If you are using a different header to track the user's IP address, you'll need to specify it.

You can also pass custom rules for specific paths.

If you like to disable rate limiting for a specific path, you can set it to false or return false from the custom rule function.

By default, rate limit data is stored in memory, which may not be suitable for many use cases, particularly in serverless environments. To address this, you can use a database, secondary storage, or custom storage for storing rate limit data.

Make sure to run migrate to create the rate limit table in your database.

Using Secondary Storage

If a Secondary Storage has been configured you can use that to store rate limit data.

If none of the above solutions suits your use case you can implement a customStorage.

When a request exceeds the rate limit, Better Auth returns the following header:

To handle rate limit errors on the client side, you can manage them either globa

*[Content truncated - see full docs]*

**Examples**:

```python
import { betterAuth } from "better-auth";

export const auth = betterAuth({
    rateLimit: {
        window: 10, // time window in seconds
        max: 100, // max requests in the window
    },
})
```

```python
import { betterAuth } from "better-auth";

export const auth = betterAuth({
    rateLimit: {
        window: 10, // time window in seconds
        max: 100, // max requests in the window
    },
})
```

```javascript
export const auth = betterAuth({
    rateLimit: {
        enabled: true,
        //...other options
    },
})
```

---

## Remix Integration | Better Auth

**URL**: https://www.better-auth.com/docs/integrations/remix

**Contents**:
- Remix Integration
- Create auth instance
- Create API Route
- Create a client
  - Example usage
    - Sign Up
    - Sign In
  - On this page

get started, concepts, and plugins

Search documentation...

Better Auth can be easily integrated with Remix. This guide will show you how to integrate Better Auth with Remix.

You can follow the steps from installation to get started or you can follow this guide to make it the Remix-way.

If you have followed the installation steps, you can skip the first step.

Create a file named auth.server.ts in one of these locations:

You can also nest any of these folders under app/ folder. (e.g. app/lib/auth.server.ts)

And in this file, import Better Auth and create your instance.

Make sure to export the auth instance with the variable name auth or as a default export.

We need to mount the handler to a API route. Create a resource route file api.auth.$.ts inside app/routes/ directory. And add the following code:

You can change the path on your better-auth configuration but it's recommended to keep it as routes/api.auth.$.ts

Create a client instance. Here we are creating auth-client.ts file inside the lib/ directory.

Once you have created the client, you can use it to sign up, sign in, and perform other actions.

**Examples**:

```python
import { betterAuth } from "better-auth"

export const auth = betterAuth({
    database: {
        provider: "postgres", //change this to your database provider
        url: process.env.DATABASE_URL, // path to your database or connection string
    }
})
```

```python
import { betterAuth } from "better-auth"

export const auth = betterAuth({
    database: {
        provider: "postgres", //change this to your database provider
        url: process.env.DATABASE_URL, // path to your database or connection string
    }
})
```

```python
import { auth } from '~/lib/auth.server' // Adjust the path as necessary
import type { LoaderFunctionArgs, ActionFunctionArgs } from "@remix-run/node"

export async function loader({ request }: LoaderFunctionArgs) {
    return auth.handler(request)
}

export async function action({ request }: ActionFunctionArgs) {
    return auth.handler(request)
}
```

---

## Resources | Better Auth

**URL**: https://www.better-auth.com/docs/reference/resources

**Contents**:
- Resources
- Video tutorials
  - The State of Authentication
  - Last Authentication You Will Ever Need
  - This Might Be My New Favourite Auth Library
  - 8 Reasons To Try Better Auth
  - Better Auth is so good that I almost switched programming languages
  - Best authentication framework for next.js

get started, concepts, and plugins

Search documentation...

A curated collection of resources to help you learn and master Better Auth. From blog posts to video tutorials, find everything you need to get started.

Theo(t3.gg) explores the current landscape of authentication, discussing trends, challenges, and where the industry is heading.

A comprehensive tutorial demonstrating why Better Auth could be the final authentication solution you'll need for your projects.

developedbyed explores the features and capabilities of Better Auth, explaining why it stands out among authentication libraries.

CJ presents 8 compelling reasons why Better Auth is the BEST auth framework he's ever used, demonstrating its superior features and ease of implementation.

Dreams of Code reviews Better Auth's features that nearly made them switch languages.

A detailed comparison of authentication frameworks for Next.js, highlighting why Better Auth might be your best choice.

An introductory overview and demonstration of Better Auth's core features and capabilities.

A tutorial on how to integrate Stripe with Better Auth.

A practical guide showing how to seamlessly integrate Better Auth with Next.js 15 for robust authentication.

Jack demonstrates how to implement headless authentication in your TanStack Start application using Better Auth, providing a modern approach to auth.

A comprehensive guide showing how to migrate your authentication from Clerk to Better Auth, with step-by-step instructions and best practices.

You'll learn how to implement authentication with Better Auth in a client - server architecture, where the frontend is separate from the backend.

Polar.sh is a platform for building payment integrations. This article will show you how to use Better Auth to authenticate your users.

Step by step guide on how to authenticate users in Astro with Better Auth.

Learn how to build multi-tenant apps with Better-Auth and ZenStack.

---

## SQLite | Better Auth

**URL**: https://www.better-auth.com/docs/adapters/sqlite

**Contents**:
- SQLite
- Example Usage
  - Better-SQLite3 (Recommended)
  - Node.js Built-in SQLite (Experimental)
  - Bun Built-in SQLite
- Schema generation & migration
- Additional Information
  - On this page

get started, concepts, and plugins

Search documentation...

SQLite is a lightweight, serverless, self-contained SQL database engine that is widely used for local data storage in applications. Read more here.

Better Auth supports multiple SQLite drivers. Choose the one that best fits your environment:

The most popular and stable SQLite driver for Node.js:

For more information, read Kysely's documentation to the SqliteDialect.

The node:sqlite module is still experimental and may change at any time. It requires Node.js 22.5.0 or later.

Starting from Node.js 22.5.0, you can use the built-in SQLite module:

To run your application with Node.js SQLite:

You can also use the built-in SQLite module in Bun, which is similar to the Node.js version:

The Better Auth CLI allows you to generate or migrate your database schema based on your Better Auth configuration and plugins.

SQLite Schema Generation

SQLite Schema Migration

SQLite is supported under the hood via the Kysely adapter, any database supported by Kysely would also be supported. (Read more here)

If you're looking for performance improvements or tips, take a look at our guide to performance optimizations.

**Examples**:

```python
import { betterAuth } from "better-auth";
import Database from "better-sqlite3";

export const auth = betterAuth({
  database: new Database("database.sqlite"),
});
```

```python
import { betterAuth } from "better-auth";
import Database from "better-sqlite3";

export const auth = betterAuth({
  database: new Database("database.sqlite"),
});
```

```python
import { betterAuth } from "better-auth";
import { DatabaseSync } from "node:sqlite";

export const auth = betterAuth({
  database: new DatabaseSync("database.sqlite"),
});
```

---

## Session Management | Better Auth

**URL**: https://www.better-auth.com/docs/concepts/session-management

**Contents**:
- Session Management
- Session table
- Session Expiration
  - Disable Session Refresh
- Session Freshness
- Session Management
  - Get Session
  - Use Session

get started, concepts, and plugins

Search documentation...

Better Auth manages session using a traditional cookie-based session management. The session is stored in a cookie and is sent to the server on every request. The server then verifies the session and returns the user data if the session is valid.

The session table stores the session data. The session table has the following fields:

The session expires after 7 days by default. But whenever the session is used and the updateAge is reached, the session expiration is updated to the current time plus the expiresIn value.

You can change both the expiresIn and updateAge values by passing the session object to the auth configuration.

You can disable session refresh so that the session is not updated regardless of the updateAge option.

Some endpoints in Better Auth require the session to be fresh. A session is considered fresh if its createdAt is within the freshAge limit. By default, the freshAge is set to 1 day (60 * 60 * 24).

You can customize the freshAge value by passing a session object in the auth configuration:

To disable the freshness check, set freshAge to 0:

Better Auth provides a set of functions to manage sessions.

The getSession function retrieves the current active session.

To learn how to customize the session response check the Customizing Session Response section.

The useSession action provides a reactive way to access the current session.

The listSessions function returns a list of sessions that are active for the user.

When a user signs out of a device, the session is automatically ended. However, you can also end a session manually from any device the user is signed into.

To end a session, use the revokeSession function. Just pass the session token as a parameter.

To revoke all other sessions except the current session, you can use the revokeOtherSessions function.

To revoke all sessions, you can use the revokeSessions function.

You can revoke all sessions when the user changes

*[Content truncated - see full docs]*

**Examples**:

```python
import { betterAuth } from "better-auth"

export const auth = betterAuth({
    //... other config options
    session: {
        expiresIn: 60 * 60 * 24 * 7, // 7 days
        updateAge: 60 * 60 * 24 // 1 day (every 1 day the session expiration is updated)
    }
})
```

```python
import { betterAuth } from "better-auth"

export const auth = betterAuth({
    //... other config options
    session: {
        expiresIn: 60 * 60 * 24 * 7, // 7 days
        updateAge: 60 * 60 * 24 // 1 day (every 1 day the session expiration is updated)
    }
})
```

```python
import { betterAuth } from "better-auth"

export const auth = betterAuth({
    //... other config options
    session: {
        disableSessionRefresh: true
    }
})
```

---

## Single Sign-On (SSO) | Better Auth

**URL**: https://www.better-auth.com/docs/plugins/sso

**Contents**:
- Single Sign-On (SSO)
- Installation
  - Install the plugin
  - Add Plugin to the server
  - Migrate the database
  - Add the client plugin
- Usage
  - Register an OIDC Provider

get started, concepts, and plugins

Search documentation...

Single Sign-On (SSO) allows users to authenticate with multiple applications using a single set of credentials. This plugin supports OpenID Connect (OIDC), OAuth2 providers, and SAML 2.0.

Run the migration or generate the schema to add the necessary fields and tables to the database.

See the Schema section to add the fields manually.

To register an OIDC provider, use the registerSSOProvider endpoint and provide the necessary configuration details for the provider.

A redirect URL will be automatically generated using the provider ID. For instance, if the provider ID is hydra, the redirect URL would be {baseURL}/api/auth/sso/callback/hydra. Note that /api/auth may vary depending on your base path configuration.

To register a SAML provider, use the registerSSOProvider endpoint with SAML configuration details. The provider will act as a Service Provider (SP) and integrate with your Identity Provider (IdP).

For SAML providers, you can retrieve the Service Provider metadata XML that needs to be configured in your Identity Provider:

To sign in with an SSO provider, you can call signIn.sso

You can sign in using the email with domain matching:

or you can specify the domain:

You can also sign in using the organization slug if a provider is associated with an organization:

Alternatively, you can sign in using the provider's ID:

To use the server API you can use signInSSO

When a user is authenticated, if the user does not exist, the user will be provisioned using the provisionUser function. If the organization provisioning is enabled and a provider is associated with an organization, the user will be added to the organization.

The SSO plugin provides powerful provisioning capabilities to automatically set up users and manage their organization memberships when they sign in through SSO providers.

User provisioning allows you to run custom logic whenever a user signs in through an SSO provider. This is us

*[Content truncated - see full docs]*

**Examples**:

```text
npm install @better-auth/sso
```

```text
npm install @better-auth/sso
```

```python
import { betterAuth } from "better-auth"
import { sso } from "@better-auth/sso";

const auth = betterAuth({
    plugins: [ 
        sso() 
    ] 
})
```

---

## SolidStart Integration | Better Auth

**URL**: https://www.better-auth.com/docs/integrations/solid-start

**Contents**:
- SolidStart Integration
  - Mount the handler
  - On this page

get started, concepts, and plugins

Search documentation...

Before you start, make sure you have a Better Auth instance configured. If you haven't done that yet, check out the installation.

We need to mount the handler to SolidStart server. Put the following code in your *auth.ts file inside /routes/api/auth folder.

**Examples**:

```python
import { auth } from "~/lib/auth";
import { toSolidStartHandler } from "better-auth/solid-start";

export const { GET, POST } = toSolidStartHandler(auth);
```

```python
import { auth } from "~/lib/auth";
import { toSolidStartHandler } from "better-auth/solid-start";

export const { GET, POST } = toSolidStartHandler(auth);
```

---

## Stripe | Better Auth

**URL**: https://www.better-auth.com/docs/plugins/stripe

**Contents**:
- Stripe
- Features
- Installation
  - Install the plugin
  - Install the Stripe SDK
  - Add the plugin to your auth config
  - Add the client plugin
  - Migrate the database

get started, concepts, and plugins

Search documentation...

The Stripe plugin integrates Stripe's payment and subscription functionality with Better Auth. Since payment and authentication are often tightly coupled, this plugin simplifies the integration of Stripe into your application, handling customer creation, subscription management, and webhook processing.

First, install the plugin:

If you're using a separate client and server setup, make sure to install the plugin in both parts of your project.

Next, install the Stripe SDK on your server:

Upgrading from Stripe v18? Version 19 uses async webhook signature verification (constructEventAsync) which is handled internally by the plugin. No code changes required on your end!

Run the migration or generate the schema to add the necessary tables to the database.

See the Schema section to add the tables manually.

Create a webhook endpoint in your Stripe dashboard pointing to:

/api/auth is the default path for the auth server.

Make sure to select at least these events:

Save the webhook signing secret provided by Stripe and add it to your environment variables as STRIPE_WEBHOOK_SECRET.

You can use this plugin solely for customer management without enabling subscriptions. This is useful if you just want to link Stripe customers to your users.

By default, when a user signs up, a Stripe customer is automatically created if you set createCustomerOnSignUp: true. This customer is linked to the user in your database. You can customize the customer creation process:

You can define your subscription plans either statically or dynamically:

see plan configuration for more.

To create a subscription, use the subscription.upgrade method:

This will create a Checkout Session and redirect the user to the Stripe Checkout page.

If the user already has an active subscription, you must provide the subscriptionId parameter. Otherwise, the user will be subscribed to (and pay for) both plans.

Important: The successUrl parameter

*[Content truncated - see full docs]*

**Examples**:

```text
npm install @better-auth/stripe
```

```text
npm install @better-auth/stripe
```

```text
npm install stripe@^19.1.0
```

---

## SvelteKit Integration | Better Auth

**URL**: https://www.better-auth.com/docs/integrations/svelte-kit

**Contents**:
- SvelteKit Integration
  - Mount the handler
  - Populate session data in the event (event.locals)
  - Server Action Cookies
- Create a client
  - Example usage
  - On this page

get started, concepts, and plugins

Search documentation...

Before you start, make sure you have a Better Auth instance configured. If you haven't done that yet, check out the installation.

We need to mount the handler to SvelteKit server hook.

The svelteKitHandler does not automatically populate event.locals.user or event.locals.session. If you want to access the current session in your server code (e.g., in +layout.server.ts, actions, or endpoints), populate event.locals in your handle hook:

To ensure cookies are properly set when you call functions like signInEmail or signUpEmail in a server action, you should use the sveltekitCookies plugin. This plugin will automatically handle setting cookies for you in SvelteKit.

You need to add it as a plugin to your Better Auth instance.

The getRequestEvent function is available in SvelteKit 2.20.0 and later. Make sure you are using a compatible version.

Create a client instance. You can name the file anything you want. Here we are creating client.ts file inside the lib/ directory.

Once you have created the client, you can use it to sign up, sign in, and perform other actions. Some of the actions are reactive. The client use nano-store to store the state and reflect changes when there is a change like a user signing in or out affecting the session state.

**Examples**:

```python
import { auth } from "$lib/auth";
import { svelteKitHandler } from "better-auth/svelte-kit";
import { building } from "$app/environment";

export async function handle({ event, resolve }) {
  return svelteKitHandler({ event, resolve, auth, building });
}
```

```python
import { auth } from "$lib/auth";
import { svelteKitHandler } from "better-auth/svelte-kit";
import { building } from "$app/environment";

export async function handle({ event, resolve }) {
  return svelteKitHandler({ event, resolve, auth, building });
}
```

```python
import { auth } from "$lib/auth";
import { svelteKitHandler } from "better-auth/svelte-kit";
import { building } from "$app/environment";

export async function handle({ event, resolve }) {
  // Fetch current session from Better Auth
  const session = await auth.api.getSession({
    headers: event.request.headers,
  });

  // Make session and user available on server
  if (session) {
    event.locals.session = session.session;
    event.locals.user = session.user;
  }

  return svelteKitHandler(
...
```

---

## TanStack Start Integration | Better Auth

**URL**: https://www.better-auth.com/docs/integrations/tanstack

**Contents**:
- TanStack Start Integration
  - Mount the handler
  - Usage tips
  - On this page

get started, concepts, and plugins

Search documentation...

This integration guide is assuming you are using TanStack Start.

Before you start, make sure you have a Better Auth instance configured. If you haven't done that yet, check out the installation.

We need to mount the handler to a TanStack API endpoint/Server Route. Create a new file: /src/routes/api/auth/$.ts

If you haven't created your server route handler yet, you can do so by creating a file: /src/server.ts

Now, when you call functions that set cookies, they will be automatically set using TanStack Start's cookie handling system.

**Examples**:

```python
import { auth } from '@/lib/auth'
import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/api/auth/$')({
  server: {
    handlers: {
      GET: ({ request }) => {
        return auth.handler(request)
      },
      POST: ({ request }) => {
        return auth.handler(request)
      },
    },
  },
})
```

```python
import { auth } from '@/lib/auth'
import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/api/auth/$')({
  server: {
    handlers: {
      GET: ({ request }) => {
        return auth.handler(request)
      },
      POST: ({ request }) => {
        return auth.handler(request)
      },
    },
  },
})
```

```python
import {
  createStartHandler,
  defaultStreamHandler,
} from '@tanstack/react-start/server'
import { createRouter } from './router'

export default createStartHandler({
  createRouter,
})(defaultStreamHandler)
```

---

## Telemetry | Better Auth

**URL**: https://www.better-auth.com/docs/reference/telemetry

**Contents**:
- Telemetry
- Why is telemetry collected?
- What is being collected?
- How is my data protected?
- How can I enable it?
  - When is telemetry sent?
  - On this page

get started, concepts, and plugins

Search documentation...

Better Auth collects anonymous usage data to help us improve the project. This is optional, transparent, and disabled by default.

Since v1.3.5, Better Auth collects anonymous telemetry data about general usage if enabled.

Telemetry data helps us understand how Better Auth is being used across different environments so we can improve performance, prioritize features, and fix issues more effectively. It guides our decisions on performance optimizations, feature development, and bug fixes. All data is collected completely anonymously and with privacy in mind, and users can opt out at any time. We strive to keep what we collect as transparent as possible.

The following data points may be reported. Everything is anonymous and intended for aggregate insights only.

We also collect anonymous telemetry from the CLI:

You can audit telemetry locally by setting the BETTER_AUTH_TELEMETRY_DEBUG=1 environment variable when running your project or by setting telemetry: { debug: true } in your auth config. In this debug mode, telemetry events are logged only to the console.

All collected data is fully anonymous and only useful in aggregate. It cannot be traced back to any individual source and is accessible only to a small group of core Better Auth maintainers to guide roadmap decisions.

You can enable telemetry collection in your auth config or by setting an environment variable.

Via your auth config.

Via an environment variable.

Telemetry is disabled automatically in tests (NODE_ENV=test) unless explicitly overridden by internal tooling.

**Examples**:

```javascript
export const auth = betterAuth({
  telemetry: { 
    debug: true
  } 
});
```

```javascript
export const auth = betterAuth({
  telemetry: { 
    debug: true
  } 
});
```

```javascript
export const auth = betterAuth({
  telemetry: { 
    enabled: true
  } 
});
```

---

## Two-Factor Authentication (2FA) | Better Auth

**URL**: https://www.better-auth.com/docs/plugins/2fa

**Contents**:
- Two-Factor Authentication (2FA)
- Installation
  - Add the plugin to your auth config
  - Migrate the database
  - Add the client plugin
- Usage
  - Enabling 2FA
  - Sign In with 2FA

get started, concepts, and plugins

Search documentation...

OTP TOTP Backup Codes Trusted Devices

Two-Factor Authentication (2FA) adds an extra security step when users log in. Instead of just using a password, they'll need to provide a second form of verification. This makes it much harder for unauthorized people to access accounts, even if they've somehow gotten the password.

This plugin offers two main methods to do a second factor verification:

Additional features include:

Add the two-factor plugin to your auth configuration and specify your app name as the issuer.

Run the migration or generate the schema to add the necessary fields and tables to the database.

See the Schema section to add the fields manually.

Add the client plugin and Specify where the user should be redirected if they need to verify 2nd factor

To enable two-factor authentication, call twoFactor.enable with the user's password and issuer (optional):

Note: twoFactorEnabled won’t be set to true until the user verifies their TOTP code. Learn more about veryifying TOTP here. You can skip verification by setting skipVerificationOnEnable to true in your plugin config.

Two Factor can only be enabled for credential accounts at the moment. For social accounts, it's assumed the provider already handles 2FA.

When a user with 2FA enabled tries to sign in via email, the response object will contain twoFactorRedirect set to true. This indicates that the user needs to verify their 2FA code.

You can handle this in the onSuccess callback or by providing a onTwoFactorRedirect callback in the plugin config.

Using the onTwoFactorRedirect config:

When you call auth.api.signInEmail on the server, and the user has 2FA enabled, it will return an object where twoFactorRedirect is set to true. This behavior isn’t inferred in TypeScript, which can be misleading. You can check using in instead to check if twoFactorRedirect is set to true.

To disable two-factor authentication, call twoFactor.disable with th

*[Content truncated - see full docs]*

**Examples**:

```python
import { betterAuth } from "better-auth"
import { twoFactor } from "better-auth/plugins"

export const auth = betterAuth({
    // ... other config options
    appName: "My App", // provide your app name. It'll be used as an issuer.
    plugins: [
        twoFactor() 
    ]
})
```

```python
import { betterAuth } from "better-auth"
import { twoFactor } from "better-auth/plugins"

export const auth = betterAuth({
    // ... other config options
    appName: "My App", // provide your app name. It'll be used as an issuer.
    plugins: [
        twoFactor() 
    ]
})
```

```text
npx @better-auth/cli migrate
```

---

## TypeScript | Better Auth

**URL**: https://www.better-auth.com/docs/concepts/typescript

**Contents**:
- TypeScript
- TypeScript Config
  - Strict Mode
- Inferring Types
- Additional Fields
  - The input property
  - Inferring Additional Fields on Client
  - On this page

get started, concepts, and plugins

Search documentation...

Better Auth is designed to be type-safe. Both the client and server are built with TypeScript, allowing you to easily infer types.

Better Auth is designed to work with TypeScript's strict mode. We recommend enabling strict mode in your TypeScript config file:

if you can't set strict to true, you can enable strictNullChecks:

If you're running into issues with TypeScript inference exceeding maximum length the compiler will serialize, then please make sure you're following the instructions above, as well as ensuring that both declaration and composite are not enabled.

Both the client SDK and the server offer types that can be inferred using the $Infer property. Plugins can extend base types like User and Session, and you can use $Infer to infer these types. Additionally, plugins can provide extra types that can also be inferred through $Infer.

The Session type includes both session and user properties. The user property represents the user object type, and the session property represents the session object type.

You can also infer types on the server side.

Better Auth allows you to add additional fields to the user and session objects. All additional fields are properly inferred and available on the server and client side.

In the example above, we added a role field to the user object. This field is now available on the Session type.

The input property in an additional field configuration determines whether the field should be included in the user input. This property defaults to true, meaning the field will be part of the user input during operations like registration.

To prevent a field from being part of the user input, you must explicitly set input: false:

When input is set to false, the field will be excluded from user input, preventing users from passing a value for it.

By default, additional fields are included in the user input, which can lead to security vulnerabilities if not handled car

*[Content truncated - see full docs]*

**Examples**:

```text
{
  "compilerOptions": {
    "strict": true
  }
}
```

```text
{
  "compilerOptions": {
    "strict": true
  }
}
```

```text
{
  "compilerOptions": {
    "strictNullChecks": true,
  }
}
```

---

## User & Accounts | Better Auth

**URL**: https://www.better-auth.com/docs/concepts/users-accounts

**Contents**:
- User & Accounts
- Update User
  - Update User Information
  - Change Email
  - Change Password
  - Set Password
- Delete User
  - Adding Verification Before Deletion

get started, concepts, and plugins

Search documentation...

Beyond authenticating users, Better Auth also provides a set of methods to manage users. This includes, updating user information, changing passwords, and more.

The user table stores the authentication data of the user Click here to view the schema.

The user table can be extended using additional fields or by plugins to store additional data.

To update user information, you can use the updateUser function provided by the client. The updateUser function takes an object with the following properties:

To allow users to change their email, first enable the changeEmail feature, which is disabled by default. Set changeEmail.enabled to true:

For users with a verified email, provide the sendChangeEmailVerification function. This function triggers when a user changes their email, sending a verification email with a URL and token. If the current email isn't verified, the change happens immediately without verification.

Once enabled, use the changeEmail function on the client to update a user’s email. The user must verify their current email before changing it.

After verification, the new email is updated in the user table, and a confirmation is sent to the new address.

If the current email is unverified, the new email is updated without the verification step.

A user's password isn't stored in the user table. Instead, it's stored in the account table. To change the password of a user, you can use one of the following approaches:

If a user was registered using OAuth or other providers, they won't have a password or a credential account. In this case, you can use the setPassword action to set a password for the user. For security reasons, this function can only be called from the server. We recommend having users go through a 'forgot password' flow to set a password for their account.

Better Auth provides a utility to hard delete a user from your database. It's disabled by default, but you can enable it easi

*[Content truncated - see full docs]*

**Examples**:

```text
await authClient.updateUser({
    image: "https://example.com/image.jpg",
    name: "John Doe",
})
```

```text
await authClient.updateUser({
    image: "https://example.com/image.jpg",
    name: "John Doe",
})
```

```javascript
export const auth = betterAuth({
    user: {
        changeEmail: {
            enabled: true,
        }
    }
})
```

---

## Username | Better Auth

**URL**: https://www.better-auth.com/docs/plugins/username

**Contents**:
- Username
- Installation
  - Add Plugin to the server
  - Migrate the database
  - Add the client plugin
- Usage
  - Sign up
  - Sign in

get started, concepts, and plugins

Search documentation...

The username plugin is a lightweight plugin that adds username support to the email and password authenticator. This allows users to sign in and sign up with their username instead of their email.

Run the migration or generate the schema to add the necessary fields and tables to the database.

See the Schema section to add the fields manually.

To sign up a user with username, you can use the existing signUp.email function provided by the client. The signUp function should take a new username property in the object.

If only username is provided, the displayUsername will be set to the pre normalized version of the username. You can see the Username Normalization and Display Username Normalization sections for more details.

To sign in a user with username, you can use the signIn.username function provided by the client.

To update the username of a user, you can use the updateUser function provided by the client.

To check if a username is available, you can use the isUsernameAvailable function provided by the client.

The minimum length of the username. Default is 3.

The maximum length of the username. Default is 30.

A function that validates the username. The function should return false if the username is invalid. By default, the username should only contain alphanumeric characters, underscores, and dots.

A function that validates the display username. The function should return false if the display username is invalid. By default, no validation is applied to display username.

A function that normalizes the username, or false if you want to disable normalization.

By default, usernames are normalized to lowercase, so "TestUser" and "testuser", for example, are considered the same username. The username field will contain the normalized (lower case) username, while displayUsername will contain the original username.

A function that normalizes the display username, or false to disable normalization.

*[Content truncated - see full docs]*

**Examples**:

```python
import { betterAuth } from "better-auth"
import { username } from "better-auth/plugins"

export const auth = betterAuth({
    plugins: [ 
        username() 
    ] 
})
```

```python
import { betterAuth } from "better-auth"
import { username } from "better-auth/plugins"

export const auth = betterAuth({
    plugins: [ 
        username() 
    ] 
})
```

```text
npx @better-auth/cli migrate
```

---
