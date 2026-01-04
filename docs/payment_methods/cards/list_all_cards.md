# List all cards

You can see a list of the cards belonging to a customer. Note that the 10 most recent sources are always available on the `Customer` object. If you need more than those 10, you can use this API method and the `limit` and `starting_after` parameters to page through additional cards.

## Returns

Returns a list of the cards stored on the customer.

## Parameters

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/customers/cus_NhD8HD2bY8dP3V/cards \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

### Response

```json
{
  "object": "list",
  "url": "/v1/customers/cus_NhD8HD2bY8dP3V/cards",
  "has_more": false,
  "data": [
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
  ]
}
```