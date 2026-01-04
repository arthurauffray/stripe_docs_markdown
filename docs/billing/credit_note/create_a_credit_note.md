# Create a credit note

Issue a credit note to adjust the amount of a finalized invoice. A credit note will first reduce the invoice’s `amount_remaining` (and `amount_due`), but not below zero. This amount is indicated by the credit note’s `pre_payment_amount`. The excess amount is indicated by `post_payment_amount`, and it can result in any combination of the following:

- Refunds: create a new refund (using `refund_amount`) or link existing refunds (using `refunds`).
- Customer balance credit: credit the customer’s balance (using `credit_amount`) which will be automatically applied to their next invoice when it’s finalized.
- Outside of Stripe credit: record the amount that is or will be credited outside of Stripe (using `out_of_band_amount`).

The sum of refunds, customer balance credits, and outside of Stripe credits must equal the `post_payment_amount`.

You may issue multiple credit notes for an invoice. Each credit note may increment the invoice’s `pre_payment_credit_notes_amount`, `post_payment_credit_notes_amount`, or both, depending on the invoice’s `amount_remaining` at the time of credit note creation.

## Returns

Returns a credit note object if the call succeeded.

## Parameters

- `invoice` (string, required)
  ID of the invoice.

- `amount` (integer, required conditionally)
  The integer amount in cents representing the total amount of the credit note. One of `amount`, `lines`, or `shipping_cost` must be provided.

- `credit_amount` (integer, optional)
  The integer amount in cents representing the amount to credit the customer’s balance, which will be automatically applied to their next invoice.

- `effective_at` (timestamp, optional)
  The date when this credit note is in effect. Same as `created` unless overwritten. When defined, this value replaces the system-generated ‘Date of issue’ printed on the credit note PDF.

- `email_type` (enum, optional)
  Type of email to send to the customer, one of `credit_note` or `none` and the default is `credit_note`.
Possible enum values:
  - `credit_note`
    credit note email

  - `none`
    no email

- `lines` (array of objects, required conditionally)
  Line items that make up the credit note. One of `amount`, `lines`, or `shipping_cost` must be provided.

  - `lines.type` (enum, required)
    Type of the credit note line item, one of `invoice_line_item` or `custom_line_item`
Possible enum values:
    - `custom_line_item`
    - `invoice_line_item`

  - `lines.amount` (integer, optional)
    The line item amount to credit. Only valid when `type` is `invoice_line_item`. If invoice is set up with `automatic_tax[enabled]=true`, this amount is tax exclusive

  - `lines.description` (string, optional)
    The description of the credit note line item. Only valid when the `type` is `custom_line_item`.

  - `lines.invoice_line_item` (string, optional)
    The invoice line item to credit. Only valid when the `type` is `invoice_line_item`.

  - `lines.quantity` (integer, optional)
    The line item quantity to credit.

  - `lines.tax_amounts` (array of objects, optional)
    A list of up to 10 tax amounts for the credit note line item. Cannot be mixed with `tax_rates`.

    - `lines.tax_amounts.amount` (integer, required)
      The amount, in cents, of the tax.

    - `lines.tax_amounts.tax_rate` (string, required)
      The id of the tax rate for this tax amount. The tax rate must have been automatically created by Stripe.

    - `lines.tax_amounts.taxable_amount` (integer, required)
      The amount on which tax is calculated, in cents.

  - `lines.tax_rates` (array of strings, optional)
    The tax rates which apply to the credit note line item. Only valid when the `type` is `custom_line_item` and cannot be mixed with `tax_amounts`.

  - `lines.unit_amount` (integer, optional)
    The integer unit amount in cents of the credit note line item. This `unit_amount` will be multiplied by the quantity to get the full amount to credit for this line item. Only valid when `type` is `custom_line_item`.

  - `lines.unit_amount_decimal` (string, optional)
    Same as `unit_amount`, but accepts a decimal value in cents with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.

- `memo` (string, optional)
  The credit note’s memo appears on the credit note PDF.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `out_of_band_amount` (integer, optional)
  The integer amount in cents representing the amount that is credited outside of Stripe.

- `reason` (enum, optional)
  Reason for issuing this credit note, one of `duplicate`, `fraudulent`, `order_change`, or `product_unsatisfactory`
Possible enum values:
  - `duplicate`
    Credit issued for a duplicate payment or charge

  - `fraudulent`
    Credit note issued for fraudulent activity

  - `order_change`
    Credit note issued for order change

  - `product_unsatisfactory`
    Credit note issued for unsatisfactory product

- `refund_amount` (integer, optional)
  The integer amount in cents representing the amount to refund. If set, a refund will be created for the charge associated with the invoice.

