# Claude - Api

**Pages**: 108

---

## Add Workspace Member

**URL**: https://docs.claude.com/en/api/admin-api/workspace_members/create-workspace-member

**Contents**:
    - Headers
    - Path Parameters
    - Body
    - Response

Your unique Admin API key for authentication.

This key is required in the header of all Admin API requests, to authenticate your account and access Anthropic's services. Get your Admin API key through the Console.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

"user_01WCz1FkmYMm4gnmykNKUu3Q"

Role of the new Workspace Member. Cannot be "workspace_billing".

For Workspace Members, this is always "workspace_member".

"user_01WCz1FkmYMm4gnmykNKUu3Q"

"wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"

Role of the Workspace Member.

---

## Agent SDK reference - Python

**URL**: https://docs.claude.com/en/api/agent-sdk/python

**Contents**:
- ​Installation
- ​Choosing Between query() and ClaudeSDKClient
  - ​Quick Comparison
  - ​When to Use query() (New Session Each Time)
  - ​When to Use ClaudeSDKClient (Continuous Conversation)
- ​Functions
  - ​query()
    - ​Parameters

**Examples**:

```text
pip install claude-agent-sdk
```

```python
async def query(
    *,
    prompt: str | AsyncIterable[dict[str, Any]],
    options: ClaudeAgentOptions | None = None
) -> AsyncIterator[Message]
```

```python
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions

async def main():
    options = ClaudeAgentOptions(
        system_prompt="You are an expert Python developer",
        permission_mode='acceptEdits',
        cwd="/home/user/project"
    )

    async for message in query(
        prompt="Create a Python web server",
        options=options
    ):
        print(message)


asyncio.run(main())
```

---

## Agent SDK reference - TypeScript

**URL**: https://docs.claude.com/en/api/agent-sdk/typescript

**Contents**:
- ​Installation
- ​Functions
  - ​query()
    - ​Parameters
    - ​Returns
  - ​tool()
    - ​Parameters
  - ​createSdkMcpServer()

**Examples**:

```text
npm install @anthropic-ai/claude-agent-sdk
```

```javascript
function query({
  prompt,
  options
}: {
  prompt: string | AsyncIterable<SDKUserMessage>;
  options?: Options;
}): Query
```

```javascript
function tool<Schema extends ZodRawShape>(
  name: string,
  description: string,
  inputSchema: Schema,
  handler: (args: z.infer<ZodObject<Schema>>, extra: unknown) => Promise<CallToolResult>
): SdkMcpToolDefinition<Schema>
```

---

## Amazon Bedrock API

**URL**: https://docs.claude.com/en/api/claude-on-amazon-bedrock

**Contents**:
- ​Install and configure the AWS CLI
- ​Install an SDK for accessing Bedrock
- ​Accessing Bedrock
  - ​Subscribe to Anthropic models
    - ​API model IDs
  - ​List available models
  - ​Making requests
- ​Activity logging

**Examples**:

```text
aws sts get-caller-identity
```

```text
pip install -U "anthropic[bedrock]"
```

```text
aws bedrock list-foundation-models --region=us-west-2 --by-provider anthropic --query "modelSummaries[*].modelId"
```

---

## Archive Workspace

**URL**: https://docs.claude.com/en/api/admin-api/workspaces/archive-workspace

**Contents**:
    - Headers
    - Path Parameters
    - Response

Your unique Admin API key for authentication.

This key is required in the header of all Admin API requests, to authenticate your account and access Anthropic's services. Get your Admin API key through the Console.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

RFC 3339 datetime string indicating when the Workspace was archived, or null if the Workspace is not archived.

"2024-11-01T23:59:27.427722Z"

RFC 3339 datetime string indicating when the Workspace was created.

"2024-10-30T23:58:27.427722Z"

Hex color code representing the Workspace in the Anthropic Console.

"wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"

Name of the Workspace.

For Workspaces, this is always "workspace".

---

## Batch processing

**URL**: https://docs.claude.com/en/docs/build-with-claude/batch-processing

**Contents**:
- ​Message Batches API
- ​How the Message Batches API works
  - ​Batch limitations
  - ​Supported models
  - ​What can be batched
- ​Pricing
- ​How to use the Message Batches API
  - ​Prepare and create your batch

How long does it take for a batch to process?

Is the Batches API available for all models?

Can I use the Message Batches API with other API features?

How does the Message Batches API affect pricing?

Can I update a batch after it's been submitted?

Are there Message Batches API rate limits and do they interact with the Messages API rate limits?

How do I handle errors in my batch requests?

How does the Message Batches API handle privacy and data separation?

Can I use prompt caching in the Message Batches API?

**Examples**:

```text
curl https://api.anthropic.com/v1/messages/batches \
     --header "x-api-key: $ANTHROPIC_API_KEY" \
     --header "anthropic-version: 2023-06-01" \
     --header "content-type: application/json" \
     --data \
'{
    "requests": [
        {
            "custom_id": "my-first-request",
            "params": {
                "model": "claude-sonnet-4-5",
                "max_tokens": 1024,
                "messages": [
                    {"role": "user", "content": "Hello, world"}
            
...
```

```text
{
  "id": "msgbatch_01HkcTjaV5uDC8jWR4ZsDV8d",
  "type": "message_batch",
  "processing_status": "in_progress",
  "request_counts": {
    "processing": 2,
    "succeeded": 0,
    "errored": 0,
    "canceled": 0,
    "expired": 0
  },
  "ended_at": null,
  "created_at": "2024-09-24T18:37:24.100435Z",
  "expires_at": "2024-09-25T18:37:24.100435Z",
  "cancel_initiated_at": null,
  "results_url": null
}
```

```text
curl https://api.anthropic.com/v1/messages/batches/msgbatch_01HkcTjaV5uDC8jWR4ZsDV8d \
 --header "x-api-key: $ANTHROPIC_API_KEY" \
 --header "anthropic-version: 2023-06-01" \
 | sed -E 's/.*"id":"([^"]+)".*"processing_status":"([^"]+)".*/Batch \1 processing status is \2/'
```

---

## Beta headers

**URL**: https://docs.claude.com/en/api/beta-headers

**Contents**:
- ​How to use beta headers
  - ​Multiple beta features
  - ​Version naming conventions
- ​Error handling
- ​Getting help

**Examples**:

```text
POST /v1/messages
Content-Type: application/json
X-API-Key: YOUR_API_KEY
anthropic-beta: BETA_FEATURE_NAME
```

```python
from anthropic import Anthropic

client = Anthropic()

response = client.beta.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude"}
    ],
    betas=["beta-feature-name"]
)
```

```text
anthropic-beta: feature1,feature2,feature3
```

---

## Cancel a Message Batch

**URL**: https://docs.claude.com/en/api/canceling-message-batches

**Contents**:
    - Headers
    - Path Parameters
    - Response

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like beta1,beta2 or specify the header multiple times for each beta.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

Your unique API key for authentication.

This key is required in the header of all API requests, to authenticate your account and access Anthropic's services. Get your API key through the Console. Each key is scoped to a Workspace.

ID of the Message Batch.

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

"2024-08-20T18:37:24.100435Z"

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

"2024-08-20T18:37:24.100435Z"

RFC 3339 datetime string representing the time at which the Message Batch was created.

"2024-08-20T18:37:24.100435Z"

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

"2024-08-20T18:37:24.100435Z"

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

"2024-08-20T18:37:24.100435Z"

Unique object identifier.

The format and length of IDs may change over time.

"msgbatch_013Zva2CMHLNnXjNJJKqJ2EF"

Processing status of the Message Batch.

Tallies requests within the Message Batch, categorized by their status.

Requests start as processing and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

Show child attributes

URL to a .jsonl file containing the results of the Message Batch requests. Specified only once proc

*[Content truncated - see full docs]*

---

## Choosing the right model

**URL**: https://docs.claude.com/en/docs/about-claude/models/choosing-a-model

**Contents**:
- ​Establish key criteria
- ​Choose the best model to start with
  - ​Option 1: Start with a fast, cost-effective model
  - ​Option 2: Start with the most capable model
- ​Model selection matrix
- ​Decide whether to upgrade or change models
- ​Next steps
- Model comparison chart

---

## Claude Code Analytics API

**URL**: https://docs.claude.com/en/api/claude-code-analytics-api

**Contents**:
- ​Quick start
- ​Claude Code Analytics API
  - ​Key concepts
  - ​Basic examples
    - ​Get analytics for a specific day
    - ​Get analytics with pagination
  - ​Request parameters
  - ​Available metrics

**Examples**:

```text
curl "https://api.anthropic.com/v1/organizations/usage_report/claude_code?\
starting_at=2025-09-08&\
limit=20" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ADMIN_API_KEY"
```

```text
User-Agent: YourApp/1.0.0 (https://yourapp.com)
```

```text
curl "https://api.anthropic.com/v1/organizations/usage_report/claude_code?\
starting_at=2025-09-08" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ADMIN_API_KEY"
```

---

## Claude Code Analytics API - Claude Docs

**URL**: https://docs.claude.com/en/api/claude-code-analytics-api

---

## Claude Developer Platform

**URL**: https://docs.claude.com/en/release-notes/api

**Contents**:
    - ​October 16, 2025
    - ​October 15, 2025
    - ​September 29, 2025
    - ​September 17, 2025
    - ​September 16, 2025
    - ​September 10, 2025
    - ​September 8, 2025
    - ​September 5, 2025

---

## Claude Developer Platform - Claude Docs

**URL**: https://docs.claude.com/en/release-notes/api

---

## Client SDKs

**URL**: https://docs.claude.com/en/api/client-sdks

**Contents**:
- ​Python
- ​TypeScript
- ​Java
- ​Go
- ​C#
- ​Ruby
- ​PHP
- ​Beta namespace in client SDKs

**Examples**:

```text
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude"}
    ]
)
print(message.content)
```

```text
# Claude 4 Models
"claude-opus-4-1-20250805"
"claude-opus-4-1"  # alias
"claude-opus-4-20250514"
"claude-opus-4-0"  # alias
"claude-sonnet-4-5-20250929"
"claude-sonnet-4-5"  # alias
"claude-sonnet-4-20250514"
"claude-sonnet-4-0"  # alias
"claude-haiku-4-5-20251001"
"claude-haiku-4-5"  # alias

# Claude 3.7 Models
"claude-3-7-sonnet-20250219"
"claude-3-7-sonnet-latest"  # alias

# Claude 3.5 Models
"claude-3-5-haiku-20241022"
"claude-3-5-haiku-latest"  # alias
"claude-3-5-sonnet-20241022"  # depr
...
```

```python
import Anthropic from '@anthropic-ai/sdk';

const anthropic = new Anthropic({
  apiKey: 'my_api_key', // defaults to process.env["ANTHROPIC_API_KEY"]
});

const msg = await anthropic.messages.create({
  model: "claude-sonnet-4-5",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Hello, Claude" }],
});
console.log(msg);
```

---

## Content moderation

**URL**: https://docs.claude.com/en/docs/about-claude/use-case-guides/content-moderation

**Contents**:
- ​Before building with Claude
  - ​Decide whether to use Claude for content moderation
  - ​Generate examples of content to moderate
- ​How to moderate content using Claude
  - ​Select the right Claude model
  - ​Build a strong prompt
  - ​Evaluate your prompt
  - ​Deploy your prompt

You want a cost-effective and rapid implementation

You desire both semantic understanding and quick decisions

