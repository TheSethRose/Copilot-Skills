# Vercel - Other

**Pages**: 63

---

## AI Gateway

**URL**: https://vercel.com/docs/ai-gateway

**Contents**:
- AI Gateway
- Key features
- More resources

AI Gateway is available on all plans and your use is subject to AI Product Terms.

The AI Gateway provides a unified API to access hundreds of models through a single endpoint. It gives you the ability to set budgets, monitor usage, load-balance requests, and manage fallbacks.

The design allows it to work seamlessly with AI SDK 5, OpenAI SDK, or your preferred framework.

**Examples**:

```python
import { generateText } from 'ai';
 
const { text } = generateText({
  model: 'anthropic/claude-sonnet-4',
  prompt: 'What is the capital of France?',
});
```

```python
import os
from openai import OpenAI
 
client = OpenAI(
  api_key=os.getenv('AI_GATEWAY_API_KEY'),
  base_url='https://ai-gateway.vercel.sh/v1'
)
 
response = client.chat.completions.create(
  model='xai/grok-4',
  messages=[
    {
      'role': 'user',
      'content': 'Why is the sky blue?'
    }
  ]
)
```

```text
curl -X POST "https://ai-gateway.vercel.sh/v1/chat/completions" \
-H "Authorization: Bearer $AI_GATEWAY_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "model": "openai/gpt-5",
  "messages": [
    {
      "role": "user",
      "content": "Why is the sky blue?"
    }
  ],
  "stream": false
}'
```

---

## AI SDK

**URL**: https://vercel.com/docs/ai-sdk

**Contents**:
- AI SDK
- Generating text
- Generating structured data
- Using tools with the AI SDK
- Getting started with the AI SDK
- More resources

The AI SDK is the TypeScript toolkit designed to help developers build AI-powered applications with Next.js, Vue, Svelte, Node.js, and more. Integrating LLMs into applications is complicated and heavily dependent on the specific model provider you use.

The AI SDK abstracts away the differences between model providers, eliminates boilerplate code for building chatbots, and allows you to go beyond text output to generate rich, interactive components.

At the center of the AI SDK is AI SDK Core, which provides a unified API to call any LLM.

The following example shows how to generate text with the AI SDK using OpenAI's GPT-5:

The unified interface means that you can easily switch between providers by changing just two lines of code. For example, to use Anthropic's Claude Sonnet 3.7:

While text generation can be useful, you might want to generate structured JSON data. For example, you might want to extract information from text, classify data, or generate synthetic data. AI SDK Core provides two functions (generateObject and streamObject) to generate structured data, allowing you to constrain model outputs to a specific schema.

The following example shows how to generate a type-safe recipe that conforms to a zod schema:

The AI SDK supports tool calling out of the box, allowing it to interact with external systems and perform discrete tasks. The following example shows how to use tool calling with the AI SDK:

The AI SDK is available as a package. To install it, run the following command:

See the AI SDK Getting Started guide for more information on how to get started with the AI SDK.

**Examples**:

```python
import { generateText } from 'ai';
 
const { text } = await generateText({
  model: 'openai/gpt-5',
  prompt: 'Explain the concept of quantum entanglement.',
});
```

```python
import { generateText } from 'ai';
import { anthropic } from '@ai-sdk/anthropic';
 
const { text } = await generateText({
  model: anthropic('claude-3-7-sonnet-20250219'),
  prompt: 'How many people will live in the world in 2040?',
});
```

```python
import { generateObject } from 'ai';
import { openai } from '@ai-sdk/openai';
import { z } from 'zod';
 
const { object } = await generateObject({
  model: 'openai/gpt-5',
  schema: z.object({
    recipe: z.object({
      name: z.string(),
      ingredients: z.array(z.object({ name: z.string(), amount: z.string() })),
      steps: z.array(z.string()),
    }),
  }),
  prompt: 'Generate a lasagna recipe.',
});
```

---

## Account Management

**URL**: https://vercel.com/docs/accounts

**Contents**:
- Account Management
- Sign up with email
- Sign up with a Git provider
- Login methods and connections
  - Login with passkeys
  - Logging in with SAML Single Sign-On
  - Choosing a connection when creating a project
  - Using an existing login connection

When you first sign up for Vercel, you'll create an account. This account is used to manage your Vercel resources. Vercel has three types of plans:

Each plan offers different features and resources, allowing you to choose the right plan for your needs.

When signing up for Vercel, you can choose to sign up with an email address or a Git provider.

To sign up with email:

When signing up with your email, no Git provider will be connected by default. See login methods and connections for information on how to connect a Git provider. If no Git provider is connected, you will be asked to verify your account on every login attempt.

You can sign up with any of the following supported Git providers:

Authorize Vercel to access your Git provider account. This will be the default login connection on your account.

Once signed up you can manage your login connections in the authentication section of your dashboard.

You can manage your login connections in the Authentication section of your account settings. To find this section:

Passkeys allow you to log into your Vercel account using biometrics such as face or fingerprint recognition, PINs, hardware security keys, and more.

To add a new passkey:

When you're done, the passkey will appear in a list of login methods on the Authentication page, alongside your other connections.

SAML Single Sign-On enables you to log into your Vercel Enterprise team with your organization's identity provider which manages your credentials.

Available only to Enterprise teams, this option can be configured by your team's administrator. To sign up for an Enterprise plan, contact sales.

When you create an account on Vercel, you will be prompted to create a project by either importing a Git repository or using a template.

Either way, you must connect a Git provider to your account, which you'll be able to use as a login method in the future.

Your Hobby team on Vercel can have only one login connection per third-party service. For example, y

*[Content truncated - see full docs]*

**Examples**:

```text
curl --request POST \
  --url https://api.vercel.com/v1/teams \
  --header "Authorization: Bearer $VERCEL_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
  "slug": "<team-slug>",
  "name": "<team-name>"
}'
```

```python
import { Vercel } from '@vercel/sdk';
 
const vercel = new Vercel({
  bearerToken: '<YOUR_BEARER_TOKEN_HERE>',
});
 
async function run() {
  const result = await vercel.teams.createTeam({
    slug: 'team-slug',
    name: 'team-name',
  });
 
  // Handle the result
  console.log(result);
}
 
run();
```

---

## Adding a Model

**URL**: https://vercel.com/docs/ai/adding-a-model

**Contents**:
- Adding a Model
- Exploring models
  - Using the model playground
  - Adding a model to your project
- Featured AI integrations
  - xAIMarketplace native integration
  - GroqMarketplace native integration
  - falMarketplace native integration

If you have integrations installed, scroll to the bottom to access the models explorer.

The model playground lets you test the model you are interested in before adding it to your project. If you have not installed an AI provider through the Vercel dashboard, then you will have ten lifetime generations per provider (they do not refresh, and once used, are spent) regardless of plan. If you have installed an AI provider that supports the model, Vercel will use your provider key.

You can use the model playground to test the model's capabilities and see if it fits your projects needs.

The model playground differs depending on the model you are testing. For example, if you are testing a chat model, you can input a prompt and see the model's response. If you are testing an image model, you can upload an image and see the model's output. Each model may have different variations based on the provider you choose.

The playground also lets you also configure the model's settings, such as temperature, maximum output length, duration, continuation, top p, and more. These settings and inputs are specific to the model you are testing.

Once you have decided on the model you want to add to your project:

An AI service with an efficient text model and a wide context image understanding model.

A high-performance AI inference service with an ultra-fast Language Processing Unit (LPU) architecture.

A serverless AI inferencing platform for creative processes.

A platform with access to a vast library of open-source models.

Learn how to integrate Perplexity with Vercel.

Learn how to integrate Replicate with Vercel.

Learn how to integrate ElevenLabs with Vercel.

Learn how to integrate LMNT with Vercel.

Learn how to integrate Together AI with Vercel.

Connect powerful AI models like GPT-4

---

## Adding a Provider

**URL**: https://vercel.com/docs/ai/adding-a-provider

**Contents**:
- Adding a Provider
- Adding a native integration provider
- Adding a connectable account provider
- Featured AI integrations
  - xAIMarketplace native integration
  - GroqMarketplace native integration
  - falMarketplace native integration
  - DeepInfraMarketplace native integration

When you navigate to the AI tab, you'll see a list of installed AI integrations. If you don't have installed integrations, you can browse and connect to the AI models and services that best fit your project's needs.

For more information on managing native integration providers, review Manage native integrations.

If no integrations are installed, browse the list of available providers and click on the provider you would like to add.

Once you add a provider, the AI tab will display a list of the providers you have installed or connected to. To add more providers:

An AI service with an efficient text model and a wide context image understanding model.

A high-performance AI inference service with an ultra-fast Language Processing Unit (LPU) architecture.

A serverless AI inferencing platform for creative processes.

A platform with access to a vast library of open-source models.

---

## App Attribution

**URL**: https://vercel.com/docs/ai-gateway/app-attribution

**Contents**:
- App Attribution
- How it works
- Examples
- Setting headers at the provider level
- Using the Global Default Provider

App attribution allows Vercel to identify the application making a request through AI Gateway. When provided, your app can be featured on AI Gateway pages, driving awareness.

App Attribution is optional. If you do not send these headers, your requests will work normally.

AI Gateway reads two request headers when present:

You can set these headers directly in your server-side requests to AI Gateway.

You can also configure attribution headers when you create the AI Gateway provider instance. This way, the headers are automatically included in all requests without needing to specify them for each function call.

You can also use the AI SDK's global provider configuration to set your custom provider instance as the default. This allows you to use plain string model IDs throughout your application while automatically including your attribution headers.

**Examples**:

```python
import { streamText } from 'ai';
 
const result = streamText({
  headers: {
    'http-referer': 'https://myapp.vercel.app',
    'x-title': 'MyApp',
  },
  model: 'anthropic/claude-sonnet-4',
  prompt: 'Hello, world!',
});
 
for await (const part of result.textStream) {
  process.stdout.write(part);
}
```

```python
import OpenAI from 'openai';
 
const openai = new OpenAI({
  apiKey: process.env.AI_GATEWAY_API_KEY,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});
 
const response = await openai.chat.completions.create(
  {
    model: 'anthropic/claude-sonnet-4',
    messages: [
      {
        role: 'user',
        content: 'Hello, world!',
      },
    ],
  },
  {
    headers: {
      'http-referer': 'https://myapp.vercel.app',
      'x-title': 'MyApp',
    },
  },
);
 
console.log(response.choices[0].mes
...
```

```python
import os
from openai import OpenAI
 
client = OpenAI(
  api_key=os.getenv('AI_GATEWAY_API_KEY'),
  base_url='https://ai-gateway.vercel.sh/v1'
)
 
response = client.chat.completions.create(
    model='anthropic/claude-sonnet-4',
    messages=[
        {
            'role': 'user',
            'content': 'Hello, world!',
        },
    ],
    extra_headers={
        'http-referer': 'https://myapp.vercel.app',
        'x-title': 'MyApp',
    },
)
 
print(response.choices[0].message.content)
```

---

## Authentication

**URL**: https://vercel.com/docs/ai-gateway/authentication

**Contents**:
- Authentication
- API key
  - Creating an API Key
  - Navigate to the AI Gateway tab
  - Access API key management
  - Create a new API key
  - Save your API key
  - Using the API key

To use the AI Gateway, you need to authenticate your requests. There are two authentication methods available:

API keys provide a secure way to authenticate your requests to the AI Gateway. You can create and manage multiple API keys through the Vercel Dashboard.

From the Vercel dashboard, click the AI Gateway tab to access the AI Gateway settings.

Click API keys on the left sidebar to view and manage your API keys.

Click Create key and proceed with Create key from the dialog to generate a new API key.

Once you have the API key, save it to .env.local at the root of your project (or in your preferred environment file):

When you specify a model id as a plain string, the AI SDK will automatically use the Vercel AI Gateway provider to route the request. The AI Gateway provider looks for the API key in the AI_GATEWAY_API_KEY environment variable by default.

The Vercel OIDC token is a way to authenticate your requests to the AI Gateway without needing to manage an API key. Vercel automatically generates the OIDC token that it associates with your Vercel project.

Vercel OIDC tokens are only valid for 12 hours, so you will need to refresh them periodically during local development. You can do this by running vercel env pull again.

Before you can use the OIDC token during local development, ensure that you link your application to a Vercel project:

Pull the environment variables from Vercel to get the OIDC token:

With OIDC authentication, you can directly use the gateway provider without needing to obtain an API key or set it in an environment variable:

**Examples**:

```text
AI_GATEWAY_API_KEY=your_api_key_here
```

```python
import { generateText } from 'ai';
 
export async function GET() {
  const result = await generateText({
    model: 'xai/grok-3',
    prompt: 'Why is the sky blue?',
  });
  return Response.json(result);
}
```

```text
vercel link
```

---

## Bring Your Own Key (BYOK)

**URL**: https://vercel.com/docs/ai-gateway/byok

**Contents**:
- Bring Your Own Key (BYOK)
- Getting started
  - Retrieve credentials from your AI provider
  - Add the credentials to your Vercel team
  - Use the credentials in your AI Gateway requests
- Testing your credentials
  - Azure OpenAI setup tips

Using your own credentials with an external AI provider allows AI Gateway to authenticate requests on your behalf with no added markup. This approach is useful for utilizing credits provided by the AI provider or executing AI queries that access private cloud data. If a query using your credentials fails, AI Gateway will retry the query with its system credentials to improve service availability.

