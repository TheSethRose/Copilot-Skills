# Better-Auth - Configuration

**Pages**: 12

---

## API Key | Better Auth

**URL**: https://www.better-auth.com/docs/plugins/api-key

**Contents**:
- API Key
- Features
- Installation
  - Add Plugin to the server
  - Migrate the database
  - Add the client plugin
- Usage
  - Create an API key

get started, concepts, and plugins

Search documentation...

The API Key plugin allows you to create and manage API keys for your application. It provides a way to authenticate and authorize API requests by verifying API keys.

Run the migration or generate the schema to add the necessary fields and tables to the database.

See the Schema section to add the fields manually.

You can view the list of API Key plugin options here.

You can adjust more specific API key configurations by using the server method instead.

If you're creating an API key on the server, without access to headers, you must pass the userId property. This is the ID of the user that the API key is associated with.

It'll return the ApiKey object which includes the key value for you to use. Otherwise if it throws, it will throw an APIError.

You'll receive everything about the API key details, except for the key value itself. If it fails, it will throw an APIError.

If fails, throws APIError. Otherwise, you'll receive the API Key details, except for the key value itself.

This endpoint is attempting to delete the API key from the perspective of the user. It will check if the user's ID matches the key owner to be able to delete it. If you want to delete a key without these checks, we recommend you use an ORM to directly mutate your DB instead.

This endpoint is attempting to delete the API key from the perspective of the user. It will check if the user's ID matches the key owner to be able to delete it. If you want to delete a key without these checks, we recommend you use an ORM to directly mutate your DB instead.

If fails, throws APIError. Otherwise, you'll receive:

If fails, throws APIError. Otherwise, you'll receive:

This function will delete all API keys that have an expired expiration date.

We automatically delete expired API keys every time any apiKey plugin endpoints were called, however they are rate-limited to a 10 second cool down each call to prevent multiple calls to the database.


*[Content truncated - see full docs]*

**Examples**:

```python
import { betterAuth } from "better-auth"
import { apiKey } from "better-auth/plugins"

export const auth = betterAuth({
    plugins: [ 
        apiKey() 
    ] 
})
```

```python
import { betterAuth } from "better-auth"
import { apiKey } from "better-auth/plugins"

export const auth = betterAuth({
    plugins: [ 
        apiKey() 
    ] 
})
```

```text
npx @better-auth/cli migrate
```

---

## Anonymous | Better Auth

**URL**: https://www.better-auth.com/docs/plugins/anonymous

**Contents**:
- Anonymous
- Installation
  - Add the plugin to your auth config
  - Migrate the database
  - Add the client plugin
- Usage
  - Sign In
  - Link Account

get started, concepts, and plugins

Search documentation...

The Anonymous plugin allows users to have an authenticated experience without requiring them to provide an email address, password, OAuth provider, or any other Personally Identifiable Information (PII). Users can later link an authentication method to their account when ready.

To enable anonymous authentication, add the anonymous plugin to your authentication configuration.

Run the migration or generate the schema to add the necessary fields and tables to the database.

See the Schema section to add the fields manually.

Next, include the anonymous client plugin in your authentication client instance.

To sign in a user anonymously, use the signIn.anonymous() method.

If a user is already signed in anonymously and tries to signIn or signUp with another method, their anonymous activities can be linked to the new account.

To do that you first need to provide onLinkAccount callback to the plugin.

Then when you call signIn or signUp with another method, the onLinkAccount callback will be called. And the anonymousUser will be deleted by default.

onLinkAccount: A callback function that is called when an anonymous user links their account to a new authentication method. The callback receives an object with the anonymousUser and the newUser.

disableDeleteAnonymousUser: By default, the anonymous user is deleted when the account is linked to a new authentication method. Set this option to true to disable this behavior.

generateName: A callback function that is called to generate a name for the anonymous user. Useful if you want to have random names for anonymous users, or if name is unique in your database.

The anonymous plugin requires an additional field in the user table:

**Examples**:

```python
import { betterAuth } from "better-auth"
import { anonymous } from "better-auth/plugins"

export const auth = betterAuth({
    // ... other config options
    plugins: [
        anonymous() 
    ]
})
```

