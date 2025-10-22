# Ai-Sdk - Reference

**Pages**: 29

---

## AI_APICallError

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-errors/ai-api-call-error

**Contents**:
- AI_APICallError
- Properties
- Checking for this Error

This error occurs when an API call fails.

You can check if an error is an instance of AI_APICallError using:

**Examples**:

```typescript
import { APICallError } from 'ai';
if (APICallError.isInstance(error)) {  // Handle the error}
```

```typescript
import { APICallError } from 'ai';
if (APICallError.isInstance(error)) {  // Handle the error}
```

---

## AI_DownloadError

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-errors/ai-download-error

**Contents**:
- AI_DownloadError
- Properties
- Checking for this Error

This error occurs when a download fails.

You can check if an error is an instance of AI_DownloadError using:

**Examples**:

```typescript
import { DownloadError } from 'ai';
if (DownloadError.isInstance(error)) {  // Handle the error}
```

```typescript
import { DownloadError } from 'ai';
if (DownloadError.isInstance(error)) {  // Handle the error}
```

---

## AI_EmptyResponseBodyError

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-errors/ai-empty-response-body-error

**Contents**:
- AI_EmptyResponseBodyError
- Properties
- Checking for this Error

This error occurs when the server returns an empty response body.

You can check if an error is an instance of AI_EmptyResponseBodyError using:

**Examples**:

```typescript
import { EmptyResponseBodyError } from 'ai';
if (EmptyResponseBodyError.isInstance(error)) {  // Handle the error}
```

```typescript
import { EmptyResponseBodyError } from 'ai';
if (EmptyResponseBodyError.isInstance(error)) {  // Handle the error}
```

---

## AI_InvalidArgumentError

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-errors/ai-invalid-argument-error

**Contents**:
- AI_InvalidArgumentError
- Properties
- Checking for this Error

This error occurs when an invalid argument was provided.

You can check if an error is an instance of AI_InvalidArgumentError using:

**Examples**:

```typescript
import { InvalidArgumentError } from 'ai';
if (InvalidArgumentError.isInstance(error)) {  // Handle the error}
```

```typescript
import { InvalidArgumentError } from 'ai';
if (InvalidArgumentError.isInstance(error)) {  // Handle the error}
```

---

## AI_InvalidDataContentError

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-errors/ai-invalid-data-content-error

**Contents**:
- AI_InvalidDataContentError
- Properties
- Checking for this Error

This error occurs when the data content provided in a multi-modal message part is invalid. Check out the prompt examples for multi-modal messages .

You can check if an error is an instance of AI_InvalidDataContentError using:

**Examples**:

```typescript
import { InvalidDataContentError } from 'ai';
if (InvalidDataContentError.isInstance(error)) {  // Handle the error}
```

```typescript
import { InvalidDataContentError } from 'ai';
if (InvalidDataContentError.isInstance(error)) {  // Handle the error}
```

---

## AI_InvalidDataContent

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-errors/ai-invalid-data-content

**Contents**:
- AI_InvalidDataContent
- Properties
- Checking for this Error

This error occurs when invalid data content is provided.

You can check if an error is an instance of AI_InvalidDataContent using:

**Examples**:

```typescript
import { InvalidDataContent } from 'ai';
if (InvalidDataContent.isInstance(error)) {  // Handle the error}
```

```typescript
import { InvalidDataContent } from 'ai';
if (InvalidDataContent.isInstance(error)) {  // Handle the error}
```

---

## AI_InvalidMessageRoleError

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-errors/ai-invalid-message-role-error

**Contents**:
- AI_InvalidMessageRoleError
- Properties
- Checking for this Error

This error occurs when an invalid message role is provided.

You can check if an error is an instance of AI_InvalidMessageRoleError using:

**Examples**:

```typescript
import { InvalidMessageRoleError } from 'ai';
if (InvalidMessageRoleError.isInstance(error)) {  // Handle the error}
```

```typescript
import { InvalidMessageRoleError } from 'ai';
if (InvalidMessageRoleError.isInstance(error)) {  // Handle the error}
```

---

## AI_InvalidPromptError

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-errors/ai-invalid-prompt-error

