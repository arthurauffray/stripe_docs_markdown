# Attach a PaymentMethod to a Customer

Attaches a PaymentMethod object to a Customer.

To attach a new PaymentMethod to a customer for future payments, we recommend you use a [SetupIntent](https://docs.stripe.com/docs/api/setup_intents.md) or a PaymentIntent with [setup_future_usage](https://docs.stripe.com/docs/api/payment_intents/create.md#create_payment_intent-setup_future_usage). These approaches will perform any necessary steps to set up the PaymentMethod for future payments. Using the `/v1/payment_methods/:id/attach` endpoint without first using a SetupIntent or PaymentIntent with `setup_future_usage` does not optimize the PaymentMethod for future use, which makes later declines and payment friction more likely. See [Optimizing cards for future payments](https://docs.stripe.com/docs/payments/payment-intents.md#future-usage) for more information about setting up future payments.

To use this PaymentMethod as the default for invoice or subscription payments, set [`invoice_settings.default_payment_method`](https://docs.stripe.com/docs/api/customers/update.md#update_customer-invoice_settings-default_payment_method), on the Customer to the PaymentMethod’s ID.

## Returns

Returns a PaymentMethod object.

## Parameters

- `customer` (string, optional)
  The ID of the customer to which to attach the PaymentMethod.

- `customer_account` (string, optional)
  The ID of the Account representing the customer to which to attach the PaymentMethod.

```curl
curl https://api.stripe.com/v1/payment_methods/pm_1MqM05LkdIwHu7ixlDxxO6Mc/attach \
  -u "<<YOUR_SECRET_KEY>>" \
  -d customer=cus_NbZ8Ki3f322LNn
```

```cli
stripe payment_methods attach pm_1MqM05LkdIwHu7ixlDxxO6Mc \
  --customer=cus_NbZ8Ki3f322LNn
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

payment_method = client.v1.payment_methods.attach(
  'pm_1MqM05LkdIwHu7ixlDxxO6Mc',
  {customer: 'cus_NbZ8Ki3f322LNn'},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

payment_method = client.v1.payment_methods.attach(
  "pm_1MqM05LkdIwHu7ixlDxxO6Mc",
  {"customer": "cus_NbZ8Ki3f322LNn"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentMethod = $stripe->paymentMethods->attach(
  'pm_1MqM05LkdIwHu7ixlDxxO6Mc',
  ['customer' => 'cus_NbZ8Ki3f322LNn']
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PaymentMethodAttachParams params =
  PaymentMethodAttachParams.builder().setCustomer("cus_NbZ8Ki3f322LNn").build();

PaymentMethod paymentMethod =
  client.v1().paymentMethods().attach("pm_1MqM05LkdIwHu7ixlDxxO6Mc", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentMethod = await stripe.paymentMethods.attach(
  'pm_1MqM05LkdIwHu7ixlDxxO6Mc',
  {
    customer: 'cus_NbZ8Ki3f322LNn',
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PaymentMethodAttachParams{
  Customer: stripe.String("cus_NbZ8Ki3f322LNn"),
}
result, err := sc.V1PaymentMethods.Attach(
  context.TODO(), "pm_1MqM05LkdIwHu7ixlDxxO6Mc", params)
```

```dotnet
var options = new PaymentMethodAttachOptions { Customer = "cus_NbZ8Ki3f322LNn" };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.PaymentMethods;
PaymentMethod paymentMethod = service.Attach("pm_1MqM05LkdIwHu7ixlDxxO6Mc", options);
```

### Response

```json
{
  "id": "pm_1MqM05LkdIwHu7ixlDxxO6Mc",
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
  "created": 1679946402,
  "customer": "cus_NbZ8Ki3f322LNn",
  "livemode": false,
  "metadata": {},
  "type": "card"
}
```