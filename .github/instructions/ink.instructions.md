# Ink - Auto-Loaded Instructions

**Auto-loads for:** `**/*.js`, `**/*.jsx`, `**/*.ts`, `**/*.tsx` (CLI-related files)

## Default Behaviors

When working with Ink CLI projects, this skill provides:
- Quick component reference
- Hook patterns for state and input handling
- Layout and styling guidance
- Testing strategies

## Common Patterns

### Building an Interactive Menu

When creating selection interfaces:
```jsx
const [selected, setSelected] = useState(0);

useInput((input, key) => {
  if (key.upArrow) setSelected(Math.max(0, selected - 1));
  if (key.downArrow) setSelected(Math.min(items.length - 1, selected + 1));
});

return items.map((item, i) => (
  <Text key={i} color={i === selected ? 'cyan' : 'white'}>
    {i === selected ? '> ' : '  '}{item}
  </Text>
));
```

### Creating Responsive Layouts

Use `measureElement` to adapt to terminal size:
```jsx
const ref = useRef();
const [width, setWidth] = useState(0);

useEffect(() => {
  const { width: measuredWidth } = measureElement(ref.current);
  setWidth(measuredWidth);
}, []);

return <Box ref={ref} width="100%">{/* content */}</Box>;
```

### Rendering Progress/Loading

For long-running operations:
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
    <Text>Progress: </Text>
    <Text color="green">{'█'.repeat(progress / 5)}</Text>
  </Box>
);
```

## Quality Guidelines

### Code Style
- Use functional components with hooks
- Keep components focused and reusable
- Proper TypeScript types for CLI apps
- Handle keyboard input gracefully

### Accessibility
- Support screen readers (enable with `INK_SCREEN_READER=true`)
- Provide keyboard navigation
- Clear visual feedback for selections
- Support common key bindings

### Performance
- Avoid excessive re-renders (use React DevTools)
- Use `<Static>` for completed output
- Limit `maxFps` for heavy components
- Memoize callback functions

## Testing Workflow

1. Write component logic
2. Test with `ink-testing-library`
3. Use `DEV=true` with React DevTools
4. Test keyboard input with real terminal
5. Verify on various terminal sizes

## Common Issues & Solutions

**Issue**: Component re-renders too frequently
**Solution**: Use `React.memo()` or `useCallback()` for optimization

**Issue**: Keyboard input not working
**Solution**: Ensure `useInput` is called and terminal is in raw mode

**Issue**: Layout looks wrong on different terminals
**Solution**: Use `measureElement()` and responsive widths

**Issue**: Colors not showing
**Solution**: Check terminal capabilities, may need `COLORTERM=truecolor`

## Best Practices

✅ **Use `<Static>` for logs** - Prevents flashing content
✅ **Handle `exitOnCtrlC`** - Graceful shutdown
✅ **Test with multiple terminal sizes**
✅ **Use React Devtools for debugging** (`DEV=true`)
✅ **Keyboard-only navigation** - No mouse support in CLI

❌ **Avoid blocking operations** - Use async/await properly
❌ **Don't mix stdout/stderr** - Can cause output issues
❌ **Avoid excessive re-renders** - Check React Devtools
