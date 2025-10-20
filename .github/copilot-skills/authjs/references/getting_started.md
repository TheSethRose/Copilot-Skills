# Authjs - Getting Started

**Pages**: 139

---

## 42School Provider

**URL**: https://authjs.dev/getting-started/providers/42-school

**Contents**:
- 42School Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
- Notes

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/42-school
```

```text
https://example.com/auth/callback/42-school
```

```text
https://example.com/auth/callback/42-school
```

---

## Apple Provider

**URL**: https://authjs.dev/getting-started/providers/apple

**Contents**:
- Apple Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

NOTE: Apple currently does not support RedirectProxyUrl usage.

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/apple
```

```text
https://example.com/auth/callback/apple
```

```text
https://example.com/auth/callback/apple
```

---

## Asgardeo Provider

**URL**: https://authjs.dev/getting-started/providers/asgardeo

**Contents**:
- Asgardeo Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

Express not documented yet. Help us by contributing here.

Then, add the ClientID, ClientSecret, and Issuer values to your environment variables.

**Examples**:

```text
https://example.com/api/auth/callback/asgardeo
```

```text
https://example.com/auth/callback/asgardeo
```

```text
https://example.com/auth/callback/asgardeo
```

---

## Auth0 Provider

**URL**: https://authjs.dev/getting-started/providers/auth0

**Contents**:
- Auth0 Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/auth0
```

```text
https://example.com/auth/callback/auth0
```

```text
https://example.com/auth/callback/auth0
```

---

## Authentication

**URL**: https://authjs.dev/getting-started/authentication

**Contents**:
- Authentication

At this point, you need to decide how you’re gonna authenticate users in your application. Auth.js supports four main authentication paradigms.

Once you have decided how to authenticate users in your application, click on your authentication method of choice under “Authentication” in the sidebar to continue.

---

## Authentik Provider

**URL**: https://authjs.dev/getting-started/providers/authentik

**Contents**:
- Authentik Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

Express not documented yet. Help us by contributing here.

issuer should include the slug without a trailing slash – e.g., https://my-authentik-domain.com/application/o/My_Slug

**Examples**:

```text
https://example.com/api/auth/callback/authentik
```

```text
https://example.com/auth/callback/authentik
```

```text
https://example.com/auth/callback/authentik
```

---

## Azure AD B2C Provider

**URL**: https://authjs.dev/getting-started/providers/azure-ad-b2c

**Contents**:
- Azure AD B2C Provider
- Resources
- Setup
  - Environment Variables
  - Configuration
  - Tenant Setup

Basic configuration sets up Azure AD B2C to return an ID Token. This should be done as a prerequisite prior to running through the Advanced configuration. In the Tenant Setup, make sure to set the following during “User attributes and token claims”.

**Examples**:

```text
AUTH_AZURE_AD_B2C_ID
AUTH_AZURE_AD_B2C_SECRET
AUTH_AZURE_AD_B2C_ISSUER
```

```python
import NextAuth from "next-auth";
import AzureADB2C from "next-auth/providers/azure-ad-b2c";
 
export const { handlers, auth, signIn, signOut } = NextAuth({
  providers: [AzureADB2C({
    clientId: AUTH_AZURE_AD_B2C_CLIENT_ID
    clientSecret: AUTH_AZURE_AD_B2C_CLIENT_SECRET
    issuer: AUTH_AZURE_AD_B2C_ISSUER
  })]
});
```

```python
import { QwikAuth$ } from "@auth/qwik"
import AzureADB2C from "@auth/qwik/providers/azure-ad-b2c";
 
export const { onRequest, useSession, useSignIn, useSignOut } = QwikAuth$(
  () => ({
    providers: [
      AzureADB2C({
        clientId: import.meta.env.AUTH_AZURE_AD_CLIENT_ID
        clientSecret: import.meta.env.AUTH_AZURE_AD_CLIENT_SECRET
        issuer: import.meta.env.AUTH_AZURE_AD_ISSUER
      })
    ],
  })
)
```

---

## Azure AD Provider

**URL**: https://authjs.dev/getting-started/providers/azure-ad

**Contents**:
- Azure AD Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
    - To allow specific Active Directory users access:

Deprecated - Microsoft has rebranded this product Microsoft Entra ID and all support work will be going into that IdP. We recommend you migrate to using that provider as well.

Express not documented yet. Help us by contributing here.

In .env.local create the following entries:

That will default the tenant to use the common authorization endpoint. For more details see here.

If you want your application to receive authorization requests from not only the tenants but also all Microsoft users just add “common” in AUTH_AZURE_AD_TENANT_ID, this will “skip” tenants authorization.

Azure AD returns the profile picture in an ArrayBuffer, instead of just a URL to the image, so our provider converts it to a base64 encoded image string and returns that instead. See: https://docs.microsoft.com/en-us/graph/api/profilephoto-get?view=graph-rest-1.0#examples. The default image size is 48x48 to avoid running out of space in case the session is saved as a JWT.

In pages/api/auth/[...nextauth].js find or add the AzureAD entries:

**Examples**:

```text
https://example.com/api/auth/callback/azure-ad
```

```text
https://example.com/auth/callback/azure-ad
```

```text
https://example.com/auth/callback/azure-ad
```

---

## Azure DevOps Provider

**URL**: https://authjs.dev/getting-started/providers/azure-devops

**Contents**:
- Azure DevOps Provider
- Resources
- Setup
  - Callback URL
  - Environment variables
  - Register application
  - Configuration
  - Refresh token rotation

Deprecated - While still available, Microsoft is no longer supporting Azure DevOps OAuth and recommends using Microsoft Entra ID instead.

Express not documented yet. Help us by contributing here.

In .env.local create the following entries:

https://app.vsaex.visualstudio.com/app/register

Provide the required details:

Click ‘Create Application’

You are required to use HTTPS even for the localhost

You will have to delete and create a new application to change the scopes later

The following data is relevant for the next step:

Use the main guide as your starting point with the following considerations:

**Examples**:

```text
https://example.com/api/auth/callback/azure-devops
```

```text
https://example.com/auth/callback/azure-devops
```

```text
https://example.com/auth/callback/azure-devops
```

---

## Azure Table Storage Adapter

**URL**: https://authjs.dev/getting-started/adapters/azure-tables

**Contents**:
- Azure Table Storage Adapter
- Resources
- Setup
  - Installation
  - Environment Variables
  - Configuration

**Examples**:

```text
npm install @auth/azure-tables-adapter
```

```text
pnpm add @auth/azure-tables-adapter
```

```text
yarn add @auth/azure-tables-adapter
```

---

## BankID Norway Provider

**URL**: https://authjs.dev/getting-started/providers/bankid-no

**Contents**:
- BankID Norway Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

BankID Norge is a widespread login method in Norway, used by banks, government agencies, and other organizations. This provider allows users to sign in with BankID Norway.

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/bankid-no
```

```text
https://example.com/auth/callback/bankid-no
```

```text
https://example.com/auth/callback/bankid-no
```

---

## Battle.net Provider

**URL**: https://authjs.dev/getting-started/providers/battlenet

**Contents**:
- Battle.net Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

Express not documented yet. Help us by contributing here.

issuer must be one of these values, based on the available regions:

**Examples**:

```text
https://example.com/api/auth/callback/battlenet
```

```text
https://example.com/auth/callback/battlenet
```

```text
https://example.com/auth/callback/battlenet
```

---

## Before You Begin

**URL**: https://authjs.dev/getting-started/migrate-to-better-auth

**Contents**:
- Before You Begin
  - Mapping Existing Columns
  - Update the Route Handler
  - Update the Client
  - Server-Side Session Handling
  - Middleware
- Wrapping Up

Before starting the migration process, set up Better Auth in your project. Follow the Better Auth installation guide to get started.

Instead of altering your existing database column names, you can map them to match Better Auth’s expected structure. This allows you to retain your current database schema.

Map the following fields in the user schema:

Map the following fields in the session schema:

Make sure to have createdAt and updatedAt fields on your session schema.

Map these fields in the account schema:

Remove the session_state, type, and token_type fields, as they are not required by Better Auth.

Note: If you use ORM adapters, you can map these fields in your schema file.

Make sure to have createdAt and updatedAt fields on your account schema.

In the app/api/auth folder, rename the [...nextauth] file to [...all] to avoid confusion. Then, update the route.ts file as follows:

Create a file named auth-client.ts in the lib folder. Add the following code:

Update your social login actions to use Better Auth. For example, for Discord:

Update useSession Calls

Replace useSession calls with Better Auth’s version. Example:

Use the auth instance to get session data on the server:

To protect routes with middleware, refer to the Next.js middleware guide.

Congratulations! You’ve successfully migrated from NextAuth.js to Better Auth. For a complete implementation with multiple authentication methods, check out the demo repository.

Better Auth offers greater flexibility and more features—be sure to explore the documentation to unlock its full potential.

**Examples**:

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
    },
  },
})
```

```text
model Session {
    id          String   @id @default(cuid())
    expiresAt   DateTime @map("expires") // Map your existing `expires` field to Better Auth's `expiresAt`
    token       String   @map("sessionToken") // Map your existing `sessionToken` field to Better Auth's `token`
    userId      String
    user        User     @relation(fields: [userId], references: [id])
}
```

```python
import { toNextJsHandler } from "better-auth/next-js"
import { auth } from "~/server/auth"
 
export const { POST, GET } = toNextJsHandler(auth)
```

---

## Beyond Identity Provider

**URL**: https://authjs.dev/getting-started/providers/beyondidentity

**Contents**:
- Beyond Identity Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/beyondidentity
```

```text
https://example.com/auth/callback/beyondidentity
```

```text
https://example.com/auth/callback/beyondidentity
```

---

## Bitbucket Provider

**URL**: https://authjs.dev/getting-started/providers/bitbucket

**Contents**:
- Bitbucket Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/bitbucket
```

```text
https://example.com/auth/callback/bitbucket
```

```text
https://example.com/auth/callback/bitbucket
```

---

## Box Provider

**URL**: https://authjs.dev/getting-started/providers/box

**Contents**:
- Box Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/box
```

```text
https://example.com/auth/callback/box
```

```text
https://example.com/auth/callback/box
```

---

## BoxyHQ SAML Provider

**URL**: https://authjs.dev/getting-started/providers/boxyhq-saml

**Contents**:
- BoxyHQ SAML Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - SAML

Add BoxyHQ SAML login to your page.

BoxyHQ SAML is an open source service that handles the SAML SSO login flow as an OAuth 2.0 flow, abstracting away all the complexities of the SAML protocol. Enable Enterprise single-sign-on in your app with ease.

You can deploy BoxyHQ SAML as a separate service or embed it into your app using our NPM library. Check out the documentation for more details

Express not documented yet. Help us by contributing here.

SAML login requires a configuration for every tenant of yours. One common method is to use the domain for an email address to figure out which tenant they belong to. You can also use a unique tenant ID (string) from your backend for this, typically some kind of account or organization ID.

Check out the documentation for more details.

On the client side you’ll need to pass additional parameters tenant and product to the signIn function. This will allow BoxyHQL SAML to figure out the right SAML configuration and take your user to the right SAML Identity Provider to sign them in.

**Examples**:

```text
https://example.com/api/auth/callback/boxyhq-saml
```

```text
https://example.com/auth/callback/boxhq-saml
```

```text
https://example.com/auth/callback/boxhq-saml
```

---

## Bungie Provider

**URL**: https://authjs.dev/getting-started/providers/bungie

**Contents**:
- Bungie Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - Notes

Express not documented yet. Help us by contributing here.

Navigate to https://www.bungie.net/en/Application and fill in the required details:

**Examples**:

```text
https://example.com/api/auth/callback/bungie
```

```text
https://example.com/auth/callback/bungie
```

```text
https://example.com/auth/callback/bungie
```

---

## Click-Up Provider

**URL**: https://authjs.dev/getting-started/providers/click-up

**Contents**:
- Click-Up Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/clickup
```

```text
https://example.com/auth/callback/clickup
```

```text
https://example.com/auth/callback/clickup
```

---

## Cloudflare D1 Adapter

**URL**: https://authjs.dev/getting-started/adapters/d1

**Contents**:
- Cloudflare D1 Adapter
- Resources
- Setup
  - Installation
  - Environment Variables
  - Configuration
  - Migrations

Environment variables in Cloudflare’s platform are set either via a wrangler.toml configuration file, or in the admin dashboard.

Somewhere in the initialization of your application you need to run the up(env.db) function to create the tables in D1. It will create 4 tables if they don’t already exist: accounts, sessions, users, verification_tokens.

The table prefix "" is not configurable at this time.

You can use something like the following to attempt the migration once each time your worker starts up. Running migrations more than once will not erase your existing tables.

**Examples**:

```text
npm install next-auth @auth/d1-adapter
```

```text
pnpm add next-auth @auth/d1-adapter
```

```text
yarn add next-auth @auth/d1-adapter
```

---

## Cognito Provider

**URL**: https://authjs.dev/getting-started/providers/cognito

**Contents**:
- Cognito Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - Notes

Express not documented yet. Help us by contributing here.

You need to select your AWS region to go the the Cognito dashboard.

The issuer is a URL, that looks like this: https://cognito-idp.{region} .amazonaws.com/{PoolId}, where PoolId is from General Settings in Cognito, not to be confused with the App Client ID.

Before you can set these settings, you must set up an Amazon Cognito hosted domain. The setting can be found in App Client/Edit Hosted UI.

Make sure you select all the appropriate client settings or the OAuth flow will not work.

**Examples**:

```text
https://example.com/api/auth/callback/cognito
```

```text
https://example.com/auth/callback/cognito
```

```text
https://example.com/auth/callback/cognito
```

---

## Coinbase Provider

**URL**: https://authjs.dev/getting-started/providers/coinbase

**Contents**:
- Coinbase Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - Notes

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/coinbase
```

```text
https://example.com/auth/callback/coinbase
```

```text
https://example.com/auth/callback/coinbase
```

---

## Credentials

**URL**: https://authjs.dev/getting-started/authentication/credentials

**Contents**:
- Credentials
  - Credentials Provider
    - credentials
    - authorize
  - Signin Form
- Validating credentials

To setup Auth.js with any external authentication mechanisms or use a traditional username/email and password flow, we can use the Credentials provider. This provider is designed to forward any credentials inserted into the login form (i.e. username/password, but not limited to) to your authentication service.

The industry has come a long way since usernames and passwords as the go-to mechanism for authenticating and authorizing users to web applications. Therefore, if possible, we recommend a more modern and secure authentication mechanism such as any of the OAuth providers, Email Magic Links, or WebAuthn (Passkeys) options instead.

However, we also want to be flexible and support anything you deem appropriate for your application and use case, so there are no plans to remove this provider.

By default, the Credentials provider does not persist data in the database. However, you can still create and save any data in your database, you just have to provide the necessary logic, eg. to encrypt passwords, add rate-limiting, add password reset functionality, etc.

To use the Credentials Provider, you’ll first need to import and configure it in your Auth.js setup. This provider allows you to implement custom login logic based on form input values.

Here’s how to set it up:

The credentials object defines the input fields displayed on the default sign-in page. These inputs are automatically rendered on the route:

Each field accepts the following properties:

These fields are also passed to the authorize function under the credentials argument.

For more details, see the Built-in Pages guide.

The authorize function handles the custom login logic and determines whether the credentials provided are valid.

