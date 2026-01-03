# Create an Account Session

Creates a AccountSession object that includes a single-use token that the platform can use on their front-end to grant client-side API access.

## Returns

Returns an Account Session object if the call succeeded.

## Parameters

- `account` (string, required)
  The identifier of the account to create an Account Session for.

- `components` (object, required)
  Each key of the dictionary represents an embedded component, and each embedded component maps to its configuration (e.g. whether it has been enabled or not).

  - `components.account_management` (object, optional)
    Configuration for the [account management](https://docs.stripe.com/connect/supported-embedded-components/account-management/.md) embedded component.

    - `components.account_management.enabled` (boolean, required)
      Whether the embedded component is enabled.

    - `components.account_management.features` (object, optional)
      The list of features enabled in the embedded component.

      - `components.account_management.features.disable_stripe_user_authentication` (boolean, optional)
        Whether Stripe user authentication is disabled. This value can only be `true` for accounts where `controller.requirement_collection` is `application` for the account. The default value is the opposite of the `external_account_collection` value. For example, if you don’t set `external_account_collection`, it defaults to `true` and `disable_stripe_user_authentication` defaults to `false`.

      - `components.account_management.features.external_account_collection` (boolean, optional)
        Whether external account collection is enabled. This feature can only be `false` for accounts where you’re responsible for collecting updated information when requirements are due or change, like Custom accounts. The default value for this feature is `true`.

  - `components.account_onboarding` (object, optional)
    Configuration for the [account onboarding](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding/.md) embedded component.

    - `components.account_onboarding.enabled` (boolean, required)
      Whether the embedded component is enabled.

    - `components.account_onboarding.features` (object, optional)
      The list of features enabled in the embedded component.

      - `components.account_onboarding.features.disable_stripe_user_authentication` (boolean, optional)
        Whether Stripe user authentication is disabled. This value can only be `true` for accounts where `controller.requirement_collection` is `application` for the account. The default value is the opposite of the `external_account_collection` value. For example, if you don’t set `external_account_collection`, it defaults to `true` and `disable_stripe_user_authentication` defaults to `false`.

      - `components.account_onboarding.features.external_account_collection` (boolean, optional)
        Whether external account collection is enabled. This feature can only be `false` for accounts where you’re responsible for collecting updated information when requirements are due or change, like Custom accounts. The default value for this feature is `true`.

  - `components.balances` (object, optional)
    Configuration for the [balances](https://docs.stripe.com/connect/supported-embedded-components/balances/.md) embedded component.

    - `components.balances.enabled` (boolean, required)
      Whether the embedded component is enabled.

    - `components.balances.features` (object, optional)
      The list of features enabled in the embedded component.

      - `components.balances.features.disable_stripe_user_authentication` (boolean, optional)
        Whether Stripe user authentication is disabled. This value can only be `true` for accounts where `controller.requirement_collection` is `application` for the account. The default value is the opposite of the `external_account_collection` value. For example, if you don’t set `external_account_collection`, it defaults to `true` and `disable_stripe_user_authentication` defaults to `false`.

      - `components.balances.features.edit_payout_schedule` (boolean, optional)
        Whether to allow payout schedule to be changed.  Defaults to `true` when `controller.losses.payments` is set to `stripe` for the account, otherwise `false`.

      - `components.balances.features.external_account_collection` (boolean, optional)
        Whether external account collection is enabled. This feature can only be `false` for accounts where you’re responsible for collecting updated information when requirements are due or change, like Custom accounts. The default value for this feature is `true`.

      - `components.balances.features.instant_payouts` (boolean, optional)
        Whether to allow creation of instant payouts. Defaults to `true` when `controller.losses.payments` is set to `stripe` for the account, otherwise `false`.

      - `components.balances.features.standard_payouts` (boolean, optional)
        Whether to allow creation of standard payouts.  Defaults to `true` when `controller.losses.payments` is set to `stripe` for the account, otherwise `false`.

  - `components.disputes_list` (object, optional)
    Configuration for the [disputes list](https://docs.stripe.com/connect/supported-embedded-components/disputes-list/.md) embedded component.

    - `components.disputes_list.enabled` (boolean, required)
      Whether the embedded component is enabled.

    - `components.disputes_list.features` (object, optional)
      The list of features enabled in the embedded component.

      - `components.disputes_list.features.capture_payments` (boolean, optional)
        Whether to allow capturing and cancelling payment intents. This is `true` by default.

      - `components.disputes_list.features.destination_on_behalf_of_charge_management` (boolean, optional)
        Whether connected accounts can manage destination charges that are created on behalf of them. This is `false` by default.

      - `components.disputes_list.features.dispute_management` (boolean, optional)
        Whether responding to disputes is enabled, including submitting evidence and accepting disputes. This is `true` by default.

      - `components.disputes_list.features.refund_management` (boolean, optional)
        Whether sending refunds is enabled. This is `true` by default.

  - `components.documents` (object, optional)
    Configuration for the [documents](https://docs.stripe.com/connect/supported-embedded-components/documents/.md) embedded component.

    - `components.documents.enabled` (boolean, required)
      Whether the embedded component is enabled.

    - `components.documents.features` (object, optional)
      An empty list, because this embedded component has no features.

  - `components.financial_account` (object, optional)
    Configuration for the [financial account](https://docs.stripe.com/connect/supported-embedded-components/financial-account/.md) embedded component.

    - `components.financial_account.enabled` (boolean, required)
      Whether the embedded component is enabled.

    - `components.financial_account.features` (object, optional)
      The list of features enabled in the embedded component.

      - `components.financial_account.features.disable_stripe_user_authentication` (boolean, optional)
        Whether Stripe user authentication is disabled. This value can only be `true` for accounts where `controller.requirement_collection` is `application` for the account. The default value is the opposite of the `external_account_collection` value. For example, if you don’t set `external_account_collection`, it defaults to `true` and `disable_stripe_user_authentication` defaults to `false`.

      - `components.financial_account.features.external_account_collection` (boolean, optional)
        Whether external account collection is enabled. This feature can only be `false` for accounts where you’re responsible for collecting updated information when requirements are due or change, like Custom accounts. The default value for this feature is `true`.

      - `components.financial_account.features.send_money` (boolean, optional)
        Whether to allow sending money.

      - `components.financial_account.features.transfer_balance` (boolean, optional)
        Whether to allow transferring balance.

  - `components.financial_account_transactions` (object, optional)
    Configuration for the [financial account transactions](https://docs.stripe.com/connect/supported-embedded-components/financial-account-transactions/.md) embedded component.

    - `components.financial_account_transactions.enabled` (boolean, required)
      Whether the embedded component is enabled.

    - `components.financial_account_transactions.features` (object, optional)
      The list of features enabled in the embedded component.

      - `components.financial_account_transactions.features.card_spend_dispute_management` (boolean, optional)
        Whether to allow card spend dispute management features.

  - `components.instant_payouts_promotion` (object, optional)
    Configuration for the [instant payouts promotion](https://docs.stripe.com/connect/supported-embedded-components/instant-payouts-promotion/.md) embedded component.

    - `components.instant_payouts_promotion.enabled` (boolean, required)
      Whether the embedded component is enabled.

    - `components.instant_payouts_promotion.features` (object, optional)
      The list of features enabled in the embedded component.

      - `components.instant_payouts_promotion.features.disable_stripe_user_authentication` (boolean, optional)
        Whether Stripe user authentication is disabled. This value can only be `true` for accounts where `controller.requirement_collection` is `application` for the account. The default value is the opposite of the `external_account_collection` value. For example, if you don’t set `external_account_collection`, it defaults to `true` and `disable_stripe_user_authentication` defaults to `false`.

      - `components.instant_payouts_promotion.features.external_account_collection` (boolean, optional)
        Whether external account collection is enabled. This feature can only be `false` for accounts where you’re responsible for collecting updated information when requirements are due or change, like Custom accounts. The default value for this feature is `true`.

      - `components.instant_payouts_promotion.features.instant_payouts` (boolean, optional)
        Whether to allow creation of instant payouts. Defaults to `true` when `controller.losses.payments` is set to `stripe` for the account, otherwise `false`.

  - `components.issuing_card` (object, optional)
    Configuration for the [issuing card](https://docs.stripe.com/connect/supported-embedded-components/issuing-card/.md) embedded component.

    - `components.issuing_card.enabled` (boolean, required)
      Whether the embedded component is enabled.

    - `components.issuing_card.features` (object, optional)
      The list of features enabled in the embedded component.

      - `components.issuing_card.features.card_management` (boolean, optional)
        Whether to allow card management features.

      - `components.issuing_card.features.card_spend_dispute_management` (boolean, optional)
        Whether to allow card spend dispute management features.

      - `components.issuing_card.features.cardholder_management` (boolean, optional)
        Whether to allow cardholder management features.

      - `components.issuing_card.features.spend_control_management` (boolean, optional)
        Whether to allow spend control management features.

  - `components.issuing_cards_list` (object, optional)
    Configuration for the [issuing cards list](https://docs.stripe.com/connect/supported-embedded-components/issuing-cards-list/.md) embedded component.

    - `components.issuing_cards_list.enabled` (boolean, required)
      Whether the embedded component is enabled.

    - `components.issuing_cards_list.features` (object, optional)
      The list of features enabled in the embedded component.

      - `components.issuing_cards_list.features.card_management` (boolean, optional)
        Whether to allow card management features.

      - `components.issuing_cards_list.features.card_spend_dispute_management` (boolean, optional)
        Whether to allow card spend dispute management features.

      - `components.issuing_cards_list.features.cardholder_management` (boolean, optional)
        Whether to allow cardholder management features.

      - `components.issuing_cards_list.features.disable_stripe_user_authentication` (boolean, optional)
        Whether Stripe user authentication is disabled. This value can only be `true` for accounts where `controller.requirement_collection` is `application` for the account. The default value is the opposite of the `external_account_collection` value. For example, if you don’t set `external_account_collection`, it defaults to `true` and `disable_stripe_user_authentication` defaults to `false`.

      - `components.issuing_cards_list.features.spend_control_management` (boolean, optional)
        Whether to allow spend control management features.

  - `components.notification_banner` (object, optional)
    Configuration for the [notification banner](https://docs.stripe.com/connect/supported-embedded-components/notification-banner/.md) embedded component.

    - `components.notification_banner.enabled` (boolean, required)
      Whether the embedded component is enabled.

    - `components.notification_banner.features` (object, optional)
      The list of features enabled in the embedded component.

      - `components.notification_banner.features.disable_stripe_user_authentication` (boolean, optional)
        Whether Stripe user authentication is disabled. This value can only be `true` for accounts where `controller.requirement_collection` is `application` for the account. The default value is the opposite of the `external_account_collection` value. For example, if you don’t set `external_account_collection`, it defaults to `true` and `disable_stripe_user_authentication` defaults to `false`.

      - `components.notification_banner.features.external_account_collection` (boolean, optional)
        Whether external account collection is enabled. This feature can only be `false` for accounts where you’re responsible for collecting updated information when requirements are due or change, like Custom accounts. The default value for this feature is `true`.

  - `components.payment_details` (object, optional)
    Configuration for the [payment details](https://docs.stripe.com/connect/supported-embedded-components/payment-details/.md) embedded component.

    - `components.payment_details.enabled` (boolean, required)
      Whether the embedded component is enabled.

    - `components.payment_details.features` (object, optional)
      The list of features enabled in the embedded component.

      - `components.payment_details.features.capture_payments` (boolean, optional)
        Whether to allow capturing and cancelling payment intents. This is `true` by default.

      - `components.payment_details.features.destination_on_behalf_of_charge_management` (boolean, optional)
        Whether connected accounts can manage destination charges that are created on behalf of them. This is `false` by default.

      - `components.payment_details.features.dispute_management` (boolean, optional)
        Whether responding to disputes is enabled, including submitting evidence and accepting disputes. This is `true` by default.

      - `components.payment_details.features.refund_management` (boolean, optional)
        Whether sending refunds is enabled. This is `true` by default.

  - `components.payment_disputes` (object, optional)
    Configuration for the [payment disputes](https://docs.stripe.com/connect/supported-embedded-components/payment-disputes/.md) embedded component.

    - `components.payment_disputes.enabled` (boolean, required)
      Whether the embedded component is enabled.

    - `components.payment_disputes.features` (object, optional)
      The list of features enabled in the embedded component.

      - `components.payment_disputes.features.destination_on_behalf_of_charge_management` (boolean, optional)
        Whether connected accounts can manage destination charges that are created on behalf of them. This is `false` by default.

      - `components.payment_disputes.features.dispute_management` (boolean, optional)
        Whether responding to disputes is enabled, including submitting evidence and accepting disputes. This is `true` by default.

      - `components.payment_disputes.features.refund_management` (boolean, optional)
        Whether sending refunds is enabled. This is `true` by default.

  - `components.payments` (object, optional)
    Configuration for the [payments](https://docs.stripe.com/connect/supported-embedded-components/payments/.md) embedded component.

    - `components.payments.enabled` (boolean, required)
      Whether the embedded component is enabled.

    - `components.payments.features` (object, optional)
      The list of features enabled in the embedded component.

      - `components.payments.features.capture_payments` (boolean, optional)
        Whether to allow capturing and cancelling payment intents. This is `true` by default.

      - `components.payments.features.destination_on_behalf_of_charge_management` (boolean, optional)
        Whether connected accounts can manage destination charges that are created on behalf of them. This is `false` by default.

      - `components.payments.features.dispute_management` (boolean, optional)
        Whether responding to disputes is enabled, including submitting evidence and accepting disputes. This is `true` by default.

      - `components.payments.features.refund_management` (boolean, optional)
        Whether sending refunds is enabled. This is `true` by default.

  - `components.payout_details` (object, optional)
    Configuration for the [payout details](https://docs.stripe.com/connect/supported-embedded-components/payout-details/.md) embedded component.

    - `components.payout_details.enabled` (boolean, required)
      Whether the embedded component is enabled.

    - `components.payout_details.features` (object, optional)
      An empty list, because this embedded component has no features.

  - `components.payouts` (object, optional)
    Configuration for the [payouts](https://docs.stripe.com/connect/supported-embedded-components/payouts/.md) embedded component.

    - `components.payouts.enabled` (boolean, required)
      Whether the embedded component is enabled.

    - `components.payouts.features` (object, optional)
      The list of features enabled in the embedded component.

      - `components.payouts.features.disable_stripe_user_authentication` (boolean, optional)
        Whether Stripe user authentication is disabled. This value can only be `true` for accounts where `controller.requirement_collection` is `application` for the account. The default value is the opposite of the `external_account_collection` value. For example, if you don’t set `external_account_collection`, it defaults to `true` and `disable_stripe_user_authentication` defaults to `false`.

      - `components.payouts.features.edit_payout_schedule` (boolean, optional)
        Whether to allow payout schedule to be changed.  Defaults to `true` when `controller.losses.payments` is set to `stripe` for the account, otherwise `false`.

      - `components.payouts.features.external_account_collection` (boolean, optional)
        Whether external account collection is enabled. This feature can only be `false` for accounts where you’re responsible for collecting updated information when requirements are due or change, like Custom accounts. The default value for this feature is `true`.

      - `components.payouts.features.instant_payouts` (boolean, optional)
        Whether to allow creation of instant payouts. Defaults to `true` when `controller.losses.payments` is set to `stripe` for the account, otherwise `false`.

      - `components.payouts.features.standard_payouts` (boolean, optional)
        Whether to allow creation of standard payouts.  Defaults to `true` when `controller.losses.payments` is set to `stripe` for the account, otherwise `false`.

  - `components.payouts_list` (object, optional)
    Configuration for the [payouts list](https://docs.stripe.com/connect/supported-embedded-components/payouts-list/.md) embedded component.

    - `components.payouts_list.enabled` (boolean, required)
      Whether the embedded component is enabled.

    - `components.payouts_list.features` (object, optional)
      An empty list, because this embedded component has no features.

  - `components.tax_registrations` (object, optional)
    Configuration for the [tax registrations](https://docs.stripe.com/connect/supported-embedded-components/tax-registrations/.md) embedded component.

    - `components.tax_registrations.enabled` (boolean, required)
      Whether the embedded component is enabled.

    - `components.tax_registrations.features` (object, optional)
      An empty list, because this embedded component has no features.

  - `components.tax_settings` (object, optional)
    Configuration for the [tax settings](https://docs.stripe.com/connect/supported-embedded-components/tax-settings/.md) embedded component.

    - `components.tax_settings.enabled` (boolean, required)
      Whether the embedded component is enabled.

    - `components.tax_settings.features` (object, optional)
      An empty list, because this embedded component has no features.

```curl
curl https://api.stripe.com/v1/account_sessions \
  -u "<<YOUR_SECRET_KEY>>" \
  -d account=acct_1NkDjjJyhOZfPCWt \
  -d "components[account_onboarding][enabled]"=true \
  -d "components[payments][enabled]"=true \
  -d "components[payouts][enabled]"=true \
  -d "components[balances][enabled]"=true
```

```cli
stripe account_sessions create  \
  --account=acct_1NkDjjJyhOZfPCWt \
  -d "components[account_onboarding][enabled]"=true \
  -d "components[payments][enabled]"=true \
  -d "components[payouts][enabled]"=true \
  -d "components[balances][enabled]"=true
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

account_session = client.v1.account_sessions.create({
  account: 'acct_1NkDjjJyhOZfPCWt',
  components: {
    account_onboarding: {enabled: true},
    payments: {enabled: true},
    payouts: {enabled: true},
    balances: {enabled: true},
  },
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

account_session = client.v1.account_sessions.create({
  "account": "acct_1NkDjjJyhOZfPCWt",
  "components": {
    "account_onboarding": {"enabled": True},
    "payments": {"enabled": True},
    "payouts": {"enabled": True},
    "balances": {"enabled": True},
  },
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$accountSession = $stripe->accountSessions->create([
  'account' => 'acct_1NkDjjJyhOZfPCWt',
  'components' => [
    'account_onboarding' => ['enabled' => true],
    'payments' => ['enabled' => true],
    'payouts' => ['enabled' => true],
    'balances' => ['enabled' => true],
  ],
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AccountSessionCreateParams params =
  AccountSessionCreateParams.builder()
    .setAccount("acct_1NkDjjJyhOZfPCWt")
    .setComponents(
      AccountSessionCreateParams.Components.builder()
        .setAccountOnboarding(
          AccountSessionCreateParams.Components.AccountOnboarding.builder()
            .setEnabled(true)
            .build()
        )
        .setPayments(
          AccountSessionCreateParams.Components.Payments.builder()
            .setEnabled(true)
            .build()
        )
        .setPayouts(
          AccountSessionCreateParams.Components.Payouts.builder()
            .setEnabled(true)
            .build()
        )
        .setBalances(
          AccountSessionCreateParams.Components.Balances.builder()
            .setEnabled(true)
            .build()
        )
        .build()
    )
    .build();

AccountSession accountSession = client.v1().accountSessions().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const accountSession = await stripe.accountSessions.create({
  account: 'acct_1NkDjjJyhOZfPCWt',
  components: {
    account_onboarding: {
      enabled: true,
    },
    payments: {
      enabled: true,
    },
    payouts: {
      enabled: true,
    },
    balances: {
      enabled: true,
    },
  },
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.AccountSessionCreateParams{
  Account: stripe.String("acct_1NkDjjJyhOZfPCWt"),
  Components: &stripe.AccountSessionCreateComponentsParams{
    AccountOnboarding: &stripe.AccountSessionCreateComponentsAccountOnboardingParams{
      Enabled: stripe.Bool(true),
    },
    Payments: &stripe.AccountSessionCreateComponentsPaymentsParams{
      Enabled: stripe.Bool(true),
    },
    Payouts: &stripe.AccountSessionCreateComponentsPayoutsParams{
      Enabled: stripe.Bool(true),
    },
    Balances: &stripe.AccountSessionCreateComponentsBalancesParams{
      Enabled: stripe.Bool(true),
    },
  },
}
result, err := sc.V1AccountSessions.Create(context.TODO(), params)
```

```dotnet
var options = new AccountSessionCreateOptions
{
    Account = "acct_1NkDjjJyhOZfPCWt",
    Components = new AccountSessionComponentsOptions
    {
        AccountOnboarding = new AccountSessionComponentsAccountOnboardingOptions
        {
            Enabled = true,
        },
        Payments = new AccountSessionComponentsPaymentsOptions { Enabled = true },
        Payouts = new AccountSessionComponentsPayoutsOptions { Enabled = true },
        Balances = new AccountSessionComponentsBalancesOptions { Enabled = true },
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.AccountSessions;
AccountSession accountSession = service.Create(options);
```

### Response

```json
{
  "object": "account_session",
  "account": "acct_1NkDjjJyhOZfPCWt",
  "client_secret": "_OXIKXxEihJokDBnDoe2sgG5OGSO2Q12shKvbeboxpALZGng",
  "expires_at": 1693261123,
  "livemode": false,
  "components": {
    "account_management": {
      "enabled": false,
      "features": {
        "external_account_collection": true,
        "disable_stripe_user_authentication": false
      }
    },
    "account_onboarding": {
      "enabled": true,
      "features": {
        "external_account_collection": true,
        "disable_stripe_user_authentication": false
      }
    },
    "balances": {
      "enabled": true,
      "features": {
        "edit_payout_schedule": false,
        "instant_payouts": false,
        "standard_payouts": false,
        "external_account_collection": true,
        "disable_stripe_user_authentication": false
      }
    },
    "documents": {
      "enabled": false,
      "features": {}
    },
    "financial_account": {
      "enabled": false,
      "features": {
        "disable_stripe_user_authentication": false,
        "external_account_collection": false,
        "money_movement": false,
        "send_money": false,
        "transfer_balance": false
      }
    },
    "financial_account_transactions": {
      "enabled": false,
      "features": {
        "card_spend_dispute_management": false
      }
    },
    "issuing_card": {
      "enabled": false,
      "features": {
        "card_management": false,
        "card_spend_dispute_management": false,
        "cardholder_management": false,
        "spend_control_management": false
      }
    },
    "issuing_cards_list": {
      "enabled": false,
      "features": {
        "card_management": false,
        "card_spend_dispute_management": false,
        "cardholder_management": false,
        "disable_stripe_user_authentication": false,
        "spend_control_management": false
      }
    },
    "notification_banner": {
      "enabled": false,
      "features": {
        "external_account_collection": true,
        "disable_stripe_user_authentication": false
      }
    },
    "payment_details": {
      "enabled": false,
      "features": {
        "capture_payments": true,
        "destination_on_behalf_of_charge_management": false,
        "dispute_management": true,
        "refund_management": true
      }
    },
    "payments": {
      "enabled": true,
      "features": {
        "capture_payments": true,
        "destination_on_behalf_of_charge_management": false,
        "dispute_management": true,
        "refund_management": true
      }
    },
    "disputes_list": {
      "enabled": false,
      "features": {
        "capture_payments": true,
        "destination_on_behalf_of_charge_management": false,
        "dispute_management": true,
        "refund_management": true
      }
    },
    "payment_disputes": {
      "enabled": false,
      "features": {
        "destination_on_behalf_of_charge_management": false,
        "dispute_management": true,
        "refund_management": true
      }
    },
    "payouts": {
      "enabled": true,
      "features": {
        "edit_payout_schedule": false,
        "instant_payouts": false,
        "standard_payouts": false,
        "external_account_collection": true,
        "disable_stripe_user_authentication": false
      }
    },
    "payouts_list": {
      "enabled": false,
      "features": {}
    },
    "tax_registrations": {
      "enabled": false,
      "features": {}
    },
    "tax_settings": {
      "enabled": false,
      "features": {}
    },
    "instant_payouts_promotion": {
      "enabled": false,
      "features": {
        "disable_stripe_user_authentication": false,
        "external_account_collection": true,
        "instant_payouts": false
      }
    },
    "payout_details": {
      "enabled": false,
      "features": {}
    }
  }
}
```