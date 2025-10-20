# Vercel - Frameworks

**Pages**: 21

---

## Astro on Vercel

**URL**: https://vercel.com/docs/frameworks/frontend/astro

**Contents**:
- Astro on Vercel
- Get Started with Astro on Vercel
- Deploy a new Astro project with a template
- Using Vercel's features with Astro
  - Configuration options
- Server-Side Rendering
  - Static rendering
- Incremental Static Regeneration

Astro is an all-in-one web framework that enables you to build performant static websites. People choose Astro when they want to build content-rich experiences with as little JavaScript as possible.

You can deploy a static Astro app to Vercel with zero configuration.

To get started with Astro on Vercel:

Get started in minutes

A minimal, responsive and SEO-friendly Astro blog theme.

Starter template for startups, marketing websites & blogs built with Astro and TailwindCSS.

The official 'Getting Started' template for Astro.

Vercel deployments can integrate with your git provider to generate preview URLs for each pull request you make to your Astro project.

To deploy a server-rendered Astro app, or a static Astro site with Vercel features like Web Analytics and Image Optimization, you must:

Add Astro's Vercel adapter to your project. There are two ways to do so:

Configure your project. In your astro.config.ts file, import either the serverless or static plugin, and set the output to server or static respectively:

Enable Vercel's features using Astro's configuration options. The following example astro.config.ts enables Web Analytics and adds a maximum duration to Vercel Function routes:

The following configuration options enable Vercel's features for Astro deployments.

For more details on the configuration options, see Astro's docs.

Using SSR, or on-demand rendering as Astro calls it, enables you to deploy your routes as Vercel functions on Vercel. This allows you to add dynamic elements to your app, such as user logins and personalized content.

You can enable SSR by adding the Vercel adapter to your project.

If your Astro project is statically rendered, you can opt individual routes. To do so:

Set your output option to hybrid in your <PreferredExtension filename="astro.config" mjs />:

Add export const prerender = false; to your components:

SSR with Astro on Vercel:

Learn more about Astro SSR

Statically rendered, or pre-rendered, Astro apps can be 

*[Content truncated - see full docs]*

**Examples**:

```text
pnpm astro add vercel
```

```text
pnpm i @astrojs/vercel
```

```python
import { defineConfig } from 'astro/config';
// Import /serverless for a Serverless SSR site
import vercelServerless from '@astrojs/vercel/serverless';
 
export default defineConfig({
  output: 'server',
  adapter: vercelServerless(),
});
```

---

## Backends on Vercel

**URL**: https://vercel.com/docs/frameworks/backend

**Contents**:
- Backends on Vercel
- Zero-configuration backends
  - Express
  - FastAPI
  - Flask
  - Hono
  - Nitro
  - xmcp

Backends deployed to Vercel receive the benefits of Vercel's infrastructure, including:

Deploy the following backends to Vercel with zero-configuration.

Fast, unopinionated, minimalist web framework for Node.js

FastAPI framework, high performance, easy to learn, fast to code, ready for production

The Python micro web framework

Web framework built on Web Standards

Nitro is a next generation server toolkit.

The MCP framework for building AI-powered tools

If you are transitioning from a fully managed server or containerized environment to Vercel’s serverless architecture, you may need to rethink a few concepts in your application since there is no longer a server always running in the background.

The following are generally applicable to serverless, and therefore Vercel Functions (running with or without Fluid compute):

Serverless functions have maximum execution limits and should respond as quickly as possible. They should not subscribe to data events. Instead, we need a client that subscribes to data events and a serverless functions that publishes new data. Consider using a serverless friendly realtime data provider.

To manage database connections efficiently, use the attachDatabasePool function from @vercel/functions.

---

## Create React App on Vercel

**URL**: https://vercel.com/docs/frameworks/frontend/create-react-app

**Contents**:
- Create React App on Vercel
- Get Started with CRA on Vercel
- Deploy a new CRA project with a template
- Static file caching
- Preview Deployments
  - Comments
- Web Analytics
- Speed Insights

Create React App (CRA) is a development environment for building single-page applications with the React framework. It sets up and configures a new React project with the latest JavaScript features, and optimizes your app for production.

To get started with CRA on Vercel:

Get started in minutes

A client-side React app created with create-react-app.

React application that implements user login, logout and sign-up features using Auth0.

Vercel deployments can integrate with your git provider to generate preview URLs for each pull request you make to your CRA project.

On Vercel, static files are replicated and deployed to every region in our global CDN after the first request. This ensures that static files are served from the closest location to the visitor, improving performance and reducing latency.

Static files are cached for up to 31 days. If a file is unchanged, it can persist across deployments, as their hash caches static files. However, the cache is effectively invalidated when you redeploy, so we always serve the latest version.

To summarize, using Static Files with CRA on Vercel:

Learn more about static files caching

When you deploy your CRA app to Vercel and connect your git repo, every pull request will generate a Preview Deployment.

Preview Deployments allow you to preview changes to your app in a live deployment. They are available by default for all projects, and are generated when you commit changes to a Git branch with an open pull request, or you create a deployment using Vercel CLI.

You can use the comments feature to receive feedback on your Preview Deployments from Vercel Team members and people you share the Preview URL with.

Comments allow you to start discussion threads, share screenshots, send notifications, and more.

To summarize, Preview Deployments with CRA on Vercel:

Learn more about Preview Deployments

Vercel's Web Analytics features enable you to visualize and monitor your application's performance over time. The Analytics

