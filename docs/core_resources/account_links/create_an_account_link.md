# Create an account link

Creates an AccountLink object that includes a single-use URL that an account can use to access a Stripe-hosted flow for collecting or updating required information.

## Parameters

- `account` (string, required)
  The ID of the Account to create link for.

- `use_case` (object, required)
  The use case of the AccountLink.

  - `use_case.account_onboarding` (object, optional)
    Hash containing configuration options for an Account Link object that onboards a new account.

    - `use_case.account_onboarding.collection_options` (object, optional)
      Specifies the requirements that Stripe collects from v2/core/accounts in the Onboarding flow.

      - `use_case.account_onboarding.collection_options.fields` (enum, optional)
        Specifies whether the platform collects only currently_due requirements (`currently_due`) or both currently_due and eventually_due requirements (`eventually_due`). If you don’t specify collection_options, the default value is currently_due.
Possible enum values:
        - `currently_due`
          Collect currently_due requirements.

        - `eventually_due`
          Collect eventually_due and currently_due requirements.

      - `use_case.account_onboarding.collection_options.future_requirements` (enum, optional)
        Specifies whether the platform collects future_requirements in addition to requirements in Connect Onboarding. The default value is `omit`.
Possible enum values:
        - `include`
          Include future requirements.

        - `omit`
          Omit future requirements.

    - `use_case.account_onboarding.configurations` (array of enums, required)
      Open Enum. A v2/core/account can be configured to enable certain functionality. The configuration param targets the v2/core/account_link to collect information for the specified v2/core/account configuration/s.
Possible enum values:
      - `customer`
        To onboard a new customer.

      - `merchant`
        To onboard a new merchant.

      - `recipient`
        To onboard a new recipient.

    - `use_case.account_onboarding.refresh_url` (string, required)
      The URL the user will be redirected to if the AccountLink is expired, has been used, or is otherwise invalid. The URL you specify should attempt to generate a new AccountLink with the same parameters used to create the original AccountLink, then redirect the user to the new AccountLink’s URL so they can continue the flow. If a new AccountLink cannot be generated or the redirect fails you should display a useful error to the user. Please make sure to implement authentication before redirecting the user in case this URL is leaked to a third party.

    - `use_case.account_onboarding.return_url` (string, optional)
      The URL that the user will be redirected to upon completing the linked flow.

  - `use_case.account_update` (object, optional)
    Hash containing configuration options for an Account Link that updates an existing account.

    - `use_case.account_update.collection_options` (object, optional)
      Specifies the requirements that Stripe collects from v2/core/accounts in the Onboarding flow.

      - `use_case.account_update.collection_options.fields` (enum, optional)
        Specifies whether the platform collects only currently_due requirements (`currently_due`) or both currently_due and eventually_due requirements (`eventually_due`). The default value is `currently_due`.
Possible enum values:
        - `currently_due`
          Collect currently_due requirements.

        - `eventually_due`
          Collect eventually_due and currently_due requirements.

      - `use_case.account_update.collection_options.future_requirements` (enum, optional)
        Specifies whether the platform collects future_requirements in addition to requirements in Connect Onboarding. The default value is `omit`.
Possible enum values:
        - `include`
          Include future requirements.

        - `omit`
          Omit future requirements.

    - `use_case.account_update.configurations` (array of enums, required)
      Open Enum. A v2/account can be configured to enable certain functionality. The configuration param targets the v2/account_link to collect information for the specified v2/account configuration/s.
Possible enum values:
      - `customer`
        To onboard a new customer.

      - `merchant`
        To onboard a new merchant.

      - `recipient`
        To update a new recipient.

    - `use_case.account_update.refresh_url` (string, required)
      The URL the user will be redirected to if the Account Link is expired, has been used, or is otherwise invalid. The URL you specify should attempt to generate a new Account Link with the same parameters used to create the original Account Link, then redirect the user to the new Account Link URL so they can continue the flow. Make sure to authenticate the user before redirecting to the new Account Link, in case the URL leaks to a third party. If a new Account Link can’t be generated, or if the redirect fails, you should display a useful error to the user.

    - `use_case.account_update.return_url` (string, optional)
      The URL that the user will be redirected to upon completing the linked flow.

  - `use_case.type` (enum, required)
    The type of Account Link the user is requesting.
Possible enum values:
    - `account_onboarding`
      A form to collect all required information to onboard a new account.

    - `account_update`
      A form to collect all required information to update a previously onboarded account.

## Returns

## Response attributes

- `object` (string, value is "v2.core.account_link")
  String representing the object’s type. Objects of the same type share the same value of the object field.

- `account` (string)
  The ID of the connected account this Account Link applies to.

- `created` (timestamp)
  The timestamp at which this Account Link was created.

- `expires_at` (timestamp)
  The timestamp at which this Account Link will expire.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `url` (string)
  The URL at which the account can access the Stripe-hosted flow.

