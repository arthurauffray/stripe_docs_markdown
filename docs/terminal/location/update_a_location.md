# Update a Location

Updates a `Location` object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

## Returns

Returns an updated `Location` object if a valid identifier was provided.

## Parameters

- `address` (object, optional)
  The full address of the location. You can’t change the location’s `country`. If you need to modify the `country` field, create a new `Location` object and re-register any existing readers to that location.

  - `address.city` (string, optional)
    City, district, suburb, town, or village.

  - `address.country` (string, required for calculating taxes)
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

  - `address.line1` (string, optional)
    Address line 1, such as the street, PO Box, or company name.

  - `address.line2` (string, optional)
    Address line 2, such as the apartment, suite, unit, or building.

  - `address.postal_code` (string, required for calculating taxes)
    ZIP or postal code.

  - `address.state` (string, optional)
    State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

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

- `display_name` (string, optional)
  A name for the location.

- `display_name_kana` (string, optional)
  The Kana variation of the name for the location (Japan only).

- `display_name_kanji` (string, optional)
  The Kanji variation of the name for the location (Japan only).

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `phone` (string, optional)
  The phone number for the location.

```curl
curl https://api.stripe.com/v1/terminal/locations/tml_FBakXQG8bQk4Mm \
  -u "<<YOUR_SECRET_KEY>>" \
  -d display_name="Update Store Name"
```

```cli
stripe terminal locations update tml_FBakXQG8bQk4Mm \
  --display-name="Update Store Name"
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

location = client.v1.terminal.locations.update(
  'tml_FBakXQG8bQk4Mm',
  {display_name: 'Update Store Name'},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

location = client.v1.terminal.locations.update(
  "tml_FBakXQG8bQk4Mm",
  {"display_name": "Update Store Name"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$location = $stripe->terminal->locations->update(
  'tml_FBakXQG8bQk4Mm',
  ['display_name' => 'Update Store Name']
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

LocationUpdateParams params =
  LocationUpdateParams.builder().setDisplayName("Update Store Name").build();

Location location =
  client.v1().terminal().locations().update("tml_FBakXQG8bQk4Mm", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const location = await stripe.terminal.locations.update(
  'tml_FBakXQG8bQk4Mm',
  {
    display_name: 'Update Store Name',
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TerminalLocationUpdateParams{
  DisplayName: stripe.String("Update Store Name"),
}
result, err := sc.V1TerminalLocations.Update(
  context.TODO(), "tml_FBakXQG8bQk4Mm", params)
```

```dotnet
var options = new Stripe.Terminal.LocationUpdateOptions
{
    DisplayName = "Update Store Name",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Terminal.Locations;
Stripe.Terminal.Location location = service.Update("tml_FBakXQG8bQk4Mm", options);
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
  "display_name": "Update Store Name",
  "livemode": false,
  "metadata": {}
}
```