# Retrieve an account token

Retrieves an Account Token.

## Parameters

- `id` (string, required)
  The ID of the Account Token to retrieve.

## Returns

## Response attributes

- `id` (string)
  Unique identifier for the token.

- `object` (string, value is "v2.core.account_token")
  String representing the object’s type. Objects of the same type share the same value of the object field.

- `created` (timestamp)
  Time at which the token was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.

- `expires_at` (timestamp)
  Time at which the token will expire.

- `livemode` (boolean)
  Has the value `true` if the token exists in live mode or the value `false` if the object exists in test mode.

- `used` (boolean)
  Determines if the token has already been used (tokens can only be used once).

## Error Codes

| HTTP status code | Code      | Description                |
| ---------------- | --------- | -------------------------- |
| 404              | not_found | The resource wasn’t found. |

```curl
curl https://api.stripe.com/v2/core/account_tokens/accttok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: {{STRIPE_API_VERSION}}"
```

```cli
stripe v2 core account_tokens retrieve accttok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

account_token = client.v2.core.account_tokens.retrieve('accttok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

account_token = client.v2.core.account_tokens.retrieve(
  "accttok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$accountToken = $stripe->v2->core->accountTokens->retrieve(
  'accttok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AccountToken accountToken =
  client.v2().core().accountTokens().retrieve(
    "accttok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY"
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const accountToken = await stripe.v2.core.accountTokens.retrieve(
  'accttok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.V2CoreAccountTokenRetrieveParams{}
result, err := sc.V2CoreAccountTokens.Retrieve(
  context.TODO(), "accttok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V2.Core.AccountTokens;
Stripe.V2.Core.AccountToken accountToken = service.Get(
    "accttok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY");
```

### Response

```json
{
  "id": "accttok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY",
  "object": "v2.core.account_token",
  "created": "2025-11-17T14:00:00.000Z",
  "expires_at": "2025-11-17T14:10:00.000Z",
  "livemode": true,
  "used": true
}
```