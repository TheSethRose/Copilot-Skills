# Ai-Sdk - Other

**Pages**: 30

---

## AI SDK RSC

**URL**: https://ai-sdk.dev/docs/ai-sdk-rsc

**Contents**:
- AI SDK RSC

AI SDK RSC is currently experimental. We recommend using AI SDK UI for production. For guidance on migrating from RSC to UI, see our migration guide.

---

## AI SDK RSC

**URL**: https://ai-sdk.dev/docs/ai-sdk-rsc/overview

**Contents**:
- AI SDK RSC
- AI SDK RSC Functions
- Templates
- API Reference

AI SDK RSC is currently experimental. We recommend using AI SDK UI for production. For guidance on migrating from RSC to UI, see our migration guide.

The @ai-sdk/rsc package is compatible with frameworks that support React Server Components.

React Server Components (RSC) allow you to write UI that can be rendered on the server and streamed to the client. RSCs enable Server Actions , a new way to call server-side code directly from the client just like any other function with end-to-end type-safety. This combination opens the door to a new way of building AI applications, allowing the large language model (LLM) to generate and stream UI directly from the server to the client.

AI SDK RSC has various functions designed to help you build AI-native applications with React Server Components. These functions:

Check out the following templates to see AI SDK RSC in action.

Please check out the AI SDK RSC API Reference for more details on each function.

---

## AI SDK UI

**URL**: https://ai-sdk.dev/docs/ai-sdk-ui/overview

**Contents**:
- AI SDK UI
- UI Framework Support
- Framework Examples
- API Reference

AI SDK UI is designed to help you build interactive chat, completion, and assistant applications with ease. It is a framework-agnostic toolkit, streamlining the integration of advanced AI functionalities into your applications.

AI SDK UI provides robust abstractions that simplify the complex tasks of managing chat streams and UI updates on the frontend, enabling you to develop dynamic AI-driven interfaces more efficiently. With three main hooks — useChat, useCompletion, and useObject — you can incorporate real-time chat capabilities, text completions, streamed JSON, and interactive assistant features into your app.

These hooks are designed to reduce the complexity and time required to implement AI interactions, letting you focus on creating exceptional user experiences.

AI SDK UI supports the following frameworks: React, Svelte, Vue.js, and Angular. Here is a comparison of the supported functions across these frameworks:

Contributions are welcome to implement missing features for non-React frameworks.

Explore these example implementations for different frameworks:

Please check out the AI SDK UI API Reference for more details on each function.

---

## AI SDK UI

**URL**: https://ai-sdk.dev/docs/ai-sdk-ui

**Contents**:
- AI SDK UI

---

## Agents

**URL**: https://ai-sdk.dev/docs/agents

**Contents**:
- Agents

The following section show you how to build agents with the AI SDK - systems where large language models (LLMs) use tools in a loop to accomplish tasks.

---

## Agents

**URL**: https://ai-sdk.dev/docs/foundations/agents

**Contents**:
- Agents
- Agent Class
- Why Use the Agent Class?
- Structured Workflows
- Next Steps

Agents are large language models (LLMs) that use tools in a loop to accomplish tasks.

These components work together:

The Agent class handles these three components. Here's an agent that uses multiple tools in a loop to accomplish a task:

The agent automatically:

The Agent class handles the loop, context management, and stopping conditions.

The Agent class is the recommended approach for building agents with the AI SDK because it:

For most use cases, start with the Agent class. Use core functions (generateText, streamText) when you need explicit control over each step for complex structured workflows.

Agents are flexible and powerful, but non-deterministic. When you need reliable, repeatable outcomes with explicit control flow, use core functions with structured workflow patterns combining:

Explore workflow patterns to learn more about building structured, reliable systems.

**Examples**:

```ts
import { Experimental_Agent as Agent, stepCountIs, tool } from 'ai';import { z } from 'zod';
const weatherAgent = new Agent({  model: 'openai/gpt-4o',  tools: {    weather: tool({      description: 'Get the weather in a location (in Fahrenheit)',      inputSchema: z.object({        location: z.string().describe('The location to get the weather for'),      }),      execute: async ({ location }) => ({        location,        temperature: 72 + Math.floor(Math.random() * 21) - 10,      }),    }),   
...
```

```ts
import { Experimental_Agent as Agent, stepCountIs, tool } from 'ai';import { z } from 'zod';
const weatherAgent = new Agent({  model: 'openai/gpt-4o',  tools: {    weather: tool({      description: 'Get the weather in a location (in Fahrenheit)',      inputSchema: z.object({        location: z.string().describe('The location to get the weather for'),      }),      execute: async ({ location }) => ({        location,        temperature: 72 + Math.floor(Math.random() * 21) - 10,      }),    }),   
...
```

---

## Agents

**URL**: https://ai-sdk.dev/docs/agents/overview

**Contents**:
- Agents
- Agent Class
- Why Use the Agent Class?
- Structured Workflows
- Next Steps

Agents are large language models (LLMs) that use tools in a loop to accomplish tasks.

These components work together:

The Agent class handles these three components. Here's an agent that uses multiple tools in a loop to accomplish a task:

The agent automatically:

The Agent class handles the loop, context management, and stopping conditions.

The Agent class is the recommended approach for building agents with the AI SDK because it:

For most use cases, start with the Agent class. Use core functions (generateText, streamText) when you need explicit control over each step for complex structured workflows.

Agents are flexible and powerful, but non-deterministic. When you need reliable, repeatable outcomes with explicit control flow, use core functions with structured workflow patterns combining:

Explore workflow patterns to learn more about building structured, reliable systems.

**Examples**:

```ts
import { Experimental_Agent as Agent, stepCountIs, tool } from 'ai';import { z } from 'zod';
const weatherAgent = new Agent({  model: 'openai/gpt-4o',  tools: {    weather: tool({      description: 'Get the weather in a location (in Fahrenheit)',      inputSchema: z.object({        location: z.string().describe('The location to get the weather for'),      }),      execute: async ({ location }) => ({        location,        temperature: 72 + Math.floor(Math.random() * 21) - 10,      }),    }),   
...
```

```ts
import { Experimental_Agent as Agent, stepCountIs, tool } from 'ai';import { z } from 'zod';
const weatherAgent = new Agent({  model: 'openai/gpt-4o',  tools: {    weather: tool({      description: 'Get the weather in a location (in Fahrenheit)',      inputSchema: z.object({        location: z.string().describe('The location to get the weather for'),      }),      execute: async ({ location }) => ({        location,        temperature: 72 + Math.floor(Math.random() * 21) - 10,      }),    }),   
...
```

---

## Authentication

**URL**: https://ai-sdk.dev/docs/ai-sdk-rsc/authentication

**Contents**:
- Authentication

AI SDK RSC is currently experimental. We recommend using AI SDK UI for production. For guidance on migrating from RSC to UI, see our migration guide.

The RSC API makes extensive use of Server Actions to power streaming values and UI from the server.

Server Actions are exposed as public, unprotected endpoints. As a result, you should treat Server Actions as you would public-facing API endpoints and ensure that the user is authorized to perform the action before returning any data.

