# Update a cash balance's settings

Changes the settings on a customer’s cash balance.

## Returns

The customer’s cash balance, with the updated settings.

## Parameters

- `settings` (object, optional)
  A hash of settings for this cash balance.

  - `settings.reconciliation_mode` (enum, optional)
    Controls how funds transferred by the customer are applied to payment intents and invoices. Valid options are `automatic`, `manual`, or `merchant_default`. For more information about these reconciliation modes, see [Reconciliation](https://docs.stripe.com/docs/payments/customer-balance/reconciliation.md).
Possible enum values:
    - `automatic`
    - `manual`
    - `merchant_default`

```curl
curl https://api.stripe.com/v1/customers/cus_Ob4Xiw8KXOqcvM/cash_balance \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "settings[reconciliation_mode]"=manual
```

```cli
stripe cash_balances update cus_Ob4Xiw8KXOqcvM \
  -d "settings[reconciliation_mode]"=manual
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

cash_balance = client.v1.customers.cash_balance.update(
  'cus_Ob4Xiw8KXOqcvM',
  {settings: {reconciliation_mode: 'manual'}},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

cash_balance = client.v1.customers.cash_balance.update(
  "cus_Ob4Xiw8KXOqcvM",
  {"settings": {"reconciliation_mode": "manual"}},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$cashBalance = $stripe->customers->updateCashBalance(
  'cus_Ob4Xiw8KXOqcvM',
  ['settings' => ['reconciliation_mode' => 'manual']]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CustomerCashBalanceUpdateParams params =
  CustomerCashBalanceUpdateParams.builder()
    .setSettings(
      CustomerCashBalanceUpdateParams.Settings.builder()
        .setReconciliationMode(
          CustomerCashBalanceUpdateParams.Settings.ReconciliationMode.MANUAL
        )
        .build()
    )
    .build();

CashBalance cashBalance =
  client.v1().customers().cashBalance().update("cus_Ob4Xiw8KXOqcvM", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const cashBalance = await stripe.customers.updateCashBalance(
  'cus_Ob4Xiw8KXOqcvM',
  {
    settings: {
      reconciliation_mode: 'manual',
    },
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CashBalanceUpdateParams{
  Settings: &stripe.CashBalanceUpdateSettingsParams{
    ReconciliationMode: stripe.String(stripe.CashBalanceSettingsReconciliationModeManual),
  },
  Customer: stripe.String("cus_Ob4Xiw8KXOqcvM"),
}
result, err := sc.V1CashBalances.Update(context.TODO(), params)
```

```dotnet
var options = new CustomerCashBalanceUpdateOptions
{
    Settings = new CustomerCashBalanceSettingsOptions
    {
        ReconciliationMode = "manual",
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Customers.CashBalance;
CashBalance cashBalance = service.Update("cus_Ob4Xiw8KXOqcvM", options);
```

### Response

```json
{
  "object": "cash_balance",
  "available": null,
  "customer": "cus_Ob4Xiw8KXOqcvM",
  "livemode": false,
  "settings": {
    "reconciliation_mode": "manual",
    "using_merchant_default": false
  }
}
```