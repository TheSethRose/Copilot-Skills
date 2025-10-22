# Svelte - Advanced

**Pages**: 2

---

## Stores

**URL**: https://svelte.dev/docs/svelte/stores

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

A store is an object that allows reactive access to a value via a simple store contract. The svelte/store module contains minimal store implementations which fulfil this contract.

Any time you have a reference to a store, you can access its value inside a component by prefixing it with the $ character. This causes Svelte to declare the prefixed variable, subscribe to the store at component initialisation and unsubscribe when appropriate.

Assignments to $-prefixed variables require that the variable be a writable store, and will result in a call to the store’s .set method.

Note that the store must be declared at the top level of the component — not inside an if block or a function, for example.

Local variables (that do not represent store values) must not have a $ prefix.

Prior to Svelte 5, stores were the go-to solution for creating cross-component reactive states or extracting logic. With runes, these use cases have greatly diminished.

Declares reactive state.

https://svelte.dev/docs/svelte/$state

Stores are still a good solution when you have complex asynchronous data streams or it’s important to have more manual control over updating values or listening to changes. If you’re familiar with RxJs and want to reuse that knowledge, the $ also comes in handy for you.

The svelte/store module contains a minimal store implementation which fulfil the store contract. It provides methods for creating stores that you can update from the outside, stores you can only update from the inside, and for combining and deriving stores.

Function that creates a store which has values that can be set from ‘outside’ components. It gets created as an object with additional set and update methods.

set is a method that takes one argument which is the value to be set. The store value gets set to the value of the argument if the store value is not already equal to it.

update is a method that takes one argument which is a callback. The callback takes the existing store value as its 

*[Content truncated - see full docs]*

**Examples**:

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

```javascript
const userState: {
    name: string;
}
```

---

## $app/stores

**URL**: https://svelte.dev/docs/kit/$app-stores

**Contents**:
  - Getting started
  - Core concepts
  - Build and deploy
  - Advanced
  - Best practices
  - Appendix
  - Reference
- $app/stores

This module contains store-based equivalents of the exports from $app/state. If you’re using SvelteKit 2.12 or later, use that module instead.

A readable store. When navigating starts, its value is a Navigation object with from, to, type and (if type === 'popstate') delta properties. When navigating finishes, its value reverts to null.

On the server, this store can only be subscribed to during component initialization. In the browser, it can be subscribed to at any time.

A readable store whose value contains page data.

On the server, this store can only be subscribed to during component initialization. In the browser, it can be subscribed to at any time.

A readable store whose initial value is false. If version.pollInterval is a non-zero value, SvelteKit will poll for new versions of the app and update the store value to true when it detects one. updated.check() will force an immediate check, regardless of polling.

On the server, this store can only be subscribed to during component initialization. In the browser, it can be subscribed to at any time.

Use navigating from $app/state instead (requires Svelte 5, see docs for more info)

A readable store. When navigating starts, its value is a Navigation object with from, to, type and (if type === 'popstate') delta properties. When navigating finishes, its value reverts to null.

On the server, this store can only be subscribed to during component initialization. In the browser, it can be subscribed to at any time.

Use page from $app/state instead (requires Svelte 5, see docs for more info)

A readable store whose value contains page data.

On the server, this store can only be subscribed to during component initialization. In the browser, it can be subscribed to at any time.

Use updated from $app/state instead (requires Svelte 5, see docs for more info)

A readable store whose initial value is false. If version.pollInterval is a non-zero value, SvelteKit will poll for new versions of the app and update the stor

*[Content truncated - see full docs]*

**Examples**:

```python
import { function getStores(): {
    page: typeof page;
    navigating: typeof navigating;
    updated: typeof updated;
}getStores, const navigating: Readable<Navigation | null>A readable store.
When navigating starts, its value is a Navigation object with from, to, type and (if type === 'popstate') delta properties.
When navigating finishes, its value reverts to null.
On the server, this store can only be subscribed to during component initialization. In the browser, it can be subscribed to at 
...
```

```javascript
function getStores(): {
    page: typeof page;
    navigating: typeof navigating;
    updated: typeof updated;
}
```

```javascript
function getStores(): {
    page: typeof page;
    navigating: typeof navigating;
    updated: typeof updated;
}
```

---
