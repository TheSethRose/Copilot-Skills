# Storybook - Writing Stories

**Pages**: 16

---

## Args

**URL**: https://storybook.js.org/docs/writing-stories/args

**Contents**:
- Args
- Args object
- Story args
- Component args
- Global args
- Args composition
- Args can modify any aspect of your component
- Setting args through the URL

A story is a component with a set of arguments that define how the component should render. “Args” are Storybook’s mechanism for defining those arguments in a single JavaScript object. Args can be used to dynamically change props, slots, styles, inputs, etc. It allows Storybook and its addons to live edit components. You do not need to modify your underlying component code to use args.

When an arg’s value changes, the component re-renders, allowing you to interact with components in Storybook’s UI via addons that affect args.

Learn how and why to write stories in the introduction. For details on how args work, read on.

The args object can be defined at the story, component and global level. It is a JSON serializable object composed of string keys with matching valid value types that can be passed into a component for your framework.

To define the args of a single story, use the args CSF story key:

These args will only apply to the story for which they are attached, although you can reuse them via JavaScript object reuse:

In the above example, we use the object spread feature of ES 2015.

You can also define args at the component level; they will apply to all the component's stories unless you overwrite them. To do so, use the args key on the default CSF export:

You can also define args at the global level; they will apply to every component's stories unless you overwrite them. To do so, define the args property in the default export of preview.js|ts:

For most uses of global args, globals are a better tool for defining globally-applied settings, such as a theme. Using globals enables users to change the value with the toolbar menu.

You can separate the arguments to a story to compose in other stories. Here's how you can combine args for multiple stories of the same component.

If you find yourself re-using the same args for most of a component's stories, you should consider using component-level args.

Args are useful when writing stories for composite compo

*[Content truncated - see full docs]*

**Examples**:

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
import type { Meta, StoryObj } from '@storybook/your-framework';
 
import { Button } from './Button';
 
const meta = {
  component: Button,
} satisfies Meta<typeof Button>;
 
export default meta;
type Story = StoryObj<typeof meta>;
 
export const Primary: Story = {
  args: {
    primary: true,
    label: 'Button',
  },
};
```

```python
// Replace your-framework with the name of your framework
import type { Meta, StoryObj } from '@storybook/your-framework';
 
import { Button } from './Button';
 
const meta = {
  component: Button,
} satisfies Meta<typeof Button>;
 
export default meta;
type Story = StoryObj<typeof meta>;
 
export const Primary: Story = {
  args: {
    primary: true,
    label: 'Button',
  },
};
 
