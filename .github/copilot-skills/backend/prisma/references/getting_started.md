# Prisma - Getting Started

**Pages**: 38

---

## Add Prisma ORM to an existing MongoDB project using TypeScript (15 min) | Prisma Documentation

**URL**: https://www.prisma.io/docs/getting-started/setup-prisma/add-to-existing-project/mongodb-typescript-mongodb

**Contents**:
- Add Prisma ORM to an existing MongoDB project using TypeScript
- Prerequisites​
- Set up Prisma ORM​

Learn how to add Prisma ORM to an existing Node.js or TypeScript project by connecting it to your database and generating a Prisma Client for database access. The following tutorial introduces you to Prisma CLI, Prisma Client, and Prisma Introspection.

If you're migrating to Prisma ORM from Mongoose, see our Migrate from Mongoose guide.

In order to successfully complete this guide, you need:

Node.js installed on your machine (see system requirements for officially supported versions)

Access to a MongoDB 4.2+ server with a replica set deployment. We recommend using MongoDB Atlas.

The MongoDB database connector uses transactions to support nested writes. Transactions requires a replica set deployment. The easiest way to deploy a replica set is with Atlas. It's free to get started.

Make sure you have your database connection URL (that includes your authentication credentials) at hand! If you don't have a database server running and just want to explore Prisma ORM, check out the Quickstart.

See System requirements for exact version requirements.

As a first step, navigate into it your project directory that contains the package.json file.

Next, add the Prisma CLI as a development dependency to your project:

If your project contains multiple directories with package.json files (e.g., frontend, backend, etc.), note that Prisma ORM is specifically designed for use in the API/backend layer. To set up Prisma, navigate to the appropriate backend directory containing the relevant package.json file and configure Prisma there.

You can now invoke the Prisma CLI by prefixing it with npx:

See installation instructions to learn how to install Prisma ORM using a different package manager.

Next, set up your Prisma ORM project by creating your Prisma Schema file with the following command:

This command does a few things:

Note that the default schema created by prisma init uses PostgreSQL as the provider. If you didn't specify a provider with the datasource-provider option

*[Content truncated - see full docs]*

**Examples**:

```terminal
npm install prisma --save-dev
```

```terminal
npx prisma init --datasource-provider mongodb --output ../generated/prisma
```

```prisma
datasource db {  provider = "mongodb"  url      = env("DATABASE_URL")}
```

---

## Add Prisma ORM to an existing project | Prisma Documentation

**URL**: https://www.prisma.io/docs/getting-started/setup-prisma/add-to-existing-project

**Contents**:
- Add to existing project
- In this section​
- Relational databases
- MongoDB

Include Prisma ORM in an existing project with the following documentation, which explains some core concepts as it guides you through integrating Prisma ORM into your workflow.

---

## Add Prisma ORM to an existing project using TypeScript and PostgreSQL (15 min) | Prisma Documentation

**URL**: https://www.prisma.io/docs/getting-started/setup-prisma/add-to-existing-project/relational-databases-typescript-postgresql

**Contents**:
- Add Prisma ORM to an existing project (TypeScript and PostgreSQL)
- Prerequisites​
- Set up Prisma ORM​

Learn how to add Prisma ORM to an existing Node.js or TypeScript project by connecting it to your database and generating a Prisma Client for database access. The following tutorial introduces you to the Prisma CLI, Prisma Client, and Prisma Introspection.

If you're migrating to Prisma ORM from another ORM, see our Migrate from TypeORM or Migrate from Sequelize migration guides.

In order to successfully complete this guide, you need:

See System requirements for exact version requirements.

Make sure you have your database connection URL (that includes your authentication credentials) at hand! If you don't have a database server running and just want to explore Prisma ORM, check out the Quickstart.

As a first step, navigate into your project directory that contains the package.json file.

Next, add the Prisma CLI as a development dependency to your project:

If your project contains multiple directories with package.json files (e.g., frontend, backend, etc.), note that Prisma ORM is specifically designed for use in the API/backend layer. To set up Prisma, navigate to the appropriate backend directory containing the relevant package.json file and configure Prisma there.

You can now invoke the Prisma CLI by prefixing it with npx:

See installation instructions to learn how to install Prisma ORM using a different package manager.

Next, set up your Prisma ORM project by creating your Prisma Schema file with the following command:

This command does a few things:

Note that the default schema created by prisma init uses PostgreSQL as the provider. If you didn't specify a provider with the datasource-provider option, you need to edit the datasource block to use the postgresql provider instead:

**Examples**:

```terminal
npm install prisma --save-dev
```

```terminal
npx prisma init --datasource-provider postgresql --output ../generated/prisma
```

```prisma
datasource db {  provider = "postgresql"  url      = env("DATABASE_URL")}
```

---

## Add Prisma ORM to an existing project using TypeScript and PlanetScale (15 min) | Prisma Documentation

**URL**: https://www.prisma.io/docs/getting-started/setup-prisma/add-to-existing-project/relational-databases-typescript-planetscale

**Contents**:
- Add Prisma ORM to an existing project (TypeScript and PlanetScale)
- Prerequisites​
- Set up Prisma ORM​

Learn how to add Prisma ORM to an existing Node.js or TypeScript project by connecting it to your database and generating a Prisma Client for database access. The following tutorial introduces you to the Prisma CLI, Prisma Client, and Prisma Introspection.

If you're migrating to Prisma ORM from another ORM, see our Migrate from TypeORM or Migrate from Sequelize migration guides.

In order to successfully complete this guide, you need:

See System requirements for exact version requirements.

Make sure you have your database connection URL (that includes your authentication credentials) at hand! If you don't have a database server running and just want to explore Prisma ORM, check out the Quickstart.

As a first step, navigate into your project directory that contains the package.json file.

Next, add the Prisma CLI as a development dependency to your project:

If your project contains multiple directories with package.json files (e.g., frontend, backend, etc.), note that Prisma ORM is specifically designed for use in the API/backend layer. To set up Prisma, navigate to the appropriate backend directory containing the relevant package.json file and configure Prisma there.

You can now invoke the Prisma CLI by prefixing it with npx:

See installation instructions to learn how to install Prisma ORM using a different package manager.

Next, set up your Prisma ORM project by creating your Prisma Schema file with the following command:

This command does a few things:

Note that the default schema created by prisma init uses PostgreSQL as the provider. If you didn't specify a provider with the datasource-provider option, you need to edit the datasource block to use the mysql provider instead:

**Examples**:

```terminal
npm install prisma --save-dev
```

```terminal
npx prisma init --datasource-provider mysql --output ../generated/prisma
```

```prisma
datasource db {  provider = "mysql"  url      = env("DATABASE_URL")}
```

---

## Add Prisma ORM to an existing project using TypeScript and SQL Server (15 min) | Prisma Documentation

**URL**: https://www.prisma.io/docs/getting-started/setup-prisma/add-to-existing-project/relational-databases-typescript-sqlserver

**Contents**:
- Add Prisma ORM to an existing project (TypeScript and SQL Server)
- Prerequisites​
- Set up Prisma ORM​

Learn how to add Prisma ORM to an existing Node.js or TypeScript project by connecting it to your database and generating a Prisma Client for database access. The following tutorial introduces you to the Prisma CLI, Prisma Client, and Prisma Introspection.

If you're migrating to Prisma ORM from another ORM, see our Migrate from TypeORM or Migrate from Sequelize migration guides.

In order to successfully complete this guide, you need:

See System requirements for exact version requirements.

Make sure you have your database connection URL (that includes your authentication credentials) at hand! If you don't have a database server running and just want to explore Prisma ORM, check out the Quickstart.

As a first step, navigate into your project directory that contains the package.json file.

Next, add the Prisma CLI as a development dependency to your project:

If your project contains multiple directories with package.json files (e.g., frontend, backend, etc.), note that Prisma ORM is specifically designed for use in the API/backend layer. To set up Prisma, navigate to the appropriate backend directory containing the relevant package.json file and configure Prisma there.

You can now invoke the Prisma CLI by prefixing it with npx:

See installation instructions to learn how to install Prisma ORM using a different package manager.

Next, set up your Prisma ORM project by creating your Prisma Schema file with the following command:

This command does a few things:

