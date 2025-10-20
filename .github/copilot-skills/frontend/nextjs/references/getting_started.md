# Nextjs - Getting Started

**Pages**: 18

---

## App Router: Getting Started | Next.js

**URL**: https://nextjs.org/docs/app/getting-started

**Contents**:
- Getting Started
- Pre-requisite knowledge
- Next Steps
  - Installation
  - Project Structure
  - Layouts and Pages
  - Linking and Navigating
  - Server and Client Components

Features available in /app

Welcome to the Next.js documentation!

This Getting Started section will help you create your first Next.js app and learn the core features you'll use in every project.

Our documentation assumes some familiarity with web development. Before getting started, it'll help if you're comfortable with:

If you're new to React or need a refresher, we recommend starting with our React Foundations course, and the Next.js Foundations course that has you building an application as you learn.

---

## Getting Started: CSS | Next.js

**URL**: https://nextjs.org/docs/app/getting-started/css

**Contents**:
- CSS
- Tailwind CSS
- CSS Modules
- Global CSS
- External stylesheets
- Ordering and Merging
  - Recommendations
- Development vs Production

Features available in /app

Next.js provides several ways to style your application using CSS, including:

Tailwind CSS is a utility-first CSS framework that provides low-level utility classes to build custom designs.

Install Tailwind CSS:

Add the PostCSS plugin to your postcss.config.mjs file:

Import Tailwind in your global CSS file:

Import the CSS file in your root layout:

Now you can start using Tailwind's utility classes in your application:

Good to know: If you need broader browser support for very old browsers, see the Tailwind CSS v3 setup instructions.

CSS Modules locally scope CSS by generating unique class names. This allows you to use the same class in different files without worrying about naming collisions.

To start using CSS Modules, create a new file with the extension .module.css and import it into any component inside the app directory:

You can use global CSS to apply styles across your application.

Create a app/global.css file and import it in the root layout to apply the styles to every route in your application:

Good to know: Global styles can be imported into any layout, page, or component inside the app directory. However, since Next.js uses React's built-in support for stylesheets to integrate with Suspense, this currently does not remove stylesheets as you navigate between routes which can lead to conflicts. We recommend using global styles for truly global CSS (like Tailwind's base styles), Tailwind CSS for component styling, and CSS Modules for custom scoped CSS when needed.

Stylesheets published by external packages can be imported anywhere in the app directory, including colocated components:

Good to know: In React 19, <link rel="stylesheet" href="..." /> can also be used. See the React link documentation for more information.

Next.js optimizes CSS during production builds by automatically chunking (merging) stylesheets. The order of your CSS depends on the order you import styles in your code.

For example, base-button.modu

*[Content truncated - see full docs]*

**Examples**:

```text
pnpm add -D tailwindcss @tailwindcss/postcss
```

```typescript
export default {
  plugins: {
    '@tailwindcss/postcss': {},
  },
}
```

```text
@import 'tailwindcss';
```

---

## Getting Started: Caching and Revalidating | Next.js

**URL**: https://nextjs.org/docs/app/getting-started/caching-and-revalidating

**Contents**:
- Caching and Revalidating
- fetch
- unstable_cache
- revalidateTag
- revalidatePath
- API Reference
  - fetch
  - unstable_cache

Features available in /app

Caching is a technique for storing the result of data fetching and other computations so that future requests for the same data can be served faster, without doing the work again. While revalidation allows you to update cache entries without having to rebuild your entire application.

Next.js provides a few APIs to handle caching and revalidation. This guide will walk you through when and how to use them.

By default, fetch requests are not cached. You can cache individual requests by setting the cache option to 'force-cache'.

Good to know: Although fetch requests are not cached by default, Next.js will prerender routes that have fetch requests and cache the HTML. If you want to guarantee a route is dynamic, use the connection API.

To revalidate the data returned by a fetch request, you can use the next.revalidate option.

This will revalidate the data after a specified amount of seconds.

See the fetch API reference to learn more.

unstable_cache allows you to cache the result of database queries and other async functions. To use it, wrap unstable_cache around the function. For example:

The function accepts a third optional object to define how the cache should be revalidated. It accepts:

See the unstable_cache API reference to learn more.

revalidateTag is used to revalidate cache entries based on a tag and following an event. To use it with fetch, start by tagging the function with the next.tags option:

Alternatively, you can mark an unstable_cache function with the tags option:

Then, call revalidateTag in a Route Handler or Server Action:

You can reuse the same tag in multiple functions to revalidate them all at once.

See the revalidateTag API reference to learn more.

revalidatePath is used to revalidate a route and following an event. To use it, call it in a Route Handler or Server Action:

