# Nextjs - Common Patterns

Quick reference for common nextjs patterns and usage.

## Code Patterns

### 1. Using App RouterFeatures available in /appLatest Version15.5.6Getting StartedInstallationProject Str

```
fetch
```

### 2. Using App RouterFeatures available in /appLatest Version15.5.6Getting StartedInstallationProject Str

```
fetch
```

### 3. App RouterGetting StartedCaching and RevalidatingCopy pageCaching and RevalidatingCaching is a techn

```
fetch
```

### 4. Caching and RevalidatingCaching is a technique for storing the result of data fetching and other com

```
fetch
```

### 5. Next.js provides a few APIs to handle caching and revalidation. This guide will walk you through whe

```
fetch
```

### 6. Using App RouterFeatures available in /appLatest Version15.5.6Getting StartedInstallationProject Str

```
package.json
```

### 7. Using App RouterFeatures available in /appLatest Version15.5.6Getting StartedInstallationProject Str

```
package.json
```

### 8. App RouterGetting StartedDeployingCopy pageDeployingNext.js can be deployed as a Node.js server, Doc

```
package.json
```

## Examples

### Example 1

```typescript
export default {
  plugins: {
    '@tailwindcss/postcss': {},
  },
}
```

### Example 2

```javascript
export default async function Page() {
  const data = await fetch('https://...', { cache: 'force-cache' })
}
```

### Example 3

```javascript
export default async function Page() {
  const data = await fetch('https://...', { next: { revalidate: 3600 } })
}
```

### Example 4

```javascript
'use server'
 
export async function createPost(prevState: any, formData: FormData) {
  const title = formData.get('title')
  const content = formData.get('content')
 
  const res = await fetch('https://api.vercel.app/posts', {
    method: 'POST',
    body: { title, content },
  })
  const json = await res.json()
 
  if (!res.ok) {
    return { message: 'Failed to create post' }
  }
}
```

### Example 5

```javascript
export default async function Page() {
  const data = await fetch('https://api.vercel.app/blog')
  const posts = await data.json()
  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  )
}
```

### Example 6

```python
import { db, posts } from '@/lib/db'
 
export default async function Page() {
  const allPosts = await db.select().from(posts)
  return (
    <ul>
      {allPosts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  )
}
```

### Example 7

```python
import { Geist } from 'next/font/google'
 
const geist = Geist({
  subsets: ['latin'],
})
 
export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className={geist.className}>
      <body>{children}</body>
    </html>
  )
}
```

### Example 8

```python
import { Geist } from 'next/font/google'
 
const geist = Geist({
  subsets: ['latin'],
})
 
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className={geist.className}>
      <body>{children}</body>
    </html>
  )
}
```

### Example 9

```python
import Image from 'next/image'
 
export default function Page() {
  return <Image src="" alt="" />
}
```

### Example 10

```python
import Image from 'next/image'
 
export default function Page() {
  return (
    <Image
      src="/profile.png"
      alt="Picture of the author"
      width={500}
      height={500}
    />
  )
}
```


## Categories

See organized documentation in `references/`:

- `references/app_router.md` - App Router
- `references/getting_started.md` - Getting Started
- `references/other.md` - Other
