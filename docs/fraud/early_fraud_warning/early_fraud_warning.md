# List ReserveReleases

Returns a list of ReserveReleases previously created. The ReserveReleases are returned in sorted order, with the most recent ReserveReleases appearing first.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` ReserveReleases, starting after ReserveRelease `starting_after` and ending before ReserveRelease `ending_before`.       Each entry in the array is a separate ReserveRelease object. If no more ReserveReleases are available, the resulting array will be empty.

## Parameters

- `currency` (enum, optional)
  Only return ReserveReleases associated with the currency specified by this currency code. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `reserve_hold` (string, optional)
  Only return ReserveReleases associated with the ReserveHold specified by this ReserveHold ID.

- `reserve_plan` (string, optional)
  Only return ReserveReleases associated with the ReservePlan specified by this ReservePlan ID.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/reserve/releases \
  -u "<<YOUR_SECRET_KEY>>" \
  -d reserve_plan=resplan_61SToUQzaDa1N5nJh412e824LPfdz \
  -d limit=10
```

```cli
stripe reserve releases list  \
  --reserve-plan=resplan_61SToUQzaDa1N5nJh412e824LPfdz \
  --limit=10
```

```ruby
# This example uses the beta SDK. See https://github.com/stripe/stripe-ruby#public-preview-sdks
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

releases = client.v1.reserve.releases.list({
  reserve_plan: 'resplan_61SToUQzaDa1N5nJh412e824LPfdz',
  limit: 10,
})
```

```python
# This example uses the beta SDK. See https://github.com/stripe/stripe-python#public-preview-sdks
client = StripeClient("<<YOUR_SECRET_KEY>>")

releases = client.v1.reserve.releases.list({
  "reserve_plan": "resplan_61SToUQzaDa1N5nJh412e824LPfdz",
  "limit": 10,
})
```

```php
// This example uses the beta SDK. See https://github.com/stripe/stripe-php#public-preview-sdks
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$releases = $stripe->reserve->releases->all([
  'reserve_plan' => 'resplan_61SToUQzaDa1N5nJh412e824LPfdz',
  'limit' => 10,
]);
```

```java
// This example uses the beta SDK. See https://github.com/stripe/stripe-java#public-preview-sdks
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ReleaseListParams params =
  ReleaseListParams.builder()
    .setReservePlan("resplan_61SToUQzaDa1N5nJh412e824LPfdz")
    .setLimit(10L)
    .build();

StripeCollection<Release> stripeCollection =
  client.v1().reserve().releases().list(params);
```

```node
// This example uses the beta SDK. See https://github.com/stripe/stripe-node#public-preview-sdks
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const releases = await stripe.reserve.releases.list({
  reserve_plan: 'resplan_61SToUQzaDa1N5nJh412e824LPfdz',
  limit: 10,
});
```

```go
// This example uses the beta SDK. See https://github.com/stripe/stripe-go#public-preview-sdks
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.ReserveReleaseListParams{
  ReservePlan: stripe.String("resplan_61SToUQzaDa1N5nJh412e824LPfdz"),
}
params.Limit = stripe.Int64(10)
result := sc.V1ReserveReleases.List(context.TODO(), params)
```

```dotnet
// This example uses the beta SDK. See https://github.com/stripe/stripe-dotnet#public-preview-sdks
var options = new Stripe.Reserve.ReleaseListOptions
{
    ReservePlan = "resplan_61SToUQzaDa1N5nJh412e824LPfdz",
    Limit = 10,
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Reserve.Releases;
StripeList<Stripe.Reserve.Release> releases = service.List(options);
```

### Response

```json
{
  "object": "list",
  "data": [
    {
      "id": "resrel_61SxyHbQOe90T6sLB41Q8rCFhzAUW",
      "object": "reserve.release",
      "amount": 500,
      "created": 1753406491,
      "created_by": "application",
      "currency": "usd",
      "livemode": false,
      "metadata": {},
      "reason": "hold_released_early",
      "released_at": 1753406491,
      "reserve_hold": "reshold_61SxrUZH1aQJj97WT41Q8rCFhzAUW",
      "reserve_plan": null
    },
    {
      "id": "resrel_61SxxvDiTp12IiQA441Q8rCFhzAUW",
      "object": "reserve.release",
      "amount": 2904,
      "created": 1753405103,
      "created_by": "stripe",
      "currency": "usd",
      "livemode": false,
      "reason": "plan_disabled",
      "released_at": 1753405102,
      "reserve_hold": null,
      "reserve_plan": "resplan_61SxrVOzQu6XIJSCx41Q8rCFhzAUW"
    }
  ],
  "has_more": false,
  "url": "/v1/reserve/releases"
}
```