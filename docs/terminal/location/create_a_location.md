# Create a Location

Creates a new `Location` object. For further details, including which address fields are required in each country, see the [Manage locations](https://docs.stripe.com/docs/terminal/fleet/locations.md) guide.

## Returns

Returns a `Location` object if creation succeeds.

## Parameters

- `address` (object, optional)
  The full address of the location.

  - `address.country` (string, required)
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

  - `address.city` (string, required in certain countries)
    City, district, suburb, town, or village.

  - `address.line1` (string, required)
    Address line 1, such as the street, PO Box, or company name.

  - `address.line2` (string, optional)
    Address line 2, such as the apartment, suite, unit, or building.

  - `address.postal_code` (string, required in certain countries)
    ZIP or postal code.

  - `address.state` (string, required in certain countries)
    State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

- `display_name` (string, optional)
  A name for the location. Maximum length is 1000 characters.

- `address_kana` (object, optional)
  The Kana variation of the full address of the location (Japan only).

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
  The Kanji variation of the full address of the location (Japan only).

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

- `configuration_overrides` (string, optional)
  The ID of a configuration that will be used to customize all readers in this location.

  The maximum length is 500 characters.

- `display_name_kana` (string, optional)
  The Kana variation of the name for the location (Japan only). Maximum length is 1000 characters.

- `display_name_kanji` (string, optional)
  The Kanji variation of the name for the location (Japan only). Maximum length is 1000 characters.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `phone` (string, optional)
  The phone number for the location.

```curl
curl https://api.stripe.com/v1/terminal/locations \
  -u "<<YOUR_SECRET_KEY>>" \
  -d display_name="My First Store" \
  -d "address[line1]"="1234 Main Street" \
  -d "address[city]"="San Francisco" \
  -d "address[postal_code]"=94111 \
  -d "address[state]"=CA \
  -d "address[country]"=US
```

```cli
stripe terminal locations create  \
  --display-name="My First Store" \
  -d "address[line1]"="1234 Main Street" \
  -d "address[city]"="San Francisco" \
  -d "address[postal_code]"=94111 \
  -d "address[state]"=CA \
  -d "address[country]"=US
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

location = client.v1.terminal.locations.create({
  display_name: 'My First Store',
  address: {
    line1: '1234 Main Street',
    city: 'San Francisco',
    postal_code: '94111',
    state: 'CA',
    country: 'US',
  },
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

location = client.v1.terminal.locations.create({
  "display_name": "My First Store",
  "address": {
    "line1": "1234 Main Street",
    "city": "San Francisco",
    "postal_code": "94111",
    "state": "CA",
    "country": "US",
  },
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$location = $stripe->terminal->locations->create([
  'display_name' => 'My First Store',
  'address' => [
    'line1' => '1234 Main Street',
    'city' => 'San Francisco',
    'postal_code' => '94111',
    'state' => 'CA',
    'country' => 'US',
  ],
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

LocationCreateParams params =
  LocationCreateParams.builder()
    .setDisplayName("My First Store")
    .setAddress(
      LocationCreateParams.Address.builder()
        .setLine1("1234 Main Street")
        .setCity("San Francisco")
        .setPostalCode("94111")
        .setState("CA")
        .setCountry("US")
        .build()
    )
    .build();

Location location = client.v1().terminal().locations().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const location = await stripe.terminal.locations.create({
  display_name: 'My First Store',
  address: {
    line1: '1234 Main Street',
    city: 'San Francisco',
    postal_code: '94111',
    state: 'CA',
    country: 'US',
  },
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TerminalLocationCreateParams{
  DisplayName: stripe.String("My First Store"),
  Address: &stripe.AddressParams{
    Line1: stripe.String("1234 Main Street"),
    City: stripe.String("San Francisco"),
    PostalCode: stripe.String("94111"),
    State: stripe.String("CA"),
    Country: stripe.String("US"),
  },
}
result, err := sc.V1TerminalLocations.Create(context.TODO(), params)
```

```dotnet
var options = new Stripe.Terminal.LocationCreateOptions
{
    DisplayName = "My First Store",
    Address = new AddressOptions
    {
        Line1 = "1234 Main Street",
        City = "San Francisco",
        PostalCode = "94111",
        State = "CA",
        Country = "US",
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Terminal.Locations;
Stripe.Terminal.Location location = service.Create(options);
```

### Response

```json
{
  "id": "tml_FBakXQG8bQk4Mm",
  "object": "terminal.location",
  "address": {
    "city": "San Francisco",
    "country": "US",
    "line1": "1234 Main Street",
    "line2": "",
    "postal_code": "94111",
    "state": "CA"
  },
  "display_name": "My First Store",
  "livemode": false,
  "metadata": {}
}
```