# Shadcn - Components

**Pages**: 66

---

## Accordion - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/accordion

**Contents**:
- Accordion
  - Product Information
  - Shipping Details
  - Return Policy
- Installation
- Usage

A vertically stacked set of interactive headings that each reveal a section of content.

Our flagship product combines cutting-edge technology with sleek design. Built with premium materials, it offers unparalleled performance and reliability.

Key features include advanced processing capabilities, and an intuitive user interface designed for both beginners and experts.

**Examples**:

```python
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion"

export function AccordionDemo() {
  return (
    <Accordion
      type="single"
      collapsible
      className="w-full"
      defaultValue="item-1"
    >
      <AccordionItem value="item-1">
        <AccordionTrigger>Product Information</AccordionTrigger>
        <AccordionContent className="flex flex-col gap-4 text-balance">
          <p>
            Our flagship product combine
...
```

```text
pnpm dlx shadcn@latest add accordion
```

```python
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion"
```

---

## Alert Dialog - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/alert-dialog

**Contents**:
- Alert Dialog
- Installation
- Usage

A modal dialog that interrupts the user with important content and expects a response.

**Examples**:

```python
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "@/components/ui/alert-dialog"
import { Button } from "@/components/ui/button"

export function AlertDialogDemo() {
  return (
    <AlertDialog>
      <AlertDialogTrigger asChild>
        <Button variant="outline">Show Dialog</Button>
      </AlertDialogTrigger>
      <AlertDialogContent>
     
...
```

```text
pnpm dlx shadcn@latest add alert-dialog
```

```python
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "@/components/ui/alert-dialog"
```

---

## Alert - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/alert

**Contents**:
- Alert
- Installation
- Usage

Displays a callout for user attention.

Please verify your billing information and try again.

**Examples**:

```python
import { AlertCircleIcon, CheckCircle2Icon, PopcornIcon } from "lucide-react"

import {
  Alert,
  AlertDescription,
  AlertTitle,
} from "@/components/ui/alert"

export function AlertDemo() {
  return (
    <div className="grid w-full max-w-xl items-start gap-4">
      <Alert>
        <CheckCircle2Icon />
        <AlertTitle>Success! Your changes have been saved</AlertTitle>
        <AlertDescription>
          This is an alert with icon, title and description.
        </AlertDescription>
     
...
```

```text
pnpm dlx shadcn@latest add alert
```

```python
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert"
```

---

## Aspect Ratio - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/aspect-ratio

**Contents**:
- Aspect Ratio
- Installation
- Usage

Displays content within a desired ratio.

**Examples**:

```python
import Image from "next/image"

import { AspectRatio } from "@/components/ui/aspect-ratio"

export function AspectRatioDemo() {
  return (
    <AspectRatio ratio={16 / 9} className="bg-muted rounded-lg">
      <Image
        src="https://images.unsplash.com/photo-1588345921523-c2dcdb7f1dcd?w=800&dpr=2&q=80"
        alt="Photo by Drew Beamer"
        fill
        className="h-full w-full rounded-lg object-cover dark:brightness-[0.2] dark:grayscale"
      />
    </AspectRatio>
  )
}
```

```text
pnpm dlx shadcn@latest add aspect-ratio
```

```python
import { AspectRatio } from "@/components/ui/aspect-ratio"
```

---

## Avatar - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/avatar

**Contents**:
- Avatar
- Installation
- Usage

An image element with a fallback for representing the user.

**Examples**:

```python
import {
  Avatar,
  AvatarFallback,
  AvatarImage,
} from "@/components/ui/avatar"

export function AvatarDemo() {
  return (
    <div className="flex flex-row flex-wrap items-center gap-12">
      <Avatar>
        <AvatarImage src="https://github.com/shadcn.png" alt="@shadcn" />
        <AvatarFallback>CN</AvatarFallback>
      </Avatar>
      <Avatar className="rounded-lg">
        <AvatarImage
          src="https://github.com/evilrabbit.png"
          alt="@evilrabbit"
        />
        <A
...
```

```text
pnpm dlx shadcn@latest add avatar
```

```python
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
```

---

## Badge - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/badge

**Contents**:
- Badge
- Installation
- Usage
  - Link

Displays a badge or a component that looks like a badge.

You can use the asChild prop to make another component look like a badge. Here's an example of a link that looks like a badge.

**Examples**:

```python
import { AlertCircleIcon, BadgeCheckIcon, CheckIcon } from "lucide-react"

import { Badge } from "@/components/ui/badge"

export function BadgeDemo() {
  return (
    <div className="flex flex-col items-center gap-2">
      <div className="flex w-full flex-wrap gap-2">
        <Badge>Badge</Badge>
        <Badge variant="secondary">Secondary</Badge>
        <Badge variant="destructive">Destructive</Badge>
        <Badge variant="outline">Outline</Badge>
      </div>
      <div className="flex w-
...
```

```text
pnpm dlx shadcn@latest add badge
```

```python
import { Badge } from "@/components/ui/badge"
```

---

## Breadcrumb - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/breadcrumb

**Contents**:
- Breadcrumb
- Installation
- Usage
- Examples
  - Custom separator
  - Dropdown
  - Collapsed
  - Link component

Displays the path to the current resource using a hierarchy of links.

Use a custom component as children for <BreadcrumbSeparator /> to create a custom separator.

You can compose <BreadcrumbItem /> with a <DropdownMenu /> to create a dropdown in the breadcrumb.

We provide a <BreadcrumbEllipsis /> component to show a collapsed state when the breadcrumb is too long.

To use a custom link component from your routing library, you can use the asChild prop on <BreadcrumbLink />.

Here's an example of a responsive breadcrumb that composes <BreadcrumbItem /> with <BreadcrumbEllipsis />, <DropdownMenu />, and <Drawer />.

It displays a dropdown on desktop and a drawer on mobile.

**Examples**:

```python
import Link from "next/link"

import {
  Breadcrumb,
  BreadcrumbEllipsis,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"

export function BreadcrumbDemo() {
  return (
    <Breadcrumb>
      <BreadcrumbList>
        <BreadcrumbItem>
          <BreadcrumbLink asChild>
            <Link
...
```

```text
pnpm dlx shadcn@latest add breadcrumb
```

```python
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"
```

---

## Button Group - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/button-group

**Contents**:
- Button Group
- Installation
- Usage
- Accessibility
- ButtonGroup vs ToggleGroup
- Examples
  - Orientation
  - Size

A container that groups related buttons together with consistent styling.

Set the orientation prop to change the button group layout.

Control the size of buttons using the size prop on individual buttons.

Nest <ButtonGroup> components to create button groups with spacing.

The ButtonGroupSeparator component visually divides buttons within a group.

Buttons with variant outline do not need a separator since they have a border. For other variants, a separator is recommended to improve the visual hierarchy.

Create a split button group by adding two buttons separated by a ButtonGroupSeparator.

Wrap an Input component with buttons.

Wrap an InputGroup component to create complex input layouts.

Create a split button group with a DropdownMenu component.

Pair with a Select component.

Use with a Popover component.

The ButtonGroup component is a container that groups related buttons together with consistent styling.

Nest multiple button groups to create complex layouts with spacing. See the nested example for more details.

The ButtonGroupSeparator component visually divides buttons within a group.

Use this component to display text within a button group.

Use the asChild prop to render a custom component as the text, for example a label.

**Examples**:

```python
"use client"

import * as React from "react"
import {
  ArchiveIcon,
  ArrowLeftIcon,
  CalendarPlusIcon,
  ClockIcon,
  ListFilterPlusIcon,
  MailCheckIcon,
  MoreHorizontalIcon,
  TagIcon,
  Trash2Icon,
} from "lucide-react"

import { Button } from "@/components/ui/button"
import { ButtonGroup } from "@/components/ui/button-group"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuGroup,
  DropdownMenuItem,
  DropdownMenuRadioGroup,
  DropdownMenuRadioItem,
  DropdownMenuSeparator,

...
```

```text
pnpm dlx shadcn@latest add button-group
```

```python
import {
  ButtonGroup,
  ButtonGroupSeparator,
  ButtonGroupText,
} from "@/components/ui/button-group"
```

---

## Button - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/button

**Contents**:
- Button
- Installation
- Usage
- Cursor
- Examples
  - Size
  - Default
  - Outline

Displays a button or a component that looks like a button.

Updated: We have updated the button component to add new sizes: icon-sm and icon-lg. See the changelog for more details. Follow the instructions to update your project.

Tailwind v4 switched from cursor: pointer to cursor: default for the button component.

If you want to keep the cursor: pointer behavior, add the following code to your CSS file:

The spacing between the icon and the text is automatically adjusted based on the size of the button. You do not need any margin on the icon.

Use the rounded-full class to make the button rounded.

To create a button group, use the ButtonGroup component. See the Button Group documentation for more details.

You can use the asChild prop to make another component look like a button. Here's an example of a link that looks like a button.

The Button component is a wrapper around the button element that adds a variety of styles and functionality.

We have added two new sizes to the button component: icon-sm and icon-lg. These sizes are used to create icon buttons. To add them, edit button.tsx and add the following code under size in buttonVariants:

**Examples**:

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

```text
<Button variant="outline">Button</Button>
<Button variant="outline" size="icon" aria-label="Submit">
  <ArrowUpIcon />
</Button>
```

```text
pnpm dlx shadcn@latest add button
```

---

## Calendar - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/calendar

**Contents**:
- Calendar
- Blocks
- Installation
- Usage
- About
- Customization
- Date Picker
- Persian / Hijri / Jalali Calendar

A date field component that allows users to enter and edit date.

We have built a collection of 30+ calendar blocks that you can use to build your own calendar components.

See all calendar blocks in the Blocks Library page.

See the React DayPicker documentation for more information.

The Calendar component is built on top of React DayPicker.

See the React DayPicker documentation for more information on how to customize the Calendar component.

You can use the <Calendar> component to build a date picker. See the Date Picker page for more information.

To use the Persian calendar, edit components/ui/calendar.tsx and replace react-day-picker with react-day-picker/persian.

This component uses the chrono-node library to parse natural language dates.

Your date of birth is used to calculate your age.

If you're already using Tailwind v4, you can upgrade to the latest version of the Calendar component by running the following command:

When you're prompted to overwrite the existing Calendar component, select Yes. If you have made any changes to the Calendar component, you will need to merge your changes with the new version.

This will update the Calendar component and react-day-picker to the latest version.

Next, follow the React DayPicker upgrade guide to upgrade your existing components to the latest version.

After upgrading the Calendar component, you can install the new blocks by running the shadcn@latest add command.

This will install the latest version of the calendar blocks.

If you're using Tailwind v3, you can upgrade to the latest version of the Calendar by copying the following code to your calendar.tsx file.

If you have made any changes to the Calendar component, you will need to merge your changes with the new version.

Then follow the React DayPicker upgrade guide to upgrade your dependencies and existing components to the latest version.

After upgrading the Calendar component, you can install the new blocks by running the shadcn@latest add command.

*[Content truncated - see full docs]*

**Examples**:

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

```text
pnpm dlx shadcn@latest add calendar
```

```python
import { Calendar } from "@/components/ui/calendar"
```

---

## Card - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/card

**Contents**:
- Card
- Installation
- Usage

Displays a card with header, content, and footer.

**Examples**:

```python
import { Button } from "@/components/ui/button"
import {
  Card,
  CardAction,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"

export function CardDemo() {
  return (
    <Card className="w-full max-w-sm">
      <CardHeader>
        <CardTitle>Login to your account</CardTitle>
        <CardDescription>
          Enter your email below to login to y
...
```

```text
pnpm dlx shadcn@latest add card
```

```python
import {
  Card,
  CardAction,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
```

---

## Carousel - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/carousel

**Contents**:
- Carousel
- About
- Installation
- Usage
- Examples
  - Sizes
  - Spacing
  - Orientation

A carousel with motion and swipe built using Embla.

The carousel component is built using the Embla Carousel library.

To set the size of the items, you can use the basis utility class on the <CarouselItem />.

To set the spacing between the items, we use a pl-[VALUE] utility on the <CarouselItem /> and a negative -ml-[VALUE] on the <CarouselContent />.

Why: I tried to use the gap property or a grid layout on the <CarouselContent /> but it required a lot of math and mental effort to get the spacing right. I found pl-[VALUE] and -ml-[VALUE] utilities much easier to use.

You can always adjust this in your own project if you need to.

Use the orientation prop to set the orientation of the carousel.

You can pass options to the carousel using the opts prop. See the Embla Carousel docs for more information.

Use a state and the setApi props to get an instance of the carousel API.

You can listen to events using the api instance from setApi.

See the Embla Carousel docs for more information on using events.

You can use the plugins prop to add plugins to the carousel.

See the Embla Carousel docs for more information on using plugins.

**Examples**:

```python
import * as React from "react"

import { Card, CardContent } from "@/components/ui/card"
import {
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselNext,
  CarouselPrevious,
} from "@/components/ui/carousel"

export function CarouselDemo() {
  return (
    <Carousel className="w-full max-w-xs">
      <CarouselContent>
        {Array.from({ length: 5 }).map((_, index) => (
          <CarouselItem key={index}>
            <div className="p-1">
              <Card>
                <CardConte
...
```

```text
pnpm dlx shadcn@latest add carousel
```

```python
import {
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselNext,
  CarouselPrevious,
} from "@/components/ui/carousel"
```

---

## Chart - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/chart

**Contents**:
- Chart
- Component
- Installation
  - Run the following command to install chart.tsx
  - Add the following colors to your CSS file
- Your First Chart
  - Start by defining your data
  - Define your chart config

Beautiful charts. Built using Recharts. Copy and paste into your apps.

Note: We're working on upgrading to Recharts v3. In the meantime, if you'd like to start testing v3, see the code in the comment here. We'll have an official release soon.

Introducing Charts. A collection of chart components that you can copy and paste into your apps.

Charts are designed to look great out of the box. They work well with the other components and are fully customizable to fit your project.

Browse the Charts Library.

We use Recharts under the hood.

We designed the chart component with composition in mind. You build your charts using Recharts components and only bring in custom components, such as ChartTooltip, when and where you need it.

We do not wrap Recharts. This means you're not locked into an abstraction. When a new Recharts version is released, you can follow the official upgrade path to upgrade your charts.

The components are yours.

Note: If you are using charts with React 19 or the Next.js 15, see the note here.

Let's build your first chart. We'll build a bar chart, add a grid, axis, tooltip and legend.

The following data represents the number of desktop and mobile users for each month.

Note: Your data can be in any shape. You are not limited to the shape of the data below. Use the dataKey prop to map your data to the chart.

The chart config holds configuration for the chart. This is where you place human-readable strings, such as labels, icons and color tokens for theming.

You can now build your chart using Recharts components.

Important: Remember to set a min-h-[VALUE] on the ChartContainer component. This is required for the chart be responsive.

Let's add a grid to the chart.

To add an x-axis to the chart, we'll use the XAxis component.

So far we've only used components from Recharts. They look great out of the box thanks to some customization in the chart component.

To add a tooltip, we'll use the custom ChartTooltip and ChartTooltipContent components

*[Content truncated - see full docs]*

**Examples**:

```python
"use client"

import * as React from "react"
import { Bar, BarChart, CartesianGrid, XAxis } from "recharts"

import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import {
  ChartConfig,
  ChartContainer,
  ChartTooltip,
  ChartTooltipContent,
} from "@/components/ui/chart"

export const description = "An interactive bar chart"

const chartData = [
  { date: "2024-04-01", desktop: 222, mobile: 150 },
  { date: "2024-04-02", desktop: 97, mobil
...
```

```python
import { Bar, BarChart } from "recharts"
 
import { ChartContainer, ChartTooltipContent } from "@/components/ui/charts"
 
export function MyChart() {
  return (
    <ChartContainer>
      <BarChart data={data}>
        <Bar dataKey="value" />
        <ChartTooltip content={<ChartTooltipContent />} />
      </BarChart>
    </ChartContainer>
  )
}
```

```text
pnpm dlx shadcn@latest add chart
```

---

## Checkbox - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/checkbox

**Contents**:
- Checkbox
- Installation
- Usage

A control that allows the user to toggle between checked and not checked.

By clicking this checkbox, you agree to the terms and conditions.

You can enable or disable notifications at any time.

**Examples**:

```python
"use client"

import { Checkbox } from "@/components/ui/checkbox"
import { Label } from "@/components/ui/label"

export function CheckboxDemo() {
  return (
    <div className="flex flex-col gap-6">
      <div className="flex items-center gap-3">
        <Checkbox id="terms" />
        <Label htmlFor="terms">Accept terms and conditions</Label>
      </div>
      <div className="flex items-start gap-3">
        <Checkbox id="terms-2" defaultChecked />
        <div className="grid gap-2">
        
...
```

```text
pnpm dlx shadcn@latest add checkbox
```

```python
import { Checkbox } from "@/components/ui/checkbox"
```

---

## Collapsible - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/collapsible

**Contents**:
- Collapsible
    - @peduarte starred 3 repositories
- Installation
- Usage

An interactive component which expands/collapses a panel.

**Examples**:

```python
"use client"

import * as React from "react"
import { ChevronsUpDown } from "lucide-react"

import { Button } from "@/components/ui/button"
import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from "@/components/ui/collapsible"

export function CollapsibleDemo() {
  const [isOpen, setIsOpen] = React.useState(false)

  return (
    <Collapsible
      open={isOpen}
      onOpenChange={setIsOpen}
      className="flex w-[350px] flex-col gap-2"
    >
      <div className="flex items
...
```

```text
pnpm dlx shadcn@latest add collapsible
```

```python
import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from "@/components/ui/collapsible"
```

---

## Command - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/command

**Contents**:
- Command
- About
- Installation
- Usage
- Examples
  - Dialog
- Command Palette
  - Combobox

Fast, composable, unstyled command menu for React.

The <Command /> component uses the cmdk component by pacocoursey.

Search for a command to run...

To show the command menu in a dialog, use the <CommandDialog /> component.

You can use the <Command /> component as a combobox. See the Combobox page for more information.

**Examples**:

```python
import {
  Calculator,
  Calendar,
  CreditCard,
  Settings,
  Smile,
  User,
} from "lucide-react"

import {
  Command,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
  CommandList,
  CommandSeparator,
  CommandShortcut,
} from "@/components/ui/command"

export function CommandDemo() {
  return (
    <Command className="rounded-lg border shadow-md md:min-w-[450px]">
      <CommandInput placeholder="Type a command or search..." />
      <CommandList>
        <CommandEmpty>No resu
...
```

```text
pnpm dlx shadcn@latest add command
```

```python
import {
  Command,
  CommandDialog,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
  CommandList,
  CommandSeparator,
  CommandShortcut,
} from "@/components/ui/command"
```

---

## Components - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components

**Contents**:
- Components

Here you can find all the components available in the library. We are working on adding more components.

---

## Context Menu - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/context-menu

**Contents**:
- Context Menu
- Installation
- Usage

Displays a menu to the user — such as a set of actions or functions — triggered by a button.

**Examples**:

```python
import {
  ContextMenu,
  ContextMenuCheckboxItem,
  ContextMenuContent,
  ContextMenuItem,
  ContextMenuLabel,
  ContextMenuRadioGroup,
  ContextMenuRadioItem,
  ContextMenuSeparator,
  ContextMenuShortcut,
  ContextMenuSub,
  ContextMenuSubContent,
  ContextMenuSubTrigger,
  ContextMenuTrigger,
} from "@/components/ui/context-menu"

export function ContextMenuDemo() {
  return (
    <ContextMenu>
      <ContextMenuTrigger className="flex h-[150px] w-[300px] items-center justify-center rounded-
...
```

```text
pnpm dlx shadcn@latest add context-menu
```

```python
import {
  ContextMenu,
  ContextMenuContent,
  ContextMenuItem,
  ContextMenuTrigger,
} from "@/components/ui/context-menu"
```

---

## Data Table - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/data-table

**Contents**:
- Data Table
- Introduction
- Table of Contents
- Installation
- Prerequisites
- Project Structure
- Basic Table
  - Column Definitions

Powerful table and datagrids built using TanStack Table.

Every data table or datagrid I've created has been unique. They all behave differently, have specific sorting and filtering requirements, and work with different data sources.