export const PrimaryLongName: Story = {
  args: {
    ...Primary.args,
    label: 'Primary with a really long name',
...
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
import type { Meta } from '@storybook/your-framework';
 
import { Button } from './Button';
 
const meta = {
  component: Button,
  //👇 Creates specific argTypes
  argTypes: {
    backgroundColor: { control: 'color' },
  },
  args: {
    //👇 Now all Button stories will be primary.
    primary: true,
  },
} satisfies Meta<typeof Button>;
 
export default meta;
```

---

## Browse Stories

**URL**: https://storybook.js.org/docs/get-started/browse-stories

**Contents**:
- Browse Stories
- Sidebar and Canvas
- Toolbar
- Addons
- Use stories to build UIs

Last chapter, we learned that stories correspond with discrete component states. This chapter demonstrates how to use Storybook as a workshop for building components.

A *.stories.js|ts|svelte file defines all the stories for a component. Each story has a corresponding sidebar item. When you click on a story, it renders in the Canvas an isolated preview iframe.

Navigate between stories by clicking on them in the sidebar. Try the sidebar search to find a story by name.

Or use keyboard shortcuts. Click on the Storybook's menu to see the list of shortcuts available.

Storybook ships with time-saving tools built-in. The toolbar contains tools that allow you to adjust how the story renders in the Canvas:

The “Docs” page displays auto-generated documentation for components (inferred from the source code). Usage documentation is helpful when sharing reusable components with your team, for example, in an application.

The toolbar is customizable. You can use globals to quickly toggle themes and languages. Or install Storybook toolbar addons from the community to enable advanced workflows.

Addons are plugins that extend Storybook's core functionality. You can find them in the addons panel, a reserved place in the Storybook UI below the Canvas. Each tab shows the generated metadata, logs, or static analysis for the selected story by the addon.

Storybook is extensible. Our rich ecosystem of addons helps you test, document, and optimize your stories. You can also create an addon to satisfy your workflow requirements. Read more in the addons section.

In the next chapter, we'll get your components rendering in Storybook so you can use it to supercharge component development.

When building apps, one of the biggest challenges is to figure out if a piece of UI already exists in your codebase and how to use it for the new feature you're building.

Storybook catalogues all your components and their use cases. Therefore, you can quickly browse it to find what you're looking for.

*[Content truncated - see full docs]*

---

## Building pages with Storybook

**URL**: https://storybook.js.org/docs/writing-stories/build-pages-with-storybook

**Contents**:
- Building pages with Storybook
- Pure presentational pages
  - Args composition for presentational screens
- Mocking connected components
  - Mocking imports
  - Mocking API Services
  - Mocking providers
  - Avoiding mocking dependencies

Storybook helps you build any component, from small “atomic” components to composed pages. But as you move up the component hierarchy toward the page level, you deal with more complexity.

There are many ways to build pages in Storybook. Here are common patterns and solutions.

Teams at the BBC, The Guardian, and the Storybook maintainers themselves build pure presentational pages. If you take this approach, you don't need to do anything special to render your pages in Storybook.

It's straightforward to write components to be fully presentational up to the screen level. That makes it easy to show in Storybook. The idea is that you do all the messy “connected” logic in a single wrapper component in your app outside of Storybook. You can see an example of this approach in the Data chapter of the Intro to Storybook tutorial.

Your existing app may not be structured in this way, and it may be difficult to change it.

Fetching data in one place means that you need to drill it down to the components that use it. This can be natural in a page that composes one big GraphQL query (for instance), but other data fetching approaches may make this less appropriate.

It's less flexible if you want to load data incrementally in different places on the screen.

When you are building screens in this way, it is typical that the inputs of a composite component are a combination of the inputs of the various sub-components it renders. For instance, if your screen renders a page layout (containing details of the current user), a header (describing the document you are looking at), and a list (of the subdocuments), the inputs of the screen may consist of the user, document and subdocuments.

In such cases, it is natural to use args composition to build the stories for the page based on the stories of the sub-components:

This approach is beneficial when the various subcomponents export a complex list of different stories. You can pick and choose to build realistic scenarios for your scre

*[Content truncated - see full docs]*

**Examples**:

```python
import PageLayout from './PageLayout';
import Document from './Document';
import SubDocuments from './SubDocuments';
import DocumentHeader from './DocumentHeader';
import DocumentList from './DocumentList';
 
export interface DocumentScreenProps {
  user?: {};
  document?: Document;
  subdocuments?: SubDocuments[];
}
 
export function DocumentScreen({ user, document, subdocuments }: DocumentScreenProps) {
  return (
    <PageLayout user={user}>
      <DocumentHeader document={document} />
      
...
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Meta, StoryObj } from '@storybook/your-framework';
 
import { DocumentScreen } from './YourPage';
 
// 👇 Imports the required stories
import * as PageLayout from './PageLayout.stories';
import * as DocumentHeader from './DocumentHeader.stories';
import * as DocumentList from './DocumentList.stories';
 
const meta = {
  component: DocumentScreen,
} satisfies Meta<typeof DocumentScree
...
```

```text
ProfilePage.js
ProfilePage.stories.js
ProfilePageContainer.js
ProfilePageContext.js
```

---

## Decorators

**URL**: https://storybook.js.org/docs/writing-stories/decorators

**Contents**:
- Decorators
- Wrap stories with extra markup
- “Context” for mocking
  - Using decorators to provide data
- Story decorators
- Component decorators
- Global decorators
- Decorator inheritance

A decorator is a way to wrap a story in extra “rendering” functionality. Many addons define decorators to augment your stories with extra rendering or gather details about how your story renders.

When writing stories, decorators are typically used to wrap stories with extra markup or context mocking.

Some components require a “harness” to render in a useful way. For instance, if a component runs right up to its edges, you might want to space it inside Storybook. Use a decorator to add spacing for all stories of the component.

The second argument to a decorator function is the story context which contains the properties:

This context can be used to adjust the behavior of your decorator based on the story's arguments or other metadata. For example, you could create a decorator that allows you to optionally apply a layout to the story, by defining parameters.pageLayout = 'page' (or 'page-mobile'): :

For another example, see the section on configuring the mock provider, which demonstrates how to use the same technique to change which theme is provided to the component.

If your components are “connected” and require side-loaded data to render, you can use decorators to provide that data in a mocked way without having to refactor your components to take that data as an arg. There are several techniques to achieve this. Depending on exactly how you are loading that data. Read more in the building pages in Storybook section.

To define a decorator for a single story, use the decorators key on a named export:

It is useful to ensure that the story remains a “pure” rendering of the component under test and that any extra HTML or components are used only as decorators. In particular the Source Doc Block works best when you do this.

To define a decorator for all stories of a component, use the decorators key of the default CSF export:

We can also set a decorator for all stories via the decorators export of your .storybook/preview.js|ts file (this is the file where you c

*[Content truncated - see full docs]*

**Examples**:

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
import type { Meta } from '@storybook/your-framework';
 
import { YourComponent } from './YourComponent';
 
const meta = {
  component: YourComponent,
  decorators: [
    (Story) => (
      <div style={{ margin: '3em' }}>
        {/* 👇 Decorators in Storybook also accept a function. Replace <Story/> with Story() to enable it  */}
        <Story />
      </div>
    ),
  ],
} satisfies Meta<typeo
...
```

```python
import React from 'react';
 
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
import type { Preview } from '@storybook/your-framework';
 
const preview: Preview = {
  decorators: [
    // 👇 Defining the decorator in the preview file applies it to all stories
    (Story, { parameters }) => {
      // 👇 Make it configurable by reading from parameters
      const { pageLayout } = parameters;
      switch (pageLayout) {
        case 'page':
     
...
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
import type { Meta, StoryObj } from '@storybook/your-framework';
 
import { Button } from './Button';
 
const meta = {
  component: Button,
} satisfies Meta<typeof Button>;
 
export default meta;
type Story = StoryObj<typeof meta>;
 
export const Primary: Story = {
  decorators: [
    (Story) => (
      <div style={{ margin: '3em' }}>
        {/* 👇 Decorators in Storybook also accept a function
...
```

---

## Embed stories

**URL**: https://storybook.js.org/docs/sharing/embed

**Contents**:
- Embed stories
- Embed a story with the toolbar
- Embed a story without the toolbar
- Embed documentation
- Embed stories on other platforms

Embed stories to showcase your work to teammates and the developer community at large. In order to use embeds, your Storybook must be published and publicly accessible.

Storybook supports <iframe> embeds out of the box. If you use Chromatic to publish Storybook, you can also embed stories in Notion, Medium, and countless other platforms that support the oEmbed standard.

Embed a story with the toolbar, and paste the published story URL. For example:

To embed a plain story without Storybook's toolbar, click the "open canvas in new tab" icon in the top-right corner of Storybook to get the canvas URL. For example:

Embed a documentation page by replacing viewMode=story with the uniquely auto-generated documentation entry for the story.

Every platform has different levels of embed support. Check the documentation of your service to see how they recommend embedding external content.

Paste the Storybook URL into your Medium article, then press Enter. The embed will automatically resize to fit the story's height.

While editing an article, Medium renders all embeds non-interactive. Once your article is published, it will become interactive. Preview a demo on Medium.

In your Notion document, type /embed, press Enter, and paste the story URL as the embed link. You can resize the embed as necessary.

Type /html in your Ghost post, press Enter and paste the iframe URL. You can resize the embed via the width and height properties as required.

**Examples**:

```text
// oEmbed
https://5ccbc373887ca40020446347-wtuhidckxo.chromatic.com/?path=/story/shadowboxcta--default
 
// iframe embed
<iframe
  src="https://5ccbc373887ca40020446347-wtuhidckxo.chromatic.com/?path=/story/shadowboxcta--default&full=1&shortcuts=false&singleStory=true"
  width="800"
  height="260"
></iframe>
```

```text
// oEmbed
https://5ccbc373887ca40020446347-wtuhidckxo.chromatic.com/iframe.html?id=/story/shadowboxcta--default&viewMode=story
 
// iframe embed
 <iframe
  src="https://5ccbc373887ca40020446347-wtuhidckxo.chromatic.com/iframe.html?id=shadowboxcta--default&viewMode=story&shortcuts=false&singleStory=true"
  width="800"
  height="200"
></iframe>
```

```text
// oEmbed
https://5ccbc373887ca40020446347-wtuhidckxo.chromatic.com/iframe.html?id=shadowboxcta--docs&viewMode=docs&shortcuts=false&singleStory=true
 
// iframe embed
 <iframe
  src="https://5ccbc373887ca40020446347-wtuhidckxo.chromatic.com/iframe.html?id=shadowboxcta--docs&viewMode=docs&shortcuts=false&singleStory=true"
  width="800"
  height="400"
></iframe>
```

---

## How to write stories

**URL**: https://storybook.js.org/docs/writing-stories

**Contents**:
- How to write stories
- Where to put stories
- Component Story Format
  - Default export
  - Defining stories
    - Custom rendering
    - Working with React Hooks
  - Rename stories

A story captures the rendered state of a UI component. It's an object with annotations that describe the component's behavior and appearance given a set of arguments.

Storybook uses the generic term arguments (args for short) when talking about React’s props, Vue’s props, Angular’s @Input, and other similar concepts.

A component’s stories are defined in a story file that lives alongside the component file. The story file is for development-only, and it won't be included in your production bundle. In your filesystem, it looks something like this:

We define stories according to the Component Story Format (CSF), an ES6 module-based standard that is easy to write and portable between tools.

The key ingredients are the default export that describes the component, and named exports that describe the stories.

The default export metadata controls how Storybook lists your stories and provides information used by addons. For example, here’s the default export for a story file Button.stories.js|ts:

Starting with Storybook version 7.0, story titles are analyzed statically as part of the build process. The default export must contain a title property that can be read statically or a component property from which an automatic title can be computed. Using the id property to customize your story URL must also be statically readable.

Use the named exports of a CSF file to define your component’s stories. We recommend you use UpperCamelCase for your story exports. Here’s how to render Button in the “primary” state and export a story called Primary.

By default, stories will render the component defined in the meta (default export), with the args passed to it. If you need to render something else, you can provide a function to the render property that returns the desired output.

For example, if you want to render a Button inside an Alert, you can define a custom render function like this:

Note how the render function spreads args onto the Button component. This ensures that f

*[Content truncated - see full docs]*

**Examples**:

```typescript
components/
├─ Button/
│  ├─ Button.js | ts | jsx | tsx | vue | svelte
│  ├─ Button.stories.js | ts | jsx | tsx | svelte
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
import type { Meta } from '@storybook/your-framework';
 
import { Button } from './Button';
 
const meta = {
  component: Button,
} satisfies Meta<typeof Button>;
 
export default meta;
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
import type { Meta, StoryObj } from '@storybook/your-framework';
 
import { Button } from './Button';
 
const meta = {
  component: Button,
} satisfies Meta<typeof Button>;
 
export default meta;
type Story = StoryObj<typeof meta>;
 
export const Primary: Story = {
  args: {
    primary: true,
    label: 'Button',
  },
};
```

---

## Mocking modules

**URL**: https://storybook.js.org/docs/writing-stories/mocking-data-and-modules/mocking-modules

**Contents**:
- Mocking modules
- Automocking
  - Registering modules to mock
    - Spy-only
    - Fully automocked modules
    - Mock files
  - Using automocked modules in stories
  - How it works

Components often depend on other modules, such as other components, utility functions, or libraries. These can be from external packages or internal to your project. When rendering those components in Storybook or testing them, you may want to mock those modules to control their behavior and isolate the component's functionality.

For example, this simple component depends on two modules, a local utility function to access the user's browser session and an external package to generate a unique ID:

The above example is written with React, but the same principles apply to other renderers like Vue, Svelte, or Web Components. The important part is the usage of the two module dependencies.

When writing stories or tests for this component, you may want to mock the getUserFromSession function to control the user data returned, or mock the uuidv4 function to return a predictable ID. This allows you to test the component's behavior without relying on the actual implementations of these modules.

For maximum flexibility, Storybook provides three ways to mock modules for your stories. Let's walk through each of them, starting with the most straightforward approach.

Automocking is the most straightforward way to mock modules in Storybook, and we recommend it for all projects using the Vite and Webpack builders (other builders must use one of the other techniques, below). This approach requires minimal configuration while allowing for flexible mocking of modules.

It works with two steps. First, register the modules you want to mock in your Storybook configuration. Then, control the behavior and make assertions about the mocked modules in your stories.

When automocking, you use the sb.mock utility function to register modules you want to mock. There are three ways to register modules: as spy-only, fully automocked, or with a mock file. Each method has its use cases and benefits.

There are some key details to keep in mind when using the sb.mock utility:

For most cases, you 

*[Content truncated - see full docs]*

**Examples**:

```python
import { v4 as uuidv4 } from 'uuid';
import { getUserFromSession } from '../lib/session';
 
export function AuthButton() {
  const user = getUserFromSession();
  const id = uuidv4();
 
  return (
    <button onClick={() => { console.log(`User: ${user.name}, ID: ${id}`) }}>
      {user ? `Welcome, ${user.name}` : 'Sign in'}
    </button>
  );
}
```

```python
import { sb } from 'storybook/test';
 
// 👇 Automatically spies on all exports from the `lib/session` local module
sb.mock(import('../lib/session.ts'), { spy: true });
// 👇 Automatically spies on all exports from the `uuid` package in `node_modules`
sb.mock(import('uuid'), { spy: true });
 
// ...rest of the file
```

```python
import { sb } from 'storybook/test';
 
// 👇 Automatically replaces all exports from the `lib/session` local module with mock functions
sb.mock(import('../lib/session.ts'));
// 👇 Automatically replaces all exports from the `uuid` package in `node_modules` with mock functions
sb.mock(import('uuid'));
 
// ...rest of the file
```

---

## Naming components and hierarchy

**URL**: https://storybook.js.org/docs/writing-stories/naming-components-and-hierarchy

**Contents**:
- Naming components and hierarchy
- Structure and hierarchy
- Naming stories
- Grouping
- Roots
- Single-story hoisting
- Sorting stories

Storybook provides a powerful way to organize your stories, giving you the necessary tools to categorize, search, and filter your stories based on your organization's needs and preferences.

When organizing your Storybook, there are two methods of structuring your stories: implicit and explicit. The implicit method involves relying upon the physical location of your stories to position them in the sidebar, while the explicit method involves utilizing the title parameter to place the story.

Based on how you structure your Storybook, you can see that the story hierarchy is made up of various parts:

When creating your stories, you can explicitly use the title parameter to define the story's position in the sidebar. It can also be used to group related components together in an expandable interface to help with Storybook organization providing a more intuitive experience for your users. For example:

It is also possible to group related components in an expandable interface to help with Storybook organization. To do so, use the / as a separator:

By default, the top-level grouping will be displayed as “root” in the Storybook UI (i.e., the uppercased, non-expandable items). If you need, you can configure Storybook and disable this behavior. Useful if you need to provide a streamlined experience for your users; nevertheless, if you have a large Storybook composed of multiple component stories, we recommend naming your components according to the file hierarchy.

Single-story components (i.e., component stories without siblings) whose display name exactly matches the component's name (last part of title) are automatically hoisted up to replace their parent component in the UI. For example:

Because story exports are automatically "start cased" (myStory becomes "My Story"), your component name should match that. Alternatively, you can override the story name using myStory.storyName = '...' to match the component name.

Out of the box, Storybook sorts stories based on the 

*[Content truncated - see full docs]*

**Examples**:

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Meta } from '@storybook/your-framework';
 
import { Button } from './Button';
 
const meta = {
  /* 👇 The title prop is optional.
   * See https://storybook.js.org/docs/configure/#configure-story-loading
   * to learn how to generate automatic titles
   */
  title: 'Button',
  component: Button,
} satisfies Meta<typeof Button>;
 
export default meta;
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Meta } from '@storybook/your-framework';
 
import { Button } from './Button';
 
const meta = {
  /* 👇 The title prop is optional.
   * See https://storybook.js.org/docs/configure/#configure-story-loading
   * to learn how to generate automatic titles
   */
  title: 'Design System/Atoms/Button',
  component: Button,
} satisfies Meta<typeof Button>;
 
export default meta;
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Meta } from '@storybook/your-framework';
 