**Contents**:
- AI_InvalidPromptError
- Properties
- Checking for this Error

This error occurs when the prompt provided is invalid.

You can check if an error is an instance of AI_InvalidPromptError using:

**Examples**:

```typescript
import { InvalidPromptError } from 'ai';
if (InvalidPromptError.isInstance(error)) {  // Handle the error}
```

```typescript
import { InvalidPromptError } from 'ai';
if (InvalidPromptError.isInstance(error)) {  // Handle the error}
```

---

## AI_InvalidResponseDataError

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-errors/ai-invalid-response-data-error

**Contents**:
- AI_InvalidResponseDataError
- Properties
- Checking for this Error

This error occurs when the server returns a response with invalid data content.

You can check if an error is an instance of AI_InvalidResponseDataError using:

**Examples**:

```typescript
import { InvalidResponseDataError } from 'ai';
if (InvalidResponseDataError.isInstance(error)) {  // Handle the error}
```

```typescript
import { InvalidResponseDataError } from 'ai';
if (InvalidResponseDataError.isInstance(error)) {  // Handle the error}
```

---

## AI_InvalidToolInputError

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-errors/ai-invalid-tool-input-error

**Contents**:
- AI_InvalidToolInputError
- Properties
- Checking for this Error

This error occurs when invalid tool input was provided.

You can check if an error is an instance of AI_InvalidToolInputError using:

**Examples**:

```typescript
import { InvalidToolInputError } from 'ai';
if (InvalidToolInputError.isInstance(error)) {  // Handle the error}
```

```typescript
import { InvalidToolInputError } from 'ai';
if (InvalidToolInputError.isInstance(error)) {  // Handle the error}
```

---

## AI_JSONParseError

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-errors/ai-json-parse-error

**Contents**:
- AI_JSONParseError
- Properties
- Checking for this Error

This error occurs when JSON fails to parse.

You can check if an error is an instance of AI_JSONParseError using:

**Examples**:

```typescript
import { JSONParseError } from 'ai';
if (JSONParseError.isInstance(error)) {  // Handle the error}
```

```typescript
import { JSONParseError } from 'ai';
if (JSONParseError.isInstance(error)) {  // Handle the error}
```

---

## AI_LoadAPIKeyError

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-errors/ai-load-api-key-error

**Contents**:
- AI_LoadAPIKeyError
- Properties
- Checking for this Error

This error occurs when API key is not loaded successfully.

You can check if an error is an instance of AI_LoadAPIKeyError using:

**Examples**:

```typescript
import { LoadAPIKeyError } from 'ai';
if (LoadAPIKeyError.isInstance(error)) {  // Handle the error}
```

```typescript
import { LoadAPIKeyError } from 'ai';
if (LoadAPIKeyError.isInstance(error)) {  // Handle the error}
```

---

## AI_LoadSettingError

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-errors/ai-load-setting-error

**Contents**:
- AI_LoadSettingError
- Properties
- Checking for this Error

This error occurs when a setting is not loaded successfully.

You can check if an error is an instance of AI_LoadSettingError using:

**Examples**:

```typescript
import { LoadSettingError } from 'ai';
if (LoadSettingError.isInstance(error)) {  // Handle the error}
```

```typescript
import { LoadSettingError } from 'ai';
if (LoadSettingError.isInstance(error)) {  // Handle the error}
```

---

## AI_MessageConversionError

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-errors/ai-message-conversion-error

**Contents**:
- AI_MessageConversionError
- Properties
- Checking for this Error

This error occurs when message conversion fails.

You can check if an error is an instance of AI_MessageConversionError using:

**Examples**:

```typescript
import { MessageConversionError } from 'ai';
if (MessageConversionError.isInstance(error)) {  // Handle the error}
```

```typescript
import { MessageConversionError } from 'ai';
if (MessageConversionError.isInstance(error)) {  // Handle the error}
```

---

## AI_NoOutputSpecifiedError

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-errors/ai-no-output-specified-error

**Contents**:
- AI_NoOutputSpecifiedError
- Properties
- Checking for this Error

This error occurs when no output format was specified for the AI response, and output-related methods are called.

You can check if an error is an instance of AI_NoOutputSpecifiedError using:

