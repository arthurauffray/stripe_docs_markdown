# Decline an authorization

[Deprecated] Declines a pending Issuing `Authorization` object. This request should be made within the timeout window of the [real time authorization](https://docs.stripe.com/docs/issuing/controls/real-time-authorizations.md) flow. This method is deprecated. Instead, [respond directly to the webhook request to decline an authorization](https://docs.stripe.com/docs/issuing/controls/real-time-authorizations.md#authorization-handling).

## Returns

Returns a declined Issuing `Authorization` object.

## Parameters

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl -X POST https://api.stripe.com/v1/issuing/authorizations/iauth_1JVXl82eZvKYlo2CPIiWlzrn/decline \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe issuing authorizations decline iauth_1JVXl82eZvKYlo2CPIiWlzrn
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

authorization = client.v1.issuing.authorizations.decline('iauth_1JVXl82eZvKYlo2CPIiWlzrn')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

authorization = client.v1.issuing.authorizations.decline(
  "iauth_1JVXl82eZvKYlo2CPIiWlzrn",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$authorization = $stripe->issuing->authorizations->decline(
  'iauth_1JVXl82eZvKYlo2CPIiWlzrn',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AuthorizationDeclineParams params = AuthorizationDeclineParams.builder().build();

Authorization authorization =
  client.v1().issuing().authorizations().decline(
    "iauth_1JVXl82eZvKYlo2CPIiWlzrn",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const authorization = await stripe.issuing.authorizations.decline(
  'iauth_1JVXl82eZvKYlo2CPIiWlzrn'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.IssuingAuthorizationDeclineParams{}
result, err := sc.V1IssuingAuthorizations.Decline(
  context.TODO(), "iauth_1JVXl82eZvKYlo2CPIiWlzrn", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Issuing.Authorizations;
Stripe.Issuing.Authorization authorization = service.Decline(
    "iauth_1JVXl82eZvKYlo2CPIiWlzrn");
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