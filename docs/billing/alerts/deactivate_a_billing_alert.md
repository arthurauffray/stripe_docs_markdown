# Deactivate a billing alert

Deactivates this alert, preventing it from triggering.

## Returns

Returns the alert with its updated status.

```curl
curl -X POST https://api.stripe.com/v1/billing/alerts/alrt_12345/deactivate \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe billing alerts deactivate alrt_12345
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

alert = client.v1.billing.alerts.deactivate('alrt_12345')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

alert = client.v1.billing.alerts.deactivate("alrt_12345")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$alert = $stripe->billing->alerts->deactivate('alrt_12345', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AlertDeactivateParams params = AlertDeactivateParams.builder().build();

Alert alert = client.v1().billing().alerts().deactivate("alrt_12345", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const alert = await stripe.billing.alerts.deactivate('alrt_12345');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.BillingAlertDeactivateParams{}
result, err := sc.V1BillingAlerts.Deactivate(context.TODO(), "alrt_12345", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Billing.Alerts;
Stripe.Billing.Alert alert = service.Deactivate("alrt_12345");
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
  "status": "inactive"
}
```