# Bun - Api

**Pages**: 4

---

## File I/O

**URL**: https://bun.sh/docs/api/file-io

**Contents**:
- Reading files (Bun.file())
  - Deleting files (file.delete())
- Writing files (Bun.write())
- Incremental writing with FileSink
- Directories
  - Reading directories (readdir)
    - Reading directories recursively
  - Creating directories (mkdir)

Note — The Bun.file and Bun.write APIs documented on this page are heavily optimized and represent the recommended way to perform file-system tasks using Bun. For operations that are not yet available with Bun.file, such as mkdir or readdir, you can use Bun's nearly complete implementation of the node:fs module.

Bun provides a set of optimized APIs for reading and writing files.

Bun.file(path): BunFile

Create a BunFile instance with the Bun.file(path) function. A BunFile represents a lazily-loaded file; initializing it does not actually read the file from disk.

The reference conforms to the Blob interface, so the contents can be read in various formats.

File references can also be created using numerical file descriptors or file:// URLs.

A BunFile can point to a location on disk where a file does not exist.

The default MIME type is text/plain;charset=utf-8, but it can be overridden by passing a second argument to Bun.file.

For convenience, Bun exposes stdin, stdout and stderr as instances of BunFile.

You can delete a file by calling the .delete() function.

Bun.write(destination, data): Promise<number>

The Bun.write function is a multi-tool for writing payloads of all kinds to disk.

The first argument is the destination which can have any of the following types:

The second argument is the data to be written. It can be any of the following:

All possible permutations are handled using the fastest available system calls on the current platform.

To write a string to disk:

To copy a file to another location on disk:

To write a byte array to disk:

To write a file to stdout:

To write the body of an HTTP response to disk:

Bun provides a native incremental file writing API called FileSink. To retrieve a FileSink instance from a BunFile:

To incrementally write to the file, call .write().

These chunks will be buffered internally. To flush the buffer to disk, use .flush(). This returns the number of flushed bytes.

The buffer will also auto-flush when the F

*[Content truncated - see full docs]*

**Examples**:

```javascript
const foo = Bun.file("foo.txt"); // relative to cwd
foo.size; // number of bytes
foo.type; // MIME type
```

```javascript
const foo = Bun.file("foo.txt");

await foo.text(); // contents as a string
await foo.stream(); // contents as ReadableStream
await foo.arrayBuffer(); // contents as ArrayBuffer
await foo.bytes(); // contents as Uint8Array
```

```text
Bun.file(1234);
Bun.file(new URL(import.meta.url)); // reference to the current file
```

---

## HTTP server

**URL**: https://bun.sh/docs/api/http

**Contents**:
- Bun.serve()
  - Routing
    - Async/await in routes
    - Promise in routes
    - Type-safe route parameters
  - Static responses
  - File Responses vs Static Responses
  - HTTP Caching Behavior

The page primarily documents the Bun-native Bun.serve API. Bun also implements fetch and the Node.js http and https modules.

These modules have been re-implemented to use Bun's fast internal HTTP infrastructure. Feel free to use these modules directly; frameworks like Express that depend on these modules should work out of the box. For granular compatibility information, see Runtime > Node.js APIs.

To start a high-performance HTTP server with a clean API, the recommended approach is Bun.serve.

Use Bun.serve to start an HTTP server in Bun.

Routes in Bun.serve() receive a BunRequest (which extends Request) and return a Response or Promise<Response>. This makes it easier to use the same code for both sending & receiving HTTP requests.

You can use async/await in route handlers to return a Promise<Response>.

You can also return a Promise<Response> from a route handler.

TypeScript parses route parameters when passed as a string literal, so that your editor will show autocomplete when accessing request.params.

Percent-encoded route parameter values are automatically decoded. Unicode characters are supported. Invalid unicode is replaced with the unicode replacement character &0xFFFD;.

Routes can also be Response objects (without the handler function). Bun.serve() optimizes it for zero-allocation dispatch - perfect for health checks, redirects, and fixed content:

Static responses do not allocate additional memory after initialization. You can generally expect at least a 15% performance improvement over manually returning a Response object.

Static route responses are cached for the lifetime of the server object. To reload static routes, call server.reload(options).

When serving files in routes, there are two distinct behaviors depending on whether you buffer the file content or serve it directly:

Static routes (new Response(await file.bytes())) buffer content in memory at startup:

File routes (new Response(Bun.file(path))) read from filesystem per request:

Both

*[Content truncated - see full docs]*

**Examples**:

```javascript
Bun.serve({
  // `routes` requires Bun v1.2.3+
  routes: {
    // Static routes
    "/api/status": new Response("OK"),

    // Dynamic routes
    "/users/:id": req => {
      return new Response(`Hello User ${req.params.id}!`);
    },

    // Per-HTTP method handlers
    "/api/posts": {
      GET: () => new Response("List posts"),
      POST: async req => {
        const body = await req.json();
        return Response.json({ created: true, ...body });
      },
    },

    // Wildcard route for 
...
```

```text
// Simplified for brevity
interface BunRequest<T extends string> extends Request {
  params: Record<T, string>;
  readonly cookies: CookieMap;
}
```