See the revalidatePath API reference to learn more.

**Examples**:

```javascript
export default async function Page() {
  const data = await fetch('https://...', { cache: 'force-cache' })
}
```

```javascript
export default async function Page() {
  const data = await fetch('https://...', { next: { revalidate: 3600 } })
}
```

```python
import { db } from '@/lib/db'
export async function getUserById(id: string) {
  return db
    .select()
    .from(users)
    .where(eq(users.id, id))
    .then((res) => res[0])
}
```

---

## Getting Started: Deploying | Next.js

**URL**: https://nextjs.org/docs/app/getting-started/deploying

**Contents**:
- Deploying
- Node.js server
  - Templates
- Docker
  - Templates
- Static export
  - Templates
- Adapters

Features available in /app

Next.js can be deployed as a Node.js server, Docker container, static export, or adapted to run on different platforms.

Next.js can be deployed to any provider that supports Node.js. Ensure your package.json has the "build" and "start" scripts:

Then, run npm run build to build your application and npm run start to start the Node.js server. This server supports all Next.js features. If needed, you can also eject to a custom server.

Node.js deployments support all Next.js features. Learn how to configure them for your infrastructure.

Next.js can be deployed to any provider that supports Docker containers. This includes container orchestrators like Kubernetes or a cloud provider that runs Docker.

Docker deployments support all Next.js features. Learn how to configure them for your infrastructure.

Note for development: While Docker is excellent for production deployments, consider using local development (npm run dev) instead of Docker during development on Mac and Windows for better performance. Learn more about optimizing local development.

Next.js enables starting as a static site or Single-Page Application (SPA), then later optionally upgrading to use features that require a server.

Since Next.js supports static exports, it can be deployed and hosted on any web server that can serve HTML/CSS/JS static assets. This includes tools like AWS S3, Nginx, or Apache.

Running as a static export does not support Next.js features that require a server. Learn more.

Next.js can be adapted to run on different platforms to support their infrastructure capabilities.

Refer to each provider's documentation for information on supported Next.js features:

Note: We are working on a Deployment Adapters API for all platforms to adopt. After completion, we will add documentation on how to write your own adapters.

**Examples**:

```text
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  }
}
```

---

## Getting Started: Error Handling | Next.js

**URL**: https://nextjs.org/docs/app/getting-started/error-handling

**Contents**:
- Error Handling
- Handling expected errors
  - Server Functions
  - Server Components
  - Not found
- Handling uncaught exceptions
  - Nested error boundaries
  - Global errors

Features available in /app

Errors can be divided into two categories: expected errors and uncaught exceptions. This page will walk you through how you can handle these errors in your Next.js application.

Expected errors are those that can occur during the normal operation of the application, such as those from server-side form validation or failed requests. These errors should be handled explicitly and returned to the client.

You can use the useActionState hook to handle expected errors in Server Functions.

For these errors, avoid using try/catch blocks and throw errors. Instead, model expected errors as return values.

You can pass your action to the useActionState hook and use the returned state to display an error message.

When fetching data inside of a Server Component, you can use the response to conditionally render an error message or redirect.

You can call the notFound function within a route segment and use the not-found.js file to show a 404 UI.

Uncaught exceptions are unexpected errors that indicate bugs or issues that should not occur during the normal flow of your application. These should be handled by throwing errors, which will then be caught by error boundaries.

Next.js uses error boundaries to handle uncaught exceptions. Error boundaries catch errors in their child components and display a fallback UI instead of the component tree that crashed.

Create an error boundary by adding an error.js file inside a route segment and exporting a React component:

Errors will bubble up to the nearest parent error boundary. This allows for granular error handling by placing error.tsx files at different levels in the route hierarchy.

Error boundaries don’t catch errors inside event handlers. They’re designed to catch errors during rendering to show a fallback UI instead of crashing the whole app.

In general, errors in event handlers or async code aren’t handled by error boundaries because they run after rendering.

To handle these cases, catch the erro

*[Content truncated - see full docs]*

**Examples**:

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

```python
'use client'
 
import { useActionState } from 'react'
import { createPost } from '@/app/actions'
 
const initialState = {
  message: '',
}
 
export function Form() {
  const [state, formAction, pending] = useActionState(createPost, initialState)
 
  return (
    <form action={formAction}>
      <label htmlFor="title">Title</label>
      <input type="text" id="title" name="title" required />
      <label htmlFor="content">Content</label>
      <textarea id="content" name="content" required />
   
...
```

