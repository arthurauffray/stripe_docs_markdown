# List all coupons

Returns a list of your coupons.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` coupons, starting after coupon `starting_after`. Each entry in the array is a separate coupon object. If no more coupons are available, the resulting array will be empty.

## Parameters

- `created` (object, optional)
  A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.

  - `created.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `created.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `created.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `created.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/coupons \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe coupons list  \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

coupons = client.v1.coupons.list({limit: 3})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

coupons = client.v1.coupons.list({"limit": 3})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$coupons = $stripe->coupons->all(['limit' => 3]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CouponListParams params = CouponListParams.builder().setLimit(3L).build();

StripeCollection<Coupon> stripeCollection = client.v1().coupons().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const coupons = await stripe.coupons.list({
  limit: 3,
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CouponListParams{}
params.Limit = stripe.Int64(3)
result := sc.V1Coupons.List(context.TODO(), params)
```

```dotnet
var options = new CouponListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Coupons;
StripeList<Coupon> coupons = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/coupons",
  "has_more": false,
  "data": [
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
  ]
}
```