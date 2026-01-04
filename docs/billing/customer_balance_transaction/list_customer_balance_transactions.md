# List customer balance transactions

Returns a list of transactions that updated the customer’s [balances](https://docs.stripe.com/docs/billing/customer/balance.md).

## Returns

A dictionary with a `data` property that contains an array of up to `limit` customer balance transactions, starting after item `starting_after`. Each entry in the array is a separate customer balance transaction object. If no more items are available, the resulting array will be empty.

## Parameters

- `created` (object, optional)
  Only return customer balance transactions that were created during the given date interval.

  - `created.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `created.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `created.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `created.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `invoice` (string, optional)
  Only return transactions that are related to the specified invoice.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/customers/cus_NcjdgdwZyI9Rj7/balance_transactions \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe customers balance_transactions cus_NcjdgdwZyI9Rj7 \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

customer_balance_transactions = client.v1.customers.balance_transactions.list(
  'cus_NcjdgdwZyI9Rj7',
  {limit: 3},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

customer_balance_transactions = client.v1.customers.balance_transactions.list(
  "cus_NcjdgdwZyI9Rj7",
  {"limit": 3},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$customerBalanceTransactions = $stripe->customers->allBalanceTransactions(
  'cus_NcjdgdwZyI9Rj7',
  ['limit' => 3]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CustomerBalanceTransactionListParams params =
  CustomerBalanceTransactionListParams.builder().setLimit(3L).build();

StripeCollection<CustomerBalanceTransaction> stripeCollection =
  client.v1().customers().balanceTransactions().list("cus_NcjdgdwZyI9Rj7", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customerBalanceTransactions = await stripe.customers.listBalanceTransactions(
  'cus_NcjdgdwZyI9Rj7',
  {
    limit: 3,
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CustomerBalanceTransactionListParams{
  Customer: stripe.String("cus_NcjdgdwZyI9Rj7"),
}
params.Limit = stripe.Int64(3)
result := sc.V1CustomerBalanceTransactions.List(context.TODO(), params)
```

```dotnet
var options = new CustomerBalanceTransactionListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Customers.BalanceTransactions;
StripeList<CustomerBalanceTransaction> customerBalanceTransactions = service.List(
    "cus_NcjdgdwZyI9Rj7",
    options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/customers/cus_NcjdgdwZyI9Rj7/balance_transactions",
  "has_more": false,
  "data": [
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
  ]
}
```