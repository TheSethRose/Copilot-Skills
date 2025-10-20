# Mantine - Getting Started

**Pages**: 2

---

## Getting started | Mantine

**URL**: https://mantine.dev/getting-started/

**Contents**:
- Getting started
- Get started with a template
- Community templates
- Framework guide
- Can I use Mantine with create-react-app?
- Get started without framework
- Set up VS Code
- Learn

The easiest way to get started is to use one of the templates. All templates include required dependencies and pre-configured settings. Some templates also include additional features like Jest, Storybook, ESLint, etc.

Templates include only @mantine/core and @mantine/hooks packages, if you need additional @mantine/* packages, follow installation instructions of the package you want to use.

To get started with a template, open it on GitHub and click "Use this template" button. In order to use this feature you need to be logged in to your GitHub account. If you are not familiar with GitHub, you can find a detailed instruction on how to bootstrap a project from a template in this article.

Next.js template with app router and full setup: Jest, Storybook, ESLint

Next.js template with pages router and full setup: Jest, Storybook, ESLint

next-app-min-template

Next.js template with app router and minimal setup – no additional tools included, only default Next.js configuration

next-pages-min-template

Next.js template with pages router and minimal setup – no additional tools included, only default Next.js configuration

next-vanilla-extract-template

Next.js template with Vanilla extract example

Vite template with full setup: Vitest, Prettier, Storybook, ESLint

Vite template with minimal setup – no additional tools included, only default Vite configuration

vite-vanilla-extract-template

Vite template with Vanilla extract example

Gatsby template with basic setup

RedwoodJS template with basic setup

Community templates are created and maintained by the community members. These templates include additional features and third-party integrations. You are welcome to share your template with the community by following this guide.

Create a template with your stack and share it with the community

Next.js app router T3 stack template

next-tailwind-template

Next.js app router + Mantine + Tailwind template

Next.js app router + Mantine + Bun template

Fullstack boilerpl

*[Content truncated - see full docs]*

**Examples**:

```text
yarn add @mantine/core @mantine/hooks
```

```text
npm install @mantine/core @mantine/hooks
```

```text
yarn add --dev postcss postcss-preset-mantine postcss-simple-vars
```

---

## Getting started | Mantine

**URL**: https://mantine.dev/dates/getting-started/

**Contents**:
- Getting started
- Installation
- Do not forget to import styles
- Usage
- dayjs
- DatesProvider
- Consistent weeks
- Custom parse format

Get started with @mantine/dates package

After installation import package styles at the root of your application:

Followed installation instructions above but something is not working (calendars and date pickers have no styles and look broken)? You've fallen into the trap of not importing dates styles! To fix the issue, import dates styles at the root of your application:

After installing @mantine/dates package and importing styles, you can use all components from it:

@mantine/dates components use dayjs under the hood for date manipulations and formatting. dayjs is a required dependency – you cannot change it to another date library. If you want to use a different date library in your application, you will need to install it separately.

DatesProvider component lets you set various settings that are shared across all components exported from @mantine/dates package. DatesProvider supports the following settings:

If you want to avoid layout shifts, set consistentWeeks: true in DatesProvider settings. This will make sure that every month has 6 weeks, even if outside days are not in the same month.

Some components like DateInput require custom parse format dayjs plugin. You need to extend dayjs with this plugin before using components that require it. Note that it is usually done once in your application root file, so you don't need to do it every time you use component.

To add localization you must import import 'dayjs/locale/x'; in your application (x is locale name) and set locale either on DatesProvider or on each component individually.

Example of setting locale on DatesProvider:

The code above works in all environments, except Next.js app router. If you are using Next.js app router, you must add 'use client'; to the top of the file where you are importing dayjs/locale/x – locale data is required both on client and server.

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```text
yarn add @mantine/dates dayjs
```

```text
npm install @mantine/dates dayjs
```

```text
import '@mantine/core/styles.css';
// ‼️ import dates styles after core package styles
import '@mantine/dates/styles.css';
```

---
