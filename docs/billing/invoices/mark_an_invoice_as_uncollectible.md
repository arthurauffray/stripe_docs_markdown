# Mark an invoice as uncollectible

Marking an invoice as uncollectible is useful for keeping track of bad debts that can be written off for accounting purposes.

## Returns

Returns the invoice object.

```curl
curl -X POST https://api.stripe.com/v1/invoices/in_1MtG0nLkdIwHu7ixAaUw3Cb4/mark_uncollectible \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe invoices mark_uncollectible in_1MtG0nLkdIwHu7ixAaUw3Cb4
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

invoice = client.v1.invoices.mark_uncollectible('in_1MtG0nLkdIwHu7ixAaUw3Cb4')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

invoice = client.v1.invoices.mark_uncollectible("in_1MtG0nLkdIwHu7ixAaUw3Cb4")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$invoice = $stripe->invoices->markUncollectible('in_1MtG0nLkdIwHu7ixAaUw3Cb4', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

InvoiceMarkUncollectibleParams params =
  InvoiceMarkUncollectibleParams.builder().build();

Invoice invoice =
  client.v1().invoices().markUncollectible("in_1MtG0nLkdIwHu7ixAaUw3Cb4", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const invoice = await stripe.invoices.markUncollectible(
  'in_1MtG0nLkdIwHu7ixAaUw3Cb4'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.InvoiceMarkUncollectibleParams{}
result, err := sc.V1Invoices.MarkUncollectible(
  context.TODO(), "in_1MtG0nLkdIwHu7ixAaUw3Cb4", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Invoices;
Invoice invoice = service.MarkUncollectible("in_1MtG0nLkdIwHu7ixAaUw3Cb4");
```

### Response

```json
{
  "id": "in_1MtG0nLkdIwHu7ixAaUw3Cb4",
  "object": "invoice",
  "account_country": "US",
  "account_name": "Stripe Docs",
  "account_tax_ids": null,
  "amount_due": 599,
  "amount_paid": 0,
  "amount_overpaid": 0,
  "amount_remaining": 599,
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
  "created": 1680638365,
  "currency": "usd",
  "custom_fields": null,
  "customer": "cus_NeZw0zvTyquTfF",
  "customer_address": null,
  "customer_email": "jennyrosen@example.com",
  "customer_name": "Jenny Rosen",
  "customer_phone": null,
  "customer_shipping": null,
  "customer_tax_exempt": "none",
  "customer_tax_ids": [
    {
      "type": "eu_vat",
      "value": "DE123456789"
    },
    {
      "type": "eu_vat",
      "value": "DE123456781"
    }
  ],
  "default_payment_method": null,
  "default_source": null,
  "default_tax_rates": [],
  "description": null,
  "discounts": [],
  "due_date": null,
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
        "id": "il_1MtG0nLkdIwHu7ix3eCoIIw7",
        "object": "line_item",
        "amount": 1099,
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
            "invoice_item": "ii_1MtG0nLkdIwHu7ixDqfiUgg8",
            "proration": false,
            "proration_details": {
              "credited_items": null
            },
            "subscription": null
          }
        },
        "period": {
          "end": 1680638365,
          "start": 1680638365
        },
        "pricing": {
          "price_details": {
            "price": "price_1Mr89PLkdIwHu7ixf5QhiWm2",
            "product": "prod_NcMtLgctyqlJDC"
          },
          "type": "price_details",
          "unit_amount_decimal": "1099"
        },
        "quantity": 1,
        "taxes": []
      }
    ],
    "has_more": false,
    "url": "/v1/invoices/in_1MtG0nLkdIwHu7ixAaUw3Cb4/lines"
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
  "period_end": 1680638365,
  "period_start": 1680638365,
  "post_payment_credit_notes_amount": 0,
  "pre_payment_credit_notes_amount": 0,
  "receipt_number": null,
  "shipping_cost": null,
  "shipping_details": null,
  "starting_balance": -500,
  "statement_descriptor": null,
  "status": "uncollectible",
  "status_transitions": {
    "finalized_at": null,
    "marked_uncollectible_at": null,
    "paid_at": null,
    "voided_at": null
  },
  "subtotal": 1099,
  "subtotal_excluding_tax": 1099,
  "test_clock": null,
  "total": 1099,
  "total_discount_amounts": [],
  "total_excluding_tax": 1099,
  "total_taxes": [],
  "webhooks_delivered_at": null,
  "closed": true,
  "forgiven": true
}
```