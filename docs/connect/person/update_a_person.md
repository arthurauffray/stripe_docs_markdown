# Update a person

Updates an existing person.

## Returns

Returns a [`person`](https://docs.stripe.com/api/persons/object.md) object.

## Parameters

- `additional_tos_acceptances` (object, optional)
  Details on the legal guardian’s or authorizer’s acceptance of the required Stripe agreements.

  - `additional_tos_acceptances.account` (object, optional)
    Details on the legal guardian’s acceptance of the main Stripe service agreement.

    - `additional_tos_acceptances.account.date` (timestamp, required if IP or user_agent is provided)
      The Unix timestamp marking when the account representative accepted the service agreement.

    - `additional_tos_acceptances.account.ip` (string, required if date or user_agent is provided)
      The IP address from which the account representative accepted the service agreement.

    - `additional_tos_acceptances.account.user_agent` (string, optional)
      The user agent of the browser from which the account representative accepted the service agreement.

- `address` (object, optional)
  The person’s address.

  - `address.city` (string, optional)
    City, district, suburb, town, or village.

    The maximum length is 100 characters.

  - `address.country` (string, optional)
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

  - `address.line1` (string, optional)
    Address line 1, such as the street, PO Box, or company name.

    The maximum length is 200 characters.

  - `address.line2` (string, optional)
    Address line 2, such as the apartment, suite, unit, or building.

    The maximum length is 200 characters.

  - `address.postal_code` (string, optional)
    ZIP or postal code.

  - `address.state` (string, optional)
    State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

- `address_kana` (object, optional)
  The Kana variation of the person’s address (Japan only).

  - `address_kana.city` (string, optional)
    City or ward.

  - `address_kana.country` (string, optional)
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

  - `address_kana.line1` (string, optional)
    Block or building number.

  - `address_kana.line2` (string, optional)
    Building details.

  - `address_kana.postal_code` (string, optional)
    Postal code.

  - `address_kana.state` (string, optional)
    Prefecture.

  - `address_kana.town` (string, optional)
    Town or cho-me.

- `address_kanji` (object, optional)
  The Kanji variation of the person’s address (Japan only).

  - `address_kanji.city` (string, optional)
    City or ward.

  - `address_kanji.country` (string, optional)
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

  - `address_kanji.line1` (string, optional)
    Block or building number.

  - `address_kanji.line2` (string, optional)
    Building details.

  - `address_kanji.postal_code` (string, optional)
    Postal code.

  - `address_kanji.state` (string, optional)
    Prefecture.

  - `address_kanji.town` (string, optional)
    Town or cho-me.

- `dob` (object, optional)
  The person’s date of birth.

  - `dob.day` (integer, required)
    The day of birth, between 1 and 31.

  - `dob.month` (integer, required)
    The month of birth, between 1 and 12.

  - `dob.year` (integer, required)
    The four-digit year of birth.

- `documents` (object, optional)
  Documents that may be submitted to satisfy various informational requests.

  - `documents.company_authorization` (object, optional)
    One or more documents that demonstrate proof that this person is authorized to represent the company.

    - `documents.company_authorization.files` (array of strings, optional)
      One or more document ids returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a `purpose` value of `account_requirement`.

  - `documents.passport` (object, optional)
    One or more documents showing the person’s passport page with photo and personal data.

    - `documents.passport.files` (array of strings, optional)
      One or more document ids returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a `purpose` value of `account_requirement`.

  - `documents.visa` (object, optional)
    One or more documents showing the person’s visa required for living in the country where they are residing.

    - `documents.visa.files` (array of strings, optional)
      One or more document ids returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a `purpose` value of `account_requirement`.

- `email` (string, optional)
  The person’s email address.

  The maximum length is 800 characters.

- `first_name` (string, optional)
  The person’s first name.

- `first_name_kana` (string, optional)
  The Kana variation of the person’s first name (Japan only).

- `first_name_kanji` (string, optional)
  The Kanji variation of the person’s first name (Japan only).

- `full_name_aliases` (array of strings, optional)
  A list of alternate names or aliases that the person is known by.

- `gender` (enum, optional)
  The person’s gender (International regulations require either “male” or “female”).

- `id_number` (string, optional)
  The person’s ID number, as appropriate for their country. For example, a social security number in the U.S., social insurance number in Canada, etc. Instead of the number itself, you can also provide a [PII token provided by Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii).

- `id_number_secondary` (string, optional)
  The person’s secondary ID number, as appropriate for their country, will be used for enhanced verification checks. In Thailand, this would be the laser code found on the back of an ID card. Instead of the number itself, you can also provide a [PII token provided by Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii).

- `last_name` (string, optional)
  The person’s last name.

- `last_name_kana` (string, optional)
  The Kana variation of the person’s last name (Japan only).

- `last_name_kanji` (string, optional)
  The Kanji variation of the person’s last name (Japan only).

- `maiden_name` (string, optional)
  The person’s maiden name.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `nationality` (string, optional)
  The country where the person is a national. Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)), or “XX” if unavailable.

