# Report payment attempt failed

Report that the most recent payment attempt on the specified Payment Record failed or errored.

## Returns

The updated payment record object with its most recent payment attempt failed, or an error (for example, if the latest Payment Attempt Record is already guaranteed).

## Parameters

- `failed_at` (timestamp, required)
  When the reported payment failed. Measured in seconds since the Unix epoch.

- `id` (string, required)
  The ID of the Payment Record.

```curl
curl https://api.stripe.com/v1/payment_records/pr_5RV730PrHyAEi/report_payment_attempt_failed \
  -u "<<YOUR_SECRET_KEY>>" \
  -d failed_at=1730253453
```

```cli
stripe payment_records report_payment_attempt_failed pr_5RV730PrHyAEi \
  --failed-at=1730253453
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

payment_record = client.v1.payment_records.report_payment_attempt_failed(
  'pr_5RV730PrHyAEi',
  {failed_at: 1730253453},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

payment_record = client.v1.payment_records.report_payment_attempt_failed(
  "pr_5RV730PrHyAEi",
  {"failed_at": 1730253453},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentRecord = $stripe->paymentRecords->reportPaymentAttemptFailed(
  'pr_5RV730PrHyAEi',
  ['failed_at' => 1730253453]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PaymentRecordReportPaymentAttemptFailedParams params =
  PaymentRecordReportPaymentAttemptFailedParams.builder()
    .setFailedAt(1730253453L)
    .build();

PaymentRecord paymentRecord =
  client.v1().paymentRecords().reportPaymentAttemptFailed(
    "pr_5RV730PrHyAEi",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentRecord = await stripe.paymentRecords.reportPaymentAttemptFailed(
  'pr_5RV730PrHyAEi',
  {
    failed_at: 1730253453,
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PaymentRecordReportPaymentAttemptFailedParams{
  FailedAt: stripe.Int64(1730253453),
}
result, err := sc.V1PaymentRecords.ReportPaymentAttemptFailed(
  context.TODO(), "pr_5RV730PrHyAEi", params)
```

```dotnet
var options = new PaymentRecordReportPaymentAttemptFailedOptions
{
    FailedAt = DateTimeOffset.FromUnixTimeSeconds(1730253453).UtcDateTime,
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.PaymentRecords;
PaymentRecord paymentRecord = service.ReportPaymentAttemptFailed(
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
    "value": 1000
  },
  "amount_guaranteed": {
    "currency": "usd",
    "value": 0
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