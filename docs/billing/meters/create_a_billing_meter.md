# Create a billing meter

Creates a billing meter.

## Returns

Returns a billing meter.

## Parameters

- `default_aggregation` (object, required)
  The default settings to aggregate a meter’s events with.

  - `default_aggregation.formula` (enum, required)
    Specifies how events are aggregated. Allowed values are `count` to count the number of events, `sum` to sum each event’s value and `last` to take the last event’s value in the window.
Possible enum values:
    - `count`
      Count the number of events.

    - `last`
      Take the last event’s value in the window.

    - `sum`
      Sum each event’s value.

- `display_name` (string, required)
  The meter’s name. Not visible to the customer.

  The maximum length is 250 characters.

- `event_name` (string, required)
  The name of the meter event to record usage for. Corresponds with the `event_name` field on meter events.

  The maximum length is 100 characters.

- `customer_mapping` (object, optional)
  Fields that specify how to map a meter event to a customer.

  - `customer_mapping.event_payload_key` (string, required)
    The key in the meter event payload to use for mapping the event to a customer.

    The maximum length is 100 characters.

  - `customer_mapping.type` (enum, required)
    The method for mapping a meter event to a customer. Must be `by_id`.
Possible enum values:
    - `by_id`
      Map a meter event to a customer by passing a customer ID in the event’s payload.

- `event_time_window` (enum, optional)
  The time window which meter events have been pre-aggregated for, if any.
Possible enum values:
  - `day`
    Events are pre-aggregated in daily buckets.

  - `hour`
    Events are pre-aggregated in hourly buckets.

- `value_settings` (object, optional)
  Fields that specify how to calculate a meter event’s value.

  - `value_settings.event_payload_key` (string, required)
    The key in the usage event payload to use as the value for this meter. For example, if the event payload contains usage on a `bytes_used` field, then set the event_payload_key to “bytes_used”.

    The maximum length is 100 characters.

```curl
curl https://api.stripe.com/v1/billing/meters \
  -u "<<YOUR_SECRET_KEY>>" \
  -d display_name="Search API Calls" \
  -d event_name=ai_search_api \
  -d "default_aggregation[formula]"=sum \
  -d "value_settings[event_payload_key]"=value \
  -d "customer_mapping[type]"=by_id \
  -d "customer_mapping[event_payload_key]"=stripe_customer_id
```

```cli
stripe billing meters create  \
  --display-name="Search API Calls" \
  --event-name=ai_search_api \
  -d "default_aggregation[formula]"=sum \
  -d "value_settings[event_payload_key]"=value \
  -d "customer_mapping[type]"=by_id \
  -d "customer_mapping[event_payload_key]"=stripe_customer_id
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

meter = client.v1.billing.meters.create({
  display_name: 'Search API Calls',
  event_name: 'ai_search_api',
  default_aggregation: {formula: 'sum'},
  value_settings: {event_payload_key: 'value'},
  customer_mapping: {
    type: 'by_id',
    event_payload_key: 'stripe_customer_id',
  },
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

meter = client.v1.billing.meters.create({
  "display_name": "Search API Calls",
  "event_name": "ai_search_api",
  "default_aggregation": {"formula": "sum"},
  "value_settings": {"event_payload_key": "value"},
  "customer_mapping": {"type": "by_id", "event_payload_key": "stripe_customer_id"},
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$meter = $stripe->billing->meters->create([
  'display_name' => 'Search API Calls',
  'event_name' => 'ai_search_api',
  'default_aggregation' => ['formula' => 'sum'],
  'value_settings' => ['event_payload_key' => 'value'],
  'customer_mapping' => [
    'type' => 'by_id',
    'event_payload_key' => 'stripe_customer_id',
  ],
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

MeterCreateParams params =
  MeterCreateParams.builder()
    .setDisplayName("Search API Calls")
    .setEventName("ai_search_api")
    .setDefaultAggregation(
      MeterCreateParams.DefaultAggregation.builder()
        .setFormula(MeterCreateParams.DefaultAggregation.Formula.SUM)
        .build()
    )
    .setValueSettings(
      MeterCreateParams.ValueSettings.builder().setEventPayloadKey("value").build()
    )
    .setCustomerMapping(
      MeterCreateParams.CustomerMapping.builder()
        .setType(MeterCreateParams.CustomerMapping.Type.BY_ID)
        .setEventPayloadKey("stripe_customer_id")
        .build()
    )
    .build();

Meter meter = client.v1().billing().meters().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const meter = await stripe.billing.meters.create({
  display_name: 'Search API Calls',
  event_name: 'ai_search_api',
  default_aggregation: {
    formula: 'sum',
  },
  value_settings: {
    event_payload_key: 'value',
  },
  customer_mapping: {
    type: 'by_id',
    event_payload_key: 'stripe_customer_id',
  },
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.BillingMeterCreateParams{
  DisplayName: stripe.String("Search API Calls"),
  EventName: stripe.String("ai_search_api"),
  DefaultAggregation: &stripe.BillingMeterCreateDefaultAggregationParams{
    Formula: stripe.String(stripe.BillingMeterDefaultAggregationFormulaSum),
  },
  ValueSettings: &stripe.BillingMeterCreateValueSettingsParams{
    EventPayloadKey: stripe.String("value"),
  },
  CustomerMapping: &stripe.BillingMeterCreateCustomerMappingParams{
    Type: stripe.String("by_id"),
    EventPayloadKey: stripe.String("stripe_customer_id"),
  },
}
result, err := sc.V1BillingMeters.Create(context.TODO(), params)
```

```dotnet
var options = new Stripe.Billing.MeterCreateOptions
{
    DisplayName = "Search API Calls",
    EventName = "ai_search_api",
    DefaultAggregation = new Stripe.Billing.MeterDefaultAggregationOptions
    {
        Formula = "sum",
    },
    ValueSettings = new Stripe.Billing.MeterValueSettingsOptions
    {
        EventPayloadKey = "value",
    },
    CustomerMapping = new Stripe.Billing.MeterCustomerMappingOptions
    {
        Type = "by_id",
        EventPayloadKey = "stripe_customer_id",
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Billing.Meters;
Stripe.Billing.Meter meter = service.Create(options);
```

### Response

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
  "updated": 1704824589,
  "value_settings": {
    "event_payload_key": "value"
  }
}
```