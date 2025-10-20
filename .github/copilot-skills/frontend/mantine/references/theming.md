# Mantine - Theming

**Pages**: 20

---

## CSS modules | Mantine

**URL**: https://mantine.dev/styles/css-modules/

**Contents**:
- CSS modules
- Usage
- How CSS modules work
- Referencing global class names
- Adding styles to Mantine components
- Styling Mantine components without CSS modules

All Mantine components use CSS modules for styling. It is recommended to use CSS modules in your project as well, but it is not required – Mantine components are fully compatible with any third-party styling solution and native CSS.

CSS modules are supported out of the box by all major frameworks and build tools. Usually, all you need to do is to create *.module.css file:

And then import it in your component:

When you create a *.module.css file, your build tool will generate a unique class name for each class in your file. For example, when you import the following file in your .js/.ts file:

You will get an object with unique class names:

With CSS modules, you do not need to worry about class name collisions, you can use any class name you want.

To reference global class names in CSS Modules, you can use :global selector:

The code above will compile to the following CSS:

You can add styles to most of Mantine components using className prop – the same way as you would do with a regular HTML element. To set properties to your theme values, you can use Mantine CSS variables:

To apply styles to inner elements of Mantine components with CSS modules, you can use classNames prop (see Styles API for more information):

All Mantine components are fully compatible with any third-party styling solution and native CSS. There are two main strategies to apply styles with a third-party library:

Example of applying styles with a utility CSS library:

Example of applying styles with global CSS:

You can combine both approaches to achieve desired results, for example, @emotion/styled and styled-components packages will pass className prop to a given component, and you can use static selectors to style inner elements:

Consider using CSS modules first

CSS modules are the recommended way of styling Mantine components. Before choosing another styling solution, make sure that CSS modules do not fit your needs. Other solutions have limitations, for example:

Build fully functio

*[Content truncated - see full docs]*

**Examples**:

```text
/* Button.module.css */
.button {
  color: red;
}
```

```python
import classes from './Button.module.css';

function Demo() {
  return (
    <button className={classes.button} type="button">
      Button
    </button>
  );
}
```

```text
/* Button.module.css */
.button {
  color: red;
}

.text {
  color: blue;
}
```

---

## CSS variables | Mantine

**URL**: https://mantine.dev/styles/css-variables/

**Contents**:
- Mantine CSS variables
- Typography variables
  - Font family
  - Font size
  - Line height
  - Headings
- This is h1 title
- This is h2 title

MantineProvider exposes all Mantine CSS variables based on the given theme. You can use these variables in CSS files, style prop or any other styles. Note that not all values are documented on this page, you can find full list of variables on this page.

Typography variables control font family, font size, line height, font weight, and other text-related properties of all Mantine components.

The following CSS variables are used to assign font families to all Mantine components:

Controls font-family property of most Mantine components

Controls font-family property of code blocks

Controls font-family property of headings

You can control these variables in the theme. Note that if theme.headings.fontFamily is not set, --mantine-font-family-headings value will be the same as --mantine-font-family.

If you want to use system fonts as a fallback for custom fonts, you can reference DEFAULT_THEME value instead of defining it manually:

You can reference font family variables in your CSS:

And in ff style prop:

Font size variables are used in most Mantine components to control text size. The variable that is chosen depends on the component and its size prop.

You can reference font size variables in CSS:

And in fz style prop:

To define custom font sizes, can use theme.fontSizes property:

Note that theme.fontSizes object is merged with the DEFAULT_THEME.fontSizes – it is not required to define all values, only those that you want to change.

You can add any number of additional font sizes to the theme.fontSizes object. These values will be defined as CSS variables in --mantine-font-size-{size} format:

After defining theme.fontSizes, you can reference these variables in your CSS:

Case conversion (camelCase to kebab-case) is not automatically applied to custom font sizes. If you define theme.fontSizes with camelCase keys, you need to reference them in camelCase format. For example, if you define { customSize: '1rem' }, you need to reference it as --mantine-font-size-c

*[Content truncated - see full docs]*

**Examples**:

```python
import { createTheme } from '@mantine/core';

const theme = createTheme({
  // Controls --mantine-font-family
  fontFamily: 'Arial, sans-serif',

  // Controls --mantine-font-family-monospace
  fontFamilyMonospace: 'Courier New, monospace',

  headings: {
    // Controls --mantine-font-family-headings
    fontFamily: 'Georgia, serif',
  },
});
```

```python
import { createTheme, DEFAULT_THEME } from '@mantine/core';

const theme = createTheme({
  fontFamily: `Roboto, ${DEFAULT_THEME.fontFamily}`,
});
```

```text
.text {
  font-family: var(--mantine-font-family);
}

.code {
  font-family: var(--mantine-font-family-monospace);
}

.heading {
  font-family: var(--mantine-font-family-headings);
}
```

---

## CSS variables list | Mantine

**URL**: https://mantine.dev/styles/css-variables-list/

**Contents**:
- Default CSS variables list
- CSS variables not depending on color scheme
- Light color scheme only variables
- Dark color scheme only variables

This page contains a list of all Mantine CSS variables that are generated from default theme.

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

---

## Color functions | Mantine

**URL**: https://mantine.dev/styles/color-functions/

**Contents**:
- Color functions
- darken and lighten
- alpha
- parseThemeColor
- getThemeColor
- getGradient
- isLightColor
- luminance

@mantine/core package exports several functions that can be used to manipulate colors or extract information before using them as CSS value.

darken and lighten functions can be used to manipulate color brightness, they accept color in any format as first argument and the amount of lightness to add/remove as second argument.