Note that the default schema created by prisma init uses PostgreSQL as the provider. If you didn't specify a provider with the datasource-provider option, you need to edit the datasource block to use the sqlserver provider instead:

**Examples**:

```terminal
npm install prisma --save-dev
```

```terminal
npx prisma init --datasource-provider sqlserver --output ../generated/prisma
```

```prisma
datasource db {  provider = "sqlserver"  url      = env("DATABASE_URL")}
```

---

## Add Prisma ORM to an existing project using TypeScript and CockroachDB (15 min) | Prisma Documentation

**URL**: https://www.prisma.io/docs/getting-started/setup-prisma/add-to-existing-project/relational-databases-typescript-cockroachdb

**Contents**:
- Add Prisma ORM to an existing project (TypeScript and CockroachDB)
- Prerequisites​
- Set up Prisma ORM​

Learn how to add Prisma ORM to an existing Node.js or TypeScript project by connecting it to your database and generating a Prisma Client for database access. The following tutorial introduces you to the Prisma CLI, Prisma Client, and Prisma Introspection.

If you're migrating to Prisma ORM from another ORM, see our Migrate from TypeORM or Migrate from Sequelize migration guides.

In order to successfully complete this guide, you need:

See System requirements for exact version requirements.

Make sure you have your database connection URL (that includes your authentication credentials) at hand! If you don't have a database server running and just want to explore Prisma ORM, check out the Quickstart.

As a first step, navigate into your project directory that contains the package.json file.

Next, add the Prisma CLI as a development dependency to your project:

If your project contains multiple directories with package.json files (e.g., frontend, backend, etc.), note that Prisma ORM is specifically designed for use in the API/backend layer. To set up Prisma, navigate to the appropriate backend directory containing the relevant package.json file and configure Prisma there.

You can now invoke the Prisma CLI by prefixing it with npx:

See installation instructions to learn how to install Prisma ORM using a different package manager.

Next, set up your Prisma ORM project by creating your Prisma Schema file with the following command:

This command does a few things:

Note that the default schema created by prisma init uses PostgreSQL as the provider. If you didn't specify a provider with the datasource-provider option, you need to edit the datasource block to use the cockroachdb provider instead:

**Examples**:

```terminal
npm install prisma --save-dev
```

```terminal
npx prisma init --datasource-provider cockroachdb --output ../generated/prisma
```

```prisma
datasource db {  provider = "cockroachdb"  url      = env("DATABASE_URL")}
```

---

## Configure Prisma Client with PgBouncer | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/pgbouncer

**Contents**:
- Configure Prisma Client with PgBouncer
- PgBouncer​
  - Set PgBouncer to transaction mode​
  - Add pgbouncer=true for PgBouncer versions below 1.21.0​
  - Configure max_prepared_statements in PgBouncer to be greater than zero​
  - Prisma Migrate and PgBouncer workaround​
  - PgBouncer with different database providers​
- Supabase Supavisor​

An external connection pooler like PgBouncer holds a connection pool to the database, and proxies incoming client connections by sitting between Prisma Client and the database. This reduces the number of processes a database has to handle at any given time.

Usually, this works transparently, but some connection poolers only support a limited set of functionality. One common feature that external connection poolers do not support are named prepared statements, which Prisma ORM uses. For these cases, Prisma ORM can be configured to behave differently.

Looking for an easy, infrastructure-free solution? Try Prisma Accelerate! It requires little to no setup and works seamlessly with all databases supported by Prisma ORM.

Ready to begin? Get started with Prisma Accelerate by clicking .

For Prisma Client to work reliably, PgBouncer must run in Transaction mode.

Transaction mode offers a connection for every transaction – a requirement for the Prisma Client to work with PgBouncer.

We recommend not setting pgbouncer=true in the database connection string if you're using PgBouncer 1.21.0 or later.

To use Prisma Client with PgBouncer, add the ?pgbouncer=true flag to the PostgreSQL connection URL:

PORT specified for PgBouncer pooling is sometimes different from the default 5432 port. Check your database provider docs for the correct port number.

Prisma uses prepared statements, and setting max_prepared_statements to a value greater than 0 enables PgBouncer to use those prepared statements.

PORT specified for PgBouncer pooling is sometimes different from the default 5432 port. Check your database provider docs for the correct port number.

Prisma Migrate uses database transactions to check out the current state of the database and the migrations table. However, the Schema Engine is designed to use a single connection to the database, and does not support connection pooling with PgBouncer. If you attempt to run Prisma Migrate commands in any environment that uses PgBoun

*[Content truncated - see full docs]*

**Examples**:

```shell
postgresql://USER:PASSWORD@HOST:PORT/DATABASE?pgbouncer=true
```

```bash
Error: undefined: Database errorError querying the database: db error: ERROR: prepared statement "s0" already exists
```

```prisma
datasource db {  provider  = "postgresql"  url       = "postgres://USER:PASSWORD@HOST:PORT/DATABASE?pgbouncer=true"  directUrl = "postgres://USER:PASSWORD@HOST:PORT/DATABASE"}
```

---

## Connect your MongoDB database using TypeScript | Prisma Documentation

**URL**: https://www.prisma.io/docs/getting-started/setup-prisma/add-to-existing-project/mongodb/connect-your-database-typescript-mongodb

**Contents**:
- Connect your MongoDB database to your existing TypeScript project
- Connecting your database​
- Troubleshooting​
  - Error in connector: SCRAM failure: Authentication failed.​
  - Raw query failed. Error code 8000 (AtlasError): empty database name not allowed.​

To connect your database, you need to set the url field of the datasource block in your Prisma schema to your database connection URL:

In this case, the url is set via an environment variable which is defined in .env:

You now need to adjust the connection URL to point to your own database.

The format of the connection URL for your database depends on the database you use. For MongoDB, it looks as follows (the parts spelled all-uppercased are placeholders for your specific connection details):

Here's a short explanation of each component:

If you see the Error in connector: SCRAM failure: Authentication failed. error message, you can specify the source database for the authentication by adding ?authSource=admin to the end of the connection string.

If you see the Raw query failed. Code: unknown. Message: Kind: Command failed: Error code 8000 (AtlasError): empty database name not allowed. error message, be sure to append the database name to the database URL. You can find more info in this GitHub issue.

**Examples**:

```prisma
datasource db {  provider = "mongodb"  url      = env("DATABASE_URL")}
```

```bash
DATABASE_URL="mongodb+srv://test:test@cluster0.ns1yp.mongodb.net/myFirstDatabase"
```

```no-lines
mongodb://USERNAME:PASSWORD@HOST:PORT/DATABASE
```

---

## Connect your existing database using TypeScript and MySQL | Prisma Documentation

**URL**: https://www.prisma.io/docs/getting-started/setup-prisma/add-to-existing-project/relational-databases/connect-your-database-typescript-mysql

**Contents**:
- Connect your existing database using TypeScript and MySQL
- Connecting your database​
  - Connection URL

To connect your database, you need to set the url field of the datasource block in your Prisma schema to your database connection URL:

In this case, the url is set via an environment variable which is defined in .env:

You now need to adjust the connection URL to point to your own database.

The format of the connection URL for your database typically depends on the database you use. For MySQL, it looks as follows (the parts spelled all-uppercased are placeholders for your specific connection details):

Here's a short explanation of each component:

As an example, for a MySQL database hosted on AWS RDS, the connection URL might look similar to this:

When running MySQL locally, your connection URL typically looks similar to this:

**Examples**:

```prisma
datasource db {  provider = "mysql"  url      = env("DATABASE_URL")}
```

```bash
DATABASE_URL="mysql://johndoe:randompassword@localhost:3306/mydb"
```

```no-lines
mysql://USER:PASSWORD@HOST:PORT/DATABASE
```

---

## Connect your existing database using TypeScript and SQL Server | Prisma Documentation

**URL**: https://www.prisma.io/docs/getting-started/setup-prisma/add-to-existing-project/relational-databases/connect-your-database-typescript-sqlserver

**Contents**:
- Connect your existing database using TypeScript and SQL Server
- Connecting your database​

To connect your database, you need to set the url field of the datasource block in your Prisma schema to your database connection URL:

The url is set via an environment variable, the following example connection URL uses SQL authentication, but there are other ways to format your connection URL

Adjust the connection URL to match your setup - see Microsoft SQL Server connection URL for more information.

