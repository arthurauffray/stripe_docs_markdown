# Update a payment method domain

Updates an existing payment method domain.

## Returns

Returns the updated payment method domain object.

## Parameters

- `enabled` (boolean, optional)
  Whether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements or Embedded Checkout.

```curl
curl https://api.stripe.com/v1/payment_method_domains/pmd_1Nnrer2eZvKYlo2Cips79tWl \
  -u "<<YOUR_SECRET_KEY>>" \
  -d enabled=false
```

```cli
stripe payment_method_domains update pmd_1Nnrer2eZvKYlo2Cips79tWl \
  --enabled=false
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

payment_method_domain = client.v1.payment_method_domains.update(
  'pmd_1Nnrer2eZvKYlo2Cips79tWl',
  {enabled: false},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

payment_method_domain = client.v1.payment_method_domains.update(
  "pmd_1Nnrer2eZvKYlo2Cips79tWl",
  {"enabled": False},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentMethodDomain = $stripe->paymentMethodDomains->update(
  'pmd_1Nnrer2eZvKYlo2Cips79tWl',
  ['enabled' => false]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PaymentMethodDomainUpdateParams params =
  PaymentMethodDomainUpdateParams.builder().setEnabled(false).build();

PaymentMethodDomain paymentMethodDomain =
  client.v1().paymentMethodDomains().update("pmd_1Nnrer2eZvKYlo2Cips79tWl", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentMethodDomain = await stripe.paymentMethodDomains.update(
  'pmd_1Nnrer2eZvKYlo2Cips79tWl',
  {
    enabled: false,
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PaymentMethodDomainUpdateParams{Enabled: stripe.Bool(false)}
result, err := sc.V1PaymentMethodDomains.Update(
  context.TODO(), "pmd_1Nnrer2eZvKYlo2Cips79tWl", params)
```

```dotnet
var options = new PaymentMethodDomainUpdateOptions { Enabled = false };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.PaymentMethodDomains;
PaymentMethodDomain paymentMethodDomain = service.Update(
    "pmd_1Nnrer2eZvKYlo2Cips79tWl",
    options);
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
  "enabled": false,
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