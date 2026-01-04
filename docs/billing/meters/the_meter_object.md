# The Meter object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `customer_mapping` (object)
  Fields that specify how to map a meter event to a customer.

  - `customer_mapping.event_payload_key` (string)
    The key in the meter event payload to use for mapping the event to a customer.

  - `customer_mapping.type` (enum)
    The method for mapping a meter event to a customer.
Possible enum values:
    - `by_id`
      Map a meter event to a customer by passing a customer ID in the event’s payload.

- `default_aggregation` (object)
  The default settings to aggregate a meter’s events with.

  - `default_aggregation.formula` (enum)
    Specifies how events are aggregated.
Possible enum values:
    - `count`
      Count the number of events.

    - `last`
      Take the last event’s value in the window.

    - `sum`
      Sum each event’s value.

- `display_name` (string)
  The meter’s name.

- `event_name` (string)
  The name of the meter event to record usage for. Corresponds with the `event_name` field on meter events.

- `event_time_window` (enum, nullable)
  The time window which meter events have been pre-aggregated for, if any.
Possible enum values:
  - `day`
    Events are pre-aggregated in daily buckets.

  - `hour`
    Events are pre-aggregated in hourly buckets.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `status` (enum)
  The meter’s status.
Possible enum values:
  - `active`
    The meter is active.

  - `inactive`
    The meter is inactive. No more events for this meter will be accepted. The meter cannot be attached to a price.

- `status_transitions` (object)
  The timestamps at which the meter status changed.

  - `status_transitions.deactivated_at` (timestamp, nullable)
    The time the meter was deactivated, if any. Measured in seconds since Unix epoch.

- `updated` (timestamp)
  Time at which the object was last updated. Measured in seconds since the Unix epoch.

- `value_settings` (object)
  Fields that specify how to calculate a meter event’s value.

  - `value_settings.event_payload_key` (string)
    The key in the meter event payload to use as the value for this meter.

### The Meter object

```json
{
  "id": "mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA",
  "object": "billing.meter",
  "created": 1704824589,
  "customer_mapping": {
    "type": "by_id",
    "event_payload_key": "stripe_customer_id"
  },
  "default_aggregation": {
    "formula": "sum"
  },
  "display_name": "Search API Calls",
  "event_name": "ai_search_api",
  "event_time_window": null,
  "livemode": false,
  "status": "active",
  "status_transitions": {
    "deactivated_at": null
  },
  "updated": 1704898330,
  "value_settings": {
    "event_payload_key": "value"
  }
}
```