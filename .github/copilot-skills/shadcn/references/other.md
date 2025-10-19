# Shadcn - Other

**Pages**: 11

---

## Authentication - shadcn/ui

**URL**: https://ui.shadcn.com/docs/registry/authentication

**Contents**:
- Authentication
- Common Authentication Patterns
  - Token-Based Authentication
  - API Key Authentication
  - Query Parameter Authentication
- Server-Side Implementation
  - Next.js API Route Example
  - Express.js Example

Secure your registry with authentication for private and personalized components.

Authentication lets you run private registries, control who can access your components, and give different teams or users different content. This guide shows common authentication patterns and how to set them up.

Authentication enables these use cases:

The most common approach uses Bearer tokens or API keys:

Set your token in environment variables:

Some registries use API keys in headers:

For simpler setups, use query parameters:

This creates: https://registry.company.com/button.json?token=your_token

Here's how to add authentication to your registry server:

Give different teams different components:

Give users components based on their preferences:

Use expiring tokens for better security:

With namespaced registries, you can set up multiple registries with different authentication:

Never commit tokens to version control. Always use environment variables:

Then reference them in components.json:

Always use HTTPS URLs for registries to protect your tokens in transit:

Protect your registry from abuse:

Change access tokens regularly:

Track registry access for security and analytics:

Test your authenticated registry locally:

The shadcn CLI handles authentication errors gracefully:

Your registry server can return custom error messages in the response body, and the CLI will display them to users:

This helps provide context-specific guidance:

To set up authentication with multiple registries and advanced patterns, see the Namespaced Registries documentation. It covers:

**Examples**:

```text
{
  "registries": {
    "@private": {
      "url": "https://registry.company.com/{name}.json",
      "headers": {
        "Authorization": "Bearer ${REGISTRY_TOKEN}"
      }
    }
  }
}
```

```text
REGISTRY_TOKEN=your_secret_token_here
```

```text
{
  "registries": {
    "@company": {
      "url": "https://api.company.com/registry/{name}.json",
      "headers": {
        "X-API-Key": "${API_KEY}",
        "X-Workspace-Id": "${WORKSPACE_ID}"
      }
    }
  }
}
```

---

## Changelog - shadcn/ui

**URL**: https://ui.shadcn.com/docs/changelog

**Contents**:
- Changelog
- October 2025 - New Components
  - Spinner
  - Kbd
  - Button Group
  - Input Group
  - Field
  - Item

Latest updates and announcements.

For this round of components, I looked at what we build every day, the boring stuff we rebuild over and over, and made reusable abstractions you can actually use.

These components work with every component library, Radix, Base UI, React Aria, you name it. Copy and paste to your projects.

Okay let's start with the easiest ones: Spinner and Kbd. Pretty basic. We all know what they do.

Here's how you render a spinner:

Here's what it looks like:

Here's what it looks like in a button:

You can edit the code and replace it with your own spinner.

Kbd is a component that renders a keyboard key.

Use KbdGroup to group keyboard keys together.

You can add it to buttons, tooltips, input groups, and more.

I got a lot of requests for this one: Button Group. It's a container that groups related buttons together with consistent styling. Great for action groups, split buttons, and more.

You can nest button groups to create more complex layouts with spacing.

Use ButtonGroupSeparator to create split buttons. Classic dropdown pattern.

You can also use it to add prefix or suffix buttons and text to inputs.

Input Group lets you add icons, buttons, and more to your inputs. You know, all those little bits you always need around your inputs.

Here's a preview with icons:

You can also add buttons to the input group.

Or text, labels, tooltips,...

It also works with textareas so you can build really complex components with lots of knobs and dials or yet another prompt form.

Oh here are some cool ones with spinners:

Introducing Field, a component for building really complex forms. The abstraction here is beautiful.

It took me a long time to get it right but I made it work with all your form libraries: Server Actions, React Hook Form, TanStack Form, Bring Your Own Form.

Here's a basic field with an input:

Choose a unique username for your account.

Must be at least 8 characters long.

It works with all form controls. Inputs, textareas, selec

*[Content truncated - see full docs]*

**Examples**:

```python
import { Spinner } from "@/components/ui/spinner"
```

```text
<Spinner />
```

