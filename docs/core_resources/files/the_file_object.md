# The File object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `expires_at` (timestamp, nullable)
  The file expires and isn’t available at this time in epoch seconds.

- `filename` (string, nullable)
  The suitable name for saving the file to a filesystem.

- `links` (object, nullable)
  A list of [file links](https://docs.stripe.com/api/files/object.md#file_links) that point at this file.

  - `links.object` (string)
    String representing the object’s type. Objects of the same type share the same value. Always has the value `list`.

  - `links.data` (array of objects)
    Details about each object.

    - `links.data.id` (string)
      Unique identifier for the object.

    - `links.data.object` (string)
      String representing the object’s type. Objects of the same type share the same value.

    - `links.data.created` (timestamp)
      Time at which the object was created. Measured in seconds since the Unix epoch.

    - `links.data.expired` (boolean)
      Returns if the link is already expired.

    - `links.data.expires_at` (timestamp, nullable)
      Time that the link expires.

    - `links.data.file` (string)
      The file object this link points to.

    - `links.data.livemode` (boolean)
      Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

    - `links.data.metadata` (object)
      Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

    - `links.data.url` (string, nullable)
      The publicly accessible URL to download the file.

  - `links.has_more` (boolean)
    True if this list has another page of items after this one that can be fetched.

  - `links.url` (string)
    The URL where this list can be accessed.

- `purpose` (enum)
  The [purpose](https://docs.stripe.com/docs/file-upload.md#uploading-a-file) of the uploaded file.
Possible enum values:
  - `account_requirement`
    Additional documentation requirements that can be requested for an account.

  - `additional_verification`
    Additional verification for custom accounts.

  - `business_icon`
    A business icon.

  - `business_logo`
    A business logo.

  - `customer_signature`
    Customer signature image.

  - `dispute_evidence`
    Evidence to submit with a dispute response.

  - `finance_report_run`
    User-accessible copies of query results from the Reporting dataset.

  - `financial_account_statement`
    Financial account statements.

  - `identity_document`
    A document to verify the identity of an account owner during account provisioning.

  - `identity_document_downloadable`
    Image of a document collected by Stripe Identity.

  - `issuing_regulatory_reporting`
    Additional regulatory reporting requirements for Issuing.

  - `pci_document`
    A self-assessment PCI questionnaire.

  - `platform_terms_of_service`
    A copy of the platform’s Terms of Service.

  - `selfie`
    Image of a selfie collected by Stripe Identity.

  - `sigma_scheduled_query`
    Sigma scheduled query file for export and download.

  - `tax_document_user_upload`
    A user-uploaded tax document.

  - `terminal_android_apk`
    Android POS apps to be deployed on Stripe smart readers.

  - `terminal_reader_splashscreen`
    Splashscreen to be displayed on Terminal readers.

- `size` (integer)
  The size of the file object in bytes.

- `title` (string, nullable)
  A suitable title for the document.

- `type` (string, nullable)
  The returned file type (for example, `csv`, `pdf`, `jpg`, or `png`).

- `url` (string, nullable)
  Use your live secret API key to download the file from this URL.

### The File object

```json
{
  "id": "file_1Mr4LDLkdIwHu7ixFCz0dZiH",
  "object": "file",
  "created": 1680116847,
  "expires_at": 1703444847,
  "filename": "file.png",
  "links": {
    "object": "list",
    "data": [],
    "has_more": false,
    "url": "/v1/file_links?file=file_1Mr4LDLkdIwHu7ixFCz0dZiH"
  },
  "purpose": "dispute_evidence",
  "size": 8429,
  "title": null,
  "type": "png",
  "url": "https://files.stripe.com/v1/files/file_1Mr4LDLkdIwHu7ixFCz0dZiH/contents"
}
```