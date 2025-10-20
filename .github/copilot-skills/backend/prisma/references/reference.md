# Prisma - Reference

**Pages**: 13

---

## Accelerate: API Reference | Prisma Documentation

**URL**: https://www.prisma.io/docs/accelerate/api-reference

**Contents**:
- API Reference
- cacheStrategy​
  - Options​
  - Examples​
  - Supported Prisma Client operations​
- withAccelerateInfo​
  - Return type​
- $accelerate.invalidate​

The Accelerate API reference documentation is based on the following schema:

All example are based on the User model.

With the Accelerate extension for Prisma Client, you can use the cacheStrategy parameter for model queries and use the ttl and swr parameters to define a cache strategy for Accelerate. The Accelerate extension requires that you install Prisma Client version 4.10.0.

The cacheStrategy parameter takes an option with the following keys:

Add a caching strategy to the query, defining a 60-second stale-while-revalidate (SWR) value, a 60-second time-to-live (TTL) value, and a cache tag of "emails_with_alice":

The following is a list of all read query operations that support cacheStrategy:

The cacheStrategy parameter is not supported on any write operations, such as create().

Any query that supports the cacheStrategy can append withAccelerateInfo() to wrap the response data and include additional information about the Accelerate response.

To retrieve the status of the response, use:

Notice the info property of the response object. This is where the request information is stored.

The info object is of type AccelerateInfo and follows the interface below:

You can invalidate the cache using the $accelerate.invalidate API.

To invalidate cached query results on-demand, a paid plan is required. Each plan has specific limits on the number of cache tag-based invalidations allowed per day, though there are no limits on calling the $accelerate.invalidate API itself. See our pricing for more details.

To invalidate the query below:

You need to provide the cache tag in the $accelerate.invalidate API:

You can invalidate up to 5 tags per call.

You can invalidate the entire cache using the $accelerate.invalidateAll API.

To invalidate the query below:

Just call the $accelerate.invalidateAll API:

This method offers better editor support (e.g. IntelliSense) than alternatives like invalidate("all").

This clears cache for the entire environment—use with care.



*[Content truncated - see full docs]*

**Examples**:

```prisma
model User {  id    Int     @id @default(autoincrement())  name  String?  email String  @unique}
```

```ts
await prisma.user.findMany({  where: {    email: {      contains: "alice@prisma.io",    },  },  cacheStrategy: {    swr: 60,    ttl: 60,    tags: ["emails_with_alice"],  },});
```

```ts
const { data, info } = await prisma.user  .count({    cacheStrategy: { ttl: 60, swr: 600 },    where: { myField: 'value' },  })  .withAccelerateInfo()console.dir(info)
```

---

## Connection URLs (Reference) | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/reference/connection-urls

**Contents**:
- Connection URLs
- Format​
  - Special characters​
- Examples​
  - Prisma Postgres​
    - Direct TCP​
    - Via Prisma Accelerate (HTTP)​
    - Local Prisma Postgres​

Prisma ORM needs a connection URL to be able to connect to your database, e.g. when sending queries with Prisma Client or when changing the database schema with Prisma Migrate.

The connection URL is provided via the url field of a datasource block in your Prisma schema. It usually consists of the following components (except for SQLite and Prisma Postgres):

Make sure you have this information at hand when getting started with Prisma ORM. If you don't have a database server running yet, you can either use a local SQLite database file (see the Quickstart) or setup a free PostgreSQL database with Prisma Postgres.

The format of the connection URL depends on the database connector you're using. Prisma ORM generally supports the standard formats for each database. You can find out more about the connection URL of your database on the dedicated docs page:

For MySQL, PostgreSQL and CockroachDB you must percentage-encode special characters in any part of your connection URL - including passwords. For example, p@$$w0rd becomes p%40%24%24w0rd.

For Microsoft SQL Server, you must escape special characters in any part of your connection string.

Here are examples for the connection URLs of the databases Prisma ORM supports:

Prisma Postgres is a managed PostgreSQL service running on unikernels. There are several ways to connect to Prisma Postgres:

The connection string formats of these are covered below.

When you connect to Prisma Postgres via direct TCP, your connection string looks as follows:

The USER and PASSWORD values are provided when you generate credentials for your Prisma Postgres instance in the . Here is an example with sample values:

When connecting via Prisma Accelerate, the connection string doesn't require a user/password like a conventional connection string does. Instead, authentication works via an API key:

In this snippet, API_KEY is a placeholder for the API key you are receiving when setting up a new Prismas Postgres instance via the . Here is an e

*[Content truncated - see full docs]*

**Examples**:

```bash
DATABASE_URL="postgres://USER:PASSWORD@db.prisma.io:5432/?sslmode=require"
```

```bash
DATABASE_URL="postgres://2f9881cc7eef46f094ac913df34c1fb441502fe66cbe28cc48998d4e6b20336b:sk_QZ3u8fMPFfBzOID4ol-mV@db.prisma.io:5432/?sslmode=require"
```

```prisma
datasource db {  provider = "postgresql"  url      = "prisma+postgres://accelerate.prisma-data.net/?api_key=API_KEY"}
```

---

## Data sources (Reference) | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-schema/overview/data-sources

**Contents**:
- Data sources
- Securing database connections​

A data source determines how Prisma ORM connects to your database, and is represented by the datasource block in the Prisma schema. The following data source uses the postgresql provider and includes a connection URL:

A Prisma schema can only have one data source. However, you can:

Note: Multiple provider support was removed in 2.22.0. Please see Deprecation of provider array notation for more information.

Some data source providers allow you to configure your connection with SSL/TLS, and provide parameters for the url to specify the location of certificates.

Prisma ORM resolves SSL certificates relative to the ./prisma directory. If your certificate files are located outside that directory, e.g. your project root directory, use relative paths for certificates:

When you're using a multi-file Prisma schema, Prisma ORM resolves SSL certificates relative to the ./prisma/schema directory.

**Examples**:

```prisma
datasource db {  provider = "postgresql"  url      = "postgresql://johndoe:mypassword@localhost:5432/mydb?schema=public"}
```

```prisma
datasource db {  provider = "postgresql"  url      = "postgresql://johndoe:mypassword@localhost:5432/mydb?schema=public&sslmode=require&sslcert=../server-ca.pem&sslidentity=../client-identity.p12&sslpassword=<REDACTED>"}
```

---

## Errors | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/reference/error-reference

**Contents**:
- Error message reference
- Prisma Client error types​
  - PrismaClientKnownRequestError​
  - PrismaClientUnknownRequestError​
  - PrismaClientRustPanicError​
  - PrismaClientInitializationError​
  - PrismaClientValidationError​
- Error codes​

For more information about how to work with exceptions and error codes, see Handling exceptions and errors.

Prisma Client throws different kinds of errors. The following lists the exception types, and their documented data fields:

Prisma Client throws a PrismaClientKnownRequestError exception if the query engine returns a known error related to the request - for example, a unique constraint violation.

Prisma Client throws a PrismaClientUnknownRequestError exception if the query engine returns an error related to a request that does not have an error code.

Prisma Client throws a PrismaClientRustPanicError exception if the underlying engine crashes and exits with a non-zero exit code. In this case, Prisma Client or the whole Node process must be restarted.

Prisma Client throws a PrismaClientInitializationError exception if something goes wrong when the query engine is started and the connection to the database is created. This happens either:

Errors that can occur include:

Prisma Client throws a PrismaClientValidationError exception if validation fails - for example:

"Authentication failed against database server at {database_host}, the provided database credentials for {database_user} are not valid. Please make sure to provide valid database credentials for the database server at {database_host}."

"Can't reach database server at {database_host}:{database_port} Please make sure your database server is running at {database_host}:{database_port}."

"The database server at {database_host}:{database_port} was reached but timed out. Please try again. Please make sure your database server is running at {database_host}:{database_port}. "

"Database {database_file_name} does not exist at {database_file_path}"

