---
description: React framework for production with hybrid static & server rendering
---

# Nextjs

**Purpose**: React framework for production with hybrid static & server rendering

## When to Use This Skill

Use this skill when:
- Working with nextjs projects
- Implementing nextjs features
- Debugging nextjs code
- Learning nextjs best practices
- Building applications with nextjs

**Keywords**: nextjs, getting_started, app_router, other

## Quick Reference

### Common Patterns

**1. Using App RouterFeatures available in /appLatest Version15.5.6Getting StartedIns**

```
<Form>
```

**2. Using App RouterFeatures available in /appLatest Version15.5.6Getting StartedIns**

```
<Form>
```

**3. API ReferenceComponentsForm ComponentCopy pageForm ComponentThe <Form> component**

```
<Form>
```

**4. Form ComponentThe <Form> component extends the HTML <form> element to provide pr**

```
<Form>
```

**5. Basic usage:**

```
import Form from 'next/form'
 
export default function Page() {
  return (
    <Form action="/search">
      {/* On submission, the input value will be appended to
          the URL, e.g. /search?quer
```

### Code Examples

**Example 1** (python):
```python
import Form from 'next/form'
 
export default function Page() {
  return (
    <Form action="/search">
      <input name="query" />
      <button type="submit">Submit</button>
    </Form>
  )
}
```

## Reference Documentation

This skill includes comprehensive documentation in `.github/copilot-skills/frontend/nextjs/references/`:

- **app_router.md** - App Router documentation
- **getting_started.md** - Getting Started documentation
- **other.md** - Other documentation

## How to Use

### For Quick Answers
Ask directly about nextjs features, APIs, or patterns.

### For Detailed Information
Reference specific documentation files:
- Check `references/getting_started.md` for setup
- Check `references/api_reference.md` for API details
- Check category files for specific topics

### For Code Examples
Use the Quick Reference patterns above or ask for specific examples.

## Related Skills

## Common Tech Stacks

### Next.js Full Stack (Recommended)
- **Framework**: Next.js with App Router + Server Components
- **Styling**: Tailwind CSS v4
- **UI Components**: ShadCN/UI
- **Database**: Prisma + PostgreSQL
- **Authentication**: Better-Auth or AuthJS
- **API**: Route handlers + API routes
- **Deployment**: Vercel
- **Forms**: React Hook Form + Zod

See also: `/react`, `/tailwind`, `/shadcn`, `/prisma`, `/better-auth`, `/vercel`

### Next.js + Headless CMS
- **Framework**: Next.js
- **Styling**: Tailwind CSS
- **UI Components**: Radix UI
- **CMS**: Contentful, Strapi, or Sanity
- **API**: Next.js API routes
- **Static Generation**: getStaticProps, generateStaticParams
- **Revalidation**: Incremental Static Regeneration (ISR)

See also: `/react`, `/tailwind`, `/radix-ui`

### Next.js with LLM Integration
- **Framework**: Next.js App Router
- **AI**: Claude API or OpenAI API
- **Styling**: Tailwind CSS
- **Database**: Supabase for vector embeddings
- **Components**: ShadCN/UI
- **Streaming**: AI response streaming

See also: `/claude`, `/openai`, `/supabase`, `/shadcn`

### Next.js + GraphQL Backend
- **Frontend**: Next.js
- **API**: GraphQL (Apollo or GraphQL Yoga)
- **Database**: Prisma
- **Authentication**: Better-Auth
- **Styling**: Tailwind CSS
- **Type Generation**: GraphQL Code Generator

See also: `/typescript`, `/prisma`, `/tailwind`

## Related Skills

- `/react` – React fundamentals
- `/tailwind` – Styling
- `/shadcn` – Component library
- `/prisma` – ORM database
- `/better-auth` – Authentication
- `/vercel` – Deployment platform
- `/supabase` – Cloud database

## More Information

- **Base Documentation**: https://nextjs.org/
- **Generated**: 2025-10-19
- **Total Pages**: 200
