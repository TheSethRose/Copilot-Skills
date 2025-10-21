# Ai-Sdk - Integrations

**Pages**: 3

---

## AI SDK UI

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-ui

**Contents**:
- AI SDK UI
- UI Framework Support

AI SDK UI is designed to help you build interactive chat, completion, and assistant applications with ease. It is framework-agnostic toolkit, streamlining the integration of advanced AI functionalities into your applications.

AI SDK UI contains the following hooks:

AI SDK UI supports the following frameworks: React, Svelte, and Vue.js. Here is a comparison of the supported functions across these frameworks:

Contributions are welcome to implement missing features for non-React frameworks.

---

## AI SDK

**URL**: https://ai-sdk.dev/docs/

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

## experimental_useObject()

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-ui/use-object

**Contents**:
- experimental_useObject()
- Import
- API Signature
  - Parameters
  - api:
  - schema:
  - id?:
  - initialValue?:

useObject is an experimental feature and only available in React, Svelte, and Vue.

Allows you to consume text streams that represent a JSON object and parse them into a complete object based on a schema. You can use it together with streamObject in the backend.

**Examples**:

```tsx
'use client';
import { experimental_useObject as useObject } from '@ai-sdk/react';
export default function Page() {  const { object, submit } = useObject({    api: '/api/use-object',    schema: z.object({ content: z.string() }),  });
  return (    <div>      <button onClick={() => submit('example input')}>Generate</button>      {object?.content && <p>{object.content}</p>}    </div>  );}
```

```tsx
'use client';
import { experimental_useObject as useObject } from '@ai-sdk/react';
export default function Page() {  const { object, submit } = useObject({    api: '/api/use-object',    schema: z.object({ content: z.string() }),  });
  return (    <div>      <button onClick={() => submit('example input')}>Generate</button>      {object?.content && <p>{object.content}</p>}    </div>  );}
```

```python
import { experimental_useObject as useObject } from '@ai-sdk/react'
```

---
