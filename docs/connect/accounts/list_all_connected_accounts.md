# List all connected accounts

Returns a list of accounts connected to your platform via [Connect](https://docs.stripe.com/docs/connect.md). If you’re not a platform, the list is empty.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` accounts, starting after account `starting_after`. Each entry in the array is a separate [`Account`](https://docs.stripe.com/api/accounts/list.md#account_object) object. If no more accounts are available, the resulting array is empty.

## Parameters

- `created` (object, optional)
  Only return connected accounts that were created during the given date interval.

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

```curl
curl -G https://api.stripe.com/v1/accounts \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe accounts list  \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

accounts = client.v1.accounts.list({limit: 3})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

accounts = client.v1.accounts.list({"limit": 3})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$accounts = $stripe->accounts->all(['limit' => 3]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AccountListParams params = AccountListParams.builder().setLimit(3L).build();

StripeCollection<Account> stripeCollection = client.v1().accounts().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const accounts = await stripe.accounts.list({
  limit: 3,
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.AccountListParams{}
params.Limit = stripe.Int64(3)
result := sc.V1Accounts.List(context.TODO(), params)
```

```dotnet
var options = new AccountListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Accounts;
StripeList<Account> accounts = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/accounts",
  "has_more": false,
  "data": [
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
      "created": 1695830751,
      "default_currency": "usd",
      "details_submitted": false,
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
      "payouts_enabled": false,
      "requirements": {
        "alternatives": [],
        "current_deadline": null,
        "currently_due": [
          "business_profile.mcc",
          "business_profile.url",
          "business_type",
          "external_account",
          "representative.first_name",
          "representative.last_name",
          "tos_acceptance.date",
          "tos_acceptance.ip"
        ],
        "disabled_reason": "requirements.past_due",
        "errors": [],
        "eventually_due": [
          "business_profile.mcc",
          "business_profile.url",
          "business_type",
          "external_account",
          "representative.first_name",
          "representative.last_name",
          "tos_acceptance.date",
          "tos_acceptance.ip"
        ],
        "past_due": [
          "business_profile.mcc",
          "business_profile.url",
          "business_type",
          "external_account",
          "representative.first_name",
          "representative.last_name",
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
  ]
}
```