It doesn't make sense to combine all of these variations into a single component. If we do that, we'll lose the flexibility that headless UI provides.

So instead of a data-table component, I thought it would be more helpful to provide a guide on how to build your own.

We'll start with the basic <Table /> component and build a complex data table from scratch.

Tip: If you find yourself using the same table in multiple places in your app, you can always extract it into a reusable component.

This guide will show you how to use TanStack Table and the <Table /> component to build your own custom data table. We'll cover the following topics:

We are going to build a table to show recent payments. Here's what our data looks like:

Start by creating the following file structure:

I'm using a Next.js example here but this works for any other React framework.

Let's start by building a basic table.

First, we'll define our columns.

Note: Columns are where you define the core of what your table will look like. They define the data that will be displayed, how it will be formatted, sorted and filtered.

Next, we'll create a <DataTable /> component to render our table.

Tip: If you find yourself using <DataTable /> in multiple places, this is the component you could make reusable by extracting it to components/ui/data-table.tsx.

<DataTable columns={columns} data={data} />

Finally, we'll render our table in our page component.

Let's format the amount cell to display the dollar amount. We'll also align the cell to the right.

Update the header and cell definitions for amount as follows:

You can use the same approach to format other cells and headers.

Let's add row actions to our table. We'll use a <Dropdown /> component for this.

Update our 

*[Content truncated - see full docs]*

**Examples**:

```python
"use client"

import * as React from "react"
import {
  ColumnDef,
  ColumnFiltersState,
  flexRender,
  getCoreRowModel,
  getFilteredRowModel,
  getPaginationRowModel,
  getSortedRowModel,
  SortingState,
  useReactTable,
  VisibilityState,
} from "@tanstack/react-table"
import { ArrowUpDown, ChevronDown, MoreHorizontal } from "lucide-react"

import { Button } from "@/components/ui/button"
import { Checkbox } from "@/components/ui/checkbox"
import {
  DropdownMenu,
  DropdownMenuCheckboxItem,

...
```

```text
pnpm dlx shadcn@latest add table
```

```text
pnpm add @tanstack/react-table
```

---

## Dialog - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/dialog

**Contents**:
- Dialog
- Installation
- Usage
- Examples
  - Custom close button
- Notes

A window overlaid on either the primary window or another dialog window, rendering the content underneath inert.

To use the Dialog component from within a Context Menu or Dropdown Menu, you must encase the Context Menu or Dropdown Menu component in the Dialog component.

**Examples**:

```python
import { Button } from "@/components/ui/button"
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"

export function DialogDemo() {
  return (
    <Dialog>
      <form>
        <DialogTrigger asChild>
          <Button variant="outline">Open Dialog</Button>
        </DialogTrigger>
        <
...
```

```text
pnpm dlx shadcn@latest add dialog
```

```python
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
```

---

## Drawer - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/drawer

**Contents**:
- Drawer
- About
- Installation
- Usage
- Examples
  - Responsive Dialog

A drawer component for React.

Drawer is built on top of Vaul by emilkowalski_.

You can combine the Dialog and Drawer components to create a responsive dialog. This renders a Dialog component on desktop and a Drawer on mobile.

**Examples**:

```python
"use client"

import * as React from "react"
import { Minus, Plus } from "lucide-react"
import { Bar, BarChart, ResponsiveContainer } from "recharts"

import { Button } from "@/components/ui/button"
import {
  Drawer,
  DrawerClose,
  DrawerContent,
  DrawerDescription,
  DrawerFooter,
  DrawerHeader,
  DrawerTitle,
  DrawerTrigger,
} from "@/components/ui/drawer"

const data = [
  {
    goal: 400,
  },
  {
    goal: 300,
  },
  {
    goal: 200,
  },
  {
    goal: 300,
  },
  {
    goal: 200,
  
...
```

```text
pnpm dlx shadcn@latest add drawer
```

```python
import {
  Drawer,
  DrawerClose,
  DrawerContent,
  DrawerDescription,
  DrawerFooter,
  DrawerHeader,
  DrawerTitle,
  DrawerTrigger,
} from "@/components/ui/drawer"
```

---

## Dropdown Menu - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/dropdown-menu

**Contents**:
- Dropdown Menu
- Installation
- Usage
- Examples
  - Checkboxes
  - Radio Group
  - Dialog

Displays a menu to the user — such as a set of actions or functions — triggered by a button.

This example shows how to open a dialog from a dropdown menu.

Use modal={false} on the DropdownMenu component.

**Examples**:

```python
import { Button } from "@/components/ui/button"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuGroup,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuPortal,
  DropdownMenuSeparator,
  DropdownMenuShortcut,
  DropdownMenuSub,
  DropdownMenuSubContent,
  DropdownMenuSubTrigger,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"

export function DropdownMenuDemo() {
  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button variant="outline">
...
```

```text
pnpm dlx shadcn@latest add dropdown-menu
```

```python
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
```

---

## Empty - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/empty

**Contents**:
- Empty
- Installation
- Usage
- Examples
  - Outline
  - Background
  - Avatar
  - Avatar Group

Use the Empty component to display a empty state.

Use the border utility class to create a outline empty state.

Use the bg-* and bg-gradient-* utilities to add a background to the empty state.

Use the EmptyMedia component to display an avatar in the empty state.

Use the EmptyMedia component to display an avatar group in the empty state.

You can add an InputGroup component to the EmptyContent component.

The main component of the empty state. Wraps the EmptyHeader and EmptyContent components.

The EmptyHeader component wraps the empty media, title, and description.

Use the EmptyMedia component to display the media of the empty state such as an icon or an image. You can also use it to display other components such as an avatar.

Use the EmptyTitle component to display the title of the empty state.

Use the EmptyDescription component to display the description of the empty state.

Use the EmptyContent component to display the content of the empty state such as a button, input or a link.

**Examples**:

```python
import { IconFolderCode } from "@tabler/icons-react"
import { ArrowUpRightIcon } from "lucide-react"

import { Button } from "@/components/ui/button"
import {
  Empty,
  EmptyContent,
  EmptyDescription,
  EmptyHeader,
  EmptyMedia,
  EmptyTitle,
} from "@/components/ui/empty"

export function EmptyDemo() {
  return (
    <Empty>
      <EmptyHeader>
        <EmptyMedia variant="icon">
          <IconFolderCode />
        </EmptyMedia>
        <EmptyTitle>No Projects Yet</EmptyTitle>
        <Emp
...
```

```text
pnpm dlx shadcn@latest add empty
```

```python
import {
  Empty,
  EmptyContent,
  EmptyDescription,
  EmptyHeader,
  EmptyMedia,
  EmptyTitle,
} from "@/components/ui/empty"
```

---

## Field - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/field

**Contents**:
- Field
- Installation
- Usage
- Anatomy
- Form
- Examples
  - Input
  - Textarea

Combine labels, controls, and help text to compose accessible form fields and grouped inputs.

All transactions are secure and encrypted

Enter your 16-digit card number

The billing address associated with your payment method

The Field family is designed for composing accessible forms. A typical field is structured as follows:

See the Form documentation for building forms with the Field component and React Hook Form or Tanstack Form.

Choose a unique username for your account.

Must be at least 8 characters long.

Share your thoughts about our service.

Select your department or area of work.

Set your budget range ($200 - 800).

We need your address to deliver your order.

Select the items you want to show on the desktop.

Your Desktop & Documents folders are being synced with iCloud Drive. You can access them from other devices.

Yearly and lifetime plans offer significant savings.

Enable multi-factor authentication. If you do not have a two-factor device, you can use a one-time code sent to your email.

Wrap Field components inside FieldLabel to create selectable field groups. This works with RadioItem, Checkbox and Switch components.

Select the compute environment for your cluster.

Run GPU workloads on a K8s configured cluster.

Access a VM configured cluster to run GPU workloads.

Stack Field components with FieldGroup. Add FieldSeparator to divide them.

Get notified when ChatGPT responds to requests that take time, like research or image generation.

Get notified when tasks you've created have updates. Manage tasks

Fill in your profile information.

Provide your full name for identification

You can write your message here. Keep it short, preferably under 100 characters.

Container that renders a semantic fieldset with spacing presets.

Legend element for a FieldSet. Switch to the label variant to align with label sizing.

The FieldLegend has two variants: legend and label. The label variant applies label sizing and alignment. Handy if you have nested 

*[Content truncated - see full docs]*

**Examples**:

```python
import { Button } from "@/components/ui/button"
import { Checkbox } from "@/components/ui/checkbox"
import {
  Field,
  FieldDescription,
  FieldGroup,
  FieldLabel,
  FieldLegend,
  FieldSeparator,
  FieldSet,
} from "@/components/ui/field"
import { Input } from "@/components/ui/input"
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"
import { Textarea } from "@/components/ui/textarea"

export function FieldDemo() {
  return (
    
...
```

```text
pnpm dlx shadcn@latest add field
```

```python
import {
  Field,
  FieldContent,
  FieldDescription,
  FieldError,
  FieldGroup,
  FieldLabel,
  FieldLegend,
  FieldSeparator,
  FieldSet,
  FieldTitle,
} from "@/components/ui/field"
```

---

## Form - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/form

**Contents**:
- Form
- Features
- Anatomy
- Example
- Installation
  - Command
- Usage
  - Create a form schema

Building forms with React Hook Form and Zod.

The Form component is an abstraction over the react-hook-form library. Going forward, we recommend using the <Field /> component to build forms. See the Form documentation for more information.

Forms are tricky. They are one of the most common things you'll build in a web application, but also one of the most complex.

Well-designed HTML forms are:

In this guide, we will take a look at building forms with react-hook-form and zod. We're going to use a <FormField> component to compose accessible forms using Radix UI components.

The <Form /> component is a wrapper around the react-hook-form library. It provides a few things:

Define the shape of your form using a Zod schema. You can read more about using Zod in the Zod documentation.

Use the useForm hook from react-hook-form to create a form.

Since FormField is using a controlled component, you need to provide a default value for the field. See the React Hook Form docs to learn more about controlled components.

We can now use the <Form /> components to build our form.

That's it. You now have a fully accessible form that is type-safe with client-side validation.

**Examples**:

