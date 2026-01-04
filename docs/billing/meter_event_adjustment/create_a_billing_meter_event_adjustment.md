# Create a billing meter event adjustment

Creates a billing meter event adjustment.

## Returns

Returns a billing meter event adjustment.

## Parameters

- `event_name` (string, required)
  The name of the meter event. Corresponds with the `event_name` field on a meter.

  The maximum length is 100 characters.

- `type` (enum, required)
  Specifies whether to cancel a single event or a range of events for a time period. Time period cancellation is not supported yet.
Possible enum values:
  - `cancel`
    Cancel a single meter event by identifier.

- `cancel` (object, optional)
  Specifies which event to cancel.

  - `cancel.identifier` (string, optional)
    Unique identifier for the event. You can only cancel events within 24 hours of Stripe receiving them.

    The maximum length is 100 characters.

```curl
curl https://api.stripe.com/v1/billing/meter_event_adjustments \
  -u "<<YOUR_SECRET_KEY>>" \
  -d type=cancel \
  -d event_name=ai_search_api \
  -d "cancel[identifier]"=identifier_123
```

```cli
stripe billing meter_event_adjustments create  \
  --type=cancel \
  --event-name=ai_search_api \
  -d "cancel[identifier]"=identifier_123
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

meter_event_adjustment = client.v1.billing.meter_event_adjustments.create({
  type: 'cancel',
  event_name: 'ai_search_api',
  cancel: {identifier: 'identifier_123'},
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

meter_event_adjustment = client.v1.billing.meter_event_adjustments.create({
  "type": "cancel",
  "event_name": "ai_search_api",
  "cancel": {"identifier": "identifier_123"},
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$meterEventAdjustment = $stripe->billing->meterEventAdjustments->create([
  'type' => 'cancel',
  'event_name' => 'ai_search_api',
  'cancel' => ['identifier' => 'identifier_123'],
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

MeterEventAdjustmentCreateParams params =
  MeterEventAdjustmentCreateParams.builder()
    .setType(MeterEventAdjustmentCreateParams.Type.CANCEL)
    .setEventName("ai_search_api")
    .setCancel(
      MeterEventAdjustmentCreateParams.Cancel.builder()
        .setIdentifier("identifier_123")
        .build()
    )
    .build();

MeterEventAdjustment meterEventAdjustment =
  client.v1().billing().meterEventAdjustments().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const meterEventAdjustment = await stripe.billing.meterEventAdjustments.create({
  type: 'cancel',
  event_name: 'ai_search_api',
  cancel: {
    identifier: 'identifier_123',
  },
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.BillingMeterEventAdjustmentCreateParams{
  Type: stripe.String("cancel"),
  EventName: stripe.String("ai_search_api"),
  Cancel: &stripe.BillingMeterEventAdjustmentCreateCancelParams{
    Identifier: stripe.String("identifier_123"),
  },
}
result, err := sc.V1BillingMeterEventAdjustments.Create(context.TODO(), params)
```

```dotnet
var options = new Stripe.Billing.MeterEventAdjustmentCreateOptions
{
    Type = "cancel",
    EventName = "ai_search_api",
    Cancel = new Stripe.Billing.MeterEventAdjustmentCancelOptions
    {
        Identifier = "identifier_123",
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Billing.MeterEventAdjustments;
Stripe.Billing.MeterEventAdjustment meterEventAdjustment = service.Create(options);
```

### Response

```json
{
  "object": "billing.meter_event_adjustment",
  "livemode": false,
  "status": "pending",
  "event_name": "ai_search_api",
  "type": "cancel",
  "cancel": {
    "identifier": "identifier_123"
  }
}
```