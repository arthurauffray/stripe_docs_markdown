# Capture a charge

Capture the payment of an existing, uncaptured charge that was created with the `capture` option set to false.

Uncaptured payments expire a set number of days after they are created ([7 by default](https://docs.stripe.com/docs/charges/placing-a-hold.md)), after which they are marked as refunded and capture attempts will fail.

Don’t use this method to capture a PaymentIntent-initiated charge. Use [Capture a PaymentIntent](https://docs.stripe.com/docs/api/payment_intents/capture.md).

## Returns

Returns the charge object, with an updated captured property (set to true). Capturing a charge will always succeed, unless the charge is already refunded, expired, captured, or an invalid capture amount is specified, in which case this method will raise [an error](https://docs.stripe.com/api/charges/capture.md#errors).

## Parameters

- `amount` (integer, optional)
  The amount to capture, which must be less than or equal to the original amount.

- `application_fee_amount` (integer, optional)
  An application fee amount to add on to this charge, which must be less than or equal to the original amount.

- `receipt_email` (string, optional)
  The email address to send this charge’s receipt to. This will override the previously-specified email address for this charge, if one was set. Receipts will not be sent in test mode.

  The maximum length is 800 characters.

- `statement_descriptor` (string, optional)
  For a non-card charge, text that appears on the customer’s statement as the statement descriptor. This value overrides the account’s default statement descriptor. For information about requirements, including the 22-character limit, see [the Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors.md).

  For a card charge, this value is ignored unless you don’t specify a `statement_descriptor_suffix`, in which case this value is used as the suffix.

- `statement_descriptor_suffix` (string, optional)
  Provides information about a card charge. Concatenated to the account’s [statement descriptor prefix](https://docs.stripe.com/get-started/account/statement-descriptors.md#static) to form the complete statement descriptor that appears on the customer’s statement. If the account has no prefix value, the suffix is concatenated to the account’s statement descriptor.

- `transfer_data` (object, optional)
  An optional dictionary including the account to automatically transfer to as part of a destination charge. [See the Connect documentation](https://docs.stripe.com/docs/connect/destination-charges.md) for details.

  - `transfer_data.amount` (integer, optional)
    The amount transferred to the destination account, if specified. By default, the entire charge amount is transferred to the destination account.

- `transfer_group` (string, optional)
  A string that identifies this transaction as part of a group. `transfer_group` may only be provided if it has not been set. See the [Connect documentation](https://docs.stripe.com/docs/connect/separate-charges-and-transfers.md#transfer-options) for details.

```curl
curl -X POST https://api.stripe.com/v1/charges/ch_3MrVHGLkdIwHu7ix1mN3zEiP/capture \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe charges capture ch_3MrVHGLkdIwHu7ix1mN3zEiP
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

charge = client.v1.charges.capture('ch_3MrVHGLkdIwHu7ix1mN3zEiP')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

charge = client.v1.charges.capture("ch_3MrVHGLkdIwHu7ix1mN3zEiP")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$charge = $stripe->charges->capture('ch_3MrVHGLkdIwHu7ix1mN3zEiP', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ChargeCaptureParams params = ChargeCaptureParams.builder().build();

Charge charge = client.v1().charges().capture("ch_3MrVHGLkdIwHu7ix1mN3zEiP", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const charge = await stripe.charges.capture('ch_3MrVHGLkdIwHu7ix1mN3zEiP');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.ChargeCaptureParams{}
result, err := sc.V1Charges.Capture(
  context.TODO(), "ch_3MrVHGLkdIwHu7ix1mN3zEiP", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Charges;
Charge charge = service.Capture("ch_3MrVHGLkdIwHu7ix1mN3zEiP");
```

### Response

```json
{
  "id": "ch_3MrVHGLkdIwHu7ix1mN3zEiP",
  "object": "charge",
  "amount": 1099,
  "amount_captured": 1099,
  "amount_refunded": 0,
  "application": null,
  "application_fee": null,
  "application_fee_amount": null,
  "balance_transaction": "txn_3MrVHGLkdIwHu7ix1Yb1LdXJ",
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
  "calculated_statement_descriptor": "Stripe",
  "captured": true,
  "created": 1680220390,
  "currency": "usd",
  "customer": null,
  "description": null,
  "destination": null,
  "dispute": null,
  "disputed": false,
  "failure_balance_transaction": null,
  "failure_code": null,
  "failure_message": null,
  "fraud_details": {},
  "livemode": false,
  "metadata": {},
  "on_behalf_of": null,
  "order": null,
  "outcome": {
    "network_status": "approved_by_network",
    "reason": null,
    "risk_level": "normal",
    "risk_score": 0,
    "seller_message": "Payment complete.",
    "type": "authorized"
  },
  "paid": true,
  "payment_intent": null,
  "payment_method": "card_1MrVHGLkdIwHu7ix7H1PgERt",
  "payment_method_details": {
    "card": {
      "brand": "visa",
      "checks": {
        "address_line1_check": null,
        "address_postal_code_check": null,
        "cvc_check": null
      },
      "country": "US",
      "exp_month": 3,
      "exp_year": 2024,
      "fingerprint": "mToisGZ01V71BCos",
      "funding": "credit",
      "installments": null,
      "last4": "4242",
      "mandate": null,
      "network": "visa",
      "network_token": {
        "used": false
      },
      "three_d_secure": null,
      "wallet": null
    },
    "type": "card"
  },
  "receipt_email": null,
  "receipt_number": null,
  "receipt_url": "https://pay.stripe.com/receipts/payment/CAcaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KOfBmKEGMgarecoy8cU6LBYTBSk6QLeqixDK3Wp7agsQfREj3vSXJTrg8SjoxhuNjSJzxMcN6QHTlEDG",
  "refunded": false,
  "review": null,
  "shipping": null,
  "source": {
    "id": "card_1MrVHGLkdIwHu7ix7H1PgERt",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "US",
    "customer": null,
    "cvc_check": null,
    "dynamic_last4": null,
    "exp_month": 3,
    "exp_year": 2024,
    "fingerprint": "mToisGZ01V71BCos",
    "funding": "credit",
    "last4": "4242",
    "metadata": {},
    "name": null,
    "tokenization_method": null
  },
  "source_transfer": null,
  "statement_descriptor": null,
  "statement_descriptor_suffix": null,
  "status": "succeeded",
  "transfer_data": null,
  "transfer_group": null
}
```