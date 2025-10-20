# Fastify - Getting Started

**Pages**: 1

---

## Getting-Started

**URL**: https://fastify.dev/docs/latest/Guides/Getting-Started/

**Contents**:
- Getting-Started
- Getting Started​
  - Install​
  - Your first server​
  - Your first plugin​
  - Loading order of your plugins​
  - Validate your data​
  - Serialize your data​

Hello! Thank you for checking out Fastify!

This document aims to be a gentle introduction to the framework and its features. It is an elementary preface with examples and links to other parts of the documentation.

Let's write our first server:

If you are using ECMAScript Modules (ESM) in your project, be sure to include "type": "module" in your package.json.

Do you prefer to use async/await? Fastify supports it out-of-the-box.

Awesome, that was easy.

Unfortunately, writing a complex application requires significantly more code than this example. A classic problem when you are building a new application is how to handle multiple files, asynchronous bootstrapping, and the architecture of your code.

Fastify offers an easy platform that helps to solve all of the problems outlined above, and more!

Note The above examples, and subsequent examples in this document, default to listening only on the localhost 127.0.0.1 interface. To listen on all available IPv4 interfaces the example should be modified to listen on 0.0.0.0 like so:

Similarly, specify ::1 to accept only local connections via IPv6. Or specify :: to accept connections on all IPv6 addresses, and, if the operating system supports it, also on all IPv4 addresses.

When deploying to a Docker (or another type of) container using 0.0.0.0 or :: would be the easiest method for exposing the application.

Note that when using 0.0.0.0, the address provided in the callback argument above will be the first address the wildcard refers to.

As with JavaScript, where everything is an object, with Fastify everything is a plugin.

Before digging into it, let's see how it works!

Let's declare our basic server, but instead of declaring the route inside the entry point, we'll declare it in an external file (check out the route declaration docs).

In this example, we used the register API, which is the core of the Fastify framework. It is the only way to add routes, plugins, et cetera.

At the beginning of this guide, we no

*[Content truncated - see full docs]*

**Examples**:

```sh
npm i fastify
```

```sh
yarn add fastify
```

```js
// Require the framework and instantiate it// ESMimport Fastify from 'fastify'const fastify = Fastify({  logger: true})// CommonJsconst fastify = require('fastify')({  logger: true})// Declare a routefastify.get('/', function (request, reply) {  reply.send({ hello: 'world' })})// Run the server!fastify.listen({ port: 3000 }, function (err, address) {  if (err) {    fastify.log.error(err)    process.exit(1)  }  // Server is now listening on ${address}})
```

---
