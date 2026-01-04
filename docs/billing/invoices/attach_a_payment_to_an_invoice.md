# Attach a payment to an Invoice

Attaches a PaymentIntent or an Out of Band Payment to the invoice, adding it to the list of `payments`.

For the PaymentIntent, when the PaymentIntent’s status changes to `succeeded`, the payment is credited to the invoice, increasing its `amount_paid`. When the invoice is fully paid, the invoice’s status becomes `paid`.

If the PaymentIntent’s status is already `succeeded` when it’s attached, it’s credited to the invoice immediately.

See: [Partial payments](https://docs.stripe.com/docs/invoicing/partial-payments.md) to learn more.

## Returns

Returns the invoice object that the payment was attached to.

## Parameters

- `payment_intent` (string, optional)
  The ID of the PaymentIntent to attach to the invoice.

- `payment_record` (string, optional)
  The ID of the PaymentRecord to attach to the invoice.

```curl
curl https://api.stripe.com/v1/invoices/in_1Nj68C2eZvKYlo2CGmFJak8q/attach_payment \
  -u "<<YOUR_SECRET_KEY>>" \
  -d payment_intent=pi_1GszwY2eZvKYlo2CohCEmT6b \
  -d "expand[]"=payments
```

```cli
stripe invoices attach_payment in_1Nj68C2eZvKYlo2CGmFJak8q \
  --payment-intent=pi_1GszwY2eZvKYlo2CohCEmT6b \
  -d "expand[0]"=payments
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

invoice = client.v1.invoices.attach_payment(
  'in_1Nj68C2eZvKYlo2CGmFJak8q',
  {
    payment_intent: 'pi_1GszwY2eZvKYlo2CohCEmT6b',
    expand: ['payments'],
  },
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

invoice = client.v1.invoices.attach_payment(
  "in_1Nj68C2eZvKYlo2CGmFJak8q",
  {"payment_intent": "pi_1GszwY2eZvKYlo2CohCEmT6b", "expand": ["payments"]},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$invoice = $stripe->invoices->attachPayment(
  'in_1Nj68C2eZvKYlo2CGmFJak8q',
  [
    'payment_intent' => 'pi_1GszwY2eZvKYlo2CohCEmT6b',
    'expand' => ['payments'],
  ]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

InvoiceAttachPaymentParams params =
  InvoiceAttachPaymentParams.builder()
    .setPaymentIntent("pi_1GszwY2eZvKYlo2CohCEmT6b")
    .addExpand("payments")
    .build();

Invoice invoice =
  client.v1().invoices().attachPayment("in_1Nj68C2eZvKYlo2CGmFJak8q", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const invoice = await stripe.invoices.attachPayment(
  'in_1Nj68C2eZvKYlo2CGmFJak8q',
  {
    payment_intent: 'pi_1GszwY2eZvKYlo2CohCEmT6b',
    expand: ['payments'],
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.InvoiceAttachPaymentParams{
  PaymentIntent: stripe.String("pi_1GszwY2eZvKYlo2CohCEmT6b"),
}
params.AddExpand("payments")
result, err := sc.V1Invoices.AttachPayment(
  context.TODO(), "in_1Nj68C2eZvKYlo2CGmFJak8q", params)
```

```dotnet
var options = new InvoiceAttachPaymentOptions
{
    PaymentIntent = "pi_1GszwY2eZvKYlo2CohCEmT6b",
    Expand = new List<string> { "payments" },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Invoices;
Invoice invoice = service.AttachPayment("in_1Nj68C2eZvKYlo2CGmFJak8q", options);
```

### Response

```json
{
  "id": "in_1Nj68C2eZvKYlo2CGmFJak8q",
  "object": "invoice",
  "account_country": "US",
  "account_name": "Stripe.com",
  "account_tax_ids": null,
  "amount_due": 1299,
  "amount_paid": 0,
  "amount_overpaid": 0,
  "amount_remaining": 1299,
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
  "created": 1692993440,
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
        "id": "il_1Nj68C2eZvKYlo2C7fRlh2gN",
        "object": "line_item",
        "amount": 1299,
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
            "invoice_item": "ii_1Nj68C2eZvKYlo2CTeCUHDgE",
            "proration": false,
            "proration_details": {
              "credited_items": null
            },
            "subscription": null
          }
        },
        "period": {
          "end": 1692993440,
          "start": 1692993440
        },
        "pricing": {
          "price_details": {
            "price": "price_1Nj5c82eZvKYlo2CfVgOGez4",
            "product": "prod_OW7r6RmADUSO13"
          },
          "type": "price_details",
          "unit_amount_decimal": "1299"
        },
        "quantity": 1,
        "taxes": []
      }
    ],
    "has_more": false,
    "url": "/v1/invoices/in_1Nj68C2eZvKYlo2CGmFJak8q/lines"
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
  "payments": {
    "object": "list",
    "data": [
      {
        "id": "inpay_1M3USa2eZvKYlo2CBjuwbq0N",
        "object": "invoice_payment",
        "amount_paid": 2000,
        "amount_requested": 2000,
        "created": 1391288554,
        "currency": "usd",
        "invoice": "in_1Nj68C2eZvKYlo2CGmFJak8q",
        "is_default": true,
        "livemode": false,
        "payment": {
          "type": "payment_intent",
          "payment_intent": "pi_1GszwY2eZvKYlo2CohCEmT6b"
        },
        "status": "paid",
        "status_transitions": {
          "canceled_at": null,
          "paid_at": 1391288554
        }
      }
    ],
    "has_more": false,
    "url": "/v1/invoices/in_1Nj68C2eZvKYlo2CGmFJak8q/payments"
  },
  "period_end": 1688482163,
  "period_start": 1688395763,
  "post_payment_credit_notes_amount": 0,
  "pre_payment_credit_notes_amount": 0,
  "receipt_number": null,
  "redaction": null,
  "shipping_cost": null,
  "shipping_details": null,
  "starting_balance": 0,
  "statement_descriptor": null,
  "status": "open",
  "status_transitions": {
    "finalized_at": null,
    "marked_uncollectible_at": null,
    "paid_at": null,
    "voided_at": null
  },
  "subtotal": 1299,
  "subtotal_excluding_tax": 1299,
  "test_clock": null,
  "total": 1299,
  "total_discount_amounts": [],
  "total_excluding_tax": 1299,
  "total_taxes": [],
  "transfer_data": null,
  "webhooks_delivered_at": null
}
```