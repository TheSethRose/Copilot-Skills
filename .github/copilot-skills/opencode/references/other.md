# Opencode - Other

**Pages**: 16

---

## Commands | opencode

**URL**: https://opencode.ai/docs/commands

**Contents**:
- Commands
- Create command files
- Configure
  - JSON
  - Markdown
- Prompt config
  - Arguments
  - Shell output

Create custom commands for repetitive tasks.

Custom commands let you specify a prompt you want to run when that command is executed in the TUI.

Custom commands are in addition to the built-in commands like /init, /undo, /redo, /share, /help. Learn more.

Create markdown files in the command/ directory to define custom commands.

Create .opencode/command/test.md:

The frontmatter defines command properties. The content becomes the template.

Use the command by typing / followed by the command name.

You can add custom commands through the OpenCode config or by creating markdown files in the command/ directory.

Use the command option in your OpenCode config:

Now you can run this command in the TUI:

You can also define commands using markdown files. Place them in:

The markdown file name becomes the command name. For example, test.md lets you run:

The prompts for the custom commands support several special placeholders and syntax.

Pass arguments to commands using the $ARGUMENTS placeholder.

Run the command with arguments:

And $ARGUMENTS will be replaced with Button.

Use !command to inject bash command output into your prompt.

For example, to create a custom command that analyzes test coverage:

Or to review recent changes:

Commands run in your project’s root directory and their output becomes part of the prompt.

Include files in your command using @ followed by the filename.

The file content gets included in the prompt automatically.

Let’s look at the configuration options in detail.

The template option defines the prompt that will be sent to the LLM when the command is executed.

This is a required config option.

Use the description option to provide a brief description of what the command does.

This is shown as the description in the TUI when you type in the command.

Use the agent config to optionally specify which agent should execute this command. If this is a subagent the command will trigger a subagent invocation by default. To disable this beh

*[Content truncated - see full docs]*

**Examples**:

```text
/my-command
```

```text
---description: Run tests with coverageagent: buildmodel: anthropic/claude-3-5-sonnet-20241022---
Run the full test suite with coverage report and show any failures.Focus on the failing tests and suggest fixes.
```

```text
{  "$schema": "https://opencode.ai/config.json",  "command": {    // This becomes the name of the command    "test": {      // This is the prompt that will be sent to the LLM      "template": "Run the full test suite with coverage report and show any failures.\nFocus on the failing tests and suggest fixes.",      // This is show as the description in the TUI      "description": "Run tests with coverage",      "agent": "build",      "model": "anthropic/claude-3-5-sonnet-20241022"    }  }}
```

---

## Config | opencode

**URL**: https://opencode.ai/docs/config

**Contents**:
- Config
- Format
- Locations
  - Global
  - Per project
  - Custom path
- Schema
  - TUI

Using the OpenCode JSON config.

You can configure OpenCode using a JSON config file.

OpenCode supports both JSON and JSONC (JSON with Comments) formats.

You can place your config in a couple of different locations and they have a different order of precedence.

Place your global OpenCode config in ~/.config/opencode/opencode.json. You’ll want to use the global config for things like themes, providers, or keybinds.

You can also add a opencode.json in your project. It takes precedence over the global config. This is useful for configuring providers or modes specific to your project.

Place project specific config in the root of your project.

When OpenCode starts up, it looks for a config file in the current directory or traverse up to the nearest Git directory.

This is also safe to be checked into Git and uses the same schema as the global one.

You can also specify a custom config file path using the OPENCODE_CONFIG environment variable. This takes precedence over the global and project configs.

The config file has a schema that’s defined in opencode.ai/config.json.

Your editor should be able to validate and autocomplete based on the schema.

You can configure TUI-specific settings through the tui option.

Learn more about using the TUI here.

You can manage the tools an LLM can use through the tools option.

Learn more about tools here.

You can configure the providers and models you want to use in your OpenCode config through the provider, model and small_model options.

The small_model option configures a separate model for lightweight tasks like title generation. By default, OpenCode tries to use a cheaper model if one is available from your provider, otherwise it falls back to your main model.

You can also configure local models. Learn more.

You can configure the theme you want to use in your OpenCode config through the theme option.

You can configure specialized agents for specific tasks through the agent option.

You can also define agents using mar

*[Content truncated - see full docs]*

