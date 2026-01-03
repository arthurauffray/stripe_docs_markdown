# Retrieve a reversal

By default, you can see the 10 most recent reversals stored directly on the transfer object, but you can also retrieve details about a specific reversal stored on the transfer.

## Returns

Returns the reversal object.

```curl
curl https://api.stripe.com/v1/transfers/tr_1Mio2dLkdIwHu7ixsUuCxJpu/reversals/trr_1Mio2eLkdIwHu7ixN5LPJS4a \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe transfer_reversals retrieve tr_1Mio2dLkdIwHu7ixsUuCxJpu trr_1Mio2eLkdIwHu7ixN5LPJS4a
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

reversal = client.v1.transfers.reversals.retrieve(
  'tr_1Mio2dLkdIwHu7ixsUuCxJpu',
  'trr_1Mio2eLkdIwHu7ixN5LPJS4a',
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

reversal = client.v1.transfers.reversals.retrieve(
  "tr_1Mio2dLkdIwHu7ixsUuCxJpu",
  "trr_1Mio2eLkdIwHu7ixN5LPJS4a",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$transferReversal = $stripe->transfers->retrieveReversal(
  'tr_1Mio2dLkdIwHu7ixsUuCxJpu',
  'trr_1Mio2eLkdIwHu7ixN5LPJS4a',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TransferReversalRetrieveParams params =
  TransferReversalRetrieveParams.builder().build();

TransferReversal transferReversal =
  client.v1().transfers().reversals().retrieve(
    "tr_1Mio2dLkdIwHu7ixsUuCxJpu",
    "trr_1Mio2eLkdIwHu7ixN5LPJS4a",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const transferReversal = await stripe.transfers.retrieveReversal(
  'tr_1Mio2dLkdIwHu7ixsUuCxJpu',
  'trr_1Mio2eLkdIwHu7ixN5LPJS4a'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TransferReversalRetrieveParams{
  ID: stripe.String("tr_1Mio2dLkdIwHu7ixsUuCxJpu"),
}
result, err := sc.V1TransferReversals.Retrieve(
  context.TODO(), "trr_1Mio2eLkdIwHu7ixN5LPJS4a", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Transfers.Reversals;
TransferReversal transferReversal = service.Get(
    "tr_1Mio2dLkdIwHu7ixsUuCxJpu",
    "trr_1Mio2eLkdIwHu7ixN5LPJS4a");
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