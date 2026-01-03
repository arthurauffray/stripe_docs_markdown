# Update a price

Updates the specified price by setting the values of the parameters passed. Any parameters not provided are left unchanged.

## Returns

The updated price object is returned upon success. Otherwise, this call raises [an error](https://docs.stripe.com/api/prices/update.md#errors).

## Parameters

- `active` (boolean, optional)
  Whether the price can be used for new purchases. Defaults to `true`.

- `currency_options` (object, optional)
  Prices defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).

  - `currency_options.<currency>.custom_unit_amount` (object, required conditionally)
    When set, provides configuration for the amount to be adjusted by the customer during Checkout Sessions and Payment Links.

    - `currency_options.<currency>.custom_unit_amount.enabled` (boolean, required)
      Pass in `true` to enable `custom_unit_amount`, otherwise omit `custom_unit_amount`.

    - `currency_options.<currency>.custom_unit_amount.maximum` (integer, optional)
      The maximum unit amount the customer can specify for this item.

    - `currency_options.<currency>.custom_unit_amount.minimum` (integer, optional)
      The minimum unit amount the customer can specify for this item. Must be at least the minimum charge amount.

    - `currency_options.<currency>.custom_unit_amount.preset` (integer, optional)
      The starting unit amount which can be updated by the customer.

  - `currency_options.<currency>.tax_behavior` (enum, recommended if calculating taxes)
    Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
Possible enum values:
    - `exclusive`
    - `inclusive`
    - `unspecified`

  - `currency_options.<currency>.tiers` (array of objects, Required if billing_scheme=tiered)
    Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`.

    - `currency_options.<currency>.tiers.up_to` (string | integer, required)
      Specifies the upper bound of this tier. The lower bound of a tier is the upper bound of the previous tier adding one. Use `inf` to define a fallback tier.

    - `currency_options.<currency>.tiers.flat_amount` (integer, optional)
      The flat billing amount for an entire tier, regardless of the number of units in the tier.

    - `currency_options.<currency>.tiers.flat_amount_decimal` (string, optional)
      Same as `flat_amount`, but accepts a decimal value representing an integer in the minor units of the currency. Only one of `flat_amount` and `flat_amount_decimal` can be set.

    - `currency_options.<currency>.tiers.unit_amount` (integer, optional)
      The per unit billing amount for each individual unit for which this tier applies.

    - `currency_options.<currency>.tiers.unit_amount_decimal` (string, optional)
      Same as `unit_amount`, but accepts a decimal value in cents with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.

  - `currency_options.<currency>.unit_amount` (integer, required conditionally)
    A positive integer in cents (or 0 for a free price) representing how much to charge.

  - `currency_options.<currency>.unit_amount_decimal` (string, required conditionally)
    Same as `unit_amount`, but accepts a decimal value in cents with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.

- `lookup_key` (string, optional)
  A lookup key used to retrieve prices dynamically from a static string. This may be up to 200 characters.

  The maximum length is 200 characters.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `nickname` (string, optional)
  A brief description of the price, hidden from customers.

- `tax_behavior` (enum, recommended if calculating taxes)
  Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
Possible enum values:
  - `exclusive`
  - `inclusive`
  - `unspecified`

- `transfer_lookup_key` (boolean, optional)
  If set to true, will atomically remove the lookup key from the existing price, and assign it to this price.

```curl
curl https://api.stripe.com/v1/prices/price_1MoBy5LkdIwHu7ixZhnattbh \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
```

```cli
stripe prices update price_1MoBy5LkdIwHu7ixZhnattbh \
  -d "metadata[order_id]"=6735
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

price = client.v1.prices.update(
  'price_1MoBy5LkdIwHu7ixZhnattbh',
  {metadata: {order_id: '6735'}},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

price = client.v1.prices.update(
  "price_1MoBy5LkdIwHu7ixZhnattbh",
  {"metadata": {"order_id": "6735"}},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$price = $stripe->prices->update(
  'price_1MoBy5LkdIwHu7ixZhnattbh',
  ['metadata' => ['order_id' => '6735']]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PriceUpdateParams params =
  PriceUpdateParams.builder().putMetadata("order_id", "6735").build();

Price price = client.v1().prices().update("price_1MoBy5LkdIwHu7ixZhnattbh", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const price = await stripe.prices.update(
  'price_1MoBy5LkdIwHu7ixZhnattbh',
  {
    metadata: {
      order_id: '6735',
    },
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PriceUpdateParams{}
params.AddMetadata("order_id", "6735")
result, err := sc.V1Prices.Update(
  context.TODO(), "price_1MoBy5LkdIwHu7ixZhnattbh", params)
```

```dotnet
var options = new PriceUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Prices;
Price price = service.Update("price_1MoBy5LkdIwHu7ixZhnattbh", options);
```

### Response

```json
{
  "id": "price_1MoBy5LkdIwHu7ixZhnattbh",
  "object": "price",
  "active": true,
  "billing_scheme": "per_unit",
  "created": 1679431181,
  "currency": "usd",
  "custom_unit_amount": null,
  "livemode": false,
  "lookup_key": null,
  "metadata": {
    "order_id": "6735"
  },
  "nickname": null,
  "product": "prod_NZKdYqrwEYx6iK",
  "recurring": {
    "interval": "month",
    "interval_count": 1,
    "trial_period_days": null,
    "usage_type": "licensed"
  },
  "tax_behavior": "unspecified",
  "tiers_mode": null,
  "transform_quantity": null,
  "type": "recurring",
  "unit_amount": 1000,
  "unit_amount_decimal": "1000"
}
```