It receives the input values defined in credentials, and you must return either a user object or null. If null is returned, the login fails.

Don’t forget to re-export the handle in your ./src/hooks.server.ts file.

If you’re using TypeScript, you can augment the User 

*[Content truncated - see full docs]*

**Examples**:

```text
Credentials({
  credentials: {
    email: {
      type: "email",
      label: "Email",
      placeholder: "johndoe@gmail.com",
    },
    password: {
      type: "password",
      label: "Password",
      placeholder: "*****",
    },
  },
})
```

```python
import NextAuth from "next-auth"
import Credentials from "next-auth/providers/credentials"
// Your own logic for dealing with plaintext password strings; be careful!
import { saltAndHashPassword } from "@/utils/password"
 
export const { handlers, signIn, signOut, auth } = NextAuth({
  providers: [
    Credentials({
      // You can specify which fields should be submitted, by adding keys to the `credentials` object.
      // e.g. domain, username, password, 2FA token, etc.
      credentials: {

...
```

```python
import { QwikAuth$ } from "@auth/qwik"
import Credentials from "@auth/qwik/providers/credentials"
 
export const { onRequest, useSession, useSignIn, useSignOut } = QwikAuth$(
  () => ({
    providers: [
      Credentials({
        credentials: {
          email: { label: "Email" },
          password: { label: "Password", type: "password" },
        },
        async authorize(credentials) {
          const response = await getUserFromDb(credentials)
          if (!response.ok) return null
      
...
```

---

## Credentials Provider

**URL**: https://authjs.dev/getting-started/providers/credentials

**Contents**:
- Credentials Provider
- Resources
- Configuration
  - Custom Error Messages

The Credentials provider allows you to handle signing in with arbitrary credentials, such as a username and password, domain, two factor authentication or hardware device (e.g. YubiKey U2F / FIDO).

It is intended to support use cases where you have an existing system you need to authenticate users against, and therefore users authenticated in this manner are not persisted in the database.

You can throw a custom error in the authorize function to return a custom error message to the user.

You will then receive that custom error code in the query parameters of the signin page your user returns to after a failed login attempt, for example https://app.company.com/auth/signin?error=CredentialsSignin&code=Invalid+identifier+or+password.

OAuth providers spend significant amounts of money, time, and engineering effort to build:

and much more for authentication solutions. It is likely that your application would benefit from leveraging these battle-tested solutions rather than try to rebuild them from scratch.

If you’d still like to build password-based authentication for your application despite these risks, Auth.js gives you full control to do so.

**Examples**:

```python
import NextAuth from "next-auth"
import Credentials from "next-auth/providers/credentials"
 
export const { signIn, signOut, auth } = NextAuth({
  providers: [
    Credentials({
      credentials: {
        username: { label: "Username" },
        password: { label: "Password", type: "password" },
      },
      async authorize({ request }) {
        const response = await fetch(request)
        if (!response.ok) return null
        return (await response.json()) ?? null
      },
    }),
  ],
})
```

```python
import { QwikAuth$ } from "@auth/qwik"
import Credentials from "@auth/qwik/providers/credentials"
 
export const { onRequest, useSession, useSignIn, useSignOut } = QwikAuth$(
  () => ({
    providers: [
      Credentials({
        credentials: {
          username: { label: "Username" },
          password: { label: "Password", type: "password" },
        },
        async authorize({ request }) {
          const response = await fetch(request)
          if (!response.ok) return null
          re
...
```

```python
import { SvelteKitAuth } from "@auth/sveltekit"
import Credentials from "@auth/sveltekit/providers/credentials"
 
export const { handle, signIn, signOut } = SvelteKitAuth({
  providers: [
    Credentials({
      credentials: {
        username: { label: "Username" },
        password: { label: "Password", type: "password" },
      },
      async authorize({ request }) {
        const response = await fetch(request)
        if (!response.ok) return null
        return (await response.json()) ?? n
...
```

---

## Custom Pages

**URL**: https://authjs.dev/getting-started/session-management/custom-pages

**Contents**:
- Custom Pages

To enable custom pages add the following to your Auth.js configuration. In the pages object, the key is the type of page and the value is the path/route at which the page is located. Please make sure you actually have a page at the specified route.

To continue setting up the custom page, checkout our guide on custom pages.

**Examples**:

```python
import { NextAuth } from "next-auth"
import GitHub from "next-auth/providers/github"
 
// Define your configuration in a separate variable and pass it to NextAuth()
// This way we can also 'export const config' for use later
export const config = {
  providers: [GitHub],
  pages: {
    signIn: "/login",
  },
}
 
export const { signIn, signOut, handle } = NextAuth(config)
```

```python
import { QwikAuth$ } from "@auth/qwik"
import GitHub from "@auth/qwik/providers/github"
 
export const { onRequest, useSession, useSignIn, useSignOut } = QwikAuth$(
  () => ({
    providers: [GitHub],
    pages: {
      signIn: "/login",
    },
  })
)
```

```python
import SvelteKitAuth from "@auth/sveltekit"
import GitHub from "@auth/sveltekit/providers/github"
import type { Provider } from "@auth/sveltekit/providers"
 
const providers: Provider[] = [GitHub]
 
// Export this map of provider details to use in the sign-in page later
export const providerMap = providers.map((provider) => {
  return { id: provider.id, name: provider.name }
})
 
export const { handle, signIn, signOut } = SvelteKitAuth({
  providers,
  pages: {
    signIn: "/signin",
  },
})
```

---

## Database Adapters

**URL**: https://authjs.dev/getting-started/database

**Contents**:
- Database Adapters
- Official Adapters
- Models

Auth.js integrations save sessions in a cookie by default. Therefore, setting up a database is optional. However, if you want to persist user information in your own database, or you want to implement certain flows, you will need to use a Database Adapter.

Database Adapters are the bridge we use to connect Auth.js to your database. For instance, when implementing magic links, the Email provider will require you to setup a database adapter to be able to store the verification tokens present on the links.

Below is a list of official adapters that are distributed as their own packages under the @auth/ namespace. Their source code is available in the nextauthjs/next-auth monorepo. If you’re going to create a database adapter, please make sure you familiarise yourself with the models Auth.js expects to be present and check out our “creating a database adapter” guide.

If you don’t find an adapter for your database or service of choice, you can create one yourself. Have a look at our guide on how to create a database adapter. If you create a new adapter, we’d love it if you opened a PR to share it with everyone!

This is a generic ER Diagram of what the full database schema should look like. Your database adapter of choice will include a template schema with more details for applying this schema to the underlying database. For more details, check out our database models documentation. Please note, that the entire schema is not required for every use-case, for more details check out our database adapters guide.

---

## Deployment

**URL**: https://authjs.dev/getting-started/deployment

**Contents**:
- Deployment
- Environment Variables
  - AUTH_SECRET
  - AUTH_TRUST_HOST
  - AUTH_URL
  - AUTH_REDIRECT_PROXY_URL
- Serverless
- Observability

For consistency, we recommend prefixing all Auth.js environment variables with AUTH_. This way we can better autodetect them, and they can also be distinguished from other environment variables more easily.

Auth.js libraries require you to set an AUTH_SECRET environment variable. This is used to encrypt cookies and tokens. It should be a cryptographically secure random string of at least 32 characters:

If you are using an OAuth Provider, your provider will provide you with a Client ID and Client Secret that you will need to set as environment variables as well (in the case of an OIDC provider, like Auth0, a third issuer value might be also required, refer to the provider’s specific documentation).

Auth.js supports environment variable inference, meaning that if you name your provider environment variables following a specific syntax, you won’t need to explicitly pass them to the providers in your configuration.

Client ID’s and client secrets should be named AUTH_[PROVIDER]_ID and AUTH_[PROVIDER]_SECRET. If your provider requires an issuer, that should be named AUTH_[PROVIDER]_ISSUER. For example:

For more information, check out our environment variables page.

This is the only strictly required environment variable. It is the secret used to encode the JWT and encrypt things in transit. As mentioned above, we recommend at least a 32 character random string. This can be generated via the CLI with npm exec auth secret or via openssl with openssl rand -base64 33.

When deploying your application behind a reverse proxy, you’ll need to set AUTH_TRUST_HOST equal to true. This tells Auth.js to trust the X-Forwarded-Host header from the reverse proxy. Auth.js will automatically infer this to be true if we detect the environment variable indicating that your application is running on one of the supported hosting providers. Currently VERCEL and CF_PAGES (Cloudflare Pages) are supported.

This environment variable is mostly unnecessary with v5 as the host is inferred from 

*[Content truncated - see full docs]*

**Examples**:

```text
npm exec auth secret
```

```text
pnpm exec auth secret
```

```text
yarn auth secret
```

---

## Descope Provider

**URL**: https://authjs.dev/getting-started/providers/descope

**Contents**:
- Descope Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - Using Descope Widgets

Express not documented yet. Help us by contributing here.

Add the required environment variables from above to your .env.local file.

If you wish to use Descope Widgets with NextAuth.js, you will have to wrap your NextAuth.js components with our Next.js SDK and <AuthProvider>.

For more information on this, please look at our documentation here.

**Examples**:

```text
https://example.com/api/auth/callback/descope
```

```text
https://example.com/auth/callback/descope
```

```text
https://example.com/auth/callback/descope
```

---

## Dgraph Adapter

**URL**: https://authjs.dev/getting-started/adapters/dgraph

**Contents**:
- Dgraph Adapter
- Resources
- Setup
  - Installation
  - Environment Variables
  - Configuration
  - Unsecure Schema
    - Example

The quickest way to use Dgraph is by applying the unsecure schema to your local Dgraph instance or if using Dgraph cloud you can paste the schema in the codebox to update.

This approach is not secure or for production use, and does not require a jwtSecret.

This schema is adapted for use in Dgraph and based upon our main schema

For production deployments you will want to restrict the access to the types used by next-auth. The main form of access control used in Dgraph is via @auth directive alongside types in the schema.

In order to secure your graphql backend define the Dgraph.Authorization object at the bottom of your schema and provide authHeader and jwtSecret values to the DgraphClient.

This is the key used to sign the JWT. Ex. process.env.SECRET or process.env.APP_SECRET.

The Header tells Dgraph where to lookup a JWT within the headers of the incoming requests made to the dgraph server. You have to configure it at the bottom of your schema file. This header is the same as the authHeader property you provide when you instantiate the DgraphClient.

The $nextAuth secret is securely generated using the jwtSecret and injected by the DgraphAdapter in order to allow interacting with the JWT DgraphClient for anonymous user requests made within the system ie. login, register. This allows secure interactions to be made with all the auth types required by next-auth. You have to specify it for each auth rule of each type defined in your secure schema.

Dgraph only works with HS256 or RS256 algorithms. If you want to use session jwt to securely interact with your dgraph database you must customize next-auth encode and decode functions, as the default algorithm is HS512. You can further customize the jwt with roles if you want to implement RBAC logic.

Once your Dgraph.Authorization is defined in your schema and the JWT settings are set, this will allow you to define @auth rules for every part of your schema.

**Examples**:

```text
npm install @auth/dgraph-adapter
```

```text
pnpm add @auth/dgraph-adapter
```

```text
yarn add @auth/dgraph-adapter
```

---

## Discord Provider

**URL**: https://authjs.dev/getting-started/providers/discord

**Contents**:
- Discord Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/discord
```

```text
https://example.com/auth/callback/discord
```

```text
https://example.com/auth/callback/discord
```

---

## Dribbble Provider

**URL**: https://authjs.dev/getting-started/providers/dribbble

**Contents**:
- Dribbble Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - Notes

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/dribbble
```

```text
https://example.com/auth/callback/dribbble
```

```text
https://example.com/auth/callback/dribbble
```

---

## Drizzle ORM Adapter

**URL**: https://authjs.dev/getting-started/adapters/drizzle

**Contents**:
- Drizzle ORM Adapter
- Resources
- Setup
  - Installation
  - Environment Variables
  - Configuration
    - Schemas
  - Adapter Setup

To use this adapter, you must have setup Drizzle ORM and Drizzle Kit in your project. Drizzle provides a simple quick start guide. For more details, follow the Drizzle documentation for your respective database (PostgreSQL, MySQL or SQLite). In summary, that setup should look something like this.

If you want to use your own tables, you can pass them as a second argument to DrizzleAdapter.

With your schema now described in your code, you’ll need to migrate your database to your schema. An example migrate.ts file looks like this. For more information, check out Drizzle’s migration quick start guide.

Full documentation on how to manage migrations with Drizzle can be found at the Drizzle Kit Migrations page.

**Examples**:

```text
npm install drizzle-orm @auth/drizzle-adapter
npm install drizzle-kit --save-dev
```

```text
pnpm add drizzle-orm @auth/drizzle-adapter
pnpm add drizzle-kit --save-dev
```

```text
yarn add drizzle-orm @auth/drizzle-adapter
yarn add drizzle-kit --dev
```

---

## Dropbox Provider

**URL**: https://authjs.dev/getting-started/providers/dropbox

