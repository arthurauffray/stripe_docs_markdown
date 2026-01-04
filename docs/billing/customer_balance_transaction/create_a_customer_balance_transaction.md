# Create a customer balance transaction

Creates an immutable transaction that updates the customer’s credit [balance](https://docs.stripe.com/docs/billing/customer/balance.md).

## Returns

Returns a customer balance transaction object if the call succeeded.

## Parameters

- `amount` (integer, required)
  The integer amount in **cents** to apply to the customer’s credit balance.

- `currency` (enum, required)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). Specifies the [`invoice_credit_balance`](https://docs.stripe.com/docs/api/customers/object.md#customer_object-invoice_credit_balance) that this transaction will apply to. If the customer’s `currency` is not set, it will be updated to this value.

- `description` (string, optional)
  An arbitrary string attached to the object. Often useful for displaying to users.

  The maximum length is 350 characters.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/customers/cus_NcjdgdwZyI9Rj7/balance_transactions \
  -u "<<YOUR_SECRET_KEY>>" \
  -d amount=-500 \
  -d currency=usd
```

```cli
stripe customer_balance_transactions create cus_NcjdgdwZyI9Rj7 \
  --amount=-500 \
  --currency=usd
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

customer_balance_transaction = client.v1.customers.balance_transactions.create(
  'cus_NcjdgdwZyI9Rj7',
  {
    amount: -500,
    currency: 'usd',
  },
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

customer_balance_transaction = client.v1.customers.balance_transactions.create(
  "cus_NcjdgdwZyI9Rj7",
  {"amount": -500, "currency": "usd"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$customerBalanceTransaction = $stripe->customers->createBalanceTransaction(
  'cus_NcjdgdwZyI9Rj7',
  [
    'amount' => -500,
    'currency' => 'usd',
  ]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CustomerBalanceTransactionCreateParams params =
  CustomerBalanceTransactionCreateParams.builder()
    .setAmount(-500L)
    .setCurrency("usd")
    .build();

CustomerBalanceTransaction customerBalanceTransaction =
  client.v1().customers().balanceTransactions().create("cus_NcjdgdwZyI9Rj7", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customerBalanceTransaction = await stripe.customers.createBalanceTransaction(
  'cus_NcjdgdwZyI9Rj7',
  {
    amount: -500,
    currency: 'usd',
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CustomerBalanceTransactionCreateParams{
  Amount: stripe.Int64(-500),
  Currency: stripe.String(stripe.CurrencyUSD),
  Customer: stripe.String("cus_NcjdgdwZyI9Rj7"),
}
result, err := sc.V1CustomerBalanceTransactions.Create(context.TODO(), params)
```

```dotnet
var options = new CustomerBalanceTransactionCreateOptions
{
    Amount = -500,
    Currency = "usd",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Customers.BalanceTransactions;
CustomerBalanceTransaction customerBalanceTransaction = service.Create(
    "cus_NcjdgdwZyI9Rj7",
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
  "metadata": {},
  "type": "adjustment"
}
```