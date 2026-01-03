# Create a refund

When you create a new refund, you must specify a Charge or a PaymentIntent object on which to create it.

Creating a new refund will refund a charge that has previously been created but not yet refunded. Funds will be refunded to the credit or debit card that was originally charged.

You can optionally refund only part of a charge. You can do so multiple times, until the entire charge has been refunded.

Once entirely refunded, a charge can’t be refunded again. This method will raise an error when called on an already-refunded charge, or when trying to refund more money than is left on a charge.

## Returns

Returns the `Refund` object if the refund succeeded. Raises [an error](https://docs.stripe.com/api/refunds/create.md#errors) if the Charge/PaymentIntent has already been refunded, or if an invalid identifier was provided.

## Parameters

- `amount` (integer, optional)
  A positive integer in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal) representing how much of this charge to refund. Can refund only up to the remaining, unrefunded amount of the charge.

- `charge` (string, optional)
  The identifier of the charge to refund.

- `instructions_email` (string, optional)
  For payment methods without native refund support (e.g., Konbini, PromptPay), use this email from the customer to receive refund instructions.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `origin` (enum, optional)
  String indicating the origin of a refund. It’s used when the refund originates from a [Customer Balance](https://docs.stripe.com/docs/payments/customer-balance/refunding.md#create-return-dashboard--api) instead of from a Charge or PaymentIntent. If this value is provided, a Charge or PaymentIntent identifier is not required.
Possible enum values:
  - `customer_balance`

- `payment_intent` (string, optional)
  The identifier of the PaymentIntent to refund.

- `reason` (string, optional)
  String indicating the reason for the refund. If set, possible values are `duplicate`, `fraudulent`, and `requested_by_customer`. If you believe the charge to be fraudulent, specifying `fraudulent` as the reason will add the associated card and email to your [block lists](https://docs.stripe.com/docs/radar/lists.md), and will also help us improve our fraud detection algorithms.

- `refund_application_fee` (boolean, optional)
  Boolean indicating whether the application fee should be refunded when refunding this charge. If a full charge refund is given, the full application fee will be refunded. Otherwise, the application fee will be refunded in an amount proportional to the amount of the charge refunded. An application fee can be refunded only by the application that created the charge.

- `reverse_transfer` (boolean, optional)
  Boolean indicating whether the transfer should be reversed when refunding this charge. The transfer will be reversed proportionally to the amount being refunded (either the entire or partial amount).A transfer can be reversed only by the application that created the charge.

```curl
curl https://api.stripe.com/v1/refunds \
  -u "<<YOUR_SECRET_KEY>>" \
  -d charge=ch_1NirD82eZvKYlo2CIvbtLWuY
```

```cli
stripe refunds create  \
  --charge=ch_1NirD82eZvKYlo2CIvbtLWuY
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

refund = client.v1.refunds.create({charge: 'ch_1NirD82eZvKYlo2CIvbtLWuY'})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

refund = client.v1.refunds.create({"charge": "ch_1NirD82eZvKYlo2CIvbtLWuY"})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$refund = $stripe->refunds->create(['charge' => 'ch_1NirD82eZvKYlo2CIvbtLWuY']);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

RefundCreateParams params =
  RefundCreateParams.builder().setCharge("ch_1NirD82eZvKYlo2CIvbtLWuY").build();

Refund refund = client.v1().refunds().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const refund = await stripe.refunds.create({
  charge: 'ch_1NirD82eZvKYlo2CIvbtLWuY',
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.RefundCreateParams{
  Charge: stripe.String("ch_1NirD82eZvKYlo2CIvbtLWuY"),
}
result, err := sc.V1Refunds.Create(context.TODO(), params)
```

```dotnet
var options = new RefundCreateOptions { Charge = "ch_1NirD82eZvKYlo2CIvbtLWuY" };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Refunds;
Refund refund = service.Create(options);
```

### Response

```json
{
  "id": "re_1Nispe2eZvKYlo2Cd31jOCgZ",
  "object": "refund",
  "amount": 1000,
  "balance_transaction": "txn_1Nispe2eZvKYlo2CYezqFhEx",
  "charge": "ch_1NirD82eZvKYlo2CIvbtLWuY",
  "created": 1692942318,
  "currency": "usd",
  "destination_details": {
    "card": {
      "reference": "123456789012",
      "reference_status": "available",
      "reference_type": "acquirer_reference_number",
      "type": "refund"
    },
    "type": "card"
  },
  "metadata": {},
  "payment_intent": "pi_1GszsK2eZvKYlo2CfhZyoZLp",
  "reason": null,
  "receipt_number": null,
  "source_transfer_reversal": null,
  "status": "succeeded",
  "transfer_reversal": null
}
```