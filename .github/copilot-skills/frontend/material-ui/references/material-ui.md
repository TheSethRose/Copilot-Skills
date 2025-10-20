# Material-Ui - Material-Ui

**Pages**: 15

---

## Example projects - Material UI

**URL**: https://mui.com/material-ui/getting-started/example-projects/

**Contents**:
- Example projects
- Official integrations
- Free templates
- Premium themes and templates

A collection of examples and scaffolds integrating Material UI with popular libraries and frameworks.

The following integration examples are available in the /examples folder of the Material UI GitHub repository. These examples feature Material UI paired with other popular React libraries and frameworks, so you can skip the initial setup steps and jump straight into building.

Not sure which to pick? We recommend Next.js for server-side rendering and more opinionated framework features, or Vite for a lightweight single-page app (SPA). See Creating a React App from the official React docs to learn more about some of the options available.

Express.js (server-rendered)

Once you've chosen your preferred scaffold above, you could move on to our collection of free templates and install a readymade user interface to get started even faster.

For more complex prebuilt UIs, check out our premium themes and templates in the MUI Store.

Was this page helpful?

---

## How to customize - Material UI

**URL**: https://mui.com/material-ui/customization/how-to-customize/

**Contents**:
- How to customize
- 1. One-off customization
  - The sx prop
  - Overriding nested component styles
  - Overriding styles with class names
  - State classes
    - Why do I need to increase specificity to override one component state?
    - What custom state classes are available in Material UI?

Learn how to customize Material UI components by taking advantage of different strategies for specific use cases.

Material UI provides several different ways to customize a component's styles. Your specific context will determine which one is ideal. From narrowest to broadest use case, here are the options:

To change the styles of one single instance of a component, you can use one of the following options:

The sx prop is the best option for adding style overrides to a single instance of a component in most cases. It can be used with all Material UI components.

To customize a specific part of a component, you can use the class name provided by Material UI inside the sx prop. As an example, let's say you want to change the Slider component's thumb from a circle to a square.

First, use your browser's dev tools to identify the class for the component slot you want to override.

The styles injected into the DOM by Material UI rely on class names that all follow a standard pattern: [hash]-Mui[Component name]-[name of the slot].

In this case, the styles are applied with .css-ae2u5c-MuiSlider-thumb but you only really need to target the .MuiSlider-thumb, where Slider is the component and thumb is the slot. Use this class name to write a CSS selector within the sx prop (& .MuiSlider-thumb), and add your overrides.

These class names can't be used as CSS selectors because they are unstable.

If you want to override a component's styles using custom classes, you can use the className prop, available on each component. To override the styles of a specific part of the component, use the global classes provided by Material UI, as described in the previous section "Overriding nested component styles" under the sx prop section.

Visit the Style library interoperability guide to find examples of this approach using different styling libraries.

States like hover, focus, disabled and selected, are styled with a higher CSS specificity. To customize them, you'll need to increase

*[Content truncated - see full docs]*

**Examples**:

```tsx
<Slider defaultValue={30} sx={{ width: 300, color: 'success.main' }} />
```

```tsx
<Slider
  defaultValue={30}
  sx={{
    width: 300,
    color: 'success.main',
    '& .MuiSlider-thumb': {
      borderRadius: '1px',
    },
  }}
/>
```

```css
.Button {
  color: black;
}

/* Increase the specificity */
.Button:disabled {
  color: white;
}
```

---

## Installation - Material UI

**URL**: https://mui.com/material-ui/getting-started/installation/

**Contents**:
- Installation
- Default installation
  - Peer dependencies
  - React 18 and below
    - Why is this needed?
- With styled-components
- Roboto font
  - Google Web Fonts

Install Material UI, the world's most popular React UI framework.

Run one of the following commands to add Material UI to your project:

Please note that react and react-dom are peer dependencies, meaning you should ensure they are installed before installing Material UI.

If you are using React 18 or below, you need to set up a resolution of react-is package to the same version as the react you are using.

For example, if you are using react@18.3.1, do the following steps:

Material UI uses react-is@19, which changed how React elements are identified.

If you're on React 18 or below, mismatched versions of react-is can cause runtime errors in prop type checks. Forcing react-is to match your React version prevents these errors.

Material UI uses Emotion as its default styling engine. If you want to use styled-components instead, run one of the following commands:

Next, follow the styled-components how-to guide to properly configure your bundler to support @mui/styled-engine-sc.

As of late 2021, styled-components is not compatible with server-rendered Material UI projects. This is because babel-plugin-styled-components isn't able to work with the styled() utility inside @mui packages. See this GitHub issue for more details.