- `person_token` (string, optional)
  A [person token](https://docs.stripe.com/connect/account-tokens.md), used to securely provide details to the person.

- `phone` (string, optional)
  The person’s phone number.

- `political_exposure` (enum, optional)
  Indicates if the person or any of their representatives, family members, or other closely related persons, declares that they hold or have held an important public job or function, in any jurisdiction.
Possible enum values:
  - `existing`
    The person has disclosed that they do have political exposure

  - `none`
    The person has disclosed that they have no political exposure

- `registered_address` (object, optional)
  The person’s registered address.

  - `registered_address.city` (string, optional)
    City, district, suburb, town, or village.

    The maximum length is 100 characters.

  - `registered_address.country` (string, optional)
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

  - `registered_address.line1` (string, optional)
    Address line 1, such as the street, PO Box, or company name.

    The maximum length is 200 characters.

  - `registered_address.line2` (string, optional)
    Address line 2, such as the apartment, suite, unit, or building.

    The maximum length is 200 characters.

  - `registered_address.postal_code` (string, optional)
    ZIP or postal code.

  - `registered_address.state` (string, optional)
    State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

- `relationship` (object, optional)
  The relationship that this person has with the account’s legal entity.

  - `relationship.authorizer` (boolean, optional)
    Whether the person is the authorizer of the account’s representative.

  - `relationship.director` (boolean, optional)
    Whether the person is a director of the account’s legal entity. Directors are typically members of the governing board of the company, or responsible for ensuring the company meets its regulatory obligations.

  - `relationship.executive` (boolean, optional)
    Whether the person has significant responsibility to control, manage, or direct the organization.

  - `relationship.legal_guardian` (boolean, optional)
    Whether the person is the legal guardian of the account’s representative.

  - `relationship.owner` (boolean, optional)
    Whether the person is an owner of the account’s legal entity.

  - `relationship.percent_ownership` (float, optional)
    The percent owned by the person of the account’s legal entity.

  - `relationship.representative` (boolean, optional)
    Whether the person is authorized as the primary representative of the account. This is the person nominated by the business to provide information about themselves, and general information about the account. There can only be one representative at any given time. At the time the account is created, this person should be set to the person responsible for opening the account.

  - `relationship.title` (string, optional)
    The person’s title (e.g., CEO, Support Engineer).

- `ssn_last_4` (string, optional)
  The last four digits of the person’s Social Security number (U.S. only).

- `us_cfpb_data` (object, optional)
  Demographic data related to the person.

  - `us_cfpb_data.ethnicity_details` (object, optional)
    The persons ethnicity details

    - `us_cfpb_data.ethnicity_details.ethnicity` (array of enums, optional)
      The persons ethnicity

    - `us_cfpb_data.ethnicity_details.ethnicity_other` (string, optional)
      Please specify your origin, when other is selected.

  - `us_cfpb_data.race_details` (object, optional)
    The persons race details

    - `us_cfpb_data.race_details.race` (array of enums, optional)
      The persons race.

    - `us_cfpb_data.race_details.race_other` (string, optional)
      Please specify your race, when other is selected.

  - `us_cfpb_data.self_identified_gender` (string, optional)
    The persons self-identified gender

- `verification` (object, optional)
  The person’s verification status.

  - `verification.additional_document` (object, optional)
    A document showing address, either a passport, local ID card, or utility bill from a well-known utility company.

    - `verification.additional_document.back` (string, optional)
      The back of an ID returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a `purpose` value of `identity_document`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

      The maximum length is 500 characters.

    - `verification.additional_document.front` (string, optional)
      The front of an ID returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a `purpose` value of `identity_document`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

      The maximum length is 500 characters.

  - `verification.document` (object, optional)
    An identifying document, either a passport or local ID card.

    - `verification.document.back` (string, optional)
      The back of an ID returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a `purpose` value of `identity_document`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

      The maximum length is 500 characters.

    - `verification.document.front` (string, optional)
      The front of an ID returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a `purpose` value of `identity_document`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

      The maximum length is 500 characters.

```curl
curl https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/persons/person_1MqjB62eZvKYlo2CaeEJzKVR \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
```

```cli
stripe persons update acct_1032D82eZvKYlo2C person_1MqjB62eZvKYlo2CaeEJzKVR \
  -d "metadata[order_id]"=6735
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

person = client.v1.accounts.persons.update(
  'acct_1032D82eZvKYlo2C',
  'person_1MqjB62eZvKYlo2CaeEJzKVR',
  {metadata: {order_id: '6735'}},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

person = client.v1.accounts.persons.update(
  "acct_1032D82eZvKYlo2C",
  "person_1MqjB62eZvKYlo2CaeEJzKVR",
  {"metadata": {"order_id": "6735"}},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$person = $stripe->accounts->updatePerson(
  'acct_1032D82eZvKYlo2C',
  'person_1MqjB62eZvKYlo2CaeEJzKVR',
  ['metadata' => ['order_id' => '6735']]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AccountPersonUpdateParams params =
  AccountPersonUpdateParams.builder().putMetadata("order_id", "6735").build();

Person person =
  client.v1().accounts().persons().update(
    "acct_1032D82eZvKYlo2C",
    "person_1MqjB62eZvKYlo2CaeEJzKVR",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const person = await stripe.accounts.updatePerson(
  'acct_1032D82eZvKYlo2C',
  'person_1MqjB62eZvKYlo2CaeEJzKVR',
  {
    metadata: {
      order_id: '6735',
    },
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PersonUpdateParams{Account: stripe.String("acct_1032D82eZvKYlo2C")}
params.AddMetadata("order_id", "6735")
result, err := sc.V1Persons.Update(
  context.TODO(), "person_1MqjB62eZvKYlo2CaeEJzKVR", params)
```

```dotnet
var options = new AccountPersonUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Accounts.Persons;
Person person = service.Update(
    "acct_1032D82eZvKYlo2C",
    "person_1MqjB62eZvKYlo2CaeEJzKVR",
    options);
```

### Response

```json
{
  "id": "person_1MqjB62eZvKYlo2CaeEJzKVR",
  "person": "person_1MqjB62eZvKYlo2CaeEJzKVR",
  "object": "person",
  "account": "acct_1032D82eZvKYlo2C",
  "created": 1680035496,
  "dob": {
    "day": null,
    "month": null,
    "year": null
  },
  "first_name": "Jane",
  "future_requirements": {
    "alternatives": [],
    "currently_due": [],
    "errors": [],
    "eventually_due": [],
    "past_due": [],
    "pending_verification": []
  },
  "id_number_provided": false,
  "last_name": "Diaz",
  "metadata": {
    "order_id": "6735"
  },
  "relationship": {
    "director": false,
    "executive": false,
    "owner": false,
    "percent_ownership": null,
    "representative": false,
    "title": null
  },
  "requirements": {
    "alternatives": [],
    "currently_due": [],
    "errors": [],
    "eventually_due": [],
    "past_due": [],
    "pending_verification": []
  },
  "ssn_last_4_provided": false,
  "verification": {
    "additional_document": {
      "back": null,
      "details": null,
      "details_code": null,
      "front": null
    },
    "details": null,
    "details_code": null,
    "document": {
      "back": null,
      "details": null,
      "details_code": null,
      "front": null
    },
    "status": "unverified"
  }
}
```