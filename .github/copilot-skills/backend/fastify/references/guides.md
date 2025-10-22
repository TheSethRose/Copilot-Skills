# Fastify - Guides

**Pages**: 19

---

## Benchmarking

**URL**: https://fastify.dev/docs/latest/Guides/Benchmarking/

**Contents**:
- Benchmarking
- Benchmarking​
- Simple​
  - Run the test in the current branch​
  - Run the test against different Node.js versions ✨​
- Advanced​
  - Run the test in different branches​
  - Run the test in different branches against different Node.js versions ✨​

Benchmarking is important if you want to measure how a change can affect your application's performance. We provide a simple way to benchmark your application from the point of view of a user and contributor. The setup allows you to automate benchmarks in different branches and on different Node.js versions.

The modules we will use:

**Examples**:

```sh
npm run benchmark
```

```sh
npx -p node@10 -- npm run benchmark
```

```sh
branchcmp --rounds 2 --script "npm run benchmark"
```

---

## Contributing To Fastify

**URL**: https://fastify.dev/docs/latest/Guides/Contributing/

**Contents**:
- Contributing To Fastify
- Note​
- Table Of Contents​
- Types Of Contributions We're Looking For​
- Ground Rules & Expectations​
- How To Contribute​
- Setting Up Your Environment​
  - Using Visual Studio Code​

Thank you for taking an interest in contributing to Fastify. We are excited to receive your support and knowledge. This guide is our attempt to help you help us.

This is an informal guide. For full details, please review the formal CONTRIBUTING document our Developer Certificate of Origin.

In short, we welcome any type of contribution you are willing to provide. No contribution is too small. We gladly accept contributions such as:

Before we get started, here are a few things we expect from you (and that you should expect from others):

If you'd like to contribute, start by searching through the issues and pull requests to see whether someone else has raised a similar idea or question.

If you don't see your idea listed, and you think it fits into the goals of this guide, do one of the following:

Please adhere to the project's code and documentation style. Some popular tools that automatically "correct" code and documentation do not follow a style that conforms to this project's styles. Notably, this project uses StandardJS for code formatting.

What follows is how to use Visual Studio Code (VSCode) portable to create a Fastify specific environment. This guide is written as if you are setting up the environment on macOS, but the principles are the same across all platforms. See the previously linked VSCode portable guide for help with other platforms.

First, download VSCode and unpackage it to /Applications/VSCodeFastify/. Upon doing so, the following should output "found" when run in a terminal:

As mentioned in the VSCode portable guide, we need to unsandbox the application for the portable mode to work correctly. So issue the following in a terminal:

Next, create the required data directories for VSCode:

Before continuing, we need to add the code command to your terminal's PATH. To do so, we will manually add VSCode to the PATH. As outlined in that document, the instructions vary depending on your default shell, so you should follow the instructions in that

*[Content truncated - see full docs]*

**Examples**:

```sh
[ -d /Applications/VSCodeFastify/Visual\ Studio\ Code.app ] && echo "found"
```

```sh
xattr -dr com.apple.quarantine /Applications/VSCodeFastify/Visual\ Studio\ Code.app
```

```sh
mkdir -p /Applications/VSCodeFastify/code-portable-data/{user-data,extensions}
```

---

## Database

**URL**: https://fastify.dev/docs/latest/Guides/Database/

**Contents**:
- Database
- Database​
  - MySQL​
  - Postgres​
  - Redis​
  - Mongo​
  - LevelDB​
  - Writing plugin for a database library​

Fastify's ecosystem provides a handful of plugins for connecting to various database engines. This guide covers engines that have Fastify plugins maintained within the Fastify organization.

If a plugin for your database of choice does not exist you can still use the database as Fastify is database agnostic. By following the examples of the database plugins listed in this guide, a plugin can be written for the missing database engine.

If you would like to write your own Fastify plugin please take a look at the plugins guide

Install the plugin by running npm i @fastify/mysql.

Install the plugin by running npm i pg @fastify/postgres.

Install the plugin by running npm i @fastify/redis

By default @fastify/redis doesn't close the client connection when Fastify server shuts down. To opt-in to this behavior, register the client like so:

Install the plugin by running npm i @fastify/mongodb

Install the plugin by running npm i @fastify/leveldb

We could write a plugin for a database library too (e.g. Knex, Prisma, or TypeORM). We will use Knex in our example.

In this example, we will create a basic Fastify MySQL plugin from scratch (it is a stripped-down example, please use the official plugin in production).

Database schema migrations are an integral part of database management and development. Migrations provide a repeatable and testable way to modify a database's schema and prevent data loss.

As stated at the beginning of the guide, Fastify is database agnostic and any Node.js database migration tool can be used with it. We will give an example of using Postgrator which has support for Postgres, MySQL, SQL Server and SQLite. For MongoDB migrations, please check migrate-mongo.

Postgrator is Node.js SQL migration tool that uses a directory of SQL scripts to alter the database schema. Each file in a migrations folder needs to follow the pattern: [version].[action].[optional-description].sql.

version: must be an incrementing number (e.g. 001 or a timestamp).

actio

*[Content truncated - see full docs]*

**Examples**:

```javascript
const fastify = require('fastify')()fastify.register(require('@fastify/mysql'), {  connectionString: 'mysql://root@localhost/mysql'})fastify.get('/user/:id', function(req, reply) {  fastify.mysql.query(    'SELECT id, username, hash, salt FROM users WHERE id=?', [req.params.id],    function onResult (err, result) {      reply.send(err || result)    }  )})fastify.listen({ port: 3000 }, err => {  if (err) throw err  console.log(`server listening on ${fastify.server.address().port}`)})
```

```javascript
const fastify = require('fastify')()fastify.register(require('@fastify/postgres'), {  connectionString: 'postgres://postgres@localhost/postgres'})fastify.get('/user/:id', function (req, reply) {  fastify.pg.query(    'SELECT id, username, hash, salt FROM users WHERE id=$1', [req.params.id],    function onResult (err, result) {      reply.send(err || result)    }  )})fastify.listen({ port: 3000 }, err => {  if (err) throw err  console.log(`server listening on ${fastify.server.address().port}`)})
```

```javascript
'use strict'const fastify = require('fastify')()fastify.register(require('@fastify/redis'), { host: '127.0.0.1' })// orfastify.register(require('@fastify/redis'), { url: 'redis://127.0.0.1', /* other redis options */ })fastify.get('/foo', function (req, reply) {  const { redis } = fastify  redis.get(req.query.key, (err, val) => {    reply.send(err || val)  })})fastify.post('/foo', function (req, reply) {  const { redis } = fastify  redis.set(req.body.key, req.body.value, (err) => {    reply.send
...
```

---

## Delay Accepting Requests

**URL**: https://fastify.dev/docs/latest/Guides/Delay-Accepting-Requests/

**Contents**:
- Delay Accepting Requests
- Introduction​
- Solution​
  - Overview​
  - Hands-on​
      - index.js​
      - provider.js​
      - delay-incoming-requests.js​

Fastify provides several hooks useful for a variety of situations. One of them is the onReady hook, which is useful for executing tasks right before the server starts accepting new requests. There isn't, though, a direct mechanism to handle scenarios in which you'd like the server to start accepting specific requests and denying all others, at least up to some point.

Say, for instance, your server needs to authenticate with an OAuth provider to start serving requests. To do that it'd need to engage in the OAuth Authorization Code Flow, which would require it to listen to two requests from the authentication provider:

Until the authorization flow is done you wouldn't be able to serve customer requests. What to do then?

There are several solutions for achieving that kind of behavior. Here we'll introduce one of such techniques and, hopefully, you'll be able to get things rolling asap!

The proposed solution is one of many possible ways of dealing with this scenario and many similar to it. It relies solely on Fastify, so no fancy infrastructure tricks or third-party libraries will be necessary.

To simplify things we won't be dealing with a precise OAuth flow but, instead, simulate a scenario in which some key is needed to serve a request and that key can only be retrieved in runtime by authenticating with an external provider.

The main goal here is to deny requests that would otherwise fail as early as possible and with some meaningful context. That's both useful for the server (fewer resources allocated to a bound-to-fail task) and for the client (they get some meaningful information and don't need to wait long for it).

That will be achieved by wrapping into a custom plugin two main features:

For this sample solution we'll be using the following:

Say we have the following base server set up at first:

Our code is simply setting up a Fastify server with a few routes:

The provider.js file, simulating actions of an external provider, is as follows:

The most imp

*[Content truncated - see full docs]*

**Examples**:

```js
const Fastify = require('fastify')const provider = require('./provider')const server = Fastify({ logger: true })const USUAL_WAIT_TIME_MS = 5000server.get('/ping', function (request, reply) {  reply.send({ error: false, ready: request.server.magicKey !== null })})server.post('/webhook', function (request, reply) {  // It's good practice to validate webhook requests come from  // who you expect. This is skipped in this sample for the sake  // of simplicity  const { magicKey } = request.body  reque
...
```

```js
const { fetch } = require('undici')const { setTimeout } = require('node:timers/promises')const MAGIC_KEY = '12345'const delay = setTimeoutexports.thirdPartyMagicKeyGenerator = async (ms) => {  // Simulate processing delay  await delay(ms)  // Simulate webhook request to our server  const { status } = await fetch(    'http://localhost:1234/webhook',    {      body: JSON.stringify({ magicKey: MAGIC_KEY }),      method: 'POST',      headers: {        'content-type': 'application/json',      },    }
...
```

```js
const Fastify = require('fastify')const customerRoutes = require('./customer-routes')const { setup, delay } = require('./delay-incoming-requests')const server = new Fastify({ logger: true })server.register(setup)// Non-blocked URLserver.get('/ping', function (request, reply) {  reply.send({ error: false, ready: request.server.magicKey !== null })})// Webhook to handle the provider's response - also non-blockedserver.post('/webhook', function (request, reply) {  // It's good practice to validate 
...
```

---

## Detecting When Clients Abort

**URL**: https://fastify.dev/docs/latest/Guides/Detecting-When-Clients-Abort/

**Contents**:
- Detecting When Clients Abort
- Introduction​
- Solution​
  - Overview​
  - Hands-on​
  - Testing​
- Conclusion​

Fastify provides request events to trigger at certain points in a request's lifecycle. However, there isn't a built-in mechanism to detect unintentional client disconnection scenarios such as when the client's internet connection is interrupted. This guide covers methods to detect if and when a client intentionally aborts a request.