We strongly recommend using Emotion for SSR projects.

Material UI uses the Roboto font by default. Add it to your project via Fontsource, or with the Google Fonts CDN.

Then you can import it in your entry point like this:

Fontsource can be configured to load specific subsets, weights and styles. Material UI's default typography configuration relies only on the 300, 400, 500, and 700 font weights.

To install Roboto through the Google Web Fonts CDN, add the following code inside your project's <head /> tag:

To use the font Icon component or the prebuilt SVG Material Icons (such as those found in the icon demos), you must first install the Material Icons font. You can do so with npm, or with the Google Web Fonts CDN.

To install the Material

*[Content truncated - see full docs]*

**Examples**:

```bash
npm install @mui/material @emotion/react @emotion/styled
```

```json
"peerDependencies": {
  "react": "^17.0.0 || ^18.0.0 || ^19.0.0",
  "react-dom": "^17.0.0 || ^18.0.0 || ^19.0.0"
},
```

```bash
npm install react-is@18.3.1
```

---

## New Free React Templates - Material UI

**URL**: https://mui.com/material-ui/getting-started/templates/

**Contents**:
- React templates
- Free templates
  - Dashboard
  - Marketing page
  - Checkout
  - Sign-in
  - Sign-in side
  - Sign-up

Browse our collection of free React templates to get started building your app with Material UI, including a React dashboard, React marketing page, and more.

Our curated collection of free Material UI templates includes a dashboard, a marketing page, a checkout flow, sign-in and sign-up pages, and a blog. You can download each one directly from the source code or via CodeSandbox or StackBlitz.

All templates feature a custom theme and a default Material Design 2 theme, with light and dark modes for both. You can toggle through each of these style options in the top right corner of the live previews.

Sections of each layout are defined either by comments or use of separate files, so you can extract parts of a page (such as a hero unit or a footer) for reuse in other pages. These templates can be combined with one of the example projects to form a complete starter app.

If you see any room for improvement, please feel free to open an issue or a pull request on GitHub.

A complex data visualization dashboard featuring the MUI X Data Grid and Charts.

A responsive marketing page layout with sections for product features, testimonials, pricing, and FAQs.

A sophisticated checkout flow with fully customizable steps.

A clean and efficient sign-in page, ready for your favorite auth provider.

A responsive, two-column sign-in page for adding content alongside the form.

A clean and efficient sign-up page, perfect for pairing with a sign-in template.

A sleek, modern blog homepage layout with Markdown support via markdown-to-jsx.

Dashboard with CRUD pages and mobile-friendly layout with highly customizable sidebar.

Looking for something more? You can find complete templates and themes like those shown below in the premium template section of the MUI Store.

Was this page helpful?

---

## Overview - Material UI

**URL**: https://mui.com/material-ui/getting-started/overview/#introduction

**Contents**:
- Material UI - Overview
- Introduction
- Advantages of Material UI
  - Material UI vs. MUI Base
- Start now
  - Installation
  - Usage
  - Example projects

Material UI is an open-source React component library that implements Google's Material Design. It's comprehensive and can be used in production out of the box.

Material UI is an open-source React component library that implements Google's Material Design.

It includes a comprehensive collection of prebuilt components that are ready for use in production right out of the box and features a suite of customization options that make it easy to implement your own custom design system on top of our components.

Material UI supports Material Design 2. You can follow this GitHub issue for future design-related updates.

Material UI and MUI Base feature many of the same UI components, but MUI Base comes without any default styles or styling solutions.

Material UI is comprehensive in that it comes packaged with default styles, and is optimized to work with Emotion (or styled-components).

MUI Base, by contrast, could be considered the "skeletal" or "headless" counterpart to Material UI—in fact, future versions of Material UI will use MUI Base components and hooks for its foundational structure.

Get started with Material UI today through some of these useful resources:

Add Material UI to your project with a few commands.

Learn the basics about Material UI components.

A collection of boilerplates to jumpstart your next project.

Learn about the available customization methods.

Get started with a selection of free templates.

The Material UI components in your favorite design tool.

Was this page helpful?

---

## Overview - Material UI

**URL**: https://mui.com/material-ui/getting-started/#start-now

**Contents**:
- Material UI - Overview
- Introduction
- Advantages of Material UI
  - Material UI vs. MUI Base
- Start now
  - Installation
  - Usage
  - Example projects

Material UI is an open-source React component library that implements Google's Material Design. It's comprehensive and can be used in production out of the box.

Material UI is an open-source React component library that implements Google's Material Design.

It includes a comprehensive collection of prebuilt components that are ready for use in production right out of the box and features a suite of customization options that make it easy to implement your own custom design system on top of our components.

