# The Cash balance object

## Attributes

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `available` (object, nullable)
  A hash of all cash balances available to this customer. You cannot delete a customer with any cash balances, even if the balance is 0. Amounts are represented in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

- `customer` (string)
  The ID of the customer whose cash balance this object represents.

- `customer_account` (string, nullable)
  The ID of an Account representing a customer whose cash balance this object represents.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `settings` (object)
  A hash of settings for this cash balance.

  - `settings.reconciliation_mode` (enum)
    The configuration for how funds that land in the customer cash balance are reconciled.
Possible enum values:
    - `automatic`
    - `manual`

  - `settings.using_merchant_default` (boolean)
    A flag to indicate if reconciliation mode returned is the user’s default or is specific to this customer cash balance

### The Cash balance object

```json
{
  "object": "cash_balance",
  "available": {
    "eur": 10000
  },
  "customer": "cus_OaCLf8Fi1nbFpJ",
  "livemode": false,
  "settings": {
    "reconciliation_mode": "automatic",
    "using_merchant_default": true
  }
}
```