*[Content truncated - see full docs]*

**Examples**:

```python
import { inject } from '@vercel/analytics';
 
inject();
```

---

## Express on Vercel

**URL**: https://vercel.com/docs/frameworks/backend/express

**Contents**:
- Express on Vercel
- Get started with Express on Vercel
  - Get started with Vercel CLI
- Exporting the Express application
  - Using a default export
  - Using a port listener
  - Local development
  - Deploying the application

Express is a fast, unopinionated, minimalist web framework for Node.js. You can deploy an Express app to Vercel with zero configuration.

Express applications on Vercel benefit from:

You can quickly deploy an Express application to Vercel by creating an Express app or using an existing one:

Get started by initializing a new Express project using Vercel CLI init command:

This will clone the Express example repository in a directory called express.

To run an Express application on Vercel, create a file that imports the express package at any one of the following locations:

The file must also export the application as a default export of the module or use a port listener.

For example, use the following code that exports your Express app:

You may also run your application using the app.listen pattern that exposes the server on a port.

Use vercel dev to run your application locally

To deploy, connect your Git repository or use Vercel CLI:

To serve static assets, place them in the public/** directory. They will be served as a part of our CDN using default headers unless otherwise specified in vercel.json.

express.static() will be ignored and will not serve static assets.

When you deploy an Express app to Vercel, your Express application becomes a single Vercel Function and uses Fluid compute by default. This means your Express app will automatically scale up and down based on traffic.

Additionally, all Vercel Functions limitations apply to the Express application, including:

Learn more about deploying Express projects on Vercel with the following resources:

**Examples**:

```text
vc init express
```

```python
// Use "type: module" in package.json to use ES modules
import express from 'express';
const app = express();
 
// Define your routes
app.get('/', (req, res) => {
  res.json({ message: 'Hello from Express on Vercel!' });
});
 
// Export the Express app
export default app;
```

```python
// Use "type: module" in package.json to use ES modules
import express from 'express';
const app = express();
const port = 3000;
 
// Define your routes
app.get('/', (req, res) => {
  res.json({ message: 'Hello from Express on Vercel!' });
});
 
app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
```

---

## FastAPI on Vercel

**URL**: https://vercel.com/docs/frameworks/backend/fastapi

**Contents**:
- FastAPI on Vercel
- Get started with FastAPI on Vercel
  - Get started with Vercel CLI
- Exporting the FastAPI application
  - Local development
  - Deploying the application
- Serving static assets
- Vercel Functions

FastAPI is a modern, high-performance, web framework for building APIs with Python based on standard Python type hints. You can deploy a FastAPI app to Vercel with zero configuration.

You can quickly deploy a FastAPI application to Vercel by creating a FastAPI app or using an existing one:

Get started by initializing a new FastAPI project using Vercel CLI init command:

This will clone the FastAPI example repository in a directory called fastapi.

To run a FastAPI application on Vercel, define an app instance that initializes FastAPI at any of the following entrypoints:

Use vercel dev to run your application locally.

To deploy, connect your Git repository or use Vercel CLI:

To serve static assets, place them in the public/** directory. They will be served as a part of our CDN using default headers unless otherwise specified in vercel.json.

When you deploy a FastAPI app to Vercel, the application becomes a single Vercel Function and uses Fluid compute by default. This means your FastAPI app will automatically scale up and down based on traffic.

All Vercel Functions limitations apply to FastAPI applications, including:

Learn more about deploying FastAPI projects on Vercel with the following resources:

**Examples**:

```text
vc init fastapi
```

```python
from fastapi import FastAPI
 
app = FastAPI()
 
@app.get("/")
def read_root():
    return {"Python": "on Vercel"}
```

```text
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
vercel dev
```

---

## Flask on Vercel

**URL**: https://vercel.com/docs/frameworks/backend/flask

**Contents**:
- Flask on Vercel
- Get started with Flask on Vercel
  - Get started with Vercel CLI
- Exporting the Flask application
  - Local development
  - Deploying the application
- Serving static assets
- Vercel Functions

Flask is a lightweight WSGI web application framework for Python. It's designed with simplicity and flexibility in mind, making it easy to get started while remaining powerful for building web applications. You can deploy a Flask app to Vercel with zero configuration.

You can quickly deploy a Flask application to Vercel by creating a Flask app or using an existing one:

Get started by initializing a new Flask project using Vercel CLI init command:

This will clone the Flask example repository in a directory called flask.

To run a Flask application on Vercel, define an app instance that initializes Flask at any of the following entrypoints:

Use vercel dev to run your application locally.

To deploy, connect your Git repository or use Vercel CLI:

To serve static assets, place them in the public/** directory. They will be served as a part of our CDN using default headers unless otherwise specified in vercel.json.

Flask's app.static_folder should not be used for static files on Vercel. Use the public/** directory instead.

When you deploy a Flask app to Vercel, the application becomes a single Vercel Function and uses Fluid compute by default. This means your Flask app will automatically scale up and down based on traffic.

All Vercel Functions limitations apply to Flask applications, including:

Learn more about deploying Flask projects on Vercel with the following resources:

**Examples**:

```text
vc init flask
```

```python
from flask import Flask
 
app = Flask(__name__)
 
@app.route("/")
def hello_world():
    return {"message": "Hello, World!"}
```

```text
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
vercel dev
```

---

## Frameworks on Vercel

**URL**: https://vercel.com/docs/frameworks

**Contents**:
- Frameworks on Vercel
- Deploy a Template
- Frameworks infrastructure support matrix
- Build Output API
- More resources

Vercel has first-class support for a wide range of the most popular frameworks. You can build and deploy using frontend, backend, and full-stack frameworks ranging from SvelteKit to Nitro, often without any upfront configuration.

Learn how to get started with Vercel or clone one of our example repos to your favorite git provider and deploy it on Vercel using one of the templates below:

Get started in minutes

Get started with Next.js and React in seconds.

SvelteKit Boilerplate

A SvelteKit app including nested routes, layouts, and page endpoints.

Deploying an API on Vercel with Nitro.

Vercel deployments can integrate with your git provider to generate preview URLs for each pull request you make to your project.

Deploying on Vercel with one of our supported frameworks gives you access to many features, such as:

The following table shows which features are supported by each framework on Vercel. The framework list represents the most popular frameworks deployed on Vercel.

Support for static assets being served and cached directly from the edge

Lets you configure incoming requests, set headers, and cache responses

Execute code before a request is processed

Server-Side Rendering

Render pages dynamically on the server

Stream responses and render parts of the UI as they become ready

Incremental Static Regeneration

Create or update content on your site without redeploying

Optimize and cache images at the edge

A granular cache for storing responses from fetches

Native OG Image Generation

Generate dynamic open graph images using Vercel Functions

Multi-runtime support (different routes)

Customize runtime environments per route

Multi-runtime support (entire app)

Lets your whole application utilize different runtime environments

Analyzes build artifacts to identify and include only necessary files for the runtime

Ensure that only the latest deployment version serves your traffic by not serving older versions of code

Framework-native integrated middlewar

*[Content truncated - see full docs]*

---

## Frontends on Vercel

**URL**: https://vercel.com/docs/frameworks/frontend

**Contents**:
- Frontends on Vercel
  - Angular
  - Astro
  - Brunch
  - React
  - Docusaurus (v1)
  - Docusaurus (v2+)
  - Dojo

The following frontend frameworks are supported with zero-configuration.

Angular is a TypeScript-based cross-platform framework from Google.

Astro is a new kind of static site builder for the modern web. Powerful developer experience meets lightweight output.

Brunch is a fast and simple webapp build tool with seamless incremental compilation for rapid development.

Create React App allows you to get going with React in no time.

Docusaurus makes it easy to maintain Open Source documentation websites.

Docusaurus makes it easy to maintain Open Source documentation websites.

Dojo is a modern progressive, TypeScript first framework.

11ty is a simpler static site generator written in JavaScript, created to be an alternative to Jekyll.

Ember.js helps webapp developers be more productive out of the box.

The fastest way to create an HTML app

Gatsby helps developers build blazing fast websites and apps with React.

Gridsome is a Vue.js-powered framework for building websites & apps that are fast by default.

Universal, Tiny, and Fast Servers

Hexo is a fast, simple & powerful blog framework powered by Node.js.

Hugo is the world’s fastest framework for building websites, written in Go.

React framework for headless commerce

Ionic Angular allows you to build mobile PWAs with Angular and the Ionic Framework.

Ionic React allows you to build mobile PWAs with React and the Ionic Framework.

Jekyll makes it super easy to transform your plain text into static websites and blogs.

Middleman is a static site generator that uses all the shortcuts and tools in modern web development.

Framework for building efficient, scalable Node.js server-side applications

Parcel is a zero configuration build tool for the web that scales to projects of any size and complexity.

Polymer is an open-source webapps library from Google, for building using Web Components.

Preact is a fast 3kB alternative to React with the same modern API.

Declarative routing for React

Saber is a framework f

*[Content truncated - see full docs]*

---

## Full-stack frameworks on Vercel

**URL**: https://vercel.com/docs/frameworks/full-stack

**Contents**:
- Full-stack frameworks on Vercel
  - Next.js
  - Nuxt
  - RedwoodJS
  - Remix
  - SvelteKit
- Frameworks infrastructure support matrix

The following full-stack frameworks are supported with zero-configuration.

Next.js makes you productive with React instantly — whether you want to build static or dynamic sites.

Nuxt is the open source framework that makes full-stack development with Vue.js intuitive.

RedwoodJS is a full-stack framework for the Jamstack.

Build Better Websites

SvelteKit is a framework for building web applications of all sizes.

The following table shows which features are supported by each framework on Vercel. The framework list is not exhaustive, but a representation of the most popular frameworks deployed on Vercel.

We're committed to having support for all Vercel features across frameworks, and continue to work with framework authors on adding support. This table is continually updated over time.

Support for static assets being served and cached directly from the edge

Lets you configure incoming requests, set headers, and cache responses

Execute code before a request is processed

Server-Side Rendering

Render pages dynamically on the server

Stream responses and render parts of the UI as they become ready

Incremental Static Regeneration

Create or update content on your site without redeploying

Optimize and cache images at the edge

A granular cache for storing responses from fetches

Native OG Image Generation

Generate dynamic open graph images using Vercel Functions

Multi-runtime support (different routes)

Customize runtime environments per route

Multi-runtime support (entire app)

Lets your whole application utilize different runtime environments

Analyzes build artifacts to identify and include only necessary files for the runtime

Ensure that only the latest deployment version serves your traffic by not serving older versions of code

Framework-native integrated middleware convention

---

## Gatsby on Vercel

**URL**: https://vercel.com/docs/frameworks/frontend/gatsby

**Contents**:
- Gatsby on Vercel
- Get started with Gatsby on Vercel
- Deploy a new Gatsby project with a template
- Using the Gatsby Vercel Plugin
- Server-Side Rendering
  - Using Gatsby's SSR API with Vercel
- Deferred Static Generation
- Incremental Static Regeneration

Gatsby is an open-source static-site generator. It enables developers to build fast and secure websites that integrate different content, APIs, and services.

Gatsby also has a large ecosystem of plugins and tools that improve the development experience. Vercel supports many Gatsby features, including Server-Side Rendering, Deferred Static Generation, API Routes, and more.

To get started with Gatsby on Vercel:

Get started in minutes

A Gatsby starter template using v5.

Turborepo & Gatsby Starter

This is an official starter Turborepo with a Gatsby app, a Next.js app, and a React.js component library shared by both applications.

Vercel deployments can integrate with your git provider to generate preview URLs for each pull request you make to your Gatsby project.

Gatsby v4+ sites deployed to Vercel will automatically detect Gatsby usage and install the @vercel/gatsby-plugin-vercel-builder plugin.

To deploy your Gatsby site to Vercel, do not install the @vercel/gatsby-plugin-vercel-builder plugin yourself, or add it to your gatsby-config.js file.

Gatsby v5 sites require Node.js 20 or higher.

Vercel persists your Gatsby project's .cache directory across builds.

Server-Side Rendering (SSR) allows you to render pages dynamically on the server. This is useful for pages where the rendered data needs to be unique on every request. For example, verifying authentication or checking the geolocation of an incoming request.

Vercel offers SSR that scales down resource consumption when traffic is low, and scales up with traffic surges. This protects your site from accruing costs during periods of no traffic or losing business during high-traffic periods.

You can server-render pages in your Gatsby application on Vercel using Gatsby's native Server-Side Rendering API. These pages will be deployed to Vercel as Vercel functions.

To server-render a Gatsby page, you must export an async function called getServerData. The function can return an object with several optional key

*[Content truncated - see full docs]*

**Examples**:

```python
import type { GetServerDataProps, GetServerDataReturn } from 'gatsby';
 
type ServerDataProps = {
  hello: string;
};
 
const Page = (props: PageProps) => {
  const { name } = props.serverData;
  return <div>Hello, {name}</div>;
};
 
export async function getServerData(
  props: GetServerDataProps,
): GetServerDataReturn<ServerDataProps> {
  try {
    const res = await fetch(`https://example-data-source.com/api/some-data`);
    return {
      props: await res.json(),
    };
  } catch (error) {
 
...
```

```python
import type { GatsbyNode } from 'gatsby';
 
export const createPages: GatsbyNode['createPages'] = async ({ actions }) => {
  const { createPage } = actions;
  createPage({
    defer: true,
    path: '/using-dsg',
    component: require.resolve('./src/templates/using-dsg.js'),
    context: {},
  });
};
```

```python
import type { VercelRequest, VercelResponse } from '@vercel/node';
 
export default function handler(
  request: VercelRequest,
  response: VercelResponse,
) {
  response.status(200).json({
    body: request.body,
    query: request.query,
    cookies: request.cookies,
  });
}
```

---

## Hono on Vercel

**URL**: https://vercel.com/docs/frameworks/backend/hono

**Contents**:
- Hono on Vercel
- Get started with Hono on Vercel
  - Get started with Vercel CLI
- Exporting the Hono application
  - Local development
- Middleware
  - Hono Middleware
  - Vercel Routing Middleware

Hono is a fast and lightweight web application framework built on Web Standards. You can deploy a Hono app to Vercel with zero configuration.

Start with Hono on Vercel by using the following Hono template to deploy to Vercel with zero configuration:

Vercel deployments can integrate with your git provider to generate preview URLs for each pull request you make to your Hono project.

Get started by initializing a new Hono project using Vercel CLI init command:

This will clone the Hono example repository in a directory called hono.

To run a Hono application on Vercel, create a file that imports the hono package at any one of the following locations:

To run your Hono application locally, use Vercel CLI:

This ensures that the application will use the default export to run the same as when deployed to Vercel. The application will be available on your localhost.

Hono has the concept of "Middleware" as a part of the framework. This is different from Vercel Routing Middleware, though they can be used together.

In Hono, Middleware runs before a request handler in the framework's router. This is commonly used for loggers, CORS handling, or authentication. The code in the Hono application might look like this:

More examples of Hono Middleware can be found in the Hono documentation.

In Vercel, Routing Middleware executes code before a request is processed by the application. This gives you a way to handle rewrites, redirects, headers, and more, before returning a response. See the Routing Middleware documentation for examples.

To serve static assets, place them in the public/** directory. They will be served as a part of our CDN using default headers unless otherwise specified in vercel.json.

Hono's serveStatic() will be ignored and will not serve static assets.

When you deploy a Hono app to Vercel, your server routes automatically become Vercel Functions and use Fluid compute by default.

Vercel Functions support streaming which can be used with Hono's stream() fun

*[Content truncated - see full docs]*

**Examples**:

```text
vc init hono
```

```python
import { Hono } from 'hono';
 
const app = new Hono();
 
// ...
 
export default app;
```

```text
app.use(logger());
app.use('/posts/*', cors());
app.post('/posts/*', basicAuth());
```

---

## NestJS on Vercel

**URL**: https://vercel.com/docs/frameworks/backend/nestjs

**Contents**:
- NestJS on Vercel
- Get started with NestJS on Vercel
- NestJS entrypoint detection
  - Local development
  - Deploying the application
- Vercel Functions
- Limitations
- More resources

NestJS is a progressive Node.js framework for building efficient, reliable and scalable server-side applications. You can deploy a NestJS app to Vercel with zero configuration using Vercel Functions.

NestJS applications on Vercel benefit from:

You can quickly deploy a NestJS application to Vercel by creating a NestJS app or using an existing one:

To allow Vercel to deploy your NestJS application and process web requests, your server entrypoint file should be named one of the following:

For example, use the following code as an entrypointt:

Use vercel dev to run your application locally

To deploy, connect your Git repository or use Vercel CLI:

When you deploy a NestJS app to Vercel, your NestJS application becomes a single Vercel Function and uses Fluid compute by default. This means your NestJS app will automatically scale up and down based on traffic.

All Vercel Functions limitations apply to the NestJS application, including the size of the application being limited to 250MB.

Learn more about deploying NestJS projects on Vercel with the following resources:

---

## Next.js on Vercel

**URL**: https://vercel.com/docs/frameworks/full-stack/nextjs

**Contents**:
- Next.js on Vercel
- Getting started
- Deploy a new Next.js project with a template
- Incremental Static Regeneration
- Server-Side Rendering (SSR)
- Streaming
    - Streaming with loading and Suspense
- Partial Prerendering

Next.js is a fullstack React framework for the web, maintained by Vercel.

While Next.js works when self-hosting, deploying to Vercel is zero-configuration and provides additional enhancements for scalability, availability, and performance globally.

To get started with Next.js on Vercel:

Get started in minutes

Next.js App Router Playground

Examples of many Next.js App Router features.

Image Gallery Starter

An image gallery built on Next.js and Cloudinary.

Get started with Next.js and React in seconds.

Vercel deployments can integrate with your git provider to generate preview URLs for each pull request you make to your Next.js project.

Incremental Static Regeneration (ISR) allows you to create or update content without redeploying your site. ISR has three main benefits for developers: better performance, improved security, and faster build times.

When self-hosting, (ISR) is limited to a single region workload. Statically generated pages are not distributed closer to visitors by default, without additional configuration or vendoring of a CDN. By default, self-hosted ISR does not persist generated pages to durable storage. Instead, these files are located in the Next.js cache (which expires).

To enable ISR with Next.js in the app router, add an options object with a revalidate property to your fetch requests:

To summarize, using ISR with Next.js on Vercel:

Learn more about Incremental Static Regeneration (ISR)

Server-Side Rendering (SSR) allows you to render pages dynamically on the server. This is useful for pages where the rendered data needs to be unique on every request. For example, checking authentication or looking at the location of an incoming request.

On Vercel, you can server-render Next.js applications through Vercel Functions.

To summarize, SSR with Next.js on Vercel:

Vercel supports streaming in Next.js projects with any of the following:

Streaming data allows you to fetch information in chunks rather than all at once, speeding up Funct

*[Content truncated - see full docs]*

**Examples**:

```javascript
export default async function Page() {
  const res = await fetch('https://api.vercel.app/blog', {
    next: { revalidate: 10 }, // Seconds
  });
 
  const data = await res.json();
 
  return (
    <main>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </main>
  );
}
```

```javascript
export default function Loading() {
  return <p>Loading...</p>;
}
```

```python
import { Suspense } from 'react';
import { PostFeed, Weather } from './components';
 
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
  );
}
```

---

## Nitro on Vercel

**URL**: https://vercel.com/docs/frameworks/backend/nitro

**Contents**:
- Nitro on Vercel
- Get started with Nitro on Vercel
  - Get started with Vercel CLI
- Using Vercel's features with Nitro
- Incremental Static Regeneration (ISR)
  - On-demand revalidation
  - Create an Environment Variable
  - Update your configuration

Nitro is a full-stack framework with TypeScript-first support. It includes filesystem routing, code-splitting for fast startup, built-in caching, and multi-driver storage. It enables deployments from the same codebase to any platform with output sizes under 1MB.

You can deploy a Nitro app to Vercel with zero configuration.

To get started with Nitro on Vercel, use the following Nitro template to deploy to Vercel with zero configuration:

Vercel deployments can integrate with your git provider to generate preview URLs for each pull request you make to your Nitro project.

Get started by initializing a new Nitro project using Vercel CLI init command:

This will clone the Nitro example repository in a directory called nitro.

When you deploy a Nitro app to Vercel, you can use Vercel specific features such as Incremental Static Regeneration (ISR), preview deployments, Fluid compute, Observability, and Vercel firewall with zero or minimum configuration.

ISR allows you to create or update content without redeploying your site. ISR has three main benefits for developers: better performance, improved security, and faster build times.

With on-demand revalidation, you can purge the cache for an ISR route whenever you want, foregoing the time interval required with background revalidation.

To revalidate a path to a prerendered function:

Create an Environment Variable to store a revalidation secret by:

Update your configuration to use the revalidation secret as follows:

You can revalidate a path to a prerendered function by making a GET or HEAD request to that path with a header of x-prerender-revalidate: bypassToken

When the prerendered function endpoint is accessed with this header set, the cache will be revalidated. The next request to that function will return a fresh response.

To have more control over ISR caching, you can pass an options object to the isr route rule as shown below:

By default, query parameters are ignored by cache unless you specify them in the 

*[Content truncated - see full docs]*

**Examples**:

```text
vc init nitro
```

```text
openssl rand -base64 32
```

```typescript
export default defineNitroConfig({
  vercel: {
    config: {
      bypassToken: process.env.VERCEL_BYPASS_TOKEN,
    },
  },
});
```

---

## Nuxt on Vercel

**URL**: https://vercel.com/docs/frameworks/full-stack/nuxt

**Contents**:
- Nuxt on Vercel
- Getting started
- Deploy a new Nuxt project with a template
  - Choosing a build command
- Editing your Nuxt config
  - Using routeRules
- Vercel Functions
- Reading and writing files

Nuxt is an open-source framework that streamlines the process of creating modern Vue apps. It offers server-side rendering, SEO features, automatic code splitting, prerendering, and more out of the box. It also has an extensive catalog of community-built modules, which allow you to integrate popular tools with your projects.

You can deploy Nuxt static and server-side rendered sites on Vercel with no configuration required.

To get started with Nuxt on Vercel:

Get started in minutes

Nuxt.js 3 Boilerplate

A Nuxt.js 3 app, bootstrapped with create-nuxt-app.

A link-in-bio SaaS built with Nuxt.js, where the data lives in the URL – no database required.

Open source changelog template made with Nuxt, Vue, and Tailwindcss.

Vercel deployments can integrate with your git provider to generate preview URLs for each pull request you make to your Nuxt project.

The following table outlines the differences between nuxt build and nuxt generate on Vercel:

In general, nuxt build is likely best for most use cases. Consider using nuxt generate to build fully static sites.

You can configure your Nuxt deployment by creating a Nuxt config file in your project's root directory. It can be a TypeScript, JavaScript, or MJS file, but the Nuxt team recommends using TypeScript. Using TypeScript will allow your editor to suggest the correct names for configuration options, which can help mitigate typos.

Your Nuxt config file should default export defineNuxtConfig by default, which you can add an options object to.

The following is an example of a Nuxt config file with no options defined:

See the Nuxt Configuration Reference docs for a list of available options.

With the routeRules config option, you can:

At the moment, there is no way to configure route deployment options within your page components, but development of this feature is in progress.

The following is an example of a Nuxt config that:

To learn more about routeRules:

Vercel Functions enable developers to write functio

*[Content truncated - see full docs]*

**Examples**:

```typescript
export default defineNuxtConfig({
  // Config options here
});
```

```typescript
export default defineNuxtConfig({
  routeRules: {
    '/examples/*': { redirect: '/redirect-route' },
    '/modify-headers-route': { headers: { 'x-magic-of': 'nuxt and vercel' } },
    // Enables client-side rendering
    '/spa': { ssr: false },
  },
});
```

```javascript
export default defineEventHandler(() => 'Hello World!');
```

---

## React Router on Vercel

**URL**: https://vercel.com/docs/frameworks/frontend/react-router

**Contents**:
- React Router on Vercel
- @vercel/react-router
- Vercel React Router Preset
- Server-Side Rendering (SSR)
- Response streaming
- Cache-Control headers
- Analytics
- Using a custom server entrypoint

React Router is a multi-strategy router for React. When used as a framework, React Router enables fullstack, server-rendered React applications. Its built-in features for nested pages, error boundaries, transitions between loading states, and more, enable developers to create modern web apps.

With Vercel, you can deploy React Router applications with server-rendering or static site generation (using SPA mode) to Vercel with zero configuration.

It is highly recommended that your application uses the Vercel Preset when deploying to Vercel.

The optional @vercel/react-router package contains Vercel specific utilities for use in React Router applications. The package contains various entry points for specific use cases:

To get started, navigate to the root directory of your React Router project with your terminal and install @vercel/react-router with your preferred package manager:

When using the React Router as a framework, you should configure the Vercel Preset to enable the full feature set that Vercel offers.

To configure the Preset, add the following lines to your react-router.config file:

When this Preset is configured, your React Router application is enhanced with Vercel-specific functionality:

Server-Side Rendering (SSR) allows you to render pages dynamically on the server. This is useful for pages where the rendered data needs to be unique on every request. For example, checking authentication or looking at the location of an incoming request. Server-Side Rendering is invoked using Vercel Functions.

Routes defined in your application are deployed with server-side rendering by default.

The following example demonstrates a basic route that renders with SSR:

To summarize, Server-Side Rendering (SSR) with React Router on Vercel:

with React Router on Vercel is supported with Vercel Functions. See the Streaming with Suspense page in the React Router docs for general instructions.

Streaming with React Router on Vercel:

Learn more about Streaming

Vercel'

*[Content truncated - see full docs]*

**Examples**:

```text
pnpm i @vercel/react-router
```

```python
import { vercelPreset } from '@vercel/react-router/vite';
import type { Config } from '@react-router/dev/config';
 
export default {
  // Config options...
  // Server-side render by default, to enable SPA mode set this to `false`
  ssr: true,
  presets: [vercelPreset()],
} satisfies Config;
```

```python
import { type RouteConfig, index } from '@react-router/dev/routes';
 
export default [index('routes/home.tsx')] satisfies RouteConfig;
```

---

## Remix on Vercel

**URL**: https://vercel.com/docs/frameworks/full-stack/remix

**Contents**:
- Remix on Vercel
- Getting started
- Deploy a new Remix project with a template
- @vercel/remix
- Vercel Vite Preset
- Server-Side Rendering (SSR)
  - Vercel Functions
- Response streaming

Remix is a fullstack, server-rendered React framework. Its built-in features for nested pages, error boundaries, transitions between loading states, and more, enable developers to create modern web apps.

With Vercel, you can deploy server-rendered Remix and Remix V2 applications to Vercel with zero configuration. When using the Remix Vite plugin, static site generation using SPA mode is also supported.

It is highly recommended that your application uses the Remix Vite plugin, in conjunction with the Vercel Preset, when deploying to Vercel.

To get started with Remix on Vercel:

Get started in minutes

Ecommerce Template with Crystallize and Remix

A fully-featured eCommerce boilerplate built using Remix and Crystallize with performance in mind.

A new Remix app — the result of running `npx create-remix`.

Product Roadmap Voting App

Public roadmap app for your product powered by Rowy and Firebase

Vercel deployments can integrate with your git provider to generate preview URLs for each pull request you make to your Remix project.

The @vercel/remix package exposes useful types and utilities for Remix apps deployed on Vercel, such as:

To best experience Vercel features such as streaming, Vercel Functions, and more, we recommend importing utilities from @vercel/remix rather than from standard Remix packages such as @remix-run/node.

@vercel/remix should be used anywhere in your code that you normally would import utility functions from the following packages:

To get started, navigate to the root directory of your Remix project with your terminal and install @vercel/remix with your preferred package manager:

When using the Remix Vite plugin (highly recommended), you should configure the Vercel Preset to enable the full feature set that Vercel offers.

To configure the Preset, add the following lines to your vite.config file:

Using this Preset enables Vercel-specific functionality such as rendering your Remix application with Vercel Functions.

Server-Side Renderi

*[Content truncated - see full docs]*

**Examples**:

```text
pnpm i @vercel/remix
```

```python
import { vitePlugin as remix } from '@remix-run/dev';
import { installGlobals } from '@remix-run/node';
import { defineConfig } from 'vite';
import tsconfigPaths from 'vite-tsconfig-paths';
import { vercelPreset } from '@vercel/remix/vite';
 
installGlobals();
 
export default defineConfig({
  plugins: [
    remix({
      presets: [vercelPreset()],
    }),
    tsconfigPaths(),
  ],
});
```

```javascript
export default function IndexRoute() {
  return (
    <div style={{ fontFamily: 'system-ui, sans-serif', lineHeight: '1.4' }}>
      <h1>This route is rendered on the server</h1>
    </div>
  );
}
```

---

## Supported Frameworks on Vercel

**URL**: https://vercel.com/docs/frameworks/more-frameworks

**Contents**:
- Supported Frameworks on Vercel
- Frameworks infrastructure support matrix
- All frameworks
  - Angular
  - Astro
  - Brunch
  - React
  - Docusaurus (v1)

The following table shows which features are supported by each framework on Vercel. The framework list is not exhaustive, but a representation of the most popular frameworks deployed on Vercel.

We're committed to having support for all Vercel features across frameworks, and continue to work with framework authors on adding support. This table is continually updated over time.

Support for static assets being served and cached directly from the edge

Lets you configure incoming requests, set headers, and cache responses

Execute code before a request is processed

Server-Side Rendering

Render pages dynamically on the server

Stream responses and render parts of the UI as they become ready

Incremental Static Regeneration

Create or update content on your site without redeploying

Optimize and cache images at the edge

A granular cache for storing responses from fetches

Native OG Image Generation

Generate dynamic open graph images using Vercel Functions

Multi-runtime support (different routes)

Customize runtime environments per route

Multi-runtime support (entire app)

Lets your whole application utilize different runtime environments

Analyzes build artifacts to identify and include only necessary files for the runtime

Ensure that only the latest deployment version serves your traffic by not serving older versions of code

Framework-native integrated middleware convention

The frameworks listed below can be deployed to Vercel with minimal configuration. See our docs on framework presets to learn more about configuration.

Angular is a TypeScript-based cross-platform framework from Google.

Astro is a new kind of static site builder for the modern web. Powerful developer experience meets lightweight output.

Brunch is a fast and simple webapp build tool with seamless incremental compilation for rapid development.

Create React App allows you to get going with React in no time.

Docusaurus makes it easy to maintain Open Source documentation websites.

Docusauru

*[Content truncated - see full docs]*

---

## SvelteKit on Vercel

**URL**: https://vercel.com/docs/frameworks/full-stack/sveltekit

**Contents**:
- SvelteKit on Vercel
- Get started with SvelteKit on Vercel
- Deploy a new SvelteKit project with a template
- Use Vercel features with Svelte
  - Install SvelteKit's Vercel adapter plugin
  - Add the Vercel adapter to your Svelte config
- Configure your SvelteKit deployment
  - Configuration options

SvelteKit is a frontend framework that enables you to build Svelte applications with modern techniques, such as Server-Side Rendering, automatic code splitting, and advanced routing.

You can deploy your SvelteKit projects to Vercel with zero configuration, enabling you to use Preview Deployments, Web Analytics, Vercel functions, and more.

To get started with SvelteKit on Vercel:

Get started in minutes

SvelteKit Boilerplate

A SvelteKit app including nested routes, layouts, and page endpoints.

SvelteKit Authentication

A SvelteKit app with authentication.

An all-in-one starter kit for high-performance e-commerce sites built with SvelteKit.

Vercel deployments can integrate with your git provider to generate preview URLs for each pull request you make to your SvelteKit project.

When you create a new SvelteKit project with npm create svelte@latest, it installs adapter-auto by default. This adapter detects that you're deploying on Vercel and installs the @sveltejs/adapter-vercel plugin for you at build time.

We recommend installing the @sveltejs/adapter-vercel package yourself. Doing so will ensure version stability, slightly speed up your CI process, and allows you to configure default deployment options for all routes in your project.

The following instructions will guide you through adding the Vercel adapter to your SvelteKit project.

You can add the Vercel adapter to your SvelteKit project by running the following command:

Add the Vercel adapter to your svelte.config.js file, which should be at the root of your project directory.

You cannot use TypeScript for your SvelteKit config file.

In your svelte.config.js file, import adapter from @sveltejs/adapter-vercel, and add your preferred options. The following example shows the default configuration, which uses the Node.js runtime (which run on Vercel functions).

Learn more about configuring your Vercel deployment in our configuration section below.

You can configure how your SvelteKit project gets deplo

*[Content truncated - see full docs]*

**Examples**:

```text
pnpm i @sveltejs/adapter-vercel
```

```python
import adapter from '@sveltejs/adapter-vercel';
 
export default {
  kit: {
    adapter: adapter(),
  },
};
```

```python
import adapter from '@sveltejs/adapter-vercel';
 
/** @type {import('@sveltejs/kit').Config} */
const config = {
  kit: {
    adapter: adapter({
      runtime: 'nodejs20.x',
    }),
  },
};
 