**Examples**:

```tsx
'use server';
import { cookies } from 'next/headers';import { createStremableUI } from '@ai-sdk/rsc';import { validateToken } from '../utils/auth';
export const getWeather = async () => {  const token = cookies().get('token');
  if (!token || !validateToken(token)) {    return {      error: 'This action requires authentication',    };  }  const streamableDisplay = createStreamableUI(null);
  streamableDisplay.update(<Skeleton />);  streamableDisplay.done(<Weather />);
  return {    display: stre
...
```

```tsx
'use server';
import { cookies } from 'next/headers';import { createStremableUI } from '@ai-sdk/rsc';import { validateToken } from '../utils/auth';
export const getWeather = async () => {  const token = cookies().get('token');
  if (!token || !validateToken(token)) {    return {      error: 'This action requires authentication',    };  }  const streamableDisplay = createStreamableUI(null);
  streamableDisplay.update(<Skeleton />);  streamableDisplay.done(<Weather />);
  return {    display: stre
...
```

---

## Building Agents

**URL**: https://ai-sdk.dev/docs/agents/building-agents

**Contents**:
- Building Agents
- Why Use the Agent Class?
- Creating an Agent
- Configuration Options
  - Model and System Prompt
  - Tools
  - Loop Control
  - Tool Choice

The Agent class provides a structured way to encapsulate LLM configuration, tools, and behavior into reusable components. It handles the agent loop for you, allowing the LLM to call tools multiple times in sequence to accomplish complex tasks. Define agents once and use them across your application.

When building AI applications, you often need to:

The Agent class provides a single place to define your agent's behavior.

Define an agent by instantiating the Agent class with your desired configuration:

The Agent class accepts all the same settings as generateText and streamText. Configure:

Provide tools that the agent can use to accomplish tasks:

By default, agents run for a single step (stopWhen: stepCountIs(1)). In each step, the model either generates text or calls a tool. If it generates text, the agent completes. If it calls a tool, the AI SDK executes that tool.

To let agents call multiple tools in sequence, configure stopWhen to allow more steps. After each tool execution, the agent triggers a new generation where the model can call another tool or generate text:

Each step represents one generation (which results in either text or a tool call). The loop continues until:

You can combine multiple conditions:

Learn more about loop control and stop conditions.

Control how the agent uses tools:

You can also force the use of a specific tool:

Define structured output schemas:

System prompts define your agent's behavior, personality, and constraints. They set the context for all interactions and guide how the agent responds to user queries and uses tools.

Set the agent's role and expertise:

Provide specific guidelines for agent behavior:

Set boundaries and ensure consistent behavior:

Guide how the agent should use available tools:

Control the output format and communication style:

Once defined, you can use your agent in three ways:

Use generate() for one-time text generation:

Use stream() for streaming responses:

Use respond() to create API respo

*[Content truncated - see full docs]*

**Examples**:

```ts
import { Experimental_Agent as Agent } from 'ai';
const myAgent = new Agent({  model: 'openai/gpt-4o',  system: 'You are a helpful assistant.',  tools: {    // Your tools here  },});
```

```ts
import { Experimental_Agent as Agent } from 'ai';
const myAgent = new Agent({  model: 'openai/gpt-4o',  system: 'You are a helpful assistant.',  tools: {    // Your tools here  },});
```

```ts
import { Experimental_Agent as Agent } from 'ai';
const agent = new Agent({  model: 'openai/gpt-4o',  system: 'You are an expert software engineer.',});
```

---

## Chatbot

**URL**: https://ai-sdk.dev/docs/ai-sdk-ui/chatbot

**Contents**:
- Chatbot
- Example
- Customized UI
  - Status
  - Error State
  - Modify messages
  - Cancellation and regeneration
  - Throttling UI Updates

The useChat hook makes it effortless to create a conversational user interface for your chatbot application. It enables the streaming of chat messages from your AI provider, manages the chat state, and updates the UI automatically as new messages arrive.

To summarize, the useChat hook provides the following features:

In this guide, you will learn how to use the useChat hook to create a chatbot application with real-time message streaming. Check out our chatbot with tools guide to learn how to use tools in your chatbot. Let's start with the following example first.

The UI messages have a new parts property that contains the message parts. We recommend rendering the messages using the parts property instead of the content property. The parts property supports different message types, including text, tool invocation, and tool result, and allows for more flexible and complex chat UIs.

In the Page component, the useChat hook will request to your AI provider endpoint whenever the user sends a message using sendMessage. The messages are then streamed back in real-time and displayed in the chat UI.

This enables a seamless chat experience where the user can see the AI response as soon as it is available, without having to wait for the entire response to be received.

useChat also provides ways to manage the chat message states via code, show status, and update messages without being triggered by user interactions.

The useChat hook returns a status. It has the following possible values:

You can use status for e.g. the following purposes:

Similarly, the error state reflects the error object thrown during the fetch request. It can be used to display an error message, disable the submit button, or show a retry button:

We recommend showing a generic error message to the user, such as "Something went wrong." This is a good practice to avoid leaking information from the server.

Please also see the error handling guide for more information.

Sometimes, you may want to dire

*[Content truncated - see full docs]*

**Examples**:

```tsx
'use client';
import { useChat } from '@ai-sdk/react';import { DefaultChatTransport } from 'ai';import { useState } from 'react';
export default function Page() {  const { messages, sendMessage, status } = useChat({    transport: new DefaultChatTransport({      api: '/api/chat',    }),  });  const [input, setInput] = useState('');
  return (    <>      {messages.map(message => (        <div key={message.id}>          {message.role === 'user' ? 'User: ' : 'AI: '}          {message.parts.map((part
...
```

```tsx
'use client';
import { useChat } from '@ai-sdk/react';import { DefaultChatTransport } from 'ai';import { useState } from 'react';
export default function Page() {  const { messages, sendMessage, status } = useChat({    transport: new DefaultChatTransport({      api: '/api/chat',    }),  });  const [input, setInput] = useState('');
  return (    <>      {messages.map(message => (        <div key={message.id}>          {message.role === 'user' ? 'User: ' : 'AI: '}          {message.parts.map((part
...
```

```ts
import { openai } from '@ai-sdk/openai';import { convertToModelMessages, streamText, UIMessage } from 'ai';
// Allow streaming responses up to 30 secondsexport const maxDuration = 30;
export async function POST(req: Request) {  const { messages }: { messages: UIMessage[] } = await req.json();
  const result = streamText({    model: openai('gpt-4.1'),    system: 'You are a helpful assistant.',    messages: convertToModelMessages(messages),  });
  return result.toUIMessageStreamResponse();}
```

---

## Chatbot Message Persistence

**URL**: https://ai-sdk.dev/docs/ai-sdk-ui/chatbot-message-persistence

**Contents**:
- Chatbot Message Persistence
- Starting a new chat
- Loading an existing chat
- Validating messages on the server
  - Validation with tools
  - Handling validation errors
- Displaying the chat
- Storing messages

Being able to store and load chat messages is crucial for most AI chatbots. In this guide, we'll show how to implement message persistence with useChat and streamText.

