# Shadcn - Cli

**Pages**: 4

---

## Index - shadcn/ui

**URL**: https://ui.shadcn.com/docs/registry/registry-index

**Contents**:
- Index
- Adding a Registry
  - Requirements
  - Validation

Open Source Registry Index

The open source registry index is a list of all the open source registries that are available to use out of the box.

When you run shadcn add or shadcn search, the CLI will automatically check the registry index for the registry you are looking for and add it to your components.json file.

You can see the full list at https://ui.shadcn.com/r/registries.json.

You can submit a PR to add a registry to the index by adding it to the registries.json file.

Here's an example of how to add a registry to the index:

Here's an example of a valid registry:

At the root of the shadcn/ui project, you can run the following command to validate the registries.json file.

This will validate the registries.json file and output any errors.

Once you have submitted your PR, it will be validated and reviewed by the team.

**Examples**:

```text
{
  "@acme": "https://registry.acme.com/r/{name}.json",
  "@example": "https://example.com/r/{name}"
}
```

```typescript
{
  "$schema": "https://ui.shadcn.com/schema/registry.json",
  "name": "acme",
  "homepage": "https://acme.com",
  "items": [
    {
      "name": "login-form",
      "type": "registry:component",
      "title": "Login Form",
      "description": "A login form component.",
      "files": [
        {
          "path": "registry/new-york/auth/login-form.tsx",
          "type": "registry:component"
        }
      ]
    },
    {
      "name": "example-login-form",
      "type": "registry:component",
...
```

```text
pnpm validate:registries
```

---

## Monorepo - shadcn/ui

**URL**: https://ui.shadcn.com/docs/monorepo

**Contents**:
- Monorepo
- Getting started
  - Create a new monorepo project
  - Add components to your project
  - Importing components
- File Structure
- Requirements

Using shadcn/ui components and CLI in a monorepo.

Until now, using shadcn/ui in a monorepo was a bit of a pain. You could add components using the CLI, but you had to manage where the components were installed and manually fix import paths.

With the new monorepo support in the CLI, we've made it a lot easier to use shadcn/ui in a monorepo.

The CLI now understands the monorepo structure and will install the components, dependencies and registry dependencies to the correct paths and handle imports for you.

To create a new monorepo project, run the init command. You will be prompted to select the type of project you are creating.

Select the Next.js (Monorepo) option.

This will create a new monorepo project with two workspaces: web and ui, and Turborepo as the build system.

Everything is set up for you, so you can start adding components to your project.

Note: The monorepo uses React 19 and Tailwind CSS v4.

To add components to your project, run the add command in the path of your app.

The CLI will figure out what type of component you are adding and install the correct files to the correct path.

For example, if you run npx shadcn@canary add button, the CLI will install the button component under packages/ui and update the import path for components in apps/web.

If you run npx shadcn@canary add login-01, the CLI will install the button, label, input and card components under packages/ui and the login-form component under apps/web/components.

You can import components from the @workspace/ui package as follows:

You can also import hooks and utilities from the @workspace/ui package.

When you create a new monorepo project, the CLI will create the following file structure:

Every workspace must have a components.json file. A package.json file tells npm how to install the dependencies. A components.json file tells the CLI how and where to install components.

The components.json file must properly define aliases for the workspace. This tells the CLI how to impo

*[Content truncated - see full docs]*

**Examples**:

```text
pnpm dlx shadcn@canary init
```

```text
? Would you like to start a new project?
    Next.js
❯   Next.js (Monorepo)
```

```text
cd apps/web
```

---

## Tailwind v4 - shadcn/ui

**URL**: https://ui.shadcn.com/docs/tailwind-v4

**Contents**:
- Tailwind v4
- What's New
- Try It Out
- Upgrade Your Project
  - 1. Follow the Tailwind v4 Upgrade Guide
  - 2. Update your CSS variables
  - 3. Update colors for charts
  - 4. Use new size-* utility

How to use shadcn/ui with Tailwind v4 and React 19.

