# List secrets

List all secrets stored on the given scope.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` Secrets, starting after Secret `starting_after`. Each entry in the array is a separate Secret object. If no more Secrets are available, the resulting array will be empty.

## Parameters

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

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/apps/secrets \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "scope[type]"=account
```

```cli
stripe apps secrets list  \
  -d "scope[type]"=account
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

secrets = client.v1.apps.secrets.list({scope: {type: 'account'}})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

secrets = client.v1.apps.secrets.list({"scope": {"type": "account"}})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$secrets = $stripe->apps->secrets->all(['scope' => ['type' => 'account']]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

SecretListParams params =
  SecretListParams.builder()
    .setScope(
      SecretListParams.Scope.builder()
        .setType(SecretListParams.Scope.Type.ACCOUNT)
        .build()
    )
    .build();

StripeCollection<Secret> stripeCollection =
  client.v1().apps().secrets().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const secrets = await stripe.apps.secrets.list({
  scope: {
    type: 'account',
  },
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.AppsSecretListParams{
  Scope: &stripe.AppsSecretListScopeParams{
    Type: stripe.String(stripe.AppsSecretScopeTypeAccount),
  },
}
result := sc.V1AppsSecrets.List(context.TODO(), params)
```

```dotnet
var options = new Stripe.Apps.SecretListOptions
{
    Scope = new Stripe.Apps.SecretScopeOptions { Type = "account" },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Apps.Secrets;
StripeList<Stripe.Apps.Secret> secrets = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/apps/secrets",
  "has_more": false,
  "data": [
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
  ]
}
```