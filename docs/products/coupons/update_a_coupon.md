# Update a coupon

Updates the metadata of a coupon. Other coupon details (currency, duration, amount_off) are, by design, not editable.

## Returns

The newly updated coupon object if the call succeeded. Otherwise, this call raises [an error](https://docs.stripe.com/api/coupons/update.md#errors), such as if the coupon has been deleted.

## Parameters

- `currency_options` (object, optional)
  Coupons defined in each available currency option (only supported if the coupon is amount-based). Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).

  - `currency_options.<currency>.amount_off` (integer, required)
    A positive integer representing the amount to subtract from an invoice total.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `name` (string, optional)
  Name of the coupon displayed to customers on, for instance invoices, or receipts. By default the `id` is shown if `name` is not set.

  The maximum length is 40 characters.

```curl
curl https://api.stripe.com/v1/coupons/jMT0WJUD \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
```

```cli
stripe coupons update jMT0WJUD \
  -d "metadata[order_id]"=6735
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

coupon = client.v1.coupons.update('jMT0WJUD', {metadata: {order_id: '6735'}})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

coupon = client.v1.coupons.update(
  "jMT0WJUD",
  {"metadata": {"order_id": "6735"}},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$coupon = $stripe->coupons->update(
  'jMT0WJUD',
  ['metadata' => ['order_id' => '6735']]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CouponUpdateParams params =
  CouponUpdateParams.builder().putMetadata("order_id", "6735").build();

Coupon coupon = client.v1().coupons().update("jMT0WJUD", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const coupon = await stripe.coupons.update(
  'jMT0WJUD',
  {
    metadata: {
      order_id: '6735',
    },
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CouponUpdateParams{}
params.AddMetadata("order_id", "6735")
result, err := sc.V1Coupons.Update(context.TODO(), "jMT0WJUD", params)
```

```dotnet
var options = new CouponUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Coupons;
Coupon coupon = service.Update("jMT0WJUD", options);
```

### Response

```json
{
  "id": "jMT0WJUD",
  "object": "coupon",
  "amount_off": null,
  "created": 1678037688,
  "currency": null,
  "duration": "repeating",
  "duration_in_months": 3,
  "livemode": false,
  "max_redemptions": null,
  "metadata": {
    "order_id": "6735"
  },
  "name": null,
  "percent_off": 25.5,
  "redeem_by": null,
  "times_redeemed": 0,
  "valid": true
}
```