# Delete a coupon

You can delete coupons via the [coupon management](https://dashboard.stripe.com/coupons) page of the Stripe dashboard. However, deleting a coupon does not affect any customers who have already applied the coupon; it means that new customers can’t redeem the coupon. You can also delete coupons via the API.

## Returns

An object with the deleted coupon’s ID and a deleted flag upon success. Otherwise, this call raises [an error](https://docs.stripe.com/api/coupons/delete.md#errors), such as if the coupon has already been deleted.

```curl
curl -X DELETE https://api.stripe.com/v1/coupons/jMT0WJUD \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe coupons delete jMT0WJUD
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

deleted = client.v1.coupons.delete('jMT0WJUD')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

deleted = client.v1.coupons.delete("jMT0WJUD")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$deleted = $stripe->coupons->delete('jMT0WJUD', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

Coupon coupon = client.v1().coupons().delete("jMT0WJUD");
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const deleted = await stripe.coupons.del('jMT0WJUD');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CouponDeleteParams{}
result, err := sc.V1Coupons.Delete(context.TODO(), "jMT0WJUD", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Coupons;
Coupon deleted = service.Delete("jMT0WJUD");
```

### Response

```json
{
  "id": "jMT0WJUD",
  "object": "coupon",
  "deleted": true
}
```