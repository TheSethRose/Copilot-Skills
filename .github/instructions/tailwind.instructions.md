---
description: "Tailwind CSS v4 - Auto-loaded context for utility-first CSS development"
applyTo: "**/*.{css,jsx,tsx,html}, **/tailwind.config.*"
---

# Tailwind CSS v4 - Automatic Context Instructions

**Related Prompt:** `/tailwind`  
**Related Skill:** `.github/copilot-skills/frontend/tailwind-v4/`

**Triggers:** tailwind, css utilities, responsive design, dark mode, styling, breakpoint, hover state

## Context: Utility-First CSS Framework

When working with Tailwind CSS files or styling with utility classes, this context is automatically activated.

## Core Principles

### Mobile-First Responsive Design
- **No prefix** = applies to all screen sizes
- **sm**, **md**, **lg**, **xl**, **2xl** = breakpoint prefixes (add at or above that size)
- **Example**: `w-1/2 md:w-1/3 lg:w-1/4` = different widths at each breakpoint
- **Default breakpoints**: sm (640px), md (768px), lg (1024px), xl (1280px), 2xl (1536px)

### Variant Stacking (Left to Right)
- **v4 change**: Variants apply left-to-right, not right-to-left
- **Hover**: `hover:bg-blue-600` applies on hover
- **Dark mode**: `dark:text-white` applies in dark mode
- **Combine**: `dark:hover:bg-blue-600` = dark mode hover state
- **Responsive**: `md:dark:hover:underline` = medium screens and up, dark mode, on hover

### CSS Variables as First-Class
- **v4 removed** `@tailwind` directives (v3: `@tailwind base;`)
- **v4 requires**: `@import "tailwindcss";`
- **Theme variables**: Access colors via `var(--color-blue-500)` in custom CSS
- **Custom properties**: Define with `@theme { --my-color: #123456; }`

## Default Behaviors

### When styling a component
1. Start with layout utilities (`flex`, `grid`, `block`, `display`)
2. Add spacing (`p-4`, `m-6`, `gap-4`)
3. Add typography (`text-lg`, `font-bold`)
4. Add colors (`bg-blue-500`, `text-gray-700`)
5. Add effects (`shadow`, `rounded-lg`)
6. Add responsive prefixes (`md:`, `lg:`)
7. Add interactive states (`hover:`, `focus:`, `dark:`)

### When using dark mode
- Add `dark:` prefix to utilities that should change: `bg-white dark:bg-gray-900`
- Dark mode uses `@media (prefers-color-scheme: dark)` by default
- Can be overridden with class-based approach: `<html class="dark">`

### When building responsive layouts
- Start with mobile view (no prefix)
- Override at breakpoints: `flex-col md:flex-row`
- Container queries: `@container md:flex-row` for component-specific sizing
- Use `gap` instead of `space-*` for better flexibility in wrapping layouts

## Quality Guidelines

### ✅ Do
- Use responsive prefixes to design mobile-first: `w-1/2 md:w-1/3 lg:w-1/4`
- Combine related utilities in class strings: `flex items-center justify-between gap-4`
- Use semantic color names: `text-gray-700`, not `text-[#374151]` (unless specific hex needed)
- Apply dark mode variants to all interactive elements: `hover:text-blue-500 dark:hover:text-blue-400`
- Use arbitrary values only for one-off, non-theme values: `text-[13px]`, `w-[343px]`
- Keep utility classes in logical order: layout → spacing → typography → colors → effects → states
- Use constrained spacing scale (`p-4`, `m-2`) instead of arbitrary values when possible
- Apply variants intelligently for better specificity: `group-hover:underline`, `peer-focus:ring`

