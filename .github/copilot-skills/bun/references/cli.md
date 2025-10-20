# Bun - Cli

**Pages**: 3

---

## Testing

**URL**: https://bun.sh/docs/cli/test

**Contents**:
- Run tests
- CI/CD integration
  - GitHub Actions
    - How to install bun in a GitHub Actions workflow
  - JUnit XML reports (GitLab, etc.)
- Timeouts
- Concurrent test execution
  - --concurrent flag

Bun ships with a fast, built-in, Jest-compatible test runner. Tests are executed with the Bun runtime, and support the following features.

Bun aims for compatibility with Jest, but not everything is implemented. To track compatibility, see this tracking issue.

Tests are written in JavaScript or TypeScript with a Jest-like API. Refer to Writing tests for full documentation.

The runner recursively searches the working directory for files that match the following patterns:

You can filter the set of test files to run by passing additional positional arguments to bun test. Any test file with a path that matches one of the filters will run. Commonly, these filters will be file or directory names; glob patterns are not yet supported.

To filter by test name, use the -t/--test-name-pattern flag.

When no tests match the filter, bun test exits with code 1.

To run a specific file in the test runner, make sure the path starts with ./ or / to distinguish it from a filter name.

The test runner runs all tests in a single process. It loads all --preload scripts (see Lifecycle for details), then runs all tests. If a test fails, the test runner will exit with a non-zero exit code.

bun test supports a variety of CI/CD integrations.

bun test automatically detects if it's running inside GitHub Actions and will emit GitHub Actions annotations to the console directly.

No configuration is needed, other than installing bun in the workflow and running bun test.

To use bun test in a GitHub Actions workflow, add the following step:

From there, you'll get GitHub Actions annotations.

To use bun test with a JUnit XML reporter, you can use the --reporter=junit in combination with --reporter-outfile.

This will continue to output to stdout/stderr as usual, and also write a JUnit XML report to the given path at the very end of the test run.

JUnit XML is a popular format for reporting test results in CI/CD pipelines.

Use the --timeout flag to specify a per-test timeout in milliseconds.

*[Content truncated - see full docs]*

**Examples**:

```python
import { expect, test } from "bun:test";

test("2 + 2", () => {
  expect(2 + 2).toBe(4);
});
```

```text
bun test <filter> <filter> ...
```

```text
# run all tests or test suites with "addition" in the name
```

---

## bun create

**URL**: https://bun.sh/docs/cli/bun-create

**Contents**:
- From a React component
    - How this works
  - Using TailwindCSS with Bun
  - Using shadcn/ui with Bun
- From npm
- From GitHub
- From a local template
    - Setup logic

Note — You don’t need bun create to use Bun. You don’t need any configuration at all. This command exists to make getting started a bit quicker and easier.

Template a new Bun project with bun create. This is a flexible command that can be used to create a new project from a React component, a create-<template> npm package, a GitHub repo, or a local template.

If you're looking to create a brand new empty project, use bun init.

bun create ./MyComponent.tsx turns an existing React component into a complete dev environment with hot reload and production builds in one command.

🚀 Create React App Successor — bun create <component> provides everything developers loved about Create React App, but with modern tooling, faster builds, and backend support.

When you run bun create <component>, Bun:

TailwindCSS is an extremely popular utility-first CSS framework used to style web applications.

When you run bun create <component>, Bun scans your JSX/TSX file for TailwindCSS class names (and any files it imports). If it detects TailwindCSS class names, it will add the following dependencies to your package.json:

We also configure bunfig.toml to use Bun's TailwindCSS plugin with Bun.serve()

And a ${component}.css file with @import "tailwindcss"; at the top:

shadcn/ui is an extremely popular component library tool for building web applications.

bun create <component> scans for any shadcn/ui components imported from @/components/ui.

If it finds any, it runs:

Since shadcn/ui itself uses TailwindCSS, bun create also adds the necessary TailwindCSS dependencies to your package.json and configures bunfig.toml to use Bun's TailwindCSS plugin with Bun.serve() as described above.

Additionally, we setup the following:

bun create ./MyComponent.jsx is one of the easiest ways to run code generated from LLMs like Claude or ChatGPT locally.

Assuming you don't have a local template with the same name, this command will download and execute the create-<template> package from npm. The 

*[Content truncated - see full docs]*

**Examples**:

```typescript
bun create ./MyComponent.jsx # .tsx also supported
```

```text
{
  "dependencies": {
    "tailwindcss": "^4",
    "bun-plugin-tailwind": "latest"
  }
}
```

```text
[serve.static]
plugins = ["bun-plugin-tailwind"]
```

---

## bun install

**URL**: https://bun.sh/docs/cli/install

**Contents**:
- Logging
- Lifecycle scripts
- Workspaces
- Installing dependencies for specific packages
- Overrides and resolutions
- Global packages
- Production mode
- Omitting dependencies

The bun CLI contains a Node.js-compatible package manager designed to be a dramatically faster replacement for npm, yarn, and pnpm. It's a standalone tool that will work in pre-existing Node.js projects; if your project has a package.json, bun install can help you speed up your workflow.

⚡️ 25x faster — Switch from npm install to bun install in any Node.js project to make your installations up to 25x faster.

💾 Disk efficient — Bun install stores all packages in a global cache (~/.bun/install/cache/) and creates hardlinks (Linux) or copy-on-write clones (macOS) to node_modules. This means duplicate packages across projects point to the same underlying data, taking up virtually no extra disk space.

For more details, see Package manager > Global cache.

The recommended minimum Linux Kernel version is 5.6. If you're on Linux kernel 5.1 - 5.5, bun install will work, but HTTP requests will be slow due to a lack of support for io_uring's connect() operation.

If you're using Ubuntu 20.04, here's how to install a newer kernel:

To install all dependencies of a project:

Running bun install will:

To modify logging verbosity:

Unlike other npm clients, Bun does not execute arbitrary lifecycle scripts like postinstall for installed dependencies. Executing arbitrary scripts represents a potential security risk.

To tell Bun to allow lifecycle scripts for a particular package, add the package to trustedDependencies in your package.json.

Then re-install the package. Bun will read this field and run lifecycle scripts for my-trusted-package.

Lifecycle scripts will run in parallel during installation. To adjust the maximum number of concurrent scripts, use the --concurrent-scripts flag. The default is two times the reported cpu count or GOMAXPROCS.

Bun supports "workspaces" in package.json. For complete documentation refer to Package manager > Workspaces.

In a monorepo, you can install the dependencies for a subset of packages using the --filter flag.

For more information o

*[Content truncated - see full docs]*

**Examples**:

```text
# If this returns a version >= 5.6, you don't need to do anything
```

```text
# Install the official Ubuntu hardware enablement kernel
```

```text
sudo apt install --install-recommends linux-generic-hwe-20.04
```

---