- `refunds` (array of objects, optional)
  Refunds to link to this credit note.

  - `refunds.amount_refunded` (integer, optional)
    Amount of the refund that applies to this credit note, in cents. Defaults to the entire refund amount.

  - `refunds.payment_record_refund` (object, optional)
    The PaymentRecord refund details to link to this credit note. Required when `type` is `payment_record_refund`.

    - `refunds.payment_record_refund.payment_record` (string, required)
      The ID of the PaymentRecord with the refund to link to this credit note.

    - `refunds.payment_record_refund.refund_group` (string, required)
      The PaymentRecord refund group to link to this credit note. For refunds processed off-Stripe, this will correspond to the `processor_details.custom.refund_reference` field provided when reporting the refund on the PaymentRecord.

  - `refunds.refund` (string, optional)
    ID of an existing refund to link this credit note to. Required when `type` is `refund`.

  - `refunds.type` (enum, optional)
    Type of the refund, one of `refund` or `payment_record_refund`. Defaults to `refund`.
Possible enum values:
    - `payment_record_refund`
      The refund being linked to this credit note is a payment record refund

    - `refund`
      The refund being linked to this credit note is a regular refund

- `shipping_cost` (object, required conditionally)
  When shipping_cost contains the shipping_rate from the invoice, the shipping_cost is included in the credit note. One of `amount`, `lines`, or `shipping_cost` must be provided.

  - `shipping_cost.shipping_rate` (string, required if shipping cost should be included for credit note)
    The ID of the shipping rate to use for this order.

```curl
curl https://api.stripe.com/v1/credit_notes \
  -u "<<YOUR_SECRET_KEY>>" \
  -d invoice=in_1MxvRkLkdIwHu7ixABNtI99m
```

```cli
stripe credit_notes create  \
  --invoice=in_1MxvRkLkdIwHu7ixABNtI99m
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

credit_note = client.v1.credit_notes.create({invoice: 'in_1MxvRkLkdIwHu7ixABNtI99m'})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

credit_note = client.v1.credit_notes.create({
  "invoice": "in_1MxvRkLkdIwHu7ixABNtI99m",
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$creditNote = $stripe->creditNotes->create([
  'invoice' => 'in_1MxvRkLkdIwHu7ixABNtI99m',
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CreditNoteCreateParams params =
  CreditNoteCreateParams.builder().setInvoice("in_1MxvRkLkdIwHu7ixABNtI99m").build();

CreditNote creditNote = client.v1().creditNotes().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const creditNote = await stripe.creditNotes.create({
  invoice: 'in_1MxvRkLkdIwHu7ixABNtI99m',
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CreditNoteCreateParams{
  Invoice: stripe.String("in_1MxvRkLkdIwHu7ixABNtI99m"),
}
result, err := sc.V1CreditNotes.Create(context.TODO(), params)
```

```dotnet
var options = new CreditNoteCreateOptions
{
    Invoice = "in_1MxvRkLkdIwHu7ixABNtI99m",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.CreditNotes;
CreditNote creditNote = service.Create(options);
```

### Response

```json
{
  "id": "cn_1MxvRqLkdIwHu7ixY0xbUcxk",
  "object": "credit_note",
  "amount": 1099,
  "amount_shipping": 0,
  "created": 1681750958,
  "currency": "usd",
  "customer": "cus_NjLgPhUokHubJC",
  "customer_balance_transaction": null,
  "discount_amount": 0,
  "discount_amounts": [],
  "invoice": "in_1MxvRkLkdIwHu7ixABNtI99m",
  "lines": {
    "object": "list",
    "data": [
      {
        "id": "cnli_1MxvRqLkdIwHu7ixFpdhBFQf",
        "object": "credit_note_line_item",
        "amount": 1099,
        "description": "T-shirt",
        "discount_amount": 0,
        "discount_amounts": [],
        "invoice_line_item": "il_1MxvRlLkdIwHu7ixnkbntxUV",
        "livemode": false,
        "quantity": 1,
        "tax_rates": [],
        "taxes": [],
        "type": "invoice_line_item",
        "unit_amount": 1099,
        "unit_amount_decimal": "1099"
      }
    ],
    "has_more": false,
    "url": "/v1/credit_notes/cn_1MxvRqLkdIwHu7ixY0xbUcxk/lines"
  },
  "livemode": false,
  "memo": null,
  "metadata": {},
  "number": "C9E0C52C-0036-CN-01",
  "out_of_band_amount": null,
  "pdf": "https://pay.stripe.com/credit_notes/acct_1M2JTkLkdIwHu7ix/test_YWNjdF8xTTJKVGtMa2RJd0h1N2l4LF9Oak9FOUtQNFlPdk52UXhFd2Z4SU45alpEd21kd0Y4LDcyMjkxNzU50200cROQsSK2/pdf?s=ap",
  "pre_payment_amount": 1099,
  "post_payment_amount": 0,
  "reason": null,
  "refunds": [],
  "shipping_cost": null,
  "status": "issued",
  "subtotal": 1099,
  "subtotal_excluding_tax": 1099,
  "total": 1099,
  "total_excluding_tax": 1099,
  "total_taxes": [],
  "type": "pre_payment",
  "voided_at": null
}
```