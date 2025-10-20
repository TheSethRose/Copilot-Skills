---
description: Unstyled, accessible React component primitives for building design systems
---

# Radix UI Primitives Skill

**Purpose**: Comprehensive guide for building accessible, composable UI components with Radix UI Primitives

## When to Use This Skill

Use this skill when:
- Building React applications with accessible component libraries
- Creating design systems or component libraries
- Working with Radix UI packages (@radix-ui/react-*)
- Implementing complex UI patterns with focus management
- Ensuring WCAG accessibility compliance
- Needing unstyled, composable components

**Keywords**: radix-ui, primitives, react, components, accessibility, a11y, design-system, unstyled

## Quick Reference

### Installation Patterns

```bash
# Install specific components
npm install @radix-ui/react-dialog @radix-ui/react-select

# Install all Radix UI packages
npm install @radix-ui/react-*
```

### Component Categories

| Category | Components |
|----------|-----------|
| **Dialog & Overlay** | Dialog, Alert Dialog, Popover, Hover Card, Collapsible |
| **Menus & Navigation** | Dropdown Menu, Context Menu, Menubar, Navigation Menu |
| **Forms & Input** | Label, Button, Checkbox, Radio Group, Toggle, Switch, Slider, Select, Combobox |
| **Display** | Avatar, Badge, Progress, Tooltip, Tabs, Accordion, Aspect Ratio |
| **Layout** | Scroll Area, Separator |

### Basic Component Structure

```tsx
import * as Component from "@radix-ui/react-component-name";

// Root wraps state
<Component.Root>
  {/* Trigger opens/interacts */}
  <Component.Trigger>Action</Component.Trigger>
  
  {/* Portal renders outside DOM flow (optional) */}
  <Component.Portal>
    {/* Overlay (optional) */}
    <Component.Overlay />
    
    {/* Content is the main element */}
    <Component.Content>
      {/* Sub-elements */}
      <Component.Title />
      <Component.Description />
      <Component.Close />
    </Component.Content>
  </Component.Portal>
</Component.Root>
```

## Core Concepts

### 1. Unstyled Components
- No built-in styles - complete styling control
- Works with Tailwind CSS, Emotion, Styled Components, etc.
- Minimal CSS footprint
- Full design flexibility

### 2. Accessibility First
- **WAI-ARIA Compliant** - Follows official ARIA patterns
- **Keyboard Navigation** - Full keyboard support by default
- **Screen Reader Support** - Tested with NVDA, JAWS, VoiceOver
- **Focus Management** - Intelligent focus handling
- **Semantic HTML** - Proper element semantics

### 3. Composable Architecture
- **Sub-components** - Granular component parts (Root, Trigger, Content, etc.)
- **No Wrapper Components** - Don't force structure
- **Flexible Composition** - Mix and match parts
- **asChild Prop** - Replace root element with custom component

### 4. Consistent API
- Similar component structures across library
- Predictable prop names and patterns
- TypeScript support throughout
- Clear documentation for each component

## Common Patterns

### Pattern 1: Dialog with Focus Management

```tsx
import * as Dialog from "@radix-ui/react-dialog";
import { useRef } from "react";

export function MyDialog() {
  const closeButtonRef = useRef<HTMLButtonElement>(null);

  return (
    <Dialog.Root>
      <Dialog.Trigger>Open</Dialog.Trigger>
      
      <Dialog.Portal>
        <Dialog.Overlay className="overlay" />
        
        <Dialog.Content
          className="dialog"
          onOpenAutoFocus={(e) => {
            // Focus close button on open
            closeButtonRef.current?.focus();
            e.preventDefault();
          }}
        >
          <Dialog.Title>Title</Dialog.Title>
          <Dialog.Description>Description</Dialog.Description>
          
          {/* Content */}
          
          <Dialog.Close ref={closeButtonRef}>
            Close
          </Dialog.Close>
        </Dialog.Content>
      </Dialog.Portal>
    </Dialog.Root>
  );
}
```

### Pattern 2: Styled Select Component

```tsx
import * as Select from "@radix-ui/react-select";
import styled from "@emotion/styled";

const SelectContent = styled(Select.Content)`
  background: white;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
`;

const SelectItem = styled(Select.Item)`
  padding: 8px 12px;
  cursor: pointer;
  
  &[data-highlighted] {
    background: #f0f0f0;
  }
`;

export function MySelect() {
  return (
    <Select.Root>
      <Select.Trigger>Select Option</Select.Trigger>
      
      <Select.Portal>
        <SelectContent>
          <SelectItem value="opt1">Option 1</SelectItem>
          <SelectItem value="opt2">Option 2</SelectItem>
        </SelectContent>
      </Select.Portal>
    </Select.Root>
  );
}
```

### Pattern 3: Controlled Checkbox Group

