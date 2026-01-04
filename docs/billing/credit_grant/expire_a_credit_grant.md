# Expire a credit grant

Expires a credit grant.

## Returns

Returns the expired credit grant.

## Parameters

- `id` (string, required)
  Unique identifier for the object.

```curl
curl -X POST https://api.stripe.com/v1/billing/credit_grants/credgr_test_61R9rm9vto9SMMvt041L6nFOS1ekDCim/expire \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe billing credit_grants expire credgr_test_61R9rm9vto9SMMvt041L6nFOS1ekDCim
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

credit_grant = client.v1.billing.credit_grants.expire('credgr_test_61R9rm9vto9SMMvt041L6nFOS1ekDCim')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

credit_grant = client.v1.billing.credit_grants.expire(
  "credgr_test_61R9rm9vto9SMMvt041L6nFOS1ekDCim",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$creditGrant = $stripe->billing->creditGrants->expire(
  'credgr_test_61R9rm9vto9SMMvt041L6nFOS1ekDCim',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CreditGrantExpireParams params = CreditGrantExpireParams.builder().build();

CreditGrant creditGrant =
  client.v1().billing().creditGrants().expire(
    "credgr_test_61R9rm9vto9SMMvt041L6nFOS1ekDCim",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const creditGrant = await stripe.billing.creditGrants.expire(
  'credgr_test_61R9rm9vto9SMMvt041L6nFOS1ekDCim'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.BillingCreditGrantExpireParams{}
result, err := sc.V1BillingCreditGrants.Expire(
  context.TODO(), "credgr_test_61R9rm9vto9SMMvt041L6nFOS1ekDCim", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Billing.CreditGrants;
Stripe.Billing.CreditGrant creditGrant = service.Expire(
    "credgr_test_61R9rm9vto9SMMvt041L6nFOS1ekDCim");
```

### Response

```json
{
  "id": "credgr_test_61R9rm9vto9SMMvt041L6nFOS1ekDCim",
  "object": "billing.credit_grant",
  "amount": {
    "monetary": {
      "currency": "usd",
      "value": 1000
    },
    "type": "monetary"
  },
  "applicability_config": {
    "scope": {
      "price_type": "metered"
    }
  },
  "category": "paid",
  "created": 1726688741,
  "customer": "cus_QsEHa3GKweMwih",
  "effective_at": 1726688741,
  "expires_at": 1726688796,
  "livemode": false,
  "metadata": {},
  "name": "Purchased Credits",
  "priority": 50,
  "test_clock": null,
  "updated": 1726688796,
  "voided_at": null
}
```