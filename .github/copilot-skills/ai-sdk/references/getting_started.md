# Ai-Sdk - Getting Started

**Pages**: 8

---

## AI SDK

**URL**: https://ai-sdk.dev/docs/introduction

**Contents**:
- AI SDK
- Why use the AI SDK?
- Model Providers
- Templates
  - Starter Kits
  - Feature Exploration
  - Frameworks
  - Generative UI

The AI SDK is the TypeScript toolkit designed to help developers build AI-powered applications and agents with React, Next.js, Vue, Svelte, Node.js, and more.

Integrating large language models (LLMs) into applications is complicated and heavily dependent on the specific model provider you use.

The AI SDK standardizes integrating artificial intelligence (AI) models across supported providers. This enables developers to focus on building great AI applications, not waste time on technical details.

For example, here’s how you can generate text with various models using the AI SDK:

The AI SDK has two main libraries:

The AI SDK supports multiple model providers.

We've built some templates that include AI SDK integrations for different use cases, providers, and frameworks. You can use these templates to get started with your AI-powered application.

If you have questions about anything related to the AI SDK, you're always welcome to ask our community on GitHub Discussions.

You can access the entire AI SDK documentation in Markdown format at ai-sdk.dev/llms.txt. This can be used to ask any LLM (assuming it has a big enough context window) questions about the AI SDK based on the most up-to-date documentation.

For instance, to prompt an LLM with questions about the AI SDK:

**Examples**:

```prompt
Documentation:{paste documentation here}---Based on the above documentation, answer the following:{your question}
```

```prompt
Documentation:{paste documentation here}---Based on the above documentation, answer the following:{your question}
```

---

## Expo Quickstart

**URL**: https://ai-sdk.dev/docs/getting-started/expo

**Contents**:
- Expo Quickstart
- Prerequisites
- Create Your Application
  - Install dependencies
  - Configure OpenAI API key
- Create an API Route
- Wire up the UI
  - Create the API URL Generator

In this quickstart tutorial, you'll build a simple AI-chatbot with a streaming user interface with Expo. Along the way, you'll learn key concepts and techniques that are fundamental to using the SDK in your own projects.

If you are unfamiliar with the concepts of Prompt Engineering and HTTP Streaming, you can optionally read these documents first.

To follow this quickstart, you'll need:

If you haven't obtained your OpenAI API key, you can do so by signing up on the OpenAI website.

Start by creating a new Expo application. This command will create a new directory named my-ai-app and set up a basic Expo application inside it.

Navigate to the newly created directory:

Install ai, @ai-sdk/react and @ai-sdk/openai, the AI package, the AI React package and AI SDK's OpenAI provider respectively.

The AI SDK is designed to be a unified interface to interact with any large language model. This means that you can change model and providers with just one line of code! Learn more about available providers and building custom providers in the providers section.

Create a .env.local file in your project root and add your OpenAI API Key. This key is used to authenticate your application with the OpenAI service.

Edit the .env.local file:

Replace xxxxxxxxx with your actual OpenAI API key.

The AI SDK's OpenAI Provider will default to using the OPENAI_API_KEY environment variable.

Create a route handler, app/api/chat+api.ts and add the following code:

Let's take a look at what is happening in this code:

This API route creates a POST request endpoint at /api/chat.

Now that you have an API route that can query an LLM, it's time to setup your frontend. The AI SDK's UI package abstracts the complexity of a chat interface into one hook, useChat.

Update your root page (app/(tabs)/index.tsx) with the following code to show a list of chat messages and provide a user message input:

This page utilizes the useChat hook, which will, by default, use the POST API route you created ear

*[Content truncated - see full docs]*

**Examples**:

```text
pnpm create expo-app@latest my-ai-app
```

```text
cd my-ai-app
```

```text
pnpm add ai @ai-sdk/openai @ai-sdk/react zod
```

---

## Next.js App Router Quickstart

**URL**: https://ai-sdk.dev/docs/getting-started/nextjs-app-router

**Contents**:
- Next.js App Router Quickstart
- Prerequisites
- Create Your Application
  - Install dependencies
  - Configure OpenAI API key
- Create a Route Handler
- Wire up the UI
- Running Your Application

