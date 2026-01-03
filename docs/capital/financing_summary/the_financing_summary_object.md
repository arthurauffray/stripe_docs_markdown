# The Financing Summary object

## Attributes

- `object` (string)
  The object type: financing_summary

- `details` (object, nullable)
  Additional information about the financing summary. Describes currency, advance amount, fee amount, withhold rate, remaining amount, paid amount, current repayment interval, repayment start date, and advance payout date.

  Only present for financing offers with the `paid_out` status.

  - `details.advance_amount` (integer)
    Amount of financing offered, in minor units. For example, 1,000 USD is represented as 100000.

  - `details.advance_paid_out_at` (float, nullable)
    The time at which the funds were paid out to the connected account’s Stripe balance. Given in milliseconds since unix epoch.

  - `details.currency` (string)
    Currency that the financing offer is transacted in. For example, `usd`.

  - `details.current_repayment_interval` (object, nullable)
    The chronologically current repayment interval for the financing offer.

    - `details.current_repayment_interval.due_at` (float)
      The time at which the minimum payment amount will be due. If not met through withholding, the Connected account’s linked bank account or account balance will be debited. Given in seconds since unix epoch.

    - `details.current_repayment_interval.duration_days` (integer, nullable)
      The length in days of the repayment interval.

    - `details.current_repayment_interval.paid_amount` (integer, nullable)
      The amount that has already been paid in the current repayment interval, in minor units. For example, 100 USD is represented as 10000.

    - `details.current_repayment_interval.remaining_amount` (integer)
      The amount that is yet to be paid in the current repayment interval, in minor units. For example, 100 USD is represented as 10000.

  - `details.fee_amount` (integer)
    Fixed fee amount, in minor units. For example, 100 USD is represented as 10000.

  - `details.paid_amount` (integer)
    The amount the Connected account has paid toward the financing debt so far, in minor units. For example, 1,000 USD is represented as 100000.

  - `details.remaining_amount` (integer)
    The balance remaining to be paid on the financing, in minor units. For example, 1,000 USD is represented as 100000.

  - `details.repayments_begin_at` (float, nullable)
    The time at which Capital will begin withholding from payments. Given in seconds since unix epoch.

  - `details.withhold_rate` (float)
    Per-transaction rate at which Stripe withholds funds to repay the financing.

- `financing_offer` (string, nullable)
  The unique identifier of the Financing Offer object that corresponds to the Financing Summary object.

- `status` (enum, nullable)
  The financing status of the connected account.
Possible enum values:
  - `accepted`
    The connected account has an active financing offer that has been paid out.

  - `delivered`
    A financing offer has been marketed to the connected account, but the account hasn’t accepted it yet.

  - `none`
    The connected account doesn’t have any active financing.

### The Financing Summary object

```json
{
  "object": "capital.financing_summary",
  "details": {
    "advance_amount": 100000,
    "advance_paid_out_at": 1688424277.0578003,
    "currency": "usd",
    "current_repayment_interval": null,
    "fee_amount": 10000,
    "paid_amount": 100263,
    "remaining_amount": 9737,
    "repayments_begin_at": 1688424277.0577993,
    "withhold_rate": 0.05
  },
  "financing_offer": "financingoffer_1NPvU12eZvKYlo2CotjdGRzu",
  "status": "accepted"
}
```