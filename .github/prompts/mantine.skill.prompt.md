---
description: Fully featured React component library
---

# Mantine

**Purpose**: Fully featured React component library

## When to Use This Skill

Use this skill when:
- Working with mantine projects
- Implementing mantine features
- Debugging mantine code
- Learning mantine best practices
- Building applications with mantine

**Keywords**: mantine, getting_started, components, hooks, theming, other

## Quick Reference

### Common Patterns

**1. 6.x → 7.x migration guide This guide is intended to help you migrate your projec**

```
@mantine/emotion
```

**2. 6.x → 7.x migration guide This guide is intended to help you migrate your projec**

```
@mantine/emotion
```

**3. 6.x → 7.x migration guide This guide is intended to help you migrate your projec**

```
@mantine/emotion
```

**4. Color scheme toggle example:**

```
import { ActionIcon, useMantineColorScheme, useComputedColorScheme } from '@mantine/core';
import { IconSun, IconMoon } from '@tabler/icons-react';
import cx from 'clsx';
import classes from './Demo.m
```

**5. DocumentationPropsStyles APIUsage Accordion allows users to expand and collapse **

```
import { Accordion } from '@mantine/core';
import { data } from './data';

function Demo() {
  const items = data.map((item) => (
    <Accordion.Item key={item.value} value={item.value}>
      <Accord
```

### Code Examples

**Example 1** (python):
```python
// 6.x
import { createStyles, Global } from '@mantine/core';

// 7.x
import { createStyles, Global } from '@mantine/emotion';
```

**Example 2** (python):
```python
// 6.x and 7.x, no changes
import { Box, Button } from '@mantine/core';

function Demo() {
  return (
    <>
      <Box
        sx={(theme) => ({ backgroundColor: theme.colors.red[5] })}
      />
      <Button styles={{ root: { height: 50 } }} />
   
```

**Example 3** (python):
```python
import { ActionIcon } from '@mantine/core';
import { IconAdjustments } from '@tabler/icons-react';

function Demo() {
  return (
    <ActionIcon variant="filled" aria-label="Settings">
      <IconAdjustments style={{ width: '70%', height: '70%' }} st
```

**Example 4** (python):
```python
import { AngleSlider } from '@mantine/core';

function Demo() {
  return <AngleSlider aria-label="Angle slider" size={60} thumbSize={8} />;
}
```

**Example 5** (python):
```python
import { useState } from 'react';
import { AngleSlider } from '@mantine/core';

function Demo() {
  const [value, setValue] = useState(180);
  return <AngleSlider value={value} onChange={setValue} />;
}
```

## Reference Documentation

This skill includes comprehensive documentation in `.github/copilot-skills/frontend/mantine/references/`:

- **components.md** - Components documentation
- **getting_started.md** - Getting Started documentation
- **hooks.md** - Hooks documentation
- **other.md** - Other documentation
- **theming.md** - Theming documentation

## How to Use

### For Quick Answers
Ask directly about mantine features, APIs, or patterns.

### For Detailed Information
Reference specific documentation files:
- Check `references/getting_started.md` for setup
- Check `references/api_reference.md` for API details
- Check category files for specific topics

### For Code Examples
Use the Quick Reference patterns above or ask for specific examples.

## Related Skills

- None (standalone skill)

## More Information

- **Base Documentation**: https://mantine.dev/
- **Generated**: 2025-10-19
- **Total Pages**: 148