Make sure TCP/IP connections are enabled via SQL Server Configuration Manager to avoid No connection could be made because the target machine actively refused it. (os error 10061)

**Examples**:

```prisma
datasource db {  provider = "sqlserver"  url      = env("DATABASE_URL")}
```

```bash
DATABASE_URL="sqlserver://localhost:1433;database=mydb;user=sa;password=r@ndomP@$$w0rd;trustServerCertificate=true"
```

---

## Connect your existing database using TypeScript and PlanetScale | Prisma Documentation

**URL**: https://www.prisma.io/docs/getting-started/setup-prisma/add-to-existing-project/relational-databases/connect-your-database-typescript-planetscale

**Contents**:
- Connect your existing database using TypeScript and PlanetScale
- Connecting your database​
  - Connection URL

To connect your database, you need to set the url field of the datasource block in your Prisma schema to your database connection URL:

You will also need to set the relation mode type to prisma in the datasource block:

The url is set via an environment variable which is defined in .env:

You now need to adjust the connection URL to point to your own database.

The format of the connection URL for your database typically depends on the database you use. PlanetScale uses the MySQL connection URL format, which has the following structure (the parts spelled all-uppercased are placeholders for your specific connection details):

Here's a short explanation of each component:

For a database hosted with PlanetScale, the connection URL looks similar to this:

The connection URL for a given database branch can be found from your PlanetScale account by going to the overview page for the branch and selecting the 'Connect' dropdown. In the 'Passwords' section, generate a new password and select 'Prisma' to get the Prisma format for the connection URL.

Alternatively, you can connect to your PlanetScale database server using the PlanetScale CLI, and use a local connection URL. In this case the connection URL will look like this:

To connect to your branch, use the following command:

The --port flag can be omitted if you are using the default port 3306.

**Examples**:

```prisma
datasource db {  provider = "postgresql"  url      = env("DATABASE_URL")}
```

```prisma
datasource db {  provider     = "mysql"  url          = env("DATABASE_URL")  relationMode = "prisma"}
```

```bash
DATABASE_URL="mysql://janedoe:mypassword@server.us-east-2.psdb.cloud/mydb?sslaccept=strict"
```

---

## Connect your existing database using TypeScript and PostgresSQL | Prisma Documentation

**URL**: https://www.prisma.io/docs/getting-started/setup-prisma/add-to-existing-project/relational-databases/connect-your-database-typescript-postgresql

**Contents**:
- Connect your existing database using TypeScript and PostgresSQL
- Connecting your database​
  - Connection URL

To connect your database, you need to set the url field of the datasource block in your Prisma schema to your database connection URL:

In this case, the url is set via an environment variable which is defined in .env:

You now need to adjust the connection URL to point to your own database.

The format of the connection URL for your database depends on the database you use. For PostgreSQL, it looks as follows (the parts spelled all-uppercased are placeholders for your specific connection details):

Note: In most cases, you can use the postgres:// and postgresql:// URI scheme designators interchangeably - however, depending on how your database is hosted, you might need to be specific.

If you're unsure what to provide for the schema parameter for a PostgreSQL connection URL, you can probably omit it. In that case, the default schema name public will be used.

As an example, for a PostgreSQL database hosted on Heroku, the connection URL might look similar to this:

When running PostgreSQL locally on macOS, your user and password as well as the database name typically correspond to the current user of your OS, e.g. assuming the user is called janedoe:

**Examples**:

```prisma
datasource db {  provider = "postgresql"  url      = env("DATABASE_URL")}
```

```bash
DATABASE_URL="postgresql://johndoe:randompassword@localhost:5432/mydb?schema=public"
```

```no-lines
postgresql://USER:PASSWORD@HOST:PORT/DATABASE?schema=SCHEMA
```

---

## Custom model and field names | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-client/setup-and-configuration/custom-model-and-field-names

**Contents**:
- Custom model and field names
- Example: Relational database​
- Using @map and @@map to rename fields and models in the Prisma Client API​
- Renaming relation fields​

The Prisma Client API is generated based on the models in your Prisma schema. Models are typically 1:1 mappings of your database tables.

In some cases, especially when using introspection, it might be useful to decouple the naming of database tables and columns from the names that are used in your Prisma Client API. This can be done via the @map and @@map attributes in your Prisma schema.

You can use @map and @@map to rename MongoDB fields and collections respectively. This page uses a relational database example.

Assume you have a PostgreSQL relational database schema looking similar to this:

When introspecting a database with that schema, you'll get a Prisma schema looking similar to this:

There are a few "issues" with this Prisma schema when the Prisma Client API is generated:

Adhering to Prisma ORM's naming conventions

Prisma ORM has a naming convention of camelCasing and using the singular form for Prisma models. If these naming conventions are not met, the Prisma schema can become harder to interpret and the generated Prisma Client API will feel less natural. Consider the following, generated model:

Although profiles refers to a 1:1 relation, its type is currently called profiles in plural, suggesting that there might be many profiles in this relation. With Prisma ORM conventions, the models and fields were ideally named as follows:

Because these fields are "Prisma ORM-level" relation fields that do not manifest you can manually rename them in your Prisma schema.

Naming of annotated relation fields

Foreign keys are represented as a combination of a annotated relation fields and its corresponding relation scalar field in the Prisma schema. Here's how all the relations from the SQL schema are currently represented:

You can "rename" fields and models that are used in Prisma Client by mapping them to the "original" names in the database using the @map and @@map attributes. For the example above, you could e.g. annotate your models as follows.

After yo

*[Content truncated - see full docs]*

**Examples**:

```sql
CREATE TABLE users (	user_id SERIAL PRIMARY KEY NOT NULL,	name VARCHAR(256),	email VARCHAR(256) UNIQUE NOT NULL);CREATE TABLE posts (	post_id SERIAL PRIMARY KEY NOT NULL,	created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,	title VARCHAR(256) NOT NULL,	content TEXT,	author_id INTEGER REFERENCES users(user_id));CREATE TABLE profiles (	profile_id SERIAL PRIMARY KEY NOT NULL,	bio TEXT,	user_id INTEGER NOT NULL UNIQUE REFERENCES users(user_id));CREATE TABLE categories (	category_id SERIAL 
...
```

```prisma
model categories {  category_id        Int                  @id @default(autoincrement())  name               String?              @db.VarChar(256)  post_in_categories post_in_categories[]}model post_in_categories {  post_id     Int  category_id Int  categories  categories @relation(fields: [category_id], references: [category_id], onDelete: NoAction, onUpdate: NoAction)  posts       posts      @relation(fields: [post_id], references: [post_id], onDelete: NoAction, onUpdate: NoAction)  @@unique(
...
```

```prisma
model users {  user_id  Int       @id @default(autoincrement())  name     String?   @db.VarChar(256)  email    String    @unique @db.VarChar(256)  posts    posts[]  profiles profiles?}
```

---

## Editor and IDE setup | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/more/development-environment/editor-setup

**Contents**:
- Editor setup
- VS Code extension​
- Community projects​
  - Emacs​
  - Vim​
  - neovim​
  - JetBrains IDE​
  - Sublime Text​

This page describes how you can configure your editor for an optimal developer experience when using Prisma ORM.

If you don't see your editor here, please open a feature request and ask for dedicated support for your editor (e.g. for syntax highlighting and auto-formatting).

You can install the official Prisma VS Code extension. It adds extra capabilities to VS Code when developing applications with Prisma ORM:

If you're using VS Code, you can use VS Code agent mode to enter prompts such as “create Postgres database” or “apply schema migration” directly in the chat. The VS code agent handles all underlying Prisma CLI invocations and API calls automatically. See our VS Code Agent documentation for more details.

Note: Community projects are not maintained or officially supported by Prisma and some features may by out of sync. Use at your own discretion.

You can get IDE-style autocompletion for Prisma CLI using inshellisense. It supports: bash, zsh, fish, pwsh, powershell (Windows Powershell).

inshellisense is built on top of Fig which you can also use directly. It works in bash, zsh, and fish.

**Examples**:

```json
"editor.formatOnSave": true
```

```json
"[prisma]": {  "editor.defaultFormatter": "Prisma.prisma"},
```

```bash
npm install -g @microsoft/inshellisense
```

---

## From the CLI | Prisma Documentation

**URL**: https://www.prisma.io/docs/getting-started/prisma-postgres/from-the-cli

