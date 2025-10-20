# React - Learn

**Pages**: 47

---

## Add React to an Existing Project – React

**URL**: https://react.dev/learn/add-react-to-an-existing-project

**Contents**:
- Add React to an Existing Project
  - Note
- Using React for an entire subroute of your existing website
- Using React for a part of your existing page
  - Step 1: Set up a modular JavaScript environment
  - Note
  - Step 2: Render React components anywhere on the page
- Using React Native in an existing native mobile app

If you want to add some interactivity to your existing project, you don’t have to rewrite it in React. Add React to your existing stack, and render interactive React components anywhere.

You need to install Node.js for local development. Although you can try React online or with a simple HTML page, realistically most JavaScript tooling you’ll want to use for development requires Node.js.

Let’s say you have an existing web app at example.com built with another server technology (like Rails), and you want to implement all routes starting with example.com/some-app/ fully with React.

Here’s how we recommend to set it up:

This ensures the React part of your app can benefit from the best practices baked into those frameworks.

Many React-based frameworks are full-stack and let your React app take advantage of the server. However, you can use the same approach even if you can’t or don’t want to run JavaScript on the server. In that case, serve the HTML/CSS/JS export (next export output for Next.js, default for Gatsby) at /some-app/ instead.

Let’s say you have an existing page built with another technology (either a server one like Rails, or a client one like Backbone), and you want to render interactive React components somewhere on that page. That’s a common way to integrate React—in fact, it’s how most React usage looked at Meta for many years!

You can do this in two steps:

The exact approach depends on your existing page setup, so let’s walk through some details.

A modular JavaScript environment lets you write your React components in individual files, as opposed to writing all of your code in a single file. It also lets you use all the wonderful packages published by other developers on the npm registry—including React itself! How you do this depends on your existing setup:

If your app is already split into files that use import statements, try to use the setup you already have. Check whether writing <div /> in your JS code causes a syntax error. If it causes 

*[Content truncated - see full docs]*

**Examples**:

```python
import { createRoot } from 'react-dom/client';// Clear the existing HTML contentdocument.body.innerHTML = '<div id="app"></div>';// Render your React component insteadconst root = createRoot(document.getElementById('app'));root.render(<h1>Hello, world</h1>);
```

```text
<!-- ... somewhere in your html ... --><nav id="navigation"></nav><!-- ... more html ... -->
```

---

## Adding Interactivity – React

**URL**: https://react.dev/learn/adding-interactivity

**Contents**:
- Adding Interactivity
  - In this chapter
- Responding to events
- Ready to learn this topic?
- State: a component’s memory
- Ready to learn this topic?
- Render and commit
- Ready to learn this topic?

Some things on the screen update in response to user input. For example, clicking an image gallery switches the active image. In React, data that changes over time is called state. You can add state to any component, and update it as needed. In this chapter, you’ll learn how to write components that handle interactions, update their state, and display different output over time.

React lets you add event handlers to your JSX. Event handlers are your own functions that will be triggered in response to user interactions like clicking, hovering, focusing on form inputs, and so on.

Built-in components like <button> only support built-in browser events like onClick. However, you can also create your own components, and give their event handler props any application-specific names that you like.

Read Responding to Events to learn how to add event handlers.

Components often need to change what’s on the screen as a result of an interaction. Typing into the form should update the input field, clicking “next” on an image carousel should change which image is displayed, clicking “buy” puts a product in the shopping cart. Components need to “remember” things: the current input value, the current image, the shopping cart. In React, this kind of component-specific memory is called state.

You can add state to a component with a useState Hook. Hooks are special functions that let your components use React features (state is one of those features). The useState Hook lets you declare a state variable. It takes the initial state and returns a pair of values: the current state, and a state setter function that lets you update it.

Here is how an image gallery uses and updates state on click:

Read State: A Component’s Memory to learn how to remember a value and update it on interaction.

Before your components are displayed on the screen, they must be rendered by React. Understanding the steps in this process will help you think about how your code executes and explain its behavior

*[Content truncated - see full docs]*

**Examples**:

```javascript
const [index, setIndex] = useState(0);const [showMore, setShowMore] = useState(false);
```

```text
console.log(count);  // 0setCount(count + 1); // Request a re-render with 1console.log(count);  // Still 0!
```

```text
console.log(score);  // 0setScore(score + 1); // setScore(0 + 1);console.log(score);  // 0setScore(score + 1); // setScore(0 + 1);console.log(score);  // 0setScore(score + 1); // setScore(0 + 1);console.log(score);  // 0
```

---

## Build a React app from Scratch – React

**URL**: https://react.dev/learn/build-a-react-app-from-scratch

**Contents**:
- Build a React app from Scratch
      - Deep Dive
    - Consider using a framework
- Step 1: Install a build tool
  - Vite
  - Parcel
  - Rsbuild
  - Note

If your app has constraints not well-served by existing frameworks, you prefer to build your own framework, or you just want to learn the basics of a React app, you can build a React app from scratch.

Starting from scratch is an easy way to get started using React, but a major tradeoff to be aware of is that going this route is often the same as building your own adhoc framework. As your requirements evolve, you may need to solve more framework-like problems that our recommended frameworks already have well developed and supported solutions for.

For example, if in the future your app needs support for server-side rendering (SSR), static site generation (SSG), and/or React Server Components (RSC), you will have to implement those on your own. Similarly, future React features that require integrating at the framework level will have to be implemented on your own if you want to use them.

Our recommended frameworks also help you build better performing apps. For example, reducing or eliminating waterfalls from network requests makes for a better user experience. This might not be a high priority when you are building a toy project, but if your app gains users you may want to improve its performance.

Going this route also makes it more difficult to get support, since the way you develop routing, data-fetching, and other features will be unique to your situation. You should only choose this option if you are comfortable tackling these problems on your own, or if you’re confident that you will never need these features.

For a list of recommended frameworks, check out Creating a React App.

The first step is to install a build tool like vite, parcel, or rsbuild. These build tools provide features to package and run source code, provide a development server for local development and a build command to deploy your app to a production server.

Vite is a build tool that aims to provide a faster and leaner development experience for modern web projects.

Vite is opinionated

*[Content truncated - see full docs]*

---

## Choosing the State Structure – React

**URL**: https://react.dev/learn/choosing-the-state-structure

**Contents**:
- Choosing the State Structure
  - You will learn
- Principles for structuring state
- Group related state
  - Pitfall
- Avoid contradictions in state
- Avoid redundant state
      - Deep Dive

Structuring state well can make a difference between a component that is pleasant to modify and debug, and one that is a constant source of bugs. Here are some tips you should consider when structuring state.

When you write a component that holds some state, you’ll have to make choices about how many state variables to use and what the shape of their data should be. While it’s possible to write correct programs even with a suboptimal state structure, there are a few principles that can guide you to make better choices:

The goal behind these principles is to make state easy to update without introducing mistakes. Removing redundant and duplicate data from state helps ensure that all its pieces stay in sync. This is similar to how a database engineer might want to “normalize” the database structure to reduce the chance of bugs. To paraphrase Albert Einstein, “Make your state as simple as it can be—but no simpler.”

Now let’s see how these principles apply in action.

You might sometimes be unsure between using a single or multiple state variables.

Technically, you can use either of these approaches. But if some two state variables always change together, it might be a good idea to unify them into a single state variable. Then you won’t forget to always keep them in sync, like in this example where moving the cursor updates both coordinates of the red dot:

Another case where you’ll group data into an object or an array is when you don’t know how many pieces of state you’ll need. For example, it’s helpful when you have a form where the user can add custom fields.

If your state variable is an object, remember that you can’t update only one field in it without explicitly copying the other fields. For example, you can’t do setPosition({ x: 100 }) in the above example because it would not have the y property at all! Instead, if you wanted to set x alone, you would either do setPosition({ ...position, x: 100 }), or split them into two state variables and do setX(100).



*[Content truncated - see full docs]*

**Examples**:

```javascript
const [x, setX] = useState(0);const [y, setY] = useState(0);
```

```javascript
const [position, setPosition] = useState({ x: 0, y: 0 });
```

```javascript
const isSending = status === 'sending';const isSent = status === 'sent';
```

---

## Conditional Rendering – React

**URL**: https://react.dev/learn/conditional-rendering

**Contents**:
- Conditional Rendering
  - You will learn
- Conditionally returning JSX
  - Conditionally returning nothing with null
- Conditionally including JSX
  - Conditional (ternary) operator (? :)
      - Deep Dive
    - Are these two examples fully equivalent?

Your components will often need to display different things depending on different conditions. In React, you can conditionally render JSX using JavaScript syntax like if statements, &&, and ? : operators.

Let’s say you have a PackingList component rendering several Items, which can be marked as packed or not:

Notice that some of the Item components have their isPacked prop set to true instead of false. You want to add a checkmark (✅) to packed items if isPacked={true}.

You can write this as an if/else statement like so:

If the isPacked prop is true, this code returns a different JSX tree. With this change, some of the items get a checkmark at the end:

Try editing what gets returned in either case, and see how the result changes!

Notice how you’re creating branching logic with JavaScript’s if and return statements. In React, control flow (like conditions) is handled by JavaScript.

In some situations, you won’t want to render anything at all. For example, say you don’t want to show packed items at all. A component must return something. In this case, you can return null:

If isPacked is true, the component will return nothing, null. Otherwise, it will return JSX to render.

In practice, returning null from a component isn’t common because it might surprise a developer trying to render it. More often, you would conditionally include or exclude the component in the parent component’s JSX. Here’s how to do that!

In the previous example, you controlled which (if any!) JSX tree would be returned by the component. You may already have noticed some duplication in the render output:

Both of the conditional branches return <li className="item">...</li>:

While this duplication isn’t harmful, it could make your code harder to maintain. What if you want to change the className? You’d have to do it in two places in your code! In such a situation, you could conditionally include a little JSX to make your code more DRY.

JavaScript has a compact syntax for writing a condit

*[Content truncated - see full docs]*

**Examples**:

```text
if (isPacked) {  return <li className="item">{name} ✅</li>;}return <li className="item">{name}</li>;
```

```text
if (isPacked) {  return null;}return <li className="item">{name}</li>;
```

```text
<li className="item">{name} ✅</li>
```

---

## Creating a React App – React

**URL**: https://react.dev/learn/start-a-new-react-project

**Contents**:
- Creating a React App
- Full-stack frameworks
  - Note
    - Full-stack frameworks do not require a server.
  - Next.js (App Router)
  - React Router (v7)
  - Expo (for native apps)
- Other frameworks

If you want to build a new app or website with React, we recommend starting with a framework.

If your app has constraints not well-served by existing frameworks, you prefer to build your own framework, or you just want to learn the basics of a React app, you can build a React app from scratch.

These recommended frameworks support all the features you need to deploy and scale your app in production. They have integrated the latest React features and take advantage of React’s architecture.

All the frameworks on this page support client-side rendering (CSR), single-page apps (SPA), and static-site generation (SSG). These apps can be deployed to a CDN or static hosting service without a server. Additionally, these frameworks allow you to add server-side rendering on a per-route basis, when it makes sense for your use case.

This allows you to start with a client-only app, and if your needs change later, you can opt-in to using server features on individual routes without rewriting your app. See your framework’s documentation for configuring the rendering strategy.

Next.js’s App Router is a React framework that takes full advantage of React’s architecture to enable full-stack React apps.

Next.js is maintained by Vercel. You can deploy a Next.js app to any hosting provider that supports Node.js or Docker containers, or to your own server. Next.js also supports static export which doesn’t require a server.

React Router is the most popular routing library for React and can be paired with Vite to create a full-stack React framework. It emphasizes standard Web APIs and has several ready to deploy templates for various JavaScript runtimes and platforms.

To create a new React Router framework project, run:

React Router is maintained by Shopify.

Expo is a React framework that lets you create universal Android, iOS, and web apps with truly native UIs. It provides an SDK for React Native that makes the native parts easier to use. To create a new Expo project, run:

If you

*[Content truncated - see full docs]*

**Examples**:

```javascript
// This component runs *only* on the server (or during the build).async function Talks({ confId }) {  // 1. You're on the server, so you can talk to your data layer. API endpoint not required.  const talks = await db.Talks.findAll({ confId });  // 2. Add any amount of rendering logic. It won't make your JavaScript bundle larger.  const videos = talks.map(talk => talk.video);  // 3. Pass the data down to the components that will run in the browser.  return <SearchableVideoList videos={videos} />;
...
```

