# The Invoice Item object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `amount` (integer)
  Amount (in the `currency` specified) of the invoice item. This should always be equal to `unit_amount * quantity`.

- `currency` (enum)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `customer` (string)
  The ID of the customer to bill for this invoice item.

- `customer_account` (string, nullable)
  The ID of the account to bill for this invoice item.

- `date` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `description` (string, nullable)
  An arbitrary string attached to the object. Often useful for displaying to users.

- `discountable` (boolean)
  If true, discounts will apply to this invoice item. Always false for prorations.

- `discounts` (array of strings, nullable)
  The discounts which apply to the invoice item. Item discounts are applied before invoice discounts. Use `expand[]=discounts` to expand each discount.

- `invoice` (string, nullable)
  The ID of the invoice this invoice item belongs to.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (object, nullable)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `net_amount` (integer, nullable)
  The amount after discounts, but before credits and taxes. This field is `null` for `discountable=true` items.

- `parent` (object, nullable)
  The parent that generated this invoice item.

  - `parent.subscription_details` (object, nullable)
    Details about the subscription that generated this invoice item

    - `parent.subscription_details.subscription` (string)
      The subscription that generated this invoice item

    - `parent.subscription_details.subscription_item` (string, nullable)
      The subscription item that generated this invoice item

  - `parent.type` (enum)
    The type of parent that generated this invoice item
Possible enum values:
    - `subscription_details`
      Details of the parent can be found in the `subscription_details` hash.

- `period` (object)
  The period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you have [Stripe Revenue Recognition](https://docs.stripe.com/docs/revenue-recognition.md) enabled, the period will be used to recognize and defer revenue. See the [Revenue Recognition documentation](https://docs.stripe.com/docs/revenue-recognition/methodology/subscriptions-and-invoicing.md) for details.

  - `period.end` (timestamp)
    The end of the period, which must be greater than or equal to the start. This value is inclusive.

  - `period.start` (timestamp)
    The start of the period. This value is inclusive.

- `pricing` (object, nullable)
  The pricing information of the invoice item.

  - `pricing.price_details` (object, nullable)
    Additional details about the price this item is associated with. This is present only when the `type` is `price_details`

    - `pricing.price_details.price` (string)
      The ID of the price this item is associated with.

    - `pricing.price_details.product` (string)
      The ID of the product this item is associated with.

  - `pricing.type` (enum)
    The type of the pricing details.

  - `pricing.unit_amount_decimal` (decimal string, nullable)
    The unit amount (in the `currency` specified) of the item which contains a decimal value with at most 12 decimal places.

- `proration` (boolean)
  Whether the invoice item was created automatically as a proration adjustment when the customer switched plans.

- `proration_details` (object, nullable)
  Contains information about proration items. This field is only populated for prorations created from subscriptions with `billing_mode=flexible`.

  - `proration_details.discount_amounts` (array of objects)
    Discount amounts applied when the proration was created.

    - `proration_details.discount_amounts.amount` (integer)
      The amount, in cents, of the discount.

    - `proration_details.discount_amounts.discount` (string)
      The discount that was applied to get this discount amount.

- `quantity` (integer)
  Quantity of units for the invoice item. If the invoice item is a proration, the quantity of the subscription that the proration was computed for.

- `tax_rates` (array of objects, nullable)
  The tax rates which apply to the invoice item. When set, the `default_tax_rates` on the invoice do not apply to this invoice item.

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

- `test_clock` (string, nullable)
  ID of the test clock this invoice item belongs to.

### The Invoice Item object

```json
{
  "id": "ii_1MtGUtLkdIwHu7ixBYwjAM00",
  "object": "invoiceitem",
  "amount": 1099,
  "currency": "usd",
  "customer": "cus_NeZei8imSbMVvi",
  "date": 1680640231,
  "description": "T-shirt",
  "discountable": true,
  "discounts": [],
  "invoice": null,
  "livemode": false,
  "metadata": {},
  "parent": null,
  "period": {
    "end": 1680640231,
    "start": 1680640231
  },
  "pricing": {
    "price_details": {
      "price": "price_1MtGUsLkdIwHu7ix1be5Ljaj",
      "product": "prod_NeZe7xbBdJT8EN"
    },
    "type": "price_details",
    "unit_amount_decimal": "1099"
  },
  "proration": false,
  "quantity": 1,
  "tax_rates": [],
  "test_clock": null
}
```