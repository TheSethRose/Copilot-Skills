# Security Review Instructions

Auto-loaded when working with security-sensitive code or conducting security reviews.

## Activation

This file loads automatically when:
- Editing authentication/authorization code
- Working with database queries
- Handling user input or API endpoints
- Reviewing cryptographic implementations
- Auditing dependencies or package files
- Analyzing security configurations

## File Patterns

- `**/auth*` - Authentication code
- `**/login*` - Login handlers
- `**/*security*` - Security modules
- `**/api/**` - API endpoints
- `**/middleware/**` - Middleware (auth, CORS, etc.)
- `**/*crypto*` - Cryptographic code
- `**/requirements.txt` - Python dependencies
- `**/package.json` - Node.js dependencies
- `**/go.mod` - Go dependencies
- `**/Cargo.toml` - Rust dependencies

## Quick Security Checks

When reviewing code, automatically check for:

### 1. Injection Vulnerabilities
- String concatenation in SQL queries
- `eval()`, `exec()`, `subprocess` with user input
- Unsanitized template rendering

### 2. Authentication Issues
- Missing authentication middleware
- Weak session configuration
- Insecure password storage
- Missing authorization checks

### 3. Data Exposure
- Hardcoded API keys, passwords, tokens
- Sensitive data in logs
- Stack traces exposed to users
- PII without proper handling

### 4. Cryptography
- MD5, SHA1 for passwords (use bcrypt/pbkdf2)
- `random` instead of `secrets`
- Weak encryption algorithms

### 5. Input Validation
- Missing validation on user input
- Type confusion risks
- Buffer overflow potential

## Quick Reference

### Run Security Scan
```bash
bash .github/copilot-skills/security/security-review/scripts/scan.sh --path .
```

### Check Specific Category
```bash
# Injection
bash scan.sh --path . --category injection

# Secrets
bash scan.sh --path . --category secrets

# Dependencies
python3 analyze_dependencies.py .
```

## Common Patterns to Flag

### Python
```python
# ⚠️ Flag these patterns
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
os.system(f"ls {path}")
API_KEY = "sk_live_1234567890"
hashlib.md5(password.encode())
random.randint(1000, 9999)
```

### JavaScript/TypeScript
```javascript
// ⚠️ Flag these patterns
db.query(`SELECT * FROM users WHERE email = '${email}'`)
eval(userCode)
const API_KEY = "pk_test_1234567890"
Math.random()  // For security tokens
<div dangerouslySetInnerHTML={{ __html: userInput }} />
```

## Remediation Quick Guide

### SQL Injection → Parameterized Queries
```python
# Instead of:
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")

# Use:
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
```

### Command Injection → Array Arguments
```python
# Instead of:
os.system(f"ls {path}")

# Use:
subprocess.run(["ls", path])
```

### Hardcoded Secrets → Environment Variables
```python
# Instead of:
API_KEY = "sk_live_..."

# Use:
API_KEY = os.environ.get("API_KEY")
```

### Weak Hashing → Strong Algorithms
```python
# Instead of:
hashlib.md5(password.encode())

# Use:
bcrypt.hashpw(password.encode(), bcrypt.gensalt())
```

### Insecure Random → Cryptographic Random
```python
# Instead of:
random.randint(1000, 9999)

# Use:
secrets.randbelow(10000)
```

## Default Security Recommendations

When reviewing code, always recommend:

1. **Authentication** - Verify on every protected route
2. **Authorization** - Check user permissions for resources
3. **Input Validation** - Validate all user input
4. **Output Encoding** - Sanitize before rendering
5. **Parameterized Queries** - Never concatenate SQL
6. **Environment Variables** - For all secrets
7. **Strong Cryptography** - bcrypt, secrets module
8. **Security Headers** - CSP, HSTS, X-Frame-Options
9. **HTTPS Only** - Secure flag on cookies
10. **Dependency Updates** - Keep packages current

## Documentation

For complete security review documentation:
- **Main Guide**: `.github/copilot-skills/security/security-review/README.md`
- **Pattern Examples**: `.github/copilot-skills/security/security-review/patterns.md`
- **Run Scan**: Use `/security-review` skill

## Framework-Specific Notes

### Next.js
- Use `getServerSession()` for auth
- Keep secrets in server components only
- Validate `searchParams` and route params
- Configure security headers in `next.config.js`

### FastAPI
- Use `Depends(get_current_user)` for auth
- Pydantic models for validation
- `HTTPException` for errors (no stack traces)
- Configure CORS properly

### Express
- Use authentication middleware
- Helmet for security headers
- Express-validator for input
- Proper error handling (no stack traces)

## CI/CD Integration

Recommend adding to workflows:
```yaml
- name: Security Scan
  run: bash .github/copilot-skills/security/security-review/scripts/scan.sh --format json --exit-code 1
```

## When to Escalate

Recommend immediate attention for:
- 🔴 **Critical**: Remote code execution, SQL injection with auth bypass
- 🟠 **High**: Authentication bypass, exposed secrets, command injection
- 🟡 **Medium**: XSS, CSRF, weak crypto
- 🟢 **Low**: Information disclosure, missing headers

## Resources

- OWASP Top 10: https://owasp.org/www-project-top-ten/
- CWE: https://cwe.mitre.org/
- Security Review Skill: `/security-review`
