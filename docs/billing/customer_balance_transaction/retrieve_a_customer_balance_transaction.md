# Retrieve a customer balance transaction

Retrieves a specific customer balance transaction that updated the customer’s [balances](https://docs.stripe.com/docs/billing/customer/balance.md).

## Returns

Returns a customer balance transaction object if a valid identifier was provided.

```curl
curl https://api.stripe.com/v1/customers/cus_NcjdgdwZyI9Rj7/balance_transactions/cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe customer_balance_transactions retrieve cus_NcjdgdwZyI9Rj7 cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

customer_balance_transaction = client.v1.customers.balance_transactions.retrieve(
  'cus_NcjdgdwZyI9Rj7',
  'cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI',
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

customer_balance_transaction = client.v1.customers.balance_transactions.retrieve(
  "cus_NcjdgdwZyI9Rj7",
  "cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$customerBalanceTransaction = $stripe->customers->retrieveBalanceTransaction(
  'cus_NcjdgdwZyI9Rj7',
  'cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CustomerBalanceTransactionRetrieveParams params =
  CustomerBalanceTransactionRetrieveParams.builder().build();

CustomerBalanceTransaction customerBalanceTransaction =
  client.v1().customers().balanceTransactions().retrieve(
    "cus_NcjdgdwZyI9Rj7",
    "cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customerBalanceTransaction = await stripe.customers.retrieveBalanceTransaction(
  'cus_NcjdgdwZyI9Rj7',
  'cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CustomerBalanceTransactionRetrieveParams{
  Customer: stripe.String("cus_NcjdgdwZyI9Rj7"),
}
result, err := sc.V1CustomerBalanceTransactions.Retrieve(
  context.TODO(), "cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Customers.BalanceTransactions;
CustomerBalanceTransaction customerBalanceTransaction = service.Get(
    "cus_NcjdgdwZyI9Rj7",
    "cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI");
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
  "metadata": {},
  "type": "adjustment"
}
```