import { CheckBox } from './Checkbox';
 
const meta = {
  /* 👇 The title prop is optional.
   * See https://storybook.js.org/docs/configure/#configure-story-loading
   * to learn how to generate automatic titles
   */
  title: 'Design System/Atoms/Checkbox',
  component: CheckBox,
} satisfies Meta<typeof CheckBox>;
 
export default meta;
```

---

## Parameters

**URL**: https://storybook.js.org/docs/writing-stories/parameters

**Contents**:
- Parameters
- Story parameters
- Component parameters
- Global parameters
- Rules of parameter inheritance

Parameters are a set of static, named metadata about a story, typically used to control the behavior of Storybook features and addons.

Available parameters are listed in the parameters API reference.

For example, let’s customize the backgrounds feature via a parameter. We’ll use parameters.backgrounds to define which backgrounds appear in the backgrounds toolbar when a story is selected.

We can set a parameter for a single story with the parameters key on a CSF export:

We can set the parameters for all stories of a component using the parameters key on the default CSF export:

We can also set the parameters for all stories via the parameters export of your .storybook/preview.js|ts file (this is the file where you configure all stories):

Setting a global parameter is a common way to configure addons. With backgrounds, you configure the list of backgrounds that every story can render in.

The way the global, component and story parameters are combined is:

The merging of parameters is important. This means it is possible to override a single specific sub-parameter on a per-story basis while retaining most of the parameters defined globally.

If you are defining an API that relies on parameters (e.g., an addon) it is a good idea to take this behavior into account.

**Examples**:

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Meta, StoryObj } from '@storybook/your-framework';
 
import { Button } from './Button';
 
const meta = {
  component: Button,
} satisfies Meta<typeof Button>;
 
export default meta;
type Story = StoryObj<typeof meta>;
 
export const Primary: Story = {
  // 👇 Story-level parameters
  parameters: {
    backgrounds: {
      options: {
        red: { name: 'Red', value: '#f00' },
      
...
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Meta } from '@storybook/your-framework';
 
import { Button } from './Button';
 
const meta = {
  component: Button,
  //👇 Creates specific parameters at the component level
  parameters: {
    backgrounds: {
      options: {},
    },
  },
} satisfies Meta<typeof Button>;
 
export default meta;
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Preview } from '@storybook/your-framework';
 
const preview: Preview = {
  parameters: {
    backgrounds: {
      options: {
        light: { name: 'Light', value: '#fff' },
        dark: { name: 'Dark', value: '#333' },
      },
    },
  },
};
 
export default preview;
```

