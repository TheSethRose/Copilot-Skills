# Security Review - Reference

Standards, frameworks, and resources for comprehensive security reviews.

## OWASP Top 10 (2021)

### A01:2021 – Broken Access Control
**What**: Restrictions on what authenticated users are allowed to do not properly enforced

**Checks**:
- Missing authorization checks
- Insecure direct object references (IDOR)
- Privilege escalation
- Force browsing to authenticated pages

**CWE Mapping**: CWE-200, CWE-201, CWE-352

---

### A02:2021 – Cryptographic Failures
**What**: Failures related to cryptography leading to sensitive data exposure

**Checks**:
- Weak hashing algorithms (MD5, SHA1)
- Hardcoded secrets
- Unencrypted data in transit/at rest
- Weak random number generation

**CWE Mapping**: CWE-259, CWE-327, CWE-759

---

### A03:2021 – Injection
**What**: User-supplied data not validated, filtered, or sanitized

**Checks**:
- SQL injection
- Command injection
- LDAP injection
- XPath/XML injection
- Template injection

**CWE Mapping**: CWE-79, CWE-89, CWE-917

---

### A04:2021 – Insecure Design
**What**: Missing or ineffective control design

**Checks**:
- Race conditions
- Business logic flaws
- Missing rate limiting
- Insufficient logging

**CWE Mapping**: CWE-209, CWE-256, CWE-501

---

### A05:2021 – Security Misconfiguration
**What**: Missing security hardening or improperly configured permissions

**Checks**:
- Missing security headers
- Permissive CORS
- Default credentials
- Debug mode in production
- Unnecessary features enabled

**CWE Mapping**: CWE-16, CWE-611

---

### A06:2021 – Vulnerable and Outdated Components
**What**: Use of components with known vulnerabilities

**Checks**:
- Outdated dependencies
- Vulnerable npm/pip packages
- Unmaintained libraries
- Missing security patches

**CWE Mapping**: CWE-1104

---

### A07:2021 – Identification and Authentication Failures
**What**: Broken authentication mechanisms

**Checks**:
- Weak password policies
- Insecure session management
- Missing MFA
- Credential stuffing vulnerabilities

**CWE Mapping**: CWE-287, CWE-384

---

### A08:2021 – Software and Data Integrity Failures
**What**: Code/infrastructure without protection against integrity violations

**Checks**:
- Insecure deserialization
- Unsigned updates
- CI/CD without validation
- Dependency confusion

**CWE Mapping**: CWE-502, CWE-829

---

### A09:2021 – Security Logging and Monitoring Failures
**What**: Insufficient logging, detection, monitoring, and response

**Checks**:
- Missing audit logs
- Insufficient log retention
- No alerting on security events
- Logs not protected

**CWE Mapping**: CWE-117, CWE-223, CWE-532

---

### A10:2021 – Server-Side Request Forgery (SSRF)
**What**: Fetching remote resources without validating URL

**Checks**:
- Unvalidated URL redirects
- Open redirects
- SSRF vulnerabilities
- DNS rebinding attacks

**CWE Mapping**: CWE-918

---

## CWE Top 25 (2023)

### Most Dangerous Software Weaknesses

1. **CWE-787**: Out-of-bounds Write
2. **CWE-79**: Cross-site Scripting (XSS)
3. **CWE-89**: SQL Injection
4. **CWE-416**: Use After Free
5. **CWE-78**: OS Command Injection
6. **CWE-20**: Improper Input Validation
7. **CWE-125**: Out-of-bounds Read
8. **CWE-22**: Path Traversal
9. **CWE-352**: CSRF
10. **CWE-434**: Unrestricted Upload
11. **CWE-862**: Missing Authorization
12. **CWE-476**: NULL Pointer Dereference
13. **CWE-287**: Improper Authentication
14. **CWE-190**: Integer Overflow
15. **CWE-502**: Deserialization of Untrusted Data
16. **CWE-77**: Command Injection
17. **CWE-119**: Buffer Errors
18. **CWE-798**: Hard-coded Credentials
19. **CWE-918**: SSRF
20. **CWE-306**: Missing Authentication
21. **CWE-362**: Race Condition
22. **CWE-269**: Improper Privilege Management
23. **CWE-94**: Code Injection
24. **CWE-863**: Incorrect Authorization
25. **CWE-276**: Incorrect Permissions

---

## Severity Levels

### Critical
- **Impact**: Immediate threat to system security
- **Examples**: RCE, SQL injection with auth bypass, exposed admin credentials
- **Response**: Fix immediately, deploy hotfix
- **CVSS**: 9.0-10.0

### High
- **Impact**: Significant security vulnerability
- **Examples**: Authentication bypass, privilege escalation, command injection
- **Response**: Fix within 24-48 hours
- **CVSS**: 7.0-8.9

### Medium
- **Impact**: Moderate security risk
- **Examples**: XSS, CSRF, information disclosure
- **Response**: Fix in next sprint
- **CVSS**: 4.0-6.9

