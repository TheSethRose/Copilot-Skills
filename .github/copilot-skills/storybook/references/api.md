# Storybook - Api

**Pages**: 30

---

## Addon API

**URL**: https://storybook.js.org/docs/addons/addons-api

**Contents**:
- Addon API
- Core Addon API
  - addons.add()
  - addons.register()
  - addons.getChannel()
  - makeDecorator
- Storybook API
  - api.selectStory()

Storybook's API allows developers to interact programmatically with Storybook. With the API, developers can build and deploy custom addons and other tools that enhance Storybook's functionality.

Our API is exposed via two distinct packages, each one with a different purpose:

The add method allows you to register the type of UI component associated with the addon (e.g., panels, toolbars, tabs). For a minimum viable Storybook addon, you should provide the following arguments:

The render function is called with active. The active value will be true when the panel is focused on the UI.

Serves as the entry point for all addons. It allows you to register an addon and access the Storybook API. For example:

Now you'll get an instance to our StorybookAPI. See the api docs for Storybook API regarding using that.

Get an instance to the channel to communicate with the manager and the preview. You can find this in both the addon register code and your addon’s wrapper component (where used inside a story).

It has a NodeJS EventEmitter compatible API. So, you can use it to emit events and listen to events.

Use the makeDecorator API to create decorators in the style of the official addons. Like so:

If the story's parameters include { exampleParameter: { disable: true } } (where exampleParameter is the parameterName of your addon), your decorator will not be called.

The makeDecorator API requires the following arguments:

Storybook's API allows you to access different functionalities of Storybook UI.

The selectStory API method allows you to select a single story. It accepts the following two parameters; story kind name and an optional story name. For example:

This is how you can select the above story:

Similar to the selectStory API method, but it only accepts the story as the only parameter.

This method allows you to set query string parameters. You can use that as temporary storage for addons. Here's how you define query params:

Additionally, if you need to remove a

*[Content truncated - see full docs]*

**Examples**:

```python
import { addons } from 'storybook/preview-api';
 
import { useStorybookApi } from 'storybook/manager-api';
```

```python
import React from 'react';
 
import { addons, types } from 'storybook/manager-api';
 
import { AddonPanel } from 'storybook/internal/components';
 
const ADDON_ID = 'myaddon';
const PANEL_ID = `${ADDON_ID}/panel`;
 
addons.register(ADDON_ID, (api) => {
  addons.add(PANEL_ID, {
    type: types.PANEL,
    title: 'My Addon',
    render: ({ active }) => (
      <AddonPanel active={active}>
        <div> Storybook addon panel </div>
      </AddonPanel>
    ),
  });
});
```

```python
import { addons } from 'storybook/preview-api';
 
// Register the addon with a unique name.
addons.register('my-organisation/my-addon', (api) => {});
```

---

## ArgTypes

**URL**: https://storybook.js.org/docs/api/arg-types

**Contents**:
- ArgTypes
- Automatic argType inference
- Manually specifying argTypes
- argTypes
  - control
    - control.type
    - control.accept
    - control.labels

ArgTypes specify the behavior of args. By specifying the type of an arg, you constrain the values that it can accept and provide information about args that are not explicitly set (i.e., description).

You can also use argTypes to “annotate” args with information used by addons that make use of those args. For instance, to instruct the controls panel to render a color picker, you could specify the 'color' control type.

The most concrete realization of argTypes is the ArgTypes doc block (Controls is similar). Each row in the table corresponds to a single argType and the current value of that arg.

If you are using the Storybook docs addon, then Storybook will infer a set of argTypes for each story based on the component specified in the default export of the CSF file.

To do so, Storybook uses various static analysis tools depending on your framework.

The data structure of argTypes is designed to match the output of the these tools. Properties specified manually will override what is inferred.

For most Storybook projects, argTypes are automatically inferred from your components. Any argTypes specified manually will override the inferred values.

ArgTypes are most often specified at the meta (component) level, in the default export of the CSF file:

They can apply to all stories when specified at the project (global) level, in the preview.js|ts configuration file:

Or they can apply only to a specific story:

You configure argTypes using an object with keys matching the name of args. The value of each key is an object with the following properties:

Specify the behavior of the controls panel for the arg. If you specify a string, it's used as the type of the control. If you specify an object, you can provide additional configuration. Specifying false will prevent the control from rendering.

Type: ControlType | null

Default: Inferred; 'select', if options are specified; falling back to 'object'

Specifies the type of control used to change the arg value with the co

*[Content truncated - see full docs]*

**Examples**:

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Meta } from '@storybook/your-framework';
 
import { Button } from './Button';
 
const meta = {
  component: Button,
  argTypes: {
    // 👇 All Button stories expect a label arg
    label: {
      control: 'text',
      description: 'Overwritten description',
    },
  },
} satisfies Meta<typeof Button>;
 
export default meta;
```

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

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Meta, StoryObj } from '@storybook/your-framework';
 
import { Button } from './Button';
 
const meta = {
  component: Button,
} satisfies Meta<typeof Button>;
 
export default meta;
type Story = StoryObj<typeof meta>;
 
export const Basic: Story = {
  argTypes: {
    // 👇 This story expects a label arg
    label: {
      control: 'text',
      description: 'Overwritten description',
...
```

---

## ArgTypes

**URL**: https://storybook.js.org/docs/api/doc-blocks/doc-block-argtypes

**Contents**:
- ArgTypes
- ArgTypes
  - exclude
  - include
  - of
  - sort

The ArgTypes block can be used to show a static table of arg types for a given component, as a way to document its interface.

If you’re looking for a dynamic table that shows a story’s current arg values for a story and supports users changing them, see the Controls block instead.

ℹ️ Like most blocks, the ArgTypes block is configured with props in MDX. Many of those props derive their default value from a corresponding parameter in the block's namespace, parameters.docs.argTypes.

The following exclude configurations are equivalent:

The example above applied the parameter at the component (or meta) level, but it could also be applied at the project or story level.

Type: string[] | RegExp

Default: parameters.docs.argTypes.exclude

Specifies which arg types to exclude from the args table. Any arg types whose names match the regex or are part of the array will be left out.

Type: string[] | RegExp

Default: parameters.docs.argTypes.include

Specifies which arg types to include in the args table. Any arg types whose names don’t match the regex or are not part of the array will be left out.

Type: Story export or CSF file exports

Specifies which story to get the arg types from. If a CSF file exports is provided, it will use the primary (first) story in the file.

Type: 'none' | 'alpha' | 'requiredFirst'

Default: parameters.docs.argTypes.sort or 'none'

Specifies how the arg types are sorted.

**Examples**:

```python
import { Meta, ArgTypes } from '@storybook/addon-docs/blocks';
import * as ButtonStories from './Button.stories';
 
<Meta of={ButtonStories} />
 
<ArgTypes of={ButtonStories} />
```