---

## Play function

**URL**: https://storybook.js.org/docs/writing-stories/play-function

**Contents**:
- Play function
- Writing stories with the play function
- Working with the canvas
- Composing stories

Play functions are small snippets of code executed after the story renders. They enable you to interact with your components and test scenarios that otherwise require user intervention.

Storybook's play functions are small code snippets that run once the story finishes rendering. Aided by the interactions panel, it allows you to build component interactions and test scenarios that were impossible without user intervention. For example, if you were working on a registration form and wanted to validate it, you could write the following story with the play function:

See the interaction testing documentation for an overview of the available API events.

When Storybook finishes rendering the story, it executes the steps defined within the play function, interacting with the component and filling the form's information. All of this without the need for user intervention. If you check your Interactions panel, you'll see the step-by-step flow.

Part of the context passed to the play function is a canvas object. This object allows you to query the DOM of the rendered story. It provides a scoped version of the Testing Library queries, so you can use them as you would in a regular test.

If you need to query outside of the canvas (for example, to test a dialog that appears outside of the story root), you can use the screen object available from storybook/test.

Thanks to the Component Story Format, an ES6 module based file format, you can also combine your play functions, similar to other existing Storybook features (e.g., args). For example, if you wanted to verify a specific workflow for your component, you could write the following stories:

By combining the stories, you're recreating the entire component workflow and can spot potential issues while reducing the boilerplate code you need to write.

**Examples**:

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Meta, StoryObj } from '@storybook/your-framework';
 
import { RegistrationForm } from './RegistrationForm';
 
const meta = {
  component: RegistrationForm,
} satisfies Meta<typeof RegistrationForm>;
 
export default meta;
type Story = StoryObj<typeof meta>;
 
/*
 * See https://storybook.js.org/docs/writing-stories/play-function#working-with-the-canvas
 * to learn more about using th
...
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Meta, StoryObj } from '@storybook/your-framework';
 
import { MyComponent } from './MyComponent';
 
const meta = {
  component: MyComponent,
} satisfies Meta<typeof MyComponent>;
export default meta;
 
type Story = StoryObj<typeof meta>;
 
export const ExampleStory: Story = {
  play: async ({ canvas, userEvent }) => {
    // Starts querying from the component's root element
    awai
...
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Meta, StoryObj } from '@storybook/your-framework';
import { screen } from 'storybook/test';
 
import { Dialog } from './Dialog';
 
const meta = {
  component: Dialog,
} satisfies Meta<typeof Dialog>;
export default meta;
 
type Story = StoryObj<typeof meta>;
 
export const Open: Story = {
  play: async ({ canvas, userEvent }) => {
    await userEvent.click(canvas.getByRole('button',
...
```

---

## Stories

**URL**: https://storybook.js.org/docs/api/doc-blocks/doc-block-stories

**Contents**:
- Stories
- Stories
  - includePrimary
  - title

The Stories block renders the full collection of stories in a stories file.

Stories is configured with the following props:

Determines if the collection of stories includes the primary (first) story.

If a stories file contains only one story and includePrimary={true}, the Stories block will render nothing to avoid a potentially confusing situation.

Sets the heading content preceding the collection of stories.

**Examples**:

```python
import { Meta, Stories } from '@storybook/addon-docs/blocks';
import * as ButtonStories from './Button.stories';
 
<Meta of={ButtonStories} />
 
<Stories />
```

```python
import { Stories } from '@storybook/addon-docs/blocks';
```

---

## Stories for multiple components

**URL**: https://storybook.js.org/docs/writing-stories/stories-for-multiple-components

**Contents**:
- Stories for multiple components
- Subcomponents
- Reusing story definitions
- Using children as an arg
- Creating a Template Component

It's useful to write stories that render two or more components at once if those components are designed to work together. For example, ButtonGroup, List, and Page components.

When the components you're documenting have a parent-child relationship, you can use the subcomponents property to document them together. This is especially useful when the child component is not meant to be used on its own, but only as part of the parent component.

Here's an example with List and ListItem components:

Note that by adding a subcomponents property to the default export, we get an extra panel on the ArgTypes and Controls tables, listing the props of ListItem:

Subcomponents are only intended for documentation purposes and have some limitations:

Let's talk about some techniques you can use to mitigate the above, which are especially useful in more complicated situations.

We can also reduce repetition in our stories by reusing story definitions. Here, we can reuse the ListItem stories' args in the story for List:

By rendering the Unchecked story with its args, we are able to reuse the input data from the ListItem stories in the List.

However, we still aren’t using args to control the ListItem stories, which means we cannot change them with controls and we cannot reuse them in other, more complex component stories.

One way we improve that situation is by pulling the rendered subcomponent out into a children arg:

Now that children is an arg, we can potentially reuse it in another story.

However, there are some caveats when using this approach that you should be aware of.

The children arg, just like all args, needs to be JSON serializable. To avoid errors with your Storybook, you should:

We're currently working on improving the overall experience for the children arg and allow you to edit children arg in a control and allow you to use other types of components in the near future. But for now you need to factor in this caveat when you're implementing your stories.

Another

*[Content truncated - see full docs]*

**Examples**:

```python
import React from 'react';
 
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
import type { Meta, StoryObj } from '@storybook/your-framework';
 
import { List } from './List';
import { ListItem } from './ListItem';
 
const meta = {
  component: List,
  subcomponents: { ListItem }, //👈 Adds the ListItem component as a subcomponent
} satisfies Meta<typeof List>;
export default meta;
 
type Story = StoryObj<typeof meta>;
 
export const Empty: St
...
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
import type { Meta, StoryObj } from '@storybook/your-framework';
 
import { List } from './List';
import { ListItem } from './ListItem';
 
//👇 We're importing the necessary stories from ListItem
import { Selected, Unselected } from './ListItem.stories';
 
const meta = {
  component: List,
} satisfies Meta<typeof List>;
 
export default meta;
type Story = StoryObj<typeof meta>;
 
export const Ma
...
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
import type { Meta, StoryObj } from '@storybook/your-framework';
 
import { List } from './List';
 
//👇 Instead of importing ListItem, we import the stories
import { Unchecked } from './ListItem.stories';
 
const meta = {
  /* 👇 The title prop is optional.
   * See https://storybook.js.org/docs/configure/#configure-story-loading
   * to learn how to generate automatic titles
   */
  title: 'Lis
