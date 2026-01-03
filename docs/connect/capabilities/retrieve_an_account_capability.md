# Retrieve an Account Capability

Retrieves information about the specified Account Capability.

## Returns

Returns an Account Capability object.

```curl
curl https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/capabilities/card_payments \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe capabilities retrieve acct_1032D82eZvKYlo2C card_payments
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

capability = client.v1.accounts.capabilities.retrieve(
  'acct_1032D82eZvKYlo2C',
  'card_payments',
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

capability = client.v1.accounts.capabilities.retrieve(
  "acct_1032D82eZvKYlo2C",
  "card_payments",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$capability = $stripe->accounts->retrieveCapability(
  'acct_1032D82eZvKYlo2C',
  'card_payments',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AccountCapabilityRetrieveParams params =
  AccountCapabilityRetrieveParams.builder().build();

Capability capability =
  client.v1().accounts().capabilities().retrieve(
    "acct_1032D82eZvKYlo2C",
    "card_payments",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const capability = await stripe.accounts.retrieveCapability(
  'acct_1032D82eZvKYlo2C',
  'card_payments'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CapabilityRetrieveParams{
  Account: stripe.String("acct_1032D82eZvKYlo2C"),
}
result, err := sc.V1Capabilities.Retrieve(context.TODO(), "card_payments", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Accounts.Capabilities;
Capability capability = service.Get("acct_1032D82eZvKYlo2C", "card_payments");
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