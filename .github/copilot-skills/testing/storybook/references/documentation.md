# Storybook - Documentation

**Pages**: 7

---

## Automatic documentation and Storybook

**URL**: https://storybook.js.org/docs/writing-docs/autodocs

**Contents**:
- Automatic documentation and Storybook
- Set up automated documentation
  - Configure
  - Write a custom template
    - With MDX
  - Generate a table of contents
  - Configure the table of contents
    - Component-level configuration

Storybook Autodocs is a powerful tool that can help you quickly generate comprehensive documentation for your UI components. By leveraging Autodocs, you're transforming your stories into living documentation which can be further extended with MDX and Doc Blocks to provide a clear and concise understanding of your components' functionality.

Storybook infers the relevant metadata (e.g., args, argTypes, parameters) and automatically generates a documentation page with this information positioned at the root-level of your component tree in the sidebar.

Autodocs is configured through tags. If a CSF file contains at least one story tagged with autodocs, then a documentation page will be generated for that component.

To enable automatic documentation for all stories in a project, add it to tags in your .storybook/preview.js|ts file:

You can also enable it at the component (or story) level:

You can disable auto docs for a particular component by removing the tag:

Similarly, you can exclude a particular story from the auto docs page, by removing the tag:

In addition to enabling the feature with tags, you can extend your Storybook configuration file (i.e., .storybook/main.js|ts|cjs) and provide additional options to control how documentation gets created. Listed below are the available options and examples of how to use them.

To replace the default documentation template used by Storybook, you can extend your UI configuration file (i.e., .storybook/preview.js|ts) and introduce a docs parameter. This parameter accepts a page function that returns a React component, which you can use to generate the required template. For example:

Internally, Storybook uses a similar implementation to generate the default template. See the Doc Blocks API reference to learn more about how Doc Blocks work.

Going over the code snippet in more detail. When Storybook starts up, it will override the default template with the custom one composed of the following:

You can also use MDX to gen

*[Content truncated - see full docs]*

**Examples**:

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Preview } from '@storybook/your-framework';
 
const preview: Preview = {
  // ...rest of preview
  //👇 Enables auto-generated documentation for all stories
  tags: ['autodocs'],
};
 
export default preview;
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Meta } from '@storybook/your-framework';
 
import { Button } from './Button';
 
const meta = {
  component: Button,
  //👇 Enables auto-generated documentation for this component and includes all stories in this file
  tags: ['autodocs'],
} satisfies Meta<typeof Button>;
export default meta;
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Meta } from '@storybook/your-framework';
 
import { Page } from './Page';
 
const meta = {
  component: Page,
  // 👇 Disable auto-generated documentation for this component
  tags: ['!autodocs'],
} satisfies Meta<typeof Page>;
export default meta;
```

---

## Code snippets contributions

**URL**: https://storybook.js.org/docs/contribute/documentation/new-snippets

**Contents**:
- Code snippets contributions
- Documented frameworks
- Snippet syntax
  - Example
- Common attributes for code snippets
  - File name as title
  - Language configuration
  - Framework-specific code

Add or update the code snippets in the documentation. This page outlines how the code snippets are structured.

Storybook maintains code snippets for a variety of frameworks. We try to keep them up to date as framework APIs evolve. But keeping track of every API change in every framework is tricky.

We welcome community contributions to the code snippets. Here's a matrix of the frameworks for which we have snippets. Help us add snippets for your favorite framework.

The code snippets referenced throughout the Storybook documentation are located in the docs/_snippets directory inside individual Markdown files, containing the supported frameworks, features and languages (i.e., JavaScript, MDX, TypeScript).

The following code block demonstrates how to structure a code snippet in the Storybook documentation and the attributes you can use to provide additional context to the code snippet.

Following are the attributes you'll use most often in the Storybook documentation code snippets, as well as a brief explanation of each to help you understand the context in which they are used.

Most code examples should include a file name so readers can understand which file they relate to and where to paste it into their project. For code examples, include the filename attribute wrapped with quotation marks to indicate the file name. This is not required if the example relates to a terminal command.

Use the language attribute to define the language to which the code snippet applies. The documentation uses this attribute to determine which variant to display (e.g., JavaScript, TypeScript, MDX).

Use the renderer attribute to indicate which of the supported frameworks the code snippet belongs to.

Alternatively, if you're documenting examples that apply to multiple frameworks, use the renderer attribute with the common value to indicate that the code snippet is framework-agnostic.

Use the packageManager attribute to configure the package manager used in the example from the follow

*[Content truncated - see full docs]*

**Examples**:

```python
```ts filename="ButtonGroup.stories.ts" renderer="vue" language="ts" tabTitle="3"
import type { Meta, StoryObj } from '@storybook/vue3-vite';
 
import ButtonGroup from './ButtonGroup.vue';
 
//👇 Imports the Button stories
import * as ButtonStories from './Button.stories';
 
const meta = {
  component: ButtonGroup,
}} satisfies Meta<typeof ButtonGroup>;
 
export default meta;
type Story = StoryObj<typeof meta>;
 
export const Pair: Story = {
  render: (args) => ({
    components: { ButtonGroup },
...
```