...
```

---

## Stories in end-to-end tests

**URL**: https://storybook.js.org/docs/writing-tests/integrations/stories-in-end-to-end-tests

**Contents**:
- Stories in end-to-end tests
- With Cypress
- With Playwright

Storybook seamlessly integrates with additional testing frameworks like Cypress and Playwright to provide a comprehensive testing solution. By leveraging the Component Story Format (CSF), developers can write test cases that simulate user interactions and verify the behavior of individual components within the Storybook environment. This approach enables developers to thoroughly test their components' functionality, responsiveness, and visual appearance across different scenarios, resulting in more robust and reliable applications.

Cypress is an end-to-end testing framework. It enables you to test a complete instance of your application by simulating user behavior. With Component Story Format, your stories are reusable with Cypress. Each named export (in other words, a story) is renderable within your testing setup.

An example of an end-to-end test with Cypress and Storybook is testing a login component for the correct inputs. For example, if you had the following story:

The play function contains small snippets of code that run after the story renders. It allows you to sequence interactions in stories.

With Cypress, you could write the following test:

When Cypress runs your test, it loads Storybook's isolated iframe and checks if the inputs match the test values.

Playwright is a browser automation tool and end-to-end testing framework from Microsoft. It offers cross-browser automation, mobile testing with device emulation, and headless testing. With Component Story Format, your stories are reusable with Playwright. Each named export (in other words, a story) is renderable within your testing setup.

A real-life scenario of user flow testing with Playwright would be how to test a login form for validity. For example, if you had the following story already created:

The play function contains small snippets of code that run after the story renders. It allows you to sequence interactions in stories.

With Playwright, you can write a test to check if the inputs a

*[Content truncated - see full docs]*

**Examples**:

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
import type { Meta, StoryObj } from '@storybook/your-framework';
 
import { expect } from 'storybook/test';
 
import { LoginForm } from './LoginForm';
 
const meta = {
  component: LoginForm,
} satisfies Meta<typeof LoginForm>;
export default meta;
 
type Story = StoryObj<typeof meta>;
 
export const EmptyForm: Story = {};
 
export const FilledForm: Story = {
  play: async ({ canvas, userEvent 
...
```

