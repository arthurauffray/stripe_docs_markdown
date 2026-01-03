# Retrieve a promotion code

Retrieves the promotion code with the given ID. In order to retrieve a promotion code by the customer-facing `code` use [list](https://docs.stripe.com/docs/api/promotion_codes/list.md) with the desired `code`.

## Returns

Returns a promotion code if a valid promotion code ID was provided. Raises [an error](https://docs.stripe.com/api/promotion_codes/retrieve.md#errors) otherwise.

```curl
curl https://api.stripe.com/v1/promotion_codes/promo_1MiM6KLkdIwHu7ixrIaX4wgn \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe promotion_codes retrieve promo_1MiM6KLkdIwHu7ixrIaX4wgn
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

promotion_code = client.v1.promotion_codes.retrieve('promo_1MiM6KLkdIwHu7ixrIaX4wgn')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

promotion_code = client.v1.promotion_codes.retrieve("promo_1MiM6KLkdIwHu7ixrIaX4wgn")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$promotionCode = $stripe->promotionCodes->retrieve(
  'promo_1MiM6KLkdIwHu7ixrIaX4wgn',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PromotionCodeRetrieveParams params = PromotionCodeRetrieveParams.builder().build();

PromotionCode promotionCode =
  client.v1().promotionCodes().retrieve("promo_1MiM6KLkdIwHu7ixrIaX4wgn", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const promotionCode = await stripe.promotionCodes.retrieve(
  'promo_1MiM6KLkdIwHu7ixrIaX4wgn'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PromotionCodeRetrieveParams{}
result, err := sc.V1PromotionCodes.Retrieve(
  context.TODO(), "promo_1MiM6KLkdIwHu7ixrIaX4wgn", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.PromotionCodes;
PromotionCode promotionCode = service.Get("promo_1MiM6KLkdIwHu7ixrIaX4wgn");
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
  "metadata": {},
  "restrictions": {
    "first_time_transaction": false,
    "minimum_amount": null,
    "minimum_amount_currency": null
  },
  "times_redeemed": 0
}
```