"Database {database_name}.{database_schema_name} does not exist on the database server at {database_host}:{database_port}."

"Database {database_name} does not exist on the database server at {database_host}:{database_port}."

"Operations timed out after {time}

*[Content truncated - see full docs]*

---

## Generators (Reference) | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-schema/overview/generators

**Contents**:
- Generators
- prisma-client-js​
  - Field reference​
  - Binary targets​
    - The native binary target​
- prisma-client​
  - Getting started​
    - 1. Configure the prisma-client generator in schema.prisma​

A Prisma schema can have one or more generators, represented by the generator block:

A generator determines which assets are created when you run the prisma generate command.

There are two generators for Prisma Client:

Alternatively, you can configure any npm package that complies with our generator specification.

The prisma-client-js is the default generator for Prisma ORM 6.X versions and before. It requires the @prisma/client npm package and generates Prisma Client into node_modules.

The generator for Prisma's JavaScript Client accepts multiple additional properties:

As of v6.16.0, Prisma ORM can be used without Rust engines in production applications. Learn more here.

When enabled, your Prisma Client will be generated without a Rust-based query engine binary:

Note that driver adapters are required if you want to use Prisma ORM without Rust engines.

When using Prisma ORM without Rust, the binaryTargets field is obsolete and not needed.

You can read about the performance and DX improvements of this change on our blog.

The prisma-client-js generator uses several engines. Engines are implemented in Rust and are used by Prisma Client in the form of executable, platform-dependent engine files. Depending on which platform you are executing your code on, you need the correct file. "Binary targets" are used to define which files should be present for the target platform(s).

The correct file is particularly important when deploying your application to production, which often differs from your local development environment.

The native binary target is special. It doesn't map to a concrete operating system. Instead, when native is specified in binaryTargets, Prisma Client detects the current operating system and automatically specifies the correct binary target for it.

As an example, assume you're running macOS and you specify the following generator:

In that case, Prisma Client detects your operating system and finds the right binary file for it based on the

*[Content truncated - see full docs]*

**Examples**:

```prisma
generator client {  provider = "prisma-client"  output   = "../generated/prisma"}
```

```prisma
generator client {  provider        = "prisma-client-js"  previewFeatures = ["sample-preview-feature"]  binaryTargets   = ["debian-openssl-1.1.x"] // defaults to `"native"`}
```

```prisma
generator client {  provider   = "prisma-client-js" // or "prisma-client"  output     = "../src/generated/prisma"  engineType = "client"           // no Rust engine}
```

---

## Preview features (Reference) | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/reference/preview-features

**Contents**:
- Preview features

Some Prisma ORM features are released as Previews. Share your feedback on all Preview features on GitHub. For information about available preview features and how to enable them, see:

For information regarding upgrading Prisma ORM and enabling Preview features see Upgrading to use Preview features.

---

## Prisma CLI reference | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/reference/prisma-cli-reference

**Contents**:
- Prisma CLI reference
- Commands​
  - version (-v)​
    - Options​
    - Examples​
      - Output version information​
      - Output version information (-v)​
      - Output version information as JSON​

This document describes the Prisma CLI commands, arguments, and options.

The version command outputs information about your current prisma version, platform, and engine binaries.

The version command recognizes the following options to modify its behavior:

Bootstraps a fresh Prisma ORM project within the current directory.

The init command does not interpret any existing files. Instead, it creates a prisma directory containing a bare-bones schema.prisma file within your current directory.

By default, the project sets up a local Prisma Postgres instance but you can choose a different database using the --datasource-provider option.

Next, run the prisma dev command to interact with your local Prisma Postgres instance (e.g. to run migrations or execute queries).

Run prisma init --datasource-provider sqlite

The command output contains helpful information on how to use the generated files and begin using Prisma ORM with your project.

The command creates a new Prisma Postgres instance. Note that it requires you to be authenticated with the , If you run it for the first time without being authenticated, the command will open the browser for you to log into Console.

Run prisma init --prompt "Simple habit tracker application"

