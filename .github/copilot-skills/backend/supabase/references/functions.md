# Supabase - Functions

**Pages**: 16

---

## Background Tasks | Supabase Docs

**URL**: https://supabase.com/docs/guides/functions/background-tasks

**Contents**:
- Background Tasks
- Run background tasks in an Edge Function outside of the request handler.
- Overview#
- Handling errors#
- Testing background tasks locally#
  - Is this helpful?

Run background tasks in an Edge Function outside of the request handler.

Edge Function instances can process background tasks outside of the request handler. Background tasks are useful for asynchronous operations like uploading a file to Storage, updating a database, or sending events to a logging service. You can respond to the request immediately and leave the task running in the background.

You can use EdgeRuntime.waitUntil(promise) to explicitly mark background tasks. The Function instance continues to run until the promise provided to waitUntil completes.

You can call EdgeRuntime.waitUntil in the request handler too. This will not block the request.

You can listen to the beforeunload event handler to be notified when the Function is about to be shut down.

We recommend using try/catch blocks within your background task function to handle errors.

You can also add an event listener to unhandledrejection to handle any promises without a rejection handler.

The maximum duration is capped based on the wall-clock, CPU, and memory limits. The function will shut down when it reaches one of these limits.

When testing Edge Functions locally with Supabase CLI, the instances are terminated automatically after a request is completed. This will prevent background tasks from running to completion.

To prevent that, you can update the supabase/config.toml with the following settings:

Latest product updates?

Something's not right?

**Examples**:

```javascript
1234567// Mark the asyncLongRunningTask's returned promise as a background task.// ⚠️ We are NOT using `await` because we don't want it to block!EdgeRuntime.waitUntil(asyncLongRunningTask())Deno.serve(async (req) => {  return new Response(...)})
```

```javascript
123456Deno.serve(async (req) => {  // Won't block the request, runs in background.  EdgeRuntime.waitUntil(asyncLongRunningTask())  return new Response(...)})
```

```javascript
1234567891011EdgeRuntime.waitUntil(asyncLongRunningTask())// Use beforeunload event handler to be notified when function is about to shutdownaddEventListener('beforeunload', (ev) => {  console.log('Function will be shutdown due to', ev.detail?.reason)  // Save state or log the current progress})Deno.serve(async (req) => {  return new Response(...)})
```

---

## Building a Discord Bot | Supabase Docs

**URL**: https://supabase.com/docs/guides/functions/examples/discord-bot

**Contents**:
- Building a Discord Bot
- Create an application on Discord Developer portal#
- Code#
- Deploy the slash command handler#
  - Configure Discord application to use our URL as interactions endpoint URL#
- Install the slash command on your Discord server#
- Run locally#
  - Is this helpful?

Building a Discord Bot

A new application is created which will hold our Slash Command. Don't close the tab as we need information from this application page throughout our development.

Before we can write some code, we need to curl a discord endpoint to register a Slash Command in our app.

Fill DISCORD_BOT_TOKEN with the token available in the Bot section and CLIENT_ID with the ID available on the General Information section of the page and run the command on your terminal.

This will register a Slash Command named hello that accepts a parameter named name of type string.

Navigate to your Function details in the Supabase Dashboard to get your Endpoint URL.

The application is now ready. Let's proceed to the next section to install it.

So to use the hello Slash Command, we need to install our Greeter application on our Discord server. Here are the steps:

Open Discord, type /Promise and press Enter.

Latest product updates?

Something's not right?

**Examples**:

```text
1234567BOT_TOKEN='replace_me_with_bot_token'CLIENT_ID='replace_me_with_client_id'curl -X POST \-H 'Content-Type: application/json' \-H "Authorization: Bot $BOT_TOKEN" \-d '{"name":"hello","description":"Greet a person","options":[{"name":"name","description":"The name of the person","type":3,"required":true}]}' \"https://discord.com/api/v8/applications/$CLIENT_ID/commands"
```

```python
12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970717273747576777879808182838485868788899091929394// Sift is a small routing library that abstracts away details like starting a// listener on a port, and provides a simple function (serve) that has an API// to invoke a function for a specific path.import { json, serve, validateRequest } from 'https://deno.land/x/sift@0.6.0/mod.ts'// TweetNaCl is a cryptography library
...
```

