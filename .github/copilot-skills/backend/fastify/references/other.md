# Fastify - Other

**Pages**: 21

---

## ContentTypeParser

**URL**: https://fastify.dev/docs/latest/Reference/ContentTypeParser/

**Contents**:
- ContentTypeParser
- Content-Type Parser​
  - Usage​
  - Using addContentTypeParser with fastify.register​
    - Correct Usage​
    - hasContentTypeParser​
    - removeContentTypeParser​
    - removeAllContentTypeParsers​

Fastify natively supports 'application/json' and 'text/plain' content types with a default charset of utf-8. These default parsers can be changed or removed.

Unsupported content types will throw an FST_ERR_CTP_INVALID_MEDIA_TYPE error.

To support other content types, use the addContentTypeParser API or an existing plugin.

As with other APIs, addContentTypeParser is encapsulated in the scope in which it is declared. If declared in the root scope, it is available everywhere; if declared in a plugin, it is available only in that scope and its children.

Fastify automatically adds the parsed request payload to the Fastify request object, accessible via request.body.

Note that for GET and HEAD requests, the payload is never parsed. For OPTIONS and DELETE requests, the payload is parsed only if a valid content-type header is provided. Unlike POST, PUT, and PATCH, the catch-all parser is not executed, and the payload is simply not parsed.

