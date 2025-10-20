# Chakra-Ui - Components

**Pages**: 16

---

## AbsoluteCenter

**URL**: https://chakra-ui.com/docs/components/absolute-center

**Contents**:
- AbsoluteCenter
- Usage
- Examples
  - Axis Control
  - With Content
  - Overlay Usage
  - RTL Support
- Props

Used to horizontally and vertically center an element relative to its parent dimensions using absolute positioning.

The AbsoluteCenter component uses the position: absolute strategy to center its child element relative to its parent.

The parent element must have position: relative for proper positioning.

Control which axis to center on using the axis prop. Options are horizontal, vertical, or both (default).

<AbsoluteCenter axis="horizontal" />

<AbsoluteCenter axis="vertical" />

<AbsoluteCenter axis="both" />

Use AbsoluteCenter with various content types like icons, badges, and status indicators.

Perfect for creating loading overlays or modal-like content that needs to be centered over existing content.

AbsoluteCenter automatically handles right-to-left (RTL) layouts by adjusting the horizontal positioning and transforms appropriately.

**Examples**:

```python
import { AbsoluteCenter, Box } from "@chakra-ui/react"

const Demo = () => {
  return (
    <Box position="relative" h="100px" bg="bg.muted" borderRadius="md">
      <AbsoluteCenter>
        <Box bg="bg.emphasized" px="4" py="2" borderRadius="md" color="fg">
          Centered Content
        </Box>
      </AbsoluteCenter>
    </Box>
  )
}
```

```python
import { AbsoluteCenter, Box } from "@chakra-ui/react"

const Demo = () => {
  return (
    <Box position="relative" h="100px" bg="bg.muted" borderRadius="md">
      <AbsoluteCenter>
        <Box bg="bg.emphasized" px="4" py="2" borderRadius="md" color="fg">
          Centered Content
        </Box>
      </AbsoluteCenter>
    </Box>
  )
}
```

```text
AbsoluteCenter
```

---

## Animation

**URL**: https://chakra-ui.com/docs/components/concepts/animation

**Contents**:
- Animation
- Enter animation
- Exit animation
- Composing animations

Using CSS animations to animate Chakra UI components

We recommend using CSS animations to animate your Chakra UI components. This approach is performant, straightforward and provides a lot of flexibility.

You can animate both the mounting and unmounting phases of your components with better control.

When a disclosure component (popover, dialog) is open, the data-state attribute is set to open. This maps to data-state=open and can be styled with _open pseudo prop.

Here's an example that uses keyframes to create a fade-in animation:

When a disclosure component (popover, dialog) is closed, the data-state attribute is set to closed. This maps to data-state=closed and can be styled with _closed pseudo prop.

Here's an example that uses keyframes to create a fade-out animation:

Use the animationName prop to compose multiple animations together. This makes it easy to create complex animations with multiple keyframes.

**Examples**:

```text
data-state=open
```

```text
<Box
  data-state="open"
  _open={{
    animation: "fade-in 300ms ease-out",
  }}
>
  This is open
</Box>
```

```text
<Box
  data-state="open"
  _open={{
    animation: "fade-in 300ms ease-out",
  }}
>
  This is open
</Box>
```

---

## Aspect Ratio

**URL**: https://chakra-ui.com/docs/components/aspect-ratio

**Contents**:
- Aspect Ratio
- Usage
- Examples
  - Image
  - Video
  - Google Map
  - Responsive
- Props

Used to embed responsive videos and maps, etc

Here's how to embed an image that has a 4 by 3 aspect ratio.

To embed a video with a specific aspect ratio, use an iframe with src pointing to the link of the video.

Here's how to embed a responsive Google map using AspectRatio.

Here's an example of applying a responsive aspect ratio to a box.

These props can be passed to the AspectRatio component.

The aspect ratio of the Box. Common values are: `21/9`, `16/9`, `9/16`, `4/3`, `1.85/1`

The underlying element to render.

Use the provided child element as the default rendered element, combining their props and behavior.

**Examples**:

```python
import { AspectRatio, Center } from "@chakra-ui/react"

const Demo = () => {
  return (
    <AspectRatio bg="bg.muted" ratio={2 / 1}>
      <Center fontSize="xl">2 / 1</Center>
    </AspectRatio>
  )
}
```

