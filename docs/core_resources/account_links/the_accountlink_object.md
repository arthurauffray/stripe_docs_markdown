# The AccountLink object

## Attributes

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

### The AccountLink object

```json
{
  "object": "v2.core.account_link",
  "account": "acct_1Nv0FGQ9RKHgCVdK",
  "created": "2025-03-27T17:15:18.000Z",
  "expires_at": "2025-03-27T17:25:18.000Z",
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