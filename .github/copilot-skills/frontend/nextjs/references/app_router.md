# Nextjs - App Router

**Pages**: 181

---

## API Reference: Components | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/components

**Contents**:
- Components
  - Font
  - Form Component
  - Image Component
  - Link Component
  - Script Component

Features available in /app

---

## API Reference: Configuration | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config

**Contents**:
- Configuration
  - next.config.js
  - TypeScript
  - ESLint

Features available in /app

---

## API Reference: Directives | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/directives

**Contents**:
- Directives
  - use cache
  - use client
  - use server

Features available in /app

The following directives are available:

---

## API Reference: File-system conventions | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/file-conventions

**Contents**:
- File-system conventions
  - default.js
  - Dynamic Segments
  - error.js
  - forbidden.js
  - instrumentation.js
  - instrumentation-client.js
  - Intercepting Routes

Features available in /app

---

## API Reference: Functions | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/functions

**Contents**:
- Functions
  - after
  - cacheLife
  - cacheTag
  - connection
  - cookies
  - draftMode
  - fetch

Features available in /app

---

## App Router: API Reference | Next.js

**URL**: https://nextjs.org/docs/app/api-reference

**Contents**:
- API Reference
  - Directives
  - Components
  - File-system conventions
  - Functions
  - Configuration
  - CLI
  - Edge Runtime

Features available in /app

---

## App Router: Guides | Next.js

**URL**: https://nextjs.org/docs/app/guides

**Contents**:
- Guides
  - Analytics
  - Authentication
  - Backend for Frontend
  - Caching
  - CI Build Caching
  - Content Security Policy
  - CSS-in-JS

Features available in /app

---

## Components: Font | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/components/font

**Contents**:
- Font Module
- Reference
  - src
  - weight
  - style
  - subsets
  - axes
  - display

Features available in /app

next/font automatically optimizes your fonts (including custom fonts) and removes external network requests for improved privacy and performance.

It includes built-in automatic self-hosting for any font file. This means you can optimally load web fonts with no layout shift.

You can also conveniently use all Google Fonts. CSS and font files are downloaded at build time and self-hosted with the rest of your static assets. No requests are sent to Google by the browser.

🎥 Watch: Learn more about using next/font → YouTube (6 minutes).

The path of the font file as a string or an array of objects (with type Array<{path: string, weight?: string, style?: string}>) relative to the directory where the font loader function is called.

Used in next/font/local

The font weight with the following possibilities:

Used in next/font/google and next/font/local

The font style with the following possibilities:

Used in next/font/google and next/font/local

The font subsets defined by an array of string values with the names of each subset you would like to be preloaded. Fonts specified via subsets will have a link preload tag injected into the head when the preload option is true, which is the default.

Used in next/font/google

You can find a list of all subsets on the Google Fonts page for your font.

Some variable fonts have extra axes that can be included. By default, only the font weight is included to keep the file size down. The possible values of axes depend on the specific font.

Used in next/font/google

The font display with possible string values of 'auto', 'block', 'swap', 'fallback' or 'optional' with default value of 'swap'.

Used in next/font/google and next/font/local

A boolean value that specifies whether the font should be preloaded or not. The default is true.

Used in next/font/google and next/font/local

The fallback font to use if the font cannot be loaded. An array of strings of fallback fonts with no default.

Used in next/font/

*[Content truncated - see full docs]*

**Examples**:

```python
import { Inter } from 'next/font/google'
 
// If loading a variable font, you don't need to specify the font weight
const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
})
 
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className={inter.className}>
      <body>{children}</body>
    </html>
  )
}
```

```python
import { Inter } from 'next/font/google'
 
// If loading a variable font, you don't need to specify the font weight
const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
})
 
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className={inter.className}>
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
  display: 'swap',
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

## Components: Form Component | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/components/form

**Contents**:
- Form Component
- Reference
  - action (string) Props
  - action (function) Props
  - Caveats
- Examples
  - Search form that leads to a search result page
  - Mutations with Server Actions

Features available in /app

The <Form> component extends the HTML <form> element to provide prefetching of loading UI, client-side navigation on submission, and progressive enhancement.

It's useful for forms that update URL search params as it reduces the boilerplate code needed to achieve the above.

The behavior of the <Form> component depends on whether the action prop is passed a string or function.

When action is a string, the <Form> component supports the following props:

When action is a function, the <Form> component supports the following prop:

Good to know: When action is a function, the replace and scroll props are ignored.

You can create a search form that navigates to a search results page by passing the path as an action:

When the user updates the query input field and submits the form, the form data will be encoded into the URL as search params, e.g. /search?query=abc.

Good to know: If you pass an empty string "" to action, the form will navigate to the same route with updated search params.

On the results page, you can access the query using the searchParams page.js prop and use it to fetch data from an external source.

When the <Form> becomes visible in the user's viewport, shared UI (such as layout.js and loading.js) on the /search page will be prefetched. On submission, the form will immediately navigate to the new route and show loading UI while the results are being fetched. You can design the fallback UI using loading.js:

To cover cases when shared UI hasn't yet loaded, you can show instant feedback to the user using useFormStatus.

First, create a component that displays a loading state when the form is pending:

Then, update the search form page to use the SearchButton component:

You can perform mutations by passing a function to the action prop.

After a mutation, it's common to redirect to the new resource. You can use the redirect function from next/navigation to navigate to the new post page.

Good to know: Since the "destinati

*[Content truncated - see full docs]*

**Examples**:

```python
import Form from 'next/form'
 
export default function Page() {
  return (
    <Form action="/search">
      {/* On submission, the input value will be appended to
          the URL, e.g. /search?query=abc */}
      <input name="query" />
      <button type="submit">Submit</button>
    </Form>
  )
}
```

```python
import Form from 'next/form'
 
export default function Page() {
  return (
    <Form action="/search">
      <input name="query" />
      <button type="submit">Submit</button>
    </Form>
  )
}
```

```python
import { getSearchResults } from '@/lib/search'
 
export default async function SearchPage({
  searchParams,
}: {
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>
}) {
  const results = await getSearchResults((await searchParams).query)
 
  return <div>...</div>
}
```

---

## Components: Image Component | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/components/image

**Contents**:
- Image Component
- Reference
  - Props
    - src
    - alt
    - width and height
    - fill
    - loader

Features available in /app

The Next.js Image component extends the HTML <img> element for automatic image optimization.

The following props are available:

The source of the image. Can be one of the following:

An internal path string.

An absolute external URL (must be configured with remotePatterns).

Good to know: For security reasons, the Image Optimization API using the default loader will not forward headers when fetching the src image. If the src image requires authentication, consider using the unoptimized property to disable Image Optimization.

The alt property is used to describe the image for screen readers and search engines. It is also the fallback text if images have been disabled or an error occurs while loading the image.

It should contain text that could replace the image without changing the meaning of the page. It is not meant to supplement the image and should not repeat information that is already provided in the captions above or below the image.

If the image is purely decorative or not intended for the user, the alt property should be an empty string (alt="").

Learn more about image accessibility guidelines.

The width and height properties represent the intrinsic image size in pixels. This property is used to infer the correct aspect ratio used by browsers to reserve space for the image and avoid layout shift during loading. It does not determine the rendered size of the image, which is controlled by CSS.

You must set both width and height properties unless:

If the height and width are unknown, we recommend using the fill property.

A boolean that causes the image to expand to the size of the parent element.

If no styles are applied to the image, the image will stretch to fit the container. You can use objectFit to control cropping and scaling.

Learn more about position and object-fit.

A custom function used to generate the image URL. The function receives the following parameters, and returns a URL string for the image:

Good to k

*[Content truncated - see full docs]*

**Examples**:

```python
import Image from 'next/image'
 
export default function Page() {
  return (
    <Image
      src="/profile.png"
      width={500}
      height={500}
      alt="Picture of the author"
    />
  )
}
```

```text
<Image src="/profile.png" />
```

```text
<Image src="https://example.com/profile.png" />
```

---

## Components: Link Component | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/components/link

**Contents**:
- Link Component
- Reference
  - href (required)
  - replace
  - scroll
  - prefetch
  - onNavigate
- Examples

Features available in /app

<Link> is a React component that extends the HTML <a> element to provide prefetching and client-side navigation between routes. It is the primary way to navigate between routes in Next.js.

The following props can be passed to the <Link> component:

Good to know: <a> tag attributes such as className or target="_blank" can be added to <Link> as props and will be passed to the underlying <a> element.

The path or URL to navigate to.

Defaults to false. When true, next/link will replace the current history state instead of adding a new URL into the browser's history stack.

Defaults to true. The default scrolling behavior of <Link> in Next.js is to maintain scroll position, similar to how browsers handle back and forwards navigation. When you navigate to a new Page, scroll position will stay the same as long as the Page is visible in the viewport. However, if the Page is not visible in the viewport, Next.js will scroll to the top of the first Page element.

When scroll = {false}, Next.js will not attempt to scroll to the first Page element.

Good to know: Next.js checks if scroll: false before managing scroll behavior. If scrolling is enabled, it identifies the relevant DOM node for navigation and inspects each top-level element. All non-scrollable elements and those without rendered HTML are bypassed, this includes sticky or fixed positioned elements, and non-visible elements such as those calculated with getBoundingClientRect. Next.js then continues through siblings until it identifies a scrollable element that is visible in the viewport.

Prefetching happens when a <Link /> component enters the user's viewport (initially or through scroll). Next.js prefetches and loads the linked route (denoted by the href) and its data in the background to improve the performance of client-side navigations. If the prefetched data has expired by the time the user hovers over a <Link />, Next.js will attempt to prefetch it again. Prefetching is only enable

*[Content truncated - see full docs]*

**Examples**:

```python
import Link from 'next/link'
 
export default function Page() {
  return <Link href="/dashboard">Dashboard</Link>
}
```

```python
import Link from 'next/link'
 
// Navigate to /about?name=test
export default function Page() {
  return (
    <Link
      href={{
        pathname: '/about',
        query: { name: 'test' },
      }}
    >
      About
    </Link>
  )
}
```

```python
import Link from 'next/link'
 
export default function Page() {
  return (
    <Link href="/dashboard" replace>
      Dashboard
    </Link>
  )
}
```

---

## Components: Script Component | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/components/script

**Contents**:
- Script Component
- Props
- Required Props
  - src
- Optional Props
  - strategy
  - beforeInteractive
  - afterInteractive

Features available in /app

This API reference will help you understand how to use props available for the Script Component. For features and usage, please see the Optimizing Scripts page.

Here's a summary of the props available for the Script Component:

The <Script /> component requires the following properties.

A path string specifying the URL of an external script. This can be either an absolute external URL or an internal path. The src property is required unless an inline script is used.

The <Script /> component accepts a number of additional properties beyond those which are required.

The loading strategy of the script. There are four different strategies that can be used:

Scripts that load with the beforeInteractive strategy are injected into the initial HTML from the server, downloaded before any Next.js module, and executed in the order they are placed.

Scripts denoted with this strategy are preloaded and fetched before any first-party code, but their execution does not block page hydration from occurring.

beforeInteractive scripts must be placed inside the root layout (app/layout.tsx) and are designed to load scripts that are needed by the entire site (i.e. the script will load when any page in the application has been loaded server-side).

This strategy should only be used for critical scripts that need to be fetched as soon as possible.

Good to know: Scripts with beforeInteractive will always be injected inside the head of the HTML document regardless of where it's placed in the component.

Some examples of scripts that should be fetched as soon as possible with beforeInteractive include:

Scripts that use the afterInteractive strategy are injected into the HTML client-side and will load after some (or all) hydration occurs on the page. This is the default strategy of the Script component and should be used for any script that needs to load as soon as possible but not before any first-party Next.js code.

afterInteractive scripts can be placed i

*[Content truncated - see full docs]*

**Examples**:

```python
import Script from 'next/script'
 
export default function Dashboard() {
  return (
    <>
      <Script src="https://example.com/script.js" />
    </>
  )
}
```

```python
import Script from 'next/script'
 
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>
        {children}
        <Script
          src="https://example.com/script.js"
          strategy="beforeInteractive"
        />
      </body>
    </html>
  )
}
```

```python
import Script from 'next/script'
 
export default function Page() {
  return (
    <>
      <Script src="https://example.com/script.js" strategy="afterInteractive" />
    </>
  )
}
```

---

## Configuration: next.config.js | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js

**Contents**:
- next.config.js
- ECMAScript Modules
- Configuration as a Function
  - Async Configuration
  - Phase
- TypeScript
- Unit Testing (experimental)
  - allowedDevOrigins

Features available in /app

Next.js can be configured through a next.config.js file in the root of your project directory (for example, by package.json) with a default export.

next.config.js is a regular Node.js module, not a JSON file. It gets used by the Next.js server and build phases, and it's not included in the browser build.

If you need ECMAScript modules, you can use next.config.mjs:

Good to know: next.config with the .cjs, .cts, or .mts extensions are currently not supported.

You can also use a function:

Since Next.js 12.1.0, you can use an async function:

phase is the current context in which the configuration is loaded. You can see the available phases. Phases can be imported from next/constants:

If you are using TypeScript in your project, you can use next.config.ts to use TypeScript in your configuration:

The commented lines are the place where you can put the configs allowed by next.config.js, which are defined in this file.

However, none of the configs are required, and it's not necessary to understand what each config does. Instead, search for the features you need to enable or modify in this section and they will show you what to do.

Avoid using new JavaScript features not available in your target Node.js version. next.config.js will not be parsed by Webpack or Babel.

This page documents all the available configuration options:

Starting in Next.js 15.1, the next/experimental/testing/server package contains utilities to help unit test next.config.js files.

The unstable_getResponseFromNextConfig function runs the headers, redirects, and rewrites functions from next.config.js with the provided request information and returns NextResponse with the results of the routing.

The response from unstable_getResponseFromNextConfig only considers next.config.js fields and does not consider middleware or filesystem routes, so the result in production may be different than the unit test.

**Examples**:

```javascript
// @ts-check
 
/** @type {import('next').NextConfig} */
const nextConfig = {
  /* config options here */
}
 
module.exports = nextConfig
```

```javascript
// @ts-check
 
/**
 * @type {import('next').NextConfig}
 */
const nextConfig = {
  /* config options here */
}
 
export default nextConfig
```

```javascript
// @ts-check
 
export default (phase, { defaultConfig }) => {
  /**
   * @type {import('next').NextConfig}
   */
  const nextConfig = {
    /* config options here */
  }
  return nextConfig
}
```

---

## Directives: use cache | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/directives/use-cache

**Contents**:
- use cache
- Usage
- How use cache works
  - Cache keys
- Non-serializable arguments
- Return values
- use cache at build time
- use cache at runtime

Features available in /app

The use cache directive allows you to mark a route, React component, or a function as cacheable. It can be used at the top of a file to indicate that all exports in the file should be cached, or inline at the top of function or component to cache the return value.

use cache is currently an experimental feature. To enable it, add the useCache option to your next.config.ts file:

Good to know: use cache can also be enabled with the cacheComponents option.

Then, add use cache at the file, component, or function level:

A cache entry's key is generated using a serialized version of its inputs, which includes:

The arguments passed to the cached function, as well as any values it reads from the parent scope automatically become a part of the key. This means, the same cache entry will be reused as long as its inputs are the same.

Any non-serializable arguments, props, or closed-over values will turn into references inside the cached function, and can be only passed through and not inspected nor modified. These non-serializable values will be filled in at the request time and won't become a part of the cache key.

For example, a cached function can take in JSX as a children prop and return <div>{children}</div>, but it won't be able to introspect the actual children object. This allows you to nest uncached content inside a cached component.

The return value of the cacheable function must be serializable. This ensures that the cached data can be stored and retrieved correctly.

When used at the top of a layout or page, the route segment will be prerendered, allowing it to later be revalidated.

This means use cache cannot be used with request-time APIs like cookies or headers.

On the server, the cache entries of individual components or functions will be cached in-memory.

Then, on the client, any content returned from the server cache will be stored in the browser's memory for the duration of the session or until revalidated.

By default, u

*[Content truncated - see full docs]*

**Examples**:

```python
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  experimental: {
    useCache: true,
  },
}
 
export default nextConfig
```

```javascript
// File level
'use cache'
 
export default async function Page() {
  // ...
}
 
// Component level
export async function MyComponent() {
  'use cache'
  return <></>
}
 
// Function level
export async function getData() {
  'use cache'
  const data = await fetch('/api/data')
  return data
}
```

```javascript
function CachedComponent({ children }: { children: ReactNode }) {
  'use cache'
  return <div>{children}</div>
}
```

---

## Directives: use client | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/directives/use-client

**Contents**:
- use client
- Usage
- Nesting Client Components within Server Components
- Reference

Features available in /app

The 'use client' directive declares an entry point for the components to be rendered on the client side and should be used when creating interactive user interfaces (UI) that require client-side JavaScript capabilities, such as state management, event handling, and access to browser APIs. This is a React feature.

You do not need to add the 'use client' directive to every file that contains Client Components. You only need to add it to the files whose components you want to render directly within Server Components. The 'use client' directive defines the client-server boundary, and the components exported from such a file serve as entry points to the client.

To declare an entry point for the Client Components, add the 'use client' directive at the top of the file, before any imports:

When using the 'use client' directive, the props of the Client Components must be serializable. This means the props need to be in a format that React can serialize when sending data from the server to the client.

Combining Server and Client Components allows you to build applications that are both performant and interactive:

In the following example:

See the React documentation for more information on 'use client'.

**Examples**:

```python
'use client'
 
import { useState } from 'react'
 
export default function Counter() {
  const [count, setCount] = useState(0)
 
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  )
}
```

```javascript
'use client'
 
export default function Counter({
  onClick /* ❌ Function is not serializable */,
}) {
  return (
    <div>
      <button onClick={onClick}>Increment</button>
    </div>
  )
}
```

```python
import Header from './header'
import Counter from './counter' // This is a Client Component
 
export default function Page() {
  return (
    <div>
      <Header />
      <Counter />
    </div>
  )
}
```

---

## Directives: use server | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/directives/use-server

**Contents**:
- use server
- Using use server at the top of a file
  - Using Server Functions in a Client Component
- Using use server inline
- Security considerations
  - Authentication and authorization
- Reference

Features available in /app

The use server directive designates a function or file to be executed on the server side. It can be used at the top of a file to indicate that all functions in the file are server-side, or inline at the top of a function to mark the function as a Server Function. This is a React feature.

The following example shows a file with a use server directive at the top. All functions in the file are executed on the server.

To use Server Functions in Client Components you need to create your Server Functions in a dedicated file using the use server directive at the top of the file. These Server Functions can then be imported into Client and Server Components and executed.

Assuming you have a fetchUsers Server Function in actions.ts:

Then you can import the fetchUsers Server Function into a Client Component and execute it on the client-side.

In the following example, use server is used inline at the top of a function to mark it as a Server Function:

When using the use server directive, it's important to ensure that all server-side logic is secure and that sensitive data remains protected.

Always authenticate and authorize users before performing sensitive server-side operations.

See the React documentation for more information on use server.

**Examples**:

```python
'use server'
import { db } from '@/lib/db' // Your database client
 
export async function createUser(data: { name: string; email: string }) {
  const user = await db.user.create({ data })
  return user
}
```

```python
'use server'
import { db } from '@/lib/db' // Your database client
 
export async function fetchUsers() {
  const users = await db.user.findMany()
  return users
}
```

```python
'use client'
import { fetchUsers } from '../actions'
 
export default function MyButton() {
  return <button onClick={() => fetchUsers()}>Fetch Users</button>
}
```

---

## File-system conventions: Dynamic Segments | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes

**Contents**:
- Dynamic Route Segments
- Convention
  - In Client Components
  - Catch-all Segments
  - Optional Catch-all Segments
  - TypeScript
- Behavior
- Examples

Features available in /app

When you don't know the exact route segment names ahead of time and want to create routes from dynamic data, you can use Dynamic Segments that are filled in at request time or prerendered at build time.

A Dynamic Segment can be created by wrapping a folder's name in square brackets: [folderName]. For example, a blog could include the following route app/blog/[slug]/page.js where [slug] is the Dynamic Segment for blog posts.

Dynamic Segments are passed as the params prop to layout, page, route, and generateMetadata functions.

In a Client Component page, dynamic segments from props can be accessed using the use hook.

Alternatively Client Components can use the useParams hook to access the params anywhere in the Client Component tree.

Dynamic Segments can be extended to catch-all subsequent segments by adding an ellipsis inside the brackets [...folderName].

For example, app/shop/[...slug]/page.js will match /shop/clothes, but also /shop/clothes/tops, /shop/clothes/tops/t-shirts, and so on.

Catch-all Segments can be made optional by including the parameter in double square brackets: [[...folderName]].

For example, app/shop/[[...slug]]/page.js will also match /shop, in addition to /shop/clothes, /shop/clothes/tops, /shop/clothes/tops/t-shirts.

The difference between catch-all and optional catch-all segments is that with optional, the route without the parameter is also matched (/shop in the example above).

When using TypeScript, you can add types for params depending on your configured route segment — use PageProps<'/route'>, LayoutProps<'/route'>, or RouteContext<'/route'> to type params in page, layout, and route respectively.

Route params values are typed as string, string[], or undefined (for optional catch-all segments), because their values aren't known until runtime. Users can enter any URL into the address bar, and these broad types help ensure that your application code handles all these possible cases.

If you're working o

*[Content truncated - see full docs]*

**Examples**:

```javascript
export default async function Page({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = await params
  return <div>My Post: {slug}</div>
}
```

```python
'use client'
import { use } from 'react'
 
export default function BlogPostPage({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = use(params)
 
  return (
    <div>
      <p>{slug}</p>
    </div>
  )
}
```

```python
import { notFound } from 'next/navigation'
import type { Locale } from '@i18n/types'
import { isValidLocale } from '@i18n/utils'
 
function assertValidLocale(value: string): asserts value is Locale {
  if (!isValidLocale(value)) notFound()
}
 
export default async function Page(props: PageProps<'/[locale]'>) {
  const { locale } = await props.params // locale is typed as string
  assertValidLocale(locale)
  // locale is now typed as Locale
}
```

---

## File-system conventions: Intercepting Routes | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/file-conventions/intercepting-routes

**Contents**:
- Intercepting Routes
- Convention
- Examples
  - Modals
- Next Steps
  - Parallel Routes

Features available in /app

Intercepting routes allows you to load a route from another part of your application within the current layout. This routing paradigm can be useful when you want to display the content of a route without the user switching to a different context.

For example, when clicking on a photo in a feed, you can display the photo in a modal, overlaying the feed. In this case, Next.js intercepts the /photo/123 route, masks the URL, and overlays it over /feed.

However, when navigating to the photo by clicking a shareable URL or by refreshing the page, the entire photo page should render instead of the modal. No route interception should occur.

Intercepting routes can be defined with the (..) convention, which is similar to relative path convention ../ but for route segments.

For example, you can intercept the photo segment from within the feed segment by creating a (..)photo directory.

Good to know: The (..) convention is based on route segments, not the file-system. For example, it does not consider @slot folders in Parallel Routes.

Intercepting Routes can be used together with Parallel Routes to create modals. This allows you to solve common challenges when building modals, such as:

Consider the following UI pattern, where a user can open a photo modal from a gallery using client-side navigation, or navigate to the photo page directly from a shareable URL:

In the above example, the path to the photo segment can use the (..) matcher since @modal is a slot and not a segment. This means that the photo route is only one segment level higher, despite being two file-system levels higher.

See the Parallel Routes documentation for a step-by-step example, or see our image gallery example.

---

## File-system conventions: Metadata Files | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/file-conventions/metadata

**Contents**:
- Metadata Files API Reference
  - favicon, icon, and apple-icon
  - manifest.json
  - opengraph-image and twitter-image
  - robots.txt
  - sitemap.xml

Features available in /app

This section of the docs covers Metadata file conventions. File-based metadata can be defined by adding special metadata files to route segments.

Each file convention can be defined using a static file (e.g. opengraph-image.jpg), or a dynamic variant that uses code to generate the file (e.g. opengraph-image.js).

Once a file is defined, Next.js will automatically serve the file (with hashes in production for caching) and update the relevant head elements with the correct metadata, such as the asset's URL, file type, and image size.

---

## File-system conventions: Parallel Routes | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes

**Contents**:
- Parallel Routes
- Convention
  - Slots
  - default.js
- Behavior
- Examples
  - With useSelectedLayoutSegment(s)
  - Conditional Routes

Features available in /app

Parallel Routes allows you to simultaneously or conditionally render one or more pages within the same layout. They are useful for highly dynamic sections of an app, such as dashboards and feeds on social sites.

For example, considering a dashboard, you can use parallel routes to simultaneously render the team and analytics pages:

Parallel routes are created using named slots. Slots are defined with the @folder convention. For example, the following file structure defines two slots: @analytics and @team:

Slots are passed as props to the shared parent layout. For the example above, the component in app/layout.js now accepts the @analytics and @team slots props, and can render them in parallel alongside the children prop:

However, slots are not route segments and do not affect the URL structure. For example, for /@analytics/views, the URL will be /views since @analytics is a slot. Slots are combined with the regular Page component to form the final page associated with the route segment. Because of this, you cannot have separate static and dynamic slots at the same route segment level. If one slot is dynamic, all slots at that level must be dynamic.

You can define a default.js file to render as a fallback for unmatched slots during the initial load or full-page reload.

Consider the following folder structure. The @team slot has a /settings page, but @analytics does not.

When navigating to /settings, the @team slot will render the /settings page while maintaining the currently active page for the @analytics slot.

On refresh, Next.js will render a default.js for @analytics. If default.js doesn't exist, a 404 is rendered instead.

Additionally, since children is an implicit slot, you also need to create a default.js file to render a fallback for children when Next.js cannot recover the active state of the parent page.

By default, Next.js keeps track of the active state (or subpage) for each slot. However, the content rendered within a

*[Content truncated - see full docs]*

**Examples**:

```javascript
export default function Layout({
  children,
  team,
  analytics,
}: {
  children: React.ReactNode
  analytics: React.ReactNode
  team: React.ReactNode
}) {
  return (
    <>
      {children}
      {team}
      {analytics}
    </>
  )
}
```

```python
'use client'
 
import { useSelectedLayoutSegment } from 'next/navigation'
 
export default function Layout({ auth }: { auth: React.ReactNode }) {
  const loginSegment = useSelectedLayoutSegment('auth')
  // ...
}
```

```python
import { checkUserRole } from '@/lib/auth'
 
export default function Layout({
  user,
  admin,
}: {
  user: React.ReactNode
  admin: React.ReactNode
}) {
  const role = checkUserRole()
  return role === 'admin' ? admin : user
}
```

---

## File-system conventions: Route Groups | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/file-conventions/route-groups

**Contents**:
- Route Groups
- Convention
- Use cases
- Caveats

Features available in /app

Route Groups are a folder convention that let you organize routes by category or team.

A route group can be created by wrapping a folder's name in parenthesis: (folderName).

This convention indicates the folder is for organizational purposes and should not be included in the route's URL path.

---

## File-system conventions: Route Segment Config | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config

**Contents**:
- Route Segment Config
- Options
  - experimental_ppr
  - dynamic
  - dynamicParams
  - revalidate
    - Revalidation Frequency
  - fetchCache

Features available in /app

The options outlined on this page are disabled if the cacheComponents flag is on, and will eventually be deprecated in the future.

The Route Segment options allows you to configure the behavior of a Page, Layout, or Route Handler by directly exporting the following variables:

Enable Partial Prerendering (PPR) for a layout or page.

Change the dynamic behavior of a layout or page to fully static or fully dynamic.

Good to know: The new model in the app directory favors granular caching control at the fetch request level over the binary all-or-nothing model of getServerSideProps and getStaticProps at the page-level in the pages directory. The dynamic option is a way to opt back in to the previous model as a convenience and provides a simpler migration path.

'auto' (default): The default option to cache as much as possible without preventing any components from opting into dynamic behavior.

'force-dynamic': Force dynamic rendering, which will result in routes being rendered for each user at request time. This option is equivalent to:

'error': Force static rendering and cache the data of a layout or page by causing an error if any components use Dynamic APIs or uncached data. This option is equivalent to:

'force-static': Force static rendering and cache the data of a layout or page by forcing cookies, headers() and useSearchParams() to return empty values. It is possible to revalidate, revalidatePath, or revalidateTag, in pages or layouts rendered with force-static.

Control what happens when a dynamic segment is visited that was not generated with generateStaticParams.

Set the default revalidation time for a layout or page. This option does not override the revalidate value set by individual fetch requests.

By default, Next.js will cache any fetch() requests that are reachable before any Dynamic APIs are used and will not cache fetch requests that are discovered after Dynamic APIs are used.

fetchCache allows you to override the defa

*[Content truncated - see full docs]*

**Examples**:

```javascript
export const experimental_ppr = true
// true | false
```

```javascript
export const dynamic = 'auto'
// 'auto' | 'force-dynamic' | 'error' | 'force-static'
```

```javascript
export const dynamicParams = true // true | false
```

---

## File-system conventions: default.js | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/file-conventions/default

**Contents**:
- default.js
- Reference
  - params (optional)
- Learn more about Parallel Routes
  - Parallel Routes

Features available in /app

The default.js file is used to render a fallback within Parallel Routes when Next.js cannot recover a slot's active state after a full-page load.

During soft navigation, Next.js keeps track of the active state (subpage) for each slot. However, for hard navigations (full-page load), Next.js cannot recover the active state. In this case, a default.js file can be rendered for subpages that don't match the current URL.

Consider the following folder structure. The @team slot has a settings page, but @analytics does not.

When navigating to /settings, the @team slot will render the settings page while maintaining the currently active page for the @analytics slot.

On refresh, Next.js will render a default.js for @analytics. If default.js doesn't exist, a 404 is rendered instead.

Additionally, since children is an implicit slot, you also need to create a default.js file to render a fallback for children when Next.js cannot recover the active state of the parent page.

A promise that resolves to an object containing the dynamic route parameters from the root segment down to the slot's subpages. For example:

**Examples**:

```javascript
export default async function Default({
  params,
}: {
  params: Promise<{ artist: string }>
}) {
  const { artist } = await params
}
```

---

## File-system conventions: error.js | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/file-conventions/error

**Contents**:
- error.js
- Reference
  - Props
    - error
    - error.message
    - error.digest
    - reset
- Examples

Features available in /app

An error file allows you to handle unexpected runtime errors and display fallback UI.

error.js wraps a route segment and its nested children in a React Error Boundary. When an error throws within the boundary, the error component shows as the fallback UI.

An instance of an Error object forwarded to the error.js Client Component.

Good to know: During development, the Error object forwarded to the client will be serialized and include the message of the original error for easier debugging. However, this behavior is different in production to avoid leaking potentially sensitive details included in the error to the client.

An automatically generated hash of the error thrown. It can be used to match the corresponding error in server-side logs.

The cause of an error can sometimes be temporary. In these cases, trying again might resolve the issue.

An error component can use the reset() function to prompt the user to attempt to recover from the error. When executed, the function will try to re-render the error boundary's contents. If successful, the fallback error component is replaced with the result of the re-render.

While less common, you can handle errors in the root layout or template using global-error.jsx, located in the root app directory, even when leveraging internationalization. Global error UI must define its own <html> and <body> tags, global styles, fonts, or other dependencies that your error page requires. This file replaces the root layout or template when active.

Good to know: Error boundaries must be Client Components, which means that metadata and generateMetadata exports are not supported in global-error.jsx. As an alternative, you can use the React <title> component.

When rendering fails on the client, it can be useful to show the last known server rendered UI for a better user experience.

The GracefullyDegradingErrorBoundary is an example of a custom error boundary that captures and preserves the current HTML befo

*[Content truncated - see full docs]*

**Examples**:

```python
'use client' // Error boundaries must be Client Components
 
import { useEffect } from 'react'
 
export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string }
  reset: () => void
}) {
  useEffect(() => {
    // Log the error to an error reporting service
    console.error(error)
  }, [error])
 
  return (
    <div>
      <h2>Something went wrong!</h2>
      <button
        onClick={
          // Attempt to recover by trying to re-render the segment
          () => r
...
```

```javascript
'use client' // Error boundaries must be Client Components
 
export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string }
  reset: () => void
}) {
  return (
    <div>
      <h2>Something went wrong!</h2>
      <button onClick={() => reset()}>Try again</button>
    </div>
  )
}
```

```javascript
'use client' // Error boundaries must be Client Components
 
export default function GlobalError({
  error,
  reset,
}: {
  error: Error & { digest?: string }
  reset: () => void
}) {
  return (
    // global-error must include html and body tags
    <html>
      <body>
        <h2>Something went wrong!</h2>
        <button onClick={() => reset()}>Try again</button>
      </body>
    </html>
  )
}
```

---

## File-system conventions: forbidden.js | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/file-conventions/forbidden

**Contents**:
- forbidden.js
- Reference
  - Props
- Version History
- Next Steps
  - forbidden

Features available in /app

The forbidden file is used to render UI when the forbidden function is invoked during authentication. Along with allowing you to customize the UI, Next.js will return a 403 status code.

forbidden.js components do not accept any props.

**Examples**:

```python
import Link from 'next/link'
 
export default function Forbidden() {
  return (
    <div>
      <h2>Forbidden</h2>
      <p>You are not authorized to access this resource.</p>
      <Link href="/">Return Home</Link>
    </div>
  )
}
```

---

## File-system conventions: instrumentation-client.js | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation-client

**Contents**:
- instrumentation-client.js
- Usage
- Router navigation tracking
- Performance considerations
- Execution timing
- Examples
  - Error tracking
  - Analytics tracking

Features available in /app

The instrumentation-client.js|ts file allows you to add monitoring, analytics code, and other side-effects that run before your application becomes interactive. This is useful for setting up performance tracking, error monitoring, polyfills, or any other client-side observability tools.

To use it, place the file in the root of your application or inside a src folder.

Unlike server-side instrumentation, you do not need to export any specific functions. You can write your monitoring code directly in the file:

Error handling: Implement try-catch blocks around your instrumentation code to ensure robust monitoring. This prevents individual tracking failures from affecting other instrumentation features.

You can export an onRouterTransitionStart function to receive notifications when navigation begins:

The onRouterTransitionStart function receives two parameters:

Keep instrumentation code lightweight.

Next.js monitors initialization time in development and will log warnings if it takes longer than 16ms, which could impact smooth page loading.

The instrumentation-client.js file executes at a specific point in the application lifecycle:

This timing makes it ideal for setting up error tracking, analytics, and performance monitoring that needs to capture early application lifecycle events.

Initialize error tracking before React starts and add navigation breadcrumbs for better debugging context.

Initialize analytics and track navigation events with detailed metadata for user behavior analysis.

Track Time to Interactive and navigation performance using the Performance Observer API and performance marks.

Load polyfills before application code runs. Use static imports for immediate loading and dynamic imports for conditional loading based on feature detection.

**Examples**:

```javascript
// Set up performance monitoring
performance.mark('app-init')
 
