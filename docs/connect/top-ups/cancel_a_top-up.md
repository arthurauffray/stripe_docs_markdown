# Cancel a top-up

Cancels a top-up. Only pending top-ups can be canceled.

## Returns

Returns the canceled top-up. If the top-up is already canceled or can’t be canceled, an error is returned.

```curl
curl -X POST https://api.stripe.com/v1/topups/tu_1NG6yj2eZvKYlo2C1FOBiHya/cancel \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe topups cancel tu_1NG6yj2eZvKYlo2C1FOBiHya
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

topup = client.v1.topups.cancel('tu_1NG6yj2eZvKYlo2C1FOBiHya')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

topup = client.v1.topups.cancel("tu_1NG6yj2eZvKYlo2C1FOBiHya")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$topup = $stripe->topups->cancel('tu_1NG6yj2eZvKYlo2C1FOBiHya', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TopupCancelParams params = TopupCancelParams.builder().build();

Topup topup = client.v1().topups().cancel("tu_1NG6yj2eZvKYlo2C1FOBiHya", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const topup = await stripe.topups.cancel('tu_1NG6yj2eZvKYlo2C1FOBiHya');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TopupCancelParams{}
result, err := sc.V1Topups.Cancel(
  context.TODO(), "tu_1NG6yj2eZvKYlo2C1FOBiHya", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Topups;
Topup topup = service.Cancel("tu_1NG6yj2eZvKYlo2C1FOBiHya");
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
  "status": "canceled",
  "transfer_group": null
}
```