# The Bank Account object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `account` (string, nullable)
  The account this bank account belongs to. Only applicable on Accounts (not customers or recipients) This property is only available when returned as an [External Account](https://docs.stripe.com/api/external_account_bank_accounts/object.md) where [controller.is_controller](https://docs.stripe.com/api/accounts/object.md#account_object-controller-is_controller) is `true`.

- `account_holder_name` (string, nullable)
  The name of the person or business that owns the bank account.

- `account_holder_type` (string, nullable)
  The type of entity that holds the account. This can be either `individual` or `company`.

- `account_type` (string, nullable)
  The bank account type. This can only be `checking` or `savings` in most countries. In Japan, this can only be `futsu` or `toza`.

- `available_payout_methods` (array of enums, nullable)
  A set of available payout methods for this bank account. Only values from this set should be passed as the `method` when creating a payout.
Possible enum values:
  - `instant`
  - `standard`

- `bank_name` (string, nullable)
  Name of the bank associated with the routing number (e.g., `WELLS FARGO`).

- `country` (string)
  Two-letter ISO code representing the country the bank account is located in.

- `currency` (enum)
  Three-letter [ISO code for the currency](https://stripe.com/docs/payouts) paid out to the bank account.

- `customer` (string, nullable)
  The ID of the customer that the bank account is associated with.

- `fingerprint` (string, nullable)
  Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

- `last4` (string)
  The last four digits of the bank account number.

- `metadata` (object, nullable)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `routing_number` (string, nullable)
  The routing transit number for the bank account.

- `status` (string)
  For bank accounts, possible values are `new`, `validated`, `verified`, `verification_failed`, `tokenized_account_number_deactivated` or `errored`. A bank account that hasn’t had any activity or validation performed is `new`. If Stripe can determine that the bank account exists, its status will be `validated`. Note that there often isn’t enough information to know (e.g., for smaller credit unions), and the validation is not always run. If customer bank account verification has succeeded, the bank account status will be `verified`. If the verification failed for any reason, such as microdeposit failure, the status will be `verification_failed`. If the status is `tokenized_account_number_deactivated`, the account utilizes a tokenized account number which has been deactivated due to expiration or revocation. This account will need to be reverified to continue using it for money movement. If a payout sent to this bank account fails, we’ll set the status to `errored` and will not continue to send [scheduled payouts](https://stripe.com/docs/payouts#payout-schedule) until the bank details are updated.

  For external accounts, possible values are `new`, `errored`, `verification_failed`, and `tokenized_account_number_deactivated`. If a payout fails, the status is set to `errored` and scheduled payouts are stopped until account details are updated. In the US and India, if we can’t [verify the owner of the bank account](https://support.stripe.com/questions/bank-account-ownership-verification), we’ll set the status to `verification_failed`. Other validations aren’t run against external accounts because they’re only used for payouts. This means the other statuses don’t apply.

### The Bank Account object

```json
{
  "id": "ba_1MvoIJ2eZvKYlo2CO9f0MabO",
  "object": "bank_account",
  "account_holder_name": "Jane Austen",
  "account_holder_type": "company",
  "account_type": null,
  "bank_name": "STRIPE TEST BANK",
  "country": "US",
  "currency": "usd",
  "customer": "cus_9s6XI9OFIdpjIg",
  "fingerprint": "1JWtPxqbdX5Gamtc",
  "last4": "6789",
  "metadata": {},
  "routing_number": "110000000",
  "status": "new"
}
```