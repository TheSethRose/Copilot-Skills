# React - Reference

**Pages**: 94

---

## Built-in React APIs – React

**URL**: https://react.dev/reference/react/apis

**Contents**:
- Built-in React APIs
- Resource APIs

In addition to Hooks and Components, the react package exports a few other APIs that are useful for defining components. This page lists all the remaining modern React APIs.

Resources can be accessed by a component without having them as part of their state. For example, a component can read a message from a Promise or read styling information from a context.

To read a value from a resource, use this API:

**Examples**:

```javascript
function MessageComponent({ messagePromise }) {  const message = use(messagePromise);  const theme = use(ThemeContext);  // ...}
```

---

## Built-in React Components – React

**URL**: https://react.dev/reference/react/components

**Contents**:
- Built-in React Components
- Built-in components
- Your own components

React exposes a few built-in components that you can use in your JSX.

You can also define your own components as JavaScript functions.

---

## Built-in React DOM Hooks – React

**URL**: https://react.dev/reference/react-dom/hooks

**Contents**:
- Built-in React DOM Hooks
- Form Hooks

The react-dom package contains Hooks that are only supported for web applications (which run in the browser DOM environment). These Hooks are not supported in non-browser environments like iOS, Android, or Windows applications. If you are looking for Hooks that are supported in web browsers and other environments see the React Hooks page. This page lists all the Hooks in the react-dom package.

Forms let you create interactive controls for submitting information. To manage forms in your components, use one of these Hooks:

**Examples**:

```javascript
function Form({ action }) {  async function increment(n) {    return n + 1;  }  const [count, incrementFormAction] = useActionState(increment, 0);  return (    <form action={action}>      <button formAction={incrementFormAction}>Count: {count}</button>      <Button />    </form>  );}function Button() {  const { pending } = useFormStatus();  return (    <button disabled={pending} type="submit">      Submit    </button>  );}
```

---

## Built-in React Hooks – React

**URL**: https://react.dev/reference/react/hooks

**Contents**:
- Built-in React Hooks
- State Hooks
- Context Hooks
- Ref Hooks
- Effect Hooks
- Performance Hooks
- Other Hooks
- Your own Hooks

Hooks let you use different React features from your components. You can either use the built-in Hooks or combine them to build your own. This page lists all built-in Hooks in React.

State lets a component “remember” information like user input. For example, a form component can use state to store the input value, while an image gallery component can use state to store the selected image index.

To add state to a component, use one of these Hooks:

Context lets a component receive information from distant parents without passing it as props. For example, your app’s top-level component can pass the current UI theme to all components below, no matter how deep.

Refs let a component hold some information that isn’t used for rendering, like a DOM node or a timeout ID. Unlike with state, updating a ref does not re-render your component. Refs are an “escape hatch” from the React paradigm. They are useful when you need to work with non-React systems, such as the built-in browser APIs.

Effects let a component connect to and synchronize with external systems. This includes dealing with network, browser DOM, animations, widgets written using a different UI library, and other non-React code.

Effects are an “escape hatch” from the React paradigm. Don’t use Effects to orchestrate the data flow of your application. If you’re not interacting with an external system, you might not need an Effect.

There are two rarely used variations of useEffect with differences in timing:

A common way to optimize re-rendering performance is to skip unnecessary work. For example, you can tell React to reuse a cached calculation or to skip a re-render if the data has not changed since the previous render.

To skip calculations and unnecessary re-rendering, use one of these Hooks:

Sometimes, you can’t skip re-rendering because the screen actually needs to update. In that case, you can improve performance by separating blocking updates that must be synchronous (like typing into an input) from no

*[Content truncated - see full docs]*

**Examples**:

```javascript
function ImageGallery() {  const [index, setIndex] = useState(0);  // ...
```

```javascript
function Button() {  const theme = useContext(ThemeContext);  // ...
```

```javascript
function Form() {  const inputRef = useRef(null);  // ...
```

---

## Client React DOM APIs – React

**URL**: https://react.dev/reference/react-dom/client

**Contents**:
- Client React DOM APIs
- Client APIs
- Browser support

The react-dom/client APIs let you render React components on the client (in the browser). These APIs are typically used at the top level of your app to initialize your React tree. A framework may call them for you. Most of your components don’t need to import or use them.

React supports all popular browsers, including Internet Explorer 9 and above. Some polyfills are required for older browsers such as IE 9 and IE 10.

---

## Common components (e.g. <div>) – React

**URL**: https://react.dev/reference/react-dom/components/common

**Contents**:
- Common components (e.g. <div>)
- Reference
  - Common components (e.g. <div>)
    - Props
    - Caveats
  - ref callback function
    - Parameters
  - Note

All built-in browser components, such as <div>, support some common props and events.

See more examples below.

These special React props are supported for all built-in components:

children: A React node (an element, a string, a number, a portal, an empty node like null, undefined and booleans, or an array of other React nodes). Specifies the content inside the component. When you use JSX, you will usually specify the children prop implicitly by nesting tags like <div><span /></div>.

dangerouslySetInnerHTML: An object of the form { __html: '<p>some html</p>' } with a raw HTML string inside. Overrides the innerHTML property of the DOM node and displays the passed HTML inside. This should be used with extreme caution! If the HTML inside isn’t trusted (for example, if it’s based on user data), you risk introducing an XSS vulnerability. Read more about using dangerouslySetInnerHTML.

ref: A ref object from useRef or createRef, or a ref callback function, or a string for legacy refs. Your ref will be filled with the DOM element for this node. Read more about manipulating the DOM with refs.

suppressContentEditableWarning: A boolean. If true, suppresses the warning that React shows for elements that both have children and contentEditable={true} (which normally do not work together). Use this if you’re building a text input library that manages the contentEditable content manually.

suppressHydrationWarning: A boolean. If you use server rendering, normally there is a warning when the server and the client render different content. In some rare cases (like timestamps), it is very hard or impossible to guarantee an exact match. If you set suppressHydrationWarning to true, React will not warn you about mismatches in the attributes and the content of that element. It only works one level deep, and is intended to be used as an escape hatch. Don’t overuse it. Read about suppressing hydration errors.

