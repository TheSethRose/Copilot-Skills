# Mantine - Hooks

**Pages**: 6

---

## use-focus-trap | Mantine

**URL**: https://mantine.dev/hooks/use-focus-trap/

**Contents**:
- use-focus-trap
- Usage
- API
- Combine with other ref based hooks
- Initial focus
- Definition

Traps focus inside given element

use-focus-trap traps focus at the given node, for example in modal, drawer or menu. Node must include at least one focusable element. When the node unmounts, the focus trap is automatically released.

The hook accepts focus trap active state as a single argument:

The hook returns ref that should be passed to the element:

To combine use-focus-trap with other ref based hooks, use use-merged-ref hook:

By default, focus trap will move focus to the first interactive element. To specify the element that should receive initial focus, add data-autofocus attribute:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { useFocusTrap } from '@mantine/hooks';

function Demo() {
  const focusTrapRef = useFocusTrap();

  return (
    <div ref={focusTrapRef}>
      <input />
    </div>
  );
}
```

```python
import { useFocusTrap } from '@mantine/hooks';

useFocusTrap(); // -> focus trap inactive
useFocusTrap(true); // -> focus trap active

useFocusTrap(false); // -> focus trap disabled
```

```python
import { Paper } from '@mantine/core';
import { useFocusTrap } from '@mantine/hooks';

function Demo() {
  const focusTrapRef = useFocusTrap();

  return (
    <>
      {/* With regular element: */}
      <div ref={focusTrapRef} />

      {/* With Mantine component: */}
      <Paper ref={focusTrapRef} />
    </>
  );
}
```

---

## use-hotkeys | Mantine

**URL**: https://mantine.dev/hooks/use-hotkeys/

**Contents**:
- use-hotkeys
- Usage
- Targeting elements
- Supported formats
- Types
- Definition
- Exported types

Listen for keys combinations on document element

use-hotkeys accepts as its first argument an array of hotkeys and handler tuples:

The second argument is a list of HTML tags on which hotkeys should be ignored. By default, hotkeys events are ignored if the focus is in input, textarea and select elements.

use-hotkeys hook can work only with document element, you will need to create your own event listener if you need to support other elements. For this purpose, @mantine/hooks package exports getHotkeyHandler function which should be used with onKeyDown:

With getHotkeyHandler you can also add events to any dom node using .addEventListener:

@mantine/hooks exports HotkeyItemOptions and HotkeyItem types:

HotkeyItemOptions provides the usePhysicalKeys option to force the physical key assignment. Useful for non-QWERTY keyboard layouts.

HotkeyItem type can be used to create hotkey items outside of use-hotkeys hook:

HotkeyItemOptions and HotkeyItem types are exported from @mantine/hooks package, you can import them in your application:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { useHotkeys } from '@mantine/hooks';
import { spotlight } from '@mantine/spotlight';
import { useMantineColorScheme } from '@mantine/core';
import { Shortcut } from './Shortcut';

function Demo() {
  const { toggleColorScheme } = useMantineColorScheme();

  useHotkeys([
    ['mod + K', () => spotlight.open()],
    ['mod + J', () => toggleColorScheme()],
    ['mod + shift + alt + X', () => secret()],
  ]);

  return (
    <>
      <Shortcut symbol="K" description="Open search" />
      <S
...
```

```python
import { useHotkeys } from '@mantine/hooks';

function Demo() {
  // Ignore hotkeys events only when focus is in input and textarea elements
  useHotkeys(
    [['ctrl+K', () => console.log('Trigger search')]],
    ['INPUT', 'TEXTAREA']
  );

  // Empty array – do not ignore hotkeys events on any element
  useHotkeys([['ctrl+K', () => console.log('Trigger search')]], []);
}
```

```python
import { useState } from 'react';
import { getHotkeyHandler } from '@mantine/hooks';
import { notifications } from '@mantine/notifications';
import { TextInput } from '@mantine/core';

function Demo() {
  const [value, setValue] = useState("I've just used a hotkey to send a message");
  const handleSubmit = () => notifications.show({ title: 'Your message', message: value });
  const handleSave = () => notifications.show({ title: 'You saved', color: 'teal', message: value });

  return (
    <Tex
...
```

---

## use-long-press | Mantine

**URL**: https://mantine.dev/hooks/use-long-press/

**Contents**:
- use-long-press
- Usage
- Definition
- Exported types

Call function on long press

UseLongPressOptions and UseLongPressReturnValue types are exported from @mantine/hooks package, you can import them in your application:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Button } from '@mantine/core';
import { useLongPress } from '@mantine/hooks';
import { notifications } from '@mantine/notifications';

function Demo() {
  const handlers = useLongPress(() => notifications.show({ message: 'Long press triggered' }));
  return <Button {...handlers}>Press and hold</Button>;
}
```

```javascript
interface UseLongPressOptions {
  /** Time in milliseconds to trigger the long press, default is 400ms */
  threshold?: number;

  /** Callback triggered when the long press starts */
  onStart?: (event: React.MouseEvent | React.TouchEvent) => void;