This guide does not cover authorization, error handling, or other real-world considerations. It is intended to be a simple example of how to implement message persistence.

When the user navigates to the chat page without providing a chat ID, we need to create a new chat and redirect to the chat page with the new chat ID.

Our example chat store implementation uses files to store the chat messages. In a real-world application, you would use a database or a cloud storage service, and get the chat ID from the database. That being said, the function interfaces are designed to be easily replaced with other implementations.

When the user navigates to the chat page with a chat ID, we need to load the chat messages from storage.

The loadChat function in our file-based chat store is implemented as follows:

When processing messages on the server that contain tool calls, custom metadata, or data parts, you should validate them using validateUIMessages before sending them to the model.

When your messages include tool calls, validate them against your tool definitions:

Handle validation errors gracefully when messages from the database don't match current schemas:

Once messages are loaded from storage, you can display them in your chat UI. Here's how to set up the page component and the chat display:

The chat component uses the useChat hook to manage the conversation:

useChat sends the chat id and the messages to the backend.

The useChat message format is different from the ModelMessage format. The useChat message format is designed for frontend display, and contains additional fields such as id and createdAt. We recommend storing the messages in the useChat message format.

When loading messages from storage that contain tools, metadata, or custom data parts, validate them using validateUIMessages befo

*[Content truncated - see full docs]*

**Examples**:

```tsx
import { redirect } from 'next/navigation';import { createChat } from '@util/chat-store';
export default async function Page() {  const id = await createChat(); // create a new chat  redirect(`/chat/${id}`); // redirect to chat page, see below}
```

```tsx
import { redirect } from 'next/navigation';import { createChat } from '@util/chat-store';
export default async function Page() {  const id = await createChat(); // create a new chat  redirect(`/chat/${id}`); // redirect to chat page, see below}
```

```tsx
import { generateId } from 'ai';import { existsSync, mkdirSync } from 'fs';import { writeFile } from 'fs/promises';import path from 'path';
export async function createChat(): Promise<string> {  const id = generateId(); // generate a unique chat ID  await writeFile(getChatFile(id), '[]'); // create an empty chat file  return id;}
function getChatFile(id: string): string {  const chatDir = path.join(process.cwd(), '.chats');  if (!existsSync(chatDir)) mkdirSync(chatDir, { recursive: true });  ret
...
```

---

## Chatbot Tool Usage

**URL**: https://ai-sdk.dev/docs/ai-sdk-ui/chatbot-with-tool-calling

**Contents**:
- Chatbot Tool Usage
- Example
  - API route
  - Client-side page
  - Error handling
- Dynamic Tools
- Tool call streaming
- Step start parts

With useChat and streamText, you can use tools in your chatbot application. The AI SDK supports three types of tools in this context:

The flow is as follows:

The tool calls and tool executions are integrated into the assistant message as typed tool parts. A tool part is at first a tool call, and then it becomes a tool result when the tool is executed. The tool result contains all information about the tool call as well as the result of the tool execution.

Tool result submission can be configured using the sendAutomaticallyWhen option. You can use the lastAssistantMessageIsCompleteWithToolCalls helper to automatically submit when all tool results are available. This simplifies the client-side code while still allowing full control when needed.

In this example, we'll use three tools:

The client-side page uses the useChat hook to create a chatbot application with real-time message streaming. Tool calls are displayed in the chat UI as typed tool parts. Please make sure to render the messages using the parts property of the message.

There are three things worth mentioning:

The onToolCall callback is used to handle client-side tools that should be automatically executed. In this example, the getLocation tool is a client-side tool that returns a random city. You call addToolResult to provide the result (without await to avoid potential deadlocks).

Always check if (toolCall.dynamic) first in your onToolCall handler. Without this check, TypeScript will throw an error like: Type 'string' is not assignable to type '"toolName1" | "toolName2"' when you try to use toolCall.toolName in addToolResult.

The sendAutomaticallyWhen option with lastAssistantMessageIsCompleteWithToolCalls helper automatically submits when all tool results are available.

The parts array of assistant messages contains tool parts with typed names like tool-askForConfirmation. The client-side tool askForConfirmation is displayed in the UI. It asks the user for confirmation and displays the result on

*[Content truncated - see full docs]*

**Examples**:

```tsx
import { openai } from '@ai-sdk/openai';import { convertToModelMessages, streamText, UIMessage } from 'ai';import { z } from 'zod';
// Allow streaming responses up to 30 secondsexport const maxDuration = 30;
export async function POST(req: Request) {  const { messages }: { messages: UIMessage[] } = await req.json();
  const result = streamText({    model: openai('gpt-4o'),    messages: convertToModelMessages(messages),    tools: {      // server-side tool with execute function:      getWeatherIn
...
```

```tsx
import { openai } from '@ai-sdk/openai';import { convertToModelMessages, streamText, UIMessage } from 'ai';import { z } from 'zod';
// Allow streaming responses up to 30 secondsexport const maxDuration = 30;
export async function POST(req: Request) {  const { messages }: { messages: UIMessage[] } = await req.json();
  const result = streamText({    model: openai('gpt-4o'),    messages: convertToModelMessages(messages),    tools: {      // server-side tool with execute function:      getWeatherIn
...
```

```tsx
'use client';
import { useChat } from '@ai-sdk/react';import {  DefaultChatTransport,  lastAssistantMessageIsCompleteWithToolCalls,} from 'ai';import { useState } from 'react';
export default function Chat() {  const { messages, sendMessage, addToolResult } = useChat({    transport: new DefaultChatTransport({      api: '/api/chat',    }),
    sendAutomaticallyWhen: lastAssistantMessageIsCompleteWithToolCalls,
    // run client-side tools that are automatically executed:    async onToolCall({ too
...
```

---

## Chatbot Tool Usage

**URL**: https://ai-sdk.dev/docs/ai-sdk-ui/chatbot-tool-usage

**Contents**:
- Chatbot Tool Usage
- Example
  - API route
  - Client-side page
  - Error handling
- Dynamic Tools
- Tool call streaming
- Step start parts

With useChat and streamText, you can use tools in your chatbot application. The AI SDK supports three types of tools in this context:

The flow is as follows:

The tool calls and tool executions are integrated into the assistant message as typed tool parts. A tool part is at first a tool call, and then it becomes a tool result when the tool is executed. The tool result contains all information about the tool call as well as the result of the tool execution.

Tool result submission can be configured using the sendAutomaticallyWhen option. You can use the lastAssistantMessageIsCompleteWithToolCalls helper to automatically submit when all tool results are available. This simplifies the client-side code while still allowing full control when needed.

In this example, we'll use three tools:

The client-side page uses the useChat hook to create a chatbot application with real-time message streaming. Tool calls are displayed in the chat UI as typed tool parts. Please make sure to render the messages using the parts property of the message.

There are three things worth mentioning:

The onToolCall callback is used to handle client-side tools that should be automatically executed. In this example, the getLocation tool is a client-side tool that returns a random city. You call addToolResult to provide the result (without await to avoid potential deadlocks).

