# The Price object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `active` (boolean)
  Whether the price can be used for new purchases.

- `billing_scheme` (enum)
  Describes how to compute the price per period. Either `per_unit` or `tiered`. `per_unit` indicates that the fixed amount (specified in `unit_amount` or `unit_amount_decimal`) will be charged per unit in `quantity` (for prices with `usage_type=licensed`), or per unit of total usage (for prices with `usage_type=metered`). `tiered` indicates that the unit pricing will be computed using a tiering strategy as defined using the `tiers` and `tiers_mode` attributes.
Possible enum values:
  - `per_unit`
  - `tiered`

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (enum)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `currency_options` (object, nullable)
  Prices defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).

  - `currency_options.<currency>.custom_unit_amount` (object, nullable)
    When set, provides configuration for the amount to be adjusted by the customer during Checkout Sessions and Payment Links.

    - `currency_options.<currency>.custom_unit_amount.maximum` (integer, nullable)
      The maximum unit amount the customer can specify for this item.

    - `currency_options.<currency>.custom_unit_amount.minimum` (integer, nullable)
      The minimum unit amount the customer can specify for this item. Must be at least the minimum charge amount.

    - `currency_options.<currency>.custom_unit_amount.preset` (integer, nullable)
      The starting unit amount which can be updated by the customer.

  - `currency_options.<currency>.tax_behavior` (enum, nullable)
    Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
Possible enum values:
    - `exclusive`
    - `inclusive`
    - `unspecified`

  - `currency_options.<currency>.tiers` (array of objects, nullable)
    Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`.

    - `currency_options.<currency>.tiers.flat_amount` (integer, nullable)
      Price for the entire tier.

    - `currency_options.<currency>.tiers.flat_amount_decimal` (decimal string, nullable)
      Same as `flat_amount`, but contains a decimal value with at most 12 decimal places.

    - `currency_options.<currency>.tiers.unit_amount` (integer, nullable)
      Per unit price for units relevant to the tier.

    - `currency_options.<currency>.tiers.unit_amount_decimal` (decimal string, nullable)
      Same as `unit_amount`, but contains a decimal value with at most 12 decimal places.

    - `currency_options.<currency>.tiers.up_to` (integer, nullable)
      Up to and including to this quantity will be contained in the tier.

  - `currency_options.<currency>.unit_amount` (integer, nullable)
    The unit amount in cents to be charged, represented as a whole integer if possible. Only set if `billing_scheme=per_unit`.

  - `currency_options.<currency>.unit_amount_decimal` (decimal string, nullable)
    The unit amount in cents to be charged, represented as a decimal string with at most 12 decimal places. Only set if `billing_scheme=per_unit`.

- `custom_unit_amount` (object, nullable)
  When set, provides configuration for the amount to be adjusted by the customer during Checkout Sessions and Payment Links.

  - `custom_unit_amount.maximum` (integer, nullable)
    The maximum unit amount the customer can specify for this item.

  - `custom_unit_amount.minimum` (integer, nullable)
    The minimum unit amount the customer can specify for this item. Must be at least the minimum charge amount.

  - `custom_unit_amount.preset` (integer, nullable)
    The starting unit amount which can be updated by the customer.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `lookup_key` (string, nullable)
  A lookup key used to retrieve prices dynamically from a static string. This may be up to 200 characters.

- `metadata` (object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `nickname` (string, nullable)
  A brief description of the price, hidden from customers.

- `product` (string)
  The ID of the product this price is associated with.

- `recurring` (object, nullable)
  The recurring components of a price such as `interval` and `usage_type`.

  - `recurring.interval` (enum)
    The frequency at which a subscription is billed. One of `day`, `week`, `month` or `year`.

  - `recurring.interval_count` (integer)
    The number of intervals (specified in the `interval` attribute) between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months.

  - `recurring.meter` (string, nullable)
    The meter tracking the usage of a metered price

  - `recurring.usage_type` (enum)
    Configures how the quantity per period should be determined. Can be either `metered` or `licensed`. `licensed` automatically bills the `quantity` set when adding it to a subscription. `metered` aggregates the total usage based on usage records. Defaults to `licensed`.

- `tax_behavior` (enum, nullable)
  Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
Possible enum values:
  - `exclusive`
  - `inclusive`
  - `unspecified`

- `tiers` (array of objects, nullable)
  Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`.

  - `tiers.flat_amount` (integer, nullable)
    Price for the entire tier.

  - `tiers.flat_amount_decimal` (decimal string, nullable)
    Same as `flat_amount`, but contains a decimal value with at most 12 decimal places.

  - `tiers.unit_amount` (integer, nullable)
    Per unit price for units relevant to the tier.

  - `tiers.unit_amount_decimal` (decimal string, nullable)
    Same as `unit_amount`, but contains a decimal value with at most 12 decimal places.

  - `tiers.up_to` (integer, nullable)
    Up to and including to this quantity will be contained in the tier.

- `tiers_mode` (enum, nullable)
  Defines if the tiering price should be `graduated` or `volume` based. In `volume`-based tiering, the maximum quantity within a period determines the per unit price. In `graduated` tiering, pricing can change as the quantity grows.
Possible enum values:
  - `graduated`
  - `volume`

- `transform_quantity` (object, nullable)
  Apply a transformation to the reported usage or set quantity before computing the amount billed. Cannot be combined with `tiers`.

  - `transform_quantity.divide_by` (integer)
    Divide usage by this number.

  - `transform_quantity.round` (enum)
    After division, either round the result `up` or `down`.

- `type` (enum)
  One of `one_time` or `recurring` depending on whether the price is for a one-time purchase or a recurring (subscription) purchase.
Possible enum values:
  - `one_time`
  - `recurring`

- `unit_amount` (integer, nullable)
  The unit amount in cents to be charged, represented as a whole integer if possible. Only set if `billing_scheme=per_unit`.

- `unit_amount_decimal` (decimal string, nullable)
  The unit amount in cents to be charged, represented as a decimal string with at most 12 decimal places. Only set if `billing_scheme=per_unit`.

### The Price object

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