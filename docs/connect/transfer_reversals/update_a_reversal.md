# Update a reversal

Updates the specified reversal by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

This request only accepts metadata and description as arguments.

## Returns

Returns the reversal object if the update succeeded. This call will raise [an error](https://docs.stripe.com/api/transfer_reversals/update.md#errors) if update parameters are invalid.

## Parameters

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/transfers/tr_1Mio2dLkdIwHu7ixsUuCxJpu/reversals/trr_1Mio2eLkdIwHu7ixN5LPJS4a \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
```

```cli
stripe transfer_reversals update tr_1Mio2dLkdIwHu7ixsUuCxJpu trr_1Mio2eLkdIwHu7ixN5LPJS4a \
  -d "metadata[order_id]"=6735
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

reversal = client.v1.transfers.reversals.update(
  'tr_1Mio2dLkdIwHu7ixsUuCxJpu',
  'trr_1Mio2eLkdIwHu7ixN5LPJS4a',
  {metadata: {order_id: '6735'}},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

reversal = client.v1.transfers.reversals.update(
  "tr_1Mio2dLkdIwHu7ixsUuCxJpu",
  "trr_1Mio2eLkdIwHu7ixN5LPJS4a",
  {"metadata": {"order_id": "6735"}},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$transferReversal = $stripe->transfers->updateReversal(
  'tr_1Mio2dLkdIwHu7ixsUuCxJpu',
  'trr_1Mio2eLkdIwHu7ixN5LPJS4a',
  ['metadata' => ['order_id' => '6735']]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TransferReversalUpdateParams params =
  TransferReversalUpdateParams.builder().putMetadata("order_id", "6735").build();

TransferReversal transferReversal =
  client.v1().transfers().reversals().update(
    "tr_1Mio2dLkdIwHu7ixsUuCxJpu",
    "trr_1Mio2eLkdIwHu7ixN5LPJS4a",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const transferReversal = await stripe.transfers.updateReversal(
  'tr_1Mio2dLkdIwHu7ixsUuCxJpu',
  'trr_1Mio2eLkdIwHu7ixN5LPJS4a',
  {
    metadata: {
      order_id: '6735',
    },
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TransferReversalUpdateParams{
  ID: stripe.String("tr_1Mio2dLkdIwHu7ixsUuCxJpu"),
}
params.AddMetadata("order_id", "6735")
result, err := sc.V1TransferReversals.Update(
  context.TODO(), "trr_1Mio2eLkdIwHu7ixN5LPJS4a", params)
```

```dotnet
var options = new TransferReversalUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Transfers.Reversals;
TransferReversal transferReversal = service.Update(
    "tr_1Mio2dLkdIwHu7ixsUuCxJpu",
    "trr_1Mio2eLkdIwHu7ixN5LPJS4a",
    options);
```

### Response

```json
{
  "id": "trr_1Mio2eLkdIwHu7ixN5LPJS4a",
  "object": "transfer_reversal",
  "amount": 400,
  "balance_transaction": "txn_1Mio2eLkdIwHu7ixosfrbjhW",
  "created": 1678147568,
  "currency": "usd",
  "destination_payment_refund": "pyr_1Mio2eQ9PRzxEwkZYewpaIFB",
  "metadata": {
    "order_id": "6735"
  },
  "source_refund": null,
  "transfer": "tr_1Mio2dLkdIwHu7ixsUuCxJpu"
}
```