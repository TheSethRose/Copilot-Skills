# Lazycommit Commit Patterns

Common commit message patterns and examples organized by type and scope.

## Feature Commits

### Authentication
```
feat(auth): add two-factor authentication
feat(auth): add password reset flow
feat(auth): add social login integration
feat(auth): add session management
feat(auth): add role-based access control
```

### API
```
feat(api): add user endpoint
feat(api): add pagination support
feat(api): add rate limiting
feat(api): add request validation
feat(api): add error response standardization
```

### UI/Components
```
feat(ui): add dark mode toggle
feat(ui): add responsive navigation
feat(ui): add form validation feedback
feat(ui): add loading states
feat(ui): add accessibility improvements
```

### Database
```
feat(db): add caching layer
feat(db): add database migrations
feat(db): add query optimization
feat(db): add connection pooling
feat(db): add data backups
```

### Performance
```
perf(cache): implement redis caching
perf(api): optimize database queries
perf(ui): add code splitting
perf(build): reduce bundle size
perf(render): memoize expensive components
```

## Bug Fix Commits

### Authentication
```
fix(auth): handle expired session tokens
fix(auth): fix token refresh logic
fix(auth): prevent session fixation attacks
fix(auth): fix password validation
fix(auth): fix logout flow
```

### API
```
fix(api): handle null pointer exception
fix(api): fix concurrent request handling
fix(api): prevent SQL injection
fix(api): fix error response format
fix(api): handle connection timeouts
```

### Database
```
fix(db): handle connection timeouts
fix(db): fix transaction rollback
fix(db): prevent deadlocks
fix(db): fix query timeout issues
fix(db): handle duplicate key errors
```

### UI
```
fix(ui): fix button alignment issue
fix(ui): fix form submission bug
fix(ui): fix responsive layout
fix(ui): fix z-index stacking
fix(ui): fix event handler memory leaks
```

## Refactor Commits

### Code Organization
```
refactor(api): extract validation logic
refactor(ui): componentize form inputs
refactor(auth): consolidate auth middleware
refactor(db): simplify query builder
refactor(utils): reorganize utility functions
```

### Type Safety
```
refactor(types): add strict type definitions
refactor(types): improve type inference
refactor(types): add generic type parameters
refactor(types): remove type assertions
```

### Performance
```
refactor(render): memoize components
refactor(queries): optimize database queries
refactor(cache): improve cache invalidation
refactor(assets): reorganize static files
```

### Testing
```
refactor(test): consolidate test utilities
refactor(test): improve test setup
refactor(test): remove duplicate tests
refactor(test): organize test suites
```

## Dependency/Build Commits

### Upgrades
```
chore(deps): upgrade typescript to 5.4
chore(deps): upgrade react to 18.3
chore(deps): upgrade express to 4.19
chore(deps): update security patches
chore(deps): bump all dependencies
```

### Build Configuration
```
chore(build): update webpack config
chore(build): configure babel
chore(build): add source maps
chore(build): optimize build output
```

### Development Tools
```
chore(eslint): update rules
chore(prettier): configure formatting
chore(husky): add pre-commit hooks
chore(jest): update test configuration
```

### CI/CD
```
chore(ci): add github actions workflow
chore(ci): update pipeline configuration
chore(ci): add automated testing
chore(ci): configure deployment
```

## Documentation Commits

### README
```
docs(readme): add installation instructions
docs(readme): update getting started guide
docs(readme): add api examples
docs(readme): improve troubleshooting section
```

### Code Comments
```
docs(types): add JSDoc comments
docs(api): document endpoint parameters
docs(utils): add function descriptions
docs(constants): document configuration
```

### Architecture
```
docs(architecture): document system design
docs(architecture): add data flow diagram
docs(architecture): explain module structure
docs(architecture): add deployment guide
```

## Style/Format Commits

### Code Style
```
style(format): format code with prettier
style(lint): fix eslint violations
style(spacing): fix indentation issues
style(naming): standardize variable names
```

### CSS/UI
```
style(button): fix spacing and alignment
style(form): improve input styling
style(colors): update color scheme
style(fonts): update typography
```

## Test Commits

### Unit Tests
```
test(auth): add login endpoint tests
test(utils): add validation function tests
test(db): add query builder tests
test(ui): add component rendering tests
```