Keep in mind, Fastify's clientErrorHandler is not designed to detect when a client aborts a request. This works in the same way as the standard Node HTTP module, which triggers the clientError event when there is a bad request or exceedingly large header data. When a client aborts a request, there is no error on the socket and the clientErrorHandler will not be triggered.

The proposed solution is a possible way of detecting when a client intentionally aborts a request, such as when a browser is closed or the HTTP request is aborted from your client application. If there is an error in your application code that results in the server crashing, you may require additional logic to avoid a false abort detection.

The goal here is to detect when a client intentionally aborts a connection so your application logic can proceed accordingly. This can be useful for logging purposes or halting business logic.

Say we have the following base server set up:

Our code is setting up a Fastify server which includes the following functionality:

Whilst the aborted property has been deprecated, destroyed is not a suitable replacement as the Node.js documentation suggests. A request can be destroyed for various reasons, such as when the server closes the connection. The aborted property is still the most reliable way to detect when a client intentionally aborts a request.

You can also perform this logic outside of a hook, directly in a specific route.

At any point in your business logic, you can check if the request has been aborted and perform alternative actions.

A benefit to adding this in your application code is that you can log Fastify details s

*[Content truncated - see full docs]*

**Examples**:

```js
import Fastify from 'fastify';const sleep = async (time) => {  return await new Promise(resolve => setTimeout(resolve, time || 1000));}const app = Fastify({  logger: {    transport: {      target: 'pino-pretty',      options: {        translateTime: 'HH:MM:ss Z',        ignore: 'pid,hostname',      },    },  },})app.addHook('onRequest', async (request, reply) => {  request.raw.on('close', () => {    if (request.raw.aborted) {      app.log.info('request closed')    }  })})app.get('/', async (requ
...
```

```js
app.get('/', async (request, reply) => {  request.raw.on('close', () => {    if (request.raw.aborted) {      app.log.info('request closed')    }  })  await sleep(3000)  reply.code(200).send({ ok: true })})
```

```js
app.get('/', async (request, reply) => {  await sleep(3000)  if (request.raw.aborted) {    // do something here  }  await sleep(3000)  reply.code(200).send({ ok: true })})
```

---

## Ecosystem

**URL**: https://fastify.dev/docs/latest/Guides/Ecosystem/

**Contents**:
- Ecosystem
- Ecosystem​
    - Core​
    - Community​
    - Community Tools​

Plugins maintained by the Fastify team are listed under Core while plugins maintained by the community are listed in the Community section.

ℹ️ Note: Fastify community plugins are part of the broader community efforts, and we are thankful for these contributions. However, they are not maintained by the Fastify team. Use them at your own discretion. If you find malicious code, please open an issue or submit a PR to remove the plugin from the list.

---

## Fastify Style Guide

**URL**: https://fastify.dev/docs/latest/Guides/Style-Guide/

**Contents**:
- Fastify Style Guide
- Welcome​
- Who is this guide for?​
- Before you write​
  - Consider your Audience​
  - Get straight to the point​
  - Avoid adding video or image content​
  - Avoid plagiarism​

Welcome to Fastify Style Guide. This guide is here to provide you with a conventional writing style for users writing developer documentation on our Open Source framework. Each topic is precise and well explained to help you write documentation users can easily understand and implement.

This guide is for anyone who loves to build with Fastify or wants to contribute to our documentation. You do not need to be an expert in writing technical documentation. This guide is here to help you.

Visit the contribute page on our website or read the CONTRIBUTING.md file on GitHub to join our Open Source folks.

You need to know the following:

Before you start writing, think about your audience. In this case, your audience should already know HTTP, JavaScript, NPM, and Node.js. It is necessary to keep your readers in mind because they are the ones consuming your content. You want to give as much useful information as possible. Consider the vital things they need to know and how they can understand them. Use words and references that readers can relate to easily. Ask for feedback from the community, it can help you write better documentation that focuses on the user and what you want to achieve.

Give your readers a clear and precise action to take. Start with what is most important. This way, you can help them find what they need faster. Mostly, readers tend to read the first content on a page, and many will not scroll further.

Less like this: Colons are very important to register a parametric path. It lets the framework know there is a new parameter created. You can place the colon before the parameter name so the parametric path can be created.

More Like this: To register a parametric path, put a colon before the parameter name. Using a colon lets the framework know it is a parametric path and not a static path.

Do not add videos or screenshots to the documentation. It is easier to keep under version control. Videos and images will eventually end up becoming outdated as n

*[Content truncated - see full docs]*

**Examples**:

```text
To learn more about hooks, see [Fastify hooks](https://fastify.dev/docs/latest/Reference/Hooks/).
```

```md
<!-- More like this -->// Add clear & brief description[Fastify Plugins] (https://fastify.dev/docs/latest/Plugins/)<!--Less like this -->// incomplete description[Fastify] (https://fastify.dev/docs/latest/Plugins/)// Adding title in link brackets[](https://fastify.dev/docs/latest/Plugins/ "fastify plugin")// Empty title[](https://fastify.dev/docs/latest/Plugins/)// Adding links localhost URLs instead of using code strings (``)[http://localhost:3000/](http://localhost:3000/)
```

---

## Fluent-Schema

**URL**: https://fastify.dev/docs/latest/Guides/Fluent-Schema/

**Contents**:
- Fluent-Schema
- Fluent Schema​
  - Basic settings​
  - Reuse​

