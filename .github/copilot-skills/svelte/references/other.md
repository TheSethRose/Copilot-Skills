# Svelte - Other

**Pages**: 144

---

## Accessibility

**URL**: https://svelte.dev/docs/kit/accessibility

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Accessibility

SvelteKit strives to provide an accessible platform for your app by default. Svelte’s compile-time accessibility checks will also apply to any SvelteKit application you build.

Here’s how SvelteKit’s built-in accessibility features work and what you need to do to help these features to work as well as possible. Keep in mind that while SvelteKit provides an accessible foundation, you are still responsible for making sure your application code is accessible. If you’re new to accessibility, see the “further reading” section of this guide for additional resources.

We recognize that accessibility can be hard to get right. If you want to suggest improvements to how SvelteKit handles accessibility, please open a GitHub issue.

In traditional server-rendered applications, every navigation (e.g. clicking on an <a> tag) triggers a full page reload. When this happens, screen readers and other assistive technology will read out the new page’s title so that users understand that the page has changed.

Since navigation between pages in SvelteKit happens without reloading the page (known as client-side routing), SvelteKit injects a live region onto the page that will read out the new page name after each navigation. This determines the page name to announce by inspecting the <title> element.

Because of this behavior, every page in your app should have a unique, descriptive title. In SvelteKit, you can do this by placing a <svelte:head> element on each page:

This will allow screen readers and other assistive technology to identify the new page after a navigation occurs. Providing a descriptive title is also important for SEO.

In traditional server-rendered applications, every navigation will reset focus to the top of the page. This ensures that people browsing the web with a keyboard or screen reader will start interacting with the page from the beginning.

To simulate this behavior during client-side routing, SvelteKit focuses the <body> element after each navigation and enhan

*[Content truncated - see full docs]*

**Examples**:

```text
<svelte:head>
	<title>Todo List</title>
</svelte:head>
```

```python
import { function afterNavigate(callback: (navigation: import("@sveltejs/kit").AfterNavigate) => void): voidA lifecycle function that runs the supplied callback when the current component mounts, and also whenever we navigate to a URL.
afterNavigate must be called during a component initialization. It remains active as long as the component is mounted.
afterNavigate } from '$app/navigation';

function afterNavigate(callback: (navigation: import("@sveltejs/kit").AfterNavigate) => void): voidA lif
...
```

```javascript
function afterNavigate(callback: (navigation: import("@sveltejs/kit").AfterNavigate) => void): void
```

---

## Adapters

**URL**: https://svelte.dev/docs/kit/adapters

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Adapters

Before you can deploy your SvelteKit app, you need to adapt it for your deployment target. Adapters are small plugins that take the built app as input and generate output for deployment.

Official adapters exist for a variety of platforms — these are documented on the following pages:

Additional community-provided adapters exist for other platforms.

Your adapter is specified in svelte.config.js:

Your adapter is run when executing vite build. It determines how the output is converted for different platforms.

Some adapters may have access to additional information about the request. For example, Cloudflare Workers can access an env object containing KV namespaces etc. This can be passed to the RequestEvent used in hooks and server routes as the platform property — consult each adapter’s documentation to learn more.

Edit this page on GitHub llms.txt

**Examples**:

```python
import const adapter: (opts: any) => import("@sveltejs/kit").Adapteradapter from 'svelte-adapter-foo';

/** @type {import('@sveltejs/kit').Config} */
const const config: Config@type{import('@sveltejs/kit').Config}config = {
	Config.kit?: KitConfig | undefinedSvelteKit options.
@seehttps://svelte.dev/docs/kit/configurationkit: {
		KitConfig.adapter?: Adapter | undefinedYour adapter is run when executing vite build. It determines how the output is converted for different platforms.
@defaultundefin
...
```

```javascript
const adapter: (opts: any) => import("@sveltejs/kit").Adapter
```

```javascript
const config: Config
```

---

## Additional resources

**URL**: https://svelte.dev/docs/kit/additional-resources

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Additional resources

Please see the SvelteKit FAQ for solutions to common issues and helpful tips and tricks.

The Svelte FAQ and vite-plugin-svelte FAQ may also be helpful for questions deriving from those libraries.

We’ve written and published a few different SvelteKit sites as examples:

SvelteKit users have also published plenty of examples on GitHub, under the #sveltekit and #sveltekit-template topics, as well as on the Svelte Society site. Note that these have not been vetted by the maintainers and may not be up to date.

You can ask for help on Discord and StackOverflow. Please first search for information related to your issue in the FAQ, Google or another search engine, issue tracker, and Discord chat history in order to be respectful of others’ time. There are many more people asking questions than answering them, so this will help in allowing the community to grow in a scalable fashion.

Edit this page on GitHub llms.txt

---

## Advanced routing

**URL**: https://svelte.dev/docs/kit/advanced-routing

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

## Auth

**URL**: https://svelte.dev/docs/kit/auth

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Auth

Auth refers to authentication and authorization, which are common needs when building a web application. Authentication means verifying that the user is who they say they are based on their provided credentials. Authorization means determining which actions they are allowed to take.

After the user has provided their credentials such as a username and password, we want to allow them to use the application without needing to provide their credentials again for future requests. Users are commonly authenticated on subsequent requests with either a session identifier or signed token such as a JSON Web Token (JWT).

Session IDs are most commonly stored in a database. They can be immediately revoked, but require a database query to be made on each request.

In contrast, JWT generally are not checked against a datastore, which means they cannot be immediately revoked. The advantage of this method is improved latency and reduced load on your datastore.

Auth cookies can be checked inside server hooks. If a user is found matching the provided credentials, the user information can be stored in locals.

Lucia is a good reference for session-based web app auth. It contains example code snippets and projects for implementing session-based auth within SvelteKit and other JS projects. You can add code which follows the Lucia guide to your project with npx sv create when creating a new project or npx sv add lucia for an existing project.

An auth system is tightly coupled to a web framework because most of the code lies in validating user input, handling errors, and directing users to the appropriate next page. As a result, many of the generic JS auth libraries include one or more web frameworks within them. For this reason, many users will find it preferrable to follow a SvelteKit-specific guide such as the examples found in Lucia rather than having multiple web frameworks inside their project.

Edit this page on GitHub llms.txt

---

## Breakpoint Debugging

**URL**: https://svelte.dev/docs/kit/debugging

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Breakpoint Debugging

In addition to the @debug tag, you can also debug Svelte and SvelteKit projects using breakpoints within various tools and development environments. This includes both frontend and backend code.

The following guides assume your JavaScript runtime environment is Node.js.

With the built-in debug terminal, you can set up breakpoints in source files within VSCode.

You may alternatively set up a .vscode/launch.json in your project. To set one up automatically:

Here’s an example launch.json:

Further reading: https://code.visualstudio.com/docs/editor/debugging.

If you use a different editor, these community guides might be useful for you:

It’s possible to debug Node.js applications using a browser-based debugger.

Note this only works with debugging client-side SvelteKit source maps.

You may alternatively open the debugger devtools by navigating to chrome://inspect in Google Chrome, or edge://inspect in Microsoft Edge.

Edit this page on GitHub llms.txt

**Examples**:

```text
{
	"version": "0.2.0",
	"configurations": [
		{
			"command": "npm run dev",
			"name": "Run development server",
			"request": "launch",
			"type": "node-terminal"
		}
	]
}
```

---

## Building your app

**URL**: https://svelte.dev/docs/kit/building-your-app

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Building your app

Building a SvelteKit app happens in two stages, which both happen when you run vite build (usually via npm run build).

Firstly, Vite creates an optimized production build of your server code, your browser code, and your service worker (if you have one). Prerendering is executed at this stage, if appropriate.

Secondly, an adapter takes this production build and tunes it for your target environment — more on this on the following pages.

SvelteKit will load your +page/layout(.server).js files (and all files they import) for analysis during the build. Any code that should not be executed at this stage must check that building from $app/environment is false:

SvelteKit analyses your app during the build step by running it. During this process, building is true. This also applies during prerendering.

SvelteKit analyses your app during the build step by running it. During this process, building is true. This also applies during prerendering.

After building, you can view your production build locally with vite preview (via npm run preview). Note that this will run the app in Node, and so is not a perfect reproduction of your deployed app — adapter-specific adjustments like the platform object do not apply to previews.

Edit this page on GitHub llms.txt

**Examples**:

```javascript
import { const building: booleanSvelteKit analyses your app during the build step by running it. During this process, building is true. This also applies during prerendering.
```

```javascript
const building: boolean
```

---

## Cloudflare

**URL**: https://svelte.dev/docs/kit/adapter-cloudflare

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Cloudflare

To deploy to Cloudflare Workers or Cloudflare Pages, use adapter-cloudflare.

This adapter will be installed by default when you use adapter-auto. If you plan on staying with Cloudflare, you can switch from adapter-auto to using this adapter directly so that event.platform is emulated during local development, type declarations are automatically applied, and the ability to set Cloudflare-specific options is provided.

Install with npm i -D @sveltejs/adapter-cloudflare, then add the adapter to your svelte.config.js:

Path to your Wrangler configuration file. If you would like to use a Wrangler configuration filename other than wrangler.jsonc, wrangler.json, or wrangler.toml you can specify it using this option.

Preferences for the emulated platform.env local bindings. See the getPlatformProxy Wrangler API documentation for a full list of options.

Whether to render a plaintext 404.html page or a rendered SPA fallback page for non-matching asset requests.

For Cloudflare Workers, the default behaviour is to return a null-body 404-status response for non-matching assets requests. However, if the assets.not_found_handling Wrangler configuration setting is set to "404-page", this page will be served if a request fails to match an asset. If assets.not_found_handling is set to "single-page-application", the adapter will render a SPA fallback index.html page regardless of the fallback option specified.

For Cloudflare Pages, this page will only be served when a request that matches an entry in routes.exclude fails to match an asset.

Most of the time plaintext is sufficient, but if you are using routes.exclude to manually exclude a set of prerendered pages without exceeding the 100 route limit, you may wish to use spa instead to avoid showing an unstyled 404 page to users.

See Cloudflare Pages’ Not Found behaviour for more info.

Only for Cloudflare Pages. Allows you to customise the _routes.json file generated by adapter-cloudflare.

You can have up to 100 include and ex

*[Content truncated - see full docs]*

**Examples**:

```python
import import adapteradapter from '@sveltejs/adapter-cloudflare';

/** @type {import('@sveltejs/kit').Config} */
const const config: {
    kit: {
        adapter: any;
    };
}@type{import('@sveltejs/kit').Config}config = {
	kit: {
    adapter: any;
}kit: {
		adapter: anyadapter: import adapteradapter({
			// See below for an explanation of these options
			config: undefinedconfig: var undefinedundefined,
			platformProxy: {
    configPath: undefined;
    environment: undefined;
    persist: und
...
```

```text
import adapter
```

```javascript
const config: {
    kit: {
        adapter: any;
    };
}
```

---

## Cloudflare Workers

**URL**: https://svelte.dev/docs/kit/adapter-cloudflare-workers

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Cloudflare Workers

adapter-cloudflare-workers has been deprecated in favour of adapter-cloudflare. We recommend using adapter-cloudflare to deploy to Cloudflare Workers with Static Assets since Cloudflare Workers Sites will be deprecated in favour of it.

To deploy to Cloudflare Workers with Workers Sites, use adapter-cloudflare-workers.

Install with npm i -D @sveltejs/adapter-cloudflare-workers, then add the adapter to your svelte.config.js:

Path to your Wrangler configuration file. If you would like to use a Wrangler configuration filename other than wrangler.jsonc, wrangler.json, or wrangler.toml you can specify it using this option.

Preferences for the emulated platform.env local bindings. See the getPlatformProxy Wrangler API documentation for a full list of options.

This adapter expects to find a Wrangler configuration file in the project root. It should look something like this:

<your-service-name> can be anything. <your-account-id> can be found by running wrangler whoami using the Wrangler CLI tool or by logging into your Cloudflare dashboard and grabbing it from the end of the URL:

You should add the .cloudflare directory (or whichever directories you specified for main and site.bucket) and the .wrangler directory to your .gitignore.

You will need to install Wrangler and log in, if you haven’t already:

Then, you can build your app and deploy it:

The env object contains your project’s bindings, which consist of KV/DO namespaces, etc. It is passed to SvelteKit via the platform property, along with ctx, caches, and cf, meaning that you can access it in hooks and endpoints:

The original request object.

Additional data made available through the adapter.

Additional data made available through the adapter.

The original request object.

Additional data made available through the adapter.

Additional data made available through the adapter.

SvelteKit’s built-in $env module should be preferred for environment variables.

To make these types available to your app, install

*[Content truncated - see full docs]*

**Examples**:

```python
import import adapteradapter from '@sveltejs/adapter-cloudflare-workers';

/** @type {import('@sveltejs/kit').Config} */
const const config: {
    kit: {
        adapter: any;
    };
}@type{import('@sveltejs/kit').Config}config = {
	kit: {
    adapter: any;
}kit: {
		adapter: anyadapter: import adapteradapter({
			// see below for options that can be set here
		})
	}
};

export default const config: {
    kit: {
        adapter: any;
    };
}@type{import('@sveltejs/kit').Config}config;
```

```text
import adapter
```

```javascript
const config: {
    kit: {
        adapter: any;
    };
}
```

---

## Compiler errors

**URL**: https://svelte.dev/docs/svelte/compiler-errors

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

The following is an error:

Here, foo is not available inside failed. The top level code inside <svelte:boundary> becomes part of the implicit children snippet, in other words the above code is equivalent to this:

The same applies to components:

The following CSS is invalid:

This is mixing a :global block, which means “everything in here is unscoped”, with a scoped selector (x in this case). As a result it’s not possible to transform the inner selector (y in this case) into something that satisfies both requirements. You therefore have to split this up into two selectors:

In legacy mode, it was possible to reassign or bind to the each block argument itself:

This turned out to be buggy and unpredictable, particularly when working with derived values (such as array.map(...)), and as such is forbidden in runes mode. You can achieve the same outcome by using the index instead:

HTML restricts where certain elements can appear. In case of a violation the browser will ‘repair’ the HTML in a way that breaks Svelte’s assumptions about the structure of your components. Some examples:

It’s possible to export a snippet from a <script module> block, but only if it doesn’t reference anything defined inside a non-module-level <script>. For example you can’t do this...

...because greeting references message, which is defined in the second <script>.

An assignment to a class field that uses a $state or $derived rune is considered a state field declaration. The declaration can happen in the class body...

Declares reactive state.

https://svelte.dev/docs/svelte/$state

...or inside the constructor...

Declares reactive state.

https://svelte.dev/docs/svelte/$state

...but it can only happen once.

Using a $ prefix to refer to the value of a store is only possible inside .svelte files, where Svelte can automatically create subscriptions when a component is mounted and unsubscribe when the component is unmounted. Consider migrating to runes instead.

See https://html.spec.whatw

*[Content truncated - see full docs]*

**Examples**:

```text
An element can only have one 'animate' directive
```