- `use_case` (object)
  Hash containing usage options.

  - `use_case.account_onboarding` (object, nullable)
    Hash containing configuration options for an Account Link object that onboards a new account.

    - `use_case.account_onboarding.collection_options` (object, nullable)
      Specifies the requirements that Stripe collects from v2/core/accounts in the Onboarding flow.

      - `use_case.account_onboarding.collection_options.fields` (enum, nullable)
        Specifies whether the platform collects only currently_due requirements (`currently_due`) or both currently_due and eventually_due requirements (`eventually_due`). If you don’t specify collection_options, the default value is currently_due.
Possible enum values:
        - `currently_due`
          Collect currently_due requirements.

        - `eventually_due`
          Collect eventually_due and currently_due requirements.

      - `use_case.account_onboarding.collection_options.future_requirements` (enum, nullable)
        Specifies whether the platform collects future_requirements in addition to requirements in Connect Onboarding. The default value is `omit`.
Possible enum values:
        - `include`
          Include future requirements.

        - `omit`
          Omit future requirements.

    - `use_case.account_onboarding.configurations` (array of enums)
      Open Enum. A v2/core/account can be configured to enable certain functionality. The configuration param targets the v2/core/account_link to collect information for the specified v2/core/account configuration/s.
Possible enum values:
      - `customer`
        To onboard a new customer.

      - `merchant`
        To onboard a new merchant.

      - `recipient`
        To onboard a new recipient.

    - `use_case.account_onboarding.refresh_url` (string)
      The URL the user will be redirected to if the AccountLink is expired, has been used, or is otherwise invalid. The URL you specify should attempt to generate a new AccountLink with the same parameters used to create the original AccountLink, then redirect the user to the new AccountLink’s URL so they can continue the flow. If a new AccountLink cannot be generated or the redirect fails you should display a useful error to the user. Please make sure to implement authentication before redirecting the user in case this URL is leaked to a third party.

    - `use_case.account_onboarding.return_url` (string, nullable)
      The URL that the user will be redirected to upon completing the linked flow.

  - `use_case.account_update` (object, nullable)
    Hash containing configuration options for an Account Link that updates an existing account.

    - `use_case.account_update.collection_options` (object, nullable)
      Specifies the requirements that Stripe collects from v2/core/accounts in the Onboarding flow.

      - `use_case.account_update.collection_options.fields` (enum, nullable)
        Specifies whether the platform collects only currently_due requirements (`currently_due`) or both currently_due and eventually_due requirements (`eventually_due`). The default value is `currently_due`.
Possible enum values:
        - `currently_due`
          Collect currently_due requirements.

        - `eventually_due`
          Collect eventually_due and currently_due requirements.

      - `use_case.account_update.collection_options.future_requirements` (enum, nullable)
        Specifies whether the platform collects future_requirements in addition to requirements in Connect Onboarding. The default value is `omit`.
Possible enum values:
        - `include`
          Include future requirements.

        - `omit`
          Omit future requirements.

    - `use_case.account_update.configurations` (array of enums)
      Open Enum. A v2/account can be configured to enable certain functionality. The configuration param targets the v2/account_link to collect information for the specified v2/account configuration/s.
Possible enum values:
      - `customer`
        To onboard a new customer.

      - `merchant`
        To onboard a new merchant.

      - `recipient`
        To update a new recipient.

    - `use_case.account_update.refresh_url` (string)
      The URL the user will be redirected to if the Account Link is expired, has been used, or is otherwise invalid. The URL you specify should attempt to generate a new Account Link with the same parameters used to create the original Account Link, then redirect the user to the new Account Link URL so they can continue the flow. Make sure to authenticate the user before redirecting to the new Account Link, in case the URL leaks to a third party. If a new Account Link can’t be generated, or if the redirect fails, you should display a useful error to the user.

    - `use_case.account_update.return_url` (string, nullable)
      The URL that the user will be redirected to upon completing the linked flow.

  - `use_case.type` (enum)
    The type of Account Link the user is requesting.
Possible enum values:
    - `account_onboarding`
      A form to collect all required information to onboard a new account.

    - `account_update`
      A form to collect all required information to update a previously onboarded account.

## Error Codes

| HTTP status code | Code                                    | Description                                                                                      |
| ---------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------ |
| 400              | accounts_v2_access_blocked              | Accounts v2 is not enabled for your platform.                                                    |
| 400              | configs_must_match_to_use_account_links | Account cannot be onboard via v2/core/account_links without specifying the right configurations. |
| 404              | not_found                               | The resource wasn’t found.                                                                       |

```curl
curl -X POST https://api.stripe.com/v2/core/account_links \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: {{STRIPE_API_VERSION}}" \
  --json '{
    "account": "acct_1Nv0FGQ9RKHgCVdK",
    "use_case": {
        "type": "account_onboarding",
        "account_onboarding": {
            "configurations": [
                "recipient"
            ],
            "return_url": "https://example.com/return",
            "refresh_url": "https://example.com/reauth"
        }
    }
  }'
```

