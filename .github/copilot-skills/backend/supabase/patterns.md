# Supabase - Common Patterns

Quick reference for common supabase patterns and usage.

## Code Patterns

### 1. DOCSStartProducts Build Manage Reference Resources DOCSSearch docs...KGetting StartedAI Prompt: Boot

```
#<filename>
```

### 2. AI Prompt: Bootstrap Next.js app with Supabase AuthHow to use# Copy the prompt to a file in your rep

```
#<filename>
```

### 3. AI Prompt: Bootstrap Next.js app with Supabase AuthHow to use# Copy the prompt to a file in your rep

```
#<filename>
```

### 4. AI Prompt: Bootstrap Next.js app with Supabase AuthHow to use# Copy the prompt to a file in your rep

```
#<filename>
```

### 5. AI Prompt: Bootstrap Next.js app with Supabase AuthHow to use# Copy the prompt to a file in your rep

```
#<filename>
```

### 6. DOCSStartProducts Build Manage Reference Resources DOCSSearch docs...KGetting StartedAI Prompt: Data

```
#<filename>
```

### 7. AI Prompt: Database: Create RLS policiesHow to use# Copy the prompt to a file in your repo. Use the 

```
#<filename>
```

### 8. AI Prompt: Database: Create RLS policiesHow to use# Copy the prompt to a file in your repo. Use the 

```
#<filename>
```

## Examples

### Example 1

```javascript
1234567Deno.serve(async (req: Request) => {  // ...  const authHeader = req.headers.get('Authorization')!  const token = authHeader.replace('Bearer ', '')  const { data } = await supabaseClient.auth.getUser(token)  // ...})
```

### Example 2

```javascript
1234567// Mark the asyncLongRunningTask's returned promise as a background task.// ⚠️ We are NOT using `await` because we don't want it to block!EdgeRuntime.waitUntil(asyncLongRunningTask())Deno.serve(async (req) => {  return new Response(...)})
```

### Example 3

```javascript
123456Deno.serve(async (req) => {  // Won't block the request, runs in background.  EdgeRuntime.waitUntil(asyncLongRunningTask())  return new Response(...)})
```

### Example 4

```javascript
1supabase functions new cloudflare-turnstile
```

### Example 5

```javascript
1234export const corsHeaders = {  'Access-Control-Allow-Origin': '*',  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',}
```

### Example 6

```javascript
1supabase functions new amazon-bedrock
```

### Example 7

```python
12345import handler from './handler.tsx'console.log('Hello from og-image Function!')Deno.serve(handler)
```

### Example 8

```javascript
12[functions.hello-world]verify_jwt = false
```

### Example 9

```python
123456import { createClient } from '@supabase/supabase-js'const SUPABASE_URL = 'https://<project>.supabase.co'const SUPABASE_KEY = '<sb_publishable_... or anon key>'const supabase = createClient(SUPABASE_URL, SUPABASE_KEY)
```

### Example 10

```python
123import { createClient } from '@supabase/supabase-js'const supabase = createClient('https://<project>.supabase.co', '<anon_key or sb_publishable_key>')
```


## Categories

See organized documentation in `references/`:

- `references/auth.md` - Auth
- `references/database.md` - Database
- `references/functions.md` - Functions
- `references/getting_started.md` - Getting Started
- `references/other.md` - Other
- `references/realtime.md` - Realtime
- `references/storage.md` - Storage
