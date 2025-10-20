# Storybook - Common Patterns

Quick reference for common storybook patterns and usage.

## Code Patterns

### 1. Frameworks are packages that auto-configure Storybook to work with most common environment setups. T

```
./storybook/main.js|ts|cjs
```

### 2. Use the Storybook CLI to install it in a single command. Run this inside your project’s root directo

```
npm create storybook@latest
```

### 3. For either command, you can specify either an npm tag such as latest or next, or a (partial) version

```
latest
```

### 4. If all goes well, you should see a setup wizard that will help you get started with Storybook introd

```
?path=/onboarding
```

### 5. The Storybook CLI includes support for the industry's popular package managers (e.g., Yarn, npm, and

```
--package-manager
```

### 6. If you're working with a custom environment setup or need to set up Storybook manually, you can use 

```
--type
```

### 7. Storybook has hundreds of reusable addons packaged as NPM modules. Let's walk through how to extend 

```
storybook add
```

### 8. Storybook has hundreds of reusable addons packaged as NPM modules. Let's walk through how to extend 

```
storybook add
```

## Examples

### Example 1

```typescript
components/
├─ Button/
│  ├─ Button.js | ts | jsx | tsx | vue | svelte
│  ├─ Button.stories.js | ts | jsx | tsx | svelte
```

### Example 2

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
import type { Meta } from '@storybook/your-framework';
 
import { Button } from './Button';
 
const meta = {
  component: Button,
} satisfies Meta<typeof Button>;
 
export default meta;
```

### Example 3

```python
import { v4 as uuidv4 } from 'uuid';
import { getUserFromSession } from '../lib/session';
 
export function AuthButton() {
  const user = getUserFromSession();
  const id = uuidv4();
 
  return (
    <button onClick={() => { console.log(`User: ${user.name}, ID: ${id}`) }}>
      {user ? `Welcome, ${user.name}` : 'Sign in'}
    </button>
  );
}
```

### Example 4

```python
import { sb } from 'storybook/test';
 
// 👇 Automatically spies on all exports from the `lib/session` local module
sb.mock(import('../lib/session.ts'), { spy: true });
// 👇 Automatically spies on all exports from the `uuid` package in `node_modules`
sb.mock(import('uuid'), { spy: true });
 
// ...rest of the file
```

### Example 5

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Preview } from '@storybook/your-framework';
 
const preview: Preview = {
  // ...rest of preview
  //👇 Enables auto-generated documentation for all stories
  tags: ['autodocs'],
};
 
export default preview;
```

### Example 6

```python
import { Title, Subtitle, Description, Primary, Controls, Stories } from '@storybook/addon-docs/blocks';
 
export const autoDocsTemplate = () => (
  <>
    <Title />
    <Subtitle />
    <Description />
    <Primary />
    <Controls />
    <Stories />
  </>
);
```

### Example 7

```python
import { Canvas, Meta } from '@storybook/addon-docs/blocks';
 
import * as CheckboxStories from './Checkbox.stories';
 
<Meta of={CheckboxStories} />
 
# Checkbox
 
A checkbox is a square box that can be activated or deactivated when ticked.
 
Use checkboxes to select one or more options from a list of choices.
 
<Canvas of={CheckboxStories.Unchecked} />
```

### Example 8

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
import { composeStories } from '@storybook/your-framework';
 
import * as stories from '../stories/Button.stories';
 
const { Primary } = composeStories(stories);
test('Button snapshot', async () => {
  await Primary.run();
  expect(document.body.firstChild).toMatchSnapshot();
});
```

### Example 9

```python
import { addons } from 'storybook/preview-api';
 
import { useStorybookApi } from 'storybook/manager-api';
```

### Example 10

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Preview } from '@storybook/your-framework';
 
const preview = {
  argTypes: {
    // 👇 All stories expect a label arg
    label: {
      control: 'text',
      description: 'Overwritten description',
    },
  },
} satisfies Preview;
 
export default preview;
```


## Categories

See organized documentation in `references/`:

- `references/api.md` - Api
- `references/documentation.md` - Documentation
- `references/getting_started.md` - Getting Started
- `references/other.md` - Other
- `references/testing.md` - Testing
- `references/writing_stories.md` - Writing Stories
