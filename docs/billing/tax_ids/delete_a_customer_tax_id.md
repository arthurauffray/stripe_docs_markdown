# Delete a Customer tax ID

Deletes an existing `tax_id` object.

## Returns

Returns an object with a deleted parameter on success. If the `tax_id` object does not exist, this call raises [an error](https://docs.stripe.com/api/tax_ids/customer_delete.md#errors).

```curl
curl -X DELETE https://api.stripe.com/v1/customers/cus_NZKoSNZZ58qtO0/tax_ids/txi_1MoC8zLkdIwHu7ixEhgWcHzJ \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe tax_ids delete cus_NZKoSNZZ58qtO0 txi_1MoC8zLkdIwHu7ixEhgWcHzJ
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

deleted = client.v1.customers.tax_ids.delete(
  'cus_NZKoSNZZ58qtO0',
  'txi_1MoC8zLkdIwHu7ixEhgWcHzJ',
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

deleted = client.v1.customers.tax_ids.delete(
  "cus_NZKoSNZZ58qtO0",
  "txi_1MoC8zLkdIwHu7ixEhgWcHzJ",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$deleted = $stripe->customers->deleteTaxId(
  'cus_NZKoSNZZ58qtO0',
  'txi_1MoC8zLkdIwHu7ixEhgWcHzJ',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TaxId taxId =
  client.v1().customers().taxIds().delete(
    "cus_NZKoSNZZ58qtO0",
    "txi_1MoC8zLkdIwHu7ixEhgWcHzJ"
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const deleted = await stripe.customers.deleteTaxId(
  'cus_NZKoSNZZ58qtO0',
  'txi_1MoC8zLkdIwHu7ixEhgWcHzJ'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TaxIDDeleteParams{Customer: stripe.String("cus_NZKoSNZZ58qtO0")}
result, err := sc.V1TaxIDs.Delete(
  context.TODO(), "txi_1MoC8zLkdIwHu7ixEhgWcHzJ", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Customers.TaxIds;
TaxId deleted = service.Delete("cus_NZKoSNZZ58qtO0", "txi_1MoC8zLkdIwHu7ixEhgWcHzJ");
```

### Response

```json
{
  "id": "txi_1MoC8zLkdIwHu7ixEhgWcHzJ",
  "object": "tax_id",
  "deleted": true
}
```