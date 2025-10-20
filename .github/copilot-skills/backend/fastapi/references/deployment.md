# Fastapi - Deployment

**Pages**: 7

---

## About FastAPI versions - FastAPI

**URL**: https://fastapi.tiangolo.com/deployment/versions/

**Contents**:
- About FastAPI versions¶
- Pin your fastapi version¶
- Available versions¶
- About versions¶
- Upgrading the FastAPI versions¶
- About Starlette¶
- About Pydantic¶

FastAPI is already being used in production in many applications and systems. And the test coverage is kept at 100%. But its development is still moving quickly.

New features are added frequently, bugs are fixed regularly, and the code is still continuously improving.

That's why the current versions are still 0.x.x, this reflects that each version could potentially have breaking changes. This follows the Semantic Versioning conventions.

You can create production applications with FastAPI right now (and you have probably been doing it for some time), you just have to make sure that you use a version that works correctly with the rest of your code.

The first thing you should do is to "pin" the version of FastAPI you are using to the specific latest version that you know works correctly for your application.

For example, let's say you are using version 0.112.0 in your app.

If you use a requirements.txt file you could specify the version with:

that would mean that you would use exactly the version 0.112.0.

Or you could also pin it with:

that would mean that you would use the versions 0.112.0 or above, but less than 0.113.0, for example, a version 0.112.2 would still be accepted.

If you use any other tool to manage your installations, like uv, Poetry, Pipenv, or others, they all have a way that you can use to define specific versions for your packages.

You can see the available versions (e.g. to check what is the current latest) in the Release Notes.

Following the Semantic Versioning conventions, any version below 1.0.0 could potentially add breaking changes.

FastAPI also follows the convention that any "PATCH" version change is for bug fixes and non-breaking changes.

The "PATCH" is the last number, for example, in 0.2.3, the PATCH version is 3.

So, you should be able to pin to a version like:

Breaking changes and new features are added in "MINOR" versions.

The "MINOR" is the number in the middle, for example, in 0.2.3, the MINOR version is 2.

You shoul

*[Content truncated - see full docs]*

**Examples**:

```text
fastapi[standard]==0.112.0
```

```text
fastapi[standard]>=0.112.0,<0.113.0
```

```text
fastapi>=0.45.0,<0.46.0
```

---

## About HTTPS - FastAPI

**URL**: https://fastapi.tiangolo.com/deployment/https/

**Contents**:
- About HTTPS¶
- Let's Encrypt¶
- HTTPS for Developers¶
  - Domain Name¶
  - DNS¶
  - TLS Handshake Start¶
  - TLS with SNI Extension¶
  - HTTPS Request¶

It is easy to assume that HTTPS is something that is just "enabled" or not.

But it is way more complex than that.

If you are in a hurry or don't care, continue with the next sections for step by step instructions to set everything up with different techniques.

To learn the basics of HTTPS, from a consumer perspective, check https://howhttps.works/.

Now, from a developer's perspective, here are several things to keep in mind while thinking about HTTPS:

It is a common practice to have one program/HTTP server running on the server (the machine, host, etc.) and managing all the HTTPS parts: receiving the encrypted HTTPS requests, sending the decrypted HTTP requests to the actual HTTP application running in the same server (the FastAPI application, in this case), take the HTTP response from the application, encrypt it using the appropriate HTTPS certificate and sending it back to the client using HTTPS. This server is often called a TLS Termination Proxy.

Some of the options you could use as a TLS Termination Proxy are:

Before Let's Encrypt, these HTTPS certificates were sold by trusted third parties.

The process to acquire one of these certificates used to be cumbersome, require quite some paperwork and the certificates were quite expensive.

But then Let's Encrypt was created.

It is a project from the Linux Foundation. It provides HTTPS certificates for free, in an automated way. These certificates use all the standard cryptographic security, and are short-lived (about 3 months), so the security is actually better because of their reduced lifespan.

The domains are securely verified and the certificates are generated automatically. This also allows automating the renewal of these certificates.

The idea is to automate the acquisition and renewal of these certificates so that you can have secure HTTPS, for free, forever.

Here's an example of how an HTTPS API could look like, step by step, paying attention mainly to the ideas important for developers.

It would

*[Content truncated - see full docs]*

---

## Deploy FastAPI on Cloud Providers - FastAPI

**URL**: https://fastapi.tiangolo.com/deployment/cloud/

**Contents**:
- Deploy FastAPI on Cloud Providers¶
- Cloud Providers - Sponsors¶

