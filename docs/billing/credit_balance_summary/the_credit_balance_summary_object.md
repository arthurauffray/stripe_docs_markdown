# The Credit Balance Summary object

## Attributes

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `balances` (array of objects)
  The billing credit balances. One entry per credit grant currency. If a customer only has credit grants in a single currency, then this will have a single balance entry.

  - `balances.available_balance` (object)
    Billing credit balance that is available for use by the customer. This is equal to ledger balance less any expired billing credits for which expiration ledger transaction entries haven’t yet been committed to the ledger. In future, this will also take into account any usage that hasn’t yet been invoiced for a customer.

    - `balances.available_balance.monetary` (object, nullable)
      The monetary amount.

      - `balances.available_balance.monetary.currency` (string)
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

      - `balances.available_balance.monetary.value` (integer)
        A positive integer representing the amount.

    - `balances.available_balance.type` (enum)
      The type of this amount. We currently only support `monetary` billing credits.
Possible enum values:
      - `monetary`
        The amount is a monetary amount.

  - `balances.ledger_balance` (object)
    Reflects billing credit balance taking into account ledger transactions that have been committed to the ledger.

    - `balances.ledger_balance.monetary` (object, nullable)
      The monetary amount.

      - `balances.ledger_balance.monetary.currency` (string)
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

      - `balances.ledger_balance.monetary.value` (integer)
        A positive integer representing the amount.

    - `balances.ledger_balance.type` (enum)
      The type of this amount. We currently only support `monetary` billing credits.
Possible enum values:
      - `monetary`
        The amount is a monetary amount.

- `customer` (string)
  The customer the balance is for.

- `customer_account` (string, nullable)
  The account the balance is for.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

### The Credit Balance Summary object

```json
{
  "object": "billing.credit_balance_summary",
  "balances": [
    {
      "available_balance": {
        "monetary": {
          "currency": "usd",
          "value": 1000
        },
        "type": "monetary"
      },
      "ledger_balance": {
        "monetary": {
          "currency": "usd",
          "value": 1000
        },
        "type": "monetary"
      }
    }
  ],
  "customer": "cus_QsEHa3GKweMwih",
  "livemode": false
}
```