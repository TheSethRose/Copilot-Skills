# Vercel - Getting Started

**Pages**: 10

---

## Add a domain

**URL**: https://vercel.com/docs/getting-started-with-vercel/domains

**Contents**:
- Add a domain
  - Next steps

Assigning a custom domain to your project guarantees that visitors to your application will have a tailored experience that aligns with your brand.

On Vercel, this domain can have any format of your choosing:

If you already own a domain, you can point it to Vercel, or transfer it over. If you don't own one yet, you can purchase a new one. For this tutorial, feel free to use that one domain you bought 11 months ago and haven’t got around to using yet!

For more information on domains at Vercel, see Domains overview.

Now that your site is deployed, you can to personalize it by setting up a custom domain. With Vercel you can either buy a new domain or use an existing domain.

---

## Buy a domain

**URL**: https://vercel.com/docs/getting-started-with-vercel/buy-domain

**Contents**:
- Buy a domain
  - Using CLI?
  - Find a domain
  - Select your domain(s)
  - Purchase your domain(s)
  - Enter payment details and registrant information
  - Configure your domain
- Next steps

Use this snippet to purchase a new domain from Vercel:

Use Vercel to find and buy a domain that resonates with your brand, establishes credibility, and captures your visitors' attention.

All domains purchased on Vercel have WHOIS privacy enabled by default.

Go to https://vercel.com/domains and search for a domain that matches you or your brand. You could try "SuperDev"!

Depending on the TLD (top-level domain), you’ll see the purchase price. Domains with Premium badges are more expensive. You can sort the results by relevance (default), length, price, or alphabetical order.

For the ICANN registrant information:

If you enter the same email address you use for your Vercel user account (or an email your team Owner uses), the information will be confirmed automatically.

If you enter another email address, please follow the instructions you receive in an email to confirm your registrant information.

You can also configure your domain from the project's domains dashboard page by following the Add and configure domain instructions.

Next, learn how to take advantage of Vercel's collaboration features as part of your developer workflow:

Use Vercel in your developer workflow

**Examples**:

```text
vercel domains buy [domain]
```

---

## Collaborate on Vercel

**URL**: https://vercel.com/docs/getting-started-with-vercel/collaborate

**Contents**:
- Collaborate on Vercel
- Make Changes
- Create a preview deployment
  - Make your changes
  - Commit your changes
  - Inspect your deployment information
  - View your deployment URL
- Commenting on previews

Collaboration is key in successful development projects, and Vercel offers robust features to enhance collaboration among developers. From seamless code collaboration to real-time previews with Comments, Vercel empowers your team to work together effortlessly.

Now that your project is publicly available on your domain of choice, it’s time to begin making changes to it. With Vercel's automatic deployments, this won't require any extra effort. By default, when your Vercel project is connected to a Git repository, Vercel will deploy every commit that is pushed to the Git repository, regardless of which branch you're pushing it to.

A Production environment is one built from the main or development branch of your Git repository. A preview environment is created when you deploy from any other branch.

Vercel provides a URL that reflects the latest pushes to that branch. You can find this either on your dashboard, or in a pull request, which you'll see in the next step

This connection was established for you automatically, so all you have to do is push commits, and you will start receiving links to deployments right on your Git provider.

Create a new branch in your project and make some changes

Commit those changes and create a pull request. After a few seconds, Vercel picks up the changes and starts to build and deploy your project. You can see the status of the build through the bot comment made on your PR:

Select Inspect to explore the build within your dashboard. You can see the build is within the preview environment and additional information about the deployment including: build information, a deployment summary, checks, and domain assignment. These happen for every deployment

Return to your pull request. At this point your build should be deployed and you can select Visit Preview. You can now see your changes and share this preview URL with others.

Comments provide a way for your team or friends to give direct feedback on preview deployments. Share with oth

*[Content truncated - see full docs]*

---

## Getting Started

**URL**: https://vercel.com/docs/ai-gateway/getting-started

**Contents**:
- Getting Started
  - Set up your application
  - Install dependencies
  - Set up your API key
  - Create and run your script
  - Next steps
- Using OpenAI SDK
- Using other community frameworks

This quickstart will walk you through making an AI model request with Vercel's AI Gateway. While this guide uses the AI SDK, you can also integrate with the OpenAI SDK or other community frameworks.

Start by creating a new directory using the mkdir command. Change into your new directory and then run the pnpm init command, which will create a package.json.