Integrating credentials like this with AI Gateway is sometimes referred to as Bring-Your-Own-Key, or BYOK. In the Vercel dashboard this feature is found in the AI Gateway tab under the Integrations section in the sidebar.

Provider credentials are scoped to be available throughout your Vercel team, so you can use the same credentials across multiple projects.

First, retrieve credentials from your AI provider. These credentials will be used first to authenticate requests made to that provider through the AI Gateway. If a query made with your credentials fails, AI Gateway will re-attempt with system credentials, aiming to provide improved availability.

Once the credentials are added, it will automatically be included in your requests to the AI Gateway. You can now use these credentials to authenticate your requests.

After successfully adding your credentials for a provider, you can verify that they're working directly from the Integrations tab. To test your credentials:

This will execute a small test query using a cheap and fast model from the selected provider to verify the health of your credentials. The test is designed to be minimal and cost-effective while ensuring your authentication is working properly.

Once the test completes, you can click on the test result badge to open a detailed test result modal. This modal includes:

---

## Build Output API

**URL**: https://vercel.com/docs/build-output-api

**Contents**:
- Build Output API
- Overview
- Known limitations
- More resources

The Build Output API is a file-system-based specification for a directory structure that can produce a Vercel deployment.

Framework authors can take advantage of framework-defined infrastructure by implementing this directory structure as the output of their build command. This allows the framework to define and use all of the Vercel platform features.

The Build Output API closely maps to the Vercel product features in a logical and understandable format.

It is primarily targeted toward authors of web frameworks who would like to utilize all of the Vercel platform features, such as Vercel Functions, Routing, Caching, etc.

If you are a framework author looking to integrate with Vercel, you can use this reference as a way to understand which files the framework should emit to the .vercel/output directory.

If you are not using a framework and would like to still take advantage of any of the features that those frameworks provide, you can create the .vercel/output directory and populate it according to this specification yourself.

You can find complete examples of Build Output API directories in vercel/examples.

Check out our blog post on using the Build Output API to build your own framework with Vercel.

Native Dependencies: Please keep in mind that when building locally, your build tools will compile native dependencies targeting your machine’s architecture. This will not necessarily match what runs in production on Vercel.

For projects that depend on native binaries, you should build on a host machine running Linux with a x64 CPU architecture, ideally the same as the platform Build Image.

---

## Build Output Configuration

**URL**: https://vercel.com/docs/build-output-api/configuration

**Contents**:
- Build Output Configuration
- config.json supported properties
  - version
    - version example
  - routes
    - Source route
        - Source route: MatchableValue
        - Source route: HasField

.vercel/output/config.json

Schema (as TypeScript):

The config.json file contains configuration information and metadata for a Deployment. The individual properties are described in greater detail in the sub-sections below.

At a minimum, a config.json file with a "version" property is required.

.vercel/output/config.json

The version property indicates which version of the Build Output API has been implemented. The version described in this document is version 3.

.vercel/output/config.json

vercel/examples/build-output-api/routes

The routes property describes the routing rules that will be applied to the Deployment. It uses the same syntax as the routes property of the vercel.json file.

Routes may be used to point certain URL paths to others on your Deployment, attach response headers to paths, and various other routing-related use-cases.

The routing system has multiple phases. The handle value indicates the start of a phase. All following routes are only checked in that phase.

The following example shows a routing rule that will cause the /redirect path to perform an HTTP redirect to an external URL:

.vercel/output/config.json

vercel/examples/build-output-api/image-optimization

The images property defines the behavior of Vercel's native Image Optimization API, which allows on-demand optimization of images at runtime.

The following example shows an image optimization configuration that specifies allowed image size dimensions, external domains, caching lifetime and file formats:

When the images property is defined, the Image Optimization API will be available by visiting the /_vercel/image path. When the images property is undefined, visiting the /_vercel/image path will respond with 404 Not Found.

The API accepts the following query string parameters:

.vercel/output/config.json

vercel/examples/build-output-api/wildcard

The wildcard property relates to Vercel's Internationalization feature. The way it works is the domain names listed in this array ar

*[Content truncated - see full docs]*

**Examples**:

```text
type Config = {
  version: 3;
  routes?: Route[];
  images?: ImagesConfig;
  wildcard?: WildcardConfig;
  overrides?: OverrideConfig;
  cache?: string[];
  crons?: CronsConfig;
};
```

```text
"version": 3
```

```text
type Route = Source | Handler;
```

---

## Build Queues

**URL**: https://vercel.com/docs/builds/build-queues

**Contents**:
- Build Queues
- With On-Demand Concurrent Builds
- Without On-Demand Concurrent Builds
- Concurrency queue
  - How concurrent build slots work
- Git branch queue

Build queueing is when a build must wait for resources to become available before starting. This creates more time between when the code is committed and the deployment being ready.

On-Demand Concurrent Builds prevent all build queueing so your team can build faster. Your builds will never be queued becuase Vercel will dynamically scale the amount of builds that can run simultaneously.

If you're experiencing build queues, we strongly recommend enabling On-Demand Concurrent Builds. For billing information, visit the usage and limits section for builds.

When multiple deployments are started concurrently from code changes, Vercel's build system places deployments into one of the following queues:

This queue manages how many builds can run in parallel based on the number of concurrent build slots available to the team. If all concurrent build slots are in use, new builds are queued until a slot becomes available unless you have On-Demand Concurrent Builds enabled at the project level.

Concurrent build slots are the key factor in concurrent build queuing. They control how many builds can run at the same time and ensure efficient use of resources while prioritizing the latest changes.

Each account plan comes with a predefined number of build slots:

Builds are handled sequentially. If new commits are pushed while a build is in progress:

This means that commits in between the current build and most recent commit will not produce builds.

Enterprise users can use Urgent On-Demand Concurrency to skip the Git branch queue for specific builds.

---

## Build image overview

**URL**: https://vercel.com/docs/builds/build-image

**Contents**:
- Build image overview
- Pre-installed packages
- Running the build image locally
- Installing additional packages

When you initiate a deployment, Vercel will build your project within a container using the build image. Vercel supports multiple runtimes.

The build image uses Amazon Linux 2023 as its base image.

The following packages are pre-installed in the build image with dnf, the default package manager for Amazon Linux 2023.

You can install these packages using the dnf package manager with the following command:

Vercel does not provide the build image itself, but you can use the Amazon Linux 2023 base image to test things locally:

When you are done, run exit to return.

You can install additional packages into the build container by configuring the Install Command within the dashboard or the "installCommand" in your vercel.json to use any of the following commands.

The build image includes access to repositories with stable versions of popular packages. You can list all packages with the following command:

You can search for a package by name with the following command:

You can install a package by name with the following command:

**Examples**:

```bash
dnf alsa-lib at-spi2-atk atk autoconf automake brotli bsdtar bzip2 bzip2-devel cups-libs expat-devel gcc gcc-c++ git glib2-devel glibc-devel gtk3 gzip ImageMagick-devel iproute java-11-amazon-corretto-headless libXScrnSaver libXcomposite libXcursor libXi libXrandr libXtst libffi-devel libglvnd-glx libicu libjpeg libjpeg-devel libpng libpng-devel libstdc++ libtool libwebp-tools libzstd-devel make nasm ncurses-libs ncurses-compat-libs openssl openssl-devel openssl-libs pango procps perl readline-d
...
```

```text
docker run --rm -it amazonlinux:2023.2.20231011.0 sh
```

```text
dnf search my-package-here
```

---

## Build with AI on Vercel

**URL**: https://vercel.com/docs/ai

**Contents**:
- Build with AI on Vercel
- Integrating with AI providers
- Using AI integrations
- Featured AI integrations
  - xAIMarketplace native integration
  - GroqMarketplace native integration
  - falMarketplace native integration
  - DeepInfraMarketplace native integration

AI services and models help enhance and automate the building and deployment of applications for various use cases:

With Vercel AI integrations, you can build and deploy these AI-powered applications efficiently. Through the Vercel Marketplace, you can research which AI service fits your needs with example use cases. Then, you can install and manage two types of AI integrations:

You can view your installed AI integrations by navigating to the AI tab of your Vercel dashboard. If you don't have installed integrations, you can browse and connect to the AI models and services that best fit your project's needs. Otherwise, you will see a list of your installed native and connectable account integrations, with an indication of which project(s) they are connected to. You will be able to browse available services, models and templates below the list of installed integrations.

See the adding a provider guide to learn how to add a provider to your Vercel project, or the adding a model guide to learn how to add a model to your Vercel project.

An AI service with an efficient text model and a wide context image understanding model.

A high-performance AI inference service with an ultra-fast Language Processing Unit (LPU) architecture.

A serverless AI inferencing platform for creative processes.

A platform with access to a vast library of open-source models.

Learn how to integrate Perplexity with Vercel.

Learn how to integrate Replicate with Vercel.

Learn how to integrate ElevenLabs with Vercel.

Learn how to integrate LMNT with Vercel.

Learn how to integrate Together AI with Vercel.

Connect powerful AI models like GPT-4

---

## Builds

**URL**: https://vercel.com/docs/builds

**Contents**:
- Builds
- Build infrastructure
- How builds are triggered
- Build customization
- Skipping the build step
- Monorepos
- Concurrency and queues
- Environment variables

Vercel automatically performs a build every time you deploy your code, whether you're pushing to a Git repository, importing a project via the dashboard, or using the Vercel CLI. This process compiles, bundles, and optimizes your application so it's ready to serve to your users.

When you initiate a build, Vercel creates a secure, isolated virtual environment for your project:

This infrastructure handles millions of builds daily, supporting everything from individual developers to large enterprises, while maintaining strict security and performance standards.

Most frontend frameworks—like Next.js, SvelteKit, and Nuxt—are auto-detected, with defaults applied for Build Command, Output Directory, and other settings. To see if your framework is included, visit the Supported Frameworks page.

Builds can be initiated in the following ways:

Push to Git: When you connect a GitHub, GitLab, or Bitbucket repository, each commit to a tracked branch initiates a new build and deployment. By default, Vercel performs a shallow clone of your repo (git clone --depth=10) to speed up build times.

Vercel CLI: Running vercel locally deploys your project. By default, this creates a preview build unless you add the --prod flag (for production).

Dashboard deploy: Clicking Deploy in the dashboard or creating a new project also triggers a build.

Depending on your framework, Vercel automatically sets the Build Command, Install Command, and Output Directory. If needed, you can customize these in your project's Settings:

Build Command: Override the default (npm run build, next build, etc.) for custom workflows.

Output Directory: Specify the folder containing your final build output (e.g., dist or build).

Install Command: Control how dependencies are installed (e.g., pnpm install, yarn install) or skip installing dev dependencies if needed.

To learn more, see Configuring a Build.

For static websites—HTML, CSS, and client-side JavaScript only—no build step is required. In those cases:



*[Content truncated - see full docs]*

---

## Configuring a Build

**URL**: https://vercel.com/docs/builds/configure-a-build

**Contents**:
- Configuring a Build
- Framework Settings
  - Framework Preset
  - Build Command
  - Output Directory
  - Install Command
    - Corepack
    - Custom Install Command for your API

When you make a deployment, Vercel builds your project. During this time, Vercel performs a "shallow clone" on your Git repository using the command git clone --depth=10 (...) and fetches ten levels of git commit history. This means that only the latest ten commits are pulled and not the entire repository history.

Vercel automatically configures the build settings for many front-end frameworks, but you can also customize the build according to your requirements.

To configure your Vercel build with customized settings, choose a project from the dashboard and go to its Settings tab.

The Build and Deployment section of the Settings tab offers the following options to customize your build settings:

If you'd like to override the settings or specify a different framework, you can do so from the Build & Development Settings section.

You have a wide range of frameworks to choose from, including Next.js, Svelte, and Nuxt. In several use cases, Vercel automatically detects your project's framework and sets the best settings for you.

Inside the Framework Preset settings, use the drop-down menu to select the framework of your choice. This selection will be used for all deployments within your Project. The available frameworks are listed below:

However, if no framework is detected, "Other" will be selected. In this case, the Override toggle for the Build Command will be enabled by default so that you can enter the build command manually. The remaining deployment process is that for default frameworks.

If you would like to override Framework Preset for a specific deployment, add framework to your vercel.json configuration.

Vercel automatically configures the Build Command based on the framework. Depending on the framework, the Build Command can refer to the project’s package.json file.

For example, if Next.js is your framework:

If you'd like to override the Build Command for all deployments in your Project, you can turn on the Override toggle and specify the custom com

*[Content truncated - see full docs]*

**Examples**:

```text
{
  "packageManager": "pnpm@7.5.1"
}
```

---

## Deploy MCP servers to Vercel

**URL**: https://vercel.com/docs/mcp/deploy-mcp-servers-to-vercel

**Contents**:
- Deploy MCP servers to Vercel
- Deploy a Template
- Deploy MCP servers efficiently
- Deploy an MCP server on Vercel
  - Test the MCP server locally
  - Configure an MCP host
- Enabling authorization
  - Secure your server with OAuth

Deploy your Model Context Protocol (MCP) servers on Vercel to take advantage of features like Vercel Functions, OAuth, and efficient scaling for AI applications.

Get started in minutes

ChatGPT app with Next.js

