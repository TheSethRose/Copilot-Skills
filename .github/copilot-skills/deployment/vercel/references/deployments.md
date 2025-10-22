# Vercel - Deployments

**Pages**: 5

---

## Build Features for Customizing Deployments

**URL**: https://vercel.com/docs/builds/build-features

**Contents**:
- Build Features for Customizing Deployments
- Private npm packages
- Ignored files and folders
- Special paths
  - Source View
  - Logs View
  - Security considerations
- Git submodules

Vercel provides the following features to customize your deployments:

When your project's code is using private npm modules that require authentication, you need to perform an additional step to install private modules.

To install private npm modules, define NPM_TOKEN as an Environment Variable in your project. Alternatively, define NPM_RC as an Environment Variable in the contents of the project's npmrc config file that resides at the root of the project folder and is named ~/.npmrc. This file defines the config settings of npm at the level of the project.

To learn more, check out the guide here if you need help configuring private dependencies.

Vercel ignores certain files and folders by default and prevents them from being uploaded during the deployment process for security and performance reasons. Please note that these ignored files are only relevant when using Vercel CLI.

A complete list of files and folders ignored by Vercel during the Deployment process.

The .vercel/output directory is not ignored when vercel deploy --prebuilt is used to deploy a prebuilt Vercel Project, according to the Build Output API specification.

You do not need to add any of the above files and folders to your .vercelignore file because it is done automatically by Vercel.

Vercel allows you to access the source code and build logs for your deployment using special pathnames for Build Logs and Source Protection. You can access this option from your project's Security settings.

All deployment URLs have two special pathnames to access the source code and the build logs:

By default, these routes are protected so that they can only be accessed by you and the members of your Vercel Team.

By appending /_src to a Deployment URL or Custom Domain in your web browser, you will be redirected to the Deployment inspector and be able to browse the sources and build outputs.

By appending /_logs to a Deployment URL or Custom Domain in your web browser, you can see a real-time stream of logs

*[Content truncated - see full docs]*

**Examples**:

```text
.hg
.git
.gitmodules
.svn
.cache
.next
.now
.vercel
.npmignore
.dockerignore
.gitignore
.*.swp
.DS_Store
.wafpicke-*
.lock-wscript
.env.local
.env.*.local
.venv
.yarn/cache
npm-debug.log
config.gypi
node_modules
__pycache__
venv
CVS
```

---

## Methods to Protect Deployments

**URL**: https://vercel.com/docs/deployment-protection/methods-to-protect-deployments

**Contents**:
- Methods to Protect Deployments
  - Vercel Authentication
  - Password Protection
  - Trusted IPs
- More resources

Vercel offers three methods for protecting your deployments. Depending on your use case, you can choose to protect a single environment, or multiple environments. See Understanding Deployment Protection by environment for more information.

You can see an overview of your projects' protections in the following way

Vercel Authentication is available on all plans

With Vercel Authentication you can restrict access to all deployments (including non-public deployments), meaning only those with a Vercel account on your team, or those you share a Sharable Link with, can access non-public urls, such as my-project-1234-your-name.vercel.app.

When a Vercel user visits your protected deployment, but they do not have permission to access it, they have the option to request access for their Vercel account. This request triggers an email and Vercel notification to the branch authors.

Learn more about Vercel Authentication and how to enable it.

Password Protection is available on Enterprise plans or with the Advanced Deployment Protection add-on for Pro plans

Password Protection on Vercel lets you restrict access to both non-public, and public deployments depending on the type of environment protection you choose.

Learn more about Password Protection and how to enable it.

Trusted IPs are available on Enterprise plans

Trusted IPs restrict deployment access to specified IPv4 addresses and CIDR ranges, returning a 404 for unauthorized IPs. This protection feature is suitable for limiting access through specific paths like VPNs or external proxies.

Learn more about Trusted IPs and how to enable it.

---

## Password Protection

**URL**: https://vercel.com/docs/deployment-protection/methods-to-protect-deployments/password-protection

**Contents**:
- Password Protection
- Password Protection security considerations
- Managing Password Protection
  - Go to Project Deployment Protection Settings
  - Manage Password Protection
  - Manage using the API
  - Manage using Terraform

Password Protection is available on Enterprise plans or with the Advanced Deployment Protection add-on for Pro plans

Those with the owner, member and admin roles can manage Password Protection

With Password Protection enabled, visitors to your deployment must enter the pre-defined password to gain access. You can set the desired password from your project settings when enabling the feature, and update it any time

The table below outlines key considerations and security implications when using Password Protection for your deployments on Vercel.

You can manage Password Protection through the dashboard, API, or Terraform:

From your Vercel dashboard:

From the Password Protection section:

All your existing and future deployments will be protected with a password for the project. Next time when you access a deployment, you will be asked to log in by entering the password, which takes you to the deployment. A cookie will then be set in your browser for the deployment URL so you don't need to enter the password every time.

You can manage Password Protection using the Vercel API endpoint to update an existing project with the following body

You can configure Password Protection using password_protection in the vercel_project data source in the Vercel Terraform Provider.

**Examples**:

```text
// enable / update password protection
{
  "passwordProtection": {
    "deploymentType": "prod_deployment_urls_and_all_previews" | "all" | "preview",
    "password": "<password>"
  },
}
 
// disable password protection
{
  "passwordProtection": null
}
```

---

## Trusted IPs

**URL**: https://vercel.com/docs/deployment-protection/methods-to-protect-deployments/trusted-ips

**Contents**:
- Trusted IPs
- Trusted IPs security considerations
- Managing Trusted IPs
  - Manage using the dashboard
  - Go to Project Deployment Protection Settings
  - Manage Vercel Authentication
  - Manage Trusted IPs
  - Manage using the API

Trusted IPs are available on Enterprise plans

Those with the owner, member and admin roles can manage Trusted IPs

With Trusted IPs enabled at the level of your project, only visitors from an allowed IP address can access your deployment. The deployment URL will return 404 No Deployment Found for all other requests. Trusted IPs is configured by specifying a list of IPv4 addresses and IPv4 CIDR ranges.

Trusted IPs is suitable for customers who access Vercel deployments through a specific IP address. For example, limiting preview deployment access to your VPN. Trusted IPs can also be enabled in production, for example, to restrict incoming access to only requests through your external proxy.

The table below outlines key considerations and security implications when using Trusted IPs for your deployments on Vercel.

You can manage Trusted IPs through the dashboard, API, or Terraform:

From your Vercel dashboard:

Ensure Vercel Authentication is enabled. See Managing Vercel Authentication.

From the Trusted IPs section:

All your existing and future deployments will be protected with Trusted IPs for that project. Visitors to your project deployments from IP addresses not included in your list will see a No Deployment Found error page.

You can manage Trusted IPs using the Vercel API endpoint to update an existing project with the following body

You can configure Trusted IPs using trusted_ips in the vercel_project data source in the Vercel Terraform Provider.

**Examples**:

```text
// enable / update trusted ips
{
  "trustedIps": {
      "deploymentType": "all" | "preview" | "production" | "prod_deployment_urls_and_all_previews",
      "addresses": { "value": "<value>"; "note": "<note>" | undefined }[],
      "protectionMode": "additional"
  }
}
// disbale trusted ips
{
  "trustedIps": null
}
```

---

## Vercel Authentication

**URL**: https://vercel.com/docs/deployment-protection/methods-to-protect-deployments/vercel-authentication

**Contents**:
- Vercel Authentication
- Who can access protected deployments?
- Access requests
- Vercel Authentication security considerations
- Managing Vercel Authentication
  - Manage using the dashboard
  - Go to Project Deployment Protection Settings
  - Manage Vercel Authentication

Vercel Authentication is available on all plans

Those with the owner, member and admin roles can manage Vercel Authentication

Vercel Authentication lets you restrict access to your public and non-public deployments. It is the recommended approach to protecting your deployments, and available on all plans. When enabled, it allows only users with deployment access to view and comment on your site.

Users attempting to access the deployment will encounter a Vercel login redirect. If already logged into Vercel, Vercel will authenticate them automatically.

After login, users are redirected and a cookie is set in the browser if they have view access. If the user does not have access to view the deployment, they will be redirected to request access.

Access requests are available on all plans

Those with the owner, member, admin and developer roles can accept or reject access requests

When a Vercel user visits your protected deployment, but they do not have permission to access it, they have the option to request access for their Vercel account. This request triggers an email and Vercel notification to the branch authors.

The access request can be approved or declined. Additionally, granted access can be revoked for a user at any time.

Users granted access can view the latest deployment from a specific branch when logged in with their Vercel account. They can also leave preview Comments if these are enabled on your team.

Those on the Hobby plan can only have one external user per account. If you need more, you can upgrade to a Pro plan.

You can manage access requests in the following way

Access requests can also be managed using the share modal on the deployment page

You can configure Vercel Authentication for different environments, as outlined in Understanding Deployment Protection by environment. This feature works alongside other security measures like Password Protection and Trusted IPs. For specific use-cases, you can bypass Vercel Authentication with metho

*[Content truncated - see full docs]*

**Examples**:

```text
// enable / update Vercel Authentication
{
  "ssoProtection": {
    "deploymentType": "prod_deployment_urls_and_all_previews" | "all" | "preview"
  }
}
 
// disable Vercel Authentication
{
  "ssoProtection": null
}
```

---