```python
import { sql, serve } from "bun";

serve({
  port: 3001,
  routes: {
    "/api/version": async () => {
      const [version] = await sql`SELECT version()`;
      return Response.json(version);
    },
  },
});
```

---

## SQLite

**URL**: https://bun.sh/docs/api/sqlite

**Contents**:
- Database
  - Strict mode
  - Load via ES module import
  - .close(throwOnError: boolean = false)
  - using statement
  - .serialize()
  - .query()
- WAL mode

Bun natively implements a high-performance SQLite3 driver. To use it import from the built-in bun:sqlite module.

The API is simple, synchronous, and fast. Credit to better-sqlite3 and its contributors for inspiring the API of bun:sqlite.

The bun:sqlite module is roughly 3-6x faster than better-sqlite3 and 8-9x faster than deno.land/x/sqlite for read queries. Each driver was benchmarked against the Northwind Traders dataset. View and run the benchmark source.

To open or create a SQLite3 database:

To open an in-memory database:

To open in readonly mode:

To create the database if the file doesn't exist:

By default, bun:sqlite requires binding parameters to include the $, :, or @ prefix, and does not throw an error if a parameter is missing.

To instead throw an error when a parameter is missing and allow binding without a prefix, set strict: true on the Database constructor:

You can also use an import attribute to load a database.

This is equivalent to the following:

To close a database connection, but allow existing queries to finish, call .close(false):

To close the database and throw an error if there are any pending queries, call .close(true):

Note: close(false) is called automatically when the database is garbage collected. It is safe to call multiple times but has no effect after the first.

You can use the using statement to ensure that a database connection is closed when the using block is exited.

bun:sqlite supports SQLite's built-in mechanism for serializing and deserializing databases to and from memory.

Internally, .serialize() calls sqlite3_serialize.

Use the db.query() method on your Database instance to prepare a SQL query. The result is a Statement instance that will be cached on the Database instance. The query will not be executed.

Note — Use the .prepare() method to prepare a query without caching it on the Database instance.

SQLite supports write-ahead log mode (WAL) which dramatically improves performance, especially in situations

*[Content truncated - see full docs]*

**Examples**:

```python
import { Database } from "bun:sqlite";

const db = new Database(":memory:");
const query = db.query("select 'Hello world' as message;");
query.get(); // => { message: "Hello world" }
```

```python
import { Database } from "bun:sqlite";

const db = new Database("mydb.sqlite");
```

```python
import { Database } from "bun:sqlite";

// all of these do the same thing
const db = new Database(":memory:");
const db = new Database();
const db = new Database("");
```

---

## WebSockets

**URL**: https://bun.sh/docs/api/websockets

**Contents**:
- Start a WebSocket server
  - Sending messages
  - Headers
  - Contextual data
  - Pub/Sub
  - Compression
  - Backpressure
  - Timeouts and limits

Bun.serve() supports server-side WebSockets, with on-the-fly compression, TLS support, and a Bun-native publish-subscribe API.

⚡️ 7x more throughput — Bun's WebSockets are fast. For a simple chatroom on Linux x64, Bun can handle 7x more requests per second than Node.js + "ws".

Internally Bun's WebSocket implementation is built on uWebSockets.

Below is a simple WebSocket server built with Bun.serve, in which all incoming requests are upgraded to WebSocket connections in the fetch handler. The socket handlers are declared in the websocket parameter.

The following WebSocket event handlers are supported:

An API designed for speed

In Bun, handlers are declared once per server, instead of per socket.

ServerWebSocket expects you to pass a WebSocketHandler object to the Bun.serve() method which has methods for open, message, close, drain, and error. This is different than the client-side WebSocket class which extends EventTarget (onmessage, onopen, onclose),

Clients tend to not have many socket connections open so an event-based API makes sense.

But servers tend to have many socket connections open, which means:

So, instead of using an event-based API, ServerWebSocket expects you to pass a single object with methods for each event in Bun.serve() and it is reused for each connection.

This leads to less memory usage and less time spent adding/removing event listeners.

The first argument to each handler is the instance of ServerWebSocket handling the event. The ServerWebSocket class is a fast, Bun-native implementation of WebSocket with some additional features.

Each ServerWebSocket instance has a .send() method for sending messages to the client. It supports a range of input types.

Once the upgrade succeeds, Bun will send a 101 Switching Protocols response per the spec. Additional headers can be attached to this Response in the call to server.upgrade().

Contextual data can be attached to a new WebSocket in the .upgrade() call. This data is made available on the

*[Content truncated - see full docs]*

**Examples**:

```text
Bun.serve({
  fetch(req, server) {
    // upgrade the request to a WebSocket
    if (server.upgrade(req)) {
      return; // do not return a Response
    }
    return new Response("Upgrade failed", { status: 500 });
  },
  websocket: {}, // handlers
});
```

```text
Bun.serve({
  fetch(req, server) {}, // upgrade logic
  websocket: {
    message(ws, message) {}, // a message is received
    open(ws) {}, // a socket is opened
    close(ws, code, message) {}, // a socket is closed
    drain(ws) {}, // the socket is ready to receive more data
  },
});
```

```text
Bun.serve({
  fetch(req, server) {}, // upgrade logic
  websocket: {
    message(ws, message) {
      ws.send(message); // echo back the message
    },
  },
});
```

---
