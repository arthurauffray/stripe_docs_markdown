# Retrieve a cash balance transaction

Retrieves a specific cash balance transaction, which updated the customer’s [cash balance](https://docs.stripe.com/docs/payments/customer-balance.md).

## Returns

Returns a cash balance transaction object if a valid identifier was provided.

```curl
curl https://api.stripe.com/v1/customers/cus_9s6XKzkNRiz8i3/cash_balance_transactions/ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe customer_cash_balance_transactions retrieve cus_9s6XKzkNRiz8i3 ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

customer_cash_balance_transaction = client.v1.customers.cash_balance_transactions.retrieve(
  'cus_9s6XKzkNRiz8i3',
  'ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF',
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

customer_cash_balance_transaction = client \
  .v1 \
  .customers \
  .cash_balance_transactions \
  .retrieve(
  "cus_9s6XKzkNRiz8i3",
  "ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$customerCashBalanceTransaction = $stripe->customers->retrieveCashBalanceTransaction(
  'cus_9s6XKzkNRiz8i3',
  'ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CustomerCashBalanceTransactionRetrieveParams params =
  CustomerCashBalanceTransactionRetrieveParams.builder().build();

CustomerCashBalanceTransaction customerCashBalanceTransaction =
  client.v1().customers().cashBalanceTransactions().retrieve(
    "cus_9s6XKzkNRiz8i3",
    "ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customerCashBalanceTransaction = await stripe
  .customers
  .retrieveCashBalanceTransaction(
  'cus_9s6XKzkNRiz8i3',
  'ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CustomerCashBalanceTransactionRetrieveParams{
  Customer: stripe.String("cus_9s6XKzkNRiz8i3"),
}
result, err := sc.V1CustomerCashBalanceTransactions.Retrieve(
  context.TODO(), "ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Customers.CashBalanceTransactions;
CustomerCashBalanceTransaction customerCashBalanceTransaction = service.Get(
    "cus_9s6XKzkNRiz8i3",
    "ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF");
```

### Response

```json
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
```