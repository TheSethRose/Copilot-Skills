# Chakra-Ui - Get-Started

**Pages**: 24

---

## AI Rules

**URL**: https://chakra-ui.com/docs/get-started/ai/rules

**Contents**:
- AI Rules
- Configuration File
- Rules
  - Core Migration
  - Component
  - Prop Name
  - Style System
- Example .cursorrules File

Configure AI assistants with Chakra UI v3 rules for better code generation

Configure your AI coding assistants (like Cursor, GitHub Copilot, or Claude) by adding these rules to your project's .cursorrules, .github/copilot-instructions.md, or AI configuration file.

Create a file with the following rules in your project root:

Create a .cursorrules file in your project root. Then feel free to copy and paste the rules above.

**Examples**:

```text
.cursorrules
```

```text
.github/copilot-instructions.md
```

```typescript
---
description: Chakra UI v3 Development Rules
globs: "*.tsx"
alwaysApply: false
---
```

---

## CLI

**URL**: https://chakra-ui.com/docs/get-started/cli

**Contents**:
- CLI
- Installation
- Usage
- chakra typegen
- chakra snippet
- chakra blocks
  - Pro API Key Setup
  - Available Options

Learn more to use the Chakra CLI command to generate snippets, typings, and download Pro blocks

The Chakra UI CLI can be used to generate typings for your custom theme tokens, like colors, semantic tokens, recipe variants, etc. You can also add community snippets and premium Pro blocks to your project.

In order to use the CLI, you need to install it as a dev dependency in your project:

Use the Chakra CLI to run any of the commands listed below with your preferred package manager.

Generates theme and recipe typings for your custom theme. This helps to provide autocompletion and type safety in your project.

Generates useful component compositions that boost your development speed.

Add premium blocks from Chakra UI Pro to your project. These are professionally designed, fully responsive components that you can customize for your needs.

To use Pro blocks, you need a Chakra UI Pro subscription and API key:

Get your API key from Chakra UI Pro

Set the environment variable:

Or create a .env file in your project root:

Add it to your shell profile (.bashrc, .zshrc, etc.) for persistence if using environment variables

Generated the file(s) that contain the default theme tokens and recipes so you can have full control over them.

After generating the typings, you need to "Restart TS Server" for the autocomplete to show up.

Alternatively, you can install the @chakra-ui/cli package locally as a dev dependency and run the chakra typegen command to generate the typings.

**Examples**:

```text
npm i -D @chakra-ui/cli
```

```text
npm i -D @chakra-ui/cli
```

```text
pnpm add -D @chakra-ui/cli
```

---

## Contributing to Chakra UI

**URL**: https://chakra-ui.com/docs/get-started/contributing

**Contents**:
- Contributing to Chakra UI
- Overview
- Architecture
  - Filing Issues
  - Feature Requests
- Local Setup
- Recommended Extensions

The guide to contributing to Chakra UI v3.0

Thanks for showing interest to contribute to Chakra UI 💖, you rock!

Here are a few ways you can help improve Chakra UI

Chakra v3.x is a composition of two projects in the Chakra ecosystem, Ark UI and Zag.js. The goal is to maintain as little code as possible in Chakra UI, and delegate the heavy lifting to these projects.

Component logic modelled as a state machine

State machine from Zag.js converted to headless UI components

The mindset for filing issues on Chakra v3.x works like this:

If the issue is a logic or accessibility bug, then it's most likely a bug in Zag.js. Consider opening an issue in the Zag.js repository.

If it's a styling issue, then you can fix it directly in the Chakra UI repo.

The mindset for filing feature requests on Chakra v3.x works like this:

If the feature is a new component without logic, then it can go in Chakra UI or Ark UI. Start a discussion on the Chakra UI repository

If the feature is a new component with logic, it belongs in Zag.js. Start a discussion on the Zag.js repository.

We recommend using the following extensions in your editor:

**Examples**:

```text
apps/compositions/src/examples
```

```text
git clone https://github.com/chakra-ui/chakra-ui.git
```

```text
git clone https://github.com/chakra-ui/chakra-ui.git
```

---

## Figma

**URL**: https://chakra-ui.com/docs/get-started/figma

**Contents**:
- Figma
- Get the Kit

Use the official Chakra UI Figma Kit to design faster and stay in sync with your code.

The official Chakra UI v3 Figma Kit is now available!

