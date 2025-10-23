# Security Review Skill

Comprehensive security analysis system for codebases across multiple languages and frameworks.

## Overview

This skill provides automated security reviews that detect vulnerabilities, misconfigurations, and security anti-patterns across your entire codebase. It adapts to different languages (Python, JavaScript/TypeScript, Go, etc.) and frameworks (Next.js, FastAPI, Express, etc.) to provide contextual, actionable security feedback.

## What This Does

- **Detects 10+ vulnerability categories** across all OWASP Top 10
- **Language-agnostic scanning** with framework-specific rules
- **Actionable remediation** with code examples
- **Risk-based prioritization** (Critical/High/Medium/Low)
- **Supply chain analysis** for vulnerable dependencies
- **Secret detection** with pattern matching
- **Configuration auditing** for security headers, CORS, etc.
- **CI/CD integration** ready

## Quick Start

### Run Full Security Scan

```bash
cd .github/copilot-skills/security/security-review/scripts
bash scan.sh --path /path/to/project
```

### Scan Specific Categories

```bash
# Check for secrets only
bash scan.sh --path . --category secrets

# Check injection vulnerabilities
bash scan.sh --path . --category injection

# Check dependencies
bash scan.sh --path . --category dependencies
```

### Generate Report

```bash
# Terminal output (default)
bash scan.sh --path . --format terminal

# JSON for CI/CD
bash scan.sh --path . --format json

# Markdown report
bash scan.sh --path . --format markdown
```

## Security Categories

### 1. Injection Attacks

**What it checks**:
- SQL injection (raw queries, string concatenation)
- Command injection (subprocess, eval, exec)
- LDAP injection (directory search queries)
- XPath injection (XML queries)
- NoSQL injection (MongoDB, etc.)
- XXE (XML External Entity) attacks

**Languages covered**: Python, JavaScript/TypeScript, Go, PHP, Java

**Example patterns**:
```python
# ❌ Vulnerable
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
subprocess.run(f"ls {user_input}", shell=True)

# ✅ Safe
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
subprocess.run(["ls", user_input])
```

### 2. Authentication & Authorization

**What it checks**:
- Broken authentication (weak session handling)
- Privilege escalation (missing role checks)
- Insecure direct object references (IDOR)
- Authorization bypass logic
- Session management flaws
- JWT vulnerabilities

**Frameworks covered**: Next.js (NextAuth), Express, FastAPI, Django, etc.

**Example patterns**:
```typescript
// ❌ Vulnerable - No auth check
app.get('/api/user/:id', (req, res) => {
  const user = db.getUser(req.params.id);
  res.json(user);
});

// ✅ Safe - With auth middleware
app.get('/api/user/:id', authenticateUser, authorizeUser, (req, res) => {
  if (req.user.id !== req.params.id && !req.user.isAdmin) {
    return res.status(403).json({ error: 'Forbidden' });
  }
  const user = db.getUser(req.params.id);
  res.json(user);
});
```

### 3. Data Exposure

**What it checks**:
- Hardcoded secrets (API keys, passwords, tokens)
- Sensitive data in logs
- Information disclosure (stack traces, debug info)
- PII handling violations
- Unencrypted sensitive data storage

**Pattern detection**:
- API keys, tokens, credentials
- Database connection strings
- Private keys, certificates
- Sensitive variable names

**Example patterns**:
```python
# ❌ Vulnerable
API_KEY = "sk_live_1234567890abcdef"
logger.info(f"User password: {password}")

# ✅ Safe
API_KEY = os.environ.get("API_KEY")
logger.info("User authentication attempt")
```

### 4. Cryptographic Issues

**What it checks**:
- Weak algorithms (MD5, SHA1, DES)
- Improper key management
- Insecure random number generation
- Missing encryption for sensitive data
- Weak password hashing

**Example patterns**:
```python
# ❌ Vulnerable
import md5
hash = md5.new(password).hexdigest()
random_token = random.randint(1000, 9999)

# ✅ Safe
import hashlib
hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
import secrets
random_token = secrets.token_urlsafe(32)
```

### 5. Input Validation

