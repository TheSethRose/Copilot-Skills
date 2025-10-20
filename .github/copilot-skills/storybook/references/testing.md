# Storybook - Testing

**Pages**: 5

---

## Accessibility tests

**URL**: https://storybook.js.org/docs/writing-tests/accessibility-testing

**Contents**:
- Accessibility tests
- Install the addon
- Check for violations
- Configure
  - Rulesets
  - Individual rules
  - Test behavior
  - Excluded elements

Web accessibility is the practice of making websites and apps accessible and inclusive to all people, regardless of ability or the technology they’re using. That means supporting requirements such as keyboard navigation, screen reader support, sufficient color contrast, etc.

Accessibility is not only the right thing to do, but it is increasingly mandated. For example, the European accessibility act is scheduled to go into law in June 2025. Similarly in the US, laws like the Americans with Disabilities Act (ADA) and Section 508 of the Rehabilitation Act apply to many public-facing services. Many of these laws are based on WCAG, a standardized guideline for making web content accessible.

Accessibility tests audit the rendered DOM against a set of heuristics based on WCAG rules and other industry-accepted best practices. They act as the first line of QA to catch blatant accessibility violations.

Storybook provides an Accessibility (a11y) addon to help ensure the accessibility of your components. It is built on top of Deque’s axe-core library, which automatically catches up to 57% of WCAG issues.

Run this command to install and configure the addon in your project:

Storybook's add command automates the addon's installation and setup. To install it manually, see our documentation on how to install addons.

Your Storybook will now include some features to check the accessibility of your components, including a button in the toolbar to simulate different vision impairments and an Accessibility addon panel to check for violations.

When you navigate to a story, automated accessibility checks are run and the results are reported in the Accessibility addon panel.

The results are broken down into three sub-tabs:

Because the addon is built on top of axe-core, much of the configuration available maps to its available options:

By default, Storybook disables the region rule, which does not typically apply to components in stories and can lead to false negatives.

We’ll shar

*[Content truncated - see full docs]*

**Examples**:

```text
npx storybook add @storybook/addon-a11y
```

```text
{
  rules: [
    {
      id: 'region',
      enabled: false,
    }
  ]
}
```

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { Preview } from '@storybook/your-framework';
 
