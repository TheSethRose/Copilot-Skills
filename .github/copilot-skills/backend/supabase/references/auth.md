# Supabase - Auth

**Pages**: 46

---

## Auth | Supabase Docs

**URL**: https://supabase.com/docs/guides/auth

**Contents**:
- Auth
- Use Supabase to authenticate and authorize your users.
- About authentication and authorization#
- The Supabase ecosystem#
- Providers#
  - Social Auth#
      - Apple
      - Azure (Microsoft)

Use Supabase to authenticate and authorize your users.

Supabase Auth makes it easy to implement authentication and authorization in your app. We provide client SDKs and API endpoints to help you create and manage users.

Your users can use many popular Auth methods, including password, magic link, one-time password (OTP), social login, and single sign-on (SSO).

Authentication and authorization are the core responsibilities of any Auth system.

Supabase Auth uses JSON Web Tokens (JWTs) for authentication. For a complete reference of all JWT fields, see the JWT Fields Reference. Auth integrates with Supabase's database features, making it easy to use Row Level Security (RLS) for authorization.

You can use Supabase Auth as a standalone product, but it's also built to integrate with the Supabase ecosystem.

Auth uses your project's Postgres database under the hood, storing user data and other Auth information in a special schema. You can connect this data to your own tables using triggers and foreign key references.

Auth also enables access control to your database's automatically generated REST API. When using Supabase SDKs, your data requests are automatically sent with the user's Auth Token. The Auth Token scopes database access on a row-by-row level when used along with RLS policies.

Supabase Auth works with many popular Auth methods, including Social and Phone Auth using third-party providers. See the following sections for a list of supported third-party providers.

Charges apply to Monthly Active Users (MAU), Monthly Active Third-Party Users (Third-Party MAU), and Monthly Active SSO Users (SSO MAU) and Advanced MFA Add-ons. For a detailed breakdown of how these charges are calculated, refer to the following pages:

Latest product updates?

Something's not right?

---

## Email Templates | Supabase Docs

**URL**: https://supabase.com/docs/guides/auth/auth-email-templates

**Contents**:
- Email Templates
- Learn how to manage the email templates in Supabase.
- Terminology#
- Editing email templates#
- Mobile deep linking#
- Limitations#
  - Email prefetching#
  - Email tracking#

Learn how to manage the email templates in Supabase.

You can customize the email messages used for the authentication flows. You can edit the following email templates:

The templating system provides the following variables for use:

On hosted Supabase projects, edit your email templates on the Email Templates page. On self-hosted projects or in local development, edit your configuration files.

You can also manage email templates using the Management API:

For mobile applications, you might need to link or redirect to a specific page within your app. See the Mobile Deep Linking guide to set this up.

Certain email providers may have spam detection or other security features that prefetch URL links from incoming emails (e.g. Safe Links in Microsoft Defender for Office 365). In this scenario, the {{ .ConfirmationURL }} sent will be consumed instantly which leads to a "Token has expired or is invalid" error. To guard against this:

Use an email OTP instead by including {{ .Token }} in the email template.

Create your own custom email link to redirect the user to a page where they can click on a button to confirm the action. For example, you can include the following in your email template:

The user should be brought to a page on your site where they can confirm the action by clicking a button. The button should contain the actual confirmation link which can be obtained from parsing the confirmation_url={{ .ConfirmationURL }} query parameter in the URL.

If you are using an external email provider that enables "email tracking", the links inside the Supabase email templates will be overwritten and won't perform as expected. We recommend disabling email tracking to ensure email links are not overwritten.

If you intend to use Server-side rendering, you might want the email link to redirect the user to a server-side endpoint to check if they are authenticated before returning the page. However, the default email link will redirect the user after verification to the red

*[Content truncated - see full docs]*

**Examples**:

```text
12345678910111213141516171819202122232425# Get your access token from https://supabase.com/dashboard/account/tokensexport SUPABASE_ACCESS_TOKEN="your-access-token"export PROJECT_REF="your-project-ref"# Get current email templatescurl -X GET "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" \  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \  | jq 'to_entries | map(select(.key | startswith("mailer_templates"))) | from_entries'# Update email templatescurl -X PATCH "https://api.sup
...
```

```text
123<a href="{{ .SiteURL }}/confirm-signup?confirmation_url={{ .ConfirmationURL }}"  >Confirm your signup</a>
```

```text
1234<a  href="https://api.example.com/v1/authenticate?token_hash={{ .TokenHash }}&type=invite&redirect_to={{ .RedirectTo }}"  >Accept the invite</a>
```

---

## Glossary | Supabase Docs

**URL**: https://supabase.com/docs/guides/resources/glossary

**Contents**:
- Glossary
- Access token#
- Authentication#
- Authenticator app#
- Authorization#
- Identity provider#
- JSON Web Token (JWT)#
- JWT signing secret#

Definitions for terminology and acronyms used in the Supabase documentation.

An access token is a short-lived (usually no more than 1 hour) token that authorizes a client to access resources on a server. It comes in the form of a JSON Web Token (JWT).

Authentication (often abbreviated authn.) is the process of verifying the identity of a user. Verification of the identity of a user can happen in multiple ways:

An authenticator app generates time-based one-time passwords (TOTPs). These passwords are generated based off a long and difficult to guess secret string. The secret is initially passed to the application by scanning a QR code.

Authorization (often abbreviated authz.) is the process of verifying if a certain identity is allowed to access resources. Authorization often occurs by verifying an access token.

An identity provider is software or service that allows third-party applications to identify users without the exchange of passwords. Social login and enterprise single-sign on won't be possible without identity providers.

Social login platforms typically use the OAuth protocol, while enterprise single-sign on is based on the OIDC or SAML protocols.

A JSON Web Token is a type of data structure, represented as a string, that usually contains identity and authorization information about a user. It encodes information about its lifetime and is signed with cryptographic key making it tamper resistant.

Access tokens are JWTs and by inspecting the information they contain you can allow or deny access to resources. Row level security policies are based on the information present in JWTs.

JWTs issued by Supabase are signed using the HMAC-SHA256 algorithm. The secret key used in the signing is called the JWT signing secret. You should not share this secret with someone or some thing you don't trust, nor should you post it publicly. Anyone with access to the secret can create arbitrary JWTs.

Multi-factor authentication is the process of authenticating a user's

*[Content truncated - see full docs]*

---

## Identities | Supabase Docs

**URL**: https://supabase.com/docs/guides/auth/identities

**Contents**:
- Identities
- The user identity object#
  - Is this helpful?

An identity is an authentication method associated with a user. Supabase Auth supports the following types of identity:

A user can have more than one identity. Anonymous users have no identity until they link an identity to their user.

The user identity object contains the following attributes:

Latest product updates?

Something's not right?

---

## Integrating With Supabase Auth | Supabase Docs

**URL**: https://supabase.com/docs/guides/functions/auth

**Contents**:
- Integrating With Supabase Auth
- Integrate Supabase Auth with Edge Functions
- Setting up auth context#
- Fetching the user#
- Row Level Security#
- Example#
  - Is this helpful?

Integrating With Supabase Auth

Integrate Supabase Auth with Edge Functions

Edge Functions work seamlessly with Supabase Auth.

When a user makes a request to an Edge Function, you can use the Authorization header to set the Auth context in the Supabase client and enforce Row Level Security policies.

Importantly, this is done inside the Deno.serve() callback argument, so that the Authorization header is set for each individual request!

By getting the JWT from the Authorization header, you can provide the token to getUser() to fetch the user object to obtain metadata for the logged in user.

After initializing a Supabase client with the Auth context, all queries will be executed with the context of the user. For database queries, this means Row Level Security will be enforced.

See the full example on GitHub.

Latest product updates?

Something's not right?

**Examples**:

```python
1234567891011121314151617import { createClient } from 'npm:@supabase/supabase-js@2'Deno.serve(async (req: Request) => {  const supabaseClient = createClient(    Deno.env.get('SUPABASE_URL') ?? '',    Deno.env.get('SUPABASE_ANON_KEY') ?? '',    // Create client with Auth context of the user that called the function.    // This way your row-level-security (RLS) policies are applied.    {      global: {        headers: { Authorization: req.headers.get('Authorization')! },      },    }  );  //...})
```

```javascript
1234567Deno.serve(async (req: Request) => {  // ...  const authHeader = req.headers.get('Authorization')!  const token = authHeader.replace('Bearer ', '')  const { data } = await supabaseClient.auth.getUser(token)  // ...})
```

```python
12345678910111213import { createClient } from 'npm:@supabase/supabase-js@2'Deno.serve(async (req: Request) => {  // ...  // This query respects RLS - users only see rows they have access to  const { data, error } = await supabaseClient.from('profiles').select('*');  if (error) {    return new Response('Database error', { status: 500 })  }  // ...})
```

---

## JSON Web Token (JWT) | Supabase Docs

**URL**: https://supabase.com/docs/guides/auth/jwts

**Contents**:
- JSON Web Token (JWT)
- Information on how best to use JSON Web Tokens with Supabase
- Introduction#
- Supabase and JWTs#
- Using custom or third-party JWTs#
- Verifying a JWT from Supabase#
  - Verifying with the legacy JWT secret or a shared secret signing key#
- Resources#

Information on how best to use JSON Web Tokens with Supabase

A JSON Web Token is a type of data structure, represented as a string, that usually contains identity and authorization information about a user. It encodes information about its lifetime and is signed with a cryptographic key to make it tamper-resistant.

Supabase Auth continuously issues a new JWT for each user session, for as long as the user remains signed in. Check the comprehensive guide on Sessions to find out how you can tailor this process for your needs.

JWTs provide the foundation for Row Level Security. Each Supabase product is able to securely decode and verify the validity of a JWT it receives before using Postgres policies and roles to authorize access to the project's data.

Supabase provides a comprehensive system of managing JWT Signing Keys used to create and verify JSON Web Tokens.

JWTs are strings that have the following structure:

Each part is a string of Base64-URL encoded JSON, or bytes for the signature.

Gives some basic identifying information about the string, indicating its type typ, the cryptographic algorithm alg that can be used to verify the data, and optionally the unique key identifier that should be used when verifying it.

Provides identifying information (called "claims") about the user (or other entity) that is represented by the token. Usually a JWT conveys information about what the user can access (then called Access Token) or who the user is (then called ID Token). You can use a Custom Access Token Hook to add, remove or change claims present in the token. A few claims are important:

A digital signature using a shared secret or public-key cryptography. The purpose of the signature is to verify the authenticity of the <header>.<payload> string without relying on database access, liveness or performance of the Auth server. To verify the signature avoid implementing the algorithms yourself and instead rely on supabase.auth.getClaims(), or other high-quality JWT 

*[Content truncated - see full docs]*

**Examples**:

```text
1<header>.<payload>.<signature>
```

```text
12345{  "typ": "JWT",  "alg": "<HS256 | ES256 | RS256>",  "kid": "<unique key identifier>"}
```

```text
123456789{  "iss": "https://project_id.supabase.co/auth/v1",  "exp": 12345678,  "sub": "<user ID>",  "role": "authenticated",  "email": "someone@example.com",  "phone": "+15552368"  // ...}
```

---

## JWT Claims Reference | Supabase Docs

**URL**: https://supabase.com/docs/guides/auth/jwt-fields

