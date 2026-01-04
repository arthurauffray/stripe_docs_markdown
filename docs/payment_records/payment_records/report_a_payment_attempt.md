# Report a payment attempt

Report a new payment attempt on the specified Payment Record. A new payment attempt can only be specified if all other payment attempts are canceled or failed.

## Returns

The updated Payment Record object with a new latest_payment_attempt_record, or an error (for example, if the Payment Record already has funds guaranteed).

## Parameters

- `id` (string, required)
  The ID of the Payment Record.

- `initiated_at` (timestamp, required)
  When the reported payment was initiated. Measured in seconds since the Unix epoch.

- `description` (string, optional)
  An arbitrary string attached to the object. Often useful for displaying to users.

- `failed` (object, optional)
  Information about the payment attempt failure.

  - `failed.failed_at` (timestamp, required)
    When the reported payment failed. Measured in seconds since the Unix epoch.

- `guaranteed` (object, optional)
  Information about the payment attempt guarantee.

  - `guaranteed.guaranteed_at` (timestamp, required)
    When the reported payment was guaranteed. Measured in seconds since the Unix epoch.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `outcome` (enum, optional)
  The outcome of the reported payment.
Possible enum values:
  - `failed`
    The payment failed.

  - `guaranteed`
    The payment was guaranteed.

- `payment_method_details` (object, optional)
  Information about the Payment Method debited for this payment.

  - `payment_method_details.billing_details` (object, optional)
    The billing details associated with the method of payment.

    - `payment_method_details.billing_details.address` (object, optional)
      The billing address associated with the method of payment.

      - `payment_method_details.billing_details.address.city` (string, optional)
        City, district, suburb, town, or village.

      - `payment_method_details.billing_details.address.country` (string, optional)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `payment_method_details.billing_details.address.line1` (string, optional)
        Address line 1, such as the street, PO Box, or company name.

      - `payment_method_details.billing_details.address.line2` (string, optional)
        Address line 2, such as the apartment, suite, unit, or building.

      - `payment_method_details.billing_details.address.postal_code` (string, optional)
        ZIP or postal code.

      - `payment_method_details.billing_details.address.state` (string, optional)
        State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

    - `payment_method_details.billing_details.email` (string, optional)
      The billing email associated with the method of payment.

      The maximum length is 800 characters.

    - `payment_method_details.billing_details.name` (string, optional)
      The billing name associated with the method of payment.

    - `payment_method_details.billing_details.phone` (string, optional)
      The billing phone number associated with the method of payment.

  - `payment_method_details.custom` (object, optional)
    Information about the custom (user-defined) payment method used to make this payment.

    - `payment_method_details.custom.display_name` (string, optional)
      Display name for the custom (user-defined) payment method type used to make this payment.

    - `payment_method_details.custom.type` (string, optional)
      The custom payment method type associated with this payment.

  - `payment_method_details.payment_method` (string, required unless type is provided)
    ID of the Stripe Payment Method used to make this payment.

  - `payment_method_details.type` (enum, required unless payment_method is provided)
    The type of the payment method details. An additional hash is included on the payment_method_details with a name matching this value. It contains additional information specific to the type.
Possible enum values:
    - `custom`
      A custom payment method that is not included in Stripe’s standard payment method types. This allows you to report payments processed through external payment processors or custom integrations.

- `shipping_details` (object, optional)
  Shipping information for this payment.

  - `shipping_details.address` (object, optional)
    The physical shipping address.

    - `shipping_details.address.city` (string, optional)
      City, district, suburb, town, or village.

    - `shipping_details.address.country` (string, optional)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `shipping_details.address.line1` (string, optional)
      Address line 1, such as the street, PO Box, or company name.

    - `shipping_details.address.line2` (string, optional)
      Address line 2, such as the apartment, suite, unit, or building.

    - `shipping_details.address.postal_code` (string, optional)
      ZIP or postal code.

    - `shipping_details.address.state` (string, optional)
      State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

  - `shipping_details.name` (string, optional)
    The shipping recipient’s name.

  - `shipping_details.phone` (string, optional)
    The shipping recipient’s phone number.

```curl
curl https://api.stripe.com/v1/payment_records/pr_5RV730PrHyAEi/report_payment_attempt \
  -u "<<YOUR_SECRET_KEY>>" \
  -d initiated_at=1730253425
```

```cli
stripe payment_records report_payment_attempt pr_5RV730PrHyAEi \
  --initiated-at=1730253425
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

payment_record = client.v1.payment_records.report_payment_attempt(
  'pr_5RV730PrHyAEi',
  {initiated_at: 1730253425},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

payment_record = client.v1.payment_records.report_payment_attempt(
  "pr_5RV730PrHyAEi",
  {"initiated_at": 1730253425},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentRecord = $stripe->paymentRecords->reportPaymentAttempt(
  'pr_5RV730PrHyAEi',
  ['initiated_at' => 1730253425]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PaymentRecordReportPaymentAttemptParams params =
  PaymentRecordReportPaymentAttemptParams.builder()
    .setInitiatedAt(1730253425L)
    .build();

PaymentRecord paymentRecord =
  client.v1().paymentRecords().reportPaymentAttempt("pr_5RV730PrHyAEi", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentRecord = await stripe.paymentRecords.reportPaymentAttempt(
  'pr_5RV730PrHyAEi',
  {
    initiated_at: 1730253425,
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PaymentRecordReportPaymentAttemptParams{
  InitiatedAt: stripe.Int64(1730253425),
}
result, err := sc.V1PaymentRecords.ReportPaymentAttempt(
  context.TODO(), "pr_5RV730PrHyAEi", params)
```

```dotnet
var options = new PaymentRecordReportPaymentAttemptOptions
{
    InitiatedAt = DateTimeOffset.FromUnixTimeSeconds(1730253425).UtcDateTime,
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.PaymentRecords;
PaymentRecord paymentRecord = service.ReportPaymentAttempt(
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
  "latest_payment_attempt_record": "par_345kjsi8WE",
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