alpha function converts color to rgba format with a given alpha channel, it is usually used to make colors more transparent. If it is not possible to convert color to rgba format (for example if color is a CSS variable), the function will use color-mix. Note that color-mix is not supported in some older browsers, you can check caniuse for more information.

parseThemeColor function returns information about a given color in the following format:

parseThemeColor function can be used everywhere theme object is available, for example in CSS variables resolver, variant color resolver or component body:

getThemeColor is a simpler version of parseThemeColor function, it accepts a color string as first argument and theme object as second argument. It returns parsed color value or CSS variable:

getGradient function transforms given MantineGradient object to CSS gradient string:

isLightColor function can be used to achieve better contrast between text and background:

luminance function returns color luminance, it can be used to check colors contrast:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { darken, lighten } from '@mantine/core';

lighten('#228BE6', 0.1); // lighten by 10%
// -> rgba(56, 151, 233, 1)

darken('rgb(245, 159, 0)', 0.5); // darken by 50%
// -> rgba(123, 80, 0, 1)

darken('rgba(245, 159, 0, .3)', 0.5); // darken by 50%
// -> rgba(123, 80, 0, 1, .3)

lighten('var(--mantine-color-gray-4)', 0.74);
// -> color-mix(in srgb, var(--mantine-color-gray-4), white 74%)
```

```python
import { alpha } from '@mantine/core';

alpha('#4578FC', 0.45); // -> rgba(69, 120, 252, 0.45)
alpha('var(--mantine-color-gray-4)', 0.74);
// -> color-mix(in srgb, var(--mantine-color-gray-4), transparent 26%)
```

```text
interface ParseThemeColorResult {
  /**
   * True if given color is theme color, for example
   * `blue`, `orange.9`, `pink.3` are theme colors
   * `#fff`, `rgba(0, 0, 0, .5)` are not
   */
  isThemeColor: boolean;

  /**
   * Key of `theme.colors` if given color is theme color, for example
   * if given color is `blue` it will be `blue`,
   * if given color is `orange.9` it will be `orange`
   */
  color: string;

  /**
   * Resolved color value, for example
   * if given color is `blue.7` it 
...
```

---

## PostCSS preset | Mantine

**URL**: https://mantine.dev/styles/postcss-preset/

**Contents**:
- Mantine PostCSS preset
- Installation
- Usage
- rem/em functions
- Auto convert px to rem
- dark and light mixins
- smaller-than and larger-than mixins
- light-dark function

postcss-preset-mantine provides several CSS functions and mixins to help you write styles. It is not required to use it, but highly recommended. All demos that feature styles assume that you have this preset installed.

postcss-preset-mantine includes the following PostCSS plugins:

Install postcss-preset-mantine as a dev dependency:

Note that setting up PostCSS may be different depending on your build tool/framework, check a dedicated framework guide to learn more. Add postcss-preset-mantine to your postcss.config.cjs file (usually it is located in the root of your project):

All done! You can now use all the features of the preset.

rem and em functions can be used to convert pixels to rem/em units. 16px = 1rem and 16px = 1em, em values are supposed to be used in media queries, rem everywhere else. You can learn more about units conversions in this guide.

Will be transformed to:

autoRem option can be used to automatically convert all pixel values to rem units in .css files:

This option works similar to rem function. The following code:

Will be transformed to:

Note that autoRem converts only CSS properties, values in @media queries are not converted automatically – you still need to use em function to convert them.

autoRem option does not convert values in the following cases:

If you want to convert above values to rem units, use rem function manually.

dark and light mixins can be used to create styles that will be applied only in dark or light color scheme.

Will be transformed to:

Note that usually you do not need to use both light and dark mixins at the same time. It is easier to define styles for light color scheme and then use dark mixin to override them in dark color scheme.

To define values for light/dark color scheme on the :root/html element, use light-root and dark-root mixins instead:

smaller-than and larger-than mixins can be used to create styles that will be applied only when the screen is smaller or larger than specified breakpoint.

Will

*[Content truncated - see full docs]*

**Examples**:

```text
yarn add --dev postcss-preset-mantine
```

```text
npm install --save-dev postcss-preset-mantine
```

```text
module.exports = {
  plugins: {
    'postcss-preset-mantine': {},
  },
};
```

---

## RTL (right-to-left) | Mantine

**URL**: https://mantine.dev/styles/rtl/

**Contents**:
- Right-to-left direction
- DirectionProvider
- dir attribute
- useDirection hook
- rtl mixin

All Mantine components support right-to-left direction out of the box. You can preview how components work with RTL direction by clicking direction control in the top right corner or pressing Ctrl + Shift + L.

DirectionProvider component is used to set direction for all components inside it. It is required to wrap your application with DirectionProvider if you are planning to either use RTL direction or change direction dynamically.

DirectionProvider supports the following props:

Setup DirectionProvider in your application:

It is required to set dir attribute on the root element of your application, usually it is html element. DirectionProvider will use its value to set direction on mount if detectDirection prop is set to true. Note that this guide does not cover setting dir attribute for different frameworks – follow your framework documentation to learn how to do it.

useDirection returns an object with the following properties:

You can use it to create direction control in your application:

If you have postcss-preset-mantine installed then you can use rtl mixin in .css files:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```text
export interface DirectionProviderProps {
  /** Your application */
  children: React.ReactNode;

  /** Direction set as a default value, `ltr` by default */
  initialDirection?: 'rtl' | 'ltr';

  /** Determines whether direction should be updated on mount based on `dir` attribute set on root element (usually html element), `true` by default  */
  detectDirection?: boolean;
}
```

```python
import { DirectionProvider, MantineProvider } from '@mantine/core';