**Contents**:
- Dropbox Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/dropbox
```

```text
https://example.com/auth/callback/dropbox
```

```text
https://example.com/auth/callback/dropbox
```

---

## Duende Identity Server Provider

**URL**: https://authjs.dev/getting-started/providers/duende-identity-server6

**Contents**:
- Duende Identity Server Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - Demo IdentityServer

Express not documented yet. Help us by contributing here.

The configuration below is for the demo server at https://demo.duendesoftware.com/

If you want to try it out, you can copy and paste the configuration below.

You can sign in to the demo service with either bob/bob or alice/alice.

**Examples**:

```text
https://example.com/api/auth/callback/duende-identity-service
```

```text
https://example.com/auth/callback/duende-identity-service
```

```text
https://example.com/auth/callback/duende-identity-service
```

---

## DynamoDB Adapter

**URL**: https://authjs.dev/getting-started/adapters/dynamodb

**Contents**:
- DynamoDB Adapter
- Resources
- Setup
  - Installation
  - Environment Variables
  - Configuration
  - AWS Credentials
- Advanced usage

You need to pass DynamoDBDocument client from the modular aws-sdk v3 to the adapter. The default table name is next-auth, but you can customise that by passing { tableName: 'your-table-name' } as the second parameter in the adapter.

Always follow the principle of least privilege when giving access to AWS services/resources -> identities should only be permitted to perform the smallest set of actions necessary to fulfill a specific task.

Below are some infrastructure-as-code templates for popular providers to help you spin up DynamoDB.

The table respects the single table design pattern. This has many advantages:

By default, the adapter expects a table with a partition key pk and a sort key sk, as well as a global secondary index named GSI1 with GSI1PK as partition key and GSI1SK as sorting key. To automatically delete sessions and verification requests after they expire using dynamodb TTL you should enable the TTL with attribute name expires. You can set whatever you want as the table name and the billing method. You can find the full schema in the table structure section below.

You can configure your custom table schema by passing the options key to the adapter constructor:

**Examples**:

```text
npm install @auth/dynamodb-adapter @aws-sdk/lib-dynamodb @aws-sdk/client-dynamodb
```

```text
pnpm add @auth/dynamodb-adapter @aws-sdk/lib-dynamodb @aws-sdk/client-dynamodb
```

```text
yarn add @auth/dynamodb-adapter @aws-sdk/lib-dynamodb @aws-sdk/client-dynamodb
```

---

## EVEOnline Provider

**URL**: https://authjs.dev/getting-started/providers/eveonline

**Contents**:
- EVEOnline Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - Notes

Express not documented yet. Help us by contributing here.

When creating your application, make sure to select Authentication & API Access as the connection type. Also ensure that the publicData scope is selected.

If using JWT for the session, you can add the CharacterID to the JWT and session. For example:

**Examples**:

```text
https://example.com/api/auth/callback/eveonline
```

```text
https://example.com/auth/callback/eveonline
```

```text
https://example.com/auth/callback/eveonline
```

---

## EdgeDB Adapter

**URL**: https://authjs.dev/getting-started/adapters/edgedb

**Contents**:
- EdgeDB Adapter
- Resources
- Setup
  - Installation
  - Environment Variables
  - Configuration
  - EdgeDB CLI
    - Linux or macOS

Ensure you have the EdgeDB CLI installed. Follow the instructions below, or read the EdgeDB quickstart to install the EdgeDB CLI and initialize a project

Check that the CLI is available with the edgedb --version command. If you get a Command not found error, you may need to open a new terminal window before the edgedb command is available.

Once the CLI is installed, initialize a project from the application’s root directory. You’ll be presented with a series of prompts.

This process will spin up an EdgeDB instance and “link” it with your current directory. As long as you’re inside that directory, CLI commands and client libraries will be able to connect to the linked instance automatically, without additional configuration.

Replace the contents of the auto-generated file in dbschema/default.esdl with the following:

To learn more about EdgeDB migrations check out the Migrations docs.

This will generate the query builder so that you can write fully typed EdgeQL queries with TypeScript in a code-first way.

First deploy an EdgeDB instance on your preferred cloud provider:

The DSN is also known as a connection string. It will have the format edgedb://username:password@hostname:port. The exact instructions for this depend on which cloud provider you’re deploying to.

Use the DSN to apply migrations against your remote instance.

Add the following prebuild script to your package.json. When your hosting provider initializes the build, it will trigger this script which will generate the query builder. The npx @edgedb/generate edgeql-js command will read the value of the EDGEDB_DSN environment variable, connect to the database, and generate the query builder before your hosting provider starts building the project.

**Examples**:

```text
npm install edgedb @auth/edgedb-adapter
npm install @edgedb/generate --save-dev
```

```text
pnpm add edgedb @auth/edgedb-adapter
pnpm add @edgedb/generate --save-dev
```

```text
yarn add edgedb @auth/edgedb-adapter
yarn add @edgedb/generate --dev
```

---

## Email Provider

**URL**: https://authjs.dev/getting-started/authentication/email

**Contents**:
- Email Provider
  - Providers
  - Forward Email Setup
  - Database Adapter
  - Setup Environment Variables
  - Setup Provider
  - Add Signin Button
  - Signin

This login mechanism starts by the user providing their email address at the login form. Then a Verification Token is sent to the provided email address. The user then has 24 hours to click the link in the email body to “consume” that token and register their account, otherwise the verification token will expire and they will have to request a new one.

An Email Provider can be used with both JSON Web Tokens and database session, whichever you choose, you must still configure a database so that Auth.js can save the verification tokens and look them up when the user attempts to login. It is not possible to enable an email provider without using a database.

Please make sure you’ve setup a database adapter, as mentioned earlier, a database is required for passwordless login to work as verification tokens need to be stored.

Auth.js will automatically pick up these if formatted like the example above. You can also use a different name for the environment variables if needed, but then you’ll need to pass them to the provider manually.

Let’s enable ForwardEmail as a sign in option in our Auth.js configuration. You’ll have to import the ForwardEmail provider from the package and pass it to the providers array we setup earlier in the Auth.js config file:

Express not documented yet. Help us by contributing here.

Next, we can add a signin button somewhere in your application like the Navbar. This will send an email to the user containing the magic link to sign in.

Express not documented yet. Help us by contributing here.

Start your application, once the user enters their Email and clicks on the signin button, they’ll be redirected to a page that asks them to check their email. When they click on the link in their email, they will be signed in.

Check our Customising magic links emails to learn how to change the look and feel of the emails the user receives to sign in.

For more information on this provider go to the Forward Email docs page.

Please make sure you’ve setu

*[Content truncated - see full docs]*

**Examples**:

```text
AUTH_FORWARDEMAIL_KEY=abc123
```

```python
import NextAuth from "next-auth"
import ForwardEmail from "next-auth/providers/forwardemail"
 
export const { handlers, auth, signIn, signOut } = NextAuth({
  providers: [ForwardEmail],
})
```

```python
import { QwikAuth$ } from "@auth/qwik"
import ForwardEmail from "@auth/qwik/providers/forwardemail"
 
export const { onRequest, useSession, useSignIn, useSignOut } = QwikAuth$(
  () => ({
    providers: [ForwardEmail],
  })
)
```

---

## Facebook Provider

**URL**: https://authjs.dev/getting-started/providers/facebook

**Contents**:
- Facebook Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - Notes

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/facebook
```

```text
https://example.com/auth/callback/facebook
```

```text
https://example.com/auth/callback/facebook
```

---

## Faceit Provider

**URL**: https://authjs.dev/getting-started/providers/faceit

**Contents**:
- Faceit Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - Notes

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/faceit
```

```text
https://example.com/auth/callback/faceit
```

```text
https://example.com/auth/callback/faceit
```

---

## Fauna Adapter

**URL**: https://authjs.dev/getting-started/adapters/fauna

**Contents**:
- Fauna Adapter
- Resources
- Setup
  - Installation
  - Environment Variables
  - Configuration
  - Migrating to v2
    - Schema

In @auth/adapter-fauna@2.0.0, we’ve renamed the collections to use an uppercase naming pattern in accordance with the Fauna best practices. If you’re migrating from v1, you’ll need to rename your collections to match the new naming scheme. Additionally, we’ve renamed the indexes to match the new method-like index names (i.e. account_by_user_id to Account.byUserId). For more information on migrating your Fauna schema, see their migration guide here

Run the following commands inside of the Shell tab in the Fauna dashboard to setup the appropriate collections and indexes.

If you want to use custom collection names, you can pass them as an option to the adapter, like this:

Make sure the collection names you pass to the provider match the collection names of your Fauna database.

**Examples**:

```text
npm install @auth/fauna-adapter fauna
```

```text
pnpm add @auth/fauna-adapter fauna
```

```text
yarn add @auth/fauna-adapter fauna
```

---

## Figma Provider

**URL**: https://authjs.dev/getting-started/providers/figma

**Contents**:
- Figma Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

Express not documented yet. Help us by contributing here.

The URL must be accessed via the user’s browser and not an embedded webview inside your application. Webview access to the Figma OAuth flow is not supported and may stop working for some or all users without an API version update.

**Examples**:

```text
https://example.com/api/auth/callback/figma
```

```text
https://example.com/auth/callback/figma
```

```text
https://example.com/auth/callback/figma
```

---

## Firebase Adapter

**URL**: https://authjs.dev/getting-started/adapters/firebase

**Contents**:
- Firebase Adapter
- Resources
- Setup
  - Installation
  - Environment variables
  - Configuration
  - Authentication
    - Service Account File

Using the Firebase Admin SDK and Firestore.

First, create a Firebase project and generate a service account key. Visit: https://console.firebase.google.com/u/0/project/{project-id}/settings/serviceaccounts/adminsdk (replace {project-id} with your project’s id)

If you already have a Firestore instance, you can pass that to the adapter directly instead.

When passing an instance and in a serverless environment, remember to handle duplicate app initialization.

You can use the initFirestore utility to initialize the app and get an instance safely.

Utility function that helps making sure that there is no duplicate app initialization issues in serverless environments. If no parameter is passed, it will use the GOOGLE_APPLICATION_CREDENTIALS environment variable to initialize a Firestore instance.

**Examples**:

```text
npm install @auth/firebase-adapter firebase-admin
```

```text
pnpm add @auth/firebase-adapter firebase-admin
```

```text
yarn add @auth/firebase-adapter firebase-admin
```

---

## Forward Email Provider

**URL**: https://authjs.dev/getting-started/providers/forwardemail

**Contents**:
- Forward Email Provider
- Overview
  - How it works
- Configuration
- Customization
  - Email Body
  - Verification Tokens
  - Normalizing Email Addresses

The Forward Email provider uses email to send “magic links” that contain URLs with verification tokens can be used to sign in.

Adding support for signing in via email in addition to one or more OAuth services provides a way for users to sign in if they lose access to their OAuth account (e.g. if it is locked or deleted).

The Forward Email provider can be used in conjunction with (or instead of) one or more OAuth providers.

On initial sign in, a Verification Token is sent to the email address provided. By default this token is valid for 24 hours. If the Verification Token is used within that time (i.e. by clicking on the link in the email) an account is created for the user and they are signed in.

If someone provides the email address of an existing account when signing in, an email is sent and they are signed into the account associated with that email address when they follow the link in the email.

The Forward Email provider can be used with both BasicAuth and database managed sessions, however you must configure a database to use it. It is not possible to enable email sign in without using a database.

First, you’ll need to add your domain to your Forward Email account. This is required by Forward Email and this domain of the address you use in the from provider option.

Next, you will have to generate an API key in the My Account → Security. You can save this API key as the AUTH_FORWARDEMAIL_KEY environment variable.

If you name your environment variable AUTH_FORWARDEMAIL_KEY, the provider will pick it up automatically and your Auth.js configuration object can be simpler. If you’d like to rename it to something else, however, you’ll have to manually pass it into the provider in your Auth.js configuration.

Express not documented yet. Help us by contributing here.

Do not forget to setup one of the database adapters for storing the Email verification token.

You can now start the sign-in process with an email address at /api/auth/signin.

A user account (i.e

*[Content truncated - see full docs]*

**Examples**:

```text
AUTH_FORWARDEMAIL_KEY=abc
```

```python
import NextAuth from "next-auth"
import ForwardEmail from "next-auth/providers/forwardemail"
 
export const { handlers, auth, signIn, signOut } = NextAuth({
  adapter: ...,
  providers: [
    ForwardEmail({
      // If your environment variable is named differently than default
      apiKey: AUTH_FORWARDEMAIL_KEY,
      from: "no-reply@company.com"
    }),
  ],
})
```

```python
import { QwikAuth$ } from "@auth/qwik"
import ForwardEmail from "@auth/qwik/providers/forwardemail"
 
export const { onRequest, useSession, useSignIn, useSignOut } = QwikAuth$(
  () => ({
    providers: [
      ForwardEmail({
        // If your environment variable is named differently than default
        apiKey: import.meta.env.AUTH_FORWARDEMAIL_KEY,
        from: "no-reply@company.com",
      }),
    ],
  })
)
```

---

## Foursquare Provider

**URL**: https://authjs.dev/getting-started/providers/foursquare

**Contents**:
- Foursquare Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - Notes

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/foursquare
```

```text
https://example.com/auth/callback/foursquare
```

```text
https://example.com/auth/callback/foursquare
```

---

## Freshbooks Provider

**URL**: https://authjs.dev/getting-started/providers/freshbooks

**Contents**:
- Freshbooks Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - Notes

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/freshbooks
```

```text
https://example.com/auth/callback/freshbooks
```

```text
https://example.com/auth/callback/freshbooks
```

---

## Frontegg Provider

**URL**: https://authjs.dev/getting-started/providers/frontegg

**Contents**:
- Frontegg Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

Qwik not documented yet. Help us by contributing here.

Express not documented yet. Help us by contributing here.

Log into the Frontegg portal

Add the required environment variables to your .env.local file.

Qwik not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/frontegg
```

```text
https://example.com/auth/callback/frontegg
```

```text
AUTH_FRONTEGG_ID
AUTH_FRONTEGG_SECRET
AUTH_FRONTEGG_ISSUER
```

---

## Fusion Auth

**URL**: https://authjs.dev/getting-started/providers/fusionauth

**Contents**:
- Fusion Auth
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - Notes

Express not documented yet. Help us by contributing here.

If you’re using multi-tenancy, you need to pass in the tenantId option to apply the proper theme.

In the OAuth settings for your application, configure the following.

If using JSON Web Tokens, you need to make sure the signing algorithm is RS256, you can create an RS256 key pair by going to Settings, Key Master, generate RSA and choosing SHA-256 as algorithm. After that, go to the JWT settings of your application and select this key as Access Token signing key and Id Token signing key.

**Examples**:

```text
https://example.com/api/auth/callback/fusionauth
```

```text
https://example.com/auth/callback/fusionauth
```

```text
https://example.com/auth/callback/fusionauth
```

---

## Get Session

**URL**: https://authjs.dev/getting-started/session-management/get-session

**Contents**:
- Get Session
  - App Router
  - Page Server Side
  - Page Client Side

Once a user is logged in, you often want to get the session object in order to use the data in some way. A common use-case is to show their profile picture or display some other user information.

Although next-auth supports client-side data retrieval using useSession and SessionProvider for both the App Router and Pages Router, in real-world scenarios, these are used less frequently. Typically, you’ll want to take full advantage of server-side rendering to optimize performance and security.

In the pages router, to access a session in a component, you’ll first need to get the session object in a page and then pass it down to the component.

When accessing the session client-side using useSession(), make sure an Auth.js <SessionProvider /> is wrapping your page.

Finally, we can use it in the component.

Under the hood Qwik is preparing automatically the session for you so you don’t have to implement custom logic for that. You can read the sesion on the server with event.sharedMap.get("session") and on the client with the useSession() action.

With SvelteKit, you have to return the session object from the load function in your +page.server.ts or +layout.server.ts files.

Then you can access the session on the $page.data object in your page.

If you’d like to extend your session with more fields from your OAuth provider, for example, please check out our “extending the session” guide.

By default, GET requests to the session endpoint will automatically return the headers to prevent caching.

**Examples**:

```python
import { auth } from "../auth"
 
export default async function UserAvatar() {
  const session = await auth()
 
  if (!session?.user) return null
 
  return (
    <div>
      <img src={session.user.image} alt="User Avatar" />
    </div>
  )
}
```

```python
"use client"
import { useSession } from "next-auth/react"
 
export default function Dashboard() {
  const { data: session } = useSession()
 
  if (session?.user?.role === "admin") {
    return <p>You are an admin, welcome!</p>
  }
 
  return <p>You are not authorized to view this page!</p>
}
```

```python
import { SessionProvider } from "next-auth/react"
import { Dashboard } from "./Dashboard"
 
export default function Administrator() {
  return (
    <SessionProvider>
      <Dashboard />
    </SessionProvider>
  )
}
```

---

## GitHub Provider

**URL**: https://authjs.dev/getting-started/providers/github

**Contents**:
- GitHub Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/github
```

```text
https://example.com/auth/callback/github
```

```text
https://example.com/auth/callback/github
```

---

## GitLab Provider

**URL**: https://authjs.dev/getting-started/providers/gitlab

**Contents**:
- GitLab Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - Notes

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/gitlab
```

```text
https://example.com/auth/callback/gitlab
```

```text
https://example.com/auth/callback/gitlab
```

---

## Google Provider

**URL**: https://authjs.dev/getting-started/providers/google

**Contents**:
- Google Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
- Notes
  - Refresh Token

Express not documented yet. Help us by contributing here.

Google only provides Refresh Token to an application the first time a user signs in.

