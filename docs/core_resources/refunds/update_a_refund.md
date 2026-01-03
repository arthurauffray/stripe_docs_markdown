# Update a refund

Updates the refund that you specify by setting the values of the passed parameters. Any parameters that you don’t provide remain unchanged.

This request only accepts `metadata` as an argument.

## Returns

Returns the refund object if the update succeeds. This call raises [an error](https://docs.stripe.com/api/refunds/update.md#errors) if update parameters are invalid.

## Parameters

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/refunds/re_1Nispe2eZvKYlo2Cd31jOCgZ \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
```

```cli
stripe refunds update re_1Nispe2eZvKYlo2Cd31jOCgZ \
  -d "metadata[order_id]"=6735
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

refund = client.v1.refunds.update(
  're_1Nispe2eZvKYlo2Cd31jOCgZ',
  {metadata: {order_id: '6735'}},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

refund = client.v1.refunds.update(
  "re_1Nispe2eZvKYlo2Cd31jOCgZ",
  {"metadata": {"order_id": "6735"}},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$refund = $stripe->refunds->update(
  're_1Nispe2eZvKYlo2Cd31jOCgZ',
  ['metadata' => ['order_id' => '6735']]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

RefundUpdateParams params =
  RefundUpdateParams.builder().putMetadata("order_id", "6735").build();

Refund refund = client.v1().refunds().update("re_1Nispe2eZvKYlo2Cd31jOCgZ", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const refund = await stripe.refunds.update(
  're_1Nispe2eZvKYlo2Cd31jOCgZ',
  {
    metadata: {
      order_id: '6735',
    },
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.RefundUpdateParams{}
params.AddMetadata("order_id", "6735")
result, err := sc.V1Refunds.Update(
  context.TODO(), "re_1Nispe2eZvKYlo2Cd31jOCgZ", params)
```

```dotnet
var options = new RefundUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Refunds;
Refund refund = service.Update("re_1Nispe2eZvKYlo2Cd31jOCgZ", options);
```

### Response

```json
{
  "id": "re_1Nispe2eZvKYlo2Cd31jOCgZ",
  "object": "refund",
  "amount": 1000,
  "balance_transaction": "txn_1Nispe2eZvKYlo2CYezqFhEx",
  "charge": "ch_1NirD82eZvKYlo2CIvbtLWuY",
  "created": 1692942318,
  "currency": "usd",
  "destination_details": {
    "card": {
      "reference": "123456789012",
      "reference_status": "available",
      "reference_type": "acquirer_reference_number",
      "type": "refund"
    },
    "type": "card"
  },
  "metadata": {
    "order_id": "6735"
  },
  "payment_intent": "pi_1GszsK2eZvKYlo2CfhZyoZLp",
  "reason": null,
  "receipt_number": null,
  "source_transfer_reversal": null,
  "status": "succeeded",
  "transfer_reversal": null
}
```