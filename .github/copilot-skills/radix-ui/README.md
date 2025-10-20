# Radix UI Skill

Unstyled, accessible React component primitives for building design systems and user interfaces.

## Overview

Radix Primitives is a comprehensive collection of open-source React components for building accessible, performant design systems. This skill provides comprehensive documentation and best practices for working with Radix UI.

## Components

### Container & Layout
- **Scroll Area** - Scrollable container with cross-browser styling
- **Separator** - Visual divider between content

### Dialog & Disclosure
- **Dialog** - Modal and non-modal dialogs with focus management
- **Alert Dialog** - Modal dialog for alerts and confirmations
- **Popover** - Floating content with collision handling
- **Hover Card** - Hover-triggered card display
- **Collapsible** - Expandable/collapsible sections

### Menu & Navigation
- **Dropdown Menu** - Menu with submenus and keyboard navigation
- **Context Menu** - Right-click context menus
- **Menubar** - Horizontal menu bar
- **Navigation Menu** - Multi-level navigation structure

### Form Components
- **Label** - Accessible form labels
- **Button** - Interactive button primitive
- **Checkbox** - Toggle checkbox input
- **Radio Group** - Single-selection radio buttons
- **Toggle** - Toggle button primitive
- **Toggle Group** - Group of toggle buttons
- **Switch** - Toggle switch control
- **Slider** - Range/value slider input
- **Select** - Dropdown select control
- **Combobox** - Searchable select/autocomplete

### Display Components
- **Avatar** - User profile image display
- **Badge** - Small badge/label display
- **Progress** - Progress bar indicator
- **Tooltip** - Informational tooltip
- **Tabs** - Tabbed content interface
- **Accordion** - Expandable accordion items
- **Aspect Ratio** - Fixed aspect ratio container

## Core Principles

### 1. Unstyled by Default
- No built-in styles - you control the appearance
- Works with any CSS solution (CSS-in-JS, Tailwind, CSS Modules, etc.)
- Minimal CSS footprint

### 2. Accessible
- WAI-ARIA compliant implementations
- Full keyboard navigation support
- Screen reader tested
- Semantic HTML

### 3. Composable
- Granular component parts
- Flexible component composition
- Mix and match subcomponents
- No wrapper components required

### 4. Developer-Friendly
- Fully TypeScript support
- Consistent API across components
- Intuitive prop names
- Excellent documentation

## Installation

Each component is independently versioned and published:

```bash
# Install individual components
npm install @radix-ui/react-dialog
npm install @radix-ui/react-dropdown-menu
npm install @radix-ui/react-select

# Or install multiple at once
npm install @radix-ui/react-* --save
```

## Common Patterns

### Basic Component Usage

```tsx
import * as Dialog from "@radix-ui/react-dialog";

export function MyDialog() {
  return (
    <Dialog.Root>
      <Dialog.Trigger>Open Dialog</Dialog.Trigger>
      <Dialog.Portal>
        <Dialog.Overlay />
        <Dialog.Content>
          <Dialog.Title>Dialog Title</Dialog.Title>
          <Dialog.Description>Dialog content here</Dialog.Description>
          <Dialog.Close>Close</Dialog.Close>
        </Dialog.Content>
      </Dialog.Portal>
    </Dialog.Root>
  );
}
```

### Styled Component Wrapper

```tsx
import styled from "@emotion/styled";
import * as Dialog from "@radix-ui/react-dialog";

const DialogContent = styled(Dialog.Content)`
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
`;

export function StyledDialog() {
  return (
    <Dialog.Root>
      <Dialog.Trigger>Open</Dialog.Trigger>
      <Dialog.Portal>
        <Dialog.Overlay />
        <DialogContent>
          <Dialog.Title>Title</Dialog.Title>
          <Dialog.Close>Close</Dialog.Close>
        </DialogContent>
      </Dialog.Portal>
    </Dialog.Root>
  );
}
```

### Controlled Component

```tsx
import { useState } from "react";
import * as Select from "@radix-ui/react-select";

export function MySelect() {
  const [value, setValue] = useState("");

  return (
    <Select.Root value={value} onValueChange={setValue}>
      <Select.Trigger>{value || "Select..."}</Select.Trigger>
      <Select.Portal>
        <Select.Content>
          <Select.Item value="option1">Option 1</Select.Item>
          <Select.Item value="option2">Option 2</Select.Item>
        </Select.Content>
      </Select.Portal>
    </Select.Root>
  );
}
```

## Best Practices

### 1. Import Only What You Need
```tsx
// ✓ Good - import only needed components
import * as Dialog from "@radix-ui/react-dialog";

// ✗ Avoid - unnecessary imports
import * as RadixUI from "@radix-ui/react-*";
```

### 2. Use asChild for Flexibility
```tsx
// ✓ Good - allows custom button styling
<Dialog.Trigger asChild>
  <button className="custom-button">Open</button>
</Dialog.Trigger>

// ✗ Avoid - limited styling options
<Dialog.Trigger>Open</Dialog.Trigger>
```

### 3. Manage Focus Properly
```tsx
// ✓ Good - custom focus management
<Dialog.Content
  onOpenAutoFocus={(e) => {
    e.preventDefault();
    focusTarget.current?.focus();
  }}
>
  {/* ... */}
</Dialog.Content>
```

### 4. Handle Portal Rendering
```tsx
// ✓ Good - portal prevents z-index issues
<Dialog.Portal>
  <Dialog.Overlay />
  <Dialog.Content>{/* ... */}</Dialog.Content>
</Dialog.Portal>
```

### 5. Accessibility Considerations
```tsx
// ✓ Good - accessible labels and descriptions
<Dialog.Root>
  <Dialog.Trigger>Open</Dialog.Trigger>
  <Dialog.Portal>
    <Dialog.Overlay />
    <Dialog.Content>
      <Dialog.Title>Are you sure?</Dialog.Title>
      <Dialog.Description>
        This action cannot be undone.
      </Dialog.Description>
    </Dialog.Content>
  </Dialog.Portal>
</Dialog.Root>
```

## Resources

- **Official Documentation**: https://www.radix-ui.com/primitives/docs
- **GitHub Repository**: https://github.com/radix-ui/primitives
- **Discord Community**: https://discord.com/invite/7Xb99uG
- **NPM Packages**: https://www.npmjs.com/org/radix-ui

## Related Skills

- **shadcn** - UI component library built on Radix UI
- **React** - Core framework
- **TypeScript** - Type safety

## Tags

`components`, `accessibility`, `a11y`, `react`, `primitives`, `ui`, `design-system`, `unstyled`, `open-source`