### Integration Tests
```
test(api): add end-to-end api tests
test(flow): add user flow tests
test(integration): add database integration tests
```

### Coverage
```
test(coverage): increase test coverage
test(coverage): add missing tests
test(types): add type tests
```

## Complex/Multi-file Patterns

### Multiple Related Changes
```
feat(auth): add two-factor auth with email verification
  (Multiple files: models, api, ui, tests)

refactor(api): simplify error handling and logging
  (Multiple files: middleware, handlers, utils)

chore(deps): upgrade dev dependencies and tooling
  (Multiple files: package.json, config, CI)
```

### Cross-cutting Concerns
```
feat(types): add strict type definitions across codebase
refactor(test): reorganize test suites for clarity
chore(ci): update build and deployment pipeline
docs(api): document all public endpoints
```

## Anti-Patterns (What NOT to Do)

### ❌ Bad Messages
```
fix bugs                       ← Too vague
update files                   ← No context
changes                        ← Meaningless
updated auth                   ← Past tense
fixed the thing                ← Vague
misc updates                   ← Generic
Work in progress               ← Not finished
TODO                          ← Incomplete
```

### ❌ Format Issues
```
feat: add feature             ← Missing scope
feat(auth-service): ...       ← Scope too long
feat(auth): Add feature       ← Capital letter
feat(auth): add feature.      ← Period at end
FEAT(AUTH): ADD FEATURE       ← All caps
feat: Add feature that does something very long and complex and complicated
  ← Message too long
```

### ❌ Scope Issues
```
feat(my-new-feature-branch): ...  ← Too long
feat(): ...                       ← Empty scope
feat(a): ...                      ← Too short/unclear
feat(authentication-and-authorization): ...  ← Too long/complex
```

## Good vs Bad Examples

### Feature Example
```
❌ Bad:    feat: updated auth
✅ Good:   feat(auth): add two-factor authentication

❌ Bad:    FEAT(AUTH): ADD TWO FACTOR AUTHENTICATION
✅ Good:   feat(auth): add two-factor authentication

❌ Bad:    feat(authentication): added new 2FA flow with email and SMS support
✅ Good:   feat(auth): add two-factor authentication
```

### Fix Example
```
❌ Bad:    fix: fixed bug
✅ Good:   fix(db): handle connection timeouts gracefully

❌ Bad:    fix the api
✅ Good:   fix(api): prevent null pointer exception

❌ Bad:    Fix(UI): Fix button
✅ Good:   fix(ui): fix button alignment issue
```

### Chore Example
```
❌ Bad:    chore: update stuff
✅ Good:   chore(deps): upgrade typescript to 5.4

❌ Bad:    chore(dependencies): Upgraded packages
✅ Good:   chore(deps): upgrade express and related packages

❌ Bad:    chore: bump versions
✅ Good:   chore(deps): bump all dependencies
```

## Scope Selection Guide

### Single Directory
```
3+ files in src/auth/
  → scope: auth

3+ files in src/api/
  → scope: api

3+ files in src/ui/pages/
  → scope: pages
```

### Mixed Directories
```
Changes across multiple dirs?
  Pick the primary one (most files)
  
If equal distribution:
  Pick by priority:
  auth > api > ui > db > config > chore
```

### Special Cases
```
package.json only
  → scope: deps

config files only
  → scope: config

docs only
  → scope: docs

tests only
  → scope: test or specific feature: test(auth)

Multiple unrelated changes
  → Consider committing separately!
```

## Size Indicators

### Scope
- **Short**: 1-2 words, <20 characters
  - ✓ auth, api, ui, db, deps, build
  - ✗ authentication, user-service, validation-middleware

- **Medium**: Feature-specific
  - ✓ auth, payments, dashboard, profile
  - ✗ authentication-and-authorization

### Subject
- **Ideal**: <50 characters
  - ✓ add password reset flow
  - ✓ fix null pointer exception

- **Maximum**: <90 characters
  - ✓ add two-factor authentication with email and SMS support
  - ✗ add feature that handles multiple different scenarios across various parts of system

### Type
- **Always present**: feat, fix, docs, style, refactor, perf, test, chore
- **Lowercase** after type and scope
- **Imperative mood**: add, fix, remove, update, refactor, improve

---

**Use these patterns as templates when committing changes.**
