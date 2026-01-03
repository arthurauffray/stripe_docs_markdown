# The Country Spec object

## Attributes

- `id` (string)
  Unique identifier for the object. Represented as the ISO country code for this country.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `default_currency` (string)
  The default currency for this country. This applies to both payment methods and bank accounts.

- `supported_bank_account_currencies` (object)
  Currencies that can be accepted in the specific country (for transfers).

- `supported_payment_currencies` (array of strings)
  Currencies that can be accepted in the specified country (for payments).

- `supported_payment_methods` (array of strings)
  Payment methods available in the specified country. You may need to enable some payment methods (e.g., [ACH](https://stripe.com/docs/ach)) on your account before they appear in this list. The `stripe` payment method refers to [charging through your platform](https://stripe.com/docs/connect/destination-charges).

- `supported_transfer_countries` (array of strings)
  Countries that can accept transfers from the specified country.

- `verification_fields` (object)
  Lists the types of verification data needed to keep an account open.

  - `verification_fields.company` (object)
    Verification types for company account.

    - `verification_fields.company.additional` (array of strings)
      Additional fields which are only required for some users.

    - `verification_fields.company.minimum` (array of strings)
      Fields which every account must eventually provide.

  - `verification_fields.individual` (object)
    Verification types for individual account.

    - `verification_fields.individual.additional` (array of strings)
      Additional fields which are only required for some users.

    - `verification_fields.individual.minimum` (array of strings)
      Fields which every account must eventually provide.

### The Country Spec object

```json
{
  "id": "US",
  "object": "country_spec",
  "default_currency": "usd",
  "supported_bank_account_currencies": {
    "usd": [
      "US"
    ]
  },
  "supported_payment_currencies": [
    "usd",
    "aed",
    "afn",
    "..."
  ],
  "supported_payment_methods": [
    "ach",
    "card",
    "stripe"
  ],
  "supported_transfer_countries": [
    "US",
    "AE",
    "AG",
    "AL",
    "AM",
    "AR",
    "AT",
    "AU",
    "BA",
    "BE",
    "BG",
    "BH",
    "BO",
    "CA",
    "CH",
    "CI",
    "CL",
    "CO",
    "CR",
    "CY",
    "CZ",
    "DE",
    "DK",
    "DO",
    "EC",
    "EE",
    "EG",
    "ES",
    "ET",
    "FI",
    "FR",
    "GB",
    "GH",
    "GM",
    "GR",
    "GT",
    "GY",
    "HK",
    "HR",
    "HU",
    "ID",
    "IE",
    "IL",
    "IS",
    "IT",
    "JM",
    "JO",
    "JP",
    "KE",
    "KH",
    "KR",
    "KW",
    "LC",
    "LI",
    "LK",
    "LT",
    "LU",
    "LV",
    "MA",
    "MD",
    "MG",
    "MK",
    "MN",
    "MO",
    "MT",
    "MU",
    "MX",
    "MY",
    "NA",
    "NG",
    "NL",
    "NO",
    "NZ",
    "OM",
    "PA",
    "PE",
    "PH",
    "PL",
    "PT",
    "PY",
    "QA",
    "RO",
    "RS",
    "RW",
    "SA",
    "SE",
    "SG",
    "SI",
    "SK",
    "SN",
    "SV",
    "TH",
    "TN",
    "TR",
    "TT",
    "TZ",
    "UY",
    "UZ",
    "VN",
    "ZA",
    "BD",
    "BJ",
    "MC",
    "NE",
    "SM",
    "AZ",
    "BN",
    "BT",
    "AO",
    "DZ",
    "TW",
    "BS",
    "BW",
    "GA",
    "LA",
    "MZ",
    "KZ",
    "PK"
  ],
  "verification_fields": {
    "company": {
      "additional": [],
      "minimum": [
        "business_profile.mcc",
        "business_profile.url",
        "business_type",
        "company.address.city",
        "company.address.line1",
        "company.address.postal_code",
        "company.address.state",
        "company.name",
        "company.owners_provided",
        "company.phone",
        "company.tax_id",
        "external_account",
        "owners.address.city",
        "owners.address.line1",
        "owners.address.postal_code",
        "owners.address.state",
        "owners.dob.day",
        "owners.dob.month",
        "owners.dob.year",
        "owners.email",
        "owners.first_name",
        "owners.id_number",
        "owners.last_name",
        "owners.phone",
        "owners.ssn_last_4",
        "owners.verification.document",
        "representative.address.city",
        "representative.address.line1",
        "representative.address.postal_code",
        "representative.address.state",
        "representative.dob.day",
        "representative.dob.month",
        "representative.dob.year",
        "representative.email",
        "representative.first_name",
        "representative.id_number",
        "representative.last_name",
        "representative.phone",
        "representative.relationship.executive",
        "representative.relationship.title",
        "representative.ssn_last_4",
        "representative.verification.document",
        "tos_acceptance.date",
        "tos_acceptance.ip"
      ]
    },
    "individual": {
      "additional": [],
      "minimum": [
        "business_profile.mcc",
        "business_profile.url",
        "business_type",
        "external_account",
        "individual.address.city",
        "individual.address.line1",
        "individual.address.postal_code",
        "individual.address.state",
        "individual.dob.day",
        "individual.dob.month",
        "individual.dob.year",
        "individual.email",
        "individual.first_name",
        "individual.id_number",
        "individual.last_name",
        "individual.phone",
        "individual.ssn_last_4",
        "individual.verification.document",
        "tos_acceptance.date",
        "tos_acceptance.ip"
      ]
    }
  }
}
```