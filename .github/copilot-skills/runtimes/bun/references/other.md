# Bun - Other

**Pages**: 4

---

## Bun.build

**URL**: https://bun.sh/docs/bundler

**Contents**:
- Why bundle?
- Basic example
- Watch mode
- Content types
  - Assets
  - Plugins
- API
  - entrypoints

Bun's fast native bundler can be used via the bun build CLI command or the Bun.build() JavaScript API.

It's fast. The numbers below represent performance on esbuild's three.js benchmark.

The bundler is a key piece of infrastructure in the JavaScript ecosystem. As a brief overview of why bundling is so important:

Let's jump into the bundler API.

Note that the Bun bundler is not intended to replace tsc for typechecking or generating type declarations.

Let's build our first bundle. You have the following two files, which implement a simple client-side rendered React app.

Here, index.tsx is the "entrypoint" to our application. Commonly, this will be a script that performs some side effect, like starting a server or—in this case—initializing a React root. Because we're using TypeScript & JSX, we need to bundle our code before it can be sent to the browser.

To create our bundle:

For each file specified in entrypoints, Bun will generate a new bundle. This bundle will be written to disk in the ./out directory (as resolved from the current working directory). After running the build, the file system looks like this:

The contents of out/index.js will look something like this:

Tutorial: Run this file in your browser

We can load this file in the browser to see our app in action. Create an index.html file in the out directory:

Then paste the following contents into it:

Then spin up a static file server serving the out directory:

Visit http://localhost:5000 to see your bundled app in action.

Like the runtime and test runner, the bundler supports watch mode natively.

Like the Bun runtime, the bundler supports an array of file types out of the box. The following table breaks down the bundler's set of standard "loaders". Refer to Bundler > File types for full documentation.

JSON files are parsed and inlined into the bundle as a JavaScript object.

TOML files are parsed and inlined into the bundle as a JavaScript object.

The contents of the text file are read and in

*[Content truncated - see full docs]*

**Examples**:

```typescript
await Bun.build({
  entrypoints: ['./index.tsx'],
  outdir: './build',
});
```

```typescript
bun build ./index.tsx --outdir ./build
```

```python
import * as ReactDOM from 'react-dom/client';
import {Component} from "./Component"

const root = ReactDOM.createRoot(document.getElementById('root')!);
root.render(<Component message="Sup!" />)
```

---

## Installation

**URL**: https://bun.sh/docs/installation

**Contents**:
- Installing
  - macOS and Linux
  - Windows
- Docker
- Checking installation
  - How to add your PATH
- Upgrading
- Canary builds

Bun ships as a single executable with no dependencies that can be installed a few different ways.

Linux users — The unzip package is required to install Bun. Use sudo apt install unzip to install unzip package. Kernel version 5.6 or higher is strongly recommended, but the minimum is 5.1. Use uname -r to check Kernel version.

To install, paste this into a terminal:

Bun requires a minimum of Windows 10 version 1809

For support and discussion, please join the #windows channel on our Discord.

Bun provides a Docker image that supports both Linux x64 and arm64.

There are also image variants for different operating systems.

To check that Bun was installed successfully, open a new terminal window and run bun --version.

To see the precise commit of oven-sh/bun that you're using, run bun --revision.

If you've installed Bun but are seeing a command not found error, you may have to manually add the installation directory (~/.bun/bin) to your PATH.

First, determine what shell you're using:

Then add these lines below to bottom of your shell's configuration file.

Save the file. You'll need to open a new shell/terminal window for the changes to take effect.

First, determine if the bun binary is properly installed on your system:

If the command runs successfully but bun --version is not recognized, it means that bun is not in your system's PATH. To fix this, open a Powershell terminal and run the following command:

After running the command, restart your terminal and test with bun --version

Once installed, the binary can upgrade itself.

Homebrew users — To avoid conflicts with Homebrew, use brew upgrade bun instead.

Scoop users — To avoid conflicts with Scoop, use scoop update bun instead.

Bun automatically releases an (untested) canary build on every commit to main. To upgrade to the latest canary build:

The canary build is useful for testing new features and bug fixes before they're released in a stable build. To help the Bun team fix bugs faster, canary builds

*[Content truncated - see full docs]*

