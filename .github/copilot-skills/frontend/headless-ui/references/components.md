# Headless-Ui - Components

**Pages**: 21

---

## Button - Headless UI

**URL**: https://headlessui.com/react/button

**Contents**:
- Components
  - Forms
- Button
- Installation
- Basic example
- Styling
  - Using data attributes
  - Using render props

A light wrapper around the native button element that provides more opinionated states for things like hover and focus.

To get started, install Headless UI via npm:

Buttons are built using the Button component:

You can pass any props to a Button that you'd normally pass to the native button element.

Headless UI keeps track of a lot of state about each component, like whether or not an input is focused, whether a popover is open or closed, or which item in a menu is currently focused via the keyboard.

But because the components are headless and completely unstyled out of the box, you can't see this information in your UI until you provide the styles you want for each state yourself.

The easiest way to style the different states of a Headless UI component is using the data-* attributes that each component exposes.

For example, the Button component exposes a data-hover attribute, which tells you if the button is currently being hovered by the mouse, and a data-active attribute, which tells you if the button is currently being pressed.

Use the CSS attribute selector to conditionally apply styles based on the presence of these data attributes. If you're using Tailwind CSS, the data attribute modifier makes this easy:

See the component API for a list of all the available data attributes.

Each component also exposes information about its current state via render props that you can use to conditionally apply different styles or render different content.

For example, the Button component exposes a hover state, which tells you if the button is currently being hovered by the mouse, and an active state, which tells you if the button is currently being pressed.

See the component API for a list of all the available render props.

Add the disabled prop to a Button to disable it:

A thin wrapper around the native button element.

The element or component the button should render as.

Whether or not the button is disabled.

Whether or not the button should receive focus 

*[Content truncated - see full docs]*

**Examples**:

```shell
npm install @headlessui/react
```

```jsx
import { Button } from '@headlessui/react'

function Example() {
  return (
    <Button className="rounded bg-sky-600 px-4 py-2 text-sm text-white data-active:bg-sky-700 data-hover:bg-sky-500">
      Save changes
    </Button>
  )
}
```

```html
<!-- Rendered `Button` -->
<button type="button" data-hover data-active></button>
```

---

## Combobox (Autocomplete) - Headless UI

**URL**: https://headlessui.com/v1/vue/combobox

**Contents**:
- Combobox (Autocomplete)
- Installation
- Basic example
- Styling different states
  - Using slots
  - Using data attributes
- Binding objects as values
- Selecting multiple values

Comboboxes are the foundation of accessible autocompletes and command palettes for your app, complete with robust support for keyboard navigation.

To get started, install Headless UI via npm.

Please note that this library only supports Vue 3.

Comboboxes are built using the Combobox, ComboboxInput, ComboboxButton, ComboboxOptions, ComboboxOption and ComboboxLabel components.

The ComboboxInput will automatically open/close the ComboboxOptions when searching.

You are completely in charge of how you filter the results, whether it be with a fuzzy search library client-side or by making server-side requests to an API. In this example we will keep the logic simple for demo purposes.

In the previous example we used a list of string values as data, but you can also use objects with additional information. The only caveat is that you have to provide a displayValue to the input. This is important so that a string based version of your object can be rendered in the ComboboxInput.

Headless UI keeps track of a lot of state about each component, like which combobox option is currently selected, whether a popover is open or closed, or which item in a combobox is currently active via the keyboard.

But because the components are headless and completely unstyled out of the box, you can't see this information in your UI until you provide the styles you want for each state yourself.

Each component exposes information about its current state via slot props that you can use to conditionally apply different styles or render different content.

For example, the ComboboxOption component exposes an active state, which tells you if the item is currently focused via the mouse or keyboard.

For a complete list of all the available slot props, see the component API documentation.

Each component also exposes information about its current state via a data-headlessui-state attribute that you can use to conditionally apply different styles.

When any of the states in the slot prop API are t

*[Content truncated - see full docs]*

**Examples**:

```
npm install @headlessui/vue
```

```
<template>
  <Combobox v-model="selectedPerson">
    <ComboboxInput @change="query = $event.target.value" />
    <ComboboxOptions>
      <ComboboxOption
        v-for="person in filteredPeople"
        :key="person"
        :value="person"
      >
        {{ person }}
      </ComboboxOption>
    </ComboboxOptions>
  </Combobox>
</template>

<script setup>
  import { ref, computed } from 'vue'
  import {
    Combobox,
    ComboboxInput,
    ComboboxOptions,
    ComboboxOption,
  } from '@headless
...
```

```
<template>
  <Combobox v-model="selectedPerson">
    <ComboboxInput
      @change="query = $event.target.value"
      :displayValue="(person) => person.name"    />
    <ComboboxOptions>
      <ComboboxOption
        v-for="person in filteredPeople"
        :key="person.id"
        :value="person"
        :disabled="person.unavailable"
      >
        {{ person.name }}
      </ComboboxOption>
    </ComboboxOptions>
  </Combobox>
</template>

<script setup>
  import { ref, computed } from 'vue'
  
...
```

---

## Combobox - Headless UI

**URL**: https://headlessui.com/react/combobox

**Contents**:
- Components
  - Forms
- Combobox
- Installation
- Basic example
- Styling
  - Using data attributes
  - Using render props

Comboboxes are the foundation of accessible autocompletes and command palettes for your app, complete with robust support for keyboard navigation.

To get started, install Headless UI via npm:

Comboboxes are built using the Combobox, ComboboxInput, ComboboxButton, ComboboxOptions, and ComboboxOption components.

You are completely in charge of how you filter the results, whether it be with a fuzzy search library client-side or by making server-side requests to an API. In this example we will keep the logic simple for demo purposes.

Headless UI keeps track of a lot of state about each component, like which combobox option is currently selected, whether a popover is open or closed, or which item in a menu is currently focused via the keyboard.

But because the components are headless and completely unstyled out of the box, you can't see this information in your UI until you provide the styles you want for each state yourself.

The easiest way to style the different states of a Headless UI component is using the data-* attributes that each component exposes.

For example, the ComboboxOption component exposes a data-focus attribute, which tells you if the option is currently focused via the mouse or keyboard, and a data-selected attribute, which tells you if that option matches the current value of the Combobox.

Use the CSS attribute selector to conditionally apply styles based on the presence of these data attributes. If you're using Tailwind CSS, the data attribute modifier makes this easy:

See the component API for a list of all the available data attributes.

Each component also exposes information about its current state via render props that you can use to conditionally apply different styles or render different content.

For example, the ComboboxOption component exposes a focus state, which tells you if the option is currently focused via the mouse or keyboard, and a selected state, which tells you if that option matches the current value of the Combobox.

Se

*[Content truncated - see full docs]*

**Examples**:

```shell
npm install @headlessui/react
```

