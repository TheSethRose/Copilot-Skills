---
description: Authentication for the Web - NextAuth.js
---

# Authjs

**Purpose**: Authentication for the Web - NextAuth.js

## When to Use This Skill

Use this skill when:
- Working with authjs projects
- Implementing authjs features
- Debugging authjs code
- Learning authjs best practices
- Building applications with authjs

**Keywords**: authjs, getting_started

## Quick Reference

### Common Patterns

**1. Mapping Existing ColumnsInstead of altering your existing database column names,**

```
emailVerified
```

**2. Replace useSession calls with Better Auth’s version. Example:**

```
useSession
```

## Reference Documentation

This skill includes comprehensive documentation in `.github/copilot-skills/auth/authjs/references/`:

- **getting_started.md** - Getting Started documentation

## How to Use

### For Quick Answers
Ask directly about authjs features, APIs, or patterns.

### For Detailed Information
Reference specific documentation files:
- Check `references/getting_started.md` for setup
- Check `references/api_reference.md` for API details

## When to Use AuthJS vs Better-Auth

| Aspect | AuthJS | Better-Auth |
|--------|--------|-------------|
| **Best For** | Existing Next-auth ecosystem | Modern full-stack apps |
| **Learning Curve** | Moderate | Lower |
| **Setup Time** | Medium (mature ecosystem) | Fast (minimal boilerplate) |
| **Auth Methods** | OAuth, JWT, Sessions | Passkeys, OAuth, Email-OTP, Sessions |
| **Database** | Prisma preferred but flexible | Flexible (Drizzle, TypeORM, etc.) |
| **Type Safety** | Good with TypeScript | Excellent (built for TS) |
| **Maintenance** | Active | Actively developed |
| **Community** | Large, well-established | Growing, modern-focused |
| **Best With** | Next.js 12+ | SvelteKit, Next.js, Remix |
| **Mobile** | Limited | Built for full-stack |

### Choose AuthJS if:
- You're already using Next-auth ecosystem
- You need mature OAuth providers
- Your project is established on NextAuth
- You prefer session-based auth

### Choose Better-Auth if:
- You're starting a new project
- You want passkey support
- You need less boilerplate
- You prefer simpler configuration

See also: `/better-auth` for the alternative
- Check category files for specific topics

### For Code Examples
Use the Quick Reference patterns above or ask for specific examples.

## Related Skills

- None (standalone skill)

## More Information

- **Base Documentation**: https://authjs.dev/getting-started
- **Generated**: 2025-10-20
- **Total Pages**: 139
