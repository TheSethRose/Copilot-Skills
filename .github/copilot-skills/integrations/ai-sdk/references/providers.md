# Ai-Sdk - Providers

**Pages**: 2

---

## Multi-Modal Agent

**URL**: https://ai-sdk.dev/docs/guides/multi-modal-chatbot

**Contents**:
- Multi-Modal Agent
- Prerequisites
- Create Your Application
  - Install dependencies
  - Configure OpenAI API key
- Implementation Plan
- Create a Route Handler
- Wire up the UI

In this guide, you will build a multi-modal agent capable of understanding both images and PDFs.

Multi-modal refers to the ability of the agent to understand and generate responses in multiple formats. In this guide, we'll focus on images and PDFs - two common document types that modern language models can process natively.

For a complete list of providers and their multi-modal capabilities, visit the providers documentation.

We'll build this agent using OpenAI's GPT-4o, but the same code works seamlessly with other providers - you can switch between them by changing just one line of code.

To follow this quickstart, you'll need:

If you haven't obtained your OpenAI API key, you can do so by signing up on the OpenAI website.

Start by creating a new Next.js application. This command will create a new directory named multi-modal-agent and set up a basic Next.js application inside it.

Be sure to select yes when prompted to use the App Router. If you are looking for the Next.js Pages Router quickstart guide, you can find it here.

Navigate to the newly created directory:

Install ai and @ai-sdk/openai, the AI SDK package and the AI SDK's OpenAI provider respectively.

The AI SDK is designed to be a unified interface to interact with any large language model. This means that you can change model and providers with just one line of code! Learn more about available providers and building custom providers in the providers section.

Create a .env.local file in your project root and add your OpenAI API Key. This key is used to authenticate your application with the OpenAI service.

Edit the .env.local file:

Replace xxxxxxxxx with your actual OpenAI API key.

The AI SDK's OpenAI Provider will default to using the OPENAI_API_KEY environment variable.

To build a multi-modal agent, you will need to:

Create a route handler, app/api/chat/route.ts and add the following code:

Let's take a look at what is happening in this code:

This Route Handler creates a POST request endp

*[Content truncated - see full docs]*

**Examples**:

```text
pnpm create next-app@latest multi-modal-agent
```

```text
cd multi-modal-agent
```

```text
pnpm add ai @ai-sdk/react @ai-sdk/openai
```

---

## Providers and Models

**URL**: https://ai-sdk.dev/docs/foundations/providers-and-models

**Contents**:
- Providers and Models
- AI SDK Providers
- Self-Hosted Models
- Model Capabilities

Companies such as OpenAI and Anthropic (providers) offer access to a range of large language models (LLMs) with differing strengths and capabilities through their own APIs.

Each provider typically has its own unique method for interfacing with their models, complicating the process of switching providers and increasing the risk of vendor lock-in.

To solve these challenges, AI SDK Core offers a standardized approach to interacting with LLMs through a language model specification that abstracts differences between providers. This unified interface allows you to switch between providers with ease while using the same API for all providers.

Here is an overview of the AI SDK Provider Architecture:

The AI SDK comes with a wide range of providers that you can use to interact with different language models:

You can also use the OpenAI Compatible provider with OpenAI-compatible APIs:

Our language model specification is published as an open-source package, which you can use to create custom providers.

The open-source community has created the following providers:

You can access self-hosted models with the following providers:

Additionally, any self-hosted provider that supports the OpenAI specification can be used with the OpenAI Compatible Provider.

The AI providers support different language models with various capabilities. Here are the capabilities of popular models:

This table is not exhaustive. Additional models can be found in the provider documentation pages and on the provider websites.

---
