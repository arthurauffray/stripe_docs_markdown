# Create a payment method domain

Creates a payment method domain.

## Returns

Returns a payment method domain object.

## Parameters

- `domain_name` (string, required)
  The domain name that this payment method domain object represents.

- `enabled` (boolean, optional)
  Whether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements or Embedded Checkout.

```curl
curl https://api.stripe.com/v1/payment_method_domains \
  -u "<<YOUR_SECRET_KEY>>" \
  -d domain_name="example.com"
```

```cli
stripe payment_method_domains create  \
  --domain-name="example.com"
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

payment_method_domain = client.v1.payment_method_domains.create({
  domain_name: 'example.com',
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

payment_method_domain = client.v1.payment_method_domains.create({
  "domain_name": "example.com",
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentMethodDomain = $stripe->paymentMethodDomains->create([
  'domain_name' => 'example.com',
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PaymentMethodDomainCreateParams params =
  PaymentMethodDomainCreateParams.builder().setDomainName("example.com").build();

PaymentMethodDomain paymentMethodDomain =
  client.v1().paymentMethodDomains().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentMethodDomain = await stripe.paymentMethodDomains.create({
  domain_name: 'example.com',
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PaymentMethodDomainCreateParams{
  DomainName: stripe.String("example.com"),
}
result, err := sc.V1PaymentMethodDomains.Create(context.TODO(), params)
```

```dotnet
var options = new PaymentMethodDomainCreateOptions { DomainName = "example.com" };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.PaymentMethodDomains;
PaymentMethodDomain paymentMethodDomain = service.Create(options);
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