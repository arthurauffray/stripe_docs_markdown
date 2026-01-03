# Delete a customer

Permanently deletes a customer. It cannot be undone. Also immediately cancels any active subscriptions on the customer.

## Returns

Returns an object with a deleted parameter on success. If the customer ID does not exist, this call raises [an error](https://docs.stripe.com/api/customers/delete.md#errors).

Unlike other objects, deleted customers can still be retrieved through the API in order to be able to track their history. Deleting customers removes all credit card details and prevents any further operations to be performed (such as adding a new subscription).

```curl
curl -X DELETE https://api.stripe.com/v1/customers/cus_NffrFeUfNV2Hib \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe customers delete cus_NffrFeUfNV2Hib
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

deleted = client.v1.customers.delete('cus_NffrFeUfNV2Hib')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

deleted = client.v1.customers.delete("cus_NffrFeUfNV2Hib")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$deleted = $stripe->customers->delete('cus_NffrFeUfNV2Hib', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

Customer customer = client.v1().customers().delete("cus_NffrFeUfNV2Hib");
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const deleted = await stripe.customers.del('cus_NffrFeUfNV2Hib');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CustomerDeleteParams{}
result, err := sc.V1Customers.Delete(context.TODO(), "cus_NffrFeUfNV2Hib", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Customers;
Customer deleted = service.Delete("cus_NffrFeUfNV2Hib");
```

### Response

```json
{
  "id": "cus_NffrFeUfNV2Hib",
  "object": "customer",
  "deleted": true
}
```