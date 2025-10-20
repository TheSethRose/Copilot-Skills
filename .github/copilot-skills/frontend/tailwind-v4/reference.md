# Tailwind CSS v4 - Complete Reference Guide

## Navigation

- **Getting Started**: Installation, setup guides, framework integration
- **Core Concepts**: Utility classes, responsive design, dark mode, variants
- **Layout**: Display, flexbox, grid, positioning, sizing
- **Spacing**: Margin, padding, gap utilities
- **Typography**: Font size, weight, color, text styling
- **Backgrounds**: Colors, gradients, images
- **Borders**: Radius, width, color, styles
- **Effects**: Shadows, opacity, filters
- **Transitions & Transforms**: Animation, transitions, transforms

---

## Installation & Setup

### Quick Start - Vite
```bash
npm create vite@latest my-app
npm install tailwindcss @tailwindcss/vite
```

```typescript
// vite.config.ts
import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [tailwindcss()]
})
```

```css
/* style.css */
@import "tailwindcss";
```

### PostCSS Setup
```bash
npm install tailwindcss @tailwindcss/postcss postcss
```

```javascript
// postcss.config.mjs
export default {
  plugins: {
    "@tailwindcss/postcss": {}
  }
}
```

### Tailwind CLI
```bash
npm install tailwindcss @tailwindcss/cli
npx @tailwindcss/cli -i input.css -o output.css --watch
```

---

## Layout Utilities

### Display
- `block` - `display: block`
- `inline` - `display: inline`
- `inline-block` - `display: inline-block`
- `flex` - `display: flex`
- `inline-flex` - `display: inline-flex`
- `grid` - `display: grid`
- `inline-grid` - `display: inline-grid`
- `hidden` - `display: none`

### Flexbox Properties
- `flex-row`, `flex-col` - direction
- `flex-wrap`, `flex-nowrap` - wrapping
- `justify-start`, `justify-center`, `justify-between`, `justify-around` - main axis
- `items-start`, `items-center`, `items-end`, `items-stretch` - cross axis
- `gap-*` - gap between items

### Grid
- `grid-cols-1` through `grid-cols-12` - column count
- `grid-rows-*` - row sizing
- `gap-*` - space between items
- `col-span-*`, `row-span-*` - item sizing

---

## Spacing

### Margin & Padding Scale
```
0, px, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 5, 6, 7, 8, 9, 10, 11, 12,
14, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 72, 80, 96
```

### Margin Utilities
- `m-*` - all sides
- `mx-*` - horizontal
- `my-*` - vertical
- `mt-*`, `mr-*`, `mb-*`, `ml-*` - individual sides
- `-m-*` - negative margins

### Padding Utilities
- `p-*` - all sides
- `px-*` - horizontal
- `py-*` - vertical
- `pt-*`, `pr-*`, `pb-*`, `pl-*` - individual sides

### Gap (Flexbox & Grid)
- `gap-*` - all directions
- `gap-x-*` - horizontal gap
- `gap-y-*` - vertical gap

---

## Typography

### Font Size
```
text-xs, text-sm, text-base, text-lg, text-xl,
text-2xl, text-3xl, text-4xl, text-5xl, text-6xl,
text-7xl, text-8xl, text-9xl
```

### Font Weight
```
font-thin (100)
font-extralight (200)
font-light (300)
font-normal (400)
font-medium (500)
font-semibold (600)
font-bold (700)
font-extrabold (800)
font-black (900)
```

### Text Color
- `text-*` - use color names: `text-blue-500`, `text-gray-600`, etc.
- Opacity modifier: `text-blue-500/50` (50% opacity)

### Text Alignment
- `text-left`, `text-center`, `text-right`, `text-justify`

### Line Height
- `leading-3` through `leading-10`, `leading-none`, `leading-tight`, `leading-normal`, `leading-relaxed`, `leading-loose`

### Letter Spacing
- `tracking-tighter`, `tracking-tight`, `tracking-normal`, `tracking-wide`, `tracking-wider`, `tracking-widest`

---

## Colors

### Color Palette
```
slate, gray, zinc, neutral, stone,
red, orange, amber, yellow, lime, green, emerald, teal, cyan, sky, blue, indigo, violet, purple, fuchsia, pink, rose
```

### Shades (per color)
```
50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950
```

### Examples
- `bg-blue-500` - background color
- `text-red-600` - text color
- `border-green-400` - border color
- `shadow-purple-500` - shadow color
- `from-blue-500` (gradient start)
- `to-purple-600` (gradient end)

### Opacity Modifier
- `bg-blue-500/50` - 50% opacity
- `text-gray-700/75` - 75% opacity

---

## Backgrounds

### Background Color
- `bg-*` - solid background color with color and shade

### Gradients
- `bg-linear-to-r` - left to right
- `bg-linear-to-b` - top to bottom
- `bg-radial` - radial gradient
- `bg-conic` - conic gradient

### Gradient Stops
- `from-blue-500` - start color
- `via-purple-500` - middle color (for 3-stop)
- `to-pink-500` - end color
- `from-50%`, `via-30%`, `to-90%` - precise positions

### Background Image
- `bg-[url(...)]` - custom image

---

## Borders

### Border Width
- `border` - 1px
- `border-0`, `border-2`, `border-4`, `border-8` - specific widths
- `border-t`, `border-r`, `border-b`, `border-l` - individual sides

### Border Radius
```
rounded-xs, rounded-sm, rounded-md, rounded-lg, rounded-xl,
rounded-2xl, rounded-3xl, rounded-full, rounded-none
```