**Examples**:

```typescript
import { NoOutputSpecifiedError } from 'ai';
if (NoOutputSpecifiedError.isInstance(error)) {  // Handle the error}
```

```typescript
import { NoOutputSpecifiedError } from 'ai';
if (NoOutputSpecifiedError.isInstance(error)) {  // Handle the error}
```

---

## AI_NoSuchModelError

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-errors/ai-no-such-model-error

**Contents**:
- AI_NoSuchModelError
- Properties
- Checking for this Error

This error occurs when a model ID is not found.

You can check if an error is an instance of AI_NoSuchModelError using:

**Examples**:

```typescript
import { NoSuchModelError } from 'ai';
if (NoSuchModelError.isInstance(error)) {  // Handle the error}
```

```typescript
import { NoSuchModelError } from 'ai';
if (NoSuchModelError.isInstance(error)) {  // Handle the error}
```

---

## AI_NoSuchProviderError

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-errors/ai-no-such-provider-error

**Contents**:
- AI_NoSuchProviderError
- Properties
- Checking for this Error

This error occurs when a provider ID is not found.

You can check if an error is an instance of AI_NoSuchProviderError using:

**Examples**:

```typescript
import { NoSuchProviderError } from 'ai';
if (NoSuchProviderError.isInstance(error)) {  // Handle the error}
```

```typescript
import { NoSuchProviderError } from 'ai';
if (NoSuchProviderError.isInstance(error)) {  // Handle the error}
```

---

## AI_NoSuchToolError

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-errors/ai-no-such-tool-error

**Contents**:
- AI_NoSuchToolError
- Properties
- Checking for this Error

This error occurs when a model tries to call an unavailable tool.

You can check if an error is an instance of AI_NoSuchToolError using:

**Examples**:

```typescript
import { NoSuchToolError } from 'ai';
if (NoSuchToolError.isInstance(error)) {  // Handle the error}
```

```typescript
import { NoSuchToolError } from 'ai';
if (NoSuchToolError.isInstance(error)) {  // Handle the error}
```

---

## AI_RetryError

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-errors/ai-retry-error

**Contents**:
- AI_RetryError
- Properties
- Checking for this Error

This error occurs when a retry operation fails.

You can check if an error is an instance of AI_RetryError using:

**Examples**:

```typescript
import { RetryError } from 'ai';
if (RetryError.isInstance(error)) {  // Handle the error}
```

```typescript
import { RetryError } from 'ai';
if (RetryError.isInstance(error)) {  // Handle the error}
```

---

## AI SDK Errors

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-errors

**Contents**:
- AI SDK Errors

---

## AI SDK RSC

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-rsc

**Contents**:
- AI SDK RSC

AI SDK RSC is currently experimental. We recommend using AI SDK UI for production. For guidance on migrating from RSC to UI, see our migration guide.

---

## AI_TooManyEmbeddingValuesForCallError

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-errors/ai-too-many-embedding-values-for-call-error

**Contents**:
- AI_TooManyEmbeddingValuesForCallError
- Properties
- Checking for this Error

This error occurs when too many values are provided in a single embedding call.

You can check if an error is an instance of AI_TooManyEmbeddingValuesForCallError using:

**Examples**:

```typescript
import { TooManyEmbeddingValuesForCallError } from 'ai';
if (TooManyEmbeddingValuesForCallError.isInstance(error)) {  // Handle the error}
```

```typescript
import { TooManyEmbeddingValuesForCallError } from 'ai';
if (TooManyEmbeddingValuesForCallError.isInstance(error)) {  // Handle the error}
```

---

## AI_TypeValidationError

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-errors/ai-type-validation-error

**Contents**:
- AI_TypeValidationError
- Properties
- Checking for this Error

This error occurs when type validation fails.

You can check if an error is an instance of AI_TypeValidationError using:

**Examples**:

```typescript
import { TypeValidationError } from 'ai';
if (TypeValidationError.isInstance(error)) {  // Handle the error}
```

```typescript
import { TypeValidationError } from 'ai';
if (TypeValidationError.isInstance(error)) {  // Handle the error}
```

---