```python
import { ArgTypes } from '@storybook/addon-docs/blocks';
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Meta } from '@storybook/your-framework';
 
import { Button } from './Button';
 
const meta = {
  component: Button,
  parameters: {
    docs: {
      controls: { exclude: ['style'] },
    },
  },
} satisfies Meta<typeof Button>;
 
export default meta;
```

---

## Builder API

**URL**: https://storybook.js.org/docs/builders/builder-api

**Contents**:
- Builder API
- How do builders work?
- Builder API
- Implementation
  - Import stories
  - Provide configuration options
  - Handle preview.js exports
  - MDX support

Storybook is architected to support multiple builders, including Webpack, Vite, and ESBuild. The builder API is the set of interfaces you can use to add a new builder to Storybook.

In Storybook, a builder is responsible for compiling your components and stories into JS bundles that run in the browser. A builder also provides a development server for interactive development and a production mode for optimized bundles.

To opt into a builder, the user must add it as a dependency and then edit their configuration file (.storybook/main.js) to enable it. For example, with the Vite builder:

In Storybook, every builder must implement the following API, exposing the following configuration options and entry points:

In development mode, the start API call is responsible for initializing the development server to monitor the file system for changes (for example, components and stories) then execute a hot module reload in the browser. It also provides a bail function to allow the running process to end gracefully, either via user input or error.

In production, the build API call is responsible for generating a static Storybook build, storing it by default in the storybook-static directory if no additional configuration is provided. The generated output should contain everything the user needs to view its Storybook by opening either the index.html or iframe.html in a browser with no other processes running.

Under the hood, a builder is responsible for serving/building the preview iframe, which has its own set of requirements. To fully support Storybook, including the essential features that ship with Storybook, it must consider the following.

The stories configuration field enables story loading in Storybook. It defines an array of file globs containing the physical location of the component's stories. The builder must be able to load those files and monitor them for changes and update the UI accordingly.

By default, Storybook's configuration is handled in a dedicated fi

*[Content truncated - see full docs]*

**Examples**:

```text
npm install @storybook/builder-vite --save-dev
```

```typescript
export default {
  stories: ['../src/**/*.mdx', '../stories/**/*.stories.@(js|jsx|mjs|ts|tsx)'],
  addons: ['@storybook/addon-docs'],
  core: {
    builder: '@storybook/builder-vite', // 👈 The builder enabled here.
  },
};
```

```javascript
export interface Builder<Config, Stats> {
  start: (args: {
    options: Options;
    startTime: ReturnType<typeof process.hrtime>;
    router: Router;
    server: Server;
  }) => Promise<void | {
    stats?: Stats;
    totalTime: ReturnType<typeof process.hrtime>;
    bail: (e?: Error) => Promise<void>;
  }>;
  build: (arg: {
    options: Options;
    startTime: ReturnType<typeof process.hrtime>;
  }) => Promise<void | Stats>;
  bail: (e?: Error) => Promise<void>;
  getConfig: (options: Options
...
```

---

## Canvas

**URL**: https://storybook.js.org/docs/api/doc-blocks/doc-block-canvas

**Contents**:
- Canvas
- Canvas
  - additionalActions
  - className
  - layout
  - meta
  - of
  - source

The Canvas block is a wrapper around a Story, featuring a toolbar that allows you to interact with its content while automatically providing the required Source snippets.

When using the Canvas block in MDX, it references a story with the of prop:

In previous versions of Storybook it was possible to pass in arbitrary components as children to Canvas. That is deprecated and the Canvas block now only supports a single story.

ℹ️ Like most blocks, the Canvas block is configured with props in MDX. Many of those props derive their default value from a corresponding parameter in the block's namespace, parameters.docs.canvas.

The following sourceState configurations are equivalent:

The example above applied the parameter at the story level, but it could also be applied at the component (or meta) level or project level.

Default: parameters.docs.canvas.additionalActions

Provides any additional custom actions to show in the bottom right corner. These are simple buttons that do anything you specify in the onClick function.

Default: parameters.docs.canvas.className

Provides HTML class(es) to the preview element, for custom styling.

Type: 'centered' | 'fullscreen' | 'padded'

Default: parameters.layout or parameters.docs.canvas.layout or 'padded'

Specifies how the canvas should layout the story.

In addition to the parameters.docs.canvas.layout property or the layout prop, the Canvas block will respect the parameters.layout value that defines how a story is laid out in the regular story view.

Type: CSF file exports

Specifies the CSF file to which the story is associated.

You can render a story from a CSF file that you haven’t attached to the MDX file (via Meta) by using the meta prop. Pass the full set of exports from the CSF file (not the default export!).

Specifies which story's source is displayed.

Type: SourceProps['code'] | SourceProps['format'] | SourceProps['language'] | SourceProps['type']

Specifies the props passed to the inner Source block. For more info

*[Content truncated - see full docs]*

**Examples**:

```python
import { Meta, Canvas } from '@storybook/addon-docs/blocks';
import * as ButtonStories from './Button.stories';
 
<Meta of={ButtonStories} />
 
<Canvas of={ButtonStories.Primary} />
```

```python
import { Canvas } from '@storybook/addon-docs/blocks';
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Meta, StoryObj } from '@storybook/your-framework';
 
import { Button } from './Button';
 
const meta = {
  component: Button,
} satisfies Meta<typeof Button>;
 
export default meta;
type Story = StoryObj<typeof meta>;
 
export const Basic: Story = {
  parameters: {
    docs: {
      canvas: { sourceState: 'shown' },
    },
  },
};
```

---

## ColorPalette

**URL**: https://storybook.js.org/docs/api/doc-blocks/doc-block-colorpalette

**Contents**:
- ColorPalette
- ColorPalette
  - children
- ColorItem
  - colors
  - subtitle
  - title

The ColorPalette block allows you to document all color-related items (e.g., swatches) used throughout your project.

ColorPalette is configured with the following props:

Type: React.ReactNode

ColorPalette expects only ColorItem children.

ColorItem is configured with the following props:

Type: string[] | { [key: string]: string }

Provides the list of colors to be displayed. Accepts any valid CSS color format (hex, RGB, HSL, etc.). When an object is provided, the keys will be displayed above the values. Additionally, it supports gradients such as 'linear-gradient(to right, white, black)' or 'linear-gradient(65deg, white, black)', etc.

Provides an additional description of the color.

Sets the name of the color to be displayed.

**Examples**:

