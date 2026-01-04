# Update an authorization

Updates the specified Issuing `Authorization` object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

## Returns

Returns an updated Issuing `Authorization` object if a valid identifier was provided.

## Parameters

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/issuing/authorizations/iauth_1JVXl82eZvKYlo2CPIiWlzrn \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
```

```cli
stripe issuing authorizations update iauth_1JVXl82eZvKYlo2CPIiWlzrn \
  -d "metadata[order_id]"=6735
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

authorization = client.v1.issuing.authorizations.update(
  'iauth_1JVXl82eZvKYlo2CPIiWlzrn',
  {metadata: {order_id: '6735'}},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

authorization = client.v1.issuing.authorizations.update(
  "iauth_1JVXl82eZvKYlo2CPIiWlzrn",
  {"metadata": {"order_id": "6735"}},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$authorization = $stripe->issuing->authorizations->update(
  'iauth_1JVXl82eZvKYlo2CPIiWlzrn',
  ['metadata' => ['order_id' => '6735']]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AuthorizationUpdateParams params =
  AuthorizationUpdateParams.builder().putMetadata("order_id", "6735").build();

Authorization authorization =
  client.v1().issuing().authorizations().update(
    "iauth_1JVXl82eZvKYlo2CPIiWlzrn",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const authorization = await stripe.issuing.authorizations.update(
  'iauth_1JVXl82eZvKYlo2CPIiWlzrn',
  {
    metadata: {
      order_id: '6735',
    },
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.IssuingAuthorizationUpdateParams{}
params.AddMetadata("order_id", "6735")
result, err := sc.V1IssuingAuthorizations.Update(
  context.TODO(), "iauth_1JVXl82eZvKYlo2CPIiWlzrn", params)
```

```dotnet
var options = new Stripe.Issuing.AuthorizationUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Issuing.Authorizations;
Stripe.Issuing.Authorization authorization = service.Update(
    "iauth_1JVXl82eZvKYlo2CPIiWlzrn",
    options);
```

### Response

```json
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
```