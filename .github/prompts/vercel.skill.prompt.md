---
description: Platform for frontend developers with tools for deployment and preview
---

# Vercel

**Purpose**: Platform for frontend developers with tools for deployment and preview

## When to Use This Skill

Use this skill when:
- Working with vercel projects
- Implementing vercel features
- Debugging vercel code
- Learning vercel best practices
- Building applications with vercel

**Keywords**: vercel, getting_started, frameworks, deployments, observability, other

## Quick Reference

### Common Patterns

**1. AI SDKSearch...⌘ KGetting StartedExpand menuProjects and DeploymentsUse a Templa**

```
@vercel/functions
```

**2. Copy pageAI SDKThe AI SDK is the TypeScript toolkit designed to help developers **

```
import { generateText } from 'ai';
 
const { text } = await generateText({
  model: 'openai/gpt-5',
  prompt: 'Explain the concept of quantum entanglement.',
});
```

**3. AI SDKThe AI SDK is the TypeScript toolkit designed to help developers build AI-**

```
import { generateText } from 'ai';
 
const { text } = await generateText({
  model: 'openai/gpt-5',
  prompt: 'Explain the concept of quantum entanglement.',
});
```

**4. The AI SDK is the TypeScript toolkit designed to help developers build AI-powere**

```
import { generateText } from 'ai';
 
const { text } = await generateText({
  model: 'openai/gpt-5',
  prompt: 'Explain the concept of quantum entanglement.',
});
```

**5. The following example shows how to generate text with the AI SDK using OpenAI's **

```
import { generateText } from 'ai';
 
const { text } = await generateText({
  model: 'openai/gpt-5',
  prompt: 'Explain the concept of quantum entanglement.',
});
```

### Code Examples

**Example 1** (python):
```python
import { generateText } from 'ai';
 
const { text } = generateText({
  model: 'anthropic/claude-sonnet-4',
  prompt: 'What is the capital of France?',
});
```

**Example 2** (python):
```python
import { generateText } from 'ai';
 
const { text } = await generateText({
  model: 'openai/gpt-5',
  prompt: 'Explain the concept of quantum entanglement.',
});
```

**Example 3** (python):
```python
import { generateText } from 'ai';
import { anthropic } from '@ai-sdk/anthropic';
 
const { text } = await generateText({
  model: anthropic('claude-3-7-sonnet-20250219'),
  prompt: 'How many people will live in the world in 2040?',
});
```

**Example 4** (python):
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
 
  // Ha
```

**Example 5** (python):
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

## Reference Documentation

This skill includes comprehensive documentation in `.github/copilot-skills/deployment/vercel/references/`:

- **deployments.md** - Deployments documentation
- **frameworks.md** - Frameworks documentation
- **getting_started.md** - Getting Started documentation
- **observability.md** - Observability documentation
- **other.md** - Other documentation

## How to Use

### For Quick Answers
Ask directly about vercel features, APIs, or patterns.

### For Detailed Information
Reference specific documentation files:
- Check `references/getting_started.md` for setup
- Check `references/api_reference.md` for API details
- Check category files for specific topics

### For Code Examples
Use the Quick Reference patterns above or ask for specific examples.

## Related Skills

- None (standalone skill)

## More Information

- **Base Documentation**: https://vercel.com/docs
- **Generated**: 2025-10-19
- **Total Pages**: 100