**What it checks**:
- Missing input validation
- Improper sanitization
- Buffer overflows
- Type confusion
- Mass assignment vulnerabilities

**Example patterns**:
```javascript
// ❌ Vulnerable
const userId = req.query.id;  // No validation
const html = `<div>${userInput}</div>`;  // No sanitization

// ✅ Safe
const userId = parseInt(req.query.id, 10);
if (isNaN(userId) || userId < 1) throw new Error('Invalid ID');
const html = DOMPurify.sanitize(userInput);
```

### 6. Business Logic Flaws

**What it checks**:
- Race conditions (TOCTOU)
- Time-of-check-time-of-use issues
- Logic bypass vulnerabilities
- Price manipulation
- Quantity manipulation

**Example patterns**:
```python
# ❌ Vulnerable - Race condition
if user.balance >= amount:
    time.sleep(1)  # Processing delay
    user.balance -= amount
    
# ✅ Safe - Atomic operation
with transaction.atomic():
    user = User.objects.select_for_update().get(id=user_id)
    if user.balance >= amount:
        user.balance -= amount
        user.save()
```

### 7. Configuration Security

**What it checks**:
- Insecure defaults
- Missing security headers (CSP, HSTS, X-Frame-Options)
- Permissive CORS policies
- Debug mode in production
- Exposed admin interfaces

**Framework-specific**: Next.js, Express, FastAPI, Django

**Example checks**:
```javascript
// ❌ Vulnerable
app.use(cors({ origin: '*' }));
app.set('trust proxy', true);  // Without validation

// ✅ Safe
app.use(cors({ origin: process.env.ALLOWED_ORIGINS.split(',') }));
app.use(helmet());  // Security headers
```

### 8. Supply Chain Security

**What it checks**:
- Vulnerable dependencies (CVEs)
- Typosquatting risks
- Unmaintained packages
- License violations
- Dependency confusion

**Package managers**: npm, pip, go mod, cargo

**Example output**:
```
🔴 CRITICAL: lodash@4.17.15 - Prototype Pollution (CVE-2020-8203)
  Fix: npm install lodash@4.17.21
  
⚠️  MEDIUM: express@4.16.0 - Outdated (latest: 4.18.2)
  Fix: npm install express@latest
```

### 9. Code Execution Vulnerabilities

**What it checks**:
- RCE via deserialization (pickle, YAML)
- eval() usage
- exec() with user input
- Unsafe template rendering
- Dynamic code loading

**Example patterns**:
```python
# ❌ Vulnerable
import pickle
data = pickle.loads(user_input)
eval(user_code)

# ✅ Safe
import json
data = json.loads(user_input)
# Use sandboxed execution or avoid dynamic code
```

### 10. Cross-Site Scripting (XSS)

**What it checks**:
- Reflected XSS (URL parameters)
- Stored XSS (database content)
- DOM-based XSS (client-side)
- Template injection
- Unsafe HTML rendering

**Frameworks**: React, Vue, Next.js, Django templates

**Example patterns**:
```typescript
// ❌ Vulnerable
<div dangerouslySetInnerHTML={{ __html: userContent }} />
document.getElementById('output').innerHTML = userInput;

// ✅ Safe
<div>{sanitize(userContent)}</div>
document.getElementById('output').textContent = userInput;
```

## Usage Workflows

### Workflow 1: Quick Project Scan

```bash
# Scan entire project
cd your-project-root
bash /path/to/scan.sh --path .

# Review findings
# Fix critical issues first
# Re-scan to verify
```

### Workflow 2: Pre-Commit Check

```bash
# Add to .git/hooks/pre-commit
#!/bin/bash
bash .github/copilot-skills/security/security-review/scripts/scan.sh \
  --path . \
  --severity critical,high \
  --exit-code 1
```

### Workflow 3: CI/CD Integration

```yaml
# .github/workflows/security.yml
- name: Security Scan
  run: |
    bash .github/copilot-skills/security/security-review/scripts/scan.sh \
      --path . \
      --format json \
      --output security-report.json
```

### Workflow 4: Targeted Category Scan

