# List all funding instructions

Retrieve all applicable funding instructions for an Issuing balance.

## Returns

Returns all funding instructions for an Issuing balance

## Parameters

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/issuing/funding_instructions \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

### Response

```json
{
  "object": "list",
  "url": "/v1/issuing/funding_instructions",
  "has_more": false,
  "data": [
    {
      "object": "funding_instructions",
      "bank_transfer": {
        "country": "DE",
        "financial_addresses": [
          {
            "iban": {
              "account_holder_name": "Stripe Technology Europe Limited",
              "bic": "SXPYDEHH",
              "country": "DE",
              "iban": "DE00000000000000000001"
            },
            "supported_networks": [
              "sepa"
            ],
            "type": "iban"
          }
        ],
        "type": "eu_bank_transfer"
      },
      "currency": "eur",
      "funding_type": "bank_transfer",
      "livemode": false
    }
  ]
}
```