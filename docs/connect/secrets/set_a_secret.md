# Set a Secret

Create or replace a secret in the secret store.

## Returns

Returns a secret object.

## Parameters

- `name` (string, required)
  A name for the secret that’s unique within the scope.

- `payload` (string, required)
  The plaintext secret value to be stored.

- `scope` (object, required)
  Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.

  - `scope.type` (enum, required)
    The secret scope type.
Possible enum values:
    - `account`
      A secret scoped to an account. Use this for API keys or other secrets that should be accessible by all UI Extension contexts.

    - `user`
      A secret scoped to a specific user. Use this for oauth tokens or other per-user secrets. If this is set, `scope.user` must also be set.

  - `scope.user` (string, optional)
    The user ID. This field is required if `type` is set to `user`, and should not be provided if `type` is set to `account`.

- `expires_at` (timestamp, optional)
  The Unix timestamp for the expiry time of the secret, after which the secret deletes.

```curl
curl https://api.stripe.com/v1/apps/secrets \
  -u "<<YOUR_SECRET_KEY>>" \
  -d name=my-api-key \
  -d payload=secret_key_xxxxxx \
  -d "scope[type]"=account
```

```cli
stripe apps secrets create  \
  --name=my-api-key \
  --payload=secret_key_xxxxxx \
  -d "scope[type]"=account
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

secret = client.v1.apps.secrets.create({
  name: 'my-api-key',
  payload: 'secret_key_xxxxxx',
  scope: {type: 'account'},
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

secret = client.v1.apps.secrets.create({
  "name": "my-api-key",
  "payload": "secret_key_xxxxxx",
  "scope": {"type": "account"},
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$secret = $stripe->apps->secrets->create([
  'name' => 'my-api-key',
  'payload' => 'secret_key_xxxxxx',
  'scope' => ['type' => 'account'],
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

SecretCreateParams params =
  SecretCreateParams.builder()
    .setName("my-api-key")
    .setPayload("secret_key_xxxxxx")
    .setScope(
      SecretCreateParams.Scope.builder()
        .setType(SecretCreateParams.Scope.Type.ACCOUNT)
        .build()
    )
    .build();

Secret secret = client.v1().apps().secrets().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const secret = await stripe.apps.secrets.create({
  name: 'my-api-key',
  payload: 'secret_key_xxxxxx',
  scope: {
    type: 'account',
  },
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.AppsSecretCreateParams{
  Name: stripe.String("my-api-key"),
  Payload: stripe.String("secret_key_xxxxxx"),
  Scope: &stripe.AppsSecretCreateScopeParams{
    Type: stripe.String(stripe.AppsSecretScopeTypeAccount),
  },
}
result, err := sc.V1AppsSecrets.Create(context.TODO(), params)
```

```dotnet
var options = new Stripe.Apps.SecretCreateOptions
{
    Name = "my-api-key",
    Payload = "secret_key_xxxxxx",
    Scope = new Stripe.Apps.SecretScopeOptions { Type = "account" },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Apps.Secrets;
Stripe.Apps.Secret secret = service.Create(options);
```

### Response

```json
{
  "id": "appsecret_5110hHS1707T6fjBnah1LkdIwHu7ix",
  "object": "apps.secret",
  "created": 1680209063,
  "expires_at": null,
  "livemode": false,
  "name": "my-api-key",
  "scope": {
    "type": "account"
  }
}
```