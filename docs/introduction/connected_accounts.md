# Connected Accounts

If you use Stripe [Connect](https://docs.stripe.com/connect.md), you can issue requests on behalf of your [connected accounts](https://docs.stripe.com/connect/accounts.md). To act as a connected account, include a `Stripe-Account` header containing the connected account ID, which typically starts with the `acct_` prefix.

The connected account ID is set per-request. Methods on the returned object reuse the same account ID.

- Related guide: [Making API calls for connected accounts](https://docs.stripe.com/connect/authentication.md)

```sh
curl https://api.stripe.com/v1/charges/ch_3LmjFA2eZvKYlo2C09TLIsrw \
  -u sk_test_xLhH7sntJEJFllhPZwbGU0Sj: \
  -H "Stripe-Account: acct_1032D82eZvKYlo2C" \
  -G
```

### Global API Key

```ruby
require 'stripe'
charge = Stripe::Charge.retrieve(
  'ch_3Lmjo22eZvKYlo2C1kuO4yZM',
  {
    stripe_account: 'acct_1032D82eZvKYlo2C',
  }
)
charge.capture # Uses the same account.
```

```sh
stripe charges retrieve ch_3LmjIH2eZvKYlo2C067UssSm \
    --stripe-account acct_1032D82eZvKYlo2C
```

```python
import stripe
charge = stripe.Charge.retrieve(
  "ch_3Lmjoz2eZvKYlo2C1rBER4Dk",
  stripe_account="acct_1032D82eZvKYlo2C"
)
charge.capture() # Uses the same account.
```

```php
$ch = $stripe->charges->retrieve(
  'ch_3Lmjrl2eZvKYlo2C1bscjw8Z',
  [],
  ['stripe_account' => 'acct_1032D82eZvKYlo2C']
);
$ch->capture(); // Uses the same account.
```

```java
RequestOptions requestOptions = RequestOptions.builder()
  .setStripeAccount("acct_1032D82eZvKYlo2C")
  .build();

Charge charge = Charge.retrieve(
  "ch_3LmjsM2eZvKYlo2C1CcKvJbn",
  requestOptions,
);

```

```javascript
stripe.charges.retrieve('ch_3LmjSR2eZvKYlo2C1cPZxlbL', {
  stripeAccount: 'acct_1032D82eZvKYlo2C'
});
```

```go
params := &stripe.ChargeParams{}
params.SetStripeAccount("acct_1032D82eZvKYlo2C")
ch, err := charge.Get("ch_3Lmjso2eZvKYlo2C0rTTv0MK", params)
```

```dotnet
var options = new RequestOptions
{
  StripeAccount = "acct_1032D82eZvKYlo2C"
};
var service = new ChargeService();
Charge charge = service.Get(
  "ch_3LmjRC2eZvKYlo2C1vvMTc1Q",
  options
);
```