This kit helps you design with the same building blocks that exist in code, making it easier for developers and designers to collaborate, stay consistent, and move faster.

You can access the kit for free on Figma Community:

👉🏽 Chakra UI v3 Figma Kit

Everything in the kit is designed to reflect how Chakra UI works, so your design decisions translate directly into production components.

---

## Installation

**URL**: https://chakra-ui.com/docs/get-started/installation

**Contents**:
- Installation
- Framework Guide
- Installation
  - Install @chakra-ui/react
  - Add snippets
  - Setup provider
  - Update tsconfig
  - Enjoy!

How to install and set up Chakra UI in your project

Chakra UI works in your favorite framework. We've put together step-by-step guides for these frameworks

Easily add Chakra UI with Next.js app

Use Chakra UI with Vite

Try Chakra UI in Stackblitz sandbox

The minimum node version required is Node.20.x

To manually set up Chakra UI in your project, follow the steps below.

Snippets are pre-built components that you can use to build your UI faster. Using the @chakra-ui/cli you can add snippets to your project.

Wrap your application with the Provider component generated in the components/ui/provider component at the root of your application.

This provider composes the following:

If you're using TypeScript, you need to update the compilerOptions in the tsconfig file to include the following options:

If you're using JavaScript, create a jsconfig.json file and add the above code to the file.

With the power of the snippets and the primitive components from Chakra UI, you can build your UI faster.

Watch our official courses and dive into dozens of videos that will teach you everything you need to know about Chakra UI, from basics to advanced concepts.

Whether you're a beginner or advanced Chakra UI user, joining our community is the best way to connect with like-minded people who build great products with the library.

**Examples**:

```text
@chakra-ui/react
```

```text
npm i @chakra-ui/react @emotion/react
```

```text
npm i @chakra-ui/react @emotion/react
```

---

## Installation

**URL**: https://chakra-ui.com/docs/get-started/installation#setup-provider

**Contents**:
- Installation
- Framework Guide
- Installation
  - Install @chakra-ui/react
  - Add snippets
  - Setup provider
  - Update tsconfig
  - Enjoy!

How to install and set up Chakra UI in your project

Chakra UI works in your favorite framework. We've put together step-by-step guides for these frameworks

Easily add Chakra UI with Next.js app

Use Chakra UI with Vite

Try Chakra UI in Stackblitz sandbox

The minimum node version required is Node.20.x

To manually set up Chakra UI in your project, follow the steps below.

Snippets are pre-built components that you can use to build your UI faster. Using the @chakra-ui/cli you can add snippets to your project.

Wrap your application with the Provider component generated in the components/ui/provider component at the root of your application.

This provider composes the following:

If you're using TypeScript, you need to update the compilerOptions in the tsconfig file to include the following options:

If you're using JavaScript, create a jsconfig.json file and add the above code to the file.

With the power of the snippets and the primitive components from Chakra UI, you can build your UI faster.

Watch our official courses and dive into dozens of videos that will teach you everything you need to know about Chakra UI, from basics to advanced concepts.

Whether you're a beginner or advanced Chakra UI user, joining our community is the best way to connect with like-minded people who build great products with the library.

**Examples**:

```text
@chakra-ui/react
```

```text
npm i @chakra-ui/react @emotion/react
```

```text
npm i @chakra-ui/react @emotion/react
```

---

## Installation

**URL**: https://chakra-ui.com/docs/get-started/installation#add-snippets

**Contents**:
- Installation
- Framework Guide
- Installation
  - Install @chakra-ui/react
  - Add snippets
  - Setup provider
  - Update tsconfig
  - Enjoy!

How to install and set up Chakra UI in your project

Chakra UI works in your favorite framework. We've put together step-by-step guides for these frameworks

Easily add Chakra UI with Next.js app

Use Chakra UI with Vite

Try Chakra UI in Stackblitz sandbox

The minimum node version required is Node.20.x

To manually set up Chakra UI in your project, follow the steps below.

Snippets are pre-built components that you can use to build your UI faster. Using the @chakra-ui/cli you can add snippets to your project.

Wrap your application with the Provider component generated in the components/ui/provider component at the root of your application.

This provider composes the following:

If you're using TypeScript, you need to update the compilerOptions in the tsconfig file to include the following options:

If you're using JavaScript, create a jsconfig.json file and add the above code to the file.