The Validation and Serialization documentation outlines all parameters accepted by Fastify to set up JSON Schema Validation to validate the input, and JSON Schema Serialization to optimize the output.

fluent-json-schema can be used to simplify this task while allowing the reuse of constants.

With fluent-json-schema, you can manipulate your schemas more easily and programmatically and then reuse them thanks to the addSchema() method. You can refer to the schema in two different manners that are detailed in the Validation and Serialization documentation.

Here are some usage examples:

$ref-way: refer to an external schema.

replace-way: refer to a shared schema to replace before the validation process.

NB You can mix up the $ref-way and the replace-way when using fastify.addSchema.

**Examples**:

```js
const S = require('fluent-json-schema')// You can have an object like this, or query a DB to get the valuesconst MY_KEYS = {  KEY1: 'ONE',  KEY2: 'TWO'}const bodyJsonSchema = S.object()  .prop('someKey', S.string())  .prop('someOtherKey', S.number())  .prop('requiredKey', S.array().maxItems(3).items(S.integer()).required())  .prop('nullableKey', S.mixed([S.TYPES.NUMBER, S.TYPES.NULL]))  .prop('multipleTypesKey', S.mixed([S.TYPES.BOOLEAN, S.TYPES.NUMBER]))  .prop('multipleRestrictedTypesKey', S.o
...
```

```js
const addressSchema = S.object()  .id('#address')  .prop('line1').required()  .prop('line2')  .prop('country').required()  .prop('city').required()  .prop('zipcode').required()const commonSchemas = S.object()  .id('https://fastify/demo')  .definition('addressSchema', addressSchema)  .definition('otherSchema', otherSchema) // You can add any schemas you needfastify.addSchema(commonSchemas)const bodyJsonSchema = S.object()  .prop('residence', S.ref('https://fastify/demo#address')).required()  .pro
...
```

```js
const sharedAddressSchema = {  $id: 'sharedAddress',  type: 'object',  required: ['line1', 'country', 'city', 'zipcode'],  properties: {    line1: { type: 'string' },    line2: { type: 'string' },    country: { type: 'string' },    city: { type: 'string' },    zipcode: { type: 'string' }  }}fastify.addSchema(sharedAddressSchema)const bodyJsonSchema = {  type: 'object',  properties: {    vacation: 'sharedAddress#'  }}const schema = { body: bodyJsonSchema }fastify.post('/the/url', { schema }, hand
...
```

---

## How to write a good plugin

**URL**: https://fastify.dev/docs/latest/Guides/Write-Plugin/

**Contents**:
- How to write a good plugin
- Code​
- Documentation​
- License​
- Examples​
- Test​
- Code Linter​
- Continuous Integration​

First, thank you for deciding to write a plugin for Fastify. Fastify is a minimal framework and plugins are its strength, so thank you.

The core principles of Fastify are performance, low overhead, and providing a good experience to our users. When writing a plugin, it is important to keep these principles in mind. Therefore, in this document, we will analyze what characterizes a quality plugin.

Need some inspiration? You can use the label "plugin suggestion" in our issue tracker!

Fastify uses different techniques to optimize its code, many of which are documented in our Guides. We highly recommend you read the hitchhiker's guide to plugins to discover all the APIs you can use to build your plugin and learn how to use them.

Do you have a question or need some advice? We are more than happy to help you! Just open an issue in our help repository.

Once you submit a plugin to our ecosystem list, we will review your code and help you improve it if necessary.

Documentation is extremely important. If your plugin is not well documented we will not accept it to the ecosystem list. Lack of quality documentation makes it more difficult for people to use your plugin, and will likely result in it going unused.

If you want to see some good examples of how to document a plugin take a look at:

You can license your plugin as you prefer, we do not enforce any kind of license.

We prefer the MIT license because we think it allows more people to use the code freely. For a list of alternative licenses see the OSI list or GitHub's choosealicense.com.

Always put an example file in your repository. Examples are very helpful for users and give a very fast way to test your plugin. Your users will be grateful.

A plugin must be thoroughly tested to verify that is working properly.

A plugin without tests will not be accepted to the ecosystem list. A lack of tests does not inspire trust nor guarantee that the code will continue to work among different versions of its dependencies.

We

*[Content truncated - see full docs]*

---

## Index

**URL**: https://fastify.dev/docs/latest/Guides/

**Contents**:
- Index
- Guides Table Of Contents​

This table of contents is in alphabetical order.

---

## Prototype-Poisoning

**URL**: https://fastify.dev/docs/latest/Guides/Prototype-Poisoning/

**Contents**:
- Prototype-Poisoning
- History behind prototype poisoning​
  - BOOM​
  - Prototype in a nutshell​
  - Oh joi!​
  - The right thing​
  - A detour​
  - A development​

The following is an article written by Eran Hammer. It is reproduced here for posterity with permission. It has been reformatted from the original HTML source to Markdown source, but otherwise remains the same. The original HTML can be retrieved from the above permission link.

Based on the article by Eran Hammer,the issue is created by a web security bug. It is also a perfect illustration of the efforts required to maintain open-source software and the limitations of existing communication channels.

But first, if we use a JavaScript framework to process incoming JSON data, take a moment to read up on Prototype Poisoning in general, and the specific technical details of this issue. This could be a critical issue so, we might need to verify your own code first. It focuses on specific framework however, any solution that uses JSON.parse() to process external data is potentially at risk.