```tsx
import * as Checkbox from "@radix-ui/react-checkbox";
import { useState } from "react";

export function CheckboxGroup() {
  const [checked, setChecked] = useState<Record<string, boolean>>({});

  return (
    <div>
      {["opt1", "opt2", "opt3"].map((opt) => (
        <div key={opt}>
          <Checkbox.Root
            checked={checked[opt] || false}
            onCheckedChange={(val) => {
              setChecked((prev) => ({ ...prev, [opt]: val }));
            }}
          >
            <Checkbox.Indicator>✓</Checkbox.Indicator>
          </Checkbox.Root>
          <label>{opt}</label>
        </div>
      ))}
    </div>
  );
}
```

### Pattern 4: Dropdown Menu with Submenus

```tsx
import * as DropdownMenu from "@radix-ui/react-dropdown-menu";

export function ContextMenu() {
  return (
    <DropdownMenu.Root>
      <DropdownMenu.Trigger>Menu</DropdownMenu.Trigger>
      
      <DropdownMenu.Portal>
        <DropdownMenu.Content>
          <DropdownMenu.Item>Edit</DropdownMenu.Item>
          
          <DropdownMenu.Sub>
            <DropdownMenu.SubTrigger>Share</DropdownMenu.SubTrigger>
            <DropdownMenu.Portal>
              <DropdownMenu.SubContent>
                <DropdownMenu.Item>Twitter</DropdownMenu.Item>
                <DropdownMenu.Item>Email</DropdownMenu.Item>
              </DropdownMenu.SubContent>
            </DropdownMenu.Portal>
          </DropdownMenu.Sub>
          
          <DropdownMenu.Separator />
          <DropdownMenu.Item>Delete</DropdownMenu.Item>
        </DropdownMenu.Content>
      </DropdownMenu.Portal>
    </DropdownMenu.Root>
  );
}
```

## Best Practices

### ✅ Do

- Import only components you need
- Use `Portal` for overlay components to avoid z-index issues
- Implement proper `ARIA` labels and descriptions
- Manage focus explicitly for complex interactions
- Use `asChild` prop for flexible styling
- Test keyboard navigation (Tab, Enter, Escape, Arrows)
- Reference official documentation for specific components

### ❌ Don't

- Override Radix's internal accessibility attributes
- Ignore keyboard navigation requirements
- Skip ARIA labels on interactive elements
- Use `Portal` for non-overlay components
- Force the component structure without flexibility
- Forget to test with screen readers

## Reference Documentation

This skill includes detailed information in `.github/copilot-skills/ui/radix-ui/`:

- **README.md** - Comprehensive overview and common patterns
- **patterns.md** - Detailed usage patterns
- **reference.md** - API reference
- **references/components.md** - Component documentation index

## Example Workflows

### Workflow: Building an Accessible Dialog Form

1. Wrap dialog with `Dialog.Root`
2. Create trigger button with `Dialog.Trigger`
3. Use `Dialog.Portal` to render outside DOM
4. Add `Dialog.Overlay` for backdrop
5. Structure content with `Dialog.Title` and `Dialog.Description`
6. Manage focus with `onOpenAutoFocus` callback
7. Style all parts with your preferred CSS solution
8. Test with keyboard (Tab, Escape) and screen readers

### Workflow: Creating a Form with Multiple Inputs

1. Create form container
2. Use individual Radix components (Select, Checkbox, RadioGroup, etc.)
3. Wrap related fields with `Label`
4. Implement controlled or uncontrolled state management
5. Add validation feedback
6. Test keyboard navigation through form
7. Verify ARIA labels for all inputs

## Quality Checklist

Before committing Radix UI component code:

- [ ] All interactive elements keyboard accessible
- [ ] Proper ARIA labels/descriptions applied
- [ ] Focus management tested (Tab, Shift+Tab)
- [ ] Screen reader compatibility verified
- [ ] Styling applied without overriding accessibility
- [ ] Component composition follows official patterns
- [ ] TypeScript types are properly used
- [ ] Portal pattern used for overlays
- [ ] Tested in multiple browsers
- [ ] Responsive behavior verified

## Resources & Links

- **Official Docs**: https://www.radix-ui.com/primitives/docs
- **GitHub**: https://github.com/radix-ui/primitives
- **Discord**: https://discord.com/invite/7Xb99uG
- **NPM Org**: https://www.npmjs.com/org/radix-ui

## Related Skills

- **shadcn** - Pre-styled component library built on Radix UI
- **React** - Core React framework
- **Accessibility** - General web accessibility patterns
- **TypeScript** - Type safety and development

## Related Components

- **shadcn/ui** - Component library (Radix UI + Tailwind)
- **Headless UI** - Alternative headless components
- **React Aria** - Hooks library by Adobe

---

**Generated**: October 19, 2025  
**Base Documentation**: https://www.radix-ui.com/primitives/docs  
**Last Updated**: 2025-10-19
