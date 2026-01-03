# The Refund object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `amount` (integer)
  Amount, in cents.

- `balance_transaction` (string, nullable)
  Balance transaction that describes the impact on your account balance.

- `charge` (string, nullable)
  ID of the charge that’s refunded.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (enum)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `description` (string, nullable)
  An arbitrary string attached to the object. You can use this for displaying to users (available on non-card refunds only).

- `destination_details` (object, nullable)
  Transaction-specific details for the refund.

  - `destination_details.affirm` (object, nullable)
    If this is a `affirm` refund, this hash contains the transaction specific details of the `affirm` refund method.

  - `destination_details.afterpay_clearpay` (object, nullable)
    If this is a `afterpay_clearpay` refund, this hash contains the transaction specific details of the `afterpay_clearpay` refund method.

  - `destination_details.alipay` (object, nullable)
    If this is a `alipay` refund, this hash contains the transaction specific details of the `alipay` refund method.

  - `destination_details.alma` (object, nullable)
    If this is a `alma` refund, this hash contains the transaction specific details of the `alma` refund method.

  - `destination_details.amazon_pay` (object, nullable)
    If this is a `amazon_pay` refund, this hash contains the transaction specific details of the `amazon_pay` refund method.

  - `destination_details.au_bank_transfer` (object, nullable)
    If this is a `au_bank_transfer` refund, this hash contains the transaction specific details of the `au_bank_transfer` refund method.

  - `destination_details.blik` (object, nullable)
    If this is a `blik` refund, this hash contains the transaction specific details of the `blik` refund method.

    - `destination_details.blik.network_decline_code` (string, nullable)
      For refunds declined by the network, a decline code provided by the network which indicates the reason the refund failed.

    - `destination_details.blik.reference` (string, nullable)
      The reference assigned to the refund.

    - `destination_details.blik.reference_status` (string, nullable)
      Status of the reference on the refund. This can be `pending`, `available` or `unavailable`.

  - `destination_details.br_bank_transfer` (object, nullable)
    If this is a `br_bank_transfer` refund, this hash contains the transaction specific details of the `br_bank_transfer` refund method.

    - `destination_details.br_bank_transfer.reference` (string, nullable)
      The reference assigned to the refund.

    - `destination_details.br_bank_transfer.reference_status` (string, nullable)
      Status of the reference on the refund. This can be `pending`, `available` or `unavailable`.

  - `destination_details.card` (object, nullable)
    If this is a `card` refund, this hash contains the transaction specific details of the `card` refund method.

    - `destination_details.card.reference` (string, nullable)
      Value of the reference number assigned to the refund.

    - `destination_details.card.reference_status` (string, nullable)
      Status of the reference number on the refund. This can be `pending`, `available` or `unavailable`.

    - `destination_details.card.reference_type` (string, nullable)
      Type of the reference number assigned to the refund.

    - `destination_details.card.type` (enum)
      The type of refund. This can be `refund`, `reversal`, or `pending`.