```text
An element that uses the `animate:` directive must be the only child of a keyed `{#each ...}` block
```

```text
An element that uses the `animate:` directive must be the only child of a keyed `{#each ...}` block. Did you forget to add a key to your each block?
```

---

## Compiler warnings

**URL**: https://svelte.dev/docs/svelte/compiler-warnings

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

Svelte warns you at compile time if it catches potential mistakes, such as writing inaccessible markup.

Some warnings may be incorrect in your concrete use case. You can disable such false positives by placing a <!-- svelte-ignore <code> --> comment above the line that causes the warning. Example:

You can list multiple rules in a single comment (separated by commas), and add an explanatory note (in parentheses) alongside them:

Enforce no accesskey on element. Access keys are HTML attributes that allow web developers to assign keyboard shortcuts to elements. Inconsistencies between keyboard shortcuts and keyboard commands used by screen reader and keyboard-only users create accessibility complications. To avoid complications, access keys should not be used.

An element with aria-activedescendant must be tabbable, so it must either have an inherent tabindex or declare tabindex as an attribute.

Certain reserved DOM elements do not support ARIA roles, states and properties. This is often because they are not visible, for example meta, html, script, style. This rule enforces that these DOM elements do not contain the aria-* props.

Enforce that autofocus is not used on elements. Autofocusing elements can cause usability issues for sighted and non-sighted users alike.

Enforce that visible, non-interactive elements with an onclick event are accompanied by a keyboard event handler.

Users should first consider whether an interactive element might be more appropriate such as a <button type="button"> element for actions or <a> element for navigations. These elements are more semantically meaningful and will have built-in key handling. E.g. Space and Enter will trigger a <button> and Enter will trigger an <a> element.

If a non-interactive element is required then onclick should be accompanied by an onkeyup or onkeydown handler that enables the user to perform equivalent actions via the keyboard. In order for the user to be able to trigger a key press, the element will al

*[Content truncated - see full docs]*

**Examples**:

```text
<!-- svelte-ignore a11y_autofocus -->
<input autofocus />
```

```text
<!-- svelte-ignore a11y_click_events_have_key_events, a11y_no_static_element_interactions (because of reasons) -->
<div onclick>...</div>
```

```text
Avoid using accesskey
```

---

## Context

**URL**: https://svelte.dev/docs/svelte/context

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

Context allows components to access values owned by parent components without passing them down as props (potentially through many layers of intermediate components, known as ‘prop-drilling’). The parent component sets context with setContext(key, value)...

...and the child retrieves it with getContext:

This is particularly useful when Parent.svelte is not directly aware of Child.svelte, but instead renders it as part of a children snippet (demo):

The key ('my-context', in the example above) and the context itself can be any JavaScript value.

In addition to setContext and getContext, Svelte exposes hasContext and getAllContexts functions.

You can store reactive state in context (demo)...

...though note that if you reassign counter instead of updating it, you will ‘break the link’ — in other words instead of this...

Svelte will warn you if you get it wrong.

As an alternative to using setContext and getContext directly, you can use them via createContext. This gives you type safety and makes it unnecessary to use a key:

Returns a [get, set] pair of functions for working with context in a type-safe way.

Returns a [get, set] pair of functions for working with context in a type-safe way.

When you have state shared by many different components, you might be tempted to put it in its own module and just import it wherever it’s needed:

Declares reactive state.

https://svelte.dev/docs/svelte/$state

In many cases this is perfectly fine, but there is a risk: if you mutate the state during server-side rendering (which is discouraged, but entirely possible!)...

...then the data may be accessible by the next user. Context solves this problem because it is not shared between requests.

Edit this page on GitHub llms.txt

**Examples**:

```python
<script>
	import { setContext } from 'svelte';

	setContext('my-context', 'hello from Parent.svelte');
</script>
```

```python
<script lang="ts">
	import { setContext } from 'svelte';

	setContext('my-context', 'hello from Parent.svelte');
</script>
```

```python
<script>
	import { getContext } from 'svelte';

	const message = getContext('my-context');
</script>

<h1>{message}, inside Child.svelte</h1>
```

---

## Creating a project

**URL**: https://svelte.dev/docs/kit/creating-a-project

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Creating a project

The easiest way to start building a SvelteKit app is to run npx sv create:

The first command will scaffold a new project in the my-app directory asking if you’d like to set up some basic tooling such as TypeScript. See the CLI docs for information about these options and the integrations page for pointers on setting up additional tooling. npm run dev will then start the development server on localhost:5173 - make sure you install dependencies before running this if you didn’t do so during project creation.

There are two basic concepts:

Try editing the files to get a feel for how everything works.

We recommend using Visual Studio Code (aka VS Code) with the Svelte extension, but support also exists for numerous other editors.

Edit this page on GitHub llms.txt

**Examples**:

```text
npx sv create my-app
cd my-app
npm run dev
```

---

## Custom elements

**URL**: https://svelte.dev/docs/svelte/custom-elements

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

Svelte components can also be compiled to custom elements (aka web components) using the customElement: true compiler option. You should specify a tag name for the component using the <svelte:options> element. Within the custom element you can access the host element via the $host rune.

You can leave out the tag name for any of your inner components which you don’t want to expose and use them like regular Svelte components. Consumers of the component can still name it afterwards if needed, using the static element property which contains the custom element constructor and which is available when the customElement compiler option is true.

Defines a new custom element, mapping the given name to the given constructor as an autonomous custom element.

Once a custom element has been defined, it can be used as a regular DOM element:

Specifies the beginning and end of the document body.

Any props are exposed as properties of the DOM element (as well as being readable/writable as attributes, where possible).

Returns the first element that is a descendant of node that matches selectors.

The console module provides a simple debugging console that is similar to the JavaScript console mechanism provided by web browsers.

The module exports two specific components:

Warning: The global console object’s methods are neither consistently synchronous like the browser APIs they resemble, nor are they consistently asynchronous like all other Node.js streams. See the note on process I/O for more information.

Example using the global console:

Example using the Console class:

Prints to stdout with newline. Multiple arguments can be passed, with the first used as the primary message and all additional used as substitution values similar to printf(3) (the arguments are all passed to util.format()).

See util.format() for more information.

Note that you need to list out all properties explicitly, i.e. doing let props = $props() without declaring props in the component options mean

*[Content truncated - see full docs]*

**Examples**:

```javascript
<svelte:options customElement="my-element" />

<script>
	let { name = 'world' } = $props();
</script>

<h1>Hello {name}!</h1>
<slot />
```

```python
import type MyElement = SvelteComponent<Record<string, any>, any, any>
const MyElement: LegacyComponentTypeMyElement from './MyElement.svelte';

var customElements: CustomElementRegistryDefines a new custom element, mapping the given name to the given constructor as an autonomous custom element.
MDN Reference
customElements.CustomElementRegistry.define(name: string, constructor: CustomElementConstructor, options?: ElementDefinitionOptions): voidMDN Reference
define('my-element', const MyElement:
...
```

```javascript
type MyElement = SvelteComponent<Record<string, any>, any, any>
const MyElement: LegacyComponentType
```

---

## Custom properties

**URL**: https://svelte.dev/docs/svelte/custom-properties

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

You can pass CSS custom properties — both static and dynamic — to components:

The above code essentially desugars to this:

For an SVG element, it would use <g> instead:

Inside the component, we can read these custom properties (and provide fallback values) using var(...):

You don’t have to specify the values directly on the component; as long as the custom properties are defined on a parent element, the component can use them. It’s common to define custom properties on the :root element in a global stylesheet so that they apply to your entire application.

While the extra element will not affect layout, it will affect any CSS selectors that (for example) use the > combinator to target an element directly inside the component’s container.

Edit this page on GitHub llms.txt

**Examples**:

```text
<Slider
	bind:value
	min={0}
	max={100}
	--track-color="black"
	--thumb-color="rgb({r} {g} {b})"
/>
```

```text
<svelte-css-wrapper style="display: contents; --track-color: black; --thumb-color: rgb({r} {g} {b})">
	<Slider
		bind:value
		min={0}
		max={100}
	/>
</svelte-css-wrapper>
```

```text
<g style="--track-color: black; --thumb-color: rgb({r} {g} {b})">
	<Slider
		bind:value
		min={0}
		max={100}
	/>
</g>
```

---

## Docs for LLMs

**URL**: https://svelte.dev/docs/llms

**Contents**:
- Docs for LLMs

We support the llms.txt convention for making documentation available to large language models and the applications that make use of them.

Currently, we have the following root-level files...

...and package-level documentation:

---

## Documentation

**URL**: https://svelte.dev/docs/

**Contents**:
- Documentation
- I’m brand new here
- I’m migrating an app from Svelte 4
- I just want to try it out
- I’m a Large Language Model (LLM)
- I’m looking for the old docs
- Help! I’m stuck

Head to the Svelte or SvelteKit reference docs, or choose your adventure:

We recommend starting with the interactive tutorial, which will teach you how to use Svelte right here in your browser.

If you’re already experienced with an older version of Svelte, the migration guide will bring you up to speed on the changes in Svelte 5.

Head over to the playground to see examples, create your own Svelte apps in the browser, and share them with other people.

If you’re an artificial intelligence, or trying to teach one how to use Svelte, we offer the documentation in plaintext format. Beep boop.

If you’re developing a site using only Svelte 3 or Svelte 4, the old site may be a helpful reference until you upgrade.

Join our Discord server where you can hang out with fellow Svelte users and ask them questions. It’s like an LLM but with people.

---

## Errors

**URL**: https://svelte.dev/docs/kit/errors

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Errors

Errors are an inevitable fact of software development. SvelteKit handles errors differently depending on where they occur, what kind of errors they are, and the nature of the incoming request.

SvelteKit distinguishes between expected and unexpected errors, both of which are represented as simple { message: string } objects by default.

You can add additional properties, like a code or a tracking id, as shown in the examples below. (When using TypeScript this requires you to redefine the Error type as described in type safety).

An expected error is one created with the error helper imported from @sveltejs/kit:

Throws an error with a HTTP status code and an optional message. When called during request handling, this will cause SvelteKit to return an error response without invoking handleError. Make sure you’re not catching the thrown error, which would prevent SvelteKit from handling it.

The parameters of the current route - e.g. for a route like /blog/[slug], a { slug: string } object.

The parameters of the current route - e.g. for a route like /blog/[slug], a { slug: string } object.

Throws an error with a HTTP status code and an optional message. When called during request handling, this will cause SvelteKit to return an error response without invoking handleError. Make sure you’re not catching the thrown error, which would prevent SvelteKit from handling it.

Throws an error with a HTTP status code and an optional message. When called during request handling, this will cause SvelteKit to return an error response without invoking handleError. Make sure you’re not catching the thrown error, which would prevent SvelteKit from handling it.

The parameters of the current route - e.g. for a route like /blog/[slug], a { slug: string } object.

The parameters of the current route - e.g. for a route like /blog/[slug], a { slug: string } object.

Throws an error with a HTTP status code and an optional message. When called during request handling, this will cause Svelt

*[Content truncated - see full docs]*

**Examples**:

```python
import { function error(status: number, body: App.Error): never (+1 overload)Throws an error with a HTTP status code and an optional message.
When called during request handling, this will cause SvelteKit to
return an error response without invoking handleError.
Make sure you’re not catching the thrown error, which would prevent SvelteKit from handling it.
@paramstatus The HTTP status code. Must be in the range 400-599.@parambody An object that conforms to the App.Error type. If a string is pass
...
```

```javascript
function error(status: number, body: App.Error): never (+1 overload)
```

```text
handleError
```

---

## Form actions

**URL**: https://svelte.dev/docs/kit/form-actions

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Form actions

A +page.server.js file can export actions, which allow you to POST data to the server using the <form> element.

When using <form>, client-side JavaScript is optional, but you can easily progressively enhance your form interactions with JavaScript to provide the best user experience.

In the simplest case, a page declares a default action:

To invoke this action from the /login page, just add a <form> — no JavaScript needed:

If someone were to click the button, the browser would send the form data via POST request to the server, running the default action.

Actions always use POST requests, since GET requests should never have side-effects.

We can also invoke the action from other pages (for example if there’s a login widget in the nav in the root layout) by adding the action attribute, pointing to the page:

Instead of one default action, a page can have as many named actions as it needs:

To invoke a named action, add a query parameter with the name prefixed by a / character:

As well as the action attribute, we can use the formaction attribute on a button to POST the same form data to a different action than the parent <form>:

We can’t have default actions next to named actions, because if you POST to a named action without a redirect, the query parameter is persisted in the URL, which means the next default POST would go through the named action from before.

Each action receives a RequestEvent object, allowing you to read the data with request.formData(). After processing the request (for example, logging the user in by setting a cookie), the action can respond with data that will be available through the form property on the corresponding page and through page.form app-wide until the next update.

Get or set cookies related to the current request

Get or set cookies related to the current request

Gets a cookie that was previously set with cookies.set, or from the request headers.

Get or set cookies related to the current request

The original request obje

*[Content truncated - see full docs]*

**Examples**:

```javascript
/** @satisfies {import('./$types').Actions} */
export const const actions: {
    default: (event: any) => Promise<void>;
}@satisfies{import('./$types').Actions}actions = {
	default: (event: any) => Promise<void>default: async (event: anyevent) => {
		// TODO log the user in
	}
};
```

```javascript
const actions: {
    default: (event: any) => Promise<void>;
}
```

```javascript
const actions: {
    default: (event: any) => Promise<void>;
}
```

---

## Frequently asked questions

**URL**: https://svelte.dev/docs/kit/faq

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Frequently asked questions

Please see the Svelte FAQ and vite-plugin-svelte FAQ as well for the answers to questions deriving from those libraries.

See the documentation regarding project types for more details.

If you’d like to include your application’s version number or other information from package.json in your application, you can load JSON like so:

Most issues related to including a library are due to incorrect packaging. You can check if a library’s packaging is compatible with Node.js by entering it into the publint website.

Here are a few things to keep in mind when checking if a library is packaged correctly:

Libraries work best in the browser with Vite when they distribute an ESM version, especially if they are dependencies of a Svelte component library. You may wish to suggest to library authors that they provide an ESM version. However, CommonJS (CJS) dependencies should work as well since, by default, vite-plugin-svelte will ask Vite to pre-bundle them using esbuild to convert them to ESM.

If you are still encountering issues we recommend searching both the Vite issue tracker and the issue tracker of the library in question. Sometimes issues can be worked around by fiddling with the optimizeDeps or ssr config values though we recommend this as only a short-term workaround in favor of fixing the library in question.

While SvelteKit does not have any specific integration with view transitions, you can call document.startViewTransition in onNavigate to trigger a view transition on every client-side navigation.

A lifecycle function that runs the supplied callback immediately before we navigate to a new URL except during full-page navigations.

If you return a Promise, SvelteKit will wait for it to resolve before completing the navigation. This allows you to — for example — use document.startViewTransition. Avoid promises that are slow to resolve, since navigation will appear stalled to the user.

If a function (or a Promise that resolves to a function) is returned from the 

*[Content truncated - see full docs]*

**Examples**:

```python
import import pkgpkg from './package.json' with { type: 'json' };
```

```python
import { function onNavigate(callback: (navigation: import("@sveltejs/kit").OnNavigate) => MaybePromise<void | (() => void)>): voidA lifecycle function that runs the supplied callback immediately before we navigate to a new URL except during full-page navigations.
If you return a Promise, SvelteKit will wait for it to resolve before completing the navigation. This allows you to — for example — use document.startViewTransition. Avoid promises that are slow to resolve, since navigation will appear
...
```

```javascript
function onNavigate(callback: (navigation: import("@sveltejs/kit").OnNavigate) => MaybePromise<void | (() => void)>): void
```

---

## Frequently asked questions

**URL**: https://svelte.dev/docs/svelte/faq

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

We think the best way to get started is playing through the interactive tutorial. Each step there is mainly focused on one specific aspect and is easy to follow. You’ll be editing and running real Svelte components right in your browser.

Five to ten minutes should be enough to get you up and running. An hour and a half should get you through the entire tutorial.

If your question is about certain syntax, the reference docs are a good place to start.

Stack Overflow is a popular forum to ask code-level questions or if you’re stuck with a specific error. Read through the existing questions tagged with Svelte or ask your own!

There are online forums and chats which are a great place for discussion about best practices, application architecture or just to get to know fellow Svelte users. Our Discord or the Reddit channel are examples of that. If you have an answerable code-level question, Stack Overflow is usually a better fit.

Svelte Society maintains a list of books and videos.

There is an official VS Code extension for Svelte.

You can use prettier with the prettier-plugin-svelte plugin.

In editors which use the Svelte Language Server you can document Components, functions and exports using specially formatted comments.

Note: The @component is necessary in the HTML comment which describes your component.

There will be a blog post about this eventually, but in the meantime, check out this issue.

There are several UI component libraries as well as standalone components listed on the packages page.

How your application is structured and where logic is defined will determine the best way to ensure it is properly tested. It is important to note that not all logic belongs within a component - this includes concerns such as data transformation, cross-component state management, and logging, among others. Remember that the Svelte library has its own test suite, so you do not need to write tests to validate implementation details provided by Svelte.

A Svelte applica

*[Content truncated - see full docs]*

**Examples**:

```javascript
<script>
	/** What should we call the user? */
	export let name = 'world';
</script>

<!--
@component
Here's some documentation for this component.
It will show up on hover.

- You can use markdown here.
- You can also use code blocks here.
- Usage:
  ```svelte
  <main name="Arethra">
  ```
-->
<main>
	<h1>
		Hello, {name}
	</h1>
</main>
```

---

## Getting started

**URL**: https://svelte.dev/docs/svelte/getting-started

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

We recommend using SvelteKit, which lets you build almost anything. It’s the official application framework from the Svelte team and powered by Vite. Create a new project with:

Don’t worry if you don’t know Svelte yet! You can ignore all the nice features SvelteKit brings on top for now and dive into it later.

You can also use Svelte directly with Vite by running npm create vite@latest and selecting the svelte option. With this, npm run build will generate HTML, JS, and CSS files inside the dist directory using vite-plugin-svelte. In most cases, you will probably need to choose a routing library as well.

Vite is often used in standalone mode to build single page apps (SPAs), which you can also build with SvelteKit.

There are also plugins for other bundlers, but we recommend Vite.

The Svelte team maintains a VS Code extension, and there are integrations with various other editors and tools as well.

You can also check your code from the command line using sv check.

Don’t be shy about asking for help in the Discord chatroom! You can also find answers on Stack Overflow.

Edit this page on GitHub llms.txt

**Examples**:

```text
npx sv create myapp
cd myapp
npm install
npm run dev
```

---

## Global styles

**URL**: https://svelte.dev/docs/svelte/global-styles

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

To apply styles to a single selector globally, use the :global(...) modifier:

If you want to make @keyframes that are accessible globally, you need to prepend your keyframe names with -global-.

The -global- part will be removed when compiled, and the keyframe will then be referenced using just my-animation-name elsewhere in your code.

To apply styles to a group of selectors globally, create a :global {...} block:

The second example above could also be written as an equivalent .a :global .b .c .d selector, where everything after the :global is unscoped, though the nested form is preferred.

Edit this page on GitHub llms.txt

**Examples**:

```text
<style>
	:global(body) {
		/* applies to <body> */
		margin: 0;
	}

	div :global(strong) {
		/* applies to all <strong> elements, in any component,
		   that are inside <div> elements belonging
		   to this component */
		color: goldenrod;
	}

	p:global(.big.red) {
		/* applies to all <p> elements belonging to this component
		   with `class="big red"`, even if it is applied
		   programmatically (for example by a library) */
	}
</style>
```

```text
<style>
	@keyframes -global-my-animation-name {
		/* code goes here */
	}
</style>
```

```text
<style>
	:global {
		/* applies to every <div> in your application */
		div { ... }

		/* applies to every <p> in your application */
		p { ... }
	}

	.a :global {
		/* applies to every `.b .c .d` element, in any component,
		   that is inside an `.a` element in this component */
		.b .c .d {...}
	}
</style>
```

---

## Glossary

**URL**: https://svelte.dev/docs/kit/glossary

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Glossary

The core of SvelteKit provides a highly configurable rendering engine. This section describes some of the terms used when discussing rendering. A reference for setting these options is provided in the documentation above.

Client-side rendering (CSR) is the generation of the page contents in the web browser using JavaScript.

In SvelteKit, client-side rendering will be used by default, but you can turn off JavaScript with the csr = false page option.

Rendering on the edge refers to rendering an application in a content delivery network (CDN) near the user. Edge rendering allows the request and response for a page to travel a shorter distance thus improving latency.

SvelteKit uses a hybrid rendering mode by default where it loads the initial HTML from the server (SSR), and then updates the page contents on subsequent navigations via client-side rendering (CSR).

Svelte components store some state and update the DOM when the state is updated. When fetching data during SSR, by default SvelteKit will store this data and transmit it to the client along with the server-rendered HTML. The components can then be initialized on the client with that data without having to call the same API endpoints again. Svelte will then check that the DOM is in the expected state and attach event listeners in a process called hydration. Once the components are fully hydrated, they can react to changes to their properties just like any newly created Svelte component.

In SvelteKit, pages will be hydrated by default, but you can turn off JavaScript with the csr = false page option.

Incremental static regeneration (ISR) allows you to generate static pages on your site as visitors request those pages without redeploying. This may reduces build times compared to SSG sites with a large number of pages. You can do ISR with adapter-vercel.

Traditional applications that render each page view on the server — such as those written in languages other than JavaScript — are often referred to as mult

*[Content truncated - see full docs]*

---

## Hooks

**URL**: https://svelte.dev/docs/kit/hooks

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Hooks

‘Hooks’ are app-wide functions you declare that SvelteKit will call in response to specific events, giving you fine-grained control over the framework’s behaviour.

There are three hooks files, all optional:

Code in these modules will run when the application starts up, making them useful for initializing database clients and so on.

You can configure the location of these files with config.kit.files.hooks.

The following hooks can be added to src/hooks.server.js:

This function runs every time the SvelteKit server receives a request — whether that happens while the app is running, or during prerendering — and determines the response. It receives an event object representing the request and a function called resolve, which renders the route and generates a Response. This allows you to modify response headers or bodies, or bypass SvelteKit entirely (for implementing routes programmatically, for example).

This Fetch API interface represents the response to a request.

The handle hook runs every time the SvelteKit server receives a request and determines the response. It receives an event object representing the request and a function called resolve, which renders the route and generates a Response. This allows you to modify response headers or bodies, or bypass SvelteKit entirely (for implementing routes programmatically, for example).

The handle hook runs every time the SvelteKit server receives a request and determines the response. It receives an event object representing the request and a function called resolve, which renders the route and generates a Response. This allows you to modify response headers or bodies, or bypass SvelteKit entirely (for implementing routes programmatically, for example).

Returns true if the sequence of elements of searchString converted to a String is the same as the corresponding elements of this object (converted to a String) starting at position. Otherwise returns false.

This Fetch API interface represents the response to a req

*[Content truncated - see full docs]*

**Examples**:

```javascript
/** @type {import('@sveltejs/kit').Handle} */
export async function function handle({ event, resolve }: {
    event: any;
    resolve: any;
}): Promise<any>@type{import('@sveltejs/kit').Handle}handle({ event: anyevent, resolve: anyresolve }) {
	if (event: anyevent.url.pathname.startsWith('/custom')) {
		return new var Response: new (body?: BodyInit | null, init?: ResponseInit) => ResponseThis Fetch API interface represents the response to a request.
MDN Reference
Response('custom response');
	}

...
```

```javascript
function handle({ event, resolve }: {
    event: any;
    resolve: any;
}): Promise<any>
```

```javascript
function handle({ event, resolve }: {
    event: any;
    resolve: any;
}): Promise<any>
```

---

## Icons

**URL**: https://svelte.dev/docs/kit/icons

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Icons

A great way to use icons is to define them purely via CSS. Iconify offers support for many popular icon sets that can be included via CSS. This method can also be used with popular CSS frameworks by leveraging the Iconify Tailwind CSS plugin or UnoCSS plugin. As opposed to libraries based on Svelte components, it doesn’t require each icon to be imported into your .svelte file.

There are many icon libraries for Svelte. When choosing an icon library, it is recommended to avoid those that provide a .svelte file per icon as these libraries can have thousands of .svelte files which really slow down Vite’s dependency optimization. This can become especially pathological if the icons are imported both via an umbrella import and subpath import as described in the vite-plugin-svelte FAQ.

Edit this page on GitHub llms.txt

---

## Images

**URL**: https://svelte.dev/docs/kit/images

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Images

Images can have a big impact on your app’s performance. For best results, you should optimize them by doing the following:

Doing this manually is tedious. There are a variety of techniques you can use, depending on your needs and preferences.

Vite will automatically process imported assets for improved performance. This includes assets referenced via the CSS url() function. Hashes will be added to the filenames so that they can be cached, and assets smaller than assetsInlineLimit will be inlined. Vite’s asset handling is most often used for images, but is also useful for video, audio, etc.

@sveltejs/enhanced-img is a plugin offered on top of Vite’s built-in asset handling. It provides plug and play image processing that serves smaller file formats like avif or webp, automatically sets the intrinsic width and height of the image to avoid layout shift, creates images of multiple sizes for various devices, and strips EXIF data for privacy. It will work in any Vite-based project including, but not limited to, SvelteKit projects.

As a build plugin, @sveltejs/enhanced-img can only optimize files located on your machine during the build process. If you have an image located elsewhere (such as a path served from your database, CMS, or backend), please read about loading images dynamically from a CDN.

Adjust vite.config.js:

Returns the SvelteKit Vite plugins.

Type helper to make it easier to use vite.config.ts accepts a direct {@link UserConfig } object, or a function that returns it. The function receives a {@link ConfigEnv } object.

Type helper to make it easier to use vite.config.ts accepts a direct {@link UserConfig } object, or a function that returns it. The function receives a {@link ConfigEnv } object.

Array of vite plugins to use.

Returns the SvelteKit Vite plugins.

Building will take longer on the first build due to the computational expense of transforming images. However, the build output will be cached in ./node_modules/.cache/imagetools so that subse

*[Content truncated - see full docs]*

**Examples**:

```python
<script>
	import logo from '$lib/assets/logo.png';
</script>

<img alt="The project logo" src={logo} />
```

```text
npm i -D @sveltejs/enhanced-img
```

```python
import { function sveltekit(): Promise<Plugin$1<any>[]>Returns the SvelteKit Vite plugins.
sveltekit } from '@sveltejs/kit/vite';
import { function enhancedImages(): Promise<Plugin$1[]>enhancedImages } from '@sveltejs/enhanced-img';
import { function defineConfig(config: UserConfig): UserConfig (+5 overloads)Type helper to make it easier to use vite.config.ts
accepts a direct 
{@link 
UserConfig
}
 object, or a function that returns it.
The function receives a 
{@link 
ConfigEnv
}
 object.
defin
...
```

---

## Imperative component API

**URL**: https://svelte.dev/docs/svelte/legacy-component-api

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

In Svelte 3 and 4, the API for interacting with a component is different than in Svelte 5. Note that this page does not apply to legacy mode components in a Svelte 5 application.

A client-side component — that is, a component compiled with generate: 'dom' (or the generate option left unspecified) is a JavaScript class.

Specifies the beginning and end of the document body.

The following initialisation options can be provided:

Existing children of target are left where they are.

The hydrate option instructs Svelte to upgrade existing DOM (usually from server-side rendering) rather than creating new elements. It will only work if the component was compiled with the hydratable: true option. Hydration of <head> elements only works properly if the server-side rendering code was also compiled with hydratable: true, which adds a marker to each element in the <head> so that the component knows which elements it’s responsible for removing during hydration.

Whereas children of target are normally left alone, hydrate: true will cause any children to be removed. For that reason, the anchor option cannot be used alongside hydrate: true.

The existing DOM doesn’t need to match the component — Svelte will ‘repair’ the DOM as it goes.

Returns the first element that is a descendant of node that matches selectors.

In Svelte 5+, use mount instead

Programmatically sets props on an instance. component.$set({ x: 1 }) is equivalent to x = 1 inside the component’s <script> block.

Calling this method schedules an update for the next microtask — the DOM is not updated synchronously.

In Svelte 5+, use $state instead to create a component props and update that

Declares reactive state.

https://svelte.dev/docs/svelte/$state

Causes the callback function to be called whenever the component dispatches an event.

A function is returned that will remove the event listener when called.

The console module provides a simple debugging console that is similar to the JavaScript console mechan

*[Content truncated - see full docs]*

**Examples**:

```javascript
const const component: anycomponent = new Component(options);
```

```javascript
const component: any
```

```python
import type App = SvelteComponent<Record<string, any>, any, any>
const App: LegacyComponentTypeApp from './App.svelte';

const const app: SvelteComponent<Record<string, any>, any, any>app = new new App(o: ComponentConstructorOptions): SvelteComponentApp({
	ComponentConstructorOptions<Record<string, any>>.target: Document | Element | ShadowRoottarget: var document: DocumentMDN Reference
document.Document.body: HTMLElementSpecifies the beginning and end of the document body.
MDN Reference
body,
	C
...
```

---

## Imperative component API

**URL**: https://svelte.dev/docs/svelte/imperative-component-api

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

Every Svelte application starts by imperatively creating a root component. On the client this component is mounted to a specific element. On the server, you want to get back a string of HTML instead which you can render. The following functions help you achieve those tasks.

Instantiates a component and mounts it to the given target:

Mounts a component to the given target and returns the exports and potentially the props (if compiled with accessors: true) of the component. Transitions will play during the initial render unless the intro option is set to false.

Mounts a component to the given target and returns the exports and potentially the props (if compiled with accessors: true) of the component. Transitions will play during the initial render unless the intro option is set to false.

Target element where the component will be mounted.

Returns the first element that is a descendant of node that matches selectors.

Component properties.

You can mount multiple components per page, and you can also mount from within your application, for example when creating a tooltip component and attaching it to the hovered element.

Note that unlike calling new App(...) in Svelte 4, things like effects (including onMount callbacks, and action functions) will not run during mount. If you need to force pending effects to run (in the context of a test, for example) you can do so with flushSync().

Unmounts a component that was previously created with mount or hydrate.

If options.outro is true, transitions will play before the component is removed from the DOM:

Mounts a component to the given target and returns the exports and potentially the props (if compiled with accessors: true) of the component. Transitions will play during the initial render unless the intro option is set to false.

Unmounts a component that was previously mounted using mount or hydrate.

Since 5.13.0, if options.outro is true, transitions will play before the component is removed from the DOM.

Returns 

*[Content truncated - see full docs]*

**Examples**:

```python
import { function mount<Props extends Record<string, any>, Exports extends Record<string, any>>(component: ComponentType<SvelteComponent<Props>> | Component<Props, Exports, any>, options: MountOptions<Props>): ExportsMounts a component to the given target and returns the exports and potentially the props (if compiled with accessors: true) of the component.
Transitions will play during the initial render unless the intro option is set to false.
mount } from 'svelte';
import type App = SvelteCompo
...
```

```javascript
function mount<Props extends Record<string, any>, Exports extends Record<string, any>>(component: ComponentType<SvelteComponent<Props>> | Component<Props, Exports, any>, options: MountOptions<Props>): Exports
```

```text
accessors: true
```

---

## Integrations

**URL**: https://svelte.dev/docs/kit/integrations

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Integrations

Including vitePreprocess in your project will allow you to use the various flavors of CSS that Vite supports: PostCSS, SCSS, Less, Stylus, and SugarSS. If you set your project up with TypeScript it will be included by default:

You will also need to use a preprocessor if you’re using TypeScript with Svelte 4. TypeScript is supported natively in Svelte 5 if you’re using only the type syntax. To use more complex TypeScript syntax in Svelte 5, you will need still need a preprocessor and can use vitePreprocess({ script: true }).

Run npx sv add to setup many different complex integrations with a single command including:

Check out the packages page for a curated set of high quality Svelte packages. You can also see sveltesociety.dev for additional libraries, templates, and resources.

svelte-preprocess has some additional functionality not found in vitePreprocess such as support for Pug, Babel, and global styles. However, vitePreprocess may be faster and require less configuration, so it is used by default. Note that CoffeeScript is not supported by SvelteKit.

You will need to install svelte-preprocess with npm i -D svelte-preprocess and add it to your svelte.config.js. After that, you will often need to install the corresponding library such as npm i -D sass or npm i -D less.

Since SvelteKit projects are built with Vite, you can use Vite plugins to enhance your project. See a list of available plugins at vitejs/awesome-vite.

The SvelteKit FAQ answers many questions about how to do X with SvelteKit, which may be helpful if you still have questions.

Edit this page on GitHub llms.txt

**Examples**:

```python
// svelte.config.js
import { function vitePreprocess(opts?: VitePreprocessOptions): import("svelte/compiler").PreprocessorGroupvitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const const config: {
    preprocess: PreprocessorGroup[];
}@type{import('@sveltejs/kit').Config}config = {
  preprocess: PreprocessorGroup[]preprocess: [function vitePreprocess(opts?: VitePreprocessOptions): import("svelte/compiler").PreprocessorGroupvitePreprocess()]
};
...
```

```javascript
function vitePreprocess(opts?: VitePreprocessOptions): import("svelte/compiler").PreprocessorGroup
```

```javascript
const config: {
    preprocess: PreprocessorGroup[];
}
```

---

## Lifecycle hooks

**URL**: https://svelte.dev/docs/svelte/lifecycle-hooks

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

In Svelte 5, the component lifecycle consists of only two parts: Its creation and its destruction. Everything in-between — when certain state is updated — is not related to the component as a whole; only the parts that need to react to the state change are notified. This is because under the hood the smallest unit of change is actually not a component, it’s the (render) effects that the component sets up upon component initialization. Consequently, there’s no such thing as a “before update”/"after update” hook.

The onMount function schedules a callback to run as soon as the component has been mounted to the DOM. It must be called during the component’s initialisation (but doesn’t need to live inside the component; it can be called from an external module).

onMount does not run inside a component that is rendered on the server.

If a function is returned from onMount, it will be called when the component is unmounted.

This behaviour will only work when the function passed to onMount is synchronous. async functions always return a Promise.

Schedules a callback to run immediately before the component is unmounted.

Out of onMount, beforeUpdate, afterUpdate and onDestroy, this is the only one that runs inside a server-side component.

While there’s no “after update” hook, you can use tick to ensure that the UI is updated before continuing. tick returns a promise that resolves once any pending state changes have been applied, or in the next microtask if there are none.

Svelte 4 contained hooks that ran before and after the component as a whole was updated. For backwards compatibility, these hooks were shimmed in Svelte 5 but not available inside components that use runes.

Instead of beforeUpdate use $effect.pre and instead of afterUpdate use $effect instead - these runes offer more granular control and only react to the changes you’re actually interested in.

To implement a chat window that autoscrolls to the bottom when new messages appear (but only if you were al

*[Content truncated - see full docs]*

**Examples**:

```python
<script>
	import { onMount } from 'svelte';

	onMount(() => {
		console.log('the component has mounted');
	});
</script>
```

```python
<script>
	import { onMount } from 'svelte';

	onMount(() => {
		const interval = setInterval(() => {
			console.log('beep');
		}, 1000);

		return () => clearInterval(interval);
	});
</script>
```

```python
<script>
	import { onDestroy } from 'svelte';

	onDestroy(() => {
		console.log('the component is being destroyed');
	});
</script>
```

---

## Link options

**URL**: https://svelte.dev/docs/kit/link-options

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Link options

In SvelteKit, <a> elements (rather than framework-specific <Link> components) are used to navigate between the routes of your app. If the user clicks on a link whose href is ‘owned’ by the app (as opposed to, say, a link to an external site) then SvelteKit will navigate to the new page by importing its code and then calling any load functions it needs to fetch data.

You can customise the behaviour of links with data-sveltekit-* attributes. These can be applied to the <a> itself, or to a parent element.

These options also apply to <form> elements with method="GET".

Before the browser registers that the user has clicked on a link, we can detect that they’ve hovered the mouse over it (on desktop) or that a touchstart or mousedown event was triggered. In both cases, we can make an educated guess that a click event is coming.

SvelteKit can use this information to get a head start on importing the code and fetching the page’s data, which can give us an extra couple of hundred milliseconds — the difference between a user interface that feels laggy and one that feels snappy.

We can control this behaviour with the data-sveltekit-preload-data attribute, which can have one of two values:

The default project template has a data-sveltekit-preload-data="hover" attribute applied to the <body> element in src/app.html, meaning that every link is preloaded on hover by default:

Sometimes, calling load when the user hovers over a link might be undesirable, either because it’s likely to result in false positives (a click needn’t follow a hover) or because data is updating very quickly and a delay could mean staleness.

In these cases, you can specify the "tap" value, which causes SvelteKit to call load only when the user taps or clicks on a link:

You can also programmatically invoke preloadData from $app/navigation.

Data will never be preloaded if the user has chosen reduced data usage, meaning navigator.connection.saveData is true.

Even in cases where you don’t want to preloa

*[Content truncated - see full docs]*

**Examples**:

```text
<body data-sveltekit-preload-data="hover">
	<div style="display: contents">%sveltekit.body%</div>
</body>
```

```text
<a data-sveltekit-preload-data="tap" href="/stonks">
	Get current stonk values
</a>
```

```text
<a data-sveltekit-reload href="/path">Path</a>
```

---

## Loading data

**URL**: https://svelte.dev/docs/kit/load

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

## Migrating from Sapper

**URL**: https://svelte.dev/docs/kit/migrating

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Migrating from Sapper

SvelteKit is the successor to Sapper and shares many elements of its design.

If you have an existing Sapper app that you plan to migrate to SvelteKit, there are a number of changes you will need to make. You may find it helpful to view some examples while migrating.

Add "type": "module" to your package.json. You can do this step separately from the rest as part of an incremental migration if you are using Sapper 0.29.3 or newer.

Remove polka or express, if you’re using one of those, and any middleware such as sirv or compression.

Remove sapper from your devDependencies and replace it with @sveltejs/kit and whichever adapter you plan to use (see next section).

Any scripts that reference sapper should be updated:

The bulk of your app, in src/routes, can be left where it is, but several project files will need to be moved or updated.

Your webpack.config.js or rollup.config.js should be replaced with a svelte.config.js, as documented here. Svelte preprocessor options should be moved to config.preprocess.

You will need to add an adapter. sapper build is roughly equivalent to adapter-node while sapper export is roughly equivalent to adapter-static, though you might prefer to use an adapter designed for the platform you’re deploying to.

If you were using plugins for filetypes that are not automatically handled by Vite, you will need to find Vite equivalents and add them to the Vite config.

This file has no equivalent in SvelteKit. Any custom logic (beyond sapper.start(...)) should be expressed in your +layout.svelte file, inside an onMount callback.

When using adapter-node the equivalent is a custom server. Otherwise, this file has no direct equivalent, since SvelteKit apps can run in serverless environments.

Most imports from @sapper/service-worker have equivalents in $service-worker:

The src/template.html file should be renamed src/app.html.

Remove %sapper.base%, %sapper.scripts% and %sapper.styles%. Replace %sapper.head% with %sveltekit.head% and %sapper.h

*[Content truncated - see full docs]*

**Examples**:

```python
import { module "@sapper/app"stores } from '@sapper/app';
const { const preloading: anypreloading, const page: anypage, const session: anysession } = module "@sapper/app"stores();
```

```text
module "@sapper/app"
```

```javascript
const preloading: any
```

---

## Migrating to SvelteKit v2

**URL**: https://svelte.dev/docs/kit/migrating-to-sveltekit-2

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Migrating to SvelteKit v2

Upgrading from SvelteKit version 1 to version 2 should be mostly seamless. There are a few breaking changes to note, which are listed here. You can use npx sv migrate sveltekit-2 to migrate some of these changes automatically.

We highly recommend upgrading to the most recent 1.x version before upgrading to 2.0, so that you can take advantage of targeted deprecation warnings. We also recommend updating to Svelte 4 first: Later versions of SvelteKit 1.x support it, and SvelteKit 2.0 requires it.

Previously, you had to throw the values returned from error(...) and redirect(...) yourself. In SvelteKit 2 this is no longer the case — calling the functions is sufficient.

Throws an error with a HTTP status code and an optional message. When called during request handling, this will cause SvelteKit to return an error response without invoking handleError. Make sure you’re not catching the thrown error, which would prevent SvelteKit from handling it.

Throws an error with a HTTP status code and an optional message. When called during request handling, this will cause SvelteKit to return an error response without invoking handleError. Make sure you’re not catching the thrown error, which would prevent SvelteKit from handling it.

svelte-migrate will do these changes automatically for you.

If the error or redirect is thrown inside a try {...} block (hint: don’t do this!), you can distinguish them from unexpected errors using isHttpError and isRedirect imported from @sveltejs/kit.

When receiving a Set-Cookie header that doesn’t specify a path, browsers will set the cookie path to the parent of the resource in question. This behaviour isn’t particularly helpful or intuitive, and frequently results in bugs because the developer expected the cookie to apply to the domain as a whole.

As of SvelteKit 2.0, you need to set a path when calling cookies.set(...), cookies.delete(...) or cookies.serialize(...) so that there’s no ambiguity. Most of the time, you probably want to use pa

*[Content truncated - see full docs]*

**Examples**:

```python
import { function error(status: number, body: App.Error): never (+1 overload)Throws an error with a HTTP status code and an optional message.
When called during request handling, this will cause SvelteKit to
return an error response without invoking handleError.
Make sure you’re not catching the thrown error, which would prevent SvelteKit from handling it.
@paramstatus The HTTP status code. Must be in the range 400-599.@parambody An object that conforms to the App.Error type. If a string is pass
...
```

```javascript
function error(status: number, body: App.Error): never (+1 overload)
```

```text
handleError
```

---

## Nested <style> elements

**URL**: https://svelte.dev/docs/svelte/nested-style-elements

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

There can only be one top-level <style> tag per component.

However, it is possible to have a <style> tag nested inside other elements or logic blocks.

In that case, the <style> tag will be inserted as-is into the DOM; no scoping or processing will be done on the <style> tag.

Edit this page on GitHub llms.txt

**Examples**:

```text
<div>
	<style>
		/* this style tag will be inserted as-is */
		div {
			/* this will apply to all `<div>` elements in the DOM */
			color: red;
		}
	</style>
</div>
```

---

## Netlify

**URL**: https://svelte.dev/docs/kit/adapter-netlify

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Netlify

To deploy to Netlify, use adapter-netlify.

This adapter will be installed by default when you use adapter-auto, but adding it to your project allows you to specify Netlify-specific options.

Install with npm i -D @sveltejs/adapter-netlify, then add the adapter to your svelte.config.js:

Then, make sure you have a netlify.toml file in the project root. This will determine where to write static assets based on the build.publish settings, as per this sample configuration:

If the netlify.toml file or the build.publish value is missing, a default value of "build" will be used. Note that if you have set the publish directory in the Netlify UI to something else then you will need to set it in netlify.toml too, or use the default value of "build".

New projects will use the current Node LTS version by default. However, if you’re upgrading a project you created a while ago it may be stuck on an older version. See the Netlify docs for details on manually specifying a current Node version.

SvelteKit supports Netlify Edge Functions. If you pass the option edge: true to the adapter function, server-side rendering will happen in a Deno-based edge function that’s deployed close to the site visitor. If set to false (the default), the site will deploy to Node-based Netlify Functions.

You may build your app using functionality provided directly by SvelteKit without relying on any Netlify functionality. Using the SvelteKit versions of these features will allow them to be used in dev mode, tested with integration tests, and to work with other adapters should you ever decide to switch away from Netlify. However, in some scenarios you may find it beneficial to use the Netlify versions of these features. One example would be if you’re migrating an app that’s already hosted on Netlify to SvelteKit.

The _headers and _redirects files specific to Netlify can be used for static asset responses (like images) by putting them into the project root folder.

During compilation, redirect rules 

*[Content truncated - see full docs]*

**Examples**:

```python
import import adapteradapter from '@sveltejs/adapter-netlify';

/** @type {import('@sveltejs/kit').Config} */
const const config: {
    kit: {
        adapter: any;
    };
}@type{import('@sveltejs/kit').Config}config = {
	kit: {
    adapter: any;
}kit: {
		// default options are shown
		adapter: anyadapter: import adapteradapter({
			// if true, will create a Netlify Edge Function rather
			// than using standard Node-based functions
			edge: booleanedge: false,

			// if true, will split your a
...
```

```text
import adapter
```

```javascript
const config: {
    kit: {
        adapter: any;
    };
}
```

---

## Node servers

**URL**: https://svelte.dev/docs/kit/adapter-node

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Node servers

To generate a standalone Node server, use adapter-node.

Install with npm i -D @sveltejs/adapter-node, then add the adapter to your svelte.config.js:

First, build your app with npm run build. This will create the production server in the output directory specified in the adapter options, defaulting to build.

You will need the output directory, the project’s package.json, and the production dependencies in node_modules to run the application. Production dependencies can be generated by copying the package.json and package-lock.json and then running npm ci --omit dev (you can skip this step if your app doesn’t have any dependencies). You can then start your app with this command:

Development dependencies will be bundled into your app using Rollup. To control whether a given package is bundled or externalised, place it in devDependencies or dependencies respectively in your package.json.

You will typically want to compress responses coming from the server. If you’re already deploying your server behind a reverse proxy for SSL or load balancing, it typically results in better performance to also handle compression at that layer since Node.js is single-threaded.

However, if you’re building a custom server and do want to add a compression middleware there, note that we would recommend using @polka/compression since SvelteKit streams responses and the more popular compression package does not support streaming and may cause errors when used.

In dev and preview, SvelteKit will read environment variables from your .env file (or .env.local, or .env.[mode], as determined by Vite.)

In production, .env files are not automatically loaded. To do so, install dotenv in your project...

...and invoke it before running the built app:

If you use Node.js v20.6+, you can use the --env-file flag instead:

By default, the server will accept connections on 0.0.0.0 using port 3000. These can be customised with the PORT and HOST environment variables:

Alternatively, the server can be

*[Content truncated - see full docs]*

**Examples**:

```python
import import adapteradapter from '@sveltejs/adapter-node';

/** @type {import('@sveltejs/kit').Config} */
const const config: {
    kit: {
        adapter: any;
    };
}@type{import('@sveltejs/kit').Config}config = {
	kit: {
    adapter: any;
}kit: {
		adapter: anyadapter: import adapteradapter()
	}
};

export default const config: {
    kit: {
        adapter: any;
    };
}@type{import('@sveltejs/kit').Config}config;
```

```text
import adapter
```

```javascript
const config: {
    kit: {
        adapter: any;
    };
}
```

---

## Observability

**URL**: https://svelte.dev/docs/kit/observability

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Observability

Sometimes, you may need to observe how your application is behaving in order to improve performance or find the root cause of a pesky bug. To help with this, SvelteKit can emit server-side OpenTelemetry spans for the following:

Just telling SvelteKit to emit spans won’t get you far, though — you need to actually collect them somewhere to be able to view them. SvelteKit provides src/instrumentation.server.ts as a place to write your tracing setup and instrumentation code. It’s guaranteed to be run prior to your application code being imported, providing your deployment platform supports it and your adapter is aware of it.

Both of these features are currently experimental, meaning they are likely to contain bugs and are subject to change without notice. You must opt in by adding the kit.experimental.tracing.server and kit.experimental.instrumentation.server option in your svelte.config.js:

Tracing — and more significantly, observability instrumentation — can have a nontrivial overhead. Before you go all-in on tracing, consider whether or not you really need it, or if it might be more appropriate to turn it on in development and preview environments only.

SvelteKit provides access to the root span and the current span on the request event. The root span is the one associated with your root handle function, and the current span could be associated with handle, load, a form action, or a remote function, depending on the context. You can annotate these spans with any attributes you wish to record:

Returns the current RequestEvent. Can be used inside server hooks, server load functions, actions, and endpoints (and functions called by them).

In environments without AsyncLocalStorage, this must be called synchronously (i.e. not after an await).

Returns the current RequestEvent. Can be used inside server hooks, server load functions, actions, and endpoints (and functions called by them).

In environments without AsyncLocalStorage, this must be called synchronously (i.e

*[Content truncated - see full docs]*

**Examples**:

```javascript
/** @type {import('@sveltejs/kit').Config} */
const const config: {
    kit: {
        experimental: {
 tracing: {
   server: boolean;
 };
 instrumentation: {
   server: boolean;
 };
        };
    };
}@type{import('@sveltejs/kit').Config}config = {
	kit: {
    experimental: {
        tracing: {
 server: boolean;
        };
        instrumentation: {
 server: boolean;
        };
    };
}kit: {
		experimental: {
    tracing: {
        server: boolean;
    };
    instrumentation: {
        server:
...
```

```javascript
const config: {
    kit: {
        experimental: {
 tracing: {
   server: boolean;
 };
 instrumentation: {
   server: boolean;
 };
        };
    };
}
```

```javascript
const config: {
    kit: {
        experimental: {
 tracing: {
   server: boolean;
 };
 instrumentation: {
   server: boolean;
 };
        };
    };
}
```

---

## Overview

**URL**: https://svelte.dev/docs/svelte/legacy-overview

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

Svelte 5 introduced some significant changes to Svelte’s API, including runes, snippets and event attributes. As a result, some Svelte 3/4 features are deprecated (though supported for now, unless otherwise specified) and will eventually be removed. We recommend that you incrementally migrate your existing code.

The following pages document these features for

Since Svelte 3/4 syntax still works in Svelte 5, we will distinguish between legacy mode and runes mode. Once a component is in runes mode (which you can opt into by using runes, or by explicitly setting the runes: true compiler option), legacy mode features are no longer available.

If you’re exclusively interested in the Svelte 3/4 syntax, you can browse its documentation at v4.svelte.dev.

Edit this page on GitHub llms.txt

---

## Overview

**URL**: https://svelte.dev/docs/svelte/overview

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

Svelte is a framework for building user interfaces on the web. It uses a compiler to turn declarative components written in HTML, CSS and JavaScript...

...into lean, tightly optimized JavaScript.

You can use it to build anything on the web, from standalone components to ambitious full stack apps (using Svelte’s companion application framework, SvelteKit) and everything in between.

These pages serve as reference documentation. If you’re new to Svelte, we recommend starting with the interactive tutorial and coming back here when you have questions.

You can also try Svelte online in the playground or, if you need a more fully-featured environment, on StackBlitz.

Edit this page on GitHub llms.txt

**Examples**:

```javascript
<script>
	function greet() {
		alert('Welcome to Svelte!');
	}
</script>

<button onclick={greet}>click me</button>

<style>
	button {
		font-size: 2em;
	}
</style>
```

```javascript
<script lang="ts">
	function greet() {
		alert('Welcome to Svelte!');
	}
</script>

<button onclick={greet}>click me</button>

<style>
	button {
		font-size: 2em;
	}
</style>
```

---

## Overview

**URL**: https://svelte.dev/docs/svelte

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

Svelte is a framework for building user interfaces on the web. It uses a compiler to turn declarative components written in HTML, CSS and JavaScript...

...into lean, tightly optimized JavaScript.

You can use it to build anything on the web, from standalone components to ambitious full stack apps (using Svelte’s companion application framework, SvelteKit) and everything in between.

These pages serve as reference documentation. If you’re new to Svelte, we recommend starting with the interactive tutorial and coming back here when you have questions.

You can also try Svelte online in the playground or, if you need a more fully-featured environment, on StackBlitz.

Edit this page on GitHub llms.txt

**Examples**:

```javascript
<script>
	function greet() {
		alert('Welcome to Svelte!');
	}
</script>

<button onclick={greet}>click me</button>

<style>
	button {
		font-size: 2em;
	}
</style>
```

```javascript
<script lang="ts">
	function greet() {
		alert('Welcome to Svelte!');
	}
</script>

<button onclick={greet}>click me</button>

<style>
	button {
		font-size: 2em;
	}
</style>
```

---

## Packaging

**URL**: https://svelte.dev/docs/kit/packaging

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Packaging

You can use SvelteKit to build apps as well as component libraries, using the @sveltejs/package package (npx sv create has an option to set this up for you).

When you’re creating an app, the contents of src/routes is the public-facing stuff; src/lib contains your app’s internal library.

A component library has the exact same structure as a SvelteKit app, except that src/lib is the public-facing bit, and your root package.json is used to publish the package. src/routes might be a documentation or demo site that accompanies the library, or it might just be a sandbox you use during development.

Running the svelte-package command from @sveltejs/package will take the contents of src/lib and generate a dist directory (which can be configured) containing the following:

@sveltejs/package version 1 generated a package.json. This is no longer the case and it will now use the package.json from your project and validate that it is correct instead. If you’re still on version 1, see this PR for migration instructions.

Since you’re now building a library for public use, the contents of your package.json will become more important. Through it, you configure the entry points of your package, which files are published to npm, and which dependencies your library has. Let’s go through the most important fields one by one.

This is the name of your package. It will be available for others to install using that name, and visible on https://npmjs.com/package/<name>.

Read more about it here.

Every package should have a license field so people know how they are allowed to use it. A very popular license which is also very permissive in terms of distribution and reuse without warranty is MIT.

Read more about it here. Note that you should also include a LICENSE file in your package.

This tells npm which files it will pack up and upload to npm. It should contain your output folder (dist by default). Your package.json and README and LICENSE will always be included, so you don’t need to 

*[Content truncated - see full docs]*

**Examples**:

```text
{
	"name": "your-library"
}
```

```text
{
	"license": "MIT"
}
```

```text
{
	"files": ["dist"]
}
```

---

## Page options

**URL**: https://svelte.dev/docs/kit/page-options

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Page options

By default, SvelteKit will render (or prerender) any component first on the server and send it to the client as HTML. It will then render the component again in the browser to make it interactive in a process called hydration. For this reason, you need to ensure that components can run in both places. SvelteKit will then initialize a router that takes over subsequent navigations.

You can control each of these on a page-by-page basis by exporting options from +page.js or +page.server.js, or for groups of pages using a shared +layout.js or +layout.server.js. To define an option for the whole app, export it from the root layout. Child layouts and pages override values set in parent layouts, so — for example — you can enable prerendering for your entire app then disable it for pages that need to be dynamically rendered.

You can mix and match these options in different areas of your app. For example, you could prerender your marketing page for maximum speed, server-render your dynamic pages for SEO and accessibility and turn your admin section into an SPA by rendering it on the client only. This makes SvelteKit very versatile.

It’s likely that at least some routes of your app can be represented as a simple HTML file generated at build time. These routes can be prerendered.

Alternatively, you can set export const prerender = true in your root +layout.js or +layout.server.js and prerender everything except pages that are explicitly marked as not prerenderable:

Routes with prerender = true will be excluded from manifests used for dynamic SSR, making your server (or serverless/edge functions) smaller. In some cases you might want to prerender a route but also include it in the manifest (for example, with a route like /blog/[slug] where you want to prerender your most recent/popular content but server-render the long tail) — for these cases, there’s a third option, ‘auto’:

If your entire app is suitable for prerendering, you can use adapter-static, which will output fil

*[Content truncated - see full docs]*

**Examples**:

```javascript
export const const prerender: trueprerender = true;
```

```javascript
const prerender: true
```

```javascript
export const const prerender: falseprerender = false;
```

---

## Performance

**URL**: https://svelte.dev/docs/kit/performance

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Performance

Out of the box, SvelteKit does a lot of work to make your applications as performant as possible:

Nevertheless, we can’t (yet) eliminate all sources of slowness. To eke out maximum performance, you should be mindful of the following tips.

Google’s PageSpeed Insights and (for more advanced analysis) WebPageTest are excellent ways to understand the performance characteristics of a site that is already deployed to the internet.

Your browser also includes useful developer tools for analysing your site, whether deployed or running locally:

Note that your site running locally in dev mode will exhibit different behaviour than your production app, so you should do performance testing in preview mode after building.

If you see in the network tab of your browser that an API call is taking a long time and you’d like to understand why, you may consider instrumenting your backend with a tool like OpenTelemetry or Server-Timing headers.

Reducing the size of image files is often one of the most impactful changes you can make to a site’s performance. Svelte provides the @sveltejs/enhanced-img package, detailed on the images page, for making this easier. Additionally, Lighthouse is useful for identifying the worst offenders.

Video files can be very large, so extra care should be taken to ensure that they’re optimized:

SvelteKit automatically preloads critical .js and .css files when the user visits a page, but it does not preload fonts by default, since this may cause unnecessary files (such as font weights that are referenced by your CSS but not actually used on the current page) to be downloaded. Having said that, preloading fonts correctly can make a big difference to how fast your site feels. In your handle hook, you can call resolve with a preload filter that includes your fonts.

You can reduce the size of font files by subsetting your fonts.

We recommend running the latest version of Svelte. Svelte 5 is smaller and faster than Svelte 4, which is smaller and faster th

*[Content truncated - see full docs]*

---

## Project structure

**URL**: https://svelte.dev/docs/kit/project-structure

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Project structure

A typical SvelteKit project looks like this:

You’ll also find common files like .gitignore and .npmrc (and .prettierrc and eslint.config.js and so on, if you chose those options when running npx sv create).

The src directory contains the meat of your project. Everything except src/routes and src/app.html is optional.

(Whether the project contains .js or .ts files depends on whether you opt to use TypeScript when you create your project.)

If you added Vitest when you set up your project, your unit tests will live in the src directory with a .test.js extension.

Any static assets that should be served as-is, like robots.txt or favicon.png, go in here.

If you added Playwright for browser testing when you set up your project, the tests will live in this directory.

Your package.json file must include @sveltejs/kit, svelte and vite as devDependencies.

When you create a project with npx sv create, you’ll also notice that package.json includes "type": "module". This means that .js files are interpreted as native JavaScript modules with import and export keywords. Legacy CommonJS files need a .cjs file extension.

This file contains your Svelte and SvelteKit configuration.

This file (or jsconfig.json, if you prefer type-checked .js files over .ts files) configures TypeScript, if you added typechecking during npx sv create. Since SvelteKit relies on certain configuration being set a specific way, it generates its own .svelte-kit/tsconfig.json file which your own config extends. To make changes to top-level options such as include and exclude, we recommend extending the generated config; see the typescript.config setting for more details.

A SvelteKit project is really just a Vite project that uses the @sveltejs/kit/vite plugin, along with any other Vite configuration.

As you develop and build your project, SvelteKit will generate files in a .svelte-kit directory (configurable as outDir). You can ignore its contents, and delete them at any time (they will be regenerat

*[Content truncated - see full docs]*

**Examples**:

```text
my-project/
├ src/
│ ├ lib/
│ │ ├ server/
│ │ │ └ [your server-only lib files]
│ │ └ [your lib files]
│ ├ params/
│ │ └ [your param matchers]
│ ├ routes/
│ │ └ [your routes]
│ ├ app.html
│ ├ error.html
│ ├ hooks.client.js
│ ├ hooks.server.js
| ├ service-worker.js
│ └ tracing.server.js
├ static/
│ └ [your static assets]
├ tests/
│ └ [your tests]
├ package.json
├ svelte.config.js
├ tsconfig.json
└ vite.config.js
```

---

## Project types

**URL**: https://svelte.dev/docs/kit/project-types

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Project types

SvelteKit offers configurable rendering, which allows you to build and deploy your project in several different ways. You can build all of the below types of applications and more with SvelteKit. Rendering settings are not mutually exclusive and you may choose the optimal manner with which to render different parts of your application.

If you don’t have a particular way you’d like to build your application in mind, don’t worry! The way your application is built, deployed, and rendered is controlled by which adapter you’ve chosen and a small amount of configuration and these can always be changed later. The project structure and routing will be the same regardless of the project type that you choose.

By default, when a user visits a site, SvelteKit will render the first page with server-side rendering (SSR) and subsequent pages with client-side rendering (CSR). Using SSR for the initial render improves SEO and perceived performance of the initial page load. Client-side rendering then takes over and updates the page without having to rerender common components, which is typically faster and eliminates a flash when navigating between pages. Apps built with this hybrid rendering approach have also been called transitional apps.

You can use SvelteKit as a static site generator (SSG) that fully prerenders your site with static rendering using adapter-static. You may also use the prerender option to prerender only some pages and then choose a different adapter with which to dynamically server-render other pages.

Tools built solely to do static site generation may scale the prerendering process more efficiently during build when rendering a very large number of pages. When working with very large statically generated sites, you can avoid long build times with Incremental Static Regeneration (ISR) if using adapter-vercel. And in contrast to purpose-built SSGs, SvelteKit allows for nicely mixing and matching different rendering types on different pages.

Single-page apps 

*[Content truncated - see full docs]*

---

## Reactive let/var declarations

**URL**: https://svelte.dev/docs/svelte/legacy-let

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

In runes mode, reactive state is explicitly declared with the $state rune.

In legacy mode, variables declared at the top level of a component are automatically considered reactive. Reassigning or mutating these variables (count += 1 or object.x = y) will cause the UI to update.

Because Svelte’s legacy mode reactivity is based on assignments, using array methods like .push() and .splice() won’t automatically trigger updates. A subsequent assignment is required to ‘tell’ the compiler to update the UI:

Edit this page on GitHub llms.txt

**Examples**:

```javascript
<script>
	let count = 0;
</script>

<button on:click={() => count += 1}>
	clicks: {count}
</button>
```

```javascript
<script>
	let numbers = [1, 2, 3, 4];

	function addNumber() {
		// this method call does not trigger an update
		numbers.push(numbers.length + 1);

		// this assignment will update anything
		// that depends on `numbers`
		numbers = numbers;
	}
</script>
```

---

## Reactive $: statements

**URL**: https://svelte.dev/docs/svelte/legacy-reactive-assignments

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

In runes mode, reactions to state updates are handled with the $derived and $effect runes.

In legacy mode, any top-level statement (i.e. not inside a block or a function) can be made reactive by prefixing it with a $: label. These statements run after other code in the <script> and before the component markup is rendered, then whenever the values that they depend on change.

Statements are ordered topologically by their dependencies and their assignments: since the console.log statement depends on sum, sum is calculated first even though it appears later in the source.

Multiple statements can be combined by putting them in a block:

The left-hand side of a reactive assignments can be an identifier, or it can be a destructuring assignment:

The dependencies of a $: statement are determined at compile time — they are whichever variables are referenced (but not assigned to) inside the statement.

In other words, a statement like this will not re-run when count changes, because the compiler cannot ‘see’ the dependency:

Similarly, topological ordering will fail if dependencies are referenced indirectly: z will never update, because y is not considered ‘dirty’ when the update occurs. Moving $: z = y below $: setY(x) will fix it:

Reactive statements run during server-side rendering as well as in the browser. This means that any code that should only run in the browser must be wrapped in an if block:

Contains the title of the document.

Edit this page on GitHub llms.txt

**Examples**:

```javascript
<script>
	let a = 1;
	let b = 2;

	// this is a 'reactive statement', and it will re-run
	// when `a`, `b` or `sum` change
	$: console.log(`${a} + ${b} = ${sum}`);

	// this is a 'reactive assignment' — `sum` will be
	// recalculated when `a` or `b` change. It is
	// not necessary to declare `sum` separately
	$: sum = a + b;
</script>
```

```javascript
$: {
	// recalculate `total` when `items` changes
	total = 0;

	for (const const item: anyitem of items) {
		total += const item: anyitem.value;
	}
}
```

```javascript
const item: any
```

---

## Remote functions

**URL**: https://svelte.dev/docs/kit/remote-functions

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Remote functions

Remote functions are a tool for type-safe communication between client and server. They can be called anywhere in your app, but always run on the server, meaning they can safely access server-only modules containing things like environment variables and database clients.

Combined with Svelte’s experimental support for await, it allows you to load and manipulate data directly inside your components.

This feature is currently experimental, meaning it is likely to contain bugs and is subject to change without notice. You must opt in by adding the kit.experimental.remoteFunctions option in your svelte.config.js and optionally, the compilerOptions.experimental.async option to use await in components:

Remote functions are exported from a .remote.js or .remote.ts file, and come in four flavours: query, form, command and prerender. On the client, the exported functions are transformed to fetch wrappers that invoke their counterparts on the server via a generated HTTP endpoint. Remote files must be placed in your src directory.

The query function allows you to read dynamic data from the server (for static data, consider using prerender instead):

Creates a remote query. When called from the browser, the function will be invoked on the server via a fetch call.

See Remote functions for full documentation.

Creates a remote query. When called from the browser, the function will be invoked on the server via a fetch call.

See Remote functions for full documentation.

Throughout this page, you’ll see imports from fictional modules like $lib/server/database and $lib/server/auth. These are purely for illustrative purposes — you can use whatever database client and auth setup you like.

The db.sql function above is a tagged template function that escapes any interpolated values.

The query returned from getPosts works as a Promise that resolves to posts:

Until the promise resolves — and if it errors — the nearest <svelte:boundary> will be invoked.

While using await is recomme

*[Content truncated - see full docs]*

**Examples**:

```javascript
/** @type {import('@sveltejs/kit').Config} */
const const config: {
    kit: {
        experimental: {
 remoteFunctions: boolean;
        };
    };
    compilerOptions: {
        experimental: {
 async: boolean;
        };
    };
}@type{import('@sveltejs/kit').Config}config = {
	kit: {
    experimental: {
        remoteFunctions: boolean;
    };
}kit: {
		experimental: {
    remoteFunctions: boolean;
}experimental: {
			remoteFunctions: booleanremoteFunctions: true
		}
	},
	compilerOptions: {
  
...
```

```javascript
const config: {
    kit: {
        experimental: {
 remoteFunctions: boolean;
        };
    };
    compilerOptions: {
        experimental: {
 async: boolean;
        };
    };
}
```

```javascript
const config: {
    kit: {
        experimental: {
 remoteFunctions: boolean;
        };
    };
    compilerOptions: {
        experimental: {
 async: boolean;
        };
    };
}
```

---

## Routing

**URL**: https://svelte.dev/docs/kit/routing

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

## Runtime errors

**URL**: https://svelte.dev/docs/svelte/runtime-errors

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

In Svelte there are two types of reaction — $derived and $effect. Deriveds can be created anywhere, because they run lazily and can be garbage collected if nothing references them. Effects, by contrast, keep running eagerly whenever their dependencies change, until they are destroyed.

Because of this, effects can only be created inside other effects (or effect roots, such as the one that is created when you first mount a component) so that Svelte knows when to destroy them.

Some sleight of hand occurs when a derived contains an await expression: Since waiting until we read {await getPromise()} to call getPromise would be too late, we use an effect to instead call it proactively, notifying Svelte when the value is available. But since we’re using an effect, we can only create asynchronous deriveds inside another effect.

See the migration guide for more information.

See the migration guide for more information.

If an effect updates some state that it also depends on, it will re-run, potentially in a loop:

Declares reactive state.

https://svelte.dev/docs/svelte/$state

Runs code when a component is mounted to the DOM, and then whenever its dependencies change, i.e. $state or $derived values. The timing of the execution is after the DOM has been updated.

If you return a function from the effect, it will be called right before the effect is run again, or when the component is unmounted.

Does not run during server-side rendering.

https://svelte.dev/docs/svelte/$effect

(Svelte intervenes before this can crash your browser tab.)

The same applies to array mutations, since these both read and write to the array:

Declares reactive state.

https://svelte.dev/docs/svelte/$state

Runs code when a component is mounted to the DOM, and then whenever its dependencies change, i.e. $state or $derived values. The timing of the execution is after the DOM has been updated.

If you return a function from the effect, it will be called right before the effect is run again, or wh

*[Content truncated - see full docs]*

**Examples**:

```text
Cannot create a `$derived(...)` with an `await` expression outside of an effect tree
```

```text
Using `bind:value` together with a checkbox input is not allowed. Use `bind:checked` instead
```

```text
Component %component% has an export named `%key%` that a consumer component is trying to access using `bind:%key%`, which is disallowed. Instead, use `bind:this` (e.g. `<%name% bind:this={component} />`) and then access the property on the bound component instance (e.g. `component.%key%`)
```

---

## Runtime warnings

**URL**: https://svelte.dev/docs/svelte/runtime-warnings

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

Given a case like this...

...the array being pushed to when the button is first clicked is the [] on the right-hand side of the assignment, but the resulting value of object.array is an empty state proxy. As a result, the pushed value will be discarded.

You can fix this by separating it into two statements:

Appends new elements to the end of an array, and returns the new length of the array.

Gets or sets the length of the array. This is a number one higher than the highest index in the array.

Svelte’s signal-based reactivity works by tracking which bits of state are read when a template or $derived(...) expression executes. If an expression contains an await, Svelte transforms it such that any state after the await is also tracked — in other words, in a case like this...

Declares derived state, i.e. one that depends on other state variables. The expression inside $derived(...) should be free of side-effects.

https://svelte.dev/docs/svelte/$derived

...both a and b are tracked, even though b is only read once a has resolved, after the initial execution.

This does not apply to an await that is not ‘visible’ inside the expression. In a case like this...

Declares derived state, i.e. one that depends on other state variables. The expression inside $derived(...) should be free of side-effects.

https://svelte.dev/docs/svelte/$derived

...total will depend on a (which is read immediately) but not b (which is not). The solution is to pass the values into the function:

Declares derived state, i.e. one that depends on other state variables. The expression inside $derived(...) should be free of side-effects.

https://svelte.dev/docs/svelte/$derived

In a case like this...

Declares derived state, i.e. one that depends on other state variables. The expression inside $derived(...) should be free of side-effects.

https://svelte.dev/docs/svelte/$derived

Declares derived state, i.e. one that depends on other state variables. The expression inside $derived(...) should be

*[Content truncated - see full docs]*

**Examples**:

```text
Assignment to `%property%` property (%location%) will evaluate to the right-hand side, not the value of `%property%` following the assignment. This may result in unexpected behaviour.
```

```javascript
<script>
	let object = $state({ array: null });

	function add() {
		(object.array ??= []).push(object.array.length);
	}
</script>

<button onclick={add}>add</button>
<p>items: {JSON.stringify(object.items)}</p>
```

```javascript
function function add(): voidadd() {
	let object: {
    array: number[];
}object.array: number[]array ??= [];
	let object: {
    array: number[];
}object.array: number[]array.Array<number>.push(...items: number[]): numberAppends new elements to the end of an array, and returns the new length of the array.
@paramitems New elements to add to the array.push(let object: {
    array: number[];
}object.array: number[]array.Array<number>.length: numberGets or sets the length of the array. This is a num
...
```

---

## SEO

**URL**: https://svelte.dev/docs/kit/seo

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- SEO

The most important aspect of SEO is to create high-quality content that is widely linked to from around the web. However, there are a few technical considerations for building sites that rank well.

While search engines have got better in recent years at indexing content that was rendered with client-side JavaScript, server-side rendered content is indexed more frequently and reliably. SvelteKit employs SSR by default, and while you can disable it in handle, you should leave it on unless you have a good reason not to.

SvelteKit’s rendering is highly configurable and you can implement dynamic rendering if necessary. It’s not generally recommended, since SSR has other benefits beyond SEO.

Signals such as Core Web Vitals impact search engine ranking. Because Svelte and SvelteKit introduce minimal overhead, they make it easier to build high performance sites. You can test your site’s performance using Google’s PageSpeed Insights or Lighthouse. With just a few key actions like using SvelteKit’s default hybrid rendering mode and optimizing your images, you can greatly improve your site’s speed. Read the performance page for more details.

SvelteKit redirects pathnames with trailing slashes to ones without (or vice versa depending on your configuration), as duplicate URLs are bad for SEO.

Every page should have well-written and unique <title> and <meta name="description"> elements inside a <svelte:head>. Guidance on how to write descriptive titles and descriptions, along with other suggestions on making content understandable by search engines, can be found on Google’s Lighthouse SEO audits documentation.

A common pattern is to return SEO-related data from page load functions, then use it (as page.data) in a <svelte:head> in your root layout.

Sitemaps help search engines prioritize pages within your site, particularly when you have a large amount of content. You can create a sitemap dynamically using an endpoint:

This Fetch API interface represents the response to a 

*[Content truncated - see full docs]*

**Examples**:

```javascript
export async function function GET(): Promise<Response>GET() {
	return new var Response: new (body?: BodyInit | null, init?: ResponseInit) => ResponseThis Fetch API interface represents the response to a request.
MDN Reference
Response(
		`
		<?xml version="1.0" encoding="UTF-8" ?>
		<urlset
			xmlns="https://www.sitemaps.org/schemas/sitemap/0.9"
			xmlns:xhtml="https://www.w3.org/1999/xhtml"
			xmlns:mobile="https://www.google.com/schemas/sitemap-mobile/1.0"
			xmlns:news="https://www.google.co
...
```

```javascript
function GET(): Promise<Response>
```

```javascript
var Response: new (body?: BodyInit | null, init?: ResponseInit) => Response
```

---

## Scoped styles

**URL**: https://svelte.dev/docs/svelte/scoped-styles

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

Svelte components can include a <style> element containing CSS that belongs to the component. This CSS is scoped by default, meaning that styles will not apply to any elements on the page outside the component in question.

This works by adding a class to affected elements, which is based on a hash of the component styles (e.g. svelte-123xyz).

Each scoped selector receives a specificity increase of 0-1-0, as a result of the scoping class (e.g. .svelte-123xyz) being added to the selector. This means that (for example) a p selector defined in a component will take precedence over a p selector defined in a global stylesheet, even if the global stylesheet is loaded later.

In some cases, the scoping class must be added to a selector multiple times, but after the first occurrence it is added with :where(.svelte-xyz123) in order to not increase specificity further.

If a component defines @keyframes, the name is scoped to the component using the same hashing approach. Any animation rules in the component will be similarly adjusted:

Edit this page on GitHub llms.txt

**Examples**:

```text
<style>
	p {
		/* this will only affect <p> elements in this component */
		color: burlywood;
	}
</style>
```

```text
<style>
	.bouncy {
		animation: bounce 10s;
	}

	/* these keyframes are only accessible inside this component */
	@keyframes bounce {
		/* ... */
	}
</style>
```

---

## Server-only modules

**URL**: https://svelte.dev/docs/kit/server-only-modules

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Server-only modules

Like a good friend, SvelteKit keeps your secrets. When writing your backend and frontend in the same repository, it can be easy to accidentally import sensitive data into your front-end code (environment variables containing API keys, for example). SvelteKit provides a way to prevent this entirely: server-only modules.

The $env/static/private and $env/dynamic/private modules can only be imported into modules that only run on the server, such as hooks.server.js or +page.server.js.

The $app/server module, which contains a read function for reading assets from the filesystem, can likewise only be imported by code that runs on the server.

You can make your own modules server-only in two ways:

Any time you have public-facing code that imports server-only code (whether directly or indirectly)...

...SvelteKit will error:

Even though the public-facing code — src/routes/+page.svelte — only uses the add export and not the secret atlantisCoordinates export, the secret code could end up in JavaScript that the browser downloads, and so the import chain is considered unsafe.

This feature also works with dynamic imports, even interpolated ones like await import(`./${foo}.js`).

Unit testing frameworks like Vitest do not distinguish between server-only and public-facing code. For this reason, illegal import detection is disabled when running tests, as determined by process.env.TEST === 'true'.

Edit this page on GitHub llms.txt

**Examples**:

```javascript
export const atlantisCoordinates = [/* redacted */];
```

```javascript
export { export atlantisCoordinatesatlantisCoordinates } from '$lib/server/secrets.js';

export const const add: (a: any, b: any) => anyadd = (a, b) => a: anya + b: anyb;
```

```text
export atlantisCoordinates
```

---

## Service workers

**URL**: https://svelte.dev/docs/kit/service-workers

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Service workers

Service workers act as proxy servers that handle network requests inside your app. This makes it possible to make your app work offline, but even if you don’t need offline support (or can’t realistically implement it because of the type of app you’re building), it’s often worth using service workers to speed up navigation by precaching your built JS and CSS.

In SvelteKit, if you have a src/service-worker.js file (or src/service-worker/index.js) it will be bundled and automatically registered. You can change the location of your service worker if you need to.

You can disable automatic registration if you need to register the service worker with your own logic or use another solution. The default registration looks something like this:

Available only in secure contexts.

Inside the service worker you have access to the $service-worker module, which provides you with the paths to all static assets, build files and prerendered pages. You’re also provided with an app version string, which you can use for creating a unique cache name, and the deployment’s base path. If your Vite config specifies define (used for global variable replacements), this will be applied to service workers as well as your server/client builds.

The following example caches the built app and any files in static eagerly, and caches all other requests as they happen. This would make each page work offline once visited.

An array of URL strings representing the files generated by Vite, suitable for caching with cache.addAll(build). During development, this is an empty array.

An array of URL strings representing the files in your static directory, or whatever directory is specified by config.kit.files.assets. You can customize which files are included from static directory using config.kit.serviceWorker.files

See config.kit.version. It’s useful for generating unique cache names inside your service worker, so that a later deployment of your app can invalidate old caches.

See config.kit.version. I

*[Content truncated - see full docs]*

**Examples**:

```javascript
if ('serviceWorker' in var navigator: NavigatorMDN Reference
navigator) {
	function addEventListener<"load">(type: "load", listener: (this: Window, ev: Event) => any, options?: boolean | AddEventListenerOptions): void (+1 overload)addEventListener('load', function () {
		var navigator: NavigatorMDN Reference
navigator.Navigator.serviceWorker: ServiceWorkerContainerAvailable only in secure contexts.
MDN Reference
serviceWorker.ServiceWorkerContainer.register(scriptURL: string | URL, options?: Reg
...
```

```text
var navigator: Navigator
```

```javascript
function addEventListener<"load">(type: "load", listener: (this: Window, ev: Event) => any, options?: boolean | AddEventListenerOptions): void (+1 overload)
```

---

## Shallow routing

**URL**: https://svelte.dev/docs/kit/shallow-routing

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Shallow routing

As you navigate around a SvelteKit app, you create history entries. Clicking the back and forward buttons traverses through this list of entries, re-running any load functions and replacing page components as necessary.

Sometimes, it’s useful to create history entries without navigating. For example, you might want to show a modal dialog that the user can dismiss by navigating back. This is particularly valuable on mobile devices, where swipe gestures are often more natural than interacting directly with the UI. In these cases, a modal that is not associated with a history entry can be a source of frustration, as a user may swipe backwards in an attempt to dismiss it and find themselves on the wrong page.

SvelteKit makes this possible with the pushState and replaceState functions, which allow you to associate state with a history entry without navigating. For example, to implement a history-driven modal:

The modal can be dismissed by navigating back (unsetting page.state.showModal) or by interacting with it in a way that causes the close callback to run, which will navigate back programmatically.

The first argument to pushState is the URL, relative to the current URL. To stay on the current URL, use ''.

The second argument is the new page state, which can be accessed via the page object as page.state. You can make page state type-safe by declaring an App.PageState interface (usually in src/app.d.ts).

To set page state without creating a new history entry, use replaceState instead of pushState.

page.state from $app/state was added in SvelteKit 2.12. If you’re using an earlier version or are using Svelte 4, use $page.state from $app/stores instead.

When shallow routing, you may want to render another +page.svelte inside the current page. For example, clicking on a photo thumbnail could pop up the detail view without navigating to the photo page.

For this to work, you need to load the data that the +page.svelte expects. A convenient way to do this is to use pr

*[Content truncated - see full docs]*

**Examples**:

```python
<script>
	import { pushState } from '$app/navigation';
	import { page } from '$app/state';
	import Modal from './Modal.svelte';

	function showModal() {
		pushState('', {
			showModal: true
		});
	}
</script>

{#if page.state.showModal}
	<Modal close={() => history.back()} />
{/if}
```

```python
<script lang="ts">
	import { pushState } from '$app/navigation';
	import { page } from '$app/state';
	import Modal from './Modal.svelte';

	function showModal() {
		pushState('', {
			showModal: true
		});
	}
</script>

{#if page.state.showModal}
	<Modal close={() => history.back()} />
{/if}
```

```python
<script>
	import { preloadData, pushState, goto } from '$app/navigation';
	import { page } from '$app/state';
	import Modal from './Modal.svelte';
	import PhotoPage from './[id]/+page.svelte';

	let { data } = $props();
</script>

{#each data.thumbnails as thumbnail}
	<a
		href="/photos/{thumbnail.id}"
		onclick={async (e) => {
			if (innerWidth < 640        // bail if the screen is too small
				|| e.shiftKey             // or the link is opened in a new window
				|| e.metaKey || e.ctrlKey // 
...
```

---

## Single-page apps

**URL**: https://svelte.dev/docs/kit/single-page-apps

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Single-page apps

You can turn a SvelteKit app into a fully client-rendered single-page app (SPA) by specifying a fallback page. This page will be served for any URLs that can’t be served by other means such as returning a prerendered page.

SPA mode has a large negative performance impact by forcing multiple network round trips (for the blank HTML document, then for the JavaScript, and then for any data needed for the page) before content can be shown. Unless you are serving the app from a local network (e.g.a mobile app that wraps a locally-served SPA) this will delay startup, especially when considering the latency of mobile devices. It also harms SEO by often causing sites to be downranked for performance (SPAs are much more likely to fail Core Web Vitals), excluding search engines that don’t render JS, and causing your site to receive less frequent updates from those that do. And finally, it makes your app inaccessible to users if JavaScript fails or is disabled (which happens more often than you probably think).

You can avoid these drawbacks by prerendering as many pages as possible when using SPA mode (especially your homepage). If you can prerender all pages, you can simply use static site generation rather than a SPA. Otherwise, you should strongly consider using an adapter which supports server side rendering. SvelteKit has officially supported adapters for various providers with generous free tiers.

First, disable SSR for the pages you don’t want to prerender. These pages will be served via the fallback page. E.g. to serve all pages via the fallback by default, you can update the root layout as shown below. You should opt back into prerendering individual pages and directories where possible.

If you don’t have any server-side logic (i.e. +page.server.js, +layout.server.js or +server.js files) you can use adapter-static to create your SPA. Install adapter-static with npm i -D @sveltejs/adapter-static and add it to your svelte.config.js with the fallback option:

The fall

*[Content truncated - see full docs]*

**Examples**:

```javascript
export const const ssr: falsessr = false;
```

```javascript
const ssr: false
```

```python
import import adapteradapter from '@sveltejs/adapter-static';

/** @type {import('@sveltejs/kit').Config} */
const const config: {
    kit: {
        adapter: any;
    };
}@type{import('@sveltejs/kit').Config}config = {
	kit: {
    adapter: any;
}kit: {
		adapter: anyadapter: import adapteradapter({
			fallback: stringfallback: '200.html' // may differ from host to host
		})
	}
};

export default const config: {
    kit: {
        adapter: any;
    };
}@type{import('@sveltejs/kit').Config}config
...
```

---

## Snapshots

**URL**: https://svelte.dev/docs/kit/snapshots

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Snapshots

Ephemeral DOM state — like scroll positions on sidebars, the content of <input> elements and so on — is discarded when you navigate from one page to another.

For example, if the user fills out a form but navigates away and then back before submitting, or if the user refreshes the page, the values they filled in will be lost. In cases where it’s valuable to preserve that input, you can take a snapshot of DOM state, which can then be restored if the user navigates back.

To do this, export a snapshot object with capture and restore methods from a +page.svelte or +layout.svelte:

When you navigate away from this page, the capture function is called immediately before the page updates, and the returned value is associated with the current entry in the browser’s history stack. If you navigate back, the restore function is called with the stored value as soon as the page is updated.

The data must be serializable as JSON so that it can be persisted to sessionStorage. This allows the state to be restored when the page is reloaded, or when the user navigates back from a different site.

Avoid returning very large objects from capture — once captured, objects will be retained in memory for the duration of the session, and in extreme cases may be too large to persist to sessionStorage.

Edit this page on GitHub llms.txt

**Examples**:

```javascript
<script>
	let comment = $state('');

	/** @type {import('./$types').Snapshot<string>} */
	export const snapshot = {
		capture: () => comment,
		restore: (value) => comment = value
	};
</script>

<form method="POST">
	<label for="comment">Comment</label>
	<textarea id="comment" bind:value={comment} />
	<button>Post comment</button>
</form>
```

```python
<script lang="ts">
	import type { Snapshot } from './$types';

	let comment = $state('');

	export const snapshot: Snapshot<string> = {
		capture: () => comment,
		restore: (value) => comment = value
	};
</script>

<form method="POST">
	<label for="comment">Comment</label>
	<textarea id="comment" bind:value={comment} />
	<button>Post comment</button>
</form>
```

---

## State management

**URL**: https://svelte.dev/docs/kit/state-management

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- State management

If you’re used to building client-only apps, state management in an app that spans server and client might seem intimidating. This section provides tips for avoiding some common gotchas.

Browsers are stateful — state is stored in memory as the user interacts with the application. Servers, on the other hand, are stateless — the content of the response is determined entirely by the content of the request.

Conceptually, that is. In reality, servers are often long-lived and shared by multiple users. For that reason it’s important not to store data in shared variables. For example, consider this code:

The original request object.

The original request object.

The user variable is shared by everyone who connects to this server. If Alice submitted an embarrassing secret, and Bob visited the page after her, Bob would know Alice’s secret. In addition, when Alice returns to the site later in the day, the server may have restarted, losing her data.

Instead, you should authenticate the user using cookies and persist the data to a database.

For the same reason, your load functions should be pure — no side-effects (except maybe the occasional console.log(...)). For example, you might be tempted to write to a store or global state inside a load function so that you can use the value in your components:

fetch is equivalent to the native fetch web API, with a few additional features:

You can learn more about making credentialed requests with cookies here

fetch is equivalent to the native fetch web API, with a few additional features:

You can learn more about making credentialed requests with cookies here

As with the previous example, this puts one user’s information in a place that is shared by all users. Instead, just return the data...

fetch is equivalent to the native fetch web API, with a few additional features:

You can learn more about making credentialed requests with cookies here.

...and pass it around to the components that need it, or use page.data.

If you’r

*[Content truncated - see full docs]*

**Examples**:

```javascript
let let user: anyuser;

/** @type {import('./$types').PageServerLoad} */
export function function load(): {
    user: any;
}@type{import('./$types').PageServerLoad}load() {
	return { user: anyuser };
}

/** @satisfies {import('./$types').Actions} */
export const const actions: {
    default: ({ request }: {
        request: any;
    }) => Promise<void>;
}@satisfies{import('./$types').Actions}actions = {
	default: ({ request }: {
    request: any;
}) => Promise<void>default: async ({ request: any
...
```

```javascript
let user: any
```

```javascript
function load(): {
    user: any;
}
```

---

## Static site generation

**URL**: https://svelte.dev/docs/kit/adapter-static

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Static site generation

To use SvelteKit as a static site generator (SSG), use adapter-static.

This will prerender your entire site as a collection of static files. If you’d like to prerender only some pages and dynamically server-render others, you will need to use a different adapter together with the prerender option.

Install with npm i -D @sveltejs/adapter-static, then add the adapter to your svelte.config.js:

...and add the prerender option to your root layout:

You must ensure SvelteKit’s trailingSlash option is set appropriately for your environment. If your host does not render /a.html upon receiving a request for /a then you will need to set trailingSlash: 'always' in your root layout to create /a/index.html instead.

Some platforms have zero-config support (more to come in future):

On these platforms, you should omit the adapter options so that adapter-static can provide the optimal configuration:

The directory to write prerendered pages to. It defaults to build.

The directory to write static assets (the contents of static, plus client-side JS and CSS generated by SvelteKit) to. Ordinarily this should be the same as pages, and it will default to whatever the value of pages is, but in rare circumstances you might need to output pages and assets to separate locations.

To create a single page app (SPA) you must specify the name of the fallback page to be generated by SvelteKit, which is used as the entry point for URLs that have not been prerendered. This is commonly 200.html, but can vary depending on your deployment platform. You should avoid index.html where possible to avoid conflicting with a prerendered homepage.

This option has large negative performance and SEO impacts. It is only recommended in certain circumstances such as wrapping the site in a mobile app. See the single page apps documentation for more details and alternatives.

If true, precompresses files with brotli and gzip. This will generate .br and .gz files.

By default, adapter-static checks that either 

*[Content truncated - see full docs]*

**Examples**:

```python
import import adapteradapter from '@sveltejs/adapter-static';

/** @type {import('@sveltejs/kit').Config} */
const const config: {
    kit: {
        adapter: any;
    };
}@type{import('@sveltejs/kit').Config}config = {
	kit: {
    adapter: any;
}kit: {
		adapter: anyadapter: import adapteradapter({
			// default options are shown. On some platforms
			// these options are set automatically — see below
			pages: stringpages: 'build',
			assets: stringassets: 'build',
			fallback: undefinedfallba
...
```

```text
import adapter
```

```javascript
const config: {
    kit: {
        adapter: any;
    };
}
```

---

## Svelte 4 migration guide

**URL**: https://svelte.dev/docs/svelte/v4-migration-guide

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

This migration guide provides an overview of how to migrate from Svelte version 3 to 4. See the linked PRs for more details about each change. Use the migration script to migrate some of these automatically: npx svelte-migrate@latest svelte-4

If you’re a library author, consider whether to only support Svelte 4 or if it’s possible to support Svelte 3 too. Since most of the breaking changes don’t affect many people, this may be easily possible. Also remember to update the version range in your peerDependencies.

Bundlers must now specify the browser condition when building a frontend bundle for the browser. SvelteKit and Vite will handle this automatically for you. If you’re using any others, you may observe lifecycle callbacks such as onMount not get called and you’ll need to update the module resolution configuration.

Svelte no longer supports the CommonJS (CJS) format for compiler output and has also removed the svelte/register hook and the CJS runtime version. If you need to stay on the CJS output format, consider using a bundler to convert Svelte’s ESM output to CJS in a post-build step. (#8613)

There are now stricter types for createEventDispatcher, Action, ActionReturn, and onMount:

Creates an event dispatcher that can be used to dispatch component events. Event dispatchers are functions that can take two arguments: name and detail.

Component events created with createEventDispatcher create a CustomEvent. These events do not bubble. The detail argument corresponds to the CustomEvent.detail property and can contain any type of data.

The event dispatcher can be typed to narrow the allowed event names and the type of the detail argument:

Creates an event dispatcher that can be used to dispatch component events. Event dispatchers are functions that can take two arguments: name and detail.

Component events created with createEventDispatcher create a CustomEvent. These events do not bubble. The detail argument corresponds to the CustomEvent.detail property a

*[Content truncated - see full docs]*

**Examples**:

```python
import { function createEventDispatcher<EventMap extends Record<string, any> = any>(): EventDispatcher<EventMap>Creates an event dispatcher that can be used to dispatch component events.
Event dispatchers are functions that can take two arguments: name and detail.
Component events created with createEventDispatcher create a
CustomEvent.
These events do not bubble.
The detail argument corresponds to the CustomEvent.detail
property and can contain any type of data.
The event dispatcher can be type
...
```

```javascript
function createEventDispatcher<EventMap extends Record<string, any> = any>(): EventDispatcher<EventMap>
```

```text
createEventDispatcher
```

---

## Svelte 5 migration guide

**URL**: https://svelte.dev/docs/svelte/v5-migration-guide

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

Version 5 comes with an overhauled syntax and reactivity system. While it may look different at first, you’ll soon notice many similarities. This guide goes over the changes in detail and shows you how to upgrade. Along with it, we also provide information on why we did these changes.

You don’t have to migrate to the new syntax right away - Svelte 5 still supports the old Svelte 4 syntax, and you can mix and match components using the new syntax with components using the old and vice versa. We expect many people to be able to upgrade with only a few lines of code changed initially. There’s also a migration script that helps you with many of these steps automatically.

At the heart of Svelte 5 is the new runes API. Runes are basically compiler instructions that inform Svelte about reactivity. Syntactically, runes are functions starting with a dollar-sign.

In Svelte 4, a let declaration at the top level of a component was implicitly reactive. In Svelte 5, things are more explicit: a variable is reactive when created using the $state rune. Let’s migrate the counter to runes mode by wrapping the counter in $state:

Nothing else changes. count is still the number itself, and you read and write directly to it, without a wrapper like .value or getCount().

let being implicitly reactive at the top level worked great, but it meant that reactivity was constrained - a let declaration anywhere else was not reactive. This forced you to resort to using stores when refactoring code out of the top level of components for reuse. This meant you had to learn an entirely separate reactivity model, and the result often wasn’t as nice to work with. Because reactivity is more explicit in Svelte 5, you can keep using the same API outside the top level of components. Head to the tutorial to learn more.

In Svelte 4, a $: statement at the top level of a component could be used to declare a derivation, i.e. state that is entirely defined through a computation of other state. In Svelte 5, th

*[Content truncated - see full docs]*

**Examples**:

```javascript
<script>
	let count = $state(0);
</script>
```

```javascript
<script>
	let count = $state(0);
	$: const double = $derived(count * 2);
</script>
```

```javascript
<script>
	let count = $state(0);

	$:$effect(() => {
		if (count > 5) {
			alert('Count is too high!');
		}
	});
</script>
```

---

## Testing

**URL**: https://svelte.dev/docs/svelte/testing

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

Testing helps you write and maintain your code and guard against regressions. Testing frameworks help you with that, allowing you to describe assertions or expectations about how your code should behave. Svelte is unopinionated about which testing framework you use — you can write unit tests, integration tests, and end-to-end tests using solutions like Vitest, Jasmine, Cypress and Playwright.

Unit tests allow you to test small isolated parts of your code. Integration tests allow you to test parts of your application to see if they work together. If you’re using Vite (including via SvelteKit), we recommend using Vitest. You can use the Svelte CLI to setup Vitest either during project creation or later on.

To setup Vitest manually, first install it:

Then adjust your vite.config.js:

The process.env property returns an object containing the user environment. See environ(7).

An example of this object looks like:

It is possible to modify this object, but such modifications will not be reflected outside the Node.js process, or (unless explicitly requested) to other Worker threads. In other words, the following example would not work:

While the following will:

Assigning a property on process.env will implicitly convert the value to a string. This behavior is deprecated. Future versions of Node.js may throw an error when the value is not a string, number, or boolean.

Use delete to delete a property from process.env.

On Windows operating systems, environment variables are case-insensitive.

Unless explicitly specified when creating a Worker instance, each Worker thread has its own copy of process.env, based on its parent thread’s process.env, or whatever was specified as the env option to the Worker constructor. Changes to process.env will not be visible across Worker threads, and only the main thread can make changes that are visible to the operating system or to native add-ons. On Windows, a copy of process.env on a Worker instance operates in a case-sensitive man

*[Content truncated - see full docs]*

**Examples**:

```text
npm install -D vitest
```

```python
import { function defineConfig(config: UserConfig): UserConfig (+3 overloads)defineConfig } from 'vitest/config';

export default function defineConfig(config: UserConfig): UserConfig (+3 overloads)defineConfig({
	// ...
	// Tell Vitest to use the `browser` entry points in `package.json` files, even though it's running in Node
	resolve?: AllResolveOptions | undefinedresolve: var process: NodeJS.Processprocess.NodeJS.Process.env: NodeJS.ProcessEnvThe process.env property returns an object contain
...
```

```javascript
function defineConfig(config: UserConfig): UserConfig (+3 overloads)
```

---

## TypeScript

**URL**: https://svelte.dev/docs/svelte/typescript

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

You can use TypeScript within Svelte components. IDE extensions like the Svelte VS Code extension will help you catch errors right in your editor, and svelte-check does the same on the command line, which you can integrate into your CI.

To use TypeScript inside your Svelte components, add lang="ts" to your script tags:

Doing so allows you to use TypeScript’s type-only features. That is, all features that just disappear when transpiling to JavaScript, such as type annotations or interface declarations. Features that require the TypeScript compiler to output actual code are not supported. This includes:

If you want to use one of these features, you need to setup up a script preprocessor.

To use non-type-only TypeScript features within Svelte components, you need to add a preprocessor that will turn TypeScript into JavaScript.

preprocess script block with vite pipeline. Since svelte5 this is not needed for typescript anymore

The easiest way to get started is scaffolding a new SvelteKit project by typing npx sv create, following the prompts and choosing the TypeScript option.

If you don’t need or want all the features SvelteKit has to offer, you can scaffold a Svelte-flavoured Vite project instead by typing npm create vite@latest and selecting the svelte-ts option.

In both cases, a svelte.config.js with vitePreprocess will be added. Vite/SvelteKit will read from this config file.

If you’re using tools like Rollup or Webpack instead, install their respective Svelte plugins. For Rollup that’s rollup-plugin-svelte and for Webpack that’s svelte-loader. For both, you need to install typescript and svelte-preprocess and add the preprocessor to the plugin config (see the respective READMEs for more info). If you’re starting a new project, you can also use the rollup or webpack template to scaffold the setup from a script.

If you’re starting a new project, we recommend using SvelteKit or Vite instead

When using TypeScript, make sure your tsconfig.json is setup correc

*[Content truncated - see full docs]*

**Examples**:

```javascript
<script lang="ts">
	let name: string = 'world';

	function greet(name: string) {
		alert(`Hello, ${name}!`);
	}
</script>

<button onclick={(e: Event) => greet(e.target.innerText)}>
	{name as string}
</button>
```

```python
import { function vitePreprocess(opts?: VitePreprocessOptions): import("svelte/compiler").PreprocessorGroupvitePreprocess } from '@sveltejs/vite-plugin-svelte';

const const config: {
    preprocess: PreprocessorGroup;
}config = {
	// Note the additional `{ script: true }`
	preprocess: PreprocessorGrouppreprocess: function vitePreprocess(opts?: VitePreprocessOptions): import("svelte/compiler").PreprocessorGroupvitePreprocess({ VitePreprocessOptions.script?: boolean | undefinedpreprocess script b
...
```

```javascript
function vitePreprocess(opts?: VitePreprocessOptions): import("svelte/compiler").PreprocessorGroup
```

---

## Vercel

**URL**: https://svelte.dev/docs/kit/adapter-vercel

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Vercel

To deploy to Vercel, use adapter-vercel.

This adapter will be installed by default when you use adapter-auto, but adding it to your project allows you to specify Vercel-specific options.

Install with npm i -D @sveltejs/adapter-vercel, then add the adapter to your svelte.config.js:

To control how your routes are deployed to Vercel as functions, you can specify deployment configuration, either through the option shown above or with export const config inside +server.js, +page(.server).js and +layout(.server).js files.

For example you could deploy one specific route as an individual serverless function, separate from the rest of your app:

The following options apply to all functions:

This option is deprecated and will be removed in a future version, at which point all your functions will use whichever Node version is specified in the project configuration on Vercel

Additionally, the following option applies to edge functions:

And the following option apply to serverless functions:

Configuration set in a layout applies to all the routes beneath that layout, unless overridden at a more granular level.

If your functions need to access data in a specific region, it’s recommended that they be deployed in the same region (or close to it) for optimal performance.

You may set the images config to control how Vercel builds your images. See the image configuration reference for full details. As an example, you may set:

https://vercel.com/docs/build-output-api/v3/configuration#images

Vercel supports Incremental Static Regeneration (ISR), which provides the performance and cost advantages of prerendered content with the flexibility of dynamically rendered content.

Use ISR only on routes where every visitor should see the same content (much like when you prerender). If there’s anything user-specific happening (like session cookies), they should happen on the client via JavaScript only to not leak sensitive information across visits

To add ISR to a route, include the 

*[Content truncated - see full docs]*

**Examples**:

```python
import function adapter(config?: Config): Adapteradapter from '@sveltejs/adapter-vercel';

/** @type {import('@sveltejs/kit').Config} */
const const config: {
    kit: {
        adapter: Adapter;
    };
}@type{import('@sveltejs/kit').Config}config = {
	kit: {
    adapter: Adapter;
}kit: {
		adapter: Adapteradapter: function adapter(config?: Config): Adapteradapter({
			// see below for options that can be set here
		})
	}
};

export default const config: {
    kit: {
        adapter: Adapter;
  
...
```

```javascript
function adapter(config?: Config): Adapter
```

```javascript
const config: {
    kit: {
        adapter: Adapter;
    };
}
```

---

## Web standards

**URL**: https://svelte.dev/docs/kit/web-standards

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Web standards

Throughout this documentation, you’ll see references to the standard Web APIs that SvelteKit builds on top of. Rather than reinventing the wheel, we use the platform, which means your existing web development skills are applicable to SvelteKit. Conversely, time spent learning SvelteKit will help you be a better web developer elsewhere.

These APIs are available in all modern browsers and in many non-browser environments like Cloudflare Workers, Deno, and Vercel Functions. During development, and in adapters for Node-based environments (including AWS Lambda), they’re made available via polyfills where necessary (for now, that is — Node is rapidly adding support for more web standards).

In particular, you’ll get comfortable with the following:

SvelteKit uses fetch for getting data from the network. It’s available in hooks and server routes as well as in the browser.

A special version of fetch is available in load functions, server hooks and API routes for invoking endpoints directly during server-side rendering, without making an HTTP call, while preserving credentials. (To make credentialled fetches in server-side code outside load, you must explicitly pass cookie and/or authorization headers.) It also allows you to make relative requests, whereas server-side fetch normally requires a fully qualified URL.

Besides fetch itself, the Fetch API includes the following interfaces:

An instance of Request is accessible in hooks and server routes as event.request. It contains useful methods like request.json() and request.formData() for getting data that was posted to an endpoint.

An instance of Response is returned from await fetch(...) and handlers in +server.js files. Fundamentally, a SvelteKit app is a machine for turning a Request into a Response.

The Headers interface allows you to read incoming request.headers and set outgoing response.headers. For example, you can get the request.headers as shown below, and use the json convenience function to send modified res

*[Content truncated - see full docs]*

**Examples**:

```python
import { function json(data: any, init?: ResponseInit): ResponseCreate a JSON Response object from the supplied data.
@paramdata The value that will be serialized as JSON.@paraminit Options such as status and headers that will be added to the response. Content-Type: application/json and Content-Length headers will be added automatically.json } from '@sveltejs/kit';

/** @type {import('./$types').RequestHandler} */
export function function GET({ request }: {
    request: any;
}): Response@type{im
...
```

```javascript
function json(data: any, init?: ResponseInit): Response
```

```text
Content-Type: application/json
```

---

## What are runes?

**URL**: https://svelte.dev/docs/svelte/what-are-runes

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

A letter or mark used as a mystical or magic symbol.

Runes are symbols that you use in .svelte and .svelte.js / .svelte.ts files to control the Svelte compiler. If you think of Svelte as a language, runes are part of the syntax — they are keywords.

Runes have a $ prefix and look like functions:

Declares reactive state.

https://svelte.dev/docs/svelte/$state

They differ from normal JavaScript functions in important ways, however:

Runes didn’t exist prior to Svelte 5.

Edit this page on GitHub llms.txt

**Examples**:

```javascript
let let message: stringmessage = function $state<"hello">(initial: "hello"): "hello" (+1 overload)
namespace $stateDeclares reactive state.
Example:
let count = $state(0);https://svelte.dev/docs/svelte/$state
@paraminitial The initial value$state('hello');
```

```javascript
let message: string
```

```javascript
function $state<"hello">(initial: "hello"): "hello" (+1 overload)
namespace $state
```

---

## Writing adapters

**URL**: https://svelte.dev/docs/kit/writing-adapters

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Writing adapters

If an adapter for your preferred environment doesn’t yet exist, you can build your own. We recommend looking at the source for an adapter to a platform similar to yours and copying it as a starting point.

Adapter packages implement the following API, which creates an Adapter:

The name of the adapter, using for logging. Will typically correspond to the package name.

This function is called after SvelteKit has built your app.

Creates an Emulator, which allows the adapter to influence the environment during dev, build and prerendering.

A function that is called with the current route config and prerender option and returns an App.Platform object

Checks called during dev and build to determine whether specific features will work in production with this adapter.

Of these, name and adapt are required. emulate and supports are optional.

Within the adapt method, there are a number of things that an adapter should do:

Where possible, we recommend putting the adapter output under the build/ directory with any intermediate output placed under .svelte-kit/[adapter-name].

Edit this page on GitHub llms.txt

**Examples**:

```javascript
/** @param {AdapterSpecificOptions} options */
export default function (options: any@paramoptions options) {
	/** @type {import('@sveltejs/kit').Adapter} */
	const const adapter: Adapter@type{import('@sveltejs/kit').Adapter}adapter = {
		Adapter.name: stringThe name of the adapter, using for logging. Will typically correspond to the package name.
name: 'adapter-package-name',
		async Adapter.adapt: (builder: Builder) => MaybePromise<void>This function is called after SvelteKit has built your app
...
```

```text
options: any
```

```javascript
const adapter: Adapter
```

---

## Zero-config deployments

**URL**: https://svelte.dev/docs/kit/adapter-auto

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- Zero-config deployments

When you create a new SvelteKit project with npx sv create, it installs adapter-auto by default. This adapter automatically installs and uses the correct adapter for supported environments when you deploy:

It’s recommended to install the appropriate adapter to your devDependencies once you’ve settled on a target environment, since this will add the adapter to your lockfile and slightly improve install times on CI.

To add configuration options, such as { edge: true } in adapter-vercel and adapter-netlify, you must install the underlying adapter — adapter-auto does not take any options.

You can add zero-config support for additional adapters by editing adapters.js and opening a pull request.

Edit this page on GitHub llms.txt

---

## 

**URL**: https://svelte.dev/docs/svelte/overview/llms.txt

---

## $app/environment

**URL**: https://svelte.dev/docs/kit/$app-environment

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- $app/environment

true if the app is running in the browser.

SvelteKit analyses your app during the build step by running it. During this process, building is true. This also applies during prerendering.

Whether the dev server is running. This is not guaranteed to correspond to NODE_ENV or MODE.

The value of config.kit.version.name.

true if the app is running in the browser.

SvelteKit analyses your app during the build step by running it. During this process, building is true. This also applies during prerendering.

Whether the dev server is running. This is not guaranteed to correspond to NODE_ENV or MODE.

The value of config.kit.version.name.

Edit this page on GitHub llms.txt

**Examples**:

```python
import { const browser: booleantrue if the app is running in the browser.
browser, const building: booleanSvelteKit analyses your app during the build step by running it. During this process, building is true. This also applies during prerendering.
building, const dev: booleanWhether the dev server is running. This is not guaranteed to correspond to NODE_ENV or MODE.
dev, const version: stringThe value of config.kit.version.name.
version } from '$app/environment';
```

```javascript
const browser: boolean
```

```javascript
const building: boolean
```

---

## $app/forms

**URL**: https://svelte.dev/docs/kit/$app-forms

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- $app/forms

This action updates the form property of the current page with the given data and updates page.status. In case of an error, it redirects to the nearest error page.

Use this function to deserialize the response from a form submission. Usage:

This action enhances a &#x3C;form> element that otherwise would work without JavaScript.

The submit function is called upon submission with the given FormData and the action that should be triggered. If cancel is called, the form will not be submitted. You can use the abort controller to cancel the submission in case another one starts. If a function is returned, that function is called with the response from the server. If nothing is returned, the fallback will be used.

If this function or its return value isn’t set, it

If you provide a custom function with a callback and want to use the default behavior, invoke update in your callback. It accepts an options object

This action updates the form property of the current page with the given data and updates page.status. In case of an error, it redirects to the nearest error page.

Use this function to deserialize the response from a form submission. Usage:

Use this function to deserialize the response from a form submission. Usage:

A string to set request’s method.

A BodyInit object or null to set request’s body.

Provides a way to easily construct a set of key/value pairs representing form fields and their values, which can then be easily sent using the XMLHttpRequest.send() method. It uses the same format a form would use if the encoding type were set to “multipart/form-data”.

Use this function to deserialize the response from a form submission. Usage:

This action enhances a <form> element that otherwise would work without JavaScript.

The submit function is called upon submission with the given FormData and the action that should be triggered. If cancel is called, the form will not be submitted. You can use the abort controller to cancel the submission in case another 

*[Content truncated - see full docs]*

**Examples**:

```python
import { function applyAction<Success extends Record<string, unknown> | undefined, Failure extends Record<string, unknown> | undefined>(result: import("@sveltejs/kit").ActionResult<Success, Failure>): Promise<void>This action updates the form property of the current page with the given data and updates page.status.
In case of an error, it redirects to the nearest error page.
applyAction, function deserialize<Success extends Record<string, unknown> | undefined, Failure extends Record<string, unkn
...
```

```javascript
function applyAction<Success extends Record<string, unknown> | undefined, Failure extends Record<string, unknown> | undefined>(result: import("@sveltejs/kit").ActionResult<Success, Failure>): Promise<void>
```

```text
page.status
```

---

## $app/navigation

**URL**: https://svelte.dev/docs/kit/$app-navigation

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- $app/navigation

A lifecycle function that runs the supplied callback when the current component mounts, and also whenever we navigate to a URL.

afterNavigate must be called during a component initialization. It remains active as long as the component is mounted.

A navigation interceptor that triggers before we navigate to a URL, whether by clicking a link, calling goto(...), or using the browser back/forward controls.

Calling cancel() will prevent the navigation from completing. If navigation.type === 'leave' — meaning the user is navigating away from the app (or closing the tab) — calling cancel will trigger the native browser unload confirmation dialog. In this case, the navigation may or may not be cancelled depending on the user’s response.

When a navigation isn’t to a SvelteKit-owned route (and therefore controlled by SvelteKit’s client-side router), navigation.to.route.id will be null.

If the navigation will (if not cancelled) cause the document to unload — in other words 'leave' navigations and 'link' navigations where navigation.to.route === null — navigation.willUnload is true.

beforeNavigate must be called during a component initialization. It remains active as long as the component is mounted.

If called when the page is being updated following a navigation (in onMount or afterNavigate or an action, for example), this disables SvelteKit’s built-in scroll handling. This is generally discouraged, since it breaks user expectations.

Allows you to navigate programmatically to a given route, with options such as keeping the current element focused. Returns a Promise that resolves when SvelteKit navigates (or fails to navigate, in which case the promise rejects) to the specified url.

For external URLs, use window.location = url instead of calling goto(url).

Causes any load functions belonging to the currently active page to re-run if they depend on the url in question, via fetch or depends. Returns a Promise that resolves when the page is subsequently updated.

If the 

*[Content truncated - see full docs]*

**Examples**:

```python
import {
	function afterNavigate(callback: (navigation: import("@sveltejs/kit").AfterNavigate) => void): voidA lifecycle function that runs the supplied callback when the current component mounts, and also whenever we navigate to a URL.
afterNavigate must be called during a component initialization. It remains active as long as the component is mounted.
afterNavigate,
	function beforeNavigate(callback: (navigation: import("@sveltejs/kit").BeforeNavigate) => void): voidA navigation interceptor th
...
```

```javascript
function afterNavigate(callback: (navigation: import("@sveltejs/kit").AfterNavigate) => void): void
```

```text
afterNavigate
```

---

## $app/paths

**URL**: https://svelte.dev/docs/kit/$app-paths

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- $app/paths

Resolve the URL of an asset in your static directory, by prefixing it with config.kit.paths.assets if configured, or otherwise by prefixing it with the base path.

During server rendering, the base path is relative and depends on the page currently being rendered.

An absolute path that matches config.kit.paths.assets.

If a value for config.kit.paths.assets is specified, it will be replaced with '/_svelte_kit_assets' during vite dev or vite preview, since the assets don’t yet live at their eventual URL.

A string that matches config.kit.paths.base.

Example usage: &#x3C;a href="{base}/your-page">Link&#x3C;/a>

Resolve a pathname by prefixing it with the base path, if any, or resolve a route ID by populating dynamic segments with parameters.

During server rendering, the base path is relative and depends on the page currently being rendered.

Resolve the URL of an asset in your static directory, by prefixing it with config.kit.paths.assets if configured, or otherwise by prefixing it with the base path.

During server rendering, the base path is relative and depends on the page currently being rendered.

Use asset(...) instead

An absolute path that matches config.kit.paths.assets.

If a value for config.kit.paths.assets is specified, it will be replaced with '/_svelte_kit_assets' during vite dev or vite preview, since the assets don’t yet live at their eventual URL.

Use resolve(...) instead

A string that matches config.kit.paths.base.

Example usage: <a href="{base}/your-page">Link</a>

Resolve a pathname by prefixing it with the base path, if any, or resolve a route ID by populating dynamic segments with parameters.

During server rendering, the base path is relative and depends on the page currently being rendered.

Resolve a pathname by prefixing it with the base path, if any, or resolve a route ID by populating dynamic segments with parameters.

During server rendering, the base path is relative and depends on the page currently being rendered.

Resolve a path

*[Content truncated - see full docs]*

**Examples**:

```python
import { function asset(file: Asset): stringResolve the URL of an asset in your static directory, by prefixing it with config.kit.paths.assets if configured, or otherwise by prefixing it with the base path.
During server rendering, the base path is relative and depends on the page currently being rendered.
@examplesvelte &#x3C;script> 	import { asset } from '$app/paths'; &#x3C;/script>  &#x3C;img alt="a potato" src={asset('/potato.jpg')} /> @since2.26asset, let assets: "" | `https://${string}` |
...
```

```javascript
function asset(file: Asset): string
```

```text
config.kit.paths.assets
```

---

## $app/server

**URL**: https://svelte.dev/docs/kit/$app-server

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- $app/server

Creates a remote command. When called from the browser, the function will be invoked on the server via a fetch call.

See Remote functions for full documentation.

Creates a form object that can be spread onto a &#x3C;form> element.

See Remote functions for full documentation.

Returns the current RequestEvent. Can be used inside server hooks, server load functions, actions, and endpoints (and functions called by them).

In environments without AsyncLocalStorage, this must be called synchronously (i.e. not after an await).

Creates a remote prerender function. When called from the browser, the function will be invoked on the server via a fetch call.

See Remote functions for full documentation.

Creates a remote query. When called from the browser, the function will be invoked on the server via a fetch call.

See Remote functions for full documentation.

Read the contents of an imported asset from the filesystem

Creates a remote command. When called from the browser, the function will be invoked on the server via a fetch call.

See Remote functions for full documentation.

Creates a form object that can be spread onto a <form> element.

See Remote functions for full documentation.

Available since 2.20.0

Returns the current RequestEvent. Can be used inside server hooks, server load functions, actions, and endpoints (and functions called by them).

In environments without AsyncLocalStorage, this must be called synchronously (i.e. not after an await).

Creates a remote prerender function. When called from the browser, the function will be invoked on the server via a fetch call.

See Remote functions for full documentation.

Creates a remote query. When called from the browser, the function will be invoked on the server via a fetch call.

See Remote functions for full documentation.

Available since 2.4.0

Read the contents of an imported asset from the filesystem

Read the contents of an imported asset from the filesystem

Read the contents of an imported asset fro

*[Content truncated - see full docs]*

**Examples**:

```python
import {
	function command<Output>(fn: () => Output): RemoteCommand<void, Output> (+2 overloads)Creates a remote command. When called from the browser, the function will be invoked on the server via a fetch call.
See Remote functions for full documentation.
@since2.27command,
	function form<Output>(fn: () => MaybePromise<Output>): RemoteForm<void, Output> (+2 overloads)Creates a form object that can be spread onto a &#x3C;form> element.
See Remote functions for full documentation.
@since2.27form
...
```

```javascript
function command<Output>(fn: () => Output): RemoteCommand<void, Output> (+2 overloads)
```

```javascript
function form<Output>(fn: () => MaybePromise<Output>): RemoteForm<void, Output> (+2 overloads)
```

---

## $app/state

**URL**: https://svelte.dev/docs/kit/$app-state

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- $app/state

SvelteKit makes three read-only state objects available via the $app/state module — page, navigating and updated.

This module was added in 2.12. If you’re using an earlier version of SvelteKit, use $app/stores instead.

A read-only object representing an in-progress navigation, with from, to, type and (if type === 'popstate') delta properties. Values are null when no navigation is occurring, or during server rendering.

A read-only reactive object with information about the current page, serving several use cases:

Changes to page are available exclusively with runes. (The legacy reactivity syntax will not reflect any changes)

On the server, values can only be read during rendering (in other words not in e.g. load functions). In the browser, the values can be read at any time.

A read-only reactive value that’s initially false. If version.pollInterval is a non-zero value, SvelteKit will poll for new versions of the app and update current to true when it detects one. updated.check() will force an immediate check, regardless of polling.

A read-only object representing an in-progress navigation, with from, to, type and (if type === 'popstate') delta properties. Values are null when no navigation is occurring, or during server rendering.

A read-only reactive object with information about the current page, serving several use cases:

Changes to page are available exclusively with runes. (The legacy reactivity syntax will not reflect any changes)

On the server, values can only be read during rendering (in other words not in e.g. load functions). In the browser, the values can be read at any time.

A read-only reactive value that’s initially false. If version.pollInterval is a non-zero value, SvelteKit will poll for new versions of the app and update current to true when it detects one. updated.check() will force an immediate check, regardless of polling.

Edit this page on GitHub llms.txt

**Examples**:

```python
import { const navigating: Navigation | {
    from: null;
    to: null;
    type: null;
    willUnload: null;
    delta: null;
    complete: null;
}A read-only object representing an in-progress navigation, with from, to, type and (if type === 'popstate') delta properties.
Values are null when no navigation is occurring, or during server rendering.
navigating, const page: Page<Record<string, string>, string | null>A read-only reactive object with information about the current page, serving sever
...
```

```javascript
const navigating: Navigation | {
    from: null;
    to: null;
    type: null;
    willUnload: null;
    delta: null;
    complete: null;
}
```

```javascript
const navigating: Navigation | {
    from: null;
    to: null;
    type: null;
    willUnload: null;
    delta: null;
    complete: null;
}
```

---

## $app/types

**URL**: https://svelte.dev/docs/kit/$app-types

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- $app/types

This module contains generated types for the routes in your app.

A union of all the route IDs in your app. Used for page.route.id and event.route.id.

A utility for getting the parameters associated with a given route.

A utility for getting the parameters associated with a given layout, which is similar to RouteParams but also includes optional parameters for any child route.

A union of all the filenames of assets contained in your static directory, plus a string wildcard for asset paths generated from import declarations.

A union of all the route IDs in your app. Used for page.route.id and event.route.id.

A union of all valid pathnames in your app.

Similar to Pathname, but possibly prefixed with a base path. Used for page.url.pathname.

A utility for getting the parameters associated with a given route.

A utility for getting the parameters associated with a given layout, which is similar to RouteParams but also includes optional parameters for any child route.

Edit this page on GitHub llms.txt

**Examples**:

```python
import type { type RouteId = stringA union of all the route IDs in your app. Used for page.route.id and event.route.id.
RouteId, type RouteParams<T extends RouteId> = T extends string ? Record<string, string> : Record<string, never>A utility for getting the parameters associated with a given route.
RouteParams, type LayoutParams<T extends RouteId> = T extends string ? Record<string, string> : Record<string, never>A utility for getting the parameters associated with a given layout, which is simil
...
```

```text
type RouteId = string
```

```text
page.route.id
```

---

## {@attach ...}

**URL**: https://svelte.dev/docs/svelte/@attach

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

Attachments are functions that run in an effect when an element is mounted to the DOM or when state read inside the function updates.

Optionally, they can return a function that is called before the attachment re-runs, or after the element is later removed from the DOM.

Attachments are available in Svelte 5.29 and newer.

An element can have any number of attachments.

A useful pattern is for a function, such as tooltip in this example, to return an attachment (demo):

Since the tooltip(content) expression runs inside an effect, the attachment will be destroyed and recreated whenever content changes. The same thing would happen for any state read inside the attachment function when it first runs. (If this isn’t what you want, see Controlling when attachments re-run.)

Attachments can also be created inline (demo):

The nested effect runs whenever color changes, while the outer effect (where canvas.getContext(...) is called) only runs once, since it doesn’t read any reactive state.

When used on a component, {@attach ...} will create a prop whose key is a Symbol. If the component then spreads props onto an element, the element will receive those attachments.

This allows you to create wrapper components that augment elements (demo):

Attachments, unlike actions, are fully reactive: {@attach foo(bar)} will re-run on changes to foo or bar (or any state read inside foo):

In the rare case that this is a problem (for example, if foo does expensive and unavoidable setup work) consider passing the data inside a function and reading it in a child effect:

Runs code when a component is mounted to the DOM, and then whenever its dependencies change, i.e. $state or $derived values. The timing of the execution is after the DOM has been updated.

If you return a function from the effect, it will be called right before the effect is run again, or when the component is unmounted.

Does not run during server-side rendering.

https://svelte.dev/docs/svelte/$effect

To add attachmen

*[Content truncated - see full docs]*

**Examples**:

```javascript
<script>
	/** @type {import('svelte/attachments').Attachment} */
	function myAttachment(element) {
		console.log(element.nodeName); // 'DIV'

		return () => {
			console.log('cleaning up');
		};
	}
</script>

<div {@attach myAttachment}>...</div>
```

```python
<script lang="ts">
	import type { Attachment } from 'svelte/attachments';

	const myAttachment: Attachment = (element) => {
		console.log(element.nodeName); // 'DIV'

		return () => {
			console.log('cleaning up');
		};
	};
</script>

<div {@attach myAttachment}>...</div>
```

```python
<script>
	import tippy from 'tippy.js';

	let content = $state('Hello!');

	/**
	 * @param {string} content
	 * @returns {import('svelte/attachments').Attachment}
	 */
	function tooltip(content) {
		return (element) => {
			const tooltip = tippy(element, { content });
			return tooltip.destroy;
		};
	}
</script>

<input bind:value={content} />

<button {@attach tooltip(content)}>
	Hover me
</button>
```

---

## {#await ...}

**URL**: https://svelte.dev/docs/svelte/await

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

Await blocks allow you to branch on the three possible states of a Promise — pending, fulfilled or rejected.

During server-side rendering, only the pending branch will be rendered.

If the provided expression is not a Promise, only the :then branch will be rendered, including during server-side rendering.

The catch block can be omitted if you don’t need to render anything when the promise rejects (or no error is possible).

If you don’t care about the pending state, you can also omit the initial block.

Similarly, if you only want to show the error state, you can omit the then block.

You can use #await with import(...) to render components lazily:

Edit this page on GitHub llms.txt

**Examples**:

```text
{#await expression}...{:then name}...{:catch name}...{/await}
```

```text
{#await expression}...{:then name}...{/await}
```

```text
{#await expression then name}...{/await}
```

---

## await

**URL**: https://svelte.dev/docs/svelte/await-expressions

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

As of Svelte 5.36, you can use the await keyword inside your components in three places where it was previously unavailable:

This feature is currently experimental, and you must opt in by adding the experimental.async option wherever you configure Svelte, usually svelte.config.js:

The experimental flag will be removed in Svelte 6.

When an await expression depends on a particular piece of state, changes to that state will not be reflected in the UI until the asynchronous work has completed, so that the UI is not left in an inconsistent state. In other words, in an example like this...

...if you increment a, the contents of the <p> will not immediately update to read this —

— instead, the text will update to 2 + 2 = 4 when add(a, b) resolves.

Updates can overlap — a fast update will be reflected in the UI while an earlier slow update is still ongoing.

Svelte will do as much asynchronous work as it can in parallel. For example if you have two await expressions in your markup...

...both functions will run at the same time, as they are independent expressions, even though they are visually sequential.

This does not apply to sequential await expressions inside your <script> or inside async functions — these run like any other asynchronous JavaScript. An exception is that independent $derived expressions will update independently, even though they will run sequentially when they are first created:

Declares derived state, i.e. one that depends on other state variables. The expression inside $derived(...) should be free of side-effects.

https://svelte.dev/docs/svelte/$derived

Declares derived state, i.e. one that depends on other state variables. The expression inside $derived(...) should be free of side-effects.

https://svelte.dev/docs/svelte/$derived

If you write code like this, expect Svelte to give you an await_waterfall warning

To render placeholder UI, you can wrap content in a <svelte:boundary> with a pending snippet. This will be shown when the boundar

*[Content truncated - see full docs]*

**Examples**:

```typescript
export default {
	compilerOptions: {
    experimental: {
        async: boolean;
    };
}compilerOptions: {
		experimental: {
    async: boolean;
}experimental: {
			async: booleanasync: true
		}
	}
};
```

```text
compilerOptions: {
    experimental: {
        async: boolean;
    };
}
```

```text
compilerOptions: {
    experimental: {
        async: boolean;
    };
}
```

---

## bind:

**URL**: https://svelte.dev/docs/svelte/bind

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

Data ordinarily flows down, from parent to child. The bind: directive allows data to flow the other way, from child to parent.

The general syntax is bind:property={expression}, where expression is an lvalue (i.e. a variable or an object property). When the expression is an identifier with the same name as the property, we can omit the expression — in other words these are equivalent:

Svelte creates an event listener that updates the bound value. If an element already has a listener for the same event, that listener will be fired before the bound value is updated.

Most bindings are two-way, meaning that changes to the value will affect the element and vice versa. A few bindings are readonly, meaning that changing their value will have no effect on the element.

You can also use bind:property={get, set}, where get and set are functions, allowing you to perform validation and transformation:

In the case of readonly bindings like dimension bindings, the get value should be null:

Function bindings are available in Svelte 5.9.0 and newer.

A bind:value directive on an <input> element binds the input’s value property:

In the case of a numeric input (type="number" or type="range"), the value will be coerced to a number (demo):

If the input is empty or invalid (in the case of type="number"), the value is undefined.

Since 5.6.0, if an <input> has a defaultValue and is part of a form, it will revert to that value instead of the empty string when the form is reset. Note that for the initial render the value of the binding takes precedence unless it is null or undefined.

Use reset buttons sparingly, and ensure that users won’t accidentally click them while trying to submit the form.

Checkbox inputs can be bound with bind:checked:

Since 5.6.0, if an <input> has a defaultChecked attribute and is part of a form, it will revert to that value instead of false when the form is reset. Note that for the initial render the value of the binding takes precedence unless it is nul

*[Content truncated - see full docs]*

**Examples**:

```text
<input bind:value={value} />
<input bind:value />
```

```javascript
<input bind:value={
	() => value,
	(v) => value = v.toLowerCase()}
/>
```

```text
<div
	bind:clientWidth={null, redraw}
	bind:clientHeight={null, redraw}
>...</div>
```

---

## $bindable

**URL**: https://svelte.dev/docs/svelte/$bindable

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

Ordinarily, props go one way, from parent to child. This makes it easy to understand how data flows around your app.

In Svelte, component props can be bound, which means that data can also flow up from child to parent. This isn’t something you should do often, but it can simplify your code if used sparingly and carefully.

It also means that a state proxy can be mutated in the child.

Mutation is also possible with normal props, but is strongly discouraged — Svelte will warn you if it detects that a component is mutating state it does not ‘own’.

To mark a prop as bindable, we use the $bindable rune:

Now, a component that uses <FancyInput> can add the bind: directive (demo):

The parent component doesn’t have to use bind: — it can just pass a normal prop. Some parents don’t want to listen to what their children have to say.

In this case, you can specify a fallback value for when no prop is passed at all:

Declares a prop as bindable, meaning the parent component can use bind:propName={value} to bind to it.

https://svelte.dev/docs/svelte/$bindable

Declares the props that a component accepts. Example:

https://svelte.dev/docs/svelte/$props

Edit this page on GitHub llms.txt

**Examples**:

```javascript
<script>
	let { value = $bindable(), ...props } = $props();
</script>

<input bind:value={value} {...props} />

<style>
	input {
		font-family: 'Comic Sans MS';
		color: deeppink;
	}
</style>
```

```javascript
<script lang="ts">
	let { value = $bindable(), ...props } = $props();
</script>

<input bind:value={value} {...props} />

<style>
	input {
		font-family: 'Comic Sans MS';
		color: deeppink;
	}
</style>
```

```python
<script>
	import FancyInput from './FancyInput.svelte';

	let message = $state('hello');
</script>

<FancyInput bind:value={message} />
<p>{message}</p>
```

---

## class

**URL**: https://svelte.dev/docs/svelte/class

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

There are two ways to set classes on elements: the class attribute, and the class: directive.

Primitive values are treated like any other attribute:

For historical reasons, falsy values (like false and NaN) are stringified (class="false"), though class={undefined} (or null) cause the attribute to be omitted altogether. In a future version of Svelte, all falsy values will cause class to be omitted.

Since Svelte 5.16, class can be an object or array, and is converted to a string using clsx.

If the value is an object, the truthy keys are added:

If the value is an array, the truthy values are combined:

Note that whether we’re using the array or object form, we can set multiple classes simultaneously with a single condition, which is particularly useful if you’re using things like Tailwind.

Arrays can contain arrays and objects, and clsx will flatten them. This is useful for combining local classes with props, for example:

The user of this component has the same flexibility to use a mixture of objects, arrays and strings:

Since Svelte 5.19, Svelte also exposes the ClassValue type, which is the type of value that the class attribute on elements accept. This is useful if you want to use a type-safe class name in component props:

Prior to Svelte 5.16, the class: directive was the most convenient way to set classes on elements conditionally.

As with other directives, we can use a shorthand when the name of the class coincides with the value:

Unless you’re using an older version of Svelte, consider avoiding class:, since the attribute is more powerful and composable.

Edit this page on GitHub llms.txt

**Examples**:

```text
<div class={large ? 'large' : 'small'}>...</div>
```

```javascript
<script>
	let { cool } = $props();
</script>

<!-- results in `class="cool"` if `cool` is truthy,
	 `class="lame"` otherwise -->
<div class={{ cool, lame: !cool }}>...</div>
```

```text
<!-- if `faded` and `large` are both truthy, results in
	 `class="saturate-0 opacity-50 scale-200"` -->
<div class={[faded && 'saturate-0 opacity-50', large && 'scale-200']}>...</div>
```

---

## {@const ...}

**URL**: https://svelte.dev/docs/svelte/@const

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

The {@const ...} tag defines a local constant.

{@const} is only allowed as an immediate child of a block — {#if ...}, {#each ...}, {#snippet ...} and so on — a <Component /> or a <svelte:boundary>.

Edit this page on GitHub llms.txt

**Examples**:

```javascript
{#each boxes as box}
	{@const area = box.width * box.height}
	{box.width} * {box.height} = {area}
{/each}
```

---

## {@debug ...}

**URL**: https://svelte.dev/docs/svelte/@debug

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

The {@debug ...} tag offers an alternative to console.log(...). It logs the values of specific variables whenever they change, and pauses code execution if you have devtools open.

{@debug ...} accepts a comma-separated list of variable names (not arbitrary expressions).

The {@debug} tag without any arguments will insert a debugger statement that gets triggered when any state changes, as opposed to the specified variables.

Edit this page on GitHub llms.txt

**Examples**:

```javascript
<script>
	let user = {
		firstname: 'Ada',
		lastname: 'Lovelace'
	};
</script>

{@debug user}

<h1>Hello {user.firstname}!</h1>
```

```text
<!-- Compiles -->
{@debug user}
{@debug user1, user2, user3}

<!-- WON'T compile -->
{@debug user.firstname}
{@debug myArray[0]}
{@debug !isReady}
{@debug typeof user === 'object'}
```

---

## $derived

**URL**: https://svelte.dev/docs/svelte/$derived

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

Derived state is declared with the $derived rune:

The expression inside $derived(...) should be free of side-effects. Svelte will disallow state changes (e.g. count++) inside derived expressions.

As with $state, you can mark class fields as $derived.

Code in Svelte components is only executed once at creation. Without the $derived rune, doubled would maintain its original value even when count changes.

Sometimes you need to create complex derivations that don’t fit inside a short expression. In these cases, you can use $derived.by which accepts a function as its argument.

In essence, $derived(expression) is equivalent to $derived.by(() => expression).

Anything read synchronously inside the $derived expression (or $derived.by function body) is considered a dependency of the derived state. When the state changes, the derived will be marked as dirty and recalculated when it is next read.

To exempt a piece of state from being treated as a dependency, use untrack.

Derived expressions are recalculated when their dependencies change, but you can temporarily override their values by reassigning them (unless they are declared with const). This can be useful for things like optimistic UI, where a value is derived from the ‘source of truth’ (such as data from your server) but you’d like to show immediate feedback to the user:

Prior to Svelte 5.25, deriveds were read-only.

Unlike $state, which converts objects and arrays to deeply reactive proxies, $derived values are left as-is. For example, in a case like this...

Declares reactive state.

https://svelte.dev/docs/svelte/$state

Declares reactive state.

https://svelte.dev/docs/svelte/$state

Declares derived state, i.e. one that depends on other state variables. The expression inside $derived(...) should be free of side-effects.

https://svelte.dev/docs/svelte/$derived

...you can change (or bind: to) properties of selected and it will affect the underlying items array. If items was not deeply reactive, mutating sel

*[Content truncated - see full docs]*

**Examples**:

```javascript
<script>
	let count = $state(0);
	let doubled = $derived(count * 2);
</script>

<button onclick={() => count++}>
	{doubled}
</button>

<p>{count} doubled is {doubled}</p>
```

```javascript
<script>
	let numbers = $state([1, 2, 3]);
	let total = $derived.by(() => {
		let total = 0;
		for (const n of numbers) {
			total += n;
		}
		return total;
	});
</script>

<button onclick={() => numbers.push(numbers.length + 1)}>
	{numbers.join(' + ')} = {total}
</button>
```

```javascript
<script>
	let { post, like } = $props();

	let likes = $derived(post.likes);

	async function onclick() {
		// increment the `likes` count immediately...
		likes += 1;

		// and tell the server, which will eventually update `post`
		try {
			await like();
		} catch {
			// failed! roll back the change
			likes -= 1;
		}
	}
</script>

<button {onclick}>🧡 {likes}</button>
```

---

## {#each ...}

**URL**: https://svelte.dev/docs/svelte/each

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

Iterating over values can be done with an each block. The values in question can be arrays, array-like objects (i.e. anything with a length property), or iterables like Map and Set — in other words, anything that can be used with Array.from.

An each block can also specify an index, equivalent to the second argument in an array.map(...) callback:

If a key expression is provided — which must uniquely identify each list item — Svelte will use it to intelligently update the list when data changes by inserting, moving and deleting items, rather than adding or removing items at the end and updating the state in the middle.

The key can be any object, but strings and numbers are recommended since they allow identity to persist when the objects themselves change.

You can freely use destructuring and rest patterns in each blocks.

In case you just want to render something n times, you can omit the as part (demo):

An each block can also have an {:else} clause, which is rendered if the list is empty.

Edit this page on GitHub llms.txt

**Examples**:

```text
{#each expression as name}...{/each}
```

```text
{#each expression as name, index}...{/each}
```

```text
<h1>Shopping list</h1>
<ul>
	{#each items as item}
		<li>{item.name} x {item.qty}</li>
	{/each}
</ul>
```

---

## $effect

**URL**: https://svelte.dev/docs/svelte/$effect

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

Effects are functions that run when state updates, and can be used for things like calling third-party libraries, drawing on <canvas> elements, or making network requests. They only run in the browser, not during server-side rendering.

Generally speaking, you should not update state inside effects, as it will make code more convoluted and will often lead to never-ending update cycles. If you find yourself doing so, see when not to use $effect to learn about alternative approaches.

You can create an effect with the $effect rune (demo):

When Svelte runs an effect function, it tracks which pieces of state (and derived state) are accessed (unless accessed inside untrack), and re-runs the function when that state later changes.

If you’re having difficulty understanding why your $effect is rerunning or is not running see understanding dependencies. Effects are triggered differently than the $: blocks you may be used to if coming from Svelte 4.

Your effects run after the component has been mounted to the DOM, and in a microtask after state changes. Re-runs are batched (i.e. changing color and size in the same moment won’t cause two separate runs), and happen after any DOM updates have been applied.

You can use $effect anywhere, not just at the top level of a component, as long as it is called while a parent effect is running.

Svelte uses effects internally to represent logic and expressions in your template — this is how <h1>hello {name}!</h1> updates when name changes.

An effect can return a teardown function which will run immediately before the effect re-runs (demo).

Teardown functions also run when the effect is destroyed, which happens when its parent is destroyed (for example, a component is unmounted) or the parent effect re-runs.

$effect automatically picks up any reactive values ($state, $derived, $props) that are synchronously read inside its function body (including indirectly, via function calls) and registers them as dependencies. When those dependen

*[Content truncated - see full docs]*

**Examples**:

```javascript
<script>
	let size = $state(50);
	let color = $state('#ff3e00');

	let canvas;

	$effect(() => {
		const context = canvas.getContext('2d');
		context.clearRect(0, 0, canvas.width, canvas.height);

		// this will re-run whenever `color` or `size` change
		context.fillStyle = color;
		context.fillRect(0, 0, size, size);
	});
</script>

<canvas bind:this={canvas} width="100" height="100"></canvas>
```

```javascript
<script>
	let count = $state(0);
	let milliseconds = $state(1000);

	$effect(() => {
		// This will be recreated whenever `milliseconds` changes
		const interval = setInterval(() => {
			count += 1;
		}, milliseconds);

		return () => {
			// if a teardown function is provided, it will run
			// a) immediately before the effect re-runs
			// b) when the component is destroyed
			clearInterval(interval);
		};
	});
</script>

<h1>{count}</h1>

<button onclick={() => (milliseconds *= 2)}>slower</bu
...
```

```javascript
function $effect(fn: () => void | (() => void)): void
namespace $effectRuns code when a component is mounted to the DOM, and then whenever its dependencies change, i.e. $state or $derived values.
The timing of the execution is after the DOM has been updated.
Example:
$effect(() => console.log('The count is now ' + count));If you return a function from the effect, it will be called right before the effect is run again, or when the component is unmounted.
Does not run during server-side rendering.
...
```

---

## $env/dynamic/private

**URL**: https://svelte.dev/docs/kit/$env-dynamic-private

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- $env/dynamic/private

This module provides access to runtime environment variables, as defined by the platform you’re running on. For example if you’re using adapter-node (or running vite preview), this is equivalent to process.env. This module only includes variables that do not begin with config.kit.env.publicPrefix and do start with config.kit.env.privatePrefix (if configured).

This module cannot be imported into client-side code.

The console module provides a simple debugging console that is similar to the JavaScript console mechanism provided by web browsers.

The module exports two specific components:

Warning: The global console object’s methods are neither consistently synchronous like the browser APIs they resemble, nor are they consistently asynchronous like all other Node.js streams. See the note on process I/O for more information.

Example using the global console:

Example using the Console class:

Prints to stdout with newline. Multiple arguments can be passed, with the first used as the primary message and all additional used as substitution values similar to printf(3) (the arguments are all passed to util.format()).

See util.format() for more information.

In dev, $env/dynamic always includes environment variables from .env. In prod, this behavior will depend on your adapter.

Edit this page on GitHub llms.txt

**Examples**:

```python
import { import envenv } from '$env/dynamic/private';
var console: ConsoleThe console module provides a simple debugging console that is similar to the
JavaScript console mechanism provided by web browsers.
The module exports two specific components:

A Console class with methods such as console.log(), console.error() and console.warn() that can be used to write to any Node.js stream.
A global console instance configured to write to process.stdout and
process.stderr. The global console can be us
...
```

```text
var console: Console
```

```text
console.log()
```

---

## $env/dynamic/public

**URL**: https://svelte.dev/docs/kit/$env-dynamic-public

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- $env/dynamic/public

Similar to $env/dynamic/private, but only includes variables that begin with config.kit.env.publicPrefix (which defaults to PUBLIC_), and can therefore safely be exposed to client-side code.

Note that public dynamic environment variables must all be sent from the server to the client, causing larger network requests — when possible, use $env/static/public instead.

The console module provides a simple debugging console that is similar to the JavaScript console mechanism provided by web browsers.

The module exports two specific components:

Warning: The global console object’s methods are neither consistently synchronous like the browser APIs they resemble, nor are they consistently asynchronous like all other Node.js streams. See the note on process I/O for more information.

Example using the global console:

Example using the Console class:

Prints to stdout with newline. Multiple arguments can be passed, with the first used as the primary message and all additional used as substitution values similar to printf(3) (the arguments are all passed to util.format()).

See util.format() for more information.

Edit this page on GitHub llms.txt

**Examples**:

```python
import { import envenv } from '$env/dynamic/public';
var console: ConsoleThe console module provides a simple debugging console that is similar to the
JavaScript console mechanism provided by web browsers.
The module exports two specific components:

A Console class with methods such as console.log(), console.error() and console.warn() that can be used to write to any Node.js stream.
A global console instance configured to write to process.stdout and
process.stderr. The global console can be use
...
```

```text
var console: Console
```

```text
console.log()
```

---

## $env/static/private

**URL**: https://svelte.dev/docs/kit/$env-static-private

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- $env/static/private

Environment variables loaded by Vite from .env files and process.env. Like $env/dynamic/private, this module cannot be imported into client-side code. This module only includes variables that do not begin with config.kit.env.publicPrefix and do start with config.kit.env.privatePrefix (if configured).

Unlike $env/dynamic/private, the values exported from this module are statically injected into your bundle at build time, enabling optimisations like dead code elimination.

Note that all environment variables referenced in your code should be declared (for example in an .env file), even if they don’t have a value until the app is deployed:

You can override .env values from the command line like so:

Edit this page on GitHub llms.txt

**Examples**:

```python
import { import API_KEYAPI_KEY } from '$env/static/private';
```

```text
import API_KEY
```

```text
MY_FEATURE_FLAG=""
```

---

## $env/static/public

**URL**: https://svelte.dev/docs/kit/$env-static-public

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- $env/static/public

Similar to $env/static/private, except that it only includes environment variables that begin with config.kit.env.publicPrefix (which defaults to PUBLIC_), and can therefore safely be exposed to client-side code.

Values are replaced statically at build time.

Edit this page on GitHub llms.txt

**Examples**:

```python
import { import PUBLIC_BASE_URLPUBLIC_BASE_URL } from '$env/static/public';
```

```text
import PUBLIC_BASE_URL
```

---

## export let

**URL**: https://svelte.dev/docs/svelte/legacy-export-let

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

In runes mode, component props are declared with the $props rune, allowing parent components to pass in data.

In legacy mode, props are marked with the export keyword, and can have a default value:

The default value is used if it would otherwise be undefined when the component is created.

Unlike in runes mode, if the parent component changes a prop from a defined value to undefined, it does not revert to the initial value.

Props without default values are considered required, and Svelte will print a warning during development if no value is provided, which you can squelch by specifying undefined as the default value:

An exported const, class or function declaration is not considered a prop — instead, it becomes part of the component’s API:

The export keyword can appear separately from the declaration. This is useful for renaming props, for example in the case of a reserved word:

Edit this page on GitHub llms.txt

**Examples**:

```javascript
<script>
	export let foo;
	export let bar = 'default value';

	// Values that are passed in as props
	// are immediately available
	console.log({ foo });
</script>
```

```javascript
export let let foo: undefinedfoo = var undefinedundefined;
```

```javascript
let foo: undefined
```

---

## $host

**URL**: https://svelte.dev/docs/svelte/$host

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

When compiling a component as a custom element, the $host rune provides access to the host element, allowing you to (for example) dispatch custom events (demo):

Edit this page on GitHub llms.txt

**Examples**:

```javascript
<svelte:options customElement="my-stepper" />

<script>
	function dispatch(type) {
		$host().dispatchEvent(new CustomEvent(type));
	}
</script>

<button onclick={() => dispatch('decrement')}>decrement</button>
<button onclick={() => dispatch('increment')}>increment</button>
```

```javascript
<svelte:options customElement="my-stepper" />

<script lang="ts">
	function dispatch(type) {
		$host().dispatchEvent(new CustomEvent(type));
	}
</script>

<button onclick={() => dispatch('decrement')}>decrement</button>
<button onclick={() => dispatch('increment')}>increment</button>
```

```javascript
<script>
	import './Stepper.svelte';

	let count = $state(0);
</script>

<my-stepper
	ondecrement={() => count -= 1}
	onincrement={() => count += 1}
></my-stepper>

<p>count: {count}</p>
```

---

## {@html ...}

**URL**: https://svelte.dev/docs/svelte/@html

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

To inject raw HTML into your component, use the {@html ...} tag:

Make sure that you either escape the passed string or only populate it with values that are under your control in order to prevent XSS attacks. Never render unsanitized content.

The expression should be valid standalone HTML — this will not work, because </div> is not valid HTML:

It also will not compile Svelte code.

Content rendered this way is ‘invisible’ to Svelte and as such will not receive scoped styles. In other words, this will not work, and the a and img styles will be regarded as unused:

Instead, use the :global modifier to target everything inside the <article>:

Edit this page on GitHub llms.txt

**Examples**:

```text
<article>
	{@html content}
</article>
```

```text
{@html '<div>'}content{@html '</div>'}
```

```text
<article>
	{@html content}
</article>

<style>
	article {
		a { color: hotpink }
		img { width: 100% }
	}
</style>
```

---

## {#if ...}

**URL**: https://svelte.dev/docs/svelte/if

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

Content that is conditionally rendered can be wrapped in an if block.

Additional conditions can be added with {:else if expression}, optionally ending in an {:else} clause.

(Blocks don’t have to wrap elements, they can also wrap text within elements.)

Edit this page on GitHub llms.txt

**Examples**:

```text
{#if expression}...{/if}
```

```text
{#if expression}...{:else if expression}...{/if}
```

```text
{#if expression}...{:else}...{/if}
```

---

## in: and out:

**URL**: https://svelte.dev/docs/svelte/in-and-out

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

The in: and out: directives are identical to transition:, except that the resulting transitions are not bidirectional — an in transition will continue to ‘play’ alongside the out transition, rather than reversing, if the block is outroed while the transition is in progress. If an out transition is aborted, transitions will restart from scratch.

Edit this page on GitHub llms.txt

**Examples**:

```python
<script>
  import { fade, fly } from 'svelte/transition';
  
  let visible = $state(false);
</script>

<label>
  <input type="checkbox" bind:checked={visible}>
  visible
</label>

{#if visible}
	<div in:fly={{ y: 200 }} out:fade>flies in, fades out</div>
{/if}
```

---

## $inspect

**URL**: https://svelte.dev/docs/svelte/$inspect

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

$inspect only works during development. In a production build it becomes a noop.

The $inspect rune is roughly equivalent to console.log, with the exception that it will re-run whenever its argument changes. $inspect tracks reactive state deeply, meaning that updating something inside an object or array using fine-grained reactivity will cause it to re-fire (demo):

$inspect returns a property with, which you can invoke with a callback, which will then be invoked instead of console.log. The first argument to the callback is either "init" or "update"; subsequent arguments are the values passed to $inspect (demo):

A convenient way to find the origin of some change is to pass console.trace to with:

Inspects one or more values whenever they, or the properties they contain, change. Example:

$inspect returns a with function, which you can invoke with a callback function that will be called with the value and the event type ('init' or 'update') on every change. By default, the values will be logged to the console.

https://svelte.dev/docs/svelte/$inspect

The console module provides a simple debugging console that is similar to the JavaScript console mechanism provided by web browsers.

The module exports two specific components:

Warning: The global console object’s methods are neither consistently synchronous like the browser APIs they resemble, nor are they consistently asynchronous like all other Node.js streams. See the note on process I/O for more information.

Example using the global console:

Example using the Console class:

This rune, added in 5.14, causes the surrounding function to be traced in development. Any time the function re-runs as part of an effect or a derived, information will be printed to the console about which pieces of reactive state caused the effect to fire.

$inspect.trace takes an optional first argument which will be used as the label.

Edit this page on GitHub llms.txt

**Examples**:

```javascript
<script>
	let count = $state(0);
	let message = $state('hello');

	$inspect(count, message); // will console.log when `count` or `message` change
</script>

<button onclick={() => count++}>Increment</button>
<input bind:value={message} />
```

```javascript
<script>
	let count = $state(0);

	$inspect(count).with((type, count) => {
		if (type === 'update') {
			debugger; // or `console.trace`, or whatever you want
		}
	});
</script>

<button onclick={() => count++}>Increment</button>
```

```javascript
function $inspect<[any]>(values_0: any): {
    with: (fn: (type: "init" | "update", values_0: any) => void) => void;
}
namespace $inspectInspects one or more values whenever they, or the properties they contain, change. Example:
$inspect(someValue, someOtherValue)$inspect returns a with function, which you can invoke with a callback function that
will be called with the value and the event type ('init' or 'update') on every change.
By default, the values will be logged to the console.
$inspect(x
...
```

---

## {#key ...}

**URL**: https://svelte.dev/docs/svelte/key

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

Key blocks destroy and recreate their contents when the value of an expression changes. When used around components, this will cause them to be reinstantiated and reinitialised:

It’s also useful if you want a transition to play whenever a value changes:

Edit this page on GitHub llms.txt

**Examples**:

```text
{#key expression}...{/key}
```

```text
{#key value}
	<Component />
{/key}
```

```text
{#key value}
	<div transition:fade>{value}</div>
{/key}
```

---

## $lib

**URL**: https://svelte.dev/docs/kit/$lib

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- $lib

SvelteKit automatically makes files under src/lib available using the $lib import alias. You can change which directory this alias points to in your config file.

Edit this page on GitHub llms.txt

**Examples**:

```text
A reusable component
```

```python
<script>
	import Component from '$lib/Component.svelte';
</script>

<Component />
```

```python
<script lang="ts">
	import Component from '$lib/Component.svelte';
</script>

<Component />
```

---

## on:

**URL**: https://svelte.dev/docs/svelte/legacy-on

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

In runes mode, event handlers are just like any other attribute or prop.

In legacy mode, we use the on: directive:

Handlers can be declared inline with no performance penalty:

Add modifiers to element event handlers with the | character.

The following modifiers are available:

Modifiers can be chained together, e.g. on:click|once|capture={...}.

If the on: directive is used without a value, the component will forward the event, meaning that a consumer of the component can listen for it.

It’s possible to have multiple event listeners for the same event:

Components can dispatch events by creating a dispatcher when they are initialised:

dispatch creates a CustomEvent. If a second argument is provided, it becomes the detail property of the event object.

A consumer of this component can listen for the dispatched events:

Component events do not bubble — a parent component can only listen for events on its immediate children.

Other than once, modifiers are not valid on component event handlers.

If you’re planning an eventual migration to Svelte 5, use callback props instead. This will make upgrading easier as createEventDispatcher is deprecated:

Edit this page on GitHub llms.txt

**Examples**:

```javascript
<script>
	let count = 0;

	/** @param {MouseEvent} event */
	function handleClick(event) {
		count += 1;
	}
</script>

<button on:click={handleClick}>
	count: {count}
</button>
```

```javascript
<script lang="ts">
	let count = 0;

	function handleClick(event: MouseEvent) {
		count += 1;
	}
</script>

<button on:click={handleClick}>
	count: {count}
</button>
```

```javascript
<button on:click={() => (count += 1)}>
	count: {count}
</button>
```

---

## $props

**URL**: https://svelte.dev/docs/svelte/$props

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

The inputs to a component are referred to as props, which is short for properties. You pass props to components just like you pass attributes to elements:

On the other side, inside MyComponent.svelte, we can receive props with the $props rune...

...though more commonly, you’ll destructure your props:

Destructuring allows us to declare fallback values, which are used if the parent component does not set a given prop (or the value is undefined):

Declares the props that a component accepts. Example:

https://svelte.dev/docs/svelte/$props

Fallback values are not turned into reactive state proxies (see Updating props for more info)

We can also use the destructuring assignment to rename props, which is necessary if they’re invalid identifiers, or a JavaScript keyword like super:

Declares the props that a component accepts. Example:

https://svelte.dev/docs/svelte/$props

Finally, we can use a rest property to get, well, the rest of the props:

Declares the props that a component accepts. Example:

https://svelte.dev/docs/svelte/$props

References to a prop inside a component update when the prop itself updates — when count changes in App.svelte, it will also change inside Child.svelte. But the child component is able to temporarily override the prop value, which can be useful for unsaved ephemeral state (demo):

While you can temporarily reassign props, you should not mutate props unless they are bindable.

If the prop is a regular object, the mutation will have no effect (demo):

If the prop is a reactive state proxy, however, then mutations will have an effect but you will see an ownership_invalid_mutation warning, because the component is mutating state that does not ‘belong’ to it (demo):

The fallback value of a prop not declared with $bindable is left untouched — it is not turned into a reactive state proxy — meaning mutations will not cause updates (demo)

In summary: don’t mutate props. Either use callback props to communicate changes, or — if parent and ch

*[Content truncated - see full docs]*

**Examples**:

```python
<script>
	import MyComponent from './MyComponent.svelte';
</script>

<MyComponent adjective="cool" />
```

```python
<script lang="ts">
	import MyComponent from './MyComponent.svelte';
</script>

<MyComponent adjective="cool" />
```

```javascript
<script>
	let props = $props();
</script>

<p>this component is {props.adjective}</p>
```

---

## $$props and $$restProps

**URL**: https://svelte.dev/docs/svelte/legacy-$$props-and-$$restProps

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

In runes mode, getting an object containing all the props that were passed in is easy, using the $props rune.

In legacy mode, we use $$props and $$restProps:

For example, a <Button> component might need to pass along all its props to its own <button> element, except the variant prop:

In Svelte 3/4 using $$props and $$restProps creates a modest performance penalty, so they should only be used when needed.

Edit this page on GitHub llms.txt

**Examples**:

```javascript
<script>
	export let variant;
</script>

<button {...$$restProps} class="variant-{variant} {$$props.class ?? ''}">
	click me
</button>

<style>
	.variant-danger {
		background: red;
	}
</style>
```

---

## {@render ...}

**URL**: https://svelte.dev/docs/svelte/@render

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

To render a snippet, use a {@render ...} tag.

The expression can be an identifier like sum, or an arbitrary JavaScript expression:

If the snippet is potentially undefined — for example, because it’s an incoming prop — then you can use optional chaining to only render it when it is defined:

Alternatively, use an {#if ...} block with an :else clause to render fallback content:

Edit this page on GitHub llms.txt

**Examples**:

```text
{#snippet sum(a, b)}
	<p>{a} + {b} = {a + b}</p>
{/snippet}

{@render sum(1, 2)}
{@render sum(3, 4)}
{@render sum(5, 6)}
```

```text
{@render (cool ? coolSnippet : lameSnippet)()}
```

```text
{@render children?.()}
```

---

## <slot>

**URL**: https://svelte.dev/docs/svelte/legacy-slots

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

In Svelte 5, content can be passed to components in the form of snippets and rendered using render tags.

In legacy mode, content inside component tags is considered slotted content, which can be rendered by the component using a <slot> element:

If you want to render a regular <slot> element, you can use <svelte:element this={'slot'} />.

A component can have named slots in addition to the default slot. On the parent side, add a slot="..." attribute to an element, component or <svelte:fragment> directly inside the component tags.

On the child side, add a corresponding <slot name="..."> element:

If no slotted content is provided, a component can define fallback content by putting it inside the <slot> element:

Slots can be rendered zero or more times and can pass values back to the parent using props. The parent exposes the values to the slot template using the let: directive.

The usual shorthand rules apply — let:item is equivalent to let:item={item}, and <slot {item}> is equivalent to <slot item={item}>.

Named slots can also expose values. The let: directive goes on the element with the slot attribute.

Edit this page on GitHub llms.txt

**Examples**:

```python
<script>
	import Modal from './Modal.svelte';
</script>

<Modal>This is some slotted content</Modal>
```

```python
<script lang="ts">
	import Modal from './Modal.svelte';
</script>

<Modal>This is some slotted content</Modal>
```

```text
<div class="modal">
	<slot></slot>
</div>
```

---

## $$slots

**URL**: https://svelte.dev/docs/svelte/legacy-$$slots

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

In runes mode, we know which snippets were provided to a component, as they’re just normal props.

In legacy mode, the way to know if content was provided for a given slot is with the $$slots object, whose keys are the names of the slots passed into the component by the parent.

Edit this page on GitHub llms.txt

**Examples**:

```text
<div>
	<slot name="title" />
	{#if $$slots.description}
		<!-- This <hr> and slot will render only if `slot="description"` is provided. -->
		<hr />
		<slot name="description" />
	{/if}
</div>
```

```text
<Card>
	<h1 slot="title">Blog Post Title</h1>
	<!-- No slot named "description" was provided so the optional slot will not be rendered. -->
</Card>
```

---

## {#snippet ...}

**URL**: https://svelte.dev/docs/svelte/snippet

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

Snippets, and render tags, are a way to create reusable chunks of markup inside your components. Instead of writing duplicative code like this...

...you can write this:

Like function declarations, snippets can have an arbitrary number of parameters, which can have default values, and you can destructure each parameter. You cannot use rest parameters, however.

Snippets can be declared anywhere inside your component. They can reference values declared outside themselves, for example in the <script> tag or in {#each ...} blocks (demo)...

...and they are ‘visible’ to everything in the same lexical scope (i.e. siblings, and children of those siblings):

Snippets can reference themselves and each other (demo):

Within the template, snippets are values just like any other. As such, they can be passed to components as props (demo):

Think about it like passing content instead of data to a component. The concept is similar to slots in web components.

As an authoring convenience, snippets declared directly inside a component implicitly become props on the component (demo):

Any content inside the component tags that is not a snippet declaration implicitly becomes part of the children snippet (demo):

Note that you cannot have a prop called children if you also have content inside the component — for this reason, you should avoid having props with that name

You can declare snippet props as being optional. You can either use optional chaining to not render anything if the snippet isn’t set...

...or use an #if block to render fallback content:

Snippets implement the Snippet interface imported from 'svelte':

With this change, red squigglies will appear if you try and use the component without providing a data prop and a row snippet. Notice that the type argument provided to Snippet is a tuple, since snippets can have multiple parameters.

We can tighten things up further by declaring a generic, so that data and row refer to the same type:

Snippets declared at the top le

*[Content truncated - see full docs]*

**Examples**:

```text
{#snippet name()}...{/snippet}
```

```text
{#snippet name(param1, param2, paramN)}...{/snippet}
```

```text
{#each images as image}
	{#if image.href}
		<a href={image.href}>
			<figure>
				<img src={image.src} alt={image.caption} width={image.width} height={image.height} />
				<figcaption>{image.caption}</figcaption>
			</figure>
		</a>
	{:else}
		<figure>
			<img src={image.src} alt={image.caption} width={image.width} height={image.height} />
			<figcaption>{image.caption}</figcaption>
		</figure>
	{/if}
{/each}
```

---

## $state

**URL**: https://svelte.dev/docs/svelte/$state

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

The $state rune allows you to create reactive state, which means that your UI reacts when it changes.

Unlike other frameworks you may have encountered, there is no API for interacting with state — count is just a number, rather than an object or a function, and you can update it like you would update any other variable.

If $state is used with an array or a simple object, the result is a deeply reactive state proxy. Proxies allow Svelte to run code when you read or write properties, including via methods like array.push(...), triggering granular updates.

State is proxified recursively until Svelte finds something other than an array or simple object (like a class or an object created with Object.create). In a case like this...

Declares reactive state.

https://svelte.dev/docs/svelte/$state

...modifying an individual todo’s property will trigger updates to anything in your UI that depends on that specific property:

If you push a new object to the array, it will also be proxified:

Appends new elements to the end of an array, and returns the new length of the array.

When you update properties of proxies, the original object is not mutated. If you need to use your own proxy handlers in a state proxy, you should wrap the object after wrapping it in $state.

Note that if you destructure a reactive value, the references are not reactive — as in normal JavaScript, they are evaluated at the point of destructuring:

Class instances are not proxied. Instead, you can use $state in class fields (whether public or private), or as the first assignment to a property immediately inside the constructor:

Declares reactive state.

https://svelte.dev/docs/svelte/$state

Declares reactive state.

https://svelte.dev/docs/svelte/$state

The compiler transforms done and text into get / set methods on the class prototype referencing private fields. This means the properties are not enumerable.

When calling methods in JavaScript, the value of this matters. This won’t work, because th

*[Content truncated - see full docs]*

**Examples**:

```javascript
<script>
	let count = $state(0);
</script>

<button onclick={() => count++}>
	clicks: {count}
</button>
```

```javascript
let let todos: {
    done: boolean;
    text: string;
}[]todos = function $state<{
    done: boolean;
    text: string;
}[]>(initial: {
    done: boolean;
    text: string;
}[]): {
    done: boolean;
    text: string;
}[] (+1 overload)
namespace $stateDeclares reactive state.
Example:
let count = $state(0);https://svelte.dev/docs/svelte/$state
@paraminitial The initial value$state([
	{
		done: booleandone: false,
		text: stringtext: 'add more todos'
	}
]);
```

```javascript
let todos: {
    done: boolean;
    text: string;
}[]
```

---

## style:

**URL**: https://svelte.dev/docs/svelte/style

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

The style: directive provides a shorthand for setting multiple styles on an element.

The value can contain arbitrary expressions:

The shorthand form is allowed:

Multiple styles can be set on a single element:

To mark a style as important, use the |important modifier:

When style: directives are combined with style attributes, the directives will take precedence, even over !important properties:

Edit this page on GitHub llms.txt

**Examples**:

```text
<!-- These are equivalent -->
<div style:color="red">...</div>
<div style="color: red;">...</div>
```

```text
<div style:color={myColor}>...</div>
```

```text
<div style:color>...</div>
```

---

## svelte

**URL**: https://svelte.dev/docs/svelte/svelte

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

This was the base class for Svelte components in Svelte 4. Svelte 5+ components are completely different under the hood. For typing, use Component instead. To instantiate components, use mount instead. See migration guide for more info.

Schedules a callback to run immediately after the component has been updated.

The first time the callback runs will be after the initial onMount.

In runes mode use $effect instead.

Schedules a callback to run immediately before the component is updated after any state change.

The first time the callback runs will be before the initial onMount.

In runes mode use $effect.pre instead.

Returns a [get, set] pair of functions for working with context in a type-safe way.

Creates an event dispatcher that can be used to dispatch component events. Event dispatchers are functions that can take two arguments: name and detail.

Component events created with createEventDispatcher create a CustomEvent. These events do not bubble. The detail argument corresponds to the CustomEvent.detail property and can contain any type of data.

The event dispatcher can be typed to narrow the allowed event names and the type of the detail argument:

Create a snippet programmatically

Synchronously flush any pending updates. Returns void if no callback is provided, otherwise returns the result of calling the callback.

Returns an AbortSignal that aborts when the current derived or effect re-runs or is destroyed.

Must be called while a derived or effect is running.

Retrieves the whole context map that belongs to the closest parent component. Must be called during component initialisation. Useful, for example, if you programmatically create a component and want to pass the existing context to it.

Retrieves the context that belongs to the closest parent component with the specified key. Must be called during component initialisation.

Checks whether a given key has been set in the context of a parent component. Must be called during component initialisation

*[Content truncated - see full docs]*

**Examples**:

```python
import {
	class SvelteComponent<Props extends Record<string, any> = Record<string, any>, Events extends Record<string, any> = any, Slots extends Record<string, any> = any>This was the base class for Svelte components in Svelte 4. Svelte 5+ components
are completely different under the hood. For typing, use Component instead.
To instantiate components, use mount instead.
See migration guide for more info.
SvelteComponent,
	class SvelteComponentTyped<Props extends Record<string, any> = Record<stri
...
```

```text
class SvelteComponent<Props extends Record<string, any> = Record<string, any>, Events extends Record<string, any> = any, Slots extends Record<string, any> = any>
```

```text
class SvelteComponentTyped<Props extends Record<string, any> = Record<string, any>, Events extends Record<string, any> = any, Slots extends Record<string, any> = any>
```

---

## .svelte files

**URL**: https://svelte.dev/docs/svelte/svelte-files

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

Components are the building blocks of Svelte applications. They are written into .svelte files, using a superset of HTML.

All three sections — script, styles and markup — are optional.

A <script> block contains JavaScript (or TypeScript, when adding the lang="ts" attribute) that runs when a component instance is created. Variables declared (or imported) at the top level can be referenced in the component’s markup.

In addition to normal JavaScript, you can use runes to declare component props and add reactivity to your component. Runes are covered in the next section.

A <script> tag with a module attribute runs once when the module first evaluates, rather than for each component instance. Variables declared in this block can be referenced elsewhere in the component, but not vice versa.

You can export bindings from this block, and they will become exports of the compiled module. You cannot export default, since the default export is the component itself.

If you are using TypeScript and import such exports from a module block into a .ts file, make sure to have your editor setup so that TypeScript knows about them. This is the case for our VS Code extension and the IntelliJ plugin, but in other cases you might need to setup our TypeScript editor plugin.

In Svelte 4, this script tag was created using <script context="module">

CSS inside a <style> block will be scoped to that component.

For more information, head to the section on styling.

Edit this page on GitHub llms.txt

**Examples**:

```vue
<script module>
	// module-level logic goes here
	// (you will rarely use this)
</script>

<script>
	// instance-level logic goes here
</script>

<!-- markup (zero or more items) goes here -->

<style>
	/* styles go here */
</style>
```

```text
<script module>
	// module-level logic goes here
	// (you will rarely use this)
</script>

<script lang="ts">
	// instance-level logic goes here
</script>

<!-- markup (zero or more items) goes here -->

<style>
	/* styles go here */
</style>
```

```javascript
<script module>
	let total = 0;
</script>

<script>
	total += 1;
	console.log(`instantiated ${total} times`);
</script>
```

---

## svelte/action

**URL**: https://svelte.dev/docs/svelte/svelte-action

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

This module provides types for actions, which have been superseded by attachments.

Actions are functions that are called when an element is created. You can use this interface to type such actions. The following example defines an action that only works on <div> elements and optionally accepts a parameter which it has a default value for:

Action<HTMLDivElement> and Action<HTMLDivElement, undefined> both signal that the action accepts no parameters.

You can return an object with methods update and destroy from the function and type which additional attributes and events it has. See interface ActionReturn for more details.

Actions can return an object containing the two properties defined in this interface. Both are optional.

Additionally, you can specify which additional attributes and events the action enables on the applied element. This applies to TypeScript typings only and has no effect at runtime.

Edit this page on GitHub llms.txt

**Examples**:

```javascript
export const const myAction: Action<HTMLDivElement, {
    someProperty: boolean;
} | undefined>myAction: type Action = /*unresolved*/ anyAction<HTMLDivElement, { someProperty: booleansomeProperty: boolean } | undefined> = (node: anynode, param: {
    someProperty: boolean;
}param = { someProperty: booleansomeProperty: true }) => {
	// ...
}
```

```javascript
const myAction: Action<HTMLDivElement, {
    someProperty: boolean;
} | undefined>
```

```javascript
const myAction: Action<HTMLDivElement, {
    someProperty: boolean;
} | undefined>
```

---

## svelte/animate

**URL**: https://svelte.dev/docs/svelte/svelte-animate

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

The flip function calculates the start and end position of an element and animates between them, translating the x and y values. flip stands for First, Last, Invert, Play.

The flip function calculates the start and end position of an element and animates between them, translating the x and y values. flip stands for First, Last, Invert, Play.

Edit this page on GitHub llms.txt

**Examples**:

```python
import { function flip(node: Element, { from, to }: {
    from: DOMRect;
    to: DOMRect;
}, params?: FlipParams): AnimationConfigThe flip function calculates the start and end position of an element and animates between them, translating the x and y values.
flip stands for First, Last, Invert, Play.
flip } from 'svelte/animate';
```

```javascript
function flip(node: Element, { from, to }: {
    from: DOMRect;
    to: DOMRect;
}, params?: FlipParams): AnimationConfig
```

```javascript
function flip(node: Element, { from, to }: {
    from: DOMRect;
    to: DOMRect;
}, params?: FlipParams): AnimationConfig
```

---

## svelte/attachments

**URL**: https://svelte.dev/docs/svelte/svelte-attachments

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

Creates an object key that will be recognised as an attachment when the object is spread onto an element, as a programmatic alternative to using {@attach ...}. This can be useful for library authors, though is generally not needed when building an app.

Converts an action into an attachment keeping the same behavior. It’s useful if you want to start using attachments on components but you have actions provided by a library.

Note that the second argument, if provided, must be a function that returns the argument to the action function, not the argument itself.

Creates an object key that will be recognised as an attachment when the object is spread onto an element, as a programmatic alternative to using {@attach ...}. This can be useful for library authors, though is generally not needed when building an app.

Converts an action into an attachment keeping the same behavior. It’s useful if you want to start using attachments on components but you have actions provided by a library.

Note that the second argument, if provided, must be a function that returns the argument to the action function, not the argument itself.

An attachment is a function that runs when an element is mounted to the DOM, and optionally returns a function that is called when the element is later removed.

It can be attached to an element with an {@attach ...} tag, or by spreading an object containing a property created with createAttachmentKey.

Edit this page on GitHub llms.txt

**Examples**:

```python
import { function createAttachmentKey(): symbolCreates an object key that will be recognised as an attachment when the object is spread onto an element,
as a programmatic alternative to using {@attach ...}. This can be useful for library authors, though
is generally not needed when building an app.
&#x3C;script>
	import { createAttachmentKey } from 'svelte/attachments';

	const props = {
		class: 'cool',
		onclick: () => alert('clicked'),
		[createAttachmentKey()]: (node) => {
			node.textConten
...
```

```javascript
function createAttachmentKey(): symbol
```

```text
{@attach ...}
```

---

## <svelte:body>

**URL**: https://svelte.dev/docs/svelte/svelte-body

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

Similarly to <svelte:window>, this element allows you to add listeners to events on document.body, such as mouseenter and mouseleave, which don’t fire on window. It also lets you use actions on the <body> element.

As with <svelte:window> and <svelte:document>, this element may only appear at the top level of your component and must never be inside a block or element.

Edit this page on GitHub llms.txt

**Examples**:

```text
<svelte:body onevent={handler} />
```

```text
<svelte:body onmouseenter={handleMouseenter} onmouseleave={handleMouseleave} use:someAction />
```

---

## <svelte:boundary>

**URL**: https://svelte.dev/docs/svelte/svelte-boundary

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

This feature was added in 5.3.0

Boundaries allow you to ‘wall off’ parts of your app, so that you can:

If a boundary handles an error (with a failed snippet or onerror handler, or both) its existing content will be removed.

Errors occurring outside the rendering process (for example, in event handlers or after a setTimeout or async work) are not caught by error boundaries.

For the boundary to do anything, one or more of the following must be provided.

This snippet will be shown when the boundary is first created, and will remain visible until all the await expressions inside the boundary have resolved (demo):

The pending snippet will not be shown for subsequent async updates — for these, you can use $effect.pending().

In the playground, your app is rendered inside a boundary with an empty pending snippet, so that you can use await without having to create one.

If a failed snippet is provided, it will be rendered when an error is thrown inside the boundary, with the error and a reset function that recreates the contents (demo):

As with snippets passed to components, the failed snippet can be passed explicitly as a property...

...or implicitly by declaring it directly inside the boundary, as in the example above.

If an onerror function is provided, it will be called with the same two error and reset arguments. This is useful for tracking the error with an error reporting service...

...or using error and reset outside the boundary itself:

If an error occurs inside the onerror function (or if you rethrow the error), it will be handled by a parent boundary if such exists.

Edit this page on GitHub llms.txt

**Examples**:

```text
<svelte:boundary onerror={handler}>...</svelte:boundary>
```

```text
<svelte:boundary>
	<p>{await delayed('hello!')}</p>

	{#snippet pending()}
		<p>loading...</p>
	{/snippet}
</svelte:boundary>
```

```text
<svelte:boundary>
	<FlakyComponent />

	{#snippet failed(error, reset)}
		<button onclick={reset}>oops! try again</button>
	{/snippet}
</svelte:boundary>
```

---

## svelte/compiler

**URL**: https://svelte.dev/docs/svelte/svelte-compiler

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

The current version, as set in package.json.

compile converts your .svelte source code into a JavaScript module that exports a component

compileModule takes your JavaScript source code containing runes, and turns it into a JavaScript module.

Does a best-effort migration of Svelte code towards using runes, event attributes and render tags. May throw an error if the code is too complex to migrate automatically.

The parse function parses a component, returning only its abstract syntax tree.

The modern option (false by default in Svelte 5) makes the parser return a modern AST instead of the legacy AST. modern will become true by default in Svelte 6, and the option will be removed in Svelte 7.

The preprocess function provides convenient hooks for arbitrarily transforming component source code. For example, it can be used to convert a &#x3C;style lang="sass"> block into vanilla CSS.

The current version, as set in package.json.

compile converts your .svelte source code into a JavaScript module that exports a component

compileModule takes your JavaScript source code containing runes, and turns it into a JavaScript module.

Does a best-effort migration of Svelte code towards using runes, event attributes and render tags. May throw an error if the code is too complex to migrate automatically.

The parse function parses a component, returning only its abstract syntax tree.

The modern option (false by default in Svelte 5) makes the parser return a modern AST instead of the legacy AST. modern will become true by default in Svelte 6, and the option will be removed in Svelte 7.

The preprocess function provides convenient hooks for arbitrarily transforming component source code. For example, it can be used to convert a <style lang="sass"> block into vanilla CSS.

Replace this with import { walk } from 'estree-walker'

Sets the name of the resulting JavaScript class (though the compiler will rename it if it would otherwise conflict with other variables in scope). If unspe

*[Content truncated - see full docs]*

**Examples**:

```python
import {
	const VERSION: stringThe current version, as set in package.json.
VERSION,
	function compile(source: string, options: CompileOptions): CompileResultcompile converts your .svelte source code into a JavaScript module that exports a component
@paramsource The component source code@paramoptions The compiler optionscompile,
	function compileModule(source: string, options: ModuleCompileOptions): CompileResultcompileModule takes your JavaScript source code containing runes, and turns it into 
...
```

```javascript
const VERSION: string
```

```javascript
function compile(source: string, options: CompileOptions): CompileResult
```

---

## <svelte:component>

**URL**: https://svelte.dev/docs/svelte/legacy-svelte-component

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

In runes mode, <MyComponent> will re-render if the value of MyComponent changes. See the Svelte 5 migration guide for an example.

In legacy mode, it won’t — we must use <svelte:component>, which destroys and recreates the component instance when the value of its this expression changes:

If this is falsy, no component is rendered.

Edit this page on GitHub llms.txt

**Examples**:

```text
<svelte:component this={MyComponent} />
```

---

## <svelte:document>

**URL**: https://svelte.dev/docs/svelte/svelte-document

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

Similarly to <svelte:window>, this element allows you to add listeners to events on document, such as visibilitychange, which don’t fire on window. It also lets you use actions on document.

As with <svelte:window>, this element may only appear the top level of your component and must never be inside a block or element.

You can also bind to the following properties:

Edit this page on GitHub llms.txt

**Examples**:

```text
<svelte:document onevent={handler} />
```

```text
<svelte:document bind:prop={value} />
```

```text
<svelte:document onvisibilitychange={handleVisibilityChange} use:someAction />
```

---

## svelte/easing

**URL**: https://svelte.dev/docs/svelte/svelte-easing

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

Edit this page on GitHub llms.txt

**Examples**:

```python
import {
	function backIn(t: number): numberbackIn,
	function backInOut(t: number): numberbackInOut,
	function backOut(t: number): numberbackOut,
	function bounceIn(t: number): numberbounceIn,
	function bounceInOut(t: number): numberbounceInOut,
	function bounceOut(t: number): numberbounceOut,
	function circIn(t: number): numbercircIn,
	function circInOut(t: number): numbercircInOut,
	function circOut(t: number): numbercircOut,
	function cubicIn(t: number): numbercubicIn,
	function cubicInOut(t:
...
```

```javascript
function backIn(t: number): number
```

```javascript
function backInOut(t: number): number
```

---

## <svelte:element>

**URL**: https://svelte.dev/docs/svelte/svelte-element

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

The <svelte:element> element lets you render an element that is unknown at author time, for example because it comes from a CMS. Any properties and event listeners present will be applied to the element.

The only supported binding is bind:this, since Svelte’s built-in bindings do not work with generic elements.

If this has a nullish value, the element and its children will not be rendered.

If this is the name of a void element (e.g., br) and <svelte:element> has child elements, a runtime error will be thrown in development mode:

Svelte tries its best to infer the correct namespace from the element’s surroundings, but it’s not always possible. You can make it explicit with an xmlns attribute:

this needs to be a valid DOM element tag, things like #text or svelte:head will not work.

Edit this page on GitHub llms.txt

**Examples**:

```text
<svelte:element this={expression} />
```

```javascript
<script>
	let tag = $state('hr');
</script>

<svelte:element this={tag}>
	This text cannot appear inside an hr element
</svelte:element>
```

```text
<svelte:element this={tag} xmlns="http://www.w3.org/2000/svg" />
```

---

## svelte/events

**URL**: https://svelte.dev/docs/svelte/svelte-events

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

Attaches an event handler to the window and returns a function that removes the handler. Using this rather than addEventListener will preserve the correct order relative to handlers added declaratively (with attributes like onclick), which use event delegation for performance reasons

Attaches an event handler to the window and returns a function that removes the handler. Using this rather than addEventListener will preserve the correct order relative to handlers added declaratively (with attributes like onclick), which use event delegation for performance reasons

Edit this page on GitHub llms.txt

**Examples**:

```python
import { function on<Type extends keyof WindowEventMap>(window: Window, type: Type, handler: (this: Window, event: WindowEventMap[Type]) => any, options?: AddEventListenerOptions | undefined): () => void (+4 overloads)Attaches an event handler to the window and returns a function that removes the handler. Using this
rather than addEventListener will preserve the correct order relative to handlers added declaratively
(with attributes like onclick), which use event delegation for performance reaso
...
```

```javascript
function on<Type extends keyof WindowEventMap>(window: Window, type: Type, handler: (this: Window, event: WindowEventMap[Type]) => any, options?: AddEventListenerOptions | undefined): () => void (+4 overloads)
```

```text
addEventListener
```

---

## <svelte:fragment>

**URL**: https://svelte.dev/docs/svelte/legacy-svelte-fragment

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

The <svelte:fragment> element allows you to place content in a named slot without wrapping it in a container DOM element. This keeps the flow layout of your document intact.

In Svelte 5+, this concept is obsolete, as snippets don’t create a wrapping element

Edit this page on GitHub llms.txt

**Examples**:

```text
<div>
	<slot name="header">No header was provided</slot>
	<p>Some content between header and footer</p>
	<slot name="footer" />
</div>
```

```python
<script>
	import Widget from './Widget.svelte';
</script>

<Widget>
	<h1 slot="header">Hello</h1>
	<svelte:fragment slot="footer">
		<p>All rights reserved.</p>
		<p>Copyright (c) 2019 Svelte Industries</p>
	</svelte:fragment>
</Widget>
```

```python
<script lang="ts">
	import Widget from './Widget.svelte';
</script>

<Widget>
	<h1 slot="header">Hello</h1>
	<svelte:fragment slot="footer">
		<p>All rights reserved.</p>
		<p>Copyright (c) 2019 Svelte Industries</p>
	</svelte:fragment>
</Widget>
```

---

## <svelte:head>

**URL**: https://svelte.dev/docs/svelte/svelte-head

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

This element makes it possible to insert elements into document.head. During server-side rendering, head content is exposed separately to the main body content.

As with <svelte:window>, <svelte:document> and <svelte:body>, this element may only appear at the top level of your component and must never be inside a block or element.

Edit this page on GitHub llms.txt

**Examples**:

```text
<svelte:head>...</svelte:head>
```

```text
<svelte:head>
	<title>Hello world!</title>
	<meta name="description" content="This is where the description goes for SEO" />
</svelte:head>
```

---

## .svelte.js and .svelte.ts files

**URL**: https://svelte.dev/docs/svelte/svelte-js-files

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

Besides .svelte files, Svelte also operates on .svelte.js and .svelte.ts files.

These behave like any other .js or .ts module, except that you can use runes. This is useful for creating reusable reactive logic, or sharing reactive state across your app (though note that you cannot export reassigned state).

This is a concept that didn’t exist prior to Svelte 5

Edit this page on GitHub llms.txt

---

## @sveltejs/kit

**URL**: https://svelte.dev/docs/kit/@sveltejs-kit

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- @sveltejs/kit

Throws an error with a HTTP status code and an optional message. When called during request handling, this will cause SvelteKit to return an error response without invoking handleError. Make sure you’re not catching the thrown error, which would prevent SvelteKit from handling it.

Create an ActionFailure object. Call when form submission fails.

Checks whether this is an action failure thrown by {@link fail } .

Checks whether this is an error thrown by {@link error } .

Checks whether this is a redirect thrown by {@link redirect } .

Create a JSON Response object from the supplied data.

Strips possible SvelteKit-internal suffixes and trailing slashes from the URL pathname. Returns the normalized URL as well as a method for adding the potential suffix back based on a new pathname (possibly including search) or URL.

Redirect a request. When called during request handling, SvelteKit will return a redirect response. Make sure you’re not catching the thrown redirect, which would prevent SvelteKit from handling it.

Most common status codes:

See all redirect status codes

Create a Response object from the supplied body.

Throws an error with a HTTP status code and an optional message. When called during request handling, this will cause SvelteKit to return an error response without invoking handleError. Make sure you’re not catching the thrown error, which would prevent SvelteKit from handling it.

Create an ActionFailure object. Call when form submission fails.

Checks whether this is an action failure thrown by fail.

Checks whether this is an error thrown by error.

Checks whether this is a redirect thrown by redirect.

Create a JSON Response object from the supplied data.

Available since 2.18.0

Strips possible SvelteKit-internal suffixes and trailing slashes from the URL pathname. Returns the normalized URL as well as a method for adding the potential suffix back based on a new pathname (possibly including search) or URL.

Strips possible SvelteKit-internal suf

*[Content truncated - see full docs]*

**Examples**:

```python
import {
	class ServerServer,
	const VERSION: stringVERSION,
	function error(status: number, body: App.Error): never (+1 overload)Throws an error with a HTTP status code and an optional message.
When called during request handling, this will cause SvelteKit to
return an error response without invoking handleError.
Make sure you’re not catching the thrown error, which would prevent SvelteKit from handling it.
@paramstatus The HTTP status code. Must be in the range 400-599.@parambody An object tha
...
```

```text
class Server
```

```javascript
const VERSION: string
```

---

## @sveltejs/kit/hooks

**URL**: https://svelte.dev/docs/kit/@sveltejs-kit-hooks

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- @sveltejs/kit/hooks

A helper function for sequencing multiple handle calls in a middleware-like manner. The behavior for the handle options is as follows:

The example above would print:

A helper function for sequencing multiple handle calls in a middleware-like manner. The behavior for the handle options is as follows:

A helper function for sequencing multiple handle calls in a middleware-like manner. The behavior for the handle options is as follows:

The example above would print:

The console module provides a simple debugging console that is similar to the JavaScript console mechanism provided by web browsers.

The module exports two specific components:

Warning: The global console object’s methods are neither consistently synchronous like the browser APIs they resemble, nor are they consistently asynchronous like all other Node.js streams. See the note on process I/O for more information.

Example using the global console:

Example using the Console class:

Prints to stdout with newline. Multiple arguments can be passed, with the first used as the primary message and all additional used as substitution values similar to printf(3) (the arguments are all passed to util.format()).

See util.format() for more information.

The console module provides a simple debugging console that is similar to the JavaScript console mechanism provided by web browsers.

The module exports two specific components:

Warning: The global console object’s methods are neither consistently synchronous like the browser APIs they resemble, nor are they consistently asynchronous like all other Node.js streams. See the note on process I/O for more information.

Example using the global console:

Example using the Console class:

Prints to stdout with newline. Multiple arguments can be passed, with the first used as the primary message and all additional used as substitution values similar to printf(3) (the arguments are all passed to util.format()).

See util.format() for more information.

The console modu

*[Content truncated - see full docs]*

**Examples**:

```python
import { function sequence(...handlers: Handle[]): HandleA helper function for sequencing multiple handle calls in a middleware-like manner.
The behavior for the handle options is as follows:

transformPageChunk is applied in reverse order and merged
preload is applied in forward order, the first option “wins” and no preload options after it are called
filterSerializedResponseHeaders behaves the same as preload

src/hooks.serverimport { sequence } from '@sveltejs/kit/hooks';

/// type: import('@
...
```

```javascript
function sequence(...handlers: Handle[]): Handle
```

```text
transformPageChunk
```

---

## @sveltejs/kit/node

**URL**: https://svelte.dev/docs/kit/@sveltejs-kit-node

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- @sveltejs/kit/node

Converts a file on disk to a readable stream

Available since 2.4.0

Converts a file on disk to a readable stream

Edit this page on GitHub llms.txt

**Examples**:

```python
import {
	function createReadableStream(file: string): ReadableStreamConverts a file on disk to a readable stream
@since2.4.0createReadableStream,
	function getRequest({ request, base, bodySizeLimit }: {
    request: import("http").IncomingMessage;
    base: string;
    bodySizeLimit?: number;
}): Promise<Request>getRequest,
	function setResponse(res: import("http").ServerResponse, response: Response): Promise<void>setResponse
} from '@sveltejs/kit/node';
```

```javascript
function createReadableStream(file: string): ReadableStream
```

```javascript
function getRequest({ request, base, bodySizeLimit }: {
    request: import("http").IncomingMessage;
    base: string;
    bodySizeLimit?: number;
}): Promise<Request>
```

---

## @sveltejs/kit/node/polyfills

**URL**: https://svelte.dev/docs/kit/@sveltejs-kit-node-polyfills

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- @sveltejs/kit/node/polyfills

Make various web APIs available as globals:

Make various web APIs available as globals:

Edit this page on GitHub llms.txt

**Examples**:

```python
import { function installPolyfills(): voidMake various web APIs available as globals:

crypto
File

installPolyfills } from '@sveltejs/kit/node/polyfills';
```

```javascript
function installPolyfills(): void
```

```javascript
function installPolyfills(): void;
```

---

## @sveltejs/kit/vite

**URL**: https://svelte.dev/docs/kit/@sveltejs-kit-vite

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- @sveltejs/kit/vite

Returns the SvelteKit Vite plugins.

Returns the SvelteKit Vite plugins.

Edit this page on GitHub llms.txt

**Examples**:

```python
import { function sveltekit(): Promise<Plugin$1<any>[]>Returns the SvelteKit Vite plugins.
sveltekit } from '@sveltejs/kit/vite';
```

```javascript
function sveltekit(): Promise<Plugin$1<any>[]>
```

```javascript
function sveltekit(): Promise<import('vite').Plugin[]>;
```

---

## svelte/legacy

**URL**: https://svelte.dev/docs/svelte/svelte-legacy

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

This module provides various functions for use during the migration, since some features can’t be replaced one to one with new features. All imports are marked as deprecated and should be migrated away from over time.

Takes the component function and returns a Svelte 4 compatible component constructor.

Function to create a bubble function that mimic the behavior of on:click without handler available in svelte 4.

Takes the same options as a Svelte 4 component and the component function and returns a Svelte 4 compatible component.

Function to mimic the multiple listeners available in svelte 4

Substitute for the nonpassive event modifier, implemented as an action

Substitute for the once event modifier

Substitute for the passive event modifier, implemented as an action

Substitute for the preventDefault event modifier

Runs the given function once immediately on the server, and works like $effect.pre on the client.

Substitute for the self event modifier

Substitute for the stopImmediatePropagation event modifier

Substitute for the stopPropagation event modifier

Substitute for the trusted event modifier

Use this only as a temporary solution to migrate your imperative component code to Svelte 5.

Takes the component function and returns a Svelte 4 compatible component constructor.

Use this only as a temporary solution to migrate your automatically delegated events in Svelte 5.

Function to create a bubble function that mimic the behavior of on:click without handler available in svelte 4.

Use this only as a temporary solution to migrate your imperative component code to Svelte 5.

Takes the same options as a Svelte 4 component and the component function and returns a Svelte 4 compatible component.

Function to mimic the multiple listeners available in svelte 4

Substitute for the nonpassive event modifier, implemented as an action

Substitute for the once event modifier

Substitute for the passive event modifier, implemented as an action

Substitute for the pr

*[Content truncated - see full docs]*

**Examples**:

```javascript
import {
	function asClassComponent<Props extends Record<string, any>, Exports extends Record<string, any>, Events extends Record<string, any>, Slots extends Record<string, any>>(component: SvelteComponent<Props, Events, Slots> | Component<Props>): ComponentType<SvelteComponent<Props, Events, Slots> & Exports>Takes the component function and returns a Svelte 4 compatible component constructor.
@deprecatedUse this only as a temporary solution to migrate your imperative component code to Svelte 5.
...
```

```javascript
function asClassComponent<Props extends Record<string, any>, Exports extends Record<string, any>, Events extends Record<string, any>, Slots extends Record<string, any>>(component: SvelteComponent<Props, Events, Slots> | Component<Props>): ComponentType<SvelteComponent<Props, Events, Slots> & Exports>
```

```javascript
function createBubbler(): (type: string) => (event: Event) => boolean
```

---

## svelte/motion

**URL**: https://svelte.dev/docs/svelte/svelte-motion

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

A wrapper for a value that behaves in a spring-like fashion. Changes to spring.target will cause spring.current to move towards it over time, taking account of the spring.stiffness and spring.damping parameters.

A wrapper for a value that tweens smoothly to its target value. Changes to tween.target will cause tween.current to move towards it over time, taking account of the delay, duration and easing options.

A media query that matches if the user prefers reduced motion.

The spring function in Svelte creates a store whose value is animated, with a motion that simulates the behavior of a spring. This means when the value changes, instead of transitioning at a steady rate, it “bounces” like a spring would, depending on the physics parameters provided. This adds a level of realism to the transitions and can enhance the user experience.

A tweened store in Svelte is a special type of store that provides smooth transitions between state values over time.

Available since 5.8.0

A wrapper for a value that behaves in a spring-like fashion. Changes to spring.target will cause spring.current to move towards it over time, taking account of the spring.stiffness and spring.damping parameters.

Create a spring whose value is bound to the return value of fn. This must be called inside an effect root (for example, during component initialisation).

Sets spring.target to value and returns a Promise that resolves if and when spring.current catches up to it.

If options.instant is true, spring.current immediately matches spring.target.

If options.preserveMomentum is provided, the spring will continue on its current trajectory for the specified number of milliseconds. This is useful for things like ‘fling’ gestures.

The end value of the spring. This property only exists on the Spring class, not the legacy spring store.

The current value of the spring. This property only exists on the Spring class, not the legacy spring store.

Available since 5.8.0

A wrapper for a value that tw

*[Content truncated - see full docs]*

**Examples**:

```python
import {
	class Spring<T>
interface Spring<T>A wrapper for a value that behaves in a spring-like fashion. Changes to spring.target will cause spring.current to
move towards it over time, taking account of the spring.stiffness and spring.damping parameters.
&#x3C;script>
	import { Spring } from 'svelte/motion';

	const spring = new Spring(0);
&#x3C;/script>

&#x3C;input type="range" bind:value={spring.target} />
&#x3C;input type="range" bind:value={spring.current} disabled />@since5.8.0Spring,
	c
...
```

```text
class Spring<T>
interface Spring<T>
```

```text
class Spring<T>
interface Spring<T>
```

---

## <svelte:options>

**URL**: https://svelte.dev/docs/svelte/svelte-options

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

The <svelte:options> element provides a place to specify per-component compiler options, which are detailed in the compiler section. The possible options are:

Deprecated options Svelte 4 also included the following options. They are deprecated in Svelte 5 and non-functional in runes mode.

Edit this page on GitHub llms.txt

**Examples**:

```text
<svelte:options option={value} />
```

```text
<svelte:options customElement="my-custom-element" />
```

---

## svelte/reactivity

**URL**: https://svelte.dev/docs/svelte/svelte-reactivity

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

Svelte provides reactive versions of various built-ins like Map, Set and URL that can be used just like their native counterparts, as well as a handful of additional utilities for handling reactivity.

Creates a media query and provides a current property that reflects whether or not it matches.

Use it carefully — during server-side rendering, there is no way to know what the correct value should be, potentially causing content to change upon hydration. If you can use the media query in CSS to achieve the same effect, do that.

A reactive version of the built-in Date object. Reading the date (whether with methods like date.getTime() or date.toString(), or via things like Intl.DateTimeFormat) in an effect or derived will cause it to be re-evaluated when the value of the date changes.

A reactive version of the built-in Map object. Reading contents of the map (by iterating, or by reading map.size or calling map.get(...) or map.has(...) as in the tic-tac-toe example below) in an effect or derived will cause it to be re-evaluated as necessary when the map is updated.

Note that values in a reactive map are not made deeply reactive.

A reactive version of the built-in Set object. Reading contents of the set (by iterating, or by reading set.size or calling set.has(...) as in the example below) in an effect or derived will cause it to be re-evaluated as necessary when the set is updated.

Note that values in a reactive set are not made deeply reactive.

A reactive version of the built-in URL object. Reading properties of the URL (such as url.href or url.pathname) in an effect or derived will cause it to be re-evaluated as necessary when the URL changes.

The searchParams property is an instance of SvelteURLSearchParams.

A reactive version of the built-in URLSearchParams object. Reading its contents (by iterating, or by calling params.get(...) or params.getAll(...) as in the example below) in an effect or derived will cause it to be re-evaluated as necessary when the para

*[Content truncated - see full docs]*

**Examples**:

```python
import {
	class MediaQueryCreates a media query and provides a current property that reflects whether or not it matches.
Use it carefully — during server-side rendering, there is no way to know what the correct value should be, potentially causing content to change upon hydration.
If you can use the media query in CSS to achieve the same effect, do that.
&#x3C;script>
	import { MediaQuery } from 'svelte/reactivity';

	const large = new MediaQuery('min-width: 800px');
&#x3C;/script>

&#x3C;h1>{la
...
```

```text
class MediaQuery
```

```python
&#x3C;script>
	import { MediaQuery } from 'svelte/reactivity';

	const large = new MediaQuery('min-width: 800px');
&#x3C;/script>

&#x3C;h1>{large.current ? 'large screen' : 'small screen'}&#x3C;/h1>
```

---

## svelte/reactivity/window

**URL**: https://svelte.dev/docs/svelte/svelte-reactivity-window

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

This module exports reactive versions of various window values, each of which has a reactive current property that you can reference in reactive contexts (templates, deriveds and effects) without using <svelte:window> bindings or manually creating your own event listeners.

devicePixelRatio.current is a reactive view of window.devicePixelRatio. On the server it is undefined. Note that behaviour differs between browsers — on Chrome it will respond to the current zoom level, on Firefox and Safari it won’t.

innerHeight.current is a reactive view of window.innerHeight. On the server it is undefined.

innerWidth.current is a reactive view of window.innerWidth. On the server it is undefined.

online.current is a reactive view of navigator.onLine. On the server it is undefined.

outerHeight.current is a reactive view of window.outerHeight. On the server it is undefined.

outerWidth.current is a reactive view of window.outerWidth. On the server it is undefined.

screenLeft.current is a reactive view of window.screenLeft. It is updated inside a requestAnimationFrame callback. On the server it is undefined.

screenTop.current is a reactive view of window.screenTop. It is updated inside a requestAnimationFrame callback. On the server it is undefined.

scrollX.current is a reactive view of window.scrollX. On the server it is undefined.

scrollY.current is a reactive view of window.scrollY. On the server it is undefined.

Available since 5.11.0

devicePixelRatio.current is a reactive view of window.devicePixelRatio. On the server it is undefined. Note that behaviour differs between browsers — on Chrome it will respond to the current zoom level, on Firefox and Safari it won’t.

Available since 5.11.0

innerHeight.current is a reactive view of window.innerHeight. On the server it is undefined.

Available since 5.11.0

innerWidth.current is a reactive view of window.innerWidth. On the server it is undefined.

Available since 5.11.0

online.current is a reactive view of navigator.o

*[Content truncated - see full docs]*

**Examples**:

```python
<script>
	import { innerWidth, innerHeight } from 'svelte/reactivity/window';
</script>

<p>{innerWidth.current}x{innerHeight.current}</p>
```

```python
import {
	const devicePixelRatio: {
    readonly current: number | undefined;
}devicePixelRatio.current is a reactive view of window.devicePixelRatio. On the server it is undefined.
Note that behaviour differs between browsers — on Chrome it will respond to the current zoom level,
on Firefox and Safari it won’t.
@since5.11.0devicePixelRatio,
	const innerHeight: ReactiveValue<number | undefined>innerHeight.current is a reactive view of window.innerHeight. On the server it is undefined.
@since5.11
...
```

```javascript
const devicePixelRatio: {
    readonly current: number | undefined;
}
```

---

## <svelte:self>

**URL**: https://svelte.dev/docs/svelte/legacy-svelte-self

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

The <svelte:self> element allows a component to include itself, recursively.

It cannot appear at the top level of your markup; it must be inside an if or each block or passed to a component’s slot to prevent an infinite loop.

This concept is obsolete, as components can import themselves:

Edit this page on GitHub llms.txt

**Examples**:

```javascript
<script>
	export let count;
</script>

{#if count > 0}
	<p>counting down... {count}</p>
	<svelte:self count={count - 1} />
{:else}
	<p>lift-off!</p>
{/if}
```

```python
<script>
	import Self from './App.svelte'
	export let count;
</script>

{#if count > 0}
	<p>counting down... {count}</p>
	<Self count={count - 1} />
{:else}
	<p>lift-off!</p>
{/if}
```

```python
<script lang="ts">
	import Self from './App.svelte'
	export let count;
</script>

{#if count > 0}
	<p>counting down... {count}</p>
	<Self count={count - 1} />
{:else}
	<p>lift-off!</p>
{/if}
```

---

## svelte/server

**URL**: https://svelte.dev/docs/svelte/svelte-server

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

Only available on the server and when compiling with the server option. Takes a component and returns an object with body and head properties on it, which you can use to populate the HTML when server-rendering your app.

Only available on the server and when compiling with the server option. Takes a component and returns an object with body and head properties on it, which you can use to populate the HTML when server-rendering your app.

Edit this page on GitHub llms.txt

**Examples**:

```python
import { function render<Comp extends SvelteComponent<any> | Component<any>, Props extends ComponentProps<Comp> = ComponentProps<Comp>>(...args: {} extends Props ? [component: Comp extends SvelteComponent<any> ? ComponentType<Comp> : Comp, options?: {
    props?: Omit<Props, "$$slots" | "$$events">;
    context?: Map<any, any>;
    idPrefix?: string;
}] : [component: Comp extends SvelteComponent<any> ? ComponentType<Comp> : Comp, options: {
    props: Omit<Props, "$$slots" | "$$events">;
    con
...
```

```javascript
function render<Comp extends SvelteComponent<any> | Component<any>, Props extends ComponentProps<Comp> = ComponentProps<Comp>>(...args: {} extends Props ? [component: Comp extends SvelteComponent<any> ? ComponentType<Comp> : Comp, options?: {
    props?: Omit<Props, "$$slots" | "$$events">;
    context?: Map<any, any>;
    idPrefix?: string;
}] : [component: Comp extends SvelteComponent<any> ? ComponentType<Comp> : Comp, options: {
    props: Omit<Props, "$$slots" | "$$events">;
    context?: Ma
...
```

```javascript
function render<Comp extends SvelteComponent<any> | Component<any>, Props extends ComponentProps<Comp> = ComponentProps<Comp>>(...args: {} extends Props ? [component: Comp extends SvelteComponent<any> ? ComponentType<Comp> : Comp, options?: {
    props?: Omit<Props, "$$slots" | "$$events">;
    context?: Map<any, any>;
    idPrefix?: string;
}] : [component: Comp extends SvelteComponent<any> ? ComponentType<Comp> : Comp, options: {
    props: Omit<Props, "$$slots" | "$$events">;
    context?: Ma
...
```

---

## svelte/store

**URL**: https://svelte.dev/docs/svelte/svelte-store

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

Derived value store by synchronizing one or more readable stores and applying an aggregation function over its input values.

Get the current value from a store by subscribing and immediately unsubscribing.

Creates a Readable store that allows reading by subscription.

Takes a store and returns a new one derived from the old one that is readable.

Create a Writable store that allows both updating and reading by subscription.

Derived value store by synchronizing one or more readable stores and applying an aggregation function over its input values.

Get the current value from a store by subscribing and immediately unsubscribing.

Creates a Readable store that allows reading by subscription.

Takes a store and returns a new one derived from the old one that is readable.

Create a Writable store that allows both updating and reading by subscription.

Readable interface for subscribing.

Subscribe on value changes.

Start and stop notification callbacks. This function is called when the first subscriber subscribes.

Callback to inform of a value updates.

Unsubscribes from value updates.

Callback to update a value.

Writable interface for both updating and subscribing.

Set value and inform subscribers.

Update value using callback and inform subscribers.

Edit this page on GitHub llms.txt

**Examples**:

```python
import {
	function derived<S extends Stores, T>(stores: S, fn: (values: StoresValues<S>, set: (value: T) => void, update: (fn: Updater<T>) => void) => Unsubscriber | void, initial_value?: T | undefined): Readable<T> (+1 overload)Derived value store by synchronizing one or more readable stores and
applying an aggregation function over its input values.
derived,
	function fromStore<V>(store: Writable<V>): {
    current: V;
} (+1 overload)fromStore,
	function get<T>(store: Readable<T>): TGet the cu
...
```

```javascript
function derived<S extends Stores, T>(stores: S, fn: (values: StoresValues<S>, set: (value: T) => void, update: (fn: Updater<T>) => void) => Unsubscriber | void, initial_value?: T | undefined): Readable<T> (+1 overload)
```

```javascript
function fromStore<V>(store: Writable<V>): {
    current: V;
} (+1 overload)
```

---

## svelte/transition

**URL**: https://svelte.dev/docs/svelte/svelte-transition

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

Animates a blur filter alongside an element’s opacity.

The crossfade function creates a pair of transitions called send and receive. When an element is ‘sent’, it looks for a corresponding element being ‘received’, and generates a transition that transforms the element to its counterpart’s position and fades it out. When an element is ‘received’, the reverse happens. If there is no counterpart, the fallback transition is used.

Animates the stroke of an SVG element, like a snake in a tube. in transitions begin with the path invisible and draw the path to the screen over time. out transitions start in a visible state and gradually erase the path. draw only works with elements that have a getTotalLength method, like &#x3C;path> and &#x3C;polyline>.

Animates the opacity of an element from 0 to the current opacity for in transitions and from the current opacity to 0 for out transitions.

Animates the x and y positions and the opacity of an element. in transitions animate from the provided values, passed as parameters to the element’s default values. out transitions animate from the element’s default values to the provided values.

Animates the opacity and scale of an element. in transitions animate from the provided values, passed as parameters, to an element’s current (default) values. out transitions animate from an element’s default values to the provided values.

Slides an element in and out.

Animates a blur filter alongside an element’s opacity.

The crossfade function creates a pair of transitions called send and receive. When an element is ‘sent’, it looks for a corresponding element being ‘received’, and generates a transition that transforms the element to its counterpart’s position and fades it out. When an element is ‘received’, the reverse happens. If there is no counterpart, the fallback transition is used.

Animates the stroke of an SVG element, like a snake in a tube. in transitions begin with the path invisible and draw the path to the screen over tim

*[Content truncated - see full docs]*

**Examples**:

```python
import {
	function blur(node: Element, { delay, duration, easing, amount, opacity }?: BlurParams | undefined): TransitionConfigAnimates a blur filter alongside an element’s opacity.
blur,
	function crossfade({ fallback, ...defaults }: CrossfadeParams & {
    fallback?: (node: Element, params: CrossfadeParams, intro: boolean) => TransitionConfig;
}): [(node: any, params: CrossfadeParams & {
    key: any;
}) => () => TransitionConfig, (node: any, params: CrossfadeParams & {
    key: any;
}) => () 
...
```

```javascript
function blur(node: Element, { delay, duration, easing, amount, opacity }?: BlurParams | undefined): TransitionConfig
```

```javascript
function crossfade({ fallback, ...defaults }: CrossfadeParams & {
    fallback?: (node: Element, params: CrossfadeParams, intro: boolean) => TransitionConfig;
}): [(node: any, params: CrossfadeParams & {
    key: any;
}) => () => TransitionConfig, (node: any, params: CrossfadeParams & {
    key: any;
}) => () => TransitionConfig]
```

---

## <svelte:window>

**URL**: https://svelte.dev/docs/svelte/svelte-window

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

The <svelte:window> element allows you to add event listeners to the window object without worrying about removing them when the component is destroyed, or checking for the existence of window when server-side rendering.

This element may only appear at the top level of your component — it cannot be inside a block or element.

You can also bind to the following properties:

All except scrollX and scrollY are readonly.

Note that the page will not be scrolled to the initial value to avoid accessibility issues. Only subsequent changes to the bound variable of scrollX and scrollY will cause scrolling. If you have a legitimate reason to scroll when the component is rendered, call scrollTo() in an $effect.

Edit this page on GitHub llms.txt

**Examples**:

```text
<svelte:window onevent={handler} />
```

```text
<svelte:window bind:prop={value} />
```

```javascript
<script>
	function handleKeydown(event) {
		alert(`pressed the ${event.key} key`);
	}
</script>

<svelte:window onkeydown={handleKeydown} />
```

---

## transition:

**URL**: https://svelte.dev/docs/svelte/transition

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

A transition is triggered by an element entering or leaving the DOM as a result of a state change.

When a block (such as an {#if ...} block) is transitioning out, all elements inside it, including those that do not have their own transitions, are kept in the DOM until every transition in the block has been completed.

The transition: directive indicates a bidirectional transition, which means it can be smoothly reversed while the transition is in progress.

Transitions are local by default. Local transitions only play when the block they belong to is created or destroyed, not when parent blocks are created or destroyed.

A selection of built-in transitions can be imported from the svelte/transition module.

Transitions can have parameters.

(The double {{curlies}} aren’t a special syntax; this is an object literal inside an expression tag.)

Transitions can use custom functions. If the returned object has a css function, Svelte will generate keyframes for a web animation.

The t argument passed to css is a value between 0 and 1 after the easing function has been applied. In transitions run from 0 to 1, out transitions run from 1 to 0 — in other words, 1 is the element’s natural state, as though no transition had been applied. The u argument is equal to 1 - t.

The function is called repeatedly before the transition begins, with different t and u arguments.

A custom transition function can also return a tick function, which is called during the transition with the same t and u arguments.

If it’s possible to use css instead of tick, do so — web animations can run off the main thread, preventing jank on slower devices.

If a transition returns a function instead of a transition object, the function will be called in the next microtask. This allows multiple transitions to coordinate, making crossfade effects possible.

Transition functions also receive a third argument, options, which contains information about the transition.

Available values in the options object 

*[Content truncated - see full docs]*

**Examples**:

```python
<script>
	import { fade } from 'svelte/transition';

	let visible = $state(false);
</script>

<button onclick={() => visible = !visible}>toggle</button>

{#if visible}
	<div transition:fade>fades in and out</div>
{/if}
```

```text
{#if x}
	{#if y}
		<p transition:fade>fades in and out only when y changes</p>

		<p transition:fade|global>fades in and out when x or y change</p>
	{/if}
{/if}
```

```text
{#if visible}
	<div transition:fade={{ duration: 2000 }}>fades in and out over two seconds</div>
{/if}
```

---

## use:

**URL**: https://svelte.dev/docs/svelte/use

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

In Svelte 5.29 and newer, consider using attachments instead, as they are more flexible and composable.

Actions are functions that are called when an element is mounted. They are added with the use: directive, and will typically use an $effect so that they can reset any state when the element is unmounted:

An action can be called with an argument:

The action is only called once (but not during server-side rendering) — it will not run again if the argument changes.

Prior to the $effect rune, actions could return an object with update and destroy methods, where update would be called with the latest value of the argument if it changed. Using effects is preferred.

The Action interface receives three optional type arguments — a node type (which can be Element, if the action applies to everything), a parameter, and any custom event handlers created by the action:

Edit this page on GitHub llms.txt

**Examples**:

```javascript
<script>
	/** @type {import('svelte/action').Action} */
	function myaction(node) {
		// the node has been mounted in the DOM

		$effect(() => {
			// setup goes here

			return () => {
				// teardown goes here
			};
		});
	}
</script>

<div use:myaction>...</div>
```

```python
<script lang="ts">
	import type { Action } from 'svelte/action';

	const myaction: Action = (node) => {
		// the node has been mounted in the DOM

		$effect(() => {
			// setup goes here

			return () => {
				// teardown goes here
			};
		});
	};
</script>

<div use:myaction>...</div>
```

```javascript
<script>
	/** @type {import('svelte/action').Action} */
	function myaction(node, data) {
		// ...
	}
</script>

<div use:myaction={data}>...</div>
```

---
