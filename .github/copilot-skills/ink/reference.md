# Ink - Reference Documentation

## Overview

Ink is a React renderer for building command-line interfaces. It enables developers familiar with React to build interactive CLI applications using the same component-based patterns they use for web development.

### Key Features

- **React Components** - All React features work in Ink
- **Flexbox Layouts** - CSS-like layout system in the terminal
- **Hooks Support** - useState, useEffect, useRef, etc.
- **Keyboard Input** - Handle keyboard input with `useInput`
- **Testing** - Test with `ink-testing-library`
- **React DevTools** - Debug with familiar React tools
- **Screen Reader Support** - Accessibility features

## Architecture

```
render() → Ink App → React Reconciler → Virtual DOM → Terminal Output
                                              ↓
                                    Yoga Layout Engine
                                    (Flexbox Calculations)
```

## Rendering Pipeline

1. **Component Tree** - React components
2. **Reconciliation** - React renders tree
3. **Layout Calculation** - Yoga computes Flexbox
4. **Output Generation** - Generate ANSI sequences
5. **Terminal Rendering** - Display to stdout

## Component Hierarchy

```
<App>
  ├── <Box> (Layout Container)
  │   ├── <Text> (Output)
  │   ├── <Newline> (Line Break)
  │   ├── <Spacer> (Flex Filler)
  │   ├── <Static> (Frozen Output)
  │   └── <Transform> (Output Transformer)
  └── Custom Components
```

## File Structure Reference

Generated from 46 TypeScript files:

- **Core**: `ink.tsx`, `render-node-to-output.ts`, `output.ts`
- **Components**: `Text.tsx`, `Box.tsx`, `Spacer.tsx`, `Static.tsx`, `Transform.tsx`
- **Contexts**: `AppContext.ts`, `FocusContext.ts`, `StdinContext.ts`
- **Layout**: `measure-element.ts`, `get-max-width.ts`, `styles.ts`
- **Input**: `parse-keypress.ts`
- **DevTools**: `devtools.ts`, `devtools-window-polyfill.ts`

## Component API Reference

### Text Component

Properties:
- `color` - Text color (named or hex)
- `backgroundColor` - Background color
- `bold` - Bold text
- `italic` - Italic text
- `underline` - Underlined text
- `strikethrough` - Strikethrough text
- `dimmed` - Dimmed/grayed text
- `inverse` - Inverted colors
- `wrap` - Enable text wrapping

Behavior:
- Default text output element
- Handles color and style formatting
- Supports ANSI color codes
- Respects terminal capabilities

### Box Component

Properties (Flexbox):
- `flexDirection` - 'row' or 'column'
- `alignItems` - 'flex-start', 'center', 'flex-end'
- `justifyContent` - 'flex-start', 'center', 'flex-end', 'space-between', 'space-around'
- `width` / `height` - In characters
- `minWidth` / `minHeight` - Minimum dimensions
- `padding` / `paddingX` / `paddingY` - Internal spacing
- `margin` / `marginX` / `marginY` - External spacing
- `borderStyle` - 'single', 'double', 'round', 'bold', 'dashed'
- `borderColor` - Border color

Behavior:
- Container for layout
- Applies Flexbox calculations
- Nests other components
- Supports borders and padding

### Static Component

Properties:
- `items` - Array to render
- `children` - Render function

Behavior:
- Renders output once
- Freezes content (no updates)
- Useful for logs and results
- Output stays in terminal

### Transform Component

Properties:
- `transform` - Function to transform output string

Behavior:
- Pipes output through transform function
- Modifies ANSI output
- Can uppercase, add prefixes, etc.
- Works with nested content

## Hook Reference

### useInput

```typescript
useInput((input: string, key: Key) => {
  // Handle input
}, options?: {
  isActive?: boolean;
})
```

Key object properties:
- `upArrow`, `downArrow`, `leftArrow`, `rightArrow` - Arrow keys
- `pageDown`, `pageUp` - Page keys
- `return` - Enter key
- `escape` - Escape key
- `tab` - Tab key
- `backspace` - Backspace key
- `delete` - Delete key
- `meta` - Meta/Command key
- `shift` - Shift key
- `ctrl` - Control key

### useApp

Returns:
- `exit()` - Exit the app
- `isActive` - Is app active
- `enableRawMode()` - Enable raw mode
- `disableRawMode()` - Disable raw mode

### useStdin / useStdout / useStderr

Return stream objects with:
- `stream` - Actual stream object
- `write()` - Write to stream
- `isTTY` - Is TTY connected

### useFocus

```typescript
useFocus(options?: {
  autoFocus?: boolean;
  isActive?: boolean;
})
```

