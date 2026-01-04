# List cash balance transactions

Returns a list of transactions that modified the customer’s [cash balance](https://docs.stripe.com/docs/payments/customer-balance.md).

## Returns

A dictionary with a `data` property that contains an array of up to `limit` cash balance transactions, starting after item `starting_after`. Each entry in the array is a separate cash balance transaction object. If no more items are available, the resulting array will be empty.

## Parameters

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/customers/cus_9s6XKzkNRiz8i3/cash_balance_transactions \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe customer_cash_balance_transactions list cus_9s6XKzkNRiz8i3 \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

customer_cash_balance_transactions = client.v1.customers.cash_balance_transactions.list(
  'cus_9s6XKzkNRiz8i3',
  {limit: 3},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

customer_cash_balance_transactions = client \
  .v1 \
  .customers \
  .cash_balance_transactions \
  .list(
  "cus_9s6XKzkNRiz8i3",
  {"limit": 3},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$customerCashBalanceTransactions = $stripe->customers->allCashBalanceTransactions(
  'cus_9s6XKzkNRiz8i3',
  ['limit' => 3]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CustomerCashBalanceTransactionListParams params =
  CustomerCashBalanceTransactionListParams.builder().setLimit(3L).build();

StripeCollection<CustomerCashBalanceTransaction> stripeCollection =
  client.v1().customers().cashBalanceTransactions().list(
    "cus_9s6XKzkNRiz8i3",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customerCashBalanceTransactions = await stripe
  .customers
  .listCashBalanceTransactions(
  'cus_9s6XKzkNRiz8i3',
  {
    limit: 3,
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CustomerCashBalanceTransactionListParams{
  Customer: stripe.String("cus_9s6XKzkNRiz8i3"),
}
params.Limit = stripe.Int64(3)
result := sc.V1CustomerCashBalanceTransactions.List(context.TODO(), params)
```

```dotnet
var options = new CustomerCashBalanceTransactionListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Customers.CashBalanceTransactions;
StripeList<CustomerCashBalanceTransaction> customerCashBalanceTransactions = service
    .List("cus_9s6XKzkNRiz8i3", options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/customers/cus_9s6XKzkNRiz8i3/cash_balance_transactions",
  "has_more": false,
  "data": [
    {
      "id": "ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF",
      "object": "customer_cash_balance_transaction",
      "created": 1690829143,
      "currency": "eur",
      "customer": "cus_9s6XKzkNRiz8i3",
      "ending_balance": 10000,
      "funded": {
        "bank_transfer": {
          "eu_bank_transfer": {
            "bic": "BANKDEAAXXX",
            "iban_last4": "7089",
            "sender_name": "Sample Business GmbH"
          },
          "reference": "Payment for Invoice 28278FC-155",
          "type": "eu_bank_transfer"
        }
      },
      "livemode": false,
      "net_amount": 5000,
      "type": "funded"
    }
  ]
}
```