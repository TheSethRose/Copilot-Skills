# Sveltekit - Building

**Pages**: 3

---

## Advanced routing

**URL**: https://kit.svelte.dev/docs/advanced-routing

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Advanced routing

If the number of route segments is unknown, you can use rest syntax — for example you might implement GitHub’s file viewer like so...

...in which case a request for /sveltejs/kit/tree/main/documentation/docs/04-advanced-routing.md would result in the following parameters being available to the page:

src/routes/a/[...rest]/z/+page.svelte will match /a/z (i.e. there’s no parameter at all) as well as /a/b/z and /a/b/c/z and so on. Make sure you check that the value of the rest parameter is valid, for example using a matcher.

Rest parameters also allow you to render custom 404s. Given these routes...

...the marx-brothers/+error.svelte file will not be rendered if you visit /marx-brothers/karl, because no route was matched. If you want to render the nested error page, you should create a route that matches any /marx-brothers/* request, and return a 404 from it:

Throws an error with a HTTP status code and an optional message. When called during request handling, this will cause SvelteKit to return an error response without invoking handleError. Make sure you’re not catching the thrown error, which would prevent SvelteKit from handling it.

Throws an error with a HTTP status code and an optional message. When called during request handling, this will cause SvelteKit to return an error response without invoking handleError. Make sure you’re not catching the thrown error, which would prevent SvelteKit from handling it.

Throws an error with a HTTP status code and an optional message. When called during request handling, this will cause SvelteKit to return an error response without invoking handleError. Make sure you’re not catching the thrown error, which would prevent SvelteKit from handling it.

Throws an error with a HTTP status code and an optional message. When called during request handling, this will cause SvelteKit to return an error response without invoking handleError. Make sure you’re not catching the thrown error, which would prevent SvelteKit from handling

*[Content truncated - see full docs]*

**Examples**:

```text
/[org]/[repo]/tree/[branch]/[...file]
```

```text
{
	org: 'sveltejs',
	repo: 'kit',
	branch: 'main',
	file: 'documentation/docs/04-advanced-routing.md'
}
```

```text
src/routes/
├ marx-brothers/
│ ├ chico/
│ ├ harpo/
│ ├ groucho/
│ └ +error.svelte
└ +error.svelte
```

---

## Loading data

**URL**: https://kit.svelte.dev/docs/load

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Loading data

Before a +page.svelte component (and its containing +layout.svelte components) can be rendered, we often need to get some data. This is done by defining load functions.

A +page.svelte file can have a sibling +page.js that exports a load function, the return value of which is available to the page via the data prop:

The parameters of the current page - e.g. for a route like /blog/[slug], a { slug: string } object

The parameters of the current page - e.g. for a route like /blog/[slug], a { slug: string } object

The parameters of the current page - e.g. for a route like /blog/[slug], a { slug: string } object

Before version 2.16.0, the props of a page and layout had to be typed individually:

Declares the props that a component accepts. Example:

https://svelte.dev/docs/svelte/$props

Declares the props that a component accepts. Example:

https://svelte.dev/docs/svelte/$props

In Svelte 4, you’d use export let data instead.

Thanks to the generated $types module, we get full type safety.

A load function in a +page.js file runs both on the server and in the browser (unless combined with export const ssr = false, in which case it will only run in the browser). If your load function should always run on the server (because it uses private environment variables, for example, or accesses a database) then it would go in a +page.server.js instead.

A more realistic version of your blog post’s load function, that only runs on the server and pulls data from a database, might look like this:

The parameters of the current route - e.g. for a route like /blog/[slug], a { slug: string } object.

The parameters of the current route - e.g. for a route like /blog/[slug], a { slug: string } object.

The parameters of the current route - e.g. for a route like /blog/[slug], a { slug: string } object.

The parameters of the current route - e.g. for a route like /blog/[slug], a { slug: string } object.

Notice that the type changed from PageLoad to PageServerLoad, because server load

*[Content truncated - see full docs]*

**Examples**:

```javascript
/** @type {import('./$types').PageLoad} */
export function function load({ params }: {
    params: any;
}): {
    post: {
        title: string;
        content: string;
    };
}@type{import('./$types').PageLoad}load({ params: anyparams }) {
	return {
		post: {
    title: string;
    content: string;
}post: {
			title: stringtitle: `Title for ${params: anyparams.slug} goes here`,
			content: stringcontent: `Content for ${params: anyparams.slug} goes here`
		}
	};
}
```

```javascript
function load({ params }: {
    params: any;
}): {
    post: {
        title: string;
        content: string;
    };
}
```

```javascript
function load({ params }: {
    params: any;
}): {
    post: {
        title: string;
        content: string;
    };
}
```

---

## Routing

**URL**: https://kit.svelte.dev/docs/routing

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Routing

At the heart of SvelteKit is a filesystem-based router. The routes of your app — i.e. the URL paths that users can access — are defined by the directories in your codebase:

You can change src/routes to a different directory by editing the project config.

Each route directory contains one or more route files, which can be identified by their + prefix.

We’ll introduce these files in a moment in more detail, but here are a few simple rules to help you remember how SvelteKit’s routing works:

A +page.svelte component defines a page of your app. By default, pages are rendered both on the server (SSR) for the initial request and in the browser (CSR) for subsequent navigation.

SvelteKit uses <a> elements to navigate between routes, rather than a framework-specific <Link> component.

Pages can receive data from load functions via the data prop.

PageProps was added in 2.16.0. In earlier versions, you had to type the data property manually with PageData instead, see $types.

In Svelte 4, you’d use export let data instead.

Often, a page will need to load some data before it can be rendered. For this, we add a +page.js module that exports a load function:

Throws an error with a HTTP status code and an optional message. When called during request handling, this will cause SvelteKit to return an error response without invoking handleError. Make sure you’re not catching the thrown error, which would prevent SvelteKit from handling it.

Throws an error with a HTTP status code and an optional message. When called during request handling, this will cause SvelteKit to return an error response without invoking handleError. Make sure you’re not catching the thrown error, which would prevent SvelteKit from handling it.

Throws an error with a HTTP status code and an optional message. When called during request handling, this will cause SvelteKit to return an error response without invoking handleError. Make sure you’re not catching the thrown error, which would prevent SvelteKit f

*[Content truncated - see full docs]*

**Examples**:

```text
<h1>Hello and welcome to my site!</h1>
<a href="/about">About my site</a>
```

```text
<h1>About this site</h1>
<p>TODO...</p>
<a href="/">Home</a>
```

```javascript
<script>
	/** @type {import('./$types').PageProps} */
	let { data } = $props();
</script>

<h1>{data.title}</h1>
<div>{@html data.content}</div>
```

---
