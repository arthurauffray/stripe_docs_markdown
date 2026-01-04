# The Credit Note Line Item object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `amount` (integer)
  The integer amount in cents representing the gross amount being credited for this line item, excluding (exclusive) tax and discounts.

- `description` (string, nullable)
  Description of the item being credited.

- `discount_amount` (integer)
  The integer amount in cents representing the discount being credited for this line item.

- `discount_amounts` (array of objects)
  The amount of discount calculated per discount for this line item

  - `discount_amounts.amount` (integer)
    The amount, in cents, of the discount.

  - `discount_amounts.discount` (string)
    The discount that was applied to get this discount amount.

- `invoice_line_item` (string, nullable)
  ID of the invoice line item being credited

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `pretax_credit_amounts` (array of objects)
  The pretax credit amounts (ex: discount, credit grants, etc) for this line item.

  - `pretax_credit_amounts.amount` (integer)
    The amount, in cents, of the pretax credit amount.

  - `pretax_credit_amounts.credit_balance_transaction` (string, nullable)
    The credit balance transaction that was applied to get this pretax credit amount.

  - `pretax_credit_amounts.discount` (string, nullable)
    The discount that was applied to get this pretax credit amount.

  - `pretax_credit_amounts.type` (enum)
    Type of the pretax credit amount referenced.
Possible enum values:
    - `credit_balance_transaction`
      The pretax credit amount is from a credit balance transaction.

    - `discount`
      The pretax credit amount is from a discount.

- `quantity` (integer, nullable)
  The number of units of product being credited.

- `tax_rates` (array of objects)
  The tax rates which apply to the line item.

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

- `taxes` (array of objects, nullable)
  The tax information of the line item.

  - `taxes.amount` (integer)
    The amount of the tax, in cents.

  - `taxes.tax_behavior` (enum)
    Whether this tax is inclusive or exclusive.
Possible enum values:
    - `exclusive`
    - `inclusive`

  - `taxes.tax_rate_details` (object, nullable)
    Additional details about the tax rate. Only present when `type` is `tax_rate_details`.

    - `taxes.tax_rate_details.tax_rate` (string)
      ID of the tax rate

  - `taxes.taxability_reason` (enum)
    The reasoning behind this tax, for example, if the product is tax exempt. The possible values for this field may be extended as new tax rules are supported.
Possible enum values:
    - `customer_exempt`
      No tax is applied as the customer is exempt from tax.

    - `not_available`
      The reasoning behind this tax is not available.

    - `not_collecting`
      No tax is collected either because you are not registered to collect tax in this jurisdiction, or because the non-taxable product tax code (`txcd_00000000`) was used.

    - `not_subject_to_tax`
      No tax is imposed on this transaction.

    - `not_supported`
      No tax applied. Stripe doesn’t support this jurisdiction, territory, or product.

    - `portion_product_exempt`
      A portion of the price is exempt from tax.

    - `portion_reduced_rated`
      A portion of the price is taxed at a reduced rate.

    - `portion_standard_rated`
      A portion of the price is taxed at the standard rate.

    - `product_exempt`
      The product or service is nontaxable or exempt from tax.

    - `product_exempt_holiday`
      The product or service is not taxed due to a sales tax holiday.

    - `proportionally_rated`
      The shipping cost tax rate is calculated as a weighted average of the other line items’ rates, weighted by their amounts.

    - `reduced_rated`
      Taxed at a reduced rate.

    - `reverse_charge`
      No tax is applied as it is the responsibility of the buyer to account for tax in this case.

    - `standard_rated`
      Taxed at the standard rate.

    - `taxable_basis_reduced`
      A reduced amount of the price is subject to tax.

    - `zero_rated`
      The transaction is taxed at a special rate of 0% or the transaction is exempt (but these exempt transactions still let you deduct the “input VAT” paid on your business purchases).

  - `taxes.taxable_amount` (integer, nullable)
    The amount on which tax is calculated, in cents.

  - `taxes.type` (enum)
    The type of tax information.

- `type` (enum)
  The type of the credit note line item, one of `invoice_line_item` or `custom_line_item`. When the type is `invoice_line_item` there is an additional `invoice_line_item` property on the resource the value of which is the id of the credited line item on the invoice.
Possible enum values:
  - `custom_line_item`
  - `invoice_line_item`

- `unit_amount` (integer, nullable)
  The cost of each unit of product being credited.

- `unit_amount_decimal` (decimal string, nullable)
  Same as `unit_amount`, but contains a decimal value with at most 12 decimal places.

### The Credit Note Line Item object

```json
{
  "id": "cnli_1NPtOx2eZvKYlo2CBH1NpUsU",
  "object": "credit_note_line_item",
  "amount": 749,
  "description": "My First Invoice Item (created for API docs)",
  "discount_amount": 0,
  "discount_amounts": [],
  "invoice_line_item": "il_1NPtOx2eZvKYlo2CAUuq0WVl",
  "livemode": false,
  "quantity": 1,
  "taxes": [],
  "tax_rates": [],
  "type": "invoice_line_item",
  "unit_amount": null,
  "unit_amount_decimal": null
}
```