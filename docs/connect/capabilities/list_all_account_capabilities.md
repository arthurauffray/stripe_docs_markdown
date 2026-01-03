# List all account capabilities

Returns a list of capabilities associated with the account. The capabilities are returned sorted by creation date, with the most recent capability appearing first.

## Returns

A dictionary with a `data` property that contains an array of the capabilities of this account. Each entry in the array is a separate capability object.

```curl
curl https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/capabilities \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe accounts capabilities acct_1032D82eZvKYlo2C
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

capabilities = client.v1.accounts.capabilities.list('acct_1032D82eZvKYlo2C')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

capabilities = client.v1.accounts.capabilities.list("acct_1032D82eZvKYlo2C")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$capabilities = $stripe->accounts->allCapabilities('acct_1032D82eZvKYlo2C', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AccountCapabilityListParams params = AccountCapabilityListParams.builder().build();

StripeCollection<Capability> stripeCollection =
  client.v1().accounts().capabilities().list("acct_1032D82eZvKYlo2C", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const capabilities = await stripe.accounts.listCapabilities('acct_1032D82eZvKYlo2C');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CapabilityListParams{
  Account: stripe.String("acct_1032D82eZvKYlo2C"),
}
result := sc.V1Capabilities.List(context.TODO(), params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Accounts.Capabilities;
StripeList<Capability> capabilities = service.List("acct_1032D82eZvKYlo2C");
```

### Response

```json
{
  "object": "list",
  "url": "/v1/accounts/acct_1032D82eZvKYlo2C/capabilities",
  "has_more": false,
  "data": [
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
      "requested_at": 1693951912,
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
  ]
}
```