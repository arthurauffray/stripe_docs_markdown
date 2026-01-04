# List all invoices

You can list all invoices, or list the invoices for a specific customer. The invoices are returned sorted by creation date, with the most recently created invoices appearing first.

## Returns

A dictionary with a `data` property that contains an array invoice attachments,

## Parameters

- `collection_method` (enum, optional)
  The collection method of the invoice to retrieve. Either `charge_automatically` or `send_invoice`.
Possible enum values:
  - `charge_automatically`
  - `send_invoice`

- `created` (object, optional)
  Only return invoices that were created during the given date interval.

  - `created.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `created.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `created.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `created.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `customer` (string, optional)
  Only return invoices for the customer specified by this customer ID.

- `customer_account` (string, optional)
  Only return invoices for the account representing the customer specified by this account ID.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `status` (enum, optional)
  The status of the invoice, one of `draft`, `open`, `paid`, `uncollectible`, or `void`. [Learn more](https://docs.stripe.com/docs/billing/invoices/workflow.md#workflow-overview)

- `subscription` (string, optional)
  Only return invoices for the subscription specified by this subscription ID.

```curl
curl -G https://api.stripe.com/v1/invoices \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe invoices list  \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

invoices = client.v1.invoices.list({limit: 3})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

invoices = client.v1.invoices.list({"limit": 3})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$invoices = $stripe->invoices->all(['limit' => 3]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

InvoiceListParams params = InvoiceListParams.builder().setLimit(3L).build();

StripeCollection<Invoice> stripeCollection = client.v1().invoices().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const invoices = await stripe.invoices.list({
  limit: 3,
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.InvoiceListParams{}
params.Limit = stripe.Int64(3)
result := sc.V1Invoices.List(context.TODO(), params)
```

```dotnet
var options = new InvoiceListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Invoices;
StripeList<Invoice> invoices = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/invoices",
  "has_more": false,
  "data": [
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
  ]
}
```