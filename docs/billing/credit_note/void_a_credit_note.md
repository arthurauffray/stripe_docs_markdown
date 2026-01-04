# Void a credit note

Marks a credit note as void. Learn more about [voiding credit notes](https://docs.stripe.com/docs/billing/invoices/credit-notes.md#voiding).

## Returns

Returns the voided credit note object if the call succeeded.

```curl
curl -X POST https://api.stripe.com/v1/credit_notes/cn_1MxvRqLkdIwHu7ixY0xbUcxk/void \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe credit_notes void_credit_note cn_1MxvRqLkdIwHu7ixY0xbUcxk
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

credit_note = client.v1.credit_notes.void_credit_note('cn_1MxvRqLkdIwHu7ixY0xbUcxk')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

credit_note = client.v1.credit_notes.void_credit_note("cn_1MxvRqLkdIwHu7ixY0xbUcxk")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$creditNote = $stripe->creditNotes->voidCreditNote(
  'cn_1MxvRqLkdIwHu7ixY0xbUcxk',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CreditNoteVoidCreditNoteParams params =
  CreditNoteVoidCreditNoteParams.builder().build();

CreditNote creditNote =
  client.v1().creditNotes().voidCreditNote("cn_1MxvRqLkdIwHu7ixY0xbUcxk", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const creditNote = await stripe.creditNotes.voidCreditNote(
  'cn_1MxvRqLkdIwHu7ixY0xbUcxk'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CreditNoteVoidCreditNoteParams{}
result, err := sc.V1CreditNotes.VoidCreditNote(
  context.TODO(), "cn_1MxvRqLkdIwHu7ixY0xbUcxk", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.CreditNotes;
CreditNote creditNote = service.VoidCreditNote("cn_1MxvRqLkdIwHu7ixY0xbUcxk");
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
  "status": "void",
  "subtotal": 1099,
  "subtotal_excluding_tax": 1099,
  "total": 1099,
  "total_excluding_tax": 1099,
  "total_taxes": [],
  "type": "pre_payment",
  "voided_at": 1681750959
}
```