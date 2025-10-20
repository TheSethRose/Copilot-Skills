# Better-Auth - Introduction

**Pages**: 2

---

## Introduction | Better Auth

**URL**: https://www.better-auth.com/docs/introduction

**Contents**:
- Introduction
- Features
- AI tooling
  - LLMs.txt
  - MCP
    - CLI Options
    - Manual Configuration
  - On this page

get started, concepts, and plugins

Search documentation...

Better Auth is a framework-agnostic, universal authentication and authorization framework for TypeScript. It provides a comprehensive set of features out of the box and includes a plugin ecosystem that simplifies adding advanced functionalities. Whether you need 2FA, passkey, multi-tenancy, multi-session support, or even enterprise features like SSO, creating your own IDP, it lets you focus on building your application instead of reinventing the wheel.

Better Auth aims to be the most comprehensive auth library. It provides a wide range of features out of the box and allows you to extend it with plugins. Here are some of the features:

Support for most popular frameworks

Built-in support for secure email and password authentication

Account & Session Management

Manage user accounts and sessions with ease

Built-In Rate Limiter

Built-in rate limiter with custom rules

Automatic Database Management

Automatic database management and migrations

Multiple social sign-on providers

Organization & Access Control

Manage organizations and access control

Two Factor Authentication

Secure your users with two factor authentication

Even more capabilities with plugins

Better Auth exposes an LLMs.txt that helps AI models understand how to integrate and interact with your authentication system. See it at https://better-auth.com/llms.txt.

Better Auth provides an MCP server so you can use it with any AI model that supports the Model Context Protocol (MCP).

Use the Better Auth CLI to easily add the MCP server to your preferred client:

Alternatively, you can manually configure the MCP server for each client:

We provide a first‑party MCP, powered by Chonkie. You can alternatively use context7 and other MCP providers.

**Examples**:

```text
pnpm @better-auth/cli mcp --cursor
```

```text
pnpm @better-auth/cli mcp --cursor
```

```text
pnpm @better-auth/cli mcp --claude-code
```

---

## Introduction | Better Auth

**URL**: https://www.better-auth.com/docs

**Contents**:
- Introduction
- Features
- AI tooling
  - LLMs.txt
  - MCP
    - CLI Options
    - Manual Configuration
  - On this page

get started, concepts, and plugins

Search documentation...

Better Auth is a framework-agnostic, universal authentication and authorization framework for TypeScript. It provides a comprehensive set of features out of the box and includes a plugin ecosystem that simplifies adding advanced functionalities. Whether you need 2FA, passkey, multi-tenancy, multi-session support, or even enterprise features like SSO, creating your own IDP, it lets you focus on building your application instead of reinventing the wheel.

Better Auth aims to be the most comprehensive auth library. It provides a wide range of features out of the box and allows you to extend it with plugins. Here are some of the features:

Support for most popular frameworks

Built-in support for secure email and password authentication

Account & Session Management

Manage user accounts and sessions with ease

Built-In Rate Limiter

Built-in rate limiter with custom rules

Automatic Database Management

Automatic database management and migrations

Multiple social sign-on providers

Organization & Access Control

Manage organizations and access control

Two Factor Authentication

Secure your users with two factor authentication

Even more capabilities with plugins

Better Auth exposes an LLMs.txt that helps AI models understand how to integrate and interact with your authentication system. See it at https://better-auth.com/llms.txt.

Better Auth provides an MCP server so you can use it with any AI model that supports the Model Context Protocol (MCP).

Use the Better Auth CLI to easily add the MCP server to your preferred client:

Alternatively, you can manually configure the MCP server for each client:

We provide a first‑party MCP, powered by Chonkie. You can alternatively use context7 and other MCP providers.

**Examples**:

```text
pnpm @better-auth/cli mcp --cursor
```

```text
pnpm @better-auth/cli mcp --cursor
```

```text
pnpm @better-auth/cli mcp --claude-code
```

---