The command scaffolds a Prisma schema and deploys it to a fresh Prisma Postgres instance. Note that it requires you to be authenticated with the , If you run it for the first time without being authenticated, the command will open the browser for you to log into Console.

Run prisma init --preview-feature

An initial schema.prisma file to define your schema in:

A file to define environment variables for your project:

A file to specify what folders/files git should ignore in your project.

Run prisma init --url mysql://user:password@localhost:3306/mydb

The init command with the --url argument allows you to specify a custom datasource URL during Prisma initialization, instead of relying on a placeholder database URL:

A minimal schema.prisma 

*[Content truncated - see full docs]*

**Examples**:

```terminal
prisma version
```

```code
Environment variables loaded from .envprisma               : 2.21.0-dev.4@prisma/client       : 2.21.0-dev.4Current platform     : windowsQuery Engine         : query-engine 2fb8f444d9cdf7c0beee7b041194b42d7a9ce1e6 (at C:\Users\veroh\AppData\Roaming\npm\node_modules\@prisma\cli\query-engine-windows.exe)Migration Engine     : migration-engine-cli 2fb8f444d9cdf7c0beee7b041194b42d7a9ce1e6 (at C:\Users\veroh\AppData\Roaming\npm\node_modules\@prisma\cli\migration-engine-windows.exe)Format Binary     
...
```

```code
Environment variables loaded from .envprisma               : 2.21.0-dev.4@prisma/client       : 2.21.0-dev.4Current platform     : windowsQuery Engine         : query-engine 2fb8f444d9cdf7c0beee7b041194b42d7a9ce1e6 (at C:\Users\veroh\AppData\Roaming\npm\node_modules\@prisma\cli\query-engine-windows.exe)Migration Engine     : migration-engine-cli 2fb8f444d9cdf7c0beee7b041194b42d7a9ce1e6 (at C:\Users\veroh\AppData\Roaming\npm\node_modules\@prisma\cli\migration-engine-windows.exe)Format Binary     
...
```

---

## Prisma Client API | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/reference/prisma-client-reference

**Contents**:
- Prisma Client API reference
- PrismaClient​
  - Remarks​
  - datasources​
    - Properties​
    - Remarks​
    - Examples​
      - Programmatically override a datasource url​

If Prisma ORM's Rust engine binaries cause large bundle sizes, slow builds, or deployment issues (for example, in serverless or edge environments), you can use it without them using this configuration of your generator block:

Prisma ORM without Rust binaries has been Generally Available since v6.16.0.

Note that you need to use a driver adapter in this case.

When using this architecture:

This setup can simplify deployments in serverless or edge runtimes. Learn more in the docs here.

Curious why we moved away from the Rust engine? Take a look at why we transitioned from Rust binary engines to an all-TypeScript approach for a faster, lighter Prisma ORM in this blog post.

The Prisma Client API reference documentation is based on the following schema:

All example generated types (such as UserSelect and UserWhereUniqueInput) are based on the User model.

This section describes the PrismaClient constructor and its parameters.

Programmatically overrides properties of the datasource block in the schema.prisma file - for example, as part of an integration test. See also: Data sources

From version 5.2.0 and upwards, you can also use the datasourceUrl property to programmatically override the database connection string.

Based on the following datasource block:

Programmatically overrides the datasource block in the schema.prisma file.

Determines the type and level of logging. See also: Logging

The query event type:

Note that for MongoDB, the params and duration fields will be undefined.

All other log level event types:

Determines the level and formatting of errors returned by Prisma Client.

Defines an instance of a driver adapter. See also Database drivers .

This is available from version 5.4.0 and newer as a Preview feature behind the driverAdapters feature flag. It has been Generally Available since 6.16.0.

The example below uses the Neon driver adapter

Note: rejectOnNotFound was removed in v5.0.0.

Deprecated: rejectOnNotFound is deprecated in v4.0.0. From

*[Content truncated - see full docs]*

**Examples**:

```prisma
generator client {  provider   = "prisma-client-js" // or "prisma-client"  engineType = "client"}
```