```javascript
/// <reference types="cypress" />
 
describe('Login Form', () => {
  it('Should contain valid login information', () => {
    cy.visit('/iframe.html?id=components-login-form--example');
    cy.get('#login-form').within(() => {
      cy.log('**enter the email**');
      cy.get('#email').should('have.value', 'email@provider.com');
      cy.log('**enter password**');
      cy.get('#password').should('have.value', 'a-random-password');
    });
  });
});
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
import type { Meta, StoryObj } from '@storybook/your-framework';
 
import { expect } from 'storybook/test';
 
import { LoginForm } from './LoginForm';
 
const meta = {
  component: LoginForm,
} satisfies Meta<typeof LoginForm>;
export default meta;
 
type Story = StoryObj<typeof meta>;
 
export const EmptyForm: Story = {};
 
export const FilledForm: Story = {
  play: async ({ canvas, userEvent 
...
```

---

## Stories in unit tests

**URL**: https://storybook.js.org/docs/writing-tests/integrations/stories-in-unit-tests

**Contents**:
- Stories in unit tests
- Write a test with Testing Library
  - Override story properties
- Run tests on a single story
- Combine stories into a single test
- Troubleshooting
  - Run tests in other frameworks
  - The args are not being passed to the test

Teams test a variety of UI characteristics using different tools. Each tool requires you to replicate the same component state over and over. That’s a maintenance headache. Ideally, you’d set up your tests similarly and reuse that across tools.

Storybook enables you to isolate a component and capture its use cases in a *.stories.js|ts file. Stories are standard JavaScript modules that are cross-compatible with the whole JavaScript ecosystem.

Stories are a practical starting point for UI testing. Import stories into tools like Jest, Testing Library, Vitest and Playwright, to save time and maintenance work.

Testing Library is a suite of helper libraries for browser-based component tests. With Component Story Format, your stories are reusable with Testing Library. Each named export (story) is renderable within your testing setup. For example, if you were working on a login component and wanted to test the invalid credentials scenario, here's how you could write your test:

Storybook provides a composeStories utility that helps convert stories from a test file into renderable elements that can be reused in your Node tests with JSDOM. It also allows you to apply other Storybook features that you have enabled your project (e.g., decorators, args) into your tests, enabling you to reuse your stories in your testing environment of choice (e.g., Jest, Vitest), ensuring your tests are always in sync with your stories without having to rewrite them. This is what we refer to as portable stories in Storybook.

You must configure your test environment to use portable stories to ensure your stories are composed with all aspects of your Storybook configuration, such as decorators.

Once the test runs, it loads the story and renders it. Testing Library then emulates the user's behavior and checks if the component state has been updated.

By default, the setProjectAnnotations function injects into your existing tests any global configuration you've defined in your Storybook instanc

*[Content truncated - see full docs]*

**Examples**:

```python
import { fireEvent, render, screen } from '@testing-library/react';
 
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
import { composeStories } from '@storybook/your-framework';
 
import * as stories from './LoginForm.stories'; // 👈 Our stories imported here.
 
const { InvalidForm } = composeStories(stories);
 
test('Checks if the form is valid', async () => {
  // Renders the composed story
  await InvalidForm.run();
 
  const buttonElement
...
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import { composeStories } from '@storybook/your-framework';
 
import * as stories from './LoginForm.stories';
 
const { ValidForm } = composeStories(stories, {
  decorators: [
    // Decorators defined here will be added to all composed stories from this function
  ],
  globalTypes: {
    // Override globals for all composed stories from this function
  },
  parameters: {
    // Override paramete
...
```

```python
import { fireEvent, screen } from '@testing-library/react';
 
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
import { composeStory } from '@storybook/your-framework';
 
import Meta, { ValidForm as ValidFormStory } from './LoginForm.stories';
 
const ValidForm = composeStory(ValidFormStory, Meta);
 
test('Validates form', async () => {
  await ValidForm.run();
 
  const buttonElement = screen.getByRole('button', {
    name: 'Submit',
  });
 
...
```

---

## Tags

**URL**: https://storybook.js.org/docs/writing-stories/tags

