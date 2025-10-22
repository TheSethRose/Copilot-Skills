# Vite - Guide

**Pages**: 15

---

## Backend Integration ​

**URL**: https://vitejs.dev/guide/backend-integration

**Contents**:
- Backend Integration ​

If you want to serve the HTML using a traditional backend (e.g. Rails, Laravel) but use Vite for serving assets, check for existing integrations listed in Awesome Vite.

If you need a custom integration, you can follow the steps in this guide to configure it manually

In your Vite config, configure the entry and enable build manifest:

If you haven't disabled the module preload polyfill, you also need to import the polyfill in your entry

For development, inject the following in your server's HTML template (substitute http://localhost:5173 with the local URL Vite is running at):

In order to properly serve assets, you have two options:

This is needed for assets such as images to load properly.

Note if you are using React with @vitejs/plugin-react, you'll also need to add this before the above scripts, since the plugin is not able to modify the HTML you are serving (substitute http://localhost:5173 with the local URL Vite is running at):

For production, after running vite build, a .vite/manifest.json file will be generated alongside other asset files. An example manifest file looks like this:

The manifest has a Record<name, chunk> structure where each chunk follows the ManifestChunk interface:

Each entry in the manifest represents one of the following:

Chunks will contain information on their static and dynamic imports (both are keys that map to the corresponding chunk in the manifest), and also their corresponding CSS and asset files (if any).

You can use this file to render links or preload directives with hashed filenames.

Here is an example HTML template to render the proper links. The syntax here is for explanation only, substitute with your server templating language. The importedChunks function is for illustration and isn't provided by Vite.

Specifically, a backend generating HTML should include the following tags given a manifest file and an entry point. Note that following this order is recommended for optimal performance:

Following the above examp

*[Content truncated - see full docs]*

**Examples**:

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

```text
// add the beginning of your app entry
import 'vite/modulepreload-polyfill'
```

```text
<!-- if development -->
<script type="module" src="http://localhost:5173/@vite/client"></script>
<script type="module" src="http://localhost:5173/main.js"></script>
```

---

## Building for Production ​

**URL**: https://vitejs.dev/guide/build

**Contents**:
- Building for Production ​
- Browser Compatibility ​
- Public Base Path ​
  - Relative base ​
- Customizing the Build ​
- Chunking Strategy ​
- Load Error Handling ​
- Rebuild on Files Changes ​

When it is time to deploy your app for production, simply run the vite build command. By default, it uses <root>/index.html as the build entry point, and produces an application bundle that is suitable to be served over a static hosting service. Check out the Deploying a Static Site for guides about popular services.

By default, the production bundle assumes a modern browser that is included in the Baseline Widely Available targets. The default browser support range is:

You can specify custom targets via the build.target config option, where the lowest target is es2015. If a lower target is set, Vite will still require these minimum browser support ranges as it relies on native ESM dynamic import, and import.meta:

Note that by default, Vite only handles syntax transforms and does not cover polyfills. You can check out https://cdnjs.cloudflare.com/polyfill/ which automatically generates polyfill bundles based on the user's browser UserAgent string.

Legacy browsers can be supported via @vitejs/plugin-legacy, which will automatically generate legacy chunks and corresponding ES language feature polyfills. The legacy chunks are conditionally loaded only in browsers that do not have native ESM support.

If you are deploying your project under a nested public path, simply specify the base config option and all asset paths will be rewritten accordingly. This option can also be specified as a command line flag, e.g. vite build --base=/my/public/path/.

JS-imported asset URLs, CSS url() references, and asset references in your .html files are all automatically adjusted to respect this option during build.

