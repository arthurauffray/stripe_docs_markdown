# Retrieve an invoice

Retrieves the invoice with the given ID.

## Returns

Returns an invoice object if a valid invoice ID was provided. Raises [an error](https://docs.stripe.com/api/invoices/retrieve.md#errors) otherwise.

The invoice object contains a `lines` hash that contains information about the subscriptions and invoice items that have been applied to the invoice, as well as any prorations that Stripe has automatically calculated. Each line on the invoice has an `amount` attribute that represents the amount actually contributed to the invoice’s total. For invoice items and prorations, the amount attribute is the same as for the invoice item or proration respectively. For subscriptions, the amount may be different from the plan’s regular price depending on whether the invoice covers a trial period or the invoice period differs from the plan’s usual interval.

The invoice object has both a `subtotal` and a `total`. The subtotal represents the total before any discounts, while the total is the final amount to be charged to the customer after all coupons have been applied.

The invoice also has a `next_payment_attempt` attribute that tells you the next time (as a Unix timestamp) payment for the invoice will be automatically attempted. For invoices with manual payment collection, that have been closed, or that have reached the maximum number of retries (specified in your [subscriptions settings](https://dashboard.stripe.com/account/billing/automatic)), the `next_payment_attempt` will be null.

```curl
curl https://api.stripe.com/v1/invoices/in_1MtHbELkdIwHu7ixl4OzzPMv \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe invoices retrieve in_1MtHbELkdIwHu7ixl4OzzPMv
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

invoice = client.v1.invoices.retrieve('in_1MtHbELkdIwHu7ixl4OzzPMv')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

invoice = client.v1.invoices.retrieve("in_1MtHbELkdIwHu7ixl4OzzPMv")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$invoice = $stripe->invoices->retrieve('in_1MtHbELkdIwHu7ixl4OzzPMv', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

InvoiceRetrieveParams params = InvoiceRetrieveParams.builder().build();

Invoice invoice =
  client.v1().invoices().retrieve("in_1MtHbELkdIwHu7ixl4OzzPMv", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const invoice = await stripe.invoices.retrieve('in_1MtHbELkdIwHu7ixl4OzzPMv');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.InvoiceRetrieveParams{}
result, err := sc.V1Invoices.Retrieve(
  context.TODO(), "in_1MtHbELkdIwHu7ixl4OzzPMv", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Invoices;
Invoice invoice = service.Get("in_1MtHbELkdIwHu7ixl4OzzPMv");
```

### Response

```json
{
  "id": "in_1MtHbELkdIwHu7ixl4OzzPMv",
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
  "attempted": false,
  "auto_advance": false,
  "automatic_tax": {
    "enabled": false,
    "liability": null,
    "status": null
  },
  "billing_reason": "manual",
  "collection_method": "charge_automatically",
  "created": 1680644467,
  "currency": "usd",
  "custom_fields": null,
  "customer": "cus_NeZwdNtLEOXuvB",
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
    "data": [],
    "has_more": false,
    "total_count": 0,
    "url": "/v1/invoices/in_1MtHbELkdIwHu7ixl4OzzPMv/lines"
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
  "period_end": 1680644467,
  "period_start": 1680644467,
  "post_payment_credit_notes_amount": 0,
  "pre_payment_credit_notes_amount": 0,
  "receipt_number": null,
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
  "subtotal": 0,
  "subtotal_excluding_tax": 0,
  "test_clock": null,
  "total": 0,
  "total_discount_amounts": [],
  "total_excluding_tax": 0,
  "total_taxes": [],
  "webhooks_delivered_at": 1680644467
}
```