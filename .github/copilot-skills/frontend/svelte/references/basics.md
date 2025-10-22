# Svelte - Basics

**Pages**: 1

---

## Basic markup

**URL**: https://svelte.dev/docs/svelte/basic-markup

**Contents**:
  - Introduction
  - Runes
  - Template syntax
  - Styling
  - Special elements
  - Runtime
  - Misc
  - Reference

Markup inside a Svelte component can be thought of as HTML++.

A lowercase tag, like <div>, denotes a regular HTML element. A capitalised tag or a tag that uses dot notation, such as <Widget> or <my.stuff>, indicates a component.

By default, attributes work exactly like their HTML counterparts.

As in HTML, values may be unquoted.

Attribute values can contain JavaScript expressions.

Or they can be JavaScript expressions.

Boolean attributes are included on the element if their value is truthy and excluded if it’s falsy.

All other attributes are included unless their value is nullish (null or undefined).

Quoting a singular expression does not affect how the value is parsed, but in Svelte 6 it will cause the value to be coerced to a string:

When the attribute name and value match (name={name}), they can be replaced with {name}.

By convention, values passed to components are referred to as properties or props rather than attributes, which are a feature of the DOM.

As with elements, name={name} can be replaced with the {name} shorthand.

Spread attributes allow many attributes or properties to be passed to an element or component at once.

An element or component can have multiple spread attributes, interspersed with regular ones. Order matters — if things.a exists it will take precedence over a="b", while c="d" would take precedence over things.c:

Listening to DOM events is possible by adding attributes to the element that start with on. For example, to listen to the click event, add the onclick attribute to a button:

Event attributes are case sensitive. onclick listens to the click event, onClick listens to the Click event, which is different. This ensures you can listen to custom events that have uppercase characters in them.

Because events are just attributes, the same rules as for attributes apply:

Timing-wise, event attributes always fire after events from bindings (e.g. oninput always fires after an update to bind:value). Under the hood, some event ha

*[Content truncated - see full docs]*

**Examples**:

```python
<script>
	import Widget from './Widget.svelte';
</script>

<div>
	<Widget />
</div>
```

```text
<div class="foo">
	<button disabled>can't touch this</button>
</div>
```

```text
<input type=checkbox />
```

---
