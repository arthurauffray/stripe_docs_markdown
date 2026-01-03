# Reject an account

With [Connect](https://docs.stripe.com/connect.md), you can reject accounts that you have flagged as suspicious.

Only accounts where your platform is liable for negative account balances, which includes Custom and Express accounts, can be rejected. Test-mode accounts can be rejected at any time. Live-mode accounts can only be rejected after all balances are zero.

## Returns

Returns an account with `payouts_enabled` and `charges_enabled` set to false on success. If the account ID does not exist, this call raises [an error](https://docs.stripe.com/api/account/reject.md#errors).

## Parameters

- `reason` (string, required)
  The reason for rejecting the account. Can be `fraud`, `terms_of_service`, or `other`.

```curl
curl https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/reject \
  -u "<<YOUR_SECRET_KEY>>" \
  -d reason=fraud
```

```cli
stripe accounts reject acct_1032D82eZvKYlo2C \
  --reason=fraud
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

account = client.v1.accounts.reject('acct_1032D82eZvKYlo2C', {reason: 'fraud'})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

account = client.v1.accounts.reject(
  "acct_1032D82eZvKYlo2C",
  {"reason": "fraud"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$account = $stripe->accounts->reject('acct_1032D82eZvKYlo2C', ['reason' => 'fraud']);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AccountRejectParams params =
  AccountRejectParams.builder().setReason("fraud").build();

Account account = client.v1().accounts().reject("acct_1032D82eZvKYlo2C", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const account = await stripe.accounts.reject(
  'acct_1032D82eZvKYlo2C',
  {
    reason: 'fraud',
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.AccountRejectParams{Reason: stripe.String("fraud")}
result, err := sc.V1Accounts.Reject(context.TODO(), "acct_1032D82eZvKYlo2C", params)
```

```dotnet
var options = new AccountRejectOptions { Reason = "fraud" };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Accounts;
Account account = service.Reject("acct_1032D82eZvKYlo2C", options);
```

### Response

```json
{
  "id": "acct_1Nv0FGQ9RKHgCVdK",
  "object": "account",
  "business_profile": {
    "annual_revenue": null,
    "estimated_worker_count": null,
    "mcc": null,
    "name": null,
    "product_description": null,
    "support_address": null,
    "support_email": null,
    "support_phone": null,
    "support_url": null,
    "url": null
  },
  "business_type": null,
  "capabilities": {},
  "charges_enabled": false,
  "controller": {
    "fees": {
      "payer": "application"
    },
    "is_controller": true,
    "losses": {
      "payments": "application"
    },
    "requirement_collection": "stripe",
    "stripe_dashboard": {
      "type": "express"
    },
    "type": "application"
  },
  "country": "US",
  "created": 1385798567,
  "default_currency": "usd",
  "details_submitted": true,
  "email": "jenny.rosen@example.com",
  "external_accounts": {
    "object": "list",
    "data": [],
    "has_more": false,
    "total_count": 0,
    "url": "/v1/accounts/acct_1Nv0FGQ9RKHgCVdK/external_accounts"
  },
  "future_requirements": {
    "alternatives": [],
    "current_deadline": null,
    "currently_due": [],
    "disabled_reason": null,
    "errors": [],
    "eventually_due": [],
    "past_due": [],
    "pending_verification": []
  },
  "login_links": {
    "object": "list",
    "total_count": 0,
    "has_more": false,
    "url": "/v1/accounts/acct_1Nv0FGQ9RKHgCVdK/login_links",
    "data": []
  },
  "metadata": {},
  "payouts_enabled": true,
  "requirements": {
    "alternatives": [],
    "current_deadline": null,
    "currently_due": [
      "business_profile.mcc",
      "business_profile.product_description",
      "business_profile.support_phone",
      "business_profile.url",
      "business_type",
      "external_account",
      "person_8UayFKIMRJklog.first_name",
      "person_8UayFKIMRJklog.last_name",
      "tos_acceptance.date",
      "tos_acceptance.ip"
    ],
    "disabled_reason": "rejected.fraud",
    "errors": [],
    "eventually_due": [
      "business_profile.mcc",
      "business_profile.product_description",
      "business_profile.support_phone",
      "business_profile.url",
      "business_type",
      "external_account",
      "person_8UayFKIMRJklog.first_name",
      "person_8UayFKIMRJklog.last_name",
      "tos_acceptance.date",
      "tos_acceptance.ip"
    ],
    "past_due": [
      "business_profile.mcc",
      "business_profile.product_description",
      "business_profile.support_phone",
      "business_profile.url",
      "business_type",
      "external_account",
      "person_8UayFKIMRJklog.first_name",
      "person_8UayFKIMRJklog.last_name",
      "tos_acceptance.date",
      "tos_acceptance.ip"
    ],
    "pending_verification": []
  },
  "settings": {
    "bacs_debit_payments": {
      "display_name": null,
      "service_user_number": null
    },
    "branding": {
      "icon": null,
      "logo": null,
      "primary_color": null,
      "secondary_color": null
    },
    "card_issuing": {
      "tos_acceptance": {
        "date": null,
        "ip": null
      }
    },
    "card_payments": {
      "decline_on": {
        "avs_failure": false,
        "cvc_failure": false
      },
      "statement_descriptor_prefix": null,
      "statement_descriptor_prefix_kanji": null,
      "statement_descriptor_prefix_kana": null
    },
    "dashboard": {
      "display_name": null,
      "timezone": "Etc/UTC"
    },
    "invoices": {
      "default_account_tax_ids": null
    },
    "payments": {
      "statement_descriptor": null,
      "statement_descriptor_kana": null,
      "statement_descriptor_kanji": null
    },
    "payouts": {
      "debit_negative_balances": true,
      "schedule": {
        "delay_days": 2,
        "interval": "daily"
      },
      "statement_descriptor": null
    },
    "sepa_debit_payments": {}
  },
  "tos_acceptance": {
    "date": null,
    "ip": null,
    "user_agent": null
  },
  "type": "none"
}
```