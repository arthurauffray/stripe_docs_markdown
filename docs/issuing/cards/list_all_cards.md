# List all cards

Returns a list of Issuing `Card` objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` cards, starting after card `starting_after`. Each entry in the array is a separate Issuing `Card` object. If no more cards are available, the resulting array will be empty.

## Parameters

- `cardholder` (string, optional)
  Only return cards belonging to the Cardholder with the provided ID.

- `created` (object, optional)
  Only return cards that were issued during the given date interval.

  - `created.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `created.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `created.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `created.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `exp_month` (integer, optional)
  Only return cards that have the given expiration month.

- `exp_year` (integer, optional)
  Only return cards that have the given expiration year.

- `last4` (string, optional)
  Only return cards that have the given last four digits.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `status` (enum, optional)
  Only return cards that have the given status. One of `active`, `inactive`, or `canceled`.
Possible enum values:
  - `active`
    The card can approve authorizations. If the card is linked to a cardholder with past-due requirements, you may be unable to change the card’s status to ‘active’.

  - `canceled`
    The card will decline authorizations with the `card_canceled` reason. This status is permanent.

  - `inactive`
    The card will decline authorizations with the `card_inactive` reason.

- `type` (enum, optional)
  Only return cards that have the given type. One of `virtual` or `physical`.
Possible enum values:
  - `physical`
    A physical card will be printed and shipped. It can be used at physical terminals.

  - `virtual`
    No physical card will be printed. The card can be used online and can be [added to digital wallets](https://stripe.com/docs/issuing/cards/digital-wallets).

```curl
curl -G https://api.stripe.com/v1/issuing/cards \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe issuing cards list  \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

cards = client.v1.issuing.cards.list({limit: 3})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

cards = client.v1.issuing.cards.list({"limit": 3})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$cards = $stripe->issuing->cards->all(['limit' => 3]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CardListParams params = CardListParams.builder().setLimit(3L).build();

StripeCollection<Card> stripeCollection = client.v1().issuing().cards().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const cards = await stripe.issuing.cards.list({
  limit: 3,
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.IssuingCardListParams{}
params.Limit = stripe.Int64(3)
result := sc.V1IssuingCards.List(context.TODO(), params)
```

```dotnet
var options = new Stripe.Issuing.CardListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Issuing.Cards;
StripeList<Stripe.Issuing.Card> cards = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/issuing/cards",
  "has_more": false,
  "data": [
    {
      "id": "ic_1MvSieLkdIwHu7ixn6uuO0Xu",
      "object": "issuing.card",
      "brand": "Visa",
      "cancellation_reason": null,
      "cardholder": {
        "id": "ich_1MsKAB2eZvKYlo2C3eZ2BdvK",
        "object": "issuing.cardholder",
        "billing": {
          "address": {
            "city": "Anytown",
            "country": "US",
            "line1": "123 Main Street",
            "line2": null,
            "postal_code": "12345",
            "state": "CA"
          }
        },
        "company": null,
        "created": 1680415995,
        "email": null,
        "individual": null,
        "livemode": false,
        "metadata": {},
        "name": "John Doe",
        "phone_number": null,
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
      },
      "created": 1681163868,
      "currency": "usd",
      "exp_month": 8,
      "exp_year": 2024,
      "last4": "4242",
      "livemode": false,
      "metadata": {},
      "replaced_by": null,
      "replacement_for": null,
      "replacement_reason": null,
      "shipping": null,
      "spending_controls": {
        "allowed_categories": null,
        "blocked_categories": null,
        "spending_limits": [],
        "spending_limits_currency": null
      },
      "status": "active",
      "type": "virtual",
      "wallets": {
        "apple_pay": {
          "eligible": false,
          "ineligible_reason": "missing_cardholder_contact"
        },
        "google_pay": {
          "eligible": false,
          "ineligible_reason": "missing_cardholder_contact"
        },
        "primary_account_identifier": null
      }
    }
  ]
}
```