```javascript
export default async function Page() {
  const res = await fetch(`https://...`)
  const data = await res.json()
 
  if (!res.ok) {
    return 'There was an error.'
  }
 
  return '...'
}
```

---

## Getting Started: Fetching Data | Next.js

**URL**: https://nextjs.org/docs/app/getting-started/fetching-data

**Contents**:
- Fetching Data
- Fetching data
  - Server Components
    - With the fetch API
    - With an ORM or database
  - Client Components
    - Streaming data with the use hook
    - Community libraries

Features available in /app

This page will walk you through how you can fetch data in Server and Client Components, and how to stream components that depend on data.

You can fetch data in Server Components using:

To fetch data with the fetch API, turn your component into an asynchronous function, and await the fetch call. For example:

Since Server Components are rendered on the server, you can safely make database queries using an ORM or database client. Turn your component into an asynchronous function, and await the call:

There are two ways to fetch data in Client Components, using:

You can use React's use hook to stream data from the server to client. Start by fetching data in your Server component, and pass the promise to your Client Component as prop:

Then, in your Client Component, use the use hook to read the promise:

In the example above, the <Posts> component is wrapped in a <Suspense> boundary. This means the fallback will be shown while the promise is being resolved. Learn more about streaming.

You can use a community library like SWR or React Query to fetch data in Client Components. These libraries have their own semantics for caching, streaming, and other features. For example, with SWR:

One way to deduplicate fetch requests is with request memoization. With this mechanism, fetch calls using GET or HEAD with the same URL and options in a single render pass are combined into one request. This happens automatically, and you can opt out by passing an Abort signal to fetch.

Request memoization is scoped to the lifetime of a request.

You can also deduplicate fetch requests by using Next.js’ Data Cache, for example by setting cache: 'force-cache' in your fetch options.

Data Cache allows sharing data across the current render pass and incoming requests.

If you are not using fetch, and instead using an ORM or database directly, you can wrap your data access with the React cache function.

Warning: The content below assumes the cacheComponents conf

*[Content truncated - see full docs]*

**Examples**:

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

```python
import Posts from '@/app/ui/posts'
import { Suspense } from 'react'
 
export default function Page() {
  // Don't await the data fetching function
  const posts = getPosts()
 
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <Posts posts={posts} />
    </Suspense>
  )
}
```

---

## Getting Started: Font Optimization | Next.js

**URL**: https://nextjs.org/docs/app/getting-started/fonts

**Contents**:
- Font Optimization
- Google fonts
- Local fonts
- API Reference
  - Font

Features available in /app

The next/font module automatically optimizes your fonts and removes external network requests for improved privacy and performance.

It includes built-in self-hosting for any font file. This means you can optimally load web fonts with no layout shift.

To start using next/font, import it from next/font/local or next/font/google, call it as a function with the appropriate options, and set the className of the element you want to apply the font to. For example:

Fonts are scoped to the component they're used in. To apply a font to your entire application, add it to the Root Layout.

You can automatically self-host any Google Font. Fonts are included stored as static assets and served from the same domain as your deployment, meaning no requests are sent to Google by the browser when the user visits your site.

To start using a Google Font, import your chosen font from next/font/google:

We recommend using variable fonts for the best performance and flexibility. But if you can't use a variable font, you will need to specify a weight:

To use a local font, import your font from next/font/local and specify the src of your local font file. Fonts can be stored in the public folder or co-located inside the app folder. For example:

If you want to use multiple files for a single font family, src can be an array:

**Examples**:

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

```python
import { Roboto } from 'next/font/google'
 
const roboto = Roboto({
  weight: '400',
  subsets: ['latin'],
})
 
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className={roboto.className}>
      <body>{children}</body>
    </html>
  )
}
```

---

## Getting Started: Image Optimization | Next.js

**URL**: https://nextjs.org/docs/app/getting-started/images

**Contents**:
- Image Optimization
- Local images
- Remote images
- API Reference
  - Image Component

Features available in /app

The Next.js <Image> component extends the HTML <img> element to provide:

To start using <Image>, import it from next/image and render it within your component.

The src property can be a local or remote image.

🎥 Watch: Learn more about how to use next/image → YouTube (9 minutes).

You can store static files, like images and fonts, under a folder called public in the root directory. Files inside public can then be referenced by your code starting from the base URL (/).

If the image is statically imported, Next.js will automatically determine the intrinsic width and height. These values are used to determine the image ratio and prevent Cumulative Layout Shift while your image is loading.

To use a remote image, you can provide a URL string for the src property.

Since Next.js does not have access to remote files during the build process, you'll need to provide the width, height and optional blurDataURL props manually. The width and height are used to infer the correct aspect ratio of image and avoid layout shift from the image loading in. Alternatively, you can use the fill property to make the image fill the size of the parent element.

To safely allow images from remote servers, you need to define a list of supported URL patterns in next.config.js. Be as specific as possible to prevent malicious usage. For example, the following configuration will only allow images from a specific AWS S3 bucket:

**Examples**:

```python
import Image from 'next/image'
 