**Examples**:

```text
{  "$schema": "https://opencode.ai/config.json",  // Theme configuration  "theme": "opencode",  "model": "anthropic/claude-sonnet-4-20250514",  "autoupdate": true,}
```

```text
export OPENCODE_CONFIG=/path/to/my/custom-config.jsonopencode run "Hello world"
```

```text
{  "$schema": "https://opencode.ai/config.json",  "tui": {    "scroll_speed": 3  }}
```

---

## Enterprise | opencode

**URL**: https://opencode.ai/docs/enterprise

**Contents**:
- Enterprise
- Trial
  - Data handling
    - Sharing conversations
  - Code ownership
- Deployment
  - SSO
  - Private NPM

Using OpenCode in your organization.

OpenCode does not store any of your code or context data. This makes it easy for you to use OpenCode at your organization.

To get started, we recommend:

Since OpenCode is open source and does not store any of your code or context data, your developers can simply get started and carry out a trial.

opencode does not store your code or context data. All processing happens locally or through direct API calls to your AI provider.

The only caveat here is the optional /share feature.

If a user enables the /share feature, the conversation and the data associated with it are sent to the service we use to host these shares pages at opencode.ai.

The data is currently served through our CDN’s edge network, and is cached on the edge near your users.

We recommend you disable this for your trial.

Learn more about sharing.

You own all code produced by opencode. There are no licensing restrictions or ownership claims.

Once you have completed your trial and you are ready to self-host opencode at your organization, you can contact us to discuss pricing and implementation options.

SSO integration can be implemented for enterprise deployments after your trial. This will allow your team’s session data and shared conversations to be protected by your enterprise’s authentication system.

opencode supports private npm registries through Bun’s native .npmrc file support. If your organization uses a private registry, such as JFrog Artifactory, Nexus, or similar, ensure developers are authenticated before running opencode.

To set up authentication with your private registry:

This creates ~/.npmrc with authentication details. opencode will automatically pick this up.

You must be logged into the private registry before running opencode.

Alternatively, you can manually configure a .npmrc file:

Developers must be logged into the private registry before running opencode to ensure packages can be installed from your enterprise registry.

The shar

*[Content truncated - see full docs]*

**Examples**:

```text
{  "$schema": "https://opencode.ai/config.json",  "share": "disabled"}
```

```text
npm login --registry=https://your-company.jfrog.io/api/npm/npm-virtual/
```

```text
registry=https://your-company.jfrog.io/api/npm/npm-virtual///your-company.jfrog.io/api/npm/npm-virtual/:_authToken=${NPM_AUTH_TOKEN}
```

---

## Formatters | opencode

**URL**: https://opencode.ai/docs/formatters

**Contents**:
- Formatters
- Built-in
- How it works
- Configure
  - Disabling formatters
  - Custom formatters

OpenCode uses language specific formatters.

OpenCode automatically formats files after they are written or edited using language-specific formatters. This ensures that the code that is generated follows the code styles of your project.

OpenCode comes with several built-in formatters for popular languages and frameworks. Below is a list of the formatters, supported file extensions, and commands or config options it needs.

So if your project has prettier in your package.json, OpenCode will automatically use it.

When OpenCode writes or edits a file, it:

This process happens in the background, ensuring your code styles are maintained without any manual steps.

You can customize formatters through the formatter section in your OpenCode config.

Each formatter configuration supports the following:

Let’s look at some examples.

To disable a specific formatter, set disabled to true:

You can override the built-in formatters or add new ones by specifying the command, environment variables, and file extensions:

The $FILE placeholder in the command will be replaced with the path to the file being formatted.

**Examples**:

```text
{  "$schema": "https://opencode.ai/config.json",  "formatter": {}}
```

```text
{  "$schema": "https://opencode.ai/config.json",  "formatter": {    "prettier": {      "disabled": true    }  }}
```

```typescript
{  "$schema": "https://opencode.ai/config.json",  "formatter": {    "prettier": {      "command": ["npx", "prettier", "--write", "$FILE"],      "environment": {        "NODE_ENV": "development"      },      "extensions": [".js", ".ts", ".jsx", ".tsx"]    },    "custom-markdown-formatter": {      "command": ["deno", "fmt", "$FILE"],      "extensions": [".md"]    }  }}
```

---

## Intro | opencode