```text
<Suspense fallback={<TalksLoading />}>  <Talks confId={conf.id} /></Suspense>
```

---

## Creating a React App – React

**URL**: https://react.dev/learn/creating-a-react-app

**Contents**:
- Creating a React App
- Full-stack frameworks
  - Note
    - Full-stack frameworks do not require a server.
  - Next.js (App Router)
  - React Router (v7)
  - Expo (for native apps)
- Other frameworks

If you want to build a new app or website with React, we recommend starting with a framework.

If your app has constraints not well-served by existing frameworks, you prefer to build your own framework, or you just want to learn the basics of a React app, you can build a React app from scratch.

These recommended frameworks support all the features you need to deploy and scale your app in production. They have integrated the latest React features and take advantage of React’s architecture.

All the frameworks on this page support client-side rendering (CSR), single-page apps (SPA), and static-site generation (SSG). These apps can be deployed to a CDN or static hosting service without a server. Additionally, these frameworks allow you to add server-side rendering on a per-route basis, when it makes sense for your use case.

This allows you to start with a client-only app, and if your needs change later, you can opt-in to using server features on individual routes without rewriting your app. See your framework’s documentation for configuring the rendering strategy.

Next.js’s App Router is a React framework that takes full advantage of React’s architecture to enable full-stack React apps.

Next.js is maintained by Vercel. You can deploy a Next.js app to any hosting provider that supports Node.js or Docker containers, or to your own server. Next.js also supports static export which doesn’t require a server.

React Router is the most popular routing library for React and can be paired with Vite to create a full-stack React framework. It emphasizes standard Web APIs and has several ready to deploy templates for various JavaScript runtimes and platforms.

To create a new React Router framework project, run:

React Router is maintained by Shopify.

Expo is a React framework that lets you create universal Android, iOS, and web apps with truly native UIs. It provides an SDK for React Native that makes the native parts easier to use. To create a new Expo project, run:

If you

*[Content truncated - see full docs]*

**Examples**:

```javascript
// This component runs *only* on the server (or during the build).async function Talks({ confId }) {  // 1. You're on the server, so you can talk to your data layer. API endpoint not required.  const talks = await db.Talks.findAll({ confId });  // 2. Add any amount of rendering logic. It won't make your JavaScript bundle larger.  const videos = talks.map(talk => talk.video);  // 3. Pass the data down to the components that will run in the browser.  return <SearchableVideoList videos={videos} />;
...
```

```text
<Suspense fallback={<TalksLoading />}>  <Talks confId={conf.id} /></Suspense>
```

---

## Debugging and Troubleshooting – React

**URL**: https://react.dev/learn/react-compiler/debugging

**Contents**:
- Debugging and Troubleshooting
  - You will learn
- Understanding Compiler Behavior
  - Compiler Errors vs Runtime Issues
- Common Breaking Patterns
- Debugging Workflow
  - Compiler Build Errors
  - Runtime Issues

This guide helps you identify and fix issues when using React Compiler. Learn how to debug compilation problems and resolve common issues.

React Compiler is designed to handle code that follows the Rules of React. When it encounters code that might break these rules, it safely skips optimization rather than risk changing your app’s behavior.

Compiler errors occur at build time and prevent your code from compiling. These are rare because the compiler is designed to skip problematic code rather than fail.

Runtime issues occur when compiled code behaves differently than expected. Most of the time, if you encounter an issue with React Compiler, it’s a runtime issue. This typically happens when your code violates the Rules of React in subtle ways that the compiler couldn’t detect, and the compiler mistakenly compiled a component it should have skipped.

When debugging runtime issues, focus your efforts on finding Rules of React violations in the affected components that were not detected by the ESLint rule. The compiler relies on your code following these rules, and when they’re broken in ways it can’t detect, that’s when runtime problems occur.

One of the main ways React Compiler can break your app is if your code was written to rely on memoization for correctness. This means your app depends on specific values being memoized to work properly. Since the compiler may memoize differently than your manual approach, this can lead to unexpected behavior like effects over-firing, infinite loops, or missing updates.

Common scenarios where this occurs:

Follow these steps when you encounter issues:

If you encounter a compiler error that unexpectedly breaks your build, this is likely a bug in the compiler. Report it to the facebook/react repository with:

For runtime behavior issues:

Use "use no memo" to isolate whether an issue is compiler-related:

If the issue disappears, it’s likely related to a Rules of React violation.

