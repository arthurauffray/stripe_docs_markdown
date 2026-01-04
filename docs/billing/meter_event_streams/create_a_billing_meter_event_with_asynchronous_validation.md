# Create a billing meter event with asynchronous validation

Creates meter events. Events are processed asynchronously, including validation. Requires a meter event session for authentication. Supports up to 10,000 requests per second in livemode. For even higher rate-limits, contact sales.

## Parameters

- `events` (array of objects, required)
  List of meter events to include in the request. Supports up to 100 events per request.

  - `events.event_name` (string, required)
    The name of the meter event. Corresponds with the `event_name` field on a meter.

  - `events.identifier` (string, optional)
    A unique identifier for the event. If not provided, one will be generated. We recommend using a globally unique identifier for this. We’ll enforce uniqueness within a rolling 24 hour period.

  - `events.payload` (map, required)
    The payload of the event. This must contain the fields corresponding to a meter’s `customer_mapping.event_payload_key` (default is `stripe_customer_id`) and `value_settings.event_payload_key` (default is `value`). Read more about the [payload](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage.md#payload-key-overrides).

  - `events.timestamp` (timestamp, optional)
    The time of the event. Must be within the past 35 calendar days or up to 5 minutes in the future. Defaults to current timestamp if not specified.

## Returns

## Error Codes

| HTTP status code | Code                                | Description                              |
| ---------------- | ----------------------------------- | ---------------------------------------- |
| 401              | billing_meter_event_session_expired | The temporary session token has expired. |

```curl
curl -X POST https://meter-events.stripe.com/v2/billing/meter_event_stream \
  -H "Authorization: Bearer {{SESSION AUTH TOKEN}}" \
  -H "Stripe-Version: {{STRIPE_API_VERSION}}" \
  --json '{
    "events": [
        {
            "identifier": "idmp_12345678",
            "event_name": "ai_search_api",
            "timestamp": "2024-06-01T12:00:00.000Z",
            "payload": {
                "stripe_customer_id": "cus_12345678",
                "value": "25"
            }
        }
    ]
  }'
```

```cli
stripe v2 billing meter_event_streams create  \
  --events.identifier=idmp_12345678 \
  --events.event-name=ai_search_api \
  --events.timestamp="2024-06-01T12:00:00.000Z" \
  --events.payload.stripe-customer-id=cus_12345678 \
  --events.payload.value=25
```

```ruby
client = Stripe::StripeClient.new("{{SESSION AUTH TOKEN}}")

empty_object = client.v2.billing.meter_event_stream.create({
  events: [
    {
      identifier: 'idmp_12345678',
      event_name: 'ai_search_api',
      timestamp: '2024-06-01T12:00:00.000Z',
      payload: {
        stripe_customer_id: 'cus_12345678',
        value: '25',
      },
    },
  ],
})
```

```python
client = StripeClient("{{SESSION AUTH TOKEN}}")

empty_object = client.v2.billing.meter_event_stream.create({
  "events": [
    {
      "identifier": "idmp_12345678",
      "event_name": "ai_search_api",
      "timestamp": "2024-06-01T12:00:00.000Z",
      "payload": {"stripe_customer_id": "cus_12345678", "value": "25"},
    },
  ],
})
```

```php
$stripe = new \Stripe\StripeClient('{{SESSION AUTH TOKEN}}');

$emptyObject = $stripe->v2->billing->meterEventStream->create([
  'events' => [
    [
      'identifier' => 'idmp_12345678',
      'event_name' => 'ai_search_api',
      'timestamp' => '2024-06-01T12:00:00.000Z',
      'payload' => [
        'stripe_customer_id' => 'cus_12345678',
        'value' => '25',
      ],
    ],
  ],
]);
```

```java
StripeClient client = new StripeClient("{{SESSION AUTH TOKEN}}");

MeterEventStreamCreateParams params =
  MeterEventStreamCreateParams.builder()
    .addEvent(
      MeterEventStreamCreateParams.Event.builder()
        .setIdentifier("idmp_12345678")
        .setEventName("ai_search_api")
        .setTimestamp(Instant.parse("2024-06-01T12:00:00.000Z"))
        .putPayload("stripe_customer_id", "cus_12345678")
        .putPayload("value", "25")
        .build()
    )
    .build();

client.v2().billing().meterEventStream().create(params);
```

```node
const stripe = require('stripe')('{{SESSION AUTH TOKEN}}');

const emptyObject = await stripe.v2.billing.meterEventStream.create({
  events: [
    {
      identifier: 'idmp_12345678',
      event_name: 'ai_search_api',
      timestamp: '2024-06-01T12:00:00.000Z',
      payload: {
        stripe_customer_id: 'cus_12345678',
        value: '25',
      },
    },
  ],
});
```

```go
sc := stripe.NewClient("{{SESSION AUTH TOKEN}}")
params := &stripe.V2BillingMeterEventStreamCreateParams{
  Events: []*stripe.V2BillingMeterEventStreamCreateEventParams{
    &stripe.V2BillingMeterEventStreamCreateEventParams{
      Identifier: stripe.String("idmp_12345678"),
      EventName: stripe.String("ai_search_api"),
      Timestamp: stripe.Time(time.Now()),
      Payload: map[string]string{
        "stripe_customer_id": "cus_12345678",
        "value": "25",
      },
    },
  },
}
sc.V2BillingMeterEventStreams.Create(context.TODO(), params)
```

```dotnet
var options = new Stripe.V2.Billing.MeterEventStreamCreateOptions
{
    Events = new List<Stripe.V2.Billing.MeterEventStreamCreateEventOptions>
    {
        new Stripe.V2.Billing.MeterEventStreamCreateEventOptions
        {
            Identifier = "idmp_12345678",
            EventName = "ai_search_api",
            Timestamp = DateTimeOffset.Parse("2024-06-01T12:00:00.000Z").UtcDateTime,
            Payload = new Dictionary<string, string>
            {
                { "stripe_customer_id", "cus_12345678" },
                { "value", "25" },
            },
        },
    },
};
var client = new StripeClient("{{SESSION AUTH TOKEN}}");
var service = client.V2.Billing.MeterEventStream;
service.Create(options);
```

### Response

```json
{}
```