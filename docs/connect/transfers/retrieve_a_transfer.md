# Retrieve a transfer

Retrieves the details of an existing transfer. Supply the unique transfer ID from either a transfer creation request or the transfer list, and Stripe will return the corresponding transfer information.

## Returns

Returns a transfer object if a valid identifier was provided, and raises [an error](https://docs.stripe.com/api/transfers/retrieve.md#errors) otherwise.

```curl
curl https://api.stripe.com/v1/transfers/tr_1MiN3gLkdIwHu7ixNCZvFdgA \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe transfers retrieve tr_1MiN3gLkdIwHu7ixNCZvFdgA
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

transfer = client.v1.transfers.retrieve('tr_1MiN3gLkdIwHu7ixNCZvFdgA')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

transfer = client.v1.transfers.retrieve("tr_1MiN3gLkdIwHu7ixNCZvFdgA")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$transfer = $stripe->transfers->retrieve('tr_1MiN3gLkdIwHu7ixNCZvFdgA', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TransferRetrieveParams params = TransferRetrieveParams.builder().build();

Transfer transfer =
  client.v1().transfers().retrieve("tr_1MiN3gLkdIwHu7ixNCZvFdgA", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const transfer = await stripe.transfers.retrieve('tr_1MiN3gLkdIwHu7ixNCZvFdgA');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TransferRetrieveParams{}
result, err := sc.V1Transfers.Retrieve(
  context.TODO(), "tr_1MiN3gLkdIwHu7ixNCZvFdgA", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Transfers;
Transfer transfer = service.Get("tr_1MiN3gLkdIwHu7ixNCZvFdgA");
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