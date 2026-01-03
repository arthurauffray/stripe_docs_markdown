# Update a promotion code

Updates the specified promotion code by setting the values of the parameters passed. Most fields are, by design, not editable.

## Returns

The updated promotion code object is returned upon success. Otherwise, this call raises [an error](https://docs.stripe.com/api/promotion_codes/update.md#errors).

## Parameters

- `active` (boolean, optional)
  Whether the promotion code is currently active. A promotion code can only be reactivated when the coupon is still valid and the promotion code is otherwise redeemable.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `restrictions` (object, optional)
  Settings that restrict the redemption of the promotion code.

  - `restrictions.currency_options` (object, optional)
    Promotion codes defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).

    - `restrictions.currency_options.<currency>.minimum_amount` (integer, optional)
      Minimum amount required to redeem this Promotion Code into a Coupon (e.g., a purchase must be $100 or more to work).

```curl
curl https://api.stripe.com/v1/promotion_codes/promo_1MiM6KLkdIwHu7ixrIaX4wgn \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
```

```cli
stripe promotion_codes update promo_1MiM6KLkdIwHu7ixrIaX4wgn \
  -d "metadata[order_id]"=6735
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

promotion_code = client.v1.promotion_codes.update(
  'promo_1MiM6KLkdIwHu7ixrIaX4wgn',
  {metadata: {order_id: '6735'}},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

promotion_code = client.v1.promotion_codes.update(
  "promo_1MiM6KLkdIwHu7ixrIaX4wgn",
  {"metadata": {"order_id": "6735"}},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$promotionCode = $stripe->promotionCodes->update(
  'promo_1MiM6KLkdIwHu7ixrIaX4wgn',
  ['metadata' => ['order_id' => '6735']]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PromotionCodeUpdateParams params =
  PromotionCodeUpdateParams.builder().putMetadata("order_id", "6735").build();

PromotionCode promotionCode =
  client.v1().promotionCodes().update("promo_1MiM6KLkdIwHu7ixrIaX4wgn", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const promotionCode = await stripe.promotionCodes.update(
  'promo_1MiM6KLkdIwHu7ixrIaX4wgn',
  {
    metadata: {
      order_id: '6735',
    },
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PromotionCodeUpdateParams{}
params.AddMetadata("order_id", "6735")
result, err := sc.V1PromotionCodes.Update(
  context.TODO(), "promo_1MiM6KLkdIwHu7ixrIaX4wgn", params)
```

```dotnet
var options = new PromotionCodeUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.PromotionCodes;
PromotionCode promotionCode = service.Update(
    "promo_1MiM6KLkdIwHu7ixrIaX4wgn",
    options);
```

### Response

```json
{
  "id": "promo_1MiM6KLkdIwHu7ixrIaX4wgn",
  "object": "promotion_code",
  "active": true,
  "code": "A1H1Q1MG",
  "promotion": {
    "type": "coupon",
    "coupon": "nVJYDOag"
  },
  "created": 1678040164,
  "customer": null,
  "expires_at": null,
  "livemode": false,
  "max_redemptions": null,
  "metadata": {
    "order_id": "6735"
  },
  "restrictions": {
    "first_time_transaction": false,
    "minimum_amount": null,
    "minimum_amount_currency": null
  },
  "times_redeemed": 0
}
```