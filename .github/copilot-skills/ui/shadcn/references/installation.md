# Shadcn - Installation

**Pages**: 14

---

## Astro - shadcn/ui

**URL**: https://ui.shadcn.com/docs/installation/astro

**Contents**:
- Astro
  - Create project
  - Edit tsconfig.json file
  - Run the CLI
  - Add Components

Install and configure shadcn/ui for Astro

Start by creating a new Astro project:

Add the following code to the tsconfig.json file to resolve paths:

Run the shadcn init command to setup your project:

You can now start adding components to your project.

The command above will add the Button component to your project. You can then import it like this:

**Examples**:

```text
pnpm dlx create-astro@latest astro-app  --template with-tailwindcss --install --add react --git
```

```text
{
  "compilerOptions": {
    // ...
    "baseUrl": ".",
    "paths": {
      "@/*": [
        "./src/*"
      ]
    }
    // ...
  }
}
```

```text
pnpm dlx shadcn@latest init
```

---

## Combobox - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/combobox

**Contents**:
- Combobox
- Installation
- Usage
- Examples
  - Combobox
  - Popover
  - Dropdown menu
  - Responsive

Autocomplete input and command palette with a list of suggestions.

The Combobox is built using a composition of the <Popover /> and the <Command /> components.

See installation instructions for the Popover and the Command components.

featureCreate a new project

You can create a responsive combobox by using the <Popover /> on desktop and the <Drawer /> components on mobile.

**Examples**:

```python
"use client"

import * as React from "react"
import { Check, ChevronsUpDown } from "lucide-react"

import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import {
  Command,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
  CommandList,
} from "@/components/ui/command"
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover"

const frameworks = [
  {
    value: "next.js",
    label: "Next.js",
  },
  {
    value: "sveltekit
...
```

```python
"use client"
 
import * as React from "react"
import { CheckIcon, ChevronsUpDownIcon } from "lucide-react"
 
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import {
  Command,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
  CommandList,
} from "@/components/ui/command"
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover"
 
const frameworks = [
  {
    value: "next.js",
    label: "Next.js",
  },
  {
    value:
...
```

```python
"use client"

import * as React from "react"
import { Check, ChevronsUpDown } from "lucide-react"

import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import {
  Command,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
  CommandList,
} from "@/components/ui/command"
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover"

const frameworks = [
  {
    value: "next.js",
    label: "Next.js",
  },
  {
    value: "sveltekit
...
```

---

## Date Picker - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/date-picker

**Contents**:
- Date Picker
- Installation
- Usage
- Examples
  - Date of Birth Picker
  - Picker with Input
  - Date and Time Picker
  - Natural Language Picker

A date picker component with range and presets.

The Date Picker is built using a composition of the <Popover /> and the <Calendar /> components.

See installation instructions for the Popover and the Calendar components.

See the React DayPicker documentation for more information.

This component uses the chrono-node library to parse natural language dates.

**Examples**:

```python
"use client"

import * as React from "react"
import { ChevronDownIcon } from "lucide-react"

import { Button } from "@/components/ui/button"
import { Calendar } from "@/components/ui/calendar"
import { Label } from "@/components/ui/label"
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover"

export function Calendar22() {
  const [open, setOpen] = React.useState(false)
  const [date, setDate] = React.useState<Date | undefined>(undefined)

  return (
    <div c
...
```

```python
"use client"
 
import * as React from "react"
import { format } from "date-fns"
import { Calendar as CalendarIcon } from "lucide-react"
 
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import { Calendar } from "@/components/ui/calendar"
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover"
 
export function DatePickerDemo() {
  const [date, setDate] = React.useState<Date>()
 
  return (
    <Popover>
      <PopoverTrigger asChi
...
```

```python
"use client"

import * as React from "react"
import { ChevronDownIcon } from "lucide-react"

import { Button } from "@/components/ui/button"
import { Calendar } from "@/components/ui/calendar"
import { Label } from "@/components/ui/label"
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover"

export function Calendar22() {
  const [open, setOpen] = React.useState(false)
  const [date, setDate] = React.useState<Date | undefined>(undefined)

  return (
    <div c
...
```