Ship a ChatGPT app on Vercel with Next.js and Model Context Protocol (MCP).

A fullstack template for using x402 with MCP and AI SDK.

Run an Model Context Protocol (MCP) server on Vercel with Next.js.

Vercel provides the following features for production MCP deployments:

Use the mcp-handler package and create the following API route to host an MCP server that provides a single tool that rolls a dice.

This assumes that your MCP server application, with the above-mentioned API route, runs locally at http://localhost:3000.

When you deploy your application on Vercel, you will get a URL such as https://my-mcp-server.vercel.app.

Using Cursor, add the URL of your MCP server to the configuration file in Streamable HTTP transport format.

You can now use your MCP roll dice tool in Cursor's AI chat or any other MCP client.

The mcp-handler provides built-in OAuth support to secure your MCP server. This ensures that only authorized clients with valid tokens can access your tools.

To add OAuth authorization to the MCP server you created in the previous section:

To comply with the MCP specification, your server must expose a metadata endpoint that provides OAuth configuration details. Among other things, this endpoint allows MCP clients to discover, how to authorize with your server, which authorization servers can issue valid tokens, and what scopes are supported.

To view the full list of values available to be returned in the OAuth Protected Resource Metadata JSON, see the protected resource metadata RFC.

MCP clients that are compliant with the latest version of the MCP spec can now securely connect and invoke tools defined in your MCP server, when provided with a valid OAuth token.

Learn how to deploy MCP servers on Vercel, connect to them using the AI SDK

*[Content truncated - see full docs]*

**Examples**:

```python
import { z } from 'zod';
import { createMcpHandler } from 'mcp-handler';
 
const handler = createMcpHandler(
  (server) => {
    server.tool(
      'roll_dice',
      'Rolls an N-sided die',
      { sides: z.number().int().min(2) },
      async ({ sides }) => {
        const value = 1 + Math.floor(Math.random() * sides);
        return {
          content: [{ type: 'text', text: `🎲 You rolled a ${value}!` }],
        };
      },
    );
  },
  {},
  { basePath: '/api' },
);
 
export { handler as 
...
```

```text
npx @modelcontextprotocol/inspector@latest http://localhost:3000
```

```text
{
  "mcpServers": {
    "server-name": {
      "url": "https://my-mcp-server.vercel.app/api/mcp"
    }
  }
}
```

---

## Deployment Protection Exception

**URL**: https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/deployment-protection-exceptions

**Contents**:
- Deployment Protection Exception
- Adding a Deployment Protection Exception
  - Go to Project Deployment Protection Settings
  - Select Add Domain
  - Specify domain
  - Confirm domain
- Removing a Deployment Protection Exception
  - Go to Project Deployment Protection Settings

Deployment Protection Exceptions are available on Enterprise plans or with the Advanced Deployment Protection add-on for Pro plans

You can use Deployment Protection Exceptions to disable Deployment Protection (including Vercel Authentication, Password Protection, and Trusted IPs) for a list of preview domains.

When you add a domain to Deployment Protection Exceptions, it will automatically become publicly accessible and will no longer be covered by Deployment Protection features. When you remove a domain from Deployment Protection Exceptions, the domain becomes protected again with the project's Deployment Protection settings.

Deployment Protection Exceptions is designed for Preview Deployment domains, if you wish to make a Production Deployment domain public, see Configuring Deployment Protection.

From your Vercel dashboard:

From the Deployment Protection Exceptions section, select Add Domain:

From the Unprotect Domain modal:

From the Unprotect Domain modal:

All your existing and future deployments for that domain will be unprotected.

From your Vercel dashboard:

From the Deployment Protection Exceptions section:

From the Reprotect Domain modal:

All your existing and future deployments for that domain will be protected.

You can view and manage all the existing Deployment Protection Exceptions for your team in the following way

---

## Deployment Protection on Vercel

**URL**: https://vercel.com/docs/deployment-protection

**Contents**:
- Deployment Protection on Vercel
- Configuring Deployment Protection
- Understanding Deployment Protection by environment
  - Standard Protection
    - Migrating to Standard Protection
  - All deployments
  - Only production deployments
  - (Legacy) Standard Protection

Deployment Protection safeguards both your preview and production URLs across various environments. Configured at the project level through your settings, Deployment Protection provides detailed access control for different deployment types.

Vercel offers the following Deployment Protection features:

Deployment protection requires authentication for all requests, including those to Middleware.

Deployment Protection is managed through your project settings. To configure Deployment Protection:

You can configure the type of Deployment Protection for each environment in your project depending on your projects security needs. When choosing your protection method, you can select from three options:

To protect only production URLs, you can use Trusted IPs. Note that this option is only available on the Enterprise plan.

Standard Protection is available on all plans

Standard Protection is the recommended way to secure your deployments, as it protects all domains except Production Custom Domains.

Standard Protection can be configured with the following Deployment Protection features:

Enabling Standard Protection restricts public access to the production generated deployment URL. This affects VERCEL_URL and VERCEL_BRANCH_URL from System Environment Variables, making them unsuitable for fetch requests.

If you are using VERCEL_URL or VERCEL_BRANCH_URL to make fetch requests, you will need to update your requests to target the same domain the user has requested.

The Framework Environment Variable VERCEL_URL is prefixed with the name of the framework. For example, VERCEL_URL for Next.js is NEXT_PUBLIC_VERCEL_URL, and VERCEL_URL for Nuxt is NUXT_ENV_VERCEL_URL. See the Framework Environment Variables documentation for more information.

For client-side requests, use relative paths in the fetch call to target the current domain, automatically including the user's authentication cookie for protected URLs.

For server-side requests, use the origin from the incoming request 

*[Content truncated - see full docs]*

**Examples**:

```text
// Before
fetch(`${process.env.VERCEL_URL}/some/path`);
 
// After
fetch('/some/path');
// Note: For operations requiring fully qualified URLs, such as generating OG images,
// replace '/some/path' with the actual domain (e.g. 'https://yourdomain.com/some/path').
```

```javascript
const headers = { cookie: <incoming request header cookies> };
fetch('<incoming request origin>/some/path', { headers });
```

---

## Directory Sync

**URL**: https://vercel.com/docs/directory-sync

**Contents**:
- Directory Sync
- Configuring Directory Sync
  - Supported providers
- Preventing account lockout

Directory Sync is available on Enterprise plans

Those with the owner role can access this feature

Directory Sync helps teams manage their organization membership from a third-party identity provider like Google Directory or Okta. Like SAML, Directory Sync is only available for Enterprise Teams and can only be configured by Team Owners.

When Directory Sync is configured, changes to your Directory Provider will automatically be synced with your team members. The previously existing permissions/roles will be overwritten by Directory Sync, including current user performing the sync.

Make sure that you still have the right permissions/role after configuring Directory Sync, otherwise you might lock yourself out.

All team members will receive an email detailing the change. For example, if a new user is added to your Okta directory, that user will automatically be invited to join your Vercel Team. If a user is removed, they will automatically be removed from the Vercel Team.

You can configure a mapping between your Directory Provider's groups and a Vercel Team role. For example, your Engineers group on Okta can be configured with the member role on Vercel, and your Admin group can use the owner role.

To configure directory sync for your team:

SAML Single Sign-On is optionally available on the Enterprise Plan. To enable contact sales.

See SAML Single Sign-On for a list of all the SAML providers that Vercel supports.

To prevent account lockout ensure that at least one person in your team has the owner role, and that they are not removed from the team.

If access is lost due to removal of team owners, use the following group names to automatically allocate the corresponding roles to individuals in that group:

---

## Features

**URL**: https://vercel.com/docs/build-output-api/features

**Contents**:
- Features
- High-level routing
    - cleanUrls
- Edge Middleware
  - Edge Middleware example
- Draft Mode
- On-Demand Incremental Static Regeneration (ISR)

This section describes how to implement common Vercel platform features through the Build Output API through a combination of platform primitives, configuration and helper functions.

The vercel.json file supports an easier-to-use syntax for routing through properties like rewrites, headers, etc. However, the config.json "routes" property supports a lower-level syntax.

The getTransformedRoutes() function from the @vercel/routing-utils npm package can be used to convert this higher-level syntax into the lower-level format that is supported by the Build Output API. For example:

The cleanUrls: true routing feature is a special case because, in addition to the routes generated with the helper function above, it also requires that the static HTML files have their .html suffix removed.

This can be achieved by utilizing the "overrides" property in the config.json file:

vercel/examples/build-output-api/edge-middleware

An Edge Runtime function can act as a "middleware" in the HTTP request lifecycle for a Deployment. Middleware is useful for implementing functionality that may be shared by many URL paths in a Project (e.g. authentication), before passing the request through to the underlying resource (such as a page or asset) at that path.

An Edge Middleware is represented on the file system in the same format as an Edge Function. To use the middleware, add additional rules in the routes configuration mapping URLs (using the src property) to the middleware (using the middlewarePath property).

The following example adds a rule that calls the auth middleware for any URL that starts with /api, before continuing to the underlying resource:

vercel/examples/build-output-api/preview-mode

When using Prerender Functions, you may want to implement "Draft Mode" which would allow you to bypass the caching aspect of prerender functions. For example, while writing draft blog posts before they are ready to be published.

To implement this, the bypassToken of the <name>.prerender-co

*[Content truncated - see full docs]*

**Examples**:

```python
import { writeFileSync } from 'fs';
import { getTransformedRoutes } from '@vercel/routing-utils';
 
const { routes } = getTransformedRoutes({
  trailingSlash: false,
  redirects: [
    { source: '/me', destination: '/profile.html' },
    { source: '/view-source', destination: 'https://github.com/vercel/vercel' },
  ],
});
 
const config = {
  version: 3,
  routes,
};
writeFileSync('.vercel/output/config.json', JSON.stringify(config));
```

```python
import { writeFileSync } from 'fs';
import { getTransformedRoutes } from '@vercel/routing-utils';
 
const { routes } = getTransformedRoutes({
  cleanUrls: true,
});
 
const config = {
  version: 3,
  routes,
  overrides: {
    'blog.html': {
      path: 'blog',
    },
  },
};
writeFileSync('.vercel/output/config.json', JSON.stringify(config));
```

```text
"routes": [
    {
      "src": "/api/(.*)",
      "middlewareRawSrc": ["/api"],
      "middlewarePath": "auth",
      "continue": true
    }
  ]
```

---

## Framework Integrations

**URL**: https://vercel.com/docs/ai-gateway/framework-integrations

**Contents**:
- Framework Integrations
  - Integration overview
  - Supported frameworks

The Vercel AI Gateway integrates with popular community AI frameworks and tools, enabling you to build powerful AI applications while leveraging the Gateway's features like cost tracking and unified API access.

You can integrate the AI Gateway with popular frameworks in several ways:

The following below list is a non-exhaustive list of frameworks that currently support AI Gateway integration:

---

## Image Generation

**URL**: https://vercel.com/docs/ai-gateway/image-generation

**Contents**:
- Image Generation
- Google Gemini 2.5 Flash Image
- Basic image generation
- Use images as input
- OpenAI-compatible API response format
  - Response structure
  - Key format details
  - Streaming responses

AI Gateway supports image generation and editing capabilities. You can generate new images from text prompts, edit existing images, and create variations with natural language instructions.

You can view all available models that support image generation by using the Image filter at the AI Gateway Models page.

Google's Gemini 2.5 Flash Image model offers state-of-the-art image generation and editing capabilities. This model supports specifying response modalities to enable image outputs alongside text responses. Find details on this model in the Model Library.

Generate images from text prompts using the generateText or streamText functions with appropriate provider options.

Provide existing images as input to edit images, combine images, or create variations of existing content.

Check the AI SDK provider documentation for more on provider/model-specific image generation configuration.

For OpenAI-compatible API usage with image generation, see the OpenAI-Compatible API Image Generation section.

When using the OpenAI-compatible API (/v1/chat/completions) for image generation, responses follow a specific format that separates text content from generated images:

For streaming requests, images are delivered in delta chunks:

Generated images are returned as GeneratedFile objects in the result.files array. Each contains:

When using streamText, images are delivered through fullStream as file events:

**Examples**:

```python
import 'dotenv/config';
import { generateText } from 'ai';
import fs from 'node:fs';
import path from 'node:path';
 
async function main() {
  const result = await generateText({
    model: 'google/gemini-2.5-flash-image-preview',
    providerOptions: {
      google: { responseModalities: ['TEXT', 'IMAGE'] },
    },
    prompt:
      'Render two versions of a pond tortoise sleeping on a log in a lake at sunset.',
  });
 
  if (result.text) {
    console.log(result.text);
  }
 
  // Save generate
...
```

```python
import 'dotenv/config';
import { streamText } from 'ai';
import fs from 'node:fs';
import path from 'node:path';
 
async function main() {
  const result = streamText({
    model: 'google/gemini-2.5-flash-image-preview',
    providerOptions: {
      google: { responseModalities: ['TEXT', 'IMAGE'] },
    },
    prompt: 'Render a pond tortoise sleeping on a log in a lake at sunset.',
  });
 
  // Create output directory if it doesn't exist
  const outputDir = 'output';
  fs.mkdirSync(outputDir, { 
...
```