```python
import { Spinner } from "@/components/ui/spinner"

export function SpinnerBasic() {
  return (
    <div className="flex flex-col items-center justify-center gap-8">
      <Spinner />
    </div>
  )
}
```

---

## Figma - shadcn/ui

**URL**: https://ui.shadcn.com/docs/figma

**Contents**:
- Figma
- Paid
- Free

Every component recreated in Figma. With customizable props, typography and icons.

Note: The Figma files are contributed by the community. If you have any questions or feedback, please reach out to the Figma file maintainers.

---

## Introduction - shadcn/ui

**URL**: https://ui.shadcn.com/docs/registry

**Contents**:
- Introduction

Run your own code registry.

You can use the shadcn CLI to run your own code registry. Running your own registry allows you to distribute your custom components, hooks, pages, config, rules and other files to any project.

Note: The registry works with any project type and any framework, and is not limited to React.

A distribution system for code

Ready to create your own registry? In the next section, we'll walk you through setting up your own custom registry step-by-step, from creating your first component to publishing it for others to use.

Set up and build your own registry

Secure your registry with authentication

Configure registries with namespaces

Registry item examples and configurations

Schema specification for registry.json

---

## JavaScript - shadcn/ui

**URL**: https://ui.shadcn.com/docs/javascript

**Contents**:
- JavaScript

How to use shadcn/ui with JavaScript

This project and the components are written in TypeScript. We recommend using TypeScript for your project as well.

However we provide a JavaScript version of the components as well. The JavaScript version is available via the cli.

To opt-out of TypeScript, you can use the tsx flag in your components.json file.

To configure import aliases, you can use the following jsconfig.json:

**Examples**:

```typescript
{
  "style": "default",
  "tailwind": {
    "config": "tailwind.config.js",
    "css": "src/app/globals.css",
    "baseColor": "zinc",
    "cssVariables": true
  },
  "rsc": false,
  "tsx": false,
  "aliases": {
    "utils": "~/lib/utils",
    "components": "~/components"
  }
}
```

```text
{
  "compilerOptions": {
    "paths": {
      "@/*": ["./*"]
    }
  }
}
```

---

## Legacy Docs - shadcn/ui

**URL**: https://ui.shadcn.com/docs/legacy

**Contents**:
- Legacy Docs

View the legacy docs for shadcn/ui and Tailwind v3.

You're looking at the docs for shadcn/ui + Tailwind v4. If you're looking for the docs for shadcn/ui + Tailwind v3, you can find them here.

---

## MCP Server - shadcn/ui

**URL**: https://ui.shadcn.com/docs/registry/mcp

**Contents**:
- MCP Server
- Prerequisites
- Configuring MCP
- Best Practices

MCP support for registry developers

The shadcn MCP server works out of the box with any shadcn-compatible registry. You do not need to do anything special to enable MCP support for your registry.

The MCP server works by requesting your registry index. Make sure you have a registry item file at the root of your registry named registry.

For example, if your registry is hosted at https://acme.com/r/[name].json, you should have a file at https://acme.com/r/registry.json or https://acme.com/r/registry if you're using a JSON file extension.

This file must be a valid JSON file that conforms to the registry schema.

Ask your registry consumers to configure your registry in their components.json file and install the shadcn MCP server:

Configure your registry in your components.json file:

Run the following command in your project:

Restart Claude Code and try the following prompts:

Note: You can use /mcp command in Claude Code to debug the MCP server.

You can read more about the MCP server in the MCP documentation.

Here are some best practices for MCP-compatible registries:

**Examples**:

```text
{
  "registries": {
    "@acme": "https://acme.com/r/{name}.json"
  }
}
```

```text
pnpm dlx shadcn@latest mcp init --client claude
```

---

## Namespaces - shadcn/ui

**URL**: https://ui.shadcn.com/docs/registry/namespace

**Contents**:
- Namespaces
- Table of Contents
- Overview
- Decentralized Namespace System
  - Examples of Multi-Registry Setups
    - By Resource Type
    - By Team or Department
    - By Stability

Configure and use multiple resource registries with namespace support.

Namespaced registries let you configure multiple resource sources in one project. This means you can install components, libraries, utilities, AI prompts, configuration files, and other resources from various registries, whether they're public, third-party, or your own custom private libraries.

