# Typescript - Getting Started

**Pages**: 121

---

## ASP.NET Core

**URL**: https://www.typescriptlang.org/docs/handbook/asp-net-core.html

**Contents**:
- ASP.NET Core
- Install ASP.NET Core and TypeScript
- Create a new project
  - Set up the server
- Add TypeScript
- Add TypeScript code
  - Add example code
- Set up the build

Was this page helpful?

First, install ASP.NET Core if you need it. This quick-start guide requires Visual Studio 2015 or 2017.

Next, if your version of Visual Studio does not already have the latest TypeScript, you can install it.

Run the application and make sure that it works.

Open Dependencies > Manage NuGet Packages > Browse. Search and install Microsoft.AspNetCore.StaticFiles and Microsoft.TypeScript.MSBuild:

Open up your Startup.cs file and edit your Configure function to look like this:

You may need to restart VS for the red squiggly lines below UseDefaultFiles and UseStaticFiles to disappear.

Next we will add a new folder and call it scripts.

Right click on scripts and click New Item. Then choose TypeScript File and name the file app.ts

Add the following code to the app.ts file.

Configure the TypeScript compiler

First we need to tell TypeScript how to build. Right click on scripts and click New Item. Then choose TypeScript Configuration File and use the default name of tsconfig.json

Replace the contents of the tsconfig.json file with:

Note: "ESNext" targets latest supported

noImplicitAny is good idea whenever you’re writing new code — you can make sure that you don’t write any untyped code by mistake. "compileOnSave" makes it easy to update your code in a running web app.

We need to setup NPM so that JavaScript packages can be downloaded. Right click on the project and select New Item. Then choose NPM Configuration File and use the default name of package.json.

Inside the "devDependencies" section of the package.json file, add gulp and del

Visual Studio should start installing gulp and del as soon as you save the file. If not, right-click package.json and then Restore Packages.

After you should see an npm folder in your solution explorer

Right click on the project and click New Item. Then choose JavaScript File and use the name of gulpfile.js

The first line tells Visual Studio to run the task ‘default’ after the build finishes. It will al

*[Content truncated - see full docs]*

**Examples**:

```text
public void Configure(IApplicationBuilder app, IHostEnvironment env)
{
    if (env.IsDevelopment())
    {
        app.UseDeveloperExceptionPage();
    }

    app.UseDefaultFiles();
    app.UseStaticFiles();
}
```

```javascript
function sayHello() {  const compiler = (document.getElementById("compiler") as HTMLInputElement)    .value;  const framework = (document.getElementById("framework") as HTMLInputElement)    .value;  return `Hello from ${compiler} and ${framework}!`;}
```

```text
{  "compilerOptions": {    "noEmitOnError": true,    "noImplicitAny": true,    "sourceMap": true,    "target": "es6"  },  "files": ["./app.ts"],  "compileOnSave": true}
```

---

## Classes

**URL**: https://www.typescriptlang.org/docs/handbook/2/classes.html

**Contents**:
- Classes
- Class Members
  - Fields
    - --strictPropertyInitialization
  - readonly
  - Constructors
    - Super Calls
  - Methods

Was this page helpful?

Background Reading:Classes (MDN)

TypeScript offers full support for the class keyword introduced in ES2015.

As with other JavaScript language features, TypeScript adds type annotations and other syntax to allow you to express relationships between classes and other types.

Here’s the most basic class - an empty one:

This class isn’t very useful yet, so let’s start adding some members.

A field declaration creates a public writeable property on a class:

As with other locations, the type annotation is optional, but will be an implicit any if not specified.

Fields can also have initializers; these will run automatically when the class is instantiated:

Just like with const, let, and var, the initializer of a class property will be used to infer its type:

The strictPropertyInitialization setting controls whether class fields need to be initialized in the constructor.

Note that the field needs to be initialized in the constructor itself. TypeScript does not analyze methods you invoke from the constructor to detect initializations, because a derived class might override those methods and fail to initialize the members.

If you intend to definitely initialize a field through means other than the constructor (for example, maybe an external library is filling in part of your class for you), you can use the definite assignment assertion operator, !:

Fields may be prefixed with the readonly modifier. This prevents assignments to the field outside of the constructor.

Background Reading: Constructor (MDN)

Class constructors are very similar to functions. You can add parameters with type annotations, default values, and overloads:

There are just a few differences between class constructor signatures and function signatures:

Just as in JavaScript, if you have a base class, you’ll need to call super(); in your constructor body before using any this. members:

Forgetting to call super is an easy mistake to make in JavaScript, but TypeScript will t

*[Content truncated - see full docs]*

**Examples**:

```text
class Point {}
```

```javascript
class Point {  x: number;  y: number;} const pt = new Point();pt.x = 0;pt.y = 0;
```

```javascript
class Point {  x = 0;  y = 0;} const pt = new Point();// Prints 0, 0console.log(`${pt.x}, ${pt.y}`);
```

---

## Compiler Options in MSBuild

**URL**: https://www.typescriptlang.org/docs/handbook/compiler-options-in-msbuild.html

**Contents**:
- Compiler Options in MSBuild
- Overview
- Using a tsconfig.json
- Using Project Settings
  - CLI Mappings
  - Additional Flags
  - Debug and Release Builds
  - ToolsVersion

Was this page helpful?

When you have an MSBuild based project which utilizes TypeScript such as an ASP.NET Core project, you can configure TypeScript in two ways. Either via a tsconfig.json or via the project settings.

We recommend using a tsconfig.json for your project when possible. To add one to an existing project, add a new item to your project which is called a “TypeScript JSON Configuration File” in modern versions of Visual Studio.

The new tsconfig.json will then be used as the source of truth for TypeScript-specific build information like files and configuration. You can learn about how TSConfigs works here and there is a comprehensive reference here.

You can also define the configuration for TypeScript inside you project’s settings. This is done by editing the XML in your .csproj to define PropertyGroups which describe how the build can work:

There is a series of mappings for common TypeScript settings, these are settings which map directly to TypeScript cli options and are used to help you write a more understandable project file. You can use the TSConfig reference to get more information on what values and defaults are for each mapping.

Allow JavaScript files to be a part of your program. Use the checkJS option to get errors from these files.

Disable emitting comments.

Enable error reporting for expressions and declarations with an implied any type..

Generate .d.ts files from TypeScript and JavaScript files in your project.

Specify what module code is generated.

Specify what JSX code is generated.

Specify an output folder for all emitted files.

Create source map files for emitted JavaScript files.

Set the JavaScript language version for emitted JavaScript and include compatible library declarations.

Disallow imports, requires or <reference>s from expanding the number of files TypeScript should add to a project.

Specify the location where debugger should locate map files instead of generated locations.

Specify the root path for debuggers 

*[Content truncated - see full docs]*

**Examples**:

```text
<PropertyGroup>  <TypeScriptNoEmitOnError>true</TypeScriptNoEmitOnError>  <TypeScriptNoImplicitReturns>true</TypeScriptNoImplicitReturns></PropertyGroup>
```

```text
<TypeScriptAdditionalFlags> $(TypeScriptAdditionalFlags) --noPropertyAccessFromIndexSignature</TypeScriptAdditionalFlags>
```

```text
<PropertyGroup Condition="'$(Configuration)' == 'Debug'">  <TypeScriptRemoveComments>false</TypeScriptRemoveComments>  <TypeScriptSourceMap>true</TypeScriptSourceMap></PropertyGroup><PropertyGroup Condition="'$(Configuration)' == 'Release'">  <TypeScriptRemoveComments>true</TypeScriptRemoveComments>  <TypeScriptSourceMap>false</TypeScriptSourceMap></PropertyGroup><Import    Project="$(MSBuildExtensionsPath32)\Microsoft\VisualStudio\v$(VisualStudioVersion)\TypeScript\Microsoft.TypeScript.targets"
...
```

---

## Conditional Types

**URL**: https://www.typescriptlang.org/docs/handbook/2/conditional-types.html

**Contents**:
- Conditional Types
  - Conditional Type Constraints
  - Inferring Within Conditional Types
- Distributive Conditional Types
      - On this page
      - Is this page helpful?
  - Indexed Access Types
  - Mapped Types

Was this page helpful?

At the heart of most useful programs, we have to make decisions based on input. JavaScript programs are no different, but given the fact that values can be easily introspected, those decisions are also based on the types of the inputs. Conditional types help describe the relation between the types of inputs and outputs.

Conditional types take a form that looks a little like conditional expressions (condition ? trueExpression : falseExpression) in JavaScript:

When the type on the left of the extends is assignable to the one on the right, then you’ll get the type in the first branch (the “true” branch); otherwise you’ll get the type in the latter branch (the “false” branch).

From the examples above, conditional types might not immediately seem useful - we can tell ourselves whether or not Dog extends Animal and pick number or string! But the power of conditional types comes from using them with generics.

For example, let’s take the following createLabel function:

These overloads for createLabel describe a single JavaScript function that makes a choice based on the types of its inputs. Note a few things:

Instead, we can encode that logic in a conditional type:

We can then use that conditional type to simplify our overloads down to a single function with no overloads.

Often, the checks in a conditional type will provide us with some new information. Just like narrowing with type guards can give us a more specific type, the true branch of a conditional type will further constrain generics by the type we check against.

For example, let’s take the following:

In this example, TypeScript errors because T isn’t known to have a property called message. We could constrain T, and TypeScript would no longer complain:

However, what if we wanted MessageOf to take any type, and default to something like never if a message property isn’t available? We can do this by moving the constraint out and introducing a conditional type:

Within the true branc

*[Content truncated - see full docs]*

**Examples**:

```text
interface Animal {  live(): void;}interface Dog extends Animal {  woof(): void;} type Example1 = Dog extends Animal ? number : string;        type Example1 = number type Example2 = RegExp extends Animal ? number : string;        type Example2 = string
```

```text
SomeType extends OtherType ? TrueType : FalseType;
```

```javascript
interface IdLabel {  id: number /* some fields */;}interface NameLabel {  name: string /* other fields */;} function createLabel(id: number): IdLabel;function createLabel(name: string): NameLabel;function createLabel(nameOrId: string | number): IdLabel | NameLabel;function createLabel(nameOrId: string | number): IdLabel | NameLabel {  throw "unimplemented";}
```

---

## Configuring Watch

**URL**: https://www.typescriptlang.org/docs/handbook/configuring-watch.html

**Contents**:
- Configuring Watch
- Background
- Configuring file watching using a tsconfig.json
- Configuring file watching using environment variable TSC_WATCHFILE
- Configuring directory watching using environment variable TSC_WATCHDIRECTORY
      - On this page
      - Is this page helpful?

Was this page helpful?

As of TypeScript 3.8 and onward, the Typescript compiler exposes configuration which controls how it watches files and directories. Prior to this version, configuration required the use of environment variables which are still available.

The --watch implementation of the compiler relies on Node’s fs.watch and fs.watchFile. Each of these methods has pros and cons.

fs.watch relies on file system events to broadcast changes in the watched files and directories. The implementation of this command is OS dependent and unreliable - on many operating systems, it does not work as expected. Additionally, some operating systems limit the number of watches which can exist simultaneously (e.g. some flavors of Linux). Heavy use of fs.watch in large codebases has the potential to exceed these limits and result in undesirable behavior. However, because this implementation relies on an events-based model, CPU use is comparatively light. The compiler typically uses fs.watch to watch directories (e.g. source directories included by compiler configuration files and directories in which module resolution failed, among others). TypeScript uses these to augment potential failures in individual file watchers. However, there is a key limitation of this strategy: recursive watching of directories is supported on Windows and macOS, but not on Linux. This suggested a need for additional strategies for file and directory watching.

fs.watchFile uses polling and thus costs CPU cycles. However, fs.watchFile is by far the most reliable mechanism available to subscribe to the events from files and directories of interest. Under this strategy, the TypeScript compiler typically uses fs.watchFile to watch source files, config files, and files which appear missing based on reference statements. This means that the degree to which CPU usage will be higher when using fs.watchFile depends directly on number of files watched in the codebase.

The suggested method of configuring wa

*[Content truncated - see full docs]*

**Examples**:

```text
{  // Some typical compiler options  "compilerOptions": {    "target": "es2020",    "moduleResolution": "node"    // ...  },  // NEW: Options for file/directory watching  "watchOptions": {    // Use native file system events for files and directories    "watchFile": "useFsEvents",    "watchDirectory": "useFsEvents",    // Poll files for updates more frequently    // when they're updated a lot.    "fallbackPolling": "dynamicPriority",    // Don't coalesce watch notification    "synchronousWatchDi
...
```

---

## Consumption

**URL**: https://www.typescriptlang.org/docs/handbook/declaration-files/consumption.html

**Contents**:
- Consumption
- Downloading
- Consuming
- Searching
      - On this page
      - Is this page helpful?
  - Publishing

Was this page helpful?

Getting type declarations requires no tools apart from npm.

As an example, getting the declarations for a library like lodash takes nothing more than the following command

It is worth noting that if the npm package already includes its declaration file as described in Publishing, downloading the corresponding @types package is not needed.

From there you’ll be able to use lodash in your TypeScript code with no fuss. This works for both modules and global code.

For example, once you’ve npm install-ed your type declarations, you can use imports and write

or if you’re not using modules, you can just use the global variable _.

For the most part, type declaration packages should always have the same name as the package name on npm, but prefixed with @types/, but if you need, you can use the Yarn package search to find the package for your favorite library.

Note: if the declaration file you are searching for is not present, you can always contribute one back and help out the next developer looking for it. Please see the DefinitelyTyped contribution guidelines page for details.

How to get your d.ts files to users

The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤

Last updated: Oct 13, 2025

**Examples**:

```text
npm install --save-dev @types/lodash
```

```python
import * as _ from "lodash";_.padStart("Hello TypeScript!", 20, " ");
```

```text
_.padStart("Hello TypeScript!", 20, " ");
```

---

## Creating Types from Types

**URL**: https://www.typescriptlang.org/docs/handbook/2/types-from-types.html

**Contents**:
- Creating Types from Types
      - On this page
      - Is this page helpful?
  - Generics

Was this page helpful?

TypeScript’s type system is very powerful because it allows expressing types in terms of other types.

The simplest form of this idea is generics. Additionally, we have a wide variety of type operators available to use. It’s also possible to express types in terms of values that we already have.

By combining various type operators, we can express complex operations and values in a succinct, maintainable way. In this section we’ll cover ways to express a new type in terms of an existing type or value.

Types which take parameters

The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤

Last updated: Oct 13, 2025

---

## Creating .d.ts Files from .js files

**URL**: https://www.typescriptlang.org/docs/handbook/declaration-files/dts-from-js.html

**Contents**:
- Creating .d.ts Files from .js files
- Setting up your Project to emit .d.ts files
  - Adding TypeScript
  - TSConfig
- Run the compiler
- Editing the package.json
- Tips
      - On this page

Was this page helpful?

With TypeScript 3.7, TypeScript added support for generating .d.ts files from JavaScript using JSDoc syntax.

This set up means you can own the editor experience of TypeScript-powered editors without porting your project to TypeScript, or having to maintain .d.ts files in your codebase. TypeScript supports most JSDoc tags, you can find the reference here.

To add creation of .d.ts files in your project, you will need to do up-to four steps:

You can learn how to do this in our installation page.

The TSConfig is a jsonc file which configures both your compiler flags, and declare where to find files. In this case, you will want a file like the following:

You can learn more about the options in the tsconfig reference. An alternative to using a TSConfig file is the CLI, this is the same behavior as a CLI command.

You can learn how to do this in our installation page. You want to make sure these files are included in your package if you have the files in your project’s .gitignore.

TypeScript replicates the node resolution for modules in a package.json, with an additional step for finding .d.ts files. Roughly, the resolution will first check the optional types field, then the "main" field, and finally will try index.d.ts in the root.

If absent, then “main” is used

If you’d like to write tests for your .d.ts files, try tsd or TSTyche.

What JSDoc does TypeScript-powered JavaScript support?

The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤

Last updated: Oct 13, 2025

**Examples**:

```javascript
{  // Change this to match your project  "include": ["src/**/*"],  "compilerOptions": {    // Tells TypeScript to read JS files, as    // normally they are ignored as source files    "allowJs": true,    // Generate d.ts files    "declaration": true,    // This compiler run should    // only output d.ts files    "emitDeclarationOnly": true,    // Types should go into this directory.    // Removing this would place the .d.ts files    // next to the .js files    "outDir": "dist",    // go to js fil
...
```

```text
npx -p typescript tsc src/**/*.js --declaration --allowJs --emitDeclarationOnly --outDir types
```

---

## DOM Manipulation

**URL**: https://www.typescriptlang.org/docs/handbook/dom-manipulation.html

**Contents**:
- DOM Manipulation
- DOM Manipulation
  - An exploration into the HTMLElement type
- Basic Example
- The Document Interface
  - Document.getElementById
  - Document.createElement
- The Node interface

Was this page helpful?

In the 20+ years since its standardization, JavaScript has come a very long way. While in 2020, JavaScript can be used on servers, in data science, and even on IoT devices, it is important to remember its most popular use case: web browsers.

Websites are made up of HTML and/or XML documents. These documents are static, they do not change. The Document Object Model (DOM) is a programming interface implemented by browsers to make static websites functional. The DOM API can be used to change the document structure, style, and content. The API is so powerful that countless frontend frameworks (jQuery, React, Angular, etc.) have been developed around it to make dynamic websites even easier to develop.

TypeScript is a typed superset of JavaScript, and it ships type definitions for the DOM API. These definitions are readily available in any default TypeScript project. Of the 20,000+ lines of definitions in lib.dom.d.ts, one stands out among the rest: HTMLElement. This type is the backbone for DOM manipulation with TypeScript.

You can explore the source code for the DOM type definitions

Given a simplified index.html file:

Let’s explore a TypeScript script that adds a <p>Hello, World!</p> element to the #app element.

After compiling and running the index.html page, the resulting HTML will be:

The first line of the TypeScript code uses a global variable document. Inspecting the variable shows it is defined by the Document interface from the lib.dom.d.ts file. The code snippet contains calls to two methods, getElementById and createElement.

The definition for this method is as follows:

Pass it an element id string and it will return either HTMLElement or null. This method introduces one of the most important types, HTMLElement. It serves as the base interface for every other element interface. For example, the p variable in the code example is of type HTMLParagraphElement. Also, take note that this method can return null. This is because the me

*[Content truncated - see full docs]*

**Examples**:

```text
<!DOCTYPE html><html lang="en">  <head><title>TypeScript Dom Manipulation</title></head>  <body>    <div id="app"></div>    <!-- Assume index.js is the compiled output of index.ts -->    <script src="index.js"></script>  </body></html>
```

```javascript
// 1. Select the div element using the id propertyconst app = document.getElementById("app");// 2. Create a new <p></p> element programmaticallyconst p = document.createElement("p");// 3. Add the text contentp.textContent = "Hello, World!";// 4. Append the p element to the div elementapp?.appendChild(p);
```

```text
<div id="app">  <p>Hello, World!</p></div>
```

---

## Declaration Merging

**URL**: https://www.typescriptlang.org/docs/handbook/declaration-merging.html

**Contents**:
- Declaration Merging
- Introduction
- Basic Concepts
- Merging Interfaces
- Merging Namespaces
- Merging Namespaces with Classes, Functions, and Enums
  - Merging Namespaces with Classes
- Disallowed Merges

Was this page helpful?

Some of the unique concepts in TypeScript describe the shape of JavaScript objects at the type level. One example that is especially unique to TypeScript is the concept of ‘declaration merging’. Understanding this concept will give you an advantage when working with existing JavaScript. It also opens the door to more advanced abstraction concepts.

For the purposes of this article, “declaration merging” means that the compiler merges two separate declarations declared with the same name into a single definition. This merged definition has the features of both of the original declarations. Any number of declarations can be merged; it’s not limited to just two declarations.

In TypeScript, a declaration creates entities in at least one of three groups: namespace, type, or value. Namespace-creating declarations create a namespace, which contains names that are accessed using a dotted notation. Type-creating declarations do just that: they create a type that is visible with the declared shape and bound to the given name. Lastly, value-creating declarations create values that are visible in the output JavaScript.

Understanding what is created with each declaration will help you understand what is merged when you perform a declaration merge.

The simplest, and perhaps most common, type of declaration merging is interface merging. At the most basic level, the merge mechanically joins the members of both declarations into a single interface with the same name.

Non-function members of the interfaces should be unique. If they are not unique, they must be of the same type. The compiler will issue an error if the interfaces both declare a non-function member of the same name, but of different types.

For function members, each function member of the same name is treated as describing an overload of the same function. Of note, too, is that in the case of interface A merging with later interface A, the second interface will have a higher precedence than 

*[Content truncated - see full docs]*

**Examples**:

```javascript
interface Box {  height: number;  width: number;}interface Box {  scale: number;}let box: Box = { height: 5, width: 6, scale: 10 };
```

```text
interface Cloner {  clone(animal: Animal): Animal;}interface Cloner {  clone(animal: Sheep): Sheep;}interface Cloner {  clone(animal: Dog): Dog;  clone(animal: Cat): Cat;}
```

```text
interface Cloner {  clone(animal: Dog): Dog;  clone(animal: Cat): Cat;  clone(animal: Sheep): Sheep;  clone(animal: Animal): Animal;}
```

---

## Declaration Reference

**URL**: https://www.typescriptlang.org/docs/handbook/declaration-files/by-example.html

**Contents**:
- Declaration Reference
- Objects with Properties
- Overloaded Functions
- Reusable Types (Interfaces)
- Reusable Types (Type Aliases)
- Organizing Types
- Classes
- Global Variables

Was this page helpful?

The purpose of this guide is to teach you how to write a high-quality definition file. This guide is structured by showing documentation for some API, along with sample usage of that API, and explaining how to write the corresponding declaration.

These examples are ordered in approximately increasing order of complexity.

The global variable myLib has a function makeGreeting for creating greetings, and a property numberOfGreetings indicating the number of greetings made so far.

Use declare namespace to describe types or values accessed by dotted notation.

The getWidget function accepts a number and returns a Widget, or accepts a string and returns a Widget array.

When specifying a greeting, you must pass a GreetingSettings object. This object has the following properties:

1 - greeting: Mandatory string

2 - duration: Optional length of time (in milliseconds)

3 - color: Optional string, e.g. ‘#ff00ff’

Use an interface to define a type with properties.

Anywhere a greeting is expected, you can provide a string, a function returning a string, or a Greeter instance.

You can use a type alias to make a shorthand for a type:

The greeter object can log to a file or display an alert. You can provide LogOptions to .log(...) and alert options to .alert(...)

Use namespaces to organize types.

You can also create nested namespaces in one declaration:

You can create a greeter by instantiating the Greeter object, or create a customized greeter by extending from it.

Use declare class to describe a class or class-like object. Classes can have properties and methods as well as a constructor.

The global variable foo contains the number of widgets present.

Use declare var to declare variables. If the variable is read-only, you can use declare const. You can also use declare let if the variable is block-scoped.

You can call the function greet with a string to show a greeting to the user.

Use declare function to declare functions.

How to write a h

*[Content truncated - see full docs]*

**Examples**:

```javascript
let result = myLib.makeGreeting("hello, world");console.log("The computed greeting is:" + result);let count = myLib.numberOfGreetings;
```

```javascript
declare namespace myLib {  function makeGreeting(s: string): string;  let numberOfGreetings: number;}
```

```javascript
let x: Widget = getWidget(43);let arr: Widget[] = getWidget("all of them");
```

---

## Decorators

**URL**: https://www.typescriptlang.org/docs/handbook/decorators.html

**Contents**:
- Decorators
- Introduction
- Decorators
- Decorator Factories
- Decorator Composition
- Decorator Evaluation
- Class Decorators
- Method Decorators

Was this page helpful?

NOTE This document refers to an experimental stage 2 decorators implementation. Stage 3 decorator support is available since Typescript 5.0. See: Decorators in Typescript 5.0

With the introduction of Classes in TypeScript and ES6, there now exist certain scenarios that require additional features to support annotating or modifying classes and class members. Decorators provide a way to add both annotations and a meta-programming syntax for class declarations and members.

Further Reading (stage 2): A Complete Guide to TypeScript Decorators

To enable experimental support for decorators, you must enable the experimentalDecorators compiler option either on the command line or in your tsconfig.json:

A Decorator is a special kind of declaration that can be attached to a class declaration, method, accessor, property, or parameter. Decorators use the form @expression, where expression must evaluate to a function that will be called at runtime with information about the decorated declaration.

For example, given the decorator @sealed we might write the sealed function as follows:

If we want to customize how a decorator is applied to a declaration, we can write a decorator factory. A Decorator Factory is simply a function that returns the expression that will be called by the decorator at runtime.

We can write a decorator factory in the following fashion:

Multiple decorators can be applied to a declaration, for example on a single line:

When multiple decorators apply to a single declaration, their evaluation is similar to function composition in mathematics. In this model, when composing functions f and g, the resulting composite (f ∘ g)(x) is equivalent to f(g(x)).

As such, the following steps are performed when evaluating multiple decorators on a single declaration in TypeScript:

If we were to use decorator factories, we can observe this evaluation order with the following example:

Which would print this output to the console:

There is a w

*[Content truncated - see full docs]*

**Examples**:

```text
tsc --target ES5 --experimentalDecorators
```

```text
{  "compilerOptions": {    "target": "ES5",    "experimentalDecorators": true  }}
```

```javascript
function sealed(target) {  // do something with 'target' ...}
```

---

## Deep Dive

**URL**: https://www.typescriptlang.org/docs/handbook/declaration-files/deep-dive.html

**Contents**:
- Deep Dive
- Declaration File Theory: A Deep Dive
- Key Concepts
  - Types
  - Values
  - Namespaces
- Simple Combinations: One name, multiple meanings
  - Built-in Combinations

Was this page helpful?

Structuring modules to give the exact API shape you want can be tricky. For example, we might want a module that can be invoked with or without new to produce different types, has a variety of named types exposed in a hierarchy, and has some properties on the module object as well.

By reading this guide, you’ll have the tools to write complex declaration files that expose a friendly API surface. This guide focuses on module (or UMD) libraries because the options here are more varied.

You can fully understand how to make any shape of declaration by understanding some key concepts of how TypeScript works.

If you’re reading this guide, you probably already roughly know what a type in TypeScript is. To be more explicit, though, a type is introduced with:

Each of these declaration forms creates a new type name.

As with types, you probably already understand what a value is. Values are runtime names that we can reference in expressions. For example let x = 5; creates a value called x.

Again, being explicit, the following things create values:

Types can exist in namespaces. For example, if we have the declaration let x: A.B.C, we say that the type C comes from the A.B namespace.

This distinction is subtle and important — here, A.B is not necessarily a type or a value.

Given a name A, we might find up to three different meanings for A: a type, a value or a namespace. How the name is interpreted depends on the context in which it is used. For example, in the declaration let m: A.A = A;, A is used first as a namespace, then as a type name, then as a value. These meanings might end up referring to entirely different declarations!

This may seem confusing, but it’s actually very convenient as long as we don’t excessively overload things. Let’s look at some useful aspects of this combining behavior.

Astute readers will notice that, for example, class appeared in both the type and value lists. The declaration class C { } creates two things: a typ

*[Content truncated - see full docs]*

**Examples**:

```text
export var SomeVar: { a: SomeType };export interface SomeType {  count: number;}
```

```python
import * as foo from "./foo";let x: foo.SomeType = foo.SomeVar.a;console.log(x.count);
```

```text
export var Bar: { a: Bar };export interface Bar {  count: number;}
```

---

## Do's and Don'ts

**URL**: https://www.typescriptlang.org/docs/handbook/declaration-files/do-s-and-don-ts.html

**Contents**:
- Do's and Don'ts
- General Types
  - Number, String, Boolean, Symbol and Object
  - Generics
  - any
- Callback Types
  - Return Types of Callbacks
  - Optional Parameters in Callbacks

Was this page helpful?

❌ Don’t ever use the types Number, String, Boolean, Symbol, or Object These types refer to non-primitive boxed objects that are almost never used appropriately in JavaScript code.

✅ Do use the types number, string, boolean, and symbol.

Instead of Object, use the non-primitive object type (added in TypeScript 2.2).

❌ Don’t ever have a generic type which doesn’t use its type parameter. See more details in TypeScript FAQ page.

❌ Don’t use any as a type unless you are in the process of migrating a JavaScript project to TypeScript. The compiler effectively treats any as “please turn off type checking for this thing”. It is similar to putting an @ts-ignore comment around every usage of the variable. This can be very helpful when you are first migrating a JavaScript project to TypeScript as you can set the type for stuff you haven’t migrated yet as any, but in a full TypeScript project you are disabling type checking for any parts of your program that use it.

In cases where you don’t know what type you want to accept, or when you want to accept anything because you will be blindly passing it through without interacting with it, you can use unknown.

❌ Don’t use the return type any for callbacks whose value will be ignored:

✅ Do use the return type void for callbacks whose value will be ignored:

❔ Why: Using void is safer because it prevents you from accidentally using the return value of x in an unchecked way:

❌ Don’t use optional parameters in callbacks unless you really mean it:

This has a very specific meaning: the done callback might be invoked with 1 argument or might be invoked with 2 arguments. The author probably intended to say that the callback might not care about the elapsedTime parameter, but there’s no need to make the parameter optional to accomplish this — it’s always legal to provide a callback that accepts fewer arguments.

✅ Do write callback parameters as non-optional:

❌ Don’t write separate overloads that differ only o

*[Content truncated - see full docs]*

**Examples**:

```javascript
/* WRONG */function reverse(s: String): String;
```

```javascript
/* OK */function reverse(s: string): string;
```

```javascript
/* WRONG */function fn(x: () => any) {  x();}
```

---

## Enums

**URL**: https://www.typescriptlang.org/docs/handbook/enums.html

**Contents**:
- Enums
- Numeric enums
- String enums
- Heterogeneous enums
- Computed and constant members
- Union enums and enum member types
- Enums at runtime
- Enums at compile time

Was this page helpful?

Enums are one of the few features TypeScript has which is not a type-level extension of JavaScript.

Enums allow a developer to define a set of named constants. Using enums can make it easier to document intent, or create a set of distinct cases. TypeScript provides both numeric and string-based enums.

We’ll first start off with numeric enums, which are probably more familiar if you’re coming from other languages. An enum can be defined using the enum keyword.

Above, we have a numeric enum where Up is initialized with 1. All of the following members are auto-incremented from that point on. In other words, Direction.Up has the value 1, Down has 2, Left has 3, and Right has 4.

If we wanted, we could leave off the initializers entirely:

Here, Up would have the value 0, Down would have 1, etc. This auto-incrementing behavior is useful for cases where we might not care about the member values themselves, but do care that each value is distinct from other values in the same enum.

Using an enum is simple: just access any member as a property off of the enum itself, and declare types using the name of the enum:

Numeric enums can be mixed in computed and constant members (see below). The short story is, enums without initializers either need to be first, or have to come after numeric enums initialized with numeric constants or other constant enum members. In other words, the following isn’t allowed:

String enums are a similar concept, but have some subtle runtime differences as documented below. In a string enum, each member has to be constant-initialized with a string literal, or with another string enum member.

While string enums don’t have auto-incrementing behavior, string enums have the benefit that they “serialize” well. In other words, if you were debugging and had to read the runtime value of a numeric enum, the value is often opaque - it doesn’t convey any useful meaning on its own (though reverse mapping can often help). String enums

*[Content truncated - see full docs]*

**Examples**:

```text
enum Direction {  Up = 1,  Down,  Left,  Right,}
```

```text
enum Direction {  Up,  Down,  Left,  Right,}
```

```javascript
enum UserResponse {  No = 0,  Yes = 1,} function respond(recipient: string, message: UserResponse): void {  // ...} respond("Princess Caroline", UserResponse.Yes);
```

---

## Everyday Types

**URL**: https://www.typescriptlang.org/docs/handbook/2/everyday-types.html

**Contents**:
- Everyday Types
- The primitives: string, number, and boolean
- Arrays
- any
  - noImplicitAny
- Type Annotations on Variables
- Functions
  - Parameter Type Annotations

Was this page helpful?

In this chapter, we’ll cover some of the most common types of values you’ll find in JavaScript code, and explain the corresponding ways to describe those types in TypeScript. This isn’t an exhaustive list, and future chapters will describe more ways to name and use other types.

Types can also appear in many more places than just type annotations. As we learn about the types themselves, we’ll also learn about the places where we can refer to these types to form new constructs.

We’ll start by reviewing the most basic and common types you might encounter when writing JavaScript or TypeScript code. These will later form the core building blocks of more complex types.

JavaScript has three very commonly used primitives: string, number, and boolean. Each has a corresponding type in TypeScript. As you might expect, these are the same names you’d see if you used the JavaScript typeof operator on a value of those types:

The type names String, Number, and Boolean (starting with capital letters) are legal, but refer to some special built-in types that will very rarely appear in your code. Always use string, number, or boolean for types.

