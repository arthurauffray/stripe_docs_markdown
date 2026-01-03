# The Financing offer object

## Attributes

- `id` (string)
  A unique identifier for the financing object.

- `object` (string)
  The object type: financing_offer.

- `accepted_terms` (object, nullable)
  Information about the current financing object. Describes currency, advance amount, fee amount, withhold rate, and fee discount of previous financing.

  - `accepted_terms.advance_amount` (integer)
    Amount of financing offered, in minor units. For example, 1,000 USD is represented as 100000.

  - `accepted_terms.currency` (string)
    Currency that the financing offer is transacted in. For example, `usd`.

  - `accepted_terms.fee_amount` (integer)
    Fixed fee amount, in minor units. For example, 100 USD is represented as 10000.

  - `accepted_terms.previous_financing_fee_discount_amount` (integer, nullable)
    Populated when the `product_type` of the `financingoffer` is `refill`. Represents the discount amount on remaining premium for the existing loan at payout time.

  - `accepted_terms.repayment_interval_configuration` (object, nullable)
    The configuration for the repayment interval of the financing.

    - `accepted_terms.repayment_interval_configuration.duration_days` (integer, nullable)
      Length of each repayment interval in days.

    - `accepted_terms.repayment_interval_configuration.maximum_amount` (integer, nullable)
      Maximum amount that can be repaid in an interval, in minor units. If provided, repayments will be capped to this amount for each repayment interval. If no maximum is specified, there is no cap on the repayment amount in a repayment interval.

    - `accepted_terms.repayment_interval_configuration.minimum_amount` (integer, nullable)
      Minimum amount that needs to be repaid in an interval, in minor units.

  - `accepted_terms.target_payback_days` (integer, nullable)
    The estimated number of days to fully repay the financing. Note that this is an estimate based on current payment volume, and the actual number of days to fully repay the financing may differ.

  - `accepted_terms.withhold_rate` (float)
    Per-transaction rate at which Stripe withholds funds to repay the financing.

- `account` (string)
  The ID of the merchant associated with this financing object.

- `charged_off_at` (timestamp, nullable)
  The time at which this financing offer was charged off, if applicable. Given in seconds since unix epoch.

- `created` (integer)
  Time at which the offer was created. Given in seconds since unix epoch.

- `expires_after` (float)
  Time at which the offer expires. Given in seconds since unix epoch.

- `financing_type` (enum, nullable)
  The type of financing being offered.
