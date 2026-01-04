# Retrieve a card

Retrieves an Issuing `Card` object.

## Returns

Returns an Issuing `Card` object if a valid identifier was provided. When requesting the ID of a card that has been deleted, a subset of the card’s information will be returned, including a `deleted` property, which will be true.

```curl
curl https://api.stripe.com/v1/issuing/cards/ic_1MvSieLkdIwHu7ixn6uuO0Xu \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe issuing cards retrieve ic_1MvSieLkdIwHu7ixn6uuO0Xu
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

card = client.v1.issuing.cards.retrieve('ic_1MvSieLkdIwHu7ixn6uuO0Xu')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

card = client.v1.issuing.cards.retrieve("ic_1MvSieLkdIwHu7ixn6uuO0Xu")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$card = $stripe->issuing->cards->retrieve('ic_1MvSieLkdIwHu7ixn6uuO0Xu', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CardRetrieveParams params = CardRetrieveParams.builder().build();

Card card =
  client.v1().issuing().cards().retrieve("ic_1MvSieLkdIwHu7ixn6uuO0Xu", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const card = await stripe.issuing.cards.retrieve('ic_1MvSieLkdIwHu7ixn6uuO0Xu');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.IssuingCardRetrieveParams{}
result, err := sc.V1IssuingCards.Retrieve(
  context.TODO(), "ic_1MvSieLkdIwHu7ixn6uuO0Xu", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Issuing.Cards;
Stripe.Issuing.Card card = service.Get("ic_1MvSieLkdIwHu7ixn6uuO0Xu");
```

### Response

```json
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
```