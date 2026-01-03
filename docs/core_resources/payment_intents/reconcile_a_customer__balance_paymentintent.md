# Reconcile a customer_balance PaymentIntent

Manually reconcile the remaining amount for a `customer_balance` PaymentIntent.

## Returns

Returns a PaymentIntent object.

## Parameters

- `amount` (integer, optional)
  Amount that you intend to apply to this PaymentIntent from the customer’s cash balance. If the PaymentIntent was created by an Invoice, the full amount of the PaymentIntent is applied regardless of this parameter.

  A positive integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal) (for example, 100 cents to charge 1 USD or 100 to charge 100 JPY, a zero-decimal currency). The maximum amount is the amount of the PaymentIntent.

  When you omit the amount, it defaults to the remaining amount requested on the PaymentIntent.

- `currency` (enum, optional)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

```curl
curl -X POST https://api.stripe.com/v1/payment_intents/pi_1GszwY2eZvKYlo2CohCEmT6b/apply_customer_balance \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe payment_intents apply_customer_balance pi_1GszwY2eZvKYlo2CohCEmT6b
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

payment_intent = client.v1.payment_intents.apply_customer_balance('pi_1GszwY2eZvKYlo2CohCEmT6b')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

payment_intent = client.v1.payment_intents.apply_customer_balance(
  "pi_1GszwY2eZvKYlo2CohCEmT6b",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentIntent = $stripe->paymentIntents->applyCustomerBalance(
  'pi_1GszwY2eZvKYlo2CohCEmT6b',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PaymentIntentApplyCustomerBalanceParams params =
  PaymentIntentApplyCustomerBalanceParams.builder().build();

PaymentIntent paymentIntent =
  client.v1().paymentIntents().applyCustomerBalance(
    "pi_1GszwY2eZvKYlo2CohCEmT6b",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.applyCustomerBalance(
  'pi_1GszwY2eZvKYlo2CohCEmT6b'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PaymentIntentApplyCustomerBalanceParams{}
result, err := sc.V1PaymentIntents.ApplyCustomerBalance(
  context.TODO(), "pi_1GszwY2eZvKYlo2CohCEmT6b", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.PaymentIntents;
PaymentIntent paymentIntent = service.ApplyCustomerBalance(
    "pi_1GszwY2eZvKYlo2CohCEmT6b");
```

### Response

```json
{
  "id": "pi_1GszwY2eZvKYlo2CohCEmT6b",
  "object": "payment_intent",
  "amount": 1000,
  "amount_capturable": 0,
  "amount_details": {
    "tip": {}
  },
  "amount_received": 0,
  "application": null,
  "application_fee_amount": null,
  "automatic_payment_methods": null,
  "canceled_at": null,
  "cancellation_reason": null,
  "capture_method": "automatic",
  "client_secret": "pi_1GszwY2eZvKYlo2CohCEmT6b_secret_1jQJzqkrQvx4BpwI5hn6WSEO5",
  "confirmation_method": "automatic",
  "created": 1591918582,
  "currency": "usd",
  "customer": null,
  "description": "Created by stripe.com/docs demo",
  "last_payment_error": null,
  "latest_charge": null,
  "livemode": false,
  "metadata": {},
  "next_action": null,
  "on_behalf_of": null,
  "payment_method": null,
  "payment_method_options": {
    "card": {
      "installments": null,
      "mandate_options": null,
      "network": null,
      "request_three_d_secure": "automatic"
    }
  },
  "payment_method_types": [
    "card"
  ],
  "processing": null,
  "receipt_email": null,
  "redaction": null,
  "review": null,
  "setup_future_usage": null,
  "shipping": null,
  "statement_descriptor": null,
  "statement_descriptor_suffix": null,
  "status": "requires_payment_method",
  "transfer_data": null,
  "transfer_group": null
}
```