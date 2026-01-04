# The PaymentMethodDomain object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `amazon_pay` (object)
  The status of Amazon Pay’s eligibility on the domain.

  - `amazon_pay.status` (enum)
    The status of the payment method on the domain.
Possible enum values:
    - `active`
      The payment method is eligible for use on this domain. To display this payment method on the domain, make sure it’s also enabled in your Stripe account. Learn more about [payment methods](https://docs.stripe.com/docs/payments/payment-methods/overview.md).

    - `inactive`
      The payment method isn’t eligible for use on this domain.

  - `amazon_pay.status_details` (object, nullable)
    Additional details about the status of the payment method on the domain.

    - `amazon_pay.status_details.error_message` (string)
      The error message associated with the status of the payment method on the domain.

- `apple_pay` (object)
  The status of Apple Pay’s eligibility on the domain.

  - `apple_pay.status` (enum)
    The status of the payment method on the domain.
Possible enum values:
    - `active`
      The payment method is eligible for use on this domain. To display this payment method on the domain, make sure it’s also enabled in your Stripe account. Learn more about [payment methods](https://docs.stripe.com/docs/payments/payment-methods/overview.md).

    - `inactive`
      The payment method isn’t eligible for use on this domain.

  - `apple_pay.status_details` (object, nullable)
    Additional details about the status of the payment method on the domain.

    - `apple_pay.status_details.error_message` (string)
      The error message associated with the status of the payment method on the domain.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `domain_name` (string)
  The domain name that this payment method domain object represents.

- `enabled` (boolean)
  Whether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements.

- `google_pay` (object)
  The status of Google Pay’s eligibility on the domain.

  - `google_pay.status` (enum)
    The status of the payment method on the domain.
Possible enum values:
    - `active`
      The payment method is eligible for use on this domain. To display this payment method on the domain, make sure it’s also enabled in your Stripe account. Learn more about [payment methods](https://docs.stripe.com/docs/payments/payment-methods/overview.md).

    - `inactive`
      The payment method isn’t eligible for use on this domain.

  - `google_pay.status_details` (object, nullable)
    Additional details about the status of the payment method on the domain.

    - `google_pay.status_details.error_message` (string)
      The error message associated with the status of the payment method on the domain.

- `klarna` (object)
  The status of Klarna’s eligibility on the domain.

  - `klarna.status` (enum)
    The status of the payment method on the domain.
Possible enum values:
    - `active`
      The payment method is eligible for use on this domain. To display this payment method on the domain, make sure it’s also enabled in your Stripe account. Learn more about [payment methods](https://docs.stripe.com/docs/payments/payment-methods/overview.md).

    - `inactive`
      The payment method isn’t eligible for use on this domain.

  - `klarna.status_details` (object, nullable)
    Additional details about the status of the payment method on the domain.

    - `klarna.status_details.error_message` (string)
      The error message associated with the status of the payment method on the domain.

- `link` (object)
  The status of Link’s eligibility on the domain.

  - `link.status` (enum)
    The status of the payment method on the domain.
Possible enum values:
    - `active`
      The payment method is eligible for use on this domain. To display this payment method on the domain, make sure it’s also enabled in your Stripe account. Learn more about [payment methods](https://docs.stripe.com/docs/payments/payment-methods/overview.md).

    - `inactive`
      The payment method isn’t eligible for use on this domain.

  - `link.status_details` (object, nullable)
    Additional details about the status of the payment method on the domain.

    - `link.status_details.error_message` (string)
      The error message associated with the status of the payment method on the domain.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `paypal` (object)
  The status of PayPal’s eligibility on the domain.

  - `paypal.status` (enum)
    The status of the payment method on the domain.
Possible enum values:
    - `active`
      The payment method is eligible for use on this domain. To display this payment method on the domain, make sure it’s also enabled in your Stripe account. Learn more about [payment methods](https://docs.stripe.com/docs/payments/payment-methods/overview.md).

    - `inactive`
      The payment method isn’t eligible for use on this domain.

  - `paypal.status_details` (object, nullable)
    Additional details about the status of the payment method on the domain.

    - `paypal.status_details.error_message` (string)
      The error message associated with the status of the payment method on the domain.

### The PaymentMethodDomain object

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