### ❌ Don't
- Mix breakpoint logic in class attributes - use responsive prefixes instead
- Override utilities with custom CSS when a utility exists
- Use arbitrary values for theme values that should be customized: use `@theme` instead
- Apply `hover:` to mobile-only interactions (they won't work on touch)
- Forget dark mode variants on text/background colors
- Mix `space-x-` with `gap` - use `gap` for better layout control
- Chain multiple inline styles when utilities can do it: `class="..."` not `style="..."`

## Common Patterns

### Flex Container Layout
```html
<!-- Flex row, center vertically, space between horizontally -->
<div class="flex items-center justify-between gap-4">
  <div>Left content</div>
  <div>Right content</div>
</div>

<!-- Flex column on mobile, row on medium screens -->
<div class="flex flex-col md:flex-row gap-4">
  <div class="md:flex-1">Item 1</div>
  <div class="md:flex-1">Item 2</div>
</div>
```

### Grid Layout
```html
<!-- 3 columns on desktop, 2 on tablet, 1 on mobile -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
  <!-- Grid items -->
</div>
```

### Typography Hierarchy
```html
<h1 class="text-4xl md:text-5xl font-bold text-gray-900 dark:text-white">
  Heading
</h1>
<p class="text-base md:text-lg text-gray-600 dark:text-gray-400 leading-relaxed">
  Body text with proper line height
</p>
<small class="text-sm text-gray-500 dark:text-gray-500">
  Supporting text
</small>
```

### Card Component
```html
<div class="rounded-lg bg-white dark:bg-gray-800 shadow-md hover:shadow-lg transition-shadow p-6">
  <h3 class="text-lg font-semibold text-gray-900 dark:text-white">
    Card Title
  </h3>
  <p class="mt-2 text-gray-600 dark:text-gray-400">
    Card description
  </p>
  <button class="mt-4 bg-blue-500 hover:bg-blue-600 text-white rounded px-4 py-2">
    Action
  </button>
</div>
```

### Interactive State Management
```html
<!-- Button with interactive states -->
<button class="
  bg-blue-500 hover:bg-blue-600 active:bg-blue-700
  disabled:opacity-50 disabled:cursor-not-allowed
  text-white font-medium py-2 px-4 rounded
  transition-colors
">
  Click me
</button>

<!-- Link with group hover -->
<a href="#" class="group flex items-center gap-2">
  <span class="group-hover:underline">Link text</span>
  <svg class="opacity-0 group-hover:opacity-100 transition-opacity">
    <!-- icon -->
  </svg>
</a>
```

## v3 to v4 Migration Notes

### Import Changes
```css
/* ❌ v3 */
@tailwind base;
@tailwind components;
@tailwind utilities;

/* ✅ v4 */
@import "tailwindcss";
```

### Config Migration
```javascript
/* ❌ v3: tailwind.config.js */
module.exports = {
  theme: {
    extend: {
      colors: { brand: '#3b82f6' }
    }
  }
}

/* ✅ v4: app.css */
@import "tailwindcss";
@theme {
  --color-brand: #3b82f6;
}
```

### Utility Renames
- `shadow-sm` → `shadow-xs` (and cascading rename for all shadow sizes)
- `ring` (3px) → `ring-3` (now 1px by default)
- `blur-sm` → `blur-xs` (and cascading for all blur utilities)
- `outline-none` → `outline-hidden` (for better semantics)
- `bg-[--color]` → `bg-(--color)` (cleaner CSS variable syntax)

### Breaking Changes
- **Space-between selector changed**: `space-y-4` now uses `:not(:last-child)` instead of `~`
- **Border color defaults**: No longer defaults to `gray-200`, must specify explicitly
- **Ring styling**: Changed from `3px` to `1px`, no longer defaults to `blue-500`
- **Variants stack left-to-right**: `*:first:pt-0` not `first:*:pt-0`

## Common Workflows

### Set Up New Tailwind Project
1. Install: `npm install tailwindcss @tailwindcss/vite` (or postcss/cli variant)
2. Import in CSS: `@import "tailwindcss";`
3. Add vite plugin to config (if using Vite)
4. Start using utilities in HTML/JSX

### Customize Theme
```css
@import "tailwindcss";

@theme {
  --color-brand-50: #eff6ff;
  --color-brand-500: #3b82f6;
  --color-brand-900: #1e3a8a;
  
  --radius-card: 0.75rem;
  --radius-button: 0.5rem;
}
```

### Add Dark Mode
```css
@import "tailwindcss";

@custom-variant dark (&:where(.dark, .dark *));
```

Then use: `bg-white dark:bg-gray-900`