**Contents**:
- JWT Claims Reference
- Complete reference for claims appearing in JWTs created by Supabase Auth
- JWT structure overview#
- Required claims#
- Optional claims#
- Special claims#
- Field value constraints#
  - Authenticator assurance level (aal)#

Complete reference for claims appearing in JWTs created by Supabase Auth

This page provides a comprehensive reference for all JWT claims used in Supabase authentication tokens. This information is essential for server-side JWT validation and serialization, especially when implementing authentication in languages like Rust where field names like ref are reserved keywords.

Supabase JWTs follow the standard JWT structure with three parts:

The payload contains various claims that provide user identity, authentication level, and authorization information.

These claims are always present in Supabase JWTs and cannot be removed:

These claims may be present depending on the authentication context:

In Rust, the ref field is a reserved keyword. When deserializing JWTs, you'll need to handle this:

When implementing JWT validation on your server:

Latest product updates?

Something's not right?

**Examples**:

```text
1234567891011121314151617181920212223242526{  "aal": "aal1",  "amr": [    {      "method": "password",      "timestamp": 1640991600    }  ],  "app_metadata": {    "provider": "email",    "providers": ["email"]  },  "aud": "authenticated",  "email": "user@example.com",  "exp": 1640995200,  "iat": 1640991600,  "iss": "https://abcdefghijklmnopqrst.supabase.co/auth/v1",  "phone": "",  "role": "authenticated",  "session_id": "123e4567-e89b-12d3-a456-426614174000",  "sub": "123e4567-e89b-12d3-a456-426
...
```

```text
1234567{  "iss": "supabase",  "ref": "abcdefghijklmnopqrst",  "role": "anon",  "iat": 1640991600,  "exp": 1640995200}
```

```text
1234567{  "iss": "supabase",  "ref": "abcdefghijklmnopqrst",  "role": "service_role",  "iat": 1640991600,  "exp": 1640995200}
```

---

## JavaScript: Create a user | Supabase Docs

**URL**: https://supabase.com/docs/reference/javascript/auth-admin-createuser

---

## JavaScript: Sign in a user | Supabase Docs

**URL**: https://supabase.com/docs/reference/javascript/auth-signinwithpassword

---

## JavaScript: Sign in a user through OAuth | Supabase Docs

**URL**: https://supabase.com/docs/reference/javascript/auth-signinwithoauth

---

## JavaScript: Sign in a user through OTP | Supabase Docs

**URL**: https://supabase.com/docs/reference/javascript/auth-signinwithotp

---

## JavaScript: Update a user | Supabase Docs

**URL**: https://supabase.com/docs/reference/javascript/auth-updateuser

---

## JavaScript: Update a user | Supabase Docs

**URL**: https://supabase.com/docs/reference/javascript/auth-admin-updateuserbyid

---

## Login with Apple | Supabase Docs

**URL**: https://supabase.com/docs/guides/auth/social-login/auth-apple

**Contents**:
- Login with Apple
- Overview#
- Using the OAuth flow for web#
        - app/auth/callback/route.ts
  - Configuration #
- Using sign in with Apple JS#
  - Configuration #
  - Is this helpful?

Supabase Auth supports using Sign in with Apple on the web and in native apps for iOS, macOS, watchOS or tvOS.

To support Sign in with Apple, you need to configure the Apple provider in the Supabase dashboard for your project.

There are three general ways to use Sign in with Apple, depending on the application you're trying to build:

In some cases you're able to use the OAuth flow within web-based native apps such as with React Native, Expo or other similar frameworks. It is best practice to use native Sign in with Apple capabilities on those platforms instead.

When developing with Expo, you can test Sign in with Apple via the Expo Go app, in all other cases you will need to obtain an Apple Developer account to enable the capability.

Sign in with Apple's OAuth flow is designed for web or browser based sign in methods. It can be used on web-based apps as well as websites, though some users can benefit by using Sign in with Apple JS directly.

Behind the scenes, Supabase Auth uses the REST APIs provided by Apple.

Make sure you're using the right supabase client in the following code.

If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the createClient from @supabase/supabase-js. If you're using Server-Side Rendering, see the Server-Side Auth guide for instructions on creating your Supabase client.

To initiate sign in, you can use the signInWithOAuth() method from the Supabase JavaScript library:

This call takes the user to Apple's consent screen. Once the flow ends, the user's profile information is exchanged and validated with Supabase Auth before it redirects back to your web application with an access and refresh token representing the user's session.

For a PKCE flow, for example in Server-Side Auth, you need an extra step to handle the code exchange. When calling signInWithOAuth, provide a redirectTo URL which points to a callback route. This redirect URL should be added to your redirect allow list.

In the browser, signI

*[Content truncated - see full docs]*

**Examples**:

```text
123supabase.auth.signInWithOAuth({  provider: 'apple',})
```

