# List all cardholders

Returns a list of Issuing `Cardholder` objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` cardholders, starting after cardholder `starting_after`. Each entry in the array is a separate Issuing `Cardholder` object. If no more cardholders are available, the resulting array will be empty.

## Parameters

- `created` (object, optional)
  Only return cardholders that were created during the given date interval.

  - `created.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `created.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `created.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `created.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `email` (string, optional)
  Only return cardholders that have the given email address.

  The maximum length is 800 characters.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `phone_number` (string, optional)
  Only return cardholders that have the given phone number.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `status` (enum, optional)
  Only return cardholders that have the given status. One of `active`, `inactive`, or `blocked`.
Possible enum values:
  - `active`
    A platform has enabled the cardholder to approve authorizations made with their attached cards. However, if Stripe hasn’t yet verified the cardholder’s identity information, authorizations might still be blocked.

  - `blocked`
    Cards attached to this cardholder will decline all authorizations with the `cardholder_blocked` reason. This status is non-reversible.

  - `inactive`
    Cards attached to this cardholder will decline all authorizations with the `cardholder_inactive` reason.

- `type` (enum, optional)
  Only return cardholders that have the given type. One of `individual` or `company`.
Possible enum values:
  - `company`
    The cardholder is a company or business entity, and additional information includes their tax ID. This option may not be available if your [use case](https://docs.stripe.com/docs/issuing/other/choose-cardholder.md#find-your-use-case) only supports individual cardholders.

  - `individual`
    The cardholder is a person, and additional information includes first and last name, date of birth, etc. If you’re issuing Celtic Spend Cards, then Individual cardholders must accept Authorized User Terms prior to activating their card.

```curl
curl -G https://api.stripe.com/v1/issuing/cardholders \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe issuing cardholders list  \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

cardholders = client.v1.issuing.cardholders.list({limit: 3})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

cardholders = client.v1.issuing.cardholders.list({"limit": 3})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$cardholders = $stripe->issuing->cardholders->all(['limit' => 3]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CardholderListParams params = CardholderListParams.builder().setLimit(3L).build();

StripeCollection<Cardholder> stripeCollection =
  client.v1().issuing().cardholders().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const cardholders = await stripe.issuing.cardholders.list({
  limit: 3,
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.IssuingCardholderListParams{}
params.Limit = stripe.Int64(3)
result := sc.V1IssuingCardholders.List(context.TODO(), params)
```

```dotnet
var options = new Stripe.Issuing.CardholderListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Issuing.Cardholders;
StripeList<Stripe.Issuing.Cardholder> cardholders = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/issuing/cardholders",
  "has_more": false,
  "data": [
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
  ]
}
```