# The Review object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `billing_zip` (string, nullable)
  The ZIP or postal code of the card used, if applicable.

- `charge` (string, nullable)
  The charge associated with this review.

- `closed_reason` (enum, nullable)
  The reason the review was closed, or null if it has not yet been closed. One of `approved`, `refunded`, `refunded_as_fraud`, `disputed`, `redacted`, `canceled`, `payment_never_settled`, or `acknowledged`.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `ip_address` (string, nullable)
  The IP address where the payment originated.

- `ip_address_location` (object, nullable)
  Information related to the location of the payment. Note that this information is an approximation and attempts to locate the nearest population center - it should not be used to determine a specific address.

  - `ip_address_location.city` (string, nullable)
    The city where the payment originated.

  - `ip_address_location.country` (string, nullable)
    Two-letter ISO code representing the country where the payment originated.

  - `ip_address_location.latitude` (float, nullable)
    The geographic latitude where the payment originated.

  - `ip_address_location.longitude` (float, nullable)
    The geographic longitude where the payment originated.

  - `ip_address_location.region` (string, nullable)
    The state/county/province/region where the payment originated.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `open` (boolean)
  If `true`, the review needs action.

- `opened_reason` (enum)
  The reason the review was opened. One of `rule` or `manual`.
Possible enum values:
  - `manual`
  - `rule`

- `payment_intent` (string, nullable)
  The PaymentIntent ID associated with this review, if one exists.

- `reason` (string)
  The reason the review is currently open or closed. One of `rule`, `manual`, `approved`, `refunded`, `refunded_as_fraud`, `disputed`, `redacted`, `canceled`, `payment_never_settled`, or `acknowledged`.

- `refund_signals` (object, nullable)
  Signals to indicate that the review should be prioritized and a payment refund should be considered.

  - `refund_signals.early_fraud_warning` (string, nullable)
    When present, this signal indicates that the payment associated with the review received an early fraud warning.

  - `refund_signals.recommended_refund` (object, nullable)
    When present, this signal indicates that [Smart Refunds](https://docs.stripe.com/docs/radar/reviews.md#smart-refunds) recommends refunding the payment based on risk signals collected after the payment completed.

- `session` (object, nullable)
  Information related to the browsing session of the user who initiated the payment.

  - `session.browser` (string, nullable)
    The browser used in this browser session (e.g., `Chrome`).

  - `session.device` (string, nullable)
    Information about the device used for the browser session (e.g., `Samsung SM-G930T`).

  - `session.platform` (string, nullable)
    The platform for the browser session (e.g., `Macintosh`).

  - `session.version` (string, nullable)
    The version for the browser session (e.g., `61.0.3163.100`).

### The Review object

```json
{
  "id": "prv_1NVyFt2eZvKYlo2CjubqF1xm",
  "object": "review",
  "billing_zip": null,
  "charge": null,
  "closed_reason": null,
  "created": 1689864901,
  "ip_address": null,
  "ip_address_location": null,
  "livemode": false,
  "open": true,
  "opened_reason": "rule",
  "payment_intent": "pi_3NVy8c2eZvKYlo2C055h7pkd",
  "reason": "rule",
  "session": null
}
```