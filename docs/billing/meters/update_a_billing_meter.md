# Update a billing meter

Updates a billing meter.

## Returns

Returns a billing meter.

## Parameters

- `display_name` (string, optional)
  The meter’s name. Not visible to the customer.

  The maximum length is 250 characters.

```curl
curl https://api.stripe.com/v1/billing/meters/mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA \
  -u "<<YOUR_SECRET_KEY>>" \
  -d display_name="Updated Display Name"
```

```cli
stripe billing meters update mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA \
  --display-name="Updated Display Name"
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

meter = client.v1.billing.meters.update(
  'mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA',
  {display_name: 'Updated Display Name'},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

meter = client.v1.billing.meters.update(
  "mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA",
  {"display_name": "Updated Display Name"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$meter = $stripe->billing->meters->update(
  'mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA',
  ['display_name' => 'Updated Display Name']
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

MeterUpdateParams params =
  MeterUpdateParams.builder().setDisplayName("Updated Display Name").build();

Meter meter =
  client.v1().billing().meters().update(
    "mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const meter = await stripe.billing.meters.update(
  'mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA',
  {
    display_name: 'Updated Display Name',
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.BillingMeterUpdateParams{
  DisplayName: stripe.String("Updated Display Name"),
}
result, err := sc.V1BillingMeters.Update(
  context.TODO(), "mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA", params)
```

```dotnet
var options = new Stripe.Billing.MeterUpdateOptions
{
    DisplayName = "Updated Display Name",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Billing.Meters;
Stripe.Billing.Meter meter = service.Update(
    "mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA",
    options);
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
  "display_name": "Updated Display Name",
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