The engineering team at Lob (long time generous supporters of my work!) reported a critical security vulnerability they identified in our data validation module — joi. They provided some technical details and a proposed solution.

The main purpose of a data validation library is to ensure the output fully complies with the rules defined. If it doesn't, validation fails. If it passes, we can blindly trust that the data you are working with is safe. In fact, most developers treat validated input as completely safe from a system integrity perspective which is crucial!

In our case, the Lob team provided an example where some data was able to escape by the validation logic and pass through undetected. This is the worst possible defect a validation library can have.

To understand this, we need to understand how JavaScript works a bit. Every object in JavaScript can have a prototype. It is a set of methods and properties it "inherits" from another object. I have put inherits in quotes because JavaScript isn't really an object-oriented language. It is a prototype- based object-oriented lan

*[Content truncated - see full docs]*

**Examples**:

```text
> const a = { b: 5 };> a.b;5> a.__proto__ = { c: 6 };> a.c;6> a;{ b: 5 }
```

```text
> const text = '{"b": 5, "__proto__": { "c": 6 }}';> const a = JSON.parse(text);> a;{b: 5, __proto__: { c: 6 }}
```

```text
> const x = Object.assign({}, a);> x;{ b: 5}> x.c;6;
```

---

## Recommendations

**URL**: https://fastify.dev/docs/latest/Guides/Recommendations/

**Contents**:
- Recommendations
- Recommendations​
- Use A Reverse Proxy​
  - HAProxy​
  - Nginx​
- Kubernetes​
- Capacity Planning For Production​
- Running Multiple Instances​

This document contains a set of recommendations when using Fastify.

Node.js is an early adopter of frameworks shipping with an easy-to-use web server within the standard library. Previously, with languages like PHP or Python, one would need either a web server with specific support for the language or the ability to set up some sort of CGI gateway that works with the language. With Node.js, one can write an application that directly handles HTTP requests. As a result, the temptation is to write applications that handle requests for multiple domains, listen on multiple ports (i.e. HTTP and HTTPS), and then expose these applications directly to the Internet to handle requests.

The Fastify team strongly considers this to be an anti-pattern and extremely bad practice:

See Why should I use a Reverse Proxy if Node.js is Production Ready? for a more thorough discussion of why one should opt to use a reverse proxy.

For a concrete example, consider the situation where:

There are many reverse proxy solutions available, and your environment may dictate the solution to use, e.g. AWS or GCP. Given the above, we could use HAProxy or Nginx to solve these requirements:

The readinessProbe uses (by default) the pod IP as the hostname. Fastify listens on 127.0.0.1 by default. The probe will not be able to reach the application in this case. To make it work, the application must listen on 0.0.0.0 or specify a custom hostname in the readinessProbe.httpGet spec, as per the following example:

In order to rightsize the production environment for your Fastify application, it is highly recommended that you perform your own measurements against different configurations of the environment, which may use real CPU cores, virtual CPU cores (vCPU), or even fractional vCPU cores. We will use the term vCPU throughout this recommendation to represent any CPU type.

Tools such as k6 or autocannon can be used for conducting the necessary performance tests.

That said, you may also consider the f

*[Content truncated - see full docs]*

**Examples**:

```conf
# The global section defines base HAProxy (engine) instance configuration.global  log /dev/log syslog  maxconn 4096  chroot /var/lib/haproxy  user haproxy  group haproxy  # Set some baseline TLS options.  tune.ssl.default-dh-param 2048  ssl-default-bind-options no-sslv3 no-tlsv10 no-tlsv11  ssl-default-bind-ciphers ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:RSA+AESGCM:RSA+AES:!aNULL:!MD5:!DSS  ssl-default-server-options no-sslv3 no-tlsv10 no-tlsv11  ssl-default-server-ciphers
...
```

```nginx
# This upstream block groups 3 servers into one named backend fastify_app# with 2 primary servers distributed via round-robin# and one backup which is used when the first 2 are not reachable# This also assumes your fastify servers are listening on port 80.# more info: https://nginx.org/en/docs/http/ngx_http_upstream_module.htmlupstream fastify_app {  server 10.10.11.1:80;  server 10.10.11.2:80;  server 10.10.11.3:80 backup;}# This server block asks NGINX to respond with a redirect when# an incom
...
```

```yaml
readinessProbe:    httpGet:        path: /health        port: 4000    initialDelaySeconds: 30    periodSeconds: 30    timeoutSeconds: 3    successThreshold: 1    failureThreshold: 5
```

---

## Serverless

**URL**: https://fastify.dev/docs/latest/Guides/Serverless/

**Contents**:
- Serverless
    - Should you use Fastify in a serverless platform?​
  - Contents​
- AWS​
  - Using @fastify/aws-lambda​
    - app.js​
    - lambda.js​
    - Example​

Run serverless applications and REST APIs using your existing Fastify application. You may need to make code changes to work on your serverless platform of choice. This document contains a small guide for the most popular serverless providers and how to use Fastify with them.

That is up to you! Keep in mind, functions as a service should always use small and focused functions, but you can also run an entire web application with them. It is important to remember that the bigger the application the slower the initial boot will be. The best way to run Fastify applications in serverless environments is to use platforms like Google Cloud Run, AWS Fargate, Azure Container Instances, and Vercel where the server can handle multiple requests at the same time and make full use of Fastify's features.

