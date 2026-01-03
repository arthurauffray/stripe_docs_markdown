# The Top-up object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `amount` (integer)
  Amount transferred.

- `balance_transaction` (string, nullable)
  ID of the balance transaction that describes the impact of this top-up on your account balance. May not be specified depending on status of top-up.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (string)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `description` (string, nullable)
  An arbitrary string attached to the object. Often useful for displaying to users.

- `expected_availability_date` (integer, nullable)
  Date the funds are expected to arrive in your Stripe account for payouts. This factors in delays like weekends or bank holidays. May not be specified depending on status of top-up.

- `failure_code` (string, nullable)
  Error code explaining reason for top-up failure if available (see [the errors section](https://docs.stripe.com/docs/api.md#errors) for a list of codes).

- `failure_message` (string, nullable)
  Message to user further explaining reason for top-up failure if available.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `source` (object, nullable)
  The source field is deprecated. It might not always be present in the API response.

  - `source.id` (string)
    Unique identifier for the object.

  - `source.object` (string)
    String representing the object’s type. Objects of the same type share the same value.

  - `source.allow_redisplay` (enum, nullable)
    This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow. The field defaults to “unspecified”.
Possible enum values:
    - `always`
      Use `always` to indicate that this payment method can always be shown to a customer in a checkout flow.

    - `limited`
      Use `limited` to indicate that this payment method can’t always be shown to a customer in a checkout flow. For example, it can only be shown in the context of a specific subscription.

    - `unspecified`
      This is the default value for payment methods where `allow_redisplay` wasn’t set.

  - `source.amount` (integer, nullable)
    A positive integer in the smallest currency unit (that is, 100 cents for $1.00, or 1 for ¥1, Japanese Yen being a zero-decimal currency) representing the total amount associated with the source. This is the amount for which the source will be chargeable once ready. Required for `single_use` sources.

  - `source.client_secret` (string)
    The client secret of the source. Used for client-side retrieval using a publishable key.

  - `source.code_verification` (object, nullable)
    Information related to the code verification flow. Present if the source is authenticated by a verification code (`flow` is `code_verification`).

    - `source.code_verification.attempts_remaining` (integer)
      The number of attempts remaining to authenticate the source object with a verification code.

    - `source.code_verification.status` (string)
      The status of the code verification, either `pending` (awaiting verification, `attempts_remaining` should be greater than 0), `succeeded` (successful verification) or `failed` (failed verification, cannot be verified anymore as `attempts_remaining` should be 0).

  - `source.created` (timestamp)
    Time at which the object was created. Measured in seconds since the Unix epoch.

  - `source.currency` (enum, nullable)
    Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) associated with the source. This is the currency for which the source will be chargeable once ready. Required for `single_use` sources.

  - `source.customer` (string, nullable)
    The ID of the customer to which this source is attached. This will not be present when the source has not been attached to a customer.

  - `source.flow` (string)
    The authentication `flow` of the source. `flow` is one of `redirect`, `receiver`, `code_verification`, `none`.

  - `source.livemode` (boolean)
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

  - `source.metadata` (object, nullable)
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

  - `source.owner` (object, nullable)
    Information about the owner of the payment instrument that may be used or required by particular source types.

    - `source.owner.address` (object, nullable)
      Owner’s address.

      - `source.owner.address.city` (string, nullable)
        City, district, suburb, town, or village.

      - `source.owner.address.country` (string, nullable)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `source.owner.address.line1` (string, nullable)
        Address line 1, such as the street, PO Box, or company name.

      - `source.owner.address.line2` (string, nullable)
        Address line 2, such as the apartment, suite, unit, or building.

      - `source.owner.address.postal_code` (string, nullable)
        ZIP or postal code.

      - `source.owner.address.state` (string, nullable)
        State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

    - `source.owner.email` (string, nullable)
      Owner’s email address.

    - `source.owner.name` (string, nullable)
      Owner’s full name.

    - `source.owner.phone` (string, nullable)
      Owner’s phone number (including extension).

    - `source.owner.verified_address` (object, nullable)
      Verified owner’s address. Verified values are verified or provided by the payment method directly (and if supported) at the time of authorization or settlement. They cannot be set or mutated.

      - `source.owner.verified_address.city` (string, nullable)
        City, district, suburb, town, or village.

      - `source.owner.verified_address.country` (string, nullable)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `source.owner.verified_address.line1` (string, nullable)
        Address line 1, such as the street, PO Box, or company name.

      - `source.owner.verified_address.line2` (string, nullable)
        Address line 2, such as the apartment, suite, unit, or building.

      - `source.owner.verified_address.postal_code` (string, nullable)
        ZIP or postal code.

      - `source.owner.verified_address.state` (string, nullable)
        State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

    - `source.owner.verified_email` (string, nullable)
      Verified owner’s email address. Verified values are verified or provided by the payment method directly (and if supported) at the time of authorization or settlement. They cannot be set or mutated.

    - `source.owner.verified_name` (string, nullable)
      Verified owner’s full name. Verified values are verified or provided by the payment method directly (and if supported) at the time of authorization or settlement. They cannot be set or mutated.

    - `source.owner.verified_phone` (string, nullable)
      Verified owner’s phone number (including extension). Verified values are verified or provided by the payment method directly (and if supported) at the time of authorization or settlement. They cannot be set or mutated.

  - `source.receiver` (object, nullable)
    Information related to the receiver flow. Present if the source is a receiver (`flow` is `receiver`).

    - `source.receiver.address` (string, nullable)
      The address of the receiver source. This is the value that should be communicated to the customer to send their funds to.

    - `source.receiver.amount_charged` (integer)
      The total amount that was moved to your balance. This is almost always equal to the amount charged. In rare cases when customers deposit excess funds and we are unable to refund those, those funds get moved to your balance and show up in amount_charged as well. The amount charged is expressed in the source’s currency.

    - `source.receiver.amount_received` (integer)
      The total amount received by the receiver source. `amount_received = amount_returned + amount_charged` should be true for consumed sources unless customers deposit excess funds. The amount received is expressed in the source’s currency.

    - `source.receiver.amount_returned` (integer)
      The total amount that was returned to the customer. The amount returned is expressed in the source’s currency.

    - `source.receiver.refund_attributes_method` (string)
      Type of refund attribute method, one of `email`, `manual`, or `none`.

    - `source.receiver.refund_attributes_status` (string)
      Type of refund attribute status, one of `missing`, `requested`, or `available`.

  - `source.redirect` (object, nullable)
    Information related to the redirect flow. Present if the source is authenticated by a redirect (`flow` is `redirect`).

    - `source.redirect.failure_reason` (string, nullable)
      The failure reason for the redirect, either `user_abort` (the customer aborted or dropped out of the redirect flow), `declined` (the authentication failed or the transaction was declined), or `processing_error` (the redirect failed due to a technical error). Present only if the redirect status is `failed`.

    - `source.redirect.return_url` (string)
      The URL you provide to redirect the customer to after they authenticated their payment.

    - `source.redirect.status` (string)
      The status of the redirect, either `pending` (ready to be used by your customer to authenticate the transaction), `succeeded` (successful authentication, cannot be reused) or `not_required` (redirect should not be used) or `failed` (failed authentication, cannot be reused).

    - `source.redirect.url` (string)
      The URL provided to you to redirect a customer to as part of a `redirect` authentication flow.

  - `source.source_order` (object, nullable)
    Information about the items and shipping associated with the source. Required for transactional credit (for example Klarna) sources before you can charge it.

    - `source.source_order.amount` (integer)
      A positive integer in the smallest currency unit (that is, 100 cents for $1.00, or 1 for ¥1, Japanese Yen being a zero-decimal currency) representing the total amount for the order.

    - `source.source_order.currency` (enum)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

    - `source.source_order.email` (string, nullable)
      The email address of the customer placing the order.

    - `source.source_order.items` (array of objects, nullable)
      List of items constituting the order.

      - `source.source_order.items.amount` (integer, nullable)
        The amount (price) for this order item.

      - `source.source_order.items.currency` (string, nullable)
        This currency of this order item. Required when `amount` is present.

      - `source.source_order.items.description` (string, nullable)
        Human-readable description for this order item.

      - `source.source_order.items.parent` (string, nullable)
        The ID of the associated object for this line item. Expandable if not null (e.g., expandable to a SKU).

      - `source.source_order.items.quantity` (integer, nullable)
        The quantity of this order item. When type is `sku`, this is the number of instances of the SKU to be ordered.

      - `source.source_order.items.type` (string, nullable)
        The type of this order item. Must be `sku`, `tax`, or `shipping`.

    - `source.source_order.shipping` (object, nullable)
      The shipping address for the order. Present if the order is for goods to be shipped.

      - `source.source_order.shipping.address` (object, nullable)
        Shipping address.

        - `source.source_order.shipping.address.city` (string, nullable)
          City, district, suburb, town, or village.

        - `source.source_order.shipping.address.country` (string, nullable)
          Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

        - `source.source_order.shipping.address.line1` (string, nullable)
          Address line 1, such as the street, PO Box, or company name.

        - `source.source_order.shipping.address.line2` (string, nullable)
          Address line 2, such as the apartment, suite, unit, or building.

        - `source.source_order.shipping.address.postal_code` (string, nullable)
          ZIP or postal code.

        - `source.source_order.shipping.address.state` (string, nullable)
          State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

      - `source.source_order.shipping.carrier` (string, nullable)
        The delivery service that shipped a physical product, such as Fedex, UPS, USPS, etc.

      - `source.source_order.shipping.name` (string, nullable)
        Recipient name.

      - `source.source_order.shipping.phone` (string, nullable)
        Recipient phone (including extension).

      - `source.source_order.shipping.tracking_number` (string, nullable)
        The tracking number for a physical product, obtained from the delivery service. If multiple tracking numbers were generated for this purchase, please separate them with commas.

  - `source.statement_descriptor` (string, nullable)
    Extra information about a source. This will appear on your customer’s statement every time you charge the source.

  - `source.status` (string)
    The status of the source, one of `canceled`, `chargeable`, `consumed`, `failed`, or `pending`. Only `chargeable` sources can be used to create a charge.

  - `source.type` (enum)
    The `type` of the source. The `type` is a payment method, one of `ach_credit_transfer`, `ach_debit`, `alipay`, `bancontact`, `card`, `card_present`, `eps`, `giropay`, `ideal`, `multibanco`, `klarna`, `p24`, `sepa_debit`, `sofort`, `three_d_secure`, or `wechat`. An additional hash is included on the source with a name matching this value. It contains additional information specific to the [payment method](https://docs.stripe.com/docs/sources.md) used.
Possible enum values:
    - `ach_credit_transfer`
    - `ach_debit`
    - `alipay`
    - `bancontact`
    - `card`
    - `card_present`
    - `eps`
    - `giropay`
    - `ideal`
    - `klarna`
    - `multibanco`
    - `p24`
    - `sepa_debit`
    - `sofort`
    - `three_d_secure`
    - `wechat`

  - `source.usage` (string, nullable)
    Either `reusable` or `single_use`. Whether this source should be reusable or not. Some source types may or may not be reusable by construction, while others may leave the option at creation. If an incompatible value is passed, an error will be returned.

- `statement_descriptor` (string, nullable)
  Extra information about a top-up. This will appear on your source’s bank statement. It must contain at least one letter.

- `status` (enum)
  The status of the top-up is either `canceled`, `failed`, `pending`, `reversed`, or `succeeded`.
Possible enum values:
  - `canceled`
  - `failed`
  - `pending`
  - `reversed`
  - `succeeded`

- `transfer_group` (string, nullable)
  A string that identifies this top-up as part of a group.

### The Top-up object

```json
{
  "id": "tu_1NG6yj2eZvKYlo2C1FOBiHya",
  "object": "topup",
  "amount": 2000,
  "balance_transaction": null,
  "created": 123456789,
  "currency": "usd",
  "description": "Top-up for Jenny Rosen",
  "expected_availability_date": 123456789,
  "failure_code": null,
  "failure_message": null,
  "livemode": false,
  "source": null,
  "statement_descriptor": "Top-up",
  "status": "pending",
  "transfer_group": null
}
```