function Demo() {
  return (
    <DirectionProvider>
      <MantineProvider>{/* Your app here */}</MantineProvider>
    </DirectionProvider>
  );
}
```

```text
<!doctype html>
<!-- Set direction attribute on html element -->
<html dir="rtl">
  <head></head>
  <body></body>
</html>
```

---

## Responsive styles | Mantine

**URL**: https://mantine.dev/styles/responsive/

**Contents**:
- Responsive styles
- Media queries
- Configure breakpoints
- Breakpoints variables in CSS modules
- hiddenFrom and visibleFrom props
- Hidden and visible from as classes
- Component size based on media query
- use-media-query hook

theme.breakpoints are used in all responsive Mantine components. Breakpoints are expected to be set in em units. You can configure these values with MantineProvider:

Default theme.breakpoints values:

It is not possible to use CSS variables inside media queries – these values cannot be dynamically generated by MantineProvider. To use Mantine theme breakpoints in your .css files, you will need postcss-simple-vars package:

Add it to your PostCSS config in postcss.config.cjs:

Then you will be able to access these variables in your .css files:

Will be transformed to:

Dynamic breakpoints are not supported

Values that are defined in postcss-simple-vars config are static and are not connected to the theme – if values change, you will need to update them manually in both theme override and postcss config.

All Mantine components that have a root element support hiddenFrom and visibleFrom props. These props accept breakpoint (xs, sm, md, lg, xl) and hide the component when viewport width is less than or greater than the specified breakpoint:

If you are building a custom component and want to use the same logic as in hiddenFrom and visibleFrom props but you do not want to use Mantine components, you can use mantine-hidden-from-{x} and mantine-visible-from-{x} classes.

Some components support size prop, which changes various aspects of component appearance. size prop is not responsive – it is not possible to define different component sizes for different screen sizes. Instead, you can render multiple components with different sizes and show/hide them based on media query with className or hiddenFrom/visibleFrom props:

You can use use-media-query hook to change some of component props based on media query. Note that this approach is not recommended for most of the cases if you have ssr in your application (you use Next.js, React Router, Gatsby or any other framework that includes ssr) as it may cause hydration mismatch. If you do not have ssr in your application (for e

*[Content truncated - see full docs]*

**Examples**:

```text
.demo {
  background-color: var(--mantine-color-blue-filled);
  color: var(--mantine-color-white);
  padding: var(--mantine-spacing-md);
  text-align: center;

  @media (min-width: em(750px)) {
    background-color: var(--mantine-color-red-filled);
  }
}
```

```python
import { createTheme, MantineProvider } from '@mantine/core';

const theme = createTheme({
  breakpoints: {
    xs: '30em',
    sm: '48em',
    md: '64em',
    lg: '74em',
    xl: '90em',
  },
});

function Demo() {
  return (
    <MantineProvider theme={theme}>
      {/* Your app here */}
    </MantineProvider>
  );
}
```

```text
yarn add --dev postcss-simple-vars
```

---

## Style props | Mantine

**URL**: https://mantine.dev/styles/style-props/

**Contents**:
- Style props
- Supported props
- Theme values
- Responsive styles

With style props, you can add inline styles to any Mantine component. Style props add styles to the root element, if you need to style nested elements, use Styles API instead.

All Mantine components that have root element support the following style props:

Some style props can reference values from theme, for example mt will use theme.spacing value if you set xs, sm, md, lg, xl:

In c, bd and bg props you can reference colors from theme.colors:

You can use object syntax to add responsive styles with style props. Note that responsive style props are less performant than regular style props, it is not recommended to use them in large lists of elements.

Responsive values are calculated the following way:

In this case the element will have the following styles:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Box } from '@mantine/core';

function Demo() {
  return (
    <Box mx="auto" maw={400} c="blue.6" bg="#fff">
      Your component
    </Box>
  );
}
```

```python
import { Box } from '@mantine/core';

function Demo() {
  return (
    <>
      {/* margin-top: theme.spacing.xs */}
      <Box mt="xs" />

      {/* margin-top: theme.spacing.md * -1 */}
      <Box mt="-md" />

      {/* margin-top: auto */}
      <Box mt="auto" />

      {/* margin-top: 1rem */}
      <Box mt={16} />

      {/* margin-top: 5rem */}
      <Box mt="5rem" />
    </>
  );
}
```

```python
import { Box } from '@mantine/core';

function Demo() {
  return (
    <>
      {/* color: theme.colors.blue[theme.primaryShade] */}
      <Box c="blue" />

      {/* background: theme.colors.orange[1] */}
      <Box bg="orange.1" />

      {/* border: 1px solid theme.colors.red[6] */}
      <Box bd="1px solid red.6" />

      {/* color: if colorScheme is dark `var(--mantine-color-dark-2)`,
      if color scheme is light `var(--mantine-color-gray-6)` */}
      <Box c="dimmed" />

      {/* color
...
```

---

## Styles API | Mantine

**URL**: https://mantine.dev/styles/styles-api/

**Contents**:
- Styles API
- What is Styles API
- Styles API selectors
- classNames prop
- classNames in theme.components
- Components CSS variables
- styles prop
- Styles API based on component props

The styles API is a set of props and techniques that allows you to customize the style of any element inside a Mantine component – inline or using the theme object. All Mantine components that have styles support Styles API.

Every Mantine component that supports the styles API has a set of element names that can be used to apply styles to inner elements inside the component. For simplicity, these elements names are called selectors in Mantine documentation. You can find selectors information under the Styles API tab in a component's documentation.

