# Retrieve a credit note's line items

When retrieving a credit note, you’ll get a **lines** property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.

## Returns

Returns a list of [line_item objects](https://docs.stripe.com/api/credit_notes/lines.md#credit_note_line_item_object).

## Parameters

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/credit_notes/cn_1NPtPy2eZvKYlo2CPaEMGMY8/lines \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe credit_note_line_items list cn_1NPtPy2eZvKYlo2CPaEMGMY8 \
  --limit=3
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

credit_note_line_items = client.v1.credit_notes.line_items.list(
  "cn_1NPtPy2eZvKYlo2CPaEMGMY8",
  {"limit": 3},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$creditNoteLineItems = $stripe->creditNotes->allLines(
  'cn_1NPtPy2eZvKYlo2CPaEMGMY8',
  ['limit' => 3]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CreditNoteLineItemListParams params =
  CreditNoteLineItemListParams.builder().setLimit(3L).build();

StripeCollection<CreditNoteLineItem> stripeCollection =
  client.v1().creditNotes().lineItems().list("cn_1NPtPy2eZvKYlo2CPaEMGMY8", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const creditNoteLineItems = await stripe.creditNotes.listLineItems(
  'cn_1NPtPy2eZvKYlo2CPaEMGMY8',
  {
    limit: 3,
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CreditNoteListLinesParams{
  CreditNote: stripe.String("cn_1NPtPy2eZvKYlo2CPaEMGMY8"),
}
params.Limit = stripe.Int64(3)
result := sc.V1CreditNotes.ListLines(context.TODO(), params)
```

```dotnet
var options = new CreditNoteLineItemListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.CreditNotes.LineItems;
StripeList<CreditNoteLineItem> creditNoteLineItems = service.List(
    "cn_1NPtPy2eZvKYlo2CPaEMGMY8",
    options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/credit_notes/cn_1NPtPy2eZvKYlo2CPaEMGMY8/lines",
  "has_more": false,
  "data": [
    {
      "object": "list",
      "url": "/v1/credit_notes/cn_1Nn7fB2eZvKYlo2CuJ0wZBlA/lines",
      "has_more": false,
      "data": [
        {
          "id": "cnli_1Nn7fB2eZvKYlo2COYgPG88j",
          "object": "credit_note_line_item",
          "amount": 799,
          "description": "My First Invoice Item (created for API docs)",
          "discount_amount": 0,
          "discount_amounts": [],
          "invoice_line_item": "il_1Nn7fB2eZvKYlo2C3GKZP9wi",
          "livemode": false,
          "quantity": 1,
          "tax_rates": [],
          "taxes": [],
          "type": "invoice_line_item",
          "unit_amount": null,
          "unit_amount_decimal": null
        }
      ]
    }
  ]
}
```