With the power of the snippets and the primitive components from Chakra UI, you can build your UI faster.

Watch our official courses and dive into dozens of videos that will teach you everything you need to know about Chakra UI, from basics to advanced concepts.

Whether you're a beginner or advanced Chakra UI user, joining our community is the best way to connect with like-minded people who build great products with the library.

**Examples**:

```text
@chakra-ui/react
```

```text
npm i @chakra-ui/react @emotion/react
```

```text
npm i @chakra-ui/react @emotion/react
```

---

## Installation

**URL**: https://chakra-ui.com/docs/get-started/installation#contribute

**Contents**:
- Installation
- Framework Guide
- Installation
  - Install @chakra-ui/react
  - Add snippets
  - Setup provider
  - Update tsconfig
  - Enjoy!

How to install and set up Chakra UI in your project

Chakra UI works in your favorite framework. We've put together step-by-step guides for these frameworks

Easily add Chakra UI with Next.js app

Use Chakra UI with Vite

Try Chakra UI in Stackblitz sandbox

The minimum node version required is Node.20.x

To manually set up Chakra UI in your project, follow the steps below.

Snippets are pre-built components that you can use to build your UI faster. Using the @chakra-ui/cli you can add snippets to your project.

Wrap your application with the Provider component generated in the components/ui/provider component at the root of your application.

This provider composes the following:

If you're using TypeScript, you need to update the compilerOptions in the tsconfig file to include the following options:

If you're using JavaScript, create a jsconfig.json file and add the above code to the file.

With the power of the snippets and the primitive components from Chakra UI, you can build your UI faster.

Watch our official courses and dive into dozens of videos that will teach you everything you need to know about Chakra UI, from basics to advanced concepts.

Whether you're a beginner or advanced Chakra UI user, joining our community is the best way to connect with like-minded people who build great products with the library.

**Examples**:

```text
@chakra-ui/react
```

```text
npm i @chakra-ui/react @emotion/react
```

```text
npm i @chakra-ui/react @emotion/react
```

---

## Installation

**URL**: https://chakra-ui.com/docs/get-started/installation#framework-guide

**Contents**:
- Installation
- Framework Guide
- Installation
  - Install @chakra-ui/react
  - Add snippets
  - Setup provider
  - Update tsconfig
  - Enjoy!

How to install and set up Chakra UI in your project

Chakra UI works in your favorite framework. We've put together step-by-step guides for these frameworks

Easily add Chakra UI with Next.js app

Use Chakra UI with Vite

Try Chakra UI in Stackblitz sandbox

The minimum node version required is Node.20.x

To manually set up Chakra UI in your project, follow the steps below.

Snippets are pre-built components that you can use to build your UI faster. Using the @chakra-ui/cli you can add snippets to your project.

Wrap your application with the Provider component generated in the components/ui/provider component at the root of your application.

This provider composes the following:

If you're using TypeScript, you need to update the compilerOptions in the tsconfig file to include the following options:

If you're using JavaScript, create a jsconfig.json file and add the above code to the file.

With the power of the snippets and the primitive components from Chakra UI, you can build your UI faster.

Watch our official courses and dive into dozens of videos that will teach you everything you need to know about Chakra UI, from basics to advanced concepts.

Whether you're a beginner or advanced Chakra UI user, joining our community is the best way to connect with like-minded people who build great products with the library.

**Examples**:

```text
@chakra-ui/react
```

```text
npm i @chakra-ui/react @emotion/react
```

```text
npm i @chakra-ui/react @emotion/react
```

---

## Installation

**URL**: https://chakra-ui.com/docs/get-started/installation#update-tsconfig

**Contents**:
- Installation
- Framework Guide
- Installation
  - Install @chakra-ui/react
  - Add snippets
  - Setup provider
  - Update tsconfig
  - Enjoy!

How to install and set up Chakra UI in your project

Chakra UI works in your favorite framework. We've put together step-by-step guides for these frameworks

Easily add Chakra UI with Next.js app

Use Chakra UI with Vite

Try Chakra UI in Stackblitz sandbox

The minimum node version required is Node.20.x

To manually set up Chakra UI in your project, follow the steps below.

Snippets are pre-built components that you can use to build your UI faster. Using the @chakra-ui/cli you can add snippets to your project.

Wrap your application with the Provider component generated in the components/ui/provider component at the root of your application.

