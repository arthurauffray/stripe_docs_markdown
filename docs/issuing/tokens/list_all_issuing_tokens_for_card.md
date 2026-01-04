# List all issuing tokens for card

Lists all Issuing `Token` objects for a given card.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` tokens, starting after token `starting_after`. Each entry in the array is a separate Issuing `Token` object. If no more tokens are available, the resulting array will be empty.

## Parameters

- `card` (string, required)
  The Issuing card identifier to list tokens for.

- `created` (object, optional)
  Only return Issuing tokens that were created during the given date interval.

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

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `status` (enum, optional)
  Select Issuing tokens with the given status.
Possible enum values:
  - `active`
    Token is provisioned and usable for payments.

  - `deleted`
    Terminal state. Token can no longer be used.

  - `requested`
    Token has been requested to be provisioned, but has not completed the activation process.

  - `suspended`
    Token temporarily cannot be used for payments.

```curl
curl -G https://api.stripe.com/v1/issuing/tokens \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3 \
  -d card=ic_1MytUz2eZvKYlo2CZCn5fuvZ
```

```cli
stripe issuing tokens list  \
  --limit=3 \
  --card=ic_1MytUz2eZvKYlo2CZCn5fuvZ
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

tokens = client.v1.issuing.tokens.list({
  limit: 3,
  card: 'ic_1MytUz2eZvKYlo2CZCn5fuvZ',
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

tokens = client.v1.issuing.tokens.list({
  "limit": 3,
  "card": "ic_1MytUz2eZvKYlo2CZCn5fuvZ",
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$tokens = $stripe->issuing->tokens->all([
  'limit' => 3,
  'card' => 'ic_1MytUz2eZvKYlo2CZCn5fuvZ',
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TokenListParams params =
  TokenListParams.builder()
    .setLimit(3L)
    .setCard("ic_1MytUz2eZvKYlo2CZCn5fuvZ")
    .build();

StripeCollection<Token> stripeCollection =
  client.v1().issuing().tokens().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const tokens = await stripe.issuing.tokens.list({
  limit: 3,
  card: 'ic_1MytUz2eZvKYlo2CZCn5fuvZ',
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.IssuingTokenListParams{
  Card: stripe.String("ic_1MytUz2eZvKYlo2CZCn5fuvZ"),
}
params.Limit = stripe.Int64(3)
result := sc.V1IssuingTokens.List(context.TODO(), params)
```

```dotnet
var options = new Stripe.Issuing.TokenListOptions
{
    Limit = 3,
    Card = "ic_1MytUz2eZvKYlo2CZCn5fuvZ",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Issuing.Tokens;
StripeList<Stripe.Issuing.Token> tokens = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/issuing/tokens",
  "has_more": false,
  "data": [
    {
      "id": "intok_1MzDbE2eZvKYlo2C26a98MDg",
      "object": "issuing.token",
      "card": "ic_1MytUz2eZvKYlo2CZCn5fuvZ",
      "created": 1682059060,
      "network_updated_at": 1682059060,
      "livemode": false,
      "status": "suspended",
      "last4": "2424",
      "token_service_provider": "visa",
      "wallet_provider": "apple_pay",
      "device_fingerprint": "intd_1MzDbE2eZvKYcp3095svdf"
    }
  ]
}
```