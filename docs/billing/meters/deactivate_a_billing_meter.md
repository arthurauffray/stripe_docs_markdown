# Deactivate a billing meter

When a meter is deactivated, no more meter events will be accepted for this meter. You can’t attach a deactivated meter to a price.

## Returns

Returns a billing meter.

```curl
curl -X POST https://api.stripe.com/v1/billing/meters/mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA/deactivate \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe billing meters deactivate mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

meter = client.v1.billing.meters.deactivate('mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

meter = client.v1.billing.meters.deactivate(
  "mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$meter = $stripe->billing->meters->deactivate(
  'mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

MeterDeactivateParams params = MeterDeactivateParams.builder().build();

Meter meter =
  client.v1().billing().meters().deactivate(
    "mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const meter = await stripe.billing.meters.deactivate(
  'mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.BillingMeterDeactivateParams{}
result, err := sc.V1BillingMeters.Deactivate(
  context.TODO(), "mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Billing.Meters;
Stripe.Billing.Meter meter = service.Deactivate(
    "mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA");
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
    "deactivated_at": 1704898330
  },
  "updated": 1704898330,
  "value_settings": {
    "event_payload_key": "value"
  }
}
```