Always check if (toolCall.dynamic) first in your onToolCall handler. Without this check, TypeScript will throw an error like: Type 'string' is not assignable to type '"toolName1" | "toolName2"' when you try to use toolCall.toolName in addToolResult.

The sendAutomaticallyWhen option with lastAssistantMessageIsCompleteWithToolCalls helper automatically submits when all tool results are available.

The parts array of assistant messages contains tool parts with typed names like tool-askForConfirmation. The client-side tool askForConfirmation is displayed in the UI. It asks the user for confirmation and displays the result on

*[Content truncated - see full docs]*

**Examples**:

```tsx
import { openai } from '@ai-sdk/openai';import { convertToModelMessages, streamText, UIMessage } from 'ai';import { z } from 'zod';
// Allow streaming responses up to 30 secondsexport const maxDuration = 30;
export async function POST(req: Request) {  const { messages }: { messages: UIMessage[] } = await req.json();
  const result = streamText({    model: openai('gpt-4o'),    messages: convertToModelMessages(messages),    tools: {      // server-side tool with execute function:      getWeatherIn
...
```

```tsx
import { openai } from '@ai-sdk/openai';import { convertToModelMessages, streamText, UIMessage } from 'ai';import { z } from 'zod';
// Allow streaming responses up to 30 secondsexport const maxDuration = 30;
export async function POST(req: Request) {  const { messages }: { messages: UIMessage[] } = await req.json();
  const result = streamText({    model: openai('gpt-4o'),    messages: convertToModelMessages(messages),    tools: {      // server-side tool with execute function:      getWeatherIn
...
```

```tsx
'use client';
import { useChat } from '@ai-sdk/react';import {  DefaultChatTransport,  lastAssistantMessageIsCompleteWithToolCalls,} from 'ai';import { useState } from 'react';
export default function Chat() {  const { messages, sendMessage, addToolResult } = useChat({    transport: new DefaultChatTransport({      api: '/api/chat',    }),
    sendAutomaticallyWhen: lastAssistantMessageIsCompleteWithToolCalls,
    // run client-side tools that are automatically executed:    async onToolCall({ too
...
```

---

## Designing Multistep Interfaces

**URL**: https://ai-sdk.dev/docs/ai-sdk-rsc/multistep-interfaces

**Contents**:
- Designing Multistep Interfaces
- Overview
- Implementation

AI SDK RSC is currently experimental. We recommend using AI SDK UI for production. For guidance on migrating from RSC to UI, see our migration guide.

Multistep interfaces refer to user interfaces that require multiple independent steps to be executed in order to complete a specific task.

For example, if you wanted to build a Generative UI chatbot capable of booking flights, it could have three steps:

To build this kind of application you will leverage two concepts, tool composition and application context.

Tool composition is the process of combining multiple tools to create a new tool. This is a powerful concept that allows you to break down complex tasks into smaller, more manageable steps. In the example above, "search all flights", "pick flight", and "check availability" come together to create a holistic "book flight" tool.

Application context refers to the state of the application at any given point in time. This includes the user's input, the output of the language model, and any other relevant information. In the example above, the flight selected in "pick flight" would be used as context necessary to complete the "check availability" task.

In order to build a multistep interface with @ai-sdk/rsc, you will need a few things:

The general flow that you will follow is:

The turn-by-turn implementation is the simplest form of multistep interfaces. In this implementation, the user and the model take turns during the conversation. For every user input, the model generates a response, and the conversation continues in this turn-by-turn fashion.

In the following example, you specify two tools (searchFlights and lookupFlight) that the model can use to search for flights and lookup details for a specific flight.

Next, create an AI context that will hold the UI State and AI State.

Next, wrap your application with your newly created context.

To call your Server Action, update your root page with the following:

This page pulls in the current UI State using th

*[Content truncated - see full docs]*

**Examples**:

```tsx
import { streamUI } from '@ai-sdk/rsc';import { openai } from '@ai-sdk/openai';import { z } from 'zod';
const searchFlights = async (  source: string,  destination: string,  date: string,) => {  return [    {      id: '1',      flightNumber: 'AA123',    },    {      id: '2',      flightNumber: 'AA456',    },  ];};
const lookupFlight = async (flightNumber: string) => {  return {    flightNumber: flightNumber,    departureTime: '10:00 AM',    arrivalTime: '12:00 PM',  };};
export async function su
...
```

```tsx
import { streamUI } from '@ai-sdk/rsc';import { openai } from '@ai-sdk/openai';import { z } from 'zod';
const searchFlights = async (  source: string,  destination: string,  date: string,) => {  return [    {      id: '1',      flightNumber: 'AA123',    },    {      id: '2',      flightNumber: 'AA456',    },  ];};
const lookupFlight = async (flightNumber: string) => {  return {    flightNumber: flightNumber,    departureTime: '10:00 AM',    arrivalTime: '12:00 PM',  };};
export async function su
...
```

```ts
import { createAI } from '@ai-sdk/rsc';import { submitUserMessage } from './actions';
export const AI = createAI<any[], React.ReactNode[]>({  initialUIState: [],  initialAIState: [],  actions: {    submitUserMessage,  },});
```

---

## Error Handling

**URL**: https://ai-sdk.dev/docs/ai-sdk-rsc/error-handling

**Contents**:
- Error Handling
- Handling UI Errors
- Handling Other Errors

AI SDK RSC is currently experimental. We recommend using AI SDK UI for production. For guidance on migrating from RSC to UI, see our migration guide.

Two categories of errors can occur when working with the RSC API: errors while streaming user interfaces and errors while streaming other values.

To handle errors while generating UI, the streamableUI object exposes an error() method.

With this method, you can catch any error with the stream, and return relevant UI. On the client, you can also use a React Error Boundary to wrap the streamed component and catch any additional errors.

To handle other errors while streaming, you can return an error object that the receiver can use to determine why the failure occurred.

**Examples**:

```tsx
'use server';
import { createStreamableUI } from '@ai-sdk/rsc';
export async function getStreamedUI() {  const ui = createStreamableUI();
  (async () => {    ui.update(<div>loading</div>);    const data = await fetchData();    ui.done(<div>{data}</div>);  })().catch(e => {    ui.error(<div>Error: {e.message}</div>);  });
  return ui.value;}
```

```tsx
'use server';
import { createStreamableUI } from '@ai-sdk/rsc';
export async function getStreamedUI() {  const ui = createStreamableUI();
  (async () => {    ui.update(<div>loading</div>);    const data = await fetchData();    ui.done(<div>{data}</div>);  })().catch(e => {    ui.error(<div>Error: {e.message}</div>);  });
  return ui.value;}
```

```tsx
import { getStreamedUI } from '@/actions';import { useState } from 'react';import { ErrorBoundary } from './ErrorBoundary';
export default function Page() {  const [streamedUI, setStreamedUI] = useState(null);
  return (    <div>      <button        onClick={async () => {          const newUI = await getStreamedUI();          setStreamedUI(newUI);        }}      >        What does the new UI look like?      </button>      <ErrorBoundary>{streamedUI}</ErrorBoundary>    </div>  );}
```

---

## Error Handling and warnings

**URL**: https://ai-sdk.dev/docs/ai-sdk-ui/error-handling

