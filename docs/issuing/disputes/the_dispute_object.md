# The Dispute object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `amount` (integer)
  Disputed amount in the card’s currency and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal). Usually the amount of the `transaction`, but can differ (usually because of currency fluctuation).

- `balance_transactions` (array of objects, nullable)
  List of balance transactions associated with the dispute.

  - `balance_transactions.id` (string)
    Unique identifier for the object.

  - `balance_transactions.object` (string)
    String representing the object’s type. Objects of the same type share the same value.

  - `balance_transactions.amount` (integer)
    Gross amount of this transaction (in cents). A positive value represents funds charged to another party, and a negative value represents funds sent to another party.

  - `balance_transactions.available_on` (timestamp)
    The date that the transaction’s net funds become available in the Stripe balance.

  - `balance_transactions.balance_type` (enum)
    The balance that this transaction impacts.
Possible enum values:
    - `issuing`
      Balance Transactions that affect your Issuing balance

    - `payments`
      Balance Transactions that affect your Payments balance

    - `refund_and_dispute_prefunding`
      Balance Transactions that affect your Refund and Dispute Prefunding balance

  - `balance_transactions.created` (timestamp)
    Time at which the object was created. Measured in seconds since the Unix epoch.

  - `balance_transactions.currency` (enum)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `balance_transactions.description` (string, nullable)
    An arbitrary string attached to the object. Often useful for displaying to users.

  - `balance_transactions.exchange_rate` (float, nullable)
    If applicable, this transaction uses an exchange rate. If money converts from currency A to currency B, then the `amount` in currency A, multipled by the `exchange_rate`, equals the `amount` in currency B. For example, if you charge a customer 10.00 EUR, the PaymentIntent’s `amount` is `1000` and `currency` is `eur`. If this converts to 12.34 USD in your Stripe account, the BalanceTransaction’s `amount` is `1234`, its `currency` is `usd`, and the `exchange_rate` is `1.234`.

  - `balance_transactions.fee` (integer)
    Fees (in cents) paid for this transaction. Represented as a positive integer when assessed.

  - `balance_transactions.fee_details` (array of objects)
    Detailed breakdown of fees (in cents) paid for this transaction.

    - `balance_transactions.fee_details.amount` (integer)
      Amount of the fee, in cents.

    - `balance_transactions.fee_details.application` (string, nullable)
      ID of the Connect application that earned the fee.

    - `balance_transactions.fee_details.currency` (enum)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

    - `balance_transactions.fee_details.description` (string, nullable)
      An arbitrary string attached to the object. Often useful for displaying to users.

    - `balance_transactions.fee_details.type` (string)
      Type of the fee, one of: `application_fee`, `payment_method_passthrough_fee`, `stripe_fee` or `tax`.

  - `balance_transactions.net` (integer)
    Net impact to a Stripe balance (in cents). A positive value represents incrementing a Stripe balance, and a negative value decrementing a Stripe balance. You can calculate the net impact of a transaction on a balance by `amount` - `fee`

  - `balance_transactions.reporting_category` (string)
    Learn more about how [reporting categories](https://stripe.com/docs/reports/reporting-categories) can help you understand balance transactions from an accounting perspective.

  - `balance_transactions.source` (string, nullable)
    This transaction relates to the Stripe object.

  - `balance_transactions.status` (string)
    The transaction’s net funds status in the Stripe balance, which are either `available` or `pending`.

  - `balance_transactions.type` (enum)
    Transaction type: `adjustment`, `advance`, `advance_funding`, `anticipation_repayment`, `application_fee`, `application_fee_refund`, `charge`, `climate_order_purchase`, `climate_order_refund`, `connect_collection_transfer`, `contribution`, `issuing_authorization_hold`, `issuing_authorization_release`, `issuing_dispute`, `issuing_transaction`, `obligation_outbound`, `obligation_reversal_inbound`, `payment`, `payment_failure_refund`, `payment_network_reserve_hold`, `payment_network_reserve_release`, `payment_refund`, `payment_reversal`, `payment_unreconciled`, `payout`, `payout_cancel`, `payout_failure`, `payout_minimum_balance_hold`, `payout_minimum_balance_release`, `refund`, `refund_failure`, `reserve_transaction`, `reserved_funds`, `stripe_fee`, `stripe_fx_fee`, `stripe_balance_payment_debit`, `stripe_balance_payment_debit_reversal`, `tax_fee`, `topup`, `topup_reversal`, `transfer`, `transfer_cancel`, `transfer_failure`, or `transfer_refund`. Learn more about [balance transaction types and what they represent](https://stripe.com/docs/reports/balance-transaction-types). To classify transactions for accounting purposes, consider `reporting_category` instead.
Possible enum values:
    - `adjustment`
    - `advance`
    - `advance_funding`
    - `anticipation_repayment`
    - `application_fee`
    - `application_fee_refund`
    - `charge`
    - `climate_order_purchase`
    - `climate_order_refund`
    - `connect_collection_transfer`
    - `contribution`
    - `issuing_authorization_hold`
    - `issuing_authorization_release`
    - `issuing_dispute`
    - `issuing_transaction`
    - `obligation_outbound`
    - `obligation_reversal_inbound`
    - `payment`
    - `payment_failure_refund`
    - `payment_network_reserve_hold`
    - `payment_network_reserve_release`
    - `payment_refund`
    - `payment_reversal`
    - `payment_unreconciled`
    - `payout`
    - `payout_cancel`
    - `payout_failure`
    - `payout_minimum_balance_hold`
    - `payout_minimum_balance_release`
    - `refund`
    - `refund_failure`
    - `reserve_transaction`
    - `reserved_funds`
    - `stripe_balance_payment_debit`
    - `stripe_balance_payment_debit_reversal`
    - `stripe_fee`
    - `stripe_fx_fee`
    - `tax_fee`
    - `topup`
    - `topup_reversal`
    - `transfer`
    - `transfer_cancel`
    - `transfer_failure`
    - `transfer_refund`

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (enum)
  The currency the `transaction` was made in.

- `evidence` (object)
  Evidence for the dispute. Evidence contains exactly two non-null fields: the `reason` for the dispute and the associated evidence field for the selected `reason`.

  - `evidence.canceled` (object, nullable)
    Evidence provided when `reason` is ‘canceled’.

    - `evidence.canceled.additional_documentation` (string, nullable)
      (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.

    - `evidence.canceled.canceled_at` (timestamp, nullable)
      Date when order was canceled.

    - `evidence.canceled.cancellation_policy_provided` (boolean, nullable)
      Whether the cardholder was provided with a cancellation policy.

    - `evidence.canceled.cancellation_reason` (string, nullable)
      Reason for canceling the order.

    - `evidence.canceled.expected_at` (timestamp, nullable)
      Date when the cardholder expected to receive the product.

    - `evidence.canceled.explanation` (string, nullable)
      Explanation of why the cardholder is disputing this transaction.

    - `evidence.canceled.product_description` (string, nullable)
      Description of the merchandise or service that was purchased.

    - `evidence.canceled.product_type` (enum, nullable)
      Whether the product was a merchandise or service.
Possible enum values:
      - `merchandise`
        Tangible goods such as groceries and furniture.

      - `service`
        Intangible goods such as domain name registration, flights and lessons.

    - `evidence.canceled.return_status` (enum, nullable)
      Result of cardholder’s attempt to return the product.
Possible enum values:
      - `merchant_rejected`
        The merchant rejected the return.

      - `successful`
        The merchant accepted the return.

    - `evidence.canceled.returned_at` (timestamp, nullable)
      Date when the product was returned or attempted to be returned.

  - `evidence.duplicate` (object, nullable)
    Evidence provided when `reason` is ‘duplicate’.

    - `evidence.duplicate.additional_documentation` (string, nullable)
      (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.

    - `evidence.duplicate.card_statement` (string, nullable)
      (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Copy of the card statement showing that the product had already been paid for.

    - `evidence.duplicate.cash_receipt` (string, nullable)
      (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Copy of the receipt showing that the product had been paid for in cash.

    - `evidence.duplicate.check_image` (string, nullable)
      (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Image of the front and back of the check that was used to pay for the product.

    - `evidence.duplicate.explanation` (string, nullable)
      Explanation of why the cardholder is disputing this transaction.

    - `evidence.duplicate.original_transaction` (string, nullable)
      Transaction (e.g., ipi_…) that the disputed transaction is a duplicate of. Of the two or more transactions that are copies of each other, this is original undisputed one.

  - `evidence.fraudulent` (object, nullable)
    Evidence provided when `reason` is ‘fraudulent’.

    - `evidence.fraudulent.additional_documentation` (string, nullable)
      (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.

    - `evidence.fraudulent.explanation` (string, nullable)
      Explanation of why the cardholder is disputing this transaction.

  - `evidence.merchandise_not_as_described` (object, nullable)
    Evidence provided when `reason` is ‘merchandise_not_as_described’.

    - `evidence.merchandise_not_as_described.additional_documentation` (string, nullable)
      (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.

    - `evidence.merchandise_not_as_described.explanation` (string, nullable)
      Explanation of why the cardholder is disputing this transaction.

    - `evidence.merchandise_not_as_described.received_at` (timestamp, nullable)
      Date when the product was received.

    - `evidence.merchandise_not_as_described.return_description` (string, nullable)
      Description of the cardholder’s attempt to return the product.

    - `evidence.merchandise_not_as_described.return_status` (enum, nullable)
      Result of cardholder’s attempt to return the product.
Possible enum values:
      - `merchant_rejected`
        The merchant rejected the return.

      - `successful`
        The merchant accepted the return.

    - `evidence.merchandise_not_as_described.returned_at` (timestamp, nullable)
      Date when the product was returned or attempted to be returned.

  - `evidence.no_valid_authorization` (object, nullable)
    Evidence provided when `reason` is ‘no_valid_authorization’.

    - `evidence.no_valid_authorization.additional_documentation` (string, nullable)
      (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.

    - `evidence.no_valid_authorization.explanation` (string, nullable)
      Explanation of why the cardholder is disputing this transaction.

  - `evidence.not_received` (object, nullable)
    Evidence provided when `reason` is ‘not_received’.

    - `evidence.not_received.additional_documentation` (string, nullable)
      (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.

    - `evidence.not_received.expected_at` (timestamp, nullable)
      Date when the cardholder expected to receive the product.

    - `evidence.not_received.explanation` (string, nullable)
      Explanation of why the cardholder is disputing this transaction.

    - `evidence.not_received.product_description` (string, nullable)
      Description of the merchandise or service that was purchased.

    - `evidence.not_received.product_type` (enum, nullable)
      Whether the product was a merchandise or service.
Possible enum values:
      - `merchandise`
        Tangible goods such as groceries and furniture.

      - `service`
        Intangible goods such as domain name registration, flights and lessons.

  - `evidence.other` (object, nullable)
    Evidence provided when `reason` is ‘other’.

    - `evidence.other.additional_documentation` (string, nullable)
      (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.

    - `evidence.other.explanation` (string, nullable)
      Explanation of why the cardholder is disputing this transaction.

    - `evidence.other.product_description` (string, nullable)
      Description of the merchandise or service that was purchased.

    - `evidence.other.product_type` (enum, nullable)
      Whether the product was a merchandise or service.
Possible enum values:
      - `merchandise`
        Tangible goods such as groceries and furniture.

      - `service`
        Intangible goods such as domain name registration, flights and lessons.

  - `evidence.reason` (enum)
    The reason for filing the dispute. Its value will match the field containing the evidence.
Possible enum values:
    - `canceled`
      Service or merchandise was canceled.

    - `duplicate`
      There were multiple copies of a charge for a single purchase, or the charge was paid by other means.

    - `fraudulent`
      The cardholder’s details were compromised and the cardholder claims to not have participated in the transaction.

    - `merchandise_not_as_described`
      The merchandise was not as described.

    - `no_valid_authorization`
      The merchant processed a transaction without first obtaining a correct and valid authorization approval.

    - `not_received`
      Merchandise or service was not received.

    - `other`
      All other types of disputes.

    - `service_not_as_described`
      The service was not as described.

  - `evidence.service_not_as_described` (object, nullable)
    Evidence provided when `reason` is ‘service_not_as_described’.

    - `evidence.service_not_as_described.additional_documentation` (string, nullable)
      (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.

    - `evidence.service_not_as_described.canceled_at` (timestamp, nullable)
      Date when order was canceled.

    - `evidence.service_not_as_described.cancellation_reason` (string, nullable)
      Reason for canceling the order.

    - `evidence.service_not_as_described.explanation` (string, nullable)
      Explanation of why the cardholder is disputing this transaction.

    - `evidence.service_not_as_described.received_at` (timestamp, nullable)
      Date when the product was received.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `loss_reason` (enum, nullable)
  The enum that describes the dispute loss outcome. If the dispute is not lost, this field will be absent. New enum values may be added in the future, so be sure to handle unknown values.
Possible enum values:
  - `cardholder_authentication_issuer_liability`
    This dispute, created for Card-Not-Present fraud, is invalid because the card network has indicated the cardholder was securely authenticated. This most commonly occurs via 3DS or a secure digital wallet (e.g. Apple Pay). The dispute was automatically rejected by the card network.

  - `eci5_token_transaction_with_tavv`
    DEPRECATED: This dispute, created under Condition 10.4: Other Fraud, is invalid for an ECI 5 Token Transaction where the Token Authentication Verification Value (TAVV) was included in the Authorization Request. The dispute was automatically rejected by Visa.

  - `excess_disputes_in_timeframe`
    This dispute is invalid as more than 35 total disputes have been submitted with 120 calendar days of this dispute. The dispute was automatically rejected by the card network.

  - `has_not_met_the_minimum_dispute_amount_requirements`
    This dispute has not met the minimum amount threshold set by the card network based on the MCC. The dispute was automatically rejected by the card network.

  - `invalid_duplicate_dispute`
    This dispute, created under Condition 12.6: Duplicate Processing/Paid by Other Means, has not met the criteria set by Visa. The dispute was automatically rejected by Visa.

  - `invalid_incorrect_amount_dispute`
    This dispute, created under Condition 12.5: Incorrect Amount, has not met the criteria set by Visa. The dispute must include evidence of the correct amount. The dispute was automatically rejected by Visa.

  - `invalid_no_authorization`
    The dispute, created under Condition 11.3: No Authorization, is invalid due to the transaction being authorized as indicated in the Visa Core Rules and Visa Product and Service Rules. The dispute was automatically rejected by Visa.

  - `invalid_use_of_disputes`
    Stripe has determined that this is an invalid use of the card network dispute process; no dispute conditions apply.

  - `merchandise_delivered_or_shipped`
    The merchant provided evidence indicating that the merchandise was shipped/delivered. Stripe has evaluated this evidence and determined that it is compelling.

  - `merchandise_or_service_as_described`
    The merchant provided information indicating the item/service provided matched the description. Stripe has evaluated this evidence and determined that it is compelling.

  - `not_cancelled`
    The cardholder claims they canceled their subscription/order, but the merchant has no record of such cancellation, nor was one provided by the cardholder. Stripe has evaluated this evidence and determined that it is compelling.

  - `other`
    Please contact Stripe for more information about this dispute.

  - `refund_issued`
    The dispute is invalid because there is already a refund for the transaction in which the refund and dispute amounts sum up to more than the original transaction amount. The dispute was automatically rejected due to this discrepancy.

  - `submitted_beyond_allowable_time_limit`
    The dispute was submitted past the disputable deadline. The dispute was automatically rejected by the card network.

  - `transaction_3ds_required`
    DEPRECATED: This dispute is invalid because the merchant attempted 3DS for a Card-Not-Present (CNP) transaction, but the card provider did not have 3DS enabled for the card. The dispute was automatically rejected by the card network.

  - `transaction_approved_after_prior_fraud_dispute`
    The cardholder/card provider didn’t deactivate the card after claiming fraud on previous transactions. The dispute was automatically rejected by the card network.

  - `transaction_authorized`
    The merchant has provided evidence that indicates this transaction was authorized by the cardholder. Stripe has evaluated this evidence and determined that it is compelling.

  - `transaction_electronically_read`
    The liability shifts to the issuer for fraudulent disputes if the card-present transaction was authorized with a chip-reading terminal. This dispute was automatically rejected by the card network.

  - `transaction_qualifies_for_visa_easy_payment_service`
    This dispute is invalid since the transaction qualifies for Visa Easy Payment Service (VEPS) Transaction, which allows businesses to accept Visa without customers pausing to sign or enter a PIN. With VEPS, the liability shifts onto the card provider. The dispute was automatically rejected by Visa.

  - `transaction_unattended`
    This dispute is invalid as the transaction was unattended, chip-initiated, and online authorized (e.g., swiping a chip card at an unattended gas pump, parking meter, or ATM). The liability is on the card provider for these types of transactions. The dispute was automatically rejected by the card network.

- `metadata` (object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `status` (enum)
  Current status of the dispute.
Possible enum values:
  - `expired`
    The dispute has expired.

  - `lost`
    The dispute is lost.

  - `submitted`
    The dispute has been submitted to Stripe.

  - `unsubmitted`
    The dispute is pending submission to Stripe.

  - `won`
    The dispute is won.

- `transaction` (string)
  The transaction being disputed.

### The Dispute object

```json
{
  "id": "idp_1MykdxFtDWhhyHE1BFAV3osZ",
  "object": "issuing.dispute",
  "amount": 100,
  "created": 1681947753,
  "currency": "usd",
  "evidence": {
    "fraudulent": {
      "additional_documentation": null,
      "dispute_explanation": null,
      "explanation": "This transaction is fraudulent.",
      "uncategorized_file": null
    },
    "reason": "fraudulent"
  },
  "livemode": false,
  "metadata": {},
  "status": "unsubmitted",
  "transaction": "ipi_1MykXhFtDWhhyHE1UjsZZ3xQ"
}
```