Material UI supports Material Design 2. You can follow this GitHub issue for future design-related updates.

Material UI and MUI Base feature many of the same UI components, but MUI Base comes without any default styles or styling solutions.

Material UI is comprehensive in that it comes packaged with default styles, and is optimized to work with Emotion (or styled-components).

MUI Base, by contrast, could be considered the "skeletal" or "headless" counterpart to Material UI—in fact, future versions of Material UI will use MUI Base components and hooks for its foundational structure.

Get started with Material UI today through some of these useful resources:

Add Material UI to your project with a few commands.

Learn the basics about Material UI components.

A collection of boilerplates to jumpstart your next project.

Learn about the available customization methods.

Get started with a selection of free templates.

The Material UI components in your favorite design tool.

Was this page helpful?

---

## Overview - Material UI

**URL**: https://mui.com/material-ui/getting-started/overview/#start-now

**Contents**:
- Material UI - Overview
- Introduction
- Advantages of Material UI
  - Material UI vs. MUI Base
- Start now
  - Installation
  - Usage
  - Example projects

Material UI is an open-source React component library that implements Google's Material Design. It's comprehensive and can be used in production out of the box.

Material UI is an open-source React component library that implements Google's Material Design.

It includes a comprehensive collection of prebuilt components that are ready for use in production right out of the box and features a suite of customization options that make it easy to implement your own custom design system on top of our components.

Material UI supports Material Design 2. You can follow this GitHub issue for future design-related updates.

Material UI and MUI Base feature many of the same UI components, but MUI Base comes without any default styles or styling solutions.

Material UI is comprehensive in that it comes packaged with default styles, and is optimized to work with Emotion (or styled-components).

MUI Base, by contrast, could be considered the "skeletal" or "headless" counterpart to Material UI—in fact, future versions of Material UI will use MUI Base components and hooks for its foundational structure.

Get started with Material UI today through some of these useful resources:

Add Material UI to your project with a few commands.

Learn the basics about Material UI components.

A collection of boilerplates to jumpstart your next project.

Learn about the available customization methods.

Get started with a selection of free templates.

The Material UI components in your favorite design tool.

Was this page helpful?

---

## Overview - Material UI

**URL**: https://mui.com/material-ui/getting-started/#advantages-of-material-ui

**Contents**:
- Material UI - Overview
- Introduction
- Advantages of Material UI
  - Material UI vs. MUI Base
- Start now
  - Installation
  - Usage
  - Example projects

Material UI is an open-source React component library that implements Google's Material Design. It's comprehensive and can be used in production out of the box.

Material UI is an open-source React component library that implements Google's Material Design.

It includes a comprehensive collection of prebuilt components that are ready for use in production right out of the box and features a suite of customization options that make it easy to implement your own custom design system on top of our components.

Material UI supports Material Design 2. You can follow this GitHub issue for future design-related updates.

Material UI and MUI Base feature many of the same UI components, but MUI Base comes without any default styles or styling solutions.

Material UI is comprehensive in that it comes packaged with default styles, and is optimized to work with Emotion (or styled-components).

MUI Base, by contrast, could be considered the "skeletal" or "headless" counterpart to Material UI—in fact, future versions of Material UI will use MUI Base components and hooks for its foundational structure.

Get started with Material UI today through some of these useful resources:

Add Material UI to your project with a few commands.

Learn the basics about Material UI components.

A collection of boilerplates to jumpstart your next project.

Learn about the available customization methods.

Get started with a selection of free templates.

The Material UI components in your favorite design tool.

Was this page helpful?

---

## Overview - Material UI

**URL**: https://mui.com/material-ui/getting-started/overview/#advantages-of-material-ui

**Contents**:
- Material UI - Overview
- Introduction
- Advantages of Material UI
  - Material UI vs. MUI Base
- Start now
  - Installation
  - Usage
  - Example projects

Material UI is an open-source React component library that implements Google's Material Design. It's comprehensive and can be used in production out of the box.

Material UI is an open-source React component library that implements Google's Material Design.

It includes a comprehensive collection of prebuilt components that are ready for use in production right out of the box and features a suite of customization options that make it easy to implement your own custom design system on top of our components.

Material UI supports Material Design 2. You can follow this GitHub issue for future design-related updates.

Material UI and MUI Base feature many of the same UI components, but MUI Base comes without any default styles or styling solutions.

Material UI is comprehensive in that it comes packaged with default styles, and is optimized to work with Emotion (or styled-components).

MUI Base, by contrast, could be considered the "skeletal" or "headless" counterpart to Material UI—in fact, future versions of Material UI will use MUI Base components and hooks for its foundational structure.