```python
import { AspectRatio, Center } from "@chakra-ui/react"

const Demo = () => {
  return (
    <AspectRatio bg="bg.muted" ratio={2 / 1}>
      <Center fontSize="xl">2 / 1</Center>
    </AspectRatio>
  )
}
```

```python
import { AspectRatio } from "@chakra-ui/react"
```

---

## Bleed

**URL**: https://chakra-ui.com/docs/components/bleed

**Contents**:
- Bleed
- Some Heading
- Usage
- Examples
  - Vertical
  - Specific Direction
- Props

Used to break an element from the boundaries of its container

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

Use the block prop to make the element bleed vertically.

Use the inlineStart, inlineEnd, blockStart, and blockEnd props to make the element bleed in a specific direction.

The negative margin on the x-axis

The negative margin on the y-axis

The negative margin on the inline-start axis

The negative margin on the inline-end axis

The negative margin on the block-start axis

The negative margin on the block-end axis

The underlying element to render.

Use the provided child element as the default rendered element, combining their props and behavior.

**Examples**:

```python
import { Bleed, Box, Heading, Stack, Text } from "@chakra-ui/react"
import { DecorativeBox } from "compositions/lib/decorative-box"

const Demo = () => {
  return (
    <Box padding="10" rounded="sm" borderWidth="1px">
      <Bleed inline="10">
        <DecorativeBox height="20">Bleed</DecorativeBox>
      </Bleed>

      <Stack mt="6">
        <Heading size="md">Some Heading</Heading>
        <Text>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</Text>
      </Stack>
    </Box>
  )
}
```

```python
import { Bleed, Box, Heading, Stack, Text } from "@chakra-ui/react"
import { DecorativeBox } from "compositions/lib/decorative-box"

const Demo = () => {
  return (
    <Box padding="10" rounded="sm" borderWidth="1px">
      <Bleed inline="10">
        <DecorativeBox height="20">Bleed</DecorativeBox>
      </Bleed>

      <Stack mt="6">
        <Heading size="md">Some Heading</Heading>
        <Text>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</Text>
      </Stack>
    </Box>
  )
}
```

```python
import { Bleed } from "@chakra-ui/react"
```

---

## Box

**URL**: https://chakra-ui.com/docs/components/box

**Contents**:
- Box
- Usage
- Examples
  - Shorthand
  - Pseudo Props
  - Border
  - As Prop
  - Shadow

The most abstract styling component in Chakra UI on top of which all other Chakra UI components are built.

The Box component provides an easy way to write styles with ease. It provides access to design tokens and an unmatched DX when writing responsive styles.

Use shorthand like bg instead of backgroundColor, m instead of margin, etc.

Use pseudo props like _hover to apply styles on hover, _focus to apply styles on focus, etc.

Use the borderWidth and borderColor prop to apply border styles.

Good to know: Chakra applies borderStyle: solid globally so you don't have to.

Use the as prop to render a different component.

Inspect the DOM to see the rendered component.

Use the boxShadow or shadow prop to apply shadow styles.

Here's an example of a property card built with layout primitives in Chakra.

Modern home in city center in the heart of historic Los Angeles

The Box component supports all CSS properties as props, making it easy to style elements.

**Examples**:

```python
import { Box } from "@chakra-ui/react"

const Demo = () => {
  return (
    <Box background="tomato" width="100%" padding="4" color="white">
      This is the Box
    </Box>
  )
}
```

```python
import { Box } from "@chakra-ui/react"

const Demo = () => {
  return (
    <Box background="tomato" width="100%" padding="4" color="white">
      This is the Box
    </Box>
  )
}
```

```python
import { Box } from "@chakra-ui/react"
```

---

## Center

**URL**: https://chakra-ui.com/docs/components/center

**Contents**:
- Center
- Usage
- Examples
  - Icon
  - Center with Inline
  - Square
  - Circle
- Props

Used to center its child within itself.

Center can be used to create frames around icons or numbers.

Use the inline to change the display to inline-flex.

Square centers its child given the size (width and height).

Circle centers its child given the size and creates a circle around it.

**Examples**:

```python
import { Box, Center } from "@chakra-ui/react"

const Demo = () => {
  return (
    <Center bg="bg.emphasized" h="100px" maxW="320px">
      <Box>This will be centered</Box>
    </Center>
  )
}
```

```python
import { Box, Center } from "@chakra-ui/react"

const Demo = () => {
  return (
    <Center bg="bg.emphasized" h="100px" maxW="320px">
      <Box>This will be centered</Box>
    </Center>
  )
}
```

```python
import { Center, Circle, Square } from "@chakra-ui/react"
```

---

## Color Mode

**URL**: https://chakra-ui.com/docs/components/concepts/color-mode

**Contents**:
- Color Mode
- Setup
- useColorMode
- useColorModeValue
- Hydration Mismatch
- ColorModeButton
- Forced Color Mode

Adding support for light and dark color mode

Chakra UI relies on next-themes to add support for light and dark color mode.

In most cases, you have it installed and set up by the CLI in the Provider component. If not, you can install it manually.

The snippet includes hooks and components that make it feel similar to Chakra v2.

The useColorMode hook returns the current color mode and a function to toggle the color mode.

Calling toggleColorMode or setColorMode anywhere in your app tree toggles the color mode from light or dark and vice versa.

The useColorModeValue hook returns a value based on the current color mode.

Here's the signature:

The value returned will be the value of the light mode if the color mode is light, and the value of the dark mode if the color mode is dark.

When using useColorModeValue or useColorMode in SSR, you may notice a hydration mismatch when the page is mounted. This is because the color mode value is computed on the server side.

To avoid this, use the ClientOnly component to wrap the component that uses useColorModeValue and render a skeleton until mounted on the client side.

The color mode snippet comes with the ColorModeButton component built-in, you can import it to render an icon button that toggles the color mode.

It renders a skeleton on the server side and the icon on the client side.

The color mode snippet comes with the LightMode and DarkMode components built-in, you can import it to force the color mode.

You might need to update the color-mode.tsx snippet since the LightMode and DarkMode components were recently added to the snippet.

**Examples**:

```text
next-themes
```

```text
npx @chakra-ui/cli snippet add color-mode
```

```text
npx @chakra-ui/cli snippet add color-mode
```

---

## Components

**URL**: https://chakra-ui.com/docs/components/concepts/overview

**Contents**:
- Components

Accessible, modern and easy to style UI components.

Here's a list of all the components available in the library.

---

## Composition

**URL**: https://chakra-ui.com/docs/components/concepts/composition

**Contents**:
- Composition
- The as Prop
- The asChild Prop
- Best Practices

Learn how to compose components in Chakra UI.

Used to change the underlying HTML element that a React component renders. It provides a straightforward way to change the underlying element while retaining the component's functionality.

Used to compose a component's functionality onto its child element. This approach, inspired by Radix UI, offers maximum flexibility.

In this example, the asChild prop allows the Button to be used as the trigger for the popover.

To avoid common pitfalls when using the as and asChild props, there are a few best practices to consider:

**Examples**:

```text
<Heading as="h3">Hello, world!</Heading>
```

```text
<Heading as="h3">Hello, world!</Heading>
```

```text
<Popover.Root>
  <Popover.Trigger asChild>
    <Button>Open</Button>
  </Popover.Trigger>
</Popover.Root>
```

---

## Container

**URL**: https://chakra-ui.com/docs/components/container

**Contents**:
- Container
- Usage
- Examples
  - Sizes
  - Fluid
- Props

Used to constrain a content's width to the current breakpoint, while keeping it fluid.

The default maxWidth is 8xl which maps to 90rem (1440px).

Use the maxWidth prop to change the size of the container.

Use the fluid prop to make the container stretch to fill the width of its parent.

The color palette of the component

The underlying element to render.

Use the provided child element as the default rendered element, combining their props and behavior.

The centerContent of the component

The fluid of the component

**Examples**:

```python
import { Container } from "@chakra-ui/react"
import { DecorativeBox } from "compositions/lib/decorative-box"

const Demo = () => {
  return (
    <Container>
      <DecorativeBox px="2">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam
        consectetur, tortor in lacinia eleifend, dui nisl tristique nunc.
      </DecorativeBox>
    </Container>
  )
}
```