export default config;
```

---

## Vite on Vercel

**URL**: https://vercel.com/docs/frameworks/frontend/vite

**Contents**:
- Vite on Vercel
- Getting started
- Deploy a new Vite project with a template
- Using Vite community plugins
  - vite-plugin-vercel
  - vite-plugin-ssr
- Environment Variables
- Vercel Functions

Vite is an opinionated build tool that aims to provide a faster and leaner development experience for modern web projects. Vite provides a dev server with rich feature enhancements such as pre-bundling NPM dependencies and hot module replacement, and a build command that bundles your code and outputs optimized static assets for production.

These features make Vite more desirable than out-of-the-box CLIs when building larger projects with frameworks for many developers.

Vite powers popular frameworks like SvelteKit, and is often used in large projects built with Vue, Svelte, React, Preact, and more.

To get started with Vite on Vercel:

Get started in minutes

Vue-powered Static Site Generator

Vite/Vue.js site that can be deployed to Vercel

Vercel deployments can integrate with your git provider to generate preview URLs for each pull request you make to your Vite project.

Although Vite offers modern features like SSR and Vercel functions out of the box, implementing those features can sometimes require complex configuration steps. Because of this, many Vite users prefer to use popular community plugins.

Vite's plugins are based on Rollup's plugin interface, giving Vite users access to many tools from the Rollup ecosystem as well as the Vite-specific ecosystem.

We recommend using Vite plugins to configure your project when possible.

vite-plugin-vercel is a popular community Vite plugin that implements the Build Output API spec. It enables your Vite apps to use the following Vercel features:

When using the Vercel CLI, set the port as an environment variable. To allow Vite to access this, include the environment variable in your vite.config file:

vite-plugin-ssr is another popular community Vite plugin that implements the Build Output API spec. It enables your Vite apps to do the following:

Vercel provides a set of System Environment Variables that our platform automatically populates. For example, the VERCEL_GIT_PROVIDER variable exposes the Git provider tha

*[Content truncated - see full docs]*

**Examples**:

```python
import { defineConfig } from 'vite';
import vercel from 'vite-plugin-vercel';
 
