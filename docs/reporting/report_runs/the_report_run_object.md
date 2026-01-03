# The Report Run object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `error` (string, nullable)
  If something should go wrong during the run, a message about the failure (populated when `status=failed`).

- `livemode` (boolean)
  `true` if the report is run on live mode data and `false` if it is run on test mode data.

- `parameters` (object)
  Parameters of this report run.

  - `parameters.columns` (array of strings, nullable)
    The set of output columns requested for inclusion in the report run.

  - `parameters.connected_account` (string, nullable)
    Connected account ID by which to filter the report run.

  - `parameters.currency` (enum, nullable)
    Currency of objects to be included in the report run.

  - `parameters.interval_end` (timestamp, nullable)
    Ending timestamp of data to be included in the report run. Can be any UTC timestamp between 1 second after the user specified `interval_start` and 1 second before this report’s last `data_available_end` value.

  - `parameters.interval_start` (timestamp, nullable)
    Starting timestamp of data to be included in the report run. Can be any UTC timestamp between 1 second after this report’s `data_available_start` and 1 second before the user specified `interval_end` value.

  - `parameters.payout` (string, nullable)
    Payout ID by which to filter the report run.

  - `parameters.reporting_category` (string, nullable)
    Category of balance transactions to be included in the report run.

  - `parameters.timezone` (string, nullable)
    Defaults to `Etc/UTC`. The output timezone for all timestamps in the report. A list of possible time zone values is maintained at the [IANA Time Zone Database](http://www.iana.org/time-zones). Has no effect on `interval_start` or `interval_end`.

- `report_type` (string)
  The ID of the [report type](https://docs.stripe.com/docs/reports/report-types.md) to run, such as `"balance.summary.1"`.

- `result` (object, nullable)
  The file object representing the result of the report run (populated when `status=succeeded`).

  - `result.id` (string)
    Unique identifier for the object.

  - `result.object` (string)
    String representing the object’s type. Objects of the same type share the same value.

  - `result.created` (timestamp)
    Time at which the object was created. Measured in seconds since the Unix epoch.

  - `result.expires_at` (timestamp, nullable)
    The file expires and isn’t available at this time in epoch seconds.

  - `result.filename` (string, nullable)
    The suitable name for saving the file to a filesystem.

  - `result.links` (object, nullable)
    A list of [file links](https://docs.stripe.com/api/reporting/report_run/object.md#file_links) that point at this file.

    - `result.links.object` (string)
      String representing the object’s type. Objects of the same type share the same value. Always has the value `list`.

    - `result.links.data` (array of objects)
      Details about each object.

      - `result.links.data.id` (string)
        Unique identifier for the object.

      - `result.links.data.object` (string)
        String representing the object’s type. Objects of the same type share the same value.

      - `result.links.data.created` (timestamp)
        Time at which the object was created. Measured in seconds since the Unix epoch.

      - `result.links.data.expired` (boolean)
        Returns if the link is already expired.

      - `result.links.data.expires_at` (timestamp, nullable)
        Time that the link expires.

      - `result.links.data.file` (string)
        The file object this link points to.

      - `result.links.data.livemode` (boolean)
        Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

      - `result.links.data.metadata` (object)
        Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

      - `result.links.data.url` (string, nullable)
        The publicly accessible URL to download the file.

    - `result.links.has_more` (boolean)
      True if this list has another page of items after this one that can be fetched.

    - `result.links.url` (string)
      The URL where this list can be accessed.

  - `result.purpose` (enum)
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

  - `result.size` (integer)
    The size of the file object in bytes.

  - `result.title` (string, nullable)
    A suitable title for the document.

  - `result.type` (string, nullable)
    The returned file type (for example, `csv`, `pdf`, `jpg`, or `png`).

  - `result.url` (string, nullable)
    Use your live secret API key to download the file from this URL.

- `status` (string)
  Status of this report run. This will be `pending` when the run is initially created. When the run finishes, this will be set to `succeeded` and the `result` field will be populated. Rarely, we may encounter an error, at which point this will be set to `failed` and the `error` field will be populated.

- `succeeded_at` (timestamp, nullable)
  Timestamp at which this run successfully finished (populated when `status=succeeded`). Measured in seconds since the Unix epoch.

### The Report Run object

```json
{
  "id": "frr_1MrQwrLkdIwHu7ixUov4x2b3",
  "object": "reporting.report_run",
  "created": 1680203749,
  "error": null,
  "livemode": false,
  "parameters": {
    "interval_end": 1680100000,
    "interval_start": 1680000000
  },
  "report_type": "balance.summary.1",
  "result": null,
  "status": "pending",
  "succeeded_at": null
}
```