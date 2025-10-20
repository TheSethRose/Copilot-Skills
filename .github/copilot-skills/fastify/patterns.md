# Fastify - Common Patterns

Quick reference for common fastify patterns and usage.

## Code Patterns

### 1. GuidesGetting-StartedVersion: latest (v5.6.x)On this pageGetting-StartedGetting Started​ Hello! Than

```
npm i fastify
```

### 2. GuidesGetting-StartedVersion: latest (v5.6.x)On this pageGetting-StartedGetting Started​ Hello! Than

```
npm i fastify
```

### 3. GuidesGetting-StartedVersion: latest (v5.6.x)On this pageGetting-StartedGetting Started​ Hello! Than

```
npm i fastify
```

### 4. GuidesGetting-StartedVersion: latest (v5.6.x)On this pageGetting-StartedGetting Started​ Hello! Than

```
npm i fastify
```

### 5. Getting-StartedGetting Started​ Hello! Thank you for checking out Fastify! This document aims to be 

```
npm i fastify
```

### 6. GuidesBenchmarkingVersion: latest (v5.6.x)On this pageBenchmarkingBenchmarking​ Benchmarking is impo

```
npm run benchmark
```

### 7. GuidesBenchmarkingVersion: latest (v5.6.x)On this pageBenchmarkingBenchmarking​ Benchmarking is impo

```
npm run benchmark
```

### 8. GuidesBenchmarkingVersion: latest (v5.6.x)On this pageBenchmarkingBenchmarking​ Benchmarking is impo

```
npm run benchmark
```

## Examples

### Example 1

```sh
npm i fastify
```

### Example 2

```sh
yarn add fastify
```

### Example 3

```sh
npm run benchmark
```

### Example 4

```sh
npx -p node@10 -- npm run benchmark
```

### Example 5

```sh
[ -d /Applications/VSCodeFastify/Visual\ Studio\ Code.app ] && echo "found"
```

### Example 6

```sh
xattr -dr com.apple.quarantine /Applications/VSCodeFastify/Visual\ Studio\ Code.app
```

### Example 7

```js
app.get('/', async (request, reply) => {  request.raw.on('close', () => {    if (request.raw.aborted) {      app.log.info('request closed')    }  })  await sleep(3000)  reply.code(200).send({ ok: true })})
```

### Example 8

```js
await fastify.register(require('@fastify/express'))fastify.use(require('cors')())fastify.use(require('dns-prefetch-control')())fastify.use(require('frameguard')())fastify.use(require('hsts')())fastify.use(require('ienoopen')())fastify.use(require('x-xss-protection')())
```

### Example 9

```js
await fastify.register(require('@fastify/middie'))fastify.use(require('cors')())
```

### Example 10

```js
fastify.register(plugin, [options])
```


## Categories

See organized documentation in `references/`:

- `references/getting_started.md` - Getting Started
- `references/guides.md` - Guides
- `references/other.md` - Other
- `references/plugins.md` - Plugins