Install the AI SDK package, ai, along with other necessary dependencies.

dotenv is used to access environment variables (your AI Gateway API key) within your application. The tsx package is a TypeScript runner that allows you to run your TypeScript code. The typescript package is the TypeScript compiler. The @types/node package is the TypeScript definitions for the Node.js API.

To create an API key, go to the AI Gateway tab of the dashboard:

Once you have the API key, create a .env.local file and save your API key:

Instead of using an API key, you can use OIDC tokens to authenticate your requests.

The AI Gateway provider will default to using the AI_GATEWAY_API_KEY environment variable.

Create an index.ts file in the root of your project and add the following code:

Now, run your script:

You should see the AI model's response to your prompt.

Continue with the AI SDK documentation to learn advanced configuration, set up provider routing and fallbacks, and explore more integration examples.

The AI Gateway provides OpenAI-compatible API endpoints that allow you to use existing OpenAI client libraries and tools with the AI Gateway.

The OpenAI-compatible API includes:

Learn more about using the OpenAI SDK with the AI Gateway in the OpenAI-Compatible API page.

The AI Gateway is designed to work with any framework that supports the OpenAI API or AI SDK 5.

Read more about using the AI Gateway with other community frameworks in the framework integrations section.

**Examples**:

```text
mkdir demo
cd demo
pnpm init
```

```typescript
pnpm i ai dotenv @types/node tsx typescript
```

```text
AI_GATEWAY_API_KEY=your_ai_gateway_api_key
```

---

## Getting started with Vercel

**URL**: https://vercel.com/docs/getting-started-with-vercel

**Contents**:
- Getting started with Vercel
- Before you begin
- Customizing your journey

Vercel is a platform for developers that provides the tools, workflows, and infrastructure you need to build and deploy your web apps faster, without the need for additional configuration.

Vercel supports popular frontend frameworks out-of-the-box, and its scalable, secure infrastructure is globally distributed to serve content from data centers near your users for optimal speeds.

During development, Vercel provides tools for real-time collaboration on your projects such as automatic preview and production environments, and comments on preview deployments.

To get started, create an account with Vercel. You can select the plan that's right for you.

Once you create an account, you can choose to authenticate either with a Git provider or by using an email. When using email authentication, you may need to confirm both your email address and a phone number.

This tutorial is framework agnostic but Vercel supports many frontend frameworks. As you go through the docs, the quickstarts will provide specific instructions for your framework. If you don't find what you need, give us feedback and we'll update them!

While many of our instructions use the dashboard, you can also use Vercel CLI to carry out most tasks on Vercel. In this tutorial, look for the "Using CLI?" section for the CLI steps. To use the CLI, you'll need to install it:

**Examples**:

```text
pnpm i -g vercel
```

---

## Import an existing project

**URL**: https://vercel.com/docs/getting-started-with-vercel/import

**Contents**:
- Import an existing project
  - Using CLI?
  - Connect to your Git provider
  - Import your repository
  - Optionally, configure any settings
  - Deploy your project
  - Enjoy the confetti!
- Next Steps

Use the following snippet to deploy your existing project with Vercel CLI:

Use the following snippet to deploy your existing project with Vercel CLI:

Your existing project can be any web project that outputs static HTML content (such as a website that contains HTML, CSS, and JavaScript). When you use any of Vercel's supported frameworks, we'll automatically detect and set the optimal build and deployment configurations for your framework.

On the New Project page, under the Import Git Repository section, select the Git provider that you would like to import your project from.

Follow the prompts to sign in to either your GitHub, GitLab, or BitBucket account.

Find the repository in the list that you would like to import and select Import.

Vercel will automatically detect the framework and any necessary build settings. However, you can also configure the Project settings at this point including the build and output settings and Environment Variables. These can also be set later.

Press the Deploy button. Vercel will create the Project and deploy it based on the chosen configurations.

To view your deployment, select the Project in the dashboard and then select the Domain. This page is now visible to anyone who has the URL.

Next, learn how to assign a domain to your new deployment.

**Examples**:

```text
vercel --cwd [path-to-project]
```

---

## Next Steps

**URL**: https://vercel.com/docs/getting-started-with-vercel/next-steps

**Contents**:
- Next Steps
- Infrastructure
- Storage
- Observability
- Security

Congratulations on getting started with Vercel!