```jsx
import { Combobox, ComboboxInput, ComboboxOption, ComboboxOptions } from '@headlessui/react'
import { useState } from 'react'

const people = [
  { id: 1, name: 'Durward Reynolds' },
  { id: 2, name: 'Kenton Towne' },
  { id: 3, name: 'Therese Wunsch' },
  { id: 4, name: 'Benedict Kessler' },
  { id: 5, name: 'Katelyn Rohan' },
]

function Example() {
  const [selectedPerson, setSelectedPerson] = useState(people[0])
  const [query, setQuery] = useState('')

  const filteredPeople =
    query ===
...
```

```html
<!-- Rendered `ComboboxOptions` -->
<div data-open>
  <div>Wade Cooper</div>
  <div data-focus data-selected>Arlene Mccoy</div>
  <div>Devon Webb</div>
</div>
```

---

## Dialog - Headless UI

**URL**: https://headlessui.com/react/dialog

**Contents**:
- Components
  - Forms
- Dialog
- Installation
- Basic example
- Styling
- Examples
  - Showing/hiding the dialog

A fully-managed, renderless dialog component jam-packed with accessibility and keyboard features, perfect for building completely custom dialogs and alerts.

To get started, install Headless UI via npm:

Dialogs are built using the Dialog, DialogPanel, DialogTitle, and Description components:

How you open and close the dialog is entirely up to you. You open a dialog by passing true to the open prop, and close it by passing false. An onClose callback is also required for when the dialog is dismissed by pressing the Esc key or by clicking outside of the DialogPanel.

Style the Dialog and DialogPanel components using the className or style props like you would with any other element. You can also introduce additional elements if needed to achieve a particular design.

Clicking outside the DialogPanel component will close the dialog, so keep that in mind when deciding which styles to apply to which elements.

Dialogs are controlled components, meaning that you have to provide and manage the open state yourself using the open prop and the onClose callback.

The onClose callback is called when an dialog is dismissed, which happens when the user presses the Esc key or clicks outside the DialogPanel. In this callback set the open state back to false to close the dialog.

For situations where you don't have easy access to your open/close state, Headless UI provides a CloseButton component that will close the nearest dialog ancestor when clicked. You can use the as prop to customize which element is being rendered:

If you require more control, you can also use the useClose hook to imperatively close the dialog, say after running an async action:

The useClose hook must be used in a component that's nested within the Dialog, otherwise it will not work.

Use the DialogBackdrop component to add a backdrop behind your dialog panel. We recommend making the backdrop a sibling to your panel container:

This lets you transition the backdrop and panel independently with their own an

*[Content truncated - see full docs]*

**Examples**:

```shell
npm install @headlessui/react
```

```jsx
import { Description, Dialog, DialogPanel, DialogTitle } from '@headlessui/react'
import { useState } from 'react'

function Example() {
  let [isOpen, setIsOpen] = useState(false)

  return (
    <>
      <button onClick={() => setIsOpen(true)}>Open dialog</button>
      <Dialog open={isOpen} onClose={() => setIsOpen(false)} className="relative z-50">
        <div className="fixed inset-0 flex w-screen items-center justify-center p-4">
          <DialogPanel className="max-w-lg space-y-4 border
...
```

```jsx
import { Dialog, DialogPanel, DialogTitle } from '@headlessui/react'
import { useState } from 'react'

function Example() {
  let [isOpen, setIsOpen] = useState(true)

  return (
    <Dialog open={isOpen} onClose={() => setIsOpen(false)} className="relative z-50">      <div className="fixed inset-0 flex w-screen items-center justify-center p-4">        <DialogPanel className="max-w-lg space-y-4 border bg-white p-12">          <DialogTitle>Deactivate account order</DialogTitle>

          {/* ...
...
```

---

## Dialog (Modal) - Headless UI

**URL**: https://headlessui.com/v1/vue/dialog

**Contents**:
- Dialog (Modal)
- Installation
- Basic example
- Showing and hiding your dialog
- Styling the dialog
- Adding a backdrop
- Scrollable dialogs
- Managing initial focus

A fully-managed, renderless dialog component jam-packed with accessibility and keyboard features, perfect for building completely custom modal and dialog windows for your next application.

To get started, install Headless UI via npm.

Please note that this library only supports Vue 3.

Dialogs are built using the Dialog, DialogPanel, DialogTitle and DialogDescription components.

When the dialog's open prop is true, the contents of the dialog will render. Focus will be moved inside the dialog and trapped there as the user cycles through the focusable elements. Scroll is locked, the rest of your application UI is hidden from screen readers, and clicking outside the DialogPanel or pressing the Escape key will fire the close event and close the dialog.

If your dialog has a title and description, use the DialogTitle and DialogDescription components to provide the most accessible experience. This will link your title and description to the root dialog component via the aria-labelledby and aria-describedby attributes, ensuring their contents are announced to users using screenreaders when your dialog opens.

Dialogs have no automatic management of their open/closed state. To show and hide your dialog, pass a ref into the open prop. When open is true the dialog will render, and when it's false the dialog will unmount.

The close event fires when an open dialog is dismissed, which happens when the user clicks outside your DialogPanel or presses the Escape key. You can use this event to set open back to false and close your dialog.

Style the Dialog and DialogPanel components using the class or style props like you would with any other element. You can also introduce additional elements if needed to achieve a particular design.

Clicking outside the DialogPanel component will close the dialog, so keep that in mind when deciding which element should receive a given style.

If you'd like to add an overlay or backdrop behind your DialogPanel to bring attention to the panel it

*[Content truncated - see full docs]*

**Examples**:

```
npm install @headlessui/vue
```

```
<template>
  <Dialog :open="isOpen" @close="setIsOpen">
    <DialogPanel>
      <DialogTitle>Deactivate account</DialogTitle>
      <DialogDescription>
        This will permanently deactivate your account
      </DialogDescription>

      <p>
        Are you sure you want to deactivate your account? All of your data will be
        permanently removed. This action cannot be undone.
      </p>

      <button @click="setIsOpen(false)">Deactivate</button>
      <button @click="setIsOpen(false)">Ca
...
```

```
<template>
  <!--
    Pass the `isOpen` ref to the `open` prop, and use the `close` event
    to set the ref back to `false` when the user clicks outside of
    the dialog or presses the escape key.
  -->
  <Dialog :open="isOpen" @close="setIsOpen">    <DialogPanel>
      <DialogTitle>Deactivate account</DialogTitle>
      <DialogDescription>
        This will permanently deactivate your account
      </DialogDescription>

      <p>
        Are you sure you want to deactivate your account? All o
...
```

---

## Disclosure - Headless UI

**URL**: https://headlessui.com/react/disclosure

**Contents**:
- Components
  - Forms
- Disclosure
- Installation
- Basic example
- Styling
  - Using data attributes
  - Using render props

A simple, accessible foundation for building custom UIs that show and hide content, like togglable accordion panels.

To get started, install Headless UI via npm:

Disclosures are built using the Disclosure, DisclosureButton, and DisclosurePanel components.

The button will automatically open/close the panel when clicked, and all components will receive the appropriate aria-* related attributes like aria-expanded and aria-controls.

