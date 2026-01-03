# Create a transfer

To send funds from your Stripe account to a connected account, you create a new transfer object. Your [Stripe balance](https://docs.stripe.com/api/transfers/create.md#balance) must be able to cover the transfer amount, or you’ll receive an “Insufficient Funds” error.

## Returns

Returns a transfer object if there were no initial errors with the transfer creation (e.g., insufficient funds).

## Parameters

- `currency` (enum, required)
  Three-letter [ISO code for currency](https://www.iso.org/iso-4217-currency-codes.html) in lowercase. Must be a [supported currency](https://docs.stripe.com/currencies.md).

- `destination` (string, required)
  The ID of a connected Stripe account. [See the Connect documentation](https://docs.stripe.com/docs/connect/separate-charges-and-transfers.md) for details.

- `amount` (integer, required)
  A positive integer in cents representing how much to transfer.

- `description` (string, optional)
  An arbitrary string attached to the object. Often useful for displaying to users.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `source_transaction` (string, optional)
  You can use this parameter to transfer funds from a charge before they are added to your available balance. A pending balance will transfer immediately but the funds will not become available until the original charge becomes available. [See the Connect documentation](https://docs.stripe.com/docs/connect/separate-charges-and-transfers.md#transfer-availability) for details.

- `source_type` (string, optional)
  The source balance to use for this transfer. One of `bank_account`, `card`, or `fpx`. For most users, this will default to `card`.

- `transfer_group` (string, optional)
  A string that identifies this transaction as part of a group. See the [Connect documentation](https://docs.stripe.com/docs/connect/separate-charges-and-transfers.md#transfer-options) for details.

```curl
curl https://api.stripe.com/v1/transfers \
  -u "<<YOUR_SECRET_KEY>>" \
  -d amount=400 \
  -d currency=usd \
  -d destination=acct_1MTfjCQ9PRzxEwkZ \
  -d transfer_group=ORDER_95
```

```cli
stripe transfers create  \
  --amount=400 \
  --currency=usd \
  --destination=acct_1MTfjCQ9PRzxEwkZ \
  --transfer-group=ORDER_95
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

transfer = client.v1.transfers.create({
  amount: 400,
  currency: 'usd',
  destination: 'acct_1MTfjCQ9PRzxEwkZ',
  transfer_group: 'ORDER_95',
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

transfer = client.v1.transfers.create({
  "amount": 400,
  "currency": "usd",
  "destination": "acct_1MTfjCQ9PRzxEwkZ",
  "transfer_group": "ORDER_95",
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$transfer = $stripe->transfers->create([
  'amount' => 400,
  'currency' => 'usd',
  'destination' => 'acct_1MTfjCQ9PRzxEwkZ',
  'transfer_group' => 'ORDER_95',
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TransferCreateParams params =
  TransferCreateParams.builder()
    .setAmount(400L)
    .setCurrency("usd")
    .setDestination("acct_1MTfjCQ9PRzxEwkZ")
    .setTransferGroup("ORDER_95")
    .build();

Transfer transfer = client.v1().transfers().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const transfer = await stripe.transfers.create({
  amount: 400,
  currency: 'usd',
  destination: 'acct_1MTfjCQ9PRzxEwkZ',
  transfer_group: 'ORDER_95',
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TransferCreateParams{
  Amount: stripe.Int64(400),
  Currency: stripe.String(stripe.CurrencyUSD),
  Destination: stripe.String("acct_1MTfjCQ9PRzxEwkZ"),
  TransferGroup: stripe.String("ORDER_95"),
}
result, err := sc.V1Transfers.Create(context.TODO(), params)
```

```dotnet
var options = new TransferCreateOptions
{
    Amount = 400,
    Currency = "usd",
    Destination = "acct_1MTfjCQ9PRzxEwkZ",
    TransferGroup = "ORDER_95",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Transfers;
Transfer transfer = service.Create(options);
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
```