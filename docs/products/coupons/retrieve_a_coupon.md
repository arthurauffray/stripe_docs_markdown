# Retrieve a coupon

Retrieves the coupon with the given ID.

## Returns

Returns a coupon if a valid coupon ID was provided. Raises [an error](https://docs.stripe.com/api/coupons/retrieve.md#errors) otherwise.

```curl
curl https://api.stripe.com/v1/coupons/jMT0WJUD \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe coupons retrieve jMT0WJUD
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

coupon = client.v1.coupons.retrieve('jMT0WJUD')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

coupon = client.v1.coupons.retrieve("jMT0WJUD")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$coupon = $stripe->coupons->retrieve('jMT0WJUD', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CouponRetrieveParams params = CouponRetrieveParams.builder().build();

Coupon coupon = client.v1().coupons().retrieve("jMT0WJUD", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const coupon = await stripe.coupons.retrieve('jMT0WJUD');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CouponRetrieveParams{}
result, err := sc.V1Coupons.Retrieve(context.TODO(), "jMT0WJUD", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Coupons;
Coupon coupon = service.Get("jMT0WJUD");
```

### Response

```json
{
  "id": "jMT0WJUD",
  "object": "coupon",
  "amount_off": null,
  "created": 1678037688,
  "currency": null,
  "duration": "repeating",
  "duration_in_months": 3,
  "livemode": false,
  "max_redemptions": null,
  "metadata": {},
  "name": null,
  "percent_off": 25.5,
  "redeem_by": null,
  "times_redeemed": 0,
  "valid": true
}
```