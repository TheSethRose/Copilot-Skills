# Tailwind CSS v4 Skill

A comprehensive Copilot skill for Tailwind CSS v4 — the utility-first CSS framework for rapidly building modern designs with zero runtime.

## What's Included

This skill provides everything needed to effectively use Tailwind CSS v4:

- **Skill Prompt** (`.github/prompts/tailwind.skill.prompt.md`) - Quick reference and core concepts
- **Auto-Load Instructions** (`.github/instructions/tailwind.instructions.md`) - Triggered when editing CSS/JSX/TSX files
- **Patterns Guide** (`patterns.md`) - Real-world code examples and best practices
- **Complete Reference** (`reference.md`) - All utilities organized by category with full documentation

## Quick Start

### Installation

**Vite:**
```bash
npm install tailwindcss @tailwindcss/vite
```

**PostCSS:**
```bash
npm install tailwindcss @tailwindcss/postcss postcss
```

**CLI:**
```bash
npm install tailwindcss @tailwindcss/cli
```

### Basic Setup

```css
/* style.css */
@import "tailwindcss";
```

```html
<!-- Use utility classes directly -->
<div class="flex items-center justify-between gap-4 p-6 bg-white rounded-lg shadow-md">
  <h1 class="text-2xl font-bold text-gray-900">Hello Tailwind</h1>
  <button class="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded">
    Click me
  </button>
</div>
```

## Key Concepts

### Utility-First
Instead of writing custom CSS, compose designs from pre-built utility classes:
```html
<!-- Good ✓ -->
<div class="flex items-center gap-2">
  <img class="w-10 h-10 rounded-full" src="..." />
  <div>
    <p class="font-bold">Name</p>
    <p class="text-sm text-gray-600">Role</p>
  </div>
</div>

<!-- Avoid ✗ -->
<div class="user-card">...</div>
<style>
  .user-card { /* lots of custom CSS */ }
</style>
```

### Responsive First (Mobile-First)
Design for mobile first, then override at larger breakpoints:
```html
<!-- 1 column on mobile, 2 on md, 3 on lg -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
  {/* items */}
</div>
```

### Dark Mode Support
Easy dark mode with `dark:` variants:
```html
<div class="bg-white dark:bg-gray-900 text-black dark:text-white">
  Content automatically adapts
</div>
```

### CSS-First Configuration
v4 uses CSS variables instead of JavaScript config:
```css
@import "tailwindcss";

@theme {
  --color-brand: #3b82f6;
  --radius-card: 0.75rem;
}
```

## File Organization

```
.github/
├── prompts/
│   └── tailwind.skill.prompt.md          # Load with /tailwind command
├── instructions/
│   └── tailwind.instructions.md          # Auto-loads on CSS/JSX/TSX files
└── copilot-skills/
    └── frontend/
        └── tailwind-v4/
            ├── README.md                 # This file
            ├── patterns.md               # Code examples & best practices
            └── reference.md              # Complete utility reference
```

## When This Skill Auto-Activates

The skill instructions are automatically loaded when editing:
- `*.css` files
- `*.jsx` files
- `*.tsx` files
- `*.html` files
- `tailwind.config.*` files
- Any files containing CSS or HTML styling

## Common Tasks

### Build a Card Component
See `patterns.md` → "Card Component" for a complete example with proper spacing, shadows, dark mode support, and interactive states.

### Create Responsive Grid
See `patterns.md` → "Responsive Grid" for mobile-first grid patterns.

### Set Up Dark Mode
See `reference.md` → "Dark Mode" section for configuration and usage patterns.

### Customize Theme
See `reference.md` → "Customization" for theme variable setup and examples.

### Migrate from v3
See `reference.md` → "Migration from v3 to v4" for breaking changes and update guide.

## Best Practices

### ✅ Do
- **Mobile-first**: Use unprefixed utilities for mobile, add breakpoint prefixes for larger screens
- **Semantic colors**: Use color names like `text-gray-700`, not arbitrary hex values
- **Consistent spacing**: Use the default spacing scale (4px = 1 unit)
- **Dark mode variants**: Apply `dark:` prefix to all text/background colors
- **Responsive prefixes**: Always consider mobile, tablet, and desktop layouts
- **Composition**: Build components from utilities rather than custom CSS

### ❌ Don't
- **Avoid inline styles**: Use utilities instead of `style="..."`
- **Don't memorize**: Reference this guide instead of guessing class names
- **Avoid over-customization**: Stick to theme defaults for consistency
- **Don't skip dark mode**: Add dark mode support from the start
- **Avoid arbitrary values**: Use theme-based values when possible
- **Don't create wrapper classes**: Compose utilities directly in markup

## Version Info

- **Framework Version**: Tailwind CSS v4.1
- **Requires**: Node.js 18+
- **Browser Support**: Safari 16.4+, Chrome 111+, Firefox 128+

## Resources

- **Official Docs**: https://tailwindcss.com/docs
- **Play Editor**: https://play.tailwindcss.com/
- **UI Components**: https://tailwindcss.com/plus/ui-blocks
- **Prettier Plugin**: https://github.com/tailwindlabs/prettier-plugin-tailwindcss

## Related Skills

- `/react` - Building React components
- `/nextjs` - Next.js framework guide
- `/vue` - Vue.js framework guide
- `/shadcn` - shadcn/ui component library (built with Tailwind)

## Skill Metadata

- **Name**: Tailwind CSS v4
- **Category**: UI/Styling
- **Keywords**: tailwind, css, utilities, responsive design, dark mode, framework
- **Auto-Load**: `**/*.{css,jsx,tsx,html}, **/tailwind.config.*`
- **Constitutional Principle**: Progressive Disclosure (metadata → prompt → details → reference)