```text
```ts filename="Button.stories.ts"
```
```

```text
```ts filename="Button.stories.ts" language="js|ts|mdx"
```
```

---

## Doc blocks

**URL**: https://storybook.js.org/docs/writing-docs/doc-blocks

**Contents**:
- Doc blocks
- Within MDX
- Customizing the automatic docs page
- Customizing doc blocks
- Available blocks
  - ArgTypes
  - Canvas
  - ColorPalette

Storybook offers several doc blocks to help document your components and other aspects of your project.

There are two common ways to use doc blocks in Storybook, within MDX and as part of the docs page template.

The blocks are most commonly used within Storybook's MDX documentation:

The blocks are also used to define the page template for automatics docs. For example, here's the default template:

If you override the default page template, you can similarly use Doc Blocks to build the perfect documentation page for your project.

Note that some doc blocks render other blocks. For example, the <Stories /> block expands to:

As a result, for example, customizing the Source block via parameters (see next section) will also affect the Source blocks rendered as part of Canvas blocks.

In both use cases (MDX and automatic docs), many of the doc blocks can be customized via parameters.

For example, you can filter out the style prop from all Controls tables through your Storybook:

Parameters can also be defined at the component (or meta) level or the story level, allowing you to customize Doc Blocks exactly as you need, where you need.

The blocks that accept customization via parameters are marked in the list of available blocks below.

When using a doc block in MDX, it can also be customized with its props:

Each block has a dedicated API reference page detailing usage, available options, and technical details.

Accepts parameters in the namespace parameters.docs.argTypes.

The ArgTypes block can be used to show a static table of arg types for a given component as a way to document its interface.

Accepts parameters in the namespace parameters.docs.canvas.

The Canvas block is a wrapper around a Story, featuring a toolbar that allows you to interact with its content while automatically providing the required Source snippets.

The ColorPalette block allows you to document all color-related items (e.g., swatches) used throughout your project.

Accepts parameters in the

*[Content truncated - see full docs]*

**Examples**:

```python
import { Meta, Primary, Controls, Story } from '@storybook/addon-docs/blocks';
 
import * as ButtonStories from './Button.stories';
 
<Meta of={ButtonStories} />
 
# Button
 
A button is ...
 
<Primary />
 
## Props
 
<Controls />
 
## Stories
 
### Primary
 
A button can be of primary importance.
 
<Story of={ButtonStories.Primary} />
 
A button can be of secondary importance.
 
<Story of={ButtonStories.Secondary} />
 
{/* ... */}
```

```python
import { Title, Subtitle, Description, Primary, Controls, Stories } from '@storybook/addon-docs/blocks';
 
export const autoDocsTemplate = () => (
  <>
    <Title />
    <Subtitle />
    <Description />
    <Primary />
    <Controls />
    <Stories />
  </>
);
```

```text
## Stories
 
<Canvas>
  ### Story name
  <Description />
  <Story />
  <Source />
</Canvas>
 
{/* ... repeat <Canvas> for each story */}
```

---

## Documentation updates

**URL**: https://storybook.js.org/docs/contribute/documentation/documentation-updates

**Contents**:
- Documentation updates
- Find the Markdown file
- Create the pull request

Fix a typo or clarify a section of the docs. This page outlines how to edit the documentation.

Scroll to the bottom of the document in question, then click ✍️ Edit on GitHub – PRs welcome! This will open the Markdown file on GitHub.

Use GitHub's web editor by clicking the pencil icon on the right-hand corner. Tweak the document to your liking.

Scroll down to the bottom of the document page on GitHub and describe what you changed and why. Select the Create a new branch for this commit and start a pull request option then click the Propose changes button.

In the Storybook repository, create a pull request that describes changes and includes additional context that would help maintainers review. Once you submit the PR, a maintainer will guide you through the triage and merge process.

Learn more about contributing to Storybook

---

## How to document components

**URL**: https://storybook.js.org/docs/writing-docs

**Contents**:
- How to document components

When you write component stories during development, you also create basic documentation to revisit later.

Storybook gives you tools to expand this essential documentation with prose and layout that feature your components and stories prominently. That allows you to create UI library usage guidelines, design system sites, and more.

