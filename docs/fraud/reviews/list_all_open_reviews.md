# List all open reviews

Returns a list of `Review` objects that have `open` set to `true`. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` reviews, starting after review `starting_after`. Each entry in the array is a separate `Review` object. If no more reviews are available, the resulting array will be empty.

## Parameters

- `created` (object, optional)
  Only return reviews that were created during the given date interval.

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
curl -G https://api.stripe.com/v1/reviews \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe reviews list  \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

reviews = client.v1.reviews.list({limit: 3})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

reviews = client.v1.reviews.list({"limit": 3})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$reviews = $stripe->reviews->all(['limit' => 3]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ReviewListParams params = ReviewListParams.builder().setLimit(3L).build();

StripeCollection<Review> stripeCollection = client.v1().reviews().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const reviews = await stripe.reviews.list({
  limit: 3,
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.ReviewListParams{}
params.Limit = stripe.Int64(3)
result := sc.V1Reviews.List(context.TODO(), params)
```

```dotnet
var options = new ReviewListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Reviews;
StripeList<Review> reviews = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/reviews",
  "has_more": false,
  "data": [
    {
      "id": "prv_1NVyFt2eZvKYlo2CjubqF1xm",
      "object": "review",
      "billing_zip": null,
      "charge": null,
      "closed_reason": null,
      "created": 1689864901,
      "ip_address": null,
      "ip_address_location": null,
      "livemode": false,
      "open": true,
      "opened_reason": "rule",
      "payment_intent": "pi_3NVy8c2eZvKYlo2C055h7pkd",
      "reason": "rule",
      "session": null
    }
  ]
}
```