```python
import { generateText } from 'ai';
import fs from 'node:fs';
 
const result = await generateText({
  model: 'google/gemini-2.5-flash-image-preview',
  providerOptions: {
    google: { responseModalities: ['TEXT', 'IMAGE'] },
  },
  messages: [
    {
      role: 'user',
      content: [
        {
          type: 'text',
          text: 'Combine these two images into one artistic composition.',
        },
        {
          type: 'file',
          mediaType: 'image/png',
          data: fs.readFi
...
```

---

## Incremental Migration to Vercel

**URL**: https://vercel.com/docs/incremental-migration

**Contents**:
- Incremental Migration to Vercel
- Why opt for incremental migration?
  - Disadvantages of one-time migrations
  - When to use incremental migration?
- Incremental migration strategies
  - Vertical migration
  - Horizontal migration
  - Hybrid migration

When migrating to Vercel you should use an incremental migration strategy. This allows your current site and your new site to operate simultaneously, enabling you to move different sections of your site at a pace that suits you.

In this guide, we'll explore incremental migration benefits, strategies, and implementation approaches for a zero-downtime migration to Vercel.

Incremental migrations offer several advantages:

One-time migration involves developing the new site separately before switching traffic over. This approach has certain drawbacks:

Despite requiring more effort to make the new and legacy sites work concurrently, incremental migration is beneficial if:

With incremental migration, legacy and new systems operate simultaneously. Depending on your strategy, you'll select a system aspect, like a feature or user group, to migrate incrementally.

This strategy targets system features with the following process:

Throughout, both systems operate in parallel with migrated features routed to the new system.

This strategy focuses on system users with the following process:

During migration, a subset of users accesses the new system while others continue using the legacy system.

A blend of vertical and horizontal strategies. For each feature subset, migrate by user group before moving to the next feature subset.

Follow these steps to incrementally migrate your website to Vercel. Two possible strategies can be applied:

In this approach, you make Vercel the entry point for all your production traffic. When you begin, all traffic will be sent to the legacy server with rewrites and/or fallbacks. As you migrate different aspects of your site to Vercel, you can remove the rewrites/fallbacks to the migrated paths so that they are now served by Vercel.

Use the framework of your choice to deploy your application to Vercel

Send all traffic to the legacy server using one of the following 3 methods:

Use rewrites built-in to the framework such as configuring next.

*[Content truncated - see full docs]*

**Examples**:

```python
import type { NextConfig } from 'next';
 
const nextConfig: NextConfig = {
  async rewrites() {
    return {
      fallback: [
        {
          source: '/:path*',
          destination: 'https://my-legacy-site.com/:path*',
        },
      ],
    };
  },
};
 
export default nextConfig;
```

```python
import { get } from '@vercel/edge-config';
import { NextRequest, NextResponse } from 'next/server';
 
export const config = {
  matcher: '/((?!api|_next/static|favicon.ico).*)',
};
 
export default async function middleware(request: NextRequest) {
  const url = request.nextUrl;
  const rewrites = await get('rewrites'); // Get rewrites stored in Edge Config
 
  for (const rewrite of rewrites) {
    if (rewrite.source === url.pathname) {
      url.pathname = rewrite.destination;
      return NextR
...
```

```python
import type { NextConfig } from 'next';
 
const nextConfig: NextConfig = {
  basePath: '/new-feature',
};
 
export default nextConfig;
```

---

## LangChain

**URL**: https://vercel.com/docs/ai-gateway/framework-integrations/langchain

**Contents**:
- LangChain
- Getting started
  - Create a new project
  - Install dependencies
  - Configure environment variables
  - Create your LangChain application
  - Running the application

LangChain gives you tools for every step of the agent development lifecycle. This guide demonstrates how to integrate Vercel AI Gateway with LangChain to access various AI models and providers.

First, create a new directory for your project and initialize it:

Install the required LangChain packages along with the dotenv and @types/node packages:

Create a .env file with your Vercel AI Gateway API key:

If you're using the AI Gateway from within a Vercel deployment, you can also use the VERCEL_OIDC_TOKEN environment variable which will be automatically provided.

Create a new file called index.ts with the following code:

Run your application using Node.js:

You should see a response from the AI model in your console.

**Examples**:

```text
mkdir langchain-ai-gateway
cd langchain-ai-gateway
pnpm dlx init -y
```

```text
pnpm i langchain @langchain/core @langchain/openai dotenv @types/node
```

```text
AI_GATEWAY_API_KEY=your-api-key-here
```

---

## LangFuse

**URL**: https://vercel.com/docs/ai-gateway/framework-integrations/langfuse

**Contents**:
- LangFuse
- Getting started
  - Create a new project
  - Install dependencies
  - Configure environment variables
  - Create your LangFuse application
  - Running the application

LangFuse is an LLM engineering platform that helps teams collaboratively develop, monitor, evaluate, and debug AI applications. This guide demonstrates how to integrate Vercel AI Gateway with LangFuse to access various AI models and providers.

First, create a new directory for your project and initialize it:

Install the required LangFuse packages along with the dotenv and @types/node packages:

Create a .env file with your Vercel AI Gateway API key and LangFuse API keys:

If you're using the AI Gateway from within a Vercel deployment, you can also use the VERCEL_OIDC_TOKEN environment variable which will be automatically provided.

Create a new file called index.ts with the following code:

Run your application using Node.js:

You should see a response from the AI model in your console.

**Examples**:

```text
mkdir langfuse-ai-gateway
cd langfuse-ai-gateway
pnpm dlx init -y
```

```text
pnpm i langfuse openai dotenv @types/node
```

```text
AI_GATEWAY_API_KEY=your-api-key-here
 
LANGFUSE_PUBLIC_KEY=your_langfuse_public_key
LANGFUSE_SECRET_KEY=your_langfuse_secret_key
LANGFUSE_HOST=https://cloud.langfuse.com
```

---

## LiteLLM

**URL**: https://vercel.com/docs/ai-gateway/framework-integrations/litellm

**Contents**:
- LiteLLM
- Getting started
  - Create a new project
  - Install dependencies
  - Configure environment variables
  - Create your LiteLLM application
  - Running the application

LiteLLM is an open-source library that provides a unified interface to call LLMs. This guide demonstrates how to integrate Vercel AI Gateway with LiteLLM to access various AI models and providers.

First, create a new directory for your project:

Install the required LiteLLM Python package:

Create a .env file with your Vercel AI Gateway API key:

If you're using the AI Gateway from within a Vercel deployment, you can also use the VERCEL_OIDC_TOKEN environment variable which will be automatically provided.

Create a new file called main.py with the following code:

Run your Python application:

You should see a response from the AI model in your console.

**Examples**:

```text
mkdir litellm-ai-gateway
cd litellm-ai-gateway
```

```text
pip install litellm python-dotenv
```

```text
VERCEL_AI_GATEWAY_API_KEY=your-api-key-here
```

---

## LlamaIndex

**URL**: https://vercel.com/docs/ai-gateway/framework-integrations/llamaindex

**Contents**:
- LlamaIndex
- Getting started
  - Create a new project
  - Install dependencies
  - Configure environment variables
  - Create your LlamaIndex application
  - Running the application

LlamaIndex makes it simple to build knowledge assistants using LLMs connected to your enterprise data. This guide demonstrates how to integrate Vercel AI Gateway with LlamaIndex to access various AI models and providers.

First, create a new directory for your project and initialize it:

Install the required LlamaIndex packages along with the python-dotenv package:

Create a .env file with your Vercel AI Gateway API key:

If you're using the AI Gateway from within a Vercel deployment, you can also use the VERCEL_OIDC_TOKEN environment variable which will be automatically provided.

Create a new file called main.py with the following code:

Run your application using Python:

You should see a streaming response from the AI model.

**Examples**:

```text
mkdir llamaindex-ai-gateway
cd llamaindex-ai-gateway
```

```text
pip install llama-index-llms-vercel-ai-gateway llama-index python-dotenv
```

```text
AI_GATEWAY_API_KEY=your-api-key-here
```

---

## Managing Builds

**URL**: https://vercel.com/docs/builds/managing-builds

**Contents**:
- Managing Builds
- Understanding builds using the dashboard
  - Managing build time
  - Number of builds
  - Optimizing builds
- Managing concurrent builds
- Concurrent builds
- On-demand concurrent builds

When you build your application code, Vercel runs compute to install dependencies, run your build script, and upload the build output to our CDN. There are several ways in which you can manage your build compute.

If you are deploying frequently and seeing build queues, you can skip the queue and pay for build compute on demand. You can also handle more builds at the same time by using concurrent builds.

If you need faster build hardware than the default (4 vCPUs and 8 GB of memory), you can purchase enhanced build machines.

The Builds section of the Usage tab shows the following charts:

The Build Time graph shows the ratio of build time vs queued time for all projects across your team on any single day.

Viewing by Projects provides you with a view of the total combined build time and queued time for each project that your team owns.

This chart shows the total number of builds that were triggered for all of the projects on your team, split by a ratio of Completed or Errored.

Viewing by Projects provides you with a view of the total number of builds for each project.

While neither of these metrics are directly chargeable, you can explore concurrent builds and on-demand concurrent builds if you need to run more than one build concurrently.

Some other considerations to take into account when optimizing your builds include:

With simultaneous changes to the same project or branch, your team can face delays with deployments being built when they are placed in a queue. In situations when you cannot wait for the build queue, Vercel provides the following options:

Review Build Queues on Vercel to understand how and when builds get queued.

Concurrent Builds is available on Enterprise and Pro plans

Those with the owner role can access this feature

Generally, when you make multiple deployments in the same Vercel account, the builds get queued, and only one deployment is built at a time. Concurrent Builds allow you to build multiple deployments with Vercel simultane

*[Content truncated - see full docs]*

**Examples**:

```text
curl --request PATCH \
  --url https://api.vercel.com/v9/projects/YOUR_PROJECT_ID?teamId=YOUR_TEAM_ID \
  --header "Authorization: Bearer $VERCEL_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
    "resourceConfig": {
      "elasticConcurrencyEnabled": true,
      "buildMachineType": "enhanced",
    }
  }'
```

```python
import { Vercel } from '@vercel/sdk';
 
const vercel = new Vercel({
  bearerToken: '<YOUR_BEARER_TOKEN_HERE>',
});
 
async function run() {
  const result = await vercel.projects.updateProject({
    idOrName: 'YOUR_PROJECT_ID',
    teamId: 'YOUR_TEAM_ID',
    requestBody: {
      resourceConfig: {
        elasticConcurrencyEnabled: true,
        buildMachineType: 'enhanced',
      },
    },
  });
 
  // Handle the result
  console.log(result);
}
 
run();
```

---

## Mastra

**URL**: https://vercel.com/docs/ai-gateway/framework-integrations/mastra

**Contents**:
- Mastra
- Getting started
  - Create a new Mastra project
  - Install dependencies
  - Configure environment variables
  - Configure your agent to use AI Gateway
  - Running the application

Mastra is a framework for building and deploying AI-powered features using a modern JavaScript stack powered by the Vercel AI SDK. Integrating with AI Gateway provides unified model management and routing capabilities.

First, create a new Mastra project using the CLI:

During the setup, the system prompts you to name your project, choose a default provider, and more. and more. Feel free to use the default settings.

To use the AI Gateway provider, install the @ai-sdk/gateway package along with Mastra:

Create or update your .env file with your Vercel AI Gateway API key:

Now, swap out the @ai-sdk/openai package (or your existing model provider) for the @ai-sdk/gateway package.

Update your agent configuration file, typically src/mastra/agents/weather-agent.ts to the following code:

Since your agent is now configured to use AI Gateway, run the Mastra development server:

Open the Mastra Playground and Mastra API to test your agents, workflows, and tools.

**Examples**:

```text
pnpm dlx create-mastra@latest
```

```text
pnpm i @ai-sdk/gateway mastra @mastra/core @mastra/memory
```

```text
AI_GATEWAY_API_KEY=your-api-key-here
```

---

## Methods to bypass Deployment Protection

**URL**: https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection

**Contents**:
- Methods to bypass Deployment Protection
- Sharable Links
- Protection bypass for Automation
- Deployment Protection Exceptions
- OPTIONS Allowlist
- More resources

To test, share, or exclude specific domains from Deployment Protection, you can use the following methods to allow specific access while maintaining overall security:

Shareable Links are available on all plans

Sharable Links allow external access to specific branch deployments through a secure query parameter. Users with this link can see the latest deployment and leave comments (if enabled and logged in with their Vercel account).

For example, if you generate a Sharable Link for the feature-new-ui branch. Users with this link can view the latest deployment and comment.

Learn more about Sharable Links, and how to generate and revoke them.

Protection Bypass for Automation is available on all plans

For automated tasks like end-to-end (E2E) testing, you can use Protection bypass for Automation. When enabled, it generates a secret that can be used as a System Environment Variable (VERCEL_AUTOMATION_BYPASS_SECRET) to bypass protection features for all deployments in a project.

For example, you set up E2E tests that run on deployments. By using this feature and the generated secret, your tests can bypass the protection mechanisms.

Learn more about Protection bypass for Automation, and how to enable and disable it.

Deployment Protection Exceptions are available on Enterprise plans or with the Advanced Deployment Protection add-on for Pro plans

With Deployment Protection Exceptions you can specify preview domains that should be exempt from deployment protection. Adding a domain to Deployment Protection Exceptions makes it publicly accessible, bypassing features like Vercel Authentication, Password Protection, and Trusted IPs.

