# Retrieve a registration

Returns a Tax `Registration` object.

## Returns

A Tax `Registration` object.

```curl
curl https://api.stripe.com/v1/tax/registrations/taxreg_NkyGPRPytKq66j \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe tax registrations retrieve taxreg_NkyGPRPytKq66j
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

registration = client.v1.tax.registrations.retrieve('taxreg_NkyGPRPytKq66j')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

registration = client.v1.tax.registrations.retrieve("taxreg_NkyGPRPytKq66j")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$registration = $stripe->tax->registrations->retrieve('taxreg_NkyGPRPytKq66j', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

RegistrationRetrieveParams params = RegistrationRetrieveParams.builder().build();

Registration registration =
  client.v1().tax().registrations().retrieve("taxreg_NkyGPRPytKq66j", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const registration = await stripe.tax.registrations.retrieve(
  'taxreg_NkyGPRPytKq66j'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TaxRegistrationRetrieveParams{}
result, err := sc.V1TaxRegistrations.Retrieve(
  context.TODO(), "taxreg_NkyGPRPytKq66j", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Tax.Registrations;
Stripe.Tax.Registration registration = service.Get("taxreg_NkyGPRPytKq66j");
```

### Response

```json
{
  "id": "taxreg_NkyGPRPytKq66j",
  "object": "tax.registration",
  "active_from": 1682036640,
  "country": "US",
  "country_options": {
    "us": {
      "state": "CA",
      "type": "state_sales_tax"
    }
  },
  "created": 1682006400,
  "expires_at": null,
  "livemode": false,
  "status": "active",
  "state": "CA",
  "type": "standard"
}
```