// Initialize analytics
console.log('Analytics initialized')
 
// Set up error tracking
window.addEventListener('error', (event) => {
  // Send to your error tracking service
  reportError(event.error)
})
```

```javascript
performance.mark('app-init')
 
export function onRouterTransitionStart(
  url: string,
  navigationType: 'push' | 'replace' | 'traverse'
) {
  console.log(`Navigation started: ${navigationType} to ${url}`)
  performance.mark(`nav-start-${Date.now()}`)
}
```

```python
import Monitor from './lib/monitoring'
 
Monitor.initialize()
 
export function onRouterTransitionStart(url: string) {
  Monitor.pushEvent({
    message: `Navigation to ${url}`,
    category: 'navigation',
  })
}
```

---

## File-system conventions: instrumentation.js | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation

**Contents**:
- instrumentation.js
- Exports
  - register (optional)
  - onRequestError (optional)
    - Parameters
  - Specifying the runtime
- Version History
- Learn more about Instrumentation

Features available in /app

The instrumentation.js|ts file is used to integrate observability tools into your application, allowing you to track the performance and behavior, and to debug issues in production.

To use it, place the file in the root of your application or inside a src folder if using one.

The file exports a register function that is called once when a new Next.js server instance is initiated. register can be an async function.

You can optionally export an onRequestError function to track server errors to any custom observability provider.

The function accepts three parameters: error, request, and context.

The instrumentation.js file works in both the Node.js and Edge runtime, however, you can use process.env.NEXT_RUNTIME to target a specific runtime.

**Examples**:

```python
import { registerOTel } from '@vercel/otel'
 
export function register() {
  registerOTel('next-app')
}
```

```python
import { type Instrumentation } from 'next'
 
export const onRequestError: Instrumentation.onRequestError = async (
  err,
  request,
  context
) => {
  await fetch('https://.../report-error', {
    method: 'POST',
    body: JSON.stringify({
      message: err.message,
      request,
      context,
    }),
    headers: {
      'Content-Type': 'application/json',
    },
  })
}
```

```javascript
export function onRequestError(
  error: { digest: string } & Error,
  request: {
    path: string // resource path, e.g. /blog?name=foo
    method: string // request method. e.g. GET, POST, etc
    headers: { [key: string]: string | string[] }
  },
  context: {
    routerKind: 'Pages Router' | 'App Router' // the router type
    routePath: string // the route file path, e.g. /app/blog/[dynamic]
    routeType: 'render' | 'route' | 'action' | 'middleware' // the context in which the error occurre
...
```

---

## File-system conventions: layout.js | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/file-conventions/layout

**Contents**:
- layout.js
- Reference
  - Props
    - children (required)
    - params (optional)
  - Layout Props Helper
  - Root Layout
- Caveats

Features available in /app

The layout file is used to define a layout in your Next.js application.

A root layout is the top-most layout in the root app directory. It is used to define the <html> and <body> tags and other globally shared UI.

Layout components should accept and use a children prop. During rendering, children will be populated with the route segments the layout is wrapping. These will primarily be the component of a child Layout (if it exists) or Page, but could also be other special files like Loading or Error when applicable.

A promise that resolves to an object containing the dynamic route parameters object from the root segment down to that layout.

You can type layouts with LayoutProps to get a strongly typed params and named slots inferred from your directory structure. LayoutProps is a globally available helper.

The app directory must include a root layout, which is the top-most layout in the root app directory. Typically, the root layout is app/layout.js.

Layouts are cached in the client during navigation to avoid unnecessary server requests.

Layouts do not rerender. They can be cached and reused to avoid unnecessary computation when navigating between pages. By restricting layouts from accessing the raw request, Next.js can prevent the execution of potentially slow or expensive user code within the layout, which could negatively impact performance.

To access the request object, you can use headers and cookies APIs in Server Components and Functions.

Layouts do not rerender on navigation, so they cannot access search params which would otherwise become stale.

To access updated query parameters, you can use the Page searchParams prop, or read them inside a Client Component using the useSearchParams hook. Since Client Components re-render on navigation, they have access to the latest query parameters.

Layouts do not re-render on navigation, so they do not access pathname which would otherwise become stale.

To access the current pathna

*[Content truncated - see full docs]*

**Examples**:

```javascript
export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return <section>{children}</section>
}
```

```javascript
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
```

```javascript
export default async function Layout({
  children,
  params,
}: {
  children: React.ReactNode
  params: Promise<{ team: string }>
}) {
  const { team } = await params
}
```

---

## File-system conventions: loading.js | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/file-conventions/loading

**Contents**:
- loading.js
- Reference
  - Parameters
- Behavior
  - Navigation
  - Instant Loading States
  - SEO
  - Status Codes

Features available in /app

The special file loading.js helps you create meaningful Loading UI with React Suspense. With this convention, you can show an instant loading state from the server while the content of a route segment streams in. The new content is automatically swapped in once complete.

Inside the loading.js file, you can add any light-weight loading UI. You may find it helpful to use the React Developer Tools to manually toggle Suspense boundaries.

By default, this file is a Server Component - but can also be used as a Client Component through the "use client" directive.

Loading UI components do not accept any parameters.

An instant loading state is fallback UI that is shown immediately upon navigation. You can pre-render loading indicators such as skeletons and spinners, or a small but meaningful part of future screens such as a cover photo, title, etc. This helps users understand the app is responding and provides a better user experience.

Create a loading state by adding a loading.js file inside a folder.

In the same folder, loading.js will be nested inside layout.js. It will automatically wrap the page.js file and any children below in a <Suspense> boundary.

When streaming, a 200 status code will be returned to signal that the request was successful.

The server can still communicate errors or issues to the client within the streamed content itself, for example, when using redirect or notFound. Since the response headers have already been sent to the client, the status code of the response cannot be updated. This does not affect SEO.

Some browsers buffer a streaming response. You may not see the streamed response until the response exceeds 1024 bytes. This typically only affects “hello world” applications, but not real applications.

Learn how to configure streaming when self-hosting Next.js.

In addition to loading.js, you can also manually create Suspense Boundaries for your own UI components. The App Router supports streaming with Suspens

*[Content truncated - see full docs]*

**Examples**:

```javascript
export default function Loading() {
  // Or a custom loading skeleton component
  return <p>Loading...</p>
}
```

```javascript
export default function Loading() {
  // You can add any UI inside Loading, including a Skeleton.
  return <LoadingSkeleton />
}
```

```python
import { Suspense } from 'react'
import { PostFeed, Weather } from './Components'
 
export default function Posts() {
  return (
    <section>
      <Suspense fallback={<p>Loading feed...</p>}>
        <PostFeed />
      </Suspense>
      <Suspense fallback={<p>Loading weather...</p>}>
        <Weather />
      </Suspense>
    </section>
  )
}
```

---

## File-system conventions: mdx-components.js | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/file-conventions/mdx-components

**Contents**:
- mdx-components.js
- Exports
  - useMDXComponents function
- Version History
- Learn more about MDX Components
  - MDX

Features available in /app

The mdx-components.js|tsx file is required to use @next/mdx with App Router and will not work without it. Additionally, you can use it to customize styles.

Use the file mdx-components.tsx (or .js) in the root of your project to define MDX Components. For example, at the same level as pages or app, or inside src if applicable.

The file must export a single function named useMDXComponents. This function does not accept any arguments.

**Examples**:

```python
import type { MDXComponents } from 'mdx/types'
 
const components: MDXComponents = {}
 
export function useMDXComponents(): MDXComponents {
  return components
}
```

```python
import type { MDXComponents } from 'mdx/types'
 
const components: MDXComponents = {}
 
export function useMDXComponents(): MDXComponents {
  return components
}
```

---

## File-system conventions: middleware.js | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/file-conventions/middleware

**Contents**:
- middleware.js
- Exports
  - Middleware function
  - Config object (optional)
  - Matcher
- Params
  - request
- NextResponse

Features available in /app

The middleware.js|ts file is used to write Middleware and run code on the server before a request is completed. Then, based on the incoming request, you can modify the response by rewriting, redirecting, modifying the request or response headers, or responding directly.

Middleware executes before routes are rendered. It's particularly useful for implementing custom server-side logic like authentication, logging, or handling redirects.

Middleware is meant to be invoked separately of your render code and in optimized cases deployed to your CDN for fast redirect/rewrite handling, you should not attempt relying on shared modules or globals.

To pass information from Middleware to your application, use headers, cookies, rewrites, redirects, or the URL.

Create a middleware.ts (or .js) file in the project root, or inside src if applicable, so that it is located at the same level as pages or app.

If you’ve customized pageExtensions, for example to .page.ts or .page.js, name your file middleware.page.ts or middleware.page.js accordingly.

The file must export a single function, either as a default export or named middleware. Note that multiple middleware from the same file are not supported.

Optionally, a config object can be exported alongside the Middleware function. This object includes the matcher to specify paths where the Middleware applies.

The matcher option allows you to target specific paths for the Middleware to run on. You can specify these paths in several ways:

Additionally, the matcher option supports complex path specifications through regular expressions, such as matcher: ['/((?!api|_next/static|_next/image|.*\\.png$).*)'], enabling precise control over which paths to include or exclude.

The matcher option accepts an array of objects with the following keys:

Read more details on path-to-regexp documentation.

When defining Middleware, the default export function accepts a single parameter, request. This parameter is an in

*[Content truncated - see full docs]*

**Examples**:

```python
import { NextResponse, NextRequest } from 'next/server'
 
// This function can be marked `async` if using `await` inside
export function middleware(request: NextRequest) {
  return NextResponse.redirect(new URL('/home', request.url))
}
 
export const config = {
  matcher: '/about/:path*',
}
```

```javascript
// Example of default export
export default function middleware(request) {
  // Middleware logic
}
```

```javascript
export const config = {
  matcher: ['/about/:path*', '/dashboard/:path*'],
}
```

---

## File-system conventions: not-found.js | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/file-conventions/not-found

**Contents**:
- not-found.js
- not-found.js
- global-not-found.js (experimental)
- Reference
  - Props
- Examples
  - Data Fetching
  - Metadata

Features available in /app

Next.js provides two conventions to handle not found cases:

The not-found file is used to render UI when the notFound function is thrown within a route segment. Along with serving a custom UI, Next.js will return a 200 HTTP status code for streamed responses, and 404 for non-streamed responses.

The global-not-found.js file lets you define a 404 page for your entire application. Unlike not-found.js, which works at the route level, this is used when a requested URL doesn't match any route at all. Next.js skips rendering and directly returns this global page.

The global-not-found.js file bypasses your app's normal rendering, which means you'll need to import any global styles, fonts, or other dependencies that your 404 page requires.

Good to know: A smaller version of your global styles, and a simpler font family could improve performance of this page.

global-not-found.js is useful when you can't build a 404 page using a combination of layout.js and not-found.js. This can happen in two cases:

To enable it, add the globalNotFound flag in next.config.ts:

Then, create a file in the root of the app directory: app/global-not-found.js:

Unlike not-found.js, this file must return a full HTML document, including <html> and <body> tags.

not-found.js or global-not-found.js components do not accept any props.

Good to know: In addition to catching expected notFound() errors, the root app/not-found.js and app/global-not-found.js files handle any unmatched URLs for your whole application. This means users that visit a URL that is not handled by your app will be shown the exported UI.

By default, not-found is a Server Component. You can mark it as async to fetch and display data:

If you need to use Client Component hooks like usePathname to display content based on the path, you must fetch data on the client-side instead.

For global-not-found.js, you can export a metadata object or a generateMetadata function to customize the <title>, <meta>, a

*[Content truncated - see full docs]*

**Examples**:

```python
import Link from 'next/link'
 
export default function NotFound() {
  return (
    <div>
      <h2>Not Found</h2>
      <p>Could not find requested resource</p>
      <Link href="/">Return Home</Link>
    </div>
  )
}
```

```python
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  experimental: {
    globalNotFound: true,
  },
}
 
export default nextConfig
```

```python
// Import global styles and fonts
import './globals.css'
import { Inter } from 'next/font/google'
import type { Metadata } from 'next'
 
const inter = Inter({ subsets: ['latin'] })
 
export const metadata: Metadata = {
  title: '404 - Page Not Found',
  description: 'The page you are looking for does not exist.',
}
 
