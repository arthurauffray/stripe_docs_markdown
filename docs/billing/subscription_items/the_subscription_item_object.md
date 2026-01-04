# The Subscription Item object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `billing_thresholds` (object, nullable)
  Define thresholds at which an invoice will be sent, and the related subscription advanced to a new billing period

  - `billing_thresholds.usage_gte` (integer, nullable)
    Usage threshold that triggers the subscription to create an invoice

- `created` (integer)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `current_period_end` (timestamp)
  The end time of this subscription item’s current billing period.

- `current_period_start` (timestamp)
  The start time of this subscription item’s current billing period.

- `discounts` (array of strings)
  The discounts applied to the subscription item. Subscription item discounts are applied before subscription discounts. Use `expand[]=discounts` to expand each discount.

- `metadata` (object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `price` (object)
  The price the customer is subscribed to.

  - `price.id` (string)
    Unique identifier for the object.

  - `price.object` (string)
    String representing the object’s type. Objects of the same type share the same value.

  - `price.active` (boolean)
    Whether the price can be used for new purchases.

  - `price.billing_scheme` (enum)
    Describes how to compute the price per period. Either `per_unit` or `tiered`. `per_unit` indicates that the fixed amount (specified in `unit_amount` or `unit_amount_decimal`) will be charged per unit in `quantity` (for prices with `usage_type=licensed`), or per unit of total usage (for prices with `usage_type=metered`). `tiered` indicates that the unit pricing will be computed using a tiering strategy as defined using the `tiers` and `tiers_mode` attributes.
Possible enum values:
    - `per_unit`
    - `tiered`

  - `price.created` (timestamp)
    Time at which the object was created. Measured in seconds since the Unix epoch.

  - `price.currency` (enum)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `price.currency_options` (object, nullable)
    Prices defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).

    - `price.currency_options.<currency>.custom_unit_amount` (object, nullable)
      When set, provides configuration for the amount to be adjusted by the customer during Checkout Sessions and Payment Links.

      - `price.currency_options.<currency>.custom_unit_amount.maximum` (integer, nullable)
        The maximum unit amount the customer can specify for this item.

      - `price.currency_options.<currency>.custom_unit_amount.minimum` (integer, nullable)
        The minimum unit amount the customer can specify for this item. Must be at least the minimum charge amount.

      - `price.currency_options.<currency>.custom_unit_amount.preset` (integer, nullable)
        The starting unit amount which can be updated by the customer.

    - `price.currency_options.<currency>.tax_behavior` (enum, nullable)
      Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
