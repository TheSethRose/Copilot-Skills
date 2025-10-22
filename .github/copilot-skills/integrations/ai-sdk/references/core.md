# Ai-Sdk - Core

**Pages**: 77

---

## AI_NoContentGeneratedError

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-errors/ai-no-content-generated-error

**Contents**:
- AI_NoContentGeneratedError
- Properties
- Checking for this Error

This error occurs when the AI provider fails to generate content.

You can check if an error is an instance of AI_NoContentGeneratedError using:

**Examples**:

```typescript
import { NoContentGeneratedError } from 'ai';
if (NoContentGeneratedError.isInstance(error)) {  // Handle the error}
```

```typescript
import { NoContentGeneratedError } from 'ai';
if (NoContentGeneratedError.isInstance(error)) {  // Handle the error}
```

---

## AI_NoImageGeneratedError

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-errors/ai-no-image-generated-error

**Contents**:
- AI_NoImageGeneratedError
- Properties
- Checking for this Error

This error occurs when the AI provider fails to generate an image. It can arise due to the following reasons:

You can check if an error is an instance of AI_NoImageGeneratedError using:

**Examples**:

```typescript
import { generateImage, NoImageGeneratedError } from 'ai';
try {  await generateImage({ model, prompt });} catch (error) {  if (NoImageGeneratedError.isInstance(error)) {    console.log('NoImageGeneratedError');    console.log('Cause:', error.cause);    console.log('Responses:', error.responses);  }}
```

```typescript
import { generateImage, NoImageGeneratedError } from 'ai';
try {  await generateImage({ model, prompt });} catch (error) {  if (NoImageGeneratedError.isInstance(error)) {    console.log('NoImageGeneratedError');    console.log('Cause:', error.cause);    console.log('Responses:', error.responses);  }}
```

---

## AI_NoObjectGeneratedError

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-errors/ai-no-object-generated-error

**Contents**:
- AI_NoObjectGeneratedError
- Properties
- Checking for this Error

This error occurs when the AI provider fails to generate a parsable object that conforms to the schema. It can arise due to the following reasons:

You can check if an error is an instance of AI_NoObjectGeneratedError using:

**Examples**:

```typescript
import { generateObject, NoObjectGeneratedError } from 'ai';
try {  await generateObject({ model, schema, prompt });} catch (error) {  if (NoObjectGeneratedError.isInstance(error)) {    console.log('NoObjectGeneratedError');    console.log('Cause:', error.cause);    console.log('Text:', error.text);    console.log('Response:', error.response);    console.log('Usage:', error.usage);    console.log('Finish Reason:', error.finishReason);  }}
```

```typescript
import { generateObject, NoObjectGeneratedError } from 'ai';
try {  await generateObject({ model, schema, prompt });} catch (error) {  if (NoObjectGeneratedError.isInstance(error)) {    console.log('NoObjectGeneratedError');    console.log('Cause:', error.cause);    console.log('Text:', error.text);    console.log('Response:', error.response);    console.log('Usage:', error.usage);    console.log('Finish Reason:', error.finishReason);  }}
```

---

## AI_NoSpeechGeneratedError

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-errors/ai-no-speech-generated-error

**Contents**:
- AI_NoSpeechGeneratedError
- Properties
- Checking for this Error

This error occurs when no audio could be generated from the input.

You can check if an error is an instance of AI_NoSpeechGeneratedError using:

**Examples**:

```typescript
import { NoSpeechGeneratedError } from 'ai';
if (NoSpeechGeneratedError.isInstance(error)) {  // Handle the error}
```

```typescript
import { NoSpeechGeneratedError } from 'ai';
if (NoSpeechGeneratedError.isInstance(error)) {  // Handle the error}
```

---

## AI_NoTranscriptGeneratedError

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-errors/ai-no-transcript-generated-error

**Contents**:
- AI_NoTranscriptGeneratedError
- Properties
- Checking for this Error

This error occurs when no transcript could be generated from the input.

You can check if an error is an instance of AI_NoTranscriptGeneratedError using:

**Examples**:

```typescript
import { NoTranscriptGeneratedError } from 'ai';
if (NoTranscriptGeneratedError.isInstance(error)) {  // Handle the error}
```

```typescript
import { NoTranscriptGeneratedError } from 'ai';
if (NoTranscriptGeneratedError.isInstance(error)) {  // Handle the error}
```

---

## AI SDK Core

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-core

**Contents**:
- AI SDK Core

AI SDK Core is a set of functions that allow you to interact with language models and other AI models. These functions are designed to be easy-to-use and flexible, allowing you to generate text, structured data, and embeddings from language models and other AI models.

AI SDK Core contains the following main functions:

It also contains the following helper functions:

---

## AI SDK Core

**URL**: https://ai-sdk.dev/docs/ai-sdk-core/overview

**Contents**:
- AI SDK Core
- AI SDK Core Functions
- API Reference

Large Language Models (LLMs) are advanced programs that can understand, create, and engage with human language on a large scale. They are trained on vast amounts of written material to recognize patterns in language and predict what might come next in a given piece of text.

AI SDK Core simplifies working with LLMs by offering a standardized way of integrating them into your app - so you can focus on building great AI applications for your users, not waste time on technical details.

For example, here’s how you can generate text with various models using the AI SDK:

AI SDK Core has various functions designed for text generation, structured data generation, and tool usage. These functions take a standardized approach to setting up prompts and settings, making it easier to work with different models.

Please check out the AI SDK Core API Reference for more details on each function.

---

## AI SDK Core

**URL**: https://ai-sdk.dev/docs/ai-sdk-core

**Contents**:
- AI SDK Core

---

## Abort breaks resumable streams

**URL**: https://ai-sdk.dev/docs/troubleshooting/abort-breaks-resumable-streams

**Contents**:
- Abort breaks resumable streams
- Issue
- Background
- Current limitations
  - Option 1: Use stream resumption without abort
  - Option 2: Use abort without stream resumption
- Related

When using useChat with resume: true for stream resumption, the abort functionality breaks. Closing a tab, refreshing the page, or calling the stop() function will trigger an abort signal that interferes with the resumption mechanism, preventing streams from being properly resumed.

When a page is closed or refreshed, the browser automatically sends an abort signal, which breaks the resumption flow.

We're aware of this incompatibility and are exploring solutions. In the meantime, please choose either stream resumption or abort functionality based on your application's requirements, but not both.

If you need to support long-running generations that persist across page reloads:

If you need to allow users to stop streams manually:

**Examples**:

```tsx
// This configuration will cause conflictsconst { messages, stop } = useChat({  id: chatId,  resume: true, // Stream resumption enabled});
// Closing the tab will trigger abort and stop resumption
```

```tsx
// This configuration will cause conflictsconst { messages, stop } = useChat({  id: chatId,  resume: true, // Stream resumption enabled});
// Closing the tab will trigger abort and stop resumption
```

```tsx
const { messages, sendMessage } = useChat({  id: chatId,  resume: true,});
```

---

## Chatbot Resume Streams

**URL**: https://ai-sdk.dev/docs/ai-sdk-ui/chatbot-resume-streams

**Contents**:
- Chatbot Resume Streams
- How stream resumption works
- Prerequisites
- Implementation
  - 1. Client-side: Enable stream resumption
  - 2. Create the POST handler
  - 3. Implement the GET handler
- How it works

useChat supports resuming ongoing streams after page reloads. Use this feature to build applications with long-running generations.

Stream resumption is not compatible with abort functionality. Closing a tab or refreshing the page triggers an abort signal that will break the resumption mechanism. Do not use resume: true if you need abort functionality in your application. See troubleshooting for more details.

Stream resumption requires persistence for messages and active streams in your application. The AI SDK provides tools to connect to storage, but you need to set up the storage yourself.

To implement resumable streams in your chat application, you need:

Use the resume option in the useChat hook to enable stream resumption. When resume is true, the hook automatically attempts to reconnect to any active stream for the chat on mount:

You must send the chat ID with each request (see prepareSendMessagesRequest).

When you enable resume, the useChat hook makes a GET request to /api/chat/[id]/stream on mount to check for and resume any active streams.

Let's start by creating the POST handler to create the resumable stream.

The POST handler creates resumable streams using the consumeSseStream callback:

Create a GET handler at /api/chat/[id]/stream that:

The after function from Next.js allows work to continue after the response has been sent. This ensures that the resumable stream persists in Redis even after the initial response is returned to the client, enabling reconnection later.

The diagram above shows the complete lifecycle of a resumable stream:

By default, the useChat hook makes a GET request to /api/chat/[id]/stream when resuming. Customize this endpoint, credentials, and headers, using the prepareReconnectToStreamRequest option in DefaultChatTransport:

**Examples**:

```tsx
'use client';
import { useChat } from '@ai-sdk/react';import { DefaultChatTransport, type UIMessage } from 'ai';
export function Chat({  chatData,  resume = false,}: {  chatData: { id: string; messages: UIMessage[] };  resume?: boolean;}) {  const { messages, sendMessage, status } = useChat({    id: chatData.id,    messages: chatData.messages,    resume, // Enable automatic stream resumption    transport: new DefaultChatTransport({      // You must send the id of the chat      prepareSendMessage
...
```

```tsx
'use client';
import { useChat } from '@ai-sdk/react';import { DefaultChatTransport, type UIMessage } from 'ai';
export function Chat({  chatData,  resume = false,}: {  chatData: { id: string; messages: UIMessage[] };  resume?: boolean;}) {  const { messages, sendMessage, status } = useChat({    id: chatData.id,    messages: chatData.messages,    resume, // Enable automatic stream resumption    transport: new DefaultChatTransport({      // You must send the id of the chat      prepareSendMessage
...
```

```ts
import { openai } from '@ai-sdk/openai';import { readChat, saveChat } from '@util/chat-store';import {  convertToModelMessages,  generateId,  streamText,  type UIMessage,} from 'ai';import { after } from 'next/server';import { createResumableStreamContext } from 'resumable-stream';
export async function POST(req: Request) {  const {    message,    id,  }: {    message: UIMessage | undefined;    id: string;  } = await req.json();
  const chat = await readChat(id);  let messages = chat.messages;
 
...
```

---

## Completion

**URL**: https://ai-sdk.dev/docs/ai-sdk-ui/completion

**Contents**:
- Completion
- Example
- Customized UI
  - Loading and error states
  - Controlled input
  - Cancelation
  - Throttling UI Updates
- Event Callbacks

The useCompletion hook allows you to create a user interface to handle text completions in your application. It enables the streaming of text completions from your AI provider, manages the state for chat input, and updates the UI automatically as new messages are received.

The useCompletion hook is now part of the @ai-sdk/react package.

In this guide, you will learn how to use the useCompletion hook in your application to generate text completions and stream them in real-time to your users.

In the Page component, the useCompletion hook will request to your AI provider endpoint whenever the user submits a message. The completion is then streamed back in real-time and displayed in the UI.

This enables a seamless text completion experience where the user can see the AI response as soon as it is available, without having to wait for the entire response to be received.

useCompletion also provides ways to manage the prompt via code, show loading and error states, and update messages without being triggered by user interactions.

To show a loading spinner while the chatbot is processing the user's message, you can use the isLoading state returned by the useCompletion hook:

Similarly, the error state reflects the error object thrown during the fetch request. It can be used to display an error message, or show a toast notification:

In the initial example, we have handleSubmit and handleInputChange callbacks that manage the input changes and form submissions. These are handy for common use cases, but you can also use uncontrolled APIs for more advanced scenarios such as form validation or customized components.

The following example demonstrates how to use more granular APIs like setInput with your custom input and submit button components:

It's also a common use case to abort the response message while it's still streaming back from the AI provider. You can do this by calling the stop function returned by the useCompletion hook.

When the user clicks the "Stop" butt

*[Content truncated - see full docs]*

**Examples**:

```tsx
'use client';
import { useCompletion } from '@ai-sdk/react';
export default function Page() {  const { completion, input, handleInputChange, handleSubmit } = useCompletion({    api: '/api/completion',  });
  return (    <form onSubmit={handleSubmit}>      <input        name="prompt"        value={input}        onChange={handleInputChange}        id="input"      />      <button type="submit">Submit</button>      <div>{completion}</div>    </form>  );}
```

```tsx
'use client';
import { useCompletion } from '@ai-sdk/react';
export default function Page() {  const { completion, input, handleInputChange, handleSubmit } = useCompletion({    api: '/api/completion',  });
  return (    <form onSubmit={handleSubmit}>      <input        name="prompt"        value={input}        onChange={handleInputChange}        id="input"      />      <button type="submit">Submit</button>      <div>{completion}</div>    </form>  );}
```

```ts
import { streamText } from 'ai';import { openai } from '@ai-sdk/openai';
// Allow streaming responses up to 30 secondsexport const maxDuration = 30;
export async function POST(req: Request) {  const { prompt }: { prompt: string } = await req.json();
  const result = streamText({    model: openai('gpt-3.5-turbo'),    prompt,  });
  return result.toUIMessageStreamResponse();}
```

---

## Embeddings

**URL**: https://ai-sdk.dev/docs/ai-sdk-core/embeddings

**Contents**:
- Embeddings
- Embedding a Single Value
- Embedding Many Values
- Embedding Similarity
- Token Usage
- Settings
  - Provider Options
  - Parallel Requests

Embeddings are a way to represent words, phrases, or images as vectors in a high-dimensional space. In this space, similar words are close to each other, and the distance between words can be used to measure their similarity.

The AI SDK provides the embed function to embed single values, which is useful for tasks such as finding similar words or phrases or clustering text. You can use it with embeddings models, e.g. openai.textEmbeddingModel('text-embedding-3-large') or mistral.textEmbeddingModel('mistral-embed').

When loading data, e.g. when preparing a data store for retrieval-augmented generation (RAG), it is often useful to embed many values at once (batch embedding).

The AI SDK provides the embedMany function for this purpose. Similar to embed, you can use it with embeddings models, e.g. openai.textEmbeddingModel('text-embedding-3-large') or mistral.textEmbeddingModel('mistral-embed').

After embedding values, you can calculate the similarity between them using the cosineSimilarity function. This is useful to e.g. find similar words or phrases in a dataset. You can also rank and filter related items based on their similarity.

Many providers charge based on the number of tokens used to generate embeddings. Both embed and embedMany provide token usage information in the usage property of the result object:

Embedding model settings can be configured using providerOptions for provider-specific parameters:

The embedMany function now supports parallel processing with configurable maxParallelCalls to optimize performance:

Both embed and embedMany accept an optional maxRetries parameter of type number that you can use to set the maximum number of retries for the embedding process. It defaults to 2 retries (3 attempts in total). You can set it to 0 to disable retries.

Both embed and embedMany accept an optional abortSignal parameter of type AbortSignal that you can use to abort the embedding process or set a timeout.

Both embed and embedMany accept an optional 

*[Content truncated - see full docs]*

**Examples**:

```tsx
import { embed } from 'ai';import { openai } from '@ai-sdk/openai';
// 'embedding' is a single embedding object (number[])const { embedding } = await embed({  model: openai.textEmbeddingModel('text-embedding-3-small'),  value: 'sunny day at the beach',});
```

```tsx
import { embed } from 'ai';import { openai } from '@ai-sdk/openai';
// 'embedding' is a single embedding object (number[])const { embedding } = await embed({  model: openai.textEmbeddingModel('text-embedding-3-small'),  value: 'sunny day at the beach',});
```

```tsx
import { openai } from '@ai-sdk/openai';import { embedMany } from 'ai';
// 'embeddings' is an array of embedding objects (number[][]).// It is sorted in the same order as the input values.const { embeddings } = await embedMany({  model: openai.textEmbeddingModel('text-embedding-3-small'),  values: [    'sunny day at the beach',    'rainy afternoon in the city',    'snowy night in the mountains',  ],});
```