### Low
- **Impact**: Minor security concern
- **Examples**: Missing headers, verbose errors, weak crypto in non-critical paths
- **Response**: Fix when convenient
- **CVSS**: 0.1-3.9

---

## Language-Specific Resources

### Python
- **Bandit**: Security linter
- **Safety**: Dependency checker
- **PyPI Advisory Database**: https://github.com/pypa/advisory-database

### JavaScript/TypeScript
- **npm audit**: Built-in vulnerability scanner
- **Snyk**: Comprehensive security platform
- **Node Security Project**: https://github.com/nodejs/security-wg

### Go
- **gosec**: Go security checker
- **govulncheck**: Official vulnerability scanner
- **Go Vulnerability Database**: https://vuln.go.dev/

---

## Framework-Specific Guidelines

### Next.js
**Common Issues**:
- Server component secrets exposed to client
- Missing authentication on API routes
- Insecure server actions
- CSP not configured

**Best Practices**:
- Use `getServerSession()` for auth
- Validate all `searchParams`
- Configure security headers
- Use middleware for route protection

### FastAPI
**Common Issues**:
- Missing Pydantic validation
- SQL injection in raw queries
- CORS misconfiguration
- Missing rate limiting

**Best Practices**:
- Use Pydantic models for all input
- Use SQLAlchemy ORM
- Configure CORS strictly
- Add rate limiting middleware

### Express
**Common Issues**:
- No helmet middleware
- Missing input validation
- Session misconfiguration
- Exposed error stack traces

**Best Practices**:
- Use helmet for security headers
- Validate with express-validator
- Secure session configuration
- Custom error handler

---

## Tools & Resources

### Static Analysis
- **Semgrep**: Multi-language static analysis
- **CodeQL**: GitHub's code analysis
- **SonarQube**: Code quality & security
- **Checkmarx**: Enterprise SAST

### Dependency Scanning
- **Dependabot**: GitHub's dependency alerts
- **Snyk**: Vulnerability database
- **OWASP Dependency-Check**: Multi-language
- **npm audit / pip-audit**: Package-specific

### Dynamic Testing
- **OWASP ZAP**: Web app scanner
- **Burp Suite**: Manual testing
- **Nuclei**: Fast vulnerability scanner

### Supply Chain Security
- **Sigstore**: Signing & verification
- **SLSA**: Supply chain levels
- **Syft & Grype**: SBOM generation & scanning

---

## Compliance & Standards

### Standards
- **OWASP ASVS**: Application Security Verification Standard
- **PCI DSS**: Payment Card Industry Data Security Standard
- **NIST 800-53**: Security and Privacy Controls
- **ISO 27001**: Information Security Management
- **SOC 2**: Service Organization Control

### Regulations
- **GDPR**: General Data Protection Regulation (EU)
- **CCPA**: California Consumer Privacy Act
- **HIPAA**: Health Insurance Portability and Accountability Act
- **SOX**: Sarbanes-Oxley Act

---

## CVE Databases

- **National Vulnerability Database**: https://nvd.nist.gov/
- **CVE.org**: https://www.cve.org/
- **GitHub Advisory Database**: https://github.com/advisories
- **Snyk Vulnerability Database**: https://snyk.io/vuln

---

## Security Testing Checklist

### Authentication & Session Management
- [ ] Strong password requirements
- [ ] Account lockout mechanism
- [ ] Secure session management
- [ ] MFA support
- [ ] Password reset flow secure
- [ ] Session timeout configured

### Authorization
- [ ] Role-based access control
- [ ] Resource-level permissions
- [ ] Horizontal privilege escalation prevented
- [ ] Vertical privilege escalation prevented

### Input Validation
- [ ] All input validated server-side
- [ ] Whitelist validation used
- [ ] File upload restrictions
- [ ] Size limits enforced

### Output Encoding
- [ ] HTML encoding for user content
- [ ] JSON encoding proper
- [ ] URL encoding where needed
- [ ] SQL parameterization

### Cryptography
- [ ] Strong algorithms (AES-256, RSA-2048+)
- [ ] Proper key management
- [ ] Secure random generation
- [ ] TLS 1.2+ enforced

### Configuration
- [ ] Security headers configured
- [ ] CORS properly restricted
- [ ] Debug mode disabled in production
- [ ] Unnecessary features disabled

### Error Handling
- [ ] Generic error messages to users
- [ ] Detailed errors logged securely
- [ ] No stack traces exposed
- [ ] HTTP status codes appropriate

### Logging & Monitoring
- [ ] Security events logged
- [ ] Logs protected from tampering
- [ ] Sensitive data not logged
- [ ] Alerting configured

---

## References

- **OWASP**: https://owasp.org/
- **CWE**: https://cwe.mitre.org/
- **NIST NVD**: https://nvd.nist.gov/
- **SANS Top 25**: https://www.sans.org/top25-software-errors/
- **Claude Security Review**: https://github.com/anthropics/claude-code-security-review

---

## Contribution

This reference is maintained as part of the Copilot Skills security review system. Contributions welcome for:
- New vulnerability patterns
- Framework-specific guidelines
- Tool recommendations
- Real-world examples
