# Retrieve a PaymentMethod

Retrieves a PaymentMethod object attached to the StripeAccount. To retrieve a payment method attached to a Customer, you should use [Retrieve a Customer’s PaymentMethods](https://docs.stripe.com/docs/api/payment_methods/customer.md)

## Returns

Returns a PaymentMethod object.

```curl
curl https://api.stripe.com/v1/payment_methods/pm_1Q0PsIJvEtkwdCNYMSaVuRz6 \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe payment_methods retrieve pm_1Q0PsIJvEtkwdCNYMSaVuRz6
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

payment_method = client.v1.payment_methods.retrieve('pm_1Q0PsIJvEtkwdCNYMSaVuRz6')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

payment_method = client.v1.payment_methods.retrieve("pm_1Q0PsIJvEtkwdCNYMSaVuRz6")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentMethod = $stripe->paymentMethods->retrieve(
  'pm_1Q0PsIJvEtkwdCNYMSaVuRz6',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PaymentMethodRetrieveParams params = PaymentMethodRetrieveParams.builder().build();

PaymentMethod paymentMethod =
  client.v1().paymentMethods().retrieve("pm_1Q0PsIJvEtkwdCNYMSaVuRz6", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentMethod = await stripe.paymentMethods.retrieve(
  'pm_1Q0PsIJvEtkwdCNYMSaVuRz6'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PaymentMethodRetrieveParams{}
result, err := sc.V1PaymentMethods.Retrieve(
  context.TODO(), "pm_1Q0PsIJvEtkwdCNYMSaVuRz6", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.PaymentMethods;
PaymentMethod paymentMethod = service.Get("pm_1Q0PsIJvEtkwdCNYMSaVuRz6");
```

### Response

```json
{
  "id": "pm_1Q0PsIJvEtkwdCNYMSaVuRz6",
  "object": "payment_method",
  "allow_redisplay": "unspecified",
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
    "name": "John Doe",
    "phone": null
  },
  "created": 1726673582,
  "customer": null,
  "livemode": false,
  "metadata": {},
  "type": "us_bank_account",
  "us_bank_account": {
    "account_holder_type": "individual",
    "account_type": "checking",
    "bank_name": "STRIPE TEST BANK",
    "financial_connections_account": null,
    "fingerprint": "LstWJFsCK7P349Bg",
    "last4": "6789",
    "networks": {
      "preferred": "ach",
      "supported": [
        "ach"
      ]
    },
    "routing_number": "110000000",
    "status_details": {}
  }
}
```