```python
import { betterAuth } from "better-auth"
import { anonymous } from "better-auth/plugins"

export const auth = betterAuth({
    // ... other config options
    plugins: [
        anonymous() 
    ]
})
```

```text
npx @better-auth/cli migrate
```

---

## Create a Database Adapter | Better Auth

**URL**: https://www.better-auth.com/docs/guides/create-a-db-adapter

**Contents**:
- Create a Database Adapter
- Quick Start
  - Get things ready
  - Configure the adapter
  - Create the adapter
- Adapter
  - Adapter Methods
  - create method

get started, concepts, and plugins

Search documentation...

Learn how to create a custom database adapter for Better-Auth using createAdapter.

Our createAdapter function is designed to be very flexible, and we've done our best to make it easy to understand and use. Our hope is to allow you to focus on writing database logic, and not have to worry about how the adapter is working with Better-Auth.

Anything from custom schema configurations, custom ID generation, safe JSON parsing, and more is handled by the createAdapter function. All you need to do is provide the database logic, and the createAdapter function will handle the rest.

The config object is mostly used to provide information about the adapter to Better-Auth. We try to minimize the amount of code you need to write in your adapter functions, and these config options are used to help us do that.

The adapter function is where you write the code that interacts with your database.

Learn more about the adapter here here.

The adapter function is where you write the code that interacts with your database.

If you haven't already, check out the options object in the config section, as it can be useful for your adapter.

Before we get into the adapter function, let's go over the parameters that are available to you.

The create method is used to create a new record in the database.

Note: If the user has enabled the useNumberId option, or if generateId is false in the user's Better Auth config, then it's expected that the id is provided in the data object. Otherwise, the id will be automatically generated.

Additionally, it's possible to pass forceAllowId as a parameter to the create method, which allows id to be provided in the data object. We handle forceAllowId internally, so you don't need to worry about it.

Make sure to return the data that is inserted into the database.

The update method is used to update a record in the database.

Make sure to return the data in the row which is updated. This include

*[Content truncated - see full docs]*

**Examples**:

```python
import { createAdapter, type DBAdapterDebugLogOption } from "better-auth/adapters";

// Your custom adapter config options
interface CustomAdapterConfig {
  /**
   * Helps you debug issues with the adapter.
   */
  debugLogs?: DBAdapterDebugLogOption;
  /**
   * If the table names in the schema are plural.
   */
  usePlural?: boolean;
}

export const myAdapter = (config: CustomAdapterConfig = {}) =>
  createAdapter({
    // ...
  });
```

```python
import { createAdapter, type DBAdapterDebugLogOption } from "better-auth/adapters";

// Your custom adapter config options
interface CustomAdapterConfig {
  /**
   * Helps you debug issues with the adapter.
   */
  debugLogs?: DBAdapterDebugLogOption;
  /**
   * If the table names in the schema are plural.
   */
  usePlural?: boolean;
}

export const myAdapter = (config: CustomAdapterConfig = {}) =>
  createAdapter({
    // ...
  });
```

```javascript
// ...
export const myAdapter = (config: CustomAdapterConfig = {}) =>
  createAdapter({
    config: {
      adapterId: "custom-adapter", // A unique identifier for the adapter.
      adapterName: "Custom Adapter", // The name of the adapter.
      usePlural: config.usePlural ?? false, // Whether the table names in the schema are plural.
      debugLogs: config.debugLogs ?? false, // Whether to enable debug logs.
      supportsJSON: false, // Whether the database supports JSON. (Default: false)
 
...
```

---

## MCP | Better Auth

**URL**: https://www.better-auth.com/docs/plugins/mcp

**Contents**:
- MCP
- Installation
  - Add the Plugin
  - Generate Schema
- Usage
  - OAuth Discovery Metadata
  - OAuth Protected Resource Metadata
  - MCP Session Handling

get started, concepts, and plugins

Search documentation...

The MCP plugin lets your app act as an OAuth provider for MCP clients. It handles authentication and makes it easy to issue and manage access tokens for MCP applications.

