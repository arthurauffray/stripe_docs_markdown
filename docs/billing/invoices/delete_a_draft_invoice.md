# Delete a draft invoice

Permanently deletes a one-off invoice draft. This cannot be undone. Attempts to delete invoices that are no longer in a draft state will fail; once an invoice has been finalized or if an invoice is for a subscription, it must be [voided](https://docs.stripe.com/api/invoices/delete.md#void_invoice).

## Returns

A successfully deleted invoice. Otherwise, this call raises [an error](https://docs.stripe.com/api/invoices/delete.md#errors), such as if the invoice has already been deleted.

```curl
curl -X DELETE https://api.stripe.com/v1/invoices/in_1MtHbELkdIwHu7ixl4OzzPMv \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe invoices delete in_1MtHbELkdIwHu7ixl4OzzPMv
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

deleted = client.v1.invoices.delete('in_1MtHbELkdIwHu7ixl4OzzPMv')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

deleted = client.v1.invoices.delete("in_1MtHbELkdIwHu7ixl4OzzPMv")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$deleted = $stripe->invoices->delete('in_1MtHbELkdIwHu7ixl4OzzPMv', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

Invoice invoice = client.v1().invoices().delete("in_1MtHbELkdIwHu7ixl4OzzPMv");
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const deleted = await stripe.invoices.del('in_1MtHbELkdIwHu7ixl4OzzPMv');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.InvoiceDeleteParams{}
result, err := sc.V1Invoices.Delete(
  context.TODO(), "in_1MtHbELkdIwHu7ixl4OzzPMv", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Invoices;
Invoice deleted = service.Delete("in_1MtHbELkdIwHu7ixl4OzzPMv");
```

### Response

```json
{
  "id": "in_1MtHbELkdIwHu7ixl4OzzPMv",
  "object": "invoice",
  "deleted": true
}
```