**Contents**:
- From the CLI
- Prerequisites​
- 1. Organize your project directory​
- 2. Set up your project​
  - 2.1. Set up TypeScript​
  - 2.2. Set up Prisma ORM​
  - 2.3. Create a TypeScript script​
- 3. Migrate the database schema​

This page provides a step-by-step guide for Prisma Postgres after setting it up with prisma init --db:

This guide assumes you set up Prisma Postgres instance with prisma init --db:

Once this command terminated:

If you ran the prisma init --db command inside a folder where you want your project to live, you can skip this step and proceed to the next section.

If you ran the command outside your intended project directory (e.g., in your home folder or another location), you need to move the generated prisma folder and the .env file into a dedicated project directory.

Create a new folder (e.g. hello-prisma) where you want your project to live and move the necessary files into it:

Navigate into your project folder:

Now that your project is in the correct location, continue with the setup.

Initialize a TypeScript project and add the Prisma CLI as a development dependency:

This creates a package.json file with an initial setup for your TypeScript app.

Next, initialize TypeScript with a tsconfig.json file in the project:

Install the required dependencies to use Prisma Postgres:

Create an index.ts file in the root directory, this will be used to query your application with Prisma ORM:

Update your prisma/schema.prisma file to include a simple User model:

After adding the models, migrate your database using Prisma Migrate:

Paste the following boilerplate into index.ts:

This code contains a main function that's invoked at the end of the script. It also instantiates PrismaClient which you'll use to send queries to your database.

Let's start with a small query to create a new User record in the database and log the resulting object to the console. Add the following code to your index.ts file:

Next, execute the script with the following command:

Great job, you just created your first database record with Prisma Postgres! 🎉

Prisma ORM offers various queries to read data from your database. In this section, you'll use the findMany query that returns all the recor

*[Content truncated - see full docs]*

**Examples**:

```terminal
npx prisma@latest init --db
```

```terminal
mkdir hello-prismamv .env ./hello-prisma/mv prisma ./hello-prisma/
```

```terminal
cd ./hello-prisma
```

---

## Generating Prisma Client | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-client/setup-and-configuration/generating-prisma-client

**Contents**:
- Generating Prisma Client
- The location of Prisma Client​
  - Using a custom output path​
- The @prisma/client npm package​

Prisma Client is a generated database client that's tailored to your database schema. By default, Prisma Client is generated into the node_modules/.prisma/client folder, but we highly recommend you specify an output location.

In Prisma ORM 7, Prisma Client will no longer be generated in node_modules by default and will require an output path to be defined. Learn more below on how to define an output path.

If Prisma ORM's Rust engine binaries cause large bundle sizes, slow builds, or deployment issues (for example, in serverless or edge environments), you can use it without them using this configuration of your generator block:

Prisma ORM without Rust binaries has been Generally Available since v6.16.0.

Note that you need to use a driver adapter in this case.

When using this architecture:

This setup can simplify deployments in serverless or edge runtimes. Learn more in the docs here.

To generate and instantiate Prisma Client:

Ensure that you have Prisma CLI installed on your machine.

Add the following generator definition to your Prisma schema:

Feel free to customize the output location to match your application. Common directories are app, src, or even the root of your project.

Install the @prisma/client npm package:

Generate Prisma Client with the following command:

You can now instantiate Prisma Client in your code:

Important: You need to re-run the prisma generate command after every change that's made to your Prisma schema to update the generated Prisma Client code.

Here is a graphical illustration of the typical workflow for generation of Prisma Client:

We strongly recommend you define a custom output path. In Prisma ORM version 6.6.0, not defining an output path will result in a warning. In Prisma ORM 7, the field will be required.

You can also specify a custom output path on the generator configuration, for example (assuming your schema.prisma file is located at the default prisma subfolder):

After running prisma generate for that schema fil

*[Content truncated - see full docs]*

**Examples**:

```prisma
generator client {  provider   = "prisma-client-js" // or "prisma-client"  engineType = "client"}
```

```terminal
npm install prisma --save-dev
```

```prisma
generator client {  provider = "prisma-client-js"  output   = "app/generated/prisma/client"}
```

---

## Get started with Prisma | Prisma Documentation

**URL**: https://www.prisma.io/docs/getting-started

**Contents**:
- Get started
- Prisma ORM​
  - The easiest way to get started with Prisma​
        - Prisma Starter Template
  - Explore quickly with a SQLite database​
        - Quickstart
        - Examples
  - Choose an option to get started with your own database​

Explore our products that make it easy to build and scale data-driven applications:

Prisma ORM is a next-generation Node.js and TypeScript ORM that unlocks a new level of developer experience when working with databases thanks to its intuitive data model, automated migrations, type-safety & auto-completion.

Prisma Postgres is a managed PostgreSQL service that gives you an always-on database with pay-as-you-go pricing.

Prisma Optimize helps you analyze queries, generate insights, and provides recommendations to make your database queries faster.

Prisma Accelerate is a global database cache with scalable connection pooling to make your queries fast.

Add Prisma ORM to your application in a few minutes to start modeling your data, run schema migrations and query your database.

Explore all Prisma products at once.

Create a new database, model your data, run migrations, and send queries in this comprehensive 5 minute tutorial.

These options don't require you to have your own database running.

Set up Prisma ORM from scratch with a SQLite database in 5 minutes.

Explore our ready-to-run examples with your favorite frameworks and libraries.

Select one of these options if you want to connect Prisma ORM to your own database.

Set up Prisma ORM from scratch with your favorite database and learn basic workflows like data modeling, querying, and migrations.

Get started with Prisma ORM and your existing database by introspecting your database schema and learn how to query your database.

Make your database queries faster by scaling your database connections and caching database results at the edge with Prisma Accelerate.

Add Accelerate to your app to use global database caching & connection pooling.

Explore our ready-to-run examples using Accelerate.

Run the speed test to see how Prisma Accelerate can make your app faster.

Make your database queries faster by using the insights and recommendations generated by Prisma Optimize.

Add Optimize to your app to gather use

*[Content truncated - see full docs]*

---

## Getting started with Prisma Accelerate | Prisma Documentation

**URL**: https://www.prisma.io/docs/accelerate/getting-started

**Contents**:
- Getting started with Prisma Accelerate
- Prerequisites​
- 1. Enable Accelerate​
- 2. Add Accelerate to your application​
  - 2.1. Update your database connection string​
  - 2.2. Install the Accelerate Prisma Client extension​
  - 2.3. Generate Prisma Client for Accelerate​
  - 2.4. Extend your Prisma Client instance with the Accelerate extension​

To get started with Accelerate, you will need the following:

Navigate to your Prisma Data Platform project, choose an environment, and enable Accelerate by providing your database connection string and selecting the region nearest your database.

If you require IP allowlisting or firewall configurations with trusted IP addresses, enable Static IP for enhanced security. Learn more on how to enable static IP for Accelerate in the Platform Console.

Once enabled, you'll be prompted to generate an API key that you'll use in your new Accelerate connection string to authenticate requests.

Replace your direct database url with your new Accelerate connection string.

Your updated connection string will be used as the datasource url in your Prisma schema file;

Prisma Migrate and Introspection do not work with a prisma:// connection string. In order to continue using these features add a new variable to the .env file named DIRECT_DATABASE_URL whose value is the direct database connection string:

Then in your Prisma schema's datasource block add a field named directUrl with the following:

Migrations and introspections will use the directUrl connection string rather than the one defined in url when this configuration is provided.

directUrl is useful for you to carry out migrations and introspections. However, you don't need directUrl to use Accelerate in your application.

If you are using Prisma with PostgreSQL, there is no need for directUrl, as Prisma Migrate and Introspection work with the prisma+postgres:// connection string.

💡 Accelerate requires Prisma Client version 4.16.1 or higher and @prisma/extension-accelerate version 1.0.0 or higher.

💡 Accelerate extension @prisma/extension-accelerate version 2.0.0 and above requires Node.js version 18 or higher.

Install the latest version of Prisma Client and Accelerate Prisma Client extension

If you're using Prisma version 5.2.0 or greater, Prisma Client will automatically determine how it should connect to the databas

*[Content truncated - see full docs]*

**Examples**:

```env
# New Accelerate connection string with generated API_KEYDATABASE_URL="prisma://accelerate.prisma-data.net/?api_key=__API_KEY__"# Previous (direct) database connection string# DATABASE_URL="postgresql://user:password@host:port/db_name?schema=public"
```

```prisma
datasource db {  provider = "postgresql"  url      = env("DATABASE_URL")}
```

```env
DATABASE_URL="prisma://accelerate.prisma-data.net/?api_key=__API_KEY__"DIRECT_DATABASE_URL="postgresql://user:password@host:port/db_name?schema=public"
```

---

## Getting started with Prisma Optimize | Prisma Documentation

**URL**: https://www.prisma.io/docs/optimize/getting-started

**Contents**:
- Getting Started
- Prerequisites​
- 1. Launch Optimize​
- 2. Add Optimize to your application​
  - 2.1. Install the Optimize Prisma Client extension​
  - 2.2. Add the Optimize API Key to your .env file​
  - 2.3. Extend your Prisma Client instance​
    - Using the Optimize extension with other extensions or middleware​

Before you begin with Prisma Optimize, ensure you have the following:

Prisma Optimize is intended for use in local environments. Learn more in the FAQ.

Install Prisma Client and the Optimize extension:

For versions of Prisma ORM between 4.2.0 and 6.1.0, you need to enable the tracing preview feature in your Prisma schema file.

Generate a Prisma Optimize API key and add it to your .env file:

Extend your existing Prisma Client instance with the Optimize extension:

Since extensions are applied one after another, make sure you apply them in the correct order. Extensions cannot share behavior and the last extension applied takes precedence.

If you are using Prisma Accelerate in your application, make sure you apply it after the Optimize extension. For example:

If you are using Prisma Middleware in your application, make sure they are added before any Prisma Client extensions (like Optimize). For example:

Follow these steps to start generating query insights with Prisma Optimize:

In the Optimize dashboard, click the Start recording button, then run your app and execute some Prisma queries while recording is active.

After your app runs and generates insights based on the executed Prisma queries, click the Stop recording button.

Explore individual query details by clicking on them, and check the Recommendations tab for any suggested improvements to enhance query performance.

Use Prisma AI to understand recommendations and apply them within your Prisma model context.

For a hands-on learning experience, try out the step-by-step example.

If you need assistance, reach out in the #help-and-questions channel on our Discord, or connect with our community to see how others are using Optimize.

**Examples**:

```bash
npm install @prisma/client@latest @prisma/extension-optimize
```

```prisma
generator client {  provider = "prisma-client-js"  previewFeatures = ["tracing"]}
```

```bash
OPTIMIZE_API_KEY="YOUR_OPTIMIZE_API_KEY"
```

---

## Import from existing Postgres database into Prisma Postgres | Prisma Documentation

**URL**: https://www.prisma.io/docs/getting-started/prisma-postgres/import-from-existing-database-postgresql

**Contents**:
- Import data from an existing database
- Prerequisites​
- 1. Create a new Prisma Postgres database​
- 2. Export data from your existing database​
- 3. Import data into Prisma Postgres​
  - 3.1. Connecting to the Prisma Postgres Database with @prisma/ppg-tunnel​
  - 3.2. Restoring the Backup with pg_restore​
- 4. Update your application code to query Prisma Postgres​

This guide provides step-by-step instructions for importing data from an existing PostgreSQL database into Prisma Postgres.

You can accomplish this migration in three steps:

In the third step, you will be using a direct connection to securely connect to your Prisma Postgres database during to run pg_restore.

Follow these steps to create a new Prisma Postgres database:

With your Prisma Postgres instance being created, you can move to the next step.

In this step, you're going to export the data from your existing database and store it in a .bak file on your local machine.

Make sure to have the connection URL for your existing database ready, it should be structured like this:

Expand below for provider-specific instructions that help you determine the right connection string:

Next, run the following command to export the data of your PostgreSQL database (replace the __DATABASE_URL__ placeholder with your actual database connection URL):

Here's a quick overview of the CLI options that were used for this command:

Running this command will create a backup file named db_dump.bak which you will use to restore the data into your Prisma Postgres database in the next step.

In this section, you'll use a TCP Tunnel in order to connect to your Prisma Postgres instance and import data via pg_restore.

Open a new terminal and set the environment variable for your Prisma Postgres database connection URL.

You should see output similar to:

Keep this tunnel process running to maintain the connection!

Use the backup file from Step 2 to restore data into Prisma Postgres database with pg_restore by running this command:

Once the command completes execution, you will have successfully imported the data from your existing PostgreSQL database into Prisma Postgres 🎉

To validate that the import worked, you can use Prisma Studio. Either open it in the by clicking the Studio tab in the left-hand sidenav in your project or run this command to launch Prisma Studio locally:

If you 

*[Content truncated - see full docs]*

**Examples**:

```no-copy
postgresql://USER:PASSWORD@HOST:PORT/DATABASE
```

```no-copy
postgresql://USER:PASSWORD@YOUR-NEON-HOST/DATABASE?sslmode=require
```

```no-copy
postgres://postgres.apbkobhfnmcqqzqeeqss:[YOUR-PASSWORD]@aws-0-ca-central-1.pooler.supabase.com:5432/postgres
```

---

## Integrate Prisma into a TypeScript Project with MySQL (15 min) | Prisma Documentation

**URL**: https://www.prisma.io/docs/getting-started/setup-prisma/add-to-existing-project/relational-databases-typescript-mysql

**Contents**:
- Add Prisma ORM to an existing project (TypeScript and MySQL)
- Overview​
- Prerequisites​
- Step 1: Set Up Prisma​

This guide walks you through integrating Prisma ORM into an existing Node.js or TypeScript project. You'll learn how to:

Migrating from another ORM? Check out our dedicated guides for TypeORM and Sequelize.

Before you begin, ensure you have:

📌 You'll need your database connection URL, including credentials.

💡 Don’t have a database yet? Try our Quickstart guide with SQLite to explore Prisma ORM.

Open your terminal and navigate to the project directory containing your package.json.

Install Prisma CLI as a development dependency:

**Examples**:

```bash
npm install prisma --save-dev
```

---

## Next steps after adding Prisma ORM to an existing project using MongoDB | Prisma Documentation

**URL**: https://www.prisma.io/docs/getting-started/setup-prisma/add-to-existing-project/mongodb/next-steps

**Contents**:
- Next steps after adding Prisma ORM to an existing project using MongoDB
  - Continue exploring the Prisma Client API​
  - Build an app with Prisma ORM​
  - Explore the data in Prisma Studio​
  - Try a Prisma ORM example​

This section lists a number of potential next steps you can now take from here. Feel free to explore these or read the Introduction page to get a high-level overview of Prisma ORM.

You can send a variety of queries with the Prisma Client API. Check out the API reference and use your existing database setup from this guide to try them out.

You can use your editor's auto-completion feature to learn about the different API calls and the arguments it takes. Auto-completion is commonly invoked by hitting CTRL+SPACE on your keyboard.

Here are a few suggestions for a number of more queries you can send with Prisma Client:

Filter all Post records that contain "hello"

Create a new Post record and connect it to an existing User record

Use the fluent relations API to retrieve the Post records of a User by traversing the relations

The Prisma blog features comprehensive tutorials about Prisma ORM, check out our latest ones:

Prisma Studio is a visual editor for the data in your database. Run npx prisma studio in your terminal.

The prisma-examples repository contains a number of ready-to-run examples:

**Examples**:

```js
const filteredPosts = await prisma.post.findMany({  where: {    OR: [{ title: { contains: 'hello' } }, { body: { contains: 'hello' } }],  },})
```

```js
const post = await prisma.post.create({  data: {    title: 'Join us for Prisma Day 2020',    slug: 'prisma-day-2020',    body: 'A conference on modern application development and databases.',    user: {      connect: { email: 'hello@prisma.com' },    },  },})
```

```js
const user = await prisma.comment  .findUnique({    where: { id: '60ff4e9500acc65700ebf470' },  })  .post()  .user()
```

---

## Next steps after adding Prisma ORM to your existing project | Prisma Documentation

**URL**: https://www.prisma.io/docs/getting-started/setup-prisma/add-to-existing-project/relational-databases/next-steps

