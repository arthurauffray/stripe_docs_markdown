# The Tax Rate object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `active` (boolean)
  Defaults to `true`. When set to `false`, this tax rate cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.

- `country` (string, nullable)
  Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `description` (string, nullable)
  An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.

- `display_name` (string)
  The display name of the tax rates as it will appear to your customer on their receipt email, PDF, and the hosted invoice page.

- `effective_percentage` (float, nullable)
  Actual/effective tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true, this percentage reflects the rate actually used to calculate tax based on the product’s taxability and whether the user is registered to collect taxes in the corresponding jurisdiction.

- `flat_amount` (object, nullable)
  The amount of the tax rate when the `rate_type` is `flat_amount`. Tax rates with `rate_type` `percentage` can vary based on the transaction, resulting in this field being `null`. This field exposes the amount and currency of the flat tax rate.

  - `flat_amount.amount` (integer)
    Amount of the tax when the `rate_type` is `flat_amount`. This positive integer represents how much to charge in the smallest currency unit (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).

  - `flat_amount.currency` (string)
    Three-letter ISO currency code, in lowercase.

- `inclusive` (boolean)
  This specifies if the tax rate is inclusive or exclusive.

- `jurisdiction` (string, nullable)
  The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.

- `jurisdiction_level` (enum, nullable)
  The level of the jurisdiction that imposes this tax rate. Will be `null` for manually defined tax rates.
Possible enum values:
  - `city`
  - `country`
  - `county`
  - `district`
  - `multiple`
  - `state`

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (object, nullable)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `percentage` (float)
  Tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true, this percentage includes the statutory tax rate of non-taxable jurisdictions.

- `rate_type` (enum, nullable)
  Indicates the type of tax rate applied to the taxable amount. This value can be `null` when no tax applies to the location. This field is only present for TaxRates created by Stripe Tax.
Possible enum values:
  - `flat_amount`
    A fixed amount applied as tax, regardless of the taxable amount, such as a retail delivery fee.

  - `percentage`
    A tax rate expressed as a percentage of the taxable amount, such as the sales tax rate in California.

- `state` (string, nullable)
  [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2), without country prefix. For example, “NY” for New York, United States.

- `tax_type` (enum, nullable)
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

### The Tax Rate object

```json
{
  "id": "txr_1MzS4RLkdIwHu7ixwvpZ9c2i",
  "object": "tax_rate",
  "active": true,
  "country": null,
  "created": 1682114687,
  "description": "VAT Germany",
  "display_name": "VAT",
  "inclusive": false,
  "jurisdiction": "DE",
  "livemode": false,
  "metadata": {},
  "percentage": 16,
  "state": null,
  "tax_type": null
}
```