**URL**: https://opencode.ai/docs

**Contents**:
- Intro
    - Prerequisites
- Install
    - Windows
- Configure
- Initialize
- Usage
  - Ask questions

Get started with OpenCode.

OpenCode is an AI coding agent built for the terminal.

To use OpenCode, you’ll need:

A modern terminal emulator like:

API keys for the LLM providers you want to use.

The easiest way to install OpenCode is through the install script.

You can also install it with the following commands:

Using Homebrew on macOS and Linux

Using Paru on Arch Linux

Support for installing OpenCode on Windows using Bun is currently in progress.

You can also grab the binary from the Releases.

With OpenCode you can use any LLM provider by configuring their API keys.

If you are new to using LLM providers, we recommend using OpenCode Zen. It’s a curated list of models that have been tested and verified by the OpenCode team.

Run opencode auth login, select opencode, and head to opencode.ai/auth.

Sign in, add your billing details, and copy your API key.

Alternatively, you can select one of the other providers. Learn more.

Now that you’ve configured a provider, you can navigate to a project that you want to work on.

Next, initialize OpenCode for the project by running the following command.

This will get OpenCode to analyze your project and create an AGENTS.md file in the project root.

You should commit your project’s AGENTS.md file to Git.

This helps OpenCode understand the project structure and the coding patterns used.

You are now ready to use OpenCode to work on your project. Feel free to ask it anything!

If you are new to using an AI coding agent, here are some examples that might help.

You can ask OpenCode to explain the codebase to you.

Use the @ key to fuzzy search for files in the project.

This is helpful if there’s a part of the codebase that you didn’t work on.

You can ask OpenCode to add new features to your project. Though we first recommend asking it to create a plan.

OpenCode has a Plan mode that disables its ability to make changes and instead suggest how it’ll implement the feature.

Switch to it using the Tab key. You’ll see a

*[Content truncated - see full docs]*

**Examples**:

```text
curl -fsSL https://opencode.ai/install | bash
```

```text
npm install -g opencode-ai
```

```text
bun install -g opencode-ai
```

---

## Intro | opencode

**URL**: https://opencode.ai/docs/

**Contents**:
- Intro
    - Prerequisites
- Install
    - Windows
- Configure
- Initialize
- Usage
  - Ask questions

Get started with OpenCode.

OpenCode is an AI coding agent built for the terminal.

To use OpenCode, you’ll need:

A modern terminal emulator like:

API keys for the LLM providers you want to use.

The easiest way to install OpenCode is through the install script.

You can also install it with the following commands:

Using Homebrew on macOS and Linux

Using Paru on Arch Linux

Support for installing OpenCode on Windows using Bun is currently in progress.

You can also grab the binary from the Releases.

With OpenCode you can use any LLM provider by configuring their API keys.

If you are new to using LLM providers, we recommend using OpenCode Zen. It’s a curated list of models that have been tested and verified by the OpenCode team.

Run opencode auth login, select opencode, and head to opencode.ai/auth.

Sign in, add your billing details, and copy your API key.

Alternatively, you can select one of the other providers. Learn more.

Now that you’ve configured a provider, you can navigate to a project that you want to work on.

Next, initialize OpenCode for the project by running the following command.

This will get OpenCode to analyze your project and create an AGENTS.md file in the project root.

You should commit your project’s AGENTS.md file to Git.

This helps OpenCode understand the project structure and the coding patterns used.

You are now ready to use OpenCode to work on your project. Feel free to ask it anything!

If you are new to using an AI coding agent, here are some examples that might help.

You can ask OpenCode to explain the codebase to you.

Use the @ key to fuzzy search for files in the project.

This is helpful if there’s a part of the codebase that you didn’t work on.

You can ask OpenCode to add new features to your project. Though we first recommend asking it to create a plan.

OpenCode has a Plan mode that disables its ability to make changes and instead suggest how it’ll implement the feature.

Switch to it using the Tab key. You’ll see a

*[Content truncated - see full docs]*

**Examples**:

```text
curl -fsSL https://opencode.ai/install | bash
```

```text
npm install -g opencode-ai
```

```text
bun install -g opencode-ai
```

---

## Keybinds | opencode

**URL**: https://opencode.ai/docs/keybinds

**Contents**:
- Keybinds
- Leader key
- Disable keybind

Customize your keybinds.

