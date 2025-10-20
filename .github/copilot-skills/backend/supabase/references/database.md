# Supabase - Database

**Pages**: 39

---

## AI & Vectors | Supabase Docs

**URL**: https://supabase.com/docs/guides/ai

**Contents**:
- AI & Vectors
- The best vector database is the database you already have.
- Search#
- Examples#
- Integrations#
- Case studies#

The best vector database is the database you already have.

Supabase provides an open source toolkit for developing AI applications using Postgres and pgvector. Use the Supabase client libraries to store, index, and query your vector embeddings at scale.

The toolkit includes:

You can use Supabase to build different types of search features for your app, including:

Check out all of the AI templates and examples in our GitHub repository.

Headless Vector Search

Image Search with OpenAI CLIP

Hugging Face inference

Building ChatGPT Plugins

Vector search with Next.js and OpenAI

Berri AI Boosts Productivity by Migrating from AWS RDS to Supabase with pgvector

Firecrawl switches from Pinecone to Supabase for PostgreSQL vector embeddings

Markprompt: GDPR-Compliant AI Chatbots for Docs and Websites

Latest product updates?

Something's not right?

---

## Cascade Deletes | Supabase Docs

**URL**: https://supabase.com/docs/guides/database/postgres/cascade-deletes

**Contents**:
- Cascade Deletes
- RESTRICT vs NO ACTION#
- Example#
  - RESTRICT#
  - NO ACTION#
  - NO ACTION INITIALLY DEFERRED#
  - Is this helpful?

There are 5 options for foreign key constraint deletes:

These options can be specified when defining a foreign key constraint using the "ON DELETE" clause. For example, the following SQL statement creates a foreign key constraint with the CASCADE option:

This means that when a row is deleted from the parent_table, all related rows in the child_table will be deleted as well.

The difference between NO ACTION and RESTRICT is subtle and can be a bit confusing.

Both NO ACTION and RESTRICT are used to prevent deletion of a row in a parent table if there are related rows in a child table. However, there is a subtle difference in how they behave.

When a foreign key constraint is defined with the option RESTRICT, it means that if a row in the parent table is deleted, the database will immediately raise an error and prevent the deletion of the row in the parent table. The database will not delete, update or set to NULL any rows in the referenced tables.

When a foreign key constraint is defined with the option NO ACTION, it means that if a row in the parent table is deleted, the database will also raise an error and prevent the deletion of the row in the parent table. However unlike RESTRICT, NO ACTION has the option to defer the check using INITIALLY DEFERRED. This will only raise the above error if the referenced rows still exist at the end of the transaction.

The difference from RESTRICT is that a constraint marked as NO ACTION INITIALLY DEFERRED is deferred until the end of the transaction, rather than running immediately. If, for example there is another foreign key constraint between the same tables marked as CASCADE, the cascade will occur first and delete the referenced rows, and no error will be thrown by the deferred constraint. Otherwise if there are still rows referencing the parent row by the end of the transaction, an error will be raised just like before. Just like RESTRICT, the database will not delete, update or set to NULL any rows in the referenced ta

*[Content truncated - see full docs]*

**Examples**:

```text
123alter table child_tableadd constraint fk_parent foreign key (parent_id) references parent_table (id)  on delete cascade;
```

```text
123456789101112131415161718192021222324252627282930313233343536373839create table grandparent (  id serial primary key,  name text);create table parent (  id serial primary key,  name text,  parent_id integer references grandparent (id)    on delete cascade);create table child (  id serial primary key,  name text,  father integer references parent (id)    on delete restrict);insert into grandparent  (id, name)values  (1, 'Elizabeth');insert into parent  (id, name, parent_id)values  (1, 'Charles'
...
```

```text
123postgres=# delete from grandparent;ERROR: update or delete on table "parent" violates foreign key constraint "child_father_fkey" on table "child"DETAIL: Key (id)=(1) is still referenced from table "child".
```

---

## Cron | Supabase Docs

**URL**: https://supabase.com/docs/guides/cron

**Contents**:
- Cron
- Schedule Recurring Jobs with Cron Syntax in Postgres
- How does Cron work?#
- Resources#
  - Is this helpful?

Schedule Recurring Jobs with Cron Syntax in Postgres

Supabase Cron is a Postgres Module that simplifies scheduling recurring Jobs with cron syntax and monitoring Job runs inside Postgres.

Cron Jobs can be created via SQL or the Integrations -> Cron interface inside the Dashboard, and can run anywhere from every second to once a year depending on your use case.

Every Job can run SQL snippets or database functions with zero network latency or make an HTTP request, such as invoking a Supabase Edge Function, with ease.

For best performance, we recommend no more than 8 Jobs run concurrently. Each Job should run no more than 10 minutes.

Under the hood, Supabase Cron uses the pg_cron Postgres database extension which is the scheduling and execution engine for your Jobs.

The extension creates a cron schema in your database and all Jobs are stored on the cron.job table. Every Job's run and its status is recorded on the cron.job_run_details table.

The Supabase Dashboard provides an interface for you to schedule Jobs and monitor Job runs. You can also do the same with SQL.

Latest product updates?

Something's not right?

---

## Database | Supabase Docs

**URL**: https://supabase.com/docs/guides/database/overview

**Contents**:
- Database
- Features#
  - Table view#
  - Relationships#
  - Clone tables#
  - The SQL editor#
  - Additional features#
  - Extensions#

Every Supabase project comes with a full Postgres database, a free and open source database which is considered one of the world's most stable and advanced databases.

You don't have to be a database expert to start using Supabase. Our table view makes Postgres as easy to use as a spreadsheet.

Dig into the relationships within your data.

You can duplicate your tables, just like you would inside a spreadsheet.

Supabase comes with a SQL Editor. You can also save your favorite queries to run later!

Database backups do not include objects stored via the Storage API, as the database only includes metadata about these objects. Restoring an old backup does not restore objects that have been deleted since then.

To expand the functionality of your Postgres database, you can use extensions. You can enable Postgres extensions with the click of a button within the Supabase dashboard.

Learn more about all the extensions provided on Supabase.

PostgreSQL the database was derived from the POSTGRES Project, a package written at the University of California at Berkeley in 1986. This package included a query language called "PostQUEL".

In 1994, Postgres95 was built on top of POSTGRES code, adding an SQL language interpreter as a replacement for PostQUEL.

Eventually, Postgres95 was renamed to PostgreSQL to reflect the SQL query capability. After this, many people referred to it as Postgres since it's less prone to confusion. Supabase is all about simplicity, so we also refer to it as Postgres.

Read about resetting your database password here and changing the timezone of your server here.

Latest product updates?

Something's not right?

---

## Database configuration | Supabase Docs

**URL**: https://supabase.com/docs/guides/database/managing-timezones

**Contents**:
- Database configuration
- Updating the default configuration for your Postgres database.
- Timeouts#
- Statement optimization#
- Managing timezones#
  - Change timezone#
  - Full list of timezones#
  - Search for a specific timezone#

Database configuration

Updating the default configuration for your Postgres database.

Postgres provides a set of sensible defaults for you database size. In some cases, these defaults can be updated. We do not recommend changing these defaults unless you know what you're doing.

See the Timeouts section.

All Supabase projects come with the pg_stat_statements extension installed, which tracks planning and execution statistics for all statements executed against it. These statistics can be used in order to diagnose the performance of your project.

This data can further be used in conjunction with the explain functionality of Postgres to optimize your usage.

Every hosted Supabase database is set to UTC timezone by default. We strongly recommend keeping it this way, even if your users are in a different location. This is because it makes it much easier to calculate differences between timezones if you adopt the mental model that everything in your database is in UTC time.

On self-hosted databases, the timezone defaults to your local timezone. We recommend changing this to UTC for the same reasons.

Get a full list of timezones supported by your database. This will return the following columns:

Use ilike (case insensitive search) to find specific timezones.

Latest product updates?

Something's not right?

**Examples**:

```text
12alter database postgresset timezone to 'America/New_York';
```

```text
123select name, abbrev, utc_offset, is_dstfrom pg_timezone_names()order by name;
```

```text
123select *from pg_timezone_names()where name ilike '%york%';
```

---

## Drop all tables in a PostgreSQL schema | Supabase Docs

**URL**: https://supabase.com/docs/guides/database/postgres/dropping-all-tables-in-schema

**Contents**:
- Drop all tables in a PostgreSQL schema
  - Is this helpful?

Drop all tables in a PostgreSQL schema

Execute the following query to drop all tables in a given schema. Replace my-schema-name with the name of your schema. In Supabase, the default schema is public.

This deletes all tables and their associated data. Ensure you have a recent backup before proceeding.

This query works by listing out all the tables in the given schema and then executing a drop table for each (hence the for... loop).

You can run this query using the SQL Editor in the Supabase Dashboard, or via psql if you're connecting directly to the database.

Latest product updates?

Something's not right?

**Examples**:

```text
1234567do $$ declare    r record;begin    for r in (select tablename from pg_tables where schemaname = 'my-schema-name') loop        execute 'drop table if exists ' || quote_ident(r.tablename) || ' cascade';    end loop;end $$;
```

---

## Import data into Supabase | Supabase Docs

**URL**: https://supabase.com/docs/guides/database/import-data

