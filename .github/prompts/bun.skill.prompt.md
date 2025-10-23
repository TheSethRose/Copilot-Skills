# Bun

**Purpose**: Bun is a fast JavaScript runtime, bundler, transpiler, and package manager built in Zig

## When to Use This Skill

Use this skill when:
- Setting up a new Bun project or migrating from Node.js/npm
- Building applications with Bun's runtime (HTTP servers, CLI tools, workers)
- Using Bun as a package manager (install, add, remove dependencies)
- Bundling and building JavaScript/TypeScript applications
- Transpiling code for different environments
- Debugging performance issues or optimizing builds
- Configuring Bun via `bunfig.toml`
- Using Bun's built-in APIs (file I/O, networking, testing, SQL, etc.)
- Running tests with Bun's test runner
- Working with Web APIs and Node.js compatibility layers
- Deploying Bun applications to production

## Quick Reference

**Keywords**: bun, javascript runtime, bundler, package manager, transpiler, builder, runtime, fast runtime, zig, performance

**Categories**:
- **Getting Started** - Installation, setup, quick start guides
- **Runtime** - HTTP servers, networking, file I/O, built-in APIs, Web APIs
- **Bundler** - Building, bundling, loaders, plugins, entry points
- **Package Manager** - Install, add, remove, workspaces, lockfile management
- **Tooling** - CLI commands, testing, debugging, deployment guides
- **Guides** - Framework integrations (Express, Hono, Elysia), deployment (Railway, Render, Docker)
- **Reference** - API reference and technical specifications

## How to Use This Skill

### 1. Quick Question (Informational)
**User asks**: "How do I create an HTTP server in Bun?" or "What's Bun's package.json format?"

**Action**: 
- Search relevant reference category (Runtime or Reference)
- Provide quick code example
- Link to full documentation in `.github/copilot-skills/runtimes/bun/references/`

### 2. Project Setup
**User asks**: "How do I set up a new Bun project?" or "Migrate Node.js to Bun"

**Action**:
- Check `getting_started.md` for installation and setup
- Provide migration guides
- Link to framework integrations if applicable

### 3. Implementation Help
**User asks**: "Build an API with Bun" or "How do I use SQL in Bun?"

**Action**:
- Reference `runtime.md` for built-in APIs
- Show code examples with proper syntax
- Link to detailed documentation pages

### 4. Bundling/Build Configuration
**User asks**: "Configure Bun bundler" or "How do I create a Bun bundle?"

**Action**:
- Check `bundler.md` for configuration options
- Reference `bunfig.toml` documentation
- Show configuration examples

### 5. Package Management
**User asks**: "Install dependencies with Bun" or "Manage monorepos with Bun"

**Action**:
- Check `package_manager.md` for CLI commands
- Show examples for common tasks (install, add, workspaces)
- Explain lockfile and dependency resolution

### 6. Testing & Debugging
**User asks**: "Write tests in Bun" or "Debug Bun application"

**Action**:
- Reference testing guides in `tooling.md`
- Show test syntax and configuration
- Link to VSCode/Web debugger guides

### 7. Deployment
**User asks**: "Deploy Bun to production" or "Docker with Bun"

**Action**:
- Check deployment guides in `guides.md`
- Show platform-specific examples (Railway, Render, etc.)
- Reference Docker setup guide

## Common Workflows

### Workflow 1: New Bun Project
```
1. Check getting_started.md for installation
2. Show: bun init, project structure
3. Reference: bunfig.toml configuration
4. Link: Framework integrations if needed
```

### Workflow 2: HTTP Server
```
1. Reference runtime.md for HTTP APIs
2. Show: Bun.serve() example
3. Reference: Request/Response APIs
4. Link: Advanced features (middleware, routing, etc.)
```

### Workflow 3: Package Installation
```
1. Reference package_manager.md
2. Show: bun install, bun add commands
3. Reference: dependency resolution, workspaces
4. Link: Lock file and cache management
```

### Workflow 4: Build & Bundle
```
1. Reference bundler.md for configuration
2. Show: bunfig.toml setup
3. Reference: loaders, plugins, entry points
4. Link: Performance optimization tips
```

### Workflow 5: Testing
```
1. Reference tooling.md for test runner
2. Show: Test file structure and syntax
3. Reference: Assertions, mocks, snapshots
4. Link: Coverage and reporter options
```

## Documentation Location

All reference documentation available in:
```
.github/copilot-skills/runtimes/bun/
├── reference.md              # Overview & category guide
├── references/
│   ├── getting_started.md    # Setup, installation, quick start
│   ├── runtime.md            # APIs, servers, built-in modules
│   ├── bundler.md            # Bundling, build configuration
│   ├── package_manager.md    # Package management CLI
│   ├── tooling.md            # Testing, debugging, CLI
│   ├── guides.md             # Framework & deployment guides
│   └── reference.md          # Additional reference pages
```

## Success Indicators

You've successfully used this skill when:
- ✅ User gets accurate Bun documentation
- ✅ Code examples provided are correct and runnable
- ✅ Workflow recommendations match user's task
- ✅ Links to detailed docs help user explore further
- ✅ User can complete their Bun task independently

## Related Skills

- `/docs-to-skill` - How this skill was generated from Bun docs
- `/create-skill` - Further customize or extend Bun skill
- `/web-research` - Research Bun ecosystem and integrations

## Tips

✅ **Do**:
- Check appropriate reference category first
- Provide runnable code examples
- Link to detailed documentation
- Suggest relevant framework integrations
- Explain Bun-specific features vs Node.js differences

❌ **Don't**:
- Provide generic Node.js solutions (Bun has different APIs)
- Skip the "when to use" context
- Forget to check for framework-specific guides
- Assume user knows Bun's unique features

## Auto-Load File Patterns

This skill auto-loads when editing:
- `**/*.ts` - TypeScript files (Bun-native support)
- `**/*.tsx` - TSX files (Bun supports JSX)
- `**/*.js` - JavaScript files
- `**/*.jsx` - JSX files
- `**/bunfig.toml` - Bun configuration file
- `**/package.json` - Package manifest (Bun format)
