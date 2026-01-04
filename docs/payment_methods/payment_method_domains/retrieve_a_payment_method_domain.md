# Retrieve a payment method domain

Retrieves the details of an existing payment method domain.

## Returns

Returns a payment method domain object.

```curl
curl https://api.stripe.com/v1/payment_method_domains/pmd_1Nnrer2eZvKYlo2Cips79tWl \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe payment_method_domains retrieve pmd_1Nnrer2eZvKYlo2Cips79tWl
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

payment_method_domain = client.v1.payment_method_domains.retrieve('pmd_1Nnrer2eZvKYlo2Cips79tWl')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

payment_method_domain = client.v1.payment_method_domains.retrieve(
  "pmd_1Nnrer2eZvKYlo2Cips79tWl",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentMethodDomain = $stripe->paymentMethodDomains->retrieve(
  'pmd_1Nnrer2eZvKYlo2Cips79tWl',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PaymentMethodDomainRetrieveParams params =
  PaymentMethodDomainRetrieveParams.builder().build();

PaymentMethodDomain paymentMethodDomain =
  client.v1().paymentMethodDomains().retrieve(
    "pmd_1Nnrer2eZvKYlo2Cips79tWl",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentMethodDomain = await stripe.paymentMethodDomains.retrieve(
  'pmd_1Nnrer2eZvKYlo2Cips79tWl'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PaymentMethodDomainRetrieveParams{}
result, err := sc.V1PaymentMethodDomains.Retrieve(
  context.TODO(), "pmd_1Nnrer2eZvKYlo2Cips79tWl", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.PaymentMethodDomains;
PaymentMethodDomain paymentMethodDomain = service.Get(
    "pmd_1Nnrer2eZvKYlo2Cips79tWl");
```

### Response

```json
{
  "id": "pmd_1Nnrer2eZvKYlo2Cips79tWl",
  "object": "payment_method_domain",
  "apple_pay": {
    "status": "active"
  },
  "created": 1694129445,
  "domain_name": "example.com",
  "enabled": true,
  "google_pay": {
    "status": "active"
  },
  "link": {
    "status": "active"
  },
  "livemode": false,
  "paypal": {
    "status": "active"
  }
}
```