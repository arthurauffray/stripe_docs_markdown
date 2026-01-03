# Authentication

The Stripe API uses [API keys](https://docs.stripe.com/keys.md) to authenticate requests. You can view and manage your API keys in [the Stripe Dashboard](https://dashboard.stripe.com/login?redirect=/apikeys).

Test mode secret keys have the prefix `sk_test_` and live mode secret keys have the prefix `sk_live_`. Alternatively, you can use [restricted API keys](https://docs.stripe.com/keys.md#limit-access) for granular permissions.

Your API keys carry many privileges, so be sure to keep them secure! Do not share your secret API keys in publicly accessible areas such as GitHub, client-side code, and so forth.

Authentication to the API is performed via [HTTP Basic Auth](http://en.wikipedia.org/wiki/Basic_access_authentication). Provide your API key as the basic auth username value. You do not need to provide a password.

If you need to authenticate via bearer auth (e.g., for a cross-origin request), use `-H "Authorization: Bearer ,[object Object],"` instead of `-u ,[object Object]`.

Connect the CLI to your Stripe account by logging in to persist your secret key locally. See also [Log in to the CLI](https://docs.stripe.com/stripe-cli.md#login-account).

Use your API key by assigning it to `Stripe.api_key`. The Ruby library will then automatically send this key in each request.

You can also set a per-request key with an option. This is often useful for Connect applications that use multiple API keys during the lifetime of a process. Methods on the returned object reuse the same API key.

Use your API key by assigning it to `stripe.api_key`. The Python library will then automatically send this key in each request.

You can also set a per-request key with an option. This is often useful for Connect applications that use multiple API keys during the lifetime of a process. Methods on the returned object reuse the same API key.

Use your API key by setting it in the initial configuration of `new \Stripe\StripeClient()`. The PHP library will then automatically send this key in each request.

You can also set a per-request key with an option. This is often useful for Connect applications that use multiple API keys during the lifetime of a process. Methods on the returned object reuse the same API key.

Use your API key by assigning it to `Stripe.apiKey`. The Java library will then automatically send this key in each request.

You can also set a per-request key with an option. This is often useful for Connect applications that use multiple API keys during the lifetime of a process.

Use your API key by setting it in the initial configuration of `stripe`. The Node.js library will then automatically send this key in each request.

You can also set a per-request key with an option. This is often useful for Connect applications that use multiple API keys during the lifetime of a process. Methods on the returned object reuse the same API key.

Use your API key by assigning it to `stripe.Key`. The Go library will then automatically send this key in each request.

You can also set a per-request key with an option. This is often useful for Connect applications that use multiple API keys during the lifetime of a process.

Use your API key by assigning it to `StripeConfiguration.ApiKey`. The .NET library will then automatically send this key in each request.

You can also set a per-request key with an option. This is often useful for Connect applications that use multiple API keys during the lifetime of a process.

All API requests must be made over [HTTPS](http://en.wikipedia.org/wiki/HTTP_Secure). Calls made over plain HTTP will fail. API requests without authentication will also fail.

```sh
curl https://api.stripe.com/v1/charges \
  -u sk_test_xLhH7sntJEJFllhPZwbGU0Sj:
# The colon prevents curl from asking for a password.
```

### Global API Key

```javascript
const Stripe = require('stripe');
const stripe = Stripe('sk_test_xLhH7sntJEJFllhPZwbGU0Sj');
```

### Per-Request API Key

```javascript
var charge = await stripe.charges.retrieve(
  'ch_3LiiC52eZvKYlo2C1da66ZSQ',
  {
    apiKey: 'sk_test_xLhH7sntJEJFllhPZwbGU0Sj'
  }
);
```

```plaintext
stripe login
```

### Global API Key

```ruby
require 'stripe'
Stripe.api_key = 'sk_test_xLhH7sntJEJFllhPZwbGU0Sj'
```

### Per-Request API Key

```ruby
require 'stripe'
charge = Stripe::Charge.retrieve(
  'ch_3Ln3cj2eZvKYlo2C1lcnB8f6',
  {
    api_key: 'sk_test_xLhH7sntJEJFllhPZwbGU0Sj',
  }
)
charge.capture # Uses the same API Key.
```

### Global API Key

```python
import stripe
stripe.api_key = "sk_test_xLhH7sntJEJFllhPZwbGU0Sj"
```

### Per-Request API Key

```python
import stripe
charge = stripe.Charge.retrieve(
  "ch_3Ln3e92eZvKYlo2C0eUfv7bi",
  api_key="sk_test_xLhH7sntJEJFllhPZwbGU0Sj"
)
charge.capture() # Uses the same API Key.
```

### Global API Key

```php
$stripe = new \Stripe\StripeClient("sk_test_xLhH7sntJEJFllhPZwbGU0Sj");
```

### Per-Request API Key

```php
$ch = $stripe->charges->retrieve(
  'ch_3Ln3fO2eZvKYlo2C1kqP3AMr',
  [],
  ['api_key' => 'sk_test_xLhH7sntJEJFllhPZwbGU0Sj']
);
$ch->capture(); // Uses the same API Key.
```

### Global API Key

```java
Stripe.apiKey = "sk_test_xLhH7sntJEJFllhPZwbGU0Sj";
```

### Per-Request API Key

```java
RequestOptions requestOptions = RequestOptions.builder()
  .setApiKey("sk_test_xLhH7sntJEJFllhPZwbGU0Sj")
  .build();

Charge charge = Charge.retrieve(
  "ch_3Ln3ga2eZvKYlo2C11iwHdxy",
  requestOptions,
);

```

### Global API Key

```go
stripe.Key = "sk_test_xLhH7sntJEJFllhPZwbGU0Sj"
```

### Per-Request API Key

```go
params := &stripe.ChargeParams{}
sc := &client.API{}
sc.Init("sk_test_xLhH7sntJEJFllhPZwbGU0Sj", nil)
sc.Charges.Get("ch_3Ln3j02eZvKYlo2C0d5IZWuG", params)
```

### Global API Key

```dotnet
StripeConfiguration.ApiKey = "sk_test_xLhH7sntJEJFllhPZwbGU0Sj";
```

### Per-Request API Key

```dotnet
var options = new RequestOptions
{
  ApiKey = "sk_test_xLhH7sntJEJFllhPZwbGU0Sj"
};
var service = new ChargeService();
Charge charge = service.Get(
  "ch_3Ln3kB2eZvKYlo2C1YRBr0Ll",
  options
);
```

## Your API Key

A sample test API key is included in all the examples here, so you can test any example right away. Do not submit any personally identifiable information in requests made with this key.

To test requests using your account, replace the sample API key with your actual API key or sign in.