You can use virtually any cloud provider to deploy your FastAPI application.

In most of the cases, the main cloud providers have guides to deploy FastAPI with them.

Some cloud providers ✨ sponsor FastAPI ✨, this ensures the continued and healthy development of FastAPI and its ecosystem.

And it shows their true commitment to FastAPI and its community (you), as they not only want to provide you a good service but also want to make sure you have a good and healthy framework, FastAPI. 🙇

You might want to try their services and follow their guides:

---

## Deployment - FastAPI

**URL**: https://fastapi.tiangolo.com/deployment/

**Contents**:
- Deployment¶
- What Does Deployment Mean¶
- Deployment Strategies¶

Deploying a FastAPI application is relatively easy.

To deploy an application means to perform the necessary steps to make it available to the users.

For a web API, it normally involves putting it in a remote machine, with a server program that provides good performance, stability, etc, so that your users can access the application efficiently and without interruptions or problems.

This is in contrast to the development stages, where you are constantly changing the code, breaking it and fixing it, stopping and restarting the development server, etc.

There are several ways to do it depending on your specific use case and the tools that you use.

You could deploy a server yourself using a combination of tools, you could use a cloud service that does part of the work for you, or other possible options.

I will show you some of the main concepts you should probably keep in mind when deploying a FastAPI application (although most of it applies to any other type of web application).

You will see more details to keep in mind and some of the techniques to do it in the next sections. ✨

---

## Deployments Concepts - FastAPI

**URL**: https://fastapi.tiangolo.com/deployment/concepts/

**Contents**:
- Deployments Concepts¶
- Security - HTTPS¶
  - Example Tools for HTTPS¶
- Program and Process¶
  - What is a Program¶
  - What is a Process¶
- Running on Startup¶
  - In a Remote Server¶

When deploying a FastAPI application, or actually, any type of web API, there are several concepts that you probably care about, and using them you can find the most appropriate way to deploy your application.

Some of the important concepts are:

We'll see how they would affect deployments.

In the end, the ultimate objective is to be able to serve your API clients in a way that is secure, to avoid disruptions, and to use the compute resources (for example remote servers/virtual machines) as efficiently as possible. 🚀

I'll tell you a bit more about these concepts here, and that would hopefully give you the intuition you would need to decide how to deploy your API in very different environments, possibly even in future ones that don't exist yet.

By considering these concepts, you will be able to evaluate and design the best way to deploy your own APIs.

In the next chapters, I'll give you more concrete recipes to deploy FastAPI applications.

But for now, let's check these important conceptual ideas. These concepts also apply to any other type of web API. 💡

In the previous chapter about HTTPS we learned about how HTTPS provides encryption for your API.

We also saw that HTTPS is normally provided by a component external to your application server, a TLS Termination Proxy.

And there has to be something in charge of renewing the HTTPS certificates, it could be the same component or it could be something different.

Some of the tools you could use as a TLS Termination Proxy are:

Another option is that you could use a cloud service that does more of the work including setting up HTTPS. It could have some restrictions or charge you more, etc. But in that case, you wouldn't have to set up a TLS Termination Proxy yourself.

I'll show you some concrete examples in the next chapters.

Then the next concepts to consider are all about the program running your actual API (e.g. Uvicorn).

We will talk a lot about the running "process", so it's useful to have clarity about w

*[Content truncated - see full docs]*

---

## Run a Server Manually - FastAPI

**URL**: https://fastapi.tiangolo.com/deployment/manually/

**Contents**:
- Run a Server Manually¶
- Use the fastapi run Command¶
- ASGI Servers¶
- Server Machine and Server Program¶
- Install the Server Program¶
- Run the Server Program¶
- Deployment Concepts¶

In short, use fastapi run to serve your FastAPI application:

That would work for most of the cases. 😎

You could use that command for example to start your FastAPI app in a container, in a server, etc.

Let's go a little deeper into the details.

FastAPI uses a standard for building Python web frameworks and servers called ASGI. FastAPI is an ASGI web framework.

The main thing you need to run a FastAPI application (or any other ASGI application) in a remote server machine is an ASGI server program like Uvicorn, this is the one that comes by default in the fastapi command.

There are several alternatives, including:

There's a small detail about names to keep in mind. 💡

The word "server" is commonly used to refer to both the remote/cloud computer (the physical or virtual machine) and also the program that is running on that machine (e.g. Uvicorn).

Just keep in mind that when you read "server" in general, it could refer to one of those two things.

