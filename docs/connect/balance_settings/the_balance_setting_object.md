# The Balance Setting object

## Attributes

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `payments` (object)
  Settings that apply to the [Payments Balance](https://docs.stripe.com/api/balance.md).

  - `payments.debit_negative_balances` (boolean, nullable)
    A Boolean indicating if Stripe should try to reclaim negative balances from an attached bank account. See [Understanding Connect account balances](https://docs.stripe.com/connect/account-balances.md) for details. The default value is `false` when [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `application`, which includes Custom accounts, otherwise `true`.

  - `payments.payouts` (object, nullable)
    Settings specific to the account’s payouts.

    - `payments.payouts.minimum_balance_by_currency` (object, nullable)
      The minimum balance amount to retain per currency after automatic payouts. Only funds that exceed these amounts are paid out. Learn more about the [minimum balances for automatic payouts](https://docs.stripe.com/payouts/minimum-balances-for-automatic-payouts.md).

    - `payments.payouts.schedule` (object, nullable)
      Details on when funds from charges are available, and when they are paid out to an external account. See our [Setting Bank and Debit Card Payouts](https://docs.stripe.com/docs/connect/bank-transfers.md#payout-information) documentation for details.

      - `payments.payouts.schedule.interval` (enum, nullable)
        How frequently funds will be paid out. One of `manual` (payouts only created via API call), `daily`, `weekly`, or `monthly`.
Possible enum values:
        - `daily`
          Stripe automatically sends money to your bank account daily

        - `manual`
          You manually send funds to your bank account

        - `monthly`
          Stripe automatically sends money to your bank account monthly

        - `weekly`
          Stripe automatically sends money to your bank account weekly

      - `payments.payouts.schedule.monthly_payout_days` (array of integers, nullable)
        The day of the month funds will be paid out. Only shown if `interval` is monthly. Payouts scheduled between the 29th and 31st of the month are sent on the last day of shorter months.

      - `payments.payouts.schedule.weekly_payout_days` (array of enums, nullable)
        The days of the week when available funds are paid out, specified as an array, for example, [`monday`, `tuesday`]. Only shown if `interval` is weekly.
Possible enum values:
        - `monday`
          Select Monday as one of the weekly payout days

        - `tuesday`
          Select Tuesday as one of the weekly payout days

        - `wednesday`
          Select Wednesday as one of the weekly payout days

        - `thursday`
          Select Thursday as one of the weekly payout days

        - `friday`
          Select Friday as one of the weekly payout days

    - `payments.payouts.statement_descriptor` (string, nullable)
      The text that appears on the bank account statement  for payouts. If not set, this defaults to the platform’s bank descriptor as set in the Dashboard.

    - `payments.payouts.status` (enum)
      Whether the funds in this account can be paid out.
Possible enum values:
      - `disabled`
        Funds in this account cannot be paid out.

      - `enabled`
        Funds in this account can be paid out.

  - `payments.settlement_timing` (object)
    Settings related to the account’s balance settlement timing. See [Balances and settlement time](https://docs.stripe.com/payments/balances.md) to learn more.

    - `payments.settlement_timing.delay_days` (integer)
      The number of days charge funds are held before becoming available.

    - `payments.settlement_timing.delay_days_override` (integer, nullable)
      The number of days charge funds are held before becoming available. If present, overrides the default, or minimum available, for the account.

### The Balance Setting object

```json
{
  "object": "balance_settings",
  "payments": {
    "debit_negative_balances": true,
    "payouts": {
      "minimum_balance_by_currency": {
        "usd": 1500,
        "cad": 8000
      },
      "schedule": {
        "interval": "weekly",
        "weekly_payout_days": [
          "monday",
          "wednesday"
        ]
      },
      "statement_descriptor": null,
      "status": "enabled"
    },
    "settlement_timing": {
      "delay_days_override": 3,
      "delay_days": 3
    }
  }
}
```