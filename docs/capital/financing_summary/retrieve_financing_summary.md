# Retrieve financing summary

Retrieve the financing summary object for the account.

## Returns

Returns a financing summary object for the account.

```curl
curl https://api.stripe.com/v1/capital/financing_summary \
  -u "<<YOUR_SECRET_KEY>>" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"
```

```cli
stripe capital financing_summarys retrieve  \
  --stripe-account {{CONNECTED_ACCOUNT_ID}}
```

```ruby
# This example uses the beta SDK. See https://github.com/stripe/stripe-ruby#public-preview-sdks
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

financing_summary = client.v1.capital.financing_summary.retrieve(
  {},
  {stripe_account: '{{CONNECTED_ACCOUNT_ID}}'},
)
```

```python
# This example uses the beta SDK. See https://github.com/stripe/stripe-python#public-preview-sdks
client = StripeClient("<<YOUR_SECRET_KEY>>")

financing_summary = client.v1.capital.financing_summary.retrieve(
  options={"stripe_account": "{{CONNECTED_ACCOUNT_ID}}"},
)
```

```php
// This example uses the beta SDK. See https://github.com/stripe/stripe-php#public-preview-sdks
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$financingSummary = $stripe->capital->financingSummary->retrieve(
  [],
  ['stripe_account' => '{{CONNECTED_ACCOUNT_ID}}']
);
```

```java
// This example uses the beta SDK. See https://github.com/stripe/stripe-java#public-preview-sdks
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

FinancingSummaryRetrieveParams params =
  FinancingSummaryRetrieveParams.builder().build();

RequestOptions requestOptions =
  RequestOptions.builder()
    .setStripeAccount("{{CONNECTED_ACCOUNT_ID}}")
    .build();

FinancingSummary financingSummary =
  client.v1().capital().financingSummary().retrieve(params, requestOptions);
```

```node
// This example uses the beta SDK. See https://github.com/stripe/stripe-node#public-preview-sdks
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const financingSummary = await stripe.capital.financingSummary.retrieve({
  stripeAccount: '{{CONNECTED_ACCOUNT_ID}}',
});
```

```go
// This example uses the beta SDK. See https://github.com/stripe/stripe-go#public-preview-sdks
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CapitalFinancingSummaryRetrieveParams{}
params.SetStripeAccount("{{CONNECTED_ACCOUNT_ID}}")
result, err := sc.V1CapitalFinancingSummary.Retrieve(context.TODO(), params)
```

```dotnet
// This example uses the beta SDK. See https://github.com/stripe/stripe-dotnet#public-preview-sdks
var options = new Stripe.Capital.FinancingSummaryGetOptions();
var requestOptions = new RequestOptions
{
    StripeAccount = "{{CONNECTED_ACCOUNT_ID}}",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Capital.FinancingSummary;
Stripe.Capital.FinancingSummary financingSummary = service.Get(
    options,
    requestOptions);
```

### Response

```json
{
  "object": "capital.financing_summary",
  "details": {
    "advance_amount": 100000,
    "advance_paid_out_at": 1688424277.0578003,
    "currency": "usd",
    "current_repayment_interval": null,
    "fee_amount": 10000,
    "paid_amount": 100263,
    "remaining_amount": 9737,
    "repayments_begin_at": 1688424277.0577993,
    "withhold_rate": 0.05
  },
  "financing_offer": "financingoffer_1NPvU12eZvKYlo2CotjdGRzu",
  "status": "accepted"
}
```