This provider composes the following:

If you're using TypeScript, you need to update the compilerOptions in the tsconfig file to include the following options:

If you're using JavaScript, create a jsconfig.json file and add the above code to the file.

With the power of the snippets and the primitive components from Chakra UI, you can build your UI faster.

Watch our official courses and dive into dozens of videos that will teach you everything you need to know about Chakra UI, from basics to advanced concepts.

Whether you're a beginner or advanced Chakra UI user, joining our community is the best way to connect with like-minded people who build great products with the library.

**Examples**:

```text
@chakra-ui/react
```

```text
npm i @chakra-ui/react @emotion/react
```

```text
npm i @chakra-ui/react @emotion/react
```

---

## Installation

**URL**: https://chakra-ui.com/docs/get-started/installation#installation

**Contents**:
- Installation
- Framework Guide
- Installation
  - Install @chakra-ui/react
  - Add snippets
  - Setup provider
  - Update tsconfig
  - Enjoy!

How to install and set up Chakra UI in your project

Chakra UI works in your favorite framework. We've put together step-by-step guides for these frameworks

Easily add Chakra UI with Next.js app

Use Chakra UI with Vite

Try Chakra UI in Stackblitz sandbox

The minimum node version required is Node.20.x

To manually set up Chakra UI in your project, follow the steps below.

Snippets are pre-built components that you can use to build your UI faster. Using the @chakra-ui/cli you can add snippets to your project.

Wrap your application with the Provider component generated in the components/ui/provider component at the root of your application.

This provider composes the following:

If you're using TypeScript, you need to update the compilerOptions in the tsconfig file to include the following options:

If you're using JavaScript, create a jsconfig.json file and add the above code to the file.

With the power of the snippets and the primitive components from Chakra UI, you can build your UI faster.

Watch our official courses and dive into dozens of videos that will teach you everything you need to know about Chakra UI, from basics to advanced concepts.

Whether you're a beginner or advanced Chakra UI user, joining our community is the best way to connect with like-minded people who build great products with the library.

**Examples**:

```text
@chakra-ui/react
```

```text
npm i @chakra-ui/react @emotion/react
```

```text
npm i @chakra-ui/react @emotion/react
```

---

## Installation

**URL**: https://chakra-ui.com/docs/get-started/installation#install-chakra-uireact

**Contents**:
- Installation
- Framework Guide
- Installation
  - Install @chakra-ui/react
  - Add snippets
  - Setup provider
  - Update tsconfig
  - Enjoy!

How to install and set up Chakra UI in your project

Chakra UI works in your favorite framework. We've put together step-by-step guides for these frameworks

Easily add Chakra UI with Next.js app

Use Chakra UI with Vite

Try Chakra UI in Stackblitz sandbox

The minimum node version required is Node.20.x

To manually set up Chakra UI in your project, follow the steps below.

Snippets are pre-built components that you can use to build your UI faster. Using the @chakra-ui/cli you can add snippets to your project.

Wrap your application with the Provider component generated in the components/ui/provider component at the root of your application.

This provider composes the following:

If you're using TypeScript, you need to update the compilerOptions in the tsconfig file to include the following options:

If you're using JavaScript, create a jsconfig.json file and add the above code to the file.

With the power of the snippets and the primitive components from Chakra UI, you can build your UI faster.

Watch our official courses and dive into dozens of videos that will teach you everything you need to know about Chakra UI, from basics to advanced concepts.

Whether you're a beginner or advanced Chakra UI user, joining our community is the best way to connect with like-minded people who build great products with the library.

**Examples**:

```text
@chakra-ui/react
```

```text
npm i @chakra-ui/react @emotion/react
```

```text
npm i @chakra-ui/react @emotion/react
```

---

## Installation

**URL**: https://chakra-ui.com/docs/get-started/installation#enjoy

**Contents**:
- Installation
- Framework Guide
- Installation
  - Install @chakra-ui/react
  - Add snippets
  - Setup provider
  - Update tsconfig
  - Enjoy!

How to install and set up Chakra UI in your project

Chakra UI works in your favorite framework. We've put together step-by-step guides for these frameworks

Easily add Chakra UI with Next.js app

Use Chakra UI with Vite

Try Chakra UI in Stackblitz sandbox

The minimum node version required is Node.20.x

To manually set up Chakra UI in your project, follow the steps below.