Example of Button component selectors:

You can use these selectors in classNames and styles in, both, component props and theme.components:

With the classNames prop you can add classes to inner elements of Mantine components. It accepts an object with element names as keys and classes as values:

You can also define classNames in theme.components to apply them to all components of a specific type:

Most of Mantine components use CSS variables to define colors, sizes, paddings and other properties. You can override these values using a custom CSS variables resolver function in theme.components or by passing it to the vars prop.

You can find CSS variables information under the Styles API tab in a component's documentation. Example of Button component CSS variables:

Example of a custom CSS variables resolver function used to add more sizes to the Button component:

The styles prop works the same way as classNames, but applies inline styles. Note that inline styles have higher specificity than classes, so you will not be able to override them with classes without using !important. You cannot use pseudo-classes (for example, :hover, :first-of-type) and media queries inside the styles prop.

Some examples and demos in the documentation use the styles prop for convenience, but it is not recommended to use the styles prop as the primary means of styling components, as the classNames prop is more flexible and has better perfo

*[Content truncated - see full docs]*

**Examples**:

```python
import { Button, createTheme, MantineProvider } from '@mantine/core';

function ClassNamesDemo() {
  return (
    <Button
      classNames={{
        root: 'my-root-class',
        label: 'my-label-class',
        inner: 'my-inner-class',
      }}
    >
      Button
    </Button>
  );
}

function StylesDemo() {
  return (
    <Button
      styles={{
        root: { backgroundColor: 'red' },
        label: { color: 'blue' },
        inner: { fontSize: 20 },
      }}
    >
      Button
    </Butto
...
```

```python
import { useState } from 'react';
import { TextInput } from '@mantine/core';
import classes from './Demo.module.css';

function Demo() {
  const [value, setValue] = useState('');
  const [focused, setFocused] = useState(false);
  const floating = focused || value.length > 0 || undefined;

  return (
    <TextInput
      label="Floating label input"
      labelProps={{ 'data-floating': floating }}
      classNames={{
        root: classes.root,
        input: classes.input,
        label: classes
...
```

```python
import { useState } from 'react';
import {
  createTheme,
  MantineProvider,
  TextInput,
} from '@mantine/core';
// Styles are the same as in previous example
import classes from './Demo.module.css';

const theme = createTheme({
  components: {
    TextInput: TextInput.extend({
      classNames: {
        root: classes.root,
        input: classes.input,
        label: classes.label,
      },
    }),
  },
});

function Demo() {
  return (
    <MantineProvider theme={theme}>
      {/* Your app h
...
```

---

## Styles overview | Mantine

**URL**: https://mantine.dev/styles/styles-overview/

**Contents**:
- Styles overview
- Component specific props
- Style props
- Style prop
- CSS modules
- Theme tokens

This guide will help you understand how to apply styles to Mantine and custom components.

Most of the components provide props that allow you to customize their styles. For example, Button component has color, variant, size and radius props that control its appearance:

These props usually control multiple CSS properties, for example color and variant props control color, background-color and border properties. In most cases, changing components props is the most optimal way to customize Mantine components.

Style props work similar to component specific props, but with several differences:

Style props are useful when you need to change a single CSS property without creating a separate file for styles. Some of the most common use cases are:

Note that style props were never intended to be used as a primary way of styling components. In most cases, it is better to limit the number of style props used per component to 3-4. If you find yourself using more than 4 style props, consider creating a separate file with styles – it will be easier to maintain and will be more performant.

Style prop is supported by all Mantine components and allows setting CSS properties as well as CSS variables. It is useful in the following cases:

Style prop works the same way as React style prop. It is not recommended to use it as a primary way of styling components. In most cases, it is better to create a separate file with styles – it will be easier to maintain and will be more performant.

CSS modules is the recommended way of applying most of the styles to Mantine components. CSS modules are the most performant and flexible way of styling components.

You can reference Mantine theme values in any styles with CSS variables:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Button } from '@mantine/core';

function Demo() {
  return <Button variant="filled">Button</Button>;
}
```

```python
import { Text } from '@mantine/core';

function Demo() {
  return (
    <div>
      <Text c="blue.8" fz="lg">
        Card title
      </Text>
      <Text c="dimmed" fz="sm">
        Card description
      </Text>
    </div>
  );
}
```

```python
import { TextInput } from '@mantine/core';

function Demo() {
  return (
    <form>
      <TextInput label="First name" />
      <TextInput label="Last name" mt="md" />
      <TextInput label="Email" mt="md" />
    </form>
  );
}
```

---

## Styles performance | Mantine

**URL**: https://mantine.dev/styles/styles-performance/

**Contents**:
- Styles performance
- CSS modules
- Inline styles
- Style props
- Responsive style props
- Components responsive props

CSS modules is the most performant way to apply styles – this approach generates static CSS that is never re-evaluated. 99% of Mantine components styles are generated with CSS modules – components are optimized out of the box.

In most cases, it is recommended to use CSS modules to style your components as well. You can apply styles to HTML elements with className prop and to Mantine components with className, classNames props.

Applying styles with className:

Applying styles with classNames (see Styles API guide to learn more):

Inline styles (style and styles props) are less performant than CSS modules, but still performant enough to be used in most cases if it is your preferred way of styling in your project.

Inline styles caveats:

Example of inline styles:

Style props transform component props into inline styles. Style props have the same caveats as inline styles, it is not recommended to use them as the primary means of styling your components. Usually, style props are used to apply 1–3 styles to a component – using them this way does not impact performance.

Responsive style props have worse performance than regular style props because they require injecting <style /> tag next to the component. It is fine to use responsive style props to apply styles to several components, but it is not recommended to use them in large lists of components, for example, if you have 1000 inputs with responsive margins, it is better to refactor to use classNames prop:

Some components, like SimpleGrid and Grid rely on the same mechanism as responsive style props to apply styles. The limitations are the same – it is fine to use these several of these components on a page, but it is not recommended to use them in large lists of components.

Polymorphic components

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Box } from '@mantine/core';
import classes from './Demo.module.css';

function Demo() {
  return (
    <Box className={classes.box}>
      Box component with <span className={classes.highlight}>some styles</span>
    </Box>
  );
}
```

