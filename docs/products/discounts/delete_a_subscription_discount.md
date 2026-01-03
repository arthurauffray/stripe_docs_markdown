# Delete a subscription discount

Removes the currently applied discount on a subscription.

## Returns

An object with a deleted flag set to true upon success. This call returns [an error](https://docs.stripe.com/api/discounts/subscription_delete.md#errors) otherwise, such as if no discount exists on this subscription.

```curl
curl -X DELETE https://api.stripe.com/v1/subscriptions/sub_1NlcNX2eZvKYlo2CFqnrn9ow/discount \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe subscriptions delete_discount sub_1NlcNX2eZvKYlo2CFqnrn9ow
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

discount = client.v1.subscriptions.delete_discount('sub_1NlcNX2eZvKYlo2CFqnrn9ow')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

deleted = client.v1.subscriptions.delete_discount("sub_1NlcNX2eZvKYlo2CFqnrn9ow")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$deleted = $stripe->subscriptions->deleteDiscount(
  'sub_1NlcNX2eZvKYlo2CFqnrn9ow',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

Discount discount =
  client.v1().subscriptions().deleteDiscount("sub_1NlcNX2eZvKYlo2CFqnrn9ow");
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const deleted = await stripe.subscriptions.deleteDiscount(
  'sub_1NlcNX2eZvKYlo2CFqnrn9ow'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.SubscriptionDeleteDiscountParams{}
result, err := sc.V1Subscriptions.DeleteDiscount(
  context.TODO(), "sub_1NlcNX2eZvKYlo2CFqnrn9ow", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Subscriptions;
Discount discount = service.DeleteDiscount("sub_1NlcNX2eZvKYlo2CFqnrn9ow");
```

### Response

```json
{
  "object": "discount",
  "deleted": true
}
```