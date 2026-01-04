# Detach a PaymentMethod from a Customer

Detaches a PaymentMethod object from a Customer. After a PaymentMethod is detached, it can no longer be used for a payment or re-attached to a Customer.

## Returns

Returns a PaymentMethod object.

```curl
curl -X POST https://api.stripe.com/v1/payment_methods/pm_1MqLiJLkdIwHu7ixUEgbFdYF/detach \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe payment_methods detach pm_1MqLiJLkdIwHu7ixUEgbFdYF
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

payment_method = client.v1.payment_methods.detach('pm_1MqLiJLkdIwHu7ixUEgbFdYF')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

payment_method = client.v1.payment_methods.detach("pm_1MqLiJLkdIwHu7ixUEgbFdYF")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentMethod = $stripe->paymentMethods->detach('pm_1MqLiJLkdIwHu7ixUEgbFdYF', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PaymentMethodDetachParams params = PaymentMethodDetachParams.builder().build();

PaymentMethod paymentMethod =
  client.v1().paymentMethods().detach("pm_1MqLiJLkdIwHu7ixUEgbFdYF", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentMethod = await stripe.paymentMethods.detach(
  'pm_1MqLiJLkdIwHu7ixUEgbFdYF'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PaymentMethodDetachParams{}
result, err := sc.V1PaymentMethods.Detach(
  context.TODO(), "pm_1MqLiJLkdIwHu7ixUEgbFdYF", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.PaymentMethods;
PaymentMethod paymentMethod = service.Detach("pm_1MqLiJLkdIwHu7ixUEgbFdYF");
```

### Response

```json
{
  "id": "pm_1MqLiJLkdIwHu7ixUEgbFdYF",
  "object": "payment_method",
  "billing_details": {
    "address": {
      "city": null,
      "country": null,
      "line1": null,
      "line2": null,
      "postal_code": null,
      "state": null
    },
    "email": null,
    "name": null,
    "phone": null
  },
  "card": {
    "brand": "visa",
    "checks": {
      "address_line1_check": null,
      "address_postal_code_check": null,
      "cvc_check": "unchecked"
    },
    "country": "US",
    "exp_month": 8,
    "exp_year": 2026,
    "fingerprint": "mToisGZ01V71BCos",
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
  "created": 1679945299,
  "customer": null,
  "livemode": false,
  "metadata": {},
  "type": "card"
}
```