**Contents**:
- Next steps after adding Prisma ORM to your existing project
  - Continue exploring the Prisma Client API​
  - Build an app with Prisma ORM​
  - Explore the data in Prisma Studio​
  - Get query insights and analytics with Prisma Optimize​
  - Change the database schema (e.g. add more tables)​
  - Try a Prisma ORM example​

This section lists a number of potential next steps you can now take from here. Feel free to explore these or read the Introduction page to get a high-level overview of Prisma ORM.

You can send a variety of queries with the Prisma Client API. Check out the API reference and use your existing database setup from this guide to try them out.

You can use your editor's auto-completion feature to learn about the different API calls and the arguments it takes. Auto-completion is commonly invoked by hitting CTRL+SPACE on your keyboard.

Here are a few suggestions for a number of more queries you can send with Prisma Client:

Filter all Post records that contain "hello"

Create a new Post record and connect it to an existing User record

Use the fluent relations API to retrieve the Post records of a User by traversing the relations

The Prisma blog features comprehensive tutorials about Prisma ORM, check out our latest ones:

Prisma Studio is a visual editor for the data in your database. Run npx prisma studio in your terminal.

Prisma Optimize helps you generate insights and provides recommendations that can help you make your database queries faster. Try it out now!

Optimize aims to help developers of all skill levels write efficient database queries, reducing database load and making applications more responsive.

To evolve the app, you need to follow the same flow of the tutorial:

The prisma-examples repository contains a number of ready-to-run examples:

**Examples**:

```js
const filteredPosts = await prisma.post.findMany({  where: {    OR: [      { title: { contains: "hello" },      { content: { contains: "hello" },    ],  },})
```

```js
const post = await prisma.post.create({  data: {    title: 'Join us for Prisma Day 2020',    author: {      connect: { email: 'alice@prisma.io' },    },  },})
```

```js
const posts = await prisma.profile  .findUnique({    where: { id: 1 },  })  .user()  .posts()
```

---

## Next steps after setting up Prisma ORM with MongoDB | Prisma Documentation

**URL**: https://www.prisma.io/docs/getting-started/setup-prisma/start-from-scratch/mongodb/next-steps

**Contents**:
- Next steps after setting up Prisma ORM with MongoDB
  - Continue exploring the Prisma Client API​
  - Build an app with Prisma ORM​
  - Explore the data in Prisma Studio​
  - Try a Prisma ORM example​

This section lists a number of potential next steps you can now take from here. Feel free to explore these or read the Introduction page to get a high-level overview of Prisma ORM.

You can send a variety of queries with the Prisma Client API. Check out the API reference and use your existing database setup from this guide to try them out.

You can use your editor's auto-completion feature to learn about the different API calls and the arguments it takes. Auto-completion is commonly invoked by hitting CTRL+SPACE on your keyboard.

Here are a few suggestions for a number of more queries you can send with Prisma Client:

Filter all Post records that contain "hello"

Create a new Post record and connect it to an existing User record

Use the fluent relations API to retrieve the Post records of a User by traversing the relations

The Prisma blog features comprehensive tutorials about Prisma ORM, check out our latest ones:

Prisma Studio is a visual editor for the data in your database. Run npx prisma studio in your terminal.

The prisma-examples repository contains a number of ready-to-run examples:

**Examples**:

```js
const filteredPosts = await prisma.post.findMany({  where: {    OR: [{ title: { contains: 'hello' } }, { body: { contains: 'hello' } }],  },})
```

```js
const post = await prisma.post.create({  data: {    title: 'Join us for Prisma Day 2020',    slug: 'prisma-day-2020',    body: 'A conference on modern application development and databases.',    user: {      connect: { email: 'hello@prisma.com' },    },  },})
```

```js
const user = await prisma.comment  .findUnique({    where: { id: '60ff4e9500acc65700ebf470' },  })  .post()  .user()
```

---

## Prisma Postgres | Prisma Documentation

**URL**: https://www.prisma.io/docs/getting-started/prisma-postgres

**Contents**:
- Prisma Postgres
- In this section​
- From the CLI
- Upgrade from Early Access
- Import from existing database

This page provides a step-by-step guide for Prisma Postgres after setting it up with prisma init --db:

This guide shows you how to migrate your Prisma Postgres Early Access (EA) database to the now official Prisma Postgres General Availability (GA) database. Prisma Postgres Early Access was introduced to allow early adopters to test Prisma’s new managed PostgreSQL service. As we move to GA, it's crucial to safely migrate data from your EA database to the new GA database.

---

## Quickstart with TypeScript & Prisma Postgres | Prisma Documentation

**URL**: https://www.prisma.io/docs/getting-started/quickstart-prismaPostgres

**Contents**:
- Quickstart with Prisma Postgres
- Prerequisites​
- 1. Set up a Prisma Postgres database in the Platform Console​
- 2. Download example and install dependencies​
- 3. Set database connection URL​
- 4. Create database tables (with a schema migration)​
- 5. Execute queries with Prisma ORM​
- 6. Explore caching with Prisma Accelerate​

In this Quickstart guide, you'll learn how to get started from scratch with Prisma ORM and a Prisma Postgres database in a plain TypeScript project. It covers the following workflows:

If you want to use Prisma Postgres with another ORM or database library (like Drizzle ORM, TypeORM or Kysely), you can follow the instructions here.

To successfully complete this tutorial, you need:

Follow these steps to create your Prisma Postgres database:

At this point, you'll be redirected to the Database page where you will need to wait for a few seconds while the status of your database changes from PROVISIONING to CONNECTED.

Once the green CONNECTED label appears, your database is ready to use!

Copy the try-prisma command that's shown in the Console, paste it into your terminal and execute it.

For reference, this is what the command looks like:

Once the try-prisma command has terminated, navigate into the project directory:

The connection to your database is configured via an environment variable in a .env file.

First, rename the existing .env.example file to just .env:

Then, in your project environment in the Platform console, find your database credentials in the Set up database access section, copy the DATABASE_URL environment variable and paste them into the .env file.

For reference, the file should now look similar to this:

Next, you need to create the tables in your database. You can do this by creating and executing a schema migration with the following command of the Prisma CLI:

This will map the User and Post models that are defined in your Prisma schema to your database. You can also review the SQL migration that was executed and created the tables in the newly created prisma/migrations directory.

The src/queries.ts script contains a number of CRUD queries that will write and read data in your database. You can execute it by running the following command in your terminal:

Once the script has completed, you can inspect the logs in your terminal or use Pr

*[Content truncated - see full docs]*

**Examples**:

```terminal
npx try-prisma@latest \  --template databases/prisma-postgres \  --name hello-prisma \  --install npm
```

```terminal
cd hello-prisma
```

```terminal
mv .env.example .env
```

---

## Quickstart with TypeScript & SQLite | Prisma Documentation

**URL**: https://www.prisma.io/docs/getting-started/quickstart-sqlite

**Contents**:
- Quickstart with SQLite
- Prerequisites​
- 1. Create TypeScript project and set up Prisma ORM​
- 2. Model your data in the Prisma schema​
- 3. Run a migration to create your database tables with Prisma Migrate​
- 4. Explore how to send queries to your database with Prisma Client​
  - 4.1. Create a new User record​
  - 4.2. Retrieve all User records​

In this Quickstart guide, you'll learn how to get started with Prisma ORM from scratch using a plain TypeScript project and a local SQLite database file. It covers data modeling, migrations and querying a database.

If you want to use Prisma ORM with your own PostgreSQL, MySQL, MongoDB or any other supported database, go here instead:

You need Node.js installed on your machine (see system requirements for officially supported versions).

As a first step, create a project directory and navigate into it:

Next, initialize a TypeScript project using npm:

This creates a package.json with an initial setup for your TypeScript app.

See installation instructions to learn how to install Prisma using a different package manager.

Now, initialize TypeScript:

Then, install the Prisma CLI as a development dependency in the project:

Finally, set up Prisma ORM with the init command of the Prisma CLI:

This creates a new prisma directory with a schema.prisma file and configures SQLite as your database. You're now ready to model your data and create your database with some tables.

The Prisma schema provides an intuitive way to model data. Add the following models to your schema.prisma file:

Models in the Prisma schema have two main purposes:

In the next section, you will map these models to database tables using Prisma Migrate.

At this point, you have a Prisma schema but no database yet. Run the following command in your terminal to create the SQLite database and the User and Post tables represented by your models:

This command did three things:

Because the SQLite database file didn't exist before, the command also created it inside the prisma directory with the name dev.db as defined via the environment variable in the .env file.

Congratulations, you now have your database and tables ready. Let's go and learn how you can send some queries to read and write data!

To get started with Prisma Client, you need to install the @prisma/client package:

The install command invo

*[Content truncated - see full docs]*

**Examples**:

```terminal
mkdir hello-prismacd hello-prisma
```

```terminal
npm init -ynpm install typescript tsx @types/node --save-dev
```

```terminal
npx tsc --init
```

---

## Set up Prisma ORM | Prisma Documentation

**URL**: https://www.prisma.io/docs/getting-started/setup-prisma

**Contents**:
- Set up Prisma ORM
- In this section​
- Start from scratch
- Add to existing project

Start from scratch or add Prisma ORM to an existing project. The following tutorials introduce you to the Prisma CLI, Prisma Client, and Prisma Migrate.

---

## Setup & configuration | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-client/setup-and-configuration

**Contents**:
- Setup & configuration
- In this section​
- Introduction
- Generating Prisma Client
- Instantiating Prisma Client
- Database connections
- Custom model and field names
- Configuring error formatting

This section describes how to set up, generate, configure, and instantiate PrismaClient , as well as when and how to actively manage connections.

Prisma Client is an auto-generated and type-safe query builder that's tailored to your data. The easiest way to get started with Prisma Client is by following the Quickstart.

Prisma Client is a generated database client that's tailored to your database schema. By default, Prisma Client is generated into the node_modules/.prisma/client folder, but we highly recommend you specify an output location.

The following example demonstrates how to import and instantiate your generated client from the default path:

The Prisma Client API is generated based on the models in your Prisma schema. Models are typically 1:1 mappings of your database tables.

By default, Prisma Client uses ANSI escape characters to pretty print the error stack and give recommendations on how to fix a problem. While this is very useful when using Prisma Client from the terminal, in contexts like a GraphQL API, you only want the minimal error without any additional formatting.

Read replicas enable you to distribute workloads across database replicas for high-traffic workloads. The read replicas extension, @prisma/extension-read-replicas, adds support for read-only database replicas to Prisma Client.

Prisma Client provides features that are typically either not achievable with particular databases or require extensions. These features are referred to as polyfills. For all databases, this includes:

As of v6.16.0, usage of Prisma ORM without Rust engine binaries on PostgreSQL, CockroachDB, Neon, MySQL, PlanetScale, SQLite, D1 & MS SQL Server databases has been Generally Available.

---

## Start from scratch with Prisma ORM | Prisma Documentation

**URL**: https://www.prisma.io/docs/getting-started/setup-prisma/start-from-scratch

**Contents**:
- Start from scratch
- In this section​
- Relational databases
- MongoDB

Start a fresh project from scratch with the following tutorials as they introduce you to the Prisma CLI, Prisma Client, and Prisma Migrate.

---

## Start from scratch with Prisma ORM using MongoDB and TypeScript (15 min) | Prisma Documentation

**URL**: https://www.prisma.io/docs/getting-started/setup-prisma/start-from-scratch/mongodb-typescript-mongodb

**Contents**:
- Start from scratch with Prisma ORM using MongoDB and TypeScript
- Prerequisites​
- Create project setup​

Learn how to create a new Node.js or TypeScript project from scratch by connecting Prisma ORM to your MongoDB database and generating a Prisma Client for database access. The following tutorial introduces you to the Prisma CLI and Prisma Client.

In order to successfully complete this guide, you need:

Node.js installed on your machine (see system requirements for officially supported versions)

Access to a MongoDB 4.2+ server with a replica set deployment. We recommend using MongoDB Atlas.

The MongoDB database connector uses transactions to support nested writes. Transactions require a replica set deployment. The easiest way to deploy a replica set is with Atlas. It's free to get started.

Make sure you have your database connection URL at hand. If you don't have a database server running and just want to explore Prisma ORM, check out the Quickstart.

See System requirements for exact version requirements.

As a first step, create a project directory and navigate into it:

Next, initialize a TypeScript project and add the Prisma CLI as a development dependency to it:

This creates a package.json with an initial setup for your TypeScript app.

Next, initialize TypeScript:

You can now invoke the Prisma CLI by prefixing it with npx:

Next, set up your Prisma ORM project by creating your Prisma Schema file with the following command:

This command does a few things:

Note that the default schema created by prisma init uses PostgreSQL as the provider. If you didn't specify a provider with the datasource-provider option, you need to edit the datasource block to use the mongodb provider instead:

**Examples**:

```terminal
mkdir hello-prismacd hello-prisma
```

```terminal
npm init -ynpm install prisma typescript tsx @types/node --save-dev
```

```terminal
npx tsc --init
```

---

## Start from scratch with Prisma ORM using TypeScript and PlanetScale (15 min) | Prisma Documentation

**URL**: https://www.prisma.io/docs/getting-started/setup-prisma/start-from-scratch/relational-databases-typescript-planetscale

**Contents**:
- Relational databases (TypeScript and PlanetScale)
- Prerequisites​
- Create project setup​

Learn how to create a new Node.js or TypeScript project from scratch by connecting Prisma ORM to your database and generating a Prisma Client for database access. The following tutorial introduces you to the Prisma CLI, Prisma Client, and Prisma Migrate.

In order to successfully complete this guide, you need:

This tutorial will also assume that you can push to the main branch of your database. Do not do this if your main branch has been promoted to production.

See System requirements for exact version requirements.

Make sure you have your database connection URL at hand. If you don't have a database server running and just want to explore Prisma ORM, check out the Quickstart.

As a first step, create a project directory and navigate into it:

Next, initialize a TypeScript project and add the Prisma CLI as a development dependency to it:

This creates a package.json with an initial setup for your TypeScript app.

Next, initialize TypeScript:

See installation instructions to learn how to install Prisma using a different package manager.

You can now invoke the Prisma CLI by prefixing it with npx:

Next, set up your Prisma ORM project by creating your Prisma Schema file with the following command:

This command does a few things:

Note that the default schema created by prisma init uses PostgreSQL as the provider. If you didn't specify a provider with the datasource-provider option, you need to edit the datasource block to use the mysql provider instead:

**Examples**:

```terminal
mkdir hello-prismacd hello-prisma
```

```terminal
npm init -ynpm install prisma typescript tsx @types/node --save-dev
```

```terminal
npx tsc --init
```

---

## Start from scratch with Prisma ORM using TypeScript and SQL Server (15 min) | Prisma Documentation

**URL**: https://www.prisma.io/docs/getting-started/setup-prisma/start-from-scratch/relational-databases-typescript-sqlserver

**Contents**:
- Relational databases (TypeScript and SQL Server)
- Prerequisites​
- Create project setup​

Learn how to create a new Node.js or TypeScript project from scratch by connecting Prisma ORM to your database and generating a Prisma Client for database access. The following tutorial introduces you to the Prisma CLI, Prisma Client, and Prisma Migrate.

In order to successfully complete this guide, you need:

See System requirements for exact version requirements.

Make sure you have your database connection URL at hand. If you don't have a database server running and just want to explore Prisma ORM, check out the Quickstart.

As a first step, create a project directory and navigate into it:

Next, initialize a TypeScript project and add the Prisma CLI as a development dependency to it:

This creates a package.json with an initial setup for your TypeScript app.

Next, initialize TypeScript:

See installation instructions to learn how to install Prisma using a different package manager.

You can now invoke the Prisma CLI by prefixing it with npx:

Next, set up your Prisma ORM project by creating your Prisma Schema file with the following command:

This command does a few things:

Note that the default schema created by prisma init uses PostgreSQL as the provider. If you didn't specify a provider with the datasource-provider option, you need to edit the datasource block to use the sqlserver provider instead:

**Examples**:

```terminal
mkdir hello-prismacd hello-prisma
```

```terminal
npm init -ynpm install prisma typescript tsx @types/node --save-dev
```

```terminal
npx tsc --init
```

---

## Start from scratch with Prisma ORM using TypeScript and MySQL (15 min) | Prisma Documentation

**URL**: https://www.prisma.io/docs/getting-started/setup-prisma/start-from-scratch/relational-databases-typescript-mysql

