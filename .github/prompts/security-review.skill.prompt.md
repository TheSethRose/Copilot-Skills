# Security Review

**Purpose**: Comprehensive automated security analysis for codebases across multiple languages and frameworks

## When to Use This Skill

Use this skill when:
- Reviewing code for security vulnerabilities
- Performing pre-commit security checks
- Setting up CI/CD security scans
- Investigating specific security concerns
- Auditing third-party dependencies
- Checking for hardcoded secrets
- Validating authentication/authorization logic
- Reviewing input validation and sanitization
- Assessing cryptographic implementations
- Analyzing business logic for race conditions

## Quick Reference

**Keywords**: security, vulnerability, owasp, injection, xss, authentication, secrets, crypto, cve, security review, security audit, penetration testing, secure code

**Coverage**:
- **10 OWASP Categories** - All Top 10 vulnerabilities
- **Multiple Languages** - Python, JavaScript/TypeScript, Go, PHP, Java, Ruby
- **Framework-Aware** - Next.js, FastAPI, Express, Django, Rails
- **Actionable Output** - CWE/OWASP mapped, remediation included
- **CI/CD Ready** - JSON/Markdown output, exit codes

## How to Use This Skill

### 1. Full Project Scan
**User asks**: "Run security scan on my project" or "Check for vulnerabilities"

**Action**:
```bash
cd .github/copilot-skills/security/security-review/scripts
bash scan.sh --path /path/to/project
```

Output shows all findings with severity, file locations, and remediation steps.

### 2. Category-Specific Check
**User asks**: "Check for SQL injection" or "Scan for hardcoded secrets"

**Action**:
```bash
bash scan.sh --path . --category injection
bash scan.sh --path . --category secrets
```

Focuses on specific vulnerability types.

### 3. Pre-Commit Check
**User asks**: "Set up security checks before commits"

**Action**:
- Add hook to `.git/hooks/pre-commit`
- Configure to block on critical/high severity
- Show findings in terminal

### 4. CI/CD Integration
**User asks**: "Add security scanning to GitHub Actions"

**Action**:
- Generate workflow YAML
- Configure JSON output
- Set exit codes for pipeline failure

### 5. Dependency Audit
**User asks**: "Check for vulnerable dependencies"

**Action**:
```bash
python3 analyze_dependencies.py /path/to/project
```

Shows CVEs, outdated packages, and update recommendations.

### 6. Framework-Specific Review
**User asks**: "Security review for Next.js app"

**Action**:
```bash
bash scan.sh --path . --framework nextjs
```

Applies Next.js-specific rules (server components, API routes, middleware).

## Security Categories

1. **Injection Attacks** - SQL, Command, NoSQL, LDAP, XPath, XXE
2. **Authentication & Authorization** - Broken auth, privilege escalation, IDOR
3. **Data Exposure** - Secrets, logging, PII, information disclosure
4. **Cryptographic Issues** - Weak algorithms, key management, random generation
5. **Input Validation** - Missing validation, improper sanitization
6. **Business Logic** - Race conditions, TOCTOU issues
7. **Configuration** - Insecure defaults, missing headers, CORS
8. **Supply Chain** - Vulnerable dependencies, typosquatting
9. **Code Execution** - RCE, deserialization, eval injection
10. **XSS** - Reflected, stored, DOM-based

## Common Workflows

### Workflow 1: Initial Security Assessment
```
1. Run full scan: bash scan.sh --path .
2. Review critical/high findings
3. Check patterns.md for examples
4. Fix vulnerabilities
5. Re-scan to verify
```

### Workflow 2: Targeted Investigation
```
1. User reports concern (e.g., "SQL injection risk")
2. Run category scan: bash scan.sh --category injection
3. Review specific findings
4. Show remediation from patterns.md
5. Verify fix with re-scan
```

### Workflow 3: CI/CD Setup
```
1. Generate GitHub Actions workflow
2. Configure severity thresholds
3. Set JSON output format
4. Test locally first
5. Add to repository
```

### Workflow 4: Dependency Security
```
1. Run: python3 analyze_dependencies.py .
2. Review CVEs and severity
3. Update vulnerable packages
4. Re-scan to confirm
```