### Border Color
- `border-*` - use color names like `border-blue-500`
- Opacity: `border-blue-500/50`

### Divide (Between Children)
- `divide-x-*`, `divide-y-*` - borders between child elements
- `divide-*` - color of dividers

---

## Effects

### Shadow
```
shadow-2xs, shadow-xs, shadow-sm, shadow-md, shadow-lg,
shadow-xl, shadow-2xl, shadow-none
```

### Opacity
```
opacity-0, opacity-5, opacity-10, opacity-20, ..., opacity-100
```

### Filter Effects
- `blur-sm`, `blur-md`, `blur-lg` - blur
- `brightness-50` through `brightness-200` - brightness
- `contrast-50` through `contrast-200` - contrast
- `grayscale`, `grayscale-0` - grayscale
- `invert`, `invert-0` - invert
- `saturate-50` through `saturate-200` - saturation

### Backdrop Filter
- `backdrop-blur-sm` - blur background
- `backdrop-brightness-75` - darken background
- `backdrop-opacity-50` - semi-transparent overlay

---

## Sizing

### Width
- `w-*` - width (0, px, 0.5, 1, 1.5, 2... up to 96 rem)
- `w-auto`, `w-full`, `w-screen`, `w-min`, `w-max`, `w-fit`
- `w-1/2`, `w-1/3`, `w-1/4`, `w-2/3`, `w-3/4` - fractions

### Height
- `h-*` - height (same scale as width)
- `h-auto`, `h-full`, `h-screen`, `h-min`, `h-max`, `h-fit`

### Min/Max Sizing
- `min-w-*`, `max-w-*` - min/max width
- `min-h-*`, `max-h-*` - min/max height
- `max-w-xs` through `max-w-7xl` - content containers

---

## Responsive Prefixes

| Prefix | Media Query |
|--------|-------------|
| (none) | All sizes |
| `sm:` | `@media (width >= 40rem)` |
| `md:` | `@media (width >= 48rem)` |
| `lg:` | `@media (width >= 64rem)` |
| `xl:` | `@media (width >= 80rem)` |
| `2xl:` | `@media (width >= 96rem)` |

### Container Queries
- `@container` - mark element as container
- `@sm:`, `@md:`, `@lg:` - query based on container size
- `@min-[475px]:` - custom container size

---

## Interactive States

### Hover, Focus, Active
- `hover:bg-blue-600` - on mouse hover
- `focus:ring-2` - on focus
- `active:scale-95` - on click
- `group-hover:underline` - when parent hovered
- `peer-focus:ring` - when sibling focused

### Disabled, Disabled States
- `disabled:opacity-50` - when disabled
- `disabled:cursor-not-allowed`
- `readonly:bg-gray-100` - read-only forms

### Input States
- `valid:border-green-500` - valid input
- `invalid:border-red-500` - invalid input
- `required:` - required field indicator
- `placeholder-shown:` - when placeholder visible

---

## Dark Mode

### Enabling Dark Mode
```css
/* Automatic with prefers-color-scheme */
@import "tailwindcss";

/* Or class-based */
@custom-variant dark (&:where(.dark, .dark *));
```

### Usage
- `dark:bg-gray-900` - background in dark mode
- `dark:text-white` - text color in dark mode
- `dark:hover:bg-gray-800` - dark mode hover state

---

## Customization

### Theme Variables
```css
@import "tailwindcss";

@theme {
  /* Colors */
  --color-brand: #3b82f6;
  --color-brand-light: #60a5fa;
  
  /* Spacing */
  --spacing: 0.25rem;
  
  /* Typography */
  --text-xl: 1.25rem;
  --text-xl--line-height: 1.75rem;
  
  /* Borders */
  --radius-card: 0.75rem;
  
  /* Shadows */
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1);
}
```

### Using Custom Theme Values
```html
<!-- Colors -->
<button class="bg-brand hover:bg-brand-light">
  Custom brand colors
</button>

<!-- Spacing -->
<div class="p-[calc(var(--spacing)*4)]">
  Custom spacing
</div>

<!-- Rounded -->
<card class="rounded-card">
  Custom radius
</card>
```

### Arbitrary Values
```html
<!-- One-off values (not in theme) -->
<div class="w-[343px] h-[200px]">
  Custom size not in scale
</div>

<!-- CSS variables -->
<div class="bg-(--my-color) text-[length:--my-font-size]">
  From CSS custom properties
</div>
```

---

## Migration from v3 to v4

| Feature | v3 | v4 |
|---------|----|----|
| Import | `@tailwind base;` | `@import "tailwindcss";` |
| Config | JS file | CSS `@theme` |
| Plugin | `tailwindcss` (PostCSS) | `@tailwindcss/postcss` |
| Vite | PostCSS | `@tailwindcss/vite` |
| Variables | Dot notation | CSS variable syntax |
| Shadows | `shadow-sm` | `shadow-xs` (renamed) |
| Ring | `ring` (3px) | `ring-3` (1px now) |
| CSS Variables | `bg-[--color]` | `bg-(--color)` |
| Outline | `outline-none` | `outline-hidden` |

---

## Resources

- **Official Documentation**: https://tailwindcss.com/docs
- **Components**: https://tailwindcss.com/plus/ui-blocks
- **Playground**: https://play.tailwindcss.com/
- **IntelliSense Extension**: VS Code `bradlc.vscode-tailwindcss`

