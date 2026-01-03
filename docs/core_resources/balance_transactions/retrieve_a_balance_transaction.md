# Retrieve a balance transaction

Retrieves the balance transaction with the given ID.

Note that this endpoint previously used the path `/v1/balance/history/:id`.

## Returns

Returns a balance transaction if a valid balance transaction ID was provided. Raises [an error](https://docs.stripe.com/api/balance_transactions/retrieve.md#errors) otherwise.

```curl
curl https://api.stripe.com/v1/balance_transactions/txn_1MiN3gLkdIwHu7ixxapQrznl \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe balance_transactions retrieve txn_1MiN3gLkdIwHu7ixxapQrznl
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

balance_transaction = client.v1.balance_transactions.retrieve('txn_1MiN3gLkdIwHu7ixxapQrznl')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

balance_transaction = client.v1.balance_transactions.retrieve(
  "txn_1MiN3gLkdIwHu7ixxapQrznl",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$balanceTransaction = $stripe->balanceTransactions->retrieve(
  'txn_1MiN3gLkdIwHu7ixxapQrznl',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

BalanceTransactionRetrieveParams params =
  BalanceTransactionRetrieveParams.builder().build();

BalanceTransaction balanceTransaction =
  client.v1().balanceTransactions().retrieve("txn_1MiN3gLkdIwHu7ixxapQrznl", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const balanceTransaction = await stripe.balanceTransactions.retrieve(
  'txn_1MiN3gLkdIwHu7ixxapQrznl'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.BalanceTransactionRetrieveParams{}
result, err := sc.V1BalanceTransactions.Retrieve(
  context.TODO(), "txn_1MiN3gLkdIwHu7ixxapQrznl", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.BalanceTransactions;
BalanceTransaction balanceTransaction = service.Get("txn_1MiN3gLkdIwHu7ixxapQrznl");
```

### Response

```json
{
  "id": "txn_1MiN3gLkdIwHu7ixxapQrznl",
  "object": "balance_transaction",
  "amount": -400,
  "available_on": 1678043844,
  "created": 1678043844,
  "currency": "usd",
  "description": null,
  "exchange_rate": null,
  "fee": 0,
  "fee_details": [],
  "net": -400,
  "reporting_category": "transfer",
  "source": "tr_1MiN3gLkdIwHu7ixNCZvFdgA",
  "status": "available",
  "type": "transfer"
}
```