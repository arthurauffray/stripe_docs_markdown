# List all personalization designs

Returns a list of personalization design objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` cards, starting after card `starting_after`. Each entry in the array is a separate personalization design object. If no more cards are available, the resulting array will be empty.

## Parameters

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `lookup_keys` (array of strings, optional)
  Only return personalization designs with the given lookup keys.

- `preferences` (object, optional)
  Only return personalization designs with the given preferences.

  - `preferences.is_default` (boolean, optional)
    Only return the personalization design that’s set as the default. A connected account uses the Connect platform’s default design if no personalization design is set as the default.

  - `preferences.is_platform_default` (boolean, optional)
    Only return the personalization design that is set as the Connect platform’s default. This parameter is only applicable to connected accounts.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `status` (enum, optional)
  Only return personalization designs with the given status.
Possible enum values:
  - `active`
    Personalization design can be used to create cards that fulfill immediately.

  - `inactive`
    Personalization design cannot be used to create cards because it was deactivated.

  - `rejected`
    Personalization design cannot be used to create cards because it was rejected by design review.

  - `review`
    Personalization design can be used to create cards but cards will only be fulfilled once the personalization design is activated.

```curl
curl -G https://api.stripe.com/v1/issuing/personalization_designs \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe issuing personalization_designs list  \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

personalization_designs = client.v1.issuing.personalization_designs.list({limit: 3})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

personalization_designs = client.v1.issuing.personalization_designs.list({
  "limit": 3,
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$personalizationDesigns = $stripe->issuing->personalizationDesigns->all([
  'limit' => 3,
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PersonalizationDesignListParams params =
  PersonalizationDesignListParams.builder().setLimit(3L).build();

StripeCollection<PersonalizationDesign> stripeCollection =
  client.v1().issuing().personalizationDesigns().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const personalizationDesigns = await stripe.issuing.personalizationDesigns.list({
  limit: 3,
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.IssuingPersonalizationDesignListParams{}
params.Limit = stripe.Int64(3)
result := sc.V1IssuingPersonalizationDesigns.List(context.TODO(), params)
```

```dotnet
var options = new Stripe.Issuing.PersonalizationDesignListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Issuing.PersonalizationDesigns;
StripeList<Stripe.Issuing.PersonalizationDesign> personalizationDesigns = service
    .List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/issuing/personalization_designs",
  "has_more": false,
  "data": [
    {
      "id": "ipcd_Oiw9GXcFRE81LZ",
      "object": "issuing.personalization_design",
      "livemode": true,
      "card_logo": "file_1LzR9L2eZvKYlo2CelTpcvKu",
      "carrier_text": null,
      "lookup_key": "my_card_design_lookup_key",
      "metadata": {},
      "name": "My personalization design name",
      "physical_bundle": "ics_Oiw9ahglMfql0U",
      "preferences": {
        "is_default": false
      },
      "rejection_reasons": {
        "card_logo": [],
        "carrier_text": []
      },
      "status": "review"
    }
  ]
}
```