style: An object with CSS styles, for example { fontWeight: 'bold', margin: 

*[Content truncated - see full docs]*

**Examples**:

```text
<div className="wrapper">Some content</div>
```

```javascript
<div ref={(node) => {  console.log('Attached', node);  return () => {    console.log('Clean up', node)  }}}>
```

```javascript
<button onClick={e => {  console.log(e); // React event object}} />
```

---

## Compiling Libraries – React

**URL**: https://react.dev/reference/react-compiler/compiling-libraries

**Contents**:
- Compiling Libraries
- Why Ship Compiled Code?
- Setting Up Compilation
- Backwards Compatibility
  - 1. Install the runtime package
  - 2. Configure the target version
- Testing Strategy
- Troubleshooting

This guide helps library authors understand how to use React Compiler to ship optimized library code to their users.

As a library author, you can compile your library code before publishing to npm. This provides several benefits:

Add React Compiler to your library’s build process:

Configure your build tool to compile your library. For example, with Babel:

If your library supports React versions below 19, you’ll need additional configuration:

We recommend installing react-compiler-runtime as a direct dependency:

Set the minimum React version your library supports:

Test your library both with and without compilation to ensure compatibility. Run your existing test suite against the compiled code, and also create a separate test configuration that bypasses the compiler. This helps catch any issues that might arise from the compilation process and ensures your library works correctly in all scenarios.

If your compiled library throws errors in React 17 or 18:

Some Babel plugins may conflict with React Compiler:

If users see “Cannot find module ‘react-compiler-runtime’“:

**Examples**:

```text
// babel.config.jsmodule.exports = {  plugins: [    'babel-plugin-react-compiler',  ],  // ... other config};
```

```text
{  "dependencies": {    "react-compiler-runtime": "^1.0.0"  },  "peerDependencies": {    "react": "^17.0.0 || ^18.0.0 || ^19.0.0"  }}
```

```text
{  target: '17', // Minimum supported React version}
```

---

## Component – React

**URL**: https://react.dev/reference/react/Component

**Contents**:
- Component
  - Pitfall
- Reference
  - Component
  - context
  - Note
  - props
  - Note

We recommend defining components as functions instead of classes. See how to migrate.

Component is the base class for the React components defined as JavaScript classes. Class components are still supported by React, but we don’t recommend using them in new code.

To define a React component as a class, extend the built-in Component class and define a render method:

Only the render method is required, other methods are optional.

See more examples below.

The context of a class component is available as this.context. It is only available if you specify which context you want to receive using static contextType.

A class component can only read one context at a time.

Reading this.context in class components is equivalent to useContext in function components.

The props passed to a class component are available as this.props.

Reading this.props in class components is equivalent to declaring props in function components.

The state of a class component is available as this.state. The state field must be an object. Do not mutate the state directly. If you wish to change the state, call setState with the new state.

Defining state in class components is equivalent to calling useState in function components.

The constructor runs before your class component mounts (gets added to the screen). Typically, a constructor is only used for two purposes in React. It lets you declare state and bind your class methods to the class instance:

If you use modern JavaScript syntax, constructors are rarely needed. Instead, you can rewrite this code above using the public class field syntax which is supported both by modern browsers and tools like Babel:

A constructor should not contain any side effects or subscriptions.

constructor should not return anything.

Do not run any side effects or subscriptions in the constructor. Instead, use componentDidMount for that.

Inside a constructor, you need to call super(props) before any other statement. If you don’t do that, this.props will

*[Content truncated - see full docs]*

**Examples**:

```text
class Greeting extends Component {  render() {    return <h1>Hello, {this.props.name}!</h1>;  }}
```

```python
import { Component } from 'react';class Greeting extends Component {  render() {    return <h1>Hello, {this.props.name}!</h1>;  }}
```

```javascript
class Button extends Component {  static contextType = ThemeContext;  render() {    const theme = this.context;    const className = 'button-' + theme;    return (      <button className={className}>        {this.props.children}      </button>    );  }}
```

---

## Components and Hooks must be pure – React

**URL**: https://react.dev/reference/rules/components-and-hooks-must-be-pure

**Contents**:
- Components and Hooks must be pure
  - Note
  - Why does purity matter?
    - How does React run your code?
      - Deep Dive
    - How to tell if code runs in render
- Components and Hooks must be idempotent
- Side effects must run outside of render

Pure functions only perform a calculation and nothing more. It makes your code easier to understand, debug, and allows React to automatically optimize your components and Hooks correctly.

This reference page covers advanced topics and requires familiarity with the concepts covered in the Keeping Components Pure page.

One of the key concepts that makes React, React is purity. A pure component or hook is one that is:

When render is kept pure, React can understand how to prioritize which updates are most important for the user to see first. This is made possible because of render purity: since components don’t have side effects in render, React can pause rendering components that aren’t as important to update, and only come back to them later when it’s needed.

Concretely, this means that rendering logic can be run multiple times in a way that allows React to give your user a pleasant user experience. However, if your component has an untracked side effect – like modifying the value of a global variable during render – when React runs your rendering code again, your side effects will be triggered in a way that won’t match what you want. This often leads to unexpected bugs that can degrade how your users experience your app. You can see an example of this in the Keeping Components Pure page.

React is declarative: you tell React what to render, and React will figure out how best to display it to your user. To do this, React has a few phases where it runs your code. You don’t need to know about all of these phases to use React well. But at a high level, you should know about what code runs in render, and what runs outside of it.

Rendering refers to calculating what the next version of your UI should look like. After rendering, Effects are flushed (meaning they are run until there are no more left) and may update the calculation if the Effects have impacts on layout. React takes this new calculation and compares it to the calculation used to create the previous versio

*[Content truncated - see full docs]*

**Examples**:

```javascript
function Dropdown() {  const selectedItems = new Set(); // created during render  // ...}
```

```javascript
function Dropdown() {  const selectedItems = new Set();  const onSelect = (item) => {    // this code is in an event handler, so it's only run when the user triggers this    selectedItems.add(item);  }}
```

```javascript
function Dropdown() {  const selectedItems = new Set();  useEffect(() => {    // this code is inside of an Effect, so it only runs after rendering    logForAnalytics(selectedItems);  }, [selectedItems]);}
```

---

## Configuration – React

**URL**: https://react.dev/reference/react-compiler/configuration

**Contents**:
- Configuration
  - Note
- Compilation Control
- Version Compatibility
- Error Handling
- Debugging
- Feature Flags
- Common Configuration Patterns

This page lists all configuration options available in React Compiler.

For most apps, the default options should work out of the box. If you have a special need, you can use these advanced options.

These options control what the compiler optimizes and how it selects components and hooks to compile.

React version configuration ensures the compiler generates code compatible with your React version.

target specifies which React version you’re using (17, 18, or 19).

These options control how the compiler responds to code that doesn’t follow the Rules of React.

panicThreshold determines whether to fail the build or skip problematic components.

Logging and analysis options help you understand what the compiler is doing.

logger provides custom logging for compilation events.

Conditional compilation lets you control when optimized code is used.

gating enables runtime feature flags for A/B testing or gradual rollouts.

For most React 19 applications, the compiler works without configuration:

Older React versions need the runtime package and target configuration:

Start with specific directories and expand gradually:

**Examples**:

```text
// babel.config.jsmodule.exports = {  plugins: [    [      'babel-plugin-react-compiler', {        // compiler options      }    ]  ]};
```

```javascript
{  compilationMode: 'annotation' // Only compile "use memo" functions}
```

```text
// For React 18 projects{  target: '18' // Also requires react-compiler-runtime package}
```

---

## Directives – React

**URL**: https://react.dev/reference/rsc/directives

**Contents**:
- Directives
  - React Server Components
- Source code directives

Directives are for use in React Server Components.

Directives provide instructions to bundlers compatible with React Server Components.

---

## Directives – React

**URL**: https://react.dev/reference/react-compiler/directives

**Contents**:
- Directives
- Overview
  - Available directives
  - Quick comparison
- Usage
  - Function-level directives
  - Module-level directives
  - Compilation modes interaction

React Compiler directives are special string literals that control whether specific functions are compiled.

React Compiler directives provide fine-grained control over which functions are optimized by the compiler. They are string literals placed at the beginning of a function body or at the top of a module.

Place directives at the beginning of a function to control its compilation:

Place directives at the top of a file to affect all functions in that module:

Directives behave differently depending on your compilationMode:

Directives are escape hatches. Prefer configuring the compiler at the project level:

Always explain why a directive is used:

Opt-out directives should be temporary:

When adopting the React Compiler in a large codebase:

For specific issues with directives, see the troubleshooting sections in:

**Examples**:

```javascript
function MyComponent() {  "use memo"; // Opt this component into compilation  return <div>{/* ... */}</div>;}
```

```javascript
// Opt into compilationfunction OptimizedComponent() {  "use memo";  return <div>This will be optimized</div>;}// Opt out of compilationfunction UnoptimizedComponent() {  "use no memo";  return <div>This won't be optimized</div>;}
```

```javascript
// At the very top of the file"use memo";// All functions in this file will be compiledfunction Component1() {  return <div>Compiled</div>;}function Component2() {  return <div>Also compiled</div>;}// Can be overridden at function levelfunction Component3() {  "use no memo"; // This overrides the module directive  return <div>Not compiled</div>;}
```

---

## <Fragment> (<>...</>) – React

**URL**: https://react.dev/reference/react/Fragment

**Contents**:
- <Fragment> (<>...</>)
  - Canary
- Reference
  - <Fragment>
    - Props
  - Canary only FragmentInstance
    - Caveats
- Usage

<Fragment>, often used via <>...</> syntax, lets you group elements without a wrapper node.

Wrap elements in <Fragment> to group them together in situations where you need a single element. Grouping elements in Fragment has no effect on the resulting DOM; it is the same as if the elements were not grouped. The empty JSX tag <></> is shorthand for <Fragment></Fragment> in most cases.

When you pass a ref to a fragment, React provides a FragmentInstance object with methods for interacting with the DOM nodes wrapped by the fragment:

Event handling methods:

Focus management methods:

If you want to pass key to a Fragment, you can’t use the <>...</> syntax. You have to explicitly import Fragment from 'react' and render <Fragment key={yourKey}>...</Fragment>.

React does not reset state when you go from rendering <><Child /></> to [<Child />] or back, or when you go from rendering <><Child /></> to <Child /> and back. This only works a single level deep: for example, going from <><><Child /></></> to <Child /> resets the state. See the precise semantics here.

Canary only If you want to pass ref to a Fragment, you can’t use the <>...</> syntax. You have to explicitly import Fragment from 'react' and render <Fragment ref={yourRef}>...</Fragment>.

Use Fragment, or the equivalent <>...</> syntax, to group multiple elements together. You can use it to put multiple elements in any place where a single element can go. For example, a component can only return one element, but by using a Fragment you can group multiple elements together and then return them as a group:

Fragments are useful because grouping elements with a Fragment has no effect on layout or styles, unlike if you wrapped the elements in another container like a DOM element. If you inspect this example with the browser tools, you’ll see that all <h1> and <article> DOM nodes appear as siblings without wrappers around them:

The example above is equivalent to importing Fragment from React:

Usually you won’t nee

*[Content truncated - see full docs]*

**Examples**:

```text
<>  <OneChild />  <AnotherChild /></>
```

```javascript
function Post() {  return (    <>      <PostTitle />      <PostBody />    </>  );}
```

```python
import { Fragment } from 'react';function Post() {  return (    <Fragment>      <PostTitle />      <PostBody />    </Fragment>  );}
```

---

## Legacy React APIs – React

**URL**: https://react.dev/reference/react/legacy

**Contents**:
- Legacy React APIs
- Legacy APIs
- Removed APIs

These APIs are exported from the react package, but they are not recommended for use in newly written code. See the linked individual API pages for the suggested alternatives.

These APIs were removed in React 19:

---

## <Profiler> – React

**URL**: https://react.dev/reference/react/Profiler

**Contents**:
- <Profiler>
- Reference
  - <Profiler>
    - Props
    - Caveats
  - onRender callback
    - Parameters
- Usage

<Profiler> lets you measure rendering performance of a React tree programmatically.

Wrap a component tree in a <Profiler> to measure its rendering performance.

React will call your onRender callback with information about what was rendered.

Wrap the <Profiler> component around a React tree to measure its rendering performance.

It requires two props: an id (string) and an onRender callback (function) which React calls any time a component within the tree “commits” an update.

Profiling adds some additional overhead, so it is disabled in the production build by default. To opt into production profiling, you need to enable a special production build with profiling enabled.

<Profiler> lets you gather measurements programmatically. If you’re looking for an interactive profiler, try the Profiler tab in React Developer Tools. It exposes similar functionality as a browser extension.

Components wrapped in <Profiler> will also be marked in the Component tracks of React Performance tracks even in profiling builds. In development builds, all components are marked in the Components track regardless of whether they’re wrapped in <Profiler>.

You can use multiple <Profiler> components to measure different parts of your application:

You can also nest <Profiler> components:

Although <Profiler> is a lightweight component, it should be used only when necessary. Each use adds some CPU and memory overhead to an application.

**Examples**:

```text
<Profiler id="App" onRender={onRender}>  <App /></Profiler>
```

```text
<Profiler id="App" onRender={onRender}>  <App /></Profiler>
```

```javascript
function onRender(id, phase, actualDuration, baseDuration, startTime, commitTime) {  // Aggregate or log render timings...}
```

---

## React DOM APIs – React

**URL**: https://react.dev/reference/react-dom

**Contents**:
- React DOM APIs
- APIs
- Resource Preloading APIs
- Entry points
- Removed APIs

The react-dom package contains methods that are only supported for the web applications (which run in the browser DOM environment). They are not supported for React Native.

These APIs can be imported from your components. They are rarely used:

These APIs can be used to make apps faster by pre-loading resources such as scripts, stylesheets, and fonts as soon as you know you need them, for example before navigating to another page where the resources will be used.

React-based frameworks frequently handle resource loading for you, so you might not have to call these APIs yourself. Consult your framework’s documentation for details.

The react-dom package provides two additional entry points:

These APIs were removed in React 19:

---

## React DOM Components – React

**URL**: https://react.dev/reference/react-dom/components

**Contents**:
- React DOM Components
- Common components
- Form components
- Resource and Metadata Components
- All HTML components
  - Note
  - Custom HTML elements
    - Setting values on custom elements

React supports all of the browser built-in HTML and SVG components.

All of the built-in browser components support some props and events.

This includes React-specific props like ref and dangerouslySetInnerHTML.

These built-in browser components accept user input:

They are special in React because passing the value prop to them makes them controlled.

These built-in browser components let you load external resources or annotate the document with metadata:

They are special in React because React can render them into the document head, suspend while resources are loading, and enact other behaviors that are described on the reference page for each specific component.

React supports all built-in browser HTML components. This includes:

Similar to the DOM standard, React uses a camelCase convention for prop names. For example, you’ll write tabIndex instead of tabindex. You can convert existing HTML to JSX with an online converter.

If you render a tag with a dash, like <my-element>, React will assume you want to render a custom HTML element.

If you render a built-in browser HTML element with an is attribute, it will also be treated as a custom element.

Custom elements have two methods of passing data into them:

By default, React will pass values bound in JSX as attributes:

Non-string JavaScript values passed to custom elements will be serialized by default:

React will, however, recognize an custom element’s property as one that it may pass arbitrary values to if the property name shows up on the class during construction:

A common pattern when using custom elements is that they may dispatch CustomEvents rather than accept a function to call when an event occur. You can listen for these events using an on prefix when binding to the event via JSX.

Events are case-sensitive and support dashes (-). Preserve the casing of the event and include all dashes when listening for custom element’s events:

React supports all built-in browser SVG components. This includes:

*[Content truncated - see full docs]*

**Examples**:

```text
<my-element value="Hello, world!"></my-element>
```

```text
// Will be passed as `"1,2,3"` as the output of `[1,2,3].toString()`<my-element value={[1,2,3]}></my-element>
```

```text
// Listens for `say-hi` events<my-element onsay-hi={console.log}></my-element>// Listens for `sayHi` events<my-element onsayHi={console.log}></my-element>
```

---

## React Reference Overview – React

**URL**: https://react.dev/reference/react

**Contents**:
- React Reference Overview
- React
- React DOM
- React Compiler
- ESLint Plugin React Hooks
- Rules of React
- Legacy APIs

This section provides detailed reference documentation for working with React. For an introduction to React, please visit the Learn section.

The React reference documentation is broken down into functional subsections:

Programmatic React features:

React-dom contains features that are only supported for web applications (which run in the browser DOM environment). This section is broken into the following:

The React Compiler is a build-time optimization tool that automatically memoizes your React components and values:

The ESLint plugin for React Hooks helps enforce the Rules of React:

React has idioms — or rules — for how to express patterns in a way that is easy to understand and yields high-quality applications:

---

## React calls Components and Hooks – React

**URL**: https://react.dev/reference/rules/react-calls-components-and-hooks

**Contents**:
- React calls Components and Hooks
- Never call component functions directly
- Never pass around Hooks as regular values
  - Don’t dynamically mutate a Hook
  - Don’t dynamically use Hooks

React is responsible for rendering components and Hooks when necessary to optimize the user experience. It is declarative: you tell React what to render in your component’s logic, and React will figure out how best to display it to your user.

Components should only be used in JSX. Don’t call them as regular functions. React should call it.

React must decide when your component function is called during rendering. In React, you do this using JSX.

If a component contains Hooks, it’s easy to violate the Rules of Hooks when components are called directly in a loop or conditionally.

Letting React orchestrate rendering also allows a number of benefits:

Hooks should only be called inside of components or Hooks. Never pass it around as a regular value.

Hooks allow you to augment a component with React features. They should always be called as a function, and never passed around as a regular value. This enables local reasoning, or the ability for developers to understand everything a component can do by looking at that component in isolation.

Breaking this rule will cause React to not automatically optimize your component.

Hooks should be as “static” as possible. This means you shouldn’t dynamically mutate them. For example, this means you shouldn’t write higher order Hooks:

Hooks should be immutable and not be mutated. Instead of mutating a Hook dynamically, create a static version of the Hook with the desired functionality.

Hooks should also not be dynamically used: for example, instead of doing dependency injection in a component by passing a Hook as a value:

You should always inline the call of the Hook into that component and handle any logic in there.

This way, <Button /> is much easier to understand and debug. When Hooks are used in dynamic ways, it increases the complexity of your app greatly and inhibits local reasoning, making your team less productive in the long term. It also makes it easier to accidentally break the Rules of Hooks that Hooks should n

*[Content truncated - see full docs]*

**Examples**:

```javascript
function BlogPost() {  return <Layout><Article /></Layout>; // ✅ Good: Only use components in JSX}
```

```javascript
function BlogPost() {  return <Layout>{Article()}</Layout>; // 🔴 Bad: Never call them directly}
```

```javascript
function ChatInput() {  const useDataWithLogging = withLogging(useData); // 🔴 Bad: don't write higher order Hooks  const data = useDataWithLogging();}
```

---

## Rules of Hooks – React

**URL**: https://react.dev/reference/rules/rules-of-hooks

**Contents**:
- Rules of Hooks
- Only call Hooks at the top level
  - Note
- Only call Hooks from React functions

Hooks are defined using JavaScript functions, but they represent a special type of reusable UI logic with restrictions on where they can be called.

Functions whose names start with use are called Hooks in React.

Don’t call Hooks inside loops, conditions, nested functions, or try/catch/finally blocks. Instead, always use Hooks at the top level of your React function, before any early returns. You can only call Hooks while React is rendering a function component:

It’s not supported to call Hooks (functions starting with use) in any other cases, for example:

If you break these rules, you might see this error.

You can use the eslint-plugin-react-hooks plugin to catch these mistakes.

Custom Hooks may call other Hooks (that’s their whole purpose). This works because custom Hooks are also supposed to only be called while a function component is rendering.

Don’t call Hooks from regular JavaScript functions. Instead, you can:

✅ Call Hooks from React function components. ✅ Call Hooks from custom Hooks.

By following this rule, you ensure that all stateful logic in a component is clearly visible from its source code.

**Examples**:

```javascript
function Counter() {  // ✅ Good: top-level in a function component  const [count, setCount] = useState(0);  // ...}function useWindowWidth() {  // ✅ Good: top-level in a custom Hook  const [width, setWidth] = useState(window.innerWidth);  // ...}
```

```javascript
function Bad({ cond }) {  if (cond) {    // 🔴 Bad: inside a condition (to fix, move it outside!)    const theme = useContext(ThemeContext);  }  // ...}function Bad() {  for (let i = 0; i < 10; i++) {    // 🔴 Bad: inside a loop (to fix, move it outside!)    const theme = useContext(ThemeContext);  }  // ...}function Bad({ cond }) {  if (cond) {    return;  }  // 🔴 Bad: after a conditional return (to fix, move it before the return!)  const theme = useContext(ThemeContext);  // ...}function Bad() {
...
```

```javascript
function FriendList() {  const [onlineStatus, setOnlineStatus] = useOnlineStatus(); // ✅}function setOnlineStatus() { // ❌ Not a component or custom Hook!  const [onlineStatus, setOnlineStatus] = useOnlineStatus();}
```

---

## Rules of React – React

**URL**: https://react.dev/reference/rules

**Contents**:
- Rules of React
  - Note
- Components and Hooks must be pure
- React calls Components and Hooks
- Rules of Hooks

Just as different programming languages have their own ways of expressing concepts, React has its own idioms — or rules — for how to express patterns in a way that is easy to understand and yields high-quality applications.

To learn more about expressing UIs with React, we recommend reading Thinking in React.

This section describes the rules you need to follow to write idiomatic React code. Writing idiomatic React code can help you write well organized, safe, and composable applications. These properties make your app more resilient to changes and makes it easier to work with other developers, libraries, and tools.

These rules are known as the Rules of React. They are rules – and not just guidelines – in the sense that if they are broken, your app likely has bugs. Your code also becomes unidiomatic and harder to understand and reason about.

We strongly recommend using Strict Mode alongside React’s ESLint plugin to help your codebase follow the Rules of React. By following the Rules of React, you’ll be able to find and address these bugs and keep your application maintainable.

Purity in Components and Hooks is a key rule of React that makes your app predictable, easy to debug, and allows React to automatically optimize your code.

React is responsible for rendering components and hooks when necessary to optimize the user experience. It is declarative: you tell React what to render in your component’s logic, and React will figure out how best to display it to your user.

Hooks are defined using JavaScript functions, but they represent a special type of reusable UI logic with restrictions on where they can be called. You need to follow the Rules of Hooks when using them.

---

## Server Components – React

**URL**: https://react.dev/reference/rsc/server-components

**Contents**:
- Server Components
  - Note
    - How do I build support for Server Components?
  - Server Components without a Server
  - Note
  - Server Components with a Server
  - Adding interactivity to Server Components
  - Note

Server Components are a new type of Component that renders ahead of time, before bundling, in an environment separate from your client app or SSR server.

This separate environment is the “server” in React Server Components. Server Components can run once at build time on your CI server, or they can be run for each request using a web server.

While React Server Components in React 19 are stable and will not break between minor versions, the underlying APIs used to implement a React Server Components bundler or framework do not follow semver and may break between minors in React 19.x.

To support React Server Components as a bundler or framework, we recommend pinning to a specific React version, or using the Canary release. We will continue working with bundlers and frameworks to stabilize the APIs used to implement React Server Components in the future.

Server components can run at build time to read from the filesystem or fetch static content, so a web server is not required. For example, you may want to read static data from a content management system.

Without Server Components, it’s common to fetch static data on the client with an Effect:

This pattern means users need to download and parse an additional 75K (gzipped) of libraries, and wait for a second request to fetch the data after the page loads, just to render static content that will not change for the lifetime of the page.

With Server Components, you can render these components once at build time:

The rendered output can then be server-side rendered (SSR) to HTML and uploaded to a CDN. When the app loads, the client will not see the original Page component, or the expensive libraries for rendering the markdown. The client will only see the rendered output:

This means the content is visible during first page load, and the bundle does not include the expensive libraries needed to render the static content.

You may notice that the Server Component above is an async function:

Async Components are a n

*[Content truncated - see full docs]*

**Examples**:

```python
// bundle.jsimport marked from 'marked'; // 35.9K (11.2K gzipped)import sanitizeHtml from 'sanitize-html'; // 206K (63.3K gzipped)function Page({page}) {  const [content, setContent] = useState('');  // NOTE: loads *after* first page render.  useEffect(() => {    fetch(`/api/content/${page}`).then((data) => {      setContent(data.content);    });  }, [page]);  return <div>{sanitizeHtml(marked(content))}</div>;}
```

```javascript
// api.jsapp.get(`/api/content/:page`, async (req, res) => {  const page = req.params.page;  const content = await file.readFile(`${page}.md`);  res.send({content});});
```

```python
import marked from 'marked'; // Not included in bundleimport sanitizeHtml from 'sanitize-html'; // Not included in bundleasync function Page({page}) {  // NOTE: loads *during* render, when the app is built.  const content = await file.readFile(`${page}.md`);  return <div>{sanitizeHtml(marked(content))}</div>;}
```

---

## Server Functions – React

**URL**: https://react.dev/reference/rsc/server-functions

**Contents**:
- Server Functions
  - React Server Components
  - Note
    - How do I build support for Server Functions?
- Usage
  - Creating a Server Function from a Server Component
  - Importing Server Functions from Client Components
  - Server Functions with Actions

Server Functions are for use in React Server Components.

Note: Until September 2024, we referred to all Server Functions as “Server Actions”. If a Server Function is passed to an action prop or called from inside an action then it is a Server Action, but not all Server Functions are Server Actions. The naming in this documentation has been updated to reflect that Server Functions can be used for multiple purposes.

Server Functions allow Client Components to call async functions executed on the server.

While Server Functions in React 19 are stable and will not break between minor versions, the underlying APIs used to implement Server Functions in a React Server Components bundler or framework do not follow semver and may break between minors in React 19.x.

To support Server Functions as a bundler or framework, we recommend pinning to a specific React version, or using the Canary release. We will continue working with bundlers and frameworks to stabilize the APIs used to implement Server Functions in the future.

When a Server Function is defined with the "use server" directive, your framework will automatically create a reference to the Server Function, and pass that reference to the Client Component. When that function is called on the client, React will send a request to the server to execute the function, and return the result.

Server Functions can be created in Server Components and passed as props to Client Components, or they can be imported and used in Client Components.

Server Components can define Server Functions with the "use server" directive:

When React renders the EmptyNote Server Component, it will create a reference to the createNoteAction function, and pass that reference to the Button Client Component. When the button is clicked, React will send a request to the server to execute the createNoteAction function with the reference provided:

For more, see the docs for "use server".

Client Components can import Server Functions from files that u

*[Content truncated - see full docs]*

**Examples**:

```python
// Server Componentimport Button from './Button';function EmptyNote () {  async function createNoteAction() {    // Server Function    'use server';        await db.notes.create();  }  return <Button onClick={createNoteAction}/>;}
```

```javascript
"use client";export default function Button({onClick}) {   console.log(onClick);   // {$$typeof: Symbol.for("react.server.reference"), $$id: 'createNoteAction'}  return <button onClick={() => onClick()}>Create Empty Note</button>}
```

```javascript
"use server";export async function createNote() {  await db.notes.create();}
```

---

## Server React DOM APIs – React

**URL**: https://react.dev/reference/react-dom/server

**Contents**:
- Server React DOM APIs
- Server APIs for Web Streams
  - Note
- Server APIs for Node.js Streams
- Legacy Server APIs for non-streaming environments

The react-dom/server APIs let you server-side render React components to HTML. These APIs are only used on the server at the top level of your app to generate the initial HTML. A framework may call them for you. Most of your components don’t need to import or use them.

These methods are only available in the environments with Web Streams, which includes browsers, Deno, and some modern edge runtimes:

Node.js also includes these methods for compatibility, but they are not recommended due to worse performance. Use the dedicated Node.js APIs instead.

These methods are only available in the environments with Node.js Streams:

These methods can be used in the environments that don’t support streams:

They have limited functionality compared to the streaming APIs.

---

## <StrictMode> – React

**URL**: https://react.dev/reference/react/StrictMode

**Contents**:
- <StrictMode>
- Reference
  - <StrictMode>
    - Props
    - Caveats
- Usage
  - Enabling Strict Mode for entire app
  - Note

<StrictMode> lets you find common bugs in your components early during development.

Use StrictMode to enable additional development behaviors and warnings for the component tree inside:

See more examples below.

Strict Mode enables the following development-only behaviors:

StrictMode accepts no props.

Strict Mode enables extra development-only checks for the entire component tree inside the <StrictMode> component. These checks help you find common bugs in your components early in the development process.

To enable Strict Mode for your entire app, wrap your root component with <StrictMode> when you render it:

We recommend wrapping your entire app in Strict Mode, especially for newly created apps. If you use a framework that calls createRoot for you, check its documentation for how to enable Strict Mode.

Although the Strict Mode checks only run in development, they help you find bugs that already exist in your code but can be tricky to reliably reproduce in production. Strict Mode lets you fix bugs before your users report them.

Strict Mode enables the following checks in development:

All of these checks are development-only and do not impact the production build.

You can also enable Strict Mode for any part of your application:

In this example, Strict Mode checks will not run against the Header and Footer components. However, they will run on Sidebar and Content, as well as all of the components inside them, no matter how deep.

When StrictMode is enabled for a part of the app, React will only enable behaviors that are possible in production. For example, if <StrictMode> is not enabled at the root of the app, it will not re-run Effects an extra time on initial mount, since this would cause child effects to double fire without the parent effects, which cannot happen in production.

React assumes that every component you write is a pure function. This means that React components you write must always return the same JSX given the same inputs (props, state, a

*[Content truncated - see full docs]*

**Examples**:

```text
<StrictMode>  <App /></StrictMode>
```

```python
import { StrictMode } from 'react';import { createRoot } from 'react-dom/client';const root = createRoot(document.getElementById('root'));root.render(  <StrictMode>    <App />  </StrictMode>);
```

```python
import { StrictMode } from 'react';import { createRoot } from 'react-dom/client';const root = createRoot(document.getElementById('root'));root.render(  <StrictMode>    <App />  </StrictMode>);
```

---

## <Suspense> – React

**URL**: https://react.dev/reference/react/Suspense

**Contents**:
- <Suspense>
- Reference
  - <Suspense>
    - Props
    - Caveats
- Usage
  - Displaying a fallback while content is loading
  - Note

<Suspense> lets you display a fallback until its children have finished loading.

You can wrap any part of your application with a Suspense boundary:

React will display your loading fallback until all the code and data needed by the children has been loaded.

In the example below, the Albums component suspends while fetching the list of albums. Until it’s ready to render, React switches the closest Suspense boundary above to show the fallback—your Loading component. Then, when the data loads, React hides the Loading fallback and renders the Albums component with data.

Only Suspense-enabled data sources will activate the Suspense component. They include:

Suspense does not detect when data is fetched inside an Effect or event handler.

The exact way you would load data in the Albums component above depends on your framework. If you use a Suspense-enabled framework, you’ll find the details in its data fetching documentation.

Suspense-enabled data fetching without the use of an opinionated framework is not yet supported. The requirements for implementing a Suspense-enabled data source are unstable and undocumented. An official API for integrating data sources with Suspense will be released in a future version of React.

By default, the whole tree inside Suspense is treated as a single unit. For example, even if only one of these components suspends waiting for some data, all of them together will be replaced by the loading indicator:

Then, after all of them are ready to be displayed, they will all appear together at once.

In the example below, both Biography and Albums fetch some data. However, because they are grouped under a single Suspense boundary, these components always “pop in” together at the same time.

Components that load data don’t have to be direct children of the Suspense boundary. For example, you can move Biography and Albums into a new Details component. This doesn’t change the behavior. Biography and Albums share the same closest parent Suspense 

*[Content truncated - see full docs]*

**Examples**:

```text
<Suspense fallback={<Loading />}>  <SomeComponent /></Suspense>
```

```text
<Suspense fallback={<Loading />}>  <Albums /></Suspense>
```

```text
<Suspense fallback={<Loading />}>  <Biography />  <Panel>    <Albums />  </Panel></Suspense>
```

---

## <ViewTransition> – React

**URL**: https://react.dev/reference/react/ViewTransition

**Contents**:
- <ViewTransition> - This feature is available in the latest Canary version of React
  - Canary
- Reference
  - <ViewTransition>
      - Deep Dive
    - How does <ViewTransition> work?
    - Props
    - Callback

The <ViewTransition /> API is currently only available in React’s Canary and Experimental channels.

Learn more about React’s release channels here.

<ViewTransition> lets you animate elements that update inside a Transition.

Wrap elements in <ViewTransition> to animate them when they update inside a Transition. React uses the following heuristics to determine if a View Transition activates for an animation:

By default, <ViewTransition> animates with a smooth cross-fade (the browser default view transition). You can customize the animation by providing a View Transition Class to the <ViewTransition> component. You can customize animations for each kind of trigger (see Styling View Transitions).

Under the hood, React applies view-transition-name to inline styles of the nearest DOM node nested inside the <ViewTransition> component. If there are multiple sibling DOM nodes like <ViewTransition><div /><div /></ViewTransition> then React adds a suffix to the name to make each unique but conceptually they’re part of the same one. React doesn’t apply these eagerly but only at the time that boundary should participate in an animation.

React automatically calls startViewTransition itself behind the scenes so you should never do that yourself. In fact, if you have something else on the page running a ViewTransition React will interrupt it. So it’s recommended that you use React itself to coordinate these. If you had other ways of trigger ViewTransitions in the past, we recommend that you migrate to the built-in way.

If there are other React ViewTransitions already running then React will wait for them to finish before starting the next one. However, importantly if there are multiple updates happening while the first one is running, those will all be batched into one. If you start A->B. Then in the meantime you get an update to go to C and then D. When the first A->B animation finishes the next one will animate from B->D.

The getSnapshotBeforeUpdate life-cycle will be cal

*[Content truncated - see full docs]*

**Examples**:

```python
import {ViewTransition} from 'react';<ViewTransition>  <div>...</div></ViewTransition>
```

```text
<ViewTransition enter="slide-in">
```

```text
::view-transition-group(.slide-in) {  }::view-transition-old(.slide-in) {}::view-transition-new(.slide-in) {}
```

---

## act – React

**URL**: https://react.dev/reference/react/act

**Contents**:
- act
  - Note
- Reference
  - await act(async actFn)
  - Note
    - Parameters
    - Returns
- Usage

act is a test helper to apply pending React updates before making assertions.

To prepare a component for assertions, wrap the code rendering it and performing updates inside an await act() call. This makes your test run closer to how React works in the browser.

You might find using act() directly a bit too verbose. To avoid some of the boilerplate, you could use a library like React Testing Library, whose helpers are wrapped with act().

When writing UI tests, tasks like rendering, user events, or data fetching can be considered as “units” of interaction with a user interface. React provides a helper called act() that makes sure all updates related to these “units” have been processed and applied to the DOM before you make any assertions.

The name act comes from the Arrange-Act-Assert pattern.

We recommend using act with await and an async function. Although the sync version works in many cases, it doesn’t work in all cases and due to the way React schedules updates internally, it’s difficult to predict when you can use the sync version.

We will deprecate and remove the sync version in the future.

act does not return anything.

When testing a component, you can use act to make assertions about its output.

For example, let’s say we have this Counter component, the usage examples below show how to test it:

To test the render output of a component, wrap the render inside act():

Here, we create a container, append it to the document, and render the Counter component inside act(). This ensures that the component is rendered and its effects are applied before making assertions.

Using act ensures that all updates have been applied before we make assertions.

To test events, wrap the event dispatch inside act():

Here, we render the component with act, and then dispatch the event inside another act(). This ensures that all updates from the event are applied before making assertions.

Don’t forget that dispatching DOM events only works when the DOM container is add

*[Content truncated - see full docs]*

**Examples**:

```text
await act(async actFn)
```

```javascript
it ('renders with button disabled', async () => {  await act(async () => {    root.render(<TestComponent />)  });  expect(container.querySelector('button')).toBeDisabled();});
```

```javascript
function Counter() {  const [count, setCount] = useState(0);  const handleClick = () => {    setCount(prev => prev + 1);  }  useEffect(() => {    document.title = `You clicked ${count} times`;  }, [count]);  return (    <div>      <p>You clicked {count} times</p>      <button onClick={handleClick}>        Click me      </button>    </div>  )}
```

---

## compilationMode – React

**URL**: https://react.dev/reference/react-compiler/compilationMode

**Contents**:
- compilationMode
- Reference
  - compilationMode
    - Type
    - Default value
    - Options
    - Caveats
- Usage

The compilationMode option controls how the React Compiler selects which functions to compile.

Controls the strategy for determining which functions the React Compiler will optimize.

'infer' (default): The compiler uses intelligent heuristics to identify React components and hooks:

'annotation': Only compile functions explicitly marked with the "use memo" directive. Ideal for incremental adoption.

'syntax': Only compile components and hooks that use Flow’s component and hook syntax.

'all': Compile all top-level functions. Not recommended as it may compile non-React functions.

The default 'infer' mode works well for most codebases that follow React conventions:

With this mode, these functions will be compiled:

For gradual migration, use 'annotation' mode to only compile marked functions:

Then explicitly mark functions to compile:

If your codebase uses Flow instead of TypeScript:

Then use Flow’s component syntax:

Regardless of compilation mode, use "use no memo" to skip compilation:

In 'infer' mode, ensure your component follows React conventions:

**Examples**:

```text
{  compilationMode: 'infer' // or 'annotation', 'syntax', 'all'}
```

```text
'infer' | 'syntax' | 'annotation' | 'all'
```

```text
{  compilationMode: 'infer'}
```

---

## component-hook-factories – React

**URL**: https://react.dev/reference/eslint-plugin-react-hooks/lints/component-hook-factories

**Contents**:
- component-hook-factories
- Rule Details
  - Invalid
  - Valid
- Troubleshooting
  - I need dynamic component behavior

Validates against higher order functions defining nested components or hooks. Components and hooks should be defined at the module level.

Defining components or hooks inside other functions creates new instances on every call. React treats each as a completely different component, destroying and recreating the entire component tree, losing all state, and causing performance problems.

Examples of incorrect code for this rule:

Examples of correct code for this rule:

You might think you need a factory to create customized components:

Pass JSX as children instead:

**Examples**:

```javascript
// ❌ Factory function creating componentsfunction createComponent(defaultValue) {  return function Component() {    // ...  };}// ❌ Component defined inside componentfunction Parent() {  function Child() {    // ...  }  return <Child />;}// ❌ Hook factory functionfunction createCustomHook(endpoint) {  return function useData() {    // ...  };}
```

```javascript
// ✅ Component defined at module levelfunction Component({ defaultValue }) {  // ...}// ✅ Custom hook at module levelfunction useData(endpoint) {  // ...}
```

```javascript
// ❌ Wrong: Factory patternfunction makeButton(color) {  return function Button({children}) {    return (      <button style={{backgroundColor: color}}>        {children}      </button>    );  };}const RedButton = makeButton('red');const BlueButton = makeButton('blue');
```

---

## config – React

**URL**: https://react.dev/reference/eslint-plugin-react-hooks/lints/config

**Contents**:
- config
- Rule Details
  - Invalid
  - Valid
- Troubleshooting
  - Configuration not working as expected

Validates the compiler configuration options.

React Compiler accepts various configuration options to control its behavior. This rule validates that your configuration uses correct option names and value types, preventing silent failures from typos or incorrect settings.

Examples of incorrect code for this rule:

Examples of correct code for this rule:

Your compiler configuration might have typos or incorrect values:

Check the configuration documentation for valid options:

**Examples**:

```text
// ❌ Unknown option namemodule.exports = {  plugins: [    ['babel-plugin-react-compiler', {      compileMode: 'all' // Typo: should be compilationMode    }]  ]};// ❌ Invalid option valuemodule.exports = {  plugins: [    ['babel-plugin-react-compiler', {      compilationMode: 'everything' // Invalid: use 'all' or 'infer'    }]  ]};
```

```text
// ✅ Valid compiler configurationmodule.exports = {  plugins: [    ['babel-plugin-react-compiler', {      compilationMode: 'infer',      panicThreshold: 'critical_errors'    }]  ]};
```

```text
// ❌ Wrong: Common configuration mistakesmodule.exports = {  plugins: [    ['babel-plugin-react-compiler', {      // Typo in option name      compilationMod: 'all',      // Wrong value type      panicThreshold: true,      // Unknown option      optimizationLevel: 'max'    }]  ]};
```

---

## createContext – React

**URL**: https://react.dev/reference/react/createContext

**Contents**:
- createContext
- Reference
  - createContext(defaultValue)
    - Parameters
    - Returns
  - SomeContext Provider
  - Note
    - Props

createContext lets you create a context that components can provide or read.

Call createContext outside of any components to create a context.

See more examples below.

createContext returns a context object.

The context object itself does not hold any information. It represents which context other components read or provide. Typically, you will use SomeContext in components above to specify the context value, and call useContext(SomeContext) in components below to read it. The context object has a few properties:

Wrap your components into a context provider to specify the value of this context for all components inside:

Starting in React 19, you can render <SomeContext> as a provider.

In older versions of React, use <SomeContext.Provider>.

Before useContext existed, there was an older way to read context:

Although this older way still works, newly written code should read context with useContext() instead:

Context lets components pass information deep down without explicitly passing props.

Call createContext outside any components to create one or more contexts.

createContext returns a context object. Components can read context by passing it to useContext():

By default, the values they receive will be the default values you have specified when creating the contexts. However, by itself this isn’t useful because the default values never change.

Context is useful because you can provide other, dynamic values from your components:

Now the Page component and any components inside it, no matter how deep, will “see” the passed context values. If the passed context values change, React will re-render the components reading the context as well.

Read more about reading and providing context and see examples.

Often, components in different files will need access to the same context. This is why it’s common to declare contexts in a separate file. Then you can use the export statement to make context available for other files:

Components declared in other file

*[Content truncated - see full docs]*

**Examples**:

```javascript
const SomeContext = createContext(defaultValue)
```

```python
import { createContext } from 'react';const ThemeContext = createContext('light');
```

```javascript
function App() {  const [theme, setTheme] = useState('light');  // ...  return (    <ThemeContext value={theme}>      <Page />    </ThemeContext>  );}
```

---

## createPortal – React

**URL**: https://react.dev/reference/react-dom/createPortal

**Contents**:
- createPortal
- Reference
  - createPortal(children, domNode, key?)
    - Parameters
    - Returns
    - Caveats
- Usage
  - Rendering to a different part of the DOM

createPortal lets you render some children into a different part of the DOM.

To create a portal, call createPortal, passing some JSX, and the DOM node where it should be rendered:

See more examples below.

A portal only changes the physical placement of the DOM node. In every other way, the JSX you render into a portal acts as a child node of the React component that renders it. For example, the child can access the context provided by the parent tree, and events bubble up from children to parents according to the React tree.

children: Anything that can be rendered with React, such as a piece of JSX (e.g. <div /> or <SomeComponent />), a Fragment (<>...</>), a string or a number, or an array of these.

domNode: Some DOM node, such as those returned by document.getElementById(). The node must already exist. Passing a different DOM node during an update will cause the portal content to be recreated.

optional key: A unique string or number to be used as the portal’s key.

createPortal returns a React node that can be included into JSX or returned from a React component. If React encounters it in the render output, it will place the provided children inside the provided domNode.

Portals let your components render some of their children into a different place in the DOM. This lets a part of your component “escape” from whatever containers it may be in. For example, a component can display a modal dialog or a tooltip that appears above and outside of the rest of the page.

To create a portal, render the result of createPortal with some JSX and the DOM node where it should go:

React will put the DOM nodes for the JSX you passed inside of the DOM node you provided.

Without a portal, the second <p> would be placed inside the parent <div>, but the portal “teleported” it into the document.body:

Notice how the second paragraph visually appears outside the parent <div> with the border. If you inspect the DOM structure with developer tools, you’ll see that the second <p> 

*[Content truncated - see full docs]*

**Examples**:

```text
<div>  <SomeComponent />  {createPortal(children, domNode, key?)}</div>
```

```python
import { createPortal } from 'react-dom';// ...<div>  <p>This child is placed in the parent div.</p>  {createPortal(    <p>This child is placed in the document body.</p>,    document.body  )}</div>
```

```python
import { createPortal } from 'react-dom';function MyComponent() {  return (    <div style={{ border: '2px solid black' }}>      <p>This child is placed in the parent div.</p>      {createPortal(        <p>This child is placed in the document body.</p>,        document.body      )}    </div>  );}
```

---

## createRoot – React

**URL**: https://react.dev/reference/react-dom/client/createRoot

**Contents**:
- createRoot
- Reference
  - createRoot(domNode, options?)
    - Parameters
    - Returns
    - Caveats
  - root.render(reactNode)
    - Parameters

createRoot lets you create a root to display React components inside a browser DOM node.

Call createRoot to create a React root for displaying content inside a browser DOM element.

React will create a root for the domNode, and take over managing the DOM inside it. After you’ve created a root, you need to call root.render to display a React component inside of it:

An app fully built with React will usually only have one createRoot call for its root component. A page that uses “sprinkles” of React for parts of the page may have as many separate roots as needed.

See more examples below.

domNode: A DOM element. React will create a root for this DOM element and allow you to call functions on the root, such as render to display rendered React content.

optional options: An object with options for this React root.

createRoot returns an object with two methods: render and unmount.

Call root.render to display a piece of JSX (“React node”) into the React root’s browser DOM node.

React will display <App /> in the root, and take over managing the DOM inside it.

See more examples below.

root.render returns undefined.

The first time you call root.render, React will clear all the existing HTML content inside the React root before rendering the React component into it.

If your root’s DOM node contains HTML generated by React on the server or during the build, use hydrateRoot() instead, which attaches the event handlers to the existing HTML.

If you call render on the same root more than once, React will update the DOM as necessary to reflect the latest JSX you passed. React will decide which parts of the DOM can be reused and which need to be recreated by “matching it up” with the previously rendered tree. Calling render on the same root again is similar to calling the set function on the root component: React avoids unnecessary DOM updates.

Although rendering is synchronous once it starts, root.render(...) is not. This means code after root.render() may run before any

*[Content truncated - see full docs]*

**Examples**:

```javascript
const root = createRoot(domNode, options?)
```

```python
import { createRoot } from 'react-dom/client';const domNode = document.getElementById('root');const root = createRoot(domNode);
```

```text
root.render(<App />);
```

---

## error-boundaries – React

**URL**: https://react.dev/reference/eslint-plugin-react-hooks/lints/error-boundaries

**Contents**:
- error-boundaries
- Rule Details
  - Invalid
  - Valid
- Troubleshooting
  - Why is the linter telling me not to wrap use in try/catch?

Validates usage of Error Boundaries instead of try/catch for errors in child components.

Try/catch blocks can’t catch errors that happen during React’s rendering process. Errors thrown in rendering methods or hooks bubble up through the component tree. Only Error Boundaries can catch these errors.

Examples of incorrect code for this rule:

Examples of correct code for this rule:

The use hook doesn’t throw errors in the traditional sense, it suspends component execution. When use encounters a pending promise, it suspends the component and lets React show a fallback. Only Suspense and Error Boundaries can handle these cases. The linter warns against try/catch around use to prevent confusion as the catch block would never run.

**Examples**:

```javascript
// ❌ Try/catch won't catch render errorsfunction Parent() {  try {    return <ChildComponent />; // If this throws, catch won't help  } catch (error) {    return <div>Error occurred</div>;  }}
```

```javascript
// ✅ Using error boundaryfunction Parent() {  return (    <ErrorBoundary>      <ChildComponent />    </ErrorBoundary>  );}
```

```javascript
// ❌ Try/catch around `use` hookfunction Component({promise}) {  try {    const data = use(promise); // Won't catch - `use` suspends, not throws    return <div>{data}</div>;  } catch (error) {    return <div>Failed to load</div>; // Unreachable  }}// ✅ Error boundary catches `use` errorsfunction App() {  return (    <ErrorBoundary fallback={<div>Failed to load</div>}>      <Suspense fallback={<div>Loading...</div>}>        <DataComponent promise={fetchData()} />      </Suspense>    </ErrorBounda
...
```

---

## eslint-plugin-react-hooks – React

**URL**: https://react.dev/reference/eslint-plugin-react-hooks

**Contents**:
- eslint-plugin-react-hooks - This feature is available in the latest RC version
  - Note
- Recommended Rules

eslint-plugin-react-hooks provides ESLint rules to enforce the Rules of React.

This plugin helps you catch violations of React’s rules at build time, ensuring your components and hooks follow React’s rules for correctness and performance. The lints cover both fundamental React patterns (exhaustive-deps and rules-of-hooks) and issues flagged by React Compiler. React Compiler diagnostics are automatically surfaced by this ESLint plugin, and can be used even if your app hasn’t adopted the compiler yet.

When the compiler reports a diagnostic, it means that the compiler was able to statically detect a pattern that is not supported or breaks the Rules of React. When it detects this, it automatically skips over those components and hooks, while keeping the rest of your app compiled. This ensures optimal coverage of safe optimizations that won’t break your app.

What this means for linting, is that you don’t need to fix all violations immediately. Address them at your own pace to gradually increase the number of optimized components.

These rules are included in the recommended preset in eslint-plugin-react-hooks:

---

## exhaustive-deps – React

**URL**: https://react.dev/reference/eslint-plugin-react-hooks/lints/exhaustive-deps

**Contents**:
- exhaustive-deps
- Rule Details
- Common Violations
  - Invalid
  - Valid
- Troubleshooting
  - Adding a function dependency causes infinite loops
  - Running an effect only once

Validates that dependency arrays for React hooks contain all necessary dependencies.

React hooks like useEffect, useMemo, and useCallback accept dependency arrays. When a value referenced inside these hooks isn’t included in the dependency array, React won’t re-run the effect or recalculate the value when that dependency changes. This causes stale closures where the hook uses outdated values.

This error often happens when you try to “trick” React about dependencies to control when an effect runs. Effects should synchronize your component with external systems. The dependency array tells React which values the effect uses, so React knows when to re-synchronize.

If you find yourself fighting with the linter, you likely need to restructure your code. See Removing Effect Dependencies to learn how.

Examples of incorrect code for this rule:

Examples of correct code for this rule:

You have an effect, but you’re creating a new function on every render:

In most cases, you don’t need the effect. Call the function where the action happens instead:

If you genuinely need the effect (for example, to subscribe to something external), make the dependency stable:

You want to run an effect once on mount, but the linter complains about missing dependencies:

Either include the dependency (recommended) or use a ref if you truly need to run once:

You can configure custom effect hooks using shared ESLint settings (available in eslint-plugin-react-hooks 6.1.1 and later):

For backward compatibility, this rule also accepts a rule-level option:

**Examples**:

```javascript
// ❌ Missing dependencyuseEffect(() => {  console.log(count);}, []); // Missing 'count'// ❌ Missing propuseEffect(() => {  fetchUser(userId);}, []); // Missing 'userId'// ❌ Incomplete dependenciesuseMemo(() => {  return items.sort(sortOrder);}, [items]); // Missing 'sortOrder'
```

```javascript
// ✅ All dependencies includeduseEffect(() => {  console.log(count);}, [count]);// ✅ All dependencies includeduseEffect(() => {  fetchUser(userId);}, [userId]);
```

```javascript
// ❌ Causes infinite loopconst logItems = () => {  console.log(items);};useEffect(() => {  logItems();}, [logItems]); // Infinite loop!
```

---

## flushSync – React

**URL**: https://react.dev/reference/react-dom/flushSync

**Contents**:
- flushSync
  - Pitfall
- Reference
  - flushSync(callback)
    - Parameters
    - Returns
    - Caveats
- Usage

Using flushSync is uncommon and can hurt the performance of your app.

flushSync lets you force React to flush any updates inside the provided callback synchronously. This ensures that the DOM is updated immediately.

Call flushSync to force React to flush any pending work and update the DOM synchronously.

Most of the time, flushSync can be avoided. Use flushSync as last resort.

See more examples below.

flushSync returns undefined.

When integrating with third-party code such as browser APIs or UI libraries, it may be necessary to force React to flush updates. Use flushSync to force React to flush any state updates inside the callback synchronously:

This ensures that, by the time the next line of code runs, React has already updated the DOM.

Using flushSync is uncommon, and using it often can significantly hurt the performance of your app. If your app only uses React APIs, and does not integrate with third-party libraries, flushSync should be unnecessary.

However, it can be helpful for integrating with third-party code like browser APIs.

Some browser APIs expect results inside of callbacks to be written to the DOM synchronously, by the end of the callback, so the browser can do something with the rendered DOM. In most cases, React handles this for you automatically. But in some cases it may be necessary to force a synchronous update.

For example, the browser onbeforeprint API allows you to change the page immediately before the print dialog opens. This is useful for applying custom print styles that allow the document to display better for printing. In the example below, you use flushSync inside of the onbeforeprint callback to immediately “flush” the React state to the DOM. Then, by the time the print dialog opens, isPrinting displays “yes”:

Without flushSync, the print dialog will display isPrinting as “no”. This is because React batches the updates asynchronously and the print dialog is displayed before the state is updated.

flushSync can significantly 

*[Content truncated - see full docs]*

**Examples**:

```text
flushSync(callback)
```

```python
import { flushSync } from 'react-dom';flushSync(() => {  setSomething(123);});
```

```javascript
flushSync(() => {  setSomething(123);});// By this line, the DOM is updated.
```

---

## gating – React

**URL**: https://react.dev/reference/eslint-plugin-react-hooks/lints/gating

**Contents**:
- gating
- Rule Details
  - Invalid
  - Valid

Validates configuration of gating mode.

Gating mode lets you gradually adopt React Compiler by marking specific components for optimization. This rule ensures your gating configuration is valid so the compiler knows which components to process.

Examples of incorrect code for this rule:

Examples of correct code for this rule:

**Examples**:

```text
// ❌ Missing required fieldsmodule.exports = {  plugins: [    ['babel-plugin-react-compiler', {      gating: {        importSpecifierName: '__experimental_useCompiler'        // Missing 'source' field      }    }]  ]};// ❌ Invalid gating typemodule.exports = {  plugins: [    ['babel-plugin-react-compiler', {      gating: '__experimental_useCompiler' // Should be object    }]  ]};
```

```javascript
// ✅ Complete gating configurationmodule.exports = {  plugins: [    ['babel-plugin-react-compiler', {      gating: {        importSpecifierName: 'isCompilerEnabled', // exported function name        source: 'featureFlags' // module name      }    }]  ]};// featureFlags.jsexport function isCompilerEnabled() {  // ...}// ✅ No gating (compile everything)module.exports = {  plugins: [    ['babel-plugin-react-compiler', {      // No gating field - compiles all components    }]  ]};
```

---

## gating – React

**URL**: https://react.dev/reference/react-compiler/gating

**Contents**:
- gating
- Reference
  - gating
    - Type
    - Default value
    - Properties
    - Caveats
- Usage

The gating option enables conditional compilation, allowing you to control when optimized code is used at runtime.

Configures runtime feature flag gating for compiled functions.

Note that the gating function is evaluated once at module time, so once the JS bundle has been parsed and evaluated the choice of component stays static for the rest of the browser session.

Verify your flag module exports the correct function:

Ensure the source path is correct:

**Examples**:

```text
{  gating: {    source: 'my-feature-flags',    importSpecifierName: 'shouldUseCompiler'  }}
```

```text
{  source: string;  importSpecifierName: string;} | null
```

```javascript
// src/utils/feature-flags.jsexport function shouldUseCompiler() {  // your logic here  return getFeatureFlag('react-compiler-enabled');}
```

---

## hydrateRoot – React

**URL**: https://react.dev/reference/react-dom/client/hydrateRoot

**Contents**:
- hydrateRoot
- Reference
  - hydrateRoot(domNode, reactNode, options?)
    - Parameters
    - Returns
    - Caveats
  - root.render(reactNode)
    - Parameters

hydrateRoot lets you display React components inside a browser DOM node whose HTML content was previously generated by react-dom/server.

Call hydrateRoot to “attach” React to existing HTML that was already rendered by React in a server environment.

React will attach to the HTML that exists inside the domNode, and take over managing the DOM inside it. An app fully built with React will usually only have one hydrateRoot call with its root component.

See more examples below.

domNode: A DOM element that was rendered as the root element on the server.

reactNode: The “React node” used to render the existing HTML. This will usually be a piece of JSX like <App /> which was rendered with a ReactDOM Server method such as renderToPipeableStream(<App />).

optional options: An object with options for this React root.

hydrateRoot returns an object with two methods: render and unmount.

Call root.render to update a React component inside a hydrated React root for a browser DOM element.

React will update <App /> in the hydrated root.

See more examples below.

root.render returns undefined.

Call root.unmount to destroy a rendered tree inside a React root.

An app fully built with React will usually not have any calls to root.unmount.

This is mostly useful if your React root’s DOM node (or any of its ancestors) may get removed from the DOM by some other code. For example, imagine a jQuery tab panel that removes inactive tabs from the DOM. If a tab gets removed, everything inside it (including the React roots inside) would get removed from the DOM as well. You need to tell React to “stop” managing the removed root’s content by calling root.unmount. Otherwise, the components inside the removed root won’t clean up and free up resources like subscriptions.

Calling root.unmount will unmount all the components in the root and “detach” React from the root DOM node, including removing any event handlers or state in the tree.

root.unmount does not accept any parameters.

root.unm

*[Content truncated - see full docs]*

**Examples**:

```javascript
const root = hydrateRoot(domNode, reactNode, options?)
```

```python
import { hydrateRoot } from 'react-dom/client';const domNode = document.getElementById('root');const root = hydrateRoot(domNode, reactNode);
```

```text
root.render(<App />);
```

---

## <input> – React

**URL**: https://react.dev/reference/react-dom/components/input

**Contents**:
- <input>
- Reference
  - <input>
    - Props
    - Caveats
- Usage
  - Displaying inputs of different types
  - Providing a label for an input

The built-in browser <input> component lets you render different kinds of form inputs.

To display an input, render the built-in browser <input> component.

See more examples below.

<input> supports all common element props.

You can make an input controlled by passing one of these props:

When you pass either of them, you must also pass an onChange handler that updates the passed value.

These <input> props are only relevant for uncontrolled inputs:

These <input> props are relevant both for uncontrolled and controlled inputs:

To display an input, render an <input> component. By default, it will be a text input. You can pass type="checkbox" for a checkbox, type="radio" for a radio button, or one of the other input types.

Typically, you will place every <input> inside a <label> tag. This tells the browser that this label is associated with that input. When the user clicks the label, the browser will automatically focus the input. It’s also essential for accessibility: a screen reader will announce the label caption when the user focuses the associated input.

If you can’t nest <input> into a <label>, associate them by passing the same ID to <input id> and <label htmlFor>. To avoid conflicts between multiple instances of one component, generate such an ID with useId.

You can optionally specify the initial value for any input. Pass it as the defaultValue string for text inputs. Checkboxes and radio buttons should specify the initial value with the defaultChecked boolean instead.

Add a <form> around your inputs with a <button type="submit"> inside. It will call your <form onSubmit> event handler. By default, the browser will send the form data to the current URL and refresh the page. You can override that behavior by calling e.preventDefault(). Read the form data with new FormData(e.target).

Give a name to every <input>, for example <input name="firstName" defaultValue="Taylor" />. The name you specified will be used as a key in the form data, for example { first

*[Content truncated - see full docs]*

**Examples**:

```text
<input name="myInput" />
```

```javascript
function Form() {  const [firstName, setFirstName] = useState(''); // Declare a state variable...  // ...  return (    <input      value={firstName} // ...force the input's value to match the state variable...      onChange={e => setFirstName(e.target.value)} // ... and update the state variable on any edits!    />  );}
```

```javascript
function Form() {  const [firstName, setFirstName] = useState('');  return (    <>      <label>        First name:        <input value={firstName} onChange={e => setFirstName(e.target.value)} />      </label>      {firstName !== '' && <p>Your name is {firstName}.</p>}      ...
```

---

## lazy – React

**URL**: https://react.dev/reference/react/lazy

**Contents**:
- lazy
- Reference
  - lazy(load)
    - Parameters
    - Returns
  - load function
    - Parameters
    - Returns

lazy lets you defer loading component’s code until it is rendered for the first time.

Call lazy outside your components to declare a lazy-loaded React component:

See more examples below.

lazy returns a React component you can render in your tree. While the code for the lazy component is still loading, attempting to render it will suspend. Use <Suspense> to display a loading indicator while it’s loading.

load receives no parameters.

You need to return a Promise or some other thenable (a Promise-like object with a then method). It needs to eventually resolve to an object whose .default property is a valid React component type, such as a function, memo, or a forwardRef component.

Usually, you import components with the static import declaration:

To defer loading this component’s code until it’s rendered for the first time, replace this import with:

This code relies on dynamic import(), which might require support from your bundler or framework. Using this pattern requires that the lazy component you’re importing was exported as the default export.

Now that your component’s code loads on demand, you also need to specify what should be displayed while it is loading. You can do this by wrapping the lazy component or any of its parents into a <Suspense> boundary:

In this example, the code for MarkdownPreview won’t be loaded until you attempt to render it. If MarkdownPreview hasn’t loaded yet, Loading will be shown in its place. Try ticking the checkbox:

This demo loads with an artificial delay. The next time you untick and tick the checkbox, Preview will be cached, so there will be no loading state. To see the loading state again, click “Reset” on the sandbox.

Learn more about managing loading states with Suspense.

Do not declare lazy components inside other components:

Instead, always declare them at the top level of your module:

**Examples**:

```javascript
const SomeComponent = lazy(load)
```

```python
import { lazy } from 'react';const MarkdownPreview = lazy(() => import('./MarkdownPreview.js'));
```

```python
import MarkdownPreview from './MarkdownPreview.js';
```

---

## <link> – React

**URL**: https://react.dev/reference/react-dom/components/link

**Contents**:
- <link>
- Reference
  - <link>
    - Props
    - Special rendering behavior
    - Special behavior for stylesheets
- Usage
  - Linking to related resources

The built-in browser <link> component lets you use external resources such as stylesheets or annotate the document with link metadata.

To link to external resources such as stylesheets, fonts, and icons, or to annotate the document with link metadata, render the built-in browser <link> component. You can render <link> from any component and React will in most cases place the corresponding DOM element in the document head.

See more examples below.

<link> supports all common element props.

These props apply when rel="stylesheet":

These props apply when rel="stylesheet" but disable React’s special treatment of stylesheets:

These props apply when rel="preload" or rel="modulepreload":

These props apply when rel="icon" or rel="apple-touch-icon":

These props apply in all cases:

Props that are not recommended for use with React:

React will always place the DOM element corresponding to the <link> component within the document’s <head>, regardless of where in the React tree it is rendered. The <head> is the only valid place for <link> to exist within the DOM, yet it’s convenient and keeps things composable if a component representing a specific page can render <link> components itself.

There are a few exceptions to this:

In addition, if the <link> is to a stylesheet (namely, it has rel="stylesheet" in its props), React treats it specially in the following ways:

There are two exception to this special behavior:

This special treatment comes with two caveats:

You can annotate the document with links to related resources such as an icon, canonical URL, or pingback. React will place this metadata within the document <head> regardless of where in the React tree it is rendered.

If a component depends on a certain stylesheet in order to be displayed correctly, you can render a link to that stylesheet within the component. Your component will suspend while the stylesheet is loading. You must supply the precedence prop, which tells React where to place this stylesheet r

*[Content truncated - see full docs]*

**Examples**:

```text
<link rel="icon" href="favicon.ico" />
```

```text
<link rel="icon" href="favicon.ico" />
```

```text
<section itemScope>  <h3>Annotating specific items</h3>  <link itemProp="author" href="http://example.com/" />  <p>...</p></section>
```

---

## logger – React

**URL**: https://react.dev/reference/react-compiler/logger

**Contents**:
- logger
- Reference
  - logger
    - Type
    - Default value
    - Methods
    - Event types
    - Caveats

The logger option provides custom logging for React Compiler events during compilation.

Configures custom logging to track compiler behavior and debug issues.

Track compilation success and failures:

Get specific information about compilation failures:

**Examples**:

```text
{  logger: {    logEvent(filename, event) {      console.log(`[Compiler] ${event.kind}: ${filename}`);    }  }}
```

```javascript
{  logEvent: (filename: string | null, event: LoggerEvent) => void;} | null
```

```text
{  logger: {    logEvent(filename, event) {      switch (event.kind) {        case 'CompileSuccess': {          console.log(`✅ Compiled: ${filename}`);          break;        }        case 'CompileError': {          console.log(`❌ Skipped: ${filename}`);          break;        }        default: {}      }    }  }}
```

---

## memo – React

**URL**: https://react.dev/reference/react/memo

**Contents**:
- memo
  - Note
- Reference
  - memo(Component, arePropsEqual?)
    - Parameters
    - Returns
- Usage
  - Skipping re-rendering when props are unchanged

memo lets you skip re-rendering a component when its props are unchanged.

React Compiler automatically applies the equivalent of memo to all components, reducing the need for manual memoization. You can use the compiler to handle component memoization automatically.

Wrap a component in memo to get a memoized version of that component. This memoized version of your component will usually not be re-rendered when its parent component is re-rendered as long as its props have not changed. But React may still re-render it: memoization is a performance optimization, not a guarantee.

See more examples below.

Component: The component that you want to memoize. The memo does not modify this component, but returns a new, memoized component instead. Any valid React component, including functions and forwardRef components, is accepted.

optional arePropsEqual: A function that accepts two arguments: the component’s previous props, and its new props. It should return true if the old and new props are equal: that is, if the component will render the same output and behave in the same way with the new props as with the old. Otherwise it should return false. Usually, you will not specify this function. By default, React will compare each prop with Object.is.

memo returns a new React component. It behaves the same as the component provided to memo except that React will not always re-render it when its parent is being re-rendered unless its props have changed.

React normally re-renders a component whenever its parent re-renders. With memo, you can create a component that React will not re-render when its parent re-renders so long as its new props are the same as the old props. Such a component is said to be memoized.

To memoize a component, wrap it in memo and use the value that it returns in place of your original component:

A React component should always have pure rendering logic. This means that it must return the same output if its props, state, and context haven’t changed

*[Content truncated - see full docs]*

**Examples**:

```javascript
const MemoizedComponent = memo(SomeComponent, arePropsEqual?)
```

```python
import { memo } from 'react';const SomeComponent = memo(function SomeComponent(props) {  // ...});
```

```javascript
const Greeting = memo(function Greeting({ name }) {  return <h1>Hello, {name}!</h1>;});export default Greeting;
```

---

## <meta> – React

**URL**: https://react.dev/reference/react-dom/components/meta

**Contents**:
- <meta>
- Reference
  - <meta>
    - Props
    - Special rendering behavior
- Usage
  - Annotating the document with metadata
  - Annotating specific items within the document with metadata

The built-in browser <meta> component lets you add metadata to the document.

To add document metadata, render the built-in browser <meta> component. You can render <meta> from any component and React will always place the corresponding DOM element in the document head.

See more examples below.

<meta> supports all common element props.

It should have exactly one of the following props: name, httpEquiv, charset, itemProp. The <meta> component does something different depending on which of these props is specified.

React will always place the DOM element corresponding to the <meta> component within the document’s <head>, regardless of where in the React tree it is rendered. The <head> is the only valid place for <meta> to exist within the DOM, yet it’s convenient and keeps things composable if a component representing a specific page can render <meta> components itself.

There is one exception to this: if <meta> has an itemProp prop, there is no special behavior, because in this case it doesn’t represent metadata about the document but rather metadata about a specific part of the page.

You can annotate the document with metadata such as keywords, a summary, or the author’s name. React will place this metadata within the document <head> regardless of where in the React tree it is rendered.

You can render the <meta> component from any component. React will put a <meta> DOM node in the document <head>.

You can use the <meta> component with the itemProp prop to annotate specific items within the document with metadata. In this case, React will not place these annotations within the document <head> but will place them like any other React component.

**Examples**:

```text
<meta name="keywords" content="React, JavaScript, semantic markup, html" />
```

```text
<meta name="keywords" content="React, JavaScript, semantic markup, html" />
```

```text
<meta name="author" content="John Smith" /><meta name="keywords" content="React, JavaScript, semantic markup, html" /><meta name="description" content="API reference for the <meta> component in React DOM" />
```

---

## <option> – React

**URL**: https://react.dev/reference/react-dom/components/option

**Contents**:
- <option>
- Reference
  - <option>
    - Props
    - Caveats
- Usage
  - Displaying a select box with options

The built-in browser <option> component lets you render an option inside a <select> box.

The built-in browser <option> component lets you render an option inside a <select> box.

See more examples below.

<option> supports all common element props.

Additionally, <option> supports these props:

Render a <select> with a list of <option> components inside to display a select box. Give each <option> a value representing the data to be submitted with the form.

Read more about displaying a <select> with a list of <option> components.

**Examples**:

```text
<select>  <option value="someOption">Some option</option>  <option value="otherOption">Other option</option></select>
```

```text
<select>  <option value="someOption">Some option</option>  <option value="otherOption">Other option</option></select>
```

---

## panicThreshold – React

**URL**: https://react.dev/reference/react-compiler/panicThreshold

**Contents**:
- panicThreshold
- Reference
  - panicThreshold
    - Type
    - Default value
    - Options
    - Caveats
- Usage

The panicThreshold option controls how the React Compiler handles errors during compilation.

Determines whether compilation errors should fail the build or skip optimization.

For production builds, always use 'none'. This is the default value:

Temporarily use stricter thresholds to find issues:

**Examples**:

```text
{  panicThreshold: 'none' // Recommended}
```

```text
'none' | 'critical_errors' | 'all_errors'
```

```text
{  panicThreshold: 'none'}
```

---

## preconnect – React

**URL**: https://react.dev/reference/react-dom/preconnect

**Contents**:
- preconnect
- Reference
  - preconnect(href)
    - Parameters
    - Returns
    - Caveats
- Usage
  - Preconnecting when rendering

preconnect lets you eagerly connect to a server that you expect to load resources from.

To preconnect to a host, call the preconnect function from react-dom.

See more examples below.

The preconnect function provides the browser with a hint that it should open a connection to the given server. If the browser chooses to do so, this can speed up the loading of resources from that server.

preconnect returns nothing.

Call preconnect when rendering a component if you know that its children will load external resources from that host.

Call preconnect in an event handler before transitioning to a page or state where external resources will be needed. This gets the process started earlier than if you call it during the rendering of the new page or state.

**Examples**:

```text
preconnect("https://example.com");
```

```python
import { preconnect } from 'react-dom';function AppRoot() {  preconnect("https://example.com");  // ...}
```

```python
import { preconnect } from 'react-dom';function AppRoot() {  preconnect("https://example.com");  return ...;}
```

---

## prefetchDNS – React

**URL**: https://react.dev/reference/react-dom/prefetchDNS

**Contents**:
- prefetchDNS
- Reference
  - prefetchDNS(href)
    - Parameters
    - Returns
    - Caveats
- Usage
  - Prefetching DNS when rendering

prefetchDNS lets you eagerly look up the IP of a server that you expect to load resources from.

To look up a host, call the prefetchDNS function from react-dom.

See more examples below.

The prefetchDNS function provides the browser with a hint that it should look up the IP address of a given server. If the browser chooses to do so, this can speed up the loading of resources from that server.

prefetchDNS returns nothing.

Call prefetchDNS when rendering a component if you know that its children will load external resources from that host.

Call prefetchDNS in an event handler before transitioning to a page or state where external resources will be needed. This gets the process started earlier than if you call it during the rendering of the new page or state.

**Examples**:

```text
prefetchDNS("https://example.com");
```

```python
import { prefetchDNS } from 'react-dom';function AppRoot() {  prefetchDNS("https://example.com");  // ...}
```

```python
import { prefetchDNS } from 'react-dom';function AppRoot() {  prefetchDNS("https://example.com");  return ...;}
```

---

## preinitModule – React

**URL**: https://react.dev/reference/react-dom/preinitModule

**Contents**:
- preinitModule
  - Note
- Reference
  - preinitModule(href, options)
    - Parameters
    - Returns
    - Caveats
- Usage

React-based frameworks frequently handle resource loading for you, so you might not have to call this API yourself. Consult your framework’s documentation for details.

preinitModule lets you eagerly fetch and evaluate an ESM module.

To preinit an ESM module, call the preinitModule function from react-dom.

See more examples below.

The preinitModule function provides the browser with a hint that it should start downloading and executing the given module, which can save time. Modules that you preinit are executed when they finish downloading.

preinitModule returns nothing.

Call preinitModule when rendering a component if you know that it or its children will use a specific module and you’re OK with the module being evaluated and thereby taking effect immediately upon being downloaded.

If you want the browser to download the module but not to execute it right away, use preloadModule instead. If you want to preinit a script that isn’t an ESM module, use preinit.

Call preinitModule in an event handler before transitioning to a page or state where the module will be needed. This gets the process started earlier than if you call it during the rendering of the new page or state.

**Examples**:

```text
preinitModule("https://example.com/module.js", {as: "script"});
```

```python
import { preinitModule } from 'react-dom';function AppRoot() {  preinitModule("https://example.com/module.js", {as: "script"});  // ...}
```

```python
import { preinitModule } from 'react-dom';function AppRoot() {  preinitModule("https://example.com/module.js", {as: "script"});  return ...;}
```

---

## preinit – React

**URL**: https://react.dev/reference/react-dom/preinit

**Contents**:
- preinit
  - Note
- Reference
  - preinit(href, options)
    - Parameters
    - Returns
    - Caveats
- Usage

React-based frameworks frequently handle resource loading for you, so you might not have to call this API yourself. Consult your framework’s documentation for details.

preinit lets you eagerly fetch and evaluate a stylesheet or external script.

To preinit a script or stylesheet, call the preinit function from react-dom.

See more examples below.

The preinit function provides the browser with a hint that it should start downloading and executing the given resource, which can save time. Scripts that you preinit are executed when they finish downloading. Stylesheets that you preinit are inserted into the document, which causes them to go into effect right away.

preinit returns nothing.

Call preinit when rendering a component if you know that it or its children will use a specific resource, and you’re OK with the resource being evaluated and thereby taking effect immediately upon being downloaded.

If you want the browser to download the script but not to execute it right away, use preload instead. If you want to load an ESM module, use preinitModule.

Call preinit in an event handler before transitioning to a page or state where external resources will be needed. This gets the process started earlier than if you call it during the rendering of the new page or state.

**Examples**:

```text
preinit("https://example.com/script.js", {as: "script"});
```

```python
import { preinit } from 'react-dom';function AppRoot() {  preinit("https://example.com/script.js", {as: "script"});  // ...}
```

```python
import { preinit } from 'react-dom';function AppRoot() {  preinit("https://example.com/script.js", {as: "script"});  return ...;}
```

---

## preloadModule – React

**URL**: https://react.dev/reference/react-dom/preloadModule

**Contents**:
- preloadModule
  - Note
- Reference
  - preloadModule(href, options)
    - Parameters
    - Returns
    - Caveats
- Usage

React-based frameworks frequently handle resource loading for you, so you might not have to call this API yourself. Consult your framework’s documentation for details.

preloadModule lets you eagerly fetch an ESM module that you expect to use.

To preload an ESM module, call the preloadModule function from react-dom.

See more examples below.

The preloadModule function provides the browser with a hint that it should start downloading the given module, which can save time.

preloadModule returns nothing.

Call preloadModule when rendering a component if you know that it or its children will use a specific module.

If you want the browser to start executing the module immediately (rather than just downloading it), use preinitModule instead. If you want to load a script that isn’t an ESM module, use preload.

Call preloadModule in an event handler before transitioning to a page or state where the module will be needed. This gets the process started earlier than if you call it during the rendering of the new page or state.

**Examples**:

```text
preloadModule("https://example.com/module.js", {as: "script"});
```

```python
import { preloadModule } from 'react-dom';function AppRoot() {  preloadModule("https://example.com/module.js", {as: "script"});  // ...}
```

```python
import { preloadModule } from 'react-dom';function AppRoot() {  preloadModule("https://example.com/module.js", {as: "script"});  return ...;}
```

---

## preload – React

**URL**: https://react.dev/reference/react-dom/preload

**Contents**:
- preload
  - Note
- Reference
  - preload(href, options)
    - Parameters
    - Returns
    - Caveats
- Usage

React-based frameworks frequently handle resource loading for you, so you might not have to call this API yourself. Consult your framework’s documentation for details.

preload lets you eagerly fetch a resource such as a stylesheet, font, or external script that you expect to use.

To preload a resource, call the preload function from react-dom.

See more examples below.

The preload function provides the browser with a hint that it should start downloading the given resource, which can save time.

preload returns nothing.

Call preload when rendering a component if you know that it or its children will use a specific resource.

If you want the browser to start executing the script immediately (rather than just downloading it), use preinit instead. If you want to load an ESM module, use preloadModule.

Call preload in an event handler before transitioning to a page or state where external resources will be needed. This gets the process started earlier than if you call it during the rendering of the new page or state.

**Examples**:

```text
preload("https://example.com/font.woff2", {as: "font"});
```

```python
import { preload } from 'react-dom';function AppRoot() {  preload("https://example.com/font.woff2", {as: "font"});  // ...}
```

```python
import { preload } from 'react-dom';function AppRoot() {  preload("https://example.com/script.js", {as: "script"});  return ...;}
```

---

## prerenderToNodeStream – React

**URL**: https://react.dev/reference/react-dom/static/prerenderToNodeStream

**Contents**:
- prerenderToNodeStream
  - Note
- Reference
  - prerenderToNodeStream(reactNode, options?)
    - Parameters
    - Returns
    - Caveats
  - Note

prerenderToNodeStream renders a React tree to a static HTML string using a Node.js Stream.

This API is specific to Node.js. Environments with Web Streams, like Deno and modern edge runtimes, should use prerender instead.

Call prerenderToNodeStream to render your app to static HTML.

On the client, call hydrateRoot to make the server-generated HTML interactive.

See more examples below.

reactNode: A React node you want to render to HTML. For example, a JSX node like <App />. It is expected to represent the entire document, so the App component should render the <html> tag.

optional options: An object with static generation options.

prerenderToNodeStream returns a Promise:

nonce is not an available option when prerendering. Nonces must be unique per request and if you use nonces to secure your application with CSP it would be inappropriate and insecure to include the nonce value in the prerender itself.

The static prerenderToNodeStream API is used for static server-side generation (SSG). Unlike renderToString, prerenderToNodeStream waits for all data to load before resolving. This makes it suitable for generating static HTML for a full page, including data that needs to be fetched using Suspense. To stream content as it loads, use a streaming server-side render (SSR) API like renderToReadableStream.

prerenderToNodeStream can be aborted and resumed later with resumeToPipeableStream to support partial pre-rendering.

Call prerenderToNodeStream to render your React tree to static HTML into a Node.js Stream:

Along with the root component, you need to provide a list of bootstrap <script> paths. Your root component should return the entire document including the root <html> tag.

For example, it might look like this:

React will inject the doctype and your bootstrap <script> tags into the resulting HTML stream:

On the client, your bootstrap script should hydrate the entire document with a call to hydrateRoot:

This will attach event listeners to the static server-

*[Content truncated - see full docs]*

**Examples**:

```javascript
const {prelude, postponed} = await prerenderToNodeStream(reactNode, options?)
```

```python
import { prerenderToNodeStream } from 'react-dom/static';// The route handler syntax depends on your backend frameworkapp.use('/', async (request, response) => {  const { prelude } = await prerenderToNodeStream(<App />, {    bootstrapScripts: ['/main.js'],  });  response.setHeader('Content-Type', 'text/plain');  prelude.pipe(response);});
```

```python
import { prerenderToNodeStream } from 'react-dom/static';// The route handler syntax depends on your backend frameworkapp.use('/', async (request, response) => {  const { prelude } = await prerenderToNodeStream(<App />, {    bootstrapScripts: ['/main.js'],  });  response.setHeader('Content-Type', 'text/plain');  prelude.pipe(response);});
```

---

## prerender – React

**URL**: https://react.dev/reference/react-dom/static/prerender

**Contents**:
- prerender
  - Note
- Reference
  - prerender(reactNode, options?)
    - Parameters
    - Returns
    - Caveats
  - Note

prerender renders a React tree to a static HTML string using a Web Stream.

This API depends on Web Streams. For Node.js, use prerenderToNodeStream instead.

Call prerender to render your app to static HTML.

On the client, call hydrateRoot to make the server-generated HTML interactive.

See more examples below.

reactNode: A React node you want to render to HTML. For example, a JSX node like <App />. It is expected to represent the entire document, so the App component should render the <html> tag.

optional options: An object with static generation options.

prerender returns a Promise:

nonce is not an available option when prerendering. Nonces must be unique per request and if you use nonces to secure your application with CSP it would be inappropriate and insecure to include the nonce value in the prerender itself.

The static prerender API is used for static server-side generation (SSG). Unlike renderToString, prerender waits for all data to load before resolving. This makes it suitable for generating static HTML for a full page, including data that needs to be fetched using Suspense. To stream content as it loads, use a streaming server-side render (SSR) API like renderToReadableStream.

prerender can be aborted and later either continued with resumeAndPrerender or resumed with resume to support partial pre-rendering.

Call prerender to render your React tree to static HTML into a Readable Web Stream::

Along with the root component, you need to provide a list of bootstrap <script> paths. Your root component should return the entire document including the root <html> tag.

For example, it might look like this:

React will inject the doctype and your bootstrap <script> tags into the resulting HTML stream:

On the client, your bootstrap script should hydrate the entire document with a call to hydrateRoot:

This will attach event listeners to the static server-generated HTML and make it interactive.

The final asset URLs (like JavaScript and CSS files) are often

*[Content truncated - see full docs]*

**Examples**:

```javascript
const {prelude, postponed} = await prerender(reactNode, options?)
```

```python
import { prerender } from 'react-dom/static';async function handler(request, response) {  const {prelude} = await prerender(<App />, {    bootstrapScripts: ['/main.js']  });  return new Response(prelude, {    headers: { 'content-type': 'text/html' },  });}
```

```python
import { prerender } from 'react-dom/static';async function handler(request) {  const {prelude} = await prerender(<App />, {    bootstrapScripts: ['/main.js']  });  return new Response(prelude, {    headers: { 'content-type': 'text/html' },  });}
```

---

## <progress> – React

**URL**: https://react.dev/reference/react-dom/components/progress

**Contents**:
- <progress>
- Reference
  - <progress>
    - Props
- Usage
  - Controlling a progress indicator

The built-in browser <progress> component lets you render a progress indicator.

To display a progress indicator, render the built-in browser <progress> component.

See more examples below.

<progress> supports all common element props.

Additionally, <progress> supports these props:

To display a progress indicator, render a <progress> component. You can pass a number value between 0 and the max value you specify. If you don’t pass a max value, it will assumed to be 1 by default.

If the operation is not ongoing, pass value={null} to put the progress indicator into an indeterminate state.

**Examples**:

```text
<progress value={0.5} />
```

```text
<progress value={0.5} />
```

---

## renderToPipeableStream – React

**URL**: https://react.dev/reference/react-dom/server/renderToPipeableStream

**Contents**:
- renderToPipeableStream
  - Note
- Reference
  - renderToPipeableStream(reactNode, options?)
    - Parameters
    - Returns
- Usage
  - Rendering a React tree as HTML to a Node.js Stream

renderToPipeableStream renders a React tree to a pipeable Node.js Stream.

This API is specific to Node.js. Environments with Web Streams, like Deno and modern edge runtimes, should use renderToReadableStream instead.

Call renderToPipeableStream to render your React tree as HTML into a Node.js Stream.

On the client, call hydrateRoot to make the server-generated HTML interactive.

See more examples below.

reactNode: A React node you want to render to HTML. For example, a JSX element like <App />. It is expected to represent the entire document, so the App component should render the <html> tag.

optional options: An object with streaming options.

renderToPipeableStream returns an object with two methods:

Call renderToPipeableStream to render your React tree as HTML into a Node.js Stream:

Along with the root component, you need to provide a list of bootstrap <script> paths. Your root component should return the entire document including the root <html> tag.

For example, it might look like this:

React will inject the doctype and your bootstrap <script> tags into the resulting HTML stream:

On the client, your bootstrap script should hydrate the entire document with a call to hydrateRoot:

This will attach event listeners to the server-generated HTML and make it interactive.

The final asset URLs (like JavaScript and CSS files) are often hashed after the build. For example, instead of styles.css you might end up with styles.123456.css. Hashing static asset filenames guarantees that every distinct build of the same asset will have a different filename. This is useful because it lets you safely enable long-term caching for static assets: a file with a certain name would never change content.

However, if you don’t know the asset URLs until after the build, there’s no way for you to put them in the source code. For example, hardcoding "/styles.css" into JSX like earlier wouldn’t work. To keep them out of your source code, your root component can read the real filen

*[Content truncated - see full docs]*

**Examples**:

```javascript
const { pipe, abort } = renderToPipeableStream(reactNode, options?)
```

```python
import { renderToPipeableStream } from 'react-dom/server';const { pipe } = renderToPipeableStream(<App />, {  bootstrapScripts: ['/main.js'],  onShellReady() {    response.setHeader('content-type', 'text/html');    pipe(response);  }});
```

```python
import { renderToPipeableStream } from 'react-dom/server';// The route handler syntax depends on your backend frameworkapp.use('/', (request, response) => {  const { pipe } = renderToPipeableStream(<App />, {    bootstrapScripts: ['/main.js'],    onShellReady() {      response.setHeader('content-type', 'text/html');      pipe(response);    }  });});
```

---

## renderToReadableStream – React

**URL**: https://react.dev/reference/react-dom/server/renderToReadableStream

**Contents**:
- renderToReadableStream
  - Note
- Reference
  - renderToReadableStream(reactNode, options?)
    - Parameters
    - Returns
- Usage
  - Rendering a React tree as HTML to a Readable Web Stream

renderToReadableStream renders a React tree to a Readable Web Stream.

This API depends on Web Streams. For Node.js, use renderToPipeableStream instead.

Call renderToReadableStream to render your React tree as HTML into a Readable Web Stream.

On the client, call hydrateRoot to make the server-generated HTML interactive.

See more examples below.

reactNode: A React node you want to render to HTML. For example, a JSX element like <App />. It is expected to represent the entire document, so the App component should render the <html> tag.

optional options: An object with streaming options.

renderToReadableStream returns a Promise:

The returned stream has an additional property:

Call renderToReadableStream to render your React tree as HTML into a Readable Web Stream:

Along with the root component, you need to provide a list of bootstrap <script> paths. Your root component should return the entire document including the root <html> tag.

For example, it might look like this:

React will inject the doctype and your bootstrap <script> tags into the resulting HTML stream:

On the client, your bootstrap script should hydrate the entire document with a call to hydrateRoot:

This will attach event listeners to the server-generated HTML and make it interactive.

The final asset URLs (like JavaScript and CSS files) are often hashed after the build. For example, instead of styles.css you might end up with styles.123456.css. Hashing static asset filenames guarantees that every distinct build of the same asset will have a different filename. This is useful because it lets you safely enable long-term caching for static assets: a file with a certain name would never change content.

However, if you don’t know the asset URLs until after the build, there’s no way for you to put them in the source code. For example, hardcoding "/styles.css" into JSX like earlier wouldn’t work. To keep them out of your source code, your root component can read the real filenames from a map passed 

*[Content truncated - see full docs]*

**Examples**:

```javascript
const stream = await renderToReadableStream(reactNode, options?)
```

```python
import { renderToReadableStream } from 'react-dom/server';async function handler(request) {  const stream = await renderToReadableStream(<App />, {    bootstrapScripts: ['/main.js']  });  return new Response(stream, {    headers: { 'content-type': 'text/html' },  });}
```

```python
import { renderToReadableStream } from 'react-dom/server';async function handler(request) {  const stream = await renderToReadableStream(<App />, {    bootstrapScripts: ['/main.js']  });  return new Response(stream, {    headers: { 'content-type': 'text/html' },  });}
```

---

## renderToStaticMarkup – React

**URL**: https://react.dev/reference/react-dom/server/renderToStaticMarkup

**Contents**:
- renderToStaticMarkup
- Reference
  - renderToStaticMarkup(reactNode, options?)
    - Parameters
    - Returns
    - Caveats
- Usage
  - Rendering a non-interactive React tree as HTML to a string

renderToStaticMarkup renders a non-interactive React tree to an HTML string.

On the server, call renderToStaticMarkup to render your app to HTML.

It will produce non-interactive HTML output of your React components.

See more examples below.

renderToStaticMarkup output cannot be hydrated.

renderToStaticMarkup has limited Suspense support. If a component suspends, renderToStaticMarkup immediately sends its fallback as HTML.

renderToStaticMarkup works in the browser, but using it in the client code is not recommended. If you need to render a component to HTML in the browser, get the HTML by rendering it into a DOM node.

Call renderToStaticMarkup to render your app to an HTML string which you can send with your server response:

This will produce the initial non-interactive HTML output of your React components.

This method renders non-interactive HTML that cannot be hydrated. This is useful if you want to use React as a simple static page generator, or if you’re rendering completely static content like emails.

Interactive apps should use renderToString on the server and hydrateRoot on the client.

**Examples**:

```javascript
const html = renderToStaticMarkup(reactNode, options?)
```

```python
import { renderToStaticMarkup } from 'react-dom/server';const html = renderToStaticMarkup(<Page />);
```

```python
import { renderToStaticMarkup } from 'react-dom/server';// The route handler syntax depends on your backend frameworkapp.use('/', (request, response) => {  const html = renderToStaticMarkup(<Page />);  response.send(html);});
```

---

## renderToString – React

**URL**: https://react.dev/reference/react-dom/server/renderToString

**Contents**:
- renderToString
  - Pitfall
- Reference
  - renderToString(reactNode, options?)
    - Parameters
    - Returns
    - Caveats
- Usage

renderToString does not support streaming or waiting for data. See the alternatives.

renderToString renders a React tree to an HTML string.

On the server, call renderToString to render your app to HTML.

On the client, call hydrateRoot to make the server-generated HTML interactive.

See more examples below.

reactNode: A React node you want to render to HTML. For example, a JSX node like <App />.

optional options: An object for server render.

renderToString has limited Suspense support. If a component suspends, renderToString immediately sends its fallback as HTML.

renderToString works in the browser, but using it in the client code is not recommended.

Call renderToString to render your app to an HTML string which you can send with your server response:

This will produce the initial non-interactive HTML output of your React components. On the client, you will need to call hydrateRoot to hydrate that server-generated HTML and make it interactive.

renderToString does not support streaming or waiting for data. See the alternatives.

renderToString returns a string immediately, so it does not support streaming content as it loads.

When possible, we recommend using these fully-featured alternatives:

You can continue using renderToString if your server environment does not support streams.

renderToString returns a string immediately, so it does not support waiting for data to load for static HTML generation.

We recommend using these fully-featured alternatives:

You can continue using renderToString if your static site generation environment does not support streams.

Sometimes, renderToString is used on the client to convert some component to HTML.

Importing react-dom/server on the client unnecessarily increases your bundle size and should be avoided. If you need to render some component to HTML in the browser, use createRoot and read HTML from the DOM:

The flushSync call is necessary so that the DOM is updated before reading its innerHTML property.

render

*[Content truncated - see full docs]*

**Examples**:

```javascript
const html = renderToString(reactNode, options?)
```

```python
import { renderToString } from 'react-dom/server';const html = renderToString(<App />);
```

```python
import { renderToString } from 'react-dom/server';// The route handler syntax depends on your backend frameworkapp.use('/', (request, response) => {  const html = renderToString(<App />);  response.send(html);});
```

---

## rules-of-hooks – React

**URL**: https://react.dev/reference/eslint-plugin-react-hooks/lints/rules-of-hooks

**Contents**:
- rules-of-hooks
- Rule Details
- Common Violations
  - Note
  - use hook
  - Invalid
  - Valid
- Troubleshooting

Validates that components and hooks follow the Rules of Hooks.

React relies on the order in which hooks are called to correctly preserve state between renders. Each time your component renders, React expects the exact same hooks to be called in the exact same order. When hooks are called conditionally or in loops, React loses track of which state corresponds to which hook call, leading to bugs like state mismatches and “Rendered fewer/more hooks than expected” errors.

These patterns violate the Rules of Hooks:

The use hook is different from other React hooks. You can call it conditionally and in loops:

However, use still has restrictions:

Learn more: use API Reference

Examples of incorrect code for this rule:

Examples of correct code for this rule:

You’re trying to conditionally call useEffect:

Call the hook unconditionally, check condition inside:

There are better ways to fetch data rather than in a useEffect. Consider using React Query, useSWR, or React Router 6.4+ for data fetching. These solutions handle deduplicating requests, caching responses, and avoiding network waterfalls.

Learn more: Fetching Data

You’re trying to conditionally initialize state:

Always call useState, conditionally set the initial value:

You can configure custom effect hooks using shared ESLint settings (available in eslint-plugin-react-hooks 6.1.1 and later):

This shared configuration is used by both rules-of-hooks and exhaustive-deps rules, ensuring consistent behavior across all hook-related linting.

**Examples**:

```javascript
// ✅ `use` can be conditionalif (shouldFetch) {  const data = use(fetchPromise);}// ✅ `use` can be in loopsfor (const promise of promises) {  results.push(use(promise));}
```

```javascript
// ❌ Hook in conditionif (isLoggedIn) {  const [user, setUser] = useState(null);}// ❌ Hook after early returnif (!data) return <Loading />;const [processed, setProcessed] = useState(data);// ❌ Hook in callback<button onClick={() => {  const [clicked, setClicked] = useState(false);}}/>// ❌ `use` in try/catchtry {  const data = use(promise);} catch (e) {  // error handling}// ❌ Hook at module levelconst globalState = useState(0); // Outside component
```

```javascript
function Component({ isSpecial, shouldFetch, fetchPromise }) {  // ✅ Hooks at top level  const [count, setCount] = useState(0);  const [name, setName] = useState('');  if (!isSpecial) {    return null;  }  if (shouldFetch) {    // ✅ `use` can be conditional    const data = use(fetchPromise);    return <div>{data}</div>;  }  return <div>{name}: {count}</div>;}
```

---

## <script> – React

**URL**: https://react.dev/reference/react-dom/components/script

**Contents**:
- <script>
- Reference
  - <script>
    - Props
    - Special rendering behavior
- Usage
  - Rendering an external script
  - Note

The built-in browser <script> component lets you add a script to your document.

To add inline or external scripts to your document, render the built-in browser <script> component. You can render <script> from any component and React will in certain cases place the corresponding DOM element in the document head and de-duplicate identical scripts.

See more examples below.

<script> supports all common element props.

It should have either children or a src prop.

Other supported props:

Props that disable React’s special treatment of scripts:

Props that are not recommended for use with React:

React can move <script> components to the document’s <head> and de-duplicate identical scripts.

To opt into this behavior, provide the src and async={true} props. React will de-duplicate scripts if they have the same src. The async prop must be true to allow scripts to be safely moved.

This special treatment comes with two caveats:

If a component depends on certain scripts in order to be displayed correctly, you can render a <script> within the component. However, the component might be committed before the script has finished loading. You can start depending on the script content once the load event is fired e.g. by using the onLoad prop.

React will de-duplicate scripts that have the same src, inserting only one of them into the DOM even if multiple components render it.

When you want to use a script, it can be beneficial to call the preinit function. Calling this function may allow the browser to start fetching the script earlier than if you just render a <script> component, for example by sending an HTTP Early Hints response.

To include an inline script, render the <script> component with the script source code as its children. Inline scripts are not de-duplicated or moved to the document <head>.

**Examples**:

```vue
<script> alert("hi!") </script>
```

```vue
<script> alert("hi!") </script><script src="script.js" />
```

---

## <select> – React

**URL**: https://react.dev/reference/react-dom/components/select

**Contents**:
- <select>
- Reference
  - <select>
    - Props
    - Caveats
- Usage
  - Displaying a select box with options
  - Providing a label for a select box

The built-in browser <select> component lets you render a select box with options.

To display a select box, render the built-in browser <select> component.

See more examples below.

<select> supports all common element props.

You can make a select box controlled by passing a value prop:

When you pass value, you must also pass an onChange handler that updates the passed value.

If your <select> is uncontrolled, you may pass the defaultValue prop instead:

These <select> props are relevant both for uncontrolled and controlled select boxes:

Render a <select> with a list of <option> components inside to display a select box. Give each <option> a value representing the data to be submitted with the form.

Typically, you will place every <select> inside a <label> tag. This tells the browser that this label is associated with that select box. When the user clicks the label, the browser will automatically focus the select box. It’s also essential for accessibility: a screen reader will announce the label caption when the user focuses the select box.

If you can’t nest <select> into a <label>, associate them by passing the same ID to <select id> and <label htmlFor>. To avoid conflicts between multiple instances of one component, generate such an ID with useId.

By default, the browser will select the first <option> in the list. To select a different option by default, pass that <option>’s value as the defaultValue to the <select> element.

Unlike in HTML, passing a selected attribute to an individual <option> is not supported.

Pass multiple={true} to the <select> to let the user select multiple options. In that case, if you also specify defaultValue to choose the initially selected options, it must be an array.

Add a <form> around your select box with a <button type="submit"> inside. It will call your <form onSubmit> event handler. By default, the browser will send the form data to the current URL and refresh the page. You can override that behavior by calling e.preve

*[Content truncated - see full docs]*

**Examples**:

```text
<select>  <option value="someOption">Some option</option>  <option value="otherOption">Other option</option></select>
```

```text
<select>  <option value="someOption">Some option</option>  <option value="otherOption">Other option</option></select>
```

```javascript
function FruitPicker() {  const [selectedFruit, setSelectedFruit] = useState('orange'); // Declare a state variable...  // ...  return (    <select      value={selectedFruit} // ...force the select's value to match the state variable...      onChange={e => setSelectedFruit(e.target.value)} // ... and update the state variable on any change!    >      <option value="apple">Apple</option>      <option value="banana">Banana</option>      <option value="orange">Orange</option>    </select>  );}
```

---

## startTransition – React

**URL**: https://react.dev/reference/react/startTransition

**Contents**:
- startTransition
- Reference
  - startTransition(action)
    - Parameters
    - Returns
    - Caveats
- Usage
  - Marking a state update as a non-blocking Transition

startTransition lets you render a part of the UI in the background.

The startTransition function lets you mark a state update as a Transition.

See more examples below.

startTransition does not return anything.

startTransition does not provide a way to track whether a Transition is pending. To show a pending indicator while the Transition is ongoing, you need useTransition instead.

You can wrap an update into a Transition only if you have access to the set function of that state. If you want to start a Transition in response to some prop or a custom Hook return value, try useDeferredValue instead.

The function you pass to startTransition is called immediately, marking all state updates that happen while it executes as Transitions. If you try to perform state updates in a setTimeout, for example, they won’t be marked as Transitions.

You must wrap any state updates after any async requests in another startTransition to mark them as Transitions. This is a known limitation that we will fix in the future (see Troubleshooting).

A state update marked as a Transition will be interrupted by other state updates. For example, if you update a chart component inside a Transition, but then start typing into an input while the chart is in the middle of a re-render, React will restart the rendering work on the chart component after handling the input state update.

Transition updates can’t be used to control text inputs.

If there are multiple ongoing Transitions, React currently batches them together. This is a limitation that may be removed in a future release.

You can mark a state update as a Transition by wrapping it in a startTransition call:

Transitions let you keep the user interface updates responsive even on slow devices.

With a Transition, your UI stays responsive in the middle of a re-render. For example, if the user clicks a tab but then change their mind and click another tab, they can do that without waiting for the first re-render to finish.

startTransitio

*[Content truncated - see full docs]*

**Examples**:

```text
startTransition(action)
```

```python
import { startTransition } from 'react';function TabContainer() {  const [tab, setTab] = useState('about');  function selectTab(nextTab) {    startTransition(() => {      setTab(nextTab);    });  }  // ...}
```

```python
import { startTransition } from 'react';function TabContainer() {  const [tab, setTab] = useState('about');  function selectTab(nextTab) {    startTransition(() => {      setTab(nextTab);    });  }  // ...}
```

---

## <style> – React

**URL**: https://react.dev/reference/react-dom/components/style

**Contents**:
- <style>
- Reference
  - <style>
    - Props
    - Special rendering behavior
- Usage
  - Rendering an inline CSS stylesheet

The built-in browser <style> component lets you add inline CSS stylesheets to your document.

To add inline styles to your document, render the built-in browser <style> component. You can render <style> from any component and React will in certain cases place the corresponding DOM element in the document head and de-duplicate identical styles.

See more examples below.

<style> supports all common element props.

Props that are not recommended for use with React:

React can move <style> components to the document’s <head>, de-duplicate identical stylesheets, and suspend while the stylesheet is loading.

To opt into this behavior, provide the href and precedence props. React will de-duplicate styles if they have the same href. The precedence prop tells React where to rank the <style> DOM node relative to others in the document <head>, which determines which stylesheet can override the other.

This special treatment comes with three caveats:

If a component depends on certain CSS styles in order to be displayed correctly, you can render an inline stylesheet within the component.

The href prop should uniquely identify the stylesheet, because React will de-duplicate stylesheets that have the same href. If you supply a precedence prop, React will reorder inline stylesheets based on the order these values appear in the component tree.

Inline stylesheets will not trigger Suspense boundaries while they’re loading. Even if they load async resources like fonts or images.

**Examples**:

```text
<style>{` p { color: red; } `}</style>
```

```text
<style>{` p { color: red; } `}</style>
```

---

## target – React

**URL**: https://react.dev/reference/react-compiler/target

**Contents**:
- target
- Reference
  - target
    - Type
    - Default value
    - Valid values
    - Caveats
- Usage

The target option specifies which React version the compiler should generate code for.

Configures the React version compatibility for the compiled output.

For React 19, no special configuration is needed:

The compiler will use React 19’s built-in runtime APIs:

For React 17 and React 18 projects, you need two steps:

The compiler will use the polyfill runtime for both versions:

If you see errors like “Cannot find module ‘react/compiler-runtime’“:

Check your React version:

If using React 17 or 18, install the runtime:

Ensure your target matches your React version:

Ensure the runtime package is:

To verify the correct runtime is being used, note the different import (react/compiler-runtime for builtin, react-compiler-runtime standalone package for 17/18):

**Examples**:

```text
{  target: '19' // or '18', '17'}
```

```text
'17' | '18' | '19'
```

```text
{  // defaults to target: '19'}
```

---

## <textarea> – React

**URL**: https://react.dev/reference/react-dom/components/textarea

**Contents**:
- <textarea>
- Reference
  - <textarea>
    - Props
    - Caveats
- Usage
  - Displaying a text area
  - Providing a label for a text area

The built-in browser <textarea> component lets you render a multiline text input.

To display a text area, render the built-in browser <textarea> component.

See more examples below.

<textarea> supports all common element props.

You can make a text area controlled by passing a value prop:

When you pass value, you must also pass an onChange handler that updates the passed value.

If your <textarea> is uncontrolled, you may pass the defaultValue prop instead:

These <textarea> props are relevant both for uncontrolled and controlled text areas:

Render <textarea> to display a text area. You can specify its default size with the rows and cols attributes, but by default the user will be able to resize it. To disable resizing, you can specify resize: none in the CSS.

Typically, you will place every <textarea> inside a <label> tag. This tells the browser that this label is associated with that text area. When the user clicks the label, the browser will focus the text area. It’s also essential for accessibility: a screen reader will announce the label caption when the user focuses the text area.

If you can’t nest <textarea> into a <label>, associate them by passing the same ID to <textarea id> and <label htmlFor>. To avoid conflicts between instances of one component, generate such an ID with useId.

You can optionally specify the initial value for the text area. Pass it as the defaultValue string.

Unlike in HTML, passing initial text like <textarea>Some content</textarea> is not supported.

Add a <form> around your textarea with a <button type="submit"> inside. It will call your <form onSubmit> event handler. By default, the browser will send the form data to the current URL and refresh the page. You can override that behavior by calling e.preventDefault(). Read the form data with new FormData(e.target).

Give a name to your <textarea>, for example <textarea name="postContent" />. The name you specified will be used as a key in the form data, for example { postConten

*[Content truncated - see full docs]*

**Examples**:

```text
<textarea />
```

```text
<textarea name="postContent" />
```

```javascript
function NewPost() {  const [postContent, setPostContent] = useState(''); // Declare a state variable...  // ...  return (    <textarea      value={postContent} // ...force the input's value to match the state variable...      onChange={e => setPostContent(e.target.value)} // ... and update the state variable on any edits!    />  );}
```

---

## <title> – React

**URL**: https://react.dev/reference/react-dom/components/title

**Contents**:
- <title>
- Reference
  - <title>
    - Props
    - Special rendering behavior
  - Pitfall
- Usage
  - Set the document title

The built-in browser <title> component lets you specify the title of the document.

To specify the title of the document, render the built-in browser <title> component. You can render <title> from any component and React will always place the corresponding DOM element in the document head.

See more examples below.

<title> supports all common element props.

React will always place the DOM element corresponding to the <title> component within the document’s <head>, regardless of where in the React tree it is rendered. The <head> is the only valid place for <title> to exist within the DOM, yet it’s convenient and keeps things composable if a component representing a specific page can render its <title> itself.

There are two exception to this:

Only render a single <title> at a time. If more than one component renders a <title> tag at the same time, React will place all of those titles in the document head. When this happens, the behavior of browsers and search engines is undefined.

Render the <title> component from any component with text as its children. React will put a <title> DOM node in the document <head>.

The children of the <title> component must be a single string of text. (Or a single number or a single object with a toString method.) It might not be obvious, but using JSX curly braces like this:

… actually causes the <title> component to get a two-element array as its children (the string "Results page" and the value of pageNumber). This will cause an error. Instead, use string interpolation to pass <title> a single string:

**Examples**:

```text
<title>My Blog</title>
```

```text
<title>My Blog</title>
```

```text
<title>Results page {pageNumber}</title> // 🔴 Problem: This is not a single string
```

---

## unmountComponentAtNode – React

**URL**: https://react.dev/reference/react-dom/unmountComponentAtNode

**Contents**:
- unmountComponentAtNode
  - Deprecated
- Reference
  - unmountComponentAtNode(domNode)
    - Parameters
    - Returns
- Usage
  - Removing a React app from a DOM element

This API will be removed in a future major version of React.

In React 18, unmountComponentAtNode was replaced by root.unmount().

unmountComponentAtNode removes a mounted React component from the DOM.

Call unmountComponentAtNode to remove a mounted React component from the DOM and clean up its event handlers and state.

See more examples below.

unmountComponentAtNode returns true if a component was unmounted and false otherwise.

Call unmountComponentAtNode to remove a mounted React component from a browser DOM node and clean up its event handlers and state.

Occasionally, you may want to “sprinkle” React on an existing page, or a page that is not fully written in React. In those cases, you may need to “stop” the React app, by removing all of the UI, state, and listeners from the DOM node it was rendered to.

In this example, clicking “Render React App” will render a React app. Click “Unmount React App” to destroy it:

**Examples**:

```text
unmountComponentAtNode(domNode)
```

```python
import { unmountComponentAtNode } from 'react-dom';const domNode = document.getElementById('root');render(<App />, domNode);unmountComponentAtNode(domNode);
```

```python
import { render, unmountComponentAtNode } from 'react-dom';import App from './App.js';const rootNode = document.getElementById('root');render(<App />, rootNode);// ...unmountComponentAtNode(rootNode);
```

---

## useActionState – React

**URL**: https://react.dev/reference/react/useActionState

**Contents**:
- useActionState
  - Note
- Reference
  - useActionState(action, initialState, permalink?)
    - Parameters
    - Returns
    - Caveats
- Usage

useActionState is a Hook that allows you to update state based on the result of a form action.

In earlier React Canary versions, this API was part of React DOM and called useFormState.

Call useActionState at the top level of your component to create component state that is updated when a form action is invoked. You pass useActionState an existing form action function as well as an initial state, and it returns a new action that you use in your form, along with the latest form state and whether the Action is still pending. The latest form state is also passed to the function that you provided.

The form state is the value returned by the action when the form was last submitted. If the form has not yet been submitted, it is the initial state that you pass.

If used with a Server Function, useActionState allows the server’s response from submitting the form to be shown even before hydration has completed.

See more examples below.

useActionState returns an array with the following values:

Call useActionState at the top level of your component to access the return value of an action from the last time a form was submitted.

useActionState returns an array with the following items:

When the form is submitted, the action function that you provided will be called. Its return value will become the new current state of the form.

The action that you provide will also receive a new first argument, namely the current state of the form. The first time the form is submitted, this will be the initial state you provided, while with subsequent submissions, it will be the return value from the last time the action was called. The rest of the arguments are the same as if useActionState had not been used.

To display messages such as an error message or toast that’s returned by a Server Function, wrap the action in a call to useActionState.

When you wrap an action with useActionState, it gets an extra argument as its first argument. The submitted form data is therefore its secon

*[Content truncated - see full docs]*

**Examples**:

```javascript
const [state, formAction, isPending] = useActionState(fn, initialState, permalink?);
```

```python
import { useActionState } from "react";async function increment(previousState, formData) {  return previousState + 1;}function StatefulForm({}) {  const [state, formAction] = useActionState(increment, 0);  return (    <form>      {state}      <button formAction={formAction}>Increment</button>    </form>  )}
```

```python
import { useActionState } from 'react';import { action } from './actions.js';function MyComponent() {  const [state, formAction] = useActionState(action, null);  // ...  return (    <form action={formAction}>      {/* ... */}    </form>  );}
```

---

## useCallback – React

**URL**: https://react.dev/reference/react/useCallback

**Contents**:
- useCallback
  - Note
- Reference
  - useCallback(fn, dependencies)
    - Parameters
    - Returns
    - Caveats
- Usage

useCallback is a React Hook that lets you cache a function definition between re-renders.

React Compiler automatically memoizes values and functions, reducing the need for manual useCallback calls. You can use the compiler to handle memoization automatically.

Call useCallback at the top level of your component to cache a function definition between re-renders:

See more examples below.

fn: The function value that you want to cache. It can take any arguments and return any values. React will return (not call!) your function back to you during the initial render. On next renders, React will give you the same function again if the dependencies have not changed since the last render. Otherwise, it will give you the function that you have passed during the current render, and store it in case it can be reused later. React will not call your function. The function is returned to you so you can decide when and whether to call it.

dependencies: The list of all reactive values referenced inside of the fn code. Reactive values include props, state, and all the variables and functions declared directly inside your component body. If your linter is configured for React, it will verify that every reactive value is correctly specified as a dependency. The list of dependencies must have a constant number of items and be written inline like [dep1, dep2, dep3]. React will compare each dependency with its previous value using the Object.is comparison algorithm.

On the initial render, useCallback returns the fn function you have passed.

During subsequent renders, it will either return an already stored fn function from the last render (if the dependencies haven’t changed), or return the fn function you have passed during this render.

When you optimize rendering performance, you will sometimes need to cache the functions that you pass to child components. Let’s first look at the syntax for how to do this, and then see in which cases it’s useful.

To cache a function between re-r

*[Content truncated - see full docs]*

**Examples**:

```javascript
const cachedFn = useCallback(fn, dependencies)
```

```python
import { useCallback } from 'react';export default function ProductPage({ productId, referrer, theme }) {  const handleSubmit = useCallback((orderDetails) => {    post('/product/' + productId + '/buy', {      referrer,      orderDetails,    });  }, [productId, referrer]);
```

```python
import { useCallback } from 'react';function ProductPage({ productId, referrer, theme }) {  const handleSubmit = useCallback((orderDetails) => {    post('/product/' + productId + '/buy', {      referrer,      orderDetails,    });  }, [productId, referrer]);  // ...
```

---

## useContext – React

**URL**: https://react.dev/reference/react/useContext

**Contents**:
- useContext
- Reference
  - useContext(SomeContext)
    - Parameters
    - Returns
    - Caveats
- Usage
  - Passing data deeply into the tree

useContext is a React Hook that lets you read and subscribe to context from your component.

Call useContext at the top level of your component to read and subscribe to context.

See more examples below.

useContext returns the context value for the calling component. It is determined as the value passed to the closest SomeContext above the calling component in the tree. If there is no such provider, then the returned value will be the defaultValue you have passed to createContext for that context. The returned value is always up-to-date. React automatically re-renders components that read some context if it changes.

Call useContext at the top level of your component to read and subscribe to context.

useContext returns the context value for the context you passed. To determine the context value, React searches the component tree and finds the closest context provider above for that particular context.

To pass context to a Button, wrap it or one of its parent components into the corresponding context provider:

It doesn’t matter how many layers of components there are between the provider and the Button. When a Button anywhere inside of Form calls useContext(ThemeContext), it will receive "dark" as the value.

useContext() always looks for the closest provider above the component that calls it. It searches upwards and does not consider providers in the component from which you’re calling useContext().

Often, you’ll want the context to change over time. To update context, combine it with state. Declare a state variable in the parent component, and pass the current state down as the context value to the provider.

Now any Button inside of the provider will receive the current theme value. If you call setTheme to update the theme value that you pass to the provider, all Button components will re-render with the new 'light' value.

In this example, the MyApp component holds a state variable which is then passed to the ThemeContext provider. Checking the “Dark mode” c

*[Content truncated - see full docs]*

**Examples**:

```javascript
const value = useContext(SomeContext)
```

```python
import { useContext } from 'react';function MyComponent() {  const theme = useContext(ThemeContext);  // ...
```

```python
import { useContext } from 'react';function Button() {  const theme = useContext(ThemeContext);  // ...
```

---

## useDebugValue – React

**URL**: https://react.dev/reference/react/useDebugValue

**Contents**:
- useDebugValue
- Reference
  - useDebugValue(value, format?)
    - Parameters
    - Returns
- Usage
  - Adding a label to a custom Hook
  - Note

useDebugValue is a React Hook that lets you add a label to a custom Hook in React DevTools.

Call useDebugValue at the top level of your custom Hook to display a readable debug value:

See more examples below.

useDebugValue does not return anything.

Call useDebugValue at the top level of your custom Hook to display a readable debug value for React DevTools.

This gives components calling useOnlineStatus a label like OnlineStatus: "Online" when you inspect them:

Without the useDebugValue call, only the underlying data (in this example, true) would be displayed.

Don’t add debug values to every custom Hook. It’s most valuable for custom Hooks that are part of shared libraries and that have a complex internal data structure that’s difficult to inspect.

You can also pass a formatting function as the second argument to useDebugValue:

Your formatting function will receive the debug value as a parameter and should return a formatted display value. When your component is inspected, React DevTools will call this function and display its result.

This lets you avoid running potentially expensive formatting logic unless the component is actually inspected. For example, if date is a Date value, this avoids calling toDateString() on it for every render.

**Examples**:

```text
useDebugValue(value, format?)
```

```python
import { useDebugValue } from 'react';function useOnlineStatus() {  // ...  useDebugValue(isOnline ? 'Online' : 'Offline');  // ...}
```

```python
import { useDebugValue } from 'react';function useOnlineStatus() {  // ...  useDebugValue(isOnline ? 'Online' : 'Offline');  // ...}
```

---

## useDeferredValue – React

**URL**: https://react.dev/reference/react/useDeferredValue

**Contents**:
- useDeferredValue
- Reference
  - useDeferredValue(value, initialValue?)
    - Parameters
    - Returns
    - Caveats
- Usage
  - Showing stale content while fresh content is loading

useDeferredValue is a React Hook that lets you defer updating a part of the UI.

Call useDeferredValue at the top level of your component to get a deferred version of that value.

See more examples below.

When an update is inside a Transition, useDeferredValue always returns the new value and does not spawn a deferred render, since the update is already deferred.

The values you pass to useDeferredValue should either be primitive values (like strings and numbers) or objects created outside of rendering. If you create a new object during rendering and immediately pass it to useDeferredValue, it will be different on every render, causing unnecessary background re-renders.

When useDeferredValue receives a different value (compared with Object.is), in addition to the current render (when it still uses the previous value), it schedules a re-render in the background with the new value. The background re-render is interruptible: if there’s another update to the value, React will restart the background re-render from scratch. For example, if the user is typing into an input faster than a chart receiving its deferred value can re-render, the chart will only re-render after the user stops typing.

useDeferredValue is integrated with <Suspense>. If the background update caused by a new value suspends the UI, the user will not see the fallback. They will see the old deferred value until the data loads.

useDeferredValue does not by itself prevent extra network requests.

There is no fixed delay caused by useDeferredValue itself. As soon as React finishes the original re-render, React will immediately start working on the background re-render with the new deferred value. Any updates caused by events (like typing) will interrupt the background re-render and get prioritized over it.

The background re-render caused by useDeferredValue does not fire Effects until it’s committed to the screen. If the background re-render suspends, its Effects will run after the data loads and the 

*[Content truncated - see full docs]*

**Examples**:

```javascript
const deferredValue = useDeferredValue(value)
```

```python
import { useState, useDeferredValue } from 'react';function SearchPage() {  const [query, setQuery] = useState('');  const deferredQuery = useDeferredValue(query);  // ...}
```

```python
import { useState, useDeferredValue } from 'react';function SearchPage() {  const [query, setQuery] = useState('');  const deferredQuery = useDeferredValue(query);  // ...}
```

---

## useEffect – React

**URL**: https://react.dev/reference/react/useEffect

**Contents**:
- useEffect
- Reference
  - useEffect(setup, dependencies?)
    - Parameters
    - Returns
    - Caveats
- Usage
  - Connecting to an external system

useEffect is a React Hook that lets you synchronize a component with an external system.

Call useEffect at the top level of your component to declare an Effect:

See more examples below.

setup: The function with your Effect’s logic. Your setup function may also optionally return a cleanup function. When your component is added to the DOM, React will run your setup function. After every re-render with changed dependencies, React will first run the cleanup function (if you provided it) with the old values, and then run your setup function with the new values. After your component is removed from the DOM, React will run your cleanup function.

optional dependencies: The list of all reactive values referenced inside of the setup code. Reactive values include props, state, and all the variables and functions declared directly inside your component body. If your linter is configured for React, it will verify that every reactive value is correctly specified as a dependency. The list of dependencies must have a constant number of items and be written inline like [dep1, dep2, dep3]. React will compare each dependency with its previous value using the Object.is comparison. If you omit this argument, your Effect will re-run after every re-render of the component. See the difference between passing an array of dependencies, an empty array, and no dependencies at all.

useEffect returns undefined.

useEffect is a Hook, so you can only call it at the top level of your component or your own Hooks. You can’t call it inside loops or conditions. If you need that, extract a new component and move the state into it.

If you’re not trying to synchronize with some external system, you probably don’t need an Effect.

When Strict Mode is on, React will run one extra development-only setup+cleanup cycle before the first real setup. This is a stress-test that ensures that your cleanup logic “mirrors” your setup logic and that it stops or undoes whatever the setup is doing. If this causes a

*[Content truncated - see full docs]*

**Examples**:

```text
useEffect(setup, dependencies?)
```

```python
import { useState, useEffect } from 'react';import { createConnection } from './chat.js';function ChatRoom({ roomId }) {  const [serverUrl, setServerUrl] = useState('https://localhost:1234');  useEffect(() => {    const connection = createConnection(serverUrl, roomId);    connection.connect();    return () => {      connection.disconnect();    };  }, [serverUrl, roomId]);  // ...}
```

```python
import { useState, useEffect } from 'react';import { createConnection } from './chat.js';function ChatRoom({ roomId }) {  const [serverUrl, setServerUrl] = useState('https://localhost:1234');  useEffect(() => {  	const connection = createConnection(serverUrl, roomId);    connection.connect();  	return () => {      connection.disconnect();  	};  }, [serverUrl, roomId]);  // ...}
```

---

## useFormStatus – React

**URL**: https://react.dev/reference/react-dom/hooks/useFormStatus

**Contents**:
- useFormStatus
- Reference
  - useFormStatus()
    - Parameters
    - Returns
    - Caveats
- Usage
  - Display a pending state during form submission

useFormStatus is a Hook that gives you status information of the last form submission.

The useFormStatus Hook provides status information of the last form submission.

To get status information, the Submit component must be rendered within a <form>. The Hook returns information like the pending property which tells you if the form is actively submitting.

In the above example, Submit uses this information to disable <button> presses while the form is submitting.

See more examples below.

useFormStatus does not take any parameters.

A status object with the following properties:

pending: A boolean. If true, this means the parent <form> is pending submission. Otherwise, false.

data: An object implementing the FormData interface that contains the data the parent <form> is submitting. If there is no active submission or no parent <form>, it will be null.

method: A string value of either 'get' or 'post'. This represents whether the parent <form> is submitting with either a GET or POST HTTP method. By default, a <form> will use the GET method and can be specified by the method property.

To display a pending state while a form is submitting, you can call the useFormStatus Hook in a component rendered in a <form> and read the pending property returned.

Here, we use the pending property to indicate the form is submitting.

The useFormStatus Hook only returns status information for a parent <form> and not for any <form> rendered in the same component calling the Hook, or child components.

Instead call useFormStatus from inside a component that is located inside <form>.

You can use the data property of the status information returned from useFormStatus to display what data is being submitted by the user.

Here, we have a form where users can request a username. We can use useFormStatus to display a temporary status message confirming what username they have requested.

useFormStatus will only return status information for a parent <form>.

If the component that calls 

*[Content truncated - see full docs]*

**Examples**:

```javascript
const { pending, data, method, action } = useFormStatus();
```

```python
import { useFormStatus } from "react-dom";import action from './actions';function Submit() {  const status = useFormStatus();  return <button disabled={status.pending}>Submit</button>}export default function App() {  return (    <form action={action}>      <Submit />    </form>  );}
```

```javascript
function Form() {  // 🚩 `pending` will never be true  // useFormStatus does not track the form rendered in this component  const { pending } = useFormStatus();  return <form action={submit}></form>;}
```

---

## useId – React

**URL**: https://react.dev/reference/react/useId

**Contents**:
- useId
- Reference
  - useId()
    - Parameters
    - Returns
    - Caveats
- Usage
  - Pitfall

useId is a React Hook for generating unique IDs that can be passed to accessibility attributes.

Call useId at the top level of your component to generate a unique ID:

See more examples below.

useId does not take any parameters.

useId returns a unique ID string associated with this particular useId call in this particular component.

useId is a Hook, so you can only call it at the top level of your component or your own Hooks. You can’t call it inside loops or conditions. If you need that, extract a new component and move the state into it.

useId should not be used to generate keys in a list. Keys should be generated from your data.

useId currently cannot be used in async Server Components.

Do not call useId to generate keys in a list. Keys should be generated from your data.

Call useId at the top level of your component to generate a unique ID:

You can then pass the generated ID to different attributes:

Let’s walk through an example to see when this is useful.

HTML accessibility attributes like aria-describedby let you specify that two tags are related to each other. For example, you can specify that an element (like an input) is described by another element (like a paragraph).

In regular HTML, you would write it like this:

However, hardcoding IDs like this is not a good practice in React. A component may be rendered more than once on the page—but IDs have to be unique! Instead of hardcoding an ID, generate a unique ID with useId:

Now, even if PasswordField appears multiple times on the screen, the generated IDs won’t clash.

Watch this video to see the difference in the user experience with assistive technologies.

With server rendering, useId requires an identical component tree on the server and the client. If the trees you render on the server and the client don’t match exactly, the generated IDs won’t match.

You might be wondering why useId is better than incrementing a global variable like nextId++.

The primary benefit of useId is that React en

*[Content truncated - see full docs]*

**Examples**:

```javascript
const id = useId()
```

```python
import { useId } from 'react';function PasswordField() {  const passwordHintId = useId();  // ...
```

```python
import { useId } from 'react';function PasswordField() {  const passwordHintId = useId();  // ...
```

---

## useImperativeHandle – React

**URL**: https://react.dev/reference/react/useImperativeHandle

**Contents**:
- useImperativeHandle
- Reference
  - useImperativeHandle(ref, createHandle, dependencies?)
    - Parameters
  - Note
    - Returns
- Usage
  - Exposing a custom ref handle to the parent component

useImperativeHandle is a React Hook that lets you customize the handle exposed as a ref.

Call useImperativeHandle at the top level of your component to customize the ref handle it exposes:

See more examples below.

ref: The ref you received as a prop to the MyInput component.

createHandle: A function that takes no arguments and returns the ref handle you want to expose. That ref handle can have any type. Usually, you will return an object with the methods you want to expose.

optional dependencies: The list of all reactive values referenced inside of the createHandle code. Reactive values include props, state, and all the variables and functions declared directly inside your component body. If your linter is configured for React, it will verify that every reactive value is correctly specified as a dependency. The list of dependencies must have a constant number of items and be written inline like [dep1, dep2, dep3]. React will compare each dependency with its previous value using the Object.is comparison. If a re-render resulted in a change to some dependency, or if you omitted this argument, your createHandle function will re-execute, and the newly created handle will be assigned to the ref.

Starting with React 19, ref is available as a prop. In React 18 and earlier, it was necessary to get the ref from forwardRef.

useImperativeHandle returns undefined.

To expose a DOM node to the parent element, pass in the ref prop to the node.

With the code above, a ref to MyInput will receive the <input> DOM node. However, you can expose a custom value instead. To customize the exposed handle, call useImperativeHandle at the top level of your component:

Note that in the code above, the ref is no longer passed to the <input>.

For example, suppose you don’t want to expose the entire <input> DOM node, but you want to expose two of its methods: focus and scrollIntoView. To do this, keep the real browser DOM in a separate ref. Then use useImperativeHandle to expose a handle

*[Content truncated - see full docs]*

**Examples**:

```text
useImperativeHandle(ref, createHandle, dependencies?)
```

```python
import { useImperativeHandle } from 'react';function MyInput({ ref }) {  useImperativeHandle(ref, () => {    return {      // ... your methods ...    };  }, []);  // ...
```

```javascript
function MyInput({ ref }) {  return <input ref={ref} />;};
```

---

## useInsertionEffect – React

**URL**: https://react.dev/reference/react/useInsertionEffect

**Contents**:
- useInsertionEffect
  - Pitfall
- Reference
  - useInsertionEffect(setup, dependencies?)
    - Parameters
    - Returns
    - Caveats
- Usage

useInsertionEffect is for CSS-in-JS library authors. Unless you are working on a CSS-in-JS library and need a place to inject the styles, you probably want useEffect or useLayoutEffect instead.

useInsertionEffect allows inserting elements into the DOM before any layout Effects fire.

Call useInsertionEffect to insert styles before any Effects fire that may need to read layout:

See more examples below.

setup: The function with your Effect’s logic. Your setup function may also optionally return a cleanup function. When your component is added to the DOM, but before any layout Effects fire, React will run your setup function. After every re-render with changed dependencies, React will first run the cleanup function (if you provided it) with the old values, and then run your setup function with the new values. When your component is removed from the DOM, React will run your cleanup function.

optional dependencies: The list of all reactive values referenced inside of the setup code. Reactive values include props, state, and all the variables and functions declared directly inside your component body. If your linter is configured for React, it will verify that every reactive value is correctly specified as a dependency. The list of dependencies must have a constant number of items and be written inline like [dep1, dep2, dep3]. React will compare each dependency with its previous value using the Object.is comparison algorithm. If you don’t specify the dependencies at all, your Effect will re-run after every re-render of the component.

useInsertionEffect returns undefined.

Traditionally, you would style React components using plain CSS.

Some teams prefer to author styles directly in JavaScript code instead of writing CSS files. This usually requires using a CSS-in-JS library or a tool. There are three common approaches to CSS-in-JS:

If you use CSS-in-JS, we recommend a combination of the first two approaches (CSS files for static styles, inline styles for dynamic st

*[Content truncated - see full docs]*

**Examples**:

```text
useInsertionEffect(setup, dependencies?)
```

```python
import { useInsertionEffect } from 'react';// Inside your CSS-in-JS libraryfunction useCSS(rule) {  useInsertionEffect(() => {    // ... inject <style> tags here ...  });  return rule;}
```

```text
// In your JS file:<button className="success" />// In your CSS file:.success { color: green; }
```

---

## useLayoutEffect – React

**URL**: https://react.dev/reference/react/useLayoutEffect

**Contents**:
- useLayoutEffect
  - Pitfall
- Reference
  - useLayoutEffect(setup, dependencies?)
    - Parameters
    - Returns
    - Caveats
- Usage

useLayoutEffect can hurt performance. Prefer useEffect when possible.

useLayoutEffect is a version of useEffect that fires before the browser repaints the screen.

Call useLayoutEffect to perform the layout measurements before the browser repaints the screen:

See more examples below.

setup: The function with your Effect’s logic. Your setup function may also optionally return a cleanup function. Before your component is added to the DOM, React will run your setup function. After every re-render with changed dependencies, React will first run the cleanup function (if you provided it) with the old values, and then run your setup function with the new values. Before your component is removed from the DOM, React will run your cleanup function.

optional dependencies: The list of all reactive values referenced inside of the setup code. Reactive values include props, state, and all the variables and functions declared directly inside your component body. If your linter is configured for React, it will verify that every reactive value is correctly specified as a dependency. The list of dependencies must have a constant number of items and be written inline like [dep1, dep2, dep3]. React will compare each dependency with its previous value using the Object.is comparison. If you omit this argument, your Effect will re-run after every re-render of the component.

useLayoutEffect returns undefined.

useLayoutEffect is a Hook, so you can only call it at the top level of your component or your own Hooks. You can’t call it inside loops or conditions. If you need that, extract a component and move the Effect there.

When Strict Mode is on, React will run one extra development-only setup+cleanup cycle before the first real setup. This is a stress-test that ensures that your cleanup logic “mirrors” your setup logic and that it stops or undoes whatever the setup is doing. If this causes a problem, implement the cleanup function.

If some of your dependencies are objects or function

*[Content truncated - see full docs]*

**Examples**:

```text
useLayoutEffect(setup, dependencies?)
```

```python
import { useState, useRef, useLayoutEffect } from 'react';function Tooltip() {  const ref = useRef(null);  const [tooltipHeight, setTooltipHeight] = useState(0);  useLayoutEffect(() => {    const { height } = ref.current.getBoundingClientRect();    setTooltipHeight(height);  }, []);  // ...
```

```javascript
function Tooltip() {  const ref = useRef(null);  const [tooltipHeight, setTooltipHeight] = useState(0); // You don't know real height yet  useLayoutEffect(() => {    const { height } = ref.current.getBoundingClientRect();    setTooltipHeight(height); // Re-render now that you know the real height  }, []);  // ...use tooltipHeight in the rendering logic below...}
```

---

## useMemo – React

**URL**: https://react.dev/reference/react/useMemo

**Contents**:
- useMemo
  - Note
- Reference
  - useMemo(calculateValue, dependencies)
    - Parameters
    - Returns
    - Caveats
  - Note

useMemo is a React Hook that lets you cache the result of a calculation between re-renders.

React Compiler automatically memoizes values and functions, reducing the need for manual useMemo calls. You can use the compiler to handle memoization automatically.

Call useMemo at the top level of your component to cache a calculation between re-renders:

See more examples below.

calculateValue: The function calculating the value that you want to cache. It should be pure, should take no arguments, and should return a value of any type. React will call your function during the initial render. On next renders, React will return the same value again if the dependencies have not changed since the last render. Otherwise, it will call calculateValue, return its result, and store it so it can be reused later.

dependencies: The list of all reactive values referenced inside of the calculateValue code. Reactive values include props, state, and all the variables and functions declared directly inside your component body. If your linter is configured for React, it will verify that every reactive value is correctly specified as a dependency. The list of dependencies must have a constant number of items and be written inline like [dep1, dep2, dep3]. React will compare each dependency with its previous value using the Object.is comparison.

On the initial render, useMemo returns the result of calling calculateValue with no arguments.

During next renders, it will either return an already stored value from the last render (if the dependencies haven’t changed), or call calculateValue again, and return the result that calculateValue has returned.

Caching return values like this is also known as memoization, which is why this Hook is called useMemo.

To cache a calculation between re-renders, wrap it in a useMemo call at the top level of your component:

You need to pass two things to useMemo:

On the initial render, the value you’ll get from useMemo will be the result of calling your ca

*[Content truncated - see full docs]*

**Examples**:

```javascript
const cachedValue = useMemo(calculateValue, dependencies)
```

```python
import { useMemo } from 'react';function TodoList({ todos, tab }) {  const visibleTodos = useMemo(    () => filterTodos(todos, tab),    [todos, tab]  );  // ...}
```

```python
import { useMemo } from 'react';function TodoList({ todos, tab, theme }) {  const visibleTodos = useMemo(() => filterTodos(todos, tab), [todos, tab]);  // ...}
```

---

## useOptimistic – React

**URL**: https://react.dev/reference/react/useOptimistic

**Contents**:
- useOptimistic
- Reference
  - useOptimistic(state, updateFn)
    - Parameters
    - Returns
- Usage
  - Optimistically updating forms

useOptimistic is a React Hook that lets you optimistically update the UI.

useOptimistic is a React Hook that lets you show a different state while an async action is underway. It accepts some state as an argument and returns a copy of that state that can be different during the duration of an async action such as a network request. You provide a function that takes the current state and the input to the action, and returns the optimistic state to be used while the action is pending.

This state is called the “optimistic” state because it is usually used to immediately present the user with the result of performing an action, even though the action actually takes time to complete.

See more examples below.

The useOptimistic Hook provides a way to optimistically update the user interface before a background operation, like a network request, completes. In the context of forms, this technique helps to make apps feel more responsive. When a user submits a form, instead of waiting for the server’s response to reflect the changes, the interface is immediately updated with the expected outcome.

For example, when a user types a message into the form and hits the “Send” button, the useOptimistic Hook allows the message to immediately appear in the list with a “Sending…” label, even before the message is actually sent to a server. This “optimistic” approach gives the impression of speed and responsiveness. The form then attempts to truly send the message in the background. Once the server confirms the message has been received, the “Sending…” label is removed.

**Examples**:

```javascript
const [optimisticState, addOptimistic] = useOptimistic(state, updateFn);
```

```python
import { useOptimistic } from 'react';function AppContainer() {  const [optimisticState, addOptimistic] = useOptimistic(    state,    // updateFn    (currentState, optimisticValue) => {      // merge and return new state      // with optimistic value    }  );}
```

---

## useReducer – React

**URL**: https://react.dev/reference/react/useReducer

**Contents**:
- useReducer
- Reference
  - useReducer(reducer, initialArg, init?)
    - Parameters
    - Returns
    - Caveats
  - dispatch function
    - Parameters

useReducer is a React Hook that lets you add a reducer to your component.

Call useReducer at the top level of your component to manage its state with a reducer.

See more examples below.

useReducer returns an array with exactly two values:

The dispatch function returned by useReducer lets you update the state to a different value and trigger a re-render. You need to pass the action as the only argument to the dispatch function:

React will set the next state to the result of calling the reducer function you’ve provided with the current state and the action you’ve passed to dispatch.

dispatch functions do not have a return value.

The dispatch function only updates the state variable for the next render. If you read the state variable after calling the dispatch function, you will still get the old value that was on the screen before your call.

If the new value you provide is identical to the current state, as determined by an Object.is comparison, React will skip re-rendering the component and its children. This is an optimization. React may still need to call your component before ignoring the result, but it shouldn’t affect your code.

React batches state updates. It updates the screen after all the event handlers have run and have called their set functions. This prevents multiple re-renders during a single event. In the rare case that you need to force React to update the screen earlier, for example to access the DOM, you can use flushSync.

Call useReducer at the top level of your component to manage state with a reducer.

useReducer returns an array with exactly two items:

To update what’s on the screen, call dispatch with an object representing what the user did, called an action:

React will pass the current state and the action to your reducer function. Your reducer will calculate and return the next state. React will store that next state, render your component with it, and update the UI.

useReducer is very similar to useState, but it lets you move t

*[Content truncated - see full docs]*

**Examples**:

```javascript
const [state, dispatch] = useReducer(reducer, initialArg, init?)
```

```python
import { useReducer } from 'react';function reducer(state, action) {  // ...}function MyComponent() {  const [state, dispatch] = useReducer(reducer, { age: 42 });  // ...
```

```javascript
const [state, dispatch] = useReducer(reducer, { age: 42 });function handleClick() {  dispatch({ type: 'incremented_age' });  // ...
```

---

## useRef – React

**URL**: https://react.dev/reference/react/useRef

**Contents**:
- useRef
- Reference
  - useRef(initialValue)
    - Parameters
    - Returns
    - Caveats
- Usage
  - Referencing a value with a ref

useRef is a React Hook that lets you reference a value that’s not needed for rendering.

Call useRef at the top level of your component to declare a ref.

See more examples below.

useRef returns an object with a single property:

On the next renders, useRef will return the same object.

Call useRef at the top level of your component to declare one or more refs.

useRef returns a ref object with a single current property initially set to the initial value you provided.

On the next renders, useRef will return the same object. You can change its current property to store information and read it later. This might remind you of state, but there is an important difference.

Changing a ref does not trigger a re-render. This means refs are perfect for storing information that doesn’t affect the visual output of your component. For example, if you need to store an interval ID and retrieve it later, you can put it in a ref. To update the value inside the ref, you need to manually change its current property:

Later, you can read that interval ID from the ref so that you can call clear that interval:

By using a ref, you ensure that:

Changing a ref does not trigger a re-render, so refs are not appropriate for storing information you want to display on the screen. Use state for that instead. Read more about choosing between useRef and useState.

This component uses a ref to keep track of how many times the button was clicked. Note that it’s okay to use a ref instead of state here because the click count is only read and written in an event handler.

If you show {ref.current} in the JSX, the number won’t update on click. This is because setting ref.current does not trigger a re-render. Information that’s used for rendering should be state instead.

Do not write or read ref.current during rendering.

React expects that the body of your component behaves like a pure function:

Reading or writing a ref during rendering breaks these expectations.

You can read or write refs from 

*[Content truncated - see full docs]*

**Examples**:

```javascript
const ref = useRef(initialValue)
```

```python
import { useRef } from 'react';function MyComponent() {  const intervalRef = useRef(0);  const inputRef = useRef(null);  // ...
```

```python
import { useRef } from 'react';function Stopwatch() {  const intervalRef = useRef(0);  // ...
```

---

## useState – React

**URL**: https://react.dev/reference/react/useState

**Contents**:
- useState
- Reference
  - useState(initialState)
    - Parameters
    - Returns
    - Caveats
  - set functions, like setSomething(nextState)
    - Parameters

useState is a React Hook that lets you add a state variable to your component.

Call useState at the top level of your component to declare a state variable.

The convention is to name state variables like [something, setSomething] using array destructuring.

See more examples below.

useState returns an array with exactly two values:

The set function returned by useState lets you update the state to a different value and trigger a re-render. You can pass the next state directly, or a function that calculates it from the previous state:

set functions do not have a return value.

The set function only updates the state variable for the next render. If you read the state variable after calling the set function, you will still get the old value that was on the screen before your call.

If the new value you provide is identical to the current state, as determined by an Object.is comparison, React will skip re-rendering the component and its children. This is an optimization. Although in some cases React may still need to call your component before skipping the children, it shouldn’t affect your code.

React batches state updates. It updates the screen after all the event handlers have run and have called their set functions. This prevents multiple re-renders during a single event. In the rare case that you need to force React to update the screen earlier, for example to access the DOM, you can use flushSync.

The set function has a stable identity, so you will often see it omitted from Effect dependencies, but including it will not cause the Effect to fire. If the linter lets you omit a dependency without errors, it is safe to do. Learn more about removing Effect dependencies.

Calling the set function during rendering is only allowed from within the currently rendering component. React will discard its output and immediately attempt to render it again with the new state. This pattern is rarely needed, but you can use it to store information from the previous renders.

*[Content truncated - see full docs]*

**Examples**:

```javascript
const [state, setState] = useState(initialState)
```

```python
import { useState } from 'react';function MyComponent() {  const [age, setAge] = useState(28);  const [name, setName] = useState('Taylor');  const [todos, setTodos] = useState(() => createTodos());  // ...
```

```javascript
const [name, setName] = useState('Edward');function handleClick() {  setName('Taylor');  setAge(a => a + 1);  // ...
```

---

## useSyncExternalStore – React

**URL**: https://react.dev/reference/react/useSyncExternalStore

**Contents**:
- useSyncExternalStore
- Reference
  - useSyncExternalStore(subscribe, getSnapshot, getServerSnapshot?)
    - Parameters
    - Returns
    - Caveats
- Usage
  - Subscribing to an external store

useSyncExternalStore is a React Hook that lets you subscribe to an external store.

Call useSyncExternalStore at the top level of your component to read a value from an external data store.

It returns the snapshot of the data in the store. You need to pass two functions as arguments:

See more examples below.

subscribe: A function that takes a single callback argument and subscribes it to the store. When the store changes, it should invoke the provided callback, which will cause React to re-call getSnapshot and (if needed) re-render the component. The subscribe function should return a function that cleans up the subscription.

getSnapshot: A function that returns a snapshot of the data in the store that’s needed by the component. While the store has not changed, repeated calls to getSnapshot must return the same value. If the store changes and the returned value is different (as compared by Object.is), React re-renders the component.

optional getServerSnapshot: A function that returns the initial snapshot of the data in the store. It will be used only during server rendering and during hydration of server-rendered content on the client. The server snapshot must be the same between the client and the server, and is usually serialized and passed from the server to the client. If you omit this argument, rendering the component on the server will throw an error.

The current snapshot of the store which you can use in your rendering logic.

The store snapshot returned by getSnapshot must be immutable. If the underlying store has mutable data, return a new immutable snapshot if the data has changed. Otherwise, return a cached last snapshot.

If a different subscribe function is passed during a re-render, React will re-subscribe to the store using the newly passed subscribe function. You can prevent this by declaring subscribe outside the component.

If the store is mutated during a non-blocking Transition update, React will fall back to performing that update as block

*[Content truncated - see full docs]*

**Examples**:

```javascript
const snapshot = useSyncExternalStore(subscribe, getSnapshot, getServerSnapshot?)
```

```python
import { useSyncExternalStore } from 'react';import { todosStore } from './todoStore.js';function TodosApp() {  const todos = useSyncExternalStore(todosStore.subscribe, todosStore.getSnapshot);  // ...}
```

```javascript
const LazyProductDetailPage = lazy(() => import('./ProductDetailPage.js'));function ShoppingApp() {  const selectedProductId = useSyncExternalStore(...);  // ❌ Calling `use` with a Promise dependent on `selectedProductId`  const data = use(fetchItem(selectedProductId))  // ❌ Conditionally rendering a lazy component based on `selectedProductId`  return selectedProductId != null ? <LazyProductDetailPage /> : <FeaturedProducts />;}
```

---

## useTransition – React

**URL**: https://react.dev/reference/react/useTransition

**Contents**:
- useTransition
- Reference
  - useTransition()
    - Parameters
    - Returns
  - startTransition(action)
  - Note
    - Functions called in startTransition are called “Actions”.

useTransition is a React Hook that lets you render a part of the UI in the background.

Call useTransition at the top level of your component to mark some state updates as Transitions.

See more examples below.

useTransition does not take any parameters.

useTransition returns an array with exactly two items:

The startTransition function returned by useTransition lets you mark an update as a Transition.

The function passed to startTransition is called an “Action”. By convention, any callback called inside startTransition (such as a callback prop) should be named action or include the “Action” suffix:

startTransition does not return anything.

useTransition is a Hook, so it can only be called inside components or custom Hooks. If you need to start a Transition somewhere else (for example, from a data library), call the standalone startTransition instead.

You can wrap an update into a Transition only if you have access to the set function of that state. If you want to start a Transition in response to some prop or a custom Hook value, try useDeferredValue instead.

The function you pass to startTransition is called immediately, marking all state updates that happen while it executes as Transitions. If you try to perform state updates in a setTimeout, for example, they won’t be marked as Transitions.

You must wrap any state updates after any async requests in another startTransition to mark them as Transitions. This is a known limitation that we will fix in the future (see Troubleshooting).

The startTransition function has a stable identity, so you will often see it omitted from Effect dependencies, but including it will not cause the Effect to fire. If the linter lets you omit a dependency without errors, it is safe to do. Learn more about removing Effect dependencies.

A state update marked as a Transition will be interrupted by other state updates. For example, if you update a chart component inside a Transition, but then start typing into an input while the 

*[Content truncated - see full docs]*

**Examples**:

```javascript
const [isPending, startTransition] = useTransition()
```

```python
import { useTransition } from 'react';function TabContainer() {  const [isPending, startTransition] = useTransition();  // ...}
```

```javascript
function TabContainer() {  const [isPending, startTransition] = useTransition();  const [tab, setTab] = useState('about');  function selectTab(nextTab) {    startTransition(() => {      setTab(nextTab);    });  }  // ...}
```

---

## use – React

**URL**: https://react.dev/reference/react/use

**Contents**:
- use
- Reference
  - use(resource)
    - Parameters
    - Returns
    - Caveats
- Usage
  - Reading context with use

use is a React API that lets you read the value of a resource like a Promise or context.

Call use in your component to read the value of a resource like a Promise or context.

Unlike React Hooks, use can be called within loops and conditional statements like if. Like React Hooks, the function that calls use must be a Component or Hook.

When called with a Promise, the use API integrates with Suspense and Error Boundaries. The component calling use suspends while the Promise passed to use is pending. If the component that calls use is wrapped in a Suspense boundary, the fallback will be displayed. Once the Promise is resolved, the Suspense fallback is replaced by the rendered components using the data returned by the use API. If the Promise passed to use is rejected, the fallback of the nearest Error Boundary will be displayed.

See more examples below.

The use API returns the value that was read from the resource like the resolved value of a Promise or context.

When a context is passed to use, it works similarly to useContext. While useContext must be called at the top level of your component, use can be called inside conditionals like if and loops like for. use is preferred over useContext because it is more flexible.

use returns the context value for the context you passed. To determine the context value, React searches the component tree and finds the closest context provider above for that particular context.

To pass context to a Button, wrap it or one of its parent components into the corresponding context provider.

It doesn’t matter how many layers of components there are between the provider and the Button. When a Button anywhere inside of Form calls use(ThemeContext), it will receive "dark" as the value.

Unlike useContext, use can be called in conditionals and loops like if.

use is called from inside a if statement, allowing you to conditionally read values from a Context.

Like useContext, use(context) always looks for the closest context provider a

*[Content truncated - see full docs]*

**Examples**:

```javascript
const value = use(resource);
```

```python
import { use } from 'react';function MessageComponent({ messagePromise }) {  const message = use(messagePromise);  const theme = use(ThemeContext);  // ...
```

```python
import { use } from 'react';function Button() {  const theme = use(ThemeContext);  // ...
```

---

## 'use client' directive – React

**URL**: https://react.dev/reference/rsc/use-client

**Contents**:
- 'use client'
  - React Server Components
- Reference
  - 'use client'
    - Caveats
  - How 'use client' marks client code
      - Deep Dive
    - How is FancyText both a Server and a Client Component?

'use client' is for use with React Server Components.

'use client' lets you mark what code runs on the client.

Add 'use client' at the top of a file to mark the module and its transitive dependencies as client code.

When a file marked with 'use client' is imported from a Server Component, compatible bundlers will treat the module import as a boundary between server-run and client-run code.

As dependencies of RichTextEditor, formatDate and Button will also be evaluated on the client regardless of whether their modules contain a 'use client' directive. Note that a single module may be evaluated on the server when imported from server code and on the client when imported from client code.

In a React app, components are often split into separate files, or modules.

For apps that use React Server Components, the app is server-rendered by default. 'use client' introduces a server-client boundary in the module dependency tree, effectively creating a subtree of Client modules.

To better illustrate this, consider the following React Server Components app.

In the module dependency tree of this example app, the 'use client' directive in InspirationGenerator.js marks that module and all of its transitive dependencies as Client modules. The subtree starting at InspirationGenerator.js is now marked as Client modules.

'use client' segments the module dependency tree of the React Server Components app, marking InspirationGenerator.js and all of its dependencies as client-rendered.

During render, the framework will server-render the root component and continue through the render tree, opting-out of evaluating any code imported from client-marked code.

The server-rendered portion of the render tree is then sent to the client. The client, with its client code downloaded, then completes rendering the rest of the tree.

The render tree for the React Server Components app. InspirationGenerator and its child component FancyText are components exported from client-marked code and

*[Content truncated - see full docs]*

**Examples**:

```python
'use client';import { useState } from 'react';import { formatDate } from './formatters';import Button from './button';export default function RichTextEditor({ timestamp, text }) {  const date = formatDate(timestamp);  // ...  const editButton = <Button />;  // ...}
```

```javascript
// This is a definition of a componentfunction MyComponent() {  return <p>My Component</p>}
```

```python
import MyComponent from './MyComponent';function App() {  // This is a usage of a component  return <MyComponent />;}
```

---

## 'use memo' directive – React

**URL**: https://react.dev/reference/react-compiler/directives/use-memo

**Contents**:
- use memo
  - Note
- Reference
  - "use memo"
    - Caveats
  - How "use memo" marks functions for optimization
  - When to use "use memo"
    - You’re using annotation mode

"use memo" marks a function for React Compiler optimization.

In most cases, you don’t need "use memo". It’s primarily needed in annotation mode where you must explicitly mark functions for optimization. In infer mode, the compiler automatically detects components and hooks by their naming patterns (PascalCase for components, use prefix for hooks). If a component or hook isn’t being compiled in infer mode, you should fix its naming convention rather than forcing compilation with "use memo".

Add "use memo" at the beginning of a function to mark it for React Compiler optimization.

When a function contains "use memo", the React Compiler will analyze and optimize it during build time. The compiler will automatically memoize values and components to prevent unnecessary re-computations and re-renders.

In a React app that uses the React Compiler, functions are analyzed at build time to determine if they can be optimized. By default, the compiler automatically infers which components to memoize, but this can depend on your compilationMode setting if you’ve set it.

"use memo" explicitly marks a function for optimization, overriding the default behavior:

The directive creates a clear boundary in your codebase between optimized and non-optimized code, giving you fine-grained control over the compilation process.

You should consider using "use memo" when:

In compilationMode: 'annotation', the directive is required for any function you want optimized:

Start with annotation mode and selectively optimize stable components:

The behavior of "use memo" changes based on your compiler configuration:

In infer mode, the compiler automatically detects components and hooks by their naming patterns (PascalCase for components, use prefix for hooks). If a component or hook isn’t being compiled in infer mode, you should fix its naming convention rather than forcing compilation with "use memo".

To confirm your component is being optimized:

**Examples**:

```javascript
function MyComponent() {  "use memo";  // ...}
```

```javascript
// ✅ This component will be optimizedfunction OptimizedList() {  "use memo";  // ...}// ❌ This component won't be optimizedfunction SimpleWrapper() {  // ...}
```

```javascript
// Start by optimizing leaf componentsfunction Button({ onClick, children }) {  "use memo";  // ...}// Gradually move up the tree as you verify behaviorfunction ButtonGroup({ buttons }) {  "use memo";  // ...}
```

---

## 'use no memo' directive – React

**URL**: https://react.dev/reference/react-compiler/directives/use-no-memo

**Contents**:
- use no memo
- Reference
  - "use no memo"
    - Caveats
  - How "use no memo" opts-out of optimization
  - When to use "use no memo"
    - Debugging compiler issues
    - Third-party library integration

"use no memo" prevents a function from being optimized by React Compiler.

Add "use no memo" at the beginning of a function to prevent React Compiler optimization.

When a function contains "use no memo", the React Compiler will skip it entirely during optimization. This is useful as a temporary escape hatch when debugging or when dealing with code that doesn’t work correctly with the compiler.

React Compiler analyzes your code at build time to apply optimizations. "use no memo" creates an explicit boundary that tells the compiler to skip a function entirely.

This directive takes precedence over all other settings:

The compiler treats these functions as if the React Compiler wasn’t enabled, leaving them exactly as written.

"use no memo" should be used sparingly and temporarily. Common scenarios include:

When you suspect the compiler is causing issues, temporarily disable optimization to isolate the problem:

When integrating with libraries that might not be compatible with the compiler:

The "use no memo" directive is placed at the beginning of a function body to prevent React Compiler from optimizing that function:

The directive can also be placed at the top of a file to affect all functions in that module:

"use no memo" at the function level overrides the module level directive.

If "use no memo" isn’t working:

Always document why you’re disabling optimization:

**Examples**:

```javascript
function MyComponent() {  "use no memo";  // ...}
```

```javascript
function ProblematicComponent({ data }) {  "use no memo"; // TODO: Remove after fixing issue #123  // Rules of React violations that weren't statically detected  // ...}
```

```javascript
function ThirdPartyWrapper() {  "use no memo";  useThirdPartyHook(); // Has side effects that compiler might optimize incorrectly  // ...}
```

---

## 'use server' directive – React

**URL**: https://react.dev/reference/rsc/use-server

**Contents**:
- 'use server'
  - React Server Components
- Reference
  - 'use server'
    - Caveats
  - Security considerations
  - Under Construction
  - Serializable arguments and return values

'use server' is for use with using React Server Components.

'use server' marks server-side functions that can be called from client-side code.

Add 'use server' at the top of an async function body to mark the function as callable by the client. We call these functions Server Functions.

When calling a Server Function on the client, it will make a network request to the server that includes a serialized copy of any arguments passed. If the Server Function returns a value, that value will be serialized and returned to the client.

Instead of individually marking functions with 'use server', you can add the directive to the top of a file to mark all exports within that file as Server Functions that can be used anywhere, including imported in client code.

Arguments to Server Functions are fully client-controlled. For security, always treat them as untrusted input, and make sure to validate and escape arguments as appropriate.

In any Server Function, make sure to validate that the logged-in user is allowed to perform that action.

To prevent sending sensitive data from a Server Function, there are experimental taint APIs to prevent unique values and objects from being passed to client code.

See experimental_taintUniqueValue and experimental_taintObjectReference.

Since client code calls the Server Function over the network, any arguments passed will need to be serializable.

Here are supported types for Server Function arguments:

Notably, these are not supported:

Supported serializable return values are the same as serializable props for a boundary Client Component.

The most common use case of Server Functions will be calling functions that mutate data. On the browser, the HTML form element is the traditional approach for a user to submit a mutation. With React Server Components, React introduces first-class support for Server Functions as Actions in forms.

Here is a form that allows a user to request a username.

In this example requestUsername is a Server Func

*[Content truncated - see full docs]*

**Examples**:

```javascript
async function addToCart(data) {  'use server';  // ...}
```

```javascript
// App.jsasync function requestUsername(formData) {  'use server';  const username = formData.get('username');  // ...}export default function App() {  return (    <form action={requestUsername}>      <input type="text" name="username" />      <button type="submit">Request</button>    </form>  );}
```

```javascript
// requestUsername.js'use server';export default async function requestUsername(formData) {  const username = formData.get('username');  if (canRequest(username)) {    // ...    return 'successful';  }  return 'failed';}
```

---
