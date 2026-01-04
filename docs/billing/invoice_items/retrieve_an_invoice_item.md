# Retrieve an invoice item

Retrieves the invoice item with the given ID.

## Returns

Returns an invoice item if a valid invoice item ID was provided. Raises [an error](https://docs.stripe.com/api/invoiceitems/retrieve.md#errors) otherwise.

```curl
curl https://api.stripe.com/v1/invoiceitems/ii_1MtGUtLkdIwHu7ixBYwjAM00 \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe invoiceitems retrieve ii_1MtGUtLkdIwHu7ixBYwjAM00
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

invoice_item = client.v1.invoice_items.retrieve('ii_1MtGUtLkdIwHu7ixBYwjAM00')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

invoice_item = client.v1.invoice_items.retrieve("ii_1MtGUtLkdIwHu7ixBYwjAM00")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$invoiceItem = $stripe->invoiceItems->retrieve('ii_1MtGUtLkdIwHu7ixBYwjAM00', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

InvoiceItemRetrieveParams params = InvoiceItemRetrieveParams.builder().build();

InvoiceItem invoiceItem =
  client.v1().invoiceItems().retrieve("ii_1MtGUtLkdIwHu7ixBYwjAM00", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const invoiceItem = await stripe.invoiceItems.retrieve(
  'ii_1MtGUtLkdIwHu7ixBYwjAM00'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.InvoiceItemRetrieveParams{}
result, err := sc.V1InvoiceItems.Retrieve(
  context.TODO(), "ii_1MtGUtLkdIwHu7ixBYwjAM00", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.InvoiceItems;
InvoiceItem invoiceItem = service.Get("ii_1MtGUtLkdIwHu7ixBYwjAM00");
```

### Response

```json
{
  "id": "ii_1MtGUtLkdIwHu7ixBYwjAM00",
  "object": "invoiceitem",
  "amount": 1099,
  "currency": "usd",
  "customer": "cus_NeZei8imSbMVvi",
  "date": 1680640231,
  "description": "T-shirt",
  "discountable": true,
  "discounts": [],
  "invoice": null,
  "livemode": false,
  "metadata": {},
  "parent": null,
  "period": {
    "end": 1680640231,
    "start": 1680640231
  },
  "pricing": {
    "price_details": {
      "price": "price_1MtGUsLkdIwHu7ix1be5Ljaj",
      "product": "prod_NeZe7xbBdJT8EN"
    },
    "type": "price_details",
    "unit_amount_decimal": "1099"
  },
  "proration": false,
  "quantity": 1,
  "tax_rates": [],
  "test_clock": null
}
```