For example, if you add preview-branch-name.vercel.app to Deployment Protection Exceptions, this domain becomes publicly accessible, bypassing the project's deployment protection settings. When removed, it reverts to the default protection settings.

Learn more about Deployment Protection Exceptions, and how to add and remove domains.

OPTIO

*[Content truncated - see full docs]*

---

## Model Context Protocol

**URL**: https://vercel.com/docs/mcp

**Contents**:
- Model Context Protocol
- Connecting LLMs to external systems
- Standardizing LLM interaction with MCP
- MCP servers, hosts and clients
- More resources

Model Context Protocol (MCP) is a standard interface that lets large language models (LLMs) communicate with external tools and data sources. It allows developers and tool providers to integrate once and interoperate with any MCP-compatible system.

LLMs don't have access to real-time or external data by default. To provide relevant context—such as current financial data, pricing, or user-specific data—developers must connect LLMs to external systems.

Each tool or service has its own API, schema, and authentication. Managing these differences becomes difficult and error-prone as the number of integrations grows.

MCP standardizes the way LLMs interact with tools and data sources. Developers implement a single integration with MCP, and use it to manage communication with any compatible service.

Tool and data providers only need to expose an MCP interface once. After that, their system can be accessed by any MCP-enabled application.

MCP is like the USB-C standard: instead of needing different connectors for every device, you use one port to handle many types of connections.

MCP uses a client-server architecture for the AI model to external system communication. The user connects to the AI application, referred to as the MCP host, such as IDEs like Cursor, AI chat apps like ChatGPT or AI agents. To connect to external services, the host creates one connection, referred to as the MCP client, to one external service, referred to as the MCP server. Therefore, to connect to multiple MCP servers, one host needs to open and manage multiple MCP clients.

Learn more about Model Context Protocol and explore available MCP servers.

---

## Model Variants

**URL**: https://vercel.com/docs/ai-gateway/model-variants

**Contents**:
- Model Variants
  - Anthropic Claude Sonnet 4: 1M token context (beta)

Some AI inference providers offer special variants of models. These models can have different features such as a larger context size. They may incur different costs associated with requests as well.

When AI Gateway makes these models available they will be highlighted on the model detail page with a Model Variants section in the relevant provider card providing an overview of the feature set and linking to more detail.

Model variants sometimes rely on preview or beta features offered by the inference provider. Their ongoing availability can therefore be less predictable than that of a stable model feature. Check the provider's site for the latest information.

Enable with header anthropic-beta: context-1m-2025-08-07.

**Examples**:

```python
import { streamText } from 'ai';
import { largePrompt } from './largePrompt.ts';
 
const result = streamText({
  headers: {
    'anthropic-beta': 'context-1m-2025-08-07',
  },
  model: 'anthropic/claude-sonnet-4',
  prompt: `You have a big brain. Summarize into 3 sentences: ${largePrompt}`,
  providerOptions: {
    gateway: { only: ['anthropic'] },
  },
});
 
for await (const part of result.textStream) {
  process.stdout.write(part);
}
// Log final chunk with provider metadata detail.
console.lo
...
```

```python
import OpenAI from 'openai';
import { largePrompt } from './largePrompt.ts';
 
const openai = new OpenAI({
  apiKey: process.env.AI_GATEWAY_API_KEY,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});
 
// @ts-expect-error
const stream = await openai.chat.completions.create(
  {
    model: 'anthropic/claude-sonnet-4',
    messages: [
      {
        role: 'user',
        content: `You have a big brain. Summarize into 3 sentences: ${largePrompt}`,
      },
    ],
    stream: true,
    providerOptio
...
```

```python
import json
import os
from openai import OpenAI
 
client = OpenAI(
  api_key=os.getenv('AI_GATEWAY_API_KEY'),
  base_url='https://ai-gateway.vercel.sh/v1'
)
large_prompt = 'your-large-prompt'
 
stream = client.chat.completions.create(
    model='anthropic/claude-sonnet-4',
    messages=[
        {
            'role': 'user',
            'content': f'You have a big brain. Summarize into 3 sentences: {large_prompt}',
        },
    ],
    extra_headers={
        'anthropic-beta': 'context-1m-2025-
...
```

---

## Models & Providers

**URL**: https://vercel.com/docs/ai-gateway/models-and-providers

**Contents**:
- Models & Providers
  - What are models and providers?
  - Specifying the model
    - As part of an AI SDK function call
    - Globally for all requests in your application
  - Embedding models
    - Single value
    - Multiple values

The AI Gateway's unified API is built to be flexible, allowing you to switch between different AI models and providers without rewriting parts of your application. This is useful for testing different models or when you want to change the underlying AI provider for cost or performance reasons.

To view the list of supported models and providers, check out the AI Gateway models page.

Models are AI algorithms that process your input data to generate responses, such as Grok, GPT-5, or Claude Sonnet 4. Providers are the companies or services that host these models, such as xAI, OpenAI, or Anthropic.

In some cases, multiple providers, including the model creator, host the same model. For example, you can use the xai/grok-4 model from xAI or the openai/gpt-5 model from OpenAI, following the format creator/model-name.

Different providers may have different specifications for the same model such as different pricing and performance. You can choose the one that best fits your needs.

You can view the list of supported models and providers by following these steps:

There are two ways to specify the model and provider to use for an AI Gateway request:

In the AI SDK, you can specify the model and provider directly in your API calls using either plain strings or the AI Gateway provider. This allows you to switch models or providers for specific requests without affecting the rest of your application.

To use AI Gateway, specify a model and provider via a plain string, for example:

You can test different models by changing the model parameter and opening your browser to http://localhost:3000/api/chat.

You can also use a provider instance. This can be useful if you'd like to specify custom provider options, or if you'd like to use a Gateway provider with the AI SDK Provider Registry.

Install the @ai-sdk/gateway package directly as a dependency in your project.

You can change the model by changing the string passed to gateway().

The example above uses the default gateway 

*[Content truncated - see full docs]*

**Examples**:

```python
import { generateText } from 'ai';
import { NextRequest } from 'next/server';
 
export async function GET() {
  const result = await generateText({
    model: 'xai/grok-3',
    prompt: 'Tell me the history of the San Francisco Mission-style burrito.',
  });
  return Response.json(result);
}
```

```text
pnpm install @ai-sdk/gateway
```

```python
import { generateText } from 'ai';
import { gateway } from '@ai-sdk/gateway';
import { NextRequest } from 'next/server';
 
export async function GET() {
  const result = await generateText({
    model: gateway('xai/grok-3'),
    prompt: 'Tell me the history of the San Francisco Mission-style burrito.',
  });
  return Response.json(result);
}
```

---

## OPTIONS Allowlist

**URL**: https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/options-allowlist

**Contents**:
- OPTIONS Allowlist
- Enabling OPTIONS Allowlist
  - Go to Project Deployment Protection Settings
  - Enable OPTIONS Allowlist
  - Specify a path
  - Add more paths
  - Save changes
- Disabling OPTIONS Allowlist

OPTIONS Allowlist is available on all plans

You can use OPTIONS Allowlist to disable Deployment Protection (including Vercel Authentication, Password Protection, and Trusted IPs) on any incoming CORS preflight OPTIONS request for a list of paths.

When you add a path to OPTIONS Allowlist, any incoming request with the method OPTIONS that starts with the path will no longer be covered by Deployment Protection. When you remove a path from OPTIONS Allowlist, the path becomes protected again with the project's Deployment Protection settings.

For example, if you specify /api, all requests to paths that start with /api (such as /api/v1/users and /api/v2/projects) will be unprotected for any OPTIONS request.

From your Vercel dashboard:

From the OPTIONS Allowlist section, enable the toggle labelled Disabled:

Specify a path to add to the OPTIONS Allowlist:

To add more paths, select Add path:

Once all the paths are added, select Save

From your Vercel dashboard:

From the OPTIONS Allowlist section, select the toggle labelled Enabled:

Once all the paths are added, select Save

---

## OpenAI-Compatible API

**URL**: https://vercel.com/docs/ai-gateway/openai-compat

**Contents**:
- OpenAI-Compatible API
- Base URL
- Authentication
- Supported endpoints
- Integration with existing tools
  - OpenAI client libraries
  - AI SDK 4
- List models

AI Gateway provides OpenAI-compatible API endpoints, letting you use multiple AI providers through a familiar interface. You can use existing OpenAI client libraries, switch to the AI Gateway with a URL change, and keep your current tools and workflows without code rewrites.

The OpenAI-compatible API implements the same specification as the OpenAI API.

The OpenAI-compatible API is available at the following base URL:

The OpenAI-compatible API supports the same authentication methods as the main AI Gateway:

You only need to use one of these forms of authentication. If an API key is specified it will take precedence over any OIDC token, even if the API key is invalid.

The AI Gateway currently supports the following OpenAI-compatible endpoints:

You can use the AI Gateway's OpenAI-compatible API with existing tools and libraries like the OpenAI client libraries and AI SDK 4. Point your existing client to the AI Gateway's base URL and use your AI Gateway API key or OIDC token for authentication.

For compatibility with AI SDK v4 and AI Gateway, install the @ai-sdk/openai-compatible package.

Verify that you are using AI SDK 4 by using the following package versions: @ai-sdk/openai-compatible version <1.0.0 (e.g., 0.2.16) and ai version <5.0.0 (e.g., 4.3.19).

Retrieve a list of all available models that can be used with the AI Gateway.

The response follows the OpenAI API format:

Retrieve details about a specific model.

Create chat completions using various AI models available through the AI Gateway.

Create a non-streaming chat completion.

Create a streaming chat completion that streams tokens as they are generated.

Streaming responses are sent as Server-Sent Events (SSE), a web standard for real-time data streaming over HTTP. Each event contains a JSON object with the partial response data.

The response format follows the OpenAI streaming specification:

SSE Parsing Libraries:

If you're building custom SSE parsing (instead of using the OpenAI SDK), these li

*[Content truncated - see full docs]*

**Examples**:

```python
import OpenAI from 'openai';
 
const openai = new OpenAI({
  apiKey: process.env.AI_GATEWAY_API_KEY,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});
 
const response = await openai.chat.completions.create({
  model: 'anthropic/claude-sonnet-4',
  messages: [{ role: 'user', content: 'Hello, world!' }],
});
```

```python
import os
from openai import OpenAI
 
client = OpenAI(
    api_key=os.getenv('AI_GATEWAY_API_KEY'),
    base_url='https://ai-gateway.vercel.sh/v1'
)
 
response = client.chat.completions.create(
    model='anthropic/claude-sonnet-4',
    messages=[
        {'role': 'user', 'content': 'Hello, world!'}
    ]
)
```

```python
import { createOpenAICompatible } from '@ai-sdk/openai-compatible';
import { generateText } from 'ai';
 
const gateway = createOpenAICompatible({
  name: 'openai',
  apiKey: process.env.AI_GATEWAY_API_KEY,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});
 
const response = await generateText({
  model: gateway('anthropic/claude-sonnet-4'),
  prompt: 'Hello, world!',
});
```

---

## Pricing

**URL**: https://vercel.com/docs/ai-gateway/pricing

**Contents**:
- Pricing
- Free and paid tiers
  - Free tier
  - Moving to paid tier
- AI Gateway Rates
- Using a custom API key
- View your AI Gateway Credits balance
- Top up your AI Gateway Credits

You only pay for what you use on the AI Gateway by purchasing AI Gateway Credits through the Vercel dashboard. There are no markups to use the AI Gateway, so you're only charged for what your AI providers would bill you if you were using the provider directly.

Charges are automatically deducted from your AI Gateway Credits balance and you can top up the balance at any time.

The AI Gateway offers both a free tier and a paid tier for AI Gateway Credits. For the paid tier, tokens are provided with zero markup, even in the case of bring your own key.

Every Vercel team account includes $5 of free usage per month, giving you the opportunity to explore the AI Gateway without any upfront costs.

You can purchase AI Gateway Credits and move to a paid account on the AI Gateway, enabling you to run larger workloads.

Once you purchase AI Gateway Credits, your account transitions to our pay-as-you-go model:

No matter whether you access the AI Gateway through a free or paid account, you'll pay the AI Gateway rates listed in the Models section of the AI Gateway tab for each request. The AI Gateway's rates are based on the provider's list price. We strive to keep the prices listed in the Model page in the AI Gateway tab of the Vercel dashboard up to date.

The charge for each request depends on the AI provider and model you select, and the number of input and output tokens processed. You're responsible for any payment processing fees that may apply.

The AI Gateway also supports using a custom API key for any provider listed in our catalog. If you use a custom API key, there is no markup or fee from AI Gateway.

To view your balance:

To add AI Gateway Credits:

---

## Production checklist for launch

**URL**: https://vercel.com/docs/production-checklist

**Contents**:
- Production checklist for launch
- Operational excellence
- Security
- Reliability
- Performance
- Cost optimization
- Enterprise support

When launching your application on Vercel, it is important to ensure that it's ready for production. This checklist is prepared by the Vercel engineering team and designed to help you prepare your application for launch by running through a series of questions to ensure:

Define an incident response plan for your team, including escalation paths, communication channels, and rollback strategies for deployments

Familiarize yourself with how to stage, promote and rollback deployments

Ensure caching is configured if deploying using a monorepo to prevent unnecessary builds

Perform a zero downtime migration to Vercel DNS

Implement a Content Security Policy (CSP) and proper security headers