To force Google to re-issue a Refresh Token, the user needs to remove the application from their account and sign in again: https://myaccount.google.com/permissions

Alternatively, you can also pass options in the params object of authorization which will force the Refresh Token to always be provided on sign in, however this will ask all users to confirm if they wish to grant your application access every time they sign in.

If you need access to the RefreshToken or AccessToken for a Google account and you are not using a database to persist user accounts, this may be something you need to do.

For more information on exchanging a code for an access token and refresh token see the Google OAuth documentation.

Google also returns a email_verified boolean property in the OAuth profile.

You can use this property to restrict access to people with verified accounts at a particular domain.

**Examples**:

```text
https://example.com/api/auth/callback/google
```

```text
https://example.com/auth/callback/google
```

```text
https://example.com/auth/callback/google
```

---

## Handling Signin and Signout

**URL**: https://authjs.dev/getting-started/session-management/login

**Contents**:
- Handling Signin and Signout
    - Form Action (Server-Side)
    - Client Side
  - Signout
    - Server-side
    - Client Side

To signin your users, make sure you have at least one authentication method setup. You then need to build a button which will call the sign in function from your Auth.js framework package.

With Qwik we can do a server-side sign in with Form action, or a more simple client-side login via submit method.

The SvelteKit client supports two signin and signout methods, one server-side using Form Actions, and one client-side using requests and redirects.

To signin your users using a SvelteKit form action, we can use the SignIn component exported from @auth/sveltekit/components.

This requires a server action at /signin, this path can be customized with the signInPage prop on the SignIn component.

Client-side is a bit simpler as we just need to import a button on:click handler from @auth/sveltekit/client.

Just like in other frameworks, you can also pass a provider to the signIn function which will attempt to login directly with that provider.

The Express package runs server-side and therefore it doesn’t make sense to create a “SignIn button component”. However, to signin or signout with Express, send a request to the appropriate REST API Endpoints from your client (i.e. /auth/signin, /auth/signout, etc.).

To sign in users with Express, you can create a route that handles the sign-in logic. Here is an example:

To sign out users with Express, you can create a route that handles the sign-out logic. Here is an example:

You can also pass a provider to the signIn function which will attempt to login directly with that provider. Otherwise, when clicking this button in your application, the user will be redirected to the configured sign in page. If you did not setup a custom sign in page, the user will be redirected to the default signin page at /[basePath]/signin.

Once authenticated, the user will be redirected back to the page they started the signin from. If you want the user to be redirected somewhere else after sign in (.i.e /dashboard), you can do so by passing the t

*[Content truncated - see full docs]*

**Examples**:

```python
import { signIn } from "@/auth"
 
export function SignIn() {
  return (
    <form
      action={async () => {
        "use server"
        await signIn()
      }}
    >
      <button type="submit">Sign in</button>
    </form>
  )
}
```

```python
"use client"
import { signIn } from "next-auth/react"
 
export function SignIn() {
  return <button onClick={() => signIn()}>Sign In</button>
}
```

```python
import { component$ } from "@builder.io/qwik"
import { Form } from "@builder.io/qwik-city"
import { useSignIn } from "./plugin@auth"
 
export default component$(() => {
  const signInSig = useSignIn()
 
  return (
    <>
      {/* server-side login with Form action */}
      <Form action={signInSig}>
        <input type="hidden" name="providerId" value="${providerId}" />
        <input
          type="hidden"
          name="options.redirectTo"
          value="/"
        />
        <button>Sign
...
```

---

## Hasura Adapter

**URL**: https://authjs.dev/getting-started/adapters/hasura

**Contents**:
- Hasura Adapter
- Resources
- Setup
  - Installation
  - Environment variables
  - Configuration
  - Migrations

Tips: Track all the tables and relationships in Hasura

**Examples**:

```text
npm install @auth/hasura-adapter
```

```text
pnpm add @auth/hasura-adapter
```

```text
yarn add @auth/hasura-adapter
```

---

## Hubspot Provider

**URL**: https://authjs.dev/getting-started/providers/hubspot

**Contents**:
- Hubspot Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - Notes

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/hubspot
```

```text
https://example.com/auth/callback/hubspot
```

```text
https://example.com/auth/callback/hubspot
```

---

## Identity Server Provider

**URL**: https://authjs.dev/getting-started/providers/identity-server4

**Contents**:
- Identity Server Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

This provider has been deprecated and is superceded by Duende IdentityServer6.

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/identity-server4
```

```text
https://example.com/auth/callback/identity-server4
```

```text
https://example.com/auth/callback/identity-server4
```

---

## Instagram Provider

**URL**: https://authjs.dev/getting-started/providers/instagram

**Contents**:
- Instagram Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - Notes

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/instagram
```

```text
https://example.com/auth/callback/instagram
```

```text
https://example.com/auth/callback/instagram
```

---

## Integrations

**URL**: https://authjs.dev/getting-started/integrations

**Contents**:
- Integrations
- Community Integrations
  - Help needed

Here are the state of planned and released integrations under the @auth/* and @next-auth/* scope, as well as next-auth. It also includes community created and maintained integrations. Integrations listed as “Planned” are something we’d love help with! See the help needed section below.

Is your framework not supported? You can easily contribute by creating a framework integration by following this guide.

Note that because of preventing breaking changes on package imports, next-auth is the only framework package which is not named following the @auth/* convention. This library initially was born as next-auth but over the years has evolved to be framework agnostic.

Framework and database integrations are all based on the Auth.js Core library. In most cases, you will not interact with this package directly, as it is intended for library authors.

The community has published some great integrations / client packages for various frameworks and libraries. We’d love to make some packages official in the future, if you’re responsible for any of them and are interested in collaborating, please do not hesitate to reach out!

In case you are a maintainer of a package that uses @auth/core, feel free to reach out to Balázs or info@authjs.dev, if you want to collaborate on making it an official package, maintained in our repository. If you are interested in bringing @auth/core support to your favorite framework, we would love to hear from you!

---

## Kakao Provider

**URL**: https://authjs.dev/getting-started/providers/kakao

**Contents**:
- Kakao Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - Notes

Express not documented yet. Help us by contributing here.

Create a provider and a Kakao application at https://developers.kakao.com/console/app. In the settings of the app under Kakao Login, activate web app, change consent items and configure callback URL.

For production: https://{YOUR_DOMAIN}/api/auth/callback/kakao

For development: http://localhost:3000/api/auth/callback/kakao

Kakao’s client key is in Summary(It is written as 요약정보 in Korean.) tab’s App Keys Field (My Application > App Settings > Summary)

**Examples**:

```text
https://example.com/api/auth/callback/kakao
```

```text
https://example.com/auth/callback/kakao
```

```text
https://example.com/auth/callback/kakao
```

---

## Keycloak Provider

**URL**: https://authjs.dev/getting-started/providers/keycloak

**Contents**:
- Keycloak Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

Express not documented yet. Help us by contributing here.

Enable the “Client Authentication” option to retrieve your client secret in the Credentials tab.

Prior to v20, create an openid-connect client in Keycloak with “confidential” as the “Access Type”.

**Examples**:

```text
https://example.com/api/auth/callback/keycloak
```

```text
https://example.com/auth/callback/keycloak
```

```text
https://example.com/auth/callback/keycloak
```

---

## Kysely Adapter

**URL**: https://authjs.dev/getting-started/adapters/kysely

**Contents**:
- Kysely Adapter
- Resources
- Setup
  - Installation
  - Environment Variables
  - Configuration
  - Schema
  - Naming conventions

This adapter supports the same first party dialects that Kysely (as of v0.24.2) supports: PostgreSQL, MySQL, and SQLite. The examples below use PostgreSQL with the pg client.

Kysely’s constructor requires a database interface that contains an entry with an interface for each of your tables. You can define these types manually, or use kysely-codegen / prisma-kysely to automatically generate them. Check out the default models required by Auth.js.

An alternative to manually defining types is generating them from the database schema using kysely-codegen, or from Prisma schemas using prisma-kysely. When using generated types with KyselyAuth, import Codegen and pass it as the second generic arg:

This schema is adapted for use in Kysely and is based upon our main schema.

For more information about creating and running migrations with Kysely, refer to the Kysely migrations documentation.

If mixed snake_case and camelCase column names is an issue for you and/or your underlying database system, we recommend using Kysely’s CamelCasePlugin (see the documentation here) feature to change the field names. This won’t affect NextAuth.js, but will allow you to have consistent casing when using Kysely.

**Examples**:

```text
npm install kysely @auth/kysely-adapter
```

```text
pnpm add kysely @auth/kysely-adapter
```

```text
yarn add kysely @auth/kysely-adapter
```

---

## Line Provider

**URL**: https://authjs.dev/getting-started/providers/line

**Contents**:
- Line Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - Notes

Express not documented yet. Help us by contributing here.

Create a provider and a LINE login channel at https://developers.line.biz/console/. In the settings of the channel under LINE Login, activate web app and configure your callback URL as defined above.

**Examples**:

```text
https://example.com/api/auth/callback/line
```

```text
https://example.com/auth/callback/line
```

```text
https://example.com/auth/callback/line
```

---

## LinkedIn Provider

**URL**: https://authjs.dev/getting-started/providers/linkedin

**Contents**:
- LinkedIn Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/linkedin
```

```text
https://example.com/auth/callback/linkedin
```

```text
https://example.com/auth/callback/linkedin
```

---

## Logto Provider

**URL**: https://authjs.dev/getting-started/providers/logto

**Contents**:
- Logto Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

Qwik not documented yet. Help us by contributing here.

Express not documented yet. Help us by contributing here.

Qwik not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/logto
```

```text
https://example.com/auth/callback/logto
```

```text
AUTH_LOGTO_ID
AUTH_LOGTO_SECRET
AUTH_LOGTO_ISSUER
```

---

## Loops Provider

**URL**: https://authjs.dev/getting-started/providers/loops

**Contents**:
- Loops Provider
- Overview
- How it works
- Configuration
  - Add and Verify your Domain on Loops
  - Generate an API Key
  - Create a Transactional Email Template on Loops
  - Configure AuthJS with the Loops Provider

The Loops provider uses email to send “magic links” that contain URLs with verification tokens can be used to sign in.

Adding support for signing in via email in addition to one or more OAuth services provides a way for users to sign in if they lose access to their OAuth account (e.g. if it is locked or deleted).

The Loops provider can be used in conjunction with (or instead of) one or more OAuth providers.

On initial sign in, a Verification Token is sent to the email address provided. By default this token is valid for 24 hours. If the Verification Token is used within that time (i.e. by clicking on the link in the email) an account is created for the user and they are signed in.

If someone provides the email address of an existing account when signing in, an email is sent and they are signed into the account associated with that email address when they follow the link in the email.

The Loops provider can be used with both JSON Web Token and database managed sessions, however you must configure a database to use it. It is not possible to enable email sign in without using a database.

First, you’ll need to have completed the steps covered in the ‘Start here’ Loops documentation. The main thing required is to set up your domain records.

Next, you will have to generate an API key in the Loops Dashboard. You can save this API key as the AUTH_LOOPS_KEY environment variable.

The easiest way to achieve this is using the Loops email editor to create a transactional email template. If you’re new to Loops, you can find rich documentation here.

Copy the Transactional ID value from the last page of the template creation process, and save this as the AUTH_LOOPS_TRANSACTIONAL_ID environment variable. If you’re following these steps, you should now have two environment variables set up for Loops.

When creating your email template, make sure to include the url variable in the template. This is the URL that will sent to the user, allowing them to signin.

Qwik not documen

*[Content truncated - see full docs]*

**Examples**:

```text
AUTH_LOOPS_KEY=abc
```

```text
AUTH_LOOPS_KEY=abc
AUTH_LOOPS_TRANSACTIONAL_ID=def
```

```python
import NextAuth from "next-auth"
import Loops from "next-auth/providers/loops"
 
export const { handlers, auth, signIn, signOut } = NextAuth({
  adapter: ..., // database adapter of your choosing
  providers: [
    Loops({
      apiKey: process.env.AUTH_LOOPS_KEY,
      transactionalId: process.env.AUTH_LOOPS_TRANSACTIONAL_ID,
    }),
  ],
})
```

---

## Mailchip Provider

**URL**: https://authjs.dev/getting-started/providers/mailchimp

**Contents**:
- Mailchip Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/mailchimp
```

```text
https://example.com/auth/callback/mailchimp
```

```text
https://example.com/auth/callback/mailchimp
```

---

## Mailgun Provider

**URL**: https://authjs.dev/getting-started/providers/mailgun

**Contents**:
- Mailgun Provider
- Resources
- Overview
  - How it works
- Configuration
- Customization
  - Email Body
  - Verification Tokens

The Mailgun provider uses email to send “magic links” that contain URLs with verification tokens can be used to sign in.

Adding support for signing in via email in addition to one or more OAuth services provides a way for users to sign in if they lose access to their OAuth account (e.g. if it is locked or deleted).

The Mailgun provider can be used in conjunction with (or instead of) one or more OAuth providers.

On initial sign in, a Verification Token is sent to the email address provided. By default this token is valid for 24 hours. If the Verification Token is used within that time (i.e. by clicking on the link in the email) an account is created for the user and they are signed in.

If someone provides the email address of an existing account when signing in, an email is sent and they are signed into the account associated with that email address when they follow the link in the email.

The Mailgun provider can be used with both JSON Web Token and database managed sessions, however you must configure a database to use it. It is not possible to enable email sign in without using a database.

First, you’ll need to add your domain to your Mailgun account. This is required by Mailgun and this domain of the address you use in the from provider option.

Next, you will have to generate an API key in the Mailgun Settings. You can save this API key as the AUTH_MAILGUN_KEY environment variable.

If you name your environment variable AUTH_MAILGUN_KEY, the provider will pick it up automatically and your Auth.js configuration object can be simpler. If you’d like to rename it to something else, however, you’ll have to manually pass it into the provider in your Auth.js configuration.

Express not documented yet. Help us by contributing here.

Do not forget to setup one of the database adapters for storing the Email verification token.

You can now start the sign-in process with an email address at /api/auth/signin.

A user account (i.e. an entry in the Users table) will not 

*[Content truncated - see full docs]*

**Examples**:

```text
AUTH_MAILGUN_KEY=abc
```

```python
import NextAuth from "next-auth"
import Mailgun from "next-auth/providers/mailgun"
 
export const { handlers, auth, signIn, signOut } = NextAuth({
  adapter: ...,
  providers: [
    Mailgun({
      // If your environment variable is named differently than default
      apiKey: process.env.AUTH_MAILGUN_KEY,
      from: "no-reply@company.com",
      region: "EU",  // Optional
    }),
  ],
})
```

```python
import { QwikAuth$ } from "@auth/qwik"
import Mailgun from "@auth/qwik/providers/mailgun"
 
export const { onRequest, useSession, useSignIn, useSignOut } = QwikAuth$(
  () => ({
    providers: [
      Mailgun({
        // If your environment variable is named differently than default
        apiKey: import.meta.env.AUTH_MAILGUN_KEY,
        from: "no-reply@company.com",
        region: "EU", // Optional
      }),
    ],
  })
)
```

---

## Mailru Provider

**URL**: https://authjs.dev/getting-started/providers/mailru