export default function Page() {
  return <Image src="" alt="" />
}
```

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

```python
import Image from 'next/image'
import ProfileImage from './profile.png'
 
export default function Page() {
  return (
    <Image
      src={ProfileImage}
      alt="Picture of the author"
      // width={500} automatically provided
      // height={500} automatically provided
      // blurDataURL="data:..." automatically provided
      // placeholder="blur" // Optional blur-up while loading
    />
  )
}
```

---

## Getting Started: Installation | Next.js

**URL**: https://nextjs.org/docs/app/getting-started/installation

**Contents**:
- Installation
- Quick start
- System requirements
- Create with the CLI
- Manual installation
  - Create the app directory
  - Create the public folder (optional)
- Run the development server

Features available in /app

Create a new Next.js app and run it locally.

Before you begin, make sure your system meets the following requirements:

The quickest way to create a new Next.js app is using create-next-app, which sets up everything automatically for you. To create a project, run:

On installation, you'll see the following prompts:

After the prompts, create-next-app will create a folder with your project name and install the required dependencies.

To manually create a new Next.js app, install the required packages:

Good to know: The App Router uses React canary releases built-in, which include all the stable React 19 changes, as well as newer features being validated in frameworks. The Pages Router uses the React version you install in package.json.

Then, add the following scripts to your package.json file:

These scripts refer to the different stages of developing an application:

Turbopack is stable for dev. For production builds, Turbopack is in beta. To try it, run next build --turbopack. See the Turbopack docs for status and caveats.

Next.js uses file-system routing, which means the routes in your application are determined by how you structure your files.

Create an app folder. Then, inside app, create a layout.tsx file. This file is the root layout. It's required and must contain the <html> and <body> tags.

Create a home page app/page.tsx with some initial content:

Both layout.tsx and page.tsx will be rendered when the user visits the root of your application (/).

Create a public folder at the root of your project to store static assets such as images, fonts, etc. Files inside public can then be referenced by your code starting from the base URL (/).

You can then reference these assets using the root path (/). For example, public/profile.png can be referenced as /profile.png:

Minimum TypeScript version: v4.5.2

Next.js comes with built-in TypeScript support. To add TypeScript to your project, rename a file to .ts / .tsx and run next dev.

*[Content truncated - see full docs]*

**Examples**:

```text
pnpm create next-app@latest my-app --yes
cd my-app
pnpm dev
```

```text
npx create-next-app@latest
```

```text
What is your project named? my-app
Would you like to use TypeScript? No / Yes
Would you like to use ESLint? No / Yes
Would you like to use Tailwind CSS? No / Yes
Would you like your code inside a `src/` directory? No / Yes
Would you like to use App Router? (recommended) No / Yes
Would you like to use Turbopack? (recommended) No / Yes
Would you like to customize the import alias (`@/*` by default)? No / Yes
What import alias would you like configured? @/*
```

---

## Getting Started: Layouts and Pages | Next.js

**URL**: https://nextjs.org/docs/app/getting-started/layouts-and-pages

**Contents**:
- Layouts and Pages
- Creating a page
- Creating a layout
- Creating a nested route
- Nesting layouts
- Creating a dynamic segment
- Rendering with search params
  - What to use and when

Features available in /app

Next.js uses file-system based routing, meaning you can use folders and files to define routes. This page will guide you through how to create layouts and pages, and link between them.

A page is UI that is rendered on a specific route. To create a page, add a page file inside the app directory and default export a React component. For example, to create an index page (/):

A layout is UI that is shared between multiple pages. On navigation, layouts preserve state, remain interactive, and do not rerender.

You can define a layout by default exporting a React component from a layout file. The component should accept a children prop which can be a page or another layout.

For example, to create a layout that accepts your index page as child, add a layout file inside the app directory:

The layout above is called a root layout because it's defined at the root of the app directory. The root layout is required and must contain html and body tags.

A nested route is a route composed of multiple URL segments. For example, the /blog/[slug] route is composed of three segments:

To create nested routes, you can nest folders inside each other. For example, to add a route for /blog, create a folder called blog in the app directory. Then, to make /blog publicly accessible, add a page.tsx file:

You can continue nesting folders to create nested routes. For example, to create a route for a specific blog post, create a new [slug] folder inside blog and add a page file:

Wrapping a folder name in square brackets (e.g. [slug]) creates a dynamic route segment which is used to generate multiple pages from data. e.g. blog posts, product pages, etc.

By default, layouts in the folder hierarchy are also nested, which means they wrap child layouts via their children prop. You can nest layouts by adding layout inside specific route segments (folders).

For example, to create a layout for the /blog route, add a new layout file inside the blog folder.

If you were 

*[Content truncated - see full docs]*

**Examples**:

```javascript
export default function Page() {
  return <h1>Hello Next.js!</h1>
}
```

```javascript
export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>
        {/* Layout UI */}
        {/* Place children where you want to render a page or nested layout */}
        <main>{children}</main>
      </body>
    </html>
  )
}
```

```python
// Dummy imports
import { getPosts } from '@/lib/posts'
import { Post } from '@/ui/post'
 
