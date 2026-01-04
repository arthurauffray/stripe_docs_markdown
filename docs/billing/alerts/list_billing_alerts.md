# List billing alerts

Lists billing active and inactive alerts

## Returns

Returns a list of billing alerts

## Parameters

- `alert_type` (enum, optional)
  Filter results to only include this type of alert.
Possible enum values:
  - `usage_threshold`
    Use `usage_threshold` if you intend for an alert to fire when a usage threshold on a meter is crossed.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `meter` (string, optional)
  Filter results to only include alerts with the given meter.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl https://api.stripe.com/v1/billing/alerts \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe billing alerts list
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

alerts = client.v1.billing.alerts.list()
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

alerts = client.v1.billing.alerts.list()
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$alerts = $stripe->billing->alerts->all([]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AlertListParams params = AlertListParams.builder().build();

StripeCollection<Alert> stripeCollection =
  client.v1().billing().alerts().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const alerts = await stripe.billing.alerts.list();
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.BillingAlertListParams{}
result := sc.V1BillingAlerts.List(context.TODO(), params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Billing.Alerts;
StripeList<Stripe.Billing.Alert> alerts = service.List();
```

### Response

```json
{
  "data": [
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
    },
    {
      "id": "alrt_67890",
      "object": "billing.alert",
      "title": "API Request usage alert",
      "livemode": true,
      "alert_type": "usage_threshold",
      "usage_threshold": {
        "gte": 120,
        "meter": "mtr_67890",
        "recurrence": "one_time"
      },
      "status": "active"
    }
  ]
}
```