---

## Error Handling

**URL**: https://ai-sdk.dev/docs/ai-sdk-core/error-handling

**Contents**:
- Error Handling
- Handling regular errors
- Handling streaming errors (simple streams)
- Handling streaming errors (streaming with error support)
- Handling stream aborts

Regular errors are thrown and can be handled using the try/catch block.

See Error Types for more information on the different types of errors that may be thrown.

When errors occur during streams that do not support error chunks, the error is thrown as a regular error. You can handle these errors using the try/catch block.

Full streams support error parts. You can handle those parts similar to other parts. It is recommended to also add a try-catch block for errors that happen outside of the streaming.

When streams are aborted (e.g., via chat stop button), you may want to perform cleanup operations like updating stored messages in your UI. Use the onAbort callback to handle these cases.

The onAbort callback is called when a stream is aborted via AbortSignal, but onFinish is not called. This ensures you can still update your UI state appropriately.

The onAbort callback receives:

You can also handle abort events directly in the stream:

**Examples**:

```ts
import { generateText } from 'ai';
try {  const { text } = await generateText({    model: 'openai/gpt-4.1',    prompt: 'Write a vegetarian lasagna recipe for 4 people.',  });} catch (error) {  // handle error}
```

```ts
import { generateText } from 'ai';
try {  const { text } = await generateText({    model: 'openai/gpt-4.1',    prompt: 'Write a vegetarian lasagna recipe for 4 people.',  });} catch (error) {  // handle error}
```

```ts
import { generateText } from 'ai';
try {  const { textStream } = streamText({    model: 'openai/gpt-4.1',    prompt: 'Write a vegetarian lasagna recipe for 4 people.',  });
  for await (const textPart of textStream) {    process.stdout.write(textPart);  }} catch (error) {  // handle error}
```

---

## Experimental_StdioMCPTransport

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-core/mcp-stdio-transport

**Contents**:
- Experimental_StdioMCPTransport
- Import
- API Signature
  - Parameters
  - config:
  - command:
  - args?:
  - env?:

Creates a transport for Model Context Protocol (MCP) clients to communicate with MCP servers using standard input and output streams. This transport is only supported in Node.js environments.

This feature is experimental and may change or be removed in the future.

**Examples**:

```python
import { Experimental_StdioMCPTransport } from "ai/mcp-stdio"
```

---

## Generating Structured Data

**URL**: https://ai-sdk.dev/docs/ai-sdk-core/generating-structured-data

**Contents**:
- Generating Structured Data
- Generate Object
  - Accessing response headers & body
- Stream Object
  - onError callback
- Output Strategy
  - Object
  - Array

While text generation can be useful, your use case will likely call for generating structured data. For example, you might want to extract information from text, classify data, or generate synthetic data.

Many language models are capable of generating structured data, often defined as using "JSON modes" or "tools". However, you need to manually provide schemas and then validate the generated data as LLMs can produce incorrect or incomplete structured data.

The AI SDK standardises structured object generation across model providers with the generateObject and streamObject functions. You can use both functions with different output strategies, e.g. array, object, enum, or no-schema, and with different generation modes, e.g. auto, tool, or json. You can use Zod schemas, Valibot, or JSON schemas to specify the shape of the data that you want, and the AI model will generate data that conforms to that structure.

You can pass Zod objects directly to the AI SDK functions or use the zodSchema helper function.

The generateObject generates structured data from a prompt. The schema is also used to validate the generated data, ensuring type safety and correctness.

See generateObject in action with these examples

Sometimes you need access to the full response from the model provider, e.g. to access some provider-specific headers or body content.

You can access the raw response headers and body using the response property:

Given the added complexity of returning structured data, model response time can be unacceptable for your interactive use case. With the streamObject function, you can stream the model's response as it is generated.

You can use streamObject to stream generated UIs in combination with React Server Components (see Generative UI)) or the useObject hook.

streamObject immediately starts streaming. Errors become part of the stream and are not thrown to prevent e.g. servers from crashing.

To log errors, you can provide an onError callback that is triggered w

*[Content truncated - see full docs]*

**Examples**:

```ts
import { generateObject } from 'ai';import { z } from 'zod';
const { object } = await generateObject({  model: 'openai/gpt-4.1',  schema: z.object({    recipe: z.object({      name: z.string(),      ingredients: z.array(z.object({ name: z.string(), amount: z.string() })),      steps: z.array(z.string()),    }),  }),  prompt: 'Generate a lasagna recipe.',});
```

```ts
import { generateObject } from 'ai';import { z } from 'zod';
const { object } = await generateObject({  model: 'openai/gpt-4.1',  schema: z.object({    recipe: z.object({      name: z.string(),      ingredients: z.array(z.object({ name: z.string(), amount: z.string() })),      steps: z.array(z.string()),    }),  }),  prompt: 'Generate a lasagna recipe.',});
```

```ts
import { generateObject } from 'ai';
const result = await generateObject({  // ...});
console.log(JSON.stringify(result.response.headers, null, 2));console.log(JSON.stringify(result.response.body, null, 2));
```

---

## Generating and Streaming Text

**URL**: https://ai-sdk.dev/docs/ai-sdk-core/generating-text

**Contents**:
- Generating and Streaming Text
- generateText
  - Accessing response headers & body
- streamText
  - onError callback
  - onChunk callback
  - onFinish callback
  - fullStream property

Large language models (LLMs) can generate text in response to a prompt, which can contain instructions and information to process. For example, you can ask a model to come up with a recipe, draft an email, or summarize a document.

The AI SDK Core provides two functions to generate text and stream it from LLMs:

Advanced LLM features such as tool calling and structured data generation are built on top of text generation.

You can generate text using the generateText function. This function is ideal for non-interactive use cases where you need to write text (e.g. drafting email or summarizing web pages) and for agents that use tools.

You can use more advanced prompts to generate text with more complex instructions and content:

The result object of generateText contains several promises that resolve when all required data is available:

Sometimes you need access to the full response from the model provider, e.g. to access some provider-specific headers or body content.

You can access the raw response headers and body using the response property:

Depending on your model and prompt, it can take a large language model (LLM) up to a minute to finish generating its response. This delay can be unacceptable for interactive use cases such as chatbots or real-time applications, where users expect immediate responses.

AI SDK Core provides the streamText function which simplifies streaming text from LLMs:

result.textStream is both a ReadableStream and an AsyncIterable.

streamText immediately starts streaming and suppresses errors to prevent server crashes. Use the onError callback to log errors.

You can use streamText on its own or in combination with AI SDK UI and AI SDK RSC. The result object contains several helper functions to make the integration into AI SDK UI easier:

streamText is using backpressure and only generates tokens as they are requested. You need to consume the stream in order for it to finish.

It also provides several promises that resolve when the st

*[Content truncated - see full docs]*

**Examples**:

```tsx
import { generateText } from 'ai';
const { text } = await generateText({  model: 'openai/gpt-4.1',  prompt: 'Write a vegetarian lasagna recipe for 4 people.',});
```

```tsx
import { generateText } from 'ai';
const { text } = await generateText({  model: 'openai/gpt-4.1',  prompt: 'Write a vegetarian lasagna recipe for 4 people.',});
```

```tsx
import { generateText } from 'ai';
const { text } = await generateText({  model: 'openai/gpt-4.1',  system:    'You are a professional writer. ' +    'You write simple, clear, and concise content.',  prompt: `Summarize the following article in 3-5 sentences: ${article}`,});
```

---

## Generative User Interfaces

**URL**: https://ai-sdk.dev/docs/ai-sdk-ui/generative-user-interfaces

**Contents**:
- Generative User Interfaces
- Build a Generative UI Chat Interface
  - Basic Chat Implementation
  - Create a Tool
  - Update the API Route
  - Create UI Components
  - Render the Weather Component
- Expanding Your Generative UI Application

Generative user interfaces (generative UI) is the process of allowing a large language model (LLM) to go beyond text and "generate UI". This creates a more engaging and AI-native experience for users.

At the core of generative UI are tools , which are functions you provide to the model to perform specialized tasks like getting the weather in a location. The model can decide when and how to use these tools based on the context of the conversation.

Generative UI is the process of connecting the results of a tool call to a React component. Here's how it works:

By passing the tool results to React components, you can create a generative UI experience that's more engaging and adaptive to your needs.

Let's create a chat interface that handles text-based conversations and incorporates dynamic UI elements based on model responses.

Start with a basic chat implementation using the useChat hook:

To handle the chat requests and model responses, set up an API route:

This API route uses the streamText function to process chat messages and stream the model's responses back to the client.

Before enhancing your chat interface with dynamic UI elements, you need to create a tool and corresponding React component. A tool will allow the model to perform a specific action, such as fetching weather information.

Create a new file called ai/tools.ts with the following content:

In this file, you've created a tool called weatherTool. This tool simulates fetching weather information for a given location. This tool will return simulated data after a 2-second delay. In a real-world application, you would replace this simulation with an actual API call to a weather service.

Update the API route to include the tool you've defined:

Now that you've defined the tool and added it to your streamText call, let's build a React component to display the weather information it returns.

Create a new file called components/weather.tsx:

This component will display the weather information for a gi

*[Content truncated - see full docs]*

**Examples**:

```tsx
'use client';
import { useChat } from '@ai-sdk/react';import { useState } from 'react';
export default function Page() {  const [input, setInput] = useState('');  const { messages, sendMessage } = useChat();
  const handleSubmit = (e: React.FormEvent) => {    e.preventDefault();    sendMessage({ text: input });    setInput('');  };
  return (    <div>      {messages.map(message => (        <div key={message.id}>          <div>{message.role === 'user' ? 'User: ' : 'AI: '}</div>          <div>    
...
```

```tsx
'use client';
import { useChat } from '@ai-sdk/react';import { useState } from 'react';
export default function Page() {  const [input, setInput] = useState('');  const { messages, sendMessage } = useChat();
  const handleSubmit = (e: React.FormEvent) => {    e.preventDefault();    sendMessage({ text: input });    setInput('');  };
  return (    <div>      {messages.map(message => (        <div key={message.id}>          <div>{message.role === 'user' ? 'User: ' : 'AI: '}</div>          <div>    
...
```

```ts
import { openai } from '@ai-sdk/openai';import { streamText, convertToModelMessages, UIMessage, stepCountIs } from 'ai';
export async function POST(request: Request) {  const { messages }: { messages: UIMessage[] } = await request.json();
  const result = streamText({    model: openai('gpt-4o'),    system: 'You are a friendly assistant!',    messages: convertToModelMessages(messages),    stopWhen: stepCountIs(5),  });
  return result.toUIMessageStreamResponse();}
```

---

## Image Generation

**URL**: https://ai-sdk.dev/docs/ai-sdk-core/image-generation

**Contents**:
- Image Generation
- Settings
  - Size and Aspect Ratio
      - Size
      - Aspect Ratio
  - Generating Multiple Images
  - Providing a Seed
  - Provider-specific Settings

The AI SDK provides the generateImage function to generate images based on a given prompt using an image model.

You can access the image data using the base64 or uint8Array properties:

Depending on the model, you can either specify the size or the aspect ratio.

The size is specified as a string in the format {width}x{height}. Models only support a few sizes, and the supported sizes are different for each model and provider.

The aspect ratio is specified as a string in the format {width}:{height}. Models only support a few aspect ratios, and the supported aspect ratios are different for each model and provider.

generateImage also supports generating multiple images at once:

generateImage will automatically call the model as often as needed (in parallel) to generate the requested number of images.

Each image model has an internal limit on how many images it can generate in a single API call. The AI SDK manages this automatically by batching requests appropriately when you request multiple images using the n parameter. By default, the SDK uses provider-documented limits (for example, DALL-E 3 can only generate 1 image per call, while DALL-E 2 supports up to 10).

If needed, you can override this behavior using the maxImagesPerCall setting when generating your image. This is particularly useful when working with new or custom models where the default batch size might not be optimal:

You can provide a seed to the generateImage function to control the output of the image generation process. If supported by the model, the same seed will always produce the same image.

Image models often have provider- or even model-specific settings. You can pass such settings to the generateImage function using the providerOptions parameter. The options for the provider (openai in the example below) become request body properties.

generateImage accepts an optional abortSignal parameter of type AbortSignal that you can use to abort the image generation process or set a timeout.

g

*[Content truncated - see full docs]*

**Examples**:

```tsx
import { experimental_generateImage as generateImage } from 'ai';import { openai } from '@ai-sdk/openai';
const { image } = await generateImage({  model: openai.image('dall-e-3'),  prompt: 'Santa Claus driving a Cadillac',});
```

```tsx
import { experimental_generateImage as generateImage } from 'ai';import { openai } from '@ai-sdk/openai';
const { image } = await generateImage({  model: openai.image('dall-e-3'),  prompt: 'Santa Claus driving a Cadillac',});
```

```tsx
const base64 = image.base64; // base64 image dataconst uint8Array = image.uint8Array; // Uint8Array image data
```

---

## InkeepStream

**URL**: https://ai-sdk.dev/docs/reference/stream-helpers/inkeep-stream

**Contents**:
- InkeepStream
- Import
  - React
- API Signature
  - Parameters
  - response:
  - callbacks?:
  - onStart:

InkeepStream is part of the legacy Inkeep integration. It is not compatible with the AI SDK 3.1 functions.

The InkeepStream function is a utility that transforms the output from Inkeep's API into a ReadableStream. It uses AIStream under the hood, applying a specific parser for the Inkeep's response data structure.

This works with the official Inkeep API, and it's supported in both Node.js, the Edge Runtime, and browser environments.

**Examples**:

```python
import { InkeepStream } from "ai"
```

---

## Language Model Middleware

**URL**: https://ai-sdk.dev/docs/ai-sdk-core/middleware

**Contents**:
- Language Model Middleware
- Using Language Model Middleware
- Multiple middlewares
- Built-in Middleware
  - Extract Reasoning
  - Simulate Streaming
  - Default Settings
- Community Middleware

Language model middleware is a way to enhance the behavior of language models by intercepting and modifying the calls to the language model.

It can be used to add features like guardrails, RAG, caching, and logging in a language model agnostic way. Such middleware can be developed and distributed independently from the language models that they are applied to.

You can use language model middleware with the wrapLanguageModel function. It takes a language model and a language model middleware and returns a new language model that incorporates the middleware.

The wrapped language model can be used just like any other language model, e.g. in streamText:

You can provide multiple middlewares to the wrapLanguageModel function. The middlewares will be applied in the order they are provided.

The AI SDK comes with several built-in middlewares that you can use to configure language models:

Some providers and models expose reasoning information in the generated text using special tags, e.g. <think> and </think>.

The extractReasoningMiddleware function can be used to extract this reasoning information and expose it as a reasoning property on the result.

You can then use that enhanced model in functions like generateText and streamText.

The extractReasoningMiddleware function also includes a startWithReasoning option. When set to true, the reasoning tag will be prepended to the generated text. This is useful for models that do not include the reasoning tag at the beginning of the response. For more details, see the DeepSeek R1 guide.

The simulateStreamingMiddleware function can be used to simulate streaming behavior with responses from non-streaming language models. This is useful when you want to maintain a consistent streaming interface even when using models that only provide complete responses.

The defaultSettingsMiddleware function can be used to apply default settings to a language model.

The AI SDK provides a Language Model Middleware specification. Community m

*[Content truncated - see full docs]*

**Examples**:

```ts
import { wrapLanguageModel } from 'ai';
const wrappedLanguageModel = wrapLanguageModel({  model: yourModel,  middleware: yourLanguageModelMiddleware,});
```

```ts
import { wrapLanguageModel } from 'ai';
const wrappedLanguageModel = wrapLanguageModel({  model: yourModel,  middleware: yourLanguageModelMiddleware,});
```

```ts
const result = streamText({  model: wrappedLanguageModel,  prompt: 'What cities are in the United States?',});
```

---

## ModelMessage

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-core/model-message

**Contents**:
- ModelMessage
- ModelMessage Types
  - SystemModelMessage
  - UserModelMessage
  - AssistantModelMessage
  - ToolModelMessage
- ModelMessage Parts
  - TextPart

ModelMessage represents the fundamental message structure used with AI SDK Core functions. It encompasses various message types that can be used in the messages field of any AI SDK Core functions.

You can access the Zod schema for ModelMessage with the modelMessageSchema export.

A system message that can contain system information.

You can access the Zod schema for SystemModelMessage with the systemModelMessageSchema export.

Using the "system" property instead of a system message is recommended to enhance resilience against prompt injection attacks.

A user message that can contain text or a combination of text, images, and files.

You can access the Zod schema for UserModelMessage with the userModelMessageSchema export.

An assistant message that can contain text, tool calls, or a combination of both.

You can access the Zod schema for AssistantModelMessage with the assistantModelMessageSchema export.

A tool message that contains the result of one or more tool calls.

You can access the Zod schema for ToolModelMessage with the toolModelMessageSchema export.

Represents a text content part of a prompt. It contains a string of text.

Represents an image part in a user message.

Represents an file part in a user message.

Represents a tool call content part of a prompt, typically generated by the AI model.

Represents the result of a tool call in a tool message.

**Examples**:

```typescript
type SystemModelMessage = {  role: 'system';  content: string;};
```

```typescript
type SystemModelMessage = {  role: 'system';  content: string;};
```

```typescript
type UserModelMessage = {  role: 'user';  content: UserContent;};
type UserContent = string | Array<TextPart | ImagePart | FilePart>;
```

---

## Model Context Protocol (MCP) Tools

**URL**: https://ai-sdk.dev/docs/ai-sdk-core/mcp-tools

**Contents**:
- Model Context Protocol (MCP) Tools
- Initializing an MCP Client
  - HTTP Transport (Recommended)
  - SSE Transport
  - Stdio Transport (Local Servers)
  - Custom Transport
  - Closing the MCP Client
- Using MCP Tools

The MCP tools feature is experimental and may change in the future.

The AI SDK supports connecting to Model Context Protocol (MCP) servers to access their tools. This enables your AI applications to discover and use tools across various services through a standardized interface.

We recommend using HTTP transport (like StreamableHTTPClientTransport) for production deployments. The stdio transport should only be used for connecting to local servers as it cannot be deployed to production environments.

Create an MCP client using one of the following transport options:

For production deployments, we recommend using HTTP transports like StreamableHTTPClientTransport from MCP's official TypeScript SDK:

SSE provides an alternative HTTP-based transport option. Configure it with a type and url property:

The stdio transport should only be used for local servers.

The Stdio transport can be imported from either the MCP SDK or the AI SDK:

You can also bring your own transport by implementing the MCPTransport interface for specific requirements not covered by the standard transports.

The client returned by the experimental_createMCPClient function is a lightweight client intended for use in tool conversion. It currently does not support all features of the full MCP client, such as: authorization, session management, resumable streams, and receiving notifications.

After initialization, you should close the MCP client based on your usage pattern:

When streaming responses, you can close the client when the LLM response has finished. For example, when using streamText, you should use the onFinish callback:

When generating responses without streaming, you can use try/finally or cleanup functions in your framework:

The client's tools method acts as an adapter between MCP tools and AI SDK tools. It supports two approaches for working with tool schemas:

With schema discovery, all tools offered by the server are automatically listed, and input parameter types are inferred bas

*[Content truncated - see full docs]*

**Examples**:

```typescript
import { experimental_createMCPClient as createMCPClient } from 'ai';import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';
const url = new URL('https://your-server.com/mcp');const mcpClient = await createMCPClient({  transport: new StreamableHTTPClientTransport(url, {    sessionId: 'session_123',  }),});
```

```typescript
import { experimental_createMCPClient as createMCPClient } from 'ai';import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';
const url = new URL('https://your-server.com/mcp');const mcpClient = await createMCPClient({  transport: new StreamableHTTPClientTransport(url, {    sessionId: 'session_123',  }),});
```

```typescript
import { experimental_createMCPClient as createMCPClient } from 'ai';
const mcpClient = await createMCPClient({  transport: {    type: 'sse',    url: 'https://my-server.com/sse',
    // optional: configure HTTP headers, e.g. for authentication    headers: {      Authorization: 'Bearer my-api-key',    },  },});
```

---

## Object Generation

**URL**: https://ai-sdk.dev/docs/ai-sdk-ui/object-generation

**Contents**:
- Object Generation
- Example
  - Schema
  - Client
  - Server
- Enum Output Mode
  - Example: Text Classification
    - Client

useObject is an experimental feature and only available in React, Svelte, and Vue.

The useObject hook allows you to create interfaces that represent a structured JSON object that is being streamed.

In this guide, you will learn how to use the useObject hook in your application to generate UIs for structured data on the fly.

The example shows a small notifications demo app that generates fake notifications in real-time.

It is helpful to set up the schema in a separate file that is imported on both the client and server.

The client uses useObject to stream the object generation process.

The results are partial and are displayed as they are received. Please note the code for handling undefined values in the JSX.

On the server, we use streamObject to stream the object generation process.

When you need to classify or categorize input into predefined options, you can use the enum output mode with useObject. This requires a specific schema structure where the object has enum as a key with z.enum containing your possible values.

This example shows how to build a simple text classifier that categorizes statements as true or false.

When using useObject with enum output mode, your schema must be an object with enum as the key:

On the server, use streamObject with output: 'enum' to stream the classification result:

useObject also provides ways to show loading and error states:

The isLoading state returned by the useObject hook can be used for several purposes:

The stop function can be used to stop the object generation process. This can be useful if the user wants to cancel the request or if the server is taking too long to respond.

Similarly, the error state reflects the error object thrown during the fetch request. It can be used to display an error message, or to disable the submit button:

We recommend showing a generic error message to the user, such as "Something went wrong." This is a good practice to avoid leaking information from the server.

useObject p

*[Content truncated - see full docs]*

**Examples**:

```ts
import { z } from 'zod';
// define a schema for the notificationsexport const notificationSchema = z.object({  notifications: z.array(    z.object({      name: z.string().describe('Name of a fictional person.'),      message: z.string().describe('Message. Do not use emojis or links.'),    }),  ),});
```

```ts
import { z } from 'zod';
// define a schema for the notificationsexport const notificationSchema = z.object({  notifications: z.array(    z.object({      name: z.string().describe('Name of a fictional person.'),      message: z.string().describe('Message. Do not use emojis or links.'),    }),  ),});
```

```tsx
'use client';
import { experimental_useObject as useObject } from '@ai-sdk/react';import { notificationSchema } from './api/notifications/schema';
export default function Page() {  const { object, submit } = useObject({    api: '/api/notifications',    schema: notificationSchema,  });
  return (    <>      <button onClick={() => submit('Messages during finals week.')}>        Generate notifications      </button>
      {object?.notifications?.map((notification, index) => (        <div key={index
...
```

---

## Prompt Engineering

**URL**: https://ai-sdk.dev/docs/ai-sdk-core/prompt-engineering

**Contents**:
- Prompt Engineering
- Tips
  - Prompts for Tools
  - Tool & Structured Data Schemas
    - Zod Dates
    - Optional Parameters
    - Temperature Settings
- Debugging

When you create prompts that include tools, getting good results can be tricky as the number and complexity of your tools increases.

Here are a few tips to help you get the best results:

In general, the goal should be to give the model all information it needs in a clear way.

The mapping from Zod schemas to LLM inputs (typically JSON schema) is not always straightforward, since the mapping is not one-to-one.

Zod expects JavaScript Date objects, but models return dates as strings. You can specify and validate the date format using z.string().datetime() or z.string().date(), and then use a Zod transformer to convert the string to a Date object.

When working with tools that have optional parameters, you may encounter compatibility issues with certain providers that use strict schema validation.

This is particularly relevant for OpenAI models with structured outputs (strict mode).

For maximum compatibility, optional parameters should use .nullable() instead of .optional():

For tool calls and object generation, it's recommended to use temperature: 0 to ensure deterministic and consistent results:

Lower temperature values reduce randomness in model outputs, which is particularly important when the model needs to:

Not all providers support all AI SDK features. Providers either throw exceptions or return warnings when they do not support a feature. To check if your prompt, tools, and settings are handled correctly by the provider, you can check the call warnings:

You can inspect the raw HTTP request bodies for models that expose them, e.g. OpenAI. This allows you to inspect the exact payload that is sent to the model provider in the provider-specific way.

Request bodies are available via the request.body property of the response:

**Examples**:

```ts
const result = await generateObject({  model: openai('gpt-4.1'),  schema: z.object({    events: z.array(      z.object({        event: z.string(),        date: z          .string()          .date()          .transform(value => new Date(value)),      }),    ),  }),  prompt: 'List 5 important events from the year 2000.',});
```

```ts
const result = await generateObject({  model: openai('gpt-4.1'),  schema: z.object({    events: z.array(      z.object({        event: z.string(),        date: z          .string()          .date()          .transform(value => new Date(value)),      }),    ),  }),  prompt: 'List 5 important events from the year 2000.',});
```

```ts
// This may fail with strict schema validationconst failingTool = tool({  description: 'Execute a command',  inputSchema: z.object({    command: z.string(),    workdir: z.string().optional(), // This can cause errors    timeout: z.string().optional(),  }),});
// This works with strict schema validationconst workingTool = tool({  description: 'Execute a command',  inputSchema: z.object({    command: z.string(),    workdir: z.string().nullable(), // Use nullable instead    timeout: z.string().null
...
```

---

## Prompts

**URL**: https://ai-sdk.dev/docs/ai-sdk-core/prompts

**Contents**:
- Prompts
- Text Prompts
- System Prompts
- Message Prompts
  - Provider Options
    - Function Call Level
    - Message Level
    - Message Part Level

Prompts are instructions that you give a large language model (LLM) to tell it what to do. It's like when you ask someone for directions; the clearer your question, the better the directions you'll get.

Many LLM providers offer complex interfaces for specifying prompts. They involve different roles and message types. While these interfaces are powerful, they can be hard to use and understand.

In order to simplify prompting, the AI SDK supports text, message, and system prompts.

Text prompts are strings. They are ideal for simple generation use cases, e.g. repeatedly generating content for variants of the same prompt text.

You can set text prompts using the prompt property made available by AI SDK functions like streamText or generateObject. You can structure the text in any way and inject variables, e.g. using a template literal.

You can also use template literals to provide dynamic data to your prompt.

System prompts are the initial set of instructions given to models that help guide and constrain the models' behaviors and responses. You can set system prompts using the system property. System prompts work with both the prompt and the messages properties.

When you use a message prompt, you can also use system messages instead of a system prompt.

A message prompt is an array of user, assistant, and tool messages. They are great for chat interfaces and more complex, multi-modal prompts. You can use the messages property to set message prompts.

Each message has a role and a content property. The content can either be text (for user and assistant messages), or an array of relevant parts (data) for that message type.

Instead of sending a text in the content property, you can send an array of parts that includes a mix of text and other content parts.

Not all language models support all message and content types. For example, some models might not be capable of handling multi-modal inputs or tool messages. Learn more about the capabilities of select models.

Yo

*[Content truncated - see full docs]*

**Examples**:

```ts
const result = await generateText({  model: 'openai/gpt-4.1',  prompt: 'Invent a new holiday and describe its traditions.',});
```

```ts
const result = await generateText({  model: 'openai/gpt-4.1',  prompt: 'Invent a new holiday and describe its traditions.',});
```

```ts
const result = await generateText({  model: 'openai/gpt-4.1',  prompt:    `I am planning a trip to ${destination} for ${lengthOfStay} days. ` +    `Please suggest the best tourist activities for me to do.`,});
```

---

## Provider & Model Management

**URL**: https://ai-sdk.dev/docs/ai-sdk-core/provider-management

**Contents**:
- Provider & Model Management
- Custom Providers
  - Example: custom model settings
  - Example: model name alias
  - Example: limit available models
- Provider Registry
  - Setup
  - Setup with Custom Separator

When you work with multiple providers and models, it is often desirable to manage them in a central place and access the models through simple string ids.

The AI SDK offers custom providers and a provider registry for this purpose:

You can mix and match custom providers, the provider registry, and middleware in your application.

You can create a custom provider using customProvider.

You might want to override the default model settings for a provider or provide model name aliases with pre-configured settings.

You can also provide model name aliases, so you can update the model version in one place in the future:

You can limit the available models in the system, even if you have multiple providers.

You can create a provider registry with multiple providers and models using createProviderRegistry.

By default, the registry uses : as the separator between provider and model IDs. You can customize this separator:

You can access language models by using the languageModel method on the registry. The provider id will become the prefix of the model id: providerId:modelId.

You can access text embedding models by using the textEmbeddingModel method on the registry. The provider id will become the prefix of the model id: providerId:modelId.

You can access image models by using the imageModel method on the registry. The provider id will become the prefix of the model id: providerId:modelId.

The central idea of provider management is to set up a file that contains all the providers and models you want to use. You may want to pre-configure model settings, provide model name aliases, limit the available models, and more.

Here is an example that implements the following concepts:

The AI SDK 5 includes a global provider feature that allows you to specify a model using just a plain model ID string:

By default, the global provider is set to the Vercel AI Gateway.

You can set your own preferred global provider:

This simplifies provider usage and makes it easier to switc

*[Content truncated - see full docs]*

**Examples**:

```ts
import { openai as originalOpenAI } from '@ai-sdk/openai';import {  customProvider,  defaultSettingsMiddleware,  wrapLanguageModel,} from 'ai';
// custom provider with different provider options:export const openai = customProvider({  languageModels: {    // replacement model with custom provider options:    'gpt-4o': wrapLanguageModel({      model: originalOpenAI('gpt-4o'),      middleware: defaultSettingsMiddleware({        settings: {          providerOptions: {            openai: {          
...
```

```ts
import { openai as originalOpenAI } from '@ai-sdk/openai';import {  customProvider,  defaultSettingsMiddleware,  wrapLanguageModel,} from 'ai';
// custom provider with different provider options:export const openai = customProvider({  languageModels: {    // replacement model with custom provider options:    'gpt-4o': wrapLanguageModel({      model: originalOpenAI('gpt-4o'),      middleware: defaultSettingsMiddleware({        settings: {          providerOptions: {            openai: {          
...
```

```ts
import { anthropic as originalAnthropic } from '@ai-sdk/anthropic';import { customProvider } from 'ai';
// custom provider with alias names:export const anthropic = customProvider({  languageModels: {    opus: originalAnthropic('claude-3-opus-20240229'),    sonnet: originalAnthropic('claude-3-5-sonnet-20240620'),    haiku: originalAnthropic('claude-3-haiku-20240307'),  },  fallbackProvider: originalAnthropic,});
```

---

## Reading UI Message Streams

**URL**: https://ai-sdk.dev/docs/ai-sdk-ui/reading-ui-message-streams

**Contents**:
- Reading UI Message Streams
- Basic Usage
- Tool Calls Integration
- Resuming Conversations

UIMessage streams are useful outside of traditional chat use cases. You can consume them for terminal UIs, custom stream processing on the client, or React Server Components (RSC).