const preview: Preview = {
  parameters: {
    a11y: {
      /*
       * Axe's context parameter
       * See https://github.com/dequelabs/axe-core/blob/develop/doc/API.md#context-parameter
       * to learn more. Typically, this is the CSS selector for the part of the DOM you want to analyze.
       */
      context: 'body',
      /*
  
...
```

---

## Interaction tests

**URL**: https://storybook.js.org/docs/writing-tests/interaction-testing

**Contents**:
- Interaction tests
- Writing interaction tests
  - Querying the canvas
  - Simulating behavior with userEvent
  - Asserting with expect
  - Spying on functions with fn
  - Run code before the component gets rendered
    - Create mock data before rendering

In Storybook, interaction tests are built as part of a story. That story renders the component with the necessary props and context to place it in an initial state. You then use a play function to simulate user behavior like clicks, typing, and submitting a form and then assert on the end result.

You can preview and debug your interaction tests using the Interactions panel in the Storybook UI. They can be automated using the Vitest addon, allowing you to run tests for your project in Storybook, terminal, or CI environments.

Every story you write can be render tested. A render test is a simple version of an interaction test that only tests the ability of a component to render successfully in a given state. That works fine for relatively simple, static components like a Button. But for more complex, interactive components, you can go farther.

You can simulate user behavior and assert on functional aspects like DOM structure or function calls using the play function. When a component is tested, the play function is ran and any assertions within it are validated.

In this example, the EmptyForm story tests the render of the LoginForm component and the FilledForm story tests the form submission:

There’s a lot going on in that code sample, so let’s walk through the APIs one-by-one.

canvas is a queryable element containing the story under test, which is provided as a parameter of your play function. You can use canvas to find specific elements to interact with or assert on. All query methods come directly from Testing Library and take the form of <type><subject>.

The available types are summarized in this table and fully documented in the Testing Library docs:

The subjects are listed here, with links to their full Testing Library documentation:

Note the order of this list! We (and Testing Libary) highly encourage you to query for elements in a way that resembles the way a real person would interact with your UI. For example, finding elements by their accessible rol

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

```text
// Find the first element with a role of button with the accessible name "Submit"
await canvas.findByRole('button', { name: 'Submit' });
 
// Get the first element with the text "An example heading"
canvas.getByText('An example heading');
 
// Get all elements with the role of listitem
canvas.getAllByRole('listitem');
```

```python
import { expect } from 'storybook/test';
```

---

## Snapshot tests

**URL**: https://storybook.js.org/docs/writing-tests/snapshot-testing

**Contents**:
- Snapshot tests
- Snapshot tests
- Get started with Portable Stories
- Snapshot testing a portable story
  - Verifying an error is thrown
- Snapshot testing with the test-runner
- FAQ
  - What’s the difference between snapshot tests and visual tests?

Snapshot testing is simply rendering a component in a given state, taking a snapshot of the rendered DOM or HTML, and then comparing it against the previous snapshot. They’re convenient to create, but can be difficult and noisy to maintain if the snapshot contains too much information. For UI components, visual tests (easier to review) or interaction tests (focused on functionality) are usually the better fit. However, there are some cases where snapshot testing may be necessary, such as ensuring an error is thrown correctly.

You can reuse your stories as the basis of snapshot tests within another test environment, like Jest or Vitest. To enable this, Storybook provides the Portable Stories API, which composes your stories with their annotations (args, decorators, parameters, etc) and produces a renderable element for your tests. Portable Stories are available for:

Looking for snapshot testing with Storyshots? Storyshots is deprecated and no longer maintained. We recommend using the Portable Stories API instead.

Please reference the Storyshots documentation for more information on how to migrate your tests.

If you’re using Storybook Test, your project is already configured to use Portable Stories in Vitest.

If you’re not using Storybook Test or would like to test in another testing environment, please follow the relevant documentation:

Snapshot testing a reusable story is a straightforward process of using composeStories from the Portable Stories API to get a renderable element, rendering that element, and then taking and comparing a snapshot.

This example renders a Button component in Vitest (by reusing one of Button’s stories) and asserts that the rendered HTML snapshot matches.

Once the test has run, a snapshot will be inserted or created. Then, when you run tests again and the snapshot doesn’t match, the test will fail and you will see output something like this:

How long did it take you to find what changed? (px-4 → px-3)

This is exactly why visual te

*[Content truncated - see full docs]*

**Examples**:

```python
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, nextjs-vite, etc.
import { composeStories } from '@storybook/your-framework';
 
import * as stories from '../stories/Button.stories';
 
const { Primary } = composeStories(stories);
test('Button snapshot', async () => {
  await Primary.run();
  expect(document.body.firstChild).toMatchSnapshot();
});
```

```text
FAIL  src/components/ui/Button.test.ts > Button snapshot
Error: Snapshot `Button snapshot 1` mismatched
 
- Expected
+ Received
 
  <div>
    <button
-     class="inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md text-sm font-medium transition-all disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 shrink-0 [&_svg]:shrink-0 outline-none focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3
...
```

```javascript
function Button(props) {
  if (props.doNotUseThisItWillThrowAnError) {
    throw new Error("I tried to tell you...")
  }
 
  return <button {...props} />
}
```

---

## Testing in CI

**URL**: https://storybook.js.org/docs/writing-tests/in-ci

**Contents**:
- Testing in CI
- Set up Storybook tests in CI
  - 1. Define package.json script
  - 2. Add a new CI workflow
    - 2.1 Debug test failures
    - 2.2 Calculate code coverage
  - 3. Run your workflow
- FAQs

The Vitest addon is great for automating your UI tests within Storybook. To have full confidence in your work, backed by tests, you need to run those automated tests in your continuous integration (CI) environment.

Thankfully, that’s quite easy!

If you cannot use the Vitest addon in your project, you can still run your stories as tests in CI using the test-runner. Follow the instructions in the test-runner documentation to set up the test-runner to run in CI in your project.

Running Storybook tests in CI is very similar to running them via CLI on your local machine: you run the same command, just in a different place.

Let’s go step-by-step to set things up.

For convenience, define a script in your package.json to run the Storybook tests. This is the same command you would run locally, but it’s useful to have it in your CI workflow.

This script calls the vitest CLI command and restricts it to the “storybook” project defined in your Vitest config, which was created when you installed the Vitest addon. (If you’ve renamed the project, adjust the script above accordingly.) You can also pass any additional vitest CLI options you may require.

Next, we’ll create a new “UI Tests” workflow to run in our CI environment. You may also adjust an existing workflow, if you prefer.

Here are some example configurations for popular CI providers:

Create a file in the root of your repo, .github/workflow/test-ui.yml:

Create a file in the root of your repo, .gitlab-ci.yml:

Create a file in the root of your repo, bitbucket-pipelines.yml:

Create a file in the root of your repo, .circleci/config.yml:

Create a file in the root of your repo, .travis.yml:

Create a file in the root of your repo, JenkinsFile:

Create a file in the root of your repo, azure-pipelines.yml:

Storybook Test uses Playwright to render your stories by default. For the fastest experience, you should use a machine image that has Playwright already installed (as in most of the snippets above).

When a Storyboo

*[Content truncated - see full docs]*

**Examples**:

```text
{ 
  "scripts": {
    "test-storybook": "vitest --project=storybook"
  }
}
```

```text
name: UI Tests
 
on: [push]
 
jobs:
  test:
    runs-on: ubuntu-latest
    container:
      # Make sure to grab the latest version of the Playwright image
      # https://playwright.dev/docs/docker#pull-the-image
      image: mcr.microsoft.com/playwright:v1.52.0-noble
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: 22.12.0
      
      - name: Install dependencies
        run: npm ci
      
   
...
```

```text
image: node:jod
 
stages:
  - UI_Tests
 
cache:
  key: $CI_COMMIT_REF_SLUG-$CI_PROJECT_DIR
  paths:
    - .npm/
 
before_script:
  # Install dependencies
  - npm ci
Test:
  stage: UI_Tests
  # Make sure to grab the latest version of the Playwright image
  # https://playwright.dev/docs/docker#pull-the-image
  image: mcr.microsoft.com/playwright:v1.52.0-noble
  script:
    - npm run test-storybook
```

---

## Visual tests

**URL**: https://storybook.js.org/docs/writing-tests/visual-testing

**Contents**:
- Visual tests
- Install the addon
- Enable visual tests
- Run visual tests
- Review changes
- Automate with CI
- PR checks
- Configure

Visual tests are the most efficient way to test your components. With the click of a button you can take snapshots of every story in your Storybook and compare those snapshots to baselines — last known “good” snapshots. Not only does this allow you to check the appearance of your components, but they are also able to check a large subset of component functionality without having to write or maintain any test code!

Storybook supports cross-browser visual testing natively using Chromatic, a cloud service made by the Storybook team. When you enable visual testing, every story is automatically turned into a test. This gives you instant feedback on UI bugs directly in Storybook.

Add visual tests to your project by installing @chromatic-com/storybook, the official addon by Storybook maintainers:

When you start Storybook, you'll see a new addon panel for Visual Tests where you can run tests and view results.

Already using the Vitest addon? In the expanded testing widget, you’ll now see a Visual tests section:

Clicking the Run tests button at the bottom will run all tests, both component and visual.

First, sign in to your Chromatic account. If you do not have an account, you can create one as part of the sign in process.

Once signed in, you will see your Chromatic account(s) and their projects. Either select one from the list or create a new one.

Now that you have linked your project to the addon, you can press the “Catch a UI change” button to run your first build of visual tests.

That first build will create the baseline snapshots for your stories, which will be compared against when you run visual tests again.

After you have made a code change, there are two ways to run visual tests in Storybook.

In the expanded testing widget in the sidebar, press the run button in the Visual tests section.

Or, in the Visual tests addon panel, press the run button in the top right corner of the panel.

Either method will send your stories to the cloud to take snapshots and d

*[Content truncated - see full docs]*

**Examples**:

```text
npx storybook@latest add @chromatic-com/storybook
```

```text
{
  "buildScriptName": "deploy-storybook",
  "debug": true,
  "projectId": "Project:64cbcde96f99841e8b007d75",
  "zip": true
}
```

---
