# Create a billing alert

Creates a billing alert

## Returns

Returns a billing alert

## Parameters

- `alert_type` (enum, required)
  The type of alert to create.
Possible enum values:
  - `usage_threshold`
    Use `usage_threshold` if you intend for an alert to fire when a usage threshold on a meter is crossed.

- `title` (string, required)
  The title of the alert.

  The maximum length is 256 characters.

- `usage_threshold` (object, optional)
  The configuration of the usage threshold.

  - `usage_threshold.gte` (integer, required)
    Defines at which value the alert will fire.

  - `usage_threshold.meter` (string, required)
    The [Billing Meter](https://docs.stripe.com/api/billing/meter.md) ID whose usage is monitored.

  - `usage_threshold.recurrence` (enum, required)
    Defines how the alert will behave.
Possible enum values:
    - `one_time`
      Use `one_time` if you intend for an alert to only fire once in the lifetime of a customer.

  - `usage_threshold.filters` (array of objects, optional)
    The filters allows limiting the scope of this usage alert. You can only specify up to one filter at this time.

    - `usage_threshold.filters.type` (enum, required)
      What type of filter is being applied to this usage alert.
Possible enum values:
      - `customer`
        Use `customer` if you intend to filter this alert to a customer.

    - `usage_threshold.filters.customer` (string, optional)
      Limit the scope to this usage alert only to this customer.

```curl
curl https://api.stripe.com/v1/billing/alerts \
  -u "<<YOUR_SECRET_KEY>>" \
  -d title="API Request usage alert" \
  -d alert_type=usage_threshold \
  -d "usage_threshold[gte]"=10000 \
  -d "usage_threshold[meter]"=mtr_12345 \
  -d "usage_threshold[recurrence]"=one_time
```

```cli
stripe billing alerts create  \
  --title="API Request usage alert" \
  --alert-type=usage_threshold \
  -d "usage_threshold[gte]"=10000 \
  -d "usage_threshold[meter]"=mtr_12345 \
  -d "usage_threshold[recurrence]"=one_time
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

alert = client.v1.billing.alerts.create({
  title: 'API Request usage alert',
  alert_type: 'usage_threshold',
  usage_threshold: {
    gte: 10000,
    meter: 'mtr_12345',
    recurrence: 'one_time',
  },
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

alert = client.v1.billing.alerts.create({
  "title": "API Request usage alert",
  "alert_type": "usage_threshold",
  "usage_threshold": {"gte": 10000, "meter": "mtr_12345", "recurrence": "one_time"},
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$alert = $stripe->billing->alerts->create([
  'title' => 'API Request usage alert',
  'alert_type' => 'usage_threshold',
  'usage_threshold' => [
    'gte' => 10000,
    'meter' => 'mtr_12345',
    'recurrence' => 'one_time',
  ],
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AlertCreateParams params =
  AlertCreateParams.builder()
    .setTitle("API Request usage alert")
    .setAlertType(AlertCreateParams.AlertType.USAGE_THRESHOLD)
    .setUsageThreshold(
      AlertCreateParams.UsageThreshold.builder()
        .setGte(10000L)
        .setMeter("mtr_12345")
        .setRecurrence(AlertCreateParams.UsageThreshold.Recurrence.ONE_TIME)
        .build()
    )
    .build();

Alert alert = client.v1().billing().alerts().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const alert = await stripe.billing.alerts.create({
  title: 'API Request usage alert',
  alert_type: 'usage_threshold',
  usage_threshold: {
    gte: 10000,
    meter: 'mtr_12345',
    recurrence: 'one_time',
  },
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.BillingAlertCreateParams{
  Title: stripe.String("API Request usage alert"),
  AlertType: stripe.String("usage_threshold"),
  UsageThreshold: &stripe.BillingAlertCreateUsageThresholdParams{
    GTE: stripe.Int64(10000),
    Meter: stripe.String("mtr_12345"),
    Recurrence: stripe.String("one_time"),
  },
}
result, err := sc.V1BillingAlerts.Create(context.TODO(), params)
```

```dotnet
var options = new Stripe.Billing.AlertCreateOptions
{
    Title = "API Request usage alert",
    AlertType = "usage_threshold",
    UsageThreshold = new Stripe.Billing.AlertUsageThresholdOptions
    {
        Gte = 10000,
        Meter = "mtr_12345",
        Recurrence = "one_time",
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Billing.Alerts;
Stripe.Billing.Alert alert = service.Create(options);
```

### Response

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