```python
import { useState } from 'react';
import { TextInput } from '@mantine/core';
import classes from './Demo.module.css';

function Demo() {
  const [value, setValue] = useState('');
  const [focused, setFocused] = useState(false);
  const floating = focused || value.length > 0 || undefined;

  return (
    <TextInput
      label="Floating label input"
      labelProps={{ 'data-floating': floating }}
      classNames={{
        root: classes.root,
        input: classes.input,
        label: classes
...
```

```python
import { Button } from '@mantine/core';

function Demo() {
  const gradient =
    'linear-gradient(45deg, var(--mantine-color-pink-filled) 0%, var(--mantine-color-orange-filled) 50%, var(--mantine-color-yellow-filled) 100%)';

  return (
    <Button
      radius="md"
      styles={{
        root: {
          padding: 2,
          border: 0,
          backgroundImage: gradient,
        },

        inner: {
          background: 'var(--mantine-color-body)',
          color: 'var(--mantine-color-te
...
```

---

## Theme object | Mantine

**URL**: https://mantine.dev/theming/theme-object/

**Contents**:
- Theme object
- Usage
- Theme properties
  - autoContrast
  - luminanceThreshold
  - focusRing
  - focusClassName
  - activeClassName

Mantine theme is an object where your application's colors, fonts, spacing, border-radius and other design tokens are stored.

To customize theme, pass theme override object to MantineProvider theme prop. Theme override will be deeply merged with the default theme.

autoContrast controls whether text color should be changed based on the given color prop in the following components:

autoContrast checks whether the given color luminosity is above or below the luminanceThreshold value and changes text color to either theme.white or theme.black accordingly.

autoContrast can be set globally on the theme level or individually for each component via autoContrast prop, except for Spotlight and @mantine/dates components which only support global theme setting.

luminanceThreshold controls which luminance value is used to determine if text color should be light or dark. It is used only if theme.autoContrast is set to true. Default value is 0.3.

theme.focusRing controls focus ring styles, it supports the following values:

theme.focusClassName is a CSS class that is added to elements that have focus styles, for example, Button or ActionIcon. It can be used to customize focus ring styles of all interactive components except inputs. Note that when theme.focusClassName is set, theme.focusRing is ignored.

:focus-visible selector

:focus-visible selector is supported by more than 91% of browsers (data from April 2023). Safari browsers added support for it in version 15.4 (released in March 2022). If you need to support Safari 15.3 and older, you can use focus-visible polyfill or provide a fallback with :focus pseudo-class.

theme.activeClassName is a CSS class that is added to elements that have active styles, for example, Button or ActionIcon. It can be used to customize active styles of all interactive components.

To disable active styles for all components, set theme.activeClassName to an empty string:

theme.defaultRadius controls the default border-radius property in most

*[Content truncated - see full docs]*

**Examples**:

```text
interface MantineTheme {
  /** Controls focus ring styles. Supports the following options:
   *  - `auto` – focus ring is displayed only when the user navigates with keyboard (default value)
   *  - `always` – focus ring is displayed when the user navigates with keyboard and mouse
   *  - `never` – focus ring is always hidden (not recommended)
   */
  focusRing: 'auto' | 'always' | 'never';

  /** rem units scale, change if you customize font-size of `<html />` element
   *  default value is `1`
...
```

```python
import { createTheme, MantineProvider } from '@mantine/core';

const theme = createTheme({
  colors: {
    // Add your color
    deepBlue: [
      '#eef3ff',
      '#dce4f5',
      '#b9c7e2',
      '#94a8d0',
      '#748dc1',
      '#5f7cb8',
      '#5474b4',
      '#44639f',
      '#39588f',
      '#2d4b81',
    ],
    // or replace default theme color
    blue: [
      '#eef3ff',
      '#dee2f2',
      '#bdc2de',
      '#98a0ca',
      '#7a84ba',
      '#6672b0',
      '#5c68ac',
      '#4c589
...
```

```python
import { Button, Code, Group } from '@mantine/core';

function Demo() {
  return (
    <>
      <Code>autoContrast: true</Code>
      <Group mt="xs" mb="lg">
        <Button color="lime.4" autoContrast>
          Lime.4 button
        </Button>
        <Button color="blue.2" autoContrast>
          Blue.2 button
        </Button>
        <Button color="orange.3" autoContrast>
          Orange.3 button
        </Button>
      </Group>

      <Code>autoContrast: false</Code>
      <Group mt="xs">

...
```

---

## Typography | Mantine

**URL**: https://mantine.dev/theming/typography/

**Contents**:
- Typography
- Typography
- Change fonts
  - Outfit or sans-serif title
- System fonts
- Font sizes
- Line heights
- h1-h6 styles

Styles provider for html content

You can change fonts and other text styles for headings, code and all other components with the following theme properties:

By default, Mantine uses system fonts. It means that different devices will display components based on available font, for example, macOS and iOS users will see San Francisco font, Windows users will see Segoe UI font, Android users will see Roboto font and so on. This approach provides a familiar experience to the users and allows avoiding common problems related to custom fonts loading (layout shift, invisible text, etc.), if you do not have strict requirements, it is recommended to use system fonts for better performance.

Default values for theme properties:

Paras is an orange, insectoid Pokémon that resembles the nymph stage of a cicada. Its ovoid body is segmented, and it has three pairs of legs. The foremost pair of legs is the largest and has sharp claws at the tips. There are five specks on its forehead and three teeth on either side of its mouth. It has circular eyes with large pseudopupils.

theme.fontSizes property defines font-size values for all Mantine components:

Default theme.fontSizes values:

theme.lineHeights property defines line-height values for Text component, most other components use theme.lineHeights.md by default:

Default theme.lineHeights values:

To customize headings styles in Title and Typography components set theme.headings:

With theme.headings you can customize font-size, font-weight and line-height per heading level. If you need more control over styles, use :is selector with Styles API to target specific heading level:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Button, Code, Title, MantineProvider, createTheme } from '@mantine/core';

const theme = createTheme({
  fontFamily: 'Verdana, sans-serif',
  fontFamilyMonospace: 'Monaco, Courier, monospace',
  headings: { fontFamily: 'Outfit, sans-serif' },
});

function Demo() {
  return (
    <MantineProvider theme={theme}>
      <Title order={3}>Outfit or sans-serif title</Title>
      <Button>Verdana button</Button>
      <Code>Monaco, Courier Code</Code>
    </MantineProvider>
  );
}
```

```python
import { Text } from '@mantine/core';

function Demo() {
  return (
    <Text fz="md" lh="md">
      Paras is an orange, insectoid Pokémon that resembles the nymph stage of a cicada. Its ovoid
      body is segmented, and it has three pairs of legs. The foremost pair of legs is the largest
      and has sharp claws at the tips. There are five specks on its forehead and three teeth on
      either side of its mouth. It has circular eyes with large pseudopupils.
    </Text>
  );
}
```

```python
import { createTheme, MantineProvider } from '@mantine/core';

const theme = createTheme({
  fontSizes: {
    xs: 10,
    sm: 11,
    md: 14,
    lg: 16,
    xl: 20,
  },
});

function Demo() {
  return (
    <MantineProvider theme={theme}>
      {/* Your app here */}
    </MantineProvider>
  );
}
```

---

## Unstyled / headless | Mantine

**URL**: https://mantine.dev/styles/unstyled/

**Contents**:
- Unstyled components
- Using Mantine as a headless UI library
- HeadlessMantineProvider
- unstyled prop

You can use Mantine as a headless UI library. To do that, simply do not import @mantine/*/styles.css in your application. Then you will be able to apply styles to Mantine components using Styles API with a styling solution of your choice.

HeadlessMantineProvider is an alternative to MantineProvider that should be used when you want to use Mantine as a headless UI library. It removes all features that are related to Mantine styles:

Limitations of HeadlessMantineProvider:

To use HeadlessMantineProvider, follow getting started guide and replace MantineProvider with HeadlessMantineProvider. Note that you do not need to use ColorSchemeScript in your application, it will not have any effect, you can ignore this part of the guide.

Most of Mantine components support unstyled prop that removes library styles from the component and allows you to style it from scratch. Note that unstyled prop is not supported by compound components (Tabs.Tab, Menu.Dropdown, Accordion.Control, etc.) – it only works on root component (Tabs, Menu, Accordion, etc.).

Unstyled Tabs component:

Choosing between unstyled prop and headless components

unstyled prop is useful when you want to remove library styles from a single component, but keep styles for other components. For example, if Tabs component does not meet your design system requirements, but all other components do, you can use unstyled prop to remove styles from Tabs and style it from scratch, while keeping all other components styled with Mantine styles.

Note that unstyled prop does not remove Mantine library styles from your .css bundle – it only does not apply them to component with unstyled prop.

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { HeadlessMantineProvider } from '@mantine/core';

function App() {
  return (
    <HeadlessMantineProvider>
      {/* Your application */}
    </HeadlessMantineProvider>
  );
}
```

```python
import { Tabs } from '@mantine/core';

function Demo() {
  return (
    <Tabs defaultValue="chat" unstyled>
      <Tabs.List>
        <Tabs.Tab value="chat">Chat</Tabs.Tab>
        <Tabs.Tab value="gallery">Gallery</Tabs.Tab>
        <Tabs.Tab value="account">Account</Tabs.Tab>
      </Tabs.List>

      <Tabs.Panel value="chat">Chat panel</Tabs.Panel>
      <Tabs.Panel value="gallery">Gallery panel</Tabs.Panel>
      <Tabs.Panel value="account">Account panel</Tabs.Panel>
    </Tabs>
  );
}
```

---

## Usage with Sass | Mantine

**URL**: https://mantine.dev/styles/sass/

**Contents**:
- Usage with Sass
- Sass modules
- Usage with Vite
- Usage with Next.js

This guide will explain how to use Sass in combination with postcss-preset-mantine. Note that examples on mantine.dev website use only postcss-preset-mantine – you will need to modify them to use with Sass.

You can use Sass modules the same way as CSS modules:

Add mantine resources in your vite.config.js file:

Create src/_mantine.scss file:

All done! you can now use breakpoint variables, rem function, hover, light/dark mixins:

Add mantine resources in your next.config.mjs file:

Create _mantine.scss file in the root folder of your project:

All done! you can now use breakpoint variables, rem function, hover, light/dark mixins:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```text
yarn add --dev sass-embedded
```

```text
npm install --save-dev sass-embedded
```

```python
import path from 'node:path';
import react from '@vitejs/plugin-react';
import { defineConfig } from 'vite';

export default defineConfig({
  plugins: [react()],
  css: {
    preprocessorOptions: {
      scss: {
        api: 'modern-compiler',
        additionalData: `@use "${path.join(process.cwd(), 'src/_mantine').replace(/\\/g, '/')}" as mantine;`,
      },
    },
  },
});
```

---

## Vanilla extract | Mantine

**URL**: https://mantine.dev/styles/vanilla-extract/

**Contents**:
- Vanilla extract integration
- Vanilla extract vs CSS Modules
- Installation
- Templates
- Theming
- Styling
- rem and em
- light and dark selectors

Vanilla extract is a TypeScript CSS preprocessor that generates static CSS files at build time. It is a great alternative to CSS Modules if you prefer to write your styles in TypeScript.

Vanilla extract and CSS Modules do the same thing, but with different syntax. Common features of Vanilla extract and CSS Modules:

Differences between Vanilla extract and CSS Modules:

Note that you can use both Vanilla extract and CSS Modules in the same project, it will not cause any issues: performance will be the same and the bundle size will not be impacted.

Follow the installation instructions to install vanilla extract. Then install @mantine/vanilla-extract package, it exports themeToVars function to convert Mantine theme to CSS variables:

You can use one of the following templates to get started or a reference for your own setup. Note that all templates include only minimal setup.

next-vanilla-extract-template

Next.js template with Vanilla extract example

vite-vanilla-extract-template

Vite template with Vanilla extract example

Vanilla extract provides createTheme function which converts given theme object into CSS variables and assigns them to :root or other selector. You should not use Vanilla extract createTheme to generate Mantine theme tokens – all Mantine theme properties are already exposed as CSS variables. Instead, use themeToVars function from @mantine/vanilla-extract package to create an object with CSS variables from Mantine theme:

Import vars object in *.css.ts files to access Mantine CSS variables:

To convert px to rem or em use rem and em functions from @mantine/core package:

vars object contains lightSelector and darkSelector properties which can be used to apply styles only in light or dark color scheme:

Note that usually it is more convenient to use only one of them: apply styles for light color scheme and then override them for dark color scheme with vars.darkSelector (or vice versa):

vars object contains largerThan and smallerThan properties w

*[Content truncated - see full docs]*

**Examples**:

```text
yarn add @mantine/vanilla-extract
```

```text
npm install @mantine/vanilla-extract
```

```python
// theme.ts
import { createTheme } from '@mantine/core';

// Do not forget to pass theme to MantineProvider
export const theme = createTheme({
  fontFamily: 'serif',
  primaryColor: 'cyan',
});
```

---

## Variants and sizes | Mantine

**URL**: https://mantine.dev/styles/variants-sizes/

**Contents**:
- Variants and sizes
- Adding custom variants
- Custom variants types
- variantColorResolver
- Sizes with components CSS variables
- Sizes with data-size attribute
- Sizes with static CSS variables

Most of Mantine components support variant prop, it can be used in CSS variables resolver, and it is also exposed as data-variant="{value}" attribute on the root element of the component. The easiest way to add custom variants is to add styles that use [data-variant="{value}"].

Example of adding a new variant to the Input component:

Note that you can add custom variants to every Mantine component that supports Styles API even if there are no variants defined on the library side.

Overriding existing variants styles

Apart from adding new variants, you can also override existing ones, for example, you can change the filled variant of the Input component with .input[data-variant="filled"] selector.

You can define types for custom variants by creating mantine.d.ts file in your project and extending {x}Props interface with the new variant type.

Example of adding custom variant type to Button component:

Button, Badge, ActionIcon and other components support custom variants with variantColorResolver – it supports both changing colors and adding new variants. Note that theme.variantColorResolver is responsible only for colors, if you need to change other properties, use data-variant attribute.

You can add custom sizes to any component that supports size prop by providing a custom CSS variables resolver, usually it is done in theme.components:

Every component that supports size prop exposes it as data-size="{value}" attribute on the root element. You can use it to add custom sizes:

Mantine components sizes are defined with CSS variables (usually on root element), for example, ActionIcon component has the following CSS variables:

You can override these values with Styles API or add new sizes values:

Note that some components have more than one CSS variable for size, for example, the Button component has the following CSS variables:

Usually, it is more convenient to use data-size attribute or vars on theme to customize sizes in this case.

Build fully functional ac

*[Content truncated - see full docs]*

**Examples**:

```python
import { Input, MantineProvider, createTheme } from '@mantine/core';
import classes from './Demo.module.css';

// It is better to add new variants in theme.components
// This way you will be able to use them in anywhere in the app
const theme = createTheme({
  components: {
    Input: Input.extend({ classNames: classes }),
  }
});

function Demo() {
  return (
    <MantineProvider theme={theme}>
      <Input variant="underline" placeholder="Underline input" />
      <Input variant="filled" place
...
```

```python
import { ButtonVariant, MantineSize } from '@mantine/core';

type ExtendedButtonVariant = ButtonVariant | 'contrast' | 'radial-gradient';

declare module '@mantine/core' {
  export interface ButtonProps {
    variant?: ExtendedButtonVariant;
  }
}
```