One of the best features of using Fastify in serverless applications is the ease of development. In your local environment, you will always run the Fastify application directly without the need for any additional tools, while the same code will be executed in your serverless platform of choice with an additional snippet of code.

To integrate with AWS, you have two choices of library:

So you can decide which option is best for you, but you can test both libraries.

The sample provided allows you to easily build serverless web applications/services and RESTful APIs using Fastify on top of AWS Lambda and Amazon API Gateway.

When executed in your lambda function we do not need to listen to a specific port, so we just export the wrapper function init in this case. The lambda.js file will use this export.

When you execute your Fastify application like always, i.e. node app.js (the detection for this could be require.main === module), you can normally listen to your port, so you can still run your Fastify function locally.

We just require @fastify/aws-lambda (make sure you install the dependency npm i @fastify/aws-lambda) and our app.js file and call the exported awsLambdaFastify 

*[Content truncated - see full docs]*

**Examples**:

```js
const fastify = require('fastify');function init() {  const app = fastify();  app.get('/', (request, reply) => reply.send({ hello: 'world' }));  return app;}if (require.main === module) {  // called directly i.e. "node app"  init().listen({ port: 3000 }, (err) => {    if (err) console.error(err);    console.log('server listening on 3000');  });} else {  // required as a module => executed on aws lambda  module.exports = init;}
```

```js
const awsLambdaFastify = require('@fastify/aws-lambda')const init = require('./app');const proxy = awsLambdaFastify(init())// or// const proxy = awsLambdaFastify(init(), { binaryMimeTypes: ['application/octet-stream'] })exports.handler = proxy;// or// exports.handler = (event, context, callback) => proxy(event, context, callback);// or// exports.handler = (event, context) => proxy(event, context);// or// exports.handler = async (event, context) => proxy(event, context);
```

```js
const fastify = require("fastify")({  logger: true // you can also define the level passing an object configuration to logger: {level: 'debug'}});
```

---

## Testing

**URL**: https://fastify.dev/docs/latest/Guides/Testing/

**Contents**:
- Testing
- Application​
  - Separating concerns makes testing easy​
  - Benefits of using fastify.inject()​
  - Testing with HTTP injection​
    - Another Example:​
  - Testing with a running server​
    - Example:​

Testing is one of the most important parts of developing an application. Fastify is very flexible when it comes to testing and is compatible with most testing frameworks (such as Node Test Runner, which is used in the examples below).

Let's cd into a fresh directory called 'testing-example' and type npm init -y in our terminal.

Run npm i fastify && npm i pino-pretty -D

First, we are going to separate our application code from our server code:

Fastify comes with built-in support for fake HTTP injection thanks to light-my-request.

Before introducing any tests, we will use the .inject method to make a fake request to our route:

First, our code will run inside an asynchronous function, giving us access to async/await.

.inject ensures all registered plugins have booted up and our application is ready to test. Finally, we pass the request method we want to use and a route. Using await we can store the response without a callback.

Run the test file in your terminal node app.test.js

Now we can replace our console.log calls with actual tests!

In your package.json change the "test" script to:

"test": "node --test --watch"

Finally, run npm test in the terminal and see your test results!

The inject method can do much more than a simple GET request to a URL:

.inject methods can also be chained by omitting the callback function:

or in the promisified version

Async await is supported as well!

Fastify can also be tested after starting the server with fastify.listen() or after initializing routes and plugins with fastify.ready().

Uses app.js from the previous example.

test-listen.js (testing with undici)

Alternatively, starting with Node.js 18, fetch may be used without requiring any extra dependencies:

test-ready.js (testing with SuperTest)

Now you should be able to step through your test file (and the rest of Fastify) in your code editor.

Let's cd into a fresh directory called 'testing-plugin-example' and type npm init -y in our terminal.

Run npm i fastify 

*[Content truncated - see full docs]*

**Examples**:

```js
'use strict'const fastify = require('fastify')function build(opts={}) {  const app = fastify(opts)  app.get('/', async function (request, reply) {    return { hello: 'world' }  })  return app}module.exports = build
```

```js
'use strict'const server = require('./app')({  logger: {    level: 'info',    transport: {      target: 'pino-pretty'    }  }})server.listen({ port: 3000 }, (err, address) => {  if (err) {    server.log.error(err)    process.exit(1)  }})
```

```js
'use strict'const build = require('./app')const test = async () => {  const app = build()  const response = await app.inject({    method: 'GET',    url: '/'  })  console.log('status code: ', response.statusCode)  console.log('body: ', response.body)}test()
```

---

## The hitchhiker's guide to plugins

**URL**: https://fastify.dev/docs/latest/Guides/Plugins-Guide/

**Contents**:
- The hitchhiker's guide to plugins
- Register​
- Decorators​
- Hooks​
- How to handle encapsulation and distribution​
- ESM support​
- Handle errors​
- Custom errors​

First of all, DON'T PANIC!

Fastify was built from the beginning to be an extremely modular system. We built a powerful API that allows you to add methods and utilities to Fastify by creating a namespace. We built a system that creates an encapsulation model, which allows you to split your application into multiple microservices at any moment, without the need to refactor the entire application.

