# Supabase - Storage

**Pages**: 5

---

## Migrated from Firebase Storage to Supabase | Supabase Docs

**URL**: https://supabase.com/docs/guides/resources/migrating-to-supabase/firebase-storage

**Contents**:
- Migrated from Firebase Storage to Supabase
- Migrate Firebase Storage files to Supabase Storage.
- Set up the migration tool #
- Generate a Firebase private key #
- Command line options#
  - Download Firestore Storage bucket to a local filesystem folder #
  - Upload files to Supabase Storage bucket #
- Resources#

Migrated from Firebase Storage to Supabase

Migrate Firebase Storage files to Supabase Storage.

Supabase provides several tools to convert storage files from Firebase Storage to Supabase Storage. Conversion is a two-step process:

Clone the firebase-to-supabase repository:

In the /storage directory, rename supabase-keys-sample.js to supabase-keys.js.

Go to your Supabase project's API settings in the Dashboard.

Copy the Project URL and update the SUPABASE_URL value in supabase-keys.js.

Under Project API keys, copy the service_role key and update the SUPABASE_KEY value in supabase-keys.js.

node download.js <prefix> [<folder>] [<batchSize>] [<limit>] [<token>]

To process in batches using multiple command-line executions, you must use the same parameters with a new <token> on subsequent calls. Use the token displayed on the last call to continue the process at a given point.

node upload.js <prefix> <folder> <bucket>

If the bucket doesn't exist, it's created as a non-public bucket. You must set permissions on this new bucket in the Supabase Dashboard before users can download any files.

Contact us if you need more help migrating your project.

Latest product updates?

Something's not right?

**Examples**:

```text
1git clone https://github.com/supabase-community/firebase-to-supabase.git
```

---

## Migrated from Firebase Storage to Supabase | Supabase Docs

**URL**: https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-storage

**Contents**:
- Migrated from Firebase Storage to Supabase
- Migrate Firebase Storage files to Supabase Storage.
- Set up the migration tool #
- Generate a Firebase private key #
- Command line options#
  - Download Firestore Storage bucket to a local filesystem folder #
  - Upload files to Supabase Storage bucket #
- Resources#

Migrated from Firebase Storage to Supabase

Migrate Firebase Storage files to Supabase Storage.

Supabase provides several tools to convert storage files from Firebase Storage to Supabase Storage. Conversion is a two-step process:

Clone the firebase-to-supabase repository:

In the /storage directory, rename supabase-keys-sample.js to supabase-keys.js.

Go to your Supabase project's API settings in the Dashboard.

Copy the Project URL and update the SUPABASE_URL value in supabase-keys.js.

Under Project API keys, copy the service_role key and update the SUPABASE_KEY value in supabase-keys.js.

node download.js <prefix> [<folder>] [<batchSize>] [<limit>] [<token>]

To process in batches using multiple command-line executions, you must use the same parameters with a new <token> on subsequent calls. Use the token displayed on the last call to continue the process at a given point.

node upload.js <prefix> <folder> <bucket>

If the bucket doesn't exist, it's created as a non-public bucket. You must set permissions on this new bucket in the Supabase Dashboard before users can download any files.

Contact us if you need more help migrating your project.

Latest product updates?

Something's not right?

**Examples**:

```text
1git clone https://github.com/supabase-community/firebase-to-supabase.git
```

---

## Migrated from Firebase Storage to Supabase | Supabase Docs

**URL**: https://supabase.com/docs/guides/migrations/firebase-storage

**Contents**:
- Migrated from Firebase Storage to Supabase
- Migrate Firebase Storage files to Supabase Storage.
- Set up the migration tool #
- Generate a Firebase private key #
- Command line options#
  - Download Firestore Storage bucket to a local filesystem folder #
  - Upload files to Supabase Storage bucket #
- Resources#

Migrated from Firebase Storage to Supabase

Migrate Firebase Storage files to Supabase Storage.

Supabase provides several tools to convert storage files from Firebase Storage to Supabase Storage. Conversion is a two-step process:

Clone the firebase-to-supabase repository:

In the /storage directory, rename supabase-keys-sample.js to supabase-keys.js.

Go to your Supabase project's API settings in the Dashboard.

Copy the Project URL and update the SUPABASE_URL value in supabase-keys.js.

Under Project API keys, copy the service_role key and update the SUPABASE_KEY value in supabase-keys.js.

node download.js <prefix> [<folder>] [<batchSize>] [<limit>] [<token>]

To process in batches using multiple command-line executions, you must use the same parameters with a new <token> on subsequent calls. Use the token displayed on the last call to continue the process at a given point.

node upload.js <prefix> <folder> <bucket>

If the bucket doesn't exist, it's created as a non-public bucket. You must set permissions on this new bucket in the Supabase Dashboard before users can download any files.

Contact us if you need more help migrating your project.

Latest product updates?

Something's not right?

**Examples**:

```text
1git clone https://github.com/supabase-community/firebase-to-supabase.git
```

---

## Self-Hosting | Supabase Docs

**URL**: https://supabase.com/docs/reference/self-hosting-storage/introduction

**Contents**:
- Self-Hosting Storage
  - Client libraries#
  - Additional links#
- Create a bucket
  - Body
  - Response codes
  - Response (200)
- Gets all buckets

An S3 compatible object storage service that integrates with Postgres.

Latest product updates?

Something's not right?

**Examples**:

```text
123{  "name": "avatars"}
```

```text
123456789101112131415[  {    "id": "bucket2",    "name": "bucket2",    "public": false,    "file_size_limit": 1000000,    "allowed_mime_types": [      "image/png",      "image/jpeg"    ],    "owner": "4d56e902-f0a0-4662-8448-a4d9e643c142",    "created_at": "2021-02-17T04:43:32.770206+00:00",    "updated_at": "2021-02-17T04:43:32.770206+00:00"  }]
```

```text
123{  "message": "Empty bucket has been queued. Completion may take up to an hour."}
```

---

## Storage | Supabase Docs

**URL**: https://supabase.com/docs/guides/storage

**Contents**:
- Storage
- Use Supabase to store and serve files.
- Features#
- Examples#
- Resources#

Use Supabase to store and serve files.

Supabase Storage makes it simple to upload and serve files of any size, providing a robust framework for file access controls.

You can use Supabase Storage to store images, videos, documents, and any other file type. Serve your assets with a global CDN to reduce latency from over 285 cities globally. Supabase Storage includes a built-in image optimizer, so you can resize and compress your media files on the fly.

Check out all of the Storage templates and examples in our GitHub repository.

Resumable Uploads with Uppy

Find the source code and documentation in the Supabase GitHub repository.

Latest product updates?

Something's not right?

---
