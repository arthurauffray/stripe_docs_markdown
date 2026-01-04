# Retrieve a credit grant

Retrieves a credit grant.

## Returns

Returns a credit grant.

## Parameters

- `id` (string, required)
  Unique identifier for the object.

```curl
curl https://api.stripe.com/v1/billing/credit_grants/credgr_test_61R9a6NUWsRmOW3RM41L6nFOS1ekDGHo \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe billing credit_grants retrieve credgr_test_61R9a6NUWsRmOW3RM41L6nFOS1ekDGHo
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

credit_grant = client.v1.billing.credit_grants.retrieve('credgr_test_61R9a6NUWsRmOW3RM41L6nFOS1ekDGHo')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

credit_grant = client.v1.billing.credit_grants.retrieve(
  "credgr_test_61R9a6NUWsRmOW3RM41L6nFOS1ekDGHo",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$creditGrant = $stripe->billing->creditGrants->retrieve(
  'credgr_test_61R9a6NUWsRmOW3RM41L6nFOS1ekDGHo',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CreditGrantRetrieveParams params = CreditGrantRetrieveParams.builder().build();

CreditGrant creditGrant =
  client.v1().billing().creditGrants().retrieve(
    "credgr_test_61R9a6NUWsRmOW3RM41L6nFOS1ekDGHo",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const creditGrant = await stripe.billing.creditGrants.retrieve(
  'credgr_test_61R9a6NUWsRmOW3RM41L6nFOS1ekDGHo'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.BillingCreditGrantRetrieveParams{}
result, err := sc.V1BillingCreditGrants.Retrieve(
  context.TODO(), "credgr_test_61R9a6NUWsRmOW3RM41L6nFOS1ekDGHo", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Billing.CreditGrants;
Stripe.Billing.CreditGrant creditGrant = service.Get(
    "credgr_test_61R9a6NUWsRmOW3RM41L6nFOS1ekDGHo");
```

### Response

```json
{
  "id": "credgr_test_61R9a6NUWsRmOW3RM41L6nFOS1ekDGHo",
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
  "created": 1726620803,
  "customer": "cus_QrvQguzkIK8zTj",
  "effective_at": 1729297860,
  "expires_at": null,
  "livemode": false,
  "metadata": {},
  "name": "Purchased Credits",
  "priority": 50,
  "test_clock": null,
  "updated": 1726620803
}
```