You need consistent policy decisions

Your moderation policies are likely to change or evolve over time

You require interpretable reasoning for your moderation decisions

You need multilingual support without maintaining separate models

You require multimodal support

**Examples**:

```text
allowed_user_comments = [
    'This movie was great, I really enjoyed it. The main actor really killed it!',
    'I hate Mondays.',
    'It is a great time to invest in gold!'
]

disallowed_user_comments = [
    'Delete this post now or you better hide. I am coming after you and your family.',
    'Stay away from the 5G cellphones!! They are using 5G to control you.',
    'Congratulations! You have won a $1,000 gift card. Click here to claim your prize!'
]

# Sample user comments to test the con
...
```

```python
import anthropic
import json

# Initialize the Anthropic client
client = anthropic.Anthropic()

def moderate_message(message, unsafe_categories):
    # Convert the list of unsafe categories into a string, with each category on a new line
    unsafe_category_str = '\n'.join(unsafe_categories)
    
    # Construct the prompt for Claude, including the message and unsafe categories
    assessment_prompt = f"""
    Determine whether the following message warrants moderation, 
    based on the unsafe 
...
```

```python
import anthropic
import json

# Initialize the Anthropic client
client = anthropic.Anthropic()

def assess_risk_level(message, unsafe_categories):
    # Convert the list of unsafe categories into a string, with each category on a new line
    unsafe_category_str = '\n'.join(unsafe_categories)
    
    # Construct the prompt for Claude, including the message, unsafe categories, and risk level definitions
    assessment_prompt = f"""
    Assess the risk level of the following message warrants mode
...
```

---

## Count Message tokens

**URL**: https://docs.claude.com/en/api/messages-count-tokens

**Contents**:
    - Headers
    - Body
    - Response

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like beta1,beta2 or specify the header multiple times for each beta.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

Your unique API key for authentication.

This key is required in the header of all API requests, to authenticate your account and access Anthropic's services. Get your API key through the Console. Each key is scoped to a Workspace.

Our models are trained to operate on alternating user and assistant conversational turns. When creating a new Message, you specify the prior conversational turns with the messages parameter, and the model then generates the next Message in the conversation. Consecutive user or assistant turns in your request will be combined into a single turn.

Each input message must be an object with a role and content. You can specify a single user-role message, or you can include multiple user and assistant messages.

If the final message uses the assistant role, the response content will continue immediately from the content in that message. This can be used to constrain part of the model's response.

Example with a single user message:

Example with multiple conversational turns:

Example with a partially-filled response from Claude:

Each input message content may be either a single string or an array of content blocks, where each block has a specific type. Using a string for content is shorthand for an array of one content block of type "text". The following input messages are equivalent:

Note that if you want to include a system prompt, you can use the top-level system parameter — there is no "system" role for input messages in the Messages API.

There is a limit of 100,000 messages in a single request.

Show child attributes

The model that will complete your prompt.

See models for additional details and options.

"claude-sonnet-4-5-20250929"

Context mana

*[Content truncated - see full docs]*

**Examples**:

```text
[{"role": "user", "content": "Hello, Claude"}]
```

```text
[  {"role": "user", "content": "Hello there."},  {"role": "assistant", "content": "Hi, I'm Claude. How can I help you?"},  {"role": "user", "content": "Can you explain LLMs in plain English?"},]
```

```text
[  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},  {"role": "assistant", "content": "The best answer is ("},]
```

---

## Create Invite

**URL**: https://docs.claude.com/en/api/admin-api/invites/create-invite

**Contents**:
    - Headers
    - Body
    - Response

Your unique Admin API key for authentication.

This key is required in the header of all Admin API requests, to authenticate your account and access Anthropic's services. Get your Admin API key through the Console.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

Role for the invited User. Cannot be "admin".

Email of the User being invited.

RFC 3339 datetime string indicating when the Invite expires.

"2024-11-20T23:58:27.427722Z"

"invite_015gWxCN9Hfg2QhZwTK7Mdeu"

RFC 3339 datetime string indicating when the Invite was created.

"2024-10-30T23:58:27.427722Z"

Organization role of the User.

Status of the Invite.

For Invites, this is always "invite".

---

## Create Invite - Claude Docs

**URL**: https://docs.claude.com/en/api/admin-api/invites/create-invite

---

## Create Skill Version

**URL**: https://docs.claude.com/en/api/skills/create-skill-version

**Contents**:
    - Headers
    - Path Parameters
    - Body
    - Response

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like beta1,beta2 or specify the header multiple times for each beta.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

Your unique API key for authentication.

This key is required in the header of all API requests, to authenticate your account and access Anthropic's services. Get your API key through the Console. Each key is scoped to a Workspace.

Unique identifier for the skill.

The format and length of IDs may change over time.

Files to upload for the skill.

All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

ISO 8601 timestamp of when the skill version was created.

"2024-10-30T23:58:27.427722Z"

Description of the skill version.

This is extracted from the SKILL.md file in the skill upload.

"A custom skill for doing something useful"

Directory name of the skill version.

This is the top-level directory name that was extracted from the uploaded files.

Unique identifier for the skill version.

The format and length of IDs may change over time.

"skillver_01JAbcdefghijklmnopqrstuvw"

Human-readable name of the skill version.

This is extracted from the SKILL.md file in the skill upload.

Identifier for the skill that this version belongs to.

"skill_01JAbcdefghijklmnopqrstuvw"

For Skill Versions, this is always "skill_version".

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

---

## Create Skill

**URL**: https://docs.claude.com/en/api/skills/create-skill

**Contents**:
    - Headers
    - Body
    - Response

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like beta1,beta2 or specify the header multiple times for each beta.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

Your unique API key for authentication.

This key is required in the header of all API requests, to authenticate your account and access Anthropic's services. Get your API key through the Console. Each key is scoped to a Workspace.

Display title for the skill.

This is a human-readable label that is not included in the prompt sent to the model.

Files to upload for the skill.

All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

ISO 8601 timestamp of when the skill was created.

"2024-10-30T23:58:27.427722Z"

Display title for the skill.

This is a human-readable label that is not included in the prompt sent to the model.

Unique identifier for the skill.

The format and length of IDs may change over time.

"skill_01JAbcdefghijklmnopqrstuvw"

The latest version identifier for the skill.

This represents the most recent version of the skill that has been created.

This may be one of the following values:

For Skills, this is always "skill".

ISO 8601 timestamp of when the skill was last updated.

"2024-10-30T23:58:27.427722Z"

---

## Create Workspace

**URL**: https://docs.claude.com/en/api/admin-api/workspaces/create-workspace

**Contents**:
    - Headers
    - Body
    - Response

Your unique Admin API key for authentication.

This key is required in the header of all Admin API requests, to authenticate your account and access Anthropic's services. Get your Admin API key through the Console.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

Name of the Workspace.

RFC 3339 datetime string indicating when the Workspace was archived, or null if the Workspace is not archived.

"2024-11-01T23:59:27.427722Z"

RFC 3339 datetime string indicating when the Workspace was created.

"2024-10-30T23:58:27.427722Z"

Hex color code representing the Workspace in the Anthropic Console.

"wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"

Name of the Workspace.

For Workspaces, this is always "workspace".

---

## Create a File

**URL**: https://docs.claude.com/en/api/files-create

**Contents**:
    - Headers
    - Body
    - Response

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like beta1,beta2 or specify the header multiple times for each beta.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

Your unique API key for authentication.

This key is required in the header of all API requests, to authenticate your account and access Anthropic's services. Get your API key through the Console. Each key is scoped to a Workspace.

RFC 3339 datetime string representing when the file was created.

Original filename of the uploaded file.

Unique object identifier.

The format and length of IDs may change over time.

MIME type of the file.

Size of the file in bytes.

For files, this is always "file".

Whether the file can be downloaded.

---

## Create a Message Batch

**URL**: https://docs.claude.com/en/api/creating-message-batches

**Contents**:
- ​Feature Support
    - Headers
    - Body
    - Response

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like beta1,beta2 or specify the header multiple times for each beta.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

Your unique API key for authentication.

This key is required in the header of all API requests, to authenticate your account and access Anthropic's services. Get your API key through the Console. Each key is scoped to a Workspace.

List of requests for prompt completion. Each is an individual request to create a Message.

Show child attributes

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

"2024-08-20T18:37:24.100435Z"

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

"2024-08-20T18:37:24.100435Z"

RFC 3339 datetime string representing the time at which the Message Batch was created.

"2024-08-20T18:37:24.100435Z"

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

"2024-08-20T18:37:24.100435Z"

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

"2024-08-20T18:37:24.100435Z"

Unique object identifier.

The format and length of IDs may change over time.

"msgbatch_013Zva2CMHLNnXjNJJKqJ2EF"

Processing status of the Message Batch.

Tallies requests within the Message Batch, categorized by their status.

Requests start as processing and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

Show child attributes

URL to a .

*[Content truncated - see full docs]*

---

## Custom Tools

**URL**: https://docs.claude.com/en/api/agent-sdk/custom-tools

**Contents**:
- ​Creating Custom Tools
- ​Using Custom Tools
  - ​Tool Name Format
  - ​Configuring Allowed Tools
  - ​Multiple Tools Example
- ​Type Safety with Python
- ​Error Handling
- ​Example Tools

**Examples**:

```python
import { query, tool, createSdkMcpServer } from "@anthropic-ai/claude-agent-sdk";
import { z } from "zod";

// Create an SDK MCP server with custom tools
const customServer = createSdkMcpServer({
  name: "my-custom-tools",
  version: "1.0.0",
  tools: [
    tool(
      "get_weather",
      "Get current weather for a location",
      {
        location: z.string().describe("City name or coordinates"),
        units: z.enum(["celsius", "fahrenheit"]).default("celsius").describe("Temperature units"
...
```

```python
import { query } from "@anthropic-ai/claude-code";

// Use the custom tools in your query with streaming input
async function* generateMessages() {
  yield {
    type: "user" as const,
    message: {
      role: "user" as const,
      content: "What's the weather in San Francisco?"
    }
  };
}

for await (const message of query({
  prompt: generateMessages(),  // Use async generator for streaming input
  options: {
    mcpServers: {
      "my-custom-tools": customServer  // Pass as object/dicti
...
```

```javascript
const multiToolServer = createSdkMcpServer({
  name: "utilities",
  version: "1.0.0",
  tools: [
    tool("calculate", "Perform calculations", { /* ... */ }, async (args) => { /* ... */ }),
    tool("translate", "Translate text", { /* ... */ }, async (args) => { /* ... */ }),
    tool("search_web", "Search the web", { /* ... */ }, async (args) => { /* ... */ })
  ]
});

// Allow only specific tools with streaming input
async function* generateMessages() {
  yield {
    type: "user" as const,
   
...
```

---

## Delete Invite

**URL**: https://docs.claude.com/en/api/admin-api/invites/delete-invite

**Contents**:
    - Headers
    - Path Parameters
    - Response

Your unique Admin API key for authentication.

This key is required in the header of all Admin API requests, to authenticate your account and access Anthropic's services. Get your Admin API key through the Console.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

"invite_015gWxCN9Hfg2QhZwTK7Mdeu"

For Invites, this is always "invite_deleted".

---

## Delete Invite - Claude Docs

**URL**: https://docs.claude.com/en/api/admin-api/invites/delete-invite

---

## Delete Skill - Claude Docs

**URL**: https://docs.claude.com/en/api/skills/delete-skill