```text
123456await supabase.auth.signInWithOAuth({  provider,  options: {    redirectTo: `http://example.com/auth/callback`,  },})
```

```python
12345678910111213141516171819202122232425262728293031323334import { NextResponse } from 'next/server'// The client you created from the Server-Side Auth instructionsimport { createClient } from '@/utils/supabase/server'export async function GET(request: Request) {  const { searchParams, origin } = new URL(request.url)  const code = searchParams.get('code')  // if "next" is in param, use it as the redirect URL  let next = searchParams.get('next') ?? '/'  if (!next.startsWith('/')) {    // if "nex
...
```

---

## Login with Azure (Microsoft) | Supabase Docs

**URL**: https://supabase.com/docs/guides/auth/social-login/auth-azure

**Contents**:
- Login with Azure (Microsoft)
- Overview#
- Access your Azure Developer account#
- Register an application#
- Obtain a client ID and secret#
- Guarding against unverified email domains#
- Configure a tenant URL (optional)#
- Add login code to your client app#

Login with Azure (Microsoft)

To enable Azure (Microsoft) Auth for your project, you need to set up an Azure OAuth application and add the application credentials to your Supabase Dashboard.

Setting up OAuth with Azure consists of four broad steps:

You can also configure the Azure auth provider using the Management API:

Microsoft Entra ID can send out unverified email domains in certain cases. This may open up your project to a vulnerability where a malicious user can impersonate already existing accounts on your project.

This only applies in at least one of these cases:

This means that most OAuth apps are not susceptible to this vulnerability.

Despite this, we recommend configuring the optional xms_edov claim on the OAuth app. This claim allows Supabase Auth to identify with certainty whether the email address sent over by Microsoft Entra ID is verified or not.

Configure this in the following way:

A Microsoft Entra tenant is the directory of users who are allowed to access your project. This section depends on what your OAuth registration uses for Supported account types.

By default, Supabase Auth uses the common Microsoft tenant (https://login.microsoftonline.com/common) which generally allows any Microsoft account to sign in to your project. Microsoft Entra further limits what accounts can access your project depending on the type of OAuth application you registered.

If your app is registered as Personal Microsoft accounts only for the Supported account types set Microsoft tenant to consumers (https://login.microsoftonline.com/consumers).

If your app is registered as My organization only for the Supported account types you may want to configure Supabase Auth with the organization's tenant URL. This will use the tenant's authorization flows instead, and will limit access at the Supabase Auth level to Microsoft accounts arising from only the specified tenant.

Configure this by storing a value under Azure Tenant URL in the Supabase Auth provider configur

*[Content truncated - see full docs]*

**Examples**:

```text
1234567891011121314# Get your access token from https://supabase.com/dashboard/account/tokensexport SUPABASE_ACCESS_TOKEN="your-access-token"export PROJECT_REF="your-project-ref"# Configure Azure auth providercurl -X PATCH "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" \  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \  -H "Content-Type: application/json" \  -d '{    "external_azure_enabled": true,    "external_azure_client_id": "your-azure-client-id",    "external_azure_sec
...
```

```text
12345678910111213141516171819202122232425"optionalClaims": {      "idToken": [          {              "name": "xms_edov",              "source": null,              "essential": false,              "additionalProperties": []          },          {              "name": "email",              "source": null,              "essential": false,              "additionalProperties": []          }      ],      "accessToken": [          {              "name": "xms_edov",              "source": null,       
...
```

```javascript
12345678async function signInWithAzure() {  const { data, error } = await supabase.auth.signInWithOAuth({    provider: 'azure',    options: {      scopes: 'email',    },  })}
```

---

## Login with Bitbucket | Supabase Docs

**URL**: https://supabase.com/docs/guides/auth/social-login/auth-bitbucket

**Contents**:
- Login with Bitbucket
- Overview#
- Access your Bitbucket account#
- Find your callback URL#
- Create a Bitbucket OAuth app#
- Add your Bitbucket credentials into your Supabase project#
- Add login code to your client app#
        - app/auth/callback/route.ts

To enable Bitbucket Auth for your project, you need to set up a Bitbucket OAuth application and add the application credentials to your Supabase Dashboard.

Setting up Bitbucket logins for your application consists of 3 parts:

The next step requires a callback URL, which looks like this: https://<project-ref>.supabase.co/auth/v1/callback

For testing OAuth locally with the Supabase CLI see the local development docs.

Make sure you're using the right supabase client in the following code.

If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the createClient from @supabase/supabase-js. If you're using Server-Side Rendering, see the Server-Side Auth guide for instructions on creating your Supabase client.

When your user signs in, call signInWithOAuth() with bitbucket as the provider:

For a PKCE flow, for example in Server-Side Auth, you need an extra step to handle the code exchange. When calling signInWithOAuth, provide a redirectTo URL which points to a callback route. This redirect URL should be added to your redirect allow list.

In the browser, signInWithOAuth automatically redirects to the OAuth provider's authentication endpoint, which then redirects to your endpoint.

At the callback endpoint, handle the code exchange to save the user session.

Create a new file at app/auth/callback/route.ts and populate with the following:

When your user signs out, call signOut() to remove them from the browser session and any objects from localStorage:

Latest product updates?

Something's not right?

**Examples**:

```javascript
12345async function signInWithBitbucket() {  const { data, error } = await supabase.auth.signInWithOAuth({    provider: 'bitbucket',  })}
```

```text
123456await supabase.auth.signInWithOAuth({  provider,  options: {    redirectTo: `http://example.com/auth/callback`,  },})
```

```python
12345678910111213141516171819202122232425262728293031323334import { NextResponse } from 'next/server'// The client you created from the Server-Side Auth instructionsimport { createClient } from '@/utils/supabase/server'export async function GET(request: Request) {  const { searchParams, origin } = new URL(request.url)  const code = searchParams.get('code')  // if "next" is in param, use it as the redirect URL  let next = searchParams.get('next') ?? '/'  if (!next.startsWith('/')) {    // if "nex
...
```

---

## Login with Discord | Supabase Docs

**URL**: https://supabase.com/docs/guides/auth/social-login/auth-discord

**Contents**:
- Login with Discord
- Overview#
- Access your Discord account#
- Find your callback URL#
- Create a Discord application#
- Add your Discord credentials into your Supabase project#
- Add login code to your client app#
        - app/auth/callback/route.ts

To enable Discord Auth for your project, you need to set up a Discord Application and add the Application OAuth credentials to your Supabase Dashboard.

Setting up Discord logins for your application consists of 3 parts:

The next step requires a callback URL, which looks like this: https://<project-ref>.supabase.co/auth/v1/callback

For testing OAuth locally with the Supabase CLI see the local development docs.

You can also configure the Discord auth provider using the Management API:

Make sure you're using the right supabase client in the following code.

If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the createClient from @supabase/supabase-js. If you're using Server-Side Rendering, see the Server-Side Auth guide for instructions on creating your Supabase client.

When your user signs in, call signInWithOAuth() with discord as the provider:

For a PKCE flow, for example in Server-Side Auth, you need an extra step to handle the code exchange. When calling signInWithOAuth, provide a redirectTo URL which points to a callback route. This redirect URL should be added to your redirect allow list.

In the browser, signInWithOAuth automatically redirects to the OAuth provider's authentication endpoint, which then redirects to your endpoint.

At the callback endpoint, handle the code exchange to save the user session.

Create a new file at app/auth/callback/route.ts and populate with the following:

If your user is already signed in, Discord prompts the user again for authorization.

When your user signs out, call signOut() to remove them from the browser session and any objects from localStorage:

Latest product updates?

Something's not right?

**Examples**:

```text
12345678910111213# Get your access token from https://supabase.com/dashboard/account/tokensexport SUPABASE_ACCESS_TOKEN="your-access-token"export PROJECT_REF="your-project-ref"# Configure Discord auth providercurl -X PATCH "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" \  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \  -H "Content-Type: application/json" \  -d '{    "external_discord_enabled": true,    "external_discord_client_id": "your-discord-client-id",    "external_dis
...
```

```javascript
12345async function signInWithDiscord() {  const { data, error } = await supabase.auth.signInWithOAuth({    provider: 'discord',  })}
```

```text
123456await supabase.auth.signInWithOAuth({  provider,  options: {    redirectTo: `http://example.com/auth/callback`,  },})
```

---

## Login with Facebook | Supabase Docs

**URL**: https://supabase.com/docs/guides/auth/social-login/auth-facebook

**Contents**:
- Login with Facebook
- Overview#
- Access your Facebook Developer account#
- Create a Facebook app#
- Set up Facebook login for your Facebook app#
- Copy your Facebook app ID and secret#
- Enter your Facebook app ID and secret into your Supabase project#
- Add login code to your client app#

To enable Facebook Auth for your project, you need to set up a Facebook OAuth application and add the application credentials to your Supabase Dashboard.

Setting up Facebook logins for your application consists of 3 parts:

The next step requires a callback URL, which looks like this: https://<project-ref>.supabase.co/auth/v1/callback

For testing OAuth locally with the Supabase CLI see the local development docs.

From the Add Products to your App screen:

Be aware that you have to set the right use case permissions to enable Third party applications to read the email address. To do so:

Under Build Your App, click on Use Cases screen. From there, do the following steps:

You can also configure the Facebook auth provider using the Management API:

Make sure you're using the right supabase client in the following code.

If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the createClient from @supabase/supabase-js. If you're using Server-Side Rendering, see the Server-Side Auth guide for instructions on creating your Supabase client.

When your user signs in, call signInWithOAuth() with facebook as the provider:

For a PKCE flow, for example in Server-Side Auth, you need an extra step to handle the code exchange. When calling signInWithOAuth, provide a redirectTo URL which points to a callback route. This redirect URL should be added to your redirect allow list.

In the browser, signInWithOAuth automatically redirects to the OAuth provider's authentication endpoint, which then redirects to your endpoint.

At the callback endpoint, handle the code exchange to save the user session.

Create a new file at app/auth/callback/route.ts and populate with the following:

When your user signs out, call signOut() to remove them from the browser session and any objects from localStorage:

Now, you should be able to login with Facebook and alert you to Submit for Login Review when users try to sign into your app. Follow the instructions there to

*[Content truncated - see full docs]*

**Examples**:

```text
12345678910111213# Get your access token from https://supabase.com/dashboard/account/tokensexport SUPABASE_ACCESS_TOKEN="your-access-token"export PROJECT_REF="your-project-ref"# Configure Facebook auth providercurl -X PATCH "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" \  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \  -H "Content-Type: application/json" \  -d '{    "external_facebook_enabled": true,    "external_facebook_client_id": "your-facebook-app-id",    "external_fa
...
```

```javascript
12345async function signInWithFacebook() {  const { data, error } = await supabase.auth.signInWithOAuth({    provider: 'facebook',  })}
```

```text
123456await supabase.auth.signInWithOAuth({  provider,  options: {    redirectTo: `http://example.com/auth/callback`,  },})
```

---

## Login with Figma | Supabase Docs

**URL**: https://supabase.com/docs/guides/auth/social-login/auth-figma

**Contents**:
- Login with Figma
- Overview#
- Access the Figma Developers page#
- Find your callback URL#
- Create a Figma OAuth app#
- Enter your Figma credentials into your Supabase project#
- Add login code to your client app#
        - app/auth/callback/route.ts

To enable Figma Auth for your project, you need to set up a Figma OAuth application and add the application credentials to your Supabase Dashboard.

Setting up Figma logins for your application consists of 3 parts:

The next step requires a callback URL, which looks like this: https://<project-ref>.supabase.co/auth/v1/callback

For testing OAuth locally with the Supabase CLI see the local development docs.

Make sure you're using the right supabase client in the following code.

If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the createClient from @supabase/supabase-js. If you're using Server-Side Rendering, see the Server-Side Auth guide for instructions on creating your Supabase client.

When your user signs in, call signInWithOAuth() with figma as the provider:

For a PKCE flow, for example in Server-Side Auth, you need an extra step to handle the code exchange. When calling signInWithOAuth, provide a redirectTo URL which points to a callback route. This redirect URL should be added to your redirect allow list.

In the browser, signInWithOAuth automatically redirects to the OAuth provider's authentication endpoint, which then redirects to your endpoint.

At the callback endpoint, handle the code exchange to save the user session.

Create a new file at app/auth/callback/route.ts and populate with the following:

When your user signs out, call signOut() to remove them from the browser session and any objects from localStorage:

Latest product updates?

Something's not right?

**Examples**:

```javascript
12345async function signInWithFigma() {  const { data, error } = await supabase.auth.signInWithOAuth({    provider: 'figma',  })}
```

```text
123456await supabase.auth.signInWithOAuth({  provider,  options: {    redirectTo: `http://example.com/auth/callback`,  },})
```

```python
12345678910111213141516171819202122232425262728293031323334import { NextResponse } from 'next/server'// The client you created from the Server-Side Auth instructionsimport { createClient } from '@/utils/supabase/server'export async function GET(request: Request) {  const { searchParams, origin } = new URL(request.url)  const code = searchParams.get('code')  // if "next" is in param, use it as the redirect URL  let next = searchParams.get('next') ?? '/'  if (!next.startsWith('/')) {    // if "nex
...
```

---

## Login with GitHub | Supabase Docs

**URL**: https://supabase.com/docs/guides/auth/social-login/auth-github

**Contents**:
- Login with GitHub
- Overview#
- Find your callback URL#
- Register a new OAuth application on GitHub#
- Enter your GitHub credentials into your Supabase project#
- Add login code to your client app#
        - app/auth/callback/route.ts
- Resources#

To enable GitHub Auth for your project, you need to set up a GitHub OAuth application and add the application credentials to your Supabase Dashboard.

Setting up GitHub logins for your application consists of 3 parts:

The next step requires a callback URL, which looks like this: https://<project-ref>.supabase.co/auth/v1/callback

For testing OAuth locally with the Supabase CLI see the local development docs.

Copy your new OAuth credentials

You can also configure the GitHub auth provider using the Management API:

Make sure you're using the right supabase client in the following code.

If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the createClient from @supabase/supabase-js. If you're using Server-Side Rendering, see the Server-Side Auth guide for instructions on creating your Supabase client.

When your user signs in, call signInWithOAuth() with github as the provider:

For a PKCE flow, for example in Server-Side Auth, you need an extra step to handle the code exchange. When calling signInWithOAuth, provide a redirectTo URL which points to a callback route. This redirect URL should be added to your redirect allow list.

In the browser, signInWithOAuth automatically redirects to the OAuth provider's authentication endpoint, which then redirects to your endpoint.

At the callback endpoint, handle the code exchange to save the user session.

Create a new file at app/auth/callback/route.ts and populate with the following:

When your user signs out, call signOut() to remove them from the browser session and any objects from localStorage:

Latest product updates?

Something's not right?

**Examples**:

```text
12345678910111213# Get your access token from https://supabase.com/dashboard/account/tokensexport SUPABASE_ACCESS_TOKEN="your-access-token"export PROJECT_REF="your-project-ref"# Configure GitHub auth providercurl -X PATCH "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" \  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \  -H "Content-Type: application/json" \  -d '{    "external_github_enabled": true,    "external_github_client_id": "your-github-client-id",    "external_github_
...
```

```javascript
12345async function signInWithGithub() {  const { data, error } = await supabase.auth.signInWithOAuth({    provider: 'github',  })}
```

```text
123456await supabase.auth.signInWithOAuth({  provider,  options: {    redirectTo: `http://example.com/auth/callback`,  },})
```

---

## Login with GitLab | Supabase Docs

**URL**: https://supabase.com/docs/guides/auth/social-login/auth-gitlab

**Contents**:
- Login with GitLab
- Overview#
- Access your GitLab account#
- Find your callback URL#
- Create your GitLab application#
- Add your GitLab credentials into your Supabase project#
- Add login code to your client app#
        - app/auth/callback/route.ts

To enable GitLab Auth for your project, you need to set up a GitLab OAuth application and add the application credentials to your Supabase Dashboard.

Setting up GitLab logins for your application consists of 3 parts:

The next step requires a callback URL, which looks like this: https://<project-ref>.supabase.co/auth/v1/callback

For testing OAuth locally with the Supabase CLI see the local development docs.

Make sure you're using the right supabase client in the following code.

If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the createClient from @supabase/supabase-js. If you're using Server-Side Rendering, see the Server-Side Auth guide for instructions on creating your Supabase client.

When your user signs in, call signInWithOAuth() with gitlab as the provider:

For a PKCE flow, for example in Server-Side Auth, you need an extra step to handle the code exchange. When calling signInWithOAuth, provide a redirectTo URL which points to a callback route. This redirect URL should be added to your redirect allow list.

In the browser, signInWithOAuth automatically redirects to the OAuth provider's authentication endpoint, which then redirects to your endpoint.

At the callback endpoint, handle the code exchange to save the user session.

Create a new file at app/auth/callback/route.ts and populate with the following:

When your user signs out, call signOut() to remove them from the browser session and any objects from localStorage:

Latest product updates?

Something's not right?

**Examples**:

```javascript
12345async function signInWithGitLab() {  const { data, error } = await supabase.auth.signInWithOAuth({    provider: 'gitlab',  })}
```

```text
123456await supabase.auth.signInWithOAuth({  provider,  options: {    redirectTo: `http://example.com/auth/callback`,  },})
```

```python
12345678910111213141516171819202122232425262728293031323334import { NextResponse } from 'next/server'// The client you created from the Server-Side Auth instructionsimport { createClient } from '@/utils/supabase/server'export async function GET(request: Request) {  const { searchParams, origin } = new URL(request.url)  const code = searchParams.get('code')  // if "next" is in param, use it as the redirect URL  let next = searchParams.get('next') ?? '/'  if (!next.startsWith('/')) {    // if "nex
...
```

---

## Login with Google | Supabase Docs

**URL**: https://supabase.com/docs/guides/auth/social-login/auth-google

**Contents**:
- Login with Google
- Prerequisites#
  - Setup required scopes#
  - Setup consent screen branding#
- Project setup#
  - Local development#
  - Using the management API#
- Signing users in#

Supabase Auth supports Sign in with Google for the web, native applications (Android, macOS and iOS), and Chrome extensions.

You can use Sign in with Google in two ways:

You need to do some setup to get started with Sign in with Google:

Supabase Auth needs a few scopes granting access to profile data of your end users, which you have to configure in the Data Access (Scopes) screen:

If you add more scopes, especially those on the sensitive or restricted list your application might be subject to verification which may take a long time.

It's strongly recommended you set up a custom domain and optionally verify your brand information with Google, as this makes phishing attempts easier to spot by your users.

Google's consent screen is shown to users when they sign in. Optionally configure the following to improve the appearance of the screen, increasing the perception of trust by your users:

To support Sign In with Google, you need to configure the Google provider for your Supabase project.

Regardless of whether you use application code or Google's pre-built solutions to implement the sign in flow, you need to configure your project by obtaining a Client ID and Client Secret in the Clients section of the Google Auth Platform console:

To use the Google provider in local development:

If you have multiple client IDs, such as one for Web, iOS and Android, concatenate all of the client IDs with a comma but make sure the web's client ID is first in the list.

Use the PATCH /v1/projects/{ref}/config/auth Management API endpoint to configure the project's Auth settings programmatically. For configuring the Google provider send these options:

To use your own application code for the signin button, call the signInWithOAuth method (or the equivalent for your language).

Make sure you're using the right supabase client in the following code.

If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the createClient from @supabase/supabase-js. I

*[Content truncated - see full docs]*

**Examples**:

```text
1SUPABASE_AUTH_EXTERNAL_GOOGLE_CLIENT_SECRET="<client-secret>"
```

```text
12345[auth.external.google]enabled = trueclient_id = "<client-id>"secret = "env(SUPABASE_AUTH_EXTERNAL_GOOGLE_CLIENT_SECRET)"skip_nonce_check = false
```

```text
12345{  "external_google_enabled": true,  "external_google_client_id": "your-google-client-id",  "external_google_secret": "your-google-client-secret"}
```

---

## Login with Kakao | Supabase Docs

**URL**: https://supabase.com/docs/guides/auth/social-login/auth-kakao

**Contents**:
- Login with Kakao
- Overview#
- Access your Kakao Developer account#
- Create and configure your app#
- Obtain a REST API key#
- Find your callback URL#
- Generate and activate a client_secret#
- Additional configurations on Kakao Developers portal#

To enable Kakao Auth for your project, you need to set up an Kakao OAuth application and add the application credentials to your Supabase Dashboard.

Kakao OAuth consists of six broad steps:

This will serve as the client_id when you make API calls to authenticate the user.

The next step requires a callback URL, which looks like this: https://<project-ref>.supabase.co/auth/v1/callback

For testing OAuth locally with the Supabase CLI see the local development docs.

Make sure you're using the right supabase client in the following code.

If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the createClient from @supabase/supabase-js. If you're using Server-Side Rendering, see the Server-Side Auth guide for instructions on creating your Supabase client.

When your user signs in, call signInWithOAuth() with kakao as the provider:

For a PKCE flow, for example in Server-Side Auth, you need an extra step to handle the code exchange. When calling signInWithOAuth, provide a redirectTo URL which points to a callback route. This redirect URL should be added to your redirect allow list.

In the browser, signInWithOAuth automatically redirects to the OAuth provider's authentication endpoint, which then redirects to your endpoint.

At the callback endpoint, handle the code exchange to save the user session.

Create a new file at app/auth/callback/route.ts and populate with the following:

When your user signs out, call signOut() to remove them from the browser session and any objects from localStorage:

Kakao Login JS SDK is an official Kakao SDK for authenticating Kakao users on websites.

Exchange the authorization code returned by Kakao API for an ID Token.

For example, this code shows a how to get ID Token:

Use the ID Token to sign in:

Latest product updates?

Something's not right?

**Examples**:

```javascript
12345async function signInWithKakao() {  const { data, error } = await supabase.auth.signInWithOAuth({    provider: 'kakao',  })}
```

```text
123456await supabase.auth.signInWithOAuth({  provider,  options: {    redirectTo: `http://example.com/auth/callback`,  },})
```

```python
12345678910111213141516171819202122232425262728293031323334import { NextResponse } from 'next/server'// The client you created from the Server-Side Auth instructionsimport { createClient } from '@/utils/supabase/server'export async function GET(request: Request) {  const { searchParams, origin } = new URL(request.url)  const code = searchParams.get('code')  // if "next" is in param, use it as the redirect URL  let next = searchParams.get('next') ?? '/'  if (!next.startsWith('/')) {    // if "nex
...
```

---

## Login with Keycloak | Supabase Docs

**URL**: https://supabase.com/docs/guides/auth/social-login/auth-keycloak

**Contents**:
- Login with Keycloak
- Overview#
- Access your Keycloak admin console#
- Create a Keycloak realm#
- Create a Keycloak client#
- Client settings#
- Obtain the client secret#
- Add login code to your client app#

To enable Keycloak Auth for your project, you need to set up an Keycloak OAuth application and add the application credentials to your Supabase Dashboard.

To get started with Keycloak, you can run it in a docker container with: docker run -p 8080:8080 -e KEYCLOAK_ADMIN=admin -e KEYCLOAK_ADMIN_PASSWORD=admin quay.io/keycloak/keycloak:latest start-dev

This guide will be assuming that you are running Keycloak in a docker container as described in the command above.

Keycloak OAuth consists of five broad steps:

The "Client ID" of the created client will serve as the client_id when you make API calls to authenticate the user.

After you've created the client successfully, ensure that you set the following settings:

This will serve as the client_secret when you make API calls to authenticate the user. Under the "Credentials" tab, the Secret value will be used as the client secret.

Since Keycloak version 22, the openid scope must be passed. Add this to the supabase.auth.signInWithOAuth() method.

Make sure you're using the right supabase client in the following code.

If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the createClient from @supabase/supabase-js. If you're using Server-Side Rendering, see the Server-Side Auth guide for instructions on creating your Supabase client.

When your user signs in, call signInWithOAuth() with keycloak as the provider:

For a PKCE flow, for example in Server-Side Auth, you need an extra step to handle the code exchange. When calling signInWithOAuth, provide a redirectTo URL which points to a callback route. This redirect URL should be added to your redirect allow list.

In the browser, signInWithOAuth automatically redirects to the OAuth provider's authentication endpoint, which then redirects to your endpoint.

At the callback endpoint, handle the code exchange to save the user session.

Create a new file at app/auth/callback/route.ts and populate with the following:

When your user signs out,

*[Content truncated - see full docs]*

**Examples**:

```javascript
12345678async function signInWithKeycloak() {  const { data, error } = await supabase.auth.signInWithOAuth({    provider: 'keycloak',    options: {      scopes: 'openid',    },  })}
```

```text
123456await supabase.auth.signInWithOAuth({  provider,  options: {    redirectTo: `http://example.com/auth/callback`,  },})
```

```python
12345678910111213141516171819202122232425262728293031323334import { NextResponse } from 'next/server'// The client you created from the Server-Side Auth instructionsimport { createClient } from '@/utils/supabase/server'export async function GET(request: Request) {  const { searchParams, origin } = new URL(request.url)  const code = searchParams.get('code')  // if "next" is in param, use it as the redirect URL  let next = searchParams.get('next') ?? '/'  if (!next.startsWith('/')) {    // if "nex
...
```

---

## Login with LinkedIn | Supabase Docs

**URL**: https://supabase.com/docs/guides/auth/social-login/auth-linkedin

**Contents**:
- Login with LinkedIn
- Overview#
- Access your LinkedIn Developer account#
- Find your callback URL#
- Create a LinkedIn OAuth app#
- Enter your LinkedIn (OIDC) credentials into your Supabase project#
- Add login code to your client app#
        - app/auth/callback/route.ts

To enable LinkedIn Auth for your project, you need to set up a LinkedIn OAuth application and add the application credentials to your Supabase Dashboard.

Setting up LinkedIn logins for your application consists of 3 parts:

The next step requires a callback URL, which looks like this: https://<project-ref>.supabase.co/auth/v1/callback

For testing OAuth locally with the Supabase CLI see the local development docs.

Ensure that the appropriate scopes have been added under OAuth 2.0 Scopes at the bottom of the Auth screen.

You can also configure the LinkedIn (OIDC) auth provider using the Management API:

Make sure you're using the right supabase client in the following code.

If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the createClient from @supabase/supabase-js. If you're using Server-Side Rendering, see the Server-Side Auth guide for instructions on creating your Supabase client.

When your user signs in, call signInWithOAuth() with linkedin_oidc as the provider:

For a PKCE flow, for example in Server-Side Auth, you need an extra step to handle the code exchange. When calling signInWithOAuth, provide a redirectTo URL which points to a callback route. This redirect URL should be added to your redirect allow list.

In the browser, signInWithOAuth automatically redirects to the OAuth provider's authentication endpoint, which then redirects to your endpoint.

At the callback endpoint, handle the code exchange to save the user session.

Create a new file at app/auth/callback/route.ts and populate with the following:

When your user signs out, call signOut() to remove them from the browser session and any objects from localStorage:

We will be replacing the LinkedIn provider with a new LinkedIn (OIDC) provider to support recent changes to the LinkedIn OAuth APIs. The new provider utilizes the Open ID Connect standard. In view of this change, we have disabled edits on the LinkedIn provider and will be removing it effective 4th J

*[Content truncated - see full docs]*

**Examples**:

```text
12345678910111213# Get your access token from https://supabase.com/dashboard/account/tokensexport SUPABASE_ACCESS_TOKEN="your-access-token"export PROJECT_REF="your-project-ref"# Configure LinkedIn (OIDC) auth providercurl -X PATCH "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" \  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \  -H "Content-Type: application/json" \  -d '{    "external_linkedin_oidc_enabled": true,    "external_linkedin_oidc_client_id": "your-linkedin-client-
...
```

```javascript
12345async function signInWithLinkedIn() {  const { data, error } = await supabase.auth.signInWithOAuth({    provider: 'linkedin_oidc',  })}
```

```text
123456await supabase.auth.signInWithOAuth({  provider,  options: {    redirectTo: `http://example.com/auth/callback`,  },})
```

---

## Login with Notion | Supabase Docs

**URL**: https://supabase.com/docs/guides/auth/social-login/auth-notion

**Contents**:
- Login with Notion
- Overview#
- Create your notion integration#
- Add the redirect URI#
- Add your Notion credentials into your Supabase project#
- Add login code to your client app#
        - app/auth/callback/route.ts
- Resources#

To enable Notion Auth for your project, you need to set up a Notion Application and add the Application OAuth credentials to your Supabase Dashboard.

Setting up Notion logins for your application consists of 3 parts:

Go to developers.notion.com.

Click "View my integrations" and login.

Once logged in, go to notion.so/my-integrations and create a new integration.

When creating your integration, ensure that you select "Public integration" under "Integration type" and "Read user information including email addresses" under "Capabilities".

You will need to add a redirect URI, see Add the redirect URI

Once you've filled in the necessary fields, click "Submit" to finish creating the integration.

The next step requires a callback URL, which looks like this: https://<project-ref>.supabase.co/auth/v1/callback

For testing OAuth locally with the Supabase CLI see the local development docs.

Make sure you're using the right supabase client in the following code.

If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the createClient from @supabase/supabase-js. If you're using Server-Side Rendering, see the Server-Side Auth guide for instructions on creating your Supabase client.

When your user signs in, call signInWithOAuth() with notion as the provider:

For a PKCE flow, for example in Server-Side Auth, you need an extra step to handle the code exchange. When calling signInWithOAuth, provide a redirectTo URL which points to a callback route. This redirect URL should be added to your redirect allow list.

In the browser, signInWithOAuth automatically redirects to the OAuth provider's authentication endpoint, which then redirects to your endpoint.

At the callback endpoint, handle the code exchange to save the user session.

Create a new file at app/auth/callback/route.ts and populate with the following:

When your user signs out, call signOut() to remove them from the browser session and any objects from localStorage:

Latest product upda

*[Content truncated - see full docs]*

**Examples**:

```javascript
12345async function signInWithNotion() {  const { data, error } = await supabase.auth.signInWithOAuth({    provider: 'notion',  })}
```

```text
123456await supabase.auth.signInWithOAuth({  provider,  options: {    redirectTo: `http://example.com/auth/callback`,  },})
```

```python
12345678910111213141516171819202122232425262728293031323334import { NextResponse } from 'next/server'// The client you created from the Server-Side Auth instructionsimport { createClient } from '@/utils/supabase/server'export async function GET(request: Request) {  const { searchParams, origin } = new URL(request.url)  const code = searchParams.get('code')  // if "next" is in param, use it as the redirect URL  let next = searchParams.get('next') ?? '/'  if (!next.startsWith('/')) {    // if "nex
...
```

---

## Login with Slack | Supabase Docs

**URL**: https://supabase.com/docs/guides/auth/social-login/auth-slack

**Contents**:
- Login with Slack
- Overview#
- Access your Slack Developer account#
- Find your callback URL#
- Create a Slack OAuth app#
- Enter your Slack credentials into your Supabase project#
- Add login code to your client app#
        - app/auth/callback/route.ts

To enable Slack Auth for your project, you need to set up a Slack OAuth application and add the application credentials to your Supabase Dashboard.

We will be replacing the existing Slack provider with a new Slack (OIDC) provider. Developers with Slack OAuth Applications created prior to 24th June 2024 should create a new application and migrate their credentials from the Slack provider to the Slack (OIDC) provider. Existing OAuth Applications built with the old Slack provider will continue to work up till 10th October. You can refer to the list of supported scopes for the new Slack (OIDC) User.

Setting up Slack logins for your application consists of 3 parts:

The next step requires a callback URL, which looks like this: https://<project-ref>.supabase.co/auth/v1/callback

For testing OAuth locally with the Supabase CLI see the local development docs.

Under Create an app...:

Under App Credentials:

Under the sidebar, select OAuth & Permissions and look for Redirect URLs:

You can also configure the Slack (OIDC) auth provider using the Management API:

Make sure you're using the right supabase client in the following code.

If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the createClient from @supabase/supabase-js. If you're using Server-Side Rendering, see the Server-Side Auth guide for instructions on creating your Supabase client.

When your user signs in, call signInWithOAuth() with slack_oidc as the provider:

For a PKCE flow, for example in Server-Side Auth, you need an extra step to handle the code exchange. When calling signInWithOAuth, provide a redirectTo URL which points to a callback route. This redirect URL should be added to your redirect allow list.

In the browser, signInWithOAuth automatically redirects to the OAuth provider's authentication endpoint, which then redirects to your endpoint.

At the callback endpoint, handle the code exchange to save the user session.

Create a new file at app/auth/callback/rout

*[Content truncated - see full docs]*

**Examples**:

```text
12345678910111213# Get your access token from https://supabase.com/dashboard/account/tokensexport SUPABASE_ACCESS_TOKEN="your-access-token"export PROJECT_REF="your-project-ref"# Configure Slack (OIDC) auth providercurl -X PATCH "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" \  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \  -H "Content-Type: application/json" \  -d '{    "external_slack_oidc_enabled": true,    "external_slack_oidc_client_id": "your-slack-client-id",    "ext
...
```

```javascript
12345async function signInWithSlack() {  const { data, error } = await supabase.auth.signInWithOAuth({    provider: 'slack_oidc',  })}
```

```text
123456await supabase.auth.signInWithOAuth({  provider,  options: {    redirectTo: `http://example.com/auth/callback`,  },})
```

---

## Login with Spotify | Supabase Docs

**URL**: https://supabase.com/docs/guides/auth/social-login/auth-spotify

**Contents**:
- Login with Spotify
- Overview#
- Access your Spotify Developer account#
- Find your callback URL#
- Create a Spotify OAuth app#
- Enter your Spotify credentials into your Supabase project#
- Add login code to your client app#
        - app/auth/callback/route.ts

To enable Spotify Auth for your project, you need to set up a Spotify OAuth application and add the application credentials to your Supabase Dashboard.

Setting up Spotify logins for your application consists of 3 parts:

The next step requires a callback URL, which looks like this: https://<project-ref>.supabase.co/auth/v1/callback

For testing OAuth locally with the Supabase CLI see the local development docs.

You can also configure the Spotify auth provider using the Management API:

The following outlines the steps to sign in using Spotify with Supabase Auth.

Make sure you're using the right supabase client in the following code.

If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the createClient from @supabase/supabase-js. If you're using Server-Side Rendering, see the Server-Side Auth guide for instructions on creating your Supabase client.

When your user signs in, call signInWithOAuth() with spotify as the provider:

For a PKCE flow, for example in Server-Side Auth, you need an extra step to handle the code exchange. When calling signInWithOAuth, provide a redirectTo URL which points to a callback route. This redirect URL should be added to your redirect allow list.

In the browser, signInWithOAuth automatically redirects to the OAuth provider's authentication endpoint, which then redirects to your endpoint.

At the callback endpoint, handle the code exchange to save the user session.

Create a new file at app/auth/callback/route.ts and populate with the following:

When your user signs out, call signOut() to remove them from the browser session and any objects from localStorage:

Latest product updates?

Something's not right?

**Examples**:

```text
12345678910111213# Get your access token from https://supabase.com/dashboard/account/tokensexport SUPABASE_ACCESS_TOKEN="your-access-token"export PROJECT_REF="your-project-ref"# Configure Spotify auth providercurl -X PATCH "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" \  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \  -H "Content-Type: application/json" \  -d '{    "external_spotify_enabled": true,    "external_spotify_client_id": "your-spotify-client-id",    "external_spo
...
```

```javascript
12345async function signInWithSpotify() {  const { data, error } = await supabase.auth.signInWithOAuth({    provider: 'spotify',  })}
```

```text
123456await supabase.auth.signInWithOAuth({  provider,  options: {    redirectTo: `http://example.com/auth/callback`,  },})
```

---

## Login with Twitch | Supabase Docs

**URL**: https://supabase.com/docs/guides/auth/social-login/auth-twitch

**Contents**:
- Login with Twitch
- Overview#
- Access your Twitch Developer account#
- Find your callback URL#
- Create a Twitch application#
- Retrieve your Twitch OAuth client ID and client secret#
- Add your Twitch credentials into your Supabase project#
- Add login code to your client app#

To enable Twitch Auth for your project, you need to set up a Twitch Application and add the Application OAuth credentials to your Supabase Dashboard.

Setting up Twitch logins for your application consists of 3 parts:

The next step requires a callback URL, which looks like this: https://<project-ref>.supabase.co/auth/v1/callback

For testing OAuth locally with the Supabase CLI see the local development docs.

Make sure you're using the right supabase client in the following code.

If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the createClient from @supabase/supabase-js. If you're using Server-Side Rendering, see the Server-Side Auth guide for instructions on creating your Supabase client.

When your user signs in, call signInWithOAuth() with twitch as the provider:

For a PKCE flow, for example in Server-Side Auth, you need an extra step to handle the code exchange. When calling signInWithOAuth, provide a redirectTo URL which points to a callback route. This redirect URL should be added to your redirect allow list.

In the browser, signInWithOAuth automatically redirects to the OAuth provider's authentication endpoint, which then redirects to your endpoint.

At the callback endpoint, handle the code exchange to save the user session.

Create a new file at app/auth/callback/route.ts and populate with the following:

When your user signs out, call signOut() to remove them from the browser session and any objects from localStorage:

Latest product updates?

Something's not right?

**Examples**:

```javascript
12345async function signInWithTwitch() {  const { data, error } = await supabase.auth.signInWithOAuth({    provider: 'twitch',  })}
```

```text
123456await supabase.auth.signInWithOAuth({  provider,  options: {    redirectTo: `http://example.com/auth/callback`,  },})
```

```python
12345678910111213141516171819202122232425262728293031323334import { NextResponse } from 'next/server'// The client you created from the Server-Side Auth instructionsimport { createClient } from '@/utils/supabase/server'export async function GET(request: Request) {  const { searchParams, origin } = new URL(request.url)  const code = searchParams.get('code')  // if "next" is in param, use it as the redirect URL  let next = searchParams.get('next') ?? '/'  if (!next.startsWith('/')) {    // if "nex
...
```

---

## Login with Twitter | Supabase Docs

**URL**: https://supabase.com/docs/guides/auth/social-login/auth-twitter

**Contents**:
- Login with Twitter
- Overview#
- Access your Twitter Developer account#
- Find your callback URL#
- Create a Twitter OAuth app#
- Enter your Twitter credentials into your Supabase project#
- Add login code to your client app#
        - app/auth/callback/route.ts

To enable Twitter Auth for your project, you need to set up a Twitter OAuth application and add the application credentials in the Supabase Dashboard.

Setting up Twitter logins for your application consists of 3 parts:

The next step requires a callback URL, which looks like this: https://<project-ref>.supabase.co/auth/v1/callback

For testing OAuth locally with the Supabase CLI see the local development docs.

You can also configure the Twitter auth provider using the Management API:

Make sure you're using the right supabase client in the following code.

If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the createClient from @supabase/supabase-js. If you're using Server-Side Rendering, see the Server-Side Auth guide for instructions on creating your Supabase client.

When your user signs in, call signInWithOAuth() with twitter as the provider:

For a PKCE flow, for example in Server-Side Auth, you need an extra step to handle the code exchange. When calling signInWithOAuth, provide a redirectTo URL which points to a callback route. This redirect URL should be added to your redirect allow list.

In the browser, signInWithOAuth automatically redirects to the OAuth provider's authentication endpoint, which then redirects to your endpoint.

At the callback endpoint, handle the code exchange to save the user session.

Create a new file at app/auth/callback/route.ts and populate with the following:

When your user signs out, call signOut() to remove them from the browser session and any objects from localStorage:

Latest product updates?

Something's not right?

**Examples**:

```text
12345678910111213# Get your access token from https://supabase.com/dashboard/account/tokensexport SUPABASE_ACCESS_TOKEN="your-access-token"export PROJECT_REF="your-project-ref"# Configure Twitter auth providercurl -X PATCH "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" \  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \  -H "Content-Type: application/json" \  -d '{    "external_twitter_enabled": true,    "external_twitter_client_id": "your-twitter-api-key",    "external_twitt
...
```

```javascript
12345async function signInWithTwitter() {  const { data, error } = await supabase.auth.signInWithOAuth({    provider: 'twitter',  })}
```

```text
123456await supabase.auth.signInWithOAuth({  provider,  options: {    redirectTo: `http://example.com/auth/callback`,  },})
```

---

## Login with Zoom | Supabase Docs

**URL**: https://supabase.com/docs/guides/auth/social-login/auth-zoom

**Contents**:
- Login with Zoom
- Overview#
- Access your Zoom Developer account#
- Find your callback URL#
- Create a Zoom OAuth app#
- Enter your Zoom credentials into your Supabase project#
- Add login code to your client app#
        - app/auth/callback/route.ts

To enable Zoom Auth for your project, you need to set up a Zoom OAuth application and add the application credentials to your Supabase Dashboard.

Setting up Zoom logins for your application consists of 3 parts:

The next step requires a callback URL, which looks like this: https://<project-ref>.supabase.co/auth/v1/callback

For testing OAuth locally with the Supabase CLI see the local development docs.

Under App credentials

Under Redirect URL for OAuth

You can also configure the Zoom auth provider using the Management API:

Make sure you're using the right supabase client in the following code.

If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the createClient from @supabase/supabase-js. If you're using Server-Side Rendering, see the Server-Side Auth guide for instructions on creating your Supabase client.

When your user signs in, call signInWithOAuth() with zoom as the provider:

For a PKCE flow, for example in Server-Side Auth, you need an extra step to handle the code exchange. When calling signInWithOAuth, provide a redirectTo URL which points to a callback route. This redirect URL should be added to your redirect allow list.

In the browser, signInWithOAuth automatically redirects to the OAuth provider's authentication endpoint, which then redirects to your endpoint.

At the callback endpoint, handle the code exchange to save the user session.

Create a new file at app/auth/callback/route.ts and populate with the following:

When your user signs out, call signOut() to remove them from the browser session and any objects from localStorage:

Latest product updates?

Something's not right?

**Examples**:

```text
12345678910111213# Get your access token from https://supabase.com/dashboard/account/tokensexport SUPABASE_ACCESS_TOKEN="your-access-token"export PROJECT_REF="your-project-ref"# Configure Zoom auth providercurl -X PATCH "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" \  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \  -H "Content-Type: application/json" \  -d '{    "external_zoom_enabled": true,    "external_zoom_client_id": "your-zoom-client-id",    "external_zoom_secret": "
...
```

```javascript
12345async function signInWithZoom() {  const { data, error } = await supabase.auth.signInWithOAuth({    provider: 'zoom',  })}
```

```text
123456await supabase.auth.signInWithOAuth({  provider,  options: {    redirectTo: `http://example.com/auth/callback`,  },})
```

---

## Manage Advanced MFA Phone usage | Supabase Docs

**URL**: https://supabase.com/docs/guides/platform/manage-your-usage/advanced-mfa-phone

**Contents**:
- Manage Advanced MFA Phone usage
- What you are charged for#
- How charges are calculated#
  - Example#
  - Usage on your invoice#
- Pricing#
- Pricing#
- Billing examples#

Manage Advanced MFA Phone usage

You are charged for having the feature Advanced Multi-Factor Authentication Phone enabled for your project.

Additional charges apply for each SMS or WhatsApp message sent, depending on your third-party messaging provider (such as Twilio or MessageBird).

MFA Phone is charged by the hour, meaning you are charged for the exact number of hours that the feature is enabled for a project. If the feature is enabled for part of an hour, you are still charged for the full hour.

Your billing cycle runs from January 1 to January 31. On January 10 at 4:30 PM, you enable the MFA Phone feature for your project. At the end of the billing cycle you are billed for 512 hours.

Usage is shown as "Auth MFA Phone Hours" on your invoice.

$0.1027 per hour ($75 per month) for the first project. $0.0137 per hour ($10 per month) for every additional project.

For a detailed breakdown of how charges are calculated, refer to Manage Advanced MFA Phone usage.

The project has MFA Phone activated throughout the entire billing cycle.

All projects have MFA Phone activated throughout the entire billing cycle.

Latest product updates?

Something's not right?

---

## Manage Monthly Active Third-Party Users usage | Supabase Docs

**URL**: https://supabase.com/docs/guides/platform/manage-your-usage/monthly-active-users-third-party

**Contents**:
- Manage Monthly Active Third-Party Users usage
- What you are charged for#
  - Example#
  - User-1 signs in via Auth0 on January 3
  - User-1 signs out on January 4.
  - User-1 signs in via Auth0 again on January 17
- How charges are calculated#
  - Usage on your invoice#

Manage Monthly Active Third-Party Users usage

You are charged for the number of distinct users who log in or refresh their token during the billing cycle using a third-party authentication provider (Clerk, Firebase Auth, Auth0, AWS Cognito). Each unique user is counted only once per billing cycle, regardless of how many times they authenticate. These users are referred to as "Third-Party MAUs".

Your billing cycle runs from January 1 to January 31. Although User-1 was signed in multiple times, they are counted as a single SSO MAU for this billing cycle.

The Third-Party MAU count increases from 0 to 1.

The Third-Party MAU count remains 1.

You are charged by Third-Party MAU.

Usage is shown as "Monthly Active Third-Party Users" on your invoice.

$0.00325 per Third-Party MAU. You are only charged for usage exceeding your subscription plan's quota.

For a detailed breakdown of how charges are calculated, refer to Manage Monthly Active Third-Party Users usage.

The count resets at the start of each billing cycle.

The organization's Third-Party MAU usage for the billing cycle is within the quota, so no charges apply.

The organization's Third-Party MAU usage for the billing cycle exceeds the quota by 4950, incurring charges for this additional usage.

You can view Monthly Active Third-Party Users usage on the organization's usage page. The page shows the usage of all projects by default. To view the usage for a specific project, select it from the dropdown. You can also select a different time period.

Latest product updates?

Something's not right?

---

## Migrate from Auth0 to Supabase Auth | Supabase Docs

**URL**: https://supabase.com/docs/guides/resources/migrating-to-supabase/auth0

**Contents**:
- Migrate from Auth0 to Supabase Auth
- Learn how to migrate your users from Auth0
- Before you begin#
- Migration strategies#
- Migration steps#
  - Step 1: Export your user data#
  - Step 2: Import your users into Supabase Auth#
    - Password-based methods#

Migrate from Auth0 to Supabase Auth

Learn how to migrate your users from Auth0

You can migrate your users from Auth0 to Supabase Auth.

Changing authentication providers for a production app is an important operation. It can affect most aspects of your application. Prepare in advance by reading this guide, and develop a plan for handling the key migration steps and possible problems.

With advance planning, a smooth and safe Auth migration is possible.

Before beginning, consider the answers to the following questions. They will help you need decide if you need to migrate, and which strategy to use:

Depending on your evaluation, you may choose to go with one of the following strategies:

Auth provider migrations require 2 main steps:

Auth0 provides two methods for exporting user data:

To export password hashes and MFA factors, contact Auth0 support.

The steps for importing your users depends on the login methods that you support.

See the following sections for how to import users with:

For users who sign in with passwords, we recommend a hybrid approach to reduce downtime:

Sign up new users using Supabase Auth's signin methods.

Migrate existing users to Supabase Auth. This requires two main steps: first, check which users need to be migrated, then create their accounts using the Supabase admin endpoints.

Get your Auth 0 user export and password hash export lists.

Filter for users who use password login.

Use Supabase Auth's admin create user method to recreate the user in Supabase Auth. If the user has a confirmed email address or phone number, set email_confirm or phone_confirm to true.

Supabase supports bcrypt and Argon2 password hashes.

If you have a plaintext password instead of a hash, you can provide that instead. Supabase Auth will handle hashing the password for you. (Passwords are always stored hashed.)

To sign in your migrated users, use the Supabase Auth sign in methods.

To check for edge cases where users aren't successfully migrated, use

*[Content truncated - see full docs]*

**Examples**:

```javascript
12345const { data, error } = await supabase.auth.admin.createUser({  email: 'valid.email@supabase.io',  password_hash: '$2y$10$a9pghn27d7m0ltXvlX8LiOowy7XfFw0hW0G80OjKYQ1jaoejaA7NC',  email_confirm: true,})
```

```javascript
1234const { data, error } = await supabase.auth.admin.createUser({  email: 'valid.email@supabase.io',  password: 'supersecurepassword123!',})
```

```javascript
1234const { data, error } = await supabase.auth.admin.createUser({  email: 'valid.email@supabase.io',  email_confirm: true,})
```

---

## Migrate from Auth0 to Supabase Auth | Supabase Docs

**URL**: https://supabase.com/docs/guides/platform/migrating-to-supabase/auth0

**Contents**:
- Migrate from Auth0 to Supabase Auth
- Learn how to migrate your users from Auth0
- Before you begin#
- Migration strategies#
- Migration steps#
  - Step 1: Export your user data#
  - Step 2: Import your users into Supabase Auth#
    - Password-based methods#

Migrate from Auth0 to Supabase Auth

Learn how to migrate your users from Auth0

You can migrate your users from Auth0 to Supabase Auth.

Changing authentication providers for a production app is an important operation. It can affect most aspects of your application. Prepare in advance by reading this guide, and develop a plan for handling the key migration steps and possible problems.

With advance planning, a smooth and safe Auth migration is possible.

Before beginning, consider the answers to the following questions. They will help you need decide if you need to migrate, and which strategy to use:

Depending on your evaluation, you may choose to go with one of the following strategies:

Auth provider migrations require 2 main steps:

Auth0 provides two methods for exporting user data:

To export password hashes and MFA factors, contact Auth0 support.

The steps for importing your users depends on the login methods that you support.

See the following sections for how to import users with:

For users who sign in with passwords, we recommend a hybrid approach to reduce downtime:

Sign up new users using Supabase Auth's signin methods.

Migrate existing users to Supabase Auth. This requires two main steps: first, check which users need to be migrated, then create their accounts using the Supabase admin endpoints.

Get your Auth 0 user export and password hash export lists.

Filter for users who use password login.

Use Supabase Auth's admin create user method to recreate the user in Supabase Auth. If the user has a confirmed email address or phone number, set email_confirm or phone_confirm to true.

Supabase supports bcrypt and Argon2 password hashes.

If you have a plaintext password instead of a hash, you can provide that instead. Supabase Auth will handle hashing the password for you. (Passwords are always stored hashed.)

To sign in your migrated users, use the Supabase Auth sign in methods.

To check for edge cases where users aren't successfully migrated, use

*[Content truncated - see full docs]*

**Examples**:

```javascript
12345const { data, error } = await supabase.auth.admin.createUser({  email: 'valid.email@supabase.io',  password_hash: '$2y$10$a9pghn27d7m0ltXvlX8LiOowy7XfFw0hW0G80OjKYQ1jaoejaA7NC',  email_confirm: true,})
```

```javascript
1234const { data, error } = await supabase.auth.admin.createUser({  email: 'valid.email@supabase.io',  password: 'supersecurepassword123!',})
```

```javascript
1234const { data, error } = await supabase.auth.admin.createUser({  email: 'valid.email@supabase.io',  email_confirm: true,})
```

---

## Migrate from Firebase Auth to Supabase | Supabase Docs

**URL**: https://supabase.com/docs/guides/migrations/firebase-auth

**Contents**:
- Migrate from Firebase Auth to Supabase
- Migrate Firebase auth users to Supabase Auth.
- Set up the migration tool #
- Generate a Firebase private key #
- Save your Firebase password hash parameters #
- Command line options#
  - Dump Firestore users to a JSON file #
  - Import JSON users file to Supabase Auth (Postgres: auth.users#

Migrate from Firebase Auth to Supabase

Migrate Firebase auth users to Supabase Auth.

Supabase provides several tools to help migrate auth users from a Firebase project to a Supabase project. There are two parts to the migration process:

Clone the firebase-to-supabase repository:

In the /auth directory, create a file named supabase-service.json with the following contents:

On your project dashboard, click Connect

Under the Session pooler, click on the View parameters under the connect string. Replace the Host and User fields with the values shown.

Enter the password you used when you created your Supabase project in the password entry in the supabase-service.json file.

node firestoreusers2json.js [<filename.json>] [<batch_size>]

node import_users.js <path_to_json_file> [<batch_size>]

For more advanced migrations, including the use of a middleware server component for verifying a user's existing Firebase password and updating that password in your Supabase project the first time a user logs in, see the firebase-to-supabase repo.

Contact us if you need more help migrating your project.

Latest product updates?

Something's not right?

**Examples**:

```text
1git clone https://github.com/supabase-community/firebase-to-supabase.git
```

```text
1234567{  "host": "database.server.com",  "password": "secretpassword",  "user": "postgres",  "database": "postgres",  "port": 5432}
```

```text
1234567hash_config {  algorithm: SCRYPT,  base64_signer_key: XXXX/XXX+XXXXXXXXXXXXXXXXX+XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX==,  base64_salt_separator: Aa==,  rounds: 8,  mem_cost: 14,}
```

---

## Migrate from Firebase Auth to Supabase | Supabase Docs

**URL**: https://supabase.com/docs/guides/resources/migrating-to-supabase/firebase-auth

**Contents**:
- Migrate from Firebase Auth to Supabase
- Migrate Firebase auth users to Supabase Auth.
- Set up the migration tool #
- Generate a Firebase private key #
- Save your Firebase password hash parameters #
- Command line options#
  - Dump Firestore users to a JSON file #
  - Import JSON users file to Supabase Auth (Postgres: auth.users#

Migrate from Firebase Auth to Supabase

Migrate Firebase auth users to Supabase Auth.

Supabase provides several tools to help migrate auth users from a Firebase project to a Supabase project. There are two parts to the migration process:

Clone the firebase-to-supabase repository:

In the /auth directory, create a file named supabase-service.json with the following contents:

On your project dashboard, click Connect

Under the Session pooler, click on the View parameters under the connect string. Replace the Host and User fields with the values shown.

Enter the password you used when you created your Supabase project in the password entry in the supabase-service.json file.

node firestoreusers2json.js [<filename.json>] [<batch_size>]

node import_users.js <path_to_json_file> [<batch_size>]

For more advanced migrations, including the use of a middleware server component for verifying a user's existing Firebase password and updating that password in your Supabase project the first time a user logs in, see the firebase-to-supabase repo.

Contact us if you need more help migrating your project.

Latest product updates?

Something's not right?

**Examples**:

```text
1git clone https://github.com/supabase-community/firebase-to-supabase.git
```

```text
1234567{  "host": "database.server.com",  "password": "secretpassword",  "user": "postgres",  "database": "postgres",  "port": 5432}
```

```text
1234567hash_config {  algorithm: SCRYPT,  base64_signer_key: XXXX/XXX+XXXXXXXXXXXXXXXXX+XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX==,  base64_salt_separator: Aa==,  rounds: 8,  mem_cost: 14,}
```

---

## Migrate from Firebase Auth to Supabase | Supabase Docs

**URL**: https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-auth

**Contents**:
- Migrate from Firebase Auth to Supabase
- Migrate Firebase auth users to Supabase Auth.
- Set up the migration tool #
- Generate a Firebase private key #
- Save your Firebase password hash parameters #
- Command line options#
  - Dump Firestore users to a JSON file #
  - Import JSON users file to Supabase Auth (Postgres: auth.users#

Migrate from Firebase Auth to Supabase

Migrate Firebase auth users to Supabase Auth.

Supabase provides several tools to help migrate auth users from a Firebase project to a Supabase project. There are two parts to the migration process:

Clone the firebase-to-supabase repository:

In the /auth directory, create a file named supabase-service.json with the following contents:

On your project dashboard, click Connect

Under the Session pooler, click on the View parameters under the connect string. Replace the Host and User fields with the values shown.

Enter the password you used when you created your Supabase project in the password entry in the supabase-service.json file.

node firestoreusers2json.js [<filename.json>] [<batch_size>]

node import_users.js <path_to_json_file> [<batch_size>]

For more advanced migrations, including the use of a middleware server component for verifying a user's existing Firebase password and updating that password in your Supabase project the first time a user logs in, see the firebase-to-supabase repo.

Contact us if you need more help migrating your project.

Latest product updates?

Something's not right?

**Examples**:

```text
1git clone https://github.com/supabase-community/firebase-to-supabase.git
```

```text
1234567{  "host": "database.server.com",  "password": "secretpassword",  "user": "postgres",  "database": "postgres",  "port": 5432}
```

```text
1234567hash_config {  algorithm: SCRYPT,  base64_signer_key: XXXX/XXX+XXXXXXXXXXXXXXXXX+XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX==,  base64_salt_separator: Aa==,  rounds: 8,  mem_cost: 14,}
```

---

## Phone Login | Supabase Docs

**URL**: https://supabase.com/docs/guides/auth/phone-login?showSmsProvider=MessageBird

**Contents**:
- Phone Login
- Enabling phone login#
  - Configuring SMS Providers
      - MessageBird
      - Twilio
      - Vonage
      - Textlocal (Community Supported)
- Signing in with phone OTP#

Phone Login is a method of authentication that allows users to log in to a website or application without using a password. The user authenticates through a one-time password (OTP) sent via a channel (SMS or WhatsApp).

At this time, WhatsApp is only supported as a channel for the Twilio and Twilio Verify Providers.

Users can also log in with their phones using Native Mobile Login with the built-in identity provider. For Native Mobile Login with Android and iOS, see the Social Login guides.

To keep SMS sending costs under control, make sure you adjust your project's rate limits and configure CAPTCHA. See the Production Checklist to learn more.

Some countries have special regulations for services that send SMS messages to users, (e.g India's TRAI DLT regulations). Remember to look up and follow the regulations of countries where you operate.

Enable phone authentication on the Auth Providers page for hosted Supabase projects.

For self-hosted projects or local development, use the configuration file. See the configuration variables namespaced under auth.sms.

You also need to set up an SMS provider. Each provider has its own configuration. Supported providers include MessageBird, Twilio, Vonage, and TextLocal (community-supported).

By default, a user can only request an OTP once every 60 seconds and they expire after 1 hour.

With OTP, a user can sign in without setting a password on their account. They need to verify their phone number each time they sign in.

The user receives an SMS with a 6-digit pin that you must verify within 60 seconds.

To verify the one-time password (OTP) sent to the user's phone number, call verifyOtp() with the phone number and OTP:

You should present a form to the user so they can input the 6 digit pin, then send it along with the phone number to verifyOtp:

If successful the user will now be logged in and you should receive a valid session like:

The access token can be sent in the Authorization header as a Bearer token for any CRU

*[Content truncated - see full docs]*

**Examples**:

```javascript
123const { data, error } = await supabase.auth.signInWithOtp({  phone: '+13334445555',})
```

```javascript
12345678const {  data: { session },  error,} = await supabase.auth.verifyOtp({  phone: '13334445555',  token: '123456',  type: 'sms',})
```

```text
123456{  "access_token": "<ACCESS_TOKEN>",  "token_type": "bearer",  "expires_in": 3600,  "refresh_token": "<REFRESH_TOKEN>"}
```

---

## Phone Login | Supabase Docs

**URL**: https://supabase.com/docs/guides/auth/phone-login?showSmsProvider=Vonage

**Contents**:
- Phone Login
- Enabling phone login#
  - Configuring SMS Providers
      - MessageBird
      - Twilio
      - Vonage
      - Textlocal (Community Supported)
- Signing in with phone OTP#

Phone Login is a method of authentication that allows users to log in to a website or application without using a password. The user authenticates through a one-time password (OTP) sent via a channel (SMS or WhatsApp).

At this time, WhatsApp is only supported as a channel for the Twilio and Twilio Verify Providers.

Users can also log in with their phones using Native Mobile Login with the built-in identity provider. For Native Mobile Login with Android and iOS, see the Social Login guides.

To keep SMS sending costs under control, make sure you adjust your project's rate limits and configure CAPTCHA. See the Production Checklist to learn more.

Some countries have special regulations for services that send SMS messages to users, (e.g India's TRAI DLT regulations). Remember to look up and follow the regulations of countries where you operate.

Enable phone authentication on the Auth Providers page for hosted Supabase projects.

For self-hosted projects or local development, use the configuration file. See the configuration variables namespaced under auth.sms.

You also need to set up an SMS provider. Each provider has its own configuration. Supported providers include MessageBird, Twilio, Vonage, and TextLocal (community-supported).

By default, a user can only request an OTP once every 60 seconds and they expire after 1 hour.

With OTP, a user can sign in without setting a password on their account. They need to verify their phone number each time they sign in.

The user receives an SMS with a 6-digit pin that you must verify within 60 seconds.

To verify the one-time password (OTP) sent to the user's phone number, call verifyOtp() with the phone number and OTP:

You should present a form to the user so they can input the 6 digit pin, then send it along with the phone number to verifyOtp:

If successful the user will now be logged in and you should receive a valid session like:

The access token can be sent in the Authorization header as a Bearer token for any CRU

*[Content truncated - see full docs]*

**Examples**:

```javascript
123const { data, error } = await supabase.auth.signInWithOtp({  phone: '+13334445555',})
```

```javascript
12345678const {  data: { session },  error,} = await supabase.auth.verifyOtp({  phone: '13334445555',  token: '123456',  type: 'sms',})
```

```text
123456{  "access_token": "<ACCESS_TOKEN>",  "token_type": "bearer",  "expires_in": 3600,  "refresh_token": "<REFRESH_TOKEN>"}
```

---

## Phone Login | Supabase Docs

**URL**: https://supabase.com/docs/guides/auth/phone-login?showSmsProvider=Twilio

**Contents**:
- Phone Login
- Enabling phone login#
  - Configuring SMS Providers
      - MessageBird
      - Twilio
      - Vonage
      - Textlocal (Community Supported)
- Signing in with phone OTP#

Phone Login is a method of authentication that allows users to log in to a website or application without using a password. The user authenticates through a one-time password (OTP) sent via a channel (SMS or WhatsApp).

At this time, WhatsApp is only supported as a channel for the Twilio and Twilio Verify Providers.

Users can also log in with their phones using Native Mobile Login with the built-in identity provider. For Native Mobile Login with Android and iOS, see the Social Login guides.

To keep SMS sending costs under control, make sure you adjust your project's rate limits and configure CAPTCHA. See the Production Checklist to learn more.

Some countries have special regulations for services that send SMS messages to users, (e.g India's TRAI DLT regulations). Remember to look up and follow the regulations of countries where you operate.

Enable phone authentication on the Auth Providers page for hosted Supabase projects.

For self-hosted projects or local development, use the configuration file. See the configuration variables namespaced under auth.sms.

You also need to set up an SMS provider. Each provider has its own configuration. Supported providers include MessageBird, Twilio, Vonage, and TextLocal (community-supported).

By default, a user can only request an OTP once every 60 seconds and they expire after 1 hour.

With OTP, a user can sign in without setting a password on their account. They need to verify their phone number each time they sign in.

The user receives an SMS with a 6-digit pin that you must verify within 60 seconds.

To verify the one-time password (OTP) sent to the user's phone number, call verifyOtp() with the phone number and OTP:

You should present a form to the user so they can input the 6 digit pin, then send it along with the phone number to verifyOtp:

If successful the user will now be logged in and you should receive a valid session like:

The access token can be sent in the Authorization header as a Bearer token for any CRU

*[Content truncated - see full docs]*

**Examples**:

```javascript
123const { data, error } = await supabase.auth.signInWithOtp({  phone: '+13334445555',})
```

```javascript
12345678const {  data: { session },  error,} = await supabase.auth.verifyOtp({  phone: '13334445555',  token: '123456',  type: 'sms',})
```

```text
123456{  "access_token": "<ACCESS_TOKEN>",  "token_type": "bearer",  "expires_in": 3600,  "refresh_token": "<REFRESH_TOKEN>"}
```

---

## SSO and Social Login with WorkOS | Supabase Docs

**URL**: https://supabase.com/docs/guides/auth/social-login/auth-workos

**Contents**:
- SSO and Social Login with WorkOS
- Use Social Login with WorkOS#
  - Step 1. Create a WorkOS organization#
- Step 2. Obtain your Client ID and WORKOS_API_KEY values#
- Step 3. Add your WorkOS credentials to your Supabase project#
- Step 4. Set your Supabase redirect URI in the WorkOS Dashboard#
- Step 5. Add login code to your client app#
- Resources#

SSO and Social Login with WorkOS

Log in to the WorkOS dashboard and visit the Organizations tab to create an organization.

Alternatively, you can create an organization via the WorkOS API.

Visit the getting started page of the WorkOS Dashboard. Copy the following values from the Quickstart panel:

You must be signed in to see these values.

You can also configure the WorkOS auth provider using the Management API:

Visit the WorkOS dashboard and click the redirects button in the left navigation panel.

On the redirects page, enter your Supabase project's Callback URL (for OAuth) which you saved in the previous step, as shown below:

When a user signs in, call signInWithOAuth with workos as the provider.

You can find your connection_id in the WorkOS dashboard under the Organizations tab. Select your organization and then click View connection.

Within your specified callback URL, you'll exchange the code for a logged-in user profile:

Latest product updates?

Something's not right?

**Examples**:

```text
1234567891011121314# Get your access token from https://supabase.com/dashboard/account/tokensexport SUPABASE_ACCESS_TOKEN="your-access-token"export PROJECT_REF="your-project-ref"# Configure WorkOS auth providercurl -X PATCH "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" \  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \  -H "Content-Type: application/json" \  -d '{    "external_workos_enabled": true,    "external_workos_url": "https://api.workos.com",    "external_workos_cli
...
```

```javascript
123456789101112131415async function signInWithWorkOS() {  const { data, error } = await supabase.auth.signInWithOAuth({    provider: 'workos',    options: {      redirectTo: 'http://example.com/auth/v1/callback', // Make sure your redirect URL is configured in the Supabase Dashboard Auth settings      queryParams: {        connection: '<connection_id>',      },    },  })  if (data.url) {    redirect(data.url) // use the redirect API for your server or framework  }}
```

```python
123456789101112131415161718192021222324252627282930313233import { NextResponse } from 'next/server'import { createClient } from '@/utils/supabase/server'export async function GET(request: Request) {  const { searchParams, origin } = new URL(request.url)  const code = searchParams.get('code')  // if "next" is in param, use it as the redirect URL  let next = searchParams.get('next') ?? '/'  if (!next.startsWith('/')) {    // if "next" is not a relative URL, use the default    next = '/'  }  if (co
...
```

---

## Self-Hosting | Supabase Docs

**URL**: https://supabase.com/docs/reference/self-hosting-auth/introduction

**Contents**:
- Self-Hosting Auth
  - Client libraries#
  - Additional links#
- Generates an email action link.
  - Body
  - Response codes
  - Response (200)
- Get a user.

The Supabase Auth Server (GoTrue) is a JSON Web Token (JWT)-based API for managing users and issuing access tokens.

GoTrue is an open-source API written in Golang, that acts as a self-standing API service for handling user registration and authentication for JAM projects. It's based on OAuth2 and JWT and handles user signup, authentication, and custom user data.

Latest product updates?

Something's not right?

**Examples**:

```text
12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849{  "action_link": "lorem",  "app_metadata": {    "property1": null,    "property2": null  },  "aud": "lorem",  "banned_until": "2021-12-31T23:34:00Z",  "confirmation_sent_at": "2021-12-31T23:34:00Z",  "confirmed_at": "2021-12-31T23:34:00Z",  "created_at": "2021-12-31T23:34:00Z",  "email": "lorem",  "email_change_sent_at": "2021-12-31T23:34:00Z",  "email_confirmed_at": "2021-12-31T23:34:00Z",  "email_otp": "l
...
```

```text
1234567891011121314151617181920212223242526272829303132333435363738394041424344{  "app_metadata": {    "property1": null,    "property2": null  },  "aud": "lorem",  "banned_until": "2021-12-31T23:34:00Z",  "confirmation_sent_at": "2021-12-31T23:34:00Z",  "confirmed_at": "2021-12-31T23:34:00Z",  "created_at": "2021-12-31T23:34:00Z",  "email": "lorem",  "email_change_sent_at": "2021-12-31T23:34:00Z",  "email_confirmed_at": "2021-12-31T23:34:00Z",  "id": "fbdf5a53-161e-4460-98ad-0e39408d8689",  "id
...
```

```text
1234567891011121314151617181920212223242526272829303132333435363738394041424344{  "app_metadata": {    "property1": null,    "property2": null  },  "aud": "lorem",  "banned_until": "2021-12-31T23:34:00Z",  "confirmation_sent_at": "2021-12-31T23:34:00Z",  "confirmed_at": "2021-12-31T23:34:00Z",  "created_at": "2021-12-31T23:34:00Z",  "email": "lorem",  "email_change_sent_at": "2021-12-31T23:34:00Z",  "email_confirmed_at": "2021-12-31T23:34:00Z",  "id": "fbdf5a53-161e-4460-98ad-0e39408d8689",  "id
...
```

---

## Send emails with custom SMTP | Supabase Docs

**URL**: https://supabase.com/docs/guides/auth/auth-smtp

**Contents**:
- Send emails with custom SMTP
- How to set up a custom SMTP server?#
- Dealing with abuse: How to maintain the sending reputation of your SMTP server?#
  - Additional best practices#
  - Is this helpful?

Send emails with custom SMTP

If you're using Supabase Auth with the following configuration:

You will need to set up a custom SMTP server to handle the delivery of messages to your users.

To get you started and let you explore and set up email message templates for your application, Supabase provides a simple SMTP server for all projects. This server imposes a few important restrictions and is not meant for production use.

Send messages only to pre-authorized addresses.

Unless you configure a custom SMTP server for your project, Supabase Auth will refuse to deliver messages to addresses that are not part of the project's team. You can manage this in the Team tab of the organization's settings.

For example, if your project's organization has these member accounts person-a@example.com, person-b@example.com and person-c@example.com then Supabase Auth will only send messages to these addresses. All other addresses will fail with the error message Email address not authorized.

Significant rate-limits that can change over time.

To maintain the health and reputation of the default SMTP sending service, the number of messages your project can send is limited and can change without notice. Currently this value is set to 2 messages per hour.

No SLA guarantee on message delivery or uptime for the default SMTP service.

The default SMTP service is provided as best-effort only and intended for the following non-production use cases:

We urge all customers to set up custom SMTP server for all other use cases.

Supabase Auth works with any email sending service that supports the SMTP protocol. First you will need to choose a service, create an account (if you already do not have one) and obtain the SMTP server settings and credentials for your account. These include: the SMTP server host, port, user and password. You will also need to choose a default From address, usually something like no-reply@example.com.

A non-exhaustive list of services that work with Supabase Auth

*[Content truncated - see full docs]*

**Examples**:

```text
12345678910111213141516171819# Get your access token from https://supabase.com/dashboard/account/tokensexport SUPABASE_ACCESS_TOKEN="your-access-token"export PROJECT_REF="your-project-ref"# Configure custom SMTPcurl -X PATCH "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" \  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \  -H "Content-Type: application/json" \  -d '{    "external_email_enabled": true,    "mailer_secure_email_change_enabled": true,    "mailer_autoconfirm": fal
...
```

---

## Social Login | Supabase Docs

**URL**: https://supabase.com/docs/guides/auth/social-login

**Contents**:
- Social Login
- Benefits#
- Set up a social provider with Supabase Auth#
      - Google
      - Facebook
      - Apple
      - Azure (Microsoft)
      - Twitter

Social Login (OAuth) is an open standard for authentication that allows users to log in to one website or application using their credentials from another website or application. OAuth allows users to grant third-party applications access to their online accounts without sharing their passwords. OAuth is commonly used for things like logging in to a social media account from a third-party app. It is a secure and convenient way to authenticate users and share information between applications.

There are several reasons why you might want to add social login to your applications:

Improved user experience: Users can register and log in to your application using their existing social media accounts, which can be faster and more convenient than creating a new account from scratch. This makes it easier for users to access your application, improving their overall experience.

Better user engagement: You can access additional data and insights about your users, such as their interests, demographics, and social connections. This can help you tailor your content and marketing efforts to better engage with your users and provide a more personalized experience.

Increased security: Social login can improve the security of your application by leveraging the security measures and authentication protocols of the social media platforms that your users are logging in with. This can help protect against unauthorized access and account takeovers.

Supabase supports a suite of social providers. Follow these guides to configure a social provider for your platform.

You can use the provider token and provider refresh token returned to make API calls to the OAuth provider. For example, you can use the Google provider token to access Google APIs on behalf of your user.

Supabase Auth does not manage refreshing the provider token for the user. Your application will need to use the provider refresh token to obtain a new provider token. If no provider refresh token is returned, then it coul

*[Content truncated - see full docs]*

---

## Users | Supabase Docs

**URL**: https://supabase.com/docs/guides/auth/users

**Contents**:
- Users
- Permanent and anonymous users#
      - Anonymous users do not use the anon role
- The user object#
- Resources#
  - Is this helpful?

A user in Supabase Auth is someone with a user ID, stored in the Auth schema. Once someone is a user, they can be issued an Access Token, which can be used to access Supabase endpoints. The token is tied to the user, so you can restrict access to resources via RLS policies.

Supabase distinguishes between permanent and anonymous users.

Anonymous users are useful for:

See the Anonymous Signins guide to learn more about anonymous users.

Just like permanent users, anonymous users use the authenticated role for database access.

The anon role is for those who aren't signed in at all and are not tied to any user ID. We refer to these as unauthenticated or public users.

The user object stores all the information related to a user in your application. The user object can be retrieved using one of these methods:

A user can sign in with one of the following methods:

An identity describes the authentication method that a user can use to sign in. A user can have multiple identities. These are the types of identities supported:

A user with an email or phone identity will be able to sign in with either a password or passwordless method (e.g. use a one-time password (OTP) or magic link). By default, a user with an unverified email or phone number will not be able to sign in.

The user object contains the following attributes:

Latest product updates?

Something's not right?

---
