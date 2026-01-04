# The Invoice Payment object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `amount_paid` (integer, nullable)
  Amount that was actually paid for this invoice, in cents. This field is null until the payment is `paid`. This amount can be less than the `amount_requested` if the PaymentIntent’s `amount_received` is not sufficient to pay all of the invoices that it is attached to.

- `amount_requested` (integer)
  Amount intended to be paid toward this invoice, in cents

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (string)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `invoice` (string)
  The invoice that was paid.

- `is_default` (boolean)
  Stripe automatically creates a default InvoicePayment when the invoice is finalized, and keeps it synchronized with the invoice’s `amount_remaining`. The PaymentIntent associated with the default payment can’t be edited or canceled directly.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `payment` (object)
  The details on the payment.

  - `payment.charge` (string, nullable)
    ID of the successful charge for this payment when `type` is `charge`.Note: charge is only surfaced if the charge object is not associated with a payment intent. If the charge object does have a payment intent, the Invoice Payment surfaces the payment intent instead.

  - `payment.payment_intent` (string, nullable)
    ID of the PaymentIntent associated with this payment when `type` is `payment_intent`. Note: This property is only populated for invoices finalized on or after March 15th, 2019.

  - `payment.payment_record` (string, nullable)
    ID of the PaymentRecord associated with this payment when `type` is `payment_record`.

  - `payment.type` (enum)
    Type of payment object associated with this invoice payment.
Possible enum values:
    - `charge`
    - `payment_intent`
    - `payment_record`

- `status` (string)
  The status of the payment, one of `open`, `paid`, or `canceled`.

- `status_transitions` (object)
  The timestamps when the payment’s status was updated.

  - `status_transitions.canceled_at` (timestamp, nullable)
    The time that the payment was canceled.

  - `status_transitions.paid_at` (timestamp, nullable)
    The time that the payment succeeded.

### The Invoice Payment object

```json
{
  "id": "inpay_1M3USa2eZvKYlo2CBjuwbq0N",
  "object": "invoice_payment",
  "amount_paid": 2000,
  "amount_requested": 2000,
  "created": 1391288554,
  "currency": "usd",
  "invoice": "in_103Q0w2eZvKYlo2C5PYwf6Wf",
  "is_default": true,
  "livemode": false,
  "payment": {
    "type": "payment_intent",
    "payment_intent": "pi_103Q0w2eZvKYlo2C364X582Z"
  },
  "status": "paid",
  "status_transitions": {
    "canceled_at": null,
    "paid_at": 1391288554
  }
}
```