# List all physical bundles

Returns a list of physical bundle objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` cards, starting after card `starting_after`. Each entry in the array is a separate physical bundle object. If no more cards are available, the resulting array will be empty.

## Parameters

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `status` (enum, optional)
  Only return physical bundles with the given status.
Possible enum values:
  - `active`
    Can be used to create cards that fulfill immediately.

  - `inactive`
    Cannot be used to create cards.

  - `review`
    Can be used to create cards but cards will only be fulfilled when this physical bundle is activated.

- `type` (enum, optional)
  Only return physical bundles with the given type.
Possible enum values:
  - `custom`
    Available only to you, you manage design and inventory.

  - `standard`
    Publicly available, Stripe manages design and inventory.

```curl
curl -G https://api.stripe.com/v1/issuing/physical_bundles \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe issuing physical_bundles list  \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

physical_bundles = client.v1.issuing.physical_bundles.list({limit: 3})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

physical_bundles = client.v1.issuing.physical_bundles.list({"limit": 3})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$physicalBundles = $stripe->issuing->physicalBundles->all(['limit' => 3]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PhysicalBundleListParams params =
  PhysicalBundleListParams.builder().setLimit(3L).build();

StripeCollection<PhysicalBundle> stripeCollection =
  client.v1().issuing().physicalBundles().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const physicalBundles = await stripe.issuing.physicalBundles.list({
  limit: 3,
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.IssuingPhysicalBundleListParams{}
params.Limit = stripe.Int64(3)
result := sc.V1IssuingPhysicalBundles.List(context.TODO(), params)
```

```dotnet
var options = new Stripe.Issuing.PhysicalBundleListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Issuing.PhysicalBundles;
StripeList<Stripe.Issuing.PhysicalBundle> physicalBundles = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/issuing/physical_bundles",
  "has_more": false,
  "data": [
    {
      "id": "ics_NLuXJPDYSTjFON",
      "object": "issuing.physical_bundle",
      "livemode": false,
      "name": "US Visa Credit White",
      "features": {
        "card_logo": "required",
        "carrier_text": "optional"
      },
      "status": "active",
      "type": "standard"
    }
  ]
}
```