The AI SDK is a powerful Typescript library designed to help developers build AI-powered applications.

In this quickstart tutorial, you'll build a simple AI-chatbot with a streaming user interface. Along the way, you'll learn key concepts and techniques that are fundamental to using the SDK in your own projects.

If you are unfamiliar with the concepts of Prompt Engineering and HTTP Streaming, you can optionally read these documents first.

To follow this quickstart, you'll need:

If you haven't obtained your OpenAI API key, you can do so by signing up on the OpenAI website.

Start by creating a new Next.js application. This command will create a new directory named my-ai-app and set up a basic Next.js application inside it.

Be sure to select yes when prompted to use the App Router and Tailwind CSS. If you are looking for the Next.js Pages Router quickstart guide, you can find it here.

Navigate to the newly created directory:

Install ai, @ai-sdk/react, and @ai-sdk/openai, the AI package, AI SDK's React hooks, and AI SDK's OpenAI provider respectively.

The AI SDK is designed to be a unified interface to interact with any large language model. This means that you can change model and providers with just one line of code! Learn more about available providers and building custom providers in the providers section.

Create a .env.local file in your project root and add your OpenAI API Key. This key is used to authenticate your application with the OpenAI service.

Edit the .env.local file:

Replace xxxxxxxxx with your actual OpenAI API key.

The AI SDK's OpenAI Provider will default to using the OPENAI_API_KEY environment variable.

Create a route handler, app/api/chat/route.ts and add the following code:

Let's take a look at what is happening in this code:

This Route Handler creates a POST request endpoint at /api/chat.

Now that you have a Route Handler that can query an LLM, it's time to setup your frontend. The AI SDK's UI package abstracts the complexity of a

*[Content truncated - see full docs]*

**Examples**:

```text
pnpm create next-app@latest my-ai-app
```

```text
cd my-ai-app
```

```text
pnpm add ai @ai-sdk/react @ai-sdk/openai zod
```

---

## Next.js Pages Router Quickstart

**URL**: https://ai-sdk.dev/docs/getting-started/nextjs-pages-router

**Contents**:
- Next.js Pages Router Quickstart
- Prerequisites
- Setup Your Application
  - Install dependencies
  - Configure OpenAI API key
- Create a Route Handler
- Wire up the UI
- Running Your Application

The AI SDK is a powerful Typescript library designed to help developers build AI-powered applications.

In this quickstart tutorial, you'll build a simple AI-chatbot with a streaming user interface. Along the way, you'll learn key concepts and techniques that are fundamental to using the SDK in your own projects.

If you are unfamiliar with the concepts of Prompt Engineering and HTTP Streaming, you can optionally read these documents first.

To follow this quickstart, you'll need:

If you haven't obtained your OpenAI API key, you can do so by signing up on the OpenAI website.

Start by creating a new Next.js application. This command will create a new directory named my-ai-app and set up a basic Next.js application inside it.

Be sure to select no when prompted to use the App Router. If you are looking for the Next.js App Router quickstart guide, you can find it here.

Navigate to the newly created directory:

Install ai, @ai-sdk/react, and @ai-sdk/openai, the AI package, AI SDK's React hooks, and AI SDK's OpenAI provider respectively.

The AI SDK is designed to be a unified interface to interact with any large language model. This means that you can change model and providers with just one line of code! Learn more about available providers and building custom providers in the providers section.

Create a .env.local file in your project root and add your OpenAI API Key. This key is used to authenticate your application with the OpenAI service.

Edit the .env.local file:

Replace xxxxxxxxx with your actual OpenAI API key.

The AI SDK's OpenAI Provider will default to using the OPENAI_API_KEY environment variable.

As long as you are on Next.js 13+, you can use Route Handlers (using the App Router) alongside the Pages Router. This is recommended to enable you to use the Web APIs interface/signature and to better support streaming.

Create a Route Handler (app/api/chat/route.ts) and add the following code:

Let's take a look at what is happening in this code:

This Rou

*[Content truncated - see full docs]*

**Examples**:

```text
pnpm create next-app@latest my-ai-app
```

```text
cd my-ai-app
```

```text
pnpm add ai @ai-sdk/react @ai-sdk/openai zod
```

