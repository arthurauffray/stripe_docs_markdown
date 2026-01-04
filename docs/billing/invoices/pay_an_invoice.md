# Pay an invoice

Stripe automatically creates and then attempts to collect payment on invoices for customers on subscriptions according to your [subscriptions settings](https://dashboard.stripe.com/account/billing/automatic). However, if you’d like to attempt payment on an invoice out of the normal collection schedule or for some other reason, you can do so.

## Returns

Returns the invoice object.

## Parameters

- `forgive` (boolean, optional)
  In cases where the source used to pay the invoice has insufficient funds, passing `forgive=true` controls whether a charge should be attempted for the full amount available on the source, up to the amount to fully pay the invoice. This effectively forgives the difference between the amount available on the source and the amount due.

  Passing `forgive=false` will fail the charge if the source hasn’t been pre-funded with the right amount. An example for this case is with ACH Credit Transfers and wires: if the amount wired is less than the amount due by a small amount, you might want to forgive the difference. Defaults to `false`.

- `mandate` (string, optional)
  ID of the mandate to be used for this invoice. It must correspond to the payment method used to pay the invoice, including the payment_method param or the invoice’s default_payment_method or default_source, if set.

- `off_session` (boolean, optional)
  Indicates if a customer is on or off-session while an invoice payment is attempted. Defaults to `true` (off-session).

- `paid_out_of_band` (boolean, optional)
  Boolean representing whether an invoice is paid outside of Stripe. This will result in no charge being made. Defaults to `false`.

- `payment_method` (string, optional)
  A PaymentMethod to be charged. The PaymentMethod must be the ID of a PaymentMethod belonging to the customer associated with the invoice being paid.

- `source` (string, optional)
  A payment source to be charged. The source must be the ID of a source belonging to the customer associated with the invoice being paid.

```curl
curl -X POST https://api.stripe.com/v1/invoices/in_1MtGmCLkdIwHu7ix6PgS6g8S/pay \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe invoices pay in_1MtGmCLkdIwHu7ix6PgS6g8S
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

invoice = client.v1.invoices.pay('in_1MtGmCLkdIwHu7ix6PgS6g8S')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

invoice = client.v1.invoices.pay("in_1MtGmCLkdIwHu7ix6PgS6g8S")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$invoice = $stripe->invoices->pay('in_1MtGmCLkdIwHu7ix6PgS6g8S', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

InvoicePayParams params = InvoicePayParams.builder().build();

Invoice invoice = client.v1().invoices().pay("in_1MtGmCLkdIwHu7ix6PgS6g8S", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const invoice = await stripe.invoices.pay('in_1MtGmCLkdIwHu7ix6PgS6g8S');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.InvoicePayParams{}
result, err := sc.V1Invoices.Pay(
  context.TODO(), "in_1MtGmCLkdIwHu7ix6PgS6g8S", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Invoices;
Invoice invoice = service.Pay("in_1MtGmCLkdIwHu7ix6PgS6g8S");
```

### Response

```json
{
  "id": "in_1MtGmCLkdIwHu7ix6PgS6g8S",
  "object": "invoice",
  "account_country": "US",
  "account_name": "Stripe Docs",
  "account_tax_ids": null,
  "amount_due": 0,
  "amount_paid": 0,
  "amount_overpaid": 0,
  "amount_remaining": 0,
  "amount_shipping": 0,
  "application": null,
  "attempt_count": 0,
  "attempted": true,
  "auto_advance": false,
  "automatic_tax": {
    "enabled": false,
    "liability": null,
    "status": null
  },
  "billing_reason": "manual",
  "collection_method": "send_invoice",
  "created": 1680641304,
  "currency": "usd",
  "custom_fields": null,
  "customer": "cus_NeZw0zvTyquTfF",
  "customer_address": null,
  "customer_email": "jennyrosen@example.com",
  "customer_name": "Jenny Rosen",
  "customer_phone": null,
  "customer_shipping": null,
  "customer_tax_exempt": "none",
  "customer_tax_ids": [],
  "default_payment_method": null,
  "default_source": null,
  "default_tax_rates": [],
  "description": null,
  "discounts": [],
  "due_date": 1681246104,
  "ending_balance": 0,
  "footer": null,
  "from_invoice": null,
  "hosted_invoice_url": "https://invoice.stripe.com/i/acct_1M2JTkLkdIwHu7ix/test_YWNjdF8xTTJKVGtMa2RJd0h1N2l4LF9OZVp3dVBYNnF0dGlvdXRubGVjSXVOOWhiVWpmUktPLDcxMTgyMTA10200x7P2wMSm?s=ap",
  "invoice_pdf": "https://pay.stripe.com/invoice/acct_1M2JTkLkdIwHu7ix/test_YWNjdF8xTTJKVGtMa2RJd0h1N2l4LF9OZVp3dVBYNnF0dGlvdXRubGVjSXVOOWhiVWpmUktPLDcxMTgyMTA10200x7P2wMSm/pdf?s=ap",
  "issuer": {
    "type": "self"
  },
  "last_finalization_error": null,
  "latest_revision": null,
  "lines": {
    "object": "list",
    "data": [],
    "has_more": false,
    "total_count": 0,
    "url": "/v1/invoices/in_1MtGmCLkdIwHu7ix6PgS6g8S/lines"
  },
  "livemode": false,
  "metadata": {},
  "next_payment_attempt": null,
  "number": "9545A614-0001",
  "on_behalf_of": null,
  "parent": null,
  "payment_settings": {
    "default_mandate": null,
    "payment_method_options": null,
    "payment_method_types": null
  },
  "period_end": 1680641304,
  "period_start": 1680641304,
  "post_payment_credit_notes_amount": 0,
  "pre_payment_credit_notes_amount": 0,
  "receipt_number": null,
  "shipping_cost": null,
  "shipping_details": null,
  "starting_balance": 0,
  "statement_descriptor": null,
  "status": "paid",
  "status_transitions": {
    "finalized_at": 1680641304,
    "marked_uncollectible_at": null,
    "paid_at": 1680641304,
    "voided_at": null
  },
  "subtotal": 0,
  "subtotal_excluding_tax": 0,
  "test_clock": null,
  "total": 0,
  "total_discount_amounts": [],
  "total_excluding_tax": 0,
  "total_taxes": [],
  "webhooks_delivered_at": 1680641304
}
```