# The Credit Balance Transaction object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `credit` (object, nullable)
  Credit details for this credit balance transaction. Only present if type is `credit`.

  - `credit.amount` (object)
    The amount of credit transaction.

    - `credit.amount.monetary` (object, nullable)
      The monetary amount.

      - `credit.amount.monetary.currency` (string)
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

      - `credit.amount.monetary.value` (integer)
        A positive integer representing the amount.

    - `credit.amount.type` (enum)
      The type of this amount. We currently only support `monetary` billing credits.
Possible enum values:
      - `monetary`
        The amount is a monetary amount.

  - `credit.credits_application_invoice_voided` (object, nullable)
    Details of the invoice to which the reinstated credits were originally applied. Only present if `type` is `credits_application_invoice_voided`.

    - `credit.credits_application_invoice_voided.invoice` (string)
      The invoice to which the reinstated billing credits were originally applied.

    - `credit.credits_application_invoice_voided.invoice_line_item` (string)
      The invoice line item to which the reinstated billing credits were originally applied.

  - `credit.type` (enum)
    The type of credit transaction.
Possible enum values:
    - `credits_application_invoice_voided`
      Represents the credits reinstated after an invoice to which credits were applied was voided.

    - `credits_granted`
      Represents the initial funding of credits after a credit grant becomes effective.

- `credit_grant` (string)
  The credit grant associated with this credit balance transaction.

- `debit` (object, nullable)
  Debit details for this credit balance transaction. Only present if type is `debit`.

  - `debit.amount` (object)
    The amount of debit transaction.

    - `debit.amount.monetary` (object, nullable)
      The monetary amount.

      - `debit.amount.monetary.currency` (string)
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

      - `debit.amount.monetary.value` (integer)
        A positive integer representing the amount.

    - `debit.amount.type` (enum)
      The type of this amount. We currently only support `monetary` billing credits.
Possible enum values:
      - `monetary`
        The amount is a monetary amount.

  - `debit.credits_applied` (object, nullable)
    Details of how the billing credits were applied to an invoice. Only present if `type` is `credits_applied`.

    - `debit.credits_applied.invoice` (string)
      The invoice to which the billing credits were applied.

    - `debit.credits_applied.invoice_line_item` (string)
      The invoice line item to which the billing credits were applied.

  - `debit.type` (enum)
    The type of debit transaction.
Possible enum values:
    - `credits_applied`
      Represents credits that were applied to a line item on an invoice.

    - `credits_expired`
      Represents credits that were expired due to credit grant being expired.

    - `credits_voided`
      Represents credits that were voided due to credit grant being voided.

- `effective_at` (timestamp)
  The effective time of this credit balance transaction.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `test_clock` (string, nullable)
  ID of the test clock this credit balance transaction belongs to.

- `type` (enum, nullable)
  The type of credit balance transaction (credit or debit).
Possible enum values:
  - `credit`
    A credit transaction.

  - `debit`
    A debit transaction.

### The Credit Balance Transaction object

```json
{
  "id": "cbtxn_test_61R9ZljjaFmdidb6e41L6nFOS1ekD9Ue",
  "object": "billing.credit_balance_transaction",
  "created": 1726619524,
  "credit": null,
  "credit_grant": "credgr_test_61R9ZkIkIzLSp0xze41L6nFOS1ekDTPE",
  "debit": {
    "amount": {
      "monetary": {
        "currency": "usd",
        "value": 1000
      },
      "type": "monetary"
    },
    "credits_applied": {
      "invoice": "in_1Q0BoLL6nFOS1ekDbwBM5ER1",
      "invoice_line_item": "il_1QB443L6nFOS1ekDwRiN3Z4n"
    },
    "type": "credits_applied"
  },
  "effective_at": 1729211351,
  "livemode": false,
  "test_clock": "clock_1Q0BoJL6nFOS1ekDbyYYuseM",
  "type": "debit"
}
```