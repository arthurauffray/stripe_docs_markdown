# Delete a customer discount

Removes the currently applied discount on a customer.

## Returns

An object with a deleted flag set to true upon success. This call returns [an error](https://docs.stripe.com/api/discounts/delete.md#errors) otherwise, such as if no discount exists on this customer.

```curl
curl -X DELETE https://api.stripe.com/v1/customers/cus_9s6XKzkNRiz8i3/discount \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe customers delete_discount cus_9s6XKzkNRiz8i3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

discount = client.v1.customers.delete_discount('cus_9s6XKzkNRiz8i3')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

deleted = client.v1.customers.delete_discount("cus_9s6XKzkNRiz8i3")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$deleted = $stripe->customers->deleteDiscount('cus_9s6XKzkNRiz8i3', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

Discount discount = client.v1().customers().deleteDiscount("cus_9s6XKzkNRiz8i3");
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const deleted = await stripe.customers.deleteDiscount('cus_9s6XKzkNRiz8i3');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CustomerDeleteDiscountParams{}
result, err := sc.V1Customers.DeleteDiscount(
  context.TODO(), "cus_9s6XKzkNRiz8i3", params)
```

```dotnet
StripeConfiguration.ApiKey = "<<YOUR_SECRET_KEY>>";

var service = new DiscountService();
service.DeleteCustomerDiscount("cus_9s6XKzkNRiz8i3");
```

### Response

```json
{
  "object": "discount",
  "deleted": true
}
```