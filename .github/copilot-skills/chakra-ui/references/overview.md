# Chakra-Ui - Overview

**Pages**: 2

---

## Overview

**URL**: https://chakra-ui.com/docs/theming/overview

**Contents**:
- Overview
- Architecture
- Config
  - cssVarsRoot
  - cssVarsPrefix
  - globalCss
  - preflight
  - theme

A guide for configuring the Chakra UI theming system.

The Chakra UI theming system is built around the API of Panda CSS.

Here's a quick overview of how the system is structured to provide a performant and extensible styling system:

The Chakra UI system is configured using the defineConfig function. This function accepts a configuration object that allows you to customize the styling system's behavior.

After a config is defined, it is passed to the createSystem function to create the styling engine.

cssVarsRoot is the root element where the token CSS variables will be applied.

cssVarsPrefix is the prefix used for the token CSS variables.

globalCss is used to apply global styles to the system.

preflight is used to apply css reset styles to the system.

Alternatively, you can use the preflight config property to apply css reset styles to the system. This is useful if you want to apply css reset styles to a specific element.

Use the theme config property to define the system theme. This property accepts the following properties:

Use the conditions config property to define custom selectors and media query conditions for use in the system.

Use the strictTokens config property to enforce the usage of only design tokens. This will throw a TS error if you try to use a token that is not defined in the theme.

When you configure the system properties (like colors, space, fonts, etc.), the CLI can be used to generate type definitions for them.

This will update the internal types in the @chakra-ui/react package, and make sure they are in sync with the theme. Providing a type-safe API and delightful experience for developers.

After a config is defined, it is passed to the createSystem function to create the styling engine. The returned system is framework-agnostic JavaScript styling engine that can be used to style components.

The system includes the following properties:

The token function is used to get a raw token value, or css variable.

Use the token.var func

*[Content truncated - see full docs]*

**Examples**:

```text
defineConfig
```

```text
createSystem
```

```text
ChakraProvider
```

---

## Styling

**URL**: https://chakra-ui.com/docs/styling/overview

**Contents**:
- Styling
- Concepts
- Compositions
- Style Props

All components are designed to be styled using props.

After installing Chakra UI, follow these guidelines to learn the key concepts:

After understanding the concepts, learn how to use these compositions to avoid repeating styles:

Style props are the most fundamental way to style your components in Chakra UI. They are basically css styles as props. Learn more about style props

---
