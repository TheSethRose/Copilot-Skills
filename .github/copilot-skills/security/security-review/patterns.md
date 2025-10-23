# Common Security Vulnerability Patterns

This document catalogs common security vulnerability patterns across languages and frameworks for quick reference during code reviews.

## Table of Contents

1. [Injection Patterns](#injection-patterns)
2. [Authentication & Authorization Patterns](#authentication--authorization-patterns)
3. [Data Exposure Patterns](#data-exposure-patterns)
4. [Cryptographic Patterns](#cryptographic-patterns)
5. [Input Validation Patterns](#input-validation-patterns)
6. [Business Logic Patterns](#business-logic-patterns)
7. [Configuration Patterns](#configuration-patterns)
8. [XSS Patterns](#xss-patterns)

---

## Injection Patterns

### SQL Injection

**Python**:
```python
# ❌ VULNERABLE
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
cursor.execute("SELECT * FROM users WHERE name = '" + name + "'")
query = "DELETE FROM orders WHERE id = %s" % order_id

# ✅ SAFE
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
cursor.execute("SELECT * FROM users WHERE name = %s", (name,))
# Use ORM
User.objects.filter(id=user_id)
```

**JavaScript/TypeScript**:
```javascript
// ❌ VULNERABLE
db.query(`SELECT * FROM users WHERE email = '${email}'`)
connection.query("SELECT * FROM products WHERE id = " + productId)

// ✅ SAFE
db.query('SELECT * FROM users WHERE email = ?', [email])
db.query('SELECT * FROM products WHERE id = $1', [productId])
// Use ORM
await prisma.user.findUnique({ where: { email } })
```

### Command Injection

**Python**:
```python
# ❌ VULNERABLE
os.system(f"ls {user_path}")
subprocess.call(f"ping {host}", shell=True)
subprocess.run(f"git clone {repo_url}", shell=True)

# ✅ SAFE
subprocess.run(["ls", user_path])
subprocess.run(["ping", "-c", "1", host])
subprocess.run(["git", "clone", repo_url])
```

**JavaScript/TypeScript**:
```javascript
// ❌ VULNERABLE
exec(`rm -rf ${userPath}`)
child_process.exec(`wget ${url}`)
eval(userCode)

// ✅ SAFE
execFile('rm', ['-rf', userPath])
child_process.spawn('wget', [url])
// Don't use eval with user input
```

### NoSQL Injection

**JavaScript (MongoDB)**:
```javascript
// ❌ VULNERABLE
db.collection.find({ username: req.body.username })
User.find({ $where: `this.username === '${username}'` })

// ✅ SAFE
db.collection.find({ username: { $eq: req.body.username } })
User.find({ username: username })
```

**Python (PyMongo)**:
```python
# ❌ VULNERABLE
db.users.find({"username": user_input})  # If user_input is dict
db.users.find(eval(user_query))

# ✅ SAFE
db.users.find({"username": str(user_input)})
# Validate input type
if not isinstance(user_input, str):
    raise ValueError("Invalid input")
```

### LDAP Injection

**Python**:
```python
# ❌ VULNERABLE
filter = f"(uid={username})"
ldap_conn.search_s(base_dn, ldap.SCOPE_SUBTREE, filter)

# ✅ SAFE
from ldap.filter import escape_filter_chars
safe_username = escape_filter_chars(username)
filter = f"(uid={safe_username})"
```

### XPath Injection

**Python**:
```python
# ❌ VULNERABLE
xpath = f"//user[username='{username}' and password='{password}']"
tree.xpath(xpath)

# ✅ SAFE
# Use parameterized queries or escape properly
xpath = "//user[username=$username and password=$password]"
tree.xpath(xpath, username=username, password=password)
```

### XXE (XML External Entity)

**Python**:
```python
# ❌ VULNERABLE
import xml.etree.ElementTree as ET
tree = ET.parse(user_xml_file)

# ✅ SAFE
from defusedxml.ElementTree import parse
tree = parse(user_xml_file)
```

**JavaScript**:
```javascript
// ❌ VULNERABLE
const parser = new DOMParser();
const doc = parser.parseFromString(xmlString, "text/xml");

// ✅ SAFE
// Disable external entities
const parser = new DOMParser({
  resolveExternalEntities: false
});
```

---

## Authentication & Authorization Patterns

### Missing Authentication

**Next.js**:
```typescript
// ❌ VULNERABLE
export async function GET(request: Request) {
  const users = await db.user.findMany();
  return Response.json(users);
}

// ✅ SAFE
import { getServerSession } from "next-auth";
export async function GET(request: Request) {
  const session = await getServerSession();
  if (!session) {
    return new Response('Unauthorized', { status: 401 });
  }
  const users = await db.user.findMany();
  return Response.json(users);
}
```

**FastAPI**:
```python
# ❌ VULNERABLE
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# ✅ SAFE
from fastapi import Depends
@app.get("/users/{user_id}")
async def get_user(user_id: int, current_user: User = Depends(get_current_user)):
    if current_user.id != user_id and not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Forbidden")
    return db.query(User).filter(User.id == user_id).first()
```

### Insecure Direct Object Reference (IDOR)

**Express**:
```javascript
// ❌ VULNERABLE
app.get('/api/order/:id', async (req, res) => {
  const order = await Order.findById(req.params.id);
  res.json(order);
});

// ✅ SAFE
app.get('/api/order/:id', authenticateUser, async (req, res) => {
  const order = await Order.findById(req.params.id);
  if (order.userId !== req.user.id) {
    return res.status(403).json({ error: 'Forbidden' });
  }
  res.json(order);
});
```

### Privilege Escalation

**Python**:
```python
# ❌ VULNERABLE
@app.route('/admin/users')
def admin_users():
    if request.args.get('role') == 'admin':
        return render_template('admin_users.html')
    
# ✅ SAFE
from functools import wraps
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function

@app.route('/admin/users')
@admin_required
def admin_users():
    return render_template('admin_users.html')
```

### Weak Session Management

**Express**:
```javascript
// ❌ VULNERABLE
app.use(session({
  secret: 'keyboard cat',
  resave: true,
  saveUninitialized: true
}));

// ✅ SAFE
app.use(session({
  secret: process.env.SESSION_SECRET,
  resave: false,
  saveUninitialized: false,
  cookie: {
    secure: true,  // HTTPS only
    httpOnly: true,  // No JS access
    maxAge: 3600000,  // 1 hour
    sameSite: 'strict'
  }
}));
```

---

## Data Exposure Patterns

### Hardcoded Secrets

**Python**:
```python
# ❌ VULNERABLE
API_KEY = "sk_live_EXAMPLE_NOT_REAL_KEY"  # Example only - not real
DATABASE_URL = "postgresql://admin:password123@localhost/db"
SECRET_KEY = "my-secret-key-12345"

# ✅ SAFE
import os
API_KEY = os.environ.get("API_KEY")
DATABASE_URL = os.environ.get("DATABASE_URL")
SECRET_KEY = os.environ.get("SECRET_KEY")
```

**JavaScript**:
```javascript
// ❌ VULNERABLE (examples only - not real keys)
const config = {
  apiKey: "AIza_EXAMPLE_NOT_REAL_API_KEY",
  stripeSecret: "sk_test_EXAMPLE_NOT_REAL"
};

// ✅ SAFE
const config = {
  apiKey: process.env.API_KEY,
  stripeSecret: process.env.STRIPE_SECRET
};
```

### Sensitive Data Logging

**Python**:
```python
# ❌ VULNERABLE
logger.info(f"User logged in: {username} with password {password}")
logger.debug(f"Credit card: {card_number}")
print(f"API Response: {response.json()}")  # May contain tokens

# ✅ SAFE
logger.info(f"User logged in: {username}")
logger.debug(f"Credit card: ****{card_number[-4:]}")
logger.debug(f"API Response status: {response.status_code}")
```

### Information Disclosure

**Express**:
```javascript
// ❌ VULNERABLE
app.use((err, req, res, next) => {
  res.status(500).json({ 
    error: err.stack,
    message: err.message 
  });
});

// ✅ SAFE
app.use((err, req, res, next) => {
  logger.error(err.stack);
  res.status(500).json({ 
    error: 'Internal server error' 
  });
});
```

---

## Cryptographic Patterns

### Weak Hashing Algorithms

**Python**:
```python
# ❌ VULNERABLE
import hashlib
import md5
password_hash = hashlib.md5(password.encode()).hexdigest()
password_hash = hashlib.sha1(password.encode()).hexdigest()

# ✅ SAFE
import hashlib
import os
salt = os.urandom(32)
password_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)

# Or use bcrypt
import bcrypt
password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
```

**JavaScript**:
```javascript
// ❌ VULNERABLE
const crypto = require('crypto');
const hash = crypto.createHash('md5').update(password).digest('hex');

// ✅ SAFE
const bcrypt = require('bcrypt');
const saltRounds = 10;
const hash = await bcrypt.hash(password, saltRounds);
```

### Insecure Random Generation

**Python**:
```python
# ❌ VULNERABLE
import random
token = random.randint(100000, 999999)
session_id = str(random.random())

# ✅ SAFE
import secrets
token = secrets.randbelow(1000000)
session_id = secrets.token_urlsafe(32)
```

**JavaScript**:
```javascript
// ❌ VULNERABLE
const token = Math.floor(Math.random() * 1000000);

// ✅ SAFE
const crypto = require('crypto');
const token = crypto.randomInt(0, 1000000);
const sessionId = crypto.randomBytes(32).toString('hex');
```

---

## Input Validation Patterns

### Missing Validation

**FastAPI**:
```python
# ❌ VULNERABLE
@app.post("/users")
async def create_user(username: str, age: int):
    user = User(username=username, age=age)
    db.add(user)
    
# ✅ SAFE
from pydantic import BaseModel, Field, validator

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, pattern="^[a-zA-Z0-9_]+$")
    age: int = Field(..., ge=0, le=150)
    
    @validator('username')
    def username_alphanumeric(cls, v):
        assert v.isalnum() or '_' in v, 'must be alphanumeric or underscore'
        return v

@app.post("/users")
async def create_user(user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
```

### Improper Sanitization

**React/Next.js**:
```typescript
// ❌ VULNERABLE
<div dangerouslySetInnerHTML={{ __html: userContent }} />
element.innerHTML = userInput;

// ✅ SAFE
import DOMPurify from 'dompurify';
<div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(userContent) }} />
element.textContent = userInput;
```

---

## Business Logic Patterns

### Race Conditions

**Python**:
```python
# ❌ VULNERABLE
def withdraw(user_id, amount):
    user = User.get(user_id)
    if user.balance >= amount:
        time.sleep(0.1)  # Processing
        user.balance -= amount
        user.save()

# ✅ SAFE
from django.db import transaction

def withdraw(user_id, amount):
    with transaction.atomic():
        user = User.objects.select_for_update().get(id=user_id)
        if user.balance >= amount:
            user.balance -= amount
            user.save()
```

### Time-of-Check Time-of-Use (TOCTOU)

**Python**:
```python
# ❌ VULNERABLE
if os.path.exists(filename):
    time.sleep(1)
    with open(filename, 'r') as f:
        data = f.read()

# ✅ SAFE
try:
    with open(filename, 'r') as f:
        data = f.read()
except FileNotFoundError:
    handle_missing_file()
```

---

## Configuration Patterns

### Permissive CORS

**Express**:
```javascript
// ❌ VULNERABLE
app.use(cors({ origin: '*' }));
app.use(cors({ origin: true, credentials: true }));

// ✅ SAFE
const allowedOrigins = process.env.ALLOWED_ORIGINS.split(',');
app.use(cors({
  origin: allowedOrigins,
  credentials: true,
  methods: ['GET', 'POST'],
  maxAge: 86400
}));
```

### Missing Security Headers

**Next.js**:
```typescript
// ❌ VULNERABLE
// No security headers configured

// ✅ SAFE
// next.config.js
module.exports = {
  async headers() {
    return [{
      source: '/(.*)',
      headers: [
        {
          key: 'X-Frame-Options',
          value: 'DENY'
        },
        {
          key: 'X-Content-Type-Options',
          value: 'nosniff'
        },
        {
          key: 'Strict-Transport-Security',
          value: 'max-age=63072000; includeSubDomains'
        },
        {
          key: 'Content-Security-Policy',
          value: "default-src 'self'; script-src 'self'"
        }
      ]
    }]
  }
}
```

---

## XSS Patterns

### Reflected XSS

**Express**:
```javascript
// ❌ VULNERABLE
app.get('/search', (req, res) => {
  res.send(`<h1>Results for: ${req.query.q}</h1>`);
});

// ✅ SAFE
const he = require('he');
app.get('/search', (req, res) => {
  const safeQuery = he.encode(req.query.q);
  res.send(`<h1>Results for: ${safeQuery}</h1>`);
});
```

### Stored XSS

**React**:
```typescript
// ❌ VULNERABLE
function Comment({ text }) {
  return <div dangerouslySetInnerHTML={{ __html: text }} />;
}

// ✅ SAFE
import DOMPurify from 'dompurify';

function Comment({ text }) {
  const sanitized = DOMPurify.sanitize(text);
  return <div dangerouslySetInnerHTML={{ __html: sanitized }} />;
}
```

### DOM-based XSS

**JavaScript**:
```javascript
// ❌ VULNERABLE
const params = new URLSearchParams(window.location.search);
document.getElementById('welcome').innerHTML = `Hello ${params.get('name')}`;

// ✅ SAFE
const params = new URLSearchParams(window.location.search);
document.getElementById('welcome').textContent = `Hello ${params.get('name')}`;
```

---

## Pattern Detection Rules

### Regular Expressions

**SQL Injection**:
```regex
execute\s*\(\s*f?["'].*\{.*\}.*["']
execute\s*\(\s*["'].*\+.*["']
\.format\s*\(.*SELECT.*FROM
```

**Command Injection**:
```regex
os\.system\s*\(\s*f?["']
subprocess\.call\s*\(.*shell\s*=\s*True
eval\s*\(
exec\s*\(
```

**Hardcoded Secrets**:
```regex
api[_-]?key\s*=\s*["'][a-zA-Z0-9]{20,}["']
password\s*=\s*["'][^"']{8,}["']
secret[_-]?key\s*=\s*["'][^"']+["']
(sk|pk)_live_[a-zA-Z0-9]{20,}
```

---

## Framework-Specific Patterns

### Next.js

```typescript
// ❌ Server component with client-side code
'use server'
export default function Page() {
  const apiKey = process.env.API_KEY;  // Exposed to client!
  return <div>{apiKey}</div>;
}

// ✅ Keep secrets server-side
'use server'
export default async function Page() {
  const data = await fetchDataWithKey();  // Server-only
  return <div>{data}</div>;
}
```

### FastAPI

```python
# ❌ Direct DB query from user input
@app.get("/search")
async def search(q: str):
    return db.execute(f"SELECT * FROM products WHERE name LIKE '%{q}%'")

# ✅ Parameterized with validation
from pydantic import BaseModel, constr

@app.get("/search")
async def search(q: constr(max_length=100, pattern="^[a-zA-Z0-9 ]+$")):
    return db.execute("SELECT * FROM products WHERE name LIKE ?", (f"%{q}%",))
```

---

## Summary

This patterns document should be used as a quick reference during:
- Code reviews
- Security audits
- Developer training
- Automated scanning tool configuration

Always consult the main README for complete context and remediation guidance.
