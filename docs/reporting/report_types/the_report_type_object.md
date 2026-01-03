# The Report Type object

## Attributes

- `id` (string)
  The [ID of the Report Type](https://docs.stripe.com/docs/reporting/statements/api.md#available-report-types), such as `balance.summary.1`.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `data_available_end` (timestamp)
  Most recent time for which this Report Type is available. Measured in seconds since the Unix epoch.

- `data_available_start` (timestamp)
  Earliest time for which this Report Type is available. Measured in seconds since the Unix epoch.

- `default_columns` (array of strings, nullable)
  List of column names that are included by default when this Report Type gets run. (If the Report Type doesn’t support the `columns` parameter, this will be null.)

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `name` (string)
  Human-readable name of the Report Type

- `updated` (timestamp)
  When this Report Type was latest updated. Measured in seconds since the Unix epoch.

- `version` (integer)
  Version of the Report Type. Different versions report with the same ID will have the same purpose, but may take different run parameters or have different result schemas.

### The Report Type object

```json
{
  "id": "balance.summary.1",
  "object": "reporting.report_type",
  "data_available_end": 1695081600,
  "data_available_start": 1667952000,
  "default_columns": [
    "category",
    "description",
    "net_amount",
    "currency"
  ],
  "livemode": false,
  "name": "Balance summary",
  "updated": 1695109133,
  "version": 1
}
```