```python
import { Container } from "@chakra-ui/react"
import { DecorativeBox } from "compositions/lib/decorative-box"

const Demo = () => {
  return (
    <Container>
      <DecorativeBox px="2">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam
        consectetur, tortor in lacinia eleifend, dui nisl tristique nunc.
      </DecorativeBox>
    </Container>
  )
}
```

```text
90rem (1440px)
```

---

## Flex

**URL**: https://chakra-ui.com/docs/components/flex

**Contents**:
- Flex
- Usage
- Examples
  - Direction
  - Align
  - Justify
  - Order
  - Auto Margin

Used to manage flex layouts

Use the direction or flexDirection prop to change the direction of the flex

Use the align or alignItems prop to align the children along the cross axis.

Use the justify or justifyContent prop to align the children along the main axis.

Use the order prop to change the order of the children.

Apply margin to a flex item to push it away from its siblings.

Use the Spacer component to create flexible space between flex items. It will expand to fill all available space, pushing items to opposite ends.

Use the wrap or flexWrap prop to wrap the children when they overflow the parent.

The underlying element to render.

Use the provided child element as the default rendered element, combining their props and behavior.

**Examples**:

```python
import { Flex } from "@chakra-ui/react"
import { DecorativeBox } from "compositions/lib/decorative-box"

const Demo = () => {
  return (
    <Flex gap="4">
      <DecorativeBox height="10" />
      <DecorativeBox height="10" />
      <DecorativeBox height="10" />
    </Flex>
  )
}
```

```python
import { Flex } from "@chakra-ui/react"
import { DecorativeBox } from "compositions/lib/decorative-box"

const Demo = () => {
  return (
    <Flex gap="4">
      <DecorativeBox height="10" />
      <DecorativeBox height="10" />
      <DecorativeBox height="10" />
    </Flex>
  )
}
```

```python
import { Flex, Spacer } from "@chakra-ui/react"
```

---

## Float

**URL**: https://chakra-ui.com/docs/components/float

**Contents**:
- Float
- Usage
- Examples
  - Placement
  - Offset X
  - Offset Y
  - Offset
  - Avatar

Used to anchor an element to the edge of a container.

Float requires a parent element with position: relative style applied.

Use the placement prop to position the element along the edges of the container.

Use the offsetX prop to offset the element along the x-axis.

Use the offsetY prop to offset the element along the y-axis.

Use the offset prop to offset the element along both axes.

Here's an example of composing a Float component with an Avatar component.

The placement of the indicator

The x offset of the indicator

The y offset of the indicator

The x and y offset of the indicator

The underlying element to render.

Use the provided child element as the default rendered element, combining their props and behavior.

**Examples**:

```python
import { Box, Circle, Float } from "@chakra-ui/react"

export const FloatBasic = () => (
  <Box position="relative" w="80px" h="80px" bg="bg.emphasized">
    <Float>
      <Circle size="5" bg="red" color="white">
        3
      </Circle>
    </Float>
  </Box>
)
```

```python
import { Box, Circle, Float } from "@chakra-ui/react"

export const FloatBasic = () => (
  <Box position="relative" w="80px" h="80px" bg="bg.emphasized">
    <Float>
      <Circle size="5" bg="red" color="white">
        3
      </Circle>
    </Float>
  </Box>
)
```

```text
position: relative
```

---

## Grid

**URL**: https://chakra-ui.com/docs/components/grid

**Contents**:
- Grid
- Usage
- Examples
  - Col Span
  - Spanning Columns
- Props

Used to manage grid layouts

Pass colSpan prop to GridItem to span across columns.

In some layouts, you may need certain grid items to span specific amount of columns or rows instead of an even distribution

The underlying element to render.

Use the provided child element as the default rendered element, combining their props and behavior.

**Examples**:

```python
import { Grid } from "@chakra-ui/react"
import { DecorativeBox } from "compositions/lib/decorative-box"

const Demo = () => {
  return (
    <Grid templateColumns="repeat(3, 1fr)" gap="6">
      <DecorativeBox h="20" />
      <DecorativeBox h="20" />
      <DecorativeBox h="20" />
    </Grid>
  )
}
```

