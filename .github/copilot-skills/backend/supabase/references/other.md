# Supabase - Other

**Pages**: 44

---

## API | Supabase Docs

**URL**: https://supabase.com/docs/guides/queues/api

**Contents**:
- API
  - pgmq_public.pop(queue_name)#
  - pgmq_public.send(queue_name, message, sleep_seconds)#
  - pgmq_public.send_batch(queue_name, messages, sleep_seconds)#
  - pgmq_public.archive(queue_name, message_id)#
  - pgmq_public.delete(queue_name, message_id)#
  - pgmq_public.read(queue_name, sleep_seconds, n)#
  - Is this helpful?

When you create a Queue in Supabase, you can choose to create helper database functions in the pgmq_public schema. This schema exposes operations to manage Queue Messages to consumers client-side, but does not expose functions for creating or dropping Queues.

Database functions in pgmq_public can be exposed via Supabase Data API so consumers client-side can call them. Visit the Quickstart for an example.

Retrieves the next available message and deletes it from the specified Queue.

Adds a Message to the specified Queue, optionally delaying its visibility to all consumers by a number of seconds.

Adds a batch of Messages to the specified Queue, optionally delaying their availability to all consumers by a number of seconds.

Archives a Message by moving it from the Queue table to the Queue's archive table.

Permanently deletes a Message from the specified Queue.

Reads up to "n" Messages from the specified Queue with an optional "sleep_seconds" (visibility timeout).

Latest product updates?

Something's not right?

---

## Adding generative Q&A for your documentation | Supabase Docs

**URL**: https://supabase.com/docs/guides/ai/examples/headless-vector-search

**Contents**:
- Adding generative Q&A for your documentation
- Learn how to build a ChatGPT-style doc search powered using our headless search toolkit.
- Tech stack#
- Toolkit#
- Usage#
  - Prepare your database#
  - Ingest your documentation#
  - Add a search interface#

Adding generative Q&A for your documentation

Learn how to build a ChatGPT-style doc search powered using our headless search toolkit.

Supabase provides a Headless Search Toolkit for adding "Generative Q&A" to your documentation. The toolkit is "headless", so that you can integrate it into your existing website and style it to match your website theme.

You can see how this works with the Supabase docs. Just hit cmd+k and "ask" for something like "what are the features of Supabase?". You will see that the response is streamed back, using the information provided in the docs:

This toolkit consists of 2 parts:

There are 3 steps to build similarity search inside your documentation:

To prepare, create a new Supabase project and store the database and API credentials, which you can find in the project settings.

Now we can use the Headless Vector Search instructions to set up the database:

Now we need to push your documentation into the database as embeddings. You can do this manually, but to make it easier we've created a GitHub Action which can update your database every time there is a Pull Request.

In your knowledge base repository, create a new action called .github/workflows/generate_embeddings.yml with the following content:

Make sure to choose the latest version, and set your SUPABASE_SERVICE_ROLE_KEY and OPENAI_API_KEY as repository secrets in your repo settings (settings > secrets > actions).

Now inside your docs, you need to create a search interface. Because this is a headless interface, you can use it with any language. The only requirement is that you send the user query to the query Edge Function, which will stream an answer back from OpenAI. It might look something like this:

Latest product updates?

Something's not right?

**Examples**:

```text
1234567891011121314151617name: 'generate_embeddings'on: # run on main branch changes  push:    branches:      - mainjobs:  generate:    runs-on: ubuntu-latest    steps:      - uses: actions/checkout@v3      - uses: supabase/embeddings-generator@v0.0.x # Update this to the latest version.        with:          supabase-url: 'https://your-project-ref.supabase.co' # Update this to your project URL.          supabase-service-role-key: ${{ secrets.SUPABASE_SERVICE_ROLE_KEY }}          openai-key: ${{
...
```