```javascript
12supabase functions deploy discord-bot --no-verify-jwtsupabase secrets set DISCORD_PUBLIC_KEY=your_public_key
```

---

## Building a Telegram Bot | Supabase Docs

**URL**: https://supabase.com/docs/guides/functions/examples/telegram-bot

**Contents**:
- Building a Telegram Bot
  - Is this helpful?

Building a Telegram Bot

Handle Telegram Bot Webhooks with the grammY framework. grammY is an open source Telegram Bot Framework which makes it easy to handle and respond to incoming messages. View on GitHub.

Latest product updates?

Something's not right?

---

## CAPTCHA support with Cloudflare Turnstile | Supabase Docs

**URL**: https://supabase.com/docs/guides/functions/examples/cloudflare-turnstile

**Contents**:
- CAPTCHA support with Cloudflare Turnstile
- Setup#
- Code#
- Deploy the server-side validation Edge Functions#
- Invoke the function from your site#
  - Is this helpful?

CAPTCHA support with Cloudflare Turnstile

Cloudflare Turnstile is a friendly, free CAPTCHA replacement, and it works seamlessly with Supabase Edge Functions to protect your forms. View on GitHub.

Create a new function in your project:

And add the code to the index.ts file:

Latest product updates?

Something's not right?

**Examples**:

```javascript
1supabase functions new cloudflare-turnstile
```

```python
1234567891011121314151617181920212223242526272829303132333435363738import { corsHeaders } from '../_shared/cors.ts'console.log('Hello from Cloudflare Trunstile!')function ips(req: Request) {  return req.headers.get('x-forwarded-for')?.split(/\s*,\s*/)}Deno.serve(async (req) => {  // This is needed if you're planning to invoke your function from a browser.  if (req.method === 'OPTIONS') {    return new Response('ok', { headers: corsHeaders })  }  const { token } = await req.json()  const clientIp
...
```

```javascript
12supabase functions deploy cloudflare-turnstilesupabase secrets set CLOUDFLARE_SECRET_KEY=your_secret_key
```

---

## CORS (Cross-Origin Resource Sharing) support for Invoking from the browser | Supabase Docs

**URL**: https://supabase.com/docs/guides/functions/cors

**Contents**:
- CORS (Cross-Origin Resource Sharing) support for Invoking from the browser
  - Recommended setup#
  - Is this helpful?

CORS (Cross-Origin Resource Sharing) support for Invoking from the browser

To invoke edge functions from the browser, you need to handle CORS Preflight requests.

See the example on GitHub.

We recommend adding a cors.ts file within a _shared folder which makes it easy to reuse the CORS headers across functions:

You can then import and use the CORS headers within your functions:

Latest product updates?

Something's not right?

**Examples**:

```javascript
1234export const corsHeaders = {  'Access-Control-Allow-Origin': '*',  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',}
```

```python
123456789101112131415161718192021222324252627import { corsHeaders } from '../_shared/cors.ts'console.log(`Function "browser-with-cors" up and running!`)Deno.serve(async (req) => {  // This is needed if you're planning to invoke your function from a browser.  if (req.method === 'OPTIONS') {    return new Response('ok', { headers: corsHeaders })  }  try {    const { name } = await req.json()    const data = {      message: `Hello ${name}!`,    }    return new Response(JSON.stringify(data), {      
...
```

---

## Edge Functions | Supabase Docs

**URL**: https://supabase.com/docs/guides/functions

**Contents**:
- Edge Functions
- Globally distributed TypeScript functions.
- How it works#
- Quick technical notes#
- When to use Edge Functions#
- Examples#
  - Is this helpful?

Globally distributed TypeScript functions.

Edge Functions are server-side TypeScript functions, distributed globally at the edge—close to your users. They can be used for listening to webhooks or integrating your Supabase project with third-parties like Stripe. Edge Functions are developed using Deno, which offers a few benefits to you as a developer:

Check out the Edge Function Examples in our GitHub repository.

Type-Safe SQL with Kysely

Monitoring with Sentry

React Native with Stripe

Building a RESTful Service API

Working with Supabase Storage

Open Graph Image Generation

OG Image Generation & Storage CDN Caching

Oak Server Middleware

Slack Bot Mention Edge Function

Latest product updates?

Something's not right?

---

## Generate Images with Amazon Bedrock | Supabase Docs