**Contents**:
- Mailru Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/mailru
```

```text
https://example.com/auth/callback/mailru
```

```text
https://example.com/auth/callback/mailru
```

---

## Mastodon Provider

**URL**: https://authjs.dev/getting-started/providers/mastodon

**Contents**:
- Mastodon Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - Notes

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/mastodon
```

```text
https://example.com/auth/callback/mastodon
```

```text
https://example.com/auth/callback/mastodon
```

---

## Mattermost Provider

**URL**: https://authjs.dev/getting-started/providers/mattermost

**Contents**:
- Mattermost Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - Notes

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/mattermost
```

```text
https://example.com/auth/callback/mattermost
```

```text
https://example.com/auth/callback/mattermost
```

---

## Medium Provider

**URL**: https://authjs.dev/getting-started/providers/medium

**Contents**:
- Medium Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - Notes

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/medium
```

```text
https://example.com/auth/callback/medium
```

```text
https://example.com/auth/callback/medium
```

---

## Microsoft Entra ID

**URL**: https://authjs.dev/getting-started/providers/microsoft-entra-id

**Contents**:
- Microsoft Entra ID
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Register Application
  - Configuration
- Notes

Microsoft has renamed Azure AD to Microsoft Entra ID, more information about the new name can be found here.

Log in to the Microsoft Entra admin center.

In the left sidebar, navigate to Identity —> Applications —> App Registrations.

Click on New registration.

Give your application a name. This name will be displayed to the user when they log in.

Select the account types you want to allow to log in. The AUTH_MICROSOFT_ENTRA_ID_ISSUER variable will be based on the selection you make here.

Single tenant only - Only allow users from your organization. https://login.microsoftonline.com/<Directory (tenant) ID>/v2.0

Multi-tenant - Allow users from any organization. https://login.microsoftonline.com/organizations/v2.0

Multi-tenant + Personal - Allow any Microsoft account (work, school, personal). https://login.microsoftonline.com/common/v2.0

Personal Only - Only allow personal Microsoft accounts. https://login.microsoftonline.com/consumers/v2.0