It’s here! Tailwind v4 and React 19. Ready for you to try out. You can start using it today.

Note: this is non-breaking. Your existing apps with Tailwind v3 and React 18 will still work. When you add new components, they'll still be in v3 and React 18 until you upgrade. Only new projects start with Tailwind v4 and React 19.

You can test Tailwind v4 + React 19 today using the canary release of the CLI. See the framework specific guides below for how to get started.

Important: Before upgrading, please read the Tailwind v4 Compatibility Docs and make sure your project is ready for the upgrade. Tailwind v4 uses bleeding-edge browser features and is designed for modern browsers.

One of the major advantages of using shadcn/ui is that the code you end up with is exactly what you'd write yourself. There are no hidden abstractions.

This means when a dependency has a new release, you can just follow the official upgrade paths.

Here's how to upgrade your existing projects (full docs are on the way):

The codemod will migrate your CSS variables as references under the @theme directive.

This works. But to make it easier to work with colors and other variables, we'll need to move the hsl wrappers and use @theme inline.

Here's how you do it:

This change makes it much simpler to access your theme variables in both utility classes and outside of CSS for eg. using color values in JavaScript.

Now that the theme colors come with hsl(), you can remove the wrapper in your chartConfig:

The new size-* utility (added in Tailwind v3.4), is now fully supported by tailwind-merge. You can replace w-* h-* with the new size-* utility:

You can use the remove-forward-ref codemod to migrate your forwardRef to props or manually update the primitives.

For the codemod, see https://github.com/reactjs/react-codemod#remove-forward-ref.

If you want to do it manually, here's how to do it step by step:

We've deprecated tailwindcss-animate in

*[Content truncated - see full docs]*

**Examples**:

```text
@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 0 0% 3.9%;
  }
}
 
@theme {
  --color-background: hsl(var(--background));
  --color-foreground: hsl(var(--foreground));
}
```

```text
:root {
  --background: hsl(0 0% 100%); // <-- Wrap in hsl
  --foreground: hsl(0 0% 3.9%);
}
 
.dark {
  --background: hsl(0 0% 3.9%); // <-- Wrap in hsl
  --foreground: hsl(0 0% 98%);
}
 
@theme inline {
  --color-background: var(--background); // <-- Remove hsl
  --color-foreground: var(--foreground);
}
```

```javascript
const chartConfig = {
  desktop: {
    label: "Desktop",
-    color: "hsl(var(--chart-1))",
+    color: "var(--chart-1)",
  },
  mobile: {
    label: "Mobile",
-   color: "hsl(var(--chart-2))",
+   color: "var(--chart-2)",
  },
} satisfies ChartConfig
```

---

## shadcn - shadcn/ui

**URL**: https://ui.shadcn.com/docs/cli

**Contents**:
- shadcn
- init
- add
- view
- search
- list
- build

Use the shadcn CLI to add components to your project.

Use the init command to initialize configuration and dependencies for a new project.

The init command installs dependencies, adds the cn util and configures CSS variables for the project.

Use the add command to add components and dependencies to your project.

Use the view command to view items from the registry before installing them.

You can view multiple items at once:

Or view items from namespaced registries:

Use the search command to search for items from registries.

You can search with a query:

Or search multiple registries at once:

The list command is an alias for search:

Use the list command to list all items from a registry.

Use the build command to generate the registry JSON files.

This command reads the registry.json file and generates the registry JSON files in the public/r directory.

To customize the output directory, use the --output option.

**Examples**:

```text
pnpm dlx shadcn@latest init
```

```vue
Usage: shadcn init [options] [components...]
 
initialize your project and install dependencies
 
Arguments:
  components         name, url or local path to component
 
Options:
  -t, --template <template>      the template to use. (next, next-monorepo)
  -b, --base-color <base-color>  the base color to use. (neutral, gray, zinc, stone, slate)
  -y, --yes                      skip confirmation prompt. (default: true)
  -f, --force                    force overwrite of existing configuration. (de
...
```

```text
pnpm dlx shadcn@latest add [component]
```

---