```javascript
<Form>
  <FormField
    control={...}
    name="..."
    render={() => (
      <FormItem>
        <FormLabel />
        <FormControl>
          { /* Your form field */}
        </FormControl>
        <FormDescription />
        <FormMessage />
      </FormItem>
    )}
  />
</Form>
```

```javascript
const form = useForm()
 
<FormField
  control={form.control}
  name="username"
  render={({ field }) => (
    <FormItem>
      <FormLabel>Username</FormLabel>
      <FormControl>
        <Input placeholder="shadcn" {...field} />
      </FormControl>
      <FormDescription>This is your public display name.</FormDescription>
      <FormMessage />
    </FormItem>
  )}
/>
```

```text
pnpm dlx shadcn@latest add form
```

---

## Forms - shadcn/ui

**URL**: https://ui.shadcn.com/docs/forms

**Contents**:
- Forms
- Pick Your Framework

Build forms with React and shadcn/ui.

Start by selecting your framework. Then follow the instructions to learn how to build forms with shadcn/ui and the form library of your choice.

---

## Hover Card - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/hover-card

**Contents**:
- Hover Card
- Installation
- Usage

For sighted users to preview content available behind a link.

**Examples**:

```python
import { CalendarIcon } from "lucide-react"

import {
  Avatar,
  AvatarFallback,
  AvatarImage,
} from "@/components/ui/avatar"
import { Button } from "@/components/ui/button"
import {
  HoverCard,
  HoverCardContent,
  HoverCardTrigger,
} from "@/components/ui/hover-card"

export function HoverCardDemo() {
  return (
    <HoverCard>
      <HoverCardTrigger asChild>
        <Button variant="link">@nextjs</Button>
      </HoverCardTrigger>
      <HoverCardContent className="w-80">
        <div c
...
```

```text
pnpm dlx shadcn@latest add hover-card
```

```python
import {
  HoverCard,
  HoverCardContent,
  HoverCardTrigger,
} from "@/components/ui/hover-card"
```

---

## Input Group - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/input-group

**Contents**:
- Input Group
- Installation
- Usage
- Examples
  - Icon
  - Text
  - Button
  - Tooltip

Display additional information or actions to an input or textarea.

Display additional text information alongside inputs.

Add buttons to perform actions within the input group.

Add tooltips to provide additional context or help.

Input groups also work with textarea components. Use block-start or block-end for alignment.

Show loading indicators while processing input.

Add labels within input groups to improve accessibility.

Pair input groups with dropdown menus for complex interactions.

Wrap input groups with button groups to create prefixes and suffixes.

Add the data-slot="input-group-control" attribute to your custom input for automatic behavior and focus state handling.

No style is applied to the custom input. Apply your own styles using the className prop.

The main component that wraps inputs and addons.

Displays icons, text, buttons, or other content alongside inputs.

For proper focus navigation, the InputGroupAddon component should be placed after the input. Set the align prop to position the addon.

For <InputGroupInput />, use the inline-start or inline-end alignment. For <InputGroupTextarea />, use the block-start or block-end alignment.

The InputGroupAddon component can have multiple InputGroupButton components and icons.

Displays buttons within input groups.

Replacement for <Input /> when building input groups. This component has the input group styles pre-applied and uses the unified data-slot="input-group-control" for focus state handling.

All other props are passed through to the underlying <Input /> component.

Replacement for <Textarea /> when building input groups. This component has the textarea group styles pre-applied and uses the unified data-slot="input-group-control" for focus state handling.

All other props are passed through to the underlying <Textarea /> component.

Add the min-w-0 class to the InputGroup component. See diff.

**Examples**:

```python
import { IconCheck, IconInfoCircle, IconPlus } from "@tabler/icons-react"
import { ArrowUpIcon, Search } from "lucide-react"

import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import {
  InputGroup,
  InputGroupAddon,
  InputGroupButton,
  InputGroupInput,
  InputGroupText,
  InputGroupTextarea,
} from "@/components/ui/input-group"
import { Separator } from "@/components/ui/separator"
import {
  Tooltip,
  TooltipCon
...
```

```text
pnpm dlx shadcn@latest add input-group
```

```python
import {
  InputGroup,
  InputGroupAddon,
  InputGroupButton,
  InputGroupInput,
  InputGroupText,
  InputGroupTextarea,
} from "@/components/ui/input-group"
```

---

## Input OTP - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/input-otp

**Contents**:
- Input OTP
- About
- Installation
  - Run the following command:
- Usage
- Examples
  - Pattern
  - Separator

Accessible one-time password component with copy paste functionality.

Input OTP is built on top of input-otp by @guilherme_rodz.

Use the pattern prop to define a custom pattern for the OTP input.

You can use the <InputOTPSeparator /> component to add a separator between the input groups.

You can use the value and onChange props to control the input value.

Please enter the one-time password sent to your phone.

We've made some updates and replaced the render props pattern with composition. Here's how to update your code if you prefer the composition pattern.

Note: You are not required to update your code if you are using the render prop. It is still supported.

To add a disabled state to the input, update <InputOTP /> as follows:

**Examples**:

```python
import {
  InputOTP,
  InputOTPGroup,
  InputOTPSeparator,
  InputOTPSlot,
} from "@/components/ui/input-otp"

export function InputOTPDemo() {
  return (
    <InputOTP maxLength={6}>
      <InputOTPGroup>
        <InputOTPSlot index={0} />
        <InputOTPSlot index={1} />
        <InputOTPSlot index={2} />
      </InputOTPGroup>
      <InputOTPSeparator />
      <InputOTPGroup>
        <InputOTPSlot index={3} />
        <InputOTPSlot index={4} />
        <InputOTPSlot index={5} />
      </Inp
...
```

```text
pnpm dlx shadcn@latest add input-otp
```

```python
import {
  InputOTP,
  InputOTPGroup,
  InputOTPSeparator,
  InputOTPSlot,
} from "@/components/ui/input-otp"
```

---

## Input - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/input

**Contents**:
- Input
- Installation
- Usage
- Examples
  - Default
  - File
  - Disabled
  - With Label

Displays a form input field or a component that looks like an input field.

Edit input.tsx and remove the flex class from the input component. This is no longer needed.

**Examples**:

```python
import { Input } from "@/components/ui/input"

export function InputDemo() {
  return <Input type="email" placeholder="Email" />
}
```

```text
pnpm dlx shadcn@latest add input
```

```python
import { Input } from "@/components/ui/input"
```

---

## Introduction - shadcn/ui

**URL**: https://ui.shadcn.com/docs

**Contents**:
- Introduction
- Open Code
  - How do I pull upstream updates in an Open Code approach?
- Composition
- Distribution
- Beautiful Defaults
- AI-Ready

shadcn/ui is a set of beautifully-designed, accessible components and a code distribution platform. Works with your favorite frameworks and AI models. Open Source. Open Code.

This is not a component library. It is how you build your component library.

You know how most traditional component libraries work: you install a package from NPM, import the components, and use them in your app.

This approach works well until you need to customize a component to fit your design system or require one that isn’t included in the library. Often, you end up wrapping library components, writing workarounds to override styles, or mixing components from different libraries with incompatible APIs.

This is what shadcn/ui aims to solve. It is built around the following principles:

shadcn/ui hands you the actual component code. You have full control to customize and extend the components to your needs. This means:

In a typical library, if you need to change a button’s behavior, you have to override styles or wrap the component. With shadcn/ui, you simply edit the button code directly.

How do I pull upstream updates in an Open Code approach?

Every component in shadcn/ui shares a common, composable interface. If a component does not exist, we bring it in, make it composable, and adjust its style to match and work with the rest of the design system.

A shared, composable interface means it's predictable for both your team and LLMs. You are not learning different APIs for every new component. Even for third-party ones.

shadcn/ui is also a code distribution system. It defines a schema for components and a CLI to distribute them.

You can use the schema to distribute your components to other projects or have AI generate completely new components based on existing schema.

shadcn/ui comes with a large collection of components that have carefully chosen default styles. They are designed to look good on their own and to work well together as a consistent system:

The design of shadcn/ui 

*[Content truncated - see full docs]*

---

## Introduction - shadcn/ui

**URL**: https://ui.shadcn.com/docs/

**Contents**:
- Introduction
- Open Code
  - How do I pull upstream updates in an Open Code approach?
- Composition
- Distribution
- Beautiful Defaults
- AI-Ready

shadcn/ui is a set of beautifully-designed, accessible components and a code distribution platform. Works with your favorite frameworks and AI models. Open Source. Open Code.

This is not a component library. It is how you build your component library.

You know how most traditional component libraries work: you install a package from NPM, import the components, and use them in your app.

This approach works well until you need to customize a component to fit your design system or require one that isn’t included in the library. Often, you end up wrapping library components, writing workarounds to override styles, or mixing components from different libraries with incompatible APIs.

This is what shadcn/ui aims to solve. It is built around the following principles:

shadcn/ui hands you the actual component code. You have full control to customize and extend the components to your needs. This means:

In a typical library, if you need to change a button’s behavior, you have to override styles or wrap the component. With shadcn/ui, you simply edit the button code directly.

How do I pull upstream updates in an Open Code approach?

Every component in shadcn/ui shares a common, composable interface. If a component does not exist, we bring it in, make it composable, and adjust its style to match and work with the rest of the design system.

A shared, composable interface means it's predictable for both your team and LLMs. You are not learning different APIs for every new component. Even for third-party ones.

shadcn/ui is also a code distribution system. It defines a schema for components and a CLI to distribute them.

You can use the schema to distribute your components to other projects or have AI generate completely new components based on existing schema.

shadcn/ui comes with a large collection of components that have carefully chosen default styles. They are designed to look good on their own and to work well together as a consistent system:

The design of shadcn/ui 

*[Content truncated - see full docs]*

---

## Item - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/item

**Contents**:
- Item
- Installation
- Usage
- Item vs Field
- Examples
  - Variants
  - Size
  - Icon

A versatile component that you can use to display any content.

The Item component is a straightforward flex container that can house nearly any type of content. Use it to display a title, description, and actions. Group it with the ItemGroup component to create a list of items.

You can pretty much achieve the same result with the div element and some classes, but I've built this so many times that I decided to create a component for it. Now I use it all the time.