Set the Redirect URI platform to web and the Callback URI for your application. When developing you will set this to your local host environment (example http://localhost:3000/api/auth/callback/microsoft-entra-id).

From the application overview page copy the Application (client) ID and paste it in the AUTH_MICROSOFT_ENTRA_ID_ID variable.

Navigate to Certificates & secrets and create a new client secret.

Copy the secret value (this will be hidden when you leave this page) and paste it in the AUTH_MICROSOFT_ENTRA_ID_SECRET variable.

If the issuer paramater is not set it will default to https://login.microsoftonline.com/common/v2.0.

Microsoft Entra returns the profile picture in an ArrayBuffer, instead of just a URL to the image, so our provider converts it to a base64 encoded image string and returns that instead. See Microsoft Graph profilePhoto. The default image size is 48x48 to avoid running out of space in case the session is saved as a JWT.

**Examples**:

```text
https://example.com/api/auth/callback/microsoft-entra-id
```

```text
https://example.com/auth/callback/microsoft-entra-id
```

```text
https://example.com/auth/callback/microsoft-entra-id
```

---

## MikroORM Adapter

**URL**: https://authjs.dev/getting-started/adapters/mikro-orm

**Contents**:
- MikroORM Adapter
- Resources
- Setup
  - Installation
  - Environment Variables
  - Configuration
  - Advanced usage
    - Passing custom entities

The MikroORM adapter ships with its own set of entities. If you’d like to extend them, you can optionally pass them to the adapter.

This schema is adapted for use in MikroORM and based upon our main schema

You may want to include the defaultEntities in your MikroORM configuration to include them in Migrations etc.

To achieve that include them in your “entities” array:

**Examples**:

```text
npm install @mikro-orm/core @auth/mikro-orm-adapter
```

```text
pnpm add @mikro-orm/core @auth/mikro-orm-adapter
```

```text
yarn add @mikro-orm/core @auth/mikro-orm-adapter
```

---

## MongoDB Adapter

**URL**: https://authjs.dev/getting-started/adapters/mongodb

**Contents**:
- MongoDB Adapter
- Resources
- Setup
  - Installation
  - Environment Variables
  - Configuration
  - Add the MongoDB client

The MongoDB adapter does not handle connections automatically, so you will have to make sure that you pass the Adapter a MongoClient that is connected already.

**Examples**:

```text
npm install @auth/mongodb-adapter mongodb
```

```text
pnpm add @auth/mongodb-adapter mongodb
```

```text
yarn add @auth/mongodb-adapter mongodb
```

---

## Naver Provider

**URL**: https://authjs.dev/getting-started/providers/naver

**Contents**:
- Naver Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/naver
```

```text
https://example.com/auth/callback/naver
```

```text
https://example.com/auth/callback/naver
```

---

## Neo4j Adapter

**URL**: https://authjs.dev/getting-started/adapters/neo4j

**Contents**:
- Neo4j Adapter
- Resources
- Setup
  - Installation
  - Environment Variables
  - Configuration
  - Schema
    - Node labels

The following node labels are used.

The following relationships and relationship labels are used.

This schema is adapted for use in Neo4j and is based upon our main models. Please check there for the node properties. Relationships have no properties.

Optimum indexes will vary on your edition of Neo4j i.e. community or enterprise, and in case you have your own additional data on the nodes. Below are basic suggested indexes.

2a. For Community Edition only create single-property indexes

2b. For Enterprise Edition only create composite node key constraints and indexes

**Examples**:

```text
npm install @auth/neo4j-adapter neo4j-driver
```

```text
pnpm add @auth/neo4j-adapter neo4j-driver
```

```text
yarn add @auth/neo4j-adapter neo4j-driver
```

---

## Neon Adapter

**URL**: https://authjs.dev/getting-started/adapters/neon

**Contents**:
- Neon Adapter
- Resources
- Setup
  - Installation
  - Environment Variables
  - Configuration
  - Schema

The SQL schema for the tables used by this adapter is as follows. Learn more about the models at our doc page on Database Models.

**Examples**:

```text
npm install @auth/neon-adapter @neondatabase/serverless
```

```text
pnpm add @auth/neon-adapter @neondatabase/serverless
```

```text
yarn add @auth/neon-adapter @neondatabase/serverless
```

---

## NetSuite

**URL**: https://authjs.dev/getting-started/providers/netsuite

**Contents**:
- NetSuite
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - Userinfo RESTLet Handler
  - Example Usage

NetSuite does not support http:// callback URLs. When testing locally, you can use a service like ngrok to get a local https URL.

Before setting up the provider, you will need to ensure the following is setup.

To use this provider, you’ll need to create a userinfo RESTlet in your NetSuite instance. Our userinfo URL needs to be a suitelet or RESTLet URL that gives us the information about the user. The best bet is to use the N/runtime module to get the basics first. - Here is an example of a RESTlet below. Be sure to deploy and enable access to “All Roles”.

Be sure to deploy and use the external RESTLet url of any usage of the URIs.

Above is an example of returning the basic runtime information. Be sure to create a new script record and deployment record. When you save the deployment record, you will get the URLs for your RESTlet, which we will use as the userinfo URL.

**Examples**:

```text
https://example.com/api/auth/callback/netsuite
```

```text
https://example.com/auth/callback/netsuite
```

```text
https://example.com/auth/callback/netsuite
```

---

## Netlify Provider

**URL**: https://authjs.dev/getting-started/providers/netlify

**Contents**:
- Netlify Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/netlify
```

```text
https://example.com/auth/callback/netlify
```

```text
https://example.com/auth/callback/netlify
```

---

## Nextcloud Provider

**URL**: https://authjs.dev/getting-started/providers/nextcloud

**Contents**:
- Nextcloud Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/nextcloud
```

```text
https://example.com/auth/callback/nextcloud
```

```text
https://example.com/auth/callback/nextcloud
```

---

## Nodemailer Provider

**URL**: https://authjs.dev/getting-started/providers/nodemailer

**Contents**:
- Nodemailer Provider
- Overview
  - How it works
- Configuration
- Customization
  - Email Body
  - Verification Tokens
  - Normalizing Email Addresses

The Nodemailer provider uses email to send “magic links” that contain URLs with verification tokens can be used to sign in.

Adding support for signing in via email in addition to one or more OAuth services provides a way for users to sign in if they lose access to their OAuth account (e.g. if it is locked or deleted).

The Nodemailer provider can be used in conjunction with (or instead of) one or more OAuth providers.

On initial sign in, a Verification Token is sent to the email address provided. By default this token is valid for 24 hours. If the Verification Token is used within that time (i.e. by clicking on the link in the email) an account is created for the user and they are signed in.

If someone provides the email address of an existing account when signing in, an email is sent and they are signed into the account associated with that email address when they follow the link in the email.

The Nodemailer provider can be used with both JSON Web Token and database managed sessions, however you must configure a database to use it. It is not possible to enable email sign in without using a database.

You will need an SMTP account; ideally for one of the services known to work with nodemailer. Nodemailer also works with other transports, however if you want to use an HTTP based email service, we recommend using one of the other Auth.js providers designed for those, like Resend or Sendgrid.

There are two ways to configure the SMTP server connection.

You can either use a connection string or a nodemailer configuration object.

Express not documented yet. Help us by contributing here.

Qwik not documented yet. Help us by contributing here.

Express not documented yet. Help us by contributing here.

Do not forget to setup one of the database adapters for storing the Email verification token.

You can now start the sign process with an email address at /api/auth/signin.

A user account (i.e. an entry in the Users table) will not be created for the user until the fi

*[Content truncated - see full docs]*

**Examples**:

```text
npm install nodemailer
```

```text
pnpm add nodemailer
```

```text
yarn add nodemailer
```

---

## Notion Provider

**URL**: https://authjs.dev/getting-started/providers/notion

**Contents**:
- Notion Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
- Notes

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/notion
```

```text
https://example.com/auth/callback/notion
```

```text
https://example.com/auth/callback/notion
```

---

## OAuth

**URL**: https://authjs.dev/getting-started/authentication/oauth

**Contents**:
- OAuth

Auth.js comes with over 80 providers preconfigured. We constantly test ~20 of the most popular ones, by having them enabled and actively used in our example application. You can choose a provider below to get a walk-through, or find your provider of choice in the sidebar for further details.

Or jump directly to one of the popular ones below.

---

## Okta Provider

**URL**: https://authjs.dev/getting-started/providers/okta

**Contents**:
- Okta Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/okta
```

```text
https://example.com/auth/callback/okta
```

```text
https://example.com/auth/callback/okta
```

---

## OneLogin Provider

**URL**: https://authjs.dev/getting-started/providers/onelogin

**Contents**:
- OneLogin Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/onelogin
```

```text
https://example.com/auth/callback/onelogin
```

```text
https://example.com/auth/callback/onelogin
```

---

## Osso Provider

**URL**: https://authjs.dev/getting-started/providers/osso

**Contents**:
- Osso Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - Notes

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/osso
```

```text
https://example.com/auth/callback/osso
```

```text
https://example.com/auth/callback/osso
```

---

## Osu Provider

**URL**: https://authjs.dev/getting-started/providers/osu

**Contents**:
- Osu Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - Notes

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/osu
```

```text
https://example.com/auth/callback/osu
```

```text
https://example.com/auth/callback/osu
```

---

## Passage Provider

**URL**: https://authjs.dev/getting-started/providers/passage

**Contents**:
- Passage Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/passage
```

```text
https://example.com/auth/callback/passage
```

```text
https://example.com/auth/callback/passage
```

---

## Passkey

**URL**: https://authjs.dev/getting-started/providers/passkey

**Contents**:
- Passkey
- Setup
  - Install peer dependencies
  - Database Setup
    - Edge Compatibility
  - Update Auth.js Configuration
  - Custom Pages
- Options

The WebAuthn / Passkeys provider is experimental and not yet recommended for production use.

The Passkeys provider requires a database adapter as well as a new table in that database. Please see the docs page for your adapter for the respective migration details.

Passkeys are currently supported in the following adapters / framework packages.

The @simplewebauthn/browser peer dependency is only required for custom signin pages. If you’re using the Auth.js default pages, you can skip installing that peer dependency.

The Passkeys provider requires an additional table called Authenticator. Passkeys are now supported in multiple adapters, please see their respective docs pages for more detailed migration steps. We’ll use Prisma as an example going forward here, but there is also a raw SQL migration included below.

If you’re using next-auth with Next.js and middleware, you should ensure that your database client of choice is “edge compatible”. If you’re using an older version of Prisma or another adapter that is not edge compatible, you’ll need to make some adjustments. Check out our edge compatibility guide for more details. There is also Prisma specific information in the Prisma adapter docs.

Add the Passkey provider to your configuration and make sure you’re using a compatible database adapter. You’ll also need to explicitly enable the experimental WebAuthn feature.

If you’re using the built-in Auth.js pages, then you are good to go now! Navigating to your /signin route should include a “Signin with Passkeys” button now.

If you’re building a custom signin page, you can leverage the next-auth/webauthn signIn function to initiate both WebAuthn registration and authentication. Remember, when using the WebAuthn signIn function, you’ll also need the @simplewebauth/browser peer dependency installed.

You can find all of the Passkeys provider options under the API reference.

**Examples**:

```text
npm install @simplewebauthn/browser@9.0.1 @simplewebauthn/server@9.0.3
```

```text
pnpm add @simplewebauthn/browser@9.0.1 @simplewebauthn/server@9.0.3
```

```text
yarn add @simplewebauthn/browser@9.0.1 @simplewebauthn/server@9.0.3
```

---

## Patreon Provider

**URL**: https://authjs.dev/getting-started/providers/patreon

**Contents**:
- Patreon Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/patreon
```

```text
https://example.com/auth/callback/patreon
```

```text
https://example.com/auth/callback/patreon
```

---

## Pinterest Provider

**URL**: https://authjs.dev/getting-started/providers/pinterest

**Contents**:
- Pinterest Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - Notes

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/pinterest
```

```text
https://example.com/auth/callback/pinterest
```

```text
https://example.com/auth/callback/pinterest
```

---

## Pipedrive Provider

**URL**: https://authjs.dev/getting-started/providers/pipedrive

**Contents**:
- Pipedrive Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/pipedrive
```

```text
https://example.com/auth/callback/pipedrive
```

```text
https://example.com/auth/callback/pipedrive
```

---

## PostgreSQL Adapter

**URL**: https://authjs.dev/getting-started/adapters/pg

**Contents**:
- PostgreSQL Adapter
- Resources
- Setup
  - Installation
  - Environment Variables
  - Configuration
  - Schema

If you are using Neon’s PostgreSQL like Vercel Postgres, you can use @neondatabase/serverless to work with edge runtime.

If you are using Neon’s PostgreSQL like Vercel Postgres, you can use @neondatabase/serverless to work with edge runtime.

If you are using Neon’s PostgreSQL like Vercel Postgres, you can use @neondatabase/serverless to work with edge runtime.

The SQL schema for the tables used by this adapter is as follows. Learn more about the models at our doc page on Database Models.

**Examples**:

```text
npm install @auth/pg-adapter pg
```

```text
pnpm add @auth/pg-adapter pg
```

```text
yarn add @auth/pg-adapter pg
```

---

## Postmark Provider

**URL**: https://authjs.dev/getting-started/providers/postmark

**Contents**:
- Postmark Provider
- Overview
  - How it works
- Configuration
- Customization
  - Email Body
  - Verification Tokens
  - Normalizing Email Addresses

The Postmark provider uses email to send “magic links” that contain URLs with verification tokens can be used to sign in.

Adding support for signing in via email in addition to one or more OAuth services provides a way for users to sign in if they lose access to their OAuth account (e.g. if it is locked or deleted).

The Postmark provider can be used in conjunction with (or instead of) one or more OAuth providers.

On initial sign in, a Verification Token is sent to the email address provided. By default this token is valid for 24 hours. If the Verification Token is used within that time (i.e. by clicking on the link in the email) an account is created for the user and they are signed in.

If someone provides the email address of an existing account when signing in, an email is sent and they are signed into the account associated with that email address when they follow the link in the email.

The Postmark provider can be used with both JSON Web Token and database managed sessions, however you must configure a database to use it. It is not possible to enable email sign in without using a database.

First, you’ll need to add your domain to your Postmark account. This is required by Postmark and this domain of the address you use in the from provider option.

Next, you will have to generate an API key in the Postmark Dashboard. You can save this API key as the AUTH_POSTMARK_KEY environment variable.

If you name your environment variable AUTH_POSTMARK_KEY, the provider will pick it up automatically and your Auth.js configuration object can be simpler. If you’d like to rename it to something else, however, you’ll have to manually pass it into the provider in your Auth.js configuration.

Express not documented yet. Help us by contributing here.

Do not forget to setup one of the database adapters for storing the Email verification token.

You can now start the sign-in process with an email address at /api/auth/signin.

A user account (i.e. an entry in the Users table) 

*[Content truncated - see full docs]*

**Examples**:

```text
AUTH_POSTMARK_KEY=abc
```

```python
import NextAuth from "next-auth"
import Postmark from "next-auth/providers/postmark"
 
export const { handlers, auth, signIn, signOut } = NextAuth({
  adapter: ...,
  providers: [
    Postmark({
      // If your environment variable is named differently than default
      apiKey: AUTH_POSTMARK_KEY,
      from: "no-reply@company.com"
    }),
  ],
})
```

```python
import { QwikAuth$ } from "@auth/qwik"
import Postmark from "@auth/qwik/providers/postmark"
 
export const { onRequest, useSession, useSignIn, useSignOut } = QwikAuth$(
  () => ({
    providers: [
      Postmark({
        // If your environment variable is named differently than default
        apiKey: import.meta.env.AUTH_POSTMARK_KEY,
        from: "no-reply@company.com",
      }),
    ],
  })
)
```

---

## PouchDB Adapter

**URL**: https://authjs.dev/getting-started/adapters/pouchdb

**Contents**:
- PouchDB Adapter
- Resources
- Setup
  - Installation
  - Configuration
  - Advanced usage
    - Memory-First Caching Strategy

Depending on your architecture you can use PouchDB’s http adapter to reach any database compliant with the CouchDB protocol (CouchDB, Cloudant, etc.) or use any other PouchDB compatible adapter (leveldb, in-memory, etc.)

Your PouchDB instance MUST provide the pouchdb-find plugin since it is used internally by the adapter to build and manage indexes

If you need to boost your authentication layer performance, you may use PouchDB’s powerful sync features and various adapters, to build a memory-first caching strategy.

Use an in-memory PouchDB as your main authentication database, and synchronize it with any other persisted PouchDB. You may do a one way, one-off replication at startup from the persisted PouchDB into the in-memory PouchDB, then two-way, continuous sync.

This will most likely not increase performance much in a serverless environment due to various reasons such as concurrency, function startup time increases, etc.

For more details, please see https://pouchdb.com/api.html#sync

**Examples**:

```text
npm install pouchdb pouchdb-find @auth/pouchdb-adapter
```

```text
pnpm add pouchdb pouchdb-find @auth/pouchdb-adapter
```

```text
yarn add pouchdb pouchdb-find @auth/pouchdb-adapter
```

---

## Prisma Adapter

**URL**: https://authjs.dev/getting-started/adapters/prisma

**Contents**:
- Prisma Adapter
- Resources
- Setup
  - Installation
  - Environment Variables
  - Configuration
  - Edge Compatibility
    - Old Edge Workaround

Prisma needs to set up the environment variable to establish a connection with your database and retrieve data. Prisma requires the DATABASE_URL environment variable to create the connection. For more information, read the docs.

To improve performance using Prisma ORM, we can set up the Prisma instance to ensure only one instance is created throughout the project and then import it from any file as needed. This approach avoids recreating instances of PrismaClient every time it is used. Finally, we can import the Prisma instance from the auth.ts file configuration.

We recommend using version @prisma/client@5.12.0 or above if using middleware or any other edge runtime(s). See edge compatibility below for more information.

Prisma has shipped edge runtime support for their client in version 5.12.0. You can read more about it on their edge documentation. This requires specific database drivers and therefore is only compatible with certain database types / hosting providers. Check their list of supported drivers before getting started. You can check out an example Auth.js application with next-auth and Prisma on the edge here.

For more about edge compatibility in general, check out our edge compatibility guide.

The original database edge-runtime workaround, to split your auth.ts configuration into two, will be kept below.

At the moment, Prisma is still working on being fully compatible with edge runtimes like Vercel’s. See the issue being tracked here, and Prisma’s announcement about early edge support in the 5.9.1 changelog. There are two options to deal with this issue:

Using Prisma with the jwt session strategy and @prisma/client@5.9.1 or above doesn’t require any additional modifications, other than ensuring you don’t do any database queries in your middleware.

Since @prisma/client@5.9.1, Prisma no longer throws about being incompatible with the edge runtime at instantiation, but at query time. Therefore, it is possible to import it in files being used in your

*[Content truncated - see full docs]*

**Examples**:

```text
npm install @prisma/client @auth/prisma-adapter
npm install prisma --save-dev
```

```text
pnpm add @prisma/client @auth/prisma-adapter
pnpm add prisma --save-dev
```

```text
yarn add @prisma/client @auth/prisma-adapter
yarn add prisma --dev
```

---

## Protecting Resources

**URL**: https://authjs.dev/getting-started/session-management/protecting

**Contents**:
- Protecting Resources
  - Pages
  - API Routes
  - Next.js Middleware

Protecting routes can be done generally by checking for the session and taking an action if an active session is not found, like redirecting the user to the login page or simply returning a 401: Unauthenticated response.

You can use the auth function returned from NextAuth() and exported from your auth.ts or auth.js configuration file to get the session object.

To protect a page in the Next.js Pages router, we can use auth in getServerSideProps to return the session to the page as props.

To access the session client-side using useSession(). Make sure <SessionProvider /> is wrapping your application.

Inside component$ you can use useSession loader to retrieve the current sessionStorage.

In SvelteKit, you can leverage the event.locals.auth() function that is put there by the Auth.js handle function we’re importing and using in hooks.server.ts.

By calling event.locals.auth() server-side, we can check for the session in any +page.server.ts or +layout.server.ts file and either allow the request on, or redirect to the /login page, for example.

You can protect routes by checking for the presence of a session and then redirect to a login page if the session is not present. This can either be done per route, or for a group of routes using a middleware such as the following:

Protecting API routes in the various frameworks can also be done with the auth export.

In Next.js, you can use the auth function to wrap an API route handler. The request parameter will then have an auth key on it which you can check for a valid session.

Session data can be accessed via the route event.sharedMap. So a route can be protected and redirect using something like this located in a layout.tsx or page index.tsx:

API Routes in SvelteKit work like any other server-side file in Auth.js in SvelteKit, you can access the session by calling event.locals.auth() in the +server.ts files as well.

API Routes are protected in the same way as any other route in Express, see the examples above.

Wit

*[Content truncated - see full docs]*

**Examples**:

```python
import { auth } from "@/auth"
 
export default async function Page() {
  const session = await auth()
  if (!session) return <div>Not authenticated</div>
 
  return (
    <div>
      <pre>{JSON.stringify(session, null, 2)}</pre>
    </div>
  )
}
```

```python
import { auth } from "../auth"
 
export default function Dashboard({ session }) {
  if (!session.user) return <div>Not authenticated</div>
 
  return <div>{JSON.stringify(session, null, 2)}</div>
}
 
export async function getServerSideProps(ctx) {
  const session = await auth(ctx)
 
  return {
    props: {
      session,
    },
  }
}
```

```python
import type { AppProps } from "next/app"
import { SessionProvider } from "next-auth/react"
 
export default function MyApp({
  Component,
  pageProps: { session, ...pageProps },
}: AppProps) {
  return (
    <SessionProvider session={session}>
      <Component {...pageProps} />;
    </SessionProvider>
  )
}
```

---

## Reddit Provider

**URL**: https://authjs.dev/getting-started/providers/reddit

**Contents**:
- Reddit Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - Notes

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/reddit
```

```text
https://example.com/auth/callback/reddit
```

```text
https://example.com/auth/callback/reddit
```

---

## Resend Provider

**URL**: https://authjs.dev/getting-started/providers/resend

**Contents**:
- Resend Provider
- Overview
  - How it works
- Configuration
- Customization
  - Email Body
  - Verification Tokens
  - Normalizing Email Addresses

The Resend provider uses email to send “magic links” that contain URLs with verification tokens can be used to sign in.

Adding support for signing in via email in addition to one or more OAuth services provides a way for users to sign in if they lose access to their OAuth account (e.g. if it is locked or deleted).

The Resend provider can be used in conjunction with (or instead of) one or more OAuth providers.

On initial sign in, a Verification Token is sent to the email address provided. By default this token is valid for 24 hours. If the Verification Token is used within that time (i.e. by clicking on the link in the email) an account is created for the user and they are signed in.

If someone provides the email address of an existing account when signing in, an email is sent and they are signed into the account associated with that email address when they follow the link in the email.

The Resend provider can be used with both JSON Web Token and database managed sessions, however you must configure a database to use it. It is not possible to enable email sign in without using a database.

First, you’ll need to add your domain to your Resend account. This is required by Resend and this domain of the address you use in the from provider option.

Next, you will have to generate an API key in the Resend Dashboard. You can save this API key as the AUTH_RESEND_KEY environment variable.

If you name your environment variable AUTH_RESEND_KEY, the provider will pick it up automatically and your Auth.js configuration object can be simpler. If you’d like to rename it to something else, however, you’ll have to manually pass it into the provider in your Auth.js configuration.

Express not documented yet. Help us by contributing here.

Do not forget to setup one of the database adapters for storing the Email verification token.

You can now start the sign-in process with an email address at /api/auth/signin.

A user account (i.e. an entry in the Users table) will not be crea

*[Content truncated - see full docs]*

**Examples**:

```text
AUTH_RESEND_KEY=abc
```

```python
import NextAuth from "next-auth"
import Resend from "next-auth/providers/resend"
 
export const { handlers, auth, signIn, signOut } = NextAuth({
  adapter: ...,
  providers: [
    Resend({
      // If your environment variable is named differently than default
      apiKey: AUTH_RESEND_KEY,
      from: "no-reply@company.com"
    }),
  ],
})
```

```python
import { QwikAuth$ } from "@auth/qwik"
import Resend from "@auth/qwik/providers/resend"
 
export const { onRequest, useSession, useSignIn, useSignOut } = QwikAuth$(
  () => ({
    providers: [
      Resend({
        // If your environment variable is named differently than default
        apiKey: import.meta.env.AUTH_RESEND_KEY,
        from: "no-reply@company.com",
      }),
    ],
  })
)
```

---

## SailPoint ISC Provider

**URL**: https://authjs.dev/getting-started/providers/sailpoint

**Contents**:
- SailPoint ISC Provider
- Resources
- Setup
  - Callback URL
  - Create OAuth Client
  - Environment Variables
  - Configuration
  - Profile

SailPoint Identity Secure Cloud (ISC) is an enterprise SaaS platform for identity and security. In order to use this OAuth integration, you will need an ISC tenant. If you’re a SailPoint customer or partner, please talk to your SailPoint account manager for more details. If you are a developer, check out the SailPoint Developer Community.

This provider is not shipped with any of the Auth.js packages because it is an enterprise provider for which we cannot obtain a tenant to test and ensure compatibility. That being said, we’d like to make providers like these available to our users, so we will share a copy and paste version of the provider on respective docs pages like this. The provider configuration below is provided as-is and has been submitted by a community member with access to a SailPoint tenant.

First, you’ll need to create a client in your SailPoint admin console in order to get your clientId and clientSecret. You can follow this guide, or follow the main steps below.

Unlike other Auth.js providers, this cannot be imported from the package (see the note at the top of this page for more details). However, you can copy and paste the following object into your providers array to enable this provider.

The SailPoint userprofile endpoint will return more fields, but by default the User table only supports id, name, email, and image. Therefore, if you’d like to use any of the following fields and you’re using a database adapter with Auth.js, make sure you modify the User table schema in whichever adapter and database you’re using. Then you can additionally return any of these fields from the profile callback above.

The available fields from the SailPoint userprofile endpoint response include the following.

**Examples**:

```text
https://example.com/api/auth/callback/sailpoint
```

```text
https://example.com/auth/callback/sailpoint
```

```text
https://example.com/auth/callback/sailpoint
```

---

## Salesforce Provider

**URL**: https://authjs.dev/getting-started/providers/salesforce

**Contents**:
- Salesforce Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/salesforce
```

```text
https://example.com/auth/callback/salesforce
```

```text
https://example.com/auth/callback/salesforce
```

---

## Sendgrid Provider

**URL**: https://authjs.dev/getting-started/providers/sendgrid

**Contents**:
- Sendgrid Provider
- Overview
  - How it works
- Configuration
- Customization
  - Email Body
  - Verification Tokens
  - Normalizing Email Addresses

The Sendgrid provider uses email to send “magic links” that contain URLs with verification tokens can be used to sign in.

Adding support for signing in via email in addition to one or more OAuth services provides a way for users to sign in if they lose access to their OAuth account (e.g. if it is locked or deleted).

The Sendgrid provider can be used in conjunction with (or instead of) one or more OAuth providers.

On initial sign in, a Verification Token is sent to the email address provided. By default this token is valid for 24 hours. If the Verification Token is used within that time (i.e. by clicking on the link in the email) an account is created for the user and they are signed in.

If someone provides the email address of an existing account when signing in, an email is sent and they are signed into the account associated with that email address when they follow the link in the email.

The Sendgrid provider can be used with both JSON Web Token and database managed sessions, however you must configure a database to use it. It is not possible to enable email sign in without using a database.

First, you’ll need to add your domain to your Sendgrid account. This is required by Sendgrid and this domain of the address you use in the from provider option.

Next, you will have to generate an API key in the Sendgrid Dashboard. You can save this API key as the AUTH_SENDGRID_KEY environment variable.

If you name your environment variable AUTH_SENDGRID_KEY, the provider will pick it up automatically and your Auth.js configuration object can be simpler. If you’d like to rename it to something else, however, you’ll have to manually pass it into the provider in your Auth.js configuration.

Express not documented yet. Help us by contributing here.

Do not forget to setup one of the database adapters for storing the Email verification token.

You can now start the sign-in process with an email address at /api/auth/signin.

A user account (i.e. an entry in the Users table) 

*[Content truncated - see full docs]*

**Examples**:

```text
AUTH_SENDGRID_KEY=abc
```

```python
import NextAuth from "next-auth"
import Sendgrid from "next-auth/providers/sendgrid"
 
export const { handlers, auth, signIn, signOut } = NextAuth({
  adapter: ...,
  providers: [
    Sendgrid({
      // If your environment variable is named differently than default
      apiKey: COMPANY_AUTH_SENDGRID_API_KEY,
      from: "no-reply@company.com"
    }),
  ],
})
```

```python
import { QwikAuth$ } from "@auth/qwik"
import Sendgrid from "@auth/qwik/providers/sendgrid"
 
export const { onRequest, useSession, useSignIn, useSignOut } = QwikAuth$(
  () => ({
    providers: [
      Sendgrid({
        // If your environment variable is named differently than default
        apiKey: import.meta.env.COMPANY_AUTH_SENDGRID_API_KEY,
        from: "no-reply@company.com",
      }),
    ],
  })
)
```

---

## Sequelize Adapter

**URL**: https://authjs.dev/getting-started/adapters/sequelize

**Contents**:
- Sequelize Adapter
- Resources
- Setup
  - Installation
  - Environment Variables
  - Configuration
  - Schema
- Advanced usage

You’ll also have to manually install the driver for your database of choice.

By default, the sequelize adapter will not create tables in your database. In production, best practice is to create the required tables in your database via migrations. In development, you are able to call sequelize.sync() to have sequelize create the necessary tables, foreign keys and indexes:

This schema is adapted for use in Sequelize and based upon our main schema

Sequelize models are option to customization like so:

**Examples**:

```text
npm install @auth/sequelize-adapter sequelize
```

```text
pnpm add @auth/sequelize-adapter sequelize
```

```text
yarn add @auth/sequelize-adapter sequelize
```

---

## SimpleLogin Provider

**URL**: https://authjs.dev/getting-started/providers/simplelogin

**Contents**:
- SimpleLogin Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
- Notes
  - Authorized Redirect URIs

Express not documented yet. Help us by contributing here.

The “Authorized redirect URIs” used must include your full domain and end in the callback path. By default, SimpleLogin whitelists all http[s]://localhost:* address to facilitate local development. For example;

Authorized Redirect URIs must be HTTPS for security reason (except for localhost).

**Examples**:

```text
https://example.com/api/auth/callback/simplelogin
```

```text
https://example.com/auth/callback/simplelogin
```

```text
https://example.com/auth/callback/simplelogin
```

---

## Slack Provider

**URL**: https://authjs.dev/getting-started/providers/slack

**Contents**:
- Slack Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - Notes

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/slack
```

```text
https://example.com/auth/callback/slack
```

```text
https://example.com/auth/callback/slack
```

---

## Spotify Provider

**URL**: https://authjs.dev/getting-started/providers/spotify

**Contents**:
- Spotify Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/spotify
```

```text
https://example.com/auth/callback/spotify
```

```text
https://example.com/auth/callback/spotify
```

---

## Strava Provider

**URL**: https://authjs.dev/getting-started/providers/strava

**Contents**:
- Strava Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/strava
```

```text
https://example.com/auth/callback/strava
```

```text
https://example.com/auth/callback/strava
```

---

## Supabase Adapter

**URL**: https://authjs.dev/getting-started/adapters/supabase

**Contents**:
- Supabase Adapter
- Resources
- Setup
  - Installation
  - Environment Variables
  - Configuration
  - Schema
  - Expose the NextAuth schema in Supabase

This adapter is developed by the community and not officially maintained or supported by Supabase. It uses the Supabase Database to store user and session data in a separate next_auth schema. It is a standalone Auth server that does not interface with Supabase Auth and therefore provides a different feature set.

If you’re looking for an officially maintained Auth server with additional features like built-in email server, phone auth, and Multi Factor Authentication (MFA / 2FA), please use Supabase Auth with the Auth Helpers for Next.js.

Setup your database as described in our main schema, by copying the SQL schema below in the Supabase SQL Editor.

Alternatively you can select the NextAuth Quickstart card on the SQL Editor page, or create a migration with the Supabase CLI.

Expose the next_auth schema via the Serverless API in the API settings by adding next_auth to the “Exposed schemas” list.

When developing locally add next_auth to the schemas array in the config.toml file in the supabase folder that was generated by the Supabase CLI.

Postgres provides a powerful feature called Row Level Security (RLS) to limit access to data.

This works by sending a signed JWT to your Supabase Serverless API. There is two steps to make this work with NextAuth:

To sign the JWT use the jsonwebtoken package:

Using the session callback create the Supabase access_token and append it to the session object.

To sign the JWT use the Supabase JWT secret which can be found in the API settings

For example, given the following public schema:

The supabaseAccessToken is now available on the session object and can be passed to the supabase-js client. This works in any environment: client-side, server-side (API routes, SSR), as well as in middleware edge functions!

You can pass types that were generated with the Supabase CLI to the Supabase Client to get enhanced type safety and auto-completion.

Creating a new supabase client object:

In order to extend the session object with the sup

*[Content truncated - see full docs]*

**Examples**:

```text
npm install @supabase/supabase-js @auth/supabase-adapter
```

```text
pnpm add @supabase/supabase-js @auth/supabase-adapter
```

```text
yarn add @supabase/supabase-js @auth/supabase-adapter
```

---

## SurrealDB Adapter

**URL**: https://authjs.dev/getting-started/adapters/surrealdb

**Contents**:
- SurrealDB Adapter
- Resources
- Setup
  - Installation
  - Environment Variables
  - Configuration
  - Utils File
  - Authorization

A valid authentication combination must be provided. The following authentication combinations are supported:

The SurrealDB adapter does not handle connections automatically, so you will have to make sure that you pass the Adapter a SurrealDBClient that is connected already. Below you can see an example how to do this.

The clientPromise provides a connection to the database. You could use any connect option you wish. For quick setup, use the DatabaseAuth method. For best security, we recommend creating a Record Access method if you know how to properly setup access table permissions.

With this configuration, we can use the database’s http endpoint. Thus, the AUTH_SURREAL_URL should begin with http or https.

With this configuration, we can use the database’s websocket endpoint. Thus, the AUTH_SURREAL_URL should begin with ws or wss.

**Examples**:

```text
npm install @auth/surrealdb-adapter surrealdb
```

```text
pnpm add @auth/surrealdb-adapter surrealdb
```

```text
yarn add @auth/surrealdb-adapter surrealdb
```

---

## Threads Provider

**URL**: https://authjs.dev/getting-started/providers/threads

**Contents**:
- Threads Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - Notes

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/threads
```

```text
https://example.com/auth/callback/threads
```

```text
https://example.com/auth/callback/threads
```

---

## TikTok Provider

**URL**: https://authjs.dev/getting-started/providers/tiktok

**Contents**:
- TikTok Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - Notes

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/tiktok
```

```text
https://example.com/auth/callback/tiktok
```

```text
https://example.com/auth/callback/tiktok
```

---

## Todoist Provider

**URL**: https://authjs.dev/getting-started/providers/todoist

**Contents**:
- Todoist Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/todoist
```

```text
https://example.com/auth/callback/todoist
```

```text
https://example.com/auth/callback/todoist
```

---

## Trakt Provider

**URL**: https://authjs.dev/getting-started/providers/trakt

**Contents**:
- Trakt Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - Notes

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/trakt
```

```text
https://example.com/auth/callback/trakt
```

```text
https://example.com/auth/callback/trakt
```

---

## Twitch Provider

**URL**: https://authjs.dev/getting-started/providers/twitch

**Contents**:
- Twitch Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - Notes

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/twitch
```

```text
https://example.com/auth/callback/twitch
```

```text
https://example.com/auth/callback/twitch
```

---

## Twitter/X Provider

**URL**: https://authjs.dev/getting-started/providers/twitter

**Contents**:
- Twitter/X Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - Notes

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/twitter
```

```text
https://example.com/auth/callback/twitter
```

```text
https://example.com/auth/callback/twitter
```

---

## TypeORM Adapter

**URL**: https://authjs.dev/getting-started/adapters/typeorm

**Contents**:
- TypeORM Adapter
- Resources
- Setup
  - Installation
  - Environment Variables
  - Configuration
  - Advanced usage
    - Custom models

TypeORMAdapter takes either a connection string, or a ConnectionOptions object as its first parameter.

The TypeORM adapter uses Entity classes to define the shape of your data.

You can override the default entities and add additional fields with a custom entities file.

The synchronize: true option in TypeORM will generate SQL that exactly matches the entities. This will automatically apply any changes it finds in the entity model. This is a useful option in development.

synchronize: true should not be enabled against production databases as it may cause data loss if the configured schema does not match the expected schema! We recommend that you synchronize/migrate your production database at build-time.

If mixed snake_case and camelCase column names are an issue for you and/or your underlying database system, we recommend using TypeORM’s naming strategy feature to change the target field names. There is a package called typeorm-naming-strategies which includes a snake_case strategy which will translate the fields from how Auth.js expects them, to snake_case in the actual database.

For example, you can add the naming convention option to the connection object in your NextAuth config.

**Examples**:

```text
npm install @auth/typeorm-adapter typeorm
```

```text
pnpm add @auth/typeorm-adapter typeorm
```

```text
yarn add @auth/typeorm-adapter typeorm
```

---

## TypeScript

**URL**: https://authjs.dev/getting-started/typescript

**Contents**:
- TypeScript
- Philosophy
- Module Augmentation
- Resources

Auth.js is committed to type-safety, so it’s written in TypeScript and 100% type safe. It comes with its own type definitions to use in your project.

Even if you don’t use TypeScript, IDEs like VS Code will pick this up to provide you with a better developer experience. While you are typing, you will get suggestions about what certain objects/functions look like, and sometimes links to documentation, examples, and other valuable resources.

We have chosen module augmentation over generics as the main technique to type Auth.js resources across your application in case you extend them.

The interfaces that are shared across submodules are not passed to Auth.js library functions as generics.

Whenever these types are used, the functions always expect to return these formats. With generics, one might be able to override the type in one place, but not the other, which would cause the types to be out of sync with the implementation.

With module augmentation, you defined the types once, and you can be sure that they are always the same where it’s expected.

Auth.js libraries come with certain interfaces that are shared across submodules and different Auth.js libraries (For example: next-auth and @auth/prisma-adapter will rely on types from @auth/core).

Good examples of such interfaces are Session or User. You can use TypeScript’s Module Augmentation to extend these types to add your own properties across Auth.js without having to pass generic all over the place.

Let’s look at extending Session for example.

Module augmentation is not limited to specific interfaces. You can augment any interface we’ve defined, here are some of the more common interfaces that you might want to override based on your use case.

The module declaration can be added to any file that is “included” in your project’s tsconfig.json.

**Examples**:

```python
import NextAuth, { type DefaultSession } from "next-auth"
 
declare module "next-auth" {
  /**
   * Returned by `auth`, `useSession`, `getSession` and received as a prop on the `SessionProvider` React Context
   */
  interface Session {
    user: {
      /** The user's postal address. */
      address: string
      /**
       * By default, TypeScript merges new interface properties and overwrites existing ones.
       * In this case, the default session user properties will be overwritten,
     
...
```

```python
import { DefaultSession, QwikAuth$ } from "@auth/qwik"
 
declare module "@auth/qwik" {
  /**
   * Returned by the `useSession` hook and the `session` object in the sharedMap
   */
  interface Session {
    user: {
      /** The user's postal address. */
      address: string
      /**
       * By default, TypeScript merges new interface properties and overwrites existing ones.
       * In this case, the default session user properties will be overwritten,
       * with the new ones defined above
...
```

```python
import SvelteKitAuth, { type DefaultSession } from "@auth/sveltekit"
 
declare module "@auth/sveltekit" {
  interface Session {
    user: {
      userId: string
      /**
       * By default, TypeScript merges new interface properties and overwrites existing ones.
       * In this case, the default session user properties will be overwritten,
       * with the new ones defined above. To keep the default session user properties,
       * you need to add them back into the newly declared interface
...
```

---

## United Effects Provider

**URL**: https://authjs.dev/getting-started/providers/united-effects

**Contents**:
- United Effects Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - Notes

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/united-effects
```

```text
https://example.com/auth/callback/united-effects
```

```text
https://example.com/auth/callback/united-effects
```

---

## Unstorage Adapter

**URL**: https://authjs.dev/getting-started/adapters/unstorage

**Contents**:
- Unstorage Adapter
- Resources
- Setup
  - Installation
  - Configuration
  - Advanced usage
    - Using multiple apps with a single storage
    - Using getItemRaw/setItemRaw instead of getItem/setItem

If you have multiple Auth.js connected apps using the same storage, you need different key prefixes for every app.

You can change the prefixes by passing an options object as the second argument to the adapter factory function.

The default values for this object are:

Usually changing the baseKeyPrefix should be enough for this scenario, but for more custom setups, you can also change the prefixes of every single key.

If you are using storage that supports JSON, you can make it use getItemRaw/setItemRaw instead of getItem/setItem.

This is an experimental feature. Please check unjs/unstorage#142 for more information.

You can enable this functionality by passing useItemRaw: true (default: false) in the options object as the second argument to the adapter factory function.

**Examples**:

```text
npm install unstorage @auth/unstorage-adapter
```

```text
pnpm add unstorage @auth/unstorage-adapter
```

```text
yarn add unstorage @auth/unstorage-adapter
```

---

## Upgrade Guide (NextAuth.js v5)

**URL**: https://authjs.dev/getting-started/migrating-to-v5

**Contents**:
- Upgrade Guide (NextAuth.js v5)
- New Features
    - Main changes
    - Universal auth()
- Breaking Changes
- Migration
  - Configuration File
- Authenticating server-side

This guide only applies to next-auth upgrades for users of Next.js. Feel free to skip to the next section, Installation, if you are not upgrading to next-auth@5.

NextAuth.js version 5 is a major rewrite of the next-auth package, that being said, we introduced as few breaking changes as possible. For all else, this document will guide you through the migration process.

Get started by installing the latest version of next-auth with the beta tag.

One of our goals was to avoid exporting your configuration from one file and passing it around as authOptions throughout your application. To achieve this, we settled on moving the configuration file to the root of the repository and having it export the necessary functions you can use everywhere else. (auth, signIn, signOut, handlers etc.).

The configuration file should look very similar to your previous route-based Auth.js configuration. Except that we’re doing it in a new file in the root of the repository now, and we’re exporting methods to be used elsewhere. Below is a simple example of a v5 configuration file.

Some things to note about the new configuration:

The old configuration file, contained in the API Route (pages/api/auth/[...nextauth].ts / app/api/auth/[...nextauth]/route.ts), now becomes much shorter. These exports are designed to be used in an App Router API Route, but the rest of your app can stay in the Pages Router if you are gradually migrating!

Auth.js has had a few different ways to authenticate server-side in the past, so we’ve tried to simplify this as much as possible.

Now that Next.js components are server-first by default, and thanks to the investment in using standard Web APIs, we were able to simplify the authentication process to a single auth() function call in most cases.

See the table below for a summary of the changes. Below that are diff examples of how to use the new auth() method in various environments and contexts.

Auth.js v4 has supported reading the session in Server Components

*[Content truncated - see full docs]*

**Examples**:

```text
npm install next-auth@beta
```

```text
pnpm add next-auth@beta
```

```text
yarn add next-auth@beta
```

---

## Upstash Redis Adapter

**URL**: https://authjs.dev/getting-started/adapters/upstash-redis

**Contents**:
- Upstash Redis Adapter
- Resources
- Setup
  - Installation
  - Environment Variables
  - Configuration
  - Advanced usage
    - Using multiple apps with a single Upstash Redis instance

The Upstash free-tier allows for only one Redis instance. If you have multiple Auth.js connected apps using this instance, you need different key prefixes for every app.

You can change the prefixes by passing an options object as the second argument to the adapter factory function.

The default values for this object are:

Usually changing the baseKeyPrefix should be enough for this scenario, but for more custom setups, you can also change the prefixes of every single key.

**Examples**:

```text
npm install @upstash/redis @auth/upstash-redis-adapter
```

```text
pnpm add @upstash/redis @auth/upstash-redis-adapter
```

```text
yarn add @upstash/redis @auth/upstash-redis-adapter
```

---

## VK Provider

**URL**: https://authjs.dev/getting-started/providers/vk

**Contents**:
- VK Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - Notes

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/vk
```

```text
https://example.com/auth/callback/vk
```

```text
https://example.com/auth/callback/vk
```

---

## Vipps MobilePay Provider

**URL**: https://authjs.dev/getting-started/providers/vipps-mobilepay

**Contents**:
- Vipps MobilePay Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Test API
  - Configuration

Vipps MobilePay is a widespread mobile payment application for mobile in Norway, Sweden, Denmark and Finland. The brand is split, where you have Vipps in Norway and Sweden, and MobilePay in Denmark and Finland, but both brands/apps are using the same API.

Express not documented yet. Help us by contributing here.

To use the test mode, you need to override the issuer with the test API endpoint.

**Examples**:

```text
https://example.com/api/auth/callback/vipps
```

```text
https://example.com/auth/callback/vipps
```

```text
https://example.com/auth/callback/vipps
```

---

## WebAuthn (Passkeys)

**URL**: https://authjs.dev/getting-started/authentication/webauthn

**Contents**:
- WebAuthn (Passkeys)
  - Install peer dependencies
  - Apply the required schema Migrations
  - Update Auth.js Configuration
  - Custom Pages

The WebAuthn / Passkeys provider is experimental and not recommended for production use.

The WebAuthn provider requires changes to all of the framework integration as well as any database adapter that plans to support it. Therefore, the WebAuthn provider is currently only supported in the following framework integration and database adapters. Support for more frameworks and adapters are coming soon.

The @simplewebauthn/browser peer dependency is only required for custom signin pages. If you’re using the Auth.js default pages, you can skip installing that peer dependency.

This is the raw SQL migration for PostgreSQL, for more details including example migrations for other databases, check out the updated Prisma schemas at the @auth/prisma-adapter docs.

In short, the Passkeys provider requires an additional table called Authenticator.

Add the Passkeys provider to your configuration. Also make sure you’re using a compatible database adapter.

If you’re using the built-in Auth.js pages, then you are good to go! Navigating to your /signin route should include a “Signin with Passkeys” button.

If you’re using a custom signin page, you can leverage the next-auth signIn function to initiate WebAuthn registration and login flows with the following code.

When using the WebAuthn signIn function, you’ll also need the @simplewebauth/browser peer dependency installed.

**Examples**:

```text
npm install @simplewebauthn/server@9.0.3 @simplewebauthn/browser@9.0.1
```

```text
pnpm add @simplewebauthn/server@9.0.3 @simplewebauthn/browser@9.0.1
```

```text
yarn add @simplewebauthn/server@9.0.3 @simplewebauthn/browser@9.0.1
```

---

## Webex Provider

**URL**: https://authjs.dev/getting-started/providers/webex

**Contents**:
- Webex Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - Notes

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/webex
```

```text
https://example.com/auth/callback/webex
```

```text
https://example.com/auth/callback/webex
```

---

## What is Auth.js?

**URL**: https://authjs.dev/getting-started

**Contents**:
- What is Auth.js?
- Authentication methods
  - Official Providers
  - Supported Databases

Auth.js is a runtime agnostic library based on standard Web APIs that integrates deeply with multiple modern JavaScript frameworks to provide an authentication experience that’s simple to get started with, easy to extend, and always private and secure!

This documentation covers next-auth@5.0.0-beta and later and all other frameworks under the @auth/* namespace. Documentation for next-auth@4.x.y can still be found at next-auth.js.org.

Select your framework of choice to get started, or view the example application deployment or repository with the buttons below.

Check the integrations page for all supported packages. We are working on supporting more frameworks, but you can create your own or help us create one for your favorite framework.

There are 4 ways to authenticate users with Auth.js:

Optionally, Auth.js can be integrated with an external database via Database adapters, in case you need or want to store user data.

---

## Wikimedia Provider

**URL**: https://authjs.dev/getting-started/providers/wikimedia

**Contents**:
- Wikimedia Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - Notes

Express not documented yet. Help us by contributing here.

After registration, you can initially test your application only with your own Wikimedia account. You may have to wait several days for the application to be approved for it to be used by everyone.

This provider also supports all Wikimedia projects:

Please be aware that Wikimedia accounts do not have to have an associated email address. So you may want to add check if the user has an email address before allowing them to login.

**Examples**:

```text
https://example.com/api/auth/callback/wikimedia
```

```text
https://example.com/auth/callback/wikimedia
```

```text
https://example.com/auth/callback/wikimedia
```

---

## WordPress Provider

**URL**: https://authjs.dev/getting-started/providers/wordpress

**Contents**:
- WordPress Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/wordpress
```

```text
https://example.com/auth/callback/wordpress
```

```text
https://example.com/auth/callback/wordpress
```

---

## WorkOS Provider

**URL**: https://authjs.dev/getting-started/providers/workos

**Contents**:
- WorkOS Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

Express not documented yet. Help us by contributing here.

WorkOS also requires you to pass in your connection ID to the provider.

**Examples**:

```text
https://example.com/api/auth/callback/workos
```

```text
https://example.com/auth/callback/workos
```

```text
https://example.com/auth/callback/workos
```

---

## Xata Adapter

**URL**: https://authjs.dev/getting-started/adapters/xata

**Contents**:
- Xata Adapter
- Resources
- Setup
  - Installation
  - Configuration
  - Xata Setup

This adapter allows using Auth.js with Xata as a database to store users, sessions, and more. The preferred way to create a Xata project and use Xata databases is using the Xata Command Line Interface (CLI).

The CLI allows generating a XataClient that will help you work with Xata in a safe way, and that this adapter depends on.

When you’re ready, let’s create a new Xata project using our Auth.js schema that the Xata adapter can work with. To do that, copy and paste this schema file into your project’s directory:

Now, run the following command:

The CLI will walk you through a setup process where you choose a workspace (kind of like a GitHub org or a Vercel team) and an appropriate database. We recommend using a fresh database for this, as we’ll augment it with tables that Auth.js needs.

**Examples**:

```text
npm install @auth/xata-adapter
```

```text
pnpm add @auth/xata-adapter
```

```text
yarn add @auth/xata-adapter
```

---

## Yandex Provider

**URL**: https://authjs.dev/getting-started/providers/yandex

**Contents**:
- Yandex Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/yandex
```

```text
https://example.com/auth/callback/yandex
```

```text
https://example.com/auth/callback/yandex
```

---

## Zitadel Provider

**URL**: https://authjs.dev/getting-started/providers/zitadel

**Contents**:
- Zitadel Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration
  - Notes

Express not documented yet. Help us by contributing here.

The Redirect URIs used when creating the credentials must include your full domain and end in the callback path. For example:

Make sure to enable dev mode in ZITADEL console to allow redirects for local development.

ZITADEL also returns a email_verified boolean property in the profile. You can use this property to restrict access to people with verified accounts.

**Examples**:

```text
https://example.com/api/auth/callback/zitadel
```

```text
https://example.com/auth/callback/zitadel
```

```text
https://example.com/auth/callback/zitadel
```

---

## Zoho Provider

**URL**: https://authjs.dev/getting-started/providers/zoho

**Contents**:
- Zoho Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/zoho
```

```text
https://example.com/auth/callback/zoho
```

```text
https://example.com/auth/callback/zoho
```

---

## Zoom Provider

**URL**: https://authjs.dev/getting-started/providers/zoom

**Contents**:
- Zoom Provider
- Resources
- Setup
  - Callback URL
  - Environment Variables
  - Configuration

Express not documented yet. Help us by contributing here.

**Examples**:

```text
https://example.com/api/auth/callback/zoom
```

```text
https://example.com/auth/callback/zoom
```

```text
https://example.com/auth/callback/zoom
```

---

## 

**URL**: https://authjs.dev/getting-started/installation

**Contents**:
  - Installing Auth.js
  - Setup Environment
  - Configure
  - Setup Authentication Methods

Start by installing the appropriate package for your framework.

Installing @auth/core is not necessary, as a user you should never have to interact with @auth/core.

The only environment variable that is mandatory is the AUTH_SECRET. This is a random value used by the library to encrypt tokens and email verification hashes. (See Deployment to learn more). You can generate one via the official Auth.js CLI running:

This will also add it to your .env file, respecting the framework conventions (eg.: Next.js’ .env.local).

Next, create the Auth.js config file and object. This is where you can control the behaviour of the library and specify custom authentication logic, adapters, etc. We recommend all frameworks to create an auth.ts file in the project. In this file we’ll pass in all the options to the framework specific initialization function and then export the route handler(s), signin and signout methods, and more.

You can name this file whatever you want and place it wherever you like, these are just conventions we’ve come up with.

This file must be an App Router Route Handler, however, the rest of your app can stay under page/ if you’d like.

Note this creates the Auth.js API, but does not yet protect resources. Continue on to protecting resources for more details.

With that, the basic setup is complete! Next we’ll setup the first authentication methods and fill out that providers array.

**Examples**:

```text
npm install next-auth@beta
```

```text
pnpm add next-auth@beta
```

```text
yarn add next-auth@beta
```

---

## 

**URL**: https://authjs.dev/getting-started/installation?framework=SvelteKit

**Contents**:
  - Installing Auth.js
  - Setup Environment
  - Configure
  - Setup Authentication Methods

Start by installing the appropriate package for your framework.

Installing @auth/core is not necessary, as a user you should never have to interact with @auth/core.

The only environment variable that is mandatory is the AUTH_SECRET. This is a random value used by the library to encrypt tokens and email verification hashes. (See Deployment to learn more). You can generate one via the official Auth.js CLI running:

This will also add it to your .env file, respecting the framework conventions (eg.: Next.js’ .env.local).

Next, create the Auth.js config file and object. This is where you can control the behaviour of the library and specify custom authentication logic, adapters, etc. We recommend all frameworks to create an auth.ts file in the project. In this file we’ll pass in all the options to the framework specific initialization function and then export the route handler(s), signin and signout methods, and more.

You can name this file whatever you want and place it wherever you like, these are just conventions we’ve come up with.

This file must be an App Router Route Handler, however, the rest of your app can stay under page/ if you’d like.

Note this creates the Auth.js API, but does not yet protect resources. Continue on to protecting resources for more details.

With that, the basic setup is complete! Next we’ll setup the first authentication methods and fill out that providers array.

**Examples**:

```text
npm install next-auth@beta
```

```text
pnpm add next-auth@beta
```

```text
yarn add next-auth@beta
```

---

## 

**URL**: https://authjs.dev/getting-started/installation?framework=Express

**Contents**:
  - Installing Auth.js
  - Setup Environment
  - Configure
  - Setup Authentication Methods

Start by installing the appropriate package for your framework.

Installing @auth/core is not necessary, as a user you should never have to interact with @auth/core.

The only environment variable that is mandatory is the AUTH_SECRET. This is a random value used by the library to encrypt tokens and email verification hashes. (See Deployment to learn more). You can generate one via the official Auth.js CLI running:

This will also add it to your .env file, respecting the framework conventions (eg.: Next.js’ .env.local).

Next, create the Auth.js config file and object. This is where you can control the behaviour of the library and specify custom authentication logic, adapters, etc. We recommend all frameworks to create an auth.ts file in the project. In this file we’ll pass in all the options to the framework specific initialization function and then export the route handler(s), signin and signout methods, and more.

You can name this file whatever you want and place it wherever you like, these are just conventions we’ve come up with.

This file must be an App Router Route Handler, however, the rest of your app can stay under page/ if you’d like.

Note this creates the Auth.js API, but does not yet protect resources. Continue on to protecting resources for more details.

With that, the basic setup is complete! Next we’ll setup the first authentication methods and fill out that providers array.

**Examples**:

```text
npm install next-auth@beta
```

```text
pnpm add next-auth@beta
```

```text
yarn add next-auth@beta
```

---

## 

**URL**: https://authjs.dev/getting-started/installation?framework=Qwik

**Contents**:
  - Installing Auth.js
  - Setup Environment
  - Configure
  - Setup Authentication Methods

Start by installing the appropriate package for your framework.

Installing @auth/core is not necessary, as a user you should never have to interact with @auth/core.

The only environment variable that is mandatory is the AUTH_SECRET. This is a random value used by the library to encrypt tokens and email verification hashes. (See Deployment to learn more). You can generate one via the official Auth.js CLI running:

This will also add it to your .env file, respecting the framework conventions (eg.: Next.js’ .env.local).

Next, create the Auth.js config file and object. This is where you can control the behaviour of the library and specify custom authentication logic, adapters, etc. We recommend all frameworks to create an auth.ts file in the project. In this file we’ll pass in all the options to the framework specific initialization function and then export the route handler(s), signin and signout methods, and more.

You can name this file whatever you want and place it wherever you like, these are just conventions we’ve come up with.

This file must be an App Router Route Handler, however, the rest of your app can stay under page/ if you’d like.

Note this creates the Auth.js API, but does not yet protect resources. Continue on to protecting resources for more details.

With that, the basic setup is complete! Next we’ll setup the first authentication methods and fill out that providers array.

**Examples**:

```text
npm install next-auth@beta
```

```text
pnpm add next-auth@beta
```

```text
yarn add next-auth@beta
```

---

## 

**URL**: https://authjs.dev/getting-started/installation?framework=Next.js

**Contents**:
  - Installing Auth.js
  - Setup Environment
  - Configure
  - Setup Authentication Methods

Start by installing the appropriate package for your framework.

Installing @auth/core is not necessary, as a user you should never have to interact with @auth/core.

The only environment variable that is mandatory is the AUTH_SECRET. This is a random value used by the library to encrypt tokens and email verification hashes. (See Deployment to learn more). You can generate one via the official Auth.js CLI running:

This will also add it to your .env file, respecting the framework conventions (eg.: Next.js’ .env.local).

Next, create the Auth.js config file and object. This is where you can control the behaviour of the library and specify custom authentication logic, adapters, etc. We recommend all frameworks to create an auth.ts file in the project. In this file we’ll pass in all the options to the framework specific initialization function and then export the route handler(s), signin and signout methods, and more.

You can name this file whatever you want and place it wherever you like, these are just conventions we’ve come up with.

This file must be an App Router Route Handler, however, the rest of your app can stay under page/ if you’d like.

Note this creates the Auth.js API, but does not yet protect resources. Continue on to protecting resources for more details.

With that, the basic setup is complete! Next we’ll setup the first authentication methods and fill out that providers array.

**Examples**:

```text
npm install next-auth@beta
```

```text
pnpm add next-auth@beta
```

```text
yarn add next-auth@beta
```

---