Enable Deployment Protection to prevent unauthorized access to your deployments

Configure the Vercel Web Application Firewall (WAF) to monitor, block, and challenge incoming traffic. This includes setting up custom rules, IP blocking, and enabling managed rulesets for enhanced security

Enable Log Drains to persist logs from your deployments

Review common SSL certificate issues

Enable a Preview Deployment Suffix to use a custom domain for Preview Deployments

Commit your lockfiles to pin dependencies and speed up builds through caching

Consider implementing rate limiting to prevent abuse

Review and implement access roles to ensure the correct permissions are set for your team members

Enable SAML SSO and SCIM (Enterprise plans with Owner role only)

Enable Audit Logs to track and analyze team member activity (Enterprise plans with Owner role only)

Ensure that cookies comply with the allowed cookie policy to enhance security. (Enterprise plans with Owner role only)

Setup a firewall rule to block requests from unwanted bots to your project deployment

Enable Observability Plus to debug and optimize performance, investigate errors, monitor traffic, and more (Available on Pro and Enterprise plans)

Enable automatic Function failover to add multi-region redundancy and protect aga

*[Content truncated - see full docs]*

---

## Protection Bypass for Automation

**URL**: https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/protection-bypass-automation

**Contents**:
- Protection Bypass for Automation
- Who can manage protection bypass for automation?
- Using Protection Bypass for Automation
  - Advanced Configuration
  - Examples
    - Playwright

Protection Bypass for Automation is available on all plans

The Protection Bypass for Automation feature lets you bypass Vercel Deployment Protection (Password Protection, Vercel Authentication, and Trusted IPs) for automated tooling (e.g. E2E testing).

The generated secret can be used to bypass deployment protection on all deployments in a project until it is revoked. This value will also be automatically added to your deployments as a system environment variable VERCEL_AUTOMATION_BYPASS_SECRET.

The environment variable value is set when a deployment is built, so regenerating the secret in the project settings will invalidate previous deployments. You will need to redeploy your app if you update the secret in order to use the new value.

To use Protection Bypass for Automation, set an HTTP header (or query parameter) named x-vercel-protection-bypass with the value of the generated secret for the project.

Using a header is strongly recommended, however in cases where your automation tool is unable to specify a header, it is also possible to set the same name and value as a query parameter.

To bypass authorization on follow-up requests (e.g. for in-browser testing) you can set an additional header or query parameter named x-vercel-set-bypass-cookie with the value true.

This will set the authorization bypass as a cookie using a redirect with a Set-Cookie header.

If you are accessing the deployment through a non-direct way (e.g. in an iframe) then you may need to further configure x-vercel-set-bypass-cookie by setting the value to samesitenone.

This will set SameSite to None on the Set-Cookie header, by default SameSite is set to Lax.

**Examples**:

```typescript
1const config: PlaywrightTestConfig = {2  use: {3    extraHTTPHeaders: {4      'x-vercel-protection-bypass': process.env.VERCEL_AUTOMATION_BYPASS_SECRET,5      'x-vercel-set-bypass-cookie': true | 'samesitenone' (optional)6    }7  }8}
```

---

## Provider Options

**URL**: https://vercel.com/docs/ai-gateway/provider-options

**Contents**:
- Provider Options
- Basic provider ordering
  - Getting started with adding a provider option
  - Install the AI SDK package
  - Configure the provider order in your request
  - Test the routing behavior
- Example provider metadata output
- Restrict providers with the only filter

AI Gateway can route your AI model requests across multiple AI providers. Each provider offers different models, pricing, and performance characteristics. By default, Vercel AI Gateway dynamically chooses the default providers to give you the best experience based on a combination recent uptime and latency.

With the Gateway Provider Options however, you have control over the routing order and fallback behavior of the models.

If you want to customize individual AI model provider settings rather than general AI Gateway behavior, please refer to the model-specific provider options in the AI SDK documentation.

You can use the order array to specify the sequence in which providers should be attempted. Providers are specified using their slug string. You can find the slugs in the table of available providers.

You can also copy the provider slug using the copy button next to a provider's name on a model's detail page. In the Vercel Dashboard:

The bottom section of the page lists the available providers for that model. The copy button next to a provider's name will copy their slug for pasting.

First, ensure you have the necessary package installed:

Use the providerOptions.gateway.order configuration:

You can monitor which provider you used by checking the provider metadata in the response.

The gateway.cost value is the amount debited from your AI Gateway Credits balance for this request. It is returned as a decimal string. For more on pricing see Pricing.

In cases where your request encounters issues with one or more providers or if your BYOK credentials fail, you'll find error detail in the attempts field of the provider metadata:

Use the only array to restrict routing to a specific subset of providers. Providers are specified by their slug and are matched against the model's available providers.

When both only and order are provided, the only filter is applied first to define the allowed set, and then order defines the priority within that filtered set. Practi

*[Content truncated - see full docs]*

**Examples**:

```text
pnpm install ai
```

```python
import { streamText } from 'ai';
 
export async function POST(request: Request) {
  const { prompt } = await request.json();
 
  const result = streamText({
    model: 'anthropic/claude-sonnet-4',
    prompt,
    providerOptions: {
      gateway: {
        order: ['bedrock', 'anthropic'], // Try Amazon Bedrock first, then Anthropic
      },
    },
  });
 
  return result.toUIMessageStreamResponse();
}
```

```python
import { streamText } from 'ai';
 
export async function POST(request: Request) {
  const { prompt } = await request.json();
 
  const result = streamText({
    model: 'anthropic/claude-sonnet-4',
    prompt,
    providerOptions: {
      gateway: {
        order: ['bedrock', 'anthropic'],
      },
    },
  });
 
  // Log which provider was actually used
  console.log(JSON.stringify(await result.providerMetadata, null, 2));
 
  return result.toUIMessageStreamResponse();
}
```

---

## Pydantic AI

**URL**: https://vercel.com/docs/ai-gateway/framework-integrations/pydantic-ai

**Contents**:
- Pydantic AI
- Getting started
  - Create a new project
  - Install dependencies
  - Configure environment variables
  - Create your Pydantic AI application
  - Running the application

Pydantic AI is a Python agent framework designed to make it easy to build production grade applications with AI. This guide demonstrates how to integrate Vercel AI Gateway with Pydantic AI to access various AI models and providers.

First, create a new directory for your project and initialize it:

Install the required Pydantic AI packages along with the python-dotenv package:

Create a .env file with your Vercel AI Gateway API key:

If you're using the AI Gateway from within a Vercel deployment, you can also use the VERCEL_OIDC_TOKEN environment variable which will be automatically provided.

Create a new file called main.py with the following code:

Run your application using Python:

You should see structured city information for Tokyo, Paris, and New York displayed in your console.

**Examples**:

```text
mkdir pydantic-ai-gateway
cd pydantic-ai-gateway
```

```text
pip install pydantic-ai python-dotenv
```

```text
VERCEL_AI_GATEWAY_API_KEY=your-api-key-here
```

---

## SAML Single Sign-On

**URL**: https://vercel.com/docs/saml

**Contents**:
- SAML Single Sign-On
- Configuring SAML SSO
- Enforcing SAML
- Authenticating with SAML SSO
  - Customizing the login page
- De-provisioning team members
- SAML providers

SAML is available on Enterprise and Pro plans

Those with the owner role can access this feature

To manage the members of your team through a third-party identity provider like Okta or Auth0, you can set up the Security Assertion Markup Language (SAML) feature from your team's settings.

Once enabled, all team members will be able to log in or access Preview and Production Deployments using your selected identity provider. Any new users signing up with SAML will automatically be added to your team.

If needed, you can also automatically assign a users Hobby team with a specific role within your team by setting up Directory Sync.

For additional security, SAML SSO can be enforced for a team so that all team members cannot access any team information unless their current session was authenticated with SAML SSO.

When modifying your SAML configuration, the option for enforcing will automatically be turned off. Please verify your new configuration is working correctly by re-authenticating with SAML SSO before re-enabling the option.

Once you have configured SAML, your team members can use SAML SSO to log in or sign up to Vercel. To login:

SAML SSO sessions last for 24 hours before users must re-authenticate with the third-party SAML provider (unless Directory Sync is configured).

You can choose to share a Vercel login page that only shows the option to log in with SAML SSO. This prevents your team members from logging in with an account that's not managed by your identity provider.

To use this page, you can set the saml query param to your team URL. For example:

Vercel is SCIM compliant and therefore when a user is removed from your SAML provider, they are automatically offboarded from Vercel.

Vercel supports the following third-party SAML providers:

**Examples**:

```text
https://vercel.com/login?saml=team_id
```

---

## Sharable Links

**URL**: https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/sharable-links

**Contents**:
- Sharable Links
- Who can create Shareable Links?
- Creating Sharable Links
  - Select your project
  - Select the deployment
  - Click Share button
  - Revoking a Sharable Link
- Managing Shareable Links

Shareable Links are available on all plans

Shareable links allow external users to securely access your deployments through a query string parameter. Shareable links include the ability to leave Comments on deployments which have them enabled.

Users with the Admin, Member, and Developer roles can create or revoke sharable links for their project's deployments. Personal accounts can also manage sharable links for their Hobby deployments.

Developers on the hobby plan can only create one shareable link in total per account.

To manage Sharable Links, do the following:

From your Vercel dashboard:

From the list of Preview Deployments, select the deployment you wish to share.

From the Deployment page, click Share to display the Share popover. From the popover, select Anyone with the link from the dropdown.

To revoke access for users, switch the dropdown option to Only people with access.

If you have also shared the deployment with individual users, you will need to remove them from the Share popover.

You can view and manage all the existing Shareable Links for your team in the following way

---

## Tools

**URL**: https://vercel.com/docs/mcp/vercel-mcp/tools

**Contents**:
- Tools
- Tools
  - Documentation tools
  - Project Management Tools
  - Deployment Tools
  - Domain Management Tools
  - Access Tools
  - CLI Tools

The Vercel MCP server provides the following MCP tools. To enhance security, enable human confirmation for tool execution and exercise caution when using Vercel MCP alongside other servers to prevent prompt injection attacks.

---

## Two-factor Authentication

**URL**: https://vercel.com/docs/two-factor-authentication

**Contents**:
- Two-factor Authentication
- Enabling Two-factor Authentication
  - Configuring an Authenticator App (TOTP)
  - Configuring a Passkey
  - Recovery Codes
- Enforcing Two-Factor Authentication

To add an additional layer of security to your Vercel account, you can enable two-factor authentication (2FA). This feature requires you to provide a second form of verification when logging in to your account. There are two methods available for 2FA on Vercel:

Scan the QR code with your authenticator app or manually enter the provided key. Once added, enter the generated 6-digit code to verify your setup.

See the Login with passkeys for more information on setting up a security key or biometric key.

After setting up two-factor authentication (2FA), you will be prompted to save your recovery codes. Store these codes in a safe place, as they can be used to access your account if you lose access to your 2FA methods.

Each recovery code can only be used once, and you can generate a new set of codes at any time.

Teams can enforce two-factor authentication (2FA) for all members. Once enabled, team members must configure 2FA before accessing team resources. Visit the Two-Factor Enforcement documentation for more information on how to enforce 2FA for your team.

---

## Use Vercel's MCP server

**URL**: https://vercel.com/docs/mcp/vercel-mcp

**Contents**:
- Use Vercel's MCP server
- What is Vercel MCP?
- Available tools
- Connecting to Vercel MCP
- Supported clients
- Setup
  - Claude Code
  - Claude.ai and Claude for desktop

Vercel MCP is available in Beta on all plans and your use is subject to Vercel's Public Beta Agreement and AI Product Terms.

Connect your AI tools to Vercel using the Model Context Protocol (MCP), an open standard that lets AI assistants interact with your Vercel projects.

Vercel MCP is Vercel's official MCP server. It's a remote MCP with OAuth that gives AI tools secure access to your Vercel projects available at:

https://mcp.vercel.com

It integrates with popular AI assistants like Claude, enabling you to:

Vercel MCP implements the latest MCP Authorization and Streamable HTTP specifications.

Vercel MCP provides a comprehensive set of tools for searching documentation and managing your Vercel projects. See the tools reference for detailed information about each available tool and the two main categories: public tools (available without authentication) and authenticated tools (requiring Vercel authentication).

To ensure secure access, Vercel MCP only supports AI clients that have been reviewed and approved by Vercel.

The list of supported AI tools that can connect to Vercel MCP to date:

Additional clients will be added over time.

Connect your AI client to Vercel MCP and authorize access to manage your Vercel projects.

You can add multiple Vercel MCP connections with different names for different projects. For example: vercel-cool-project, vercel-awesome-ai, vercel-super-app, etc.

Custom connectors using remote MCP are available on Claude and Claude Desktop for users on Pro, Max, Team, and Enterprise plans.

Custom connectors using MCP are available on ChatGPT for Pro and Plus accounts on the web.

Follow these steps to set up Vercel as a connector within ChatGPT:

The Vercel connector will appear in the composer's "Developer mode" tool later during conversations.

Click the button above to open Cursor and automatically add Vercel MCP. You can also add the snippet below to your project-specific or global .cursor/mcp.json file manually. For more details, se

*[Content truncated - see full docs]*

**Examples**:

