# Create a shipping rate

Creates a new shipping rate object.

## Returns

Returns a shipping rate object if the call succeeded.

## Parameters

- `display_name` (string, required)
  The name of the shipping rate, meant to be displayable to the customer. This will appear on CheckoutSessions.

  The maximum length is 100 characters.

- `delivery_estimate` (object, optional)
  The estimated range for how long shipping will take, meant to be displayable to the customer. This will appear on CheckoutSessions.

  - `delivery_estimate.maximum` (object, optional)
    The upper bound of the estimated range. If empty, represents no upper bound i.e., infinite.

    - `delivery_estimate.maximum.unit` (enum, required)
      A unit of time.
Possible enum values:
      - `business_day`
        The delivery estimate is in business days.

      - `day`
        The delivery estimate is in days.

      - `hour`
        The delivery estimate is in hours.

      - `month`
        The delivery estimate is in months.

      - `week`
        The delivery estimate is in weeks.

    - `delivery_estimate.maximum.value` (integer, required)
      Must be greater than 0.

  - `delivery_estimate.minimum` (object, optional)
    The lower bound of the estimated range. If empty, represents no lower bound.

    - `delivery_estimate.minimum.unit` (enum, required)
      A unit of time.
Possible enum values:
      - `business_day`
        The delivery estimate is in business days.

      - `day`
        The delivery estimate is in days.

      - `hour`
        The delivery estimate is in hours.

      - `month`
        The delivery estimate is in months.

      - `week`
        The delivery estimate is in weeks.

    - `delivery_estimate.minimum.value` (integer, required)
      Must be greater than 0.

- `fixed_amount` (object, optional)
  Describes a fixed amount to charge for shipping. Must be present if type is `fixed_amount`.

  - `fixed_amount.amount` (integer, required)
    A non-negative integer in cents representing how much to charge.

  - `fixed_amount.currency` (enum, required)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `fixed_amount.currency_options` (object, optional)
    Shipping rates defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).

    - `fixed_amount.currency_options.<currency>.amount` (integer, required)
      A non-negative integer in cents representing how much to charge.

    - `fixed_amount.currency_options.<currency>.tax_behavior` (enum, recommended if calculating taxes)
      Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`.
Possible enum values:
      - `exclusive`
      - `inclusive`
      - `unspecified`

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `tax_behavior` (enum, recommended if calculating taxes)
  Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`.
Possible enum values:
  - `exclusive`
  - `inclusive`
  - `unspecified`

- `tax_code` (string, recommended if calculating taxes)
  A [tax code](https://docs.stripe.com/docs/tax/tax-categories.md) ID. The Shipping tax code is `txcd_92010001`.

- `type` (enum, required)
  The type of calculation to use on the shipping rate.
Possible enum values:
  - `fixed_amount`
    The shipping rate is a fixed amount.

```curl
curl https://api.stripe.com/v1/shipping_rates \
  -u "<<YOUR_SECRET_KEY>>" \
  -d display_name="Ground shipping" \
  -d type=fixed_amount \
  -d "fixed_amount[amount]"=500 \
  -d "fixed_amount[currency]"=usd
```

```cli
stripe shipping_rates create  \
  --display-name="Ground shipping" \
  --type=fixed_amount \
  -d "fixed_amount[amount]"=500 \
  -d "fixed_amount[currency]"=usd
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

shipping_rate = client.v1.shipping_rates.create({
  display_name: 'Ground shipping',
  type: 'fixed_amount',
  fixed_amount: {
    amount: 500,
    currency: 'usd',
  },
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

shipping_rate = client.v1.shipping_rates.create({
  "display_name": "Ground shipping",
  "type": "fixed_amount",
  "fixed_amount": {"amount": 500, "currency": "usd"},
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$shippingRate = $stripe->shippingRates->create([
  'display_name' => 'Ground shipping',
  'type' => 'fixed_amount',
  'fixed_amount' => [
    'amount' => 500,
    'currency' => 'usd',
  ],
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ShippingRateCreateParams params =
  ShippingRateCreateParams.builder()
    .setDisplayName("Ground shipping")
    .setType(ShippingRateCreateParams.Type.FIXED_AMOUNT)
    .setFixedAmount(
      ShippingRateCreateParams.FixedAmount.builder()
        .setAmount(500L)
        .setCurrency("usd")
        .build()
    )
    .build();

ShippingRate shippingRate = client.v1().shippingRates().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const shippingRate = await stripe.shippingRates.create({
  display_name: 'Ground shipping',
  type: 'fixed_amount',
  fixed_amount: {
    amount: 500,
    currency: 'usd',
  },
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.ShippingRateCreateParams{
  DisplayName: stripe.String("Ground shipping"),
  Type: stripe.String("fixed_amount"),
  FixedAmount: &stripe.ShippingRateCreateFixedAmountParams{
    Amount: stripe.Int64(500),
    Currency: stripe.String(stripe.CurrencyUSD),
  },
}
result, err := sc.V1ShippingRates.Create(context.TODO(), params)
```

```dotnet
var options = new ShippingRateCreateOptions
{
    DisplayName = "Ground shipping",
    Type = "fixed_amount",
    FixedAmount = new ShippingRateFixedAmountOptions
    {
        Amount = 500,
        Currency = "usd",
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.ShippingRates;
ShippingRate shippingRate = service.Create(options);
```

### Response

```json
{
  "id": "shr_1MrRx2LkdIwHu7ixikgEA6Wd",
  "object": "shipping_rate",
  "active": true,
  "created": 1680207604,
  "delivery_estimate": null,
  "display_name": "Ground shipping",
  "fixed_amount": {
    "amount": 500,
    "currency": "usd"
  },
  "livemode": false,
  "metadata": {},
  "tax_behavior": "unspecified",
  "tax_code": null,
  "type": "fixed_amount"
}
```