export default async function Page() {
  const posts = await getPosts()
 
  return (
    <ul>
      {posts.map((post) => (
        <Post key={post.id} post={post} />
      ))}
    </ul>
  )
}
```

---

## Getting Started: Linking and Navigating | Next.js

**URL**: https://nextjs.org/docs/app/getting-started/linking-and-navigating

**Contents**:
- Linking and Navigating
- How navigation works
  - Server Rendering
  - Prefetching
  - Streaming
  - Client-side transitions
- What can make transitions slow?
  - Dynamic routes without loading.tsx

Features available in /app

In Next.js, routes are rendered on the server by default. This often means the client has to wait for a server response before a new route can be shown. Next.js comes with built-in prefetching, streaming, and client-side transitions ensuring navigation stays fast and responsive.

This guide explains how navigation works in Next.js and how you can optimize it for dynamic routes and slow networks.

To understand how navigation works in Next.js, it helps to be familiar with the following concepts:

In Next.js, Layouts and Pages are React Server Components by default. On initial and subsequent navigations, the Server Component Payload is generated on the server before being sent to the client.

There are two types of server rendering, based on when it happens:

The trade-off of server rendering is that the client must wait for the server to respond before the new route can be shown. Next.js addresses this delay by prefetching routes the user is likely to visit and performing client-side transitions.

Good to know: HTML is also generated for the initial visit.

Prefetching is the process of loading a route in the background before the user navigates to it. This makes navigation between routes in your application feel instant, because by the time a user clicks on a link, the data to render the next route is already available client side.

Next.js automatically prefetches routes linked with the <Link> component when they enter the user's viewport.

How much of the route is prefetched depends on whether it's static or dynamic:

By skipping or partially prefetching dynamic routes, Next.js avoids unnecessary work on the server for routes the users may never visit. However, waiting for a server response before navigation can give the users the impression that the app is not responding.

To improve the navigation experience to dynamic routes, you can use streaming.

Streaming allows the server to send parts of a dynamic route to the client as soon as

*[Content truncated - see full docs]*

**Examples**:

```python
import Link from 'next/link'
 
export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <html>
      <body>
        <nav>
          {/* Prefetched when the link is hovered or enters the viewport */}
          <Link href="/blog">Blog</Link>
          {/* No prefetching */}
          <a href="/contact">Contact</a>
        </nav>
        {children}
      </body>
    </html>
  )
}
```

```javascript
export default function Loading() {
  // Add fallback UI that will be shown while the route is loading.
  return <LoadingSkeleton />
}
```

```javascript
export default function Loading() {
  return <LoadingSkeleton />
}
```

---

## Getting Started: Metadata and OG images | Next.js

**URL**: https://nextjs.org/docs/app/getting-started/metadata-and-og-images

**Contents**:
- Metadata and OG images
- Default fields
- Static metadata
- Generated metadata
  - Streaming metadata
  - Memoizing data requests
- File-based metadata
- Favicons

Features available in /app

The Metadata APIs can be used to define your application metadata for improved SEO and web shareability and include:

With all the options above, Next.js will automatically generate the relevant <head> tags for your page, which can be inspected in the browser's developer tools.

The metadata object and generateMetadata function exports are only supported in Server Components.

There are two default meta tags that are always added even if a route doesn't define metadata:

The other metadata fields can be defined with the Metadata object (for static metadata) or the generateMetadata function (for generated metadata).

To define static metadata, export a Metadata object from a static layout.js or page.js file. For example, to add a title and description to the blog route:

You can view a full list of available options, in the generateMetadata documentation.

You can use generateMetadata function to fetch metadata that depends on data. For example, to fetch the title and description for a specific blog post:

For dynamically rendered pages, Next.js streams metadata separately, injecting it into the HTML once generateMetadata resolves, without blocking UI rendering.

Streaming metadata improves perceived performance by allowing visual content to stream first.

Streaming metadata is disabled for bots and crawlers that expect metadata to be in the <head> tag (e.g. Twitterbot, Slackbot, Bingbot). These are detected by using the User Agent header from the incoming request.

You can customize or disable streaming metadata completely, with the htmlLimitedBots option in your Next.js config file.

Statically rendered pages don’t use streaming since metadata is resolved at build time.

Learn more about streaming metadata.

There may be cases where you need to fetch the same data for metadata and the page itself. To avoid duplicate requests, you can use React's cache function to memoize the return value and only fetch the data once. For example, to fetc

*[Content truncated - see full docs]*

**Examples**:

```text
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
```

```python
import type { Metadata } from 'next'
 
