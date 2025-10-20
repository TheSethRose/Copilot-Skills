# Svelte - Common Patterns

Quick reference for common svelte patterns and usage.

## Code Patterns

### 1. Introduction OverviewGetting started.svelte files.svelte.js and .svelte.ts filesRunes What are runes

```
<div>
```

### 2. SvelteTemplate syntax Basic markup On this page Basic markup TagsElement attributesComponent propsSp

```
<div>
```

### 3. SvelteTemplate syntax Basic markup On this page Basic markup TagsElement attributesComponent propsSp

```
<div>
```

### 4. Markup inside a Svelte component can be thought of as HTML++. TagsA lowercase tag, like <div>, denot

```
<div>
```

### 5. Markup inside a Svelte component can be thought of as HTML++. TagsA lowercase tag, like <div>, denot

```
<div>
```

### 6. Introduction OverviewGetting started.svelte files.svelte.js and .svelte.ts filesRunes What are runes

```
svelte/store
```

### 7. SvelteRuntime Stores On this page Stores When to use storessvelte/storeStore contract A store is an 

```
svelte/store
```

### 8. SvelteRuntime Stores On this page Stores When to use storessvelte/storeStore contract A store is an 

```
svelte/store
```

## Examples

### Example 1

```python
<script>
	import Widget from './Widget.svelte';
</script>

<div>
	<Widget />
</div>
```

### Example 2

```python
<script>
	import { writable } from 'svelte/store';

	const count = writable(0);
	console.log($count); // logs 0

	count.set(1);
	console.log($count); // logs 1

	$count = 2;
	console.log($count); // logs 2
</script>
```

### Example 3

```javascript
export const const userState: {
    name: string;
}userState = function $state<{
    name: string;
}>(initial: {
    name: string;
}): {
    name: string;
} (+1 overload)
namespace $stateDeclares reactive state.
Example:
let count = $state(0);https://svelte.dev/docs/svelte/$state
@paraminitial The initial value$state({
	name: stringname: 'name',
	/* ... */
});
```

### Example 4

```javascript
function getStores(): {
    page: typeof page;
    navigating: typeof navigating;
    updated: typeof updated;
}
```

### Example 5

```javascript
const adapter: (opts: any) => import("@sveltejs/kit").Adapter
```

### Example 6

```javascript
import { const building: booleanSvelteKit analyses your app during the build step by running it. During this process, building is true. This also applies during prerendering.
```

### Example 7

```javascript
const building: boolean
```


## Categories

See organized documentation in `references/`:

- `references/advanced.md` - Advanced
- `references/animations.md` - Animations
- `references/basics.md` - Basics
- `references/introduction.md` - Introduction
- `references/other.md` - Other
