# The Funding Instruction object

## Attributes

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `bank_transfer` (object)
  Details to display instructions for initiating a bank transfer

  - `bank_transfer.country` (string)
    The country of the bank account to fund

  - `bank_transfer.financial_addresses` (array of objects)
    A list of financial addresses that can be used to fund a particular balance

    - `bank_transfer.financial_addresses.iban` (object, nullable)
      An IBAN-based FinancialAddress

      - `bank_transfer.financial_addresses.iban.account_holder_address` (object)
        The account holder’s physical address

        - `bank_transfer.financial_addresses.iban.account_holder_address.city` (string, nullable)
          City, district, suburb, town, or village.

        - `bank_transfer.financial_addresses.iban.account_holder_address.country` (string, nullable)
          Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

        - `bank_transfer.financial_addresses.iban.account_holder_address.line1` (string, nullable)
          Address line 1, such as the street, PO Box, or company name.

        - `bank_transfer.financial_addresses.iban.account_holder_address.line2` (string, nullable)
          Address line 2, such as the apartment, suite, unit, or building.

        - `bank_transfer.financial_addresses.iban.account_holder_address.postal_code` (string, nullable)
          ZIP or postal code.

        - `bank_transfer.financial_addresses.iban.account_holder_address.state` (string, nullable)
          State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

      - `bank_transfer.financial_addresses.iban.account_holder_name` (string)
        The name of the person or business that owns the bank account

      - `bank_transfer.financial_addresses.iban.bank_address` (object)
        The bank’s physical address

        - `bank_transfer.financial_addresses.iban.bank_address.city` (string, nullable)
          City, district, suburb, town, or village.

        - `bank_transfer.financial_addresses.iban.bank_address.country` (string, nullable)
          Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

        - `bank_transfer.financial_addresses.iban.bank_address.line1` (string, nullable)
          Address line 1, such as the street, PO Box, or company name.

        - `bank_transfer.financial_addresses.iban.bank_address.line2` (string, nullable)
          Address line 2, such as the apartment, suite, unit, or building.

        - `bank_transfer.financial_addresses.iban.bank_address.postal_code` (string, nullable)
          ZIP or postal code.

        - `bank_transfer.financial_addresses.iban.bank_address.state` (string, nullable)
          State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

      - `bank_transfer.financial_addresses.iban.bic` (string)
        The BIC/SWIFT code of the account.

      - `bank_transfer.financial_addresses.iban.country` (string)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `bank_transfer.financial_addresses.iban.iban` (string)
        The IBAN of the account.

    - `bank_transfer.financial_addresses.sort_code` (object, nullable)
      An account number and sort code-based FinancialAddress

      - `bank_transfer.financial_addresses.sort_code.account_holder_address` (object)
        The account holder’s physical address

        - `bank_transfer.financial_addresses.sort_code.account_holder_address.city` (string, nullable)
          City, district, suburb, town, or village.

        - `bank_transfer.financial_addresses.sort_code.account_holder_address.country` (string, nullable)
          Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

        - `bank_transfer.financial_addresses.sort_code.account_holder_address.line1` (string, nullable)
          Address line 1, such as the street, PO Box, or company name.

        - `bank_transfer.financial_addresses.sort_code.account_holder_address.line2` (string, nullable)
          Address line 2, such as the apartment, suite, unit, or building.

        - `bank_transfer.financial_addresses.sort_code.account_holder_address.postal_code` (string, nullable)
          ZIP or postal code.

        - `bank_transfer.financial_addresses.sort_code.account_holder_address.state` (string, nullable)
          State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

      - `bank_transfer.financial_addresses.sort_code.account_holder_name` (string)
        The name of the person or business that owns the bank account

      - `bank_transfer.financial_addresses.sort_code.account_number` (string)
        The account number

      - `bank_transfer.financial_addresses.sort_code.bank_address` (object)
        The bank’s physical address

        - `bank_transfer.financial_addresses.sort_code.bank_address.city` (string, nullable)
          City, district, suburb, town, or village.

        - `bank_transfer.financial_addresses.sort_code.bank_address.country` (string, nullable)
          Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

        - `bank_transfer.financial_addresses.sort_code.bank_address.line1` (string, nullable)
          Address line 1, such as the street, PO Box, or company name.

        - `bank_transfer.financial_addresses.sort_code.bank_address.line2` (string, nullable)
          Address line 2, such as the apartment, suite, unit, or building.

        - `bank_transfer.financial_addresses.sort_code.bank_address.postal_code` (string, nullable)
          ZIP or postal code.

        - `bank_transfer.financial_addresses.sort_code.bank_address.state` (string, nullable)
          State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

      - `bank_transfer.financial_addresses.sort_code.sort_code` (string)
        The six-digit sort code

    - `bank_transfer.financial_addresses.supported_networks` (array of enums, nullable)
      The payment networks supported by this FinancialAddress
Possible enum values:

    - `bank_transfer.financial_addresses.type` (enum)
      The type of financial address
Possible enum values:

  - `bank_transfer.type` (enum)
    The bank_transfer type
Possible enum values:
    - `eu_bank_transfer`
      A bank transfer to an EU bank account

    - `gb_bank_transfer`
      A bank transfer to a GB bank account

- `currency` (string)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `funding_type` (enum)
  The `funding_type` of the returned instructions
Possible enum values:
  - `bank_transfer`
    Use a bank_transfer hash to define the bank transfer type

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

### The Funding Instruction object

```json
{
  "object": "funding_instructions",
  "bank_transfer": {
    "country": "DE",
    "financial_addresses": [
      {
        "iban": {
          "account_holder_name": "Stripe Technology Europe Limited",
          "bic": "SXPYDEHH",
          "country": "DE",
          "iban": "DE00000000000000000001"
        },
        "supported_networks": [
          "sepa"
        ],
        "type": "iban"
      }
    ],
    "type": "eu_bank_transfer"
  },
  "currency": "eur",
  "funding_type": "bank_transfer",
  "livemode": false
}
```