Returns:
- `isFocused` - Is component focused

### useFocusManager

Returns:
- `focus(id)` - Focus component by ID
- `focusNext()` - Focus next component
- `focusPrevious()` - Focus previous component

## Styling System

### Colors

**Named Colors**: black, red, green, yellow, blue, magenta, cyan, white, gray
**Bright Colors**: redBright, greenBright, blueBright, etc.
**RGB Colors**: Hex format (limited support)

### Text Styles

- `bold` - Bold text
- `italic` - Italic (if supported)
- `underline` - Underlined text
- `strikethrough` - Strikethrough
- `inverse` - Inverted colors
- `dimmed` - Reduced brightness

### Borders

**Styles**: 'single', 'double', 'round', 'bold', 'dashed', 'dotted'

```jsx
<Box borderStyle="round" borderColor="cyan">
  Content
</Box>
```

## Layout System

### Flexbox Properties

- `flexDirection` - Direction of flex items
  - 'row' - Horizontal
  - 'column' - Vertical
  - 'row-reverse' - Reversed horizontal
  - 'column-reverse' - Reversed vertical

- `alignItems` - Cross-axis alignment
  - 'flex-start' - Top/left
  - 'center' - Centered
  - 'flex-end' - Bottom/right

- `justifyContent` - Main-axis alignment
  - 'flex-start' - Start
  - 'center' - Centered
  - 'flex-end' - End
  - 'space-between' - Space between items
  - 'space-around' - Space around items

### Dimensions

```jsx
<Box width={50} height={10} minWidth={30} minHeight={5}>
  {/* Content */}
</Box>
```

### Spacing

```jsx
<Box padding={1} paddingX={2} paddingY={1} margin={1}>
  {/* Content */}
</Box>
```

## Render Options

```typescript
render(component, {
  stdout: process.stdout,           // Output stream
  stderr: process.stderr,            // Error stream
  stdin: process.stdin,              // Input stream
  exitOnCtrlC: true,                 // Exit on Ctrl+C
  patchConsole: true,                // Patch console methods
  debug: false,                      // Debug mode
  experimental_useStdoutFallback: false,
  maxFps: 30,                        // Max frames per second
})
```

Returns:
```typescript
{
  rerender(tree),        // Update component
  unmount(),             // Unmount app
  waitUntilExit(),       // Promise: wait for exit
  clear()                // Clear output
}
```

## Testing

### Using ink-testing-library

```typescript
import { render } from 'ink-testing-library';

const { lastFrame } = render(<YourComponent />);
expect(lastFrame()).toContain('Expected text');
```

Methods:
- `lastFrame()` - Get last rendered frame
- `unmount()` - Unmount component
- `waitFor()` - Wait for condition
- `debug()` - Print current output

## Debugging

### React DevTools

Enable with environment variable:
```bash
DEV=true node app.js
```

Then run:
```bash
npx react-devtools
```

Features:
- Component tree inspection
- Props/state inspection
- Hot reload of props
- Component highlighting

### Screen Reader Support

Enable with environment variable:
```bash
INK_SCREEN_READER=true node app.js
```

Or in code:
```jsx
render(<App />, { isScreenReaderEnabled: true })
```

## Performance Considerations

- Max FPS default is 30
- Set lower for reduced CPU usage
- Use React.memo for expensive components
- Memoize callbacks with useCallback
- Avoid unnecessary state updates
- Use Static for immutable content

## Terminal Compatibility

- **TTY Detection** - Check if connected to terminal
- **Color Support** - Respects terminal capabilities
- **COLORTERM** - Set `COLORTERM=truecolor` for 24-bit colors
- **Raw Mode** - Automatically handled by Ink
- **Alternate Screen** - Can use with `experimental` flags

## Common Patterns

### Menu Selection
Combine useState + useInput with map rendering

### Progress Bar
Update state with timer, render progress bars with styled text

### Form Input
Track input state with useInput, validate on submit

### Logging
Use Static for completed output, update dynamic content separately

### Async Operations
Use useEffect for API calls, update state on completion

## Known Limitations

- Mouse input not supported (keyboard-only)
- Limited color support on some terminals
- Terminal size changes require re-measurement
- No true graphics/images (limited to text)
- TTY detection may fail in some environments

## Best Practices Summary

1. Use components for reusability
2. Leverage React hooks (useState, useEffect)
3. Handle keyboard input gracefully
4. Test with ink-testing-library
5. Use Static for logs
6. Enable React DevTools for debugging
7. Consider terminal compatibility
8. Memoize expensive operations
9. Handle graceful shutdown
10. Keyboard-only navigation
