---
description: Chakra UI - Accessible React component library with built-in theming and styling
---

# Chakra-Ui

**Purpose**: Comprehensive Chakra UI development assistance for building accessible, composable React components with theme support

## When to Use This Skill

Use this skill when:
- Building components with Chakra UI
- Implementing theme configuration and customization
- Working with Chakra's styling system and responsive design
- Using Chakra UI's form components and patterns
- Implementing color mode (dark/light theme) support
- Debugging Chakra UI issues or styling problems
- Learning Chakra UI best practices and patterns

**Keywords**: chakra-ui, @chakra-ui/react, components, theming, accessibility, responsive design, color mode, form components, layout

## Quick Reference

### Installation

```bash
npm install @chakra-ui/react @emotion/react @emotion/styled framer-motion
```

### Basic Setup

```tsx
import { ChakraProvider } from '@chakra-ui/react'

function App() {
  return (
    <ChakraProvider>
      {/* Your app */}
    </ChakraProvider>
  )
}
```

### Common Component Patterns

**Button**
```tsx
import { Button } from '@chakra-ui/react'

<Button colorScheme="blue" size="md">
  Click me
</Button>
```

**Box (Layout)**
```tsx
import { Box } from '@chakra-ui/react'

<Box bg="blue.500" p={4} borderRadius="md">
  Styled container
</Box>
```

**Form Field**
```tsx
import { Input, FormControl, FormLabel } from '@chakra-ui/react'

<FormControl>
  <FormLabel>Email</FormLabel>
  <Input type="email" />
</FormControl>
```

**Responsive Design**
```tsx
<Box fontSize={['sm', 'md', 'lg']} p={[2, 4, 6]}>
  Responsive text
</Box>
```

## Reference Documentation

This skill includes comprehensive documentation in `.github/copilot-skills/chakra-ui/`:

- **components.md** - All Chakra UI component documentation and examples
- **get-started.md** - Installation, setup, configuration, and guides
- **overview.md** - Overview and styling system concepts
- **patterns.md** - Common code patterns and usage examples

## How to Use

### For Quick Answers
Ask directly about Chakra UI components, APIs, theming, or styling.

### For Detailed Information
Reference specific documentation files:
- Check `references/get-started.md` for setup and configuration
- Check `references/components.md` for component APIs and examples
- Check `patterns.md` for common usage patterns

### For Theme Customization
Ask about color schemes, variants, spacing, or custom theme tokens.

### For Accessibility
Ask about ARIA labels, keyboard navigation, or accessible patterns.

## Related Skills

- `/shadcn` - shadcn/ui component library
- `/radix-ui` - Radix UI primitives

## More Information

- **Base Documentation**: https://chakra-ui.com/
- **Package**: `@chakra-ui/react`
- **License**: MIT
- **Generated**: 2025-10-19

