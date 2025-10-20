---
description: Beautiful and accessible component library built with Radix UI and Tailwind CSS
---

# ShadCN/UI

**Purpose**: Production-ready component library built on Radix UI primitives and Tailwind CSS for building accessible, customizable interfaces

## When to Use This Skill

Use this skill when:
- Installing ShadCN components into your project
- Building forms, tables, or data displays
- Implementing dialogs, modals, or dropdowns
- Styling components with Tailwind utilities
- Configuring theming and dark mode
- Setting up ShadCN in different frameworks (Next.js, Vite, Astro, etc.)
- Learning ShadCN best practices and patterns

**Keywords**: shadcn, shadcn/ui, components, button, card, form, input, dialog, table, accessible, radix ui

## Quick Reference

### Installation

**Quick Start:**
```bash
# Initialize shadcn in your project
npx shadcn-ui@latest init

# Add a component
npx shadcn-ui@latest add button
npx shadcn-ui@latest add card input form
```

**Framework Setup:**
- **Next.js**: `npx shadcn-ui@latest init`
- **Vite + React**: `npx shadcn-ui@latest init`
- **Astro**: `npx shadcn-ui@latest init`
- **Remix**: `npx shadcn-ui@latest init`

### Basic Button Component

```jsx
import { Button } from "@/components/ui/button"

export function MyButton() {
  return (
    <Button onClick={() => alert("Clicked!")}>
      Click Me
    </Button>
  )
}
```

### Button Variants

```jsx
import { Button } from "@/components/ui/button"

export function ButtonVariants() {
  return (
    <div className="flex gap-2 flex-wrap">
      <Button>Default</Button>
      <Button variant="secondary">Secondary</Button>
      <Button variant="destructive">Destructive</Button>
      <Button variant="outline">Outline</Button>
      <Button variant="ghost">Ghost</Button>
      <Button disabled>Disabled</Button>
      <Button size="sm">Small</Button>
      <Button size="lg">Large</Button>
    </div>
  )
}
```

### Card Component with Content

```jsx
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"

export function MyCard() {
  return (
    <Card className="w-full max-w-md">
      <CardHeader>
        <CardTitle>Card Title</CardTitle>
        <CardDescription>Card description goes here</CardDescription>
      </CardHeader>
      <CardContent>
        <p className="text-sm text-gray-600 dark:text-gray-400">
          This is the card content area.
        </p>
        <Button className="mt-4">Action</Button>
      </CardContent>
    </Card>
  )
}
```

### Form with Inputs

```jsx
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Button } from "@/components/ui/button"

export function MyForm() {
  return (
    <form className="space-y-4 max-w-md">
      <div className="space-y-2">
        <Label htmlFor="email">Email</Label>
        <Input id="email" type="email" placeholder="Enter your email" />
      </div>
      
      <div className="space-y-2">
        <Label htmlFor="password">Password</Label>
        <Input id="password" type="password" placeholder="Enter your password" />
      </div>
      
      <Button type="submit" className="w-full">
        Sign In
      </Button>
    </form>
  )
}
```

### Dialog/Modal Component

```jsx
import { Button } from "@/components/ui/button"
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"

export function MyDialog() {
  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button>Open Dialog</Button>
      </DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Confirm Action</DialogTitle>
          <DialogDescription>
            Are you sure you want to proceed with this action?
          </DialogDescription>
        </DialogHeader>
        <div className="flex gap-2 justify-end">
          <Button variant="outline">Cancel</Button>
          <Button>Confirm</Button>
        </div>
      </DialogContent>
    </Dialog>
  )
}
```

### Dropdown Menu

```jsx
import { Button } from "@/components/ui/button"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"

export function MyDropdown() {
  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button variant="outline">Menu</Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent>
        <DropdownMenuItem>Profile</DropdownMenuItem>
        <DropdownMenuItem>Settings</DropdownMenuItem>
        <DropdownMenuSeparator />
        <DropdownMenuItem className="text-red-600">Logout</DropdownMenuItem>
      </DropdownMenuContent>
    </DropdownMenu>
  )
}
```

### Select Component

```jsx
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"

export function MySelect() {
  return (
    <Select>
      <SelectTrigger className="w-48">
        <SelectValue placeholder="Choose an option" />
      </SelectTrigger>
      <SelectContent>
        <SelectItem value="option1">Option 1</SelectItem>
        <SelectItem value="option2">Option 2</SelectItem>
        <SelectItem value="option3">Option 3</SelectItem>
      </SelectContent>
    </Select>
  )
}
```

