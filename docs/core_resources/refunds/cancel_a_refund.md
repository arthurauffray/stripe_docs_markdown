# Cancel a refund

Cancels a refund with a status of `requires_action`.

You can’t cancel refunds in other states. Only refunds for payment methods that require customer action can enter the `requires_action` state.

## Returns

Returns the refund object if the cancellation succeeds. This call raises [an error](https://docs.stripe.com/api/refunds/cancel.md#errors) if you can’t cancel the refund.

```curl
curl -X POST https://api.stripe.com/v1/refunds/re_1Nispe2eZvKYlo2Cd31jOCgZ/cancel \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe refunds cancel re_1Nispe2eZvKYlo2Cd31jOCgZ
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

refund = client.v1.refunds.cancel('re_1Nispe2eZvKYlo2Cd31jOCgZ')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

refund = client.v1.refunds.cancel("re_1Nispe2eZvKYlo2Cd31jOCgZ")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$refund = $stripe->refunds->cancel('re_1Nispe2eZvKYlo2Cd31jOCgZ', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

RefundCancelParams params = RefundCancelParams.builder().build();

Refund refund = client.v1().refunds().cancel("re_1Nispe2eZvKYlo2Cd31jOCgZ", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const refund = await stripe.refunds.cancel('re_1Nispe2eZvKYlo2Cd31jOCgZ');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.RefundCancelParams{}
result, err := sc.V1Refunds.Cancel(
  context.TODO(), "re_1Nispe2eZvKYlo2Cd31jOCgZ", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Refunds;
Refund refund = service.Cancel("re_1Nispe2eZvKYlo2Cd31jOCgZ");
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
  "failure_balance_transaction": "txn_3MmlLrLkdIwHu7ix0uke3Ezy",
  "failure_reason": "merchant_request",
  "metadata": {},
  "payment_intent": "pi_1GszsK2eZvKYlo2CfhZyoZLp",
  "reason": null,
  "receipt_number": null,
  "source_transfer_reversal": null,
  "status": "canceled",
  "transfer_reversal": null
}
```