OpenCode has a list of keybinds that you can customize through the OpenCode config.

OpenCode uses a leader key for most keybinds. This avoids conflicts in your terminal.

By default, ctrl+x is the leader key and most actions require you to first press the leader key and then the shortcut. For example, to start a new session you first press ctrl+x and then press n.

You don’t need to use a leader key for your keybinds but we recommend doing so.

You can disable a keybind by adding the key to your config with a value of “none”.

**Examples**:

```text
{  "$schema": "https://opencode.ai/config.json",  "keybinds": {    "leader": "ctrl+x",    "app_help": "<leader>h",    "app_exit": "ctrl+c,<leader>q",    "editor_open": "<leader>e",    "theme_list": "<leader>t",    "project_init": "<leader>i",    "tool_details": "<leader>d",    "thinking_blocks": "<leader>b",    "session_export": "<leader>x",    "session_new": "<leader>n",    "session_list": "<leader>l",    "session_share": "<leader>s",    "session_unshare": "none",    "session_interrupt": "esc",
...
```

```text
{  "$schema": "https://opencode.ai/config.json",  "keybinds": {    "session_compact": "none"  }}
```

---

## MCP servers | opencode

**URL**: https://opencode.ai/docs/mcp-servers

**Contents**:
- MCP servers
- Caveats
- Configure
  - Local
    - Options
  - Remote
    - Options
- Manage

Add local and remote MCP tools.

You can add external tools to OpenCode using the Model Context Protocol, or MCP.

OpenCode supports both:

Once added, MCP tools are automatically available to the LLM alongside built-in tools.

OAuth support for MCP servers is coming soon.

When you use an MCP server, it adds to the context. This can quickly add up if you have a lot of tools. So we recommend being careful with which MCP servers you use.

MCP servers add to your context, so you want to be careful with which ones you enable.

Certain MCP servers, like the GitHub MCP server tend to add a lot of tokens and can easily exceed the context limit.

You can define MCP servers in your OpenCode config under mcp. Add each MCP with a unique name. You can refer to that MCP by name when prompting the LLM.

You can also disable a server by setting enabled to false. This is useful if you want to temporarily disable a server without removing it from your config.

Add local MCP servers using type to "local" within the MCP object.

The command is how the local MCP server is started. You can also pass in a list of environment variables as well.

For example, here’s how I can add the test @modelcontextprotocol/server-everything MCP server.

And to use it I can add use the mcp_everything tool to my prompts.

Here are all the options for configuring a local MCP server.

Add remote MCP servers under by setting type to "remote".

Here the url is the URL of the remote MCP server and with the headers option you can pass in a list of headers.

Your MCPs are available as tools in OpenCode, alongside built-in tools. So you can manage them through the OpenCode config like any other tool.

This means that you can enable or disable them globally.

We can also use a glob pattern to disable all matching MCPs.

Here we are using the glob pattern my-mcp* to disable all MCPs.

If you have a large number of MCP servers you may want to only enable them per agent and disable them globally. To do this:

The g

*[Content truncated - see full docs]*

**Examples**:

```text
{  "$schema": "https://opencode.ai/config.json",  "mcp": {    "name-of-mcp-server": {      // ...      "enabled": true    },    "name-of-other-mcp-server": {      // ...    }  }}
```

```text
{  "$schema": "https://opencode.ai/config.json",  "mcp": {    "my-local-mcp-server": {      "type": "local",      // Or ["bun", "x", "my-mcp-command"]      "command": ["npx", "-y", "my-mcp-command"],      "enabled": true,      "environment": {        "MY_ENV_VAR": "my_env_var_value"      }    }  }}
```

```text
{  "$schema": "https://opencode.ai/config.json",  "mcp": {    "mcp_everything": {      "type": "local",      "command": ["npx", "-y", "@modelcontextprotocol/server-everything"],    }  }}
```

---

## Models | opencode

**URL**: https://opencode.ai/docs/models

**Contents**:
- Models
- Providers
- Select a model
- Recommended models
- Set a default
- Configure models
- Loading models

Configuring an LLM provider and model.

OpenCode uses the AI SDK and Models.dev to support for 75+ LLM providers and it supports running local models.

Most popular providers are preloaded by default. If you’ve added the credentials for a provider through opencode auth login, they’ll be available when you start OpenCode.

