---
description: Ink - React for CLIs. Build interactive command-line applications with React components.
---

# Ink

**Purpose**: Ink is React for CLIs - build interactive command-line applications using familiar React component patterns.

## When to Use This Skill

Use this skill when:
- Building CLI applications with interactive UIs
- Creating React-based command-line tools
- Need Flexbox layouts in the terminal
- Building interactive prompts, dashboards, or interactive CLIs
- Developing tools that need component-based structure

**Keywords**: ink, cli, react, terminal, command-line, interactive, components

## Quick Start

### 1. Install

```bash
npm install ink react
```

### 2. Create Your First Component

```jsx
import React from 'react';
import { render, Text } from 'ink';

const App = () => <Text color="green">Hello from Ink!</Text>;

render(<App />);
```

### 3. Run It

```bash
node app.js
```

## Core Components

### `<Text>`
Renders text output with styling options.

```jsx
<Text color="blue" bold underline>
  Styled Text
</Text>
```

**Props**: `color`, `backgroundColor`, `bold`, `italic`, `underline`, `strikethrough`, `dimmed`, `inverse`, `wrap`

---

### `<Box>`
Container component for layout using Flexbox.

```jsx
<Box flexDirection="column" padding={1}>
  <Text>Left</Text>
  <Text>Right</Text>
</Box>
```

**Props**: `flexDirection`, `alignItems`, `justifyContent`, `width`, `height`, `minWidth`, `minHeight`, `padding`, `paddingX`, `paddingY`, `margin`, `marginX`, `marginY`, `borderStyle`, `borderColor`

---

### `<Newline>`
Renders a newline character.

```jsx
<>
  <Text>Line 1</Text>
  <Newline />
  <Text>Line 2</Text>
</>
```

---

### `<Spacer>`
Fills available space between components.

```jsx
<Box>
  <Text>Left</Text>
  <Spacer />
  <Text>Right</Text>
</Box>
```

---

### `<Static>`
Renders content once and freezes it.

```jsx
<Static items={logs}>
  {(log) => <Text>{log}</Text>}
</Static>
```

---

### `<Transform>`
Transform output with a custom function.

```jsx
<Transform transform={(str) => str.toUpperCase()}>
  <Text>hello</Text>
</Transform>
```

## Hooks

### `useInput(inputHandler, options)`
Handle keyboard input in your CLI.

```jsx
const [isRunning, setIsRunning] = useState(true);

useInput((input, key) => {
  if (input === 'q') setIsRunning(false);
  if (key.upArrow) moveUp();
});
```

---

### `useApp()`
Get access to the Ink app instance.

```jsx
const { exit } = useApp();

// Exit the app
exit();
```

---

### `useStdin()`
Access stdin stream information.

```jsx
const { isRawMode, isTTY } = useStdin();
```

---

### `useStdout()`
Access stdout stream.

```jsx
const { stdout, write } = useStdout();
```

---

### `useStderr()`
Access stderr stream for error output.

```jsx
const { stderr, write } = useStderr();
```

---

### `useFocus(options)`
Manage focus for components.

```jsx
const { isFocused } = useFocus({ autoFocus: true });

return <Box borderStyle={isFocused ? 'double' : 'single'}>;
```

---

### `useFocusManager()`
Manage focus between multiple components.

```jsx
const { focus, focusNext, focusPrevious } = useFocusManager();

useEffect(() => {
  focus('input-1');
}, []);
```

## API Methods

### `render(tree, options)`
Render your Ink app.

```jsx
const { rerender, unmount, waitUntilExit, clear } = render(<App />);
```

**Options**: `stdout`, `stderr`, `stdin`, `exitOnCtrlC`, `patchConsole`, `debug`, `experimental_useStdoutFallback`, `maxFps`

---

### `measureElement(ref)`
Measure dimensions of a `<Box>` element.

```jsx
const ref = useRef();
const { width, height } = measureElement(ref.current);
```

