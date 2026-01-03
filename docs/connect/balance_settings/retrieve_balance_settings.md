# Retrieve balance settings

Retrieves balance settings for a given connected account. Related guide: [Making API calls for connected accounts](https://docs.stripe.com/connect/authentication.md)

## Returns

Returns a balance settings object for the account specified in the request.

```curl
curl https://api.stripe.com/v1/balance_settings \
  -u "<<YOUR_SECRET_KEY>>" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"
```

```cli
stripe balance_settingss retrieve  \
  --stripe-account {{CONNECTED_ACCOUNT_ID}}
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

balance_settings = client.v1.balance_settings.retrieve(
  {},
  {stripe_account: '{{CONNECTED_ACCOUNT_ID}}'},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

balance_settings = client.v1.balance_settings.retrieve(
  options={"stripe_account": "{{CONNECTED_ACCOUNT_ID}}"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$balanceSettings = $stripe->balanceSettings->retrieve(
  [],
  ['stripe_account' => '{{CONNECTED_ACCOUNT_ID}}']
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

BalanceSettingsRetrieveParams params =
  BalanceSettingsRetrieveParams.builder().build();

RequestOptions requestOptions =
  RequestOptions.builder()
    .setStripeAccount("{{CONNECTED_ACCOUNT_ID}}")
    .build();

BalanceSettings balanceSettings =
  client.v1().balanceSettings().retrieve(params, requestOptions);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const balanceSettings = await stripe.balanceSettings.retrieve({
  stripeAccount: '{{CONNECTED_ACCOUNT_ID}}',
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.BalanceSettingsRetrieveParams{}
params.SetStripeAccount("{{CONNECTED_ACCOUNT_ID}}")
result, err := sc.V1BalanceSettings.Retrieve(context.TODO(), params)
```

```dotnet
var options = new BalanceSettingsGetOptions();
var requestOptions = new RequestOptions
{
    StripeAccount = "{{CONNECTED_ACCOUNT_ID}}",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.BalanceSettings;
BalanceSettings balanceSettings = service.Get(options, requestOptions);
```

### Response

```json
{
  "object": "balance_settings",
  "payments": {
    "debit_negative_balances": true,
    "payouts": {
      "minimum_balance_by_currency": {
        "usd": 1500,
        "cad": 8000
      },
      "schedule": {
        "interval": "weekly",
        "weekly_payout_days": [
          "monday",
          "wednesday"
        ]
      },
      "statement_descriptor": null,
      "status": "enabled"
    },
    "settlement_timing": {
      "delay_days_override": 3,
      "delay_days": 3
    }
  }
}
```