Learn more about providers.

Once you’ve configured your provider you can select the model you want by typing in:

There are a lot of models out there, with new models coming out every week.

Consider using one of the models we recommend.

However, there are only a few of them that are good at both generating code and tool calling.

Here are several models, in no particular order, that work well with OpenCode (to name a few):

To set one of these as the default model, you can set the model key in your OpenCode config.

Here the full ID is provider_id/model_id.

If you’ve configured a custom provider, the provider_id is key from the provider part of your config, and the model_id is the key from provider.models.

You can globally configure a model’s options through the config.

Here we’re configuring global settings for two built-in models: gpt-5 when accessed via the openai provider, and claude-sonnet-4-20250514 when accessed via the anthropic provider. The built-in provider and model names can be found on Models.dev.

You can also configure these options for any agents that you are using. The agent config overrides any global options here. Learn more.

You can also define custom models that extend built-in ones and can optionally use specific options by referring to their id:

When OpenCode starts up, it checks for models in the following priority order:

The --model or -m command line flag. The format is the same as in the config file: provider_id/model_id.

The model list in the OpenCode config.

The format here is provider/model.

The first model using an internal priority.

**Examples**:

```text
{  "$schema": "https://opencode.ai/config.json",  "model": "lmstudio/google/gemma-3n-e4b"}
```

```text
{  "$schema": "https://opencode.ai/config.json",  "provider": {    "openai": {      "models": {        "gpt-5": {          "options": {            "reasoningEffort": "high",            "textVerbosity": "low",            "reasoningSummary": "auto",            "include": ["reasoning.encrypted_content"],          },        },      },    },    "anthropic": {      "models": {        "claude-sonnet-4-5-20250929": {          "options": {            "thinking": {              "type": "enabled",         
...
```

```text
{  "$schema": "https://opencode.ai/config.json",  "provider": {    "opencode": {      "models": {        "gpt-5-high": {          "id": "gpt-5",          "options": {            "reasoningEffort": "high",            "textVerbosity": "low",            "reasoningSummary": "auto",          },        },        "gpt-5-low": {          "id": "gpt-5",          "options": {            "reasoningEffort": "low",            "textVerbosity": "low",            "reasoningSummary": "auto",          },        }
...
```

---

## Permissions | opencode

**URL**: https://opencode.ai/docs/permissions

**Contents**:
- Permissions
- Tools
  - edit
  - bash
    - Wildcards
      - Glob patterns
  - webfetch
- Agents

Control which actions require approval to run.

By default, OpenCode allows all operations without requiring explicit approval. You can configure this using the permission option.

This lets you configure granular controls for the edit, bash, and webfetch tools.

Currently, the permissions for the edit, bash, and webfetch tools can be configured through the permission option.

Use the permission.edit key to control whether file editing operations require user approval.

You can use the permission.bash key to control whether bash commands as a whole need user approval.

Or, you can target specific commands and set it to allow, ask, or deny.

You can also use wildcards to manage permissions for specific bash commands.

You can use wildcards to manage permissions for specific bash commands.

For example, disable all Terraform commands.

You can also use the * wildcard to manage permissions for all commands. For example, deny all commands except a couple of specific ones.

Here a specific rule can override the * wildcard.

The wildcard uses simple regex globbing patterns.

Use the permission.webfetch key to control whether the LLM can fetch web pages.

You can also configure permissions per agent. Where the agent specific config overrides the global config. Learn more about agent permissions.

For example, here the build agent overrides the global bash permission to allow git push commands.

You can also configure permissions for agents in Markdown.

**Examples**:

```text
{  "$schema": "https://opencode.ai/config.json",  "permission": {    "edit": "allow",    "bash": "ask",    "webfetch": "deny"  }}
```

```text
{  "$schema": "https://opencode.ai/config.json",  "permission": {    "edit": "ask"  }}
```

```text
{  "$schema": "https://opencode.ai/config.json",  "permission": {    "bash": "ask"  }}
```

---

## Providers | opencode

**URL**: https://opencode.ai/docs/providers

**Contents**:
- Providers
  - Credentials
  - Config
    - Base URL
- OpenCode Zen
- Directory
  - Amazon Bedrock
  - Anthropic

Using any LLM provider in OpenCode.

OpenCode uses the AI SDK and Models.dev to support for 75+ LLM providers and it supports running local models.

