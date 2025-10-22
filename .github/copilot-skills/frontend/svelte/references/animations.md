# Svelte - Animations

**Pages**: 1

---

## animate:

**URL**: https://svelte.dev/docs/svelte/animate

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

An animation is triggered when the contents of a keyed each block are re-ordered. Animations do not run when an element is added or removed, only when the index of an existing data item within the each block changes. Animate directives must be on an element that is an immediate child of a keyed each block.

Animations can be used with Svelte’s built-in animation functions or custom animation functions.

As with actions and transitions, animations can have parameters.

(The double {{curlies}} aren’t a special syntax; this is an object literal inside an expression tag.)

Animations can use custom functions that provide the node, an animation object and any parameters as arguments. The animation parameter is an object containing from and to properties each containing a DOMRect describing the geometry of the element in its start and end positions. The from property is the DOMRect of the element in its starting position, and the to property is the DOMRect of the element in its final position after the list has been reordered and the DOM updated.

If the returned object has a css method, Svelte will create a web animation that plays on the element.

The t argument passed to css is a value that goes from 0 and 1 after the easing function has been applied. The u argument is equal to 1 - t.

The function is called repeatedly before the animation begins, with different t and u arguments.

A custom animation function can also return a tick function, which is called during the animation with the same t and u arguments.

If it’s possible to use css instead of tick, do so — web animations can run off the main thread, preventing jank on slower devices.

Edit this page on GitHub llms.txt

**Examples**:

```text
<!-- When `list` is reordered the animation will run -->
{#each list as item, index (item)}
	<li animate:flip>{item}</li>
{/each}
```

```text
{#each list as item, index (item)}
	<li animate:flip={{ delay: 500 }}>{item}</li>
{/each}
```

```javascript
animation = (node: HTMLElementnode: HTMLElement, { from: anyfrom: type DOMRect: anyDOMRect, to: anyto: type DOMRect: anyDOMRect } , params: anyparams: any) => {
	delay?: number,
	duration?: number,
	easing?: (t: numbert: number) => number,
	css?: (t: numbert: number, u: numberu: number) => string,
	tick?: (t: numbert: number, u: numberu: number) => void
}
```

---