**Contents**:
- Error Handling and warnings
- Warnings
  - When Warnings Appear
  - Warning Messages
  - Turning Off Warnings
    - Turn Off All Warnings
    - Custom Warning Handler
- Error Handling

The AI SDK shows warnings when something might not work as expected. These warnings help you fix problems before they cause errors.

Warnings are shown in the browser console when:

All warnings start with "AI SDK Warning:" so you can easily find them. For example:

By default, warnings are shown in the console. You can control this behavior:

Set a global variable to turn off warnings completely:

You can also provide your own function to handle warnings:

Custom warning functions are experimental and can change in patch releases without notice.

Each AI SDK UI hook also returns an error object that you can use to render the error in your UI. You can use the error object to show an error message, disable the submit button, or show a retry button.

We recommend showing a generic error message to the user, such as "Something went wrong." This is a good practice to avoid leaking information from the server.

Alternatively you can write a custom submit handler that replaces the last message when an error is present.

Errors can be processed by passing an onError callback function as an option to the useChat or useCompletion hooks. The callback function receives an error object as an argument.

You might want to create errors for testing. You can easily do so by throwing an error in your route handler:

**Examples**:

```undefined
AI SDK Warning: The "temperature" setting is not supported by this modelAI SDK Warning: The tool "calculator" is not supported by this model
```

```undefined
AI SDK Warning: The "temperature" setting is not supported by this modelAI SDK Warning: The tool "calculator" is not supported by this model
```

```ts
globalThis.AI_SDK_LOG_WARNINGS = false;
```

---

## Foundations

**URL**: https://ai-sdk.dev/docs/foundations

**Contents**:
- Foundations

---

## Getting Started

**URL**: https://ai-sdk.dev/docs/getting-started

**Contents**:
- Getting Started
- Backend Framework Examples

The following guides are intended to provide you with an introduction to some of the core features provided by the AI SDK.

You can also use AI SDK Core and AI SDK UI with the following backend frameworks:

---

## Loop Control

**URL**: https://ai-sdk.dev/docs/agents/loop-control

**Contents**:
- Loop Control
- Stop Conditions
  - Use Built-in Conditions
  - Combine Multiple Conditions
  - Create Custom Conditions
- Prepare Step
  - Dynamic Model Selection
  - Context Management

You can control both the execution flow and the settings at each step of the agent loop. The AI SDK provides built-in loop control through two parameters: stopWhen for defining stopping conditions and prepareStep for modifying settings (model, tools, messages, and more) between steps.

The stopWhen parameter controls when to stop execution when there are tool results in the last step. By default, agents stop after a single step using stepCountIs(1).

When you provide stopWhen, the agent continues executing after tool calls until a stopping condition is met. When the condition is an array, execution stops when any of the conditions are met.

The AI SDK provides several built-in stopping conditions:

Combine multiple stopping conditions. The loop stops when it meets any condition:

Build custom stopping conditions for specific requirements:

Custom conditions receive step information across all steps:

The prepareStep callback runs before each step in the loop and defaults to the initial settings if you don't return any changes. Use it to modify settings, manage context, or implement dynamic behavior based on execution history.

Switch models based on step requirements:

Manage growing conversation history in long-running loops:

Control which tools are available at each step:

You can also force a specific tool to be used:

Transform messages before sending them to the model:

Both stopWhen and prepareStep receive detailed information about the current execution:

For scenarios requiring complete control over the agent loop, you can use AI SDK Core functions (generateText and streamText) to implement your own loop management instead of using stopWhen and prepareStep. This approach provides maximum flexibility for complex workflows.

Build your own agent loop when you need full control over execution:

This manual approach gives you complete control over:

Learn more about manual agent loops in the cookbook.

**Examples**:

```ts
import { Experimental_Agent as Agent, stepCountIs } from 'ai';
const agent = new Agent({  model: 'openai/gpt-4o',  tools: {    // your tools  },  stopWhen: stepCountIs(20), // Stop after 20 steps maximum});
const result = await agent.generate({  prompt: 'Analyze this dataset and create a summary report',});
```

```ts
import { Experimental_Agent as Agent, stepCountIs } from 'ai';
const agent = new Agent({  model: 'openai/gpt-4o',  tools: {    // your tools  },  stopWhen: stepCountIs(20), // Stop after 20 steps maximum});
const result = await agent.generate({  prompt: 'Analyze this dataset and create a summary report',});
```

```ts
import { Experimental_Agent as Agent, stepCountIs, hasToolCall } from 'ai';
const agent = new Agent({  model: 'openai/gpt-4o',  tools: {    // your tools  },  stopWhen: [    stepCountIs(20), // Maximum 20 steps    hasToolCall('someTool'), // Stop after calling 'someTool'  ],});
const result = await agent.generate({  prompt: 'Research and analyze the topic',});
```

---

## Managing Generative UI State

**URL**: https://ai-sdk.dev/docs/ai-sdk-rsc/generative-ui-state

**Contents**:
- Managing Generative UI State
- What is AI and UI State?
  - AI State
  - UI State
- Using AI / UI State
  - Creating the AI Context
- Reading UI State in Client
- Reading AI State in Client

AI SDK RSC is currently experimental. We recommend using AI SDK UI for production. For guidance on migrating from RSC to UI, see our migration guide.

State is an essential part of any application. State is particularly important in AI applications as it is passed to large language models (LLMs) on each request to ensure they have the necessary context to produce a great generation. Traditional chatbots are text-based and have a structure that mirrors that of any chat application.

For example, in a chatbot, state is an array of messages where each message has:

This state can be rendered in the UI and sent to the model without any modifications.

With Generative UI, the model can now return a React component, rather than a plain text message. The client can render that component without issue, but that state can't be sent back to the model because React components aren't serialisable. So, what can you do?

The solution is to split the state in two, where one (AI State) becomes a proxy for the other (UI State).

One way to understand this concept is through a Lego analogy. Imagine a 10,000 piece Lego model that, once built, cannot be easily transported because it is fragile. By taking the model apart, it can be easily transported, and then rebuilt following the steps outlined in the instructions pamphlet. In this way, the instructions pamphlet is a proxy to the physical structure. Similarly, AI State provides a serialisable (JSON) representation of your UI that can be passed back and forth to the model.

The RSC API simplifies how you manage AI State and UI State, providing a robust way to keep them in sync between your database, server and client.

AI State refers to the state of your application in a serialisable format that will be used on the server and can be shared with the language model.

For a chat app, the AI State is the conversation history (messages) between the user and the assistant. Components generated by the model would be represented in a JSON for

*[Content truncated - see full docs]*

**Examples**:

```tsx
// Define the AI state and UI state typesexport type ServerMessage = {  role: 'user' | 'assistant';  content: string;};
export type ClientMessage = {  id: string;  role: 'user' | 'assistant';  display: ReactNode;};
export const sendMessage = async (input: string): Promise<ClientMessage> => {  "use server"  ...}
```

```tsx
// Define the AI state and UI state typesexport type ServerMessage = {  role: 'user' | 'assistant';  content: string;};
export type ClientMessage = {  id: string;  role: 'user' | 'assistant';  display: ReactNode;};
export const sendMessage = async (input: string): Promise<ClientMessage> => {  "use server"  ...}
```