To add a provider you need to:

When you add a provider’s API keys with opencode auth login, they are stored in ~/.local/share/opencode/auth.json.

You can customize the providers through the provider section in your OpenCode config.

You can customize the base URL for any provider by setting the baseURL option. This is useful when using proxy services or custom endpoints.

OpenCode Zen is a list of models provided by the OpenCode team that have been tested and verified to work well with OpenCode. Learn more.

If you are new, we recommend starting with OpenCode Zen.

Run opencode auth login, select opencode, and head to opencode.ai/auth.

Sign in, add your billing details, and copy your API key.

Run /models in the TUI to see the list of models we recommend.

It works like any other provider in OpenCode. And is completely optional to use it.

Let’s look at some of the providers in detail. If you’d like to add a provider to the list, feel free to open a PR.

Don’t see a provider here? Submit a PR.

To use Amazon Bedrock with OpenCode:

Head over to the Model catalog in the Amazon Bedrock console and request access to the models you want.

You need to have access to the model you want in Amazon Bedrock.

You’ll need either to set one of the following environment variables:

Once you have one of the above, set it while running opencode.

Or add it to a .env file in the project root.

Or add it to your bash profile.

Run the /models command to select the model you want.

We recommend signing up for Claude Pro or Max, it’s the most cost-effective way to use opencode.

Once you’ve signed up, run opencode auth login and select Anthropic.

Here you can select the Claude Pro/Max option and it’ll open your browser and ask you to authenticate.

Now all the the Anthropic models should be available when you use the /models command.


*[Content truncated - see full docs]*

**Examples**:

```text
{  "$schema": "https://opencode.ai/config.json",  "provider": {    "anthropic": {      "options": {        "baseURL": "https://api.anthropic.com/v1"      }    }  }}
```

```text
$ opencode auth login
┌  Add credential│◇  Select provider│  opencode│●  Create an api key at https://opencode.ai/auth│◆  Enter your API key│  _└
```

```text
AWS_ACCESS_KEY_ID=XXX opencode
```

---

## Rules | opencode

**URL**: https://opencode.ai/docs/rules/

**Contents**:
- Rules
- Initialize
- Example
- Types
  - Project
  - Global
- Precedence
- Custom Instructions

Set custom instructions for opencode.

You can provide custom instructions to opencode by creating an AGENTS.md file. This is similar to CLAUDE.md or Cursor’s rules. It contains instructions that will be included in the LLM’s context to customize its behavior for your specific project.

To create a new AGENTS.md file, you can run the /init command in opencode.

You should commit your project’s AGENTS.md file to Git.

This will scan your project and all its contents to understand what the project is about and generate an AGENTS.md file with it. This helps opencode to navigate the project better.

If you have an existing AGENTS.md file, this will try to add to it.

You can also just create this file manually. Here’s an example of some things you can put into an AGENTS.md file.

We are adding project-specific instructions here and this will be shared across your team.

opencode also supports reading the AGENTS.md file from multiple locations. And this serves different purposes.

The ones we have seen above, where the AGENTS.md is placed in the project root, are project-specific rules. These only apply when you are working in this directory or its sub-directories.

You can also have global rules in a ~/.config/opencode/AGENTS.md file. This gets applied across all opencode sessions.

Since this isn’t committed to Git or shared with your team, we recommend using this to specify any personal rules that the LLM should follow.

So when opencode starts, it looks for:

If you have both global and project-specific rules, opencode will combine them together.

You can specify custom instruction files in your opencode.json or the global ~/.config/opencode/opencode.json. This allows you and your team to reuse existing rules rather than having to duplicate them to AGENTS.md.

All instruction files are combined with your AGENTS.md files.

While opencode doesn’t automatically parse file references in AGENTS.md, you can achieve similar functionality in two ways:

The recommended approa

*[Content truncated - see full docs]*

**Examples**:

```javascript
# SST v3 Monorepo Project
This is an SST v3 monorepo with TypeScript. The project uses bun workspaces for package management.
## Project Structure
- `packages/` - Contains all workspace packages (functions, core, web, etc.)- `infra/` - Infrastructure definitions split by service (storage.ts, api.ts, web.ts)- `sst.config.ts` - Main SST configuration with dynamic imports
## Code Standards
- Use TypeScript with strict mode enabled- Shared code goes in `packages/core/` with proper exports configurat
...
```

