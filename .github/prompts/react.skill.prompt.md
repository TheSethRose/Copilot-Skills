---
description: JavaScript library for building user interfaces
---

# React

**Purpose**: JavaScript library for building user interfaces

## When to Use This Skill

Use this skill when:
- Working with react projects
- Implementing react features
- Debugging react code
- Learning react best practices
- Building applications with react

**Keywords**: react, learn, reference, other

## Quick Reference

### Common Patterns

**1. Learn ReactInstallationAdd React to an Existing ProjectIf you want to add some i**

```
example.com
```

**2. If you want to add some interactivity to your existing project, you don’t have t**

```
example.com
```

**3. If you want to add some interactivity to your existing project, you don’t have t**

```
example.com
```

**4. If the entire content of your page was replaced by a “Hello, world!”, everything**

```
import { createRoot } from 'react-dom/client';// Clear the existing HTML contentdocument.body.innerHTML = '<div id="app"></div>';// Render your React component insteadconst root = createRoot(document.
```

**5. Instead, you probably want to render your React components in specific places in**

```
id
```

### Code Examples

**Example 1** (python):
```python
import { createRoot } from 'react-dom/client';// Clear the existing HTML contentdocument.body.innerHTML = '<div id="app"></div>';// Render your React component insteadconst root = createRoot(document.getElementById('app'));root.render(<h1>Hello, worl
```

**Example 2** (javascript):
```javascript
const [index, setIndex] = useState(0);const [showMore, setShowMore] = useState(false);
```

**Example 3** (javascript):
```javascript
function MessageComponent({ messagePromise }) {  const message = use(messagePromise);  const theme = use(ThemeContext);  // ...}
```

**Example 4** (javascript):
```javascript
function ImageGallery() {  const [index, setIndex] = useState(0);  // ...
```

**Example 5** (javascript):
```javascript
function Button() {  const theme = useContext(ThemeContext);  // ...
```

## Reference Documentation

This skill includes comprehensive documentation in `.github/copilot-skills/frontend/react/references/`:

- **learn.md** - Learn documentation
- **other.md** - Other documentation
- **reference.md** - Reference documentation

## How to Use

### For Quick Answers
Ask directly about react features, APIs, or patterns.

### For Detailed Information
Reference specific documentation files:
- Check `references/getting_started.md` for setup
- Check `references/api_reference.md` for API details
- Check category files for specific topics

### For Code Examples
Use the Quick Reference patterns above or ask for specific examples.

## Common Tech Stacks

### React + Vite + TypeScript (Recommended)
- **Build Tool**: Vite for fast development
- **Styling**: Tailwind CSS
- **UI Components**: ShadCN/UI or Radix UI
- **State Management**: TanStack Query + Zustand
- **API Client**: Fetch API or Axios
- **Testing**: Vitest + React Testing Library

See also: `/vite`, `/tailwind`, `/shadcn`, `/radix-ui`, `/typescript`

### React + Next.js Full Stack
- **Framework**: Next.js with App Router
- **Styling**: Tailwind CSS
- **UI Components**: ShadCN/UI
- **Database**: Prisma + PostgreSQL
- **Auth**: Better-Auth or AuthJS
- **API Routes**: Next.js API routes
- **Deployment**: Vercel

See also: `/nextjs`, `/tailwind`, `/shadcn`, `/prisma`, `/better-auth`, `/vercel`

### React + Material-UI + Redux
- **UI Library**: Material-UI
- **State Management**: Redux Toolkit
- **API Client**: React Query + Axios
- **Styling**: Material-UI theming
- **Form Handling**: React Hook Form
- **Testing**: Jest + React Testing Library

See also: `/material-ui`, `/typescript`

### React + Vite + FastAPI Backend
- **Frontend**: React + Vite + TypeScript
- **Backend**: FastAPI + Python
- **Database**: Supabase or PostgreSQL
- **API Communication**: Axios with interceptors
- **Authentication**: Better-Auth
- **Styling**: Tailwind CSS

See also: `/vite`, `/fastapi`, `/supabase`, `/tailwind`

## Related Skills

- `/vite` – Build tool and dev server
- `/nextjs` – Full-stack framework
- `/tailwind` – Utility CSS framework
- `/shadcn` – Component library
- `/radix-ui` – Headless UI primitives
- `/typescript` – Type safety
- `/fastapi` – Backend framework

## More Information

- **Base Documentation**: https://react.dev/
- **Generated**: 2025-10-19
- **Total Pages**: 150
