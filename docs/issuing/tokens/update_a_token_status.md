# Update a token status

Attempts to update the specified Issuing `Token` object to the status specified.

## Returns

Returns an updated Issuing `Token` object if a valid identifier was provided.

## Parameters

- `status` (enum, required)
  Specifies which status the token should be updated to.
Possible enum values:
  - `active`
    Token is provisioned and usable for payments.

  - `deleted`
    Terminal state. Token can no longer be used.

  - `suspended`
    Token temporarily cannot be used for payments.

```curl
curl https://api.stripe.com/v1/issuing/tokens/intok_1MzDbE2eZvKYlo2C26a98MDg \
  -u "<<YOUR_SECRET_KEY>>" \
  -d status=suspended
```

```cli
stripe issuing tokens update intok_1MzDbE2eZvKYlo2C26a98MDg \
  --status=suspended
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

token = client.v1.issuing.tokens.update(
  'intok_1MzDbE2eZvKYlo2C26a98MDg',
  {status: 'suspended'},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

token = client.v1.issuing.tokens.update(
  "intok_1MzDbE2eZvKYlo2C26a98MDg",
  {"status": "suspended"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$token = $stripe->issuing->tokens->update(
  'intok_1MzDbE2eZvKYlo2C26a98MDg',
  ['status' => 'suspended']
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TokenUpdateParams params =
  TokenUpdateParams.builder().setStatus(TokenUpdateParams.Status.SUSPENDED).build();

Token token =
  client.v1().issuing().tokens().update("intok_1MzDbE2eZvKYlo2C26a98MDg", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const token = await stripe.issuing.tokens.update(
  'intok_1MzDbE2eZvKYlo2C26a98MDg',
  {
    status: 'suspended',
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.IssuingTokenUpdateParams{
  Status: stripe.String(stripe.IssuingTokenStatusSuspended),
}
result, err := sc.V1IssuingTokens.Update(
  context.TODO(), "intok_1MzDbE2eZvKYlo2C26a98MDg", params)
```

```dotnet
var options = new Stripe.Issuing.TokenUpdateOptions { Status = "suspended" };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Issuing.Tokens;
Stripe.Issuing.Token token = service.Update(
    "intok_1MzDbE2eZvKYlo2C26a98MDg",
    options);
```

### Response

```json
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
```