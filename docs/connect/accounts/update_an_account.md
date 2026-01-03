# Update an account

Updates a [connected account](https://docs.stripe.com/connect/accounts.md) by setting the values of the parameters passed. Any parameters not provided are left unchanged.

For accounts where [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `application`, which includes Custom accounts, you can update any information on the account.

For accounts where [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `stripe`, which includes Standard and Express accounts, you can update all information until you create an [Account Link](https://docs.stripe.com/api/account_links.md) or [Account Session](https://docs.stripe.com/api/account_sessions.md) to start Connect onboarding, after which some properties can no longer be updated.

To update your own account, use the [Dashboard](https://dashboard.stripe.com/settings/account). Refer to our [Connect](https://docs.stripe.com/docs/connect/updating-accounts.md) documentation to learn more about updating accounts.

## Returns

Returns an [`Account`](https://docs.stripe.com/api/accounts/update.md#account_object) object if the call succeeds. If the account ID does not exist or another issue occurs, this call raises [an error](https://docs.stripe.com/api/accounts/update.md#errors). Some validations will not raise an error but will instead populate the [`requirements.errors`](https://docs.stripe.com/api/accounts/update.md#account_object-requirements-errors) array.

## Parameters

- `account_token` (string, optional)
  An [account token](https://docs.stripe.com/api/accounts/update.md#create_account_token), used to securely provide details to the account.

- `business_profile` (object, optional)
  Business information about the account.

  - `business_profile.annual_revenue` (object, optional)
    The applicant’s gross annual revenue for its preceding fiscal year.

    - `business_profile.annual_revenue.amount` (integer, required)
      A non-negative integer representing the amount in the [smallest currency unit](https://docs.stripe.com/currencies.md#zero-decimal).

    - `business_profile.annual_revenue.currency` (enum, required)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

    - `business_profile.annual_revenue.fiscal_year_end` (string, required)
      The close-out date of the preceding fiscal year in ISO 8601 format. E.g. 2023-12-31 for the 31st of December, 2023.

  - `business_profile.estimated_worker_count` (integer, optional)
    An estimated upper bound of employees, contractors, vendors, etc. currently working for the business.

  - `business_profile.mcc` (string, optional)
    [The merchant category code for the account](https://docs.stripe.com/connect/setting-mcc.md). MCCs are used to classify businesses based on the goods or services they provide.

    The maximum length is 4 characters.

  - `business_profile.minority_owned_business_designation` (array of enums, optional)
    Whether the business is a minority-owned, women-owned, and/or LGBTQI+ -owned business.
Possible enum values:
    - `lgbtqi_owned_business`
      This business is owned by LGBTQI+ individual(s).

    - `minority_owned_business`
      This is a minority owned business. Minority means Hispanic or Latino, American Indian or Alaska Native, Asian, Black or African American, or Native Hawaiian or Other Pacific Islander. A multi-racial or multi-ethnic individual is a minority for this purpose.

    - `none_of_these_apply`
      None of these apply.

    - `prefer_not_to_answer`
      Prefer not to answer.

    - `women_owned_business`
      This business is owned by women.

  - `business_profile.monthly_estimated_revenue` (object, optional)
    An estimate of the monthly revenue of the business. Only accepted for accounts in Brazil and India.

    - `business_profile.monthly_estimated_revenue.amount` (integer, required)
      A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies.md#zero-decimal).

    - `business_profile.monthly_estimated_revenue.currency` (enum, required)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `business_profile.name` (string, optional)
    The customer-facing business name.

  - `business_profile.product_description` (string, optional)
    Internal-only description of the product sold by, or service provided by, the business. Used by Stripe for risk and underwriting purposes.

  - `business_profile.support_address` (object, optional)
    A publicly available mailing address for sending support issues to.

    - `business_profile.support_address.city` (string, optional)
      City, district, suburb, town, or village.

      The maximum length is 100 characters.

    - `business_profile.support_address.country` (string, optional)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `business_profile.support_address.line1` (string, optional)
      Address line 1, such as the street, PO Box, or company name.

      The maximum length is 200 characters.

    - `business_profile.support_address.line2` (string, optional)
      Address line 2, such as the apartment, suite, unit, or building.

      The maximum length is 200 characters.

    - `business_profile.support_address.postal_code` (string, optional)
      ZIP or postal code.

    - `business_profile.support_address.state` (string, optional)
      State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

  - `business_profile.support_email` (string, optional)
    A publicly available email address for sending support issues to.

    The maximum length is 800 characters.

  - `business_profile.support_phone` (string, optional)
    A publicly available phone number to call with support issues.

  - `business_profile.support_url` (string, optional)
    A publicly available website for handling support issues.

  - `business_profile.url` (string, optional)
    The business’s publicly available website.

- `business_type` (enum, optional)
  The business type. Once you create an [Account Link](https://docs.stripe.com/api/account_links.md) or [Account Session](https://docs.stripe.com/api/account_sessions.md), this property can only be updated for accounts where [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `application`, which includes Custom accounts.
Possible enum values:
  - `company`
  - `government_entity`
    US only

  - `individual`
  - `non_profit`

- `capabilities` (object, optional)
  Each key of the dictionary represents a capability, and each capability maps to its settings (for example, whether it has been requested or not). Each capability is inactive until you have provided its specific requirements and Stripe has verified them. An account might have some of its requested capabilities be active and some be inactive.

  Required when [account.controller.stripe_dashboard.type](https://docs.stripe.com/api/accounts/create.md#create_account-controller-dashboard-type) is `none`, which includes Custom accounts.

  - `capabilities.acss_debit_payments` (object, optional)
    The acss_debit_payments capability.

    - `capabilities.acss_debit_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.acss_debit_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.affirm_payments` (object, optional)
    The affirm_payments capability.

    - `capabilities.affirm_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.affirm_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.afterpay_clearpay_payments` (object, optional)
    The afterpay_clearpay_payments capability.

    - `capabilities.afterpay_clearpay_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.afterpay_clearpay_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.alma_payments` (object, optional)
    The alma_payments capability.

    - `capabilities.alma_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.alma_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.amazon_pay_payments` (object, optional)
    The amazon_pay_payments capability.

    - `capabilities.amazon_pay_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.amazon_pay_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.au_becs_debit_payments` (object, optional)
    The au_becs_debit_payments capability.

    - `capabilities.au_becs_debit_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.au_becs_debit_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.bacs_debit_payments` (object, optional)
    The bacs_debit_payments capability.

    - `capabilities.bacs_debit_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.bacs_debit_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.bancontact_payments` (object, optional)
    The bancontact_payments capability.

    - `capabilities.bancontact_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.bancontact_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.bank_transfer_payments` (object, optional)
    The bank_transfer_payments capability.

    - `capabilities.bank_transfer_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.bank_transfer_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.billie_payments` (object, optional)
    The billie_payments capability.

    - `capabilities.billie_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.billie_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.blik_payments` (object, optional)
    The blik_payments capability.

    - `capabilities.blik_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.blik_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.boleto_payments` (object, optional)
    The boleto_payments capability.

    - `capabilities.boleto_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.boleto_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.card_issuing` (object, optional)
    The card_issuing capability.

    - `capabilities.card_issuing.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.card_issuing.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.card_payments` (object, optional)
    The card_payments capability.

    - `capabilities.card_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.card_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.cartes_bancaires_payments` (object, optional)
    The cartes_bancaires_payments capability.

    - `capabilities.cartes_bancaires_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.cartes_bancaires_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.cashapp_payments` (object, optional)
    The cashapp_payments capability.

    - `capabilities.cashapp_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.cashapp_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.crypto_payments` (object, optional)
    The crypto_payments capability.

    - `capabilities.crypto_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.crypto_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.eps_payments` (object, optional)
    The eps_payments capability.

    - `capabilities.eps_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.eps_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.fpx_payments` (object, optional)
    The fpx_payments capability.

    - `capabilities.fpx_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.fpx_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.gb_bank_transfer_payments` (object, optional)
    The gb_bank_transfer_payments capability.

    - `capabilities.gb_bank_transfer_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.gb_bank_transfer_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.giropay_payments` (object, optional)
    The giropay_payments capability.

    - `capabilities.giropay_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.giropay_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.grabpay_payments` (object, optional)
    The grabpay_payments capability.

    - `capabilities.grabpay_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.grabpay_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.ideal_payments` (object, optional)
    The ideal_payments capability.

    - `capabilities.ideal_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.ideal_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.india_international_payments` (object, optional)
    The india_international_payments capability.

    - `capabilities.india_international_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.india_international_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.jcb_payments` (object, optional)
    The jcb_payments capability.

    - `capabilities.jcb_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.jcb_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.jp_bank_transfer_payments` (object, optional)
    The jp_bank_transfer_payments capability.

    - `capabilities.jp_bank_transfer_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.jp_bank_transfer_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.kakao_pay_payments` (object, optional)
    The kakao_pay_payments capability.

    - `capabilities.kakao_pay_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.kakao_pay_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.klarna_payments` (object, optional)
    The klarna_payments capability.

    - `capabilities.klarna_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.klarna_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.konbini_payments` (object, optional)
    The konbini_payments capability.

    - `capabilities.konbini_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.konbini_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.kr_card_payments` (object, optional)
    The kr_card_payments capability.

    - `capabilities.kr_card_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.kr_card_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.legacy_payments` (object, optional)
    The legacy_payments capability.

    - `capabilities.legacy_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.legacy_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.link_payments` (object, optional)
    The link_payments capability.

    - `capabilities.link_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.link_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.mb_way_payments` (object, optional)
    The mb_way_payments capability.

    - `capabilities.mb_way_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.mb_way_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.mobilepay_payments` (object, optional)
    The mobilepay_payments capability.

    - `capabilities.mobilepay_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.mobilepay_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.multibanco_payments` (object, optional)
    The multibanco_payments capability.

    - `capabilities.multibanco_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.multibanco_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.mx_bank_transfer_payments` (object, optional)
    The mx_bank_transfer_payments capability.

    - `capabilities.mx_bank_transfer_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.mx_bank_transfer_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.naver_pay_payments` (object, optional)
    The naver_pay_payments capability.

    - `capabilities.naver_pay_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.naver_pay_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.nz_bank_account_becs_debit_payments` (object, optional)
    The nz_bank_account_becs_debit_payments capability.

    - `capabilities.nz_bank_account_becs_debit_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.nz_bank_account_becs_debit_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.oxxo_payments` (object, optional)
    The oxxo_payments capability.

    - `capabilities.oxxo_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.oxxo_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.p24_payments` (object, optional)
    The p24_payments capability.

    - `capabilities.p24_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.p24_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.pay_by_bank_payments` (object, optional)
    The pay_by_bank_payments capability.

    - `capabilities.pay_by_bank_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.pay_by_bank_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.payco_payments` (object, optional)
    The payco_payments capability.

    - `capabilities.payco_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.payco_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.paynow_payments` (object, optional)
    The paynow_payments capability.

    - `capabilities.paynow_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.paynow_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.payto_payments` (object, optional)
    The payto_payments capability.

    - `capabilities.payto_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.payto_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.pix_payments` (object, optional)
    The pix_payments capability.

    - `capabilities.pix_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.pix_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.promptpay_payments` (object, optional)
    The promptpay_payments capability.

    - `capabilities.promptpay_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.promptpay_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.revolut_pay_payments` (object, optional)
    The revolut_pay_payments capability.

    - `capabilities.revolut_pay_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.revolut_pay_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.samsung_pay_payments` (object, optional)
    The samsung_pay_payments capability.

    - `capabilities.samsung_pay_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.samsung_pay_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.satispay_payments` (object, optional)
    The satispay_payments capability.

    - `capabilities.satispay_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.satispay_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.sepa_bank_transfer_payments` (object, optional)
    The sepa_bank_transfer_payments capability.

    - `capabilities.sepa_bank_transfer_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.sepa_bank_transfer_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.sepa_debit_payments` (object, optional)
    The sepa_debit_payments capability.

    - `capabilities.sepa_debit_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.sepa_debit_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.sofort_payments` (object, optional)
    The sofort_payments capability.

    - `capabilities.sofort_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.sofort_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.swish_payments` (object, optional)
    The swish_payments capability.

    - `capabilities.swish_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.swish_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.tax_reporting_us_1099_k` (object, optional)
    The tax_reporting_us_1099_k capability.

    - `capabilities.tax_reporting_us_1099_k.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.tax_reporting_us_1099_k.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.tax_reporting_us_1099_misc` (object, optional)
    The tax_reporting_us_1099_misc capability.

    - `capabilities.tax_reporting_us_1099_misc.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.tax_reporting_us_1099_misc.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.transfers` (object, optional)
    The transfers capability.

    - `capabilities.transfers.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.transfers.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.twint_payments` (object, optional)
    The twint_payments capability.

    - `capabilities.twint_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.twint_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.us_bank_account_ach_payments` (object, optional)
    The us_bank_account_ach_payments capability.

    - `capabilities.us_bank_account_ach_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.us_bank_account_ach_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.us_bank_transfer_payments` (object, optional)
    The us_bank_transfer_payments capability.

    - `capabilities.us_bank_transfer_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.us_bank_transfer_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

  - `capabilities.zip_payments` (object, optional)
    The zip_payments capability.

    - `capabilities.zip_payments.experimental` (boolean, optional)
      Passing true assigns the experimental onboarding policy to the capability.

    - `capabilities.zip_payments.requested` (boolean, optional)
      Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.

- `company` (object, optional)
  Information about the company or business. This field is available for any `business_type`. Once you create an [Account Link](https://docs.stripe.com/api/account_links.md) or [Account Session](https://docs.stripe.com/api/account_sessions.md), this property can only be updated for accounts where [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `application`, which includes Custom accounts.

  - `company.address` (object, optional)
    The company’s primary address.

    - `company.address.city` (string, optional)
      City, district, suburb, town, or village.

      The maximum length is 100 characters.

    - `company.address.country` (string, optional)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `company.address.line1` (string, optional)
      Address line 1, such as the street, PO Box, or company name.

      The maximum length is 200 characters.

    - `company.address.line2` (string, optional)
      Address line 2, such as the apartment, suite, unit, or building.

      The maximum length is 200 characters.

    - `company.address.postal_code` (string, optional)
      ZIP or postal code.

    - `company.address.state` (string, optional)
      State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

  - `company.address_kana` (object, optional)
    The Kana variation of the company’s primary address (Japan only).

    - `company.address_kana.city` (string, optional)
      City or ward.

    - `company.address_kana.country` (string, optional)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `company.address_kana.line1` (string, optional)
      Block or building number.

    - `company.address_kana.line2` (string, optional)
      Building details.

    - `company.address_kana.postal_code` (string, optional)
      Postal code.

    - `company.address_kana.state` (string, optional)
      Prefecture.

    - `company.address_kana.town` (string, optional)
      Town or cho-me.

  - `company.address_kanji` (object, optional)
    The Kanji variation of the company’s primary address (Japan only).

    - `company.address_kanji.city` (string, optional)
      City or ward.

    - `company.address_kanji.country` (string, optional)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `company.address_kanji.line1` (string, optional)
      Block or building number.

    - `company.address_kanji.line2` (string, optional)
      Building details.

    - `company.address_kanji.postal_code` (string, optional)
      Postal code.

    - `company.address_kanji.state` (string, optional)
      Prefecture.

    - `company.address_kanji.town` (string, optional)
      Town or cho-me.

  - `company.directors_provided` (boolean, optional)
    Whether the company’s directors have been provided. Set this Boolean to `true` after creating all the company’s directors with [the Persons API](https://docs.stripe.com/api/persons.md) for accounts with a `relationship.director` requirement. This value is not automatically set to `true` after creating directors, so it needs to be updated to indicate all directors have been provided.

  - `company.directorship_declaration` (object, optional)
    This hash is used to attest that the directors information provided to Stripe is both current and correct.

    - `company.directorship_declaration.date` (timestamp, optional)
      The Unix timestamp marking when the directorship declaration attestation was made.

    - `company.directorship_declaration.ip` (string, optional)
      The IP address from which the directorship declaration attestation was made.

    - `company.directorship_declaration.user_agent` (string, optional)
      The user agent of the browser from which the directorship declaration attestation was made.

  - `company.executives_provided` (boolean, optional)
    Whether the company’s executives have been provided. Set this Boolean to `true` after creating all the company’s executives with [the Persons API](https://docs.stripe.com/api/persons.md) for accounts with a `relationship.executive` requirement.

  - `company.export_license_id` (string, optional)
    The export license ID number of the company, also referred as Import Export Code (India only).

  - `company.export_purpose_code` (string, optional)
    The purpose code to use for export transactions (India only).

  - `company.name` (string, optional)
    The company’s legal name.

    The maximum length is 100 characters.

  - `company.name_kana` (string, optional)
    The Kana variation of the company’s legal name (Japan only).

    The maximum length is 100 characters.

  - `company.name_kanji` (string, optional)
    The Kanji variation of the company’s legal name (Japan only).

    The maximum length is 100 characters.

  - `company.owners_provided` (boolean, optional)
    Whether the company’s owners have been provided. Set this Boolean to `true` after creating all the company’s owners with [the Persons API](https://docs.stripe.com/api/persons.md) for accounts with a `relationship.owner` requirement.

  - `company.ownership_declaration` (object, optional)
    This hash is used to attest that the beneficial owner information provided to Stripe is both current and correct.

    - `company.ownership_declaration.date` (timestamp, optional)
      The Unix timestamp marking when the beneficial owner attestation was made.

    - `company.ownership_declaration.ip` (string, optional)
      The IP address from which the beneficial owner attestation was made.

    - `company.ownership_declaration.user_agent` (string, optional)
      The user agent of the browser from which the beneficial owner attestation was made.

  - `company.ownership_exemption_reason` (enum, optional)
    This value is used to determine if a business is exempt from providing ultimate beneficial owners. See [this support article](https://support.stripe.com/questions/exemption-from-providing-ownership-details) and [changelog](https://docs.stripe.com/changelog/acacia/2025-01-27/ownership-exemption-reason-accounts-api.md) for more details.

  - `company.phone` (string, optional)
    The company’s phone number (used for verification).

  - `company.registration_number` (string, optional)
    The identification number given to a company when it is registered or incorporated, if distinct from the identification number used for filing taxes. (Examples are the CIN for companies and LLP IN for partnerships in India, and the Company Registration Number in Hong Kong).

  - `company.representative_declaration` (object, optional)
    This hash is used to attest that the representative is authorized to act as the representative of their legal entity.

    - `company.representative_declaration.date` (timestamp, optional)
      The Unix timestamp marking when the representative declaration attestation was made.

    - `company.representative_declaration.ip` (string, optional)
      The IP address from which the representative declaration attestation was made.

    - `company.representative_declaration.user_agent` (string, optional)
      The user agent of the browser from which the representative declaration attestation was made.

  - `company.structure` (enum, optional)
    The category identifying the legal structure of the company or legal entity. See [Business structure](https://docs.stripe.com/connect/identity-verification.md#business-structure) for more details. Pass an empty string to unset this value.

  - `company.tax_id` (string, optional)
    The business ID number of the company, as appropriate for the company’s country. (Examples are an Employer ID Number in the U.S., a Business Number in Canada, or a Company Number in the UK.)

  - `company.tax_id_registrar` (string, optional)
    The jurisdiction in which the `tax_id` is registered (Germany-based companies only).

  - `company.vat_id` (string, optional)
    The VAT number of the company.

  - `company.verification` (object, optional)
    Information on the verification state of the company.

    - `company.verification.document` (object, optional)
      A document verifying the business.

      - `company.verification.document.back` (string, optional)
        The back of a document returned by a [file upload](https://docs.stripe.com/api/accounts/update.md#create_file) with a `purpose` value of `additional_verification`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

        The maximum length is 500 characters.

      - `company.verification.document.front` (string, optional)
        The front of a document returned by a [file upload](https://docs.stripe.com/api/accounts/update.md#create_file) with a `purpose` value of `additional_verification`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

        The maximum length is 500 characters.

- `default_currency` (enum, optional)
  Three-letter ISO currency code representing the default currency for the account. This must be a currency that [Stripe supports in the account’s country](https://docs.stripe.com/payouts.md).

- `documents` (object, optional)
  Documents that may be submitted to satisfy various informational requests.

  - `documents.bank_account_ownership_verification` (object, optional)
    One or more documents that support the [Bank account ownership verification](https://support.stripe.com/questions/bank-account-ownership-verification) requirement. Must be a document associated with the account’s primary active bank account that displays the last 4 digits of the account number, either a statement or a check.

    - `documents.bank_account_ownership_verification.files` (array of strings, optional)
      One or more document ids returned by a [file upload](https://docs.stripe.com/api/accounts/update.md#create_file) with a `purpose` value of `account_requirement`.

  - `documents.company_license` (object, optional)
    One or more documents that demonstrate proof of a company’s license to operate.

    - `documents.company_license.files` (array of strings, optional)
      One or more document ids returned by a [file upload](https://docs.stripe.com/api/accounts/update.md#create_file) with a `purpose` value of `account_requirement`.

  - `documents.company_memorandum_of_association` (object, optional)
    One or more documents showing the company’s Memorandum of Association.

    - `documents.company_memorandum_of_association.files` (array of strings, optional)
      One or more document ids returned by a [file upload](https://docs.stripe.com/api/accounts/update.md#create_file) with a `purpose` value of `account_requirement`.

  - `documents.company_ministerial_decree` (object, optional)
    (Certain countries only) One or more documents showing the ministerial decree legalizing the company’s establishment.

    - `documents.company_ministerial_decree.files` (array of strings, optional)
      One or more document ids returned by a [file upload](https://docs.stripe.com/api/accounts/update.md#create_file) with a `purpose` value of `account_requirement`.

  - `documents.company_registration_verification` (object, optional)
    One or more documents that demonstrate proof of a company’s registration with the appropriate local authorities.

    - `documents.company_registration_verification.files` (array of strings, optional)
      One or more document ids returned by a [file upload](https://docs.stripe.com/api/accounts/update.md#create_file) with a `purpose` value of `account_requirement`.

  - `documents.company_tax_id_verification` (object, optional)
    One or more documents that demonstrate proof of a company’s tax ID.

    - `documents.company_tax_id_verification.files` (array of strings, optional)
      One or more document ids returned by a [file upload](https://docs.stripe.com/api/accounts/update.md#create_file) with a `purpose` value of `account_requirement`.

  - `documents.proof_of_address` (object, optional)
    One or more documents that demonstrate proof of address.

    - `documents.proof_of_address.files` (array of strings, optional)
      One or more document ids returned by a [file upload](https://docs.stripe.com/api/accounts/update.md#create_file) with a `purpose` value of `account_requirement`.

  - `documents.proof_of_registration` (object, optional)
    One or more documents showing the company’s proof of registration with the national business registry.

    - `documents.proof_of_registration.files` (array of strings, optional)
      One or more document ids returned by a [file upload](https://docs.stripe.com/api/accounts/update.md#create_file) with a `purpose` value of `account_requirement`.

    - `documents.proof_of_registration.signer` (object, optional)
      Information regarding the person signing the document if applicable.

      - `documents.proof_of_registration.signer.person` (string, optional)
        The token of the person signing the document, if applicable.

  - `documents.proof_of_ultimate_beneficial_ownership` (object, optional)
    One or more documents that demonstrate proof of ultimate beneficial ownership.

    - `documents.proof_of_ultimate_beneficial_ownership.files` (array of strings, optional)
      One or more document ids returned by a [file upload](https://docs.stripe.com/api/accounts/update.md#create_file) with a `purpose` value of `account_requirement`.

    - `documents.proof_of_ultimate_beneficial_ownership.signer` (object, optional)
      Information regarding the person signing the document if applicable.

      - `documents.proof_of_ultimate_beneficial_ownership.signer.person` (string, optional)
        The token of the person signing the document, if applicable.

- `email` (string, optional)
  The email address of the account holder. This is only to make the account easier to identify to you. If [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `application`, which includes Custom accounts, Stripe doesn’t email the account without your consent.

  The maximum length is 800 characters.

- `external_account` (string, optional)
  A card or bank account to attach to the account for receiving [payouts](https://docs.stripe.com/connect/bank-debit-card-payouts.md) (you won’t be able to use it for top-ups). You can provide either a token, like the ones returned by [Stripe.js](https://docs.stripe.com/js.md), or a dictionary, as documented in the `external_account` parameter for [bank account](https://docs.stripe.com/api.md#account_create_bank_account) creation. By default, providing an external account sets it as the new default external account for its currency, and deletes the old default if one exists. To add additional external accounts without replacing the existing default for the currency, use the [bank account](https://docs.stripe.com/api.md#account_create_bank_account) or [card creation](https://docs.stripe.com/api.md#account_create_card) APIs. After you create an [Account Link](https://docs.stripe.com/api/account_links.md) or [Account Session](https://docs.stripe.com/api/account_sessions.md), this property can only be updated for accounts where [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `application`, which includes Custom accounts.

- `groups` (object, optional)
  A hash of account group type to tokens. These are account groups this account should be added to.

  - `groups.payments_pricing` (string, optional)
    The group the account is in to determine their payments pricing, and null if the account is on customized pricing. [See the Platform pricing tool documentation](https://docs.stripe.com/docs/connect/platform-pricing-tools.md) for details.

- `individual` (object, optional)
  Information about the person represented by the account. This field is null unless `business_type` is set to `individual`. Once you create an [Account Link](https://docs.stripe.com/api/account_links.md) or [Account Session](https://docs.stripe.com/api/account_sessions.md), this property can only be updated for accounts where [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `application`, which includes Custom accounts.

  - `individual.address` (object, optional)
    The individual’s primary address.

    - `individual.address.city` (string, optional)
      City, district, suburb, town, or village.

      The maximum length is 100 characters.

    - `individual.address.country` (string, optional)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `individual.address.line1` (string, optional)
      Address line 1, such as the street, PO Box, or company name.

      The maximum length is 200 characters.

    - `individual.address.line2` (string, optional)
      Address line 2, such as the apartment, suite, unit, or building.

      The maximum length is 200 characters.

    - `individual.address.postal_code` (string, optional)
      ZIP or postal code.

    - `individual.address.state` (string, optional)
      State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

  - `individual.address_kana` (object, optional)
    The Kana variation of the individual’s primary address (Japan only).

    - `individual.address_kana.city` (string, optional)
      City or ward.

    - `individual.address_kana.country` (string, optional)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `individual.address_kana.line1` (string, optional)
      Block or building number.

    - `individual.address_kana.line2` (string, optional)
      Building details.

    - `individual.address_kana.postal_code` (string, optional)
      Postal code.

    - `individual.address_kana.state` (string, optional)
      Prefecture.

    - `individual.address_kana.town` (string, optional)
      Town or cho-me.

  - `individual.address_kanji` (object, optional)
    The Kanji variation of the individual’s primary address (Japan only).

    - `individual.address_kanji.city` (string, optional)
      City or ward.

    - `individual.address_kanji.country` (string, optional)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `individual.address_kanji.line1` (string, optional)
      Block or building number.

    - `individual.address_kanji.line2` (string, optional)
      Building details.

    - `individual.address_kanji.postal_code` (string, optional)
      Postal code.

    - `individual.address_kanji.state` (string, optional)
      Prefecture.

    - `individual.address_kanji.town` (string, optional)
      Town or cho-me.

  - `individual.dob` (object, optional)
    The individual’s date of birth.

    - `individual.dob.day` (integer, required)
      The day of birth, between 1 and 31.

    - `individual.dob.month` (integer, required)
      The month of birth, between 1 and 12.

    - `individual.dob.year` (integer, required)
      The four-digit year of birth.

  - `individual.email` (string, optional)
    The individual’s email address.

    The maximum length is 800 characters.

  - `individual.first_name` (string, optional)
    The individual’s first name.

    The maximum length is 100 characters.

  - `individual.first_name_kana` (string, optional)
    The Kana variation of the individual’s first name (Japan only).

  - `individual.first_name_kanji` (string, optional)
    The Kanji variation of the individual’s first name (Japan only).

  - `individual.full_name_aliases` (array of strings, optional)
    A list of alternate names or aliases that the individual is known by.

  - `individual.gender` (enum, optional)
    The individual’s gender

  - `individual.id_number` (string, optional)
    The government-issued ID number of the individual, as appropriate for the representative’s country. (Examples are a Social Security Number in the U.S., or a Social Insurance Number in Canada). Instead of the number itself, you can also provide a [PII token created with Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii).

  - `individual.id_number_secondary` (string, optional)
    The government-issued secondary ID number of the individual, as appropriate for the representative’s country, will be used for enhanced verification checks. In Thailand, this would be the laser code found on the back of an ID card. Instead of the number itself, you can also provide a [PII token created with Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii).

  - `individual.last_name` (string, optional)
    The individual’s last name.

    The maximum length is 100 characters.

  - `individual.last_name_kana` (string, optional)
    The Kana variation of the individual’s last name (Japan only).

  - `individual.last_name_kanji` (string, optional)
    The Kanji variation of the individual’s last name (Japan only).

  - `individual.maiden_name` (string, optional)
    The individual’s maiden name.

  - `individual.metadata` (object, optional)
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

  - `individual.phone` (string, optional)
    The individual’s phone number.

  - `individual.political_exposure` (enum, optional)
    Indicates if the person or any of their representatives, family members, or other closely related persons, declares that they hold or have held an important public job or function, in any jurisdiction.
Possible enum values:
    - `existing`
      The person has disclosed that they do have political exposure

    - `none`
      The person has disclosed that they have no political exposure

  - `individual.registered_address` (object, optional)
    The individual’s registered address.

    - `individual.registered_address.city` (string, optional)
      City, district, suburb, town, or village.

      The maximum length is 100 characters.

    - `individual.registered_address.country` (string, optional)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `individual.registered_address.line1` (string, optional)
      Address line 1, such as the street, PO Box, or company name.

      The maximum length is 200 characters.

    - `individual.registered_address.line2` (string, optional)
      Address line 2, such as the apartment, suite, unit, or building.

      The maximum length is 200 characters.

    - `individual.registered_address.postal_code` (string, optional)
      ZIP or postal code.

    - `individual.registered_address.state` (string, optional)
      State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

  - `individual.relationship` (object, optional)
    Describes the person’s relationship to the account.

    - `individual.relationship.director` (boolean, optional)
      Whether the person is a director of the account’s legal entity. Directors are typically members of the governing board of the company, or responsible for ensuring the company meets its regulatory obligations.

    - `individual.relationship.executive` (boolean, optional)
      Whether the person has significant responsibility to control, manage, or direct the organization.

    - `individual.relationship.owner` (boolean, optional)
      Whether the person is an owner of the account’s legal entity.

    - `individual.relationship.percent_ownership` (float, optional)
      The percent owned by the person of the account’s legal entity.

    - `individual.relationship.title` (string, optional)
      The person’s title (e.g., CEO, Support Engineer).

  - `individual.ssn_last_4` (string, optional)
    The last four digits of the individual’s Social Security Number (U.S. only).

  - `individual.verification` (object, optional)
    The individual’s verification document information.

    - `individual.verification.additional_document` (object, optional)
      A document showing address, either a passport, local ID card, or utility bill from a well-known utility company.

      - `individual.verification.additional_document.back` (string, optional)
        The back of an ID returned by a [file upload](https://docs.stripe.com/api/accounts/update.md#create_file) with a `purpose` value of `identity_document`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

        The maximum length is 500 characters.

      - `individual.verification.additional_document.front` (string, optional)
        The front of an ID returned by a [file upload](https://docs.stripe.com/api/accounts/update.md#create_file) with a `purpose` value of `identity_document`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

        The maximum length is 500 characters.

    - `individual.verification.document` (object, optional)
      An identifying document, either a passport or local ID card.

      - `individual.verification.document.back` (string, optional)
        The back of an ID returned by a [file upload](https://docs.stripe.com/api/accounts/update.md#create_file) with a `purpose` value of `identity_document`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

        The maximum length is 500 characters.

      - `individual.verification.document.front` (string, optional)
        The front of an ID returned by a [file upload](https://docs.stripe.com/api/accounts/update.md#create_file) with a `purpose` value of `identity_document`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

        The maximum length is 500 characters.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `settings` (object, optional)
  Options for customizing how the account functions within Stripe.

  - `settings.bacs_debit_payments` (object, optional)
    Settings specific to Bacs Direct Debit payments.

    - `settings.bacs_debit_payments.display_name` (string, optional)
      The Bacs Direct Debit Display Name for this account. For payments made with Bacs Direct Debit, this name appears on the mandate as the statement descriptor. Mobile banking apps display it as the name of the business. To use custom branding, set the Bacs Direct Debit Display Name during or right after creation. Custom branding incurs an additional monthly fee for the platform. If you don’t set the display name before requesting Bacs capability, it’s automatically set as “Stripe” and the account is onboarded to Stripe branding, which is free.

  - `settings.branding` (object, optional)
    Settings used to apply the account’s branding to email receipts, invoices, Checkout, and other products.

    - `settings.branding.icon` (string, optional)
      (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) An icon for the account. Must be square and at least 128px x 128px.

    - `settings.branding.logo` (string, optional)
      (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) A logo for the account that will be used in Checkout instead of the icon and without the account’s name next to it if provided. Must be at least 128px x 128px.

    - `settings.branding.primary_color` (string, optional)
      A CSS hex color value representing the primary branding color for this account.

    - `settings.branding.secondary_color` (string, optional)
      A CSS hex color value representing the secondary branding color for this account.

  - `settings.card_issuing` (object, optional)
    Settings specific to the account’s use of the Card Issuing product.

    - `settings.card_issuing.tos_acceptance` (object, optional)
      Details on the account’s acceptance of the [Stripe Issuing Terms and Disclosures](https://docs.stripe.com/issuing/connect/tos_acceptance.md).

      - `settings.card_issuing.tos_acceptance.date` (timestamp, required if IP or user_agent is provided)
        The Unix timestamp marking when the account representative accepted the service agreement.

      - `settings.card_issuing.tos_acceptance.ip` (string, required if date or user_agent is provided)
        The IP address from which the account representative accepted the service agreement.

      - `settings.card_issuing.tos_acceptance.user_agent` (string, optional)
        The user agent of the browser from which the account representative accepted the service agreement.

  - `settings.card_payments` (object, optional)
    Settings specific to card charging on the account.

    - `settings.card_payments.decline_on` (object, optional)
      Automatically declines certain charge types regardless of whether the card issuer accepted or declined the charge.

      - `settings.card_payments.decline_on.avs_failure` (boolean, optional)
        Whether Stripe automatically declines charges with an incorrect ZIP or postal code. This setting only applies when a ZIP or postal code is provided and they fail bank verification.

      - `settings.card_payments.decline_on.cvc_failure` (boolean, optional)
        Whether Stripe automatically declines charges with an incorrect CVC. This setting only applies when a CVC is provided and it fails bank verification.

  - `settings.invoices` (object, optional)
    Settings specific to the account’s use of Invoices.

    - `settings.invoices.default_account_tax_ids` (array of strings, optional)
      The list of default Account Tax IDs to automatically include on invoices. Account Tax IDs get added when an invoice is finalized.

    - `settings.invoices.hosted_payment_method_save` (enum, optional)
      Whether to save the payment method after a payment is completed for a one-time invoice or a subscription invoice when the customer already has a default payment method on the hosted invoice page.
Possible enum values:
      - `always`
        The payment method, if reusable, will be saved for one-time invoice payments.

      - `never`
        The payment method will not be saved for one-time invoice payments.

      - `offer`
        The payment method, if reusable, will be saved for one-time invoice payments if the customer chooses to save it.

  - `settings.payments` (object, optional)
    Settings that apply across payment methods for charging on the account.

    - `settings.payments.statement_descriptor` (string, optional)
      The default text that appears on statements for non-card charges outside of Japan. For card charges, if you don’t set a `statement_descriptor_prefix`, this text is also used as the statement descriptor prefix. In that case, if concatenating the statement descriptor suffix causes the combined statement descriptor to exceed 22 characters, we truncate the `statement_descriptor` text to limit the full descriptor to 22 characters. For more information about statement descriptors and their requirements, see the [account settings documentation](https://docs.stripe.com/get-started/account/statement-descriptors.md).

    - `settings.payments.statement_descriptor_kana` (string, optional)
      The Kana variation of `statement_descriptor` used for charges in Japan. Japanese statement descriptors have [special requirements](https://docs.stripe.com/get-started/account/statement-descriptors.md#set-japanese-statement-descriptors).

    - `settings.payments.statement_descriptor_kanji` (string, optional)
      The Kanji variation of `statement_descriptor` used for charges in Japan. Japanese statement descriptors have [special requirements](https://docs.stripe.com/get-started/account/statement-descriptors.md#set-japanese-statement-descriptors).

    - `settings.payments.statement_descriptor_prefix` (string, optional)
      Default text that appears on statements for card charges outside of Japan, prefixing any dynamic `statement_descriptor_suffix` specified on the charge. To maximize space for the dynamic part of the descriptor, keep this text short. If you don’t specify this value, `statement_descriptor` is used as the prefix. For more information about statement descriptors and their requirements, see the [account settings documentation](https://docs.stripe.com/get-started/account/statement-descriptors.md).

    - `settings.payments.statement_descriptor_prefix_kana` (string, optional)
      The Kana variation of `statement_descriptor_prefix` used for card charges in Japan. Japanese statement descriptors have [special requirements](https://docs.stripe.com/get-started/account/statement-descriptors.md#set-japanese-statement-descriptors).

    - `settings.payments.statement_descriptor_prefix_kanji` (string, optional)
      The Kanji variation of `statement_descriptor_prefix` used for card charges in Japan. Japanese statement descriptors have [special requirements](https://docs.stripe.com/get-started/account/statement-descriptors.md#set-japanese-statement-descriptors).

  - `settings.payouts` (object, optional)
    Settings specific to the account’s payouts.

    - `settings.payouts.debit_negative_balances` (boolean, optional)
      A Boolean indicating whether Stripe should try to reclaim negative balances from an attached bank account. For details, see [Understanding Connect Account Balances](https://docs.stripe.com/connect/account-balances.md).

    - `settings.payouts.schedule` (object, optional)
      Details on when funds from charges are available, and when they are paid out to an external account. For details, see our [Setting Bank and Debit Card Payouts](https://docs.stripe.com/connect/bank-transfers.md#payout-information) documentation.

      - `settings.payouts.schedule.delay_days` (string | integer, optional)
        The number of days charge funds are held before being paid out. May also be set to `minimum`, representing the lowest available value for the account country. Default is `minimum`. The `delay_days` parameter remains at the last configured value if `interval` is `manual`. [Learn more about controlling payout delay days](https://docs.stripe.com/connect/manage-payout-schedule.md).

      - `settings.payouts.schedule.interval` (string, optional)
        How frequently available funds are paid out. One of: `daily`, `manual`, `weekly`, or `monthly`. Default is `daily`.

      - `settings.payouts.schedule.monthly_anchor` (integer, optional)
        The day of the month when available funds are paid out, specified as a number between 1–31. Payouts nominally scheduled between the 29th and 31st of the month are instead sent on the last day of a shorter month. Required and applicable only if `interval` is `monthly`.

      - `settings.payouts.schedule.monthly_payout_days` (array of integers, optional)
        The days of the month when available funds are paid out, specified as an array of numbers between 1–31. Payouts nominally scheduled between the 29th and 31st of the month are instead sent on the last day of a shorter month. Required and applicable only if `interval` is `monthly` and `monthly_anchor` is not set.

      - `settings.payouts.schedule.weekly_anchor` (string, optional)
        The day of the week when available funds are paid out, specified as `monday`, `tuesday`, etc. Required and applicable only if `interval` is `weekly`.

      - `settings.payouts.schedule.weekly_payout_days` (array of enums, optional)
        The days of the week when available funds are paid out, specified as an array, e.g., [`monday`, `tuesday`]. Required and applicable only if `interval` is `weekly`.
Possible enum values:
        - `monday`
          Select Monday as one of the weekly payout days

        - `tuesday`
          Select Tuesday as one of the weekly payout days

        - `wednesday`
          Select Wednesday as one of the weekly payout days

        - `thursday`
          Select Thursday as one of the weekly payout days

        - `friday`
          Select Friday as one of the weekly payout days

    - `settings.payouts.statement_descriptor` (string, optional)
      The text that appears on the bank account statement for payouts. If not set, this defaults to the platform’s bank descriptor as set in the Dashboard.

- `tos_acceptance` (object, optional)
  Details on the account’s acceptance of the [Stripe Services Agreement](https://docs.stripe.com/connect/updating-accounts.md#tos-acceptance). This property can only be updated for accounts where [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `application`, which includes Custom accounts. This property defaults to a `full` service agreement when empty.

  - `tos_acceptance.date` (timestamp, required if IP or user_agent is provided)
    The Unix timestamp marking when the account representative accepted their service agreement.

  - `tos_acceptance.ip` (string, required if date or user_agent is provided)
    The IP address from which the account representative accepted their service agreement.

  - `tos_acceptance.service_agreement` (string, optional)
    The user’s service agreement type.

  - `tos_acceptance.user_agent` (string, optional)
    The user agent of the browser from which the account representative accepted their service agreement.

```curl
curl https://api.stripe.com/v1/accounts/acct_1Nv0FGQ9RKHgCVdK \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
```

```cli
stripe accounts update acct_1Nv0FGQ9RKHgCVdK \
  -d "metadata[order_id]"=6735
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

account = client.v1.accounts.update(
  'acct_1Nv0FGQ9RKHgCVdK',
  {metadata: {order_id: '6735'}},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

account = client.v1.accounts.update(
  "acct_1Nv0FGQ9RKHgCVdK",
  {"metadata": {"order_id": "6735"}},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$account = $stripe->accounts->update(
  'acct_1Nv0FGQ9RKHgCVdK',
  ['metadata' => ['order_id' => '6735']]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AccountUpdateParams params =
  AccountUpdateParams.builder().putMetadata("order_id", "6735").build();

Account account = client.v1().accounts().update("acct_1Nv0FGQ9RKHgCVdK", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const account = await stripe.accounts.update(
  'acct_1Nv0FGQ9RKHgCVdK',
  {
    metadata: {
      order_id: '6735',
    },
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.AccountUpdateParams{}
params.AddMetadata("order_id", "6735")
result, err := sc.V1Accounts.Update(context.TODO(), "acct_1Nv0FGQ9RKHgCVdK", params)
```

```dotnet
var options = new AccountUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Accounts;
Account account = service.Update("acct_1Nv0FGQ9RKHgCVdK", options);
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
  "metadata": {
    "order_id": "6735"
  },
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
```