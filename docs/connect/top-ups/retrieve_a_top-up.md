# Retrieve a top-up

Retrieves the details of a top-up that has previously been created. Supply the unique top-up ID that was returned from your previous request, and Stripe will return the corresponding top-up information.

## Returns

Returns a top-up if a valid identifier was provided, and raises [an error](https://docs.stripe.com/api/topups/retrieve.md#errors) otherwise.

```curl
curl https://api.stripe.com/v1/topups/tu_1NG6yj2eZvKYlo2C1FOBiHya \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe topups retrieve tu_1NG6yj2eZvKYlo2C1FOBiHya
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

topup = client.v1.topups.retrieve('tu_1NG6yj2eZvKYlo2C1FOBiHya')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

topup = client.v1.topups.retrieve("tu_1NG6yj2eZvKYlo2C1FOBiHya")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$topup = $stripe->topups->retrieve('tu_1NG6yj2eZvKYlo2C1FOBiHya', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TopupRetrieveParams params = TopupRetrieveParams.builder().build();

Topup topup = client.v1().topups().retrieve("tu_1NG6yj2eZvKYlo2C1FOBiHya", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const topup = await stripe.topups.retrieve('tu_1NG6yj2eZvKYlo2C1FOBiHya');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TopupRetrieveParams{}
result, err := sc.V1Topups.Retrieve(
  context.TODO(), "tu_1NG6yj2eZvKYlo2C1FOBiHya", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Topups;
Topup topup = service.Get("tu_1NG6yj2eZvKYlo2C1FOBiHya");
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
  "transfer_group": null
}
```