```python
import { Grid } from "@chakra-ui/react"
import { DecorativeBox } from "compositions/lib/decorative-box"

const Demo = () => {
  return (
    <Grid templateColumns="repeat(3, 1fr)" gap="6">
      <DecorativeBox h="20" />
      <DecorativeBox h="20" />
      <DecorativeBox h="20" />
    </Grid>
  )
}
```

```python
import { Grid, GridItem } from "@chakra-ui/react"
```

---

## Group

**URL**: https://chakra-ui.com/docs/components/group

**Contents**:
- Group
- Usage
- Examples
  - Button
  - Attached
  - Grow
- Props

Used to group and attach elements together

Here's an example of using the Group component to group buttons together.

Use the attached prop to attach the children together.

Note: When composing custom components and attaching them to a Group, ensure you forward props.

Use the grow prop to make the children grow to fill the available space.

The underlying element to render.

Use the provided child element as the default rendered element, combining their props and behavior.

**Examples**:

```python
import { Group } from "@chakra-ui/react"
import { DecorativeBox } from "compositions/lib/decorative-box"

const Demo = () => {
  return (
    <Group>
      <DecorativeBox h="20" w="40">
        1
      </DecorativeBox>
      <DecorativeBox h="20" w="40">
        2
      </DecorativeBox>
    </Group>
  )
}
```

```python
import { Group } from "@chakra-ui/react"
import { DecorativeBox } from "compositions/lib/decorative-box"

const Demo = () => {
  return (
    <Group>
      <DecorativeBox h="20" w="40">
        1
      </DecorativeBox>
      <DecorativeBox h="20" w="40">
        2
      </DecorativeBox>
    </Group>
  )
}
```

```python
import { Group } from "@chakra-ui/react"
```

---

## Server Components

**URL**: https://chakra-ui.com/docs/components/concepts/server-components

**Contents**:
- Server Components
- Usage
- Chakra Factory
- Hooks
- Render Props

Learn how to use Chakra UI with React Server Components.

React Server Components is a new feature in React that allows you to build components that render on the server and return UI to the client without hydration.

Client components are still server-rendered but hydrated on the client. Learn more about Server component patterns

Chakra UI components are client components because they rely on useState, useRef and useState which are not available in server components.

Here's an example of how to use Chakra UI components with React Server Components in Next.js

When using the chakra() factory function, use the use client directive and move the component to a dedicated file.

Then import the component in your page server component

When importing hooks from Chakra UI, use the use client directive

When using render props, use the use client directive

**Examples**:

```python
import { Heading } from "@chakra-ui/react"
import fs from "node:fs"

export default async function Page() {
  const content = fs.readFileSync("path/to/file.md", "utf-8")
  return <Heading as="h1">{content}</Heading>
}
```

```python
import { Heading } from "@chakra-ui/react"
import fs from "node:fs"

export default async function Page() {
  const content = fs.readFileSync("path/to/file.md", "utf-8")
  return <Heading as="h1">{content}</Heading>
}
```

```python
"use client"

import { chakra } from "@chakra-ui/react"

export const BlogPost = chakra("div", {
  base: {
    color: "red",
  },
  variants: {
    primary: {
      true: { color: "blue" },
      false: { color: "green" },
    },
  },
})
```

---

## Testing

**URL**: https://chakra-ui.com/docs/components/concepts/testing

**Contents**:
- Testing
- Setup
- Configuration
- Setup Test File
- Custom Render
- Testing Components

Best practices for testing React components using Vitest and Jest.

When writing tests with Vitest or Jest, use the following practices to get the best results.

Before writing tests, ensure your project has the necessary dependencies:

Create the vite.config.ts file to configure Vitest.

Setting globals: true will automatically import the Vitest globals and removes the need to import expect, test, describe, etc.

Create the setup-test.ts file to configure the testing environment and mock unimplemented APIs.

Here's a common example for Chakra v3 projects:

First, you need to create a custom render function to wrap your component in the ChakraProvider.

test-utils/render.tsx

Now, you can use the render function to test your components.

**Examples**:

```text
npm install --save-dev vitest jsdom @testing-library/dom @testing-library/jest-dom @testing-library/react @testing-library/user-event
```

```text
npm install --save-dev vitest jsdom @testing-library/dom @testing-library/jest-dom @testing-library/react @testing-library/user-event
```

```text
vite.config.ts
```

---
