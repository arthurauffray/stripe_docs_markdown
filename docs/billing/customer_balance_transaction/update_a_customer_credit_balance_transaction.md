# Update a customer credit balance transaction

Most credit balance transaction fields are immutable, but you may update its `description` and `metadata`.

## Returns

Returns a customer balance transaction object if the call succeeded.

## Parameters

- `description` (string, optional)
  An arbitrary string attached to the object. Often useful for displaying to users.

  The maximum length is 350 characters.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/customers/cus_NcjdgdwZyI9Rj7/balance_transactions/cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
```

```cli
stripe customer_balance_transactions update cus_NcjdgdwZyI9Rj7 cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI \
  -d "metadata[order_id]"=6735
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

customer_balance_transaction = client.v1.customers.balance_transactions.update(
  'cus_NcjdgdwZyI9Rj7',
  'cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI',
  {metadata: {order_id: '6735'}},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

customer_balance_transaction = client.v1.customers.balance_transactions.update(
  "cus_NcjdgdwZyI9Rj7",
  "cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI",
  {"metadata": {"order_id": "6735"}},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$customerBalanceTransaction = $stripe->customers->updateBalanceTransaction(
  'cus_NcjdgdwZyI9Rj7',
  'cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI',
  ['metadata' => ['order_id' => '6735']]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CustomerBalanceTransactionUpdateParams params =
  CustomerBalanceTransactionUpdateParams.builder()
    .putMetadata("order_id", "6735")
    .build();

CustomerBalanceTransaction customerBalanceTransaction =
  client.v1().customers().balanceTransactions().update(
    "cus_NcjdgdwZyI9Rj7",
    "cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customerBalanceTransaction = await stripe.customers.updateBalanceTransaction(
  'cus_NcjdgdwZyI9Rj7',
  'cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI',
  {
    metadata: {
      order_id: '6735',
    },
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CustomerBalanceTransactionUpdateParams{
  Customer: stripe.String("cus_NcjdgdwZyI9Rj7"),
}
params.AddMetadata("order_id", "6735")
result, err := sc.V1CustomerBalanceTransactions.Update(
  context.TODO(), "cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI", params)
```

```dotnet
var options = new CustomerBalanceTransactionUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Customers.BalanceTransactions;
CustomerBalanceTransaction customerBalanceTransaction = service.Update(
    "cus_NcjdgdwZyI9Rj7",
    "cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI",
    options);
```

### Response

```json
{
  "id": "cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI",
  "object": "customer_balance_transaction",
  "amount": -500,
  "created": 1680216086,
  "credit_note": null,
  "currency": "usd",
  "customer": "cus_NcjdgdwZyI9Rj7",
  "description": null,
  "ending_balance": -500,
  "invoice": null,
  "livemode": false,
  "metadata": {
    "order_id": "6735"
  },
  "type": "adjustment"
}
```