Snippets are pre-built components that you can use to build your UI faster. Using the @chakra-ui/cli you can add snippets to your project.

Wrap your application with the Provider component generated in the components/ui/provider component at the root of your application.

This provider composes the following:

If you're using TypeScript, you need to update the compilerOptions in the tsconfig file to include the following options:

If you're using JavaScript, create a jsconfig.json file and add the above code to the file.

With the power of the snippets and the primitive components from Chakra UI, you can build your UI faster.

Watch our official courses and dive into dozens of videos that will teach you everything you need to know about Chakra UI, from basics to advanced concepts.

Whether you're a beginner or advanced Chakra UI user, joining our community is the best way to connect with like-minded people who build great products with the library.

**Examples**:

```text
@chakra-ui/react
```

```text
npm i @chakra-ui/react @emotion/react
```

```text
npm i @chakra-ui/react @emotion/react
```

---

## Installation

**URL**: https://chakra-ui.com/docs/get-started/installation#learn

**Contents**:
- Installation
- Framework Guide
- Installation
  - Install @chakra-ui/react
  - Add snippets
  - Setup provider
  - Update tsconfig
  - Enjoy!

How to install and set up Chakra UI in your project

Chakra UI works in your favorite framework. We've put together step-by-step guides for these frameworks

Easily add Chakra UI with Next.js app

Use Chakra UI with Vite

Try Chakra UI in Stackblitz sandbox

The minimum node version required is Node.20.x

To manually set up Chakra UI in your project, follow the steps below.

Snippets are pre-built components that you can use to build your UI faster. Using the @chakra-ui/cli you can add snippets to your project.

Wrap your application with the Provider component generated in the components/ui/provider component at the root of your application.

This provider composes the following:

If you're using TypeScript, you need to update the compilerOptions in the tsconfig file to include the following options:

If you're using JavaScript, create a jsconfig.json file and add the above code to the file.

With the power of the snippets and the primitive components from Chakra UI, you can build your UI faster.

Watch our official courses and dive into dozens of videos that will teach you everything you need to know about Chakra UI, from basics to advanced concepts.

Whether you're a beginner or advanced Chakra UI user, joining our community is the best way to connect with like-minded people who build great products with the library.

**Examples**:

```text
@chakra-ui/react
```

```text
npm i @chakra-ui/react @emotion/react
```

```text
npm i @chakra-ui/react @emotion/react
```

---

## LLMs.txt Documentation

**URL**: https://chakra-ui.com/docs/get-started/ai/llms

**Contents**:
- LLMs.txt Documentation
- Directory Overview
- Usage
  - Cursor
  - Windstatic

How to get tools like Cursor, Windstatic, GitHub Copilot, ChatGPT, and Claude to understand Chakra v3.

We support LLMs.txt files for making the Chakra UI v3 documentation available to large language models.

The following files are available.

Separate docs are available if you have a limited context window.

We also have a special llms-v3-migration.txt file that contains documentation for migrating to Chakra UI v3.

Use @Docs feature in Cursor to include the LLMs.txt files in your project.

Reference the LLMs.txt files using @ or in your .windsurfrules files.

**Examples**:

```text
llms-v3-migration.txt
```

```text
.windsurfrules
```

---

## MCP Server

**URL**: https://chakra-ui.com/docs/get-started/ai/mcp-server

**Contents**:
- MCP Server
- Tools
  - Component Tools
  - Chakra UI Pro Tools
  - Design System Tools
  - Migration Tools
- Setup
  - Visual Studio Code

Bridging the gap between AI agents and Chakra UI

The Chakra UI MCP Server is a specialized Model Context Protocol server that provides AI assistants (like Claude Code, Cursor, and Copilot) with access to the Chakra UI component library, design tokens, and migration guidance.

The Chakra UI MCP exposes the following tools to AI agents:

These tools provide AI agents with access to well-designed, fully responsive, and accessible component templates from Chakra UI Pro.

The MCP server currently supports only stdio transport and is published at @chakra-ui/react-mcp.

Make sure you have the GitHub Copilot and GitHub Copilot Chat extensions installed.

In the .vscode/mcp.json file at the root of your project, add the MCP server block:

The MCP server is now ready to use. Click on Start on the MCP server.

In the .cursor/mcp.json file at the root of your project, add the following configuration:

If Cursor doesn't automatically detect the changes, restart the editor or manually enable the Chakra UI server via "MCP Tools."

Make sure you have Claude Code installed. Visit Anthropic docs for installation instructions.

Run the following command in your terminal to add the Chakra UI MCP server:

The MCP server is now ready to use. Start a Claude Code session by running claude.

Navigate to "Settings" > "Windsurf Settings" > "Cascade"

Click the "Manage MCPs" button, then click the "View raw config" button.

Add the following to the MCP configuration file:

.codeium/windsurf/mcp_config.json

You might need to click the "Refresh" button to see the MCP server in the list.

Go to Settings > Open Settings

In the settings.json file, add MCP server as a new context server

.config/zed/settings.json

To run the MCP server in a local or development environment using a custom MCP client, you need to add the MCP server to the client's configuration file.

To enable access to premium component templates from Chakra UI Pro, you'll need to configure your API key. This requires an active C

*[Content truncated - see full docs]*

**Examples**:

```text
list_components
```

```text
get_component_props
```

```text
get_component_example
```

---

## Migration to v3

**URL**: https://chakra-ui.com/docs/get-started/migration

**Contents**:
- Migration to v3
- Steps
  - Update Packages
  - Refactor Custom Theme
  - Update ChakraProvider
- Improvements
- Removed Features
  - Color Mode

How to migrate to Chakra UI v3.x from v2.x

Watch the migration livestream (1)

Watch the migration livestream (2)

The minimum node version required is Node.20.x

Remove the unused packages: @emotion/styled and framer-motion. These packages are no longer required in Chakra UI.

Install updated versions of the packages: @chakra-ui/react and @emotion/react.

Next, install component snippets using the CLI snippets. Snippets provide pre-built compositions of Chakra components to save you time and put you in charge.

Move your custom theme to a dedicated theme.js or theme.ts file. Use createSystem and defaultConfig to configure your theme.

All token values need to be wrapped in an object with a value key. Learn more about tokens here.

Update the ChakraProvider import from @chakra-ui/react to the one from the snippets. Next, rename the theme prop to value to match the new system-based theming approach.

If you have a custom theme, replace defaultSystem with the custom system

The Provider component compose the ChakraProvider from Chakra and ThemeProvider from next-themes

Performance: Improved reconciliation performance by 4x and re-render performance by 1.6x

Namespaced imports: Import components using the dot notation for more concise imports

TypeScript: Improved IntelliSense and type inference for style props and tokens.

Polymorphism: Loosened the as prop typings in favor of using the asChild prop. This pattern was inspired by Radix Primitives and Ark UI.

We removed the hooks package in favor of using dedicated, robust libraries like react-use and usehooks-ts

The only hooks we ship now are useBreakpointValue, useCallbackRef, useDisclosure, useControllableState and useMediaQuery.

We removed the styleConfig and multiStyleConfig concept in favor of recipes and slot recipes. This pattern was inspired by Panda CSS.

We've removed the @chakra-ui/next-js package in favor of using the asChild prop for better flexibility.

To style the Next.js image component, use the a

*[Content truncated - see full docs]*

**Examples**:

```text
@emotion/styled
```

```text
framer-motion
```

```text
npm uninstall @emotion/styled framer-motion
```

---

## Using Chakra UI in Iframe

**URL**: https://chakra-ui.com/docs/get-started/environments/iframe

**Contents**:
- Using Chakra UI in Iframe
- Template
- Installation
  - Install dependencies
  - Add snippets
  - Update tsconfig
  - Setup Iframe
  - Setup provider

A guide for installing and using Chakra UI in an Iframe

Iframes are useful for isolating styles and logic in a separate context. For example, you might want to showcase a Chakra component in dedicated sandbox.

Use the following template to get started quickly

The minimum node version required is Node.20.x

The additional packages used are:

Snippets are pre-built components that you can use to build your UI faster. Using the @chakra-ui/cli you can add snippets to your project.

If you're using TypeScript, you need to update the compilerOptions in the tsconfig file to include the following options:

Create a components/ui/iframe-provider.tsx file to setup the iframe using the react-frame-component package.

components/ui/iframe-provider.tsx

Wrap your application with the Provider component generated in the components/ui/provider component at the root of your application.

This provider composes the following:

At any component in your application, wrap it with the IframeProvider component to render it inside the iframe.

