# The MeterEventAdjustment object

## Attributes

- `id` (string)
  The unique id of this meter event adjustment.

- `object` (string, value is "v2.billing.meter_event_adjustment")
  String representing the object’s type. Objects of the same type share the same value of the object field.

- `cancel` (object)
  Specifies which event to cancel.

  - `cancel.identifier` (string)
    Unique identifier for the event. You can only cancel events within 24 hours of Stripe receiving them.

- `created` (timestamp)
  The time the adjustment was created.

- `event_name` (string)
  The name of the meter event. Corresponds with the `event_name` field on a meter.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `status` (enum)
  The meter event adjustment’s status.
Possible enum values:
  - `complete`
    The event adjustment has been processed.

  - `pending`
    The event adjustment is still being processed.

- `type` (enum)
  Specifies whether to cancel a single event or a range of events for a time period. Time period cancellation is not supported yet.
Possible enum values:
  - `cancel`
    Cancel a single meter event by identifier.

### The MeterEventAdjustment object

```json
{
  "object": "v2.billing.meter_event_adjustment",
  "id": "mtr_event_adj_12345678",
  "livemode": false,
  "created": "2024-06-01T12:00:00.000Z",
  "status": "pending",
  "event_name": "ai_search_api",
  "type": "cancel",
  "cancel": {
    "identifier": "idmp_12345678"
  }
}
```