Get started with Material UI today through some of these useful resources:

Add Material UI to your project with a few commands.

Learn the basics about Material UI components.

A collection of boilerplates to jumpstart your next project.

Learn about the available customization methods.

Get started with a selection of free templates.

The Material UI components in your favorite design tool.

Was this page helpful?

---

## Overview - Material UI

**URL**: https://mui.com/material-ui/getting-started/#material-ui-vs-mui-base

**Contents**:
- Material UI - Overview
- Introduction
- Advantages of Material UI
  - Material UI vs. MUI Base
- Start now
  - Installation
  - Usage
  - Example projects

Material UI is an open-source React component library that implements Google's Material Design. It's comprehensive and can be used in production out of the box.

Material UI is an open-source React component library that implements Google's Material Design.

It includes a comprehensive collection of prebuilt components that are ready for use in production right out of the box and features a suite of customization options that make it easy to implement your own custom design system on top of our components.

Material UI supports Material Design 2. You can follow this GitHub issue for future design-related updates.

Material UI and MUI Base feature many of the same UI components, but MUI Base comes without any default styles or styling solutions.

Material UI is comprehensive in that it comes packaged with default styles, and is optimized to work with Emotion (or styled-components).

MUI Base, by contrast, could be considered the "skeletal" or "headless" counterpart to Material UI—in fact, future versions of Material UI will use MUI Base components and hooks for its foundational structure.

Get started with Material UI today through some of these useful resources:

Add Material UI to your project with a few commands.

Learn the basics about Material UI components.

A collection of boilerplates to jumpstart your next project.

Learn about the available customization methods.

Get started with a selection of free templates.

The Material UI components in your favorite design tool.

Was this page helpful?

---

## Overview - Material UI

**URL**: https://mui.com/material-ui/getting-started/overview/#material-ui-vs-mui-base

**Contents**:
- Material UI - Overview
- Introduction
- Advantages of Material UI
  - Material UI vs. MUI Base
- Start now
  - Installation
  - Usage
  - Example projects

Material UI is an open-source React component library that implements Google's Material Design. It's comprehensive and can be used in production out of the box.

Material UI is an open-source React component library that implements Google's Material Design.

It includes a comprehensive collection of prebuilt components that are ready for use in production right out of the box and features a suite of customization options that make it easy to implement your own custom design system on top of our components.

Material UI supports Material Design 2. You can follow this GitHub issue for future design-related updates.

Material UI and MUI Base feature many of the same UI components, but MUI Base comes without any default styles or styling solutions.

Material UI is comprehensive in that it comes packaged with default styles, and is optimized to work with Emotion (or styled-components).

MUI Base, by contrast, could be considered the "skeletal" or "headless" counterpart to Material UI—in fact, future versions of Material UI will use MUI Base components and hooks for its foundational structure.

Get started with Material UI today through some of these useful resources:

Add Material UI to your project with a few commands.

Learn the basics about Material UI components.

A collection of boilerplates to jumpstart your next project.

Learn about the available customization methods.

Get started with a selection of free templates.

The Material UI components in your favorite design tool.

Was this page helpful?

---

## Overview - Material UI

**URL**: https://mui.com/material-ui/getting-started/overview/

**Contents**:
- Material UI - Overview
- Introduction
- Advantages of Material UI
  - Material UI vs. MUI Base
- Start now
  - Installation
  - Usage
  - Example projects

Material UI is an open-source React component library that implements Google's Material Design. It's comprehensive and can be used in production out of the box.

Material UI is an open-source React component library that implements Google's Material Design.

It includes a comprehensive collection of prebuilt components that are ready for use in production right out of the box and features a suite of customization options that make it easy to implement your own custom design system on top of our components.

Material UI supports Material Design 2. You can follow this GitHub issue for future design-related updates.

Material UI and MUI Base feature many of the same UI components, but MUI Base comes without any default styles or styling solutions.

Material UI is comprehensive in that it comes packaged with default styles, and is optimized to work with Emotion (or styled-components).

MUI Base, by contrast, could be considered the "skeletal" or "headless" counterpart to Material UI—in fact, future versions of Material UI will use MUI Base components and hooks for its foundational structure.

Get started with Material UI today through some of these useful resources:

Add Material UI to your project with a few commands.

Learn the basics about Material UI components.

A collection of boilerplates to jumpstart your next project.

Learn about the available customization methods.

Get started with a selection of free templates.

The Material UI components in your favorite design tool.

Was this page helpful?

---

## Overview - Material UI

**URL**: https://mui.com/material-ui/getting-started/#introduction

