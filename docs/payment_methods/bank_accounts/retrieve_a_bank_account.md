# Retrieve a bank account

By default, you can see the 10 most recent sources stored on a Customer directly on the object, but you can also retrieve details about a specific bank account stored on the Stripe account.

## Returns

Returns the bank account object.

```curl
curl https://api.stripe.com/v1/customers/cus_9s6XI9OFIdpjIg/bank_accounts/ba_1MvoIJ2eZvKYlo2CO9f0MabO \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
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
```