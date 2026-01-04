# Retrieve a cardholder

Retrieves an Issuing `Cardholder` object.

## Returns

Returns an Issuing `Cardholder` object if a valid identifier was provided.

```curl
curl https://api.stripe.com/v1/issuing/cardholders/ich_1MsKAB2eZvKYlo2C3eZ2BdvK \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe issuing cardholders retrieve ich_1MsKAB2eZvKYlo2C3eZ2BdvK
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

cardholder = client.v1.issuing.cardholders.retrieve('ich_1MsKAB2eZvKYlo2C3eZ2BdvK')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

cardholder = client.v1.issuing.cardholders.retrieve("ich_1MsKAB2eZvKYlo2C3eZ2BdvK")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$cardholder = $stripe->issuing->cardholders->retrieve(
  'ich_1MsKAB2eZvKYlo2C3eZ2BdvK',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CardholderRetrieveParams params = CardholderRetrieveParams.builder().build();

Cardholder cardholder =
  client.v1().issuing().cardholders().retrieve(
    "ich_1MsKAB2eZvKYlo2C3eZ2BdvK",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const cardholder = await stripe.issuing.cardholders.retrieve(
  'ich_1MsKAB2eZvKYlo2C3eZ2BdvK'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.IssuingCardholderRetrieveParams{}
result, err := sc.V1IssuingCardholders.Retrieve(
  context.TODO(), "ich_1MsKAB2eZvKYlo2C3eZ2BdvK", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Issuing.Cardholders;
Stripe.Issuing.Cardholder cardholder = service.Get("ich_1MsKAB2eZvKYlo2C3eZ2BdvK");
```

### Response

```json
{
  "id": "ich_1MsKAB2eZvKYlo2C3eZ2BdvK",
  "object": "issuing.cardholder",
  "billing": {
    "address": {
      "line1": "1234 Main Street",
      "city": "San Francisco",
      "state": "CA",
      "country": "US",
      "postal_code": "94111"
    }
  },
  "company": null,
  "created": 1680415995,
  "email": "jenny.rosen@example.com",
  "individual": null,
  "livemode": false,
  "metadata": {},
  "name": "Jenny Rosen",
  "phone_number": "+18888675309",
  "redaction": null,
  "requirements": {
    "disabled_reason": "requirements.past_due",
    "past_due": [
      "individual.card_issuing.user_terms_acceptance.ip",
      "individual.card_issuing.user_terms_acceptance.date",
      "individual.first_name",
      "individual.last_name"
    ]
  },
  "spending_controls": {
    "allowed_categories": [],
    "blocked_categories": [],
    "spending_limits": [],
    "spending_limits_currency": null
  },
  "status": "active",
  "type": "individual"
}
```