# List all disputes

Returns a list of Issuing `Dispute` objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` disputes, starting after dispute `starting_after`. Each entry in the array is a separate Issuing `Dispute` object. If no more disputes are available, the resulting array will be empty.

## Parameters

- `created` (object, optional)
  Only return Issuing disputes that were created during the given date interval.

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

- `status` (enum, optional)
  Select Issuing disputes with the given status.
Possible enum values:
  - `expired`
    The dispute has expired.

  - `lost`
    The dispute is lost.

  - `submitted`
    The dispute has been submitted to Stripe.

  - `unsubmitted`
    The dispute is pending submission to Stripe.

  - `won`
    The dispute is won.

- `transaction` (string, optional)
  Select the Issuing dispute for the given transaction.

```curl
curl -G https://api.stripe.com/v1/issuing/disputes \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe issuing disputes list  \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

disputes = client.v1.issuing.disputes.list({limit: 3})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

disputes = client.v1.issuing.disputes.list({"limit": 3})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$disputes = $stripe->issuing->disputes->all(['limit' => 3]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

DisputeListParams params = DisputeListParams.builder().setLimit(3L).build();

StripeCollection<Dispute> stripeCollection =
  client.v1().issuing().disputes().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const disputes = await stripe.issuing.disputes.list({
  limit: 3,
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.IssuingDisputeListParams{}
params.Limit = stripe.Int64(3)
result := sc.V1IssuingDisputes.List(context.TODO(), params)
```

```dotnet
var options = new Stripe.Issuing.DisputeListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Issuing.Disputes;
StripeList<Stripe.Issuing.Dispute> disputes = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/issuing/disputes",
  "has_more": false,
  "data": [
    {
      "id": "idp_1MykdxFtDWhhyHE1BFAV3osZ",
      "object": "issuing.dispute",
      "amount": 100,
      "created": 1681947753,
      "currency": "usd",
      "evidence": {
        "fraudulent": {
          "additional_documentation": null,
          "dispute_explanation": null,
          "explanation": "This transaction is fraudulent.",
          "uncategorized_file": null
        },
        "reason": "fraudulent"
      },
      "livemode": false,
      "metadata": {},
      "status": "unsubmitted",
      "transaction": "ipi_1MykXhFtDWhhyHE1UjsZZ3xQ"
    }
  ]
}
```