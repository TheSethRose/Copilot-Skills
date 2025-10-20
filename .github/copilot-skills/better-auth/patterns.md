# Better-Auth - Common Patterns

Quick reference for common better-auth patterns and usage.

## Code Patterns

### 1. On this pageIntroductionBetter Auth is a framework-agnostic, universal authentication and authorizat

```
LLMs.txt
```

### 2. Better Auth is a framework-agnostic, universal authentication and authorization framework for TypeSc

```
LLMs.txt
```

### 3. Better Auth exposes an LLMs.txt that helps AI models understand how to integrate and interact with y

```
LLMs.txt
```

### 4. On this pageIntroductionBetter Auth is a framework-agnostic, universal authentication and authorizat

```
LLMs.txt
```

### 5. Better Auth is a framework-agnostic, universal authentication and authorization framework for TypeSc

```
LLMs.txt
```

### 6. Better Auth exposes an LLMs.txt that helps AI models understand how to integrate and interact with y

```
LLMs.txt
```

### 7. On this pageInstallationCopy MarkdownOpen inInstall the PackageLet's start by adding Better Auth to 

```
npm install better-auth
```

### 8. Install the PackageLet's start by adding Better Auth to your project:npmpnpmyarnbunnpm install bette

```
npm install better-auth
```

## Examples

### Example 1

```python
import { betterAuth } from "better-auth"
import { apiKey } from "better-auth/plugins"

export const auth = betterAuth({
    plugins: [ 
        apiKey() 
    ] 
})
```

### Example 2

```python
import { betterAuth } from "better-auth"
import { apiKey } from "better-auth/plugins"

export const auth = betterAuth({
    plugins: [ 
        apiKey() 
    ] 
})
```

### Example 3

```python
import { betterAuth } from "better-auth"
import { anonymous } from "better-auth/plugins"

export const auth = betterAuth({
    // ... other config options
    plugins: [
        anonymous() 
    ]
})
```

### Example 4

```python
import { betterAuth } from "better-auth"
import { anonymous } from "better-auth/plugins"

export const auth = betterAuth({
    // ... other config options
    plugins: [
        anonymous() 
    ]
})
```

### Example 5

```python
import { betterAuth } from "better-auth";
import { mcp } from "better-auth/plugins";

export const auth = betterAuth({
    plugins: [
        mcp({
            loginPage: "/sign-in" // path to your login page
        })
    ]
});
```

### Example 6

```python
import { betterAuth } from "better-auth";
import { mcp } from "better-auth/plugins";

export const auth = betterAuth({
    plugins: [
        mcp({
            loginPage: "/sign-in" // path to your login page
        })
    ]
});
```

### Example 7

```python
import { auth } from "@/lib/auth";
import { toNextJsHandler } from "better-auth/next-js";

export const { GET, POST } = toNextJsHandler(auth.handler);
```

### Example 8

```python
import { auth } from "@/lib/auth";
import { toNextJsHandler } from "better-auth/next-js";

export const { GET, POST } = toNextJsHandler(auth.handler);
```

### Example 9

```python
import { auth } from "~/lib/auth"; // import your auth config

export default defineEventHandler((event) => {
	return auth.handler(toWebRequest(event));
});
```

### Example 10

```python
import { auth } from "~/lib/auth"; // import your auth config

export default defineEventHandler((event) => {
	return auth.handler(toWebRequest(event));
});
```


## Categories

See organized documentation in `references/`:

- `references/authentication.md` - Authentication
- `references/configuration.md` - Configuration
- `references/guides.md` - Guides
- `references/installation.md` - Installation
- `references/introduction.md` - Introduction