Now, let's explore what's next on your journey. At this point, you can either continue learning more about Vercel's many features, or you can dive straight in and get to work. The choice is yours!

Dive into my dashboard

Manage your projects, domains, and more.

Alternatively, you can start learning about many of the products and features that Vercel provides:

Learn about Vercel's CDN and implement scalable infrastructure in your app using Functions. Get started today by implementing a Vercel Function in your app:

Vercel offers a suite of managed, serverless storage products that integrate with your frontend framework.

Learn more about which storage option is right for you and get started with implementing them:

Vercel provides a suite of observability tools to allow you to monitor, analyze, and manage your site.

Vercel takes security seriously. It uses HTTPS by default for secure data transmission, regularly updates its platform to mitigate potential vulnerabilities, limits system access for increased safety, and offers built-in DDoS mitigation. This layered approach ensures robust protection for your sites and applications.

---

## Projects and deployments

**URL**: https://vercel.com/docs/getting-started-with-vercel/projects-deployments

**Contents**:
- Projects and deployments
  - More resources

To get started with Vercel, it's helpful to understand projects and deployments:

To get started you'll create a new project by either deploying a template or importing and deploying an existing project:

---

## Use a template

**URL**: https://vercel.com/docs/getting-started-with-vercel/template

**Contents**:
- Use a template
  - Using CLI?
  - Find a template
  - Deploy the template to Vercel
  - Connect your Git provider
  - Project deployment
  - View your dashboard
  - Clone the project to your machine

Clone the template to your local machine and use the following snippet to deploy the template with Vercel CLI:

Clone the template to your local machine and use the following snippet to deploy the template with Vercel CLI:

Accelerate your development on Vercel with Templates. This guide will show you how to use templates to fast-track project setup, leverage popular frontend frameworks, and maximize Vercel's features.

From https://vercel.com/templates, select the template you’d like to deploy. You can use the filters to select a template based on use case, framework, and other requirements.

Not sure which one to use? How about exploring Next.js.

Once you've selected a template, Click Deploy on the template page to start the process.

To ensure you can easily update your project after deploying it, Vercel will create a new repository with your chosen Git provider. Every push to that Git repository will be deployed automatically.

First, select the Git provider that you'd like to connect to. Once you’ve signed in, you’ll need to set the scope and repository name. At this point, Vercel will clone a copy of the source code into your Git account.

Once the project has been cloned to your git provider, Vercel will automatically start deploying the project. This starts with building your project, then assigning the domain, and finally celebrating your deployed project with confetti.

At this point, you’ve created a production deployment, with its very own domain assigned. If you continue to your dashboard, you can click on the domain to preview a live, accessible URL that is instantly available on the internet.

Finally, you'll want to clone the source files to your local machine so that you can make some changes later. To do this from your dashboard, select the Git repository button and clone the repository.

Because you used a template, we’ve automatically included any additional environment set up as part of the template. You can customize your project by configurin

*[Content truncated - see full docs]*

**Examples**:

```text
vercel --cwd [path-to-project]
```

---

## Use an existing domain

**URL**: https://vercel.com/docs/getting-started-with-vercel/use-existing

**Contents**:
- Use an existing domain
  - Using CLI?
  - Go to your project's domains settings
  - Add your existing domain to your project
  - Configure your DNS records
- Next steps

Use this snippet to add a domain that you own to a Vercel project:

Use this snippet to add a domain that you own to a Vercel project:

Already have a domain you love? Seamlessly integrate it with Vercel to leverage the platform's powerful features and infrastructure. Whether you're migrating an existing project or want to maintain your established online presence, you can use the steps below to add your custom domain.

Select your project and select the Settings tab. Then, select the Domains menu item or click on this link and select your project

From the Domains page, enter the domain you wish to add to the project.

If you add an apex domain (e.g. example.com) to the project, Vercel will prompt you to add the wwwsubdomain prefix, the apex domain, and some basic redirection options.

For more information on which redirect option to choose, see Redirecting www domains.

Configure the DNS records of your domain with your registrar so it can be used with your Project. The dashboard will automatically display different methods for configuring it:

Both apex domains and subdomains can also be configured using the Nameservers method. Wildcard domains must use the nameservers method for verification. For more information see Add a custom domain.

Next, learn how to take advantage of Vercel's collaboration features as part of your developer workflow:

Use Vercel in your developer workflow

**Examples**:

```text
vercel domains add [domain] [project]
```

---