**Contents**:
- Import data into Supabase
- How to import data into Supabase#
  - Option 1: CSV import via Supabase dashboard#
  - Option 2: Bulk import using pgloader#
  - Option 3: Using Postgres copy command#
  - Option 4: Using the Supabase API#
- Preparing to import data#
  - 1. Back up your data#

Import data into Supabase

You can import data into Supabase in multiple ways. The best method depends on your data size and app requirements.

If you're working with small datasets in development, you can experiment quickly using CSV import in the Supabase dashboard. If you're working with a large dataset in production, you should plan your data import to minimize app latency and ensure data integrity.

You have multiple options for importing your data into Supabase:

If you're importing a large dataset or importing data into production, plan ahead and prepare your database.

Supabase dashboard provides a user-friendly way to import data. However, for very large datasets, this method may not be the most efficient choice, given the size limit is 100MB. It's generally better suited for smaller datasets and quick data imports. Consider using alternative methods like pgloader for large-scale data imports.

pgloader is a powerful tool for efficiently importing data into a Postgres database that supports a wide range of source database engines, including MySQL and MS SQL.

You can use it in conjunction with Supabase by following these steps:

Install pgloader on your local machine or a server. For more info, you can refer to the official pgloader installation page.

Create a configuration file that specifies the source data and the target Supabase database (e.g., config.load). Here's an example configuration file:

Customize the source and Supabase database URL and options to fit your specific use case:

Run pgloader with the configuration file.

For databases using the Postgres engine, we recommend using the pg_dump and psql command line tools.

Read more about Bulk data loading.

The Supabase API allows you to programmatically import data into your tables. You can use various client libraries to interact with the API and perform data import operations. This approach is useful when you need to automate data imports, and it gives you fine-grained control over the process

*[Content truncated - see full docs]*

**Examples**:

```text
1$ apt-get install pgloader
```

```text
12345LOAD DATABASE    FROM sourcedb://USER:PASSWORD@HOST/SOURCE_DB    INTO postgres://postgres.xxxx:password@xxxx.pooler.supabase.com:6543/postgresALTER SCHEMA 'public' OWNER TO 'postgres';set wal_buffers = '64MB', max_wal_senders = 0, statement_timeout = 0, work_mem to '2GB';
```

```text
1pgloader config.load
```

---

## Integrating with Supabase Database (Postgres) | Supabase Docs

**URL**: https://supabase.com/docs/guides/functions/connect-to-postgres

**Contents**:
- Integrating with Supabase Database (Postgres)
- Connect to your Postgres database from Edge Functions.
- Using supabase-js#
- Using a Postgres client#
- Using Drizzle#
- SSL connections#
  - Production#
  - Local development#

Integrating with Supabase Database (Postgres)

Connect to your Postgres database from Edge Functions.

Connect to your Postgres database from an Edge Function by using the supabase-js client. You can also use other Postgres clients like Deno Postgres

The supabase-js client handles authorization with Row Level Security and automatically formats responses as JSON. This is the recommended approach for most applications:

Because Edge Functions are a server-side technology, it's safe to connect directly to your database using any popular Postgres client. This means you can run raw SQL from your Edge Functions.

Here is how you can connect to the database using Deno Postgres driver and run raw SQL. Check out the full example.

You can use Drizzle together with Postgres.js. Both can be loaded directly from npm:

Set up dependencies in import_map.json:

Use in your function:

You can find the full example on GitHub.

Deployed edge functions are pre-configured to use SSL for connections to the Supabase database. You don't need to add any extra configurations.

If you want to use SSL connections during local development, follow these steps:

Then, restart your local development server:

Latest product updates?

Something's not right?

**Examples**:

```python
123456789101112131415161718192021222324import { createClient } from 'npm:@supabase/supabase-js@2'Deno.serve(async (req) => {  try {    const supabase = createClient(      Deno.env.get('SUPABASE_URL') ?? '',      Deno.env.get('SUPABASE_PUBLISHABLE_KEY') ?? '',      { global: { headers: { Authorization: req.headers.get('Authorization')! } } }    )    const { data, error } = await supabase.from('countries').select('*')    if (error) {      throw error    }    return new Response(JSON.stringify({ da
...
```

```python
123456789101112131415161718192021222324252627282930313233343536373839404142434445464748import { Pool } from 'https://deno.land/x/postgres@v0.17.0/mod.ts'// Create a database pool with one connection.const pool = new Pool(  {    tls: { enabled: false },    database: 'postgres',    hostname: Deno.env.get('DB_HOSTNAME'),    user: Deno.env.get('DB_USER'),    port: 6543,    password: Deno.env.get('DB_PASSWORD'),  },  1)Deno.serve(async (_req) => {  try {    // Grab a connection from the pool    const
...
```

```text
1234567{  "imports": {    "drizzle-orm": "npm:drizzle-orm@0.29.1",    "drizzle-orm/": "npm:/drizzle-orm@0.29.1/",    "postgres": "npm:postgres@3.4.3"  }}
```

---

## LangChain | Supabase Docs

**URL**: https://supabase.com/docs/guides/ai/langchain

**Contents**:
- LangChain
- Initializing your database#
- Usage#
  - Simple metadata filtering#
  - Advanced metadata filtering#
- Hybrid search#
- Resources#
  - Is this helpful?

LangChain is a popular framework for working with AI, Vectors, and embeddings. LangChain supports using Supabase as a vector store, using the pgvector extension.

Prepare you database with the relevant tables:

You can now search your documents using any Node.js application. This is intended to be run on a secure server route.

Given the above match_documents Postgres function, you can also pass a filter parameter to only return documents with a specific metadata field value. This filter parameter is a JSON object, and the match_documents function will use the Postgres JSONB Containment operator @> to filter documents by the metadata field values you specify. See details on the Postgres JSONB Containment operator for more information.

You can also use query builder-style filtering (similar to how the Supabase JavaScript library works) instead of passing an object. Note that since the filter properties will be in the metadata column, you need to use arrow operators (-> for integer or ->> for text) as defined in PostgREST API documentation and specify the data type of the property (e.g. the column should look something like metadata->some_int_value::int).

LangChain supports the concept of a hybrid search, which combines Similarity Search with Full Text Search. Read the official docs to get started: Supabase Hybrid Search.

You can install the LangChain Hybrid Search function though our database.dev package manager.

Latest product updates?

Something's not right?

**Examples**:

```python
12345678910111213141516171819202122232425262728import { SupabaseVectorStore } from '@langchain/community/vectorstores/supabase'import { OpenAIEmbeddings } from '@langchain/openai'import { createClient } from '@supabase/supabase-js'const supabaseKey = process.env.SUPABASE_SERVICE_ROLE_KEYif (!supabaseKey) throw new Error(`Expected SUPABASE_SERVICE_ROLE_KEY`)const url = process.env.SUPABASE_URLif (!url) throw new Error(`Expected env var SUPABASE_URL`)export const run = async () => {  const client 
...
```

