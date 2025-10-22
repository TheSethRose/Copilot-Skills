---
description: Open source authentication framework for the modern web
---

# Better-Auth

**Purpose**: Open source authentication framework for the modern web

## When to Use This Skill

Use this skill when:
- Working with better-auth projects
- Implementing better-auth features
- Debugging better-auth code
- Learning better-auth best practices
- Building applications with better-auth

**Keywords**: better-auth, introduction, installation, configuration, guides, authentication

## Quick Reference

### Common Patterns

**1. On this pageAPI KeyCopy MarkdownOpen inThe API Key plugin allows you to create a**

```
import { betterAuth } from "better-auth"
import { apiKey } from "better-auth/plugins"

export const auth = betterAuth({
    plugins: [ 
        apiKey() 
    ] 
})
```

**2. The API Key plugin allows you to create and manage API keys for your application**

```
import { betterAuth } from "better-auth"
import { apiKey } from "better-auth/plugins"

export const auth = betterAuth({
    plugins: [ 
        apiKey() 
    ] 
})
```

**3. Here's an example:**

```
export const auth = betterAuth({
  plugins: [
    apiKey({
      customKeyGenerator: (options: {
        length: number;
        prefix: string | undefined;
      }) => {
        const apiKey = mySupe
```

**4. type Permissions = { [resourceType: string]: string[]; }; // Example: const perm**

```
type Permissions = {
  [resourceType: string]: string[];
};

// Example:
const permissions = {
  files: ["read", "write", "delete"],
  users: ["read"],
  projects: ["read", "write"],
};
```

**5. type Permissions = { [resourceType: string]: string[]; }; // Example: const perm**

```
type Permissions = {
  [resourceType: string]: string[];
};

// Example:
const permissions = {
  files: ["read", "write", "delete"],
  users: ["read"],
  projects: ["read", "write"],
};
```

### Code Examples

**Example 1** (python):
```python
import { betterAuth } from "better-auth";
import { headers } from "next/headers";

export const auth = betterAuth({
    //...
})

// calling get session on the server
await auth.api.getSession({
    headers: await headers() // some endpoints might re
```

**Example 2** (python):
```python
import { betterAuth } from "better-auth";
import { headers } from "next/headers";

export const auth = betterAuth({
    //...
})

// calling get session on the server
await auth.api.getSession({
    headers: await headers() // some endpoints might re
```

**Example 3** (python):
```python
import { betterAuth } from "better-auth"
import { apiKey } from "better-auth/plugins"

export const auth = betterAuth({
    plugins: [ 
        apiKey() 
    ] 
})
```

**Example 4** (python):
```python
import { betterAuth } from "better-auth"
import { apiKey } from "better-auth/plugins"

export const auth = betterAuth({
    plugins: [ 
        apiKey() 
    ] 
})
```

**Example 5** (python):
```python
import { betterAuth } from "better-auth"
import { admin } from "better-auth/plugins"

export const auth = betterAuth({
    // ... other config options
    plugins: [
        admin() 
    ]
})
```

## Reference Documentation

This skill includes comprehensive documentation in `.github/copilot-skills/auth/better-auth/references/`:

- **authentication.md** - Authentication documentation
- **configuration.md** - Configuration documentation
- **guides.md** - Guides documentation
- **installation.md** - Installation documentation
- **introduction.md** - Introduction documentation

## How to Use

### For Quick Answers
Ask directly about better-auth features, APIs, or patterns.

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

- **Base Documentation**: https://www.better-auth.com/docs
- **Generated**: 2025-10-20
- **Total Pages**: 86