**URL**: https://supabase.com/docs/guides/functions/examples/amazon-bedrock-image-generator

**Contents**:
- Generate Images with Amazon Bedrock
- Setup#
  - Configure Storage#
- Code#
- Run the function locally#
- Deploy to your hosted project#
  - Is this helpful?

Generate Images with Amazon Bedrock

Amazon Bedrock is a fully managed service that offers a choice of high-performing foundation models (FMs) from leading AI companies like AI21 Labs, Anthropic, Cohere, Meta, Mistral AI, Stability AI, and Amazon. Each model is accessible through a common API which implements a broad set of features to help build generative AI applications with security, privacy, and responsible AI in mind.

This guide will walk you through an example using the Amazon Bedrock JavaScript SDK in Supabase Edge Functions to generate images using the Amazon Titan Image Generator G1 model.

Create a new function in your project:

And add the code to the index.ts file:

You've now deployed a serverless function that uses AI to generate and upload images to your Supabase storage bucket.

Latest product updates?

Something's not right?

**Examples**:

```text
12345678AWS_DEFAULT_REGION="<your_region>"AWS_ACCESS_KEY_ID="<replace_your_own_credentials>"AWS_SECRET_ACCESS_KEY="<replace_your_own_credentials>"AWS_SESSION_TOKEN="<replace_your_own_credentials>"# Mocked config filesAWS_SHARED_CREDENTIALS_FILE="./aws/credentials"AWS_CONFIG_FILE="./aws/config"
```

```javascript
1supabase functions new amazon-bedrock
```

```python
123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778// We need to mock the file system for the AWS SDK to work.import { prepareVirtualFile } from 'https://deno.land/x/mock_file@v1.1.2/mod.ts'import { BedrockRuntimeClient, InvokeModelCommand } from 'npm:@aws-sdk/client-bedrock-runtime'import { createClient } from 'npm:@supabase/supabase-js'import { decode } from 'npm:base64-arraybuffer'console.log('Hell
...
```

---

## Generating OG Images | Supabase Docs

**URL**: https://supabase.com/docs/guides/functions/examples/og-image

**Contents**:
- Generating OG Images
- Code#
  - Is this helpful?

Generate Open Graph images with Deno and Supabase Edge Functions. View on GitHub.

Create a handler.tsx file to construct the OG image in React:

Create an index.ts file to execute the handler on incoming requests:

Latest product updates?

Something's not right?

**Examples**:

```python
12345678910111213141516171819202122import React from 'https://esm.sh/react@18.2.0'import { ImageResponse } from 'https://deno.land/x/og_edge@0.0.4/mod.ts'export default function handler(req: Request) {  return new ImageResponse(    (      <div        style={{          width: '100%',          height: '100%',          display: 'flex',          alignItems: 'center',          justifyContent: 'center',          fontSize: 128,          background: 'lavender',        }}      >        Hello OG Image!   
...
```

```python
12345import handler from './handler.tsx'console.log('Hello from og-image Function!')Deno.serve(handler)
```

---

## GitHub Actions | Supabase Docs

**URL**: https://supabase.com/docs/guides/functions/examples/github-actions

**Contents**:
- GitHub Actions
  - Is this helpful?

Use the Supabase CLI together with GitHub Actions to automatically deploy our Supabase Edge Functions. View on GitHub.

Since Supabase CLI v1.62.0 you can deploy all functions with a single command.

Individual function configuration like JWT verification and import map location can be set via the config.toml file.

Latest product updates?

Something's not right?

**Examples**:

```javascript
123456789101112131415161718192021222324name: Deploy Functionon:  push:    branches:      - main  workflow_dispatch:jobs:  deploy:    runs-on: ubuntu-latest    env:      SUPABASE_ACCESS_TOKEN: YOUR_SUPABASE_ACCESS_TOKEN      PROJECT_ID: YOUR_SUPABASE_PROJECT_ID    steps:      - uses: actions/checkout@v4      - uses: supabase/setup-cli@v1        with:          version: latest      - run: supabase functions deploy --project-ref $PROJECT_ID
```

```javascript
12[functions.hello-world]verify_jwt = false
```

---

## Handling Stripe Webhooks | Supabase Docs

**URL**: https://supabase.com/docs/guides/functions/examples/stripe-webhooks