```prisma
model User {  id           Int              @id @default(autoincrement())  name         String?  email        String           @unique  profileViews Int              @default(0)  role         Role             @default(USER)  coinflips    Boolean[]  posts        Post[]  city         String  country      String  profile      ExtendedProfile?  pets         Json}model ExtendedProfile {  id     Int     @id @default(autoincrement())  userId Int?    @unique  bio    String?  User   User?   @relation(fie
...
```

```ts
import { PrismaClient } from '@prisma/client';const prisma = new PrismaClient({  datasources: {    db: {      url: 'file:./dev_qa.db',    },  },});
```

---

## Prisma Schema API | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/reference/prisma-schema-reference

**Contents**:
- Prisma schema reference
- datasource​
  - Fields​
  - Remarks​
  - Examples​
    - Specify a PostgreSQL data source​
    - Specify a PostgreSQL data source via an environment variable​
    - Specify a MySQL data source​

Defines a data source in the Prisma schema.

A datasource block accepts the following fields:

The following providers are available:

In this example, the target database is available with the following credentials:

Learn more about PostgreSQL connection strings here.

In this example, the target database is available with the following credentials:

When running a Prisma CLI command that needs the database connection URL (e.g. prisma generate), you need to make sure that the DATABASE_URL environment variable is set.

One way to do so is by creating a .env file with the following contents. Note that the file must be in the same directory as your schema.prisma file to automatically picked up the Prisma CLI.

In this example, the target database is available with the following credentials:

Learn more about MySQL connection strings here.

Learn more about MongoDB connection strings here.

In this example, the target database is located in a file called dev.db:

Learn more about SQLite connection strings here.

In this example, the target database is available with the following credentials:

The format for connection strings is the same as for PostgreSQL. Learn more about PostgreSQL connection strings here.

Defines a generator in the Prisma schema.

This is the default generator for Prisma ORM 6.x and earlier versions. Learn more about generators.

A generator block accepts the following fields:

We recommend defining a custom output path, adding the path to .gitignore, and then making sure to run prisma generate via a custom build script or postinstall hook.

The ESM-first client generator that offers greater control and flexibility across different JavaScript environments. It generates plain TypeScript code into a custom directory, providing full visibility over the generated code. Learn more about the new prisma-client generator.

The prisma-client generator will be the default generator in Prisma ORM 7.0 and we recommend migrating to it as soon as possible. It 

*[Content truncated - see full docs]*

**Examples**:

```prisma
datasource db {  provider = "postgresql"  url      = "postgresql://johndoe:mypassword@localhost:5432/mydb?schema=public"}
```

```prisma
datasource db {  provider = "postgresql"  url      = env("DATABASE_URL")}
```

```text
DATABASE_URL=postgresql://johndoe:mypassword@localhost:5432/mydb?schema=public
```

---

## Prisma Schema Overview | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-schema/overview

**Contents**:
- Overview on Prisma Schema
- Example​
- Syntax​
  - VS Code​
  - GitHub​
- Accessing environment variables from the schema​
- Comments​
- Auto formatting​

The Prisma Schema (or schema for short) is the main method of configuration for your Prisma ORM setup. It consists of the following parts:

It is typically a single file called schema.prisma (or multiple files with .prisma file extension) that is stored in a defined but customizable location. You can also organize your Prisma schema in multiple files if you prefer that.

See the Prisma schema API reference for detailed information about each section of the schema.

Whenever a prisma command is invoked, the CLI typically reads some information from the schema, e.g.:

You can also use environment variables inside the schema to provide configuration options when a CLI command is invoked.

The following is an example of a Prisma Schema that specifies:

Prisma Schema files are written in Prisma Schema Language (PSL). See the data sources, generators, data model definition and of course Prisma Schema API reference pages for details and examples.

Syntax highlighting for PSL is available via a VS Code extension (which also lets you auto-format the contents of your Prisma schema and indicates syntax errors with red squiggly lines). Learn more about setting up Prisma ORM in your editor.