```bash
# Check specific vulnerabilities
bash scan.sh --path . --category injection
bash scan.sh --path . --category secrets
bash scan.sh --path . --category xss
```

### Workflow 5: Framework-Specific Review

```bash
# Next.js project
bash scan.sh --path . --framework nextjs

# FastAPI project
bash scan.sh --path . --framework fastapi

# Express project
bash scan.sh --path . --framework express
```

## Script Reference

### scan.sh

Main entry point for security scans.

**Usage**:
```bash
bash scan.sh [OPTIONS]
```

**Options**:
- `--path PATH` - Project path to scan (default: current directory)
- `--category CAT` - Specific category: injection, auth, secrets, crypto, etc.
- `--severity SEV` - Filter by severity: critical, high, medium, low
- `--framework FW` - Framework: nextjs, fastapi, express, django, etc.
- `--format FMT` - Output format: terminal, json, markdown
- `--output FILE` - Output file path
- `--exit-code CODE` - Exit code on findings (for CI/CD)
- `--exclude PATTERN` - Exclude paths (glob pattern)

**Examples**:
```bash
# Full scan
bash scan.sh --path /project

# Critical findings only
bash scan.sh --path . --severity critical,high

# JSON output for CI/CD
bash scan.sh --path . --format json --exit-code 1

# Exclude test files
bash scan.sh --path . --exclude "**/*test*,**/node_modules/**"
```

### analyze_dependencies.py

Checks for vulnerable dependencies.

**Usage**:
```bash
python3 analyze_dependencies.py [PATH]
```

**What it does**:
- Scans package.json, requirements.txt, go.mod, Cargo.toml
- Checks against CVE databases
- Identifies outdated packages
- Detects typosquatting risks

### scan_secrets.py

Detects hardcoded secrets.

**Usage**:
```bash
python3 scan_secrets.py [PATH]
```

**Patterns detected**:
- API keys, tokens
- Database credentials
- Private keys
- OAuth secrets
- Cloud provider credentials

### check_injection.py

Analyzes code for injection vulnerabilities.

**Usage**:
```bash
python3 check_injection.py [PATH] [--lang LANGUAGE]
```

**Languages**: python, javascript, typescript, go, php, java

### generate_report.py

Generates formatted security reports.

**Usage**:
```bash
python3 generate_report.py [--input FILE] [--format FORMAT]
```

**Formats**: terminal, json, markdown, html

## Output Format

### Terminal Output

```
🔒 Security Review Report
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Summary:
  🔴 Critical: 2
  🟠 High: 5
  🟡 Medium: 12
  🟢 Low: 8
  
🔴 CRITICAL FINDINGS:

[1] SQL Injection in user authentication
  File: src/auth.py:45
  Pattern: cursor.execute(f"SELECT * FROM users WHERE email = '{email}'")
  CWE: CWE-89
  OWASP: A03:2021 – Injection
  
  🔧 Remediation:
  Use parameterized queries:
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    
  📚 References:
  - https://owasp.org/www-community/attacks/SQL_Injection
  - CWE-89: https://cwe.mitre.org/data/definitions/89.html

[2] Hardcoded API Key
  File: config/settings.py:12
  Pattern: API_KEY = "sk_live_a1b2c3d4e5f6"
  CWE: CWE-798
  OWASP: A02:2021 – Cryptographic Failures
  
  🔧 Remediation:
  Use environment variables:
    API_KEY = os.environ.get("API_KEY")
    
  📚 References:
  - https://owasp.org/www-project-top-ten/2017/A3_2017-Sensitive_Data_Exposure
```

### JSON Output

```json
{
  "summary": {
    "total": 27,
    "critical": 2,
    "high": 5,
    "medium": 12,
    "low": 8
  },
  "findings": [
    {
      "id": "INJ-001",
      "severity": "critical",
      "category": "injection",
      "subcategory": "sql",
      "title": "SQL Injection in user authentication",
      "file": "src/auth.py",
      "line": 45,
      "code": "cursor.execute(f\"SELECT * FROM users WHERE email = '{email}'\")",
      "cwe": "CWE-89",
      "owasp": "A03:2021",
      "remediation": "Use parameterized queries",
      "references": [
        "https://owasp.org/www-community/attacks/SQL_Injection"
      ]
    }
  ]
}
```