```python
import {
  Button,
  Group,
  MantineProvider,
  defaultVariantColorsResolver,
  VariantColorsResolver,
  parseThemeColor,
  rgba,
  darken,
} from '@mantine/core';

const variantColorResolver: VariantColorsResolver = (input) => {
  const defaultResolvedColors = defaultVariantColorsResolver(input);
  const parsedColor = parseThemeColor({
    color: input.color || input.theme.primaryColor,
    theme: input.theme,
  });

  // Override some properties for variant
  if (parsedColor.isThemeColor && p
...
```

---

## data-* attributes | Mantine

**URL**: https://mantine.dev/styles/data-attributes/

**Contents**:
- data attributes
- data attributes values
- Components data attributes documentation
- mod prop

Mantine components use data-* attributes to apply styles. These attributes are used as a modifier to apply styles based on component state. General rule of Mantine components styles: one class with shared styles and any number of data-* attributes as modifiers.

Example of applying styles with data-* attributes:

Most of the data-* attributes do not have associated values, they represent boolean state or a feature. For example, when the disabled prop on Button is set, the data-disabled attribute is added to the <button /> element:

Will output the following HTML:

You can then use this attribute to apply styles to the disabled button:

When the disabled prop is not set, then the data-disabled attribute is not added to the button:

In some cases, data-* attributes have associated values, for example, a Button component's section element has an associated data-position attribute which can be left or right. The following example will render two section elements, one with data-position="left" and another with data-position="right":

Will output the following HTML:

You can then use this attribute to apply styles to the left and right sections:

Every component that uses data-* attributes has a dedicated section under the Styles API tab.

Button component data-* attributes table:

How to read the table:

All components support mod prop, which allows adding data attributes to the root element:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```text
.root {
  border-top-left-radius: var(--mantine-radius-xl);
  border-bottom-left-radius: var(--mantine-radius-xl);
  padding-left: 4px;

  /* The following styles will be applied only when button is disabled */
  &[data-disabled] {
    /* You can use Mantine PostCSS mixins inside data attributes */
    @mixin light {
      border: 1px solid var(--mantine-color-gray-2);
    }

    @mixin dark {
      border: 1px solid var(--mantine-color-dark-4);
    }

    /* You can target child elements that a
...
```

```python
import { Button } from '@mantine/core';

function Demo() {
  return (
    <Button disabled className="my-button">
      Disabled button
    </Button>
  );
}
```

```text
<button class="my-button" data-disabled>Disabled button</button>
```

---

## rem, em and px units | Mantine

**URL**: https://mantine.dev/styles/rem/

**Contents**:
- rem, em and px units
- rem units
- rem units scaling
- em units
- px conversions
- rem and em function
- Convert rem to px
- rem/em functions in css files

All Mantine components use rem units to apply size styles (margin, padding, width, etc.). By default, 1rem is considered to be 16px as it is a default setting in most browsers. All components scale based on the user's browser font-size settings or font-size of html/:root.

If you want to change font-size of :root/html element and preserve Mantine components sizes, set scale on theme to the value of 1 / htmlFontSize.

For example, if you set html font-size to 10px and want to scale Mantine components accordingly, you need to set scale to 1 / (10 / 16) (16 – default font-size) = 1 / 0.625 = 1.6:

em units are used in media queries the same way as rem units, but they are not affected by font-size specified on html/:root element. 1em is considered to be 16px.

You can use numbers in some Mantine components props. Numbers are treated as px and converted to rem, for example:

The same conversion happens in style props:

@mantine/core package exports rem and em function that can be used to convert px into rem/em:

To convert rem/em to px use px function exported from @mantine/core:

You can use rem and em function in css files if postcss-preset-mantine is installed:

To convert px to rem automatically in css files, enable autoRem option in postcss-preset-mantine configuration:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Slider } from '@mantine/core';

function Demo() {
  return (
    <Slider
      defaultValue={100}
      min={70}
      max={130}
      onChange={(value) => {
        document.documentElement.style.fontSize = `${value}%`;
      }}
    />
  );
}
```

```text
:root {
  font-size: 10px;
}
```

```python
import { createTheme, MantineProvider } from '@mantine/core';

const theme = createTheme({
  scale: 1.6,
});

function Demo() {
  return (
    <MantineProvider theme={theme}>
      {/* Your app here */}
    </MantineProvider>
  );
}
```

---

## style prop | Mantine

**URL**: https://mantine.dev/styles/style/

**Contents**:
- Style prop
- Style object
- Define CSS variables in style prop
- Style function
- Styles array

All Mantine components that have root element support style prop. It works similar to React style prop, but with some additional features.

You can pass a style object to the style prop – in this case it works the same way as React style prop. You can use Mantine CSS variables in style object the same way as in .css files.

You can define CSS variables in the style prop. Note that it only works with Mantine components:

You can pass a style function to the style prop – in this case it will be called with theme. It is useful when you need to access theme properties that are not exposed as CSS variables, for example, properties from theme.other.

You can pass an array of style objects and/or functions to style prop – in this case, all styles will be merged into one object. It is useful when you want to create a wrapper around Mantine component, add inline styles and keep the option to pass style prop to it.

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Box, rem } from '@mantine/core';

function Demo() {
  return (
    <Box
      style={{
        color: 'var(--mantine-color-red-5)',
        fontSize: rem(12),
      }}
    />
  );
}
```

```python
import { Box } from '@mantine/core';

function Demo() {
  return (
    <Box
      style={{ '--radius': '0.5rem', borderRadius: 'var(--radius)' }}
    />
  );
}
```

```python
import { Box } from '@mantine/core';

function Demo() {
  return (
    <Box
      style={(theme) => ({
        color: theme.colors.red[5],
        fontSize: theme.fontSizes.xs,
      })}
    />
  );
}
```

---
