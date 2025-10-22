# Sveltekit - Common Patterns

Quick reference for common sveltekit patterns and usage.

## Code Patterns

### 1. Getting started IntroductionCreating a projectProject typesProject structureWeb standardsCore concep

```
/[org]/[repo]/tree/[branch]/[...file]
```

### 2. SvelteKitAdvanced Advanced routing On this page Advanced routing Rest parametersOptional parametersM

```
/[org]/[repo]/tree/[branch]/[...file]
```

### 3. SvelteKitAdvanced Advanced routing On this page Advanced routing Rest parametersOptional parametersM

```
/[org]/[repo]/tree/[branch]/[...file]
```

### 4. Pages can break out of the current layout hierarchy on a route-by-route basis. Suppose we have an /i

```
/item/[id]/embed
```

### 5. Getting started IntroductionCreating a projectProject typesProject structureWeb standardsCore concep

```
+page.svelte
```

### 6. SvelteKitCore concepts Loading data On this page Loading data Page dataLayout datapage.dataUniversal

```
+page.svelte
```

### 7. SvelteKitCore concepts Loading data On this page Loading data Page dataLayout datapage.dataUniversal

```
+page.svelte
```

### 8. Before a +page.svelte component (and its containing +layout.svelte components) can be rendered, we o

```
+page.svelte
```

## Examples

### Example 1

```javascript
function load({ params }: {
    params: any;
}): {
    post: {
        title: string;
        content: string;
    };
}
```

### Example 2

```javascript
const adapter: (opts: any) => import("@sveltejs/kit").Adapter
```

### Example 3

```javascript
const adapter: () => import("@sveltejs/kit").Adapter
```

### Example 4

```javascript
function error(status: number, body: App.Error): never (+1 overload)
```

### Example 5

```javascript
/** @satisfies {import('./$types').Actions} */
export const const actions: {
    default: (event: any) => Promise<void>;
}@satisfies{import('./$types').Actions}actions = {
	default: (event: any) => Promise<void>default: async (event: anyevent) => {
		// TODO log the user in
	}
};
```

### Example 6

```javascript
const actions: {
    default: (event: any) => Promise<void>;
}
```

### Example 7

```javascript
function handle({ event, resolve }: {
    event: any;
    resolve: any;
}): Promise<any>
```

### Example 8

```python
<script>
	import logo from '$lib/assets/logo.png';
</script>

<img alt="The project logo" src={logo} />
```

### Example 9

```javascript
const config: {
    kit: {
        experimental: {
 tracing: {
   server: boolean;
 };
 instrumentation: {
   server: boolean;
 };
        };
    };
}
```


## Categories

See organized documentation in `references/`:

- `references/building.md` - Building
- `references/introduction.md` - Introduction
- `references/other.md` - Other
