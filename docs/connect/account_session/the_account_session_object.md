# The Account Session object

## Attributes

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `account` (string)
  The ID of the account the AccountSession was created for

- `client_secret` (string)
  The client secret of this AccountSession. Used on the client to set up secure access to the given `account`.

  The client secret can be used to provide access to `account` from your frontend. It should not be stored, logged, or exposed to anyone other than the connected account. Make sure that you have TLS enabled on any page that includes the client secret.

  Refer to our docs to [setup Connect embedded components](https://docs.stripe.com/docs/connect/get-started-connect-embedded-components.md) and learn about how `client_secret` should be handled.

- `components` (object)
  Information about which embedded components and component features are enabled for this Account Session. Components that have no features have an empty `features` hash.

  - `components.account_management` (object)
    Configuration for the [account management](https://docs.stripe.com/connect/supported-embedded-components/account-management/.md) embedded component.

    - `components.account_management.enabled` (boolean)
      Whether the embedded component is enabled.

    - `components.account_management.features` (object)
      The list of features enabled in the embedded component.

      - `components.account_management.features.disable_stripe_user_authentication` (boolean)
        Whether Stripe user authentication is disabled. This value can only be `true` for accounts where `controller.requirement_collection` is `application` for the account. The default value is the opposite of the `external_account_collection` value. For example, if you don’t set `external_account_collection`, it defaults to `true` and `disable_stripe_user_authentication` defaults to `false`.

      - `components.account_management.features.external_account_collection` (boolean)
        Whether external account collection is enabled. This feature can only be `false` for accounts where you’re responsible for collecting updated information when requirements are due or change, like Custom accounts. The default value for this feature is `true`.

  - `components.account_onboarding` (object)
    Configuration for the [account onboarding](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding/.md) embedded component.

    - `components.account_onboarding.enabled` (boolean)
      Whether the embedded component is enabled.

    - `components.account_onboarding.features` (object)
      The list of features enabled in the embedded component.

      - `components.account_onboarding.features.disable_stripe_user_authentication` (boolean)
        Whether Stripe user authentication is disabled. This value can only be `true` for accounts where `controller.requirement_collection` is `application` for the account. The default value is the opposite of the `external_account_collection` value. For example, if you don’t set `external_account_collection`, it defaults to `true` and `disable_stripe_user_authentication` defaults to `false`.

      - `components.account_onboarding.features.external_account_collection` (boolean)
        Whether external account collection is enabled. This feature can only be `false` for accounts where you’re responsible for collecting updated information when requirements are due or change, like Custom accounts. The default value for this feature is `true`.

  - `components.balance_report` (object)
    Configuration for the [balance report](https://docs.stripe.com/connect/supported-embedded-components/financial-reports.md#balance-report) embedded component.

    - `components.balance_report.enabled` (boolean)
      Whether the embedded component is enabled.

    - `components.balance_report.features` (object)
      An empty list, because this embedded component has no features.

  - `components.balances` (object)
    Configuration for the [balances](https://docs.stripe.com/connect/supported-embedded-components/balances/.md) embedded component.

    - `components.balances.enabled` (boolean)
      Whether the embedded component is enabled.

    - `components.balances.features` (object)
      The list of features enabled in the embedded component.

      - `components.balances.features.disable_stripe_user_authentication` (boolean)
        Whether Stripe user authentication is disabled. This value can only be `true` for accounts where `controller.requirement_collection` is `application` for the account. The default value is the opposite of the `external_account_collection` value. For example, if you don’t set `external_account_collection`, it defaults to `true` and `disable_stripe_user_authentication` defaults to `false`.

      - `components.balances.features.edit_payout_schedule` (boolean)
        Whether to allow payout schedule to be changed.  Defaults to `true` when `controller.losses.payments` is set to `stripe` for the account, otherwise `false`.

      - `components.balances.features.external_account_collection` (boolean)
        Whether external account collection is enabled. This feature can only be `false` for accounts where you’re responsible for collecting updated information when requirements are due or change, like Custom accounts. The default value for this feature is `true`.

      - `components.balances.features.instant_payouts` (boolean)
        Whether to allow creation of instant payouts. Defaults to `true` when `controller.losses.payments` is set to `stripe` for the account, otherwise `false`.

      - `components.balances.features.standard_payouts` (boolean)
        Whether to allow creation of standard payouts.  Defaults to `true` when `controller.losses.payments` is set to `stripe` for the account, otherwise `false`.

  - `components.disputes_list` (object)
    Configuration for the [disputes list](https://docs.stripe.com/connect/supported-embedded-components/disputes-list/.md) embedded component.

    - `components.disputes_list.enabled` (boolean)
      Whether the embedded component is enabled.

    - `components.disputes_list.features` (object)
      The list of features enabled in the embedded component.

      - `components.disputes_list.features.capture_payments` (boolean)
        Whether to allow capturing and cancelling payment intents. This is `true` by default.

      - `components.disputes_list.features.destination_on_behalf_of_charge_management` (boolean)
        Whether connected accounts can manage destination charges that are created on behalf of them. This is `false` by default.

      - `components.disputes_list.features.dispute_management` (boolean)
        Whether responding to disputes is enabled, including submitting evidence and accepting disputes. This is `true` by default.

      - `components.disputes_list.features.refund_management` (boolean)
        Whether sending refunds is enabled. This is `true` by default.

  - `components.documents` (object)
    Configuration for the [documents](https://docs.stripe.com/connect/supported-embedded-components/documents/.md) embedded component.

    - `components.documents.enabled` (boolean)
      Whether the embedded component is enabled.

    - `components.documents.features` (object)
      An empty list, because this embedded component has no features.

  - `components.financial_account` (object)
    Configuration for the [financial account](https://docs.stripe.com/connect/supported-embedded-components/financial-account/.md) embedded component.

    - `components.financial_account.enabled` (boolean)
      Whether the embedded component is enabled.

    - `components.financial_account.features` (object)
      The list of features enabled in the embedded component.

      - `components.financial_account.features.disable_stripe_user_authentication` (boolean)
        Whether Stripe user authentication is disabled. This value can only be `true` for accounts where `controller.requirement_collection` is `application` for the account. The default value is the opposite of the `external_account_collection` value. For example, if you don’t set `external_account_collection`, it defaults to `true` and `disable_stripe_user_authentication` defaults to `false`.

      - `components.financial_account.features.external_account_collection` (boolean)
        Whether external account collection is enabled. This feature can only be `false` for accounts where you’re responsible for collecting updated information when requirements are due or change, like Custom accounts. The default value for this feature is `true`.

      - `components.financial_account.features.send_money` (boolean)
        Whether to allow sending money.

      - `components.financial_account.features.transfer_balance` (boolean)
        Whether to allow transferring balance.

  - `components.financial_account_transactions` (object)
    Configuration for the [financial account transactions](https://docs.stripe.com/connect/supported-embedded-components/financial-account-transactions/.md) embedded component.

    - `components.financial_account_transactions.enabled` (boolean)
      Whether the embedded component is enabled.

    - `components.financial_account_transactions.features` (object)
      The list of features enabled in the embedded component.

      - `components.financial_account_transactions.features.card_spend_dispute_management` (boolean)
        Whether to allow card spend dispute management features.

  - `components.instant_payouts_promotion` (object)
    Configuration for the [instant payouts promotion](https://docs.stripe.com/connect/supported-embedded-components/instant-payouts-promotion/.md) embedded component.

    - `components.instant_payouts_promotion.enabled` (boolean)
      Whether the embedded component is enabled.

    - `components.instant_payouts_promotion.features` (object)
      The list of features enabled in the embedded component.

      - `components.instant_payouts_promotion.features.disable_stripe_user_authentication` (boolean)
        Whether Stripe user authentication is disabled. This value can only be `true` for accounts where `controller.requirement_collection` is `application` for the account. The default value is the opposite of the `external_account_collection` value. For example, if you don’t set `external_account_collection`, it defaults to `true` and `disable_stripe_user_authentication` defaults to `false`.

      - `components.instant_payouts_promotion.features.external_account_collection` (boolean)
        Whether external account collection is enabled. This feature can only be `false` for accounts where you’re responsible for collecting updated information when requirements are due or change, like Custom accounts. The default value for this feature is `true`.

      - `components.instant_payouts_promotion.features.instant_payouts` (boolean)
        Whether to allow creation of instant payouts. Defaults to `true` when `controller.losses.payments` is set to `stripe` for the account, otherwise `false`.

  - `components.issuing_card` (object)
    Configuration for the [issuing card](https://docs.stripe.com/connect/supported-embedded-components/issuing-card/.md) embedded component.

    - `components.issuing_card.enabled` (boolean)
      Whether the embedded component is enabled.

    - `components.issuing_card.features` (object)
      The list of features enabled in the embedded component.

      - `components.issuing_card.features.card_management` (boolean)
        Whether to allow card management features.

      - `components.issuing_card.features.card_spend_dispute_management` (boolean)
        Whether to allow card spend dispute management features.

      - `components.issuing_card.features.cardholder_management` (boolean)
        Whether to allow cardholder management features.

      - `components.issuing_card.features.spend_control_management` (boolean)
        Whether to allow spend control management features.

  - `components.issuing_cards_list` (object)
    Configuration for the [issuing cards list](https://docs.stripe.com/connect/supported-embedded-components/issuing-cards-list/.md) embedded component.

    - `components.issuing_cards_list.enabled` (boolean)
      Whether the embedded component is enabled.

    - `components.issuing_cards_list.features` (object)
      The list of features enabled in the embedded component.

      - `components.issuing_cards_list.features.card_management` (boolean)
        Whether to allow card management features.

      - `components.issuing_cards_list.features.card_spend_dispute_management` (boolean)
        Whether to allow card spend dispute management features.

      - `components.issuing_cards_list.features.cardholder_management` (boolean)
        Whether to allow cardholder management features.

      - `components.issuing_cards_list.features.disable_stripe_user_authentication` (boolean)
        Whether Stripe user authentication is disabled. This value can only be `true` for accounts where `controller.requirement_collection` is `application` for the account. The default value is the opposite of the `external_account_collection` value. For example, if you don’t set `external_account_collection`, it defaults to `true` and `disable_stripe_user_authentication` defaults to `false`.

      - `components.issuing_cards_list.features.spend_control_management` (boolean)
        Whether to allow spend control management features.

  - `components.notification_banner` (object)
    Configuration for the [notification banner](https://docs.stripe.com/connect/supported-embedded-components/notification-banner/.md) embedded component.

    - `components.notification_banner.enabled` (boolean)
      Whether the embedded component is enabled.

    - `components.notification_banner.features` (object)
      The list of features enabled in the embedded component.

      - `components.notification_banner.features.disable_stripe_user_authentication` (boolean)
        Whether Stripe user authentication is disabled. This value can only be `true` for accounts where `controller.requirement_collection` is `application` for the account. The default value is the opposite of the `external_account_collection` value. For example, if you don’t set `external_account_collection`, it defaults to `true` and `disable_stripe_user_authentication` defaults to `false`.

      - `components.notification_banner.features.external_account_collection` (boolean)
        Whether external account collection is enabled. This feature can only be `false` for accounts where you’re responsible for collecting updated information when requirements are due or change, like Custom accounts. The default value for this feature is `true`.

  - `components.payment_details` (object)
    Configuration for the [payment details](https://docs.stripe.com/connect/supported-embedded-components/payment-details/.md) embedded component.

    - `components.payment_details.enabled` (boolean)
      Whether the embedded component is enabled.

    - `components.payment_details.features` (object)
      The list of features enabled in the embedded component.

      - `components.payment_details.features.capture_payments` (boolean)
        Whether to allow capturing and cancelling payment intents. This is `true` by default.

      - `components.payment_details.features.destination_on_behalf_of_charge_management` (boolean)
        Whether connected accounts can manage destination charges that are created on behalf of them. This is `false` by default.

      - `components.payment_details.features.dispute_management` (boolean)
        Whether responding to disputes is enabled, including submitting evidence and accepting disputes. This is `true` by default.

      - `components.payment_details.features.refund_management` (boolean)
        Whether sending refunds is enabled. This is `true` by default.

  - `components.payment_disputes` (object)
    Configuration for the [payment disputes](https://docs.stripe.com/connect/supported-embedded-components/payment-disputes/.md) embedded component.

    - `components.payment_disputes.enabled` (boolean)
      Whether the embedded component is enabled.

    - `components.payment_disputes.features` (object)
      The list of features enabled in the embedded component.

      - `components.payment_disputes.features.destination_on_behalf_of_charge_management` (boolean)
        Whether connected accounts can manage destination charges that are created on behalf of them. This is `false` by default.

      - `components.payment_disputes.features.dispute_management` (boolean)
        Whether responding to disputes is enabled, including submitting evidence and accepting disputes. This is `true` by default.

      - `components.payment_disputes.features.refund_management` (boolean)
        Whether sending refunds is enabled. This is `true` by default.

  - `components.payments` (object)
    Configuration for the [payments](https://docs.stripe.com/connect/supported-embedded-components/payments/.md) embedded component.

    - `components.payments.enabled` (boolean)
      Whether the embedded component is enabled.

    - `components.payments.features` (object)
      The list of features enabled in the embedded component.

      - `components.payments.features.capture_payments` (boolean)
        Whether to allow capturing and cancelling payment intents. This is `true` by default.

      - `components.payments.features.destination_on_behalf_of_charge_management` (boolean)
        Whether connected accounts can manage destination charges that are created on behalf of them. This is `false` by default.

      - `components.payments.features.dispute_management` (boolean)
        Whether responding to disputes is enabled, including submitting evidence and accepting disputes. This is `true` by default.

      - `components.payments.features.refund_management` (boolean)
        Whether sending refunds is enabled. This is `true` by default.

  - `components.payout_details` (object)
    Configuration for the [payout details](https://docs.stripe.com/connect/supported-embedded-components/payout-details/.md) embedded component.

    - `components.payout_details.enabled` (boolean)
      Whether the embedded component is enabled.

    - `components.payout_details.features` (object)
      An empty list, because this embedded component has no features.

  - `components.payout_reconciliation_report` (object)
    Configuration for the [payout reconciliation report](https://docs.stripe.com/connect/supported-embedded-components/financial-reports.md#payout-reconciliation-report) embedded component.

    - `components.payout_reconciliation_report.enabled` (boolean)
      Whether the embedded component is enabled.

    - `components.payout_reconciliation_report.features` (object)
      An empty list, because this embedded component has no features.

  - `components.payouts` (object)
    Configuration for the [payouts](https://docs.stripe.com/connect/supported-embedded-components/payouts/.md) embedded component.

    - `components.payouts.enabled` (boolean)
      Whether the embedded component is enabled.

    - `components.payouts.features` (object)
      The list of features enabled in the embedded component.

      - `components.payouts.features.disable_stripe_user_authentication` (boolean)
        Whether Stripe user authentication is disabled. This value can only be `true` for accounts where `controller.requirement_collection` is `application` for the account. The default value is the opposite of the `external_account_collection` value. For example, if you don’t set `external_account_collection`, it defaults to `true` and `disable_stripe_user_authentication` defaults to `false`.

      - `components.payouts.features.edit_payout_schedule` (boolean)
        Whether to allow payout schedule to be changed.  Defaults to `true` when `controller.losses.payments` is set to `stripe` for the account, otherwise `false`.

      - `components.payouts.features.external_account_collection` (boolean)
        Whether external account collection is enabled. This feature can only be `false` for accounts where you’re responsible for collecting updated information when requirements are due or change, like Custom accounts. The default value for this feature is `true`.

      - `components.payouts.features.instant_payouts` (boolean)
        Whether to allow creation of instant payouts. Defaults to `true` when `controller.losses.payments` is set to `stripe` for the account, otherwise `false`.

      - `components.payouts.features.standard_payouts` (boolean)
        Whether to allow creation of standard payouts.  Defaults to `true` when `controller.losses.payments` is set to `stripe` for the account, otherwise `false`.

  - `components.payouts_list` (object)
    Configuration for the [payouts list](https://docs.stripe.com/connect/supported-embedded-components/payouts-list/.md) embedded component.

    - `components.payouts_list.enabled` (boolean)
      Whether the embedded component is enabled.

    - `components.payouts_list.features` (object)
      An empty list, because this embedded component has no features.

  - `components.tax_registrations` (object)
    Configuration for the [tax registrations](https://docs.stripe.com/connect/supported-embedded-components/tax-registrations/.md) embedded component.

    - `components.tax_registrations.enabled` (boolean)
      Whether the embedded component is enabled.

    - `components.tax_registrations.features` (object)
      An empty list, because this embedded component has no features.

  - `components.tax_settings` (object)
    Configuration for the [tax settings](https://docs.stripe.com/connect/supported-embedded-components/tax-settings/.md) embedded component.

    - `components.tax_settings.enabled` (boolean)
      Whether the embedded component is enabled.

    - `components.tax_settings.features` (object)
      An empty list, because this embedded component has no features.

- `expires_at` (timestamp)
  The timestamp at which this AccountSession will expire.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

### The Account Session object

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
    }
  }
}
```