**Contents**:
- Material UI - Overview
- Introduction
- Advantages of Material UI
  - Material UI vs. MUI Base
- Start now
  - Installation
  - Usage
  - Example projects

Material UI is an open-source React component library that implements Google's Material Design. It's comprehensive and can be used in production out of the box.

Material UI is an open-source React component library that implements Google's Material Design.

It includes a comprehensive collection of prebuilt components that are ready for use in production right out of the box and features a suite of customization options that make it easy to implement your own custom design system on top of our components.

Material UI supports Material Design 2. You can follow this GitHub issue for future design-related updates.

Material UI and MUI Base feature many of the same UI components, but MUI Base comes without any default styles or styling solutions.

Material UI is comprehensive in that it comes packaged with default styles, and is optimized to work with Emotion (or styled-components).

MUI Base, by contrast, could be considered the "skeletal" or "headless" counterpart to Material UI—in fact, future versions of Material UI will use MUI Base components and hooks for its foundational structure.

Get started with Material UI today through some of these useful resources:

Add Material UI to your project with a few commands.

Learn the basics about Material UI components.

A collection of boilerplates to jumpstart your next project.

Learn about the available customization methods.

Get started with a selection of free templates.

The Material UI components in your favorite design tool.

Was this page helpful?

---

## Sponsors and Backers - Material UI

**URL**: https://mui.com/material-ui/discover-more/backers/#diamond-sponsors

**Contents**:
- Sponsors and Backers
- Diamond sponsors
- Gold sponsors
- Silver sponsors
- Bronze sponsors
- Backers
- FAQ
  - Why is Material UI a "crowd-funded open-source project"?

Support the development of the open-source projects of the MUI organization through crowdfunding.

Material UI, MUI Base, MUI System, and Joy UI are crowd-funded open-source projects, licensed under the permissive MIT license. Sponsorship increases the rate of bug fixes, documentation improvements, and feature development.

Diamond sponsors are those who've pledged $1,500/month or more to the MUI organization. Tier benefits.

via Open Collective or via the for-profit

Goread.io Buzzoid Buzzoid Twicsy Views4You Poprey SocialWick Follower24 TikTokFame Reputation Manage

Gold sponsors are those who've pledged $500/month or more to the MUI organization. Tier benefits.

Silvers sponsors are those who've pledged $250/month to $500/month to the MUI organization. Tier benefits.

Bronze sponsors are those who've pledged $100/month to $250/month to the MUI organization. Tier benefits.

Material UI (as well as MUI Base, MUI System, and Joy UI) is open-source to give users great freedom in how they use the software and to enable the community to have influence over how the project progresses to make it appropriate for a wide range of use cases. To ensure that these open-source libraries can stand the test of time for our users, they need to be well-directed and financially sustainable.

The absolute best way to support the MUI organization to work on its libraries' ongoing development efforts is to become a sponsor. Crowd-sourced funding enables us to spend the most time directly working on improving the open-source projects, which you and the rest of the community then benefit from.

Sponsorship money is used to fund open-source software development, testing, documentation, and releases of the projects.

Users are not obligated to give back to Material UI, but it is in their interest to do so.

By significantly reducing the amount of work needed to achieve business goals and reducing running costs, the open-source libraries result in huge time and money savings for users. We e

*[Content truncated - see full docs]*

---

## Usage - Material UI

**URL**: https://mui.com/material-ui/getting-started/usage/

**Contents**:
- Usage
- Quickstart
- Globals
  - Responsive meta tag
  - CssBaseline
  - Default font

Learn the basics of working with Material UI components.

After installation, you can import any Material UI component and start playing around. For example, try changing the variant on the Button to outlined to see how the style changes:

Since Material UI components are built to function in isolation, they don't require any kind of globally scoped styles. For a better user experience and developer experience, we recommend adding the following globals to your app.

Material UI is a mobile-first component library—we write code for mobile devices first, and then scale up the components as necessary using CSS media queries.

To ensure proper rendering and touch zooming for all devices, add the responsive viewport meta tag to your <head> element:

Material UI provides an optional CssBaseline component. It fixes some inconsistencies across browsers and devices while providing resets that are better tailored to fit Material UI than alternative global style sheets like normalize.css.

Material UI uses the Roboto font by default. See Installation—Roboto font for complete details.

Was this page helpful?

**Examples**:

```tsx
import * as React from 'react';
import Button from '@mui/material/Button';

export default function ButtonUsage() {
  return <Button variant="contained">Hello world</Button>;
}
```

```html
<meta name="viewport" content="initial-scale=1, width=device-width" />
```

---