To specify the type of an array like [1, 2, 3], you can use the syntax number[]; this syntax works for any type (e.g. string[] is an array of strings, and so on). You may also see this written as Array<number>, which means the same thing. We’ll learn more about the syntax T<U> when we cover generics.

Note that [number] is a different thing; refer to the section on Tuples.

TypeScript also has a special type, any, that you can use whenever you don’t want a particular value to cause typechecking errors.

When a value is of type any, you can access any properties of it (which will in turn be of type any), call it like a function, assign it to (or from) a value of any type, or pretty much anything else that’s syntactically legal:

The any type is useful when you don’t want to write out a long type just to convince TypeS

*[Content truncated - see full docs]*

**Examples**:

```javascript
let obj: any = { x: 0 };// None of the following lines of code will throw compiler errors.// Using `any` disables all further type checking, and it is assumed// you know the environment better than TypeScript.obj.foo();obj();obj.bar = 100;obj = "hello";const n: number = obj;
```

```javascript
let myName: string = "Alice";
```

```javascript
// No type annotation needed -- 'myName' inferred as type 'string'let myName = "Alice";
```

---

## Generics

**URL**: https://www.typescriptlang.org/docs/handbook/2/generics.html

**Contents**:
- Generics
- Hello World of Generics
- Working with Generic Type Variables
- Generic Types
- Generic Classes
- Generic Constraints
- Using Type Parameters in Generic Constraints
- Using Class Types in Generics

Was this page helpful?

A major part of software engineering is building components that not only have well-defined and consistent APIs, but are also reusable. Components that are capable of working on the data of today as well as the data of tomorrow will give you the most flexible capabilities for building up large software systems.

In languages like C# and Java, one of the main tools in the toolbox for creating reusable components is generics, that is, being able to create a component that can work over a variety of types rather than a single one. This allows users to consume these components and use their own types.

To start off, let’s do the “hello world” of generics: the identity function. The identity function is a function that will return back whatever is passed in. You can think of this in a similar way to the echo command.

Without generics, we would either have to give the identity function a specific type:

Or, we could describe the identity function using the any type:

While using any is certainly generic in that it will cause the function to accept any and all types for the type of arg, we actually are losing the information about what that type was when the function returns. If we passed in a number, the only information we have is that any type could be returned.

Instead, we need a way of capturing the type of the argument in such a way that we can also use it to denote what is being returned. Here, we will use a type variable, a special kind of variable that works on types rather than values.

We’ve now added a type variable Type to the identity function. This Type allows us to capture the type the user provides (e.g. number), so that we can use that information later. Here, we use Type again as the return type. On inspection, we can now see the same type is used for the argument and the return type. This allows us to traffic that type information in one side of the function and out the other.

We say that this version of the identity function 

*[Content truncated - see full docs]*

**Examples**:

```javascript
function identity(arg: number): number {  return arg;}
```

```javascript
function identity(arg: any): any {  return arg;}
```

```javascript
function identity<Type>(arg: Type): Type {  return arg;}
```

---

## Global: Modifying Module

**URL**: https://www.typescriptlang.org/docs/handbook/declaration-files/templates/global-modifying-module-d-ts.html

**Contents**:
- Global: Modifying Module
- Global-modifying Modules
- Identifying global-modifying modules
      - On this page
      - Is this page helpful?

Was this page helpful?

A global-modifying module alters existing values in the global scope when they are imported. For example, there might exist a library which adds new members to String.prototype when imported. This pattern is somewhat dangerous due to the possibility of runtime conflicts, but we can still write a declaration file for it.

Global-modifying modules are generally easy to identify from their documentation. In general, they’re similar to global plugins, but need a require call to activate their effects.

You might see documentation like this:

The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤

Last updated: Oct 13, 2025

**Examples**:

```text
// 'require' call that doesn't use its return valuevar unused = require("magic-string-time");/* or */require("magic-string-time");var x = "hello, world";// Creates new methods on built-in typesconsole.log(x.startsWithHello());var y = [1, 2, 3];// Creates new methods on built-in typesconsole.log(y.reverseAndSort());
```

```javascript
// Type definitions for [~THE LIBRARY NAME~] [~OPTIONAL VERSION NUMBER~]// Project: [~THE PROJECT NAME~]// Definitions by: [~YOUR NAME~] <[~A URL FOR YOU~]>/*~ This is the global-modifying module template file. You should rename it to index.d.ts *~ and place it in a folder with the same name as the module. *~ For example, if you were writing a file for "super-greeter", this *~ file should be 'super-greeter/index.d.ts' *//*~ Note: If your global-modifying module is callable or constructable, you'
...
```

---

## Global: Plugin

**URL**: https://www.typescriptlang.org/docs/handbook/declaration-files/templates/global-plugin-d-ts.html

**Contents**:
- Global: Plugin
- UMD
  - Identifying a UMD library
  - Examples of UMD libraries
  - Template
- Module Plugin or UMD Plugin
  - Template
- Global Plugin

Was this page helpful?

A UMD module is one that can either be used as module (through an import), or as a global (when run in an environment without a module loader). Many popular libraries, such as Moment.js, are written this way. For example, in Node.js or using RequireJS, you would write:

whereas in a vanilla browser environment you would write:

UMD modules check for the existence of a module loader environment. This is an easy-to-spot pattern that looks something like this:

If you see tests for typeof define, typeof window, or typeof module in the code of a library, especially at the top of the file, it’s almost always a UMD library.

Documentation for UMD libraries will also often demonstrate a “Using in Node.js” example showing require, and a “Using in the browser” example showing using a <script> tag to load the script.

Most popular libraries are now available as UMD packages. Examples include jQuery, Moment.js, lodash, and many more.

There are three templates available for modules, module.d.ts, module-class.d.ts and module-function.d.ts.

Use module-function.d.ts if your module can be called like a function:

Be sure to read the footnote “The Impact of ES6 on Module Call Signatures”

Use module-class.d.ts if your module can be constructed using new:

The same footnote applies to these modules.

If your module is not callable or constructable, use the module.d.ts file.

A module plugin changes the shape of another module (either UMD or module). For example, in Moment.js, moment-range adds a new range method to the moment object.

For the purposes of writing a declaration file, you’ll write the same code whether the module being changed is a plain module or UMD module.

Use the module-plugin.d.ts template.

A global plugin is global code that changes the shape of some global. As with global-modifying modules, these raise the possibility of runtime conflict.

For example, some libraries add new functions to Array.prototype or String.prototype.

Global plu

*[Content truncated - see full docs]*

**Examples**:

```text
import moment = require("moment");console.log(moment.format());
```

```text
console.log(moment.format());
```

```javascript
(function (root, factory) {    if (typeof define === "function" && define.amd) {        define(["libName"], factory);    } else if (typeof module === "object" && module.exports) {        module.exports = factory(require("libName"));    } else {        root.returnExports = factory(root.libName);    }}(this, function (b) {
```

---

## Global .d.ts

**URL**: https://www.typescriptlang.org/docs/handbook/declaration-files/templates/global-d-ts.html

**Contents**:
- Global .d.ts
- Global Libraries
- Identifying a Global Library from Code
- Examples of Global Libraries
- Global Library Template
      - On this page
      - Is this page helpful?

Was this page helpful?

A global library is one that can be accessed from the global scope (i.e. without using any form of import). Many libraries simply expose one or more global variables for use. For example, if you were using jQuery, the $ variable can be used by simply referring to it:

You’ll usually see guidance in the documentation of a global library of how to use the library in an HTML script tag:

Today, most popular globally-accessible libraries are actually written as UMD libraries (see below). UMD library documentation is hard to distinguish from global library documentation. Before writing a global declaration file, make sure the library isn’t actually UMD.

Global library code is usually extremely simple. A global “Hello, world” library might look like this:

When looking at the code of a global library, you’ll usually see:

Because it’s usually easy to turn a global library into a UMD library, very few popular libraries are still written in the global style. However, libraries that are small and require the DOM (or have no dependencies) may still be global.

You can see an example DTS below:

The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤

Last updated: Oct 13, 2025

**Examples**:

```javascript
$(() => {  console.log("hello!");});
```

```text
<script src="http://a.great.cdn.for/someLib.js"></script>
```

```javascript
function createGreeting(s) {  return "Hello, " + s;}
```

---

## Gulp

**URL**: https://www.typescriptlang.org/docs/handbook/gulp.html

**Contents**:
- Gulp
- Minimal project
  - Initialize the project
  - Install our dependencies
  - Write a simple example
  - Create a gulpfile.js
  - Test the resulting app
- Add modules to the code

Was this page helpful?

This quick start guide will teach you how to build TypeScript with gulp and then add Browserify, terser, or Watchify to the gulp pipeline. This guide also shows how to add Babel functionality using Babelify.

We assume that you’re already using Node.js with npm.

Let’s start out with a new directory. We’ll name it proj for now, but you can change it to whatever you want.

To start, we’re going to structure our project in the following way:

TypeScript files will start out in your src folder, run through the TypeScript compiler and end up in dist.

Let’s scaffold this out:

Now we’ll turn this folder into an npm package.

You’ll be given a series of prompts. You can use the defaults except for your entry point. For your entry point, use ./dist/main.js. You can always go back and change these in the package.json file that’s been generated for you.

Now we can use npm install to install packages. First install gulp-cli globally (if you use a Unix system, you may need to prefix the npm install commands in this guide with sudo).

Then install typescript, gulp and gulp-typescript in your project’s dev dependencies. Gulp-typescript is a gulp plugin for TypeScript.

Let’s write a Hello World program. In src, create the file main.ts:

In the project root, proj, create the file tsconfig.json:

In the project root, create the file gulpfile.js:

The program should print “Hello from TypeScript!“.

Before we get to Browserify, let’s build our code out and add modules to the mix. This is the structure you’re more likely to use for a real app.

Create a file called src/greet.ts:

Now change the code in src/main.ts to import sayHello from greet.ts:

Finally, add src/greet.ts to tsconfig.json:

Make sure that the modules work by running gulp and then testing in Node:

Notice that even though we used ES2015 module syntax, TypeScript emitted CommonJS modules that Node uses. We’ll stick with CommonJS for this tutorial, but you could set module in the options obje

*[Content truncated - see full docs]*

**Examples**:

```text
mkdir projcd proj
```

```text
proj/   ├─ src/   └─ dist/
```

```text
mkdir srcmkdir dist
```

---

## Indexed Access Types

**URL**: https://www.typescriptlang.org/docs/handbook/2/indexed-access-types.html

**Contents**:
- Indexed Access Types
      - On this page
      - Is this page helpful?
  - Typeof Type Operator
  - Conditional Types

Was this page helpful?

We can use an indexed access type to look up a specific property on another type:

The indexing type is itself a type, so we can use unions, keyof, or other types entirely:

You’ll even see an error if you try to index a property that doesn’t exist:

Another example of indexing with an arbitrary type is using number to get the type of an array’s elements. We can combine this with typeof to conveniently capture the element type of an array literal:

You can only use types when indexing, meaning you can’t use a const to make a variable reference:

However, you can use a type alias for a similar style of refactor:

Using the typeof operator in type contexts.

Create types which act like if statements in the type system.

The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤

Last updated: Oct 13, 2025

**Examples**:

```text
type Person = { age: number; name: string; alive: boolean };type Age = Person["age"];     type Age = number
```

```text
type I1 = Person["age" | "name"];     type I1 = string | number type I2 = Person[keyof Person];     type I2 = string | number | boolean type AliveOrName = "alive" | "name";type I3 = Person[AliveOrName];     type I3 = string | boolean
```

```text
type I1 = Person["alve"];Property 'alve' does not exist on type 'Person'.2339Property 'alve' does not exist on type 'Person'.
```

---

## Integrating with Build Tools

**URL**: https://www.typescriptlang.org/docs/handbook/integrating-with-build-tools.html

**Contents**:
- Integrating with Build Tools
- Babel
  - Install
  - .babelrc
  - Using Command Line Interface
  - package.json
  - Execute Babel from the command line
- Browserify

Was this page helpful?

More details: smrq/tsify

More details: TypeStrong/grunt-ts

More details: jmreidy/grunt-browserify, TypeStrong/tsify

More details: ivogabe/gulp-typescript

Note: Currently TypeScript support in jspm is in 0.16beta

More details: TypeScriptSamples/jspm

Update project file to include locally installed Microsoft.TypeScript.Default.props (at the top) and Microsoft.TypeScript.targets (at the bottom) files:

More details about defining MSBuild compiler options: Setting Compiler Options in MSBuild projects

More details can be found at Package Manager Dialog and using nightly builds with NuGet

Note that both typescript and tslib are peer dependencies of this plugin that need to be installed separately.

Create a rollup.config.js configuration file and import the plugin:

Note that typescript is an optional peer dependencies of this plugin and needs to be installed separately. tslib is not provided either.

You may also consider svelte-check for CLI type checking.

Create a svelte.config.js configuration file and import the plugin:

You can now specify that script blocks are written in TypeScript:

Vite supports importing .ts files out-of-the-box. It only performs transpilation and not type checking. It also requires that some compilerOptions have certain values. See the Vite docs for more details.

See more details on ts-loader here.

The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤

Last updated: Oct 13, 2025

**Examples**:

```text
npm install @babel/cli @babel/core @babel/preset-typescript --save-dev
```

```text
{  "presets": ["@babel/preset-typescript"]}
```

```text
./node_modules/.bin/babel --out-file bundle.js src/index.ts
```

---

## Interfaces

**URL**: https://www.typescriptlang.org/docs/handbook/interfaces.html

**Contents**:
  - This page has been deprecated
- Interfaces
- Our First Interface
- Optional Properties
- Readonly properties
  - readonly vs const
- Excess Property Checks
- Function Types

Was this page helpful?

This handbook page has been replaced, go to the new page

One of TypeScript’s core principles is that type checking focuses on the shape that values have. This is sometimes called “duck typing” or “structural subtyping”. In TypeScript, interfaces fill the role of naming these types, and are a powerful way of defining contracts within your code as well as contracts with code outside of your project.

The easiest way to see how interfaces work is to start with a simple example:

The type checker checks the call to printLabel. The printLabel function has a single parameter that requires that the object passed in has a property called label of type string. Notice that our object actually has more properties than this, but the compiler only checks that at least the ones required are present and match the types required. There are some cases where TypeScript isn’t as lenient, which we’ll cover in a bit.

We can write the same example again, this time using an interface to describe the requirement of having the label property that is a string:

The interface LabeledValue is a name we can now use to describe the requirement in the previous example. It still represents having a single property called label that is of type string. Notice we didn’t have to explicitly say that the object we pass to printLabel implements this interface like we might have to in other languages. Here, it’s only the shape that matters. If the object we pass to the function meets the requirements listed, then it’s allowed.

It’s worth pointing out that the type checker does not require that these properties come in any sort of order, only that the properties the interface requires are present and have the required type.

Not all properties of an interface may be required. Some exist under certain conditions or may not be there at all. These optional properties are popular when creating patterns like “option bags” where you pass an object to a function that only has a couple o

*[Content truncated - see full docs]*

**Examples**:

```javascript
function printLabel(labeledObj: { label: string }) {  console.log(labeledObj.label);} let myObj = { size: 10, label: "Size 10 Object" };printLabel(myObj);
```

```javascript
interface LabeledValue {  label: string;} function printLabel(labeledObj: LabeledValue) {  console.log(labeledObj.label);} let myObj = { size: 10, label: "Size 10 Object" };printLabel(myObj);
```

```javascript
interface SquareConfig {  color?: string;  width?: number;} function createSquare(config: SquareConfig): { color: string; area: number } {  let newSquare = { color: "white", area: 100 };  if (config.color) {    newSquare.color = config.color;  }  if (config.width) {    newSquare.area = config.width * config.width;  }  return newSquare;} let mySquare = createSquare({ color: "black" });
```

---

## Introduction

**URL**: https://www.typescriptlang.org/docs/handbook/declaration-files/introduction.html

**Contents**:
- Introduction
- Declaration Reference
- Library Structures
- Do’s and Don’ts
- Deep Dive
- Publish to npm
- Find and Install Declaration Files
      - On this page

Was this page helpful?

The Declaration Files section is designed to teach you how to write a high-quality TypeScript Declaration File. We need to assume basic familiarity with the TypeScript language in order to get started.

If you haven’t already, you should read the TypeScript Handbook to familiarize yourself with basic concepts, especially types and modules.

The most common case for learning how .d.ts files work is that you’re typing an npm package with no types. In that case, you can jump straight to Modules .d.ts.

The Declaration Files section is broken down into the following sections.

We are often faced with writing a declaration file when we only have examples of the underlying library to guide us. The Declaration Reference section shows many common API patterns and how to write declarations for each of them. This guide is aimed at the TypeScript novice who may not yet be familiar with every language construct in TypeScript.

The Library Structures guide helps you understand common library formats and how to write a proper declaration file for each format. If you’re editing an existing file, you probably don’t need to read this section. Authors of new declaration files are strongly encouraged to read this section to properly understand how the format of the library influences the writing of the declaration file.

In the Template section you’ll find a number of declaration files that serve as a useful starting point when writing a new file. If you already know what your structure is, see the d.ts Template section in the sidebar.

Many common mistakes in declaration files can be easily avoided. The Do’s and Don’ts section identifies common errors, describes how to detect them, and how to fix them. Everyone should read this section to help themselves avoid common mistakes.

For seasoned authors interested in the underlying mechanics of how declaration files work, the Deep Dive section explains many advanced concepts in declaration writing, and shows how to

*[Content truncated - see full docs]*

---

## Iterators and Generators

**URL**: https://www.typescriptlang.org/docs/handbook/iterators-and-generators.html

**Contents**:
- Iterators and Generators
- Iterables
  - Iterable interface
  - for..of statements
  - for..of vs. for..in statements
  - Code generation
    - Targeting ES5
    - Targeting ECMAScript 2015 and higher

Was this page helpful?

An object is deemed iterable if it has an implementation for the Symbol.iterator property. Some built-in types like Array, Map, Set, String, Int32Array, Uint32Array, etc. have their Symbol.iterator property already implemented. Symbol.iterator function on an object is responsible for returning the list of values to iterate on.

Iterable is a type we can use if we want to take in types listed above which are iterable. Here is an example:

for..of loops over an iterable object, invoking the Symbol.iterator property on the object. Here is a simple for..of loop on an array:

Both for..of and for..in statements iterate over lists; the values iterated on are different though, for..in returns a list of keys on the object being iterated, whereas for..of returns a list of values of the numeric properties of the object being iterated.

Here is an example that demonstrates this distinction:

Another distinction is that for..in operates on any object; it serves as a way to inspect properties on this object. for..of on the other hand, is mainly interested in values of iterable objects. Built-in objects like Map and Set implement Symbol.iterator property allowing access to stored values.

When targeting an ES5-compliant engine, iterators are only allowed on values of Array type. It is an error to use for..of loops on non-Array values, even if these non-Array values implement the Symbol.iterator property.

The compiler will generate a simple for loop for a for..of loop, for instance:

will be generated as:

When targeting an ECMAScript 2015-compliant engine, the compiler will generate for..of loops to target the built-in iterator implementation in the engine.

The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤

Last updated: Oct 13, 2025

**Examples**:

```javascript
function toArray<X>(xs: Iterable<X>): X[] {  return [...xs]}
```

```javascript
let someArray = [1, "string", false];for (let entry of someArray) {  console.log(entry); // 1, "string", false}
```

```javascript
let list = [4, 5, 6];for (let i in list) {  console.log(i); // "0", "1", "2",}for (let i of list) {  console.log(i); // 4, 5, 6}
```

---

## JSDoc Reference

**URL**: https://www.typescriptlang.org/docs/handbook/jsdoc-supported-types.html

**Contents**:
- JSDoc Reference
    - Types
    - Classes
    - Documentation
    - Other
- Types
  - @type
    - Casts

Was this page helpful?

The list below outlines which constructs are currently supported when using JSDoc annotations to provide type information in JavaScript files.

Documentation tags work in both TypeScript and JavaScript.

The meaning is usually the same, or a superset, of the meaning of the tag given at jsdoc.app. The code below describes the differences and gives some example usage of each tag.

Note: You can use the playground to explore JSDoc support.

You can reference types with the “@type” tag. The type can be:

You can use most JSDoc type syntax and any TypeScript syntax, from the most basic like string to the most advanced, like conditional types.

@type can specify a union type — for example, something can be either a string or a boolean.

You can specify array types using a variety of syntaxes:

You can also specify object literal types. For example, an object with properties ‘a’ (string) and ‘b’ (number) uses the following syntax:

You can specify map-like and array-like objects using string and number index signatures, using either standard JSDoc syntax or TypeScript syntax.

The preceding two types are equivalent to the TypeScript types { [x: string]: number } and { [x: number]: any }. The compiler understands both syntaxes.

You can specify function types using either TypeScript or Google Closure syntax:

Or you can just use the unspecified Function type:

Other types from Closure also work:

TypeScript borrows cast syntax from Google Closure. This lets you cast types to other types by adding a @type tag before any parenthesized expression.

You can even cast to const just like TypeScript:

You can import declarations from other files using import types. This syntax is TypeScript-specific and differs from the JSDoc standard:

import types can be used to get the type of a value from a module if you don’t know the type, or if it has a large type that is annoying to type:

The @import tag can let us reference exports from other files.

These tags do

*[Content truncated - see full docs]*

**Examples**:

```text
/** * @type {string} */var s; /** @type {Window} */var win; /** @type {PromiseLike<string>} */var promisedString; // You can specify an HTML Element with DOM properties/** @type {HTMLElement} */var myElement = document.querySelector(selector);element.dataset.myData = "";
```

```text
/** * @type {string | boolean} */var sb;
```

```text
/** @type {number[]} */var ns;/** @type {Array.<number>} */var jsdoc;/** @type {Array<number>} */var nas;
```

---

## JSX

**URL**: https://www.typescriptlang.org/docs/handbook/jsx.html

**Contents**:
- JSX
- Basic usage
- The as operator
- Type Checking
  - The JSX namespace
  - Intrinsic elements
  - Value-based elements
    - Function Component

Was this page helpful?

JSX is an embeddable XML-like syntax. It is meant to be transformed into valid JavaScript, though the semantics of that transformation are implementation-specific. JSX rose to popularity with the React framework, but has since seen other implementations as well. TypeScript supports embedding, type checking, and compiling JSX directly to JavaScript.

In order to use JSX you must do two things.

TypeScript ships with several JSX modes: preserve, react (classic runtime), react-jsx (automatic runtime), react-jsxdev (automatic development runtime), and react-native. The preserve mode will keep the JSX as part of the output to be further consumed by another transform step (e.g. Babel). Additionally the output will have a .jsx file extension. The react mode will emit React.createElement, does not need to go through a JSX transformation before use, and the output will have a .js file extension. The react-native mode is the equivalent of preserve in that it keeps all JSX, but the output will instead have a .js file extension.

You can specify this mode using either the jsx command line flag or the corresponding option jsx in your tsconfig.json file.

*Note: You can specify the JSX factory function to use when targeting react JSX emit with jsxFactory option (defaults to React.createElement)

Recall how to write a type assertion:

This asserts the variable bar to have the type Foo. Since TypeScript also uses angle brackets for type assertions, combining it with JSX’s syntax would introduce certain parsing difficulties. As a result, TypeScript disallows angle bracket type assertions in .tsx files.

Since the above syntax cannot be used in .tsx files, an alternate type assertion operator should be used: as. The example can easily be rewritten with the as operator.

The as operator is available in both .ts and .tsx files, and is identical in behavior to the angle-bracket type assertion style.

In order to understand type checking with JSX, you must first u

*[Content truncated - see full docs]*

**Examples**:

```javascript
const foo = <Foo>bar;
```

```javascript
const foo = bar as Foo;
```

```javascript
export function createElement(): any;export namespace JSX {  // …}
```

---

## JS Projects Utilizing TypeScript

**URL**: https://www.typescriptlang.org/docs/handbook/intro-to-js-ts.html

**Contents**:
- JS Projects Utilizing TypeScript
- TypeScript with JavaScript
- Providing Type Hints in JS via JSDoc
- @ts-check
      - On this page
      - Is this page helpful?
  - Type Checking JavaScript Files

Was this page helpful?

The type system in TypeScript has different levels of strictness when working with a codebase:

Each step represents a move towards a safer type-system, but not every project needs that level of verification.

This is when you use an editor which uses TypeScript to provide tooling like auto-complete, jump to symbol and refactoring tools like rename. The homepage has a list of editors which have TypeScript plugins.

In a .js file, types can often be inferred. When types can’t be inferred, they can be specified using JSDoc syntax.

JSDoc annotations that come before a declaration will be used to set the type of that declaration. For example:

You can find the full list of supported JSDoc patterns in JSDoc Supported Types.

The last line of the previous code sample would raise an error in TypeScript, but it doesn’t by default in a JS project. To enable errors in your JavaScript files add: // @ts-check to the first line in your .js files to have TypeScript raise it as an error.

If you have a lot of JavaScript files you want to add errors to then you can switch to using a jsconfig.json. You can skip checking some files by adding a // @ts-nocheck comment to files.

TypeScript may offer you errors which you disagree with, in those cases you can ignore errors on specific lines by adding // @ts-ignore or // @ts-expect-error on the preceding line.

To learn more about how JavaScript is interpreted by TypeScript read How TS Type Checks JS

How to add type checking to JavaScript files using TypeScript

The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤

Last updated: Oct 13, 2025

**Examples**:

```text
/** @type {number} */var x; x = 0; // OKx = false; // OK?!
```

```text
// @ts-check/** @type {number} */var x; x = 0; // OKx = false; // Not OKType 'boolean' is not assignable to type 'number'.2322Type 'boolean' is not assignable to type 'number'.
```

```text
// @ts-check/** @type {number} */var x; x = 0; // OK// @ts-expect-errorx = false; // Not OK
```

---

## Keyof Type Operator

**URL**: https://www.typescriptlang.org/docs/handbook/2/keyof-types.html

**Contents**:
- Keyof Type Operator
- The keyof type operator
      - On this page
      - Is this page helpful?
  - Generics
  - Typeof Type Operator

Was this page helpful?

The keyof operator takes an object type and produces a string or numeric literal union of its keys. The following type P is the same type as type P = "x" | "y":

If the type has a string or number index signature, keyof will return those types instead:

Note that in this example, M is string | number — this is because JavaScript object keys are always coerced to a string, so obj[0] is always the same as obj["0"].

keyof types become especially useful when combined with mapped types, which we’ll learn more about later.

Types which take parameters

Using the typeof operator in type contexts.

The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤

Last updated: Oct 13, 2025

**Examples**:

```text
type Point = { x: number; y: number };type P = keyof Point;    type P = keyof Point
```

```text
type Arrayish = { [n: number]: unknown };type A = keyof Arrayish;    type A = number type Mapish = { [k: string]: boolean };type M = keyof Mapish;    type M = string | number
```

---

## Library Structures

**URL**: https://www.typescriptlang.org/docs/handbook/declaration-files/library-structures.html

**Contents**:
- Library Structures
- Identifying Kinds of Libraries
  - What should you look for?
  - Smaller samples for different types of libraries
  - Modular Libraries
    - Identifying a Module Library from Code
    - Templates For Modules
  - Global Libraries

Was this page helpful?

Broadly speaking, the way you structure your declaration file depends on how the library is consumed. There are many ways of offering a library for consumption in JavaScript, and you’ll need to write your declaration file to match it. This guide covers how to identify common library patterns, and how to write declaration files which correspond to that pattern.

Each type of major library structuring pattern has a corresponding file in the Templates section. You can start with these templates to help you get going faster.

First, we’ll review the kinds of libraries TypeScript declaration files can represent. We’ll briefly show how each kind of library is used, how it is written, and list some example libraries from the real world.

Identifying the structure of a library is the first step in writing its declaration file. We’ll give hints on how to identify structure both based on its usage and its code. Depending on the library’s documentation and organization, one might be easier than the other. We recommend using whichever is more comfortable to you.

Question to ask yourself while looking at a library you are trying to type.

How do you obtain the library?

For example, can you only get it through npm or only from a CDN?

How would you import it?

Does it add a global object? Does it use require or import/export statements?

Almost every modern Node.js library falls into the module family. These type of libraries only work in a JS environment with a module loader. For example, express only works in Node.js and must be loaded using the CommonJS require function.

ECMAScript 2015 (also known as ES2015, ECMAScript 6, and ES6), CommonJS, and RequireJS have similar notions of importing a module. In JavaScript CommonJS (Node.js), for example, you would write

In TypeScript or ES6, the import keyword serves the same purpose:

You’ll typically see modular libraries include one of these lines in their documentation:

As with global modules, you might

*[Content truncated - see full docs]*

**Examples**:

```text
var fs = require("fs");
```

```python
import * as fs from "fs";
```

```text
var someLib = require("someLib");
```

---

## Mapped Types

**URL**: https://www.typescriptlang.org/docs/handbook/2/mapped-types.html

**Contents**:
- Mapped Types
  - Mapping Modifiers
- Key Remapping via as
  - Further Exploration
      - On this page
      - Is this page helpful?
  - Conditional Types
  - Template Literal Types

Was this page helpful?

When you don’t want to repeat yourself, sometimes a type needs to be based on another type.

Mapped types build on the syntax for index signatures, which are used to declare the types of properties which have not been declared ahead of time:

A mapped type is a generic type which uses a union of PropertyKeys (frequently created via a keyof) to iterate through keys to create a type:

In this example, OptionsFlags will take all the properties from the type Type and change their values to be a boolean.

There are two additional modifiers which can be applied during mapping: readonly and ? which affect mutability and optionality respectively.

You can remove or add these modifiers by prefixing with - or +. If you don’t add a prefix, then + is assumed.

In TypeScript 4.1 and onwards, you can re-map keys in mapped types with an as clause in a mapped type:

You can leverage features like template literal types to create new property names from prior ones:

You can filter out keys by producing never via a conditional type:

You can map over arbitrary unions, not just unions of string | number | symbol, but unions of any type:

Mapped types work well with other features in this type manipulation section, for example here is a mapped type using a conditional type which returns either a true or false depending on whether an object has the property pii set to the literal true:

Create types which act like if statements in the type system.

Generating mapping types which change properties via template literal strings.

The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤

Last updated: Oct 13, 2025

**Examples**:

```javascript
type OnlyBoolsAndHorses = {  [key: string]: boolean | Horse;}; const conforms: OnlyBoolsAndHorses = {  del: true,  rodney: false,};
```

```text
type OptionsFlags<Type> = {  [Property in keyof Type]: boolean;};
```

```javascript
type Features = {  darkMode: () => void;  newUserProfile: () => void;}; type FeatureOptions = OptionsFlags<Features>;           type FeatureOptions = {
    darkMode: boolean;
    newUserProfile: boolean;
}
```

---

## Migrating from JavaScript

**URL**: https://www.typescriptlang.org/docs/handbook/migrating-from-javascript.html

**Contents**:
- Migrating from JavaScript
- Setting up your Directories
- Writing a Configuration File
- Early Benefits
- Integrating with Build Tools
  - Gulp
  - Webpack
- Moving to TypeScript Files

Was this page helpful?

TypeScript doesn’t exist in a vacuum. It was built with the JavaScript ecosystem in mind, and a lot of JavaScript exists today. Converting a JavaScript codebase over to TypeScript is, while somewhat tedious, usually not challenging. In this tutorial, we’re going to look at how you might start out. We assume you’ve read enough of the handbook to write new TypeScript code.

If you’re looking to convert a React project, we recommend looking at the React Conversion Guide first.

If you’re writing in plain JavaScript, it’s likely that you’re running your JavaScript directly, where your .js files are in a src, lib, or dist directory, and then run as desired.

If that’s the case, the files that you’ve written are going to be used as inputs to TypeScript, and you’ll run the outputs it produces. During our JS to TS migration, we’ll need to separate our input files to prevent TypeScript from overwriting them. If your output files need to reside in a specific directory, then that will be your output directory.

You might also be running some intermediate steps on your JavaScript, such as bundling or using another transpiler like Babel. In this case, you might already have a folder structure like this set up.

From this point on, we’re going to assume that your directory is set up something like this:

If you have a tests folder outside of your src directory, you might have one tsconfig.json in src, and one in tests as well.

TypeScript uses a file called tsconfig.json for managing your project’s options, such as which files you want to include, and what sorts of checking you want to perform. Let’s create a bare-bones one for our project:

Here we’re specifying a few things to TypeScript:

At this point, if you try running tsc at the root of your project, you should see output files in the built directory. The layout of files in built should look identical to the layout of src. You should now have TypeScript working with your project.

Even at this point

*[Content truncated - see full docs]*

**Examples**:

```text
projectRoot├── src│   ├── file1.js│   └── file2.js├── built└── tsconfig.json
```

```text
{  "compilerOptions": {    "outDir": "./built",    "allowJs": true,    "target": "es5"  },  "include": ["./src/**/*"]}
```

