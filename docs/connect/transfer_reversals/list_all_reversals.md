# List all reversals

You can see a list of the reversals belonging to a specific transfer. Note that the 10 most recent reversals are always available by default on the transfer object. If you need more than those 10, you can use this API method and the `limit` and `starting_after` parameters to page through additional reversals.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` reversals, starting after reversal `starting_after`. Each entry in the array is a separate reversal object. If no more reversals are available, the resulting array will be empty. If you provide a non-existent transfer ID, this call raises [an error](https://docs.stripe.com/api/transfer_reversals/list.md#errors).

## Parameters

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/transfers/tr_1Mio2dLkdIwHu7ixsUuCxJpu/reversals \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe transfer_reversals list tr_1Mio2dLkdIwHu7ixsUuCxJpu \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

reversals = client.v1.transfers.reversals.list(
  'tr_1Mio2dLkdIwHu7ixsUuCxJpu',
  {limit: 3},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

reversals = client.v1.transfers.reversals.list(
  "tr_1Mio2dLkdIwHu7ixsUuCxJpu",
  {"limit": 3},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$transferReversals = $stripe->transfers->allReversals(
  'tr_1Mio2dLkdIwHu7ixsUuCxJpu',
  ['limit' => 3]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TransferReversalListParams params =
  TransferReversalListParams.builder().setLimit(3L).build();

StripeCollection<TransferReversal> stripeCollection =
  client.v1().transfers().reversals().list("tr_1Mio2dLkdIwHu7ixsUuCxJpu", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const transferReversals = await stripe.transfers.listReversals(
  'tr_1Mio2dLkdIwHu7ixsUuCxJpu',
  {
    limit: 3,
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TransferReversalListParams{
  ID: stripe.String("tr_1Mio2dLkdIwHu7ixsUuCxJpu"),
}
params.Limit = stripe.Int64(3)
result := sc.V1TransferReversals.List(context.TODO(), params)
```

```dotnet
var options = new TransferReversalListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Transfers.Reversals;
StripeList<TransferReversal> transferReversals = service.List(
    "tr_1Mio2dLkdIwHu7ixsUuCxJpu",
    options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/transfers/tr_1Mio2dLkdIwHu7ixsUuCxJpu/reversals",
  "has_more": false,
  "data": [
    {
      "id": "trr_1Mio2eLkdIwHu7ixN5LPJS4a",
      "object": "transfer_reversal",
      "amount": 400,
      "balance_transaction": "txn_1Mio2eLkdIwHu7ixosfrbjhW",
      "created": 1678147568,
      "currency": "usd",
      "destination_payment_refund": "pyr_1Mio2eQ9PRzxEwkZYewpaIFB",
      "metadata": {},
      "source_refund": null,
      "transfer": "tr_1Mio2dLkdIwHu7ixsUuCxJpu"
    }
  ]
}
```