```tsx
import { createAI } from '@ai-sdk/rsc';import { ClientMessage, ServerMessage, sendMessage } from './actions';
export type AIState = ServerMessage[];export type UIState = ClientMessage[];
// Create the AI provider with the initial states and allowed actionsexport const AI = createAI<AIState, UIState>({  initialAIState: [],  initialUIState: [],  actions: {    sendMessage,  },});
```

---

## Message Metadata

**URL**: https://ai-sdk.dev/docs/ai-sdk-ui/message-metadata

**Contents**:
- Message Metadata
- Overview
- Getting Started
  - Defining Metadata Types
  - Sending Metadata from the Server
  - Accessing Metadata on the Client
- Common Use Cases
- See Also

Message metadata allows you to attach custom information to messages at the message level. This is useful for tracking timestamps, model information, token usage, user context, and other message-level data.

Message metadata differs from data parts in that it's attached at the message level rather than being part of the message content. While data parts are ideal for dynamic content that forms part of the message, metadata is perfect for information about the message itself.

Here's a simple example of using message metadata to track timestamps and model information:

First, define your metadata type for type safety:

Use the messageMetadata callback in toUIMessageStreamResponse to send metadata at different streaming stages:

To enable type-safe metadata return object in messageMetadata, pass in the originalMessages parameter typed to your UIMessage type.

Access metadata through the message.metadata property:

For streaming arbitrary data that changes during generation, consider using data parts instead.

Message metadata is ideal for:

**Examples**:

```tsx
import { UIMessage } from 'ai';import { z } from 'zod';
// Define your metadata schemaexport const messageMetadataSchema = z.object({  createdAt: z.number().optional(),  model: z.string().optional(),  totalTokens: z.number().optional(),});
export type MessageMetadata = z.infer<typeof messageMetadataSchema>;
// Create a typed UIMessageexport type MyUIMessage = UIMessage<MessageMetadata>;
```

```tsx
import { UIMessage } from 'ai';import { z } from 'zod';
// Define your metadata schemaexport const messageMetadataSchema = z.object({  createdAt: z.number().optional(),  model: z.string().optional(),  totalTokens: z.number().optional(),});
export type MessageMetadata = z.infer<typeof messageMetadataSchema>;
// Create a typed UIMessageexport type MyUIMessage = UIMessage<MessageMetadata>;
```

```ts
import { openai } from '@ai-sdk/openai';import { convertToModelMessages, streamText } from 'ai';import type { MyUIMessage } from '@/types';
export async function POST(req: Request) {  const { messages }: { messages: MyUIMessage[] } = await req.json();
  const result = streamText({    model: openai('gpt-4o'),    messages: convertToModelMessages(messages),  });
  return result.toUIMessageStreamResponse({    originalMessages: messages, // pass this in for type-safe return objects    messageMetadata
...
```

---

## Migrating from RSC to UI

**URL**: https://ai-sdk.dev/docs/ai-sdk-rsc/migrating-to-ui

**Contents**:
- Migrating from RSC to UI
- Background
- Streaming Chat Completions
  - Basic Setup
    - Before: Handle generation and rendering in a single server action
    - Before: Call server action and update UI state
    - After: Replace server action with route handler
    - After: Update client to use chat hook

This guide helps you migrate from AI SDK RSC to AI SDK UI.

The AI SDK has two packages that help you build the frontend for your applications – AI SDK UI and AI SDK RSC.

We introduced support for using React Server Components (RSC) within the AI SDK to simplify building generative user interfaces for frameworks that support RSC.

However, given we're pushing the boundaries of this technology, AI SDK RSC currently faces significant limitations that make it unsuitable for stable production use.

Due to these limitations, AI SDK RSC is marked as experimental, and we do not recommend using it for stable production environments.

As a result, we strongly recommend migrating to AI SDK UI, which has undergone extensive development to provide a more stable and production grade experience.

In building v0, we have invested considerable time exploring how to create the best chat experience on the web. AI SDK UI ships with many of these best practices and commonly used patterns like language model middleware, multi-step tool calls, attachments, telemetry, provider registry, and many more. These features have been considerately designed into a neat abstraction that you can use to reliably integrate AI into your applications.

The streamUI function executes as part of a server action as illustrated below.

The chat interface calls the server action. The response is then saved using the useUIState hook.

The streamUI function combines generating text and rendering the user interface. To migrate to AI SDK UI, you need to separate these concerns – streaming generations with streamText and rendering the UI with useChat.

The streamText function executes as part of a route handler and streams the response to the client. The useChat hook on the client decodes this stream and renders the response within the chat interface.

In AI SDK RSC, streamUI does not support parallel tool calls. You will have to use a combination of streamText, createStreamableUI and createStreamableValue.

Wit

*[Content truncated - see full docs]*

**Examples**:

```tsx
import { openai } from '@ai-sdk/openai';import { getMutableAIState, streamUI } from '@ai-sdk/rsc';
export async function sendMessage(message: string) {  'use server';
  const messages = getMutableAIState('messages');
  messages.update([...messages.get(), { role: 'user', content: message }]);
  const { value: stream } = await streamUI({    model: openai('gpt-4o'),    system: 'you are a friendly assistant!',    messages: messages.get(),    text: async function* ({ content, done }) {      // proces
...
```

```tsx
import { openai } from '@ai-sdk/openai';import { getMutableAIState, streamUI } from '@ai-sdk/rsc';
export async function sendMessage(message: string) {  'use server';
  const messages = getMutableAIState('messages');
  messages.update([...messages.get(), { role: 'user', content: message }]);
  const { value: stream } = await streamUI({    model: openai('gpt-4o'),    system: 'you are a friendly assistant!',    messages: messages.get(),    text: async function* ({ content, done }) {      // proces
...
```

```tsx
'use client';
import { useState, ReactNode } from 'react';import { useActions, useUIState } from '@ai-sdk/rsc';
export default function Page() {  const { sendMessage } = useActions();  const [input, setInput] = useState('');  const [messages, setMessages] = useUIState();
  return (    <div>      {messages.map(message => message)}
      <form        onSubmit={async () => {          const response: ReactNode = await sendMessage(input);          setMessages(msgs => [...msgs, response]);        }}  
...
```

---

## Navigating the Library

**URL**: https://ai-sdk.dev/docs/getting-started/navigating-the-library

**Contents**:
- Navigating the Library
- Choosing the Right Tool for Your Environment
- Environment Compatibility
- When to use AI SDK UI
- AI SDK UI Framework Compatibility
- When to use AI SDK RSC

The AI SDK is a powerful toolkit for building AI applications. This page will help you pick the right tools for your requirements.

Let’s start with a quick overview of the AI SDK, which is comprised of three parts:

When deciding which part of the AI SDK to use, your first consideration should be the environment and existing stack you are working with. Different components of the SDK are tailored to specific frameworks and environments.

These tools have been designed to work seamlessly with each other and it's likely that you will be using them together. Let's look at how you could decide which libraries to use based on your application environment, existing stack, and requirements.

