# The External Account Card object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `account` (string, nullable)
  The account this card belongs to. This attribute will not be in the card object if the card belongs to a customer or recipient instead. This property is only available for accounts where [controller.is_controller](https://docs.stripe.com/api/accounts/object.md#account_object-controller-is_controller) is `true`.

- `address_city` (string, nullable)
  City/District/Suburb/Town/Village.

- `address_country` (string, nullable)
  Billing address country, if provided when creating card.

- `address_line1` (string, nullable)
  Address line 1 (Street address/PO Box/Company name).

- `address_line1_check` (string, nullable)
  If `address_line1` was provided, results of the check: `pass`, `fail`, `unavailable`, or `unchecked`.

- `address_line2` (string, nullable)
  Address line 2 (Apartment/Suite/Unit/Building).

- `address_state` (string, nullable)
  State/County/Province/Region.

- `address_zip` (string, nullable)
  ZIP or postal code.

- `address_zip_check` (string, nullable)
  If `address_zip` was provided, results of the check: `pass`, `fail`, `unavailable`, or `unchecked`.

- `allow_redisplay` (enum, nullable)
  This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow. The field defaults to “unspecified”.
Possible enum values:
  - `always`
    Use `always` to indicate that this payment method can always be shown to a customer in a checkout flow.

  - `limited`
    Use `limited` to indicate that this payment method can’t always be shown to a customer in a checkout flow. For example, it can only be shown in the context of a specific subscription.

  - `unspecified`
    This is the default value for payment methods where `allow_redisplay` wasn’t set.

- `available_payout_methods` (array of enums, nullable)
  A set of available payout methods for this card. Only values from this set should be passed as the `method` when creating a payout.
Possible enum values:
  - `instant`
  - `standard`

- `brand` (string)
  Card brand. Can be `American Express`, `Cartes Bancaires`, `Diners Club`, `Discover`, `Eftpos Australia`, `Girocard`, `JCB`, `MasterCard`, `UnionPay`, `Visa`, or `Unknown`.

- `country` (string, nullable)
  Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you’ve collected.

- `currency` (enum, nullable)
  Three-letter [ISO code for currency](https://www.iso.org/iso-4217-currency-codes.html) in lowercase. Must be a [supported currency](https://docs.stripe.com/currencies.md). Only applicable on accounts (not customers or recipients). The card can be used as a transfer destination for funds in this currency. This property is only available for accounts where [controller.is_controller](https://docs.stripe.com/api/accounts/object.md#account_object-controller-is_controller) is `true`.

- `customer` (string, nullable)
  The customer that this card belongs to. This attribute will not be in the card object if the card belongs to an account or recipient instead.

- `cvc_check` (string, nullable)
  If a CVC was provided, results of the check: `pass`, `fail`, `unavailable`, or `unchecked`. A result of unchecked indicates that CVC was provided but hasn’t been checked yet. Checks are typically performed when attaching a card to a Customer object, or when creating a charge. For more details, see [Check if a card is valid without a charge](https://support.stripe.com/questions/check-if-a-card-is-valid-without-a-charge).

- `default_for_currency` (boolean, nullable)
  Whether this card is the default external account for its currency. This property is only available for accounts where [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `application`, which includes Custom accounts.

- `dynamic_last4` (string, nullable)
  (For tokenized numbers only.) The last four digits of the device account number.

- `exp_month` (integer)
  Two-digit number representing the card’s expiration month.

- `exp_year` (integer)
  Four-digit number representing the card’s expiration year.

- `fingerprint` (string, nullable)
  Uniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.

  *As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card—one for India and one for the rest of the world.*

- `funding` (string)
  Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.

- `iin` (string, nullable)
  Issuer identification number of the card.

- `last4` (string)
  The last four digits of the card.

- `metadata` (object, nullable)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `name` (string, nullable)
  Cardholder name.

- `regulated_status` (enum, nullable)
  Status of a card based on the card issuer.
Possible enum values:
  - `regulated`
    The card falls under a regulated account range.

  - `unregulated`
    The card does not fall under a regulated account range.

- `status` (string, nullable)
  For external accounts that are cards, possible values are `new` and `errored`. If a payout fails, the status is set to `errored` and [scheduled payouts](https://stripe.com/docs/payouts#payout-schedule) are stopped until account details are updated.

- `tokenization_method` (string, nullable)
  If the card number is tokenized, this is the method that was used. Can be `android_pay` (includes Google Pay), `apple_pay`, `masterpass`, `visa_checkout`, or null.

- `wallet` (object, nullable)
  If this Card is part of a card wallet, this contains the details of the card wallet.

  - `wallet.apple_pay` (object, nullable)
    If this is a `apple_pay` card wallet, this hash contains details about the wallet.

  - `wallet.type` (enum)
    The type of the card wallet, one of `apple_pay` or `link`. An additional hash is included on the Wallet subhash with a name matching this value. It contains additional information specific to the card wallet type.
Possible enum values:
    - `apple_pay`
    - `link`

### The External Account Card object

```json
{
  "id": "card_1MvoiELkdIwHu7ixOeFGbN9D",
  "object": "card",
  "address_city": null,
  "address_country": null,
  "address_line1": null,
  "address_line1_check": null,
  "address_line2": null,
  "address_state": null,
  "address_zip": null,
  "address_zip_check": null,
  "brand": "Visa",
  "country": "US",
  "customer": "cus_NhD8HD2bY8dP3V",
  "cvc_check": null,
  "dynamic_last4": null,
  "exp_month": 4,
  "exp_year": 2024,
  "fingerprint": "mToisGZ01V71BCos",
  "funding": "credit",
  "last4": "4242",
  "metadata": {},
  "name": null,
  "tokenization_method": null,
  "wallet": null
}
```