PSL code snippets on GitHub can be rendered with syntax highlighting as well by using the .prisma file extension or annotating fenced code blocks in Markdown with prisma:

You can use environment variables to provide configuration options when a CLI command is invoked, or a Prisma Client query is run.

Hardcoding URLs directly in your schema is possible but is discouraged because it poses a security risk. Using environment variables in the schema allows you to keep secrets out of the schema which in turn improves the portability of the schema by allowing you to use it in different environments.

Environment variables can be accessed using the env() function:

You can use the env() function in the following places:

See Environment variables for more information about how to use an .env file 

*[Content truncated - see full docs]*

**Examples**:

```prisma
datasource db {  provider = "postgresql"  url      = env("DATABASE_URL")}generator client {  provider = "prisma-client-js"}model User {  id        Int      @id @default(autoincrement())  createdAt DateTime @default(now())  email     String   @unique  name      String?  role      Role     @default(USER)  posts     Post[]}model Post {  id        Int      @id @default(autoincrement())  createdAt DateTime @default(now())  updatedAt DateTime @updatedAt  published Boolean  @default(false)  title     S
...
```

```prisma
datasource db {  provider = "mongodb"  url      = env("DATABASE_URL")}generator client {  provider = "prisma-client-js"}model User {  id        String   @id @default(auto()) @map("_id") @db.ObjectId  createdAt DateTime @default(now())  email     String   @unique  name      String?  role      Role     @default(USER)  posts     Post[]}model Post {  id        String   @id @default(auto()) @map("_id") @db.ObjectId  createdAt DateTime @default(now())  updatedAt DateTime @updatedAt  published Boolean 
...
```

```text
```prismamodel User {  id        Int      @id @default(autoincrement())  createdAt DateTime @default(now())  email     String   @unique  name      String?}```
```

---

## Reference | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/reference

**Contents**:
- Reference
- In this section​
- Prisma Client API
- Prisma Schema
- Prisma CLI
- Errors
- Environment variables
- Prisma Config

The reference section of the documentation is a collection of reference pages that describe the Prisma ORM APIs and database implementations.

If Prisma ORM's Rust engine binaries cause large bundle sizes, slow builds, or deployment issues (for example, in serverless or edge environments), you can use it without them using this configuration of your generator block:

This document describes the Prisma CLI commands, arguments, and options.

For more information about how to work with exceptions and error codes, see Handling exceptions and errors.

This document describes different environment variables and their use cases.

This page gives an overview of the features which are provided by the databases that Prisma ORM supports. Additionally, it explains how each of these features can be used in Prisma ORM with pointers to further documentation.

Prisma ORM currently supports the following databases.

Prisma ORM needs a connection URL to be able to connect to your database, e.g. when sending queries with Prisma Client or when changing the database schema with Prisma Migrate.

This page provides an overview of the system requirements for Prisma ORM.

---

## System requirements (Reference) | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/reference/system-requirements

**Contents**:
- System requirements
- System requirements​
  - Software requirements​
  - Prisma ORM v5​
  - Operating systems​
    - Linux runtime dependencies​
    - Windows runtime dependencies​
    - macOS runtime dependencies​

This page provides an overview of the system requirements for Prisma ORM.

This section lists the software that Prisma ORM requires and the supported operating systems, along with runtime dependency requirements for specific operating systems.

The latest version of Prisma ORM requires the following software:

See also: Supported database versions

Prisma ORM v5 requires the following software:

Prisma ORM is supported on macOS, Windows and most Linux distributions.

Prisma ORM requires the following system libraries to be installed to work:

The following two tables show the supported Linux distro families, OpenSSL versions and C standard libraries for each CPU architecture.

On AMD64 (x86_64) architecture:

On ARM64 (aarch64) architecture:

When Prisma ORM can not resolve the OpenSSL version on a system (e.g. because it is not installed), it will default to OpenSSL 1.1.x.

Systems that can run the supported Node.js versions will most likely have zlib and libgcc available. One notable exception is Google's Distroless images, where libz.so.1 needs to be copied from a compatible Debian system.

