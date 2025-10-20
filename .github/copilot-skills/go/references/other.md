# Go - Other

**Pages**: 96

---

## A Guide to the Go Garbage Collector

**URL**: https://go.dev/doc/gc-guide

**Contents**:
- A Guide to the Go Garbage Collector
- Introduction
  - Where Go Values Live
  - Tracing Garbage Collection
- The GC cycle
  - Understanding costs
  - GOGC
  - Memory limit

This guide is intended to aid advanced Go users in better understanding their application costs by providing insights into the Go garbage collector. It also provides guidance on how Go users may use these insights to improve their applications' resource utilization. It does not assume any knowledge of garbage collection, but does assume familiarity with the Go programming language.

The Go language takes responsibility for arranging the storage of Go values; in most cases, a Go developer need not care about where these values are stored, or why, if at all. In practice, however, these values often need to be stored in computer physical memory and physical memory is a finite resource. Because it is finite, memory must be managed carefully and recycled in order to avoid running out of it while executing a Go program. It's the job of a Go implementation to allocate and recycle memory as needed.

Another term for automatically recycling memory is garbage collection. At a high level, a garbage collector (or GC, for short) is a system that recycles memory on behalf of the application by identifying which parts of memory are no longer needed. The Go standard toolchain provides a runtime library that ships with every application, and this runtime library includes a garbage collector.

Note that the existence of a garbage collector as described by this guide is not guaranteed by the Go specification, only that the underlying storage for Go values is managed by the language itself. This omission is intentional and enables the use of radically different memory management techniques.

Therefore, this guide is about a specific implementation of the Go programming language and may not apply to other implementations. Specifically, this following guide applies to the standard toolchain (the gc Go compiler and tools). Gccgo and Gollvm both use a very similar GC implementation so many of the same concepts apply, but details may vary.

Furthermore, this is a living document and will ch

*[Content truncated - see full docs]*

---

## A Quick Guide to Go's Assembler

**URL**: https://go.dev/doc/asm

**Contents**:
- A Quick Guide to Go's Assembler
- A Quick Guide to Go's Assembler
  - Constants
  - Symbols
  - Directives
  - Special instructions
  - Interacting with Go types and constants
  - Runtime Coordination

This document is a quick outline of the unusual form of assembly language used by the gc Go compiler. The document is not comprehensive.

The assembler is based on the input style of the Plan 9 assemblers, which is documented in detail elsewhere. If you plan to write assembly language, you should read that document although much of it is Plan 9-specific. The current document provides a summary of the syntax and the differences with what is explained in that document, and describes the peculiarities that apply when writing assembly code to interact with Go.

The most important thing to know about Go's assembler is that it is not a direct representation of the underlying machine. Some of the details map precisely to the machine, but some do not. This is because the compiler suite (see this description) needs no assembler pass in the usual pipeline. Instead, the compiler operates on a kind of semi-abstract instruction set, and instruction selection occurs partly after code generation. The assembler works on the semi-abstract form, so when you see an instruction like MOV what the toolchain actually generates for that operation might not be a move instruction at all, perhaps a clear or load. Or it might correspond exactly to the machine instruction with that name. In general, machine-specific operations tend to appear as themselves, while more general concepts like memory move and subroutine call and return are more abstract. The details vary with architecture, and we apologize for the imprecision; the situation is not well-defined.

