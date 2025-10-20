# Go - Getting

**Pages**: 2

---

## Tutorial: Get started with Go

**URL**: https://go.dev/doc/tutorial/getting-started.html

**Contents**:
- Tutorial: Get started with Go
- Prerequisites
- Install Go
- Write some code
- Call code in an external package
- Write more code

In this tutorial, you'll get a brief introduction to Go programming. Along the way, you will:

Just use the Download and install steps.

Get started with Hello, World.

For example, use the following commands:

When your code imports packages contained in other modules, you manage those dependencies through your code's own module. That module is defined by a go.mod file that tracks the modules that provide those packages. That go.mod file stays with your code, including in your source code repository.

To enable dependency tracking for your code by creating a go.mod file, run the go mod init command, giving it the name of the module your code will be in. The name is the module's module path.

In actual development, the module path will typically be the repository location where your source code will be kept. For example, the module path might be github.com/mymodule. If you plan to publish your module for others to use, the module path must be a location from which Go tools can download your module. For more about naming a module with a module path, see Managing dependencies.

For the purposes of this tutorial, just use example/hello.

In your text editor, create a file hello.go in which to write your code.

Paste the following code into your hello.go file and save the file.

This is your Go code. In this code, you:

Run your code to see the greeting.

The go run command is one of many go commands you'll use to get things done with Go. Use the following command to get a list of the others:

When you need your code to do something that might have been implemented by someone else, you can look for a package that has functions you can use in your code.

You can use the pkg.go.dev site to find published modules whose packages have functions you can use in your own code. Packages are published in modules -- like rsc.io/quote -- where others can use them. Modules are improved with new versions over time, and you can upgrade your code to use the improved versions.

After ad

*[Content truncated - see full docs]*

---

## Tutorial: Get started with Go

**URL**: https://go.dev/doc/tutorial/getting-started

**Contents**:
- Tutorial: Get started with Go
- Prerequisites
- Install Go
- Write some code
- Call code in an external package
- Write more code

In this tutorial, you'll get a brief introduction to Go programming. Along the way, you will:

Just use the Download and install steps.

Get started with Hello, World.

For example, use the following commands:

When your code imports packages contained in other modules, you manage those dependencies through your code's own module. That module is defined by a go.mod file that tracks the modules that provide those packages. That go.mod file stays with your code, including in your source code repository.

To enable dependency tracking for your code by creating a go.mod file, run the go mod init command, giving it the name of the module your code will be in. The name is the module's module path.

In actual development, the module path will typically be the repository location where your source code will be kept. For example, the module path might be github.com/mymodule. If you plan to publish your module for others to use, the module path must be a location from which Go tools can download your module. For more about naming a module with a module path, see Managing dependencies.

For the purposes of this tutorial, just use example/hello.

In your text editor, create a file hello.go in which to write your code.

Paste the following code into your hello.go file and save the file.

This is your Go code. In this code, you:

Run your code to see the greeting.

The go run command is one of many go commands you'll use to get things done with Go. Use the following command to get a list of the others:

When you need your code to do something that might have been implemented by someone else, you can look for a package that has functions you can use in your code.

You can use the pkg.go.dev site to find published modules whose packages have functions you can use in your own code. Packages are published in modules -- like rsc.io/quote -- where others can use them. Modules are improved with new versions over time, and you can upgrade your code to use the improved versions.

After ad

*[Content truncated - see full docs]*

---