```python
1234567891011121314151617181920212223242526272829303132import { SupabaseVectorStore } from '@langchain/community/vectorstores/supabase'import { OpenAIEmbeddings } from '@langchain/openai'import { createClient } from '@supabase/supabase-js'// First, follow set-up instructions aboveconst privateKey = process.env.SUPABASE_SERVICE_ROLE_KEYif (!privateKey) throw new Error(`Expected env var SUPABASE_SERVICE_ROLE_KEY`)const url = process.env.SUPABASE_URLif (!url) throw new Error(`Expected env var SUPAB
...
```

```python
1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859606162import { SupabaseFilterRPCCall, SupabaseVectorStore } from '@langchain/community/vectorstores/supabase'import { OpenAIEmbeddings } from '@langchain/openai'import { createClient } from '@supabase/supabase-js'// First, follow set-up instructions aboveconst privateKey = process.env.SUPABASE_SERVICE_ROLE_KEYif (!privateKey) throw new Error(`Expected env var SUPABASE_SERVICE_ROLE_KEY`)co
...
```

---

## Learn how to integrate Supabase with LlamaIndex, a data framework for your LLM applications. | Supabase Docs

**URL**: https://supabase.com/docs/guides/ai/integrations/llamaindex

**Contents**:
- Learn how to integrate Supabase with LlamaIndex, a data framework for your LLM applications.
- Learn how to integrate Supabase with LlamaIndex, a data framework for your LLM applications.
- Project setup#
- Launching a notebook#
- Fill in your OpenAI credentials#
- Connecting to your database#
- Stepping through the notebook#
- Resources#

Learn how to integrate Supabase with LlamaIndex, a data framework for your LLM applications.

Learn how to integrate Supabase with LlamaIndex, a data framework for your LLM applications.

This guide will walk you through a basic example using the LlamaIndex SupabaseVectorStore.

Let's create a new Postgres database. This is as simple as starting a new Project in Supabase:

Your database will be available in less than a minute.

Finding your credentials:

You can find your project credentials on the dashboard:

Launch our LlamaIndex notebook in Colab:

At the top of the notebook, you'll see a button Copy to Drive. Click this button to copy the notebook to your Google Drive.

Inside the Notebook, add your OPENAI_API_KEY key. Find the cell which contains this code:

Inside the Notebook, find the cell which specifies the DB_CONNECTION. It will contain some code like this:

Replace the DB_CONNECTION with your own connection string. You can find the connection string on your project dashboard by clicking Connect.

SQLAlchemy requires the connection string to start with postgresql:// (instead of postgres://). Don't forget to rename this after copying the string from the dashboard.

You must use the "connection pooling" string (domain ending in *.pooler.supabase.com) with Google Colab since Colab does not support IPv6.

Now all that's left is to step through the notebook. You can do this by clicking the "execute" button (ctrl+enter) at the top left of each code cell. The notebook guides you through the process of creating a collection, adding data to it, and querying it.

You can view the inserted items in the Table Editor, by selecting the vecs schema from the schema dropdown.

Latest product updates?

Something's not right?

**Examples**:

```text
12import osos.environ['OPENAI_API_KEY'] = "[your_openai_api_key]"
```

```text
1234DB_CONNECTION = "postgresql://<user>:<password>@<host>:<port>/<db_name>"# create vector store clientvx = vecs.create_client(DB_CONNECTION)
```

---

## Managing Indexes in PostgreSQL | Supabase Docs

**URL**: https://supabase.com/docs/guides/database/postgres/indexes

**Contents**:
- Managing Indexes in PostgreSQL
- Create an index#
- Partial indexes#
- Ordering indexes#
- Reindexing#
- Index Advisor#
  - Understanding Index Advisor results#
  - Is this helpful?

Managing Indexes in PostgreSQL

An index makes your Postgres queries faster. The index is like a "table of contents" for your data - a reference list which allows queries to quickly locate a row in a given table without needing to scan the entire table (which in large tables can take a long time).

Indexes can be structured in a few different ways. The type of index chosen depends on the values you are indexing. By far the most common index type, and the default in Postgres, is the B-Tree. A B-Tree is the generalized form of a binary search tree, where nodes can have more than two children.

Even though indexes improve query performance, the Postgres query planner may not always make use of a given index when choosing which optimizations to make. Additionally indexes come with some overhead - additional writes and increased storage - so it's useful to understand how and when to use indexes, if at all.

Let's take an example table:

All the queries in this guide can be run using the SQL Editor in the Supabase Dashboard, or via psql if you're connecting directly to the database.

We might want to frequently query users based on their age:

Without an index, Postgres will scan every row in the table to find equality matches on age.

You can verify this by doing an explain on the query:

To add a simple B-Tree index you can run:

It can take a long time to build indexes on large datasets and the default behaviour of create index is to lock the table from writes.

Luckily Postgres provides us with create index concurrently which prevents blocking writes on the table, but does take a bit longer to build.

Here is a simplified diagram of the index we just created (note that in practice, nodes actually have more than two children).

You can see that in any large data set, traversing the index to locate a given value can be done in much less operations (O(log n)) than compared to scanning the table one value at a time from top to bottom (O(n)).

If you are frequently queryin

*[Content truncated - see full docs]*

**Examples**:

```text
12345678create table persons (  id bigint generated by default as identity primary key,  age int,  height int,  weight int,  name text,  deceased boolean);
```

```text
1select name from persons where age = 32;
```

```text
1explain select name from persons where age = 32;
```

---

## Migrate from Amazon RDS to Supabase | Supabase Docs

**URL**: https://supabase.com/docs/guides/platform/migrating-to-supabase/amazon-rds

**Contents**:
- Migrate from Amazon RDS to Supabase
- Migrate your Amazon RDS MySQL or MS SQL database to Supabase.
- Retrieve your Amazon RDS database credentials #
- Retrieve your Supabase host #
- Migrate the database#
- Enterprise#
  - Is this helpful?

Migrate from Amazon RDS to Supabase

Migrate your Amazon RDS MySQL or MS SQL database to Supabase.

This guide aims to exhibit the process of transferring your Amazon RDS database from any of these engines Postgres, MySQL or MS SQL to Supabase's Postgres database. Although Amazon RDS is a favored managed database service provided by AWS, it may not suffice for all use cases. Supabase, on the other hand, provides an excellent free and open source option that encompasses all the necessary backend features to develop a product: a Postgres database, authentication, instant APIs, edge functions, real-time subscriptions, and storage.

Supabase's core is Postgres, enabling the use of row-level security and providing access to over 40 Postgres extensions. By migrating from Amazon RDS to Supabase, you can leverage Postgres to its fullest potential and acquire all the features you need to complete your project.

The fastest way to migrate your database is with the Supabase migration tool on Google Colab.

Alternatively, you can use pgloader, a flexible and powerful data migration tool that supports a wide range of source database engines, including MySQL and MS SQL, and migrates the data to a Postgres database. For databases using the Postgres engine, we recommend using the pg_dump and psql command line tools, which are included in a full Postgres installation.

If you're planning to migrate a database larger than 6 GB, we recommend upgrading to at least a Large compute add-on. This will ensure you have the necessary resources to handle the migration efficiently.

We strongly advise you to pre-provision the disk space you will need for your migration. On paid projects, you can do this by navigating to the Compute and Disk Settings page. For more information on disk scaling and disk limits, check out our disk settings documentation.

Contact us if you need more help migrating your project.

Latest product updates?

Something's not right?

---

## Migrate from Amazon RDS to Supabase | Supabase Docs

**URL**: https://supabase.com/docs/guides/resources/migrating-to-supabase/amazon-rds

**Contents**:
- Migrate from Amazon RDS to Supabase
- Migrate your Amazon RDS MySQL or MS SQL database to Supabase.
- Retrieve your Amazon RDS database credentials #
- Retrieve your Supabase host #
- Migrate the database#
- Enterprise#
  - Is this helpful?

Migrate from Amazon RDS to Supabase

Migrate your Amazon RDS MySQL or MS SQL database to Supabase.

This guide aims to exhibit the process of transferring your Amazon RDS database from any of these engines Postgres, MySQL or MS SQL to Supabase's Postgres database. Although Amazon RDS is a favored managed database service provided by AWS, it may not suffice for all use cases. Supabase, on the other hand, provides an excellent free and open source option that encompasses all the necessary backend features to develop a product: a Postgres database, authentication, instant APIs, edge functions, real-time subscriptions, and storage.

Supabase's core is Postgres, enabling the use of row-level security and providing access to over 40 Postgres extensions. By migrating from Amazon RDS to Supabase, you can leverage Postgres to its fullest potential and acquire all the features you need to complete your project.

The fastest way to migrate your database is with the Supabase migration tool on Google Colab.

Alternatively, you can use pgloader, a flexible and powerful data migration tool that supports a wide range of source database engines, including MySQL and MS SQL, and migrates the data to a Postgres database. For databases using the Postgres engine, we recommend using the pg_dump and psql command line tools, which are included in a full Postgres installation.

If you're planning to migrate a database larger than 6 GB, we recommend upgrading to at least a Large compute add-on. This will ensure you have the necessary resources to handle the migration efficiently.

We strongly advise you to pre-provision the disk space you will need for your migration. On paid projects, you can do this by navigating to the Compute and Disk Settings page. For more information on disk scaling and disk limits, check out our disk settings documentation.

Contact us if you need more help migrating your project.

Latest product updates?

Something's not right?

---

## Migrate from Firebase Firestore to Supabase | Supabase Docs

**URL**: https://supabase.com/docs/guides/platform/migrating-to-supabase/firestore-data

**Contents**:
- Migrate from Firebase Firestore to Supabase
- Migrate your Firebase Firestore database to a Supabase Postgres database.
- Set up the migration tool #
- Generate a Firebase private key #
- Command line options#
  - List all Firestore collections#
  - Dump Firestore collection to JSON file#
    - Customize the JSON file with hooks#

Migrate from Firebase Firestore to Supabase

Migrate your Firebase Firestore database to a Supabase Postgres database.

Supabase provides several tools to convert data from a Firebase Firestore database to a Supabase Postgres database. The process copies the entire contents of a single Firestore collection to a single Postgres table.

The Firestore collection is "flattened" and converted to a table with basic columns of one of the following types: text, numeric, boolean, or jsonb. If your structure is more complex, you can write a program to split the newly-created json file into multiple, related tables before you import your json file(s) to Supabase.

Clone the firebase-to-supabase repository:

In the /firestore directory, create a file named supabase-service.json with the following contents:

On your project dashboard, click Connect

Under the Session pooler, click on the View parameters under the connect string. Replace the Host and User fields with the values shown.

Enter the password you used when you created your Supabase project in the password entry in the supabase-service.json file.

node firestore2json.js <collectionName> [<batchSize>] [<limit>]

You can customize the way your JSON file is written using a custom hook. A common use for this is to "flatten" the JSON file, or to split nested data into separate, related database tables. For example, you could take a Firestore document that looks like this:

And split it into two files (one table for users and one table for items):

node json2supabase.js <path_to_json_file> [<primary_key_strategy>] [<primary_key_name>]

Hooks are used to customize the process of exporting a collection of Firestore documents to JSON. They can be used for:

If your Firestore collection is called users, create a file called users.js in the current folder.

The basic format of a hook file looks like this:

Flatten the users collection into separate files:

The users.js hook file:

The result is two separate JSON files:

Contact u

*[Content truncated - see full docs]*

**Examples**:

```text
1git clone https://github.com/supabase-community/firebase-to-supabase.git
```

```text
1234567{  "host": "database.server.com",  "password": "secretpassword",  "user": "postgres",  "database": "postgres",  "port": 5432}
```

```text
1[{ "user": "mark", "score": 100, "items": ["hammer", "nail", "glue"] }]
```

---

## Migrate from Firebase Firestore to Supabase | Supabase Docs

**URL**: https://supabase.com/docs/guides/resources/migrating-to-supabase/firestore-data

**Contents**:
- Migrate from Firebase Firestore to Supabase
- Migrate your Firebase Firestore database to a Supabase Postgres database.
- Set up the migration tool #
- Generate a Firebase private key #
- Command line options#
  - List all Firestore collections#
  - Dump Firestore collection to JSON file#
    - Customize the JSON file with hooks#

Migrate from Firebase Firestore to Supabase

Migrate your Firebase Firestore database to a Supabase Postgres database.

Supabase provides several tools to convert data from a Firebase Firestore database to a Supabase Postgres database. The process copies the entire contents of a single Firestore collection to a single Postgres table.

The Firestore collection is "flattened" and converted to a table with basic columns of one of the following types: text, numeric, boolean, or jsonb. If your structure is more complex, you can write a program to split the newly-created json file into multiple, related tables before you import your json file(s) to Supabase.

Clone the firebase-to-supabase repository:

In the /firestore directory, create a file named supabase-service.json with the following contents:

On your project dashboard, click Connect

Under the Session pooler, click on the View parameters under the connect string. Replace the Host and User fields with the values shown.

Enter the password you used when you created your Supabase project in the password entry in the supabase-service.json file.

node firestore2json.js <collectionName> [<batchSize>] [<limit>]

You can customize the way your JSON file is written using a custom hook. A common use for this is to "flatten" the JSON file, or to split nested data into separate, related database tables. For example, you could take a Firestore document that looks like this:

And split it into two files (one table for users and one table for items):

node json2supabase.js <path_to_json_file> [<primary_key_strategy>] [<primary_key_name>]

Hooks are used to customize the process of exporting a collection of Firestore documents to JSON. They can be used for:

If your Firestore collection is called users, create a file called users.js in the current folder.

The basic format of a hook file looks like this:

Flatten the users collection into separate files:

The users.js hook file:

The result is two separate JSON files:

Contact u

*[Content truncated - see full docs]*

**Examples**:

```text
1git clone https://github.com/supabase-community/firebase-to-supabase.git
```

```text
1234567{  "host": "database.server.com",  "password": "secretpassword",  "user": "postgres",  "database": "postgres",  "port": 5432}
```

```text
1[{ "user": "mark", "score": 100, "items": ["hammer", "nail", "glue"] }]
```

---

## Migrate from Firebase Firestore to Supabase | Supabase Docs

**URL**: https://supabase.com/docs/guides/migrations/firestore-data

**Contents**:
- Migrate from Firebase Firestore to Supabase
- Migrate your Firebase Firestore database to a Supabase Postgres database.
- Set up the migration tool #
- Generate a Firebase private key #
- Command line options#
  - List all Firestore collections#
  - Dump Firestore collection to JSON file#
    - Customize the JSON file with hooks#

Migrate from Firebase Firestore to Supabase

Migrate your Firebase Firestore database to a Supabase Postgres database.

Supabase provides several tools to convert data from a Firebase Firestore database to a Supabase Postgres database. The process copies the entire contents of a single Firestore collection to a single Postgres table.

The Firestore collection is "flattened" and converted to a table with basic columns of one of the following types: text, numeric, boolean, or jsonb. If your structure is more complex, you can write a program to split the newly-created json file into multiple, related tables before you import your json file(s) to Supabase.

Clone the firebase-to-supabase repository:

In the /firestore directory, create a file named supabase-service.json with the following contents:

On your project dashboard, click Connect

Under the Session pooler, click on the View parameters under the connect string. Replace the Host and User fields with the values shown.

Enter the password you used when you created your Supabase project in the password entry in the supabase-service.json file.

node firestore2json.js <collectionName> [<batchSize>] [<limit>]

You can customize the way your JSON file is written using a custom hook. A common use for this is to "flatten" the JSON file, or to split nested data into separate, related database tables. For example, you could take a Firestore document that looks like this:

And split it into two files (one table for users and one table for items):

node json2supabase.js <path_to_json_file> [<primary_key_strategy>] [<primary_key_name>]

Hooks are used to customize the process of exporting a collection of Firestore documents to JSON. They can be used for:

If your Firestore collection is called users, create a file called users.js in the current folder.

The basic format of a hook file looks like this:

Flatten the users collection into separate files:

The users.js hook file:

The result is two separate JSON files:

Contact u

*[Content truncated - see full docs]*

**Examples**:

```text
1git clone https://github.com/supabase-community/firebase-to-supabase.git
```

```text
1234567{  "host": "database.server.com",  "password": "secretpassword",  "user": "postgres",  "database": "postgres",  "port": 5432}
```

```text
1[{ "user": "mark", "score": 100, "items": ["hammer", "nail", "glue"] }]
```

---

## Migrate from Heroku to Supabase | Supabase Docs

**URL**: https://supabase.com/docs/guides/resources/migrating-to-supabase/heroku

**Contents**:
- Migrate from Heroku to Supabase
- Migrate your Heroku Postgres database to Supabase.
- Quick demo#
- Retrieve your Heroku database credentials #
- Retrieve your Supabase connection string #
- Export your Heroku database to a file #
- Import the database to your Supabase project #
- Additional options#

Migrate from Heroku to Supabase

Migrate your Heroku Postgres database to Supabase.

Supabase is one of the best free alternatives to Heroku Postgres. This guide shows how to migrate your Heroku Postgres database to Supabase. This migration requires the pg_dump and psql CLI tools, which are installed automatically as part of the complete Postgres installation package.

Alternatively, use the Heroku to Supabase migration tool to migrate in just a few clicks.

Use pg_dump with your Heroku credentials to export your Heroku database to a file (e.g., heroku_dump.sql).

Use psql to import the Heroku database file to your Supabase project.

Run pg_dump --help for a full list of options.

If you're planning to migrate a database larger than 6 GB, we recommend upgrading to at least a Large compute add-on. This will ensure you have the necessary resources to handle the migration efficiently.

We strongly advise you to pre-provision the disk space you will need for your migration. On paid projects, you can do this by navigating to the Compute and Disk Settings page. For more information on disk scaling and disk limits, check out our disk settings documentation.

Contact us if you need more help migrating your project.

Latest product updates?

Something's not right?

**Examples**:

```text
123pg_dump --clean --if-exists --quote-all-identifiers \ -h $HEROKU_HOST -U $HEROKU_USER -d $HEROKU_DATABASE \ --no-owner --no-privileges > heroku_dump.sql
```

```text
1psql -d "$YOUR_CONNECTION_STRING" -f heroku_dump.sql
```

---

## Migrate from Heroku to Supabase | Supabase Docs

**URL**: https://supabase.com/docs/guides/platform/migrating-to-supabase/heroku

**Contents**:
- Migrate from Heroku to Supabase
- Migrate your Heroku Postgres database to Supabase.
- Quick demo#
- Retrieve your Heroku database credentials #
- Retrieve your Supabase connection string #
- Export your Heroku database to a file #
- Import the database to your Supabase project #
- Additional options#

Migrate from Heroku to Supabase

Migrate your Heroku Postgres database to Supabase.

Supabase is one of the best free alternatives to Heroku Postgres. This guide shows how to migrate your Heroku Postgres database to Supabase. This migration requires the pg_dump and psql CLI tools, which are installed automatically as part of the complete Postgres installation package.

Alternatively, use the Heroku to Supabase migration tool to migrate in just a few clicks.

Use pg_dump with your Heroku credentials to export your Heroku database to a file (e.g., heroku_dump.sql).

Use psql to import the Heroku database file to your Supabase project.

Run pg_dump --help for a full list of options.

If you're planning to migrate a database larger than 6 GB, we recommend upgrading to at least a Large compute add-on. This will ensure you have the necessary resources to handle the migration efficiently.

We strongly advise you to pre-provision the disk space you will need for your migration. On paid projects, you can do this by navigating to the Compute and Disk Settings page. For more information on disk scaling and disk limits, check out our disk settings documentation.

Contact us if you need more help migrating your project.

Latest product updates?

Something's not right?

**Examples**:

```text
123pg_dump --clean --if-exists --quote-all-identifiers \ -h $HEROKU_HOST -U $HEROKU_USER -d $HEROKU_DATABASE \ --no-owner --no-privileges > heroku_dump.sql
```

```text
1psql -d "$YOUR_CONNECTION_STRING" -f heroku_dump.sql
```

---

## Migrate from MSSQL to Supabase | Supabase Docs

**URL**: https://supabase.com/docs/guides/platform/migrating-to-supabase/mssql

**Contents**:
- Migrate from MSSQL to Supabase
- Migrate your Microsoft SQL Server database to Supabase.
- Retrieve your MSSQL database credentials#
- Retrieve your Supabase host #
- Migrate the database#
- Enterprise#
  - Is this helpful?

Migrate from MSSQL to Supabase

Migrate your Microsoft SQL Server database to Supabase.

This guide aims to demonstrate the process of transferring your Microsoft SQL Server database to Supabase's Postgres database. Supabase is a powerful and open-source platform offering a wide range of backend features, including a Postgres database, authentication, instant APIs, edge functions, real-time subscriptions, and storage. Migrating your MSSQL database to Supabase's Postgres enables you to leverage Postgres's capabilities and access all the features you need for your project.

Before you begin the migration, you need to collect essential information about your MSSQL database. Follow these steps:

If you're new to Supabase, create a project. Make a note of your password, you will need this later. If you forget it, you can reset it here.

On your project dashboard, click Connect

Under the Session pooler, click on the View parameters under the connect string. Note your Host ($SUPABASE_HOST).

The fastest way to migrate your database is with the Supabase migration tool on Google Colab.

Alternatively, you can use pgloader, a flexible and powerful data migration tool that supports a wide range of source database engines, including MySQL and MS SQL, and migrates the data to a Postgres database. For databases using the Postgres engine, we recommend using the pg_dump and psql command line tools, which are included in a full Postgres installation.

If you're planning to migrate a database larger than 6 GB, we recommend upgrading to at least a Large compute add-on. This will ensure you have the necessary resources to handle the migration efficiently.

We strongly advise you to pre-provision the disk space you will need for your migration. On paid projects, you can do this by navigating to the Compute and Disk Settings page. For more information on disk scaling and disk limits, check out our disk settings documentation.

Contact us if you need more help migrating your project.

La

*[Content truncated - see full docs]*

---

## Migrate from MSSQL to Supabase | Supabase Docs

**URL**: https://supabase.com/docs/guides/resources/migrating-to-supabase/mssql

**Contents**:
- Migrate from MSSQL to Supabase
- Migrate your Microsoft SQL Server database to Supabase.
- Retrieve your MSSQL database credentials#
- Retrieve your Supabase host #
- Migrate the database#
- Enterprise#
  - Is this helpful?

Migrate from MSSQL to Supabase

Migrate your Microsoft SQL Server database to Supabase.

This guide aims to demonstrate the process of transferring your Microsoft SQL Server database to Supabase's Postgres database. Supabase is a powerful and open-source platform offering a wide range of backend features, including a Postgres database, authentication, instant APIs, edge functions, real-time subscriptions, and storage. Migrating your MSSQL database to Supabase's Postgres enables you to leverage Postgres's capabilities and access all the features you need for your project.

Before you begin the migration, you need to collect essential information about your MSSQL database. Follow these steps:

If you're new to Supabase, create a project. Make a note of your password, you will need this later. If you forget it, you can reset it here.

On your project dashboard, click Connect

Under the Session pooler, click on the View parameters under the connect string. Note your Host ($SUPABASE_HOST).

The fastest way to migrate your database is with the Supabase migration tool on Google Colab.

Alternatively, you can use pgloader, a flexible and powerful data migration tool that supports a wide range of source database engines, including MySQL and MS SQL, and migrates the data to a Postgres database. For databases using the Postgres engine, we recommend using the pg_dump and psql command line tools, which are included in a full Postgres installation.

If you're planning to migrate a database larger than 6 GB, we recommend upgrading to at least a Large compute add-on. This will ensure you have the necessary resources to handle the migration efficiently.

We strongly advise you to pre-provision the disk space you will need for your migration. On paid projects, you can do this by navigating to the Compute and Disk Settings page. For more information on disk scaling and disk limits, check out our disk settings documentation.

Contact us if you need more help migrating your project.

La

*[Content truncated - see full docs]*

---

## Migrate from MySQL to Supabase | Supabase Docs

**URL**: https://supabase.com/docs/guides/resources/migrating-to-supabase/mysql

**Contents**:
- Migrate from MySQL to Supabase
- Migrate your MySQL database to Supabase Postgres database.
- Retrieve your MySQL database credentials#
- Retrieve your Supabase host #
- Migrate the database#
- Enterprise#
  - Is this helpful?

Migrate from MySQL to Supabase

Migrate your MySQL database to Supabase Postgres database.

This guide aims to exhibit the process of transferring your MySQL database to Supabase's Postgres database. Supabase is a robust and open-source platform offering a wide range of backend features, including a Postgres database, authentication, instant APIs, edge functions, real-time subscriptions, and storage. Migrating your MySQL database to Supabase's Postgres enables you to leverage PostgreSQL's capabilities and access all the features you need for your project.

Before you begin the migration, you need to collect essential information about your MySQL database. Follow these steps:

Log in to your MySQL database provider.

Locate and note the following database details:

If you're new to Supabase, create a project. Make a note of your password, you will need this later. If you forget it, you can reset it here.

On your project dashboard, click Connect

Under the Session pooler, click on the View parameters under the connect string. Note your Host ($SUPABASE_HOST).

The fastest way to migrate your database is with the Supabase migration tool on Google Colab.

Alternatively, you can use pgloader, a flexible and powerful data migration tool that supports a wide range of source database engines, including MySQL and MS SQL, and migrates the data to a Postgres database. For databases using the Postgres engine, we recommend using the pg_dump and psql command line tools, which are included in a full Postgres installation.

If you're planning to migrate a database larger than 6 GB, we recommend upgrading to at least a Large compute add-on. This will ensure you have the necessary resources to handle the migration efficiently.

We strongly advise you to pre-provision the disk space you will need for your migration. On paid projects, you can do this by navigating to the Compute and Disk Settings page. For more information on disk scaling and disk limits, check out our disk settings do

*[Content truncated - see full docs]*

---

## Migrate from MySQL to Supabase | Supabase Docs

**URL**: https://supabase.com/docs/guides/platform/migrating-to-supabase/mysql

**Contents**:
- Migrate from MySQL to Supabase
- Migrate your MySQL database to Supabase Postgres database.
- Retrieve your MySQL database credentials#
- Retrieve your Supabase host #
- Migrate the database#
- Enterprise#
  - Is this helpful?

Migrate from MySQL to Supabase

Migrate your MySQL database to Supabase Postgres database.

This guide aims to exhibit the process of transferring your MySQL database to Supabase's Postgres database. Supabase is a robust and open-source platform offering a wide range of backend features, including a Postgres database, authentication, instant APIs, edge functions, real-time subscriptions, and storage. Migrating your MySQL database to Supabase's Postgres enables you to leverage PostgreSQL's capabilities and access all the features you need for your project.

Before you begin the migration, you need to collect essential information about your MySQL database. Follow these steps:

Log in to your MySQL database provider.

Locate and note the following database details:

If you're new to Supabase, create a project. Make a note of your password, you will need this later. If you forget it, you can reset it here.

On your project dashboard, click Connect

Under the Session pooler, click on the View parameters under the connect string. Note your Host ($SUPABASE_HOST).

The fastest way to migrate your database is with the Supabase migration tool on Google Colab.

Alternatively, you can use pgloader, a flexible and powerful data migration tool that supports a wide range of source database engines, including MySQL and MS SQL, and migrates the data to a Postgres database. For databases using the Postgres engine, we recommend using the pg_dump and psql command line tools, which are included in a full Postgres installation.

If you're planning to migrate a database larger than 6 GB, we recommend upgrading to at least a Large compute add-on. This will ensure you have the necessary resources to handle the migration efficiently.

We strongly advise you to pre-provision the disk space you will need for your migration. On paid projects, you can do this by navigating to the Compute and Disk Settings page. For more information on disk scaling and disk limits, check out our disk settings do

*[Content truncated - see full docs]*

---

## Migrate from Neon to Supabase | Supabase Docs

**URL**: https://supabase.com/docs/guides/platform/migrating-to-supabase/neon

**Contents**:
- Migrate from Neon to Supabase
- Migrate your existing Neon database to Supabase.
- Retrieve your Neon database credentials #
- Set your OLD_DB_URL environment variable#
- Retrieve your Supabase connection string #
- Set your NEW_DB_URL environment variable#
- Migrate the database#
- Enterprise#

Migrate from Neon to Supabase

Migrate your existing Neon database to Supabase.

This guide demonstrates how to migrate your Neon database to Supabase to get the most out of Postgres while gaining access to all the features you need to build a project.

Set the OLD_DB_URL environment variable at the command line using your Neon database credentials from the clipboard.

If you're new to Supabase, create a project. Make a note of your password, you will need this later. If you forget it, you can reset it here.

On your project dashboard, click Connect

Under the Session pooler, click the Copy button to the right of your connection string to copy it to the clipboard.

Set the NEW_DB_URL environment variable at the command line using your Supabase connection string. You will need to replace [YOUR-PASSWORD] with your actual database password.

You will need the pg_dump and psql command line tools, which are included in a full Postgres installation.

Export your database to a file in console

Use pg_dump with your Postgres credentials to export your database to a file (e.g., dump.sql).

Import the database to your Supabase project

Use psql to import the Postgres database file to your Supabase project.

Run pg_dump --help for a full list of options.

If you're planning to migrate a database larger than 6 GB, we recommend upgrading to at least a Large compute add-on. This will ensure you have the necessary resources to handle the migration efficiently.

We strongly advise you to pre-provision the disk space you will need for your migration. On paid projects, you can do this by navigating to the Compute and Disk Settings page. For more information on disk scaling and disk limits, check out our disk settings documentation.

Contact us if you need more help migrating your project.

Latest product updates?

Something's not right?

**Examples**:

```text
1postgresql://neondb_owner:xxxxxxxxxxxxxxx-random-word-yyyyyyyy.us-west-2.aws.neon.tech/neondb?sslmode=require
```

```text
1export OLD_DB_URL="postgresql://neondb_owner:xxxxxxxxxxxxxxx-random-word-yyyyyyyy.us-west-2.aws.neon.tech/neondb?sslmode=require"
```

```text
1export NEW_DB_URL="postgresql://postgres.xxxxxxxxxxxxxxxxxxxx:[YOUR-PASSWORD]@aws-0-us-west-1.pooler.supabase.com:5432/postgres"
```

---

## Migrate from Postgres to Supabase | Supabase Docs

**URL**: https://supabase.com/docs/guides/platform/migrating-to-supabase/postgres

**Contents**:
- Migrate from Postgres to Supabase
- Migrate your existing Postgres database to Supabase.
- Retrieve your Postgres database credentials #
- Retrieve your Supabase connection string #
- Migrate the database#
- Enterprise#
  - Is this helpful?

Migrate from Postgres to Supabase

Migrate your existing Postgres database to Supabase.

This is a guide for migrating your Postgres database to Supabase. Supabase is a robust and open-source platform. Supabase provide all the backend features developers need to build a product: a Postgres database, authentication, instant APIs, edge functions, realtime subscriptions, and storage. Postgres is the core of Supabase—for example, you can use row-level security and there are more than 40 Postgres extensions available.

This guide demonstrates how to migrate your Postgres database to Supabase to get the most out of Postgres while gaining access to all the features you need to build a project.

If you're new to Supabase, create a project. Make a note of your password, you will need this later. If you forget it, you can reset it here.

On your project dashboard, click Connect

Under Session pooler, Copy the connection string and replace the password placeholder with your database password.

If you're in an IPv6 environment or have the IPv4 Add-On, you can use the direct connection string instead of Supavisor in Session mode.

The fastest way to migrate your database is with the Supabase migration tool on Google Colab. Alternatively, you can use the pg_dump and psql command line tools, which are included in a full Postgres installation.

If you're planning to migrate a database larger than 6 GB, we recommend upgrading to at least a Large compute add-on. This will ensure you have the necessary resources to handle the migration efficiently.

We strongly advise you to pre-provision the disk space you will need for your migration. On paid projects, you can do this by navigating to the Compute and Disk Settings page. For more information on disk scaling and disk limits, check out our disk settings documentation.

Contact us if you need more help migrating your project.

Latest product updates?

Something's not right?

**Examples**:

```text
1%env PSQL_COMMAND=PGPASSWORD=RgaMDfTS_password_FTPa7 psql -h dpg-a_server_in.oregon-postgres.provider.com -U my_db_pxl0_user my_db_pxl0
```

---

## Migrate from Postgres to Supabase | Supabase Docs

**URL**: https://supabase.com/docs/guides/resources/migrating-to-supabase/postgres

**Contents**:
- Migrate from Postgres to Supabase
- Migrate your existing Postgres database to Supabase.
- Retrieve your Postgres database credentials #
- Retrieve your Supabase connection string #
- Migrate the database#
- Enterprise#
  - Is this helpful?

Migrate from Postgres to Supabase

Migrate your existing Postgres database to Supabase.

This is a guide for migrating your Postgres database to Supabase. Supabase is a robust and open-source platform. Supabase provide all the backend features developers need to build a product: a Postgres database, authentication, instant APIs, edge functions, realtime subscriptions, and storage. Postgres is the core of Supabase—for example, you can use row-level security and there are more than 40 Postgres extensions available.

This guide demonstrates how to migrate your Postgres database to Supabase to get the most out of Postgres while gaining access to all the features you need to build a project.

If you're new to Supabase, create a project. Make a note of your password, you will need this later. If you forget it, you can reset it here.

On your project dashboard, click Connect

Under Session pooler, Copy the connection string and replace the password placeholder with your database password.

If you're in an IPv6 environment or have the IPv4 Add-On, you can use the direct connection string instead of Supavisor in Session mode.

The fastest way to migrate your database is with the Supabase migration tool on Google Colab. Alternatively, you can use the pg_dump and psql command line tools, which are included in a full Postgres installation.

If you're planning to migrate a database larger than 6 GB, we recommend upgrading to at least a Large compute add-on. This will ensure you have the necessary resources to handle the migration efficiently.

We strongly advise you to pre-provision the disk space you will need for your migration. On paid projects, you can do this by navigating to the Compute and Disk Settings page. For more information on disk scaling and disk limits, check out our disk settings documentation.

Contact us if you need more help migrating your project.

Latest product updates?

Something's not right?

**Examples**:

```text
1%env PSQL_COMMAND=PGPASSWORD=RgaMDfTS_password_FTPa7 psql -h dpg-a_server_in.oregon-postgres.provider.com -U my_db_pxl0_user my_db_pxl0
```

---

## Migrate from Render to Supabase | Supabase Docs

**URL**: https://supabase.com/docs/guides/platform/migrating-to-supabase/render

**Contents**:
- Migrate from Render to Supabase
- Migrate your Render Postgres database to Supabase.
- Retrieve your Render database credentials #
- Retrieve your Supabase connection string #
- Migrate the database#
- Enterprise#
  - Is this helpful?

Migrate from Render to Supabase

Migrate your Render Postgres database to Supabase.

Render is a popular Web Hosting service in the online services category that also has a managed Postgres service. Render has a great developer experience, allowing users to deploy straight from GitHub or GitLab. This is the core of their product and they do it really well. However, when it comes to Postgres databases, it may not be the best option.

Supabase is one of the best free alternative to Render Postgres. Supabase provide all the backend features developers need to build a product: a Postgres database, authentication, instant APIs, edge functions, realtime subscriptions, and storage. Postgres is the core of Supabase—for example, you can use row-level security and there are more than 40 Postgres extensions available.

This guide demonstrates how to migrate from Render to Supabase to get the most out of Postgres while gaining access to all the features you need to build a project.

If you're new to Supabase, create a project. Make a note of your password, you will need this later. If you forget it, you can reset it here.

On your project dashboard, click Connect

Under Session pooler, Copy the connection string and replace the password placeholder with your database password.

If you're in an IPv6 environment or have the IPv4 Add-On, you can use the direct connection string instead of Supavisor in Session mode.

The fastest way to migrate your database is with the Supabase migration tool on Google Colab. Alternatively, you can use the pg_dump and psql command line tools, which are included in a full Postgres installation.

If you're planning to migrate a database larger than 6 GB, we recommend upgrading to at least a Large compute add-on. This will ensure you have the necessary resources to handle the migration efficiently.

We strongly advise you to pre-provision the disk space you will need for your migration. On paid projects, you can do this by navigating to the Compute an

*[Content truncated - see full docs]*

**Examples**:

```text
1%env PSQL_COMMAND=PGPASSWORD=RgaMDfTS_password_FTPa7 psql -h dpg-a_server_in.oregon-postgres.render.com -U my_db_pxl0_user my_db_pxl0
```

---

## Migrate from Render to Supabase | Supabase Docs

**URL**: https://supabase.com/docs/guides/resources/migrating-to-supabase/render

**Contents**:
- Migrate from Render to Supabase
- Migrate your Render Postgres database to Supabase.
- Retrieve your Render database credentials #
- Retrieve your Supabase connection string #
- Migrate the database#
- Enterprise#
  - Is this helpful?

Migrate from Render to Supabase

Migrate your Render Postgres database to Supabase.

Render is a popular Web Hosting service in the online services category that also has a managed Postgres service. Render has a great developer experience, allowing users to deploy straight from GitHub or GitLab. This is the core of their product and they do it really well. However, when it comes to Postgres databases, it may not be the best option.

Supabase is one of the best free alternative to Render Postgres. Supabase provide all the backend features developers need to build a product: a Postgres database, authentication, instant APIs, edge functions, realtime subscriptions, and storage. Postgres is the core of Supabase—for example, you can use row-level security and there are more than 40 Postgres extensions available.

This guide demonstrates how to migrate from Render to Supabase to get the most out of Postgres while gaining access to all the features you need to build a project.

If you're new to Supabase, create a project. Make a note of your password, you will need this later. If you forget it, you can reset it here.

On your project dashboard, click Connect

Under Session pooler, Copy the connection string and replace the password placeholder with your database password.

If you're in an IPv6 environment or have the IPv4 Add-On, you can use the direct connection string instead of Supavisor in Session mode.

The fastest way to migrate your database is with the Supabase migration tool on Google Colab. Alternatively, you can use the pg_dump and psql command line tools, which are included in a full Postgres installation.

If you're planning to migrate a database larger than 6 GB, we recommend upgrading to at least a Large compute add-on. This will ensure you have the necessary resources to handle the migration efficiently.

We strongly advise you to pre-provision the disk space you will need for your migration. On paid projects, you can do this by navigating to the Compute an

*[Content truncated - see full docs]*

**Examples**:

```text
1%env PSQL_COMMAND=PGPASSWORD=RgaMDfTS_password_FTPa7 psql -h dpg-a_server_in.oregon-postgres.render.com -U my_db_pxl0_user my_db_pxl0
```

---

## Migrate from Vercel Postgres to Supabase | Supabase Docs

**URL**: https://supabase.com/docs/guides/platform/migrating-to-supabase/vercel-postgres

**Contents**:
- Migrate from Vercel Postgres to Supabase
- Migrate your existing Vercel Postgres database to Supabase.
- Retrieve your Vercel Postgres database credentials #
- Set your OLD_DB_URL environment variable#
- Retrieve your Supabase connection string #
- Set your NEW_DB_URL environment variable#
- Migrate the database#
- Enterprise#

Migrate from Vercel Postgres to Supabase

Migrate your existing Vercel Postgres database to Supabase.

This guide demonstrates how to migrate your Vercel Postgres database to Supabase to get the most out of Postgres while gaining access to all the features you need to build a project.

Copy this part to your clipboard:

Set the OLD_DB_URL environment variable at the command line using your Vercel Postgres Database credentials.

If you're new to Supabase, create a project. Make a note of your password, you will need this later. If you forget it, you can reset it here.

On your project dashboard, click Connect

Under the Session pooler, click the Copy button to the right of your connection string to copy it to the clipboard.

Set the NEW_DB_URL environment variable at the command line using your Supabase connection string. You will need to replace [YOUR-PASSWORD] with your actual database password.

You will need the pg_dump and psql command line tools, which are included in a full Postgres installation.

Export your database to a file in console

Use pg_dump with your Postgres credentials to export your database to a file (e.g., dump.sql).

Import the database to your Supabase project

Use psql to import the Postgres database file to your Supabase project.

Run pg_dump --help for a full list of options.

If you're planning to migrate a database larger than 6 GB, we recommend upgrading to at least a Large compute add-on. This will ensure you have the necessary resources to handle the migration efficiently.

We strongly advise you to pre-provision the disk space you will need for your migration. On paid projects, you can do this by navigating to the Compute and Disk Settings page. For more information on disk scaling and disk limits, check out our disk settings documentation.

Contact us if you need more help migrating your project.

Latest product updates?

Something's not right?

**Examples**:

```text
1psql "postgres://default:xxxxxxxxxxxx@yy-yyyyy-yyyyyy-yyyyyyy.us-west-2.aws.neon.tech:5432/verceldb?sslmode=require"
```

```text
1"postgres://default:xxxxxxxxxxxx@yy-yyyyy-yyyyyy-yyyyyyy.us-west-2.aws.neon.tech:5432/verceldb?sslmode=require"
```

```text
1export OLD_DB_URL="postgres://default:xxxxxxxxxxxx@yy-yyyyy-yyyyyy-yyyyyyy.us-west-2.aws.neon.tech:5432/verceldb?sslmode=require"
```

---

## Postgres Changes | Supabase Docs

**URL**: https://supabase.com/docs/guides/realtime/postgres-changes

**Contents**:
- Postgres Changes
- Listen to Postgres changes using Supabase Realtime.
- Quick start#
  - Set up a Supabase project with a 'todos' table
  - Allow anonymous access
  - Enable Postgres replication
  - Install the client
  - Create the client

Listen to Postgres changes using Supabase Realtime.

Let's explore how to use Realtime's Postgres Changes feature to listen to database events.

In this example we'll set up a database table, secure it with Row Level Security, and subscribe to all changes using the Supabase client libraries.

Create a new project in the Supabase Dashboard.

After your project is ready, create a table in your Supabase database. You can do this with either the Table interface or the SQL Editor.

In this example we'll turn on Row Level Security for this table and allow anonymous access. In production, be sure to secure your application with the appropriate permissions.

Go to your project's Publications settings, and under supabase_realtime, toggle on the tables you want to listen to.

Alternatively, add tables to the supabase_realtime publication by running the given SQL:

Install the Supabase JavaScript client.

This client will be used to listen to Postgres changes.

Listen to changes on all tables in the public schema by setting the schema property to 'public' and event name to *. The event name can be one of:

The channel name can be any string except 'realtime'.

Now we can add some data to our table which will trigger the channelA event handler.

You can use the Supabase client libraries to subscribe to database changes.

Subscribe to specific schema events using the schema parameter:

The channel name can be any string except 'realtime'.

Use the event parameter to listen only to database INSERTs:

The channel name can be any string except 'realtime'.

Use the event parameter to listen only to database UPDATEs:

The channel name can be any string except 'realtime'.

Use the event parameter to listen only to database DELETEs:

The channel name can be any string except 'realtime'.

Subscribe to specific table events using the table parameter:

The channel name can be any string except 'realtime'.

To listen to different events and schema/tables/filters combinations with the same 

*[Content truncated - see full docs]*

**Examples**:

```text
123456-- Create a table called "todos"-- with a column to store tasks.create table todos (  id serial primary key,  task text);
```

```text
12345678910-- Turn on securityalter table "todos"enable row level security;-- Allow anonymous accesscreate policy "Allow anonymous access"on todosfor selectto anonusing (true);
```

```text
12alter publication supabase_realtimeadd table your_table_name;
```

---

## Postgres Extensions Overview | Supabase Docs

**URL**: https://supabase.com/docs/guides/database/extensions

**Contents**:
- Postgres Extensions Overview
  - Enable and disable extensions#
  - Upgrade extensions#
  - Full list of extensions#
  - Is this helpful?

Postgres Extensions Overview

Extensions are exactly as they sound - they "extend" the database with functionality which isn't part of the Postgres core. Supabase has pre-installed some of the most useful open source extensions.

Most extensions are installed under the extensions schema, which is accessible to public by default. To avoid namespace pollution, we do not recommend creating other entities in the extensions schema.

If you need to restrict user access to tables managed by extensions, we recommend creating a separate schema for installing that specific extension.

Some extensions can only be created under a specific schema, for example, postgis_tiger_geocoder extension creates a schema named tiger. Before enabling such extensions, make sure you have not created a conflicting schema with the same name.

In addition to the pre-configured extensions, you can also install your own SQL extensions directly in the database using Supabase's SQL editor. The SQL code for the extensions, including plpgsql extensions, can be added through the SQL editor.

If a new version of an extension becomes available on Supabase, you need to initiate a software upgrade in the Infrastructure Settings to access it. Software upgrades can also be initiated by restarting your server in the General Settings.

Supabase is pre-configured with over 50 extensions and you can install additional extensions through the database.dev package manager.

You can install pure SQL extensions directly in the database using the SQL editor or any Postgres client.

If you would like to request an extension, add (or upvote) it in the GitHub Discussion.

Latest product updates?

Something's not right?

---

## Postgres Roles | Supabase Docs

**URL**: https://supabase.com/docs/guides/database/managing-passwords

**Contents**:
- Postgres Roles
- Managing access to your Postgres database and configuring permissions.
- Users vs roles#
- Creating roles#
- Creating users#
- Passwords#
  - Special symbols in passwords#
  - Changing your project password#

Managing access to your Postgres database and configuring permissions.

Postgres manages database access permissions using the concept of roles. Generally you wouldn't use these roles for your own application - they are mostly for configuring system access to your database. If you want to configure application access, then you should use Row Level Security (RLS). You can also implement Role-based Access Control on top of RLS.

In Postgres, roles can function as users or groups of users. Users are roles with login privileges, while groups (also known as role groups) are roles that don't have login privileges but can be used to manage permissions for multiple users.

You can create a role using the create role command:

Roles and users are essentially the same in Postgres, however if you want to use password-logins for a specific role, then you can use WITH LOGIN PASSWORD:

Your Postgres database is the core of your Supabase project, so it's important that every role has a strong, secure password at all times. Here are some tips for creating a secure password:

If you use special symbols in your Postgres password, you must remember to percent-encode your password later if using the Postgres connection string, for example, postgresql://postgres.projectref:p%3Dword@aws-0-us-east-1.pooler.supabase.com:6543/postgres

When you created your project you were also asked to enter a password. This is the password for the postgres role in your database. You can update this from the Dashboard under the Database Settings page. You should never give this to third-party service unless you absolutely trust them. Instead, we recommend that you create a new user for every service that you want to give access too. This will also help you with debugging - you can see every query that each role is executing in your database within pg_stat_statements.

Changing the password does not result in any downtime. All connected services, such as PostgREST, PgBouncer, and other Supabase managed ser

*[Content truncated - see full docs]*

**Examples**:

```text
1create role "role_name";
```

```text
1create role "role_name" with login password 'extremely_secure_password';
```

```text
1REVOKE permission_type ON object_name FROM role_name;
```

---

## Print PostgreSQL version | Supabase Docs

**URL**: https://supabase.com/docs/guides/database/postgres/which-version-of-postgres

**Contents**:
- Print PostgreSQL version
  - Is this helpful?

Print PostgreSQL version

It's important to know which version of Postgres you are running as each major version has different features and may cause breaking changes. You may also need to update your schema when upgrading or downgrading to a major Postgres version.

Run the following query using the SQL Editor in the Supabase Dashboard:

Which should return something like:

This query can also be executed via psql or any other query editor if you prefer to connect directly to the database.

Latest product updates?

Something's not right?

**Examples**:

```text
12select  version();
```

```text
1PostgreSQL 15.1 on aarch64-unknown-linux-gnu, compiled by gcc (Ubuntu 10.3.0-1ubuntu1~20.04) 10.3.0, 64-bit
```

---

## Python client | Supabase Docs

**URL**: https://supabase.com/docs/guides/ai/vecs-python-client

**Contents**:
- Python client
- Manage unstructured vector stores in PostgreSQL.
- Quick start#
  - Initialize your project#
  - Create a collection#
  - Add embeddings#
  - Query the collection#
- Deep dive#

Manage unstructured vector stores in PostgreSQL.

Supabase provides a Python client called vecs for managing unstructured vector stores. This client provides a set of useful tools for creating and querying collections in Postgres using the pgvector extension.

Let's see how Vecs works using a local database. Make sure you have the Supabase CLI installed on your machine.

Start a local Postgres instance in any folder using the init and start commands. Make sure you have Docker running!

Inside a Python shell, run the following commands to create a new collection called "docs", with 3 dimensions.

Now we can insert some embeddings into our "docs" collection using the upsert() command:

You can now query the collection to retrieve a relevant match:

For a more in-depth guide on vecs collections, see API.

Latest product updates?

Something's not right?

**Examples**:

```text
12345# Initialize your projectsupabase init# Start Postgressupabase start
```

```text
1234567import vecs# create vector store clientvx = vecs.create_client("postgresql://postgres:postgres@localhost:54322/postgres")# create a collection of vectors with 3 dimensionsdocs = vx.get_or_create_collection(name="docs", dimension=3)
```

```text
12345678910111213import vecs# create vector store clientdocs = vecs.get_or_create_collection(name="docs", dimension=3)# a collection of vectors with 3 dimensionsvectors=[  ("vec0", [0.1, 0.2, 0.3], {"year": 1973}),  ("vec1", [0.7, 0.8, 0.9], {"year": 2012})]# insert our vectorsdocs.upsert(vectors=vectors)
```

---

## REST API | Supabase Docs

**URL**: https://supabase.com/docs/guides/api

**Contents**:
- REST API
- Features #
- API URL and keys#
  - Is this helpful?

Supabase auto-generates an API directly from your database schema allowing you to connect to your database through a restful interface, directly from the browser.

The API is auto-generated from your database and is designed to get you building as fast as possible, without writing a single line of code.

You can use them directly from the browser (two-tier architecture), or as a complement to your own API server (three-tier architecture).

Supabase provides a RESTful API using PostgREST. This is a very thin API layer on top of Postgres. It exposes everything you need from a CRUD API at the URL https://<project_ref>.supabase.co/rest/v1/.

The REST interface is automatically reflected from your database's schema and is:

The reflected API is designed to retain as much of Postgres' capability as possible including:

The REST API resolves all requests to a single SQL statement leading to fast response times and high throughput.

You can find the API URL and Keys in the Dashboard.

Latest product updates?

Something's not right?

---

## Row Level Security | Supabase Docs

**URL**: https://supabase.com/docs/guides/database/postgres/row-level-security

**Contents**:
- Row Level Security
- Secure your data using Postgres Row Level Security.
- Row Level Security in Supabase#
- Policies#
- Enabling Row Level Security#
      - `auth.uid()` Returns `null` When Unauthenticated
- Authenticated and unauthenticated roles#
      - Anonymous user vs the anon key

Secure your data using Postgres Row Level Security.

When you need granular authorization rules, nothing beats Postgres's Row Level Security (RLS).

Supabase allows convenient and secure data access from the browser, as long as you enable RLS.

RLS must always be enabled on any tables stored in an exposed schema. By default, this is the public schema.

RLS is enabled by default on tables created with the Table Editor in the dashboard. If you create one in raw SQL or with the SQL editor, remember to enable RLS yourself:

RLS is incredibly powerful and flexible, allowing you to write complex SQL rules that fit your unique business needs. RLS can be combined with Supabase Auth for end-to-end user security from the browser to the database.

RLS is a Postgres primitive and can provide "defense in depth" to protect your data from malicious actors even when accessed through third-party tooling.

Policies are Postgres's rule engine. Policies are easy to understand once you get the hang of them. Each policy is attached to a table, and the policy is executed every time a table is accessed.

You can just think of them as adding a WHERE clause to every query. For example a policy like this ...

.. would translate to this whenever a user tries to select from the todos table:

You can enable RLS for any table using the enable row level security clause:

Once you have enabled RLS, no data will be accessible via the API when using the public anon key, until you create policies.

When a request is made without an authenticated user (e.g., no access token is provided or the session has expired), auth.uid() returns null.

This means that a policy like:

will silently fail for unauthenticated users, because:

is always false in SQL.

To avoid confusion and make your intention clear, we recommend explicitly checking for authentication:

Supabase maps every request to one of the roles:

These are actually Postgres Roles. You can use these roles within your Policies using the TO clause:



*[Content truncated - see full docs]*

**Examples**:

```text
12alter table <schema_name>.<table_name>enable row level security;
```

```text
123create policy "Individuals can view their own todos."on todos for selectusing ( (select auth.uid()) = user_id );
```

```text
1234select *from todoswhere auth.uid() = todos.user_id;-- Policy is implicitly added.
```

---

## Select first row for each group in PostgreSQL | Supabase Docs

**URL**: https://supabase.com/docs/guides/database/postgres/first-row-in-group

**Contents**:
- Select first row for each group in PostgreSQL
  - Is this helpful?

Select first row for each group in PostgreSQL

Given a table seasons:

We want to find the rows containing the maximum number of points per team.

The expected output we want is:

From the SQL Editor, you can run a query like:

The important bits here are:

This query can also be executed via psql or any other query editor if you prefer to connect directly to the database.

Latest product updates?

Something's not right?

**Examples**:

```text
12345678910select distinct  on (team) id,  team,  pointsfrom  seasonsorder BY  id,  points desc,  team;
```

---

## Self-Hosting | Supabase Docs

**URL**: https://supabase.com/docs/reference/self-hosting-realtime/introduction

**Contents**:
- Self-Hosting Realtime
- Why not just use PostgreSQL's NOTIFY?#
- Benefits#
- Does this server guarantee delivery of every data change?#
  - Client libraries#
  - Additional links#

Supabase Realtime is a server built with Elixir using the Phoenix Framework that allows you to listen to changes in your PostgreSQL database via logical replication and then broadcast those changes via WebSockets.

There are two versions of this server: Realtime and Realtime RLS.

Realtime server works by:

Realtime RLS server works by:

Not yet! Due to the following limitations:

Latest product updates?

Something's not right?

---

## Supabase Queues | Supabase Docs

**URL**: https://supabase.com/docs/guides/queues

**Contents**:
- Supabase Queues
- Durable Message Queues with Guaranteed Delivery in Postgres
- Features#
- Resources#
  - Is this helpful?

Durable Message Queues with Guaranteed Delivery in Postgres

Supabase Queues is a Postgres-native durable Message Queue system with guaranteed delivery built on the pgmq database extension. It offers developers a seamless way to persist and process Messages in the background while improving the resiliency and scalability of their applications and services.

Queues couples the reliability of Postgres with the simplicity Supabase's platform and developer experience, enabling developers to manage Background Tasks with zero configuration.

Latest product updates?

Something's not right?

---

## Type-Safe SQL with Kysely | Supabase Docs

**URL**: https://supabase.com/docs/guides/functions/kysely-postgres

**Contents**:
- Type-Safe SQL with Kysely
- Code#
  - Is this helpful?

Type-Safe SQL with Kysely

Supabase Edge Functions can connect directly to your Postgres database to execute SQL queries. Kysely is a type-safe and autocompletion-friendly typescript SQL query builder.

Combining Kysely with Deno Postgres gives you a convenient developer experience for interacting directly with your Postgres database.

Find the example on GitHub

Get your database connection credentials from the project's Connect panel and store them in an .env file:

Create a DenoPostgresDriver.ts file to manage the connection to Postgres via deno-postgres:

Create an index.ts file to execute a query on incoming requests:

Latest product updates?

Something's not right?

**Examples**:

```text
12345DB_HOSTNAME=DB_PASSWORD=DB_SSL_CERT="-----BEGIN CERTIFICATE-----GET YOUR CERT FROM YOUR PROJECT DASHBOARD-----END CERTIFICATE-----"
```

```python
123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114115116117118119120121122123124125126127128129130131132133134135136137138139140141142143144145146147148149150151import {  CompiledQuery,  DatabaseConnection,  Driver,  PostgresCursorConstructor,  QueryResult,  TransactionSettings,} from 'https://esm.sh/kysely@0.23.4'
...
```

```python
12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970717273747576777879808182import { serve } from 'https://deno.land/std@0.175.0/http/server.ts'import { Pool } from 'https://deno.land/x/postgres@v0.17.0/mod.ts'import {  Kysely,  Generated,  PostgresAdapter,  PostgresIntrospector,  PostgresQueryCompiler,} from 'https://esm.sh/kysely@0.23.4'import { PostgresDriver } from './DenoPostgresDriver.ts'console.log(`Function "k
...
```

---
