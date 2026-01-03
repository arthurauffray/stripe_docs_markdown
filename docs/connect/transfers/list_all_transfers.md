# List all transfers

Returns a list of existing transfers sent to connected accounts. The transfers are returned in sorted order, with the most recently created transfers appearing first.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` transfers, starting after transfer `starting_after`. Each entry in the array is a separate transfer object. If no more transfers are available, the resulting array will be empty.

## Parameters

- `created` (object, optional)
  Only return transfers that were created during the given date interval.

  - `created.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `created.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `created.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `created.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `destination` (string, optional)
  Only return transfers for the destination specified by this account ID.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `transfer_group` (string, optional)
  Only return transfers with the specified transfer group.

```curl
curl -G https://api.stripe.com/v1/transfers \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe transfers list  \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

transfers = client.v1.transfers.list({limit: 3})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

transfers = client.v1.transfers.list({"limit": 3})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$transfers = $stripe->transfers->all(['limit' => 3]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TransferListParams params = TransferListParams.builder().setLimit(3L).build();

StripeCollection<Transfer> stripeCollection = client.v1().transfers().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const transfers = await stripe.transfers.list({
  limit: 3,
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TransferListParams{}
params.Limit = stripe.Int64(3)
result := sc.V1Transfers.List(context.TODO(), params)
```

```dotnet
var options = new TransferListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Transfers;
StripeList<Transfer> transfers = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/transfers",
  "has_more": false,
  "data": [
    {
      "id": "tr_1MiN3gLkdIwHu7ixNCZvFdgA",
      "object": "transfer",
      "amount": 400,
      "amount_reversed": 0,
      "balance_transaction": "txn_1MiN3gLkdIwHu7ixxapQrznl",
      "created": 1678043844,
      "currency": "usd",
      "description": null,
      "destination": "acct_1MTfjCQ9PRzxEwkZ",
      "destination_payment": "py_1MiN3gQ9PRzxEwkZWTPGNq9o",
      "livemode": false,
      "metadata": {},
      "reversals": {
        "object": "list",
        "data": [],
        "has_more": false,
        "total_count": 0,
        "url": "/v1/transfers/tr_1MiN3gLkdIwHu7ixNCZvFdgA/reversals"
      },
      "reversed": false,
      "source_transaction": null,
      "source_type": "card",
      "transfer_group": "ORDER_95"
    }
  ]
}
```