---

## Node.js Quickstart

**URL**: https://ai-sdk.dev/docs/getting-started/nodejs

**Contents**:
- Node.js Quickstart
- Prerequisites
- Setup Your Application
  - Install Dependencies
  - Configure OpenAI API key
- Create Your Application
- Running Your Application
- Enhance Your Chatbot with Tools

The AI SDK is a powerful Typescript library designed to help developers build AI-powered applications.

In this quickstart tutorial, you'll build a simple AI-chatbot with a streaming user interface. Along the way, you'll learn key concepts and techniques that are fundamental to using the SDK in your own projects.

If you are unfamiliar with the concepts of Prompt Engineering and HTTP Streaming, you can optionally read these documents first.

To follow this quickstart, you'll need:

If you haven't obtained your OpenAI API key, you can do so by signing up on the OpenAI website.

Start by creating a new directory using the mkdir command. Change into your new directory and then run the pnpm init command. This will create a package.json in your new directory.

Install ai and @ai-sdk/openai, the AI SDK's OpenAI provider, along with other necessary dependencies.

The AI SDK is designed to be a unified interface to interact with any large language model. This means that you can change model and providers with just one line of code! Learn more about available providers and building custom providers in the providers section.

The ai and @ai-sdk/openai packages contain the AI SDK and the AI SDK OpenAI provider, respectively. You will use zod to define type-safe schemas that you will pass to the large language model (LLM). You will use dotenv to access environment variables (your OpenAI key) within your application. There are also three development dependencies, installed with the -D flag, that are necessary to run your Typescript code.

Create a .env file in your project's root directory and add your OpenAI API Key. This key is used to authenticate your application with the OpenAI service.

Replace xxxxxxxxx with your actual OpenAI API key.

The AI SDK's OpenAI Provider will default to using the OPENAI_API_KEY environment variable.

Create an index.ts file in the root of your project and add the following code:

Let's take a look at what is happening in this code:

With that, 

*[Content truncated - see full docs]*

**Examples**:

```bash
mkdir my-ai-appcd my-ai-apppnpm init
```

```bash
mkdir my-ai-appcd my-ai-apppnpm init
```

```bash
pnpm add ai@beta @ai-sdk/openai@beta zod dotenvpnpm add -D @types/node tsx typescript
```

---

## Overview

**URL**: https://ai-sdk.dev/docs/foundations/overview

**Contents**:
- Overview
- Generative Artificial Intelligence
- Large Language Models
- Embedding Models

This page is a beginner-friendly introduction to high-level artificial intelligence (AI) concepts. To dive right into implementing the AI SDK, feel free to skip ahead to our quickstarts or learn about our supported models and providers.

The AI SDK standardizes integrating artificial intelligence (AI) models across supported providers. This enables developers to focus on building great AI applications, not waste time on technical details.

For example, here’s how you can generate text with various models using the AI SDK:

To effectively leverage the AI SDK, it helps to familiarize yourself with the following concepts:

Generative artificial intelligence refers to models that predict and generate various types of outputs (such as text, images, or audio) based on what’s statistically likely, pulling from patterns they’ve learned from their training data. For example:

A large language model (LLM) is a subset of generative models focused primarily on text. An LLM takes a sequence of words as input and aims to predict the most likely sequence to follow. It assigns probabilities to potential next sequences and then selects one. The model continues to generate sequences until it meets a specified stopping criterion.

LLMs learn by training on massive collections of written text, which means they will be better suited to some use cases than others. For example, a model trained on GitHub data would understand the probabilities of sequences in source code particularly well.

However, it's crucial to understand LLMs' limitations. When asked about less known or absent information, like the birthday of a personal relative, LLMs might "hallucinate" or make up information. It's essential to consider how well-represented the information you need is in the model.

An embedding model is used to convert complex data (like words or images) into a dense vector (a list of numbers) representation, known as an embedding. Unlike generative models, embedding models do not generate new text

*[Content truncated - see full docs]*

---

## Svelte Quickstart

**URL**: https://ai-sdk.dev/docs/getting-started/svelte

**Contents**:
- Svelte Quickstart
- Prerequisites
- Set Up Your Application
  - Install Dependencies
  - Configure OpenAI API Key