The readUIMessageStream helper transforms a stream of UIMessageChunk objects into an AsyncIterableStream of UIMessage objects, allowing you to process messages as they're being constructed.

Handle streaming responses that include tool calls:

Resume streaming from a previous message state:

**Examples**:

```tsx
import { openai } from '@ai-sdk/openai';import { readUIMessageStream, streamText } from 'ai';
async function main() {  const result = streamText({    model: openai('gpt-4o'),    prompt: 'Write a short story about a robot.',  });
  for await (const uiMessage of readUIMessageStream({    stream: result.toUIMessageStream(),  })) {    console.log('Current message state:', uiMessage);  }}
```

```tsx
import { openai } from '@ai-sdk/openai';import { readUIMessageStream, streamText } from 'ai';
async function main() {  const result = streamText({    model: openai('gpt-4o'),    prompt: 'Write a short story about a robot.',  });
  for await (const uiMessage of readUIMessageStream({    stream: result.toUIMessageStream(),  })) {    console.log('Current message state:', uiMessage);  }}
```

```tsx
import { openai } from '@ai-sdk/openai';import { readUIMessageStream, streamText, tool } from 'ai';import { z } from 'zod';
async function handleToolCalls() {  const result = streamText({    model: openai('gpt-4o'),    tools: {      weather: tool({        description: 'Get the weather in a location',        inputSchema: z.object({          location: z.string().describe('The location to get the weather for'),        }),        execute: ({ location }) => ({          location,          temperature:
...
```

---

## Settings

**URL**: https://ai-sdk.dev/docs/ai-sdk-core/settings

**Contents**:
- Settings
  - maxOutputTokens
  - temperature
  - topP
  - topK
  - presencePenalty
  - frequencyPenalty
  - stopSequences

Large language models (LLMs) typically provide settings to augment their output.

All AI SDK functions support the following common settings in addition to the model, the prompt, and additional provider-specific settings:

Some providers do not support all common settings. If you use a setting with a provider that does not support it, a warning will be generated. You can check the warnings property in the result object to see if any warnings were generated.

Maximum number of tokens to generate.

The value is passed through to the provider. The range depends on the provider and model. For most providers, 0 means almost deterministic results, and higher values mean more randomness.

It is recommended to set either temperature or topP, but not both.

The value is passed through to the provider. The range depends on the provider and model. For most providers, nucleus sampling is a number between 0 and 1. E.g. 0.1 would mean that only tokens with the top 10% probability mass are considered.

It is recommended to set either temperature or topP, but not both.

Only sample from the top K options for each subsequent token.

Used to remove "long tail" low probability responses. Recommended for advanced use cases only. You usually only need to use temperature.

The presence penalty affects the likelihood of the model to repeat information that is already in the prompt.

The value is passed through to the provider. The range depends on the provider and model. For most providers, 0 means no penalty.

The frequency penalty affects the likelihood of the model to repeatedly use the same words or phrases.

The value is passed through to the provider. The range depends on the provider and model. For most providers, 0 means no penalty.

The stop sequences to use for stopping the text generation.

If set, the model will stop generating text when one of the stop sequences is generated. Providers may have limits on the number of stop sequences.

It is the seed (integer) to use for rando

*[Content truncated - see full docs]*

**Examples**:

```ts
const result = await generateText({  model: 'openai/gpt-4.1',  maxOutputTokens: 512,  temperature: 0.3,  maxRetries: 5,  prompt: 'Invent a new holiday and describe its traditions.',});
```

```ts
const result = await generateText({  model: 'openai/gpt-4.1',  maxOutputTokens: 512,  temperature: 0.3,  maxRetries: 5,  prompt: 'Invent a new holiday and describe its traditions.',});
```

```ts
const result = await generateText({  model: openai('gpt-4o'),  prompt: 'Invent a new holiday and describe its traditions.',  abortSignal: AbortSignal.timeout(5000), // 5 seconds});
```

---

## Speech

**URL**: https://ai-sdk.dev/docs/ai-sdk-core/speech

**Contents**:
- Speech
  - Language Setting
- Settings
  - Provider-Specific settings
  - Abort Signals and Timeouts
  - Custom Headers
  - Warnings
  - Error Handling

The AI SDK provides the generateSpeech function to generate speech from text using a speech model.

You can specify the language for speech generation (provider support varies):

To access the generated audio:

You can set model-specific settings with the providerOptions parameter.

generateSpeech accepts an optional abortSignal parameter of type AbortSignal that you can use to abort the speech generation process or set a timeout.

generateSpeech accepts an optional headers parameter of type Record<string, string> that you can use to add custom headers to the speech generation request.

Warnings (e.g. unsupported parameters) are available on the warnings property.

When generateSpeech cannot generate a valid audio, it throws a AI_NoSpeechGeneratedError.

This error can arise for any the following reasons:

The error preserves the following information to help you log the issue:

Above are a small subset of the speech models supported by the AI SDK providers. For more, see the respective provider documentation.

**Examples**:

```ts
import { experimental_generateSpeech as generateSpeech } from 'ai';import { openai } from '@ai-sdk/openai';
const audio = await generateSpeech({  model: openai.speech('tts-1'),  text: 'Hello, world!',  voice: 'alloy',});
```

```ts
import { experimental_generateSpeech as generateSpeech } from 'ai';import { openai } from '@ai-sdk/openai';
const audio = await generateSpeech({  model: openai.speech('tts-1'),  text: 'Hello, world!',  voice: 'alloy',});
```

```ts
import { experimental_generateSpeech as generateSpeech } from 'ai';import { lmnt } from '@ai-sdk/lmnt';
const audio = await generateSpeech({  model: lmnt.speech('aurora'),  text: 'Hola, mundo!',  language: 'es', // Spanish});
```

---

## Stream Protocols

**URL**: https://ai-sdk.dev/docs/ai-sdk-ui/stream-protocol

**Contents**:
- Stream Protocols
- Text Stream Protocol
  - Text Stream Example
- Data Stream Protocol
  - Message Start Part
  - Text Parts
    - Text Start Part
    - Text Delta Part

AI SDK UI functions such as useChat and useCompletion support both text streams and data streams. The stream protocol defines how the data is streamed to the frontend on top of the HTTP protocol.

This page describes both protocols and how to use them in the backend and frontend.

You can use this information to develop custom backends and frontends for your use case, e.g., to provide compatible API endpoints that are implemented in a different language such as Python.

For instance, here's an example using FastAPI as a backend.

A text stream contains chunks in plain text, that are streamed to the frontend. Each chunk is then appended together to form a full text response.

Text streams are supported by useChat, useCompletion, and useObject. When you use useChat or useCompletion, you need to enable text streaming by setting the streamProtocol options to text.

You can generate text streams with streamText in the backend. When you call toTextStreamResponse() on the result object, a streaming HTTP response is returned.

Text streams only support basic text data. If you need to stream other types of data such as tool calls, use data streams.

Here is a Next.js example that uses the text stream protocol:

A data stream follows a special protocol that the AI SDK provides to send information to the frontend.

The data stream protocol uses Server-Sent Events (SSE) format for improved standardization, keep-alive through ping, reconnect capabilities, and better cache handling.

When you provide data streams from a custom backend, you need to set the x-vercel-ai-ui-message-stream header to v1.

The following stream parts are currently supported:

Indicates the beginning of a new message with metadata.

Format: Server-Sent Event with JSON object

Text content is streamed using a start/delta/end pattern with unique IDs for each text block.

Indicates the beginning of a text block.

Format: Server-Sent Event with JSON object

Contains incremental text content for the text block

*[Content truncated - see full docs]*

**Examples**:

```tsx
'use client';
import { useChat } from '@ai-sdk/react';import { TextStreamChatTransport } from 'ai';import { useState } from 'react';
export default function Chat() {  const [input, setInput] = useState('');  const { messages, sendMessage } = useChat({    transport: new TextStreamChatTransport({ api: '/api/chat' }),  });
  return (    <div className="flex flex-col w-full max-w-md py-24 mx-auto stretch">      {messages.map(message => (        <div key={message.id} className="whitespace-pre-wrap"> 
...
```

```tsx
'use client';
import { useChat } from '@ai-sdk/react';import { TextStreamChatTransport } from 'ai';import { useState } from 'react';
export default function Chat() {  const [input, setInput] = useState('');  const { messages, sendMessage } = useChat({    transport: new TextStreamChatTransport({ api: '/api/chat' }),  });
  return (    <div className="flex flex-col w-full max-w-md py-24 mx-auto stretch">      {messages.map(message => (        <div key={message.id} className="whitespace-pre-wrap"> 
...
```

```ts
import { streamText, UIMessage, convertToModelMessages } from 'ai';import { openai } from '@ai-sdk/openai';
// Allow streaming responses up to 30 secondsexport const maxDuration = 30;
export async function POST(req: Request) {  const { messages }: { messages: UIMessage[] } = await req.json();
  const result = streamText({    model: openai('gpt-4o'),    messages: convertToModelMessages(messages),  });
  return result.toTextStreamResponse();}
```

---

## Streaming

**URL**: https://ai-sdk.dev/docs/foundations/streaming

**Contents**:
- Streaming
- Real-world Examples
  - Blocking UI
  - Streaming UI

Streaming conversational text UIs (like ChatGPT) have gained massive popularity over the past few months. This section explores the benefits and drawbacks of streaming and blocking interfaces.

Large language models (LLMs) are extremely powerful. However, when generating long outputs, they can be very slow compared to the latency you're likely used to. If you try to build a traditional blocking UI, your users might easily find themselves staring at loading spinners for 5, 10, even up to 40s waiting for the entire LLM response to be generated. This can lead to a poor user experience, especially in conversational applications like chatbots. Streaming UIs can help mitigate this issue by displaying parts of the response as they become available.

Blocking responses wait until the full response is available before displaying it.

Streaming responses can transmit parts of the response as they become available.

Here are 2 examples that illustrate how streaming UIs can improve user experiences in a real-world setting – the first uses a blocking UI, while the second uses a streaming UI.

As you can see, the streaming UI is able to start displaying the response much faster than the blocking UI. This is because the blocking UI has to wait for the entire response to be generated before it can display anything, while the streaming UI can display parts of the response as they become available.

While streaming interfaces can greatly enhance user experiences, especially with larger language models, they aren't always necessary or beneficial. If you can achieve your desired functionality using a smaller, faster model without resorting to streaming, this route can often lead to simpler and more manageable development processes.

However, regardless of the speed of your model, the AI SDK is designed to make implementing streaming UIs as simple as possible. In the example below, we stream text generation from OpenAI's gpt-4.1 in under 10 lines of code using the SDK's streamText funct

*[Content truncated - see full docs]*

**Examples**:

```ts
import { openai } from '@ai-sdk/openai';import { streamText } from 'ai';
const { textStream } = streamText({  model: openai('gpt-4.1'),  prompt: 'Write a poem about embedding models.',});
for await (const textPart of textStream) {  console.log(textPart);}
```

```ts
import { openai } from '@ai-sdk/openai';import { streamText } from 'ai';
const { textStream } = streamText({  model: openai('gpt-4.1'),  prompt: 'Write a poem about embedding models.',});
for await (const textPart of textStream) {  console.log(textPart);}
```

---

## Streaming Custom Data

**URL**: https://ai-sdk.dev/docs/ai-sdk-ui/streaming-data

**Contents**:
- Streaming Custom Data
- Setting Up Type-Safe Data Streaming
- Streaming Data from the Server
- Types of Streamable Data
  - Data Parts (Persistent)
  - Sources
  - Transient Data Parts (Ephemeral)
- Data Part Reconciliation

It is often useful to send additional data alongside the model's response. For example, you may want to send status information, the message ids after storing them, or references to content that the language model is referring to.

The AI SDK provides several helpers that allows you to stream additional data to the client and attach it to the UIMessage parts array:

The data is streamed as part of the response stream using Server-Sent Events.

First, define your custom message type with data part schemas for type safety:

In your server-side route handler, you can create a UIMessageStream and then pass it to createUIMessageStreamResponse:

You can also send stream data from custom backends, e.g. Python / FastAPI, using the UI Message Stream Protocol.

Regular data parts are added to the message history and appear in message.parts:

Sources are useful for RAG implementations where you want to show which documents or URLs were referenced:

Transient parts are sent to the client but not added to the message history. They are only accessible via the onData useChat handler:

When you write to a data part with the same ID, the client automatically reconciles and updates that part. This enables powerful dynamic experiences like:

The reconciliation happens automatically - simply use the same id when writing to the stream.

The onData callback is essential for handling streaming data, especially transient parts:

Important: Transient data parts are only available through the onData callback. They will not appear in the message.parts array since they're not added to message history.

You can filter and render data parts from the message parts array:

Both message metadata and data parts allow you to send additional information alongside messages, but they serve different purposes:

Message metadata is best for message-level information that describes the message as a whole:

Data parts are best for streaming dynamic arbitrary data:

For more details on message metadata, see 

*[Content truncated - see full docs]*

**Examples**:

```tsx
import { UIMessage } from 'ai';
// Define your custom message type with data part schemasexport type MyUIMessage = UIMessage<  never, // metadata type  {    weather: {      city: string;      weather?: string;      status: 'loading' | 'success';    };    notification: {      message: string;      level: 'info' | 'warning' | 'error';    };  } // data parts type>;
```

```tsx
import { UIMessage } from 'ai';
// Define your custom message type with data part schemasexport type MyUIMessage = UIMessage<  never, // metadata type  {    weather: {      city: string;      weather?: string;      status: 'loading' | 'success';    };    notification: {      message: string;      level: 'info' | 'warning' | 'error';    };  } // data parts type>;
```

```tsx
import { openai } from '@ai-sdk/openai';import {  createUIMessageStream,  createUIMessageStreamResponse,  streamText,  convertToModelMessages,} from 'ai';import type { MyUIMessage } from '@/ai/types';
export async function POST(req: Request) {  const { messages } = await req.json();
  const stream = createUIMessageStream<MyUIMessage>({    execute: ({ writer }) => {      // 1. Send initial status (transient - won't be added to message history)      writer.write({        type: 'data-notification',
...
```

---

## Streaming React Components

**URL**: https://ai-sdk.dev/docs/ai-sdk-rsc/streaming-react-components

**Contents**:
- Streaming React Components
  - Concepts
  - Adding A Tool
- Using streamUI with Next.js
  - Step 1: Create a Server Action
  - Step 2: Create a Page
- Going beyond a single prompt

AI SDK RSC is currently experimental. We recommend using AI SDK UI for production. For guidance on migrating from RSC to UI, see our migration guide.

The RSC API allows you to stream React components from the server to the client with the streamUI function. This is useful when you want to go beyond raw text and stream components to the client in real-time.

Similar to AI SDK Core APIs (like streamText and streamObject ), streamUI provides a single function to call a model and allow it to respond with React Server Components. It supports the same model interfaces as AI SDK Core APIs.

To give the model the ability to respond to a user's prompt with a React component, you can leverage tools.

Remember, tools are like programs you can give to the model, and the model can decide as and when to use based on the context of the conversation.

With the streamUI function, you provide tools that return React components. With the ability to stream components, the model is akin to a dynamic router that is able to understand the user's intention and display relevant UI.

At a high level, the streamUI works like other AI SDK Core functions: you can provide the model with a prompt or some conversation history and, optionally, some tools. If the model decides, based on the context of the conversation, to call a tool, it will generate a tool call. The streamUI function will then run the respective tool, returning a React component. If the model doesn't have a relevant tool to use, it will return a text generation, which will be passed to the text function, for you to handle (render and return as a React component).