export default function GlobalNotFound() {
  return (
    <html lang="en" className={inter.className}>
      <body>
        <h1>404 - Page Not Found</h1>
        <p>This page does n
...
```

---

## File-system conventions: page.js | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/file-conventions/page

**Contents**:
- page.js
- Good to know
- Reference
  - Props
    - params (optional)
    - searchParams (optional)
  - Page Props Helper
- Examples

Features available in /app

The page file allows you to define UI that is unique to a route. You can create a page by default exporting a component from the file:

A promise that resolves to an object containing the dynamic route parameters from the root segment down to that page.

A promise that resolves to an object containing the search parameters of the current URL. For example:

Client Component pages can also access searchParams using React’s use hook:

You can type pages with PageProps to get strongly typed params and searchParams from the route literal. PageProps is a globally available helper.

Using dynamic route segments, you can display or fetch specific content for the page based on the params prop.

You can use the searchParams prop to handle filtering, pagination, or sorting based on the query string of the URL.

To use searchParams and params in a Client Component (which cannot be async), you can use React's use function to read the promise:

**Examples**:

```javascript
export default function Page({
  params,
  searchParams,
}: {
  params: Promise<{ slug: string }>
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>
}) {
  return <h1>My Page</h1>
}
```

```javascript
export default async function Page({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = await params
}
```

```javascript
export default async function Page({
  searchParams,
}: {
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>
}) {
  const filters = (await searchParams).filters
}
```

---

## File-system conventions: public | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/file-conventions/public-folder

**Contents**:
- public Folder
- Caching
- Robots, Favicons, and others

Features available in /app

Next.js can serve static files, like images, under a folder called public in the root directory. Files inside public can then be referenced by your code starting from the base URL (/).

For example, the file public/avatars/me.png can be viewed by visiting the /avatars/me.png path. The code to display that image might look like:

Next.js cannot safely cache assets in the public folder because they may change. The default caching headers applied are:

For static metadata files, such as robots.txt, favicon.ico, etc, you should use special metadata files inside the app folder.

**Examples**:

```python
import Image from 'next/image'
 
export function Avatar({ id, alt }) {
  return <Image src={`/avatars/${id}.png`} alt={alt} width="64" height="64" />
}
 
export function AvatarOfMe() {
  return <Avatar id="me" alt="A portrait of me" />
}
```

```text
Cache-Control: public, max-age=0
```

---

## File-system conventions: route.js | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/file-conventions/route

**Contents**:
- route.js
- Reference
  - HTTP Methods
  - Parameters
    - request (optional)
    - context (optional)
  - Route Context Helper
- Examples

Features available in /app

Route Handlers allow you to create custom request handlers for a given route using the Web Request and Response APIs.

A route file allows you to create custom request handlers for a given route. The following HTTP methods are supported: GET, POST, PUT, PATCH, DELETE, HEAD, and OPTIONS.

The request object is a NextRequest object, which is an extension of the Web Request API. NextRequest gives you further control over the incoming request, including easily accessing cookies and an extended, parsed, URL object nextUrl.

You can type the Route Handler context using RouteContext to get strongly typed params from a route literal. RouteContext is a globally available helper.

You can read or set cookies with cookies from next/headers.

Alternatively, you can return a new Response using the Set-Cookie header.

You can also use the underlying Web APIs to read cookies from the request (NextRequest):

You can read headers with headers from next/headers.

This headers instance is read-only. To set headers, you need to return a new Response with new headers.

You can also use the underlying Web APIs to read headers from the request (NextRequest):

You can revalidate cached data using the revalidate route segment config option.

Route Handlers can use Dynamic Segments to create request handlers from dynamic data.

The request object passed to the Route Handler is a NextRequest instance, which includes some additional convenience methods, such as those for more easily handling query parameters.

Streaming is commonly used in combination with Large Language Models (LLMs), such as OpenAI, for AI-generated content. Learn more about the AI SDK.

These abstractions use the Web APIs to create a stream. You can also use the underlying Web APIs directly.

You can read the Request body using the standard Web API methods:

You can read the FormData using the request.formData() function:

Since formData data are all strings, you may want to use zod-form-data to 

*[Content truncated - see full docs]*

**Examples**:

```javascript
export async function GET() {
  return Response.json({ message: 'Hello World' })
}
```

```javascript
export async function GET(request: Request) {}
 
export async function HEAD(request: Request) {}
 
export async function POST(request: Request) {}
 
export async function PUT(request: Request) {}
 
export async function DELETE(request: Request) {}
 
export async function PATCH(request: Request) {}
 
// If `OPTIONS` is not defined, Next.js will automatically implement `OPTIONS` and set the appropriate Response `Allow` header depending on the other methods defined in the Route Handler.
export asyn
...
```

```python
import type { NextRequest } from 'next/server'
 
export async function GET(request: NextRequest) {
  const url = request.nextUrl
}
```

---

## File-system conventions: src | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/file-conventions/src-folder

**Contents**:
- src Folder
- Next Steps
  - Project Structure

Features available in /app

As an alternative to having the special Next.js app or pages directories in the root of your project, Next.js also supports the common pattern of placing application code under the src folder.

This separates application code from project configuration files which mostly live in the root of a project, which is preferred by some individuals and teams.

To use the src folder, move the app Router folder or pages Router folder to src/app or src/pages respectively.

---

## File-system conventions: template.js | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/file-conventions/template

**Contents**:
- template.js
- Convention
- Props
  - children (required)
- Behavior
- Version History

Features available in /app

A template file is similar to a layout in that it wraps a layout or page. Unlike layouts that persist across routes and maintain state, templates are given a unique key, meaning children Client Components reset their state on navigation.

They are useful when you need to:

A template can be defined by exporting a default React component from a template.js file. The component should accept a children prop.

In terms of nesting, template.js is rendered between a layout and its children. Here's a simplified output:

Template accepts a children prop.

**Examples**:

```javascript
export default function Template({ children }: { children: React.ReactNode }) {
  return <div>{children}</div>
}
```

```text
<Layout>
  {/* Note that the template is given a unique key. */}
  <Template key={routeParam}>{children}</Template>
</Layout>
```

```text
<Layout>
  {/* Note that the template is automatically given a unique key. */}
  <Template key={routeParam}>{children}</Template>
</Layout>
```

---

## File-system conventions: unauthorized.js | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/file-conventions/unauthorized

**Contents**:
- unauthorized.js
- Reference
  - Props
- Examples
  - Displaying login UI to unauthenticated users
- Version History
- Next Steps
  - unauthorized

Features available in /app

The unauthorized file is used to render UI when the unauthorized function is invoked during authentication. Along with allowing you to customize the UI, Next.js will return a 401 status code.

unauthorized.js components do not accept any props.

You can use unauthorized function to render the unauthorized.js file with a login UI.

**Examples**:

```python
import Login from '@/app/components/Login'
 
export default function Unauthorized() {
  return (
    <main>
      <h1>401 - Unauthorized</h1>
      <p>Please log in to access this page.</p>
      <Login />
    </main>
  )
}
```

```python
import { verifySession } from '@/app/lib/dal'
import { unauthorized } from 'next/navigation'
 
export default async function DashboardPage() {
  const session = await verifySession()
 
  if (!session) {
    unauthorized()
  }
 
  return <div>Dashboard</div>
}
```

```python
import Login from '@/app/components/Login'
 
export default function UnauthorizedPage() {
  return (
    <main>
      <h1>401 - Unauthorized</h1>
      <p>Please log in to access this page.</p>
      <Login />
    </main>
  )
}
```

---

## Functions: ImageResponse | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/functions/image-response

**Contents**:
- ImageResponse
- Reference
  - Parameters
  - Supported HTML and CSS features
- Behavior
- Examples
  - Route Handlers
  - File-based Metadata

Features available in /app

The ImageResponse constructor allows you to generate dynamic images using JSX and CSS. This is useful for generating social media images such as Open Graph images, Twitter cards, and more.

The following parameters are available for ImageResponse:

Examples are available in the Vercel OG Playground.

ImageResponse supports common CSS properties including flexbox and absolute positioning, custom fonts, text wrapping, centering, and nested images.

Please refer to Satori’s documentation for a list of supported HTML and CSS features.

ImageResponse can be used in Route Handlers to generate images dynamically at request time.

You can use ImageResponse in a opengraph-image.tsx file to generate Open Graph images at build time or dynamically at request time.

You can use custom fonts in your ImageResponse by providing a fonts array in the options.

**Examples**:

```python
import { ImageResponse } from 'next/og'
 
new ImageResponse(
  element: ReactElement,
  options: {
    width?: number = 1200
    height?: number = 630
    emoji?: 'twemoji' | 'blobmoji' | 'noto' | 'openmoji' = 'twemoji',
    fonts?: {
      name: string,
      data: ArrayBuffer,
      weight: number,
      style: 'normal' | 'italic'
    }[]
    debug?: boolean = false
 
    // Options that will be passed to the HTTP response
    status?: number = 200
    statusText?: string
    headers?: Record<
...
```

```python
import { ImageResponse } from 'next/og'
 
export async function GET() {
  try {
    return new ImageResponse(
      (
        <div
          style={{
            height: '100%',
            width: '100%',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'center',
            backgroundColor: 'white',
            padding: '40px',
          }}
        >
          <div
            style={{
              fontSize: 60,
   
...
```

```python
import { ImageResponse } from 'next/og'
 
// Image metadata
export const alt = 'My site'
export const size = {
  width: 1200,
  height: 630,
}
 
export const contentType = 'image/png'
 
// Image generation
export default async function Image() {
  return new ImageResponse(
    (
      // ImageResponse JSX element
      <div
        style={{
          fontSize: 128,
          background: 'white',
          width: '100%',
          height: '100%',
          display: 'flex',
          alignItems: '
...
```

---

## Functions: NextRequest | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/functions/next-request

**Contents**:
- NextRequest
- cookies
  - set(name, value)
  - get(name)
  - getAll()
  - delete(name)
  - has(name)
  - clear()

Features available in /app

NextRequest extends the Web Request API with additional convenience methods.

Read or mutate the Set-Cookie header of the request.

Given a name, set a cookie with the given value on the request.

Given a cookie name, return the value of the cookie. If the cookie is not found, undefined is returned. If multiple cookies are found, the first one is returned.

Given a cookie name, return the values of the cookie. If no name is given, return all cookies on the request.

Given a cookie name, delete the cookie from the request.

Given a cookie name, return true if the cookie exists on the request.

Remove the Set-Cookie header from the request.

Extends the native URL API with additional convenience methods, including Next.js specific properties.

The following options are available:

Note: The internationalization properties from the Pages Router are not available for usage in the App Router. Learn more about internationalization with the App Router.

**Examples**:

```text
// Given incoming request /home
// Set a cookie to hide the banner
// request will have a `Set-Cookie:show-banner=false;path=/home` header
request.cookies.set('show-banner', 'false')
```

```text
// Given incoming request /home
// { name: 'show-banner', value: 'false', Path: '/home' }
request.cookies.get('show-banner')
```

```text
// Given incoming request /home
// [
//   { name: 'experiments', value: 'new-pricing-page', Path: '/home' },
//   { name: 'experiments', value: 'winter-launch', Path: '/home' },
// ]
request.cookies.getAll('experiments')
// Alternatively, get all cookies for the request
request.cookies.getAll()
```

---

## Functions: NextResponse | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/functions/next-response

**Contents**:
- NextResponse
- cookies
  - set(name, value)
  - get(name)
  - getAll()
  - delete(name)
- json()
- redirect()

Features available in /app

NextResponse extends the Web Response API with additional convenience methods.

Read or mutate the Set-Cookie header of the response.

Given a name, set a cookie with the given value on the response.

Given a cookie name, return the value of the cookie. If the cookie is not found, undefined is returned. If multiple cookies are found, the first one is returned.

Given a cookie name, return the values of the cookie. If no name is given, return all cookies on the response.

Given a cookie name, delete the cookie from the response.

Produce a response with the given JSON body.

Produce a response that redirects to a URL.

The URL can be created and modified before being used in the NextResponse.redirect() method. For example, you can use the request.nextUrl property to get the current URL, and then modify it to redirect to a different URL.

Produce a response that rewrites (proxies) the given URL while preserving the original URL.

The next() method is useful for Middleware, as it allows you to return early and continue routing.

You can also forward headers upstream when producing the response, using NextResponse.next({ request: { headers } }):

This forwards newHeaders upstream to the target page, route, or server action, and does not expose them to the client. While this pattern is useful for passing data upstream, it should be used with caution because the headers containing this data may be forwarded to external services.

In contrast, NextResponse.next({ headers }) is a shorthand for sending headers from middleware to the client. This is NOT good practice and should be avoided. Among other reasons because setting response headers like Content-Type, can override framework expectations (for example, the Content-Type used by Server Actions), leading to failed submissions or broken streaming responses.

In general, avoid copying all incoming request headers because doing so can leak sensitive data to clients or upstream services.

Prefer a 

*[Content truncated - see full docs]*

**Examples**:

```javascript
// Given incoming request /home
let response = NextResponse.next()
// Set a cookie to hide the banner
response.cookies.set('show-banner', 'false')
// Response will have a `Set-Cookie:show-banner=false;path=/home` header
return response
```

```javascript
// Given incoming request /home
let response = NextResponse.next()
// { name: 'show-banner', value: 'false', Path: '/home' }
response.cookies.get('show-banner')
```

```javascript
// Given incoming request /home
let response = NextResponse.next()
// [
//   { name: 'experiments', value: 'new-pricing-page', Path: '/home' },
//   { name: 'experiments', value: 'winter-launch', Path: '/home' },
// ]
response.cookies.getAll('experiments')
// Alternatively, get all cookies for the response
response.cookies.getAll()
```

---

## Functions: after | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/functions/after

**Contents**:
- after
- Reference
  - Parameters
  - Duration
- Good to know
- Examples
  - With request APIs
- Platform Support

Features available in /app

after allows you to schedule work to be executed after a response (or prerender) is finished. This is useful for tasks and other side effects that should not block the response, such as logging and analytics.

It can be used in Server Components (including generateMetadata), Server Actions, Route Handlers, and Middleware.

The function accepts a callback that will be executed after the response (or prerender) is finished:

Good to know: after is not a Dynamic API and calling it does not cause a route to become dynamic. If it's used within a static page, the callback will execute at build time, or whenever a page is revalidated.

after will run for the platform's default or configured max duration of your route. If your platform supports it, you can configure the timeout limit using the maxDuration route segment config.

You can use request APIs such as cookies and headers inside after in Server Actions and Route Handlers. This is useful for logging activity after a mutation. For example:

However, you cannot use these request APIs inside after in Server Components. This is because Next.js needs to know which part of the tree access the request APIs to support Partial Prerendering, but after runs after React's rendering lifecycle.

Learn how to configure after when self-hosting Next.js.

Using after in a serverless context requires waiting for asynchronous tasks to finish after the response has been sent. In Next.js and Vercel, this is achieved using a primitive called waitUntil(promise), which extends the lifetime of a serverless invocation until all promises passed to waitUntil have settled.

If you want your users to be able to run after, you will have to provide your implementation of waitUntil that behaves in an analogous way.

When after is called, Next.js will access waitUntil like this:

Which means that globalThis[Symbol.for('@next/request-context')] is expected to contain an object like this:

Here is an example of the implementa

*[Content truncated - see full docs]*

**Examples**:

```python
import { after } from 'next/server'
// Custom logging function
import { log } from '@/app/utils'
 
export default function Layout({ children }: { children: React.ReactNode }) {
  after(() => {
    // Execute after the layout is rendered and sent to the user
    log()
  })
  return <>{children}</>
}
```

```python
import { after } from 'next/server'
import { cookies, headers } from 'next/headers'
import { logUserAction } from '@/app/utils'
 
export async function POST(request: Request) {
  // Perform mutation
  // ...
 
  // Log user activity for analytics
  after(async () => {
    const userAgent = (await headers().get('user-agent')) || 'unknown'
    const sessionCookie =
      (await cookies().get('session-id'))?.value || 'anonymous'
 
    logUserAction({ sessionCookie, userAgent })
  })
 
  return new 
...
```

```javascript
const RequestContext = globalThis[Symbol.for('@next/request-context')]
const contextValue = RequestContext?.get()
const waitUntil = contextValue?.waitUntil
```

---

## Functions: cacheLife | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/functions/cacheLife

**Contents**:
- cacheLife
- Usage
- Reference
  - Default cache profiles
  - Custom cache profiles
- Examples
  - Defining reusable cache profiles
  - Overriding the default cache profiles

Features available in /app

The cacheLife function is used to set the cache lifetime of a function or component. It should be used alongside the use cache directive, and within the scope of the function or component.

To use cacheLife, enable the cacheComponents flag in your next.config.js file:

Then, import and invoke the cacheLife function within the scope of the function or component:

Next.js provides a set of named cache profiles modeled on various timescales. If you don't specify a cache profile in the cacheLife function alongside the use cache directive, Next.js will automatically apply the default cache profile.

However, we recommend always adding a cache profile when using the use cache directive to explicitly define caching behavior.

The string values used to reference cache profiles don't carry inherent meaning; instead they serve as semantic labels. This allows you to better understand and manage your cached content within your codebase.

Good to know: Updating the staleTimes and expireTime config options also updates the stale and expire properties of the default cache profile.

You can configure custom cache profiles by adding them to the cacheLife option in your next.config.ts file.

Cache profiles are objects that contain the following properties:

The "stale" property differs from the staleTimes setting in that it specifically controls client-side router caching. While staleTimes is a global setting that affects all instances of both dynamic and static data, the cacheLife configuration allows you to define "stale" times on a per-function or per-route basis.

Good to know: The “stale” property does not set the Cache-control: max-age header. It instead controls the client-side router cache.

You can create a reusable cache profile by defining them in your next.config.ts file. Choose a name that suits your use case and set values for the stale, revalidate, and expire properties. You can create as many custom cache profiles as needed. Each profile ca

*[Content truncated - see full docs]*

**Examples**:

```python
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  experimental: {
    cacheComponents: true,
  },
}
 
export default nextConfig
```

```python
'use cache'
import { unstable_cacheLife as cacheLife } from 'next/cache'
 
export default async function Page() {
  cacheLife('hours')
  return <div>Page</div>
}
```

```python
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  experimental: {
    cacheComponents: true,
    cacheLife: {
      biweekly: {
        stale: 60 * 60 * 24 * 14, // 14 days
        revalidate: 60 * 60 * 24, // 1 day
        expire: 60 * 60 * 24 * 14, // 14 days
      },
    },
  },
}
 
module.exports = nextConfig
```

---

## Functions: cacheTag | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/functions/cacheTag

**Contents**:
- cacheTag
- Usage
- Good to know
- Examples
  - Tagging components or functions
  - Creating tags from external data
  - Invalidating tagged cache
- Related

Features available in /app

The cacheTag function allows you to tag cached data for on-demand invalidation. By associating tags with cache entries, you can selectively purge or revalidate specific cache entries without affecting other cached data.

To use cacheTag, enable the cacheComponents flag in your next.config.js file:

The cacheTag function takes one or more string values.

You can then purge the cache on-demand using revalidateTag API in another function, for example, a route handler or Server Action:

Tag your cached data by calling cacheTag within a cached function or component:

You can use the data returned from an async function to tag the cache entry.

Using revalidateTag, you can invalidate the cache for a specific tag when needed:

**Examples**:

```python
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  experimental: {
    cacheComponents: true,
  },
}
 
export default nextConfig
```

```python
import { unstable_cacheTag as cacheTag } from 'next/cache'
 
export async function getData() {
  'use cache'
  cacheTag('my-data')
  const data = await fetch('/api/data')
  return data
}
```

```python
'use server'
 
import { revalidateTag } from 'next/cache'
 
export default async function submit() {
  await addPost()
  revalidateTag('my-data')
}
```

---

## Functions: connection | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/functions/connection

**Contents**:
- connection
- Reference
  - Type
  - Parameters
  - Returns
- Good to know
  - Version History

Features available in /app

The connection() function allows you to indicate rendering should wait for an incoming user request before continuing.

It's useful when a component doesn’t use Dynamic APIs, but you want it to be dynamically rendered at runtime and not statically rendered at build time. This usually occurs when you access external information that you intentionally want to change the result of a render, such as Math.random() or new Date().

**Examples**:

```python
import { connection } from 'next/server'
 
export default async function Page() {
  await connection()
  // Everything below will be excluded from prerendering
  const rand = Math.random()
  return <span>{rand}</span>
}
```

```javascript
function connection(): Promise<void>
```

---

## Functions: cookies | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/functions/cookies

**Contents**:
- cookies
- Reference
  - Methods
  - Options
- Good to know
- Understanding Cookie Behavior in Server Components
- Understanding Cookie Behavior in Server Actions
- Examples

Features available in /app

cookies is an async function that allows you to read the HTTP incoming request cookies in Server Components, and read/write outgoing request cookies in Server Actions or Route Handlers.

The following methods are available:

When setting a cookie, the following properties from the options object are supported:

The only option with a default value is path.

To learn more about these options, see the MDN docs.

When working with cookies in Server Components, it's important to understand that cookies are fundamentally a client-side storage mechanism:

The server can only send instructions (via Set-Cookie headers) to tell the browser to store cookies - the actual storage happens on the client side. This is why cookie operations that modify state (.set, .delete, .clear) must be performed in a Route Handler or Server Action where the response headers can be properly set.

After you set or delete a cookie in a Server Action, Next.js re-renders the current page and its layouts on the server so the UI reflects the new cookie value. See the Caching guide.

The UI is not unmounted, but effects that depend on data coming from the server will re-run.

To refresh cached data too, call revalidatePath or revalidateTag inside the action.

You can use the (await cookies()).get('name') method to get a single cookie:

You can use the (await cookies()).getAll() method to get all cookies with a matching name. If name is unspecified, it returns all the available cookies.

You can use the (await cookies()).set(name, value, options) method in a Server Action or Route Handler to set a cookie. The options object is optional.

You can use the (await cookies()).has(name) method to check if a cookie exists:

There are three ways you can delete a cookie.

Using the delete() method:

Setting a new cookie with the same name and an empty value:

Setting the maxAge to 0 will immediately expire a cookie. maxAge accepts a value in seconds.

**Examples**:

```python
import { cookies } from 'next/headers'
 
export default async function Page() {
  const cookieStore = await cookies()
  const theme = cookieStore.get('theme')
  return '...'
}
```

```python
import { cookies } from 'next/headers'
 
export default async function Page() {
  const cookieStore = await cookies()
  const theme = cookieStore.get('theme')
  return '...'
}
```

```python
import { cookies } from 'next/headers'
 
export default async function Page() {
  const cookieStore = await cookies()
  return cookieStore.getAll().map((cookie) => (
    <div key={cookie.name}>
      <p>Name: {cookie.name}</p>
      <p>Value: {cookie.value}</p>
    </div>
  ))
}
```

---

## Functions: draftMode | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/functions/draft-mode

**Contents**:
- draftMode
- Reference
- Good to know
- Examples
  - Enabling Draft Mode
  - Disabling Draft Mode
  - Checking if Draft Mode is enabled
- Version History

Features available in /app

draftMode is an async function allows you to enable and disable Draft Mode, as well as check if Draft Mode is enabled in a Server Component.

The following methods and properties are available:

To enable Draft Mode, create a new Route Handler and call the enable() method:

By default, the Draft Mode session ends when the browser is closed.

To disable Draft Mode manually, call the disable() method in your Route Handler:

Then, send a request to invoke the Route Handler. If calling the route using the <Link> component, you must pass prefetch={false} to prevent accidentally deleting the cookie on prefetch.

You can check if Draft Mode is enabled in a Server Component with the isEnabled property:

**Examples**:

```python
import { draftMode } from 'next/headers'
 
export default async function Page() {
  const { isEnabled } = await draftMode()
}
```

```python
import { draftMode } from 'next/headers'
 
export async function GET(request: Request) {
  const draft = await draftMode()
  draft.enable()
  return new Response('Draft mode is enabled')
}
```

```python
import { draftMode } from 'next/headers'
 
export async function GET(request: Request) {
  const draft = await draftMode()
  draft.disable()
  return new Response('Draft mode is disabled')
}
```

---

## Functions: fetch | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/functions/fetch

**Contents**:
- fetch
- fetch(url, options)
  - options.cache
  - options.next.revalidate
  - options.next.tags
- Troubleshooting
  - Fetch default auto no store and cache: 'no-store' not showing fresh data in development
  - Hard refresh and caching in development

Features available in /app

Next.js extends the Web fetch() API to allow each request on the server to set its own persistent caching and revalidation semantics.

In the browser, the cache option indicates how a fetch request will interact with the browser's HTTP cache. With this extension, cache indicates how a server-side fetch request will interact with the framework's persistent Data Cache.

You can call fetch with async and await directly within Server Components.

Since Next.js extends the Web fetch() API, you can use any of the native options available.

Configure how the request should interact with Next.js Data Cache.

Set the cache lifetime of a resource (in seconds). Data Cache.

Set the cache tags of a resource. Data can then be revalidated on-demand using revalidateTag. The max length for a custom tag is 256 characters and the max tag items is 128.

Next.js caches fetch responses in Server Components across Hot Module Replacement (HMR) in local development for faster responses and to reduce costs for billed API calls.

By default, the HMR cache applies to all fetch requests, including those with the default auto no cache and cache: 'no-store' option. This means uncached requests will not show fresh data between HMR refreshes. However, the cache will be cleared on navigation or full-page reloads.

See the serverComponentsHmrCache docs for more information.

In development mode, if the request includes the cache-control: no-cache header, options.cache, options.next.revalidate, and options.next.tags are ignored, and the fetch request is served from the source.

Browsers typically include cache-control: no-cache when the cache is disabled in developer tools or during a hard refresh.

**Examples**:

```javascript
export default async function Page() {
  let data = await fetch('https://api.vercel.app/blog')
  let posts = await data.json()
  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  )
}
```

```text
fetch(`https://...`, { cache: 'force-cache' | 'no-store' })
```

```text
fetch(`https://...`, { next: { revalidate: false | 0 | number } })
```

---

## Functions: forbidden | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/functions/forbidden

**Contents**:
- forbidden
- Good to know
- Examples
  - Role-based route protection
  - Mutations with Server Actions
- Version History
- Next Steps
  - forbidden.js

Features available in /app

The forbidden function throws an error that renders a Next.js 403 error page. It's useful for handling authorization errors in your application. You can customize the UI using the forbidden.js file.

To start using forbidden, enable the experimental authInterrupts configuration option in your next.config.js file:

forbidden can be invoked in Server Components, Server Actions, and Route Handlers.

You can use forbidden to restrict access to certain routes based on user roles. This ensures that users who are authenticated but lack the required permissions cannot access the route.

When implementing mutations in Server Actions, you can use forbidden to only allow users with a specific role to update sensitive data.

**Examples**:

```python
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  experimental: {
    authInterrupts: true,
  },
}
 
export default nextConfig
```

```python
import { verifySession } from '@/app/lib/dal'
import { forbidden } from 'next/navigation'
 
export default async function AdminPage() {
  const session = await verifySession()
 
  // Check if the user has the 'admin' role
  if (session.role !== 'admin') {
    forbidden()
  }
 
  // Render the admin page for authorized users
  return <></>
}
```

```python
import { verifySession } from '@/app/lib/dal'
import { forbidden } from 'next/navigation'
 
export default async function AdminPage() {
  const session = await verifySession()
 
  // Check if the user has the 'admin' role
  if (session.role !== 'admin') {
    forbidden()
  }
 
  // Render the admin page for authorized users
  return (
    <main>
      <h1>Admin Dashboard</h1>
      <p>Welcome, {session.user.name}!</p>
    </main>
  )
}
```

---

## Functions: generateImageMetadata | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata

**Contents**:
- generateImageMetadata
- Parameters
    - params (optional)
- Returns
  - Examples
    - Using external data
- Version History
- Next Steps

Features available in /app

You can use generateImageMetadata to generate different versions of one image or return multiple images for one route segment. This is useful for when you want to avoid hard-coding metadata values, such as for icons.

generateImageMetadata function accepts the following parameters:

An object containing the dynamic route parameters object from the root segment down to the segment generateImageMetadata is called from.

The generateImageMetadata function should return an array of objects containing the image's metadata such as alt and size. In addition, each item must include an id value which will be passed to the props of the image generating function.

This example uses the params object and external data to generate multiple Open Graph images for a route segment.

**Examples**:

```javascript
export function generateImageMetadata({
  params,
}: {
  params: { slug: string }
}) {
  // ...
}
```

```python
import { ImageResponse } from 'next/og'
 
export function generateImageMetadata() {
  return [
    {
      contentType: 'image/png',
      size: { width: 48, height: 48 },
      id: 'small',
    },
    {
      contentType: 'image/png',
      size: { width: 72, height: 72 },
      id: 'medium',
    },
  ]
}
 
export default function Icon({ id }: { id: string }) {
  return new ImageResponse(
    (
      <div
        style={{
          width: '100%',
          height: '100%',
          display: 'fl
...
```

```python
import { ImageResponse } from 'next/og'
import { getCaptionForImage, getOGImages } from '@/app/utils/images'
 
export async function generateImageMetadata({
  params,
}: {
  params: { id: string }
}) {
  const images = await getOGImages(params.id)
 
  return images.map((image, idx) => ({
    id: idx,
    size: { width: 1200, height: 600 },
    alt: image.text,
    contentType: 'image/png',
  }))
}
 
export default async function Image({
  params,
  id,
}: {
  params: { id: string }
  id: number

...
```

---

## Functions: generateMetadata | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/functions/generate-metadata

**Contents**:
- generateMetadata
- The metadata object
- generateMetadata function
- Reference
  - Parameters
  - Returns
  - Metadata Fields
    - title

Features available in /app

You can use the metadata object or the generateMetadata function to define metadata.

To define static metadata, export a Metadata object from a layout.js or page.js file.

See the Metadata Fields for a complete list of supported options.

Dynamic metadata depends on dynamic information, such as the current route parameters, external data, or metadata in parent segments, can be set by exporting a generateMetadata function that returns a Metadata object.

Resolving generateMetadata is part of rendering the page. If the page can be pre-rendered and generateMetadata doesn't introduce dynamic behavior, the resulting metadata is included in the page’s initial HTML.

Otherwise the metadata resolved from generateMetadata can be streamed after sending the initial UI.

For type completion of params and searchParams, you can type the first argument with PageProps<'/route'> or LayoutProps<'/route'> for pages and layouts respectively.

generateMetadata function accepts the following parameters:

props - An object containing the parameters of the current route:

params - An object containing the dynamic route parameters object from the root segment down to the segment generateMetadata is called from. Examples:

searchParams - An object containing the current URL's search params. Examples:

parent - A promise of the resolved metadata from parent route segments.

generateMetadata should return a Metadata object containing one or more metadata fields.

The following fields are supported:

The title attribute is used to set the title of the document. It can be defined as a simple string or an optional template object.

title.default can be used to provide a fallback title to child route segments that don't define a title.

title.template can be used to add a prefix or a suffix to titles defined in child route segments.

title.absolute can be used to provide a title that ignores title.template set in parent segments.

metadataBase is a convenience option t

*[Content truncated - see full docs]*

**Examples**:

```python
import type { Metadata } from 'next'
 
export const metadata: Metadata = {
  title: '...',
  description: '...',
}
 
export default function Page() {}
```

```python
import type { Metadata, ResolvingMetadata } from 'next'
 
type Props = {
  params: Promise<{ id: string }>
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>
}
 
export async function generateMetadata(
  { params, searchParams }: Props,
  parent: ResolvingMetadata
): Promise<Metadata> {
  // read route params
  const { id } = await params
 
  // fetch data
  const product = await fetch(`https://.../${id}`).then((res) => res.json())
 
  // optionally access and extend (rath
...
```

```javascript
export const metadata = {
  title: 'Next.js',
}
```

---

## Functions: generateSitemaps | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/functions/generate-sitemaps

**Contents**:
- generateSitemaps
- Returns
- URLs
- Example
- Version History
- Next Steps
  - sitemap.xml

Features available in /app

You can use the generateSitemaps function to generate multiple sitemaps for your application.

The generateSitemaps returns an array of objects with an id property.

Your generated sitemaps will be available at /.../sitemap/[id].xml. For example, /product/sitemap/1.xml.

For example, to split a sitemap using generateSitemaps, return an array of objects with the sitemap id. Then, use the id to generate the unique sitemaps.

**Examples**:

```python
import { BASE_URL } from '@/app/lib/constants'
 
export async function generateSitemaps() {
  // Fetch the total number of products and calculate the number of sitemaps needed
  return [{ id: 0 }, { id: 1 }, { id: 2 }, { id: 3 }]
}
 
export default async function sitemap({
  id,
}: {
  id: number
}): Promise<MetadataRoute.Sitemap> {
  // Google's limit is 50,000 URLs per sitemap
  const start = id * 50000
  const end = start + 50000
  const products = await getProducts(
    `SELECT id, date FROM
...
```

---

## Functions: generateStaticParams | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/functions/generate-static-params

**Contents**:
- generateStaticParams
- Parameters
- Returns
- Single Dynamic Segment
- Multiple Dynamic Segments
- Catch-all Dynamic Segment
- Examples
  - Static Rendering

Features available in /app

The generateStaticParams function can be used in combination with dynamic route segments to statically generate routes at build time instead of on-demand at request time.

options.params (optional)

If multiple dynamic segments in a route use generateStaticParams, the child generateStaticParams function is executed once for each set of params the parent generates.

The params object contains the populated params from the parent generateStaticParams, which can be used to generate the params in a child segment.

generateStaticParams should return an array of objects where each object represents the populated dynamic segments of a single route.

To statically render all paths at build time, supply the full list of paths to generateStaticParams:

To statically render a subset of paths at build time, and the rest the first time they're visited at runtime, return a partial list of paths:

Then, by using the dynamicParams segment config option, you can control what happens when a dynamic segment is visited that was not generated with generateStaticParams.

To statically render all paths the first time they're visited, return an empty array (no paths will be rendered at build time) or utilize export const dynamic = 'force-static':

Good to know: You must always return an array from generateStaticParams, even if it's empty. Otherwise, the route will be dynamically rendered.

To prevent unspecified paths from being statically rendered at runtime, add the export const dynamicParams = false option in a route segment. When this config option is used, only paths provided by generateStaticParams will be served, and unspecified routes will 404 or match (in the case of catch-all routes).

You can generate params for dynamic segments above the current layout or page, but not below. For example, given the app/products/[category]/[product] route:

There are two approaches to generating params for a route with multiple dynamic segments:

Generate multiple dyn

*[Content truncated - see full docs]*

**Examples**:

```javascript
// Return a list of `params` to populate the [slug] dynamic segment
export async function generateStaticParams() {
  const posts = await fetch('https://.../posts').then((res) => res.json())
 
  return posts.map((post) => ({
    slug: post.slug,
  }))
}
 
// Multiple versions of this page will be statically generated
// using the `params` returned by `generateStaticParams`
export default async function Page({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = await params

...
```

```javascript
export function generateStaticParams() {
  return [{ id: '1' }, { id: '2' }, { id: '3' }]
}
 
// Three versions of this page will be statically generated
// using the `params` returned by `generateStaticParams`
// - /product/1
// - /product/2
// - /product/3
export default async function Page({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params
  // ...
}
```

```javascript
export function generateStaticParams() {
  return [
    { category: 'a', product: '1' },
    { category: 'b', product: '2' },
    { category: 'c', product: '3' },
  ]
}
 
// Three versions of this page will be statically generated
// using the `params` returned by `generateStaticParams`
// - /products/a/1
// - /products/b/2
// - /products/c/3
export default async function Page({
  params,
}: {
  params: Promise<{ category: string; product: string }>
}) {
  const { category, product } = await par
...
```

---

## Functions: generateViewport | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/functions/generate-viewport

**Contents**:
- generateViewport
- The viewport object
- generateViewport function
- Viewport Fields
  - themeColor
  - width, initialScale, maximumScale and userScalable
  - colorScheme
- Types

Features available in /app

You can customize the initial viewport of the page with the static viewport object or the dynamic generateViewport function.

To define the viewport options, export a viewport object from a layout.jsx or page.jsx file.

generateViewport should return a Viewport object containing one or more viewport fields.

In TypeScript, the params argument can be typed via PageProps<'/route'> or LayoutProps<'/route'> depending on where generateViewport is defined.

Learn more about theme-color.

Good to know: The viewport meta tag is automatically set, and manual configuration is usually unnecessary as the default is sufficient. However, the information is provided for completeness.

Learn more about color-scheme.

You can add type safety to your viewport object by using the Viewport type. If you are using the built-in TypeScript plugin in your IDE, you do not need to manually add the type, but you can still explicitly add it if you want.

For JavaScript projects, you can use JSDoc to add type safety.

**Examples**:

```python
import type { Viewport } from 'next'
 
export const viewport: Viewport = {
  themeColor: 'black',
}
 
export default function Page() {}
```

```javascript
export function generateViewport({ params }) {
  return {
    themeColor: '...',
  }
}
```

```python
import type { Viewport } from 'next'
 
export const viewport: Viewport = {
  themeColor: 'black',
}
```

---

## Functions: headers | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/functions/headers

**Contents**:
- headers
- Reference
  - Parameters
  - Returns
- Good to know
- Examples
  - Using the Authorization header
- Version History

Features available in /app

headers is an async function that allows you to read the HTTP incoming request headers from a Server Component.

headers does not take any parameters.

headers returns a read-only Web Headers object.

**Examples**:

```python
import { headers } from 'next/headers'
 
export default async function Page() {
  const headersList = await headers()
  const userAgent = headersList.get('user-agent')
}
```

```python
import { headers } from 'next/headers'
 
export default async function Page() {
  const authorization = (await headers()).get('authorization')
  const res = await fetch('...', {
    headers: { authorization }, // Forward the authorization header
  })
  const user = await res.json()
 
  return <h1>{user.name}</h1>
}
```

---

## Functions: notFound | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/functions/not-found

**Contents**:
- notFound
- notFound()
- Version History

Features available in /app

The notFound function allows you to render the not-found file within a route segment as well as inject a <meta name="robots" content="noindex" /> tag.

Invoking the notFound() function throws a NEXT_HTTP_ERROR_FALLBACK;404 error and terminates rendering of the route segment in which it was thrown. Specifying a not-found file allows you to gracefully handle such errors by rendering a Not Found UI within the segment.

Good to know: notFound() does not require you to use return notFound() due to using the TypeScript never type.

**Examples**:

```python
import { notFound } from 'next/navigation'
 
async function fetchUser(id) {
  const res = await fetch('https://...')
  if (!res.ok) return undefined
  return res.json()
}
 
export default async function Profile({ params }) {
  const { id } = await params
  const user = await fetchUser(id)
 
  if (!user) {
    notFound()
  }
 
  // ...
}
```

---

## Functions: permanentRedirect | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/functions/permanentRedirect

**Contents**:
- permanentRedirect
- Parameters
- Returns
- Example
- Next Steps
  - redirect

Features available in /app

The permanentRedirect function allows you to redirect the user to another URL. permanentRedirect can be used in Server Components, Client Components, Route Handlers, and Server Actions.

When used in a streaming context, this will insert a meta tag to emit the redirect on the client side. When used in a server action, it will serve a 303 HTTP redirect response to the caller. Otherwise, it will serve a 308 (Permanent) HTTP redirect response to the caller.

If a resource doesn't exist, you can use the notFound function instead.

Good to know: If you prefer to return a 307 (Temporary) HTTP redirect instead of 308 (Permanent), you can use the redirect function instead.

The permanentRedirect function accepts two arguments:

By default, permanentRedirect will use push (adding a new entry to the browser history stack) in Server Actions and replace (replacing the current URL in the browser history stack) everywhere else. You can override this behavior by specifying the type parameter.

The type parameter has no effect when used in Server Components.

permanentRedirect does not return a value.

Invoking the permanentRedirect() function throws a NEXT_REDIRECT error and terminates rendering of the route segment in which it was thrown.

Good to know: permanentRedirect does not require you to use return permanentRedirect() as it uses the TypeScript never type.

**Examples**:

```text
permanentRedirect(path, type)
```

```python
import { permanentRedirect } from 'next/navigation'
 
async function fetchTeam(id) {
  const res = await fetch('https://...')
  if (!res.ok) return undefined
  return res.json()
}
 
export default async function Profile({ params }) {
  const { id } = await params
  const team = await fetchTeam(id)
  if (!team) {
    permanentRedirect('/login')
  }
 
  // ...
}
```

---

## Functions: redirect | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/functions/redirect

**Contents**:
- redirect
- Reference
  - Parameters
  - Returns
- Behavior
- Example
  - Server Component
  - Client Component

Features available in /app

The redirect function allows you to redirect the user to another URL. redirect can be used while rendering in Server and Client Components, Route Handlers, and Server Actions.

When used in a streaming context, this will insert a meta tag to emit the redirect on the client side. When used in a server action, it will serve a 303 HTTP redirect response to the caller. Otherwise, it will serve a 307 HTTP redirect response to the caller.

If a resource doesn't exist, you can use the notFound function instead.

The redirect function accepts two arguments:

By default, redirect will use push (adding a new entry to the browser history stack) in Server Actions and replace (replacing the current URL in the browser history stack) everywhere else. You can override this behavior by specifying the type parameter.

The RedirectType object contains the available options for the type parameter.

The type parameter has no effect when used in Server Components.

redirect does not return a value.

Invoking the redirect() function throws a NEXT_REDIRECT error and terminates rendering of the route segment in which it was thrown.

Good to know: redirect does not require you to use return redirect() as it uses the TypeScript never type.

redirect can be directly used in a Client Component.

Good to know: When using redirect in a Client Component on initial page load during Server-Side Rendering (SSR), it will perform a server-side redirect.

redirect can be used in a Client Component through a Server Action. If you need to use an event handler to redirect the user, you can use the useRouter hook.

When using redirect() you may notice that the status codes used are 307 for a temporary redirect, and 308 for a permanent redirect. While traditionally a 302 was used for a temporary redirect, and a 301 for a permanent redirect, many browsers changed the request method of the redirect, from a POST to GET request when using a 302, regardless of the origins request metho

*[Content truncated - see full docs]*

**Examples**:

```text
redirect(path, type)
```

```python
import { redirect, RedirectType } from 'next/navigation'
 
redirect('/redirect-to', RedirectType.replace)
// or
redirect('/redirect-to', RedirectType.push)
```

```python
import { redirect } from 'next/navigation'
 
async function fetchTeam(id: string) {
  const res = await fetch('https://...')
  if (!res.ok) return undefined
  return res.json()
}
 
export default async function Profile({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params
  const team = await fetchTeam(id)
 
  if (!team) {
    redirect('/login')
  }
 
  // ...
}
```

---

## Functions: revalidatePath | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/functions/revalidatePath

**Contents**:
- revalidatePath
- Usage
- Parameters
- Returns
- What can be invalidated
- Relationship with revalidateTag
  - Building revalidation utilities
- Examples

Features available in /app

revalidatePath allows you to invalidate cached data on-demand for a specific path.

revalidatePath can be called in Server Functions and Route Handlers.

revalidatePath cannot be called in Client Components or Middleware, as it only works in server environments.

Use a specific URL when you want to refresh a single page. Use a route pattern plus type to refresh multiple URLs.

revalidatePath does not return a value.

The path parameter can point to pages, layouts, or route handlers:

revalidatePath and revalidateTag serve different purposes:

When you call revalidatePath, only the specified path gets fresh data on the next visit. Other pages that use the same data tags will continue to serve cached data until those specific tags are also revalidated:

After calling revalidatePath('/blog'):

revalidatePath and revalidateTag are complementary primitives that are often used together in utility functions to ensure comprehensive data consistency across your application:

This pattern ensures that both the specific page and any other pages using the same data remain consistent.

This will invalidate one specific URL for revalidation on the next page visit.

This will invalidate any URL that matches the provided page file for revalidation on the next page visit. This will not invalidate pages beneath the specific page. For example, /blog/[slug] won't invalidate /blog/[slug]/[author].

This will invalidate any URL that matches the provided layout file for revalidation on the next page visit. This will cause pages beneath with the same layout to be invalidated and revalidated on the next visit. For example, in the above case, /blog/[slug]/[another] would also be invalidated and revalidated on the next visit.

This will purge the Client-side Router Cache, and invalidate the Data Cache for revalidation on the next page visit.

**Examples**:

```text
revalidatePath(path: string, type?: 'page' | 'layout'): void;
```

```javascript
export async function GET() {
  const data = await fetch('https://api.vercel.app/blog', {
    cache: 'force-cache',
  })
 
  return Response.json(await data.json())
}
```

```javascript
// Page A: /blog
const posts = await fetch('https://api.vercel.app/blog', {
  next: { tags: ['posts'] },
})
 
// Page B: /dashboard
const recentPosts = await fetch('https://api.vercel.app/blog?limit=5', {
  next: { tags: ['posts'] },
})
```

---

## Functions: revalidateTag | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/functions/revalidateTag

**Contents**:
- revalidateTag
- Usage
- Parameters
- Returns
- Relationship with revalidatePath
- Examples
  - Server Action
  - Route Handler

Features available in /app

revalidateTag allows you to invalidate cached data on-demand for a specific cache tag.

revalidateTag can be called in Server Functions and Route Handlers.

revalidateTag cannot be called in Client Components or Middleware, as it only works in server environments.

Good to know: revalidateTag marks tagged data as stale, but fresh data is only fetched when pages using that tag are next visited. This means calling revalidateTag will not immediately trigger many revalidations at once. The invalidation only happens when any page using that tag is next visited.

You can add tags to fetch as follows:

revalidateTag does not return a value.

revalidateTag invalidates data with specific tags across all pages that use those tags, while revalidatePath invalidates specific page or layout paths.

Good to know: These functions serve different purposes and may need to be used together for comprehensive data consistency. For detailed examples and considerations, see Relationship with revalidateTag.

**Examples**:

```text
revalidateTag(tag: string): void;
```

```text
fetch(url, { next: { tags: [...] } });
```

```python
'use server'
 
import { revalidateTag } from 'next/cache'
 
export default async function submit() {
  await addPost()
  revalidateTag('posts')
}
```

---

## Functions: unauthorized | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/functions/unauthorized

**Contents**:
- unauthorized
- Good to know
- Examples
  - Displaying login UI to unauthenticated users
  - Mutations with Server Actions
  - Fetching data with Route Handlers
- Version History
- Next Steps

Features available in /app

The unauthorized function throws an error that renders a Next.js 401 error page. It's useful for handling authorization errors in your application. You can customize the UI using the unauthorized.js file.

To start using unauthorized, enable the experimental authInterrupts configuration option in your next.config.js file:

unauthorized can be invoked in Server Components, Server Actions, and Route Handlers.

You can use unauthorized function to display the unauthorized.js file with a login UI.

You can invoke unauthorized in Server Actions to ensure only authenticated users can perform specific mutations.

You can use unauthorized in Route Handlers to ensure only authenticated users can access the endpoint.

**Examples**:

```python
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  experimental: {
    authInterrupts: true,
  },
}
 
export default nextConfig
```

```python
import { verifySession } from '@/app/lib/dal'
import { unauthorized } from 'next/navigation'
 
export default async function DashboardPage() {
  const session = await verifySession()
 
  if (!session) {
    unauthorized()
  }
 
  // Render the dashboard for authenticated users
  return (
    <main>
      <h1>Welcome to the Dashboard</h1>
      <p>Hi, {session.user.name}.</p>
    </main>
  )
}
```

```python
import { verifySession } from '@/app/lib/dal'
import { unauthorized } from 'next/navigation'
 
export default async function DashboardPage() {
  const session = await verifySession()
 
  if (!session) {
    unauthorized()
  }
 
  return <div>Dashboard</div>
}
```

---

## Functions: unstable_cache | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/functions/unstable_cache

**Contents**:
- unstable_cache
- Parameters
- Returns
- Example
- Version History

Features available in /app

Warning: This API will be replaced by use cache when it reaches stability.

unstable_cache allows you to cache the results of expensive operations, like database queries, and reuse them across multiple requests.

unstable_cache returns a function that when invoked, returns a Promise that resolves to the cached data. If the data is not in the cache, the provided function will be invoked, and its result will be cached and returned.

**Examples**:

```python
import { getUser } from './data';
import { unstable_cache } from 'next/cache';
 
const getCachedUser = unstable_cache(
  async (id) => getUser(id),
  ['my-app-user']
);
 
export default async function Component({ userID }) {
  const user = await getCachedUser(userID);
  ...
}
```

```javascript
const data = unstable_cache(fetchData, keyParts, options)()
```

```python
import { unstable_cache } from 'next/cache'
 
export default async function Page({
  params,
}: {
  params: Promise<{ userId: string }>
}) {
  const { userId } = await params
  const getCachedUser = unstable_cache(
    async () => {
      return { id: userId }
    },
    [userId], // add the user ID to the cache key
    {
      tags: ['users'],
      revalidate: 60,
    }
  )
 
  //...
}
```

---

## Functions: unstable_noStore | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/functions/unstable_noStore

**Contents**:
- unstable_noStore
- Usage
- Version History

Features available in /app

In version 15, we recommend using connection instead of unstable_noStore.

unstable_noStore can be used to declaratively opt out of static rendering and indicate a particular component should not be cached.

If you prefer not to pass additional options to fetch, like cache: 'no-store', next: { revalidate: 0 } or in cases where fetch is not available, you can use noStore() as a replacement for all of these use cases.

**Examples**:

```python
import { unstable_noStore as noStore } from 'next/cache';
 
export default async function ServerComponent() {
  noStore();
  const result = await db.query(...);
  ...
}
```

```python
import { unstable_noStore as noStore } from 'next/cache';
 
export default async function ServerComponent() {
  noStore();
  const result = await db.query(...);
  ...
}
```

---

## Functions: unstable_rethrow | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/functions/unstable_rethrow

**Contents**:
- unstable_rethrow

Features available in /app

unstable_rethrow can be used to avoid catching internal errors thrown by Next.js when attempting to handle errors thrown in your application code.

For example, calling the notFound function will throw an internal Next.js error and render the not-found.js component. However, if used inside the try block of a try/catch statement, the error will be caught, preventing not-found.js from rendering:

You can use unstable_rethrow API to re-throw the internal error and continue with the expected behavior:

The following Next.js APIs rely on throwing an error which should be rethrown and handled by Next.js itself:

If a route segment is marked to throw an error unless it's static, a Dynamic API call will also throw an error that should similarly not be caught by the developer. Note that Partial Prerendering (PPR) affects this behavior as well. These APIs are:

**Examples**:

```python
import { notFound } from 'next/navigation'
 
export default async function Page() {
  try {
    const post = await fetch('https://.../posts/1').then((res) => {
      if (res.status === 404) notFound()
      if (!res.ok) throw new Error(res.statusText)
      return res.json()
    })
  } catch (err) {
    console.error(err)
  }
}
```

```python
import { notFound, unstable_rethrow } from 'next/navigation'
 
export default async function Page() {
  try {
    const post = await fetch('https://.../posts/1').then((res) => {
      if (res.status === 404) notFound()
      if (!res.ok) throw new Error(res.statusText)
      return res.json()
    })
  } catch (err) {
    unstable_rethrow(err)
    console.error(err)
  }
}
```

---

## Functions: useLinkStatus | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/functions/use-link-status

**Contents**:
- useLinkStatus
- Parameters
- Returns
- Example
  - Inline loading indicator
- Gracefully handling fast navigation
- Next Steps
  - Link Component

Features available in /app

The useLinkStatus hook lets you tracks the pending state of a <Link>. You can use it to show inline visual feedback to the user (like spinners or text glimmers) while a navigation to a new route completes.

useLinkStatus is useful when:

useLinkStatus does not take any parameters.

useLinkStatus returns an object with a single property:

It's helpful to add visual feedback that navigation is happening in case the user clicks a link before prefetching is complete.

If the navigation to a new route is fast, users may see an unnecessary flash of the loading indicator. One way to improve the user experience and only show the loading indicator when the navigation takes time to complete is to add an initial animation delay (e.g. 100ms) and start the animation as invisible (e.g. opacity: 0).

**Examples**:

```python
'use client'
 
import { useLinkStatus } from 'next/link'
 
export default function LoadingIndicator() {
  const { pending } = useLinkStatus()
  return pending ? (
    <div role="status" aria-label="Loading" className="spinner" />
  ) : null
}
```

```python
import Link from 'next/link'
import LoadingIndicator from './loading-indicator'
 
export default function Header() {
  return (
    <header>
      <Link href="/dashboard" prefetch={false}>
        Dashboard <LoadingIndicator />
      </Link>
    </header>
  )
}
```

```javascript
const { pending } = useLinkStatus()
```

---

## Functions: useParams | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/functions/use-params

**Contents**:
- useParams
- Parameters
- Returns
- Version History

Features available in /app

useParams is a Client Component hook that lets you read a route's dynamic params filled in by the current URL.

useParams does not take any parameters.

useParams returns an object containing the current route's filled in dynamic parameters.

**Examples**:

```python
'use client'
 
import { useParams } from 'next/navigation'
 
export default function ExampleClientComponent() {
  const params = useParams<{ tag: string; item: string }>()
 
  // Route -> /shop/[tag]/[item]
  // URL -> /shop/shoes/nike-air-max-97
  // `params` -> { tag: 'shoes', item: 'nike-air-max-97' }
  console.log(params)
 
  return '...'
}
```

```javascript
const params = useParams()
```

---

## Functions: usePathname | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/functions/use-pathname

**Contents**:
- usePathname
- Parameters
- Returns
- Examples
  - Do something in response to a route change
  - Avoid hydration mismatch with rewrites

Features available in /app

usePathname is a Client Component hook that lets you read the current URL's pathname.

usePathname intentionally requires using a Client Component. It's important to note Client Components are not a de-optimization. They are an integral part of the Server Components architecture.

For example, a Client Component with usePathname will be rendered into HTML on the initial page load. When navigating to a new route, this component does not need to be re-fetched. Instead, the component is downloaded once (in the client JavaScript bundle), and re-renders based on the current state.

usePathname does not take any parameters.

usePathname returns a string of the current URL's pathname. For example:

When a page is pre-rendered, the HTML is generated for the source pathname. If the page is then reached through a rewrite using next.config or Middleware, the browser URL may differ, and usePathname() will read the rewritten pathname on the client.

To avoid hydration mismatches, design the UI so that only a small, isolated part depends on the client pathname. Render a stable fallback on the server and update that part after mount.

**Examples**:

```python
'use client'
 
import { usePathname } from 'next/navigation'
 
export default function ExampleClientComponent() {
  const pathname = usePathname()
  return <p>Current pathname: {pathname}</p>
}
```

```javascript
const pathname = usePathname()
```

```python
'use client'
 
import { useEffect } from 'react'
import { usePathname, useSearchParams } from 'next/navigation'
 
function ExampleClientComponent() {
  const pathname = usePathname()
  const searchParams = useSearchParams()
  useEffect(() => {
    // Do something here...
  }, [pathname, searchParams])
}
```

---

## Functions: useReportWebVitals | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/functions/use-report-web-vitals

**Contents**:
- useReportWebVitals
- useReportWebVitals
- Web Vitals
- Sending results to external systems

Features available in /app

The useReportWebVitals hook allows you to report Core Web Vitals, and can be used in combination with your analytics service.

New functions passed to useReportWebVitals are called with the available metrics up to that point. To prevent reporting duplicated data, ensure that the callback function reference does not change (as shown in the code examples below).

Since the useReportWebVitals hook requires the 'use client' directive, the most performant approach is to create a separate component that the root layout imports. This confines the client boundary exclusively to the WebVitals component.

The metric object passed as the hook's argument consists of a number of properties:

Web Vitals are a set of useful metrics that aim to capture the user experience of a web page. The following web vitals are all included:

You can handle all the results of these metrics using the name property.

You can send results to any endpoint to measure and track real user performance on your site. For example:

Good to know: If you use Google Analytics, using the id value can allow you to construct metric distributions manually (to calculate percentiles, etc.)

Read more about sending results to Google Analytics.

**Examples**:

```python
'use client'
 
import { useReportWebVitals } from 'next/web-vitals'
 
const logWebVitals = (metric) => {
  console.log(metric)
}
 
export function WebVitals() {
  useReportWebVitals(logWebVitals)
 
  return null
}
```

```python
import { WebVitals } from './_components/web-vitals'
 
export default function Layout({ children }) {
  return (
    <html>
      <body>
        <WebVitals />
        {children}
      </body>
    </html>
  )
}
```

```python
'use client'
 
import { useReportWebVitals } from 'next/web-vitals'
 
type ReportWebVitalsCallback = Parameters<typeof useReportWebVitals>[0]
 
const handleWebVitals: ReportWebVitalsCallback = (metric) => {
  switch (metric.name) {
    case 'FCP': {
      // handle FCP results
    }
    case 'LCP': {
      // handle LCP results
    }
    // ...
  }
}
 
export function WebVitals() {
  useReportWebVitals(handleWebVitals)
}
```

---

## Functions: useRouter | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/functions/use-router

**Contents**:
- useRouter
- useRouter()
  - Migrating from next/router
- Examples
  - Router events
  - Disabling scroll to top
- Version History

Features available in /app

The useRouter hook allows you to programmatically change routes inside Client Components.

Recommendation: Use the <Link> component for navigation unless you have a specific requirement for using useRouter.

View the full migration guide.

You can listen for page changes by composing other Client Component hooks like usePathname and useSearchParams.

Which can be imported into a layout.

Good to know: <NavigationEvents> is wrapped in a Suspense boundary becauseuseSearchParams() causes client-side rendering up to the closest Suspense boundary during static rendering. Learn more.

By default, Next.js will scroll to the top of the page when navigating to a new route. You can disable this behavior by passing scroll: false to router.push() or router.replace().

**Examples**:

```python
'use client'
 
import { useRouter } from 'next/navigation'
 
export default function Page() {
  const router = useRouter()
 
  return (
    <button type="button" onClick={() => router.push('/dashboard')}>
      Dashboard
    </button>
  )
}
```

```python
'use client'
 
import { useEffect } from 'react'
import { usePathname, useSearchParams } from 'next/navigation'
 
export function NavigationEvents() {
  const pathname = usePathname()
  const searchParams = useSearchParams()
 
  useEffect(() => {
    const url = `${pathname}?${searchParams}`
    console.log(url)
    // You can now use the current URL
    // ...
  }, [pathname, searchParams])
 
  return '...'
}
```

```python
import { Suspense } from 'react'
import { NavigationEvents } from './components/navigation-events'
 
export default function Layout({ children }) {
  return (
    <html lang="en">
      <body>
        {children}
 
        <Suspense fallback={null}>
          <NavigationEvents />
        </Suspense>
      </body>
    </html>
  )
}
```

---

## Functions: useSearchParams | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/functions/use-search-params

**Contents**:
- useSearchParams
- Parameters
- Returns
- Behavior
  - Static Rendering
  - Dynamic Rendering
  - Server Components
    - Pages

Features available in /app

useSearchParams is a Client Component hook that lets you read the current URL's query string.

useSearchParams returns a read-only version of the URLSearchParams interface.

useSearchParams does not take any parameters.

useSearchParams returns a read-only version of the URLSearchParams interface, which includes utility methods for reading the URL's query string:

URLSearchParams.get(): Returns the first value associated with the search parameter. For example:

URLSearchParams.has(): Returns a boolean value indicating if the given parameter exists. For example:

Learn more about other read-only methods of URLSearchParams, including the getAll(), keys(), values(), entries(), forEach(), and toString().

If a route is statically rendered, calling useSearchParams will cause the Client Component tree up to the closest Suspense boundary to be client-side rendered.

This allows a part of the route to be statically rendered while the dynamic part that uses useSearchParams is client-side rendered.

We recommend wrapping the Client Component that uses useSearchParams in a <Suspense/> boundary. This will allow any Client Components above it to be statically rendered and sent as part of initial HTML. Example.

Good to know: In development, all pages are rendered on-demand, so useSearchParams doesn't suspend. However, pre-rendering a static page that worked in development will fail the build if useSearchParams is used in a Client Component that isn’t directly or indirectly wrapped in a Suspense boundary.

If a route is dynamically rendered, useSearchParams will be available on the server during the initial server render of the Client Component.

Good to know: Setting the dynamic route segment config option to force-dynamic can be used to force dynamic rendering.

To access search params in Pages (Server Components), use the searchParams prop.

Unlike Pages, Layouts (Server Components) do not receive the searchParams prop. This is because a shared layo

*[Content truncated - see full docs]*

**Examples**:

```python
'use client'
 
import { useSearchParams } from 'next/navigation'
 
export default function SearchBar() {
  const searchParams = useSearchParams()
 
  const search = searchParams.get('search')
 
  // URL -> `/dashboard?search=my-project`
  // `search` -> 'my-project'
  return <>Search: {search}</>
}
```

```javascript
const searchParams = useSearchParams()
```

```python
'use client'
 
import { useSearchParams } from 'next/navigation'
 
export default function SearchBar() {
  const searchParams = useSearchParams()
 
  const search = searchParams.get('search')
 
  // This will not be logged on the server when using static rendering
  console.log(search)
 
  return <>Search: {search}</>
}
```

---

## Functions: useSelectedLayoutSegment | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segment

**Contents**:
- useSelectedLayoutSegment
- Parameters
- Returns
- Examples
  - Creating an active link component
- Version History

Features available in /app

useSelectedLayoutSegment is a Client Component hook that lets you read the active route segment one level below the Layout it is called from.

It is useful for navigation UI, such as tabs inside a parent layout that change style depending on the active child segment.

useSelectedLayoutSegment optionally accepts a parallelRoutesKey, which allows you to read the active route segment within that slot.

useSelectedLayoutSegment returns a string of the active segment or null if one doesn't exist.

For example, given the Layouts and URLs below, the returned segment would be:

You can use useSelectedLayoutSegment to create an active link component that changes style depending on the active segment. For example, a featured posts list in the sidebar of a blog:

**Examples**:

```python
'use client'
 
import { useSelectedLayoutSegment } from 'next/navigation'
 
export default function ExampleClientComponent() {
  const segment = useSelectedLayoutSegment()
 
  return <p>Active segment: {segment}</p>
}
```

```javascript
const segment = useSelectedLayoutSegment(parallelRoutesKey?: string)
```

```python
'use client'
 
import Link from 'next/link'
import { useSelectedLayoutSegment } from 'next/navigation'
 
// This *client* component will be imported into a blog layout
export default function BlogNavLink({
  slug,
  children,
}: {
  slug: string
  children: React.ReactNode
}) {
  // Navigating to `/blog/hello-world` will return 'hello-world'
  // for the selected layout segment
  const segment = useSelectedLayoutSegment()
  const isActive = slug === segment
 
  return (
    <Link
      href={`/b
...
```

---

## Functions: useSelectedLayoutSegments | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segments

**Contents**:
- useSelectedLayoutSegments
- Parameters
- Returns
- Version History

Features available in /app

useSelectedLayoutSegments is a Client Component hook that lets you read the active route segments below the Layout it is called from.

It is useful for creating UI in parent Layouts that need knowledge of active child segments such as breadcrumbs.

useSelectedLayoutSegments optionally accepts a parallelRoutesKey, which allows you to read the active route segment within that slot.

useSelectedLayoutSegments returns an array of strings containing the active segments one level down from the layout the hook was called from. Or an empty array if none exist.

For example, given the Layouts and URLs below, the returned segments would be:

**Examples**:

```python
'use client'
 
import { useSelectedLayoutSegments } from 'next/navigation'
 
export default function ExampleClientComponent() {
  const segments = useSelectedLayoutSegments()
 
  return (
    <ul>
      {segments.map((segment, index) => (
        <li key={index}>{segment}</li>
      ))}
    </ul>
  )
}
```

```javascript
const segments = useSelectedLayoutSegments(parallelRoutesKey?: string)
```

---

## Functions: userAgent | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/functions/userAgent

**Contents**:
- userAgent
- isBot
- browser
- device
- engine
- os
- cpu

Features available in /app

The userAgent helper extends the Web Request API with additional properties and methods to interact with the user agent object from the request.

A boolean indicating whether the request comes from a known bot.

An object containing information about the browser used in the request.

An object containing information about the device used in the request.

An object containing information about the browser's engine.

An object containing information about the operating system.

An object containing information about the CPU architecture.

**Examples**:

```python
import { NextRequest, NextResponse, userAgent } from 'next/server'
 
export function middleware(request: NextRequest) {
  const url = request.nextUrl
  const { device } = userAgent(request)
 
  // device.type can be: 'mobile', 'tablet', 'console', 'smarttv',
  // 'wearable', 'embedded', or undefined (for desktop browsers)
  const viewport = device.type || 'desktop'
 
  url.searchParams.set('viewport', viewport)
  return NextResponse.rewrite(url)
}
```

---

## Guides: Analytics | Next.js

**URL**: https://nextjs.org/docs/app/guides/analytics

**Contents**:
- How to add analytics to your Next.js application
- Client Instrumentation
- Build Your Own
- Web Vitals
- Sending results to external systems

Features available in /app

Next.js has built-in support for measuring and reporting performance metrics. You can either use the useReportWebVitals hook to manage reporting yourself, or alternatively, Vercel provides a managed service to automatically collect and visualize metrics for you.

For more advanced analytics and monitoring needs, Next.js provides a instrumentation-client.js|ts file that runs before your application's frontend code starts executing. This is ideal for setting up global analytics, error tracking, or performance monitoring tools.

To use it, create an instrumentation-client.js or instrumentation-client.ts file in your application's root directory:

Since the useReportWebVitals hook requires the 'use client' directive, the most performant approach is to create a separate component that the root layout imports. This confines the client boundary exclusively to the WebVitals component.

View the API Reference for more information.

Web Vitals are a set of useful metrics that aim to capture the user experience of a web page. The following web vitals are all included:

You can handle all the results of these metrics using the name property.

You can send results to any endpoint to measure and track real user performance on your site. For example:

Good to know: If you use Google Analytics, using the id value can allow you to construct metric distributions manually (to calculate percentiles, etc.)

Read more about sending results to Google Analytics.

**Examples**:

```javascript
// Initialize analytics before the app starts
console.log('Analytics initialized')
 
// Set up global error tracking
window.addEventListener('error', (event) => {
  // Send to your error tracking service
  reportError(event.error)
})
```

```python
'use client'
 
import { useReportWebVitals } from 'next/web-vitals'
 
export function WebVitals() {
  useReportWebVitals((metric) => {
    console.log(metric)
  })
}
```

```python
import { WebVitals } from './_components/web-vitals'
 
export default function Layout({ children }) {
  return (
    <html>
      <body>
        <WebVitals />
        {children}
      </body>
    </html>
  )
}
```

---

## Guides: Authentication | Next.js

**URL**: https://nextjs.org/docs/app/guides/authentication

**Contents**:
- How to implement authentication in Next.js
- Authentication
  - Sign-up and login functionality
    - 1. Capture user credentials
    - 2. Validate form fields on the server
    - 3. Create a user or check user credentials
- Session Management
  - Stateless Sessions

Features available in /app

Understanding authentication is crucial for protecting your application's data. This page will guide you through what React and Next.js features to use to implement auth.

Before starting, it helps to break down the process into three concepts:

This diagram shows the authentication flow using React and Next.js features:

The examples on this page walk through basic username and password auth for educational purposes. While you can implement a custom auth solution, for increased security and simplicity, we recommend using an authentication library. These offer built-in solutions for authentication, session management, and authorization, as well as additional features such as social logins, multi-factor authentication, and role-based access control. You can find a list in the Auth Libraries section.

You can use the <form> element with React's Server Actions and useActionState to capture user credentials, validate form fields, and call your Authentication Provider's API or database.

Since Server Actions always execute on the server, they provide a secure environment for handling authentication logic.

Here are the steps to implement signup/login functionality:

To capture user credentials, create a form that invokes a Server Action on submission. For example, a signup form that accepts the user's name, email, and password:

Use the Server Action to validate the form fields on the server. If your authentication provider doesn't provide form validation, you can use a schema validation library like Zod or Yup.

Using Zod as an example, you can define a form schema with appropriate error messages:

To prevent unnecessary calls to your authentication provider's API or database, you can return early in the Server Action if any form fields do not match the defined schema.

Back in your <SignupForm />, you can use React's useActionState hook to display validation errors while the form is submitting:

After validating form fields, you can create a

*[Content truncated - see full docs]*

**Examples**:

```python
import { signup } from '@/app/actions/auth'
 
export function SignupForm() {
  return (
    <form action={signup}>
      <div>
        <label htmlFor="name">Name</label>
        <input id="name" name="name" placeholder="Name" />
      </div>
      <div>
        <label htmlFor="email">Email</label>
        <input id="email" name="email" type="email" placeholder="Email" />
      </div>
      <div>
        <label htmlFor="password">Password</label>
        <input id="password" name="password" type=
...
```

```javascript
export async function signup(formData: FormData) {}
```

```python
import { z } from 'zod'
 
export const SignupFormSchema = z.object({
  name: z
    .string()
    .min(2, { message: 'Name must be at least 2 characters long.' })
    .trim(),
  email: z.string().email({ message: 'Please enter a valid email.' }).trim(),
  password: z
    .string()
    .min(8, { message: 'Be at least 8 characters long' })
    .regex(/[a-zA-Z]/, { message: 'Contain at least one letter.' })
    .regex(/[0-9]/, { message: 'Contain at least one number.' })
    .regex(/[^a-zA-Z0-9]/, {
...
```

---

## Guides: Backend for Frontend | Next.js

**URL**: https://nextjs.org/docs/app/guides/backend-for-frontend

**Contents**:
- How to use Next.js as a backend for your frontend
- Public Endpoints
- Content types
  - Consuming request payloads
- Manipulating data
- Proxying to a backend
- NextRequest and NextResponse
- Webhooks and callback URLs

Features available in /app

Next.js supports the "Backend for Frontend" pattern. This lets you create public endpoints to handle HTTP requests and return any content type—not just HTML. You can also access data sources and perform side effects like updating remote data.

If you are starting a new project, using create-next-app with the --api flag automatically includes an example route.ts in your new project’s app/ folder, demonstrating how to create an API endpoint.

Good to know: Next.js backend capabilities are not a full backend replacement. They serve as an API layer that:

To implement this pattern, use:

Route Handlers are public HTTP endpoints. Any client can access them.

Create a Route Handler using the route.ts or route.js file convention:

This handles GET requests sent to /api.

Use try/catch blocks for operations that may throw an exception:

Avoid exposing sensitive information in error messages sent to the client.

To restrict access, implement authentication and authorization. See Authentication.

Route Handlers let you serve non-UI responses, including JSON, XML, images, files, and plain text.

Next.js uses file conventions for common endpoints:

You can also define custom ones, such as:

For example, app/rss.xml/route.ts creates a Route Handler for rss.xml.

Sanitize any input used to generate markup.

Use Request instance methods like .json(), .formData(), or .text() to access the request body.

GET and HEAD requests don’t carry a body.

Good to know: Validate data before passing it to other systems

You can only read the request body once. Clone the request if you need to read it again:

Route Handlers can transform, filter, and aggregate data from one or more sources. This keeps logic out of the frontend and avoids exposing internal systems.

You can also offload heavy computations to the server and reduce client battery and data usage.

Good to know: This example uses POST to avoid putting geo-location data in the URL. GET requests may be cach

*[Content truncated - see full docs]*

**Examples**:

```text
npx create-next-app@latest --api
```

```javascript
export function GET(request: Request) {}
```

```python
import { submit } from '@/lib/submit'
 
export async function POST(request: Request) {
  try {
    await submit(request)
    return new Response(null, { status: 204 })
  } catch (reason) {
    const message =
      reason instanceof Error ? reason.message : 'Unexpected error'
 
    return new Response(message, { status: 500 })
  }
}
```

---

## Guides: CI Build Caching | Next.js

**URL**: https://nextjs.org/docs/app/guides/ci-build-caching

**Contents**:
- How to configure Continuous Integration (CI) build caching
- Vercel
- CircleCI
- Travis CI
- GitLab CI
- Netlify CI
- AWS CodeBuild
- GitHub Actions

Features available in /app

To improve build performance, Next.js saves a cache to .next/cache that is shared between builds.

To take advantage of this cache in Continuous Integration (CI) environments, your CI workflow will need to be configured to correctly persist the cache between builds.

If your CI is not configured to persist .next/cache between builds, you may see a No Cache Detected error.

Here are some example cache configurations for common CI providers:

Next.js caching is automatically configured for you. There's no action required on your part. If you are using Turborepo on Vercel, learn more here.

Edit your save_cache step in .circleci/config.yml to include .next/cache:

If you do not have a save_cache key, please follow CircleCI's documentation on setting up build caching.

Add or merge the following into your .travis.yml:

Add or merge the following into your .gitlab-ci.yml:

Use Netlify Plugins with @netlify/plugin-nextjs.

Add (or merge in) the following to your buildspec.yml:

Using GitHub's actions/cache, add the following step in your workflow file:

Add or merge the following into your bitbucket-pipelines.yml at the top level (same level as pipelines):

Then reference it in the caches section of your pipeline's step:

Using Heroku's custom cache, add a cacheDirectories array in your top-level package.json:

Using Azure Pipelines' Cache task, add the following task to your pipeline yaml file somewhere prior to the task that executes next build:

Using Jenkins' Job Cacher plugin, add the following build step to your Jenkinsfile where you would normally run next build or npm install:

**Examples**:

```text
steps:
  - save_cache:
      key: dependency-cache-{{ checksum "yarn.lock" }}
      paths:
        - ./node_modules
        - ./.next/cache
```

```text
cache:
  directories:
    - $HOME/.cache/yarn
    - node_modules
    - .next/cache
```

```text
cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - node_modules/
    - .next/cache/
```

---

## Guides: CSS-in-JS | Next.js

**URL**: https://nextjs.org/docs/app/guides/css-in-js

**Contents**:
- How to use CSS-in-JS libraries
- Configuring CSS-in-JS in app
  - styled-jsx
  - Styled Components

Features available in /app

Warning: Using CSS-in-JS with newer React features like Server Components and Streaming requires library authors to support the latest version of React, including concurrent rendering.

The following libraries are supported in Client Components in the app directory (alphabetical):

The following are currently working on support:

Good to know: We're testing out different CSS-in-JS libraries and we'll be adding more examples for libraries that support React 18 features and/or the app directory.

Configuring CSS-in-JS is a three-step opt-in process that involves:

Using styled-jsx in Client Components requires using v5.1.0. First, create a new registry:

Then, wrap your root layout with the registry:

View an example here.

Below is an example of how to configure styled-components@6 or newer:

First, enable styled-components in next.config.js.

Then, use the styled-components API to create a global registry component to collect all CSS style rules generated during a render, and a function to return those rules. Then use the useServerInsertedHTML hook to inject the styles collected in the registry into the <head> HTML tag in the root layout.

Wrap the children of the root layout with the style registry component:

View an example here.

**Examples**:

```python
'use client'
 
import React, { useState } from 'react'
import { useServerInsertedHTML } from 'next/navigation'
import { StyleRegistry, createStyleRegistry } from 'styled-jsx'
 
export default function StyledJsxRegistry({
  children,
}: {
  children: React.ReactNode
}) {
  // Only create stylesheet once with lazy initial state
  // x-ref: https://reactjs.org/docs/hooks-reference.html#lazy-initial-state
  const [jsxStyleRegistry] = useState(() => createStyleRegistry())
 
  useServerInsertedHTML(()
...
```

```python
import StyledJsxRegistry from './registry'
 
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html>
      <body>
        <StyledJsxRegistry>{children}</StyledJsxRegistry>
      </body>
    </html>
  )
}
```

```text
module.exports = {
  compiler: {
    styledComponents: true,
  },
}
```

---

## Guides: Caching | Next.js

**URL**: https://nextjs.org/docs/app/guides/caching

**Contents**:
- Caching in Next.js
- Overview
- Request Memoization
  - Duration
  - Revalidating
  - Opting out
- Data Cache
  - Duration

Features available in /app

Next.js improves your application's performance and reduces costs by caching rendering work and data requests. This page provides an in-depth look at Next.js caching mechanisms, the APIs you can use to configure them, and how they interact with each other.

Good to know: This page helps you understand how Next.js works under the hood but is not essential knowledge to be productive with Next.js. Most of Next.js' caching heuristics are determined by your API usage and have defaults for the best performance with zero or minimal configuration. If you instead want to jump to examples, start here.

Here's a high-level overview of the different caching mechanisms and their purpose:

By default, Next.js will cache as much as possible to improve performance and reduce cost. This means routes are statically rendered and data requests are cached unless you opt out. The diagram below shows the default caching behavior: when a route is statically rendered at build time and when a static route is first visited.

Caching behavior changes depending on whether the route is statically or dynamically rendered, data is cached or uncached, and whether a request is part of an initial visit or a subsequent navigation. Depending on your use case, you can configure the caching behavior for individual routes and data requests.

Fetch caching is not supported in middleware. Any fetches done inside of your middleware will be uncached.

Next.js extends the fetch API to automatically memoize requests that have the same URL and options. This means you can call a fetch function for the same data in multiple places in a React component tree while only executing it once.

For example, if you need to use the same data across a route (e.g. in a Layout, Page, and multiple components), you do not have to fetch data at the top of the tree, and forward props between components. Instead, you can fetch data in the components that need it without worrying about the performance imp

*[Content truncated - see full docs]*

**Examples**:

```javascript
async function getItem() {
  // The `fetch` function is automatically memoized and the result
  // is cached
  const res = await fetch('https://.../item/1')
  return res.json()
}
 
// This function is called twice, but only executed the first time
const item = await getItem() // cache MISS
 
// The second call could be anywhere in your route
const item = await getItem() // cache HIT
```

```javascript
const { signal } = new AbortController()
fetch(url, { signal })
```

```text
// Revalidate at most every hour
fetch('https://...', { next: { revalidate: 3600 } })
```

---

## Guides: Content Security Policy | Next.js

**URL**: https://nextjs.org/docs/app/guides/content-security-policy

**Contents**:
- How to set a Content Security Policy (CSP) for your Next.js application
- Nonces
  - Why use a nonce?
  - Adding a nonce with Middleware
  - How nonces work in Next.js
  - Forcing dynamic rendering
  - Reading the nonce
- Static vs Dynamic Rendering with CSP

Features available in /app

Content Security Policy (CSP) is important to guard your Next.js application against various security threats such as cross-site scripting (XSS), clickjacking, and other code injection attacks.

By using CSP, developers can specify which origins are permissible for content sources, scripts, stylesheets, images, fonts, objects, media (audio, video), iframes, and more.

A nonce is a unique, random string of characters created for a one-time use. It is used in conjunction with CSP to selectively allow certain inline scripts or styles to execute, bypassing strict CSP directives.

CSP can block both inline and external scripts to prevent attacks. A nonce lets you safely allow specific scripts to run—only if they include the matching nonce value.

If an attacker wanted to load a script into your page, they'd need to guess the nonce value. That's why the nonce must be unpredictable and unique for every request.

Middleware enables you to add headers and generate nonces before the page renders.

Every time a page is viewed, a fresh nonce should be generated. This means that you must use dynamic rendering to add nonces.

By default, Middleware runs on all requests. You can filter Middleware to run on specific paths using a matcher.

We recommend ignoring matching prefetches (from next/link) and static assets that don't need the CSP header.

To use a nonce, your page must be dynamically rendered. This is because Next.js applies nonces during server-side rendering, based on the CSP header present in the request. Static pages are generated at build time, when no request or response headers exist—so no nonce can be injected.

Here’s how nonce support works in a dynamically rendered page:

Because of this automatic behavior, you don’t need to manually add a nonce to each tag.

If you're using nonces, you may need to explicitly opt pages into dynamic rendering:

You can read the nonce from a Server Component using headers:

Using nonces has important im

*[Content truncated - see full docs]*

**Examples**:

```python
import { NextRequest, NextResponse } from 'next/server'
 
export function middleware(request: NextRequest) {
  const nonce = Buffer.from(crypto.randomUUID()).toString('base64')
  const cspHeader = `
    default-src 'self';
    script-src 'self' 'nonce-${nonce}' 'strict-dynamic';
    style-src 'self' 'nonce-${nonce}';
    img-src 'self' blob: data:;
    font-src 'self';
    object-src 'none';
    base-uri 'self';
    form-action 'self';
    frame-ancestors 'none';
    upgrade-insecure-requests;
`
...
```

```javascript
export const config = {
  matcher: [
    /*
     * Match all request paths except for the ones starting with:
     * - api (API routes)
     * - _next/static (static files)
     * - _next/image (image optimization files)
     * - favicon.ico (favicon file)
     */
    {
      source: '/((?!api|_next/static|_next/image|favicon.ico).*)',
      missing: [
        { type: 'header', key: 'next-router-prefetch' },
        { type: 'header', key: 'purpose', value: 'prefetch' },
      ],
    },
  ],
}
```

```python
import { connection } from 'next/server'
 
export default async function Page() {
  // wait for an incoming request to render this page
  await connection()
  // Your page content
}
```

---

## Guides: Custom Server | Next.js

**URL**: https://nextjs.org/docs/app/guides/custom-server

**Contents**:
- How to set up a custom server in Next.js

Features available in /app

Next.js includes its own server with next start by default. If you have an existing backend, you can still use it with Next.js (this is not a custom server). A custom Next.js server allows you to programmatically start a server for custom patterns. The majority of the time, you will not need this approach. However, it's available if you need to eject.

Take a look at the following example of a custom server:

server.js does not run through the Next.js Compiler or bundling process. Make sure the syntax and source code this file requires are compatible with the current Node.js version you are using. View an example.

To run the custom server, you'll need to update the scripts in package.json like so:

Alternatively, you can set up nodemon (example). The custom server uses the following import to connect the server with the Next.js application:

The above next import is a function that receives an object with the following options:

The returned app can then be used to let Next.js handle requests as required.

**Examples**:

```python
import { createServer } from 'http'
import { parse } from 'url'
import next from 'next'
 
const port = parseInt(process.env.PORT || '3000', 10)
const dev = process.env.NODE_ENV !== 'production'
const app = next({ dev })
const handle = app.getRequestHandler()
 
app.prepare().then(() => {
  createServer((req, res) => {
    const parsedUrl = parse(req.url!, true)
    handle(req, res, parsedUrl)
  }).listen(port)
 
  console.log(
    `> Server listening at http://localhost:${port} as ${
      dev ? 
...
```

```text
{
  "scripts": {
    "dev": "node server.js",
    "build": "next build",
    "start": "NODE_ENV=production node server.js"
  }
}
```

```python
import next from 'next'
 
const app = next({})
```

---

## Guides: Data Security | Next.js

**URL**: https://nextjs.org/docs/app/guides/data-security

**Contents**:
- How to think about data security in Next.js
- Data fetching approaches
  - External HTTP APIs
  - Data Access Layer
  - Component-level data access
- Reading data
  - Passing data from server to client
  - Tainting

Features available in /app

React Server Components improve performance and simplify data fetching, but also shift where and how data is accessed, changing some of the traditional security assumptions for handling data in frontend apps.

This guide will help you understand how to think about data security in Next.js and how to implement best practices.

There are three main approaches we recommend for fetching data in Next.js, depending on the size and age of your project:

We recommend choosing one data fetching approach and avoiding mixing them. This makes it clear for both developers working in your code base and security auditors what to expect.

You should follow a Zero Trust model when adopting Server Components in an existing project. You can continue calling your existing API endpoints such as REST or GraphQL from Server Components using fetch, just as you would in Client Components.

This approach works well when:

For new projects, we recommend creating a dedicated Data Access Layer (DAL). This is a internal library that controls how and when data is fetched, and what gets passed to your render context.

A Data Access Layer should:

This approach centralizes all data access logic, making it easier to enforce consistent data access and reduces the risk of authorization bugs. You also get the benefit of sharing an in-memory cache across different parts of a request.

Good to know: Secret keys should be stored in environment variables, but only the Data Access Layer should access process.env. This keeps secrets from being exposed to other parts of the application.

For quick prototypes and iteration, database queries can be placed directly in Server Components.

This approach, however, makes it easier to accidentally expose private data to the client, for example:

You should sanitize the data before passing it to the Client Component:

On the initial load, both Server and Client Components run on the server to generate HTML. However, they execute in isolated

*[Content truncated - see full docs]*

**Examples**:

```python
import { cookies } from 'next/headers'
 
export default async function Page() {
  const cookieStore = cookies()
  const token = cookieStore.get('AUTH_TOKEN')?.value
 
  const res = await fetch('https://api.example.com/profile', {
    headers: {
      Cookie: `AUTH_TOKEN=${token}`,
      // Other headers
    },
  })
 
  // ....
}
```

```python
import { cache } from 'react'
import { cookies } from 'next/headers'
 
// Cached helper methods makes it easy to get the same value in many places
// without manually passing it around. This discourages passing it from Server
// Component to Server Component which minimizes risk of passing it to a Client
// Component.
export const getCurrentUser = cache(async () => {
  const token = cookies().get('AUTH_TOKEN')
  const decodedToken = await decryptAndValidate(token)
  // Don't include secret token
...
```

```python
import 'server-only'
import { getCurrentUser } from './auth'
 
function canSeeUsername(viewer: User) {
  // Public info for now, but can change
  return true
}
 
function canSeePhoneNumber(viewer: User, team: string) {
  // Privacy rules
  return viewer.isAdmin || team === viewer.team
}
 
export async function getProfileDTO(slug: string) {
  // Don't pass values, read back cached values, also solves context and easier to make it lazy
 
  // use a database API that supports safe templating of que
...
```

---

## Guides: Debugging | Next.js

**URL**: https://nextjs.org/docs/app/guides/debugging

**Contents**:
- How to use debugging tools with Next.js
- Debugging with VS Code
- Using the Debugger in Jetbrains WebStorm
- Debugging with Browser DevTools
  - Client-side code
  - React Developer Tools
  - Server-side code
  - Inspect Server Errors with Browser DevTools

Features available in /app

This documentation explains how you can debug your Next.js frontend and backend code with full source maps support using the VS Code debugger, Chrome DevTools, or Firefox DevTools.

Any debugger that can attach to Node.js can also be used to debug a Next.js application. You can find more details in the Node.js Debugging Guide.

Create a file named .vscode/launch.json at the root of your project with the following content:

Note: To use Firefox debugging in VS Code, you'll need to install the Firefox Debugger extension.

npm run dev can be replaced with yarn dev if you're using Yarn or pnpm dev if you're using pnpm.

In the "Next.js: debug full stack" configuration, serverReadyAction.action specifies which browser to open when the server is ready. debugWithEdge means to launch the Edge browser. If you are using Chrome, change this value to debugWithChrome.

If you're changing the port number your application starts on, replace the 3000 in http://localhost:3000 with the port you're using instead.

If you're running Next.js from a directory other than root (for example, if you're using Turborepo) then you need to add cwd to the server-side and full stack debugging tasks. For example, "cwd": "${workspaceFolder}/apps/web".

Now go to the Debug panel (Ctrl+Shift+D on Windows/Linux, ⇧+⌘+D on macOS), select a launch configuration, then press F5 or select Debug: Start Debugging from the Command Palette to start your debugging session.

Click the drop down menu listing the runtime configuration, and click Edit Configurations.... Create a JavaScript Debug debug configuration with http://localhost:3000 as the URL. Customize to your liking (e.g. Browser for debugging, store as project file), and click OK. Run this debug configuration, and the selected browser should automatically open. At this point, you should have 2 applications in debug mode: the NextJS node application, and the client/browser application.

Start your development server as usual by

*[Content truncated - see full docs]*

**Examples**:

```text
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Next.js: debug server-side",
      "type": "node-terminal",
      "request": "launch",
      "command": "npm run dev"
    },
    {
      "name": "Next.js: debug client-side",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:3000"
    },
    {
      "name": "Next.js: debug client-side (Firefox)",
      "type": "firefox",
      "request": "launch",
      "url": "http://localhost:3000",
      "reAtta
...
```

```text
NODE_OPTIONS='--inspect' next dev
```

```text
{
  "scripts": {
    "dev": "NODE_OPTIONS='--inspect' next dev"
  }
}
```

---

## Guides: Development Environment | Next.js

**URL**: https://nextjs.org/docs/app/guides/local-development

**Contents**:
- How to optimize your local development environment
- Local dev vs. production
- Improving local dev performance
  - 1. Check your computer's antivirus
  - 2. Update Next.js and enable Turbopack
  - 3. Check your imports
    - Icon libraries
    - Barrel files

Features available in /app

Next.js is designed to provide a great developer experience. As your application grows, you might notice slower compilation times during local development. This guide will help you identify and fix common compile-time performance issues.

The development process with next dev is different than next build and next start.

next dev compiles routes in your application as you open or navigate to them. This enables you to start the dev server without waiting for every route in your application to compile, which is both faster and uses less memory. Running a production build applies other optimizations, like minifying files and creating content hashes, which are not needed for local development.

Antivirus software can slow down file access.

Try adding your project folder to the antivirus exclusion list. While this is more common on Windows machines, we recommend this for any system with an antivirus tool installed.

Make sure you're using the latest version of Next.js. Each new version often includes performance improvements.

Turbopack is a new bundler integrated into Next.js that can improve local performance.

Learn more about Turbopack. See our upgrade guides and codemods for more information.

The way you import code can greatly affect compilation and bundling time. Learn more about optimizing package bundling and explore tools like Dependency Cruiser or Madge.

Libraries like @material-ui/icons, @phosphor-icons/react, or react-icons can import thousands of icons, even if you only use a few. Try to import only the icons you need:

You can often find what import pattern to use in the documentation for the icon library you're using. This example follows @phosphor-icons/react recommendation.

Libraries like react-icons includes many different icon sets. Choose one set and stick with that set.

For example, if your application uses react-icons and imports all of these:

Combined they will be tens of thousands of modules that the compiler has

*[Content truncated - see full docs]*

**Examples**:

```text
npm install next@latest
npm run dev --turbopack
```

```python
// Instead of this:
import { TriangleIcon } from '@phosphor-icons/react'
 
// Do this:
import { TriangleIcon } from '@phosphor-icons/react/dist/csr/Triangle'
```

```text
module.exports = {
  experimental: {
    optimizePackageImports: ['package-name'],
  },
}
```

---

## Guides: Draft Mode | Next.js

**URL**: https://nextjs.org/docs/app/guides/draft-mode

**Contents**:
- How to preview content with Draft Mode in Next.js
- Step 1: Create a Route Handler
- Step 2: Access the Route Handler from your Headless CMS
- Step 3: Preview the Draft Content
- Next Steps
  - draftMode

Features available in /app

Draft Mode allows you to preview draft content from your headless CMS in your Next.js application. This is useful for static pages that are generated at build time as it allows you to switch to dynamic rendering and see the draft changes without having to rebuild your entire site.

This page walks through how to enable and use Draft Mode.

Create a Route Handler. It can have any name, for example, app/api/draft/route.ts.

Then, import the draftMode function and call the enable() method.

This will set a cookie to enable draft mode. Subsequent requests containing this cookie will trigger draft mode and change the behavior of statically generated pages.

You can test this manually by visiting /api/draft and looking at your browser’s developer tools. Notice the Set-Cookie response header with a cookie named __prerender_bypass.

These steps assume that the headless CMS you’re using supports setting custom draft URLs. If it doesn’t, you can still use this method to secure your draft URLs, but you’ll need to construct and access the draft URL manually. The specific steps will vary depending on which headless CMS you’re using.

To securely access the Route Handler from your headless CMS:

Your headless CMS might allow you to include a variable in the draft URL so that <path> can be set dynamically based on the CMS’s data like so: &slug=/posts/{entry.fields.slug}

If it succeeds, then the browser will be redirected to the path you want to view with the draft mode cookie.

The next step is to update your page to check the value of draftMode().isEnabled.

If you request a page which has the cookie set, then data will be fetched at request time (instead of at build time).

Furthermore, the value of isEnabled will be true.

If you access the draft Route Handler (with secret and slug) from your headless CMS or manually using the URL, you should now be able to see the draft content. And, if you update your draft without publishing, you should be able t

*[Content truncated - see full docs]*

**Examples**:

```javascript
export async function GET(request: Request) {
  return new Response('')
}
```

```python
import { draftMode } from 'next/headers'
 
export async function GET(request: Request) {
  const draft = await draftMode()
  draft.enable()
  return new Response('Draft mode is enabled')
}
```

```text
https://<your-site>/api/draft?secret=<token>&slug=<path>
```

---

## Guides: Environment Variables | Next.js

**URL**: https://nextjs.org/docs/app/guides/environment-variables

**Contents**:
- How to use environment variables in Next.js
- Loading Environment Variables
  - Loading Environment Variables with @next/env
  - Referencing Other Variables
- Bundling Environment Variables for the Browser
  - Runtime Environment Variables
- Test Environment Variables
- Environment Variable Load Order

Features available in /app

Next.js comes with built-in support for environment variables, which allows you to do the following:

Warning: The default create-next-app template ensures all .env files are added to your .gitignore. You almost never want to commit these files to your repository.

Next.js has built-in support for loading environment variables from .env* files into process.env.

Note: Next.js also supports multiline variables inside of your .env* files:

Note: If you are using a /src folder, please note that Next.js will load the .env files only from the parent folder and not from the /src folder. This loads process.env.DB_HOST, process.env.DB_USER, and process.env.DB_PASS into the Node.js environment automatically allowing you to use them in Route Handlers.

If you need to load environment variables outside of the Next.js runtime, such as in a root config file for an ORM or test runner, you can use the @next/env package.

This package is used internally by Next.js to load environment variables from .env* files.

To use it, install the package and use the loadEnvConfig function to load the environment variables:

Then, you can import the configuration where needed. For example:

Next.js will automatically expand variables that use $ to reference other variables e.g. $VARIABLE inside of your .env* files. This allows you to reference other secrets. For example:

In the above example, process.env.TWITTER_URL would be set to https://x.com/nextjs.

Good to know: If you need to use variable with a $ in the actual value, it needs to be escaped e.g. \$.

Non-NEXT_PUBLIC_ environment variables are only available in the Node.js environment, meaning they aren't accessible to the browser (the client runs in a different environment).

In order to make the value of an environment variable accessible in the browser, Next.js can "inline" a value, at build time, into the js bundle that is delivered to the client, replacing all references to process.env.[variable] with a h

*[Content truncated - see full docs]*

**Examples**:

```text
DB_HOST=localhost
DB_USER=myuser
DB_PASS=mypassword
```

```text
# .env
 
# you can write with line breaks
PRIVATE_KEY="-----BEGIN RSA PRIVATE KEY-----
...
Kh9NV...
...
-----END DSA PRIVATE KEY-----"
 
# or with `\n` inside double quotes
PRIVATE_KEY="-----BEGIN RSA PRIVATE KEY-----\nKh9NV...\n-----END DSA PRIVATE KEY-----\n"
```

```javascript
export async function GET() {
  const db = await myDB.connect({
    host: process.env.DB_HOST,
    username: process.env.DB_USER,
    password: process.env.DB_PASS,
  })
  // ...
}
```

---

## Guides: Forms | Next.js

**URL**: https://nextjs.org/docs/app/guides/forms

**Contents**:
- How to create forms with Server Actions
- How it works
- Passing additional arguments
- Form validation
- Validation errors
- Pending states
- Optimistic updates
- Nested form elements

Features available in /app

React Server Actions are Server Functions that execute on the server. They can be called in Server and Client Components to handle form submissions. This guide will walk you through how to create forms in Next.js with Server Actions.

React extends the HTML <form> element to allow Server Actions to be invoked with the action attribute.

When used in a form, the function automatically receives the FormData object. You can then extract the data using the native FormData methods:

Good to know: When working with forms that have multiple fields, use JavaScript's Object.fromEntries(). For example: const rawFormData = Object.fromEntries(formData). Note that this object will contain extra properties prefixed with $ACTION_.

Outside of form fields, you can pass additional arguments to a Server Function using the JavaScript bind method. For example, to pass the userId argument to the updateUser Server Function:

The Server Function will receive the userId as an additional argument:

Forms can be validated on the client or server.

To display validation errors or messages, turn the component that defines the <form> into a Client Component and use React useActionState.

When using useActionState, the Server function signature will change to receive a new prevState or initialState parameter as its first argument.

You can then conditionally render the error message based on the state object.

The useActionState hook exposes a pending boolean that can be used to show a loading indicator or disable the submit button while the action is being executed.

Alternatively, you can use the useFormStatus hook to show a loading indicator while the action is being executed. When using this hook, you'll need to create a separate component to render the loading indicator. For example, to disable the button when the action is pending:

You can then nest the SubmitButton component inside the form:

Good to know: In React 19, useFormStatus includes additional keys on

*[Content truncated - see full docs]*

**Examples**:

```javascript
export default function Page() {
  async function createInvoice(formData: FormData) {
    'use server'
 
    const rawFormData = {
      customerId: formData.get('customerId'),
      amount: formData.get('amount'),
      status: formData.get('status'),
    }
 
    // mutate data
    // revalidate the cache
  }
 
  return <form action={createInvoice}>...</form>
}
```

```python
'use client'
 
import { updateUser } from './actions'
 
export function UserProfile({ userId }: { userId: string }) {
  const updateUserWithId = updateUser.bind(null, userId)
 
  return (
    <form action={updateUserWithId}>
      <input type="text" name="name" />
      <button type="submit">Update User Name</button>
    </form>
  )
}
```

```javascript
'use server'
 
export async function updateUser(userId: string, formData: FormData) {}
```

---

## Guides: ISR | Next.js

**URL**: https://nextjs.org/docs/app/guides/incremental-static-regeneration

**Contents**:
- How to implement Incremental Static Regeneration (ISR)
- Reference
  - Route segment config
  - Functions
- Examples
  - Time-based revalidation
  - On-demand revalidation with revalidatePath
  - On-demand revalidation with revalidateTag

Features available in /app

Incremental Static Regeneration (ISR) enables you to:

Here's a minimal example:

Here's how this example works:

This fetches and displays a list of blog posts on /blog. After an hour has passed, the next visitor will still receive the cached (stale) version of the page immediately for a fast response. Simultaneously, Next.js triggers regeneration of a fresh version in the background. Once the new version is successfully generated, it replaces the cached version, and subsequent visitors will receive the updated content.

We recommend setting a high revalidation time. For instance, 1 hour instead of 1 second. If you need more precision, consider using on-demand revalidation. If you need real-time data, consider switching to dynamic rendering.

For a more precise method of revalidation, invalidate cached pages on-demand with the revalidatePath function.

For example, this Server Action would get called after adding a new post. Regardless of how you retrieve your data in your Server Component, either using fetch or connecting to a database, this will invalidate the cache for the entire route. The next request to that route will trigger regeneration and serve fresh data, which will then be cached for subsequent requests.

Note: revalidatePath invalidates the cache entries but regeneration happens on the next request. If you want to eagerly regenerate the cache entry immediately instead of waiting for the next request, you can use the Pages router res.revalidate method. We're working on adding new methods to provide eager regeneration capabilities for the App Router.

View a demo and explore the source code.

For most use cases, prefer revalidating entire paths. If you need more granular control, you can use the revalidateTag function. For example, you can tag individual fetch calls:

If you are using an ORM or connecting to a database, you can use unstable_cache:

You can then use revalidateTag in a Server Actions or Route Handler:

If an er

*[Content truncated - see full docs]*

**Examples**:

```javascript
interface Post {
  id: string
  title: string
  content: string
}
 
// Next.js will invalidate the cache when a
// request comes in, at most once every 60 seconds.
export const revalidate = 60
 
export async function generateStaticParams() {
  const posts: Post[] = await fetch('https://api.vercel.app/blog').then((res) =>
    res.json()
  )
  return posts.map((post) => ({
    id: String(post.id),
  }))
}
 
export default async function Page({
  params,
}: {
  params: Promise<{ id: string }>
}) {

...
```

```javascript
interface Post {
  id: string
  title: string
  content: string
}
 
export const revalidate = 3600 // invalidate every hour
 
export default async function Page() {
  const data = await fetch('https://api.vercel.app/blog')
  const posts: Post[] = await data.json()
  return (
    <main>
      <h1>Blog Posts</h1>
      <ul>
        {posts.map((post) => (
          <li key={post.id}>{post.title}</li>
        ))}
      </ul>
    </main>
  )
}
```

```python
'use server'
 
import { revalidatePath } from 'next/cache'
 
export async function createPost() {
  // Invalidate the cache for the /posts route
  revalidatePath('/posts')
}
```

---

## Guides: Instrumentation | Next.js

**URL**: https://nextjs.org/docs/app/guides/instrumentation

**Contents**:
- How to set up instrumentation
- Convention
- Examples
  - Importing files with side effects
  - Importing runtime-specific code
- Learn more about Instrumentation
  - instrumentation.js

Features available in /app

Instrumentation is the process of using code to integrate monitoring and logging tools into your application. This allows you to track the performance and behavior of your application, and to debug issues in production.

To set up instrumentation, create instrumentation.ts|js file in the root directory of your project (or inside the src folder if using one).

Then, export a register function in the file. This function will be called once when a new Next.js server instance is initiated.

For example, to use Next.js with OpenTelemetry and @vercel/otel:

See the Next.js with OpenTelemetry example for a complete implementation.

Sometimes, it may be useful to import a file in your code because of the side effects it will cause. For example, you might import a file that defines a set of global variables, but never explicitly use the imported file in your code. You would still have access to the global variables the package has declared.

We recommend importing files using JavaScript import syntax within your register function. The following example demonstrates a basic usage of import in a register function:

We recommend importing the file from within the register function, rather than at the top of the file. By doing this, you can colocate all of your side effects in one place in your code, and avoid any unintended consequences from importing globally at the top of the file.

Next.js calls register in all environments, so it's important to conditionally import any code that doesn't support specific runtimes (e.g. Edge or Node.js). You can use the NEXT_RUNTIME environment variable to get the current environment:

**Examples**:

```python
import { registerOTel } from '@vercel/otel'
 
export function register() {
  registerOTel('next-app')
}
```

```javascript
export async function register() {
  await import('package-with-side-effect')
}
```

```javascript
export async function register() {
  if (process.env.NEXT_RUNTIME === 'nodejs') {
    await import('./instrumentation-node')
  }
 
  if (process.env.NEXT_RUNTIME === 'edge') {
    await import('./instrumentation-edge')
  }
}
```

---

## Guides: Internationalization | Next.js

**URL**: https://nextjs.org/docs/app/guides/internationalization

**Contents**:
- Internationalization
- Terminology
- Routing Overview
- Localization
- Static Rendering
- Resources

Features available in /app

Next.js enables you to configure the routing and rendering of content to support multiple languages. Making your site adaptive to different locales includes translated content (localization) and internationalized routes.

It’s recommended to use the user’s language preferences in the browser to select which locale to use. Changing your preferred language will modify the incoming Accept-Language header to your application.

For example, using the following libraries, you can look at an incoming Request to determine which locale to select, based on the Headers, locales you plan to support, and the default locale.

Routing can be internationalized by either the sub-path (/fr/products) or domain (my-site.fr/products). With this information, you can now redirect the user based on the locale inside Middleware.

Finally, ensure all special files inside app/ are nested under app/[lang]. This enables the Next.js router to dynamically handle different locales in the route, and forward the lang parameter to every layout and page. For example:

The root layout can also be nested in the new folder (e.g. app/[lang]/layout.js).

Changing displayed content based on the user’s preferred locale, or localization, is not something specific to Next.js. The patterns described below would work the same with any web application.

Let’s assume we want to support both English and Dutch content inside our application. We might maintain two different “dictionaries”, which are objects that give us a mapping from some key to a localized string. For example:

We can then create a getDictionary function to load the translations for the requested locale:

Given the currently selected language, we can fetch the dictionary inside of a layout or page.

Because all layouts and pages in the app/ directory default to Server Components, we do not need to worry about the size of the translation files affecting our client-side JavaScript bundle size. This code will only run on th

*[Content truncated - see full docs]*

**Examples**:

```python
import { match } from '@formatjs/intl-localematcher'
import Negotiator from 'negotiator'
 
let headers = { 'accept-language': 'en-US,en;q=0.5' }
let languages = new Negotiator({ headers }).languages()
let locales = ['en-US', 'nl-NL', 'nl']
let defaultLocale = 'en-US'
 
match(languages, locales, defaultLocale) // -> 'en-US'
```

```python
import { NextResponse } from "next/server";
 
let locales = ['en-US', 'nl-NL', 'nl']
 
// Get the preferred locale, similar to the above or using a library
function getLocale(request) { ... }
 
export function middleware(request) {
  // Check if there is any supported locale in the pathname
  const { pathname } = request.nextUrl
  const pathnameHasLocale = locales.some(
    (locale) => pathname.startsWith(`/${locale}/`) || pathname === `/${locale}`
  )
 
  if (pathnameHasLocale) return
 
  // Re
...
```

```javascript
// You now have access to the current locale
// e.g. /en-US/products -> `lang` is "en-US"
export default async function Page({
  params,
}: {
  params: Promise<{ lang: string }>
}) {
  const { lang } = await params
  return ...
}
```

---

## Guides: JSON-LD | Next.js

**URL**: https://nextjs.org/docs/app/guides/json-ld

**Contents**:
- How to implement JSON-LD in your Next.js application

Features available in /app

JSON-LD is a format for structured data that can be used by search engines and AI to help them understand the structure of the page beyond pure content. For example, you can use it to describe a person, an event, an organization, a movie, a book, a recipe, and many other types of entities.

Our current recommendation for JSON-LD is to render structured data as a <script> tag in your layout.js or page.js components.

The following snippet uses JSON.stringify, which does not sanitize malicious strings used in XSS injection. To prevent this type of vulnerability, you can scrub HTML tags from the JSON-LD payload, for example, by replacing the character, <, with its unicode equivalent, \u003c.

Review your organization's recommended approach to sanitize potentially dangerous strings, or use community maintained alternatives for JSON.stringify such as, serialize-javascript.

You can validate and test your structured data with the Rich Results Test for Google or the generic Schema Markup Validator.

You can type your JSON-LD with TypeScript using community packages like schema-dts:

**Examples**:

```javascript
export default async function Page({ params }) {
  const { id } = await params
  const product = await getProduct(id)
 
  const jsonLd = {
    '@context': 'https://schema.org',
    '@type': 'Product',
    name: product.name,
    image: product.image,
    description: product.description,
  }
 
  return (
    <section>
      {/* Add JSON-LD to your page */}
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify(jsonLd).replace(/</g, '\
...
```

```python
import { Product, WithContext } from 'schema-dts'
 
const jsonLd: WithContext<Product> = {
  '@context': 'https://schema.org',
  '@type': 'Product',
  name: 'Next.js Sticker',
  image: 'https://nextjs.org/imgs/sticker.png',
  description: 'Dynamic at the speed of static.',
}
```

---

## Guides: Lazy Loading | Next.js

**URL**: https://nextjs.org/docs/app/guides/lazy-loading

**Contents**:
- How to lazy load Client Components and libraries
- next/dynamic
- Examples
  - Importing Client Components
  - Skipping SSR
  - Importing Server Components
  - Loading External Libraries
  - Adding a custom loading component

Features available in /app

Lazy loading in Next.js helps improve the initial loading performance of an application by decreasing the amount of JavaScript needed to render a route.

It allows you to defer loading of Client Components and imported libraries, and only include them in the client bundle when they're needed. For example, you might want to defer loading a modal until a user clicks to open it.

There are two ways you can implement lazy loading in Next.js:

By default, Server Components are automatically code split, and you can use streaming to progressively send pieces of UI from the server to the client. Lazy loading applies to Client Components.

next/dynamic is a composite of React.lazy() and Suspense. It behaves the same way in the app and pages directories to allow for incremental migration.

Note: When a Server Component dynamically imports a Client Component, automatic code splitting is currently not supported.

When using React.lazy() and Suspense, Client Components will be prerendered (SSR) by default.

Note: ssr: false option will only work for Client Components, move it into Client Components ensure the client code-splitting working properly.

If you want to disable pre-rendering for a Client Component, you can use the ssr option set to false:

If you dynamically import a Server Component, only the Client Components that are children of the Server Component will be lazy-loaded - not the Server Component itself. It will also help preload the static assets such as CSS when you're using it in Server Components.

Note: ssr: false option is not supported in Server Components. You will see an error if you try to use it in Server Components. ssr: false is not allowed with next/dynamic in Server Components. Please move it into a Client Component.

External libraries can be loaded on demand using the import() function. This example uses the external library fuse.js for fuzzy search. The module is only loaded on the client after the user types in the sear

*[Content truncated - see full docs]*

**Examples**:

```python
'use client'
 
import { useState } from 'react'
import dynamic from 'next/dynamic'
 
// Client Components:
const ComponentA = dynamic(() => import('../components/A'))
const ComponentB = dynamic(() => import('../components/B'))
const ComponentC = dynamic(() => import('../components/C'), { ssr: false })
 
export default function ClientComponentExample() {
  const [showMore, setShowMore] = useState(false)
 
  return (
    <div>
      {/* Load immediately, but in a separate client bundle */}
      <
...
```

```javascript
const ComponentC = dynamic(() => import('../components/C'), { ssr: false })
```

```python
import dynamic from 'next/dynamic'
 
// Server Component:
const ServerComponent = dynamic(() => import('../components/ServerComponent'))
 
export default function ServerComponentExample() {
  return (
    <div>
      <ServerComponent />
    </div>
  )
}
```

---

## Guides: MDX | Next.js

**URL**: https://nextjs.org/docs/app/guides/mdx

**Contents**:
- How to use markdown and MDX in Next.js
- Install dependencies
- Configure next.config.mjs
  - Handling .md files
- Add an mdx-components.tsx file
- Rendering MDX
  - Using file based routing
  - Using imports

Features available in /app

Markdown is a lightweight markup language used to format text. It allows you to write using plain text syntax and convert it to structurally valid HTML. It's commonly used for writing content on websites and blogs.

MDX is a superset of markdown that lets you write JSX directly in your markdown files. It is a powerful way to add dynamic interactivity and embed React components within your content.

Next.js can support both local MDX content inside your application, as well as remote MDX files fetched dynamically on the server. The Next.js plugin handles transforming markdown and React components into HTML, including support for usage in Server Components (the default in App Router).

Good to know: View the Portfolio Starter Kit template for a complete working example.

The @next/mdx package, and related packages, are used to configure Next.js so it can process markdown and MDX. It sources data from local files, allowing you to create pages with a .md or .mdx extension, directly in your /pages or /app directory.

Install these packages to render MDX with Next.js:

Update the next.config.mjs file at your project's root to configure it to use MDX:

This allows .mdx files to act as pages, routes, or imports in your application.

By default, next/mdx only compiles files with the .mdx extension. To handle .md files with webpack, update the extension option:

Create an mdx-components.tsx (or .js) file in the root of your project to define global MDX Components. For example, at the same level as pages or app, or inside src if applicable.

You can render MDX using Next.js's file based routing or by importing MDX files into other pages.

When using file based routing, you can use MDX pages like any other page.

In App Router apps, that includes being able to use metadata.

Create a new MDX page within the /app directory:

You can use MDX in these files, and even import React components, directly inside your MDX page:

Navigating to the /mdx-page ro

*[Content truncated - see full docs]*

**Examples**:

```text
I **love** using [Next.js](https://nextjs.org/)
```

```text
<p>I <strong>love</strong> using <a href="https://nextjs.org/">Next.js</a></p>
```

```text
npm install @next/mdx @mdx-js/loader @mdx-js/react @types/mdx
```

---

## Guides: Memory Usage | Next.js

**URL**: https://nextjs.org/docs/app/guides/memory-usage

**Contents**:
- How to optimize memory usage
- Reduce number of dependencies
- Try experimental.webpackMemoryOptimizations
- Run next build with --experimental-debug-memory-usage
- Record a heap profile
- Analyze a snapshot of the heap
- Webpack build worker
- Disable Webpack cache

Features available in /app

As applications grow and become more feature rich, they can demand more resources when developing locally or creating production builds.

Let's explore some strategies and techniques to optimize memory and address common memory issues in Next.js.

Applications with a large amount of dependencies will use more memory.

The Bundle Analyzer can help you investigate large dependencies in your application that may be able to be removed to improve performance and memory usage.

Starting in v15.0.0, you can add experimental.webpackMemoryOptimizations: true to your next.config.js file to change behavior in Webpack that reduces max memory usage but may increase compilation times by a slight amount.

Good to know: This feature is currently experimental to test on more projects first, but it is considered to be low-risk.

Starting in 14.2.0, you can run next build --experimental-debug-memory-usage to run the build in a mode where Next.js will print out information about memory usage continuously throughout the build, such as heap usage and garbage collection statistics. Heap snapshots will also be taken automatically when memory usage gets close to the configured limit.

Good to know: This feature is not compatible with the Webpack build worker option which is auto-enabled unless you have custom webpack config.

To look for memory issues, you can record a heap profile from Node.js and load it in Chrome DevTools to identify potential sources of memory leaks.

In your terminal, pass the --heap-prof flag to Node.js when starting your Next.js build:

At the end of the build, a .heapprofile file will be created by Node.js.

In Chrome DevTools, you can open the Memory tab and click on the "Load Profile" button to visualize the file.

You can use an inspector tool to analyze the memory usage of the application.

When running the next build or next dev command, add NODE_OPTIONS=--inspect to the beginning of the command. This will expose the inspector agent 

*[Content truncated - see full docs]*

**Examples**:

```text
node --heap-prof node_modules/next/dist/bin/next build
```

```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  webpack: (
    config,
    { buildId, dev, isServer, defaultLoaders, nextRuntime, webpack }
  ) => {
    if (config.cache && !dev) {
      config.cache = Object.freeze({
        type: 'memory',
      })
    }
    // Important: return the modified config
    return config
  },
}
 
export default nextConfig
```

```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  eslint: {
    // Warning: This allows production builds to successfully complete even if
    // your project has ESLint errors.
    ignoreDuringBuilds: true,
  },
  typescript: {
    // !! WARN !!
    // Dangerously allow production builds to successfully complete even if
    // your project has type errors.
    // !! WARN !!
    ignoreBuildErrors: true,
  },
}
 
export default nextConfig
```

---

## Guides: Migrating | Next.js

**URL**: https://nextjs.org/docs/app/guides/migrating

**Contents**:
- Migrating
  - App Router
  - Create React App
  - Vite

Features available in /app

---

## Guides: Multi-tenant | Next.js

**URL**: https://nextjs.org/docs/app/guides/multi-tenant

**Contents**:
- How to build multi-tenant apps in Next.js

Features available in /app

If you are looking to build a single Next.js application that serves multiple tenants, we have built an example showing our recommended architecture.

---

## Guides: Multi-zones | Next.js

**URL**: https://nextjs.org/docs/app/guides/multi-zones

**Contents**:
- How to build micro-frontends using multi-zones and Next.js
- How to define a zone
- How to route requests to the right zone
  - Routing requests using middleware
- Linking between zones
- Sharing code
- Server Actions

Features available in /app

Multi-Zones are an approach to micro-frontends that separate a large application on a domain into smaller Next.js applications that each serve a set of paths. This is useful when there are collections of pages unrelated to the other pages in the application. By moving those pages to a separate zone (i.e., a separate application), you can reduce the size of each application which improves build times and removes code that is only necessary for one of the zones. Since applications are decoupled, Multi-Zones also allows other applications on the domain to use their own choice of framework.

For example, let's say you have the following set of pages that you would like to split up:

With Multi-Zones support, you can create three applications that all are served on the same domain and look the same to the user, but you can develop and deploy each of the applications independently.

Navigating between pages in the same zone will perform soft navigations, a navigation that does not require reloading the page. For example, in this diagram, navigating from / to /products will be a soft navigation.

Navigating from a page in one zone to a page in another zone, such as from / to /dashboard, will perform a hard navigation, unloading the resources of the current page and loading the resources of the new page. Pages that are frequently visited together should live in the same zone to avoid hard navigations.

A zone is a normal Next.js application where you also configure an assetPrefix to avoid conflicts with pages and static files in other zones.

Next.js assets, such as JavaScript and CSS, will be prefixed with assetPrefix to make sure that they don't conflict with assets from other zones. These assets will be served under /assetPrefix/_next/... for each of the zones.

The default application handling all paths not routed to another more specific zone does not need an assetPrefix.

In versions older than Next.js 15, you may also need an additional re

*[Content truncated - see full docs]*

**Examples**:

```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  assetPrefix: '/blog-static',
}
```

```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  assetPrefix: '/blog-static',
  async rewrites() {
    return {
      beforeFiles: [
        {
          source: '/blog-static/_next/:path+',
          destination: '/_next/:path+',
        },
      ],
    }
  },
}
```

```text
async rewrites() {
    return [
        {
            source: '/blog',
            destination: `${process.env.BLOG_DOMAIN}/blog`,
        },
        {
            source: '/blog/:path+',
            destination: `${process.env.BLOG_DOMAIN}/blog/:path+`,
        },
        {
            source: '/blog-static/:path+',
            destination: `${process.env.BLOG_DOMAIN}/blog-static/:path+`,
        }
    ];
}
```

---

## Guides: OpenTelemetry | Next.js

**URL**: https://nextjs.org/docs/app/guides/open-telemetry

**Contents**:
- How to set up instrumentation with OpenTelemetry
- Getting Started
  - Using @vercel/otel
  - Manual OpenTelemetry configuration
- Testing your instrumentation
- Deployment
  - Using OpenTelemetry Collector
    - Deploying on Vercel

Features available in /app

Observability is crucial for understanding and optimizing the behavior and performance of your Next.js app.

As applications become more complex, it becomes increasingly difficult to identify and diagnose issues that may arise. By leveraging observability tools, such as logging and metrics, developers can gain insights into their application's behavior and identify areas for optimization. With observability, developers can proactively address issues before they become major problems and provide a better user experience. Therefore, it is highly recommended to use observability in your Next.js applications to improve performance, optimize resources, and enhance user experience.

We recommend using OpenTelemetry for instrumenting your apps. It's a platform-agnostic way to instrument apps that allows you to change your observability provider without changing your code. Read Official OpenTelemetry docs for more information about OpenTelemetry and how it works.

This documentation uses terms like Span, Trace or Exporter throughout this doc, all of which can be found in the OpenTelemetry Observability Primer.

Next.js supports OpenTelemetry instrumentation out of the box, which means that we already instrumented Next.js itself.

OpenTelemetry is extensible but setting it up properly can be quite verbose. That's why we prepared a package @vercel/otel that helps you get started quickly.

To get started, install the following packages:

Next, create a custom instrumentation.ts (or .js) file in the root directory of the project (or inside src folder if using one):

See the @vercel/otel documentation for additional configuration options.

The @vercel/otel package provides many configuration options and should serve most of common use cases. But if it doesn't suit your needs, you can configure OpenTelemetry manually.

Firstly you need to install OpenTelemetry packages:

Now you can initialize NodeSDK in your instrumentation.ts. Unlike @vercel/otel, No

*[Content truncated - see full docs]*

**Examples**:

```text
npm install @vercel/otel @opentelemetry/sdk-logs @opentelemetry/api-logs @opentelemetry/instrumentation
```

```python
import { registerOTel } from '@vercel/otel'
 
export function register() {
  registerOTel({ serviceName: 'next-app' })
}
```

```text
npm install @opentelemetry/sdk-node @opentelemetry/resources @opentelemetry/semantic-conventions @opentelemetry/sdk-trace-node @opentelemetry/exporter-trace-otlp-http
```

---

## Guides: PWAs | Next.js

**URL**: https://nextjs.org/docs/app/guides/progressive-web-apps

**Contents**:
- How to build a Progressive Web Application (PWA) with Next.js
- Creating a PWA with Next.js
  - 1. Creating the Web App Manifest
  - 2. Implementing Web Push Notifications
  - 3. Implementing Server Actions
  - 4. Generating VAPID Keys
  - 5. Creating a Service Worker
  - 6. Adding to Home Screen

Features available in /app

Progressive Web Applications (PWAs) offer the reach and accessibility of web applications combined with the features and user experience of native mobile apps. With Next.js, you can create PWAs that provide a seamless, app-like experience across all platforms without the need for multiple codebases or app store approvals.

Next.js provides built-in support for creating a web app manifest using the App Router. You can create either a static or dynamic manifest file:

For example, create a app/manifest.ts or app/manifest.json file:

This file should contain information about the name, icons, and how it should be displayed as an icon on the user's device. This will allow users to install your PWA on their home screen, providing a native app-like experience.

You can use tools like favicon generators to create the different icon sets and place the generated files in your public/ folder.

Web Push Notifications are supported with all modern browsers, including:

This makes PWAs a viable alternative to native apps. Notably, you can trigger install prompts without needing offline support.

Web Push Notifications allow you to re-engage users even when they're not actively using your app. Here's how to implement them in a Next.js application:

First, let's create the main page component in app/page.tsx. We'll break it down into smaller parts for better understanding. First, we’ll add some of the imports and utilities we’ll need. It’s okay that the referenced Server Actions do not yet exist:

Let’s now add a component to manage subscribing, unsubscribing, and sending push notifications.

Finally, let’s create a component to show a message for iOS devices to instruct them to install to their home screen, and only show this if the app is not already installed.

Now, let’s create the Server Actions which this file calls.

Create a new file to contain your actions at app/actions.ts. This file will handle creating subscriptions, deleting subscriptions, 

*[Content truncated - see full docs]*

**Examples**:

```python
import type { MetadataRoute } from 'next'
 
export default function manifest(): MetadataRoute.Manifest {
  return {
    name: 'Next.js PWA',
    short_name: 'NextPWA',
    description: 'A Progressive Web App built with Next.js',
    start_url: '/',
    display: 'standalone',
    background_color: '#ffffff',
    theme_color: '#000000',
    icons: [
      {
        src: '/icon-192x192.png',
        sizes: '192x192',
        type: 'image/png',
      },
      {
        src: '/icon-512x512.png',
    
...
```

```python
'use client'
 
import { useState, useEffect } from 'react'
import { subscribeUser, unsubscribeUser, sendNotification } from './actions'
 
function urlBase64ToUint8Array(base64String: string) {
  const padding = '='.repeat((4 - (base64String.length % 4)) % 4)
  const base64 = (base64String + padding).replace(/-/g, '+').replace(/_/g, '/')
 
  const rawData = window.atob(base64)
  const outputArray = new Uint8Array(rawData.length)
 
  for (let i = 0; i < rawData.length; ++i) {
    outputArray[i] = 
...
```

```javascript
function PushNotificationManager() {
  const [isSupported, setIsSupported] = useState(false)
  const [subscription, setSubscription] = useState<PushSubscription | null>(
    null
  )
  const [message, setMessage] = useState('')
 
  useEffect(() => {
    if ('serviceWorker' in navigator && 'PushManager' in window) {
      setIsSupported(true)
      registerServiceWorker()
    }
  }, [])
 
  async function registerServiceWorker() {
    const registration = await navigator.serviceWorker.register('/
...
```

---

## Guides: Package Bundling | Next.js

**URL**: https://nextjs.org/docs/app/guides/package-bundling

**Contents**:
- How to optimize package bundling
- Analyzing JavaScript bundles
  - Installation
  - Generating a report
- Optimizing package imports
- Opting specific packages out of bundling
- Next Steps
  - Production

Features available in /app

Bundling external packages can significantly improve the performance of your application. By default, packages imported inside Server Components and Route Handlers are automatically bundled by Next.js. This page will guide you through how to analyze and further optimize package bundling.

@next/bundle-analyzer is a plugin for Next.js that helps you manage the size of your application bundles. It generates a visual report of the size of each package and their dependencies. You can use the information to remove large dependencies, split, or lazy-load your code.

Install the plugin by running the following command:

Then, add the bundle analyzer's settings to your next.config.js.

Run the following command to analyze your bundles:

The report will open three new tabs in your browser, which you can inspect. Periodically evaluating your application's bundles can help you maintain application performance over time.

Some packages, such as icon libraries, can export hundreds of modules, which can cause performance issues in development and production.

You can optimize how these packages are imported by adding the optimizePackageImports option to your next.config.js. This option will only load the modules you actually use, while still giving you the convenience of writing import statements with many named exports.

Next.js also optimizes some libraries automatically, thus they do not need to be included in the optimizePackageImports list. See the full list.

Since packages imported inside Server Components and Route Handlers are automatically bundled by Next.js, you can opt specific packages out of bundling using the serverExternalPackages option in your next.config.js.

Next.js includes a list of popular packages that currently are working on compatibility and automatically opt-ed out. See the full list.

**Examples**:

```text
npm i @next/bundle-analyzer
# or
yarn add @next/bundle-analyzer
# or
pnpm add @next/bundle-analyzer
```

```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {}
 
const withBundleAnalyzer = require('@next/bundle-analyzer')({
  enabled: process.env.ANALYZE === 'true',
})
 
module.exports = withBundleAnalyzer(nextConfig)
```

```text
ANALYZE=true npm run build
# or
ANALYZE=true yarn build
# or
ANALYZE=true pnpm build
```

---

## Guides: Prefetching | Next.js

**URL**: https://nextjs.org/docs/app/guides/prefetching

**Contents**:
- Prefetching
- How does prefetching work?
- Prefetching static vs. dynamic routes
- Automatic prefetch
- Manual prefetch
- Hover-triggered prefetch
- Extending or ejecting link
- Disabled prefetch

Features available in /app

Prefetching makes navigating between different routes in your application feel instant. Next.js tries to intelligently prefetch by default, based on the links used in your application code.

This guide will explain how prefetching works and show common implementation patterns:

When navigating between routes, the browser requests assets for the page like HTML and JavaScript files. Prefetching is the process of fetching these resources ahead of time, before you navigate to a new route.

Next.js automatically splits your application into smaller JavaScript chunks based on routes. Instead of loading all the code upfront like traditional SPAs, only the code needed for the current route is loaded. This reduces the initial load time while other parts of the app are loaded in the background. By the time you click the link, the resources for the new route have already been loaded into the browser cache.

When navigating to the new page, there's no full page reload or browser loading spinner. Instead, Next.js performs a client-side transition, making the page navigation feel instant.

Good to know: During the initial navigation, the browser fetches the HTML, JavaScript, and React Server Components (RSC) Payload. For subsequent navigations, the browser will fetch the RSC Payload for Server Components and JS bundle for Client Components.

Automatic prefetching runs only in production. Disable with prefetch={false} or use the wrapper in Disabled Prefetch.

Call router.prefetch() to warm routes outside the viewport or in response to analytics, hover, scroll, etc.

Proceed with caution: Extending Link opts you into maintaining prefetching, cache invalidation, and accessibility concerns. Proceed only if defaults are insufficient.

Next.js tries to do the right prefetching by default, but power users can eject and modify based on their needs. You have the control between performance and resource consumption.

For example, you might have to only trigger p

*[Content truncated - see full docs]*

**Examples**:

```python
import Link from 'next/link'
 
export default function NavLink() {
  return <Link href="/about">About</Link>
}
```

```python
'use client'
 
import { useRouter } from 'next/navigation'
 
const router = useRouter()
router.prefetch('/pricing')
```

```python
'use client'
 
import Link from 'next/link'
import { useState } from 'react'
 
export function HoverPrefetchLink({
  href,
  children,
}: {
  href: string
  children: React.ReactNode
}) {
  const [active, setActive] = useState(false)
 
  return (
    <Link
      href={href}
      prefetch={active ? null : false}
      onMouseEnter={() => setActive(true)}
    >
      {children}
    </Link>
  )
}
```

---

## Guides: Production | Next.js

**URL**: https://nextjs.org/docs/app/guides/production-checklist

**Contents**:
- How to optimize your Next.js application for production
- Automatic optimizations
- During development
  - Routing and rendering
  - Data fetching and caching
  - UI and accessibility
  - Security
  - Metadata and SEO

Features available in /app

Before taking your Next.js application to production, there are some optimizations and patterns you should consider implementing for the best user experience, performance, and security.

This page provides best practices that you can use as a reference when building your application and before going to production, as well as the automatic Next.js optimizations you should be aware of.

These Next.js optimizations are enabled by default and require no configuration:

These defaults aim to improve your application's performance, and reduce the cost and amount of data transferred on each network request.

While building your application, we recommend using the following features to ensure the best performance and user experience:

Good to know: Partial Prerendering (experimental) will allow parts of a route to be dynamic without opting the whole route into dynamic rendering.

Before going to production, you can run next build to build your application locally and catch any build errors, then run next start to measure the performance of your application in a production-like environment.

Use the @next/bundle-analyzer plugin to analyze the size of your JavaScript bundles and identify large modules and dependencies that might be impacting your application's performance.

Additionally, the following tools can help you understand the impact of adding new dependencies to your application:

---

## Guides: Redirecting | Next.js

**URL**: https://nextjs.org/docs/app/guides/redirecting

**Contents**:
- How to handle redirects in Next.js
- redirect function
- permanentRedirect function
- useRouter() hook
- redirects in next.config.js
- NextResponse.redirect in Middleware
- Managing redirects at scale (advanced)
  - 1. Creating and storing a redirect map

Features available in /app

There are a few ways you can handle redirects in Next.js. This page will go through each available option, use cases, and how to manage large numbers of redirects.

The redirect function allows you to redirect the user to another URL. You can call redirect in Server Components, Route Handlers, and Server Actions.

redirect is often used after a mutation or event. For example, creating a post:

See the redirect API reference for more information.

The permanentRedirect function allows you to permanently redirect the user to another URL. You can call permanentRedirect in Server Components, Route Handlers, and Server Actions.

permanentRedirect is often used after a mutation or event that changes an entity's canonical URL, such as updating a user's profile URL after they change their username:

See the permanentRedirect API reference for more information.

If you need to redirect inside an event handler in a Client Component, you can use the push method from the useRouter hook. For example:

See the useRouter API reference for more information.

The redirects option in the next.config.js file allows you to redirect an incoming request path to a different destination path. This is useful when you change the URL structure of pages or have a list of redirects that are known ahead of time.

redirects supports path, header, cookie, and query matching, giving you the flexibility to redirect users based on an incoming request.

To use redirects, add the option to your next.config.js file:

See the redirects API reference for more information.

Middleware allows you to run code before a request is completed. Then, based on the incoming request, redirect to a different URL using NextResponse.redirect. This is useful if you want to redirect users based on a condition (e.g. authentication, session management, etc) or have a large number of redirects.

For example, to redirect the user to a /login page if they are not authenticated:

See the Middleware 

*[Content truncated - see full docs]*

**Examples**:

```python
'use server'
 
import { redirect } from 'next/navigation'
import { revalidatePath } from 'next/cache'
 
export async function createPost(id: string) {
  try {
    // Call database
  } catch (error) {
    // Handle errors
  }
 
  revalidatePath('/posts') // Update cached posts
  redirect(`/post/${id}`) // Navigate to the new post page
}
```

```python
'use server'
 
import { permanentRedirect } from 'next/navigation'
import { revalidateTag } from 'next/cache'
 
export async function updateUsername(username: string, formData: FormData) {
  try {
    // Call database
  } catch (error) {
    // Handle errors
  }
 
  revalidateTag('username') // Update all references to the username
  permanentRedirect(`/profile/${username}`) // Navigate to the new user profile
}
```

```python
'use client'
 
import { useRouter } from 'next/navigation'
 
export default function Page() {
  const router = useRouter()
 
  return (
    <button type="button" onClick={() => router.push('/dashboard')}>
      Dashboard
    </button>
  )
}
```

---

## Guides: SPAs | Next.js

**URL**: https://nextjs.org/docs/app/guides/single-page-applications

**Contents**:
- How to build single-page applications with Next.js
- What is a Single-Page Application?
- Why use Next.js for SPAs?
- Examples
  - Using React’s use within a Context Provider
  - SPAs with SWR
  - SPAs with React Query
  - Rendering components only in the browser

Features available in /app

Next.js fully supports building Single-Page Applications (SPAs).

This includes fast route transitions with prefetching, client-side data fetching, using browser APIs, integrating with third-party client libraries, creating static routes, and more.

If you have an existing SPA, you can migrate to Next.js without large changes to your code. Next.js then allows you to progressively add server features as needed.

The definition of a SPA varies. We’ll define a “strict SPA” as:

Strict SPAs often require large amounts of JavaScript to load before the page can be interactive. Further, client data waterfalls can be challenging to manage. Building SPAs with Next.js can address these issues.

Next.js can automatically code split your JavaScript bundles, and generate multiple HTML entry points into different routes. This avoids loading unnecessary JavaScript code on the client-side, reducing the bundle size and enabling faster page loads.

The next/link component automatically prefetches routes, giving you the fast page transitions of a strict SPA, but with the advantage of persisting application routing state to the URL for linking and sharing.

Next.js can start as a static site or even a strict SPA where everything is rendered client-side. If your project grows, Next.js allows you to progressively add more server features (e.g. React Server Components, Server Actions, and more) as needed.

Let's explore common patterns used to build SPAs and how Next.js solves them.

We recommend fetching data in a parent component (or layout), returning the Promise, and then unwrapping the value in a Client Component with React’s use hook.

Next.js can start data fetching early on the server. In this example, that’s the root layout — the entry point to your application. The server can immediately begin streaming a response to the client.

By “hoisting” your data fetching to the root layout, Next.js starts the specified requests on the server early before any o

*[Content truncated - see full docs]*

**Examples**:

```python
import { UserProvider } from './user-provider'
import { getUser } from './user' // some server-side function
 
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  let userPromise = getUser() // do NOT await
 
  return (
    <html lang="en">
      <body>
        <UserProvider userPromise={userPromise}>{children}</UserProvider>
      </body>
    </html>
  )
}
```

```python
'use client';
 
import { createContext, useContext, ReactNode } from 'react';
 
type User = any;
type UserContextType = {
  userPromise: Promise<User | null>;
};
 
const UserContext = createContext<UserContextType | null>(null);
 
export function useUser(): UserContextType {
  let context = useContext(UserContext);
  if (context === null) {
    throw new Error('useUser must be used within a UserProvider');
  }
  return context;
}
 
export function UserProvider({
  children,
  userPromise
}: {
  
...
```

```python
'use client'
 
import { use } from 'react'
import { useUser } from './user-provider'
 
export function Profile() {
  const { userPromise } = useUser()
  const user = use(userPromise)
 
  return '...'
}
```

---

## Guides: Sass | Next.js

**URL**: https://nextjs.org/docs/app/guides/sass

**Contents**:
- How to use Sass
  - Customizing Sass Options
    - Implementation
  - Sass Variables

Features available in /app

Next.js has built-in support for integrating with Sass after the package is installed using both the .scss and .sass extensions. You can use component-level Sass via CSS Modules and the .module.scssor .module.sass extension.

Sass supports two different syntaxes, each with their own extension. The .scss extension requires you use the SCSS syntax, while the .sass extension requires you use the Indented Syntax ("Sass").

If you're not sure which to choose, start with the .scss extension which is a superset of CSS, and doesn't require you learn the Indented Syntax ("Sass").

If you want to configure your Sass options, use sassOptions in next.config.

You can use the implementation property to specify the Sass implementation to use. By default, Next.js uses the sass package.

Next.js supports Sass variables exported from CSS Module files.

For example, using the exported primaryColor Sass variable:

**Examples**:

```text
npm install --save-dev sass
```

```python
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  sassOptions: {
    additionalData: `$var: red;`,
  },
}
 
export default nextConfig
```

```python
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  sassOptions: {
    implementation: 'sass-embedded',
  },
}
 
export default nextConfig
```

---

## Guides: Scripts | Next.js

**URL**: https://nextjs.org/docs/app/guides/scripts

**Contents**:
- How to load and optimize scripts
  - Layout Scripts
  - Application Scripts
  - Strategy
  - Offloading Scripts To A Web Worker (experimental)
  - Inline Scripts
  - Executing Additional Code
  - Additional Attributes

Features available in /app

To load a third-party script for multiple routes, import next/script and include the script directly in your layout component:

The third-party script is fetched when the folder route (e.g. dashboard/page.js) or any nested route (e.g. dashboard/settings/page.js) is accessed by the user. Next.js will ensure the script will only load once, even if a user navigates between multiple routes in the same layout.

To load a third-party script for all routes, import next/script and include the script directly in your root layout:

This script will load and execute when any route in your application is accessed. Next.js will ensure the script will only load once, even if a user navigates between multiple pages.

Recommendation: We recommend only including third-party scripts in specific pages or layouts in order to minimize any unnecessary impact to performance.

Although the default behavior of next/script allows you to load third-party scripts in any page or layout, you can fine-tune its loading behavior by using the strategy property:

Refer to the next/script API reference documentation to learn more about each strategy and their use cases.

Warning: The worker strategy is not yet stable and does not yet work with the App Router. Use with caution.

Scripts that use the worker strategy are offloaded and executed in a web worker with Partytown. This can improve the performance of your site by dedicating the main thread to the rest of your application code.

This strategy is still experimental and can only be used if the nextScriptWorkers flag is enabled in next.config.js:

Then, run next (normally npm run dev or yarn dev) and Next.js will guide you through the installation of the required packages to finish the setup:

You'll see instructions like these: Please install Partytown by running npm install @builder.io/partytown

Once setup is complete, defining strategy="worker" will automatically instantiate Partytown in your application and offload 

*[Content truncated - see full docs]*

**Examples**:

```python
import Script from 'next/script'
 
export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <>
      <section>{children}</section>
      <Script src="https://example.com/script.js" />
    </>
  )
}
```

```python
import Script from 'next/script'
 
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
      <Script src="https://example.com/script.js" />
    </html>
  )
}
```

```text
module.exports = {
  experimental: {
    nextScriptWorkers: true,
  },
}
```

---

## Guides: Self-Hosting | Next.js

**URL**: https://nextjs.org/docs/app/guides/self-hosting

**Contents**:
- How to self-host your Next.js application
- Image Optimization
- Middleware
- Environment Variables
- Caching and ISR
  - Automatic Caching
  - Static Assets
  - Configuring Caching

Features available in /app

When deploying your Next.js app, you may want to configure how different features are handled based on your infrastructure.

🎥 Watch: Learn more about self-hosting Next.js → YouTube (45 minutes).

Image Optimization through next/image works self-hosted with zero configuration when deploying using next start. If you would prefer to have a separate service to optimize images, you can configure an image loader.

Image Optimization can be used with a static export by defining a custom image loader in next.config.js. Note that images are optimized at runtime, not during the build.

Middleware works self-hosted with zero configuration when deploying using next start. Since it requires access to the incoming request, it is not supported when using a static export.

Middleware uses the Edge runtime, a subset of all available Node.js APIs to help ensure low latency, since it may run in front of every route or asset in your application. If you do not want this, you can use the full Node.js runtime to run Middleware.

If you are looking to add logic (or use an external package) that requires all Node.js APIs, you might be able to move this logic to a layout as a Server Component. For example, checking headers and redirecting. You can also use headers, cookies, or query parameters to redirect or rewrite through next.config.js. If that does not work, you can also use a custom server.

Next.js can support both build time and runtime environment variables.

By default, environment variables are only available on the server. To expose an environment variable to the browser, it must be prefixed with NEXT_PUBLIC_. However, these public environment variables will be inlined into the JavaScript bundle during next build.

You safely read environment variables on the server during dynamic rendering.

This allows you to use a singular Docker image that can be promoted through multiple environments with different values.

Next.js can cache responses, generated s

*[Content truncated - see full docs]*

**Examples**:

```python
import { connection } from 'next/server'
 
export default async function Component() {
  await connection()
  // cookies, headers, and other Dynamic APIs
  // will also opt into dynamic rendering, meaning
  // this env variable is evaluated at runtime
  const value = process.env.MY_VALUE
  // ...
}
```

```text
module.exports = {
  cacheHandler: require.resolve('./cache-handler.js'),
  cacheMaxMemorySize: 0, // disable default in-memory caching
}
```

```javascript
const cache = new Map()
 
module.exports = class CacheHandler {
  constructor(options) {
    this.options = options
  }
 
  async get(key) {
    // This could be stored anywhere, like durable storage
    return cache.get(key)
  }
 
  async set(key, data, ctx) {
    // This could be stored anywhere, like durable storage
    cache.set(key, {
      value: data,
      lastModified: Date.now(),
      tags: ctx.tags,
    })
  }
 
  async revalidateTag(tags) {
    // tags is either a string or an array
...
```

---

## Guides: Static Exports | Next.js

**URL**: https://nextjs.org/docs/app/guides/static-exports

**Contents**:
- How to create a static export of your Next.js application
- Configuration
- Supported Features
  - Server Components
  - Client Components
  - Image Optimization
  - Route Handlers
  - Browser APIs

Features available in /app

Next.js enables starting as a static site or Single-Page Application (SPA), then later optionally upgrading to use features that require a server.

When running next build, Next.js generates an HTML file per route. By breaking a strict SPA into individual HTML files, Next.js can avoid loading unnecessary JavaScript code on the client-side, reducing the bundle size and enabling faster page loads.

Since Next.js supports this static export, it can be deployed and hosted on any web server that can serve HTML/CSS/JS static assets.

To enable a static export, change the output mode inside next.config.js:

After running next build, Next.js will create an out folder with the HTML/CSS/JS assets for your application.

The core of Next.js has been designed to support static exports.

When you run next build to generate a static export, Server Components consumed inside the app directory will run during the build, similar to traditional static-site generation.

The resulting component will be rendered into static HTML for the initial page load and a static payload for client navigation between routes. No changes are required for your Server Components when using the static export, unless they consume dynamic server functions.

If you want to perform data fetching on the client, you can use a Client Component with SWR to memoize requests.

Since route transitions happen client-side, this behaves like a traditional SPA. For example, the following index route allows you to navigate to different posts on the client:

Image Optimization through next/image can be used with a static export by defining a custom image loader in next.config.js. For example, you can optimize images with a service like Cloudinary:

This custom loader will define how to fetch images from a remote source. For example, the following loader will construct the URL for Cloudinary:

You can then use next/image in your application, defining relative paths to the image in Cloudinary:

R

*[Content truncated - see full docs]*

**Examples**:

```javascript
/**
 * @type {import('next').NextConfig}
 */
const nextConfig = {
  output: 'export',
 
  // Optional: Change links `/me` -> `/me/` and emit `/me.html` -> `/me/index.html`
  // trailingSlash: true,
 
  // Optional: Prevent automatic `/me` -> `/me/`, instead preserve `href`
  // skipTrailingSlashRedirect: true,
 
  // Optional: Change the output directory `out` -> `dist`
  // distDir: 'dist',
}
 
module.exports = nextConfig
```

```javascript
export default async function Page() {
  // This fetch will run on the server during `next build`
  const res = await fetch('https://api.example.com/...')
  const data = await res.json()
 
  return <main>...</main>
}
```

```python
'use client'
 
import useSWR from 'swr'
 
const fetcher = (url: string) => fetch(url).then((r) => r.json())
 
export default function Page() {
  const { data, error } = useSWR(
    `https://jsonplaceholder.typicode.com/posts/1`,
    fetcher
  )
  if (error) return 'Failed to load'
  if (!data) return 'Loading...'
 
  return data.title
}
```

---

## Guides: Tailwind CSS v3 | Next.js

**URL**: https://nextjs.org/docs/app/guides/tailwind-v3-css

**Contents**:
- How to install Tailwind CSS v3 in your Next.js application
- Installing Tailwind v3
- Configuring Tailwind v3
- Using classes
- Usage with Turbopack

Features available in /app

This guide will walk you through how to install Tailwind CSS v3 in your Next.js application.

Good to know: For the latest Tailwind 4 setup, see the Tailwind CSS setup instructions.

Install Tailwind CSS and its peer dependencies, then run the init command to generate both tailwind.config.js and postcss.config.js files:

Configure your template paths in your tailwind.config.js file:

Add the Tailwind directives to your global CSS file:

Import the CSS file in your root layout:

After installing Tailwind CSS and adding the global styles, you can use Tailwind's utility classes in your application.

As of Next.js 13.1, Tailwind CSS and PostCSS are supported with Turbopack.

**Examples**:

```text
pnpm add -D tailwindcss@^3 postcss autoprefixer
npx tailwindcss init -p
```

```typescript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './app/**/*.{js,ts,jsx,tsx,mdx}',
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

```text
@tailwind base;
@tailwind components;
@tailwind utilities;
```

---

## Guides: Testing | Next.js

**URL**: https://nextjs.org/docs/app/guides/testing

**Contents**:
- Testing
- Types of tests
- Async Server Components
- Guides
  - Cypress
  - Jest
  - Playwright
  - Vitest

Features available in /app

In React and Next.js, there are a few different types of tests you can write, each with its own purpose and use cases. This page provides an overview of types and commonly used tools you can use to test your application.

Since async Server Components are new to the React ecosystem, some tools do not fully support them. In the meantime, we recommend using End-to-End Testing over Unit Testing for async components.

See the guides below to learn how to set up Next.js with these commonly used testing tools:

---

## Guides: Third Party Libraries | Next.js

**URL**: https://nextjs.org/docs/app/guides/third-party-libraries

**Contents**:
- How to optimize third-party libraries
- Getting Started
- Google Third-Parties
  - Google Tag Manager
    - Sending Events
    - Server-side Tagging
    - Options
  - Google Analytics

Features available in /app

@next/third-parties is a library that provides a collection of components and utilities that improve the performance and developer experience of loading popular third-party libraries in your Next.js application.

All third-party integrations provided by @next/third-parties have been optimized for performance and ease of use.

To get started, install the @next/third-parties library:

@next/third-parties is currently an experimental library under active development. We recommend installing it with the latest or canary flags while we work on adding more third-party integrations.

All supported third-party libraries from Google can be imported from @next/third-parties/google.

The GoogleTagManager component can be used to instantiate a Google Tag Manager container to your page. By default, it fetches the original inline script after hydration occurs on the page.

To load Google Tag Manager for all routes, include the component directly in your root layout and pass in your GTM container ID:

To load Google Tag Manager for a single route, include the component in your page file:

The sendGTMEvent function can be used to track user interactions on your page by sending events using the dataLayer object. For this function to work, the <GoogleTagManager /> component must be included in either a parent layout, page, or component, or directly in the same file.

Refer to the Tag Manager developer documentation to learn about the different variables and events that can be passed into the function.

If you're using a server-side tag manager and serving gtm.js scripts from your tagging server you can use gtmScriptUrl option to specify the URL of the script.

Options to pass to the Google Tag Manager. For a full list of options, read the Google Tag Manager docs.

The GoogleAnalytics component can be used to include Google Analytics 4 to your page via the Google tag (gtag.js). By default, it fetches the original scripts after hydration occurs on the page.


*[Content truncated - see full docs]*

**Examples**:

```text
npm install @next/third-parties@latest next@latest
```

```python
import { GoogleTagManager } from '@next/third-parties/google'
 
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <GoogleTagManager gtmId="GTM-XYZ" />
      <body>{children}</body>
    </html>
  )
}
```

```python
import { GoogleTagManager } from '@next/third-parties/google'
 
export default function Page() {
  return <GoogleTagManager gtmId="GTM-XYZ" />
}
```

---

## Guides: Upgrading | Next.js

**URL**: https://nextjs.org/docs/app/guides/upgrading

**Contents**:
- Upgrade Guides
  - Codemods
  - Version 14
  - Version 15

Features available in /app

Learn how to upgrade to the latest versions of Next.js following the versions-specific guides:

---

## Guides: Videos | Next.js

**URL**: https://nextjs.org/docs/app/guides/videos

**Contents**:
- How to use and optimize videos
- Using <video> and <iframe>
  - <video>
  - Common <video> tag attributes
  - Video best practices
  - <iframe>
  - Common <iframe> tag attributes
  - Choosing a video embedding method

Features available in /app

This page outlines how to use videos with Next.js applications, showing how to store and display video files without affecting performance.

Videos can be embedded on the page using the HTML <video> tag for direct video files and <iframe> for external platform-hosted videos.

The HTML <video> tag can embed self-hosted or directly served video content, allowing full control over the playback and appearance.

Good to know: When using the autoPlay attribute, it is important to also include the muted attribute to ensure the video plays automatically in most browsers and the playsInline attribute for compatibility with iOS devices.

For a comprehensive list of video attributes, refer to the MDN documentation.

The HTML <iframe> tag allows you to embed videos from external platforms like YouTube or Vimeo.

For a comprehensive list of iframe attributes, refer to the MDN documentation.

There are two ways you can embed videos in your Next.js application:

Choose the embedding method that aligns with your application's requirements and the user experience you aim to deliver.

To embed videos from external platforms, you can use Next.js to fetch the video information and React Suspense to handle the fallback state while loading.

1. Create a Server Component for video embedding

The first step is to create a Server Component that generates the appropriate iframe for embedding the video. This component will fetch the source URL for the video and render the iframe.

2. Stream the video component using React Suspense

After creating the Server Component to embed the video, the next step is to stream the component using React Suspense.

Good to know: When embedding videos from external platforms, consider the following best practices:

This approach results in a better user experience as it prevents the page from blocking, meaning the user can interact with the page while the video component streams in.

For a more engaging and informative loading expe

*[Content truncated - see full docs]*

**Examples**:

```javascript
export function Video() {
  return (
    <video width="320" height="240" controls preload="none">
      <source src="/path/to/video.mp4" type="video/mp4" />
      <track
        src="/path/to/captions.vtt"
        kind="subtitles"
        srcLang="en"
        label="English"
      />
      Your browser does not support the video tag.
    </video>
  )
}
```

```javascript
export default function Page() {
  return (
    <iframe src="https://www.youtube.com/embed/19g66ezsKAg" allowFullScreen />
  )
}
```

```javascript
export default async function VideoComponent() {
  const src = await getVideoSrc()
 
  return <iframe src={src} allowFullScreen />
}
```

---

## Metadata Files: favicon, icon, and apple-icon | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons

**Contents**:
- favicon, icon, and apple-icon
- Image files (.ico, .jpg, .png)
  - favicon
  - icon
  - apple-icon
- Generate icons using code (.js, .ts, .tsx)
  - Props
    - params (optional)

Features available in /app

The favicon, icon, or apple-icon file conventions allow you to set icons for your application.

They are useful for adding app icons that appear in places like web browser tabs, phone home screens, and search engine results.

There are two ways to set app icons:

Use an image file to set an app icon by placing a favicon, icon, or apple-icon image file within your /app directory. The favicon image can only be located in the top level of app/.

Next.js will evaluate the file and automatically add the appropriate tags to your app's <head> element.

Add a favicon.ico image file to the root /app route segment.

Add an icon.(ico|jpg|jpeg|png|svg) image file.

Add an apple-icon.(jpg|jpeg|png) image file.

In addition to using literal image files, you can programmatically generate icons using code.

Generate an app icon by creating an icon or apple-icon route that default exports a function.

The easiest way to generate an icon is to use the ImageResponse API from next/og.

The default export function receives the following props:

An object containing the dynamic route parameters object from the root segment down to the segment icon or apple-icon is colocated in.

The default export function should return a Blob | ArrayBuffer | TypedArray | DataView | ReadableStream | Response.

Good to know: ImageResponse satisfies this return type.

You can optionally configure the icon's metadata by exporting size and contentType variables from the icon or apple-icon route.

icon and apple-icon are specialized Route Handlers that can use the same route segment configuration options as Pages and Layouts.

**Examples**:

```text
<link rel="icon" href="/favicon.ico" sizes="any" />
```

```text
<link
  rel="icon"
  href="/icon?<generated>"
  type="image/<generated>"
  sizes="<generated>"
/>
```

```text
<link
  rel="apple-touch-icon"
  href="/apple-icon?<generated>"
  type="image/<generated>"
  sizes="<generated>"
/>
```

---

## Metadata Files: manifest.json | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest

**Contents**:
- manifest.json
- Static Manifest file
- Generate a Manifest file
  - Manifest Object

Features available in /app

Add or generate a manifest.(json|webmanifest) file that matches the Web Manifest Specification in the root of app directory to provide information about your web application for the browser.

Add a manifest.js or manifest.ts file that returns a Manifest object.

Good to know: manifest.js is special Route Handlers that is cached by default unless it uses a Dynamic API or dynamic config option.

The manifest object contains an extensive list of options that may be updated due to new web standards. For information on all the current options, refer to the MetadataRoute.Manifest type in your code editor if using TypeScript or see the MDN docs.

**Examples**:

```text
{
  "name": "My Next.js Application",
  "short_name": "Next.js App",
  "description": "An application built with Next.js",
  "start_url": "/"
  // ...
}
```

```python
import type { MetadataRoute } from 'next'
 
export default function manifest(): MetadataRoute.Manifest {
  return {
    name: 'Next.js App',
    short_name: 'Next.js App',
    description: 'Next.js App',
    start_url: '/',
    display: 'standalone',
    background_color: '#fff',
    theme_color: '#fff',
    icons: [
      {
        src: '/favicon.ico',
        sizes: 'any',
        type: 'image/x-icon',
      },
    ],
  }
}
```

---

## Metadata Files: opengraph-image and twitter-image | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image

**Contents**:
- opengraph-image and twitter-image
- Image files (.jpg, .png, .gif)
  - opengraph-image
  - twitter-image
  - opengraph-image.alt.txt
  - twitter-image.alt.txt
- Generate images using code (.js, .ts, .tsx)
  - Props

Features available in /app

The opengraph-image and twitter-image file conventions allow you to set Open Graph and Twitter images for a route segment.

They are useful for setting the images that appear on social networks and messaging apps when a user shares a link to your site.

There are two ways to set Open Graph and Twitter images:

Use an image file to set a route segment's shared image by placing an opengraph-image or twitter-image image file in the segment.

Next.js will evaluate the file and automatically add the appropriate tags to your app's <head> element.

The twitter-image file size must not exceed 5MB, and the opengraph-image file size must not exceed 8MB. If the image file size exceeds these limits, the build will fail.

Add an opengraph-image.(jpg|jpeg|png|gif) image file to any route segment.

Add a twitter-image.(jpg|jpeg|png|gif) image file to any route segment.

Add an accompanying opengraph-image.alt.txt file in the same route segment as the opengraph-image.(jpg|jpeg|png|gif) image it's alt text.

Add an accompanying twitter-image.alt.txt file in the same route segment as the twitter-image.(jpg|jpeg|png|gif) image it's alt text.

In addition to using literal image files, you can programmatically generate images using code.

Generate a route segment's shared image by creating an opengraph-image or twitter-image route that default exports a function.

The easiest way to generate an image is to use the ImageResponse API from next/og.

The default export function receives the following props:

An object containing the dynamic route parameters object from the root segment down to the segment opengraph-image or twitter-image is colocated in.

The default export function should return a Blob | ArrayBuffer | TypedArray | DataView | ReadableStream | Response.

Good to know: ImageResponse satisfies this return type.

You can optionally configure the image's metadata by exporting alt, size, and contentType variables from opengraph-image or twitter-image r

*[Content truncated - see full docs]*

**Examples**:

```text
<meta property="og:image" content="<generated>" />
<meta property="og:image:type" content="<generated>" />
<meta property="og:image:width" content="<generated>" />
<meta property="og:image:height" content="<generated>" />
```

```text
<meta name="twitter:image" content="<generated>" />
<meta name="twitter:image:type" content="<generated>" />
<meta name="twitter:image:width" content="<generated>" />
<meta name="twitter:image:height" content="<generated>" />
```

```text
<meta property="og:image:alt" content="About Acme" />
```

---

## Metadata Files: robots.txt | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots

**Contents**:
- robots.txt
- Static robots.txt
- Generate a Robots file
  - Customizing specific user agents
  - Robots object
- Version History

Features available in /app

Add or generate a robots.txt file that matches the Robots Exclusion Standard in the root of app directory to tell search engine crawlers which URLs they can access on your site.

Add a robots.js or robots.ts file that returns a Robots object.

Good to know: robots.js is a special Route Handlers that is cached by default unless it uses a Dynamic API or dynamic config option.

You can customise how individual search engine bots crawl your site by passing an array of user agents to the rules property. For example:

**Examples**:

```text
User-Agent: *
Allow: /
Disallow: /private/

Sitemap: https://acme.com/sitemap.xml
```

```python
import type { MetadataRoute } from 'next'
 
export default function robots(): MetadataRoute.Robots {
  return {
    rules: {
      userAgent: '*',
      allow: '/',
      disallow: '/private/',
    },
    sitemap: 'https://acme.com/sitemap.xml',
  }
}
```

```text
User-Agent: *
Allow: /
Disallow: /private/

Sitemap: https://acme.com/sitemap.xml
```

---

## Metadata Files: sitemap.xml | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap

**Contents**:
- sitemap.xml
  - Sitemap files (.xml)
  - Generating a sitemap using code (.js, .ts)
  - Image Sitemaps
  - Video Sitemaps
  - Generate a localized Sitemap
  - Generating multiple sitemaps
- Returns

Features available in /app

sitemap.(xml|js|ts) is a special file that matches the Sitemaps XML format to help search engine crawlers index your site more efficiently.

For smaller applications, you can create a sitemap.xml file and place it in the root of your app directory.

You can use the sitemap.(js|ts) file convention to programmatically generate a sitemap by exporting a default function that returns an array of URLs. If using TypeScript, a Sitemap type is available.

Good to know: sitemap.js is a special Route Handler that is cached by default unless it uses a Dynamic API or dynamic config option.

You can use images property to create image sitemaps. Learn more details in the Google Developer Docs.

You can use videos property to create video sitemaps. Learn more details in the Google Developer Docs.

While a single sitemap will work for most applications. For large web applications, you may need to split a sitemap into multiple files.

There are two ways you can create multiple sitemaps:

For example, to split a sitemap using generateSitemaps, return an array of objects with the sitemap id. Then, use the id to generate the unique sitemaps.

Your generated sitemaps will be available at /.../sitemap/[id]. For example, /product/sitemap/1.xml.

See the generateSitemaps API reference for more information.

The default function exported from sitemap.(xml|ts|js) should return an array of objects with the following properties:

**Examples**:

```text
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://acme.com</loc>
    <lastmod>2023-04-06T15:02:24.021Z</lastmod>
    <changefreq>yearly</changefreq>
    <priority>1</priority>
  </url>
  <url>
    <loc>https://acme.com/about</loc>
    <lastmod>2023-04-06T15:02:24.021Z</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://acme.com/blog</loc>
    <lastmod>2023-04-06T15:02:24.021Z</lastmod>
    <changefreq>w
...
```

```python
import type { MetadataRoute } from 'next'
 
export default function sitemap(): MetadataRoute.Sitemap {
  return [
    {
      url: 'https://acme.com',
      lastModified: new Date(),
      changeFrequency: 'yearly',
      priority: 1,
    },
    {
      url: 'https://acme.com/about',
      lastModified: new Date(),
      changeFrequency: 'monthly',
      priority: 0.8,
    },
    {
      url: 'https://acme.com/blog',
      lastModified: new Date(),
      changeFrequency: 'weekly',
      priority
...
```

```text
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://acme.com</loc>
    <lastmod>2023-04-06T15:02:24.021Z</lastmod>
    <changefreq>yearly</changefreq>
    <priority>1</priority>
  </url>
  <url>
    <loc>https://acme.com/about</loc>
    <lastmod>2023-04-06T15:02:24.021Z</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://acme.com/blog</loc>
    <lastmod>2023-04-06T15:02:24.021Z</lastmod>
    <changefreq>w
...
```

---

## Migrating: App Router | Next.js

**URL**: https://nextjs.org/docs/app/guides/migrating/app-router-migration

**Contents**:
- How to migrate from Pages to the App Router
- Upgrading
  - Node.js Version
  - Next.js Version
  - ESLint Version
- Next Steps
- Upgrading New Features
  - <Image/> Component

Features available in /app

This guide will help you:

The minimum Node.js version is now v18.17. See the Node.js documentation for more information.

To update to Next.js version 13, run the following command using your preferred package manager:

If you're using ESLint, you need to upgrade your ESLint version:

Good to know: You may need to restart the ESLint server in VS Code for the ESLint changes to take effect. Open the Command Palette (cmd+shift+p on Mac; ctrl+shift+p on Windows) and search for ESLint: Restart ESLint Server.

After you've updated, see the following sections for next steps:

Next.js 13 introduced the new App Router with new features and conventions. The new Router is available in the app directory and co-exists with the pages directory.

Upgrading to Next.js 13 does not require using the App Router. You can continue using pages with new features that work in both directories, such as the updated Image component, Link component, Script component, and Font optimization.

Next.js 12 introduced new improvements to the Image Component with a temporary import: next/future/image. These improvements included less client-side JavaScript, easier ways to extend and style images, better accessibility, and native browser lazy loading.

In version 13, this new behavior is now the default for next/image.

There are two codemods to help you migrate to the new Image Component:

The <Link> Component no longer requires manually adding an <a> tag as a child. This behavior was added as an experimental option in version 12.2 and is now the default. In Next.js 13, <Link> always renders <a> and allows you to forward props to the underlying tag.

To upgrade your links to Next.js 13, you can use the new-link codemod.

The behavior of next/script has been updated to support both pages and app, but some changes need to be made to ensure a smooth migration:

Previously, Next.js helped you optimize fonts by inlining font CSS. Version 13 introduces the new next/font module 

*[Content truncated - see full docs]*

**Examples**:

```text
npm install next@latest react@latest react-dom@latest
```

```text
npm install -D eslint-config-next@latest
```

```python
import Link from 'next/link'
 
// Next.js 12: `<a>` has to be nested otherwise it's excluded
<Link href="/about">
  <a>About</a>
</Link>
 
// Next.js 13: `<Link>` always renders `<a>` under the hood
<Link href="/about">
  About
</Link>
```

---

## Migrating: Create React App | Next.js

**URL**: https://nextjs.org/docs/app/guides/migrating/from-create-react-app

**Contents**:
- How to migrate from Create React App to Next.js
- Why Switch?
  - Slow initial page loading time
  - No automatic code splitting
  - Network waterfalls
  - Fast and intentional loading states
  - Choose the data fetching strategy
  - Middleware

Features available in /app

This guide will help you migrate an existing Create React App (CRA) site to Next.js.

There are several reasons why you might want to switch from Create React App to Next.js:

Create React App uses purely client-side rendering. Client-side only applications, also known as single-page applications (SPAs), often experience slow initial page loading time. This happens due to a couple of reasons:

The previous issue of slow loading times can be somewhat mitigated with code splitting. However, if you try to do code splitting manually, you can inadvertently introduce network waterfalls. Next.js provides automatic code splitting and tree-shaking built into its router and build pipeline.

A common cause of poor performance occurs when applications make sequential client-server requests to fetch data. One pattern for data fetching in a SPA is to render a placeholder, and then fetch data after the component has mounted. Unfortunately, a child component can only begin fetching data after its parent has finished loading its own data, resulting in a “waterfall” of requests.

While client-side data fetching is supported in Next.js, Next.js also lets you move data fetching to the server. This often eliminates client-server waterfalls altogether.

With built-in support for streaming through React Suspense, you can define which parts of your UI load first and in what order, without creating network waterfalls.

This enables you to build pages that are faster to load and eliminate layout shifts.

Depending on your needs, Next.js allows you to choose your data fetching strategy on a page or component-level basis. For example, you could fetch data from your CMS and render blog posts at build time (SSG) for quick load speeds, or fetch data at request time (SSR) when necessary.

Next.js Middleware allows you to run code on the server before a request is completed. For instance, you can avoid a flash of unauthenticated content by redirecting a user to a login p

*[Content truncated - see full docs]*

**Examples**:

```text
npm install next@latest
```

```python
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  output: 'export', // Outputs a Single-Page Application (SPA)
  distDir: 'build', // Changes the build output directory to `build`
}
 
export default nextConfig
```

```javascript
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return '...'
}
```

---

## Migrating: Vite | Next.js

**URL**: https://nextjs.org/docs/app/guides/migrating/from-vite

**Contents**:
- How to migrate from Vite to Next.js
- Why Switch?
  - Slow initial page loading time
  - No automatic code splitting
  - Network waterfalls
  - Fast and intentional loading states
  - Choose the data fetching strategy
  - Middleware

Features available in /app

This guide will help you migrate an existing Vite application to Next.js.

There are several reasons why you might want to switch from Vite to Next.js:

If you have built your application with the default Vite plugin for React, your application is a purely client-side application. Client-side only applications, also known as single-page applications (SPAs), often experience slow initial page loading time. This happens due to a couple of reasons:

The previous issue of slow loading times can be somewhat managed with code splitting. However, if you try to do code splitting manually, you'll often make performance worse. It's easy to inadvertently introduce network waterfalls when code-splitting manually. Next.js provides automatic code splitting built into its router.

A common cause of poor performance occurs when applications make sequential client-server requests to fetch data. One common pattern for data fetching in an SPA is to initially render a placeholder, and then fetch data after the component has mounted. Unfortunately, this means that a child component that fetches data can't start fetching until the parent component has finished loading its own data.

While fetching data on the client is supported with Next.js, it also gives you the option to shift data fetching to the server, which can eliminate client-server waterfalls.

With built-in support for streaming through React Suspense, you can be more intentional about which parts of your UI you want to load first and in what order without introducing network waterfalls.

This enables you to build pages that are faster to load and eliminate layout shifts.

Depending on your needs, Next.js allows you to choose your data fetching strategy on a page and component basis. You can decide to fetch at build time, at request time on the server, or on the client. For example, you can fetch data from your CMS and render your blog posts at build time, which can then be efficiently cached on a C

*[Content truncated - see full docs]*

**Examples**:

```text
npm install next@latest
```

```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export', // Outputs a Single-Page Application (SPA).
  distDir: './dist', // Changes the build output directory to `./dist/`.
}
 
export default nextConfig
```

```text
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "esModuleInterop": true,
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "preserve",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch
...
```

---

## Testing: Cypress | Next.js

**URL**: https://nextjs.org/docs/app/guides/testing/cypress

**Contents**:
- How to set up Cypress with Next.js
- Quickstart
- Manual setup
- Creating your first Cypress E2E test
  - Running E2E Tests
- Creating your first Cypress component test
  - Running Component Tests
- Continuous Integration (CI)

Features available in /app

Cypress is a test runner used for End-to-End (E2E) and Component Testing. This page will show you how to set up Cypress with Next.js and write your first tests.

You can use create-next-app with the with-cypress example to quickly get started.

To manually set up Cypress, install cypress as a dev dependency:

Add the Cypress open command to the package.json scripts field:

Run Cypress for the first time to open the Cypress testing suite:

You can choose to configure E2E Testing and/or Component Testing. Selecting any of these options will automatically create a cypress.config.js file and a cypress folder in your project.

Ensure your cypress.config file has the following configuration:

Then, create two new Next.js files:

Add a test to check your navigation is working correctly:

Cypress will simulate a user navigating your application, this requires your Next.js server to be running. We recommend running your tests against your production code to more closely resemble how your application will behave.

Run npm run build && npm run start to build your Next.js application, then run npm run cypress:open in another terminal window to start Cypress and run your E2E Testing suite.

Component tests build and mount a specific component without having to bundle your whole application or start a server.

Select Component Testing in the Cypress app, then select Next.js as your front-end framework. A cypress/component folder will be created in your project, and a cypress.config.js file will be updated to enable Component Testing.

Ensure your cypress.config file has the following configuration:

Assuming the same components from the previous section, add a test to validate a component is rendering the expected output:

Run npm run cypress:open in your terminal to start Cypress and run your Component Testing suite.

In addition to interactive testing, you can also run Cypress headlessly using the cypress run command, which is better suited for CI en

*[Content truncated - see full docs]*

**Examples**:

```text
npx create-next-app@latest --example with-cypress with-cypress-app
```

```text
npm install -D cypress
# or
yarn add -D cypress
# or
pnpm install -D cypress
```

```text
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "eslint",
    "cypress:open": "cypress open"
  }
}
```

---

## Testing: Jest | Next.js

**URL**: https://nextjs.org/docs/app/guides/testing/jest

**Contents**:
- How to set up Jest with Next.js
- Quickstart
- Manual setup
- Optional: Handling Absolute Imports and Module Path Aliases
- Optional: Extend Jest with custom matchers
- Add a test script to package.json
  - Creating your first test
- Running your tests

Features available in /app

Jest and React Testing Library are frequently used together for Unit Testing and Snapshot Testing. This guide will show you how to set up Jest with Next.js and write your first tests.

Good to know: Since async Server Components are new to the React ecosystem, Jest currently does not support them. While you can still run unit tests for synchronous Server and Client Components, we recommend using an E2E tests for async components.

You can use create-next-app with the Next.js with-jest example to quickly get started:

Since the release of Next.js 12, Next.js now has built-in configuration for Jest.

To set up Jest, install jest and the following packages as dev dependencies:

Generate a basic Jest configuration file by running the following command:

This will take you through a series of prompts to setup Jest for your project, including automatically creating a jest.config.ts|js file.

Update your config file to use next/jest. This transformer has all the necessary configuration options for Jest to work with Next.js:

Under the hood, next/jest is automatically configuring Jest for you, including:

Good to know: To test environment variables directly, load them manually in a separate setup script or in your jest.config.ts file. For more information, please see Test Environment Variables.

If your project is using Module Path Aliases, you will need to configure Jest to resolve the imports by matching the paths option in the jsconfig.json file with the moduleNameMapper option in the jest.config.js file. For example:

@testing-library/jest-dom includes a set of convenient custom matchers such as .toBeInTheDocument() making it easier to write tests. You can import the custom matchers for every test by adding the following option to the Jest configuration file:

Then, inside jest.setup, add the following import:

Good to know: extend-expect was removed in v6.0, so if you are using @testing-library/jest-dom before version 6, you will need to imp

*[Content truncated - see full docs]*

**Examples**:

```text
npx create-next-app@latest --example with-jest with-jest-app
```

```text
npm install -D jest jest-environment-jsdom @testing-library/react @testing-library/dom @testing-library/jest-dom ts-node @types/jest
# or
yarn add -D jest jest-environment-jsdom @testing-library/react @testing-library/dom @testing-library/jest-dom ts-node @types/jest
# or
pnpm install -D jest jest-environment-jsdom @testing-library/react @testing-library/dom @testing-library/jest-dom ts-node @types/jest
```

```text
npm init jest@latest
# or
yarn create jest@latest
# or
pnpm create jest@latest
```

---

## Testing: Playwright | Next.js

**URL**: https://nextjs.org/docs/app/guides/testing/playwright

**Contents**:
- How to set up Playwright with Next.js
- Quickstart
- Manual setup
- Creating your first Playwright E2E test
  - Running your Playwright tests
  - Running Playwright on Continuous Integration (CI)

Features available in /app

Playwright is a testing framework that lets you automate Chromium, Firefox, and WebKit with a single API. You can use it to write End-to-End (E2E) testing. This guide will show you how to set up Playwright with Next.js and write your first tests.

The fastest way to get started is to use create-next-app with the with-playwright example. This will create a Next.js project complete with Playwright configured.

To install Playwright, run the following command:

This will take you through a series of prompts to setup and configure Playwright for your project, including adding a playwright.config.ts file. Please refer to the Playwright installation guide for the step-by-step guide.

Create two new Next.js pages:

Then, add a test to verify that your navigation is working correctly:

Good to know: You can use page.goto("/") instead of page.goto("http://localhost:3000/"), if you add "baseURL": "http://localhost:3000" to the playwright.config.ts configuration file.

Playwright will simulate a user navigating your application using three browsers: Chromium, Firefox and Webkit, this requires your Next.js server to be running. We recommend running your tests against your production code to more closely resemble how your application will behave.

Run npm run build and npm run start, then run npx playwright test in another terminal window to run the Playwright tests.

Good to know: Alternatively, you can use the webServer feature to let Playwright start the development server and wait until it's fully available.

Playwright will by default run your tests in the headless mode. To install all the Playwright dependencies, run npx playwright install-deps.

You can learn more about Playwright and Continuous Integration from these resources:

**Examples**:

```text
npx create-next-app@latest --example with-playwright with-playwright-app
```

```text
npm init playwright
# or
yarn create playwright
# or
pnpm create playwright
```

```python
import Link from 'next/link'
 
export default function Page() {
  return (
    <div>
      <h1>Home</h1>
      <Link href="/about">About</Link>
    </div>
  )
}
```

---

## Testing: Vitest | Next.js

**URL**: https://nextjs.org/docs/app/guides/testing/vitest

**Contents**:
- How to set up Vitest with Next.js
- Quickstart
- Manual Setup
- Creating your first Vitest Unit Test
- Running your tests
- Additional Resources

Features available in /app

Vitest and React Testing Library are frequently used together for Unit Testing. This guide will show you how to setup Vitest with Next.js and write your first tests.

Good to know: Since async Server Components are new to the React ecosystem, Vitest currently does not support them. While you can still run unit tests for synchronous Server and Client Components, we recommend using E2E tests for async components.

You can use create-next-app with the Next.js with-vitest example to quickly get started:

To manually set up Vitest, install vitest and the following packages as dev dependencies:

Create a vitest.config.mts|js file in the root of your project, and add the following options:

For more information on configuring Vitest, please refer to the Vitest Configuration docs.

Then, add a test script to your package.json:

When you run npm run test, Vitest will watch for changes in your project by default.

Check that everything is working by creating a test to check if the <Page /> component successfully renders a heading:

Good to know: The example above uses the common __tests__ convention, but test files can also be colocated inside the app router.

Then, run the following command to run your tests:

You may find these resources helpful:

**Examples**:

```text
npx create-next-app@latest --example with-vitest with-vitest-app
```

```text
# Using TypeScript
npm install -D vitest @vitejs/plugin-react jsdom @testing-library/react @testing-library/dom vite-tsconfig-paths
# Using JavaScript
npm install -D vitest @vitejs/plugin-react jsdom @testing-library/react @testing-library/dom
```

```python
import { defineConfig } from 'vitest/config'
import react from '@vitejs/plugin-react'
import tsconfigPaths from 'vite-tsconfig-paths'
 
export default defineConfig({
  plugins: [tsconfigPaths(), react()],
  test: {
    environment: 'jsdom',
  },
})
```

---

## Upgrading: Codemods | Next.js

**URL**: https://nextjs.org/docs/app/guides/upgrading/codemods

**Contents**:
- Codemods
- Usage
- Codemods
  - 16.0
    - Migrate from next lint to ESLint CLI
      - next-lint-to-eslint-cli
  - 15.0
    - Transform App Router Route Segment Config runtime value from experimental-edge to edge

Features available in /app

Codemods are transformations that run on your codebase programmatically. This allows a large number of changes to be programmatically applied without having to manually go through every file.

Next.js provides Codemod transformations to help upgrade your Next.js codebase when an API is updated or deprecated.

In your terminal, navigate (cd) into your project's folder, then run:

Replacing <transform> and <path> with appropriate values.

This codemod migrates projects from using next lint to using the ESLint CLI with your local ESLint config. It:

Note: This codemod is App Router specific.

This codemod transforms Route Segment Config runtime value experimental-edge to edge.

APIs that opted into dynamic rendering that previously supported synchronous access are now asynchronous. You can read more about this breaking change in the upgrade guide.

This codemod will transform dynamic APIs (cookies(), headers() and draftMode() from next/headers) that are now asynchronous to be properly awaited or wrapped with React.use() if applicable. When an automatic migration isn't possible, the codemod will either add a typecast (if a TypeScript file) or a comment to inform the user that it needs to be manually reviewed & updated.

When we detect property access on the params or searchParams props in the page / route entries (page.js, layout.js, route.js, or default.js) or the generateMetadata / generateViewport APIs, it will attempt to transform the callsite from a sync to an async function, and await the property access. If it can't be made async (such as with a Client Component), it will use React.use to unwrap the promise .

Good to know: When this codemod identifies a spot that might require manual intervention, but we aren't able to determine the exact fix, it will add a comment or typecast to the code to inform the user that it needs to be manually updated. These comments are prefixed with @next/codemod, and typecasts are prefixed with UnsafeUnwra

*[Content truncated - see full docs]*

**Examples**:

```text
npx @next/codemod <transform> <path>
```

```text
npx @next/codemod@canary next-lint-to-eslint-cli .
```

```text
{
  "scripts": {
    "lint": "next lint"
  }
}
```

---

## Upgrading: Version 14 | Next.js

**URL**: https://nextjs.org/docs/app/guides/upgrading/version-14

**Contents**:
- How to upgrade to version 14
- Upgrading from 13 to 14
  - v14 Summary

Features available in /app

To update to Next.js version 14, run the following command using your preferred package manager:

Good to know: If you are using TypeScript, ensure you also upgrade @types/react and @types/react-dom to their latest versions.

**Examples**:

```text
npm i next@next-14 react@18 react-dom@18 && npm i eslint-config-next@next-14 -D
```

```text
yarn add next@next-14 react@18 react-dom@18 && yarn add eslint-config-next@next-14 -D
```

```text
pnpm i next@next-14 react@18 react-dom@18 && pnpm i eslint-config-next@next-14 -D
```

---

## Upgrading: Version 15 | Next.js

**URL**: https://nextjs.org/docs/app/guides/upgrading/version-15

**Contents**:
- How to upgrade to version 15
- Upgrading from 14 to 15
- React 19
- Async Request APIs (Breaking change)
  - cookies
    - Recommended Async Usage
    - Temporary Synchronous Usage
  - headers

Features available in /app

To update to Next.js version 15, you can use the upgrade codemod:

If you prefer to do it manually, ensure that you're installing the latest Next & React versions:

Good to know: If you are using TypeScript, ensure you also upgrade @types/react and @types/react-dom to their latest versions.

Previously synchronous Dynamic APIs that rely on runtime information are now asynchronous:

To ease the burden of migration, a codemod is available to automate the process and the APIs can temporarily be accessed synchronously.

The runtime segment configuration previously supported a value of experimental-edge in addition to edge. Both configurations refer to the same thing, and to simplify the options, we will now error if experimental-edge is used. To fix this, update your runtime configuration to edge. A codemod is available to automatically do this.

fetch requests are no longer cached by default.

To opt specific fetch requests into caching, you can pass the cache: 'force-cache' option.

To opt all fetch requests in a layout or page into caching, you can use the export const fetchCache = 'default-cache' segment config option. If individual fetch requests specify a cache option, that will be used instead.

GET functions in Route Handlers are no longer cached by default. To opt GET methods into caching, you can use a route config option such as export const dynamic = 'force-static' in your Route Handler file.

When navigating between pages via <Link> or useRouter, page segments are no longer reused from the client-side router cache. However, they are still reused during browser backward and forward navigation and for shared layouts.

To opt page segments into caching, you can use the staleTimes config option:

Layouts and loading states are still cached and reused on navigation.

The @next/font package has been removed in favor of the built-in next/font. A codemod is available to safely and automatically rename your imports.

experimental.bundlePa

*[Content truncated - see full docs]*

**Examples**:

```text
npx @next/codemod@canary upgrade latest
```

```text
npm i next@latest react@latest react-dom@latest eslint-config-next@latest
```

```python
import { cookies } from 'next/headers'
 
// Before
const cookieStore = cookies()
const token = cookieStore.get('token')
 
// After
const cookieStore = await cookies()
const token = cookieStore.get('token')
```

---

## next.config.js: allowedDevOrigins | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/allowedDevOrigins

**Contents**:
- allowedDevOrigins

Features available in /app

Next.js does not automatically block cross-origin requests during development, but will block by default in a future major version of Next.js to prevent unauthorized requesting of internal assets/endpoints that are available in development mode.

To configure a Next.js application to allow requests from origins other than the hostname the server was initialized with (localhost by default) you can use the allowedDevOrigins config option.

allowedDevOrigins allows you to set additional origins that can be used in development mode. For example, to use local-origin.dev instead of only localhost, open next.config.js and add the allowedDevOrigins config:

**Examples**:

```text
module.exports = {
  allowedDevOrigins: ['local-origin.dev', '*.local-origin.dev'],
}
```

---

## next.config.js: appDir | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/appDir

**Contents**:
- appDir

Features available in /app

Good to know: This option is no longer needed as of Next.js 13.4. The App Router is now stable.

The App Router (app directory) enables support for layouts, Server Components, streaming, and colocated data fetching.

Using the app directory will automatically enable React Strict Mode. Learn how to incrementally adopt app.

---

## next.config.js: assetPrefix | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/assetPrefix

**Contents**:
- assetPrefix
- Set up a CDN

Features available in /app

Attention: Deploying to Vercel automatically configures a global CDN for your Next.js project. You do not need to manually setup an Asset Prefix.

Good to know: Next.js 9.5+ added support for a customizable Base Path, which is better suited for hosting your application on a sub-path like /docs. We do not suggest you use a custom Asset Prefix for this use case.

To set up a CDN, you can set up an asset prefix and configure your CDN's origin to resolve to the domain that Next.js is hosted on.

Open next.config.mjs and add the assetPrefix config based on the phase:

Next.js will automatically use your asset prefix for the JavaScript and CSS files it loads from the /_next/ path (.next/static/ folder). For example, with the above configuration, the following request for a JS chunk:

Would instead become:

The exact configuration for uploading your files to a given CDN will depend on your CDN of choice. The only folder you need to host on your CDN is the contents of .next/static/, which should be uploaded as _next/static/ as the above URL request indicates. Do not upload the rest of your .next/ folder, as you should not expose your server code and other configuration to the public.

While assetPrefix covers requests to _next/static, it does not influence the following paths:

**Examples**:

```python
// @ts-check
import { PHASE_DEVELOPMENT_SERVER } from 'next/constants'
 
export default (phase) => {
  const isDev = phase === PHASE_DEVELOPMENT_SERVER
  /**
   * @type {import('next').NextConfig}
   */
  const nextConfig = {
    assetPrefix: isDev ? undefined : 'https://cdn.mydomain.com',
  }
  return nextConfig
}
```

```text
/_next/static/chunks/4b9b41aaa062cbbfeff4add70f256968c51ece5d.4d708494b3aed70c04f0.js
```

```text
https://cdn.mydomain.com/_next/static/chunks/4b9b41aaa062cbbfeff4add70f256968c51ece5d.4d708494b3aed70c04f0.js
```

---

## next.config.js: authInterrupts | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/authInterrupts

**Contents**:
- authInterrupts
- Next Steps
  - forbidden
  - unauthorized
  - forbidden.js
  - unauthorized.js

Features available in /app

The authInterrupts configuration option allows you to use forbidden and unauthorized APIs in your application. While these functions are experimental, you must enable the authInterrupts option in your next.config.js file to use them:

**Examples**:

```python
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  experimental: {
    authInterrupts: true,
  },
}
 
export default nextConfig
```

---

## next.config.js: basePath | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath

**Contents**:
- basePath
  - Links
  - Images

Features available in /app

To deploy a Next.js application under a sub-path of a domain you can use the basePath config option.

basePath allows you to set a path prefix for the application. For example, to use /docs instead of '' (an empty string, the default), open next.config.js and add the basePath config:

Good to know: This value must be set at build time and cannot be changed without re-building as the value is inlined in the client-side bundles.

When linking to other pages using next/link and next/router the basePath will be automatically applied.

For example, using /about will automatically become /docs/about when basePath is set to /docs.

This makes sure that you don't have to change all links in your application when changing the basePath value.

When using the next/image component, you will need to add the basePath in front of src.

For example, using /docs/me.png will properly serve your image when basePath is set to /docs.

**Examples**:

```text
module.exports = {
  basePath: '/docs',
}
```

```javascript
export default function HomePage() {
  return (
    <>
      <Link href="/about">About Page</Link>
    </>
  )
}
```

```text
<a href="/docs/about">About Page</a>
```

---

## next.config.js: browserDebugInfoInTerminal | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/browserDebugInfoInTerminal

**Contents**:
- browserDebugInfoInTerminal
- Usage
  - Serialization limits
  - Source location

Features available in /app

The experimental.browserDebugInfoInTerminal option forwards console output and runtime errors originating in the browser to the dev server terminal.

This option is disabled by default. When enabled it only works in development mode.

Deeply nested objects/arrays are truncated using sensible defaults. You can tweak these limits:

Source locations are included by default when this feature is enabled.

Clicking the button prints this message to the terminal.

To suppress them, set showSourceLocation: false.

**Examples**:

```python
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  experimental: {
    browserDebugInfoInTerminal: true,
  },
}
 
export default nextConfig
```

```python
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  experimental: {
    browserDebugInfoInTerminal: {
      depthLimit: 5,
      edgeLimit: 100,
    },
  },
}
 
export default nextConfig
```

```javascript
'use client'
 
export default function Home() {
  return (
    <button
      type="button"
      onClick={() => {
        console.log('Hello World')
      }}
    >
      Click me
    </button>
  )
}
```

---

## next.config.js: cacheComponents | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents

**Contents**:
- cacheComponents
- Usage
- Notes

Features available in /app

The cacheComponents flag is an experimental feature in Next.js that causes data fetching operations in the App Router to be excluded from pre-renders unless they are explicitly cached. This can be useful for optimizing the performance of dynamic data fetching in Server Components.

It is useful if your application requires fresh data fetching during runtime rather than serving from a pre-rendered cache.

It is expected to be used in conjunction with use cache so that your data fetching happens at runtime by default unless you define specific parts of your application to be cached with use cache at the page, function, or component level.

To enable the cacheComponents flag, set it to true in the experimental section of your next.config.ts file:

When cacheComponents is enabled, you can use the following cache functions and configurations:

**Examples**:

```python
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  experimental: {
    cacheComponents: true,
  },
}
 
export default nextConfig
```

---

## next.config.js: cacheHandler | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath

**Contents**:
- Custom Next.js Cache Handler
- API Reference
  - get()
  - set()
  - revalidateTag()
  - resetRequestCache()
- Platform Support
- Version History

Features available in /app

You can configure the Next.js cache location if you want to persist cached pages and data to durable storage, or share the cache across multiple containers or instances of your Next.js application.

View an example of a custom cache handler and learn more about the implementation.

The cache handler can implement the following methods: get, set, revalidateTag, and resetRequestCache.

Returns the cached value or null if not found.

Returns Promise<void>.

Returns Promise<void>. Learn more about revalidating data or the revalidateTag() function.

This method resets the temporary in-memory cache for a single request before the next request.

Learn how to configure ISR when self-hosting Next.js.

**Examples**:

```text
module.exports = {
  cacheHandler: require.resolve('./cache-handler.js'),
  cacheMaxMemorySize: 0, // disable default in-memory caching
}
```

---

## next.config.js: cacheLife | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheLife

**Contents**:
- cacheLife
- Usage
- Reference

Features available in /app

The cacheLife option allows you to define custom cache profiles when using the cacheLife function inside components or functions, and within the scope of the use cache directive.

To define a profile, enable the cacheComponents flag and add the cache profile in the cacheLife object in the next.config.js file. For example, a blog profile:

You can now use this custom blog configuration in your component or function as follows:

The configuration object has key values with the following format:

**Examples**:

```python
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  experimental: {
    cacheComponents: true,
    cacheLife: {
      blog: {
        stale: 3600, // 1 hour
        revalidate: 900, // 15 minutes
        expire: 86400, // 1 day
      },
    },
  },
}
 
export default nextConfig
```

```python
import { unstable_cacheLife as cacheLife } from 'next/cache'
 
export async function getCachedData() {
  'use cache'
  cacheLife('blog')
  const data = await fetch('/api/data')
  return data
}
```

---

## next.config.js: compress | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/compress

**Contents**:
- compress
- Disabling compression

Features available in /app

By default, Next.js uses gzip to compress rendered content and static files when using next start or a custom server. This is an optimization for applications that do not have compression configured. If compression is already configured in your application via a custom server, Next.js will not add compression.

You can check if compression is enabled and which algorithm is used by looking at the Accept-Encoding (browser accepted options) and Content-Encoding (currently used) headers in the response.

To disable compression, set the compress config option to false:

We do not recommend disabling compression unless you have compression configured on your server, as compression reduces bandwidth usage and improves the performance of your application. For example, you're using nginx and want to switch to brotli, set the compress option to false to allow nginx to handle compression.

**Examples**:

```text
module.exports = {
  compress: false,
}
```

---

## next.config.js: crossOrigin | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/crossOrigin

**Contents**:
- crossOrigin
- Options

Features available in /app

Use the crossOrigin option to add a crossOrigin attribute in all <script> tags generated by the next/script component , and define how cross-origin requests should be handled.

**Examples**:

```text
module.exports = {
  crossOrigin: 'anonymous',
}
```

---

## next.config.js: cssChunking | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/cssChunking

**Contents**:
- cssChunking
- Options

Features available in /app

CSS Chunking is a strategy used to improve the performance of your web application by splitting and re-ordering CSS files into chunks. This allows you to load only the CSS that is needed for a specific route, instead of loading all the application's CSS at once.

You can control how CSS files are chunked using the experimental.cssChunking option in your next.config.js file:

You may consider using 'strict' if you run into unexpected CSS behavior. For example, if you import a.css and b.css in different files using a different import order (a before b, or b before a), true will merge the files in any order and assume there are no dependencies between them. However, if b.css depends on a.css, you may want to use 'strict' to prevent the files from being merged, and instead, load them in the order they are imported - which can result in more chunks and requests.

For most applications, we recommend true as it leads to fewer requests and better performance.

**Examples**:

```python
import type { NextConfig } from 'next'
 
const nextConfig = {
  experimental: {
    cssChunking: true, // default
  },
} satisfies NextConfig
 
export default nextConfig
```

---

## next.config.js: devIndicators | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/devIndicators

**Contents**:
- devIndicators
- Troubleshooting
  - Indicator not marking a route as static
- Version History

Features available in /app

devIndicators allows you to configure the on-screen indicator that gives context about the current route you're viewing during development.

Setting devIndicators to false will hide the indicator, however Next.js will continue to surface any build or runtime errors that were encountered.

If you expect a route to be static and the indicator has marked it as dynamic, it's likely the route has opted out of static rendering.

You can confirm if a route is static or dynamic by building your application using next build --debug, and checking the output in your terminal. Static (or prerendered) routes will display a ○ symbol, whereas dynamic routes will display a ƒ symbol. For example:

There are two reasons a route might opt out of static rendering:

Check your route for any of these conditions, and if you are not able to statically render the route, then consider using loading.js or <Suspense /> to leverage streaming.

**Examples**:

```text
devIndicators: false | {
    position?: 'bottom-right'
    | 'bottom-left'
    | 'top-right'
    | 'top-left', // defaults to 'bottom-left',
  },
```

```text
Route (app)                              Size     First Load JS
┌ ○ /_not-found                          0 B               0 kB
└ ƒ /products/[id]                       0 B               0 kB
 
○  (Static)   prerendered as static content
ƒ  (Dynamic)  server-rendered on demand
```

---

## next.config.js: distDir | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/distDir

**Contents**:
- distDir

Features available in /app

You can specify a name to use for a custom build directory to use instead of .next.

Open next.config.js and add the distDir config:

Now if you run next build Next.js will use build instead of the default .next folder.

distDir should not leave your project directory. For example, ../build is an invalid directory.

**Examples**:

```text
module.exports = {
  distDir: 'build',
}
```

---

## next.config.js: env | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/env

**Contents**:
- env

Features available in /app

Since the release of Next.js 9.4 we now have a more intuitive and ergonomic experience for adding environment variables. Give it a try!

Good to know: environment variables specified in this way will always be included in the JavaScript bundle, prefixing the environment variable name with NEXT_PUBLIC_ only has an effect when specifying them through the environment or .env files.

To add environment variables to the JavaScript bundle, open next.config.js and add the env config:

Now you can access process.env.customKey in your code. For example:

Next.js will replace process.env.customKey with 'my-value' at build time. Trying to destructure process.env variables won't work due to the nature of webpack DefinePlugin.

For example, the following line:

**Examples**:

```text
module.exports = {
  env: {
    customKey: 'my-value',
  },
}
```

```javascript
function Page() {
  return <h1>The value of customKey is: {process.env.customKey}</h1>
}
 
export default Page
```

```text
return <h1>The value of customKey is: {process.env.customKey}</h1>
```

---

## next.config.js: eslint | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/eslint

**Contents**:
- eslint

Features available in /app

When ESLint is detected in your project, Next.js fails your production build (next build) when errors are present.

If you'd like Next.js to produce production code even when your application has ESLint errors, you can disable the built-in linting step completely. This is not recommended unless you already have ESLint configured to run in a separate part of your workflow (for example, in CI or a pre-commit hook).

Open next.config.js and enable the ignoreDuringBuilds option in the eslint config:

**Examples**:

```text
module.exports = {
  eslint: {
    // Warning: This allows production builds to successfully complete even if
    // your project has ESLint errors.
    ignoreDuringBuilds: true,
  },
}
```

---

## next.config.js: experimental.middlewareClientMaxBodySize | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/middlewareClientMaxBodySize

**Contents**:
- experimental.middlewareClientMaxBodySize
- Options
  - String format (recommended)
  - Number format
- Behavior
- Example
- Good to know

Features available in /app

When middleware is used, Next.js automatically clones the request body and buffers it in memory to enable multiple reads - both in middleware and the underlying route handler. To prevent excessive memory usage, this configuration option sets a size limit on the buffered body.

By default, the maximum body size is 10MB. If a request body exceeds this limit, the body will only be buffered up to the limit, and a warning will be logged indicating which route exceeded the limit.

Specify the size using a human-readable string format:

Supported units: b, kb, mb, gb

Alternatively, specify the size in bytes as a number:

When a request body exceeds the configured limit:

If your application needs to process the full request body, you should either:

**Examples**:

```python
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  experimental: {
    middlewareClientMaxBodySize: '1mb',
  },
}
 
export default nextConfig
```

```python
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  experimental: {
    middlewareClientMaxBodySize: 1048576, // 1MB in bytes
  },
}
 
export default nextConfig
```

```python
import { NextRequest, NextResponse } from 'next/server'
 
export async function middleware(request: NextRequest) {
  // Next.js automatically buffers the body with the configured size limit
  // You can read the body in middleware...
  const body = await request.text()
 
  // If the body exceeded the limit, only partial data will be available
  console.log('Body size:', body.length)
 
  return NextResponse.next()
}
```

---

## next.config.js: expireTime | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/expireTime

**Contents**:
- expireTime

Features available in /app

You can specify a custom stale-while-revalidate expire time for CDNs to consume in the Cache-Control header for ISR enabled pages.

Open next.config.js and add the expireTime config:

Now when sending the Cache-Control header the expire time will be calculated depending on the specific revalidate period.

For example, if you have a revalidate of 15 minutes on a path and the expire time is one hour the generated Cache-Control header will be s-maxage=900, stale-while-revalidate=2700 so that it can stay stale for 15 minutes less than the configured expire time.

**Examples**:

```text
module.exports = {
  // one hour in seconds
  expireTime: 3600,
}
```

---

## next.config.js: exportPathMap | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/exportPathMap

**Contents**:
- exportPathMap
- Adding a trailing slash
- Customizing the output directory

Features available in /app

This feature is exclusive to next export and currently deprecated in favor of getStaticPaths with pages or generateStaticParams with app.

exportPathMap allows you to specify a mapping of request paths to page destinations, to be used during export. Paths defined in exportPathMap will also be available when using next dev.

Let's start with an example, to create a custom exportPathMap for an app with the following pages:

Open next.config.js and add the following exportPathMap config:

Good to know: the query field in exportPathMap cannot be used with automatically statically optimized pages or getStaticProps pages as they are rendered to HTML files at build-time and additional query information cannot be provided during next export.

The pages will then be exported as HTML files, for example, /about will become /about.html.

exportPathMap is an async function that receives 2 arguments: the first one is defaultPathMap, which is the default map used by Next.js. The second argument is an object with:

The returned object is a map of pages where the key is the pathname and the value is an object that accepts the following fields:

The exported pathname can also be a filename (for example, /readme.md), but you may need to set the Content-Type header to text/html when serving its content if it is different than .html.

It is possible to configure Next.js to export pages as index.html files and require trailing slashes, /about becomes /about/index.html and is routable via /about/. This was the default behavior prior to Next.js 9.

To switch back and add a trailing slash, open next.config.js and enable the trailingSlash config:

next export will use out as the default output directory, you can customize this using the -o argument, like so:

Warning: Using exportPathMap is deprecated and is overridden by getStaticPaths inside pages. We don't recommend using them together.

**Examples**:

```javascript
module.exports = {
  exportPathMap: async function (
    defaultPathMap,
    { dev, dir, outDir, distDir, buildId }
  ) {
    return {
      '/': { page: '/' },
      '/about': { page: '/about' },
      '/p/hello-nextjs': { page: '/post', query: { title: 'hello-nextjs' } },
      '/p/learn-nextjs': { page: '/post', query: { title: 'learn-nextjs' } },
      '/p/deploy-nextjs': { page: '/post', query: { title: 'deploy-nextjs' } },
    }
  },
}
```

```text
module.exports = {
  trailingSlash: true,
}
```

```text
next export -o outdir
```

---

## next.config.js: generateBuildId | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/generateBuildId

**Contents**:
- generateBuildId

Features available in /app

Next.js generates an ID during next build to identify which version of your application is being served. The same build should be used and boot up multiple containers.

If you are rebuilding for each stage of your environment, you will need to generate a consistent build ID to use between containers. Use the generateBuildId command in next.config.js:

**Examples**:

```javascript
module.exports = {
  generateBuildId: async () => {
    // This could be anything, using the latest git hash
    return process.env.GIT_HASH
  },
}
```

---

## next.config.js: generateEtags | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/generateEtags

**Contents**:
- generateEtags

Features available in /app

Next.js will generate etags for every page by default. You may want to disable etag generation for HTML pages depending on your cache strategy.

Open next.config.js and disable the generateEtags option:

**Examples**:

```text
module.exports = {
  generateEtags: false,
}
```

---

## next.config.js: headers | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/headers

**Contents**:
- headers
- Header Overriding Behavior
- Path Matching
  - Wildcard Path Matching
  - Regex Path Matching
- Header, Cookie, and Query Matching
- Headers with basePath support
- Headers with i18n support

Features available in /app

Headers allow you to set custom HTTP headers on the response to an incoming request on a given path.

To set custom HTTP headers you can use the headers key in next.config.js:

headers is an async function that expects an array to be returned holding objects with source and headers properties:

Headers are checked before the filesystem which includes pages and /public files.

If two headers match the same path and set the same header key, the last header key will override the first. Using the below headers, the path /hello will result in the header x-hello being world due to the last header value set being world.

Path matches are allowed, for example /blog/:slug will match /blog/hello-world (no nested paths):

To match a wildcard path you can use * after a parameter, for example /blog/:slug* will match /blog/a/b/c/d/hello-world:

To match a regex path you can wrap the regex in parenthesis after a parameter, for example /blog/:slug(\\d{1,}) will match /blog/123 but not /blog/abc:

The following characters (, ), {, }, :, *, +, ? are used for regex path matching, so when used in the source as non-special values they must be escaped by adding \\ before them:

To only apply a header when header, cookie, or query values also match the has field or don't match the missing field can be used. Both the source and all has items must match and all missing items must not match for the header to be applied.

has and missing items can have the following fields:

When leveraging basePath support with headers each source is automatically prefixed with the basePath unless you add basePath: false to the header:

When leveraging i18n support with headers each source is automatically prefixed to handle the configured locales unless you add locale: false to the header. If locale: false is used you must prefix the source with a locale for it to be matched correctly.

Next.js sets the Cache-Control header of public, max-age=31536000, immutable for truly immutab

*[Content truncated - see full docs]*

**Examples**:

```text
module.exports = {
  async headers() {
    return [
      {
        source: '/about',
        headers: [
          {
            key: 'x-custom-header',
            value: 'my custom header value',
          },
          {
            key: 'x-another-custom-header',
            value: 'my other custom header value',
          },
        ],
      },
    ]
  },
}
```

```text
module.exports = {
  async headers() {
    return [
      {
        source: '/:path*',
        headers: [
          {
            key: 'x-hello',
            value: 'there',
          },
        ],
      },
      {
        source: '/hello',
        headers: [
          {
            key: 'x-hello',
            value: 'world',
          },
        ],
      },
    ]
  },
}
```

```text
module.exports = {
  async headers() {
    return [
      {
        source: '/blog/:slug',
        headers: [
          {
            key: 'x-slug',
            value: ':slug', // Matched parameters can be used in the value
          },
          {
            key: 'x-slug-:slug', // Matched parameters can be used in the key
            value: 'my other custom header value',
          },
        ],
      },
    ]
  },
}
```

---

## next.config.js: htmlLimitedBots | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/htmlLimitedBots

**Contents**:
- htmlLimitedBots
- Default list
- Disabling
- Version History

Features available in /app

The htmlLimitedBots config allows you to specify a list of user agents that should receive blocking metadata instead of streaming metadata.

Next.js includes a default list of HTML limited bots, including:

See the full list here.

Specifying a htmlLimitedBots config will override the Next.js' default list. However, this is advanced behavior, and the default should be sufficient for most cases.

To fully disable streaming metadata:

**Examples**:

```python
import type { NextConfig } from 'next'
 
const config: NextConfig = {
  htmlLimitedBots: /MySpecialBot|MyAnotherSpecialBot|SimpleCrawler/,
}
 
export default config
```

```javascript
const config: NextConfig = {
  htmlLimitedBots: /MySpecialBot|MyAnotherSpecialBot|SimpleCrawler/,
}
 
export default config
```

```python
import type { NextConfig } from 'next'
 
const config: NextConfig = {
  htmlLimitedBots: /.*/,
}
 
export default config
```

---

## next.config.js: httpAgentOptions | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/httpAgentOptions

**Contents**:
- httpAgentOptions

Features available in /app

In Node.js versions prior to 18, Next.js automatically polyfills fetch() with undici and enables HTTP Keep-Alive by default.

To disable HTTP Keep-Alive for all fetch() calls on the server-side, open next.config.js and add the httpAgentOptions config:

**Examples**:

```text
module.exports = {
  httpAgentOptions: {
    keepAlive: false,
  },
}
```

---

## next.config.js: images | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/images

**Contents**:
- images
- Example Loader Configuration
  - Akamai
  - AWS CloudFront
  - Cloudinary
  - Cloudflare
  - Contentful
  - Fastly

Features available in /app

If you want to use a cloud provider to optimize images instead of using the Next.js built-in Image Optimization API, you can configure next.config.js with the following:

This loaderFile must point to a file relative to the root of your Next.js application. The file must export a default function that returns a string, for example:

Alternatively, you can use the loader prop to pass the function to each instance of next/image.

Good to know: Customizing the image loader file, which accepts a function, requires using Client Components to serialize the provided function.

To learn more about configuring the behavior of the built-in Image Optimization API and the Image Component, see Image Configuration Options for available options.

**Examples**:

```text
module.exports = {
  images: {
    loader: 'custom',
    loaderFile: './my/image/loader.js',
  },
}
```

```javascript
'use client'
 
export default function myImageLoader({ src, width, quality }) {
  return `https://example.com/${src}?w=${width}&q=${quality || 75}`
}
```

```javascript
// Docs: https://techdocs.akamai.com/ivm/reference/test-images-on-demand
export default function akamaiLoader({ src, width, quality }) {
  return `https://example.com/${src}?imwidth=${width}`
}
```

---

## next.config.js: inlineCss | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/inlineCss

**Contents**:
- inlineCss
- Usage
- Trade-Offs
  - When to Use Inline CSS
  - When Not to Use Inline CSS

Features available in /app

Experimental support for inlining CSS in the <head>. When this flag is enabled, all places where we normally generate a <link> tag will instead have a generated <style> tag.

Inlining CSS can be beneficial in several scenarios:

First-Time Visitors: Since CSS files are render-blocking resources, inlining eliminates the initial download delay that first-time visitors experience, improving page load performance.

Performance Metrics: By removing the additional network requests for CSS files, inlining can significantly improve key metrics like First Contentful Paint (FCP) and Largest Contentful Paint (LCP).

Slow Connections: For users on slower networks where each request adds considerable latency, inlining CSS can provide a noticeable performance boost by reducing network roundtrips.

Atomic CSS Bundles (e.g., Tailwind): With utility-first frameworks like Tailwind CSS, the size of the styles required for a page is often O(1) relative to the complexity of the design. This makes inlining a compelling choice because the entire set of styles for the current page is lightweight and doesn’t grow with the page size. Inlining Tailwind styles ensures minimal payload and eliminates the need for additional network requests, which can further enhance performance.

While inlining CSS offers significant benefits for performance, there are scenarios where it may not be the best choice:

Large CSS Bundles: If your CSS bundle is too large, inlining it may significantly increase the size of the HTML, resulting in slower Time to First Byte (TTFB) and potentially worse performance for users with slow connections.

Dynamic or Page-Specific CSS: For applications with highly dynamic styles or pages that use different sets of CSS, inlining may lead to redundancy and bloat, as the full CSS for all pages may need to be inlined repeatedly.

Browser Caching: In cases where visitors frequently return to your site, external CSS files allow browsers to cache styles effi

*[Content truncated - see full docs]*

**Examples**:

```python
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  experimental: {
    inlineCss: true,
  },
}
 
export default nextConfig
```

---

## next.config.js: logging | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/logging

**Contents**:
- logging
- Options
  - Fetching
  - Incoming Requests
  - Disabling Logging

Features available in /app

You can configure the logging level and whether the full URL is logged to the console when running Next.js in development mode.

Currently, logging only applies to data fetching using the fetch API. It does not yet apply to other logs inside of Next.js.

Any fetch requests that are restored from the Server Components HMR cache are not logged by default. However, this can be enabled by setting logging.fetches.hmrRefreshes to true.

By default all the incoming requests will be logged in the console during development. You can use the incomingRequests option to decide which requests to ignore. Since this is only logged in development, this option doesn't affect production builds.

Or you can disable incoming request logging by setting incomingRequests to false.

In addition, you can disable the development logging by setting logging to false.

**Examples**:

```text
module.exports = {
  logging: {
    fetches: {
      fullUrl: true,
    },
  },
}
```

```text
module.exports = {
  logging: {
    fetches: {
      hmrRefreshes: true,
    },
  },
}
```

```text
module.exports = {
  logging: {
    incomingRequests: {
      ignore: [/\api\/v1\/health/],
    },
  },
}
```

---

## next.config.js: mdxRs | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/mdxRs

**Contents**:
- mdxRs

Features available in /app

For experimental use with @next/mdx. Compiles MDX files using the new Rust compiler.

**Examples**:

```javascript
const withMDX = require('@next/mdx')()
 
/** @type {import('next').NextConfig} */
const nextConfig = {
  pageExtensions: ['ts', 'tsx', 'mdx'],
  experimental: {
    mdxRs: true,
  },
}
 
module.exports = withMDX(nextConfig)
```

---

## next.config.js: onDemandEntries | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/onDemandEntries

**Contents**:
- onDemandEntries

Features available in /app

Next.js exposes some options that give you some control over how the server will dispose or keep in memory built pages in development.

To change the defaults, open next.config.js and add the onDemandEntries config:

**Examples**:

```text
module.exports = {
  onDemandEntries: {
    // period (in ms) where the server will keep pages in the buffer
    maxInactiveAge: 25 * 1000,
    // number of pages that should be kept simultaneously without being disposed
    pagesBufferLength: 2,
  },
}
```

---

## next.config.js: optimizePackageImports | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/optimizePackageImports

**Contents**:
- optimizePackageImports

Features available in /app

Some packages can export hundreds or thousands of modules, which can cause performance issues in development and production.

Adding a package to experimental.optimizePackageImports will only load the modules you are actually using, while still giving you the convenience of writing import statements with many named exports.

The following libraries are optimized by default:

**Examples**:

```text
module.exports = {
  experimental: {
    optimizePackageImports: ['package-name'],
  },
}
```

---

## next.config.js: output | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/output

**Contents**:
- output
- How it Works
- Automatically Copying Traced Files
- Caveats

Features available in /app

During a build, Next.js will automatically trace each page and its dependencies to determine all of the files that are needed for deploying a production version of your application.

This feature helps reduce the size of deployments drastically. Previously, when deploying with Docker you would need to have all files from your package's dependencies installed to run next start. Starting with Next.js 12, you can leverage Output File Tracing in the .next/ directory to only include the necessary files.

Furthermore, this removes the need for the deprecated serverless target which can cause various issues and also creates unnecessary duplication.

During next build, Next.js will use @vercel/nft to statically analyze import, require, and fs usage to determine all files that a page might load.

Next.js' production server is also traced for its needed files and output at .next/next-server.js.nft.json which can be leveraged in production.

To leverage the .nft.json files emitted to the .next output directory, you can read the list of files in each trace that are relative to the .nft.json file and then copy them to your deployment location.

Next.js can automatically create a standalone folder that copies only the necessary files for a production deployment including select files in node_modules.

To leverage this automatic copying you can enable it in your next.config.js:

This will create a folder at .next/standalone which can then be deployed on its own without installing node_modules.

Additionally, a minimal server.js file is also output which can be used instead of next start. This minimal server does not copy the public or .next/static folders by default as these should ideally be handled by a CDN instead, although these folders can be copied to the standalone/public and standalone/.next/static folders manually, after which server.js file will serve these automatically.

To copy these manually, you can use the cp command-line tool after you 

*[Content truncated - see full docs]*

**Examples**:

```text
module.exports = {
  output: 'standalone',
}
```

```text
cp -r public .next/standalone/ && cp -r .next/static .next/standalone/.next/
```

```text
node .next/standalone/server.js
```

---

## next.config.js: pageExtensions | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/pageExtensions

**Contents**:
- pageExtensions

Features available in /app

By default, Next.js accepts files with the following extensions: .tsx, .ts, .jsx, .js. This can be modified to allow other extensions like markdown (.md, .mdx).

**Examples**:

```javascript
const withMDX = require('@next/mdx')()
 
/** @type {import('next').NextConfig} */
const nextConfig = {
  pageExtensions: ['js', 'jsx', 'ts', 'tsx', 'md', 'mdx'],
}
 
module.exports = withMDX(nextConfig)
```

---

## next.config.js: poweredByHeader | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/poweredByHeader

**Contents**:
- poweredByHeader

Features available in /app

By default Next.js will add the x-powered-by header. To opt-out of it, open next.config.js and disable the poweredByHeader config:

**Examples**:

```text
module.exports = {
  poweredByHeader: false,
}
```

---

## next.config.js: ppr | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/ppr

**Contents**:
- ppr
- Using Partial Prerendering
  - Incremental Adoption (Version 15)
- Learn more about Partial Prerendering
  - Partial Prerendering

Features available in /app

Partial Prerendering (PPR) enables you to combine static and dynamic components together in the same route. Learn more about PPR.

In Next.js 15, you can incrementally adopt Partial Prerendering in layouts and pages by setting the ppr option in next.config.js to incremental, and exporting the experimental_ppr route config option at the top of the file:

**Examples**:

```python
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  experimental: {
    ppr: 'incremental',
  },
}
 
export default nextConfig
```

```python
import { Suspense } from "react"
import { StaticComponent, DynamicComponent, Fallback } from "@/app/ui"
 
export const experimental_ppr = true
 
export default function Page() {
  return {
     <>
      <StaticComponent />
      <Suspense fallback={<Fallback />}>
        <DynamicComponent />
      </Suspense>
     </>
  };
}
```

---

## next.config.js: productionBrowserSourceMaps | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/productionBrowserSourceMaps

**Contents**:
- productionBrowserSourceMaps

Features available in /app

Source Maps are enabled by default during development. During production builds, they are disabled to prevent you leaking your source on the client, unless you specifically opt-in with the configuration flag.

Next.js provides a configuration flag you can use to enable browser source map generation during the production build:

When the productionBrowserSourceMaps option is enabled, the source maps will be output in the same directory as the JavaScript files. Next.js will automatically serve these files when requested.

**Examples**:

```text
module.exports = {
  productionBrowserSourceMaps: true,
}
```

---

## next.config.js: reactCompiler | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/reactCompiler

**Contents**:
- reactCompiler
- How It Works
- Annotations

Features available in /app

Next.js includes support for the React Compiler, a tool designed to improve performance by automatically optimizing component rendering. This reduces the need for manual memoization using useMemo and useCallback.

Next.js includes a custom performance optimization written in SWC that makes the React Compiler more efficient. Instead of running the compiler on every file, Next.js analyzes your project and only applies the React Compiler to relevant files. This avoids unnecessary work and leads to faster builds compared to using the Babel plugin on its own.

The React Compiler runs through a Babel plugin. To keep builds fast, Next.js uses a custom SWC optimization that only applies the React Compiler to relevant files—like those with JSX or React Hooks.

This avoids compiling everything and keeps the performance cost minimal. You may still see slightly slower builds compared to the default Rust-based compiler, but the impact is small and localized.

To use it, install the babel-plugin-react-compiler:

Then, add experimental.reactCompiler option in next.config.js:

You can configure the compiler to run in "opt-in" mode as follows:

Then, you can annotate specific components or hooks with the "use memo" directive from React to opt-in:

Note: You can also use the "use no memo" directive from React for the opposite effect, to opt-out a component or hook.

**Examples**:

```text
npm install babel-plugin-react-compiler
```

```python
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  experimental: {
    reactCompiler: true,
  },
}
 
export default nextConfig
```

```python
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  experimental: {
    reactCompiler: {
      compilationMode: 'annotation',
    },
  },
}
 
export default nextConfig
```

---

## next.config.js: reactMaxHeadersLength | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/reactMaxHeadersLength

**Contents**:
- reactMaxHeadersLength

Features available in /app

During static rendering, React can emit headers that can be added to the response. These can be used to improve performance by allowing the browser to preload resources like fonts, scripts, and stylesheets. The default value is 6000, but you can override this value by configuring the reactMaxHeadersLength option in next.config.js:

Good to know: This option is only available in App Router.

Depending on the type of proxy between the browser and the server, the headers can be truncated. For example, if you are using a reverse proxy that doesn't support long headers, you should set a lower value to ensure that the headers are not truncated.

**Examples**:

```text
module.exports = {
  reactMaxHeadersLength: 1000,
}
```

---

## next.config.js: reactStrictMode | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/reactStrictMode

**Contents**:
- reactStrictMode

Features available in /app

Good to know: Since Next.js 13.5.1, Strict Mode is true by default with app router, so the above configuration is only necessary for pages. You can still disable Strict Mode by setting reactStrictMode: false.

Suggested: We strongly suggest you enable Strict Mode in your Next.js application to better prepare your application for the future of React.

React's Strict Mode is a development mode only feature for highlighting potential problems in an application. It helps to identify unsafe lifecycles, legacy API usage, and a number of other features.

The Next.js runtime is Strict Mode-compliant. To opt-in to Strict Mode, configure the following option in your next.config.js:

If you or your team are not ready to use Strict Mode in your entire application, that's OK! You can incrementally migrate on a page-by-page basis using <React.StrictMode>.

**Examples**:

```text
module.exports = {
  reactStrictMode: true,
}
```

---

## next.config.js: redirects | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects

**Contents**:
- redirects
- Path Matching
  - Wildcard Path Matching
  - Regex Path Matching
- Header, Cookie, and Query Matching
  - Redirects with basePath support
  - Redirects with i18n support
- Other Redirects

Features available in /app

Redirects allow you to redirect an incoming request path to a different destination path.

To use redirects you can use the redirects key in next.config.js:

redirects is an async function that expects an array to be returned holding objects with source, destination, and permanent properties:

Why does Next.js use 307 and 308? Traditionally a 302 was used for a temporary redirect, and a 301 for a permanent redirect, but many browsers changed the request method of the redirect to GET, regardless of the original method. For example, if the browser made a request to POST /v1/users which returned status code 302 with location /v2/users, the subsequent request might be GET /v2/users instead of the expected POST /v2/users. Next.js uses the 307 temporary redirect, and 308 permanent redirect status codes to explicitly preserve the request method used.

Redirects are checked before the filesystem which includes pages and /public files.

When using the Pages Router, redirects are not applied to client-side routing (Link, router.push) unless Middleware is present and matches the path.

When a redirect is applied, any query values provided in the request will be passed through to the redirect destination. For example, see the following redirect configuration:

Good to know: Remember to include the forward slash / before the colon : in path parameters of the source and destination paths, otherwise the path will be treated as a literal string and you run the risk of causing infinite redirects.

When /old-blog/post-1?hello=world is requested, the client will be redirected to /blog/post-1?hello=world.

Path matches are allowed, for example /old-blog/:slug will match /old-blog/hello-world (no nested paths):

To match a wildcard path you can use * after a parameter, for example /blog/:slug* will match /blog/a/b/c/d/hello-world:

To match a regex path you can wrap the regex in parentheses after a parameter, for example /post/:slug(\\d{1,}) will match /post/

*[Content truncated - see full docs]*

**Examples**:

```text
module.exports = {
  async redirects() {
    return [
      {
        source: '/about',
        destination: '/',
        permanent: true,
      },
    ]
  },
}
```

```text
{
  source: '/old-blog/:path*',
  destination: '/blog/:path*',
  permanent: false
}
```

```text
module.exports = {
  async redirects() {
    return [
      {
        source: '/old-blog/:slug',
        destination: '/news/:slug', // Matched parameters can be used in the destination
        permanent: true,
      },
    ]
  },
}
```

---

## next.config.js: rewrites | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites

**Contents**:
- rewrites
- Rewrite parameters
- Path Matching
  - Wildcard Path Matching
  - Regex Path Matching
- Header, Cookie, and Query Matching
- Rewriting to an external URL
  - Incremental adoption of Next.js

Features available in /app

Rewrites allow you to map an incoming request path to a different destination path.

Rewrites act as a URL proxy and mask the destination path, making it appear the user hasn't changed their location on the site. In contrast, redirects will reroute to a new page and show the URL changes.

To use rewrites you can use the rewrites key in next.config.js:

Rewrites are applied to client-side routing. In the example above, navigating to <Link href="/about"> will serve content from / while keeping the URL as /about.

rewrites is an async function that expects to return either an array or an object of arrays (see below) holding objects with source and destination properties:

When the rewrites function returns an array, rewrites are applied after checking the filesystem (pages and /public files) and before dynamic routes. When the rewrites function returns an object of arrays with a specific shape, this behavior can be changed and more finely controlled, as of v10.1 of Next.js:

Good to know: rewrites in beforeFiles do not check the filesystem/dynamic routes immediately after matching a source, they continue until all beforeFiles have been checked.

The order Next.js routes are checked is:

When using parameters in a rewrite the parameters will be passed in the query by default when none of the parameters are used in the destination.

If a parameter is used in the destination none of the parameters will be automatically passed in the query.

You can still pass the parameters manually in the query if one is already used in the destination by specifying the query in the destination.

Good to know: Static pages from Automatic Static Optimization or prerendering params from rewrites will be parsed on the client after hydration and provided in the query.

Path matches are allowed, for example /blog/:slug will match /blog/hello-world (no nested paths):

To match a wildcard path you can use * after a parameter, for example /blog/:slug* will match /blog

*[Content truncated - see full docs]*

**Examples**:

```text
module.exports = {
  async rewrites() {
    return [
      {
        source: '/about',
        destination: '/',
      },
    ]
  },
}
```

```text
module.exports = {
  async rewrites() {
    return {
      beforeFiles: [
        // These rewrites are checked after headers/redirects
        // and before all files including _next/public files which
        // allows overriding page files
        {
          source: '/some-page',
          destination: '/somewhere-else',
          has: [{ type: 'query', key: 'overrideMe' }],
        },
      ],
      afterFiles: [
        // These rewrites are checked after pages/public files
        // are 
...
```

```text
module.exports = {
  async rewrites() {
    return [
      {
        source: '/old-about/:path*',
        destination: '/about', // The :path parameter isn't used here so will be automatically passed in the query
      },
    ]
  },
}
```

---

## next.config.js: sassOptions | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/sassOptions

**Contents**:
- sassOptions

Features available in /app

sassOptions allow you to configure the Sass compiler.

Good to know: sassOptions are not typed outside of implementation because Next.js does not maintain the other possible properties.

**Examples**:

```python
import type { NextConfig } from 'next'
 
const sassOptions = {
  additionalData: `
    $var: red;
  `,
}
 
const nextConfig: NextConfig = {
  sassOptions: {
    ...sassOptions,
    implementation: 'sass-embedded',
  },
}
 
export default nextConfig
```

---

## next.config.js: serverActions | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/serverActions

**Contents**:
- serverActions
- allowedOrigins
- bodySizeLimit
- Enabling Server Actions (v13)

Features available in /app

Options for configuring Server Actions behavior in your Next.js application.

A list of extra safe origin domains from which Server Actions can be invoked. Next.js compares the origin of a Server Action request with the host domain, ensuring they match to prevent CSRF attacks. If not provided, only the same origin is allowed.

By default, the maximum size of the request body sent to a Server Action is 1MB, to prevent the consumption of excessive server resources in parsing large amounts of data, as well as potential DDoS attacks.

However, you can configure this limit using the serverActions.bodySizeLimit option. It can take the number of bytes or any string format supported by bytes, for example 1000, '500kb' or '3mb'.

Server Actions became a stable feature in Next.js 14, and are enabled by default. However, if you are using an earlier version of Next.js, you can enable them by setting experimental.serverActions to true.

**Examples**:

```text
/** @type {import('next').NextConfig} */
 
module.exports = {
  experimental: {
    serverActions: {
      allowedOrigins: ['my-proxy.com', '*.my-proxy.com'],
    },
  },
}
```

```text
/** @type {import('next').NextConfig} */
 
module.exports = {
  experimental: {
    serverActions: {
      bodySizeLimit: '2mb',
    },
  },
}
```

```javascript
/** @type {import('next').NextConfig} */
const config = {
  experimental: {
    serverActions: true,
  },
}
 
module.exports = config
```

---

## next.config.js: serverComponentsHmrCache | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/serverComponentsHmrCache

**Contents**:
- serverComponentsHmrCache

Features available in /app

The experimental serverComponentsHmrCache option allows you to cache fetch responses in Server Components across Hot Module Replacement (HMR) refreshes in local development. This results in faster responses and reduced costs for billed API calls.

By default, the HMR cache applies to all fetch requests, including those with the cache: 'no-store' option. This means uncached requests will not show fresh data between HMR refreshes. However, the cache will be cleared on navigation or full-page reloads.

You can disable the HMR cache by setting serverComponentsHmrCache to false in your next.config.js file:

Good to know: For better observability, we recommend using the logging.fetches option which logs fetch cache hits and misses in the console during development.

**Examples**:

```python
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  experimental: {
    serverComponentsHmrCache: false, // defaults to true
  },
}
 
export default nextConfig
```

---

## next.config.js: serverExternalPackages | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/serverExternalPackages

**Contents**:
- serverExternalPackages

Features available in /app

Dependencies used inside Server Components and Route Handlers will automatically be bundled by Next.js.

If a dependency is using Node.js specific features, you can choose to opt-out specific dependencies from the Server Components bundling and use native Node.js require.

Next.js includes a short list of popular packages that currently are working on compatibility and automatically opt-ed out:

**Examples**:

```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  serverExternalPackages: ['@acme/ui'],
}
 
module.exports = nextConfig
```

---

## next.config.js: staleTimes | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/staleTimes

**Contents**:
- staleTimes
  - Version History

Features available in /app

staleTimes is an experimental feature that enables caching of page segments in the client-side router cache.

You can enable this experimental feature and provide custom revalidation times by setting the experimental staleTimes flag:

The static and dynamic properties correspond with the time period (in seconds) based on different types of link prefetching.

You can learn more about the Client Router Cache here.

**Examples**:

```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    staleTimes: {
      dynamic: 30,
      static: 180,
    },
  },
}
 
module.exports = nextConfig
```

---

## next.config.js: staticGeneration* | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/staticGeneration

**Contents**:
- staticGeneration*
- Config Options

Features available in /app

The staticGeneration* options allow you to configure the Static Generation process for advanced use cases.

The following options are available:

**Examples**:

```python
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  experimental: {
    staticGenerationRetryCount: 1,
    staticGenerationMaxConcurrency: 8,
    staticGenerationMinPagesPerWorker: 25,
  },
}
 
export default nextConfig
```

---

## next.config.js: taint | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/taint

**Contents**:
- taint
- Usage
- Caveats
- Examples
  - Tainting an object reference
  - Tainting a unique value

Features available in /app

The taint option enables support for experimental React APIs for tainting objects and values. This feature helps prevent sensitive data from being accidentally passed to the client. When enabled, you can use:

Good to know: Activating this flag also enables the React experimental channel for app directory.

Warning: Do not rely on the taint API as your only mechanism to prevent exposing sensitive data to the client. See our security recommendations.

The taint APIs allows you to be defensive, by declaratively and explicitly marking data that is not allowed to pass through the Server-Client boundary. When an object or value, is passed through the Server-Client boundary, React throws an error.

This is helpful for cases where:

It is recommended to model your data and APIs so that sensitive data is not returned to contexts where it is not needed.

In this case, the getUserDetails function returns data about a given user. We taint the user object reference, so that it cannot cross a Server-Client boundary. For example, assuming UserCard is a Client Component.

We can still access individual fields from the tainted userDetails object.

Now, passing the entire object to the Client Component will throw an error.

In this case, we can access the server configuration by awaiting calls to config.getConfigDetails. However, the system configuration contains the SERVICE_API_KEY that we don't want to expose to clients.

We can taint the config.SERVICE_API_KEY value.

We can still access other properties of the systemConfig object.

However, passing SERVICE_API_KEY to ClientDashboard throws an error.

Note that, even though, systemConfig.SERVICE_API_KEY is reassigned to a new variable. Passing it to a Client Component still throws an error.

Whereas, a value derived from a tainted unique value, will be exposed to the client.

A better approach is to remove SERVICE_API_KEY from the data returned by getSystemConfig.

**Examples**:

```python
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  experimental: {
    taint: true,
  },
}
 
export default nextConfig
```

```python
import { experimental_taintObjectReference } from 'react'
 
function getUserDetails(id: string): UserDetails {
  const user = await db.queryUserById(id)
 
  experimental_taintObjectReference(
    'Do not use the entire user info object. Instead, select only the fields you need.',
    user
  )
 
  return user
}
```

```javascript
export async function ContactPage({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params
  const userDetails = await getUserDetails(id)
 
  return (
    <UserCard
      firstName={userDetails.firstName}
      lastName={userDetails.lastName}
    />
  )
}
```

---

## next.config.js: trailingSlash | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/trailingSlash

**Contents**:
- trailingSlash
- Version History

Features available in /app

By default Next.js will redirect URLs with trailing slashes to their counterpart without a trailing slash. For example /about/ will redirect to /about. You can configure this behavior to act the opposite way, where URLs without trailing slashes are redirected to their counterparts with trailing slashes.

Open next.config.js and add the trailingSlash config:

With this option set, URLs like /about will redirect to /about/.

When using trailingSlash: true, certain URLs are exceptions and will not have a trailing slash appended:

For example, the following URLs will remain unchanged: /file.txt, images/photos/picture.png, and .well-known/subfolder/config.json.

When used with output: "export" configuration, the /about page will output /about/index.html (instead of the default /about.html).

**Examples**:

```text
module.exports = {
  trailingSlash: true,
}
```

---

## next.config.js: transpilePackages | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/transpilePackages

**Contents**:
- transpilePackages
- Version History

Features available in /app

Next.js can automatically transpile and bundle dependencies from local packages (like monorepos) or from external dependencies (node_modules). This replaces the next-transpile-modules package.

**Examples**:

```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  transpilePackages: ['package-name'],
}
 
module.exports = nextConfig
```

---

## next.config.js: turbopackPersistentCaching | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopackPersistentCaching

**Contents**:
- turbopackPersistentCaching
- Usage
- Version Changes

Features available in /app

Turbopack Persistent Caching enables Turbopack to reduce work across next dev or next build commands. When enabled, Turbopack will save and restore data to the .next folder between builds, which can greatly speed up subsequent builds and dev sessions.

Warning: Persistent Caching is still under development and is not yet stable. Users adopting should expect some stability issues.

Good to know: Note that while next dev and next build can share cached data with each other, most cache entries are command-specific due to different configuration and environment variables.

**Examples**:

```python
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  experimental: {
    turbopackPersistentCaching: true,
  },
}
 
export default nextConfig
```

---

## next.config.js: turbopack | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack

**Contents**:
- turbopack
- Reference
  - Options
  - Supported loaders
- Examples
  - Root directory
  - Configuring webpack loaders
  - Resolving aliases

Features available in /app

The turbopack option lets you customize Turbopack to transform different files and change how modules are resolved.

The following options are available for the turbo configuration:

The following loaders have been tested to work with Turbopack's webpack loader implementation, but many other webpack loaders should work as well even if not listed here:

Turbopack uses the root directory to resolve modules. Files outside of the project root are not resolved.

Next.js automatically detects the root directory of your project. It does so by looking for one of these files:

If you have a different project structure, for example if you don't use workspaces, you can manually set the root option:

If you need loader support beyond what's built in, many webpack loaders already work with Turbopack. There are currently some limitations:

To configure loaders, add the names of the loaders you've installed and any options in next.config.js, mapping file extensions to a list of loaders.

Here is an example below using the @svgr/webpack loader, which enables importing .svg files and rendering them as React components.

For loaders that require configuration options, you can use an object format instead of a string:

Good to know: Prior to Next.js version 13.4.4, turbo.rules was named turbo.loaders and only accepted file extensions like .mdx instead of *.mdx.

Turbopack can be configured to modify module resolution through aliases, similar to webpack's resolve.alias configuration.

To configure resolve aliases, map imported patterns to their new destination in next.config.js:

This aliases imports of the underscore package to the lodash package. In other words, import underscore from 'underscore' will load the lodash module instead of underscore.

Turbopack also supports conditional aliasing through this field, similar to Node.js' conditional exports. At the moment only the browser condition is supported. In the case above, imports of the mocha module wil

*[Content truncated - see full docs]*

**Examples**:

```python
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  turbopack: {
    // ...
  },
}
 
export default nextConfig
```

```javascript
const path = require('path')
module.exports = {
  turbopack: {
    root: path.join(__dirname, '..'),
  },
}
```

```text
module.exports = {
  turbopack: {
    rules: {
      '*.svg': {
        loaders: ['@svgr/webpack'],
        as: '*.js',
      },
    },
  },
}
```

---

## next.config.js: typedRoutes | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/typedRoutes

**Contents**:
- typedRoutes

Features available in /app

Note: This option has been marked as stable, so you should use typedRoutes instead of experimental.typedRoutes.

Support for statically typed links. This feature requires using TypeScript in your project.

**Examples**:

```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  typedRoutes: true,
}
 
module.exports = nextConfig
```

---

## next.config.js: typescript | Next.js

**URL**: https://nextjs.org/docs/app/api-reference/config/next-config-js/typescript

**Contents**:
- typescript

Features available in /app

Next.js fails your production build (next build) when TypeScript errors are present in your project.

If you'd like Next.js to dangerously produce production code even when your application has errors, you can disable the built-in type checking step.

If disabled, be sure you are running type checks as part of your build or deploy process, otherwise this can be very dangerous.

Open next.config.js and enable the ignoreBuildErrors option in the typescript config:

**Examples**:

```text
module.exports = {
  typescript: {
    // !! WARN !!
    // Dangerously allow production builds to successfully complete even if
    // your project has type errors.
    // !! WARN !!
    ignoreBuildErrors: true,
  },
}
```

---
