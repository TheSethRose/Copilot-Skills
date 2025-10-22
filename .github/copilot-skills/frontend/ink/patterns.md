# Ink - Common Patterns

Quick reference for common Ink patterns and code examples.

## Pattern 1: Interactive Menu Selection

```jsx
import React, { useState } from 'react';
import { render, Text, Box } from 'ink';

const Menu = ({ items = ['Option 1', 'Option 2', 'Option 3'], onSelect }) => {
  const [selected, setSelected] = useState(0);

  const { stdin } = require('process');
  stdin.setRawMode(true);
  
  useInput((input, key) => {
    if (key.upArrow && selected > 0) setSelected(selected - 1);
    if (key.downArrow && selected < items.length - 1) setSelected(selected + 1);
    if (input === '\r') onSelect(items[selected]);
  });

  return (
    <Box flexDirection="column">
      {items.map((item, i) => (
        <Text key={i} color={i === selected ? 'cyan' : 'white'}>
          {i === selected ? '> ' : '  '}{item}
        </Text>
      ))}
    </Box>
  );
};
```

---

## Pattern 2: Progress Bar

```jsx
import React, { useState, useEffect } from 'react';
import { render, Text, Box } from 'ink';

const ProgressBar = ({ max = 100 }) => {
  const [current, setCurrent] = useState(0);

  useEffect(() => {
    if (current < max) {
      setTimeout(() => setCurrent(current + 1), 100);
    }
  }, [current, max]);

  const percentage = Math.floor((current / max) * 100);
  const filled = Math.floor(percentage / 5);
  const empty = 20 - filled;

  return (
    <Box>
      <Text>Progress: </Text>
      <Text color="green">{'█'.repeat(filled)}</Text>
      <Text color="gray">{'░'.repeat(empty)}</Text>
      <Text> {percentage}%</Text>
    </Box>
  );
};
```

---

## Pattern 3: Text Input Form

```jsx
import React, { useState } from 'react';
import { render, Text, Box } from 'ink';
import { useInput } from 'ink';

const TextInput = ({ prompt = 'Enter text: ', onSubmit }) => {
  const [input, setInput] = useState('');
  const [submitted, setSubmitted] = useState(false);

  useInput((input, key) => {
    if (input === '\r') {
      setSubmitted(true);
      onSubmit(input);
    } else if (key.backspace) {
      setInput(i => i.slice(0, -1));
    } else if (input && !/[\x00-\x1F\x7F]/.test(input)) {
      setInput(i => i + input);
    }
  });

  return (
    <Text>
      {prompt}
      <Text color="cyan">{input}</Text>
      {submitted && <Text color="green"> ✓</Text>}
    </Text>
  );
};
```

---

## Pattern 4: Spinner/Loading Indicator

```jsx
import React, { useState, useEffect } from 'react';
import { render, Text } from 'ink';

const Spinner = ({ message = 'Loading' }) => {
  const [frame, setFrame] = useState(0);
  const spinnerFrames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'];

  useEffect(() => {
    const timer = setInterval(() => {
      setFrame(f => (f + 1) % spinnerFrames.length);
    }, 80);
    return () => clearInterval(timer);
  }, []);

  return <Text>{spinnerFrames[frame]} {message}</Text>;
};
```

---

## Pattern 5: Tab Navigation

```jsx
import React, { useState } from 'react';
import { render, Text, Box } from 'ink';
import { useInput, useFocus } from 'ink';

const TabbedView = ({ tabs = ['Tab 1', 'Tab 2', 'Tab 3'] }) => {
  const [active, setActive] = useState(0);

  useInput((input, key) => {
    if (key.leftArrow && active > 0) setActive(active - 1);
    if (key.rightArrow && active < tabs.length - 1) setActive(active + 1);
  });

  return (
    <Box flexDirection="column">
      <Box>
        {tabs.map((tab, i) => (
          <Text key={i} color={i === active ? 'cyan' : 'gray'}>
            {i === active ? `[${tab}]` : ` ${tab} `}
          </Text>
        ))}
      </Box>
      <Box borderStyle="single" borderColor="gray" padding={1}>
        <Text>Content for {tabs[active]}</Text>
      </Box>
    </Box>
  );
};
```

---

## Pattern 6: Responsive Layout

```jsx
import React, { useState, useEffect, useRef } from 'react';
import { render, Box, Text, measureElement } from 'ink';

const ResponsiveBox = () => {
  const ref = useRef();
  const [dimensions, setDimensions] = useState({ width: 0, height: 0 });

  useEffect(() => {
    const { width, height } = measureElement(ref.current);
    setDimensions({ width, height });
  }, []);

  return (
    <Box ref={ref} width="100%" flexDirection="column">
      <Text>Width: {dimensions.width}, Height: {dimensions.height}</Text>
    </Box>
  );
};
```

