# Retrieve a Mandate

Retrieves a Mandate object.

## Returns

Returns a Mandate object.

```curl
curl https://api.stripe.com/v1/mandates/mandate_1MvojA2eZvKYlo2CvqTABjZs \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe mandates retrieve mandate_1MvojA2eZvKYlo2CvqTABjZs
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

mandate = client.v1.mandates.retrieve('mandate_1MvojA2eZvKYlo2CvqTABjZs')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

mandate = client.v1.mandates.retrieve("mandate_1MvojA2eZvKYlo2CvqTABjZs")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$mandate = $stripe->mandates->retrieve('mandate_1MvojA2eZvKYlo2CvqTABjZs', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

MandateRetrieveParams params = MandateRetrieveParams.builder().build();

Mandate mandate =
  client.v1().mandates().retrieve("mandate_1MvojA2eZvKYlo2CvqTABjZs", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const mandate = await stripe.mandates.retrieve('mandate_1MvojA2eZvKYlo2CvqTABjZs');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.MandateRetrieveParams{}
result, err := sc.V1Mandates.Retrieve(
  context.TODO(), "mandate_1MvojA2eZvKYlo2CvqTABjZs", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Mandates;
Mandate mandate = service.Get("mandate_1MvojA2eZvKYlo2CvqTABjZs");
```

### Response

```json
{
  "id": "mandate_1MvojA2eZvKYlo2CvqTABjZs",
  "object": "mandate",
  "customer_acceptance": {
    "accepted_at": 123456789,
    "online": {
      "ip_address": "127.0.0.0",
      "user_agent": "device"
    },
    "type": "online"
  },
  "livemode": false,
  "multi_use": {},
  "payment_method": "pm_123456789",
  "payment_method_details": {
    "sepa_debit": {
      "reference": "123456789",
      "url": ""
    },
    "type": "sepa_debit"
  },
  "status": "active",
  "type": "multi_use"
}
```