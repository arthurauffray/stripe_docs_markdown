# The Meter Event Summary object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `aggregated_value` (float)
  Aggregated value of all the events within `start_time` (inclusive) and `end_time` (inclusive). The aggregation strategy is defined on meter via `default_aggregation`.

- `end_time` (timestamp)
  End timestamp for this event summary (exclusive). Must be aligned with minute boundaries.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `meter` (string)
  The meter associated with this event summary.

- `start_time` (timestamp)
  Start timestamp for this event summary (inclusive). Must be aligned with minute boundaries.

### The Meter Event Summary object

```json
{
  "id": "mtrusg_test_6041CMAXJrFdZ56U76ce6L35Hz7xA3Tn58z5sY7bq6gM3XN5bx5Y459D4Xt2E17ko6M86kt7kV3bl5PM7LV59l4sY50b6oU5QD7bY3HP58z5sY7bq6gM3Y57LF2Dr7od3Hb8927gh4Tt4Lo4xO4ge60T81C6Y53gl4QS2D33ft3HC3Xi3Cy3Cy3Cy",
  "object": "billing.meter_event_summary",
  "aggregated_value": 10,
  "end_time": 1711659600,
  "livemode": false,
  "meter": "mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA",
  "start_time": 1711656000
}
```