---

## Pattern 7: List with Scrolling

```jsx
import React, { useState } from 'react';
import { render, Text, Box } from 'ink';
import { useInput } from 'ink';

const ScrollableList = ({ items = [], pageSize = 5 }) => {
  const [offset, setOffset] = useState(0);

  useInput((input, key) => {
    if (key.upArrow && offset > 0) setOffset(offset - 1);
    if (key.downArrow && offset < items.length - pageSize) setOffset(offset + 1);
  });

  const visibleItems = items.slice(offset, offset + pageSize);

  return (
    <Box flexDirection="column">
      {visibleItems.map((item, i) => (
        <Text key={i}>{item}</Text>
      ))}
      <Text dimmed>↑↓ to scroll • {offset + 1} of {items.length}</Text>
    </Box>
  );
};
```

---

## Pattern 8: Confirmation Dialog

```jsx
import React, { useState } from 'react';
import { render, Text, Box } from 'ink';
import { useInput } from 'ink';

const ConfirmDialog = ({ message = 'Continue?', onConfirm, onCancel }) => {
  const [confirmed, setConfirmed] = useState(null);

  useInput((input) => {
    if (input === 'y' || input === 'Y') {
      setConfirmed(true);
      onConfirm();
    } else if (input === 'n' || input === 'N') {
      setConfirmed(false);
      onCancel();
    }
  });

  return (
    <Box>
      <Text>{message} </Text>
      <Text bold color={confirmed === true ? 'green' : 'white'}>
        Y
      </Text>
      <Text>/</Text>
      <Text bold color={confirmed === false ? 'red' : 'white'}>
        N
      </Text>
    </Box>
  );
};
```

---

## Pattern 9: Status Box

```jsx
import React from 'react';
import { render, Text, Box } from 'ink';

const StatusBox = ({ status = 'pending', message = 'Processing' }) => {
  const colors = {
    pending: 'yellow',
    loading: 'blue',
    success: 'green',
    error: 'red'
  };

  const icons = {
    pending: '⏳',
    loading: '⌛',
    success: '✓',
    error: '✗'
  };

  return (
    <Box borderStyle="round" borderColor={colors[status]} padding={1}>
      <Text color={colors[status]}>
        {icons[status]} {message}
      </Text>
    </Box>
  );
};
```

---

## Pattern 10: Multi-Column Layout

```jsx
import React from 'react';
import { render, Text, Box, Spacer } from 'ink';

const MultiColumn = ({ data = [] }) => {
  return (
    <Box flexDirection="column">
      {data.map((row, i) => (
        <Box key={i}>
          <Text width={20}>{row.name}</Text>
          <Spacer />
          <Text>{row.value}</Text>
        </Box>
      ))}
    </Box>
  );
};
```

---

## Pattern 11: Error Handling

```jsx
import React, { useState } from 'react';
import { render, Text, Box } from 'ink';
import { useApp } from 'ink';

const ErrorHandler = ({ error, onRetry }) => {
  const { exit } = useApp();

  return (
    <Box flexDirection="column">
      <Text color="red" bold>Error:</Text>
      <Text color="red">{error.message}</Text>
      <Box marginTop={1}>
        <Text>(R)etry • (Q)uit</Text>
      </Box>
    </Box>
  );
};
```

---

## Pattern 12: Async Data Loading

```jsx
import React, { useState, useEffect } from 'react';
import { render, Text, Box } from 'ink';

const DataLoader = ({ url }) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(url)
      .then(r => r.json())
      .then(data => {
        setData(data);
        setLoading(false);
      })
      .catch(err => {
        setError(err.message);
        setLoading(false);
      });
  }, [url]);

  if (loading) return <Text>Loading...</Text>;
  if (error) return <Text color="red">Error: {error}</Text>;
  return <Text>{JSON.stringify(data, null, 2)}</Text>;
};
```

---

## Key Takeaways

1. **Always use hooks** for state management
2. **Handle keyboard input** with useInput
3. **Measure elements** for responsive layouts
4. **Use Static** for logs and completed output
5. **Combine Box + Text** for layouts and styling
6. **Test with ink-testing-library** before deployment
7. **Debug with React DevTools** (DEV=true)
8. **Consider terminal compatibility** for colors
9. **Handle graceful shutdown** with useApp().exit()
10. **Keyboard-only navigation** - no mouse support
