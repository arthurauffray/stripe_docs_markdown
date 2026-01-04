# Create a cardholder

Creates a new Issuing `Cardholder` object that can be issued cards.

## Returns

Returns an Issuing `Cardholder` object if creation succeeds.

## Parameters

- `billing` (object, required)
  The cardholder’s billing address.

  - `billing.address` (object, required)
    The cardholder’s billing address.

    - `billing.address.city` (string, required)
      City, district, suburb, town, or village.

    - `billing.address.country` (string, required)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `billing.address.line1` (string, required)
      Address line 1, such as the street, PO Box, or company name.

    - `billing.address.postal_code` (string, required)
      ZIP or postal code.

    - `billing.address.line2` (string, optional)
      Address line 2, such as the apartment, suite, unit, or building.

    - `billing.address.state` (string, optional)
      State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

- `name` (string, required)
  The cardholder’s name. This will be printed on cards issued to them. The maximum length of this field is 24 characters. This field cannot contain any special characters or numbers.

- `company` (object, optional)
  Additional information about a `company` cardholder.

  - `company.tax_id` (string, optional)
    The entity’s business ID number.

- `email` (string, optional)
  The cardholder’s email address.

  The maximum length is 800 characters.

- `individual` (object, optional)
  Additional information about an `individual` cardholder.

  - `individual.card_issuing` (object, optional)
    Information related to the card_issuing program for this cardholder.

    - `individual.card_issuing.user_terms_acceptance` (object, optional)
      Information about cardholder acceptance of Celtic [Authorized User Terms](https://stripe.com/docs/issuing/cards#accept-authorized-user-terms). Required for cards backed by a Celtic program.

      - `individual.card_issuing.user_terms_acceptance.date` (timestamp, required if IP or user_agent is provided)
        The Unix timestamp marking when the cardholder accepted the Authorized User Terms. Required for Celtic Spend Card users.

      - `individual.card_issuing.user_terms_acceptance.ip` (string, required if date or user_agent is provided)
        The IP address from which the cardholder accepted the Authorized User Terms. Required for Celtic Spend Card users.

      - `individual.card_issuing.user_terms_acceptance.user_agent` (string, optional)
        The user agent of the browser from which the cardholder accepted the Authorized User Terms.

  - `individual.dob` (object, optional)
    The date of birth of this cardholder. Cardholders must be older than 13 years old.

    - `individual.dob.day` (integer, required)
      The day of birth, between 1 and 31.

    - `individual.dob.month` (integer, required)
      The month of birth, between 1 and 12.

    - `individual.dob.year` (integer, required)
      The four-digit year of birth.

  - `individual.first_name` (string, optional)
    The first name of this cardholder. Required before activating Cards. This field cannot contain any numbers, special characters (except periods, commas, hyphens, spaces and apostrophes) or non-latin letters.

  - `individual.last_name` (string, optional)
    The last name of this cardholder.  Required before activating Cards. This field cannot contain any numbers, special characters (except periods, commas, hyphens, spaces and apostrophes) or non-latin letters.

  - `individual.verification` (object, optional)
    Government-issued ID document for this cardholder.

    - `individual.verification.document` (object, optional)
      An identifying document, either a passport or local ID card.

      - `individual.verification.document.back` (string, optional)
        The back of an ID returned by a [file upload](https://docs.stripe.com/api/issuing/cardholders/create.md#create_file) with a `purpose` value of `identity_document`.

      - `individual.verification.document.front` (string, optional)
        The front of an ID returned by a [file upload](https://docs.stripe.com/api/issuing/cardholders/create.md#create_file) with a `purpose` value of `identity_document`.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `phone_number` (string, optional)
  The cardholder’s phone number. This will be transformed to [E.164](https://en.wikipedia.org/wiki/E.164) if it is not provided in that format already. This is required for all cardholders who will be creating EU cards. See the [3D Secure documentation](https://docs.stripe.com/docs/issuing/3d-secure.md#when-is-3d-secure-applied) for more details.

- `preferred_locales` (array of enums, optional)
  The cardholder’s preferred locales (languages), ordered by preference. Locales can be `de`, `en`, `es`, `fr`, or `it`. This changes the language of the [3D Secure flow](https://docs.stripe.com/docs/issuing/3d-secure.md) and one-time password messages sent to the cardholder.

- `spending_controls` (object, optional)
  Rules that control spending across this cardholder’s cards. Refer to our [documentation](https://docs.stripe.com/docs/issuing/controls/spending-controls.md) for more details.

  - `spending_controls.allowed_categories` (array of strings, optional)
    Array of strings containing [categories](https://docs.stripe.com/docs/api.md#issuing_authorization_object-merchant_data-category) of authorizations to allow. All other categories will be blocked. Cannot be set with `blocked_categories`.

  - `spending_controls.allowed_merchant_countries` (array of strings, optional)
    Array of strings containing representing countries from which authorizations will be allowed. Authorizations from merchants in all other countries will be declined. Country codes should be ISO 3166 alpha-2 country codes (e.g. `US`). Cannot be set with `blocked_merchant_countries`. Provide an empty value to unset this control.

  - `spending_controls.blocked_categories` (array of strings, optional)
    Array of strings containing [categories](https://docs.stripe.com/docs/api.md#issuing_authorization_object-merchant_data-category) of authorizations to decline. All other categories will be allowed. Cannot be set with `allowed_categories`.

  - `spending_controls.blocked_merchant_countries` (array of strings, optional)
    Array of strings containing representing countries from which authorizations will be declined. Country codes should be ISO 3166 alpha-2 country codes (e.g. `US`). Cannot be set with `allowed_merchant_countries`. Provide an empty value to unset this control.

  - `spending_controls.spending_limits` (array of objects, optional)
    Limit spending with amount-based rules that apply across this cardholder’s cards.

    - `spending_controls.spending_limits.amount` (integer, required)
      Maximum amount allowed to spend per interval.

    - `spending_controls.spending_limits.interval` (enum, required)
      Interval (or event) to which the amount applies.
Possible enum values:
      - `all_time`
        Limit applies to all transactions.

      - `daily`
        Limit applies to a day, starting at midnight UTC.

      - `monthly`
        Limit applies to a month, starting on the 1st at midnight UTC.

      - `per_authorization`
        Limit applies to each authorization.

      - `weekly`
        Limit applies to a week, starting on Sunday at midnight UTC.

      - `yearly`
        Limit applies to a year, starting on January 1st at midnight UTC.

    - `spending_controls.spending_limits.categories` (array of strings, optional)
      Array of strings containing [categories](https://docs.stripe.com/docs/api.md#issuing_authorization_object-merchant_data-category) this limit applies to. Omitting this field will apply the limit to all categories.

  - `spending_controls.spending_limits_currency` (string, optional)
    Currency of amounts within `spending_limits`. Defaults to your merchant country’s currency.

- `status` (enum, optional)
  Specifies whether to permit authorizations on this cardholder’s cards. Defaults to `active`.
Possible enum values:
  - `active`
    A platform has enabled the cardholder to approve authorizations made with cards attached to this cardholder. If Stripe’s review of the cardholder’s identity information isn’t complete, authorizations might be blocked, even if its `status` is `active`.

  - `inactive`
    Cards attached to this cardholder will decline all authorizations with a `cardholder_inactive` reason.

- `type` (enum, optional)
  One of `individual` or `company`. See [Choose a cardholder type](https://docs.stripe.com/docs/issuing/other/choose-cardholder.md) for more details.
Possible enum values:
  - `company`
    The cardholder is a company or business entity, and additional information includes their tax ID. This option may not be available if your [use case](https://docs.stripe.com/docs/issuing/other/choose-cardholder.md#find-your-use-case) only supports individual cardholders.

  - `individual`
    The cardholder is a person, and additional information includes first and last name, date of birth, etc. If you’re issuing Celtic Spend Cards, then Individual cardholders must accept Authorized User Terms prior to activating their card.

```curl
curl https://api.stripe.com/v1/issuing/cardholders \
  -u "<<YOUR_SECRET_KEY>>" \
  -d type=individual \
  -d name="Jenny Rosen" \
  --data-urlencode email="jenny.rosen@example.com" \
  --data-urlencode phone_number="+18888675309" \
  -d "billing[address][line1]"="1234 Main Street" \
  -d "billing[address][city]"="San Francisco" \
  -d "billing[address][state]"=CA \
  -d "billing[address][country]"=US \
  -d "billing[address][postal_code]"=94111
```

```cli
stripe issuing cardholders create  \
  --type=individual \
  --name="Jenny Rosen" \
  --email="jenny.rosen@example.com" \
  --phone-number="+18888675309" \
  -d "billing[address][line1]"="1234 Main Street" \
  -d "billing[address][city]"="San Francisco" \
  -d "billing[address][state]"=CA \
  -d "billing[address][country]"=US \
  -d "billing[address][postal_code]"=94111
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

cardholder = client.v1.issuing.cardholders.create({
  type: 'individual',
  name: 'Jenny Rosen',
  email: 'jenny.rosen@example.com',
  phone_number: '+18888675309',
  billing: {
    address: {
      line1: '1234 Main Street',
      city: 'San Francisco',
      state: 'CA',
      country: 'US',
      postal_code: '94111',
    },
  },
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

cardholder = client.v1.issuing.cardholders.create({
  "type": "individual",
  "name": "Jenny Rosen",
  "email": "jenny.rosen@example.com",
  "phone_number": "+18888675309",
  "billing": {
    "address": {
      "line1": "1234 Main Street",
      "city": "San Francisco",
      "state": "CA",
      "country": "US",
      "postal_code": "94111",
    },
  },
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$cardholder = $stripe->issuing->cardholders->create([
  'type' => 'individual',
  'name' => 'Jenny Rosen',
  'email' => 'jenny.rosen@example.com',
  'phone_number' => '+18888675309',
  'billing' => [
    'address' => [
      'line1' => '1234 Main Street',
      'city' => 'San Francisco',
      'state' => 'CA',
      'country' => 'US',
      'postal_code' => '94111',
    ],
  ],
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CardholderCreateParams params =
  CardholderCreateParams.builder()
    .setType(CardholderCreateParams.Type.INDIVIDUAL)
    .setName("Jenny Rosen")
    .setEmail("jenny.rosen@example.com")
    .setPhoneNumber("+18888675309")
    .setBilling(
      CardholderCreateParams.Billing.builder()
        .setAddress(
          CardholderCreateParams.Billing.Address.builder()
            .setLine1("1234 Main Street")
            .setCity("San Francisco")
            .setState("CA")
            .setCountry("US")
            .setPostalCode("94111")
            .build()
        )
        .build()
    )
    .build();

Cardholder cardholder = client.v1().issuing().cardholders().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const cardholder = await stripe.issuing.cardholders.create({
  type: 'individual',
  name: 'Jenny Rosen',
  email: 'jenny.rosen@example.com',
  phone_number: '+18888675309',
  billing: {
    address: {
      line1: '1234 Main Street',
      city: 'San Francisco',
      state: 'CA',
      country: 'US',
      postal_code: '94111',
    },
  },
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.IssuingCardholderCreateParams{
  Type: stripe.String(stripe.IssuingCardholderTypeIndividual),
  Name: stripe.String("Jenny Rosen"),
  Email: stripe.String("jenny.rosen@example.com"),
  PhoneNumber: stripe.String("+18888675309"),
  Billing: &stripe.IssuingCardholderCreateBillingParams{
    Address: &stripe.AddressParams{
      Line1: stripe.String("1234 Main Street"),
      City: stripe.String("San Francisco"),
      State: stripe.String("CA"),
      Country: stripe.String("US"),
      PostalCode: stripe.String("94111"),
    },
  },
}
result, err := sc.V1IssuingCardholders.Create(context.TODO(), params)
```

```dotnet
var options = new Stripe.Issuing.CardholderCreateOptions
{
    Type = "individual",
    Name = "Jenny Rosen",
    Email = "jenny.rosen@example.com",
    PhoneNumber = "+18888675309",
    Billing = new Stripe.Issuing.CardholderBillingOptions
    {
        Address = new AddressOptions
        {
            Line1 = "1234 Main Street",
            City = "San Francisco",
            State = "CA",
            Country = "US",
            PostalCode = "94111",
        },
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Issuing.Cardholders;
Stripe.Issuing.Cardholder cardholder = service.Create(options);
```

### Response

```json
{
  "id": "ich_1MsKAB2eZvKYlo2C3eZ2BdvK",
  "object": "issuing.cardholder",
  "billing": {
    "address": {
      "line1": "1234 Main Street",
      "city": "San Francisco",
      "state": "CA",
      "country": "US",
      "postal_code": "94111"
    }
  },
  "company": null,
  "created": 1680415995,
  "email": "jenny.rosen@example.com",
  "individual": null,
  "livemode": false,
  "metadata": {},
  "name": "Jenny Rosen",
  "phone_number": "+18888675309",
  "redaction": null,
  "requirements": {
    "disabled_reason": "requirements.past_due",
    "past_due": [
      "individual.card_issuing.user_terms_acceptance.ip",
      "individual.card_issuing.user_terms_acceptance.date",
      "individual.first_name",
      "individual.last_name"
    ]
  },
  "spending_controls": {
    "allowed_categories": [],
    "blocked_categories": [],
    "spending_limits": [],
    "spending_limits_currency": null
  },
  "status": "active",
  "type": "individual"
}
```