Possible enum values:
      - `exclusive`
      - `inclusive`
      - `unspecified`

    - `price.currency_options.<currency>.tiers` (array of objects, nullable)
      Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`.

      - `price.currency_options.<currency>.tiers.flat_amount` (integer, nullable)
        Price for the entire tier.

      - `price.currency_options.<currency>.tiers.flat_amount_decimal` (decimal string, nullable)
        Same as `flat_amount`, but contains a decimal value with at most 12 decimal places.

      - `price.currency_options.<currency>.tiers.unit_amount` (integer, nullable)
        Per unit price for units relevant to the tier.

      - `price.currency_options.<currency>.tiers.unit_amount_decimal` (decimal string, nullable)
        Same as `unit_amount`, but contains a decimal value with at most 12 decimal places.

      - `price.currency_options.<currency>.tiers.up_to` (integer, nullable)
        Up to and including to this quantity will be contained in the tier.

    - `price.currency_options.<currency>.unit_amount` (integer, nullable)
      The unit amount in cents to be charged, represented as a whole integer if possible. Only set if `billing_scheme=per_unit`.

    - `price.currency_options.<currency>.unit_amount_decimal` (decimal string, nullable)
      The unit amount in cents to be charged, represented as a decimal string with at most 12 decimal places. Only set if `billing_scheme=per_unit`.

  - `price.custom_unit_amount` (object, nullable)
    When set, provides configuration for the amount to be adjusted by the customer during Checkout Sessions and Payment Links.

    - `price.custom_unit_amount.maximum` (integer, nullable)
      The maximum unit amount the customer can specify for this item.

    - `price.custom_unit_amount.minimum` (integer, nullable)
      The minimum unit amount the customer can specify for this item. Must be at least the minimum charge amount.

    - `price.custom_unit_amount.preset` (integer, nullable)
      The starting unit amount which can be updated by the customer.

  - `price.livemode` (boolean)
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

  - `price.lookup_key` (string, nullable)
    A lookup key used to retrieve prices dynamically from a static string. This may be up to 200 characters.

  - `price.metadata` (object)
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

  - `price.nickname` (string, nullable)
    A brief description of the price, hidden from customers.

  - `price.product` (string)
    The ID of the product this price is associated with.

  - `price.recurring` (object, nullable)
    The recurring components of a price such as `interval` and `usage_type`.

    - `price.recurring.interval` (enum)
      The frequency at which a subscription is billed. One of `day`, `week`, `month` or `year`.

    - `price.recurring.interval_count` (integer)
      The number of intervals (specified in the `interval` attribute) between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months.

    - `price.recurring.meter` (string, nullable)
      The meter tracking the usage of a metered price

    - `price.recurring.usage_type` (enum)
      Configures how the quantity per period should be determined. Can be either `metered` or `licensed`. `licensed` automatically bills the `quantity` set when adding it to a subscription. `metered` aggregates the total usage based on usage records. Defaults to `licensed`.

  - `price.tax_behavior` (enum, nullable)
    Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
Possible enum values:
    - `exclusive`
    - `inclusive`
    - `unspecified`

  - `price.tiers` (array of objects, nullable)
    Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`.

    - `price.tiers.flat_amount` (integer, nullable)
      Price for the entire tier.

    - `price.tiers.flat_amount_decimal` (decimal string, nullable)
      Same as `flat_amount`, but contains a decimal value with at most 12 decimal places.

    - `price.tiers.unit_amount` (integer, nullable)
      Per unit price for units relevant to the tier.

    - `price.tiers.unit_amount_decimal` (decimal string, nullable)
      Same as `unit_amount`, but contains a decimal value with at most 12 decimal places.

    - `price.tiers.up_to` (integer, nullable)
      Up to and including to this quantity will be contained in the tier.

  - `price.tiers_mode` (enum, nullable)
    Defines if the tiering price should be `graduated` or `volume` based. In `volume`-based tiering, the maximum quantity within a period determines the per unit price. In `graduated` tiering, pricing can change as the quantity grows.
Possible enum values:
    - `graduated`
    - `volume`

  - `price.transform_quantity` (object, nullable)
    Apply a transformation to the reported usage or set quantity before computing the amount billed. Cannot be combined with `tiers`.

    - `price.transform_quantity.divide_by` (integer)
      Divide usage by this number.

    - `price.transform_quantity.round` (enum)
      After division, either round the result `up` or `down`.

  - `price.type` (enum)
    One of `one_time` or `recurring` depending on whether the price is for a one-time purchase or a recurring (subscription) purchase.
Possible enum values:
    - `one_time`
    - `recurring`

  - `price.unit_amount` (integer, nullable)
    The unit amount in cents to be charged, represented as a whole integer if possible. Only set if `billing_scheme=per_unit`.

  - `price.unit_amount_decimal` (decimal string, nullable)
    The unit amount in cents to be charged, represented as a decimal string with at most 12 decimal places. Only set if `billing_scheme=per_unit`.

