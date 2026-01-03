# Retrieve a refund

Retrieves the details of an existing refund.

## Returns

Returns a refund if you provide a valid ID. Raises [an error](https://docs.stripe.com/api/refunds/retrieve.md#errors) otherwise.

```curl
curl https://api.stripe.com/v1/refunds/re_1Nispe2eZvKYlo2Cd31jOCgZ \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe refunds retrieve re_1Nispe2eZvKYlo2Cd31jOCgZ
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

refund = client.v1.refunds.retrieve('re_1Nispe2eZvKYlo2Cd31jOCgZ')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

refund = client.v1.refunds.retrieve("re_1Nispe2eZvKYlo2Cd31jOCgZ")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$refund = $stripe->refunds->retrieve('re_1Nispe2eZvKYlo2Cd31jOCgZ', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

RefundRetrieveParams params = RefundRetrieveParams.builder().build();

Refund refund =
  client.v1().refunds().retrieve("re_1Nispe2eZvKYlo2Cd31jOCgZ", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const refund = await stripe.refunds.retrieve('re_1Nispe2eZvKYlo2Cd31jOCgZ');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.RefundRetrieveParams{}
result, err := sc.V1Refunds.Retrieve(
  context.TODO(), "re_1Nispe2eZvKYlo2Cd31jOCgZ", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Refunds;
Refund refund = service.Get("re_1Nispe2eZvKYlo2Cd31jOCgZ");
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
  "metadata": {},
  "payment_intent": "pi_1GszsK2eZvKYlo2CfhZyoZLp",
  "reason": null,
  "receipt_number": null,
  "source_transfer_reversal": null,
  "status": "succeeded",
  "transfer_reversal": null
}
```