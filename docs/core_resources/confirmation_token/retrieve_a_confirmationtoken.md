# Retrieve a ConfirmationToken

Retrieves an existing ConfirmationToken object

## Returns

Returns the specified ConfirmationToken

```curl
curl https://api.stripe.com/v1/confirmation_tokens/ctoken_1NnQUf2eZvKYlo2CIObdtbnb \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe confirmation_tokens retrieve ctoken_1NnQUf2eZvKYlo2CIObdtbnb
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

confirmation_token = client.v1.confirmation_tokens.retrieve('ctoken_1NnQUf2eZvKYlo2CIObdtbnb')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

confirmation_token = client.v1.confirmation_tokens.retrieve(
  "ctoken_1NnQUf2eZvKYlo2CIObdtbnb",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$confirmationToken = $stripe->confirmationTokens->retrieve(
  'ctoken_1NnQUf2eZvKYlo2CIObdtbnb',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ConfirmationTokenRetrieveParams params =
  ConfirmationTokenRetrieveParams.builder().build();

ConfirmationToken confirmationToken =
  client.v1().confirmationTokens().retrieve(
    "ctoken_1NnQUf2eZvKYlo2CIObdtbnb",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const confirmationToken = await stripe.confirmationTokens.retrieve(
  'ctoken_1NnQUf2eZvKYlo2CIObdtbnb'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.ConfirmationTokenRetrieveParams{}
result, err := sc.V1ConfirmationTokens.Retrieve(
  context.TODO(), "ctoken_1NnQUf2eZvKYlo2CIObdtbnb", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.ConfirmationTokens;
ConfirmationToken confirmationToken = service.Get("ctoken_1NnQUf2eZvKYlo2CIObdtbnb");
```

### Response

```json
{
  "id": "ctoken_1NnQUf2eZvKYlo2CIObdtbnb",
  "object": "confirmation_token",
  "created": 1694025025,
  "expires_at": 1694068225,
  "livemode": true,
  "mandate_data": null,
  "payment_intent": null,
  "payment_method": null,
  "payment_method_preview": {
    "billing_details": {
      "address": {
        "city": "Hyde Park",
        "country": "US",
        "line1": "50 Sprague St",
        "line2": "",
        "postal_code": "02136",
        "state": "MA"
      },
      "email": "jennyrosen@stripe.com",
      "name": "Jenny Rosen",
      "phone": null
    },
    "card": {
      "brand": "visa",
      "checks": {
        "address_line1_check": null,
        "address_postal_code_check": null,
        "cvc_check": null
      },
      "country": "US",
      "display_brand": "visa",
      "exp_month": 8,
      "exp_year": 2026,
      "funding": "credit",
      "generated_from": null,
      "last4": "4242",
      "networks": {
        "available": [
          "visa"
        ],
        "preferred": null
      },
      "three_d_secure_usage": {
        "supported": true
      },
      "wallet": null
    },
    "type": "card"
  },
  "return_url": "https://example.com/return",
  "setup_future_usage": "off_session",
  "setup_intent": null,
  "shipping": {
    "address": {
      "city": "Hyde Park",
      "country": "US",
      "line1": "50 Sprague St",
      "line2": "",
      "postal_code": "02136",
      "state": "MA"
    },
    "name": "Jenny Rosen",
    "phone": null
  }
}
```