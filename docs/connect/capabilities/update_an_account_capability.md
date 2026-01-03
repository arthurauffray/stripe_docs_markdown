# Update an Account Capability

Updates an existing Account Capability. Request or remove a capability by updating its `requested` parameter.

## Returns

Returns an Account Capability object.

## Parameters

- `experimental` (boolean, optional)
  Passing true assigns the experimental onboarding policy to the capability.

- `requested` (boolean, optional)
  To request a new capability for an account, pass true. There can be a delay before the requested capability becomes active. If the capability has any activation requirements, the response includes them in the `requirements` arrays.

  If a capability isn’t permanent, you can remove it from the account by passing false. Some capabilities are permanent after they’ve been requested. Attempting to remove a permanent capability returns an error.

```curl
curl https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/capabilities/card_payments \
  -u "<<YOUR_SECRET_KEY>>" \
  -d requested=true
```

```cli
stripe capabilities update acct_1032D82eZvKYlo2C card_payments \
  --requested=true
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

capability = client.v1.accounts.capabilities.update(
  'acct_1032D82eZvKYlo2C',
  'card_payments',
  {requested: true},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

capability = client.v1.accounts.capabilities.update(
  "acct_1032D82eZvKYlo2C",
  "card_payments",
  {"requested": True},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$capability = $stripe->accounts->updateCapability(
  'acct_1032D82eZvKYlo2C',
  'card_payments',
  ['requested' => true]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AccountCapabilityUpdateParams params =
  AccountCapabilityUpdateParams.builder().setRequested(true).build();

Capability capability =
  client.v1().accounts().capabilities().update(
    "acct_1032D82eZvKYlo2C",
    "card_payments",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const capability = await stripe.accounts.updateCapability(
  'acct_1032D82eZvKYlo2C',
  'card_payments',
  {
    requested: true,
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CapabilityUpdateParams{
  Requested: stripe.Bool(true),
  Account: stripe.String("acct_1032D82eZvKYlo2C"),
}
result, err := sc.V1Capabilities.Update(context.TODO(), "card_payments", params)
```

```dotnet
var options = new AccountCapabilityUpdateOptions { Requested = true };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Accounts.Capabilities;
Capability capability = service.Update(
    "acct_1032D82eZvKYlo2C",
    "card_payments",
    options);
```

### Response

```json
{
  "id": "card_payments",
  "object": "capability",
  "account": "acct_1032D82eZvKYlo2C",
  "future_requirements": {
    "alternatives": [],
    "current_deadline": null,
    "currently_due": [],
    "disabled_reason": null,
    "errors": [],
    "eventually_due": [],
    "past_due": [],
    "pending_verification": []
  },
  "requested": true,
  "requested_at": 1688491010,
  "requirements": {
    "alternatives": [],
    "current_deadline": null,
    "currently_due": [],
    "disabled_reason": null,
    "errors": [],
    "eventually_due": [],
    "past_due": [],
    "pending_verification": []
  },
  "status": "inactive"
}
```