```javascript
12345678910111213141516171819202122232425262728293031const onSubmit = (e: Event) => {  e.preventDefault()  answer.value = ""  isLoading.value = true  const query = new URLSearchParams({ query: inputRef.current!.value })  const projectUrl = `https://your-project-ref.supabase.co/functions/v1`  const queryURL = `${projectURL}/${query}`  const eventSource = new EventSource(queryURL)  eventSource.addEventListener("error", (err) => {    isLoading.value = false    console.error(err)  })  eventSource.ad
...
```

---

## Amazon Bedrock | Supabase Docs

**URL**: https://supabase.com/docs/guides/ai/integrations/amazon-bedrock

**Contents**:
- Amazon Bedrock
- Create an environment#
- Create embeddings#
  - Store the embeddings with vecs#
  - Querying for most similar sentences#
- Resources#
  - Is this helpful?

Amazon Bedrock is a fully managed service that offers a choice of high-performing foundation models (FMs) from leading AI companies like AI21 Labs, Anthropic, Cohere, Meta, Mistral AI, Stability AI, and Amazon. Each model is accessible through a common API which implements a broad set of features to help build generative AI applications with security, privacy, and responsible AI in mind.

This guide will walk you through an example using Amazon Bedrock SDK with vecs. We will create embeddings using the Amazon Titan Embeddings G1 – Text v1.2 (amazon.titan-embed-text-v1) model, insert these embeddings into a Postgres database using vecs, and then query the collection to find the most similar sentences to a given query sentence.

First, you need to set up your environment. You will need Python 3.7+ with the vecs and boto3 libraries installed.

You can install the necessary Python libraries using pip:

Next, we will use Amazon’s Titan Embedding G1 - Text v1.2 model to create embeddings for a set of sentences.

Now that we have our embeddings, we can insert them into a Postgres database using vecs.

Now, we query the sentences collection to find the most similar sentences to a sample query sentence. First need to create an embedding for the query sentence. Next, we query the collection we created earlier to find the most similar sentences.

This returns the most similar 3 records and their distance to the query vector.

Latest product updates?

Something's not right?

**Examples**:

```text
1pip install vecs boto3
```

```python
12345678910111213141516171819202122232425262728293031323334import boto3import vecsimport jsonclient = boto3.client(    'bedrock-runtime',    region_name='us-east-1',	# Credentials from your AWS account    aws_access_key_id='<replace_your_own_credentials>',    aws_secret_access_key='<replace_your_own_credentials>',    aws_session_token='<replace_your_own_credentials>',)dataset = [    "The cat sat on the mat.",    "The quick brown fox jumps over the lazy dog.",    "Friends, Romans, countrymen, len
...
```

```text
12345678910111213141516import vecsDB_CONNECTION = "postgresql://<user>:<password>@<host>:<port>/<db_name>"# create vector store clientvx = vecs.Client(DB_CONNECTION)# create a collection named 'sentences' with 1536 dimensional vectors# to match the default dimension of the Titan Embeddings G1 - Text modelsentences = vx.get_or_create_collection(name="sentences", dimension=1536)# upsert the embeddings into the 'sentences' collectionsentences.upsert(records=embeddings)# create an index for the 'sen
...
```

---

## Build a Supabase Integration | Supabase Docs

**URL**: https://supabase.com/docs/guides/integrations/build-a-supabase-integration

**Contents**:
- Build a Supabase Integration
- This guide steps through building a Supabase Integration using OAuth2 and the management API, allowing you to manage users' organizations and projects on their behalf.
- Create an OAuth app#
- Show a "Connect Supabase" button#
- Implementing the OAuth 2.0 flow#
  - Redirecting to the authorize URL#
  - Handling the callback#
- Refreshing an access token#

Build a Supabase Integration

This guide steps through building a Supabase Integration using OAuth2 and the management API, allowing you to manage users' organizations and projects on their behalf.

Using OAuth2.0 you can retrieve an access and refresh token that grant your application full access to the Management API on behalf of the user.

In your user interface, add a "Connect Supabase" button to kick off the OAuth flow. Follow the design guidelines outlined in our brand assets.

Once you've published your OAuth App on Supabase, you can use the OAuth 2.0 protocol get authorization from Supabase users to manage their organizations and projects.

You can use your preferred OAuth2 client or follow the steps below. You can see an example implementation in TypeScript using Supabase Edge Functions on our GitHub.

Within your app's UI, redirect the user to https://api.supabase.com/v1/oauth/authorize. Make sure to include all required query parameters such as:

Find the full example on GitHub.

Once the user consents to providing API access to your OAuth App, Supabase will redirect the user to the redirect_uri provided in the previous step. The URL will contain these query parameters:

Exchange the authorization code for an access and refresh token by calling POST https://api.supabase.com/v1/oauth/token with the following query parameters as content-type application/x-www-form-urlencoded:

If your application need to support dynamically generated Redirect URLs, check out Handling Dynamic Redirect URLs section below.

As per OAuth2 spec, provide the client id and client secret as basic auth header:

Find the full example on GitHub.

You can use the POST /v1/oauth/token endpoint to refresh an access token using the refresh token returned at the end of the previous section.

If the user has revoked access to your application, you will not be able to refresh a token. Furthermore, access tokens will stop working. Make sure you handle HTTP Unauthorized errors when calling any

*[Content truncated - see full docs]*

**Examples**:

```javascript
123456789101112router.get('/connect-supabase/login', async (ctx) => {  // Construct the URL for the authorization redirect and get a PKCE codeVerifier.  const { uri, codeVerifier } = await oauth2Client.code.getAuthorizationUri()  console.log(uri.toString())  // console.log: https://api.supabase.com/v1/oauth/authorize?response_type=code&client_id=7673bde9-be72-4d75-bd5e-b0dba2c49b38&redirect_uri=http%3A%2F%2Flocalhost%3A54321%2Ffunctions%2Fv1%2Fconnect-supabase%2Foauth2%2Fcallback&scope=all&code_
...
```

```javascript
1234567891011121314151617181920212223242526router.get('/connect-supabase/oauth2/callback', async (ctx) => {  // Make sure the codeVerifier is present for the user's session.  const codeVerifier = ctx.state.session.get('codeVerifier') as string  if (!codeVerifier) throw new Error('No codeVerifier!')  // Exchange the authorization code for an access token.  const tokens = await fetch(config.tokenUri, {    method: 'POST',    headers: {      'Content-Type': 'application/x-www-form-urlencoded',      
...
```

```python
123import { SupabaseManagementAPI } from 'supabase-management-js'const client = new SupabaseManagementAPI({ accessToken: '<access token>' })
```

---

## Building ChatGPT plugins | Supabase Docs

**URL**: https://supabase.com/docs/guides/ai/examples/building-chatgpt-plugins

**Contents**:
- Building ChatGPT plugins
- Use Supabase as a Retrieval Store for your ChatGPT plugin.
- What is ChatGPT Retrieval Plugin?#
- Example: Chat with Postgres docs#
  - Step 1: Fork the ChatGPT Retrieval Plugin repository#
  - Step 2: Install dependencies#
  - Step 3: Create a Supabase project#
  - Step 4: Run Postgres locally#

Building ChatGPT plugins

Use Supabase as a Retrieval Store for your ChatGPT plugin.

ChatGPT recently released Plugins which help ChatGPT access up-to-date information, run computations, or use third-party services. If you're building a plugin for ChatGPT, you'll probably want to answer questions from a specific source. We can solve this with “retrieval plugins”, which allow ChatGPT to access information from a database.

A Retrieval Plugin is a Python project designed to inject external data into a ChatGPT conversation. It does a few things:

It allows ChatGPT to dynamically pull relevant information into conversations from your data sources. This could be PDF documents, Confluence, or Notion knowledge bases.

Let’s build an example where we can “ask ChatGPT questions” about the Postgres documentation. Although ChatGPT already knows about the Postgres documentation because it is publicly available, this is a simple example which demonstrates how to work with PDF files.

This plugin requires several steps:

We'll be saving the Postgres documentation in Postgres, and ChatGPT will be retrieving the documentation whenever a user asks a question:

Fork the ChatGPT Retrieval Plugin repository to your GitHub account and clone it to your local machine. Read through the README.md file to understand the project structure.

Choose your desired datastore provider and remove unused dependencies from pyproject.toml. For this example, we'll use Supabase. And install dependencies with Poetry:

Create a Supabase project and database by following the instructions here. Export the environment variables required for the retrieval plugin to work:

For Postgres datastore, you'll need to export these environment variables instead:

To start quicker you may use Supabase CLI to spin everything up locally as it already includes pgvector from the start. Install supabase-cli, go to the examples/providers folder in the repo and run:

This will pull all docker images and run Supabase stack in 

*[Content truncated - see full docs]*

**Examples**:

```text
1poetry install
```

```text
1234export OPENAI_API_KEY=<open_ai_api_key>export DATASTORE=supabaseexport SUPABASE_URL=<supabase_url>export SUPABASE_SERVICE_ROLE_KEY=<supabase_key>
```

```text
1234export OPENAI_API_KEY=<open_ai_api_key>export DATASTORE=postgresexport PG_HOST=<postgres_host_url>export PG_PASSWORD=<postgres_password>
```

---

## CLI Reference | Supabase Docs

**URL**: https://supabase.com/docs/reference/cli/introduction

**Contents**:
- Supabase CLI
  - Additional links#
- Global flags
  - Flags
- supabase bootstrap
  - Usage
  - Flags
- supabase init

The Supabase CLI provides tools to develop your project locally and deploy to the Supabase Platform. The CLI is still under development, but it contains all the functionality for working with your Supabase projects and the Supabase Platform.

Supabase CLI supports global flags for every command.

create a support ticket for any CLI error

output debug logs to stderr

lookup domain names using the specified resolver

enable experimental features

use the specified docker network instead of a generated one

output format of status variables

use a specific profile for connecting to Supabase API

path to a Supabase project directory

answer yes to all prompts

Password to your remote Postgres database.

Initialize configurations for Supabase local development.

A supabase/config.toml file is created in your current working directory. This configuration is specific to each local project.

You may override the directory path by specifying the SUPABASE_WORKDIR environment variable or --workdir flag.

In addition to config.toml, the supabase directory may also contain other Supabase objects, such as migrations, functions, tests, etc.

Overwrite existing supabase/config.toml.

Use OrioleDB storage engine for Postgres.

Generate IntelliJ IDEA settings for Deno.

Generate VS Code settings for Deno.

Connect the Supabase CLI to your Supabase account by logging in with your personal access token.

Your access token is stored securely in native credentials storage. If native credentials storage is unavailable, it will be written to a plain text file at ~/.supabase/access-token.

If this behavior is not desired, such as in a CI environment, you may skip login by specifying the SUPABASE_ACCESS_TOKEN environment variable in other commands.

The Supabase CLI uses the stored token to access Management APIs for projects, functions, secrets, etc.

Name that will be used to store token in your settings

Do not open browser automatically

Use provided token instead of automatic login flo

*[Content truncated - see full docs]*

**Examples**:

```text
1supabase bootstrap [template] [flags]
```

```text
1supabase init [flags]
```

```text
1supabase init
```

---

## CLI Reference | Supabase Docs

**URL**: https://supabase.com/docs/reference/cli/supabase-test-new

**Contents**:
- Supabase CLI
  - Additional links#
- Global flags
  - Flags
- supabase bootstrap
  - Usage
  - Flags
- supabase init

The Supabase CLI provides tools to develop your project locally and deploy to the Supabase Platform. The CLI is still under development, but it contains all the functionality for working with your Supabase projects and the Supabase Platform.

Supabase CLI supports global flags for every command.

create a support ticket for any CLI error

output debug logs to stderr

lookup domain names using the specified resolver

enable experimental features

use the specified docker network instead of a generated one

output format of status variables

use a specific profile for connecting to Supabase API

path to a Supabase project directory

answer yes to all prompts

Password to your remote Postgres database.

Initialize configurations for Supabase local development.

A supabase/config.toml file is created in your current working directory. This configuration is specific to each local project.

You may override the directory path by specifying the SUPABASE_WORKDIR environment variable or --workdir flag.

In addition to config.toml, the supabase directory may also contain other Supabase objects, such as migrations, functions, tests, etc.

Overwrite existing supabase/config.toml.

Use OrioleDB storage engine for Postgres.

Generate IntelliJ IDEA settings for Deno.

Generate VS Code settings for Deno.

Connect the Supabase CLI to your Supabase account by logging in with your personal access token.

Your access token is stored securely in native credentials storage. If native credentials storage is unavailable, it will be written to a plain text file at ~/.supabase/access-token.

If this behavior is not desired, such as in a CI environment, you may skip login by specifying the SUPABASE_ACCESS_TOKEN environment variable in other commands.

The Supabase CLI uses the stored token to access Management APIs for projects, functions, secrets, etc.

Name that will be used to store token in your settings

Do not open browser automatically

Use provided token instead of automatic login flo

*[Content truncated - see full docs]*

**Examples**:

```text
1supabase bootstrap [template] [flags]
```

```text
1supabase init [flags]
```

```text
1supabase init
```

---

## CLI Reference | Supabase Docs

**URL**: https://supabase.com/docs/reference/cli/supabase-gen-types

**Contents**:
- Supabase CLI
  - Additional links#
- Global flags
  - Flags
- supabase bootstrap
  - Usage
  - Flags
- supabase init

The Supabase CLI provides tools to develop your project locally and deploy to the Supabase Platform. The CLI is still under development, but it contains all the functionality for working with your Supabase projects and the Supabase Platform.

Supabase CLI supports global flags for every command.

create a support ticket for any CLI error

output debug logs to stderr

lookup domain names using the specified resolver

enable experimental features

use the specified docker network instead of a generated one

output format of status variables

use a specific profile for connecting to Supabase API

path to a Supabase project directory

answer yes to all prompts

Password to your remote Postgres database.

Initialize configurations for Supabase local development.

A supabase/config.toml file is created in your current working directory. This configuration is specific to each local project.

You may override the directory path by specifying the SUPABASE_WORKDIR environment variable or --workdir flag.

In addition to config.toml, the supabase directory may also contain other Supabase objects, such as migrations, functions, tests, etc.

Overwrite existing supabase/config.toml.

Use OrioleDB storage engine for Postgres.

Generate IntelliJ IDEA settings for Deno.

Generate VS Code settings for Deno.

Connect the Supabase CLI to your Supabase account by logging in with your personal access token.

Your access token is stored securely in native credentials storage. If native credentials storage is unavailable, it will be written to a plain text file at ~/.supabase/access-token.

If this behavior is not desired, such as in a CI environment, you may skip login by specifying the SUPABASE_ACCESS_TOKEN environment variable in other commands.

The Supabase CLI uses the stored token to access Management APIs for projects, functions, secrets, etc.

Name that will be used to store token in your settings

Do not open browser automatically

Use provided token instead of automatic login flo

*[Content truncated - see full docs]*

**Examples**:

```text
1supabase bootstrap [template] [flags]
```

```text
1supabase init [flags]
```

```text
1supabase init
```

---

## CLI Reference | Supabase Docs

**URL**: https://supabase.com/docs/reference/cli/supabase-db-dump

**Contents**:
- Supabase CLI
  - Additional links#
- Global flags
  - Flags
- supabase bootstrap
  - Usage
  - Flags
- supabase init

The Supabase CLI provides tools to develop your project locally and deploy to the Supabase Platform. The CLI is still under development, but it contains all the functionality for working with your Supabase projects and the Supabase Platform.

Supabase CLI supports global flags for every command.

create a support ticket for any CLI error

output debug logs to stderr

lookup domain names using the specified resolver

enable experimental features

use the specified docker network instead of a generated one

output format of status variables

use a specific profile for connecting to Supabase API

path to a Supabase project directory

answer yes to all prompts

Password to your remote Postgres database.

Initialize configurations for Supabase local development.

A supabase/config.toml file is created in your current working directory. This configuration is specific to each local project.

You may override the directory path by specifying the SUPABASE_WORKDIR environment variable or --workdir flag.

In addition to config.toml, the supabase directory may also contain other Supabase objects, such as migrations, functions, tests, etc.

Overwrite existing supabase/config.toml.

Use OrioleDB storage engine for Postgres.

Generate IntelliJ IDEA settings for Deno.

Generate VS Code settings for Deno.

Connect the Supabase CLI to your Supabase account by logging in with your personal access token.

Your access token is stored securely in native credentials storage. If native credentials storage is unavailable, it will be written to a plain text file at ~/.supabase/access-token.

If this behavior is not desired, such as in a CI environment, you may skip login by specifying the SUPABASE_ACCESS_TOKEN environment variable in other commands.

The Supabase CLI uses the stored token to access Management APIs for projects, functions, secrets, etc.

Name that will be used to store token in your settings

Do not open browser automatically

Use provided token instead of automatic login flo

*[Content truncated - see full docs]*

**Examples**:

```text
1supabase bootstrap [template] [flags]
```

```text
1supabase init [flags]
```

```text
1supabase init
```

---

## CLI Reference | Supabase Docs

**URL**: https://supabase.com/docs/reference/cli/supabase-db-diff

**Contents**:
- Supabase CLI
  - Additional links#
- Global flags
  - Flags
- supabase bootstrap
  - Usage
  - Flags
- supabase init

The Supabase CLI provides tools to develop your project locally and deploy to the Supabase Platform. The CLI is still under development, but it contains all the functionality for working with your Supabase projects and the Supabase Platform.

Supabase CLI supports global flags for every command.

create a support ticket for any CLI error

output debug logs to stderr

lookup domain names using the specified resolver

enable experimental features

use the specified docker network instead of a generated one

output format of status variables

use a specific profile for connecting to Supabase API

path to a Supabase project directory

answer yes to all prompts

Password to your remote Postgres database.

Initialize configurations for Supabase local development.

A supabase/config.toml file is created in your current working directory. This configuration is specific to each local project.

You may override the directory path by specifying the SUPABASE_WORKDIR environment variable or --workdir flag.

In addition to config.toml, the supabase directory may also contain other Supabase objects, such as migrations, functions, tests, etc.

Overwrite existing supabase/config.toml.

Use OrioleDB storage engine for Postgres.

Generate IntelliJ IDEA settings for Deno.

Generate VS Code settings for Deno.

Connect the Supabase CLI to your Supabase account by logging in with your personal access token.

Your access token is stored securely in native credentials storage. If native credentials storage is unavailable, it will be written to a plain text file at ~/.supabase/access-token.

If this behavior is not desired, such as in a CI environment, you may skip login by specifying the SUPABASE_ACCESS_TOKEN environment variable in other commands.

The Supabase CLI uses the stored token to access Management APIs for projects, functions, secrets, etc.

Name that will be used to store token in your settings

Do not open browser automatically

Use provided token instead of automatic login flo

*[Content truncated - see full docs]*

**Examples**:

```text
1supabase bootstrap [template] [flags]
```

```text
1supabase init [flags]
```

```text
1supabase init
```

---

## CLI Reference | Supabase Docs

**URL**: https://supabase.com/docs/reference/cli/supabase-secrets

**Contents**:
- Supabase CLI
  - Additional links#
- Global flags
  - Flags
- supabase bootstrap
  - Usage
  - Flags
- supabase init

The Supabase CLI provides tools to develop your project locally and deploy to the Supabase Platform. The CLI is still under development, but it contains all the functionality for working with your Supabase projects and the Supabase Platform.

Supabase CLI supports global flags for every command.

create a support ticket for any CLI error

output debug logs to stderr

lookup domain names using the specified resolver

enable experimental features

use the specified docker network instead of a generated one

output format of status variables

use a specific profile for connecting to Supabase API

path to a Supabase project directory

answer yes to all prompts

Password to your remote Postgres database.

Initialize configurations for Supabase local development.

A supabase/config.toml file is created in your current working directory. This configuration is specific to each local project.

You may override the directory path by specifying the SUPABASE_WORKDIR environment variable or --workdir flag.

In addition to config.toml, the supabase directory may also contain other Supabase objects, such as migrations, functions, tests, etc.

Overwrite existing supabase/config.toml.

Use OrioleDB storage engine for Postgres.

Generate IntelliJ IDEA settings for Deno.

Generate VS Code settings for Deno.

Connect the Supabase CLI to your Supabase account by logging in with your personal access token.

Your access token is stored securely in native credentials storage. If native credentials storage is unavailable, it will be written to a plain text file at ~/.supabase/access-token.

If this behavior is not desired, such as in a CI environment, you may skip login by specifying the SUPABASE_ACCESS_TOKEN environment variable in other commands.

The Supabase CLI uses the stored token to access Management APIs for projects, functions, secrets, etc.

Name that will be used to store token in your settings

Do not open browser automatically

Use provided token instead of automatic login flo

*[Content truncated - see full docs]*

**Examples**:

```text
1supabase bootstrap [template] [flags]
```

```text
1supabase init [flags]
```

```text
1supabase init
```

---

## CLI Reference | Supabase Docs

**URL**: https://supabase.com/docs/reference/cli/supabase-gen-signing-key

**Contents**:
- Supabase CLI
  - Additional links#
- Global flags
  - Flags
- supabase bootstrap
  - Usage
  - Flags
- supabase init

The Supabase CLI provides tools to develop your project locally and deploy to the Supabase Platform. The CLI is still under development, but it contains all the functionality for working with your Supabase projects and the Supabase Platform.

Supabase CLI supports global flags for every command.

create a support ticket for any CLI error

output debug logs to stderr

lookup domain names using the specified resolver

enable experimental features

use the specified docker network instead of a generated one

output format of status variables

use a specific profile for connecting to Supabase API

path to a Supabase project directory

answer yes to all prompts

Password to your remote Postgres database.

Initialize configurations for Supabase local development.

A supabase/config.toml file is created in your current working directory. This configuration is specific to each local project.

You may override the directory path by specifying the SUPABASE_WORKDIR environment variable or --workdir flag.

In addition to config.toml, the supabase directory may also contain other Supabase objects, such as migrations, functions, tests, etc.

Overwrite existing supabase/config.toml.

Use OrioleDB storage engine for Postgres.

Generate IntelliJ IDEA settings for Deno.

Generate VS Code settings for Deno.

Connect the Supabase CLI to your Supabase account by logging in with your personal access token.

Your access token is stored securely in native credentials storage. If native credentials storage is unavailable, it will be written to a plain text file at ~/.supabase/access-token.

If this behavior is not desired, such as in a CI environment, you may skip login by specifying the SUPABASE_ACCESS_TOKEN environment variable in other commands.

The Supabase CLI uses the stored token to access Management APIs for projects, functions, secrets, etc.

Name that will be used to store token in your settings

Do not open browser automatically

Use provided token instead of automatic login flo

*[Content truncated - see full docs]*

**Examples**:

```text
1supabase bootstrap [template] [flags]
```

```text
1supabase init [flags]
```

```text
1supabase init
```

---

## CLI Reference | Supabase Docs

**URL**: https://supabase.com/docs/reference/cli/supabase-db-lint

**Contents**:
- Supabase CLI
  - Additional links#
- Global flags
  - Flags
- supabase bootstrap
  - Usage
  - Flags
- supabase init

The Supabase CLI provides tools to develop your project locally and deploy to the Supabase Platform. The CLI is still under development, but it contains all the functionality for working with your Supabase projects and the Supabase Platform.

Supabase CLI supports global flags for every command.

create a support ticket for any CLI error

output debug logs to stderr

lookup domain names using the specified resolver

enable experimental features

use the specified docker network instead of a generated one

output format of status variables

use a specific profile for connecting to Supabase API

path to a Supabase project directory

answer yes to all prompts

Password to your remote Postgres database.

Initialize configurations for Supabase local development.

A supabase/config.toml file is created in your current working directory. This configuration is specific to each local project.

You may override the directory path by specifying the SUPABASE_WORKDIR environment variable or --workdir flag.

In addition to config.toml, the supabase directory may also contain other Supabase objects, such as migrations, functions, tests, etc.

Overwrite existing supabase/config.toml.

Use OrioleDB storage engine for Postgres.

Generate IntelliJ IDEA settings for Deno.

Generate VS Code settings for Deno.

Connect the Supabase CLI to your Supabase account by logging in with your personal access token.

Your access token is stored securely in native credentials storage. If native credentials storage is unavailable, it will be written to a plain text file at ~/.supabase/access-token.

If this behavior is not desired, such as in a CI environment, you may skip login by specifying the SUPABASE_ACCESS_TOKEN environment variable in other commands.

The Supabase CLI uses the stored token to access Management APIs for projects, functions, secrets, etc.

Name that will be used to store token in your settings

Do not open browser automatically

Use provided token instead of automatic login flo

*[Content truncated - see full docs]*

**Examples**:

```text
1supabase bootstrap [template] [flags]
```

```text
1supabase init [flags]
```

```text
1supabase init
```

---

## CLI Reference | Supabase Docs

**URL**: https://supabase.com/docs/reference/cli/supabase-gen-bearer-jwt

**Contents**:
- Supabase CLI
  - Additional links#
- Global flags
  - Flags
- supabase bootstrap
  - Usage
  - Flags
- supabase init

The Supabase CLI provides tools to develop your project locally and deploy to the Supabase Platform. The CLI is still under development, but it contains all the functionality for working with your Supabase projects and the Supabase Platform.

Supabase CLI supports global flags for every command.

create a support ticket for any CLI error

output debug logs to stderr

lookup domain names using the specified resolver

enable experimental features

use the specified docker network instead of a generated one

output format of status variables

use a specific profile for connecting to Supabase API

path to a Supabase project directory

answer yes to all prompts

Password to your remote Postgres database.

Initialize configurations for Supabase local development.

A supabase/config.toml file is created in your current working directory. This configuration is specific to each local project.

You may override the directory path by specifying the SUPABASE_WORKDIR environment variable or --workdir flag.

In addition to config.toml, the supabase directory may also contain other Supabase objects, such as migrations, functions, tests, etc.

Overwrite existing supabase/config.toml.

Use OrioleDB storage engine for Postgres.

Generate IntelliJ IDEA settings for Deno.

Generate VS Code settings for Deno.

Connect the Supabase CLI to your Supabase account by logging in with your personal access token.

Your access token is stored securely in native credentials storage. If native credentials storage is unavailable, it will be written to a plain text file at ~/.supabase/access-token.

If this behavior is not desired, such as in a CI environment, you may skip login by specifying the SUPABASE_ACCESS_TOKEN environment variable in other commands.

The Supabase CLI uses the stored token to access Management APIs for projects, functions, secrets, etc.

Name that will be used to store token in your settings

Do not open browser automatically

Use provided token instead of automatic login flo

*[Content truncated - see full docs]*

**Examples**:

```text
1supabase bootstrap [template] [flags]
```

```text
1supabase init [flags]
```

```text
1supabase init
```

---

## CLI Reference | Supabase Docs

**URL**: https://supabase.com/docs/reference/cli/supabase-db-pull

**Contents**:
- Supabase CLI
  - Additional links#
- Global flags
  - Flags
- supabase bootstrap
  - Usage
  - Flags
- supabase init

The Supabase CLI provides tools to develop your project locally and deploy to the Supabase Platform. The CLI is still under development, but it contains all the functionality for working with your Supabase projects and the Supabase Platform.

Supabase CLI supports global flags for every command.

create a support ticket for any CLI error

output debug logs to stderr

lookup domain names using the specified resolver

enable experimental features

use the specified docker network instead of a generated one

output format of status variables

use a specific profile for connecting to Supabase API

path to a Supabase project directory

answer yes to all prompts

Password to your remote Postgres database.

Initialize configurations for Supabase local development.

A supabase/config.toml file is created in your current working directory. This configuration is specific to each local project.

You may override the directory path by specifying the SUPABASE_WORKDIR environment variable or --workdir flag.

In addition to config.toml, the supabase directory may also contain other Supabase objects, such as migrations, functions, tests, etc.

Overwrite existing supabase/config.toml.

Use OrioleDB storage engine for Postgres.

Generate IntelliJ IDEA settings for Deno.

Generate VS Code settings for Deno.

Connect the Supabase CLI to your Supabase account by logging in with your personal access token.

Your access token is stored securely in native credentials storage. If native credentials storage is unavailable, it will be written to a plain text file at ~/.supabase/access-token.

If this behavior is not desired, such as in a CI environment, you may skip login by specifying the SUPABASE_ACCESS_TOKEN environment variable in other commands.

The Supabase CLI uses the stored token to access Management APIs for projects, functions, secrets, etc.

Name that will be used to store token in your settings

Do not open browser automatically

Use provided token instead of automatic login flo

*[Content truncated - see full docs]*

**Examples**:

```text
1supabase bootstrap [template] [flags]
```

```text
1supabase init [flags]
```

```text
1supabase init
```

---

## CLI Reference | Supabase Docs

**URL**: https://supabase.com/docs/reference/cli/supabase-test-db

**Contents**:
- Supabase CLI
  - Additional links#
- Global flags
  - Flags
- supabase bootstrap
  - Usage
  - Flags
- supabase init

The Supabase CLI provides tools to develop your project locally and deploy to the Supabase Platform. The CLI is still under development, but it contains all the functionality for working with your Supabase projects and the Supabase Platform.

Supabase CLI supports global flags for every command.

create a support ticket for any CLI error

output debug logs to stderr

lookup domain names using the specified resolver

enable experimental features

use the specified docker network instead of a generated one

output format of status variables

use a specific profile for connecting to Supabase API

path to a Supabase project directory

answer yes to all prompts

Password to your remote Postgres database.

Initialize configurations for Supabase local development.

A supabase/config.toml file is created in your current working directory. This configuration is specific to each local project.

You may override the directory path by specifying the SUPABASE_WORKDIR environment variable or --workdir flag.

In addition to config.toml, the supabase directory may also contain other Supabase objects, such as migrations, functions, tests, etc.

Overwrite existing supabase/config.toml.

Use OrioleDB storage engine for Postgres.

Generate IntelliJ IDEA settings for Deno.

Generate VS Code settings for Deno.

Connect the Supabase CLI to your Supabase account by logging in with your personal access token.

Your access token is stored securely in native credentials storage. If native credentials storage is unavailable, it will be written to a plain text file at ~/.supabase/access-token.

If this behavior is not desired, such as in a CI environment, you may skip login by specifying the SUPABASE_ACCESS_TOKEN environment variable in other commands.

The Supabase CLI uses the stored token to access Management APIs for projects, functions, secrets, etc.

Name that will be used to store token in your settings

Do not open browser automatically

Use provided token instead of automatic login flo

*[Content truncated - see full docs]*

**Examples**:

```text
1supabase bootstrap [template] [flags]
```

```text
1supabase init [flags]
```

```text
1supabase init
```

---

## C#: Introduction | Supabase Docs

**URL**: https://supabase.com/docs/reference/csharp/introduction

---

## Compute and Disk | Supabase Docs

**URL**: https://supabase.com/docs/guides/platform/compute-add-ons

**Contents**:
- Compute and Disk
- Compute#
      - Nano instances in paid plan organizations
  - Dedicated vs shared CPU#
  - Compute upgrades #
- Disk#
  - Compute size#
  - Choosing the right compute instance for consistent disk performance#

Every project on the Supabase Platform comes with its own dedicated Postgres instance.

The following table describes the base instances, Nano (free plan) and Micro (paid plans), with additional compute instance sizes available if you need extra performance when scaling up.

In paid organizations, Nano Compute are billed at the same price as Micro Compute. It is recommended to upgrade your Project from Nano Compute to Micro Compute when it's convenient for you. Compute sizes are not auto-upgraded because of the downtime incurred. See Supabase Pricing for more information. You cannot launch Nano instances on paid plans, only Micro and above - but you might have Nano instances after upgrading from Free Plan.

Compute sizes can be changed by first selecting your project in the dashboard here and the upgrade process will incur downtime.

We charge hourly for additional compute based on your usage. Read more about usage-based billing for compute.

All Postgres databases on Supabase run in isolated environments. Compute instances smaller than Large compute size have CPUs which can burst to higher performance levels for short periods of time. Instances bigger than Large have predictable performance levels and do not exhibit the same burst behavior.

Compute instance changes are usually applied with less than 2 minutes of downtime, but can take longer depending on the underlying Cloud Provider.

When considering compute upgrades, assess whether your bottlenecks are hardware-constrained or software-constrained. For example, you may want to look into optimizing the number of connections or examining query performance. When you're happy with your Postgres instance's performance, then you can focus on additional compute resources. For example, you can load test your application in staging to understand your compute requirements. You can also start out on a smaller tier, create a report in the Dashboard to monitor your CPU utilization, and upgrade as needed.

Supabase databases 

*[Content truncated - see full docs]*

---

## Flutter: Introduction | Supabase Docs

**URL**: https://supabase.com/docs/reference/dart/introduction

---

## Generate image captions using Hugging Face | Supabase Docs

**URL**: https://supabase.com/docs/guides/ai/examples/huggingface-image-captioning

**Contents**:
- Generate image captions using Hugging Face
- Use the Hugging Face Inference API to make calls to 100,000+ Machine Learning models from Supabase Edge Functions.
- About Hugging Face#
- Setup#
- Generate TypeScript types#
- Code#
  - Is this helpful?

Generate image captions using Hugging Face

Use the Hugging Face Inference API to make calls to 100,000+ Machine Learning models from Supabase Edge Functions.

We can combine Hugging Face with Supabase Storage and Database Webhooks to automatically caption for any image we upload to a storage bucket.

Hugging Face is the collaboration platform for the machine learning community.

Huggingface.js provides a convenient way to make calls to 100,000+ Machine Learning models, making it easy to incorporate AI functionality into your Supabase Edge Functions.

To generate the types.ts file for the storage and public schemas, run the following command in the terminal:

Find the complete code on GitHub.

Latest product updates?

Something's not right?

**Examples**:

```javascript
1supabase gen types typescript --project-id=your-project-ref --schema=storage,public > supabase/functions/huggingface-image-captioning/types.ts
```

```python
12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849import { serve } from 'https://deno.land/std@0.168.0/http/server.ts'import { HfInference } from 'https://esm.sh/@huggingface/inference@2.3.2'import { createClient } from 'npm:@supabase/supabase-js@2'import { Database } from './types.ts'console.log('Hello from `huggingface-image-captioning` function!')const hf = new HfInference(Deno.env.get('HUGGINGFACE_ACCESS_TOKEN'))type SoRecord = Database['storage']['Tabl
...
```

---

## Generating OpenAI GPT3 completions | Supabase Docs

**URL**: https://supabase.com/docs/guides/ai/examples/openai

**Contents**:
- Generating OpenAI GPT3 completions
- Generate GPT text completions using OpenAI and Supabase Edge Functions.
- Setup Supabase project#
- Create edge function#
- Create OpenAI key#
- Run locally#
- Deploy#
- Go deeper#

Generating OpenAI GPT3 completions

Generate GPT text completions using OpenAI and Supabase Edge Functions.

OpenAI provides a completions API that allows you to use their generative GPT models in your own applications.

OpenAI's API is intended to be used from the server-side. Supabase offers Edge Functions to make it easy to interact with third party APIs like OpenAI.

If you haven't already, install the Supabase CLI and initialize your project:

Scaffold a new edge function called openai by running:

A new edge function will now exist under ./supabase/functions/openai/index.ts.

We'll design the function to take your user's query (via POST request) and forward it to OpenAI's API.

Note that we are setting stream to false which will wait until the entire response is complete before returning. If you wish to stream GPT's response word-by-word back to your client, set stream to true.

You may have noticed we were passing OPENAI_API_KEY in the Authorization header to OpenAI. To generate this key, go to https://platform.openai.com/account/api-keys and create a new secret key.

After getting the key, copy it into a new file called .env.local in your ./supabase folder:

Serve the edge function locally by running:

Notice how we are passing in the .env.local file.

Use cURL or Postman to make a POST request to http://localhost:54321/functions/v1/openai.

You should see a GPT response come back from OpenAI!

Deploy your function to the cloud by running:

If you're interesting in learning how to use this to build your own ChatGPT, read the blog post and check out the video:

Latest product updates?

Something's not right?

**Examples**:

```text
1supabase init
```

```javascript
1supabase functions new openai
```

```python
1234567891011121314151617181920212223import OpenAI from 'https://deno.land/x/openai@v4.24.0/mod.ts'Deno.serve(async (req) => {  const { query } = await req.json()  const apiKey = Deno.env.get('OPENAI_API_KEY')  const openai = new OpenAI({    apiKey: apiKey,  })  // Documentation here: https://github.com/openai/openai-node  const chatCompletion = await openai.chat.completions.create({    messages: [{ role: 'user', content: query }],    // Choose model from here: https://platform.openai.com/docs/m
...
```

---

## Getting Started | Supabase Docs

**URL**: https://supabase.com/docs/guides/resources/examples

**Contents**:
- Getting Started
  - Use cases#
  - Framework quickstarts#
  - Web app demos#
  - Mobile tutorials#

AI, Vectors, and embeddings

Subscription Payments (SaaS)

Expo React Native Social Auth

Latest product updates?

Something's not right?

---

## Hugging Face Inference API | Supabase Docs

**URL**: https://supabase.com/docs/guides/ai/hugging-face

**Contents**:
- Hugging Face Inference API
- AI tasks#
  - Natural language#
  - Computer vision#
  - Audio#
- Access token#
- Edge Functions#
- Next steps#

Hugging Face Inference API

Hugging Face is an open source hub for AI/ML models and tools. With over 100,000 machine learning models available, Hugging Face provides a great way to integrate specialized AI & ML tasks into your application.

There are 3 ways to use Hugging Face models in your application:

Below are some of the types of tasks you can perform with Hugging Face:

See a full list of tasks.

First generate a Hugging Face access token for your app:

https://huggingface.co/settings/tokens

Name your token based on the app its being used for and the environment. For example, if you are building an image generation app you might create 2 tokens:

Since we will be using this token for the inference API, choose the read role.

Though it is possible to use the Hugging Face inference API today without an access token, you may be rate limited.

To ensure you don't experience any unexpected downtime or errors, we recommend creating an access token.

Edge Functions are server-side TypeScript functions that run on-demand. Since Edge Functions run on a server, you can safely give them access to your Hugging Face access token.

You will need the supabase CLI installed for the following commands to work.

To create a new Edge Function, navigate to your local project and initialize Supabase if you haven't already:

Then create an Edge Function:

Create a file called .env.local to store your Hugging Face access token:

Let's modify the Edge Function to import Hugging Face's inference client and perform a text-to-image request:

This function creates a new instance of HfInference using the HUGGING_FACE_ACCESS_TOKEN environment variable.

It expects a POST request that includes a JSON request body. The JSON body should include a parameter called prompt that represents the text-to-image prompt that we will pass to Hugging Face's inference API.

Next we call textToImage(), passing in the user's prompt along with the model that we would like to use for the image generation. T

*[Content truncated - see full docs]*

**Examples**:

```text
1supabase init
```

```javascript
1supabase functions new text-to-image
```

```text
1HUGGING_FACE_ACCESS_TOKEN=<your-token-here>
```

---

## Hybrid search | Supabase Docs

**URL**: https://supabase.com/docs/guides/ai/hybrid-search

**Contents**:
- Hybrid search
- Combine keyword search with semantic search.
- Use cases for hybrid search#
- When to consider hybrid search#
- How to combine search methods#
- Reciprocal Ranked Fusion (RRF)#
  - Smoothing constant k#
- Hybrid search in Postgres#

Combine keyword search with semantic search.

Hybrid search combines full text search (searching by keyword) with semantic search (searching by meaning) to identify results that are both directly and contextually relevant to the user's query.

Sometimes a single search method doesn't quite capture what a user is really looking for. For example, if a user searches for "Italian recipes with tomato sauce" on a cooking app, a keyword search would pull up recipes that specifically mention "Italian," "recipes," and "tomato sauce" in the text. However, it might miss out on dishes that are quintessentially Italian and use tomato sauce but don't explicitly label themselves with these words, or use variations like "pasta sauce" or "marinara." On the other hand, a semantic search might understand the culinary context and find recipes that match the intent, such as a traditional "Spaghetti Marinara," even if they don't match the exact keyword phrase. However, it could also suggest recipes that are contextually related but not what the user is looking for, like a "Mexican salsa" recipe, because it understands the context to be broadly about tomato-based sauces.

Hybrid search combines the strengths of both these methods. It would ensure that recipes explicitly mentioning the keywords are prioritized, thus capturing direct hits that satisfy the keyword criteria. At the same time, it would include recipes identified through semantic understanding as being related in meaning or context, like different Italian dishes that traditionally use tomato sauce but might not have been tagged explicitly with the user's search terms. It identifies results that are both directly and contextually relevant to the user's query while ideally minimizing misses and irrelevant suggestions.

The decision to use hybrid search depends on what your users are looking for in your app. For a code repository where developers need to find exact lines of code or error messages, keyword search is likely ideal be

*[Content truncated - see full docs]*

**Examples**:

```text
123456create table documents (  id bigint primary key generated always as identity,  content text,  fts tsvector generated always as (to_tsvector('english', content)) stored,  embedding vector(512));
```

```text
12345-- Create an index for the full-text searchcreate index on documents using gin(fts);-- Create an index for the semantic vector searchcreate index on documents using hnsw (embedding vector_ip_ops);
```

```javascript
123456789101112131415161718192021222324252627282930313233343536373839404142434445464748create or replace function hybrid_search(  query_text text,  query_embedding vector(512),  match_count int,  full_text_weight float = 1,  semantic_weight float = 1,  rrf_k int = 50)returns setof documentslanguage sqlas $$with full_text as (  select    id,    -- Note: ts_rank_cd is not indexable but will only rank matches of the where clause    -- which shouldn't be too big    row_number() over(order by ts_rank
...
```

---

## Image Search with OpenAI CLIP | Supabase Docs

**URL**: https://supabase.com/docs/guides/ai/examples/image-search-openai-clip

**Contents**:
- Image Search with OpenAI CLIP
- Implement image search with the OpenAI CLIP Model and Supabase Vector.
- Create a new Python project with Poetry#
- Setup Supabase project#
- Install the dependencies#
- Import the necessary dependencies#
- Create embeddings for your images#
- Perform an image search from a text query#

Image Search with OpenAI CLIP

Implement image search with the OpenAI CLIP Model and Supabase Vector.

The OpenAI CLIP Model was trained on a variety of (image, text)-pairs. You can use the CLIP model for:

SentenceTransformers provides models that allow you to embed images and text into the same vector space. You can use this to find similar images as well as to implement image search.

You can find the full application code as a Python Poetry project on GitHub.

Poetry provides packaging and dependency management for Python. If you haven't already, install poetry via pip:

Then initialize a new project:

If you haven't already, install the Supabase CLI, then initialize Supabase in the root of your newly created poetry project:

Next, start your local Supabase stack:

This will start up the Supabase stack locally and print out a bunch of environment details, including your local DB URL. Make a note of that for later user.

We will need to add the following dependencies to our project:

At the top of your main python script, import the dependencies and store your DB URL from above in a variable:

In the root of your project, create a new folder called images and add some images. You can use the images from the example project on GitHub or you can find license free images on Unsplash.

Next, create a seed method, which will create a new Supabase Vector Collection, generate embeddings for your images, and upsert the embeddings into your database:

Add this method as a script in your pyproject.toml file:

After activating the virtual environment with poetry shell you can now run your seed script via poetry run seed. You can inspect the generated embeddings in your local database by visiting the local Supabase dashboard at localhost:54323, selecting the vecs schema, and the image_vectors database.

With Supabase Vector we can query our embeddings. We can use either an image as search input or alternative we can generate an embedding from a string input and use that as t

*[Content truncated - see full docs]*

**Examples**:

```text
1pip install poetry
```

```text
1poetry new image-search
```

```text
1supabase init
```

---

## Integrations | Supabase Docs

**URL**: https://supabase.com/docs/guides/integrations

**Contents**:
- Integrations
- Vercel Marketplace#
- Supabase Marketplace#
  - Is this helpful?

Supabase integrates with many of your favorite third-party services.

Create and manage your Supabase projects directly through Vercel. Get started with Vercel.

Browse tools for extending your Supabase project. Browse the Supabase Marketplace.

Latest product updates?

Something's not right?

---

## JavaScript: Initializing | Supabase Docs

**URL**: https://supabase.com/docs/reference/javascript/initializing

---

## JavaScript: Introduction | Supabase Docs

**URL**: https://supabase.com/docs/reference/javascript/introduction

---

## Keyword search | Supabase Docs

**URL**: https://supabase.com/docs/guides/ai/keyword-search

**Contents**:
- Keyword search
- Learn how to search by words or phrases.
- When and why to use keyword search#
- Using full-text search#
- See also#
  - Is this helpful?

Learn how to search by words or phrases.

Keyword search involves locating documents or records that contain specific words or phrases, primarily based on the exact match between the search terms and the text within the data. It differs from semantic search, which interprets the meaning behind the query to provide results that are contextually related, even if the exact words aren't present in the text. Semantic search considers synonyms, intent, and natural language nuances to provide a more nuanced approach to information retrieval.

In Postgres, keyword search is implemented using full-text search. It supports indexing and text analysis for data retrieval, focusing on records that match the search criteria. Postgres' full-text search extends beyond simple keyword matching to address linguistic nuances, making it effective for applications that require precise text queries.

Keyword search is particularly useful in scenarios where precision and specificity matter. It's more effective than semantic search when users are looking for information using exact terminology or specific identifiers. It ensures that results directly contain those terms, reducing the chance of retrieving irrelevant information that might be semantically related but not what the user seeks.

For example in technical or academic research databases, researchers often search for specific studies, compounds, or concepts identified by certain terms or codes. Searching for a specific chemical compound using its exact molecular formula or a unique identifier will yield more focused and relevant results compared to a semantic search, which could return a wide range of documents discussing the compound in different contexts. Keyword search ensures documents that explicitly mention the exact term are found, allowing users to access the precise data they need efficiently.

It's also possible to combine keyword search with semantic search to get the best of both worlds. See Hybrid search for more details

*[Content truncated - see full docs]*

---

## Kotlin: Introduction | Supabase Docs

**URL**: https://supabase.com/docs/reference/kotlin/introduction

---

## Local Development & CLI | Supabase Docs

**URL**: https://supabase.com/docs/guides/cli

**Contents**:
- Local Development & CLI
- Learn how to develop locally and use the Supabase CLI
- Quickstart#
- Local development#
- CLI#
  - Is this helpful?

Local Development & CLI

Learn how to develop locally and use the Supabase CLI

Develop locally while running the Supabase stack on your machine.

As a prerequisite, you must install a container runtime compatible with Docker APIs.

Install the Supabase CLI:

In your repo, initialize the Supabase project:

Start the Supabase stack:

View your local Supabase instance at http://localhost:54323.

Local development with Supabase allows you to work on your projects in a self-contained environment on your local machine. Working locally has several advantages:

To get started with local development, you'll need to install the Supabase CLI and Docker. The Supabase CLI allows you to start and manage your local Supabase stack, while Docker is used to run the necessary services.

Once set up, you can initialize a new Supabase project, start the local stack, and begin developing your application using local Supabase services. This includes access to a local Postgres database, Auth, Storage, and other Supabase features.

The Supabase CLI is a powerful tool that enables developers to manage their Supabase projects directly from the terminal. It provides a suite of commands for various tasks, including:

With the CLI, you can streamline your development workflow, automate repetitive tasks, and maintain consistency across different environments. It's an essential tool for both local development and CI/CD pipelines.

See the CLI Getting Started guide for more information.

Latest product updates?

Something's not right?

**Examples**:

```text
1npm install supabase --save-dev
```

```text
1npx supabase init
```

```text
1npx supabase start
```

---

## Manage Monthly Active SSO Users usage | Supabase Docs

**URL**: https://supabase.com/docs/guides/platform/manage-your-usage/monthly-active-users-sso

**Contents**:
- Manage Monthly Active SSO Users usage
- What you are charged for#
  - Example#
  - Sign User-1 in on January 3
  - Sign User-1 out on January 4
  - Sign User-1 in again on January 17
- How charges are calculated#
  - Usage on your invoice#

Manage Monthly Active SSO Users usage

You are charged for the number of distinct users who log in or refresh their token during the billing cycle using a SAML 2.0 compatible identity provider (e.g. Google Workspace, Microsoft Active Directory). Each unique user is counted only once per billing cycle, regardless of how many times they authenticate. These users are referred to as "SSO MAUs".

Your billing cycle runs from January 1 to January 31. Although User-1 was signed in multiple times, they are counted as a single SSO MAU for this billing cycle.

The SSO MAU count increases from 0 to 1.

The SSO MAU count remains 1.

You are charged by SSO MAU.

Usage is shown as "Monthly Active SSO Users" on your invoice.

$0.015 per SSO MAU. You are only charged for usage exceeding your subscription plan's quota.

For a detailed breakdown of how charges are calculated, refer to Manage Monthly Active SSO Users usage.

The count resets at the start of each billing cycle.

The organization's SSO MAU usage for the billing cycle is within the quota, so no charges apply.

The organization's SSO MAU usage for the billing cycle exceeds the quota by 10, incurring charges for this additional usage.

You can view Monthly Active SSO Users usage on the organization's usage page. The page shows the usage of all projects by default. To view the usage for a specific project, select it from the dropdown. You can also select a different time period.

In the Monthly Active SSO Users section, you can see the usage for the selected time period.

Latest product updates?

Something's not right?

**Examples**:

```javascript
12345678const { data, error } = await supabase.auth.signInWithSSO({domain: 'company.com'})if (data?.url) {// redirect User-1 to the identity provider's authentication flowwindow.location.href = data.url}
```

```javascript
1const { error } = await supabase.auth.signOut()
```

```javascript
12345678const { data, error } = await supabase.auth.signInWithSSO({domain: 'company.com'})if (data?.url) {// redirect User-1 to the identity provider's authentication flowwindow.location.href = data.url}
```

---

## Manage Monthly Active Users usage | Supabase Docs

**URL**: https://supabase.com/docs/guides/platform/manage-your-usage/monthly-active-users

**Contents**:
- Manage Monthly Active Users usage
- What you are charged for#
  - Example#
  - Sign User-1 in on January 3
  - Sign User-1 out on January 4
  - Sign User-1 in again on January 17
- How charges are calculated#
  - Usage on your invoice#

Manage Monthly Active Users usage

You are charged for the number of distinct users who log in or refresh their token during the billing cycle (including Social Login with e.g. Google, Facebook, GitHub). Each unique user is counted only once per billing cycle, regardless of how many times they authenticate. These users are referred to as "MAUs".

Your billing cycle runs from January 1 to January 31. Although User-1 was signed in multiple times, they are counted as a single MAU for this billing cycle.

The MAU count increases from 0 to 1.

javascript const {error} = await supabase.auth.signOut()

The MAU count remains 1.

You are charged by MAU.

Usage is shown as "Monthly Active Users" on your invoice.

$0.00325 per MAU. You are only charged for usage exceeding your subscription plan's quota.

The count resets at the start of each billing cycle.

The organization's MAU usage for the billing cycle is within the quota, so no charges apply.

The organization's MAU usage for the billing cycle exceeds the quota by 60,000, incurring charges for this additional usage.

You can view Monthly Active Users usage on the organization's usage page. The page shows the usage of all projects by default. To view the usage for a specific project, select it from the dropdown. You can also select a different time period.

In the Monthly Active Users section, you can see the usage for the selected time period.

Latest product updates?

Something's not right?

**Examples**:

```javascript
1234const {data, error} = await supabase.auth.signInWithPassword({email: 'user-1@email.com',password: 'example-password-1',})
```

```javascript
1234const {data, error} = await supabase.auth.signInWithPassword({email: 'user-1@email.com',password: 'example-password-1',})
```

---

## Management API Reference | Supabase Docs

**URL**: https://supabase.com/docs/reference/api/introduction

**Contents**:
- Management API
- Authentication#
- Rate limits#
- Gets project performance advisors.deprecated
  - Path parameters
  - Response codes
  - Response (200)
- Gets project security advisors.deprecated

Manage your Supabase organizations and projects programmatically.

All API requests require an access token to be included in the Authorization header: Authorization Bearer <access_token>.

There are two ways to generate an access token:

Personal access token (PAT): PATs are long-lived tokens that you manually generate to access the Management API. They are useful for automating workflows or developing against the Management API. PATs carry the same privileges as your user account, so be sure to keep it secret.

To generate or manage your personal access tokens, visit your account page.

OAuth2: OAuth2 allows your application to generate tokens on behalf of a Supabase user, providing secure and limited access to their account without requiring their credentials. Use this if you're building a third-party app that needs to create or manage Supabase projects on behalf of your users. Tokens generated via OAuth2 are short-lived and tied to specific scopes to ensure your app can only perform actions that are explicitly approved by the user.

See Build a Supabase Integration to set up OAuth2 for your application.

All API requests must be authenticated and made over HTTPS.

The rate limit for Management API is 60 requests per one minute per user, and applies cumulatively across all requests made with your personal access tokens.

If you exceed this limit, all Management API calls for the next minute will be blocked, resulting in a HTTP 429 response.

The Management API is subject to our fair-use policy. All resources created via the API are subject to the pricing detailed on our Pricing pages.

This is an experimental endpoint. It is subject to change or removal in future versions. Use it with caution, as it may not remain supported or stable.

This is an experimental endpoint. It is subject to change or removal in future versions. Use it with caution, as it may not remain supported or stable.

Executes a SQL query on the project's logs.

Either the 'iso_timestamp_start' 

*[Content truncated - see full docs]*

**Examples**:

```text
12curl https://api.supabase.com/v1/projects \  -H "Authorization: Bearer sbp_bdd0••••••••••••••••••••••••••••••••4f23"
```

```text
123456789101112131415161718192021222324252627{  "lints": [    {      "name": "unindexed_foreign_keys",      "title": "lorem",      "level": "ERROR",      "facing": "EXTERNAL",      "categories": [        "PERFORMANCE"      ],      "description": "lorem",      "detail": "lorem",      "remediation": "lorem",      "metadata": {        "schema": "lorem",        "name": "lorem",        "entity": "lorem",        "type": "table",        "fkey_name": "lorem",        "fkey_columns": [          42        
...
```

```text
123456789101112131415161718192021222324252627{  "lints": [    {      "name": "unindexed_foreign_keys",      "title": "lorem",      "level": "ERROR",      "facing": "EXTERNAL",      "categories": [        "PERFORMANCE"      ],      "description": "lorem",      "detail": "lorem",      "remediation": "lorem",      "metadata": {        "schema": "lorem",        "name": "lorem",        "entity": "lorem",        "type": "table",        "fkey_name": "lorem",        "fkey_columns": [          42        
...
```

---

## Python: Introduction | Supabase Docs

**URL**: https://supabase.com/docs/reference/python/introduction

---

## Resources | Supabase Docs

**URL**: https://supabase.com/docs/guides/resources

**Contents**:
- Resources
  - Migrate to Supabase#
      - Auth0
      - Firebase Auth
      - Firestore Data
      - Firebase Storage
      - Heroku
      - Render

Drop all tables in schema

Select first row per group

Print PostgreSQL version

Latest product updates?

Something's not right?

---

## Self-Hosting | Supabase Docs

**URL**: https://supabase.com/docs/reference/self-hosting-analytics/introduction

**Contents**:
- Self-Hosting Analytics
      - Logflare Technical Docs
- Backends Supported#
- Getting Started#
- Postgres Backend Setup#
  - Configuration and Requirements#
- BigQuery Backend Setup#
  - Configuration and Requirements#

The Supabase Analytics server is a Logflare self-hostable instance that manages the ingestion and query pipelines for searching and aggregating structured analytics events.

When self-hosting the Analytics server, the full logging experience matching that of the Supabase Platform is available in the Studio instance, allowing for an integrated and enhanced development experience. However, it's important to note that certain differences may arise due to the platform's infrastructure.

All Logflare technical documentation is available at https://docs.logflare.app.

The Analytics server supports either Postgres or BigQuery as the backend. The supabase-cli experience uses the Postgres backend out-of-the-box. However, the Supabase Platform uses the BigQuery backend for storing all platform logs.

When using the BigQuery backend, a BigQuery dataset is created in the provided Google Cloud project, and tables are created for each source. Log events are streamed into each table, and all queries generated by Studio or by the Logs Explorer are executed against the BigQuery API. This backend requires internet access to work, and cannot be run fully locally.

When using the Postgres backend, tables are created for each source within the provided schema (for supabase-cli, this would be _analytics). Log events received by Logflare are inserted directly into the respective tables. All BigQuery-dialect SQL queries from Studio will be handled by a translation layer within the Analytics server. This translation layer translates the query to PostgreSQL dialect, and then executes it against the Postgres database.

The Postgres backend is not yet optimized for a high volume of inserts, or for heavy query usage. Today the translation layer only handles a limited subset of the BigQuery dialect. As such, the Log Explorer may produce errors for more advanced queries when using the Postgres Backend.

The Postgres backend is recommended when familiarizing and experimenting with self-hosting Sup

*[Content truncated - see full docs]*

**Examples**:

```text
123# clone the supabase/supabase repo, and run the followingcd dockerdocker compose -f docker-compose.yml up
```

```text
123# assuming you clone the supabase/supabase repo.cd dockerdocker compose -f docker-compose.yml
```

```text
123456789101112131415[  {    "cache_duration_seconds": 42,    "enable_auth": true,    "inserted_at": "2021-12-31T23:34:00Z",    "max_limit": 42,    "name": "lorem",    "proactive_requerying_seconds": 42,    "query": "lorem",    "sandboxable": true,    "source_mapping": {},    "token": "lorem",    "updated_at": "2021-12-31T23:34:00Z"  }]
```

---

## Self-Hosting | Supabase Docs

**URL**: https://supabase.com/docs/guides/self-hosting

**Contents**:
- Self-Hosting
- Host Supabase on your own infrastructure.
- Officially supported#
- Community supported#
- Third-party guides#

Host Supabase on your own infrastructure.

There are several ways to host Supabase on your own computer, server, or cloud.

Deploy Supabase within your own infrastructure using Docker Compose.

Supabase is also a hosted platform. If you want to get started for free, visit supabase.com/dashboard.

There are several community-driven projects to help you deploy Supabase. We encourage you to try them out and contribute back to the community.

The following third-party providers have shown consistent support for the self-hosted version of Supabase:.

Latest product updates?

Something's not right?

---

## Semantic search | Supabase Docs

**URL**: https://supabase.com/docs/guides/ai/semantic-search

**Contents**:
- Semantic search
- Learn how to search by meaning rather than exact keywords.
- When to use semantic search#
- How semantic search works#
- Embedding models#
- Semantic search in Postgres#
  - Similarity metric#
  - Calling from your application#

Learn how to search by meaning rather than exact keywords.

Semantic search interprets the meaning behind user queries rather than exact keywords. It uses machine learning to capture the intent and context behind the query, handling language nuances like synonyms, phrasing variations, and word relationships.

Semantic search is useful in applications where the depth of understanding and context is important for delivering relevant results. A good example is in customer support or knowledge base search engines. Users often phrase their problems or questions in various ways, and a traditional keyword-based search might not always retrieve the most helpful documents. With semantic search, the system can understand the meaning behind the queries and match them with relevant solutions or articles, even if the exact wording differs.

For instance, a user searching for "increase text size on display" might miss articles titled "How to adjust font size in settings" in a keyword-based search system. However, a semantic search engine would understand the intent behind the query and correctly match it to relevant articles, regardless of the specific terminology used.

It's also possible to combine semantic search with keyword search to get the best of both worlds. See Hybrid search for more details.

Semantic search uses an intermediate representation called an “embedding vector” to link database records with search queries. A vector, in the context of semantic search, is a list of numerical values. They represent various features of the text and allow for the semantic comparison between different pieces of text.

The best way to think of embeddings is by plotting them on a graph, where each embedding is a single point whose coordinates are the numerical values within its vector. Importantly, embeddings are plotted such that similar concepts are positioned close together while dissimilar concepts are far apart. For more details, see What are embeddings?

Embeddings are generat

*[Content truncated - see full docs]*

**Examples**:

```text
123create extension vectorwith  schema extensions;
```

```text
12345create table documents (  id bigint primary key generated always as identity,  content text,  embedding vector(512));
```

```text
12alter table documentsadd column embedding vector(512);
```

---

## Supabase Docs

**URL**: https://supabase.com/docs

**Contents**:
- Supabase Documentation
- Getting Started
- Products
- Postgres Modules
      - AI & Vectors
      - Cron
      - Queues
- Client Libraries

Learn how to get up and running with Supabase through tutorials, APIs and platform resources.

Set up and connect a database in just a few minutes.

Bring your existing data, auth and storage to Supabase following our migration guides.

Get started with self-hosting Supabase.

Latest product updates?

Something's not right?

---

## Supabase Platform | Supabase Docs

**URL**: https://supabase.com/docs/guides/platform

**Contents**:
- Supabase Platform
- Projects#
- Organizations#
- Platform status#
  - Is this helpful?

Supabase is a hosted platform which makes it very simple to get started without needing to manage any infrastructure.

Visit supabase.com/dashboard and sign in to start creating projects.

Each project on Supabase comes with:

Organizations are a way to group your projects. Each organization can be configured with different team members and billing settings. Refer to access control for more information on how to manage team members within an organization.

If Supabase experiences outages, we keep you as informed as possible, as early as possible. We provide the following feedback channels:

Make sure to review our SLA for details on our commitment to Platform Stability.

Latest product updates?

Something's not right?

---

## Swift: Introduction | Supabase Docs

**URL**: https://supabase.com/docs/reference/swift/introduction

---

## Vector columns | Supabase Docs

**URL**: https://supabase.com/docs/guides/ai/vector-columns

**Contents**:
- Vector columns
- Usage#
  - Enable the extension#
  - Create a table to store vectors#
  - Storing a vector / embedding#
  - Querying a vector / embedding#
  - Indexes#
  - Is this helpful?

Supabase offers a number of different ways to store and query vectors within Postgres. The SQL included in this guide is applicable for clients in all programming languages. If you are a Python user see your Python client options after reading the Learn section.

Vectors in Supabase are enabled via pgvector, a Postgres extension for storing and querying vectors in Postgres. It can be used to store embeddings.

After enabling the vector extension, you will get access to a new data type called vector. The size of the vector (indicated in parenthesis) represents the number of dimensions stored in that vector.

In the above SQL snippet, we create a documents table with a column called embedding (note this is just a regular Postgres column - you can name it whatever you like). We give the embedding column a vector data type with 384 dimensions. Change this to the number of dimensions produced by your embedding model. For example, if you are generating embeddings using the open source gte-small model, you would set this number to 384 since that model produces 384 dimensions.

In general, embeddings with fewer dimensions perform best. See our analysis on fewer dimensions in pgvector.

In this example we'll generate a vector using Transformers.js, then store it in the database using the Supabase JavaScript client.

This example uses the JavaScript Supabase client, but you can modify it to work with any supported language library.

Similarity search is the most common use case for vectors. pgvector support 3 new operators for computing distance:

Choosing the right operator depends on your needs. Dot product tends to be the fastest if your vectors are normalized. For more information on how embeddings work and how they relate to each other, see What are Embeddings?.

Supabase client libraries like supabase-js connect to your Postgres instance via PostgREST. PostgREST does not currently support pgvector similarity operators, so we'll need to wrap our query in a Postgres funct

*[Content truncated - see full docs]*

**Examples**:

```text
123456create table documents (  id serial primary key,  title text not null,  body text not null,  embedding vector(384));
```

```python
123456789101112131415161718192021import { pipeline } from '@xenova/transformers'const generateEmbedding = await pipeline('feature-extraction', 'Supabase/gte-small')const title = 'First post!'const body = 'Hello world!'// Generate a vector using Transformers.jsconst output = await generateEmbedding(body, {  pooling: 'mean',  normalize: true,})// Extract the embedding outputconst embedding = Array.from(output.data)// Store the vector in Postgresconst { data, error } = await supabase.from('document
...
```

```javascript
1234567891011121314151617181920212223create or replace function match_documents (  query_embedding vector(384),  match_threshold float,  match_count int)returns table (  id bigint,  title text,  body text,  similarity float)language sql stableas $$  select    documents.id,    documents.title,    documents.body,    1 - (documents.embedding <=> query_embedding) as similarity  from documents  where 1 - (documents.embedding <=> query_embedding) > match_threshold  order by (documents.embedding <=> qu
...
```

---

## Vector search with Next.js and OpenAI | Supabase Docs

**URL**: https://supabase.com/docs/guides/ai/examples/nextjs-vector-search

**Contents**:
- Vector search with Next.js and OpenAI
- Learn how to build a ChatGPT-style doc search powered by Next.js, OpenAI, and Supabase.
- Create a project#
- Prepare the database#
- Pre-process the knowledge base at build time#
  - Generate Embeddings
  - Set up environment variables
  - Run script at build time

Vector search with Next.js and OpenAI

Learn how to build a ChatGPT-style doc search powered by Next.js, OpenAI, and Supabase.

While our Headless Vector search provides a toolkit for generative Q&A, in this tutorial we'll go more in-depth, build a custom ChatGPT-like search experience from the ground-up using Next.js. You will:

You can read our Supabase Clippy blog post for a full example.

We assume that you have a Next.js project with a collection of .mdx files nested inside your pages directory. We will start developing locally with the Supabase CLI and then push our local database changes to our hosted Supabase project. You can find the full Next.js example on GitHub.

Let's prepare the database schema. We can use the "OpenAI Vector Search" quickstart in the SQL Editor, or you can copy/paste the SQL below and run it yourself.

With our database set up, we need to process and store all .mdx files in the pages directory. You can find the full script here, or follow the steps below:

Create a new file lib/generate-embeddings.ts and copy the code over from GitHub.

We need some environment variables to run the script. Add them to your .env file and make sure your .env file is not committed to source control! You can get your local Supabase credentials by running supabase status.

Include the script in your package.json script commands to enable Vercel to automatically run it at build time.

Anytime a user asks a question, we need to create an embedding for their question, perform a similarity search, and then send a text completion request to the OpenAI API with the query and then context content merged together into a prompt.

All of this is glued together in a Vercel Edge Function, the code for which can be found on GitHub.

In order to perform similarity search we need to turn the question into an embedding.

Using the embeddingResponse we can now perform similarity search by performing an remote procedure call (RPC) to the database function we created earlier.

*[Content truncated - see full docs]*

**Examples**:

```text
123curl \https://raw.githubusercontent.com/supabase-community/nextjs-openai-doc-search/main/lib/generate-embeddings.ts \-o "lib/generate-embeddings.ts"
```

```text
123456NEXT_PUBLIC_SUPABASE_URL=NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY=SUPABASE_SERVICE_ROLE_KEY=# Get your key at https://platform.openai.com/account/api-keysOPENAI_API_KEY=
```

```typescript
123456"scripts": {  "dev": "next dev",  "build": "pnpm run embeddings && next build",  "start": "next start",  "embeddings": "tsx lib/generate-embeddings.ts"},
```

---
