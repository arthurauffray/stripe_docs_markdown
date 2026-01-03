# Create a person token

Creates a single-use token that represents the details for a person. Use this when you create or update persons associated with a Connect account. Learn more about [account tokens](https://docs.stripe.com/docs/connect/account-tokens.md).

You can only create person tokens with your application’s publishable key and in live mode. You can use your application’s secret key to create person tokens only in test mode.

## Returns

Returns the created person token if it’s successful. Otherwise, this call raises [an error](https://docs.stripe.com/api/tokens/create_person.md#errors).

## Parameters

- `person` (object, required)
  Information for the person this token represents.

  - `person.additional_tos_acceptances` (object, optional)
    Details on the legal guardian’s or authorizer’s acceptance of the required Stripe agreements.

    - `person.additional_tos_acceptances.account` (object, optional)
      Details on the legal guardian’s acceptance of the main Stripe service agreement.

      - `person.additional_tos_acceptances.account.date` (timestamp, required if IP or user_agent is provided)
        The Unix timestamp marking when the account representative accepted the service agreement.

      - `person.additional_tos_acceptances.account.ip` (string, required if date or user_agent is provided)
        The IP address from which the account representative accepted the service agreement.

      - `person.additional_tos_acceptances.account.user_agent` (string, optional)
        The user agent of the browser from which the account representative accepted the service agreement.

  - `person.address` (object, optional)
    The person’s address.

    - `person.address.city` (string, optional)
      City, district, suburb, town, or village.

      The maximum length is 100 characters.

    - `person.address.country` (string, optional)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `person.address.line1` (string, optional)
      Address line 1, such as the street, PO Box, or company name.

      The maximum length is 200 characters.

    - `person.address.line2` (string, optional)
      Address line 2, such as the apartment, suite, unit, or building.

      The maximum length is 200 characters.

    - `person.address.postal_code` (string, optional)
      ZIP or postal code.

    - `person.address.state` (string, optional)
      State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

  - `person.address_kana` (object, optional)
    The Kana variation of the person’s address (Japan only).

    - `person.address_kana.city` (string, optional)
      City or ward.

    - `person.address_kana.country` (string, optional)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `person.address_kana.line1` (string, optional)
      Block or building number.

    - `person.address_kana.line2` (string, optional)
      Building details.

    - `person.address_kana.postal_code` (string, optional)
      Postal code.

    - `person.address_kana.state` (string, optional)
      Prefecture.

    - `person.address_kana.town` (string, optional)
      Town or cho-me.

  - `person.address_kanji` (object, optional)
    The Kanji variation of the person’s address (Japan only).

    - `person.address_kanji.city` (string, optional)
      City or ward.

    - `person.address_kanji.country` (string, optional)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `person.address_kanji.line1` (string, optional)
      Block or building number.

    - `person.address_kanji.line2` (string, optional)
      Building details.

    - `person.address_kanji.postal_code` (string, optional)
      Postal code.

    - `person.address_kanji.state` (string, optional)
      Prefecture.

    - `person.address_kanji.town` (string, optional)
      Town or cho-me.

  - `person.dob` (object, optional)
    The person’s date of birth.

    - `person.dob.day` (integer, required)
      The day of birth, between 1 and 31.

    - `person.dob.month` (integer, required)
      The month of birth, between 1 and 12.

    - `person.dob.year` (integer, required)
      The four-digit year of birth.

  - `person.documents` (object, optional)
    Documents that may be submitted to satisfy various informational requests.

    - `person.documents.company_authorization` (object, optional)
      One or more documents that demonstrate proof that this person is authorized to represent the company.

      - `person.documents.company_authorization.files` (array of strings, optional)
        One or more document ids returned by a [file upload](https://docs.stripe.com/api/tokens/create_person.md#create_file) with a `purpose` value of `account_requirement`.

    - `person.documents.passport` (object, optional)
      One or more documents showing the person’s passport page with photo and personal data.

      - `person.documents.passport.files` (array of strings, optional)
        One or more document ids returned by a [file upload](https://docs.stripe.com/api/tokens/create_person.md#create_file) with a `purpose` value of `account_requirement`.

    - `person.documents.visa` (object, optional)
      One or more documents showing the person’s visa required for living in the country where they are residing.

      - `person.documents.visa.files` (array of strings, optional)
        One or more document ids returned by a [file upload](https://docs.stripe.com/api/tokens/create_person.md#create_file) with a `purpose` value of `account_requirement`.

  - `person.email` (string, optional)
    The person’s email address.

    The maximum length is 800 characters.

  - `person.first_name` (string, optional)
    The person’s first name.

  - `person.first_name_kana` (string, optional)
    The Kana variation of the person’s first name (Japan only).

  - `person.first_name_kanji` (string, optional)
    The Kanji variation of the person’s first name (Japan only).

  - `person.full_name_aliases` (array of strings, optional)
    A list of alternate names or aliases that the person is known by.

  - `person.gender` (enum, optional)
    The person’s gender (International regulations require either “male” or “female”).

  - `person.id_number` (string, optional)
    The person’s ID number, as appropriate for their country. For example, a social security number in the U.S., social insurance number in Canada, etc. Instead of the number itself, you can also provide a [PII token provided by Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii).

  - `person.id_number_secondary` (string, optional)
    The person’s secondary ID number, as appropriate for their country, will be used for enhanced verification checks. In Thailand, this would be the laser code found on the back of an ID card. Instead of the number itself, you can also provide a [PII token provided by Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii).

  - `person.last_name` (string, optional)
    The person’s last name.

  - `person.last_name_kana` (string, optional)
    The Kana variation of the person’s last name (Japan only).

  - `person.last_name_kanji` (string, optional)
    The Kanji variation of the person’s last name (Japan only).

  - `person.maiden_name` (string, optional)
    The person’s maiden name.

  - `person.metadata` (object, optional)
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

  - `person.nationality` (string, optional)
    The country where the person is a national. Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)), or “XX” if unavailable.

  - `person.phone` (string, optional)
    The person’s phone number.

  - `person.political_exposure` (enum, optional)
    Indicates if the person or any of their representatives, family members, or other closely related persons, declares that they hold or have held an important public job or function, in any jurisdiction.
Possible enum values:
    - `existing`
      The person has disclosed that they do have political exposure

    - `none`
      The person has disclosed that they have no political exposure

  - `person.registered_address` (object, optional)
    The person’s registered address.

    - `person.registered_address.city` (string, optional)
      City, district, suburb, town, or village.

      The maximum length is 100 characters.

    - `person.registered_address.country` (string, optional)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `person.registered_address.line1` (string, optional)
      Address line 1, such as the street, PO Box, or company name.

      The maximum length is 200 characters.

    - `person.registered_address.line2` (string, optional)
      Address line 2, such as the apartment, suite, unit, or building.

      The maximum length is 200 characters.

    - `person.registered_address.postal_code` (string, optional)
      ZIP or postal code.

    - `person.registered_address.state` (string, optional)
      State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

  - `person.relationship` (object, optional)
    The relationship that this person has with the account’s legal entity.

    - `person.relationship.authorizer` (boolean, optional)
      Whether the person is the authorizer of the account’s representative.

    - `person.relationship.director` (boolean, optional)
      Whether the person is a director of the account’s legal entity. Directors are typically members of the governing board of the company, or responsible for ensuring the company meets its regulatory obligations.

    - `person.relationship.executive` (boolean, optional)
      Whether the person has significant responsibility to control, manage, or direct the organization.

    - `person.relationship.legal_guardian` (boolean, optional)
      Whether the person is the legal guardian of the account’s representative.

    - `person.relationship.owner` (boolean, optional)
      Whether the person is an owner of the account’s legal entity.

    - `person.relationship.percent_ownership` (float, optional)
      The percent owned by the person of the account’s legal entity.

    - `person.relationship.representative` (boolean, optional)
      Whether the person is authorized as the primary representative of the account. This is the person nominated by the business to provide information about themselves, and general information about the account. There can only be one representative at any given time. At the time the account is created, this person should be set to the person responsible for opening the account.

    - `person.relationship.title` (string, optional)
      The person’s title (e.g., CEO, Support Engineer).

  - `person.ssn_last_4` (string, optional)
    The last four digits of the person’s Social Security number (U.S. only).

  - `person.us_cfpb_data` (object, optional)
    Demographic data related to the person.

    - `person.us_cfpb_data.ethnicity_details` (object, optional)
      The persons ethnicity details

      - `person.us_cfpb_data.ethnicity_details.ethnicity` (array of enums, optional)
        The persons ethnicity

      - `person.us_cfpb_data.ethnicity_details.ethnicity_other` (string, optional)
        Please specify your origin, when other is selected.

    - `person.us_cfpb_data.race_details` (object, optional)
      The persons race details

      - `person.us_cfpb_data.race_details.race` (array of enums, optional)
        The persons race.

      - `person.us_cfpb_data.race_details.race_other` (string, optional)
        Please specify your race, when other is selected.

    - `person.us_cfpb_data.self_identified_gender` (string, optional)
      The persons self-identified gender

  - `person.verification` (object, optional)
    The person’s verification status.

    - `person.verification.additional_document` (object, optional)
      A document showing address, either a passport, local ID card, or utility bill from a well-known utility company.

      - `person.verification.additional_document.back` (string, optional)
        The back of an ID returned by a [file upload](https://docs.stripe.com/api/tokens/create_person.md#create_file) with a `purpose` value of `identity_document`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

        The maximum length is 500 characters.

      - `person.verification.additional_document.front` (string, optional)
        The front of an ID returned by a [file upload](https://docs.stripe.com/api/tokens/create_person.md#create_file) with a `purpose` value of `identity_document`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

        The maximum length is 500 characters.

    - `person.verification.document` (object, optional)
      An identifying document, either a passport or local ID card.

      - `person.verification.document.back` (string, optional)
        The back of an ID returned by a [file upload](https://docs.stripe.com/api/tokens/create_person.md#create_file) with a `purpose` value of `identity_document`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

        The maximum length is 500 characters.

      - `person.verification.document.front` (string, optional)
        The front of an ID returned by a [file upload](https://docs.stripe.com/api/tokens/create_person.md#create_file) with a `purpose` value of `identity_document`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

        The maximum length is 500 characters.

```curl
curl https://api.stripe.com/v1/tokens \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "person[first_name]"=Jane \
  -d "person[last_name]"=Doe \
  -d "person[relationship][owner]"=true
```

```cli
stripe tokens create  \
  -d "person[first_name]"=Jane \
  -d "person[last_name]"=Doe \
  -d "person[relationship][owner]"=true
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

token = client.v1.tokens.create({
  person: {
    first_name: 'Jane',
    last_name: 'Doe',
    relationship: {owner: true},
  },
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

token = client.v1.tokens.create({
  "person": {
    "first_name": "Jane",
    "last_name": "Doe",
    "relationship": {"owner": True},
  },
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$token = $stripe->tokens->create([
  'person' => [
    'first_name' => 'Jane',
    'last_name' => 'Doe',
    'relationship' => ['owner' => true],
  ],
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TokenCreateParams params =
  TokenCreateParams.builder()
    .setPerson(
      TokenCreateParams.Person.builder()
        .setFirstName("Jane")
        .setLastName("Doe")
        .setRelationship(
          TokenCreateParams.Person.Relationship.builder().setOwner(true).build()
        )
        .build()
    )
    .build();

Token token = client.v1().tokens().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const token = await stripe.tokens.create({
  person: {
    first_name: 'Jane',
    last_name: 'Doe',
    relationship: {
      owner: true,
    },
  },
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TokenCreateParams{
  Person: &stripe.PersonParams{
    FirstName: stripe.String("Jane"),
    LastName: stripe.String("Doe"),
    Relationship: &stripe.PersonRelationshipParams{Owner: stripe.Bool(true)},
  },
}
result, err := sc.V1Tokens.Create(context.TODO(), params)
```

```dotnet
var options = new TokenCreateOptions
{
    Person = new TokenPersonOptions
    {
        FirstName = "Jane",
        LastName = "Doe",
        Relationship = new TokenPersonRelationshipOptions { Owner = true },
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Tokens;
Token token = service.Create(options);
```

### Response

```json
{
  "id": "cpt_1EDww82eZvKYlo2CsdelTHFu",
  "object": "token",
  "client_ip": "8.21.168.117",
  "created": 1552582904,
  "livemode": false,
  "redaction": null,
  "type": "person",
  "used": false
}
```