```text
# Install Claude Code
npm install -g @anthropic-ai/claude-code
 
# Navigate to your project
cd your-awesome-project
 
# Add Vercel MCP (general access)
claude mcp add --transport http vercel https://mcp.vercel.com
 
# Add Vercel MCP (project-specific access)
claude mcp add --transport http vercel-awesome-ai https://mcp.vercel.com/my-team/my-awesome-project
 
# Start coding with Claude
claude
 
# Authenticate the MCP tools by typing /mcp
/mcp
```

```text
{
  "mcpServers": {
    "vercel": {
      "url": "https://mcp.vercel.com"
    }
  }
}
```

```text
{
  "mcpServers": {
    "vercel": {
      "serverUrl": "https://mcp.vercel.com"
    }
  }
}
```

---

## Using the Activity Log

**URL**: https://vercel.com/docs/activity-log

**Contents**:
- Using the Activity Log
- When to use the Activity log
- Events logged

Activity Log is available on all plans

The Activity Log provides a list of all events on a Hobby team or team, chronologically organized since its creation. These events include:

Vercel does not emit any logs to third-party services. The Activity Log is only available to the account owner and team members.

Example events list on the Activity page.

Common use cases for viewing the Activity log include:

The table below shows a list of events logged on the Activity page.

---

## Using the REST API

**URL**: https://vercel.com/docs/rest-api

---

## Using the Vercel SDK

**URL**: https://vercel.com/docs/sdk

---

## Vercel Agent Overview

**URL**: https://vercel.com/docs/agent/overview

**Contents**:
- Vercel Agent Overview
- How to setup Vercel Agent on your repositories
- Pricing
- Privacy
- Files analyzed
- Usage

Vercel Agent is available in Beta on Enterprise and Pro plans

Vercel Agent is an AI code reviewer for speeding up your development process. It sits in your repository and for every PR it analyzes your PR diff, reproduces issues in secure sandboxes, generates and validates proposed fixes, and lets you apply them. Key features include:

To enable code reviews for your repositories, navigate to the Agent tab of the dashboard.

Vercel Agent is now enabled for your team and will automatically review pull requests in repositories connected to your Vercel projects.

Vercel Agent is charged on a credit basis. You can purchase Vercel Agent credit in the Agent tab of your Vercel dashboard. This pricing is usage based and composed of two components:

The token cost is based on the number of tokens the model uses to generate each review, which varies based on the code complexity, file types, and depth of analysis required. You can track your realtime spending in the Agent tab of your Vercel dashboard or read more about usage.

Vercel Agent does not store or train on any of your data. It only uses LLMs from providers on our subprocessor list, and we have agreements in place that do not allow them to train on your data.

When performing code review, Vercel Agent has access to the entire codebase as context and analyzes all human-readable files including but not limited to:

Check out the Usage page for more details on how to configure and monitor your Vercel Agent reviews along with detailed usage metrics and analytics.

---

## Vercel Agent Usage

**URL**: https://vercel.com/docs/agent/usage

**Contents**:
- Vercel Agent Usage
- Customize what repositories are reviewed
- Monitor your reviews and spending

The Agent tab in your Vercel dashboard provides custom configuration options and detailed usage metrics that help you monitor reviews, spending, and performance across your repositories.

When Vercel Agent is enabled for your team, it will automatically review pull requests in repositories connected to Vercel projects in that team. You can also configure the following options:

Vercel Agent exposes the following observability details for each pull request:

You can also export this data to CSV for deeper analysis or reporting.

---

## Vercel Deep Infra IntegrationNative Integration

**URL**: https://vercel.com/docs/ai/deepinfra

**Contents**:
- Vercel Deep Infra IntegrationNative Integration
- Use cases
  - Available models
  - Some available models on Deep Infra
- Getting started
  - Prerequisites
  - Add the provider to your project
    - Using the dashboard

Deep Infra provides scalable and cost-effective infrastructure for deploying and managing machine learning models. It's optimized for reduced latency and low costs compared to traditional cloud providers.

This integration gives you access to the large selection of available AI models and allows you to manage your tokens, billing and usage directly from Vercel.

You can use the Vercel and Deep Infra integration to:

Deep Infra provides a diverse range of AI models designed for high-performance tasks for a variety of applications.

A generative text model

A generative text model

A generative text model

Llama 3.1 8B Instruct Turbo

Llama 3.1 is an auto-regressive language model that uses an optimized transformer architecture.

Llama 3.3 70B Instruct Turbo

Llama 3.3 is an auto-regressive language model that uses an optimized transformer architecture.

DeepSeek R1 Distill Llama 70B

A generative text model

Llama 4 Maverick 17B 128E Instruct

Meta's advanced natively multimodal model with a 17B parameter mixture-of-experts architecture (128 experts) that enables sophisticated text and image understanding, supporting 12 languages.

Llama 4 Scout 17B 16E Instruct

Meta's natively multimodal model with a 17B parameter mixture-of-experts architecture that enables text and image understanding, supporting 12 languages.

The Vercel Deep Infra integration can be accessed through the AI tab on your Vercel dashboard.

To follow this guide, you'll need the following:

Learn more about Deep Infra by visiting their website.

Learn more about Deep Infra pricing.

Visit the Deep Infra documentation.

Visit the Deep Infra AI SDK reference page.

**Examples**:

```text
pnpm i -g vercel@latest
```

```text
vercel env pull
```

```text
pnpm i @ai-sdk/deepinfra ai
```

---

## Vercel Documentation

**URL**: https://vercel.com/docs

**Contents**:
- Vercel Documentation
- Get started with Vercel
- Build your applications
- Use Vercel's AI infrastructure
- Collaborate with your team
- Secure your applications
- Deploy and scale

Vercel is the AI Cloud for building and deploying modern web applications, from static sites to AI-powered agents.

You can build and host many different types of applications on Vercel, static sites with your favorite framework, multi-tenant applications, or microfrontends, to AI-powered agents.

You can also use the Vercel Marketplace to find and install integrations such as AI providers, databases, CMSs, analytics, storage, and more.

When you are ready to build, connect your Git repository to deploy on every push, with automatic preview environments for testing changes before production.

See the getting started guide for more information, or the incremental migration guide for a step-by-step guide to migrating your existing application to Vercel.

Use one or more of the following tools to build your application depending on your needs:

Add intelligence to your applications with Vercel's AI-first infrastructure:

Collaborate with your team using the following tools:

Secure your applications with the following tools:

Vercel handles infrastructure automatically based on your framework and code, and provides the following tools to help you deploy and scale your applications:

---

## Vercel ElevenLabs IntegrationConnectable Account

**URL**: https://vercel.com/docs/ai/elevenlabs

**Contents**:
- Vercel ElevenLabs IntegrationConnectable Account
- Use cases
  - Available models
  - Some available models on ElevenLabs
- Getting started
  - Prerequisites
  - Add the provider to your project
    - Using the dashboard

ElevenLabs specializes in advanced voice synthesis and audio processing technologies. Its integration with Vercel allows you to incorporate realistic voice and audio enhancements into your applications, ideal for creating interactive media experiences.

You can use the Vercel and ElevenLabs integration to power a variety of AI applications, including:

ElevenLabs offers models that specialize in advanced voice synthesis and audio processing, delivering natural-sounding speech and audio enhancements suitable for various interactive media applications.

The highest quality English text-to-speech model.

The original ElevenLabs English text-to-speech model.

Eleven Multilingual v1

A multilingual text-to-speech model. This has been surpassed by the Eleven Multilingual v2 model.

Eleven Multilingual v2

A multilingual text-to-speech model that supports 28 languages.

The fastest text-to-speech model. Only English is supported.

A highly optimized, low-latency text-to-speech model supporting 32 languages.

The Vercel ElevenLabs integration can be accessed through the AI tab on your Vercel dashboard.

To follow this guide, you'll need the following:

Learn more about ElevenLabs by visiting their website.

Learn more about ElevenLabs pricing.

Visit the ElevenLabs documentation.

**Examples**:

```text
pnpm i -g vercel@latest
```

```text
vercel env pull
```

```text
pnpm i @elevenlabs/elevenlabs-js
```

---

## Vercel Groq IntegrationNative Integration

**URL**: https://vercel.com/docs/ai/groq

**Contents**:
- Vercel Groq IntegrationNative Integration
- Use cases
  - Available models
  - Some available models on Groq
- Getting started
  - Prerequisites
  - Add the provider to your project
    - Using the dashboard

Groq is a high-performance AI inference service with an ultra-fast Language Processing Unit (LPU) architecture. It enables fast response times for language model inference, making it ideal for applications requiring low latency.

You can use the Vercel and Groq integration to:

Groq provides a diverse range of AI models designed for high-performance tasks.

DeepSeek R1 Distill Llama 70B

A generative text model

Distil Whisper Large V3 English

A distilled, or compressed, version of OpenAI's Whisper model, designed to provide faster, lower cost English speech recognition while maintaining comparable accuracy.

A fast and efficient language model for text generation.

Mistral Saba 24B is a specialized model trained to excel in Arabic, Farsi, Urdu, Hebrew, and Indic languages. Designed for high-performance multilingual capabilities, it delivers exceptional results across a wide range of tasks in these languages while maintaining strong performance in English. With a 32K token context window and tool use capabilities, it's ideal for complex multilingual applications requiring deep language understanding and regional context.

Qwen QWQ 32B is a powerful large language model with strong reasoning capabilities and versatile applications across various tasks.

A state-of-the-art model for automatic speech recognition (ASR) and speech translation, trained on 1M hours of weakly labeled and 4M hours of pseudo-labeled audio. Supports 99 languages with improved accuracy over previous versions.

Whisper Large V3 Turbo

A faster version of Whisper Large V3 with reduced decoding layers (4 instead of 32), providing significantly improved speed with minimal quality degradation. Supports 99 languages for speech recognition and translation.

Llama 3.3 70B Instruct Turbo

Meta's Llama 3.3 is an auto-regressive language model that uses an optimized transformer architecture. Supports 128K context length and multilingual processing.

Llama 4 Scout 17B 16E Instruct

Meta's natively multimo

*[Content truncated - see full docs]*

**Examples**:

```text
pnpm i -g vercel@latest
```

```text
vercel env pull
```

```text
pnpm i @ai-sdk/groq ai
```

---

## Vercel LMNT IntegrationConnectable Account

**URL**: https://vercel.com/docs/ai/lmnt

**Contents**:
- Vercel LMNT IntegrationConnectable Account
- Use cases
- Getting started
  - Prerequisites
  - Add the provider to your project
    - Using the dashboard
- More resources
  - LMNT Website

LMNT provides data processing and predictive analytics models, known for their precision and efficiency. Integrating LMNT with Vercel enables your applications to offer accurate insights and forecasts, particularly useful in finance and healthcare sectors.

You can use the Vercel and LMNT integration to power a variety of AI applications, including:

The Vercel LMNT integration can be accessed through the AI tab on your Vercel dashboard.

To follow this guide, you'll need the following:

Learn more about LMNT by visiting their website.

Learn more about LMNT pricing.

Visit the LMNT documentation.

**Examples**:

```text
pnpm i -g vercel@latest
```

```text
vercel env pull
```

```text
pnpm i lmnt-node
```

---

## Vercel & OpenAI Integration

**URL**: https://vercel.com/docs/ai/openai

**Contents**:
- Vercel & OpenAI Integration
- Getting started
- Getting Your OpenAI API Key
  - Navigate to API Keys
  - Generate API Key
  - Set Environment Variable
- Building chat interfaces with the AI SDK
- Using OpenAI Functions with Vercel

Vercel integrates with OpenAI to enable developers to build fast, scalable, and secure AI applications.

You can integrate with any OpenAI model using the AI SDK, including the following OpenAI models:

To help you get started, we have built a variety of AI templates integrating OpenAI with Vercel.

Vercel Postgres pgvector Starter

A Next.js template that uses Vercel Postgres as the database, pgvector for vector similarity search + OpenAI's text embedding models.

A full-featured, hackable Next.js AI chatbot built by Vercel

Before you begin, ensure you have an OpenAI account. Once registered:

Log into your OpenAI Dashboard and view API keys.

Click on Create new secret key. Copy the generated API key securely.

Always keep your API keys confidential. Do not expose them in client-side code. Use Vercel Environment Variables for safe storage and do not commit these values to git.

Finally, add the OPENAI_API_KEY environment variable in your project:

Integrating OpenAI into your Vercel project is seamless with the AI SDK.

Install the AI SDK in your project with your favorite package manager:

You can use the SDK to build AI applications with React (Next.js), Vue (Nuxt), Svelte (SvelteKit), and Node.js.

The AI SDK also has full support for OpenAI Functions (tool calling).

Learn more about using tools with the AI SDK.

**Examples**:

```text
OPENAI_API_KEY='sk-...3Yu5'
```

---

## Vercel Perplexity IntegrationConnectable Account

**URL**: https://vercel.com/docs/ai/perplexity

**Contents**:
- Vercel Perplexity IntegrationConnectable Account
- Use cases
  - Available models
  - Some available models on Perplexity API
- Getting started
  - Prerequisites
  - Add the provider to your project
    - Using the dashboard

Perplexity API specializes in providing accurate, real-time answers to user questions by combining AI-powered search with large language models, delivering concise, well-sourced, and conversational responses. Integrating Perplexity via its Sonar API with Vercel allows your applications to deliver real-time, web-wide research and question-answering capabilities—complete with accurate citations, customizable sources, and advanced reasoning—enabling users to access up-to-date, trustworthy information directly within your product experience.