On Windows Microsoft Visual C++ Redistributable 2015 or newer must be installed (which is by default the case on most modern installations).

Prisma ORM supports macOS 10.15 or newer. There are no additional platform-specific requirements on macOS other than what is listed for all platforms in the Software requirements section.

There are some common problems caused by using outdated versions of the system requirements:

You see the following error when you try type-checking a project after you run prisma generate.

Upgrade the TypeScript dependency in your project to a version supported by Prisma ORM. npm install -D typescript.

You see the following console error when you attempt to run an app that uses the groupBy preview feature:

Upgrade the TypeScript dependency in your project to a version supported by Prisma ORM. npm install -D typescript.

**Examples**:

```terminal
./node_modules/.prisma/client/index.d.ts:10:33Type error: Type expected.   8 | export type PrismaPromise<A> = Promise<A> & {[prisma]: true}   9 | type UnwrapTuple<Tuple extends readonly unknown[]> = {> 10 |   [K in keyof Tuple]: K extends `${number}` ? Tuple[K] extends PrismaPromise<infer X> ? X : never : never     |                                 ^  11 | };  12 |  13 |
```

```terminal
server.ts:6:25 - error TS2615: Type of property 'OR' circularly references itself in mapped type '{ [K in keyof { AND?: Enumerable<ProductScalarWhereWithAggregatesInput>; OR?: Enumerable<ProductScalarWhereWithAggregatesInput>; ... 4 more ...; category?: string | StringWithAggregatesFilter; }]: Or<...> extends 1 ? { ...; }[K] extends infer TK ? GetHavingFields<...> : never : {} extends FieldPaths<...> ? never : K...'.6   const grouped = await prisma.product.groupBy({                          ~~~~
...
```

---

## What is introspection? (Reference) | Prisma Documentation

**URL**: https://www.prisma.io/docs/orm/prisma-schema/introspection

**Contents**:
- What is introspection?
- What does introspection do?​
- The prisma db pull command​
- Introspection workflow​
- Rules and conventions​
  - Model, field and enum names​
    - Sanitization of invalid characters​
    - Duplicate Identifiers after Sanitization​

You can introspect your database using the Prisma CLI in order to generate the data model in your Prisma schema. The data model is needed to generate Prisma Client.

Introspection is often used to generate an initial version of the data model when adding Prisma ORM to an existing project.

However, it can also be used repeatedly in an application. This is most commonly the case when you're not using Prisma Migrate but perform schema migrations using plain SQL or another migration tool. In that case, you also need to re-introspect your database and subsequently re-generate Prisma Client to reflect the schema changes in your Prisma Client API.

Introspection has one main function: Populate your Prisma schema with a data model that reflects the current database schema.

Here's an overview of its main functions on SQL databases:

On MongoDB, the main functions are the following:

You can learn more about how Prisma ORM maps types from the database to the types available in the Prisma schema on the respective docs page for the data source connector:

You can introspect your database using the prisma db pull command of the Prisma CLI. Note that using this command requires your connection URL to be set in your Prisma schema datasource.

Here's a high-level overview of the steps that prisma db pull performs internally:

The typical workflow for projects that are not using Prisma Migrate, but instead use plain SQL or another migration tool looks as follows:

Note that as you evolve the application, this process can be repeated for an indefinite number of times.

Prisma ORM employs a number of conventions for translating a database schema into a data model in the Prisma schema:

Field, model and enum names (identifiers) must start with a letter and generally must only contain underscores, letters and digits. You can find the naming rules and conventions for each of these identifiers on the respective docs page:

The general rule for identifiers is that they need to adhere to 

*[Content truncated - see full docs]*

**Examples**:

```text
[A-Za-z][A-Za-z0-9_]*
```

```sql
CREATE TABLE "42User" (  _id SERIAL PRIMARY KEY,  _name VARCHAR(255),  two$two INTEGER);
```

```prisma
model User {  id      Int     @id @default(autoincrement()) @map("_id")  name    String? @map("_name")  two_two Int?    @map("two$two")  @@map("42User")}
```

---