As with JavaScript, where everything is an object, in Fastify everything is a plugin.

Your routes, your utilities, and so on are all plugins. To add a new plugin, whatever its functionality may be, in Fastify you have a nice and unique API: register.

register creates a new Fastify context, which means that if you perform any changes on the Fastify instance, those changes will not be reflected in the context's ancestors. In other words, encapsulation!

Why is encapsulation important?

Well, let's say you are creating a new disruptive startup, what do you do? You create an API server with all your stuff, everything in the same place, a monolith!

Ok, you are growing very fast and you want to change your architecture and try microservices. Usually, this implies a huge amount of work, because of cross dependencies and a lack of separation of concerns in the codebase.

Fastify helps you in that regard. Thanks to the encapsulation model, it will completely avoid cross dependencies and will help you structure your code into cohesive blocks.

Let's return to how to correctly use register.

As you probably know, the required plugins must expose a single function with the following signature

Where fastify is the encapsulated Fastify instance, options is the options object, and done is the function you must call when your plugin is ready.

Fastify's plugin model is fully reentrant and graph-based, it handles asynchronous code without any problems and it enforces both the load and close order of plugins. How? Glad you asked, check out avvio! Fastify starts loading the plugin after .

*[Content truncated - see full docs]*

**Examples**:

```js
fastify.register(  require('./my-plugin'),  { options })
```

```js
module.exports = function (fastify, options, done) {}
```

```js
module.exports = function (fastify, options, done) {  fastify.get('/plugin', (request, reply) => {    reply.send({ hello: 'world' })  })  done()}
```

---

## V3 Migration Guide

**URL**: https://fastify.dev/docs/latest/Guides/Migration-Guide-V3/