```python
import { Meta, ColorPalette, ColorItem } from '@storybook/addon-docs/blocks';
 
<Meta title="Colors" />
 
<ColorPalette>
  <ColorItem
    title="theme.color.greyscale"
    subtitle="Some of the greys"
    colors={{ White: '#FFFFFF', Alabaster: '#F8F8F8', Concrete: '#F3F3F3' }}
  />
  <ColorItem 
    title="theme.color.primary" 
    subtitle="Coral" 
    colors={{ WildWatermelon: '#FF4785' }} 
  />
  <ColorItem 
    title="theme.color.secondary" 
    subtitle="Ocean" 
    colors={{ DodgerBlue: '#
...
```

```python
import { ColorPalette } from '@storybook/addon-docs/blocks';
```

```python
import { ColorItem } from '@storybook/addon-docs/blocks';
```

---

## Component Story Format (CSF)

**URL**: https://storybook.js.org/docs/api/csf

**Contents**:
- Component Story Format (CSF)
- Default export
- Named story exports
- Args story inputs
- Play function
- Custom render functions
- Storybook export vs. name handling
- Non-story exports

Component Story Format (CSF) is the recommended way to write stories. It's an open standard based on ES6 modules that is portable beyond Storybook.

In CSF, stories and component metadata are defined as ES Modules. Every component story file consists of a required default export and one or more named exports.

The default export defines metadata about your component, including the component itself, its title (where it will show up in the navigation UI story hierarchy), decorators, and parameters.

The component field is required and used by addons for automatic prop table generation and display of other component metadata. The title field is optional and should be unique (i.e., not re-used across files).

For more examples, see writing stories.

With CSF, every named export in the file represents a story object by default.

The exported identifiers will be converted to "start case" using Lodash's startCase function. For example:

We recommend that all export names to start with a capital letter.

Story objects can be annotated with a few different fields to define story-level decorators and parameters, and also to define the name of the story.

Storybook's name configuration element is helpful in specific circumstances. Common use cases are names with special characters or Javascript restricted words. If not specified, Storybook defaults to the named export.

Starting in SB 6.0, stories accept named inputs called Args. Args are dynamic data that are provided (and possibly updated by) Storybook and its addons.

Consider Storybook’s "Button" example of a text button that logs its click events:

Now consider the same example, re-written with args:

Not only are these versions shorter and more accessible to write than their no-args counterparts, but they are also more portable since the code doesn't depend on the actions feature specifically.

For more information on setting up Docs and Actions, see their respective documentation.

Storybook's play functions are small s

*[Content truncated - see full docs]*

**Examples**:

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Meta } from '@storybook/your-framework';
 
import { MyComponent } from './MyComponent';
 
