# List Payment Attempt Records

List all the Payment Attempt Records attached to the specified Payment Record.

## Returns

A dictionary with a data property that contains an array of Payment Attempt Records.

## Parameters

- `payment_record` (string, required)
  The ID of the Payment Record.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/payment_attempt_records \
  -u "<<YOUR_SECRET_KEY>>" \
  -d payment_record=pr_5RV730PrHyAEi
```

```cli
stripe payment_attempt_records list  \
  --payment-record=pr_5RV730PrHyAEi
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

payment_attempt_records = client.v1.payment_attempt_records.list({
  payment_record: 'pr_5RV730PrHyAEi',
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

payment_attempt_records = client.v1.payment_attempt_records.list({
  "payment_record": "pr_5RV730PrHyAEi",
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentAttemptRecords = $stripe->paymentAttemptRecords->all([
  'payment_record' => 'pr_5RV730PrHyAEi',
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PaymentAttemptRecordListParams params =
  PaymentAttemptRecordListParams.builder()
    .setPaymentRecord("pr_5RV730PrHyAEi")
    .build();

StripeCollection<PaymentAttemptRecord> stripeCollection =
  client.v1().paymentAttemptRecords().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentAttemptRecords = await stripe.paymentAttemptRecords.list({
  payment_record: 'pr_5RV730PrHyAEi',
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PaymentAttemptRecordListParams{
  PaymentRecord: stripe.String("pr_5RV730PrHyAEi"),
}
result := sc.V1PaymentAttemptRecords.List(context.TODO(), params)
```

```dotnet
var options = new PaymentAttemptRecordListOptions
{
    PaymentRecord = "pr_5RV730PrHyAEi",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.PaymentAttemptRecords;
StripeList<PaymentAttemptRecord> paymentAttemptRecords = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/payment_attempt_records",
  "has_more": false,
  "data": [
    {
      "id": "par_4sdDKj23235s",
      "object": "payment_attempt_record",
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
      "payment_record": "pr_5RV730PrHyAEi",
      "processor_details": {
        "type": "custom",
        "custom": {
          "payment_reference": "npp2358872734k"
        }
      },
      "shipping_details": null
    }
  ]
}
```