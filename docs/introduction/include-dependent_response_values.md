# Include-dependent response values (API v2)

Some API v2 responses contain null values for certain properties by default, regardless of their actual values. That reduces the size of response payloads while maintaining the basic response structure. To retrieve the actual values for those properties, specify them in the `include` array request parameter.

To determine whether you need to use the `include` parameter in a given request, look at the request description. The `include` parameter’s enum values represent the response properties that depend on the `include` parameter.

## Note

Whether a response property defaults to null depends on the request endpoint, not the object that the endpoint references. If multiple endpoints return data from the same object, a particular property can depend on `include` in one endpoint and return its actual value by default for a different endpoint.

A hash property can depend on a single `include` value, or on multiple `include` values associated with its child properties. For example, when updating an Account, to return actual values for the entire `identity` hash, specify `identity` in the `include` parameter. Otherwise, the `identity` hash is null in the response. However, to return actual values for the `configuration` hash, you must specify individual configurations in the request. If you specify at least one configuration, but not all of them, specified configurations return actual values and unspecified configurations return null. If you don’t specify any configurations, the `configuration` hash is null in the response.

```curl
curl -X POST https://api.stripe.com/v2/core/accounts \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: {{STRIPE_API_VERSION}}" \
  --json '{
    "include": [
        "identity",
        "configuration.customer"
    ]
  }'
```

```cli
stripe v2 core accounts create  \
  --include=identity \
  --include="configuration.customer"
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

account = client.v2.core.accounts.create({
  include: ['identity', 'configuration.customer'],
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

account = client.v2.core.accounts.create({
  "include": ["identity", "configuration.customer"],
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$account = $stripe->v2->core->accounts->create([
  'include' => ['identity', 'configuration.customer'],
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AccountCreateParams params =
  AccountCreateParams.builder()
    .addInclude(AccountCreateParams.Include.IDENTITY)
    .addInclude(AccountCreateParams.Include.CONFIGURATION__CUSTOMER)
    .build();

Account account = client.v2().core().accounts().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const account = await stripe.v2.core.accounts.create({
  include: ['identity', 'configuration.customer'],
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.V2CoreAccountCreateParams{
  Include: []*string{
    stripe.String("identity"),
    stripe.String("configuration.customer"),
  },
}
result, err := sc.V2CoreAccounts.Create(context.TODO(), params)
```

```dotnet
var options = new Stripe.V2.Core.AccountCreateOptions
{
    Include = new List<string> { "identity", "configuration.customer" },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V2.Core.Accounts;
Stripe.V2.Core.Account account = service.Create(options);
```

## Included response properties

The response includes actual values for the properties specified in the `include` parameter, and null for all other include-dependent properties.

### Response

```json
{
  "id": "acct_123",
  "object": "v2.core.account",
  "applied_configurations": [
    "customer",
    "merchant"
  ],
  "configuration": {
    "customer": {
      "automatic_indirect_tax": {
        ...
      },
      "billing": {
        ...
      },
      "capabilities": {
        ...
      },
      ...
    },
    "merchant": null,
    "recipient": null
  },
  "contact_email": "furever@example.com",
  "created": "2025-06-09T21:16:03.000Z",
  "dashboard": "full",
  "defaults": null,
  "display_name": "Furever",
  "identity": {
    "business_details": {
      "doing_business_as": "FurEver",
      "id_numbers": [
        {
          "type": "us_ein"
        }
      ],
      "product_description": "Saas pet grooming platform at furever.dev using Connect embedded components",
      "structure": "sole_proprietorship",
      "url": "http://accessible.stripe.com"
    },
    "country": "US"
  },
  "livemode": true,
  "metadata": {},
  "requirements": null
}
```

- Related guide: [Include-dependent response values](https://docs.stripe.com/api-includable-response-values.md)