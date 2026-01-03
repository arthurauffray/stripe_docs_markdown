# Retrieve a Country Spec

Returns a Country Spec for a given Country code.

## Returns

Returns a [country_spec](https://docs.stripe.com/api/country_specs/retrieve.md#country_spec_object) object if a valid country code is provided, and raises [an error](https://docs.stripe.com/api/country_specs/retrieve.md#errors) otherwise.

```curl
curl https://api.stripe.com/v1/country_specs/US \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe country_specs retrieve US
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

country_spec = client.v1.country_specs.retrieve('US')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

country_spec = client.v1.country_specs.retrieve("US")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$countrySpec = $stripe->countrySpecs->retrieve('US', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CountrySpecRetrieveParams params = CountrySpecRetrieveParams.builder().build();

CountrySpec countrySpec = client.v1().countrySpecs().retrieve("US", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const countrySpec = await stripe.countrySpecs.retrieve('US');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CountrySpecRetrieveParams{}
result, err := sc.V1CountrySpecs.Retrieve(context.TODO(), "US", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.CountrySpecs;
CountrySpec countrySpec = service.Get("US");
```

### Response

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