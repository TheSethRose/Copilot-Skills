# Storybook - Getting Started

**Pages**: 4

---

## Framework support

**URL**: https://storybook.js.org/docs/configure/integration/frameworks

**Contents**:
- Framework support
- How do frameworks work in Storybook?
- Which frameworks are supported?
  - What about feature support?
- Configure
- Troubleshooting
  - NextJS 13 doesn't work with Storybook
  - My framework doesn't work with Storybook

Frameworks are packages that auto-configure Storybook to work with most common environment setups. They simplify the setup process and reduce boilerplate by mirroring your framework's conventions to create applications.

You start by installing Storybook into an existing project. Then, it tries to detect the framework you're using and automatically configures Storybook to work with it. That means adding the necessary libraries as dependencies and adjusting the configuration. Finally, starting Storybook will automatically load the framework configuration before loading any existing addons to match your application environment.

Storybook provides support for the leading industry builders and frameworks. However, that doesn't mean you can't use Storybook with other frameworks. Below is a list of currently supported frameworks divided by their builders.

In addition to supporting the most popular frameworks in the industry, Storybook also tries to retain the same level of feature support for each framework, including the addon ecosystem. For more information, see Framework support for a comprehensive list of which features and addons are currently maintained with the community's help.

Every modern web application has unique requirements and relies on various tools and frameworks. By default, with Storybook, you get an out-of-the-box configuration generated to work with most frameworks. However, you can extend your existing configuration file (i.e., ./storybook/main.js|ts|cjs) and provide additional options. Below is an abridged table with available options and examples of configuring Storybook for your framework.

With the release of Next.js version 13, it introduced breaking changes (e.g., TurboPack, Server Components) that are not yet fully supported by Storybook. The Storybook team is working on adding support for these features. In the meantime, you can still use Storybook alongside your Next.js 13 project if you're not relying on them.

Out of the box, most frame

*[Content truncated - see full docs]*

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

## Install Storybook

**URL**: https://storybook.js.org/docs/get-started/install

**Contents**:
- Install Storybook
- Project requirements
- Run the Setup Wizard
- Start Storybook
  - Troubleshooting
    - Run Storybook with other package managers
    - The CLI doesn't detect my framework
    - Yarn Plug'n'Play (PnP) support with Storybook

Use the Storybook CLI to install it in a single command. Run this inside your project’s root directory:

For installing Storybook 8.3 or newer, you can use the create command with a specific version:

To install a Storybook version prior to 8.3, you must use the init command:

For either command, you can specify either an npm tag such as latest or next, or a (partial) version number. For example:

storybook@latest init will initialize the latest version

storybook@7.6.10 init will initialize 7.6.10

storybook@7 init will initialize the newest 7.x.x version

Storybook will look into your project's dependencies during its install process and provide you with the best configuration available.

The command above will make the following changes to your local environment:

Storybook is designed to work with a variety of frameworks and environments. If your project is using one of the packages listed here, please ensure that you have the following versions installed:

Additionally, the Storybook app supports the following browsers:

You can use Storybook with older browsers in two ways:

If all goes well, you should see a setup wizard that will help you get started with Storybook introducing you to the main concepts and features, including how the UI is organized, how to write your first story, and how to test your components' response to various inputs utilizing controls.

If you skipped the wizard, you can always run it again by adding the ?path=/onboarding query parameter to the URL of your Storybook instance, provided that the example stories are still available.

Storybook comes with a built-in development server featuring everything you need for project development. Depending on your system configuration, running the storybook command will start the local development server, output the address for you, and automatically open the address in a new browser tab where a welcome screen greets you.

Storybook collects completely anonymous data to help us improve user experi

*[Content truncated - see full docs]*

**Examples**:

```text
npm create storybook@latest
```

```text
npm create storybook@8.3
```

```text
npx storybook@8.2 init
```

---

## Install addons

**URL**: https://storybook.js.org/docs/addons/install-addons

**Contents**:
- Install addons
- Automatic installation
  - Manual installation
  - Removing addons

Storybook has hundreds of reusable addons packaged as NPM modules. Let's walk through how to extend Storybook by installing and registering addons.

