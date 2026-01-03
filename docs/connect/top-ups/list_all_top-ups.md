# List all top-ups

Returns a list of top-ups.

## Returns

A dictionary containing the `data` property, which is an array of separate top-up objects. The number of top-ups in the array is limited to the number designated in `limit`. If no more top-ups are available, the resulting array will be empty.

## Parameters

- `amount` (object, optional)
  A positive integer representing how much to transfer.

  - `amount.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `amount.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `amount.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `amount.lte` (integer, optional)
    Maximum value to filter by (inclusive)

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

- `status` (string, optional)
  Only return top-ups that have the given status. One of `canceled`, `failed`, `pending` or `succeeded`.

```curl
curl -G https://api.stripe.com/v1/topups \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe topups list  \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

topups = client.v1.topups.list({limit: 3})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

topups = client.v1.topups.list({"limit": 3})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$topups = $stripe->topups->all(['limit' => 3]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TopupListParams params = TopupListParams.builder().setLimit(3L).build();

StripeCollection<Topup> stripeCollection = client.v1().topups().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const topups = await stripe.topups.list({
  limit: 3,
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TopupListParams{}
params.Limit = stripe.Int64(3)
result := sc.V1Topups.List(context.TODO(), params)
```

```dotnet
var options = new TopupListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Topups;
StripeList<Topup> topups = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/topups",
  "has_more": false,
  "data": [
    {
      "id": "tu_1NG6yj2eZvKYlo2C1FOBiHya",
      "object": "topup",
      "amount": 2000,
      "balance_transaction": null,
      "created": 123456789,
      "currency": "usd",
      "description": "Top-up for Jenny Rosen",
      "expected_availability_date": 123456789,
      "failure_code": null,
      "failure_message": null,
      "livemode": false,
      "source": null,
      "statement_descriptor": "Top-up",
      "status": "pending",
      "transfer_group": null
    }
  ]
}
```