Registry namespaces are prefixed with @ and provide a way to organize and reference resources from different sources. Resources can be any type of content: components, libraries, utilities, hooks, AI prompts, configuration files, themes, and more. For example:

We intentionally designed the namespace system to be decentralized. There is a central open source registry index for open source namespaces but you are free to create and use any namespace you want.

This decentralized approach gives you complete flexibility to organize your resources however makes sense for your organization.

You can create multiple registries for different purposes:

Once configured, you can install resources using the namespace syntax:

or multiple resources at once:

Add registries to your components.json:

Then start installing:

Registry names must follow these rules:

The pattern for referencing resources is: @namespace/resource-name

Namespaced registries are configured in your components.json file under the registries field.

The simplest way to configure a registry is with a URL template string:

Note: The {name} placeholder in the URL is automatically parsed and replaced with the resource name when you run npx shadcn@latest add @namespace/resource-name. For example, @acme/button becomes https://registry.acme.com/resources/button.json. See URL Pattern System for more details.

For registries that require authentication or additional parameters, use the object format:

Note: Environment variables in the format ${VAR_NAME} are automatically expanded from your environment (process.env). This works in URLs, headers, and pa

*[Content truncated - see full docs]*

**Examples**:

```text
{
  "registries": {
    "@acme-ui": "https://registry.acme.com/ui/{name}.json",
    "@acme-docs": "https://registry.acme.com/docs/{name}.json",
    "@acme-ai": "https://registry.acme.com/ai/{name}.json",
    "@acme-themes": "https://registry.acme.com/themes/{name}.json",
    "@acme-internal": {
      "url": "https://internal.acme.com/registry/{name}.json",
      "headers": {
        "Authorization": "Bearer ${INTERNAL_TOKEN}"
      }
    }
  }
}
```

```text
{
  "@components": "https://cdn.company.com/components/{name}.json",
  "@hooks": "https://cdn.company.com/hooks/{name}.json",
  "@utils": "https://cdn.company.com/utils/{name}.json",
  "@prompts": "https://cdn.company.com/ai-prompts/{name}.json"
}
```

```text
{
  "@design": "https://design.company.com/registry/{name}.json",
  "@engineering": "https://eng.company.com/registry/{name}.json",
  "@marketing": "https://marketing.company.com/registry/{name}.json"
}
```

---

## Next.js 15 + React 19 - shadcn/ui

**URL**: https://ui.shadcn.com/docs/react-19

**Contents**:
- Next.js 15 + React 19
- TL;DR
- What's happening?
- How to fix this
  - Solution 1: --force or --legacy-peer-deps
  - What do the --force and --legacy-peer-deps flag do?
  - Solution 2: Use React 18
- Using shadcn/ui on Next.js 15

Using shadcn/ui with Next.js 15 and React 19.

Update: We have added full support for React 19 and Tailwind v4 in the canary release. See the docs for Tailwind v4 for more information.

The following guide applies to any framework that supports React 19. I titled this page "Next.js 15 + React 19" to help people upgrading to Next.js 15 find it. We are working with package maintainers to help upgrade to React 19.

If you're using npm, you can install shadcn/ui dependencies with a flag. The shadcn CLI will prompt you to select a flag when you run it. No flags required for pnpm, bun, or yarn.

See Upgrade Status for the status of React 19 support for each package.

React 19 is now rc and is tested and supported in the latest Next.js 15 release.

To support React 19, package maintainers will need to test and update their packages to include React 19 as a peer dependency. This is already in progress.

You can check if a package lists React 19 as a peer dependency by running npm info <package> peerDependencies.

In the meantime, if you are installing a package that does not list React 19 as a peer dependency, you will see an error message like this:

Note: This is npm only. PNPM and Bun will only show a silent warning.

You can force install a package with the --force or the --legacy-peer-deps flag.

This will install the package and ignore the peer dependency warnings.

What do the --force and --legacy-peer-deps flag do?

You can downgrade react and react-dom to version 18, which is compatible with the package you are installing and upgrade when the dependency is updated.

Whichever solution you choose, make sure you test your app thoroughly to ensure there are no regressions.

Follow the instructions in the installation guide to install shadcn/ui. No flags are needed.

When you run npx shadcn@latest init -d, you will be prompted to select an option to resolve the peer dependency issues.

You can then run the command with the flag you choose.

