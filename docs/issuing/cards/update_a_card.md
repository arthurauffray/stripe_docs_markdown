# Update a card

Updates the specified Issuing `Card` object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

## Returns

Returns an updated Issuing `Card` object if a valid identifier was provided.

## Parameters

- `cancellation_reason` (enum, optional)
  Reason why the `status` of this card is `canceled`.
Possible enum values:
  - `lost`
    The card was lost.

  - `stolen`
    The card was stolen.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `pin` (object, optional)
  The desired new PIN for this card.

  - `pin.encrypted_number` (string, optional)
    The card’s desired new PIN, encrypted under Stripe’s public key.

- `shipping` (object, optional)
  Updated shipping information for the card.

  - `shipping.address` (object, required)
    The address that the card is shipped to.

    - `shipping.address.city` (string, required)
      City, district, suburb, town, or village.

    - `shipping.address.country` (string, required)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `shipping.address.line1` (string, required)
      Address line 1, such as the street, PO Box, or company name.

    - `shipping.address.postal_code` (string, required)
      ZIP or postal code.

    - `shipping.address.line2` (string, optional)
      Address line 2, such as the apartment, suite, unit, or building.

    - `shipping.address.state` (string, optional)
      State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

  - `shipping.name` (string, required)
    The name printed on the shipping label when shipping the card.

  - `shipping.address_validation` (object, optional)
    Address validation settings.

    - `shipping.address_validation.mode` (enum, required)
      The address validation capabilities to use.
Possible enum values:
      - `disabled`
        The card will be shipped without validating or normalizing the shipping address.

      - `normalization_only`
        The card will be shipped with the normalized address without validation. Undeliverable addresses won’t be blocked.

      - `validation_and_normalization`
        The card will be shipped with the normalized, validated address. Undeliverable addresses will be blocked.

  - `shipping.customs` (object, optional)
    Customs information for the shipment.

    - `shipping.customs.eori_number` (string, optional)
      The Economic Operators Registration and Identification (EORI) number to use for Customs. Required for bulk shipments to Europe.

  - `shipping.phone_number` (string, optional)
    Phone number of the recipient of the shipment.

  - `shipping.require_signature` (boolean, optional)
    Whether a signature is required for card delivery.

  - `shipping.service` (enum, optional)
    Shipment service.
Possible enum values:
    - `express`
      Cards arrive in 4 business days.

    - `priority`
      Cards arrive in 2-3 business days.

    - `standard`
      Cards arrive in 5-8 business days.

  - `shipping.type` (enum, optional)
    Packaging options.
Possible enum values:
    - `bulk`
      Cards are grouped and mailed together.

    - `individual`
      Cards are sent individually in an envelope.

- `spending_controls` (object, optional)
  Rules that control spending for this card. Refer to our [documentation](https://docs.stripe.com/docs/issuing/controls/spending-controls.md) for more details.

  - `spending_controls.allowed_categories` (array of strings, optional)
    Array of strings containing [categories](https://docs.stripe.com/docs/api.md#issuing_authorization_object-merchant_data-category) of authorizations to allow. All other categories will be blocked. Cannot be set with `blocked_categories`.

  - `spending_controls.allowed_merchant_countries` (array of strings, optional)
    Array of strings containing representing countries from which authorizations will be allowed. Authorizations from merchants in all other countries will be declined. Country codes should be ISO 3166 alpha-2 country codes (e.g. `US`). Cannot be set with `blocked_merchant_countries`. Provide an empty value to unset this control.

  - `spending_controls.blocked_categories` (array of strings, optional)
    Array of strings containing [categories](https://docs.stripe.com/docs/api.md#issuing_authorization_object-merchant_data-category) of authorizations to decline. All other categories will be allowed. Cannot be set with `allowed_categories`.

  - `spending_controls.blocked_merchant_countries` (array of strings, optional)
    Array of strings containing representing countries from which authorizations will be declined. Country codes should be ISO 3166 alpha-2 country codes (e.g. `US`). Cannot be set with `allowed_merchant_countries`. Provide an empty value to unset this control.

  - `spending_controls.spending_limits` (array of objects, optional)
    Limit spending with amount-based rules that apply across any cards this card replaced (i.e., its `replacement_for` card and *that* card’s `replacement_for` card, up the chain).

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

- `status` (enum, optional)
  Dictates whether authorizations can be approved on this card. May be blocked from activating cards depending on past-due Cardholder requirements. Defaults to `inactive`. If this card is being canceled because it was lost or stolen, this information should be provided as `cancellation_reason`.
Possible enum values:
  - `active`
    The card can approve authorizations. If the card is linked to a cardholder with past-due requirements, you may be unable to change the card’s status to ‘active’.

  - `canceled`
    The card will decline authorizations with the `card_canceled` reason. This status is permanent.

  - `inactive`
    The card will decline authorizations with the `card_inactive` reason.

```curl
curl https://api.stripe.com/v1/issuing/cards/ic_1MvSieLkdIwHu7ixn6uuO0Xu \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
```

```cli
stripe issuing cards update ic_1MvSieLkdIwHu7ixn6uuO0Xu \
  -d "metadata[order_id]"=6735
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

card = client.v1.issuing.cards.update(
  'ic_1MvSieLkdIwHu7ixn6uuO0Xu',
  {metadata: {order_id: '6735'}},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

card = client.v1.issuing.cards.update(
  "ic_1MvSieLkdIwHu7ixn6uuO0Xu",
  {"metadata": {"order_id": "6735"}},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$card = $stripe->issuing->cards->update(
  'ic_1MvSieLkdIwHu7ixn6uuO0Xu',
  ['metadata' => ['order_id' => '6735']]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CardUpdateParams params =
  CardUpdateParams.builder().putMetadata("order_id", "6735").build();

Card card =
  client.v1().issuing().cards().update("ic_1MvSieLkdIwHu7ixn6uuO0Xu", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const card = await stripe.issuing.cards.update(
  'ic_1MvSieLkdIwHu7ixn6uuO0Xu',
  {
    metadata: {
      order_id: '6735',
    },
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.IssuingCardUpdateParams{}
params.AddMetadata("order_id", "6735")
result, err := sc.V1IssuingCards.Update(
  context.TODO(), "ic_1MvSieLkdIwHu7ixn6uuO0Xu", params)
```

```dotnet
var options = new Stripe.Issuing.CardUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Issuing.Cards;
Stripe.Issuing.Card card = service.Update("ic_1MvSieLkdIwHu7ixn6uuO0Xu", options);
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
  "metadata": {
    "order_id": "6735"
  },
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