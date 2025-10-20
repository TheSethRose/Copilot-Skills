# Chakra-Ui - Common Patterns

Quick reference for common chakra-ui patterns and usage.

## Code Patterns

### 1. OverviewInstallationMigrationCLIFigmaContributingPlaygroundChangelogAI for AgentsMCP ServerLLMs.txtA

```
.cursorrules
```

### 2. AI RulesConfigure AI assistants with Chakra UI v3 rules for better code generationAI TipWant to skip

```
.cursorrules
```

### 3. Configure your AI coding assistants (like Cursor, GitHub Copilot, or Claude) by adding these rules t

```
.cursorrules
```

### 4. Here's an example:

```
---
description: Chakra UI v3 Development
globs: "*.tsx"
---

# Chakra UI v3 Rules

This project uses Chakra UI v3. Follow these rules:

1. Import from @chakra-ui/react: Alert, Avatar, Button, Card, Field, Table, etc.
2. Import from components/ui: Checkbox, Drawer, Radio, Menu, Dialog, Tooltip,
   e
```

### 5. OverviewInstallationMigrationCLIFigmaContributingPlaygroundChangelogAI for AgentsMCP ServerLLMs.txtA

```
npm i -D @chakra-ui/cli
```

### 6. CLILearn more to use the Chakra CLI command to generate snippets, typings, and download Pro blocksAI

```
npm i -D @chakra-ui/cli
```

### 7. The Chakra UI CLI can be used to generate typings for your custom theme tokens, like colors, semanti

```
npm i -D @chakra-ui/cli
```

### 8. Usage: npx chakra [options] [command] The official CLI for Chakra UI projects Options: -V, --version

```
Usage: npx chakra [options] [command]

The official CLI for Chakra UI projects

Options:
  -V, --version               output the version number
  -h, --help                  display help for command

Commands:
  typegen [options] <source>  Generate theme and recipe typings
  snippet                
```

## Examples

### Example 1

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

### Example 2

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

### Example 3

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

### Example 4

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

### Example 5

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

### Example 6

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

### Example 7

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

### Example 8

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

### Example 9

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

### Example 10

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


## Categories

See organized documentation in `references/`:

- `references/components.md` - Components
- `references/get-started.md` - Get-Started
- `references/overview.md` - Overview