**Contents**:
- Handling Stripe Webhooks
  - Is this helpful?

Handling Stripe Webhooks

Handling signed Stripe Webhooks with Edge Functions. View on GitHub.

Latest product updates?

Something's not right?

**Examples**:

```python
1234567891011121314151617181920212223242526272829303132333435363738// Follow this setup guide to integrate the Deno language server with your editor:// https://deno.land/manual/getting_started/setup_your_environment// This enables autocomplete, go to definition, etc.// Import via bare specifier thanks to the import_map.json file.import Stripe from 'https://esm.sh/stripe@14?target=denonext'const stripe = new Stripe(Deno.env.get('STRIPE_API_KEY') as string, {  // This is needed to use the Fetch AP
...
```

---

## Monitoring with Sentry | Supabase Docs

**URL**: https://supabase.com/docs/guides/functions/examples/sentry-monitoring

**Contents**:
- Monitoring with Sentry
  - Prerequisites#
  - 1. Create Supabase function#
  - 2. Add the Sentry Deno SDK#
  - 3. Deploy and test#
  - 4. Try it yourself#
- Working with scopes#
  - Is this helpful?

Monitoring with Sentry

Add the Sentry Deno SDK to your Supabase Edge Functions to track exceptions and get notified of errors or performance issues.

Create a new function locally:

Handle exceptions within your function and send them to Sentry.

Run function locally:

Test it: http://localhost:54321/functions/v1/sentryfied

Deploy function to Supabase:

Find the complete example on GitHub.

Sentry Deno SDK currently do not support Deno.serve instrumentation, which means that there is no scope separation between requests. Because of that, when the Edge Functions runtime is reused between multiple requests, all globally captured breadcrumbs and contextual data will be shared, which is not the desired behavior. To work around this, all default integrations in the example code above are disabled, and you should be relying on withScope to encapsulate all Sentry SDK API calls, or pass context directly to the captureException or captureMessage calls.

Latest product updates?

Something's not right?

**Examples**:

```javascript
1supabase functions new sentryfied
```

```python
1234567891011121314151617181920212223242526272829303132333435import * as Sentry from 'https://deno.land/x/sentry/index.mjs'Sentry.init({  // https://docs.sentry.io/product/sentry-basics/concepts/dsn-explainer/#where-to-find-your-dsn  dsn: SENTRY_DSN,  defaultIntegrations: false,  // Performance Monitoring  tracesSampleRate: 1.0,  // Set sampling rate for profiling - this is relative to tracesSampleRate  profilesSampleRate: 1.0,})// Set region and execution_id as custom tagsSentry.setTag('region'
...
```

```javascript
12supabase startsupabase functions serve --no-verify-jwt
```

---

## Rate Limiting Edge Functions | Supabase Docs

**URL**: https://supabase.com/docs/guides/functions/examples/rate-limiting

**Contents**:
- Rate Limiting Edge Functions
  - Is this helpful?

Rate Limiting Edge Functions

Redis is an open source (BSD licensed), in-memory data structure store used as a database, cache, message broker, and streaming engine. It is optimized for atomic operations like incrementing a value, for example for a view counter or rate limiting. We can even rate limit based on the user ID from Supabase Auth!

Upstash provides an HTTP/REST based Redis client which is ideal for serverless use-cases and therefore works well with Supabase Edge Functions.

Find the code on GitHub.

Latest product updates?

Something's not right?

---

## Sending Emails | Supabase Docs

**URL**: https://supabase.com/docs/guides/functions/examples/send-emails

**Contents**:
- Sending Emails
  - Prerequisites#
  - 1. Create Supabase function#
  - 2. Edit the handler function#
  - 3. Deploy and send email#
  - 4. Try it yourself#
  - Is this helpful?

Sending emails from Edge Functions using the Resend API.

To get the most out of this guide, you’ll need to:

Make sure you have the latest version of the Supabase CLI installed.

Create a new function locally:

Store the RESEND_API_KEY in your .env file.

Paste the following code into the index.ts file:

Run function locally:

Test it: http://localhost:54321/functions/v1/resend

Deploy function to Supabase:

When you deploy to Supabase, make sure that your RESEND_API_KEY is set in Edge Function Secrets Management

Open the endpoint URL to send an email:

Find the complete example on GitHub.

Latest product updates?