**Contents**:
- Tags
- Built-in tags
- Applying tags
- Removing tags
- Filtering by custom tags
- Recipes
  - Docs-only stories
  - Combo stories, still tested individually

Tags allow you to control which stories are included in your Storybook, enabling many different uses of the same total set of stories. For example, you can use tags to include/exclude tests from the test runner. For more complex use cases, see the recipes section, below.

The following tags are available in every Storybook project:

The dev and test tags are automatically, implicitly applied to every story in your Storybook project.

A tag can be any static (i.e. not created dynamically) string, either the built-in tags or custom tags of your own design. To apply tags to a story, assign an array of strings to the tags property. Tags may be applied at the project, component (meta), or story levels.

For example, to apply the autodocs tag to all stories in your project, you can use .storybook/preview.js|ts:

Within a component stories file, you apply tags like so:

To remove a tag from a story, prefix it with !. For example:

Tags can be removed for all stories in your project (in .storybook/preview.js|ts), all stories for a component (in the CSF file meta), or a single story (as above).

Custom tags enable a flexible layer of categorization on top of Storybook's sidebar hierarchy. In the example above, we created an experimental tag to indicate that a story is not yet stable.

You can create custom tags for any purpose. Sample uses might include:

Custom tags are useful because they show up as filters in Storybook's sidebar. Selecting a tag in the filter causes the sidebar to only show stories with that tag. Selecting multiple tags shows stories that contain any of those tags.

Filtering by tags is a powerful way to focus on a subset of stories, especially in large Storybook projects. You can also narrow your stories by tag and then search within that subset.

It can sometimes be helpful to provide example stories for documentation purposes, but you want to keep the sidebar navigation more focused on stories useful for development. By enabling the autodocs tag and re

*[Content truncated - see full docs]*

**Examples**:

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Preview } from '@storybook/your-framework';
 
const preview: Preview = {
  // ...rest of preview
  /*
   * All stories in your project will have these tags applied:
   * - autodocs
   * - dev (implicit default)
   * - test (implicit default)
   */
  tags: ['autodocs'],
};
 
export default preview;
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Meta, StoryObj } from '@storybook/your-framework';
 
import { Button } from './Button';
 
const meta = {
  component: Button,
  /*
   * All stories in this file will have these tags applied:
   * - autodocs
   * - dev (implicit default, inherited from preview)
   * - test (implicit default, inherited from preview)
   */
  tags: ['autodocs'],
} satisfies Meta<typeof Button>;
 
export
...
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Meta, StoryObj } from '@storybook/your-framework';
 
import { Button } from './Button';
 
const meta = {
  component: Button,
  // 👇 Applies to all stories in this file
  tags: ['stable'],
} satisfies Meta<typeof Button>;
export default meta;
 
type Story = StoryObj<typeof meta>;
 
export const ExperimentalFeatureStory: Story = {
  //👇 For this particular story, remove the inherited
...
```

---

## stories

**URL**: https://storybook.js.org/docs/api/main-config/main-config-stories

**Contents**:
- stories
- With an array of globs
- With a configuration object
  - StoriesSpecifier
    - StoriesSpecifier.directory
    - StoriesSpecifier.files
    - StoriesSpecifier.titlePrefix
- With a custom implementation

Parent: main.js|ts configuration

Configures Storybook to load stories from the specified locations. The intention is for you to colocate a story file along with the component it documents:

If you want to use a different naming convention, you can alter the glob using the syntax supported by picomatch.

Keep in mind that some addons may assume Storybook's default naming convention.

Storybook will load stories from your project as found by this array of globs (pattern matching strings).

Stories are loaded in the order they are defined in the array. This allows you to control the order in which stories are displayed in the sidebar:

Additionally, you can customize your Storybook configuration to load your stories based on a configuration object. This object is of the type StoriesSpecifier, defined below.

For example, if you wanted to load your stories from a packages/components directory, you could adjust your stories configuration field into the following:

When Storybook starts, it will look for any file containing the stories extension inside the packages/components directory and generate the titles for your stories.

Where to start looking for story files, relative to the root of your project.

Default: '**/*.@(mdx|stories.@(js|jsx|mjs|ts|tsx))'

A glob, relative to StoriesSpecifier.directory (with no leading ./), that matches the filenames to load.

When auto-titling, prefix used when generating the title for your stories.

💡 Storybook now statically analyzes the configuration file to improve performance. Loading stories with a custom implementation may de-optimize or break this ability.

You can also adjust your Storybook configuration and implement custom logic to load your stories. For example, suppose you were working on a project that includes a particular pattern that the conventional ways of loading stories could not solve. In that case, you could adjust your configuration as follows:

**Examples**:

```javascript
| (string | StoriesSpecifier)[]
| async (list: (string | StoriesSpecifier)[]) => (string | StoriesSpecifier)[]
```

```text
•
└── components
    ├── Button.ts
    └── Button.stories.ts
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { StorybookConfig } from '@storybook/your-framework';
 
const config: StorybookConfig = {
  framework: '@storybook/your-framework',
  stories: ['../src/**/*.stories.@(js|jsx|mjs|ts|tsx)'],
};
 
export default config;
```

---