You can use the Vercel and Perplexity integration to power a variety of AI applications, including:

The Sonar models are each optimized for tasks such as real-time search, advanced reasoning, and in-depth research. Please refer to Perplexity's list of available models here.

Perplexity's premier offering with search grounding, supporting advanced queries and follow-ups.

Perplexity's lightweight offering with search grounding, quicker and cheaper than Sonar Pro.

The Vercel Perplexity API integration can be accessed through the AI tab on your Vercel dashboard.

To follow this guide, you'll need the following:

Learn more about Perplexity API by visiting their website.

Learn more about Perplexity API pricing.

Visit the Perplexity API documentation.

**Examples**:

```text
pnpm i -g vercel@latest
```

```text
vercel env pull
```

```text
pnpm i @ai-sdk/perplexity ai
```

---

## Vercel Pinecone IntegrationConnectable Account

**URL**: https://vercel.com/docs/ai/pinecone

**Contents**:
- Vercel Pinecone IntegrationConnectable Account
  - What is a vector database?
- Use cases
- Getting started
  - Prerequisites
  - Add the provider to your project
    - Using the dashboard
- Deploy a template

Pinecone is a vector database service that handles the storage and search of complex data. With Pinecone, you can use machine-learning models for content recommendation systems, personalized search, image recognition, and more. The Vercel Pinecone integration allows you to deploy your models to Vercel and use them in your applications.

A vector database is a database that stores and searches for vectors. In this context, a vector represents a data point mathematically, often termed as an embedding.

An embedding is data that's converted to an array of numbers (a vector). The combination of the numbers that make up the vector form a multi-dimensional map used in comparison to other vectors to determine similarity.

Take the below example of two vectors, one for an image of a cat and one for an image of a dog. In the cat's vector, the first element is 0.1, and in the dog's vector 0.2. This similarity and difference in values illustrate how vector comparison works. The closer the values are to each other, the more similar the vectors are.

You can use the Vercel and Pinecone integration to power a variety of AI applications, including:

The Vercel Pinecone integration can be accessed through the AI tab on your Vercel dashboard.

To follow this guide, you'll need the following:

You can deploy a template to Vercel that includes a pre-trained model and a sample application that uses the model:

Pinecone - Vercel AI SDK Starter

A Next.js starter chatbot using Vercel's AI SDK and implements the Retrieval-Augmented Generation (RAG) pattern with Pinecone

Learn more about Pinecone by visiting their website.

Learn more about Pinecone pricing.

Visit the Pinecone documentation.

**Examples**:

```text
// Example of a vector for an image of a cat
[0.1, 0.2, 0.3, 0.4, 0.5];
// Example of a vector for an image of a dog
[(0.2, 0.3, 0.4, 0.5, 0.6)];
```

```text
pnpm i -g vercel@latest
```

```text
vercel env pull
```

---

## Vercel Primitives

**URL**: https://vercel.com/docs/build-output-api/primitives

**Contents**:
- Vercel Primitives
- Static files
  - Configuration
  - Directory structure for static files
- Serverless Functions
  - Serverless function configuration
    - Base config
    - Node.js config

The following directories, code files, and configuration files represent all Vercel platform primitives. These primitives are the "building blocks" that make up a Vercel Deployment.

Files outside of these directories are ignored and will not be served to visitors.

.vercel/output/static

vercel/examples/build-output-api/static-files

Static files that are publicly accessible from the Deployment URL should be placed in the .vercel/output/static directory.

These files are served with the Vercel Edge CDN.

Files placed within this directory will be made available at the root (/) of the Deployment URL and neither their contents, nor their file name or extension will be modified in any way. Sub directories within static are also retained in the URL, and are appended before the file name.

There is no standalone configuration file that relates to static files.

However, certain properties of static files (such as the Content-Type response header) can be modified by utilizing the overrides property of the config.json file.

The following example shows static files placed into the .vercel/output/static directory:

.vercel/output/functions

vercel/examples/build-output-api/serverless-functions

A Vercel Function is represented on the file system as a directory with a .func suffix on the name, contained within the .vercel/output/functions directory.

Conceptually, you can think of this .func directory as a filesystem mount for a Vercel Function: the files below the .func directory are included (recursively) and files above the .func directory are not included. Private files may safely be placed within this directory because they will not be directly accessible to end-users. However, they can be referenced by code that will be executed by the Vercel Function.

A .func directory may be a symlink to another .func directory in cases where you want to have more than one path point to the same underlying Vercel Function.

A configuration file named .vc-config.json must be include

*[Content truncated - see full docs]*

**Examples**:

```text
type ServerlessFunctionConfig = {
  handler: string;
  runtime: string;
  memory?: number;
  maxDuration?: number;
  environment: Record<string, string>[];
  regions?: string[];
  supportsWrapper?: boolean;
  supportsResponseStreaming?: boolean;
};
```

```text
type NodejsServerlessFunctionConfig = ServerlessFunctionConfig & {
  launcherType: 'Nodejs';
  shouldAddHelpers?: boolean; // default: false
  shouldAddSourcemapSupport?: boolean; // default: false
};
```

```text
{
  "runtime": "nodejs22.x",
  "handler": "serve.js",
  "maxDuration": 3,
  "launcherType": "Nodejs",
  "shouldAddHelpers": true,
  "shouldAddSourcemapSupport": true
}
```

---

## Vercel Replicate IntegrationConnectable Account

**URL**: https://vercel.com/docs/ai/replicate

**Contents**:
- Vercel Replicate IntegrationConnectable Account
- Use cases
  - Available models
  - Some available models on Replicate
- Getting started
  - Prerequisites
  - Add the provider to your project
    - Using the dashboard

Replicate provides a platform for accessing and deploying a wide range of open-source artificial intelligence models. These models span various AI applications such as image and video processing, natural language processing, and audio synthesis. With the Vercel Replicate integration, you can incorporate these AI capabilities into your applications, enabling advanced functionalities and enhancing user experiences.

You can use the Vercel and Replicate integration to power a variety of AI applications, including:

Replicate models cover a broad spectrum of AI applications ranging from image and video processing to natural language processing and audio synthesis.

Generate image captions

Faster, better FLUX Pro. Text-to-image model with excellent image quality, prompt adherence, and output diversity.

A 12 billion parameter rectified flow transformer capable of generating images from text descriptions

State-of-the-art image generation with top of the line prompt following, visual quality, image detail and output diversity.

The fastest image generation model tailored for local development and personal use

An excellent image model with state of the art inpainting, prompt comprehension and text rendering

A fast image model with state of the art inpainting, prompt comprehension and text rendering.

Incredibly Fast Whisper

whisper-large-v3, incredibly fast, powered by Hugging Face Transformers.

A 70 billion parameter language model from Meta, fine tuned for chat completions

An 8 billion parameter language model from Meta, fine tuned for chat completions

Llama 3.1 405B Instruct

Meta's flagship 405 billion parameter language model, fine-tuned for chat completions

Visual instruction tuning towards large language and vision models with GPT-4 level capabilities

Moondream2 is a small vision language model designed to run efficiently on edge devices

Recraft V3 (code-named red_panda) is a text-to-image model with the ability to generate long texts, and images in a wide

*[Content truncated - see full docs]*

**Examples**:

```text
pnpm i -g vercel@latest
```

```text
vercel env pull
```

```text
pnpm i replicate
```

---

## Vercel Together AI IntegrationConnectable Account

**URL**: https://vercel.com/docs/ai/togetherai

**Contents**:
- Vercel Together AI IntegrationConnectable Account
- Use cases
  - Available models
  - Some available models on Together AI
- Getting started
  - Prerequisites
  - Add the provider to your project
    - Using the dashboard

Together AI offers models for interactive AI experiences, focusing on collaborative and real-time engagement. Integrating Together AI with Vercel empowers your applications with enhanced user interaction and co-creative functionalities.

You can use the Vercel and Together AI integration to power a variety of AI applications, including:

Together AI offers models that specialize in collaborative and interactive AI experiences. These models are adept at facilitating real-time interaction, enhancing user engagement, and supporting co-creative processes.

Nous Hermes 2 - Mixtral 8x7B-DPO

Nous Hermes 2 Mixtral 8x7B DPO is the new flagship Nous Research model trained over the Mixtral 8x7B MoE LLM.

Llama 3.1 70B Instruct Turbo

Llama 3.1 is an auto-regressive language model that uses an optimized transformer architecture.

Llama 3.1 8B Instruct Turbo

Llama 3.1 is an auto-regressive language model that uses an optimized transformer architecture.

Llama 3.1 405B Instruct Turbo

Llama 3.1 is an auto-regressive language model that uses an optimized transformer architecture.

Llama 3.2 3B Instruct Turbo

Llama 3.2 is an auto-regressive language model that uses an optimized transformer architecture.

Llama-3.3-70b-Instruct-Turbo

The Meta Llama 3.3 multilingual large language model (LLM) is a pretrained and instruction tuned generative model in 70B (text in/text out).

Mistral 7B Instruct v0.3

The Mistral 7B Instruct v0.3 Large Language Model (LLM) is an instruct fine-tuned version of the Mistral 7B v0.3.

A variant of Mythomix proficient at both roleplaying and storywriting.

The Vercel Together AI integration can be accessed through the AI tab on your Vercel dashboard.

To follow this guide, you'll need the following:

Learn more about Together AI by visiting their website.

Learn more about Together AI pricing.

Visit the Together AI documentation.

**Examples**:

```text
pnpm i -g vercel@latest
```

```text
vercel env pull
```

```text
pnpm i @ai-sdk/togetherai ai
```

---

## Vercel fal IntegrationNative Integration

**URL**: https://vercel.com/docs/ai/fal

**Contents**:
- Vercel fal IntegrationNative Integration
- Use cases
  - Available models
  - Some available models on fal
- Getting started
  - Prerequisites
  - Add the provider to your project
    - Using the dashboard

fal enables the development of real-time AI applications with a focus on rapid inference speeds, achieving response times under ~120ms. Specializing in diffusion models, fal has no cold starts and a pay-for-what-you-use pricing model.

You can use the Vercel and fal integration to power a variety of AI applications, including:

fal provides a diverse range of AI models designed for high-performance tasks in image and text processing.

Run SDXL at the speed of light

Create creative upscaled images.

FLUX.1 [dev] with LoRAs

Super fast endpoint for the FLUX.1 [dev] model with LoRA support, enabling rapid and high-quality image generation using pre-trained LoRA adaptations for personalization, specific styles, brand identities, and product-specific outputs.

Run SDXL at the speed of light

Veo creates videos with realistic motion and high quality output. Explore different styles and find your own with extensive camera controls.

Wan-2.1 Image to Video

Wan-2.1 generates high-quality videos with excellent visual quality and motion diversity from still images. Bring your photos to life with natural, fluid movement.

The Vercel fal integration can be accessed through the AI tab on your Vercel dashboard.

To follow this guide, you'll need the following:

Learn more about fal by visiting their website.

Learn more about fal pricing.

Visit the fal documentation.

Visit the fal AI SDK reference page.

**Examples**:

```text
pnpm i -g vercel@latest
```

```text
vercel env pull
```

```text
pnpm i @fal-ai/client
```

---

## Vercel xAI IntegrationNative Integration

**URL**: https://vercel.com/docs/ai/xai

**Contents**:
- Vercel xAI IntegrationNative Integration
- Use cases
  - Available models
  - Some available models on xAI
- Getting started
  - Prerequisites
  - Add the provider to your project
    - Using the dashboard

xAI provides language, chat and vision AI capabilities with integrated billing through Vercel.

You can use the Vercel and xAI integration to:

xAI provides language and language with vision AI models.

Grok-2 is a large language model that can be used for a variety of tasks, including text generation, translation, and question answering.

Grok-2 Vision is a multimodal AI model that combines advanced language understanding with powerful visual processing capabilities.

A text-to-image model that can generate high-quality images across several domains where other image generation models often struggle. It can render precise visual details of real-world entities, text, logos, and can create realistic portraits of humans.

xAI's flagship model that excels at enterprise use cases like data extraction, coding, and text summarization. Possesses deep domain knowledge in finance, healthcare, law, and science.

xAI's flagship model that excels at enterprise use cases like data extraction, coding, and text summarization. Possesses deep domain knowledge in finance, healthcare, law, and science. Fast mode delivers reduced latency and a quicker time-to-first-token.

xAI's flagship model that excels at enterprise use cases like data extraction, coding, and text summarization. Possesses deep domain knowledge in finance, healthcare, law, and science. Fast mode delivers reduced latency and a quicker time-to-first-token. Mini is a lightweight model that thinks before responding. Great for simple or logic-based tasks that do not require deep domain knowledge. The raw thinking traces are accessible.

Grok-3 Mini Fast Beta

xAI's flagship model that excels at enterprise use cases like data extraction, coding, and text summarization. Possesses deep domain knowledge in finance, healthcare, law, and science. Fast mode delivers reduced latency and a quicker time-to-first-token. Mini is a lightweight model that thinks before responding. Fast mode delivers reduced latency and a quicker time-t

*[Content truncated - see full docs]*

**Examples**:

```text
pnpm i -g vercel@latest
```

```text
vercel env pull
```

```text
pnpm i @ai-sdk/xai ai
```

---