Something's not right?

**Examples**:

```javascript
1supabase functions new resend
```

```javascript
12345678910111213141516171819202122232425262728const RESEND_API_KEY = Deno.env.get('RESEND_API_KEY')const handler = async (_request: Request): Promise<Response> => {  const res = await fetch('https://api.resend.com/emails', {    method: 'POST',    headers: {      'Content-Type': 'application/json',      Authorization: `Bearer ${RESEND_API_KEY}`,    },    body: JSON.stringify({      from: 'onboarding@resend.dev',      to: 'delivered@resend.dev',      subject: 'hello world',      html: '<strong>it
...
```

```javascript
12supabase startsupabase functions serve --no-verify-jwt --env-file .env
```

---

## Slack Bot Mention Edge Function | Supabase Docs

**URL**: https://supabase.com/docs/guides/functions/examples/slack-bot-mention

**Contents**:
- Slack Bot Mention Edge Function
- Configuring Slack apps#
- Creating the Edge Function#
  - Is this helpful?

Slack Bot Mention Edge Function

The Slack Bot Mention Edge Function allows you to process mentions in Slack and respond accordingly.

For your bot to seamlessly interact with Slack, you'll need to configure Slack Apps:

Deploy the following code as an Edge function using the CLI:

Here's the code of the Edge Function, you can change the response to handle the text received:

Latest product updates?

Something's not right?

**Examples**:

```text
supabase --project-ref nacho_slacker secrets set SLACK_TOKEN=<PASTE_YOUR_TOKEN_HERE>
```

```python
12345678910111213141516171819202122232425262728293031323334import { WebClient } from 'https://deno.land/x/slack_web_api@6.7.2/mod.js'const slackBotToken = Deno.env.get('SLACK_TOKEN') ?? ''const botClient = new WebClient(slackBotToken)console.log(`Slack URL verification function up and running!`)Deno.serve(async (req) => {  try {    const reqBody = await req.json()    console.log(JSON.stringify(reqBody, null, 2))    const { token, challenge, type, event } = reqBody    if (type == 'url_verificatio
...
```

---

## Taking Screenshots with Puppeteer | Supabase Docs

**URL**: https://supabase.com/docs/guides/functions/examples/screenshots

**Contents**:
- Taking Screenshots with Puppeteer
  - Is this helpful?

Taking Screenshots with Puppeteer

Puppeteer is a handy tool to programmatically take screenshots and generate PDFs. However, trying to do so in Edge Functions can be challenging due to the size restrictions. Luckily there is a serverless browser offering available that we can connect to via WebSockets.

Find the code on GitHub.

Latest product updates?

Something's not right?

---

## Upstash Redis | Supabase Docs

**URL**: https://supabase.com/docs/guides/functions/examples/upstash-redis

**Contents**:
- Upstash Redis
- Redis database setup#
- Code#
- Run locally#
- Deploy#
  - Is this helpful?

A Redis counter example that stores a hash of function invocation count per region. Find the code on GitHub.

Create a Redis database using the Upstash Console or Upstash CLI.

Select the Global type to minimize the latency from all edge locations. Copy the UPSTASH_REDIS_REST_URL and UPSTASH_REDIS_REST_TOKEN to your .env file.

You'll find them under Details > REST API > .env.

Make sure you have the latest version of the Supabase CLI installed.

Create a new function in your project:

And add the code to the index.ts file:

Navigate to http://localhost:54321/functions/v1/upstash-redis-counter.

Latest product updates?

Something's not right?

**Examples**:

```javascript
1cp supabase/functions/upstash-redis-counter/.env.example supabase/functions/upstash-redis-counter/.env
```

```javascript
1supabase functions new upstash-redis-counter
```

```python
12345678910111213141516171819202122232425262728293031323334import { Redis } from 'https://deno.land/x/upstash_redis@v1.19.3/mod.ts'console.log(`Function "upstash-redis-counter" up and running!`)Deno.serve(async (_req) => {  try {    const redis = new Redis({      url: Deno.env.get('UPSTASH_REDIS_REST_URL')!,      token: Deno.env.get('UPSTASH_REDIS_REST_TOKEN')!,    })    const deno_region = Deno.env.get('DENO_REGION')    if (deno_region) {      // Increment region counter      await redis.hincrb
...
```

---