export default defineConfig({
  server: {
    port: process.env.PORT as unknown as number,
  },
  plugins: [vercel()],
});
```

```javascript
export default defineConfig(() => {
  return {
    define: {
      __APP_ENV__: process.env.VITE_VERCEL_ENV,
    },
  };
});
```

```python
import type { VercelRequest, VercelResponse } from '@vercel/node';
 
export default function handler(
  request: VercelRequest,
  response: VercelResponse,
) {
  response.status(200).json({
    body: request.body,
    query: request.query,
    cookies: request.cookies,
  });
}
```

---

## xmcp on Vercel

**URL**: https://vercel.com/docs/frameworks/backend/xmcp

**Contents**:
- xmcp on Vercel
- Get started with xmcp on Vercel
  - Get started with Vercel CLI
- Local development
- Middleware
  - xmcp Middleware
  - Vercel Routing Middleware
- Vercel Functions

xmcp is a TypeScript-first framework for building MCP-compatible backends. It provides an opinionated project structure, automatic tool discovery, and a streamlined middleware layer for request/response processing. You can deploy an xmcp app to Vercel with zero configuration.

Start with xmcp on Vercel by creating a new xmcp project:

This scaffolds a project with a src/tools/ directory for tools, optional src/middleware.ts, and an xmcp.config.ts file.

To deploy, connect your Git repository or use Vercel CLI:

Get started by initializing a new Xmcp project using Vercel CLI init command:

This will clone the Xmcp example repository in a directory called xmcp.

To run your xmcp application locally, you can use Vercel CLI:

Alternatively, use your project's dev script:

In xmcp, an optional middleware.ts lets you run code before and after tool execution. This is commonly used for logging, auth, or request shaping:

In Vercel, Routing Middleware executes before a request is processed by your application. Use it for rewrites, redirects, headers, or personalization, and combine it with xmcp's own middleware as needed.

When you deploy an xmcp app to Vercel, your server endpoints automatically run as Vercel Functions and use Fluid compute by default.

**Examples**:

```text
npx create-xmcp-app@latest
```

```text
vc init xmcp
```

```text
npm run dev
yarn dev
pnpm run dev
```

---