Possible enum values:
      - `pending`
        The refund is still processing and its type is not confirmed yet.

      - `refund`
        The refund will show as a credit entry on the bank statement.

      - `reversal`
        The refund goes through as a reversal. The original charge will drop off the bank statement altogether.

  - `destination_details.cashapp` (object, nullable)
    If this is a `cashapp` refund, this hash contains the transaction specific details of the `cashapp` refund method.

  - `destination_details.crypto` (object, nullable)
    If this is a `crypto` refund, this hash contains the transaction specific details of the `crypto` refund method.

    - `destination_details.crypto.reference` (string, nullable)
      The transaction hash of the refund.

  - `destination_details.customer_cash_balance` (object, nullable)
    If this is a `customer_cash_balance` refund, this hash contains the transaction specific details of the `customer_cash_balance` refund method.

  - `destination_details.eps` (object, nullable)
    If this is a `eps` refund, this hash contains the transaction specific details of the `eps` refund method.

  - `destination_details.eu_bank_transfer` (object, nullable)
    If this is a `eu_bank_transfer` refund, this hash contains the transaction specific details of the `eu_bank_transfer` refund method.

    - `destination_details.eu_bank_transfer.reference` (string, nullable)
      The reference assigned to the refund.

    - `destination_details.eu_bank_transfer.reference_status` (string, nullable)
      Status of the reference on the refund. This can be `pending`, `available` or `unavailable`.

  - `destination_details.gb_bank_transfer` (object, nullable)
    If this is a `gb_bank_transfer` refund, this hash contains the transaction specific details of the `gb_bank_transfer` refund method.

    - `destination_details.gb_bank_transfer.reference` (string, nullable)
      The reference assigned to the refund.

    - `destination_details.gb_bank_transfer.reference_status` (string, nullable)
      Status of the reference on the refund. This can be `pending`, `available` or `unavailable`.

  - `destination_details.giropay` (object, nullable)
    If this is a `giropay` refund, this hash contains the transaction specific details of the `giropay` refund method.

  - `destination_details.grabpay` (object, nullable)
    If this is a `grabpay` refund, this hash contains the transaction specific details of the `grabpay` refund method.

  - `destination_details.jp_bank_transfer` (object, nullable)
    If this is a `jp_bank_transfer` refund, this hash contains the transaction specific details of the `jp_bank_transfer` refund method.

    - `destination_details.jp_bank_transfer.reference` (string, nullable)
      The reference assigned to the refund.

    - `destination_details.jp_bank_transfer.reference_status` (string, nullable)
      Status of the reference on the refund. This can be `pending`, `available` or `unavailable`.

  - `destination_details.klarna` (object, nullable)
    If this is a `klarna` refund, this hash contains the transaction specific details of the `klarna` refund method.

  - `destination_details.mb_way` (object, nullable)
    If this is a `mb_way` refund, this hash contains the transaction specific details of the `mb_way` refund method.

    - `destination_details.mb_way.reference` (string, nullable)
      The reference assigned to the refund.

    - `destination_details.mb_way.reference_status` (string, nullable)
      Status of the reference on the refund. This can be `pending`, `available` or `unavailable`.

  - `destination_details.multibanco` (object, nullable)
    If this is a `multibanco` refund, this hash contains the transaction specific details of the `multibanco` refund method.

    - `destination_details.multibanco.reference` (string, nullable)
      The reference assigned to the refund.

    - `destination_details.multibanco.reference_status` (string, nullable)
      Status of the reference on the refund. This can be `pending`, `available` or `unavailable`.

  - `destination_details.mx_bank_transfer` (object, nullable)
    If this is a `mx_bank_transfer` refund, this hash contains the transaction specific details of the `mx_bank_transfer` refund method.

    - `destination_details.mx_bank_transfer.reference` (string, nullable)
      The reference assigned to the refund.

    - `destination_details.mx_bank_transfer.reference_status` (string, nullable)
      Status of the reference on the refund. This can be `pending`, `available` or `unavailable`.

  - `destination_details.nz_bank_transfer` (object, nullable)
    If this is a `nz_bank_transfer` refund, this hash contains the transaction specific details of the `nz_bank_transfer` refund method.

  - `destination_details.p24` (object, nullable)
    If this is a `p24` refund, this hash contains the transaction specific details of the `p24` refund method.

    - `destination_details.p24.reference` (string, nullable)
      The reference assigned to the refund.

    - `destination_details.p24.reference_status` (string, nullable)
      Status of the reference on the refund. This can be `pending`, `available` or `unavailable`.

  - `destination_details.paynow` (object, nullable)
    If this is a `paynow` refund, this hash contains the transaction specific details of the `paynow` refund method.

  - `destination_details.paypal` (object, nullable)
    If this is a `paypal` refund, this hash contains the transaction specific details of the `paypal` refund method.

    - `destination_details.paypal.network_decline_code` (string, nullable)
      For refunds declined by the network, a decline code provided by the network which indicates the reason the refund failed.

  - `destination_details.pix` (object, nullable)
    If this is a `pix` refund, this hash contains the transaction specific details of the `pix` refund method.

  - `destination_details.revolut` (object, nullable)
    If this is a `revolut` refund, this hash contains the transaction specific details of the `revolut` refund method.

  - `destination_details.sofort` (object, nullable)
    If this is a `sofort` refund, this hash contains the transaction specific details of the `sofort` refund method.

  - `destination_details.swish` (object, nullable)
    If this is a `swish` refund, this hash contains the transaction specific details of the `swish` refund method.

    - `destination_details.swish.network_decline_code` (string, nullable)
      For refunds declined by the network, a decline code provided by the network which indicates the reason the refund failed.

    - `destination_details.swish.reference` (string, nullable)
      The reference assigned to the refund.

    - `destination_details.swish.reference_status` (string, nullable)
      Status of the reference on the refund. This can be `pending`, `available` or `unavailable`.

  - `destination_details.th_bank_transfer` (object, nullable)
    If this is a `th_bank_transfer` refund, this hash contains the transaction specific details of the `th_bank_transfer` refund method.

    - `destination_details.th_bank_transfer.reference` (string, nullable)
      The reference assigned to the refund.

    - `destination_details.th_bank_transfer.reference_status` (string, nullable)
      Status of the reference on the refund. This can be `pending`, `available` or `unavailable`.

  - `destination_details.twint` (object, nullable)
    If this is a `twint` refund, this hash contains the transaction specific details of the `twint` refund method.

  - `destination_details.type` (string)
    The type of transaction-specific details of the payment method used in the refund (e.g., `card`). An additional hash is included on `destination_details` with a name matching this value. It contains information specific to the refund transaction.

  - `destination_details.us_bank_transfer` (object, nullable)
    If this is a `us_bank_transfer` refund, this hash contains the transaction specific details of the `us_bank_transfer` refund method.

    - `destination_details.us_bank_transfer.reference` (string, nullable)
      The reference assigned to the refund.

    - `destination_details.us_bank_transfer.reference_status` (string, nullable)
      Status of the reference on the refund. This can be `pending`, `available` or `unavailable`.

  - `destination_details.wechat_pay` (object, nullable)
    If this is a `wechat_pay` refund, this hash contains the transaction specific details of the `wechat_pay` refund method.

  - `destination_details.zip` (object, nullable)
    If this is a `zip` refund, this hash contains the transaction specific details of the `zip` refund method.