## Integration Examples

### GitHub Actions

```yaml
name: Security Review

on: [push, pull_request]

jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Run Security Scan
        run: |
          bash .github/copilot-skills/security/security-review/scripts/scan.sh \
            --path . \
            --format json \
            --output security-report.json \
            --exit-code 1
            
      - name: Upload Report
        uses: actions/upload-artifact@v3
        with:
          name: security-report
          path: security-report.json
```

### Pre-Commit Hook

```bash
#!/bin/bash
# .git/hooks/pre-commit

echo "🔒 Running security checks..."

bash .github/copilot-skills/security/security-review/scripts/scan.sh \
  --path . \
  --severity critical,high \
  --format terminal

if [ $? -ne 0 ]; then
  echo "❌ Security issues found. Commit blocked."
  echo "Fix critical/high issues or use --no-verify to skip"
  exit 1
fi

echo "✅ Security checks passed"
```

## Language & Framework Support

### Supported Languages

- **Python** - Django, Flask, FastAPI
- **JavaScript/TypeScript** - Node.js, Express, Next.js, React
- **Go** - Gin, Echo, standard library
- **PHP** - Laravel, Symfony
- **Java** - Spring Boot
- **Ruby** - Rails

### Framework-Specific Rules

Each framework has custom rules for common patterns:

- **Next.js**: API routes, server actions, middleware
- **FastAPI**: Dependency injection, Pydantic models
- **Express**: Middleware chains, route handlers
- **Django**: ORM queries, templates, views

## Configuration

Create `.security-review.yml` in project root:

```yaml
# Exclude paths
exclude:
  - "**/node_modules/**"
  - "**/venv/**"
  - "**/*test*"
  - "**/dist/**"

# Severity thresholds
fail_on:
  - critical
  - high

# Custom patterns
custom_patterns:
  - name: "Internal API Key"
    pattern: "INTERNAL_KEY_[A-Z0-9]{32}"
    severity: high
    
# Framework detection
framework: auto  # or: nextjs, fastapi, express, etc.

# Categories to check
categories:
  - injection
  - auth
  - secrets
  - crypto
  - xss
  - dependencies
```

## Best Practices

### For Developers

1. **Run locally before commit** - Catch issues early
2. **Fix by severity** - Critical → High → Medium → Low
3. **Review all findings** - Some may be false positives
4. **Add to CI/CD** - Automated checks on every push
5. **Regular scans** - Weekly/monthly full scans

### For Teams

1. **Establish baseline** - Document initial findings
2. **Track metrics** - Monitor security debt over time
3. **Security champions** - Designate reviewers
4. **Regular training** - Educate on common patterns
5. **Integrate tools** - Complement with SCA tools (Snyk, Dependabot)

## Troubleshooting

### High False Positive Rate

```bash
# Add exclusions
bash scan.sh --path . --exclude "**/test/**,**/mock/**"

# Review patterns
# Edit scripts/check_injection.py to tune patterns
```

### Performance Issues

```bash
# Scan specific directories
bash scan.sh --path src/

# Single category
bash scan.sh --path . --category secrets

# Exclude large dirs
bash scan.sh --path . --exclude "**/node_modules/**"
```

### Missing Vulnerabilities

```bash
# Enable all categories
bash scan.sh --path . --category all

# Lower severity threshold
bash scan.sh --path . --severity low

# Check framework detection
bash scan.sh --path . --framework auto --verbose
```

## References

- **OWASP Top 10**: https://owasp.org/www-project-top-ten/
- **CWE List**: https://cwe.mitre.org/
- **NIST NVD**: https://nvd.nist.gov/
- **Claude Security Review**: https://github.com/anthropics/claude-code-security-review

## Related Skills

- `/create-skill` - Customize this skill for your needs
- `/web-research` - Research specific vulnerabilities
- `/git-ops` - Safe commits after security fixes

## License

MIT - Use and modify freely
