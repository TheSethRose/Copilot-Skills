# Bun - Common Patterns

Quick reference for common bun patterns and usage.

## Code Patterns

### 1. # Example: Enable quiet output for Claude CodeCLAUDECODE=1 bun test # Still shows failures and summa

```
# Example: Enable quiet output for Claude Code
```

### 2. # Example: Enable quiet output for Claude Code

```
# Example: Enable quiet output for Claude Code
```

### 3. # Example: Enable quiet output for Claude Code

```
# Example: Enable quiet output for Claude Code
```

### 4. For Linux usersThe recommended minimum Linux Kernel version is 5.6. If you're on Linux kernel 5.1 - 

```
bun install
```

### 5. The recommended minimum Linux Kernel version is 5.6. If you're on Linux kernel 5.1 - 5.5, bun instal

```
bun install
```

### 6. If you're using Ubuntu 20.04, here's how to install a newer kernel:

```
# If this returns a version >= 5.6, you don't need to do anything
```

### 7. For example:

```
[name]
```

### 8. try { const result = await Bun.build({ entrypoints: ["./index.tsx"], outdir: "./out", }); } catch (e

```
try {
  const result = await Bun.build({
    entrypoints: ["./index.tsx"],
    outdir: "./out",
  });
} catch (e) {
  // TypeScript does not allow annotations on the catch clause
  const error = e as AggregateError;
  console.error("Build Failed");

  // Example: Using the built-in formatter
  conso
```

## Examples

### Example 1

```python
import { expect, test } from "bun:test";

test("2 + 2", () => {
  expect(2 + 2).toBe(4);
});
```

### Example 2

```typescript
bun create ./MyComponent.jsx # .tsx also supported
```

### Example 3

```javascript
const foo = Bun.file("foo.txt"); // relative to cwd
foo.size; // number of bytes
foo.type; // MIME type
```

### Example 4

```javascript
const foo = Bun.file("foo.txt");

await foo.text(); // contents as a string
await foo.stream(); // contents as ReadableStream
await foo.arrayBuffer(); // contents as ArrayBuffer
await foo.bytes(); // contents as Uint8Array
```

### Example 5

```python
import { Database } from "bun:sqlite";

const db = new Database(":memory:");
const query = db.query("select 'Hello world' as message;");
query.get(); // => { message: "Hello world" }
```

### Example 6

```python
import { Database } from "bun:sqlite";

const db = new Database("mydb.sqlite");
```

### Example 7

```typescript
await Bun.build({
  entrypoints: ['./index.tsx'],
  outdir: './build',
});
```

### Example 8

```typescript
bun build ./index.tsx --outdir ./build
```

### Example 9

```typescript
bun run index.tsx  # TS and JSX supported out of the box
```


## Categories

See organized documentation in `references/`:

- `references/api.md` - Api
- `references/cli.md` - Cli
- `references/other.md` - Other