---

## Gatsby - shadcn/ui

**URL**: https://ui.shadcn.com/docs/installation/gatsby

**Contents**:
- Gatsby
  - Create project
  - Configure your Gatsby project to use TypeScript and Tailwind CSS
  - Edit tsconfig.json file
  - Create gatsby-node.ts file
  - Run the CLI
  - Configure components.json
  - That's it

Install and configure Gatsby.

Update: We have added full support for React 19 and Tailwind v4 in the canary release. See the docs for Tailwind v4 for more information.

Start by creating a new Gatsby project using create-gatsby:

You will be asked a few questions to configure your project:

Add the following code to the tsconfig.json file to resolve paths:

Create a gatsby-node.ts file at the root of your project if it doesn’t already exist, and add the code below to the gatsby-node file so your app can resolve paths:

Run the shadcn init command to setup your project:

You will be asked a few questions to configure components.json:

You can now start adding components to your project.

The command above will add the Button component to your project. You can then import it like this:

**Examples**:

```text
npm init gatsby
```

```text
✔ What would you like to call your site?
· your-app-name
✔ What would you like to name the folder where your site will be created?
· your-app-name
✔ Will you be using JavaScript or TypeScript?
· TypeScript
✔ Will you be using a CMS?
· Choose whatever you want
✔ Would you like to install a styling system?
· Tailwind CSS
✔ Would you like to install additional features with other plugins?
· Choose whatever you want
✔ Shall we do this? (Y/n) · Yes
```

```text
{
  "compilerOptions": {
    // ...
    "baseUrl": ".",
    "paths": {
      "@/*": [
        "./src/*"
      ]
    }
    // ...
  }
}
```

---

## Getting Started - shadcn/ui

**URL**: https://ui.shadcn.com/docs/registry/getting-started

**Contents**:
- Getting Started
- Requirements
- registry.json
- Add a registry.json file
- Add a registry item
  - Create your component
  - Add your component to the registry
- Build your registry

Learn how to get setup and run your own component registry.

This guide will walk you through the process of setting up your own component registry. It assumes you already have a project with components and would like to turn it into a registry.

If you're starting a new registry project, you can use the registry template as a starting point. We have already configured it for you.

You are free to design and host your custom registry as you see fit. The only requirement is that your registry items must be valid JSON files that conform to the registry-item schema specification.

If you'd like to see an example of a registry, we have a template project for you to use as a starting point.

The registry.json is the entry point for the registry. It contains the registry's name, homepage, and defines all the items present in the registry.

Your registry must have this file (or JSON payload) present at the root of the registry endpoint. The registry endpoint is the URL where your registry is hosted.

The shadcn CLI will automatically generate this file for you when you run the build command.

Create a registry.json file in the root of your project. Your project can be a Next.js, Vite, Vue, Svelte, PHP or any other framework as long as it supports serving JSON over HTTP.

This registry.json file must conform to the registry schema specification.

Add your first component. Here's an example of a simple <HelloWorld /> component:

Note: This example places the component in the registry/new-york directory. You can place it anywhere in your project as long as you set the correct path in the registry.json file and you follow the registry/[NAME] directory structure.

To add your component to the registry, you need to add your component definition to registry.json.

You define your registry item by adding a name, type, title, description and files.

For every file you add, you must specify the path and type of the file. The path is the relative path to the file from the root of you

*[Content truncated - see full docs]*

**Examples**:

```text
{
  "$schema": "https://ui.shadcn.com/schema/registry.json",
  "name": "acme",
  "homepage": "https://acme.com",
  "items": [
    // ...
  ]
}
```

```python
import { Button } from "@/components/ui/button"
 
export function HelloWorld() {
  return <Button>Hello World</Button>
}
```

```typescript
registry
└── new-york
    └── hello-world
        └── hello-world.tsx
```

---

## Installation - shadcn/ui

**URL**: https://ui.shadcn.com/docs/installation

