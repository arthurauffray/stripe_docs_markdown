# Report a payment

Report a new Payment Record. You may report a Payment Record as it is initialized and later report updates through the other report_* methods, or report Payment Records in a terminal state directly, through this method.

## Returns

The newly created Payment Record.

## Parameters

- `amount_requested` (object, required)
  The amount you initially requested for this payment.

  - `amount_requested.currency` (enum, required)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `amount_requested.value` (integer, required)
    A positive integer representing the amount in the currency’s [minor unit](https://docs.stripe.com/docs/currencies.md#zero-decimal). For example, `100` can represent 1 USD or 100 JPY.

- `initiated_at` (timestamp, required)
  When the reported payment was initiated. Measured in seconds since the Unix epoch.

- `payment_method_details` (object, required)
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

- `customer_details` (object, optional)
  Customer information for this payment.

  - `customer_details.customer` (string, optional)
    The customer who made the payment.

  - `customer_details.email` (string, optional)
    The customer’s phone number.

    The maximum length is 800 characters.

  - `customer_details.name` (string, optional)
    The customer’s name.

  - `customer_details.phone` (string, optional)
    The customer’s phone number.

- `customer_presence` (enum, optional)
  Indicates whether the customer was present in your checkout flow during this payment.
Possible enum values:
  - `off_session`
    The customer was not present during the transaction.

  - `on_session`
    The customer was present during the transaction.

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

- `processor_details` (object, required)
  Processor information for this payment.

  - `processor_details.type` (enum, required)
    The type of the processor details. An additional hash is included on processor_details with a name matching this value. It contains additional information specific to the processor.
Possible enum values:
    - `custom`
      A custom payment processor that is not included in Stripe’s standard processor types. This allows you to report payments processed through external payment processors or custom integrations.

  - `processor_details.custom` (object, optional)
    Information about the custom processor used to make this payment.

    - `processor_details.custom.payment_reference` (string, required)
      An opaque string for manual reconciliation of this payment, for example a check number or a payment processor ID.

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
curl https://api.stripe.com/v1/payment_records/report_payment \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "amount_requested[currency]"=usd \
  -d "amount_requested[value]"=1000 \
  -d customer_presence=on_session \
  -d description="computer software" \
  -d initiated_at=1730253453 \
  -d "payment_method_details[custom][display_name]"=newpay \
  -d "payment_method_details[custom][type]"=cpmt_125kjj3hn3sdf \
  -d "payment_method_details[payment_method]"=pm_5j23kjksibjlks \
  -d "payment_method_details[type]"=custom
```

```cli
stripe payment_records report_payment  \
  -d "amount_requested[currency]"=usd \
  -d "amount_requested[value]"=1000 \
  --customer-presence=on_session \
  --description="computer software" \
  --initiated-at=1730253453 \
  -d "payment_method_details[custom][display_name]"=newpay \
  -d "payment_method_details[custom][type]"=cpmt_125kjj3hn3sdf \
  -d "payment_method_details[payment_method]"=pm_5j23kjksibjlks \
  -d "payment_method_details[type]"=custom
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

payment_record = client.v1.payment_records.report_payment({
  amount_requested: {
    currency: 'usd',
    value: 1000,
  },
  customer_presence: 'on_session',
  description: 'computer software',
  initiated_at: 1730253453,
  payment_method_details: {
    custom: {
      display_name: 'newpay',
      type: 'cpmt_125kjj3hn3sdf',
    },
    payment_method: 'pm_5j23kjksibjlks',
    type: 'custom',
  },
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

payment_record = client.v1.payment_records.report_payment({
  "amount_requested": {"currency": "usd", "value": 1000},
  "customer_presence": "on_session",
  "description": "computer software",
  "initiated_at": 1730253453,
  "payment_method_details": {
    "custom": {"display_name": "newpay", "type": "cpmt_125kjj3hn3sdf"},
    "payment_method": "pm_5j23kjksibjlks",
    "type": "custom",
  },
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentRecord = $stripe->paymentRecords->reportPayment([
  'amount_requested' => [
    'currency' => 'usd',
    'value' => 1000,
  ],
  'customer_presence' => 'on_session',
  'description' => 'computer software',
  'initiated_at' => 1730253453,
  'payment_method_details' => [
    'custom' => [
      'display_name' => 'newpay',
      'type' => 'cpmt_125kjj3hn3sdf',
    ],
    'payment_method' => 'pm_5j23kjksibjlks',
    'type' => 'custom',
  ],
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PaymentRecordReportPaymentParams params =
  PaymentRecordReportPaymentParams.builder()
    .setAmountRequested(
      PaymentRecordReportPaymentParams.AmountRequested.builder()
        .setCurrency("usd")
        .setValue(1000L)
        .build()
    )
    .setCustomerPresence(
      PaymentRecordReportPaymentParams.CustomerPresence.ON_SESSION
    )
    .setDescription("computer software")
    .setInitiatedAt(1730253453L)
    .setPaymentMethodDetails(
      PaymentRecordReportPaymentParams.PaymentMethodDetails.builder()
        .setCustom(
          PaymentRecordReportPaymentParams.PaymentMethodDetails.Custom.builder()
            .setDisplayName("newpay")
            .setType("cpmt_125kjj3hn3sdf")
            .build()
        )
        .setPaymentMethod("pm_5j23kjksibjlks")
        .setType(PaymentRecordReportPaymentParams.PaymentMethodDetails.Type.CUSTOM)
        .build()
    )
    .build();

PaymentRecord paymentRecord = client.v1().paymentRecords().reportPayment(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentRecord = await stripe.paymentRecords.reportPayment({
  amount_requested: {
    currency: 'usd',
    value: 1000,
  },
  customer_presence: 'on_session',
  description: 'computer software',
  initiated_at: 1730253453,
  payment_method_details: {
    custom: {
      display_name: 'newpay',
      type: 'cpmt_125kjj3hn3sdf',
    },
    payment_method: 'pm_5j23kjksibjlks',
    type: 'custom',
  },
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PaymentRecordReportPaymentParams{
  AmountRequested: &stripe.PaymentRecordReportPaymentAmountRequestedParams{
    Currency: stripe.String(stripe.CurrencyUSD),
    Value: stripe.Int64(1000),
  },
  CustomerPresence: stripe.String(stripe.PaymentRecordCustomerPresenceOnSession),
  Description: stripe.String("computer software"),
  InitiatedAt: stripe.Int64(1730253453),
  PaymentMethodDetails: &stripe.PaymentRecordReportPaymentPaymentMethodDetailsParams{
    Custom: &stripe.PaymentRecordReportPaymentPaymentMethodDetailsCustomParams{
      DisplayName: stripe.String("newpay"),
      Type: stripe.String("cpmt_125kjj3hn3sdf"),
    },
    PaymentMethod: stripe.String("pm_5j23kjksibjlks"),
    Type: stripe.String("custom"),
  },
}
result, err := sc.V1PaymentRecords.ReportPayment(context.TODO(), params)
```

```dotnet
var options = new PaymentRecordReportPaymentOptions
{
    AmountRequested = new PaymentRecordAmountRequestedOptions
    {
        Currency = "usd",
        Value = 1000,
    },
    CustomerPresence = "on_session",
    Description = "computer software",
    InitiatedAt = DateTimeOffset.FromUnixTimeSeconds(1730253453).UtcDateTime,
    PaymentMethodDetails = new PaymentRecordPaymentMethodDetailsOptions
    {
        Custom = new PaymentRecordPaymentMethodDetailsCustomOptions
        {
            DisplayName = "newpay",
            Type = "cpmt_125kjj3hn3sdf",
        },
        PaymentMethod = "pm_5j23kjksibjlks",
        Type = "custom",
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.PaymentRecords;
PaymentRecord paymentRecord = service.ReportPayment(options);
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