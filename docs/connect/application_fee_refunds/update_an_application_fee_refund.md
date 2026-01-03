# Update an application fee refund

Updates the specified application fee refund by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

This request only accepts metadata as an argument.

## Returns

Returns the application fee refund object if the update succeeded. This call will raise [an error](https://docs.stripe.com/api/fee_refunds/update.md#errors) if update parameters are invalid.

## Parameters

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/application_fees/fee_1B73DOKbnvuxQXGuhY8Aw0TN/refunds/fr_1MtJRpKbnvuxQXGuM6Ww0D24 \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
```

```cli
stripe fee_refunds update fee_1B73DOKbnvuxQXGuhY8Aw0TN fr_1MtJRpKbnvuxQXGuM6Ww0D24 \
  -d "metadata[order_id]"=6735
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

application_fee_refund = client.v1.application_fees.refunds.update(
  'fee_1B73DOKbnvuxQXGuhY8Aw0TN',
  'fr_1MtJRpKbnvuxQXGuM6Ww0D24',
  {metadata: {order_id: '6735'}},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

application_fee_refund = client.v1.application_fees.refunds.update(
  "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
  "fr_1MtJRpKbnvuxQXGuM6Ww0D24",
  {"metadata": {"order_id": "6735"}},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$applicationFeeRefund = $stripe->applicationFees->updateRefund(
  'fee_1B73DOKbnvuxQXGuhY8Aw0TN',
  'fr_1MtJRpKbnvuxQXGuM6Ww0D24',
  ['metadata' => ['order_id' => '6735']]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ApplicationFeeRefundUpdateParams params =
  ApplicationFeeRefundUpdateParams.builder().putMetadata("order_id", "6735").build();

FeeRefund feeRefund =
  client.v1().applicationFees().refunds().update(
    "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
    "fr_1MtJRpKbnvuxQXGuM6Ww0D24",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const feeRefund = await stripe.applicationFees.updateRefund(
  'fee_1B73DOKbnvuxQXGuhY8Aw0TN',
  'fr_1MtJRpKbnvuxQXGuM6Ww0D24',
  {
    metadata: {
      order_id: '6735',
    },
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.FeeRefundUpdateParams{
  Fee: stripe.String("fee_1B73DOKbnvuxQXGuhY8Aw0TN"),
}
params.AddMetadata("order_id", "6735")
result, err := sc.V1FeeRefunds.Update(
  context.TODO(), "fr_1MtJRpKbnvuxQXGuM6Ww0D24", params)
```

```dotnet
var options = new ApplicationFeeRefundUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.ApplicationFees.Refunds;
ApplicationFeeRefund applicationFeeRefund = service.Update(
    "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
    "fr_1MtJRpKbnvuxQXGuM6Ww0D24",
    options);
```

### Response

```json
{
  "id": "fr_1MtJRpKbnvuxQXGuM6Ww0D24",
  "object": "fee_refund",
  "amount": 100,
  "balance_transaction": null,
  "created": 1680651573,
  "currency": "usd",
  "fee": "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
  "metadata": {
    "order_id": "6735"
  }
}
```