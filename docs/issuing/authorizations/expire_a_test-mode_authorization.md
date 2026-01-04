# Expire a test-mode authorization

Expire a test-mode Authorization.

## Returns

An Authorization object

```curl
curl -X POST https://api.stripe.com/v1/test_helpers/issuing/authorizations/iauth_1DPc772eZvKYlo2C6avLyZ25/expire \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe test_helpers issuing authorizations expire iauth_1DPc772eZvKYlo2C6avLyZ25
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

authorization = client.v1.test_helpers.issuing.authorizations.expire('iauth_1DPc772eZvKYlo2C6avLyZ25')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

authorization = client.v1.test_helpers.issuing.authorizations.expire(
  "iauth_1DPc772eZvKYlo2C6avLyZ25",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$authorization = $stripe->testHelpers->issuing->authorizations->expire(
  'iauth_1DPc772eZvKYlo2C6avLyZ25',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AuthorizationExpireParams params = AuthorizationExpireParams.builder().build();

Authorization authorization =
  client.v1().testHelpers().issuing().authorizations().expire(
    "iauth_1DPc772eZvKYlo2C6avLyZ25",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const authorization = await stripe.testHelpers.issuing.authorizations.expire(
  'iauth_1DPc772eZvKYlo2C6avLyZ25'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TestHelpersIssuingAuthorizationExpireParams{}
result, err := sc.V1TestHelpersIssuingAuthorizations.Expire(
  context.TODO(), "iauth_1DPc772eZvKYlo2C6avLyZ25", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.TestHelpers.Issuing.Authorizations;
Stripe.Issuing.Authorization authorization = service.Expire(
    "iauth_1DPc772eZvKYlo2C6avLyZ25");
```

### Response

```json
{
  "id": "iauth_1DPc772eZvKYlo2C6avLyZ25",
  "object": "issuing.authorization",
  "amount": 0,
  "amount_details": {
    "atm_fee": null,
    "cashback_amount": null
  },
  "approved": true,
  "authorization_method": "keyed_in",
  "balance_transactions": [],
  "card": {
    "id": "ic_1FEiQC2eZvKYlo2CtahKepKy",
    "object": "issuing.card",
    "brand": "Visa",
    "cancellation_reason": null,
    "cardholder": {
      "id": "ich_1Ccy6F2eZvKYlo2ClnIm9bs4",
      "object": "issuing.cardholder",
      "billing": {
        "address": {
          "city": "Beverly Hills",
          "country": "US",
          "line1": "123 Fake St",
          "line2": "Apt 3",
          "postal_code": "90210",
          "state": "CA"
        }
      },
      "company": null,
      "created": 1528992903,
      "email": "jenny@example.com",
      "individual": null,
      "livemode": false,
      "metadata": {},
      "name": "Jenny Rosen",
      "phone_number": "+18008675309",
      "preferred_locales": [],
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
    "created": 1567541772,
    "currency": "usd",
    "exp_month": 12,
    "exp_year": 2020,
    "last4": "4242",
    "livemode": false,
    "metadata": {
      "status": "canceled"
    },
    "redaction": null,
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
    "status": "canceled",
    "type": "physical",
    "wallets": {
      "apple_pay": {
        "eligible": true,
        "ineligible_reason": null
      },
      "google_pay": {
        "eligible": false,
        "ineligible_reason": "missing_agreement"
      },
      "primary_account_identifier": null
    }
  },
  "cardholder": "ich_1Ccy6F2eZvKYlo2ClnIm9bs4",
  "created": 1540586461,
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
    "state": "CA",
    "terminal_id": null
  },
  "metadata": {},
  "network_data": null,
  "pending_request": null,
  "redaction": null,
  "request_history": [],
  "status": "reversed",
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