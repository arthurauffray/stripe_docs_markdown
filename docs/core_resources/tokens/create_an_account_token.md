# Create an account token

Creates a single-use token that wraps a user’s legal entity information. Use this when creating or updating a Connect account. Learn more about [account tokens](https://docs.stripe.com/docs/connect/account-tokens.md).

In live mode, you can only create account tokens with your application’s publishable key. In test mode, you can only create account tokens with your secret key or publishable key.

## Returns

Returns the created account token if it’s successful. Otherwise, this call raises [an error](https://docs.stripe.com/api/tokens/create_account.md#errors).

## Parameters

- `account` (object, required)
  Information for the account this token represents.

  - `account.business_type` (enum, optional)
    The business type.
Possible enum values:
    - `company`
    - `government_entity`
      US only

    - `individual`
    - `non_profit`

  - `account.company` (object, optional)
    Information about the company or business.

    - `account.company.address` (object, optional)
      The company’s primary address.

      - `account.company.address.city` (string, optional)
        City, district, suburb, town, or village.

        The maximum length is 100 characters.

      - `account.company.address.country` (string, optional)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `account.company.address.line1` (string, optional)
        Address line 1, such as the street, PO Box, or company name.

        The maximum length is 200 characters.

      - `account.company.address.line2` (string, optional)
        Address line 2, such as the apartment, suite, unit, or building.

        The maximum length is 200 characters.

      - `account.company.address.postal_code` (string, optional)
        ZIP or postal code.

      - `account.company.address.state` (string, optional)
        State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

    - `account.company.address_kana` (object, optional)
      The Kana variation of the company’s primary address (Japan only).

      - `account.company.address_kana.city` (string, optional)
        City or ward.

      - `account.company.address_kana.country` (string, optional)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `account.company.address_kana.line1` (string, optional)
        Block or building number.

      - `account.company.address_kana.line2` (string, optional)
        Building details.

      - `account.company.address_kana.postal_code` (string, optional)
        Postal code.

      - `account.company.address_kana.state` (string, optional)
        Prefecture.

      - `account.company.address_kana.town` (string, optional)
        Town or cho-me.

    - `account.company.address_kanji` (object, optional)
      The Kanji variation of the company’s primary address (Japan only).

      - `account.company.address_kanji.city` (string, optional)
        City or ward.

      - `account.company.address_kanji.country` (string, optional)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `account.company.address_kanji.line1` (string, optional)
        Block or building number.

      - `account.company.address_kanji.line2` (string, optional)
        Building details.

      - `account.company.address_kanji.postal_code` (string, optional)
        Postal code.

      - `account.company.address_kanji.state` (string, optional)
        Prefecture.

      - `account.company.address_kanji.town` (string, optional)
        Town or cho-me.

    - `account.company.directors_provided` (boolean, optional)
      Whether the company’s directors have been provided. Set this Boolean to `true` after creating all the company’s directors with [the Persons API](https://docs.stripe.com/api/persons.md) for accounts with a `relationship.director` requirement. This value is not automatically set to `true` after creating directors, so it needs to be updated to indicate all directors have been provided.

    - `account.company.directorship_declaration` (object, optional)
      This hash is used to attest that the directors information provided to Stripe is both current and correct.

      - `account.company.directorship_declaration.date` (timestamp, optional)
        The Unix timestamp marking when the directorship declaration attestation was made.

      - `account.company.directorship_declaration.ip` (string, optional)
        The IP address from which the directorship declaration attestation was made.

      - `account.company.directorship_declaration.user_agent` (string, optional)
        The user agent of the browser from which the directorship declaration attestation was made.

    - `account.company.executives_provided` (boolean, optional)
      Whether the company’s executives have been provided. Set this Boolean to `true` after creating all the company’s executives with [the Persons API](https://docs.stripe.com/api/persons.md) for accounts with a `relationship.executive` requirement.

    - `account.company.export_license_id` (string, optional)
      The export license ID number of the company, also referred as Import Export Code (India only).

    - `account.company.export_purpose_code` (string, optional)
      The purpose code to use for export transactions (India only).

    - `account.company.name` (string, optional)
      The company’s legal name.

      The maximum length is 100 characters.

    - `account.company.name_kana` (string, optional)
      The Kana variation of the company’s legal name (Japan only).

      The maximum length is 100 characters.

    - `account.company.name_kanji` (string, optional)
      The Kanji variation of the company’s legal name (Japan only).

      The maximum length is 100 characters.

    - `account.company.owners_provided` (boolean, optional)
      Whether the company’s owners have been provided. Set this Boolean to `true` after creating all the company’s owners with [the Persons API](https://docs.stripe.com/api/persons.md) for accounts with a `relationship.owner` requirement.

    - `account.company.ownership_declaration` (object, optional)
      This hash is used to attest that the beneficial owner information provided to Stripe is both current and correct.

      - `account.company.ownership_declaration.date` (timestamp, optional)
        The Unix timestamp marking when the beneficial owner attestation was made.

      - `account.company.ownership_declaration.ip` (string, optional)
        The IP address from which the beneficial owner attestation was made.

      - `account.company.ownership_declaration.user_agent` (string, optional)
        The user agent of the browser from which the beneficial owner attestation was made.

    - `account.company.ownership_declaration_shown_and_signed` (boolean, optional)
      Whether the user described by the data in the token has been shown the Ownership Declaration and indicated that it is correct.

    - `account.company.ownership_exemption_reason` (enum, optional)
      This value is used to determine if a business is exempt from providing ultimate beneficial owners. See [this support article](https://support.stripe.com/questions/exemption-from-providing-ownership-details) and [changelog](https://docs.stripe.com/changelog/acacia/2025-01-27/ownership-exemption-reason-accounts-api.md) for more details.

    - `account.company.phone` (string, optional)
      The company’s phone number (used for verification).

    - `account.company.registration_date` (object, optional)
      When the business was incorporated or registered.

      - `account.company.registration_date.day` (integer, required)
        The day of registration, between 1 and 31.

      - `account.company.registration_date.month` (integer, required)
        The month of registration, between 1 and 12.

      - `account.company.registration_date.year` (integer, required)
        The four-digit year of registration.

    - `account.company.registration_number` (string, optional)
      The identification number given to a company when it is registered or incorporated, if distinct from the identification number used for filing taxes. (Examples are the CIN for companies and LLP IN for partnerships in India, and the Company Registration Number in Hong Kong).

    - `account.company.representative_declaration` (object, optional)
      This hash is used to attest that the representative is authorized to act as the representative of their legal entity.

      - `account.company.representative_declaration.date` (timestamp, optional)
        The Unix timestamp marking when the representative declaration attestation was made.

      - `account.company.representative_declaration.ip` (string, optional)
        The IP address from which the representative declaration attestation was made.

      - `account.company.representative_declaration.user_agent` (string, optional)
        The user agent of the browser from which the representative declaration attestation was made.

    - `account.company.structure` (enum, optional)
      The category identifying the legal structure of the company or legal entity. See [Business structure](https://docs.stripe.com/connect/identity-verification.md#business-structure) for more details. Pass an empty string to unset this value.

    - `account.company.tax_id` (string, optional)
      The business ID number of the company, as appropriate for the company’s country. (Examples are an Employer ID Number in the U.S., a Business Number in Canada, or a Company Number in the UK.)

    - `account.company.tax_id_registrar` (string, optional)
      The jurisdiction in which the `tax_id` is registered (Germany-based companies only).

    - `account.company.vat_id` (string, optional)
      The VAT number of the company.

    - `account.company.verification` (object, optional)
      Information on the verification state of the company.

      - `account.company.verification.document` (object, optional)
        A document verifying the business.

        - `account.company.verification.document.back` (string, optional)
          The back of a document returned by a [file upload](https://docs.stripe.com/api/tokens/create_account.md#create_file) with a `purpose` value of `additional_verification`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

          The maximum length is 500 characters.

        - `account.company.verification.document.front` (string, optional)
          The front of a document returned by a [file upload](https://docs.stripe.com/api/tokens/create_account.md#create_file) with a `purpose` value of `additional_verification`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

          The maximum length is 500 characters.

  - `account.individual` (object, optional)
    Information about the person represented by the account.

    - `account.individual.address` (object, optional)
      The individual’s primary address.

      - `account.individual.address.city` (string, optional)
        City, district, suburb, town, or village.

        The maximum length is 100 characters.

      - `account.individual.address.country` (string, optional)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `account.individual.address.line1` (string, optional)
        Address line 1, such as the street, PO Box, or company name.

        The maximum length is 200 characters.

      - `account.individual.address.line2` (string, optional)
        Address line 2, such as the apartment, suite, unit, or building.

        The maximum length is 200 characters.

      - `account.individual.address.postal_code` (string, optional)
        ZIP or postal code.

      - `account.individual.address.state` (string, optional)
        State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

    - `account.individual.address_kana` (object, optional)
      The Kana variation of the individual’s primary address (Japan only).

      - `account.individual.address_kana.city` (string, optional)
        City or ward.

      - `account.individual.address_kana.country` (string, optional)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `account.individual.address_kana.line1` (string, optional)
        Block or building number.

      - `account.individual.address_kana.line2` (string, optional)
        Building details.

      - `account.individual.address_kana.postal_code` (string, optional)
        Postal code.

      - `account.individual.address_kana.state` (string, optional)
        Prefecture.

      - `account.individual.address_kana.town` (string, optional)
        Town or cho-me.

    - `account.individual.address_kanji` (object, optional)
      The Kanji variation of the individual’s primary address (Japan only).

      - `account.individual.address_kanji.city` (string, optional)
        City or ward.

      - `account.individual.address_kanji.country` (string, optional)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `account.individual.address_kanji.line1` (string, optional)
        Block or building number.

      - `account.individual.address_kanji.line2` (string, optional)
        Building details.

      - `account.individual.address_kanji.postal_code` (string, optional)
        Postal code.

      - `account.individual.address_kanji.state` (string, optional)
        Prefecture.

      - `account.individual.address_kanji.town` (string, optional)
        Town or cho-me.

    - `account.individual.dob` (object, optional)
      The individual’s date of birth.

      - `account.individual.dob.day` (integer, required)
        The day of birth, between 1 and 31.

      - `account.individual.dob.month` (integer, required)
        The month of birth, between 1 and 12.

      - `account.individual.dob.year` (integer, required)
        The four-digit year of birth.

    - `account.individual.email` (string, optional)
      The individual’s email address.

      The maximum length is 800 characters.

    - `account.individual.first_name` (string, optional)
      The individual’s first name.

      The maximum length is 100 characters.

    - `account.individual.first_name_kana` (string, optional)
      The Kana variation of the individual’s first name (Japan only).

    - `account.individual.first_name_kanji` (string, optional)
      The Kanji variation of the individual’s first name (Japan only).

    - `account.individual.full_name_aliases` (array of strings, optional)
      A list of alternate names or aliases that the individual is known by.

    - `account.individual.gender` (enum, optional)
      The individual’s gender

    - `account.individual.id_number` (string, optional)
      The government-issued ID number of the individual, as appropriate for the representative’s country. (Examples are a Social Security Number in the U.S., or a Social Insurance Number in Canada). Instead of the number itself, you can also provide a [PII token created with Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii).

    - `account.individual.id_number_secondary` (string, optional)
      The government-issued secondary ID number of the individual, as appropriate for the representative’s country, will be used for enhanced verification checks. In Thailand, this would be the laser code found on the back of an ID card. Instead of the number itself, you can also provide a [PII token created with Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii).

    - `account.individual.last_name` (string, optional)
      The individual’s last name.

      The maximum length is 100 characters.

    - `account.individual.last_name_kana` (string, optional)
      The Kana variation of the individual’s last name (Japan only).

    - `account.individual.last_name_kanji` (string, optional)
      The Kanji variation of the individual’s last name (Japan only).

    - `account.individual.maiden_name` (string, optional)
      The individual’s maiden name.

    - `account.individual.metadata` (object, optional)
      Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

    - `account.individual.phone` (string, optional)
      The individual’s phone number.

    - `account.individual.political_exposure` (enum, optional)
      Indicates if the person or any of their representatives, family members, or other closely related persons, declares that they hold or have held an important public job or function, in any jurisdiction.
Possible enum values:
      - `existing`
        The person has disclosed that they do have political exposure

      - `none`
        The person has disclosed that they have no political exposure

    - `account.individual.registered_address` (object, optional)
      The individual’s registered address.

      - `account.individual.registered_address.city` (string, optional)
        City, district, suburb, town, or village.

        The maximum length is 100 characters.

      - `account.individual.registered_address.country` (string, optional)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `account.individual.registered_address.line1` (string, optional)
        Address line 1, such as the street, PO Box, or company name.

        The maximum length is 200 characters.

      - `account.individual.registered_address.line2` (string, optional)
        Address line 2, such as the apartment, suite, unit, or building.

        The maximum length is 200 characters.

      - `account.individual.registered_address.postal_code` (string, optional)
        ZIP or postal code.

      - `account.individual.registered_address.state` (string, optional)
        State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

    - `account.individual.relationship` (object, optional)
      Describes the person’s relationship to the account.

      - `account.individual.relationship.director` (boolean, optional)
        Whether the person is a director of the account’s legal entity. Directors are typically members of the governing board of the company, or responsible for ensuring the company meets its regulatory obligations.

      - `account.individual.relationship.executive` (boolean, optional)
        Whether the person has significant responsibility to control, manage, or direct the organization.

      - `account.individual.relationship.owner` (boolean, optional)
        Whether the person is an owner of the account’s legal entity.

      - `account.individual.relationship.percent_ownership` (float, optional)
        The percent owned by the person of the account’s legal entity.

      - `account.individual.relationship.title` (string, optional)
        The person’s title (e.g., CEO, Support Engineer).

    - `account.individual.ssn_last_4` (string, optional)
      The last four digits of the individual’s Social Security Number (U.S. only).

    - `account.individual.verification` (object, optional)
      The individual’s verification document information.

      - `account.individual.verification.additional_document` (object, optional)
        A document showing address, either a passport, local ID card, or utility bill from a well-known utility company.

        - `account.individual.verification.additional_document.back` (string, optional)
          The back of an ID returned by a [file upload](https://docs.stripe.com/api/tokens/create_account.md#create_file) with a `purpose` value of `identity_document`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

          The maximum length is 500 characters.

        - `account.individual.verification.additional_document.front` (string, optional)
          The front of an ID returned by a [file upload](https://docs.stripe.com/api/tokens/create_account.md#create_file) with a `purpose` value of `identity_document`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

          The maximum length is 500 characters.

      - `account.individual.verification.document` (object, optional)
        An identifying document, either a passport or local ID card.

        - `account.individual.verification.document.back` (string, optional)
          The back of an ID returned by a [file upload](https://docs.stripe.com/api/tokens/create_account.md#create_file) with a `purpose` value of `identity_document`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

          The maximum length is 500 characters.

        - `account.individual.verification.document.front` (string, optional)
          The front of an ID returned by a [file upload](https://docs.stripe.com/api/tokens/create_account.md#create_file) with a `purpose` value of `identity_document`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

          The maximum length is 500 characters.

  - `account.tos_shown_and_accepted` (boolean, optional)
    Whether the user described by the data in the token has been shown [the Stripe Connected Account Agreement](https://docs.stripe.com/connect/account-tokens.md#stripe-connected-account-agreement). When creating an account token to create a new Connect account, this value must be `true`.

```curl
curl https://api.stripe.com/v1/tokens \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "account[business_type]"=individual \
  -d "account[individual][first_name]"=Jane \
  -d "account[individual][last_name]"=Doe \
  -d "account[tos_shown_and_accepted]"=true
```

```cli
stripe tokens create  \
  -d "account[business_type]"=individual \
  -d "account[individual][first_name]"=Jane \
  -d "account[individual][last_name]"=Doe \
  -d "account[tos_shown_and_accepted]"=true
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

token = client.v1.tokens.create({
  account: {
    business_type: 'individual',
    individual: {
      first_name: 'Jane',
      last_name: 'Doe',
    },
    tos_shown_and_accepted: true,
  },
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

token = client.v1.tokens.create({
  "account": {
    "business_type": "individual",
    "individual": {"first_name": "Jane", "last_name": "Doe"},
    "tos_shown_and_accepted": True,
  },
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$token = $stripe->tokens->create([
  'account' => [
    'business_type' => 'individual',
    'individual' => [
      'first_name' => 'Jane',
      'last_name' => 'Doe',
    ],
    'tos_shown_and_accepted' => true,
  ],
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TokenCreateParams params =
  TokenCreateParams.builder()
    .setAccount(
      TokenCreateParams.Account.builder()
        .setBusinessType(TokenCreateParams.Account.BusinessType.INDIVIDUAL)
        .setIndividual(
          TokenCreateParams.Account.Individual.builder()
            .setFirstName("Jane")
            .setLastName("Doe")
            .build()
        )
        .setTosShownAndAccepted(true)
        .build()
    )
    .build();

Token token = client.v1().tokens().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const token = await stripe.tokens.create({
  account: {
    business_type: 'individual',
    individual: {
      first_name: 'Jane',
      last_name: 'Doe',
    },
    tos_shown_and_accepted: true,
  },
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TokenCreateParams{
  Account: &stripe.TokenCreateAccountParams{
    BusinessType: stripe.String("individual"),
    Individual: &stripe.PersonParams{
      FirstName: stripe.String("Jane"),
      LastName: stripe.String("Doe"),
    },
    TOSShownAndAccepted: stripe.Bool(true),
  },
}
result, err := sc.V1Tokens.Create(context.TODO(), params)
```

```dotnet
var options = new TokenCreateOptions
{
    Account = new TokenAccountOptions
    {
        BusinessType = "individual",
        Individual = new TokenAccountIndividualOptions
        {
            FirstName = "Jane",
            LastName = "Doe",
        },
        TosShownAndAccepted = true,
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Tokens;
Token token = service.Create(options);
```

### Response

```json
{
  "id": "ct_1BZ6xr2eZvKYlo2CsSOhuTfi",
  "object": "token",
  "client_ip": "104.198.25.169",
  "created": 1513297331,
  "livemode": false,
  "redaction": null,
  "type": "account",
  "used": false
}
```