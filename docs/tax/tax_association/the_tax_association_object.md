# The Tax Association object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `calculation` (string)
  The [Tax Calculation](https://docs.stripe.com/docs/api/tax/calculations/object.md) that was included in PaymentIntent.

- `payment_intent` (string)
  The [PaymentIntent](https://docs.stripe.com/docs/api/payment_intents/object.md) that this Tax Association is tracking.

- `tax_transaction_attempts` (array of objects, nullable)
  Information about the tax transactions linked to this payment intent

  - `tax_transaction_attempts.committed` (object, nullable)
    If status is `committed`, this attribute contains further details about the committed tax transaction and subsequent reversals.

    - `tax_transaction_attempts.committed.transaction` (string)
      The [Tax Transaction](https://docs.stripe.com/docs/api/tax/transaction/object.md)

  - `tax_transaction_attempts.errored` (object, nullable)
    If status is `errored`, this attribute contains further details about the type of error encountered.

    - `tax_transaction_attempts.errored.reason` (enum)
      Details on why we couldn’t commit the tax transaction.
Possible enum values:
      - `another_payment_associated_with_calculation`
        Another payment already committed the calculation. Refunds on this payment won’t affect the tax transaction.

      - `calculation_expired`
        The calculation expired and can’t be committed as a tax transaction.

      - `currency_mismatch`
        The payment and tax calculation have different presentment currencies. Can’t commit the tax transaction.

      - `original_transaction_voided`
        The original sales tax transaction was voided.

      - `unique_reference_violation`
        A tax transaction with the provided reference (PaymentIntent id) already exists.

  - `tax_transaction_attempts.source` (string)
    The source of the tax transaction attempt. This is either a refund or a payment intent.

  - `tax_transaction_attempts.status` (string)
    The status of the transaction attempt. This can be `errored` or `committed`.

### The Tax Association object

```json
{
  "id": "taxa_1PYP5RRw02rhjhAjNemx66hC",
  "object": "tax.association",
  "calculation": "taxcalc_1PYP4vRw02rhjhAjPfzylM7p",
  "payment_intent": "pi_3PYP4zRw02rhjhAj1UotslTI",
  "tax_transaction_attempts": [
    {
      "source": "pi_1PXmsSE5ebw4kUHWK7FIhQlS",
      "status": "committed",
      "committed": {
        "transaction": "tax_1PXmsRE5ebw4kUHWLyVEiMis"
      }
    },
    {
      "source": "re_1PXmsSE5ebw4kUHWK7FIhQlS",
      "status": "committed",
      "committed": {
        "transaction": "tax_1PXmsgE5ebw4kUHW7Gg8jvpX"
      }
    }
  ]
}
```