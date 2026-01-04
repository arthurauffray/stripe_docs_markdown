# List all authorizations

Returns a list of Issuing `Authorization` objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` authorizations, starting after authorization `starting_after`. Each entry in the array is a separate Issuing `Authorization` object. If no more authorizations are available, the resulting array will be empty.

## Parameters

- `card` (string, optional)
  Only return authorizations that belong to the given card.

- `cardholder` (string, optional)
  Only return authorizations that belong to the given cardholder.

- `created` (object, optional)
  Only return authorizations that were created during the given date interval.

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

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `status` (enum, optional)
  Only return authorizations with the given status. One of `pending`, `closed`, or `reversed`.
Possible enum values:
  - `closed`
    The authorization was declined or [captured](https://docs.stripe.com/docs/issuing/purchases/transactions.md) through one or more [transactions](https://docs.stripe.com/docs/api/issuing/authorizations/object.md#issuing_authorization_object-transactions).

  - `expired`
    The authorization was expired without capture.

  - `pending`
    The authorization was created and is awaiting approval or was approved and is awaiting [capture](https://docs.stripe.com/docs/issuing/purchases/transactions.md).

  - `reversed`
    The authorization was reversed by the merchant.

```curl
curl -G https://api.stripe.com/v1/issuing/authorizations \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe issuing authorizations list  \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

authorizations = client.v1.issuing.authorizations.list({limit: 3})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

authorizations = client.v1.issuing.authorizations.list({"limit": 3})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$authorizations = $stripe->issuing->authorizations->all(['limit' => 3]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AuthorizationListParams params =
  AuthorizationListParams.builder().setLimit(3L).build();

StripeCollection<Authorization> stripeCollection =
  client.v1().issuing().authorizations().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const authorizations = await stripe.issuing.authorizations.list({
  limit: 3,
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.IssuingAuthorizationListParams{}
params.Limit = stripe.Int64(3)
result := sc.V1IssuingAuthorizations.List(context.TODO(), params)
```

```dotnet
var options = new Stripe.Issuing.AuthorizationListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Issuing.Authorizations;
StripeList<Stripe.Issuing.Authorization> authorizations = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/issuing/authorizations",
  "has_more": false,
  "data": [
    {
      "id": "iauth_1JVXl82eZvKYlo2CPIiWlzrn",
      "object": "issuing.authorization",
      "amount": 382,
      "amount_details": {
        "atm_fee": null
      },
      "approved": false,
      "authorization_method": "online",
      "balance_transactions": [],
      "card": {
        "id": "ic_1JDmgz2eZvKYlo2CRXlTsXj6",
        "object": "issuing.card",
        "brand": "Visa",
        "cancellation_reason": null,
        "cardholder": {
          "id": "ich_1JDmfb2eZvKYlo2CwHUgaAxU",
          "object": "issuing.cardholder",
          "billing": {
            "address": {
              "city": "San Francisco",
              "country": "US",
              "line1": "123 Main Street",
              "line2": null,
              "postal_code": "94111",
              "state": "CA"
            }
          },
          "company": null,
          "created": 1626425119,
          "email": "jenny.rosen@example.com",
          "individual": null,
          "livemode": false,
          "metadata": {},
          "name": "Jenny Rosen",
          "phone_number": "+18008675309",
          "redaction": null,
          "requirements": {
            "disabled_reason": null,
            "past_due": []
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
        "created": 1626425206,
        "currency": "usd",
        "exp_month": 6,
        "exp_year": 2024,
        "last4": "8693",
        "livemode": false,
        "metadata": {},
        "redaction": null,
        "replaced_by": null,
        "replacement_for": null,
        "replacement_reason": null,
        "shipping": null,
        "spending_controls": {
          "allowed_categories": null,
          "blocked_categories": null,
          "spending_limits": [
            {
              "amount": 50000,
              "categories": [],
              "interval": "daily"
            }
          ],
          "spending_limits_currency": "usd"
        },
        "status": "active",
        "type": "virtual",
        "wallets": {
          "apple_pay": {
            "eligible": true,
            "ineligible_reason": null
          },
          "google_pay": {
            "eligible": true,
            "ineligible_reason": null
          },
          "primary_account_identifier": null
        }
      },
      "cardholder": "ich_1JDmfb2eZvKYlo2CwHUgaAxU",
      "created": 1630657706,
      "currency": "usd",
      "livemode": false,
      "merchant_amount": 382,
      "merchant_currency": "usd",
      "merchant_data": {
        "category": "computer_software_stores",
        "category_code": "5734",
        "city": "SAN FRANCISCO",
        "country": "US",
        "name": "STRIPE",
        "network_id": "1234567890",
        "postal_code": "94103",
        "state": "CA"
      },
      "metadata": {
        "order_id": "6735"
      },
      "network_data": null,
      "pending_request": null,
      "redaction": null,
      "request_history": [
        {
          "amount": 382,
          "amount_details": {
            "atm_fee": null
          },
          "approved": false,
          "created": 1630657706,
          "currency": "usd",
          "merchant_amount": 382,
          "merchant_currency": "usd",
          "reason": "verification_failed",
          "reason_message": null
        }
      ],
      "status": "closed",
      "transactions": [],
      "verification_data": {
        "address_line1_check": "not_provided",
        "address_postal_code_check": "not_provided",
        "cvc_check": "mismatch",
        "expiry_check": "match"
      },
      "wallet": null
    }
  ]
}
```