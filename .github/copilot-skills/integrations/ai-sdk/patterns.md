# Ai-Sdk - Common Patterns

Quick reference for common ai-sdk patterns and usage.

## Code Patterns

### 1. This simple example demonstrates how tools can expand your model's capabilities. You can create more

```
pnpm add @ungap/structured-clone @stardazed/streams-text-encoding
```

### 2. This simple example demonstrates how tools can expand your model's capabilities. You can create more

```
@ai-sdk/svelte
```

### 3. import { generateObject, NoObjectGeneratedError } from 'ai'; try { await generateObject({ model, sch

```
import { generateObject, NoObjectGeneratedError } from 'ai';
try {  await generateObject({ model, schema, prompt });} catch (error) {  if (NoObjectGeneratedError.isInstance(error)) {    console.log('NoObjectGeneratedError');    console.log('Cause:', error.cause);    console.log('Text:', error.text);
```

### 4. app/chat/[chatId]/chat.tsximport { useChat } from '@ai-sdk/react';import { DefaultChatTransport } fr

```
import { useChat } from '@ai-sdk/react';import { DefaultChatTransport } from 'ai';
export function Chat({ chatData, resume }) {  const { messages, sendMessage } = useChat({    id: chatData.id,    messages: chatData.messages,    resume,    transport: new DefaultChatTransport({      // Customize recon
```

### 5. // Or use a different pattern:

```
resume: true
```

### 6. // Or use a different pattern:

```
resume: true
```

### 7. const codeReviewAgent = new Agent({ model: 'openai/gpt-4o', system: `You are a senior software engin

```
const codeReviewAgent = new Agent({  model: 'openai/gpt-4o',  system: `You are a senior software engineer conducting code reviews.
  Your approach:  - Focus on security vulnerabilities first  - Identify performance bottlenecks  - Suggest improvements for readability and maintainability  - Be constru
```

### 8. - Always explain why something is an issue and how to fix it`,

```
const customerSupportAgent = new Agent({  model: 'openai/gpt-4o',  system: `You are a customer support specialist for an e-commerce platform.
  Rules:  - Never make promises about refunds without checking the policy  - Always be empathetic and professional  - If you don't know something, say so and 
```

## Examples

### Example 1

```prompt
Documentation:{paste documentation here}---Based on the above documentation, answer the following:{your question}
```

### Example 2

```prompt
Documentation:{paste documentation here}---Based on the above documentation, answer the following:{your question}
```

### Example 3

```bash
mkdir my-ai-appcd my-ai-apppnpm init
```

### Example 4

```bash
mkdir my-ai-appcd my-ai-apppnpm init
```

### Example 5

```typescript
import { NoContentGeneratedError } from 'ai';
if (NoContentGeneratedError.isInstance(error)) {  // Handle the error}
```

### Example 6

```typescript
import { NoContentGeneratedError } from 'ai';
if (NoContentGeneratedError.isInstance(error)) {  // Handle the error}
```

### Example 7

```typescript
import { generateImage, NoImageGeneratedError } from 'ai';
try {  await generateImage({ model, prompt });} catch (error) {  if (NoImageGeneratedError.isInstance(error)) {    console.log('NoImageGeneratedError');    console.log('Cause:', error.cause);    console.log('Responses:', error.responses);  }}
```

### Example 8

```typescript
import { generateImage, NoImageGeneratedError } from 'ai';
try {  await generateImage({ model, prompt });} catch (error) {  if (NoImageGeneratedError.isInstance(error)) {    console.log('NoImageGeneratedError');    console.log('Cause:', error.cause);    console.log('Responses:', error.responses);  }}
```

### Example 9

```typescript
import { NoSpeechGeneratedError } from 'ai';
if (NoSpeechGeneratedError.isInstance(error)) {  // Handle the error}
```

### Example 10

```typescript
import { NoSpeechGeneratedError } from 'ai';
if (NoSpeechGeneratedError.isInstance(error)) {  // Handle the error}
```


## Categories

See organized documentation in `references/`:

- `references/core.md` - Core
- `references/getting_started.md` - Getting Started
- `references/integrations.md` - Integrations
- `references/other.md` - Other
- `references/providers.md` - Providers
- `references/reference.md` - Reference