### Data Table

```jsx
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"

export function MyTable() {
  const data = [
    { id: 1, name: "John", email: "john@example.com" },
    { id: 2, name: "Jane", email: "jane@example.com" },
    { id: 3, name: "Bob", email: "bob@example.com" },
  ]

  return (
    <Table>
      <TableHeader>
        <TableRow>
          <TableHead>Name</TableHead>
          <TableHead>Email</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        {data.map((row) => (
          <TableRow key={row.id}>
            <TableCell>{row.name}</TableCell>
            <TableCell>{row.email}</TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  )
}
```

### Dark Mode Support

```jsx
import { useTheme } from "next-themes"
import { Button } from "@/components/ui/button"
import { Moon, Sun } from "lucide-react"

export function ThemeToggle() {
  const { theme, setTheme } = useTheme()

  return (
    <Button
      variant="outline"
      size="icon"
      onClick={() => setTheme(theme === "dark" ? "light" : "dark")}
    >
      <Sun className="h-4 w-4 rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0" />
      <Moon className="absolute h-4 w-4 rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100" />
      <span className="sr-only">Toggle theme</span>
    </Button>
  )
}
```

## Component Categories

### Basic Components (14)
Accordion, Alert, Badge, Button, Card, Checkbox, Label, Radio Group, Select, Separator, Switch, Tabs, Toggle, Tooltip

### Input Components (8)
Input, Textarea, Combobox, Date Picker, Input OTP, Search, Slider, Progress

### Display Components (7)
Avatar, Empty State, Spinner, Skeleton, Alert Dialog, Status Badge, Typography

### Layout Components (6)
Scroll Area, Resizable, Sheet, Drawer, Sidebar, Container

### Form Components (10+)
Form, Form Builder, React Hook Form integration, Form Validation, Error Handling, Success Messages

### Overlay Components (8)
Dialog, Popover, Hover Card, Context Menu, Dropdown Menu, Command Palette, Toast, Notification

### Data Display (5)
Table, Data Table (complex), Tree View, Breadcrumb, Pagination

### Navigation (6)
Navigation Menu, Tabs, Breadcrumb, Sidebar Navigation, Top Navigation, Mobile Menu

## Installation by Framework

- **Next.js App Router** - Full support, recommended
- **Next.js Pages Router** - Full support
- **Vite + React** - Full support
- **Astro** - Full support with JSX/TSX
- **Remix** - Full support
- **Laravel** - Full support with Blade
- **Gatsby** - Full support
- **React Router** - Full support
- **TanStack Router** - Full support
- **TanStack Start** - Full support
- **Create React App** - Full support
- **Expo** - Supported via React Native Web
- **Manual Setup** - Available for custom setups

## Configuration

### components.json

```json
{
  "style": "default",
  "tailwind": {
    "config": "tailwind.config.js",
    "css": "src/app/globals.css",
    "baseColor": "slate",
    "cssVariables": true
  },
  "rsc": true,
  "tsx": true,
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils"
  }
}
```

## File Types & Auto-Load

**When editing**: `**/*.tsx`, `**/*.jsx`, `**/components.json`, `**/tailwind.config.*`

This context is automatically loaded when working with ShadCN-related files.

## How to Load This Skill

1. **Core Reference**: Start with this skill prompt for quick component lookups and patterns
2. **For component details**: Read `.github/copilot-skills/ui/shadcn/references/components.md` for all 66 components
3. **For installation**: Check `.github/copilot-skills/ui/shadcn/references/installation.md` for framework-specific setup
4. **For theming**: See `.github/copilot-skills/ui/shadcn/references/theming.md` for dark mode and customization
5. **For CLI**: Reference `.github/copilot-skills/ui/shadcn/references/cli.md` for CLI commands

## Related Skills

- **`/tailwind`** - Tailwind CSS utilities for styling components
- **`/react`** - React patterns and best practices
- **`/nextjs`** - Next.js specific setup and patterns
- **`/radix-ui`** - Radix UI primitives (underlying component library)

## Resources

- **Official Docs**: https://ui.shadcn.com/
- **GitHub**: https://github.com/shadcn-ui/ui
- **Component Registry**: https://ui.shadcn.com/docs/components
- **Themes & Colors**: https://ui.shadcn.com/themes
- **CLI Documentation**: https://ui.shadcn.com/docs/cli
