# Validate an existing payment method domain

Some payment methods might require additional steps to register a domain. If the requirements weren’t satisfied when the domain was created, the payment method will be inactive on the domain. The payment method doesn’t appear in Elements or Embedded Checkout for this domain until it is active.

To activate a payment method on an existing payment method domain, complete the required registration steps specific to the payment method, and then validate the payment method domain with this endpoint.

Related guides: [Payment method domains](https://docs.stripe.com/docs/payments/payment-methods/pmd-registration.md).

## Returns

Returns the updated payment method domain object.

```curl
curl -X POST https://api.stripe.com/v1/payment_method_domains/pmd_1Nnrer2eZvKYlo2Cips79tWl/validate \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe payment_method_domains validate pmd_1Nnrer2eZvKYlo2Cips79tWl
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

payment_method_domain = client.v1.payment_method_domains.validate('pmd_1Nnrer2eZvKYlo2Cips79tWl')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

payment_method_domain = client.v1.payment_method_domains.validate(
  "pmd_1Nnrer2eZvKYlo2Cips79tWl",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentMethodDomain = $stripe->paymentMethodDomains->validate(
  'pmd_1Nnrer2eZvKYlo2Cips79tWl',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PaymentMethodDomainValidateParams params =
  PaymentMethodDomainValidateParams.builder().build();

PaymentMethodDomain paymentMethodDomain =
  client.v1().paymentMethodDomains().validate(
    "pmd_1Nnrer2eZvKYlo2Cips79tWl",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentMethodDomain = await stripe.paymentMethodDomains.validate(
  'pmd_1Nnrer2eZvKYlo2Cips79tWl'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PaymentMethodDomainValidateParams{}
result, err := sc.V1PaymentMethodDomains.Validate(
  context.TODO(), "pmd_1Nnrer2eZvKYlo2Cips79tWl", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.PaymentMethodDomains;
PaymentMethodDomain paymentMethodDomain = service.Validate(
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