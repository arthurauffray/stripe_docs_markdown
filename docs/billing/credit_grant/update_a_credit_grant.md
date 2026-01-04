# Update a credit grant

Updates a credit grant.

## Returns

Returns the updated credit grant.

## Parameters

- `id` (string, required)
  Unique identifier for the object.

- `expires_at` (timestamp, optional)
  The time when the billing credits created by this credit grant expire. If set to empty, the billing credits never expire.

- `metadata` (object, optional)
  Set of key-value pairs you can attach to an object. You can use this to store additional information about the object (for example, cost basis) in a structured format.

```curl
curl https://api.stripe.com/v1/billing/credit_grants/credgr_test_61R9rpFu8SZkXPTkU41L6nFOS1ekDKoa \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[cost_basis]"="0.9" \
  -d expires_at=1759302000
```

```cli
stripe billing credit_grants update credgr_test_61R9rpFu8SZkXPTkU41L6nFOS1ekDKoa \
  -d "metadata[cost_basis]"="0.9" \
  --expires-at=1759302000
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

credit_grant = client.v1.billing.credit_grants.update(
  'credgr_test_61R9rpFu8SZkXPTkU41L6nFOS1ekDKoa',
  {
    metadata: {cost_basis: '0.9'},
    expires_at: 1759302000,
  },
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

credit_grant = client.v1.billing.credit_grants.update(
  "credgr_test_61R9rpFu8SZkXPTkU41L6nFOS1ekDKoa",
  {"metadata": {"cost_basis": "0.9"}, "expires_at": 1759302000},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$creditGrant = $stripe->billing->creditGrants->update(
  'credgr_test_61R9rpFu8SZkXPTkU41L6nFOS1ekDKoa',
  [
    'metadata' => ['cost_basis' => '0.9'],
    'expires_at' => 1759302000,
  ]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CreditGrantUpdateParams params =
  CreditGrantUpdateParams.builder()
    .putMetadata("cost_basis", "0.9")
    .setExpiresAt(1759302000L)
    .build();

CreditGrant creditGrant =
  client.v1().billing().creditGrants().update(
    "credgr_test_61R9rpFu8SZkXPTkU41L6nFOS1ekDKoa",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const creditGrant = await stripe.billing.creditGrants.update(
  'credgr_test_61R9rpFu8SZkXPTkU41L6nFOS1ekDKoa',
  {
    metadata: {
      cost_basis: '0.9',
    },
    expires_at: 1759302000,
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.BillingCreditGrantUpdateParams{ExpiresAt: stripe.Int64(1759302000)}
params.AddMetadata("cost_basis", "0.9")
result, err := sc.V1BillingCreditGrants.Update(
  context.TODO(), "credgr_test_61R9rpFu8SZkXPTkU41L6nFOS1ekDKoa", params)
```

```dotnet
var options = new Stripe.Billing.CreditGrantUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "cost_basis", "0.9" } },
    ExpiresAt = DateTimeOffset.FromUnixTimeSeconds(1759302000).UtcDateTime,
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Billing.CreditGrants;
Stripe.Billing.CreditGrant creditGrant = service.Update(
    "credgr_test_61R9rpFu8SZkXPTkU41L6nFOS1ekDKoa",
    options);
```

### Response

```json
{
  "id": "credgr_test_61R9rpFu8SZkXPTkU41L6nFOS1ekDKoa",
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
  "created": 1726688933,
  "customer": "cus_QsEHa3GKweMwih",
  "effective_at": 1726688933,
  "expires_at": 1759302000,
  "livemode": false,
  "metadata": {
    "cost_basis": "0.9"
  },
  "name": "Purchased Credits",
  "priority": 50,
  "test_clock": null,
  "updated": 1726688977,
  "voided_at": null
}
```