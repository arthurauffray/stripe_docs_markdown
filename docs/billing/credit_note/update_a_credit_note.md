# Update a credit note

Updates an existing credit note.

## Returns

Returns the updated credit note object if the call succeeded.

## Parameters

- `memo` (string, optional)
  Credit note memo.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/credit_notes/cn_1MxvRqLkdIwHu7ixY0xbUcxk \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
```

```cli
stripe credit_notes update cn_1MxvRqLkdIwHu7ixY0xbUcxk \
  -d "metadata[order_id]"=6735
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

credit_note = client.v1.credit_notes.update(
  'cn_1MxvRqLkdIwHu7ixY0xbUcxk',
  {metadata: {order_id: '6735'}},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

credit_note = client.v1.credit_notes.update(
  "cn_1MxvRqLkdIwHu7ixY0xbUcxk",
  {"metadata": {"order_id": "6735"}},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$creditNote = $stripe->creditNotes->update(
  'cn_1MxvRqLkdIwHu7ixY0xbUcxk',
  ['metadata' => ['order_id' => '6735']]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CreditNoteUpdateParams params =
  CreditNoteUpdateParams.builder().putMetadata("order_id", "6735").build();

CreditNote creditNote =
  client.v1().creditNotes().update("cn_1MxvRqLkdIwHu7ixY0xbUcxk", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const creditNote = await stripe.creditNotes.update(
  'cn_1MxvRqLkdIwHu7ixY0xbUcxk',
  {
    metadata: {
      order_id: '6735',
    },
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CreditNoteUpdateParams{}
params.AddMetadata("order_id", "6735")
result, err := sc.V1CreditNotes.Update(
  context.TODO(), "cn_1MxvRqLkdIwHu7ixY0xbUcxk", params)
```

```dotnet
var options = new CreditNoteUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.CreditNotes;
CreditNote creditNote = service.Update("cn_1MxvRqLkdIwHu7ixY0xbUcxk", options);
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
  "metadata": {
    "order_id": "6735"
  },
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