The following table outlines AI SDK compatibility based on environment:

AI SDK UI provides a set of framework-agnostic hooks for quickly building production-ready AI-native applications. It offers:

AI SDK UI supports the following frameworks: React, Svelte, and Vue.js. Here is a comparison of the supported functions across these frameworks:

Contributions are welcome to implement missing features for non-React frameworks.

AI SDK RSC is currently experimental. We recommend using AI SDK UI for production. For guidance on migrating from RSC to UI, see our migration guide.

React Server Components (RSCs) provide a new approach to building React applications that allow components to render on the server, fetch data directly, and stream the results to the client, reducing bundle size and improving performance. They also introduce a new way to call server-side functions from anywhere in your application called Server Actions.

AI SDK RSC provides a number of utilities that allow you to stream values and UI directly from the server to the client. However, it's important to be aware of current limitations:

Given these limitations, we recommend using AI SDK UI for production applications.

---

## Prompt Engineering

**URL**: https://ai-sdk.dev/docs/advanced/prompt-engineering

**Contents**:
- Prompt Engineering
- What is a Large Language Model (LLM)?
- What is a prompt?
- Why is prompt engineering needed?
- Example: Build a Slogan Generator
  - Start with an instruction
  - Include examples
  - Tweak your settings

A Large Language Model is essentially a prediction engine that takes a sequence of words as input and aims to predict the most likely sequence to follow. It does this by assigning probabilities to potential next sequences and then selecting one. The model continues to generate sequences until it meets a specified stopping criterion.

These models learn by training on massive text corpuses, which means they will be better suited to some use cases than others. For example, a model trained on GitHub data would understand the probabilities of sequences in source code particularly well. However, it's crucial to understand that the generated sequences, while often seeming plausible, can sometimes be random and not grounded in reality. As these models become more accurate, many surprising abilities and applications emerge.

Prompts are the starting points for LLMs. They are the inputs that trigger the model to generate text. The scope of prompt engineering involves not just crafting these prompts but also understanding related concepts such as hidden prompts, tokens, token limits, and the potential for prompt hacking, which includes phenomena like jailbreaks and leaks.

Prompt engineering currently plays a pivotal role in shaping the responses of LLMs. It allows us to tweak the model to respond more effectively to a broader range of queries. This includes the use of techniques like semantic search, command grammars, and the ReActive model architecture. The performance, context window, and cost of LLMs varies between models and model providers which adds further constraints to the mix. For example, the GPT-4 model is more expensive than GPT-3.5-turbo and significantly slower, but it can also be more effective at certain tasks. And so, like many things in software engineering, there is a trade-offs between cost and performance.

To assist with comparing and tweaking LLMs, we've built an AI playground that allows you to compare the performance of different models side-by-side

*[Content truncated - see full docs]*

---

## Prompts

**URL**: https://ai-sdk.dev/docs/foundations/prompts

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

## RAG Agent Guide

**URL**: https://ai-sdk.dev/docs/guides/rag-chatbot

**Contents**:
- RAG Agent Guide
  - What is RAG?
  - Why is RAG important?
  - Embedding
  - Chunking
  - All Together Now
- Project Setup
  - Clone Repo

In this guide, you will learn how to build a retrieval-augmented generation (RAG) agent.

Before we dive in, let's look at what RAG is, and why we would want to use it.

RAG stands for retrieval augmented generation. In simple terms, RAG is the process of providing a Large Language Model (LLM) with specific information relevant to the prompt.

While LLMs are powerful, the information they can reason on is restricted to the data they were trained on. This problem becomes apparent when asking an LLM for information outside of their training data, like proprietary data or common knowledge that has occurred after the model’s training cutoff. RAG solves this problem by fetching information relevant to the prompt and then passing that to the model as context.

To illustrate with a basic example, imagine asking the model for your favorite food:

Not surprisingly, the model doesn’t know. But imagine, alongside your prompt, the model received some extra context:

Just like that, you have augmented the model’s generation by providing relevant information to the query. Assuming the model has the appropriate information, it is now highly likely to return an accurate response to the users query. But how does it retrieve the relevant information? The answer relies on a concept called embedding.

You could fetch any context for your RAG application (eg. Google search). Embeddings and Vector Databases are just a specific retrieval approach to achieve semantic search.

Embeddings are a way to represent words, phrases, or images as vectors in a high-dimensional space. In this space, similar words are close to each other, and the distance between words can be used to measure their similarity.

In practice, this means that if you embedded the words cat and dog, you would expect them to be plotted close to each other in vector space. The process of calculating the similarity between two vectors is called ‘cosine similarity’ where a value of 1 would indicate high similarity and a value o

*[Content truncated - see full docs]*

**Examples**:

```txt
**input**What is my favorite food?
**generation**I don't have access to personal information about individuals, including theirfavorite foods.
```

```txt
**input**What is my favorite food?
**generation**I don't have access to personal information about individuals, including theirfavorite foods.
```

```txt
**input**Respond to the user's prompt using only the provided context.user prompt: 'What is my favorite food?'context: user loves chicken nuggets
**generation**Your favorite food is chicken nuggets!
```

---

## Saving and Restoring States

**URL**: https://ai-sdk.dev/docs/ai-sdk-rsc/saving-and-restoring-states

**Contents**:
- Saving and Restoring States
- AI State
  - Saving AI state
  - Restoring AI state
- UI State
  - Saving UI state
  - Restoring UI state

AI SDK RSC is currently experimental. We recommend using AI SDK UI for production. For guidance on migrating from RSC to UI, see our migration guide.

AI SDK RSC provides convenient methods for saving and restoring AI and UI state. This is useful for saving the state of your application after every model generation, and restoring it when the user revisits the generations.

The AI state can be saved using the onSetAIState callback, which gets called whenever the AI state is updated. In the following example, you save the chat history to a database whenever the generation is marked as done.

The AI state can be restored using the initialAIState prop passed to the context provider created by the createAI function. In the following example, you restore the chat history from a database when the component is mounted.

The UI state cannot be saved directly, since the contents aren't yet serializable. Instead, you can use the AI state as proxy to store details about the UI state and use it to restore the UI state when needed.

The UI state can be restored using the AI state as a proxy. In the following example, you restore the chat history from the AI state when the component is mounted. You use the onGetUIState callback to listen for SSR events and restore the UI state.

To learn more, check out this example that persists and restores states in your Next.js application.

Next, you will learn how you can use @ai-sdk/rsc functions like useActions and useUIState to create interactive, multistep interfaces.

**Examples**:

```tsx
export const AI = createAI<ServerMessage[], ClientMessage[]>({  actions: {    continueConversation,  },  onSetAIState: async ({ state, done }) => {    'use server';
    if (done) {      saveChatToDB(state);    }  },});
```

```tsx
export const AI = createAI<ServerMessage[], ClientMessage[]>({  actions: {    continueConversation,  },  onSetAIState: async ({ state, done }) => {    'use server';
    if (done) {      saveChatToDB(state);    }  },});
```

