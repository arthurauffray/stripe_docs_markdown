# Find a Secret

Finds a secret in the secret store by name and scope.

## Returns

Returns a secret object.

## Parameters

- `name` (string, required)
  A name for the secret that’s unique within the scope.

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

```curl
curl -G https://api.stripe.com/v1/apps/secrets/find \
  -u "<<YOUR_SECRET_KEY>>" \
  -d name=my-api-key \
  -d "scope[type]"=account
```

```cli
stripe apps secrets find  \
  --name=my-api-key \
  -d "scope[type]"=account
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

secret = client.v1.apps.secrets.find({
  name: 'my-api-key',
  scope: {type: 'account'},
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

secret = client.v1.apps.secrets.find({
  "name": "my-api-key",
  "scope": {"type": "account"},
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$secret = $stripe->apps->secrets->find([
  'name' => 'my-api-key',
  'scope' => ['type' => 'account'],
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

SecretFindParams params =
  SecretFindParams.builder()
    .setName("my-api-key")
    .setScope(
      SecretFindParams.Scope.builder()
        .setType(SecretFindParams.Scope.Type.ACCOUNT)
        .build()
    )
    .build();

Secret secret = client.v1().apps().secrets().find(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const secret = await stripe.apps.secrets.find({
  name: 'my-api-key',
  scope: {
    type: 'account',
  },
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.AppsSecretFindParams{
  Name: stripe.String("my-api-key"),
  Scope: &stripe.AppsSecretFindScopeParams{
    Type: stripe.String(stripe.AppsSecretScopeTypeAccount),
  },
}
result, err := sc.V1AppsSecrets.Find(context.TODO(), params)
```

```dotnet
var options = new Stripe.Apps.SecretFindOptions
{
    Name = "my-api-key",
    Scope = new Stripe.Apps.SecretScopeOptions { Type = "account" },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Apps.Secrets;
Stripe.Apps.Secret secret = service.Find(options);
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