Headless UI keeps track of a lot of state about each component, like which listbox option is currently selected, whether a popover is open or closed, or which item in a disclosure is currently focused via the keyboard.

But because the components are headless and completely unstyled out of the box, you can't see this information in your UI until you provide the styles you want for each state yourself.

The easiest way to style the different states of a Headless UI component is using the data-* attributes that each component exposes.

For example, the DisclosureButton component exposes a data-open attribute, which tells you if the disclosure is currently open.

Use the CSS attribute selector to conditionally apply styles based on the presence of these data attributes. If you're using Tailwind CSS, the data attribute modifier makes this easy:

See the component API for a list of all the available data attributes.

Each component also exposes information about its current state via render props that you can use to conditionally apply different styles or render different content.

For example, the DisclosureButton component exposes an open state, which tells you if the disclosure is currently open.

See the component API for a list of all the available render props.

To animate the opening and closing of the disclosure panel, add the transition prop to the DisclosurePanel component and then use CSS to style the different stages of the transition:

Internally, the transition prop is implemented in the exact same way as the Transition componen

*[Content truncated - see full docs]*

**Examples**:

```shell
npm install @headlessui/react
```

```jsx
import { Disclosure, DisclosureButton, DisclosurePanel } from '@headlessui/react'

function Example() {
  return (
    <Disclosure>
      <DisclosureButton className="py-2">Is team pricing available?</DisclosureButton>
      <DisclosurePanel className="text-gray-500">
        Yes! You can purchase a license that you can share with your entire team.
      </DisclosurePanel>
    </Disclosure>
  )
}
```

```html
<!-- Rendered `Disclosure` -->
<button data-open>Do you offer technical support?</button>
<div data-open>No</div>
```

---

## Disclosure - Headless UI

**URL**: https://headlessui.com/v1/vue/disclosure

**Contents**:
- Disclosure
- Installation
- Basic example
- Styling different states
  - Using slots
  - Using data attributes
- Showing/hiding the panel
- Closing disclosures manually

A simple, accessible foundation for building custom UIs that show and hide content, like togglable accordion panels.

To get started, install Headless UI via npm.

Please note that this library only supports Vue 3.

Disclosures are built using the Disclosure, DisclosureButton and DisclosurePanel components.

The button will automatically open/close the panel when clicked, and all components will receive the appropriate aria-* related attributes like aria-expanded and aria-controls.

Headless UI keeps track of a lot of state about each component, like which listbox option is currently selected, whether a popover is open or closed, or which item in a disclosure is currently active via the keyboard.

But because the components are headless and completely unstyled out of the box, you can't see this information in your UI until you provide the styles you want for each state yourself.

Each component exposes information about its current state via slot props that you can use to conditionally apply different styles or render different content.

For example, the Disclosure component exposes an open state, which tells you if the disclosure is currently open.

For a complete list of all the available slot props, see the component API documentation.

Each component also exposes information about its current state via a data-headlessui-state attribute that you can use to conditionally apply different styles.

When any of the states in the slot prop API are true, they will be listed in this attribute as space-separated strings so you can target them with a CSS attribute selector in the form [attr~=value].

For example, here's what the Disclosure component renders when the disclosure is open:

If you are using Tailwind CSS, you can use the @headlessui/tailwindcss plugin to target this attribute with modifiers like ui-open:*:

By default, your DisclosurePanel will be shown/hidden automatically based on the internal open state tracked within the Disclosure component itself.

If you

*[Content truncated - see full docs]*

**Examples**:

```
npm install @headlessui/vue
```

```
<template>
  <Disclosure>
    <DisclosureButton class="py-2">
      Is team pricing available?
    </DisclosureButton>
    <DisclosurePanel class="text-gray-500">
      Yes! You can purchase a license that you can share with your entire team.
    </DisclosurePanel>
  </Disclosure>
</template>

<script setup>
  import {
    Disclosure,
    DisclosureButton,
    DisclosurePanel,
  } from '@headlessui/vue'
</script>
```

```
<template>
  <Disclosure v-slot="{ open }">    <!-- Use the `open` state to conditionally change the direction of an icon. -->
    <DisclosureButton class="py-2">
      <span>Do you offer technical support?</span>
      <ChevronRightIcon :class="open && 'rotate-90 transform'" />    </DisclosureButton>
    <DisclosurePanel>No</DisclosurePanel>
  </Disclosure>
</template>

<script setup>
  import {
    Disclosure,
    DisclosureButton,
    DisclosurePanel,
  } from '@headlessui/vue'
  import { Che
...
```

---

## Dropdown Menu - Headless UI

**URL**: https://headlessui.com/react/menu

**Contents**:
- Components
  - Forms
- Dropdown Menu
- Installation
- Basic example
- Styling
  - Using data attributes
  - Using render props

Menus offer an easy way to build custom, accessible dropdown components with robust support for keyboard navigation.

To get started, install Headless UI via npm:

Menus are built using the Menu, MenuButton, MenuItems, and MenuItem components:

The MenuButton will automatically open and close the MenuItems when clicked, and when the menu is opened the list of items receives focus and is navigable via the keyboard.

Headless UI keeps track of a lot of state about each component, like which menu item is currently focused via the keyboard, whether a popover is open or closed, or which listbox option is currently selected.

But because the components are headless and completely unstyled out of the box, you can't see this information in your UI until you provide the styles you want for each state yourself.

The easiest way to style the different states of a Headless UI component is using the data-* attributes that each component exposes.

For example, the MenuButton component exposes a data-active attribute, which tells you if the menu is currently open, and the MenuItem component exposes a data-focus attribute, which tells you if the menu item is currently focused via the mouse or keyboard.

Use the CSS attribute selector to conditionally apply styles based on the presence of these data attributes. If you're using Tailwind CSS, the data attribute modifier makes this easy:

See the component API for a list of all the available data attributes.

Each component also exposes information about its current state via render props that you can use to conditionally apply different styles or render different content.

For example, the MenuButton component exposes an active state, which tells you if the menu is currently open, and the MenuItem component exposes a focus state, which tells you if the menu item is currently focused via the mouse or keyboard.

See the component API for a list of all the available render props.

In addition to links, you can also use buttons in a MenuI

*[Content truncated - see full docs]*

**Examples**:

```shell
npm install @headlessui/react
```

```jsx
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/react'

function Example() {
  return (
    <Menu>
      <MenuButton>My account</MenuButton>
      <MenuItems anchor="bottom">
        <MenuItem>
          <a className="block data-focus:bg-blue-100" href="/settings">
            Settings
          </a>
        </MenuItem>
        <MenuItem>
          <a className="block data-focus:bg-blue-100" href="/support">
            Support
          </a>
        </MenuItem>
        <MenuI
...
```

```html
<!-- Rendered `MenuButton`, `MenuItems`, and `MenuItem` -->
<button data-active>Options</button>
<div data-open>
  <a href="/settings">Settings</a>
  <a href="/support" data-focus>Support</a>
  <a href="/license">License</a>
</div>
```

---

## Listbox - Headless UI

