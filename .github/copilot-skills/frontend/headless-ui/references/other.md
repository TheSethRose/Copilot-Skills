# Headless-Ui - Other

**Pages**: 6

---

## Checkbox - Headless UI

**URL**: https://headlessui.com/react/checkbox

**Contents**:
- Components
  - Forms
- Checkbox
- Installation
- Basic example
- Styling
  - Using data attributes
  - Using render props

Checkboxes provide the same functionality as native HTML checkboxes, without any of the styling, giving you a clean slate to design them however you'd like.

To get started, install Headless UI via npm:

Checkboxes are built using the Checkbox component. You can toggle your checkbox by clicking directly on the component, or by pressing the spacebar while it's focused.

Toggling the checkbox calls the onChange function with the new checked value.

Headless UI keeps track of a lot of state about each component, like whether or not a checkbox is checked, whether a popover is open or closed, or which item in a menu is currently focused via the keyboard.

But because the components are headless and completely unstyled out of the box, you can't see this information in your UI until you provide the styles you want for each state yourself.

The easiest way to style the different states of a Headless UI component is using the data-* attributes that each component exposes.

For example, the Checkbox component exposes a data-checked attribute, which tells you if the checkbox is currently checked, and a data-disabled attribute, which tells you if the checkbox is currently disabled.

Use the CSS attribute selector to conditionally apply styles based on the presence of these data attributes. If you're using Tailwind CSS, the data attribute modifier makes this easy:

See the component API for a list of all the available data attributes.

Each component also exposes information about its current state via render props that you can use to conditionally apply different styles or render different content.

For example, the Checkbox component exposes a checked state, which tells you if the checkbox is currently checked, and a disabled state, which tells you if the checkbox is currently disabled.

See the component API for a list of all the available render props.

Wrap a Label and Checkbox with the Field component to automatically associate them using a generated ID:

By default, click

*[Content truncated - see full docs]*

**Examples**:

```shell
npm install @headlessui/react
```

```jsx
import { Checkbox } from '@headlessui/react'
import { useState } from 'react'

function Example() {
  const [enabled, setEnabled] = useState(false)

  return (
    <Checkbox
      checked={enabled}
      onChange={setEnabled}
      className="group block size-4 rounded border bg-white data-checked:bg-blue-500"
    >
      {/* Checkmark icon */}
      <svg className="stroke-white opacity-0 group-data-checked:opacity-100" viewBox="0 0 14 14" fill="none">
        <path d="M3 8L6 11L11 3.5" strokeWi
...
```

```html
<!-- Rendered `Checkbox` -->
<span role="checkbox" data-checked data-disabled>
  <!-- ... -->
</span>
```

---

## Fieldset - Headless UI

**URL**: https://headlessui.com/react/fieldset

**Contents**:
- Components
  - Forms
- Fieldset
- Installation
- Basic example
- Styling
  - Using data attributes
  - Using render props

Group a set of form controls together with these fully accessible but much easier-to-style versions of the native fieldset and legend elements.

To get started, install Headless UI via npm:

Use the Fieldset and Legend components to group a set of form controls together with a title:

Since the native HTML <legend> element is difficult to style, the Legend component is rendered as a <div>. The <Fieldset> component uses the native <fieldset> component.

Headless UI keeps track of a lot of state about each component, like whether or not a fieldset is disabled, whether a popover is open or closed, or which item in a menu is currently focused via the keyboard.

But because the components are headless and completely unstyled out of the box, you can't see this information in your UI until you provide the styles you want for each state yourself.

The easiest way to style the different states of a Headless UI component is using the data-* attributes that each component exposes.

For example, both the Fieldset and Legend components expose a data-disabled attribute, which tells you if the fieldset is currently disabled.

Use the CSS attribute selector to conditionally apply styles based on the presence of these data attributes. If you're using Tailwind CSS, the data attribute modifier makes this easy:

See the component API for a list of all the available data attributes.

Each component also exposes information about its current state via render props that you can use to conditionally apply different styles or render different content.

For example, both the Fieldset and Legend components expose a disabled state, which tells you if the fieldset is currently disabled.

See the component API for a list of all the available render props.

Add the disabled prop to a Fieldset component to disable the entire fieldset:

Group a set of form controls together with a title.

The element or component the fieldset should render as.

Use this to disable all form controls in the fieldset.

*[Content truncated - see full docs]*

**Examples**:

```shell
npm install @headlessui/react
```

```jsx
import { Field, Fieldset, Input, Label, Legend, Select, Textarea } from '@headlessui/react'

function Example() {
  return (
    <Fieldset className="space-y-8">
      <Legend className="text-lg font-bold">Shipping details</Legend>
      <Field>
        <Label className="block">Street address</Label>
        <Input className="mt-1 block" name="address" />
      </Field>
      <Field>
        <Label className="block">Country</Label>
        <Select className="mt-1 block" name="country">
         
...
```

```html
<!-- Rendered `Fieldset` and `Legend` -->
<fieldset aria-labelledby="..." disabled data-disabled>
  <div id="..." data-disabled>Shipping details</div>
  <!-- ... -->
</fieldset>
```

---

## Headless UI - Unstyled, fully accessible UI components

**URL**: https://headlessui.com/v1/vue

---

## Input - Headless UI

**URL**: https://headlessui.com/react/input

**Contents**:
- Components
  - Forms
- Input
- Installation
- Basic example
- Styling
  - Using data attributes
  - Using render props

A light wrapper around the native input element that handles tedious accessibility concerns and provides more opinionated states for things like hover and focus.

To get started, install Headless UI via npm:

Inputs are built using the Input component:

You can pass any props to an Input that you'd normally pass to the native input element.