## AI_UnsupportedFunctionalityError

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-errors/ai-unsupported-functionality-error

**Contents**:
- AI_UnsupportedFunctionalityError
- Properties
- Checking for this Error

This error occurs when functionality is not unsupported.

You can check if an error is an instance of AI_UnsupportedFunctionalityError using:

**Examples**:

```typescript
import { UnsupportedFunctionalityError } from 'ai';
if (UnsupportedFunctionalityError.isInstance(error)) {  // Handle the error}
```

```typescript
import { UnsupportedFunctionalityError } from 'ai';
if (UnsupportedFunctionalityError.isInstance(error)) {  // Handle the error}
```

---

## API Reference

**URL**: https://ai-sdk.dev/docs/reference

**Contents**:
- API Reference

---

## ToolCallRepairError

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-errors/ai-tool-call-repair-error

**Contents**:
- ToolCallRepairError
- Properties
- Checking for this Error

This error occurs when there is a failure while attempting to repair an invalid tool call. This typically happens when the AI attempts to fix either a NoSuchToolError or InvalidToolInputError.

You can check if an error is an instance of ToolCallRepairError using:

**Examples**:

```typescript
import { ToolCallRepairError } from 'ai';
if (ToolCallRepairError.isInstance(error)) {  // Handle the error}
```

```typescript
import { ToolCallRepairError } from 'ai';
if (ToolCallRepairError.isInstance(error)) {  // Handle the error}
```

---

## pruneMessages()

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-ui/prune-messages

**Contents**:
- pruneMessages()
- Import
- API Signature
  - Parameters
  - messages:
  - reasoning:
  - toolCalls:
  - emptyMessages:

The pruneMessages function is used to prune or filter an array of ModelMessage objects. This is useful for reducing message context (to save tokens), removing intermediate reasoning, or trimming tool calls and empty messages before sending to an LLM.

An array of ModelMessage objects, pruned according to the provided options.

Tip: pruneMessages is typically used prior to sending a context window to an LLM to reduce message/token count, especially after a series of tool-calls and approvals.

For advanced usage and the full list of possible message parts, see ModelMessage and pruneMessages implementation.

**Examples**:

```ts
import { pruneMessages, streamText } from 'ai';
export async function POST(req: Request) {  const { messages } = await req.json();
  const prunedMessages = pruneMessages({    messages,    reasoning: 'before-last-message',    toolCalls: 'before-last-2-messages',    emptyMessages: 'remove',  });
  const result = streamText({    model: 'openai/gpt-4o',    messages: prunedMessages,  });
  return result.toUIMessageStreamResponse();}
```

```ts
import { pruneMessages, streamText } from 'ai';
export async function POST(req: Request) {  const { messages } = await req.json();
  const prunedMessages = pruneMessages({    messages,    reasoning: 'before-last-message',    toolCalls: 'before-last-2-messages',    emptyMessages: 'remove',  });
  const result = streamText({    model: 'openai/gpt-4o',    messages: prunedMessages,  });
  return result.toUIMessageStreamResponse();}
```

```python
import { pruneMessages } from "ai"
```

---

## useChat()

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-ui/use-chat

**Contents**:
- useChat()
- Import
- API Signature
  - Parameters
  - chat?:
  - transport?:
  - api?:
  - credentials?:

Allows you to easily create a conversational user interface for your chatbot application. It enables the streaming of chat messages from your AI provider, manages the chat state, and updates the UI automatically as new messages are received.

The useChat API has been significantly updated in AI SDK 5.0. It now uses a transport-based architecture and no longer manages input state internally. See the migration guide for details.

**Examples**:

```python
import { useChat } from '@ai-sdk/react'
```

---

## useCompletion()

**URL**: https://ai-sdk.dev/docs/reference/ai-sdk-ui/use-completion

**Contents**:
- useCompletion()
- Import
- API Signature
  - Parameters
  - api:
  - id:
  - initialInput:
  - initialCompletion:

Allows you to create text completion based capabilities for your application. It enables the streaming of text completions from your AI provider, manages the state for chat input, and updates the UI automatically as new messages are received.

**Examples**:

```python
import { useCompletion } from '@ai-sdk/react'
```

---
