# The Alert object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `alert_type` (enum)
  Defines the type of the alert.
Possible enum values:
  - `usage_threshold`
    Use `usage_threshold` if you intend for an alert to fire when a usage threshold on a meter is crossed.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `status` (enum, nullable)
  Status of the alert. This can be active, inactive or archived.

- `title` (string)
  Title of the alert.

- `usage_threshold` (object, nullable)
  Encapsulates configuration of the alert to monitor usage on a specific [Billing Meter](https://docs.stripe.com/docs/api/billing/meter.md).

  - `usage_threshold.filters` (array of objects, nullable)
    The filters allow limiting the scope of this usage alert. You can only specify up to one filter at this time.

    - `usage_threshold.filters.customer` (string, nullable)
      Limit the scope of the alert to this customer ID

  - `usage_threshold.gte` (integer)
    The value at which this alert will trigger.

  - `usage_threshold.meter` (string)
    The [Billing Meter](https://docs.stripe.com/api/billing/meter.md) ID whose usage is monitored.

  - `usage_threshold.recurrence` (enum)
    Defines how the alert will behave.
Possible enum values:
    - `one_time`
      Use `one_time` if you intend for an alert to only fire once in the lifetime of a customer.

### The Alert object

```json
{
  "id": "alrt_12345",
  "object": "billing.alert",
  "title": "API Request usage alert",
  "livemode": true,
  "alert_type": "usage_threshold",
  "usage_threshold": {
    "gte": 10000,
    "meter": "mtr_12345",
    "recurrence": "one_time"
  },
  "status": "active"
}
```