If you created a custom theme using the createSystem function, ensure it's passed to the IframeProvider and Provider components to ensure it's used inside the iframe.

For example, let's say you created a custom theme:

Then, pass it to the IframeProvider and Provider components:

**Examples**:

```text
npm i @chakra-ui/react @emotion/react @emotion/cache react-frame-component
```

```text
npm i @chakra-ui/react @emotion/react @emotion/cache react-frame-component
```

```text
react-frame-component
```

---

## Using Chakra UI in Next.js (App)

**URL**: https://chakra-ui.com/docs/get-started/frameworks/next-app

**Contents**:
- Using Chakra UI in Next.js (App)
- Templates
- Installation
  - Install dependencies
  - Add snippets
  - Update tsconfig
  - Setup provider
  - Optimize Bundle

A guide for installing Chakra UI with Next.js app directory

Use one of the following templates to get started quickly. The templates are configured correctly to use Chakra UI.

Next.js pages template

The minimum node version required is Node.20.x

Snippets are pre-built components that you can use to build your UI faster. Using the @chakra-ui/cli you can add snippets to your project.

If you're using TypeScript, you need to update the compilerOptions in the tsconfig file to include the following options:

If you're using JavaScript, create a jsconfig.json file and add the above code to the file.

Wrap your application with the Provider component generated in the components/ui/provider component at the root of your application.

This provider composes the following:

Adding the suppressHydrationWarning prop to the html element is required to prevent the warning about the next-themes library.

We recommend using the experimental.optimizePackageImports feature in Next.js to optimize your bundle size by loading only the modules that you are actually using.

This also helps to resolve warnings like:

If you see an error like this: Hydration failed because the initial server rendered HTML did not match the client, and the error looks similar to:

This is caused by how Next.js hydrates Emotion CSS in --turbo mode. Please remove the --turbo flag from your dev script in your package.json file.

When this is fixed by the Next.js team, we'll update this guide.

With the power of the snippets and the primitive components from Chakra UI, you can build your UI faster.

**Examples**:

```text
npm i @chakra-ui/react @emotion/react
```

```text
npm i @chakra-ui/react @emotion/react
```

```text
@chakra-ui/cli
```

---

## Using Chakra UI in Next.js (Pages)

**URL**: https://chakra-ui.com/docs/get-started/frameworks/next-pages

**Contents**:
- Using Chakra UI in Next.js (Pages)
- Templates
- Installation
  - Install dependencies
  - Add snippets
  - Update tsconfig
  - Setup provider
  - Optimize Bundle

A guide for installing Chakra UI with Next.js pages directory

Use one of the following templates to get started quickly. The templates are configured correctly to use Chakra UI.

Next.js pages template

The minimum node version required is Node.20.x

Snippets are pre-built components that you can use to build your UI faster. Using the @chakra-ui/cli you can add snippets to your project.

If you're using TypeScript, you need to update the compilerOptions in the tsconfig file to include the following options:

If you're using JavaScript, create a jsconfig.json file and add the above code to the file.

Wrap your application with the Provider component at the root of your application.

This provider composes the following:

In the pages/_document.tsx file, add the suppressHydrationWarning prop to the html element.

We recommend using the experimental.optimizePackageImports feature in Next.js to optimize your bundle size by loading only the modules that you are actually using.

This also helps resolve warnings like:

If you see an error like this: Hydration failed because the initial server rendered HTML did not match the client, and the error looks similar to:

This is caused by how Next.js hydrates Emotion CSS in --turbo mode. Please remove the --turbo flag from your dev script in your package.json file.

When this is fixed by the Next.js team, we'll update this guide.

With the power of the snippets and the primitive components from Chakra UI, you can build your UI faster.

**Examples**:

```text
npm i @chakra-ui/react @emotion/react
```

```text
npm i @chakra-ui/react @emotion/react
```

```text
@chakra-ui/cli
```

---

## Using Chakra UI in Shadow DOM

**URL**: https://chakra-ui.com/docs/get-started/environments/shadow-dom

**Contents**:
- Using Chakra UI in Shadow DOM
- Template
- Installation
  - Install dependencies
  - Add snippets
  - Update tsconfig
  - Configure style engine
  - Setup provider

A guide for installing Chakra UI with Shadow DOM

When developing extensions for browsers or using Chakra as part of a large project, leveraging the Shadow DOM is useful for style and logic encapsulation.

