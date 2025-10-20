---
description: Utility-first CSS framework for rapidly building modern designs
---

# Tailwind CSS v4

**Purpose**: Utility-first CSS framework for building responsive, maintainable user interfaces with zero-runtime

## When to Use This Skill

Use this skill when:
- Building styled UIs with Tailwind utility classes
- Implementing responsive designs with breakpoints
- Using dark mode styling
- Customizing theme variables and colors
- Setting up Tailwind in new projects
- Migrating from Tailwind v3 to v4
- Learning Tailwind best practices

**Keywords**: tailwind, tailwind css, utility classes, responsive design, dark mode, styling, css framework

## Quick Reference

### Installation Setup

**Vite + Tailwind v4:**
```bash
npm install tailwindcss @tailwindcss/vite
```

**PostCSS + Tailwind v4:**
```bash
npm install tailwindcss @tailwindcss/postcss postcss
```

**CLI + Tailwind v4:**
```bash
npm install tailwindcss @tailwindcss/cli
npx @tailwindcss/cli -i ./src/input.css -o ./src/output.css --watch
```

### Core Concepts

1. **Utility Classes** - Single-purpose CSS classes applied directly to HTML:
```html
<button class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600">
  Submit
</button>
```

2. **Responsive Design** - Mobile-first breakpoints (sm, md, lg, xl, 2xl):
```html
<div class="flex flex-col md:flex-row lg:gap-8">
  <!-- Stacked on mobile, row on md, with gap on lg -->
</div>
```

3. **Dark Mode** - Use `dark:` prefix:
```html
<div class="bg-white dark:bg-gray-900 text-black dark:text-white">
  Content adapts to dark mode
</div>
```

4. **Variants** - Prefix utilities with conditions:
- **Hover/Focus**: `hover:bg-blue-600`, `focus:ring-2`
- **Breakpoints**: `md:text-lg`, `lg:flex-row`
- **Dark Mode**: `dark:bg-gray-900`
- **State**: `disabled:opacity-50`, `group-hover:underline`

### Common Utility Patterns

**Layout - Flexbox:**
```html
<div class="flex flex-row gap-4 items-center justify-between">
  <div class="flex-1">Item 1</div>
  <div class="flex-1">Item 2</div>
</div>
```

**Layout - Grid:**
```html
<div class="grid grid-cols-3 gap-4 md:grid-cols-4 lg:grid-cols-6">
  <!-- Responsive grid columns -->
</div>
```

**Spacing (Margin/Padding):**
```html
<div class="m-4 p-6 mx-auto my-8">
  <!-- margin: 1rem on all sides, padding: 1.5rem -->
  <!-- margin-inline: auto (centers), margin-top/bottom: 2rem -->
</div>
```

**Typography:**
```html
<h1 class="text-4xl font-bold text-gray-900 dark:text-white">
  Heading
</h1>
<p class="text-base text-gray-600 dark:text-gray-400">
  Body text with semantic colors
</p>
```

**Colors & Backgrounds:**
```html
<div class="bg-gradient-to-r from-purple-500 to-pink-500 text-white">
  <div class="bg-white/50 backdrop-blur">
    Semi-transparent with blur effect
  </div>
</div>
```

**Rounded Corners & Shadows:**
```html
<card class="rounded-lg shadow-md hover:shadow-xl transition-shadow">
  Smooth rounded card with interactive shadow
</card>
```

### v3 to v4 Breaking Changes

| v3 | v4 |
|----|----|
| `@tailwind base;` | `@import "tailwindcss";` |
| `shadow-sm` | `shadow-xs` |
| `ring` (3px) | `ring-3` (1px) |
| `bg-[--color]` | `bg-(--color)` |
| `outline-none` | `outline-hidden` |
| `postcss.config.js: tailwindcss` | `@tailwindcss/postcss` |

### Theme Customization

Define custom theme variables in your CSS:
```css
@import "tailwindcss";

@theme {
  --color-brand: #3b82f6;
  --spacing: 0.25rem;
  --text-xl: 1.25rem;
  --radius-xl: 0.75rem;
}
```

Use in markup:
```html
<button class="bg-brand rounded-xl px-4 py-2 text-xl">
  Custom themed button
</button>
```

## File Types & Auto-Load

**When editing**: `**/*.css`, `**/*.jsx`, `**/*.tsx`, `**/tailwind.config.*`

This context is automatically loaded when working with Tailwind-related files.

## How to Load This Skill

1. **Core Reference**: Start with this skill prompt for quick utility lookups
2. **For patterns**: Read `.github/copilot-skills/tailwind-v4/patterns.md` for real-world examples
3. **For detailed reference**: Check `.github/copilot-skills/tailwind-v4/reference.md` for all utilities by category
4. **For v3→v4 migration**: See `.github/copilot-skills/tailwind-v4/references/upgrade-guide.md`

## Common Workflows

### Build a Responsive Card Component
```html
<div class="max-w-sm rounded-lg bg-white shadow-md overflow-hidden">
  <img class="w-full h-48 object-cover" src="..." alt="..." />
  <div class="p-6">
    <h3 class="text-lg font-bold text-gray-900">Title</h3>
    <p class="mt-2 text-sm text-gray-600">Description</p>
    <button class="mt-4 w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600">
      Action
    </button>
  </div>
</div>
```

### Create Responsive Navigation
```html
<nav class="flex items-center justify-between p-4 bg-white shadow">
  <div class="text-xl font-bold">Logo</div>
  <div class="hidden md:flex gap-4">
    <a class="hover:text-blue-500">Home</a>
    <a class="hover:text-blue-500">About</a>
  </div>
</nav>
```

### Apply Dark Mode
```html
<html class="dark">
  <body class="bg-white dark:bg-gray-950 text-black dark:text-white">
    <!-- All dark: utilities apply when parent has class="dark" -->
  </body>
</html>
```

## Editor Setup

- **VS Code**: Install [Tailwind CSS IntelliSense](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss)
- **Prettier**: Install [prettier-plugin-tailwindcss](https://github.com/tailwindlabs/prettier-plugin-tailwindcss) for class sorting

## Resources

- **Official Docs**: https://tailwindcss.com/docs
- **Play Playground**: https://play.tailwindcss.com/
- **Component Library**: https://tailwindcss.com/plus/ui-blocks

