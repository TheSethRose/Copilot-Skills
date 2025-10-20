---
description: Component development environment and testing tool for UI components
---

# Storybook

**Purpose**: Component development environment and testing tool for UI components

## When to Use This Skill

Use this skill when:
- Working with storybook projects
- Implementing storybook features
- Debugging storybook code
- Learning storybook best practices
- Building applications with storybook

**Keywords**: storybook, getting_started, writing_stories, documentation, testing, api, other

## Quick Reference

### Common Patterns

**1. Web accessibility is the practice of making websites and apps accessible and inc**

```
npx storybook add @storybook/addon-a11y
```

**2. ℹ️Storybook's add command automates the addon's installation and setup. To insta**

```
add
```

**3. Storybook's add command automates the addon's installation and setup. To install**

```
add
```

**4. Storybook's add command automates the addon's installation and setup. To install**

```
add
```

**5. Storybook's add command automates the addon's installation and setup. To install**

```
add
```

### Code Examples

**Example 1** (python):
```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Preview } from '@storybook/your-framework';
 
const preview: Preview = {
  parameters: {
    actions: { argTypesRegex: '^on.*' },
  },

```

**Example 2** (python):
```python
import { addons } from 'storybook/preview-api';
 
import { useStorybookApi } from 'storybook/manager-api';
```

**Example 3** (javascript):
```javascript
addons.register(ADDON_ID, () => {
  addons.add(PANEL_ID, {
    type: types.PANEL,
    title: 'My Addon',
    render: () => <div>Addon tab content</div>,
    paramKey: 'myAddon', // this element
  });
});
```

**Example 4** (python):
```python
import { Meta, ArgTypes } from '@storybook/addon-docs/blocks';
import * as ButtonStories from './Button.stories';
 
<Meta of={ButtonStories} />
 
<ArgTypes of={ButtonStories} />
```

**Example 5** (python):
```python
import { ArgTypes } from '@storybook/addon-docs/blocks';
```

## Reference Documentation

This skill includes comprehensive documentation in `.github/copilot-skills/storybook/references/`:

- **api.md** - Api documentation
- **documentation.md** - Documentation documentation
- **getting_started.md** - Getting Started documentation
- **other.md** - Other documentation
- **testing.md** - Testing documentation
- **writing_stories.md** - Writing Stories documentation

## How to Use

### For Quick Answers
Ask directly about storybook features, APIs, or patterns.

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

- **Base Documentation**: https://storybook.js.org/docs/
- **Generated**: 2025-10-19
- **Total Pages**: 119