When referring to the remote machine, it's common to call it server, but also machine, VM (virtual machine), node. Those all refer to some type of remote machine, normally running Linux, where you run programs.

When you install FastAPI, it comes with a production server, Uvicorn, and you can start it with the fastapi run command.

But you can also install an ASGI server manually.

Make sure you create a virtual environment, activate it, and then you can install the server application.

For example, to install Uvicorn:

A similar process would apply to any other ASGI server program.

By adding the standard, Uvicorn will install and use some recommended extra dependencies.

That including uvloop, the high-performance drop-in replacement for asyncio, that provides the big concurrency performance boost.

When you install FastAPI with something like pip install "fastapi[standard]" you already get uvicorn[standard] as well.

If you installed an ASGI server manually, you would normally need to pass an import string in a speci

*[Content truncated - see full docs]*

**Examples**:

```python
$ <font color="#4E9A06">fastapi</font> run <u style="text-decoration-style:solid">main.py</u>

  <span style="background-color:#009485"><font color="#D3D7CF"> FastAPI </font></span>  Starting production server 🚀

             Searching for package file structure from directories
             with <font color="#3465A4">__init__.py</font> files
             Importing from <font color="#75507B">/home/user/code/</font><font color="#AD7FA8">awesomeapp</font>

   <span style="background-color:#007166"
...
```

```text
$ pip install "uvicorn[standard]"

---> 100%
```

```text
$ uvicorn main:app --host 0.0.0.0 --port 80

<span style="color: green;">INFO</span>:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)
```

---

## Server Workers - Uvicorn with Workers - FastAPI

**URL**: https://fastapi.tiangolo.com/deployment/server-workers/

**Contents**:
- Server Workers - Uvicorn with Workers¶
- Multiple Workers¶
- Deployment Concepts¶
- Containers and Docker¶
- Recap¶

Let's check back those deployment concepts from before:

Up to this point, with all the tutorials in the docs, you have probably been running a server program, for example, using the fastapi command, that runs Uvicorn, running a single process.

When deploying applications you will probably want to have some replication of processes to take advantage of multiple cores and to be able to handle more requests.

As you saw in the previous chapter about Deployment Concepts, there are multiple strategies you can use.

Here I'll show you how to use Uvicorn with worker processes using the fastapi command or the uvicorn command directly.

If you are using containers, for example with Docker or Kubernetes, I'll tell you more about that in the next chapter: FastAPI in Containers - Docker.

In particular, when running on Kubernetes you will probably not want to use workers and instead run a single Uvicorn process per container, but I'll tell you about it later in that chapter.

You can start multiple workers with the --workers command line option:

If you use the fastapi command:

If you prefer to use the uvicorn command directly:

The only new option here is --workers telling Uvicorn to start 4 worker processes.

You can also see that it shows the PID of each process, 27365 for the parent process (this is the process manager) and one for each worker process: 27368, 27369, 27370, and 27367.

Here you saw how to use multiple workers to parallelize the execution of the application, take advantage of multiple cores in the CPU, and be able to serve more requests.

From the list of deployment concepts from above, using workers would mainly help with the replication part, and a little bit with the restarts, but you still need to take care of the others:

In the next chapter about FastAPI in Containers - Docker I'll explain some strategies you could use to handle the other deployment concepts.

I'll show you how to build your own image from scratch to run a single Uvicorn process. It 

*[Content truncated - see full docs]*

**Examples**:

```python
$ <font color="#4E9A06">fastapi</font> run --workers 4 <u style="text-decoration-style:solid">main.py</u>

  <span style="background-color:#009485"><font color="#D3D7CF"> FastAPI </font></span>  Starting production server 🚀

             Searching for package file structure from directories with
             <font color="#3465A4">__init__.py</font> files
             Importing from <font color="#75507B">/home/user/code/</font><font color="#AD7FA8">awesomeapp</font>

   <span style="background-co
...
```

```text
$ uvicorn main:app --host 0.0.0.0 --port 8080 --workers 4
<font color="#A6E22E">INFO</font>:     Uvicorn running on <b>http://0.0.0.0:8080</b> (Press CTRL+C to quit)
<font color="#A6E22E">INFO</font>:     Started parent process [<font color="#A1EFE4"><b>27365</b></font>]
<font color="#A6E22E">INFO</font>:     Started server process [<font color="#A1EFE4">27368</font>]
<font color="#A6E22E">INFO</font>:     Waiting for application startup.
<font color="#A6E22E">INFO</font>:     Application startu
...
```

---