  /** Callback triggered when the long press finishes */
  onFinish?: (event: React.MouseEvent | React.TouchEvent) => void;

  /** Callback triggered when the long press is canceled */
  onCancel?: (event: React.MouseEvent | React.TouchEvent) => voi
...
```

```python
import type { UseLongPressOptions, UseLongPressReturnValue } from '@mantine/hooks';
```

---

## use-media-query | Mantine

**URL**: https://mantine.dev/hooks/use-media-query/

**Contents**:
- use-media-query
- Usage
- Server Side Rendering
- Definition
- Exported types

Subscribes to media queries with window.matchMedia

use-media-query subscribes to media queries. It receives a media query as an argument and returns true if the given media query matches the current state. The hook relies on window.matchMedia() API and will return false if the API is not available, unless an initial value is provided in the second argument.

Resize browser window to trigger window.matchMedia event:

During server side rendering the hook will always return false as window.matchMedia api is not available, if that is not a desired behavior, you can override the initial value:

UseMediaQueryOptions type is exported from @mantine/hooks package, you can import it in your application:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Badge } from '@mantine/core';
import { useMediaQuery } from '@mantine/hooks';

function Demo() {
  const matches = useMediaQuery('(min-width: 56.25em)');

  return (
    <Badge color={matches ? 'teal' : 'red'} variant="filled">
      Breakpoint {matches ? 'matches' : 'does not match'}
    </Badge>
  );
}
```

```python
import { useMediaQuery } from '@mantine/hooks';

function Demo() {
  // Set initial value in second argument and getInitialValueInEffect option to false
  const matches = useMediaQuery('(max-width: 40em)', true, {
    getInitialValueInEffect: false,
  });
}
```

```javascript
interface UseMediaQueryOptions {
  getInitialValueInEffect: boolean;
}

function useMediaQuery(
  query: string,
  initialValue?: boolean,
  options?: UseMediaQueryOptions,
): boolean;
```

---

## use-mouse | Mantine

**URL**: https://mantine.dev/hooks/use-mouse/

**Contents**:
- use-mouse
- Usage
- API
- Definition

Tracks mouse position over the viewport or given element

Mouse coordinates { x: 0, y: 0 }

If you do not provide ref, mouse position is tracked relative to the document element:

Mouse coordinates { x: 0, y: 0 }

Set resetOnExit option to reset mouse position to 0, 0 when mouse leaves the element:

The hook returns an object with ref and x, y mouse coordinates:

On the first render (as well as during SSR), both x and y values are equal to 0.

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Text, Code, Group, Box } from '@mantine/core';
import { useMouse } from '@mantine/hooks';

function Demo() {
  const { ref, x, y } = useMouse();

  return (
    <>
      <Group justify="center">
        <Box ref={ref} w={300} h={180} bg="var(--mantine-color-blue-light)" />
      </Group>
      <Text ta="center">
        Mouse coordinates <Code>{`{ x: ${x}, y: ${y} }`}</Code>
      </Text>
    </>
  );
}
```

```python
import { Text, Code } from '@mantine/core';
import { useMouse } from '@mantine/hooks';

function Demo() {
  const { x, y } = useMouse();

  return (
    <Text ta="center">
      Mouse coordinates <Code>{`{ x: ${x}, y: ${y} }`}</Code>
    </Text>
  );
}
```

```python
import { useMouse } from '@mantine/hooks';

const { ref, x, y } = useMouse({ resetOnExit: true });
```

---

## use-pagination | Mantine

**URL**: https://mantine.dev/hooks/use-pagination/

**Contents**:
- use-pagination
- Usage
- Controlled
- Siblings
- Boundaries
- Definition
- Exported types

Manages pagination state

use-pagination is a state management hook for Pagination component, it manages pagination with controlled and uncontrolled state:

The hook supports controlled mode, provide page and onChange props to manage state from outside:

Control number of active item siblings with siblings:

Control number of items on each boundary with boundaries:

UsePaginationOptions and UsePaginationReturnValue types are exported from @mantine/hooks package, you can import them in your application:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { usePagination } from '@mantine/hooks';

const pagination = usePagination({ total: 10, initialPage: 1 });

pagination.range; // -> [1, 2, 3, 4, 5, 'dots', 10];

pagination.setPage(5);
pagination.range; // -> [1, 'dots', 4, 5, 6, 'dots', 10];

pagination.next();
pagination.range; // -> [1, 'dots', 5, 6, 7, 'dots', 10];

pagination.previous();
pagination.range; // -> [1, 'dots', 4, 5, 6, 'dots', 10];

pagination.last();
pagination.range; // -> [1, 'dots', 6, 7, 8, 9, 10];

pagination.first
...
```

```python
import { useState } from 'react';
import { usePagination } from '@mantine/hooks';

const [page, onChange] = useState(1);
const pagination = usePagination({ total: 10, page, onChange });

// Will call onChange with 5
pagination.setPage(5);
pagination.range; // -> [1, 'dots', 4, 5, 6, 'dots', 10];

// ... All other examples work the same
```

```python
import { usePagination } from '@mantine/hooks';

const pagination = usePagination({ total: 20, siblings: 3 });
```

---
