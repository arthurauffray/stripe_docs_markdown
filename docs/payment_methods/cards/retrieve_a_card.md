# Retrieve a card

You can always see the 10 most recent cards directly on a customer; this method lets you retrieve details about a specific card stored on the customer.

## Returns

Returns the `Card` object.

```curl
curl https://api.stripe.com/v1/customers/cus_NhD8HD2bY8dP3V/cards/card_1MvoiELkdIwHu7ixOeFGbN9D \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "card_1MvoiELkdIwHu7ixOeFGbN9D",
  "object": "card",
  "address_city": null,
  "address_country": null,
  "address_line1": null,
  "address_line1_check": null,
  "address_line2": null,
  "address_state": null,
  "address_zip": null,
  "address_zip_check": null,
  "brand": "Visa",
  "country": "US",
  "customer": "cus_NhD8HD2bY8dP3V",
  "cvc_check": null,
  "dynamic_last4": null,
  "exp_month": 4,
  "exp_year": 2024,
  "fingerprint": "mToisGZ01V71BCos",
  "funding": "credit",
  "last4": "4242",
  "metadata": {},
  "name": null,
  "tokenization_method": null,
  "wallet": null
}
```