**Contents**:
- Installation
- Pick Your Framework

How to install dependencies and structure your app.

Start by selecting your framework of choice. Then follow the instructions to install the dependencies and structure your app. shadcn/ui is built to work with all React frameworks.

---

## Laravel - shadcn/ui

**URL**: https://ui.shadcn.com/docs/installation/laravel

**Contents**:
- Laravel
  - Create project
  - Add Components

Install and configure shadcn/ui for Laravel

Start by creating a new Laravel project with Inertia and React using the laravel installer laravel new my-app:

You can now start adding components to your project.

The command above will add the Switch component to resources/js/components/ui/switch.tsx. You can then import it like this:

**Examples**:

```text
laravel new my-app --react
```

```text
pnpm dlx shadcn@latest add switch
```

```python
import { Switch } from "@/components/ui/switch"
 
const MyPage = () => {
  return (
    <div>
      <Switch />
    </div>
  )
}
 
export default MyPage
```

---

## Manual Installation - shadcn/ui

**URL**: https://ui.shadcn.com/docs/installation/manual

**Contents**:
- Manual Installation
  - Add Tailwind CSS
  - Add dependencies
  - Configure path aliases
  - Configure styles
  - Add a cn helper
  - Create a components.json file
  - That's it

Add dependencies to your project manually.

Components are styled using Tailwind CSS. You need to install Tailwind CSS in your project.

Follow the Tailwind CSS installation instructions to get started.

Add the following dependencies to your project:

Configure the path aliases in your tsconfig.json file.

The @ alias is a preference. You can use other aliases if you want.

Add the following to your styles/globals.css file. You can learn more about using CSS variables for theming in the theming section.

Create a components.json file in the root of your project.

You can now start adding components to your project.

**Examples**:

```text
pnpm add class-variance-authority clsx tailwind-merge lucide-react tw-animate-css
```

```text
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["./*"]
    }
  }
}
```

```text
@import "tailwindcss";
@import "tw-animate-css";
 
@custom-variant dark (&:is(.dark *));
 
:root {
  --background: oklch(1 0 0);
  --foreground: oklch(0.145 0 0);
  --card: oklch(1 0 0);
  --card-foreground: oklch(0.145 0 0);
  --popover: oklch(1 0 0);
  --popover-foreground: oklch(0.145 0 0);
  --primary: oklch(0.205 0 0);
  --primary-foreground: oklch(0.985 0 0);
  --secondary: oklch(0.97 0 0);
  --secondary-foreground: oklch(0.205 0 0);
  --muted: oklch(0.97 0 0);
  --muted-foreground: oklch(
...
```

---

## Next.js - shadcn/ui

**URL**: https://ui.shadcn.com/docs/installation/next

**Contents**:
- Next.js
  - Create project
  - Add Components

Install and configure shadcn/ui for Next.js.

Run the init command to create a new Next.js project or to setup an existing one:

Choose between a Next.js project or a Monorepo.

You can now start adding components to your project.

The command above will add the Button component to your project. You can then import it like this:

**Examples**:

```text
pnpm dlx shadcn@latest init
```

```text
pnpm dlx shadcn@latest add button
```

```python
import { Button } from "@/components/ui/button"
 
export default function Home() {
  return (
    <div>
      <Button>Click me</Button>
    </div>
  )
}
```

---

## React Router - shadcn/ui

**URL**: https://ui.shadcn.com/docs/installation/react-router

**Contents**:
- React Router
  - Create project
  - Run the CLI
  - Add Components

Install and configure shadcn/ui for React Router.

Run the shadcn init command to setup your project:

You can now start adding components to your project.

The command above will add the Button component to your project. You can then import it like this:

**Examples**:

```text
pnpm dlx create-react-router@latest my-app
```

```text
pnpm dlx shadcn@latest init
```

```text
pnpm dlx shadcn@latest add button
```

---

## Remix - shadcn/ui

**URL**: https://ui.shadcn.com/docs/installation/remix

**Contents**:
- Remix
  - Create project
  - Run the CLI
  - Configure components.json
  - App structure
  - Install Tailwind CSS
  - Add tailwind.css to your app
  - That's it