- Create an API route
- Wire up the UI
- Running Your Application

The AI SDK is a powerful Typescript library designed to help developers build AI-powered applications.

In this quickstart tutorial, you'll build a simple AI-chatbot with a streaming user interface. Along the way, you'll learn key concepts and techniques that are fundamental to using the SDK in your own projects.

If you are unfamiliar with the concepts of Prompt Engineering and HTTP Streaming, you can optionally read these documents first.

To follow this quickstart, you'll need:

If you haven't obtained your OpenAI API key, you can do so by signing up on the OpenAI website.

Start by creating a new SvelteKit application. This command will create a new directory named my-ai-app and set up a basic SvelteKit application inside it.

Navigate to the newly created directory:

Install ai and @ai-sdk/openai, the AI SDK's OpenAI provider.

The AI SDK is designed to be a unified interface to interact with any large language model. This means that you can change model and providers with just one line of code! Learn more about available providers and building custom providers in the providers section.

Create a .env.local file in your project root and add your OpenAI API Key. This key is used to authenticate your application with the OpenAI service.

Edit the .env.local file:

Replace xxxxxxxxx with your actual OpenAI API key.

Vite does not automatically load environment variables onto process.env, so you'll need to import OPENAI_API_KEY from $env/static/private in your code (see below).

Create a SvelteKit Endpoint, src/routes/api/chat/+server.ts and add the following code:

If you see type errors with OPENAI_API_KEY or your POST function, run the dev server.

Let's take a look at what is happening in this code:

Now that you have an API route that can query an LLM, it's time to set up your frontend. The AI SDK's UI package abstracts the complexity of a chat interface into one class, Chat. Its properties and API are largely the same as React's useChat.

Update your root pag

*[Content truncated - see full docs]*

**Examples**:

```text
npx sv create my-ai-app
```

```text
cd my-ai-app
```

```text
pnpm add -D ai @ai-sdk/openai @ai-sdk/svelte zod
```

---

## Vue.js (Nuxt) Quickstart

**URL**: https://ai-sdk.dev/docs/getting-started/nuxt

**Contents**:
- Vue.js (Nuxt) Quickstart
- Prerequisites
- Setup Your Application
  - Install dependencies
  - Configure OpenAI API key
- Create an API route
- Wire up the UI
- Running Your Application

The AI SDK is a powerful Typescript library designed to help developers build AI-powered applications.

In this quickstart tutorial, you'll build a simple AI-chatbot with a streaming user interface. Along the way, you'll learn key concepts and techniques that are fundamental to using the SDK in your own projects.

If you are unfamiliar with the concepts of Prompt Engineering and HTTP Streaming, you can optionally read these documents first.

To follow this quickstart, you'll need:

If you haven't obtained your OpenAI API key, you can do so by signing up on the OpenAI website.

Start by creating a new Nuxt application. This command will create a new directory named my-ai-app and set up a basic Nuxt application inside it.

Navigate to the newly created directory:

Install ai and @ai-sdk/openai, the AI SDK's OpenAI provider.

The AI SDK is designed to be a unified interface to interact with any large language model. This means that you can change model and providers with just one line of code! Learn more about available providers and building custom providers in the providers section.

Create a .env file in your project root and add your OpenAI API Key. This key is used to authenticate your application with the OpenAI service.

Replace xxxxxxxxx with your actual OpenAI API key and configure the environment variable in nuxt.config.ts:

The AI SDK's OpenAI Provider will default to using the OPENAI_API_KEY environment variable.

Create an API route, server/api/chat.ts and add the following code:

Let's take a look at what is happening in this code:

Now that you have an API route that can query an LLM, it's time to setup your frontend. The AI SDK's UI package abstract the complexity of a chat interface into one hook, useChat.

Update your root page (pages/index.vue) with the following code to show a list of chat messages and provide a user message input:

If your project has app.vue instead of pages/index.vue, delete the app.vue file and create a new pages/index.vue file 

*[Content truncated - see full docs]*

**Examples**:

```text
pnpm create nuxt my-ai-app
```

```text
cd my-ai-app
```

```text
pnpm add ai @ai-sdk/openai @ai-sdk/vue zod
```

---