export const metadata: Metadata = {
  title: 'My Blog',
  description: '...',
}
 
export default function Layout() {}
```

```python
import type { Metadata, ResolvingMetadata } from 'next'
 
type Props = {
  params: Promise<{ slug: string }>
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>
}
 
export async function generateMetadata(
  { params, searchParams }: Props,
  parent: ResolvingMetadata
): Promise<Metadata> {
  const slug = (await params).slug
 
  // fetch post information
  const post = await fetch(`https://api.vercel.app/blog/${slug}`).then((res) =>
    res.json()
  )
 
  return {
    title:
...
```

---

## Getting Started: Partial Prerendering | Next.js

**URL**: https://nextjs.org/docs/app/getting-started/partial-prerendering

**Contents**:
- Partial Prerendering
- How does Partial Prerendering work?
  - Static Rendering
  - Dynamic Rendering
  - Suspense
  - Streaming
- Enabling Partial Prerendering
- Examples

Features available in /app

Partial Prerendering (PPR) is a rendering strategy that allows you to combine static and dynamic content in the same route. This improves the initial page performance while still supporting personalized, dynamic data.

When a user visits a route:

🎥 Watch: Why PPR and how it works → YouTube (10 minutes).

To understand Partial Prerendering, it helps to be familiar with the rendering strategies available in Next.js.

With Static Rendering, HTML is generated ahead of time—either at build time or through revalidation. The result is cached and shared across users and requests.

In Partial Prerendering, Next.js prerenders a static shell for a route. This can include the layout and any other components that don't depend on request-time data.

With Dynamic Rendering, HTML is generated at request time. This allows you to serve personalized content based on request-time data.

A component becomes dynamic if it uses the following APIs:

In Partial Prerendering, using these APIs throws a special React error that informs Next.js the component cannot be statically rendered, causing a build error. You can use a Suspense boundary to wrap your component to defer rendering until runtime.

React Suspense is used to defer rendering parts of your application until some condition is met.

In Partial Prerendering, Suspense is used to mark dynamic boundaries in your component tree.

At build time, Next.js prerenders the static content and the fallback UI. The dynamic content is postponed until the user requests the route.

Wrapping a component in Suspense doesn't make the component itself dynamic (your API usage does), but rather Suspense is used as a boundary that encapsulates dynamic content and enable streaming

Streaming splits the route into chunks and progressively streams them to the client as they become ready. This allows the user to see parts of the page immediately, before the entire content has finished rendering.

In Partial Prerendering, dynamic c

*[Content truncated - see full docs]*

**Examples**:

```python
import { Suspense } from 'react'
import StaticComponent from './StaticComponent'
import DynamicComponent from './DynamicComponent'
import Fallback from './Fallback'
 
export const experimental_ppr = true
 
export default function Page() {
  return (
    <>
      <StaticComponent />
      <Suspense fallback={<Fallback />}>
        <DynamicComponent />
      </Suspense>
    </>
  )
}
```

```python
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  experimental: {
    ppr: 'incremental',
  },
}
 
export default nextConfig
```

```javascript
export const experimental_ppr = true
 
export default function Layout({ children }: { children: React.ReactNode }) {
  // ...
}
```

---

## Getting Started: Project Structure | Next.js

**URL**: https://nextjs.org/docs/app/getting-started/project-structure

**Contents**:
- Project structure and organization
- Folder and file conventions
  - Top-level folders
  - Top-level files
  - Routing Files
  - Nested routes
  - Dynamic routes
  - Route Groups and private folders

Features available in /app

This page provides an overview of all the folder and file conventions in Next.js, and recommendations for organizing your project.

Top-level folders are used to organize your application's code and static assets.

Top-level files are used to configure your application, manage dependencies, run middleware, integrate monitoring tools, and define environment variables.

Add page to expose a route, layout for shared UI such as header, nav, or footer, loading for skeletons, error for error boundaries and route for APIs.

Folders define URL segments. Nesting folders nests segments. Layouts at any level wrap their child segments. A route becomes public when a page or route file exists.

Parameterize segments with square brackets. Use [segment] for a single param, [...segment] for catch‑all, and [[...segment]] for optional catch‑all. Access values via the params prop.

Organize code without changing URLs with route groups (group), and colocate non-routable files with private folders _folder.

These features fit specific UI patterns, such as slot-based layouts or modal routing.

Use @slot for named slots rendered by a parent layout. Use intercept patterns to render another route inside the current layout without changing the URL, for example, to show a details view as a modal over a list.

Next.js is unopinionated about how you organize and colocate your project files. But it does provide several features to help you organize your project.

The components defined in special files are rendered in a specific hierarchy:

The components are rendered recursively in nested routes, meaning the components of a route segment will be nested inside the components of its parent segment.

In the app directory, nested folders define route structure. Each folder represents a route segment that is mapped to a corresponding segment in a URL path.

However, even though route structure is defined through folders, a route is not publicly accessible until a page.js o

*[Content truncated - see full docs]*

---

## Getting Started: Route Handlers and Middleware | Next.js

**URL**: https://nextjs.org/docs/app/getting-started/route-handlers-and-middleware

**Contents**:
- Route Handlers and Middleware
- Route Handlers
  - Convention
  - Supported HTTP Methods
  - Extended NextRequest and NextResponse APIs
  - Caching
  - Special Route Handlers
  - Route Resolution

Features available in /app

Route Handlers allow you to create custom request handlers for a given route using the Web Request and Response APIs.

Good to know: Route Handlers are only available inside the app directory. They are the equivalent of API Routes inside the pages directory meaning you do not need to use API Routes and Route Handlers together.

Route Handlers are defined in a route.js|ts file inside the app directory:

Route Handlers can be nested anywhere inside the app directory, similar to page.js and layout.js. But there cannot be a route.js file at the same route segment level as page.js.

The following HTTP methods are supported: GET, POST, PUT, PATCH, DELETE, HEAD, and OPTIONS. If an unsupported method is called, Next.js will return a 405 Method Not Allowed response.

In addition to supporting the native Request and Response APIs, Next.js extends them with NextRequest and NextResponse to provide convenient helpers for advanced use cases.

Route Handlers are not cached by default. You can, however, opt into caching for GET methods. Other supported HTTP methods are not cached. To cache a GET method, use a route config option such as export const dynamic = 'force-static' in your Route Handler file.

Good to know: Other supported HTTP methods are not cached, even if they are placed alongside a GET method that is cached, in the same file.

Special Route Handlers like sitemap.ts, opengraph-image.tsx, and icon.tsx, and other metadata files remain static by default unless they use Dynamic APIs or dynamic config options.

You can consider a route the lowest level routing primitive.

Each route.js or page.js file takes over all HTTP verbs for that route.

Read more about how Route Handlers complement your frontend application, or explore the Route Handlers API Reference.

In TypeScript, you can type the context parameter for Route Handlers with the globally available RouteContext helper:

Middleware allows you to run code before a request is completed. Then,

*[Content truncated - see full docs]*

**Examples**:

```javascript
export async function GET(request: Request) {}
```

```javascript
export const dynamic = 'force-static'
 
export async function GET() {
  const res = await fetch('https://data.mongodb-api.com/...', {
    headers: {
      'Content-Type': 'application/json',
      'API-Key': process.env.DATA_API_KEY,
    },
  })
  const data = await res.json()
 
  return Response.json({ data })
}
```

```javascript
export default function Page() {
  return <h1>Hello, Next.js!</h1>
}
 
// Conflict
// `app/route.ts`
export async function POST(request: Request) {}
```

---

## Getting Started: Server and Client Components | Next.js

**URL**: https://nextjs.org/docs/app/getting-started/server-and-client-components

**Contents**:
- Server and Client Components
- When to use Server and Client Components?
- How do Server and Client Components work in Next.js?
  - On the server
  - On the client (first load)
  - Subsequent Navigations
- Examples
  - Using Client Components

Features available in /app

By default, layouts and pages are Server Components, which lets you fetch data and render parts of your UI on the server, optionally cache the result, and stream it to the client. When you need interactivity or browser APIs, you can use Client Components to layer in functionality.

This page explains how Server and Client Components work in Next.js and when to use them, with examples of how to compose them together in your application.

The client and server environments have different capabilities. Server and Client components allow you to run logic in each environment depending on your use case.

Use Client Components when you need:

Use Server Components when you need:

For example, the <Page> component is a Server Component that fetches data about a post, and passes it as props to the <LikeButton> which handles client-side interactivity.

On the server, Next.js uses React's APIs to orchestrate rendering. The rendering work is split into chunks, by individual route segments (layouts and pages):

What is the React Server Component Payload (RSC)?

The RSC Payload is a compact binary representation of the rendered React Server Components tree. It's used by React on the client to update the browser's DOM. The RSC Payload contains:

Hydration is React's process for attaching event handlers to the DOM, to make the static HTML interactive.

On subsequent navigations:

You can create a Client Component by adding the "use client" directive at the top of the file, above your imports.

"use client" is used to declare a boundary between the Server and Client module graphs (trees).

Once a file is marked with "use client", all its imports and child components are considered part of the client bundle. This means you don't need to add the directive to every component that is intended for the client.

To reduce the size of your client JavaScript bundles, add 'use client' to specific interactive components instead of marking large parts of your UI as C

*[Content truncated - see full docs]*

**Examples**:

```python
import LikeButton from '@/app/ui/like-button'
import { getPost } from '@/lib/data'
 
export default async function Page({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params
  const post = await getPost(id)
 
  return (
    <div>
      <main>
        <h1>{post.title}</h1>
        {/* ... */}
        <LikeButton likes={post.likes} />
      </main>
    </div>
  )
}
```

```python
'use client'
 
import { useState } from 'react'
 
export default function LikeButton({ likes }: { likes: number }) {
  // ...
}
```

```python
'use client'
 
import { useState } from 'react'
 
export default function Counter() {
  const [count, setCount] = useState(0)
 
  return (
    <div>
      <p>{count} likes</p>
      <button onClick={() => setCount(count + 1)}>Click me</button>
    </div>
  )
}
```

---

## Getting Started: Updating Data | Next.js

**URL**: https://nextjs.org/docs/app/getting-started/updating-data

**Contents**:
- Updating Data
- What are Server Functions?
- Creating Server Functions
  - Server Components
  - Client Components
  - Passing actions as props
- Invoking Server Functions
  - Forms

Features available in /app

You can update data in Next.js using React's Server Functions. This page will go through how you can create and invoke Server Functions.

A Server Function is an asynchronous function that runs on the server. They can be called from client through a network request, which is why they must be asynchronous.

In an action or mutation context, they are also called Server Actions.

By convention, a Server Action is an async function used with startTransition. This happens automatically when the function is:

In Next.js, Server Actions integrate with the framework's caching architecture. When an action is invoked, Next.js can return both the updated UI and new data in a single server roundtrip.

Behind the scenes, actions use the POST method, and only this HTTP method can invoke them.

A Server Function can be defined by using the use server directive. You can place the directive at the top of an asynchronous function to mark the function as a Server Function, or at the top of a separate file to mark all exports of that file.

Server Functions can be inlined in Server Components by adding the "use server" directive to the top of the function body:

Good to know: Server Components support progressive enhancement by default, meaning forms that call Server Actions will be submitted even if JavaScript hasn't loaded yet or is disabled.

It's not possible to define Server Functions in Client Components. However, you can invoke them in Client Components by importing them from a file that has the "use server" directive at the top of it:

Good to know: In Client Components, forms invoking Server Actions will queue submissions if JavaScript isn't loaded yet, and will be prioritized for hydration. After hydration, the browser does not refresh on form submission.

You can also pass an action to a Client Component as a prop:

There are two main ways you can invoke a Server Function:

Good to know: Server Functions are designed for server-side mutations. The

*[Content truncated - see full docs]*

**Examples**:

```javascript
export async function createPost(formData: FormData) {
  'use server'
  const title = formData.get('title')
  const content = formData.get('content')
 
  // Update data
  // Revalidate cache
}
 
export async function deletePost(formData: FormData) {
  'use server'
  const id = formData.get('id')
 
  // Update data
  // Revalidate cache
}
```

```javascript
export default function Page() {
  // Server Action
  async function createPost(formData: FormData) {
    'use server'
    // ...
  }
 
  return <></>
}
```

```javascript
'use server'
 
export async function createPost() {}
```

---

## Getting Started: Upgrading | Next.js

**URL**: https://nextjs.org/docs/app/getting-started/upgrading

**Contents**:
- Upgrading
- Latest version
- Canary version
  - Features available in canary
- Version guides
  - Version 15
  - Version 14

Features available in /app

To update to the latest version of Next.js, you can use the upgrade codemod:

If you prefer to upgrade manually, install the latest Next.js and React versions:

To update to the latest canary, make sure you're on the latest version of Next.js and everything is working as expected. Then, run the following command:

The following features are currently available in canary:

**Examples**:

```text
npx @next/codemod@latest upgrade latest
```

```text
pnpm i next@latest react@latest react-dom@latest eslint-config-next@latest
```

```text
npm i next@canary
```

---