This example calls the streamUI function using OpenAI's gpt-4o model, passes a prompt, specifies how the model's plain text response (content) should be rendered, and then provides an empty object for tools. Even though this example does not define any tools, it will stream the model's response as a div rather than plain text.

Using tools with streamUI is similar to ho

*[Content truncated - see full docs]*

**Examples**:

```tsx
const result = await streamUI({  model: openai('gpt-4o'),  prompt: 'Get the weather for San Francisco',  text: ({ content }) => <div>{content}</div>,  tools: {},});
```

```tsx
const result = await streamUI({  model: openai('gpt-4o'),  prompt: 'Get the weather for San Francisco',  text: ({ content }) => <div>{content}</div>,  tools: {},});
```

```tsx
const result = await streamUI({  model: openai('gpt-4o'),  prompt: 'Get the weather for San Francisco',  text: ({ content }) => <div>{content}</div>,  tools: {    getWeather: {      description: 'Get the weather for a location',      inputSchema: z.object({ location: z.string() }),      generate: async function* ({ location }) {        yield <LoadingComponent />;        const weather = await getWeather(location);        return <WeatherComponent weather={weather} location={location} />;      },  
...
```

---

## Streaming Values

**URL**: https://ai-sdk.dev/docs/ai-sdk-rsc/streaming-values

**Contents**:
- Streaming Values
- createStreamableValue
- Creating a Streamable Value
- Reading a Streamable Value
- createStreamableUI
- Using createStreamableUI
- Reading a Streamable UI

AI SDK RSC is currently experimental. We recommend using AI SDK UI for production. For guidance on migrating from RSC to UI, see our migration guide.

The RSC API provides several utility functions to allow you to stream values from the server to the client. This is useful when you need more granular control over what you are streaming and how you are streaming it.

These utilities can also be paired with AI SDK Core functions like streamText and streamObject to easily stream LLM generations from the server to the client.

There are two functions provided by the RSC API that allow you to create streamable values:

The RSC API allows you to stream serializable Javascript values from the server to the client using createStreamableValue, such as strings, numbers, objects, and arrays.

This is useful when you want to stream:

You can import createStreamableValue from @ai-sdk/rsc and use it to create a streamable value.

You can read streamable values on the client using readStreamableValue. It returns an async iterator that yields the value of the streamable as it is updated:

Learn how to stream a text generation (with streamText) using the Next.js App Router and createStreamableValue in this example.

createStreamableUI creates a stream that holds a React component. Unlike AI SDK Core APIs, this function does not call a large language model. Instead, it provides a primitive that can be used to have granular control over streaming a React component.

Let's look at how you can use the createStreamableUI function with a Server Action.

First, you create a streamable UI with an empty state and then update it with a loading message. After 1 second, you mark the stream as done passing in the actual weather information as its final value. The .value property contains the actual UI that can be sent to the client.

On the client side, you can call the getWeather Server Action and render the returned UI like any other React component.

When the button is clicked, the getWeather

*[Content truncated - see full docs]*

**Examples**:

```tsx
'use server';
import { createStreamableValue } from '@ai-sdk/rsc';
export const runThread = async () => {  const streamableStatus = createStreamableValue('thread.init');
  setTimeout(() => {    streamableStatus.update('thread.run.create');    streamableStatus.update('thread.run.update');    streamableStatus.update('thread.run.end');    streamableStatus.done('thread.end');  }, 1000);
  return {    status: streamableStatus.value,  };};
```

```tsx
'use server';
import { createStreamableValue } from '@ai-sdk/rsc';
export const runThread = async () => {  const streamableStatus = createStreamableValue('thread.init');
  setTimeout(() => {    streamableStatus.update('thread.run.create');    streamableStatus.update('thread.run.update');    streamableStatus.update('thread.run.end');    streamableStatus.done('thread.end');  }, 1000);
  return {    status: streamableStatus.value,  };};
```

```tsx
import { readStreamableValue } from '@ai-sdk/rsc';import { runThread } from '@/actions';
export default function Page() {  return (    <button      onClick={async () => {        const { status } = await runThread();
        for await (const value of readStreamableValue(status)) {          console.log(value);        }      }}    >      Ask    </button>  );}
```

---

## Streaming

**URL**: https://ai-sdk.dev/docs/advanced/why-streaming

**Contents**:
- Streaming
- Real-world Examples
  - Blocking UI
  - Streaming UI

Streaming conversational text UIs (like ChatGPT) have gained massive popularity over the past few months. This section explores the benefits and drawbacks of streaming and blocking interfaces.

Large language models (LLMs) are extremely powerful. However, when generating long outputs, they can be very slow compared to the latency you're likely used to. If you try to build a traditional blocking UI, your users might easily find themselves staring at loading spinners for 5, 10, even up to 40s waiting for the entire LLM response to be generated. This can lead to a poor user experience, especially in conversational applications like chatbots. Streaming UIs can help mitigate this issue by displaying parts of the response as they become available.

Blocking responses wait until the full response is available before displaying it.

Streaming responses can transmit parts of the response as they become available.

Here are 2 examples that illustrate how streaming UIs can improve user experiences in a real-world setting – the first uses a blocking UI, while the second uses a streaming UI.

As you can see, the streaming UI is able to start displaying the response much faster than the blocking UI. This is because the blocking UI has to wait for the entire response to be generated before it can display anything, while the streaming UI can display parts of the response as they become available.

While streaming interfaces can greatly enhance user experiences, especially with larger language models, they aren't always necessary or beneficial. If you can achieve your desired functionality using a smaller, faster model without resorting to streaming, this route can often lead to simpler and more manageable development processes.

However, regardless of the speed of your model, the AI SDK is designed to make implementing streaming UIs as simple as possible. In the example below, we stream text generation from OpenAI's gpt-4.1 in under 10 lines of code using the SDK's streamText funct

*[Content truncated - see full docs]*

**Examples**:

```ts
import { openai } from '@ai-sdk/openai';import { streamText } from 'ai';
const { textStream } = streamText({  model: openai('gpt-4.1'),  prompt: 'Write a poem about embedding models.',});
for await (const textPart of textStream) {  console.log(textPart);}
```

```ts
import { openai } from '@ai-sdk/openai';import { streamText } from 'ai';
const { textStream } = streamText({  model: openai('gpt-4.1'),  prompt: 'Write a poem about embedding models.',});
for await (const textPart of textStream) {  console.log(textPart);}
```

---

## Telemetry

**URL**: https://ai-sdk.dev/docs/ai-sdk-core/telemetry

**Contents**:
- Telemetry
- Enabling telemetry
- Telemetry Metadata
- Custom Tracer
- Collected Data
  - generateText function
  - streamText function
  - generateObject function

AI SDK Telemetry is experimental and may change in the future.

The AI SDK uses OpenTelemetry to collect telemetry data. OpenTelemetry is an open-source observability framework designed to provide standardized instrumentation for collecting telemetry data.

Check out the AI SDK Observability Integrations to see providers that offer monitoring and tracing for AI SDK applications.

For Next.js applications, please follow the Next.js OpenTelemetry guide to enable telemetry first.

You can then use the experimental_telemetry option to enable telemetry on specific function calls while the feature is experimental:

When telemetry is enabled, you can also control if you want to record the input values and the output values for the function. By default, both are enabled. You can disable them by setting the recordInputs and recordOutputs options to false.

Disabling the recording of inputs and outputs can be useful for privacy, data transfer, and performance reasons. You might for example want to disable recording inputs if they contain sensitive information.

You can provide a functionId to identify the function that the telemetry data is for, and metadata to include additional information in the telemetry data.

You may provide a tracer which must return an OpenTelemetry Tracer. This is useful in situations where you want your traces to use a TracerProvider other than the one provided by the @opentelemetry/api singleton.

generateText records 3 types of spans:

ai.generateText (span): the full length of the generateText call. It contains 1 or more ai.generateText.doGenerate spans. It contains the basic LLM span information and the following attributes:

ai.generateText.doGenerate (span): a provider doGenerate call. It can contain ai.toolCall spans. It contains the call LLM span information and the following attributes:

ai.toolCall (span): a tool call that is made as part of the generateText call. See Tool call spans for more details.

streamText records 3 types of spans a

*[Content truncated - see full docs]*

**Examples**:

```ts
const result = await generateText({  model: openai('gpt-4.1'),  prompt: 'Write a short story about a cat.',  experimental_telemetry: { isEnabled: true },});
```

```ts
const result = await generateText({  model: openai('gpt-4.1'),  prompt: 'Write a short story about a cat.',  experimental_telemetry: { isEnabled: true },});
```

```ts
const result = await generateText({  model: openai('gpt-4.1'),  prompt: 'Write a short story about a cat.',  experimental_telemetry: {    isEnabled: true,    functionId: 'my-awesome-function',    metadata: {      something: 'custom',      someOtherThing: 'other-value',    },  },});
```

---

## Testing

**URL**: https://ai-sdk.dev/docs/ai-sdk-core/testing

**Contents**:
- Testing
- Examples
  - generateText
  - streamText
  - generateObject
  - streamObject
  - Simulate UI Message Stream Responses

Testing language models can be challenging, because they are non-deterministic and calling them is slow and expensive.

To enable you to unit test your code that uses the AI SDK, the AI SDK Core includes mock providers and test helpers. You can import the following helpers from ai/test:

With mock providers and test helpers, you can control the output of the AI SDK and test your code in a repeatable and deterministic way without actually calling a language model provider.

You can use the test helpers with the AI Core functions in your unit tests:

You can also simulate UI Message Stream responses for testing, debugging, or demonstration purposes.

Here is a Next example:

**Examples**:

```ts
import { generateText } from 'ai';import { MockLanguageModelV2 } from 'ai/test';
const result = await generateText({  model: new MockLanguageModelV2({    doGenerate: async () => ({      finishReason: 'stop',      usage: { inputTokens: 10, outputTokens: 20, totalTokens: 30 },      content: [{ type: 'text', text: `Hello, world!` }],      warnings: [],    }),  }),  prompt: 'Hello, test!',});
```

```ts
import { generateText } from 'ai';import { MockLanguageModelV2 } from 'ai/test';
const result = await generateText({  model: new MockLanguageModelV2({    doGenerate: async () => ({      finishReason: 'stop',      usage: { inputTokens: 10, outputTokens: 20, totalTokens: 30 },      content: [{ type: 'text', text: `Hello, world!` }],      warnings: [],    }),  }),  prompt: 'Hello, test!',});
```

```ts
import { streamText, simulateReadableStream } from 'ai';import { MockLanguageModelV2 } from 'ai/test';
const result = streamText({  model: new MockLanguageModelV2({    doStream: async () => ({      stream: simulateReadableStream({        chunks: [          { type: 'text-start', id: 'text-1' },          { type: 'text-delta', id: 'text-1', delta: 'Hello' },          { type: 'text-delta', id: 'text-1', delta: ', ' },          { type: 'text-delta', id: 'text-1', delta: 'world!' },          { type: '
...
```

---

## Tool Calling

**URL**: https://ai-sdk.dev/docs/ai-sdk-core/tools-and-tool-calling

**Contents**:
- Tool Calling
- Multi-Step Calls (using stopWhen)
  - Example
  - Steps
    - Example: Extract tool results from all steps
  - onStepFinish callback
  - prepareStep callback
    - Message Modification for Longer Agentic Loops

As covered under Foundations, tools are objects that can be called by the model to perform a specific task. AI SDK Core tools contain three elements:

You can use the tool helper function to infer the types of the execute parameters.

The tools parameter of generateText and streamText is an object that has the tool names as keys and the tools as values:

When a model uses a tool, it is called a "tool call" and the output of the tool is called a "tool result".

Tool calling is not restricted to only text generation. You can also use it to render user interfaces (Generative UI).

With the stopWhen setting, you can enable multi-step calls in generateText and streamText. When stopWhen is set and the model generates a tool call, the AI SDK will trigger a new generation passing in the tool result until there are no further tool calls or the stopping condition is met.

The stopWhen conditions are only evaluated when the last step contains tool results.

By default, when you use generateText or streamText, it triggers a single generation. This works well for many use cases where you can rely on the model's training data to generate a response. However, when you provide tools, the model now has the choice to either generate a normal text response, or generate a tool call. If the model generates a tool call, it's generation is complete and that step is finished.

You may want the model to generate text after the tool has been executed, either to summarize the tool results in the context of the users query. In many cases, you may also want the model to use multiple tools in a single response. This is where multi-step calls come in.

