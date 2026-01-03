# Create a promotion code

A promotion code points to an underlying promotion. You can optionally restrict the code to a specific customer, redemption limit, and expiration date.

## Returns

Returns the promotion code object.

## Parameters

- `promotion` (object, required)
  The promotion referenced by this promotion code.

  - `promotion.type` (enum, required)
    Specifies the type of promotion.
Possible enum values:
    - `coupon`
      Coupon promotion type.

  - `promotion.coupon` (string, optional)
    If promotion `type` is `coupon`, the coupon for this promotion code.

- `active` (boolean, optional)
  Whether the promotion code is currently active.

- `code` (string, optional)
  The customer-facing code. Regardless of case, this code must be unique across all active promotion codes for a specific customer. Valid characters are lower case letters (a-z), upper case letters (A-Z), and digits (0-9).

  If left blank, we will generate one automatically.

  The maximum length is 500 characters.

- `customer` (string, optional)
  The customer who can use this promotion code. If not set, all customers can use the promotion code.

- `customer_account` (string, optional)
  The account representing the customer who can use this promotion code. If not set, all customers can use the promotion code.

- `expires_at` (timestamp, optional)
  The timestamp at which this promotion code will expire. If the coupon has specified a `redeems_by`, then this value cannot be after the coupon’s `redeems_by`.

- `max_redemptions` (integer, optional)
  A positive integer specifying the number of times the promotion code can be redeemed. If the coupon has specified a `max_redemptions`, then this value cannot be greater than the coupon’s `max_redemptions`.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `restrictions` (object, optional)
  Settings that restrict the redemption of the promotion code.

  - `restrictions.currency_options` (object, optional)
    Promotion codes defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).

    - `restrictions.currency_options.<currency>.minimum_amount` (integer, optional)
      Minimum amount required to redeem this Promotion Code into a Coupon (e.g., a purchase must be $100 or more to work).

  - `restrictions.first_time_transaction` (boolean, optional)
    A Boolean indicating if the Promotion Code should only be redeemed for Customers without any successful payments or invoices

  - `restrictions.minimum_amount` (integer, optional)
    Minimum amount required to redeem this Promotion Code into a Coupon (e.g., a purchase must be $100 or more to work).

  - `restrictions.minimum_amount_currency` (enum, optional)
    Three-letter [ISO code](https://stripe.com/docs/currencies) for minimum_amount

```curl
curl https://api.stripe.com/v1/promotion_codes \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "promotion[type]"=coupon \
  -d "promotion[coupon]"=nVJYDOag
```

```cli
stripe promotion_codes create  \
  -d "promotion[type]"=coupon \
  -d "promotion[coupon]"=nVJYDOag
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

promotion_code = client.v1.promotion_codes.create({
  promotion: {
    type: 'coupon',
    coupon: 'nVJYDOag',
  },
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

promotion_code = client.v1.promotion_codes.create({
  "promotion": {"type": "coupon", "coupon": "nVJYDOag"},
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$promotionCode = $stripe->promotionCodes->create([
  'promotion' => [
    'type' => 'coupon',
    'coupon' => 'nVJYDOag',
  ],
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PromotionCodeCreateParams params =
  PromotionCodeCreateParams.builder()
    .setPromotion(
      PromotionCodeCreateParams.Promotion.builder()
        .setType(PromotionCodeCreateParams.Promotion.Type.COUPON)
        .setCoupon("nVJYDOag")
        .build()
    )
    .build();

PromotionCode promotionCode = client.v1().promotionCodes().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const promotionCode = await stripe.promotionCodes.create({
  promotion: {
    type: 'coupon',
    coupon: 'nVJYDOag',
  },
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PromotionCodeCreateParams{
  Promotion: &stripe.PromotionCodeCreatePromotionParams{
    Type: stripe.String("coupon"),
    Coupon: stripe.String("nVJYDOag"),
  },
}
result, err := sc.V1PromotionCodes.Create(context.TODO(), params)
```

```dotnet
var options = new PromotionCodeCreateOptions
{
    Promotion = new PromotionCodePromotionOptions
    {
        Type = "coupon",
        Coupon = "nVJYDOag",
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.PromotionCodes;
PromotionCode promotionCode = service.Create(options);
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