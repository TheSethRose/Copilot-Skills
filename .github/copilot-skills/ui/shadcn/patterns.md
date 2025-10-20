# Shadcn - Common Patterns

Quick reference for common shadcn patterns and usage.

## Code Patterns

### 1. SectionsGet StartedComponentsRegistryMCP ServerFormsChangelogGet StartedInstallationcomponents.jsonT

```
registry.json
```

### 2. SectionsGet StartedComponentsRegistryMCP ServerFormsChangelogGet StartedInstallationcomponents.jsonT

```
registry.json
```

### 3. Getting StartedCopy PagePreviousNextLearn how to get setup and run your own component registry.This 

```
registry.json
```

### 4. Getting StartedCopy PagePreviousNextLearn how to get setup and run your own component registry.This 

```
registry.json
```

### 5. Getting StartedCopy PagePreviousNextLearn how to get setup and run your own component registry.This 

```
registry.json
```

### 6. SectionsGet StartedComponentsRegistryMCP ServerFormsChangelogGet StartedInstallationcomponents.jsonT

```
"use client"

import * as React from "react"

import { Calendar } from "@/components/ui/calendar"

export function CalendarDemo() {
  const [date, setDate] = React.useState<Date | undefined>(new Date())

  return (
    <Calendar
      mode="single"
      selected={date}
      onSelect={setDate}
    
```

### 7. SectionsGet StartedComponentsRegistryMCP ServerFormsChangelogGet StartedInstallationcomponents.jsonT

```
"use client"

import * as React from "react"

import { Calendar } from "@/components/ui/calendar"

export function CalendarDemo() {
  const [date, setDate] = React.useState<Date | undefined>(new Date())

  return (
    <Calendar
      mode="single"
      selected={date}
      onSelect={setDate}
    
```

### 8. CalendarCopy PagePreviousNextA date field component that allows users to enter and edit date.Docs Pr

```
"use client"

import * as React from "react"

import { Calendar } from "@/components/ui/calendar"

export function CalendarDemo() {
  const [date, setDate] = React.useState<Date | undefined>(new Date())

  return (
    <Calendar
      mode="single"
      selected={date}
      onSelect={setDate}
    
```

## Examples

### Example 1

```python
import { Button } from "@/components/ui/button"
 
export function HelloWorld() {
  return <Button>Hello World</Button>
}
```

### Example 2

```python
import { ArrowUpIcon } from "lucide-react"

import { Button } from "@/components/ui/button"

export function ButtonDemo() {
  return (
    <div className="flex flex-wrap items-center gap-2 md:flex-row">
      <Button variant="outline">Button</Button>
      <Button variant="outline" size="icon" aria-label="Submit">
        <ArrowUpIcon />
      </Button>
    </div>
  )
}
```

### Example 3

```python
"use client"

import * as React from "react"

import { Calendar } from "@/components/ui/calendar"

export function CalendarDemo() {
  const [date, setDate] = React.useState<Date | undefined>(new Date())

  return (
    <Calendar
      mode="single"
      selected={date}
      onSelect={setDate}
      className="rounded-md border shadow-sm"
      captionLayout="dropdown"
    />
  )
}
```

### Example 4

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

### Example 5

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

### Example 6

```python
import { Spinner } from "@/components/ui/spinner"
```

### Example 7

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


## Categories

See organized documentation in `references/`:

- `references/cli.md` - Cli
- `references/components.md` - Components
- `references/installation.md` - Installation
- `references/other.md` - Other
- `references/theming.md` - Theming