You can think of multi-step calls in a similar way to a conversation with a human. When you ask a question, if the person does not have the requisite knowledge in their common knowledge (a model's training data), the person may need to look up information (use a tool) before they can provide you with an answer. In the same way, the model may need t

*[Content truncated - see full docs]*

**Examples**:

```ts
import { z } from 'zod';import { generateText, tool } from 'ai';
const result = await generateText({  model: 'openai/gpt-4o',  tools: {    weather: tool({      description: 'Get the weather in a location',      inputSchema: z.object({        location: z.string().describe('The location to get the weather for'),      }),      execute: async ({ location }) => ({        location,        temperature: 72 + Math.floor(Math.random() * 21) - 10,      }),    }),  },  prompt: 'What is the weather in San Fr
...
```

```ts
import { z } from 'zod';import { generateText, tool } from 'ai';
const result = await generateText({  model: 'openai/gpt-4o',  tools: {    weather: tool({      description: 'Get the weather in a location',      inputSchema: z.object({        location: z.string().describe('The location to get the weather for'),      }),      execute: async ({ location }) => ({        location,        temperature: 72 + Math.floor(Math.random() * 21) - 10,      }),    }),  },  prompt: 'What is the weather in San Fr
...
```

```ts
import { z } from 'zod';import { generateText, tool, stepCountIs } from 'ai';
const { text, steps } = await generateText({  model: 'openai/gpt-4o',  tools: {    weather: tool({      description: 'Get the weather in a location',      inputSchema: z.object({        location: z.string().describe('The location to get the weather for'),      }),      execute: async ({ location }) => ({        location,        temperature: 72 + Math.floor(Math.random() * 21) - 10,      }),    }),  },  stopWhen: stepCo
...
```

---

## Transcription

**URL**: https://ai-sdk.dev/docs/ai-sdk-core/transcription

**Contents**:
- Transcription
- Settings
  - Provider-Specific settings
  - Abort Signals and Timeouts
  - Custom Headers
  - Warnings
  - Error Handling
- Transcription Models

The AI SDK provides the transcribe function to transcribe audio using a transcription model.

The audio property can be a Uint8Array, ArrayBuffer, Buffer, string (base64 encoded audio data), or a URL.

To access the generated transcript:

Transcription models often have provider or model-specific settings which you can set using the providerOptions parameter.

transcribe accepts an optional abortSignal parameter of type AbortSignal that you can use to abort the transcription process or set a timeout.

transcribe accepts an optional headers parameter of type Record<string, string> that you can use to add custom headers to the transcription request.

Warnings (e.g. unsupported parameters) are available on the warnings property.

When transcribe cannot generate a valid transcript, it throws a AI_NoTranscriptGeneratedError.

This error can arise for any the following reasons:

The error preserves the following information to help you log the issue:

Above are a small subset of the transcription models supported by the AI SDK providers. For more, see the respective provider documentation.

**Examples**:

```ts
import { experimental_transcribe as transcribe } from 'ai';import { openai } from '@ai-sdk/openai';import { readFile } from 'fs/promises';
const transcript = await transcribe({  model: openai.transcription('whisper-1'),  audio: await readFile('audio.mp3'),});
```

```ts
import { experimental_transcribe as transcribe } from 'ai';import { openai } from '@ai-sdk/openai';import { readFile } from 'fs/promises';
const transcript = await transcribe({  model: openai.transcription('whisper-1'),  audio: await readFile('audio.mp3'),});
```

```ts
const text = transcript.text; // transcript text e.g. "Hello, world!"const segments = transcript.segments; // array of segments with start and end times, if availableconst language = transcript.language; // language of the transcript e.g. "en", if availableconst durationInSeconds = transcript.durationInSeconds; // duration of the transcript in seconds, if available
```

---

## UIMessage

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-core/ui-message

**Contents**:
- UIMessage
- Type Safety
- Creating Your Own UIMessage Type
- UIMessage Interface
- UIMessagePart Types
  - TextUIPart
  - ReasoningUIPart
  - ToolUIPart

UIMessage serves as the source of truth for your application's state, representing the complete message history including metadata, data parts, and all contextual information. In contrast to ModelMessage, which represents the state or context passed to the model, UIMessage contains the full application state needed for UI rendering and client-side functionality.

UIMessage is designed to be type-safe and accepts three generic parameters to ensure proper typing throughout your application:

Here's an example of how to create a custom typed UIMessage for your application:

A text part of a message.

A reasoning part of a message.

A tool part of a message that represents tool invocations and their results.

The type is based on the name of the tool (e.g., tool-someTool for a tool named someTool).

A source URL part of a message.

A document source part of a message.

A file part of a message.

A data part of a message for custom data types.

The type is based on the name of the data part (e.g., data-someDataPart for a data part named someDataPart).

A step boundary part of a message.

**Examples**:

```typescript
import { InferUITools, ToolSet, UIMessage, tool } from 'ai';import z from 'zod';
const metadataSchema = z.object({  someMetadata: z.string().datetime(),});
type MyMetadata = z.infer<typeof metadataSchema>;
const dataPartSchema = z.object({  someDataPart: z.object({}),  anotherDataPart: z.object({}),});
type MyDataPart = z.infer<typeof dataPartSchema>;
const tools = {  someTool: tool({}),} satisfies ToolSet;
type MyTools = InferUITools<typeof tools>;
export type MyUIMessage = UIMessage<MyMetadata
...
```

```typescript
import { InferUITools, ToolSet, UIMessage, tool } from 'ai';import z from 'zod';
const metadataSchema = z.object({  someMetadata: z.string().datetime(),});
type MyMetadata = z.infer<typeof metadataSchema>;
const dataPartSchema = z.object({  someDataPart: z.object({}),  anotherDataPart: z.object({}),});
type MyDataPart = z.infer<typeof dataPartSchema>;
const tools = {  someTool: tool({}),} satisfies ToolSet;
type MyTools = InferUITools<typeof tools>;
export type MyUIMessage = UIMessage<MyMetadata
...
```

```typescript
interface UIMessage<  METADATA = unknown,  DATA_PARTS extends UIDataTypes = UIDataTypes,  TOOLS extends UITools = UITools,> {  /**   * A unique identifier for the message.   */  id: string;
  /**   * The role of the message.   */  role: 'system' | 'user' | 'assistant';
  /**   * The metadata of the message.   */  metadata?: METADATA;
  /**   * The parts of the message. Use this for rendering the message in the UI.   */  parts: Array<UIMessagePart<DATA_PARTS, TOOLS>>;}
```

---

## convertToModelMessages()

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-ui/convert-to-model-messages

**Contents**:
- convertToModelMessages()
- Import
- API Signature
  - Parameters
  - messages:
  - options:
  - Returns
  - ModelMessage[]:

The convertToModelMessages function is used to transform an array of UI messages from the useChat hook into an array of ModelMessage objects. These ModelMessage objects are compatible with AI core functions like streamText.

An array of ModelMessage objects.

The convertToModelMessages function supports tools that can return multi-modal content. This is useful when tools need to return non-text content like images.

Tools can implement the optional toModelOutput method to transform their results into multi-modal content. The content is an array of content parts, where each part has a type (e.g., 'text', 'image') and corresponding data.

**Examples**:

```ts
import { openai } from '@ai-sdk/openai';import { convertToModelMessages, streamText } from 'ai';
export async function POST(req: Request) {  const { messages } = await req.json();
  const result = streamText({    model: openai('gpt-4o'),    messages: convertToModelMessages(messages),  });
  return result.toUIMessageStreamResponse();}
```

```ts
import { openai } from '@ai-sdk/openai';import { convertToModelMessages, streamText } from 'ai';
export async function POST(req: Request) {  const { messages } = await req.json();
  const result = streamText({    model: openai('gpt-4o'),    messages: convertToModelMessages(messages),  });
  return result.toUIMessageStreamResponse();}
```

```python
import { convertToModelMessages } from "ai"
```

---

## cosineSimilarity()

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-core/cosine-similarity

**Contents**:
- cosineSimilarity()
- Import
- API Signature
  - Parameters
  - vector1:
  - vector2:
  - Returns

When you want to compare the similarity of embeddings, standard vector similarity metrics like cosine similarity are often used.

cosineSimilarity calculates the cosine similarity between two vectors. A high value (close to 1) indicates that the vectors are very similar, while a low value (close to -1) indicates that they are different.

A number between -1 and 1 representing the cosine similarity between the two vectors.

**Examples**:

```ts
import { openai } from '@ai-sdk/openai';import { cosineSimilarity, embedMany } from 'ai';
const { embeddings } = await embedMany({  model: openai.textEmbeddingModel('text-embedding-3-small'),  values: ['sunny day at the beach', 'rainy afternoon in the city'],});
console.log(  `cosine similarity: ${cosineSimilarity(embeddings[0], embeddings[1])}`,);
```

```ts
import { openai } from '@ai-sdk/openai';import { cosineSimilarity, embedMany } from 'ai';
const { embeddings } = await embedMany({  model: openai.textEmbeddingModel('text-embedding-3-small'),  values: ['sunny day at the beach', 'rainy afternoon in the city'],});
console.log(  `cosine similarity: ${cosineSimilarity(embeddings[0], embeddings[1])}`,);
```

```python
import { cosineSimilarity } from "ai"
```

---

## createIdGenerator()

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-core/create-id-generator

**Contents**:
- createIdGenerator()
- Import
- API Signature
  - Parameters
  - options:
  - options.alphabet:
  - options.prefix:
  - options.separator:

Creates a customizable ID generator function. You can configure the alphabet, prefix, separator, and default size of the generated IDs.

Returns a function that generates IDs based on the configured options.

**Examples**:

```ts
import { createIdGenerator } from 'ai';
const generateCustomId = createIdGenerator({  prefix: 'user',  separator: '_',});
const id = generateCustomId(); // Example: "user_1a2b3c4d5e6f7g8h"
```

```ts
import { createIdGenerator } from 'ai';
const generateCustomId = createIdGenerator({  prefix: 'user',  separator: '_',});
const id = generateCustomId(); // Example: "user_1a2b3c4d5e6f7g8h"
```

```python
import { createIdGenerator } from "ai"
```

---

## createProviderRegistry()

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-core/provider-registry

**Contents**:
- createProviderRegistry()
  - Setup
  - Custom Separator
  - Language models
  - Text embedding models
  - Image models
- Import
- API Signature

When you work with multiple providers and models, it is often desirable to manage them in a central place and access the models through simple string ids.

createProviderRegistry lets you create a registry with multiple providers that you can access by their ids in the format providerId:modelId.

You can create a registry with multiple providers and models using createProviderRegistry.

By default, the registry uses : as the separator between provider and model IDs. You can customize this separator by passing a separator option:

You can access language models by using the languageModel method on the registry. The provider id will become the prefix of the model id: providerId:modelId.

You can access text embedding models by using the textEmbeddingModel method on the registry. The provider id will become the prefix of the model id: providerId:modelId.

You can access image models by using the imageModel method on the registry. The provider id will become the prefix of the model id: providerId:modelId.

The createProviderRegistry function returns a Provider instance. It has the following methods:

**Examples**:

```ts
import { anthropic } from '@ai-sdk/anthropic';import { createOpenAI } from '@ai-sdk/openai';import { createProviderRegistry } from 'ai';
export const registry = createProviderRegistry({  // register provider with prefix and default setup:  anthropic,
  // register provider with prefix and custom setup:  openai: createOpenAI({    apiKey: process.env.OPENAI_API_KEY,  }),});
```

```ts
import { anthropic } from '@ai-sdk/anthropic';import { createOpenAI } from '@ai-sdk/openai';import { createProviderRegistry } from 'ai';
export const registry = createProviderRegistry({  // register provider with prefix and default setup:  anthropic,
  // register provider with prefix and custom setup:  openai: createOpenAI({    apiKey: process.env.OPENAI_API_KEY,  }),});
```

```ts
const registry = createProviderRegistry(  {    anthropic,    openai,  },  { separator: ' > ' },);
// Now you can use the custom separatorconst model = registry.languageModel('anthropic > claude-3-opus-20240229');
```

---

## createStreamableUI

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-rsc/create-streamable-ui

**Contents**:
- createStreamableUI
- Import
- API Signature
  - Parameters
  - initialValue?:
  - Returns
  - value:
  - Methods

AI SDK RSC is currently experimental. We recommend using AI SDK UI for production. For guidance on migrating from RSC to UI, see our migration guide.

Create a stream that sends UI from the server to the client. On the client side, it can be rendered as a normal React node.

**Examples**:

```python
import { createStreamableUI } from "@ai-sdk/rsc"
```

---

## createStreamableValue

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-rsc/create-streamable-value

**Contents**:
- createStreamableValue
- Import
- API Signature
  - Parameters
  - value:
  - Returns
  - value:

AI SDK RSC is currently experimental. We recommend using AI SDK UI for production. For guidance on migrating from RSC to UI, see our migration guide.

Create a stream that sends values from the server to the client. The value can be any serializable data.

**Examples**:

```python
import { createStreamableValue } from "@ai-sdk/rsc"
```

---

## createUIMessageStreamResponse

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-ui/create-ui-message-stream-response

**Contents**:
- createUIMessageStreamResponse
- Import
- Example
- API Signature
  - Parameters
  - stream:
  - status?:
  - statusText?:

The createUIMessageStreamResponse function creates a Response object that streams UI messages to the client.

A Response object that streams UI message chunks with the specified status, headers, and content.

**Examples**:

```python
import { createUIMessageStreamResponse } from "ai"
```

```tsx
import { createUIMessageStream, createUIMessageStreamResponse } from 'ai';
const response = createUIMessageStreamResponse({  status: 200,  statusText: 'OK',  headers: {    'Custom-Header': 'value',  },  stream: createUIMessageStream({    execute({ writer }) {      // Write custom data      writer.write({        type: 'data',        value: { message: 'Hello' },      });
      // Write text content      writer.write({        type: 'text',        value: 'Hello, world!',      });
      // Write sour
...
```

```tsx
import { createUIMessageStream, createUIMessageStreamResponse } from 'ai';
const response = createUIMessageStreamResponse({  status: 200,  statusText: 'OK',  headers: {    'Custom-Header': 'value',  },  stream: createUIMessageStream({    execute({ writer }) {      // Write custom data      writer.write({        type: 'data',        value: { message: 'Hello' },      });
      // Write text content      writer.write({        type: 'text',        value: 'Hello, world!',      });
      // Write sour
...
```

---

## createUIMessageStream

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-ui/create-ui-message-stream

**Contents**:
- createUIMessageStream
- Import
- Example
- API Signature
  - Parameters
  - execute:
  - write:
  - merge:

The createUIMessageStream function allows you to create a readable stream for UI messages with advanced features like message merging, error handling, and finish callbacks.

ReadableStream<UIMessageChunk>

A readable stream that emits UI message chunks. The stream automatically handles error propagation, merging of multiple streams, and proper cleanup when all operations are complete.

**Examples**:

```python
import { createUIMessageStream } from "ai"
```

```tsx
const existingMessages: UIMessage[] = [  /* ... */];
const stream = createUIMessageStream({  async execute({ writer }) {    // Start a text message    // Note: The id must be consistent across text-start, text-delta, and text-end steps    // This allows the system to correctly identify they belong to the same text block    writer.write({      type: 'text-start',      id: 'example-text',    });
    // Write a message chunk    writer.write({      type: 'text-delta',      id: 'example-text',      d
...
```

```tsx
const existingMessages: UIMessage[] = [  /* ... */];
const stream = createUIMessageStream({  async execute({ writer }) {    // Start a text message    // Note: The id must be consistent across text-start, text-delta, and text-end steps    // This allows the system to correctly identify they belong to the same text block    writer.write({      type: 'text-start',      id: 'example-text',    });
    // Write a message chunk    writer.write({      type: 'text-delta',      id: 'example-text',      d
...
```

---

## customProvider()

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-core/custom-provider

**Contents**:
- customProvider()
  - Example: custom model settings
- Import
- API Signature
  - Parameters
  - languageModels?:
  - textEmbeddingModels?:
  - imageModels?:

With a custom provider, you can map ids to any model. This allows you to set up custom model configurations, alias names, and more. The custom provider also supports a fallback provider, which is useful for wrapping existing providers and adding additional functionality.

You can create a custom provider using customProvider.

The customProvider function returns a Provider instance. It has the following methods:

**Examples**:

```ts
import { openai } from '@ai-sdk/openai';import { customProvider } from 'ai';
// custom provider with different model settings:export const myOpenAI = customProvider({  languageModels: {    // replacement model with custom settings:    'gpt-4': wrapLanguageModel({      model: openai('gpt-4'),      middleware: defaultSettingsMiddleware({        settings: {          providerOptions: {            openai: {              reasoningEffort: 'high',            },          },        },      }),    }),    /
...
```

```ts
import { openai } from '@ai-sdk/openai';import { customProvider } from 'ai';
// custom provider with different model settings:export const myOpenAI = customProvider({  languageModels: {    // replacement model with custom settings:    'gpt-4': wrapLanguageModel({      model: openai('gpt-4'),      middleware: defaultSettingsMiddleware({        settings: {          providerOptions: {            openai: {              reasoningEffort: 'high',            },          },        },      }),    }),    /
...
```

```python
import {  customProvider } from "ai"
```

---

## defaultSettingsMiddleware()

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-core/default-settings-middleware

**Contents**:
- defaultSettingsMiddleware()
- Import
- API Signature
  - Parameters
  - Returns
  - Usage Example
- How It Works

defaultSettingsMiddleware is a middleware function that applies default settings to language model calls. This is useful when you want to establish consistent default parameters across multiple model invocations.

The middleware accepts a configuration object with the following properties:

Returns a middleware object that:

**Examples**:

```ts
import { defaultSettingsMiddleware } from 'ai';
const middleware = defaultSettingsMiddleware({  settings: {    temperature: 0.7,    maxOutputTokens: 1000,    // other settings...  },});
```

```ts
import { defaultSettingsMiddleware } from 'ai';
const middleware = defaultSettingsMiddleware({  settings: {    temperature: 0.7,    maxOutputTokens: 1000,    // other settings...  },});
```

```python
import { defaultSettingsMiddleware } from "ai"
```

---

## dynamicTool()

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-core/dynamic-tool

**Contents**:
- dynamicTool()
- Import
- API Signature
  - Parameters
  - tool:
  - description?:
  - inputSchema:
  - execute:

The dynamicTool function creates tools where the input and output types are not known at compile time. This is useful for scenarios such as:

Unlike the regular tool function, dynamicTool accepts and returns unknown types, allowing you to work with tools that have runtime-determined schemas.

A Tool<unknown, unknown> with type: 'dynamic' that can be used with generateText, streamText, and other AI SDK functions.

When using dynamic tools alongside static tools, you need to check the dynamic flag for proper type narrowing:

When used with useChat (UIMessage format), dynamic tools appear as dynamic-tool parts:

**Examples**:

```ts
import { dynamicTool } from 'ai';import { z } from 'zod';
export const customTool = dynamicTool({  description: 'Execute a custom user-defined function',  inputSchema: z.object({}),  // input is typed as 'unknown'  execute: async input => {    const { action, parameters } = input as any;
    // Execute your dynamic logic    return {      result: `Executed ${action} with ${JSON.stringify(parameters)}`,    };  },});
```

```ts
import { dynamicTool } from 'ai';import { z } from 'zod';
export const customTool = dynamicTool({  description: 'Execute a custom user-defined function',  inputSchema: z.object({}),  // input is typed as 'unknown'  execute: async input => {    const { action, parameters } = input as any;
    // Execute your dynamic logic    return {      result: `Executed ${action} with ${JSON.stringify(parameters)}`,    };  },});
```

```python
import { dynamicTool } from "ai"
```

---

## embedMany()

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-core/embed-many

**Contents**:
- embedMany()
- Import
- API Signature
  - Parameters
  - model:
  - values:
  - maxRetries?:
  - abortSignal?:

Embed several values using an embedding model. The type of the value is defined by the embedding model.

embedMany automatically splits large requests into smaller chunks if the model has a limit on how many embeddings can be generated in a single call.

**Examples**:

```ts
import { openai } from '@ai-sdk/openai';import { embedMany } from 'ai';
const { embeddings } = await embedMany({  model: openai.textEmbeddingModel('text-embedding-3-small'),  values: [    'sunny day at the beach',    'rainy afternoon in the city',    'snowy night in the mountains',  ],});
```

```ts
import { openai } from '@ai-sdk/openai';import { embedMany } from 'ai';
const { embeddings } = await embedMany({  model: openai.textEmbeddingModel('text-embedding-3-small'),  values: [    'sunny day at the beach',    'rainy afternoon in the city',    'snowy night in the mountains',  ],});
```

```python
import { embedMany } from "ai"
```

---

## embed()

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-core/embed

**Contents**:
- embed()
- Import
- API Signature
  - Parameters
  - model:
  - value:
  - maxRetries?:
  - abortSignal?:

Generate an embedding for a single value using an embedding model.

This is ideal for use cases where you need to embed a single value to e.g. retrieve similar items or to use the embedding in a downstream task.

**Examples**:

```ts
import { openai } from '@ai-sdk/openai';import { embed } from 'ai';
const { embedding } = await embed({  model: openai.textEmbeddingModel('text-embedding-3-small'),  value: 'sunny day at the beach',});
```

```ts
import { openai } from '@ai-sdk/openai';import { embed } from 'ai';
const { embedding } = await embed({  model: openai.textEmbeddingModel('text-embedding-3-small'),  value: 'sunny day at the beach',});
```

```python
import { embed } from "ai"
```

---

## experimental_createMCPClient()

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-core/create-mcp-client

**Contents**:
- experimental_createMCPClient()
- Import
- API Signature
  - Parameters
  - config:
  - transport:
  - start:
  - send:

Creates a lightweight Model Context Protocol (MCP) client that connects to an MCP server. The client's primary purpose is tool conversion between MCP tools and AI SDK tools.

It currently does not support accepting notifications from an MCP server, and custom configuration of the client.

This feature is experimental and may change or be removed in the future.

Returns a Promise that resolves to an MCPClient with the following methods:

The client throws MCPClientError for:

For tool execution, errors are propagated as CallToolError errors.

For unknown errors, the client exposes an onUncaughtError callback that can be used to manually log or handle errors that are not covered by known error types.

**Examples**:

```python
import { experimental_createMCPClient } from "ai"
```

```typescript
import { experimental_createMCPClient, generateText } from 'ai';import { Experimental_StdioMCPTransport } from 'ai/mcp-stdio';import { openai } from '@ai-sdk/openai';
let client;
try {  client = await experimental_createMCPClient({    transport: new Experimental_StdioMCPTransport({      command: 'node server.js',    }),  });
  const tools = await client.tools();
  const response = await generateText({    model: openai('gpt-4o-mini'),    tools,    messages: [{ role: 'user', content: 'Query the da
...
```

```typescript
import { experimental_createMCPClient, generateText } from 'ai';import { Experimental_StdioMCPTransport } from 'ai/mcp-stdio';import { openai } from '@ai-sdk/openai';
let client;
try {  client = await experimental_createMCPClient({    transport: new Experimental_StdioMCPTransport({      command: 'node server.js',    }),  });
  const tools = await client.tools();
  const response = await generateText({    model: openai('gpt-4o-mini'),    tools,    messages: [{ role: 'user', content: 'Query the da
...
```

---

## extractReasoningMiddleware()

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-core/extract-reasoning-middleware

**Contents**:
- extractReasoningMiddleware()
- Import
- API Signature
  - Parameters
  - tagName:
  - separator?:
  - startWithReasoning?:
  - Returns

extractReasoningMiddleware is a middleware function that extracts XML-tagged reasoning sections from generated text and exposes them separately from the main text content. This is particularly useful when you want to separate an AI model's reasoning process from its final output.

Returns a middleware object that:

The middleware works with the LanguageModelV2StreamPart type for streaming responses.

**Examples**:

```ts
import { extractReasoningMiddleware } from 'ai';
const middleware = extractReasoningMiddleware({  tagName: 'reasoning',  separator: '\n',});
```

```ts
import { extractReasoningMiddleware } from 'ai';
const middleware = extractReasoningMiddleware({  tagName: 'reasoning',  separator: '\n',});
```

```python
import { extractReasoningMiddleware } from "ai"
```

---

## generateId()

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-core/generate-id

**Contents**:
- generateId()
- Import
- API Signature
  - Parameters
  - size:
  - Returns
- See also

Generates a unique identifier. You can optionally provide the length of the ID.

This is the same id generator used by the AI SDK.

A string representing the generated ID.

**Examples**:

```ts
import { generateId } from 'ai';
const id = generateId();
```

```ts
import { generateId } from 'ai';
const id = generateId();
```

```python
import { generateId } from "ai"
```

---

## generateImage()

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-core/generate-image

**Contents**:
- generateImage()
- Import
- API Signature
  - Parameters
  - model:
  - prompt:
  - n?:
  - size?:

Generates images based on a given prompt using an image model.

It is ideal for use cases where you need to generate images programmatically, such as creating visual content or generating images for data augmentation.

**Examples**:

```ts
import { experimental_generateImage as generateImage } from 'ai';
const { images } = await generateImage({  model: openai.image('dall-e-3'),  prompt: 'A futuristic cityscape at sunset',  n: 3,  size: '1024x1024',});
console.log(images);
```

```ts
import { experimental_generateImage as generateImage } from 'ai';
const { images } = await generateImage({  model: openai.image('dall-e-3'),  prompt: 'A futuristic cityscape at sunset',  n: 3,  size: '1024x1024',});
console.log(images);
```

```python
import { experimental_generateImage as generateImage } from "ai"
```

---

## generateObject()

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-core/generate-object

**Contents**:
- generateObject()
    - Example: generate an object using a schema
    - Example: generate an array using a schema
    - Example: generate an enum
    - Example: generate JSON without a schema
- Import
- API Signature
  - Parameters

Generates a typed, structured object for a given prompt and schema using a language model.

It can be used to force the language model to return structured data, e.g. for information extraction, synthetic data generation, or classification tasks.

For arrays, you specify the schema of the array items.

When you want to generate a specific enum value, you can set the output strategy to enum and provide the list of possible values in the enum parameter.

To see generateObject in action, check out the additional examples.

**Examples**:

```ts
import { openai } from '@ai-sdk/openai';import { generateObject } from 'ai';import { z } from 'zod';
const { object } = await generateObject({  model: openai('gpt-4.1'),  schema: z.object({    recipe: z.object({      name: z.string(),      ingredients: z.array(z.string()),      steps: z.array(z.string()),    }),  }),  prompt: 'Generate a lasagna recipe.',});
console.log(JSON.stringify(object, null, 2));
```

```ts
import { openai } from '@ai-sdk/openai';import { generateObject } from 'ai';import { z } from 'zod';
const { object } = await generateObject({  model: openai('gpt-4.1'),  schema: z.object({    recipe: z.object({      name: z.string(),      ingredients: z.array(z.string()),      steps: z.array(z.string()),    }),  }),  prompt: 'Generate a lasagna recipe.',});
console.log(JSON.stringify(object, null, 2));
```

```ts
import { openai } from '@ai-sdk/openai';import { generateObject } from 'ai';import { z } from 'zod';
const { object } = await generateObject({  model: openai('gpt-4.1'),  output: 'array',  schema: z.object({    name: z.string(),    class: z      .string()      .describe('Character class, e.g. warrior, mage, or thief.'),    description: z.string(),  }),  prompt: 'Generate 3 hero descriptions for a fantasy role playing game.',});
```

---

## generateSpeech()

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-core/generate-speech

**Contents**:
- generateSpeech()
- Examples
  - OpenAI
  - ElevenLabs
- Import
- API Signature
  - Parameters
  - model:

Generates speech audio from text.

**Examples**:

```ts
import { experimental_generateSpeech as generateSpeech } from 'ai';import { openai } from '@ai-sdk/openai';
const { audio } = await generateSpeech({  model: openai.speech('tts-1'),  text: 'Hello from the AI SDK!',  voice: 'alloy',});
console.log(audio);
```

```ts
import { experimental_generateSpeech as generateSpeech } from 'ai';import { openai } from '@ai-sdk/openai';
const { audio } = await generateSpeech({  model: openai.speech('tts-1'),  text: 'Hello from the AI SDK!',  voice: 'alloy',});
console.log(audio);
```

```ts
import { experimental_generateSpeech as generateSpeech } from 'ai';import { openai } from '@ai-sdk/openai';
const { audio } = await generateSpeech({  model: openai.speech('tts-1'),  text: 'Hello from the AI SDK!',  voice: 'alloy',});
```

---

## generateText()

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-core/generate-text

**Contents**:
- generateText()
- Import
- API Signature
  - Parameters
  - model:
  - system:
  - prompt:
  - messages:

Generates text and calls tools for a given prompt using a language model.

It is ideal for non-interactive use cases such as automation tasks where you need to write text (e.g. drafting email or summarizing web pages) and for agents that use tools.

To see generateText in action, check out these examples.

**Examples**:

```ts
import { openai } from '@ai-sdk/openai';import { generateText } from 'ai';
const { text } = await generateText({  model: openai('gpt-4o'),  prompt: 'Invent a new holiday and describe its traditions.',});
console.log(text);
```

```ts
import { openai } from '@ai-sdk/openai';import { generateText } from 'ai';
const { text } = await generateText({  model: openai('gpt-4o'),  prompt: 'Invent a new holiday and describe its traditions.',});
console.log(text);
```

```python
import { generateText } from "ai"
```

---

## hasToolCall()

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-core/has-tool-call

**Contents**:
- hasToolCall()
- Import
- API Signature
  - Parameters
  - toolName:
  - Returns
- Examples
  - Basic Usage

Creates a stop condition that stops when a specific tool is called.

This function is used with stopWhen in generateText and streamText to control when a tool-calling loop should stop based on whether a particular tool has been invoked.

A StopCondition function that returns true when the specified tool is called in the current step. The function can be used with the stopWhen parameter in generateText and streamText.

Stop when a specific tool is called:

You can combine multiple stop conditions in an array:

Common pattern for agents that run until they provide a final answer:

**Examples**:

```ts
import { openai } from '@ai-sdk/openai';import { generateText, hasToolCall } from 'ai';
const result = await generateText({  model: openai('gpt-4o'),  tools: {    weather: weatherTool,    finalAnswer: finalAnswerTool,  },  // Stop when the finalAnswer tool is called  stopWhen: hasToolCall('finalAnswer'),});
```

```ts
import { openai } from '@ai-sdk/openai';import { generateText, hasToolCall } from 'ai';
const result = await generateText({  model: openai('gpt-4o'),  tools: {    weather: weatherTool,    finalAnswer: finalAnswerTool,  },  // Stop when the finalAnswer tool is called  stopWhen: hasToolCall('finalAnswer'),});
```

```python
import { hasToolCall } from "ai"
```

---

## jsonSchema()

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-core/json-schema

**Contents**:
- jsonSchema()
- Import
- API Signature
  - Parameters
  - schema:
  - options:
  - validate?:
  - Returns

jsonSchema is a helper function that creates a JSON schema object that is compatible with the AI SDK. It takes the JSON schema and an optional validation function as inputs, and can be typed.

You can use it to generate structured data and in tools.

jsonSchema is an alternative to using Zod schemas that provides you with flexibility in dynamic situations (e.g. when using OpenAPI definitions) or for using other validation libraries.

A JSON schema object that is compatible with the AI SDK.

**Examples**:

```ts
import { jsonSchema } from 'ai';
const mySchema = jsonSchema<{  recipe: {    name: string;    ingredients: { name: string; amount: string }[];    steps: string[];  };}>({  type: 'object',  properties: {    recipe: {      type: 'object',      properties: {        name: { type: 'string' },        ingredients: {          type: 'array',          items: {            type: 'object',            properties: {              name: { type: 'string' },              amount: { type: 'string' },            },  
...
```

```ts
import { jsonSchema } from 'ai';
const mySchema = jsonSchema<{  recipe: {    name: string;    ingredients: { name: string; amount: string }[];    steps: string[];  };}>({  type: 'object',  properties: {    recipe: {      type: 'object',      properties: {        name: { type: 'string' },        ingredients: {          type: 'array',          items: {            type: 'object',            properties: {              name: { type: 'string' },              amount: { type: 'string' },            },  
...
```

```python
import { jsonSchema } from "ai"
```

---

## pipeUIMessageStreamToResponse

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-ui/pipe-ui-message-stream-to-response

**Contents**:
- pipeUIMessageStreamToResponse
- Import
- Example
- API Signature
  - Parameters
  - response:
  - stream:
  - status:

The pipeUIMessageStreamToResponse function pipes streaming data to a Node.js ServerResponse object (see Streaming Data).

**Examples**:

```python
import { pipeUIMessageStreamToResponse } from "ai"
```

```tsx
pipeUIMessageStreamToResponse({  response: serverResponse,  status: 200,  statusText: 'OK',  headers: {    'Custom-Header': 'value',  },  stream: myUIMessageStream,  consumeSseStream: ({ stream }) => {    // Optional: consume the SSE stream independently    console.log('Consuming SSE stream:', stream);  },});
```

```tsx
pipeUIMessageStreamToResponse({  response: serverResponse,  status: 200,  statusText: 'OK',  headers: {    'Custom-Header': 'value',  },  stream: myUIMessageStream,  consumeSseStream: ({ stream }) => {    // Optional: consume the SSE stream independently    console.log('Consuming SSE stream:', stream);  },});
```

---

## readUIMessageStream

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-ui/read-ui-message-stream

**Contents**:
- readUIMessageStream
- Import
- API Signature
  - Parameters
  - message?:
  - stream:
  - onError?:
  - terminateOnError?:

Transforms a stream of UIMessageChunks into an AsyncIterableStream of UIMessages.

UI message streams are useful outside of Chat use cases, e.g. for terminal UIs, custom stream consumption on the client, or RSC (React Server Components).

An AsyncIterableStream of UIMessages. Each stream part represents a different state of the same message as it is being completed.

For comprehensive examples and use cases, see Reading UI Message Streams.

**Examples**:

```tsx
import { readUIMessageStream } from 'ai';
```

```tsx
import { readUIMessageStream } from 'ai';
```

---

## safeValidateUIMessages

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-core/safe-validate-ui-messages

**Contents**:
- safeValidateUIMessages
- Basic Usage
- Advanced Usage

safeValidateUIMessages is an async function that validates UI messages like validateUIMessages, but instead of throwing it returns an object with a success key and either data or error.

Simple validation without custom schemas:

Comprehensive validation with custom metadata, data parts, and tools:

**Examples**:

```typescript
import { safeValidateUIMessages } from 'ai';
const messages = [  {    id: '1',    role: 'user',    parts: [{ type: 'text', text: 'Hello!' }],  },];
const result = await safeValidateUIMessages({  messages,});
if (!result.success) {  console.error(result.error.message);} else {  const validatedMessages = result.data;}
```

```typescript
import { safeValidateUIMessages } from 'ai';
const messages = [  {    id: '1',    role: 'user',    parts: [{ type: 'text', text: 'Hello!' }],  },];
const result = await safeValidateUIMessages({  messages,});
if (!result.success) {  console.error(result.error.message);} else {  const validatedMessages = result.data;}
```

```typescript
import { safeValidateUIMessages, tool } from 'ai';import { z } from 'zod';
// Define schemasconst metadataSchema = z.object({  timestamp: z.string().datetime(),  userId: z.string(),});
const dataSchemas = {  chart: z.object({    data: z.array(z.number()),    labels: z.array(z.string()),  }),  image: z.object({    url: z.string().url(),    caption: z.string(),  }),};
const tools = {  weather: tool({    description: 'Get weather info',    parameters: z.object({      location: z.string(),    }),   
...
```

---

## simulateReadableStream()

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-core/simulate-readable-stream

**Contents**:
- simulateReadableStream()
- Import
- API Signature
  - Parameters
  - chunks:
  - initialDelayInMs?:
  - chunkDelayInMs?:
  - Returns

simulateReadableStream is a utility function that creates a ReadableStream which emits provided values sequentially with configurable delays. This is particularly useful for testing streaming functionality or simulating time-delayed data streams.

Returns a ReadableStream<T> that:

**Examples**:

```ts
import { simulateReadableStream } from 'ai';
const stream = simulateReadableStream({  chunks: ['Hello', ' ', 'World'],  initialDelayInMs: 100,  chunkDelayInMs: 50,});
```

```ts
import { simulateReadableStream } from 'ai';
const stream = simulateReadableStream({  chunks: ['Hello', ' ', 'World'],  initialDelayInMs: 100,  chunkDelayInMs: 50,});
```

```python
import { simulateReadableStream } from "ai"
```

---

## simulateStreamingMiddleware()

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-core/simulate-streaming-middleware

**Contents**:
- simulateStreamingMiddleware()
- Import
- API Signature
  - Parameters
  - Returns
  - Usage Example
- How It Works

simulateStreamingMiddleware is a middleware function that simulates streaming behavior with responses from non-streaming language models. This is useful when you want to maintain a consistent streaming interface even when using models that only provide complete responses.

This middleware doesn't accept any parameters.

Returns a middleware object that:

**Examples**:

```ts
import { simulateStreamingMiddleware } from 'ai';
const middleware = simulateStreamingMiddleware();
```

```ts
import { simulateStreamingMiddleware } from 'ai';
const middleware = simulateStreamingMiddleware();
```

```python
import { simulateStreamingMiddleware } from "ai"
```

---

## smoothStream()

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-core/smooth-stream

**Contents**:
- smoothStream()
- Import
- API Signature
  - Parameters
  - delayInMs?:
  - chunking?:
    - Word chunking caveats with non-latin languages
    - Regex based chunking

smoothStream is a utility function that creates a TransformStream for the streamText transform option to smooth out text streaming by buffering and releasing complete words with configurable delays. This creates a more natural reading experience when streaming text responses.

The word based chunking does not work well with the following languages that do not delimit words with spaces:

For these languages we recommend using a custom regex, like the following:

For these languages you could pass your own language aware chunking function:

To use regex based chunking, pass a RegExp to the chunking option.

To use a custom callback for chunking, pass a function to the chunking option.

Returns a TransformStream that:

**Examples**:

```ts
import { smoothStream, streamText } from 'ai';
const result = streamText({  model,  prompt,  experimental_transform: smoothStream({    delayInMs: 20, // optional: defaults to 10ms    chunking: 'line', // optional: defaults to 'word'  }),});
```

```ts
import { smoothStream, streamText } from 'ai';
const result = streamText({  model,  prompt,  experimental_transform: smoothStream({    delayInMs: 20, // optional: defaults to 10ms    chunking: 'line', // optional: defaults to 'word'  }),});
```

```python
import { smoothStream } from "ai"
```

---

## streamObject()

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-core/stream-object

**Contents**:
- streamObject()
    - Example: stream an object using a schema
    - Example: stream an array using a schema
    - Example: generate JSON without a schema
    - Example: generate an enum
- Import
- API Signature
  - Parameters

Streams a typed, structured object for a given prompt and schema using a language model.

It can be used to force the language model to return structured data, e.g. for information extraction, synthetic data generation, or classification tasks.

For arrays, you specify the schema of the array items. You can use elementStream to get the stream of complete array elements.

When you want to generate a specific enum value, you can set the output strategy to enum and provide the list of possible values in the enum parameter.

To see streamObject in action, check out the additional examples.

**Examples**:

```ts
import { openai } from '@ai-sdk/openai';import { streamObject } from 'ai';import { z } from 'zod';
const { partialObjectStream } = streamObject({  model: openai('gpt-4.1'),  schema: z.object({    recipe: z.object({      name: z.string(),      ingredients: z.array(z.string()),      steps: z.array(z.string()),    }),  }),  prompt: 'Generate a lasagna recipe.',});
for await (const partialObject of partialObjectStream) {  console.clear();  console.log(partialObject);}
```

```ts
import { openai } from '@ai-sdk/openai';import { streamObject } from 'ai';import { z } from 'zod';
const { partialObjectStream } = streamObject({  model: openai('gpt-4.1'),  schema: z.object({    recipe: z.object({      name: z.string(),      ingredients: z.array(z.string()),      steps: z.array(z.string()),    }),  }),  prompt: 'Generate a lasagna recipe.',});
for await (const partialObject of partialObjectStream) {  console.clear();  console.log(partialObject);}
```

```ts
import { openai } from '@ai-sdk/openai';import { streamObject } from 'ai';import { z } from 'zod';
const { elementStream } = streamObject({  model: openai('gpt-4.1'),  output: 'array',  schema: z.object({    name: z.string(),    class: z      .string()      .describe('Character class, e.g. warrior, mage, or thief.'),    description: z.string(),  }),  prompt: 'Generate 3 hero descriptions for a fantasy role playing game.',});
for await (const hero of elementStream) {  console.log(hero);}
```

---

## streamText()

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-core/stream-text

**Contents**:
- streamText()
- Import
- API Signature
  - Parameters
  - model:
  - system:
  - prompt:
  - messages:

Streams text generations from a language model.

You can use the streamText function for interactive use cases such as chat bots and other real-time applications. You can also generate UI components with tools.

To see streamText in action, check out these examples.

**Examples**:

```ts
import { openai } from '@ai-sdk/openai';import { streamText } from 'ai';
const { textStream } = streamText({  model: openai('gpt-4o'),  prompt: 'Invent a new holiday and describe its traditions.',});
for await (const textPart of textStream) {  process.stdout.write(textPart);}
```

```ts
import { openai } from '@ai-sdk/openai';import { streamText } from 'ai';
const { textStream } = streamText({  model: openai('gpt-4o'),  prompt: 'Invent a new holiday and describe its traditions.',});
for await (const textPart of textStream) {  process.stdout.write(textPart);}
```

```python
import { streamText } from "ai"
```

---

## streamUI

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-rsc/stream-ui

**Contents**:
- streamUI
- Import
- Parameters
  - model:
  - initial?:
  - system:
  - prompt:
  - messages:

AI SDK RSC is currently experimental. We recommend using AI SDK UI for production. For guidance on migrating from RSC to UI, see our migration guide.

A helper function to create a streamable UI from LLM providers. This function is similar to AI SDK Core APIs and supports the same model interfaces.

To see streamUI in action, check out these examples.

**Examples**:

```python
import { streamUI } from "@ai-sdk/rsc"
```

---

## tool()

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-core/tool

**Contents**:
- tool()
- Import
- API Signature
  - Parameters
  - tool:
  - description?:
  - inputSchema:
  - execute?:

Tool is a helper function that infers the tool input for its execute method.

It does not have any runtime behavior, but it helps TypeScript infer the types of the input for the execute method.

Without this helper function, TypeScript is unable to connect the inputSchema property to the execute method, and the argument types of execute cannot be inferred.

The tool that was passed in.

**Examples**:

```ts
import { tool } from 'ai';import { z } from 'zod';
export const weatherTool = tool({  description: 'Get the weather in a location',  inputSchema: z.object({    location: z.string().describe('The location to get the weather for'),  }),  // location below is inferred to be a string:  execute: async ({ location }) => ({    location,    temperature: 72 + Math.floor(Math.random() * 21) - 10,  }),});
```

```ts
import { tool } from 'ai';import { z } from 'zod';
export const weatherTool = tool({  description: 'Get the weather in a location',  inputSchema: z.object({    location: z.string().describe('The location to get the weather for'),  }),  // location below is inferred to be a string:  execute: async ({ location }) => ({    location,    temperature: 72 + Math.floor(Math.random() * 21) - 10,  }),});
```

```python
import { tool } from "ai"
```

---

## transcribe()

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-core/transcribe

**Contents**:
- transcribe()
- Import
- API Signature
  - Parameters
  - model:
  - audio:
  - providerOptions?:
  - maxRetries?:

Generates a transcript from an audio file.

**Examples**:

```ts
import { experimental_transcribe as transcribe } from 'ai';import { openai } from '@ai-sdk/openai';import { readFile } from 'fs/promises';
const { text: transcript } = await transcribe({  model: openai.transcription('whisper-1'),  audio: await readFile('audio.mp3'),});
console.log(transcript);
```

```ts
import { experimental_transcribe as transcribe } from 'ai';import { openai } from '@ai-sdk/openai';import { readFile } from 'fs/promises';
const { text: transcript } = await transcribe({  model: openai.transcription('whisper-1'),  audio: await readFile('audio.mp3'),});
console.log(transcript);
```

```python
import { experimental_transcribe as transcribe } from "ai"
```

---

## valibotSchema()

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-core/valibot-schema

**Contents**:
- valibotSchema()
- Example
- Import
- API Signature
  - Parameters
  - valibotSchema:
  - Returns

valibotSchema is a helper function that converts a Valibot schema into a JSON schema object that is compatible with the AI SDK. It takes a Valibot schema as input, and returns a typed schema.

You can use it to generate structured data and in tools.

A Schema object that is compatible with the AI SDK, containing both the JSON schema representation and validation functionality.

**Examples**:

```ts
import { valibotSchema } from '@ai-sdk/valibot';import { object, string, array } from 'valibot';
const recipeSchema = valibotSchema(  object({    name: string(),    ingredients: array(      object({        name: string(),        amount: string(),      }),    ),    steps: array(string()),  }),);
```

```ts
import { valibotSchema } from '@ai-sdk/valibot';import { object, string, array } from 'valibot';
const recipeSchema = valibotSchema(  object({    name: string(),    ingredients: array(      object({        name: string(),        amount: string(),      }),    ),    steps: array(string()),  }),);
```

```python
import { valibotSchema } from "ai"
```

---

## validateUIMessages

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-core/validate-ui-messages

**Contents**:
- validateUIMessages
- Basic Usage
- Advanced Usage

validateUIMessages is an async function that validates UI messages against schemas for metadata, data parts, and tools. It ensures type safety and data integrity for your message arrays before processing or rendering.

Simple validation without custom schemas:

Comprehensive validation with custom metadata, data parts, and tools:

**Examples**:

```typescript
import { validateUIMessages } from 'ai';
const messages = [  {    id: '1',    role: 'user',    parts: [{ type: 'text', text: 'Hello!' }],  },];
const validatedMessages = await validateUIMessages({  messages,});
```

```typescript
import { validateUIMessages } from 'ai';
const messages = [  {    id: '1',    role: 'user',    parts: [{ type: 'text', text: 'Hello!' }],  },];
const validatedMessages = await validateUIMessages({  messages,});
```

```typescript
import { validateUIMessages, tool } from 'ai';import { z } from 'zod';
// Define schemasconst metadataSchema = z.object({  timestamp: z.string().datetime(),  userId: z.string(),});
const dataSchemas = {  chart: z.object({    data: z.array(z.number()),    labels: z.array(z.string()),  }),  image: z.object({    url: z.string().url(),    caption: z.string(),  }),};
const tools = {  weather: tool({    description: 'Get weather info',    parameters: z.object({      location: z.string(),    }),    exe
...
```

---

## wrapLanguageModel()

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-core/wrap-language-model

**Contents**:
- wrapLanguageModel()
- Import
- API Signature
  - Parameters
  - model:
  - middleware:
  - modelId:
  - providerId:

The wrapLanguageModel function provides a way to enhance the behavior of language models by wrapping them with middleware. See Language Model Middleware for more information on middleware.

A new LanguageModelV2 instance with middleware applied.

**Examples**:

```ts
import { wrapLanguageModel } from 'ai';
const wrappedLanguageModel = wrapLanguageModel({  model: 'openai/gpt-4.1',  middleware: yourLanguageModelMiddleware,});
```

```ts
import { wrapLanguageModel } from 'ai';
const wrappedLanguageModel = wrapLanguageModel({  model: 'openai/gpt-4.1',  middleware: yourLanguageModelMiddleware,});
```

```python
import { wrapLanguageModel } from "ai"
```

---

## zodSchema()

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-core/zod-schema

**Contents**:
- zodSchema()
- Example with recursive schemas
- Import
- API Signature
  - Parameters
  - zodSchema:
  - options:
  - useReferences?:

zodSchema is a helper function that converts a Zod schema into a JSON schema object that is compatible with the AI SDK. It takes a Zod schema and optional configuration as inputs, and returns a typed schema.

You can use it to generate structured data and in tools.

You can also pass Zod objects directly to the AI SDK functions. Internally, the AI SDK will convert the Zod schema to a JSON schema using zodSchema(). However, if you want to specify options such as useReferences, you can pass the zodSchema() helper function instead.

A Schema object that is compatible with the AI SDK, containing both the JSON schema representation and validation functionality.

**Examples**:

```ts
import { zodSchema } from 'ai';import { z } from 'zod';
// Define a base category schemaconst baseCategorySchema = z.object({  name: z.string(),});
// Define the recursive Category typetype Category = z.infer<typeof baseCategorySchema> & {  subcategories: Category[];};
// Create the recursive schema using z.lazyconst categorySchema: z.ZodType<Category> = baseCategorySchema.extend({  subcategories: z.lazy(() => categorySchema.array()),});
// Create the final schema with useReferences enabled for 
...
```

```ts
import { zodSchema } from 'ai';import { z } from 'zod';
// Define a base category schemaconst baseCategorySchema = z.object({  name: z.string(),});
// Define the recursive Category typetype Category = z.infer<typeof baseCategorySchema> & {  subcategories: Category[];};
// Create the recursive schema using z.lazyconst categorySchema: z.ZodType<Category> = baseCategorySchema.extend({  subcategories: z.lazy(() => categorySchema.array()),});
// Create the final schema with useReferences enabled for 
...
```

```python
import { zodSchema } from "ai"
```

---
