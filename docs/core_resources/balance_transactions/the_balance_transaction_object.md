# The Balance Transaction object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `amount` (integer)
  Gross amount of this transaction (in cents). A positive value represents funds charged to another party, and a negative value represents funds sent to another party.

- `available_on` (timestamp)
  The date that the transaction’s net funds become available in the Stripe balance.

- `balance_type` (enum)
  The balance that this transaction impacts.
Possible enum values:
  - `issuing`
    Balance Transactions that affect your Issuing balance

  - `payments`
    Balance Transactions that affect your Payments balance

  - `refund_and_dispute_prefunding`
    Balance Transactions that affect your Refund and Dispute Prefunding balance

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (enum)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `description` (string, nullable)
  An arbitrary string attached to the object. Often useful for displaying to users.

- `exchange_rate` (float, nullable)
  If applicable, this transaction uses an exchange rate. If money converts from currency A to currency B, then the `amount` in currency A, multipled by the `exchange_rate`, equals the `amount` in currency B. For example, if you charge a customer 10.00 EUR, the PaymentIntent’s `amount` is `1000` and `currency` is `eur`. If this converts to 12.34 USD in your Stripe account, the BalanceTransaction’s `amount` is `1234`, its `currency` is `usd`, and the `exchange_rate` is `1.234`.

- `fee` (integer)
  Fees (in cents) paid for this transaction. Represented as a positive integer when assessed.

- `fee_details` (array of objects)
  Detailed breakdown of fees (in cents) paid for this transaction.

  - `fee_details.amount` (integer)
    Amount of the fee, in cents.

  - `fee_details.application` (string, nullable)
    ID of the Connect application that earned the fee.

  - `fee_details.currency` (enum)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `fee_details.description` (string, nullable)
    An arbitrary string attached to the object. Often useful for displaying to users.

  - `fee_details.type` (string)
    Type of the fee, one of: `application_fee`, `payment_method_passthrough_fee`, `stripe_fee` or `tax`.

- `net` (integer)
  Net impact to a Stripe balance (in cents). A positive value represents incrementing a Stripe balance, and a negative value decrementing a Stripe balance. You can calculate the net impact of a transaction on a balance by `amount` - `fee`

- `reporting_category` (string)
  Learn more about how [reporting categories](https://stripe.com/docs/reports/reporting-categories) can help you understand balance transactions from an accounting perspective.

- `source` (string, nullable)
  This transaction relates to the Stripe object.

- `status` (string)
  The transaction’s net funds status in the Stripe balance, which are either `available` or `pending`.

- `type` (enum)
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

### The Balance Transaction object

```json
{
  "id": "txn_1MiN3gLkdIwHu7ixxapQrznl",
  "object": "balance_transaction",
  "amount": -400,
  "available_on": 1678043844,
  "created": 1678043844,
  "currency": "usd",
  "description": null,
  "exchange_rate": null,
  "fee": 0,
  "fee_details": [],
  "net": -400,
  "reporting_category": "transfer",
  "source": "tr_1MiN3gLkdIwHu7ixNCZvFdgA",
  "status": "available",
  "type": "transfer"
}
```