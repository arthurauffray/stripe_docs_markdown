# Retrieve a token

Retrieves the token with the given ID.

## Returns

Returns a token if you provide a valid ID. Raises [an error](https://docs.stripe.com/api/tokens/retrieve.md#errors) otherwise.

```curl
curl https://api.stripe.com/v1/tokens/tok_1N3T00LkdIwHu7ixt44h1F8k \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe tokens retrieve tok_1N3T00LkdIwHu7ixt44h1F8k
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

token = client.v1.tokens.retrieve('tok_1N3T00LkdIwHu7ixt44h1F8k')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

token = client.v1.tokens.retrieve("tok_1N3T00LkdIwHu7ixt44h1F8k")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$token = $stripe->tokens->retrieve('tok_1N3T00LkdIwHu7ixt44h1F8k', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TokenRetrieveParams params = TokenRetrieveParams.builder().build();

Token token = client.v1().tokens().retrieve("tok_1N3T00LkdIwHu7ixt44h1F8k", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const token = await stripe.tokens.retrieve('tok_1N3T00LkdIwHu7ixt44h1F8k');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TokenRetrieveParams{}
result, err := sc.V1Tokens.Retrieve(
  context.TODO(), "tok_1N3T00LkdIwHu7ixt44h1F8k", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Tokens;
Token token = service.Get("tok_1N3T00LkdIwHu7ixt44h1F8k");
```

### Response

```json
{
  "id": "tok_1N3T00LkdIwHu7ixt44h1F8k",
  "object": "token",
  "card": {
    "id": "card_1N3T00LkdIwHu7ixRdxpVI1Q",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "US",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 5,
    "exp_year": 2026,
    "fingerprint": "mToisGZ01V71BCos",
    "funding": "credit",
    "last4": "4242",
    "metadata": {},
    "name": null,
    "tokenization_method": null,
    "wallet": null
  },
  "client_ip": "52.35.78.6",
  "created": 1683071568,
  "livemode": false,
  "type": "card",
  "used": false
}
```