const meta = {
  /* 👇 The title prop is optional.
   * See https://storybook.js.org/docs/configure/#configure-story-loading
   * to learn how to generate automatic titles
   */
  title: 'Path/To/MyComponent',
  component: MyComponent,
  decorators: [
    /* ... */
  ],
  parameters: {
    /* ..
...
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
import type { Meta, StoryObj } from '@storybook/your-framework';
 
import { MyComponent } from './MyComponent';
 
const meta = {
  component: MyComponent,
} satisfies Meta<typeof MyComponent>;
 
export default meta;
type Story = StoryObj<typeof meta>;
 
export const Basic: Story = {};
 
export const WithProp: Story = {
  render: () => <MyComponent prop="value" />,
};
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Meta, StoryObj } from '@storybook/your-framework';
 
import { MyComponent } from './MyComponent';
 
const meta = {
  component: MyComponent,
} satisfies Meta<typeof MyComponent>;
 
export default meta;
type Story = StoryObj<typeof meta>;
 
export const Simple: Story = {
  name: 'So simple!',
  // ...
};
```

---

## Controls

**URL**: https://storybook.js.org/docs/api/doc-blocks/doc-block-controls

**Contents**:
- Controls
- Controls
  - exclude
  - include
  - of
  - sort

The Controls block can be used to show a dynamic table of args for a given story, as a way to document its interface, and to allow you to change the args for a (separately) rendered story (via the Story or Canvas blocks).

If you’re looking for a static table that shows a component's arg types with no controls, see the ArgTypes block instead.

The Controls doc block will only have functioning UI controls if you haven't turned off inline stories with the inline configuration option.

ℹ️ Like most blocks, the Controls block is configured with props in MDX. Many of those props derive their default value from a corresponding parameter in the block's namespace, parameters.docs.controls.

The following exclude configurations are equivalent:

The example above applied the parameter at the component (or meta) level, but it could also be applied at the project or story level.

This API configures the Controls blocks used within docs pages. To configure the Controls panel, see the feature documentation. To configure individual controls, specify argTypes for each.

Type: string[] | RegExp

Default: parameters.docs.controls.exclude

Specifies which controls to exclude from the args table. Any controls whose names match the regex or are part of the array will be left out.

Type: string[] | RegExp

Default: parameters.docs.controls.include

Specifies which controls to include in the args table. Any controls whose names don't match the regex or are not part of the array will be left out.

Type: Story export or CSF file exports

Specifies which story to get the controls from. If a CSF file exports is provided, it will use the primary (first) story in the file.

Type: 'none' | 'alpha' | 'requiredFirst'

Default: parameters.docs.controls.sort or 'none'

Specifies how the controls are sorted.

**Examples**:

```python
import { Meta, Canvas, Controls } from '@storybook/addon-docs/blocks';
import * as ButtonStories from './Button.stories'
 
<Meta of={ButtonStories} />
 
<Canvas of={ButtonStories.Primary} />
 
<Controls of={ButtonStories.Primary} />
```

```python
import { Controls } from '@storybook/addon-docs/blocks';
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Meta } from '@storybook/your-framework';
 
import { Button } from './Button';
 
const meta = {
  component: Button,
  parameters: {
    docs: {
      controls: { exclude: ['style'] },
    },
  },
} satisfies Meta<typeof Button>;
 
export default meta;
```

---

## Description

**URL**: https://storybook.js.org/docs/api/doc-blocks/doc-block-description

**Contents**:
- Description
- Description
  - of
- Writing descriptions

The Description block displays the description for a component, story, or meta, obtained from their respective JSDoc comments.

Description is configured with the following props:

Type: Story export or CSF file exports

Specifies where to pull the description from. It can either point to a story or a meta, depending on which description you want to show.

Descriptions are pulled from the JSDoc comments or parameters, and they are rendered as markdown. See Writing descriptions for more details.

There are multiple places to write the description of a component/story, depending on what you want to achieve. Descriptions can be written at the story level to describe each story of a component, or they can be written at the meta or component level to describe the component in general.

Descriptions can be written as JSDoc comments above stories, meta, or components. Alternatively they can also be specified in parameters. To describe a story via parameters instead of comments, add it to parameters.docs.description.story; to describe meta/component, add it to parameters.docs.description.component.

We recommend using JSDoc comments for descriptions, and only use the parameters.docs.description.X properties in situations where comments are not possible to write for some reason, or where you want the description shown in Storybook to be different from the comments. Comments provide a better writing experience as you don’t have to worry about indentation, and they are more discoverable for other developers that are exploring the story/component sources.

When documenting a story, reference a story export in the of prop (see below) and the Description block will look for descriptions in the following order:

When documenting a component, reference a meta export in the of prop (see below) and the Description block will look for descriptions in the following order:

This flow gives you powerful ways to override the description for each scenario. Take the following example:

**Examples**:

```python
import { Meta, Description } from '@storybook/addon-docs/blocks';
import * as ButtonStories from './Button.stories';
 
<Meta of={ButtonStories} />
 
<Description of={ButtonStories.Primary} />
```

```python
import { Description } from '@storybook/addon-docs/blocks';
```

```javascript
/**
 * The Button component shows a button
 */
export const Button = () => <button>Click me</button>;
```

---

## IconGallery

**URL**: https://storybook.js.org/docs/api/doc-blocks/doc-block-icongallery

**Contents**:
- IconGallery
- Documenting icons
  - Automate icon documentation
- IconGallery
  - children
- IconItem
  - name
  - children

The IconGallery block enables you to easily document React icon components associated with your project, displayed in a neat grid.

To document a set of icons, use the IconGallery block to display them in a grid. Each icon is wrapped in an IconItem block, enabling you to specify its properties, such as the name and the icon itself.

If you're working on a project that contains a large number of icons that you want to document, you can extend the IconGallery block, wrap IconItem in a loop, and iterate over the icons you want to document, including their properties. For example:

IconGallery is configured with the following props:

Type: React.ReactNode

IconGallery expects only IconItem children.

IconItem is configured with the following props:

Sets the name of the icon.

Type: React.ReactNode

Provides the icon to be displayed.

**Examples**:

```python
import { Meta, IconGallery, IconItem } from '@storybook/addon-docs/blocks';
 
import { Icon as IconExample } from './Icon';
 
<Meta title="Iconography" />
 
# Iconography
 
<IconGallery>
  <IconItem name="mobile">
    <IconExample name="mobile" />
  </IconItem>
  <IconItem name="user">
    <IconExample name="user" />
  </IconItem>
  <IconItem name="browser">
    <IconExample name="browser" />
  </IconItem>
  <IconItem name="component">
    <IconExample name="component" />
  </IconItem>
  <IconIt
...
```

```python
import { Meta, IconGallery, IconItem } from '@storybook/addon-docs/blocks';
 
import { Icon as IconExample } from './Icon';
import * as icons from './icons';
 
# Iconography
 
<IconGallery>
  {Object.keys(icons).map((icon) => (
    <IconItem name={icon}>
      <IconExample icon={icon} />
    </IconItem>
  ))}
</IconGallery>
```

```python
import { IconGallery } from '@storybook/addon-docs/blocks';
```

---

## Main configuration

**URL**: https://storybook.js.org/docs/api/main-config/main-config

**Contents**:
- Main configuration
- main.js or main.ts
- config

The main configuration defines a Storybook project's behavior, including the location of stories, addons to use, feature flags, and other project-specific settings.

This configuration is defined in .storybook/main.js|ts, which is located relative to the root of your project.

A typical Storybook configuration file looks like this:

An object to configure Storybook containing the following properties:

**Examples**:

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { StorybookConfig } from '@storybook/your-framework';
 
const config: StorybookConfig = {
  // Required
  framework: '@storybook/your-framework',
  stories: ['../src/**/*.mdx', '../src/**/*.stories.@(js|jsx|mjs|ts|tsx)'],
  // Optional
  addons: ['@storybook/addon-docs'],
  docs: {
    defaultName: 'Documentation',
  },
  staticDirs: ['../public'],
};
 
export default config;
```

---

## Markdown

**URL**: https://storybook.js.org/docs/api/doc-blocks/doc-block-markdown

**Contents**:
- Markdown
- Markdown
  - children
  - options
- Why not import markdown directly?

The Markdown block allows you to import and include plain markdown in your MDX files.

When importing markdown files, it’s important to use the ?raw suffix on the import path to ensure the content is imported as-is, and isn’t being evaluated:

Markdown is configured with the following props:

Provides the markdown-formatted string to parse and display.

Specifies the options passed to the underlying markdown-to-jsx library.

From a purely technical standpoint, we could include the imported markdown directly in the MDX file like this:

However, there are small syntactical differences between plain markdown and MDX2. MDX2 is more strict and will interpret certain content as JSX expressions. Here’s an example of a perfectly valid markdown file, that would break if it was handled directly by MDX2:

Furthermore, MDX2 wraps all strings on newlines in p tags or similar, meaning that content would render differently between a plain .md file and an .mdx file.

**Examples**:

```python
# Button
 
Primary UI component for user interaction
 
```js
import { Button } from "@storybook/design-system";
```
```

```python
// DON'T do this, will error
import ReadMe from './README.md';
// DO this, will work
import ReadMe from './README.md?raw';
 
import { Markdown } from '@storybook/addon-docs/blocks';
 
# A header 
 
<Markdown>{ReadMe}</Markdown>
```

```python
import { Markdown } from '@storybook/addon-docs/blocks';
```

---

## Meta

**URL**: https://storybook.js.org/docs/api/doc-blocks/doc-block-meta

**Contents**:
- Meta
- Meta
  - isTemplate
  - name
  - of
  - title
- Attached vs. unattached

The Meta block is used to attach a custom MDX docs page alongside a component’s list of stories. It doesn’t render any content, but serves two purposes in an MDX file:

The Meta block doesn’t render anything visible.

Meta is configured with the following props:

Determines whether the MDX file serves as an automatic docs template. When true, the MDX file is not indexed as it normally would be.

Sets the name of the attached doc entry. You can attach more than one MDX file to the same component in the sidebar by setting different names for each file's Meta.

Type: CSF file exports

Specifies which CSF file is attached to this MDX file. Pass the full set of exports from the CSF file (not the default export!).

Attaching an MDX file to a component’s stories with the of prop serves two purposes:

The of prop is optional. If you don’t want to attach a specific CSF file to this MDX file, you can either use the title prop to control the location, or emit Meta entirely, and let autotitle decide where it goes.

Sets the title of an unattached MDX file.

If you want to change the sorting of the docs entry with the component’s stories, use Story Sorting, or add specific MDX files to your stories field in main.js in order.

In Storybook, a docs entry (MDX file) is "attached" when it is associated with a stories file, via Meta's of prop. Attached docs entries display next to the stories list under the component in the sidebar.

"Unattached" docs entries are not associated with a stories file and can be displayed anywhere in the sidebar via Meta's title prop.

**Examples**:

```python
import { Meta } from '@storybook/addon-docs/blocks';
import * as ButtonStories from './Button.stories';
 
<Meta of={ButtonStories} />
```

```python
import { Meta } from '@storybook/addon-docs/blocks';
```

```python
import { Meta } from '@storybook/addon-docs/blocks';
import * as ComponentStories from './component.stories';
 
{/* This MDX file is now called "Special Docs" */}
<Meta of={ComponentStories} name="Special Docs" />
```

---

## Primary

**URL**: https://storybook.js.org/docs/api/doc-blocks/doc-block-primary

**Contents**:
- Primary
- Primary
  - of

The Primary block displays the primary (first defined in the stories file) story, in a Story block. It is typically rendered immediately under the title in a docs entry.

Primary is configured with the following props:

Type: CSF file exports

Specifies which CSF file is used to find the first story, which is then rendered by this block. Pass the full set of exports from the CSF file (not the default export!).

**Examples**:

```python
import { Meta, Primary } from '@storybook/addon-docs/blocks';
import * as ButtonStories from './Button.stories';
 
<Meta of={ButtonStories} />
 
<Primary />
```

```python
import { Primary } from '@storybook/addon-docs/blocks';
```

---

## Source

**URL**: https://storybook.js.org/docs/api/doc-blocks/doc-block-source

**Contents**:
- Source
- Source
  - code
  - dark
  - excludeDecorators
  - language
  - of
  - transform

The Source block is used to render a snippet of source code directly.

ℹ️ Like most blocks, the Source block is configured with props in MDX. Many of those props derive their default value from a corresponding parameter in the block's namespace, parameters.docs.source.

The following language configurations are equivalent:

The example above applied the parameter at the story level, but it could also be applied at the component (or meta) level or project level.

Default: parameters.docs.source.code

Provides the source code to be rendered.

Default: parameters.docs.source.dark

Determines if the snippet is rendered in dark mode.

Light mode is only supported when the Source block is rendered independently. When rendered as part of a Canvas block—like it is in autodocs—it will always use dark mode.

Default: parameters.docs.source.excludeDecorators

Determines if decorators are rendered in the source code snippet.

Default: parameters.docs.source.language or 'jsx'

Specifies the language used for syntax highlighting.

Specifies which story's source is rendered.

Type: (code: string, storyContext: StoryContext) => string | Promise<string>

Default: parameters.docs.source.transform

An async function to dynamically transform the source before being rendered, based on the original source and any story context necessary. The returned string is displayed as-is. If both code and transform are specified, transform will be ignored.

This example shows how to use Prettier to format all source code snippets in your documentation. The transform function is applied globally through the preview configuration, ensuring consistent code formatting across all stories.

Type: 'auto' | 'code' | 'dynamic'

Default: parameters.docs.source.type or 'auto'

Specifies how the source code is rendered.

Note that dynamic snippets will only work if the story uses args and the Story block for that story is rendered along with the Source block.

**Examples**:

```python
import { Meta, Source } from '@storybook/addon-docs/blocks';
import * as ButtonStories from './Button.stories';
 
<Meta of={ButtonStories} />
 
<Source of={ButtonStories.Primary} />
```

```python
import { Source } from '@storybook/addon-docs/blocks';
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Meta, StoryObj } from '@storybook/your-framework';
 
import { Button } from './Button';
 
const meta = {
  component: Button,
} satisfies Meta<typeof Button>;
 
export default meta;
type Story = StoryObj<typeof meta>;
 
export const Basic: Story = {
  parameters: {
    docs: {
      source: { language: 'tsx' },
    },
  },
};
```

---

## Story

**URL**: https://storybook.js.org/docs/api/doc-blocks/doc-block-story

**Contents**:
- Story
- Story
  - autoplay
  - height
  - inline
  - meta
  - of

Stories are Storybook's fundamental building blocks.

In Storybook Docs, you can render any of your stories from your CSF files in the context of an MDX file with all annotations (parameters, args, loaders, decorators, play function) applied using the Story block.

Typically you want to use the Canvas block to render a story with a surrounding border and the source block, but you can use the Story block to render just the story.

ℹ️ Like most blocks, the Story block is configured with props in MDX. Many of those props derive their default value from a corresponding parameter in the block's namespace, parameters.docs.story.

The following autoplay configurations are equivalent:

The example above applied the parameter at the story level, but it could also be applied at the component (or meta) level or project level.

Default: parameters.docs.story.autoplay

Determines whether a story's play function runs.

Because all stories render simultaneously in docs entries, play functions can perform arbitrary actions that can interact with each other (such as stealing focus or scrolling the screen). For that reason, by default, stories do not run play functions in docs mode.

However, if you know your play function is “safe” to run in docs, you can use this prop to run it automatically.

If a story uses mount in its play function, it will not render in docs unless autoplay is set to true.

Default: parameters.docs.story.height

Set a minimum height (note for an iframe this is the actual height) when rendering a story in an iframe or inline. This overrides parameters.docs.story.iframeHeight for iframes.

Default: parameters.docs.story.inline or true (for supported frameworks)

Determines whether the story is rendered inline (in the same browser frame as the other docs content) or in an iframe.

Setting the inline option to false will prevent the associated controls from updating the story within the documentation page. This is a known limitation of the current implementation a

*[Content truncated - see full docs]*

**Examples**:

```python
import { Meta, Story } from '@storybook/addon-docs/blocks';
import * as ButtonStories from './Button.stories';
 
<Meta of={ButtonStories} />
 
<Story of={ButtonStories.Primary} />
```

```python
import { Story } from '@storybook/addon-docs/blocks';
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Meta, StoryObj } from '@storybook/your-framework';
 
import { Button } from './Button';
 
const meta = {
  component: Button,
} satisfies Meta<typeof Button>;
 
export default meta;
type Story = StoryObj<typeof meta>;
 
export const Basic: Story = {
  parameters: {
    docs: {
      story: { autoplay: true },
    },
  },
};
```

---

## Subtitle

**URL**: https://storybook.js.org/docs/api/doc-blocks/doc-block-subtitle

**Contents**:
- Subtitle
- Subtitle
  - children
  - of

The Subtitle block can serve as a secondary heading for your docs entry.

Subtitle is configured with the following props:

Type: JSX.Element | string

Default: parameters.docs.subtitle

Provides the content.

Type: CSF file exports

Specifies which meta's subtitle is displayed.

**Examples**:

```python
import { Subtitle } from '@storybook/addon-docs/blocks';
 
<Subtitle>This is the subtitle</Subtitle>
```

```python
import { Subtitle } from '@storybook/addon-docs/blocks';
```

---

## Title

**URL**: https://storybook.js.org/docs/api/doc-blocks/doc-block-title

**Contents**:
- Title
- Title
  - children
  - of

The Title block serves as the primary heading for your docs entry. It is typically used to provide the component or page name.

Title is configured with the following props:

Type: JSX.Element | string

Provides the content. Falls back to value of title in an attached CSF file (or value derived from autotitle), trimmed to the last segment. For example, if the title value is 'path/to/components/Button', the default content is 'Button'.

Type: CSF file exports

Specifies which meta's title is displayed.

**Examples**:

```python
import { Title } from '@storybook/addon-docs/blocks';
 
<Title>This is the title</Title>
```

```python
import { Title } from '@storybook/addon-docs/blocks';
```

---

## TypeScript

**URL**: https://storybook.js.org/docs/configure/integration/typescript

**Contents**:
- TypeScript
- Configure Storybook with TypeScript
  - Extending the default configuration
- Write stories with TypeScript
  - TypeScript 4.9 support
- Troubleshooting
  - The satisfies operator is not working as expected
  - Storybook doesn't create the required types for external packages

Storybook provides an integrated TypeScript experience, including zero-configuration setup and built-in types for APIs, addons, and stories.

Storybook's configuration file (i.e., main.ts) is defined as an ESM module written in TypeScript, providing you with the baseline configuration to support your existing framework while enabling you stricter type-checking and autocompletion in your editor. Below is an abridged configuration file.

See the main configuration API reference for more details and additional properties.

See the Vite builder TypeScript documentation if using @storybook/builder-vite.

Out of the box, Storybook is built to work with a wide range of third-party libraries, enabling you to safely access and document metadata (e.g., props) for your components without any additional configuration. It relies on react-docgen, a fast and highly customizable parser to process TypeScript files to infer the component's metadata and generate types automatically for improved performance and type safety. If you need to customize the default configuration for a specific use case scenario, you can adjust your Storybook configuration file and provide the required options. Listed below are the available options and examples of how to use them.

Additional options are available for the typescript configuration option. See the config.typescript API reference for more information.

Storybook provides zero-config TypeScript support, allowing you to write stories using this language without additional configuration. You can use this format for improved type safety and code completion. For example, if you're testing a Button component, you could do the following in your story file:

The example above uses the power of TypeScript in combination with the exported generic types (Meta and StoryObj) to tell Storybook how to infer the component's metadata and the type of the component's inputs (e.g., props). This can greatly improve the developer experience by letting your IDE show

*[Content truncated - see full docs]*

**Examples**:

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { StorybookConfig } from '@storybook/your-framework';
 
const config: StorybookConfig = {
  // Required
  framework: '@storybook/your-framework',
  stories: ['../src/**/*.mdx', '../src/**/*.stories.@(js|jsx|mjs|ts|tsx)'],
  // Optional
  addons: ['@storybook/addon-docs'],
  docs: {
    defaultName: 'Documentation',
  },
  staticDirs: ['../public'],
};
 
export default config;
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { StorybookConfig } from '@storybook/your-framework';
 
const config: StorybookConfig = {
  framework: '@storybook/your-framework',
  stories: ['../src/**/*.mdx', '../src/**/*.stories.@(js|jsx|mjs|ts|tsx)'],
  typescript: {
    check: false,
    checkOptions: {},
    skipCompiler: false,
  },
};
 
export default config;
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Meta, StoryObj } from '@storybook/your-framework';
 
import { Button } from './Button';
 
const meta = {
  component: Button,
} satisfies Meta<typeof Button>;
 
export default meta;
type Story = StoryObj<typeof meta>;
 
//👇 Throws a type error if the args don't match the component props
export const Primary: Story = {
  args: {
    primary: true,
  },
};
```

---

## Typeset

**URL**: https://storybook.js.org/docs/api/doc-blocks/doc-block-typeset

**Contents**:
- Typeset
- Typeset
  - fontFamily
  - fontSizes
  - fontWeight
  - sampleText

The Typeset block helps document the fonts used throughout your project.

Typeset is configured with the following props:

Provides a font family to be displayed.

Type: (string | number)[]

Provides a list of available font sizes (in px).

Specifies the weight of the font to be displayed.

Sets the text to be displayed.

**Examples**:

```python
import { Meta, Typeset } from '@storybook/addon-docs/blocks';
 
<Meta title="Typography" />
 
export const typography = {
  type: {
    primary: '"Nunito Sans", "Helvetica Neue", Helvetica, Arial, sans-serif',
  },
  weight: {
    regular: '400',
    bold: '700',
    extrabold: '800',
    black: '900',
  },
  size: {
    s1: 12,
    s2: 14,
    s3: 16,
    m1: 20,
    m2: 24,
    m3: 28,
    l1: 32,
    l2: 40,
    l3: 48,
  },
};
 
export const SampleText = 'Lorem ipsum dolor sit amet, consecte
...
```

```python
import { Typeset } from '@storybook/addon-docs/blocks';
```

---

## Unstyled

**URL**: https://storybook.js.org/docs/api/doc-blocks/doc-block-unstyled

**Contents**:
- Unstyled
- Unstyled
  - children

The Unstyled block is a special block that disables Storybook's default styling in MDX docs wherever it is added.

By default, most elements (like h1, p, etc.) in docs have a few default styles applied to ensure the docs look good. However, sometimes you might want some of your content to not have these styles applied. In those cases, wrap the content with the Unstyled block to remove the default styles.

The other blocks like Story and Canvas are already unstyled, so there’s no need to wrap those in the Unstyled block to ensure that Storybook’s styles don’t bleed into the stories. However, if you import your components directly in the MDX, you most likely want to wrap them in the Unstyled block.

Due to how CSS inheritance works it’s best to always add the Unstyled block to the root of your MDX, and not nested into other elements. The following example will cause some Storybook styles like color to be inherited into CustomComponent because they are applied to the root div:

Unstyled is configured with the following props:

Type: React.ReactNode

Provides the content to which you do not want to apply default docs styles.

**Examples**:

```python
import { Meta, Unstyled } from "@storybook/addon-docs/blocks";
import { Header } from "./Header.tsx";
 
<Meta title="Unstyled" />
 
> This block quote will be styled
 
... and so will this paragraph.
 
<Unstyled>
  > This block quote will not be styled
 
  ... neither will this paragraph, nor the following component (which contains an \<h1\>):
 
  <Header />
 
</Unstyled>
```

```text
<div>
  <Unstyled>
    <CustomComponent/>
  </Unstyled>
</div>
```

```python
import { Unstyled } from '@storybook/addon-docs/blocks';
```

---

## Write a preset addon

**URL**: https://storybook.js.org/docs/addons/writing-presets

**Contents**:
- Write a preset addon
- How presets work
  - Local presets
  - Root-level presets
- Presets API
  - Babel
  - Builders
    - Vite

Storybook presets are pre-configured settings or configurations that enable developers quickly set up and customize their environment with a specific set of features, functionalities, or integrations.

Preset addons allow developers to compose various configuration options and plugins via APIs to integrate with Storybook and customize its behavior and functionality. Typically, presets are separated into two files, each with its specific role.

This type of preset allows you to encapsulate and organize configurations specific to the addon, including builder support, Babel, or third-party integrations. For example:

This type of preset is user-facing and responsible for registering the addon without any additional configuration from the user by bundling Storybook-related features (e.g., parameters) via the previewAnnotations and UI related features (e.g., addons) via the managerEntries API. For example:

When writing a preset, you can access a select set of APIs to interact with the Storybook environment, including the supported builders (e.g., Webpack, Vite), the Storybook configuration, and UI. Below are the available APIs you can use when writing a preset addon.

To customize Storybook's Babel configuration and add support for additional features, you can use the babelDefault API. It will apply the provided configuration ahead of any other user presets, which can be further customized by the end user via the babel configuration option. For example:

The Babel configuration is only applied to frameworks that use Babel internally. If you enable it for a framework that uses a different compiler, like SWC or esbuild, it will be ignored.

By default, Storybook provides support for the leading industry builders, including Webpack and Vite. If you need additional features for any of these builders, you can use APIs to extend the builder configuration based on your specific needs.

If you are creating a preset and want to include Vite support, the viteFinal API can be used

*[Content truncated - see full docs]*

**Examples**:

```python
import { webpackFinal as webpack } from './webpack/webpackFinal';
 
import { viteFinal as vite } from './vite/viteFinal';
 
import { babelDefault as babel } from './babel/babelDefault';
 
export const webpackFinal = webpack as any;
 
export const viteFinal = vite as any;
 
export const babelDefault = babel as any;
```

```javascript
export const previewAnnotations = [require.resolve('./dist/preview')];
 
export const managerEntries = [require.resolve('./dist/manager')];
 
export * from './dist/preset';
```

```python
import { TransformOptions } from '@babel/core';
 
export function babelDefault(config: TransformOptions) {
  return {
    ...config,
    plugins: [
      ...config.plugins,
      [require.resolve('@babel/plugin-transform-react-jsx'), {}, 'preset'],
    ],
  };
}
```

---

## addons

**URL**: https://storybook.js.org/docs/api/main-config/main-config-addons

**Contents**:
- addons

Parent: main.js|ts configuration

Type: (string | { name: string; options?: AddonOptions })[]

Registers the addons loaded by Storybook.

For each addon's available options, see their respective documentation.

**Examples**:

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { StorybookConfig } from '@storybook/your-framework';
 
const config: StorybookConfig = {
  framework: '@storybook/your-framework',
  stories: ['../src/**/*.mdx', '../src/**/*.stories.@(js|jsx|mjs|ts|tsx)'],
  addons: [
    '@storybook/addon-docs',
    {
      name: '@storybook/addon-styling-webpack',
      options: {
        rules: [
          {
            test: /\.css$/,
          
...
```

---

## babelDefault

**URL**: https://storybook.js.org/docs/api/main-config/main-config-babel-default

**Contents**:
- babelDefault
- Babel.Config
- Options

Parent: main.js|ts configuration

Type: (config: Babel.Config, options: Options) => Babel.Config | Promise<Babel.Config>

babelDefault allows customization of Storybook's Babel setup. It is applied to the preview config before any user presets have been applied, which makes it useful and recommended for addon authors so that the end user's babel setup can override it.

To adjust your Storybook's Babel setup directly—not via an addon—use babel instead.

The options provided by Babel are only applicable if you've enabled the @storybook/addon-webpack5-compiler-babel addon.

Type: { configType?: 'DEVELOPMENT' | 'PRODUCTION' }

There are other options that are difficult to document here. Please introspect the type definition for more information.

**Examples**:

```python
import { TransformOptions } from '@babel/core';
 
export function babelDefault(config: TransformOptions) {
  return {
    plugins: [[require.resolve('@babel/plugin-transform-react-jsx'), {}, 'preset']],
  };
}
```

---

## babel

**URL**: https://storybook.js.org/docs/api/main-config/main-config-babel

**Contents**:
- babel
- Babel.Config
- Options

Parent: main.js|ts configuration

Type: (config: Babel.Config, options: Options) => Babel.Config | Promise<Babel.Config>

Customize Storybook's Babel setup.

Addon authors should use babelDefault instead, which is applied to the preview config before any user presets have been applied.

The options provided by Babel are only applicable if you've enabled the @storybook/addon-webpack5-compiler-babel addon.

If you have an existing Babel configuration file (e.g., .babelrc), it will be automatically detected and used by Storybook without any additional configuration required.

Type: { configType?: 'DEVELOPMENT' | 'PRODUCTION' }

There are other options that are difficult to document here. Please introspect the type definition for more information.

**Examples**:

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { StorybookConfig } from '@storybook/your-framework';
 
const config: StorybookConfig = {
  framework: '@storybook/your-framework',
  stories: ['../src/**/*.mdx', '../stories/**/*.stories.@(js|jsx|mjs|ts|tsx)'],
  async babel(config, { configType }) {
    if (configType === 'DEVELOPMENT') {
      // Your development configuration goes here
    }
    if (configType === 'PRODUCTION') {

...
```

---

## build

**URL**: https://storybook.js.org/docs/api/main-config/main-config-build

**Contents**:
- build
- test
  - test.disableBlocks
  - test.disabledAddons
  - test.disableMDXEntries
  - test.disableAutoDocs
  - test.disableDocgen
  - test.disableSourcemaps

Parent: main.js|ts configuration

Type: TestBuildConfig

Provides configuration options to optimize Storybook's production build output.

Configures Storybook's production builds for performance testing purposes by disabling certain features from the build. When running build-storybook, this feature is enabled by setting the --test flag.

The options documented on this page are automatically enabled when the --test flag is provided to the storybook build command. We encourage you to override these options only if you need to disable a specific feature for your project or if you are debugging a build issue.

Excludes the @storybook/addon-docs/blocks module from the build, which generates automatic documentation with Docs Blocks.

Sets the list of addons that will disabled in the build output.

Enabling this option removes user-written documentation entries in MDX format from the build.

Prevents automatic documentation generated with the autodocs feature from being included in the build.

Disables automatic argType and component property inference with any of the supported static analysis tools based on the framework you are using.

Overrides the default behavior of generating source maps for the build.

Disables tree shaking in the build.

**Examples**:

```text
{
  disableBlocks?: boolean;
  disabledAddons?: string[];
  disableMDXEntries?: boolean;
  disableAutoDocs?: boolean;
  disableDocgen?: boolean;
  disableSourcemaps?: boolean;
  disableTreeShaking?: boolean;
 
}
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { StorybookConfig } from '@storybook/your-framework';
 
const config: StorybookConfig = {
  framework: '@storybook/your-framework',
  stories: ['../src/**/*.mdx', '../src/**/*.stories.@(js|jsx|mjs|ts|tsx)'],
  build: {
    test: {
      disableBlocks: false,
    },
  },
};
 
export default config;
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { StorybookConfig } from '@storybook/your-framework';
 
const config: StorybookConfig = {
  framework: '@storybook/your-framework',
  stories: ['../src/**/*.mdx', '../src/**/*.stories.@(js|jsx|mjs|ts|tsx)'],
  addons: ['@storybook/addon-a11y', '@storybook/addon-vitest'],
  build: {
    test: {
      disabledAddons: ['@storybook/addon-a11y'],
    },
  },
};
 
export default config;
```

---

## framework

**URL**: https://storybook.js.org/docs/api/main-config/main-config-framework

**Contents**:
- framework
- name
- options
  - options.builder

Parent: main.js|ts configuration

Type: FrameworkName | { name: FrameworkName; options?: FrameworkOptions }

Configures Storybook based on a set of framework-specific settings.

For available frameworks and their options, see their respective documentation.

Type: Record<string, any>

While many options are specific to a framework, there are some options that are shared across some frameworks, e.g. those that configure Storybook's builder.

Type: Record<string, any>

Configures Storybook's builder, Vite or Webpack.

**Examples**:

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
import type { StorybookConfig } from '@storybook/your-framework';
 
const config: StorybookConfig = {
  framework: {
    name: '@storybook/your-framework',
    options: {
      legacyRootApi: true,
    },
  },
  stories: ['../src/**/*.mdx', '../src/**/*.stories.@(js|jsx|mjs|ts|tsx)'],
};
 
export default config;
```

---

## useOf

**URL**: https://storybook.js.org/docs/api/doc-blocks/doc-block-useof

**Contents**:
- useOf
- useOf
  - Type
  - Parameters
    - moduleExportOrType
    - validTypes
  - Return
    - EnhancedResolvedModuleExportType['type'] === 'story'

The default blocks supplied by Storybook do not fit all use cases, so you might want to write your own blocks.

If your own doc blocks need to interface with annotations from Storybook—that is stories, meta or components—you can use the useOf hook. Pass in a module export of a story, meta, or component and it will return its annotated form (with applied parameters, args, loaders, decorators, play function) that you can then use for anything you like. In fact, most of the existing blocks like Description and Canvas use useOf under the hood.

Here’s an example of how theuseOf hook could be used to create a custom block that displays the name of the story:

Type: ModuleExport | 'story' | 'meta' | 'component'

Provides the story export, meta export, component export, or CSF file exports from which you get annotations.

When the custom block is in an attached doc, it’s also possible to get the primary (first) story, meta, or component by passing in a string instead. This is useful as a fallback, so the of prop can be omitted in your block. The most common pattern is using this as useOf(props.of || 'story') which will fall back to the primary story if no of prop is defined.

Type: Array<'story' | 'meta' | 'component'>

Optionally specify an array of valid types that your block accepts. Passing anything other than the valid type(s) will result in an error. For example, the Canvas block uses useOf(of, ['story']), which ensures it only accepts a reference to a story, not a meta or component.

The return value depends on the matched type:

Type: { type: 'story', story: PreparedStory }

For stories, annotated stories are returned as is. They are prepared, meaning that they are already merged with project and meta annotations.

Type: { type: 'meta', csfFile: CSFFile, preparedMeta: PreparedMeta }

For meta, the parsed CSF file is returned, along with prepared annotated meta. That is, project annotations merged with meta annotations, but no story annotations.

Type: { type: 'comp

*[Content truncated - see full docs]*

**Examples**:

```python
import { useOf } from '@storybook/addon-docs/blocks';
 
/**
 * A block that displays the story name or title from the of prop
 * - if a story reference is passed, it renders the story name
 * - if a meta reference is passed, it renders the stories' title
 * - if nothing is passed, it defaults to the primary story
 */
export const StoryName = ({ of }) => {
  const resolvedOf = useOf(of || 'story', ['story', 'meta']);
  switch (resolvedOf.type) {
    case 'story': {
      return <h1>{resolvedOf.st
...
```

```python
import { Meta } from '@storybook/addon-docs/blocks';
import { StoryName } from '../.storybook/blocks/StoryName';
import * as ButtonStories from './Button.stories';
 
<Meta of={ButtonStories} />
 
{/* Renders "Secondary" */}
<StoryName of={ButtonStories.Secondary} />
 
{/* Renders "Primary" */}
<StoryName />
 
{/* Renders "Button" */}
<StoryName of={ButtonStories} />
```

```javascript
(
  moduleExportOrType: ModuleExport | 'story' | 'meta' | 'component',
  validTypes?: Array<'story' | 'meta' | 'component'>
) => EnhancedResolvedModuleExportType
```

---

## viteFinal

**URL**: https://storybook.js.org/docs/api/main-config/main-config-vite-final

**Contents**:
- viteFinal
- Options

Parent: main.js|ts configuration

Type: (config: Vite.InlineConfig, options: Options) => Vite.InlineConfig | Promise<Vite.InlineConfig>

Customize Storybook's Vite setup when using the Vite builder.

Type: { configType?: 'DEVELOPMENT' | 'PRODUCTION' }

There are other options that are difficult to document here. Please introspect the type definition for more information.

**Examples**:

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs-vite, vue3-vite, etc.
import type { StorybookConfig } from '@storybook/your-framework';
 
const config: StorybookConfig = {
  framework: '@storybook/your-framework',
  stories: ['../src/**/*.mdx', '../stories/**/*.stories.@(js|jsx|mjs|ts|tsx)'],
  async viteFinal(config, { configType }) {
    const { mergeConfig } = await import('vite');
 
    if (configType === 'DEVELOPMENT') {
      // Your development configur
...
```

---

## webpackFinal

**URL**: https://storybook.js.org/docs/api/main-config/main-config-webpack-final

**Contents**:
- webpackFinal
- Options

Parent: main.js|ts configuration

Type: async (config: Config, options: WebpackOptions) => Config

Customize Storybook's Webpack setup when using the webpack builder.

Type: { configType?: 'DEVELOPMENT' | 'PRODUCTION' }

There are other options that are difficult to document here. Please introspect the type definition for more information.

**Examples**:

```python
// Replace your-framework with the framework you are using, e.g. react-webpack5, nextjs, angular, etc.
import type { StorybookConfig } from '@storybook/your-framework';
 
const config: StorybookConfig = {
  framework: '@storybook/your-framework',
  stories: ['../src/**/*.mdx', '../src/**/*.stories.@(js|jsx|mjs|ts|tsx)'],
  webpackFinal: async (config, { configType }) => {
    if (configType === 'DEVELOPMENT') {
      // Modify config for development
    }
    if (configType === 'PRODUCTION') {
 
...
```

---