- `quantity` (integer, nullable)
  The [quantity](https://docs.stripe.com/docs/subscriptions/quantities.md) of the plan to which the customer should be subscribed.

- `subscription` (string)
  The `subscription` this `subscription_item` belongs to.

- `tax_rates` (array of objects, nullable)
  The tax rates which apply to this `subscription_item`. When set, the `default_tax_rates` on the subscription do not apply to this `subscription_item`.

  - `tax_rates.id` (string)
    Unique identifier for the object.

  - `tax_rates.object` (string)
    String representing the object’s type. Objects of the same type share the same value.

  - `tax_rates.active` (boolean)
    Defaults to `true`. When set to `false`, this tax rate cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.

  - `tax_rates.country` (string, nullable)
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

  - `tax_rates.created` (timestamp)
    Time at which the object was created. Measured in seconds since the Unix epoch.

  - `tax_rates.description` (string, nullable)
    An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.

  - `tax_rates.display_name` (string)
    The display name of the tax rates as it will appear to your customer on their receipt email, PDF, and the hosted invoice page.

  - `tax_rates.effective_percentage` (float, nullable)
    Actual/effective tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true, this percentage reflects the rate actually used to calculate tax based on the product’s taxability and whether the user is registered to collect taxes in the corresponding jurisdiction.

  - `tax_rates.flat_amount` (object, nullable)
    The amount of the tax rate when the `rate_type` is `flat_amount`. Tax rates with `rate_type` `percentage` can vary based on the transaction, resulting in this field being `null`. This field exposes the amount and currency of the flat tax rate.

    - `tax_rates.flat_amount.amount` (integer)
      Amount of the tax when the `rate_type` is `flat_amount`. This positive integer represents how much to charge in the smallest currency unit (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).

    - `tax_rates.flat_amount.currency` (string)
      Three-letter ISO currency code, in lowercase.

  - `tax_rates.inclusive` (boolean)
    This specifies if the tax rate is inclusive or exclusive.

  - `tax_rates.jurisdiction` (string, nullable)
    The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.

  - `tax_rates.jurisdiction_level` (enum, nullable)
    The level of the jurisdiction that imposes this tax rate. Will be `null` for manually defined tax rates.
Possible enum values:
    - `city`
    - `country`
    - `county`
    - `district`
    - `multiple`
    - `state`

  - `tax_rates.livemode` (boolean)
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

  - `tax_rates.metadata` (object, nullable)
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

  - `tax_rates.percentage` (float)
    Tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true, this percentage includes the statutory tax rate of non-taxable jurisdictions.

  - `tax_rates.rate_type` (enum, nullable)
    Indicates the type of tax rate applied to the taxable amount. This value can be `null` when no tax applies to the location. This field is only present for TaxRates created by Stripe Tax.
Possible enum values:
    - `flat_amount`
      A fixed amount applied as tax, regardless of the taxable amount, such as a retail delivery fee.

    - `percentage`
      A tax rate expressed as a percentage of the taxable amount, such as the sales tax rate in California.

  - `tax_rates.state` (string, nullable)
    [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2), without country prefix. For example, “NY” for New York, United States.

  - `tax_rates.tax_type` (enum, nullable)
    The high-level tax type, such as `vat` or `sales_tax`.
Possible enum values:
    - `amusement_tax`
      Amusement Tax

    - `communications_tax`
      Communications Tax

    - `gst`
      Goods and Services Tax

    - `hst`
      Harmonized Sales Tax

    - `igst`
      Integrated Goods and Services Tax

    - `jct`
      Japanese Consumption Tax

    - `lease_tax`
      Chicago Lease Tax

    - `pst`
      Provincial Sales Tax

    - `qst`
      Quebec Sales Tax

    - `retail_delivery_fee`
      Retail Delivery Fee

    - `rst`
      Retail Sales Tax

    - `sales_tax`
      Sales Tax

    - `service_tax`
      Service Tax

    - `vat`
      Value-Added Tax

### The Subscription Item object

```json
{
  "id": "si_NcLYdDxLHxlFo7",
  "object": "subscription_item",
  "created": 1680126546,
  "metadata": {},
  "price": {
    "id": "price_1Mr6rdLkdIwHu7ixwPmiybbR",
    "object": "price",
    "active": true,
    "billing_scheme": "per_unit",
    "created": 1680126545,
    "currency": "usd",
    "custom_unit_amount": null,
    "discounts": null,
    "livemode": false,
    "lookup_key": null,
    "metadata": {},
    "nickname": null,
    "product": "prod_NcLYGKH0eY5b8s",
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
  },
  "quantity": 2,
  "subscription": "sub_1Mr6rbLkdIwHu7ix4Xm9Ahtd",
  "tax_rates": []
}
```