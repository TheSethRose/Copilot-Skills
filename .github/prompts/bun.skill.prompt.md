---
description: Fast all-in-one JavaScript runtime
---

# Bun

**Purpose**: Fast all-in-one JavaScript runtime

## When to Use This Skill

Use this skill when:
- Working with bun projects
- Implementing bun features
- Debugging bun code
- Learning bun best practices
- Building applications with bun

**Keywords**: bun, cli, api, other

## Quick Reference

### Common Patterns

**1. For example:**

```
[name]
```

**2. try { const result = await Bun.build({ entrypoints: ["./index.tsx"], outdir: "./**

```
try {
  const result = await Bun.build({
    entrypoints: ["./index.tsx"],
    outdir: "./out",
  });
} catch (e) {
  // TypeScript does not allow annotations on the catch clause
  const error = e as 
```

**3. try { const result = await Bun.build({ entrypoints: ["./index.tsx"], outdir: "./**

```
try {
  const result = await Bun.build({
    entrypoints: ["./index.tsx"],
    outdir: "./out",
  });
} catch (e) {
  // TypeScript does not allow annotations on the catch clause
  const error = e as 
```

**4. try { const result = await Bun.build({ entrypoints: ["./index.tsx"], outdir: "./**

```
try {
  const result = await Bun.build({
    entrypoints: ["./index.tsx"],
    outdir: "./out",
  });
} catch (e) {
  // TypeScript does not allow annotations on the catch clause
  const error = e as 
```

**5. # Example: Enable quiet output for Claude CodeCLAUDECODE=1 bun test # Still show**

```
# Example: Enable quiet output for Claude Code
```

### Code Examples

**Example 1** (typescript):
```typescript
await Bun.build({
  entrypoints: ['./index.tsx'],
  outdir: './build',
});
```

**Example 2** (typescript):
```typescript
bun build ./index.tsx --outdir ./build
```

**Example 3** (javascript):
```javascript
const foo = Bun.file("foo.txt"); // relative to cwd
foo.size; // number of bytes
foo.type; // MIME type
```

**Example 4** (javascript):
```javascript
const foo = Bun.file("foo.txt");

await foo.text(); // contents as a string
await foo.stream(); // contents as ReadableStream
await foo.arrayBuffer(); // contents as ArrayBuffer
await foo.bytes(); // contents as Uint8Array
```

**Example 5** (python):
```python
import { Database } from "bun:sqlite";

const db = new Database(":memory:");
const query = db.query("select 'Hello world' as message;");
query.get(); // => { message: "Hello world" }
```

## Reference Documentation

This skill includes comprehensive documentation in `.github/copilot-skills/bun/references/`:

- **api.md** - Api documentation
- **cli.md** - Cli documentation
- **other.md** - Other documentation

## How to Use

### For Quick Answers
Ask directly about bun features, APIs, or patterns.

### For Detailed Information
Reference specific documentation files:
- Check `references/getting_started.md` for setup
- Check `references/api_reference.md` for API details
- Check category files for specific topics

### For Code Examples
Use the Quick Reference patterns above or ask for specific examples.

## Related Skills

- None (standalone skill)

## More Information

- **Base Documentation**: https://bun.sh/docs/
- **Generated**: 2025-10-20
- **Total Pages**: 11
