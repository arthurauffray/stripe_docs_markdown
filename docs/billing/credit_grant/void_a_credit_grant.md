# Void a credit grant

Voids a credit grant.

## Returns

Returns the voided credit grant.

## Parameters

- `id` (string, required)
  Unique identifier for the object.

```curl
curl -X POST https://api.stripe.com/v1/billing/credit_grants/credgr_test_61R9rnNTDmZ657a2r41L6nFOS1ekD5Ae/void \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe billing credit_grants void_grant credgr_test_61R9rnNTDmZ657a2r41L6nFOS1ekD5Ae
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

credit_grant = client.v1.billing.credit_grants.void_grant('credgr_test_61R9rnNTDmZ657a2r41L6nFOS1ekD5Ae')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

credit_grant = client.v1.billing.credit_grants.void_grant(
  "credgr_test_61R9rnNTDmZ657a2r41L6nFOS1ekD5Ae",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$creditGrant = $stripe->billing->creditGrants->voidGrant(
  'credgr_test_61R9rnNTDmZ657a2r41L6nFOS1ekD5Ae',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CreditGrantVoidGrantParams params = CreditGrantVoidGrantParams.builder().build();

CreditGrant creditGrant =
  client.v1().billing().creditGrants().voidGrant(
    "credgr_test_61R9rnNTDmZ657a2r41L6nFOS1ekD5Ae",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const creditGrant = await stripe.billing.creditGrants.voidGrant(
  'credgr_test_61R9rnNTDmZ657a2r41L6nFOS1ekD5Ae'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.BillingCreditGrantVoidGrantParams{}
result, err := sc.V1BillingCreditGrants.VoidGrant(
  context.TODO(), "credgr_test_61R9rnNTDmZ657a2r41L6nFOS1ekD5Ae", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Billing.CreditGrants;
Stripe.Billing.CreditGrant creditGrant = service.VoidGrant(
    "credgr_test_61R9rnNTDmZ657a2r41L6nFOS1ekD5Ae");
```

### Response

```json
{
  "id": "credgr_test_61R9rnNTDmZ657a2r41L6nFOS1ekD5Ae",
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
  "created": 1726688817,
  "customer": "cus_QsEHa3GKweMwih",
  "effective_at": 1726688817,
  "expires_at": null,
  "livemode": false,
  "metadata": {},
  "name": "Purchased Credits",
  "priority": 50,
  "test_clock": null,
  "updated": 1726688829,
  "voided_at": 1726688829
}
```