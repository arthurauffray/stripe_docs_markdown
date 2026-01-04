# List all early fraud warnings

Returns a list of early fraud warnings.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` EarlyFraudWarnings, starting after EarlyFraudWarnings `starting_after`. Each entry in the array is a separate EarlyFraudWarning object. If no more EarlyFraudWarnings are available, the resulting array will be empty.

## Parameters

- `charge` (string, optional)
  Only return early fraud warnings for the charge specified by this charge ID.

- `created` (object, optional)
  Only return early fraud warnings that were created during the given date interval.

  - `created.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `created.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `created.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `created.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `payment_intent` (string, optional)
  Only return early fraud warnings for charges that were created by the PaymentIntent specified by this PaymentIntent ID.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/radar/early_fraud_warnings \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe radar early_fraud_warnings list  \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

early_fraud_warnings = client.v1.radar.early_fraud_warnings.list({limit: 3})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

early_fraud_warnings = client.v1.radar.early_fraud_warnings.list({"limit": 3})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$earlyFraudWarnings = $stripe->radar->earlyFraudWarnings->all(['limit' => 3]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

EarlyFraudWarningListParams params =
  EarlyFraudWarningListParams.builder().setLimit(3L).build();

StripeCollection<EarlyFraudWarning> stripeCollection =
  client.v1().radar().earlyFraudWarnings().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const earlyFraudWarnings = await stripe.radar.earlyFraudWarnings.list({
  limit: 3,
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.RadarEarlyFraudWarningListParams{}
params.Limit = stripe.Int64(3)
result := sc.V1RadarEarlyFraudWarnings.List(context.TODO(), params)
```

```dotnet
var options = new Stripe.Radar.EarlyFraudWarningListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Radar.EarlyFraudWarnings;
StripeList<Stripe.Radar.EarlyFraudWarning> earlyFraudWarnings = service.List(
    options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/radar/early_fraud_warnings",
  "has_more": false,
  "data": [
    {
      "id": "issfr_1NnrwHBw2dPENLoi9lnhV3RQ",
      "object": "radar.early_fraud_warning",
      "actionable": true,
      "charge": "ch_1234",
      "created": 123456789,
      "fraud_type": "misc",
      "livemode": false
    }
  ]
}
```