You can also try removing manual memoization (

*[Content truncated - see full docs]*

**Examples**:

```javascript
function ProblematicComponent() {  "use no memo"; // Skip compilation for this component  // ... rest of component}
```

---

## Describing the UI – React

**URL**: https://react.dev/learn/describing-the-ui

**Contents**:
- Describing the UI
  - In this chapter
- Your first component
- Ready to learn this topic?
- Importing and exporting components
- Ready to learn this topic?
- Writing markup with JSX
- Ready to learn this topic?

React is a JavaScript library for rendering user interfaces (UI). UI is built from small units like buttons, text, and images. React lets you combine them into reusable, nestable components. From web sites to phone apps, everything on the screen can be broken down into components. In this chapter, you’ll learn to create, customize, and conditionally display React components.

React applications are built from isolated pieces of UI called components. A React component is a JavaScript function that you can sprinkle with markup. Components can be as small as a button, or as large as an entire page. Here is a Gallery component rendering three Profile components:

Read Your First Component to learn how to declare and use React components.

You can declare many components in one file, but large files can get difficult to navigate. To solve this, you can export a component into its own file, and then import that component from another file:

Read Importing and Exporting Components to learn how to split components into their own files.

Each React component is a JavaScript function that may contain some markup that React renders into the browser. React components use a syntax extension called JSX to represent that markup. JSX looks a lot like HTML, but it is a bit stricter and can display dynamic information.

If we paste existing HTML markup into a React component, it won’t always work:

If you have existing HTML like this, you can fix it using a converter:

Read Writing Markup with JSX to learn how to write valid JSX.

JSX lets you write HTML-like markup inside a JavaScript file, keeping rendering logic and content in the same place. Sometimes you will want to add a little JavaScript logic or reference a dynamic property inside that markup. In this situation, you can use curly braces in your JSX to “open a window” to JavaScript:

Read JavaScript in JSX with Curly Braces to learn how to access JavaScript data from JSX.

React components use props to communicate with each o

*[Content truncated - see full docs]*

---

## Escape Hatches – React

**URL**: https://react.dev/learn/escape-hatches

**Contents**:
- Escape Hatches
  - In this chapter
- Referencing values with refs
- Ready to learn this topic?
- Manipulating the DOM with refs
- Ready to learn this topic?
- Synchronizing with Effects
- Ready to learn this topic?

Some of your components may need to control and synchronize with systems outside of React. For example, you might need to focus an input using the browser API, play and pause a video player implemented without React, or connect and listen to messages from a remote server. In this chapter, you’ll learn the escape hatches that let you “step outside” React and connect to external systems. Most of your application logic and data flow should not rely on these features.

When you want a component to “remember” some information, but you don’t want that information to trigger new renders, you can use a ref:

Like state, refs are retained by React between re-renders. However, setting state re-renders a component. Changing a ref does not! You can access the current value of that ref through the ref.current property.

A ref is like a secret pocket of your component that React doesn’t track. For example, you can use refs to store timeout IDs, DOM elements, and other objects that don’t impact the component’s rendering output.

Read Referencing Values with Refs to learn how to use refs to remember information.

React automatically updates the DOM to match your render output, so your components won’t often need to manipulate it. However, sometimes you might need access to the DOM elements managed by React—for example, to focus a node, scroll to it, or measure its size and position. There is no built-in way to do those things in React, so you will need a ref to the DOM node. For example, clicking the button will focus the input using a ref:

Read Manipulating the DOM with Refs to learn how to access DOM elements managed by React.

Some components need to synchronize with external systems. For example, you might want to control a non-React component based on the React state, set up a server connection, or send an analytics log when a component appears on the screen. Unlike event handlers, which let you handle particular events, Effects let you run some code after rendering. Use them

*[Content truncated - see full docs]*

**Examples**:

```javascript
const ref = useRef(0);
```

```javascript
function Form() {  const [firstName, setFirstName] = useState('Taylor');  const [lastName, setLastName] = useState('Swift');  // 🔴 Avoid: redundant state and unnecessary Effect  const [fullName, setFullName] = useState('');  useEffect(() => {    setFullName(firstName + ' ' + lastName);  }, [firstName, lastName]);  // ...}
```

```javascript
function Form() {  const [firstName, setFirstName] = useState('Taylor');  const [lastName, setLastName] = useState('Swift');  // ✅ Good: calculated during rendering  const fullName = firstName + ' ' + lastName;  // ...}
```

---

## Extracting State Logic into a Reducer – React

**URL**: https://react.dev/learn/extracting-state-logic-into-a-reducer

**Contents**:
- Extracting State Logic into a Reducer
  - You will learn
- Consolidate state logic with a reducer
  - Step 1: Move from setting state to dispatching actions
  - Note
  - Step 2: Write a reducer function
  - Note
      - Deep Dive

Components with many state updates spread across many event handlers can get overwhelming. For these cases, you can consolidate all the state update logic outside your component in a single function, called a reducer.

As your components grow in complexity, it can get harder to see at a glance all the different ways in which a component’s state gets updated. For example, the TaskApp component below holds an array of tasks in state and uses three different event handlers to add, remove, and edit tasks:

Each of its event handlers calls setTasks in order to update the state. As this component grows, so does the amount of state logic sprinkled throughout it. To reduce this complexity and keep all your logic in one easy-to-access place, you can move that state logic into a single function outside your component, called a “reducer”.

Reducers are a different way to handle state. You can migrate from useState to useReducer in three steps:

Your event handlers currently specify what to do by setting state:

Remove all the state setting logic. What you are left with are three event handlers:

Managing state with reducers is slightly different from directly setting state. Instead of telling React “what to do” by setting state, you specify “what the user just did” by dispatching “actions” from your event handlers. (The state update logic will live elsewhere!) So instead of “setting tasks” via an event handler, you’re dispatching an “added/changed/deleted a task” action. This is more descriptive of the user’s intent.

The object you pass to dispatch is called an “action”:

It is a regular JavaScript object. You decide what to put in it, but generally it should contain the minimal information about what happened. (You will add the dispatch function itself in a later step.)

An action object can have any shape.

By convention, it is common to give it a string type that describes what happened, and pass any additional information in other fields. The type is specific to a compone

*[Content truncated - see full docs]*

**Examples**:

```javascript
function handleAddTask(text) {  setTasks([    ...tasks,    {      id: nextId++,      text: text,      done: false,    },  ]);}function handleChangeTask(task) {  setTasks(    tasks.map((t) => {      if (t.id === task.id) {        return task;      } else {        return t;      }    })  );}function handleDeleteTask(taskId) {  setTasks(tasks.filter((t) => t.id !== taskId));}
```

```javascript
function handleAddTask(text) {  dispatch({    type: 'added',    id: nextId++,    text: text,  });}function handleChangeTask(task) {  dispatch({    type: 'changed',    task: task,  });}function handleDeleteTask(taskId) {  dispatch({    type: 'deleted',    id: taskId,  });}
```

```javascript
function handleDeleteTask(taskId) {  dispatch(    // "action" object:    {      type: 'deleted',      id: taskId,    }  );}
```

---

## Importing and Exporting Components – React

**URL**: https://react.dev/learn/importing-and-exporting-components

**Contents**:
- Importing and Exporting Components
  - You will learn
- The root component file
- Exporting and importing a component
  - Note
      - Deep Dive
    - Default vs named exports
- Exporting and importing multiple components from the same file

The magic of components lies in their reusability: you can create components that are composed of other components. But as you nest more and more components, it often makes sense to start splitting them into different files. This lets you keep your files easy to scan and reuse components in more places.

In Your First Component, you made a Profile component and a Gallery component that renders it:

These currently live in a root component file, named App.js in this example. Depending on your setup, your root component could be in another file, though. If you use a framework with file-based routing, such as Next.js, your root component will be different for every page.

What if you want to change the landing screen in the future and put a list of science books there? Or place all the profiles somewhere else? It makes sense to move Gallery and Profile out of the root component file. This will make them more modular and reusable in other files. You can move a component in three steps:

Here both Profile and Gallery have been moved out of App.js into a new file called Gallery.js. Now you can change App.js to import Gallery from Gallery.js:

Notice how this example is broken down into two component files now:

You may encounter files that leave off the .js file extension like so:

Either './Gallery.js' or './Gallery' will work with React, though the former is closer to how native ES Modules work.

There are two primary ways to export values with JavaScript: default exports and named exports. So far, our examples have only used default exports. But you can use one or both of them in the same file. A file can have no more than one default export, but it can have as many named exports as you like.

How you export your component dictates how you must import it. You will get an error if you try to import a default export the same way you would a named export! This chart can help you keep track:

When you write a default import, you can put any name you want after import. For 

*[Content truncated - see full docs]*

**Examples**:

```python
import Gallery from './Gallery';
```

```javascript
export function Profile() {  // ...}
```

```python
import { Profile } from './Gallery.js';
```

---

## Installation – React

**URL**: https://react.dev/learn/installation

**Contents**:
- Installation
- Try React
- Creating a React App
- Build a React App from Scratch
- Add React to an existing project
  - Note
    - Should I use Create React App?
- Next steps

React has been designed from the start for gradual adoption. You can use as little or as much React as you need. Whether you want to get a taste of React, add some interactivity to an HTML page, or start a complex React-powered app, this section will help you get started.

You don’t need to install anything to play with React. Try editing this sandbox!

You can edit it directly or open it in a new tab by pressing the “Fork” button in the upper right corner.

Most pages in the React documentation contain sandboxes like this. Outside of the React documentation, there are many online sandboxes that support React: for example, CodeSandbox, StackBlitz, or CodePen.

To try React locally on your computer, download this HTML page. Open it in your editor and in your browser!

If you want to start a new React app, you can create a React app using a recommended framework.

If a framework is not a good fit for your project, you prefer to build your own framework, or you just want to learn the basics of a React app you can build a React app from scratch.

If want to try using React in your existing app or a website, you can add React to an existing project.

No. Create React App has been deprecated. For more information, see Sunsetting Create React App.

Head to the Quick Start guide for a tour of the most important React concepts you will encounter every day.

---

## JavaScript in JSX with Curly Braces – React

**URL**: https://react.dev/learn/javascript-in-jsx-with-curly-braces

**Contents**:
- JavaScript in JSX with Curly Braces
  - You will learn
- Passing strings with quotes
- Using curly braces: A window into the JavaScript world
  - Where to use curly braces
- Using “double curlies”: CSS and other objects in JSX
  - Pitfall
- More fun with JavaScript objects and curly braces

JSX lets you write HTML-like markup inside a JavaScript file, keeping rendering logic and content in the same place. Sometimes you will want to add a little JavaScript logic or reference a dynamic property inside that markup. In this situation, you can use curly braces in your JSX to open a window to JavaScript.

When you want to pass a string attribute to JSX, you put it in single or double quotes:

Here, "https://i.imgur.com/7vQD0fPs.jpg" and "Gregorio Y. Zara" are being passed as strings.

But what if you want to dynamically specify the src or alt text? You could use a value from JavaScript by replacing " and " with { and }:

Notice the difference between className="avatar", which specifies an "avatar" CSS class name that makes the image round, and src={avatar} that reads the value of the JavaScript variable called avatar. That’s because curly braces let you work with JavaScript right there in your markup!

JSX is a special way of writing JavaScript. That means it’s possible to use JavaScript inside it—with curly braces { }. The example below first declares a name for the scientist, name, then embeds it with curly braces inside the <h1>:

Try changing the name’s value from 'Gregorio Y. Zara' to 'Hedy Lamarr'. See how the list title changes?

Any JavaScript expression will work between curly braces, including function calls like formatDate():

You can only use curly braces in two ways inside JSX:

In addition to strings, numbers, and other JavaScript expressions, you can even pass objects in JSX. Objects are also denoted with curly braces, like { name: "Hedy Lamarr", inventions: 5 }. Therefore, to pass a JS object in JSX, you must wrap the object in another pair of curly braces: person={{ name: "Hedy Lamarr", inventions: 5 }}.

You may see this with inline CSS styles in JSX. React does not require you to use inline styles (CSS classes work great for most cases). But when you need an inline style, you pass an object to the style attribute:

Try changing the values 

*[Content truncated - see full docs]*

**Examples**:

```text
<ul style={  {    backgroundColor: 'black',    color: 'pink'  }}>
```

```javascript
const person = {  name: 'Gregorio Y. Zara',  theme: {    backgroundColor: 'black',    color: 'pink'  }};
```

```text
<div style={person.theme}>  <h1>{person.name}'s Todos</h1>
```

---

## Keeping Components Pure – React

**URL**: https://react.dev/learn/keeping-components-pure

**Contents**:
- Keeping Components Pure
  - You will learn
- Purity: Components as formulas
- Side Effects: (un)intended consequences
      - Deep Dive
    - Detecting impure calculations with StrictMode
  - Local mutation: Your component’s little secret
- Where you can cause side effects

Some JavaScript functions are pure. Pure functions only perform a calculation and nothing more. By strictly only writing your components as pure functions, you can avoid an entire class of baffling bugs and unpredictable behavior as your codebase grows. To get these benefits, though, there are a few rules you must follow.

In computer science (and especially the world of functional programming), a pure function is a function with the following characteristics:

You might already be familiar with one example of pure functions: formulas in math.

Consider this math formula: y = 2x.

If x = 2 then y = 4. Always.

If x = 3 then y = 6. Always.

If x = 3, y won’t sometimes be 9 or –1 or 2.5 depending on the time of day or the state of the stock market.

If y = 2x and x = 3, y will always be 6.

If we made this into a JavaScript function, it would look like this:

In the above example, double is a pure function. If you pass it 3, it will return 6. Always.

React is designed around this concept. React assumes that every component you write is a pure function. This means that React components you write must always return the same JSX given the same inputs:

When you pass drinkers={2} to Recipe, it will return JSX containing 2 cups of water. Always.

If you pass drinkers={4}, it will return JSX containing 4 cups of water. Always.

Just like a math formula.

You could think of your components as recipes: if you follow them and don’t introduce new ingredients during the cooking process, you will get the same dish every time. That “dish” is the JSX that the component serves to React to render.

Illustrated by Rachel Lee Nabors

React’s rendering process must always be pure. Components should only return their JSX, and not change any objects or variables that existed before rendering—that would make them impure!

Here is a component that breaks this rule:

This component is reading and writing a guest variable declared outside of it. This means that calling this component multipl

*[Content truncated - see full docs]*

**Examples**:

```javascript
function double(number) {  return 2 * number;}
```

---

## Lifecycle of Reactive Effects – React

**URL**: https://react.dev/learn/lifecycle-of-reactive-effects

**Contents**:
- Lifecycle of Reactive Effects
  - You will learn
- The lifecycle of an Effect
  - Note
  - Why synchronization may need to happen more than once
  - How React re-synchronizes your Effect
  - Thinking from the Effect’s perspective
  - How React verifies that your Effect can re-synchronize

Effects have a different lifecycle from components. Components may mount, update, or unmount. An Effect can only do two things: to start synchronizing something, and later to stop synchronizing it. This cycle can happen multiple times if your Effect depends on props and state that change over time. React provides a linter rule to check that you’ve specified your Effect’s dependencies correctly. This keeps your Effect synchronized to the latest props and state.

Every React component goes through the same lifecycle:

It’s a good way to think about components, but not about Effects. Instead, try to think about each Effect independently from your component’s lifecycle. An Effect describes how to synchronize an external system to the current props and state. As your code changes, synchronization will need to happen more or less often.

To illustrate this point, consider this Effect connecting your component to a chat server:

Your Effect’s body specifies how to start synchronizing:

The cleanup function returned by your Effect specifies how to stop synchronizing:

Intuitively, you might think that React would start synchronizing when your component mounts and stop synchronizing when your component unmounts. However, this is not the end of the story! Sometimes, it may also be necessary to start and stop synchronizing multiple times while the component remains mounted.

Let’s look at why this is necessary, when it happens, and how you can control this behavior.

Some Effects don’t return a cleanup function at all. More often than not, you’ll want to return one—but if you don’t, React will behave as if you returned an empty cleanup function.

Imagine this ChatRoom component receives a roomId prop that the user picks in a dropdown. Let’s say that initially the user picks the "general" room as the roomId. Your app displays the "general" chat room:

After the UI is displayed, React will run your Effect to start synchronizing. It connects to the "general" room:

Later, the use

*[Content truncated - see full docs]*

**Examples**:

```javascript
const serverUrl = 'https://localhost:1234';function ChatRoom({ roomId }) {  useEffect(() => {    const connection = createConnection(serverUrl, roomId);    connection.connect();    return () => {      connection.disconnect();    };  }, [roomId]);  // ...}
```

```javascript
// ...    const connection = createConnection(serverUrl, roomId);    connection.connect();    return () => {      connection.disconnect();    };    // ...
```

```javascript
// ...    const connection = createConnection(serverUrl, roomId);    connection.connect();    return () => {      connection.disconnect();    };    // ...
```

---

## Managing State – React

**URL**: https://react.dev/learn/managing-state

**Contents**:
- Managing State
  - In this chapter
- Reacting to input with state
- Ready to learn this topic?
- Choosing the state structure
- Ready to learn this topic?
- Sharing state between components
- Ready to learn this topic?

As your application grows, it helps to be more intentional about how your state is organized and how the data flows between your components. Redundant or duplicate state is a common source of bugs. In this chapter, you’ll learn how to structure your state well, how to keep your state update logic maintainable, and how to share state between distant components.

With React, you won’t modify the UI from code directly. For example, you won’t write commands like “disable the button”, “enable the button”, “show the success message”, etc. Instead, you will describe the UI you want to see for the different visual states of your component (“initial state”, “typing state”, “success state”), and then trigger the state changes in response to user input. This is similar to how designers think about UI.

Here is a quiz form built using React. Note how it uses the status state variable to determine whether to enable or disable the submit button, and whether to show the success message instead.

Read Reacting to Input with State to learn how to approach interactions with a state-driven mindset.

Structuring state well can make a difference between a component that is pleasant to modify and debug, and one that is a constant source of bugs. The most important principle is that state shouldn’t contain redundant or duplicated information. If there’s unnecessary state, it’s easy to forget to update it, and introduce bugs!

For example, this form has a redundant fullName state variable:

You can remove it and simplify the code by calculating fullName while the component is rendering:

This might seem like a small change, but many bugs in React apps are fixed this way.

Read Choosing the State Structure to learn how to design the state shape to avoid bugs.

Sometimes, you want the state of two components to always change together. To do it, remove state from both of them, move it to their closest common parent, and then pass it down to them via props. This is known as “lifting state up”,

*[Content truncated - see full docs]*

---

## Manipulating the DOM with Refs – React

**URL**: https://react.dev/learn/manipulating-the-dom-with-refs

**Contents**:
- Manipulating the DOM with Refs
  - You will learn
- Getting a ref to the node
  - Example: Focusing a text input
  - Example: Scrolling to an element
      - Deep Dive
    - How to manage a list of refs using a ref callback
  - Note

React automatically updates the DOM to match your render output, so your components won’t often need to manipulate it. However, sometimes you might need access to the DOM elements managed by React—for example, to focus a node, scroll to it, or measure its size and position. There is no built-in way to do those things in React, so you will need a ref to the DOM node.

To access a DOM node managed by React, first, import the useRef Hook:

Then, use it to declare a ref inside your component:

Finally, pass your ref as the ref attribute to the JSX tag for which you want to get the DOM node:

The useRef Hook returns an object with a single property called current. Initially, myRef.current will be null. When React creates a DOM node for this <div>, React will put a reference to this node into myRef.current. You can then access this DOM node from your event handlers and use the built-in browser APIs defined on it.

In this example, clicking the button will focus the input:

While DOM manipulation is the most common use case for refs, the useRef Hook can be used for storing other things outside React, like timer IDs. Similarly to state, refs remain between renders. Refs are like state variables that don’t trigger re-renders when you set them. Read about refs in Referencing Values with Refs.

You can have more than a single ref in a component. In this example, there is a carousel of three images. Each button centers an image by calling the browser scrollIntoView() method on the corresponding DOM node:

In the above examples, there is a predefined number of refs. However, sometimes you might need a ref to each item in the list, and you don’t know how many you will have. Something like this wouldn’t work:

This is because Hooks must only be called at the top-level of your component. You can’t call useRef in a loop, in a condition, or inside a map() call.

One possible way around this is to get a single ref to their parent element, and then use DOM manipulation methods like que

*[Content truncated - see full docs]*

**Examples**:

```python
import { useRef } from 'react';
```

```javascript
const myRef = useRef(null);
```

```text
<div ref={myRef}>
```

---

## Passing Data Deeply with Context – React

**URL**: https://react.dev/learn/passing-data-deeply-with-context

**Contents**:
- Passing Data Deeply with Context
  - You will learn
- The problem with passing props
- Context: an alternative to passing props
  - Step 1: Create the context
  - Step 2: Use the context
  - Step 3: Provide the context
- Using and providing context from the same component

Usually, you will pass information from a parent component to a child component via props. But passing props can become verbose and inconvenient if you have to pass them through many components in the middle, or if many components in your app need the same information. Context lets the parent component make some information available to any component in the tree below it—no matter how deep—without passing it explicitly through props.

Passing props is a great way to explicitly pipe data through your UI tree to the components that use it.

But passing props can become verbose and inconvenient when you need to pass some prop deeply through the tree, or if many components need the same prop. The nearest common ancestor could be far removed from the components that need data, and lifting state up that high can lead to a situation called “prop drilling”.

Wouldn’t it be great if there were a way to “teleport” data to the components in the tree that need it without passing props? With React’s context feature, there is!

Context lets a parent component provide data to the entire tree below it. There are many uses for context. Here is one example. Consider this Heading component that accepts a level for its size:

Let’s say you want multiple headings within the same Section to always have the same size:

Currently, you pass the level prop to each <Heading> separately:

It would be nice if you could pass the level prop to the <Section> component instead and remove it from the <Heading>. This way you could enforce that all headings in the same section have the same size:

But how can the <Heading> component know the level of its closest <Section>? That would require some way for a child to “ask” for data from somewhere above in the tree.

You can’t do it with props alone. This is where context comes into play. You will do it in three steps:

Context lets a parent—even a distant one!—provide some data to the entire tree inside of it.

Using context in close children

Using con

*[Content truncated - see full docs]*

**Examples**:

```text
<Section>  <Heading level={3}>About</Heading>  <Heading level={3}>Photos</Heading>  <Heading level={3}>Videos</Heading></Section>
```

```text
<Section level={3}>  <Heading>About</Heading>  <Heading>Photos</Heading>  <Heading>Videos</Heading></Section>
```

```python
import { useContext } from 'react';import { LevelContext } from './LevelContext.js';
```

---

## Passing Props to a Component – React

**URL**: https://react.dev/learn/passing-props-to-a-component

**Contents**:
- Passing Props to a Component
  - You will learn
- Familiar props
- Passing props to a component
  - Step 1: Pass props to the child component
  - Note
  - Step 2: Read props inside the child component
  - Pitfall

React components use props to communicate with each other. Every parent component can pass some information to its child components by giving them props. Props might remind you of HTML attributes, but you can pass any JavaScript value through them, including objects, arrays, and functions.

Props are the information that you pass to a JSX tag. For example, className, src, alt, width, and height are some of the props you can pass to an <img>:

The props you can pass to an <img> tag are predefined (ReactDOM conforms to the HTML standard). But you can pass any props to your own components, such as <Avatar>, to customize them. Here’s how!

In this code, the Profile component isn’t passing any props to its child component, Avatar:

You can give Avatar some props in two steps.

First, pass some props to Avatar. For example, let’s pass two props: person (an object), and size (a number):

If double curly braces after person= confuse you, recall they’re merely an object inside the JSX curlies.

Now you can read these props inside the Avatar component.

You can read these props by listing their names person, size separated by the commas inside ({ and }) directly after function Avatar. This lets you use them inside the Avatar code, like you would with a variable.

Add some logic to Avatar that uses the person and size props for rendering, and you’re done.

Now you can configure Avatar to render in many different ways with different props. Try tweaking the values!

Props let you think about parent and child components independently. For example, you can change the person or the size props inside Profile without having to think about how Avatar uses them. Similarly, you can change how the Avatar uses these props, without looking at the Profile.

You can think of props like “knobs” that you can adjust. They serve the same role as arguments serve for functions—in fact, props are the only argument to your component! React component functions accept a single argument, a props object

*[Content truncated - see full docs]*

**Examples**:

```javascript
export default function Profile() {  return (    <Avatar />  );}
```

```javascript
export default function Profile() {  return (    <Avatar      person={{ name: 'Lin Lanying', imageId: '1bX5QH6' }}      size={100}    />  );}
```

```javascript
function Avatar({ person, size }) {  // person and size are available here}
```

---

## Preserving and Resetting State – React

**URL**: https://react.dev/learn/preserving-and-resetting-state

**Contents**:
- Preserving and Resetting State
  - You will learn
- State is tied to a position in the render tree
- Same component at the same position preserves state
  - Pitfall
- Different components at the same position reset state
  - Pitfall
- Resetting state at the same position

State is isolated between components. React keeps track of which state belongs to which component based on their place in the UI tree. You can control when to preserve state and when to reset it between re-renders.

React builds render trees for the component structure in your UI.

When you give a component state, you might think the state “lives” inside the component. But the state is actually held inside React. React associates each piece of state it’s holding with the correct component by where that component sits in the render tree.

Here, there is only one <Counter /> JSX tag, but it’s rendered at two different positions:

Here’s how these look as a tree:

These are two separate counters because each is rendered at its own position in the tree. You don’t usually have to think about these positions to use React, but it can be useful to understand how it works.

In React, each component on the screen has fully isolated state. For example, if you render two Counter components side by side, each of them will get its own, independent, score and hover states.

Try clicking both counters and notice they don’t affect each other:

As you can see, when one counter is updated, only the state for that component is updated:

React will keep the state around for as long as you render the same component at the same position in the tree. To see this, increment both counters, then remove the second component by unchecking “Render the second counter” checkbox, and then add it back by ticking it again:

Notice how the moment you stop rendering the second counter, its state disappears completely. That’s because when React removes a component, it destroys its state.

When you tick “Render the second counter”, a second Counter and its state are initialized from scratch (score = 0) and added to the DOM.

React preserves a component’s state for as long as it’s being rendered at its position in the UI tree. If it gets removed, or a different component gets rendered at the same position

*[Content truncated - see full docs]*

**Examples**:

```text
{isPlayerA ? (  <Counter key="Taylor" person="Taylor" />) : (  <Counter key="Sarah" person="Sarah" />)}
```

```text
<Chat key={to.id} contact={to} />
```

---

## Queueing a Series of State Updates – React

**URL**: https://react.dev/learn/queueing-a-series-of-state-updates

**Contents**:
- Queueing a Series of State Updates
  - You will learn
- React batches state updates
- Updating the same state multiple times before the next render
  - What happens if you update state after replacing it
  - Note
  - What happens if you replace state after updating it
  - Naming conventions

Setting a state variable will queue another render. But sometimes you might want to perform multiple operations on the value before queueing the next render. To do this, it helps to understand how React batches state updates.

You might expect that clicking the “+3” button will increment the counter three times because it calls setNumber(number + 1) three times:

However, as you might recall from the previous section, each render’s state values are fixed, so the value of number inside the first render’s event handler is always 0, no matter how many times you call setNumber(1):

But there is one other factor at play here. React waits until all code in the event handlers has run before processing your state updates. This is why the re-render only happens after all these setNumber() calls.

This might remind you of a waiter taking an order at the restaurant. A waiter doesn’t run to the kitchen at the mention of your first dish! Instead, they let you finish your order, let you make changes to it, and even take orders from other people at the table.

Illustrated by Rachel Lee Nabors

This lets you update multiple state variables—even from multiple components—without triggering too many re-renders. But this also means that the UI won’t be updated until after your event handler, and any code in it, completes. This behavior, also known as batching, makes your React app run much faster. It also avoids dealing with confusing “half-finished” renders where only some of the variables have been updated.

React does not batch across multiple intentional events like clicks—each click is handled separately. Rest assured that React only does batching when it’s generally safe to do. This ensures that, for example, if the first button click disables a form, the second click would not submit it again.

It is an uncommon use case, but if you would like to update the same state variable multiple times before the next render, instead of passing the next state value like setNumber(number + 

*[Content truncated - see full docs]*

**Examples**:

```text
setNumber(0 + 1);setNumber(0 + 1);setNumber(0 + 1);
```

```javascript
setNumber(n => n + 1);setNumber(n => n + 1);setNumber(n => n + 1);
```

```javascript
<button onClick={() => {  setNumber(number + 5);  setNumber(n => n + 1);}}>
```

---

## Quick Start – React

**URL**: https://react.dev/learn

**Contents**:
- Quick Start
  - You will learn
- Creating and nesting components
- Writing markup with JSX
- Adding styles
- Displaying data
- Conditional rendering
- Rendering lists

Welcome to the React documentation! This page will give you an introduction to 80% of the React concepts that you will use on a daily basis.

React apps are made out of components. A component is a piece of the UI (user interface) that has its own logic and appearance. A component can be as small as a button, or as large as an entire page.

React components are JavaScript functions that return markup:

Now that you’ve declared MyButton, you can nest it into another component:

Notice that <MyButton /> starts with a capital letter. That’s how you know it’s a React component. React component names must always start with a capital letter, while HTML tags must be lowercase.

Have a look at the result:

The export default keywords specify the main component in the file. If you’re not familiar with some piece of JavaScript syntax, MDN and javascript.info have great references.

The markup syntax you’ve seen above is called JSX. It is optional, but most React projects use JSX for its convenience. All of the tools we recommend for local development support JSX out of the box.

JSX is stricter than HTML. You have to close tags like <br />. Your component also can’t return multiple JSX tags. You have to wrap them into a shared parent, like a <div>...</div> or an empty <>...</> wrapper:

If you have a lot of HTML to port to JSX, you can use an online converter.

In React, you specify a CSS class with className. It works the same way as the HTML class attribute:

Then you write the CSS rules for it in a separate CSS file:

React does not prescribe how you add CSS files. In the simplest case, you’ll add a <link> tag to your HTML. If you use a build tool or a framework, consult its documentation to learn how to add a CSS file to your project.

JSX lets you put markup into JavaScript. Curly braces let you “escape back” into JavaScript so that you can embed some variable from your code and display it to the user. For example, this will display user.name:

You can also “escape into 

*[Content truncated - see full docs]*

**Examples**:

```javascript
function MyButton() {  return (    <button>I'm a button</button>  );}
```

```javascript
export default function MyApp() {  return (    <div>      <h1>Welcome to my app</h1>      <MyButton />    </div>  );}
```

```javascript
function AboutPage() {  return (    <>      <h1>About</h1>      <p>Hello there.<br />How do you do?</p>    </>  );}
```

---

## React Compiler – React

**URL**: https://react.dev/learn/react-compiler

**Contents**:
- React Compiler
- Introduction
- Installation
- Incremental Adoption
- Debugging and Troubleshooting
- Configuration and Reference
- Additional resources

Learn what React Compiler does and how it automatically optimizes your React application by handling memoization for you, eliminating the need for manual useMemo, useCallback, and React.memo.

Get started with installing React Compiler and learn how to configure it with your build tools.

Learn strategies for gradually adopting React Compiler in your existing codebase if you’re not ready to enable it everywhere yet.

When things don’t work as expected, use our debugging guide to understand the difference between compiler errors and runtime issues, identify common breaking patterns, and follow a systematic debugging workflow.

For detailed configuration options and API reference:

In addition to these docs, we recommend checking the React Compiler Working Group for additional information and discussion about the compiler.

---

## React Developer Tools – React

**URL**: https://react.dev/learn/react-developer-tools

**Contents**:
- React Developer Tools
  - You will learn
- Browser extension
  - Safari and other browsers
- Mobile (React Native)

Use React Developer Tools to inspect React components, edit props and state, and identify performance problems.

The easiest way to debug websites built with React is to install the React Developer Tools browser extension. It is available for several popular browsers:

Now, if you visit a website built with React, you will see the Components and Profiler panels.

For other browsers (for example, Safari), install the react-devtools npm package:

Next open the developer tools from the terminal:

Then connect your website by adding the following <script> tag to the beginning of your website’s <head>:

Reload your website in the browser now to view it in developer tools.

To inspect apps built with React Native, you can use React Native DevTools, the built-in debugger that deeply integrates React Developer Tools. All features work identically to the browser extension, including native element highlighting and selection.

Learn more about debugging in React Native.

For versions of React Native earlier than 0.76, please use the standalone build of React DevTools by following the Safari and other browsers guide above.

**Examples**:

```text
# Yarnyarn global add react-devtools# Npmnpm install -g react-devtools
```

```text
react-devtools
```

```text
<html>  <head>    <script src="http://localhost:8097"></script>
```

---

## Reacting to Input with State – React

**URL**: https://react.dev/learn/reacting-to-input-with-state

**Contents**:
- Reacting to Input with State
  - You will learn
- How declarative UI compares to imperative
- Thinking about UI declaratively
  - Step 1: Identify your component’s different visual states
      - Deep Dive
    - Displaying many visual states at once
  - Step 2: Determine what triggers those state changes

React provides a declarative way to manipulate the UI. Instead of manipulating individual pieces of the UI directly, you describe the different states that your component can be in, and switch between them in response to the user input. This is similar to how designers think about the UI.

When you design UI interactions, you probably think about how the UI changes in response to user actions. Consider a form that lets the user submit an answer:

In imperative programming, the above corresponds directly to how you implement interaction. You have to write the exact instructions to manipulate the UI depending on what just happened. Here’s another way to think about this: imagine riding next to someone in a car and telling them turn by turn where to go.

Illustrated by Rachel Lee Nabors

They don’t know where you want to go, they just follow your commands. (And if you get the directions wrong, you end up in the wrong place!) It’s called imperative because you have to “command” each element, from the spinner to the button, telling the computer how to update the UI.

In this example of imperative UI programming, the form is built without React. It only uses the browser DOM:

Manipulating the UI imperatively works well enough for isolated examples, but it gets exponentially more difficult to manage in more complex systems. Imagine updating a page full of different forms like this one. Adding a new UI element or a new interaction would require carefully checking all existing code to make sure you haven’t introduced a bug (for example, forgetting to show or hide something).

React was built to solve this problem.

In React, you don’t directly manipulate the UI—meaning you don’t enable, disable, show, or hide components directly. Instead, you declare what you want to show, and React figures out how to update the UI. Think of getting into a taxi and telling the driver where you want to go instead of telling them exactly where to turn. It’s the driver’s job to get you there, a

*[Content truncated - see full docs]*

**Examples**:

```javascript
const [answer, setAnswer] = useState('');const [error, setError] = useState(null);
```

```javascript
const [isEmpty, setIsEmpty] = useState(true);const [isTyping, setIsTyping] = useState(false);const [isSubmitting, setIsSubmitting] = useState(false);const [isSuccess, setIsSuccess] = useState(false);const [isError, setIsError] = useState(false);
```

```javascript
const [answer, setAnswer] = useState('');const [error, setError] = useState(null);const [status, setStatus] = useState('typing'); // 'typing', 'submitting', or 'success'
```

---

## Referencing Values with Refs – React

**URL**: https://react.dev/learn/referencing-values-with-refs

**Contents**:
- Referencing Values with Refs
  - You will learn
- Adding a ref to your component
- Example: building a stopwatch
- Differences between refs and state
      - Deep Dive
    - How does useRef work inside?
- When to use refs

When you want a component to “remember” some information, but you don’t want that information to trigger new renders, you can use a ref.

You can add a ref to your component by importing the useRef Hook from React:

Inside your component, call the useRef Hook and pass the initial value that you want to reference as the only argument. For example, here is a ref to the value 0:

useRef returns an object like this:

Illustrated by Rachel Lee Nabors

You can access the current value of that ref through the ref.current property. This value is intentionally mutable, meaning you can both read and write to it. It’s like a secret pocket of your component that React doesn’t track. (This is what makes it an “escape hatch” from React’s one-way data flow—more on that below!)

Here, a button will increment ref.current on every click:

The ref points to a number, but, like state, you could point to anything: a string, an object, or even a function. Unlike state, ref is a plain JavaScript object with the current property that you can read and modify.

Note that the component doesn’t re-render with every increment. Like state, refs are retained by React between re-renders. However, setting state re-renders a component. Changing a ref does not!

You can combine refs and state in a single component. For example, let’s make a stopwatch that the user can start or stop by pressing a button. In order to display how much time has passed since the user pressed “Start”, you will need to keep track of when the Start button was pressed and what the current time is. This information is used for rendering, so you’ll keep it in state:

When the user presses “Start”, you’ll use setInterval in order to update the time every 10 milliseconds:

When the “Stop” button is pressed, you need to cancel the existing interval so that it stops updating the now state variable. You can do this by calling clearInterval, but you need to give it the interval ID that was previously returned by the setInterval call 

*[Content truncated - see full docs]*

**Examples**:

```python
import { useRef } from 'react';
```

```javascript
const ref = useRef(0);
```

```text
{   current: 0 // The value you passed to useRef}
```

---

## Removing Effect Dependencies – React

**URL**: https://react.dev/learn/removing-effect-dependencies

**Contents**:
- Removing Effect Dependencies
  - You will learn
- Dependencies should match the code
  - To remove a dependency, prove that it’s not a dependency
  - To change the dependencies, change the code
  - Pitfall
      - Deep Dive
    - Why is suppressing the dependency linter so dangerous?

When you write an Effect, the linter will verify that you’ve included every reactive value (like props and state) that the Effect reads in the list of your Effect’s dependencies. This ensures that your Effect remains synchronized with the latest props and state of your component. Unnecessary dependencies may cause your Effect to run too often, or even create an infinite loop. Follow this guide to review and remove unnecessary dependencies from your Effects.

When you write an Effect, you first specify how to start and stop whatever you want your Effect to be doing:

Then, if you leave the Effect dependencies empty ([]), the linter will suggest the correct dependencies:

Fill them in according to what the linter says:

Effects “react” to reactive values. Since roomId is a reactive value (it can change due to a re-render), the linter verifies that you’ve specified it as a dependency. If roomId receives a different value, React will re-synchronize your Effect. This ensures that the chat stays connected to the selected room and “reacts” to the dropdown:

Notice that you can’t “choose” the dependencies of your Effect. Every reactive value used by your Effect’s code must be declared in your dependency list. The dependency list is determined by the surrounding code:

Reactive values include props and all variables and functions declared directly inside of your component. Since roomId is a reactive value, you can’t remove it from the dependency list. The linter wouldn’t allow it:

And the linter would be right! Since roomId may change over time, this would introduce a bug in your code.

To remove a dependency, “prove” to the linter that it doesn’t need to be a dependency. For example, you can move roomId out of your component to prove that it’s not reactive and won’t change on re-renders:

Now that roomId is not a reactive value (and can’t change on a re-render), it doesn’t need to be a dependency:

This is why you could now specify an empty ([]) dependency list. Your Effec

*[Content truncated - see full docs]*

**Examples**:

```javascript
const serverUrl = 'https://localhost:1234';function ChatRoom({ roomId }) {  useEffect(() => {    const connection = createConnection(serverUrl, roomId);    connection.connect();    return () => connection.disconnect();  	// ...}
```

```javascript
function ChatRoom({ roomId }) {  useEffect(() => {    const connection = createConnection(serverUrl, roomId);    connection.connect();    return () => connection.disconnect();  }, [roomId]); // ✅ All dependencies declared  // ...}
```

```javascript
const serverUrl = 'https://localhost:1234';function ChatRoom({ roomId }) { // This is a reactive value  useEffect(() => {    const connection = createConnection(serverUrl, roomId); // This Effect reads that reactive value    connection.connect();    return () => connection.disconnect();  }, [roomId]); // ✅ So you must specify that reactive value as a dependency of your Effect  // ...}
```

---

## Render and Commit – React

**URL**: https://react.dev/learn/render-and-commit

**Contents**:
- Render and Commit
  - You will learn
- Step 1: Trigger a render
  - Initial render
  - Re-renders when state updates
- Step 2: React renders your components
  - Pitfall
      - Deep Dive

Before your components are displayed on screen, they must be rendered by React. Understanding the steps in this process will help you think about how your code executes and explain its behavior.

Imagine that your components are cooks in the kitchen, assembling tasty dishes from ingredients. In this scenario, React is the waiter who puts in requests from customers and brings them their orders. This process of requesting and serving UI has three steps:

Illustrated by Rachel Lee Nabors

There are two reasons for a component to render:

When your app starts, you need to trigger the initial render. Frameworks and sandboxes sometimes hide this code, but it’s done by calling createRoot with the target DOM node, and then calling its render method with your component:

Try commenting out the root.render() call and see the component disappear!

Once the component has been initially rendered, you can trigger further renders by updating its state with the set function. Updating your component’s state automatically queues a render. (You can imagine these as a restaurant guest ordering tea, dessert, and all sorts of things after putting in their first order, depending on the state of their thirst or hunger.)

Illustrated by Rachel Lee Nabors

After you trigger a render, React calls your components to figure out what to display on screen. “Rendering” is React calling your components.

This process is recursive: if the updated component returns some other component, React will render that component next, and if that component also returns something, it will render that component next, and so on. The process will continue until there are no more nested components and React knows exactly what should be displayed on screen.

In the following example, React will call Gallery() and Image() several times:

Rendering must always be a pure calculation:

Otherwise, you can encounter confusing bugs and unpredictable behavior as your codebase grows in complexity. When developing in “Strict 

*[Content truncated - see full docs]*

---

## Rendering Lists – React

**URL**: https://react.dev/learn/rendering-lists

**Contents**:
- Rendering Lists
  - You will learn
- Rendering data from arrays
- Filtering arrays of items
  - Pitfall
- Keeping list items in order with key
  - Note
      - Deep Dive

You will often want to display multiple similar components from a collection of data. You can use the JavaScript array methods to manipulate an array of data. On this page, you’ll use filter() and map() with React to filter and transform your array of data into an array of components.

Say that you have a list of content.

The only difference among those list items is their contents, their data. You will often need to show several instances of the same component using different data when building interfaces: from lists of comments to galleries of profile images. In these situations, you can store that data in JavaScript objects and arrays and use methods like map() and filter() to render lists of components from them.

Here’s a short example of how to generate a list of items from an array:

Notice the sandbox above displays a console error:

You’ll learn how to fix this error later on this page. Before we get to that, let’s add some structure to your data.

This data can be structured even more.

Let’s say you want a way to only show people whose profession is 'chemist'. You can use JavaScript’s filter() method to return just those people. This method takes an array of items, passes them through a “test” (a function that returns true or false), and returns a new array of only those items that passed the test (returned true).

You only want the items where profession is 'chemist'. The “test” function for this looks like (person) => person.profession === 'chemist'. Here’s how to put it together:

Arrow functions implicitly return the expression right after =>, so you didn’t need a return statement:

However, you must write return explicitly if your => is followed by a { curly brace!

Arrow functions containing => { are said to have a “block body”. They let you write more than a single line of code, but you have to write a return statement yourself. If you forget it, nothing gets returned!

Notice that all the sandboxes above show an error in the console:

You need to

*[Content truncated - see full docs]*

**Examples**:

```text
<ul>  <li>Creola Katherine Johnson: mathematician</li>  <li>Mario José Molina-Pasquel Henríquez: chemist</li>  <li>Mohammad Abdus Salam: physicist</li>  <li>Percy Lavon Julian: chemist</li>  <li>Subrahmanyan Chandrasekhar: astrophysicist</li></ul>
```

```javascript
const people = [  'Creola Katherine Johnson: mathematician',  'Mario José Molina-Pasquel Henríquez: chemist',  'Mohammad Abdus Salam: physicist',  'Percy Lavon Julian: chemist',  'Subrahmanyan Chandrasekhar: astrophysicist'];
```

```javascript
const listItems = people.map(person => <li>{person}</li>);
```

---

## Responding to Events – React

**URL**: https://react.dev/learn/responding-to-events

**Contents**:
- Responding to Events
  - You will learn
- Adding event handlers
  - Pitfall
  - Reading props in event handlers
  - Passing event handlers as props
  - Naming event handler props
  - Note

React lets you add event handlers to your JSX. Event handlers are your own functions that will be triggered in response to interactions like clicking, hovering, focusing form inputs, and so on.

To add an event handler, you will first define a function and then pass it as a prop to the appropriate JSX tag. For example, here is a button that doesn’t do anything yet:

You can make it show a message when a user clicks by following these three steps:

You defined the handleClick function and then passed it as a prop to <button>. handleClick is an event handler. Event handler functions:

By convention, it is common to name event handlers as handle followed by the event name. You’ll often see onClick={handleClick}, onMouseEnter={handleMouseEnter}, and so on.

Alternatively, you can define an event handler inline in the JSX:

Or, more concisely, using an arrow function:

All of these styles are equivalent. Inline event handlers are convenient for short functions.

Functions passed to event handlers must be passed, not called. For example:

The difference is subtle. In the first example, the handleClick function is passed as an onClick event handler. This tells React to remember it and only call your function when the user clicks the button.

In the second example, the () at the end of handleClick() fires the function immediately during rendering, without any clicks. This is because JavaScript inside the JSX { and } executes right away.

When you write code inline, the same pitfall presents itself in a different way:

Passing inline code like this won’t fire on click—it fires every time the component renders:

If you want to define your event handler inline, wrap it in an anonymous function like so:

Rather than executing the code inside with every render, this creates a function to be called later.

In both cases, what you want to pass is a function:

Read more about arrow functions.

Because event handlers are declared inside of a component, they have access to the compon

*[Content truncated - see full docs]*

**Examples**:

```javascript
<button onClick={function handleClick() {  alert('You clicked me!');}}>
```

```javascript
<button onClick={() => {  alert('You clicked me!');}}>
```

```text
// This alert fires when the component renders, not when clicked!<button onClick={alert('You clicked me!')}>
```

---

## Reusing Logic with Custom Hooks – React

**URL**: https://react.dev/learn/reusing-logic-with-custom-hooks

**Contents**:
- Reusing Logic with Custom Hooks
  - You will learn
- Custom Hooks: Sharing logic between components
  - Extracting your own custom Hook from a component
  - Hook names always start with use
  - Note
      - Deep Dive
    - Should all functions called during rendering start with the use prefix?

React comes with several built-in Hooks like useState, useContext, and useEffect. Sometimes, you’ll wish that there was a Hook for some more specific purpose: for example, to fetch data, to keep track of whether the user is online, or to connect to a chat room. You might not find these Hooks in React, but you can create your own Hooks for your application’s needs.

Imagine you’re developing an app that heavily relies on the network (as most apps do). You want to warn the user if their network connection has accidentally gone off while they were using your app. How would you go about it? It seems like you’ll need two things in your component:

This will keep your component synchronized with the network status. You might start with something like this:

Try turning your network on and off, and notice how this StatusBar updates in response to your actions.

Now imagine you also want to use the same logic in a different component. You want to implement a Save button that will become disabled and show “Reconnecting…” instead of “Save” while the network is off.

To start, you can copy and paste the isOnline state and the Effect into SaveButton:

Verify that, if you turn off the network, the button will change its appearance.

These two components work fine, but the duplication in logic between them is unfortunate. It seems like even though they have different visual appearance, you want to reuse the logic between them.

Imagine for a moment that, similar to useState and useEffect, there was a built-in useOnlineStatus Hook. Then both of these components could be simplified and you could remove the duplication between them:

Although there is no such built-in Hook, you can write it yourself. Declare a function called useOnlineStatus and move all the duplicated code into it from the components you wrote earlier:

At the end of the function, return isOnline. This lets your components read that value:

Verify that switching the network on and off updates both components.

Now 

*[Content truncated - see full docs]*

**Examples**:

```javascript
function StatusBar() {  const isOnline = useOnlineStatus();  return <h1>{isOnline ? '✅ Online' : '❌ Disconnected'}</h1>;}function SaveButton() {  const isOnline = useOnlineStatus();  function handleSaveClick() {    console.log('✅ Progress saved');  }  return (    <button disabled={!isOnline} onClick={handleSaveClick}>      {isOnline ? 'Save progress' : 'Reconnecting...'}    </button>  );}
```

```javascript
function useOnlineStatus() {  const [isOnline, setIsOnline] = useState(true);  useEffect(() => {    function handleOnline() {      setIsOnline(true);    }    function handleOffline() {      setIsOnline(false);    }    window.addEventListener('online', handleOnline);    window.addEventListener('offline', handleOffline);    return () => {      window.removeEventListener('online', handleOnline);      window.removeEventListener('offline', handleOffline);    };  }, []);  return isOnline;}
```

```javascript
// 🔴 Avoid: A Hook that doesn't use Hooksfunction useSorted(items) {  return items.slice().sort();}// ✅ Good: A regular function that doesn't use Hooksfunction getSorted(items) {  return items.slice().sort();}
```

---

## Scaling Up with Reducer and Context – React

**URL**: https://react.dev/learn/scaling-up-with-reducer-and-context

**Contents**:
- Scaling Up with Reducer and Context
  - You will learn
- Combining a reducer with context
  - Step 1: Create the context
  - Step 2: Put state and dispatch into context
  - Step 3: Use context anywhere in the tree
- Moving all wiring into a single file
  - Note

Reducers let you consolidate a component’s state update logic. Context lets you pass information deep down to other components. You can combine reducers and context together to manage state of a complex screen.

In this example from the introduction to reducers, the state is managed by a reducer. The reducer function contains all of the state update logic and is declared at the bottom of this file:

A reducer helps keep the event handlers short and concise. However, as your app grows, you might run into another difficulty. Currently, the tasks state and the dispatch function are only available in the top-level TaskApp component. To let other components read the list of tasks or change it, you have to explicitly pass down the current state and the event handlers that change it as props.

For example, TaskApp passes a list of tasks and the event handlers to TaskList:

And TaskList passes the event handlers to Task:

In a small example like this, this works well, but if you have tens or hundreds of components in the middle, passing down all state and functions can be quite frustrating!

This is why, as an alternative to passing them through props, you might want to put both the tasks state and the dispatch function into context. This way, any component below TaskApp in the tree can read the tasks and dispatch actions without the repetitive “prop drilling”.

Here is how you can combine a reducer with context:

The useReducer Hook returns the current tasks and the dispatch function that lets you update them:

To pass them down the tree, you will create two separate contexts:

Export them from a separate file so that you can later import them from other files:

Here, you’re passing null as the default value to both contexts. The actual values will be provided by the TaskApp component.

Now you can import both contexts in your TaskApp component. Take the tasks and dispatch returned by useReducer() and provide them to the entire tree below:

For now, you pass the informatio

*[Content truncated - see full docs]*

**Examples**:

```text
<TaskList  tasks={tasks}  onChangeTask={handleChangeTask}  onDeleteTask={handleDeleteTask}/>
```

```text
<Task  task={task}  onChange={onChangeTask}  onDelete={onDeleteTask}/>
```

```javascript
const [tasks, dispatch] = useReducer(tasksReducer, initialTasks);
```

---

## Separating Events from Effects – React

**URL**: https://react.dev/learn/separating-events-from-effects

**Contents**:
- Separating Events from Effects
  - You will learn
- Choosing between event handlers and Effects
  - Event handlers run in response to specific interactions
  - Effects run whenever synchronization is needed
- Reactive values and reactive logic
  - Logic inside event handlers is not reactive
  - Logic inside Effects is reactive

Event handlers only re-run when you perform the same interaction again. Unlike event handlers, Effects re-synchronize if some value they read, like a prop or a state variable, is different from what it was during the last render. Sometimes, you also want a mix of both behaviors: an Effect that re-runs in response to some values but not others. This page will teach you how to do that.

First, let’s recap the difference between event handlers and Effects.

Imagine you’re implementing a chat room component. Your requirements look like this:

Let’s say you’ve already implemented the code for them, but you’re not sure where to put it. Should you use event handlers or Effects? Every time you need to answer this question, consider why the code needs to run.

From the user’s perspective, sending a message should happen because the particular “Send” button was clicked. The user will get rather upset if you send their message at any other time or for any other reason. This is why sending a message should be an event handler. Event handlers let you handle specific interactions:

With an event handler, you can be sure that sendMessage(message) will only run if the user presses the button.

Recall that you also need to keep the component connected to the chat room. Where does that code go?

The reason to run this code is not some particular interaction. It doesn’t matter why or how the user navigated to the chat room screen. Now that they’re looking at it and could interact with it, the component needs to stay connected to the selected chat server. Even if the chat room component was the initial screen of your app, and the user has not performed any interactions at all, you would still need to connect. This is why it’s an Effect:

With this code, you can be sure that there is always an active connection to the currently selected chat server, regardless of the specific interactions performed by the user. Whether the user has only opened your app, selected a different room, or nav

*[Content truncated - see full docs]*

**Examples**:

```javascript
function ChatRoom({ roomId }) {  const [message, setMessage] = useState('');  // ...  function handleSendClick() {    sendMessage(message);  }  // ...  return (    <>      <input value={message} onChange={e => setMessage(e.target.value)} />      <button onClick={handleSendClick}>Send</button>    </>  );}
```

```javascript
function ChatRoom({ roomId }) {  // ...  useEffect(() => {    const connection = createConnection(serverUrl, roomId);    connection.connect();    return () => {      connection.disconnect();    };  }, [roomId]);  // ...}
```

```javascript
const serverUrl = 'https://localhost:1234';function ChatRoom({ roomId }) {  const [message, setMessage] = useState('');  // ...}
```

---

## Setup – React

**URL**: https://react.dev/learn/setup

**Contents**:
- Setup
- Editor Setup
- Using TypeScript
- React Developer Tools
- React Compiler
- Next steps

React integrates with tools like editors, TypeScript, browser extensions, and compilers. This section will help you get your environment set up.

See our recommended editors and learn how to set them up to work with React.

TypeScript is a popular way to add type definitions to JavaScript codebases. Learn how to integrate TypeScript into your React projects.

React Developer Tools is a browser extension that can inspect React components, edit props and state, and identify performance problems. Learn how to install it here.

React Compiler is a tool that automatically optimizes your React app. Learn more.

Head to the Quick Start guide for a tour of the most important React concepts you will encounter every day.

---

## Sharing State Between Components – React

**URL**: https://react.dev/learn/sharing-state-between-components

**Contents**:
- Sharing State Between Components
  - You will learn
- Lifting state up by example
  - Step 1: Remove state from the child components
  - Step 2: Pass hardcoded data from the common parent
  - Step 3: Add state to the common parent
      - Deep Dive
    - Controlled and uncontrolled components

Sometimes, you want the state of two components to always change together. To do it, remove state from both of them, move it to their closest common parent, and then pass it down to them via props. This is known as lifting state up, and it’s one of the most common things you will do writing React code.

In this example, a parent Accordion component renders two separate Panels:

Each Panel component has a boolean isActive state that determines whether its content is visible.

Press the Show button for both panels:

Notice how pressing one panel’s button does not affect the other panel—they are independent.

Initially, each Panel’s isActive state is false, so they both appear collapsed

Clicking either Panel’s button will only update that Panel’s isActive state alone

But now let’s say you want to change it so that only one panel is expanded at any given time. With that design, expanding the second panel should collapse the first one. How would you do that?

To coordinate these two panels, you need to “lift their state up” to a parent component in three steps:

This will allow the Accordion component to coordinate both Panels and only expand one at a time.

You will give control of the Panel’s isActive to its parent component. This means that the parent component will pass isActive to Panel as a prop instead. Start by removing this line from the Panel component:

And instead, add isActive to the Panel’s list of props:

Now the Panel’s parent component can control isActive by passing it down as a prop. Conversely, the Panel component now has no control over the value of isActive—it’s now up to the parent component!

To lift state up, you must locate the closest common parent component of both of the child components that you want to coordinate:

In this example, it’s the Accordion component. Since it’s above both panels and can control their props, it will become the “source of truth” for which panel is currently active. Make the Accordion component pass a hardcoded va

*[Content truncated - see full docs]*

**Examples**:

```javascript
const [isActive, setIsActive] = useState(false);
```

```javascript
function Panel({ title, children, isActive }) {
```

```javascript
const [activeIndex, setActiveIndex] = useState(0);
```

---

## State: A Component's Memory – React

**URL**: https://react.dev/learn/state-a-components-memory

**Contents**:
- State: A Component's Memory
  - You will learn
- When a regular variable isn’t enough
- Adding a state variable
  - Meet your first Hook
  - Pitfall
  - Anatomy of useState
  - Note

Components often need to change what’s on the screen as a result of an interaction. Typing into the form should update the input field, clicking “next” on an image carousel should change which image is displayed, clicking “buy” should put a product in the shopping cart. Components need to “remember” things: the current input value, the current image, the shopping cart. In React, this kind of component-specific memory is called state.

Here’s a component that renders a sculpture image. Clicking the “Next” button should show the next sculpture by changing the index to 1, then 2, and so on. However, this won’t work (you can try it!):

The handleClick event handler is updating a local variable, index. But two things prevent that change from being visible:

To update a component with new data, two things need to happen:

The useState Hook provides those two things:

To add a state variable, import useState from React at the top of the file:

Then, replace this line:

index is a state variable and setIndex is the setter function.

The [ and ] syntax here is called array destructuring and it lets you read values from an array. The array returned by useState always has exactly two items.

This is how they work together in handleClick:

Now clicking the “Next” button switches the current sculpture:

In React, useState, as well as any other function starting with “use”, is called a Hook.

Hooks are special functions that are only available while React is rendering (which we’ll get into in more detail on the next page). They let you “hook into” different React features.

State is just one of those features, but you will meet the other Hooks later.

Hooks—functions starting with use—can only be called at the top level of your components or your own Hooks. You can’t call Hooks inside conditions, loops, or other nested functions. Hooks are functions, but it’s helpful to think of them as unconditional declarations about your component’s needs. You “use” React features at the top o

*[Content truncated - see full docs]*

**Examples**:

```python
import { useState } from 'react';
```

```javascript
let index = 0;
```

```javascript
const [index, setIndex] = useState(0);
```

---

## State as a Snapshot – React

**URL**: https://react.dev/learn/state-as-a-snapshot

**Contents**:
- State as a Snapshot
  - You will learn
- Setting state triggers renders
- Rendering takes a snapshot in time
- State over time
- Recap
- Try out some challenges
    - Challenge 1 of 1: Implement a traffic light

State variables might look like regular JavaScript variables that you can read and write to. However, state behaves more like a snapshot. Setting it does not change the state variable you already have, but instead triggers a re-render.

You might think of your user interface as changing directly in response to the user event like a click. In React, it works a little differently from this mental model. On the previous page, you saw that setting state requests a re-render from React. This means that for an interface to react to the event, you need to update the state.

In this example, when you press “send”, setIsSent(true) tells React to re-render the UI:

Here’s what happens when you click the button:

Let’s take a closer look at the relationship between state and rendering.

“Rendering” means that React is calling your component, which is a function. The JSX you return from that function is like a snapshot of the UI in time. Its props, event handlers, and local variables were all calculated using its state at the time of the render.

Unlike a photograph or a movie frame, the UI “snapshot” you return is interactive. It includes logic like event handlers that specify what happens in response to inputs. React updates the screen to match this snapshot and connects the event handlers. As a result, pressing a button will trigger the click handler from your JSX.

When React re-renders a component:

Illustrated by Rachel Lee Nabors

As a component’s memory, state is not like a regular variable that disappears after your function returns. State actually “lives” in React itself—as if on a shelf!—outside of your function. When React calls your component, it gives you a snapshot of the state for that particular render. Your component returns a snapshot of the UI with a fresh set of props and event handlers in its JSX, all calculated using the state values from that render!

Illustrated by Rachel Lee Nabors

Here’s a little experiment to show you how this works. In this example

*[Content truncated - see full docs]*

**Examples**:

```javascript
<button onClick={() => {  setNumber(number + 1);  setNumber(number + 1);  setNumber(number + 1);}}>+3</button>
```

```javascript
<button onClick={() => {  setNumber(0 + 1);  setNumber(0 + 1);  setNumber(0 + 1);}}>+3</button>
```

```javascript
<button onClick={() => {  setNumber(1 + 1);  setNumber(1 + 1);  setNumber(1 + 1);}}>+3</button>
```

---

## Synchronizing with Effects – React

**URL**: https://react.dev/learn/synchronizing-with-effects

**Contents**:
- Synchronizing with Effects
  - You will learn
- What are Effects and how are they different from events?
  - Note
- You might not need an Effect
- How to write an Effect
  - Step 1: Declare an Effect
  - Pitfall

Some components need to synchronize with external systems. For example, you might want to control a non-React component based on the React state, set up a server connection, or send an analytics log when a component appears on the screen. Effects let you run some code after rendering so that you can synchronize your component with some system outside of React.

Before getting to Effects, you need to be familiar with two types of logic inside React components:

Rendering code (introduced in Describing the UI) lives at the top level of your component. This is where you take the props and state, transform them, and return the JSX you want to see on the screen. Rendering code must be pure. Like a math formula, it should only calculate the result, but not do anything else.

Event handlers (introduced in Adding Interactivity) are nested functions inside your components that do things rather than just calculate them. An event handler might update an input field, submit an HTTP POST request to buy a product, or navigate the user to another screen. Event handlers contain “side effects” (they change the program’s state) caused by a specific user action (for example, a button click or typing).

Sometimes this isn’t enough. Consider a ChatRoom component that must connect to the chat server whenever it’s visible on the screen. Connecting to a server is not a pure calculation (it’s a side effect) so it can’t happen during rendering. However, there is no single particular event like a click that causes ChatRoom to be displayed.

Effects let you specify side effects that are caused by rendering itself, rather than by a particular event. Sending a message in the chat is an event because it is directly caused by the user clicking a specific button. However, setting up a server connection is an Effect because it should happen no matter which interaction caused the component to appear. Effects run at the end of a commit after the screen updates. This is a good time to synchronize the R

*[Content truncated - see full docs]*

**Examples**:

```python
import { useEffect } from 'react';
```

```javascript
function MyComponent() {  useEffect(() => {    // Code here will run after *every* render  });  return <div />;}
```

```text
<VideoPlayer isPlaying={isPlaying} />;
```

---

## Thinking in React – React

**URL**: https://react.dev/learn/thinking-in-react

**Contents**:
- Thinking in React
- Start with the mockup
- Step 1: Break the UI into a component hierarchy
- Step 2: Build a static version in React
  - Pitfall
- Step 3: Find the minimal but complete representation of UI state
      - Deep Dive
    - Props vs State

React can change how you think about the designs you look at and the apps you build. When you build a user interface with React, you will first break it apart into pieces called components. Then, you will describe the different visual states for each of your components. Finally, you will connect your components together so that the data flows through them. In this tutorial, we’ll guide you through the thought process of building a searchable product data table with React.

Imagine that you already have a JSON API and a mockup from a designer.

The JSON API returns some data that looks like this:

The mockup looks like this:

To implement a UI in React, you will usually follow the same five steps.

Start by drawing boxes around every component and subcomponent in the mockup and naming them. If you work with a designer, they may have already named these components in their design tool. Ask them!

Depending on your background, you can think about splitting up a design into components in different ways:

If your JSON is well-structured, you’ll often find that it naturally maps to the component structure of your UI. That’s because UI and data models often have the same information architecture—that is, the same shape. Separate your UI into components, where each component matches one piece of your data model.

There are five components on this screen:

If you look at ProductTable (lavender), you’ll see that the table header (containing the “Name” and “Price” labels) isn’t its own component. This is a matter of preference, and you could go either way. For this example, it is a part of ProductTable because it appears inside the ProductTable’s list. However, if this header grows to be complex (e.g., if you add sorting), you can move it into its own ProductTableHeader component.

Now that you’ve identified the components in the mockup, arrange them into a hierarchy. Components that appear within another component in the mockup should appear as a child in the hierarchy:

Now 

*[Content truncated - see full docs]*

**Examples**:

```text
[  { category: "Fruits", price: "$1", stocked: true, name: "Apple" },  { category: "Fruits", price: "$1", stocked: true, name: "Dragonfruit" },  { category: "Fruits", price: "$2", stocked: false, name: "Passionfruit" },  { category: "Vegetables", price: "$2", stocked: true, name: "Spinach" },  { category: "Vegetables", price: "$4", stocked: false, name: "Pumpkin" },  { category: "Vegetables", price: "$1", stocked: true, name: "Peas" }]
```

```javascript
function FilterableProductTable({ products }) {  const [filterText, setFilterText] = useState('');  const [inStockOnly, setInStockOnly] = useState(false);
```

```text
<div>  <SearchBar     filterText={filterText}     inStockOnly={inStockOnly} />  <ProductTable     products={products}    filterText={filterText}    inStockOnly={inStockOnly} /></div>
```

---

## Tutorial: Tic-Tac-Toe – React

**URL**: https://react.dev/learn/tutorial-tic-tac-toe

**Contents**:
- Tutorial: Tic-Tac-Toe
  - Note
  - What are you building?
- Setup for the tutorial
  - Note
- Overview
  - Inspecting the starter code
    - App.js

You will build a small tic-tac-toe game during this tutorial. This tutorial does not assume any existing React knowledge. The techniques you’ll learn in the tutorial are fundamental to building any React app, and fully understanding it will give you a deep understanding of React.

This tutorial is designed for people who prefer to learn by doing and want to quickly try making something tangible. If you prefer learning each concept step by step, start with Describing the UI.

The tutorial is divided into several sections:

In this tutorial, you’ll build an interactive tic-tac-toe game with React.

You can see what it will look like when you’re finished here:

If the code doesn’t make sense to you yet, or if you are unfamiliar with the code’s syntax, don’t worry! The goal of this tutorial is to help you understand React and its syntax.

We recommend that you check out the tic-tac-toe game above before continuing with the tutorial. One of the features that you’ll notice is that there is a numbered list to the right of the game’s board. This list gives you a history of all of the moves that have occurred in the game, and it is updated as the game progresses.

Once you’ve played around with the finished tic-tac-toe game, keep scrolling. You’ll start with a simpler template in this tutorial. Our next step is to set you up so that you can start building the game.

In the live code editor below, click Fork in the top-right corner to open the editor in a new tab using the website CodeSandbox. CodeSandbox lets you write code in your browser and preview how your users will see the app you’ve created. The new tab should display an empty square and the starter code for this tutorial.

You can also follow this tutorial using your local development environment. To do this, you need to:

If you get stuck, don’t let this stop you! Follow along online instead and try a local setup again later.

Now that you’re set up, let’s get an overview of React!

In CodeSandbox you’ll see three m

*[Content truncated - see full docs]*

**Examples**:

```javascript
export default function Square() {  return <button className="square">X</button>;}
```

```javascript
export default function Square() {  return <button className="square">X</button>;}
```

```javascript
export default function Square() {  return <button className="square">X</button>;}
```

---

## Understanding Your UI as a Tree – React

**URL**: https://react.dev/learn/understanding-your-ui-as-a-tree

**Contents**:
- Understanding Your UI as a Tree
  - You will learn
- Your UI as a tree
- The Render Tree
      - Deep Dive
    - Where are the HTML tags in the render tree?
- The Module Dependency Tree
- Recap

Your React app is taking shape with many components being nested within each other. How does React keep track of your app’s component structure?

React, and many other UI libraries, model UI as a tree. Thinking of your app as a tree is useful for understanding the relationship between components. This understanding will help you debug future concepts like performance and state management.

Trees are a relationship model between items. The UI is often represented using tree structures. For example, browsers use tree structures to model HTML (DOM) and CSS (CSSOM). Mobile platforms also use trees to represent their view hierarchy.

React creates a UI tree from your components. In this example, the UI tree is then used to render to the DOM.

Like browsers and mobile platforms, React also uses tree structures to manage and model the relationship between components in a React app. These trees are useful tools to understand how data flows through a React app and how to optimize rendering and app size.

A major feature of components is the ability to compose components of other components. As we nest components, we have the concept of parent and child components, where each parent component may itself be a child of another component.

When we render a React app, we can model this relationship in a tree, known as the render tree.

Here is a React app that renders inspirational quotes.

React creates a render tree, a UI tree, composed of the rendered components.

From the example app, we can construct the above render tree.

The tree is composed of nodes, each of which represents a component. App, FancyText, Copyright, to name a few, are all nodes in our tree.

The root node in a React render tree is the root component of the app. In this case, the root component is App and it is the first component React renders. Each arrow in the tree points from a parent component to a child component.

You’ll notice in the above render tree, there is no mention of the HTML tags that each 

*[Content truncated - see full docs]*

---

## Updating Arrays in State – React

**URL**: https://react.dev/learn/updating-arrays-in-state

**Contents**:
- Updating Arrays in State
  - You will learn
- Updating arrays without mutation
  - Pitfall
  - Adding to an array
  - Removing from an array
  - Transforming an array
  - Replacing items in an array

Arrays are mutable in JavaScript, but you should treat them as immutable when you store them in state. Just like with objects, when you want to update an array stored in state, you need to create a new one (or make a copy of an existing one), and then set state to use the new array.

In JavaScript, arrays are just another kind of object. Like with objects, you should treat arrays in React state as read-only. This means that you shouldn’t reassign items inside an array like arr[0] = 'bird', and you also shouldn’t use methods that mutate the array, such as push() and pop().

Instead, every time you want to update an array, you’ll want to pass a new array to your state setting function. To do that, you can create a new array from the original array in your state by calling its non-mutating methods like filter() and map(). Then you can set your state to the resulting new array.

Here is a reference table of common array operations. When dealing with arrays inside React state, you will need to avoid the methods in the left column, and instead prefer the methods in the right column:

Alternatively, you can use Immer which lets you use methods from both columns.

Unfortunately, slice and splice are named similarly but are very different:

In React, you will be using slice (no p!) a lot more often because you don’t want to mutate objects or arrays in state. Updating Objects explains what mutation is and why it’s not recommended for state.

push() will mutate an array, which you don’t want:

Instead, create a new array which contains the existing items and a new item at the end. There are multiple ways to do this, but the easiest one is to use the ... array spread syntax:

Now it works correctly:

The array spread syntax also lets you prepend an item by placing it before the original ...artists:

In this way, spread can do the job of both push() by adding to the end of an array and unshift() by adding to the beginning of an array. Try it in the sandbox above!

The easiest wa

*[Content truncated - see full docs]*

**Examples**:

```text
setArtists( // Replace the state  [ // with a new array    ...artists, // that contains all the old items    { id: nextId++, name: name } // and one new item at the end  ]);
```

```text
setArtists([  { id: nextId++, name: name },  ...artists // Put old items at the end]);
```

```javascript
setArtists(  artists.filter(a => a.id !== artist.id));
```

---

## Updating Objects in State – React

**URL**: https://react.dev/learn/updating-objects-in-state

**Contents**:
- Updating Objects in State
  - You will learn
- What’s a mutation?
- Treat state as read-only
      - Deep Dive
    - Local mutation is fine
- Copying objects with the spread syntax
      - Deep Dive

State can hold any kind of JavaScript value, including objects. But you shouldn’t change objects that you hold in the React state directly. Instead, when you want to update an object, you need to create a new one (or make a copy of an existing one), and then set the state to use that copy.

You can store any kind of JavaScript value in state.

So far you’ve been working with numbers, strings, and booleans. These kinds of JavaScript values are “immutable”, meaning unchangeable or “read-only”. You can trigger a re-render to replace a value:

The x state changed from 0 to 5, but the number 0 itself did not change. It’s not possible to make any changes to the built-in primitive values like numbers, strings, and booleans in JavaScript.

Now consider an object in state:

Technically, it is possible to change the contents of the object itself. This is called a mutation:

However, although objects in React state are technically mutable, you should treat them as if they were immutable—like numbers, booleans, and strings. Instead of mutating them, you should always replace them.

In other words, you should treat any JavaScript object that you put into state as read-only.

This example holds an object in state to represent the current pointer position. The red dot is supposed to move when you touch or move the cursor over the preview area. But the dot stays in the initial position:

The problem is with this bit of code.

This code modifies the object assigned to position from the previous render. But without using the state setting function, React has no idea that object has changed. So React does not do anything in response. It’s like trying to change the order after you’ve already eaten the meal. While mutating state can work in some cases, we don’t recommend it. You should treat the state value you have access to in a render as read-only.

To actually trigger a re-render in this case, create a new object and pass it to the state setting function:

With setPosition, you’re t

*[Content truncated - see full docs]*

**Examples**:

```javascript
const [x, setX] = useState(0);
```

```javascript
const [position, setPosition] = useState({ x: 0, y: 0 });
```

```text
position.x = 5;
```

---

## Writing Markup with JSX – React

**URL**: https://react.dev/learn/writing-markup-with-jsx

**Contents**:
- Writing Markup with JSX
  - You will learn
- JSX: Putting markup into JavaScript
  - Note
- Converting HTML to JSX
  - Note
- The Rules of JSX
  - 1. Return a single root element

JSX is a syntax extension for JavaScript that lets you write HTML-like markup inside a JavaScript file. Although there are other ways to write components, most React developers prefer the conciseness of JSX, and most codebases use it.

The Web has been built on HTML, CSS, and JavaScript. For many years, web developers kept content in HTML, design in CSS, and logic in JavaScript—often in separate files! Content was marked up inside HTML while the page’s logic lived separately in JavaScript:

But as the Web became more interactive, logic increasingly determined content. JavaScript was in charge of the HTML! This is why in React, rendering logic and markup live together in the same place—components.

Sidebar.js React component

Form.js React component

Keeping a button’s rendering logic and markup together ensures that they stay in sync with each other on every edit. Conversely, details that are unrelated, such as the button’s markup and a sidebar’s markup, are isolated from each other, making it safer to change either of them on their own.

Each React component is a JavaScript function that may contain some markup that React renders into the browser. React components use a syntax extension called JSX to represent that markup. JSX looks a lot like HTML, but it is a bit stricter and can display dynamic information. The best way to understand this is to convert some HTML markup to JSX markup.

JSX and React are two separate things. They’re often used together, but you can use them independently of each other. JSX is a syntax extension, while React is a JavaScript library.

Suppose that you have some (perfectly valid) HTML:

And you want to put it into your component:

If you copy and paste it as is, it will not work:

This is because JSX is stricter and has a few more rules than HTML! If you read the error messages above, they’ll guide you to fix the markup, or you can follow the guide below.

Most of the time, React’s on-screen error messages will help you find where th

*[Content truncated - see full docs]*

**Examples**:

```text
<h1>Hedy Lamarr's Todos</h1><img   src="https://i.imgur.com/yXOvdOSs.jpg"   alt="Hedy Lamarr"   class="photo"><ul>    <li>Invent new traffic lights    <li>Rehearse a movie scene    <li>Improve the spectrum technology</ul>
```

```javascript
export default function TodoList() {  return (    // ???  )}
```

```text
<div>  <h1>Hedy Lamarr's Todos</h1>  <img     src="https://i.imgur.com/yXOvdOSs.jpg"     alt="Hedy Lamarr"     class="photo"  >  <ul>    ...  </ul></div>
```

---

## You Might Not Need an Effect – React

**URL**: https://react.dev/learn/you-might-not-need-an-effect

**Contents**:
- You Might Not Need an Effect
  - You will learn
- How to remove unnecessary Effects
  - Updating state based on props or state
  - Caching expensive calculations
  - Note
      - Deep Dive
    - How to tell if a calculation is expensive?

Effects are an escape hatch from the React paradigm. They let you “step outside” of React and synchronize your components with some external system like a non-React widget, network, or the browser DOM. If there is no external system involved (for example, if you want to update a component’s state when some props or state change), you shouldn’t need an Effect. Removing unnecessary Effects will make your code easier to follow, faster to run, and less error-prone.

There are two common cases in which you don’t need Effects:

You do need Effects to synchronize with external systems. For example, you can write an Effect that keeps a jQuery widget synchronized with the React state. You can also fetch data with Effects: for example, you can synchronize the search results with the current search query. Keep in mind that modern frameworks provide more efficient built-in data fetching mechanisms than writing Effects directly in your components.

To help you gain the right intuition, let’s look at some common concrete examples!

Suppose you have a component with two state variables: firstName and lastName. You want to calculate a fullName from them by concatenating them. Moreover, you’d like fullName to update whenever firstName or lastName change. Your first instinct might be to add a fullName state variable and update it in an Effect:

This is more complicated than necessary. It is inefficient too: it does an entire render pass with a stale value for fullName, then immediately re-renders with the updated value. Remove the state variable and the Effect:

When something can be calculated from the existing props or state, don’t put it in state. Instead, calculate it during rendering. This makes your code faster (you avoid the extra “cascading” updates), simpler (you remove some code), and less error-prone (you avoid bugs caused by different state variables getting out of sync with each other). If this approach feels new to you, Thinking in React explains what should go into sta

*[Content truncated - see full docs]*

**Examples**:

```javascript
function Form() {  const [firstName, setFirstName] = useState('Taylor');  const [lastName, setLastName] = useState('Swift');  // 🔴 Avoid: redundant state and unnecessary Effect  const [fullName, setFullName] = useState('');  useEffect(() => {    setFullName(firstName + ' ' + lastName);  }, [firstName, lastName]);  // ...}
```

```javascript
function Form() {  const [firstName, setFirstName] = useState('Taylor');  const [lastName, setLastName] = useState('Swift');  // ✅ Good: calculated during rendering  const fullName = firstName + ' ' + lastName;  // ...}
```

```javascript
function TodoList({ todos, filter }) {  const [newTodo, setNewTodo] = useState('');  // 🔴 Avoid: redundant state and unnecessary Effect  const [visibleTodos, setVisibleTodos] = useState([]);  useEffect(() => {    setVisibleTodos(getFilteredTodos(todos, filter));  }, [todos, filter]);  // ...}
```

---

## Your First Component – React

**URL**: https://react.dev/learn/your-first-component

**Contents**:
- Your First Component
  - You will learn
- Components: UI building blocks
- Defining a component
  - Step 1: Export the component
  - Step 2: Define the function
  - Pitfall
  - Step 3: Add markup

Components are one of the core concepts of React. They are the foundation upon which you build user interfaces (UI), which makes them the perfect place to start your React journey!

On the Web, HTML lets us create rich structured documents with its built-in set of tags like <h1> and <li>:

This markup represents this article <article>, its heading <h1>, and an (abbreviated) table of contents as an ordered list <ol>. Markup like this, combined with CSS for style, and JavaScript for interactivity, lies behind every sidebar, avatar, modal, dropdown—every piece of UI you see on the Web.

React lets you combine your markup, CSS, and JavaScript into custom “components”, reusable UI elements for your app. The table of contents code you saw above could be turned into a <TableOfContents /> component you could render on every page. Under the hood, it still uses the same HTML tags like <article>, <h1>, etc.

Just like with HTML tags, you can compose, order and nest components to design whole pages. For example, the documentation page you’re reading is made out of React components:

As your project grows, you will notice that many of your designs can be composed by reusing components you already wrote, speeding up your development. Our table of contents above could be added to any screen with <TableOfContents />! You can even jumpstart your project with the thousands of components shared by the React open source community like Chakra UI and Material UI.

Traditionally when creating web pages, web developers marked up their content and then added interaction by sprinkling on some JavaScript. This worked great when interaction was a nice-to-have on the web. Now it is expected for many sites and all apps. React puts interactivity first while still using the same technology: a React component is a JavaScript function that you can sprinkle with markup. Here’s what that looks like (you can edit the example below):

And here’s how to build a component:

The export default prefix is a 

*[Content truncated - see full docs]*

**Examples**:

```text
<article>  <h1>My First Component</h1>  <ol>    <li>Components: UI Building Blocks</li>    <li>Defining a Component</li>    <li>Using a Component</li>  </ol></article>
```

```text
<PageLayout>  <NavigationHeader>    <SearchBar />    <Link to="/docs">Docs</Link>  </NavigationHeader>  <Sidebar />  <PageContent>    <TableOfContents />    <DocumentationText />  </PageContent></PageLayout>
```

```text
return <img src="https://i.imgur.com/MK3eW3As.jpg" alt="Katherine Johnson" />;
```

---
