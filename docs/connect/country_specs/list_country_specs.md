# List Country Specs

Lists all Country Spec objects available in the API.

## Returns

Returns a list of country_spec objects.

## Parameters

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/country_specs \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe country_specs list  \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

country_specs = client.v1.country_specs.list({limit: 3})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

country_specs = client.v1.country_specs.list({"limit": 3})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$countrySpecs = $stripe->countrySpecs->all(['limit' => 3]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CountrySpecListParams params = CountrySpecListParams.builder().setLimit(3L).build();

StripeCollection<CountrySpec> stripeCollection =
  client.v1().countrySpecs().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const countrySpecs = await stripe.countrySpecs.list({
  limit: 3,
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CountrySpecListParams{}
params.Limit = stripe.Int64(3)
result := sc.V1CountrySpecs.List(context.TODO(), params)
```

```dotnet
var options = new CountrySpecListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.CountrySpecs;
StripeList<CountrySpec> countrySpecs = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/country_specs",
  "has_more": false,
  "data": [
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
  ]
}
```