A simple item with title and description.

Use Field if you need to display a form input such as a checkbox, input, radio, or select.

If you only need to display content such as a title, description, and actions, use Item.

Standard styling with subtle background and borders.

Outlined style with clear borders and transparent background.

Subdued appearance with muted colors for secondary content.

The Item component has different sizes for different use cases. For example, you can use the sm size for a compact item or the default size for a standard item.

A simple item with title and description.

New login detected from unknown device.

Last seen 5 months ago

Invite your team to collaborate on this project.

evilrabbit@vercel.com

Everyday tasks and UI generation.

Advanced thinking or reasoning.

Open Source model for everyone.

To render an item as a link, use the asChild prop. The hover and focus states will be applied to the anchor element.

Learn how to get started with our components.

Opens in a new tab with security attributes.

The main component for displaying content with media, title, description, and actions.

You can use the asChild prop to render a custom component as the item, for example a link. The hover and focus states will be applied to the custom component.

The ItemGroup component is a container that groups related items together with consistent styling.

The ItemSeparator component is a separator that separates items in the item group.

Use the ItemMedia component to display 

*[Content truncated - see full docs]*

**Examples**:

```python
import { BadgeCheckIcon, ChevronRightIcon } from "lucide-react"

import { Button } from "@/components/ui/button"
import {
  Item,
  ItemActions,
  ItemContent,
  ItemDescription,
  ItemMedia,
  ItemTitle,
} from "@/components/ui/item"

export function ItemDemo() {
  return (
    <div className="flex w-full max-w-md flex-col gap-6">
      <Item variant="outline">
        <ItemContent>
          <ItemTitle>Basic Item</ItemTitle>
          <ItemDescription>
            A simple item with title and 
...
```

```text
pnpm dlx shadcn@latest add item
```

```python
import {
  Item,
  ItemActions,
  ItemContent,
  ItemDescription,
  ItemFooter,
  ItemHeader,
  ItemMedia,
  ItemTitle,
} from "@/components/ui/item"
```

---

## Kbd - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/kbd

**Contents**:
- Kbd
- Installation
- Usage
- Examples
  - Group
  - Button
  - Tooltip
  - Input Group

Used to display textual user input from keyboard.

Use the KbdGroup component to group keyboard keys together.

Use Ctrl + BCtrl + K to open the command palette

Use the Kbd component inside a Button component to display a keyboard key inside a button.

You can use the Kbd component inside a Tooltip component to display a tooltip with a keyboard key.

You can use the Kbd component inside a InputGroupAddon component to display a keyboard key inside an input group.

Use the Kbd component to display a keyboard key.

Use the KbdGroup component to group Kbd components together.

**Examples**:

```python
import { Kbd, KbdGroup } from "@/components/ui/kbd"

export function KbdDemo() {
  return (
    <div className="flex flex-col items-center gap-4">
      <KbdGroup>
        <Kbd>⌘</Kbd>
        <Kbd>⇧</Kbd>
        <Kbd>⌥</Kbd>
        <Kbd>⌃</Kbd>
      </KbdGroup>
      <KbdGroup>
        <Kbd>Ctrl</Kbd>
        <span>+</span>
        <Kbd>B</Kbd>
      </KbdGroup>
    </div>
  )
}
```

```text
pnpm dlx shadcn@latest add kbd
```

```python
import { Kbd } from "@/components/ui/kbd"
```

---

## Label - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/label

**Contents**:
- Label
- Installation
- Usage

Renders an accessible label associated with controls.

**Examples**:

```python
import { Checkbox } from "@/components/ui/checkbox"
import { Label } from "@/components/ui/label"

export function LabelDemo() {
  return (
    <div>
      <div className="flex items-center space-x-2">
        <Checkbox id="terms" />
        <Label htmlFor="terms">Accept terms and conditions</Label>
      </div>
    </div>
  )
}
```

```text
pnpm dlx shadcn@latest add label
```

```python
import { Label } from "@/components/ui/label"
```

---

## MCP Server - shadcn/ui

**URL**: https://ui.shadcn.com/docs/mcp

**Contents**:
- MCP Server
- Quick Start
- What is MCP?
- How It Works
- Supported Registries
- Configuration
  - Claude Code
  - Cursor

Use the shadcn MCP server to browse, search, and install components from registries.

The shadcn MCP Server allows AI assistants to interact with items from registries. You can browse available components, search for specific ones, and install them directly into your project using natural language.

For example, you can ask an AI assistant to "Build a landing page using components from the acme registry" or "Find me a login form from the shadcn registry".

Registries are configured in your project's components.json file.

Select your MCP client and follow the instructions to configure the shadcn MCP server. If you'd like to do it manually, see the Configuration section.

Run the following command in your project:

Restart Claude Code and try the following prompts:

Note: You can use /mcp command in Claude Code to debug the MCP server.

Model Context Protocol (MCP) is an open protocol that enables AI assistants to securely connect to external data sources and tools. With the shadcn MCP server, your AI assistant gains direct access to:

The MCP server acts as a bridge between your AI assistant, component registries and the shadcn CLI.

The shadcn MCP server works out of the box with any shadcn-compatible registry.

You can use any MCP client to interact with the shadcn MCP server. Here are the instructions for the most popular ones.

To use the shadcn MCP server with Claude Code, add the following configuration to your project's .mcp.json file:

After adding the configuration, restart Claude Code and run /mcp to see the shadcn MCP server in the list. If you see Connected, you're good to go.

See the Claude Code MCP documentation for more details.

To configure MCP in Cursor, add the shadcn server to your project's .cursor/mcp.json configuration file:

After adding the configuration, enable the shadcn MCP server in Cursor Settings.

Once enabled, you should see a green dot next to the shadcn server in the MCP server list and a list of available tools.

See the Cursor M

*[Content truncated - see full docs]*

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

```text
{
  "mcpServers": {
    "shadcn": {
      "command": "npx",
      "args": ["shadcn@latest", "mcp"]
    }
  }
}
```

---

## Menubar - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/menubar

**Contents**:
- Menubar
- Installation
- Usage

A visually persistent menu common in desktop applications that provides quick access to a consistent set of commands.

**Examples**:

```python
import {
  Menubar,
  MenubarCheckboxItem,
  MenubarContent,
  MenubarItem,
  MenubarMenu,
  MenubarRadioGroup,
  MenubarRadioItem,
  MenubarSeparator,
  MenubarShortcut,
  MenubarSub,
  MenubarSubContent,
  MenubarSubTrigger,
  MenubarTrigger,
} from "@/components/ui/menubar"

export function MenubarDemo() {
  return (
    <Menubar>
      <MenubarMenu>
        <MenubarTrigger>File</MenubarTrigger>
        <MenubarContent>
          <MenubarItem>
            New Tab <MenubarShortcut>⌘T</MenubarS
...
```

```text
pnpm dlx shadcn@latest add menubar
```

```python
import {
  Menubar,
  MenubarContent,
  MenubarItem,
  MenubarMenu,
  MenubarSeparator,
  MenubarShortcut,
  MenubarTrigger,
} from "@/components/ui/menubar"
```

---

## Navigation Menu - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/navigation-menu

**Contents**:
- Navigation Menu
- Installation
- Usage
- Link

A collection of links for navigating websites.

You can use the asChild prop to make another component look like a navigation menu trigger. Here's an example of a link that looks like a navigation menu trigger.

**Examples**:

```python
"use client"

import * as React from "react"
import Link from "next/link"
import { CircleCheckIcon, CircleHelpIcon, CircleIcon } from "lucide-react"

import { useIsMobile } from "@/hooks/use-mobile"
import {
  NavigationMenu,
  NavigationMenuContent,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
  navigationMenuTriggerStyle,
} from "@/components/ui/navigation-menu"

const components: { title: string; href: string; description: string }[] = [
  {
    t
...
```

```text
pnpm dlx shadcn@latest add navigation-menu
```

```python
import {
  NavigationMenu,
  NavigationMenuContent,
  NavigationMenuIndicator,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
  NavigationMenuViewport,
} from "@/components/ui/navigation-menu"
```

---

## Open in v0 - shadcn/ui

**URL**: https://ui.shadcn.com/docs/v0

**Contents**:
- Open in v0

Open components in v0 for customization.

Every component on ui.shadcn.com is editable on v0 by Vercel. This allows you to easily customize the components in natural language and paste into your app.

To use v0, sign-up for a free Vercel account here. In addition to v0, this gives you free access to Vercel's frontend cloud platform by the creators of Next.js, where you can deploy and host your project for free.

Learn more about getting started with Vercel here.

Learn more about getting started with v0 here.

---

## Open in v0 - shadcn/ui

**URL**: https://ui.shadcn.com/docs/registry/open-in-v0

**Contents**:
- Open in v0
- Button
- Authentication
  - Using Query Parameter Authentication
  - Example Implementation

Integrate your registry with Open in v0.

If your registry is hosted and publicly accessible via a URL, you can open a registry item in v0 by using the https://v0.dev/chat/api/open?url=[URL] endpoint.

eg. https://v0.dev/chat/api/open?url=https://ui.shadcn.com/r/styles/new-york/login-01.json

Important: Open in v0 does not support cssVars, css, envVars, namespaced registries, or advanced authentication methods.

See Build your Open in v0 button for more information on how to build your own Open in v0 button.

Here's a simple example of how to add a Open in v0 button to your site.

Open in v0 only supports query parameter authentication. It does not support namespaced registries or advanced authentication methods like Bearer tokens or API keys in headers.

To add authentication to your registry for Open in v0, use a token query parameter:

When implementing this on your registry server:

Security Note: Make sure to encrypt and expire tokens. Never expose production tokens in documentation or examples.

**Examples**:

```python
import { Button } from "@/components/ui/button"
 
export function OpenInV0Button({ url }: { url: string }) {
  return (
    <Button
      aria-label="Open in v0"
      className="h-8 gap-1 rounded-[6px] bg-black px-3 text-xs text-white hover:bg-black hover:text-white dark:bg-white dark:text-black"
      asChild
    >
      <a
        href={`https://v0.dev/chat/api/open?url=${url}`}
        target="_blank"
        rel="noreferrer"
      >
        Open in{" "}
        <svg
          viewBox="0 0 4