The assembler program is a way to parse a description of that semi-abstract instruction set and turn it into instructions to be input to the linker. If you want to see what the instructions look like in assembly for a given architecture, say amd64, there are many examples in the sources of the standard library, in packages such as runtime and math/big. You can also examine what the compiler emits as assembly code (the actual output may diffe

*[Content truncated - see full docs]*

---

## About the go command

**URL**: https://go.dev/doc/articles/go_command.html

**Contents**:
- About the go command
- Motivation
- Configuration versus convention
- Go's conventions
- Getting started with the go command
- Limitations
- More information

The Go distribution includes a command, named "go", that automates the downloading, building, installation, and testing of Go packages and commands. This document talks about why we wrote a new command, what it is, what it's not, and how to use it.

You might have seen early Go talks in which Rob Pike jokes that the idea for Go arose while waiting for a large Google server to compile. That really was the motivation for Go: to build a language that worked well for building the large software that Google writes and runs. It was clear from the start that such a language must provide a way to express dependencies between code libraries clearly, hence the package grouping and the explicit import blocks. It was also clear from the start that you might want arbitrary syntax for describing the code being imported; this is why import paths are string literals.

An explicit goal for Go from the beginning was to be able to build Go code using only the information found in the source itself, not needing to write a makefile or one of the many modern replacements for makefiles. If Go needed a configuration file to explain how to build your program, then Go would have failed.

At first, there was no Go compiler, and the initial development focused on building one and then building libraries for it. For expedience, we postponed the automation of building Go code by using make and writing makefiles. When compiling a single package involved multiple invocations of the Go compiler, we even used a program to write the makefiles for us. You can find it if you dig through the repository history.

The purpose of the new go command is our return to this ideal, that Go programs should compile without configuration or additional effort on the part of the developer beyond writing the necessary import statements.

The way to achieve the simplicity of a configuration-free system is to establish conventions. The system works only to the extent that those conventions are followed. When we first l

*[Content truncated - see full docs]*

---

## Accessing relational databases

**URL**: https://go.dev/doc/database/index

**Contents**:
- Accessing relational databases
  - Supported database management systems
  - Functions to execute queries or make database changes
  - Transactions
  - Query cancellation
  - Managed connection pool

Using Go, you can incorporate a wide variety of databases and data access approaches into your applications. Topics in this section describe how to use the standard library’s database/sql package to access relational databases.

For an introductory tutorial to data access with Go, please see Tutorial: Accessing a relational database.

Go supports other data access technologies as well, including ORM libraries for higher-level access to relational databases, and also non-relational NoSQL data stores.

Go supports all of the most common relational database management systems, including MySQL, Oracle, Postgres, SQL Server, SQLite, and more.

You’ll find a complete list of drivers at the SQLDrivers page.

The database/sql package includes functions specifically designed for the kind of database operation you’re executing. For example, while you can use Query or QueryRow to execute queries, QueryRow is designed for the case when you’re expecting only a single row, omitting the overhead of returning an sql.Rows that includes only one row. You can use the Exec function to make database changes with SQL statements such as INSERT, UPDATE, or DELETE.

For more, see the following:

Through sql.Tx, you can write code to execute database operations in a transaction. In a transaction, multiple operations can be performed together and conclude with a final commit, to apply all the changes in one atomic step, or a rollback, to discard them.

For more about transactions, see Executing transactions.

You can use context.Context when you want the ability to cancel a database operation, such as when the client’s connection closes or the operation runs longer than you want it to.

For any database operation, you can use a database/sql package function that takes Context as an argument. Using the Context, you can specify a timeout or deadline for the operation. You can also use the Context to propagate a cancellation request through your application to the function executing an SQL state

*[Content truncated - see full docs]*

---

## Add a test

**URL**: https://go.dev/doc/tutorial/add-a-test.html

**Contents**:
- Add a test

Now that you've gotten your code to a stable place (nicely done, by the way), add a test. Testing your code during development can expose bugs that find their way in as you make changes. In this topic, you add a test for the Hello function.

Go's built-in support for unit testing makes it easier to test as you go. Specifically, using naming conventions, Go's testing package, and the go test command, you can quickly write and execute tests.

Ending a file's name with _test.go tells the go test command that this file contains test functions.

The go test command executes test functions (whose names begin with Test) in test files (whose names end with _test.go). You can add the -v flag to get verbose output that lists all of the tests and their results.

The tests should pass.

The TestHelloName test function checks the return value for the name you specified as a Hello function parameter. To view a failing test result, change the greetings.Hello function so that it no longer includes the name.

In greetings/greetings.go, paste the following code in place of the Hello function. Note that the highlighted lines change the value that the function returns, as if the name argument had been accidentally removed.

This time, run go test without the -v flag. The output will include results for only the tests that failed, which can be useful when you have a lot of tests. The TestHelloName test should fail -- TestHelloEmpty still passes.

In the next (and last) topic, you'll see how to compile and install your code to run it locally.

< Return greetings for multiple people Compile and install the application >

---

## Avoiding SQL injection risk

**URL**: https://go.dev/doc/database/sql-injection

**Contents**:
- Avoiding SQL injection risk

You can avoid an SQL injection risk by providing SQL parameter values as sql package function arguments. Many functions in the sql package provide parameters for the SQL statement and for values to be used in that statement’s parameters (others provide a parameter for a prepared statement and parameters).

Code in the following example uses the ? symbol as a placeholder for the id parameter, which is provided as a function argument:

sql package functions that perform database operations create prepared statements from the arguments you supply. At run time, the sql package turns the SQL statement into a prepared statement and sends it along with the parameter, which is separate.

Note: Parameter placeholders vary depending on the DBMS and driver you’re using. For example, pq driver for Postgres accepts a placeholder form such as $1 instead of ?.

You might be tempted to use a function from the fmt package to assemble the SQL statement as a string with parameters included – like this:

This is not secure! When you do this, Go assembles the entire SQL statement, replacing the %s format verb with the parameter value, before sending the full statement to the DBMS. This poses an SQL injection risk because the code’s caller could send an unexpected SQL snippet as the id argument. That snippet could complete the SQL statement in unpredictable ways that are dangerous to your application.

For example, by passing a certain %s value, you might end up with something like the following, which could return all user records in your database:

**Examples**:

```text
// Correct format for executing an SQL statement with parameters.
rows, err := db.Query("SELECT * FROM user WHERE id = ?", id)
```

```text
// SECURITY RISK!
rows, err := db.Query(fmt.Sprintf("SELECT * FROM user WHERE id = %s", id))
```

```text
SELECT * FROM user WHERE id = 1 OR 1=1;
```

---

## Call your code from another module

**URL**: https://go.dev/doc/tutorial/call-module-code.html

**Contents**:
- Call your code from another module

In the previous section, you created a greetings module. In this section, you'll write code to make calls to the Hello function in the module you just wrote. You'll write code you can execute as an application, and which calls code in the greetings module.

After you create this directory, you should have both a hello and a greetings directory at the same level in the hierarchy, like so:

For example, if your command prompt is in the greetings directory, you could use the following commands:

To enable dependency tracking for your code, run the go mod init command, giving it the name of the module your code will be in.

For the purposes of this tutorial, use example.com/hello for the module path.

To do that, paste the following code into hello.go.

For production use, you’d publish the example.com/greetings module from its repository (with a module path that reflected its published location), where Go tools could find it to download it. For now, because you haven't published the module yet, you need to adapt the example.com/hello module so it can find the example.com/greetings code on your local file system.

To do that, use the go mod edit command to edit the example.com/hello module to redirect Go tools from its module path (where the module isn't) to the local directory (where it is).

The command specifies that example.com/greetings should be replaced with ../greetings for the purpose of locating the dependency. After you run the command, the go.mod file in the hello directory should include a replace directive:

After the command completes, the example.com/hello module's go.mod file should look like this:

The command found the local code in the greetings directory, then added a require directive to specify that example.com/hello requires example.com/greetings. You created this dependency when you imported the greetings package in hello.go.

The number following the module path is a pseudo-version number -- a generated number used in place of a semantic versio

*[Content truncated - see full docs]*

---

## Canceling in-progress operations

**URL**: https://go.dev/doc/database/cancel-operations

**Contents**:
- Canceling in-progress operations
  - Canceling database operations after a timeout

You can manage in-progress operations by using Go context.Context. A Context is a standard Go data value that can report whether the overall operation it represents has been canceled and is no longer needed. By passing a context.Context across function calls and services in your application, those can stop working early and return an error when their processing is no longer needed. For more about Context, see Go Concurrency Patterns: Context.

For example, you might want to:

Many APIs for Go developers include methods that take a Context argument, making it easier for you to use Context throughout your application.

You can use a Context to set a timeout or deadline after which an operation will be canceled. To derive a Context with a timeout or deadline, call context.WithTimeout or context.WithDeadline.

Code in the following timeout example derives a Context and passes it into the sql.DB QueryContext method.

When one context is derived from an outer context, as queryCtx is derived from ctx in this example, if the outer context is canceled, then the derived context is automatically canceled as well. For example, in HTTP servers, the http.Request.Context method returns a context associated with the request. That context is canceled if the HTTP client disconnects or cancels the HTTP request (possible in HTTP/2). Passing an HTTP request’s context to QueryWithTimeout above would cause the database query to stop early either if the overall HTTP request was canceled or if the query took more than five seconds.

Note: Always defer a call to the cancel function that’s returned when you create a new Context with a timeout or deadline. This releases resources held by the new Context when the containing function exits. It also cancels queryCtx, but by the time the function returns, nothing should be using queryCtx anymore.

**Examples**:

```text
func QueryWithTimeout(ctx context.Context) {
    // Create a Context with a timeout.
    queryCtx, cancel := context.WithTimeout(ctx, 5*time.Second)
    defer cancel()

    // Pass the timeout Context with a query.
    rows, err := db.QueryContext(queryCtx, "SELECT * FROM album")
    if err != nil {
        log.Fatal(err)
    }
    defer rows.Close()

    // Handle returned rows.
}
```

---

## Codewalk: First-Class Functions in Go

**URL**: https://go.dev/doc/codewalk/functions

**Contents**:
- Codewalk: First-Class Functions in Go

---

## Codewalk: Generating arbitrary text: a Markov chain algorithm

**URL**: https://go.dev/doc/codewalk/markov

**Contents**:
- Codewalk: Generating arbitrary text: a Markov chain algorithm

---

## Codewalk: Share Memory By Communicating

**URL**: https://go.dev/doc/codewalk/sharemem

**Contents**:
- Codewalk: Share Memory By Communicating

---

## Codewalk: Share Memory By Communicating

**URL**: https://go.dev/doc/codewalk/sharemem/

**Contents**:
- Codewalk: Share Memory By Communicating

---

## Command Documentation

**URL**: https://go.dev/doc/cmd

**Contents**:
- Command Documentation

There is a suite of programs to build and process Go source code. Instead of being run directly, programs in the suite are usually invoked by the go program.

The most common way to run these programs is as a subcommand of the go program, for instance as go fmt. Run like this, the command operates on complete packages of Go source code, with the go program invoking the underlying binary with arguments appropriate to package-level processing.

The programs can also be run as stand-alone binaries, with unmodified arguments, using the go tool subcommand, such as go tool cgo. For most commands this is mainly useful for debugging. Some of the commands, such as pprof, are accessible only through the go tool subcommand.

The Go installation process also installs an executable called gofmt, equivalent to go fmt, because it is so often referenced.

Click on the links for more documentation, invocation methods, and usage details.

This is an abridged list. See the full command reference for documentation of the compilers and more.

---

## Compile and install the application

**URL**: https://go.dev/doc/tutorial/compile-install.html

**Contents**:
- Compile and install the application

In this last topic, you'll learn a couple new go commands. While the go run command is a useful shortcut for compiling and running a program when you're making frequent changes, it doesn't generate a binary executable.

This topic introduces two additional commands for building code:

Note that your result might differ depending on whether you changed your greetings.go code after testing it.

You've compiled the application into an executable so you can run it. But to run it currently, your prompt needs either to be in the executable's directory, or to specify the executable's path.

Next, you'll install the executable so you can run it without specifying its path.

You can discover the install path by running the go list command, as in the following example:

For example, the command's output might say /home/gopher/bin/hello, meaning that binaries are installed to /home/gopher/bin. You'll need this install directory in the next step.

That way, you'll be able to run your program's executable without specifying where the executable is.

As an alternative, if you already have a directory like $HOME/bin in your shell path and you'd like to install your Go programs there, you can change the install target by setting the GOBIN variable using the go env command:

That wraps up this Go tutorial!

< Add a test Conclusion and links to more information >

---

## Contributing to the gccgo frontend

**URL**: https://go.dev/doc/gccgo_contribute.html

**Contents**:
- Contributing to the gccgo frontend
- Introduction
- Legal Prerequisites
- Code
- Testing
- Submitting Changes

These are some notes on contributing to the gccgo frontend for GCC. For information on contributing to parts of Go other than gccgo, see Contributing to the Go project. For information on building gccgo for yourself, see Setting up and using gccgo. For more of the gritty details on the process of doing development with the gccgo frontend, see the file HACKING in the gofrontend repository.

You must follow the Go copyright rules for all changes to the gccgo frontend and the associated libgo library. Code that is part of GCC rather than gccgo must follow the general GCC contribution rules.

The master sources for the gccgo frontend may be found at https://go.googlesource.com/gofrontend. They are mirrored at https://github.com/golang/gofrontend. The master sources are not buildable by themselves, but only in conjunction with GCC (in the future, other compilers may be supported). Changes made to the gccgo frontend are also applied to the GCC source code repository hosted at gcc.gnu.org. In the gofrontend repository, the go directory is mirrored to the gcc/go/gofrontend directory in the GCC repository, and the gofrontend libgo directory is mirrored to the GCC libgo directory. In addition, the test directory from the main Go repository is mirrored to the gcc/testsuite/go.test/test directory in the GCC repository.

Changes to these directories always flow from the master sources to the GCC repository. The files should never be changed in the GCC repository except by changing them in the master sources and mirroring them.

The gccgo frontend is written in C++. It follows the GNU and GCC coding standards for C++. In writing code for the frontend, follow the formatting of the surrounding code. Almost all GCC-specific code is not in the frontend proper and is instead in the GCC sources in the gcc/go directory.

The run-time library for gccgo is mostly the same as the library in the main Go repository. The library code in the Go repository is periodically merged into the libgo/

*[Content truncated - see full docs]*

---

## Contribution Guide

**URL**: https://go.dev/doc/contribute

**Contents**:
- Contribution Guide
- Becoming a contributor
  - Overview
  - Step 0: Select a Google Account
  - Step 1: Contributor License Agreement
  - Step 2: Configure git authentication
  - Step 3: Create a Gerrit account
  - Step 4: Install the git-codereview command

The Go project welcomes all contributors.

This document is a guide to help you through the process of contributing to the Go project, which is a little different from that used by other open source projects. We assume you have a basic understanding of Git and Go.

In addition to the information here, the Go community maintains a CodeReview wiki page. Feel free to contribute to the wiki as you learn the review process.

Note that the gccgo front end lives elsewhere; see Contributing to gccgo.

The first step is registering as a Go contributor and configuring your environment. Here is a checklist of the required steps to follow:

If you prefer, there is an automated tool that walks through these steps. Just run:

The rest of this chapter elaborates on these instructions. If you have completed the steps above (either manually or through the tool), jump to Before contributing code.

A contribution to Go is made through a Google account with a specific e-mail address. Make sure to use the same account throughout the process and for all your subsequent contributions. You may need to decide whether to use a personal address or a corporate address. The choice will depend on who will own the copyright for the code that you will be writing and submitting. You might want to discuss this topic with your employer before deciding which account to use.

Google accounts can either be Gmail e-mail accounts, G Suite organization accounts, or accounts associated with an external e-mail address. For instance, if you need to use an existing corporate e-mail that is not managed through G Suite, you can create an account associated with your existing e-mail address.

You also need to make sure that your Git tool is configured to create commits using your chosen e-mail address. You can either configure Git globally (as a default for all projects), or locally (for a single specific project). You can check the current configuration with this command:

To change the configured address:

Befo

*[Content truncated - see full docs]*

---

## Contribution Guide

**URL**: https://go.dev/doc/contribute.html

**Contents**:
- Contribution Guide
- Becoming a contributor
  - Overview
  - Step 0: Select a Google Account
  - Step 1: Contributor License Agreement
  - Step 2: Configure git authentication
  - Step 3: Create a Gerrit account
  - Step 4: Install the git-codereview command

The Go project welcomes all contributors.

This document is a guide to help you through the process of contributing to the Go project, which is a little different from that used by other open source projects. We assume you have a basic understanding of Git and Go.

In addition to the information here, the Go community maintains a CodeReview wiki page. Feel free to contribute to the wiki as you learn the review process.

Note that the gccgo front end lives elsewhere; see Contributing to gccgo.

The first step is registering as a Go contributor and configuring your environment. Here is a checklist of the required steps to follow:

If you prefer, there is an automated tool that walks through these steps. Just run:

The rest of this chapter elaborates on these instructions. If you have completed the steps above (either manually or through the tool), jump to Before contributing code.

A contribution to Go is made through a Google account with a specific e-mail address. Make sure to use the same account throughout the process and for all your subsequent contributions. You may need to decide whether to use a personal address or a corporate address. The choice will depend on who will own the copyright for the code that you will be writing and submitting. You might want to discuss this topic with your employer before deciding which account to use.

Google accounts can either be Gmail e-mail accounts, G Suite organization accounts, or accounts associated with an external e-mail address. For instance, if you need to use an existing corporate e-mail that is not managed through G Suite, you can create an account associated with your existing e-mail address.

You also need to make sure that your Git tool is configured to create commits using your chosen e-mail address. You can either configure Git globally (as a default for all projects), or locally (for a single specific project). You can check the current configuration with this command:

To change the configured address:

Befo

*[Content truncated - see full docs]*

---

## Coverage profiling support for integration tests

**URL**: https://go.dev/doc/build-cover

**Contents**:
- Coverage profiling support for integration tests
- Overview
- Building a binary for coverage profiling
- How packages are selected for instrumentation
- Running a coverage-instrumented binary
- Tests involving multiple runs
- Working with coverage data files
- Creating coverage profile reports

Overview Building a binary for coverage profiling Running a coverage-instrumented binary Working with coverage data files Frequently Asked Questions Resources Glossary

Beginning in Go 1.20, Go supports collection of coverage profiles from applications and from integration tests, larger and more complex tests for Go programs.

Go provides easy-to-use support for collecting coverage profiles at the level of package unit tests via the “go test -coverprofile=... <pkg_target>” command. Starting with Go 1.20, users can now collect coverage profiles for larger integration tests: more heavy-weight, complex tests that perform multiple runs of a given application binary.

For unit tests, collecting a coverage profile and generating a report requires two steps: a go test -coverprofile=... run, followed by an invocation of go tool cover {-func,-html} to generate a report.

For integration tests, three steps are needed: a build step, a run step (which may involve multiple invocations of the binary from the build step), and finally a reporting step, as described below.

To build an application for collecting coverage profiles, pass the -cover flag when invoking go build on your application binary target. See the section below for a sample go build -cover invocation. The resulting binary can then be run using an environment variable setting to capture coverage profiles (see the next section on running).

During a given “go build -cover” invocation, the Go command will select packages in the main module for coverage profiling; other packages that feed into the build (dependencies listed in go.mod, or packages that are part of the Go standard library) will not be included by default.

For example, here is a toy program containing a main package, a local main-module package greetings and a set of packages imported from outside the module, including (among others) rsc.io/quote and fmt (link to full program).

If you build this program with the “-cover” command line flag and run it, e

*[Content truncated - see full docs]*

**Examples**:

```text
$ cat go.mod
module mydomain.com

go 1.20

require rsc.io/quote v1.5.2

require (
    golang.org/x/text v0.0.0-20170915032832-14c0d48ead0c // indirect
    rsc.io/sampler v1.3.0 // indirect
)

$ cat myprogram.go
package main

import (
    "fmt"
    "mydomain.com/greetings"
    "rsc.io/quote"
)

func main() {
    fmt.Printf("I say %q and %q\n", quote.Hello(), greetings.Goodbye())
}
$ cat greetings/greetings.go
package greetings

func Goodbye() string {
    return "see ya"
}
$ go build -cover -o my
...
```

```text
$ go build -cover -o myprogramMorePkgs.exe -coverpkg=io,mydomain.com,rsc.io/quote .
$
```

```text
$ go build -cover -o myprogram.exe myprogram.go
$ mkdir somedata
$ GOCOVERDIR=somedata ./myprogram.exe
I say "Hello, world." and "see ya"
$ ls somedata
covcounters.c6de772f99010ef5925877a7b05db4cc.2424989.1670252383678349347
covmeta.c6de772f99010ef5925877a7b05db4cc
$
```

---

## Data Race Detector

**URL**: https://go.dev/doc/articles/race_detector.html

**Contents**:
- Data Race Detector
- Introduction
- Usage
- Report Format
- Options
- Excluding Tests
- How To Use
- Typical Data Races

Data races are among the most common and hardest to debug types of bugs in concurrent systems. A data race occurs when two goroutines access the same variable concurrently and at least one of the accesses is a write. See the The Go Memory Model for details.

Here is an example of a data race that can lead to crashes and memory corruption:

To help diagnose such bugs, Go includes a built-in data race detector. To use it, add the -race flag to the go command:

When the race detector finds a data race in the program, it prints a report. The report contains stack traces for conflicting accesses, as well as stacks where the involved goroutines were created. Here is an example:

The GORACE environment variable sets race detector options. The format is:

When you build with -race flag, the go command defines additional build tag race. You can use the tag to exclude some code and tests when running the race detector. Some examples:

To start, run your tests using the race detector (go test -race). The race detector only finds races that happen at runtime, so it can't find races in code paths that are not executed. If your tests have incomplete coverage, you may find more races by running a binary built with -race under a realistic workload.

Here are some typical data races. All of them can be detected with the race detector.

The variable i in the function literal is the same variable used by the loop, so the read in the goroutine races with the loop increment. (This program typically prints 55555, not 01234.) The program can be fixed by making a copy of the variable:

The fix is to introduce new variables in the goroutines (note the use of :=):

If the following code is called from several goroutines, it leads to races on the service map. Concurrent reads and writes of the same map are not safe:

To make the code safe, protect the accesses with a mutex:

Data races can happen on variables of primitive types as well (bool, int, int64, etc.), as in this example:

Even such 

*[Content truncated - see full docs]*

---

## Debugging Go Code with GDB

**URL**: https://go.dev/doc/gdb

**Contents**:
- Debugging Go Code with GDB
- Introduction
  - Common Operations
  - Go Extensions
  - Known Issues
- Tutorial
  - Getting Started
  - Inspecting the source

The following instructions apply to the standard toolchain (the gc Go compiler and tools). Gccgo has native gdb support.

Note that Delve is a better alternative to GDB when debugging Go programs built with the standard toolchain. It understands the Go runtime, data structures, and expressions better than GDB. Delve currently supports Linux, OSX, and Windows on amd64. For the most up-to-date list of supported platforms, please see the Delve documentation.

GDB does not understand Go programs well. The stack management, threading, and runtime contain aspects that differ enough from the execution model GDB expects that they can confuse the debugger and cause incorrect results even when the program is compiled with gccgo. As a consequence, although GDB can be useful in some situations (e.g., debugging Cgo code, or debugging the runtime itself), it is not a reliable debugger for Go programs, particularly heavily concurrent ones. Moreover, it is not a priority for the Go project to address these issues, which are difficult.

In short, the instructions below should be taken only as a guide to how to use GDB when it works, not as a guarantee of success. Besides this overview you might want to consult the GDB manual.

When you compile and link your Go programs with the gc toolchain on Linux, macOS, FreeBSD or NetBSD, the resulting binaries contain DWARFv4 debugging information that recent versions (≥7.5) of the GDB debugger can use to inspect a live process or a core dump.

Pass the '-w' flag to the linker to omit the debug information (for example, go build -ldflags=-w prog.go).

The code generated by the gc compiler includes inlining of function invocations and registerization of variables. These optimizations can sometimes make debugging with gdb harder. If you find that you need to disable these optimizations, build your program using go build -gcflags=all="-N -l".

If you want to use gdb to inspect a core dump, you can trigger a dump on a program crash, on systems that

*[Content truncated - see full docs]*

---

## Developing a major version update

**URL**: https://go.dev/doc/modules/major-version

**Contents**:
- Developing a major version update
- Considerations for a major version update
- Branching for a major release

You must update to a major version when changes you’re making in a potential new version can’t guarantee backward compatibility for the module’s users. For example, you’ll make this change if you change your module’s public API such that it breaks client code using previous versions of the module.

Note: Each release type – major, minor, patch, or pre-release – has a different meaning for a module’s users. Those users rely on these differences to understand the level of risk a release represents to their own code. In other words, when preparing a release, be sure that its version number accurately reflects the nature of the changes since the preceding release. For more on version numbers, see Module version numbering.

You should only update to a new major version when it’s absolutely necessary. A major version update represents significant churn for both you and your module’s users. When you’re considering a major version update, think about the following:

Be clear with your users about what releasing the new major version means for your support of previous major versions.

Are previous versions deprecated? Supported as they were before? Will you be maintaining previous versions, including with bug fixes?

Be ready to take on the maintenance of two versions: the old and the new. For example, if you fix bugs in one, you’ll often be porting those fixes into the other.

Remember that a new major version is a new module from a dependency management perspective. Your users will need to update to use a new module after you release, rather than simply upgrading.

That’s because a new major version has a different module path from the preceding major version. For example, for a module whose module path is example.com/mymodule, a v2 version would have the module path example.com/mymodule/v2.

When you’re developing a new major version, you must also update import paths wherever code imports packages from the new module. Your module’s users must also update their import pat

*[Content truncated - see full docs]*

**Examples**:

```text
$ cd mymodule
$ git checkout -b v2
Switched to a new branch "v2"
```

---

## Developing and publishing modules

**URL**: https://go.dev/doc/modules/developing

**Contents**:
- Developing and publishing modules
- Workflow for developing and publishing modules
- Design and development
- Decentralized publishing
- Package discovery
- Versioning

You can collect related packages into modules, then publish the modules for other developers to use. This topic gives an overview of developing and publishing modules.

To support developing, publishing, and using modules, you use:

When you want to publish your modules for others, you adopt a few conventions to make using those modules easier.

The following high-level steps are described in more detail in Module release and versioning workflow.

Your module will be easier for developers to find and use if the functions and packages in it form a coherent whole. When you’re designing a module’s public API, try to keep its functionality focused and discrete.

Also, designing and developing your module with backward compatibility in mind helps its users upgrade while minimizing churn to their own code. You can use certain techniques in code to avoid releasing a version that breaks backward compatibility. For more about those techniques, see Keeping your modules compatible on the Go blog.

Before you publish a module, you can reference it on the local file system using the replace directive. This makes it easier to write client code that calls functions in the module while the module is still in development. For more information, see “Coding against an unpublished module” in Module release and versioning workflow.

In Go, you publish your module by tagging its code in your repository to make it available for other developers to use. You don’t need to push your module to a centralized service because Go tools can download your module directly from your repository (located using the module’s path, which is a URL with the scheme omitted) or from a proxy server.

After importing your package in their code, developers use Go tools (including the go get command) to download your module’s code to compile with. To support this model, you follow conventions and best practices that make it possible for Go tools (on behalf of another developer) to retrieve your module’s source fr

*[Content truncated - see full docs]*

---

## Diagnostics

**URL**: https://go.dev/doc/diagnostics.html

**Contents**:
- Diagnostics
- Introduction
- Profiling
- Tracing
- Debugging
- Runtime statistics and events
  - Execution tracer
  - GODEBUG

The Go ecosystem provides a large suite of APIs and tools to diagnose logic and performance problems in Go programs. This page summarizes the available tools and helps Go users pick the right one for their specific problem.

Diagnostics solutions can be categorized into the following groups:

Note: Some diagnostics tools may interfere with each other. For example, precise memory profiling skews CPU profiles and goroutine blocking profiling affects scheduler trace. Use tools in isolation to get more precise info.

Profiling is useful for identifying expensive or frequently called sections of code. The Go runtime provides profiling data in the format expected by the pprof visualization tool. The profiling data can be collected during testing via go test or endpoints made available from the net/http/pprof package. Users need to collect the profiling data and use pprof tools to filter and visualize the top code paths.

Predefined profiles provided by the runtime/pprof package:

What other profilers can I use to profile Go programs?

On Linux, perf tools can be used for profiling Go programs. Perf can profile and unwind cgo/SWIG code and kernel, so it can be useful to get insights into native/kernel performance bottlenecks. On macOS, Instruments suite can be used profile Go programs.

Can I profile my production services?

Yes. It is safe to profile programs in production, but enabling some profiles (e.g. the CPU profile) adds cost. You should expect to see performance downgrade. The performance penalty can be estimated by measuring the overhead of the profiler before turning it on in production.

You may want to periodically profile your production services. Especially in a system with many replicas of a single process, selecting a random replica periodically is a safe option. Select a production process, profile it for X seconds for every Y seconds and save the results for visualization and analysis; then repeat periodically. Results may be manually and/or automaticall

*[Content truncated - see full docs]*

---

## Diagnostics

**URL**: https://go.dev/doc/diagnostics

**Contents**:
- Diagnostics
- Introduction
- Profiling
- Tracing
- Debugging
- Runtime statistics and events
  - Execution tracer
  - GODEBUG

The Go ecosystem provides a large suite of APIs and tools to diagnose logic and performance problems in Go programs. This page summarizes the available tools and helps Go users pick the right one for their specific problem.

Diagnostics solutions can be categorized into the following groups:

Note: Some diagnostics tools may interfere with each other. For example, precise memory profiling skews CPU profiles and goroutine blocking profiling affects scheduler trace. Use tools in isolation to get more precise info.

Profiling is useful for identifying expensive or frequently called sections of code. The Go runtime provides profiling data in the format expected by the pprof visualization tool. The profiling data can be collected during testing via go test or endpoints made available from the net/http/pprof package. Users need to collect the profiling data and use pprof tools to filter and visualize the top code paths.

Predefined profiles provided by the runtime/pprof package:

What other profilers can I use to profile Go programs?

On Linux, perf tools can be used for profiling Go programs. Perf can profile and unwind cgo/SWIG code and kernel, so it can be useful to get insights into native/kernel performance bottlenecks. On macOS, Instruments suite can be used profile Go programs.

Can I profile my production services?

Yes. It is safe to profile programs in production, but enabling some profiles (e.g. the CPU profile) adds cost. You should expect to see performance downgrade. The performance penalty can be estimated by measuring the overhead of the profiler before turning it on in production.

You may want to periodically profile your production services. Especially in a system with many replicas of a single process, selecting a random replica periodically is a safe option. Select a production process, profile it for X seconds for every Y seconds and save the results for visualization and analysis; then repeat periodically. Results may be manually and/or automaticall

*[Content truncated - see full docs]*

---

## Documentation

**URL**: https://go.dev/doc/

**Contents**:
- Documentation
- Getting Started
  - Installing Go
  - Tutorial: Getting started
  - Tutorial: Create a module
  - Tutorial: Getting started with multi-module workspaces
  - Tutorial: Developing a RESTful API with Go and Gin
  - Tutorial: Getting started with generics

The Go programming language is an open source project to make programmers more productive.

Go is expressive, concise, clean, and efficient. Its concurrency mechanisms make it easy to write programs that get the most out of multicore and networked machines, while its novel type system enables flexible and modular program construction. Go compiles quickly to machine code yet has the convenience of garbage collection and the power of run-time reflection. It's a fast, statically typed, compiled language that feels like a dynamically typed, interpreted language.

Instructions for downloading and installing Go.

A brief Hello, World tutorial to get started. Learn a bit about Go code, tools, packages, and modules.

A tutorial of short topics introducing functions, error handling, arrays, maps, unit testing, and compiling.

Introduces the basics of creating and using multi-module workspaces in Go. Multi-module workspaces are useful for making changes across multiple modules.

Introduces the basics of writing a RESTful web service API with Go and the Gin Web Framework.

With generics, you can declare and use functions or types that are written to work with any of a set of types provided by calling code.

Fuzzing can generate inputs to your tests that can catch edge cases and security issues that you may have missed.

Building a simple web application.

This doc explains how to develop a simple set of Go packages inside a module, and it shows how to use the go command to build and test packages.

An interactive introduction to Go in four sections. The first section covers basic syntax and data structures; the second discusses methods and interfaces; the third is about Generics; and the fourth introduces Go's concurrency primitives. Each section concludes with a few exercises so you can practice what you've learned. You can take the tour online or install it locally with:

This will place the tour binary in your GOPATH's bin directory.

A document that gives tips for writing 

*[Content truncated - see full docs]*

---

## Download and install

**URL**: https://go.dev/doc/install

**Contents**:
- Download and install
- Go installation
- You're all set!
    - Report Issues

Download and install Go quickly with the steps described here.

For other content on installing, you might be interested in:

Select the tab for your computer's operating system below, then follow its installation instructions.

(You may need to run each command separately with the necessary permissions, as root or through sudo.)

Do not untar the archive into an existing /usr/local/go tree. This is known to produce broken Go installations.

You can do this by adding the following line to your $HOME/.profile or /etc/profile (for a system-wide installation):

Note: Changes made to a profile file may not apply until the next time you log into your computer. To apply the changes immediately, just run the shell commands directly or execute them from the profile using a command such as source $HOME/.profile.

The package installs the Go distribution to /usr/local/go. The package should put the /usr/local/go/bin directory in your PATH environment variable. You may need to restart any open Terminal sessions for the change to take effect.

By default, the installer will install Go to Program Files or Program Files (x86). You can change the location as needed. After installing, you will need to close and reopen any open command prompts so that changes to the environment made by the installer are reflected at the command prompt.

Visit the Getting Started tutorial to write some simple Go code. It takes about 10 minutes to complete.

If you spot bugs, mistakes, or inconsistencies in the Go project's code or documentation, please let us know by filing a ticket on our issue tracker. Of course, you should check it's not an existing issue before creating a new one.

---

## Editor plugins and IDEs

**URL**: https://go.dev/doc/editors.html

**Contents**:
- Editor plugins and IDEs
- Introduction
- Options

This document lists commonly used editor plugins and IDEs from the Go ecosystem that make Go development more productive and seamless. A comprehensive list of editor support and IDEs for Go development is available at the wiki.

The Go ecosystem provides a variety of editor plugins and IDEs to enhance your day-to-day editing, navigation, testing, and debugging experience.

Note that these are only a few top solutions; a more comprehensive community-maintained list of IDEs and text editor plugins is available at the Wiki.

---

## Editor plugins and IDEs

**URL**: https://go.dev/doc/editors

**Contents**:
- Editor plugins and IDEs
- Introduction
- Options

This document lists commonly used editor plugins and IDEs from the Go ecosystem that make Go development more productive and seamless. A comprehensive list of editor support and IDEs for Go development is available at the wiki.

The Go ecosystem provides a variety of editor plugins and IDEs to enhance your day-to-day editing, navigation, testing, and debugging experience.

Note that these are only a few top solutions; a more comprehensive community-maintained list of IDEs and text editor plugins is available at the Wiki.

---

## Executing SQL statements that don't return data

**URL**: https://go.dev/doc/database/change-data

**Contents**:
- Executing SQL statements that don't return data
    - Functions for executing SQL statements that don’t return rows

When you perform database actions that don’t return data, use an Exec or ExecContext method from the database/sql package. SQL statements you’d execute this way include INSERT, DELETE, and UPDATE.

When your query might return rows, use a Query or QueryContext method instead. For more, see Querying a database.

An ExecContext method works as an Exec method does, but with an additional context.Context argument, as described in Canceling in-progress operations.

Code in the following example uses DB.Exec to execute a statement to add a new record album to an album table.

DB.Exec returns values: an sql.Result and an error. When the error is nil, you can use the Result to get the ID of the last inserted item (as in the example) or to retrieve the number of rows affected by the operation.

Note: Parameter placeholders in prepared statements vary depending on the DBMS and driver you’re using. For example, the pq driver for Postgres requires a placeholder like $1 instead of ?.

If your code will be executing the same SQL statement repeatedly, consider using an sql.Stmt to create a reusable prepared statement from the SQL statement. For more, see Using prepared statements.

Caution: Don’t use string formatting functions such as fmt.Sprintf to assemble an SQL statement! You could introduce an SQL injection risk. For more, see Avoiding SQL injection risk.

**Examples**:

```text
func AddAlbum(alb Album) (int64, error) {
    result, err := db.Exec("INSERT INTO album (title, artist) VALUES (?, ?)", alb.Title, alb.Artist)
    if err != nil {
        return 0, fmt.Errorf("AddAlbum: %v", err)
    }

    // Get the new album's generated ID for the client.
    id, err := result.LastInsertId()
    if err != nil {
        return 0, fmt.Errorf("AddAlbum: %v", err)
    }
    // Return the new album's ID.
    return id, nil
}
```

---

## Executing transactions

**URL**: https://go.dev/doc/database/execute-transactions

**Contents**:
- Executing transactions
  - Best practices
  - Example

You can execute database transactions using an sql.Tx, which represents a transaction. In addition to Commit and Rollback methods representing transaction-specific semantics, sql.Tx has all of the methods you use to perform common database operations. To get the sql.Tx, you call DB.Begin or DB.BeginTx.

A database transaction groups multiple operations as part of a larger goal. All of the operations must succeed or none can, with the data’s integrity preserved in either case. Typically, a transaction workflow includes:

The sql package provides methods for beginning and concluding a transaction, as well as methods for performing the intervening database operations. These methods correspond to the four steps in the workflow above.

DB.Begin or DB.BeginTx begin a new database transaction, returning an sql.Tx that represents it.

Perform database operations.

Using an sql.Tx, you can query or update the database in a series of operations that use a single connection. To support this, Tx exports the following methods:

Exec and ExecContext for making database changes through SQL statements such as INSERT, UPDATE, and DELETE.

For more, see Executing SQL statements that don’t return data.

Query, QueryContext, QueryRow, and QueryRowContext for operations that return rows.

For more, see Querying for data.

Prepare, PrepareContext, Stmt, and StmtContext for pre-defining prepared statements.

For more, see Using prepared statements.

End the transaction with one of the following:

Commit the transaction using Tx.Commit.

If Commit succeeds (returns a nil error), then all the query results are confirmed as valid and all the executed updates are applied to the database as a single atomic change. If Commit fails, then all the results from Query and Exec on the Tx should be discarded as invalid.

Roll back the transaction using Tx.Rollback.

Even if Tx.Rollback fails, the transaction will no longer be valid, nor will it have been committed to the database.

Follow the best pra

*[Content truncated - see full docs]*

**Examples**:

```javascript
// CreateOrder creates an order for an album and returns the new order ID.
func CreateOrder(ctx context.Context, albumID, quantity, custID int) (orderID int64, err error) {

    // Create a helper function for preparing failure results.
    fail := func(err error) (int64, error) {
        return 0, fmt.Errorf("CreateOrder: %v", err)
    }

    // Get a Tx for making transaction requests.
    tx, err := db.BeginTx(ctx, nil)
    if err != nil {
        return fail(err)
    }
    // Defer a rollbac
...
```

---

## Frequently Asked Questions (FAQ)

**URL**: https://go.dev/doc/faq

**Contents**:
- Frequently Asked Questions (FAQ)
- Origins
  - What is the purpose of the project?
  - What is the history of the project?
  - What’s the origin of the gopher mascot?
  - Is the language called Go or Golang?
  - Why did you create a new language?
  - What are Go’s ancestors?

At the time of Go’s inception in 2007 the programming world was different from today. Production software was usually written in C++ or Java, GitHub did not exist, most computers were not yet multiprocessors, and other than Visual Studio and Eclipse there were few IDEs or other high-level tools available at all, let alone for free on the Internet.

Meanwhile, we had become frustrated by the undue complexity required to build large software projects with the languages we were using and their associated build systems. Computers had become enormously quicker since languages such as C, C++ and Java were first developed but the act of programming had not itself advanced nearly as much. Also, it was clear that multiprocessors were becoming universal but most languages offered little help to program them efficiently and safely.

We decided to take a step back and think about what major issues were going to dominate software engineering in the years ahead as technology developed, and how a new language might help address them. For instance, the rise of multicore CPUs argued that a language should provide first-class support for some sort of concurrency or parallelism. And to make resource management tractable in a large concurrent program, garbage collection, or at least some sort of safe automatic memory management was required.

These considerations led to a series of discussions from which Go arose, first as a set of ideas and desiderata, then as a language. An overarching goal was that Go do more to help the working programmer by enabling tooling, automating mundane tasks such as code formatting, and removing obstacles to working on large code bases.

A much more expansive description of the goals of Go and how they are met, or at least approached, is available in the article, Go at Google: Language Design in the Service of Software Engineering.

Robert Griesemer, Rob Pike and Ken Thompson started sketching the goals for a new language on the white board on September 21

*[Content truncated - see full docs]*

**Examples**:

```text
type T struct{}
var _ I = T{}       // Verify that T implements I.
var _ I = (*T)(nil) // Verify that *T implements I.
```

```text
type Fooer interface {
    Foo()
    ImplementsFooer()
}
```

```text
type Bar struct{}
func (b Bar) ImplementsFooer() {}
func (b Bar) Foo() {}
```

---

## Go 1.11 Release Notes

**URL**: https://go.dev/doc/go1.11

**Contents**:
- Go 1.11 Release Notes
- Introduction to Go 1.11
- Changes to the language
- Ports
  - WebAssembly
  - RISC-V GOARCH values reserved
- Tools
  - Modules, package versioning, and dependency management

The latest Go release, version 1.11, arrives six months after Go 1.10. Most of its changes are in the implementation of the toolchain, runtime, and libraries. As always, the release maintains the Go 1 promise of compatibility. We expect almost all Go programs to continue to compile and run as before.

There are no changes to the language specification.

As announced in the Go 1.10 release notes, Go 1.11 now requires OpenBSD 6.2 or later, macOS 10.10 Yosemite or later, or Windows 7 or later; support for previous versions of these operating systems has been removed.

Go 1.11 supports the upcoming OpenBSD 6.4 release. Due to changes in the OpenBSD kernel, older versions of Go will not work on OpenBSD 6.4.

There are known issues with NetBSD on i386 hardware.

The race detector is now supported on linux/ppc64le and, to a lesser extent, on netbsd/amd64. The NetBSD race detector support has known issues.

The memory sanitizer (-msan) is now supported on linux/arm64.

The build modes c-shared and c-archive are now supported on freebsd/amd64.

On 64-bit MIPS systems, the new environment variable settings GOMIPS64=hardfloat (the default) and GOMIPS64=softfloat select whether to use hardware instructions or software emulation for floating-point computations. For 32-bit systems, the environment variable is still GOMIPS, as added in Go 1.10.

On soft-float ARM systems (GOARM=5), Go now uses a more efficient software floating point interface. This is transparent to Go code, but ARM assembly that uses floating-point instructions not guarded on GOARM will break and must be ported to the new interface.

Go 1.11 on ARMv7 no longer requires a Linux kernel configured with KUSER_HELPERS. This setting is enabled in default kernel configurations, but is sometimes disabled in stripped-down configurations.

Go 1.11 adds an experimental port to WebAssembly (js/wasm).

Go programs currently compile to one WebAssembly module that includes the Go runtime for goroutine scheduling, garbage colle

*[Content truncated - see full docs]*

**Examples**:

```text
func f(v interface{}) {
    switch x := v.(type) {
    }
}
```

```text
func wrapper(s string, args ...interface{}) {
    fmt.Printf(s, args...)
}

func main() {
    wrapper("%s", 42)
}
```

```text
for k := range m {
    delete(m, k)
}
```

---

## Go 1.12 Release Notes

**URL**: https://go.dev/doc/go1.12

**Contents**:
- Go 1.12 Release Notes
- Introduction to Go 1.12
- Changes to the language
- Ports
  - Windows
  - AIX
  - Darwin
- Tools

The latest Go release, version 1.12, arrives six months after Go 1.11. Most of its changes are in the implementation of the toolchain, runtime, and libraries. As always, the release maintains the Go 1 promise of compatibility. We expect almost all Go programs to continue to compile and run as before.

There are no changes to the language specification.

The race detector is now supported on linux/arm64.

Go 1.12 is the last release that is supported on FreeBSD 10.x, which has already reached end-of-life. Go 1.13 will require FreeBSD 11.2+ or FreeBSD 12.0+. FreeBSD 12.0+ requires a kernel with the COMPAT_FREEBSD11 option set (this is the default).

cgo is now supported on linux/ppc64.

hurd is now a recognized value for GOOS, reserved for the GNU/Hurd system for use with gccgo.

Go’s new windows/arm port supports running Go on Windows 10 IoT Core on 32-bit ARM chips such as the Raspberry Pi 3.

Go now supports AIX 7.2 and later on POWER8 architectures (aix/ppc64). External linking, cgo, pprof and the race detector aren’t yet supported.

Go 1.12 is the last release that will run on macOS 10.10 Yosemite. Go 1.13 will require macOS 10.11 El Capitan or later.

libSystem is now used when making syscalls on Darwin, ensuring forward-compatibility with future versions of macOS and iOS. The switch to libSystem triggered additional App Store checks for private API usage. Since it is considered private, syscall.Getdirentries now always fails with ENOSYS on iOS. Additionally, syscall.Setrlimit reports invalid argument in places where it historically succeeded. These consequences are not specific to Go and users should expect behavioral parity with libSystem’s implementation going forward.

The go vet command has been rewritten to serve as the base for a range of different source code analysis tools. See the golang.org/x/tools/go/analysis package for details. A side-effect is that go tool vet is no longer supported. External tools that use go tool vet must be changed to use go ve

*[Content truncated - see full docs]*

**Examples**:

```text
go get -u golang.org/x/tools/go/analysis/passes/shadow/cmd/shadow
go vet -vettool=$(which shadow)
```

```text
go get -u golang.org/x/tour
tour
```

```text
// Old code which no longer works correctly (it will miss inlined call frames).
var pcs [10]uintptr
n := runtime.Callers(1, pcs[:])
for _, pc := range pcs[:n] {
    f := runtime.FuncForPC(pc)
    if f != nil {
        fmt.Println(f.Name())
    }
}
```

---

## Go 1.13 Release Notes

**URL**: https://go.dev/doc/go1.13

**Contents**:
- Go 1.13 Release Notes
- Introduction to Go 1.13
- Changes to the language
- Ports
  - AIX
  - Android
  - Darwin
  - FreeBSD

The latest Go release, version 1.13, arrives six months after Go 1.12. Most of its changes are in the implementation of the toolchain, runtime, and libraries. As always, the release maintains the Go 1 promise of compatibility. We expect almost all Go programs to continue to compile and run as before.

As of Go 1.13, the go command by default downloads and authenticates modules using the Go module mirror and Go checksum database run by Google. See https://proxy.golang.org/privacy for privacy information about these services and the go command documentation for configuration details including how to disable the use of these servers or use different ones. If you depend on non-public modules, see the documentation for configuring your environment.

Per the number literal proposal, Go 1.13 supports a more uniform and modernized set of number literal prefixes.

Per the signed shift counts proposal Go 1.13 removes the restriction that a shift count must be unsigned. This change eliminates the need for many artificial uint conversions, solely introduced to satisfy this (now removed) restriction of the << and >> operators.

These language changes were implemented by changes to the compiler, and corresponding internal changes to the library packages go/scanner and text/scanner (number literals), and go/types (signed shift counts).

If your code uses modules and your go.mod files specifies a language version, be sure it is set to at least 1.13 to get access to these language changes. You can do this by editing the go.mod file directly, or you can run go mod edit -go=1.13.

Go 1.13 is the last release that will run on Native Client (NaCl).

For GOARCH=wasm, the new environment variable GOWASM takes a comma-separated list of experimental features that the binary gets compiled with. The valid values are documented here.

AIX on PPC64 (aix/ppc64) now supports cgo, external linking, and the c-archive and pie build modes.

Go programs are now compatible with Android 10.

As announce

*[Content truncated - see full docs]*

**Examples**:

```text
go env -w GOPROXY=direct
go env -w GOSUMDB=off
```

```text
require github.com/docker/docker v1.14.0-0.20190319215453-e7b5f7dbe98c
```

```text
require github.com/docker/docker e7b5f7dbe98c
```

---

## Go 1.14 Release Notes

**URL**: https://go.dev/doc/go1.14

**Contents**:
- Go 1.14 Release Notes
- Introduction to Go 1.14
- Changes to the language
- Ports
  - Darwin
  - Windows
  - WebAssembly
  - RISC-V

The latest Go release, version 1.14, arrives six months after Go 1.13. Most of its changes are in the implementation of the toolchain, runtime, and libraries. As always, the release maintains the Go 1 promise of compatibility. We expect almost all Go programs to continue to compile and run as before.

Module support in the go command is now ready for production use, and we encourage all users to migrate to Go modules for dependency management. If you are unable to migrate due to a problem in the Go toolchain, please ensure that the problem has an open issue filed. (If the issue is not on the Go1.15 milestone, please let us know why it prevents you from migrating so that we can prioritize it appropriately.)

Per the overlapping interfaces proposal, Go 1.14 now permits embedding of interfaces with overlapping method sets: methods from an embedded interface may have the same names and identical signatures as methods already present in the (embedding) interface. This solves problems that typically (but not exclusively) occur with diamond-shaped embedding graphs. Explicitly declared methods in an interface must remain unique, as before.

Go 1.14 is the last release that will run on macOS 10.11 El Capitan. Go 1.15 will require macOS 10.12 Sierra or later.

Go 1.14 is the last Go release to support 32-bit binaries on macOS (the darwin/386 port). They are no longer supported by macOS, starting with macOS 10.15 (Catalina). Go continues to support the 64-bit darwin/amd64 port.

Go 1.14 will likely be the last Go release to support 32-bit binaries on iOS, iPadOS, watchOS, and tvOS (the darwin/arm port). Go continues to support the 64-bit darwin/arm64 port.

Go binaries on Windows now have DEP (Data Execution Prevention) enabled.

On Windows, creating a file via os.OpenFile with the os.O_CREATE flag, or via syscall.Open with the syscall.O_CREAT flag, will now create the file as read-only if the bit 0o200 (owner write permission) is not set in the permission argument. This makes

*[Content truncated - see full docs]*

---

## Go 1.15 Release Notes

**URL**: https://go.dev/doc/go1.15

**Contents**:
- Go 1.15 Release Notes
- Introduction to Go 1.15
- Changes to the language
- Ports
  - Darwin
  - Windows
  - Android
  - OpenBSD

The latest Go release, version 1.15, arrives six months after Go 1.14. Most of its changes are in the implementation of the toolchain, runtime, and libraries. As always, the release maintains the Go 1 promise of compatibility. We expect almost all Go programs to continue to compile and run as before.

Go 1.15 includes substantial improvements to the linker, improves allocation for small objects at high core counts, and deprecates X.509 CommonName. GOPROXY now supports skipping proxies that return errors and a new embedded tzdata package has been added.

There are no changes to the language.

As announced in the Go 1.14 release notes, Go 1.15 requires macOS 10.12 Sierra or later; support for previous versions has been discontinued.

As announced in the Go 1.14 release notes, Go 1.15 drops support for 32-bit binaries on macOS, iOS, iPadOS, watchOS, and tvOS (the darwin/386 and darwin/arm ports). Go continues to support the 64-bit darwin/amd64 and darwin/arm64 ports.

Go now generates Windows ASLR executables when -buildmode=pie cmd/link flag is provided. Go command uses -buildmode=pie by default on Windows.

The -race and -msan flags now always enable -d=checkptr, which checks uses of unsafe.Pointer. This was previously the case on all OSes except Windows.

Go-built DLLs no longer cause the process to exit when it receives a signal (such as Ctrl-C at a terminal).

When linking binaries for Android, Go 1.15 explicitly selects the lld linker available in recent versions of the NDK. The lld linker avoids crashes on some devices, and is planned to become the default NDK linker in a future NDK version.

Go 1.15 adds support for OpenBSD 6.7 on GOARCH=arm and GOARCH=arm64. Previous versions of Go already supported OpenBSD 6.7 on GOARCH=386 and GOARCH=amd64.

There has been progress in improving the stability and performance of the 64-bit RISC-V port on Linux (GOOS=linux, GOARCH=riscv64). It also now supports asynchronous preemption.

Go 1.15 is the last release to support x8

*[Content truncated - see full docs]*

---

## Go 1.16 Release Notes

**URL**: https://go.dev/doc/go1.16

**Contents**:
- Go 1.16 Release Notes
- Introduction to Go 1.16
- Changes to the language
- Ports
  - Darwin and iOS
  - NetBSD
  - OpenBSD
  - 386

The latest Go release, version 1.16, arrives six months after Go 1.15. Most of its changes are in the implementation of the toolchain, runtime, and libraries. As always, the release maintains the Go 1 promise of compatibility. We expect almost all Go programs to continue to compile and run as before.

There are no changes to the language.

Go 1.16 adds support of 64-bit ARM architecture on macOS (also known as Apple Silicon) with GOOS=darwin, GOARCH=arm64. Like the darwin/amd64 port, the darwin/arm64 port supports cgo, internal and external linking, c-archive, c-shared, and pie build modes, and the race detector.

The iOS port, which was previously darwin/arm64, has been renamed to ios/arm64. GOOS=ios implies the darwin build tag, just as GOOS=android implies the linux build tag. This change should be transparent to anyone using gomobile to build iOS apps.

The introduction of GOOS=ios means that file names like x_ios.go will now only be built for GOOS=ios; see go help buildconstraint for details. Existing packages that use file names of this form will have to rename the files.

Go 1.16 adds an ios/amd64 port, which targets the iOS simulator running on AMD64-based macOS. Previously this was unofficially supported through darwin/amd64 with the ios build tag set. See also misc/ios/README for details about how to build programs for iOS and iOS simulator.

Go 1.16 is the last release that will run on macOS 10.12 Sierra. Go 1.17 will require macOS 10.13 High Sierra or later.

Go now supports the 64-bit ARM architecture on NetBSD (the netbsd/arm64 port).

Go now supports the MIPS64 architecture on OpenBSD (the openbsd/mips64 port). This port does not yet support cgo.

On the 64-bit x86 and 64-bit ARM architectures on OpenBSD (the openbsd/amd64 and openbsd/arm64 ports), system calls are now made through libc, instead of directly using the SYSCALL/SVC instruction. This ensures forward-compatibility with future versions of OpenBSD. In particular, OpenBSD 6.9 onwards will req

*[Content truncated - see full docs]*

**Examples**:

```text
func TestFoo(t *testing.T) {
    go func() {
        if condition() {
            t.Fatal("oops") // This exits the inner func instead of TestFoo.
        }
        ...
    }()
}
```

```text
func TestFoo(t *testing.T) {
    go func() {
        if condition() {
            t.Error("oops")
            return
        }
        ...
    }()
}
```

---

## Go 1.17 Release Notes

**URL**: https://go.dev/doc/go1.17

**Contents**:
- Go 1.17 Release Notes
- Introduction to Go 1.17
- Changes to the language
- Ports
  - Darwin
  - Windows
  - OpenBSD
  - ARM64

The latest Go release, version 1.17, arrives six months after Go 1.16. Most of its changes are in the implementation of the toolchain, runtime, and libraries. As always, the release maintains the Go 1 promise of compatibility. We expect almost all Go programs to continue to compile and run as before.

Go 1.17 includes three small enhancements to the language.

The package unsafe enhancements were added to simplify writing code that conforms to unsafe.Pointer’s safety rules, but the rules remain unchanged. In particular, existing programs that correctly use unsafe.Pointer remain valid, and new programs must still follow the rules when using unsafe.Add or unsafe.Slice.

Note that the new conversion from slice to array pointer is the first case in which a type conversion can panic at run time. Analysis tools that assume type conversions can never panic should be updated to consider this possibility.

As announced in the Go 1.16 release notes, Go 1.17 requires macOS 10.13 High Sierra or later; support for previous versions has been discontinued.

Go 1.17 adds support of 64-bit ARM architecture on Windows (the windows/arm64 port). This port supports cgo.

The 64-bit MIPS architecture on OpenBSD (the openbsd/mips64 port) now supports cgo.

In Go 1.16, on the 64-bit x86 and 64-bit ARM architectures on OpenBSD (the openbsd/amd64 and openbsd/arm64 ports) system calls are made through libc, instead of directly using machine instructions. In Go 1.17, this is also done on the 32-bit x86 and 32-bit ARM architectures on OpenBSD (the openbsd/386 and openbsd/arm ports). This ensures compatibility with OpenBSD 6.9 onwards, which require system calls to be made through libc for non-static Go binaries.

Go programs now maintain stack frame pointers on the 64-bit ARM architecture on all operating systems. Previously, stack frame pointers were only enabled on Linux, macOS, and iOS.

The main Go compiler does not yet support the LoongArch architecture, but we’ve reserved the GOARCH value

*[Content truncated - see full docs]*

**Examples**:

```text
go mod tidy -go=1.17
```

```text
go mod tidy -compat=1.17
```

```text
c := make(chan os.Signal)
// signals are sent on c before the channel is read from.
// This signal may be dropped as c is unbuffered.
signal.Notify(c, os.Interrupt)
```

---

## Go 1.18 Release Notes

**URL**: https://go.dev/doc/go1.18

**Contents**:
- Go 1.18 Release Notes
- Introduction to Go 1.18
- Changes to the language
  - Generics
    - golang.org/x/exp/constraints
    - golang.org/x/exp/slices
    - golang.org/x/exp/maps
  - Bug fixes

The latest Go release, version 1.18, is a significant release, including changes to the language, implementation of the toolchain, runtime, and libraries. Go 1.18 arrives seven months after Go 1.17. As always, the release maintains the Go 1 promise of compatibility. We expect almost all Go programs to continue to compile and run as before.

Go 1.18 includes an implementation of generic features as described by the Type Parameters Proposal. This includes major - but fully backward-compatible - changes to the language.

These new language changes required a large amount of new code that has not had significant testing in production settings. That will only happen as more people write and use generic code. We believe that this feature is well implemented and high quality. However, unlike most aspects of Go, we can’t back up that belief with real world experience. Therefore, while we encourage the use of generics where it makes sense, please use appropriate caution when deploying generic code in production.

While we believe that the new language features are well designed and clearly specified, it is possible that we have made mistakes. We want to stress that the Go 1 compatibility guarantee says “If it becomes necessary to address an inconsistency or incompleteness in the specification, resolving the issue could affect the meaning or legality of existing programs. We reserve the right to address such issues, including updating the implementations.” It also says “If a compiler or library has a bug that violates the specification, a program that depends on the buggy behavior may break if the bug is fixed. We reserve the right to fix such bugs.” In other words, it is possible that there will be code using generics that will work with the 1.18 release but break in later releases. We do not plan or expect to make any such change. However, breaking 1.18 programs in future releases may become necessary for reasons that we cannot today foresee. We will minimize any such break

*[Content truncated - see full docs]*

**Examples**:

```text
func Print[T ~int|~string](t T) {
    fmt.Printf("%d", t)
}
```

```text
func PrintString(x string) {
    fmt.Printf("%d", x)
}
```

```text
// fmt.Printf formatting directive %d is being passed to Println.
  fmt.Println("%d"+` ≡ x (mod 2)`+"\n", x%2)
```

---

## Go 1.19 Release Notes

**URL**: https://go.dev/doc/go1.19

**Contents**:
- Go 1.19 Release Notes
- Introduction to Go 1.19
- Changes to the language
- Memory Model
- Ports
  - LoongArch 64-bit
  - RISC-V
- Tools

The latest Go release, version 1.19, arrives five months after Go 1.18. Most of its changes are in the implementation of the toolchain, runtime, and libraries. As always, the release maintains the Go 1 promise of compatibility. We expect almost all Go programs to continue to compile and run as before.

There is only one small change to the language, a very small correction to the scope of type parameters in method declarations. Existing programs are unaffected.

The Go memory model has been revised to align Go with the memory model used by C, C++, Java, JavaScript, Rust, and Swift. Go only provides sequentially consistent atomics, not any of the more relaxed forms found in other languages. Along with the memory model update, Go 1.19 introduces new types in the sync/atomic package that make it easier to use atomic values, such as atomic.Int64 and atomic.Pointer[T].

Go 1.19 adds support for the Loongson 64-bit architecture LoongArch on Linux (GOOS=linux, GOARCH=loong64). The implemented ABI is LP64D. Minimum kernel version supported is 5.19.

Note that most existing commercial Linux distributions for LoongArch come with older kernels, with a historical incompatible system call ABI. Compiled binaries will not work on these systems, even if statically linked. Users on such unsupported systems are limited to the distribution-provided Go package.

The riscv64 port now supports passing function arguments and result using registers. Benchmarking shows typical performance improvements of 10% or more on riscv64.

Go 1.19 adds support for links, lists, and clearer headings in doc comments. As part of this change, gofmt now reformats doc comments to make their rendered meaning clearer. See “Go Doc Comments” for syntax details and descriptions of common mistakes now highlighted by gofmt. As another part of this change, the new package go/doc/comment provides parsing and reformatting of doc comments as well as support for rendering them to HTML, Markdown, and text.

The build co

*[Content truncated - see full docs]*

---

## Go 1.20 Release Notes

**URL**: https://go.dev/doc/go1.20

**Contents**:
- Go 1.20 Release Notes
- Introduction to Go 1.20
- Changes to the language
- Ports
  - Windows
  - Darwin and iOS
  - FreeBSD/RISC-V
- Tools

The latest Go release, version 1.20, arrives six months after Go 1.19. Most of its changes are in the implementation of the toolchain, runtime, and libraries. As always, the release maintains the Go 1 promise of compatibility. We expect almost all Go programs to continue to compile and run as before.

Go 1.20 includes four changes to the language.

Go 1.17 added conversions from slice to an array pointer. Go 1.20 extends this to allow conversions from a slice to an array: given a slice x, [4]byte(x) can now be written instead of *(*[4]byte)(x).

The unsafe package defines three new functions SliceData, String, and StringData. Along with Go 1.17’s Slice, these functions now provide the complete ability to construct and deconstruct slice and string values, without depending on their exact representation.

The specification now defines that struct values are compared one field at a time, considering fields in the order they appear in the struct type definition, and stopping at the first mismatch. The specification could previously have been read as if all fields needed to be compared beyond the first mismatch. Similarly, the specification now defines that array values are compared one element at a time, in increasing index order. In both cases, the difference affects whether certain comparisons must panic. Existing programs are unchanged: the new spec wording describes what the implementations have always done.

Comparable types (such as ordinary interfaces) may now satisfy comparable constraints, even if the type arguments are not strictly comparable (comparison may panic at runtime). This makes it possible to instantiate a type parameter constrained by comparable (e.g., a type parameter for a user-defined generic map key) with a non-strictly comparable type argument such as an interface type, or a composite type containing an interface type.

Go 1.20 is the last release that will run on any release of Windows 7, 8, Server 2008 and Server 2012. Go 1.21 will require at

*[Content truncated - see full docs]*

**Examples**:

```text
func RequestHandler(w ResponseWriter, r *Request) {
  rc := http.NewResponseController(w)
  rc.SetWriteDeadline(time.Time{}) // disable Server.WriteTimeout when sending a large response
  io.Copy(w, bigData)
}
```

```text
proxyHandler := &httputil.ReverseProxy{
  Rewrite: func(r *httputil.ProxyRequest) {
    r.SetURL(outboundURL) // Forward request to outboundURL.
    r.SetXForwarded()     // Set X-Forwarded-* headers.
    r.Out.Header.Set("X-Additional-Header", "header set by the proxy")
  },
}
```

---

## Go 1.21 Release Notes

**URL**: https://go.dev/doc/go1.21

**Contents**:
- Go 1.21 Release Notes
- Introduction to Go 1.21
- Changes to the language
- Tools
  - Go command
  - Cgo
- Runtime
- Compiler

The latest Go release, version 1.21, arrives six months after Go 1.20. Most of its changes are in the implementation of the toolchain, runtime, and libraries. As always, the release maintains the Go 1 promise of compatibility; in fact, Go 1.21 improves upon that promise. We expect almost all Go programs to continue to compile and run as before.

Go 1.21 introduces a small change to the numbering of releases. In the past, we used Go 1.N to refer to both the overall Go language version and release family as well as the first release in that family. Starting in Go 1.21, the first release is now Go 1.N.0. Today we are releasing both the Go 1.21 language and its initial implementation, the Go 1.21.0 release. These notes refer to “Go 1.21”; tools like go version will report “go1.21.0” (until you upgrade to Go 1.21.1). See “Go versions” in the “Go Toolchains” documentation for details about the new version numbering.

Go 1.21 adds three new built-ins to the language.

Package initialization order is now specified more precisely. The new algorithm is:

This may change the behavior of some programs that rely on a specific initialization ordering that was not expressed by explicit imports. The behavior of such programs was not well defined by the spec in past releases. The new rule provides an unambiguous definition.

Multiple improvements that increase the power and precision of type inference have been made.

More generally, the description of type inference in the language spec has been clarified. Together, all these changes make type inference more powerful and inference failures less surprising.

Go 1.21 includes a preview of a language change we are considering for a future version of Go: making for loop variables per-iteration instead of per-loop, to avoid accidental sharing bugs. For details about how to try that language change, see the LoopvarExperiment wiki page.

Go 1.21 now defines that if a goroutine is panicking and recover was called directly by a deferred fun

*[Content truncated - see full docs]*

---

## Go 1.22 Release Notes

**URL**: https://go.dev/doc/go1.22

**Contents**:
- Go 1.22 Release Notes
- Introduction to Go 1.22
- Changes to the language
- Tools
  - Go command
  - Trace
  - Vet
    - References to loop variables

The latest Go release, version 1.22, arrives six months after Go 1.21. Most of its changes are in the implementation of the toolchain, runtime, and libraries. As always, the release maintains the Go 1 promise of compatibility. We expect almost all Go programs to continue to compile and run as before.

Go 1.22 makes two changes to “for” loops.

Previously, the variables declared by a “for” loop were created once and updated by each iteration. In Go 1.22, each iteration of the loop creates new variables, to avoid accidental sharing bugs. The transition support tooling described in the proposal continues to work in the same way it did in Go 1.21.

“For” loops may now range over integers. For example:

See the spec for details.

Go 1.22 includes a preview of a language change we are considering for a future version of Go: range-over-function iterators. Building with GOEXPERIMENT=rangefunc enables this feature.

Commands in workspaces can now use a vendor directory containing the dependencies of the workspace. The directory is created by go work vendor, and used by build commands when the -mod flag is set to vendor, which is the default when a workspace vendor directory is present.

Note that the vendor directory’s contents for a workspace are different from those of a single module: if the directory at the root of a workspace also contains one of the modules in the workspace, its vendor directory can contain the dependencies of either the workspace or of the module, but not both.

go get is no longer supported outside of a module in the legacy GOPATH mode (that is, with GO111MODULE=off). Other build commands, such as go build and go test, will continue to work indefinitely for legacy GOPATH programs.

go mod init no longer attempts to import module requirements from configuration files for other vendoring tools (such as Gopkg.lock).

go test -cover now prints coverage summaries for covered packages that do not have their own test files. Prior to Go 1.22 a go test -cover

*[Content truncated - see full docs]*

**Examples**:

```text
package main

import "fmt"

func main() {
  for i := range 10 {
    fmt.Println(10 - i)
  }
  fmt.Println("go1.22 has lift-off!")
}
```

```text
t := time.Now()
defer log.Println(time.Since(t)) // non-deferred call to time.Since
tmp := time.Since(t); defer log.Println(tmp) // equivalent to the previous defer

defer func() {
  log.Println(time.Since(t)) // a correctly deferred call to time.Since
}()
```

---

## Go 1.23 Release Notes

**URL**: https://go.dev/doc/go1.23

**Contents**:
- Go 1.23 Release Notes
- Introduction to Go 1.23
- Changes to the language
- Tools
  - Telemetry
  - Go command
  - Vet
  - Cgo

The latest Go release, version 1.23, arrives six months after Go 1.22. Most of its changes are in the implementation of the toolchain, runtime, and libraries. As always, the release maintains the Go 1 promise of compatibility. We expect almost all Go programs to continue to compile and run as before.

The “range” clause in a “for-range” loop now accepts iterator functions of the following types

as range expressions. Calls of the iterator argument function produce the iteration values for the “for-range” loop. For details see the iter package documentation, the language spec, and the Range over Function Types blog post. For motivation see the 2022 “range-over-func” discussion.

Go 1.23 includes preview support for generic type aliases. Building the toolchain with GOEXPERIMENT=aliastypeparams enables this feature within a package. (Using generic alias types across package boundaries is not yet supported.)

Starting in Go 1.23, the Go toolchain can collect usage and breakage statistics that help the Go team understand how the Go toolchain is used and how well it is working. We refer to these statistics as Go telemetry.

Go telemetry is an opt-in system, controlled by the go telemetry command. By default, the toolchain programs collect statistics in counter files that can be inspected locally but are otherwise unused (go telemetry local).

To help us keep Go working well and understand Go usage, please consider opting in to Go telemetry by running go telemetry on. In that mode, anonymous counter reports are uploaded to telemetry.go.dev weekly, where they are aggregated into graphs and also made available for download by any Go contributors or users wanting to analyze the data. See “Go Telemetry” for more details about the Go Telemetry system.

Setting the GOROOT_FINAL environment variable no longer has an effect (#62047). Distributions that install the go command to a location other than $GOROOT/bin/go should install a symlink instead of relocating or copying the go bi

*[Content truncated - see full docs]*

**Examples**:

```text
func(func() bool)
func(func(K) bool)
func(func(K, V) bool)
```

---

## Go 1.24 Release Notes

**URL**: https://go.dev/doc/go1.24

**Contents**:
- Go 1.24 Release Notes
- Introduction to Go 1.24
- Changes to the language
- Tools
  - Go command
  - Cgo
  - Objdump
  - Vet

The latest Go release, version 1.24, arrives in February 2025, six months after Go 1.23. Most of its changes are in the implementation of the toolchain, runtime, and libraries. As always, the release maintains the Go 1 promise of compatibility. We expect almost all Go programs to continue to compile and run as before.

Go 1.24 now fully supports generic type aliases: a type alias may be parameterized like a defined type. See the language spec for details. For now, the feature can be disabled by setting GOEXPERIMENT=noaliastypeparams; but the aliastypeparams setting will be removed for Go 1.25.

Go modules can now track executable dependencies using tool directives in go.mod. This removes the need for the previous workaround of adding tools as blank imports to a file conventionally named “tools.go”. The go tool command can now run these tools in addition to tools shipped with the Go distribution. For more information see the documentation.

The new -tool flag for go get causes a tool directive to be added to the current module for named packages in addition to adding require directives.

The new tool meta-pattern refers to all tools in the current module. This can be used to upgrade them all with go get tool or to install them into your GOBIN directory with go install tool.

Executables created by go run and the new behavior of go tool are now cached in the Go build cache. This makes repeated executions faster at the expense of making the cache larger. See #69290.

The go build and go install commands now accept a -json flag that reports build output and failures as structured JSON output on standard output. For details of the reporting format, see go help buildjson.

Furthermore, go test -json now reports build output and failures in JSON, interleaved with test result JSON. These are distinguished by new Action types, but if they cause problems in a test integration system, you can revert to the text build output with GODEBUG setting gotestjsonbuildtext=1.

The new 

*[Content truncated - see full docs]*

**Examples**:

```text
params := fn.Type.(*types.Signature).Params()
for i := 0; i < params.Len(); i++ {
   use(params.At(i))
}
```

```text
for param := range fn.Signature().Params().Variables() {
   use(param)
}
```

---

## Go 1.25 Release Notes

**URL**: https://go.dev/doc/go1.25

**Contents**:
- Go 1.25 Release Notes
- Introduction to Go 1.25
- Changes to the language
- Tools
  - Go command
  - Vet
- Runtime
  - Container-aware GOMAXPROCS

The latest Go release, version 1.25, arrives in August 2025, six months after Go 1.24. Most of its changes are in the implementation of the toolchain, runtime, and libraries. As always, the release maintains the Go 1 promise of compatibility. We expect almost all Go programs to continue to compile and run as before.

There are no languages changes that affect Go programs in Go 1.25. However, in the language specification the notion of core types has been removed in favor of dedicated prose. See the respective blog post for more information.

The go build -asan option now defaults to doing leak detection at program exit. This will report an error if memory allocated by C is not freed and is not referenced by any other memory allocated by either C or Go. These new error reports may be disabled by setting ASAN_OPTIONS=detect_leaks=0 in the environment when running the program.

The Go distribution will include fewer prebuilt tool binaries. Core toolchain binaries such as the compiler and linker will still be included, but tools not invoked by build or test operations will be built and run by go tool as needed.

The new go.mod ignore directive can be used to specify directories the go command should ignore. Files in these directories and their subdirectories will be ignored by the go command when matching package patterns, such as all or ./..., but will still be included in module zip files.

The new go doc -http option will start a documentation server showing documentation for the requested object, and open the documentation in a browser window.

The new go version -m -json option will print the JSON encodings of the runtime/debug.BuildInfo structures embedded in the given Go binary files.

The go command now supports using a subdirectory of a repository as the path for a module root, when resolving a module path using the syntax <meta name="go-import" content="root-path vcs repo-url subdir"> to indicate that the root-path corresponds to the subdir of the repo-url wit

*[Content truncated - see full docs]*

**Examples**:

```text
panic: PANIC [recovered]
  panic: PANIC
```

```text
panic: PANIC [recovered, repanicked]
```

```text
package main

import "os"

func main() {
    f, err := os.Open("nonExistentFile")
    name := f.Name()
    if err != nil {
        return
    }
    println(name)
}
```

---

## Go 1 and the Future of Go Programs

**URL**: https://go.dev/doc/go1compat.html

**Contents**:
- Go 1 and the Future of Go Programs
- Introduction
- Expectations
- Sub-repositories
- Operating systems
- Tools

The release of Go version 1, Go 1 for short, is a major milestone in the development of the language. Go 1 is a stable platform for the growth of programs and projects written in Go.

Go 1 defines two things: first, the specification of the language; and second, the specification of a set of core APIs, the "standard packages" of the Go library. The Go 1 release includes their implementation in the form of two compiler suites (gc and gccgo), and the core libraries themselves.

It is intended that programs written to the Go 1 specification will continue to compile and run correctly, unchanged, over the lifetime of that specification. At some indefinite point, a Go 2 specification may arise, but until that time, Go programs that work today should continue to work even as future "point" releases of Go 1 arise (Go 1.1, Go 1.2, etc.).

Compatibility is at the source level. Binary compatibility for compiled packages is not guaranteed between releases. After a point release, Go source will need to be recompiled to link against the new release.

The APIs may grow, acquiring new packages and features, but not in a way that breaks existing Go 1 code.

Although we expect that the vast majority of programs will maintain this compatibility over time, it is impossible to guarantee that no future change will break any program. This document is an attempt to set expectations for the compatibility of Go 1 software in the future. There are a number of ways in which a program that compiles and runs today may fail to do so after a future point release. They are all unlikely but worth recording.

Of course, for all of these possibilities, should they arise, we would endeavor whenever feasible to update the specification, compilers, or libraries without affecting existing code.

These same considerations apply to successive point releases. For instance, code that runs under Go 1.2 should be compatible with Go 1.2.1, Go 1.3, Go 1.4, etc., although not necessarily with Go 1.1 since it may u

*[Content truncated - see full docs]*

---

## Go, Backwards Compatibility, and GODEBUG

**URL**: https://go.dev/doc/godebug

**Contents**:
- Go, Backwards Compatibility, and GODEBUG
- Introduction
- Default GODEBUG Values
- GODEBUG History
  - Go 1.26
  - Go 1.25
  - Go 1.24
  - Go 1.23

Go’s emphasis on backwards compatibility is one of its key strengths. There are, however, times when we cannot maintain complete compatibility. If code depends on buggy (including insecure) behavior, then fixing the bug will break that code. New features can also have similar impacts: enabling the HTTP/2 use by the HTTP client broke programs connecting to servers with buggy HTTP/2 implementations. These kinds of changes are unavoidable and permitted by the Go 1 compatibility rules. Even so, Go provides a mechanism called GODEBUG to reduce the impact such changes have on Go developers using newer toolchains to compile old code.

A GODEBUG setting is a key=value pair that controls the execution of certain parts of a Go program. The environment variable GODEBUG can hold a comma-separated list of these settings. For example, if a Go program is running in an environment that contains

then that Go program will disable the use of HTTP/2 by default in both the HTTP client and the HTTP server. Unrecognized settings in the GODEBUG environment variable are ignored. It is also possible to set the default GODEBUG for a given program (discussed below).

When preparing any change that is permitted by Go 1 compatibility but may nonetheless break some existing programs, we first engineer the change to keep as many existing programs working as possible. For the remaining programs, we define a new GODEBUG setting that allows individual programs to opt back in to the old behavior. A GODEBUG setting may not be added if doing so is infeasible, but that should be extremely rare.

GODEBUG settings added for compatibility will be maintained for a minimum of two years (four Go releases). Some, such as http2client and http2server, will be maintained much longer, even indefinitely.

When possible, each GODEBUG setting has an associated runtime/metrics counter named /godebug/non-default-behavior/<name>:events that counts the number of times a particular program’s behavior has changed based on 

*[Content truncated - see full docs]*

**Examples**:

```text
GODEBUG=http2client=0,http2server=0
```

```text
godebug (
    default=go1.21
    panicnil=1
    asynctimerchan=0
)
```

```text
//go:debug default=go1.21
//go:debug panicnil=1
//go:debug asynctimerchan=0
```

---

## Go Doc Comments

**URL**: https://go.dev/doc/comment

**Contents**:
- Go Doc Comments
- Packages
- Commands
- Types
- Funcs
- Consts
- Vars
- Syntax

Packages Commands Types Funcs Consts Vars Syntax Common mistakes and pitfalls

“Doc comments” are comments that appear immediately before top-level package, const, func, type, and var declarations with no intervening newlines. Every exported (capitalized) name should have a doc comment.

The go/doc and go/doc/comment packages provide the ability to extract documentation from Go source code, and a variety of tools make use of this functionality. The go doc command looks up and prints the doc comment for a given package or symbol. (A symbol is a top-level const, func, type, or var.) The web server pkg.go.dev shows the documentation for public Go packages (when their licenses permit that use). The program serving that site is golang.org/x/pkgsite/cmd/pkgsite, which can also be run locally to view documentation for private modules or without an internet connection. The language server gopls provides documentation when editing Go source files in IDEs.

The rest of this page documents how to write Go doc comments.

Every package should have a package comment introducing the package. It provides information relevant to the package as a whole and generally sets expectations for the package. Especially in large packages, it can be helpful for the package comment to give a brief overview of the most important parts of the API, linking to other doc comments as needed.

If the package is simple, the package comment can be brief. For example:

The square brackets in [path/filepath] create a documentation link.

As can be seen in this example, Go doc comments use complete sentences. For a package comment, that means the first sentence begins with “Package ”.

For multi-file packages, the package comment should only be in one source file. If multiple files have package comments, they are concatenated to form one large comment for the entire package.

A package comment for a command is similar, but it describes the behavior of the program rather than the Go symbols in the package. 

*[Content truncated - see full docs]*

**Examples**:

```text
// Package path implements utility routines for manipulating slash-separated
// paths.
//
// The path package should only be used for paths separated by forward
// slashes, such as the paths in URLs. This package does not deal with
// Windows paths with drive letters or backslashes; to manipulate
// operating system paths, use the [path/filepath] package.
package path
```

```text
/*
Gofmt formats Go programs.
It uses tabs for indentation and blanks for alignment.
Alignment assumes that an editor is using a fixed-width font.

Without an explicit path, it processes the standard input. Given a file,
it operates on that file; given a directory, it operates on all .go files in
that directory, recursively. (Files starting with a period are ignored.)
By default, gofmt prints the reformatted sources to standard output.

Usage:

    gofmt [flags] [path ...]

The flags are:

    -
...
```

```text
$ go doc gofmt
Gofmt formats Go programs. It uses tabs for indentation and blanks for
alignment. Alignment assumes that an editor is using a fixed-width font.

Without an explicit path, it processes the standard input. Given a file, it
operates on that file; given a directory, it operates on all .go files in that
directory, recursively. (Files starting with a period are ignored.) By default,
gofmt prints the reformatted sources to standard output.

Usage:

    gofmt [flags] [path ...]

The flags
...
```

---

## Go Toolchains

**URL**: https://go.dev/doc/toolchain

**Contents**:
- Go Toolchains
- Introduction
- Go versions
- Go toolchain names
- Module and workspace configuration
- The GOTOOLCHAIN setting
- Go toolchain selection
- Go toolchain switches

Starting in Go 1.21, the Go distribution consists of a go command and a bundled Go toolchain, which is the standard library as well as the compiler, assembler, and other tools. The go command can use its bundled Go toolchain as well as other versions that it finds in the local PATH or downloads as needed.

The choice of Go toolchain being used depends on the GOTOOLCHAIN environment setting and the go and toolchain lines in the main module’s go.mod file or the current workspace’s go.work file. As you move between different main modules and workspaces, the toolchain version being used can vary, just as module dependency versions do.

In the standard configuration, the go command uses its own bundled toolchain when that toolchain is at least as new as the go or toolchain lines in the main module or workspace. For example, when using the go command bundled with Go 1.21.3 in a main module that says go 1.21.0, the go command uses Go 1.21.3. When the go or toolchain line is newer than the bundled toolchain, the go command runs the newer toolchain instead. For example, when using the go command bundled with Go 1.21.3 in a main module that says go 1.21.9, the go command finds and runs Go 1.21.9 instead. It first looks in the PATH for a program named go1.21.9 and otherwise downloads and caches a copy of the Go 1.21.9 toolchain. This automatic toolchain switching can be disabled, but in that case, for more precise forwards compatibility, the go command will refuse to run in a main module or workspace in which the go line requires a newer version of Go. That is, the go line sets the minimum required Go version necessary to use a module or workspace.

Modules that are dependencies of other modules may need to set a minimum Go version requirement lower than the preferred toolchain to use when working in that module directly. In this case, the toolchain line in go.mod or go.work sets a preferred toolchain that takes precedence over the go line when the go command is deciding which

*[Content truncated - see full docs]*

**Examples**:

```text
GOTOOLCHAIN=go1.21rc3 go test
```

```text
go env -w GOTOOLCHAIN=go1.21.3+auto
```

```text
go: module example.com/widget@v1.2.3 requires go >= 1.24rc1; switching to go 1.27.9
```

---

## How to Write Go Code

**URL**: https://go.dev/doc/code

**Contents**:
- How to Write Go Code
- Introduction
- Code organization
- Your first program
  - Importing packages from your module
  - Importing packages from remote modules
- Testing
- What's next

This document demonstrates the development of a simple Go package inside a module and introduces the go tool, the standard way to fetch, build, and install Go modules, packages, and commands.

Go programs are organized into packages. A package is a collection of source files in the same directory that are compiled together. Functions, types, variables, and constants defined in one source file are visible to all other source files within the same package.

A repository contains one or more modules. A module is a collection of related Go packages that are released together. A Go repository typically contains only one module, located at the root of the repository. A file named go.mod there declares the module path: the import path prefix for all packages within the module. The module contains the packages in the directory containing its go.mod file as well as subdirectories of that directory, up to the next subdirectory containing another go.mod file (if any).

Note that you don't need to publish your code to a remote repository before you can build it. A module can be defined locally without belonging to a repository. However, it's a good habit to organize your code as if you will publish it someday.

Each module's path not only serves as an import path prefix for its packages, but also indicates where the go command should look to download it. For example, in order to download the module golang.org/x/tools, the go command would consult the repository indicated by https://golang.org/x/tools (described more here).

An import path is a string used to import a package. A package's import path is its module path joined with its subdirectory within the module. For example, the module github.com/google/go-cmp contains a package in the directory cmp/. That package's import path is github.com/google/go-cmp/cmp. Packages in the standard library do not have a module path prefix.

To compile and run a simple program, first choose a module path (we'll use example/user/hello) and 

*[Content truncated - see full docs]*

---

## How to Write Go Code

**URL**: https://go.dev/doc/code.html

**Contents**:
- How to Write Go Code
- Introduction
- Code organization
- Your first program
  - Importing packages from your module
  - Importing packages from remote modules
- Testing
- What's next

This document demonstrates the development of a simple Go package inside a module and introduces the go tool, the standard way to fetch, build, and install Go modules, packages, and commands.

Go programs are organized into packages. A package is a collection of source files in the same directory that are compiled together. Functions, types, variables, and constants defined in one source file are visible to all other source files within the same package.

A repository contains one or more modules. A module is a collection of related Go packages that are released together. A Go repository typically contains only one module, located at the root of the repository. A file named go.mod there declares the module path: the import path prefix for all packages within the module. The module contains the packages in the directory containing its go.mod file as well as subdirectories of that directory, up to the next subdirectory containing another go.mod file (if any).

Note that you don't need to publish your code to a remote repository before you can build it. A module can be defined locally without belonging to a repository. However, it's a good habit to organize your code as if you will publish it someday.

Each module's path not only serves as an import path prefix for its packages, but also indicates where the go command should look to download it. For example, in order to download the module golang.org/x/tools, the go command would consult the repository indicated by https://golang.org/x/tools (described more here).

An import path is a string used to import a package. A package's import path is its module path joined with its subdirectory within the module. For example, the module github.com/google/go-cmp contains a package in the directory cmp/. That package's import path is github.com/google/go-cmp/cmp. Packages in the standard library do not have a module path prefix.

To compile and run a simple program, first choose a module path (we'll use example/user/hello) and 

*[Content truncated - see full docs]*

---

## Installing Go from source

**URL**: https://go.dev/doc/install/source

**Contents**:
- Installing Go from source
- Introduction
- Install Go compiler binaries for bootstrap
  - Bootstrap toolchain from binary release
  - Bootstrap toolchain from cross-compiled source
  - Bootstrap toolchain using gccgo
  - Bootstrap toolchain from C source code
- Install Git, if needed

This topic describes how to build and run Go from source code. To install with an installer, see Download and install.

Go is an open source project, distributed under a BSD-style license. This document explains how to check out the sources, build them on your own machine, and run them.

Most users don't need to do this, and will instead install from precompiled binary packages as described in Download and install, a much simpler process. If you want to help develop what goes into those precompiled packages, though, read on.

There are two official Go compiler toolchains. This document focuses on the gc Go compiler and tools. For information on how to work on gccgo, a more traditional compiler using the GCC back end, see Setting up and using gccgo.

The Go compilers support the following instruction sets: amd64, 386 The x86 instruction set, 64- and 32-bit. arm64, arm The ARM instruction set, 64-bit (AArch64) and 32-bit. loong64 The 64-bit LoongArch instruction set. mips64, mips64le, mips, mipsle The MIPS instruction set, big- and little-endian, 64- and 32-bit. ppc64, ppc64le The 64-bit PowerPC instruction set, big- and little-endian. riscv64 The 64-bit RISC-V instruction set. s390x The IBM z/Architecture. wasm WebAssembly.

The compilers can target the AIX, Android, DragonFly BSD, FreeBSD, Illumos, Linux, macOS/iOS (Darwin), NetBSD, OpenBSD, Plan 9, Solaris, and Windows operating systems (although not all operating systems support all architectures).

A list of ports which are considered "first class" is available at the first class ports wiki page.

The full set of supported combinations is listed in the discussion of environment variables below.

See the Go Wiki MinimumRequirements page for the overall system requirements.

The Go toolchain is written in Go. To build it, you need a Go compiler installed. The scripts that do the initial build of the tools look for a "go" command in $PATH, so as long as you have Go installed in your system and configured in your $PA

*[Content truncated - see full docs]*

---

## Managing Go installations

**URL**: https://go.dev/doc/manage-install

**Contents**:
- Managing Go installations
- Installing multiple Go versions
- Uninstalling Go
  - Removing user config and data
  - Linux / macOS / FreeBSD
  - Windows

This topic describes how to install multiple versions of Go on the same machine, as well as how to uninstall Go.

For other content on installing, you might be interested in:

You can install multiple Go versions on the same machine. For example, you might want to test your code on multiple Go versions. For a list of versions you can install this way, see the download page.

Note: To install using the method described here, you'll need to have git installed.

To install additional Go versions, run the go install command, specifying the download location of the version you want to install. The following example illustrates with version 1.10.7:

To run go commands with the newly-downloaded version, append the version number to the go command, as follows:

When you have multiple versions installed, you can discover where each is installed, look at the version's GOROOT value. For example, run a command such as the following:

To uninstall a downloaded version, just remove the directory specified by its GOROOT environment variable and the goX.Y.Z binary.

You can remove Go from your system using the steps described in this topic.

Go stores user configuration in the go directory within the user configuration directory, as returned by os.UserConfigDir. This can also be found as the directory containing the config file returned by go env GOENV.

Go stores intermediate build artifacts in the directory returned by go env GOCACHE. These can be removed with go clean -cache.

Go stores downloaded dependencies in the directory returned by go env GOMODCACHE. These can be removed with go clean -modcache.

This is usually /usr/local/go.

Under Linux and FreeBSD, edit /etc/profile or $HOME/.profile. If you installed Go with the macOS package, remove the /etc/paths.d/go file.

The simplest way to remove Go is via Add/Remove Programs in the Windows control panel:

For removing Go with tools, you can also use the command line:

Note: Using this uninstall process for Windows will automa

*[Content truncated - see full docs]*

---

## Managing connections

**URL**: https://go.dev/doc/database/manage-connections

**Contents**:
- Managing connections
  - Setting connection pool properties
    - Setting the maximum number of open connections
    - Setting the maximum number of idle connections
    - Setting the maximum amount a time a connection can be idle
    - Setting the maximum lifetime of connections
  - Using dedicated connections

For the vast majority of programs, you needn’t adjust the sql.DB connection pool defaults. But for some advanced programs, you might need to tune the connection pool parameters or work with connections explicitly. This topic explains how.

The sql.DB database handle is safe for concurrent use by multiple goroutines (meaning the handle is what other languages might call “thread-safe”). Some other database access libraries are based on connections that can only be used for one operation at a time. To bridge that gap, each sql.DB manages a pool of active connections to the underlying database, creating new ones as needed for parallelism in your Go program.

The connection pool is suitable for most data access needs. When you call an sql.DB Query or Exec method, the sql.DB implementation retrieves an available connection from the pool or, if needed, creates one. The package returns the connection to the pool when it’s no longer needed. This supports a high level of parallelism for database access.

You can set properties that guide how the sql package manages a connection pool. To get statistics about the effects of these properties, use DB.Stats.

DB.SetMaxOpenConns imposes a limit on the number of open connections. Past this limit, new database operations will wait for an existing operation to finish, at which time sql.DB will create another connection. By default, sql.DB creates a new connection any time all the existing connections are in use when a connection is needed.

Keep in mind that setting a limit makes database usage similar to acquiring a lock or semaphore, with the result that your application can deadlock waiting for a new database connection.

DB.SetMaxIdleConns changes the limit on the maximum number of idle connections sql.DB maintains.

When an SQL operation finishes on a given database connection, it is not typically shut down immediately: the application may need one again soon, and keeping the open connection around avoids having to reconnect to t

*[Content truncated - see full docs]*

---

## Managing dependencies

**URL**: https://go.dev/doc/modules/managing-dependencies

**Contents**:
- Managing dependencies
- Workflow for using and managing dependencies
- Managing dependencies as modules
- Locating and importing useful packages
- Enabling dependency tracking in your code
- Naming a module
- Adding a dependency
- Getting a specific dependency version

When your code uses external packages, those packages (distributed as modules) become dependencies. Over time, you may need to upgrade them or replace them. Go provides dependency management tools that help you keep your Go applications secure as you incorporate external dependencies.

This topic describes how to perform tasks to manage dependencies you take on in your code. You can perform most of these with Go tools. This topic also describes how to perform a few other dependency-related tasks you might find useful.

You can get and use useful packages with Go tools. On pkg.go.dev, you can search for packages you might find useful, then use the go command to import those packages into your own code to call their functions.

The following lists the most common dependency management steps. For more about each, see the sections in this topic.

In Go, you manage dependencies as modules that contain the packages you import. This process is supported by:

You can search pkg.go.dev to find packages with functions you might find useful.

When you’ve found a package you want to use in your code, locate the package path at the top of the page and click the Copy path button to copy the path to your clipboard. In your own code, paste the path into an import statement, as in the following example:

After your code imports the package, enable dependency tracking and get the package’s code to compile with. For more, see Enabling dependency tracking in your code and Adding a dependency.

To track and manage the dependencies you add, you begin by putting your code in its own module. This creates a go.mod file at the root of your source tree. Dependencies you add will be listed in that file.

To add your code to its own module, use the go mod init command. For example, from the command line, change to your code’s root directory, then run the command as in the following example:

The go mod init command’s argument is your module’s module path. If possible, the module path should be 

*[Content truncated - see full docs]*

**Examples**:

```text
import "rsc.io/quote"
```

```text
$ go mod init example/mymodule
```

```text
<prefix>/<descriptive-text>
```

---

## Managing module source

**URL**: https://go.dev/doc/modules/managing-source

**Contents**:
- Managing module source
- How Go tools find your published module
- Organizing code in the repository
- Choosing repository scope
  - Sourcing one module per repository
  - Sourcing multiple modules in a single repository

When you’re developing modules to publish for others to use, you can help ensure that your modules are easier for other developers to use by following the repository conventions described in this topic.

This topic describes actions you might take when managing your module repository. For information about the sequence of workflow steps you’d take when revising from version to version, see Module release and versioning workflow.

Some of the conventions described here are required in modules, while others are best practices. This content assumes you’re familiar with the basic module use practices described in Managing dependencies.

Go supports the following repositories for publishing modules: Git, Subversion, Mercurial, Bazaar, and Fossil.

For an overview of module development, see Developing and publishing modules.

In Go’s decentralized system for publishing modules and retrieving their code, you can publish your module while leaving the code in your repository. Go tools rely on naming rules that have repository paths and repository tags indicating a module’s name and version number. When your repository follows these requirements, your module code is downloadable from your repository by Go tools such as the go get command.

When a developer uses the go get command to get source code for packages their code imports, the command does the following:

You can keep maintenance simple and improve developers’ experience with your module by following the conventions described here. Getting your module code into a repository is generally as simple as with other code.

The following diagram illustrates a source hierarchy for a simple module with two packages.

Your initial commit should include files listed in the following table:

Describes the module, including its module path (in effect, its name) and its dependencies. For more, see the go.mod reference.

The module path will be given in a module directive, such as:

For more about choosing a module path, see Managin

*[Content truncated - see full docs]*

**Examples**:

```text
$ git init
$ git add --all
$ git commit -m "mycode: initial commit"
$ git push
```

---

## Module release and versioning workflow

**URL**: https://go.dev/doc/modules/release-workflow

**Contents**:
- Module release and versioning workflow
- Common workflow steps
- Coding against an unpublished module
- Publishing pre-release versions
- Publishing the first (unstable) version
- Publishing the first stable version
- Publishing bug fixes
- Publishing non-breaking API changes

When you develop modules for use by other developers, you can follow a workflow that helps ensure a reliable, consistent experience for developers using the module. This topic describes the high-level steps in that workflow.

For an overview of module development, see Developing and publishing modules.

The following sequence illustrates release and versioning workflow steps for an example new module. For more about each step, see the sections in this topic.

Begin a module and organize its sources to make it easier for developers to use and for you to maintain.

If you’re brand new to developing modules, check out Tutorial: Create a Go module.

In Go’s decentralized module publishing system, how you organize your code matters. For more, see Managing module source.

Set up to write local client code that calls functions in the unpublished module.

Before you publish a module, it’s unavailable for the typical dependency management workflow using commands such as go get. A good way to test your module code at this stage is to try it while it is in a directory local to your calling code.

See Coding against an unpublished module for more about local development.

When the module’s code is ready for other developers to try it out, begin publishing v0 pre-releases such as alphas and betas. See Publishing pre-release versions for more.

Release a v0 that’s not guaranteed to be stable, but which users can try out. For more, see Publishing the first (unstable) version.

After your v0 version is published, you can (and should!) continue to release new versions of it.

These new versions might include bug fixes (patch releases), additions to the module’s public API (minor releases), and even breaking changes. Because a v0 release makes no guarantees of stability or backward compatibility, you can make breaking changes in its versions.

For more, see Publishing bug fixes and Publishing non-breaking API changes.

When you’re getting a stable version ready for release, you publi

*[Content truncated - see full docs]*

**Examples**:

```text
v0.2.1-beta.1
v1.2.3-alpha
```

```text
go get example.com/theirmodule@v1.2.3-alpha
```

```text
example.com/mymodule/v2
```

---

## Module version numbering

**URL**: https://go.dev/doc/modules/version-numbers

**Contents**:
- Module version numbering
- In development
  - Pseudo-version number
    - Syntax
    - Parts
  - v0 number
- Pre-release version
    - Example

A module’s developer uses each part of a module’s version number to signal the version’s stability and backward compatibility. For each new release, a module’s release version number specifically reflects the nature of the module’s changes since the preceding release.

When you’re developing code that uses external modules, you can use the version numbers to understand an external module’s stability when you’re considering an upgrade. When you’re developing your own modules, your version numbers will signal your modules’ stability and backward compatibility to other developers.

This topic describes what module version numbers mean.

A released module is published with a version number in the semantic versioning model, as in the following illustration:

The following table describes how the parts of a version number signify a module’s stability and backward compatibility.

Signals that the module is still in development and unstable. This release carries no backward compatibility or stability guarantees.

The version number can take one of the following forms:

Pseudo-version number

v0.0.0-20170915032832-14c0d48ead0c

When a module has not been tagged in its repository, Go tools will generate a pseudo-version number for use in the go.mod file of code that calls functions in the module.

Note: As a best practice, always allow Go tools to generate the pseudo-version number rather than creating your own.

Pseudo-versions are useful when a developer of code consuming the module’s functions needs to develop against a commit that hasn’t been tagged with a semantic version tag yet.

A pseudo-version number has three parts separated by dashes, as shown in the following form:

baseVersionPrefix-timestamp-revisionIdentifier

baseVersionPrefix (vX.0.0 or vX.Y.Z-0) is a value derived either from a semantic version tag that precedes the revision or from vX.0.0 if there is no such tag.

timestamp (yymmddhhmmss) is the UTC time the revision was created. In Git, this is the commit

*[Content truncated - see full docs]*

**Examples**:

```text
vx.x.x-beta.2
```

```text
module example.com/mymodule/v2 v2.0.0
```

---

## Opening a database handle

**URL**: https://go.dev/doc/database/open-handle

**Contents**:
- Opening a database handle
  - Locating and importing a database driver
  - Opening a database handle
    - Opening with a connection string
    - Opening with a Connector
    - Handling errors
  - Confirming a connection
  - Storing database credentials

The database/sql package simplifies database access by reducing the need for you to manage connections. Unlike many data access APIs, with database/sql you don’t explicitly open a connection, do work, then close the connection. Instead, your code opens a database handle that represents a connection pool, then executes data access operations with the handle, calling a Close method only when needed to free resources, such as those held by retrieved rows or a prepared statement.

In other words, it’s the database handle, represented by an sql.DB, that handles connections, opening and closing them on your code’s behalf. As your code uses the handle to execute database operations, those operations have concurrent access to the database. For more, see Managing connections.

Note: You can also reserve a database connection. For more information, see Using dedicated connections.

In addition to the APIs available in the database/sql package, the Go community has developed drivers for all of the most common (and many uncommon) database management systems (DBMSes).

When opening a database handle, you follow these high-level steps:

A driver translates requests and responses between your Go code and the database. For more, see Locating and importing a database driver.

Open a database handle.

After you’ve imported the driver, you can open a handle for a specific database. For more, see Opening a database handle.

Confirm a connection.

Once you’ve opened a database handle, your code can check that a connection is available. For more, see Confirming a connection.

Your code typically won’t explicitly open or close database connections – that’s done by the database handle. However, your code should free resources it obtains along the way, such as an sql.Rows containing query results. For more, see Freeing resources.

You’ll need a database driver that supports the DBMS you’re using. To locate a driver for your database, see SQLDrivers.

To make the driver available to your cod

*[Content truncated - see full docs]*

**Examples**:

```text
import "github.com/go-sql-driver/mysql"
```

```text
import _ "github.com/go-sql-driver/mysql"
```

```text
db, err = sql.Open("mysql", "username:password@tcp(127.0.0.1:3306)/jazzrecords")
if err != nil {
    log.Fatal(err)
}
```

---

## Organizing a Go module

**URL**: https://go.dev/doc/modules/layout

**Contents**:
- Organizing a Go module
  - Basic package
  - Basic command
  - Package or command with supporting packages
  - Multiple packages
  - Multiple commands
  - Packages and commands in the same repository
  - Server project

A common question developers new to Go have is “How do I organize my Go project?”, in terms of the layout of files and folders. The goal of this document is to provide some guidelines that will help answer this question. To make the most of this document, make sure you’re familiar with the basics of Go modules by reading the tutorial and managing module source.

Go projects can include packages, command-line programs or a combination of the two. This guide is organized by project type.

A basic Go package has all its code in the project’s root directory. The project consists of a single module, which consists of a single package. The package name matches the last path component of the module name. For a very simple package requiring a single Go file, the project structure is:

[throughout this document, file/package names are entirely arbitrary]

Assuming this directory is uploaded to a GitHub repository at github.com/someuser/modname, the module line in the go.mod file should say module github.com/someuser/modname.

The code in modname.go declares the package with:

Users can then rely on this package by import-ing it in their Go code with:

A Go package can be split into multiple files, all residing within the same directory, e.g.:

All the files in the directory declare package modname.

A basic executable program (or command-line tool) is structured according to its complexity and code size. The simplest program can consist of a single Go file where func main is defined. Larger programs can have their code split across multiple files, all declaring package main:

Here the main.go file contains func main, but this is just a convention. The “main” file can also be called modname.go (for an appropriate value of modname) or anything else.

Assuming this directory is uploaded to a GitHub repository at github.com/someuser/modname, the module line in the go.mod file should say:

And a user should be able to install it on their machine with:

Larger packages or commands

*[Content truncated - see full docs]*

**Examples**:

```text
project-root-directory/
  go.mod
  modname.go
  modname_test.go
```

```text
package modname

// ... package code here
```

```text
import "github.com/someuser/modname"
```

---

## Profile-guided optimization

**URL**: https://go.dev/doc/pgo

**Contents**:
- Profile-guided optimization
- Overview
- Collecting profiles
- Building with PGO
- Notes
- Collecting representative profiles from production
- Merging profiles
- AutoFDO

Starting in Go 1.20, the Go compiler supports profile-guided optimization (PGO) to further optimize builds.

Overview Collecting profiles Building with PGO Notes Frequently Asked Questions Appendix: alternative profile sources

Profile-guided optimization (PGO), also known as feedback-directed optimization (FDO), is a compiler optimization technique that feeds information (a profile) from representative runs of the application back into to the compiler for the next build of the application, which uses that information to make more informed optimization decisions. For example, the compiler may decide to more aggressively inline functions which the profile indicates are called frequently.

In Go, the compiler uses CPU pprof profiles as the input profile, such as from runtime/pprof or net/http/pprof.

As of Go 1.22, benchmarks for a representative set of Go programs show that building with PGO improves performance by around 2-14%. We expect performance gains to generally increase over time as additional optimizations take advantage of PGO in future versions of Go.

The Go compiler expects a CPU pprof profile as the input to PGO. Profiles generated by the Go runtime (such as from runtime/pprof and net/http/pprof) can be used directly as the compiler input. It may also be possible to use/convert profiles from other profiling systems. See the appendix for additional information.

For best results, it is important that profiles are representative of actual behavior in the application’s production environment. Using an unrepresentative profile is likely to result in a binary with little to no improvement in production. Thus, collecting profiles directly from the production environment is recommended, and is the primary method that Go’s PGO is designed for.

The typical workflow is as follows:

Go PGO is generally robust to skew between the profiled version of an application and the version building with the profile, as well as to building with profiles collected from alread

*[Content truncated - see full docs]*

**Examples**:

```text
$ go tool pprof -proto a.pprof b.pprof > merged.pprof
```

---

## Publishing a module

**URL**: https://go.dev/doc/modules/publishing

**Contents**:
- Publishing a module
- Publishing steps

When you want to make a module available for other developers, you publish it so that it’s visible to Go tools. Once you’ve published the module, developers importing its packages will be able to resolve a dependency on the module by running commands such as go get.

Note: Don’t change a tagged version of a module after publishing it. For developers using the module, Go tools authenticate a downloaded module against the first downloaded copy. If the two differ, Go tools will return a security error. Instead of changing the code for a previously published version, publish a new version.

Use the following steps to publish a module.

Open a command prompt and change to your module’s root directory in the local repository.

Run go mod tidy, which removes any dependencies the module might have accumulated that are no longer necessary.

Run go test ./... a final time to make sure everything is working.

This runs the unit tests you’ve written to use the Go testing framework.

Tag the project with a new version number using the git tag command.

For the version number, use a number that signals to users the nature of changes in this release. For more, see Module version numbering.

Push the new tag to the origin repository.

Make the module available by running the go list command to prompt Go to update its index of modules with information about the module you’re publishing.

Precede the command with a statement to set the GOPROXY environment variable to a Go proxy. This will ensure that your request reaches the proxy.

Developers interested in your module import a package from it and run the go get command just as they would with any other module. They can run the go get command for latest versions or they can specify a particular version, as in the following example:

**Examples**:

```text
$ go mod tidy
```

```text
$ go test ./...
ok      example.com/mymodule       0.015s
```

```text
$ git commit -m "mymodule: changes for v0.1.0"
$ git tag v0.1.0
```

---

## Querying for data

**URL**: https://go.dev/doc/database/querying

**Contents**:
- Querying for data
  - Querying for a single row
    - Handling errors
    - Functions for returning a single row
  - Querying for multiple rows
    - Handling errors
    - Functions for returning multiple rows
  - Handling nullable column values

When executing an SQL statement that returns data, use one of the Query methods provided in the database/sql package. Each of these returns a Row or Rows whose data you can copy to variables using the Scan method. You’d use these methods to, for example, execute SELECT statements.

When executing a statement that doesn’t return data, you can use an Exec or ExecContext method instead. For more, see Executing statements that don’t return data.

The database/sql package provides two ways to execute a query for results.

If your code will be executing the same SQL statement repeatedly, consider using a prepared statement. For more, see Using prepared statements.

Caution: Don’t use string formatting functions such as fmt.Sprintf to assemble an SQL statement! You could introduce an SQL injection risk. For more, see Avoiding SQL injection risk.

QueryRow retrieves at most a single database row, such as when you want to look up data by a unique ID. If multiple rows are returned by the query, the Scan method discards all but the first.

QueryRowContext works like QueryRow but with a context.Context argument. For more, see Canceling in-progress operations.

The following example uses a query to find out if there’s enough inventory to support a purchase. The SQL statement returns true if there’s enough, false if not. Row.Scan copies the boolean return value into the enough variable through a pointer.

Note: Parameter placeholders in prepared statements vary depending on the DBMS and driver you’re using. For example, the pq driver for Postgres requires a placeholder like $1 instead of ?.

QueryRow itself returns no error. Instead, Scan reports any error from the combined lookup and scan. It returns sql.ErrNoRows when the query finds no rows.

You can query for multiple rows using Query or QueryContext, which return a Rows representing the query results. Your code iterates over the returned rows using Rows.Next. Each iteration calls Scan to copy column values into variables.

Q

*[Content truncated - see full docs]*

**Examples**:

```text
func canPurchase(id int, quantity int) (bool, error) {
    var enough bool
    // Query for a value based on a single row.
    if err := db.QueryRow("SELECT (quantity >= ?) from album where id = ?",
        quantity, id).Scan(&enough); err != nil {
        if err == sql.ErrNoRows {
            return false, fmt.Errorf("canPurchase %d: unknown album", id)
        }
        return false, fmt.Errorf("canPurchase %d: %v", id, err)
    }
    return enough, nil
}
```

```text
func albumsByArtist(artist string) ([]Album, error) {
    rows, err := db.Query("SELECT * FROM album WHERE artist = ?", artist)
    if err != nil {
        return nil, err
    }
    defer rows.Close()

    // An album slice to hold data from returned rows.
    var albums []Album

    // Loop through rows, using Scan to assign column data to struct fields.
    for rows.Next() {
        var alb Album
        if err := rows.Scan(&alb.ID, &alb.Title, &alb.Artist,
            &alb.Price, &alb.Quantit
...
```

```text
var s sql.NullString
err := db.QueryRow("SELECT name FROM customer WHERE id = ?", id).Scan(&s)
if err != nil {
    log.Fatal(err)
}

// Find customer name, using placeholder if not present.
name := "Valued Customer"
if s.Valid {
    name = s.String
}
```

---

## Release History

**URL**: https://go.dev/doc/devel/release.html

**Contents**:
- Release History
- Release Policy
- go1.25.0 (released 2025-08-12)
  - Minor revisions
- go1.24.0 (released 2025-02-11)
  - Minor revisions
- go1.23.0 (released 2024-08-13)
  - Minor revisions

This page summarizes the changes between official stable releases of Go. The change log has the full details.

To update to a specific release, use:

Each major Go release is supported until there are two newer major releases. For example, Go 1.5 was supported until the Go 1.7 release, and Go 1.6 was supported until the Go 1.8 release. We fix critical problems, including critical security problems, in supported releases as needed by issuing minor revisions (for example, Go 1.6.1, Go 1.6.2, and so on).

Go 1.25.0 is a major release of Go. Read the Go 1.25 Release Notes for more information.

go1.25.1 (released 2025-09-03) includes security fixes to the net/http package, as well as bug fixes to the go command, and the net, os, os/exec, and testing/synctest packages. See the Go 1.25.1 milestone on our issue tracker for details.

go1.25.2 (released 2025-10-07) includes security fixes to the archive/tar, crypto/tls, crypto/x509, encoding/asn1, encoding/pem, net/http, net/mail, net/textproto, and net/url packages, as well as bug fixes to the compiler, the runtime, and the context, debug/pe, net/http, os, and sync/atomic packages. See the Go 1.25.2 milestone on our issue tracker for details.

go1.25.3 (released 2025-10-13) includes fixes to the crypto/x509 package. See the Go 1.25.3 milestone on our issue tracker for details.

Go 1.24.0 is a major release of Go. Read the Go 1.24 Release Notes for more information.

go1.24.1 (released 2025-03-04) includes security fixes to the net/http package, as well as bug fixes to cgo, the compiler, the go command, and the reflect, runtime, and syscall packages. See the Go 1.24.1 milestone on our issue tracker for details.

go1.24.2 (released 2025-04-01) includes security fixes to the net/http package, as well as bug fixes to the compiler, the runtime, the go command, and the crypto/tls, go/types, net/http, and testing packages. See the Go 1.24.2 milestone on our issue tracker for details.

go1.24.3 (released 2025-05-06) includes securi

*[Content truncated - see full docs]*

---

## Release History

**URL**: https://go.dev/doc/devel/release

**Contents**:
- Release History
- Release Policy
- go1.25.0 (released 2025-08-12)
  - Minor revisions
- go1.24.0 (released 2025-02-11)
  - Minor revisions
- go1.23.0 (released 2024-08-13)
  - Minor revisions

This page summarizes the changes between official stable releases of Go. The change log has the full details.

To update to a specific release, use:

Each major Go release is supported until there are two newer major releases. For example, Go 1.5 was supported until the Go 1.7 release, and Go 1.6 was supported until the Go 1.8 release. We fix critical problems, including critical security problems, in supported releases as needed by issuing minor revisions (for example, Go 1.6.1, Go 1.6.2, and so on).

Go 1.25.0 is a major release of Go. Read the Go 1.25 Release Notes for more information.

go1.25.1 (released 2025-09-03) includes security fixes to the net/http package, as well as bug fixes to the go command, and the net, os, os/exec, and testing/synctest packages. See the Go 1.25.1 milestone on our issue tracker for details.

go1.25.2 (released 2025-10-07) includes security fixes to the archive/tar, crypto/tls, crypto/x509, encoding/asn1, encoding/pem, net/http, net/mail, net/textproto, and net/url packages, as well as bug fixes to the compiler, the runtime, and the context, debug/pe, net/http, os, and sync/atomic packages. See the Go 1.25.2 milestone on our issue tracker for details.

go1.25.3 (released 2025-10-13) includes fixes to the crypto/x509 package. See the Go 1.25.3 milestone on our issue tracker for details.

Go 1.24.0 is a major release of Go. Read the Go 1.24 Release Notes for more information.

go1.24.1 (released 2025-03-04) includes security fixes to the net/http package, as well as bug fixes to cgo, the compiler, the go command, and the reflect, runtime, and syscall packages. See the Go 1.24.1 milestone on our issue tracker for details.

go1.24.2 (released 2025-04-01) includes security fixes to the net/http package, as well as bug fixes to the compiler, the runtime, the go command, and the crypto/tls, go/types, net/http, and testing packages. See the Go 1.24.2 milestone on our issue tracker for details.

go1.24.3 (released 2025-05-06) includes securi

*[Content truncated - see full docs]*

---

## Return a random greeting

**URL**: https://go.dev/doc/tutorial/random-greeting.html

**Contents**:
- Return a random greeting

In this section, you'll change your code so that instead of returning a single greeting every time, it returns one of several predefined greeting messages.

To do this, you'll use a Go slice. A slice is like an array, except that its size changes dynamically as you add and remove items. The slice is one of Go's most useful types.

You'll add a small slice to contain three greeting messages, then have your code return one of the messages randomly. For more on slices, see Go slices in the Go blog.

You're just adding Gladys's name (or a different name, if you like) as an argument to the Hello function call in hello.go.

Next, you'll use a slice to greet multiple people.

< Return and handle an error Return greetings for multiple people >

---

## Return and handle an error

**URL**: https://go.dev/doc/tutorial/handle-errors.html

**Contents**:
- Return and handle an error

Handling errors is an essential feature of solid code. In this section, you'll add a bit of code to return an error from the greetings module, then handle it in the caller.

There's no sense sending a greeting back if you don't know who to greet. Return an error to the caller if the name is empty. Copy the following code into greetings.go and save the file.

Paste the following code into hello.go.

Now that you're passing in an empty name, you'll get an error.

That's common error handling in Go: Return an error as a value so the caller can check for it.

Next, you'll use a Go slice to return a randomly-selected greeting.

< Call your code from another module Return a random greeting >

---

## Return greetings for multiple people

**URL**: https://go.dev/doc/tutorial/greetings-multiple-people.html

**Contents**:
- Return greetings for multiple people

In the last changes you'll make to your module's code, you'll add support for getting greetings for multiple people in one request. In other words, you'll handle a multiple-value input, then pair values in that input with a multiple-value output. To do this, you'll need to pass a set of names to a function that can return a greeting for each of them.

But there's a hitch. Changing the Hello function's parameter from a single name to a set of names would change the function's signature. If you had already published the example.com/greetings module and users had already written code calling Hello, that change would break their programs.

In this situation, a better choice is to write a new function with a different name. The new function will take multiple parameters. That preserves the old function for backward compatibility.

In hello.go, change your code so it looks like the following.

With these changes, you:

The output should be a string representation of the map associating names with messages, something like the following:

This topic introduced maps for representing name/value pairs. It also introduced the idea of preserving backward compatibility by implementing a new function for new or changed functionality in a module. For more about backward compatibility, see Keeping your modules compatible.

Next, you'll use built-in Go features to create a unit test for your code.

< Return a random greeting Add a test >

---

## Source file doc/articles/wiki/final.go

**URL**: https://go.dev/doc/articles/wiki/final.go

**Contents**:
- Source file doc/articles/wiki/final.go

---

## Source file doc/articles/wiki/part1.go

**URL**: https://go.dev/doc/articles/wiki/part1.go

**Contents**:
- Source file doc/articles/wiki/part1.go

---

## Source file doc/articles/wiki/part2.go

**URL**: https://go.dev/doc/articles/wiki/part2.go

**Contents**:
- Source file doc/articles/wiki/part2.go

---

## Source file doc/articles/wiki/part3.go

**URL**: https://go.dev/doc/articles/wiki/part3.go

**Contents**:
- Source file doc/articles/wiki/part3.go

---

## The Go Blog

**URL**: https://go.dev/doc/articles/defer_panic_recover.html

**Contents**:
- The Go Blog
- Defer, Panic, and Recover

Andrew Gerrand 4 August 2010

Go has the usual mechanisms for control flow: if, for, switch, goto. It also has the go statement to run code in a separate goroutine. Here I’d like to discuss some of the less common ones: defer, panic, and recover.

A defer statement pushes a function call onto a list. The list of saved calls is executed after the surrounding function returns. Defer is commonly used to simplify functions that perform various clean-up actions.

For example, let’s look at a function that opens two files and copies the contents of one file to the other:

This works, but there is a bug. If the call to os.Create fails, the function will return without closing the source file. This can be easily remedied by putting a call to src.Close before the second return statement, but if the function were more complex the problem might not be so easily noticed and resolved. By introducing defer statements we can ensure that the files are always closed:

Defer statements allow us to think about closing each file right after opening it, guaranteeing that, regardless of the number of return statements in the function, the files will be closed.

The behavior of defer statements is straightforward and predictable. There are three simple rules:

In this example, the expression “i” is evaluated when the Println call is deferred. The deferred call will print “0” after the function returns.

This function prints “3210”:

In this example, a deferred function increments the return value i after the surrounding function returns. Thus, this function returns 2:

This is convenient for modifying the error return value of a function; we will see an example of this shortly.

Panic is a built-in function that stops the ordinary flow of control and begins panicking. When the function F calls panic, execution of F stops, any deferred functions in F are executed normally, and then F returns to its caller. To the caller, F then behaves like a call to panic. The process continues up the sta

*[Content truncated - see full docs]*

**Examples**:

```text
func CopyFile(dstName, srcName string) (written int64, err error) {
    src, err := os.Open(srcName)
    if err != nil {
        return
    }

    dst, err := os.Create(dstName)
    if err != nil {
        return
    }

    written, err = io.Copy(dst, src)
    dst.Close()
    src.Close()
    return
}
```

```text
func CopyFile(dstName, srcName string) (written int64, err error) {
    src, err := os.Open(srcName)
    if err != nil {
        return
    }
    defer src.Close()

    dst, err := os.Create(dstName)
    if err != nil {
        return
    }
    defer dst.Close()

    return io.Copy(dst, src)
}
```

```text
func a() {
    i := 0
    defer fmt.Println(i)
    i++
    return
}
```

---

## The Go Blog

**URL**: https://go.dev/doc/articles/error_handling.html

**Contents**:
- The Go Blog
- Error handling and Go
- Introduction
- The error type
- Simplifying repetitive error handling
- Conclusion

Andrew Gerrand 12 July 2011

If you have written any Go code you have probably encountered the built-in error type. Go code uses error values to indicate an abnormal state. For example, the os.Open function returns a non-nil error value when it fails to open a file.

The following code uses os.Open to open a file. If an error occurs it calls log.Fatal to print the error message and stop.

You can get a lot done in Go knowing just this about the error type, but in this article we’ll take a closer look at error and discuss some good practices for error handling in Go.

The error type is an interface type. An error variable represents any value that can describe itself as a string. Here is the interface’s declaration:

The error type, as with all built in types, is predeclared in the universe block.

The most commonly-used error implementation is the errors package’s unexported errorString type.

You can construct one of these values with the errors.New function. It takes a string that it converts to an errors.errorString and returns as an error value.

Here’s how you might use errors.New:

A caller passing a negative argument to Sqrt receives a non-nil error value (whose concrete representation is an errors.errorString value). The caller can access the error string (“math: square root of…”) by calling the error’s Error method, or by just printing it:

The fmt package formats an error value by calling its Error() string method.

It is the error implementation’s responsibility to summarize the context. The error returned by os.Open formats as “open /etc/passwd: permission denied,” not just “permission denied.” The error returned by our Sqrt is missing information about the invalid argument.

To add that information, a useful function is the fmt package’s Errorf. It formats a string according to Printf’s rules and returns it as an error created by errors.New.

In many cases fmt.Errorf is good enough, but since error is an interface, you can use arbitrary data structures 

*[Content truncated - see full docs]*

**Examples**:

```text
func Open(name string) (file *File, err error)
```

```text
f, err := os.Open("filename.ext")
if err != nil {
    log.Fatal(err)
}
// do something with the open *File f
```

```text
type error interface {
    Error() string
}
```

---

## The Go Blog

**URL**: https://go.dev/doc/articles/slices_usage_and_internals.html

**Contents**:
- The Go Blog
- Go Slices: usage and internals
- Introduction
- Arrays
- Slices
- Slice internals
- Growing slices (the copy and append functions)
- A possible “gotcha”

Andrew Gerrand 5 January 2011

Go’s slice type provides a convenient and efficient means of working with sequences of typed data. Slices are analogous to arrays in other languages, but have some unusual properties. This article will look at what slices are and how they are used.

The slice type is an abstraction built on top of Go’s array type, and so to understand slices we must first understand arrays.

An array type definition specifies a length and an element type. For example, the type [4]int represents an array of four integers. An array’s size is fixed; its length is part of its type ([4]int and [5]int are distinct, incompatible types). Arrays can be indexed in the usual way, so the expression s[n] accesses the nth element, starting from zero.

Arrays do not need to be initialized explicitly; the zero value of an array is a ready-to-use array whose elements are themselves zeroed:

The in-memory representation of [4]int is just four integer values laid out sequentially:

Go’s arrays are values. An array variable denotes the entire array; it is not a pointer to the first array element (as would be the case in C). This means that when you assign or pass around an array value you will make a copy of its contents. (To avoid the copy you could pass a pointer to the array, but then that’s a pointer to an array, not an array.) One way to think about arrays is as a sort of struct but with indexed rather than named fields: a fixed-size composite value.

An array literal can be specified like so:

Or, you can have the compiler count the array elements for you:

In both cases, the type of b is [2]string.

Arrays have their place, but they’re a bit inflexible, so you don’t see them too often in Go code. Slices, though, are everywhere. They build on arrays to provide great power and convenience.

The type specification for a slice is []T, where T is the type of the elements of the slice. Unlike an array type, a slice type has no specified length.

A slice literal is declar

*[Content truncated - see full docs]*

**Examples**:

```text
var a [4]int
a[0] = 1
i := a[0]
// i == 1
```

```text
// a[2] == 0, the zero value of the int type
```

```text
b := [2]string{"Penn", "Teller"}
```

---

## The Go Blog

**URL**: https://go.dev/doc/articles/laws_of_reflection.html

**Contents**:
- The Go Blog
- The Laws of Reflection
- Introduction
- Types and interfaces
- The representation of an interface
- The first law of reflection
- 1. Reflection goes from interface value to reflection object.
- The second law of reflection

Rob Pike 6 September 2011

Reflection in computing is the ability of a program to examine its own structure, particularly through types; it’s a form of metaprogramming. It’s also a great source of confusion.

In this article we attempt to clarify things by explaining how reflection works in Go. Each language’s reflection model is different (and many languages don’t support it at all), but this article is about Go, so for the rest of this article the word “reflection” should be taken to mean “reflection in Go”.

Note added January 2022: This blog post was written in 2011 and predates parametric polymorphism (a.k.a. generics) in Go. Although nothing important in the article has become incorrect as a result of that development in the language, it has been tweaked in a few places to avoid confusing someone familiar with modern Go.

Because reflection builds on the type system, let’s start with a refresher about types in Go.

Go is statically typed. Every variable has a static type, that is, exactly one type known and fixed at compile time: int, float32, *MyType, []byte, and so on. If we declare

then i has type int and j has type MyInt. The variables i and j have distinct static types and, although they have the same underlying type, they cannot be assigned to one another without a conversion.

One important category of type is interface types, which represent fixed sets of methods. (When discussing reflection, we can ignore the use of interface definitions as constraints within polymorphic code.) An interface variable can store any concrete (non-interface) value as long as that value implements the interface’s methods. A well-known pair of examples is io.Reader and io.Writer, the types Reader and Writer from the io package:

Any type that implements a Read (or Write) method with this signature is said to implement io.Reader (or io.Writer). For the purposes of this discussion, that means that a variable of type io.Reader can hold any value whose type has a Read method:


*[Content truncated - see full docs]*

**Examples**:

```text
type MyInt int

var i int
var j MyInt
```

```text
// Reader is the interface that wraps the basic Read method.
type Reader interface {
    Read(p []byte) (n int, err error)
}

// Writer is the interface that wraps the basic Write method.
type Writer interface {
    Write(p []byte) (n int, err error)
}
```

```text
var r io.Reader
r = os.Stdin
r = bufio.NewReader(r)
r = new(bytes.Buffer)
// and so on
```

---

## The Go Blog

**URL**: https://go.dev/doc/articles/gos_declaration_syntax.html

**Contents**:
- The Go Blog
- Go's Declaration Syntax
- Introduction
- C syntax
- Go syntax
- Pointers
- Notes

Newcomers to Go wonder why the declaration syntax is different from the tradition established in the C family. In this post we’ll compare the two approaches and explain why Go’s declarations look as they do.

First, let’s talk about C syntax. C took an unusual and clever approach to declaration syntax. Instead of describing the types with special syntax, one writes an expression involving the item being declared, and states what type that expression will have. Thus

declares x to be an int: the expression ‘x’ will have type int. In general, to figure out how to write the type of a new variable, write an expression involving that variable that evaluates to a basic type, then put the basic type on the left and the expression on the right.

Thus, the declarations

state that p is a pointer to int because ‘*p’ has type int, and that a is an array of ints because a[3] (ignoring the particular index value, which is punned to be the size of the array) has type int.

What about functions? Originally, C’s function declarations wrote the types of the arguments outside the parens, like this:

Again, we see that main is a function because the expression main(argc, argv) returns an int. In modern notation we’d write

but the basic structure is the same.

This is a clever syntactic idea that works well for simple types but can get confusing fast. The famous example is declaring a function pointer. Follow the rules and you get this:

Here, fp is a pointer to a function because if you write the expression (*fp)(a, b) you’ll call a function that returns int. What if one of fp’s arguments is itself a function?

That’s starting to get hard to read.

Of course, we can leave out the name of the parameters when we declare a function, so main can be declared

Recall that argv is declared like this,

so you drop the name from the middle of its declaration to construct its type. It’s not obvious, though, that you declare something of type char *[] by putting its name in the middle.

And loo

*[Content truncated - see full docs]*

**Examples**:

```text
int *p;
int a[3];
```

```cpp
int main(argc, argv)
    int argc;
    char *argv[];
{ /* ... */ }
```

```cpp
int main(int argc, char *argv[]) { /* ... */ }
```

---

## Tutorial: Accessing a relational database

**URL**: https://go.dev/doc/tutorial/database-access

**Contents**:
- Tutorial: Accessing a relational database
- Prerequisites
- Create a folder for your code
- Set up a database
- Find and import a database driver
- Get a database handle and connect
    - Write the code
    - Run the code

This tutorial introduces the basics of accessing a relational database with Go and the database/sql package in its standard library.

You’ll get the most out of this tutorial if you have a basic familiarity with Go and its tooling. If this is your first exposure to Go, please see Tutorial: Get started with Go for a quick introduction.

The database/sql package you’ll be using includes types and functions for connecting to databases, executing transactions, canceling an operation in progress, and more. For more details on using the package, see Accessing databases.

In this tutorial, you’ll create a database, then write code to access the database. Your example project will be a repository of data about vintage jazz records.

In this tutorial, you’ll progress through the following sections:

Note: For other tutorials, see Tutorials.

To begin, create a folder for the code you’ll write.

Open a command prompt and change to your home directory.

For the rest of the tutorial we will show a $ as the prompt. The commands we use will work on Windows too.

From the command prompt, create a directory for your code called data-access.

Create a module in which you can manage dependencies you will add during this tutorial.

Run the go mod init command, giving it your new code’s module path.

This command creates a go.mod file in which dependencies you add will be listed for tracking. For more, be sure to see Managing dependencies.

Note: In actual development, you’d specify a module path that’s more specific to your own needs. For more, see Managing dependencies.

Next, you’ll create a database.

In this step, you’ll create the database you’ll be working with. You’ll use the CLI for the DBMS itself to create the database and table, as well as to add data.

You’ll be creating a database with data about vintage jazz recordings on vinyl.

The code here uses the MySQL CLI, but most DBMSes have their own CLI with similar features.

Open a new command prompt.

At the command line, l

*[Content truncated - see full docs]*

**Examples**:

```text
C:\> cd %HOMEPATH%
```

```text
$ mkdir data-access
$ cd data-access
```

```text
$ go mod init example/data-access
go: creating new go.mod: module example/data-access
```

---

## Tutorial: Create a Go module

**URL**: https://go.dev/doc/tutorial/create-module

**Contents**:
- Tutorial: Create a Go module
- Prerequisites
- Start a module that others can use

This is the first part of a tutorial that introduces a few fundamental features of the Go language. If you're just getting started with Go, be sure to take a look at Tutorial: Get started with Go, which introduces the go command, Go modules, and very simple Go code.

In this tutorial you'll create two modules. The first is a library which is intended to be imported by other libraries or applications. The second is a caller application which will use the first.

This tutorial's sequence includes seven brief topics that each illustrate a different part of the language.

Start by creating a Go module. In a module, you collect one or more related packages for a discrete and useful set of functions. For example, you might create a module with packages that have functions for doing financial analysis so that others writing financial applications can use your work. For more about developing modules, see Developing and publishing modules.

Go code is grouped into packages, and packages are grouped into modules. Your module specifies dependencies needed to run your code, including the Go version and the set of other modules it requires.

As you add or improve functionality in your module, you publish new versions of the module. Developers writing code that calls functions in your module can import the module's updated packages and test with the new version before putting it into production use.

For example, from your home directory use the following commands:

Run the go mod init command, giving it your module path -- here, use example.com/greetings. If you publish a module, this must be a path from which your module can be downloaded by Go tools. That would be your code's repository.

For more on naming your module with a module path, see Managing dependencies.

The go mod init command creates a go.mod file to track your code's dependencies. So far, the file includes only the name of your module and the Go version your code supports. But as you add dependencies, the go.mod

*[Content truncated - see full docs]*

---

## Tutorial: Create a Go module

**URL**: https://go.dev/doc/tutorial/create-module.html

**Contents**:
- Tutorial: Create a Go module
- Prerequisites
- Start a module that others can use

This is the first part of a tutorial that introduces a few fundamental features of the Go language. If you're just getting started with Go, be sure to take a look at Tutorial: Get started with Go, which introduces the go command, Go modules, and very simple Go code.

In this tutorial you'll create two modules. The first is a library which is intended to be imported by other libraries or applications. The second is a caller application which will use the first.

This tutorial's sequence includes seven brief topics that each illustrate a different part of the language.

Start by creating a Go module. In a module, you collect one or more related packages for a discrete and useful set of functions. For example, you might create a module with packages that have functions for doing financial analysis so that others writing financial applications can use your work. For more about developing modules, see Developing and publishing modules.

Go code is grouped into packages, and packages are grouped into modules. Your module specifies dependencies needed to run your code, including the Go version and the set of other modules it requires.

As you add or improve functionality in your module, you publish new versions of the module. Developers writing code that calls functions in your module can import the module's updated packages and test with the new version before putting it into production use.

For example, from your home directory use the following commands:

Run the go mod init command, giving it your module path -- here, use example.com/greetings. If you publish a module, this must be a path from which your module can be downloaded by Go tools. That would be your code's repository.

For more on naming your module with a module path, see Managing dependencies.

The go mod init command creates a go.mod file to track your code's dependencies. So far, the file includes only the name of your module and the Go version your code supports. But as you add dependencies, the go.mod

*[Content truncated - see full docs]*

---

## Tutorial: Developing a RESTful API with Go and Gin

**URL**: https://go.dev/doc/tutorial/web-service-gin

**Contents**:
- Tutorial: Developing a RESTful API with Go and Gin
- Prerequisites
- Design API endpoints
- Create a folder for your code
- Create the data
    - Write the code
- Write a handler to return all items
    - Write the code

This tutorial introduces the basics of writing a RESTful web service API with Go and the Gin Web Framework (Gin).

You’ll get the most out of this tutorial if you have a basic familiarity with Go and its tooling. If this is your first exposure to Go, please see Tutorial: Get started with Go for a quick introduction.

Gin simplifies many coding tasks associated with building web applications, including web services. In this tutorial, you’ll use Gin to route requests, retrieve request details, and marshal JSON for responses.

In this tutorial, you will build a RESTful API server with two endpoints. Your example project will be a repository of data about vintage jazz records.

The tutorial includes the following sections:

Note: For other tutorials, see Tutorials.

To try this as an interactive tutorial you complete in Google Cloud Shell, click the button below.

You’ll build an API that provides access to a store selling vintage recordings on vinyl. So you’ll need to provide endpoints through which a client can get and add albums for users.

When developing an API, you typically begin by designing the endpoints. Your API’s users will have more success if the endpoints are easy to understand.

Here are the endpoints you’ll create in this tutorial.

Next, you’ll create a folder for your code.

To begin, create a project for the code you’ll write.

Open a command prompt and change to your home directory.

Using the command prompt, create a directory for your code called web-service-gin.

Create a module in which you can manage dependencies.

Run the go mod init command, giving it the path of the module your code will be in.

This command creates a go.mod file in which dependencies you add will be listed for tracking. For more about naming a module with a module path, see Managing dependencies.

Next, you’ll design data structures for handling data.

To keep things simple for the tutorial, you’ll store data in memory. A more typical API would interact with a database.

No

*[Content truncated - see full docs]*

**Examples**:

```text
C:\> cd %HOMEPATH%
```

```text
$ mkdir web-service-gin
$ cd web-service-gin
```

```text
$ go mod init example/web-service-gin
go: creating new go.mod: module example/web-service-gin
```

---

## Tutorial: Developing a RESTful API with Go and Gin

**URL**: https://go.dev/doc/tutorial/web-service-gin.html

**Contents**:
- Tutorial: Developing a RESTful API with Go and Gin
- Prerequisites
- Design API endpoints
- Create a folder for your code
- Create the data
    - Write the code
- Write a handler to return all items
    - Write the code

This tutorial introduces the basics of writing a RESTful web service API with Go and the Gin Web Framework (Gin).

You’ll get the most out of this tutorial if you have a basic familiarity with Go and its tooling. If this is your first exposure to Go, please see Tutorial: Get started with Go for a quick introduction.

Gin simplifies many coding tasks associated with building web applications, including web services. In this tutorial, you’ll use Gin to route requests, retrieve request details, and marshal JSON for responses.

In this tutorial, you will build a RESTful API server with two endpoints. Your example project will be a repository of data about vintage jazz records.

The tutorial includes the following sections:

Note: For other tutorials, see Tutorials.

To try this as an interactive tutorial you complete in Google Cloud Shell, click the button below.

You’ll build an API that provides access to a store selling vintage recordings on vinyl. So you’ll need to provide endpoints through which a client can get and add albums for users.

When developing an API, you typically begin by designing the endpoints. Your API’s users will have more success if the endpoints are easy to understand.

Here are the endpoints you’ll create in this tutorial.

Next, you’ll create a folder for your code.

To begin, create a project for the code you’ll write.

Open a command prompt and change to your home directory.

Using the command prompt, create a directory for your code called web-service-gin.

Create a module in which you can manage dependencies.

Run the go mod init command, giving it the path of the module your code will be in.

This command creates a go.mod file in which dependencies you add will be listed for tracking. For more about naming a module with a module path, see Managing dependencies.

Next, you’ll design data structures for handling data.

To keep things simple for the tutorial, you’ll store data in memory. A more typical API would interact with a database.

No

*[Content truncated - see full docs]*

**Examples**:

```text
C:\> cd %HOMEPATH%
```

```text
$ mkdir web-service-gin
$ cd web-service-gin
```

```text
$ go mod init example/web-service-gin
go: creating new go.mod: module example/web-service-gin
```

---

## Tutorial: Getting started with fuzzing

**URL**: https://go.dev/doc/tutorial/fuzz

**Contents**:
- Tutorial: Getting started with fuzzing
- Prerequisites
- Create a folder for your code
- Add code to test
  - Write the code
  - Run the code
- Add a unit test
  - Write the code

This tutorial introduces the basics of fuzzing in Go. With fuzzing, random data is run against your test in an attempt to find vulnerabilities or crash-causing inputs. Some examples of vulnerabilities that can be found by fuzzing are SQL injection, buffer overflow, denial of service and cross-site scripting attacks.

In this tutorial, you’ll write a fuzz test for a simple function, run the go command, and debug and fix issues in the code.

For help with terminology throughout this tutorial, see the Go Fuzzing glossary.

You’ll progress through the following sections:

Note: For other tutorials, see Tutorials.

Note: Go fuzzing currently supports a subset of built-in types, listed in the Go Fuzzing docs, with support for more built-in types to be added in the future.

To begin, create a folder for the code you’ll write.

Open a command prompt and change to your home directory.

The rest of the tutorial will show a $ as the prompt. The commands you use will work on Windows too.

From the command prompt, create a directory for your code called fuzz.

Create a module to hold your code.

Run the go mod init command, giving it your new code’s module path.

Note: For production code, you’d specify a module path that’s more specific to your own needs. For more, be sure to see Managing dependencies.

Next, you’ll add some simple code to reverse a string, which we’ll fuzz later.

In this step, you’ll add a function to reverse a string.

Using your text editor, create a file called main.go in the fuzz directory.

Into main.go, at the top of the file, paste the following package declaration.

A standalone program (as opposed to a library) is always in package main.

Beneath the package declaration, paste the following function declaration.

This function will accept a string, loop over it a byte at a time, and return the reversed string at the end.

Note: This code is based on the stringutil.Reverse function within golang.org/x/example.

At the top of main.go, beneath the packa

*[Content truncated - see full docs]*

**Examples**:

```text
C:\> cd %HOMEPATH%
```

```text
$ mkdir fuzz
$ cd fuzz
```

```text
$ go mod init example/fuzz
go: creating new go.mod: module example/fuzz
```

---

## Tutorial: Getting started with fuzzing

**URL**: https://go.dev/doc/tutorial/fuzz.html

**Contents**:
- Tutorial: Getting started with fuzzing
- Prerequisites
- Create a folder for your code
- Add code to test
  - Write the code
  - Run the code
- Add a unit test
  - Write the code

This tutorial introduces the basics of fuzzing in Go. With fuzzing, random data is run against your test in an attempt to find vulnerabilities or crash-causing inputs. Some examples of vulnerabilities that can be found by fuzzing are SQL injection, buffer overflow, denial of service and cross-site scripting attacks.

In this tutorial, you’ll write a fuzz test for a simple function, run the go command, and debug and fix issues in the code.

For help with terminology throughout this tutorial, see the Go Fuzzing glossary.

You’ll progress through the following sections:

Note: For other tutorials, see Tutorials.

Note: Go fuzzing currently supports a subset of built-in types, listed in the Go Fuzzing docs, with support for more built-in types to be added in the future.

To begin, create a folder for the code you’ll write.

Open a command prompt and change to your home directory.

The rest of the tutorial will show a $ as the prompt. The commands you use will work on Windows too.

From the command prompt, create a directory for your code called fuzz.

Create a module to hold your code.

Run the go mod init command, giving it your new code’s module path.

Note: For production code, you’d specify a module path that’s more specific to your own needs. For more, be sure to see Managing dependencies.

Next, you’ll add some simple code to reverse a string, which we’ll fuzz later.

In this step, you’ll add a function to reverse a string.

Using your text editor, create a file called main.go in the fuzz directory.

Into main.go, at the top of the file, paste the following package declaration.

A standalone program (as opposed to a library) is always in package main.

Beneath the package declaration, paste the following function declaration.

This function will accept a string, loop over it a byte at a time, and return the reversed string at the end.

Note: This code is based on the stringutil.Reverse function within golang.org/x/example.

At the top of main.go, beneath the packa

*[Content truncated - see full docs]*

**Examples**:

```text
C:\> cd %HOMEPATH%
```

```text
$ mkdir fuzz
$ cd fuzz
```

```text
$ go mod init example/fuzz
go: creating new go.mod: module example/fuzz
```

---

## Tutorial: Getting started with generics

**URL**: https://go.dev/doc/tutorial/generics

**Contents**:
- Tutorial: Getting started with generics
- Prerequisites
- Create a folder for your code
- Add non-generic functions
    - Write the code
    - Run the code
- Add a generic function to handle multiple types
    - Write the code

This tutorial introduces the basics of generics in Go. With generics, you can declare and use functions or types that are written to work with any of a set of types provided by calling code.

In this tutorial, you’ll declare two simple non-generic functions, then capture the same logic in a single generic function.

You’ll progress through the following sections:

Note: For other tutorials, see Tutorials.

Note: If you prefer, you can use the Go playground in “Go dev branch” mode to edit and run your program instead.

To begin, create a folder for the code you’ll write.

Open a command prompt and change to your home directory.

The rest of the tutorial will show a $ as the prompt. The commands you use will work on Windows too.

From the command prompt, create a directory for your code called generics.

Create a module to hold your code.

Run the go mod init command, giving it your new code’s module path.

Note: For production code, you’d specify a module path that’s more specific to your own needs. For more, be sure to see Managing dependencies.

Next, you’ll add some simple code to work with maps.

In this step, you’ll add two functions that each add together the values of a map and return the total.

You’re declaring two functions instead of one because you’re working with two different types of maps: one that stores int64 values, and one that stores float64 values.

Using your text editor, create a file called main.go in the generics directory. You’ll write your Go code in this file.

Into main.go, at the top of the file, paste the following package declaration.

A standalone program (as opposed to a library) is always in package main.

Beneath the package declaration, paste the following two function declarations.

At the top of main.go, beneath the package declaration, paste the following main function to initialize the two maps and use them as arguments when calling the functions you declared in the preceding step.

Near the top of main.go, just beneath the pa

*[Content truncated - see full docs]*

**Examples**:

```text
C:\> cd %HOMEPATH%
```

```text
$ mkdir generics
$ cd generics
```

```text
$ go mod init example/generics
go: creating new go.mod: module example/generics
```

---

## Tutorial: Getting started with generics

**URL**: https://go.dev/doc/tutorial/generics.html

**Contents**:
- Tutorial: Getting started with generics
- Prerequisites
- Create a folder for your code
- Add non-generic functions
    - Write the code
    - Run the code
- Add a generic function to handle multiple types
    - Write the code

This tutorial introduces the basics of generics in Go. With generics, you can declare and use functions or types that are written to work with any of a set of types provided by calling code.

In this tutorial, you’ll declare two simple non-generic functions, then capture the same logic in a single generic function.

You’ll progress through the following sections:

Note: For other tutorials, see Tutorials.

Note: If you prefer, you can use the Go playground in “Go dev branch” mode to edit and run your program instead.

To begin, create a folder for the code you’ll write.

Open a command prompt and change to your home directory.

The rest of the tutorial will show a $ as the prompt. The commands you use will work on Windows too.

From the command prompt, create a directory for your code called generics.

Create a module to hold your code.

Run the go mod init command, giving it your new code’s module path.

Note: For production code, you’d specify a module path that’s more specific to your own needs. For more, be sure to see Managing dependencies.

Next, you’ll add some simple code to work with maps.

In this step, you’ll add two functions that each add together the values of a map and return the total.

You’re declaring two functions instead of one because you’re working with two different types of maps: one that stores int64 values, and one that stores float64 values.

Using your text editor, create a file called main.go in the generics directory. You’ll write your Go code in this file.

Into main.go, at the top of the file, paste the following package declaration.

A standalone program (as opposed to a library) is always in package main.

Beneath the package declaration, paste the following two function declarations.

At the top of main.go, beneath the package declaration, paste the following main function to initialize the two maps and use them as arguments when calling the functions you declared in the preceding step.

Near the top of main.go, just beneath the pa

*[Content truncated - see full docs]*

**Examples**:

```text
C:\> cd %HOMEPATH%
```

```text
$ mkdir generics
$ cd generics
```

```text
$ go mod init example/generics
go: creating new go.mod: module example/generics
```

---

## Tutorial: Getting started with multi-module workspaces

**URL**: https://go.dev/doc/tutorial/workspaces.html

**Contents**:
- Tutorial: Getting started with multi-module workspaces
- Prerequisites
- Create a module for your code
- Create the workspace
    - Initialize the workspace
    - Run the program in the workspace directory
- Download and modify the golang.org/x/example/hello module
    - Run the code in the workspace

This tutorial introduces the basics of multi-module workspaces in Go. With multi-module workspaces, you can tell the Go command that you’re writing code in multiple modules at the same time and easily build and run code in those modules.

In this tutorial, you’ll create two modules in a shared multi-module workspace, make changes across those modules, and see the results of those changes in a build.

Note: For other tutorials, see Tutorials.

This tutorial requires go1.18 or later. Make sure you’ve installed Go at Go 1.18 or later using the links at go.dev/dl.

To begin, create a module for the code you’ll write.

Open a command prompt and change to your home directory.

The rest of the tutorial will show a $ as the prompt. The commands you use will work on Windows too.

From the command prompt, create a directory for your code called workspace.

Initialize the module

Our example will create a new module hello that will depend on the golang.org/x/example module.

Create the hello module:

Add a dependency on the golang.org/x/example/hello/reverse package by using go get.

Create hello.go in the hello directory with the following contents:

Now, run the hello program:

In this step, we’ll create a go.work file to specify a workspace with the module.

In the workspace directory, run:

The go work init command tells go to create a go.work file for a workspace containing the modules in the ./hello directory.

The go command produces a go.work file that looks like this:

The go.work file has similar syntax to go.mod.

The go directive tells Go which version of Go the file should be interpreted with. It’s similar to the go directive in the go.mod file.

The use directive tells Go that the module in the hello directory should be main modules when doing a build.

So in any subdirectory of workspace the module will be active.

In the workspace directory, run:

The Go command includes all the modules in the workspace as main modules. This allows us to refer to a package in t

*[Content truncated - see full docs]*

**Examples**:

```text
C:\> cd %HOMEPATH%
```

```text
$ mkdir workspace
$ cd workspace
```

```text
$ mkdir hello
$ cd hello
$ go mod init example.com/hello
go: creating new go.mod: module example.com/hello
```

---

## Tutorial: Getting started with multi-module workspaces

**URL**: https://go.dev/doc/tutorial/workspaces

**Contents**:
- Tutorial: Getting started with multi-module workspaces
- Prerequisites
- Create a module for your code
- Create the workspace
    - Initialize the workspace
    - Run the program in the workspace directory
- Download and modify the golang.org/x/example/hello module
    - Run the code in the workspace

This tutorial introduces the basics of multi-module workspaces in Go. With multi-module workspaces, you can tell the Go command that you’re writing code in multiple modules at the same time and easily build and run code in those modules.

In this tutorial, you’ll create two modules in a shared multi-module workspace, make changes across those modules, and see the results of those changes in a build.

Note: For other tutorials, see Tutorials.

This tutorial requires go1.18 or later. Make sure you’ve installed Go at Go 1.18 or later using the links at go.dev/dl.

To begin, create a module for the code you’ll write.

Open a command prompt and change to your home directory.

The rest of the tutorial will show a $ as the prompt. The commands you use will work on Windows too.

From the command prompt, create a directory for your code called workspace.

Initialize the module

Our example will create a new module hello that will depend on the golang.org/x/example module.

Create the hello module:

Add a dependency on the golang.org/x/example/hello/reverse package by using go get.

Create hello.go in the hello directory with the following contents:

Now, run the hello program:

In this step, we’ll create a go.work file to specify a workspace with the module.

In the workspace directory, run:

The go work init command tells go to create a go.work file for a workspace containing the modules in the ./hello directory.

The go command produces a go.work file that looks like this:

The go.work file has similar syntax to go.mod.

The go directive tells Go which version of Go the file should be interpreted with. It’s similar to the go directive in the go.mod file.

The use directive tells Go that the module in the hello directory should be main modules when doing a build.

So in any subdirectory of workspace the module will be active.

In the workspace directory, run:

The Go command includes all the modules in the workspace as main modules. This allows us to refer to a package in t

*[Content truncated - see full docs]*

**Examples**:

```text
C:\> cd %HOMEPATH%
```

```text
$ mkdir workspace
$ cd workspace
```

```text
$ mkdir hello
$ cd hello
$ go mod init example.com/hello
go: creating new go.mod: module example.com/hello
```

---

## Tutorials

**URL**: https://go.dev/doc/tutorial/index.html

**Contents**:
- Tutorials

If you're new to a part of Go, take a look at the tutorials linked below.

If you haven't installed Go yet, see Download and install.

---

## Tutorials

**URL**: https://go.dev/doc/tutorial/

**Contents**:
- Tutorials

If you're new to a part of Go, take a look at the tutorials linked below.

If you haven't installed Go yet, see Download and install.

---

## Using prepared statements

**URL**: https://go.dev/doc/database/prepared-statements

**Contents**:
- Using prepared statements
  - What is a prepared statement?
  - How you use prepared statements
  - Prepared statement behavior
    - Functions for creating a prepared statement

You can define a prepared statement for repeated use. This can help your code run a bit faster by avoiding the overhead of re-creating the statement each time your code performs the database operation.

Note: Parameter placeholders in prepared statements vary depending on the DBMS and driver you’re using. For example, the pq driver for Postgres requires a placeholder like $1 instead of ?.

A prepared statement is SQL that is parsed and saved by the DBMS, typically containing placeholders but with no actual parameter values. Later, the statement can be executed with a set of parameter values.

When you expect to execute the same SQL repeatedly, you can use an sql.Stmt to prepare the SQL statement in advance, then execute it as needed.

The following example creates a prepared statement that selects a specific album from the database. DB.Prepare returns an sql.Stmt representing a prepared statement for a given SQL text. You can pass the parameters for the SQL statement to Stmt.Exec, Stmt.QueryRow, or Stmt.Query to run the statement.

A prepared sql.Stmt provides the usual Exec, QueryRow, and Query methods for invoking the statement. For more on using these methods, see Querying for data and Executing SQL statements that don’t return data.

However, because an sql.Stmt already represents a preset SQL statement, its Exec, QueryRow, and Query methods take only the SQL parameter values corresponding to placeholders, omitting the SQL text.

You can define a new sql.Stmt in different ways, depending on how you will use it.

Be sure that stmt.Close is called when your code is finished with a statement. This will release any database resources (such as underlying connections) that may be associated with it. For statements that are only local variables in a function, it’s enough to defer stmt.Close().

**Examples**:

```javascript
// AlbumByID retrieves the specified album.
func AlbumByID(id int) (Album, error) {
    // Define a prepared statement. You'd typically define the statement
    // elsewhere and save it for use in functions such as this one.
    stmt, err := db.Prepare("SELECT * FROM album WHERE id = ?")
    if err != nil {
        log.Fatal(err)
    }
    defer stmt.Close()

    var album Album

    // Execute the prepared statement, passing in an id value for the
    // parameter whose placeholder is ?
    err
...
```

---

## Writing Web Applications

**URL**: https://go.dev/doc/articles/wiki/

**Contents**:
- Writing Web Applications
- Introduction
- Getting Started
- Data Structures
- Introducing the net/http package (an interlude)
- Using net/http to serve wiki pages
- Editing Pages
- The html/template package

Covered in this tutorial:

At present, you need to have a FreeBSD, Linux, macOS, or Windows machine to run Go. We will use $ to represent the command prompt.

Install Go (see the Installation Instructions).

Make a new directory for this tutorial inside your GOPATH and cd to it:

Create a file named wiki.go, open it in your favorite editor, and add the following lines:

We import the fmt and os packages from the Go standard library. Later, as we implement additional functionality, we will add more packages to this import declaration.

Let's start by defining the data structures. A wiki consists of a series of interconnected pages, each of which has a title and a body (the page content). Here, we define Page as a struct with two fields representing the title and body.

The type []byte means "a byte slice". (See Slices: usage and internals for more on slices.) The Body element is a []byte rather than string because that is the type expected by the io libraries we will use, as you'll see below.

The Page struct describes how page data will be stored in memory. But what about persistent storage? We can address that by creating a save method on Page:

This method's signature reads: "This is a method named save that takes as its receiver p, a pointer to Page . It takes no parameters, and returns a value of type error."

This method will save the Page's Body to a text file. For simplicity, we will use the Title as the file name.

The save method returns an error value because that is the return type of WriteFile (a standard library function that writes a byte slice to a file). The save method returns the error value, to let the application handle it should anything go wrong while writing the file. If all goes well, Page.save() will return nil (the zero-value for pointers, interfaces, and some other types).

The octal integer literal 0600, passed as the third parameter to WriteFile, indicates that the file should be created with read-write permissions for the current user o

*[Content truncated - see full docs]*

---

## 

**URL**: https://go.dev/doc/gopher/modelsheet.jpg

---

## /doc/articles/

**URL**: https://go.dev/doc/articles/

**Contents**:
- /doc/articles/

See the Documents page and the Blog index for a complete list of Go articles.

---

## go.mod file reference

**URL**: https://go.dev/doc/modules/gomod-ref

**Contents**:
- go.mod file reference
- Example
- module
  - Syntax
  - Examples
  - Notes
- go
  - Syntax

Each Go module is defined by a go.mod file that describes the module’s properties, including its dependencies on other modules and on versions of Go.

These properties include:

Go generates a go.mod file when you run the go mod init command. The following example creates a go.mod file, setting the module’s module path to example/mymodule:

Use go commands to manage dependencies. The commands ensure that the requirements described in your go.mod file remain consistent and the content of your go.mod file is valid. These commands include the go get and go mod tidy and go mod edit commands.

For reference on go commands, see Command go. You can get help from the command line by typing go help command-name, as with go help mod tidy.

A go.mod file includes directives as shown in the following example. These are described elsewhere in this topic.

Declares the module’s module path, which is the module’s unique identifier (when combined with the module version number). The module path becomes the import prefix for all packages the module contains.

For more, see module directive in the Go Modules Reference.

The following examples substitute example.com for a repository domain from which the module could be downloaded.

The module path must uniquely identify your module. For most modules, the path is a URL where the go command can find the code (or a redirect to the code). For modules that won’t ever be downloaded directly, the module path can be just some name you control that will ensure uniqueness. The prefix example/ is also reserved for use in examples like these.

For more details, see Managing dependencies.

In practice, the module path is typically the module source’s repository domain and path to the module code within the repository. The go command relies on this form when downloading module versions to resolve dependencies on the module user’s behalf.

Even if you’re not at first intending to make your module available for use from other code, using its reposit

*[Content truncated - see full docs]*

**Examples**:

```text
$ go mod init example/mymodule
```

```javascript
module example.com/mymodule

go 1.14

require (
    example.com/othermodule v1.2.3
    example.com/thismodule v1.2.3
    example.com/thatmodule v1.2.3
)

replace example.com/thatmodule => ../thatmodule
exclude example.com/thismodule v1.3.0
```

```text
module example.com/mymodule
```

---
