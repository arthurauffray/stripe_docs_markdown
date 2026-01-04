# Report payment attempt guaranteed

Report that the most recent payment attempt on the specified Payment Record was guaranteed.

## Returns

The updated Payment Record object with its most recent payment attempt guaranteed, or an error (for example, if the latest Payment Attempt Record is already guaranteed).

## Parameters

- `guaranteed_at` (timestamp, required)
  When the reported payment was guaranteed. Measured in seconds since the Unix epoch.

- `id` (string, required)
  The ID of the Payment Record.

```curl
curl https://api.stripe.com/v1/payment_records/pr_5RV730PrHyAEi/report_payment_attempt_guaranteed \
  -u "<<YOUR_SECRET_KEY>>" \
  -d guaranteed_at=1730253453
```

```cli
stripe payment_records report_payment_attempt_guaranteed pr_5RV730PrHyAEi \
  --guaranteed-at=1730253453
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

payment_record = client.v1.payment_records.report_payment_attempt_guaranteed(
  'pr_5RV730PrHyAEi',
  {guaranteed_at: 1730253453},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

payment_record = client.v1.payment_records.report_payment_attempt_guaranteed(
  "pr_5RV730PrHyAEi",
  {"guaranteed_at": 1730253453},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentRecord = $stripe->paymentRecords->reportPaymentAttemptGuaranteed(
  'pr_5RV730PrHyAEi',
  ['guaranteed_at' => 1730253453]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PaymentRecordReportPaymentAttemptGuaranteedParams params =
  PaymentRecordReportPaymentAttemptGuaranteedParams.builder()
    .setGuaranteedAt(1730253453L)
    .build();

PaymentRecord paymentRecord =
  client.v1().paymentRecords().reportPaymentAttemptGuaranteed(
    "pr_5RV730PrHyAEi",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentRecord = await stripe.paymentRecords.reportPaymentAttemptGuaranteed(
  'pr_5RV730PrHyAEi',
  {
    guaranteed_at: 1730253453,
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PaymentRecordReportPaymentAttemptGuaranteedParams{
  GuaranteedAt: stripe.Int64(1730253453),
}
result, err := sc.V1PaymentRecords.ReportPaymentAttemptGuaranteed(
  context.TODO(), "pr_5RV730PrHyAEi", params)
```

```dotnet
var options = new PaymentRecordReportPaymentAttemptGuaranteedOptions
{
    GuaranteedAt = DateTimeOffset.FromUnixTimeSeconds(1730253453).UtcDateTime,
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.PaymentRecords;
PaymentRecord paymentRecord = service.ReportPaymentAttemptGuaranteed(
    "pr_5RV730PrHyAEi",
    options);
```

### Response

```json
{
  "id": "pr_5RV730PrHyAEi",
  "object": "payment_record",
  "amount_canceled": {
    "currency": "usd",
    "value": 0
  },
  "amount_failed": {
    "currency": "usd",
    "value": 0
  },
  "amount_guaranteed": {
    "currency": "usd",
    "value": 1000
  },
  "amount_refunded": {
    "currency": "usd",
    "value": 0
  },
  "amount_requested": {
    "currency": "usd",
    "value": 1000
  },
  "created": 1730211363,
  "customer_details": null,
  "customer_presence": "on_session",
  "description": "computer software",
  "latest_payment_attempt_record": "par_1ArV730PrHyQuG",
  "livemode": true,
  "metadata": {},
  "payment_method_details": {
    "billing_details": null,
    "custom": {
      "display_name": "newpay",
      "type": "cpmt_125kjj3hn3sdf"
    },
    "payment_method": "pm_5j23kjksibjlks",
    "type": "custom"
  },
  "processor_details": {
    "type": "custom",
    "custom": {
      "payment_reference": "npp2358872734k"
    }
  },
  "shipping_details": null
}
```