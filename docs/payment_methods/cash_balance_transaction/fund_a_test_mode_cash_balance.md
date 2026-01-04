# Fund a test mode cash balance

Create an incoming testmode bank transfer

## Returns

Returns a specific cash balance transaction, which funded the customer’s [cash balance](https://docs.stripe.com/docs/payments/customer-balance.md).

## Parameters

- `amount` (integer, required)
  Amount to be used for this test cash balance transaction. A positive integer representing how much to fund in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal) (e.g., 100 cents to fund $1.00 or 100 to fund ¥100, a zero-decimal currency).

- `currency` (enum, required)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `reference` (string, optional)
  A description of the test funding. This simulates free-text references supplied by customers when making bank transfers to their cash balance. You can use this to test how Stripe’s [reconciliation algorithm](https://docs.stripe.com/docs/payments/customer-balance/reconciliation.md) applies to different user inputs.

```curl
curl https://api.stripe.com/v1/test_helpers/customers/cus_9s6XKzkNRiz8i3/fund_cash_balance \
  -u "<<YOUR_SECRET_KEY>>" \
  -d amount=5000 \
  -d currency=eur
```

```cli
stripe test_helpers customers fund_cash_balance cus_9s6XKzkNRiz8i3 \
  --amount=5000 \
  --currency=eur
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

customer_cash_balance_transaction = client.v1.test_helpers.customers.fund_cash_balance(
  'cus_9s6XKzkNRiz8i3',
  {
    amount: 5000,
    currency: 'eur',
  },
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

customer_cash_balance_transaction = client \
  .v1 \
  .test_helpers \
  .customers \
  .fund_cash_balance(
  "cus_9s6XKzkNRiz8i3",
  {"amount": 5000, "currency": "eur"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$customerCashBalanceTransaction = $stripe->testHelpers->customers->fundCashBalance(
  'cus_9s6XKzkNRiz8i3',
  [
    'amount' => 5000,
    'currency' => 'eur',
  ]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CustomerFundCashBalanceParams params =
  CustomerFundCashBalanceParams.builder()
    .setAmount(5000L)
    .setCurrency("eur")
    .build();

CustomerCashBalanceTransaction customerCashBalanceTransaction =
  client.v1().testHelpers().customers().fundCashBalance(
    "cus_9s6XKzkNRiz8i3",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customerCashBalanceTransaction = await stripe
  .testHelpers
  .customers
  .fundCashBalance(
  'cus_9s6XKzkNRiz8i3',
  {
    amount: 5000,
    currency: 'eur',
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TestHelpersCustomerFundCashBalanceParams{
  Amount: stripe.Int64(5000),
  Currency: stripe.String(stripe.CurrencyEUR),
}
result, err := sc.V1TestHelpersCustomers.FundCashBalance(
  context.TODO(), "cus_9s6XKzkNRiz8i3", params)
```

```dotnet
var options = new Stripe.TestHelpers.CustomerFundCashBalanceOptions
{
    Amount = 5000,
    Currency = "eur",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.TestHelpers.Customers;
CustomerCashBalanceTransaction customerCashBalanceTransaction = service
    .FundCashBalance("cus_9s6XKzkNRiz8i3", options);
```

### Response

```json
{
  "id": "ccsbtxn_1NlhIV2eZvKYlo2CKwRcXkii",
  "object": "customer_cash_balance_transaction",
  "created": 1693612963,
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