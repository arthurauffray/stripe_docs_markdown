# Create a transfer reversal

When you create a new reversal, you must specify a transfer to create it on.

When reversing transfers, you can optionally reverse part of the transfer. You can do so as many times as you wish until the entire transfer has been reversed.

Once entirely reversed, a transfer can’t be reversed again. This method will return an error when called on an already-reversed transfer, or when trying to reverse more money than is left on a transfer.

## Returns

Returns a transfer reversal object if the reversal succeeded. Raises [an error](https://docs.stripe.com/api/transfer_reversals/create.md#errors) if the transfer has already been reversed or an invalid transfer identifier was provided.

## Parameters

- `amount` (integer, optional)
  A positive integer in cents representing how much of this transfer to reverse. Can only reverse up to the unreversed amount remaining of the transfer. Partial transfer reversals are only allowed for transfers to Stripe Accounts. Defaults to the entire transfer amount.

- `description` (string, optional)
  An arbitrary string which you can attach to a reversal object. This will be unset if you POST an empty value.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `refund_application_fee` (boolean, optional)
  Boolean indicating whether the application fee should be refunded when reversing this transfer. If a full transfer reversal is given, the full application fee will be refunded. Otherwise, the application fee will be refunded with an amount proportional to the amount of the transfer reversed.

```curl
curl https://api.stripe.com/v1/transfers/tr_1Mio2dLkdIwHu7ixsUuCxJpu/reversals \
  -u "<<YOUR_SECRET_KEY>>" \
  -d amount=400
```

```cli
stripe transfer_reversals create tr_1Mio2dLkdIwHu7ixsUuCxJpu \
  --amount=400
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

reversal = client.v1.transfers.reversals.create(
  'tr_1Mio2dLkdIwHu7ixsUuCxJpu',
  {amount: 400},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

reversal = client.v1.transfers.reversals.create(
  "tr_1Mio2dLkdIwHu7ixsUuCxJpu",
  {"amount": 400},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$transferReversal = $stripe->transfers->createReversal(
  'tr_1Mio2dLkdIwHu7ixsUuCxJpu',
  ['amount' => 400]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TransferReversalCreateParams params =
  TransferReversalCreateParams.builder().setAmount(400L).build();

TransferReversal transferReversal =
  client.v1().transfers().reversals().create("tr_1Mio2dLkdIwHu7ixsUuCxJpu", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const transferReversal = await stripe.transfers.createReversal(
  'tr_1Mio2dLkdIwHu7ixsUuCxJpu',
  {
    amount: 400,
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TransferReversalCreateParams{
  Amount: stripe.Int64(400),
  ID: stripe.String("tr_1Mio2dLkdIwHu7ixsUuCxJpu"),
}
result, err := sc.V1TransferReversals.Create(context.TODO(), params)
```

```dotnet
var options = new TransferReversalCreateOptions { Amount = 400 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Transfers.Reversals;
TransferReversal transferReversal = service.Create(
    "tr_1Mio2dLkdIwHu7ixsUuCxJpu",
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
  "metadata": {},
  "source_refund": null,
  "transfer": "tr_1Mio2dLkdIwHu7ixsUuCxJpu"
}
```