```tsx
import { ReactNode } from 'react';import { AI } from './ai';
export default async function RootLayout({  children,}: Readonly<{ children: ReactNode }>) {  const chat = await loadChatFromDB();
  return (    <html lang="en">      <body>        <AI initialAIState={chat}>{children}</AI>      </body>    </html>  );}
```

---

## Tools

**URL**: https://ai-sdk.dev/docs/foundations/tools

**Contents**:
- Tools
- What is a tool?
- Schemas
- Toolkits
- Learn more

While large language models (LLMs) have incredible generation capabilities, they struggle with discrete tasks (e.g. mathematics) and interacting with the outside world (e.g. getting the weather).

Tools are actions that an LLM can invoke. The results of these actions can be reported back to the LLM to be considered in the next response.

For example, when you ask an LLM for the "weather in London", and there is a weather tool available, it could call a tool with London as the argument. The tool would then fetch the weather data and return it to the LLM. The LLM can then use this information in its response.

A tool is an object that can be called by the model to perform a specific task. You can use tools with generateText and streamText by passing one or more tools to the tools parameter.

A tool consists of three properties:

streamUI uses UI generator tools with a generate function that can return React components.

If the LLM decides to use a tool, it will generate a tool call. Tools with an execute function are run automatically when these calls are generated. The output of the tool calls are returned using tool result objects.

You can automatically pass tool results back to the LLM using multi-step calls with streamText and generateText.

Schemas are used to define the parameters for tools and to validate the tool calls.

The AI SDK supports both raw JSON schemas (using the jsonSchema function) and Zod schemas (either directly or using the zodSchema function).

Zod is a popular TypeScript schema validation library. You can install it with:

You can then specify a Zod schema, for example:

You can also use schemas for structured output generation with generateObject and streamObject.

When you work with tools, you typically need a mix of application specific tools and general purpose tools. There are several providers that offer pre-built tools as toolkits that you can use out of the box:

Do you have open source tools or tool libraries that are compatible with

*[Content truncated - see full docs]*

**Examples**:

```text
pnpm add zod
```

```ts
import z from 'zod';
const recipeSchema = z.object({  recipe: z.object({    name: z.string(),    ingredients: z.array(      z.object({        name: z.string(),        amount: z.string(),      }),    ),    steps: z.array(z.string()),  }),});
```

```ts
import z from 'zod';
const recipeSchema = z.object({  recipe: z.object({    name: z.string(),    ingredients: z.array(      z.object({        name: z.string(),        amount: z.string(),      }),    ),    steps: z.array(z.string()),  }),});
```

---

## Transport

**URL**: https://ai-sdk.dev/docs/ai-sdk-ui/transport

**Contents**:
- Transport
- Default Transport
- Custom Transport Configuration
  - Dynamic Configuration
  - Request Transformation
- Building Custom Transports

The useChat transport system provides fine-grained control over how messages are sent to your API endpoints and how responses are processed. This is particularly useful for alternative communication protocols like WebSockets, custom authentication patterns, or specialized backend integrations.

By default, useChat uses HTTP POST requests to send messages to /api/chat:

This is equivalent to:

Configure the default transport with custom options:

You can also provide functions that return configuration values. This is useful for authentication tokens that need to be refreshed, or for configuration that depends on runtime conditions:

Transform requests before sending to your API:

To understand how to build your own transport, refer to the source code of the default implementation:

These implementations show you exactly how to:

The transport system gives you complete control over how your chat application communicates, enabling integration with any backend protocol or service.

**Examples**:

```tsx
import { useChat } from '@ai-sdk/react';
// Uses default HTTP transportconst { messages, sendMessage } = useChat();
```

```tsx
import { useChat } from '@ai-sdk/react';
// Uses default HTTP transportconst { messages, sendMessage } = useChat();
```

```tsx
import { useChat } from '@ai-sdk/react';import { DefaultChatTransport } from 'ai';
const { messages, sendMessage } = useChat({  transport: new DefaultChatTransport({    api: '/api/chat',  }),});
```

---

## Workflow Patterns

**URL**: https://ai-sdk.dev/docs/agents/workflows

**Contents**:
- Workflow Patterns
- Choose Your Approach
- Patterns with Examples
- Sequential Processing (Chains)
- Routing
- Parallel Processing
- Orchestrator-Worker
- Evaluator-Optimizer

Combine the building blocks from the overview with these patterns to add structure and reliability to your agents:

Consider these key factors:

Start with the simplest approach that meets your needs. Add complexity only when required by:

Let's look at examples of these patterns in action.

These patterns, adapted from Anthropic's guide on building effective agents, serve as building blocks you can combine to create comprehensive workflows. Each pattern addresses specific aspects of task execution. Combine them thoughtfully to build reliable solutions for complex problems.

The simplest workflow pattern executes steps in a predefined order. Each step's output becomes input for the next step, creating a clear chain of operations. Use this pattern for tasks with well-defined sequences, like content generation pipelines or data transformation processes.

This pattern lets the model decide which path to take through a workflow based on context and intermediate results. The model acts as an intelligent router, directing the flow of execution between different branches of your workflow. Use this when handling varied inputs that require different processing approaches. In the example below, the first LLM call's results determine the second call's model size and system prompt.

Break down tasks into independent subtasks that execute simultaneously. This pattern uses parallel execution to improve efficiency while maintaining the benefits of structured workflows. For example, analyze multiple documents or process different aspects of a single input concurrently (like code review).

A primary model (orchestrator) coordinates the execution of specialized workers. Each worker optimizes for a specific subtask, while the orchestrator maintains overall context and ensures coherent results. This pattern excels at complex tasks requiring different types of expertise or processing.

Add quality control to workflows with dedicated evaluation steps that assess intermediate results. Bas

*[Content truncated - see full docs]*

**Examples**:

```ts
import { generateText, generateObject } from 'ai';import { z } from 'zod';
async function generateMarketingCopy(input: string) {  const model = 'openai/gpt-4o';
  // First step: Generate marketing copy  const { text: copy } = await generateText({    model,    prompt: `Write persuasive marketing copy for: ${input}. Focus on benefits and emotional appeal.`,  });
  // Perform quality check on copy  const { object: qualityMetrics } = await generateObject({    model,    schema: z.object({      hasCal
...
```

```ts
import { generateText, generateObject } from 'ai';import { z } from 'zod';
async function generateMarketingCopy(input: string) {  const model = 'openai/gpt-4o';
  // First step: Generate marketing copy  const { text: copy } = await generateText({    model,    prompt: `Write persuasive marketing copy for: ${input}. Focus on benefits and emotional appeal.`,  });
  // Perform quality check on copy  const { object: qualityMetrics } = await generateObject({    model,    schema: z.object({      hasCal
...
```

```ts
import { generateObject, generateText } from 'ai';import { z } from 'zod';
async function handleCustomerQuery(query: string) {  const model = 'openai/gpt-4o';
  // First step: Classify the query type  const { object: classification } = await generateObject({    model,    schema: z.object({      reasoning: z.string(),      type: z.enum(['general', 'refund', 'technical']),      complexity: z.enum(['simple', 'complex']),    }),    prompt: `Classify this customer query:    ${query}
    Determine:   
...
```

---