Install and configure shadcn/ui for Remix.

Note: This guide is for Remix. For React Router, see the React Router guide.

Start by creating a new Remix project using create-remix:

Run the shadcn init command to setup your project:

You will be asked a few questions to configure components.json:

Note: This app structure is only a suggestion. You can place the files wherever you want.

Then we create a postcss.config.js file:

And finally we add the following to our remix.config.js file:

In your app/root.tsx file, import the tailwind.css file:

You can now start adding components to your project.

The command above will add the Button component to your project. You can then import it like this:

**Examples**:

```text
pnpm dlx create-remix@latest my-app
```

```text
pnpm dlx shadcn@latest init
```

```text
Which color would you like to use as base color? › Neutral
```

---

## TanStack Router - shadcn/ui

**URL**: https://ui.shadcn.com/docs/installation/tanstack-router

**Contents**:
- TanStack Router
  - Create project
  - Add Components

Install and configure shadcn/ui for TanStack Router.

Start by creating a new TanStack Router project:

You can now start adding components to your project.

The command above will add the Button component to your project. You can then import it like this:

**Examples**:

```text
pnpm dlx create-tsrouter-app@latest my-app --template file-router --tailwind --add-ons shadcn
```

```text
pnpm dlx shadcn@canary add button
```

```python
import { createFileRoute } from "@tanstack/react-router"
 
import { Button } from "@/components/ui/button"
 
export const Route = createFileRoute("/")({
  component: App,
})
 
function App() {
  return (
    <div>
      <Button>Click me</Button>
    </div>
  )
}
```

---

## TanStack Start - shadcn/ui

**URL**: https://ui.shadcn.com/docs/installation/tanstack

**Contents**:
- TanStack Start
  - Create project
  - Add Tailwind
  - Create postcss.config.ts
  - Create app/styles/app.css
  - Import app.css
  - Edit tsconfig.json file
  - Run the CLI

Install and configure shadcn/ui for TanStack Start.

Start by creating a new TanStack Start project by following the Build a Project from Scratch guide on the TanStack Start website.

Do not add Tailwind yet. We'll install Tailwind v4 in the next step.

Install tailwindcss and its dependencies.

Create a postcss.config.ts file at the root of your project.

Create an app.css file in the app/styles directory and import tailwindcss

Add the following code to the tsconfig.json file to resolve paths.

Run the shadcn init command to setup your project:

This will create a components.json file in the root of your project and configure CSS variables inside app/styles/app.css.

You can now start adding components to your project.

The command above will add the Button component to your project. You can then import it like this:

**Examples**:

```text
pnpm add tailwindcss @tailwindcss/postcss postcss
```

```typescript
export default {
  plugins: {
    "@tailwindcss/postcss": {},
  },
}
```

```text
@import "tailwindcss" source("../");
```

---

## Vite - shadcn/ui

**URL**: https://ui.shadcn.com/docs/installation/vite

**Contents**:
- Vite
  - Create project
  - Add Tailwind CSS
  - Edit tsconfig.json file
  - Edit tsconfig.app.json file
  - Update vite.config.ts
  - Run the CLI
  - Add Components

Install and configure shadcn/ui for Vite.

Start by creating a new React project using vite. Select the React + TypeScript template:

Replace everything in src/index.css with the following:

The current version of Vite splits TypeScript configuration into three files, two of which need to be edited. Add the baseUrl and paths properties to the compilerOptions section of the tsconfig.json and tsconfig.app.json files:

Add the following code to the tsconfig.app.json file to resolve paths, for your IDE:

Add the following code to the vite.config.ts so your app can resolve paths without error:

Run the shadcn init command to setup your project:

You will be asked a few questions to configure components.json.

You can now start adding components to your project.

The command above will add the Button component to your project. You can then import it like this:

**Examples**:

```text
pnpm create vite@latest
```

```text
pnpm add tailwindcss @tailwindcss/vite
```

```text
@import "tailwindcss";
```

---