**URL**: https://headlessui.com/react/listbox

**Contents**:
- Components
  - Forms
- Listbox
- Installation
- Basic example
- Styling
  - Using data attributes
  - Using render props

Listboxes are a great foundation for building custom, accessible select menus for your app, complete with robust support for keyboard navigation.

To get started, install Headless UI via npm:

Listboxes are built using the Listbox, ListboxButton, ListboxSelectedOption, ListboxOptions, and ListboxOption components.

The ListboxButton will automatically open/close the ListboxOptions when clicked, and when the listbox is open, the list of options receives focus and is automatically navigable via the keyboard.

Headless UI keeps track of a lot of state about each component, like which listbox option is currently selected, whether a popover is open or closed, or which item in a menu is currently focused via the keyboard.

But because the components are headless and completely unstyled out of the box, you can't see this information in your UI until you provide the styles you want for each state yourself.

The easiest way to style the different states of a Headless UI component is using the data-* attributes that each component exposes.

For example, the ListboxOption component exposes a data-focus attribute, which tells you if the option is currently focused via the mouse or keyboard, and a data-selected attribute, which tells you if that option matches the current value of the Listbox.

Use the CSS attribute selector to conditionally apply styles based on the presence of these data attributes. If you're using Tailwind CSS, the data attribute modifier makes this easy:

See the component API for a list of all the available data attributes.

Each component also exposes information about its current state via render props that you can use to conditionally apply different styles or render different content.

For example, the ListboxOption component exposes a focus state, which tells you if the option is currently focused via the mouse or keyboard, and a selected state, which tells you if that option matches the current value of the Listbox.

See the component API for a list o

*[Content truncated - see full docs]*

**Examples**:

```shell
npm install @headlessui/react
```

```jsx
import { Listbox, ListboxButton, ListboxOption, ListboxOptions } from '@headlessui/react'
import { useState } from 'react'

const people = [
  { id: 1, name: 'Durward Reynolds' },
  { id: 2, name: 'Kenton Towne' },
  { id: 3, name: 'Therese Wunsch' },
  { id: 4, name: 'Benedict Kessler' },
  { id: 5, name: 'Katelyn Rohan' },
]

function Example() {
  const [selectedPerson, setSelectedPerson] = useState(people[0])

  return (
    <Listbox value={selectedPerson} onChange={setSelectedPerson}>
     
...
```

```html
<!-- Rendered `ListboxOption` -->
<div data-focus data-selected>Arlene Mccoy</div>
```

---

## Listbox (Select) - Headless UI

**URL**: https://headlessui.com/v1/vue/listbox

**Contents**:
- Listbox (Select)
- Installation
- Basic example
- Styling different states
  - Using slots
  - Using data attributes
- Binding objects as values
- Selecting multiple values

Listboxes are a great foundation for building custom, accessible select menus for your app, complete with robust support for keyboard navigation.

To get started, install Headless UI via npm.

Please note that this library only supports Vue 3.

Listboxes are built using the Listbox, ListboxButton, ListboxOptions, ListboxOption and ListboxLabel components.

The ListboxButton will automatically open/close the ListboxOptions when clicked, and when the menu is open, the list of items receives focus and is automatically navigable via the keyboard.

Headless UI keeps track of a lot of state about each component, like which listbox option is currently selected, whether a popover is open or closed, or which item in a listbox is currently active via the keyboard.

But because the components are headless and completely unstyled out of the box, you can't see this information in your UI until you provide the styles you want for each state yourself.

Each component exposes information about its current state via slot props that you can use to conditionally apply different styles or render different content.

For example, the ListboxOption component exposes an active state, which tells you if the item is currently focused via the mouse or keyboard.

For a complete list of all the available slot props, see the component API documentation.

Each component also exposes information about its current state via a data-headlessui-state attribute that you can use to conditionally apply different styles.

When any of the states in the slot prop API are true, they will be listed in this attribute as space-separated strings so you can target them with a CSS attribute selector in the form [attr~=value].

For example, here's what the ListboxOptions component with some child ListboxOption components renders when the listbox is open and the second item is active:

If you are using Tailwind CSS, you can use the @headlessui/tailwindcss plugin to target this attribute with modifiers like ui-open:*

*[Content truncated - see full docs]*

**Examples**:

```
npm install @headlessui/vue
```

```
<template>
  <Listbox v-model="selectedPerson">
    <ListboxButton>{{ selectedPerson.name }}</ListboxButton>
    <ListboxOptions>
      <ListboxOption
        v-for="person in people"
        :key="person.id"
        :value="person"
        :disabled="person.unavailable"
      >
        {{ person.name }}
      </ListboxOption>
    </ListboxOptions>
  </Listbox>
</template>

<script setup>
  import { ref } from 'vue'
  import {
    Listbox,
    ListboxButton,
    ListboxOptions,
    ListboxOption
...
```

```
<template>
  <Listbox v-model="selectedPerson">
    <ListboxButton>{{ selectedPerson.name }}</ListboxButton>
    <ListboxOptions>
      <!-- Use the `active` state to conditionally style the active option. -->
      <!-- Use the `selected` state to conditionally style the selected option. -->
      <ListboxOption
        v-for="person in people"
        :key="person.id"
        :value="person"
        as="template"
        v-slot="{ active, selected }"      >
        <li
          :class="{
    
...
```

---

## Menu (Dropdown) - Headless UI

**URL**: https://headlessui.com/v1/vue/menu

**Contents**:
- Menu (Dropdown)
- Installation
- Basic example
- Styling different states
  - Using slots
  - Using data attributes
- Showing/hiding the menu
- Closing menus manually

Menus offer an easy way to build custom, accessible dropdown components with robust support for keyboard navigation.

To get started, install Headless UI via npm.

Please note that this library only supports Vue 3.

Menu Buttons are built using the Menu, MenuButton, MenuItems, and MenuItem components.

The MenuButton will automatically open/close the MenuItems when clicked, and when the menu is open, the list of items receives focus and is automatically navigable via the keyboard.

Headless UI keeps track of a lot of state about each component, like which listbox option is currently selected, whether a popover is open or closed, or which item in a menu is currently active via the keyboard.

But because the components are headless and completely unstyled out of the box, you can't see this information in your UI until you provide the styles you want for each state yourself.

Each component exposes information about its current state via slot props that you can use to conditionally apply different styles or render different content.

For example, the MenuItem component exposes an active state, which tells you if the item is currently focused via the mouse or keyboard.

For a complete list of all the available slot props, see the component API documentation.

Each component also exposes information about its current state via a data-headlessui-state attribute that you can use to conditionally apply different styles.

When any of the states in the slot prop API are true, they will be listed in this attribute as space-separated strings so you can target them with a CSS attribute selector in the form [attr~=value].

For example, here's what the MenuItems component with some child MenuItem components renders when the menu is open and the second item is active:

If you are using Tailwind CSS, you can use the @headlessui/tailwindcss plugin to target this attribute with modifiers like ui-open:* and ui-active:*:

