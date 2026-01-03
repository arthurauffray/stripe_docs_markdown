# Create a price

Creates a new [Price](https://docs.stripe.com/api/prices.md) for an existing [Product](https://docs.stripe.com/api/products.md). The Price can be recurring or one-time.

## Returns

The newly created `Price` object is returned upon success. Otherwise, this call raises [an error](https://docs.stripe.com/api/prices/create.md#errors).

## Parameters

- `currency` (enum, required)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `active` (boolean, optional)
  Whether the price can be used for new purchases. Defaults to `true`.

- `billing_scheme` (enum, optional)
  Describes how to compute the price per period. Either `per_unit` or `tiered`. `per_unit` indicates that the fixed amount (specified in `unit_amount` or `unit_amount_decimal`) will be charged per unit in `quantity` (for prices with `usage_type=licensed`), or per unit of total usage (for prices with `usage_type=metered`). `tiered` indicates that the unit pricing will be computed using a tiering strategy as defined using the `tiers` and `tiers_mode` attributes.
Possible enum values:
  - `per_unit`
  - `tiered`

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

- `custom_unit_amount` (object, Required unless unit_amount is provided)
  When set, provides configuration for the amount to be adjusted by the customer during Checkout Sessions and Payment Links.

  - `custom_unit_amount.enabled` (boolean, required)
    Pass in `true` to enable `custom_unit_amount`, otherwise omit `custom_unit_amount`.

  - `custom_unit_amount.maximum` (integer, optional)
    The maximum unit amount the customer can specify for this item.

  - `custom_unit_amount.minimum` (integer, optional)
    The minimum unit amount the customer can specify for this item. Must be at least the minimum charge amount.

  - `custom_unit_amount.preset` (integer, optional)
    The starting unit amount which can be updated by the customer.

- `lookup_key` (string, optional)
  A lookup key used to retrieve prices dynamically from a static string. This may be up to 200 characters.

  The maximum length is 200 characters.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `nickname` (string, optional)
  A brief description of the price, hidden from customers.

- `product` (string, required unless product_data is provided)
  The ID of the [Product](https://docs.stripe.com/api/products.md) that this [Price](https://docs.stripe.com/api/prices.md) will belong to.

- `product_data` (object, required unless product is provided)
  These fields can be used to create a new product that this price will belong to.

  - `product_data.name` (string, required)
    The product’s name, meant to be displayable to the customer.

  - `product_data.active` (boolean, optional)
    Whether the product is currently available for purchase. Defaults to `true`.

  - `product_data.metadata` (object, optional)
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

  - `product_data.statement_descriptor` (string, optional)
    An arbitrary string to be displayed on your customer’s credit card or bank statement. While most banks display this information consistently, some may display it incorrectly or not at all.

    This may be up to 22 characters. The statement description may not include `<`, `>`, `\`, `"`, `'` characters, and will appear on your customer’s statement in capital letters. Non-ASCII characters are automatically stripped.

  - `product_data.tax_code` (string, recommended if calculating taxes)
    A [tax code](https://docs.stripe.com/docs/tax/tax-categories.md) ID.

  - `product_data.unit_label` (string, optional)
    A label that represents units of this product. When set, this will be included in customers’ receipts, invoices, Checkout, and the customer portal.

    The maximum length is 12 characters.

- `recurring` (object, optional)
  The recurring components of a price such as `interval` and `usage_type`.

  - `recurring.interval` (enum, required)
    Specifies billing frequency. Either `day`, `week`, `month` or `year`.
Possible enum values:
    - `day`
    - `month`
    - `week`
    - `year`

  - `recurring.interval_count` (integer, optional)
    The number of intervals between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of three years interval allowed (3 years, 36 months, or 156 weeks).

  - `recurring.meter` (string, optional)
    The meter tracking the usage of a metered price

  - `recurring.usage_type` (enum, optional)
    Configures how the quantity per period should be determined. Can be either `metered` or `licensed`. `licensed` automatically bills the `quantity` set when adding it to a subscription. `metered` aggregates the total usage based on usage records. Defaults to `licensed`.
Possible enum values:
    - `licensed`
    - `metered`

- `tax_behavior` (enum, recommended if calculating taxes)
  Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
Possible enum values:
  - `exclusive`
  - `inclusive`
  - `unspecified`

- `tiers` (array of objects, Required if billing_scheme=tiered)
  Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`.

  - `tiers.up_to` (string | integer, required)
    Specifies the upper bound of this tier. The lower bound of a tier is the upper bound of the previous tier adding one. Use `inf` to define a fallback tier.

  - `tiers.flat_amount` (integer, optional)
    The flat billing amount for an entire tier, regardless of the number of units in the tier.

  - `tiers.flat_amount_decimal` (string, optional)
    Same as `flat_amount`, but accepts a decimal value representing an integer in the minor units of the currency. Only one of `flat_amount` and `flat_amount_decimal` can be set.

  - `tiers.unit_amount` (integer, optional)
    The per unit billing amount for each individual unit for which this tier applies.

  - `tiers.unit_amount_decimal` (string, optional)
    Same as `unit_amount`, but accepts a decimal value in cents with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.

- `tiers_mode` (enum, Required if billing_scheme=tiered)
  Defines if the tiering price should be `graduated` or `volume` based. In `volume`-based tiering, the maximum quantity within a period determines the per unit price, in `graduated` tiering pricing can successively change as the quantity grows.

- `transfer_lookup_key` (boolean, optional)
  If set to true, will atomically remove the lookup key from the existing price, and assign it to this price.

- `transform_quantity` (object, optional)
  Apply a transformation to the reported usage or set quantity before computing the billed price. Cannot be combined with `tiers`.

  - `transform_quantity.divide_by` (integer, required)
    Divide usage by this number.

  - `transform_quantity.round` (enum, required)
    After division, either round the result `up` or `down`.

- `unit_amount` (integer, Required conditionally)
  A positive integer in cents (or 0 for a free price) representing how much to charge. One of `unit_amount`, `unit_amount_decimal`, or `custom_unit_amount` is required, unless `billing_scheme=tiered`.

- `unit_amount_decimal` (string, optional)
  Same as `unit_amount`, but accepts a decimal value in cents with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.

```curl
curl https://api.stripe.com/v1/prices \
  -u "<<YOUR_SECRET_KEY>>" \
  -d currency=usd \
  -d unit_amount=1000 \
  -d "recurring[interval]"=month \
  -d "product_data[name]"="Gold Plan"
```

```cli
stripe prices create  \
  --currency=usd \
  --unit-amount=1000 \
  -d "recurring[interval]"=month \
  -d "product_data[name]"="Gold Plan"
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

price = client.v1.prices.create({
  currency: 'usd',
  unit_amount: 1000,
  recurring: {interval: 'month'},
  product_data: {name: 'Gold Plan'},
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

price = client.v1.prices.create({
  "currency": "usd",
  "unit_amount": 1000,
  "recurring": {"interval": "month"},
  "product_data": {"name": "Gold Plan"},
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$price = $stripe->prices->create([
  'currency' => 'usd',
  'unit_amount' => 1000,
  'recurring' => ['interval' => 'month'],
  'product_data' => ['name' => 'Gold Plan'],
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PriceCreateParams params =
  PriceCreateParams.builder()
    .setCurrency("usd")
    .setUnitAmount(1000L)
    .setRecurring(
      PriceCreateParams.Recurring.builder()
        .setInterval(PriceCreateParams.Recurring.Interval.MONTH)
        .build()
    )
    .setProductData(
      PriceCreateParams.ProductData.builder().setName("Gold Plan").build()
    )
    .build();

Price price = client.v1().prices().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const price = await stripe.prices.create({
  currency: 'usd',
  unit_amount: 1000,
  recurring: {
    interval: 'month',
  },
  product_data: {
    name: 'Gold Plan',
  },
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PriceCreateParams{
  Currency: stripe.String(stripe.CurrencyUSD),
  UnitAmount: stripe.Int64(1000),
  Recurring: &stripe.PriceCreateRecurringParams{
    Interval: stripe.String(stripe.PriceRecurringIntervalMonth),
  },
  ProductData: &stripe.PriceCreateProductDataParams{
    Name: stripe.String("Gold Plan"),
  },
}
result, err := sc.V1Prices.Create(context.TODO(), params)
```

```dotnet
var options = new PriceCreateOptions
{
    Currency = "usd",
    UnitAmount = 1000,
    Recurring = new PriceRecurringOptions { Interval = "month" },
    ProductData = new PriceProductDataOptions { Name = "Gold Plan" },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Prices;
Price price = service.Create(options);
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
  "metadata": {},
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