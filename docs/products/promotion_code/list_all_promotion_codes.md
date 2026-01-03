# List all promotion codes

Returns a list of your promotion codes.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` promotion codes, starting after promotion code `starting_after`. Each entry in the array is a separate promotion code object. If no more promotion codes are available, the resulting array will be empty.

## Parameters

- `active` (boolean, optional)
  Filter promotion codes by whether they are active.

- `code` (string, optional)
  Only return promotion codes that have this case-insensitive code.

- `coupon` (string, optional)
  Only return promotion codes for this coupon.

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

- `customer` (string, optional)
  Only return promotion codes that are restricted to this customer.

- `customer_account` (string, optional)
  Only return promotion codes that are restricted to this account representing the customer.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/promotion_codes \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe promotion_codes list  \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

promotion_codes = client.v1.promotion_codes.list({limit: 3})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

promotion_codes = client.v1.promotion_codes.list({"limit": 3})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$promotionCodes = $stripe->promotionCodes->all(['limit' => 3]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PromotionCodeListParams params =
  PromotionCodeListParams.builder().setLimit(3L).build();

StripeCollection<PromotionCode> stripeCollection =
  client.v1().promotionCodes().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const promotionCodes = await stripe.promotionCodes.list({
  limit: 3,
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PromotionCodeListParams{}
params.Limit = stripe.Int64(3)
result := sc.V1PromotionCodes.List(context.TODO(), params)
```

```dotnet
var options = new PromotionCodeListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.PromotionCodes;
StripeList<PromotionCode> promotionCodes = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/promotion_codes",
  "has_more": false,
  "data": [
    {
      "id": "promo_1MiM6KLkdIwHu7ixrIaX4wgn",
      "object": "promotion_code",
      "active": true,
      "code": "A1H1Q1MG",
      "promotion": {
        "type": "coupon",
        "coupon": "nVJYDOag"
      },
      "created": 1678040164,
      "customer": null,
      "expires_at": null,
      "livemode": false,
      "max_redemptions": null,
      "metadata": {},
      "restrictions": {
        "first_time_transaction": false,
        "minimum_amount": null,
        "minimum_amount_currency": null
      },
      "times_redeemed": 0
    }
  ]
}
```