## Common Patterns

### Pattern 1: Interactive Menu

```jsx
const [selected, setSelected] = useState(0);
const items = ['Option 1', 'Option 2', 'Option 3'];

useInput((input, key) => {
  if (key.upArrow) setSelected(Math.max(0, selected - 1));
  if (key.downArrow) setSelected(Math.min(items.length - 1, selected + 1));
  if (input === '\r') handleSelect(items[selected]);
});

return items.map((item, i) => (
  <Text key={i} color={i === selected ? 'cyan' : 'white'}>
    {i === selected ? '> ' : '  '}{item}
  </Text>
));
```

### Pattern 2: Progress Display

```jsx
const [progress, setProgress] = useState(0);

useEffect(() => {
  const timer = setInterval(() => {
    setProgress(p => (p < 100 ? p + 1 : p));
  }, 100);
  return () => clearInterval(timer);
}, []);

return (
  <Box>
    <Text>Loading: </Text>
    <Text color="green">{'█'.repeat(Math.floor(progress / 5))}</Text>
    <Text dimmed>{'░'.repeat(20 - Math.floor(progress / 5))}</Text>
    <Text> {progress}%</Text>
  </Box>
);
```

### Pattern 3: Form Input

```jsx
const [input, setInput] = useState('');

useInput((input) => {
  if (input === '\r') submitForm();
  else if (input === '\u0008') setInput(i => i.slice(0, -1));
  else setInput(i => i + input);
});

return <Text>Enter value: {input}</Text>;
```

## Styling

Ink supports terminal colors and styles:

**Colors**: `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`, `gray`, `redBright`, `greenBright`, `yellowBright`, `blueBright`, `magentaBright`, `cyanBright`, `whiteBright`

**Styles**: `bold`, `italic`, `underline`, `strikethrough`, `inverse`, `dimmed`

## Layout

Ink uses Flexbox for layouts:

```jsx
<Box flexDirection="row" justifyContent="space-between">
  <Text>Left</Text>
  <Text>Right</Text>
</Box>
```

**Properties**: `flexDirection`, `alignItems`, `justifyContent`, `width`, `height`, `minWidth`, `minHeight`, `padding`, `margin`, `borderStyle`

## Testing

Use `ink-testing-library` for testing Ink components:

```bash
npm install --save-dev ink-testing-library
```

```jsx
import { render } from 'ink-testing-library';

const { lastFrame } = render(<YourComponent />);
expect(lastFrame()).toContain('Expected output');
```

## Popular Apps Built with Ink

- **OpenAI Codex** - Agentic coding tool by OpenAI
- **Cloudflare Wrangler** - CLI for Cloudflare Workers
- **Prisma CLI** - Database toolkit CLI
- **Shopify CLI** - Build for Shopify
- **GitHub Copilot CLI** - Copilot in the shell
- **Linear CLI** - Internal deployment management
- **Gatsby CLI** - Web framework CLI

## Best Practices

✅ **Do:**
- Use components for reusability
- Leverage React hooks for state management
- Handle keyboard input with `useInput`
- Test with `ink-testing-library`
- Use `<Static>` for logs and completed output
- Enable React DevTools with `DEV=true` for debugging

❌ **Don't:**
- Avoid excessive re-renders with proper memoization
- Don't block with synchronous operations
- Avoid mixing stdout/stderr output without context

## Reference Documentation

For detailed information and examples, check:
- [Ink GitHub Repository](https://github.com/vadimdemedes/ink)
- [ink-testing-library](https://github.com/vadimdemedes/ink-testing-library)
- [React Documentation](https://reactjs.org) - All React features work in Ink!

## Related Skills

- `/react` - React fundamentals
- `/nodejs` - Node.js development
- `/typescript` - TypeScript in CLI apps

## More Information

- **Repository**: https://github.com/vadimdemedes/ink
- **NPM Package**: https://npmjs.com/package/ink
- **Latest Version**: Check package.json for current version