Add the MCP plugin to your auth configuration and specify the login page path.

This doesn't have a client plugin, so you don't need to make any changes to your authClient.

Run the migration or generate the schema to add the necessary fields and tables to the database.

The MCP plugin uses the same schema as the OIDC Provider plugin. See the OIDC Provider Schema section for details.

Better Auth already handles the /api/auth/.well-known/oauth-authorization-server route automatically but some client may fail to parse the WWW-Authenticate header and default to /.well-known/oauth-authorization-server (this can happen, for example, if your CORS configuration doesn't expose the WWW-Authenticate). For this reason it's better to add a route to expose OAuth metadata for MCP clients:

Better Auth already handles the /api/auth/.well-known/oauth-protected-resource route automatically but some client may fail to parse the WWW-Authenticate header and default to /.well-known/oauth-protected-resource (this can happen, for example, if your CORS configuration doesn't expose the WWW-Authenticate). For this reason it's better to add a route to expose OAuth metadata for MCP clients:

You can use the helper function withMcpAuth to get the session and handle unauthenticated calls automatically.

You can also use auth.api.getMcpSession to get the session using the access token sent from the MCP client:

The MCP plugin accepts the following configuration options:

The plugin supports additional OIDC configuration options through the oidcConfig parameter:

The MCP plugin uses the same schema as the OIDC Provider plugin. See the OIDC Provider Schema section for details.

**Examples**:

```python
import { betterAuth } from "better-auth";
import { mcp } from "better-auth/plugins";

export const auth = betterAuth({
    plugins: [
        mcp({
            loginPage: "/sign-in" // path to your login page
        })
    ]
});
```

```python
import { betterAuth } from "better-auth";
import { mcp } from "better-auth/plugins";

export const auth = betterAuth({
    plugins: [
        mcp({
            loginPage: "/sign-in" // path to your login page
        })
    ]
});
```

```text
npx @better-auth/cli migrate
```

---

## Migrating from Supabase Auth to Better Auth | Better Auth

**URL**: https://www.better-auth.com/docs/guides/supabase-migration-guide

**Contents**:
- Migrating from Supabase Auth to Better Auth
- Before You Begin
  - Connect to your database
  - Enable Email and Password (Optional)
  - Setup Social Providers (Optional)
  - Add admin and anonymous plugins (Optional)
  - Run the migration
  - Copy the migration script

get started, concepts, and plugins

Search documentation...

In this guide, we'll walk through the steps to migrate a project from Supabase Auth to Better Auth.

This migration will invalidate all active sessions. While this guide doesn't currently cover migrating two-factor (2FA) or Row Level Security (RLS) configurations, both should be possible with additional steps.

Before starting the migration process, set up Better Auth in your project. Follow the installation guide to get started.

You'll need to connect to your database to migrate the users and accounts. Copy your DATABASE_URL from your Supabase project and use it to connect to your database. And for this example, we'll need to install pg to connect to the database.

And then you can use the following code to connect to your database.

Enable the email and password in your auth config.

Add social providers you have enabled in your Supabase project in your auth config.

Add the admin and anonymous plugins to your auth config.

Run the migration to create the necessary tables in your database.

This will create the following tables in your database:

This tables will be created on the public schema.

Now that we have the necessary tables in our database, we can run the migration script to migrate the users and accounts from Supabase to Better Auth.

Start by creating a .ts file in your project.

And then copy and paste the following code into the file.

Run the migration script to migrate the users and accounts from Supabase to Better Auth.

By default, Better Auth uses the scrypt algorithm to hash passwords. Since Supabase uses bcrypt, you'll need to configure Better Auth to use bcrypt for password verification.

First, install bcrypt:

Then update your auth configuration:

Update your codebase from Supabase auth calls to Better Auth API.

Here's a list of the Supabase auth API calls and their Better Auth counterparts.

To protect routes with middleware, refer to the Next.js middleware guide or your framew

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

## Next.js integration | Better Auth

**URL**: https://www.better-auth.com/docs/integrations/next

**Contents**:
- Next.js integration
  - Create API Route
- Create a client
- RSC and Server actions
  - Server Action Cookies
- Middleware
  - How to handle auth checks in each page/route
  - For Next.js release 15.1.7 and below

get started, concepts, and plugins

Search documentation...

Better Auth can be easily integrated with Next.js. Before you start, make sure you have a Better Auth instance configured. If you haven't done that yet, check out the installation.

We need to mount the handler to an API route. Create a route file inside /api/auth/[...all] directory. And add the following code:

You can change the path on your better-auth configuration but it's recommended to keep it as /api/auth/[...all]

For pages route, you need to use toNodeHandler instead of toNextJsHandler and set bodyParser to false in the config object. Here is an example:

Create a client instance. You can name the file anything you want. Here we are creating client.ts file inside the lib/ directory.

Once you have created the client, you can use it to sign up, sign in, and perform other actions. Some of the actions are reactive. The client uses nano-store to store the state and re-render the components when the state changes.

The client also uses better-fetch to make the requests. You can pass the fetch configuration to the client.

The api object exported from the auth instance contains all the actions that you can perform on the server. Every endpoint made inside Better Auth is a invocable as a function. Including plugins endpoints.

Example: Getting Session on a server action

Example: Getting Session on a RSC

When you call a function that needs to set cookies, like signInEmail or signUpEmail in a server action, cookies won’t be set. This is because server actions need to use the cookies helper from Next.js to set cookies.

To simplify this, you can use the nextCookies plugin, which will automatically set cookies for you whenever a Set-Cookie header is present in the response.

Now, when you call functions that set cookies, they will be automatically set.

In Next.js middleware, it's recommended to only check for the existence of a session cookie to handle redirection. To avoid blocking requests by making AP

*[Content truncated - see full docs]*

**Examples**:

```python
import { auth } from "@/lib/auth";
import { toNextJsHandler } from "better-auth/next-js";

export const { GET, POST } = toNextJsHandler(auth.handler);
```

```python
import { auth } from "@/lib/auth";
import { toNextJsHandler } from "better-auth/next-js";

export const { GET, POST } = toNextJsHandler(auth.handler);
```

```python
import { toNodeHandler } from "better-auth/node"
import { auth } from "@/lib/auth"

// Disallow body parsing, we will parse it manually
export const config = { api: { bodyParser: false } }

export default toNodeHandler(auth.handler)
```

---

## Nuxt Integration | Better Auth

**URL**: https://www.better-auth.com/docs/integrations/nuxt

**Contents**:
- Nuxt Integration
  - Create API Route
  - Migrate the database
- Create a client
  - Example usage
  - Server Usage
  - SSR Usage
  - Middleware

get started, concepts, and plugins

Search documentation...

Before you start, make sure you have a Better Auth instance configured. If you haven't done that yet, check out the installation.

We need to mount the handler to an API route. Create a file inside /server/api/auth called [...all].ts and add the following code:

You can change the path on your better-auth configuration but it's recommended to keep it as /api/auth/[...all]

Run the following command to create the necessary tables in your database:

Create a client instance. You can name the file anything you want. Here we are creating client.ts file inside the lib/ directory.

Once you have created the client, you can use it to sign up, sign in, and perform other actions. Some of the actions are reactive.

The api object exported from the auth instance contains all the actions that you can perform on the server. Every endpoint made inside Better Auth is a invocable as a function. Including plugins endpoints.

Example: Getting Session on a server API route

If you are using Nuxt with SSR, you can use the useSession function in the setup function of your page component and pass useFetch to make it work with SSR.

To add middleware to your Nuxt project, you can use the useSession method from the client.

**Examples**:

```python
import { auth } from "~/lib/auth"; // import your auth config

export default defineEventHandler((event) => {
	return auth.handler(toWebRequest(event));
});
```

```python
import { auth } from "~/lib/auth"; // import your auth config

export default defineEventHandler((event) => {
	return auth.handler(toWebRequest(event));
});
```

```text
npx @better-auth/cli migrate
```

---

## One Tap | Better Auth

**URL**: https://www.better-auth.com/docs/plugins/one-tap

**Contents**:
- One Tap
- Installation
  - Add the Server Plugin
  - Add the Client Plugin
  - Usage
  - Customizing Redirect Behavior
    - Avoiding a Hard Redirect
    - Specifying a Custom Callback URL

get started, concepts, and plugins

Search documentation...

The One Tap plugin allows users to log in with a single tap using Google's One Tap API. The plugin provides a simple way to integrate One Tap into your application, handling the client-side and server-side logic for you.

Add the One Tap plugin to your auth configuration:

Add the client plugin and specify where the user should be redirected after sign-in or if additional verification (like 2FA) is needed.

To display the One Tap popup, simply call the oneTap method on your auth client:

By default, after a successful login the plugin will hard redirect the user to /. You can customize this behavior as follows:

Pass fetchOptions with an onSuccess callback to handle the login response without a page reload:

To perform a hard redirect to a different page after login, use the callbackURL option:

If the user dismisses or skips the prompt, the plugin will retry showing the One Tap prompt using exponential backoff based on your configured promptOptions.

If the maximum number of attempts is reached without a successful sign-in, you can use the onPromptNotification callback to be notified—allowing you to render an alternative UI (e.g., a traditional Google Sign-In button) so users can restart the process manually:

Sign In With Ethereum

**Examples**:

```python
import { betterAuth } from "better-auth";
import { oneTap } from "better-auth/plugins"; 

export const auth = betterAuth({
    plugins: [ 
        oneTap(), // Add the One Tap server plugin
    ] 
});
```

```python
import { betterAuth } from "better-auth";
import { oneTap } from "better-auth/plugins"; 

export const auth = betterAuth({
    plugins: [ 
        oneTap(), // Add the One Tap server plugin
    ] 
});
```

```python
import { createAuthClient } from "better-auth/client";
import { oneTapClient } from "better-auth/client/plugins";

export const authClient = createAuthClient({
  plugins: [
    oneTapClient({
      clientId: "YOUR_CLIENT_ID",
      // Optional client configuration:
      autoSelect: false,
      cancelOnTapOutside: true,
      context: "signin",
      additionalOptions: {
        // Any extra options for the Google initialize method
      },
      // Configure prompt behavior and exponential bac
...
```

---

## Options | Better Auth

**URL**: https://www.better-auth.com/docs/reference/options

**Contents**:
- Options
- appName
- baseURL
- basePath
- trustedOrigins
  - Static Origins
  - Dynamic Origins
  - Wildcard Support

get started, concepts, and plugins

Search documentation...

List of all the available options for configuring Better Auth. See Better Auth Options.

The name of the application.

Base URL for Better Auth. This is typically the root URL where your application server is hosted. Note: If you include a path in the baseURL, it will take precedence over the default path.

If not explicitly set, the system will check for the environment variable process.env.BETTER_AUTH_URL

Base path for Better Auth. This is typically the path where the Better Auth routes are mounted. It will be overridden if there is a path component within baseURL.

List of trusted origins. You can provide a static array of origins, a function that returns origins dynamically, or use wildcard patterns to match multiple domains.

You can provide a static array of origins:

You can provide a function that returns origins dynamically:

You can use wildcard patterns in trusted origins:

The secret used for encryption, signing, and hashing.

By default, Better Auth will look for the following environment variables:

If none of these environment variables are set, it will default to "better-auth-secret-123456789". In production, if it's not set, it will throw an error.

You can generate a good secret using the following command:

Database configuration for Better Auth.

Better Auth supports various database configurations including PostgreSQL, MySQL, and SQLite.

Read more about databases here.

Secondary storage configuration used to store session and rate limit data.

Read more about secondary storage here.

Email verification configuration.

Email and password authentication configuration.

Configure social login providers.

List of Better Auth plugins.

User configuration options.

Session configuration options.

Account configuration options.

Encrypt OAuth tokens before storing them in the database. Default: false.

If enabled (true), the user account data (accessToken, idToken, refreshToken, etc.) will

*[Content truncated - see full docs]*

**Examples**:

```python
import { betterAuth } from "better-auth";
export const auth = betterAuth({
	appName: "My App",
})
```

```python
import { betterAuth } from "better-auth";
export const auth = betterAuth({
	appName: "My App",
})
```

```python
import { betterAuth } from "better-auth";
export const auth = betterAuth({
	baseURL: "https://example.com",
})
```

---

## SAML SSO with Okta | Better Auth

**URL**: https://www.better-auth.com/docs/guides/saml-sso-with-okta

**Contents**:
- SAML SSO with Okta
- What is SAML?
  - Step 1: Create a SAML Application in Okta
  - Step 2: Configure Better Auth
  - Step 3: Multiple Default Providers (Optional)
  - Step 4: Initiating Sign-In
  - Step 5: Dynamically Registering SAML Providers
- Additional Resources

get started, concepts, and plugins

Search documentation...

This guide walks you through setting up SAML Single Sign-On (SSO) with your Identity Provider (IdP), using Okta as an example. For advanced configuration details and the full API reference, check out the SSO Plugin Documentation.

SAML (Security Assertion Markup Language) is an XML-based standard for exchanging authentication and authorization data between an Identity Provider (IdP) (e.g., Okta, Azure AD, OneLogin) and a Service Provider (SP) (in this case, Better Auth).

Log in to your Okta Admin Console

Navigate to Applications > Applications

Click "Create App Integration"

Select "SAML 2.0" as the Sign-in method

Configure the following settings:

Download the IdP metadata XML file and certificate

Here’s an example configuration for Okta in a dev environment:

You can configure multiple SAML providers for different domains:

Explicit: Pass providerId directly when signing in. Domain fallback: Matches based on the user’s email domain. e.g. [email protected] → matches company-okta provider.

You can start an SSO flow in three ways:

1. Explicitly by providerId (recommended):

2. By email domain matching:

3. By specifying domain:

For dynamic registration, you should register SAML providers using the API. See the SSO Plugin Documentation for detailed registration instructions.

Example registration:

Browser Extension Guide

Optimize for Performance

**Examples**:

```javascript
const ssoConfig = {
  defaultSSO: [{
    domain: "localhost:3000", // Your domain
    providerId: "sso",
    samlConfig: {
      // SP Configuration
      issuer: "http://localhost:3000/api/auth/sso/saml2/sp/metadata",
      entryPoint: "https://trial-1076874.okta.com/app/trial-1076874_samltest_1/exktofb0a62hqLAUL697/sso/saml",
      callbackUrl: "/dashboard", // Redirect after successful authentication
      
      // IdP Configuration
      idpMetadata: {
        entityID: "https://trial-10768
...
```

```javascript
const ssoConfig = {
  defaultSSO: [{
    domain: "localhost:3000", // Your domain
    providerId: "sso",
    samlConfig: {
      // SP Configuration
      issuer: "http://localhost:3000/api/auth/sso/saml2/sp/metadata",
      entryPoint: "https://trial-1076874.okta.com/app/trial-1076874_samltest_1/exktofb0a62hqLAUL697/sso/saml",
      callbackUrl: "/dashboard", // Redirect after successful authentication
      
      // IdP Configuration
      idpMetadata: {
        entityID: "https://trial-10768
...
```

```javascript
const ssoConfig = {
  defaultSSO: [
    {
      domain: "company.com",
      providerId: "company-okta",
      samlConfig: {
        // Okta SAML configuration for company.com
      }
    },
    {
      domain: "partner.com", 
      providerId: "partner-adfs",
      samlConfig: {
        // ADFS SAML configuration for partner.com
      }
    },
    {
      domain: "contractor.org",
      providerId: "contractor-azure",
      samlConfig: {
        // Azure AD SAML configuration for contractor.org
...
```

---

## Security | Better Auth

**URL**: https://www.better-auth.com/docs/reference/security

**Contents**:
- Security
- Password Hashing
- Session Management
  - Session Expiration
  - Session Revocation
- CSRF Protection
- OAuth State and PKCE
- Cookies

get started, concepts, and plugins

Search documentation...

This page contains information about security features of Better Auth.

Better Auth uses the scrypt algorithm to hash passwords by default. This algorithm is designed to be memory-hard and CPU-intensive, making it resistant to brute-force attacks. You can customize the password hashing function by setting the password option in the configuration. This option should include a hash function to hash passwords and a verify function to verify them.

Better Auth uses secure session management to protect user data. Sessions are stored in the database or a secondary storage, if configured, to prevent unauthorized access. By default, sessions expire after 7 days, but you can customize this value in the configuration. Additionally, each time a session is used, if it reaches the updateAge threshold, the expiration date is extended, which by default is set to 1 day.

Better Auth allows you to revoke sessions to enhance security. When a session is revoked, the user is logged out and can no longer access the application. A logged in user can also revoke their own sessions to log out from different devices or browsers.

See the session management for more details.

Better Auth includes multiple safeguards to prevent Cross-Site Request Forgery (CSRF) attacks:

Non-Simple Headers POST requests must either have a non-simple header or a Content-Type header of application/json. Non-simple headers are headers that are not included in the simple headers list.

Origin Validation Each request’s Origin header is verified to confirm it comes from your application or another explicitly trusted source. Requests from untrusted origins are rejected. By default, Better Auth trusts the base URL of your app, but you can specify additional trusted origins via the trustedOrigins configuration option.

Secure Cookie Settings Session cookies use the SameSite=Lax attribute by default, preventing browsers from sending cookies with most cross-si

*[Content truncated - see full docs]*

**Examples**:

```text
{
  advanced: {
    disableCSRFCheck: true
  }
}
```

```text
{
  advanced: {
    disableCSRFCheck: true
  }
}
```

```text
{
  advanced: {
    disableOriginCheck: true
  }
}
```

---

## Sign In With Ethereum (SIWE) | Better Auth

**URL**: https://www.better-auth.com/docs/plugins/siwe

**Contents**:
- Sign In With Ethereum (SIWE)
- Installation
  - Add the Server Plugin
  - Migrate the database
  - Add the Client Plugin
- Usage
  - Generate a Nonce
  - Sign In with Ethereum

get started, concepts, and plugins

Search documentation...

The Sign in with Ethereum (SIWE) plugin allows users to authenticate using their Ethereum wallets following the ERC-4361 standard. This plugin provides flexibility by allowing you to implement your own message verification and nonce generation logic.

Add the SIWE plugin to your auth configuration:

Run the migration or generate the schema to add the necessary fields and tables to the database.

See the Schema section to add the fields manually.

Before signing a SIWE message, you need to generate a nonce for the wallet address:

After generating a nonce and creating a SIWE message, verify the signature to authenticate:

Here are examples for different blockchain networks:

The chainId must match the Chain ID specified in your SIWE message. Verification will fail with a 401 error if there's a mismatch between the message's Chain ID and the chainId parameter.

The SIWE plugin accepts the following configuration options:

The SIWE client plugin doesn't require any configuration options, but you can pass them if needed for future extensibility:

The SIWE plugin adds a walletAddress table to store user wallet associations:

Here's a complete example showing how to implement SIWE authentication:

**Examples**:

```python
import { betterAuth } from "better-auth";
import { siwe } from "better-auth/plugins";

export const auth = betterAuth({
    plugins: [
        siwe({
            domain: "example.com",
            emailDomainName: "example.com", // optional
            anonymous: false, // optional, default is true
            getNonce: async () => {
                // Implement your nonce generation logic here
                return "your-secure-random-nonce";
            },
            verifyMessage: async (ar
...
```

```python
import { betterAuth } from "better-auth";
import { siwe } from "better-auth/plugins";

export const auth = betterAuth({
    plugins: [
        siwe({
            domain: "example.com",
            emailDomainName: "example.com", // optional
            anonymous: false, // optional, default is true
            getNonce: async () => {
                // Implement your nonce generation logic here
                return "your-secure-random-nonce";
            },
            verifyMessage: async (ar
...
```

```text
npx @better-auth/cli migrate
```

---