By default, your MenuItems instance will be shown/hidden automati

*[Content truncated - see full docs]*

**Examples**:

```
npm install @headlessui/vue
```

```
<template>
  <Menu>
    <MenuButton>More</MenuButton>
    <MenuItems>
      <MenuItem v-slot="{ active }">
        <a :class='{ "bg-blue-500": active }' href="/account-settings">
          Account settings
        </a>
      </MenuItem>
      <MenuItem v-slot="{ active }">
        <a :class='{ "bg-blue-500": active }' href="/account-settings">
          Documentation
        </a>
      </MenuItem>
      <MenuItem disabled>
        <span class="opacity-75">Invite a friend (coming soon!)</span>
  
...
```

```
<template>
  <Menu>
    <MenuButton>Options</MenuButton>
    <MenuItems>
      <!-- Use the `active` state to conditionally style the active item. -->
      <MenuItem
        v-for="link in links"
        :key="link.href"
        as="template"
        v-slot="{ active }"      >
        <a
          :href="link.href"
          :class="{ 'bg-blue-500 text-white': active, 'bg-white text-black': !active }"        >
          {{ link.label }}
        </a>
      </MenuItem>
    </MenuItems>
  </Menu>

...
```

---

## Popover - Headless UI

**URL**: https://headlessui.com/v1/vue/popover

**Contents**:
- Popover
- Installation
- Basic example
- Styling different states
  - Using slots
  - Using data attributes
- Showing/hiding the popover
- Closing popovers manually

Popovers are perfect for floating panels with arbitrary content like navigation menus, mobile menus and flyout menus.

To get started, install Headless UI via npm.

Please note that this library only supports Vue 3.

Popovers are built using the Popover, PopoverButton, and PopoverPanel components.

Clicking the PopoverButton will automatically open/close the PopoverPanel. When the panel is open, clicking anywhere outside of its contents, pressing the Escape key, or tabbing away from it will close the Popover.

These components are completely unstyled, so how you style your Popover is up to you. In our example we're using absolute positioning on the PopoverPanel to position it near the PopoverButton and not disturb the normal document flow.

Headless UI keeps track of a lot of state about each component, like which listbox option is currently selected, whether a popover is open or closed, or which item in a popover is currently active via the keyboard.

But because the components are headless and completely unstyled out of the box, you can't see this information in your UI until you provide the styles you want for each state yourself.

Each component exposes information about its current state via slot props that you can use to conditionally apply different styles or render different content.

For example, the Popover component exposes an open state, which tells you if the popover is currently open.

For a complete list of all the available slot props, see the component API documentation.

Each component also exposes information about its current state via a data-headlessui-state attribute that you can use to conditionally apply different styles.

When any of the states in the slot prop API are true, they will be listed in this attribute as space-separated strings so you can target them with a CSS attribute selector in the form [attr~=value].

For example, here's what the Popover component renders when the popover is open:

If you are using Tailwind CSS, you can use 

*[Content truncated - see full docs]*

**Examples**:

```
npm install @headlessui/vue
```

```
<template>
  <Popover class="relative">
    <PopoverButton>Solutions</PopoverButton>

    <PopoverPanel class="absolute z-10">
      <div class="grid grid-cols-2">
        <a href="/analytics">Analytics</a>
        <a href="/engagement">Engagement</a>
        <a href="/security">Security</a>
        <a href="/integrations">Integrations</a>
      </div>

      <img src="/solutions.jpg" alt="" />
    </PopoverPanel>
  </Popover>
</template>

<script setup>
  import { Popover, PopoverButton, Popove
...
```

```
<template>
  <Popover v-slot="{ open }">    <!-- Use the `open` state to conditionally change the direction of the chevron icon. -->
    <PopoverButton>
      Solutions
      <ChevronDownIcon :class="{ 'rotate-180 transform': open }" />    </PopoverButton>

    <PopoverPanel>
      <a href="/insights">Insights</a>
      <a href="/automations">Automations</a>
      <a href="/reports">Reports</a>
    </PopoverPanel>
  </Popover>
</template>

<script setup>
  import { Popover, PopoverButton, Popove
...
```

---

## Popover - Headless UI

**URL**: https://headlessui.com/react/popover

**Contents**:
- Components
  - Forms
- Popover
- Installation
- Basic example
- Styling
  - Using data attributes
  - Using render props

Popovers are perfect for floating panels with arbitrary content like navigation menus, mobile menus and flyout menus.

To get started, install Headless UI via npm:

Popovers are built using the Popover, PopoverButton, and PopoverPanel components.

Clicking the PopoverButton will automatically open/close the PopoverPanel. When the panel is open, clicking anywhere outside of its contents, pressing the Escape key, or tabbing away from it will close the popover.

Headless UI keeps track of a lot of state about each component, like which listbox option is currently selected, whether a popover is open or closed, or which item in a popover is currently focused via the keyboard.

But because the components are headless and completely unstyled out of the box, you can't see this information in your UI until you provide the styles you want for each state yourself.

The easiest way to style the different states of a Headless UI component is using the data-* attributes that each component exposes.

For example, the Popover component exposes a data-open attribute, which tells you if the popover is currently open.

Use the CSS attribute selector to conditionally apply styles based on the presence of these data attributes. If you're using Tailwind CSS, the data attribute modifier makes this easy:

See the component API for a list of all the available data attributes.

Each component also exposes information about its current state via render props that you can use to conditionally apply different styles or render different content.

For example, the Popover component exposes an open state, which tells you if the popover is currently open.

See the component API for a list of all the available render props.

When rendering several related popovers, for example in a site's header navigation, use the PopoverGroup component. This ensures panels stay open while users are tabbing between popovers within a group, but closes any open panel once the user tabs outside of the group:

The Popo

*[Content truncated - see full docs]*

**Examples**:

```shell
npm install @headlessui/react
```

```jsx
import { Popover, PopoverButton, PopoverPanel } from '@headlessui/react'

function Example() {
  return (
    <Popover className="relative">
      <PopoverButton>Solutions</PopoverButton>
      <PopoverPanel anchor="bottom" className="flex flex-col">
        <a href="/analytics">Analytics</a>
        <a href="/engagement">Engagement</a>
        <a href="/security">Security</a>
        <a href="/integrations">Integrations</a>
      </PopoverPanel>
    </Popover>
  )
}
```

```html
<!-- Rendered `Popover` -->
<div data-open>
  <button data-open>Solutions</button>
  <div data-open>
    <a href="/insights">Insights</a>
    <a href="/automations">Automations</a>
    <a href="/reports">Reports</a>
  </div>
</div>
```

---

## Radio Group - Headless UI

**URL**: https://headlessui.com/react/radio-group

**Contents**:
- Components
  - Forms
- Radio Group
- Installation
- Basic example
- Styling
  - Using data attributes
  - Using render props

Radio groups give you the same functionality as native HTML radio inputs, without any of the styling. They're perfect for building out custom UIs for selectors.

To get started, install Headless UI via npm:

Radio groups are built using the RadioGroup, Radio, Field, and Label components.

