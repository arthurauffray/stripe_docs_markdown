# Retrieve a person token

Retrieves a Person Token associated with an Account.

## Parameters

- `account_id` (string, required)
  The Account the Person is associated with.

- `id` (string, required)
  The ID of the Person Token to retrieve.

## Returns

## Response attributes

- `id` (string)
  Unique identifier for the token.

- `object` (string, value is "v2.core.account_person_token")
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
curl https://api.stripe.com/v2/core/accounts/acct_1Nv0FGQ9RKHgCVdK/person_tokens/perstok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: {{STRIPE_API_VERSION}}"
```

```cli
stripe v2 core accounts person_tokens retrieve acct_1Nv0FGQ9RKHgCVdK perstok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

account_person_token = client.v2.core.accounts.person_tokens.retrieve(
  'acct_1Nv0FGQ9RKHgCVdK',
  'perstok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY',
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

account_person_token = client.v2.core.accounts.person_tokens.retrieve(
  "acct_1Nv0FGQ9RKHgCVdK",
  "perstok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$accountPersonToken = $stripe->v2->core->accounts->personTokens->retrieve(
  'acct_1Nv0FGQ9RKHgCVdK',
  'perstok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AccountPersonToken accountPersonToken =
  client.v2().core().accounts().personTokens().retrieve(
    "acct_1Nv0FGQ9RKHgCVdK",
    "perstok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY"
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const accountPersonToken = await stripe.v2.core.accounts.personTokens.retrieve(
  'acct_1Nv0FGQ9RKHgCVdK',
  'perstok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.V2CoreAccountsPersonTokenRetrieveParams{
  AccountID: stripe.String("acct_1Nv0FGQ9RKHgCVdK"),
}
result, err := sc.V2CoreAccountsPersonTokens.Retrieve(
  context.TODO(), "perstok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V2.Core.Accounts.PersonTokens;
Stripe.V2.Core.AccountPersonToken accountPersonToken = service.Get(
    "acct_1Nv0FGQ9RKHgCVdK",
    "perstok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY");
```

### Response

```json
{
  "id": "perstok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY",
  "object": "v2.core.account_person_token",
  "created": "2025-11-17T14:00:00.000Z",
  "expires_at": "2025-11-17T14:10:00.000Z",
  "livemode": true,
  "used": true
}
```