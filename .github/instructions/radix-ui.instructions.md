---
description: "Automatic context for Radix UI components - provides accessibility patterns, API guidance, and best practices"
applyTo: "**/*.tsx, **/*.jsx, **/*.ts, **/package.json"
---

# Radix UI - Automatic Context Instructions

**Related Prompt:** `/radix-ui`  
**Related Skill:** `.github/copilot-skills/ui/radix-ui/`

**Triggers:** radix-ui, @radix-ui/react-, Dialog, Select, Menu, Checkbox, primitives, composable components, unstyled components

## Context: What This Provides

When working with Radix UI packages (@radix-ui/react-*) or when user queries mention accessibility, component composition, or unstyled components, this context is automatically activated.

## Core Principles

### Accessibility First
- **WAI-ARIA Compliance** - All components follow official ARIA patterns
- **Keyboard Navigation** - Full keyboard support is mandatory
- **Focus Management** - Explicit focus control with callbacks
- **Screen Reader Testing** - Test with assistive technologies
- **Semantic HTML** - Use proper semantic elements

### Unstyled & Composable
- **No Default Styles** - You control the appearance completely
- **Granular Components** - Root, Trigger, Content, Overlay, etc. parts
- **asChild Flexibility** - Replace root element with custom component
- **Portal Pattern** - Use Portal for overlays/modals
- **Type Safety** - Full TypeScript support

### Developer Experience
- **Consistent APIs** - Similar structure across all components
- **Well Documented** - Clear examples and patterns available
- **Incremental Adoption** - Use components alongside existing code
- **No Breaking Changes** - Stable, predictable versioning

## Default Behaviors

### When user mentions "Radix UI component"
1. Suggest `/radix-ui` skill prompt for comprehensive guide
2. Review component structure (Root, Trigger, Content, etc.)
3. Check for Portal usage in overlay components
4. Verify ARIA labels are present
5. Consider focus management needs

### When user mentions "accessibility" or "a11y"
1. Activate Radix UI accessibility best practices
2. Suggest `/radix-ui` skill for pattern examples
3. Recommend keyboard testing (Tab, Escape, Arrows)
4. Check ARIA attributes (aria-label, aria-describedby, etc.)
5. Review screen reader compatibility

### When user mentions "keyboard navigation"
1. Ensure all interactive elements are keyboard accessible
2. Check Tab order and focus management
3. Implement arrow key navigation for lists/menus
4. Verify Escape key handling for modals
5. Test with keyboard-only navigation

### When user mentions "styling" or "CSS"
1. Remember components are unstyled by default
2. Use preferred CSS solution (Tailwind, CSS-in-JS, etc.)
3. Don't override internal Radix accessibility attributes
4. Consider Portal pattern for z-index management
5. Use data attributes for styling states

## Quality Guidelines

### ✅ Do
- Import only components you need (`import * as Dialog from "@radix-ui/react-dialog"`)
- Use `Portal` for overlay/dialog/menu components
- Add ARIA labels to interactive elements
- Implement explicit focus management
- Test keyboard navigation thoroughly
- Use TypeScript for type safety
- Follow official component patterns
- Consider composed components (multiple Radix components together)
- Test with screen readers (VoiceOver, NVDA, JAWS)

### ❌ Don't
- Import unnecessary components to keep bundle size small
- Forget Portal pattern for overlays (z-index issues)
- Override accessibility attributes manually
- Skip focus management in complex interactions
- Use generic `<div onClick>` instead of semantic elements
- Ignore keyboard navigation requirements
- Hardcode string values without ARIA descriptions
- Mix controlled/uncontrolled state patterns in same component
- Deploy without accessibility testing

## Common Component Patterns

### Basic Component Structure
```tsx
import * as ComponentName from "@radix-ui/react-component-name";

export function MyComponent() {
  return (
    <ComponentName.Root>
      <ComponentName.Trigger>Action</ComponentName.Trigger>
      <ComponentName.Portal>
        <ComponentName.Overlay />
        <ComponentName.Content>
          <ComponentName.Close />
        </ComponentName.Content>
      </ComponentName.Portal>
    </ComponentName.Root>
  );
}
```

### Focus Management in Dialog
```tsx
onOpenAutoFocus={(e) => {
  e.preventDefault();
  closeButtonRef.current?.focus();
}}
```

### Styled with CSS-in-JS
```tsx
const DialogContent = styled(Dialog.Content)`
  background: white;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
`;
```

### Using asChild for Flexibility
```tsx
<Dialog.Trigger asChild>
  <button className="custom-button">Open</button>
</Dialog.Trigger>
```

## Common Workflows

### Setup New Radix Component
```bash
npm install @radix-ui/react-[component-name]  # Install specific component
npm install @radix-ui/react-*                 # Install all (optional)
```

### Build Dialog Component
1. Import Dialog from @radix-ui/react-dialog
2. Structure with Root > Trigger > Portal > (Overlay + Content)
3. Add Title and Description for accessibility
4. Implement focus management
5. Style with your CSS solution
6. Test keyboard (Tab, Escape) and screen readers

### Build Form with Multiple Inputs
1. Create form container
2. Use individual Radix components (Input, Select, Checkbox, etc.)
3. Associate labels with inputs
4. Implement validation feedback
5. Keyboard test the entire form
6. Verify tab order

### Create Accessible Menu
1. Use Dropdown/Context Menu component
2. Add semantic Item elements
3. Implement arrow key navigation
4. Add Separator elements for grouping
5. Support nested submenus (Sub pattern)
6. Test with keyboard and screen readers

## Bundled Scripts

The radix-ui skill provides helper tools in `.github/copilot-skills/ui/radix-ui/`:

- `README.md` - Full component reference and patterns
- `patterns.md` - Detailed usage patterns
- `reference.md` - API reference documentation
- `references/` - Component-specific documentation

## Integration Points

### TypeScript Support
All Radix UI packages include complete TypeScript definitions:

```tsx
import * as Dialog from "@radix-ui/react-dialog";

type DialogProps = React.ComponentProps<typeof Dialog.Content>;
```

### CSS Solutions
Works seamlessly with:
- Tailwind CSS
- Styled Components
- Emotion
- CSS Modules
- CSS-in-JS frameworks

### State Management
Compatible with:
- React useState (uncontrolled)
- External state (Redux, Zustand, etc.)
- Form libraries (React Hook Form, Formik)

## Next Steps

When working with Radix UI:
1. Use `/radix-ui` prompt for guided implementation
2. Check `.github/copilot-skills/ui/radix-ui/README.md` for comprehensive patterns
3. Reference component-specific docs in `references/` directory
4. Test keyboard navigation and screen reader compatibility
5. Verify ARIA labels and semantic HTML structure

## Related Skills

- **React** - Core framework and hooks
- **TypeScript** - Type-safe component development
- **shadcn/ui** - Pre-styled components built on Radix
- **Tailwind CSS** - Styling framework compatible with Radix

## Documentation Links

- **Official**: https://www.radix-ui.com/primitives/docs
- **GitHub**: https://github.com/radix-ui/primitives
- **Discord Community**: https://discord.com/invite/7Xb99uG
- **Component Packages**: https://www.npmjs.com/org/radix-ui

---

**Last Updated**: 2025-10-19  
**Applies to**: React projects using @radix-ui packages