Headless UI keeps track of a lot of state about each component, like which radio group option is currently checked, whether a popover is open or closed, or which item in a menu is currently focused via the keyboard.

But because the components are headless and completely unstyled out of the box, you can't see this information in your UI until you provide the styles you want for each state yourself.

The easiest way to style the different states of a Headless UI component is using the data-* attributes that each component exposes.

For example, the Radio component exposes a data-checked attribute, which tells you if the radio is currently checked, and a data-disabled attribute, which tells you if the radio is currently disabled.

Use the CSS attribute selector to conditionally apply styles based on the presence of these data attributes. If you're using Tailwind CSS, the data attribute modifier makes this easy:

Each component also exposes information about its current state via render props that you can use to conditionally apply different styles or render different content.

For example, the Radio component exposes a checked state, which tells you if the radio is currently checked, and a disabled state, which tells you if the radio is currently disabled.

See the component API for a list of all the available render props.

Use the Description component within a Field to automatically associate it with a Radio using the aria-describedby attribute:

If you add the name prop to your RadioGroup, a hidden input element will be rendered and kept in sync with the radio group state.

This lets you use a radio group inside a native HTML <form> and make traditional form submissions as if you

*[Content truncated - see full docs]*

**Examples**:

```shell
npm install @headlessui/react
```

```jsx
import { Field, Label, Radio, RadioGroup } from '@headlessui/react'
import { useState } from 'react'

const plans = ['Startup', 'Business', 'Enterprise']

function Example() {
  let [selected, setSelected] = useState(plans[0])

  return (
    <RadioGroup value={selected} onChange={setSelected} aria-label="Server size">
      {plans.map((plan) => (
        <Field key={plan} className="flex items-center gap-2">
          <Radio
            value={plan}
            className="group flex size-5 item
...
```

```html
<!-- Rendered `Radio` -->
<span role="radio" data-checked data-disabled>
  <!-- ... -->
</span>
```

---

## Radio Group - Headless UI

**URL**: https://headlessui.com/v1/vue/radio-group

**Contents**:
- Radio Group
- Installation
- Basic example
- Styling different states
  - Using slots
  - Using data attributes
- Binding objects as values
- Using with HTML forms

Radio Groups give you the same functionality as native HTML radio inputs, without any of the styling. They're perfect for building out custom UIs for selectors.

To get started, install Headless UI via npm.

Please note that this library only supports Vue 3.

Radio Groups are built using the RadioGroup, RadioGroupLabel, and RadioGroupOption components.

Clicking an option will select it, and when the Radio Group is focused, the arrow keys will change the selected option.

Headless UI keeps track of a lot of state about each component, like which radiogroup option is currently selected, whether a popover is open or closed, or which item in a radiogroup is currently active via the keyboard.

But because the components are headless and completely unstyled out of the box, you can't see this information in your UI until you provide the styles you want for each state yourself.

Each component exposes information about its current state via slot props that you can use to conditionally apply different styles or render different content.

For example, the RadioGroupOption component exposes an active state, which tells you if the item is currently focused via the mouse or keyboard.

For a complete list of all the available slot props, see the component API documentation.

Each component also exposes information about its current state via a data-headlessui-state attribute that you can use to conditionally apply different styles.

When any of the states in the slot prop API are true, they will be listed in this attribute as space-separated strings so you can target them with a CSS attribute selector in the form [attr~=value].

For example, here's what the RadioGroup component with some child RadioGroupOption components renders when the radiogroup is open and the second item is active:

If you are using Tailwind CSS, you can use the @headlessui/tailwindcss plugin to target this attribute with modifiers like ui-open:* and ui-active:*:

Unlike native HTML form controls which only

*[Content truncated - see full docs]*

**Examples**:

```
npm install @headlessui/vue
```

```
<template>
  <RadioGroup v-model="plan">
    <RadioGroupLabel>Plan</RadioGroupLabel>
    <RadioGroupOption v-slot="{ checked }" value="startup">
      <span :class="checked ? 'bg-blue-200' : ''">Startup</span>
    </RadioGroupOption>
    <RadioGroupOption v-slot="{ checked }" value="business">
      <span :class="checked ? 'bg-blue-200' : ''">Business</span>
    </RadioGroupOption>
    <RadioGroupOption v-slot="{ checked }" value="enterprise">
      <span :class="checked ? 'bg-blue-200' : ''">En
...
```

```
<template>
  <RadioGroup v-model="plan">
    <RadioGroupLabel>Plan</RadioGroupLabel>
    <!-- Use the `active` state to conditionally style the active option. -->
    <!-- Use the `checked` state to conditionally style the checked option. -->
    <RadioGroupOption
      v-for="plan in plans"
      :key="plan"
      :value="plan"
      as="template"
      v-slot="{ active, checked }"    >
      <li
        :class="{
          'bg-blue-500 text-white': active,          'bg-white text-black': !acti
...
```

---

## Switch - Headless UI

**URL**: https://headlessui.com/react/switch

**Contents**:
- Components
  - Forms
- Switch
- Installation
- Basic example
- Styling
  - Using data attributes
  - Using render props

Switches are a pleasant interface for toggling a value between two states, and offer the same semantics and keyboard navigation as native checkbox elements.

To get started, install Headless UI via npm:

Switches are built using the Switch component. You can toggle your switch by clicking directly on the component, or by pressing the spacebar while it's focused.

Toggling the switch calls the onChange function with a negated version of the checked value.

Headless UI keeps track of a lot of state about each component, like whether or not a switch is checked, whether a popover is open or closed, or which item in a menu is currently focused via the keyboard.

But because the components are headless and completely unstyled out of the box, you can't see this information in your UI until you provide the styles you want for each state yourself.

The easiest way to style the different states of a Headless UI component is using the data-* attributes that each component exposes.

For example, the Switch component exposes a data-checked attribute, which tells you if the switch is currently checked, and a data-disabled attribute, which tells you if the switch is currently disabled.

Use the CSS attribute selector to conditionally apply styles based on the presence of these data attributes. If you're using Tailwind CSS, the data attribute modifier makes this easy:

See the component API for a list of all the available data attributes.

Each component also exposes information about its current state via render props that you can use to conditionally apply different styles or render different content.

For example, the Switch component exposes a checked state, which tells you if the switch is currently checked, and a disabled state, which tells you if the switch is currently disabled.

See the component API for a list of all the available render props.

Wrap a Label and Switch with the Field component to automatically associate them using a generated ID:

By default, clicking the

*[Content truncated - see full docs]*

**Examples**:

```shell
npm install @headlessui/react
```

```jsx
import { Switch } from '@headlessui/react'
import { useState } from 'react'

function Example() {
  const [enabled, setEnabled] = useState(false)

  return (
    <Switch
      checked={enabled}
      onChange={setEnabled}
      className="group inline-flex h-6 w-11 items-center rounded-full bg-gray-200 transition data-checked:bg-blue-600"
    >
      <span className="size-4 translate-x-1 rounded-full bg-white transition group-data-checked:translate-x-6" />
    </Switch>
  )
}
```

