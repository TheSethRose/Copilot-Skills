# Storybook - Other

**Pages**: 57

---

## Actions

**URL**: https://storybook.js.org/docs/essentials/actions

**Contents**:
- Actions
- Action args
  - Via storybook/test fn spy function
  - Automatically matching args
- API
  - Parameters
    - argTypesRegex
    - disable

Actions are used to display data received by event handler (callback) arguments in your stories.

Actions work via supplying special Storybook-generated “action” arguments (referred to as "args" for short) to your stories. There are two ways to get an action arg:

The recommended way to write actions is to use the fn utility from storybook/test to mock and spy args. This is very useful for writing interaction tests. You can mock your component's methods by assigning them to the fn() function:

If your component calls an arg (because of either the user's interaction or the play function) and that arg is spied on , the event will show up in the action panel:

Another option is to use a global parameter to match all argTypes that match a certain pattern. The following configuration automatically creates actions for each on argType (which you can either specify manually or can be inferred automatically).

This is quite useful when your component has dozens (or hundreds) of methods and you do not want to manually apply the fn utility for each of those methods. However, this is not the recommended way of writing actions. That's because automatically inferred args are not available as spies in your play function. If you use argTypesRegex and your stories have play functions, you will need to also define args with the fn utility to test them in your play function.

If you need more granular control over which argTypes are matched, you can adjust your stories and include the argTypesRegex parameter. For example:

This will bind a standard HTML event handler to the outermost HTML element rendered by your component and trigger an action when the event is called for a given selector. The format is <eventname> <selector>. The selector is optional; it defaults to all elements.

This contributes the following parameters to Storybook, under the actions namespace:

Create actions for each arg that matches the regex. Please note the significant limitations of this approach, as descri

*[Content truncated - see full docs]*

**Examples**:

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Meta } from '@storybook/your-framework';
 
import { fn } from 'storybook/test';
 
import { Button } from './Button';
 
const meta = {
  component: Button,
  // 👇 Use `fn` to spy on the onClick arg, which will appear in the actions panel once invoked
  args: { onClick: fn() },
} satisfies Meta<typeof Button>;
 
export default meta;
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Preview } from '@storybook/your-framework';
 
const preview: Preview = {
  parameters: {
    actions: { argTypesRegex: '^on.*' },
  },
};
 
export default preview;
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Meta } from '@storybook/your-framework';
 
import { Button } from './Button';
 
const meta = {
  component: Button,
  parameters: { actions: { argTypesRegex: '^on.*' } },
} satisfies Meta<typeof Button>;
 
export default meta;
```

---

## Addon knowledge base

**URL**: https://storybook.js.org/docs/addons/addon-knowledge-base

**Contents**:
- Addon knowledge base
- Disable the addon panel
- Style your addon
- Storybook components
- Build system
- Hot module replacement
- Standalone Storybook addons
  - Local Storybook addons

Once you understand the basics of writing addons, there are a variety of common enhancements to make your addon better. This page details additional information about addon creation. Use it as a quick reference guide when creating your own addons.

It’s possible to disable the addon panel for a particular story.

To make that possible, you need to pass the paramKey element when you register the panel:

Then when adding a story, you can pass a disabled parameter.

Storybook uses Emotion for styling. Alongside with a theme that you can customize!

We recommend using Emotion to style your addon’s UI components. That allows you to use the active Storybook theme to deliver a seamless developer experience. If you don’t want to use Emotion, you can use inline styles or another css-in-js lib. You can receive the theme as a prop by using Emotion's withTheme HOC. Read more about theming.

Addon authors can develop their UIs using any React library. But we recommend using Storybook’s UI components in storybook/internal/components to build addons faster. When you use Storybook components, you get:

Use the components listed below with your next addon.

Complementing the components, also included is a set of UI primitives. Use the content listed below as a reference for styling your addon.

The color palette implemented by @storybook/addon-docs/blocks is a high-level abstraction of the storybook/theming module.

When you're developing your addon as a package, you can’t use npm link to add it to your project. List your addon as a local dependency into your package.json:

Run either yarn or npm install to install the addon.

While developing your addon, you can configure HMR (hot module replacement) to reflect the changes made.

If you're developing a standalone addon, add a new script to package.json with the following:

If you're developing a local Storybook addon built on top of an existing Storybook installation, HMR (hot module replacement) is available out of the box.

If yo

*[Content truncated - see full docs]*

**Examples**:

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

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Meta } from '@storybook/your-framework';
 
import { Button } from './Button';
 
const meta = {
  /* 👇 The title prop is optional.
   * See https://storybook.js.org/docs/configure/#configure-story-loading
   * to learn how to generate automatic titles
   */
  title: 'Button',
  component: Button,
  parameters: {
    myAddon: { disable: true }, // Disables the addon
  },
} satisfies M
...
```

```text
{
  "dependencies": {
    "@storybook/addon-controls": "file:///home/username/myrepo"
  }
}
```

---

## Backgrounds

**URL**: https://storybook.js.org/docs/essentials/backgrounds

**Contents**:
- Backgrounds
- Configuration
- Defining the background for a story
- Extending the configuration
- Disable backgrounds
- Grid
- API
  - Globals

The backgrounds feature allows you to set the background color on which the story renders in the UI:

By default, the backgrounds feature includes a light and dark background.

But you're not restricted to these backgrounds. You can configure your own set of colors with the backgrounds parameter in your .storybook/preview.js|ts.

You can define the available background colors using the options property and set the initial background color using the initialGlobals property:

The backgrounds feature enables you to change the background color applied to a story by selecting from the list of predefined background colors in the toolbar. If needed, you can set a story to default to a specific background color, by using the globals option:

When you specify a background color for a story (or a component's stories) using globals, the color is applied and cannot be changed using the toolbar. This is useful to ensure a story is always rendered on a specific background color.

You can also configure backgrounds on a per-component or per-story basis through parameter inheritance.

To set the available background colors, use the options property. In this example, we'll adjust the colors for all of the Button component's stories:

If you want to turn off backgrounds in a story, you can do so by configuring the backgrounds parameter like so:

The backgrounds feature also includes a Grid selector, which allows you to quickly see if your components are aligned.

You don't need additional configuration to get started. But its properties are fully customizable; if you don't supply any value to any of its properties, they'll default to the following values:

This module contributes the following globals to Storybook, under the backgrounds namespace:

Whether the grid is displayed.

When set, the background color is applied and cannot be changed using the toolbar. Must match the key of one of the available colors.

This module contributes the following parameters to Storybook, under the

*[Content truncated - see full docs]*

**Examples**:

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Preview } from '@storybook/your-framework';
 
