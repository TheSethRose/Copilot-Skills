# Shadcn - Theming

**Pages**: 6

---

## Astro - shadcn/ui

**URL**: https://ui.shadcn.com/docs/dark-mode/astro

**Contents**:
- Astro
- Create an inline theme script
- Add a mode toggle
- Display the mode toggle

Adding dark mode to your astro app.

Place a mode toggle on your site to toggle between light and dark mode.

**Examples**:

```javascript
---
import '../styles/globals.css'
---
 
<script is:inline>
	const getThemePreference = () => {
		if (typeof localStorage !== 'undefined' && localStorage.getItem('theme')) {
			return localStorage.getItem('theme');
		}
		return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
	};
	const isDark = getThemePreference() === 'dark';
	document.documentElement.classList[isDark ? 'add' : 'remove']('dark');
 
	if (typeof localStorage !== 'undefined') {
		const observer = new 
...
```

```python
import * as React from "react"
import { Moon, Sun } from "lucide-react"
 
import { Button } from "@/components/ui/button"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
 
export function ModeToggle() {
  const [theme, setThemeState] = React.useState<
    "theme-light" | "dark" | "system"
  >("theme-light")
 
  React.useEffect(() => {
    const isDarkMode = document.documentElement.classList.contains("dark")
    se
...
```

```python
---
import '../styles/globals.css'
import { ModeToggle } from '@/components/ModeToggle';
---
 
<!-- Inline script -->
 
<html lang="en">
	<body>
      <h1>Astro</h1>
      <ModeToggle client:load />
	</body>
</html>
```

---

## Dark Mode - shadcn/ui

**URL**: https://ui.shadcn.com/docs/dark-mode

**Contents**:
- Dark Mode

Adding dark mode to your site.

---

## Next.js - shadcn/ui

**URL**: https://ui.shadcn.com/docs/dark-mode/next

**Contents**:
- Next.js
- Install next-themes
- Create a theme provider
- Wrap your root layout
- Add a mode toggle

Adding dark mode to your next app.

Start by installing next-themes:

Add the ThemeProvider to your root layout and add the suppressHydrationWarning prop to the html tag.

Place a mode toggle on your site to toggle between light and dark mode.

**Examples**:

```text
pnpm add next-themes
```

```python
"use client"
 
import * as React from "react"
import { ThemeProvider as NextThemesProvider } from "next-themes"
 
export function ThemeProvider({
  children,
  ...props
}: React.ComponentProps<typeof NextThemesProvider>) {
  return <NextThemesProvider {...props}>{children}</NextThemesProvider>
}
```

```python
import { ThemeProvider } from "@/components/theme-provider"
 
export default function RootLayout({ children }: RootLayoutProps) {
  return (
    <>
      <html lang="en" suppressHydrationWarning>
        <head />
        <body>
          <ThemeProvider
            attribute="class"
            defaultTheme="system"
            enableSystem
            disableTransitionOnChange
          >
            {children}
          </ThemeProvider>
        </body>
      </html>
    </>
  )
}
```

---

## Remix - shadcn/ui

**URL**: https://ui.shadcn.com/docs/dark-mode/remix

**Contents**:
- Remix
- Modify your tailwind.css file
- Install remix-themes
- Create a session storage and theme session resolver
- Set up Remix Themes
- Add an action route
- Add a mode toggle

Adding dark mode to your remix app.

Add :root[class~="dark"] to your tailwind.css file. This will allow you to use the dark class on your html element to apply dark mode styles.

Start by installing remix-themes:

Add the ThemeProvider to your root layout.

Create a file in /routes/action.set-theme.ts. Ensure that you pass the filename to the ThemeProvider component. This route it's used to store the preferred theme in the session storage when the user changes it.

Place a mode toggle on your site to toggle between light and dark mode.

**Examples**:

```text
.dark,
:root[class~="dark"] {
  ...;
}
```

```text
pnpm add remix-themes
```

```python
import { createThemeSessionResolver } from "remix-themes"
 
// You can default to 'development' if process.env.NODE_ENV is not set
const isProduction = process.env.NODE_ENV === "production"
 
const sessionStorage = createCookieSessionStorage({
  cookie: {
    name: "theme",
    path: "/",
    httpOnly: true,
    sameSite: "lax",
    secrets: ["s3cr3t"],
    // Set domain and secure only if in production
    ...(isProduction
      ? { domain: "your-production-domain.com", secure: true }
      : {
...
```

---

## Theming - shadcn/ui

**URL**: https://ui.shadcn.com/docs/theming

**Contents**:
- Theming
- CSS Variables
- Utility classes
- Convention
- List of variables
- Adding new colors
- Other color formats
- Base Colors

Using CSS Variables and color utilities for theming.

You can choose between using CSS variables (recommended) or utility classes for theming.

To use CSS variables for theming set tailwind.cssVariables to true in your components.json file.

To use utility classes for theming set tailwind.cssVariables to false in your components.json file.

We use a simple background and foreground convention for colors. The background variable is used for the background color of the component and the foreground variable is used for the text color.

The background suffix is omitted when the variable is used for the background color of the component.

Given the following CSS variables:

The background color of the following component will be var(--primary) and the foreground color will be var(--primary-foreground).

Here's the list of variables available for customization:

To add new colors, you need to add them to your CSS file and to your tailwind.config.js file.

You can now use the warning utility class in your components.

See the Tailwind CSS documentation for more information on using colors in Tailwind CSS.

For reference, here's a list of the base colors that are available.

**Examples**:

```text
<div className="bg-background text-foreground" />
```

```text
{
  "style": "default",
  "rsc": true,
  "tailwind": {
    "config": "",
    "css": "app/globals.css",
    "baseColor": "neutral",
    "cssVariables": true
  },
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils",
    "ui": "@/components/ui",
    "lib": "@/lib",
    "hooks": "@/hooks"
  },
  "iconLibrary": "lucide"
}
```

```text
<div className="bg-zinc-950 dark:bg-white" />
```

---

## Vite - shadcn/ui

**URL**: https://ui.shadcn.com/docs/dark-mode/vite

**Contents**:
- Vite
- Create a theme provider
- Wrap your root layout
- Add a mode toggle

Adding dark mode to your vite app.

Add the ThemeProvider to your root layout.

Place a mode toggle on your site to toggle between light and dark mode.

**Examples**:

```python
import { createContext, useContext, useEffect, useState } from "react"
 
type Theme = "dark" | "light" | "system"
 
type ThemeProviderProps = {
  children: React.ReactNode
  defaultTheme?: Theme
  storageKey?: string
}
 
type ThemeProviderState = {
  theme: Theme
  setTheme: (theme: Theme) => void
}
 
const initialState: ThemeProviderState = {
  theme: "system",
  setTheme: () => null,
}
 
const ThemeProviderContext = createContext<ThemeProviderState>(initialState)
 
export function ThemeProvide
...
```

```python
import { ThemeProvider } from "@/components/theme-provider"
 
function App() {
  return (
    <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
      {children}
    </ThemeProvider>
  )
}
 
export default App
```

```python
import { Moon, Sun } from "lucide-react"
 
import { Button } from "@/components/ui/button"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import { useTheme } from "@/components/theme-provider"
 
export function ModeToggle() {
  const { setTheme } = useTheme()
 
  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button variant="outline" size="icon">
          <Sun className="h-[1.2rem] w-[1.
...
```

---
