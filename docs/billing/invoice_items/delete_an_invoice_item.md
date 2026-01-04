# Delete an invoice item

Deletes an invoice item, removing it from an invoice. Deleting invoice items is only possible when they’re not attached to invoices, or if it’s attached to a draft invoice.

## Returns

An object with the deleted invoice item’s ID and a deleted flag upon success. Otherwise, this call raises [an error](https://docs.stripe.com/api/invoiceitems/delete.md#errors), such as if the invoice item has already been deleted.

```curl
curl -X DELETE https://api.stripe.com/v1/invoiceitems/ii_1MtGUtLkdIwHu7ixBYwjAM00 \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe invoiceitems delete ii_1MtGUtLkdIwHu7ixBYwjAM00
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

deleted = client.v1.invoice_items.delete('ii_1MtGUtLkdIwHu7ixBYwjAM00')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

deleted = client.v1.invoice_items.delete("ii_1MtGUtLkdIwHu7ixBYwjAM00")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$deleted = $stripe->invoiceItems->delete('ii_1MtGUtLkdIwHu7ixBYwjAM00', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

InvoiceItem invoiceItem =
  client.v1().invoiceItems().delete("ii_1MtGUtLkdIwHu7ixBYwjAM00");
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const deleted = await stripe.invoiceItems.del('ii_1MtGUtLkdIwHu7ixBYwjAM00');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.InvoiceItemDeleteParams{}
result, err := sc.V1InvoiceItems.Delete(
  context.TODO(), "ii_1MtGUtLkdIwHu7ixBYwjAM00", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.InvoiceItems;
InvoiceItem deleted = service.Delete("ii_1MtGUtLkdIwHu7ixBYwjAM00");
```

### Response

```json
{
  "id": "ii_1MtGUtLkdIwHu7ixBYwjAM00",
  "object": "invoiceitem",
  "deleted": true
}
```