```cli
stripe v2 core account_links create  \
  --account=acct_1Nv0FGQ9RKHgCVdK \
  --use-case.type=account_onboarding \
  --use-case.account-onboarding.configurations=recipient \
  --use-case.account-onboarding.return-url="https://example.com/return" \
  --use-case.account-onboarding.refresh-url="https://example.com/reauth"
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

account_link = client.v2.core.account_links.create({
  account: 'acct_1Nv0FGQ9RKHgCVdK',
  use_case: {
    type: 'account_onboarding',
    account_onboarding: {
      configurations: ['recipient'],
      return_url: 'https://example.com/return',
      refresh_url: 'https://example.com/reauth',
    },
  },
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

account_link = client.v2.core.account_links.create({
  "account": "acct_1Nv0FGQ9RKHgCVdK",
  "use_case": {
    "type": "account_onboarding",
    "account_onboarding": {
      "configurations": ["recipient"],
      "return_url": "https://example.com/return",
      "refresh_url": "https://example.com/reauth",
    },
  },
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$accountLink = $stripe->v2->core->accountLinks->create([
  'account' => 'acct_1Nv0FGQ9RKHgCVdK',
  'use_case' => [
    'type' => 'account_onboarding',
    'account_onboarding' => [
      'configurations' => ['recipient'],
      'return_url' => 'https://example.com/return',
      'refresh_url' => 'https://example.com/reauth',
    ],
  ],
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AccountLinkCreateParams params =
  AccountLinkCreateParams.builder()
    .setAccount("acct_1Nv0FGQ9RKHgCVdK")
    .setUseCase(
      AccountLinkCreateParams.UseCase.builder()
        .setType(AccountLinkCreateParams.UseCase.Type.ACCOUNT_ONBOARDING)
        .setAccountOnboarding(
          AccountLinkCreateParams.UseCase.AccountOnboarding.builder()
            .addConfiguration(
              AccountLinkCreateParams.UseCase.AccountOnboarding.Configuration.RECIPIENT
            )
            .setReturnUrl("https://example.com/return")
            .setRefreshUrl("https://example.com/reauth")
            .build()
        )
        .build()
    )
    .build();

AccountLink accountLink = client.v2().core().accountLinks().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const accountLink = await stripe.v2.core.accountLinks.create({
  account: 'acct_1Nv0FGQ9RKHgCVdK',
  use_case: {
    type: 'account_onboarding',
    account_onboarding: {
      configurations: ['recipient'],
      return_url: 'https://example.com/return',
      refresh_url: 'https://example.com/reauth',
    },
  },
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.V2CoreAccountLinkCreateParams{
  Account: stripe.String("acct_1Nv0FGQ9RKHgCVdK"),
  UseCase: &stripe.V2CoreAccountLinkCreateUseCaseParams{
    Type: stripe.String("account_onboarding"),
    AccountOnboarding: &stripe.V2CoreAccountLinkCreateUseCaseAccountOnboardingParams{
      Configurations: []*string{stripe.String("recipient")},
      ReturnURL: stripe.String("https://example.com/return"),
      RefreshURL: stripe.String("https://example.com/reauth"),
    },
  },
}
result, err := sc.V2CoreAccountLinks.Create(context.TODO(), params)
```

```dotnet
var options = new Stripe.V2.Core.AccountLinkCreateOptions
{
    Account = "acct_1Nv0FGQ9RKHgCVdK",
    UseCase = new Stripe.V2.Core.AccountLinkCreateUseCaseOptions
    {
        Type = "account_onboarding",
        AccountOnboarding = new Stripe.V2.Core.AccountLinkCreateUseCaseAccountOnboardingOptions
        {
            Configurations = new List<string> { "recipient" },
            ReturnUrl = "https://example.com/return",
            RefreshUrl = "https://example.com/reauth",
        },
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V2.Core.AccountLinks;
Stripe.V2.Core.AccountLink accountLink = service.Create(options);
```

### Response

```json
{
  "object": "v2.core.account_link",
  "account": "acct_1Nv0FGQ9RKHgCVdK",
  "created": "2025-03-27T17:15:18.000Z",
  "expires_at": "2025-03-27T17:25:18.000Z",
  "livemode": true,
  "url": "https://accounts.stripe.com/r/acct_1Nv0FGQ9RKHgCVdK#alu_test_61SGhyomRuz7xsw5216SGhyj0ASQdCLwMKdRUF3mi3H6",
  "use_case": {
    "account_onboarding": {
      "configurations": [
        "recipient"
      ],
      "refresh_url": "https://example.com/reauth",
      "return_url": "https://example.com/return"
    },
    "type": "account_onboarding"
  }
}
```