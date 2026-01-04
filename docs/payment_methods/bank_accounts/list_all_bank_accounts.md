# List all bank accounts

You can see a list of the bank accounts belonging to a Customer. Note that the 10 most recent sources are always available by default on the Customer. If you need more than those 10, you can use this API method and the `limit` and `starting_after` parameters to page through additional bank accounts.

## Returns

Returns a list of the bank accounts stored on the customer.

## Parameters

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/customers/cus_9s6XI9OFIdpjIg/bank_accounts \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

### Response

```json
{
  "object": "list",
  "url": "/v1/customers/cus_9s6XI9OFIdpjIg/bank_accounts",
  "has_more": false,
  "data": [
    {
      "id": "ba_1MvoIJ2eZvKYlo2CO9f0MabO",
      "object": "bank_account",
      "account_holder_name": "Jane Austen",
      "account_holder_type": "company",
      "account_type": null,
      "bank_name": "STRIPE TEST BANK",
      "country": "US",
      "currency": "usd",
      "customer": "cus_9s6XI9OFIdpjIg",
      "fingerprint": "1JWtPxqbdX5Gamtc",
      "last4": "6789",
      "metadata": {},
      "routing_number": "110000000",
      "status": "new"
    }
  ]
}
```