- `failure_balance_transaction` (string, nullable)
  After the refund fails, this balance transaction describes the adjustment made on your account balance that reverses the initial balance transaction.

- `failure_reason` (string, nullable)
  Provides the reason for the refund failure. Possible values are: `lost_or_stolen_card`, `expired_or_canceled_card`, `charge_for_pending_refund_disputed`, `insufficient_funds`, `declined`, `merchant_request`, or `unknown`.

- `instructions_email` (string, nullable)
  For payment methods without native refund support (for example, Konbini, PromptPay), provide an email address for the customer to receive refund instructions.

- `metadata` (object, nullable)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `next_action` (object, nullable)
  If the refund has a status of `requires_action`, this property describes what the refund needs to continue processing.

  - `next_action.display_details` (object, nullable)
    Contains the refund details.

    - `next_action.display_details.email_sent` (object)
      Contains information about the email sent to the customer.

      - `next_action.display_details.email_sent.email_sent_at` (timestamp)
        The timestamp when the email was sent.

      - `next_action.display_details.email_sent.email_sent_to` (string)
        The recipient’s email address.

    - `next_action.display_details.expires_at` (timestamp)
      The expiry timestamp.

  - `next_action.type` (string)
    Type of the next action to perform.

- `payment_intent` (string, nullable)
  ID of the PaymentIntent that’s refunded.

- `pending_reason` (enum, nullable)
  Provides the reason for why the refund is pending. Possible values are: `processing`, `insufficient_funds`, or `charge_pending`.

- `reason` (enum, nullable)
  Reason for the refund, which is either user-provided (`duplicate`, `fraudulent`, or `requested_by_customer`) or generated by Stripe internally (`expired_uncaptured_charge`).

- `receipt_number` (string, nullable)
  This is the transaction number that appears on email receipts sent for this refund.

- `source_transfer_reversal` (string, nullable)
  The transfer reversal that’s associated with the refund. Only present if the charge came from another Stripe account.

- `status` (string, nullable)
  Status of the refund. This can be `pending`, `requires_action`, `succeeded`, `failed`, or `canceled`. Learn more about [failed refunds](https://docs.stripe.com/docs/refunds.md#failed-refunds).

- `transfer_reversal` (string, nullable)
  This refers to the transfer reversal object if the accompanying transfer reverses. This is only applicable if the charge was created using the destination parameter.

### The Refund object

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