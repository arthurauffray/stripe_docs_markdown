# Retrieve a billing meter

Retrieves a billing meter given an ID.

## Returns

Returns a billing meter.

```curl
curl https://api.stripe.com/v1/billing/meters/mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe billing meters retrieve mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

meter = client.v1.billing.meters.retrieve('mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

meter = client.v1.billing.meters.retrieve(
  "mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$meter = $stripe->billing->meters->retrieve(
  'mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

MeterRetrieveParams params = MeterRetrieveParams.builder().build();

Meter meter =
  client.v1().billing().meters().retrieve(
    "mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const meter = await stripe.billing.meters.retrieve(
  'mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.BillingMeterRetrieveParams{}
result, err := sc.V1BillingMeters.Retrieve(
  context.TODO(), "mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Billing.Meters;
Stripe.Billing.Meter meter = service.Get(
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
    "deactivated_at": null
  },
  "updated": 1704898330,
  "value_settings": {
    "event_payload_key": "value"
  }
}
```