The exception is when you need to dynamically concatenate URLs on the fly. In this case, you can use the globally injected import.meta.env.BASE_URL variable which will be the public base path. Note this variable is statically replaced during build so it must appear exactly as-is (i.e. import.meta.env['BASE_URL'] won't work).

For advanced base path control, check out Ad

*[Content truncated - see full docs]*

**Examples**:

```typescript
export default defineConfig({
  build: {
    rollupOptions: {
      // https://rollupjs.org/configuration-options/
    },
  },
})
```

```javascript
window.addEventListener('vite:preloadError', (event) => {
  window.location.reload() // for example, refresh the page
})
```

```typescript
export default defineConfig({
  build: {
    watch: {
      // https://rollupjs.org/configuration-options/#watch
    },
  },
})
```

---

## Command Line Interface ​

**URL**: https://vitejs.dev/guide/cli

**Contents**:
- Command Line Interface ​
- Dev server ​
  - vite ​
    - Usage ​
    - Options ​
- Build ​
  - vite build ​
    - Usage ​

Start Vite dev server in the current directory. vite dev and vite serve are aliases for vite.

Build for production.

Pre-bundle dependencies.

Deprecated: the pre-bundle process runs automatically and does not need to be called.

Locally preview the production build. Do not use this as a production server as it's not designed for it.

This command starts a server in the build directory (by default dist). Run vite build beforehand to ensure that the build directory is up-to-date. Depending on the project's configured appType, it makes use of certain middleware.

**Examples**:

```text
vite [root]
```

```text
vite build [root]
```

```text
vite optimize [root]
```

---

## Dependency Pre-Bundling ​

**URL**: https://vitejs.dev/guide/dep-pre-bundling

**Contents**:
- Dependency Pre-Bundling ​
- The Why ​
- Automatic Dependency Discovery ​
- Monorepos and Linked Dependencies ​
- Customizing the Behavior ​
- Caching ​
  - File System Cache ​
  - Browser Cache ​

When you run vite for the first time, Vite prebundles your project dependencies before loading your site locally. It is done automatically and transparently by default.

This is Vite performing what we call "dependency pre-bundling". This process serves two purposes:

CommonJS and UMD compatibility: During development, Vite's dev serves all code as native ESM. Therefore, Vite must convert dependencies that are shipped as CommonJS or UMD into ESM first.

When converting CommonJS dependencies, Vite performs smart import analysis so that named imports to CommonJS modules will work as expected even if the exports are dynamically assigned (e.g. React):

Performance: Vite converts ESM dependencies with many internal modules into a single module to improve subsequent page load performance.

Some packages ship their ES modules builds as many separate files importing one another. For example, lodash-es has over 600 internal modules! When we do import { debounce } from 'lodash-es', the browser fires off 600+ HTTP requests at the same time! Even though the server has no problem handling them, the large amount of requests create a network congestion on the browser side, causing the page to load noticeably slower.

By pre-bundling lodash-es into a single module, we now only need one HTTP request instead!

Dependency pre-bundling only applies in development mode, and uses esbuild to convert dependencies to ESM. In production builds, @rollup/plugin-commonjs is used instead.

If an existing cache is not found, Vite will crawl your source code and automatically discover dependency imports (i.e. "bare imports" that expect to be resolved from node_modules) and use these found imports as entry points for the pre-bundle. The pre-bundling is performed with esbuild so it's typically very fast.

After the server has already started, if a new dependency import is encountered that isn't already in the cache, Vite will re-run the dep bundling process and reload the page if needed.

In a monor

*[Content truncated - see full docs]*

**Examples**:

```python
// works as expected
import React, { useState } from 'react'
```

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

---

## Deploying a Static Site ​

**URL**: https://vitejs.dev/guide/static-deploy

**Contents**:
- Deploying a Static Site ​
- Building the App ​
  - Testing the App Locally ​
- GitHub Pages ​
- GitLab Pages and GitLab CI ​
- Netlify ​
  - Netlify CLI ​
  - Netlify with Git ​

The following guides are based on some shared assumptions:

It is important to note that vite preview is intended for previewing the build locally and not meant as a production server.

These guides provide instructions for performing a static deployment of your Vite site. Vite also supports Server-Side Rendering. SSR refers to front-end frameworks that support running the same application in Node.js, pre-rendering it to HTML, and finally hydrating it on the client. Check out the SSR Guide to learn about this feature. On the other hand, if you are looking for integration with traditional server-side frameworks, check out the Backend Integration guide instead.

You may run npm run build command to build the app.

By default, the build output will be placed at dist. You may deploy this dist folder to any of your preferred platforms.

Once you've built the app, you may test it locally by running npm run preview command.

The vite preview command will boot up a local static web server that serves the files from dist at http://localhost:4173. It's an easy way to check if the production build looks OK in your local environment.

You may configure the port of the server by passing the --port flag as an argument.

Now the preview command will launch the server at http://localhost:8080.

Set the correct base in vite.config.js.

If you are deploying to https://<USERNAME>.github.io/, or to a custom domain through GitHub Pages (eg. www.example.com), set base to '/'. Alternatively, you can remove base from the configuration, as it defaults to '/'.

If you are deploying to https://<USERNAME>.github.io/<REPO>/ (eg. your repository is at https://github.com/<USERNAME>/<REPO>), then set base to '/<REPO>/'.

Go to your GitHub Pages configuration in the repository settings page and choose the source of deployment as "GitHub Actions", this will lead you to create a workflow that builds and deploys your project, a sample workflow that installs dependencies and builds using npm is provide

*[Content truncated - see full docs]*

**Examples**:

```text
{
  "scripts": {
    "build": "vite build",
    "preview": "vite preview"
  }
}
```

```text
$ npm run build
```

```text
$ npm run preview
```

---

## Env Variables and Modes ​

**URL**: https://vitejs.dev/guide/env-and-mode

**Contents**:
- Env Variables and Modes ​
- Built-in Constants ​
- Env Variables ​
  - .env Files ​
- IntelliSense for TypeScript ​
- HTML Constant Replacement ​
- Modes ​
  - NODE_ENV and Modes ​

Vite exposes certain constants under the special import.meta.env object. These constants are defined as global variables during dev and statically replaced at build time to make tree-shaking effective.

Some built-in constants are available in all cases:

import.meta.env.MODE: {string} the mode the app is running in.

import.meta.env.BASE_URL: {string} the base url the app is being served from. This is determined by the base config option.

import.meta.env.PROD: {boolean} whether the app is running in production (running the dev server with NODE_ENV='production' or running an app built with NODE_ENV='production').

import.meta.env.DEV: {boolean} whether the app is running in development (always the opposite of import.meta.env.PROD)

import.meta.env.SSR: {boolean} whether the app is running in the server.

Vite exposes env variables under import.meta.env object as strings automatically.

To prevent accidentally leaking env variables to the client, only variables prefixed with VITE_ are exposed to your Vite-processed code. e.g. for the following env variables:

Only VITE_SOME_KEY will be exposed as import.meta.env.VITE_SOME_KEY to your client source code, but DB_PASSWORD will not.

If you want to customize the env variables prefix, see the envPrefix option.

As shown above, VITE_SOME_KEY is a number but returns a string when parsed. The same would also happen for boolean env variables. Make sure to convert to the desired type when using it in your code.

Vite uses dotenv to load additional environment variables from the following files in your environment directory:

Env Loading Priorities

An env file for a specific mode (e.g. .env.production) will take higher priority than a generic one (e.g. .env).

Vite will always load .env and .env.local in addition to the mode-specific .env.[mode] file. Variables declared in mode-specific files will take precedence over those in generic files, but variables defined only in .env or .env.local will still be available in the envir

*[Content truncated - see full docs]*

**Examples**:

```text
if (import.meta.env.DEV) {
  // code inside here will be tree-shaken in production builds
  console.log('Dev mode')
}
```

```text
VITE_SOME_KEY=123
DB_PASSWORD=foobar
```

```text
console.log(import.meta.env.VITE_SOME_KEY) // "123"
console.log(import.meta.env.DB_PASSWORD) // undefined
```

---

## Features ​

**URL**: https://vitejs.dev/guide/features

**Contents**:
- Features ​
- npm Dependency Resolving and Pre-Bundling ​
- Hot Module Replacement ​
- TypeScript ​
  - Transpile Only ​
  - TypeScript Compiler Options ​
    - isolatedModules ​
    - useDefineForClassFields ​

At the very basic level, developing using Vite is not that different from using a static file server. However, Vite provides many enhancements over native ESM imports to support various features that are typically seen in bundler-based setups.

Native ES imports do not support bare module imports like the following:

The above will throw an error in the browser. Vite will detect such bare module imports in all served source files and perform the following:

Pre-bundle them to improve page loading speed and convert CommonJS / UMD modules to ESM. The pre-bundling step is performed with esbuild and makes Vite's cold start time significantly faster than any JavaScript-based bundler.

Rewrite the imports to valid URLs like /node_modules/.vite/deps/my-dep.js?v=f3sf2ebd so that the browser can import them properly.

Dependencies are Strongly Cached

Vite caches dependency requests via HTTP headers, so if you wish to locally edit/debug a dependency, follow the steps here.

Vite provides an HMR API over native ESM. Frameworks with HMR capabilities can leverage the API to provide instant, precise updates without reloading the page or blowing away application state. Vite provides first-party HMR integrations for Vue Single File Components and React Fast Refresh. There are also official integrations for Preact via @prefresh/vite.

Note you don't need to manually set these up - when you create an app via create-vite, the selected templates would have these pre-configured for you already.

Vite supports importing .ts files out of the box.

Note that Vite only performs transpilation on .ts files and does NOT perform type checking. It assumes type checking is taken care of by your IDE and build process.

The reason Vite does not perform type checking as part of the transform process is because the two jobs work fundamentally differently. Transpilation can work on a per-file basis and aligns perfectly with Vite's on-demand compile model. In comparison, type checking requires knowled

*[Content truncated - see full docs]*

**Examples**:

```python
import { someMethod } from 'my-dep'
```

```python
import type { T } from 'only/types'
export type { T }
```

```text
{
  "compilerOptions": {
    "types": ["vite/client", "some-other-global-lib"]
  }
}
```

---

## Getting Started ​

**URL**: https://vitejs.dev/guide/

**Contents**:
- Getting Started ​
- Overview ​
- Browser Support ​
- Trying Vite Online ​
- Scaffolding Your First Vite Project ​
- Community Templates ​
- Manual Installation ​
- index.html and Project Root ​

Vite (French word for "quick", pronounced /vit/, like "veet") is a build tool that aims to provide a faster and leaner development experience for modern web projects. It consists of two major parts:

A dev server that provides rich feature enhancements over native ES modules, for example extremely fast Hot Module Replacement (HMR).

A build command that bundles your code with Rollup, pre-configured to output highly optimized static assets for production.

Vite is opinionated and comes with sensible defaults out of the box. Read about what's possible in the Features Guide. Support for frameworks or integration with other tools is possible through Plugins. The Config Section explains how to adapt Vite to your project if needed.

Vite is also highly extensible via its Plugin API and JavaScript API with full typing support.

You can learn more about the rationale behind the project in the Why Vite section.

During development, Vite assumes that a modern browser is used. This means the browser supports most of the latest JavaScript and CSS features. For that reason, Vite sets esnext as the transform target. This prevents syntax lowering, letting Vite serve modules as close as possible to the original source code. Vite injects some runtime code to make the development server work. These code use features included in Baseline Newly Available at the time of each major release (2025-05-01 for this major).

For production builds, Vite by default targets Baseline Widely Available browsers. These are browsers that were released at least 2.5 years ago. The target can be lowered via configuration. Additionally, legacy browsers can be supported via the official @vitejs/plugin-legacy. See the Building for Production section for more details.

You can try Vite online on StackBlitz. It runs the Vite-based build setup directly in the browser, so it is almost identical to the local setup but doesn't require installing anything on your machine. You can navigate to vite.new/{template} to

*[Content truncated - see full docs]*

**Examples**:

```text
$ npm create vite@latest
```

```text
$ yarn create vite
```

```text
$ pnpm create vite
```

---

## HMR API ​

**URL**: https://vitejs.dev/guide/api-hmr

**Contents**:
- HMR API ​
- Required Conditional Guard ​
- IntelliSense for TypeScript ​
- hot.accept(cb) ​
- hot.accept(deps, cb) ​
- hot.dispose(cb) ​
- hot.prune(cb) ​
- hot.data ​

This is the client HMR API. For handling HMR update in plugins, see handleHotUpdate.

The manual HMR API is primarily intended for framework and tooling authors. As an end user, HMR is likely already handled for you in the framework specific starter templates.

Vite exposes its manual HMR API via the special import.meta.hot object:

First of all, make sure to guard all HMR API usage with a conditional block so that the code can be tree-shaken in production:

Vite provides type definitions for import.meta.hot in vite/client.d.ts. You can add "vite/client" in the tsconfig.json so TypeScript picks up the type definitions:

For a module to self-accept, use import.meta.hot.accept with a callback which receives the updated module:

A module that "accepts" hot updates is considered an HMR boundary.

Vite's HMR does not actually swap the originally imported module: if an HMR boundary module re-exports imports from a dep, then it is responsible for updating those re-exports (and these exports must be using let). In addition, importers up the chain from the boundary module will not be notified of the change. This simplified HMR implementation is sufficient for most dev use cases, while allowing us to skip the expensive work of generating proxy modules.

Vite requires that the call to this function appears as import.meta.hot.accept( (whitespace-sensitive) in the source code in order for the module to accept update. This is a requirement of the static analysis that Vite does to enable HMR support for a module.

A module can also accept updates from direct dependencies without reloading itself:

A self-accepting module or a module that expects to be accepted by others can use hot.dispose to clean-up any persistent side effects created by its updated copy:

Register a callback that will call when the module is no longer imported on the page. Compared to hot.dispose, this can be used if the source code cleans up side-effects by itself on updates and you only need to clean-up when 

*[Content truncated - see full docs]*

**Examples**:

```javascript
interface ImportMeta {
  readonly hot?: ViteHotContext
}

interface ViteHotContext {
  readonly data: any

  accept(): void
  accept(cb: (mod: ModuleNamespace | undefined) => void): void
  accept(dep: string, cb: (mod: ModuleNamespace | undefined) => void): void
  accept(
    deps: readonly string[],
    cb: (mods: Array<ModuleNamespace | undefined>) => void,
  ): void

  dispose(cb: (data: any) => void): void
  prune(cb: (data: any) => void): void
  invalidate(message?: string): void

  on<T ex
...
```

```text
if (import.meta.hot) {
  // HMR code
}
```

```text
{
  "compilerOptions": {
    "types": ["vite/client"]
  }
}
```

---

## JavaScript API ​

**URL**: https://vitejs.dev/guide/api-javascript

**Contents**:
- JavaScript API ​
- createServer ​
- InlineConfig ​
- ResolvedConfig ​
- ViteDevServer ​
- build ​
- preview ​
- PreviewServer ​

Vite's JavaScript APIs are fully typed, and it's recommended to use TypeScript or enable JS type checking in VS Code to leverage the intellisense and validation.

When using createServer and build in the same Node.js process, both functions rely on process.env.NODE_ENV to work properly, which also depends on the mode config option. To prevent conflicting behavior, set process.env.NODE_ENV or the mode of the two APIs to development. Otherwise, you can spawn a child process to run the APIs separately.

When using middleware mode combined with proxy config for WebSocket, the parent http server should be provided in middlewareMode to bind the proxy correctly.

The InlineConfig interface extends UserConfig with additional properties:

The ResolvedConfig interface has all the same properties of a UserConfig, except most properties are resolved and non-undefined. It also contains utilities like:

waitForRequestsIdle is meant to be used as a escape hatch to improve DX for features that can't be implemented following the on-demand nature of the Vite dev server. It can be used during startup by tools like Tailwind to delay generating the app CSS classes until the app code has been seen, avoiding flashes of style changes. When this function is used in a load or transform hook, and the default HTTP1 server is used, one of the six http channels will be blocked until the server processes all static imports. Vite's dependency optimizer currently uses this function to avoid full-page reloads on missing dependencies by delaying loading of pre-bundled dependencies until all imported dependencies have been collected from static imported sources. Vite may switch to a different strategy in a future major release, setting optimizeDeps.crawlUntilStaticImports: false by default to avoid the performance hit in large applications during cold start.

The command value is serve in dev and preview, and build in build.

Deeply merge two Vite configs. isRoot represents the level within the Vite c

*[Content truncated - see full docs]*

**Examples**:

```javascript
async function createServer(inlineConfig?: InlineConfig): Promise<ViteDevServer>
```

```python
import { fileURLToPath } from 'node:url'
import { createServer } from 'vite'

const __dirname = fileURLToPath(new URL('.', import.meta.url))

const server = await createServer({
  // any valid user config options, plus `mode` and `configFile`
  configFile: false,
  root: __dirname,
  server: {
    port: 1337,
  },
})
await server.listen()

server.printUrls()
server.bindCLIShortcuts({ print: true })
```

```python
import http from 'http'
import { createServer } from 'vite'

const parentServer = http.createServer() // or express, koa, etc.

const vite = await createServer({
  server: {
    // Enable middleware mode
    middlewareMode: {
      // Provide the parent http server for proxy WebSocket
      server: parentServer,
    },
    proxy: {
      '/ws': {
        target: 'ws://localhost:3000',
        // Proxying WebSocket
        ws: true,
      },
    },
  },
})

parentServer.use(vite.middlewares)
```

---

## Plugin API ​

**URL**: https://vitejs.dev/guide/api-plugin

**Contents**:
- Plugin API ​
- Authoring a Plugin ​
- Conventions ​
- Plugins Config ​
- Simple Examples ​
  - Transforming Custom File Types ​
  - Importing a Virtual File ​
- Virtual Modules Convention ​

Vite plugins extends Rollup's well-designed plugin interface with a few extra Vite-specific options. As a result, you can write a Vite plugin once and have it work for both dev and build.

It is recommended to go through Rollup's plugin documentation first before reading the sections below.

Vite strives to offer established patterns out of the box, so before creating a new plugin make sure that you check the Features guide to see if your need is covered. Also review available community plugins, both in the form of a compatible Rollup plugin and Vite Specific plugins

When creating a plugin, you can inline it in your vite.config.js. There is no need to create a new package for it. Once you see that a plugin was useful in your projects, consider sharing it to help others in the ecosystem.

When learning, debugging, or authoring plugins, we suggest including vite-plugin-inspect in your project. It allows you to inspect the intermediate state of Vite plugins. After installing, you can visit localhost:5173/__inspect/ to inspect the modules and transformation stack of your project. Check out install instructions in the vite-plugin-inspect docs.

If the plugin doesn't use Vite specific hooks and can be implemented as a Compatible Rollup Plugin, then it is recommended to use the Rollup Plugin naming conventions.

This exposes the plugin to be also used in pure Rollup or WMR based projects

For Vite only plugins

If your plugin is only going to work for a particular framework, its name should be included as part of the prefix

See also Virtual Modules Convention.

Users will add plugins to the project devDependencies and configure them using the plugins array option.

Falsy plugins will be ignored, which can be used to easily activate or deactivate plugins.

plugins also accepts presets including several plugins as a single element. This is useful for complex features (like framework integration) that are implemented using several plugins. The array will be flattened intern

*[Content truncated - see full docs]*

**Examples**:

```python
import vitePlugin from 'vite-plugin-feature'
import rollupPlugin from 'rollup-plugin-feature'

export default defineConfig({
  plugins: [vitePlugin(), rollupPlugin()],
})
```

```python
// framework-plugin
import frameworkRefresh from 'vite-plugin-framework-refresh'
import frameworkDevtools from 'vite-plugin-framework-devtools'

export default function framework(config) {
  return [frameworkRefresh(config), frameworkDevTools(config)]
}
```

```python
import { defineConfig } from 'vite'
import framework from 'vite-plugin-framework'

export default defineConfig({
  plugins: [framework()],
})
```

---

## Server-Side Rendering (SSR) ​

**URL**: https://vitejs.dev/guide/ssr

**Contents**:
- Server-Side Rendering (SSR) ​
- Example Projects ​
- Source Structure ​
- Conditional Logic ​
- Setting Up the Dev Server ​
- Building for Production ​
- Generating Preload Directives ​
- Pre-Rendering / SSG ​

SSR specifically refers to front-end frameworks (for example React, Preact, Vue, and Svelte) that support running the same application in Node.js, pre-rendering it to HTML, and finally hydrating it on the client. If you are looking for integration with traditional server-side frameworks, check out the Backend Integration guide instead.

The following guide also assumes prior experience working with SSR in your framework of choice, and will only focus on Vite-specific integration details.

This is a low-level API meant for library and framework authors. If your goal is to create an application, make sure to check out the higher-level SSR plugins and tools at Awesome Vite SSR section first. That said, many applications are successfully built directly on top of Vite's native low-level API.

Currently, Vite is working on an improved SSR API with the Environment API. Check out the link for more details.

Vite provides built-in support for server-side rendering (SSR). create-vite-extra contains example SSR setups you can use as references for this guide:

You can also scaffold these projects locally by running create-vite and choose Others > create-vite-extra under the framework option.

A typical SSR application will have the following source file structure:

The index.html will need to reference entry-client.js and include a placeholder where the server-rendered markup should be injected:

You can use any placeholder you prefer instead of <!--ssr-outlet-->, as long as it can be precisely replaced.

If you need to perform conditional logic based on SSR vs. client, you can use

This is statically replaced during build so it will allow tree-shaking of unused branches.

When building an SSR app, you likely want to have full control over your main server and decouple Vite from the production environment. It is therefore recommended to use Vite in middleware mode. Here is an example with express:

Here vite is an instance of ViteDevServer. vite.middlewares is a Connect instan

*[Content truncated - see full docs]*

**Examples**:

```text
- index.html
- server.js # main application server
- src/
  - main.js          # exports env-agnostic (universal) app code
  - entry-client.js  # mounts the app to a DOM element
  - entry-server.js  # renders the app using the framework's SSR API
```

```text
<div id="app"><!--ssr-outlet--></div>
<script type="module" src="/src/entry-client.js"></script>
```

```text
if (import.meta.env.SSR) {
  // ... server only logic
}
```

---

## Static Asset Handling ​

**URL**: https://vitejs.dev/guide/assets

**Contents**:
- Static Asset Handling ​
- Importing Asset as URL ​
  - Explicit URL Imports ​
  - Explicit Inline Handling ​
  - Importing Asset as String ​
  - Importing Script as a Worker ​
- The public Directory ​
- new URL(url, import.meta.url) ​

Importing a static asset will return the resolved public URL when it is served:

For example, imgUrl will be /src/img.png during development, and become /assets/img.2d8efhg.png in the production build.

The behavior is similar to webpack's file-loader. The difference is that the import can be either using absolute public paths (based on project root during dev) or relative paths.

url() references in CSS are handled the same way.

If using the Vue plugin, asset references in Vue SFC templates are automatically converted into imports.

Common image, media, and font filetypes are detected as assets automatically. You can extend the internal list using the assetsInclude option.

Referenced assets are included as part of the build assets graph, will get hashed file names, and can be processed by plugins for optimization.

Assets smaller in bytes than the assetsInlineLimit option will be inlined as base64 data URLs.

Git LFS placeholders are automatically excluded from inlining because they do not contain the content of the file they represent. To get inlining, make sure to download the file contents via Git LFS before building.

TypeScript, by default, does not recognize static asset imports as valid modules. To fix this, include vite/client.

Inlining SVGs through url()

When passing a URL of SVG to a manually constructed url() by JS, the variable should be wrapped within double quotes.

Assets that are not included in the internal list or in assetsInclude can be explicitly imported as a URL using the ?url suffix. This is useful, for example, to import Houdini Paint Worklets.

Assets can be explicitly imported with inlining or no inlining using the ?inline or ?no-inline suffix respectively.

Assets can be imported as strings using the ?raw suffix.

Scripts can be imported as web workers with the ?worker or ?sharedworker suffix.

Check out the Web Worker section for more details.

If you have assets that are:

Then you can place the asset in a special public directory u

*[Content truncated - see full docs]*

**Examples**:

```python
import imgUrl from './img.png'
document.getElementById('hero-img').src = imgUrl
```

```python
import imgUrl from './img.svg'
document.getElementById('hero-img').style.background = `url("${imgUrl}")`
```

```python
import workletURL from 'extra-scalloped-border/worklet.js?url'
CSS.paintWorklet.addModule(workletURL)
```

---

## Using Plugins ​

**URL**: https://vitejs.dev/guide/using-plugins

**Contents**:
- Using Plugins ​
- Adding a Plugin ​
- Finding Plugins ​
- Enforcing Plugin Ordering ​
- Conditional Application ​
- Building Plugins ​

Vite can be extended using plugins, which are based on Rollup's well-designed plugin interface with a few extra Vite-specific options. This means that Vite users can rely on the mature ecosystem of Rollup plugins, while also being able to extend the dev server and SSR functionality as needed.

To use a plugin, it needs to be added to the devDependencies of the project and included in the plugins array in the vite.config.js config file. For example, to provide support for legacy browsers, the official @vitejs/plugin-legacy can be used:

plugins also accepts presets including several plugins as a single element. This is useful for complex features (like framework integration) that are implemented using several plugins. The array will be flattened internally.

Falsy plugins will be ignored, which can be used to easily activate or deactivate plugins.

Vite aims to provide out-of-the-box support for common web development patterns. Before searching for a Vite or compatible Rollup plugin, check out the Features Guide. A lot of the cases where a plugin would be needed in a Rollup project are already covered in Vite.

Check out the Plugins section for information about official plugins. Community plugins are listed in awesome-vite.

You can also find plugins that follow the recommended conventions using a npm search for vite-plugin for Vite plugins or a npm search for rollup-plugin for Rollup plugins.

For compatibility with some Rollup plugins, it may be needed to enforce the order of the plugin or only apply at build time. This should be an implementation detail for Vite plugins. You can enforce the position of a plugin with the enforce modifier:

Check out Plugins API Guide for detailed information.

By default, plugins are invoked for both serve and build. In cases where a plugin needs to be conditionally applied only during serve or build, use the apply property to only invoke them during 'build' or 'serve':

Check out the Plugins API Guide for documentation about crea

*[Content truncated - see full docs]*

**Examples**:

```text
$ npm add -D @vitejs/plugin-legacy
```

```python
import legacy from '@vitejs/plugin-legacy'
import { defineConfig } from 'vite'

export default defineConfig({
  plugins: [
    legacy({
      targets: ['defaults', 'not IE 11'],
    }),
  ],
})
```

```python
import image from '@rollup/plugin-image'
import { defineConfig } from 'vite'

export default defineConfig({
  plugins: [
    {
      ...image(),
      enforce: 'pre',
    },
  ],
})
```

---

## Why Vite ​

**URL**: https://vitejs.dev/guide/why

**Contents**:
- Why Vite ​
- The Problems ​
  - Slow Server Start ​
  - Slow Updates ​
- Why Bundle for Production ​
- Why Not Bundle with esbuild? ​
- How Vite Relates to Other Unbundled Build Tools? ​

Before ES modules were available in browsers, developers had no native mechanism for authoring JavaScript in a modularized fashion. This is why we are all familiar with the concept of "bundling": using tools that crawl, process and concatenate our source modules into files that can run in the browser.

Over time we have seen tools like webpack, Rollup and Parcel, which greatly improved the development experience for frontend developers.

However, as we build more and more ambitious applications, the amount of JavaScript we are dealing with is also increasing dramatically. It is not uncommon for large scale projects to contain thousands of modules. We are starting to hit a performance bottleneck for JavaScript based tooling: it can often take an unreasonably long wait (sometimes up to minutes!) to spin up a dev server, and even with Hot Module Replacement (HMR), file edits can take a couple of seconds to be reflected in the browser. The slow feedback loop can greatly affect developers' productivity and happiness.

Vite aims to address these issues by leveraging new advancements in the ecosystem: the availability of native ES modules in the browser, and the rise of JavaScript tools written in compile-to-native languages.

When cold-starting the dev server, a bundler-based build setup has to eagerly crawl and build your entire application before it can be served.

Vite improves the dev server start time by first dividing the modules in an application into two categories: dependencies and source code.

Dependencies are mostly plain JavaScript that do not change often during development. Some large dependencies (e.g. component libraries with hundreds of modules) are also quite expensive to process. Dependencies may also be shipped in various module formats (e.g. ESM or CommonJS).

Vite pre-bundles dependencies using esbuild. esbuild is written in Go and pre-bundles dependencies 10-100x faster than JavaScript-based bundlers.

Source code often contains non-plain JavaScrip

*[Content truncated - see full docs]*

---