---

## Delete Skill Version

**URL**: https://docs.claude.com/en/api/skills/delete-skill-version

**Contents**:
    - Headers
    - Path Parameters
    - Response

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like beta1,beta2 or specify the header multiple times for each beta.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

Your unique API key for authentication.

This key is required in the header of all API requests, to authenticate your account and access Anthropic's services. Get your API key through the Console. Each key is scoped to a Workspace.

Unique identifier for the skill.

The format and length of IDs may change over time.

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

For Skill Versions, this is always "skill_version_deleted".

---

## Delete Skill

**URL**: https://docs.claude.com/en/api/skills/delete-skill

**Contents**:
    - Headers
    - Path Parameters
    - Response

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like beta1,beta2 or specify the header multiple times for each beta.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

Your unique API key for authentication.

This key is required in the header of all API requests, to authenticate your account and access Anthropic's services. Get your API key through the Console. Each key is scoped to a Workspace.

Unique identifier for the skill.

The format and length of IDs may change over time.

Unique identifier for the skill.

The format and length of IDs may change over time.

"skill_01JAbcdefghijklmnopqrstuvw"

For Skills, this is always "skill_deleted".

---

## Delete Workspace Member

**URL**: https://docs.claude.com/en/api/admin-api/workspace_members/delete-workspace-member

**Contents**:
    - Headers
    - Path Parameters
    - Response

Your unique Admin API key for authentication.

This key is required in the header of all Admin API requests, to authenticate your account and access Anthropic's services. Get your Admin API key through the Console.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

For Workspace Members, this is always "workspace_member_deleted".

"user_01WCz1FkmYMm4gnmykNKUu3Q"

"wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"

---

## Delete a File

**URL**: https://docs.claude.com/en/api/files-delete

**Contents**:
    - Headers
    - Path Parameters
    - Response

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like beta1,beta2 or specify the header multiple times for each beta.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

Your unique API key for authentication.

This key is required in the header of all API requests, to authenticate your account and access Anthropic's services. Get your API key through the Console. Each key is scoped to a Workspace.

ID of the deleted file.

For file deletion, this is always "file_deleted".

---

## Delete a Message Batch

**URL**: https://docs.claude.com/en/api/deleting-message-batches

**Contents**:
    - Headers
    - Path Parameters
    - Response

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like beta1,beta2 or specify the header multiple times for each beta.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

Your unique API key for authentication.

This key is required in the header of all API requests, to authenticate your account and access Anthropic's services. Get your API key through the Console. Each key is scoped to a Workspace.

ID of the Message Batch.

ID of the Message Batch.

"msgbatch_013Zva2CMHLNnXjNJJKqJ2EF"

For Message Batches, this is always "message_batch_deleted".

---

## Download a File

**URL**: https://docs.claude.com/en/api/files-content

**Contents**:
    - Headers
    - Path Parameters
    - Response

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like beta1,beta2 or specify the header multiple times for each beta.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

Your unique API key for authentication.

This key is required in the header of all API requests, to authenticate your account and access Anthropic's services. Get your API key through the Console. Each key is scoped to a Workspace.

The response is of type string.

---

## Errors - Claude Docs

**URL**: https://docs.claude.com/en/api/errors

---

## Errors

**URL**: https://docs.claude.com/en/api/errors

**Contents**:
- ​HTTP errors
- ​Request size limits
- ​Error shapes
- ​Request id
- ​Long requests

**Examples**:

```text
{
  "type": "error",
  "error": {
    "type": "not_found_error",
    "message": "The requested resource could not be found."
  },
  "request_id": "req_011CSHoEeqs5C35K2UUqR7Fy"
}
```

```text
import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude"}
    ]
)
print(f"Request ID: {message._request_id}")
```

---

## Files API

**URL**: https://docs.claude.com/en/docs/build-with-claude/files

**Contents**:
- ​Supported models
- ​How the Files API works
- ​How to use the Files API
  - ​Uploading a file
  - ​Using a file in messages
  - ​File types and content blocks
  - ​Working with other file formats
    - ​Document blocks

**Examples**:

```text
curl -X POST https://api.anthropic.com/v1/files \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: files-api-2025-04-14" \
  -F "file=@/path/to/document.pdf"
```

```text
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "type": "file",
  "filename": "document.pdf",
  "mime_type": "application/pdf",
  "size_bytes": 1024000,
  "created_at": "2025-01-01T00:00:00Z",
  "downloadable": false
}
```

```text
curl -X POST https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: files-api-2025-04-14" \
  -H "content-type: application/json" \
  -d '{
    "model": "claude-sonnet-4-5",
    "max_tokens": 1024,
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Please summarize this document for me."          
          },
          {
          
...
```

---

## Generate a prompt

**URL**: https://docs.claude.com/en/api/prompt-tools-generate

**Contents**:
- ​Before you begin
- ​Getting started with the prompt generator
- ​Generate a prompt
    - Headers
    - Body
    - Response

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like beta1,beta2 or specify the header multiple times for each beta.

Your unique API key for authentication.

This key is required in the header of all API requests, to authenticate your account and access Anthropic's services. Get your API key through the Console. Each key is scoped to a Workspace.

Description of the prompt's purpose.

The task parameter tells Claude what the prompt should do or what kind of role or functionality you want to create. This helps guide the prompt generation process toward your intended use case.

"a chef for a meal prep planning service"

The model this prompt will be used for. This optional parameter helps us understand which models our prompt tools are being used with, but it doesn't currently affect functionality.

"claude-3-7-sonnet-20250219"

The response contains a list of message objects in the same format used by the Messages API. Typically includes a user message with the complete generated prompt text, and may include an assistant message with a prefill to guide the model's initial response.

These messages can be used directly in a Messages API request to start a conversation with the generated prompt.

Show child attributes

Currently, the system field is always returned as an empty string (""). In future iterations, this field may contain generated system prompts.

Directions similar to what would normally be included in a system prompt are included in messages when generating a prompt.

Show child attributes

**Examples**:

```text
{"task": "a chef for a meal prep planning service"}
```

```text
"claude-3-7-sonnet-20250219"
```

```text
{  "messages": [    {      "role": "user",      "content": [        {          "type": "text",          "text": "You are a chef for a meal prep planning service..."        }      ]    },    {      "role": "assistant",      "content": [        {          "type": "text",          "text": "<recipe_planning>"        }      ]    }  ]}
```

---

## Get API Key

**URL**: https://docs.claude.com/en/api/admin-api/apikeys/get-api-key

**Contents**:
    - Headers
    - Path Parameters
    - Response

Your unique Admin API key for authentication.

This key is required in the header of all Admin API requests, to authenticate your account and access Anthropic's services. Get your Admin API key through the Console.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

RFC 3339 datetime string indicating when the API Key was created.

"2024-10-30T23:58:27.427722Z"

The ID and type of the actor that created the API key.

Show child attributes

"apikey_01Rj2N8SVvo6BePZj99NhmiT"

Partially redacted hint for the API key.

"sk-ant-api03-R2D...igAA"

Status of the API key.

For API Keys, this is always "api_key".

ID of the Workspace associated with the API key, or null if the API key belongs to the default Workspace.

"wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"

---

## Get Claude Code Usage Report - Claude Docs

**URL**: https://docs.claude.com/en/api/admin-api/claude-code/get-claude-code-usage-report

---

## Get Claude Code Usage Report

**URL**: https://docs.claude.com/en/api/admin-api/claude-code/get-claude-code-usage-report

**Contents**:
    - Headers
    - Query Parameters
    - Response

Your unique Admin API key for authentication.

This key is required in the header of all Admin API requests, to authenticate your account and access Anthropic's services. Get your Admin API key through the Console.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

UTC date in YYYY-MM-DD format. Returns metrics for this single day only.

Number of records per page (default: 20, max: 1000).

Opaque cursor token from previous response's next_page field.

List of Claude Code usage records for the requested date.

Show child attributes

True if there are more records available beyond the current page.

Opaque cursor token for fetching the next page of results, or null if no more pages are available.

"page_MjAyNS0wNS0xNFQwMDowMDowMFo="

---

## Get Cost Report

**URL**: https://docs.claude.com/en/api/admin-api/usage-cost/get-cost-report

**Contents**:
    - Headers
    - Query Parameters
    - Response

Your unique Admin API key for authentication.

This key is required in the header of all Admin API requests, to authenticate your account and access Anthropic's services. Get your Admin API key through the Console.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

Maximum number of time buckets to return in the response.

Optionally set to the next_page token from the previous response.

"page_MjAyNS0wNS0xNFQwMDowMDowMFo="

Time buckets that start on or after this RFC 3339 timestamp will be returned. Each time bucket will be snapped to the start of the minute/hour/day in UTC.

"2024-10-30T23:58:27.427722Z"

Time buckets that end before this RFC 3339 timestamp will be returned.

"2024-10-30T23:58:27.427722Z"

Group by any subset of the available options.

Show child attributes

Time granularity of the response data.

Show child attributes

Indicates if there are more results.

Token to provide in as page in the subsequent request to retrieve the next page of data.

"page_MjAyNS0wNS0xNFQwMDowMDowMFo="

---

## Get File Metadata

**URL**: https://docs.claude.com/en/api/files-metadata

**Contents**:
    - Headers
    - Path Parameters
    - Response

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like beta1,beta2 or specify the header multiple times for each beta.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

Your unique API key for authentication.

This key is required in the header of all API requests, to authenticate your account and access Anthropic's services. Get your API key through the Console. Each key is scoped to a Workspace.

RFC 3339 datetime string representing when the file was created.

Original filename of the uploaded file.

Unique object identifier.

The format and length of IDs may change over time.

MIME type of the file.

Size of the file in bytes.

For files, this is always "file".

Whether the file can be downloaded.

---

## Get Invite

**URL**: https://docs.claude.com/en/api/admin-api/invites/get-invite

**Contents**:
    - Headers
    - Path Parameters
    - Response

Your unique Admin API key for authentication.

This key is required in the header of all Admin API requests, to authenticate your account and access Anthropic's services. Get your Admin API key through the Console.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

Email of the User being invited.

RFC 3339 datetime string indicating when the Invite expires.

"2024-11-20T23:58:27.427722Z"

"invite_015gWxCN9Hfg2QhZwTK7Mdeu"

RFC 3339 datetime string indicating when the Invite was created.

"2024-10-30T23:58:27.427722Z"

Organization role of the User.

Status of the Invite.

For Invites, this is always "invite".

---

## Get Invite - Claude Docs

**URL**: https://docs.claude.com/en/api/admin-api/invites/get-invite

---

## Get Organization Info - Claude Docs

**URL**: https://docs.claude.com/en/api/admin-api/organization/get-me

---

## Get Organization Info

**URL**: https://docs.claude.com/en/api/admin-api/organization/get-me

**Contents**:
    - Headers
    - Response

Your unique Admin API key for authentication.

This key is required in the header of all Admin API requests, to authenticate your account and access Anthropic's services. Get your Admin API key through the Console.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

ID of the Organization.

"12345678-1234-5678-1234-567812345678"

Name of the Organization.

For Organizations, this is always "organization".

---

## Get Skill

**URL**: https://docs.claude.com/en/api/skills/get-skill

**Contents**:
    - Headers
    - Path Parameters
    - Response

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like beta1,beta2 or specify the header multiple times for each beta.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

Your unique API key for authentication.