Storybook includes a storybook add command to automate the setup of addons. Several community-led addons can be added using this command, except for preset addons. We encourage you to read the addon's documentation to learn more about its installation process.

Run the storybook add command using your chosen package manager, and the CLI will update your Storybook configuration to include the addon and install any necessary dependencies.

If you're attempting to install multiple addons at once, it will only install the first addon that was specified. This is a known limitation of the current implementation and will be addressed in a future release.

Storybook addons are always added through the addons configuration array in .storybook/main.js|ts. The following example shows how to manually add the Accessibility addon to Storybook.

Run the following command with your package manager of choice to install the addon.

Next, update .storybook/main.js|ts to the following:

When you run Storybook, the accessibility testing addon will be enabled.

To remove an addon from Storybook, you can choose to manually uninstall it and remove it from the configuration file (i.e., .storybook/main.js|ts) or opt-in to do it automatically via the CLI with the remove command. For example, to remove the Accessibility addon from Storybook with the CLI, run the following command:

**Examples**:

```text
npx storybook@latest add @storybook/addon-a11y
```

```text
npm install @storybook/addon-a11y --save-dev
```

```python
// Replace your-framework with the framework you are using (e.g., react-vite, vue3-vite, angular, etc.)
import type { StorybookConfig } from '@storybook/your-framework';
 
const config: StorybookConfig = {
  framework: '@storybook/your-framework',
  stories: ['../src/**/*.mdx', '../src/**/*.stories.@(js|jsx|mjs|ts|tsx)'],
  addons: [
    // Other Storybook addons
    '@storybook/addon-a11y', //👈 The a11y addon goes here
  ],
};
 
export default config;
```

---

## Setup Storybook

**URL**: https://storybook.js.org/docs/get-started/setup

**Contents**:
- Setup Storybook
- Render component styles
- Configure Storybook for your stack
- Load assets and resources

Now that you’ve learned what stories are and how to browse them, let’s demo working on one of your components.

Pick a simple component from your project, like a Button, and write a .stories.js, .stories.ts, or .stories.svelte file to go along with it. It might look something like this:

Go to your Storybook to view the rendered component. It’s OK if it looks a bit unusual right now.

Depending on your technology stack, you also might need to configure the Storybook environment further.

Storybook isn’t opinionated about how you generate or load CSS. It renders whatever DOM elements you provide. But sometimes, things won’t “look right” out of the box.

You may have to configure your CSS tooling for Storybook’s rendering environment. Here are some setup guides for popular tools in the community.

Don't see the tool that you're looking for? Check out the styling and css page for more details.

Storybook comes with a permissive default configuration. It attempts to customize itself to fit your setup. But it’s not foolproof.

Your project may have additional requirements before components can be rendered in isolation. This warrants customizing configuration further. There are three broad categories of configuration you might need.

If you see errors on the CLI when you run the yarn storybook command, you likely need to make changes to Storybook’s build configuration. Here are some things to try:

If Storybook builds but you see an error immediately when connecting to it in the browser, in that case, chances are one of your input files is not compiling/transpiling correctly to be interpreted by the browser. Storybook supports evergreen browsers, but you may need to check the Babel and Webpack settings (see above) to ensure your component code works correctly.

If a particular story has a problem rendering, often it means your component expects a specific environment is available to the component.

A common frontend pattern is for components to assume that they render in 

*[Content truncated - see full docs]*

**Examples**:

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
import type { Meta, StoryObj } from '@storybook/your-framework';
 
import { YourComponent } from './YourComponent';
 
//👇 This default export determines where your story goes in the story list
const meta = {
  component: YourComponent,
} satisfies Meta<typeof YourComponent>;
 
export default meta;
type Story = StoryObj<typeof meta>;
 
export const FirstStory: Story = {
  args: {
    //👇 The arg
...
```

```python
import React from 'react';
 
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
import type { Preview } from '@storybook/your-framework';
 
import { ThemeProvider } from 'styled-components';
 
const preview: Preview = {
  decorators: [
    (Story) => (
      <ThemeProvider theme="default">
        {/* 👇 Decorators in Storybook also accept a function. Replace <Story/> with Story() to enable it  */}
        <Story />
      </ThemeProvider>
    ),
...
```

---