**Contents**:
- Relational databases (TypeScript and MySQL)
- Prerequisites​
- Create project setup​

Learn how to create a new Node.js or TypeScript project from scratch by connecting Prisma ORM to your database and generating a Prisma Client for database access. The following tutorial introduces you to the Prisma CLI, Prisma Client, and Prisma Migrate.

In order to successfully complete this guide, you need:

See System requirements for exact version requirements.

Make sure you have your database connection URL at hand. If you don't have a database server running and just want to explore Prisma ORM, check out the Quickstart.

As a first step, create a project directory and navigate into it:

Next, initialize a TypeScript project and add the Prisma CLI as a development dependency to it:

This creates a package.json with an initial setup for your TypeScript app.

Next, initialize TypeScript:

See installation instructions to learn how to install Prisma using a different package manager.

You can now invoke the Prisma CLI by prefixing it with npx:

Next, set up your Prisma ORM project by creating your Prisma Schema file with the following command:

This command does a few things:

Note that the default schema created by prisma init uses PostgreSQL as the provider. If you didn't specify a provider with the datasource-provider option, you need to edit the datasource block to use the mysql provider instead:

**Examples**:

```terminal
mkdir hello-prismacd hello-prisma
```

```terminal
npm init -ynpm install prisma typescript tsx @types/node --save-dev
```

```terminal
npx tsc --init
```

---

## Start from scratch with Prisma ORM using TypeScript and CockroachDB (15 min) | Prisma Documentation

**URL**: https://www.prisma.io/docs/getting-started/setup-prisma/start-from-scratch/relational-databases-typescript-cockroachdb

**Contents**:
- Relational databases (TypeScript and CockroachDB)
- Prerequisites​
- Create project setup​

Learn how to create a new Node.js or TypeScript project from scratch by connecting Prisma ORM to your database and generating a Prisma Client for database access. The following tutorial introduces you to the Prisma CLI, Prisma Client, and Prisma Migrate.

In order to successfully complete this guide, you need:

See System requirements for exact version requirements.

Make sure you have your database connection URL at hand. If you don't have a database server running and just want to explore Prisma ORM, check out the Quickstart.

As a first step, create a project directory and navigate into it:

Next, initialize a TypeScript project and add the Prisma CLI as a development dependency to it:

This creates a package.json with an initial setup for your TypeScript app.

Next, initialize TypeScript:

See installation instructions to learn how to install Prisma using a different package manager.

You can now invoke the Prisma CLI by prefixing it with npx:

Next, set up your Prisma ORM project by creating your Prisma Schema file with the following command:

This command does a few things:

Note that the default schema created by prisma init uses PostgreSQL as the provider. If you didn't specify a provider with the datasource-provider option, you need to edit the datasource block to use the cockroachdb provider instead:

**Examples**:

```terminal
mkdir hello-prismacd hello-prisma
```

```terminal
npm init -ynpm install prisma typescript tsx @types/node --save-dev
```

```terminal
npx tsc --init
```

---

## Start from scratch with Prisma ORM using TypeScript and Prisma Postgres (15 min) | Prisma Documentation

**URL**: https://www.prisma.io/docs/getting-started/setup-prisma/start-from-scratch/relational-databases-typescript-prismaPostgres

**Contents**:
- Relational databases (TypeScript and Prisma Postgres)
- Prerequisites​
- Create project setup​

Learn how to create a new TypeScript project with a Prisma Postgres database from scratch. This tutorial introduces you to the Prisma CLI, Prisma Client, and Prisma Migrate and covers the following workflows:

To successfully complete this tutorial, you need:

Create a project directory and navigate into it:

Next, initialize a TypeScript project and add the Prisma CLI as a development dependency to it:

This creates a package.json with an initial setup for your TypeScript app.

Next, initialize TypeScript:

You can now invoke the Prisma CLI by prefixing it with npx:

Next, set up your Prisma ORM project by creating your Prisma Schema file with the following command:

This command does a few things:

In the next section, you'll learn how to connect your Prisma Postgres database to the project you just created on your file system.

**Examples**:

```terminal
mkdir hello-prismacd hello-prisma
```

```terminal
npm init -ynpm install prisma typescript tsx @types/node --save-dev
```

```terminal
npx tsc --init
```

---

## Start from scratch with Prisma ORM using TypeScript and PostgreSQL (15 min) | Prisma Documentation

**URL**: https://www.prisma.io/docs/getting-started/setup-prisma/start-from-scratch/relational-databases-typescript-postgresql

**Contents**:
- Relational databases (TypeScript and PostgreSQL)
- Prerequisites​
- Create project setup​

Learn how to create a new Node.js or TypeScript project from scratch by connecting Prisma ORM to your database and generating a Prisma Client for database access. The following tutorial introduces you to the Prisma CLI, Prisma Client, and Prisma Migrate.

In order to successfully complete this guide, you need:

See System requirements for exact version requirements.

Make sure you have your database connection URL at hand. If you don't have a database server running and just want to explore Prisma ORM, check out the Quickstart.

As a first step, create a project directory and navigate into it:

Next, initialize a TypeScript project and add the Prisma CLI as a development dependency to it:

This creates a package.json with an initial setup for your TypeScript app.

Next, initialize TypeScript:

See installation instructions to learn how to install Prisma using a different package manager.

You can now invoke the Prisma CLI by prefixing it with npx:

Next, set up your Prisma ORM project by creating your Prisma Schema file with the following command:

This command does a few things:

Note that the default schema created by prisma init uses PostgreSQL as the provider. If you didn't specify a provider with the datasource-provider option, you need to edit the datasource block to use the postgresql provider instead:

**Examples**:

```terminal
mkdir hello-prismacd hello-prisma
```

```terminal
npm init -ynpm install prisma typescript tsx @types/node --save-dev
```

```terminal
npx tsc --init
```

---

## Upgrade Prisma Postgres from Early Access | Prisma Documentation

**URL**: https://www.prisma.io/docs/getting-started/prisma-postgres/upgrade-from-early-access

**Contents**:
- Upgrade from Early Access
- Prerequisites​
- Option A: Interactive approach​
  - Steps​
- Option B: Manual backup-and-restore approach​
- 1. Back up the EA database​
  - 1.1. Connecting to the EA database directly with @prisma/ppg-tunnel​
  - 1.2. Creating the Backup with pg_dump​

This guide shows you how to migrate your Prisma Postgres Early Access (EA) database to the now official Prisma Postgres General Availability (GA) database. Prisma Postgres Early Access was introduced to allow early adopters to test Prisma’s new managed PostgreSQL service. As we move to GA, it's crucial to safely migrate data from your EA database to the new GA database.

Prisma will not automatically migrate your data to ensure its integrity. Instead, this process must be done manually. You can accomplish this in three main steps:

We will be using the @prisma/ppg-tunnel package to securely connect to both databases. This tool sets up a secure proxy tunnel, eliminating the need for manual credential handling.

You can learn more about Prisma Postgres on this page.

Before you begin, make sure you have:

To create and restore backups, ensure you have the PostgreSQL command-line tools installed. Run the following commands based on your operating system:

If you installed PostgreSQL but still see a “command not found” error for pg_dump or pg_restore, ensure your installation directory is in your system’s PATH environment variable.

Please make sure that you are installing Postgresql version 16. Other versions may cause errors during the backup and restore process.

This approach is recommended if you prefer a guided, one-command solution. In this mode, the @prisma/ppg-tunnel CLI:

Interactive mode does not accept any CLI arguments or read API keys from the environment. You must provide them interactively.

When prompted, paste your Early Access database key or connection string. The CLI will create a .bak file in the current directory.

When prompted again, paste your GA database key or connection string. The CLI will automatically restore the .bak file into the new GA database.

Once complete, connect with your favorite Database IDE to verify your data in the GA database.

If you prefer or need finer control over the migration process (or to pass environment variables

*[Content truncated - see full docs]*

**Examples**:

```terminal
brew install postgresql@16which pg_dumpwhich pg_restore
```

```terminal
# Download from the official PostgreSQL website:# https://www.postgresql.org/download/windows/# During installation, select "Command Line Tools".# Then verify with:where pg_dumpwhere pg_restore
```

```terminal
sudo apt-get updatesudo apt-get install postgresql-client-16which pg_dumpwhich pg_restore
```

---