Use the following template to get started quickly

The minimum node version required is Node.20.x

The additional packages used are:

Snippets are pre-built components that you can use to build your UI faster. Using the @chakra-ui/cli you can add snippets to your project.

If you're using TypeScript, you need to update the compilerOptions in the tsconfig file to include the following options:

Create a system.ts file in the root of your project and configure the style engine.

components/ui/system.ts

Good to know: The main purpose of the system.ts file is to configure the style engine to target the Shadow DOM.

Update the generated components/ui/provider component with the Provider component.

This provider composes the following:

components/ui/provider.tsx

Wrap your application with the Provider component generated in the components/ui/provider component at the root of your application.

With the power of the snippets and the primitive components from Chakra UI, you can build your UI faster.

**Examples**:

```text
npm i @chakra-ui/react @emotion/react @emotion/cache react-shadow
```

```text
npm i @chakra-ui/react @emotion/react @emotion/cache react-shadow
```

```text
react-shadow
```

---

## Using Chakra UI in Storybook

**URL**: https://chakra-ui.com/docs/get-started/frameworks/storybook

**Contents**:
- Using Chakra UI in Storybook
- Installation
  - Install dependencies
  - Setup Preview
  - Setup dark mode toggle
  - Start the Storybook server
  - Enjoy!

A guide for using Chakra UI with Storybook

Install the required dependencies for Chakra UI and Storybook.

Edit the .storybook/preview.tsx file to include the Chakra UI provider.

Use the withThemeByClassName decorator from @storybook/addon-themes to add a color mode toggle to the Storybook toolbar.

Use Chakra UI components in your stories.

**Examples**:

```text
npm i @storybook/addon-themes @chakra-ui/react @emotion/react
```

```text
npm i @storybook/addon-themes @chakra-ui/react @emotion/react
```

```typescript
.storybook/preview.tsx
```

---

## Using Chakra in Remix

**URL**: https://chakra-ui.com/docs/get-started/frameworks/remix

**Contents**:
- Using Chakra in Remix
- Templates
- Installation
  - Install dependencies
  - Add snippets
  - Setup emotion cache
  - Update tsconfig
  - Setup provider

A guide for installing Chakra UI with Remix projects

Use the remix template below to get started quickly.

Snippets are pre-built components that you can use to build your UI faster. Using the @chakra-ui/cli you can add snippets to your project.

Using snippets from the Remix sandbox, you can add the emotion cache to your application.

Emotion cache snippet

If you're using TypeScript, you need to update the compilerOptions in the tsconfig file to include the following options:

If you're using JavaScript, create a jsconfig.json file and add the above code to the file.

Wrap your application with the Provider component at the root of your application.

This provider composes the following:

When the power of the snippets and the primitive components from Chakra UI, you can build your UI faster.

You may encounter the following issues when using Chakra UI with Remix:

This is a known issue related to extension installed in your browser. We recommend testing your application in incognito mode to see if the issue persists.

We welcome contributions to fix this issue.

**Examples**:

```text
npm i @chakra-ui/react @emotion/react
```

```text
npm i @chakra-ui/react @emotion/react
```

```text
@chakra-ui/cli
```

---

## Using Chakra in Vite

**URL**: https://chakra-ui.com/docs/get-started/frameworks/vite

**Contents**:
- Using Chakra in Vite
- Templates
- Installation
  - Install dependencies
  - Add snippets
  - Update tsconfig
  - Setup provider
  - Setup Vite Config Paths

A guide for installing Chakra UI with Vite.js projects

Use the vite template below to get started quickly.

The minimum node version required is Node.20.x

Snippets are pre-built components that you can use to build your UI faster. Using the @chakra-ui/cli you can add snippets to your project.

If you're using TypeScript, in the tsconfig.app.json file, make sure the compilerOptions includes the following:

If you're using JavaScript, create a jsconfig.json file and add the above code to the file.

Wrap your application with the Provider component at the root of your application.

This provider composes the following:

In your project, set up a vite config path to automatically sync tsconfig with vite using the command:

Update the vite.config.ts file:

With the power of the snippets and the primitive components from Chakra UI, you can build your UI faster.

**Examples**:

```text
npm i @chakra-ui/react @emotion/react
```

```text
npm i @chakra-ui/react @emotion/react
```

```text
@chakra-ui/cli
```

---