```text
{  "$schema": "https://opencode.ai/config.json",  "instructions": ["CONTRIBUTING.md", "docs/guidelines.md", ".cursor/rules/*.md"]}
```

```text
{  "$schema": "https://opencode.ai/config.json",  "instructions": ["docs/development-standards.md", "test/testing-guidelines.md", "packages/*/AGENTS.md"]}
```

---

## Rules | opencode

**URL**: https://opencode.ai/docs/rules

**Contents**:
- Rules
- Initialize
- Example
- Types
  - Project
  - Global
- Precedence
- Custom Instructions

Set custom instructions for opencode.

You can provide custom instructions to opencode by creating an AGENTS.md file. This is similar to CLAUDE.md or Cursor’s rules. It contains instructions that will be included in the LLM’s context to customize its behavior for your specific project.

To create a new AGENTS.md file, you can run the /init command in opencode.

You should commit your project’s AGENTS.md file to Git.

This will scan your project and all its contents to understand what the project is about and generate an AGENTS.md file with it. This helps opencode to navigate the project better.

If you have an existing AGENTS.md file, this will try to add to it.

You can also just create this file manually. Here’s an example of some things you can put into an AGENTS.md file.

We are adding project-specific instructions here and this will be shared across your team.

opencode also supports reading the AGENTS.md file from multiple locations. And this serves different purposes.

The ones we have seen above, where the AGENTS.md is placed in the project root, are project-specific rules. These only apply when you are working in this directory or its sub-directories.

You can also have global rules in a ~/.config/opencode/AGENTS.md file. This gets applied across all opencode sessions.

Since this isn’t committed to Git or shared with your team, we recommend using this to specify any personal rules that the LLM should follow.

So when opencode starts, it looks for:

If you have both global and project-specific rules, opencode will combine them together.

You can specify custom instruction files in your opencode.json or the global ~/.config/opencode/opencode.json. This allows you and your team to reuse existing rules rather than having to duplicate them to AGENTS.md.

All instruction files are combined with your AGENTS.md files.

While opencode doesn’t automatically parse file references in AGENTS.md, you can achieve similar functionality in two ways:

The recommended approa

*[Content truncated - see full docs]*

**Examples**:

```javascript
# SST v3 Monorepo Project
This is an SST v3 monorepo with TypeScript. The project uses bun workspaces for package management.
## Project Structure
- `packages/` - Contains all workspace packages (functions, core, web, etc.)- `infra/` - Infrastructure definitions split by service (storage.ts, api.ts, web.ts)- `sst.config.ts` - Main SST configuration with dynamic imports
## Code Standards
- Use TypeScript with strict mode enabled- Shared code goes in `packages/core/` with proper exports configurat
...
```

```text
{  "$schema": "https://opencode.ai/config.json",  "instructions": ["CONTRIBUTING.md", "docs/guidelines.md", ".cursor/rules/*.md"]}
```

```text
{  "$schema": "https://opencode.ai/config.json",  "instructions": ["docs/development-standards.md", "test/testing-guidelines.md", "packages/*/AGENTS.md"]}
```

---

## Share | opencode

**URL**: https://opencode.ai/docs/share

**Contents**:
- Share
- How it works
- Sharing
  - Manual (default)
  - Auto-share
  - Disabled
- Un-sharing
- Privacy

Share your OpenCode conversations.

OpenCode’s share feature allows you to create public links to your OpenCode conversations, so you can collaborate with teammates or get help from others.

Shared conversations are publicly accessible to anyone with the link.

When you share a conversation, OpenCode:

OpenCode supports three sharing modes that control how conversations are shared:

By default, OpenCode uses manual sharing mode. Sessions are not shared automatically, but you can manually share them using the /share command:

This will generate a unique URL that’ll be copied to your clipboard.

To explicitly set manual mode in your config file:

You can enable automatic sharing for all new conversations by setting the share option to "auto" in your config file:

With auto-share enabled, every new conversation will automatically be shared and a link will be generated.

You can disable sharing entirely by setting the share option to "disabled" in your config file:

To enforce this across your team for a given project, add it to the opencode.json in your project and check into Git.

To stop sharing a conversation and remove it from public access:

This will remove the share link and delete the data related to the conversation.

