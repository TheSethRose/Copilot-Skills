---
description: Next generation frontend tooling
---

# Vite

**Purpose**: Next generation frontend tooling

## When to Use This Skill

Use this skill when:
- Working with vite projects
- Implementing vite features
- Debugging vite code
- Learning vite best practices
- Building applications with vite

**Keywords**: vite, guide

## Quick Reference

### Common Patterns

**1. Are you an LLM? You can read better optimized documentation at /guide/features.m**

```
import { someMethod } from 'my-dep'
```

**2. Are you an LLM? You can read better optimized documentation at /guide/features.m**

```
import { someMethod } from 'my-dep'
```

**3. Use the Type-Only Imports and Export syntax to avoid potential problems like typ**

```
import type { T } from 'only/types'
export type { T }
```

**4. Are you an LLM? You can read better optimized documentation at /guide.md for thi**

```
/vit/
```

**5. Are you an LLM? You can read better optimized documentation at /guide.md for thi**

```
/vit/
```

### Code Examples

**Example 1** (typescript):
```typescript
export default defineConfig({
  build: {
    rollupOptions: {
      // https://rollupjs.org/configuration-options/
    },
  },
})
```

**Example 2** (javascript):
```javascript
window.addEventListener('vite:preloadError', (event) => {
  window.location.reload() // for example, refresh the page
})
```

**Example 3** (python):
```python
// works as expected
import React, { useState } from 'react'
```

**Example 4** (typescript):
```typescript
export default defineConfig({
  optimizeDeps: {
    include: ['linked-dep'],
  },
  build: {
    commonjsOptions: {
      include: [/linked-dep/, /node_modules/],
    },
  },
})
```

**Example 5** (python):
```python
import { someMethod } from 'my-dep'
```

## Reference Documentation

This skill includes comprehensive documentation in `.github/copilot-skills/vite/references/`:

- **guide.md** - Guide documentation

## How to Use

### For Quick Answers
Ask directly about vite features, APIs, or patterns.

### For Detailed Information
Reference specific documentation files:
- Check `references/getting_started.md` for setup
- Check `references/api_reference.md` for API details
- Check category files for specific topics

### For Code Examples
Use the Quick Reference patterns above or ask for specific examples.

## Related Skills

- `/react` – Primary framework for Vite
- `/vue` – Vue support in Vite
- `/svelte` – Svelte support in Vite
- `/typescript` – TypeScript integration
- `/tailwind` – CSS framework integration

## More Information

- **Base Documentation**: https://vitejs.dev/guide/
- **Generated**: 2025-10-20
- **Total Pages**: 15
