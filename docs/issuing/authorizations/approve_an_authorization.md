# Approve an authorization

[Deprecated] Approves a pending Issuing `Authorization` object. This request should be made within the timeout window of the [real-time authorization](https://docs.stripe.com/docs/issuing/controls/real-time-authorizations.md) flow. This method is deprecated. Instead, [respond directly to the webhook request to approve an authorization](https://docs.stripe.com/docs/issuing/controls/real-time-authorizations.md#authorization-handling).

## Returns

Returns an approved Issuing `Authorization` object.

## Parameters

- `amount` (integer, optional)
  If the authorization’s `pending_request.is_amount_controllable` property is `true`, you may provide this value to control how much to hold for the authorization. Must be positive (use [`decline`](https://docs.stripe.com/docs/api/issuing/authorizations/decline.md) to decline an authorization request).

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl -X POST https://api.stripe.com/v1/issuing/authorizations/iauth_1MvSKeLkdIwHu7ixKr8rO1HV/approve \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe issuing authorizations approve iauth_1MvSKeLkdIwHu7ixKr8rO1HV
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

authorization = client.v1.issuing.authorizations.approve('iauth_1MvSKeLkdIwHu7ixKr8rO1HV')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

authorization = client.v1.issuing.authorizations.approve(
  "iauth_1MvSKeLkdIwHu7ixKr8rO1HV",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$authorization = $stripe->issuing->authorizations->approve(
  'iauth_1MvSKeLkdIwHu7ixKr8rO1HV',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AuthorizationApproveParams params = AuthorizationApproveParams.builder().build();

Authorization authorization =
  client.v1().issuing().authorizations().approve(
    "iauth_1MvSKeLkdIwHu7ixKr8rO1HV",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const authorization = await stripe.issuing.authorizations.approve(
  'iauth_1MvSKeLkdIwHu7ixKr8rO1HV'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.IssuingAuthorizationApproveParams{}
result, err := sc.V1IssuingAuthorizations.Approve(
  context.TODO(), "iauth_1MvSKeLkdIwHu7ixKr8rO1HV", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Issuing.Authorizations;
Stripe.Issuing.Authorization authorization = service.Approve(
    "iauth_1MvSKeLkdIwHu7ixKr8rO1HV");
```

### Response

```json
{
  "id": "iauth_1MvSKeLkdIwHu7ixKr8rO1HV",
  "object": "issuing.authorization",
  "amount": 0,
  "amount_details": {
    "atm_fee": null
  },
  "approved": true,
  "authorization_method": "keyed_in",
  "balance_transactions": [],
  "card": {
    "id": "ic_1MvSKeLkdIwHu7ixFANTvxgn",
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
    "created": 1681162380,
    "currency": "usd",
    "exp_month": 8,
    "exp_year": 2024,
    "last4": "4242",
    "livemode": false,
    "metadata": {},
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
  },
  "cardholder": null,
  "created": 1681162380,
  "currency": "usd",
  "livemode": false,
  "merchant_amount": 0,
  "merchant_currency": "usd",
  "merchant_data": {
    "category": "taxicabs_limousines",
    "category_code": "4121",
    "city": "San Francisco",
    "country": "US",
    "name": "Rocket Rides",
    "network_id": "1234567890",
    "postal_code": "94107",
    "state": "CA"
  },
  "metadata": {},
  "network_data": null,
  "pending_request": {
    "amount": 700,
    "amount_details": {
      "atm_fee": null
    },
    "currency": "usd",
    "is_amount_controllable": false,
    "merchant_amount": 700,
    "merchant_currency": "usd"
  },
  "request_history": [],
  "status": "pending",
  "transactions": [],
  "verification_data": {
    "address_line1_check": "not_provided",
    "address_postal_code_check": "match",
    "cvc_check": "match",
    "expiry_check": "match"
  },
  "wallet": null
}
```