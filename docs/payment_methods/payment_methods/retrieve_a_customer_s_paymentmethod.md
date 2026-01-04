# Retrieve a Customer's PaymentMethod

Retrieves a PaymentMethod object for a given Customer.

## Returns

Returns a PaymentMethod object.

```curl
curl https://api.stripe.com/v1/customers/cus_9s6XKzkNRiz8i3/payment_methods/pm_1NVChw2eZvKYlo2CHxiM5E2E \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe customers retrieve_payment_method cus_9s6XKzkNRiz8i3 pm_1NVChw2eZvKYlo2CHxiM5E2E
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

payment_method = client.v1.customers.payment_methods.retrieve(
  'cus_9s6XKzkNRiz8i3',
  'pm_1NVChw2eZvKYlo2CHxiM5E2E',
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

payment_method = client.v1.customers.payment_methods.retrieve(
  "cus_9s6XKzkNRiz8i3",
  "pm_1NVChw2eZvKYlo2CHxiM5E2E",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentMethod = $stripe->customers->retrievePaymentMethod(
  'cus_9s6XKzkNRiz8i3',
  'pm_1NVChw2eZvKYlo2CHxiM5E2E',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CustomerPaymentMethodRetrieveParams params =
  CustomerPaymentMethodRetrieveParams.builder().build();

PaymentMethod paymentMethod =
  client.v1().customers().paymentMethods().retrieve(
    "cus_9s6XKzkNRiz8i3",
    "pm_1NVChw2eZvKYlo2CHxiM5E2E",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentMethod = await stripe.customers.retrievePaymentMethod(
  'cus_9s6XKzkNRiz8i3',
  'pm_1NVChw2eZvKYlo2CHxiM5E2E'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CustomerRetrievePaymentMethodParams{
  Customer: stripe.String("cus_9s6XKzkNRiz8i3"),
}
result, err := sc.V1Customers.RetrievePaymentMethod(
  context.TODO(), "pm_1NVChw2eZvKYlo2CHxiM5E2E", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Customers.PaymentMethods;
PaymentMethod paymentMethod = service.Get(
    "cus_9s6XKzkNRiz8i3",
    "pm_1NVChw2eZvKYlo2CHxiM5E2E");
```

### Response

```json
{
  "id": "pm_1NVChw2eZvKYlo2CHxiM5E2E",
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
      "cvc_check": "pass"
    },
    "country": "US",
    "exp_month": 12,
    "exp_year": 2034,
    "fingerprint": "Xt5EWLLDS7FJjR1c",
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
  "created": 1689682128,
  "customer": "cus_9s6XKzkNRiz8i3",
  "livemode": false,
  "metadata": {},
  "redaction": null,
  "type": "card"
}
```