If you're including Storybook in your project for the first time, we provide you with a documentation page ("Autodocs" for short), positioned near your stories. It's a baseline template automatically generated, listing your existing stories and relevant metadata.

Additionally, you can customize this template if needed or create free-form pages for each component using MDX. In both cases, you’ll use Doc Blocks as the building blocks to create full-featured documentation.

Docs is autoconfigured to work out of the box in most use cases. In some cases, you may need or want to tweak the configuration. Read more about it here.

---

## MDX

**URL**: https://storybook.js.org/docs/writing-docs/mdx

**Contents**:
- MDX
- Basic example
  - MDX and CSF
  - Anatomy of MDX
  - Known limitations
- Setup custom documentation
  - Using the Meta Doc Block
  - Writing unattached documentation

MDX files mix Markdown and Javascript/JSX to create rich interactive documentation. You can use Markdown’s readable syntax (such as # heading) for your documentation, include stories defined in Component Story Format (CSF), and freely embed JSX component blocks at any point in the file. All at once.

In addition, you can write pure documentation pages in MDX and add them to Storybook alongside your stories.

Let's start with an example, Checkbox.mdx, combining Markdown with a single story.

This MDX file references a story file, Checkbox.stories.js|ts, that is written in Component Story Format (CSF):

And here's how that's rendered in Storybook:

There’s a lot going on here. We're writing Markdown, we're writing JSX, and we're also defining and referencing Storybook stories that are drop-in compatible with the entire Storybook ecosystem.

The first thing you'll notice is that the component documentation is divided into distinct formats: one for writing component stories describing each possible component state and the second one for documenting how to use them. This split leverages the best qualities of each format:

Assuming you’re already familiar with writing stories with CSF, we can dissect the MDX side of things in greater detail.

The document consists of a number of blocks separated by blank lines. Since MDX mixes a few different languages together, it uses those blank lines to help distinguish where one starts, and the next begins. Failing to separate blocks by whitespace can cause (sometimes cryptic) parse errors.

Going through the code blocks in sequence:

Comments in MDX are JSX blocks that contain JS comments.

Imports the components and stories that will be used in the JSX throughout the rest of the file.

When providing the of prop to the Meta block, make sure that you're referencing the default export of the story file and not the component itself to prevent render issues with the generated documentation.

The Meta block defines where the document wi

*[Content truncated - see full docs]*

**Examples**:

```python
import { Canvas, Meta } from '@storybook/addon-docs/blocks';
 
import * as CheckboxStories from './Checkbox.stories';
 
<Meta of={CheckboxStories} />
 
# Checkbox
 
A checkbox is a square box that can be activated or deactivated when ticked.
 
Use checkboxes to select one or more options from a list of choices.
 
<Canvas of={CheckboxStories.Unchecked} />
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Meta, StoryObj } from '@storybook/your-framework';
 
import { Checkbox } from './Checkbox';
 
const meta = {
  component: Checkbox,
} satisfies Meta<typeof Checkbox>;
 
export default meta;
type Story = StoryObj<typeof meta>;
 
export const Unchecked: Story = {
  args: {
    label: 'Unchecked',
  },
};
```

```text
{ /* Checkbox.mdx */ }
```

---

## Preview and build docs

**URL**: https://storybook.js.org/docs/writing-docs/build-documentation

**Contents**:
- Preview and build docs
- Preview Storybook's documentation
- Publish Storybook's documentation

Storybook allows you to create rich and extensive documentation that will help you and any other stakeholder involved in the development process. Out of the box you have the tooling required to not only write it but also to preview it and build it.

At any point during your development, you can preview the documentation you've written. Storybook allows you to generate a preview of the final documentation when you use the --docs flag. We recommend including it in your package.json as a new script:

Depending on your configuration, when you execute the storybook-docs script. Storybook will be put into documentation mode and will generate a different build.

It will look for any stories available either in MDX or CSF and based on the documentation you've added it will display it...

There's some caveats to this build mode, as to the normal Storybook build:

You can also publish your documentation the same you would publish your Storybook. You can use the --docs flag with the storybook build command. We recommend as well including it as a script in your package.json file:

Based on the configuration you have, when the build-storybook-docs script is executed, Storybook once again will be put into documentation mode and will generate a different build and output the documentation into the storybook-static folder.

The same caveats mentioned above will apply.

You can use any hosting provider to deploy your documentation, for instance:

Learn more about Storybook documentation

**Examples**:

```text
{
  "scripts": {
    "storybook-docs": "storybook dev --docs"
  }
}
```

```text
{
  "scripts": {
    "build-storybook-docs": "storybook build --docs"
  }
}
```

---
