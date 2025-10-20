# Vercel - Common Patterns

Quick reference for common vercel patterns and usage.

## Code Patterns

### 1. Buy a DomainSearch...⌘ KGetting StartedExpand menuProjects and DeploymentsUse a TemplateImport Exist

```
@vercel/functions
```

### 2. Getting StartedBuy a DomainCopy pageBuy a domainUsing CLI?Use this snippet to purchase a new domain 

```
vercel domains buy [domain]
```

### 3. Buy a domainUsing CLI?Use this snippet to purchase a new domain from Vercel:terminalvercel domains b

```
vercel domains buy [domain]
```

### 4. Using CLI?Use this snippet to purchase a new domain from Vercel:terminalvercel domains buy [domain] 

```
vercel domains buy [domain]
```

### 5. Getting StartedSearch...⌘ KGetting StartedExpand menuProjects and DeploymentsUse a TemplateImport Ex

```
@vercel/functions
```

### 6. AI GatewayGetting StartedCopy pageGetting StartedThis quickstart will walk you through making an AI 

```
mkdir
```

### 7. Getting StartedThis quickstart will walk you through making an AI model request with Vercel's AI Gat

```
mkdir
```

### 8. This quickstart will walk you through making an AI model request with Vercel's AI Gateway. While thi

```
mkdir
```

## Examples

### Example 1

```typescript
pnpm i ai dotenv @types/node tsx typescript
```

### Example 2

```python
import { inject } from '@vercel/analytics';
 
inject();
```

### Example 3

```python
// Use "type: module" in package.json to use ES modules
import express from 'express';
const app = express();
 
// Define your routes
app.get('/', (req, res) => {
  res.json({ message: 'Hello from Express on Vercel!' });
});
 
// Export the Express app
export default app;
```

### Example 4

```python
from fastapi import FastAPI
 
app = FastAPI()
 
@app.get("/")
def read_root():
    return {"Python": "on Vercel"}
```

### Example 5

```python
from flask import Flask
 
app = Flask(__name__)
 
@app.route("/")
def hello_world():
    return {"message": "Hello, World!"}
```

### Example 6

```python
import type { GatsbyNode } from 'gatsby';
 
export const createPages: GatsbyNode['createPages'] = async ({ actions }) => {
  const { createPage } = actions;
  createPage({
    defer: true,
    path: '/using-dsg',
    component: require.resolve('./src/templates/using-dsg.js'),
    context: {},
  });
};
```

### Example 7

```python
import { generateText } from 'ai';
 
const { text } = generateText({
  model: 'anthropic/claude-sonnet-4',
  prompt: 'What is the capital of France?',
});
```

### Example 8

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

### Example 9

```python
import { generateText } from 'ai';
 
const { text } = await generateText({
  model: 'openai/gpt-5',
  prompt: 'Explain the concept of quantum entanglement.',
});
```

### Example 10

```python
import { generateText } from 'ai';
import { anthropic } from '@ai-sdk/anthropic';
 
const { text } = await generateText({
  model: anthropic('claude-3-7-sonnet-20250219'),
  prompt: 'How many people will live in the world in 2040?',
});
```


## Categories

See organized documentation in `references/`:

- `references/deployments.md` - Deployments
- `references/frameworks.md` - Frameworks
- `references/getting_started.md` - Getting Started
- `references/observability.md` - Observability
- `references/other.md` - Other