const preview: Preview = {
  parameters: {
    backgrounds: {
      options: {
        // 👇 Default options
        dark: { name: 'Dark', value: '#333' },
        light: { name: 'Light', value: '#F7F9F2' },
        // 👇 Add your own
        maroon: { name: 'Maroon', value: '#400' },
      },
    },
  },
  initialGlobals: {
    // 👇 Set t
...
```

```python
// Replace your-framework with the name of your framework (e.g., react-vite, vue3-vite, etc.)
import type { Meta, StoryObj } from '@storybook/your-framework';
 
import { Button } from './Button';
 
const meta = {
  component: Button,
  globals: {
    // 👇 Set background value for all component stories
    backgrounds: { value: 'gray', grid: false },
  },
} satisfies Meta<typeof Button>;
 
export default meta;
type Story = StoryObj<typeof meta>;
 
export const OnDark: Story = {
  globals: {
    /
...
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
import type { Meta } from '@storybook/your-framework';
 
import { Button } from './Button';
 
const meta = {
  component: Button,
  parameters: {
    backgrounds: {
      options: {
        // 👇 Override the default `dark` option
        dark: { name: 'Dark', value: '#000' },
        // 👇 Add a new option
        gray: { name: 'Gray', value: '#CCC' },
      },
    },
  },
} satisfies Meta<typeo
...
```

---

## Builders

**URL**: https://storybook.js.org/docs/builders

**Contents**:
- Builders
- CLI basics
- Manual setup

Storybook, at its core, is powered by builders such as Webpack and Vite. These builders spin up a development environment, compile your code—Javascript, CSS, and MDX—into an executable bundle and update the browser in real-time.

Before diving into setting up Storybook's builders, let's look at how the CLI configures them. When you initialize Storybook (via npx storybook@latest init), the CLI automatically detects which builder to use based on your application. For example, if you're working with Vite, it will install the Vite builder. If you're working with Webpack, it installs the Webpack 5 builder by default.

Additionally, you can also provide a flag to Storybook's CLI and specify the builder you want to use:

Storybook uses the Webpack 5 builder by default if you don't specify one. If you want to use a different builder in your application, these docs detail how you can set up Storybook's supported builders.

**Examples**:

```text
npx storybook@latest init --builder <webpack5 | vite>
```

---

## Code contributions

**URL**: https://storybook.js.org/docs/contribute/code

**Contents**:
- Code contributions
- Prerequisites
- Initial setup
- Run your first sandbox
- Running a different sandbox template
- Running tests
- Start developing
- Check your work

Contribute a new feature or bug fix to Storybook's monorepo. This page outlines how to get your environment set up to contribute code.

Start by forking the Storybook monorepo and cloning it locally.

Storybook uses the Yarn package manager. Use Corepack to set up the correct version for use with Storybook.

Storybook development happens in a set of sandboxes which are templated Storybook environments corresponding to different user setups. Within each sandbox, we inject a set of generalized stories that allow us to test core features and addons in all such environments.

To run a sandbox locally, you can use the start command:

It will install the required prerequisites, build the code, create and link a starter example based on a Vite React setup and finally start the Storybook server.

If all goes well, you should see the sandbox running.

By default, the start command is configured to initialize a Vite-based React template. If you're planning on working on a different renderer instead, you can do so as well. Start by running the task command as follows:

When prompted, answer the questions as accurately as possible to allow Storybook to determine your goals. After answering these questions, you should see the entire command with the options you've selected should you require to re-run it.

The yarn task command takes a few development shortcuts that can catch you off guard when switching branches and may require you to re-run both the install and compile tasks. You can speed up the process by running the command with the start-from=install flag.

After successfully running your first sandbox, you should have a fully functional Storybook version built on your local machine. Before jumping onto any code changes, verifying everything is working is essential—specifically, the test suite.

Run the following command to execute the tests:

Now that you've verified your setup, it's time to jump into code. The simplest way is to run one of the sandboxes in one terminal w

*[Content truncated - see full docs]*

**Examples**:

```text
git clone https://github.com/your-username/storybook.git
cd storybook
```

```text
corepack enable
```

```text
git checkout -b my-first-storybook-contribution
```

---

## Compiler support

**URL**: https://storybook.js.org/docs/configure/integration/compilers

**Contents**:
- Compiler support
- SWC
- Babel
  - Configure
  - Working with Create React App
- Troubleshooting
  - The SWC compiler doesn't work with React
  - Babel configuration not working

Javascript compilers are essential in optimizing and transforming code, enhancing performance, and ensuring compatibility across different environments. Storybook provides support for the leading compilers, ensuring lightning-fast build time and execution with SWC or leveraging Babel with its extensive ecosystem of plugins and presets to allow you to use the latest features of the ecosystem with minimal configuration required for your Webpack-based project.

SWC is a fast, highly extensible tool for compiling and bundling modern JavaScript applications. Powered by Rust, it improves performance and reduces build times. Storybook includes a built-in integration with SWC, allowing zero-configuration setup and built-in types for APIs. If you've initialized Storybook in a Webpack-based project with any of the supported frameworks, except Angular, Create React App, Ember.js and Next.js, it will automatically use SWC as its default, providing you with faster loading time.

Support for the SWC builder is currently experimental for Next.js projects, and it's not enabled by default. It requires you to opt in to use it. For more information on configuring SWC with the supported frameworks, see the SWC API documentation.

Babel is a widely adopted JavaScript compiler providing a modular architecture and extensive plugin system to support a wide range of use cases, enabling access to the cutting-edge features of the tooling ecosystem. Storybook provides a seamless integration with Babel, allowing you to share a standard setup between your project and Storybook without any additional configuration.

If you're not using Storybook 7, please reference the previous documentation for guidance on configuring your Babel setup.

By default, Babel provides an opinionated configuration that works for most projects, relying on two distinct methods for configuring projects with the tool:

Storybook relies on an agnostic approach to configuring Babel, enabling you to provide the necessary con

*[Content truncated - see full docs]*

**Examples**:

```python
// Replace your-framework with the webpack-based framework you are using (e.g., react-webpack5)
import type { StorybookConfig } from '@storybook/your-framework';
 
const config: StorybookConfig = {
  framework: {
    name: '@storybook/your-framework',
    options: {},
  },
  swc: (config, options) => ({
    jsc: {
      transform: {
        react: {
          runtime: 'automatic',
        },
      },
    },
  }),
};
 
export default config;
```

```text
BABEL_SHOW_CONFIG_FOR=.storybook/preview.js yarn storybook
```

---

## Configure Storybook

**URL**: https://storybook.js.org/docs/configure

**Contents**:
- Configure Storybook
- Configure your Storybook project
- Configure story loading
  - With a configuration object
  - With a directory
  - With a custom implementation
    - Known limitations
- Configure story rendering

Storybook is configured via a folder called .storybook, which contains various configuration files.

Note that you can change the folder that Storybook uses by setting the -c flag to your storybook dev and storybook build CLI commands.

Storybook's main configuration (i.e., the main.js|ts) defines your Storybook project's behavior, including the location of your stories, the addons you use, feature flags and other project-specific settings. This file should be in the .storybook folder in your project's root directory. You can author this file in either JavaScript or TypeScript. Listed below are the available options and examples of how to use them.

This configuration file is a preset and, as such, has a powerful interface, which can be further customized. Read our documentation on writing presets to learn more.

By default, Storybook will load stories from your project based on a glob (pattern matching string) in .storybook/main.js|ts that matches all files in your project with extension .stories.*. The intention is for you to colocate a story file along with the component it documents.

If you want to use a different naming convention, you can alter the glob using the syntax supported by picomatch.

For example, if you wanted to pull both .md and .js files from the my-project/src/components directory, you could write:

Additionally, you can customize your Storybook configuration to load your stories based on a configuration object. For example, if you wanted to load your stories from a packages/components directory, you could adjust your stories configuration field into the following:

When Storybook starts, it will look for any file containing the stories extension inside the packages/components directory and generate the titles for your stories.

You can also simplify your Storybook configuration and load the stories using a directory. For example, if you want to load all the stories inside a packages/MyStories, you can adjust the configuration as such:

You can

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

```text
•
└── components
    ├── Button.js
    └── Button.stories.js
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { StorybookConfig } from '@storybook/your-framework';
 
const config: StorybookConfig = {
  framework: '@storybook/your-framework',
  stories: ['../my-project/src/components/*.@(js|md)'],
};
 
export default config;
```

---

## Contributing a Storybook framework

**URL**: https://storybook.js.org/docs/contribute/framework

**Contents**:
- Contributing a Storybook framework
- How to make a framework
  - 1. Decide on a package name
  - 2. Consider what your framework will need to do
  - 3. Write the documentation
  - 4. Author the framework itself
    - package.json (example)
    - preset.js (example)

A Storybook framework is a node package that enables out-of-the-box support for either a metaframework (Next.js, NuxtJS, SvelteKit) or a combination of builder (Webpack, Vite) plus renderer (React, Angular, Vue 3, web components, etc).

For metaframeworks, the Storybook framework also takes care of additional configuration necessary to make Storybook behave similarly to apps generated by the metaframework. For example, @storybook/nextjs recreates or mocks a number of features of Next.js apps inside Storybook.

For your reference, you can view all of the official Storybook frameworks, including their full source code and documentation.

The name should start with storybook-framework- and then correspond to what your framework supports. For example, a framework targeting SvelteKit would be storybook-framework-svelte-kit and a framework targeting Stencil with Vite would be storybook-framework-stencil-vite. When not targeting a metaframework, the naming convention is storybook-framework-<renderer>-<builder>.

The goal is to make Storybook behave—out-of-the-box—as similarly as possible to the metaframework or builder-renderer combination you’re targeting.

For metaframeworks, this means attempting to recreate any builder or babel configuration provided by the metaframework. You should try to do so in a way that respects the user's existing project configuration as much as possible.

The library or libraries your framework supports may have different major versions available. Consider which versions of each library your framework will support. You will need to account for the changes within those different versions or split your framework into different versions/packages itself to support each library version. To speed up maintenance, please consider adding integration tests for the various library versions your framework supports.

Before writing any code, write a helpful README that contains installation instructions and a list of available features. Use the README for 

*[Content truncated - see full docs]*

**Examples**:

```text
{
  "name": "<your-framework-name>",
  "version": "1.0.0",
  "description": "Storybook for <meta-framework-name> or <renderer> & <builder>",
  "keywords": [
    "Storybook",
    "<meta-framework-name>",
    "<renderer>",
    "<builder>",
    "<anything>",
    "<else>",
    "<relevant>"
  ],
  "homepage": "<your package's homepage>",
  "bugs": {
    "url": "https://github.com/<your-org>/<your-repo>/issues"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/<your-org>/<your-r
...
```

---

## Controls

**URL**: https://storybook.js.org/docs/essentials/controls

**Contents**:
- Controls
- Choosing the control type
- Custom control type matchers
- Fully custom args
  - Dealing with complex values
- Creating and editing stories from controls
  - Create a new story
  - Edit a story

Storybook Controls gives you a graphical UI to interact with a component's arguments dynamically without needing to code. Use the Controls panel to edit the inputs to your stories and see the results in real-time. It's a great way to explore your components and test different states.

Controls do not require any modification to your components. Stories for controls are:

To use Controls, you need to write your stories using args. Storybook will automatically generate UI controls based on your args and what it can infer about your component. Still, you can configure the controls further using argTypes, see below.

If you have stories in the older pre-Storybook 6 style, check the args & controls migration guide to learn how to convert your existing stories for args.

By default, Storybook will choose a control for each arg based on its initial value. This will work well with specific arg types (e.g., boolean or string). To enable them, add the component annotation to the default export of your story file, and it will be used to infer the controls and auto-generate the matching argTypes for your component using react-docgen, a documentation generator for React components that also includes first-class support for TypeScript.

For instance, suppose you have a variant arg on your story that should be primary or secondary:

By default, Storybook will render a free text input for the variant arg:

It works as long as you type a valid string into the auto-generated text control. Still, it's not the best UI for our scenario, given that the component only accepts primary or secondary as variants. Let’s replace it with Storybook’s radio component.

We can specify which controls get used by declaring a custom argType for the variant property. ArgTypes encode basic metadata for args, such as name, description, and defaultValue for an arg. These get automatically filled in by Storybook Docs.

ArgTypes can also contain arbitrary annotations, which the user can override. Since vari

*[Content truncated - see full docs]*

**Examples**:

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
import type { Meta } from '@storybook/your-framework';
 
import { Button } from './Button';
 
const meta = {
  component: Button,
} satisfies Meta<typeof Button>;
 
export default meta;
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
 
export const Primary: Story = {
  args: {
    variant: 'primary',
  },
};
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Meta } from '@storybook/your-framework';
 
import { Button } from './Button';
 
const meta = {
  component: Button,
  argTypes: {
    variant: {
      options: ['primary', 'secondary'],
      control: { type: 'radio' },
    },
  },
} satisfies Meta<typeof Button>;
 
export default meta;
```

---

## Design integrations

**URL**: https://storybook.js.org/docs/sharing/design-integrations

**Contents**:
- Design integrations
- Figma
  - Embed Storybook in Figma with the plugin
    - Install plugin
    - Link stories to Figma components
    - View stories in Figma
  - Embed Figma in Storybook with the addon
    - Install design addon

Storybook integrates with design tools to speed up your development workflow. That helps you debug inconsistencies earlier in the design process, discover existing components to reuse, and compare designs to stories.

Figma is a collaborative UI design tool that allows multiple people to work on the same design simultaneously in the browser. There are two ways to integrate Storybook and Figma.

Storybook Connect is a Figma plugin that allows you to embed component stories in Figma. It’s powered by Storybook embeds and Chromatic, a publishing tool created by the Storybook team.

Before we begin, you must have a Storybook published to Chromatic. It provides the index, versions, and access control that back the plugin.

Go to Storybook Connect to install the plugin.

In Figma, open the command palette (in Mac OS, use Command + /, in Windows use Control + /) and type Storybook Connect to enable it.

Follow the instructions to connect and authenticate with Chromatic.

Link stories to Figma components, variants, and instances.

Go to a story in a Storybook published on Chromatic. Make sure it’s on the branch you want to link. Then copy the URL to the story.

In Figma, select the component, open the plugin, and paste the URL.

Chromatic will automatically update your linked stories to reflect the most recent Storybook published on the branch you linked. That means the link persists even as you push new code.

The plugin does not support linking stories to Figma layers.

Once they're connected, you'll be able to view the story by clicking the link in the sidebar. Click "View story". Alternatively, open the plugin by using the command palette (in Mac OS, use Command + /, in Windows, use Control + /), then type Storybook Connect.

Designs addon allows you to embed Figma files and prototypes in Storybook.

Run the following command to install the addon.

The CLI's add command automates the addon's installation and setup. To install it manually, see our documentation on how to 

*[Content truncated - see full docs]*

**Examples**:

```text
npx storybook@latest add @storybook/addon-designs
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
import type { Meta, StoryObj } from '@storybook/your-framework';
 
import { MyComponent } from './MyComponent';
 
// More on default export: https://storybook.js.org/docs/writing-stories/#default-export
const meta = {
  component: MyComponent,
} satisfies Meta<typeof MyComponent>;
 
export default meta;
type Story = StoryObj<typeof meta>;
 
export const Example: Story = {
  parameters: {
    de
...
```

---

## Environment variables

**URL**: https://storybook.js.org/docs/configure/environment-variables

**Contents**:
- Environment variables
- Using .env files
  - With Vite
- Using Storybook configuration
- Using environment variables to choose the browser
- Troubleshooting
  - Environment variables are not working

You can use environment variables in Storybook to change its behavior in different “modes”. If you supply an environment variable prefixed with STORYBOOK_, it will be available in process.env when using Webpack, or import.meta.env when using the Vite builder:

Do not store any secrets (e.g., private API keys) or other types of sensitive information in your Storybook. Environment variables are embedded into the build, meaning anyone can view them by inspecting your files.

Then we can access these environment variables anywhere inside our preview JavaScript code like below:

You can also access these variables in your custom <head>/<body> using the substitution %STORYBOOK_X%, for example: %STORYBOOK_THEME% will become red.

If using the environment variables as attributes or values in JavaScript, you may need to add quotes, as the value will be inserted directly, for example: <link rel="stylesheet" href="%STORYBOOK_STYLE_URL%" />.

You can also use .env files to change Storybook's behavior in different modes. For example, if you add a .env file to your project with the following:

Then you can access this environment variable anywhere, even within your stories:

Out of the box, Storybook provides a Vite builder, which does not output Node.js globals like process.env. To access environment variables in Storybook (e.g., STORYBOOK_, VITE_), you can use import.meta.env. For example:

You can also use specific files for specific modes. Add a .env.development or .env.production to apply different values to your environment variables.

You can also pass these environment variables when you are building your Storybook with build-storybook.

Then they'll be hardcoded to the static version of your Storybook.

Additionally, you can extend your Storybook configuration file (i.e., .storybook/main.js|.ts) and provide a configuration field that you can use to define specific variables (e.g., API URLs). For example:

When Storybook loads, it will enable you to access them in your st

*[Content truncated - see full docs]*

**Examples**:

```text
STORYBOOK_THEME=red STORYBOOK_DATA_KEY=12345 npm run storybook
```

```text
console.log(process.env.STORYBOOK_THEME);
console.log(process.env.STORYBOOK_DATA_KEY);
```

```text
STORYBOOK_DATA_KEY=12345
```

---

## Essentials

**URL**: https://storybook.js.org/docs/essentials

**Contents**:
- Essentials
  - Configuration
  - Disabling features

Storybook essentials is a set of tools that help you build, test, and document your components within Storybook. It includes the following:

Essentials is "zero-config”. It comes with a recommended configuration out of the box.

Many of the features above can be configured via parameters. See each feature's documentation (linked above) for more details.

If you need to disable any of the essential features, you can do it by changing your .storybook/main.js|ts file.

For example, if you wanted to disable the backgrounds feature, you would apply the following change to your Storybook configuration:

You can use the following keys for each individual feature: actions, backgrounds, controls, highlight, measure, outline, toolbars, and viewport.

**Examples**:

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { StorybookConfig } from '@storybook/your-framework';
 
const config: StorybookConfig = {
  framework: '@storybook/your-framework',
  stories: ['../src/**/*.mdx', '../src/**/*.stories.@(js|jsx|mjs|ts|tsx)'],
  features: {
    backgrounds: false, // 👈 disable the backgrounds feature
  },
};
 
export default config;
```

---

## Feature support for frameworks

**URL**: https://storybook.js.org/docs/configure/integration/frameworks-feature-support

**Contents**:
- Feature support for frameworks
- Core frameworks
- Community frameworks
- Deprecated

Storybook integrates with many popular frontend frameworks. We do our best to keep feature parity amongst frameworks, but it’s tricky for our modest team to support every framework.

Below is a comprehensive table of what’s supported in which framework integration. If you’d like a certain feature supported in your framework, we welcome pull requests.

Core frameworks have dedicated maintainers or contributors who are responsible for maintaining the integration. As such, you can use most Storybook features in these frameworks.

Community frameworks have fewer contributors which means they may not be as up to date as core frameworks. If you use one of these frameworks for your job, please consider contributing to its integration with Storybook.

To align the Storybook ecosystem with the current state of frontend development, the following features and addons are now deprecated, no longer maintained, and will be removed in future versions of Storybook

---

## Features and behavior

**URL**: https://storybook.js.org/docs/configure/user-interface/features-and-behavior

**Contents**:
- Features and behavior
- Customize the UI
  - Override sidebar visibility
  - Configure the toolbar
- Configuring through URL parameters

To control the layout of Storybook’s UI you can use addons.setConfig in your .storybook/manager.js:

The following table details how to use the API values:

The following options are configurable under the sidebar namespace:

The following options are configurable under the toolbar namespace:

The following options are configurable under the layoutCustomisations namespace:

The showSidebar and showToolbar functions let you hide parts of the UI that are essential to Storybook's functionality. If misused, they can make navigation impossible. When hiding the sidebar, ensure the displayed page provides an alternative means of navigation.

Storybook's UI is highly customizable. Its API and configuration options, available via the showSidebar and showToolbar functions, allow you to control how the sidebar and toolbar elements are displayed. Both functions will enable you to include some default behavior and can be overridden to customize the UI to your needs.

The sidebar, present on the left of the screen, contains the search function and navigation menu. Users may show or hide it with a keyboard shortcut. If you want to force the sidebar to be visible or hidden in certain places, you can define a showSidebar function in layoutCustomisations. Below are the available parameters passed to this function and an overview of how to use them.

If you're hiding the sidebar through showSidebar, ensure the displayed page provides an alternative means of navigation.

By default, Storybook displays a toolbar at the top of the UI, allowing you to access menus from addons (e.g., viewport, background), or custom defined menus. However, if you want to customize the toolbar's behavior, you can use the showToolbar function. Listed below are the available options and an overview of how to use them.

You can use URL parameters to configure some of the available features:

**Examples**:

```python
import { addons, type State } from 'storybook/manager-api';
 
addons.setConfig({
  navSize: 300,
  bottomPanelHeight: 300,
  rightPanelWidth: 300,
  panelPosition: 'bottom',
  enableShortcuts: true,
  showToolbar: true,
  theme: undefined,
  selectedPanel: undefined,
  initialActive: 'sidebar',
  layoutCustomisations: {
    showSidebar(state: State, defaultValue: boolean) {
      return state.storyId === 'landing' ? false : defaultValue;
    },
    showToolbar(state: State, defaultValue: boolean
...
```

```python
import { addons, type State } from 'storybook/manager-api';
 
addons.setConfig({
  layoutCustomisations: {
    // Hide the sidebar on the landing page, which has its own nav links to other pages.
    showSidebar(state: State, defaultValue: boolean) {
      if (state.storyId === 'landing' && state.viewMode === 'docs') {
        return false;
      }
 
      return defaultValue;
    },
  },
});
```

```python
import { addons, type State } from 'storybook/manager-api';
 
addons.setConfig({
  layoutCustomisations: {
    // Always hide the toolbar on docs pages, and respect user preferences elsewhere.
    showToolbar(state: State, defaultValue: boolean) {
      if (state.viewMode === 'docs') {
        return false;
      }
 
      return defaultValue;
    },
  },
});
```

---

## Frequently Asked Questions

**URL**: https://storybook.js.org/docs/faq

**Contents**:
- Frequently Asked Questions
- Error: No angular.json file found
- How can I opt-out of Angular Ivy?
- How can I opt-out of Angular ngcc?
- How can I run coverage tests with Create React App and leave out stories?
- How do I setup Storybook to share Webpack configuration with Next.js?
- How do I fix module resolution in special environments?
- How do I setup the new React Context Root API with Storybook?

Here are some answers to frequently asked questions. If you have a question, you can ask it in our GitHub discussions.

Storybook can be set up for both single-project and multi-project Angular workspaces. To set up Storybook for a project, run the install command at the root of the workspace where the angular.json file is located. During initialization, the .storybook folder will be created and the angular.json file will be edited to add the Storybook configuration for the selected project. It's important to run the command at the root level to ensure that Storybook detects all projects correctly.

In case you are having trouble with Angular Ivy you can deactivate it in your main.js|ts:

In case you postinstall ngcc, you can disable it:

Please report any issues related to Ivy in our GitHub Issue Tracker as the support for View Engine will be dropped in a future release of Angular.

Create React App does not allow providing options to Jest in your package.json, however you can run jest with commandline arguments:

If you're using Yarn as a package manager, you'll need to adjust the command accordingly.

You can generally reuse Webpack rules by placing them in a file that is require()-ed from both your next.config.js and your .storybook/main.js|ts files. For example:

In case you are using Yarn Plug-n-Play or your project is set up within a mono repository environment, you might run into issues with module resolution similar to this when running Storybook:

To fix this, you can wrap the package name inside your Storybook configuration file (i.e., .storybook/main.js|ts) as follows:

If your installed React Version equals or is higher than 18.0.0, the new React Root API is automatically used and the newest React concurrent features can be used.

You can opt-out from the new React Root API by setting the following property in your .storybook/main.js|ts file:

A common error is that an addon tries to access the "channel", but the channel is not set. It can happen in a f

*[Content truncated - see full docs]*

**Examples**:

```typescript
export default {
  stories: [
    /* ... */
  ],
  addons: [
    /* ... */
  ],
  framework: {
    name: '@storybook/angular',
    options: {
      enableIvy: false,
    },
  },
};
```

```typescript
export default {
  stories: [
    /* ... */
  ],
  addons: [
    /* ... */
  ],
  framework: {
    name: '@storybook/angular',
    options: {
      enableNgcc: false,
    },
  },
};
```

```text
npm test -- --coverage --collectCoverageFrom='["src/**/*.{js,jsx}","!src/**/stories/*"]'
```

---

## Get started with Storybook

**URL**: https://storybook.js.org/docs/

**Contents**:
- Get started with Storybook
- What is Storybook?
- Install Storybook
- Main concepts
- Additional resources

Welcome to Storybook's documentation ✦ Learn how to get started with Storybook in your project. Then, explore Storybook's main concepts and discover additional resources to help you grow and maintain your Storybook.

Storybook is a frontend workshop for building UI components and pages in isolation. It helps you develop and share hard-to-reach states and edge cases without needing to run your whole app. Thousands of teams use it for UI development, testing, and documentation. It's open source and free.

Storybook is a standalone tool that runs alongside your app. It's a zero-config environment that works with any modern frontend framework. You can install Storybook into an existing project or create a new one from scratch.

with Vite (in browser)

Want to know more about installing Storybook? Check out the installation guide.

Storybook is a powerful tool that can help you with many aspects of your UI development workflow. Here are some of the main concepts to get you started.

A story captures the rendered state of a UI component. Each component can have multiple stories, where each story describes a different component state.

Storybook can analyze your components to automatically create documentation alongside your stories. This automatic documentation makes it easier for you to create UI library usage guidelines, design system sites, and more.

Stories are a pragmatic starting point for your UI testing strategy. You already write stories as a natural part of UI development, so testing those stories is a low-effort way to prevent UI bugs over time.

Publishing your Storybook allows you to share your work with others. You can also embed your stories in places like Notion or Figma.

Once you've learned the basics, explore these other ways to get the most out of Storybook.

Latest product updates

**Examples**:

```text
npm create storybook@latest
```

---

## Highlight

**URL**: https://storybook.js.org/docs/essentials/highlight

**Contents**:
- Highlight
- Highlighting DOM Elements
  - Customize style
  - Highlight menu
- Remove highlights
- Reset highlighted elements
- Scroll element into view
- API

Storybook's Highlight feature is a helpful tool for visually debugging your components. It allows you to highlight specific DOM nodes within your story when used directly or enhancing addons such as the Accessibility addon to inform you of accessibility issues within your components.

To highlight DOM elements with the feature, you'll need to emit the HIGHLIGHT event from within a story or an addon. The event payload must contain a selectors property assigned to an array of selectors matching the elements you want to highlight. For example:

We recommend choosing the most specific selector possible to avoid highlighting elements other addons use. This is because the feature tries to match selectors against the entire DOM tree.

By default, highlighted elements contain a standard outline style applied to the selected elements. However, you can enable your custom style by extending the payload object with additional properties to customize the appearance of the highlighted elements. For example:

These properties are optional, and you can use them to customize the appearance of the highlighted elements. The hoverStyles and focusStyles properties are recommended for use with the menu property. Pseudo-classes and pseudo-elements are not supported.

The Highlight feature includes a built-in debugging option, allowing you to select the highlighted elements when you click them. This is particularly useful for inspecting the elements affected by the feature, as it lets you preview a list of elements matching the selector you provided. To enable it, add a menu property in the payload object containing additional information about the elements or trigger actions. Each item must include an id and a title, and you can also provide an optional selectors property to limit the menu item to specific highlighted elements.

When enabled, the menu will be displayed when you click on the selected element matching your provided selectors. However, if you don't want to show any informati

*[Content truncated - see full docs]*

**Examples**:

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
import type { Meta, StoryObj } from '@storybook/your-framework';
 
import { useChannel } from 'storybook/preview-api';
import { HIGHLIGHT } from 'storybook/highlight';
 
import { MyComponent } from './MyComponent';
 
const meta = {
  component: MyComponent,
} satisfies Meta<typeof MyComponent>;
 
export default meta;
type Story = StoryObj<typeof meta>;
 
export const Highlighted: Story = {
  de
...
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
import type { Meta, StoryObj } from '@storybook/your-framework';
 
import { useChannel } from 'storybook/preview-api';
import { HIGHLIGHT } from 'storybook/highlight';
 
import { MyComponent } from './MyComponent';
 
const meta = {
  component: MyComponent,
} satisfies Meta<typeof MyComponent>;
 
export default meta;
type Story = StoryObj<typeof meta>;
 
export const StyledHighlight: Story = {

...
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
import type { Meta, StoryObj } from '@storybook/your-framework';
 
import { useChannel } from 'storybook/preview-api';
import { HIGHLIGHT } from 'storybook/highlight';
 
import { MyComponent } from './MyComponent';
 
const meta = {
  component: MyComponent,
} satisfies Meta<typeof MyComponent>;
 
export default meta;
type Story = StoryObj<typeof meta>;
 
export const StyledHighlight: Story = {

...
```

---

## How to contribute

**URL**: https://storybook.js.org/docs/contribute

**Contents**:
- How to contribute
- Contributor covenant
- Ways to contribute
- Not sure how to get started?

Storybook is a community-oriented open source project that welcomes contributions. Some of our most popular features started with a developer wanting to solve a problem for themselves.

In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to making participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation. Continue reading our contributor covenant »

---

## How to test UIs with Storybook

**URL**: https://storybook.js.org/docs/writing-tests

**Contents**:
- How to test UIs with Storybook
- Get started
- Key concepts
  - Component tests
  - Storybook Test
  - Watch mode
  - CI
  - Coverage

Storybook stories are test cases for your UI components in their various states and configurations. With Storybook, you can develop and test your components at the same time, in multiple ways, with instant feedback.

Storybook tackles UI component testing from a holistic perspective, ensuring that you can not only execute component tests quickly and reliably, but that you also have well established patterns to develop, debug, maintain, and even collaborate on these tests across the development lifecycle.

If your project is using Vite, you can likely use the Vitest addon to run your component tests in Storybook. This addon is built on top of Vitest, a fast and lightweight test runner that works seamlessly with Vite.

Run this command, which will install and configure the Vitest addon and Vitest:

The full installation instructions, including project requirements, are available in the Vitest addon documentation.

Once your project is set up, you will see a testing widget in the bottom of your sidebar. After running tests, you will also see test status indicators on sidebar items. Additionally, many tests can be debugged with an addon panel.

If you cannot use the Vitest addon in your project, you can still run tests using the test-runner.

Next, we’ll cover some key concepts of testing in Storybook.

Testing in Storybook is similar to other testing environments. Most of the knowledge and techniques you’ve been using apply here, too. But there are also some significant improvements.

A component test is a test which:

This combination of using a real browser, simulating behavior, and mocking provides a powerful means of testing the functional aspects of your UI.

In Storybook, the entire testing experience is built around component tests. This means that you can run your tests in the same environment as your stories, with the same tools and techniques.

Storybook Test enables real time testing of your stories, through the Vitest addon. It uses a Vitest plugin to autom

*[Content truncated - see full docs]*

**Examples**:

```text
npx storybook add @storybook/addon-vitest
```

```text
{ 
  "scripts": {
    "test-storybook": "vitest --project=storybook"
  }
}
```

```text
name: Storybook Tests
 
on: [push]
 
jobs:
  test:
    runs-on: ubuntu-latest
    container:
      # Make sure to grab the latest version of the Playwright image
      # https://playwright.dev/docs/docker#pull-the-image
      image: mcr.microsoft.com/playwright:v1.52.0-noble
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: 22.12.0
      
      - name: Install dependencies
        run: npm ci
   
...
```

---

## Images, fonts, and assets

**URL**: https://storybook.js.org/docs/configure/integration/images-and-assets

**Contents**:
- Images, fonts, and assets
- Import assets into stories
- Serving static files via Storybook Configuration
- Reference assets from a CDN
- Absolute versus relative paths
- Referencing Fonts in Stories

Components often rely on images, videos, fonts, and other assets to render as the user expects. There are many ways to use these assets in your story files.

You can import any media assets by importing (or requiring) them. It works out of the box with our default config. But, if you are using a custom webpack config, you’ll need to add the file loader to handle the required files.

Afterward, you can use any asset in your stories:

We recommend serving static files via Storybook to ensure that your components always have the assets they need to load. We recommend this technique for assets that your components often use, like logos, fonts, and icons.

Configure a directory (or a list of directories) where your assets live when starting Storybook. Use the staticDirs configuration element in your main Storybook configuration file (i.e., .storybook/main.js|ts) to specify the directories:

Here ../public is your static directory. Now use it in a component or story like this.

You can also pass a list of directories separated by commas without spaces instead of a single directory.

Or even use a configuration object to define the directories:

Upload your files to an online CDN and reference them. In this example, we’re using a placeholder image service.

Sometimes, you may want to deploy your Storybook into a subpath, like https://example.com/storybook.

In this case, you need to have all your images and media files with relative paths. Otherwise, the browser cannot locate those files.

If you load static content via importing, this is automatic, and you do not have to do anything.

Suppose you are serving assets in a static directory along with your Storybook. In that case, you need to use relative paths to load images or use the base element.

After configuring Storybook to serve assets from your static folder, you can reference those assets in Storybook. For example, you can reference and apply a custom font to your stories. To do this, create a preview-head.html fil

*[Content truncated - see full docs]*

**Examples**:

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
import type { Meta, StoryObj } from '@storybook/your-framework';
 
import imageFile from './static/image.png';
 
import { MyComponent } from './MyComponent';
 
const meta = {
  component: MyComponent,
} satisfies Meta<typeof MyComponent>;
 
export default meta;
type Story = StoryObj<typeof meta>;
 
const image = {
  src: imageFile,
  alt: 'my image',
};
 
export const WithAnImage: Story = {
  r
...
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { StorybookConfig } from '@storybook/your-framework';
 
const config: StorybookConfig = {
  framework: '@storybook/your-framework',
  stories: ['../src/**/*.mdx', '../src/**/*.stories.@(js|jsx|mjs|ts|tsx)'],
  staticDirs: ['../public', '../static'],
};
 
export default config;
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
 
// Assume image.png is located in the "public" directory.
export const WithAnImage: Story = {
  render: () => <img src="/image.png" alt="my ima
...
```

---

## Introduction to addons

**URL**: https://storybook.js.org/docs/addons

**Contents**:
- Introduction to addons
- Storybook basics
- Anatomy of an addon
  - UI-based addons
  - Preset addons

Addons extend Storybook with features and integrations that are not built into the core. Most Storybook features are implemented as addons. For instance: documentation, accessibility testing, interactive controls, among others. The addon API makes it easy for you to configure and customize Storybook in new ways. There are countless addons made by the community that unlocks time-saving workflows.

Browse our addon catalog to install an existing addon or as inspiration for your own addon.

Before writing your first addon, let’s take a look at the basics of Storybook’s architecture. While Storybook presents a unified user interface, under the hood it’s divided down the middle into Manager and Preview.

The Manager is the UI responsible for rendering the:

The Preview area is an iframe where your stories are rendered.

Because both elements run in their own separate iframes, they use a communication channel to keep in sync. For example, when you select a story in the Manager an event is dispatched across the channel notifying the Preview to render the story.

Storybook addons allow you to extend what's already possible with Storybook, everything from the user interface to the API. Each one is classified into two broader categories.

UI-based addons focus on customizing Storybook's user interface to extend your development workflow. Examples of UI-based addons include: Controls, Docs and Accessibility.

Learn how to write an addon »

Preset addons help you integrate Storybook with other technologies and libraries. An examples of a preset addons is preset-create-react-app.

Learn how to write a preset addon »

---

## Measure & outline

**URL**: https://storybook.js.org/docs/essentials/measure-and-outline

**Contents**:
- Measure & outline
- Measure
- Outline
- API
  - Parameters
    - disable

Storybook's measure and outline features give you the necessary tooling to inspect and visually debug CSS layout and alignment issues within your stories. It makes it easy to catch UI bugs early in development.

While working with composite components or page layouts, dealing with whitespace (i.e., margin, padding, border) and individual component measurements can be tedious. It would require that you open up the browser's development tools and manually inspect the DOM tree for issues and UI bugs.

Instead, you can quickly visualize each component's measurements by clicking the measure button in the toolbar. Now when you hover over an element in your story, that element's dimensions and any whitespace (i.e., margin, padding, border) will be shown.

Alternatively you can press the m key on your keyboard to toggle measure on and off.

When building your layouts, checking the visual alignment of all components can be pretty complicated, especially if your components are spread apart or contain unique shapes.

Click the outline button in the toolbar to toggle the outlines associated with all your UI elements, allowing you to spot bugs and broken layouts instantly.

These features contribute the following parameters to Storybook, under the measure or outline namespace:

Disable the feature's behavior. If you wish to disable the feature for the entire Storybook, you should do so in your main configuration file.

This parameter is most useful to allow overriding at more specific levels. For example, if this parameter is set to true at the project level, it could then be re-enabled by setting it to false at the meta (component) or story level.

---

## Migration guide for Storybook 9

**URL**: https://storybook.js.org/docs/releases/migration-guide

**Contents**:
- Migration guide for Storybook 9
- Major breaking changes
- Automatic upgrade
- New projects
- Troubleshooting
- Package structure changes
- Optional migrations
  - test-runner to addon-vitest

Storybook 9 improves performance, compatibility, and stability. Its key features include:

This guide is meant to help you upgrade from Storybook 8.x to 9 successfully!

Migrating from a Storybook version prior to 8?

You'll first need to upgrade to Storybook 8. Then you can return to this guide.

The rest of this guide will help you upgrade successfully, either automatically or manually. But first, there are some breaking changes in Storybook 9. Here are the most impactful changes you should know about before you go further:

If any of these changes apply to your project, please read through the linked migration notes before continuing.

If any of these new requirements or changes are blockers for your project, we recommend to continue using Storybook 8.x.

You may wish to read the full migration notes before migrating. Or you can run the upgrade command below and we’ll try to take care of everything for you!

To upgrade your Storybook, run the upgrade command in the root of your repository:

To add Storybook to a project that isn’t currently using Storybook:

The automatic upgrade should get your Storybook into a working state. If you encounter an error running Storybook after upgrading, here’s what to do:

If you prefer to debug yourself, here are a few useful things you can do to help narrow down the problem:

The following packages are no longer published. Instead they have been consolidated into Storybook's core package, storybook. If a consolidated package had exports, those are available via the replacement path in the table below. See the full migration notes for details.

The following packages have been consolidated and moved into an internal path to indicate that they are now for internal usage only. They will continue to work in 9.x releases, but will likely be removed in 10.0. See the full migration notes for details.

Addon authors may continue to use the internal packages, there is currently not yet any replacement.

In addition to the automigrations

*[Content truncated - see full docs]*

**Examples**:

```text
npx storybook@latest upgrade
```

```text
npm create storybook@latest
```

```typescript
# Convert CSF 2 to CSF 3
npx storybook@latest migrate csf-2-to-3 --glob="**/*.stories.tsx" --parser=tsx
```

---

## Migration guide from Storybook 7.x to 8.6

**URL**: https://storybook.js.org/docs/releases/migration-guide-from-older-version

**Contents**:
- Migration guide from Storybook 7.x to 8.6
- Major breaking changes
- Automatic upgrade
  - Common upgrade issues
    - storyStoreV7:false and storiesOf
    - Missing vite.config.js file
- New projects
- Manual migrations

Storybook 8 focuses on improving performance, compatibility, and stability. Key features include:

This guide is meant to help you upgrade from Storybook 7.x to 8.6 successfully!

Migrating from Storybook 6.x?

You can reference our migration guide for Storybook 6 to 8.

The rest of this guide will help you upgrade successfully, either automatically or manually. But first, there are some breaking changes in Storybook 8. Here are the most impactful changes you should know about before you go further:

If any of these changes apply to your project, please read through the linked migration notes before continuing.

If any of these new requirements or changes are blockers for your project, we recommend to continue using Storybook 7.x.

You may wish to read the full migration notes before migrating. Or you can follow the instructions below and we’ll try to take care of everything for you!

To upgrade your Storybook:

While we'll do our best to upgrade your project automatically, there is one issue worth mentioning that you might encounter during the upgrade process:

If you have storyStoreV7: false in your .storybook/main.js, you will need to remove it before you're able to upgrade to Storybook 8.

If you are using the storiesOf API (which requires storyStoreV7: false in Storybook 7), you will need to either migrate your stories to CSF or use the new indexer API to continue creating stories dynamically.

If you are using Vite, you may now need to create a vite.config.js file in your project root to allow newer versions of Vite to work with Storybook. Additionally, you may need to install and configure a Vite plugin for your framework. More information is available in the full migration notes.

To add Storybook to a project that isn’t currently using Storybook:

In addition to the automated upgrades above, there are manual migrations that might be required to get Storybook 8 working in your project. We’ve tried to minimize this list to make it easier to upgrade. These inc

*[Content truncated - see full docs]*

**Examples**:

```text
npx storybook@latest upgrade
```

```text
npm create storybook@latest
```

```text
# Convert stories in MDX to CSF
npx storybook@latest migrate mdx-to-csf --glob "src/**/*.stories.mdx"
```

---

## Package Composition

**URL**: https://storybook.js.org/docs/sharing/package-composition

**Contents**:
- Package Composition
- For consumers
  - Set up
  - Switching versions
- For authors
  - Automatic version selection
  - Show a version selector

Storybook is widely used by component libraries and design systems. Design system authors can automatically compose their design systems inside their consumer’s Storybooks.

For example, if you use a design system package, its stories can appear alongside your own. That makes it convenient to cross reference usage documentation without leaving Storybook.

Composition via a package requires a secure integration between the service where you publish Storybook and Storybook’s own APIs. We recommend publishing Storybook to Chromatic for full support of these features.

Composition happens automatically if the package supports it. When you install the package, Storybook will load its stories alongside your own.

If you want to configure how the composed Storybook behaves, you can disable the ref element in your .storybook/main.js

Change the version of the composed Storybook to see how the library evolves. This requires configuration from the package author.

Component library authors can expand adoption by composing their components in their consumer’s Storybooks.

Add a storybook property in your published package.json that contains an object with a url field. Point the URL field to a published Storybook at the version you want.

If you're using Chromatic, you can provide a single URL for your Storybook in the storybook.url field. You do not need to change the URL each time you publish a new version. Storybook will automatically find the correct URL for your package. For example:

In this example xyz123 is your Chromatic project id. Storybook will automatically compose in the Storybook published to that project corresponding to the version the user has installed.

If you're using Chromatic, you can provide a list of versions for the user to choose from to experiment with other versions of your package.

**Examples**:

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { StorybookConfig } from '@storybook/your-framework';
 
const config: StorybookConfig = {
  framework: '@storybook/your-framework',
  stories: ['../src/**/*.mdx', '../src/**/*.stories.@(js|jsx|mjs|ts|tsx)'],
  refs: {
    'package-name': { disable: true },
  },
};
 
export default config;
```

```text
{
  "storybook": {
    "url": "https://host.com/your-storybook-for-this-version"
  }
}
```

```text
{
  "storybook": {
    "url": "https://master--xyz123.chromatic.com"
  }
}
```

---

## Publish Storybook

**URL**: https://storybook.js.org/docs/sharing/publish-storybook

**Contents**:
- Publish Storybook
- Build Storybook as a static web application
  - Customizing the build for performance
  - Build Storybook for older browsers
- Publish Storybook with Chromatic
  - Setup CI to publish automatically
  - Review with your team
  - Versioning and history

Teams publish Storybook online to review and collaborate on works in progress. That allows developers, designers, PMs, and other stakeholders to check if the UI looks right without touching code or requiring a local dev environment.

First, we'll need to build Storybook as a static web application. The functionality is already built-in and pre-configured for most supported frameworks. Run the following command inside your project's root directory:

You can provide additional flags to customize the command. Read more about the flag options here.

Storybook will create a static web application capable of being served by any web server. Preview it locally by running the following command:

By default, Storybook's production build will encapsulate all stories and documentation into the production bundle. This is ideal for small projects but can cause performance issues for larger projects or when decreased build times are a priority (e.g., testing, CI/CD). If you need, you can customize the production build with the test option in your main.js|ts configuration file and adjust your build script to enable the optimizations with the --test flag.

The Storybook app's UI supports modern browsers. If you need to run the app in older, unsupported browsers, you can use the --preview-only CLI flag to build Storybook in "preview-only" mode. This skips building the Storybook manager (the UI surrounding your stories) and only builds the preview (the iframe that contains your stories). That makes your Storybook builder and its configuration solely responsible for which browsers are supported.

When in "preview-only" mode, the normal entry point, /index.html, will result in a 404, because the client-side router is not available. To work around this, start from the /iframe.html route and add the ?navigator=true query parameter to the URL. This will render a basic, HTML-only sidebar inside the preview so that you can navigate to your stories. For example, you can access the preview at 

*[Content truncated - see full docs]*

**Examples**:

```text
npm run build-storybook
```

```text
npx http-server ./path/to/build
```

```text
npm run build-storybook -- --test
```

---

## RFC process

**URL**: https://storybook.js.org/docs/contribute/RFC

**Contents**:
- RFC process
- Goal
  - “Feature Request” vs. “RFC”
- The RFC lifecycle
  - 1. Status: Proposed
  - 2. Status: In review
  - 3. Status: accepted/rejected
- Implementing an accepted RFC

The RFC (Request for Comment) process is intended to provide a consistent and controlled path for new features to enter the project. It helps ensure that new features are well-designed, well-implemented, and well-tested, and they do not conflict with the project's overall direction and scope.

Many changes, such as bug fixes and documentation improvements, can be implemented and reviewed via the normal GitHub pull request workflow. Some changes, however, are considered “substantial”, and we ask that these undergo a design process, solicit community input, and reach a consensus among the Storybook core team.

The purpose of the RFC (Request for Comment) process is to:

A feature request is a straightforward and relatively informal way for Storybook users to suggest a new feature or enhancement to the project. While feature requests can provide valuable insights and ideas, they typically do not involve an in-depth design process or require consensus among the core team. Feature requests are usually open to discussion and may or may not be implemented based on factors like popularity, feasibility, and alignment with the project's goals.

On the other hand, an RFC is a more formalized and structured process for proposing substantial changes or additions to the project. It involves following a defined set of steps to ensure that the proposed feature or modification receives proper consideration, design, and feedback. RFCs are typically used for changes that significantly impact the project, such as introducing new API functionality, removing existing features, or establishing new usage conventions. The RFC process aims to foster discussions, gather feedback from a wider audience, and reach consensus among the core team before integrating the proposed change into the project. Accepted RFCs are more likely to be implemented than regular feature requests.

Open a new GitHub discussion in the “RFC” category. Fill out the form as instructed.

Details matter: RFCs that do not 

*[Content truncated - see full docs]*

---

## Sharing

**URL**: https://storybook.js.org/docs/sharing

**Contents**:
- Sharing

You have your components ready and tested. That's great! Now you want to make your component library available to your team or community to help them understand how they work. There are multiple ways you can do that. You can publish your Storybook to services like Chromatic, embed some of your stories in your own website, or use third party services like Figma.

---

## Sidebar & URLS

**URL**: https://storybook.js.org/docs/configure/user-interface/sidebar-and-urls

**Contents**:
- Sidebar & URLS
- Roots
- Permalink to stories
- CSF 3.0 auto-titles
  - Auto-title filename case
  - Auto-title redundant filenames
  - Auto-title prefixes
  - Story Indexers

Storybook’s sidebar lists all your stories grouped by component. When you have many components, you may also wish to group those components. To do so, you can add the / separator to the title of your CSF file, and Storybook will group the stories into groups based on common prefixes:

We recommend using a nesting scheme that mirrors the filesystem path of the components. For example, if you have a file components/modals/Alert.js, name the CSF file components/modals/Alert.stories.js and title it Components/Modals/Alert.

By default, Storybook will treat your top-level nodes as “roots”. Roots are displayed in the UI as “sections” of the hierarchy. Lower level groups will show up as folders:

If you’d prefer to show top-level nodes as folders rather than roots, you can set the sidebar.showRoots option to false in ./storybook/manager.js:

By default, Storybook generates an id for each story based on the component title and the story name. This id in particular is used in the URL for each story, and that URL can serve as a permalink (primarily when you publish your Storybook).

Consider the following story:

Storybook's ID-generation logic will give this the id foo-bar--baz, so the link would be ?path=/story/foo-bar--baz.

It is possible to manually set the story's id, which is helpful if you want to rename stories without breaking permalinks. Suppose you want to change the position in the hierarchy to OtherFoo/Bar and the story name to Moo. Here's how to do that:

Storybook will prioritize the id over the title for ID generation if provided and prioritize the story.name over the export key for display.

Storybook 6.4 introduced CSF 3.0 as an experimental feature, allowing you to write stories more compactly. Suppose you're already using this format to write your stories. In that case, you can omit the title element from the default export and allow Storybook automatically infer it based on the file's physical location. For example, given the following configuration and 

*[Content truncated - see full docs]*

**Examples**:

```python
import { addons } from 'storybook/manager-api';
 
addons.setConfig({
  sidebar: {
    showRoots: false,
  },
});
```

```python
// Replace your-framework with the name of your framework
import type { Meta, StoryObj } from '@storybook/your-framework';
 
import { Foo } from './Foo';
 
const meta = {
  /* 👇 The title prop is optional.
   * See https://storybook.js.org/docs/configure/#configure-story-loading
   * to learn how to generate automatic titles
   */
  title: 'Foo/Bar',
  component: Foo,
} satisfies Meta<typeof Foo>;
 
export default meta;
type Story = StoryObj<typeof meta>;
 
export const Baz: Story = {};
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Meta, StoryObj } from '@storybook/your-framework';
 
import { Foo } from './Foo';
 
const meta = {
  /* 👇 The title prop is optional.
   * See https://storybook.js.org/docs/configure/#configure-story-loading
   * to learn how to generate automatic titles
   */
  title: 'OtherFoo/Bar',
  component: Foo,
  id: 'Foo/Bar', // Or 'foo-bar' if you prefer
} satisfies Meta<typeof Foo>;
 
ex
...
```

---

## Story layout

**URL**: https://storybook.js.org/docs/configure/story-layout

**Contents**:
- Story layout
- Global layout
- Component layout
- Story layout

The layout parameter allows you to configure how stories are positioned in Storybook's Canvas tab.

You can add the parameter to your ./storybook/preview.js, like so:

In the example above, Storybook will center all stories in the UI. layout accepts these options:

You can also set it at a component level like so:

Or even apply it to specific stories like so:

**Examples**:

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Preview } from '@storybook/your-framework';
 
const preview: Preview = {
  parameters: {
    layout: 'centered',
  },
};
 
export default preview;
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Meta } from '@storybook/your-framework';
 
import { Button } from './Button';
 
const meta = {
  component: Button,
  // Sets the layout parameter component wide.
  parameters: {
    layout: 'centered',
  },
} satisfies Meta<typeof Button>;
 
export default meta;
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
 
export const WithLayout: Story = {
  parameters: {
    layout: 'centered',
  },
};
```

---

## Story rendering

**URL**: https://storybook.js.org/docs/configure/story-rendering

**Contents**:
- Story rendering
- Running code for every story
- Adding to <head>
- Adding to <body>

In Storybook, your stories render in a particular “preview” iframe (also called the Canvas) inside the larger Storybook web application. The JavaScript build configuration of the preview is controlled by a builder config, but you also may want to run some code for every story or directly control the rendered HTML to help your stories render correctly.

Code executed in the preview file (.storybook/preview.js|ts) runs for every story in your Storybook. This is useful for setting up global styles, initializing libraries, or anything else required to render your components.

Here's an example of how you might use the preview file to initialize a library that must run before your components render:

If you need to add extra elements to the head of the preview iframe, for instance, to load static stylesheets, font files, or similar, you can create a file called .storybook/preview-head.html and add tags like this:

Storybook will inject these tags into the preview iframe where your components render, not the Storybook application UI.

However, it's also possible to modify the preview head HTML programmatically using a preset defined in the main.js file. Read the presets documentation for more information.

Sometimes, you may need to add different tags to the <body>. Helpful for adding some custom content roots.

You can accomplish this by creating a file called preview-body.html inside your .storybook directory and adding tags like this:

If using relative sizing in your project (like rem or em), you may update the base font-size by adding a style tag to preview-body.html:

Storybook will inject these tags into the preview iframe where your components render, not the Storybook application UI.

Just like how you have the ability to customize the preview head HTML tag, you can also follow the same steps to customize the preview body with a preset. To obtain more information on how to do this, refer to the presets documentation.

**Examples**:

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Preview } from '@storybook/your-framework';
 
import { initialize } from '../lib/your-library';
 
initialize();
 
const preview: Preview = {
  // ...
};
 
export default preview;
```

```vue
<!--
Pull in static files served from your Static directory or the internet
Example:
`main.js|ts` is configured with staticDirs: ['../public'] and your font is located in the `fonts`
directory inside your `public` directory
-->
<link rel="preload" href="/fonts/my-font.woff2" />
 
<!-- Or you can load custom head-tag JavaScript: -->
<script src="https://use.typekit.net/xxxyyy.js"></script>
<script>
  try {
    Typekit.load();
  } catch (e) {}
</script>
```

```text
<div id="custom-root"></div>
```

---

## Storybook Addons

**URL**: https://storybook.js.org/docs/configure/user-interface/storybook-addons

**Contents**:
- Storybook Addons
- Addon features
- Essential, core and community addons

A key strength of Storybook is its extensibility. Use addons to extend and customize Storybook to fit your team’s development workflow.

Addons are integral to the way Storybook works. Many of Storybook's core features are implemented as addons, such as addon-docs.

The most obvious thing addons affect in Storybook is the UI of Storybook itself. Within the UI the toolbar and addons panel are the two chief places addons will appear.

Addons can also hook into the rendering of your story in the preview pane via injecting their own decorators.

Finally, addons can affect the build setup of Storybook by injecting their own webpack configuration to allow the use of other tools in Storybook. Addons that do only this are often referred to as presets.

There are many, many Storybook addons, but they can be roughly categorized into two areas:

---

## Storybook Composition

**URL**: https://storybook.js.org/docs/sharing/storybook-composition

**Contents**:
- Storybook Composition
- Compose published Storybooks
- Compose local Storybooks
- Compose Storybooks per environment
- Troubleshooting
  - Storybook composition is not working with my project

Composition allows you to browse components from any Storybook accessible via URL inside your local Storybook. You can compose any Storybook published online or running locally no matter the view layer, tech stack, or dependencies.

You’ll see the composed Storybook’s stories in the sidebar alongside your own. This unlocks common workflows that teams often struggle with:

In your .storybook/main.js|ts file add a refs field with information about the reference Storybook. Pass in a URL to a statically built Storybook.

Addons in composed Storybooks will not work as they normally do in a non-composed Storybook.

You can also compose multiple Storybooks that are running locally. For instance, if you have a React Storybook and an Angular Storybook running on different ports, you can update your configuration file (i.e., .storybook/main.js|ts) and reference them as follows:

Adding this configuration will combine React and Angular Storybooks into your current one. You’ll see the changes being applied automatically when either of these changes. Enabling you to develop both frameworks in sync.

You can also compose Storybooks based on the current development environment (e.g., development, staging, production). For instance, if the project you're working on already has a published Storybook but also includes a version with cutting-edge features not yet released, you can adjust the composition based on that. For example:

Similar to other fields available in Storybook’s configuration file, the refs field can also be a function that accepts a config parameter containing Storybook’s configuration object. See the API reference for more information.

If you're working with an outdated Storybook version or have a project-specific requirement that prevents you from updating your Storybook to the latest version, you can rely on the Storybook CLI to generate the index.json file when you deploy your Storybook. For example:

The usage of a specific version of the CLI is intended as th

*[Content truncated - see full docs]*

**Examples**:

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { StorybookConfig } from '@storybook/your-framework';
 
const config: StorybookConfig = {
  framework: '@storybook/your-framework',
  stories: ['../src/**/*.mdx', '../src/**/*.stories.@(js|jsx|mjs|ts|tsx)'],
  refs: {
    'design-system': {
      title: 'Storybook Design System',
      url: 'https://master--5ccbc373887ca40020446347.chromatic.com/',
      expanded: false, // Optional, 
...
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { StorybookConfig } from '@storybook/your-framework';
 
const config: StorybookConfig = {
  framework: '@storybook/your-framework',
  stories: ['../src/**/*.mdx', '../src/**/*.stories.@(js|jsx|mjs|ts|tsx)'],
  refs: {
    react: {
      title: 'React',
      url: 'http://localhost:7007',
    },
    angular: {
      title: 'Angular',
      url: 'http://localhost:7008',
    },
  },
};
 
...
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { StorybookConfig } from '@storybook/your-framework';
 
const config: StorybookConfig = {
  framework: '@storybook/your-framework',
  stories: ['../src/**/*.mdx', '../src/**/*.stories.@(js|jsx|mjs|ts|tsx)'],
 
  // 👇 Retrieve the current environment from the configType argument
  refs: (config, { configType }) => {
    if (configType === 'DEVELOPMENT') {
      return {
        react: 
...
```

---

## Storybook for Angular

**URL**: https://storybook.js.org/docs/get-started/frameworks/angular?renderer=angular

**Contents**:
- Storybook for Angular
- Requirements
- Getting started
  - In a project without Storybook
  - In a project with Storybook
    - Automatic migration
    - Manual migration
- Run Storybook

Storybook for Angular is a framework that makes it easy to develop and test UI components in isolation for Angular applications. It includes:

Follow the prompts after running this command in your Angular project's root directory:

More on getting started with Storybook.

This framework is designed to work with Storybook 7+. If you’re not already using v7, upgrade with this command:

When running the upgrade command above, you should get a prompt asking you to migrate to @storybook/angular, which should handle everything for you. In case that auto-migration does not work for your project, refer to the manual migration below.

First, install the framework:

Then, update your .storybook/main.js|ts to change the framework property:

Finally, update your angular.json to include the Storybook builder:

To run Storybook for a particular project, please run the following:

To build Storybook, run:

You will find the output in the configured outputDir (default is dist/storybook/<your-project>).

You can include JSDoc comments above components, directives, and other parts of your Angular code to include documentation for those elements. Compodoc uses these comments to generate documentation for your application. In Storybook, it is useful to add explanatory comments above @Inputs and @Outputs, since these are the main elements that Storybook displays in its user interface. The @Inputs and @Outputs are elements you can interact with in Storybook, such as controls.

When installing Storybook via npx storybook@latest init, you can set up Compodoc automatically.

If you have already installed Storybook, you can set up Compodoc manually.

Install the following dependencies:

Add the following option to your Storybook Builder:

Go to your .storybook/preview.ts and add the following:

If your component relies on application-wide providers, like the ones defined by BrowserAnimationsModule or any other modules that use the forRoot pattern to provide a ModuleWithProviders, you can app

*[Content truncated - see full docs]*

**Examples**:

```text
npm create storybook@latest
```

```text
npx storybook@latest upgrade
```

```text
npm install --save-dev @storybook/angular
```

---

## Storybook for Next.js

**URL**: https://storybook.js.org/docs/get-started/frameworks/nextjs?renderer=react

**Contents**:
- Storybook for Next.js
- Requirements
- Getting started
  - In a project without Storybook
  - In a project with Storybook
    - Automatic migration
    - Manual migration
    - With Vite

Storybook for Next.js is a framework that makes it easy to develop and test UI components in isolation for Next.js applications. It includes:

Follow the prompts after running this command in your Next.js project's root directory:

More on getting started with Storybook.

This framework is designed to work with Storybook 7+. If you’re not already using v7, upgrade with this command:

When running the upgrade command above, you should get a prompt asking you to migrate to @storybook/nextjs, which should handle everything for you. In case that auto-migration does not work for your project, refer to the manual migration below.

First, install the framework:

Then, update your .storybook/main.js|ts to change the framework property:

Finally, if you were using Storybook plugins to integrate with Next.js, those are no longer necessary when using this framework and can be removed:

Storybook recommends using the @storybook/nextjs-vite framework, which is based on Vite and removes the need for Webpack and Babel. It supports all of the features documented here.

Then, update your .storybook/main.js|ts to change the framework property:

If your Storybook configuration contains custom Webpack operations in webpackFinal, you will likely need to create equivalents in viteFinal.

For more information, see the Vite builder documentation.

Finally, if you were using Storybook plugins to integrate with Next.js, those are no longer necessary when using this framework and can be removed:

If all goes well, you should see a setup wizard that will help you get started with Storybook introducing you to the main concepts and features, including how the UI is organized, how to write your first story, and how to test your components' response to various inputs utilizing controls.

If you skipped the wizard, you can always run it again by adding the ?path=/onboarding query parameter to the URL of your Storybook instance, provided that the example stories are still available.

This framework 

*[Content truncated - see full docs]*

**Examples**:

```text
npm create storybook@latest
```

```text
npx storybook@latest upgrade
```

```text
npm install --save-dev @storybook/nextjs
```

---

## Storybook for Preact & Vite

**URL**: https://storybook.js.org/docs/get-started/frameworks/preact-vite?renderer=preact

**Contents**:
- Storybook for Preact & Vite
- Requirements
- Getting started
  - In a project without Storybook
  - In a project with Storybook
    - Automatic migration
    - Manual migration
- API

Storybook for Preact & Vite is a framework that makes it easy to develop and test UI components in isolation for Preact applications built with Vite. It includes:

Follow the prompts after running this command in your Preact project's root directory:

More on getting started with Storybook.

This framework is designed to work with Storybook 7+. If you’re not already using v7, upgrade with this command:

When running the upgrade command above, you should get a prompt asking you to migrate to @storybook/preact-vite, which should handle everything for you. In case that auto-migration does not work for your project, refer to the manual migration below.

First, install the framework:

Then, update your .storybook/main.js|ts to change the framework property:

You can pass an options object for additional configuration if needed:

Type: Record<string, any>

Configure options for the framework's builder. For this framework, available options can be found in the Vite builder docs.

**Examples**:

```text
npm create storybook@latest
```

```text
npx storybook@latest upgrade
```

```text
npm install --save-dev @storybook/preact-vite
```

---

## Storybook for React Native Web

**URL**: https://storybook.js.org/docs/get-started/frameworks/react-native-web-vite?renderer=react-native-web

**Contents**:
- Storybook for React Native Web
- Requirements
- Getting started
  - In a project without Storybook
  - In a project with Storybook addon-react-native-web
  - In a project with Storybook react-native
- Run the Setup Wizard
- React Native vs React Native Web

Storybook for React Native Web is a framework that makes it easy to develop and test UI components in isolation for React Native applications. It uses Vite to build your components for web browsers. The framework includes:

In addition to React Native Web, Storybook supports on-device React Native development. If you're unsure what's right for you, read our comparison.

Follow the prompts after running this command in your React Native project's root directory:

More on getting started with Storybook.

The React Native Web addon was a Webpack-based precursor to the React Native Web Vite framework (i.e., @storybook/react-native-web-vite). If you're using the addon, you should migrate to the framework, which is faster, more stable, maintained, and better documented. To do so, follow the steps below.

Run the following command to upgrade Storybook to the latest version:

This framework is designed to work with Storybook 8.5 and above for the best experience. We won't be able to provide support if you're using an older Storybook version.

Install the framework and its peer dependencies:

Update your .storybook/main.js|ts to change the framework property and remove the @storybook/addon-react-native-web addon:

Finally, remove the addon and similar packages (i.e., @storybook/react-webpack5 and @storybook/addon-react-native-web) from your project.

Storybook for React Native is a framework that runs in a simulator or on your mobile device. It's possible to run React Native Web alongside React Native, but we are still working on a seamless integration. In the meantime, we recommend running one or the other. If you need help figuring out what's right for you, read our comparison.

If all goes well, you should see a setup wizard that will help you get started with Storybook. The wizard will introduce you to the main concepts and features, including how the UI is organized, how to write your first story, and how to test your components' response to various inputs utilizing con

*[Content truncated - see full docs]*

**Examples**:

```text
npm create storybook@latest
```

```text
npx storybook@latest upgrade
```

```text
npm install --save-dev @storybook/react-native-web-vite vite
```

---

## Storybook for React & Vite

**URL**: https://storybook.js.org/docs/get-started/frameworks/react-vite?renderer=react

**Contents**:
- Storybook for React & Vite
- Requirements
- Getting started
  - In a project without Storybook
  - In a project with Storybook
    - Automatic migration
    - Manual migration
- Run the Setup Wizard

Storybook for React & Vite is a framework that makes it easy to develop and test UI components in isolation for React applications built with Vite. It includes:

Follow the prompts after running this command in your React project's root directory:

More on getting started with Storybook.

This framework is designed to work with Storybook 7+. If you’re not already using v7, upgrade with this command:

When running the upgrade command above, you should get a prompt asking you to migrate to @storybook/react-vite, which should handle everything for you. In case that auto-migration does not work for your project, refer to the manual migration below.

First, install the framework:

Then, update your .storybook/main.js|ts to change the framework property:

If all goes well, you should see a setup wizard that will help you get started with Storybook introducing you to the main concepts and features, including how the UI is organized, how to write your first story, and how to test your components' response to various inputs utilizing controls.

If you skipped the wizard, you can always run it again by adding the ?path=/onboarding query parameter to the URL of your Storybook instance, provided that the example stories are still available.

You can pass an options object for additional configuration if needed:

Type: Record<string, any>

Configure options for the framework's builder. For this framework, available options can be found in the Vite builder docs.

**Examples**:

```text
npm create storybook@latest
```

```text
npx storybook@latest upgrade
```

```text
npm install --save-dev @storybook/react-vite
```

---

## Storybook for React & Webpack

**URL**: https://storybook.js.org/docs/get-started/frameworks/react-webpack5?renderer=react

**Contents**:
- Storybook for React & Webpack
- Requirements
- Getting started
  - In a project without Storybook
  - In a project with Storybook
    - Automatic migration
    - Manual migration
- Run the Setup Wizard

Storybook for React & Webpack is a framework that makes it easy to develop and test UI components in isolation for React applications built with Webpack.

Follow the prompts after running this command in your React project's root directory:

More on getting started with Storybook.

This framework is designed to work with Storybook 7+. If you’re not already using v7, upgrade with this command:

When running the upgrade command above, you should get a prompt asking you to migrate to @storybook/react-webpack5, which should handle everything for you. In case that auto-migration does not work for your project, refer to the manual migration below.

First, install the framework:

Next, install and register your appropriate compiler addon, depending on whether you're using SWC (recommended) or Babel:

If your project is using Create React App, you can skip this step.

More details can be found in the Webpack builder docs.

Finally, update your .storybook/main.js|ts to change the framework property:

If all goes well, you should see a setup wizard that will help you get started with Storybook introducing you to the main concepts and features, including how the UI is organized, how to write your first story, and how to test your components' response to various inputs utilizing controls.

If you skipped the wizard, you can always run it again by adding the ?path=/onboarding query parameter to the URL of your Storybook instance, provided that the example stories are still available.

Support for Create React App is handled by @storybook/preset-create-react-app.

This preset enables support for all CRA features, including Sass/SCSS and TypeScript.

If you're working on an app that was initialized manually (i.e., without the use of CRA), ensure that your app has react-dom included as a dependency. Failing to do so can lead to unforeseen issues with Storybook and your project.

You can pass an options object for additional configuration if needed:

Type: Record<string, any>

Confi

*[Content truncated - see full docs]*

**Examples**:

```text
npm create storybook@latest
```

```text
npx storybook@latest upgrade
```

```text
npm install --save-dev @storybook/react-webpack5
```

---

## Storybook for SvelteKit

**URL**: https://storybook.js.org/docs/get-started/frameworks/sveltekit?renderer=svelte

**Contents**:
- Storybook for SvelteKit
- Requirements
- Getting started
  - In a project without Storybook
  - In a project with Storybook
    - Automatic migration
    - Manual migration
- Supported features

Storybook for SvelteKit is a framework that makes it easy to develop and test UI components in isolation for SvelteKit applications. It includes:

Follow the prompts after running this command in your Sveltekit project's root directory:

More on getting started with Storybook.

This framework is designed to work with Storybook 7+. If you’re not already using v7, upgrade with this command:

When running the upgrade command above, you should get a prompt asking you to migrate to @storybook/sveltekit, which should handle everything for you. In case that auto-migration does not work for your project, refer to the manual migration below.

First, install the framework:

Then, update your .storybook/main.js|ts to change the framework property:

Finally, these packages are now either obsolete or part of @storybook/sveltekit, so you no longer need to depend on them directly. You can remove them (npm uninstall, yarn remove, pnpm remove) from your project:

All Svelte language features are supported out of the box, as the Storybook framework uses the Svelte compiler directly. However, SvelteKit has some Kit-specific modules that aren't supported. Here's a breakdown of what will and will not work within Storybook:

To mock a SvelteKit import you can define it within parameters.sveltekit_experimental:

The available parameters are documented in the API section, below.

The default link-handling behavior (e.g., when clicking an <a href="..." /> element) is to log an action to the Actions panel.

You can override this by assigning an object to parameters.sveltekit_experimental.hrefs, where the keys are strings representing an href, and the values define your mock. For example:

See the API reference for more information.

Storybook provides a Svelte addon maintained by the community, enabling you to write stories for your Svelte components using the template syntax.

The community actively maintains the Svelte CSF addon but still lacks some features currently available in the offi

*[Content truncated - see full docs]*

**Examples**:

```text
npm create storybook@latest
```

```text
npx storybook@latest upgrade
```

```text
npm install --save-dev @storybook/sveltekit
```

---

## Storybook for Svelte & Vite

**URL**: https://storybook.js.org/docs/get-started/frameworks/svelte-vite?renderer=svelte

**Contents**:
- Storybook for Svelte & Vite
- Requirements
- Getting started
  - In a project without Storybook
  - In a project with Storybook
    - Automatic migration
    - Manual migration
- Writing native Svelte stories

Storybook for Svelte & Vite is a framework that makes it easy to develop and test UI components in isolation for applications using Svelte built with Vite.

Follow the prompts after running this command in your Svelte project's root directory:

More on getting started with Storybook.

This framework is designed to work with Storybook 7+. If you’re not already using v7, upgrade with this command:

When running the upgrade command above, you should get a prompt asking you to migrate to @storybook/svelte-vite, which should handle everything for you. In case that auto-migration does not work for your project, refer to the manual migration below.

First, install the framework:

Then, update your .storybook/main.js|ts to change the framework property:

Storybook provides a Svelte addon maintained by the community, enabling you to write stories for your Svelte components using the template syntax.

The community actively maintains the Svelte CSF addon but still lacks some features currently available in the official Storybook Svelte framework support. For more information, see the addon's documentation.

If you initialized your project with the Svelte framework, the addon has already been installed and configured for you. However, if you're migrating from a previous version, you'll need to take additional steps to enable this feature.

Run the following command to install the addon.

The CLI's add command automates the addon's installation and setup. To install it manually, see our documentation on how to install addons.

Update your Storybook configuration file (i.e., .storybook/main.js|ts) to enable support for this format.

By default, the Svelte addon offers zero-config support for Storybook's Svelte framework. However, you can extend your Storybook configuration file (i.e., .storybook/main.js|ts) and provide additional addon options. Listed below are the available options and examples of how to use them.

Enabling the legacyTemplate option can introduce a performance 

*[Content truncated - see full docs]*

**Examples**:

```text
npm create storybook@latest
```

```text
npx storybook@latest upgrade
```

```text
npm install --save-dev @storybook/svelte-vite
```

---

## Storybook for Vue & Vite

**URL**: https://storybook.js.org/docs/get-started/frameworks/vue3-vite?renderer=vue

**Contents**:
- Storybook for Vue & Vite
- Requirements
- Getting started
  - In a project without Storybook
  - In a project with Storybook
    - Automatic migration
    - Manual migration
- Extending the Vue application

Storybook for Vue & Vite is a framework that makes it easy to develop and test UI components in isolation for Vue applications built with Vite. It includes:

Follow the prompts after running this command in your Vue project's root directory:

More on getting started with Storybook.

This framework is designed to work with Storybook 7+. If you’re not already using v7, upgrade with this command:

When running the upgrade command above, you should get a prompt asking you to migrate to @storybook/vue3-vite, which should handle everything for you. In case that auto-migration does not work for your project, refer to the manual migration below.

First, install the framework:

Then, update your .storybook/main.js|ts to change the framework property:

Storybook creates a Vue 3 application for your component preview. When using global custom components (app.component), directives (app.directive), extensions (app.use), or other application methods, you will need to configure those in the ./storybook/preview.js|ts file.

Therefore, Storybook provides you with a setup function exported from this package. This function receives your Storybook instance as a callback, which you can interact with and add your custom configuration.

vue-component-meta is only available in Storybook ≥ 8. It is currently an opt-in, but it will become the default in a future version of Storybook.

vue-component-meta is a tool maintained by the Vue team that extracts metadata from Vue components. Storybook can use it to generate the controls for your stories and documentation. It's a more full-featured alternative to vue-docgen-api and is recommended for most projects.

If you want to use vue-component-meta, you can configure it in your .storybook/main.js|ts file:

vue-component-meta comes with many benefits and enables more documentation features, such as:

vue-component-meta supports all types of Vue components (including SFC, functional, composition/options API components) from .vue, .ts, .tsx, .js, a

*[Content truncated - see full docs]*

**Examples**:

```text
npm create storybook@latest
```

```text
npx storybook@latest upgrade
```

```text
npm install --save-dev @storybook/vue3-vite
```

---

## Storybook for Web components & Vite

**URL**: https://storybook.js.org/docs/get-started/frameworks/web-components-vite?renderer=web-components

**Contents**:
- Storybook for Web components & Vite
- Requirements
- Getting started
  - In a project without Storybook
  - In a project with Storybook
    - Automatic migration
    - Manual migration
- API

Storybook for Web components & Vite is a framework that makes it easy to develop and test UI components in isolation for applications using Web components built with Vite.

Follow the prompts after running this command in your Web components project's root directory:

More on getting started with Storybook.

This framework is designed to work with Storybook 7+. If you’re not already using v7, upgrade with this command:

When running the upgrade command above, you should get a prompt asking you to migrate to @storybook/web-components-vite, which should handle everything for you. In case that auto-migration does not work for your project, refer to the manual migration below.

First, install the framework:

Then, update your .storybook/main.js|ts to change the framework property:

You can pass an options object for additional configuration if needed:

The available options are:

Type: Record<string, any>

Configure options for the framework's builder. For this framework, available options can be found in the Vite builder docs.

**Examples**:

```text
npm create storybook@latest
```

```text
npx storybook@latest upgrade
```

```text
npm install --save-dev @storybook/web-components-vite
```

---

## Styling and CSS

**URL**: https://storybook.js.org/docs/configure/styling-and-css

**Contents**:
- Styling and CSS
- CSS
  - Import bundled CSS (Recommended)
  - Include static CSS
- CSS modules
  - Vite
  - Webpack
- PostCSS

There are many ways to include CSS in a web application, and correspondingly there are many ways to include CSS in Storybook. Usually, it is best to try and replicate what your application does with styling in Storybook’s configuration.

Storybook supports importing CSS files in a few different ways. Storybook will inject these tags into the preview iframe where your components render, not the Storybook Manager UI. The best way to import CSS depends on your project's configuration and your preferences.

All Storybooks are pre-configured to recognize imports for CSS files. To add global CSS for all your stories, import it in .storybook/preview.ts. These files will be subject to HMR, so you can see your changes without restarting your Storybook server.

If your component files import their CSS files, this will work too. However, if you're using CSS processor tools like Sass or Postcss, you may need some more configuration.

If you have a global CSS file that you want to include in all your stories, you can import it in .storybook/preview-head.html. However, these files will not be subject to HMR, so you'll need to restart your Storybook server to see your changes.

Vite comes with CSS modules support out-of-the-box. If you have customized the CSS modules configuration in your vite.config.js this will automatically be applied to your Storybook as well. Read more about Vite's CSS modules support.

Storybook recreates your Next.js configuration, so you can use CSS modules in your stories without any extra configuration.

If you're using Webpack and want to use CSS modules, you'll need some extra configuration. We recommend installing @storybook/addon-styling-webpack to help you configure these tools.

Vite comes with PostCSS support out-of-the-box. If you have customized the PostCSS configuration in your vite.config.js this will automatically be applied to your Storybook as well. Read more about Vite's PostCSS support.

Storybook recreates your Next.js configuration, so 

*[Content truncated - see full docs]*

**Examples**:

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Preview } from '@storybook/your-framework';
 
import '../src/styles/global.css';
 
const preview: Preview = {
  parameters: {},
};
 
export default preview;
```

```text
<!-- Loads a font from a CDN -->
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link
  href="https://fonts.googleapis.com/css2?family=Inter:wght@100..900&display=swap"
  rel="stylesheet"
/>
<!-- Load your CSS file -->
<link rel="stylesheet" href="path/to/your/styles.css" />
```

---

## Test coverage

**URL**: https://storybook.js.org/docs/writing-tests/test-coverage

**Contents**:
- Test coverage
- Set up
- Usage
  - Storybook UI
  - CLI
  - Editor extension
  - CI
- Configuration

Test coverage is the practice of measuring whether existing tests fully cover your code. It marks which conditions, logic branches, functions and variables in your code are and are not being tested.

Coverage tests examine the instrumented code against a set of industry-accepted best practices. They act as the last line of QA to improve the quality of your test suite.

Each project’s coverage report will look different, but the important things to note are:

When you run component tests with the Vitest addon, it can generate a coverage report. The result is summarized in the testing widget, showing the percentage of statements covered by your tested stories.

If you cannot use the Vitest addon in your project, you can still generate code coverage using the test-runner. Follow the instructions in the test-runner documentation to set up the test-runner with code coverage in your project.

Coverage is included in the Vitest addon and, when enabled, will be calculated when running component tests for your project. To enable coverage, check the coverage checkbox in the testing widget.

Before coverage can be calculated, you may need to install a support package corresponding to your coverage provider:

Because coverage is built into the Vitest addon, you can use it everywhere you run your tests.

When you enable coverage in the Storybook UI, the coverage report will be generated and summarized in the testing widget after you run your tests. You can see the percentage of statements covered by your tested stories, as well as whether the coverage meets the watermarks.

Additionally, the full coverage report will be served at the /coverage/index.html route of your running Storybook.

The report is interactive. You can click through to a component to view its source and see which parts of your code are covered by tests or not:

It's important to understand that the coverage reported in the Storybook UI has three important limitations:

Like the rest of Storybook Test, coverag

*[Content truncated - see full docs]*

**Examples**:

```text
# For v8
npm install --save-dev @vitest/coverage-v8
 
# For istanbul
npm install --save-dev @vitest/coverage-istanbul
```

```text
{
  "scripts": {
    "test-storybook": "vitest --project=storybook"
  }
}
```

```text
npm run test-storybook -- --coverage
```

---

## Test runner

**URL**: https://storybook.js.org/docs/writing-tests/integrations/test-runner

**Contents**:
- Test runner
- Setup
- Configure
  - CLI Options
  - Run tests against a deployed Storybook
- Run accessibility tests
- Run snapshot tests
  - Set up

The test runner has been superseded by the Vitest addon, which offers the same functionality, powered by the faster and more modern Vitest browser mode. It also enables the full Storybook Test experience, allowing you to run interaction, accessibility, and visual tests from your Storybook app.

If you are using a Vite-powered Storybook framework, we recommend using the Vitest addon instead of the test runner.

Storybook test runner turns all of your stories into executable tests. It is powered by Jest and Playwright.

These tests run in a live browser and can be executed via the command line or your CI server.

The test-runner is a standalone, framework-agnostic utility that runs parallel to your Storybook. You will need to take some additional steps to set it up properly. Detailed below is our recommendation to configure and execute it.

Run the following command to install it.

Update your package.json scripts and enable the test runner.

Start your Storybook with:

Storybook's test runner requires either a locally running Storybook instance or a published Storybook to run all the existing tests.

Finally, open a new terminal window and run the test-runner with:

Test runner offers zero-config support for Storybook. However, you can run test-storybook --eject for more fine-grained control. It generates a test-runner-jest.config.js file at the root of your project, which you can modify. Additionally, you can extend the generated configuration file and provide testEnvironmentOptions as the test runner also uses jest-playwright under the hood.

The test-runner is powered by Jest and accepts a subset of its CLI options (for example, --watch, --maxWorkers). If you're already using any of those flags in your project, you should be able to migrate them into Storybook's test-runner without any issues. Listed below are all the available flags and examples of using them.

By default, the test-runner assumes that you're running it against a locally served Storybook on port 6

*[Content truncated - see full docs]*

**Examples**:

```text
npm install @storybook/test-runner --save-dev
```

```text
{
  "scripts": {
    "test-storybook": "test-storybook"
  }
}
```

```text
npm run storybook
```

---

## Theming

**URL**: https://storybook.js.org/docs/configure/user-interface/theming

**Contents**:
- Theming
- Global theming
- Theming docs
- Create a theme quickstart
- CSS escape hatches
- MDX component overrides
- Addons and theme creation
- Using the theme for addon authors

Storybook is theme-able using a lightweight theming API.

It's possible to theme Storybook globally.

Storybook includes two themes that look good out of the box: "light" and "dark". Unless you've set your preferred color scheme as dark, Storybook will use the light theme as default.

As an example, you can tell Storybook to use the "dark" theme by modifying .storybook/manager.js:

When setting a theme, set a complete theme object. The theme is replaced, not combined.

Storybook Docs uses the same theme system as Storybook’s UI but is themed independently from the main UI.

Supposing you have a Storybook theme defined for the main UI in .storybook/manager.js:

Here's how you'd specify the same theme for docs in .storybook/preview.js:

Continue to read if you want to learn how to create your theme.

The easiest way to customize Storybook is to generate a new theme using the create() function from storybook/theming. This function includes shorthands for the most common theme variables. Here's how to use it:

Inside your .storybook directory, create a new file called YourTheme.js and add the following:

If you're using brandImage to add your custom logo, you can use any of the most common image formats.

Above, we're creating a new theme that will:

Finally, we'll need to import the theme into Storybook. Create a new file called manager.js in your .storybook directory and add the following:

Now your custom theme will replace Storybook's default theme, and you'll see a similar set of changes in the UI.

Let's take a look at a more complex example. Copy the code below and paste it in .storybook/YourTheme.js.

Above, we're updating the theme with the following changes:

With the new changes introduced, the custom theme should yield a similar result.

Many theme variables are optional, the base property is NOT.

The storybook/theming module is built using TypeScript, which should help create a valid theme for TypeScript users. The types are part of the package itself.

Th

*[Content truncated - see full docs]*

**Examples**:

```python
import { addons } from 'storybook/manager-api';
import { themes } from 'storybook/theming';
 
addons.setConfig({
  theme: themes.dark,
});
```

```python
import { addons } from 'storybook/manager-api';
import { themes } from 'storybook/theming';
 
addons.setConfig({
  theme: themes.dark,
});
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Preview } from '@storybook/your-framework';
 
import { themes } from 'storybook/theming';
 
const preview: Preview = {
  parameters: {
    docs: {
      theme: themes.dark,
    },
  },
};
 
export default preview;
```

---

## Toolbars & globals

**URL**: https://storybook.js.org/docs/essentials/toolbars-and-globals

**Contents**:
- Toolbars & globals
- Globals
- Global types and the toolbar annotation
- Create a decorator
- Setting globals on a story
- Advanced usage
- Consuming globals from within a story
- Consuming globals from within an addon

Storybook ships with features to control the viewport and background the story renders in. Similarly, you can use built-in features to create toolbar items which control special “globals”. You can then read the global values to create decorators to control story rendering.

Globals in Storybook represent “global” (as in not story-specific) inputs to the rendering of the story. As they aren’t specific to the story, they aren’t passed in the args argument to the story function (although they are accessible as context.globals). Instead, they are typically used in decorators, which apply to all stories.

When the globals change, the story re-renders and the decorators rerun with the new values. The easiest way to change globals is to create a toolbar item for them.

Storybook has a simple, declarative syntax for configuring toolbar menus. In your .storybook/preview.js|ts, you can add your own toolbars by creating globalTypes with a toolbar annotation:

As globals are global you can only set globalTypes and initialGlobals in .storybook/preview.js|ts.

When you start your Storybook, your toolbar should have a new dropdown menu with the light and dark options.

We have a global implemented. Let's wire it up! We can consume our new theme global in a decorator using the context.globals.theme value.

For example, suppose you are using styled-components. You can add a theme provider decorator to your .storybook/preview.js|ts config:

When a global value is changed with a toolbar menu in Storybook, that value continues to be used as you navigate between stories. But sometimes a story requires a specific value to render correctly, e.g., when testing against a particular environment.

To ensure that a story always uses a specific global value, regardless of what has been chosen in the toolbar, you can set the globals annotation on a story or component. This overrides the global value for those stories and disables the toolbar menu for that global when viewing the stories.

In the

*[Content truncated - see full docs]*

**Examples**:

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Preview } from '@storybook/your-framework';
 
const preview: Preview = {
  globalTypes: {
    theme: {
      description: 'Global theme for components',
      toolbar: {
        // The label to show for this toolbar item
        title: 'Theme',
        icon: 'circlehollow',
        // Array of plain string values or MenuItem shape (see below)
        items: ['light', 'dark'],
      
...
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Preview } from '@storybook/your-framework';
 
import { MyThemes } from '../my-theme-folder/my-theme-file';
 
const preview: Preview = {
  decorators: [
    (story, context) => {
      const selectedTheme = context.globals.theme || 'light';
      const theme = MyThemes[selectedTheme];
      // Your theme provider and other context providers goes in the return statement
      return;

...
```

```python
// Replace your-framework with the name of your framework (e.g., react-vite, vue3-vite, etc.)
import type { Meta, StoryObj } from '@storybook/your-framework';
 
import { Button } from './Button';
 
const meta = {
  component: Button,
  globals: {
    // 👇 Set background value for all component stories
    backgrounds: { value: 'gray', grid: false },
  },
} satisfies Meta<typeof Button>;
 
export default meta;
type Story = StoryObj<typeof meta>;
 
export const OnDark: Story = {
  globals: {
    /
...
```

---

## Types of addons

**URL**: https://storybook.js.org/docs/addons/addon-types

**Contents**:
- Types of addons
- UI-based addons
  - Panels
  - Toolbars
  - Tabs
- Preset addons

Each Storybook addon is classified into two general categories, UI-based or Presets. Each type of addons feature is documented here. Use this as a reference when creating your addon.

UI-based addons allow you to customize Storybook's UI with the following elements.

Panel addons allow you to add your own UI in Storybook's addon panel. This is the most common type of addon in the ecosystem. For example, the official @storybook/addon-a11y uses this pattern.

Use this boilerplate code to add a new Panel to Storybook's UI:

Toolbar addons allow you to add your own custom tools in Storybook's Toolbar. For example, the official @storybook/addon-themes uses this pattern.

Use this boilerplate code to add a new button to Storybook's Toolbar:

The match property allows you to conditionally render your toolbar addon, based on the current view. The icon element used in the example loads the icons from the storybook/internal/components module. See here for the list of available icons that you can use.

Tab addons allow you to create your own custom tabs in Storybook.

Use this boilerplate code to add a new Tab to Storybook's UI:

Learn how to write your own addon that includes these UI elements here.

Storybook preset addons are grouped collections of babel, webpack, and addons configurations to integrate Storybook and other technologies. For example the official preset-create-react-app.

Use this boilerplate code while writing your own preset addon.

Learn more about the Storybook addon ecosystem

**Examples**:

```python
import React from 'react';
 
import { AddonPanel } from 'storybook/internal/components';
 
import { useGlobals, addons, types } from 'storybook/manager-api';
 
addons.register('my/panel', () => {
  addons.add('my-panel-addon/panel', {
    title: 'Example Storybook panel',
    //👇 Sets the type of UI element in Storybook
    type: types.PANEL,
    render: ({ active }) => (
      <AddonPanel active={active}>
        <h2>I'm a panel addon in Storybook</h2>
      </AddonPanel>
    ),
  });
});
```

```python
import React from 'react';
 
import { addons, types } from 'storybook/manager-api';
import { IconButton } from 'storybook/internal/components';
import { OutlineIcon } from '@storybook/icons';
 
addons.register('my-addon', () => {
  addons.add('my-addon/toolbar', {
    title: 'Example Storybook toolbar',
    //👇 Sets the type of UI element in Storybook
    type: types.TOOL,
    //👇 Shows the Toolbar UI element if the story canvas is being viewed
    match: ({ tabId, viewMode }) => !tabId && viewM
...
```

```python
import React from 'react';
 
import { addons, types } from 'storybook/manager-api';
 
addons.register('my-addon', () => {
  addons.add('my-addon/tab', {
    type: types.TAB,
    title: 'Example Storybook tab',
    render: () => (
      <div>
        <h2>I'm a tabbed addon in Storybook</h2>
      </div>
    ),
  });
});
```

---

## Upgrading Storybook

**URL**: https://storybook.js.org/docs/releases/upgrading

**Contents**:
- Upgrading Storybook
- Upgrade script
  - Mono-repository support
    - Limiting scope in large mono-repositories
- Upgrade process
  - Automatic health check
  - Error handling and debugging
- Command-line options

The frontend ecosystem is a fast-moving place. Regular dependency upgrades are a way of life, whether upgrading a framework, library, tooling, or all of the above! Storybook provides a few resources to help ease the pain of upgrading.

The most common upgrade is Storybook itself. Storybook releases follow Semantic Versioning. We publish patch releases with bug fixes continuously, minor versions of Storybook with new features every few months, and major versions of Storybook with breaking changes roughly once per year.

To help ease the pain of keeping Storybook up-to-date, we provide a command-line script that automatically detects all Storybook projects in your repository:

Important: Always run the upgrade command from your repository root. The script will automatically detect all Storybook projects in your repository, including in mono-repository setups.

The upgrade command will use whichever version you specify. For example:

The upgrade command is designed to upgrade from one major version to the next.

If you want to upgrade across more than major version, run the command multiple times. For example, to upgrade from Storybook 7 to Storybook 9, you first need to upgrade to the latest version of Storybook 8 with storybook@8 upgrade, and then run storybook@9 upgrade to upgrade to the latest version of Storybook 9.

The only exception to this is when upgrading from 6 to 8, where you can run storybook@8 upgrade directly to upgrade from 6.x.x to 8.x.x.

The upgrade script provides enhanced support for mono-repositories:

For large mono-repositories where you want to limit the upgrade to a specific directory, use the STORYBOOK_PROJECT_ROOT environment variable:

This is especially helpful in huge mono-repositories with semi-encapsulated Storybooks.

After running the command, the script will:

In addition to running the command, we also recommend checking the MIGRATION.md file, for the detailed log of relevant changes and deprecations that might affect your upgrade.

*[Content truncated - see full docs]*

**Examples**:

```text
npx storybook@latest upgrade
```

```text
STORYBOOK_PROJECT_ROOT=./packages/frontend storybook@latest upgrade
```

```text
npx storybook@latest doctor
```

---

## Viewport

**URL**: https://storybook.js.org/docs/essentials/viewport

**Contents**:
- Viewport
- Configuration
  - Use a detailed set of devices
  - Add new devices
  - Configuring per component or story
- Defining the viewport for a story
- API
  - Keyboard shortcuts

The viewport feature allows you to adjust the dimensions of the iframe your story is rendered in. It makes it easy to develop responsive UIs.

Out of the box, the viewport feature offers you a standard set of viewports that you can use. If you want to change the default set of viewports, you can configure your own viewports with the viewport parameter in your .storybook/preview.js|ts.

You can define the available viewports using the options property and set the initial viewport using the initialGlobals property:

By default, the viewport feature will use a minimal set of viewports, which enables you to test your UI in common responsive scenarios. These are also available in the MINIMAL_VIEWPORTS export and include the following devices:

If you need a more detailed set of devices, you can use the INITIAL_VIEWPORTS export, which includes the following devices:

To use the detailed set of devices, you can adjust the options property in your configuration to include the INITIAL_VIEWPORTS export:

If the predefined viewports don't meet your needs, you can add new devices to the list of viewports. For example, let's add two Kindle devices to the default set of minimal viewports:

In some cases, it's not practical for you to use a specific visual viewport on a global scale, and you need to adjust it to an individual story or set of stories for a component.

Parameters can be applied at the project, component, and story levels, which allows you to specify the configuration where needed. For example, you can set the available viewports for all of the stories for a component like so:

The Viewport module enables you to change the viewport applied to a story by selecting from the list of predefined viewports in the toolbar. If needed, you can set a story to default to a specific viewport by using the globals option:

When you specify a viewport for a story (or a component's stories) using globals, the viewport is applied and cannot be changed using the toolbar. This is usefu

*[Content truncated - see full docs]*

**Examples**:

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Preview } from '@storybook/your-framework';
 
import { INITIAL_VIEWPORTS } from 'storybook/viewport';
 
const preview: Preview = {
  parameters: {
    viewport: {
      options: INITIAL_VIEWPORTS,
    },
  },
  initialGlobals: {
    viewport: { value: 'ipad', isRotated: false },
  },
};
 
export default preview;
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Preview } from '@storybook/your-framework';
 
import { INITIAL_VIEWPORTS } from 'storybook/viewport';
 
const preview: Preview = {
  parameters: {
    viewport: {
      options: INITIAL_VIEWPORTS,
    },
  },
  initialGlobals: {
    viewport: { value: 'ipad', isRotated: false },
  },
};
 
export default preview;
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Preview } from '@storybook/your-framework';
 
import { MINIMAL_VIEWPORTS } from 'storybook/viewport';
 
const kindleViewports = {
  kindleFire2: {
    name: 'Kindle Fire 2',
    styles: {
      width: '600px',
      height: '963px',
    },
  },
  kindleFireHD: {
    name: 'Kindle Fire HD',
    styles: {
      width: '533px',
      height: '801px',
    },
  },
};
 
const preview: Pre
...
```

---

## Vite

**URL**: https://storybook.js.org/docs/builders/vite

**Contents**:
- Vite
- Setup
- Configuration
  - Environment-based configuration
  - Override the default configuration
  - TypeScript
- Troubleshooting
  - Migrating from Webpack

Storybook Vite builder bundles your components and stories with Vite, a fast ESM bundler.

If you ran npx storybook@latest init to include Storybook in your Vite application, the builder is already installed and configured for you. If you want, you can also opt into it manually.

Run the following command to install the builder.

Update your Storybook configuration (in .storybook/main.js|ts) to include the builder.

Out of the box, Storybook's Vite builder includes a set of configuration defaults for the supported frameworks, which are merged alongside your existing configuration file. For an optimal experience when using the Vite builder, we recommend applying any configuration directly inside Vite's configuration file (i.e., vite.config.js|ts).

When Storybook loads, it automatically merges the configuration into its own. However, since different projects may have specific requirements, you may need to provide a custom configuration for Storybook. In such cases, you can modify your configuration file (.storybook/main.js|ts) and add the viteFinal configuration function as follows:

The asynchronous function viteFinal receives a config object with the default builder configuration and returns the updated configuration.

If you need to customize the builder's configuration and apply specific options based on your environment, extend the viteFinal function as follows:

By default, the Vite builder in Storybook searches for the Vite configuration file in the root directory of your Storybook project. However, you can customize it to look for the configuration file in a different location. For example:

If you do not want Storybook to load the Vite configuration file automatically, you can use the viteConfigPath option to point to a non-existent file.

If you need, you can also configure Storybook's Vite builder using TypeScript. Rename your .storybook/main.js to .storybook/main.ts and adjust it as follows:

Vite generally handles more use cases out of the box than Webpa

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
export default {
  // Replace your-framework with the framework you are using, e.g. react-vite, nextjs-vite, vue3-vite, etc.
  framework: '@storybook/your-framework',
  stories: ['../src/**/*.mdx', '../stories/**/*.stories.@(js|jsx|mjs|ts|tsx)'],
  addons: ['@storybook/addon-docs'],
  core: {
    builder: '@storybook/builder-vite',
  },
  async viteFinal(config) {
    // Merge custom configuration into the default config
    const { mergeConfig } = await import('vite');
 
    return mergeConfig(
...
```

---

## Vitest addon

**URL**: https://storybook.js.org/docs/writing-tests/integrations/vitest-addon

**Contents**:
- Vitest addon
- Install and set up
  - Automatic setup
  - Manual setup
  - Example configuration files
- Usage
  - Storybook UI
  - CLI

Storybook's Vitest addon allows you to test your components directly inside Storybook. On its own, it transforms your stories into component tests, which test the rendering and behavior of your components in a real browser environment. It can also calculate project coverage provided by your stories.

If your project is using other testing addons, such as the Visual tests addon or the Accessibility addon, you can run those tests alongside your component tests.

When component tests are run for a story, the status is shown in the sidebar. The sidebar can be filtered to only show failing stories, and you can press the menu button on a failing story to see debugging options.

You can also run tests in watch mode, which will automatically re-run tests when you make changes to your components or stories. To activate, press the watch mode toggle (the eye icon) in the testing widget.

Before installing, make sure your project meets the following requirements:

Using with Next.js — The Vitest addon is supported in Next.js ≥ 14.1 projects, but you must be using the @storybook/nextjs-vite framework. When you run the setup command below, you will be prompted to install and use the framework if you haven't already.

Run the following command to install and configure the addon, which contains the plugin to run your stories as tests using Vitest:

That add command will install and register the Vitest addon. It will also inspect your project's Vite and Vitest setup, and install and configure them with sensible defaults, if necessary. You may need to adjust the configuration to fit your project's needs. The full configuration options can be found in the API section, below.

For some project setups, the add command may be unable to automate the addon and plugin setup and ask you to complete additional setup steps. Here's what to do:

When the addon is set up automatically, it will create or adjust your Vitest configuration files for you. If you're setting up manually, you can use the

*[Content truncated - see full docs]*

**Examples**:

```text
npx storybook add @storybook/addon-vitest
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
import { setProjectAnnotations } from '@storybook/your-framework';
import * as previewAnnotations from './preview';
 
const annotations = setProjectAnnotations([previewAnnotations]);
```

```python
import { defineConfig, defineProject, mergeConfig } from 'vitest/config';
import { storybookTest } from '@storybook/addon-vitest/vitest-plugin';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
 
const dirname =
  typeof __dirname !== 'undefined' ? __dirname : path.dirname(fileURLToPath(import.meta.url));
 
import viteConfig from './vite.config';
 
export default mergeConfig(
  viteConfig,
  defineConfig({
    test: {
      // Use `workspace` field in Vitest < 3.2
      pr
...
```

---

## Webpack

**URL**: https://storybook.js.org/docs/builders/webpack

**Contents**:
- Webpack
- Configure
  - Override the default configuration
    - Working with Webpack plugins
  - Import a custom Webpack configuration
  - Debug Webpack configuration
- Compiler support
  - SWC

Storybook Webpack builder is the default builder for Storybook. This builder enables you to create a seamless development and testing experience for your components and provides an efficient way to develop UI components in isolation allowing you to leverage your existing Webpack configuration with Storybook.

By default, Storybook provides zero-config support for Webpack and automatically sets up a baseline configuration created to work with the most common use cases. However, you can extend your Storybook configuration file (i.e., .storybook/main.js|ts) and provide additional options to improve your Storybook's performance or customize it to your needs. Listed below are the available options and examples of how to use them.

Storybook's Webpack configuration is based on Webpack 5, allowing it to be extended to fit your project's needs. If you need to add a loader or a plugin, you can provide the webpackFinal configuration element in your .storybook/main.js|ts file. The configuration element should export a function that receives the baseline configuration as the first argument and Storybook's options object as the second argument. For example:

When Storybook starts, it automatically merges the configuration into its own. However, when providing the webpackFinal configuration element, you're responsible for merging the configuration yourself. We recommend that you handle the changes to the config object responsibly, preserving both the entry and output properties.

Another way to customize your Storybook configuration is to add a custom plugin or loader to help with code optimization, asset management, or other tasks. Nevertheless, since Storybook relies on the HtmlWebpackPlugin to generate the preview page, we recommend that you append the changes to the config.plugins array rather than overwriting it. For example:

Additionally, when working with Webpack loaders that don't explicitly include specific file extensions (i.e., via the test property), you should exclu

*[Content truncated - see full docs]*

**Examples**:

```python
// Replace your-framework with the framework you are using, e.g. react-webpack5, nextjs, angular, etc.
import type { StorybookConfig } from '@storybook/your-framework';
 
const config: StorybookConfig = {
  framework: '@storybook/your-framework',
  stories: ['../src/**/*.mdx', '../src/**/*.stories.@(js|jsx|mjs|ts|tsx)'],
  core: {
    builder: {
      name: '@storybook/builder-webpack5',
      options: {
        fsCache: true,
        lazyCompilation: true,
      },
    },
  },
};
 
export defau
...
```

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

```python
// Replace your-framework with the framework you are using, e.g. react-webpack5, nextjs, angular, etc.
import type { StorybookConfig } from '@storybook/your-framework';
 
const config: StorybookConfig = {
  framework: '@storybook/your-framework',
  stories: ['../src/**/*.mdx', '../src/**/*.stories.@(js|jsx|mjs|ts|tsx)'],
  webpackFinal: async (config) => {
    config.plugins.push(/* ... */);
    return config;
  },
};
 
export default config;
```

---

## What's a story?

**URL**: https://storybook.js.org/docs/get-started/whats-a-story

**Contents**:
- What's a story?
- Working with stories
  - Create a new story
  - Edit a story

A story captures the rendered state of a UI component. Developers write multiple stories per component that describe all the “interesting” states a component can support.

When you installed Storybook, the CLI created example components that demonstrate the types of components you can build with Storybook: Button, Header, and Page.

Each example component has a set of stories that show the states it supports. You can browse the stories in the UI and see the code behind them in files that end with .stories.js|ts. The stories are written in Component Story Format (CSF), an ES6 modules-based standard for writing component examples.

Let’s start with the Button component. A story is an object that describes how to render the component in question. Here’s how to render Button in the “primary” state and export a story called Primary.

View the rendered Button by clicking on it in the Storybook sidebar. Note how the values specified in args are used to render the component and match those represented in the Controls panel. Using args in your stories has additional benefits:

Storybook makes it easy to work on one component in one state (aka a story) at a time. When you edit a component's code or its stories, Storybook will instantly re-render in the browser. No need to refresh manually.

If you're working on a component that does not yet have any stories, you can click the ➕ button in the sidebar to search for your component and have a basic story created for you.

You can also create a story file for your new story. We recommend copy/pasting an existing story file next to the component source file, then adjusting it for your component.

If you're working on a component that already has other stories, you can use the Controls panel to adjust the value of a control and then save those changes as a new story.

Or, if you prefer, edit the story file's code to add a new named export for your story:

Using the Controls panel, update a control's value for a story. You can then s

*[Content truncated - see full docs]*

**Examples**:

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
import type { Meta, StoryObj } from '@storybook/your-framework';
 
import { Button } from './Button';
 
const meta = {
  component: Button,
} satisfies Meta<typeof Button>;
 
export default meta;
type Story = StoryObj<typeof meta>;
 
export const Primary: Story = {
  args: {
    primary: true,
    label: 'Button',
  },
};
```

---

## Why Storybook?

**URL**: https://storybook.js.org/docs/get-started/why-storybook

**Contents**:
- Why Storybook?
- The problem
- The solution
  - Build UIs in isolation
  - Capture UI variations as “stories”
  - Storybook keeps track of every story
- Benefits
- Write stories once, reuse everywhere

The web’s universality is pushing more complexity into the frontend. It began with responsive web design, which turned every user interface from one to 10, 100, 1000 different user interfaces. Over time, additional requirements piled on like devices, browsers, accessibility, performance, and async states.

Component-driven tools like React, Vue 3, and Angular help break down complex UIs into simple components but they’re not silver bullets. As frontends grow, the number of components swells. Mature projects can contain hundreds of components that yield thousands of discrete variations.

To complicate matters further, those UIs are painful to debug because they’re entangled in business logic, interactive states, and app context.

The breadth of modern frontends overwhelm existing workflows. Developers must consider countless UI variations, yet aren’t equipped to develop or organize them all. You end up in a situation where UIs are tougher to build, less satisfying to work on, and brittle.

Every piece of UI is now a component. The superpower of components is that you don't need to spin up the whole app just to see how they render. You can render a specific variation in isolation by passing in props, mocking data, or faking events.

Storybook is packaged as a small, development-only, workshop that lives alongside your app. It provides an isolated iframe to render components without interference from app business logic and context. That helps you focus development on each variation of a component, even the hard-to-reach edge cases.

When developing a component variation in isolation, save it as a story. Stories are a declarative syntax for supplying props and mock data to simulate component variations. Each component can have multiple stories. Each story allows you to demonstrate a specific variation of that component to verify appearance and behavior.

You write stories for granular UI component variation and then use those stories in development, testing, and documen

*[Content truncated - see full docs]*

**Examples**:

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
import type { Meta, StoryObj } from '@storybook/your-framework';
 
import { Histogram } from './Histogram';
 
const meta = {
  component: Histogram,
} satisfies Meta<typeof Histogram>;
 
export default meta;
type Story = StoryObj<typeof meta>;
 
export const Default: Story = {
  args: {
    dataType: 'latency',
    showHistogramLabels: true,
    histogramAccentColor: '#1EA7FD',
    label: 'Late
...
```

---

## Write an addon

**URL**: https://storybook.js.org/docs/addons/writing-addons

**Contents**:
- Write an addon
- What are we going to build?
- Addon anatomy
  - UI-based addons
- Setup
  - Understanding the build system
- Register the addon
  - Conditionally render the addon

Storybook addons are a powerful way to extend Storybook's functionality and customize the development experience. They can be used to add new features, customize the UI, or integrate with third-party tools.

This reference guide is to help you develop a mental model for how Storybook addons work by building a simple addon based on the popular Outline addon (which is the historical basis for the built-in outline feature). Throughout this guide, you'll learn how addons are structured, Storybook's APIs, how to test your addon locally, and how to publish it.

There are two main categories of addons, each with its role:

The addon built in this guide is a UI-based addon, specifically a toolbar addon, enabling users to draw outlines around each element in the story through a shortcut or click of a button. UI addons can create other types of UI elements, each with its function: panels and tabs, providing users with various ways to interact with the UI.

To create your first addon, you're going to use the Addon Kit, a ready-to-use template featuring all the required building blocks, dependencies and configurations to help you get started building your addon. In the Addon Kit repository, click the Use this template button to create a new repository based on the Addon Kit's code.

Clone the repository you just created and install its dependencies. When the installation process finishes, you will be prompted with questions to configure your addon. Answer them, and when you're ready to start building your addon, run the following command to start Storybook in development mode and develop your addon in watch mode:

The Addon Kit uses Typescript by default. If you want to use JavaScript instead, you can run the eject-ts command to convert the project to JavaScript.

Addons built in the Storybook ecosystem rely on tsup, a fast, zero-config bundler powered by esbuild to transpile your addon's code into modern JavaScript that can run in the browser. Out of the box, the Addon Kit com

*[Content truncated - see full docs]*

**Examples**:

```python
import React, { memo, useCallback, useEffect } from 'react';
 
import { useGlobals, useStorybookApi } from 'storybook/manager-api';
import { IconButton } from 'storybook/internal/components';
import { LightningIcon } from '@storybook/icons';
 
import { ADDON_ID, PARAM_KEY, TOOL_ID } from './constants';
 
export const Tool = memo(function MyAddonSelector() {
  const [globals, updateGlobals] = useGlobals();
  const api = useStorybookApi();
 
  const isActive = [true, 'true'].includes(globals[PARAM
...
```

```text
npm run start
```

```python
import React, { memo, useCallback, useEffect } from 'react';
 
import { useGlobals, useStorybookApi } from 'storybook/manager-api';
import { IconButton } from 'storybook/internal/components';
import { LightningIcon } from '@storybook/icons';
 
import { ADDON_ID, PARAM_KEY, TOOL_ID } from './constants';
 
export const Tool = memo(function MyAddonSelector() {
  const [globals, updateGlobals] = useGlobals();
  const api = useStorybookApi();
 
  const isActive = [true, 'true'].includes(globals[PARAM
...
```

---