This key is required in the header of all API requests, to authenticate your account and access Anthropic's services. Get your API key through the Console. Each key is scoped to a Workspace.

Unique identifier for the skill.

The format and length of IDs may change over time.

ISO 8601 timestamp of when the skill was created.

"2024-10-30T23:58:27.427722Z"

Display title for the skill.

This is a human-readable label that is not included in the prompt sent to the model.

Unique identifier for the skill.

The format and length of IDs may change over time.

"skill_01JAbcdefghijklmnopqrstuvw"

The latest version identifier for the skill.

This represents the most recent version of the skill that has been created.

This may be one of the following values:

For Skills, this is always "skill".

ISO 8601 timestamp of when the skill was last updated.

"2024-10-30T23:58:27.427722Z"

---

## Get Skill Version

**URL**: https://docs.claude.com/en/api/skills/get-skill-version

**Contents**:
    - Headers
    - Path Parameters
    - Response

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like beta1,beta2 or specify the header multiple times for each beta.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

Your unique API key for authentication.

This key is required in the header of all API requests, to authenticate your account and access Anthropic's services. Get your API key through the Console. Each key is scoped to a Workspace.

Unique identifier for the skill.

The format and length of IDs may change over time.

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

ISO 8601 timestamp of when the skill version was created.

"2024-10-30T23:58:27.427722Z"

Description of the skill version.

This is extracted from the SKILL.md file in the skill upload.

"A custom skill for doing something useful"

Directory name of the skill version.

This is the top-level directory name that was extracted from the uploaded files.

Unique identifier for the skill version.

The format and length of IDs may change over time.

"skillver_01JAbcdefghijklmnopqrstuvw"

Human-readable name of the skill version.

This is extracted from the SKILL.md file in the skill upload.

Identifier for the skill that this version belongs to.

"skill_01JAbcdefghijklmnopqrstuvw"

For Skill Versions, this is always "skill_version".

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

---

## Get Usage Report for the Messages API

**URL**: https://docs.claude.com/en/api/admin-api/usage-cost/get-messages-usage-report

**Contents**:
    - Headers
    - Query Parameters
    - Response

Your unique Admin API key for authentication.

This key is required in the header of all Admin API requests, to authenticate your account and access Anthropic's services. Get your Admin API key through the Console.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

Maximum number of time buckets to return in the response.

The default and max limits depend on bucket_width: • "1d": Default of 7 days, maximum of 31 days • "1h": Default of 24 hours, maximum of 168 hours • "1m": Default of 60 minutes, maximum of 1440 minutes

Optionally set to the next_page token from the previous response.

"page_MjAyNS0wNS0xNFQwMDowMDowMFo="

Time buckets that start on or after this RFC 3339 timestamp will be returned. Each time bucket will be snapped to the start of the minute/hour/day in UTC.

"2024-10-30T23:58:27.427722Z"

Time buckets that end before this RFC 3339 timestamp will be returned.

"2024-10-30T23:58:27.427722Z"

Restrict usage returned to the specified API key ID(s).

"apikey_01Rj2N8SVvo6BePZj99NhmiT"

Restrict usage returned to the specified workspace ID(s).

"wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"

Restrict usage returned to the specified model(s).

"claude-sonnet-4-20250514"

"claude-3-5-haiku-20241022"

Restrict usage returned to the specified service tier(s).

Show child attributes

Restrict usage returned to the specified context window(s).

Show child attributes

Group by any subset of the available options.

Show child attributes

Time granularity of the response data.

Show child attributes

Indicates if there are more results.

Token to provide in as page in the subsequent request to retrieve the next page of data.

"page_MjAyNS0wNS0xNFQwMDowMDowMFo="

---

## Get User

**URL**: https://docs.claude.com/en/api/admin-api/users/get-user

**Contents**:
    - Headers
    - Path Parameters
    - Response

Your unique Admin API key for authentication.

This key is required in the header of all Admin API requests, to authenticate your account and access Anthropic's services. Get your Admin API key through the Console.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

RFC 3339 datetime string indicating when the User joined the Organization.

"2024-10-30T23:58:27.427722Z"

"user_01WCz1FkmYMm4gnmykNKUu3Q"

Organization role of the User.

For Users, this is always "user".

---

## Get Workspace Member

**URL**: https://docs.claude.com/en/api/admin-api/workspace_members/get-workspace-member

**Contents**:
    - Headers
    - Path Parameters
    - Response

Your unique Admin API key for authentication.

This key is required in the header of all Admin API requests, to authenticate your account and access Anthropic's services. Get your Admin API key through the Console.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

For Workspace Members, this is always "workspace_member".

"user_01WCz1FkmYMm4gnmykNKUu3Q"

"wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"

Role of the Workspace Member.

---

## Get Workspace

**URL**: https://docs.claude.com/en/api/admin-api/workspaces/get-workspace

**Contents**:
    - Headers
    - Path Parameters
    - Response

Your unique Admin API key for authentication.

This key is required in the header of all Admin API requests, to authenticate your account and access Anthropic's services. Get your Admin API key through the Console.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

RFC 3339 datetime string indicating when the Workspace was archived, or null if the Workspace is not archived.

"2024-11-01T23:59:27.427722Z"

RFC 3339 datetime string indicating when the Workspace was created.

"2024-10-30T23:58:27.427722Z"

Hex color code representing the Workspace in the Anthropic Console.

"wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"

Name of the Workspace.

For Workspaces, this is always "workspace".

---

## Get a Model

**URL**: https://docs.claude.com/en/api/models

**Contents**:
    - Headers
    - Path Parameters
    - Response

The version of the Claude API you want to use.

Read more about versioning and our version history here.

Your unique API key for authentication.

This key is required in the header of all API requests, to authenticate your account and access Anthropic's services. Get your API key through the Console. Each key is scoped to a Workspace.

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like beta1,beta2 or specify the header multiple times for each beta.

Model identifier or alias.

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

"2025-02-19T00:00:00Z"

A human-readable name for the model.

Unique model identifier.

"claude-sonnet-4-20250514"

For Models, this is always "model".

---

## Getting help

**URL**: https://docs.claude.com/en/api/getting-help

---

## Getting help - Claude Docs

**URL**: https://docs.claude.com/en/api/getting-help

---

## Google Sheets add-on

**URL**: https://docs.claude.com/en/docs/agents-and-tools/claude-for-sheets

**Contents**:
- ​Why use Claude for Sheets?
- ​Get started with Claude for Sheets
  - ​Install Claude for Sheets
  - ​Enter your first prompt
- ​Advanced use
  - ​Optional function parameters
- ​Claude for Sheets usage examples
  - ​Prompt engineering interactive tutorial

Get your Claude API key

Install the Claude for Sheets extension

Example multiturn CLAUDEMESSAGES() call with system prompt

Example: Setting parameters

NAME? Error: Unknown function: 'claude'

#ERROR!, ⚠ DEFERRED ⚠ or ⚠ THROTTLED ⚠

**Examples**:

```text
=CLAUDEMESSAGES("User: In one sentence, what is good about the color blue?
Assistant: The color blue is great because")
```

```text
=CLAUDEMESSAGES("User: What's your favorite flower? Answer in <answer> tags.
Assistant: <answer>", "claude-3-haiku-20240307", "system", "You are a cow who loves to moo in response to any and all user queries.")`
```

```text
=CLAUDE("Hi, Claude!", "claude-3-haiku-20240307", "system", "Repeat exactly what the user says.", "max_tokens", 100, "temperature", 0.1)
```

---

## Handling Permissions

**URL**: https://docs.claude.com/en/api/agent-sdk/permissions

**Contents**:
- ​SDK Permissions
- ​Overview
- ​Permission Flow Diagram
- ​Permission Modes
  - ​Available Modes
  - ​Setting Permission Mode
    - ​1. Initial Configuration
    - ​2. Dynamic Mode Changes (Streaming Only)

**Examples**:

```python
import { query } from "@anthropic-ai/claude-agent-sdk";

const result = await query({
  prompt: "Help me refactor this code",
  options: {
    permissionMode: 'default'  // Standard permission mode
  }
});
```

```python
import { query } from "@anthropic-ai/claude-agent-sdk";

// Create an async generator for streaming input
async function* streamInput() {
  yield { 
    type: 'user',
    message: { 
      role: 'user', 
      content: "Let's start with default permissions" 
    }
  };
  
  // Later in the conversation...
  yield {
    type: 'user',
    message: {
      role: 'user',
      content: "Now let's speed up development"
    }
  };
}