**Contents**:
- V3 Migration Guide
- Breaking changes​
  - Changed middleware support (#2014)​
  - Changed logging serialization (#2017)​
  - Changed schema substitution (#2023)​
  - Changed schema validation options (#2023)​
  - Changed preParsing hook behavior (#2286)​
  - Changed hooks behavior (#2004)​

Version 3 and before of Fastify are no longer maintained.

This guide is intended to help with migration from Fastify v2 to v3.

Before beginning please ensure that any deprecation warnings from v2 are fixed. All v2 deprecations have been removed and they will no longer work after upgrading. (#1750)

From Fastify v3, middleware support does not come out-of-the-box with the framework itself.

If you use Express middleware in your application, please install and register the @fastify/express or @fastify/middie plugin before doing so.

The logging Serializers have been updated to now Fastify Request and Reply objects instead of native ones.

Any custom serializers must be updated if they rely upon request or reply properties that are present on the native objects but not the Fastify objects.

The non-standard replace-way shared schema support has been removed. This feature has been replaced with JSON Schema specification compliant $ref based substitution. To help understand this change read Validation and Serialization in Fastify v3.

The setSchemaCompiler and setSchemaResolver options have been replaced with the setValidatorCompiler to enable future tooling improvements. To help understand this change read Validation and Serialization in Fastify v3.

From Fastify v3, the behavior of the preParsing hook will change slightly to support request payload manipulation.

The hook now takes an additional argument, payload, and therefore the new hook signature is fn(request, reply, payload, done) or async fn(request, reply, payload).

The hook can optionally return a new stream via done(null, stream) or returning the stream in case of async functions.

If the hook returns a new stream, it will be used instead of the original one in subsequent hooks. A sample use case for this is handling compressed requests.

The new stream should add the receivedEncodedLength property to the stream that should reflect the actual data size received from the client. For instance, in a compresse

*[Content truncated - see full docs]*

**Examples**:

```js
// Using the Express `cors` middleware in Fastify v2.fastify.use(require('cors')());
```

```js
// Using the Express `cors` middleware in Fastify v3.await fastify.register(require('@fastify/express'));fastify.use(require('cors')());
```

```js
const fastify = require('fastify')({  logger: {    serializers: {      res(res) {        return {          statusCode: res.statusCode,          customProp: res.customProp        };      }    }  }});
```

---

## V4 Migration Guide

**URL**: https://fastify.dev/docs/latest/Guides/Migration-Guide-V4/

**Contents**:
- V4 Migration Guide
- Codemods​
  - Fastify v4 Codemods​
- Breaking Changes​
  - Error handling composition (#3261)​
  - Removed app.use() (#3506)​
  - reply.res moved to reply.raw​
  - Need to return reply to signal a "fork" of the promise chain​

Version 3 and before of Fastify are no longer maintained.

This guide is intended to help with migration from Fastify v3 to v4.

Before migrating to v4, please ensure that you have fixed all deprecation warnings from v3. All v3 deprecations have been removed and they will no longer work after upgrading.

To help with the upgrade, we’ve worked with the team at Codemod to publish codemods that will automatically update your code to many of the new APIs and patterns in Fastify v4.

Run the following migration recipe to automatically update your code to Fastify v4:

This will run the following codemods:

Each of these codemods automates the changes listed in the v4 migration guide. For a complete list of available Fastify codemods and further details, see Codemod Registry.

When an error is thrown in an async error handler function, the upper-level error handler is executed if set. If there is no upper-level error handler, the default will be executed as it was previously:

The root error handler is Fastify’s generic error handler. This error handler will use the headers and status code in the Error object, if they exist. The headers and status code will not be automatically set if a custom error handler is provided.

With v4 of Fastify, app.use() has been removed and the use of middleware is no longer supported.

If you need to use middleware, use @fastify/middie or @fastify/express, which will continue to be maintained. However, it is strongly recommended that you migrate to Fastify's hooks.

Note: Codemod remove app.use() with:

If you previously used the reply.res attribute to access the underlying Request object you will now need to use reply.raw.

Note: Codemod reply.res to reply.raw with:

In some situations, like when a response is sent asynchronously or when you are not explicitly returning a response, you will now need to return the reply argument from your router handler.

Starting with v4, every GET route will create a sibling HEAD route. You can revert this

*[Content truncated - see full docs]*

**Examples**:

```text
npx codemod@latest fastify/4/migration-recipe
```

```js
import Fastify from 'fastify'const fastify = Fastify()fastify.register(async fastify => {  fastify.setErrorHandler(async err => {    console.log(err.message) // 'kaboom'    throw new Error('caught')  })  fastify.get('/encapsulated', async () => {    throw new Error('kaboom')  })})fastify.setErrorHandler(async err => {  console.log(err.message) // 'caught'  throw new Error('wrapped')})const res = await fastify.inject('/encapsulated')console.log(res.json().message) // 'wrapped'
```

```bash
npx codemod@latest fastify/4/remove-app-use
```

---

## V5 Migration Guide

**URL**: https://fastify.dev/docs/latest/Guides/Migration-Guide-V5/

**Contents**:
- V5 Migration Guide
- Long Term Support Cycle​
  - Why Node.js v20?​
- Breaking Changes​
  - Full JSON Schema is now required for querystring, params and body and response schemas​
  - New logger constructor signature​
  - useSemicolonDelimiter false by default​
  - The parameters object no longer has a prototype​

Version 3 and before of Fastify are no longer maintained.

This guide is intended to help with migration from Fastify v4 to v5.

Before migrating to v5, please ensure that you have fixed all deprecation warnings from v4. All v4 deprecations have been removed and will no longer work after upgrading.

Fastify v5 will only support Node.js v20+. If you are using an older version of Node.js, you will need to upgrade to a newer version to use Fastify v5.

Fastify v4 is still supported until June 30, 2025. If you are unable to upgrade, you should consider buying an end-of-life support plan from HeroDevs.

Fastify v5 will only support Node.js v20+ because it has significant differences compared to v18, such as better support for node:test. This allows us to provide a better developer experience and streamline maintenance.

Node.js v18 will exit Long Term Support on April 30, 2025, so you should be planning to upgrade to v20 anyway.

Starting with v5, Fastify will require a full JSON schema for the querystring, params and body schema. Note that the jsonShortHand option has been removed as well.

If the default JSON Schema validator is used, you will need to provide a full JSON schema for the querystring, params, body, and response schemas, including the type property.

See #5586 for more details

Note that it's still possible to override the JSON Schema validator to use a different format, such as Zod. This change simplifies that as well.

This change helps with integration of other tools, such as @fastify/swagger.

In Fastify v4, Fastify accepted the options to build a pino logger in the logger option, as well as a custom logger instance. This was the source of significant confusion.

As a result, the logger option will not accept a custom logger anymore in v5. To use a custom logger, you should use the loggerInstance option instead:

Starting with v5, Fastify instances will no longer default to supporting the use of semicolon delimiters in the query string as they did in v

*[Content truncated - see full docs]*

**Examples**:

```js
// v4fastify.get('/route', {  schema: {    querystring: {      name: { type: 'string' }    }  }}, (req, reply) => {  reply.send({ hello: req.query.name });});
```

```js
// v5fastify.get('/route', {  schema: {    querystring: {      type: 'object',      properties: {        name: { type: 'string' }      },      required: ['name']    }  }}, (req, reply) => {  reply.send({ hello: req.query.name });});
```

```js
// v4const logger = require('pino')();const fastify = require('fastify')({  logger});
```

---

## Write-Type-Provider

**URL**: https://fastify.dev/docs/latest/Guides/Write-Type-Provider/

**Contents**:
- Write-Type-Provider
- How to write your own type provider​
  - Type Contravariance​

Things to keep in mind when implementing a custom type provider:

Whereas exhaustive type narrowing checks normally rely on never to represent an unreachable state, reduction in type provider interfaces should only be done up to unknown.

The reasoning is that certain methods of FastifyInstance are contravariant on TypeProvider, which can lead to TypeScript surfacing assignability issues unless the custom type provider interface is substitutable with FastifyTypeProviderDefault.

For example, FastifyTypeProviderDefault will not be assignable to the following:

**Examples**:

```ts
export interface NotSubstitutableTypeProvider extends FastifyTypeProvider {   // bad, nothing is assignable to `never` (except for itself)  validator: this['schema'] extends /** custom check here**/ ? /** narrowed type here **/ : never;  serializer: this['schema'] extends /** custom check here**/ ? /** narrowed type here **/ : never;}
```

```ts
export interface SubstitutableTypeProvider extends FastifyTypeProvider {  // good, anything can be assigned to `unknown`  validator: this['schema'] extends /** custom check here**/ ? /** narrowed type here **/ : unknown;  serializer: this['schema'] extends /** custom check here**/ ? /** narrowed type here **/ : unknown;}
```

---
