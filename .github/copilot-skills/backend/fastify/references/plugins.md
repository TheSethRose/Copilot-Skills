# Fastify - Plugins

**Pages**: 2

---

## Middleware

**URL**: https://fastify.dev/docs/latest/Reference/Middleware/

**Contents**:
- Middleware
- Middleware​
    - Restrict middleware execution to certain paths​
  - Alternatives​

Starting with Fastify v3.0.0, middleware is not supported out of the box and requires an external plugin such as @fastify/express or @fastify/middie.

An example of registering the @fastify/express plugin to use Express middleware:

@fastify/middie can also be used, which provides support for simple Express-style middleware with improved performance:

Middleware can be encapsulated, allowing control over where it runs using register as explained in the plugins guide.

Fastify middleware does not expose the send method or other methods specific to the Fastify Reply instance. This is because Fastify wraps the incoming req and res Node instances using the Request and Reply objects internally, but this is done after the middleware phase. To create middleware, use the Node req and res instances. Alternatively, use the preHandler hook that already has the Fastify Request and Reply instances. For more information, see Hooks.

To run middleware under certain paths, pass the path as the first parameter to use.

ℹ️ Note: This does not support routes with parameters (e.g. /user/:id/comments) and wildcards are not supported in multiple paths.

Fastify offers alternatives to commonly used middleware, such as @fastify/helmet for helmet, @fastify/cors for cors, and @fastify/static for serve-static.

**Examples**:

```js
await fastify.register(require('@fastify/express'))fastify.use(require('cors')())fastify.use(require('dns-prefetch-control')())fastify.use(require('frameguard')())fastify.use(require('hsts')())fastify.use(require('ienoopen')())fastify.use(require('x-xss-protection')())
```

```js
await fastify.register(require('@fastify/middie'))fastify.use(require('cors')())
```

```js
const path = require('node:path')const serveStatic = require('serve-static')// Single pathfastify.use('/css', serveStatic(path.join(__dirname, '/assets')))// Wildcard pathfastify.use('/css/(.*)', serveStatic(path.join(__dirname, '/assets')))// Multiple pathsfastify.use(['/css', '/js'], serveStatic(path.join(__dirname, '/assets')))
```

---

## Plugins

**URL**: https://fastify.dev/docs/latest/Reference/Plugins/

**Contents**:
- Plugins
- Plugins​
  - Plugin Options​
    - Route Prefixing option​
    - Error handling​
  - async/await​
    - ESM support​
  - Create a plugin​

Fastify can be extended with plugins, which can be a set of routes, a server decorator, or other functionality. Use the register API to add one or more plugins.

By default, register creates a new scope, meaning changes to the Fastify instance (via decorate) will not affect the current context ancestors, only its descendants. This feature enables plugin encapsulation and inheritance, creating a directed acyclic graph (DAG) and avoiding cross-dependency issues.

The Getting Started guide includes an example of using this API:

The optional options parameter for fastify.register supports a predefined set of options that Fastify itself will use, except when the plugin has been wrapped with fastify-plugin. This options object will also be passed to the plugin upon invocation, regardless of whether or not the plugin has been wrapped. The currently supported list of Fastify specific options is:

These options will be ignored when used with fastify-plugin.

To avoid collisions, a plugin should consider namespacing its options. For example, a plugin foo might be registered like so:

If collisions are not a concern, the plugin may accept the options object as-is:

The options parameter can also be a Function evaluated at plugin registration, providing access to the Fastify instance via the first argument:

The Fastify instance passed to the function is the latest state of the external Fastify instance the plugin was declared on, allowing access to variables injected via decorate by preceding plugins according to the order of registration. This is useful if a plugin depends on changes made to the Fastify instance by a preceding plugin, such as utilizing an existing database connection.

Keep in mind that the Fastify instance passed to the function is the same as the one passed into the plugin, a copy of the external Fastify instance rather than a reference. Any usage of the instance will behave the same as it would if called within the plugin's function. For example, if decor

*[Content truncated - see full docs]*

**Examples**:

```js
fastify.register(plugin, [options])
```

```js
fastify.register(require('fastify-foo'), {  prefix: '/foo',  foo: {    fooOption1: 'value',    fooOption2: 'value'  }})
```

```js
fastify.register(require('fastify-foo'), {  prefix: '/foo',  fooOption1: 'value',  fooOption2: 'value'})
```

---
