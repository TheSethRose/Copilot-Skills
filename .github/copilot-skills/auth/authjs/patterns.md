# Authjs - Common Patterns

Quick reference for common authjs patterns and usage.

## Code Patterns

## Examples

### Example 1

```python
import NextAuth from "next-auth";
import AzureADB2C from "next-auth/providers/azure-ad-b2c";
 
export const { handlers, auth, signIn, signOut } = NextAuth({
  providers: [AzureADB2C({
    clientId: AUTH_AZURE_AD_B2C_CLIENT_ID
    clientSecret: AUTH_AZURE_AD_B2C_CLIENT_SECRET
    issuer: AUTH_AZURE_AD_B2C_ISSUER
  })]
});
```


## Categories

See organized documentation in `references/`:

- `references/getting_started.md` - Getting Started
