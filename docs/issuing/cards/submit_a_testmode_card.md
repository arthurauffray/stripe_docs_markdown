# Submit a testmode card

Updates the shipping status of the specified Issuing `Card` object to `submitted`. This method requires Stripe Version ‘2024-09-30.acacia’ or later.

## Returns

Returns an updated Issuing `Card` object.

```curl
curl -X POST https://api.stripe.com/v1/test_helpers/issuing/cards/ic_1MvSieLkdIwHu7ixn6uuO0Xu/shipping/submit \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe test_helpers issuing cards submit_card ic_1MvSieLkdIwHu7ixn6uuO0Xu
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

card = client.v1.test_helpers.issuing.cards.submit_card('ic_1MvSieLkdIwHu7ixn6uuO0Xu')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

card = client.v1.test_helpers.issuing.cards.submit_card(
  "ic_1MvSieLkdIwHu7ixn6uuO0Xu",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$card = $stripe->testHelpers->issuing->cards->submitCard(
  'ic_1MvSieLkdIwHu7ixn6uuO0Xu',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CardSubmitCardParams params = CardSubmitCardParams.builder().build();

Card card =
  client.v1().testHelpers().issuing().cards().submitCard(
    "ic_1MvSieLkdIwHu7ixn6uuO0Xu",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const card = await stripe.testHelpers.issuing.cards.submitCard(
  'ic_1MvSieLkdIwHu7ixn6uuO0Xu'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TestHelpersIssuingCardSubmitCardParams{}
result, err := sc.V1TestHelpersIssuingCards.SubmitCard(
  context.TODO(), "ic_1MvSieLkdIwHu7ixn6uuO0Xu", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.TestHelpers.Issuing.Cards;
Stripe.Issuing.Card card = service.SubmitCard("ic_1MvSieLkdIwHu7ixn6uuO0Xu");
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
  "shipping": {
    "address": {
      "city": "San Francisco",
      "country": "US",
      "line1": "1234 Main Street",
      "postal_code": "94111",
      "state": "CA"
    },
    "carrier": "usps",
    "eta": 1655362799,
    "name": "Jenny Rosen",
    "service": "standard",
    "status": "submitted",
    "type": "individual"
  },
  "spending_controls": {
    "allowed_categories": null,
    "blocked_categories": null,
    "spending_limits": [],
    "spending_limits_currency": null
  },
  "status": "active",
  "type": "physical",
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