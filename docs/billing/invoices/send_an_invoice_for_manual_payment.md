# Send an invoice for manual payment

Stripe will automatically send invoices to customers according to your [subscriptions settings](https://dashboard.stripe.com/account/billing/automatic). However, if you’d like to manually send an invoice to your customer out of the normal schedule, you can do so. When sending invoices that have already been paid, there will be no reference to the payment in the email.

Requests made in test-mode result in no emails being sent, despite sending an `invoice.sent` event.

## Returns

Returns the invoice object.

```curl
curl -X POST https://api.stripe.com/v1/invoices/in_1MtGmCLkdIwHu7ixJlveR2DO/send \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe invoices send_invoice in_1MtGmCLkdIwHu7ixJlveR2DO
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

invoice = client.v1.invoices.send_invoice('in_1MtGmCLkdIwHu7ixJlveR2DO')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

invoice = client.v1.invoices.send_invoice("in_1MtGmCLkdIwHu7ixJlveR2DO")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$invoice = $stripe->invoices->sendInvoice('in_1MtGmCLkdIwHu7ixJlveR2DO', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

InvoiceSendInvoiceParams params = InvoiceSendInvoiceParams.builder().build();

Invoice invoice =
  client.v1().invoices().sendInvoice("in_1MtGmCLkdIwHu7ixJlveR2DO", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const invoice = await stripe.invoices.sendInvoice('in_1MtGmCLkdIwHu7ixJlveR2DO');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.InvoiceSendInvoiceParams{}
result, err := sc.V1Invoices.SendInvoice(
  context.TODO(), "in_1MtGmCLkdIwHu7ixJlveR2DO", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Invoices;
Invoice invoice = service.SendInvoice("in_1MtGmCLkdIwHu7ixJlveR2DO");
```

### Response

```json
{
  "id": "in_1MtGmCLkdIwHu7ixJlveR2DO",
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
  "customer": "cus_NeZwvqcz9Sh2uw",
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
  "hosted_invoice_url": "https://invoice.stripe.com/i/acct_1M2JTkLkdIwHu7ix/test_YWNjdF8xTTJKVGtMa2RJd0h1N2l4LF9OZVp3SDR0Q1Q4U1N0YkVjY2lvSmRoRGppU3E1eGVJLDcxMTgyMTA10200hQIJrDM1?s=ap",
  "invoice_pdf": "https://pay.stripe.com/invoice/acct_1M2JTkLkdIwHu7ix/test_YWNjdF8xTTJKVGtMa2RJd0h1N2l4LF9OZVp3SDR0Q1Q4U1N0YkVjY2lvSmRoRGppU3E1eGVJLDcxMTgyMTA10200hQIJrDM1/pdf?s=ap",
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
    "url": "/v1/invoices/in_1MtGmCLkdIwHu7ixJlveR2DO/lines"
  },
  "livemode": false,
  "metadata": {},
  "next_payment_attempt": null,
  "number": "3AB9C0CA-0001",
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