# Retrieve an issuing token

Retrieves an Issuing `Token` object.

## Returns

Returns an Issuing `Token` object if a valid identifier was provided.

```curl
curl https://api.stripe.com/v1/issuing/tokens/intok_1MzDbE2eZvKYlo2C26a98MDg \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe issuing tokens retrieve intok_1MzDbE2eZvKYlo2C26a98MDg
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

token = client.v1.issuing.tokens.retrieve('intok_1MzDbE2eZvKYlo2C26a98MDg')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

token = client.v1.issuing.tokens.retrieve("intok_1MzDbE2eZvKYlo2C26a98MDg")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$token = $stripe->issuing->tokens->retrieve('intok_1MzDbE2eZvKYlo2C26a98MDg', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TokenRetrieveParams params = TokenRetrieveParams.builder().build();

Token token =
  client.v1().issuing().tokens().retrieve("intok_1MzDbE2eZvKYlo2C26a98MDg", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const token = await stripe.issuing.tokens.retrieve('intok_1MzDbE2eZvKYlo2C26a98MDg');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.IssuingTokenRetrieveParams{}
result, err := sc.V1IssuingTokens.Retrieve(
  context.TODO(), "intok_1MzDbE2eZvKYlo2C26a98MDg", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Issuing.Tokens;
Stripe.Issuing.Token token = service.Get("intok_1MzDbE2eZvKYlo2C26a98MDg");
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
  "status": "active",
  "last4": "2424",
  "token_service_provider": "visa",
  "wallet_provider": "apple_pay",
  "device_fingerprint": "intd_1MzDbE2eZvKYcp3095svdf"
}
```