# Update a top-up

Updates the metadata of a top-up. Other top-up details are not editable by design.

## Returns

The newly updated top-up object if the call succeeded. Otherwise, this call raises [an error](https://docs.stripe.com/api/topups/update.md#errors).

## Parameters

- `description` (string, optional)
  An arbitrary string attached to the object. Often useful for displaying to users.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/topups/tu_1NG6yj2eZvKYlo2C1FOBiHya \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
```

```cli
stripe topups update tu_1NG6yj2eZvKYlo2C1FOBiHya \
  -d "metadata[order_id]"=6735
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

topup = client.v1.topups.update(
  'tu_1NG6yj2eZvKYlo2C1FOBiHya',
  {metadata: {order_id: '6735'}},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

topup = client.v1.topups.update(
  "tu_1NG6yj2eZvKYlo2C1FOBiHya",
  {"metadata": {"order_id": "6735"}},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$topup = $stripe->topups->update(
  'tu_1NG6yj2eZvKYlo2C1FOBiHya',
  ['metadata' => ['order_id' => '6735']]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TopupUpdateParams params =
  TopupUpdateParams.builder().putMetadata("order_id", "6735").build();

Topup topup = client.v1().topups().update("tu_1NG6yj2eZvKYlo2C1FOBiHya", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const topup = await stripe.topups.update(
  'tu_1NG6yj2eZvKYlo2C1FOBiHya',
  {
    metadata: {
      order_id: '6735',
    },
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TopupUpdateParams{}
params.AddMetadata("order_id", "6735")
result, err := sc.V1Topups.Update(
  context.TODO(), "tu_1NG6yj2eZvKYlo2C1FOBiHya", params)
```

```dotnet
var options = new TopupUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Topups;
Topup topup = service.Update("tu_1NG6yj2eZvKYlo2C1FOBiHya", options);
```

### Response

```json
{
  "id": "tu_1NG6yj2eZvKYlo2C1FOBiHya",
  "object": "topup",
  "amount": 2000,
  "balance_transaction": null,
  "created": 123456789,
  "currency": "usd",
  "description": "Top-up for Jenny Rosen",
  "expected_availability_date": 123456789,
  "failure_code": null,
  "failure_message": null,
  "livemode": false,
  "source": null,
  "statement_descriptor": "Top-up",
  "status": "pending",
  "transfer_group": null,
  "metadata": {
    "order_id": "6735"
  }
}
```