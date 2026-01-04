# Bulk remove invoice line items

Removes multiple line items from an invoice. This is only possible when an invoice is still a draft.

## Returns

The updated invoice without the removed line items is returned upon success. Otherwise, this call raises [an error](https://docs.stripe.com/api/invoice-line-item/invoices/remove-lines/bulk.md#errors).

## Parameters

- `lines` (array of objects, required)
  The line items to remove.

  - `lines.behavior` (enum, required)
    Either `delete` or `unassign`. Deleted line items are permanently deleted. Unassigned line items can be reassigned to an invoice.
Possible enum values:
    - `delete`
      The line item is removed from the invoice and deleted.

    - `unassign`
      The line item is removed from the invoice and moved into a pending state.

  - `lines.id` (string, required)
    ID of an existing line item to remove from this invoice.

- `invoice_metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/invoices/in_1NuhUa2eZvKYlo2CWYVhyvD9/remove_lines \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "lines[0][id]"=il_1NuhUa2eZvKYlo2CC98Fg3Bo \
  -d "lines[0][behavior]"=delete \
  -d "lines[1][id]"=il_1NuLVe2eZvKYlo2Canh35EfU \
  -d "lines[1][behavior]"=unassign
```

```cli
stripe invoices remove_lines in_1NuhUa2eZvKYlo2CWYVhyvD9 \
  -d "lines[0][id]"=il_1NuhUa2eZvKYlo2CC98Fg3Bo \
  -d "lines[0][behavior]"=delete \
  -d "lines[1][id]"=il_1NuLVe2eZvKYlo2Canh35EfU \
  -d "lines[1][behavior]"=unassign
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

invoice = client.v1.invoices.remove_lines(
  'in_1NuhUa2eZvKYlo2CWYVhyvD9',
  {
    lines: [
      {
        id: 'il_1NuhUa2eZvKYlo2CC98Fg3Bo',
        behavior: 'delete',
      },
      {
        id: 'il_1NuLVe2eZvKYlo2Canh35EfU',
        behavior: 'unassign',
      },
    ],
  },
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

invoice = client.v1.invoices.remove_lines(
  "in_1NuhUa2eZvKYlo2CWYVhyvD9",
  {
    "lines": [
      {"id": "il_1NuhUa2eZvKYlo2CC98Fg3Bo", "behavior": "delete"},
      {"id": "il_1NuLVe2eZvKYlo2Canh35EfU", "behavior": "unassign"},
    ],
  },
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$invoice = $stripe->invoices->removeLines(
  'in_1NuhUa2eZvKYlo2CWYVhyvD9',
  [
    'lines' => [
      [
        'id' => 'il_1NuhUa2eZvKYlo2CC98Fg3Bo',
        'behavior' => 'delete',
      ],
      [
        'id' => 'il_1NuLVe2eZvKYlo2Canh35EfU',
        'behavior' => 'unassign',
      ],
    ],
  ]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

InvoiceRemoveLinesParams params =
  InvoiceRemoveLinesParams.builder()
    .addLine(
      InvoiceRemoveLinesParams.Line.builder()
        .setId("il_1NuhUa2eZvKYlo2CC98Fg3Bo")
        .setBehavior(InvoiceRemoveLinesParams.Line.Behavior.DELETE)
        .build()
    )
    .addLine(
      InvoiceRemoveLinesParams.Line.builder()
        .setId("il_1NuLVe2eZvKYlo2Canh35EfU")
        .setBehavior(InvoiceRemoveLinesParams.Line.Behavior.UNASSIGN)
        .build()
    )
    .build();

Invoice invoice =
  client.v1().invoices().removeLines("in_1NuhUa2eZvKYlo2CWYVhyvD9", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const invoice = await stripe.invoices.removeLines(
  'in_1NuhUa2eZvKYlo2CWYVhyvD9',
  {
    lines: [
      {
        id: 'il_1NuhUa2eZvKYlo2CC98Fg3Bo',
        behavior: 'delete',
      },
      {
        id: 'il_1NuLVe2eZvKYlo2Canh35EfU',
        behavior: 'unassign',
      },
    ],
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.InvoiceRemoveLinesParams{
  Lines: []*stripe.InvoiceRemoveLinesLineParams{
    &stripe.InvoiceRemoveLinesLineParams{
      ID: stripe.String("il_1NuhUa2eZvKYlo2CC98Fg3Bo"),
      Behavior: stripe.String("delete"),
    },
    &stripe.InvoiceRemoveLinesLineParams{
      ID: stripe.String("il_1NuLVe2eZvKYlo2Canh35EfU"),
      Behavior: stripe.String("unassign"),
    },
  },
}
result, err := sc.V1Invoices.RemoveLines(
  context.TODO(), "in_1NuhUa2eZvKYlo2CWYVhyvD9", params)
```

```dotnet
var options = new InvoiceRemoveLinesOptions
{
    Lines = new List<InvoiceLineOptions>
    {
        new InvoiceLineOptions
        {
            Id = "il_1NuhUa2eZvKYlo2CC98Fg3Bo",
            Behavior = "delete",
        },
        new InvoiceLineOptions
        {
            Id = "il_1NuLVe2eZvKYlo2Canh35EfU",
            Behavior = "unassign",
        },
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Invoices;
Invoice invoice = service.RemoveLines("in_1NuhUa2eZvKYlo2CWYVhyvD9", options);
```

### Response

```json
{
  "id": "in_1NuhUa2eZvKYlo2CWYVhyvD9",
  "object": "invoice",
  "account_country": "US",
  "account_name": "Stripe.com",
  "account_tax_ids": null,
  "amount_due": 998,
  "amount_paid": 0,
  "amount_overpaid": 0,
  "amount_remaining": 998,
  "amount_shipping": 0,
  "application": null,
  "attempt_count": 0,
  "attempted": false,
  "auto_advance": false,
  "automatic_tax": {
    "enabled": false,
    "liability": null,
    "status": null
  },
  "billing_reason": "manual",
  "collection_method": "charge_automatically",
  "created": 1695758664,
  "currency": "usd",
  "custom_fields": null,
  "customer": "cus_9s6XKzkNRiz8i3",
  "customer_address": null,
  "customer_email": "test@test.com",
  "customer_name": null,
  "customer_phone": null,
  "customer_shipping": null,
  "customer_tax_exempt": "none",
  "customer_tax_ids": [],
  "default_payment_method": null,
  "default_source": null,
  "default_tax_rates": [],
  "description": null,
  "discounts": [],
  "due_date": null,
  "effective_at": null,
  "ending_balance": null,
  "footer": null,
  "from_invoice": null,
  "hosted_invoice_url": null,
  "invoice_pdf": null,
  "issuer": {
    "type": "self"
  },
  "last_finalization_error": null,
  "latest_revision": null,
  "lines": {
    "object": "list",
    "data": [
      {
        "id": "il_1NuhUa2eZvKYlo2CC98Fg3Bo",
        "object": "line_item",
        "amount": 799,
        "currency": "usd",
        "description": "test description",
        "discount_amounts": [],
        "discountable": true,
        "discounts": [],
        "livemode": false,
        "metadata": {},
        "parent": {
          "type": "invoice_item_details",
          "invoice_item_details": {
            "invoice_item": "ii_1NuhUa2eZvKYlo2CGeF7Qgx0",
            "proration": false,
            "proration_details": {
              "credited_items": null
            },
            "subscription": null
          }
        },
        "period": {
          "end": 1695758664,
          "start": 1695758664
        },
        "pricing": {
          "price_details": {
            "price": "price_1NuhLA2eZvKYlo2Cq1tIGEBp",
            "product": "prod_Oi7aO1GPi1dWX7"
          },
          "type": "price_details",
          "unit_amount_decimal": "799"
        },
        "quantity": 1,
        "taxes": []
      },
      {
        "id": "il_1NuLVe2eZvKYlo2Canh35EfU",
        "object": "line_item",
        "amount": 199,
        "currency": "usd",
        "description": "Canned Coffee",
        "discount_amounts": [],
        "discountable": true,
        "discounts": [],
        "livemode": false,
        "metadata": {},
        "parent": {
          "type": "invoice_item_details",
          "invoice_item_details": {
            "invoice_item": "ii_1NuLVd2eZvKYlo2CRWY0Hqgi",
            "proration": false,
            "proration_details": {
              "credited_items": null
            },
            "subscription": null
          }
        },
        "period": {
          "end": 1695674161,
          "start": 1695674161
        },
        "pricing": {
          "price_details": {
            "price": "price_1NuI212eZvKYlo2CWgdD8kET",
            "product": "prod_OhhQNWDYdIbXYv"
          },
          "type": "price_details",
          "unit_amount_decimal": "199"
        },
        "quantity": 1,
        "taxes": []
      }
    ],
    "has_more": false,
    "url": "/v1/invoices/upcoming/lines?customer=cus_9s6XKzkNRiz8i3"
  },
  "livemode": false,
  "metadata": {},
  "next_payment_attempt": null,
  "number": null,
  "on_behalf_of": null,
  "parent": null,
  "payment_settings": {
    "default_mandate": null,
    "payment_method_options": null,
    "payment_method_types": null
  },
  "period_end": 1688482163,
  "period_start": 1688395763,
  "post_payment_credit_notes_amount": 0,
  "pre_payment_credit_notes_amount": 0,
  "receipt_number": null,
  "redaction": null,
  "rendering": null,
  "shipping_cost": null,
  "shipping_details": null,
  "starting_balance": 0,
  "statement_descriptor": null,
  "status": "draft",
  "status_transitions": {
    "finalized_at": null,
    "marked_uncollectible_at": null,
    "paid_at": null,
    "voided_at": null
  },
  "subtotal": 998,
  "subtotal_excluding_tax": 998,
  "test_clock": null,
  "total": 998,
  "total_discount_amounts": [],
  "total_excluding_tax": 998,
  "total_taxes": [],
  "webhooks_delivered_at": null
}
```