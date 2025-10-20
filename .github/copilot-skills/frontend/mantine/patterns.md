# Mantine - Common Patterns

Quick reference for common mantine patterns and usage.

## Code Patterns

### 1. Getting started Get started with a template The easiest way to get started is to use one of the temp

```
@mantine/core
```

### 2. Getting started Get started with a template The easiest way to get started is to use one of the temp

```
@mantine/core
```

### 3. Getting started Get started with a template The easiest way to get started is to use one of the temp

```
@mantine/core
```

### 4. To get started with a template, open it on GitHub and click "Use this template" button. In order to 

```
@mantine/hooks
```

### 5. DocumentationPropsStyles APIUsage Accordion allows users to expand and collapse sections of content.

```
import { Accordion } from '@mantine/core';
import { data } from './data';

function Demo() {
  const items = data.map((item) => (
    <Accordion.Item key={item.value} value={item.value}>
      <Accordion.Control icon={item.emoji}>{item.value}</Accordion.Control>
      <Accordion.Panel>{item.descript
```

### 6. DocumentationPropsStyles APIUsage Accordion allows users to expand and collapse sections of content.

```
import { Accordion } from '@mantine/core';
import { data } from './data';

function Demo() {
  const items = data.map((item) => (
    <Accordion.Item key={item.value} value={item.value}>
      <Accordion.Control icon={item.emoji}>{item.value}</Accordion.Control>
      <Accordion.Panel>{item.descript
```

### 7. Usage Accordion allows users to expand and collapse sections of content. It helps manage large amoun

```
import { Accordion } from '@mantine/core';
import { data } from './data';

function Demo() {
  const items = data.map((item) => (
    <Accordion.Item key={item.value} value={item.value}>
      <Accordion.Control icon={item.emoji}>{item.value}</Accordion.Control>
      <Accordion.Panel>{item.descript
```

### 8. Usage Accordion allows users to expand and collapse sections of content. It helps manage large amoun

```
import { Accordion } from '@mantine/core';
import { data } from './data';

function Demo() {
  const items = data.map((item) => (
    <Accordion.Item key={item.value} value={item.value}>
      <Accordion.Control icon={item.emoji}>{item.value}</Accordion.Control>
      <Accordion.Panel>{item.descript
```

## Examples

### Example 1

```python
import { ActionIcon } from '@mantine/core';
import { IconAdjustments } from '@tabler/icons-react';

function Demo() {
  return (
    <ActionIcon variant="filled" aria-label="Settings">
      <IconAdjustments style={{ width: '70%', height: '70%' }} stroke={1.5} />
    </ActionIcon>
  );
}
```

### Example 2

```python
import { ActionIcon } from '@mantine/core';
import { IconHeart } from '@tabler/icons-react';

function Demo() {
  return (
    <ActionIcon
      variant="gradient"
      size="xl"
      aria-label="Gradient action icon"
      gradient={{ from: 'blue', to: 'cyan', deg: 90 }}
    >
      <IconHeart />
    </ActionIcon>
  );
}
```

### Example 3

```python
import { Alert } from '@mantine/core';
import { IconInfoCircle } from '@tabler/icons-react';

function Demo() {
  const icon = <IconInfoCircle />;
  return (
    <Alert variant="light" color="blue" title="Alert title" icon={icon}>
      Lorem ipsum dolor sit, amet consectetur adipisicing elit. At officiis, quae tempore necessitatibus placeat saepe.
    </Alert>
  );
}
```

### Example 4

```python
import { AngleSlider } from '@mantine/core';

function Demo() {
  return <AngleSlider aria-label="Angle slider" size={60} thumbSize={8} />;
}
```

### Example 5

```python
import { useState } from 'react';
import { AngleSlider } from '@mantine/core';

function Demo() {
  const [value, setValue] = useState(180);
  return <AngleSlider value={value} onChange={setValue} />;
}
```

### Example 6

```python
import { Autocomplete } from '@mantine/core';

function Demo() {
  return (
    <Autocomplete
      label="Your favorite library"
      placeholder="Pick value or enter anything"
      data={['React', 'Angular', 'Vue', 'Svelte']}
    />
  );
}
```

### Example 7

```python
import { useState } from 'react';
import { Autocomplete } from '@mantine/core';

function Demo() {
  const [value, setValue] = useState('');
  return <Autocomplete data={[]} value={value} onChange={setValue} />;
}
```

### Example 8

```python
import { Avatar, Group } from '@mantine/core';

const names = [
  'John Doe',
  'Jane Mol',
  'Alex Lump',
  'Sarah Condor',
  'Mike Johnson',
  'Kate Kok',
  'Tom Smith',
];

function Demo() {
  const avatars = names.map((name) => <Avatar key={name} name={name} color="initials" />);
  return <Group>{avatars}</Group>;
}
```

### Example 9

```python
import { BackgroundImage } from '@mantine/core';

function Demo() {
  return <BackgroundImage component="button" />;
}
```

### Example 10

```python
import { Badge } from '@mantine/core';

function Demo() {
  return <Badge color="blue">Badge</Badge>;
}
```


## Categories

See organized documentation in `references/`:

- `references/components.md` - Components
- `references/getting_started.md` - Getting Started
- `references/hooks.md` - Hooks
- `references/other.md` - Other
- `references/theming.md` - Theming