```html
<!-- Rendered `Switch` -->
<button data-checked data-disabled>
  <!-- ... -->
</button>
```

---

## Switch (Toggle) - Headless UI

**URL**: https://headlessui.com/v1/vue/switch

**Contents**:
- Switch (Toggle)
- Installation
- Basic example
- Styling different states
  - Using slots
  - Using data attributes
- Using a custom label
- Using with HTML forms

Switches are a pleasant interface for toggling a value between two states, and offer the same semantics and keyboard navigation as native checkbox elements.

To get started, install Headless UI via npm.

Please note that this library only supports Vue 3.

Switches are built using the Switch component, which takes in a ref via the v-model prop. You can toggle your Switch by clicking directly on the component, or by pressing the spacebar while its focused.

Toggling the switch updates your ref to its negated value.

Headless UI keeps track of a lot of state about each component, like which switch option is currently selected, whether a popover is open or closed, or which item in a menu is currently active via the keyboard.

But because the components are headless and completely unstyled out of the box, you can't see this information in your UI until you provide the styles you want for each state yourself.

Each component exposes information about its current state via slot props that you can use to conditionally apply different styles or render different content.

For example, the Switch component exposes an checked state, which tells you if the switch is currently checked or not.

For a complete list of all the available slot props, see the component API documentation.

Each component also exposes information about its current state via a data-headlessui-state attribute that you can use to conditionally apply different styles.

When any of the states in the slot prop API are true, they will be listed in this attribute as space-separated strings so you can target them with a CSS attribute selector in the form [attr~=value].

For example, here's what the Switch component renders when the switch is checked:

If you are using Tailwind CSS, you can use the @headlessui/tailwindcss plugin to target this attribute with modifiers like ui-checked:*:

By default, a Switch renders a button as well as whatever children you pass into it. This can make it harder to implement certai

*[Content truncated - see full docs]*

**Examples**:

```
npm install @headlessui/vue
```

```
<template>
  <Switch
    v-model="enabled"
    :class="enabled ? 'bg-blue-600' : 'bg-gray-200'"
    class="relative inline-flex h-6 w-11 items-center rounded-full"
  >
    <span class="sr-only">Enable notifications</span>
    <span
      :class="enabled ? 'translate-x-6' : 'translate-x-1'"
      class="inline-block h-4 w-4 transform rounded-full bg-white transition"
    />
  </Switch>
</template>

<script setup>
  import { ref } from 'vue'
  import { Switch } from '@headlessui/vue'

  const enab
...
```

```
<template>
  <!-- Use the `checked` state to conditionally style the button. -->  <Switch v-model="enabled" as="template" v-slot="{ checked }">
    <button
      class="relative inline-flex h-6 w-11 items-center rounded-full"
      :class="checked ? 'bg-blue-600' : 'bg-gray-200'"    >
      <span class="sr-only">Enable notifications</span>
      <span
        :class="checked ? 'translate-x-6' : 'translate-x-1'"        class="inline-block h-4 w-4 transform rounded-full bg-white transition"
      
...
```

---

## Tabs - Headless UI

**URL**: https://headlessui.com/react/tabs

**Contents**:
- Components
  - Forms
- Tabs
- Installation
- Basic example
- Styling
  - Using data attributes
  - Using render props

Easily create accessible, fully customizable tab interfaces, with robust focus management and keyboard navigation support.

To get started, install Headless UI via npm:

Tabs are built using the TabGroup, TabList, Tab, TabPanels, and TabPanel components. By default the first tab is selected, and clicking on any tab or selecting it with the keyboard will activate the corresponding panel.

Headless UI keeps track of a lot of state about each component, like which tab is currently selected, whether a popover is open or closed, or which item in a menu is currently focused via the keyboard.

But because the components are headless and completely unstyled out of the box, you can't see this information in your UI until you provide the styles you want for each state yourself.

The easiest way to style the different states of a Headless UI component is using the data-* attributes that each component exposes.

For example, the Tab component exposes a data-selected attribute, which tells you if the tab is currently selected, and a data-hover attribute, which tells you if the tab is currently being hovered by the mouse.

Use the CSS attribute selector to conditionally apply styles based on the presence of these data attributes. If you're using Tailwind CSS, the data attribute modifier makes this easy:

See the component API for a list of all the available data attributes.

Each component also exposes information about its current state via render props that you can use to conditionally apply different styles or render different content.

For example, the Tab component exposes a selected state, which tells you if the tab is currently selected, and a hover state, which tells you if the tab is currently being hovered by the mouse.

See the component API for a list of all the available render props.

Use the disabled prop to disable a Tab and prevent it from being selected:

If you've styled your TabList to appear vertically, use the vertical prop to enable navigating with the up a

*[Content truncated - see full docs]*

**Examples**:

```shell
npm install @headlessui/react
```

```jsx
import { Tab, TabGroup, TabList, TabPanel, TabPanels } from '@headlessui/react'

function Example() {
  return (
    <TabGroup>
      <TabList>
        <Tab>Tab 1</Tab>
        <Tab>Tab 2</Tab>
        <Tab>Tab 3</Tab>
      </TabList>
      <TabPanels>
        <TabPanel>Content 1</TabPanel>
        <TabPanel>Content 2</TabPanel>
        <TabPanel>Content 3</TabPanel>
      </TabPanels>
    </TabGroup>
  )
}
```

```html
<!-- Rendered `TabGroup` -->
<div>
  <div>
    <button>Tab 1</button>
    <button data-selected>Tab 2</button>
    <button data-hover>Tab 3</button>
  </div>
  <div>
    <div>Content 1</div>
    <div data-selected>Content 2</div>
    <div>Content 3</div>
  </div>
</div>
```

---

## Tabs - Headless UI

**URL**: https://headlessui.com/v1/vue/tabs

**Contents**:
- Tabs
- Installation
- Basic example
- Styling different states
  - Using slots
  - Using data attributes
- Disabling a tab
- Manually activating tabs

Easily create accessible, fully customizable tab interfaces, with robust focus management and keyboard navigation support.

To get started, install Headless UI via npm:

Tabs are built using the TabGroup, TabList, Tab, TabPanels, and TabPanel components. By default the first tab is selected, and clicking on any tab or selecting it with the keyboard will activate the corresponding panel.

Headless UI keeps track of a lot of state about each component, like which tab option is currently checked, whether a popover is open or closed, or which item in a menu is currently active via the keyboard.

But because the components are headless and completely unstyled out of the box, you can't see this information in your UI until you provide the styles you want for each state yourself.

Each component exposes information about its current state via slot props that you can use to conditionally apply different styles or render different content.

For example, the Tab component exposes a selected state, which tells you if the tab is currently selected.

For the complete slot props API for each component, see the component API documentation.

Each component also exposes information about its current state via a data-headlessui-state attribute that you can use to conditionally apply different styles.

When any of the states in the slot props API are true, they will be listed in this attribute as space-separated strings so you can target them with a CSS attribute selector in the form [attr~=value].

