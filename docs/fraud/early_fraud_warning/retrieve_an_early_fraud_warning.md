# Retrieve an early fraud warning

Retrieves the details of an early fraud warning that has previously been created.

Please refer to the [early fraud warning](https://docs.stripe.com/api/radar/early_fraud_warnings/retrieve.md#early_fraud_warning_object) object reference for more details.

## Returns

Returns an EarlyFraudWarning if a valid identifier was provided.

```curl
curl https://api.stripe.com/v1/radar/early_fraud_warnings/issfr_1NnrwHBw2dPENLoi9lnhV3RQ \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe radar early_fraud_warnings retrieve issfr_1NnrwHBw2dPENLoi9lnhV3RQ
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

early_fraud_warning = client.v1.radar.early_fraud_warnings.retrieve('issfr_1NnrwHBw2dPENLoi9lnhV3RQ')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

early_fraud_warning = client.v1.radar.early_fraud_warnings.retrieve(
  "issfr_1NnrwHBw2dPENLoi9lnhV3RQ",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$earlyFraudWarning = $stripe->radar->earlyFraudWarnings->retrieve(
  'issfr_1NnrwHBw2dPENLoi9lnhV3RQ',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

EarlyFraudWarningRetrieveParams params =
  EarlyFraudWarningRetrieveParams.builder().build();

EarlyFraudWarning earlyFraudWarning =
  client.v1().radar().earlyFraudWarnings().retrieve(
    "issfr_1NnrwHBw2dPENLoi9lnhV3RQ",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const earlyFraudWarning = await stripe.radar.earlyFraudWarnings.retrieve(
  'issfr_1NnrwHBw2dPENLoi9lnhV3RQ'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.RadarEarlyFraudWarningRetrieveParams{}
result, err := sc.V1RadarEarlyFraudWarnings.Retrieve(
  context.TODO(), "issfr_1NnrwHBw2dPENLoi9lnhV3RQ", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Radar.EarlyFraudWarnings;
Stripe.Radar.EarlyFraudWarning earlyFraudWarning = service.Get(
    "issfr_1NnrwHBw2dPENLoi9lnhV3RQ");
```

### Response

```json
{
  "id": "issfr_1NnrwHBw2dPENLoi9lnhV3RQ",
  "object": "radar.early_fraud_warning",
  "actionable": true,
  "charge": "ch_1234",
  "created": 123456789,
  "fraud_type": "misc",
  "livemode": false
}
```