### Workflow 5: Framework Migration Security
```
1. Specify framework: bash scan.sh --framework nextjs
2. Review framework-specific issues
3. Check patterns.md for safe alternatives
4. Fix and validate
```

## Documentation Location

```
.github/copilot-skills/security/security-review/
├── README.md              # Complete documentation
├── patterns.md           # Vulnerability patterns with examples
├── reference.md          # Standards and references
├── scripts/
│   ├── scan.sh          # Main scan entry point
│   ├── analyze_dependencies.py
│   ├── scan_secrets.py
│   ├── check_injection.py
│   └── generate_report.py
└── references/
    ├── owasp-top-10.md
    ├── cwe-mapping.md
    └── remediation-guide.md
```

## Script Options

### scan.sh
```bash
--path PATH          # Project to scan (default: .)
--category CAT       # injection, auth, secrets, etc.
--severity SEV       # critical, high, medium, low
--framework FW       # nextjs, fastapi, express, etc.
--format FMT         # terminal, json, markdown
--output FILE        # Output file path
--exit-code N        # Exit code on findings
--exclude PATTERN    # Exclude paths
```

### Example Commands
```bash
# Full scan
bash scan.sh --path .

# Critical only
bash scan.sh --severity critical,high

# JSON for CI/CD
bash scan.sh --format json --exit-code 1

# Exclude tests
bash scan.sh --exclude "**/*test*"
```

## Output Format

### Terminal (Default)
```
🔒 Security Review Report
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Summary:
  🔴 Critical: 2
  🟠 High: 5
  🟡 Medium: 12
  🟢 Low: 8

🔴 [1] SQL Injection in auth
  File: src/auth.py:45
  CWE: CWE-89
  OWASP: A03:2021
  
  🔧 Remediation:
  Use parameterized queries
  
  📚 References:
  - https://owasp.org/...
```

### JSON (CI/CD)
```json
{
  "summary": {
    "total": 27,
    "critical": 2,
    "high": 5
  },
  "findings": [{
    "severity": "critical",
    "category": "injection",
    "file": "src/auth.py",
    "line": 45,
    "remediation": "...",
    "cwe": "CWE-89"
  }]
}
```

## Integration Examples

### GitHub Actions
```yaml
- name: Security Scan
  run: |
    bash .github/copilot-skills/security/security-review/scripts/scan.sh \
      --format json --exit-code 1
```

### Pre-Commit Hook
```bash
bash .github/copilot-skills/security/security-review/scripts/scan.sh \
  --severity critical,high --exit-code 1
```

## Success Indicators

✅ You've successfully used this skill when:
- Security vulnerabilities are identified with file/line precision
- Remediation steps are clear and actionable
- Severity levels help prioritize fixes
- CI/CD integration prevents vulnerable code from merging
- Dependency vulnerabilities are tracked and updated
- Team understands security patterns to avoid

## Tips

✅ **Do**:
- Run scans regularly (pre-commit, CI/CD, weekly)
- Fix by severity: Critical → High → Medium → Low
- Review patterns.md for examples
- Validate fixes with re-scan
- Track security debt over time

❌ **Don't**:
- Ignore findings without investigation
- Skip validation of proposed fixes
- Assume all findings are false positives
- Forget to update dependencies
- Deploy without passing security checks

## Related Skills

- `/create-skill` - Customize security rules for your stack
- `/web-research` - Research specific CVEs or vulnerabilities
- `/git-ops` - Safe commits after security fixes

## Configuration

Create `.security-review.yml`:
```yaml
exclude:
  - "**/node_modules/**"
  - "**/test/**"

fail_on:
  - critical
  - high

framework: auto  # or nextjs, fastapi, etc.

categories:
  - injection
  - auth
  - secrets
  - crypto
  - xss
```

## Resources

- **Full Documentation**: `.github/copilot-skills/security/security-review/README.md`
- **Patterns Guide**: `patterns.md`
- **OWASP Top 10**: https://owasp.org/www-project-top-ten/
- **Claude Security Review**: https://github.com/anthropics/claude-code-security-review
