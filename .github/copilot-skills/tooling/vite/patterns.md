# Vite - Common Patterns

Quick reference for common vite patterns and usage.

## Code Patterns

### 1. Are you an LLM? You can read better optimized documentation at /guide/features.md for this page in M

```
import { someMethod } from 'my-dep'
```

### 2. Are you an LLM? You can read better optimized documentation at /guide/features.md for this page in M

```
import { someMethod } from 'my-dep'
```

### 3. Use the Type-Only Imports and Export syntax to avoid potential problems like type-only imports being

```
import type { T } from 'only/types'
export type { T }
```

### 4. Are you an LLM? You can read better optimized documentation at /guide.md for this page in Markdown f

```
/vit/
```

### 5. Are you an LLM? You can read better optimized documentation at /guide.md for this page in Markdown f

```
/vit/
```

### 6. Vite is opinionated and comes with sensible defaults out of the box. Read about what's possible in t

```
esnext
```

### 7. Are you an LLM? You can read better optimized documentation at /guide/api-hmr.md for this page in Ma

```
import.meta.hot
```

### 8. Are you an LLM? You can read better optimized documentation at /guide/api-hmr.md for this page in Ma

```
import.meta.hot
```

## Examples

### Example 1

```typescript
export default defineConfig({
  server: {
    cors: {
      // the origin you will be accessing via browser
      origin: 'http://my-backend.example.com',
    },
  },
  build: {
    // generate .vite/manifest.json in outDir
    manifest: true,
    rollupOptions: {
      // overwrite default .html entry
      input: '/path/to/main.js',
    },
  },
})
```

### Example 2

```typescript
export default defineConfig({
  build: {
    rollupOptions: {
      // https://rollupjs.org/configuration-options/
    },
  },
})
```

### Example 3

```javascript
window.addEventListener('vite:preloadError', (event) => {
  window.location.reload() // for example, refresh the page
})
```

### Example 4

```python
// works as expected
import React, { useState } from 'react'
```

### Example 5

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

### Example 6

```python
import { someMethod } from 'my-dep'
```

### Example 7

```python
import type { T } from 'only/types'
export type { T }
```

### Example 8

```javascript
async function createServer(inlineConfig?: InlineConfig): Promise<ViteDevServer>
```


## Categories

See organized documentation in `references/`:

- `references/guide.md` - Guide
