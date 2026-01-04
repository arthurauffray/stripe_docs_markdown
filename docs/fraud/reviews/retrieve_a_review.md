# Retrieve a review

Retrieves a `Review` object.

## Returns

Returns a `Review` object if a valid identifier was provided.

```curl
curl https://api.stripe.com/v1/reviews/prv_1NVyFt2eZvKYlo2CjubqF1xm \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe reviews retrieve prv_1NVyFt2eZvKYlo2CjubqF1xm
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

review = client.v1.reviews.retrieve('prv_1NVyFt2eZvKYlo2CjubqF1xm')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

review = client.v1.reviews.retrieve("prv_1NVyFt2eZvKYlo2CjubqF1xm")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$review = $stripe->reviews->retrieve('prv_1NVyFt2eZvKYlo2CjubqF1xm', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ReviewRetrieveParams params = ReviewRetrieveParams.builder().build();

Review review =
  client.v1().reviews().retrieve("prv_1NVyFt2eZvKYlo2CjubqF1xm", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const review = await stripe.reviews.retrieve('prv_1NVyFt2eZvKYlo2CjubqF1xm');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.ReviewRetrieveParams{}
result, err := sc.V1Reviews.Retrieve(
  context.TODO(), "prv_1NVyFt2eZvKYlo2CjubqF1xm", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Reviews;
Review review = service.Get("prv_1NVyFt2eZvKYlo2CjubqF1xm");
```

### Response

```json
{
  "id": "prv_1NVyFt2eZvKYlo2CjubqF1xm",
  "object": "review",
  "billing_zip": null,
  "charge": null,
  "closed_reason": null,
  "created": 1689864901,
  "ip_address": null,
  "ip_address_location": null,
  "livemode": false,
  "open": true,
  "opened_reason": "rule",
  "payment_intent": "pi_3NVy8c2eZvKYlo2C055h7pkd",
  "reason": "rule",
  "session": null
}
```