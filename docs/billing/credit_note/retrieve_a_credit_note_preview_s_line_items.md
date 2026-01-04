# Retrieve a credit note preview's line items

When retrieving a credit note preview, you’ll get a **lines** property containing the first handful of those items. This URL you can retrieve the full (paginated) list of line items.

## Returns

Returns a list of [line_item objects](https://docs.stripe.com/api/credit_notes/preview_lines.md#credit_note_line_item_object).

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

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

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

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/credit_notes/preview/lines \
  -u "<<YOUR_SECRET_KEY>>" \
  -d invoice=in_1Nn8592eZvKYlo2Ci4yFC46f
```

```cli
stripe credit_notes preview_lines  \
  --invoice=in_1Nn8592eZvKYlo2Ci4yFC46f
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

credit_note_line_items = client.v1.credit_notes.preview_lines.list({
  invoice: 'in_1Nn8592eZvKYlo2Ci4yFC46f',
})
```

```python
stripe.api_key = "<<YOUR_SECRET_KEY>>"

stripe.CreditNote.preview(
  invoice="in_1Nn8cq2eZvKYlo2CNDpusCKy",
  lines=[
    {
      "type": "invoice_line_item",
      "invoice_line_item": "il_1Nn8cq2eZvKYlo2CidbpuBZa",
      "quantity": 1,
    },
  ],
)
credit_note = stripe.CreditNote.retrieve('cn_1Nn8cq2eZvKYlo2C6rIUxWuM')
lines = credit_note.lines.list(limit=5)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$creditNoteLineItems = $stripe->creditNotes->previewLines([
  'invoice' => 'in_1Nn8592eZvKYlo2Ci4yFC46f',
]);
```

```java
Stripe.apiKey = "<<YOUR_SECRET_KEY>>";

List<Object> lines = new ArrayList<>();
Map<String, Object> line1 = new HashMap<>();
line1.put("type", "invoice_line_item");
line1.put("invoice_line_item", "il_1Nn8kH2eZvKYlo2CWxizx0jH");
line1.put("quantity", 1);
lines.add(line1);
Map<String, Object> params = new HashMap<>();
params.put("invoice", "in_1Nn8kH2eZvKYlo2CtNPfxvBa");
params.put("lines", lines);

CreditNote creditNote = CreditNote.preview(params);

creditNote.getLines().list();
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const creditNoteLineItems = await stripe.creditNotes.listPreviewLineItems({
  invoice: 'in_1Nn8592eZvKYlo2Ci4yFC46f',
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CreditNotePreviewLinesParams{
  Invoice: stripe.String("in_1Nn8592eZvKYlo2Ci4yFC46f"),
}
result := sc.V1CreditNotes.PreviewLines(context.TODO(), params)
```

```dotnet
var options = new CreditNotePreviewLinesListOptions
{
    Invoice = "in_1Nn8592eZvKYlo2Ci4yFC46f",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.CreditNotes.PreviewLines;
StripeList<CreditNoteLineItem> creditNoteLineItems = service.List(options);
```

### Response

```json
{
  "id": "cn_1Nn7fB2eZvKYlo2CuJ0wZBlA",
  "object": "credit_note",
  "amount": 1451,
  "amount_shipping": 0,
  "created": 1693952641,
  "currency": "usd",
  "customer": "cus_9s6XKzkNRiz8i3",
  "customer_balance_transaction": null,
  "discount_amount": 0,
  "discount_amounts": [],
  "effective_at": null,
  "invoice": "in_1Nn7fB2eZvKYlo2C7meA67Xp",
  "lines": {
    "object": "list",
    "data": [
      {
        "id": "cnli_1Nn7fB2eZvKYlo2Cp8nLMci9",
        "object": "credit_note_line_item",
        "amount": 951,
        "description": "My First Invoice Item (created for API docs)",
        "discount_amount": 0,
        "discount_amounts": [],
        "invoice_line_item": "il_1Nn7fB2eZvKYlo2ChKG2H1tv",
        "livemode": false,
        "quantity": 1,
        "tax_rates": [
          {
            "id": "txr_1Nn7fB2eZvKYlo2CcbF7zzmD",
            "object": "tax_rate",
            "active": true,
            "country": "DE",
            "created": 1693952641,
            "description": "VAT Germany",
            "display_name": "VAT",
            "effective_percentage": null,
            "inclusive": false,
            "jurisdiction": "DE",
            "livemode": false,
            "metadata": {},
            "percentage": 19,
            "state": null,
            "tax_type": "vat"
          }
        ],
        "taxes": [
          {
            "amount": 152,
            "tax_behavior": "exclusive",
            "tax_rate_details": {
              "tax_rate": "txr_1Nn7fB2eZvKYlo2CcbF7zzmD"
            },
            "taxability_reason": "not_available",
            "taxable_amount": 799,
            "type": "tax_rate_details"
          }
        ],
        "type": "invoice_line_item",
        "unit_amount": null,
        "unit_amount_decimal": null
      },
      {
        "id": "cnli_1Nn7fB2eZvKYlo2C7OxQLHdz",
        "object": "credit_note_line_item",
        "amount": 500,
        "description": "Service credit",
        "discount_amount": 0,
        "discount_amounts": [],
        "livemode": false,
        "quantity": 1,
        "tax_rates": [],
        "taxes": [],
        "type": "custom_line_item",
        "unit_amount": 500,
        "unit_amount_decimal": "500"
      }
    ],
    "has_more": false,
    "url": "/v1/credit_notes/cn_1Nn7fB2eZvKYlo2CuJ0wZBlA/lines"
  },
  "livemode": false,
  "memo": null,
  "metadata": {},
  "number": "ABCD-1234-CN-01",
  "out_of_band_amount": null,
  "pdf": "https://pay.stripe.com/credit_notes/acct_1032D82eZvKYlo2C/cnst_123456789/pdf?s=ap",
  "reason": null,
  "refund": null,
  "shipping_cost": null,
  "status": "issued",
  "subtotal": 1451,
  "subtotal_excluding_tax": 1451,
  "total": 1451,
  "total_excluding_tax": null,
  "total_taxes": [
    {
      "amount": 152,
      "tax_behavior": "exclusive",
      "tax_rate_details": {
        "tax_rate": "txr_1Nn7fB2eZvKYlo2CcbF7zzmD"
      },
      "taxability_reason": "not_available",
      "taxable_amount": 799,
      "type": "tax_rate_details"
    }
  ],
  "type": "pre_payment",
  "voided_at": null
}
```