```text
npm install ts-loader source-map-loader
```

---

## Mixins

**URL**: https://www.typescriptlang.org/docs/handbook/mixins.html

**Contents**:
- Mixins
- How Does A Mixin Work?
- Constrained Mixins
- Alternative Pattern
- Constraints
    - Decorators and Mixins #4881
    - Static Property Mixins #17829
      - On this page

Was this page helpful?

Along with traditional OO hierarchies, another popular way of building up classes from reusable components is to build them by combining simpler partial classes. You may be familiar with the idea of mixins or traits for languages like Scala, and the pattern has also reached some popularity in the JavaScript community.

The pattern relies on using generics with class inheritance to extend a base class. TypeScript’s best mixin support is done via the class expression pattern. You can read more about how this pattern works in JavaScript here.

To get started, we’ll need a class which will have the mixins applied on top of:

Then you need a type and a factory function which returns a class expression extending the base class.

With these all set up, then you can create a class which represents the base class with mixins applied:

In the above form, the mixin’s have no underlying knowledge of the class which can make it hard to create the design you want.

To model this, we modify the original constructor type to accept a generic argument.

This allows for creating classes which only work with constrained base classes:

Then you can create mixins which only work when you have a particular base to build on:

Previous versions of this document recommended a way to write mixins where you created both the runtime and type hierarchies separately, then merged them at the end:

This pattern relies less on the compiler, and more on your codebase to ensure both runtime and type-system are correctly kept in sync.

The mixin pattern is supported natively inside the TypeScript compiler by code flow analysis. There are a few cases where you can hit the edges of the native support.

You cannot use decorators to provide mixins via code flow analysis:

More of a gotcha than a constraint. The class expression pattern creates singletons, so they can’t be mapped at the type system to support different variable types.

You can work around this by using functions to r

*[Content truncated - see full docs]*

**Examples**:

```text
class Sprite {  name = "";  x = 0;  y = 0;   constructor(name: string) {    this.name = name;  }}
```

```javascript
// To get started, we need a type which we'll use to extend// other classes from. The main responsibility is to declare// that the type being passed in is a class. type Constructor = new (...args: any[]) => {}; // This mixin adds a scale property, with getters and setters// for changing it with an encapsulated private property: function Scale<TBase extends Constructor>(Base: TBase) {  return class Scaling extends Base {    // Mixins may not declare private/protected properties    // however, you
...
```

```javascript
// Compose a new class from the Sprite class,// with the Mixin Scale applier:const EightBitSprite = Scale(Sprite); const flappySprite = new EightBitSprite("Bird");flappySprite.setScale(0.8);console.log(flappySprite.scale);
```

---

## Module: Class

**URL**: https://www.typescriptlang.org/docs/handbook/declaration-files/templates/module-class-d-ts.html

**Contents**:
- Module: Class
      - On this page
      - Is this page helpful?

Was this page helpful?

For example, when you want to work with JavaScript code which looks like:

To handle both importing via UMD and modules:

The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤

Last updated: Oct 13, 2025

**Examples**:

```javascript
const Greeter = require("super-greeter");const greeter = new Greeter();greeter.greet();
```

```python
// Type definitions for [~THE LIBRARY NAME~] [~OPTIONAL VERSION NUMBER~]// Project: [~THE PROJECT NAME~]// Definitions by: [~YOUR NAME~] <[~A URL FOR YOU~]>/*~ This is the module template file for class modules. *~ You should rename it to index.d.ts and place it in a folder with the same name as the module. *~ For example, if you were writing a file for "super-greeter", this *~ file should be 'super-greeter/index.d.ts' */// Note that ES6 modules cannot directly export class objects.// This file 
...
```

---

## Module: Function

**URL**: https://www.typescriptlang.org/docs/handbook/declaration-files/templates/module-function-d-ts.html

**Contents**:
- Module: Function
      - On this page
      - Is this page helpful?

Was this page helpful?

For example, when you want to work with JavaScript code which looks like:

To handle both importing via UMD and modules:

The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤

Last updated: Oct 13, 2025

**Examples**:

```python
import greeter from "super-greeter";greeter(2);greeter("Hello world");
```

```python
// Type definitions for [~THE LIBRARY NAME~] [~OPTIONAL VERSION NUMBER~]// Project: [~THE PROJECT NAME~]// Definitions by: [~YOUR NAME~] <[~A URL FOR YOU~]>/*~ This is the module template file for function modules. *~ You should rename it to index.d.ts and place it in a folder with the same name as the module. *~ For example, if you were writing a file for "super-greeter", this *~ file should be 'super-greeter/index.d.ts' */// Note that ES6 modules cannot directly export class objects.// This fi
...
```

---

## Module: Plugin

**URL**: https://www.typescriptlang.org/docs/handbook/declaration-files/templates/module-plugin-d-ts.html

**Contents**:
- Module: Plugin
- The Impact of ES6 on Module Plugins
      - On this page
      - Is this page helpful?

Was this page helpful?

For example, when you want to work with JavaScript code which extends another library.

The definition for “super-greeter”:

We can extend the existing module like the following:

This uses declaration merging

Some plugins add or modify top-level exports on existing modules. While this is legal in CommonJS and other loaders, ES6 modules are considered immutable and this pattern will not be possible. Because TypeScript is loader-agnostic, there is no compile-time enforcement of this policy, but developers intending to transition to an ES6 module loader should be aware of this.

The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤

Last updated: Oct 13, 2025

**Examples**:

```python
import { greeter } from "super-greeter";// Normal Greeter APIgreeter(2);greeter("Hello world");// Now we extend the object with a new function at runtimeimport "hyper-super-greeter";greeter.hyperGreet();
```

```javascript
/*~ This example shows how to have multiple overloads for your function */export interface GreeterFunction {  (name: string): void  (time: number): void}/*~ This example shows how to export a function specified by an interface */export const greeter: GreeterFunction;
```

```python
// Type definitions for [~THE LIBRARY NAME~] [~OPTIONAL VERSION NUMBER~]// Project: [~THE PROJECT NAME~]// Definitions by: [~YOUR NAME~] <[~A URL FOR YOU~]>/*~ This is the module plugin template file. You should rename it to index.d.ts *~ and place it in a folder with the same name as the module. *~ For example, if you were writing a file for "super-greeter", this *~ file should be 'super-greeter/index.d.ts' *//*~ On this line, import the module which this module adds to */import { greeter } fro
...
```

---

## Modules - Choosing Compiler Options

**URL**: https://www.typescriptlang.org/docs/handbook/modules/guides/choosing-compiler-options.html

**Contents**:
- Modules - Choosing Compiler Options
- I’m writing an app
  - I’m using a bundler
  - I’m compiling and running the outputs in Node.js
  - I’m using ts-node
  - I’m using tsx
  - I’m writing ES modules for the browser, with no bundler or module compiler
- I’m writing a library

Was this page helpful?

A single tsconfig.json can only represent a single environment, both in terms of what globals are available and in terms of how modules behave. If your app contains server code, DOM code, web worker code, test code, and code to be shared by all of those, each of those should have its own tsconfig.json, connected with project references. Then, use this guide once for each tsconfig.json. For library-like projects within an app, especially ones that need to run in multiple runtime environments, use the “I’m writing a library” section.

In addition to adopting the following settings, it’s also recommended not to set { "type": "module" } or use .mts files in bundler projects for now. Some bundlers adopt different ESM/CJS interop behavior under these circumstances, which TypeScript cannot currently analyze with "moduleResolution": "bundler". See issue #54102 for more information.

Remember to set "type": "module" or use .mts files if you intend to emit ES modules.

ts-node attempts to be compatible with the same code and the same tsconfig.json settings that can be used to compile and run the JS outputs in Node.js. Refer to ts-node documentation for more details.

Whereas ts-node makes minimal modifications to Node.js’s module system by default, tsx behaves more like a bundler, allowing extensionless/index module specifiers and arbitrary mixing of ESM and CJS. Use the same settings for tsx as you would for a bundler.

TypeScript does not currently have options dedicated to this scenario, but you can approximate them by using a combination of the nodenext ESM module resolution algorithm and paths as a substitute for URL and import map support.

This setup allows explicitly listed HTTPS imports to use locally-installed type declaration files, while erroring on imports that would normally resolve in node_modules:

Alternatively, you can use import maps to explicitly map a list of bare specifiers to URLs in the browser, while relying on nodenext’s defau

*[Content truncated - see full docs]*

**Examples**:

```text
{  "compilerOptions": {    // This is not a complete template; it only    // shows relevant module-related settings.    // Be sure to set other important options    // like `target`, `lib`, and `strict`.    // Required    "module": "esnext",    "moduleResolution": "bundler",    "esModuleInterop": true,    // Consult your bundler’s documentation    "customConditions": ["module"],    // Recommended    "noEmit": true, // or `emitDeclarationOnly`    "allowImportingTsExtensions": true,    "allowArbit
...
```

```text
{  "compilerOptions": {    // This is not a complete template; it only    // shows relevant module-related settings.    // Be sure to set other important options    // like `target`, `lib`, and `strict`.    // Required    "module": "nodenext",    // Implied by `"module": "nodenext"`:    // "moduleResolution": "nodenext",    // "esModuleInterop": true,    // "target": "esnext",    // Recommended    "verbatimModuleSyntax": true,  }}
```

```text
// tsconfig.json{  "compilerOptions": {    // This is not a complete template; it only    // shows relevant module-related settings.    // Be sure to set other important options    // like `target`, `lib`, and `strict`.    // Combined with `"type": "module"` in a local package.json,    // this enforces including file extensions on relative path imports.    "module": "nodenext",    "paths": {      // Point TS to local types for remote URLs:      "https://esm.sh/lodash@4.17.21": ["./node_modules/@
...
```

---

## Modules - ESM/CJS Interoperability

**URL**: https://www.typescriptlang.org/docs/handbook/modules/appendices/esm-cjs-interop.html

**Contents**:
- Modules - ESM/CJS Interoperability
- allowSyntheticDefaultImports and esModuleInterop
- Interop in Node.js
  - No __esModule detection (the “double default” problem)
  - Unreliable named exports
  - Cannot require a true ES module before Node.js v22
  - Different module resolution algorithms
- Conclusions

Was this page helpful?

It’s 2015, and you’re writing an ESM-to-CJS transpiler. There’s no specification for how to do this; all you have is a specification of how ES modules are supposed to interact with each other, knowledge of how CommonJS modules interact with each other, and a knack for figuring things out. Consider an exporting ES module:

How would you turn this into a CommonJS module? Recalling that default exports are just named exports with special syntax, there seems to be only one choice:

This is a nice analog, and it lets you implement a similar on the importing side:

So far, everything in CJS-world matches up one-to-one with everything in ESM-world. Extending the equivalence above one step further, we can see that we also have:

You might notice that in this scheme, there’s no way to write an ESM export that produces an output where exports is assigned a function, class, or primitive:

But existing CommonJS modules frequently take this form. How might an ESM import, processed with our transpiler, access this module? We just established that a namespace import (import *) transpiles to a plain require call, so we can support an input like:

Our output works at runtime, but we have a compliance problem: according to the JavaScript specification, a namespace import always resolves to a Module Namespace Object, that is, an object whose members are the exports of the module. In this case, require would return the function hello, but import * can never return a function. The correspondence we assumed appears invalid.

It’s worth taking a step back here and clarifying what the goal is. As soon as modules landed in the ES2015 specification, transpilers emerged with support for downleveling ESM to CJS, allowing users to adopt the new syntax long before runtimes implemented support for it. There was even a sense that writing ESM code was a good way to “future-proof” new projects. For this to be true, there needed to be a seamless migration path from executing t

*[Content truncated - see full docs]*

**Examples**:

```javascript
export const A = {};export const B = {};export default "Hello, world!";
```

```text
exports.A = {};exports.B = {};exports.default = "Hello, world!";
```

```python
import hello, { A, B } from "./module";console.log(hello, A, B);// transpiles to:const module_1 = require("./module");console.log(module_1.default, module_1.A, module_1.B);
```

---

## Modules - Introduction

**URL**: https://www.typescriptlang.org/docs/handbook/modules/introduction.html

**Contents**:
- Modules - Introduction
      - On this page
      - Is this page helpful?

Was this page helpful?

This document is divided into four sections:

The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤

Last updated: Oct 13, 2025

---

## Modules - Reference

**URL**: https://www.typescriptlang.org/docs/handbook/modules/reference.html

**Contents**:
- Modules - Reference
- Module syntax
  - Importing and exporting TypeScript-specific declarations
  - Type-only imports and exports
  - import() types
  - export = and import = require()
  - Ambient modules
- The module compiler option

Was this page helpful?

The TypeScript compiler recognizes standard ECMAScript module syntax in TypeScript and JavaScript files and many forms of CommonJS syntax in JavaScript files.

There are also a few TypeScript-specific syntax extensions that can be used in TypeScript files and/or JSDoc comments.

Type aliases, interfaces, enums, and namespaces can be exported from a module with an export modifier, like any standard JavaScript declaration:

They can also be referenced in named exports, even alongside references to standard JavaScript declarations:

Exported types (and other TypeScript-specific declarations) can be imported with standard ECMAScript imports:

When using namespace imports or exports, exported types are available on the namespace when referenced in a type position:

When emitting imports and exports to JavaScript, by default, TypeScript automatically elides (does not emit) imports that are only used in type positions and exports that only refer to types. Type-only imports and exports can be used to force this behavior and make the elision explicit. Import declarations written with import type, export declarations written with export type { ... }, and import or export specifiers prefixed with the type keyword are all guaranteed to be elided from the output JavaScript.

Even values can be imported with import type, but since they won’t exist in the output JavaScript, they can only be used in non-emitting positions:

A type-only import declaration may not declare both a default import and named bindings, since it appears ambiguous whether type applies to the default import or to the entire import declaration. Instead, split the import declaration into two, or use default as a named binding:

TypeScript provides a type syntax similar to JavaScript’s dynamic import for referencing the type of a module without writing an import declaration:

This is especially useful in JSDoc comments in JavaScript files, where it’s not possible to import types otherwise

*[Content truncated - see full docs]*

**Examples**:

```javascript
// Standard JavaScript syntax...export function f() {}// ...extended to type declarationsexport type SomeType = /* ... */;export interface SomeInterface { /* ... */ }
```

```text
export { f, SomeType, SomeInterface };
```

```python
import { f, SomeType, SomeInterface } from "./module.js";
```

---

## Modules - Theory

**URL**: https://www.typescriptlang.org/docs/handbook/modules/theory.html

**Contents**:
- Modules - Theory
- Scripts and modules in JavaScript
- TypeScript’s job concerning modules
- Who is the host?
- The module output format
  - Module format detection
  - Input module syntax
  - ESM and CJS interoperability

Was this page helpful?

In the early days of JavaScript, when the language only ran in browsers, there were no modules, but it was still possible to split the JavaScript for a web page into multiple files by using multiple script tags in HTML:

This approach had some downsides, especially as web pages grew larger and more complex. In particular, all scripts loaded onto the same page share the same scope—appropriately called the “global scope”—meaning the scripts had to be very careful not to overwrite each others’ variables and functions.

Any system that solves this problem by giving files their own scope while still providing a way to make bits of code available to other files can be called a “module system.” (It may sound obvious to say that each file in a module system is called a “module,” but the term is often used to contrast with script files, which run outside a module system, in a global scope.)

There are many module systems, and TypeScript supports emitting several, but this documentation will focus on the two most important systems today: ECMAScript modules (ESM) and CommonJS (CJS).

ECMAScript Modules (ESM) is the module system built into the language, supported in modern browsers and in Node.js since v12. It uses dedicated import and export syntax:

CommonJS (CJS) is the module system that originally shipped in Node.js, before ESM was part of the language specification. It’s still supported in Node.js alongside ESM. It uses plain JavaScript objects and functions named exports and require:

Accordingly, when TypeScript detects that a file is a CommonJS or ECMAScript module, it starts by assuming that file will have its own scope. Beyond that, though, the compiler’s job gets a little more complicated.

The TypeScript compiler’s chief goal is to prevent certain kinds of runtime errors by catching them at compile time. With or without modules involved, the compiler needs to know about the code’s intended runtime environment—what globals are available, for

*[Content truncated - see full docs]*

**Examples**:

```text
<html>  <head>    <script src="a.js"></script>    <script src="b.js"></script>  </head>  <body></body></html>
```

```typescript
// a.jsexport default "Hello from a.js";
```

```python
// b.jsimport a from "./a.js";console.log(a); // 'Hello from a.js'
```

---

## Modules

**URL**: https://www.typescriptlang.org/docs/handbook/2/modules.html

**Contents**:
- Modules
- How JavaScript Modules are Defined
- Non-modules
- Modules in TypeScript
  - ES Module Syntax
  - Additional Import Syntax
    - TypeScript Specific ES Module Syntax
        - import type

Was this page helpful?

JavaScript has a long history of different ways to handle modularizing code. Having been around since 2012, TypeScript has implemented support for a lot of these formats, but over time the community and the JavaScript specification has converged on a format called ES Modules (or ES6 modules). You might know it as the import/export syntax.

ES Modules was added to the JavaScript spec in 2015, and by 2020 had broad support in most web browsers and JavaScript runtimes.

For focus, the handbook will cover both ES Modules and its popular pre-cursor CommonJS module.exports = syntax, and you can find information about the other module patterns in the reference section under Modules.

In TypeScript, just as in ECMAScript 2015, any file containing a top-level import or export is considered a module.

Conversely, a file without any top-level import or export declarations is treated as a script whose contents are available in the global scope (and therefore to modules as well).

Modules are executed within their own scope, not in the global scope. This means that variables, functions, classes, etc. declared in a module are not visible outside the module unless they are explicitly exported using one of the export forms. Conversely, to consume a variable, function, class, interface, etc. exported from a different module, it has to be imported using one of the import forms.

Before we start, it’s important to understand what TypeScript considers a module. The JavaScript specification declares that any JavaScript files without an import declaration, export, or top-level await should be considered a script and not a module.

Inside a script file variables and types are declared to be in the shared global scope, and it’s assumed that you’ll either use the outFile compiler option to join multiple input files into one output file, or use multiple <script> tags in your HTML to load these files (in the correct order!).

If you have a file that doesn’t currently h

*[Content truncated - see full docs]*

**Examples**:

```javascript
// @filename: hello.tsexport default function helloWorld() {  console.log("Hello, world!");}
```

```python
import helloWorld from "./hello.js";helloWorld();
```

```javascript
// @filename: maths.tsexport var pi = 3.14;export let squareTwo = 1.41;export const phi = 1.61; export class RandomNumberGenerator {} export function absolute(num: number) {  if (num < 0) return num * -1;  return num;}
```

---

## Modules .d.ts

**URL**: https://www.typescriptlang.org/docs/handbook/declaration-files/templates/module-d-ts.html

**Contents**:
- Modules .d.ts
- Comparing JavaScript to an example DTS
- Common CommonJS Patterns
  - Default Exports
- Handling Many Consuming Import
- Types in Modules
  - Namespaces in Module Code
  - Optional Global Usage

Was this page helpful?

A module using CommonJS patterns uses module.exports to describe the exported values. For example, here is a module which exports a function and a numerical constant:

This can be described by the following .d.ts:

The TypeScript playground can show you the .d.ts equivalent for JavaScript code. You can try it yourself here.

The .d.ts syntax intentionally looks like ES Modules syntax. ES Modules was ratified by TC39 in 2015 as part of ES2015 (ES6), while it has been available via transpilers for a long time, however if you have a JavaScript codebase using ES Modules:

This would have the following .d.ts equivalent:

In CommonJS you can export any value as the default export, for example here is a regular expression module:

Which can be described by the following .d.ts:

One style of exporting in CommonJS is to export a function. Because a function is also an object, then extra fields can be added and are included in the export.

Which can be described with:

See Module: Functions for details of how that works, and the Modules reference page.

There are many ways to import a module in modern consuming code:

Covering all of these cases requires the JavaScript code to actually support all of these patterns. To support many of these patterns, a CommonJS module would need to look something like:

You may want to provide a type for JavaScript code which does not exist

This can be described with:

This example is a good case for using generics to provide richer type information:

Now the type of the array propagates into the ArrayMetadata type.

The types which are exported can then be re-used by consumers of the modules using either import or import type in TypeScript code or JSDoc imports.

Trying to describe the runtime relationship of JavaScript code can be tricky. When the ES Module-like syntax doesn’t provide enough tools to describe the exports then you can use namespaces.

For example, you may have complex enough types to describe that yo

*[Content truncated - see full docs]*

**Examples**:

```javascript
const maxInterval = 12;function getArrayLength(arr) {  return arr.length;}module.exports = {  getArrayLength,  maxInterval,};
```

```javascript
export function getArrayLength(arr: any[]): number;export const maxInterval: 12;
```

```javascript
export function getArrayLength(arr) {  return arr.length;}
```

---

## More on Functions

**URL**: https://www.typescriptlang.org/docs/handbook/2/functions.html

**Contents**:
- More on Functions
- Function Type Expressions
- Call Signatures
- Construct Signatures
- Generic Functions
  - Inference
  - Constraints
  - Working with Constrained Values

Was this page helpful?

Functions are the basic building block of any application, whether they’re local functions, imported from another module, or methods on a class. They’re also values, and just like other values, TypeScript has many ways to describe how functions can be called. Let’s learn about how to write types that describe functions.

The simplest way to describe a function is with a function type expression. These types are syntactically similar to arrow functions:

The syntax (a: string) => void means “a function with one parameter, named a, of type string, that doesn’t have a return value”. Just like with function declarations, if a parameter type isn’t specified, it’s implicitly any.

Note that the parameter name is required. The function type (string) => void means “a function with a parameter named string of type any“!

Of course, we can use a type alias to name a function type:

In JavaScript, functions can have properties in addition to being callable. However, the function type expression syntax doesn’t allow for declaring properties. If we want to describe something callable with properties, we can write a call signature in an object type:

Note that the syntax is slightly different compared to a function type expression - use : between the parameter list and the return type rather than =>.

JavaScript functions can also be invoked with the new operator. TypeScript refers to these as constructors because they usually create a new object. You can write a construct signature by adding the new keyword in front of a call signature:

Some objects, like JavaScript’s Date object, can be called with or without new. You can combine call and construct signatures in the same type arbitrarily:

It’s common to write a function where the types of the input relate to the type of the output, or where the types of two inputs are related in some way. Let’s consider for a moment a function that returns the first element of an array:

This function does its job, but

*[Content truncated - see full docs]*

**Examples**:

```javascript
function greeter(fn: (a: string) => void) {  fn("Hello, World");} function printToConsole(s: string) {  console.log(s);} greeter(printToConsole);
```

```javascript
type GreetFunction = (a: string) => void;function greeter(fn: GreetFunction) {  // ...}
```

```javascript
type DescribableFunction = {  description: string;  (someArg: number): boolean;};function doSomething(fn: DescribableFunction) {  console.log(fn.description + " returned " + fn(6));} function myFunc(someArg: number) {  return someArg > 3;}myFunc.description = "default description"; doSomething(myFunc);
```

---

## Namespaces and Modules

**URL**: https://www.typescriptlang.org/docs/handbook/namespaces-and-modules.html

**Contents**:
- Namespaces and Modules
- Using Modules
- Using Namespaces
- Pitfalls of Namespaces and Modules
  - /// <reference>-ing a module
  - Needless Namespacing
  - Trade-offs of Modules
      - On this page

Was this page helpful?

This post outlines the various ways to organize your code using modules and namespaces in TypeScript. We’ll also go over some advanced topics of how to use namespaces and modules, and address some common pitfalls when using them in TypeScript.

See the Modules documentation for more information about ES Modules. See the Namespaces documentation for more information about TypeScript namespaces.

Note: In very old versions of TypeScript namespaces were called ‘Internal Modules’, these pre-date JavaScript module systems.

Modules can contain both code and declarations.

Modules also have a dependency on a module loader (such as CommonJs/Require.js) or a runtime which supports ES Modules. Modules provide for better code reuse, stronger isolation and better tooling support for bundling.

It is also worth noting that, for Node.js applications, modules are the default and we recommended modules over namespaces in modern code.

Starting with ECMAScript 2015, modules are native part of the language, and should be supported by all compliant engine implementations. Thus, for new projects modules would be the recommended code organization mechanism.

Namespaces are a TypeScript-specific way to organize code. Namespaces are simply named JavaScript objects in the global namespace. This makes namespaces a very simple construct to use. Unlike modules, they can span multiple files, and can be concatenated using outFile. Namespaces can be a good way to structure your code in a Web Application, with all dependencies included as <script> tags in your HTML page.

Just like all global namespace pollution, it can be hard to identify component dependencies, especially in a large application.

In this section we’ll describe various common pitfalls in using namespaces and modules, and how to avoid them.

A common mistake is to try to use the /// <reference ... /> syntax to refer to a module file, rather than using an import statement. To understand the distinction, we

*[Content truncated - see full docs]*

**Examples**:

```javascript
// In a .d.ts file or .ts file that is not a module:declare module "SomeModule" {  export function fn(): string;}
```

```python
/// <reference path="myModules.d.ts" />import * as m from "SomeModule";
```

```text
export namespace Shapes {  export class Triangle {    /* ... */  }  export class Square {    /* ... */  }}
```

---

## Namespaces

**URL**: https://www.typescriptlang.org/docs/handbook/namespaces.html

**Contents**:
- Namespaces
- First steps
- Validators in a single file
- Namespacing
- Namespaced Validators
- Splitting Across Files
- Multi-file namespaces
      - Validation.ts

Was this page helpful?

