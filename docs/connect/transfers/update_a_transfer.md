# Update a transfer

Updates the specified transfer by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

This request accepts only metadata as an argument.

## Returns

Returns the transfer object if the update succeeded. This call will raise [an error](https://docs.stripe.com/api/transfers/update.md#errors) if update parameters are invalid.

## Parameters

- `description` (string, optional)
  An arbitrary string attached to the object. Often useful for displaying to users.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/transfers/tr_1MiN3gLkdIwHu7ixNCZvFdgA \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
```

```cli
stripe transfers update tr_1MiN3gLkdIwHu7ixNCZvFdgA \
  -d "metadata[order_id]"=6735
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

transfer = client.v1.transfers.update(
  'tr_1MiN3gLkdIwHu7ixNCZvFdgA',
  {metadata: {order_id: '6735'}},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

transfer = client.v1.transfers.update(
  "tr_1MiN3gLkdIwHu7ixNCZvFdgA",
  {"metadata": {"order_id": "6735"}},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$transfer = $stripe->transfers->update(
  'tr_1MiN3gLkdIwHu7ixNCZvFdgA',
  ['metadata' => ['order_id' => '6735']]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TransferUpdateParams params =
  TransferUpdateParams.builder().putMetadata("order_id", "6735").build();

Transfer transfer =
  client.v1().transfers().update("tr_1MiN3gLkdIwHu7ixNCZvFdgA", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const transfer = await stripe.transfers.update(
  'tr_1MiN3gLkdIwHu7ixNCZvFdgA',
  {
    metadata: {
      order_id: '6735',
    },
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TransferUpdateParams{}
params.AddMetadata("order_id", "6735")
result, err := sc.V1Transfers.Update(
  context.TODO(), "tr_1MiN3gLkdIwHu7ixNCZvFdgA", params)
```

```dotnet
var options = new TransferUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Transfers;
Transfer transfer = service.Update("tr_1MiN3gLkdIwHu7ixNCZvFdgA", options);
```

### Response

```json
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
  "metadata": {
    "order_id": "6735"
  },
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
```