Possible enum values:
  - `cash_advance`
    Capital’s Merchant Cash Advance program.

  - `fixed_term_loan`
    Capital’s fixed-term loan offering. See the [integration guide](https://docs.stripe.com/docs/capital/platforms.md) for more information.

  - `flex_loan`
    Capital’s flex loan offering. See the [integration guide](https://docs.stripe.com/docs/capital/platforms.md) for more information.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (object, nullable)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `offered_terms` (object, nullable)
  Information about the financing offer. Describes currency, offered advance amount, offered fee amount, campaign type, withhold rate, and fee discount rate of previous financing.

  - `offered_terms.advance_amount` (integer)
    Amount of financing offered, in minor units. For example, 1,000 USD is represented as 100000.

  - `offered_terms.campaign_type` (enum)
    Describes the type of user the offer is being extended to.
Possible enum values:
    - `newly_eligible_user`
      A user who has never been eligible for Capital before.

    - `previously_eligible_user`
      A user who has been offered financing through Capital before, but never accepted an offer.

    - `repeat_user`
      A user who has already accepted or fully repaid a loan, and is receiving another offer.

  - `offered_terms.currency` (string)
    Currency that the financing offer is transacted in. For example, `usd`.

  - `offered_terms.fee_amount` (integer)
    Fixed fee amount, in minor units. For example, 100 USD is represented as 10000.

  - `offered_terms.previous_financing_fee_discount_rate` (float, nullable)
    Populated when the `product_type` of the `financingoffer` is `refill`. Represents the discount rate percentage on remaining fee on the existing loan. When the `financing_offer` is paid out, the `previous_financing_fee_discount_amount` will be computed as the multiple of this rate and the remaining fee.

  - `offered_terms.repayment_interval_configuration` (object, nullable)
    The configuration for the repayment interval of the financing.

    - `offered_terms.repayment_interval_configuration.duration_days` (integer, nullable)
      Length of each repayment interval in days.

    - `offered_terms.repayment_interval_configuration.maximum_amount` (integer, nullable)
      Maximum amount that can be repaid in an interval, in minor units. If provided, repayments will be capped to this amount for each repayment interval. If no maximum is specified, there is no cap on the repayment amount in a repayment interval.

    - `offered_terms.repayment_interval_configuration.minimum_amount` (integer, nullable)
      Minimum amount that needs to be repaid in an interval, in minor units.

  - `offered_terms.target_payback_days` (integer, nullable)
    The estimated number of days to fully repay the financing. Note that this is an estimate based on current payment volume, and the actual number of days to fully repay the financing may differ.

  - `offered_terms.withhold_rate` (float)
    Per-transaction rate at which Stripe withholds funds to repay the financing.

- `product_type` (enum, nullable)
  Financing product identifier.
Possible enum values:
  - `refill`
    A “refill” financing offer extended through Stripe Capital. Refills are a form of discounted refinancing. See the [integration guide](https://docs.stripe.com/docs/capital/platforms.md#refills) for more information.

  - `standard`
    A standard financing offer extended through Stripe Capital.

- `replacement` (string, nullable)
  The ID of the financing offer that replaced this offer.

- `replacement_for` (string, nullable)
  The ID of the financing offer that this offer is a replacement for.

- `status` (enum)
  The current status of the offer.
Possible enum values:
  - `accepted`
    Set once an offer has been accepted by the Connected account.

  - `canceled`
    Set when the Connected account has reached out to Capital’s servicing team within 48 hours of acceptance and requested cancellation of their offer.

  - `completed`
    Set when the financing offer has fully repaid. This status is no longer in use. See `fully_repaid` instead.

  - `delivered`
    Once an offer has been delivered, mark it so using the [mark_delivered](https://docs.stripe.com/docs/api/capital/financing_offers/mark_delivered.md) endpoint.

  - `expired`
    Set when the financing offer has expired, usually 30 days after creation.

  - `fully_repaid`
    Set when the financing offer has been fully repaid.

  - `paid_out`
    Set once an offer has been paid out to the Connected account.

  - `rejected`
    Set when Capital’s servicing team has rejected the application for financing. The Connected account receives an email with the reason for rejection.

  - `replaced`
    Set when the financing offer has been replaced.

  - `undelivered`
    All offers begin in this state. A financing offer must be delivered to its Connected account using approved marketing materials.

- `status_transitions` (object)
  Hash containing timestamps of when the offer transitioned to a particular status.

  - `status_transitions.accepted_at` (timestamp, nullable)
    Timestamp describing when a FinancingOffer changed status to `accepted`

  - `status_transitions.canceled_at` (timestamp, nullable)
    Timestamp describing when a FinancingOffer changed status to `canceled`

  - `status_transitions.fully_repaid_at` (timestamp, nullable)
    Timestamp describing when a FinancingOffer changed status to `fully_repaid`

  - `status_transitions.paid_out_at` (timestamp, nullable)
    Timestamp describing when a FinancingOffer changed status to `paid_out`

  - `status_transitions.rejected_at` (timestamp, nullable)
    Timestamp describing when a FinancingOffer changed status to `rejected`

  - `status_transitions.replaced_at` (timestamp, nullable)
    Timestamp describing when a FinancingOffer changed status to `replaced`

- `type` (enum, nullable)
  See [financing_type](https://docs.stripe.com/docs/api/capital/connect_financing_object.md#financing_offer_object-financing_type).
Possible enum values:
  - `cash_advance`
  - `fixed_term_loan`
  - `flex_loan`

### The Financing offer object

```json
{
  "id": "financingoffer_1NPvKg2eZvKYlo2CnEEmlCVh",
  "object": "capital.financing_offer",
  "account": "acct_1NPvKgBY65lDjjDk",
  "created": 1688423699,
  "expires_after": 1690934400,
  "financing_type": "flex_loan",
  "livemode": true,
  "offered_terms": {
    "advance_amount": 10000,
    "campaign_type": "newly_eligible_user",
    "currency": "usd",
    "fee_amount": 1000,
    "previous_financing_fee_discount_rate": null,
    "withhold_rate": 0.05
  },
  "product_type": "standard",
  "status": "undelivered"
}
```