The process for adding compo

*[Content truncated - see full docs]*

**Examples**:

```text
"peerDependencies": {
-  "react": "^16.8 || ^17.0 || ^18.0",
+  "react": "^16.8 || ^17.0 || ^18.0 || ^19.0",
-  "react-dom": "^16.8 || ^17.0 || ^18.0"
+  "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0"
},
```

```text
npm error code ERESOLVE
npm error ERESOLVE unable to resolve dependency tree
npm error
npm error While resolving: my-app@0.1.0
npm error Found: react@19.0.0-rc-69d4b800-20241021
npm error node_modules/react
npm error   react@"19.0.0-rc-69d4b800-20241021" from the root project
```

```text
npm i <package> --force
 
npm i <package> --legacy-peer-deps
```

---

## registry-item.json - shadcn/ui

**URL**: https://ui.shadcn.com/docs/registry/registry-item-json

**Contents**:
- registry-item.json
- Definitions
  - $schema
  - name
  - title
  - description
  - type
  - author

Specification for registry items.

The registry-item.json schema is used to define your custom registry items.

You can see the JSON Schema for registry-item.json here.

The $schema property is used to specify the schema for the registry-item.json file.

The name of the item. This is used to identify the item in the registry. It should be unique for your registry.

A human-readable title for your registry item. Keep it short and descriptive.

A description of your registry item. This can be longer and more detailed than the title.

The type property is used to specify the type of your registry item. This is used to determine the type and target path of the item when resolved for a project.

The following types are supported:

The author property is used to specify the author of the registry item.

It can be unique to the registry item or the same as the author of the registry.

The dependencies property is used to specify the dependencies of your registry item. This is for npm packages.

Use @version to specify the version of your registry item.

Used for registry dependencies. Can be names, namespaced or URLs.

Note: The CLI will automatically resolve remote registry dependencies.

The files property is used to specify the files of your registry item. Each file has a path, type and target (optional) property.

The target property is required for registry:page and registry:file types.

The path property is used to specify the path to the file in your registry. This path is used by the build script to parse, transform and build the registry JSON payload.

The type property is used to specify the type of the file. See the type section for more information.

The target property is used to indicate where the file should be placed in a project. This is optional and only required for registry:page and registry:file types.

By default, the shadcn cli will read a project's components.json file to determine the target path. For some files, such as routes or config you can sp

*[Content truncated - see full docs]*

**Examples**:

```typescript
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "hello-world",
  "type": "registry:block",
  "title": "Hello World",
  "description": "A simple hello world component.",
  "registryDependencies": [
    "button",
    "@acme/input-form",
    "https://example.com/r/foo"
  ],
  "dependencies": ["is-even@3.0.0", "motion"],
  "files": [
    {
      "path": "registry/new-york/hello-world/hello-world.tsx",
      "type": "registry:component"
    },
    {
      "path": "registry
...
```

```text
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json"
}
```

```text
{
  "name": "hello-world"
}
```

---

## registry.json - shadcn/ui

**URL**: https://ui.shadcn.com/docs/registry/registry-json

**Contents**:
- registry.json
- Definitions
  - $schema
  - name
  - homepage
  - items

Schema for running your own component registry.

The registry.json schema is used to define your custom component registry.

You can see the JSON Schema for registry.json here.

The $schema property is used to specify the schema for the registry.json file.

The name property is used to specify the name of your registry. This is used for data attributes and other metadata.

The homepage of your registry. This is used for data attributes and other metadata.

The items in your registry. Each item must implement the registry-item schema specification.

See the registry-item schema documentation for more information.

**Examples**:

```typescript
{
  "$schema": "https://ui.shadcn.com/schema/registry.json",
  "name": "shadcn",
  "homepage": "https://ui.shadcn.com",
  "items": [
    {
      "name": "hello-world",
      "type": "registry:block",
      "title": "Hello World",
      "description": "A simple hello world component.",
      "registryDependencies": [
        "button",
        "@acme/input-form",
        "https://example.com/r/foo"
      ],
      "dependencies": ["is-even@3.0.0", "motion"],
      "files": [
        {
          "pa
...
```

```text
{
  "$schema": "https://ui.shadcn.com/schema/registry.json"
}
```

```text
{
  "name": "acme"
}
```

---