A note about terminology: It’s important to note that in TypeScript 1.5, the nomenclature has changed. “Internal modules” are now “namespaces”. “External modules” are now simply “modules”, as to align with ECMAScript 2015’s terminology, (namely that module X { is equivalent to the now-preferred namespace X {).

This post outlines the various ways to organize your code using namespaces (previously “internal modules”) in TypeScript. As we alluded in our note about terminology, “internal modules” are now referred to as “namespaces”. Additionally, anywhere the module keyword was used when declaring an internal module, the namespace keyword can and should be used instead. This avoids confusing new users by overloading them with similarly named terms.

Let’s start with the program we’ll be using as our example throughout this page. We’ve written a small set of simplistic string validators, as you might write to check a user’s input on a form in a webpage or check the format of an externally-provided data file.

As we add more validators, we’re going to want to have some kind of organization scheme so that we can keep track of our types and not worry about name collisions with other objects. Instead of putting lots of different names into the global namespace, let’s wrap up our objects into a namespace.

In this example, we’ll move all validator-related entities into a namespace called Validation. Because we want the interfaces and classes here to be visible outside the namespace, we preface them with export. Conversely, the variables lettersRegexp and numberRegexp are implementation details, so they are left unexported and will not be visible to code outside the namespace. In the test code at the bottom of the file, we now need to qualify the names of the types when used outside the namespace, e.g. Validation.LettersOnlyValidator.

As our application grows, we’ll want to split the code across multiple files to make it easier to maintain.

Here, we’

*[Content truncated - see full docs]*

**Examples**:

```javascript
interface StringValidator {  isAcceptable(s: string): boolean;}let lettersRegexp = /^[A-Za-z]+$/;let numberRegexp = /^[0-9]+$/;class LettersOnlyValidator implements StringValidator {  isAcceptable(s: string) {    return lettersRegexp.test(s);  }}class ZipCodeValidator implements StringValidator {  isAcceptable(s: string) {    return s.length === 5 && numberRegexp.test(s);  }}// Some samples to trylet strings = ["Hello", "98052", "101"];// Validators to uselet validators: { [s: string]: StringVal
...
```

```javascript
namespace Validation {  export interface StringValidator {    isAcceptable(s: string): boolean;  }  const lettersRegexp = /^[A-Za-z]+$/;  const numberRegexp = /^[0-9]+$/;  export class LettersOnlyValidator implements StringValidator {    isAcceptable(s: string) {      return lettersRegexp.test(s);    }  }  export class ZipCodeValidator implements StringValidator {    isAcceptable(s: string) {      return s.length === 5 && numberRegexp.test(s);    }  }}// Some samples to trylet strings = ["Hello"
...
```

```text
namespace Validation {  export interface StringValidator {    isAcceptable(s: string): boolean;  }}
```

---

## Narrowing

**URL**: https://www.typescriptlang.org/docs/handbook/2/narrowing.html

**Contents**:
- Narrowing
- typeof type guards
- Truthiness narrowing
- Equality narrowing
- The in operator narrowing
- instanceof narrowing
- Assignments
- Control flow analysis

Was this page helpful?

Imagine we have a function called padLeft.

If padding is a number, it will treat that as the number of spaces we want to prepend to input. If padding is a string, it should just prepend padding to input. Let’s try to implement the logic for when padLeft is passed a number for padding.

Uh-oh, we’re getting an error on padding. TypeScript is warning us that we’re passing a value with type number | string to the repeat function, which only accepts a number, and it’s right. In other words, we haven’t explicitly checked if padding is a number first, nor are we handling the case where it’s a string, so let’s do exactly that.

If this mostly looks like uninteresting JavaScript code, that’s sort of the point. Apart from the annotations we put in place, this TypeScript code looks like JavaScript. The idea is that TypeScript’s type system aims to make it as easy as possible to write typical JavaScript code without bending over backwards to get type safety.

While it might not look like much, there’s actually a lot going on under the covers here. Much like how TypeScript analyzes runtime values using static types, it overlays type analysis on JavaScript’s runtime control flow constructs like if/else, conditional ternaries, loops, truthiness checks, etc., which can all affect those types.

Within our if check, TypeScript sees typeof padding === "number" and understands that as a special form of code called a type guard. TypeScript follows possible paths of execution that our programs can take to analyze the most specific possible type of a value at a given position. It looks at these special checks (called type guards) and assignments, and the process of refining types to more specific types than declared is called narrowing. In many editors we can observe these types as they change, and we’ll even do so in our examples.

There are a couple of different constructs TypeScript understands for narrowing.

As we’ve seen, JavaScript supports a typeof operat

*[Content truncated - see full docs]*

**Examples**:

```javascript
function padLeft(padding: number | string, input: string): string {  throw new Error("Not implemented yet!");}
```

```javascript
function padLeft(padding: number | string, input: string): string {  return " ".repeat(padding) + input;Argument of type 'string | number' is not assignable to parameter of type 'number'.
  Type 'string' is not assignable to type 'number'.2345Argument of type 'string | number' is not assignable to parameter of type 'number'.
  Type 'string' is not assignable to type 'number'.}
```

```javascript
function padLeft(padding: number | string, input: string): string {  if (typeof padding === "number") {    return " ".repeat(padding) + input;  }  return padding + input;}
```

---

## Nightly Builds

**URL**: https://www.typescriptlang.org/docs/handbook/nightly-builds.html

**Contents**:
- Nightly Builds
- Using npm
- Updating your IDE to use the nightly builds
  - Visual Studio Code
  - Sublime Text
  - Visual Studio 2013 and 2015
  - IntelliJ IDEA (Mac)
  - IntelliJ IDEA (Windows)

Was this page helpful?

A nightly build from the TypeScript’s main branch is published by midnight PST to npm. Here is how you can get it and use it with your tools.

You can also update your editor/IDE to use the nightly drop. You will typically need to install the package through npm. The rest of this section mostly assumes typescript@next is already installed.

The VS Code website has documentation on selecting a workspace version of TypeScript. After installing a nightly version of TypeScript in your workspace, you can follow directions there, or simply update your workspace settings in the JSON view. A direct way to do this is to open or create your workspace’s .vscode/settings.json and add the following property:

Alternatively, if you simply want to run the nightly editing experience for JavaScript and TypeScript in Visual Studio Code without changing your workspace version, you can run the JavaScript and TypeScript Nightly Extension

Update the Settings - User file with the following:

More information is available at the TypeScript Plugin for Sublime Text installation documentation.

Note: Most changes do not require you to install a new version of the VS TypeScript plugin.

The nightly build currently does not include the full plugin setup, but we are working on publishing an installer on a nightly basis as well.

Download the VSDevMode.ps1 script.

Also see our wiki page on using a custom language service file.

From a PowerShell command window, run:

Go to Preferences > Languages & Frameworks > TypeScript:

TypeScript Version: If you installed with npm: /usr/local/lib/node_modules/typescript/lib

Go to File > Settings > Languages & Frameworks > TypeScript:

TypeScript Version: If you installed with npm: C:\Users\USERNAME\AppData\Roaming\npm\node_modules\typescript\lib

The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤

Last updated: Oct 13, 2025

**Examples**:

```text
npm install -D typescript@next
```

```text
"typescript.tsdk": "<path to your folder>/node_modules/typescript/lib"
```

```text
"typescript_tsdk": "<path to your folder>/node_modules/typescript/lib"
```

---

## Object Types

**URL**: https://www.typescriptlang.org/docs/handbook/2/objects.html

**Contents**:
- Object Types
- Quick Reference
- Property Modifiers
  - Optional Properties
  - readonly Properties
  - Index Signatures
- Excess Property Checks
- Extending Types

Was this page helpful?

In JavaScript, the fundamental way that we group and pass around data is through objects. In TypeScript, we represent those through object types.

As we’ve seen, they can be anonymous:

or they can be named by using either an interface:

In all three examples above, we’ve written functions that take objects that contain the property name (which must be a string) and age (which must be a number).

We have cheat-sheets available for both type and interface, if you want a quick look at the important every-day syntax at a glance.

Each property in an object type can specify a couple of things: the type, whether the property is optional, and whether the property can be written to.

Much of the time, we’ll find ourselves dealing with objects that might have a property set. In those cases, we can mark those properties as optional by adding a question mark (?) to the end of their names.

In this example, both xPos and yPos are considered optional. We can choose to provide either of them, so every call above to paintShape is valid. All optionality really says is that if the property is set, it better have a specific type.

We can also read from those properties - but when we do under strictNullChecks, TypeScript will tell us they’re potentially undefined.

In JavaScript, even if the property has never been set, we can still access it - it’s just going to give us the value undefined. We can just handle undefined specially by checking for it.

Note that this pattern of setting defaults for unspecified values is so common that JavaScript has syntax to support it.

Here we used a destructuring pattern for paintShape’s parameter, and provided default values for xPos and yPos. Now xPos and yPos are both definitely present within the body of paintShape, but optional for any callers to paintShape.

Note that there is currently no way to place type annotations within destructuring patterns. This is because the following syntax already means something different

*[Content truncated - see full docs]*

**Examples**:

```javascript
function greet(person: { name: string; age: number }) {  return "Hello " + person.name;}
```

```javascript
interface Person {  name: string;  age: number;} function greet(person: Person) {  return "Hello " + person.name;}
```

```javascript
type Person = {  name: string;  age: number;}; function greet(person: Person) {  return "Hello " + person.name;}
```

---

## Project References

**URL**: https://www.typescriptlang.org/docs/handbook/project-references.html

**Contents**:
- Project References
- An Example Project
- What is a Project Reference?
- composite
- declarationMap
- Caveats for Project References
- Build Mode for TypeScript
  - tsc -b Commandline

Was this page helpful?

Project references allows you to structure your TypeScript programs into smaller pieces, available in TypeScript 3.0 and newer.

By doing this, you can greatly improve build times, enforce logical separation between components, and organize your code in new and better ways.

We’re also introducing a new mode for tsc, the --build flag, that works hand in hand with project references to enable faster TypeScript builds.

Let’s look at a fairly normal program and see how project references can help us better organize it. Imagine you have a project with two modules, converter and units, and a corresponding test file for each:

The test files import the implementation files and do some testing:

Previously, this structure was rather awkward to work with if you used a single tsconfig file:

You could use multiple tsconfig files to solve some of those problems, but new ones would appear:

Project references can solve all of these problems and more.

tsconfig.json files have a new top-level property, references. It’s an array of objects that specifies projects to reference:

The path property of each reference can point to a directory containing a tsconfig.json file, or to the config file itself (which may have any name).

When you reference a project, new things happen:

By separating into multiple projects, you can greatly improve the speed of typechecking and compiling, reduce memory usage when using an editor, and improve enforcement of the logical groupings of your program.

Referenced projects must have the new composite setting enabled. This setting is needed to ensure TypeScript can quickly determine where to find the outputs of the referenced project. Enabling the composite flag changes a few things:

We’ve also added support for declaration source maps. If you enable declarationMap, you’ll be able to use editor features like “Go to Definition” and Rename to transparently navigate and edit code across project boundaries in supported editors.


*[Content truncated - see full docs]*

**Examples**:

```text
/├── src/│   ├── converter.ts│   └── units.ts├── test/│   ├── converter-tests.ts│   └── units-tests.ts└── tsconfig.json
```

```python
// converter-tests.tsimport * as converter from "../src/converter";assert.areEqual(converter.celsiusToFahrenheit(0), 32);
```

```text
{    "compilerOptions": {        // The usual    },    "references": [        { "path": "../src" }    ]}
```

---

## Publishing

**URL**: https://www.typescriptlang.org/docs/handbook/declaration-files/publishing.html

**Contents**:
- Publishing
- Including declarations in your npm package
- Dependencies
- Red flags
  - /// <reference path="..." />
  - Packaging dependent declarations
- Version selection with typesVersions
    - Folder redirects (using *)

Was this page helpful?

Now that you have authored a declaration file following the steps of this guide, it is time to publish it to npm. There are two main ways you can publish your declaration files to npm:

If your types are generated by your source code, publish the types with your source code. Both TypeScript and JavaScript projects can generate types via declaration.

Otherwise, we recommend submitting the types to DefinitelyTyped, which will publish them to the @types organization on npm.

If your package has a main .js file, you will need to indicate the main declaration file in your package.json file as well. Set the types property to point to your bundled declaration file. For example:

Note that the "typings" field is synonymous with types, and could be used as well.

All dependencies are managed by npm. Make sure all the declaration packages you depend on are marked appropriately in the "dependencies" section in your package.json. For example, imagine we authored a package that used Browserify and TypeScript.

Here, our package depends on the browserify and typescript packages. browserify does not bundle its declaration files with its npm packages, so we needed to depend on @types/browserify for its declarations. typescript, on the other hand, packages its declaration files, so there was no need for any additional dependencies.

Our package exposes declarations from each of those, so any user of our browserify-typescript-extension package needs to have these dependencies as well. For that reason, we used "dependencies" and not "devDependencies", because otherwise our consumers would have needed to manually install those packages. If we had just written a command line application and not expected our package to be used as a library, we might have used devDependencies.

Don’t use /// <reference path="..." /> in your declaration files.

Do use /// <reference types="..." /> instead.

Make sure to revisit the Consuming dependencies section for more informatio

*[Content truncated - see full docs]*

**Examples**:

```text
{  "name": "awesome",  "author": "Vandelay Industries",  "version": "1.0.0",  "main": "./lib/main.js",  "types": "./lib/main.d.ts"}
```

```text
{  "name": "browserify-typescript-extension",  "author": "Vandelay Industries",  "version": "1.0.0",  "main": "./lib/main.js",  "types": "./lib/main.d.ts",  "dependencies": {    "browserify": "latest",    "@types/browserify": "latest",    "typescript": "next"  }}
```

```text
/// <reference path="../typescript/lib/typescriptServices.d.ts" />....
```

---

## Symbols

**URL**: https://www.typescriptlang.org/docs/handbook/symbols.html

**Contents**:
- Symbols
- unique symbol
- Well-known Symbols
  - Symbol.asyncIterator
  - Symbol.hasInstance
  - Symbol.isConcatSpreadable
  - Symbol.iterator
  - Symbol.match

Was this page helpful?

Starting with ECMAScript 2015, symbol is a primitive data type, just like number and string.

symbol values are created by calling the Symbol constructor.

Symbols are immutable, and unique.

Just like strings, symbols can be used as keys for object properties.

Symbols can also be combined with computed property declarations to declare object properties and class members.

To enable treating symbols as unique literals a special type unique symbol is available. unique symbol is a subtype of symbol, and are produced only from calling Symbol() or Symbol.for(), or from explicit type annotations. This type is only allowed on const declarations and readonly static properties, and in order to reference a specific unique symbol, you’ll have to use the typeof operator. Each reference to a unique symbol implies a completely unique identity that’s tied to a given declaration.

Because each unique symbol has a completely separate identity, no two unique symbol types are assignable or comparable to each other.

In addition to user-defined symbols, there are well-known built-in symbols. Built-in symbols are used to represent internal language behaviors.

Here is a list of well-known symbols:

A method that returns async iterator for an object, compatible to be used with for await..of loop.

A method that determines if a constructor object recognizes an object as one of the constructor’s instances. Called by the semantics of the instanceof operator.

A Boolean value indicating that an object should be flattened to its array elements by Array.prototype.concat.

A method that returns the default iterator for an object. Called by the semantics of the for-of statement.

A regular expression method that matches the regular expression against a string. Called by the String.prototype.match method.

A regular expression method that replaces matched substrings of a string. Called by the String.prototype.replace method.

A regular expression method that returns the 

*[Content truncated - see full docs]*

**Examples**:

```javascript
let sym1 = Symbol();let sym2 = Symbol("key"); // optional string key
```

```javascript
let sym2 = Symbol("key");let sym3 = Symbol("key");sym2 === sym3; // false, symbols are unique
```

```javascript
const sym = Symbol();let obj = {  [sym]: "value",};console.log(obj[sym]); // "value"
```

---

## Template Literal Types

**URL**: https://www.typescriptlang.org/docs/handbook/2/template-literal-types.html

**Contents**:
- Template Literal Types
  - String Unions in Types
  - Inference with Template Literals
- Intrinsic String Manipulation Types
  - Uppercase<StringType>
      - Example
  - Lowercase<StringType>
      - Example

Was this page helpful?

Template literal types build on string literal types, and have the ability to expand into many strings via unions.

They have the same syntax as template literal strings in JavaScript, but are used in type positions. When used with concrete literal types, a template literal produces a new string literal type by concatenating the contents.

When a union is used in the interpolated position, the type is the set of every possible string literal that could be represented by each union member:

For each interpolated position in the template literal, the unions are cross multiplied:

We generally recommend that people use ahead-of-time generation for large string unions, but this is useful in smaller cases.

The power in template literals comes when defining a new string based on information inside a type.

Consider the case where a function (makeWatchedObject) adds a new function called on() to a passed object. In JavaScript, its call might look like: makeWatchedObject(baseObject). We can imagine the base object as looking like:

The on function that will be added to the base object expects two arguments, an eventName (a string) and a callback (a function).

The eventName should be of the form attributeInThePassedObject + "Changed"; thus, firstNameChanged as derived from the attribute firstName in the base object.

The callback function, when called:

The naive function signature of on() might thus be: on(eventName: string, callback: (newValue: any) => void). However, in the preceding description, we identified important type constraints that we’d like to document in our code. Template Literal types let us bring these constraints into our code.

Notice that on listens on the event "firstNameChanged", not just "firstName". Our naive specification of on() could be made more robust if we were to ensure that the set of eligible event names was constrained by the union of attribute names in the watched object with “Changed” added at the end. While we a

*[Content truncated - see full docs]*

**Examples**:

```text
type World = "world"; type Greeting = `hello ${World}`;        type Greeting = "hello world"
```

```text
type EmailLocaleIDs = "welcome_email" | "email_heading";type FooterLocaleIDs = "footer_title" | "footer_sendoff"; type AllLocaleIDs = `${EmailLocaleIDs | FooterLocaleIDs}_id`;          type AllLocaleIDs = "welcome_email_id" | "email_heading_id" | "footer_title_id" | "footer_sendoff_id"
```

```text
type AllLocaleIDs = `${EmailLocaleIDs | FooterLocaleIDs}_id`;type Lang = "en" | "ja" | "pt"; type LocaleMessageIDs = `${Lang}_${AllLocaleIDs}`;            type LocaleMessageIDs = "en_welcome_email_id" | "en_email_heading_id" | "en_footer_title_id" | "en_footer_sendoff_id" | "ja_welcome_email_id" | "ja_email_heading_id" | "ja_footer_title_id" | "ja_footer_sendoff_id" | "pt_welcome_email_id" | "pt_email_heading_id" | "pt_footer_title_id" | "pt_footer_sendoff_id"
```

---

## Templates

**URL**: https://www.typescriptlang.org/docs/handbook/declaration-files/templates.html

**Contents**:
- Templates
      - On this page
      - Is this page helpful?

Was this page helpful?

global-modifying-module.d.ts

The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤

Last updated: Oct 13, 2025

---

## The Basics

**URL**: https://www.typescriptlang.org/docs/handbook/2/basic-types.html

**Contents**:
- The Basics
- Static type-checking
- Non-exception Failures
- Types for Tooling
- tsc, the TypeScript compiler
- Emitting with Errors
- Explicit Types
- Erased Types

Was this page helpful?

Welcome to the first page of the handbook. If this is your first experience with TypeScript - you may want to start at one of the 'Getting Started' guides

Each and every value in JavaScript has a set of behaviors you can observe from running different operations. That sounds abstract, but as a quick example, consider some operations we might run on a variable named message.

If we break this down, the first runnable line of code accesses a property called toLowerCase and then calls it. The second one tries to call message directly.

But assuming we don’t know the value of message - and that’s pretty common - we can’t reliably say what results we’ll get from trying to run any of this code. The behavior of each operation depends entirely on what value we had in the first place.

The answers to these questions are usually things we keep in our heads when we write JavaScript, and we have to hope we got all the details right.

Let’s say message was defined in the following way.

As you can probably guess, if we try to run message.toLowerCase(), we’ll get the same string only in lower-case.

What about that second line of code? If you’re familiar with JavaScript, you’ll know this fails with an exception:

It’d be great if we could avoid mistakes like this.

When we run our code, the way that our JavaScript runtime chooses what to do is by figuring out the type of the value - what sorts of behaviors and capabilities it has. That’s part of what that TypeError is alluding to - it’s saying that the string "Hello World!" cannot be called as a function.

For some values, such as the primitives string and number, we can identify their type at runtime using the typeof operator. But for other things like functions, there’s no corresponding runtime mechanism to identify their types. For example, consider this function:

We can observe by reading the code that this function will only work if given an object with a callable flip property, but JavaScript doesn

*[Content truncated - see full docs]*

**Examples**:

```text
// Accessing the property 'toLowerCase'// on 'message' and then calling itmessage.toLowerCase();// Calling 'message'message();
```

```javascript
const message = "Hello World!";
```

```javascript
TypeError: message is not a function
```

---

## The TypeScript Handbook

**URL**: https://www.typescriptlang.org/docs/handbook/intro.html

**Contents**:
- The TypeScript Handbook
- About this Handbook
- How is this Handbook Structured
  - Non-Goals
- Get Started
      - On this page
      - Is this page helpful?
  - The Basics

Was this page helpful?

Over 20 years after its introduction to the programming community, JavaScript is now one of the most widespread cross-platform languages ever created. Starting as a small scripting language for adding trivial interactivity to webpages, JavaScript has grown to be a language of choice for both frontend and backend applications of every size. While the size, scope, and complexity of programs written in JavaScript has grown exponentially, the ability of the JavaScript language to express the relationships between different units of code has not. Combined with JavaScript’s rather peculiar runtime semantics, this mismatch between language and program complexity has made JavaScript development a difficult task to manage at scale.

The most common kinds of errors that programmers write can be described as type errors: a certain kind of value was used where a different kind of value was expected. This could be due to simple typos, a failure to understand the API surface of a library, incorrect assumptions about runtime behavior, or other errors. The goal of TypeScript is to be a static typechecker for JavaScript programs - in other words, a tool that runs before your code runs (static) and ensures that the types of the program are correct (typechecked).

If you are coming to TypeScript without a JavaScript background, with the intention of TypeScript being your first language, we recommend you first start reading the documentation on either the Microsoft Learn JavaScript tutorial or read JavaScript at the Mozilla Web Docs. If you have experience in other languages, you should be able to pick up JavaScript syntax quite quickly by reading the handbook.

The handbook is split into two sections:

The TypeScript Handbook is intended to be a comprehensive document that explains TypeScript to everyday programmers. You can read the handbook by going from top to bottom in the left-hand navigation.

You should expect each chapter or page to provide you with a s

*[Content truncated - see full docs]*

---

## Triple-Slash Directives

**URL**: https://www.typescriptlang.org/docs/handbook/triple-slash-directives.html

**Contents**:
- Triple-Slash Directives
- /// <reference path="..." />
  - Preprocessing input files
  - Errors
  - Using --noResolve
- /// <reference types="..." />
- /// <reference lib="..." />
- /// <reference no-default-lib="true"/>

Was this page helpful?

Triple-slash directives are single-line comments containing a single XML tag. The contents of the comment are used as compiler directives.

Triple-slash directives are only valid at the top of their containing file. A triple-slash directive can only be preceded by single or multi-line comments, including other triple-slash directives. If they are encountered following a statement or a declaration they are treated as regular single-line comments, and hold no special meaning.

As of TypeScript 5.5, the compiler does not generate reference directives, and does not emit handwritten triple-slash directives to output files unless those directives are marked as preserve="true".

The /// <reference path="..." /> directive is the most common of this group. It serves as a declaration of dependency between files.

Triple-slash references instruct the compiler to include additional files in the compilation process.

They also serve as a method to order the output when using out or outFile. Files are emitted to the output file location in the same order as the input after preprocessing pass.

The compiler performs a preprocessing pass on input files to resolve all triple-slash reference directives. During this process, additional files are added to the compilation.

The process starts with a set of root files; these are the file names specified on the command-line or in the files list in the tsconfig.json file. These root files are preprocessed in the same order they are specified. Before a file is added to the list, all triple-slash references in it are processed, and their targets included. Triple-slash references are resolved in a depth-first manner, in the order they have been seen in the file.

A triple-slash reference path is resolved relative to the containing file, if a relative path is used.

It is an error to reference a file that does not exist. It is an error for a file to have a triple-slash reference to itself.

If the compiler flag noResolv

*[Content truncated - see full docs]*

**Examples**:

```text
/// <reference lib="es2017.string" />"foo".padStart(4);
```

```text
/// <amd-module name="NamedModule"/>export class C {}
```

```javascript
define("NamedModule", ["require", "exports"], function (require, exports) {  var C = (function () {    function C() {}    return C;  })();  exports.C = C;});
```

---

## TypeScript 1.1

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-1-1.html

**Contents**:
- TypeScript 1.1
- Performance Improvements
- Better Module Visibility Rules
      - On this page
      - Is this page helpful?

Was this page helpful?

The 1.1 compiler is typically around 4x faster than any previous release. See this blog post for some impressive charts.

TypeScript now only strictly enforces the visibility of types in modules if the declaration flag is provided. This is very useful for Angular scenarios, for example:

The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤

Last updated: Oct 13, 2025

**Examples**:

```text
module MyControllers {  interface ZooScope extends ng.IScope {    animals: Animal[];  }  export class ZooController {    // Used to be an error (cannot expose ZooScope), but now is only    // an error when trying to generate .d.ts files    constructor(public $scope: ZooScope) {}    /* more code */  }}
```

---

## TypeScript 1.3

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-1-3.html

**Contents**:
- TypeScript 1.3
- Protected
- Tuple types
      - On this page
      - Is this page helpful?

Was this page helpful?

The new protected modifier in classes works like it does in familiar languages like C++, C#, and Java. A protected member of a class is visible only inside subclasses of the class in which it is declared:

Tuple types express an array where the type of certain elements is known, but need not be the same. For example, you may want to represent an array with a string at position 0 and a number at position 1:

When accessing an element with a known index, the correct type is retrieved:

Note that in TypeScript 1.4, when accessing an element outside the set of known indices, a union type is used instead:

The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤

Last updated: Oct 13, 2025

**Examples**:

```text
class Thing {  protected doSomething() {    /* ... */  }}class MyThing extends Thing {  public myMethod() {    // OK, can access protected member from subclass    this.doSomething();  }}var t = new MyThing();t.doSomething(); // Error, cannot call protected member from outside class
```

```text
// Declare a tuple typevar x: [string, number];// Initialize itx = ["hello", 10]; // OK// Initialize it incorrectlyx = [10, "hello"]; // Error
```

```text
console.log(x[0].substr(1)); // OKconsole.log(x[1].substr(1)); // Error, 'number' does not have 'substr'
```

---

## TypeScript 1.4

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-1-4.html

**Contents**:
- TypeScript 1.4
- Union types
  - Overview
  - Stricter Generics
  - Better Type Inference
- let declarations
- const declarations
- Template strings

Was this page helpful?

Union types are a powerful way to express a value that can be one of several types. For example, you might have an API for running a program that takes a commandline as either a string, a string[] or a function that returns a string. You can now write:

Assignment to union types works very intuitively — anything you could assign to one of the union type’s members is assignable to the union:

When reading from a union type, you can see any properties that are shared by them:

Using Type Guards, you can easily work with a variable of a union type:

With union types able to represent a wide range of type scenarios, we’ve decided to improve the strictness of certain generic calls. Previously, code like this would (surprisingly) compile without error:

With union types, you can now specify the desired behavior at both the function declaration site and the call site:

Union types also allow for better type inference in arrays and other places where you might have multiple kinds of values in a collection:

In JavaScript, var declarations are “hoisted” to the top of their enclosing scope. This can result in confusing bugs:

The new ES6 keyword let, now supported in TypeScript, declares a variable with more intuitive “block” semantics. A let variable can only be referred to after its declaration, and is scoped to the syntactic block where it is defined:

let is only available when targeting ECMAScript 6 (--target ES6).

The other new ES6 declaration type supported in TypeScript is const. A const variable may not be assigned to, and must be initialized where it is declared. This is useful for declarations where you don’t want to change the value after its initialization:

const is only available when targeting ECMAScript 6 (--target ES6).

TypeScript now supports ES6 template strings. These are an easy way to embed arbitrary expressions in strings:

When compiling to pre-ES6 targets, the string is decomposed:

A common pattern in JavaScript is to use t

*[Content truncated - see full docs]*

**Examples**:

```javascript
interface RunOptions {  program: string;  commandline: string[] | string | (() => string);}
```

```text
var opts: RunOptions = /* ... */;opts.commandline = '-hello world'; // OKopts.commandline = ['-hello', 'world']; // OKopts.commandline = [42]; // Error, number is not string or string[]
```

```text
if (opts.commandline.length === 0) {  // OK, string and string[] both have 'length' property  console.log("it's empty");}
```

---

## TypeScript 1.5

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-1-5.html

**Contents**:
- TypeScript 1.5
- ES6 Modules
    - Export Declarations
    - Re-exporting
    - Default Export
    - Bare Import
- Destructuring in declarations and assignments
    - Declarations

Was this page helpful?

TypeScript 1.5 supports ECMAScript 6 (ES6) modules. ES6 modules are effectively TypeScript external modules with a new syntax: ES6 modules are separately loaded source files that possibly import other modules and provide a number of externally accessible exports. ES6 modules feature several new export and import declarations. It is recommended that TypeScript libraries and applications be updated to use the new syntax, but this is not a requirement. The new ES6 module syntax coexists with TypeScript’s original internal and external module constructs and the constructs can be mixed and matched at will.

In addition to the existing TypeScript support for decorating declarations with export, module members can also be exported using separate export declarations, optionally specifying different names for exports using as clauses.

Import declarations, as well, can optionally use as clauses to specify different local names for the imports. For example:

As an alternative to individual imports, a namespace import can be used to import an entire module:

Using from clause a module can copy the exports of a given module to the current module without introducing local names.

export * can be used to re-export all exports of another module. This is useful for creating modules that aggregate the exports of several other modules.

An export default declaration specifies an expression that becomes the default export of a module:

Which in turn can be imported using default imports:

A “bare import” can be used to import a module only for its side-effects.

For more information about module, please see the ES6 module support spec.

TypeScript 1.5 adds support to ES6 destructuring declarations and assignments.

A destructuring declaration introduces one or more named variables and initializes them with values extracted from properties of an object or elements of an array.

For example, the following sample declares variables x, y, and z, and initializes the

*[Content truncated - see full docs]*

**Examples**:

```javascript
interface Stream { ... }function writeToStream(stream: Stream, data: string) { ... }export { Stream, writeToStream as write };  // writeToStream exported as write
```

```python
import { read, write, standardOutput as stdout } from "./inout";var s = read(stdout);write(stdout, s);
```

```python
import * as io from "./inout";var s = io.read(io.standardOutput);io.write(io.standardOutput, s);
```

---

## TypeScript 1.6

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-1-6.html

**Contents**:
- TypeScript 1.6
- JSX support
    - New .tsx file extension and as operator
    - Using React
    - Using other JSX frameworks
    - Output generation
- Intersection types
      - Example

Was this page helpful?

JSX is an embeddable XML-like syntax. It is meant to be transformed into valid JavaScript, but the semantics of that transformation are implementation-specific. JSX came to popularity with the React library but has since seen other applications. TypeScript 1.6 supports embedding, type checking, and optionally compiling JSX directly into JavaScript.

TypeScript 1.6 introduces a new .tsx file extension. This extension does two things: it enables JSX inside of TypeScript files, and it makes the new as operator the default way to cast (removing any ambiguity between JSX expressions and the TypeScript prefix cast operator). For example:

To use JSX-support with React you should use the React typings. These typings define the JSX namespace so that TypeScript can correctly check JSX expressions for React. For example:

JSX element names and properties are validated against the JSX namespace. Please see the [[JSX]] wiki page for defining the JSX namespace for your framework.

TypeScript ships with two JSX modes: preserve and react.

See the [[JSX]] wiki page for more information on using JSX in TypeScript.

TypeScript 1.6 introduces intersection types, the logical complement of union types. A union type A | B represents an entity that is either of type A or type B, whereas an intersection type A & B represents an entity that is both of type A and type B.

See issue #1256 for more information.

Local class, interface, enum, and type alias declarations can now appear inside function declarations. Local types are block scoped, similar to variables declared with let and const. For example:

The inferred return type of a function may be a type declared locally within the function. It is not possible for callers of the function to reference such a local type, but it can of course be matched structurally. For example:

Local types may reference enclosing type parameters and local class and interfaces may themselves be generic. For example:

TypeScript 1.6 a

*[Content truncated - see full docs]*

**Examples**:

```text
var x = <any>foo;// is equivalent to:var x = foo as any;
```

```text
/// <reference path="react.d.ts" />interface Props {  name: string;}class MyComponent extends React.Component<Props, {}> {  render() {    return <span>{this.props.name}</span>;  }}<MyComponent name="bar" />; // OK<MyComponent name={0} />; // error, `name` is not a number
```

```javascript
function extend<T, U>(first: T, second: U): T & U {  let result = <T & U>{};  for (let id in first) {    result[id] = first[id];  }  for (let id in second) {    if (!result.hasOwnProperty(id)) {      result[id] = second[id];    }  }  return result;}var x = extend({ a: "hello" }, { b: 42 });var s = x.a;var n = x.b;
```

---

## TypeScript 1.7

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-1-7.html

**Contents**:
- TypeScript 1.7
- async/await support in ES6 targets (Node v4+)
      - Example
- Support for --target ES6 with --module
      - Example
- this-typing
- ES7 exponentiation operator
      - Example

Was this page helpful?

TypeScript now supports asynchronous functions for engines that have native support for ES6 generators, e.g. Node v4 and above. Asynchronous functions are prefixed with the async keyword; await suspends the execution until an asynchronous function return promise is fulfilled and unwraps the value from the Promise returned.

In the following example, each input element will be printed out one at a time with a 400ms delay:

For more information see async function reference reference.

TypeScript 1.7 adds ES6 to the list of options available for the module option and allows you to specify the module output when targeting ES6. This provides more flexibility to target exactly the features you want in specific runtimes.

It is a common pattern to return the current object (i.e. this) from a method to create fluent-style APIs. For instance, consider the following BasicCalculator module:

A user could express 2 * 5 + 1 as

This often opens up very elegant ways of writing code; however, there was a problem for classes that wanted to extend from BasicCalculator. Imagine a user wanted to start writing a ScientificCalculator:

Because TypeScript used to infer the type BasicCalculator for each method in BasicCalculator that returned this, the type system would forget that it had ScientificCalculator whenever using a BasicCalculator method.

This is no longer the case - TypeScript now infers this to have a special type called this whenever inside an instance method of a class. The this type is written as so, and basically means “the type of the left side of the dot in a method call”.

The this type is also useful with intersection types in describing libraries (e.g. Ember.js) that use mixin-style patterns to describe inheritance:

TypeScript 1.7 supports upcoming ES7/ES2016 exponentiation operators: ** and **=. The operators will be transformed in the output to ES3/ES5 using Math.pow.

Will generate the following JavaScript output:

TypeScript 1.7 makes ch

*[Content truncated - see full docs]*

**Examples**:

```javascript
"use strict";// printDelayed is a 'Promise<void>'async function printDelayed(elements: string[]) {  for (const element of elements) {    await delay(400);    console.log(element);  }}async function delay(milliseconds: number) {  return new Promise<void>((resolve) => {    setTimeout(resolve, milliseconds);  });}printDelayed(["Hello", "beautiful", "asynchronous", "world"]).then(() => {  console.log();  console.log("Printed every element!");});
```

```text
{  "compilerOptions": {    "module": "amd",    "target": "es6"  }}
```

```typescript
export default class BasicCalculator {  public constructor(protected value: number = 0) {}  public currentValue(): number {    return this.value;  }  public add(operand: number) {    this.value += operand;    return this;  }  public subtract(operand: number) {    this.value -= operand;    return this;  }  public multiply(operand: number) {    this.value *= operand;    return this;  }  public divide(operand: number) {    this.value /= operand;    return this;  }}
```

---

## TypeScript 1.8

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-1-8.html

**Contents**:
- TypeScript 1.8
- Type parameters as constraints
      - Example
- Control flow analysis errors
  - Unreachable code
      - Example
  - Unused labels
      - Example

Was this page helpful?

With TypeScript 1.8 it becomes possible for a type parameter constraint to reference type parameters from the same type parameter list. Previously this was an error. This capability is usually referred to as F-Bounded Polymorphism.

TypeScript 1.8 introduces control flow analysis to help catch common errors that users tend to run into. Read on to get more details, and check out these errors in action:

Statements guaranteed to not be executed at run time are now correctly flagged as unreachable code errors. For instance, statements following unconditional return, throw, break or continue statements are considered unreachable. Use allowUnreachableCode to disable unreachable code detection and reporting.

Here’s a simple example of an unreachable code error:

A more common error that this feature catches is adding a newline after a return statement:

Since JavaScript automatically terminates the return statement at the end of the line, the object literal becomes a block.

Unused labels are also flagged. Just like unreachable code checks, these are turned on by default; use allowUnusedLabels to stop reporting these errors.

Functions with code paths that do not return a value in JS implicitly return undefined. These can now be flagged by the compiler as implicit returns. The check is turned off by default; use noImplicitReturns to turn it on.

TypeScript can reports errors for fall-through cases in switch statement where the case clause is non-empty. This check is turned off by default, and can be enabled using noFallthroughCasesInSwitch.

With noFallthroughCasesInSwitch, this example will trigger an error:

However, in the following example, no error will be reported because the fall-through case is empty:

TypeScript now supports Function components. These are lightweight components that easily compose other components:

For this feature and simplified props, be sure to use the latest version of react.d.ts.

In TypeScript 1.8 with the latest v

*[Content truncated - see full docs]*

**Examples**:

```javascript
function assign<T extends U, U>(target: T, source: U): T {  for (let id in source) {    target[id] = source[id];  }  return target;}let x = { a: 1, b: 2, c: 3, d: 4 };assign(x, { b: 10, d: 20 });assign(x, { e: 0 }); // Error
```

```javascript
function f(x) {  if (x) {    return true;  } else {    return false;  }  x = 0; // Error: Unreachable code detected.}
```

```javascript
function f() {  return; // Automatic Semicolon Insertion triggered at newline  {    x: "string"; // Error: Unreachable code detected.  }}
```

---

## TypeScript 2.0

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html

**Contents**:
- TypeScript 2.0
- Null- and undefined-aware types
- --strictNullChecks
      - Example
- Assigned-before-use checking
      - Example
- Optional parameters and properties
- Non-null and non-undefined type guards

Was this page helpful?

TypeScript has two special types, Null and Undefined, that have the values null and undefined respectively. Previously it was not possible to explicitly name these types, but null and undefined may now be used as type names regardless of type checking mode.

The type checker previously considered null and undefined assignable to anything. Effectively, null and undefined were valid values of every type and it wasn’t possible to specifically exclude them (and therefore not possible to detect erroneous use of them).

strictNullChecks switches to a new strict null checking mode.

In strict null checking mode, the null and undefined values are not in the domain of every type and are only assignable to themselves and any (the one exception being that undefined is also assignable to void). So, whereas T and T | undefined are considered synonymous in regular type checking mode (because undefined is considered a subtype of any T), they are different types in strict type checking mode, and only T | undefined permits undefined values. The same is true for the relationship of T to T | null.

In strict null checking mode the compiler requires every reference to a local variable of a type that doesn’t include undefined to be preceded by an assignment to that variable in every possible preceding code path.

The compiler checks that variables are definitely assigned by performing control flow based type analysis. See later for further details on this topic.

Optional parameters and properties automatically have undefined added to their types, even when their type annotations don’t specifically include undefined. For example, the following two types are identical:

A property access or a function call produces a compile-time error if the object or function is of a type that includes null or undefined. However, type guards are extended to support non-null and non-undefined checks.

Non-null and non-undefined type guards may use the ==, !=, ===, or !== operator

*[Content truncated - see full docs]*

**Examples**:

```javascript
// Compiled with --strictNullCheckslet x: number;let y: number | undefined;let z: number | null | undefined;x = 1; // Oky = 1; // Okz = 1; // Okx = undefined; // Errory = undefined; // Okz = undefined; // Okx = null; // Errory = null; // Errorz = null; // Okx = y; // Errorx = z; // Errory = x; // Oky = z; // Errorz = x; // Okz = y; // Ok
```

```javascript
// Compiled with --strictNullCheckslet x: number;let y: number | null;let z: number | undefined;x; // Error, reference not preceded by assignmenty; // Error, reference not preceded by assignmentz; // Okx = 1;y = null;x; // Oky; // Ok
```

```javascript
// Compiled with --strictNullCheckstype T1 = (x?: number) => string; // x has type number | undefinedtype T2 = (x?: number | undefined) => string; // x has type number | undefined
```

---

## TypeScript 2.1

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-1.html

**Contents**:
- TypeScript 2.1
- keyof and Lookup Types
      - Example
      - Example
- Mapped Types
- Partial, Readonly, Record, and Pick
- Object Spread and Rest
- Downlevel Async Functions

Was this page helpful?

In JavaScript it is fairly common to have APIs that expect property names as parameters, but so far it hasn’t been possible to express the type relationships that occur in those APIs.

Enter Index Type Query or keyof; An indexed type query keyof T yields the type of permitted property names for T. A keyof T type is considered a subtype of string.

The dual of this is indexed access types, also called lookup types. Syntactically, they look exactly like an element access, but are written as types:

You can use this pattern with other parts of the type system to get type-safe lookups.

One common task is to take an existing type and make each of its properties entirely optional. Let’s say we have a Person:

A partial version of it would be:

with Mapped types, PartialPerson can be written as a generalized transformation on the type Person as:

Mapped types are produced by taking a union of literal types, and computing a set of properties for a new object type. They’re like list comprehensions in Python, but instead of producing new elements in a list, they produce new properties in a type.

In addition to Partial, Mapped Types can express many useful transformations on types:

Partial and Readonly, as described earlier, are very useful constructs. You can use them to describe some common JS routines like:

Because of that, they are now included by default in the standard library.

We’re also including two other utility types as well: Record and Pick.

TypeScript 2.1 brings support for ESnext Spread and Rest.

Similar to array spread, spreading an object can be handy to get a shallow copy:

Similarly, you can merge several different objects. In the following example, merged will have properties from foo, bar, and baz.

You can also override existing properties and add new ones:

The order of specifying spread operations determines what properties end up in the resulting object; properties in later spreads “win out” over previously created propert

*[Content truncated - see full docs]*

**Examples**:

```text
interface Person {  name: string;  age: number;  location: string;}type K1 = keyof Person; // "name" | "age" | "location"type K2 = keyof Person[]; // "length" | "push" | "pop" | "concat" | ...type K3 = keyof { [x: string]: Person }; // string
```

```javascript
type P1 = Person["name"]; // stringtype P2 = Person["name" | "age"]; // string | numbertype P3 = string["charAt"]; // (pos: number) => stringtype P4 = string[]["push"]; // (...items: string[]) => numbertype P5 = string[][0]; // string
```

```javascript
function getProperty<T, K extends keyof T>(obj: T, key: K) {  return obj[key]; // Inferred type is T[K]}function setProperty<T, K extends keyof T>(obj: T, key: K, value: T[K]) {  obj[key] = value;}let x = { foo: 10, bar: "hello!" };let foo = getProperty(x, "foo"); // numberlet bar = getProperty(x, "bar"); // stringlet oops = getProperty(x, "wargarbl"); // Error! "wargarbl" is not "foo" | "bar"setProperty(x, "foo", "string"); // Error!, string expected number
```

---

## TypeScript 2.2

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-2.html

**Contents**:
- TypeScript 2.2
- Support for Mix-in classes
      - First some terminology
      - Putting all of the above rules together in an example
- object type
- Support for new.target
      - Example
- Better checking for null/undefined in operands of expressions

Was this page helpful?

TypeScript 2.2 adds support for the ECMAScript 2015 mixin class pattern (see MDN Mixin description and “Real” Mixins with JavaScript Classes for more details) as well as rules for combining mixin construct signatures with regular construct signatures in intersection types.

A mixin constructor type refers to a type that has a single construct signature with a single rest argument of type any[] and an object-like return type. For example, given an object-like type X, new (...args: any[]) => X is a mixin constructor type with an instance type X.

A mixin class is a class declaration or expression that extends an expression of a type parameter type. The following rules apply to mixin class declarations:

Given an expression Base of a parametric type T with a constraint X, a mixin class class C extends Base {...} is processed as if Base had type X and the resulting type is the intersection typeof C & T. In other words, a mixin class is represented as an intersection between the mixin class constructor type and the parametric base class constructor type.

When obtaining the construct signatures of an intersection type that contains mixin constructor types, the mixin construct signatures are discarded and their instance types are mixed into the return types of the other construct signatures in the intersection type. For example, the intersection type { new(...args: any[]) => A } & { new(s: string) => B } has a single construct signature new(s: string) => A & B.

Mixin classes can constrain the types of classes they can mix into by specifying a construct signature return type in the constraint for the type parameter. For example, the following WithLocation function implements a subclass factory that adds a getLocation method to any class that satisfies the Point interface (i.e. that has x and y properties of type number).

TypeScript did not have a type that represents the non-primitive type, i.e. any thing that is not number, string, boolean, symbo

*[Content truncated - see full docs]*

**Examples**:

```javascript
class Point {  constructor(public x: number, public y: number) {}}class Person {  constructor(public name: string) {}}type Constructor<T> = new (...args: any[]) => T;function Tagged<T extends Constructor<{}>>(Base: T) {  return class extends Base {    _tag: string;    constructor(...args: any[]) {      super(...args);      this._tag = "";    }  };}const TaggedPoint = Tagged(Point);let point = new TaggedPoint(10, 20);point._tag = "hello";class Customer extends Tagged(Person) {  accountBalance: nu
...
```

```javascript
interface Point {  x: number;  y: number;}const WithLocation = <T extends Constructor<Point>>(Base: T) =>  class extends Base {    getLocation(): [number, number] {      return [this.x, this.y];    }  };
```

```javascript
declare function create(o: object | null): void;create({ prop: 0 }); // OKcreate(null); // OKcreate(42); // Errorcreate("string"); // Errorcreate(false); // Errorcreate(undefined); // Error
```

---

## TypeScript 2.3

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-3.html

**Contents**:
- TypeScript 2.3
- Generators and Iteration for ES5/ES3
      - Iterators
      - Generators
      - New --downlevelIteration
- Async Iteration
      - Async iterators
      - Async Generators

Was this page helpful?

First some ES2016 terminology:

ES2015 introduced Iterator, which is an object that exposes three methods, next, return, and throw, as per the following interface:

This kind of iterator is useful for iterating over synchronously available values, such as the elements of an Array or the keys of a Map. An object that supports iteration is said to be “iterable” if it has a Symbol.iterator method that returns an Iterator object.

The Iterator protocol also defines the target of some of the ES2015 features like for..of and spread operator and the array rest in destructuring assignments.

ES2015 also introduced “Generators”, which are functions that can be used to yield partial computation results via the Iterator interface and the yield keyword. Generators can also internally delegate calls to another iterable through yield *. For example:

Previously generators were only supported if the target is ES6/ES2015 or later. Moreover, constructs that operate on the Iterator protocol, e.g. for..of were only supported if they operate on arrays for targets below ES6/ES2015.

TypeScript 2.3 adds full support for generators and the Iterator protocol for ES3 and ES5 targets with downlevelIteration flag.

With downlevelIteration, the compiler uses new type check and emit behavior that attempts to call a [Symbol.iterator]() method on the iterated object if it is found, and creates a synthetic array iterator over the object if it is not.

Please note that this requires a native Symbol.iterator or Symbol.iterator shim at runtime for any non-array values.

for..of statements, Array Destructuring, and Spread elements in Array, Call, and New expressions support Symbol.iterator in ES5/E3 if available when using downlevelIteration, but can be used on an Array even if it does not define Symbol.iterator at run time or design time.

TypeScript 2.3 adds support for the async iterators and generators as described by the current TC39 proposal.

The Async Iteration introduc

*[Content truncated - see full docs]*

**Examples**:

```text
interface Iterator<T> {  next(value?: any): IteratorResult<T>;  return?(value?: any): IteratorResult<T>;  throw?(e?: any): IteratorResult<T>;}
```

```javascript
function* f() {  yield 1;  yield* [2, 3];}
```

```text
interface AsyncIterator<T> {  next(value?: any): Promise<IteratorResult<T>>;  return?(value?: any): Promise<IteratorResult<T>>;  throw?(e?: any): Promise<IteratorResult<T>>;}
```

---

## TypeScript 2.4

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-4.html

**Contents**:
- TypeScript 2.4
- Dynamic Import Expressions
- String Enums
- Improved inference for generics
  - Return types as inference targets
  - Type parameter inference from contextual types
  - Stricter checking for generic functions
- Strict contravariance for callback parameters

Was this page helpful?

Dynamic import expressions are a new feature and part of ECMAScript that allows users to asynchronously request a module at any arbitrary point in your program.

This means that you can conditionally and lazily import other modules and libraries. For example, here’s an async function that only imports a utility library when it’s needed:

Many bundlers have support for automatically splitting output bundles based on these import expressions, so consider using this new feature with the esnext module target.

TypeScript 2.4 now allows enum members to contain string initializers.

The caveat is that string-initialized enums can’t be reverse-mapped to get the original enum member name. In other words, you can’t write Colors["RED"] to get the string "Red".

TypeScript 2.4 introduces a few wonderful changes around the way generics are inferred.

For one, TypeScript can now make inferences for the return type of a call. This can improve your experience and catch errors. Something that now works:

As an example of new errors you might spot as a result:

Prior to TypeScript 2.4, in the following example

y would have the type any. This meant the program would type-check, but you could technically do anything with y, such as the following:

That last example isn’t actually type-safe.

In TypeScript 2.4, the function on the right side implicitly gains type parameters, and y is inferred to have the type of that type-parameter.

If you use y in a way that the type parameter’s constraint doesn’t support, you’ll correctly get an error. In this case, the constraint of T was (implicitly) {}, so the last example will appropriately fail.

TypeScript now tries to unify type parameters when comparing two single-signature types. As a result, you’ll get stricter checks when relating two generic signatures, and may catch some bugs.

TypeScript has always compared parameters in a bivariant way. There are a number of reasons for this, but by-and-large this was not been

*[Content truncated - see full docs]*

**Examples**:

```javascript
async function getZipFile(name: string, files: File[]): Promise<File> {  const zipUtil = await import("./utils/create-zip-file");  const zipContents = await zipUtil.getContentAsBlob(files);  return new File(zipContents, name);}
```

```text
enum Colors {  Red = "RED",  Green = "GREEN",  Blue = "BLUE"}
```

```javascript
function arrayMap<T, U>(f: (x: T) => U): (a: T[]) => U[] {  return a => a.map(f);}const lengths: (a: string[]) => number[] = arrayMap(s => s.length);
```

---

## TypeScript 2.5

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-5.html

**Contents**:
- TypeScript 2.5
- Optional catch clause variables
- Type assertion/cast syntax in checkJs/@ts-check mode
- Deduplicated and redirected packages
- The --preserveSymlinks compiler flag
      - On this page
      - Is this page helpful?

Was this page helpful?

Thanks to work done by @tinganho, TypeScript 2.5 implements a new ECMAScript feature that allows users to omit the variable in catch clauses. For example, when using JSON.parse you may need to wrap calls to the function with a try/catch, but you may not end up using the SyntaxError that gets thrown when input is erroneous.

TypeScript 2.5 introduces the ability to assert the type of expressions when using plain JavaScript in your projects. The syntax is an /** @type {...} */ annotation comment followed by a parenthesized expression whose type needs to be re-evaluated. For example:

When importing using the Node module resolution strategy in TypeScript 2.5, the compiler will now check whether files originate from “identical” packages. If a file originates from a package with a package.json containing the same name and version fields as a previously encountered package, then TypeScript will redirect itself to the top-most package. This helps resolve problems where two packages might contain identical declarations of classes, but which contain private members that cause them to be structurally incompatible.

As a nice bonus, this can also reduce the memory and runtime footprint of the compiler and language service by avoiding loading .d.ts files from duplicate packages.

TypeScript 2.5 brings the preserveSymlinks flag, which parallels the behavior of the --preserve-symlinks flag in Node.js. This flag also exhibits the opposite behavior to Webpack’s resolve.symlinks option (i.e. setting TypeScript’s preserveSymlinks to true parallels setting Webpack’s resolve.symlinks to false, and vice-versa).

In this mode, references to modules and packages (e.g. imports and /// <reference type="..." /> directives) are all resolved relative to the location of the symbolic link file, rather than relative to the path that the symbolic link resolves to. For a more concrete example, we’ll defer to the documentation on the Node.js website.

The TypeScript docs are 

*[Content truncated - see full docs]*

**Examples**:

```javascript
let input = "...";try {  JSON.parse(input);} catch {  // ^ Notice that our `catch` clause doesn't declare a variable.  console.log("Invalid JSON given\n\n" + input);}
```

```text
var x = /** @type {SomeType} */ AnyParenthesizedExpression;
```

---

## TypeScript 2.6

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-6.html

**Contents**:
- TypeScript 2.6
- Strict function types
      - Example
      - Note
- Cache tagged template objects in modules
      - Example
- Localized diagnostics on the command line
      - Example

Was this page helpful?

TypeScript 2.6 introduces a new strict checking flag, strictFunctionTypes. The strictFunctionTypes switch is part of the strict family of switches, meaning that it defaults to on in strict mode. You can opt-out by setting --strictFunctionTypes false on your command line or in your tsconfig.json.

Under strictFunctionTypes function type parameter positions are checked contravariantly instead of bivariantly. For some background on what variance means for function types check out What are covariance and contravariance?.

The stricter checking applies to all function types, except those originating in method or constructor declarations. Methods are excluded specifically to ensure generic classes and interfaces (such as Array<T>) continue to mostly relate covariantly.

Consider the following example in which Animal is the supertype of Dog and Cat:

The first assignment is permitted in default type checking mode, but flagged as an error in strict function types mode. Intuitively, the default mode permits the assignment because it is possibly sound, whereas strict function types mode makes it an error because it isn’t provably sound. In either mode the third assignment is an error because it is never sound.

Another way to describe the example is that the type (x: T) => void is bivariant (i.e. covariant or contravariant) for T in default type checking mode, but contravariant for T in strict function types mode.

The first assignment is now an error. Effectively, T is contravariant in Comparer<T> because it is used only in function type parameter positions.

By the way, note that whereas some languages (e.g. C# and Scala) require variance annotations (out/in or +/-), variance emerges naturally from the actual use of a type parameter within a generic type due to TypeScript’s structural type system.

Under strictFunctionTypes the first assignment is still permitted if compare was declared as a method. Effectively, T is bivariant in Comparer<T> because 

*[Content truncated - see full docs]*

**Examples**:

```javascript
declare let f1: (x: Animal) => void;declare let f2: (x: Dog) => void;declare let f3: (x: Cat) => void;f1 = f2; // Error with --strictFunctionTypesf2 = f1; // Okf2 = f3; // Error
```

```javascript
interface Comparer<T> {  compare: (a: T, b: T) => number;}declare let animalComparer: Comparer<Animal>;declare let dogComparer: Comparer<Dog>;animalComparer = dogComparer; // ErrordogComparer = animalComparer; // Ok
```

```javascript
interface Comparer<T> {  compare(a: T, b: T): number;}declare let animalComparer: Comparer<Animal>;declare let dogComparer: Comparer<Dog>;animalComparer = dogComparer; // Ok because of bivariancedogComparer = animalComparer; // Ok
```

---

## TypeScript 2.7

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-7.html

**Contents**:
- TypeScript 2.7
- Constant-named properties
      - Example
      - Example
- unique symbol
      - Example
      - Example
- Strict Class Initialization

Was this page helpful?

TypeScript 2.7 adds support for declaring const-named properties on types including ECMAScript symbols.

This also applies to numeric and string literals.

To enable treating symbols as unique literals a new type unique symbol is available. unique symbol is a subtype of symbol, and are produced only from calling Symbol() or Symbol.for(), or from explicit type annotations. The new type is only allowed on const declarations and readonly static properties, and in order to reference a specific unique symbol, you’ll have to use the typeof operator. Each reference to a unique symbol implies a completely unique identity that’s tied to a given declaration.

Because each unique symbol has a completely separate identity, no two unique symbol types are assignable or comparable to each other.

TypeScript 2.7 introduces a new flag called strictPropertyInitialization. This flag performs checks to ensure that each instance property of a class gets initialized in the constructor body, or by a property initializer. For example

In the above, if we truly meant for baz to potentially be undefined, we should have declared it with the type boolean | undefined.

There are certain scenarios where properties can be initialized indirectly (perhaps by a helper method or dependency injection library), in which case you can use the new definite assignment assertion modifiers for your properties (discussed below).

Keep in mind that strictPropertyInitialization will be turned on along with other strict mode flags, which can impact your project. You can set the strictPropertyInitialization setting to false in your tsconfig.json’s compilerOptions, or --strictPropertyInitialization false on the command line to turn off this checking.

The definite assignment assertion is a feature that allows a ! to be placed after instance property and variable declarations to relay to TypeScript that a variable is indeed assigned for all intents and purposes, even if TypeScript’s analyses

*[Content truncated - see full docs]*

**Examples**:

```javascript
// Libexport const SERIALIZE = Symbol("serialize-method-key");export interface Serializable {  [SERIALIZE](obj: {}): string;}
```

```python
// consumerimport { SERIALIZE, Serializable } from "lib";class JSONSerializableItem implements Serializable {  [SERIALIZE](obj: {}) {    return JSON.stringify(obj);  }}
```

```javascript
const Foo = "Foo";const Bar = "Bar";let x = {  [Foo]: 100,  [Bar]: "hello"};let a = x[Foo]; // has type 'number'let b = x[Bar]; // has type 'string'
```

---

## TypeScript 2.8

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-8.html

**Contents**:
- TypeScript 2.8
- Conditional Types
      - Example
- Distributive conditional types
      - Example
      - Example
      - Example
- Type inference in conditional types

Was this page helpful?

TypeScript 2.8 introduces conditional types which add the ability to express non-uniform type mappings. A conditional type selects one of two possible types based on a condition expressed as a type relationship test:

The type above means when T is assignable to U the type is X, otherwise the type is Y.

A conditional type T extends U ? X : Y is either resolved to X or Y, or deferred because the condition depends on one or more type variables. Whether to resolve or defer is determined as follows:

Conditional types in which the checked type is a naked type parameter are called distributive conditional types. Distributive conditional types are automatically distributed over union types during instantiation. For example, an instantiation of T extends U ? X : Y with the type argument A | B | C for T is resolved as (A extends U ? X : Y) | (B extends U ? X : Y) | (C extends U ? X : Y).

In instantiations of a distributive conditional type T extends U ? X : Y, references to T within the conditional type are resolved to individual constituents of the union type (i.e. T refers to the individual constituents after the conditional type is distributed over the union type). Furthermore, references to T within X have an additional type parameter constraint U (i.e. T is considered assignable to U within X).

Notice that T has the additional constraint any[] within the true branch of Boxed<T> and it is therefore possible to refer to the element type of the array as T[number]. Also, notice how the conditional type is distributed over the union type in the last example.

The distributive property of conditional types can conveniently be used to filter union types:

Conditional types are particularly useful when combined with mapped types:

Similar to union and intersection types, conditional types are not permitted to reference themselves recursively. For example the following is an error.

Within the extends clause of a conditional type, it is now possible t

*[Content truncated - see full docs]*

**Examples**:

```text
T extends U ? X : Y
```

```javascript
type TypeName<T> = T extends string  ? "string"  : T extends number  ? "number"  : T extends boolean  ? "boolean"  : T extends undefined  ? "undefined"  : T extends Function  ? "function"  : "object";type T0 = TypeName<string>; // "string"type T1 = TypeName<"a">; // "string"type T2 = TypeName<true>; // "boolean"type T3 = TypeName<() => void>; // "function"type T4 = TypeName<string[]>; // "object"
```

```javascript
type T10 = TypeName<string | (() => void)>; // "string" | "function"type T12 = TypeName<string | string[] | undefined>; // "string" | "object" | "undefined"type T11 = TypeName<string[] | number[]>; // "object"
```

---

## TypeScript 2.9

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-9.html

**Contents**:
- TypeScript 2.9
- Support number and symbol named properties with keyof and mapped types
      - Example
      - Example
    - Recommendations
- Generic type arguments in JSX elements
      - Example
- Generic type arguments in generic tagged templates

Was this page helpful?

TypeScript 2.9 adds support for number and symbol named properties in index types and mapped types. Previously, the keyof operator and mapped types only supported string named properties.

Given an object type X, keyof X is resolved as follows:

In a mapped type { [P in K]: XXX }, each string literal type in K introduces a property with a string name, each numeric literal type in K introduces a property with a numeric name, and each unique symbol type in K introduces a property with a unique symbol name. Furthermore, if K includes type string, a string index signature is introduced, and if K includes type number, a numeric index signature is introduced.

Since keyof now reflects the presence of a numeric index signature by including type number in the key type, mapped types such as Partial<T> and Readonly<T> work correctly when applied to object types with numeric index signatures:

Furthermore, with the keyof operator’s support for number and symbol named keys, it is now possible to abstract over access to properties of objects that are indexed by numeric literals (such as numeric enum types) and unique symbols.

This is a breaking change; previously, the keyof operator and mapped types only supported string named properties. Code that assumed values typed with keyof T were always strings, will now be flagged as error.

If your functions are only able to handle string named property keys, use Extract<keyof T, string> in the declaration:

If your functions are open to handling all property keys, then the changes should be done down-stream:

Otherwise use keyofStringsOnly compiler option to disable the new behavior.

JSX elements now allow passing type arguments to generic components.

Tagged templates are a form of invocation introduced in ECMAScript 2015. Like call expressions, generic functions may be used in a tagged template and TypeScript will infer the type arguments utilized.

TypeScript 2.9 allows passing generic type arguments to tag

*[Content truncated - see full docs]*

**Examples**:

```javascript
const c = "c";const d = 10;const e = Symbol();const enum E1 {  A,  B,  C,}const enum E2 {  A = "A",  B = "B",  C = "C",}type Foo = {  a: string; // String-like name  5: string; // Number-like name  [c]: string; // String-like name  [d]: string; // Number-like name  [e]: string; // Symbol-like name  [E1.A]: string; // Number-like name  [E2.A]: string; // String-like name};type K1 = keyof Foo; // "a" | 5 | "c" | 10 | typeof e | E1.A | E2.Atype K2 = Extract<keyof Foo, string>; // "a" | "c" | E2.Aty
...
```

```javascript
type Arrayish<T> = {  length: number;  [x: number]: T;};type ReadonlyArrayish<T> = Readonly<Arrayish<T>>;declare const map: ReadonlyArrayish<string>;let n = map.length;let x = map[123]; // Previously of type any (or an error with --noImplicitAny)
```

```javascript
const enum Enum {  A,  B,  C,}const enumToStringMap = {  [Enum.A]: "Name A",  [Enum.B]: "Name B",  [Enum.C]: "Name C",};const sym1 = Symbol();const sym2 = Symbol();const sym3 = Symbol();const symbolToNumberMap = {  [sym1]: 1,  [sym2]: 2,  [sym3]: 3,};type KE = keyof typeof enumToStringMap; // Enum (i.e. Enum.A | Enum.B | Enum.C)type KS = keyof typeof symbolToNumberMap; // typeof sym1 | typeof sym2 | typeof sym3function getValue<T, K extends keyof T>(obj: T, key: K): T[K] {  return obj[key];}let 
...
```

---

## TypeScript 3.0

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-0.html

**Contents**:
- TypeScript 3.0
- Project References
- Tuples in rest parameters and spread expressions
- Rest parameters with tuple types
- Spread expressions with tuple types
- Generic rest parameters
      - Example
- Optional elements in tuple types

Was this page helpful?

TypeScript 3.0 introduces a new concept of project references. Project references allow TypeScript projects to depend on other TypeScript projects - specifically, allowing tsconfig.json files to reference other tsconfig.json files. Specifying these dependencies makes it easier to split your code into smaller projects, since it gives TypeScript (and tools around it) a way to understand build ordering and output structure.

TypeScript 3.0 also introduces a new mode for tsc, the --build flag, that works hand-in-hand with project references to enable faster TypeScript builds.

See Project References handbook page for more documentation.

TypeScript 3.0 adds support to multiple new capabilities to interact with function parameter lists as tuple types. TypeScript 3.0 adds support for:

With these features it becomes possible to strongly type a number of higher-order functions that transform functions and their parameter lists.

When a rest parameter has a tuple type, the tuple type is expanded into a sequence of discrete parameters. For example the following two declarations are equivalent:

When a function call includes a spread expression of a tuple type as the last argument, the spread expression corresponds to a sequence of discrete arguments of the tuple element types.

Thus, the following calls are equivalent:

A rest parameter is permitted to have a generic type that is constrained to an array type, and type inference can infer tuple types for such generic rest parameters. This enables higher-order capturing and spreading of partial parameter lists:

In the declaration of f2 above, type inference infers types number, [string, boolean] and void for T, U and V respectively.

Note that when a tuple type is inferred from a sequence of parameters and later expanded into a parameter list, as is the case for U, the original parameter names are used in the expansion (however, the names have no semantic meaning and are not otherwise observable).

Tup

*[Content truncated - see full docs]*

**Examples**:

```javascript
declare function foo(...args: [number, string, boolean]): void;
```

```javascript
declare function foo(args_0: number, args_1: string, args_2: boolean): void;
```

```javascript
const args: [number, string, boolean] = [42, "hello", true];foo(42, "hello", true);foo(args[0], args[1], args[2]);foo(...args);
```

---

## TypeScript 3.1

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-1.html

**Contents**:
- TypeScript 3.1
- Mapped types on tuples and arrays
- Properties declarations on functions
- Version selection with typesVersions
      - On this page
      - Is this page helpful?

Was this page helpful?

In TypeScript 3.1, mapped object types[1] over tuples and arrays now produce new tuples/arrays, rather than creating a new type where members like push(), pop(), and length are converted. For example:

MapToPromise takes a type T, and when that type is a tuple like Coordinate, only the numeric properties are converted. In [number, number], there are two numerically named properties: 0 and 1. When given a tuple like that, MapToPromise will create a new tuple where the 0 and 1 properties are Promises of the original type. So the resulting type PromiseCoordinate ends up with the type [Promise<number>, Promise<number>].

TypeScript 3.1 brings the ability to define properties on function declarations and const-declared functions, simply by assigning to properties on these functions in the same scope. This allows us to write canonical JavaScript code without resorting to namespace hacks. For example:

Here, we have a function readImage which reads an image in a non-blocking asynchronous way. In addition to readImage, we’ve provided a convenience function on readImage itself called readImage.sync.

While ECMAScript exports are often a better way of providing this functionality, this new support allows code written in this style to “just work” in TypeScript. Additionally, this approach for property declarations allows us to express common patterns like defaultProps and propTypes on React function components (formerly known as SFCs).

[1] More specifically, homomorphic mapped types like in the above form.

Feedback from our community, as well as our own experience, has shown us that leveraging the newest TypeScript features while also accommodating users on the older versions are difficult. TypeScript introduces a new feature called typesVersions to help accommodate these scenarios.

You can read about it in the Publishing section of the declaration files section

The TypeScript docs are an open source project. Help us improve these pages by sending a

*[Content truncated - see full docs]*

**Examples**:

```text
type MapToPromise<T> = { [K in keyof T]: Promise<T[K]> };type Coordinate = [number, number];type PromiseCoordinate = MapToPromise<Coordinate>; // [Promise<number>, Promise<number>]
```

```javascript
function readImage(path: string, callback: (err: any, image: Image) => void) {  // ...}readImage.sync = (path: string) => {  const contents = fs.readFileSync(path);  return decodeImageSync(contents);};
```

```javascript
export const FooComponent = ({ name }) => <div>Hello! I am {name}</div>;FooComponent.defaultProps = {  name: "(anonymous)",};
```

---

## TypeScript 3.2

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-2.html

**Contents**:
- TypeScript 3.2
- strictBindCallApply
- Caveats
- Generic spread expressions in object literals
- Generic object rest variables and parameters
- BigInt
- Caveats
- Non-unit types as union discriminants

Was this page helpful?

TypeScript 3.2 introduces a new strictBindCallApply compiler option (in the strict family of options) with which the bind, call, and apply methods on function objects are strongly typed and strictly checked.

This is achieved by introducing two new types, CallableFunction and NewableFunction, in lib.d.ts. These types contain specialized generic method declarations for bind, call, and apply for regular functions and constructor functions, respectively. The declarations use generic rest parameters (see #24897) to capture and reflect parameter lists in a strongly typed manner. In strictBindCallApply mode these declarations are used in place of the (very permissive) declarations provided by type Function.

Since the stricter checks may uncover previously unreported errors, this is a breaking change in strict mode.

Additionally, another caveat of this new functionality is that due to certain limitations, bind, call, and apply can’t yet fully model generic functions or functions that have overloads. When using these methods on a generic function, type parameters will be substituted with the empty object type ({}), and when used on a function with overloads, only the last overload will ever be modeled.

In TypeScript 3.2, object literals now allow generic spread expressions which now produce intersection types, similar to the Object.assign function and JSX literals. For example:

Property assignments and non-generic spread expressions are merged to the greatest extent possible on either side of a generic spread expression. For example:

Non-generic spread expressions continue to be processed as before: Call and construct signatures are stripped, only non-method properties are preserved, and for properties with the same name, the type of the rightmost property is used. This contrasts with intersection types which concatenate call and construct signatures, preserve all properties, and intersect the types of properties with the same name. Thus, spread

*[Content truncated - see full docs]*

**Examples**:

```javascript
function foo(a: number, b: string): string {  return a + b;}let a = foo.apply(undefined, [10]); // error: too few argumentslet b = foo.apply(undefined, [10, 20]); // error: 2nd argument is a numberlet c = foo.apply(undefined, [10, "hello", 30]); // error: too many argumentslet d = foo.apply(undefined, [10, "hello"]); // okay! returns a string
```

```javascript
function taggedObject<T, U extends string>(obj: T, tag: U) {  return { ...obj, tag }; // T & { tag: U }}let x = taggedObject({ x: 10, y: 20 }, "point"); // { x: number, y: number } & { tag: "point" }
```

```javascript
function foo1<T>(t: T, obj1: { a: string }, obj2: { b: string }) {  return { ...obj1, x: 1, ...t, ...obj2, y: 2 }; // { a: string, x: number } & T & { b: string, y: number }}
```

---

## TypeScript 3.3

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-3.html

**Contents**:
- TypeScript 3.3
- Improved behavior for calling union types
- Caveats
- Incremental file watching for composite projects in --build --watch
      - On this page
      - Is this page helpful?

Was this page helpful?

In prior versions of TypeScript, unions of callable types could only be invoked if they had identical parameter lists.

However, in the above example, both FruitEaters and ColorConsumers should be able to take the string "orange", and return either a number or a string.

In TypeScript 3.3, this is no longer an error.

In TypeScript 3.3, the parameters of these signatures are intersected together to create a new signature.

In the example above, the parameters fruit and color are intersected together to a new parameter of type Fruit & Color. Fruit & Color is really the same as ("apple" | "orange") & ("red" | "orange") which is equivalent to ("apple" & "red") | ("apple" & "orange") | ("orange" & "red") | ("orange" & "orange"). Each of those impossible intersections reduces to never, and we’re left with "orange" & "orange" which is just "orange".

This new behavior only kicks in when at most one type in the union has multiple overloads, and at most one type in the union has a generic signature. That means methods on number[] | string[] like map (which is generic) still won’t be callable.

On the other hand, methods like forEach will now be callable, but under noImplicitAny there may be some issues.

This is still strictly more capable in TypeScript 3.3, and adding an explicit type annotation will work.

TypeScript 3.0 introduced a new feature for structuring builds called “composite projects”. Part of the goal here was to ensure users could break up large projects into smaller parts that build quickly and preserve project structure, without compromising the existing TypeScript experience. Thanks to composite projects, TypeScript can use --build mode to recompile only the set of projects and dependencies. You can think of this as optimizing inter-project builds.

TypeScript 2.7 also introduced --watch mode builds via a new incremental “builder” API. In a similar vein, the entire idea is that this mode only re-checks and re-emits changed files or 

*[Content truncated - see full docs]*

**Examples**:

```javascript
type Fruit = "apple" | "orange";type Color = "red" | "orange";type FruitEater = (fruit: Fruit) => number; // eats and ranks the fruittype ColorConsumer = (color: Color) => string; // consumes and describes the colorsdeclare let f: FruitEater | ColorConsumer;// Cannot invoke an expression whose type lacks a call signature.//   Type 'FruitEater | ColorConsumer' has no compatible call signatures.ts(2349)f("orange");
```

```javascript
type Fruit = "apple" | "orange";type Color = "red" | "orange";type FruitEater = (fruit: Fruit) => number; // eats and ranks the fruittype ColorConsumer = (color: Color) => string; // consumes and describes the colorsdeclare let f: FruitEater | ColorConsumer;f("orange"); // It works! Returns a 'number | string'.f("apple"); // error - Argument of type '"apple"' is not assignable to parameter of type '"orange"'.f("red"); // error - Argument of type '"red"' is not assignable to parameter of type '"o
...
```

```javascript
interface Dog {  kind: "dog";  dogProp: any;}interface Cat {  kind: "cat";  catProp: any;}const catOrDogArray: Dog[] | Cat[] = [];catOrDogArray.forEach(animal => {  //                ~~~~~~ error!  // Parameter 'animal' implicitly has an 'any' type.});
```

---

## TypeScript 3.4

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-4.html

**Contents**:
- TypeScript 3.4
- Faster subsequent builds with the --incremental flag
  - Composite projects
  - outFile
- Higher order type inference from generic functions
- Improvements for ReadonlyArray and readonly tuples
  - A new syntax for ReadonlyArray
  - readonly tuples

Was this page helpful?

TypeScript 3.4 introduces a new flag called incremental which tells TypeScript to save information about the project graph from the last compilation. The next time TypeScript is invoked with incremental, it will use that information to detect the least costly way to type-check and emit changes to your project.

By default with these settings, when we run tsc, TypeScript will look for a file called .tsbuildinfo in the output directory (./lib). If ./lib/.tsbuildinfo doesn’t exist, it’ll be generated. But if it does, tsc will try to use that file to incrementally type-check and update our output files.

These .tsbuildinfo files can be safely deleted and don’t have any impact on our code at runtime - they’re purely used to make compilations faster. We can also name them anything that we want, and place them anywhere we want using the tsBuildInfoFile option.

Part of the intent with composite projects (tsconfig.jsons with composite set to true) is that references between different projects can be built incrementally. As such, composite projects will always produce .tsbuildinfo files.

When outFile is used, the build information file’s name will be based on the output file’s name. As an example, if our output JavaScript file is ./output/foo.js, then under the incremental flag, TypeScript will generate the file ./output/foo.tsbuildinfo. As above, this can be controlled with the tsBuildInfoFile option.

TypeScript 3.4 can now produce generic function types when inference from other generic functions produces free type variables for inferences. This means many function composition patterns now work better in 3.4.

To get more specific, let’s build up some motivation and consider the following compose function:

compose takes two other functions:

compose then returns a function which feeds its argument through f and then g.

When calling this function, TypeScript will try to figure out the types of A, B, and C through a process called type argument in

*[Content truncated - see full docs]*

**Examples**:

```text
// tsconfig.json{  "compilerOptions": {    "incremental": true,    "outDir": "./lib"  },  "include": ["./src"]}
```

```text
// front-end.tsconfig.json{  "compilerOptions": {    "incremental": true,    "tsBuildInfoFile": "./buildcache/front-end",    "outDir": "./lib"  },  "include": ["./src"]}
```

```javascript
function compose<A, B, C>(f: (arg: A) => B, g: (arg: B) => C): (arg: A) => C {  return (x) => g(f(x));}
```

---

## TypeScript 3.5

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-5.html

**Contents**:
- TypeScript 3.5
- Speed improvements
  - Type-checking speed-ups
  - --incremental improvements
- The Omit helper type
  - Improved excess property checks in union types
- The --allowUmdGlobalAccess flag
- Smarter union type checking

Was this page helpful?

TypeScript 3.5 introduces several optimizations around type-checking and incremental builds.

TypeScript 3.5 contains certain optimizations over TypeScript 3.4 for type-checking more efficiently. These improvements are significantly more pronounced in editor scenarios where type-checking drives operations like code completion lists.

TypeScript 3.5 improves on 3.4’s incremental build mode, by saving information about how the state of the world was calculated - compiler settings, why files were looked up, where files were found, etc. In scenarios involving hundreds of projects using TypeScript’s project references in --build mode, we’ve found that the amount of time rebuilding can be reduced by as much as 68% compared to TypeScript 3.4!

For more details, you can see the pull requests to

TypeScript 3.5 introduces the new Omit helper type, which creates a new type with some properties dropped from the original.

Here we were able to copy over all the properties of Person except for location using the Omit helper.

For more details, see the pull request on GitHub to add Omit, as well as the change to use Omit for object rest.

In TypeScript 3.4 and earlier, certain excess properties were allowed in situations where they really shouldn’t have been. For instance, TypeScript 3.4 permitted the incorrect name property in the object literal even though its types don’t match between Point and Label.

Previously, a non-discriminated union wouldn’t have any excess property checking done on its members, and as a result, the incorrectly typed name property slipped by.

In TypeScript 3.5, the type-checker at least verifies that all the provided properties belong to some union member and have the appropriate type, meaning that the sample above correctly issues an error.

Note that partial overlap is still permitted as long as the property types are valid.

In TypeScript 3.5, you can now reference UMD global declarations like

from anywhere - even modules - 

*[Content truncated - see full docs]*

**Examples**:

```text
type Person = {  name: string;  age: number;  location: string;};type QuantumPerson = Omit<Person, "location">;// equivalent totype QuantumPerson = {  name: string;  age: number;};
```

```javascript
type Point = {  x: number;  y: number;};type Label = {  name: string;};const thing: Point | Label = {  x: 0,  y: 0,  name: true // uh-oh!};
```

```javascript
const pl: Point | Label = {  x: 0,  y: 0,  name: "origin" // okay};
```

---

## TypeScript 3.6

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-6.html

**Contents**:
- TypeScript 3.6
- Stricter Generators
- More Accurate Array Spread
- Improved UX Around Promises
- Better Unicode Support for Identifiers
- import.meta Support in SystemJS
- get and set Accessors Are Allowed in Ambient Contexts
- Ambient Classes and Functions Can Merge

Was this page helpful?

TypeScript 3.6 introduces stricter checking for iterators and generator functions. In earlier versions, users of generators had no way to differentiate whether a value was yielded or returned from a generator.

Additionally, generators just assumed the type of yield was always any.

In TypeScript 3.6, the checker now knows that the correct type for curr.value should be string in our first example, and will correctly error on our call to next() in our last example. This is thanks to some changes in the Iterator and IteratorResult type declarations to include a few new type parameters, and to a new type that TypeScript uses to represent generators called the Generator type.

The Iterator type now allows users to specify the yielded type, the returned type, and the type that next can accept.

Building on that work, the new Generator type is an Iterator that always has both the return and throw methods present, and is also iterable.

To allow differentiation between returned values and yielded values, TypeScript 3.6 converts the IteratorResult type to a discriminated union type:

In short, what this means is that you’ll be able to appropriately narrow down values from iterators when dealing with them directly.

To correctly represent the types that can be passed in to a generator from calls to next(), TypeScript 3.6 also infers certain uses of yield within the body of a generator function.

If you’d prefer to be explicit, you can also enforce the type of values that can be returned, yielded, and evaluated from yield expressions using an explicit return type. Below, next() can only be called with booleans, and depending on the value of done, value is either a string or a number.

For more details on the change, see the pull request here.

In pre-ES2015 targets, the most faithful emit for constructs like for/of loops and array spreads can be a bit heavy. For this reason, TypeScript uses a simpler emit by default that only supports array types, and 

*[Content truncated - see full docs]*

**Examples**:

```javascript
function* foo() {  if (Math.random() < 0.5) yield 100;  return "Finished!";}let iter = foo();let curr = iter.next();if (curr.done) {  // TypeScript 3.5 and prior thought this was a 'string | number'.  // It should know it's 'string' since 'done' was 'true'!  curr.value;}
```

```javascript
function* bar() {  let x: { hello(): void } = yield;  x.hello();}let iter = bar();iter.next();iter.next(123); // oops! runtime error!
```

```text
interface Iterator<T, TReturn = any, TNext = undefined> {  // Takes either 0 or 1 arguments - doesn't accept 'undefined'  next(...args: [] | [TNext]): IteratorResult<T, TReturn>;  return?(value?: TReturn): IteratorResult<T, TReturn>;  throw?(e?: any): IteratorResult<T, TReturn>;}
```

---

## TypeScript 3.7

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-7.html

**Contents**:
- TypeScript 3.7
- Optional Chaining
- Nullish Coalescing
- Assertion Functions
- Better Support for never-Returning Functions
- (More) Recursive Type Aliases
- --declaration and --allowJs
- The useDefineForClassFields Flag and The declare Property Modifier

Was this page helpful?

Optional chaining is issue #16 on our issue tracker. For context, there have been over 23,000 issues on the TypeScript issue tracker since then.

At its core, optional chaining lets us write code where TypeScript can immediately stop running some expressions if we run into a null or undefined. The star of the show in optional chaining is the new ?. operator for optional property accesses. When we write code like

this is a way of saying that when foo is defined, foo.bar.baz() will be computed; but when foo is null or undefined, stop what we’re doing and just return undefined.”

More plainly, that code snippet is the same as writing the following.

Note that if bar is null or undefined, our code will still hit an error accessing baz. Likewise, if baz is null or undefined, we’ll hit an error at the call site. ?. only checks for whether the value on the left of it is null or undefined - not any of the subsequent properties.

You might find yourself using ?. to replace a lot of code that performs repetitive nullish checks using the && operator.

Keep in mind that ?. acts differently than those && operations since && will act specially on “falsy” values (e.g. the empty string, 0, NaN, and, well, false), but this is an intentional feature of the construct. It doesn’t short-circuit on valid data like 0 or empty strings.

Optional chaining also includes two other operations. First there’s the optional element access which acts similarly to optional property accesses, but allows us to access non-identifier properties (e.g. arbitrary strings, numbers, and symbols):

There’s also optional call, which allows us to conditionally call expressions if they’re not null or undefined.

The “short-circuiting” behavior that optional chains have is limited property accesses, calls, element accesses - it doesn’t expand any further out from these expressions. In other words,

doesn’t stop the division or someComputation() call from occurring. It’s equivalent to

Tha

*[Content truncated - see full docs]*

**Examples**:

```javascript
let x = foo?.bar.baz();
```

```javascript
let x = foo === null || foo === undefined ? undefined : foo.bar.baz();
```

```text
// Beforeif (foo && foo.bar && foo.bar.baz) {  // ...}// After-ishif (foo?.bar?.baz) {  // ...}
```

---

## TypeScript 3.8

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-8.html

**Contents**:
- TypeScript 3.8
- Type-Only Imports and Export
- ECMAScript Private Fields
  - Which should I use?
- export * as ns Syntax
- Top-Level await
- es2020 for target and module
- JSDoc Property Modifiers

Was this page helpful?

This feature is something most users may never have to think about; however, if you’ve hit issues under isolatedModules, TypeScript’s transpileModule API, or Babel, this feature might be relevant.

TypeScript 3.8 adds a new syntax for type-only imports and exports.

import type only imports declarations to be used for type annotations and declarations. It always gets fully erased, so there’s no remnant of it at runtime. Similarly, export type only provides an export that can be used for type contexts, and is also erased from TypeScript’s output.

It’s important to note that classes have a value at runtime and a type at design-time, and the use is context-sensitive. When using import type to import a class, you can’t do things like extend from it.

If you’ve used Flow before, the syntax is fairly similar. One difference is that we’ve added a few restrictions to avoid code that might appear ambiguous.

In conjunction with import type, TypeScript 3.8 also adds a new compiler flag to control what happens with imports that won’t be utilized at runtime: importsNotUsedAsValues. This flag takes 3 different values:

For more information about the feature, you can take a look at the pull request, and relevant changes around broadening where imports from an import type declaration can be used.

TypeScript 3.8 brings support for ECMAScript’s private fields, part of the stage-3 class fields proposal.

Unlike regular properties (even ones declared with the private modifier), private fields have a few rules to keep in mind. Some of them are:

Apart from “hard” privacy, another benefit of private fields is that uniqueness we just mentioned. For example, regular property declarations are prone to being overwritten in subclasses.

With private fields, you’ll never have to worry about this, since each field name is unique to the containing class.

Another thing worth noting is that accessing a private field on any other type will result in a TypeError!

Finally

*[Content truncated - see full docs]*

**Examples**:

```python
import type { SomeThing } from "./some-module.js";export type { SomeThing };
```

```python
import type { Component } from "react";interface ButtonProps {  // ...}class Button extends Component<ButtonProps> {  //               ~~~~~~~~~  // error! 'Component' only refers to a type, but is being used as a value here.  // ...}
```

```python
// Is only 'Foo' a type? Or every declaration in the import?// We just give an error because it's not clear.import type Foo, { Bar, Baz } from "some-module";//     ~~~~~~~~~~~~~~~~~~~~~~// error! A type-only import can specify a default import or named bindings, but not both.
```

---

## TypeScript 3.9

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-9.html

**Contents**:
- TypeScript 3.9
- Improvements in Inference and Promise.all
  - What About the awaited Type?
- Speed Improvements
- // @ts-expect-error Comments
  - ts-ignore or ts-expect-error?
- Uncalled Function Checks in Conditional Expressions
- Editor Improvements

Was this page helpful?

Recent versions of TypeScript (around 3.7) have had updates to the declarations of functions like Promise.all and Promise.race. Unfortunately, that introduced a few regressions, especially when mixing in values with null or undefined.

This is strange behavior! The fact that sealExhibit contained an undefined somehow poisoned type of lion to include undefined.

Thanks to a pull request from Jack Bates, this has been fixed with improvements in our inference process in TypeScript 3.9. The above no longer errors. If you’ve been stuck on older versions of TypeScript due to issues around Promises, we encourage you to give 3.9 a shot!

If you’ve been following our issue tracker and design meeting notes, you might be aware of some work around a new type operator called awaited. This goal of this type operator is to accurately model the way that Promise unwrapping works in JavaScript.

We initially anticipated shipping awaited in TypeScript 3.9, but as we’ve run early TypeScript builds with existing codebases, we’ve realized that the feature needs more design work before we can roll it out to everyone smoothly. As a result, we’ve decided to pull the feature out of our main branch until we feel more confident. We’ll be experimenting more with the feature, but we won’t be shipping it as part of this release.

TypeScript 3.9 ships with many new speed improvements. Our team has been focusing on performance after observing extremely poor editing/compilation speed with packages like material-ui and styled-components. We’ve dived deep here, with a series of different pull requests that optimize certain pathological cases involving large unions, intersections, conditional types, and mapped types.

Each of these pull requests gains about a 5-10% reduction in compile times on certain codebases. In total, we believe we’ve achieved around a 40% reduction in material-ui’s compile time!

We also have some changes to file renaming functionality in editor scenarios.

*[Content truncated - see full docs]*

**Examples**:

```javascript
interface Lion {  roar(): void;}interface Seal {  singKissFromARose(): void;}async function visitZoo(  lionExhibit: Promise<Lion>,  sealExhibit: Promise<Seal | undefined>) {  let [lion, seal] = await Promise.all([lionExhibit, sealExhibit]);  lion.roar(); // uh oh  //  ~~~~  // Object is possibly 'undefined'.}
```

```javascript
function doStuff(abc: string, xyz: string) {  assert(typeof abc === "string");  assert(typeof xyz === "string");  // do some stuff}
```

```javascript
expect(() => {  doStuff(123, 456);}).toThrow();
```

---

## TypeScript 4.0

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-0.html

**Contents**:
- TypeScript 4.0
- Variadic Tuple Types
- Labeled Tuple Elements
- Class Property Inference from Constructors
- Short-Circuiting Assignment Operators
- unknown on catch Clause Bindings
- Custom JSX Factories
- Speed Improvements in build mode with --noEmitOnError

Was this page helpful?

Consider a function in JavaScript called concat that takes two array or tuple types and concatenates them together to make a new array.

Also consider tail, that takes an array or tuple, and returns all elements but the first.

How would we type either of these in TypeScript?

For concat, the only valid thing we could do in older versions of the language was to try and write some overloads.

Uh…okay, that’s…seven overloads for when the second array is always empty. Let’s add some for when arr2 has one argument.

We hope it’s clear that this is getting unreasonable. Unfortunately, you’d also end up with the same sorts of issues typing a function like tail.

This is another case of what we like to call “death by a thousand overloads”, and it doesn’t even solve the problem generally. It only gives correct types for as many overloads as we care to write. If we wanted to make a catch-all case, we’d need an overload like the following:

But that signature doesn’t encode anything about the lengths of the input, or the order of the elements, when using tuples.

TypeScript 4.0 brings two fundamental changes, along with inference improvements, to make typing these possible.

The first change is that spreads in tuple type syntax can now be generic. This means that we can represent higher-order operations on tuples and arrays even when we don’t know the actual types we’re operating over. When generic spreads are instantiated (or, replaced with a real type) in these tuple types, they can produce other sets of array and tuple types.

For example, that means we can type function like tail, without our “death by a thousand overloads” issue.

The second change is that rest elements can occur anywhere in a tuple - not just at the end!

Previously, TypeScript would issue an error like the following:

But with TypeScript 4.0, this restriction is relaxed.

Note that in cases when we spread in a type without a known length, the resulting type becomes unbounded as 

*[Content truncated - see full docs]*

**Examples**:

```javascript
function concat(arr1, arr2) {  return [...arr1, ...arr2];}
```

```javascript
function tail(arg) {  const [_, ...result] = arg;  return result;}
```

```javascript
function concat(arr1: [], arr2: []): [];function concat<A>(arr1: [A], arr2: []): [A];function concat<A, B>(arr1: [A, B], arr2: []): [A, B];function concat<A, B, C>(arr1: [A, B, C], arr2: []): [A, B, C];function concat<A, B, C, D>(arr1: [A, B, C, D], arr2: []): [A, B, C, D];function concat<A, B, C, D, E>(arr1: [A, B, C, D, E], arr2: []): [A, B, C, D, E];function concat<A, B, C, D, E, F>(arr1: [A, B, C, D, E, F], arr2: []): [A, B, C, D, E, F];
```

---

## TypeScript 4.1

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-1.html

**Contents**:
- TypeScript 4.1
- Template Literal Types
- Key Remapping in Mapped Types
- Recursive Conditional Types
- Checked Indexed Accesses (--noUncheckedIndexedAccess)
- paths without baseUrl
- checkJs Implies allowJs
- React 17 JSX Factories

Was this page helpful?

String literal types in TypeScript allow us to model functions and APIs that expect a set of specific strings.

This is pretty nice because string literal types can basically spell-check our string values.

We also like that string literals can be used as property names in mapped types. In this sense, they’re also usable as building blocks:

But there’s another place that string literal types could be used as building blocks: building other string literal types.

That’s why TypeScript 4.1 brings the template literal string type. It has the same syntax as template literal strings in JavaScript, but is used in type positions. When you use it with concrete literal types, it produces a new string literal type by concatenating the contents.

What happens when you have unions in substitution positions? It produces the set of every possible string literal that could be represented by each union member.

This can be used beyond cute examples in release notes. For example, several libraries for UI components have a way to specify both vertical and horizontal alignment in their APIs, often with both at once using a single string like "bottom-right". Between vertically aligning with "top", "middle", and "bottom", and horizontally aligning with "left", "center", and "right", there are 9 possible strings where each of the former strings is connected with each of the latter strings using a dash.

While there are lots of examples of this sort of API in the wild, this is still a bit of a toy example since we could write these out manually. In fact, for 9 strings, this is likely fine; but when you need a ton of strings, you should consider automatically generating them ahead of time to save work on every type-check (or just use string, which will be much simpler to comprehend).

Some of the real value comes from dynamically creating new string literals. For example, imagine a makeWatchedObject API that takes an object and produces a mostly identical object, b

*[Content truncated - see full docs]*

**Examples**:

```javascript
function setVerticalAlignment(location: "top" | "middle" | "bottom") {  // ...} setVerticalAlignment("middel");Argument of type '"middel"' is not assignable to parameter of type '"top" | "middle" | "bottom"'.2345Argument of type '"middel"' is not assignable to parameter of type '"top" | "middle" | "bottom"'.
```

```text
type Options = {  [K in "noImplicitAny" | "strictNullChecks" | "strictFunctionTypes"]?: boolean;};// same as//   type Options = {//       noImplicitAny?: boolean,//       strictNullChecks?: boolean,//       strictFunctionTypes?: boolean//   };
```

```text
type World = "world"; type Greeting = `hello ${World}`;        type Greeting = "hello world"
```

---

## TypeScript 4.2

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-2.html

**Contents**:
- TypeScript 4.2
- Smarter Type Alias Preservation
- Leading/Middle Rest Elements in Tuple Types
- Stricter Checks For The in Operator
- --noPropertyAccessFromIndexSignature
- abstract Construct Signatures
- Understanding Your Project Structure With --explainFiles
- Improved Uncalled Function Checks in Logical Expressions

Was this page helpful?

TypeScript has a way to declare new names for types called type aliases. If you’re writing a set of functions that all work on string | number | boolean, you can write a type alias to avoid repeating yourself over and over again.

TypeScript has always used a set of rules and guesses for when to reuse type aliases when printing out types. For example, take the following code snippet.

If we hover our mouse over x in an editor like Visual Studio, Visual Studio Code, or the TypeScript Playground, we’ll get a quick info panel that shows the type BasicPrimitive. Likewise, if we get the declaration file output (.d.ts output) for this file, TypeScript will say that doStuff returns BasicPrimitive.

However, what happens if we return a BasicPrimitive or undefined?

We can see what happens in the TypeScript 4.1 playground. While we might want TypeScript to display the return type of doStuff as BasicPrimitive | undefined, it instead displays string | number | boolean | undefined! What gives?

Well this has to do with how TypeScript represents types internally. When creating a union type out of one or more union types, it will always normalize those types into a new flattened union type - but doing that loses information. The type-checker would have to find every combination of types from string | number | boolean | undefined to see what type aliases could have been used, and even then, there might be multiple type aliases to string | number | boolean.

In TypeScript 4.2, our internals are a little smarter. We keep track of how types were constructed by keeping around parts of how they were originally written and constructed over time. We also keep track of, and differentiate, type aliases to instances of other aliases!

Being able to print back the types based on how you used them in your code means that as a TypeScript user, you can avoid some unfortunately humongous types getting displayed, and that often translates to getting better .d.ts file outpu

*[Content truncated - see full docs]*

**Examples**:

```text
type BasicPrimitive = number | string | boolean;
```

```javascript
export type BasicPrimitive = number | string | boolean;export function doStuff(value: BasicPrimitive) {  let x = value;  return x;}
```

```javascript
export type BasicPrimitive = number | string | boolean;export function doStuff(value: BasicPrimitive) {  if (Math.random() < 0.5) {    return undefined;  }  return value;}
```

---

## TypeScript 4.3

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-3.html

**Contents**:
- TypeScript 4.3
- Separate Write Types on Properties
- override and the --noImplicitOverride Flag
- Template String Type Improvements
- ECMAScript #private Class Elements
- ConstructorParameters Works on Abstract Classes
- Contextual Narrowing for Generics
- Always-Truthy Promise Checks

Was this page helpful?

In JavaScript, it’s pretty common for APIs to convert values that are passed in before storing them. This often happens with getters and setters too. For example, let’s imagine we’ve got a class with a setter that always converts a value into a number before saving it in a private field.

How would we type this JavaScript code in TypeScript? Well, technically we don’t have to do anything special here - TypeScript can look at this with no explicit types and can figure out that size is a number.

The problem is that size allows you to assign more than just numbers to it. We could get around this by saying that size has the type unknown or any like in this snippet:

But that’s no good - unknown forces people reading size to do a type assertion, and any won’t catch any mistakes. If we really want to model APIs that convert values, previous versions of TypeScript forced us to pick between being precise (which makes reading values easier, and writing harder) and being permissive (which makes writing values easier, and reading harder).

That’s why TypeScript 4.3 allows you to specify types for reading and writing to properties.

In the above example, our set accessor takes a broader set of types (strings, booleans, and numbers), but our get accessor always guarantees it will be a number. Now we can finally assign other types to these properties with no errors!

When considering how two properties with the same name relate to each other, TypeScript will only use the “reading” type (e.g. the type on the get accessor above). “Writing” types are only considered when directly writing to a property.

Keep in mind, this isn’t a pattern that’s limited to classes. You can write getters and setters with different types in object literals.

In fact, we’ve added syntax to interfaces/object types to support different reading/writing types on properties.

One limitation of using different types for reading and writing properties is that the type for reading a pro

*[Content truncated - see full docs]*

**Examples**:

```javascript
class Thing {  #size = 0;   get size() {    return this.#size;  }  set size(value) {    let num = Number(value);     // Don't allow NaN and stuff.    if (!Number.isFinite(num)) {      this.#size = 0;      return;    }     this.#size = num;  }}
```

```text
class Thing {  // ...  get size(): unknown {    return this.#size;  }}
```

```javascript
class Thing {  #size = 0;   get size(): number {    return this.#size;  }   set size(value: string | number | boolean) {    let num = Number(value);     // Don't allow NaN and stuff.    if (!Number.isFinite(num)) {      this.#size = 0;      return;    }     this.#size = num;  }}
```

---

## TypeScript 4.4

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-4.html

**Contents**:
- TypeScript 4.4
- Control Flow Analysis of Aliased Conditions and Discriminants
- Symbol and Template String Pattern Index Signatures
- Defaulting to the unknown Type in Catch Variables (--useUnknownInCatchVariables)
- Exact Optional Property Types (--exactOptionalPropertyTypes)
- static Blocks in Classes
- tsc --help Updates and Improvements
- Performance Improvements

Was this page helpful?

In JavaScript, we often have to probe a value in different ways, and do something different once we know more about its type. TypeScript understands these checks and calls them type guards. Instead of having to convince TypeScript of a variable’s type whenever we use it, the type-checker leverages something called control flow analysis to see if we’ve used a type guard before a given piece of code.

For example, we can write something like

In this example, we checked whether arg was a string. TypeScript recognized the typeof arg === "string" check, which it considered a type guard, and knew that arg was a string inside the body of the if block. That let us access string methods like toUpperCase() without getting an error.

However, what would happen if we moved the condition out to a constant called argIsString?

In previous versions of TypeScript, this would be an error - even though argIsString was assigned the value of a type guard, TypeScript simply lost that information. That’s unfortunate since we might want to re-use the same check in several places. To get around that, users often have to repeat themselves or use type assertions (a.k.a. casts).

In TypeScript 4.4, that is no longer the case. The above example works with no errors! When TypeScript sees that we are testing a constant value, it will do a little bit of extra work to see if it contains a type guard. If that type guard operates on a const, a readonly property, or an un-modified parameter, then TypeScript is able to narrow that value appropriately.

Different sorts of type guard conditions are preserved - not just typeof checks. For example, checks on discriminated unions work like a charm.

Analysis on discriminants in 4.4 also goes a little bit deeper - we can now extract out discriminants and TypeScript can narrow the original object.

As another example, here’s a function that checks whether two of its inputs have contents.

TypeScript can understand that both inputA an

*[Content truncated - see full docs]*

**Examples**:

```javascript
function foo(arg: unknown) {  if (typeof arg === "string") {    console.log(arg.toUpperCase());                (parameter) arg: string  }}
```

```javascript
// In TS 4.3 and belowfunction foo(arg: unknown) {  const argIsString = typeof arg === "string";  if (argIsString) {    console.log(arg.toUpperCase());    //              ~~~~~~~~~~~    // Error! Property 'toUpperCase' does not exist on type 'unknown'.  }}
```

```javascript
type Shape =  | { kind: "circle"; radius: number }  | { kind: "square"; sideLength: number }; function area(shape: Shape): number {  const isCircle = shape.kind === "circle";  if (isCircle) {    // We know we have a circle here!    return Math.PI * shape.radius ** 2;  } else {    // We know we're left with a square here!    return shape.sideLength ** 2;  }}
```

---

## TypeScript 4.5

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-5.html

**Contents**:
- TypeScript 4.5
- Supporting lib from node_modules
- The Awaited Type and Promise Improvements
- Template String Types as Discriminants
- module es2022
- Tail-Recursion Elimination on Conditional Types
- Disabling Import Elision
- type Modifiers on Import Names

Was this page helpful?

To ensure that TypeScript and JavaScript support works well out of the box, TypeScript bundles a series of declaration files (.d.ts files). These declaration files represent the available APIs in the JavaScript language, and the standard browser DOM APIs. While there are some reasonable defaults based on your target, you can pick and choose which declaration files your program uses by configuring the lib setting in the tsconfig.json.

There are two occasional downsides to including these declaration files with TypeScript though:

TypeScript 4.5 introduces a way to override a specific built-in lib in a manner similar to how @types/ support works. When deciding which lib files TypeScript should include, it will first look for a scoped @typescript/lib-* package in node_modules. For example, when including dom as an option in lib, TypeScript will use the types in node_modules/@typescript/lib-dom if available.

You can then use your package manager to install a specific package to take over for a given lib For example, today TypeScript publishes versions of the DOM APIs on @types/web. If you wanted to lock your project to a specific version of the DOM APIs, you could add this to your package.json:

Then from 4.5 onwards, you can update TypeScript and your dependency manager’s lockfile will ensure that it uses the exact same version of the DOM types. That means you get to update your types on your own terms.

We’d like to give a shout-out to saschanaz who has been extremely helpful and patient as we’ve been building out and experimenting with this feature.

For more information, you can see the implementation of this change.

TypeScript 4.5 introduces a new utility type called the Awaited type. This type is meant to model operations like await in async functions, or the .then() method on Promises - specifically, the way that they recursively unwrap Promises.

The Awaited type can be helpful for modeling existing APIs, including JavaScript built-ins

*[Content truncated - see full docs]*

**Examples**:

```text
{  "dependencies": {    "@typescript/lib-dom": "npm:@types/web"  }}
```

```text
// A = stringtype A = Awaited<Promise<string>>;// B = numbertype B = Awaited<Promise<Promise<number>>>;// C = boolean | numbertype C = Awaited<boolean | Promise<number>>;
```

```javascript
declare function MaybePromise<T>(value: T): T | Promise<T> | PromiseLike<T>;async function doSomething(): Promise<[number, number]> {  const result = await Promise.all([MaybePromise(100), MaybePromise(200)]);  // Error!  //  //    [number | Promise<100>, number | Promise<200>]  //  // is not assignable to type  //  //    [number, number]  return result;}
```

---

## TypeScript 4.6

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-6.html

**Contents**:
- TypeScript 4.6
- Allowing Code in Constructors Before super()
- Control Flow Analysis for Destructured Discriminated Unions
- Improved Recursion Depth Checks
- Indexed Access Inference Improvements
- Control Flow Analysis for Dependent Parameters
- --target es2022
- Removed Unnecessary Arguments in react-jsx

Was this page helpful?

In JavaScript classes it’s mandatory to call super() before referring to this. TypeScript enforces this as well, though it was a bit too strict in how it ensured this. In TypeScript, it was previously an error to contain any code at the beginning of a constructor if its containing class had any property initializers.

This made it cheap to check that super() gets called before this is referenced, but it ended up rejecting a lot of valid code. TypeScript 4.6 is now much more lenient in that check and permits other code to run before super()., all while still ensuring that super() occurs at the top-level before any references to this.

We’d like to extend our thanks to Joshua Goldberg for patiently working with us to land this change!

TypeScript is able to narrow types based on what’s called a discriminant property. For example, in the following code snippet, TypeScript is able to narrow the type of action based on every time we check against the value of kind.

This lets us work with objects that can hold different data, but a common field tells us which data those objects have.

This is very common in TypeScript; however, depending on your preferences, you might have wanted to destructure kind and payload in the example above. Perhaps something like the following:

Previously TypeScript would error on these - once kind and payload were extracted from the same object into variables, they were considered totally independent.

In TypeScript 4.6, this just works!

When destructuring individual properties into a const declaration, or when destructuring a parameter into variables that are never assigned to, TypeScript will check for if the destructured type is a discriminated union. If it is, TypeScript can now narrow the types of variables depending on checks of other variables So in our example, a check on kind narrows the type of payload.

For more information, see the pull request that implemented this analysis.

TypeScript has some interestin

*[Content truncated - see full docs]*

**Examples**:

```text
class Base {  // ...}class Derived extends Base {  someProperty = true;  constructor() {    // error!    // have to call 'super()' first because it needs to initialize 'someProperty'.    doSomeStuff();    super();  }}
```

```javascript
type Action =  | { kind: "NumberContents"; payload: number }  | { kind: "StringContents"; payload: string };function processAction(action: Action) {  if (action.kind === "NumberContents") {    // `action.payload` is a number here.    let num = action.payload * 2;    // ...  } else if (action.kind === "StringContents") {    // `action.payload` is a string here.    const str = action.payload.trim();    // ...  }}
```

```javascript
type Action =  | { kind: "NumberContents"; payload: number }  | { kind: "StringContents"; payload: string };function processAction(action: Action) {  const { kind, payload } = action;  if (kind === "NumberContents") {    let num = payload * 2;    // ...  } else if (kind === "StringContents") {    const str = payload.trim();    // ...  }}
```

---

## TypeScript 4.7

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-7.html

**Contents**:
- TypeScript 4.7
- ECMAScript Module Support in Node.js
  - type in package.json and New Extensions
  - New File Extensions
  - CommonJS Interoperability
  - package.json Exports, Imports, and Self-Referencing
  - Your Feedback Wanted!
- Control over Module Detection

Was this page helpful?

For the last few years, Node.js has been working to support ECMAScript modules (ESM). This has been a very difficult feature, since the Node.js ecosystem is built on a different module system called CommonJS (CJS). Interoperating between the two brings large challenges, with many new features to juggle; however, support for ESM in Node.js was largely implemented in Node.js 12 and later. Around TypeScript 4.5 we rolled out nightly-only support for ESM in Node.js to get some feedback from users and let library authors ready themselves for broader support.

TypeScript 4.7 adds this functionality with two new module settings: node16 and nodenext.

These new modes bring a few high-level features which we’ll explore here.

Node.js supports a new setting in package.json called type. "type" can be set to either "module" or "commonjs".

This setting controls whether .js and .d.ts files are interpreted as ES modules or CommonJS modules, and defaults to CommonJS when not set. When a file is considered an ES module, a few different rules come into play compared to CommonJS:

We’ll come back to some of these.

To overlay the way TypeScript works in this system, .ts and .tsx files now work the same way. When TypeScript finds a .ts, .tsx, .js, or .jsx file, it will walk up looking for a package.json to see whether that file is an ES module, and use that to determine:

When a .ts file is compiled as an ES module, ECMAScript import/export statements are left alone in the .js output; when it’s compiled as a CommonJS module, it will produce the same output you get today under --module commonjs.

This also means paths resolve differently between .ts files that are ES modules and ones that are CJS modules. For example, let’s say you have the following code today:

This code works in CommonJS modules, but will fail in ES modules because relative import paths need to use extensions. As a result, it will have to be rewritten to use the extension of the output of foo

*[Content truncated - see full docs]*

**Examples**:

```text
{    "compilerOptions": {        "module": "node16",    }}
```

```text
{    "name": "my-package",    "type": "module",    "//": "...",    "dependencies": {    }}
```

```python
// ./foo.tsexport function helper() {    // ...}// ./bar.tsimport { helper } from "./foo"; // only works in CJShelper();
```

---

## TypeScript 4.8

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-8.html

**Contents**:
- TypeScript 4.8
- Improved Intersection Reduction, Union Compatibility, and Narrowing
- Improved Inference for infer Types in Template String Types
- --build, --watch, and --incremental Performance Improvements
- Errors When Comparing Object and Array Literals
- Improved Inference from Binding Patterns
- File-Watching Fixes (Especially Across git checkouts)
- Find-All-References Performance Improvements

Was this page helpful?

TypeScript 4.8 brings a series of correctness and consistency improvements under --strictNullChecks. These changes affect how intersection and union types work, and are leveraged in how TypeScript narrows types.

For example, unknown is close in spirit to the union type {} | null | undefined because it accepts null, undefined, and any other type. TypeScript now recognizes this, and allows assignments from unknown to {} | null | undefined.

Another change is that {} intersected with any other object type simplifies right down to that object type. That meant that we were able to rewrite NonNullable to just use an intersection with {}, because {} & null and {} & undefined just get tossed away.

This is an improvement because intersection types like this can be reduced and assigned to, while conditional types currently cannot. So NonNullable<NonNullable<T>> now simplifies at least to NonNullable<T>, whereas it didn’t before.

These changes also allowed us to bring in sensible improvements in control flow analysis and type narrowing. For example, unknown is now narrowed just like {} | null | undefined in truthy branches.

Generic values also get narrowed similarly. When checking that a value isn’t null or undefined, TypeScript now just intersects it with {} - which again, is the same as saying it’s NonNullable. Putting many of the changes here together, we can now define the following function without any type assertions.

value now gets narrowed to T & {}, and is now identical with NonNullable<T> - so the body of the function just works with no TypeScript-specific syntax.

On their own, these changes may appear small - but they represent fixes for many many paper cuts that have been reported over several years.

For more specifics on these improvements, you can read more here.

TypeScript recently introduced a way to add extends constraints to infer type variables in conditional types.

If these infer types appear in a template string type and ar

*[Content truncated - see full docs]*

**Examples**:

```javascript
function f(x: unknown, y: {} | null | undefined) {    x = y; // always worked    y = x; // used to error, now works}
```

```text
- type NonNullable<T> = T extends null | undefined ? never : T;+ type NonNullable<T> = T & {};
```

```javascript
function foo<T>(x: NonNullable<T>, y: NonNullable<NonNullable<T>>) {    x = y; // always worked    y = x; // used to error, now works}
```

---

## TypeScript 4.9

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-9.html

**Contents**:
- TypeScript 4.9
- The satisfies Operator
- Unlisted Property Narrowing with the in Operator
- Auto-Accessors in Classes
- Checks For Equality on NaN
- File-Watching Now Uses File System Events
- “Remove Unused Imports” and “Sort Imports” Commands for Editors
- Go-to-Definition on return Keywords

Was this page helpful?

TypeScript developers are often faced with a dilemma: we want to ensure that some expression matches some type, but also want to keep the most specific type of that expression for inference purposes.

Notice that we’ve written bleu, whereas we probably should have written blue. We could try to catch that bleu typo by using a type annotation on palette, but we’d lose the information about each property.

The new satisfies operator lets us validate that the type of an expression matches some type, without changing the resulting type of that expression. As an example, we could use satisfies to validate that all the properties of palette are compatible with string | number[]:

satisfies can be used to catch lots of possible errors. For example, we could ensure that an object has all the keys of some type, but no more:

Maybe we don’t care about if the property names match up somehow, but we do care about the types of each property. In that case, we can also ensure that all of an object’s property values conform to some type.

For more examples, you can see the issue proposing this and the implementing pull request. We’d like to thank Oleksandr Tarasiuk who implemented and iterated on this feature with us.

As developers, we often need to deal with values that aren’t fully known at runtime. In fact, we often don’t know if properties exist, whether we’re getting a response from a server or reading a configuration file. JavaScript’s in operator can check whether a property exists on an object.

Previously, TypeScript allowed us to narrow away any types that don’t explicitly list a property.

Here, the type RGB didn’t list the hue and got narrowed away, and leaving us with the type HSV.

But what about examples where no type listed a given property? In those cases, the language didn’t help us much. Let’s take the following example in JavaScript:

Rewriting this to canonical TypeScript would just be a matter of defining and using a type for context; h

*[Content truncated - see full docs]*

**Examples**:

```javascript
// Each property can be a string or an RGB tuple.const palette = {    red: [255, 0, 0],    green: "#00ff00",    bleu: [0, 0, 255]//  ^^^^ sacrebleu - we've made a typo!};// We want to be able to use string methods on 'green'...const greenNormalized = palette.green.toUpperCase();
```

```javascript
type Colors = "red" | "green" | "blue";type RGB = [red: number, green: number, blue: number];const palette: Record<Colors, string | RGB> = {    red: [255, 0, 0],    green: "#00ff00",    bleu: [0, 0, 255]//  ~~~~ The typo is now correctly detected};// But we now have an undesirable error here - 'palette.green' "could" be of type RGB and// property 'toUpperCase' does not exist on type 'string | RGB'.const greenNormalized = palette.green.toUpperCase();
```

```javascript
type Colors = "red" | "green" | "blue";type RGB = [red: number, green: number, blue: number];const palette = {    red: [255, 0, 0],    green: "#00ff00",    bleu: [0, 0, 255]//  ~~~~ The typo is now caught!} satisfies Record<Colors, string | RGB>;// toUpperCase() method is still accessible!const greenNormalized = palette.green.toUpperCase();
```

---

## TypeScript 5.0

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-0.html

**Contents**:
- TypeScript 5.0
- Decorators
  - Differences with Experimental Legacy Decorators
  - Writing Well-Typed Decorators
- const Type Parameters
- Supporting Multiple Configuration Files in extends
- All enums Are Union enums
- --moduleResolution bundler

Was this page helpful?

Decorators are an upcoming ECMAScript feature that allow us to customize classes and their members in a reusable way.

Let’s consider the following code:

greet is pretty simple here, but let’s imagine it’s something way more complicated - maybe it does some async logic, it’s recursive, it has side effects, etc. Regardless of what kind of ball-of-mud you’re imagining, let’s say you throw in some console.log calls to help debug greet.

This pattern is fairly common. It sure would be nice if there was a way we could do this for every method!

This is where decorators come in. We can write a function called loggedMethod that looks like the following:

“What’s the deal with all of these anys? What is this, anyScript!?”

Just be patient - we’re keeping things simple for now so that we can focus on what this function is doing. Notice that loggedMethod takes the original method (originalMethod) and returns a function that

Now we can use loggedMethod to decorate the method greet:

We just used loggedMethod as a decorator above greet - and notice that we wrote it as @loggedMethod. When we did that, it got called with the method target and a context object. Because loggedMethod returned a new function, that function replaced the original definition of greet.

We didn’t mention it yet, but loggedMethod was defined with a second parameter. It’s called a “context object”, and it has some useful information about how the decorated method was declared - like whether it was a #private member, or static, or what the name of the method was. Let’s rewrite loggedMethod to take advantage of that and print out the name of the method that was decorated.

We’re now using the context parameter - and that it’s the first thing in loggedMethod that has a type stricter than any and any[]. TypeScript provides a type called ClassMethodDecoratorContext that models the context object that method decorators take.

Apart from metadata, the context object for methods also has 

*[Content truncated - see full docs]*

**Examples**:

```javascript
class Person {    name: string;    constructor(name: string) {        this.name = name;    }    greet() {        console.log(`Hello, my name is ${this.name}.`);    }}const p = new Person("Ray");p.greet();
```

```text
class Person {    name: string;    constructor(name: string) {        this.name = name;    }    greet() {        console.log("LOG: Entering method.");        console.log(`Hello, my name is ${this.name}.`);        console.log("LOG: Exiting method.")    }}
```

```javascript
function loggedMethod(originalMethod: any, _context: any) {    function replacementMethod(this: any, ...args: any[]) {        console.log("LOG: Entering method.")        const result = originalMethod.call(this, ...args);        console.log("LOG: Exiting method.")        return result;    }    return replacementMethod;}
```

---

## TypeScript 5.1

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-1.html

**Contents**:
- TypeScript 5.1
- Easier Implicit Returns for undefined-Returning Functions
- Unrelated Types for Getters and Setters
- Decoupled Type-Checking Between JSX Elements and JSX Tag Types
- Namespaced JSX Attributes
- typeRoots Are Consulted In Module Resolution
- Move Declarations to Existing Files
- Linked Cursors for JSX Tags

Was this page helpful?

In JavaScript, if a function finishes running without hitting a return, it returns the value undefined.

However, in previous versions of TypeScript, the only functions that could have absolutely no return statements were void- and any-returning functions. That meant that even if you explicitly said “this function returns undefined” you were forced to have at least one return statement.

This could be a pain if some API expected a function returning undefined - you would need to have either at least one explicit return of undefined or a return statement and an explicit annotation.

This behavior was frustrating and confusing, especially when calling functions outside of one’s control. Understanding the interplay between inferring void over undefined, whether an undefined-returning function needs a return statement, etc. seems like a distraction.

First, TypeScript 5.1 now allows undefined-returning functions to have no return statement.

Second, if a function has no return expressions and is being passed to something expecting a function that returns undefined, TypeScript infers undefined for that function’s return type.

To address another similar pain-point, under TypeScript’s --noImplicitReturns option, functions returning only undefined now have a similar exception to void, in that not every single code path must end in an explicit return.

For more information, you can read up on the original issue and the implementing pull request.

TypeScript 4.3 made it possible to say that a get and set accessor pair might specify two different types.

Initially we required that the get type had to be a subtype of the set type. This meant that writing

would always be valid.

However, there are plenty of existing and proposed APIs that have completely unrelated types between their getters and setters. For example, consider one of the most common examples - the style property in the DOM and CSSStyleRule API. Every style rule has a style property that 

*[Content truncated - see full docs]*

**Examples**:

```javascript
function foo() {    // no return}// x = undefinedlet x = foo();
```

```javascript
// ✅ fine - we inferred that 'f1' returns 'void'function f1() {    // no returns}// ✅ fine - 'void' doesn't need a return statementfunction f2(): void {    // no returns}// ✅ fine - 'any' doesn't need a return statementfunction f3(): any {    // no returns}// ❌ error!// A function whose declared type is neither 'void' nor 'any' must return a value.function f4(): undefined {    // no returns}
```

```javascript
declare function takesFunction(f: () => undefined): undefined;// ❌ error!// Argument of type '() => void' is not assignable to parameter of type '() => undefined'.takesFunction(() => {    // no returns});// ❌ error!// A function whose declared type is neither 'void' nor 'any' must return a value.takesFunction((): undefined => {    // no returns});// ❌ error!// Argument of type '() => void' is not assignable to parameter of type '() => undefined'.takesFunction(() => {    return;});// ✅ workstakes
...
```

---

## TypeScript 5.2

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-2.html

**Contents**:
- TypeScript 5.2
- using Declarations and Explicit Resource Management
- Decorator Metadata
- Named and Anonymous Tuple Elements
- Easier Method Usage for Unions of Arrays
- Type-Only Import Paths with TypeScript Implementation File Extensions
- Comma Completions for Object Members
- Inline Variable Refactoring

Was this page helpful?

TypeScript 5.2 adds support for the upcoming Explicit Resource Management feature in ECMAScript. Let’s explore some of the motivations and understand what the feature brings us.

It’s common to need to do some sort of “clean-up” after creating an object. For example, you might need to close network connections, delete temporary files, or just free up some memory.

Let’s imagine a function that creates a temporary file, reads and writes to it for various operations, and then closes and deletes it.

This is fine, but what happens if we need to perform an early exit?

We’re starting to see some duplication of clean-up which can be easy to forget. We’re also not guaranteed to close and delete the file if an error gets thrown. This could be solved by wrapping this all in a try/finally block.

While this is more robust, it’s added quite a bit of “noise” to our code. There are also other foot-guns we can run into if we start adding more clean-up logic to our finally block — for example, exceptions preventing other resources from being disposed. This is what the explicit resource management proposal aims to solve. The key idea of the proposal is to support resource disposal — this clean-up work we’re trying to deal with — as a first class idea in JavaScript.

This starts by adding a new built-in symbol called Symbol.dispose, and we can create objects with methods named by Symbol.dispose. For convenience, TypeScript defines a new global type called Disposable which describes these.

Later on we can call those methods.

Moving the clean-up logic to TempFile itself doesn’t buy us much; we’ve basically just moved all the clean-up work from the finally block into a method, and that’s always been possible. But having a well-known “name” for this method means that JavaScript can build other features on top of it.

That brings us to the first star of the feature: using declarations! using is a new keyword that lets us declare new fixed bindings, kind of like

*[Content truncated - see full docs]*

**Examples**:

```python
import * as fs from "fs";export function doSomeWork() {    const path = ".some_temp_file";    const file = fs.openSync(path, "w+");    // use file...    // Close the file and delete it.    fs.closeSync(file);    fs.unlinkSync(path);}
```

```javascript
export function doSomeWork() {    const path = ".some_temp_file";    const file = fs.openSync(path, "w+");    // use file...    if (someCondition()) {        // do some more work...        // Close the file and delete it.        fs.closeSync(file);        fs.unlinkSync(path);        return;    }    // Close the file and delete it.    fs.closeSync(file);    fs.unlinkSync(path);}
```

```javascript
export function doSomeWork() {    const path = ".some_temp_file";    const file = fs.openSync(path, "w+");    try {        // use file...        if (someCondition()) {            // do some more work...            return;        }    }    finally {        // Close the file and delete it.        fs.closeSync(file);        fs.unlinkSync(path);    }}
```

---

## TypeScript 5.3

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-3.html

**Contents**:
- TypeScript 5.3
- Import Attributes
- Stable Support resolution-mode in Import Types
- resolution-mode Supported in All Module Modes
- switch (true) Narrowing
- Narrowing On Comparisons to Booleans
- instanceof Narrowing Through Symbol.hasInstance
- Checks for super Property Accesses on Instance Fields

Was this page helpful?

TypeScript 5.3 supports the latest updates to the import attributes proposal.

One use-case of import attributes is to provide information about the expected format of a module to the runtime.

The contents of these attributes are not checked by TypeScript since they’re host-specific, and are simply left alone so that browsers and runtimes can handle them (and possibly error).

Dynamic import() calls can also use import attributes through a second argument.

The expected type of that second argument is defined by a type called ImportCallOptions, which by default just expects a property called with.

Note that import attributes are an evolution of an earlier proposal called “import assertions”, which were implemented in TypeScript 4.5. The most obvious difference is the use of the with keyword over the assert keyword. But the less-visible difference is that runtimes are now free to use attributes to guide the resolution and interpretation of import paths, whereas import assertions could only assert some characteristics after loading a module.

Over time, TypeScript will be deprecating the old syntax for import assertions in favor of the proposed syntax for import attributes. Existing code using assert should migrate towards the with keyword. New code that needs an import attribute should use with exclusively.

We’d like to thank Oleksandr Tarasiuk for implementing this proposal! And we’d also like to call out Wenlu Wang for their implementation of import assertions!

In TypeScript 4.7, TypeScript added support for a resolution-mode attribute in /// <reference types="..." /> to control whether a specifier should be resolved via import or require semantics.

A corresponding field was added to import assertions on type-only imports as well; however, it was only supported in nightly versions of TypeScript. The rationale was that in spirit, import assertions were not intended to guide module resolution. So this feature was shipped experimentally in

*[Content truncated - see full docs]*

**Examples**:

```python
// We only want this to be interpreted as JSON,// not a runnable/malicious JavaScript file with a `.json` extension.import obj from "./something.json" with { type: "json" };
```

```python
// TypeScript is fine with this.// But your browser? Probably not.import * as foo from "./foo.js" with { type: "fluffy bunny" };
```

```javascript
const obj = await import("./something.json", {    with: { type: "json" }});
```

---

## TypeScript 5.4

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-4.html

**Contents**:
- TypeScript 5.4
- Preserved Narrowing in Closures Following Last Assignments
- The NoInfer Utility Type
- Object.groupBy and Map.groupBy
- Support for require() calls in --moduleResolution bundler and --module preserve
- Checked Import Attributes and Assertions
- Quick Fix for Adding Missing Parameters
- Upcoming Changes from TypeScript 5.0 Deprecations

Was this page helpful?

TypeScript can usually figure out a more specific type for a variable based on checks that you might perform. This process is called narrowing.

One common pain point was that these narrowed types weren’t always preserved within function closures.

Here, TypeScript decided that it wasn’t “safe” to assume that url was actually a URL object in our callback function because it was mutated elsewhere; however, in this instance, that arrow function is always created after that assignment to url, and it’s also the last assignment to url.

TypeScript 5.4 takes advantage of this to make narrowing a little smarter. When parameters and let variables are used in non-hoisted functions, the type-checker will look for a last assignment point. If one is found, TypeScript can safely narrow from outside the containing function. What that means is the above example just works now.

Note that narrowing analysis doesn’t kick in if the variable is assigned anywhere in a nested function. This is because there’s no way to know for sure whether the function will be called later.

This should make lots of typical JavaScript code easier to express. You can read more about the change on GitHub.

When calling generic functions, TypeScript is able to infer type arguments from whatever you pass in.

One challenge, however, is that it is not always clear what the “best” type is to infer. This might lead to TypeScript rejecting valid calls, accepting questionable calls, or just reporting worse error messages when it catches a bug.

For example, let’s imagine a createStreetLight function that takes a list of color names, along with an optional default color.

What happens when we pass in a defaultColor that wasn’t in the original colors array? In this function, colors is supposed to be the “source of truth” and describe what can be passed to defaultColor.

In this call, type inference decided that "blue" was just as valid of a type as "red" or "yellow" or "green". So instead 

*[Content truncated - see full docs]*

**Examples**:

```javascript
function uppercaseStrings(x: string | number) {    if (typeof x === "string") {        // TypeScript knows 'x' is a 'string' here.        return x.toUpperCase();    }}
```

```javascript
function getUrls(url: string | URL, names: string[]) {    if (typeof url === "string") {        url = new URL(url);    }    return names.map(name => {        url.searchParams.set("name", name)        //  ~~~~~~~~~~~~        // error!        // Property 'searchParams' does not exist on type 'string | URL'.        return url.toString();    });}
```

```javascript
function printValueLater(value: string | undefined) {    if (value === undefined) {        value = "missing!";    }    setTimeout(() => {        // Modifying 'value', even in a way that shouldn't affect        // its type, will invalidate type refinements in closures.        value = value;    }, 500);    setTimeout(() => {        console.log(value.toUpperCase());        //          ~~~~~        // error! 'value' is possibly 'undefined'.    }, 1000);}
```

---

## TypeScript 5.5

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-5.html

**Contents**:
- TypeScript 5.5
- Inferred Type Predicates
- Control Flow Narrowing for Constant Indexed Accesses
- The JSDoc @import Tag
- Regular Expression Syntax Checking
- Support for New ECMAScript Set Methods
- Isolated Declarations
  - Use-case: Faster Declaration Emit Tools

Was this page helpful?

This section was written by Dan Vanderkam, who implemented this feature in TypeScript 5.5. Thanks Dan!

TypeScript’s control flow analysis does a great job of tracking how the type of a variable changes as it moves through your code:

By making you handle the undefined case, TypeScript pushes you to write more robust code.

In the past, this sort of type refinement was more difficult to apply to arrays. This would have been an error in all previous versions of TypeScript:

This code is perfectly fine: we’ve filtered all the undefined values out of the list. But TypeScript hasn’t been able to follow along.

With TypeScript 5.5, the type checker is fine with this code:

Note the more precise type for birds.

This works because TypeScript now infers a type predicate for the filter function. You can see what’s going on more clearly by pulling it out into a standalone function:

bird is Bird is the type predicate. It means that, if the function returns true, then it’s a Bird (if the function returns false then it’s undefined). The type declarations for Array.prototype.filter know about type predicates, so the net result is that you get a more precise type and the code passes the type checker.

TypeScript will infer that a function returns a type predicate if these conditions hold:

Generally this works how you’d expect. Here’s a few more examples of inferred type predicates:

Previously, TypeScript would have just inferred that these functions return boolean. It now infers signatures with type predicates like x is number or x is NonNullable<T>.

Type predicates have “if and only if” semantics. If a function returns x is T, then it means that:

If you’re expecting a type predicate to be inferred but it’s not, then you may be running afoul of the second rule. This often comes up with “truthiness” checks:

TypeScript did not infer a type predicate for score => !!score, and rightly so: if this returns true then score is a number. But if it returns fal

*[Content truncated - see full docs]*

**Examples**:

```javascript
interface Bird {    commonName: string;    scientificName: string;    sing(): void;}// Maps country names -> national bird.// Not all nations have official birds (looking at you, Canada!)declare const nationalBirds: Map<string, Bird>;function makeNationalBirdCall(country: string) {  const bird = nationalBirds.get(country);  // bird has a declared type of Bird | undefined  if (bird) {    bird.sing();  // bird has type Bird inside the if statement  } else {    // bird has type undefined here.  }}
```

```javascript
function makeBirdCalls(countries: string[]) {  // birds: (Bird | undefined)[]  const birds = countries    .map(country => nationalBirds.get(country))    .filter(bird => bird !== undefined);  for (const bird of birds) {    bird.sing();  // error: 'bird' is possibly 'undefined'.  }}
```

```javascript
function makeBirdCalls(countries: string[]) {  // birds: Bird[]  const birds = countries    .map(country => nationalBirds.get(country))    .filter(bird => bird !== undefined);  for (const bird of birds) {    bird.sing();  // ok!  }}
```

---

## TypeScript 5.6

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-6.html

**Contents**:
- TypeScript 5.6
- Disallowed Nullish and Truthy Checks
- Iterator Helper Methods
- Strict Builtin Iterator Checks (and --strictBuiltinIteratorReturn)
- Support for Arbitrary Module Identifiers
- The --noUncheckedSideEffectImports Option
- The --noCheck Option
- Allow --build with Intermediate Errors

Was this page helpful?

Maybe you’ve written a regex and forgotten to call .test(...) on it:

or maybe you’ve accidentally written => (which creates an arrow function) instead of >= (the greater-than-or-equal-to operator):

or maybe you’ve tried to use a default value with ??, but mixed up the precedence of ?? and a comparison operator like <:

or maybe you’ve misplaced a parenthesis in a complex expression:

None of these examples do what the author intended, but they’re all valid JavaScript code. Previously TypeScript also quietly accepted these examples.

But with a little bit of experimentation, we found that many many bugs could be caught from flagging down suspicious examples like above. In TypeScript 5.6, the compiler now errors when it can syntactically determine a truthy or nullish check will always evaluate in a specific way. So in the above examples, you’ll start to see errors:

Similar results can be achieved by enabling the ESLint no-constant-binary-expression rule, and you can see some of the results they achieved in their blog post; but the new checks TypeScript performs does not have perfect overlap with the ESLint rule, and we also believe there is a lot of value in having these checks built into TypeScript itself.

Note that certain expressions are still allowed, even if they are always truthy or nullish. Specifically, true, false, 0, and 1 are all still allowed despite always being truthy or falsy, since code like the following:

is still idiomatic and useful, and code like the following:

is useful while iterating/debugging code.

If you’re curious about the implementation or the sorts of bugs it catches, take a look at the pull request that implemented this feature.

JavaScript has a notion of iterables (things which we can iterate over by calling a [Symbol.iterator]() and getting an iterator) and iterators (things which have a next() method which we can call to try to get the next value as we iterate). By and large, you don’t typically have to 

*[Content truncated - see full docs]*

**Examples**:

```text
if (/0x[0-9a-f]/) {    // Oops! This block always runs.    // ...}
```

```javascript
if (x => 0) {    // Oops! This block always runs.    // ...}
```

```javascript
function isValid(value: string | number, options: any, strictness: "strict" | "loose") {    if (strictness === "loose") {        value = +value    }    return value < options.max ?? 100;    // Oops! This is parsed as (value < options.max) ?? 100}
```

---

## TypeScript 5.7

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-7.html

**Contents**:
- TypeScript 5.7
- Checks for Never-Initialized Variables
- Path Rewriting for Relative Paths
- Support for --target es2024 and --lib es2024
- Searching Ancestor Configuration Files for Project Ownership
- Faster Project Ownership Checks in Editors for Composite Projects
  - Validated JSON Imports in --module nodenext
- Support for V8 Compile Caching in Node.js

Was this page helpful?

For a long time, TypeScript has been able to catch issues when a variable has not yet been initialized in all prior branches.

Unfortunately, there are some places where this analysis doesn’t work. For example, if the variable is accessed in a separate function, the type system doesn’t know when the function will be called, and instead takes an “optimistic” view that the variable will be initialized.

While TypeScript 5.7 is still lenient on variables that have possibly been initialized, the type system is able to report errors when variables have never been initialized at all.

This change was contributed thanks to the work of GitHub user Zzzen!

There are several tools and runtimes that allow you to run TypeScript code “in-place”, meaning they do not require a build step which generates output JavaScript files. For example, ts-node, tsx, Deno, and Bun all support running .ts files directly. More recently, Node.js has been investigating such support with --experimental-strip-types (soon to be unflagged!) and --experimental-transform-types. This is extremely convenient because it allows us to iterate faster without worrying about re-running a build task.

There is some complexity to be aware of when using these modes though. To be maximally compatible with all these tools, a TypeScript file that’s imported “in-place” must be imported with the appropriate TypeScript extension at runtime. For example, to import a file called foo.ts, we have to write the following in Node’s new experimental support:

Typically, TypeScript would issue an error if we did this, because it expects us to import the output file. Because some tools do allow .ts imports, TypeScript has supported this import style with an option called --allowImportingTsExtensions for a while now. This works fine, but what happens if we need to actually generate .js files out of these .ts files? This is a requirement for library authors who will need to be able to distribute just .js fil

*[Content truncated - see full docs]*

**Examples**:

```javascript
let result: numberif (someCondition()) {    result = doSomeWork();}else {    let temporaryWork = doSomeWork();    temporaryWork *= 2;    // forgot to assign to 'result'}console.log(result); // error: Variable 'result' is used before being assigned.
```

```javascript
function foo() {    let result: number    if (someCondition()) {        result = doSomeWork();    }    else {        let temporaryWork = doSomeWork();        temporaryWork *= 2;        // forgot to assign to 'result'    }    printResult();    function printResult() {        console.log(result); // no error here.    }}
```

```javascript
function foo() {    let result: number        // do work, but forget to assign to 'result'    function printResult() {        console.log(result); // error: Variable 'result' is used before being assigned.    }}
```

---

## TypeScript 5.8

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-8.html

**Contents**:
- TypeScript 5.8
- Granular Checks for Branches in Return Expressions
- Support for require() of ECMAScript Modules in --module nodenext
- --module node18
- The --erasableSyntaxOnly Option
- The --libReplacement Flag
- Preserved Computed Property Names in Declaration Files
- Optimizations on Program Loads and Updates

Was this page helpful?

Consider some code like the following:

The intent of this code is to retrieve a URL object from a cache if it exists, or to create a new URL object if it doesn’t. However, there’s a bug: we forgot to actually construct a new URL object with the input. Unfortunately, TypeScript generally didn’t catch this sort of bug.

When TypeScript checks conditional expressions like cond ? trueBranch : falseBranch, its type is treated as a union of the types of the two branches. In other words, it gets the type of trueBranch and falseBranch, and combines them into a union type. In this case, the type of untypedCache.get(urlString) is any, and the type of urlString is string. This is where things go wrong because any is so infectious in how it interacts with other types. The union any | string is simplified to any, so by the time TypeScript starts checking whether the expression in our return statement is compatible with the expected return type of URL, the type system has lost any information that would have caught the bug in this code.

In TypeScript 5.8, the type system special-cases conditional expressions directly inside return statements. Each branch of the conditional is checked against the declared return type of the containing functions (if one exists), so the type system can catch the bug in the example above.

This change was made within this pull request, as part of a broader set of future improvements for TypeScript.

For years, Node.js supported ECMAScript modules (ESM) alongside CommonJS modules. Unfortunately, the interoperability between the two had some challenges.

In other words, consuming CommonJS files from ESM files was possible, but not the other way around. This introduced many challenges for library authors who wanted to provide ESM support. These library authors would either have to break compatibility with CommonJS users, “dual-publish” their libraries (providing separate entry-points for ESM and CommonJS), or just stay on Commo

*[Content truncated - see full docs]*

**Examples**:

```javascript
declare const untypedCache: Map<any, any>;function getUrlObject(urlString: string): URL {    return untypedCache.has(urlString) ?        untypedCache.get(urlString) :        urlString;}
```

```javascript
declare const untypedCache: Map<any, any>;function getUrlObject(urlString: string): URL {    return untypedCache.has(urlString) ?        untypedCache.get(urlString) :        urlString;    //  ~~~~~~~~~    // error! Type 'string' is not assignable to type 'URL'.}
```

```text
// ❌ error: An `import ... = require(...)` aliasimport foo = require("foo");// ❌ error: A namespace with runtime code.namespace container {}// ❌ error: An `import =` aliasimport Bar = container.Bar;class Point {    // ❌ error: Parameter properties    constructor(public x: number, public y: number) { }}// ❌ error: An `export =` assignment.export = Point;// ❌ error: An enum declaration.enum Direction {    Up,    Down,    Left,    Right,}
```

---

## TypeScript 5.9

**URL**: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-9.html

**Contents**:
- TypeScript 5.9
- Minimal and Updated tsc --init
- Support for import defer
- Support for --module node20
- Summary Descriptions in DOM APIs
- Expandable Hovers (Preview)
- Configurable Maximum Hover Length
- Optimizations

Was this page helpful?

For a while, the TypeScript compiler has supported an --init flag that can create a tsconfig.json within the current directory. In the last few years, running tsc --init created a very “full” tsconfig.json, filled with commented-out settings and their descriptions. We designed this with the intent of making options discoverable and easy to toggle.

However, given external feedback (and our own experience), we found it’s common to immediately delete most of the contents of these new tsconfig.json files. When users want to discover new options, we find they rely on auto-complete from their editor, or navigate to the tsconfig reference on our website (which the generated tsconfig.json links to!). What each setting does is also documented on that same page, and can be seen via editor hovers/tooltips/quick info. While surfacing some commented-out settings might be helpful, the generated tsconfig.json was often considered overkill.

We also felt that it was time that tsc --init initialized with a few more prescriptive settings than we already enable. We looked at some common pain points and papercuts users have when they create a new TypeScript project. For example, most users write in modules (not global scripts), and --moduleDetection can force TypeScript to treat every implementation file as a module. Developers also often want to use the latest ECMAScript features directly in their runtime, so --target can typically be set to esnext. JSX users often find that going back to set --jsx is needless friction, and its options are slightly confusing. And often, projects end up loading more declaration files from node_modules/@types than TypeScript actually needs; but specifying an empty types array can help limit this.

In TypeScript 5.9, a plain tsc --init with no other flags will generate the following tsconfig.json:

For more details, see the implementing pull request and discussion issue.

TypeScript 5.9 introduces support for ECMAScript’s deferre

*[Content truncated - see full docs]*

**Examples**:

```text
{  // Visit https://aka.ms/tsconfig to read more about this file  "compilerOptions": {    // File Layout    // "rootDir": "./src",    // "outDir": "./dist",    // Environment Settings    // See also https://aka.ms/tsconfig_modules    "module": "nodenext",    "target": "esnext",    "types": [],    // For nodejs:    // "lib": ["esnext"],    // "types": ["node"],    // and npm install -D @types/node    // Other Outputs    "sourceMap": true,    "declaration": true,    "declarationMap": true,    // S
...
```

```python
import defer * as feature from "./some-feature.js";
```

```javascript
// ./some-feature.tsinitializationWithSideEffects();function initializationWithSideEffects() {  // ...  specialConstant = 42;  console.log("Side effects have occurred!");}export let specialConstant: number;
```

---

## TypeScript Tooling in 5 minutes

**URL**: https://www.typescriptlang.org/docs/handbook/typescript-tooling-in-5-minutes.html

**Contents**:
- TypeScript Tooling in 5 minutes
- Installing TypeScript
- Building your first TypeScript file
- Compiling your code
- Type annotations
- Interfaces
- Classes
- Running your TypeScript web app

Was this page helpful?

Let’s get started by building a simple web application with TypeScript.

There are two main ways to add TypeScript to your project:

Visual Studio 2017 and Visual Studio 2015 Update 3 include TypeScript language support by default but does not include the TypeScript compiler, tsc. If you didn’t install TypeScript with Visual Studio, you can still download it.

In your editor, type the following JavaScript code in greeter.ts:

We used a .ts extension, but this code is just JavaScript. You could have copy/pasted this straight out of an existing JavaScript app.

At the command line, run the TypeScript compiler:

The result will be a file greeter.js which contains the same JavaScript that you fed in. We’re up and running using TypeScript in our JavaScript app!

Now we can start taking advantage of some of the new tools TypeScript offers. Add a : string type annotation to the ‘person’ function parameter as shown here:

Type annotations in TypeScript are lightweight ways to record the intended contract of the function or variable. In this case, we intend the greeter function to be called with a single string parameter. We can try changing the call greeter to pass an array instead:

Re-compiling, you’ll now see an error:

Similarly, try removing all the arguments to the greeter call. TypeScript will let you know that you have called this function with an unexpected number of arguments. In both cases, TypeScript can offer static analysis based on both the structure of your code, and the type annotations you provide.

Notice that although there were errors, the greeter.js file is still created. You can use TypeScript even if there are errors in your code. But in this case, TypeScript is warning that your code will likely not run as expected.

Let’s develop our sample further. Here we use an interface that describes objects that have a firstName and lastName field. In TypeScript, two types are compatible if their internal structure is compatible. This 

*[Content truncated - see full docs]*

**Examples**:

```text
> npm install -g typescript
```

```javascript
function greeter(person) {  return "Hello, " + person;} let user = "Jane User"; document.body.textContent = greeter(user);
```

```text
tsc greeter.ts
```

---

## TypeScript for Functional Programmers

**URL**: https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes-func.html

**Contents**:
- TypeScript for Functional Programmers
- Prerequisites
- Concepts not in Haskell
  - Built-in types
    - Other important TypeScript types
    - Boxed types
  - Gradual typing
  - Structural typing

Was this page helpful?

TypeScript began its life as an attempt to bring traditional object-oriented types to JavaScript so that the programmers at Microsoft could bring traditional object-oriented programs to the web. As it has developed, TypeScript’s type system has evolved to model code written by native JavaScripters. The resulting system is powerful, interesting and messy.

This introduction is designed for working Haskell or ML programmers who want to learn TypeScript. It describes how the type system of TypeScript differs from Haskell’s type system. It also describes unique features of TypeScript’s type system that arise from its modelling of JavaScript code.

This introduction does not cover object-oriented programming. In practice, object-oriented programs in TypeScript are similar to those in other popular languages with OO features.

In this introduction, I assume you know the following:

If you need to learn the good parts of JavaScript, read JavaScript: The Good Parts. You may be able to skip the book if you know how to write programs in a call-by-value lexically scoped language with lots of mutability and not much else. R4RS Scheme is a good example.

The C++ Programming Language is a good place to learn about C-style type syntax. Unlike C++, TypeScript uses postfix types, like so: x: string instead of string x.

JavaScript defines 8 built-in types:

See the MDN page for more detail.

TypeScript has corresponding primitive types for the built-in types:

Function syntax includes parameter names. This is pretty hard to get used to!

Object literal type syntax closely mirrors object literal value syntax:

[T, T] is a subtype of T[]. This is different than Haskell, where tuples are not related to lists.

JavaScript has boxed equivalents of primitive types that contain the methods that programmers associate with those types. TypeScript reflects this with, for example, the difference between the primitive type number and the boxed type Number. The boxed type

*[Content truncated - see full docs]*

**Examples**:

```javascript
let fst: (a: any, b: any) => any = (a, b) => a;// or more precisely:let fst: <T, U>(a: T, b: U) => T = (a, b) => a;
```

```javascript
let o: { n: number; xs: object[] } = { n: 1, xs: [] };
```

```text
(1).toExponential();// equivalent toNumber.prototype.toExponential.call(1);
```

---

## TypeScript for Java/C# Programmers

**URL**: https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes-oop.html

**Contents**:
- TypeScript for Java/C# Programmers
- Co-learning JavaScript
- Rethinking the Class
  - Free Functions and Data
  - Static Classes
- OOP in TypeScript
- Rethinking Types
  - Nominal Reified Type Systems

Was this page helpful?

TypeScript is a popular choice for programmers accustomed to other languages with static typing, such as C# and Java.

TypeScript’s type system offers many of the same benefits, such as better code completion, earlier detection of errors, and clearer communication between parts of your program. While TypeScript provides many familiar features for these developers, it’s worth stepping back to see how JavaScript (and therefore TypeScript) differ from traditional OOP languages. Understanding these differences will help you write better JavaScript code, and avoid common pitfalls that programmers who go straight from C#/Java to TypeScript may fall into.

If you’re familiar with JavaScript already but are primarily a Java or C# programmer, this introductory page can help explain some of the common misconceptions and pitfalls you might be susceptible to. Some of the ways that TypeScript models types are quite different from Java or C#, and it’s important to keep these in mind when learning TypeScript.

If you’re a Java or C# programmer that is new to JavaScript in general, we recommend learning a little bit of JavaScript without types first to understand JavaScript’s runtime behaviors. Because TypeScript doesn’t change how your code runs, you’ll still have to learn how JavaScript works in order to write code that actually does something!

It’s important to remember that TypeScript uses the same runtime as JavaScript, so any resources about how to accomplish specific runtime behavior (converting a string to a number, displaying an alert, writing a file to disk, etc.) will always apply equally well to TypeScript programs. Don’t limit yourself to TypeScript-specific resources!

C# and Java are what we might call mandatory OOP languages. In these languages, the class is the basic unit of code organization, and also the basic container of all data and behavior at runtime. Forcing all functionality and data to be held in classes can be a good domain model

*[Content truncated - see full docs]*

**Examples**:

```javascript
interface Pointlike {  x: number;  y: number;}interface Named {  name: string;} function logPoint(point: Pointlike) {  console.log("x = " + point.x + ", y = " + point.y);} function logName(x: Named) {  console.log("Hello, " + x.name);} const obj = {  x: 0,  y: 0,  name: "Origin",}; logPoint(obj);logName(obj);
```

```javascript
class Empty {} function fn(arg: Empty) {  // do something?} // No error, but this isn't an 'Empty' ?fn({ k: 10 });
```

```javascript
class Car {  drive() {    // hit the gas  }}class Golfer {  drive() {    // hit the ball far  }}// No error?let w: Car = new Golfer();
```

---

## TypeScript for JavaScript Programmers

**URL**: https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html

**Contents**:
- TypeScript for JavaScript Programmers
- Types by Inference
- Defining Types
- Composing Types
  - Unions
  - Generics
- Structural Type System
- Next Steps

Was this page helpful?

TypeScript stands in an unusual relationship to JavaScript. TypeScript offers all of JavaScript’s features, and an additional layer on top of these: TypeScript’s type system.

For example, JavaScript provides language primitives like string and number, but it doesn’t check that you’ve consistently assigned these. TypeScript does.

This means that your existing working JavaScript code is also TypeScript code. The main benefit of TypeScript is that it can highlight unexpected behavior in your code, lowering the chance of bugs.

This tutorial provides a brief overview of TypeScript, focusing on its type system.

TypeScript knows the JavaScript language and will generate types for you in many cases. For example in creating a variable and assigning it to a particular value, TypeScript will use the value as its type.

By understanding how JavaScript works, TypeScript can build a type-system that accepts JavaScript code but has types. This offers a type-system without needing to add extra characters to make types explicit in your code. That’s how TypeScript knows that helloWorld is a string in the above example.

You may have written JavaScript in Visual Studio Code, and had editor auto-completion. Visual Studio Code uses TypeScript under the hood to make it easier to work with JavaScript.

You can use a wide variety of design patterns in JavaScript. However, some design patterns make it difficult for types to be inferred automatically (for example, patterns that use dynamic programming). To cover these cases, TypeScript supports an extension of the JavaScript language, which offers places for you to tell TypeScript what the types should be.

For example, to create an object with an inferred type which includes name: string and id: number, you can write:

You can explicitly describe this object’s shape using an interface declaration:

You can then declare that a JavaScript object conforms to the shape of your new interface by using syntax like : Typ

*[Content truncated - see full docs]*

**Examples**:

```javascript
let helloWorld = "Hello World";        let helloWorld: string
```

```javascript
const user = {  name: "Hayes",  id: 0,};
```

```text
interface User {  name: string;  id: number;}
```

---

## TypeScript for the New Programmer

**URL**: https://www.typescriptlang.org/docs/handbook/typescript-from-scratch.html

**Contents**:
- TypeScript for the New Programmer
- What is JavaScript? A Brief History
- TypeScript: A Static Type Checker
  - A Typed Superset of JavaScript
    - Syntax
    - Types
    - Runtime Behavior
    - Erased Types

Was this page helpful?

Congratulations on choosing TypeScript as one of your first languages — you’re already making good decisions!

You’ve probably already heard that TypeScript is a “flavor” or “variant” of JavaScript. The relationship between TypeScript (TS) and JavaScript (JS) is rather unique among modern programming languages, so learning more about this relationship will help you understand how TypeScript adds to JavaScript.

JavaScript (also known as ECMAScript) started its life as a simple scripting language for browsers. At the time it was invented, it was expected to be used for short snippets of code embedded in a web page — writing more than a few dozen lines of code would have been somewhat unusual. Due to this, early web browsers executed such code pretty slowly. Over time, though, JS became more and more popular, and web developers started using it to create interactive experiences.

Web browser developers responded to this increased JS usage by optimizing their execution engines (dynamic compilation) and extending what could be done with it (adding APIs), which in turn made web developers use it even more. On modern websites, your browser is frequently running applications that span hundreds of thousands of lines of code. This is the long and gradual growth of “the web”, starting as a simple network of static pages, and evolving into a platform for rich applications of all kinds.

More than this, JS has become popular enough to be used outside the context of browsers, such as implementing JS servers using node.js. The “run anywhere” nature of JS makes it an attractive choice for cross-platform development. There are many developers these days that use only JavaScript to program their entire stack!

To summarize, we have a language that was designed for quick uses, and then grew to a full-fledged tool to write applications with millions of lines. Every language has its own quirks — oddities and surprises, and JavaScript’s humble beginning makes it 

*[Content truncated - see full docs]*

**Examples**:

```text
if ("" == 0) {  // It is! But why??}if (1 < x < 3) {  // True for *any* value of x!}
```

```javascript
const obj = { width: 10, height: 15 };// Why is this NaN? Spelling is hard!const area = obj.width * obj.heigth;
```

```javascript
const obj = { width: 10, height: 15 };const area = obj.width * obj.heigth;Property 'heigth' does not exist on type '{ width: number; height: number; }'. Did you mean 'height'?2551Property 'heigth' does not exist on type '{ width: number; height: number; }'. Did you mean 'height'?
```

---

## Type Checking JavaScript Files

**URL**: https://www.typescriptlang.org/docs/handbook/type-checking-javascript-files.html

**Contents**:
- Type Checking JavaScript Files
- Properties are inferred from assignments in class bodies
- Constructor functions are equivalent to classes
- CommonJS modules are supported
- Classes, functions, and object literals are namespaces
- Object literals are open-ended
- null, undefined, and empty array initializers are of type any or any[]
- Function parameters are optional by default

Was this page helpful?

Here are some notable differences on how checking works in .js files compared to .ts files.

ES2015 does not have a means for declaring properties on classes. Properties are dynamically assigned, just like object literals.

In a .js file, the compiler infers properties from property assignments inside the class body. The type of a property is the type given in the constructor, unless it’s not defined there, or the type in the constructor is undefined or null. In that case, the type is the union of the types of all the right-hand values in these assignments. Properties defined in the constructor are always assumed to exist, whereas ones defined just in methods, getters, or setters are considered optional.

If properties are never set in the class body, they are considered unknown. If your class has properties that are only read from, add and then annotate a declaration in the constructor with JSDoc to specify the type. You don’t even have to give a value if it will be initialized later:

Before ES2015, JavaScript used constructor functions instead of classes. The compiler supports this pattern and understands constructor functions as equivalent to ES2015 classes. The property inference rules described above work exactly the same way.

In a .js file, TypeScript understands the CommonJS module format. Assignments to exports and module.exports are recognized as export declarations. Similarly, require function calls are recognized as module imports. For example:

The module support in JavaScript is much more syntactically forgiving than TypeScript’s module support. Most combinations of assignments and declarations are supported.

Classes are namespaces in .js files. This can be used to nest classes, for example:

And, for pre-ES2015 code, it can be used to simulate static methods:

It can also be used to create simple namespaces:

Other variants are allowed as well:

In a .ts file, an object literal that initializes a variable declaration gives it

*[Content truncated - see full docs]*

**Examples**:

```text
class C {  constructor() {    this.constructorOnly = 0;    this.constructorUnknown = undefined;  }  method() {    this.constructorOnly = false;Type 'boolean' is not assignable to type 'number'.2322Type 'boolean' is not assignable to type 'number'.    this.constructorUnknown = "plunkbat"; // ok, constructorUnknown is string | undefined    this.methodOnly = "ok"; // ok, but methodOnly could also be undefined  }  method2() {    this.methodOnly = true; // also, ok, methodOnly's type is string | bool
...
```

```javascript
class C {  constructor() {    /** @type {number | undefined} */    this.prop = undefined;    /** @type {number | undefined} */    this.count;  }} let c = new C();c.prop = 0; // OKc.count = "string";Type 'string' is not assignable to type 'number'.2322Type 'string' is not assignable to type 'number'.
```

```javascript
function C() {  this.constructorOnly = 0;  this.constructorUnknown = undefined;}C.prototype.method = function () {  this.constructorOnly = false;Type 'boolean' is not assignable to type 'number'.2322Type 'boolean' is not assignable to type 'number'.  this.constructorUnknown = "plunkbat"; // OK, the type is string | undefined};
```

---

## Type Compatibility

**URL**: https://www.typescriptlang.org/docs/handbook/type-compatibility.html

**Contents**:
- Type Compatibility
- A Note on Soundness
- Starting out
- Comparing two functions
  - Function Parameter Bivariance
  - Optional Parameters and Rest Parameters
  - Functions with overloads
- Enums

Was this page helpful?

Type compatibility in TypeScript is based on structural subtyping. Structural typing is a way of relating types based solely on their members. This is in contrast with nominal typing. Consider the following code:

In nominally-typed languages like C# or Java, the equivalent code would be an error because the Dog class does not explicitly describe itself as being an implementer of the Pet interface.

TypeScript’s structural type system was designed based on how JavaScript code is typically written. Because JavaScript widely uses anonymous objects like function expressions and object literals, it’s much more natural to represent the kinds of relationships found in JavaScript libraries with a structural type system instead of a nominal one.

TypeScript’s type system allows certain operations that can’t be known at compile-time to be safe. When a type system has this property, it is said to not be “sound”. The places where TypeScript allows unsound behavior were carefully considered, and throughout this document we’ll explain where these happen and the motivating scenarios behind them.

The basic rule for TypeScript’s structural type system is that x is compatible with y if y has at least the same members as x. For example consider the following code involving an interface named Pet which has a name property:

To check whether dog can be assigned to pet, the compiler checks each property of pet to find a corresponding compatible property in dog. In this case, dog must have a member called name that is a string. It does, so the assignment is allowed.

The same rule for assignment is used when checking function call arguments:

Note that dog has an extra owner property, but this does not create an error. Only members of the target type (Pet in this case) are considered when checking for compatibility. This comparison process proceeds recursively, exploring the type of each member and sub-member.

Be aware, however, that object literals may only spe

*[Content truncated - see full docs]*

**Examples**:

```javascript
interface Pet {  name: string;}class Dog {  name: string;}let pet: Pet;// OK, because of structural typingpet = new Dog();
```

```javascript
interface Pet {  name: string;}let pet: Pet;// dog's inferred type is { name: string; owner: string; }let dog = { name: "Lassie", owner: "Rudd Weatherwax" };pet = dog;
```

```javascript
interface Pet {  name: string;}let dog = { name: "Lassie", owner: "Rudd Weatherwax" };function greet(pet: Pet) {  console.log("Hello, " + pet.name);}greet(dog); // OK
```

---

## Type Inference

**URL**: https://www.typescriptlang.org/docs/handbook/type-inference.html

**Contents**:
- Type Inference
- Best common type
- Contextual Typing
      - On this page
      - Is this page helpful?

Was this page helpful?

In TypeScript, there are several places where type inference is used to provide type information when there is no explicit type annotation. For example, in this code

The type of the x variable is inferred to be number. This kind of inference takes place when initializing variables and members, setting parameter default values, and determining function return types.

In most cases, type inference is straightforward. In the following sections, we’ll explore some of the nuances in how types are inferred.

When a type inference is made from several expressions, the types of those expressions are used to calculate a “best common type”. For example,

To infer the type of x in the example above, we must consider the type of each array element. Here we are given two choices for the type of the array: number and null. The best common type algorithm considers each candidate type, and picks the type that is compatible with all the other candidates.

Because the best common type has to be chosen from the provided candidate types, there are some cases where types share a common structure, but no one type is the super type of all candidate types. For example:

Ideally, we may want zoo to be inferred as an Animal[], but because there is no object that is strictly of type Animal in the array, we make no inference about the array element type. To correct this, explicitly provide the type when no one type is a super type of all other candidates:

When no best common type is found, the resulting inference is the union array type, (Rhino | Elephant | Snake)[].

Type inference also works in “the other direction” in some cases in TypeScript. This is known as “contextual typing”. Contextual typing occurs when the type of an expression is implied by its location. For example:

Here, the TypeScript type checker used the type of the Window.onmousedown function to infer the type of the function expression on the right hand side of the assignment. When it did so, it wa

*[Content truncated - see full docs]*

**Examples**:

```javascript
let x = 3;   let x: number
```

```javascript
let x = [0, 1, null];   let x: (number | null)[]
```

```javascript
let zoo = [new Rhino(), new Elephant(), new Snake()];    let zoo: (Rhino | Elephant | Snake)[]
```

---

## Typeof Type Operator

**URL**: https://www.typescriptlang.org/docs/handbook/2/typeof-types.html

**Contents**:
- Typeof Type Operator
- The typeof type operator
  - Limitations
      - On this page
      - Is this page helpful?
  - Keyof Type Operator
  - Indexed Access Types

Was this page helpful?

JavaScript already has a typeof operator you can use in an expression context:

TypeScript adds a typeof operator you can use in a type context to refer to the type of a variable or property:

This isn’t very useful for basic types, but combined with other type operators, you can use typeof to conveniently express many patterns. For an example, let’s start by looking at the predefined type ReturnType<T>. It takes a function type and produces its return type:

If we try to use ReturnType on a function name, we see an instructive error:

Remember that values and types aren’t the same thing. To refer to the type that the value f has, we use typeof:

TypeScript intentionally limits the sorts of expressions you can use typeof on.

Specifically, it’s only legal to use typeof on identifiers (i.e. variable names) or their properties. This helps avoid the confusing trap of writing code you think is executing, but isn’t:

Using the keyof operator in type contexts.

Using Type['a'] syntax to access a subset of a type.

The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤

Last updated: Oct 13, 2025

**Examples**:

```text
// Prints "string"console.log(typeof "Hello world");
```

```javascript
let s = "hello";let n: typeof s;   let n: string
```

```javascript
type Predicate = (x: unknown) => boolean;type K = ReturnType<Predicate>;    type K = boolean
```

---

## Using Babel with TypeScript

**URL**: https://www.typescriptlang.org/docs/handbook/babel-with-typescript.html

**Contents**:
- Using Babel with TypeScript
- Babel vs tsc for TypeScript
- Babel for transpiling, tsc for types
    - Type Checking and d.ts file generation
      - On this page
      - Is this page helpful?

Was this page helpful?

When making a modern JavaScript project, you might ask yourself what is the right way to convert files from TypeScript to JavaScript?

A lot of the time the answer is “it depends”, or “someone may have decided for you” depending on the project. If you are building your project with an existing framework like tsdx, Angular, NestJS or any framework mentioned in the Getting Started then this decision is handled for you.

However, a useful heuristic could be:

This is a common pattern for projects with existing build infrastructure which may have been ported from a JavaScript codebase to TypeScript.

This technique is a hybrid approach, using Babel’s preset-typescript to generate your JS files, and then using TypeScript to do type checking and .d.ts file generation.

By using babel’s support for TypeScript, you get the ability to work with existing build pipelines and are more likely to have a faster JS emit time because Babel does not type check your code.

The downside to using babel is that you don’t get type checking during the transition from TS to JS. This can mean that type errors which you miss in your editor could sneak through into production code.

In addition to that, Babel cannot create .d.ts files for your TypeScript which can make it harder to work with your project if it is a library.

To fix these issues, you would probably want to set up a command to type check your project using TSC. This likely means duplicating some of your babel config into a corresponding tsconfig.json and ensuring these flags are enabled:

For more information on these flags:

The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤

Last updated: Oct 13, 2025

**Examples**:

```text
"compilerOptions": {  // Ensure that .d.ts files are created by tsc, but not .js files  "declaration": true,  "emitDeclarationOnly": true,  // Ensure that Babel can safely transpile files in the TypeScript project  "isolatedModules": true}
```

---

## Utility Types

**URL**: https://www.typescriptlang.org/docs/handbook/utility-types.html

**Contents**:
- Utility Types
- Awaited<Type>
      - Example
- Partial<Type>
      - Example
- Required<Type>
      - Example
- Readonly<Type>

Was this page helpful?

TypeScript provides several utility types to facilitate common type transformations. These utilities are available globally.

This type is meant to model operations like await in async functions, or the .then() method on Promises - specifically, the way that they recursively unwrap Promises.

Constructs a type with all properties of Type set to optional. This utility will return a type that represents all subsets of a given type.

Constructs a type consisting of all properties of Type set to required. The opposite of Partial.

Constructs a type with all properties of Type set to readonly, meaning the properties of the constructed type cannot be reassigned.

This utility is useful for representing assignment expressions that will fail at runtime (i.e. when attempting to reassign properties of a frozen object).

Constructs an object type whose property keys are Keys and whose property values are Type. This utility can be used to map the properties of a type to another type.

Constructs a type by picking the set of properties Keys (string literal or union of string literals) from Type.

Constructs a type by picking all properties from Type and then removing Keys (string literal or union of string literals). The opposite of Pick.

Constructs a type by excluding from UnionType all union members that are assignable to ExcludedMembers.

Constructs a type by extracting from Type all union members that are assignable to Union.

Constructs a type by excluding null and undefined from Type.

Constructs a tuple type from the types used in the parameters of a function type Type.

For overloaded functions, this will be the parameters of the last signature; see Inferring Within Conditional Types.

Constructs a tuple or array type from the types of a constructor function type. It produces a tuple type with all the parameter types (or the type never if Type is not a function).

Constructs a type consisting of the return type of function Type.

For overloaded f

*[Content truncated - see full docs]*

**Examples**:

```text
type A = Awaited<Promise<string>>;    type A = string type B = Awaited<Promise<Promise<number>>>;    type B = number type C = Awaited<boolean | Promise<number>>;    type C = number | boolean
```

```javascript
interface Todo {  title: string;  description: string;} function updateTodo(todo: Todo, fieldsToUpdate: Partial<Todo>) {  return { ...todo, ...fieldsToUpdate };} const todo1 = {  title: "organize desk",  description: "clear clutter",}; const todo2 = updateTodo(todo1, {  description: "throw out trash",});
```

```javascript
interface Props {  a?: number;  b?: string;} const obj: Props = { a: 5 }; const obj2: Required<Props> = { a: 5 };Property 'b' is missing in type '{ a: number; }' but required in type 'Required<Props>'.2741Property 'b' is missing in type '{ a: number; }' but required in type 'Required<Props>'.
```

---

## Variable Declaration

**URL**: https://www.typescriptlang.org/docs/handbook/variable-declarations.html

**Contents**:
- Variable Declaration
- var declarations
  - Scoping rules
  - Variable capturing quirks
- let declarations
  - Block-scoping
  - Re-declarations and Shadowing
  - Block-scoped variable capturing

Was this page helpful?

let and const are two relatively new concepts for variable declarations in JavaScript. As we mentioned earlier, let is similar to var in some respects, but allows users to avoid some of the common “gotchas” that users run into in JavaScript.

const is an augmentation of let in that it prevents re-assignment to a variable.

With TypeScript being an extension of JavaScript, the language naturally supports let and const. Here we’ll elaborate more on these new declarations and why they’re preferable to var.

If you’ve used JavaScript offhandedly, the next section might be a good way to refresh your memory. If you’re intimately familiar with all the quirks of var declarations in JavaScript, you might find it easier to skip ahead.

Declaring a variable in JavaScript has always traditionally been done with the var keyword.

As you might’ve figured out, we just declared a variable named a with the value 10.

We can also declare a variable inside of a function:

and we can also access those same variables within other functions:

In this above example, g captured the variable a declared in f. At any point that g gets called, the value of a will be tied to the value of a in f. Even if g is called once f is done running, it will be able to access and modify a.

var declarations have some odd scoping rules for those used to other languages. Take the following example:

Some readers might do a double-take at this example. The variable x was declared within the if block, and yet we were able to access it from outside that block. That’s because var declarations are accessible anywhere within their containing function, module, namespace, or global scope - all which we’ll go over later on - regardless of the containing block. Some people call this var-scoping or function-scoping. Parameters are also function scoped.

These scoping rules can cause several types of mistakes. One problem they exacerbate is the fact that it is not an error to declare the same var

*[Content truncated - see full docs]*

**Examples**:

```text
var a = 10;
```

```javascript
function f() {  var message = "Hello, world!";  return message;}
```

```javascript
function f() {  var a = 10;  return function g() {    var b = a + 1;    return b;  };}var g = f();g(); // returns '11'
```

---

## What is a tsconfig.json

**URL**: https://www.typescriptlang.org/docs/handbook/tsconfig-json.html

**Contents**:
- What is a tsconfig.json
- Overview
- Using tsconfig.json or jsconfig.json
- Examples
- TSConfig Bases
- Details
- TSConfig Reference
- Schema

Was this page helpful?

The presence of a tsconfig.json file in a directory indicates that the directory is the root of a TypeScript project. The tsconfig.json file specifies the root files and the compiler options required to compile the project.

JavaScript projects can use a jsconfig.json file instead, which acts almost the same but has some JavaScript-related compiler flags enabled by default.

A project is compiled in one of the following ways:

When input files are specified on the command line, tsconfig.json files are ignored.

Example tsconfig.json files:

Using the files property

Using the include and exclude properties

Depending on the JavaScript runtime environment which you intend to run your code in, there may be a base configuration which you can use at github.com/tsconfig/bases. These are tsconfig.json files which your project extends from which simplifies your tsconfig.json by handling the runtime support.

For example, if you were writing a project which uses Node.js version 12 and above, then you could use the npm module @tsconfig/node12:

This lets your tsconfig.json focus on the unique choices for your project, and not all of the runtime mechanics. There are a few tsconfig bases already, and we’re hoping the community can add more for different environments.

The "compilerOptions" property can be omitted, in which case the compiler’s defaults are used. See our full list of supported Compiler Options.

To learn more about the hundreds of configuration options in the TSConfig Reference.

The tsconfig.json Schema can be found at the JSON Schema Store.

The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤

Last updated: Oct 13, 2025

**Examples**:

```text
{  "compilerOptions": {    "module": "commonjs",    "noImplicitAny": true,    "removeComments": true,    "preserveConstEnums": true,    "sourceMap": true  },  "files": [    "core.ts",    "sys.ts",    "types.ts",    "scanner.ts",    "parser.ts",    "utilities.ts",    "binder.ts",    "checker.ts",    "emitter.ts",    "program.ts",    "commandLineParser.ts",    "tsc.ts",    "diagnosticInformationMap.generated.ts"  ]}
```

```text
{  "compilerOptions": {    "module": "system",    "noImplicitAny": true,    "removeComments": true,    "preserveConstEnums": true,    "outFile": "../../built/local/tsc.js",    "sourceMap": true  },  "include": ["src/**/*"],  "exclude": ["**/*.spec.ts"]}
```

```text
{  "extends": "@tsconfig/node12/tsconfig.json",  "compilerOptions": {    "preserveConstEnums": true  },  "include": ["src/**/*"],  "exclude": ["**/*.spec.ts"]}
```

---

## 

**URL**: https://www.typescriptlang.org/docs/handbook/react-&-webpack.html

---

## 

**URL**: https://www.typescriptlang.org/docs/handbook/modules.html

---

## tsc CLI Options

**URL**: https://www.typescriptlang.org/docs/handbook/compiler-options.html

**Contents**:
- tsc CLI Options
- Using the CLI
- Compiler Options
  - CLI Commands
  - Build Options
  - Watch Options
  - Compiler Flags
- Related

Was this page helpful?

Running tsc locally will compile the closest project defined by a tsconfig.json, or you can compile a set of TypeScript files by passing in a glob of files you want. When input files are specified on the command line, tsconfig.json files are ignored.

If you’re looking for more information about the compiler options in a tsconfig, check out the TSConfig Reference

Show all compiler options.

Gives local information for help on the CLI.

Initializes a TypeScript project and creates a tsconfig.json file.

Print names of files that are part of the compilation and then stop processing.

Set the language of the messaging from TypeScript. This does not affect emit.

Compile the project given the path to its configuration file, or to a folder with a 'tsconfig.json'.

Print the final configuration instead of building.

Print the compiler's version.

Build one or more projects and their dependencies, if out of date

Delete the outputs of all projects.

Show what would be built (or deleted, if specified with '--clean')

Build all projects, including those that appear to be up to date.

Enable verbose logging.

Remove a list of directories from the watch process.

Remove a list of files from the watch mode's processing.

fixedinterval, priorityinterval, dynamicpriority, or fixedchunksize

Specify what approach the watcher should use if the system runs out of native file watchers.

Synchronously call callbacks and update the state of directory watchers on platforms that don`t support recursive watching natively.

usefsevents, fixedpollinginterval, dynamicprioritypolling, or fixedchunksizepolling

Specify how directories are watched on systems that lack recursive file-watching functionality.

fixedpollinginterval, prioritypollinginterval, dynamicprioritypolling, fixedchunksizepolling, usefsevents, or usefseventsonparentdirectory

Specify how the TypeScript watch mode works.

Enable importing files with any extension, provided a declaration file is present

*[Content truncated - see full docs]*

**Examples**:

```text
# Run a compile based on a backwards look through the fs for a tsconfig.jsontsc# Emit JS for just the index.ts with the compiler defaultstsc index.ts# Emit JS for any .ts files in the folder src, with the default settingstsc src/*.ts# Emit files referenced in with the compiler settings from tsconfig.production.jsontsc --project tsconfig.production.json# Emit d.ts files for a js file with showing compiler options which are booleanstsc index.js --declaration --emitDeclarationOnly# Emit a single .j
...
```

---