For example, here's what the TabGroup component with some child Tab components renders when the second tab is selected:

If you are using Tailwind CSS, you can use the @headlessui/tailwindcss plugin to target this attribute with modifiers like ui-open:*:

To disable a tab, use the disabled prop on the Tab component. Disabled tabs cannot be selected with the mouse, and are also skipped when navigating the tab list using the keyboard.

By default, tabs are automatically selected as the user 

*[Content truncated - see full docs]*

**Examples**:

```
npm install @headlessui/vue
```

```
<template>
  <TabGroup>
    <TabList>
      <Tab>Tab 1</Tab>
      <Tab>Tab 2</Tab>
      <Tab>Tab 3</Tab>
    </TabList>
    <TabPanels>
      <TabPanel>Content 1</TabPanel>
      <TabPanel>Content 2</TabPanel>
      <TabPanel>Content 3</TabPanel>
    </TabPanels>
  </TabGroup>
</template>

<script setup>
  import { TabGroup, TabList, Tab, TabPanels, TabPanel } from '@headlessui/vue'
</script>
```

```
<template>
  <TabGroup>
    <TabList>
      <!-- Use the `selected` state to conditionally style the selected tab. -->
      <Tab as="template" v-slot="{ selected }">        <button
          :class="{ 'bg-blue-500 text-white': selected, 'bg-white text-black': !selected }"        >
          Tab 1
        </button>
      </Tab>
      <!-- ... -->
    </TabList>
    <TabPanels>
      <TabPanel>Content 1</TabPanel>
      <!-- ... -->
    </TabPanels>
  </TabGroup>
</template>

<script setup>
  imp
...
```

---

## Transition - Headless UI

**URL**: https://headlessui.com/v1/vue/transition

**Contents**:
- Transition
- Installation
- About this component
- Basic example
- Showing and hiding content
- Rendering as a different element
- Animating transitions
- Co-ordinating multiple transitions

The Transition component takes Vue's built-in transition element one step further by letting you coordinate nested child transitions from a single root component.

To get started, install Headless UI via npm.

Please note that this library only supports Vue 3.

Vue has a built-in <transition> component that works great with Tailwind's class-based styling approach, as well as alongside other Headless UI components. In fact, most of the demos and code snippets you'll find for the other Vue components on this site rely on this built-in transition exclusively.

But there's one exception: nested child transitions. This technique is needed when you want to coordinate different animations for different child elements – for example, fading in a Dialog's backdrop, while at the same time sliding in the contents of the Dialog from one side of the screen.

The only way to achieve this effect using the built-in <transition> element is to manually synchronize each of the child transitions, and even then the approach can be buggy and error-prone.

That's why we've included a <TransitionRoot /> component in Headless UI. Its API is similar to Vue's own element, but it also provides a means for coordinating multiple transitions via the included <TransitionChild /> component, as described below.

For all components except Dialog, you may use Vue's built-in <transition> element whenever you're applying a single transition. For animating a Dialog, or coordinating multiple transitions on any other component, use the TransitionRoot component from Headless UI instead.

The TransitionRoot accepts a show prop that controls whether the children should be shown or hidden, and a set of lifecycle props (like enter-from, and leave-to) that let you add CSS classes at specific phases of a transition.

Wrap the content that should be conditionally rendered in a <TransitionRoot> component, and use the show prop to control whether the content should be visible or hidden.

By default, the transition co

*[Content truncated - see full docs]*

**Examples**:

```
npm install @headlessui/vue
```

```
<template>
  <button @click="isShowing = !isShowing">Toggle</button>
  <TransitionRoot
    :show="isShowing"
    enter="transition-opacity duration-75"
    enter-from="opacity-0"
    enter-to="opacity-100"
    leave="transition-opacity duration-150"
    leave-from="opacity-100"
    leave-to="opacity-0"
  >
    I will fade in and out
  </TransitionRoot>
</template>

<script setup>
  import { ref } from 'vue'
  import { TransitionRoot } from '@headlessui/vue'

  const isShowing = ref(true)
</scrip
...
```

```
<template>
  <button @click="isShowing = !isShowing">Toggle</button>
  <TransitionRoot :show="isShowing">    I will appear and disappear.
  </TransitionRoot>
</template>

<script setup>
  import { ref } from 'vue'
  import { TransitionRoot } from '@headlessui/vue'

  const isShowing = ref(true)
</script>
```

---

## Transition - Headless UI

**URL**: https://headlessui.com/react/transition

**Contents**:
- Components
  - Forms
- Transition
- Installation
- Basic example
- Examples
  - Different enter/leave transitions
  - Coordinating multiple transitions

Control the transition styles of conditionally rendered elements, including nested child transitions, using CSS classes.

To get started, install Headless UI via npm:

To transition a conditionally rendered element, wrap it in the Transition component and use the show prop to indicate whether it is open or closed.

Then, use native CSS transition styles to apply an animation, specifying the element's closed styles by targeting the data-closed attribute that the Transition component exposes.

Styles defined with the data-closed attribute will be used as the starting point when transitioning in as well as the ending point when transitioning out.

For more complex transitions, you can also use the data-enter, data-leave, and data-transition attributes to apply styles at the different stages of the transition.

Use the data-enter and data-leave attributes to apply different transition styles when entering and leaving:

This example combines the data-enter and data-closed attributes to specify the starting point of the enter transition, and combines the data-leave and data-closed attributes to specify the ending point of the leave transition.

It also uses the data-enter and data-leave attributes to specify different enter and leave durations.

Sometimes you need to transition multiple elements with different animations but all based on the same state. For example, say the user clicks a button to open a sidebar that slides over the screen, and you also need to fade-in a backdrop at the same time.

You can do this by wrapping the related elements with a parent Transition component, and wrapping each child that needs its own transition styles with a TransitionChild component, which will automatically communicate with the parent Transition and inherit the parent's open state.

The TransitionChild component has the exact same API as the Transition component, but with no show prop, since the show value is controlled by the parent.

Parent Transition components will always aut

*[Content truncated - see full docs]*

**Examples**:

```shell
npm install @headlessui/react
```

```jsx
import { Transition } from '@headlessui/react'
import { useState } from 'react'

function Example() {
  const [open, setOpen] = useState(false)

  return (
    <>
      <button onClick={() => setOpen((open) => !open)}>Toggle</button>
      <Transition show={open}>
        <div className="transition duration-300 ease-in data-closed:opacity-0">I will fade in and out</div>
      </Transition>
    </>
  )
}
```

```jsx
import { Transition } from '@headlessui/react'
import clsx from 'clsx'
import { useState } from 'react'

function Example() {
  const [open, setOpen] = useState(false)

  return (
    <div className="relative">
      <button onClick={() => setOpen((open) => !open)}>Toggle</button>
      <Transition show={open}>
        <div
          className={clsx([
            // Base styles
            'absolute w-48 border transition ease-in-out',
            // Shared closed styles
            'data-closed
...
```

---
