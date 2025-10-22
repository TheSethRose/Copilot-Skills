# Prisma Instructions

**Auto-loaded when**: Working with files matching: `**/prisma/**, **/*.prisma, **/*.ts, **/*.js, **/schema.prisma`

## Default Behaviors

When working with Prisma:

1. **Use Prisma Schema First**: Define your data model in `prisma/schema.prisma`
2. **Generate Client**: Always run `npx prisma generate` after schema changes
3. **Type Safety**: Leverage generated types from Prisma Client
4. **Migrations**: Use `npx prisma migrate` for schema changes
5. **Testing**: Use `@prisma/internals` for testing databases
6. **Async Patterns**: Always use `.disconnect()` after operations

## Common Workflows

### Schema Definition

```prisma
// prisma/schema.prisma
datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model User {
  id    Int     @id @default(autoincrement())
  email String  @unique
  name  String?
  posts Post[]
}

model Post {
  id    Int     @id @default(autoincrement())
  title String
  authorId Int
  author User @relation(fields: [authorId], references: [id])
}
```

### Basic CRUD Operations

```typescript
import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

// Create
const user = await prisma.user.create({
  data: { email: "user@example.com", name: "John" }
});

// Read
const foundUser = await prisma.user.findUnique({
  where: { id: 1 }
});

// Update
const updated = await prisma.user.update({
  where: { id: 1 },
  data: { name: "Jane" }
});

// Delete
await prisma.user.delete({ where: { id: 1 } });

await prisma.$disconnect();
```

### With Relations

```typescript
// Create with nested relations
const user = await prisma.user.create({
  data: {
    email: "user@example.com",
    posts: {
      create: [
        { title: "First Post" },
        { title: "Second Post" }
      ]
    }
  },
  include: { posts: true }
});

// Query with relations
const userWithPosts = await prisma.user.findUnique({
  where: { id: 1 },
  include: {
    posts: {
      where: { published: true },
      orderBy: { createdAt: "desc" }
    }
  }
});
```

### Migrations

```bash
# Create migration
npx prisma migrate dev --name add_published_field

# Reset database (dev only)
npx prisma migrate reset

# Apply migrations to production
npx prisma migrate deploy
```

### With FastAPI/Next.js

```typescript
// In Next.js API route or FastAPI
import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

export async function GET() {
  const users = await prisma.user.findMany();
  return new Response(JSON.stringify(users));
}
```

### Advanced Queries

```typescript
// Complex filtering
const posts = await prisma.post.findMany({
  where: {
    AND: [
      { author: { email: { contains: "@company.com" } } },
      { published: true }
    ]
  }
});

// Aggregation
const count = await prisma.post.count({
  where: { published: true }
});

// Grouping
const grouped = await prisma.post.groupBy({
  by: ["authorId"],
  _count: true
});
```

## Common Patterns

### Setup & Installation

```bash
npm install @prisma/client
npm install -D prisma

# Initialize Prisma
npx prisma init

# Setup database
npx prisma migrate dev --name init
```

### Development Best Practices

1. Always include generated types in TypeScript files
2. Use environment variables for DATABASE_URL
3. Run migrations before deploying
4. Use `.findUnique()` with `@unique` fields
5. Always call `prisma.$disconnect()` or use connection pooling

### Common Issues

- **"Global PrismaClient is not defined"**: Use singleton pattern in production
- **"P1000 Can't reach database"**: Check DATABASE_URL connection string
- **"P2025 An operation failed because it depended on one or more records"**: Record not found
- **"P2002 Unique constraint failed"**: Duplicate value in unique field
- **Migration conflicts**: Resolve conflicts in `prisma/migrations/`

## Quality Guidelines

- ✅ Define relationships clearly in schema
- ✅ Use migrations for all schema changes
- ✅ Validate data at application layer
- ✅ Use transactions for complex operations
- ✅ Implement proper error handling
- ⚠️ Never skip migrations in production
- ⚠️ Don't expose database credentials
- ⚠️ Avoid N+1 query problems (use `include` or `select`)

## Integration Patterns

### With TypeScript

```typescript
// Type-safe query results
type UserWithPosts = Prisma.UserGetPayload<{
  include: { posts: true }
}>;
```

### With Testing

```typescript
import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

beforeEach(async () => {
  await prisma.user.deleteMany();
});

afterAll(async () => {
  await prisma.$disconnect();
});
```

## Resources

- Skill prompt: `.github/prompts/prisma.skill.prompt.md`
- References: `.github/copilot-skills/backend/prisma/references/`
- Official docs: https://www.prisma.io/
- Prisma Schema Reference: https://www.prisma.io/docs/reference/api-reference/prisma-schema-reference
- Data Model Guide: https://www.prisma.io/docs/orm/prisma-schema/data-model

## Related Skills

- `/supabase` – Cloud database option with Prisma
- `/fastapi` – Python backend (Prisma has Python support)
- `/nextjs` – Full-stack Next.js applications
- `/typescript` – Type-safe database queries
- `/better-auth` – Authentication with Prisma
