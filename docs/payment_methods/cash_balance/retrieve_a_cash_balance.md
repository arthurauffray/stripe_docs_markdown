# Retrieve a cash balance

Retrieves a customer’s cash balance.

## Returns

The Cash Balance object for a given customer.

```curl
curl https://api.stripe.com/v1/customers/cus_OaCLf8Fi1nbFpJ/cash_balance \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe cash_balances retrieve cus_OaCLf8Fi1nbFpJ
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

cash_balance = client.v1.customers.cash_balance.retrieve('cus_OaCLf8Fi1nbFpJ')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

cash_balance = client.v1.customers.cash_balance.retrieve("cus_OaCLf8Fi1nbFpJ")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$cashBalance = $stripe->customers->retrieveCashBalance('cus_OaCLf8Fi1nbFpJ', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CustomerCashBalanceRetrieveParams params =
  CustomerCashBalanceRetrieveParams.builder().build();

CashBalance cashBalance =
  client.v1().customers().cashBalance().retrieve("cus_OaCLf8Fi1nbFpJ", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const cashBalance = await stripe.customers.retrieveCashBalance('cus_OaCLf8Fi1nbFpJ');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CashBalanceRetrieveParams{
  Customer: stripe.String("cus_OaCLf8Fi1nbFpJ"),
}
result, err := sc.V1CashBalances.Retrieve(context.TODO(), params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Customers.CashBalance;
CashBalance cashBalance = service.Get("cus_OaCLf8Fi1nbFpJ");
```

### Response

```json
{
  "object": "cash_balance",
  "available": {
    "eur": 10000
  },
  "customer": "cus_OaCLf8Fi1nbFpJ",
  "livemode": false,
  "settings": {
    "reconciliation_mode": "automatic",
    "using_merchant_default": true
  }
}
```