There are a few things to keep in mind when sharing a conversation.

Shared conversations remain accessible until you explicitly unshare them. This includes:

For enterprise deployments, the share feature can be:

Learn more about using opencode in your organization.

**Examples**:

```text
{  "$schema": "https://opencode.ai/config.json",  "share": "manual"}
```

```text
{  "$schema": "https://opencode.ai/config.json",  "share": "auto"}
```

```text
{  "$schema": "https://opencode.ai/config.json",  "share": "disabled"}
```

---

## Themes | opencode

**URL**: https://opencode.ai/docs/themes

**Contents**:
- Themes
- Terminal requirements
- Built-in themes
- System theme
- Using a theme
- Custom themes
  - Hierarchy
  - Creating a theme

Select a built-in theme or define your own.

With OpenCode you can select from one of several built-in themes, use a theme that adapts to your terminal theme, or define your own custom theme.

By default, OpenCode uses our own opencode theme.

For themes to display correctly with their full color palette, your terminal must support truecolor (24-bit color). Most modern terminals support this by default, but you may need to enable it:

Without truecolor support, themes may appear with reduced color accuracy or fall back to the nearest 256-color approximation.

OpenCode comes with several built-in themes.

And more, we are constantly adding new themes.

The system theme is designed to automatically adapt to your terminal’s color scheme. Unlike traditional themes that use fixed colors, the system theme:

The system theme is for users who:

You can select a theme by bringing up the theme select with the /theme command. Or you can specify it in your config.

OpenCode supports a flexible JSON-based theme system that allows users to create and customize themes easily.

Themes are loaded from multiple directories in the following order where later directories override earlier ones:

If multiple directories contain a theme with the same name, the theme from the directory with higher priority will be used.

To create a custom theme, create a JSON file in one of the theme directories.

For user-wide themes:

And for project-specific themes.

Themes use a flexible JSON format with support for:

The defs section is optional and it allows you to define reusable colors that can be referenced in the theme.

The special value "none" can be used for any color to inherit the terminal’s default color. This is particularly useful for creating themes that blend seamlessly with your terminal’s color scheme:

Here’s an example of a custom theme:

**Examples**:

```text
{  "$schema": "https://opencode.ai/config.json",  "theme": "tokyonight"}
```

```text
mkdir -p ~/.config/opencode/themesvim ~/.config/opencode/themes/my-theme.json
```

```text
mkdir -p .opencode/themesvim .opencode/themes/my-theme.json
```

---

## Zen | opencode

**URL**: https://opencode.ai/docs/zen

**Contents**:
- Zen
- Background
- How it works
- Endpoints
- Pricing
- Privacy
- For Teams
  - Roles

Curated list of models provided by OpenCode.

OpenCode Zen is a list of tested and verified models provided by the OpenCode team.

OpenCode Zen is currently in beta.

Zen works like any other provider in OpenCode. You login to OpenCode Zen and get your API key. It’s completely optional and you don’t need to use it to use OpenCode.

There are a large number of models out there but only a few of these models work well as coding agents. Additionally, most providers are configured very differently; so you get very different performance and quality.

We tested a select group of models and providers that work well with OpenCode.

So if you are using a model through something like OpenRouter, you can never be sure if you are getting the best version of the model you want.

To fix this, we did a couple of things:

OpenCode Zen is an AI gateway that gives you access to these models.

OpenCode Zen works like any other provider in OpenCode.

You are charged per request and you can add credits to your account.

You can also access our models through the following API endpoints.

The model id in your OpenCode config uses the format opencode/<model-id>. For example, for GPT 5 Codex, you would use opencode/gpt-5-codex in your config.

We support a pay-as-you-go model. Below are the prices per 1M tokens.

You might notice Claude Haiku 3.5 in your usage history. This is a low cost model that’s used to generate the titles of your sessions.

Credit card fees are passed along at cost; we don’t charge anything beyond that.

Subscription plans and a free tier are coming soon.

Contact us if you have any questions.

All our models are hosted in the US. Our providers follow a zero-retention policy and do not use your data for model training, with the following exceptions:

Zen also works great for teams. You can invite teammates, assign roles, curate the models your team uses, and more.

Workspaces are currently free for teams as a part of the beta.

Managing your workspace is currently fr

*[Content truncated - see full docs]*

---