Headless UI keeps track of a lot of state about each component, like whether or not an input is focused, whether a popover is open or closed, or which item in a menu is currently focused via the keyboard.

But because the components are headless and completely unstyled out of the box, you can't see this information in your UI until you provide the styles you want for each state yourself.

The easiest way to style the different states of a Headless UI component is using the data-* attributes that each component exposes.

For example, the Input component exposes a data-focus attribute, which tells you if the input is currently focused via the mouse or keyboard, and a data-hover attribute, which tells you if the input is currently being hovered by the mouse.

Use the CSS attribute selector to conditionally apply styles based on the presence of these data attributes. If you're using Tailwind CSS, the data attribute modifier makes this easy:

See the component API for a list of all the available data attributes.

Each component also exposes information about its current state via render props that you can use to conditionally apply different styles or render different content.

For example, the Input component exposes a focus state, which tells you if the input is currently focused via the mouse or keyboard, and a hover state, which tells you if the input is currently being hovered by the mouse.

See the component API for a list of all the available render props.

Wrap a Label and Input with the Field component to automatically associate them using a generated ID:

Use the Description component within a Field to automatically associa

*[Content truncated - see full docs]*

**Examples**:

```shell
npm install @headlessui/react
```

```jsx
import { Input } from '@headlessui/react'

function Example() {
  return <Input name="full_name" type="text" />
}
```

```html
<!-- Rendered `Input` -->
<input type="text" name="full_name" data-focus data-hover />
```

---

## Select - Headless UI

**URL**: https://headlessui.com/react/select

**Contents**:
- Components
  - Forms
- Select
- Installation
- Basic example
- Styling
  - Using data attributes
  - Using render props

A light wrapper around the native select element that handles tedious accessibility concerns and provides more opinionated states for things like hover and focus.

To get started, install Headless UI via npm:

Select controls are built using the Select component:

You can pass any props to a Select that you'd normally pass to the native select element.

Headless UI keeps track of a lot of state about each component, like whether or not a select is focused, whether a popover is open or closed, or which item in a menu is currently focused via the keyboard.

But because the components are headless and completely unstyled out of the box, you can't see this information in your UI until you provide the styles you want for each state yourself.

The easiest way to style the different states of a Headless UI component is using the data-* attributes that each component exposes.

For example, the Select component exposes a data-focus attribute, which tells you if the select is currently focused via keyboard, and a data-hover attribute, which tells you if the select is currently being hovered by the mouse.

Use the CSS attribute selector to conditionally apply styles based on the presence of these data attributes. If you're using Tailwind CSS, the data attribute modifier makes this easy:

See the component API for a list of all the available data attributes.

Each component also exposes information about its current state via render props that you can use to conditionally apply different styles or render different content.

For example, the Select component exposes a focus state, which tells you if the select is currently focused via the keyboard, and a hover state, which tells you if the select is currently being hovered by the mouse.

See the component API for a list of all the available render props.

Wrap a Label and Select with the Field component to automatically associate them using a generated ID:

Use the Description component within a Field to automatically associate 

*[Content truncated - see full docs]*

**Examples**:

```shell
npm install @headlessui/react
```

```jsx
import { Select } from '@headlessui/react'

function Example() {
  return (
    <Select name="status" aria-label="Project status">
      <option value="active">Active</option>
      <option value="paused">Paused</option>
      <option value="delayed">Delayed</option>
      <option value="canceled">Canceled</option>
    </Select>
  )
}
```

```html
<!-- Rendered `Select` -->
<select name="status" data-focus data-hover>
  <option value="active">Active</option>
  <option value="paused">Paused</option>
  <option value="delayed">Delayed</option>
  <option value="canceled">Canceled</option>
</select>
```

---

## Textarea - Headless UI

**URL**: https://headlessui.com/react/textarea

**Contents**:
- Components
  - Forms
- Textarea
- Installation
- Basic example
- Styling
  - Using data attributes
  - Using render props

A light wrapper around the native textarea element that handles tedious accessibility concerns and provides more opinionated states for things like hover and focus.

To get started, install Headless UI via npm:

Textareas are built using the Textarea component:

You can pass any props to a Textarea that you'd normally pass to the native textarea element.

Headless UI keeps track of a lot of state about each component, like whether or not a textarea is focused, whether a popover is open or closed, or which item in a menu is currently focused via the keyboard.

But because the components are headless and completely unstyled out of the box, you can't see this information in your UI until you provide the styles you want for each state yourself.

The easiest way to style the different states of a Headless UI component is using the data-* attributes that each component exposes.

For example, the Textarea component exposes a data-focus attribute, which tells you if the textarea is currently focused via the mouse or keyboard, and a data-hover attribute, which tells you if the textarea is currently being hovered by the mouse.

Use the CSS attribute selector to conditionally apply styles based on the presence of these data attributes. If you're using Tailwind CSS, the data attribute modifier makes this easy:

See the component API for a list of all the available data attributes.

Each component also exposes information about its current state via render props that you can use to conditionally apply different styles or render different content.

For example, the Textarea component exposes a focus state, which tells you if the textarea is currently focused via the mouse or keyboard, and a hover state, which tells you if the textarea is currently being hovered by the mouse.

See the component API for a list of all the available render props.

Wrap a Label and Textarea with the Field component to automatically associate them using a generated ID:

Use the Description component wi

*[Content truncated - see full docs]*

**Examples**:

```shell
npm install @headlessui/react
```

```jsx
import { Textarea } from '@headlessui/react'

function Example() {
  return <Textarea name="description"></Textarea>
}
```

```html
<!-- Rendered `Textarea` -->
<textarea name="description" data-focus data-hover></textarea>
```

---