...
```

```text
<OpenInV0Button url="https://example.com/r/hello-world.json" />
```

```text
https://registry.company.com/r/hello-world.json?token=your_secure_token_here
```

---

## Pagination - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/pagination

**Contents**:
- Pagination
- Installation
- Usage
  - Next.js

Pagination with page navigation, next and previous links.

By default the <PaginationLink /> component will render an <a /> tag.

To use the Next.js <Link /> component, make the following updates to pagination.tsx.

Note: We are making updates to the cli to automatically do this for you.

**Examples**:

```python
import {
  Pagination,
  PaginationContent,
  PaginationEllipsis,
  PaginationItem,
  PaginationLink,
  PaginationNext,
  PaginationPrevious,
} from "@/components/ui/pagination"

export function PaginationDemo() {
  return (
    <Pagination>
      <PaginationContent>
        <PaginationItem>
          <PaginationPrevious href="#" />
        </PaginationItem>
        <PaginationItem>
          <PaginationLink href="#">1</PaginationLink>
        </PaginationItem>
        <PaginationItem>
         
...
```

```text
pnpm dlx shadcn@latest add pagination
```

```python
import {
  Pagination,
  PaginationContent,
  PaginationEllipsis,
  PaginationItem,
  PaginationLink,
  PaginationNext,
  PaginationPrevious,
} from "@/components/ui/pagination"
```

---

## Popover - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/popover

**Contents**:
- Popover
- Installation
- Usage

Displays rich content in a portal, triggered by a button.

**Examples**:

```python
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover"

export function PopoverDemo() {
  return (
    <Popover>
      <PopoverTrigger asChild>
        <Button variant="outline">Open popover</Button>
      </PopoverTrigger>
      <PopoverContent className="w-80">
        <div className="grid gap-4">
          <div className=
...
```

```text
pnpm dlx shadcn@latest add popover
```

```python
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover"
```

---

## Progress - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/progress

**Contents**:
- Progress
- Installation
- Usage

Displays an indicator showing the completion progress of a task, typically displayed as a progress bar.

**Examples**:

```python
"use client"

import * as React from "react"

import { Progress } from "@/components/ui/progress"

export function ProgressDemo() {
  const [progress, setProgress] = React.useState(13)

  React.useEffect(() => {
    const timer = setTimeout(() => setProgress(66), 500)
    return () => clearTimeout(timer)
  }, [])

  return <Progress value={progress} className="w-[60%]" />
}
```

```text
pnpm dlx shadcn@latest add progress
```

```python
import { Progress } from "@/components/ui/progress"
```

---

## Radio Group - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/radio-group

**Contents**:
- Radio Group
- Installation
- Usage

A set of checkable buttons—known as radio buttons—where no more than one of the buttons can be checked at a time.

**Examples**:

```python
import { Label } from "@/components/ui/label"
import {
  RadioGroup,
  RadioGroupItem,
} from "@/components/ui/radio-group"

export function RadioGroupDemo() {
  return (
    <RadioGroup defaultValue="comfortable">
      <div className="flex items-center gap-3">
        <RadioGroupItem value="default" id="r1" />
        <Label htmlFor="r1">Default</Label>
      </div>
      <div className="flex items-center gap-3">
        <RadioGroupItem value="comfortable" id="r2" />
        <Label htmlFor="r2
...
```

```text
pnpm dlx shadcn@latest add radio-group
```

```python
import { Label } from "@/components/ui/label"
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"
```

---

## React Hook Form - shadcn/ui

**URL**: https://ui.shadcn.com/docs/forms/react-hook-form

**Contents**:
- React Hook Form
- Demo
- Approach
- Anatomy
- Form
  - Create a form schema
  - Setup the form
  - Build the form

Build forms in React using React Hook Form and Zod.

In this guide, we will take a look at building forms with React Hook Form. We'll cover building forms with the <Field /> component, adding schema validation using Zod, error handling, accessibility, and more.

We are going to build the following form. It has a simple text input and a textarea. On submit, we'll validate the form data and display any errors.

Note: For the purpose of this demo, we have intentionally disabled browser validation to show how schema validation and form errors work in React Hook Form. It is recommended to add basic browser validation in your production code.

Include steps to reproduce, expected behavior, and what actually happened.

This form leverages React Hook Form for performant, flexible form handling. We'll build our form using the <Field /> component, which gives you complete flexibility over the markup and styling.

Here's a basic example of a form using the <Controller /> component from React Hook Form and the <Field /> component.

We'll start by defining the shape of our form using a Zod schema

Note: This example uses zod v3 for schema validation, but you can replace it with any other Standard Schema validation library supported by React Hook Form.

Next, we'll use the useForm hook from React Hook Form to create our form instance. We'll also add the Zod resolver to validate the form data.

We can now build the form using the <Controller /> component from React Hook Form and the <Field /> component.

That's it. You now have a fully accessible form with client-side validation.

When you submit the form, the onSubmit function will be called with the validated form data. If the form data is invalid, React Hook Form will display the errors next to each field.

React Hook Form validates your form data using the Zod schema. Define a schema and pass it to the resolver option of the useForm hook.

React Hook Form supports different validation modes.

Display errors next to the field u

*[Content truncated - see full docs]*

**Examples**:

```python
"use client"

import * as React from "react"
import { zodResolver } from "@hookform/resolvers/zod"
import { Controller, useForm } from "react-hook-form"
import { toast } from "sonner"
import * as z from "zod"

import { Button } from "@/components/ui/button"
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import {
  Field,
  FieldDescription,
  FieldError,
  FieldGroup,
  FieldLabel,
} from "@/components/ui/field"
import { 
...
```

```javascript
<Controller
  name="title"
  control={form.control}
  render={({ field, fieldState }) => (
    <Field data-invalid={fieldState.invalid}>
      <FieldLabel htmlFor={field.name}>Bug Title</FieldLabel>
      <Input
        {...field}
        id={field.name}
        aria-invalid={fieldState.invalid}
        placeholder="Login button not working on mobile"
        autoComplete="off"
      />
      <FieldDescription>
        Provide a concise title for your bug report.
      </FieldDescription>
      
...
```

```python
import * as z from "zod"
 
const formSchema = z.object({
  title: z
    .string()
    .min(5, "Bug title must be at least 5 characters.")
    .max(32, "Bug title must be at most 32 characters."),
  description: z
    .string()
    .min(20, "Description must be at least 20 characters.")
    .max(100, "Description must be at most 100 characters."),
})
```

---

## Resizable - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/resizable

**Contents**:
- Resizable
- About
- Installation
- Usage
- Examples
  - Vertical
  - Handle

Accessible resizable panel groups and layouts with keyboard support.

The Resizable component is built on top of react-resizable-panels by bvaughn.

Use the direction prop to set the direction of the resizable panels.

You can set or hide the handle by using the withHandle prop on the ResizableHandle component.

**Examples**:

```python
import {
  ResizableHandle,
  ResizablePanel,
  ResizablePanelGroup,
} from "@/components/ui/resizable"

export function ResizableDemo() {
  return (
    <ResizablePanelGroup
      direction="horizontal"
      className="max-w-md rounded-lg border md:min-w-[450px]"
    >
      <ResizablePanel defaultSize={50}>
        <div className="flex h-[200px] items-center justify-center p-6">
          <span className="font-semibold">One</span>
        </div>
      </ResizablePanel>
      <ResizableHandle 
...
```

```text
pnpm dlx shadcn@latest add resizable
```

```python
import {
  ResizableHandle,
  ResizablePanel,
  ResizablePanelGroup,
} from "@/components/ui/resizable"
```

---

## Scroll Area - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/scroll-area

**Contents**:
- Scroll Area
    - Tags
- Installation
- Usage
- Examples
  - Horizontal Scrolling

Augments native scroll functionality for custom, cross-browser styling.

**Examples**:

```python
import * as React from "react"

import { ScrollArea } from "@/components/ui/scroll-area"
import { Separator } from "@/components/ui/separator"

const tags = Array.from({ length: 50 }).map(
  (_, i, a) => `v1.2.0-beta.${a.length - i}`
)

export function ScrollAreaDemo() {
  return (
    <ScrollArea className="h-72 w-48 rounded-md border">
      <div className="p-4">
        <h4 className="mb-4 text-sm leading-none font-medium">Tags</h4>
        {tags.map((tag) => (
          <React.Fragment key={
...
```

```text
pnpm dlx shadcn@latest add scroll-area
```

```python
import { ScrollArea } from "@/components/ui/scroll-area"
```

---

## Select - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/select

**Contents**:
- Select
- Installation
- Usage
- Examples
  - Scrollable

Displays a list of options for the user to pick from—triggered by a button.

**Examples**:

```python
import * as React from "react"

import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"

export function SelectDemo() {
  return (
    <Select>
      <SelectTrigger className="w-[180px]">
        <SelectValue placeholder="Select a fruit" />
      </SelectTrigger>
      <SelectContent>
        <SelectGroup>
          <SelectLabel>Fruits</SelectLabel>
          <SelectItem value="apple">Apple</SelectItem>
     
...
```

```text
pnpm dlx shadcn@latest add select
```

```python
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"
```

---

## Separator - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/separator

**Contents**:
- Separator
    - Radix Primitives
- Installation
- Usage

Visually or semantically separates content.

An open-source UI component library.

**Examples**:

```python
import { Separator } from "@/components/ui/separator"

export function SeparatorDemo() {
  return (
    <div>
      <div className="space-y-1">
        <h4 className="text-sm leading-none font-medium">Radix Primitives</h4>
        <p className="text-muted-foreground text-sm">
          An open-source UI component library.
        </p>
      </div>
      <Separator className="my-4" />
      <div className="flex h-5 items-center space-x-4 text-sm">
        <div>Blog</div>
        <Separator orient
...
```

```text
pnpm dlx shadcn@latest add separator
```

```python
import { Separator } from "@/components/ui/separator"
```

---

## Sheet - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/sheet

**Contents**:
- Sheet
- Installation
  - Usage
- Examples
  - Side
  - Size

Extends the Dialog component to display content that complements the main content of the screen.

Use the side property to <SheetContent /> to indicate the edge of the screen where the component will appear. The values can be top, right, bottom or left.

You can adjust the size of the sheet using CSS classes:

**Examples**:

```python
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import {
  Sheet,
  SheetClose,
  SheetContent,
  SheetDescription,
  SheetFooter,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "@/components/ui/sheet"

export function SheetDemo() {
  return (
    <Sheet>
      <SheetTrigger asChild>
        <Button variant="outline">Open</Button>
      </SheetTrigger>
      <SheetContent>
        <SheetHeader>
     
...
```

```text
pnpm dlx shadcn@latest add sheet
```

```python
import {
  Sheet,
  SheetContent,
  SheetDescription,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "@/components/ui/sheet"
```

---

## Sidebar - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/sidebar

**Contents**:
- Sidebar
- Installation
  - Run the following command to install sidebar.tsx
  - Add the following colors to your CSS file
- Structure
- Usage
- Your First Sidebar
  - Add a SidebarProvider and SidebarTrigger at the root of your application.

A composable, themeable and customizable sidebar component.

A sidebar that collapses to icons.

Sidebars are one of the most complex components to build. They are central to any application and often contain a lot of moving parts.

I don't like building sidebars. So I built 30+ of them. All kinds of configurations. Then I extracted the core components into sidebar.tsx.

We now have a solid foundation to build on top of. Composable. Themeable. Customizable.

Browse the Blocks Library.

The command above should install the colors for you. If not, copy and paste the following in your CSS file.

We'll go over the colors later in the theming section.

A Sidebar component is composed of the following parts:

Let's start with the most basic sidebar. A collapsible sidebar with a menu.

Add a SidebarProvider and SidebarTrigger at the root of your application.

We'll use the SidebarMenu component in a SidebarGroup.

You should see something like this:

The components in sidebar.tsx are built to be composable i.e you build your sidebar by putting the provided components together. They also compose well with other shadcn/ui components such as DropdownMenu, Collapsible or Dialog etc.

If you need to change the code in sidebar.tsx, you are encouraged to do so. The code is yours. Use sidebar.tsx as a starting point and build your own.

In the next sections, we'll go over each component and how to use them.

The SidebarProvider component is used to provide the sidebar context to the Sidebar component. You should always wrap your application in a SidebarProvider component.

If you have a single sidebar in your application, you can use the SIDEBAR_WIDTH and SIDEBAR_WIDTH_MOBILE variables in sidebar.tsx to set the width of the sidebar.

For multiple sidebars in your application, you can use the style prop to set the width of the sidebar.

To set the width of the sidebar, you can use the --sidebar-width and --sidebar-width-mobile CSS variables in the style prop.

This will handle the 

*[Content truncated - see full docs]*

**Examples**:

```text
pnpm dlx shadcn@latest add sidebar
```

```text
@layer base {
  :root {
    --sidebar: oklch(0.985 0 0);
    --sidebar-foreground: oklch(0.145 0 0);
    --sidebar-primary: oklch(0.205 0 0);
    --sidebar-primary-foreground: oklch(0.985 0 0);
    --sidebar-accent: oklch(0.97 0 0);
    --sidebar-accent-foreground: oklch(0.205 0 0);
    --sidebar-border: oklch(0.922 0 0);
    --sidebar-ring: oklch(0.708 0 0);
  }
 
  .dark {
    --sidebar: oklch(0.205 0 0);
    --sidebar-foreground: oklch(0.985 0 0);
    --sidebar-primary: oklch(0.488 0.243 264.
...
```

```python
import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar"
import { AppSidebar } from "@/components/app-sidebar"
 
export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <SidebarProvider>
      <AppSidebar />
      <main>
        <SidebarTrigger />
        {children}
      </main>
    </SidebarProvider>
  )
}
```

---

## Skeleton - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/skeleton

**Contents**:
- Skeleton
- Installation
- Usage
- Examples
  - Card

Use to show a placeholder while content is loading.

**Examples**:

```python
import { Skeleton } from "@/components/ui/skeleton"

export function SkeletonDemo() {
  return (
    <div className="flex items-center space-x-4">
      <Skeleton className="h-12 w-12 rounded-full" />
      <div className="space-y-2">
        <Skeleton className="h-4 w-[250px]" />
        <Skeleton className="h-4 w-[200px]" />
      </div>
    </div>
  )
}
```

```text
pnpm dlx shadcn@latest add skeleton
```

```python
import { Skeleton } from "@/components/ui/skeleton"
```

---

## Slider - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/slider

**Contents**:
- Slider
- Installation
- Usage

An input where the user selects a value from within a given range.

**Examples**:

```python
import { cn } from "@/lib/utils"
import { Slider } from "@/components/ui/slider"

type SliderProps = React.ComponentProps<typeof Slider>

export function SliderDemo({ className, ...props }: SliderProps) {
  return (
    <Slider
      defaultValue={[50]}
      max={100}
      step={1}
      className={cn("w-[60%]", className)}
      {...props}
    />
  )
}
```

```text
pnpm dlx shadcn@latest add slider
```

```python
import { Slider } from "@/components/ui/slider"
```

---

## Sonner - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/sonner

**Contents**:
- Sonner
- About
- Installation
  - Run the following command:
  - Add the Toaster component
- Usage
- Examples
- Changelog

An opinionated toast component for React.

Sonner is built and maintained by emilkowalski_.

We've updated the Sonner component to use icons from lucide. Update your sonner.tsx file to use the new icons.

**Examples**:

```python
"use client"

import { toast } from "sonner"

import { Button } from "@/components/ui/button"

export function SonnerDemo() {
  return (
    <Button
      variant="outline"
      onClick={() =>
        toast("Event has been created", {
          description: "Sunday, December 03, 2023 at 9:00 AM",
          action: {
            label: "Undo",
            onClick: () => console.log("Undo"),
          },
        })
      }
    >
      Show Toast
    </Button>
  )
}
```

```text
pnpm dlx shadcn@latest add sonner
```

```python
import { Toaster } from "@/components/ui/sonner"
 
export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head />
      <body>
        <main>{children}</main>
        <Toaster />
      </body>
    </html>
  )
}
```

---

## Spinner - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/spinner

**Contents**:
- Spinner
- Installation
- Usage
- Customization
- Examples
  - Size
  - Color
  - Button

An indicator that can be used to show a loading state.

You can replace the default spinner icon with any other icon by editing the Spinner component.

Use the size-* utility class to change the size of the spinner.

Use the text- utility class to change the color of the spinner.

Add a spinner to a button to indicate a loading state. The <Button /> will handle the spacing between the spinner and the text.

You can also use a spinner inside a badge.

Input Group can have spinners inside <InputGroupAddon>.

Use the spinner inside <ItemMedia> to indicate a loading state.

Use the Spinner component to display a spinner.

**Examples**:

```python
import {
  Item,
  ItemContent,
  ItemMedia,
  ItemTitle,
} from "@/components/ui/item"
import { Spinner } from "@/components/ui/spinner"

export function SpinnerDemo() {
  return (
    <div className="flex w-full max-w-xs flex-col gap-4 [--radius:1rem]">
      <Item variant="muted">
        <ItemMedia>
          <Spinner />
        </ItemMedia>
        <ItemContent>
          <ItemTitle className="line-clamp-1">Processing payment...</ItemTitle>
        </ItemContent>
        <ItemContent classN
...
```

```text
pnpm dlx shadcn@latest add spinner
```

```python
import { Spinner } from "@/components/ui/spinner"
```

---

## Switch - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/switch

**Contents**:
- Switch
- Installation
- Usage

A control that allows the user to toggle between checked and not checked.

**Examples**:

```python
import { Label } from "@/components/ui/label"
import { Switch } from "@/components/ui/switch"

export function SwitchDemo() {
  return (
    <div className="flex items-center space-x-2">
      <Switch id="airplane-mode" />
      <Label htmlFor="airplane-mode">Airplane Mode</Label>
    </div>
  )
}
```

```text
pnpm dlx shadcn@latest add switch
```

```python
import { Switch } from "@/components/ui/switch"
```

---

## Table - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/table

**Contents**:
- Table
- Installation
- Usage
- Data Table

A responsive table component.

You can use the <Table /> component to build more complex data tables. Combine it with @tanstack/react-table to create tables with sorting, filtering and pagination.

See the Data Table documentation for more information.

You can also see an example of a data table in the Tasks demo.

**Examples**:

```python
import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableFooter,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"

const invoices = [
  {
    invoice: "INV001",
    paymentStatus: "Paid",
    totalAmount: "$250.00",
    paymentMethod: "Credit Card",
  },
  {
    invoice: "INV002",
    paymentStatus: "Pending",
    totalAmount: "$150.00",
    paymentMethod: "PayPal",
  },
  {
    invoice: "INV003",
    paymentStatus: "Unpaid",
    totalAmount: "$350.00",
    paymen
...
```

```text
pnpm dlx shadcn@latest add table
```

```python
import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"
```

---

## Tabs - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/tabs

**Contents**:
- Tabs
- Installation
- Usage

A set of layered sections of content—known as tab panels—that are displayed one at a time.

**Examples**:

```python
import { AppWindowIcon, CodeIcon } from "lucide-react"

import { Button } from "@/components/ui/button"
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import {
  Tabs,
  TabsContent,
  TabsList,
  TabsTrigger,
} from "@/components/ui/tabs"

export function TabsDemo() {
  return (
    <div className="flex w-full max-w-sm flex-col ga
...
```

```text
pnpm dlx shadcn@latest add tabs
```

```python
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
```

---

## TanStack Form - shadcn/ui

**URL**: https://ui.shadcn.com/docs/forms/tanstack-form

**Contents**:
- TanStack Form
- Demo
- Approach
- Anatomy
- Form
  - Create a schema
  - Setup the form
  - Build the form

Build forms in React using TanStack Form and Zod.

This guide explores how to build forms using TanStack Form. You'll learn to create forms with the <Field /> component, implement schema validation with Zod, handle errors, and ensure accessibility.

We'll start by building the following form. It has a simple text input and a textarea. On submit, we'll validate the form data and display any errors.

Note: For the purpose of this demo, we have intentionally disabled browser validation to show how schema validation and form errors work in TanStack Form. It is recommended to add basic browser validation in your production code.

Include steps to reproduce, expected behavior, and what actually happened.

This form leverages TanStack Form for powerful, headless form handling. We'll build our form using the <Field /> component, which gives you complete flexibility over the markup and styling.

Here's a basic example of a form using TanStack Form with the <Field /> component.

We'll start by defining the shape of our form using a Zod schema.

Note: This example uses zod v3 for schema validation. TanStack Form integrates seamlessly with Zod and other Standard Schema validation libraries through its validators API.

Use the useForm hook from TanStack Form to create your form instance with Zod validation.

We are using onSubmit to validate the form data here. TanStack Form supports other validation modes, which you can read about in the documentation.

We can now build the form using the form.Field component from TanStack Form and the <Field /> component.

That's it. You now have a fully accessible form with client-side validation.

When you submit the form, the onSubmit function will be called with the validated form data. If the form data is invalid, TanStack Form will display the errors next to each field.

TanStack Form validates your form data using the Zod schema. Validation happens in real-time as the user types.

TanStack Form supports different validation strategies t

*[Content truncated - see full docs]*

**Examples**:

```python
"use client"

import * as React from "react"
import { useForm } from "@tanstack/react-form"
import { toast } from "sonner"
import * as z from "zod"

import { Button } from "@/components/ui/button"
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import {
  Field,
  FieldDescription,
  FieldError,
  FieldGroup,
  FieldLabel,
} from "@/components/ui/field"
import { Input } from "@/components/ui/input"
import {
  InputGroup,
 
...
```

```javascript
<form
  onSubmit={(e) => {
    e.preventDefault()
    form.handleSubmit()
  }}
>
  <FieldGroup>
    <form.Field
      name="title"
      children={(field) => {
        const isInvalid =
          field.state.meta.isTouched && !field.state.meta.isValid
        return (
          <Field data-invalid={isInvalid}>
            <FieldLabel htmlFor={field.name}>Bug Title</FieldLabel>
            <Input
              id={field.name}
              name={field.name}
              value={field.state.value}
...
```

```python
import * as z from "zod"
 
const formSchema = z.object({
  title: z
    .string()
    .min(5, "Bug title must be at least 5 characters.")
    .max(32, "Bug title must be at most 32 characters."),
  description: z
    .string()
    .min(20, "Description must be at least 20 characters.")
    .max(100, "Description must be at most 100 characters."),
})
```

---

## Textarea - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/textarea

**Contents**:
- Textarea
- Installation
- Usage
- Examples
  - Default
  - Disabled
  - With Label
  - With Text

Displays a form textarea or a component that looks like a textarea.

Your message will be copied to the support team.

**Examples**:

```python
import { Textarea } from "@/components/ui/textarea"

export function TextareaDemo() {
  return <Textarea placeholder="Type your message here." />
}
```

```text
pnpm dlx shadcn@latest add textarea
```

```python
import { Textarea } from "@/components/ui/textarea"
```

---

## Toast - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/toast

**Contents**:
- Toast

A succinct message that is displayed temporarily.

See the sonner documentation for more information.

If you're looking for the old toast component, see the old docs for more information.

---

## Toggle Group - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/toggle-group

**Contents**:
- Toggle Group
- Installation
- Usage
- Examples
  - Default
  - Outline
  - Single
  - Small

A set of two-state buttons that can be toggled on or off.

**Examples**:

```python
import { Bold, Italic, Underline } from "lucide-react"

import {
  ToggleGroup,
  ToggleGroupItem,
} from "@/components/ui/toggle-group"

export function ToggleGroupDemo() {
  return (
    <ToggleGroup variant="outline" type="multiple">
      <ToggleGroupItem value="bold" aria-label="Toggle bold">
        <Bold className="h-4 w-4" />
      </ToggleGroupItem>
      <ToggleGroupItem value="italic" aria-label="Toggle italic">
        <Italic className="h-4 w-4" />
      </ToggleGroupItem>
      <To
...
```

```text
pnpm dlx shadcn@latest add toggle-group
```

```python
import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group"
```

---

## Toggle - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/toggle

**Contents**:
- Toggle
- Installation
- Usage
- Examples
  - Default
  - Outline
  - With Text
  - Small

A two-state button that can be either on or off.

**Examples**:

```python
import { Bold } from "lucide-react"

import { Toggle } from "@/components/ui/toggle"

export function ToggleDemo() {
  return (
    <Toggle aria-label="Toggle italic">
      <Bold className="h-4 w-4" />
    </Toggle>
  )
}
```

```text
pnpm dlx shadcn@latest add toggle
```

```python
import { Toggle } from "@/components/ui/toggle"
```

---

## Tooltip - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/tooltip

**Contents**:
- Tooltip
- Installation
- Usage
- Changelog
  - 2025-09-22 Update tooltip colors

A popup that displays information related to an element when the element receives keyboard focus or the mouse hovers over it.

We've updated the tooltip colors to use the foreground color for the background and the background color for the foreground.

Replace bg-primary text-primary-foreground with bg-foreground text-background for both <TooltipContent /> and <TooltipArrow />.

**Examples**:

```python
import { Button } from "@/components/ui/button"
import {
  Tooltip,
  TooltipContent,
  TooltipTrigger,
} from "@/components/ui/tooltip"

export function TooltipDemo() {
  return (
    <Tooltip>
      <TooltipTrigger asChild>
        <Button variant="outline">Hover</Button>
      </TooltipTrigger>
      <TooltipContent>
        <p>Add to library</p>
      </TooltipContent>
    </Tooltip>
  )
}
```

```text
pnpm dlx shadcn@latest add tooltip
```

```python
import {
  Tooltip,
  TooltipContent,
  TooltipTrigger,
} from "@/components/ui/tooltip"
```

---

## Typography - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components/typography

**Contents**:
- Typography
- Taxing Laughter: The Joke Tax Chronicles
- The King's Plan
  - The Joke Tax
  - Jokester's Revolt
  - The People's Rebellion
- h1
- Taxing Laughter: The Joke Tax Chronicles

Styles for headings, paragraphs, lists...etc

We do not ship any typography styles by default. This page is an example of how you can use utility classes to style your text.

Once upon a time, in a far-off land, there was a very lazy king who spent all day lounging on his throne. One day, his advisors came to him with a problem: the kingdom was running out of money.

The king thought long and hard, and finally came up with a brilliant plan: he would tax the jokes in the kingdom.

The king's subjects were not amused. They grumbled and complained, but the king was firm:

As a result, people stopped telling jokes, and the kingdom fell into a gloom. But there was one person who refused to let the king's foolishness get him down: a court jester named Jokester.

Jokester began sneaking into the castle in the middle of the night and leaving jokes all over the place: under the king's pillow, in his soup, even in the royal toilet. The king was furious, but he couldn't seem to stop Jokester.

And then, one day, the people of the kingdom discovered that the jokes left by Jokester were so funny that they couldn't help but laugh. And once they started laughing, they couldn't stop.

The people of the kingdom, feeling uplifted by the laughter, started to tell jokes and puns again, and soon the entire kingdom was in on the joke.

The king, seeing how much happier his subjects were, realized the error of his ways and repealed the joke tax. Jokester was declared a hero, and the kingdom lived happily ever after.

The moral of the story is: never underestimate the power of a good laugh and always be careful of bad ideas.

The king, seeing how much happier his subjects were, realized the error of his ways and repealed the joke tax.

A modal dialog that interrupts the user with important content and expects a response.

Enter your email address.

**Examples**:

```javascript
export function TypographyDemo() {
  return (
    <div>
      <h1 className="scroll-m-20 text-4xl font-extrabold tracking-tight text-balance">
        Taxing Laughter: The Joke Tax Chronicles
      </h1>
      <p className="text-muted-foreground text-xl leading-7 [&:not(:first-child)]:mt-6">
        Once upon a time, in a far-off land, there was a very lazy king who
        spent all day lounging on his throne. One day, his advisors came to him
        with a problem: the kingdom was running out
...
```

```javascript
export function TypographyH1() {
  return (
    <h1 className="scroll-m-20 text-center text-4xl font-extrabold tracking-tight text-balance">
      Taxing Laughter: The Joke Tax Chronicles
    </h1>
  )
}
```

```javascript
export function TypographyH2() {
  return (
    <h2 className="scroll-m-20 border-b pb-2 text-3xl font-semibold tracking-tight first:mt-0">
      The People of the Kingdom
    </h2>
  )
}
```

---

## components.json - shadcn/ui

**URL**: https://ui.shadcn.com/docs/components-json

**Contents**:
- components.json
- $schema
- style
- tailwind
  - tailwind.config
  - tailwind.css
  - tailwind.baseColor
  - tailwind.cssVariables

Configuration for your project.

The components.json file holds configuration for your project.

We use it to understand how your project is set up and how to generate components customized for your project.

It is only required if you're using the CLI to add components to your project. If you're using the copy and paste method, you don't need this file.

You can create a components.json file in your project by running the following command:

See the CLI section for more information.

You can see the JSON Schema for components.json here.

The style for your components. This cannot be changed after initialization.

The default style has been deprecated. Use the new-york style instead.

Configuration to help the CLI understand how Tailwind CSS is set up in your project.

See the installation section for how to set up Tailwind CSS.

Path to where your tailwind.config.js file is located. For Tailwind CSS v4, leave this blank.

Path to the CSS file that imports Tailwind CSS into your project.

This is used to generate the default color palette for your components. This cannot be changed after initialization.

You can choose between using CSS variables or Tailwind CSS utility classes for theming.

To use utility classes for theming set tailwind.cssVariables to false. For CSS variables, set tailwind.cssVariables to true.

For more information, see the theming docs.

This cannot be changed after initialization. To switch between CSS variables and utility classes, you'll have to delete and re-install your components.

The prefix to use for your Tailwind CSS utility classes. Components will be added with this prefix.

Whether or not to enable support for React Server Components.

The CLI automatically adds a use client directive to client components when set to true.

Choose between TypeScript or JavaScript components.

Setting this option to false allows components to be added as JavaScript with the .jsx file extension.

The CLI uses these values and the paths config from yo

*[Content truncated - see full docs]*

**Examples**:

```text
pnpm dlx shadcn@latest init
```

```text
{
  "$schema": "https://ui.shadcn.com/schema.json"
}
```

```text
{
  "style": "new-york"
}
```

---
