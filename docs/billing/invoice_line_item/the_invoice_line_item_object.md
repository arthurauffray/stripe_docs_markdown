# The Invoice Line Item object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `amount` (integer)
  The amount, in cents.

- `currency` (enum)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `description` (string, nullable)
  An arbitrary string attached to the object. Often useful for displaying to users.

- `discount_amounts` (array of objects, nullable)
  The amount of discount calculated per discount for this line item.

  - `discount_amounts.amount` (integer)
    The amount, in cents, of the discount.

  - `discount_amounts.discount` (string)
    The discount that was applied to get this discount amount.

- `discountable` (boolean)
  If true, discounts will apply to this line item. Always false for prorations.

- `discounts` (array of strings)
  The discounts applied to the invoice line item. Line item discounts are applied before invoice discounts. Use `expand[]=discounts` to expand each discount.

- `invoice` (string, nullable)
  The ID of the invoice that contains this line item.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Note that for line items with `type=subscription`, `metadata` reflects the current metadata from the subscription associated with the line item, unless the invoice line was directly updated with different metadata after creation.

- `parent` (object, nullable)
  The parent that generated this line item.

  - `parent.invoice_item_details` (object, nullable)
    Details about the invoice item that generated this line item

    - `parent.invoice_item_details.invoice_item` (string)
      The invoice item that generated this line item

    - `parent.invoice_item_details.proration` (boolean)
      Whether this is a proration

    - `parent.invoice_item_details.proration_details` (object, nullable)
      Additional details for proration line items

      - `parent.invoice_item_details.proration_details.credited_items` (object, nullable)
        For a credit proration `line_item`, the original debit line_items to which the credit proration applies.

        - `parent.invoice_item_details.proration_details.credited_items.invoice` (string)
          Invoice containing the credited invoice line items

        - `parent.invoice_item_details.proration_details.credited_items.invoice_line_items` (array of strings)
          Credited invoice line items

    - `parent.invoice_item_details.subscription` (string, nullable)
      The subscription that the invoice item belongs to

  - `parent.subscription_item_details` (object, nullable)
    Details about the subscription item that generated this line item

    - `parent.subscription_item_details.invoice_item` (string, nullable)
      The invoice item that generated this line item

    - `parent.subscription_item_details.proration` (boolean)
      Whether this is a proration

    - `parent.subscription_item_details.proration_details` (object, nullable)
      Additional details for proration line items

      - `parent.subscription_item_details.proration_details.credited_items` (object, nullable)
        For a credit proration `line_item`, the original debit line_items to which the credit proration applies.

        - `parent.subscription_item_details.proration_details.credited_items.invoice` (string)
          Invoice containing the credited invoice line items

        - `parent.subscription_item_details.proration_details.credited_items.invoice_line_items` (array of strings)
          Credited invoice line items

    - `parent.subscription_item_details.subscription` (string, nullable)
      The subscription that the subscription item belongs to

    - `parent.subscription_item_details.subscription_item` (string)
      The subscription item that generated this line item

  - `parent.type` (enum)
    The type of parent that generated this line item
Possible enum values:
    - `invoice_item_details`
      Details of the parent can be found in the `invoice_item_details` hash.

    - `subscription_item_details`
      Details of the parent can be found in the `subscription_item_details` hash.

- `period` (object)
  The period this `line_item` covers. For subscription line items, this is the subscription period. For prorations, this starts when the proration was calculated, and ends at the period end of the subscription. For invoice items, this is the time at which the invoice item was created or the period of the item. If you have [Stripe Revenue Recognition](https://docs.stripe.com/docs/revenue-recognition.md) enabled, the period will be used to recognize and defer revenue. See the [Revenue Recognition documentation](https://docs.stripe.com/docs/revenue-recognition/methodology/subscriptions-and-invoicing.md) for details.

  - `period.end` (timestamp)
    The end of the period, which must be greater than or equal to the start. This value is inclusive.

  - `period.start` (timestamp)
    The start of the period. This value is inclusive.

- `pretax_credit_amounts` (array of objects, nullable)
  Contains pretax credit amounts (ex: discount, credit grants, etc) that apply to this line item.

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

- `pricing` (object, nullable)
  The pricing information of the line item.

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

- `quantity` (integer, nullable)
  The quantity of the subscription, if the line item is a subscription or a proration.

- `subtotal` (integer)
  The subtotal of the line item, in cents, before any discounts or taxes.

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

### The Invoice Line Item object

```json
{
  "id": "il_tmp_1Nzo1ZGgdF1VjufLzD1UUn9R",
  "object": "line_item",
  "amount": 1000,
  "currency": "usd",
  "description": "My First Invoice Item (created for API docs)",
  "discount_amounts": [],
  "discountable": true,
  "discounts": [],
  "livemode": false,
  "metadata": {},
  "parent": {
    "type": "invoice_item_details",
    "invoice_item_details": {
      "invoice_item": "ii_1NpHiK2eZvKYlo2C9NdV8VrI",
      "proration": false,
      "proration_details": {
        "credited_items": null
      },
      "subscription": null
    }
  },
  "period": {
    "end": 1696975413,
    "start": 1696975413
  },
  "pricing": {
    "price_details": {
      "price": "price_1NzlYfGgdF1VjufL0cVjLJVI",
      "product": "prod_OnMHDH6VBmYlTr"
    },
    "type": "price_details",
    "unit_amount_decimal": "1000"
  },
  "quantity": 1,
  "taxes": []
}
```