⚠ Warning: When using regular expressions to detect Content-Type, it is important to ensure proper detection. For example, to match application/*, use /^application\/([\w-]+);?/ to match the essence MIME type only.

Fastify first tries to match a content-type parser with a string value before trying to find a matching RegExp. For overlapping content types, it starts with the last one configured and ends with the first (last in, first out). To specify a general content type more precisely, first specify the general type, then the specific one, as shown below.

When using addContentTypeParser with fastify.register, avoid await when registering routes. Using await makes route registration asynchronous, potentially registering routes before addContentTypeParser is set.

In addition to addContentTypeParser, the hasContentTypeParser, removeContentTypeParser, and removeAllContentTypeParsers APIs are available.

Use the hasContentTypeParser API to check if a specific content type parser exists.

removeContentTypeParser can remove a single co

*[Content truncated - see full docs]*

**Examples**:

```js
fastify.addContentTypeParser('application/jsoff', function (request, payload, done) {  jsoffParser(payload, function (err, body) {    done(err, body)  })})// Handle multiple content types with the same functionfastify.addContentTypeParser(['text/xml', 'application/xml'], function (request, payload, done) {  xmlParser(payload, function (err, body) {    done(err, body)  })})// Async is also supported in Node versions >= 8.0.0fastify.addContentTypeParser('application/jsoff', async function (request
...
```

```js
// Here only the second content type parser is called because its value also matches the first onefastify.addContentTypeParser('application/vnd.custom+xml', (request, body, done) => {} )fastify.addContentTypeParser('application/vnd.custom', (request, body, done) => {} )// Here the desired behavior is achieved because fastify first tries to match the// `application/vnd.custom+xml` content type parserfastify.addContentTypeParser('application/vnd.custom', (request, body, done) => {} )fastify.addCon
...
```

```js
const fastify = require('fastify')();fastify.register((fastify, opts) => {  fastify.addContentTypeParser('application/json', function (request, payload, done) {    jsonParser(payload, function (err, body) {      done(err, body)    })  })  fastify.get('/hello', async (req, res) => {});});
```

---

## Decorators

**URL**: https://fastify.dev/docs/latest/Reference/Decorators/

**Contents**:
- Decorators
- Decorators​
  - Usage​
    - decorate(name, value, [dependencies])​
    - decorateReply(name, value, [dependencies])​
    - decorateRequest(name, value, [dependencies])​
    - hasDecorator(name)​
    - hasRequestDecorator​

The decorators API customizes core Fastify objects, such as the server instance and any request and reply objects used during the HTTP request lifecycle. It can attach any type of property to core objects, e.g., functions, plain objects, or native types.

This API is synchronous. Defining a decoration asynchronously could result in the Fastify instance booting before the decoration completes. To register an asynchronous decoration, use the register API with fastify-plugin. See the Plugins documentation for more details.

Decorating core objects with this API allows the underlying JavaScript engine to optimize the handling of server, request, and reply objects. This is accomplished by defining the shape of all such object instances before they are instantiated and used. As an example, the following is not recommended because it will change the shape of objects during their lifecycle:

The above example mutates the request object after instantiation, causing the JavaScript engine to deoptimize access. Using the decoration API avoids this deoptimization:

Keep the initial shape of a decorated field close to its future dynamic value. Initialize a decorator as '' for strings and null for objects or functions. This works only with value types; reference types will throw an error during Fastify startup. See decorateRequest and JavaScript engine fundamentals: Shapes and Inline Caches for more information.

This method customizes the Fastify server instance.

For example, to attach a new method to the server instance:

Non-function values can also be attached to the server instance:

To access decorated properties, use the name provided to the decoration API:

The decorated Fastify server is bound to this in route handlers:

The dependencies parameter is an optional list of decorators that the decorator being defined relies upon. This list contains the names of other decorators. In the following example, the "utility" decorator depends on the "greet" and "hi" decorators:

Us

*[Content truncated - see full docs]*

**Examples**:

```js
// Bad example! Continue reading.// Attach a user property to the incoming request before the request// handler is invoked.fastify.addHook('preHandler', function (req, reply, done) {  req.user = 'Bob Dylan'  done()})// Use the attached user property in the request handler.fastify.get('/', function (req, reply) {  reply.send(`Hello, ${req.user}`)})
```

```js
// Decorate request with a 'user' propertyfastify.decorateRequest('user', '')// Update our propertyfastify.addHook('preHandler', (req, reply, done) => {  req.user = 'Bob Dylan'  done()})// And finally access itfastify.get('/', (req, reply) => {  reply.send(`Hello, ${req.user}!`)})
```

```js
fastify.decorate('utility', function () {  // Something very useful})
```

---

## Encapsulation

**URL**: https://fastify.dev/docs/latest/Reference/Encapsulation/

**Contents**:
- Encapsulation
- Encapsulation​
- Sharing Between Contexts​

A fundamental feature of Fastify is the "encapsulation context." It governs which decorators, registered hooks, and plugins are available to routes. A visual representation of the encapsulation context is shown in the following figure:

In the figure above, there are several entities:

Every child context and grandchild context has access to the root plugins. Within each child context, the grandchild contexts have access to the child plugins registered within the containing child context, but the containing child context does not have access to the child plugins registered within its grandchild context.

Given that everything in Fastify is a plugin except for the root context, every "context" and "plugin" in this example is a plugin that can consist of decorators, hooks, plugins, and routes. To put this example into concrete terms, consider a basic scenario of a REST API server with three routes: the first route (/one) requires authentication, the second route (/two) does not, and the third route (/three) has access to the same context as the second route. Using @fastify/bearer-auth to provide authentication, the code for this example is as follows:

The server example above demonstrates the encapsulation concepts from the original diagram:

To see this, start the server and issue requests:

Each context in the prior example inherits only from its parent contexts. Parent contexts cannot access entities within their descendant contexts. If needed, encapsulation can be broken using fastify-plugin, making anything registered in a descendant context available to the parent context.

To allow publicContext access to the bar decorator in grandchildContext, rewrite the code as follows:

Restarting the server and re-issuing the requests for /two and /three:

**Examples**:

```js
'use strict'const fastify = require('fastify')()fastify.decorateRequest('answer', 42)fastify.register(async function authenticatedContext (childServer) {  childServer.register(require('@fastify/bearer-auth'), { keys: ['abc123'] })  childServer.route({    path: '/one',    method: 'GET',    handler (request, response) {      response.send({        answer: request.answer,        // request.foo will be undefined as it is only defined in publicContext        foo: request.foo,        // request.bar wi
...
```

```sh
# curl -H 'authorization: Bearer abc123' http://127.0.0.1:8000/one{"answer":42}# curl http://127.0.0.1:8000/two{"answer":42,"foo":"foo"}# curl http://127.0.0.1:8000/three{"answer":42,"foo":"foo","bar":"bar"}
```

```js
'use strict'const fastify = require('fastify')()const fastifyPlugin = require('fastify-plugin')fastify.decorateRequest('answer', 42)// `authenticatedContext` omitted for clarityfastify.register(async function publicContext (childServer) {  childServer.decorateRequest('foo', 'foo')  childServer.route({    path: '/two',    method: 'GET',    handler (request, response) {      response.send({        answer: request.answer,        foo: request.foo,        bar: request.bar      })    }  })  childServe
...
```

---

## Errors

**URL**: https://fastify.dev/docs/latest/Reference/Errors/

**Contents**:
- Errors
- Errors​
  - Error Handling In Node.js​
    - Uncaught Errors​
    - Catching Errors In Promises​
  - Errors In Fastify​
    - Errors In Input Data​
    - Catching Uncaught Errors In Fastify​

In Node.js, uncaught errors can cause memory leaks, file descriptor leaks, and other major production issues. Domains were a failed attempt to fix this.

Given that it is not possible to process all uncaught errors sensibly, the best way to deal with them is to crash.

When using promises, attach a .catch() handler synchronously.

Fastify follows an all-or-nothing approach and aims to be lean and optimal. The developer is responsible for ensuring errors are handled properly.

Most errors result from unexpected input data, so it is recommended to validate input data against a JSON schema.

Fastify tries to catch as many uncaught errors as possible without hindering performance. This includes:

In both cases, the error will be caught safely and routed to Fastify's default error handler, resulting in a generic 500 Internal Server Error response.

To customize this behavior, use setErrorHandler.

From the Hooks documentation:

If you get an error during the execution of your hook, just pass it to done() and Fastify will automatically close the request and send the appropriate error code to the user.

When a custom error handler is defined through setErrorHandler, it will receive the error passed to the done() callback or through other supported automatic error handling mechanisms. If setErrorHandler is used multiple times, the error will be routed to the most precedent handler within the error encapsulation context. Error handlers are fully encapsulated, so a setErrorHandler call within a plugin will limit the error handler to that plugin's context.

The root error handler is Fastify's generic error handler. This error handler will use the headers and status code in the Error object, if they exist. The headers and status code will not be automatically set if a custom error handler is provided.

The following should be considered when using a custom error handler:

reply.send(data) behaves as in regular route handlers

Throwing a new error in a custom error handler will 

*[Content truncated - see full docs]*

**Examples**:

```js
const Fastify = require('fastify')// Instantiate the frameworkconst fastify = Fastify({  logger: true})// Register parent error handlerfastify.setErrorHandler((error, request, reply) => {  reply.status(500).send({ ok: false })})fastify.register((app, options, next) => {  // Register child error handler  fastify.setErrorHandler((error, request, reply) => {    throw error  })  fastify.get('/bad', async () => {    // Throws a non-Error type, 'bar'    throw 'foo'  })  fastify.get('/good', async () =
...
```

```js
// ESMimport { errorCodes } from 'fastify'// CommonJSconst errorCodes = require('fastify').errorCodes
```

```js
const Fastify = require('fastify')// Instantiate the frameworkconst fastify = Fastify({  logger: true})// Declare a routefastify.get('/', function (request, reply) {  reply.code('bad status code').send({ hello: 'world' })})fastify.setErrorHandler(function (error, request, reply) {  if (error instanceof Fastify.errorCodes.FST_ERR_BAD_STATUS_CODE) {    // Log error    this.log.error(error)    // Send error response    reply.status(500).send({ ok: false })  } else {    // Fastify will use parent er
...
```

---

## HTTP2

**URL**: https://fastify.dev/docs/latest/Reference/HTTP2/

**Contents**:
- HTTP2
- HTTP2​
  - Secure (HTTPS)​
  - Plain or insecure​

Fastify supports HTTP2 over HTTPS (h2) or plaintext (h2c).

Currently, none of the HTTP2-specific APIs are available through Fastify, but Node's req and res can be accessed through the Request and Reply interfaces. PRs are welcome.

HTTP2 is supported in all modern browsers only over a secure connection:

ALPN negotiation allows support for both HTTPS and HTTP/2 over the same socket. Node core req and res objects can be either HTTP/1 or HTTP/2. Fastify supports this out of the box:

Test the new server with:

For microservices, HTTP2 can connect in plain text, but this is not supported by browsers.

Test the new server with:

**Examples**:

```js
'use strict'const fs = require('node:fs')const path = require('node:path')const fastify = require('fastify')({  http2: true,  https: {    key: fs.readFileSync(path.join(__dirname, '..', 'https', 'fastify.key')),    cert: fs.readFileSync(path.join(__dirname, '..', 'https', 'fastify.cert'))  }})fastify.get('/', function (request, reply) {  reply.code(200).send({ hello: 'world' })})fastify.listen({ port: 3000 })
```

```js
'use strict'const fs = require('node:fs')const path = require('node:path')const fastify = require('fastify')({  http2: true,  https: {    allowHTTP1: true, // fallback support for HTTP1    key: fs.readFileSync(path.join(__dirname, '..', 'https', 'fastify.key')),    cert: fs.readFileSync(path.join(__dirname, '..', 'https', 'fastify.cert'))  }})// this route can be accessed through both protocolsfastify.get('/', function (request, reply) {  reply.code(200).send({ hello: 'world' })})fastify.listen(
...
```

```text
$ npx h2url https://localhost:3000
```

---

## Hooks

**URL**: https://fastify.dev/docs/latest/Reference/Hooks/

**Contents**:
- Hooks
- Hooks​
- Request/Reply Hooks​
  - onRequest​
  - preParsing​
  - preValidation​
  - preHandler​
  - preSerialization​

Hooks are registered with the fastify.addHook method and allow you to listen to specific events in the application or request/response lifecycle. You have to register a hook before the event is triggered, otherwise, the event is lost.

By using hooks you can interact directly with the lifecycle of Fastify. There are Request/Reply hooks and application hooks:

ℹ️ Note: The done callback is not available when using async/await or returning a Promise. If you do invoke a done callback in this situation unexpected behavior may occur, e.g. duplicate invocation of handlers.

Request and Reply are the core Fastify objects.

done is the function to continue with the lifecycle.

It is easy to understand where each hook is executed by looking at the lifecycle page.

Hooks are affected by Fastify's encapsulation, and can thus be applied to selected routes. See the Scopes section for more information.

There are eight different hooks that you can use in Request/Reply (in order of execution):

ℹ️ Note: In the onRequest hook, request.body will always be undefined, because the body parsing happens before the preValidation hook.

If you are using the preParsing hook, you can transform the request payload stream before it is parsed. It receives the request and reply objects as other hooks, and a stream with the current request payload.

If it returns a value (via return or via the callback function), it must return a stream.

For instance, you can decompress the request body:

ℹ️ Note: In the preParsing hook, request.body will always be undefined, because the body parsing happens before the preValidation hook.

ℹ️ Note: You should also add a receivedEncodedLength property to the returned stream. This property is used to correctly match the request payload with the Content-Length header value. Ideally, this property should be updated on each received chunk.

ℹ️ Note: The size of the returned stream is checked to not exceed the limit set in bodyLimit option.

If you are using the preVa

*[Content truncated - see full docs]*

**Examples**:

```js
fastify.addHook('onRequest', (request, reply, done) => {  // Some code  done()})
```

```js
fastify.addHook('onRequest', async (request, reply) => {  // Some code  await asyncMethod()})
```

```js
fastify.addHook('preParsing', (request, reply, payload, done) => {  // Some code  done(null, newPayload)})
```

---

## Index

**URL**: https://fastify.dev/docs/latest/Reference/

**Contents**:
- Index
- Core Documents​
- Reference Documentation Table Of Contents​

For the full table of contents (TOC), see below. The following list is a subset of the full TOC that detail core Fastify APIs and concepts in order of most likely importance to the reader:

This table of contents is in alphabetical order.

---

## Introduction

**URL**: https://fastify.dev/docs/latest/

**Contents**:
- Introduction
- Where To Start​
- Additional Documentation​

The documentation for Fastify is split into two categories:

The reference documentation utilizes a very formal style in an effort to document Fastify's API and implementation details thoroughly for the developer who needs such. The guides category utilizes an informal educational style as a means to introduce newcomers to core and advanced Fastify concepts.

Complete newcomers to Fastify should first read our Getting Started guide.

Developers experienced with Fastify should consult the reference documentation directly to find the topic they are seeking more information about.

---

## LTS

**URL**: https://fastify.dev/docs/latest/Reference/LTS/

**Contents**:
- LTS
- Long Term Support​
- Security Releases and Semver​
  - Security Support Beyond LTS​
  - Schedule​
  - CI tested operating systems​

Fastify's Long Term Support (LTS) is provided according to the schedule laid out in this document:

A "month" is defined as 30 consecutive days.

As a consequence of providing long-term support for major releases, there are occasions where we need to release breaking changes as a minor version release. Such changes will always be noted in the release notes.

To avoid automatically receiving breaking security updates it is possible to use the tilde (~) range qualifier. For example, to get patches for the 3.15 release, and avoid automatically updating to the 3.16 release, specify the dependency as "fastify": "~3.15.x". This will leave your application vulnerable, so please use it with caution.

Fastify's partner, HeroDevs, provides commercial security support through the OpenJS Ecosystem Sustainability Program for versions of Fastify that are EOL. For more information, see their Never Ending Support service.

Fastify uses GitHub Actions for CI testing, please refer to GitHub's documentation regarding workflow runners for further details on what the latest virtual environment is in relation to the YAML workflow labels below:

Using yarn might require passing the --ignore-engines flag.

---

## LTS

**URL**: https://fastify.dev/docs/latest/Reference/LTS

**Contents**:
- LTS
- Long Term Support​
- Security Releases and Semver​
  - Security Support Beyond LTS​
  - Schedule​
  - CI tested operating systems​

Fastify's Long Term Support (LTS) is provided according to the schedule laid out in this document:

A "month" is defined as 30 consecutive days.

As a consequence of providing long-term support for major releases, there are occasions where we need to release breaking changes as a minor version release. Such changes will always be noted in the release notes.

To avoid automatically receiving breaking security updates it is possible to use the tilde (~) range qualifier. For example, to get patches for the 3.15 release, and avoid automatically updating to the 3.16 release, specify the dependency as "fastify": "~3.15.x". This will leave your application vulnerable, so please use it with caution.

Fastify's partner, HeroDevs, provides commercial security support through the OpenJS Ecosystem Sustainability Program for versions of Fastify that are EOL. For more information, see their Never Ending Support service.

Fastify uses GitHub Actions for CI testing, please refer to GitHub's documentation regarding workflow runners for further details on what the latest virtual environment is in relation to the YAML workflow labels below:

Using yarn might require passing the --ignore-engines flag.

---

## Lifecycle

**URL**: https://fastify.dev/docs/latest/Reference/Lifecycle/

**Contents**:
- Lifecycle
- Lifecycle​
- Reply Lifecycle​

This schema shows the internal lifecycle of Fastify.

The right branch of each section shows the next phase of the lifecycle. The left branch shows the corresponding error code generated if the parent throws an error. All errors are automatically handled by Fastify.

Before or during the User Handler, reply.hijack() can be called to:

If reply.raw is used to send a response, onResponse hooks will still be executed.

When the user handles the request, the result may be:

If the reply was hijacked, all subsequent steps are skipped. Otherwise, when submitted, the data flow is as follows:

reply sent means the JSON payload will be serialized by one of the following:

**Examples**:

```text
Incoming Request  │  └─▶ Routing        │        └─▶ Instance Logger             │   4**/5** ◀─┴─▶ onRequest Hook                  │        4**/5** ◀─┴─▶ preParsing Hook                        │              4**/5** ◀─┴─▶ Parsing                             │                   4**/5** ◀─┴─▶ preValidation Hook                                  │                            400 ◀─┴─▶ Validation                                        │                              4**/5** ◀─┴─▶ preHandler Hook       
...
```

```text
★ schema validation Error                                    │                                    └─▶ schemaErrorFormatter                                               │                          reply sent ◀── JSON ─┴─ Error instance                                                      │                                                      │         ★ throw an Error                     ★ send or return                 │                 │                            │                         │   
...
```

---

## Logging

**URL**: https://fastify.dev/docs/latest/Reference/Logging/

**Contents**:
- Logging
- Logging​
  - Enable Logging​
    - Basic logging setup​
    - Environment-Specific Configuration​
  - Usage​
    - Passing Logger Options​
  - Advanced Logger Configuration​

Logging is disabled by default. Enable it by passing { logger: true } or { logger: { level: 'info' } } when creating a Fastify instance. Note that if the logger is disabled, it cannot be enabled at runtime. abstract-logging is used for this purpose.

As Fastify is focused on performance, it uses pino as its logger, with the default log level set to 'info' when enabled.

Enabling the production JSON logger:

Enabling the logger with appropriate configuration for local development, production, and test environments requires more configuration:

⚠️ pino-pretty needs to be installed as a dev dependency. It is not included by default for performance reasons.

The logger can be used in route handlers as follows:

Trigger new logs outside route handlers using the Pino instance from the Fastify instance:

To pass options to the logger, provide them to Fastify. See the Pino documentation for available options. To specify a file destination, use:

To pass a custom stream to the Pino instance, add a stream field to the logger object:

By default, Fastify adds an ID to every request for easier tracking. If the requestIdHeader option is set and the corresponding header is present, its value is used; otherwise, a new incremental ID is generated. See Fastify Factory requestIdHeader and Fastify Factory genReqId for customization options.

The default logger uses standard serializers for objects with req, res, and err properties. The req object is the Fastify Request object, and the res object is the Fastify Reply object. This behavior can be customized with custom serializers.

For example, the response payload and headers could be logged using the approach below (not recommended):

ℹ️ Note: In some cases, the Reply object passed to the res serializer cannot be fully constructed. When writing a custom res serializer, check for the existence of any properties on reply aside from statusCode, which is always present. For example, verify the existence of getHeaders before calling it:



*[Content truncated - see full docs]*

**Examples**:

```js
const fastify = require('fastify')({  logger: true})
```

```js
const envToLogger = {  development: {    transport: {      target: 'pino-pretty',      options: {        translateTime: 'HH:MM:ss Z',        ignore: 'pid,hostname',      },    },  },  production: true,  test: false,}const fastify = require('fastify')({  logger: envToLogger[environment] ?? true // defaults to true if no entry matches in the map})
```

```js
fastify.get('/', options, function (request, reply) {  request.log.info('Some info about the current request')  reply.send({ hello: 'world' })})
```

---

## Reply

**URL**: https://fastify.dev/docs/latest/Reference/Reply/

**Contents**:
- Reply
- Reply​
  - Introduction​
  - .code(statusCode)​
  - .elapsedTime​
  - .statusCode​
  - .server​
  - .header(key, value)​

The second parameter of the handler function is Reply. Reply is a core Fastify object that exposes the following functions and properties:

If not set via reply.code, the resulting statusCode will be 200.

Invokes the custom response time getter to calculate the amount of time passed since the request was received by Fastify.

This property reads and sets the HTTP status code. It is an alias for reply.code() when used as a setter.

The Fastify server instance, scoped to the current encapsulation context.

Sets a response header. If the value is omitted or undefined, it is coerced to ''.

ℹ️ Note: The header's value must be properly encoded using encodeURI or similar modules such as encodeurl. Invalid characters will result in a 500 TypeError response.

For more information, see http.ServerResponse#setHeader.

The browser will only consider the latest reference of a key for the set-cookie header. This is done to avoid parsing the set-cookie header when added to a reply and speeds up the serialization of the reply.

To reset the set-cookie header, you need to make an explicit call to reply.removeHeader('set-cookie'), read more about .removeHeader(key) here.

Sets all the keys of the object as response headers. .header will be called under the hood.

Retrieves the value of a previously set header.

Gets a shallow copy of all current response headers, including those set via the raw http.ServerResponse. Note that headers set via Fastify take precedence over those set via http.ServerResponse.

Remove the value of a previously set header.

Returns a boolean indicating if the specified header has been set.

Sends early hints to the client. Early hints allow the client to start processing resources before the final response is sent. This can improve performance by allowing the client to preload or preconnect to resources while the server is still generating the response.

The hints parameter is an object containing the early hint key-value pairs.

The optional callback para

*[Content truncated - see full docs]*

**Examples**:

```js
fastify.get('/', options, function (request, reply) {  // Your code  reply    .code(200)    .header('Content-Type', 'application/json; charset=utf-8')    .send({ hello: 'world' })})
```

```js
const milliseconds = reply.elapsedTime
```

```js
if (reply.statusCode >= 299) {  reply.statusCode = 500}
```

---

## Request

**URL**: https://fastify.dev/docs/latest/Reference/Request/

**Contents**:
- Request
- Request​
  - Headers​
  - .getValidationFunction(schema | httpPart)​
  - .compileValidationSchema(schema, [httpPart])​
  - .validateInput(data, [schema | httpPart], [httpPart])​

The first parameter of the handler function is Request.

Request is a core Fastify object containing the following fields:

The request.headers is a getter that returns an object with the headers of the incoming request. Set custom headers as follows:

This operation adds new values to the request headers, accessible via request.headers.bar. Standard request headers remain accessible via request.raw.headers.

For performance reasons, Symbol('fastify.RequestAcceptVersion') may be added to headers on not found routes.

ℹ️ Note: Schema validation may mutate the request.headers and request.raw.headers objects, causing the headers to become empty.

By calling this function with a provided schema or httpPart, it returns a validation function to validate diverse inputs. It returns undefined if no serialization function is found using the provided inputs.

This function has an errors property. Errors encountered during the last validation are assigned to errors.

See .compileValidationSchema(schema, [httpStatus]) for more information on compiling validation schemas.

This function compiles a validation schema and returns a function to validate data. The returned function (a.k.a. validation function) is compiled using the provided SchemaController#ValidationCompiler. A WeakMap is used to cache this, reducing compilation calls.

The optional parameter httpPart, if provided, is forwarded to the ValidationCompiler, allowing it to compile the validation function if a custom ValidationCompiler is provided for the route.

This function has an errors property. Errors encountered during the last validation are assigned to errors.

Be careful when using this function, as it caches compiled validation functions based on the provided schema. If schemas are mutated or changed, the validation functions will not detect the alterations and will reuse the previously compiled validation function, as the cache is based on the schema's reference.

If schema properties need to be changed, creat

*[Content truncated - see full docs]*

**Examples**:

```js
request.headers = {  'foo': 'bar',  'baz': 'qux'}
```

```js
fastify.post('/:params', options, function (request, reply) {  console.log(request.body)  console.log(request.query)  console.log(request.params)  console.log(request.headers)  console.log(request.raw)  console.log(request.server)  console.log(request.id)  console.log(request.ip)  console.log(request.ips)  console.log(request.host)  console.log(request.hostname)  console.log(request.port)  console.log(request.protocol)  console.log(request.url)  console.log(request.routeOptions.method)  console.
...
```

```js
const validate = request                  .getValidationFunction({                    type: 'object',                    properties: {                      foo: {                        type: 'string'                      }                    }                  })console.log(validate({ foo: 'bar' })) // trueconsole.log(validate.errors) // null// orconst validate = request                  .getValidationFunction('body')console.log(validate({ foo: 0.5 })) // falseconsole.log(validate.errors) // va
...
```

---

## Routes

**URL**: https://fastify.dev/docs/latest/Reference/Routes/

**Contents**:
- Routes
- Routes​
  - Full declaration​
  - Routes options​
  - Shorthand declaration​
  - Url building​
  - Async Await​
  - Promise resolution​

The route methods configure the endpoints of the application. Routes can be declared using the shorthand method or the full declaration.

method: currently it supports GET, HEAD, TRACE, DELETE, OPTIONS, PATCH, PUT and POST. To accept more methods, the addHttpMethod must be used. It could also be an array of methods.

url: the path of the URL to match this route (alias: path).

schema: an object containing the schemas for the request and response. They need to be in JSON Schema format, check here for more info.

exposeHeadRoute: creates a sibling HEAD route for any GET routes. Defaults to the value of exposeHeadRoutes instance option. If you want a custom HEAD handler without disabling this option, make sure to define it before the GET route.

attachValidation: attach validationError to request, if there is a schema validation error, instead of sending the error to the error handler. The default error format is the Ajv one.

onRequest(request, reply, done): a function called as soon as a request is received, it could also be an array of functions.

preParsing(request, reply, payload, done): a function called before parsing the request, it could also be an array of functions.

preValidation(request, reply, done): a function called after the shared preValidation hooks, useful if you need to perform authentication at route level for example, it could also be an array of functions.

preHandler(request, reply, done): a function called just before the request handler, it could also be an array of functions.

preSerialization(request, reply, payload, done): a function called just before the serialization, it could also be an array of functions.

onSend(request, reply, payload, done): a function called right before a response is sent, it could also be an array of functions.

onResponse(request, reply, done): a function called when a response has been sent, so you will not be able to send more data to the client. It could also be an array of functions.

onTimeout(request, rep

*[Content truncated - see full docs]*

**Examples**:

```js
fastify.route(options)
```

```js
fastify.route({  method: 'GET',  url: '/',  schema: {    querystring: {      type: 'object',      properties: {        name: { type: 'string' },        excitement: { type: 'integer' }      }    },    response: {      200: {        type: 'object',        properties: {          hello: { type: 'string' }        }      }    }  },  handler: function (request, reply) {    reply.send({ hello: 'world' })  }})
```

```js
const opts = {  schema: {    response: {      200: {        type: 'object',        properties: {          hello: { type: 'string' }        }      }    }  }}fastify.get('/', opts, (request, reply) => {  reply.send({ hello: 'world' })})
```

---

## Server

**URL**: https://fastify.dev/docs/latest/Reference/Server/

**Contents**:
- Server
- Factory​
  - http​
  - http2​
  - https​
  - connectionTimeout​
  - keepAliveTimeout​
  - forceCloseConnections​

The Fastify module exports a factory function that is used to create new Fastify server instances. This factory function accepts an options object which is used to customize the resulting instance. This document describes the properties available in that options object.

An object used to configure the server's listening socket. The options are the same as the Node.js core createServer method.

This option is ignored if options http2 or https are set.

If true Node.js core's HTTP/2 module is used for binding the socket.

An object used to configure the server's listening socket for TLS. The options are the same as the Node.js core createServer method. When this property is null, the socket will not be configured for TLS.

This option also applies when the http2 option is set.

Defines the server timeout in milliseconds. See documentation for server.timeout property to understand the effect of this option.

When serverFactory option is specified this option is ignored.

Defines the server keep-alive timeout in milliseconds. See documentation for server.keepAliveTimeout property to understand the effect of this option. This option only applies when HTTP/1 is in use.

When serverFactory option is specified this option is ignored.

When set to true, upon close the server will iterate the current persistent connections and destroy their sockets.

When used with HTTP/2 server, it will also close all active HTTP/2 sessions.

ℹ️ Note: Since Node.js v24 active sessions are closed by default

⚠ Warning: Connections are not inspected to determine if requests have been completed.

Fastify will prefer the HTTP server's closeAllConnections method if supported, otherwise, it will use internal connection tracking.

When set to "idle", upon close the server will iterate the current persistent connections which are not sending a request or waiting for a response and destroy their sockets. The value is only supported if the HTTP server supports the closeIdleConnections method, otherwi

*[Content truncated - see full docs]*

**Examples**:

```js
fastify.get('/foo', function (req, res) {  req.log.info({req}) // log the serialized request object  res.send('foo')})
```

```js
const pino = require('pino')();const customLogger = {  info: function (o, ...n) {},  warn: function (o, ...n) {},  error: function (o, ...n) {},  fatal: function (o, ...n) {},  trace: function (o, ...n) {},  debug: function (o, ...n) {},  child: function() {    const child = Object.create(this);    child.pino = pino.child(...arguments);    return child;  },};const fastify = require('fastify')({logger: customLogger});
```

```js
// Examples of hooks to replicate the disabled functionality.fastify.addHook('onRequest', (req, reply, done) => {  req.log.info({ url: req.raw.url, id: req.id }, 'received request')  done()})fastify.addHook('onResponse', (req, reply, done) => {  req.log.info({ url: req.raw.originalUrl, statusCode: reply.raw.statusCode }, 'request completed')  done()})
```

---

## Technical Principles

**URL**: https://fastify.dev/docs/latest/Reference/Principles/

**Contents**:
- Technical Principles
- "Zero" Overhead in Production​
- "Good" Developer Experience​
- Works great for small and big projects alike​
- Easy to migrate to microservices (or even serverless) and back​
- Security and Data Validation​
- If something could be a plugin, it likely should​
- Easily testable​

Every decision in the Fastify framework and its official plugins is guided by the following technical principles:

Fastify aims to implement features with minimal overhead. This is achieved by using fast algorithms, data structures, and JavaScript-specific features.

Since JavaScript does not offer zero-overhead data structures, this principle can conflict with providing a great developer experience and additional features, as these usually incur some overhead.

Fastify aims to provide the best developer experience at its performance point. It offers a great out-of-the-box experience that is flexible enough to adapt to various situations.

For example, binary addons are forbidden because most JavaScript developers do not have access to a compiler.

Most applications start small and become more complex over time. Fastify aims to grow with this complexity, providing advanced features to structure codebases.

Route deployment should not matter. The framework should "just work".

A web framework is the first point of contact with untrusted data and must act as the first line of defense for the system.

Recognizing the infinite use cases for an HTTP framework, catering to all in a single module would make the codebase unmaintainable. Therefore, hooks and options are provided to customize the framework as needed.

Testing Fastify applications should be a first-class concern.

Monkeypatching Node.js APIs or installing globals that alter the runtime makes building modular applications harder and limits Fastify's use cases. Other frameworks do this; Fastify does not.

A clear Long Term Support strategy is provided to inform developers when to upgrade.

In doubt, we chose the strict behavior as defined by the relevant Specifications.

---

## TypeScript

**URL**: https://fastify.dev/docs/latest/Reference/TypeScript/

**Contents**:
- TypeScript
- TypeScript​
- Learn By Example​
  - Getting Started​
  - Using Generics​
  - JSON Schema​
    - Fastify Type Providers​
    - TypeBox​

The Fastify framework is written in vanilla JavaScript, and as such type definitions are not as easy to maintain; however, since version 2 and beyond, maintainers and contributors have put in a great effort to improve the types.

The type system was changed in Fastify version 3. The new type system introduces generic constraining and defaulting, plus a new way to define schema types such as a request body, querystring, and more! As the team works on improving framework and type definition synergy, sometimes parts of the API will not be typed or may be typed incorrectly. We encourage you to contribute to help us fill in the gaps. Just make sure to read our CONTRIBUTING.md file before getting started to make sure things go smoothly!

The documentation in this section covers Fastify version 3.x typings

Plugins may or may not include typings. See Plugins for more information. We encourage users to send pull requests to improve typings support.

🚨 Don't forget to install @types/node

The best way to learn the Fastify type system is by example! The following four examples should cover the most common Fastify development cases. After the examples there is further, more detailed documentation for the type system.

This example will get you up and running with Fastify and TypeScript. It results in a blank http Fastify server.

or use one of the recommended ones.

Note: Set target property in tsconfig.json to es2017 or greater to avoid FastifyDeprecation warning.

🎉 You now have a working Typescript Fastify server! This example demonstrates the simplicity of the version 3.x type system. By default, the type system assumes you are using an http server. The later examples will demonstrate how to create more complex servers such as https and http2, how to specify route schemas, and more!

For more examples on initializing Fastify with TypeScript (such as enabling HTTP2) check out the detailed API section here

The type system heavily relies on generic properties to provide the 

*[Content truncated - see full docs]*

**Examples**:

```bash
npm init -ynpm i fastifynpm i -D typescript @types/node
```

```json
{  "scripts": {    "build": "tsc -p tsconfig.json",    "start": "node index.js"  }}
```

```bash
npx tsc --init
```

---

## Type-Providers

**URL**: https://fastify.dev/docs/latest/Reference/Type-Providers/

**Contents**:
- Type-Providers
- Type Providers​
  - Providers​
  - Json Schema to Ts​
  - TypeBox​
  - Zod​
  - Scoped Type-Provider​
  - Type Definition of FastifyInstance + TypeProvider​

Type Providers are a TypeScript feature that enables Fastify to infer type information from inline JSON Schema. They are an alternative to specifying generic arguments on routes and can reduce the need to keep associated types for each schema in a project.

Official Type Provider packages follow the @fastify/type-provider-{provider-name} naming convention. Several community providers are also available.

The following inference packages are supported:

See also the Type Provider wrapper packages for each of the packages respectively:

The following sets up a json-schema-to-ts Type Provider:

The following sets up a TypeBox Type Provider:

See the TypeBox documentation for setting up AJV to work with TypeBox.

See official documentation for Zod Type Provider instructions.

The provider types don't propagate globally. In encapsulated usage, one can remap the context to use one or more providers (for example, typebox and json-schema-to-ts can be used in the same application).

It is important to note that since the types do not propagate globally, it is currently not possible to avoid multiple registrations on routes when dealing with several scopes, as shown below:

When working with modules, use FastifyInstance with Type Provider generics. See the example below:

**Examples**:

```bash
$ npm i @fastify/type-provider-json-schema-to-ts
```

```typescript
import fastify from 'fastify'import { JsonSchemaToTsProvider } from '@fastify/type-provider-json-schema-to-ts'const server = fastify().withTypeProvider<JsonSchemaToTsProvider>()server.get('/route', {  schema: {    querystring: {      type: 'object',      properties: {        foo: { type: 'number' },        bar: { type: 'string' },      },      required: ['foo', 'bar']    }  }}, (request, reply) => {  // type Query = { foo: number, bar: string }  const { foo, bar } = request.query // type safe!})
```

```bash
$ npm i @fastify/type-provider-typebox
```

---

## Validation-and-Serialization

**URL**: https://fastify.dev/docs/latest/Reference/Validation-and-Serialization/

**Contents**:
- Validation-and-Serialization
- Validation and Serialization​
  - Core concepts​
    - Adding a shared schema​
    - Retrieving the shared schemas​
  - Validation​
    - Ajv Plugins​
    - Validator Compiler​

Fastify uses a schema-based approach. We recommend using JSON Schema to validate routes and serialize outputs. Fastify compiles the schema into a highly performant function.

Validation is only attempted if the content type is application/json.

All examples use the JSON Schema Draft 7 specification.

⚠ Warning: Treat schema definitions as application code. Validation and serialization features use new Function(), which is unsafe with user-provided schemas. See Ajv and fast-json-stringify for details.

Whilst Fastify supports the $async Ajv feature, it should not be used for initial validation. Accessing databases during validation may lead to Denial of Service attacks. Use Fastify's hooks like preHandler for async tasks after validation.

When using custom validators with async preValidation hooks, validators must return {error} objects instead of throwing errors. Throwing errors from custom validators will cause unhandled promise rejections that crash the application when combined with async hooks. See the custom validator examples below for the correct pattern.

Validation and serialization are handled by two customizable dependencies:

These dependencies share only the JSON schemas added to Fastify's instance via .addSchema(schema).

The addSchema API allows adding multiple schemas to the Fastify instance for reuse throughout the application. This API is encapsulated.

Shared schemas can be reused with the JSON Schema $ref keyword. Here is an overview of how references work:

$ref as root reference:

If the validator and serializer are customized, .addSchema is not useful since Fastify no longer controls them. To access schemas added to the Fastify instance, use .getSchemas():

The getSchemas function is encapsulated and returns shared schemas available in the selected scope:

Route validation relies on Ajv v8, a high-performance JSON Schema validator. To validate input, add the required fields to the route schema.

Supported validations include:

Validations ca

*[Content truncated - see full docs]*

**Examples**:

```js
fastify.addSchema({  $id: 'http://example.com/',  type: 'object',  properties: {    hello: { type: 'string' }  }})fastify.post('/', {  handler () {},  schema: {    body: {      type: 'array',      items: { $ref: 'http://example.com#/properties/hello' }    }  }})
```

```js
fastify.addSchema({  $id: 'commonSchema',  type: 'object',  properties: {    hello: { type: 'string' }  }})fastify.post('/', {  handler () {},  schema: {    body: { $ref: 'commonSchema#' },    headers: { $ref: 'commonSchema#' }  }})
```

```js
fastify.addSchema({  $id: 'schemaId',  type: 'object',  properties: {    hello: { type: 'string' }  }})const mySchemas = fastify.getSchemas()const mySchema = fastify.getSchema('schemaId')
```

---

## Warnings

**URL**: https://fastify.dev/docs/latest/Reference/Warnings/

**Contents**:
- Warnings
- Warnings​
  - Warnings In Fastify​
  - Fastify Warning Codes​
  - Fastify Deprecation Codes​

Fastify uses Node.js's warning event API to notify users of deprecated features and coding mistakes. Fastify's warnings are recognizable by the FSTWRN and FSTDEP prefixes. When encountering such a warning, it is highly recommended to determine the cause using the --trace-warnings and --trace-deprecation flags. These produce stack traces pointing to where the issue occurs in the application's code. Issues opened about warnings without this information will be closed due to lack of details.

Warnings can also be disabled, though it is not recommended. If necessary, use one of the following methods:

For more information on disabling warnings, see Node's documentation.

Disabling warnings may cause issues when upgrading Fastify versions. Only experienced users should consider disabling warnings.

Deprecation codes are supported by the Node.js CLI options:

---