**Examples**:

```text
curl -fsSL https://bun.com/install | bash # for macOS, Linux, and WSL
```

```text
# to install a specific version
```

```text
curl -fsSL https://bun.com/install | bash -s "bun-v1.3.0"
```

---

## Quickstart

**URL**: https://bun.sh/docs/quickstart

**Contents**:
- Run a file
- Run a script
- Install a package

Let's write a simple HTTP server using the built-in Bun.serve API. First, create a fresh directory.

Run bun init to scaffold a new project. It's an interactive tool; for this tutorial, just press enter to accept the default answer for each prompt.

Since our entry point is a *.ts file, Bun generates a tsconfig.json for you. If you're using plain JavaScript, it will generate a jsconfig.json instead.

Open index.ts and paste the following code snippet, which implements a simple HTTP server with Bun.serve.

Seeing TypeScript errors on Bun?

If you used bun init, Bun will have automatically installed Bun's TypeScript declarations and configured your tsconfig.json. If you're trying out Bun in an existing project, you may see a type error on the Bun global.

To fix this, first install @types/bun as a dev dependency.

Then add the following to your compilerOptions in tsconfig.json:

Run the file from your shell.

Visit http://localhost:3000 to test the server. You should see a simple page that says "Bun!".

Bun can also execute "scripts" from your package.json. Add the following script:

Then run it with bun run start.

⚡️ Performance — bun run is roughly 28x faster than npm run (6ms vs 170ms of overhead).

Let's make our server a little more interesting by installing a package. First install the figlet package and its type declarations. Figlet is a utility for converting strings into ASCII art.

Update index.ts to use figlet in the fetch handler.

Restart the server and refresh the page. You should see a new ASCII art banner.

**Examples**:

```text
mkdir quickstart
```

```text
cd quickstart
```

```text
? Select a project template - Press return to submit.
❯ Blank
  React
  Library

✓ Select a project template: Blank

+ .gitignore
+ index.ts
+ tsconfig.json (for editor autocomplete)
+ README.md

To get started, run:

    bun run index.ts

bun install v1.3.0

+ @types/bun@1.3.0
+ typescript@5.9.2

7 packages installed
```

---

## What is Bun?

**URL**: https://bun.sh/docs/

**Contents**:
- What is a runtime?
  - Browsers
  - Node.js
- Design goals

Bun is an all-in-one toolkit for JavaScript and TypeScript apps. It ships as a single executable called bun.

At its core is the Bun runtime, a fast JavaScript runtime designed as a drop-in replacement for Node.js. It's written in Zig and powered by JavaScriptCore under the hood, dramatically reducing startup times and memory usage.

The bun command-line tool also implements a test runner, script runner, and Node.js-compatible package manager, all significantly faster than existing tools and usable in existing Node.js projects with little to no changes necessary.

Get started with one of the quick links below, or read on to learn more about Bun.

Use a project template

Bundle code for production

Build a Websocket server

JavaScript (or, more formally, ECMAScript) is just a specification for a programming language. Anyone can write a JavaScript engine that ingests a valid JavaScript program and executes it. The two most popular engines in use today are V8 (developed by Google) and JavaScriptCore (developed by Apple). Both are open source.

But most JavaScript programs don't run in a vacuum. They need a way to access the outside world to perform useful tasks. This is where runtimes come in. They implement additional APIs that are then made available to the JavaScript programs they execute.

Notably, browsers ship with JavaScript runtimes that implement a set of Web-specific APIs that are exposed via the global window object. Any JavaScript code executed by the browser can use these APIs to implement interactive or dynamic behavior in the context of the current webpage.

Similarly, Node.js is a JavaScript runtime that can be used in non-browser environments, like servers. JavaScript programs executed by Node.js have access to a set of Node.js-specific globals like Buffer, process, and __dirname in addition to built-in modules for performing OS-level tasks like reading/writing files (node:fs) and networking (node:net, node:http). Node.js also implements a CommonJS-bas

*[Content truncated - see full docs]*

**Examples**:

```typescript
bun run index.tsx  # TS and JSX supported out of the box
```

```text
bun run start                 # run the `start` script
```

```text
bun install <pkg>             # install a package
```

---