const q = query({
  prompt: streamInput(),
  options: {
    permissi
...
```

```text
// Start in default mode for controlled execution
permissionMode: 'default'

// Switch to acceptEdits for rapid iteration
await q.setPermissionMode('acceptEdits')
```

---

## Handling stop reasons

**URL**: https://docs.claude.com/en/api/handling-stop-reasons

**Contents**:
- ​What is stop_reason?
- ​Stop reason values
  - ​end_turn
    - ​Empty responses with end_turn
  - ​max_tokens
  - ​stop_sequence
  - ​tool_use
  - ​pause_turn

**Examples**:

```text
{
  "id": "msg_01234",
  "type": "message",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "Here's the answer to your question..."
    }
  ],
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "usage": {
    "input_tokens": 100,
    "output_tokens": 50
  }
}
```

```text
if response.stop_reason == "end_turn":
    # Process the complete response
    print(response.content[0].text)
```

```python
# INCORRECT: Adding text immediately after tool_result
messages = [
    {"role": "user", "content": "Calculate the sum of 1234 and 5678"},
    {"role": "assistant", "content": [
        {
            "type": "tool_use",
            "id": "toolu_123",
            "name": "calculator",
            "input": {"operation": "add", "a": 1234, "b": 5678}
        }
    ]},
    {"role": "user", "content": [
        {
            "type": "tool_result",
            "tool_use_id": "toolu_123",
            "c
...
```

---

## Hosting the Agent SDK

**URL**: https://docs.claude.com/en/api/agent-sdk/hosting

**Contents**:
- ​Hosting Requirements
  - ​Container-Based Sandboxing
  - ​System Requirements
- ​Understanding the SDK Architecture
- ​Sandbox Provider Options
- ​Production Deployment Patterns
  - ​Pattern 1: Ephemeral Sessions
  - ​Pattern 2: Long-Running Sessions

---

## IP addresses

**URL**: https://docs.claude.com/en/api/ip-addresses

**Contents**:
- ​Inbound IP addresses
    - ​IPv4
    - ​IPv6
- ​Outbound IP addresses
    - ​IPv4

**Examples**:

```text
34.162.46.92
34.162.102.82
34.162.136.91
34.162.142.92
34.162.183.95
```

---

## Improve a prompt

**URL**: https://docs.claude.com/en/api/prompt-tools-improve

**Contents**:
- ​Before you begin
- ​Getting started with the prompt improver
- ​Improve a prompt
    - Headers
    - Body
    - Response

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like beta1,beta2 or specify the header multiple times for each beta.

Your unique API key for authentication.

This key is required in the header of all API requests, to authenticate your account and access Anthropic's services. Get your API key through the Console. Each key is scoped to a Workspace.

The prompt to improve, structured as a list of message objects.

Each message in the messages array must:

As a simple text prompt:

With example interactions to guide improvement:

Note that only contiguous user messages with text content are allowed. Assistant prefill is permitted, but other content types will cause validation errors.

Show child attributes

Feedback for improving the prompt.

Use this parameter to share specific guidance on what aspects of the prompt should be enhanced or modified.

When not set, the API will improve the prompt using general prompt engineering best practices.

"Make it more detailed and include cooking times"

The existing system prompt to incorporate, if any.

Note that while system prompts typically appear as separate parameters in standard API calls, in the improve_prompt response, the system content will be incorporated directly into the returned user message.

"You are a professional chef"

The model this prompt will be used for. This optional parameter helps us understand which models our prompt tools are being used with, but it doesn't currently affect functionality.

"claude-3-7-sonnet-20250219"

Contains the result of the prompt improvement process in a list of message objects.

Includes a user-role message with the improved prompt text and may optionally include an assistant-role message with a prefill. These messages follow the standard Messages API format and can be used directly in subsequent API calls.

Show child attributes

Currently, the system field is always returned as an empty string (""). In future

*[Content truncated - see full docs]*

**Examples**:

```text
[  {    "role": "user",     "content": [      {        "type": "text",        "text": "Concise recipe for {{food}}"      }    ]  }]
```

```text
[  {    "role": "user",     "content": [      {        "type": "text",        "text": "Concise for {{food}}.\n\nexample\mandu: Put the mandu in the air fryer at 380F for 7 minutes."      }    ]  }]
```

```text
[  {    "content": [      {        "text": "<generated prompt>",        "type": "text"      }    ],    "role": "user"  }]
```

---

## List API Keys

**URL**: https://docs.claude.com/en/api/admin-api/apikeys/list-api-keys

**Contents**:
    - Headers
    - Query Parameters
    - Response

Your unique Admin API key for authentication.

This key is required in the header of all Admin API requests, to authenticate your account and access Anthropic's services. Get your Admin API key through the Console.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

Number of items to return per page.

Defaults to 20. Ranges from 1 to 1000.

Filter by API key status.

Filter by Workspace ID.

Filter by the ID of the User who created the object.

Show child attributes

First ID in the data list. Can be used as the before_id for the previous page.

Indicates if there are more results in the requested page direction.

Last ID in the data list. Can be used as the after_id for the next page.

---

## List API Keys - Claude Docs

**URL**: https://docs.claude.com/en/api/admin-api/apikeys/list-api-keys

---

## List Files

**URL**: https://docs.claude.com/en/api/files-list

**Contents**:
    - Headers
    - Query Parameters
    - Response

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like beta1,beta2 or specify the header multiple times for each beta.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

Your unique API key for authentication.

This key is required in the header of all API requests, to authenticate your account and access Anthropic's services. Get your API key through the Console. Each key is scoped to a Workspace.

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

Number of items to return per page.

Defaults to 20. Ranges from 1 to 1000.

List of file metadata objects.

Show child attributes

ID of the first file in this page of results.

Whether there are more results available.

ID of the last file in this page of results.

---

## List Invites

**URL**: https://docs.claude.com/en/api/admin-api/invites/list-invites

**Contents**:
    - Headers
    - Query Parameters
    - Response

Your unique Admin API key for authentication.

This key is required in the header of all Admin API requests, to authenticate your account and access Anthropic's services. Get your Admin API key through the Console.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

Number of items to return per page.

Defaults to 20. Ranges from 1 to 1000.

Show child attributes

First ID in the data list. Can be used as the before_id for the previous page.

Indicates if there are more results in the requested page direction.

Last ID in the data list. Can be used as the after_id for the next page.

---

## List Message Batches

**URL**: https://docs.claude.com/en/api/listing-message-batches

**Contents**:
    - Headers
    - Query Parameters
    - Response

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like beta1,beta2 or specify the header multiple times for each beta.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

Your unique API key for authentication.

This key is required in the header of all API requests, to authenticate your account and access Anthropic's services. Get your API key through the Console. Each key is scoped to a Workspace.

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

Number of items to return per page.

Defaults to 20. Ranges from 1 to 1000.

Show child attributes

First ID in the data list. Can be used as the before_id for the previous page.

Indicates if there are more results in the requested page direction.

Last ID in the data list. Can be used as the after_id for the next page.

---

## List Models

**URL**: https://docs.claude.com/en/api/models-list

**Contents**:
    - Headers
    - Query Parameters
    - Response

The version of the Claude API you want to use.

Read more about versioning and our version history here.

Your unique API key for authentication.

This key is required in the header of all API requests, to authenticate your account and access Anthropic's services. Get your API key through the Console. Each key is scoped to a Workspace.

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like beta1,beta2 or specify the header multiple times for each beta.

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

Number of items to return per page.

Defaults to 20. Ranges from 1 to 1000.

Show child attributes

First ID in the data list. Can be used as the before_id for the previous page.

Indicates if there are more results in the requested page direction.

Last ID in the data list. Can be used as the after_id for the next page.

---

## List Skill Versions - Claude Docs

**URL**: https://docs.claude.com/en/api/skills/list-skill-versions

---

## List Skill Versions

**URL**: https://docs.claude.com/en/api/skills/list-skill-versions

**Contents**:
    - Headers
    - Path Parameters
    - Query Parameters
    - Response

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like beta1,beta2 or specify the header multiple times for each beta.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

Your unique API key for authentication.

This key is required in the header of all API requests, to authenticate your account and access Anthropic's services. Get your API key through the Console. Each key is scoped to a Workspace.

Unique identifier for the skill.

The format and length of IDs may change over time.

Optionally set to the next_page token from the previous response.

Number of items to return per page.

Defaults to 20. Ranges from 1 to 1000.

List of skill versions.

Show child attributes

Indicates if there are more results in the requested page direction.

Token to provide in as page in the subsequent request to retrieve the next page of data.

"page_MjAyNS0wNS0xNFQwMDowMDowMFo="

---

## List Skills

**URL**: https://docs.claude.com/en/api/skills/list-skills

**Contents**:
    - Headers
    - Query Parameters
    - Response

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like beta1,beta2 or specify the header multiple times for each beta.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

Your unique API key for authentication.

This key is required in the header of all API requests, to authenticate your account and access Anthropic's services. Get your API key through the Console. Each key is scoped to a Workspace.

Pagination token for fetching a specific page of results.

Pass the value from a previous response's next_page field to get the next page of results.

Number of results to return per page.

Maximum value is 100. Defaults to 20.

Filter skills by source.

If provided, only skills from the specified source will be returned:

Show child attributes

Whether there are more results available.

If true, there are additional results that can be fetched using the next_page token.

Token for fetching the next page of results.

If null, there are no more results available. Pass this value to the page_token parameter in the next request to get the next page.

"page_MjAyNS0wNS0xNFQwMDowMDowMFo="

---

## List Users

**URL**: https://docs.claude.com/en/api/admin-api/users/list-users

**Contents**:
    - Headers
    - Query Parameters
    - Response

Your unique Admin API key for authentication.

This key is required in the header of all Admin API requests, to authenticate your account and access Anthropic's services. Get your Admin API key through the Console.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

Number of items to return per page.

Defaults to 20. Ranges from 1 to 1000.

Filter by user email.

Show child attributes

First ID in the data list. Can be used as the before_id for the previous page.

Indicates if there are more results in the requested page direction.

Last ID in the data list. Can be used as the after_id for the next page.

---

## List Workspace Members

**URL**: https://docs.claude.com/en/api/admin-api/workspace_members/list-workspace-members

**Contents**:
    - Headers
    - Path Parameters
    - Query Parameters
    - Response

Your unique Admin API key for authentication.

This key is required in the header of all Admin API requests, to authenticate your account and access Anthropic's services. Get your Admin API key through the Console.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

Number of items to return per page.

Defaults to 20. Ranges from 1 to 1000.

Show child attributes

First ID in the data list. Can be used as the before_id for the previous page.

Indicates if there are more results in the requested page direction.

Last ID in the data list. Can be used as the after_id for the next page.

---

## List Workspaces

**URL**: https://docs.claude.com/en/api/admin-api/workspaces/list-workspaces

**Contents**:
    - Headers
    - Query Parameters
    - Response

Your unique Admin API key for authentication.

This key is required in the header of all Admin API requests, to authenticate your account and access Anthropic's services. Get your Admin API key through the Console.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

Whether to include Workspaces that have been archived in the response

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

Number of items to return per page.

Defaults to 20. Ranges from 1 to 1000.

Show child attributes

First ID in the data list. Can be used as the before_id for the previous page.

Indicates if there are more results in the requested page direction.

Last ID in the data list. Can be used as the after_id for the next page.

---

## MCP in the SDK

**URL**: https://docs.claude.com/en/api/agent-sdk/mcp

**Contents**:
- ​Overview
- ​Configuration
  - ​Basic Configuration
  - ​Using MCP Servers in SDK
- ​Transport Types
  - ​stdio Servers
  - ​HTTP/SSE Servers
  - ​SDK MCP Servers

**Examples**:

```text
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-filesystem"],
      "env": {
        "ALLOWED_PATHS": "/Users/me/projects"
      }
    }
  }
}
```

```python
import { query } from "@anthropic-ai/claude-agent-sdk";

for await (const message of query({
  prompt: "List files in my project",
  options: {
    mcpServers: {
      "filesystem": {
        command: "npx",
        args: ["@modelcontextprotocol/server-filesystem"],
        env: {
          ALLOWED_PATHS: "/Users/me/projects"
        }
      }
    },
    allowedTools: ["mcp__filesystem__list_files"]
  }
})) {
  if (message.type === "result" && message.subtype === "success") {
    console.log(mes
...
```

```text
// .mcp.json configuration
{
  "mcpServers": {
    "my-tool": {
      "command": "node",
      "args": ["./my-mcp-server.js"],
      "env": {
        "DEBUG": "${DEBUG:-false}"
      }
    }
  }
}
```

---

## Message Batches examples

**URL**: https://docs.claude.com/en/api/messages-batch-examples

**Contents**:
- ​Creating a Message Batch
- ​Polling for Message Batch completion
- ​Listing all Message Batches in a Workspace
- ​Retrieving Message Batch Results
- ​Canceling a Message Batch

**Examples**:

```python
import anthropic
from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
from anthropic.types.messages.batch_create_params import Request

client = anthropic.Anthropic()

message_batch = client.messages.batches.create(
    requests=[
        Request(
            custom_id="my-first-request",
            params=MessageCreateParamsNonStreaming(
                model="claude-sonnet-4-5",
                max_tokens=1024,
                messages=[{
                    "role
...
```

```text
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch",
  "processing_status": "in_progress",
  "request_counts": {
    "processing": 2,
    "succeeded": 0,
    "errored": 0,
    "canceled": 0,
    "expired": 0
  },
  "ended_at": null,
  "created_at": "2024-09-24T18:37:24.100435Z",
  "expires_at": "2024-09-25T18:37:24.100435Z",
  "cancel_initiated_at": null,
  "results_url": null
}
```

```text
import anthropic

client = anthropic.Anthropic()

message_batch = None
while True:
    message_batch = client.messages.batches.retrieve(
        MESSAGE_BATCH_ID
    )
    if message_batch.processing_status == "ended":
        break
              
    print(f"Batch {MESSAGE_BATCH_ID} is still processing...")
    time.sleep(60)
print(message_batch)
```

---

## Messages

**URL**: https://docs.claude.com/en/api/messages

**Contents**:
    - Headers
    - Body
    - Response

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like beta1,beta2 or specify the header multiple times for each beta.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

Your unique API key for authentication.

This key is required in the header of all API requests, to authenticate your account and access Anthropic's services. Get your API key through the Console. Each key is scoped to a Workspace.

The model that will complete your prompt.

See models for additional details and options.

"claude-sonnet-4-5-20250929"

Our models are trained to operate on alternating user and assistant conversational turns. When creating a new Message, you specify the prior conversational turns with the messages parameter, and the model then generates the next Message in the conversation. Consecutive user or assistant turns in your request will be combined into a single turn.

Each input message must be an object with a role and content. You can specify a single user-role message, or you can include multiple user and assistant messages.

If the final message uses the assistant role, the response content will continue immediately from the content in that message. This can be used to constrain part of the model's response.

Example with a single user message:

Example with multiple conversational turns:

Example with a partially-filled response from Claude:

Each input message content may be either a single string or an array of content blocks, where each block has a specific type. Using a string for content is shorthand for an array of one content block of type "text". The following input messages are equivalent:

Note that if you want to include a system prompt, you can use the top-level system parameter — there is no "system" role for input messages in the Messages API.

There is a limit of 100,000 messages in a single request.

Show child attributes

The maximum 

*[Content truncated - see full docs]*

**Examples**:

```text
[{"role": "user", "content": "Hello, Claude"}]
```

```text
[  {"role": "user", "content": "Hello there."},  {"role": "assistant", "content": "Hi, I'm Claude. How can I help you?"},  {"role": "user", "content": "Can you explain LLMs in plain English?"},]
```

```text
[  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},  {"role": "assistant", "content": "The best answer is ("},]
```

---

## Messages examples

**URL**: https://docs.claude.com/en/api/messages-examples

**Contents**:
- ​Basic request and response
- ​Multiple conversational turns
- ​Putting words in Claude’s mouth
- ​Vision
- ​Tool use, JSON mode, and computer use

**Examples**:

```text
#!/bin/sh
curl https://api.anthropic.com/v1/messages \
     --header "x-api-key: $ANTHROPIC_API_KEY" \
     --header "anthropic-version: 2023-06-01" \
     --header "content-type: application/json" \
     --data \
'{
    "model": "claude-sonnet-4-5",
    "max_tokens": 1024,
    "messages": [
        {"role": "user", "content": "Hello, Claude"}
    ]
}'
```

```text
{
  "id": "msg_01XFDUDYJgAACzvnptvVoYEL",
  "type": "message",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "Hello!"
    }
  ],
  "model": "claude-sonnet-4-5",
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "usage": {
    "input_tokens": 12,
    "output_tokens": 6
  }
}
```

```text
#!/bin/sh
curl https://api.anthropic.com/v1/messages \
     --header "x-api-key: $ANTHROPIC_API_KEY" \
     --header "anthropic-version: 2023-06-01" \
     --header "content-type: application/json" \
     --data \
'{
    "model": "claude-sonnet-4-5",
    "max_tokens": 1024,
    "messages": [
        {"role": "user", "content": "Hello, Claude"},
        {"role": "assistant", "content": "Hello!"},
        {"role": "user", "content": "Can you describe LLMs to me?"}

    ]
}'
```

---

## Migrating from Text Completions

**URL**: https://docs.claude.com/en/api/migrating-from-text-completions-to-messages

**Contents**:
  - ​Inputs and outputs
  - ​Putting words in Claude’s mouth
  - ​System prompt
  - ​Model names
  - ​Stop reason
  - ​Specifying max tokens
  - ​Streaming format

**Examples**:

```text
prompt = "\n\nHuman: Hello there\n\nAssistant: Hi, I'm Claude. How can I help?\n\nHuman: Can you explain Glycolysis to me?\n\nAssistant:"
```

```text
messages = [
  {"role": "user", "content": "Hello there."},
  {"role": "assistant", "content": "Hi, I'm Claude. How can I help?"},
  {"role": "user", "content": "Can you explain Glycolysis to me?"},
]
```

```text
>>> response = anthropic.completions.create(...)
>>> response.completion
" Hi, I'm Claude"
```

---

## Migrating to Claude 4.5

**URL**: https://docs.claude.com/en/docs/about-claude/models/migrating-to-claude-4

**Contents**:
- ​Migrating from Claude Sonnet 3.7 to Claude Sonnet 4.5
  - ​Migration steps
  - ​Sonnet 3.7 → 4.5 migration checklist
  - ​Features removed from Claude Sonnet 3.7
- ​Migrating from Claude Haiku 3.5 to Claude Haiku 4.5
  - ​Migration steps
  - ​Haiku 3.5 → 4.5 migration checklist
- ​Choosing between Sonnet 4.5 and Haiku 4.5

**Examples**:

```text
# Before (Claude Sonnet 3.7)
model="claude-3-7-sonnet-20250219"

# After (Claude Sonnet 4.5)
model="claude-sonnet-4-5-20250929"
```

```text
# Before (Claude Sonnet 3.7) - This will error in Sonnet 4.5
response = client.messages.create(
    model="claude-3-7-sonnet-20250219",
    temperature=0.7,
    top_p=0.9,  # Cannot use both
    ...
)

# After (Claude Sonnet 4.5)
response = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    temperature=0.7,  # Use temperature OR top_p, not both
    ...
)
```

```text
response = client.messages.create(...)

if response.stop_reason == "refusal":
    # Handle refusal appropriately
    pass
```

---

## Modifying system prompts

**URL**: https://docs.claude.com/en/api/agent-sdk/modifying-system-prompts

**Contents**:
- ​Understanding system prompts
- ​Methods of modification
  - ​Method 1: CLAUDE.md files (project-level instructions)
    - ​How CLAUDE.md works with the SDK
    - ​Example CLAUDE.md
    - ​Using CLAUDE.md with the SDK
    - ​When to use CLAUDE.md
  - ​Method 2: Output styles (persistent configurations)

**Examples**:

```javascript
# Project Guidelines

## Code Style

- Use TypeScript strict mode
- Prefer functional components in React
- Always include JSDoc comments for public APIs

## Testing

- Run `npm test` before committing
- Maintain >80% code coverage
- Use jest for unit tests, playwright for E2E

## Commands

- Build: `npm run build`
- Dev server: `npm run dev`
- Type check: `npm run typecheck`
```

```python
import { query } from "@anthropic-ai/claude-agent-sdk";

// IMPORTANT: You must specify settingSources to load CLAUDE.md
// The claude_code preset alone does NOT load CLAUDE.md files
const messages = [];

for await (const message of query({
  prompt: "Add a new React component for user profiles",
  options: {
    systemPrompt: {
      type: "preset",
      preset: "claude_code", // Use Claude Code's system prompt
    },
    settingSources: ["project"], // Required to load CLAUDE.md from project

...
```

```python
import { writeFile, mkdir } from "fs/promises";
import { join } from "path";
import { homedir } from "os";

async function createOutputStyle(
  name: string,
  description: string,
  prompt: string
) {
  // User-level: ~/.claude/output-styles
  // Project-level: .claude/output-styles
  const outputStylesDir = join(homedir(), ".claude", "output-styles");

  await mkdir(outputStylesDir, { recursive: true });

  const content = `---
name: ${name}
description: ${description}
---

${prompt}`;

  cons
...
```

---

## OpenAI SDK compatibility

**URL**: https://docs.claude.com/en/api/openai-sdk

**Contents**:
- ​Getting started with the OpenAI SDK
  - ​Quick start example
- ​Important OpenAI compatibility limitations
    - ​API behavior
    - ​Output quality considerations
    - ​System / Developer message hoisting
    - ​Extended thinking support
- ​Rate limits

**Examples**:

```python
from openai import OpenAI

client = OpenAI(
    api_key="ANTHROPIC_API_KEY",  # Your Claude API key
    base_url="https://api.anthropic.com/v1/"  # the Claude API endpoint
)

response = client.chat.completions.create(
    model="claude-sonnet-4-5", # Anthropic model name
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who are you?"}
    ],
)

print(response.choices[0].message.content)
```

```text
response = client.chat.completions.create(
    model="claude-sonnet-4-5",
    messages=...,
    extra_body={
        "thinking": { "type": "enabled", "budget_tokens": 2000 }
    }
)
```

---

## Prompt caching

**URL**: https://docs.claude.com/en/docs/build-with-claude/prompt-caching

**Contents**:
- ​How prompt caching works
- ​Pricing
- ​How to implement prompt caching
  - ​Supported models
  - ​Structuring your prompt
    - ​How automatic prefix checking works
    - ​When to use multiple breakpoints
  - ​Cache limitations

Large context caching example

Caching tool definitions

Continuing a multi-turn conversation

Putting it all together: Multiple cache breakpoints

Do I need multiple cache breakpoints or is one at the end sufficient?

Do cache breakpoints add extra cost?

What is the cache lifetime?

How many cache breakpoints can I use?

Is prompt caching available for all models?

How does prompt caching work with extended thinking?

How do I enable prompt caching?

Can I use prompt caching with other API features?

How does prompt caching affect pricing?

Can I manually clear the cache?

How can I track the effectiveness of my caching strategy?

What can break the cache?

How does prompt caching handle privacy and data separation?

Can I use prompt caching with the Batches API?

Why am I seeing the error `AttributeError: 'Beta' object has no attribute 'prompt_caching'` in Python?

Why am I seeing 'TypeError: Cannot read properties of undefined (reading 'messages')'?

**Examples**:

```text
curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-sonnet-4-5",
    "max_tokens": 1024,
    "system": [
      {
        "type": "text",
        "text": "You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.\n"
      },
      {
        "type": "text",
        "tex
...
```

```text
{"cache_creation_input_tokens":188086,"cache_read_input_tokens":0,"input_tokens":21,"output_tokens":393}
{"cache_creation_input_tokens":0,"cache_read_input_tokens":188086,"input_tokens":21,"output_tokens":393}
```

```text
Request 1: User: "What's the weather in Paris?"
Response: [thinking_block_1] + [tool_use block 1]

Request 2:
User: ["What's the weather in Paris?"],
Assistant: [thinking_block_1] + [tool_use block 1],
User: [tool_result_1, cache=True]
Response: [thinking_block_2] + [text block 2]
# Request 2 caches its request content (not the response)
# The cache includes: user message, thinking_block_1, tool_use block 1, and tool_result_1

Request 3:
User: ["What's the weather in Paris?"],
Assistant: [thinki
...
```

---

## Rate limits

**URL**: https://docs.claude.com/en/api/rate-limits

**Contents**:
- ​About our limits
- ​Spend limits
  - ​Requirements to advance tier
- ​Rate limits
  - ​Cache-aware ITPM
  - ​Message Batches API
  - ​Long context rate limits
  - ​Monitoring your rate limits in the Console

---

## Remove User

**URL**: https://docs.claude.com/en/api/admin-api/users/remove-user

**Contents**:
    - Headers
    - Path Parameters
    - Response

Your unique Admin API key for authentication.

This key is required in the header of all Admin API requests, to authenticate your account and access Anthropic's services. Get your Admin API key through the Console.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

"user_01WCz1FkmYMm4gnmykNKUu3Q"

For Users, this is always "user_deleted".

---

## Retrieve Message Batch Results

**URL**: https://docs.claude.com/en/api/retrieving-message-batch-results

**Contents**:
    - Headers
    - Path Parameters
    - Response

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like beta1,beta2 or specify the header multiple times for each beta.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

Your unique API key for authentication.

This key is required in the header of all API requests, to authenticate your account and access Anthropic's services. Get your API key through the Console. Each key is scoped to a Workspace.

ID of the Message Batch.

This is a single line in the response .jsonl file and does not represent the response as a whole.

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Show child attributes

**Examples**:

```javascript
{"custom_id":"my-second-request","result":{"type":"succeeded","message":{"id":"msg_014VwiXbi91y3JMjcpyGBHX5","type":"message","role":"assistant","model":"claude-3-5-sonnet-20240620","content":[{"type":"text","text":"Hello again! It's nice to see you. How can I assist you today? Is there anything specific you'd like to chat about or any questions you have?"}],"stop_reason":"end_turn","stop_sequence":null,"usage":{"input_tokens":11,"output_tokens":36}}}}
{"custom_id":"my-first-request","result":{"
...
```

---

## Retrieve a Message Batch

**URL**: https://docs.claude.com/en/api/retrieving-message-batches

**Contents**:
    - Headers
    - Path Parameters
    - Response

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like beta1,beta2 or specify the header multiple times for each beta.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

Your unique API key for authentication.

This key is required in the header of all API requests, to authenticate your account and access Anthropic's services. Get your API key through the Console. Each key is scoped to a Workspace.

ID of the Message Batch.

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

"2024-08-20T18:37:24.100435Z"

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

"2024-08-20T18:37:24.100435Z"

RFC 3339 datetime string representing the time at which the Message Batch was created.

"2024-08-20T18:37:24.100435Z"

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

"2024-08-20T18:37:24.100435Z"

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

"2024-08-20T18:37:24.100435Z"

Unique object identifier.

The format and length of IDs may change over time.

"msgbatch_013Zva2CMHLNnXjNJJKqJ2EF"

Processing status of the Message Batch.

Tallies requests within the Message Batch, categorized by their status.

Requests start as processing and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

Show child attributes

URL to a .jsonl file containing the results of the Message Batch requests. Specified only once proc

*[Content truncated - see full docs]*

---

## Service tiers

**URL**: https://docs.claude.com/en/api/service-tiers

**Contents**:
- ​Standard Tier
- ​Priority Tier
- ​How requests get assigned tiers
- ​Using service tiers
- ​Get started with Priority Tier
  - ​Supported models
  - ​How to access Priority Tier

**Examples**:

```text
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude!"}],
    service_tier="auto"  # Automatically use Priority Tier when available, fallback to standard
)
```

```text
{
  "usage": {
    "input_tokens": 410,
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0,
    "output_tokens": 585,
    "service_tier": "priority"
  }
}
```

```text
anthropic-priority-input-tokens-limit: 10000
anthropic-priority-input-tokens-remaining: 9618
anthropic-priority-input-tokens-reset: 2025-01-12T23:11:59Z
anthropic-priority-output-tokens-limit: 10000
anthropic-priority-output-tokens-remaining: 6000
anthropic-priority-output-tokens-reset: 2025-01-12T23:12:21Z
```

---

## Session Management

**URL**: https://docs.claude.com/en/api/agent-sdk/sessions

**Contents**:
- ​Session Management
- ​How Sessions Work
  - ​Getting the Session ID
- ​Resuming Sessions
- ​Forking Sessions
  - ​When to Fork a Session
  - ​Forking vs Continuing
  - ​Example: Forking a Session

**Examples**:

```python
import { query } from "@anthropic-ai/claude-agent-sdk"

let sessionId: string | undefined

const response = query({
  prompt: "Help me build a web application",
  options: {
    model: "claude-sonnet-4-5"
  }
})

for await (const message of response) {
  // The first message is a system init message with the session ID
  if (message.type === 'system' && message.subtype === 'init') {
    sessionId = message.session_id
    console.log(`Session started with ID: ${sessionId}`)
    // You can save th
...
```

```python
import { query } from "@anthropic-ai/claude-agent-sdk"

// Resume a previous session using its ID
const response = query({
  prompt: "Continue implementing the authentication system from where we left off",
  options: {
    resume: "session-xyz", // Session ID from previous conversation
    model: "claude-sonnet-4-5",
    allowedTools: ["Read", "Edit", "Write", "Glob", "Grep", "Bash"]
  }
})

// The conversation continues with full context from the previous session
for await (const message of re
...
```

```python
import { query } from "@anthropic-ai/claude-agent-sdk"

// First, capture the session ID
let sessionId: string | undefined

const response = query({
  prompt: "Help me design a REST API",
  options: { model: "claude-sonnet-4-5" }
})

for await (const message of response) {
  if (message.type === 'system' && message.subtype === 'init') {
    sessionId = message.session_id
    console.log(`Original session: ${sessionId}`)
  }
}

// Fork the session to try a different approach
const forkedResponse 
...
```

---

## Slash Commands in the SDK

**URL**: https://docs.claude.com/en/api/agent-sdk/slash-commands

**Contents**:
- ​Discovering Available Slash Commands
- ​Sending Slash Commands
- ​Common Slash Commands
  - ​/compact - Compact Conversation History
  - ​/clear - Clear Conversation
- ​Creating Custom Slash Commands
  - ​File Locations
  - ​File Format

**Examples**:

```python
import { query } from "@anthropic-ai/claude-agent-sdk";

for await (const message of query({
  prompt: "Hello Claude",
  options: { maxTurns: 1 }
})) {
  if (message.type === "system" && message.subtype === "init") {
    console.log("Available slash commands:", message.slash_commands);
    // Example output: ["/compact", "/clear", "/help"]
  }
}
```

```python
import { query } from "@anthropic-ai/claude-agent-sdk";

// Send a slash command
for await (const message of query({
  prompt: "/compact",
  options: { maxTurns: 1 }
})) {
  if (message.type === "result") {
    console.log("Command executed:", message.result);
  }
}
```

```python
import { query } from "@anthropic-ai/claude-agent-sdk";

for await (const message of query({
  prompt: "/compact",
  options: { maxTurns: 1 }
})) {
  if (message.type === "system" && message.subtype === "compact_boundary") {
    console.log("Compaction completed");
    console.log("Pre-compaction tokens:", message.compact_metadata.pre_tokens);
    console.log("Trigger:", message.compact_metadata.trigger);
  }
}
```

---

## Streaming Input

**URL**: https://docs.claude.com/en/api/agent-sdk/streaming-vs-single-mode

**Contents**:
- ​Overview
- ​Streaming Input Mode (Recommended)
  - ​How It Works
  - ​Benefits
- Image Uploads
- Queued Messages
- Tool Integration
- Hooks Support

**Examples**:

```python
import { query } from "@anthropic-ai/claude-agent-sdk";
import { readFileSync } from "fs";

async function* generateMessages() {
  // First message
  yield {
    type: "user" as const,
    message: {
      role: "user" as const,
      content: "Analyze this codebase for security issues"
    }
  };
  
  // Wait for conditions or user input
  await new Promise(resolve => setTimeout(resolve, 2000));
  
  // Follow-up with image
  yield {
    type: "user" as const,
    message: {
      role: "user" 
...
```

```python
import { query } from "@anthropic-ai/claude-agent-sdk";

// Simple one-shot query
for await (const message of query({
  prompt: "Explain the authentication flow",
  options: {
    maxTurns: 1,
    allowedTools: ["Read", "Grep"]
  }
})) {
  if (message.type === "result") {
    console.log(message.result);
  }
}

// Continue conversation with session management
for await (const message of query({
  prompt: "Now explain the authorization process",
  options: {
    continue: true,
    maxTurns: 1
  
...
```

---

## Streaming Messages - Claude Docs

**URL**: https://docs.claude.com/en/docs/build-with-claude/streaming

---

## Streaming Messages

**URL**: https://docs.claude.com/en/docs/build-with-claude/streaming

**Contents**:
- ​Streaming with SDKs
- ​Event types
  - ​Ping events
  - ​Error events
  - ​Other events
- ​Content block delta types
  - ​Text delta
  - ​Input JSON delta

**Examples**:

```text
import anthropic

client = anthropic.Anthropic()

with client.messages.stream(
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}],
    model="claude-sonnet-4-5",
) as stream:
  for text in stream.text_stream:
      print(text, end="", flush=True)
```

```text
event: error
data: {"type": "error", "error": {"type": "overloaded_error", "message": "Overloaded"}}
```

```text
event: content_block_delta
data: {"type": "content_block_delta","index": 0,"delta": {"type": "text_delta", "text": "ello frien"}}
```

---

## Subagents in the SDK

**URL**: https://docs.claude.com/en/api/agent-sdk/subagents

**Contents**:
- ​Overview
- ​Benefits of Using Subagents
  - ​Context Management
  - ​Parallelization
  - ​Specialized Instructions and Knowledge
  - ​Tool Restrictions
- ​Creating Subagents
  - ​Programmatic Definition (Recommended)

**Examples**:

```python
import { query } from '@anthropic-ai/claude-agent-sdk';

const result = query({
  prompt: "Review the authentication module for security issues",
  options: {
    agents: {
      'code-reviewer': {
        description: 'Expert code review specialist. Use for quality, security, and maintainability reviews.',
        prompt: `You are a code review specialist with expertise in security, performance, and best practices.

When reviewing code:
- Identify security vulnerabilities
- Check for performanc
...
```

```text
---
name: code-reviewer
description: Expert code review specialist. Use for quality, security, and maintainability reviews.
tools: Read, Grep, Glob, Bash
---

Your subagent's system prompt goes here. This defines the subagent's
role, capabilities, and approach to solving problems.
```

```javascript
const result = query({
  prompt: "Optimize the database queries in the API layer",
  options: {
    agents: {
      'performance-optimizer': {
        description: 'Use PROACTIVELY when code changes might impact performance. MUST BE USED for optimization tasks.',
        prompt: 'You are a performance optimization specialist...',
        tools: ['Read', 'Edit', 'Bash', 'Grep'],
        model: 'sonnet'
      }
    }
  }
});
```

---

## Supported regions - Claude Docs

**URL**: https://docs.claude.com/en/api/supported-regions

---

## Supported regions

**URL**: https://docs.claude.com/en/api/supported-regions

---

## Templatize a prompt

**URL**: https://docs.claude.com/en/api/prompt-tools-templatize

**Contents**:
- ​Before you begin
- ​Getting started with the prompt improver
- ​Templatize a prompt
    - Headers
    - Body
    - Response

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like beta1,beta2 or specify the header multiple times for each beta.

Your unique API key for authentication.

This key is required in the header of all API requests, to authenticate your account and access Anthropic's services. Get your API key through the Console. Each key is scoped to a Workspace.

The prompt to templatize, structured as a list of message objects.

Each message in the messages array must:

Example of a simple text prompt:

Note that only contiguous user messages with text content are allowed. Assistant prefill is permitted, but other content types will cause validation errors.

Show child attributes

The existing system prompt to templatize.

Note that this differs from the Messages API; it is strictly a string.

"You are a professional English to German translator"

The templatized prompt with variable placeholders.

The response includes the input messages with specific values replaced by variable placeholders. These messages maintain the original message structure but contain uppercase variable names in place of concrete values.

For example, an input message content like "Translate hello to German" would be transformed to "Translate {{WORD_TO_TRANSLATE}} to {{TARGET_LANGUAGE}}".

Show child attributes

The input system prompt with variables identified and replaced.

If no system prompt was provided in the original request, this field will be an empty string.

"You are a professional English to {{TARGET_LANGUAGE}} translator"

Show child attributes

A mapping of template variable names to their original values, as extracted from the input prompt during templatization. Each key represents a variable name identified in the templatized prompt, and each value contains the corresponding content from the original prompt that was replaced by that variable.

In this example response, the original prompt – Translate hello to German – was t

*[Content truncated - see full docs]*

**Examples**:

```text
[  {    "role": "user",     "content": [      {        "type": "text",        "text": "Translate hello to German"      }    ]  }]
```

```text
[  {    "content": [      {        "text": "Translate hello to German",        "type": "text"      }    ],    "role": "user"  }]
```

```text
{  "system": "You are a professional English to German translator",  [...]}
```

---

## Todo Lists

**URL**: https://docs.claude.com/en/api/agent-sdk/todo-tracking

**Contents**:
  - ​Todo Lifecycle
  - ​When Todos Are Used
- ​Examples
  - ​Monitoring Todo Changes
  - ​Real-time Progress Display
- ​Related Documentation

**Examples**:

```python
import { query } from "@anthropic-ai/claude-agent-sdk";

for await (const message of query({
  prompt: "Optimize my React app performance and track progress with todos",
  options: { maxTurns: 15 }
})) {
  // Todo updates are reflected in the message stream
  if (message.type === "assistant") {
    for (const block of message.message.content) {
      if (block.type === "tool_use" && block.name === "TodoWrite") {
        const todos = block.input.todos;

        console.log("Todo Status Update:")
...
```

```python
import { query } from "@anthropic-ai/claude-agent-sdk";

class TodoTracker {
  private todos: any[] = [];
  
  displayProgress() {
    if (this.todos.length === 0) return;
    
    const completed = this.todos.filter(t => t.status === "completed").length;
    const inProgress = this.todos.filter(t => t.status === "in_progress").length;
    const total = this.todos.length;
    
    console.log(`\nProgress: ${completed}/${total} completed`);
    console.log(`Currently working on: ${inProgress} tas
...
```

---

## Tracking Costs and Usage

**URL**: https://docs.claude.com/en/api/agent-sdk/cost-tracking

**Contents**:
- ​SDK Cost Tracking
- ​Understanding Token Usage
  - ​Key Concepts
- ​Usage Reporting Structure
  - ​Single vs Parallel Tool Use
  - ​Message Flow Example
- ​Important Usage Rules
  - ​1. Same ID = Same Usage

**Examples**:

```python
import { query } from "@anthropic-ai/claude-agent-sdk";

// Example: Tracking usage in a conversation
const result = await query({
  prompt: "Analyze this codebase and run tests",
  options: {
    onMessage: (message) => {
      if (message.type === 'assistant' && message.usage) {
        console.log(`Message ID: ${message.id}`);
        console.log(`Usage:`, message.usage);
      }
    }
  }
});
```

```text
<!-- Step 1: Initial request with parallel tool uses -->
assistant (text)      { id: "msg_1", usage: { output_tokens: 100, ... } }
assistant (tool_use)  { id: "msg_1", usage: { output_tokens: 100, ... } }
assistant (tool_use)  { id: "msg_1", usage: { output_tokens: 100, ... } }
assistant (tool_use)  { id: "msg_1", usage: { output_tokens: 100, ... } }
user (tool_result)
user (tool_result)
user (tool_result)

<!-- Step 2: Follow-up response -->
assistant (text)      { id: "msg_2", usage: { output_
...
```

```javascript
// All these messages have the same ID and usage
const messages = [
  { type: 'assistant', id: 'msg_123', usage: { output_tokens: 100 } },
  { type: 'assistant', id: 'msg_123', usage: { output_tokens: 100 } },
  { type: 'assistant', id: 'msg_123', usage: { output_tokens: 100 } }
];

// Charge only once per unique message ID
const uniqueUsage = messages[0].usage; // Same for all messages with this ID
```

---

## Update API Keys

**URL**: https://docs.claude.com/en/api/admin-api/apikeys/update-api-key

**Contents**:
    - Headers
    - Path Parameters
    - Body
    - Response

Your unique Admin API key for authentication.

This key is required in the header of all Admin API requests, to authenticate your account and access Anthropic's services. Get your Admin API key through the Console.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

Status of the API key.

RFC 3339 datetime string indicating when the API Key was created.

"2024-10-30T23:58:27.427722Z"

The ID and type of the actor that created the API key.

Show child attributes

"apikey_01Rj2N8SVvo6BePZj99NhmiT"

Partially redacted hint for the API key.

"sk-ant-api03-R2D...igAA"

Status of the API key.

For API Keys, this is always "api_key".

ID of the Workspace associated with the API key, or null if the API key belongs to the default Workspace.

"wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"

---

## Update User

**URL**: https://docs.claude.com/en/api/admin-api/users/update-user

**Contents**:
    - Headers
    - Path Parameters
    - Body
    - Response

Your unique Admin API key for authentication.

This key is required in the header of all Admin API requests, to authenticate your account and access Anthropic's services. Get your Admin API key through the Console.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

New role for the User. Cannot be "admin".

RFC 3339 datetime string indicating when the User joined the Organization.

"2024-10-30T23:58:27.427722Z"

"user_01WCz1FkmYMm4gnmykNKUu3Q"

Organization role of the User.

For Users, this is always "user".

---

## Update User - Claude Docs

**URL**: https://docs.claude.com/en/api/admin-api/users/update-user

---

## Update Workspace Member

**URL**: https://docs.claude.com/en/api/admin-api/workspace_members/update-workspace-member

**Contents**:
    - Headers
    - Path Parameters
    - Body
    - Response

Your unique Admin API key for authentication.

This key is required in the header of all Admin API requests, to authenticate your account and access Anthropic's services. Get your Admin API key through the Console.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

New workspace role for the User.

For Workspace Members, this is always "workspace_member".

"user_01WCz1FkmYMm4gnmykNKUu3Q"

"wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"

Role of the Workspace Member.

---

## Update Workspace

**URL**: https://docs.claude.com/en/api/admin-api/workspaces/update-workspace

**Contents**:
    - Headers
    - Path Parameters
    - Body
    - Response

Your unique Admin API key for authentication.

This key is required in the header of all Admin API requests, to authenticate your account and access Anthropic's services. Get your Admin API key through the Console.

The version of the Claude API you want to use.

Read more about versioning and our version history here.

Name of the Workspace.

RFC 3339 datetime string indicating when the Workspace was archived, or null if the Workspace is not archived.

"2024-11-01T23:59:27.427722Z"

RFC 3339 datetime string indicating when the Workspace was created.

"2024-10-30T23:58:27.427722Z"

Hex color code representing the Workspace in the Anthropic Console.

"wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"

Name of the Workspace.

For Workspaces, this is always "workspace".

---

## Usage and Cost API

**URL**: https://docs.claude.com/en/api/usage-cost-api

**Contents**:
- ​Partner solutions
- Datadog
- Grafana Cloud
- Honeycomb
- ​Quick start
- ​Usage API
  - ​Key concepts
  - ​Basic examples

**Examples**:

```text
curl "https://api.anthropic.com/v1/organizations/usage_report/messages?\
starting_at=2025-01-08T00:00:00Z&\
ending_at=2025-01-15T00:00:00Z&\
bucket_width=1d" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ADMIN_API_KEY"
```

```text
User-Agent: YourApp/1.0.0 (https://yourapp.com)
```

```text
curl "https://api.anthropic.com/v1/organizations/usage_report/messages?\
starting_at=2025-01-01T00:00:00Z&\
ending_at=2025-01-08T00:00:00Z&\
group_by[]=model&\
bucket_width=1d" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ADMIN_API_KEY"
```

---

## Using Agent Skills with the API

**URL**: https://docs.claude.com/en/api/skills-guide

**Contents**:
- ​Quick Links
- Get started with Agent Skills
- Create Custom Skills
- ​Overview
  - ​Using Skills
  - ​Prerequisites
- ​Using Skills in Messages
  - ​Container Parameter

**Examples**:

```text
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [
            {
                "type": "anthropic",
                "skill_id": "pptx",
                "version": "latest"
            }
        ]
    },
    messages=[{
        "role": "user",
        "content": "Create a presentation about renewable
...
```

```python
import anthropic

client = anthropic.Anthropic()

# Step 1: Use a Skill to create a file
response = client.beta.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [
            {"type": "anthropic", "skill_id": "xlsx", "version": "latest"}
        ]
    },
    messages=[{
        "role": "user",
        "content": "Create an Excel file with a simple budget spreadsheet"
    }
...
```

```text
# Get file metadata
file_info = client.beta.files.retrieve_metadata(
    file_id=file_id,
    betas=["files-api-2025-04-14"]
)
print(f"Filename: {file_info.filename}, Size: {file_info.size_bytes} bytes")

# List all files
files = client.beta.files.list(betas=["files-api-2025-04-14"])
for file in files.data:
    print(f"{file.filename} - {file.created_at}")

# Delete a file
client.beta.files.delete(
    file_id=file_id,
    betas=["files-api-2025-04-14"]
)
```

---

## Versions

**URL**: https://docs.claude.com/en/api/versioning

**Contents**:
- ​Version history

---

## Vertex AI API

**URL**: https://docs.claude.com/en/api/claude-on-vertex-ai

**Contents**:
- ​Install an SDK for accessing Vertex AI
- ​Accessing Vertex AI
  - ​Model Availability
    - ​API model IDs
  - ​Making requests
- ​Activity logging
- ​Feature support
- ​Global vs regional endpoints

**Examples**:

```text
pip install -U google-cloud-aiplatform "anthropic[vertex]"
```

```python
from anthropic import AnthropicVertex

project_id = "MY_PROJECT_ID"
region = "global"

client = AnthropicVertex(project_id=project_id, region=region)

message = client.messages.create(
    model="claude-sonnet-4-5@20250929",
    max_tokens=100,
    messages=[
        {
            "role": "user",
            "content": "Hey Claude!",
        }
    ],
)
print(message)
```

```python
from anthropic import AnthropicVertex

project_id = "MY_PROJECT_ID"
region = "global"

client = AnthropicVertex(project_id=project_id, region=region)

message = client.messages.create(
    model="claude-sonnet-4-5@20250929",
    max_tokens=100,
    messages=[
        {
            "role": "user",
            "content": "Hey Claude!",
        }
    ],
)
print(message)
```

---

## What's new in Claude 4.5

**URL**: https://docs.claude.com/en/docs/about-claude/models/whats-new-claude-4-5

**Contents**:
- ​Key improvements in Sonnet 4.5 over Sonnet 4
  - ​Coding excellence
  - ​Agent capabilities
  - ​Communication and interaction style
  - ​Creative content generation
- ​Key improvements in Haiku 4.5 over Haiku 3.5
  - ​Near-frontier intelligence with blazing speed
  - ​Extended thinking capabilities

**Examples**:

```text
tools=[
    {
        "type": "memory_20250818",
        "name": "memory"
    }
]
```

```text
response = client.beta.messages.create(
    betas=["context-management-2025-06-27"],
    model="claude-sonnet-4-5",  # or claude-haiku-4-5
    max_tokens=4096,
    messages=[{"role": "user", "content": "..."}],
    context_management={
        "edits": [
            {
                "type": "clear_tool_uses_20250919",
                "trigger": {"type": "input_tokens", "value": 500},
                "keep": {"type": "tool_uses", "value": 2},
                "clear_at_least": {"type": "input_tok
...
```

```text
{
  "stop_reason": "model_context_window_exceeded",
  "usage": {
    "input_tokens": 150000,
    "output_tokens": 49950
  }
}
```

---
