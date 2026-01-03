# The Account object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `business_profile` (object, nullable)
  Business information about the account.

  - `business_profile.annual_revenue` (object, nullable)
    The applicant’s gross annual revenue for its preceding fiscal year.

    - `business_profile.annual_revenue.amount` (integer, nullable)
      A non-negative integer representing the amount in the [smallest currency unit](https://docs.stripe.com/currencies.md#zero-decimal).

    - `business_profile.annual_revenue.currency` (enum, nullable)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

    - `business_profile.annual_revenue.fiscal_year_end` (string, nullable)
      The close-out date of the preceding fiscal year in ISO 8601 format. E.g. 2023-12-31 for the 31st of December, 2023.

  - `business_profile.estimated_worker_count` (integer, nullable)
    An estimated upper bound of employees, contractors, vendors, etc. currently working for the business.

  - `business_profile.mcc` (string, nullable)
    [The merchant category code for the account](https://docs.stripe.com/connect/setting-mcc.md). MCCs are used to classify businesses based on the goods or services they provide.

  - `business_profile.minority_owned_business_designation` (array of enums, nullable)
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

  - `business_profile.monthly_estimated_revenue` (object, nullable)
    An estimate of the monthly revenue of the business. Only accepted for accounts in Brazil and India.

    - `business_profile.monthly_estimated_revenue.amount` (integer)
      A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies.md#zero-decimal).

    - `business_profile.monthly_estimated_revenue.currency` (enum)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `business_profile.name` (string, nullable)
    The customer-facing business name.

  - `business_profile.product_description` (string, nullable)
    Internal-only description of the product sold or service provided by the business. It’s used by Stripe for risk and underwriting purposes.

  - `business_profile.support_address` (object, nullable)
    A publicly available mailing address for sending support issues to.

    - `business_profile.support_address.city` (string, nullable)
      City, district, suburb, town, or village.

    - `business_profile.support_address.country` (string, nullable)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `business_profile.support_address.line1` (string, nullable)
      Address line 1, such as the street, PO Box, or company name.

    - `business_profile.support_address.line2` (string, nullable)
      Address line 2, such as the apartment, suite, unit, or building.

    - `business_profile.support_address.postal_code` (string, nullable)
      ZIP or postal code.

    - `business_profile.support_address.state` (string, nullable)
      State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

  - `business_profile.support_email` (string, nullable)
    A publicly available email address for sending support issues to.

  - `business_profile.support_phone` (string, nullable)
    A publicly available phone number to call with support issues.

  - `business_profile.support_url` (string, nullable)
    A publicly available website for handling support issues.

  - `business_profile.url` (string, nullable)
    The business’s publicly available website.

- `business_type` (enum, nullable)
  The business type.
Possible enum values:
  - `company`
  - `government_entity`
    US only

  - `individual`
  - `non_profit`

- `capabilities` (object, nullable)
  A hash containing the set of capabilities that was requested for this account and their associated states. Keys are names of capabilities. You can see the full list [here](https://docs.stripe.com/docs/api/capabilities/list.md). Values may be `active`, `inactive`, or `pending`.

  - `capabilities.acss_debit_payments` (enum, nullable)
    The status of the Canadian pre-authorized debits payments capability of the account, or whether the account can directly process Canadian pre-authorized debits charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.affirm_payments` (enum, nullable)
    The status of the Affirm capability of the account, or whether the account can directly process Affirm charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.afterpay_clearpay_payments` (enum, nullable)
    The status of the Afterpay Clearpay capability of the account, or whether the account can directly process Afterpay Clearpay charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.alma_payments` (enum, nullable)
    The status of the Alma capability of the account, or whether the account can directly process Alma payments.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.amazon_pay_payments` (enum, nullable)
    The status of the AmazonPay capability of the account, or whether the account can directly process AmazonPay payments.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.au_becs_debit_payments` (enum, nullable)
    The status of the BECS Direct Debit (AU) payments capability of the account, or whether the account can directly process BECS Direct Debit (AU) charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.bacs_debit_payments` (enum, nullable)
    The status of the Bacs Direct Debits payments capability of the account, or whether the account can directly process Bacs Direct Debits charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.bancontact_payments` (enum, nullable)
    The status of the Bancontact payments capability of the account, or whether the account can directly process Bancontact charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.bank_transfer_payments` (enum, nullable)
    The status of the customer_balance payments capability of the account, or whether the account can directly process customer_balance charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.billie_payments` (enum, nullable)
    The status of the Billie capability of the account, or whether the account can directly process Billie payments.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.blik_payments` (enum, nullable)
    The status of the blik payments capability of the account, or whether the account can directly process blik charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.boleto_payments` (enum, nullable)
    The status of the boleto payments capability of the account, or whether the account can directly process boleto charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.card_issuing` (enum, nullable)
    The status of the card issuing capability of the account, or whether you can use Issuing to distribute funds on cards
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.card_payments` (enum, nullable)
    The status of the card payments capability of the account, or whether the account can directly process credit and debit card charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.cartes_bancaires_payments` (enum, nullable)
    The status of the Cartes Bancaires payments capability of the account, or whether the account can directly process Cartes Bancaires card charges in EUR currency.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.cashapp_payments` (enum, nullable)
    The status of the Cash App Pay capability of the account, or whether the account can directly process Cash App Pay payments.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.crypto_payments` (enum, nullable)
    The status of the Crypto capability of the account, or whether the account can directly process Crypto payments.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.eps_payments` (enum, nullable)
    The status of the EPS payments capability of the account, or whether the account can directly process EPS charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.fpx_payments` (enum, nullable)
    The status of the FPX payments capability of the account, or whether the account can directly process FPX charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.gb_bank_transfer_payments` (enum, nullable)
    The status of the GB customer_balance payments (GBP currency) capability of the account, or whether the account can directly process GB customer_balance charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.giropay_payments` (enum, nullable)
    The status of the giropay payments capability of the account, or whether the account can directly process giropay charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.grabpay_payments` (enum, nullable)
    The status of the GrabPay payments capability of the account, or whether the account can directly process GrabPay charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.ideal_payments` (enum, nullable)
    The status of the iDEAL payments capability of the account, or whether the account can directly process iDEAL charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.india_international_payments` (enum, nullable)
    The status of the india_international_payments capability of the account, or whether the account can process international charges (non INR) in India.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.jcb_payments` (enum, nullable)
    The status of the JCB payments capability of the account, or whether the account (Japan only) can directly process JCB credit card charges in JPY currency.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.jp_bank_transfer_payments` (enum, nullable)
    The status of the Japanese customer_balance payments (JPY currency) capability of the account, or whether the account can directly process Japanese customer_balance charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.kakao_pay_payments` (enum, nullable)
    The status of the KakaoPay capability of the account, or whether the account can directly process KakaoPay payments.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.klarna_payments` (enum, nullable)
    The status of the Klarna payments capability of the account, or whether the account can directly process Klarna charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.konbini_payments` (enum, nullable)
    The status of the konbini payments capability of the account, or whether the account can directly process konbini charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.kr_card_payments` (enum, nullable)
    The status of the KrCard capability of the account, or whether the account can directly process KrCard payments.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.legacy_payments` (enum, nullable)
    The status of the legacy payments capability of the account.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.link_payments` (enum, nullable)
    The status of the link_payments capability of the account, or whether the account can directly process Link charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.mb_way_payments` (enum, nullable)
    The status of the MB WAY payments capability of the account, or whether the account can directly process MB WAY charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.mobilepay_payments` (enum, nullable)
    The status of the MobilePay capability of the account, or whether the account can directly process MobilePay charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.multibanco_payments` (enum, nullable)
    The status of the Multibanco payments capability of the account, or whether the account can directly process Multibanco charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.mx_bank_transfer_payments` (enum, nullable)
    The status of the Mexican customer_balance payments (MXN currency) capability of the account, or whether the account can directly process Mexican customer_balance charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.naver_pay_payments` (enum, nullable)
    The status of the NaverPay capability of the account, or whether the account can directly process NaverPay payments.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.nz_bank_account_becs_debit_payments` (enum, nullable)
    The status of the New Zealand BECS Direct Debit payments capability of the account, or whether the account can directly process New Zealand BECS Direct Debit charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.oxxo_payments` (enum, nullable)
    The status of the OXXO payments capability of the account, or whether the account can directly process OXXO charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.p24_payments` (enum, nullable)
    The status of the P24 payments capability of the account, or whether the account can directly process P24 charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.pay_by_bank_payments` (enum, nullable)
    The status of the pay_by_bank payments capability of the account, or whether the account can directly process pay_by_bank charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.payco_payments` (enum, nullable)
    The status of the Payco capability of the account, or whether the account can directly process Payco payments.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.paynow_payments` (enum, nullable)
    The status of the paynow payments capability of the account, or whether the account can directly process paynow charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.payto_payments` (enum, nullable)
    The status of the PayTo capability of the account, or whether the account can directly process PayTo charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.pix_payments` (enum, nullable)
    The status of the pix payments capability of the account, or whether the account can directly process pix charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.promptpay_payments` (enum, nullable)
    The status of the promptpay payments capability of the account, or whether the account can directly process promptpay charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.revolut_pay_payments` (enum, nullable)
    The status of the RevolutPay capability of the account, or whether the account can directly process RevolutPay payments.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.samsung_pay_payments` (enum, nullable)
    The status of the SamsungPay capability of the account, or whether the account can directly process SamsungPay payments.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.satispay_payments` (enum, nullable)
    The status of the Satispay capability of the account, or whether the account can directly process Satispay payments.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.sepa_bank_transfer_payments` (enum, nullable)
    The status of the SEPA customer_balance payments (EUR currency) capability of the account, or whether the account can directly process SEPA customer_balance charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.sepa_debit_payments` (enum, nullable)
    The status of the SEPA Direct Debits payments capability of the account, or whether the account can directly process SEPA Direct Debits charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.sofort_payments` (enum, nullable)
    The status of the Sofort payments capability of the account, or whether the account can directly process Sofort charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.swish_payments` (enum, nullable)
    The status of the Swish capability of the account, or whether the account can directly process Swish payments.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.tax_reporting_us_1099_k` (enum, nullable)
    The status of the tax reporting 1099-K (US) capability of the account.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.tax_reporting_us_1099_misc` (enum, nullable)
    The status of the tax reporting 1099-MISC (US) capability of the account.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.transfers` (enum, nullable)
    The status of the transfers capability of the account, or whether your platform can transfer funds to the account.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.twint_payments` (enum, nullable)
    The status of the TWINT capability of the account, or whether the account can directly process TWINT charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.us_bank_account_ach_payments` (enum, nullable)
    The status of the US bank account ACH payments capability of the account, or whether the account can directly process US bank account charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.us_bank_transfer_payments` (enum, nullable)
    The status of the US customer_balance payments (USD currency) capability of the account, or whether the account can directly process US customer_balance charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

  - `capabilities.zip_payments` (enum, nullable)
    The status of the Zip capability of the account, or whether the account can directly process Zip charges.
Possible enum values:
    - `active`
    - `inactive`
    - `pending`

- `charges_enabled` (boolean)
  Whether the account can process charges.

- `company` (object, nullable)
  Information about the company or business. This property is available for any `business_type`. After you create an [Account Link](https://docs.stripe.com/api/account_links.md) or [Account Session](https://docs.stripe.com/api/account_sessions.md), only a subset of this property is returned for accounts where [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `stripe`, which includes Standard and Express accounts.

  - `company.address` (object, nullable)
    The company’s primary address.

    - `company.address.city` (string, nullable)
      City, district, suburb, town, or village.

    - `company.address.country` (string, nullable)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `company.address.line1` (string, nullable)
      Address line 1, such as the street, PO Box, or company name.

    - `company.address.line2` (string, nullable)
      Address line 2, such as the apartment, suite, unit, or building.

    - `company.address.postal_code` (string, nullable)
      ZIP or postal code.

    - `company.address.state` (string, nullable)
      State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

  - `company.address_kana` (object, nullable)
    The Kana variation of the company’s primary address (Japan only).

    - `company.address_kana.city` (string, nullable)
      City/Ward.

    - `company.address_kana.country` (string, nullable)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `company.address_kana.line1` (string, nullable)
      Block/Building number.

    - `company.address_kana.line2` (string, nullable)
      Building details.

    - `company.address_kana.postal_code` (string, nullable)
      ZIP or postal code.

    - `company.address_kana.state` (string, nullable)
      Prefecture.

    - `company.address_kana.town` (string, nullable)
      Town/cho-me.

  - `company.address_kanji` (object, nullable)
    The Kanji variation of the company’s primary address (Japan only).

    - `company.address_kanji.city` (string, nullable)
      City/Ward.

    - `company.address_kanji.country` (string, nullable)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `company.address_kanji.line1` (string, nullable)
      Block/Building number.

    - `company.address_kanji.line2` (string, nullable)
      Building details.

    - `company.address_kanji.postal_code` (string, nullable)
      ZIP or postal code.

    - `company.address_kanji.state` (string, nullable)
      Prefecture.

    - `company.address_kanji.town` (string, nullable)
      Town/cho-me.

  - `company.directors_provided` (boolean)
    Whether the company’s directors have been provided. This Boolean will be `true` if you’ve manually indicated that all directors are provided via [the `directors_provided` parameter](https://docs.stripe.com/docs/api/accounts/update.md#update_account-company-directors_provided).

  - `company.directorship_declaration` (object, nullable)
    This hash is used to attest that the director information provided to Stripe is both current and correct.

    - `company.directorship_declaration.date` (timestamp, nullable)
      The Unix timestamp marking when the directorship declaration attestation was made.

    - `company.directorship_declaration.ip` (string, nullable)
      The IP address from which the directorship declaration attestation was made.

    - `company.directorship_declaration.user_agent` (string, nullable)
      The user-agent string from the browser where the directorship declaration attestation was made.

  - `company.executives_provided` (boolean)
    Whether the company’s executives have been provided. This Boolean will be `true` if you’ve manually indicated that all executives are provided via [the `executives_provided` parameter](https://docs.stripe.com/docs/api/accounts/update.md#update_account-company-executives_provided), or if Stripe determined that sufficient executives were provided.

  - `company.export_license_id` (string, nullable)
    The export license ID number of the company, also referred as Import Export Code (India only).

  - `company.export_purpose_code` (string, nullable)
    The purpose code to use for export transactions (India only).

  - `company.name` (string, nullable)
    The company’s legal name. Also available for accounts where [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `stripe`.

  - `company.name_kana` (string, nullable)
    The Kana variation of the company’s legal name (Japan only). Also available for accounts where [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `stripe`.

  - `company.name_kanji` (string, nullable)
    The Kanji variation of the company’s legal name (Japan only). Also available for accounts where [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `stripe`.

  - `company.owners_provided` (boolean)
    Whether the company’s owners have been provided. This Boolean will be `true` if you’ve manually indicated that all owners are provided via [the `owners_provided` parameter](https://docs.stripe.com/docs/api/accounts/update.md#update_account-company-owners_provided), or if Stripe determined that sufficient owners were provided. Stripe determines ownership requirements using both the number of owners provided and their total percent ownership (calculated by adding the `percent_ownership` of each owner together).

  - `company.ownership_declaration` (object, nullable)
    This hash is used to attest that the beneficial owner information provided to Stripe is both current and correct.

    - `company.ownership_declaration.date` (timestamp, nullable)
      The Unix timestamp marking when the beneficial owner attestation was made.

    - `company.ownership_declaration.ip` (string, nullable)
      The IP address from which the beneficial owner attestation was made.

    - `company.ownership_declaration.user_agent` (string, nullable)
      The user-agent string from the browser where the beneficial owner attestation was made.

  - `company.ownership_exemption_reason` (enum, nullable)
    This value is used to determine if a business is exempt from providing ultimate beneficial owners. See [this support article](https://support.stripe.com/questions/exemption-from-providing-ownership-details) and [changelog](https://docs.stripe.com/changelog/acacia/2025-01-27/ownership-exemption-reason-accounts-api.md) for more details.

  - `company.phone` (string, nullable)
    The company’s phone number (used for verification).

  - `company.representative_declaration` (object, nullable)
    This hash is used to attest that the representative is authorized to act as the representative of their legal entity.

    - `company.representative_declaration.date` (timestamp, nullable)
      The Unix timestamp marking when the representative declaration attestation was made.

    - `company.representative_declaration.ip` (string, nullable)
      The IP address from which the representative declaration attestation was made.

    - `company.representative_declaration.user_agent` (string, nullable)
      The user-agent string from the browser where the representative declaration attestation was made.

  - `company.structure` (enum, nullable)
    The category identifying the legal structure of the company or legal entity. Also available for accounts where [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `stripe`. See [Business structure](https://docs.stripe.com/docs/connect/identity-verification.md#business-structure) for more details.

  - `company.tax_id_provided` (boolean)
    Whether the company’s business ID number was provided.

  - `company.tax_id_registrar` (string, nullable)
    The jurisdiction in which the `tax_id` is registered (Germany-based companies only).

  - `company.vat_id_provided` (boolean, nullable)
    Whether the company’s business VAT number was provided.

  - `company.verification` (object, nullable)
    Information on the verification state of the company.

    - `company.verification.document` (object)
      A document for the company.

      - `company.verification.document.back` (string, nullable)
        The back of a document returned by a [file upload](https://docs.stripe.com/api/accounts/object.md#create_file) with a `purpose` value of `additional_verification`. Note that `additional_verification` files are [not downloadable](https://docs.stripe.com/file-upload.md#uploading-a-file).

      - `company.verification.document.details` (string, nullable)
        A user-displayable string describing the verification state of this document.

      - `company.verification.document.details_code` (string, nullable)
        One of `document_corrupt`, `document_expired`, `document_failed_copy`, `document_failed_greyscale`, `document_failed_other`, `document_failed_test_mode`, `document_fraudulent`, `document_incomplete`, `document_invalid`, `document_manipulated`, `document_not_readable`, `document_not_uploaded`, `document_type_not_supported`, or `document_too_large`. A machine-readable code specifying the verification state for this document.

      - `company.verification.document.front` (string, nullable)
        The front of a document returned by a [file upload](https://docs.stripe.com/api/accounts/object.md#create_file) with a `purpose` value of `additional_verification`. Note that `additional_verification` files are [not downloadable](https://docs.stripe.com/file-upload.md#uploading-a-file).

- `controller` (object, nullable)
  The controller of the account.

  - `controller.fees` (object, nullable)
    A hash of configuration related to fees for this account. Only returned when the Connect application retrieving the resource controls the account.

    - `controller.fees.payer` (enum)
      A value indicating the responsible payer of a bundle of Stripe fees for pricing-control eligible products on this account. Learn more about [fee behavior on connected accounts](https://docs.stripe.com/connect/direct-charges-fee-payer-behavior.md).
Possible enum values:
      - `account`
        The account is responsible for paying Stripe fees.

      - `application`
        The Connect application is responsible for Stripe fees on pricing-control eligible products.

      - `application_custom`
        The Connect application is responsible for fees matching the behavior of Custom accounts.

      - `application_express`
        The Connect application is responsible for fees matching the behavior of Express accounts.

  - `controller.is_controller` (boolean, nullable)
    `true` if the Connect application retrieving the resource controls the account and can therefore exercise [platform controls](https://docs.stripe.com/docs/connect/platform-controls-for-standard-accounts.md). Otherwise, this field is null.

  - `controller.losses` (object, nullable)
    The list of products that have a negative balance liability and whether Stripe or a Connect application is responsible. Only returned when the Connect application retrieving the resource controls the account.

    - `controller.losses.payments` (enum)
      A value indicating who is liable when this account can’t pay back negative balances from payments.
Possible enum values:
      - `application`
        The Connect application is liable when this account can’t pay back negative balances resulting from payments.

      - `stripe`
        Stripe is liable when this account can’t pay back negative balances resulting from payments.

  - `controller.requirement_collection` (enum, nullable)
    A value indicating responsibility for collecting requirements on this account. Only returned when the Connect application retrieving the resource controls the account.
Possible enum values:
    - `application`
      The Connect application is responsible for collecting outstanding and updated requirements on the account. The Connect application can [fully access the KYC properties](https://docs.stripe.com/connect/identity-verification.md) on the account, as well as attest that the account has seen and accepted the [Stripe service agreement](https://docs.stripe.com/connect/service-agreement-types.md) via the API.

    - `stripe`
      Stripe is responsible for collecting outstanding and updated requirements on the account.

  - `controller.stripe_dashboard` (object, nullable)
    A hash of configuration controlling Stripe provided dashboards. Only returned when the Connect application retrieving the resource controls the account.

    - `controller.stripe_dashboard.type` (enum)
      A value indicating the Stripe dashboard this account has access to independent of the Connect application.
Possible enum values:
      - `express`
        The account has access to the [Express Dashboard](https://connect.stripe.com/express_login).

      - `full`
        The account has access to the full [Stripe Dashboard](https://dashboard.stripe.com).

      - `none`
        The account does not have access to a Stripe-hosted dashboard. The Connect application is responsible for providing UIs to the account.

  - `controller.type` (enum)
    The controller type. Can be `application`, if a Connect application controls the account, or `account`, if the account controls itself.
Possible enum values:
    - `account`
    - `application`

- `country` (string)
  The account’s country.

- `created` (timestamp)
  Time at which the account was connected. Measured in seconds since the Unix epoch.

- `default_currency` (string)
  Three-letter ISO currency code representing the default currency for the account. This must be a currency that [Stripe supports in the account’s country](https://stripe.com/docs/payouts).

- `details_submitted` (boolean)
  Whether account details have been submitted. Accounts with Stripe Dashboard access, which includes Standard accounts, cannot receive payouts before this is true. Accounts where this is false should be directed to [an onboarding flow](https://docs.stripe.com/connect/onboarding.md) to finish submitting account details.

- `email` (string, nullable)
  An email address associated with the account. It’s not used for authentication and Stripe doesn’t market to this field without explicit approval from the platform.

- `external_accounts` (object)
  External accounts (bank accounts and debit cards) currently attached to this account. External accounts are only returned for requests where `controller[is_controller]` is true.

  - `external_accounts.object` (string)
    String representing the object’s type. Objects of the same type share the same value. Always has the value `list`.

  - `external_accounts.data` (array of objects)
    The list contains all external accounts that have been attached to the Stripe account. These may be bank accounts or cards.

    - `external_accounts.data.id` (string)
      Unique identifier for the object.

    - `external_accounts.data.object` (string)
      String representing the object’s type. Objects of the same type share the same value.

    - `external_accounts.data.account` (string, nullable)
      The account this card belongs to. This attribute will not be in the card object if the card belongs to a customer or recipient instead. This property is only available for accounts where [controller.is_controller](https://docs.stripe.com/api/accounts/object.md#account_object-controller-is_controller) is `true`.

    - `external_accounts.data.address_city` (string, nullable)
      City/District/Suburb/Town/Village.

    - `external_accounts.data.address_country` (string, nullable)
      Billing address country, if provided when creating card.

    - `external_accounts.data.address_line1` (string, nullable)
      Address line 1 (Street address/PO Box/Company name).

    - `external_accounts.data.address_line1_check` (string, nullable)
      If `address_line1` was provided, results of the check: `pass`, `fail`, `unavailable`, or `unchecked`.

    - `external_accounts.data.address_line2` (string, nullable)
      Address line 2 (Apartment/Suite/Unit/Building).

    - `external_accounts.data.address_state` (string, nullable)
      State/County/Province/Region.

    - `external_accounts.data.address_zip` (string, nullable)
      ZIP or postal code.

    - `external_accounts.data.address_zip_check` (string, nullable)
      If `address_zip` was provided, results of the check: `pass`, `fail`, `unavailable`, or `unchecked`.

    - `external_accounts.data.allow_redisplay` (enum, nullable)
      This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow. The field defaults to “unspecified”.
Possible enum values:
      - `always`
        Use `always` to indicate that this payment method can always be shown to a customer in a checkout flow.

      - `limited`
        Use `limited` to indicate that this payment method can’t always be shown to a customer in a checkout flow. For example, it can only be shown in the context of a specific subscription.

      - `unspecified`
        This is the default value for payment methods where `allow_redisplay` wasn’t set.

    - `external_accounts.data.available_payout_methods` (array of enums, nullable)
      A set of available payout methods for this card. Only values from this set should be passed as the `method` when creating a payout.
Possible enum values:
      - `instant`
      - `standard`

    - `external_accounts.data.brand` (string)
      Card brand. Can be `American Express`, `Cartes Bancaires`, `Diners Club`, `Discover`, `Eftpos Australia`, `Girocard`, `JCB`, `MasterCard`, `UnionPay`, `Visa`, or `Unknown`.

    - `external_accounts.data.country` (string, nullable)
      Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you’ve collected.

    - `external_accounts.data.currency` (enum, nullable)
      Three-letter [ISO code for currency](https://www.iso.org/iso-4217-currency-codes.html) in lowercase. Must be a [supported currency](https://docs.stripe.com/currencies.md). Only applicable on accounts (not customers or recipients). The card can be used as a transfer destination for funds in this currency. This property is only available for accounts where [controller.is_controller](https://docs.stripe.com/api/accounts/object.md#account_object-controller-is_controller) is `true`.

    - `external_accounts.data.customer` (string, nullable)
      The customer that this card belongs to. This attribute will not be in the card object if the card belongs to an account or recipient instead.

    - `external_accounts.data.cvc_check` (string, nullable)
      If a CVC was provided, results of the check: `pass`, `fail`, `unavailable`, or `unchecked`. A result of unchecked indicates that CVC was provided but hasn’t been checked yet. Checks are typically performed when attaching a card to a Customer object, or when creating a charge. For more details, see [Check if a card is valid without a charge](https://support.stripe.com/questions/check-if-a-card-is-valid-without-a-charge).

    - `external_accounts.data.default_for_currency` (boolean, nullable)
      Whether this card is the default external account for its currency. This property is only available for accounts where [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `application`, which includes Custom accounts.

    - `external_accounts.data.dynamic_last4` (string, nullable)
      (For tokenized numbers only.) The last four digits of the device account number.

    - `external_accounts.data.exp_month` (integer)
      Two-digit number representing the card’s expiration month.

    - `external_accounts.data.exp_year` (integer)
      Four-digit number representing the card’s expiration year.

    - `external_accounts.data.fingerprint` (string, nullable)
      Uniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.

      *As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card—one for India and one for the rest of the world.*

    - `external_accounts.data.funding` (string)
      Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.

    - `external_accounts.data.iin` (string, nullable)
      Issuer identification number of the card.

    - `external_accounts.data.last4` (string)
      The last four digits of the card.

    - `external_accounts.data.metadata` (object, nullable)
      Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

    - `external_accounts.data.name` (string, nullable)
      Cardholder name.

    - `external_accounts.data.regulated_status` (enum, nullable)
      Status of a card based on the card issuer.
Possible enum values:
      - `regulated`
        The card falls under a regulated account range.

      - `unregulated`
        The card does not fall under a regulated account range.

    - `external_accounts.data.status` (string, nullable)
      For external accounts that are cards, possible values are `new` and `errored`. If a payout fails, the status is set to `errored` and [scheduled payouts](https://stripe.com/docs/payouts#payout-schedule) are stopped until account details are updated.

    - `external_accounts.data.tokenization_method` (string, nullable)
      If the card number is tokenized, this is the method that was used. Can be `android_pay` (includes Google Pay), `apple_pay`, `masterpass`, `visa_checkout`, or null.

    - `external_accounts.data.wallet` (object, nullable)
      If this Card is part of a card wallet, this contains the details of the card wallet.

      - `external_accounts.data.wallet.apple_pay` (object, nullable)
        If this is a `apple_pay` card wallet, this hash contains details about the wallet.

      - `external_accounts.data.wallet.type` (enum)
        The type of the card wallet, one of `apple_pay` or `link`. An additional hash is included on the Wallet subhash with a name matching this value. It contains additional information specific to the card wallet type.
Possible enum values:
        - `apple_pay`
        - `link`

  - `external_accounts.has_more` (boolean)
    True if this list has another page of items after this one that can be fetched.

  - `external_accounts.url` (string)
    The URL where this list can be accessed.

- `future_requirements` (object, nullable)
  Details about the [upcoming new requirements for the account](https://docs.stripe.com/docs/connect/custom-accounts/future-requirements.md), including what information needs to be collected, verified, or reviewed, and by when. After a requirement is collected, verified, or reviewed, it is considered resolved. Most requirements can be addressed programmatically, however, some must be completed through a form or challenge using the Stripe Interface. [Learn more about handling requirements](https://docs.stripe.com/docs/connect/handling-api-verification.md).

  - `future_requirements.alternatives` (array of objects, nullable)
    Fields that are due and can be resolved by providing the corresponding alternative fields instead. Many alternatives can list the same `original_fields_due`, and any of these alternatives can serve as a pathway for attempting to resolve the fields again. Re-providing `original_fields_due` also serves as a pathway for attempting to resolve the fields again.

    - `future_requirements.alternatives.alternative_fields_due` (array of strings)
      Fields that can be provided to resolve all fields in `original_fields_due`.

    - `future_requirements.alternatives.original_fields_due` (array of strings)
      Fields that are due and can be resolved by providing all fields in `alternative_fields_due`.

  - `future_requirements.current_deadline` (timestamp, nullable)
    Date on which `future_requirements` becomes the main `requirements` hash and `future_requirements` becomes empty. After the transition, `currently_due` requirements may immediately become `past_due`, but the account may also be given a grace period depending on its enablement state prior to transitioning.

  - `future_requirements.currently_due` (array of strings, nullable)
    Fields that need to be resolved to keep the account enabled. If not resolved by `future_requirements[current_deadline]`, these fields will transition to the main `requirements` hash.

  - `future_requirements.disabled_reason` (enum, nullable)
    This is typed as an enum for consistency with `requirements.disabled_reason`.
Possible enum values:
    - `action_required.requested_capabilities`
      The account has been disabled because its requested capabilities require action.

    - `listed`
      The account has been listed.

    - `other`
      The account has been disabled for another reason.

    - `platform_paused`
      The account has been paused by the platform.

    - `rejected.fraud`
      The account has been rejected for fraud.

    - `rejected.incomplete_verification`
      The account has been rejected for incomplete verification.

    - `rejected.listed`
      The account has been rejected because it is listed.

    - `rejected.other`
      The account has been rejected for another reason.

    - `rejected.platform_fraud`
      The account has been rejected by the platform for fraud.

    - `rejected.platform_other`
      The account has been rejected by the platform.

    - `rejected.platform_terms_of_service`
      The account has been rejected by the platform for violating the Stripe services agreement.

    - `rejected.terms_of_service`
      The account has been rejected because it does not meet Stripe’s terms of service.

    - `requirements.past_due`
      The account has been disabled because requirements are past_due.

    - `requirements.pending_verification`
      The account has been disabled because requirements are pending verification.

    - `under_review`
      The account has been disabled because it is under review.

  - `future_requirements.errors` (array of objects, nullable)
    Details about validation and verification failures for `due` requirements that must be resolved.

    - `future_requirements.errors.code` (enum)
      The code for the type of error.
Possible enum values:
      - `information_missing`
        The requirement associated with this error is missing critical information. The associated error reason provides more details.

      - `invalid_address_city_state_postal_code`
        The combination of the city, state, and postal code in the provided address could not be validated.

      - `invalid_address_cmra_address`
        The address you provided appears to be associated with a mailbox or virtual address service, which we can’t accept. Please update your address to proceed.

      - `invalid_address_highway_contract_box`
        Invalid address. Your business address must be a valid physical address from which you conduct business and cannot be a Highway Contract Box.

      - `invalid_address_private_mailbox`
        Invalid address. Your business address must be a valid physical address from which you conduct business and cannot be a private mailbox.

      - `invalid_address_registered_agent_address`
        The address you provided appears to be associated with a registered agent, which we can’t accept. Please update your address to proceed. If you believe this is an error, you can submit a proof of address document for review.

      - `invalid_business_profile_name`
        Business profile names must consist of recognizable words.

      - `invalid_business_profile_name_denylisted`
        Generic or well-known business names aren’t supported.

      - `invalid_company_name_denylisted`
        Generic or well-known business names aren’t supported.

      - `invalid_dob_age_over_maximum`
        Date of birth must be within the past 120 years.

      - `invalid_dob_age_under_18`
        Underage. Age must be at least 18.

      - `invalid_dob_age_under_minimum`
        Person must be at least 13 years old.

      - `invalid_product_description_length`
        Your product description must be at least 10 characters.

      - `invalid_product_description_url_match`
        Your product description must be different from your URL.

      - `invalid_representative_country`
        The representative must have an address in the same country as the company.

      - `invalid_signator`
        We could not verify the professional certifying body of this document.

      - `invalid_statement_descriptor_business_mismatch`
        The statement descriptor must be similar to your business name, legal entity name, or URL.

      - `invalid_statement_descriptor_denylisted`
        Generic or well-known statement descriptors aren’t supported.

      - `invalid_statement_descriptor_length`
        The statement descriptor must be at least 5 characters.

      - `invalid_statement_descriptor_prefix_denylisted`
        Generic or well-known statement descriptor prefixes aren’t supported.

      - `invalid_statement_descriptor_prefix_mismatch`
        The statement descriptor prefix must be similar to your statement descriptor, business name, legal entity name, or URL.

      - `invalid_street_address`
        The street name and/or number for the provided address could not be validated.

      - `invalid_tax_id`
        The provided tax ID must have 9 digits

      - `invalid_tax_id_format`
        Tax IDs must be a unique set of 9 numbers without dashes or other special characters.

      - `invalid_tos_acceptance`
        The existing terms of service signature has been invalidated because the account’s tax ID has changed. The account needs to accept the terms of service again. For more information, see [this documentation](https://docs.stripe.com/connect/update-verified-information.md).

      - `invalid_url_denylisted`
        Generic business URLs aren’t supported.

      - `invalid_url_format`
        URL must be formatted as https://example.com.

      - `invalid_url_web_presence_detected`
        Because you use a website, app, social media page, or online profile to sell products or services, you must provide a URL for your business.

      - `invalid_url_website_business_information_mismatch`
        The business information on your website must match the details you provided to Stripe.

      - `invalid_url_website_empty`
        Your provided website appears to be empty.

      - `invalid_url_website_inaccessible`
        This URL couldn’t be reached. Make sure it’s available and entered correctly or provide another.

      - `invalid_url_website_inaccessible_geoblocked`
        Your provided website appears to be geographically blocked.

      - `invalid_url_website_inaccessible_password_protected`
        Your provided website appears to be password protected.

      - `invalid_url_website_incomplete`
        Your website seems to be missing some required information. [Learn about the requirements](https://support.stripe.com/questions/information-required-on-your-business-website-to-use-stripe)

      - `invalid_url_website_incomplete_cancellation_policy`
        Your provided website appears to have an incomplete cancellation policy.

      - `invalid_url_website_incomplete_customer_service_details`
        Your provided website appears to have incomplete customer service details.

      - `invalid_url_website_incomplete_legal_restrictions`
        Your provided website appears to have incomplete legal restrictions.

      - `invalid_url_website_incomplete_refund_policy`
        Your provided website appears to have an incomplete refund policy.

      - `invalid_url_website_incomplete_return_policy`
        Your provided website appears to have an incomplete refund policy.

      - `invalid_url_website_incomplete_terms_and_conditions`
        Your provided website appears to have incomplete terms and conditions.

      - `invalid_url_website_incomplete_under_construction`
        Your provided website appears to be incomplete or under construction.

      - `invalid_url_website_other`
        We weren’t able to verify your business using the URL you provided. Make sure it’s entered correctly or provide another URL.

      - `invalid_value_other`
        An invalid value was provided for the related field. This is a general error code.

      - `unsupported_business_type`
        The business type you provided isn’t supported in this country.

      - `verification_directors_mismatch`
        Directors on the account don’t match government records. Update the account and upload a directorship document with current directors.

      - `verification_document_address_mismatch`
        Address on the account doesn’t match the verification document. Update the account and upload the document again.

      - `verification_document_address_missing`
        The company address was missing on the document. Upload a document that includes the address.

      - `verification_document_corrupt`
        File seems to be corrupted or damaged. Provide a different file.

      - `verification_document_country_not_supported`
        Document isn’t supported in this person’s country or region. Provide a supported verification document.

      - `verification_document_directors_mismatch`
        Directors on the account don’t match the document provided. Update the account to match the registration document and upload it again.

      - `verification_document_dob_mismatch`
        The date of birth (DOB) on the document did not match the DOB on the account. Upload a document with a matching DOB or update the DOB on the account.

      - `verification_document_duplicate_type`
        The same type of document was used twice. Two unique types of documents are required for verification.

      - `verification_document_expired`
        The document could not be used for verification because it has expired. If it’s an identity document, its expiration date must be after the date the document was submitted. If it’s an address document, the issue date must be within the last six months.

      - `verification_document_failed_copy`
        Document is a photo or screenshot. Upload the original document.

      - `verification_document_failed_greyscale`
        Document seems to be in grayscale or black and white. Provide a full color photo of the document for verification.

      - `verification_document_failed_other`
        The document could not be verified for an unknown reason. Ensure that the document follows the [guidelines for document uploads](https://docs.stripe.com/acceptable-verification-documents.md).

      - `verification_document_failed_test_mode`
        A test data helper was supplied to simulate verification failure. Refer to the documentation for [test file tokens](https://docs.stripe.com/connect/testing.md#test-file-tokens).

      - `verification_document_fraudulent`
        Document seems to be altered. This could be because it’s fraudulent.

      - `verification_document_id_number_mismatch`
        Tax ID number on the account doesn’t match the verification document. Update the account to match the verification document and upload it again.

      - `verification_document_id_number_missing`
        The company ID number was missing on the document. Upload a document that includes the ID number.

      - `verification_document_incomplete`
        Document doesn’t include required information. Make sure all pages and sections are complete.

      - `verification_document_invalid`
        Document isn’t an acceptable form of identification in this account’s country or region. Ensure that the document follows the [guidelines for document uploads](https://docs.stripe.com/acceptable-verification-documents.md).

      - `verification_document_issue_or_expiry_date_missing`
        Document is missing an expiration date. Provide a document with an expiration date.

      - `verification_document_manipulated`
        Document seems to be altered. This could be because it’s fraudulent.

      - `verification_document_missing_back`
        The back of the document is missing. Provide both sides of the document for verification.

      - `verification_document_missing_front`
        The front of the document is missing. Provide both sides of the document for verification.

      - `verification_document_name_mismatch`
        The name on the account does not match the name on the document. Update the account to match the document and upload it again.

      - `verification_document_name_missing`
        The company name was missing on the document. Upload a document that includes the company name.

      - `verification_document_nationality_mismatch`
        The nationality on the document did not match the person’s stated nationality. Update the person’s stated nationality, or upload a document that matches it.

      - `verification_document_not_readable`
        Document isn’t readable. This could be because it’s blurry or dark, or because the document was obstructed.

      - `verification_document_not_signed`
        Document doesn’t seem to be signed. Provide a signed document.

      - `verification_document_not_uploaded`
        Document didn’t upload because of a problem with the file.

      - `verification_document_photo_mismatch`
        ID photo on the document doesn’t match the selfie provided by this account.

      - `verification_document_too_large`
        Document file is too large. Upload one that’s 10MB or less.

      - `verification_document_type_not_supported`
        The provided document type is not accepted. Ensure that the document follows the [guidelines for document uploads](https://docs.stripe.com/acceptable-verification-documents.md).

      - `verification_extraneous_directors`
        Extraneous directors have been added to the account. Update the account and upload a registration document with current directors.

      - `verification_failed_address_match`
        The address on the account could not be verified. Correct any errors in the address field or upload a document that includes the address.

      - `verification_failed_authorizer_authority`
        The account authorizer is not a registered authorized representative. Refer to [this support article](https://support.stripe.com/questions/representative-authority-verification) for more information.

      - `verification_failed_business_iec_number`
        The Importer Exporter Code (IEC) number on your account could not be verified. Either correct any possible errors in the company name or IEC number. Refer to the support article for [accepting international payments in India](https://support.stripe.com/questions/accepting-international-payments-from-stripe-accounts-in-india).

      - `verification_failed_document_match`
        The document could not be verified. Upload a document that includes the company name, ID number, and address fields.

      - `verification_failed_id_number_match`
        ID number on the document doesn’t match the ID number provided by this account.

      - `verification_failed_keyed_identity`
        The person’s keyed-in identity information could not be verified. Correct any errors or upload a document that matches the identity fields (e.g., name and date of birth) entered.

      - `verification_failed_keyed_match`
        The keyed-in information on the account could not be verified. Correct any errors in the company name, ID number, or address fields. You can also upload a document that includes those fields.

      - `verification_failed_name_match`
        The company name on the account could not be verified. Correct any errors in the company name field or upload a document that includes the company name.

      - `verification_failed_other`
        Verification failed for an unknown reason. Correct any errors and resubmit the required fields.

      - `verification_failed_representative_authority`
        The authority of the account representative could not be verified. Please change the account representative to a person who is registered as an authorized representative. Please refer to [this support article](https://support.stripe.com/questions/representative-authority-verification).

      - `verification_failed_residential_address`
        We could not verify that the person resides at the provided address. The address must be a valid physical address where the individual resides and cannot be a P.O. Box.

      - `verification_failed_tax_id_match`
        The tax ID on the account cannot be verified by the IRS. Either correct any possible errors in the company name or tax ID, or upload a document that contains those fields.

      - `verification_failed_tax_id_not_issued`
        The tax ID on the account was not recognized by the IRS. Refer to the support article for [newly-issued tax ID numbers](https://support.stripe.com/questions/newly-issued-us-tax-id-number-tin-not-verifying).

      - `verification_legal_entity_structure_mismatch`
        Business type or structure seems to be incorrect. Provide the correct business type and structure for this account.

      - `verification_missing_directors`
        We identified that your business has directors that have not been added to the account. Please add missing directors to your account.

      - `verification_missing_executives`
        We have identified executives that haven’t been added on the account. Add any missing executives to the account.

      - `verification_missing_owners`
        We have identified owners that haven’t been added on the account. Add any missing owners to the account.

      - `verification_rejected_ownership_exemption_reason`
        The ownership exemption reason was rejected.

      - `verification_requires_additional_memorandum_of_associations`
        We have identified holding companies with significant percentage ownership. Upload a Memorandum of Association for each of the holding companies.

      - `verification_requires_additional_proof_of_registration`
        The uploaded document contains holding companies with significant percentage ownership. Upload a proof of registration for each of the holding companies.

      - `verification_supportability`
        We can’t accept payments for this business under the Stripe Services Agreement without additional verification, as mentioned in the [prohibited and restricted businesses list](https://stripe.com/legal/restricted-businesses).

    - `future_requirements.errors.reason` (string)
      An informative message that indicates the error type and provides additional details about the error.

    - `future_requirements.errors.requirement` (string)
      The specific user onboarding requirement field (in the requirements hash) that needs to be resolved.

  - `future_requirements.eventually_due` (array of strings, nullable)
    Fields you must collect when all thresholds are reached. As they become required, they appear in `currently_due` as well.

  - `future_requirements.past_due` (array of strings, nullable)
    Fields that haven’t been resolved by `requirements.current_deadline`. These fields need to be resolved to enable the capability on the account. `future_requirements.past_due` is a subset of `requirements.past_due`.

  - `future_requirements.pending_verification` (array of strings, nullable)
    Fields that are being reviewed, or might become required depending on the results of a review. If the review fails, these fields can move to `eventually_due`, `currently_due`, `past_due` or `alternatives`. Fields might appear in `eventually_due`, `currently_due`, `past_due` or `alternatives` and in `pending_verification` if one verification fails but another is still pending.

- `groups` (object, nullable)
  The groups associated with the account.

  - `groups.payments_pricing` (string, nullable)
    The group the account is in to determine their payments pricing, and null if the account is on customized pricing. [See the Platform pricing tool documentation](https://docs.stripe.com/docs/connect/platform-pricing-tools.md) for details.

- `individual` (object, nullable)
  Information about the person represented by the account. This property is null unless `business_type` is set to `individual`. After you create an [Account Link](https://docs.stripe.com/api/account_links.md) or [Account Session](https://docs.stripe.com/api/account_sessions.md), only a subset of this property is returned for accounts where [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `stripe`, which includes Standard and Express accounts.

  - `individual.id` (string)
    Unique identifier for the object.

  - `individual.object` (string)
    String representing the object’s type. Objects of the same type share the same value.

  - `individual.account` (string)
    The account the individual is associated with.

  - `individual.address` (object, nullable)
    The individual’s primary address.

    - `individual.address.city` (string, nullable)
      City, district, suburb, town, or village.

    - `individual.address.country` (string, nullable)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `individual.address.line1` (string, nullable)
      Address line 1, such as the street, PO Box, or company name.

    - `individual.address.line2` (string, nullable)
      Address line 2, such as the apartment, suite, unit, or building.

    - `individual.address.postal_code` (string, nullable)
      ZIP or postal code.

    - `individual.address.state` (string, nullable)
      State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

  - `individual.address_kana` (object, nullable)
    The Kana variation of the individual’s primary address (Japan only).

    - `individual.address_kana.city` (string, nullable)
      City/Ward.

    - `individual.address_kana.country` (string, nullable)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `individual.address_kana.line1` (string, nullable)
      Block/Building number.

    - `individual.address_kana.line2` (string, nullable)
      Building details.

    - `individual.address_kana.postal_code` (string, nullable)
      ZIP or postal code.

    - `individual.address_kana.state` (string, nullable)
      Prefecture.

    - `individual.address_kana.town` (string, nullable)
      Town/cho-me.

  - `individual.address_kanji` (object, nullable)
    The Kanji variation of the individual’s primary address (Japan only).

    - `individual.address_kanji.city` (string, nullable)
      City/Ward.

    - `individual.address_kanji.country` (string, nullable)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `individual.address_kanji.line1` (string, nullable)
      Block/Building number.

    - `individual.address_kanji.line2` (string, nullable)
      Building details.

    - `individual.address_kanji.postal_code` (string, nullable)
      ZIP or postal code.

    - `individual.address_kanji.state` (string, nullable)
      Prefecture.

    - `individual.address_kanji.town` (string, nullable)
      Town/cho-me.

  - `individual.created` (timestamp)
    Time at which the object was created. Measured in seconds since the Unix epoch.

  - `individual.dob` (object, nullable)
    The individual’s date of birth.

    - `individual.dob.day` (integer, nullable)
      The day of birth, between 1 and 31.

    - `individual.dob.month` (integer, nullable)
      The month of birth, between 1 and 12.

    - `individual.dob.year` (integer, nullable)
      The four-digit year of birth.

  - `individual.email` (string, nullable)
    The individual’s email address. Also available for accounts where [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `stripe`.

  - `individual.first_name` (string, nullable)
    The individual’s first name. Also available for accounts where [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `stripe`.

  - `individual.first_name_kana` (string, nullable)
    The Kana variation of the individual’s first name (Japan only). Also available for accounts where [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `stripe`.

  - `individual.first_name_kanji` (string, nullable)
    The Kanji variation of the individual’s first name (Japan only). Also available for accounts where [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `stripe`.

  - `individual.full_name_aliases` (array of strings, nullable)
    A list of alternate names or aliases that the individual is known by. Also available for accounts where [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `stripe`.

  - `individual.future_requirements` (object, nullable)
    Information about the [upcoming new requirements for the individual](https://docs.stripe.com/docs/connect/custom-accounts/future-requirements.md), including what information needs to be collected, and by when.

    - `individual.future_requirements.alternatives` (array of objects, nullable)
      Fields that are due and can be resolved by providing the corresponding alternative fields instead. Many alternatives can list the same `original_fields_due`, and any of these alternatives can serve as a pathway for attempting to resolve the fields again. Re-providing `original_fields_due` also serves as a pathway for attempting to resolve the fields again.

      - `individual.future_requirements.alternatives.alternative_fields_due` (array of strings)
        Fields that can be provided to resolve all fields in `original_fields_due`.

      - `individual.future_requirements.alternatives.original_fields_due` (array of strings)
        Fields that are due and can be resolved by providing all fields in `alternative_fields_due`.

    - `individual.future_requirements.currently_due` (array of strings)
      Fields that need to be resolved to keep the person’s account enabled. If not resolved by the account’s `future_requirements[current_deadline]`, these fields will transition to the main `requirements` hash, and may immediately become `past_due`, but the account may also be given a grace period depending on the account’s enablement state prior to transition.

    - `individual.future_requirements.errors` (array of objects)
      Details about validation and verification failures for `due` requirements that must be resolved.

      - `individual.future_requirements.errors.code` (enum)
        The code for the type of error.
Possible enum values:
        - `information_missing`
          The requirement associated with this error is missing critical information. The associated error reason provides more details.

        - `invalid_address_city_state_postal_code`
          The combination of the city, state, and postal code in the provided address could not be validated.

        - `invalid_address_cmra_address`
          The address you provided appears to be associated with a mailbox or virtual address service, which we can’t accept. Please update your address to proceed.

        - `invalid_address_highway_contract_box`
          Invalid address. Your business address must be a valid physical address from which you conduct business and cannot be a Highway Contract Box.

        - `invalid_address_private_mailbox`
          Invalid address. Your business address must be a valid physical address from which you conduct business and cannot be a private mailbox.

        - `invalid_address_registered_agent_address`
          The address you provided appears to be associated with a registered agent, which we can’t accept. Please update your address to proceed. If you believe this is an error, you can submit a proof of address document for review.

        - `invalid_business_profile_name`
          Business profile names must consist of recognizable words.

        - `invalid_business_profile_name_denylisted`
          Generic or well-known business names aren’t supported.

        - `invalid_company_name_denylisted`
          Generic or well-known business names aren’t supported.

        - `invalid_dob_age_over_maximum`
          Date of birth must be within the past 120 years.

        - `invalid_dob_age_under_18`
          Underage. Age must be at least 18.

        - `invalid_dob_age_under_minimum`
          Person must be at least 13 years old.

        - `invalid_product_description_length`
          Your product description must be at least 10 characters.

        - `invalid_product_description_url_match`
          Your product description must be different from your URL.

        - `invalid_representative_country`
          The representative must have an address in the same country as the company.

        - `invalid_signator`
          We could not verify the professional certifying body of this document.

        - `invalid_statement_descriptor_business_mismatch`
          The statement descriptor must be similar to your business name, legal entity name, or URL.

        - `invalid_statement_descriptor_denylisted`
          Generic or well-known statement descriptors aren’t supported.

        - `invalid_statement_descriptor_length`
          The statement descriptor must be at least 5 characters.

        - `invalid_statement_descriptor_prefix_denylisted`
          Generic or well-known statement descriptor prefixes aren’t supported.

        - `invalid_statement_descriptor_prefix_mismatch`
          The statement descriptor prefix must be similar to your statement descriptor, business name, legal entity name, or URL.

        - `invalid_street_address`
          The street name and/or number for the provided address could not be validated.

        - `invalid_tax_id`
          The provided tax ID must have 9 digits

        - `invalid_tax_id_format`
          Tax IDs must be a unique set of 9 numbers without dashes or other special characters.

        - `invalid_tos_acceptance`
          The existing terms of service signature has been invalidated because the account’s tax ID has changed. The account needs to accept the terms of service again. For more information, see [this documentation](https://docs.stripe.com/connect/update-verified-information.md).

        - `invalid_url_denylisted`
          Generic business URLs aren’t supported.

        - `invalid_url_format`
          URL must be formatted as https://example.com.

        - `invalid_url_web_presence_detected`
          Because you use a website, app, social media page, or online profile to sell products or services, you must provide a URL for your business.

        - `invalid_url_website_business_information_mismatch`
          The business information on your website must match the details you provided to Stripe.

        - `invalid_url_website_empty`
          Your provided website appears to be empty.

        - `invalid_url_website_inaccessible`
          This URL couldn’t be reached. Make sure it’s available and entered correctly or provide another.

        - `invalid_url_website_inaccessible_geoblocked`
          Your provided website appears to be geographically blocked.

        - `invalid_url_website_inaccessible_password_protected`
          Your provided website appears to be password protected.

        - `invalid_url_website_incomplete`
          Your website seems to be missing some required information. [Learn about the requirements](https://support.stripe.com/questions/information-required-on-your-business-website-to-use-stripe)

        - `invalid_url_website_incomplete_cancellation_policy`
          Your provided website appears to have an incomplete cancellation policy.

        - `invalid_url_website_incomplete_customer_service_details`
          Your provided website appears to have incomplete customer service details.

        - `invalid_url_website_incomplete_legal_restrictions`
          Your provided website appears to have incomplete legal restrictions.

        - `invalid_url_website_incomplete_refund_policy`
          Your provided website appears to have an incomplete refund policy.

        - `invalid_url_website_incomplete_return_policy`
          Your provided website appears to have an incomplete refund policy.

        - `invalid_url_website_incomplete_terms_and_conditions`
          Your provided website appears to have incomplete terms and conditions.

        - `invalid_url_website_incomplete_under_construction`
          Your provided website appears to be incomplete or under construction.

        - `invalid_url_website_other`
          We weren’t able to verify your business using the URL you provided. Make sure it’s entered correctly or provide another URL.

        - `invalid_value_other`
          An invalid value was provided for the related field. This is a general error code.

        - `unsupported_business_type`
          The business type you provided isn’t supported in this country.

        - `verification_directors_mismatch`
          Directors on the account don’t match government records. Update the account and upload a directorship document with current directors.

        - `verification_document_address_mismatch`
          Address on the account doesn’t match the verification document. Update the account and upload the document again.

        - `verification_document_address_missing`
          The company address was missing on the document. Upload a document that includes the address.

        - `verification_document_corrupt`
          File seems to be corrupted or damaged. Provide a different file.

        - `verification_document_country_not_supported`
          Document isn’t supported in this person’s country or region. Provide a supported verification document.

        - `verification_document_directors_mismatch`
          Directors on the account don’t match the document provided. Update the account to match the registration document and upload it again.

        - `verification_document_dob_mismatch`
          The date of birth (DOB) on the document did not match the DOB on the account. Upload a document with a matching DOB or update the DOB on the account.

        - `verification_document_duplicate_type`
          The same type of document was used twice. Two unique types of documents are required for verification.

        - `verification_document_expired`
          The document could not be used for verification because it has expired. If it’s an identity document, its expiration date must be after the date the document was submitted. If it’s an address document, the issue date must be within the last six months.

        - `verification_document_failed_copy`
          Document is a photo or screenshot. Upload the original document.

        - `verification_document_failed_greyscale`
          Document seems to be in grayscale or black and white. Provide a full color photo of the document for verification.

        - `verification_document_failed_other`
          The document could not be verified for an unknown reason. Ensure that the document follows the [guidelines for document uploads](https://docs.stripe.com/acceptable-verification-documents.md).

        - `verification_document_failed_test_mode`
          A test data helper was supplied to simulate verification failure. Refer to the documentation for [test file tokens](https://docs.stripe.com/connect/testing.md#test-file-tokens).

        - `verification_document_fraudulent`
          Document seems to be altered. This could be because it’s fraudulent.

        - `verification_document_id_number_mismatch`
          Tax ID number on the account doesn’t match the verification document. Update the account to match the verification document and upload it again.

        - `verification_document_id_number_missing`
          The company ID number was missing on the document. Upload a document that includes the ID number.

        - `verification_document_incomplete`
          Document doesn’t include required information. Make sure all pages and sections are complete.

        - `verification_document_invalid`
          Document isn’t an acceptable form of identification in this account’s country or region. Ensure that the document follows the [guidelines for document uploads](https://docs.stripe.com/acceptable-verification-documents.md).

        - `verification_document_issue_or_expiry_date_missing`
          Document is missing an expiration date. Provide a document with an expiration date.

        - `verification_document_manipulated`
          Document seems to be altered. This could be because it’s fraudulent.

        - `verification_document_missing_back`
          The back of the document is missing. Provide both sides of the document for verification.

        - `verification_document_missing_front`
          The front of the document is missing. Provide both sides of the document for verification.

        - `verification_document_name_mismatch`
          The name on the account does not match the name on the document. Update the account to match the document and upload it again.

        - `verification_document_name_missing`
          The company name was missing on the document. Upload a document that includes the company name.

        - `verification_document_nationality_mismatch`
          The nationality on the document did not match the person’s stated nationality. Update the person’s stated nationality, or upload a document that matches it.

        - `verification_document_not_readable`
          Document isn’t readable. This could be because it’s blurry or dark, or because the document was obstructed.

        - `verification_document_not_signed`
          Document doesn’t seem to be signed. Provide a signed document.

        - `verification_document_not_uploaded`
          Document didn’t upload because of a problem with the file.

        - `verification_document_photo_mismatch`
          ID photo on the document doesn’t match the selfie provided by this account.

        - `verification_document_too_large`
          Document file is too large. Upload one that’s 10MB or less.

        - `verification_document_type_not_supported`
          The provided document type is not accepted. Ensure that the document follows the [guidelines for document uploads](https://docs.stripe.com/acceptable-verification-documents.md).

        - `verification_extraneous_directors`
          Extraneous directors have been added to the account. Update the account and upload a registration document with current directors.

        - `verification_failed_address_match`
          The address on the account could not be verified. Correct any errors in the address field or upload a document that includes the address.

        - `verification_failed_authorizer_authority`
          The account authorizer is not a registered authorized representative. Refer to [this support article](https://support.stripe.com/questions/representative-authority-verification) for more information.

        - `verification_failed_business_iec_number`
          The Importer Exporter Code (IEC) number on your account could not be verified. Either correct any possible errors in the company name or IEC number. Refer to the support article for [accepting international payments in India](https://support.stripe.com/questions/accepting-international-payments-from-stripe-accounts-in-india).

        - `verification_failed_document_match`
          The document could not be verified. Upload a document that includes the company name, ID number, and address fields.

        - `verification_failed_id_number_match`
          ID number on the document doesn’t match the ID number provided by this account.

        - `verification_failed_keyed_identity`
          The person’s keyed-in identity information could not be verified. Correct any errors or upload a document that matches the identity fields (e.g., name and date of birth) entered.

        - `verification_failed_keyed_match`
          The keyed-in information on the account could not be verified. Correct any errors in the company name, ID number, or address fields. You can also upload a document that includes those fields.

        - `verification_failed_name_match`
          The company name on the account could not be verified. Correct any errors in the company name field or upload a document that includes the company name.

        - `verification_failed_other`
          Verification failed for an unknown reason. Correct any errors and resubmit the required fields.

        - `verification_failed_representative_authority`
          The authority of the account representative could not be verified. Please change the account representative to a person who is registered as an authorized representative. Please refer to [this support article](https://support.stripe.com/questions/representative-authority-verification).

        - `verification_failed_residential_address`
          We could not verify that the person resides at the provided address. The address must be a valid physical address where the individual resides and cannot be a P.O. Box.

        - `verification_failed_tax_id_match`
          The tax ID on the account cannot be verified by the IRS. Either correct any possible errors in the company name or tax ID, or upload a document that contains those fields.

        - `verification_failed_tax_id_not_issued`
          The tax ID on the account was not recognized by the IRS. Refer to the support article for [newly-issued tax ID numbers](https://support.stripe.com/questions/newly-issued-us-tax-id-number-tin-not-verifying).

        - `verification_legal_entity_structure_mismatch`
          Business type or structure seems to be incorrect. Provide the correct business type and structure for this account.

        - `verification_missing_directors`
          We identified that your business has directors that have not been added to the account. Please add missing directors to your account.

        - `verification_missing_executives`
          We have identified executives that haven’t been added on the account. Add any missing executives to the account.

        - `verification_missing_owners`
          We have identified owners that haven’t been added on the account. Add any missing owners to the account.

        - `verification_rejected_ownership_exemption_reason`
          The ownership exemption reason was rejected.

        - `verification_requires_additional_memorandum_of_associations`
          We have identified holding companies with significant percentage ownership. Upload a Memorandum of Association for each of the holding companies.

        - `verification_requires_additional_proof_of_registration`
          The uploaded document contains holding companies with significant percentage ownership. Upload a proof of registration for each of the holding companies.

        - `verification_supportability`
          We can’t accept payments for this business under the Stripe Services Agreement without additional verification, as mentioned in the [prohibited and restricted businesses list](https://stripe.com/legal/restricted-businesses).

      - `individual.future_requirements.errors.reason` (string)
        An informative message that indicates the error type and provides additional details about the error.

      - `individual.future_requirements.errors.requirement` (string)
        The specific user onboarding requirement field (in the requirements hash) that needs to be resolved.

    - `individual.future_requirements.eventually_due` (array of strings)
      Fields you must collect when all thresholds are reached. As they become required, they appear in `currently_due` as well, and the account’s `future_requirements[current_deadline]` becomes set.

    - `individual.future_requirements.past_due` (array of strings)
      Fields that haven’t been resolved by the account’s `requirements.current_deadline`. These fields need to be resolved to enable the person’s account. `future_requirements.past_due` is a subset of `requirements.past_due`.

    - `individual.future_requirements.pending_verification` (array of strings)
      Fields that are being reviewed, or might become required depending on the results of a review. If the review fails, these fields can move to `eventually_due`, `currently_due`, `past_due` or `alternatives`. Fields might appear in `eventually_due`, `currently_due`, `past_due` or `alternatives` and in `pending_verification` if one verification fails but another is still pending.

  - `individual.gender` (enum, nullable)
    The individual’s gender.

  - `individual.id_number_provided` (boolean)
    Whether the individual’s personal ID number was provided. True if either the full ID number was provided or if only the required part of the ID number was provided (ex. last four of an individual’s SSN for the US indicated by `ssn_last_4_provided`).

  - `individual.id_number_secondary_provided` (boolean, nullable)
    Whether the individual’s personal secondary ID number was provided.

  - `individual.last_name` (string, nullable)
    The individual’s last name. Also available for accounts where [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `stripe`.

  - `individual.last_name_kana` (string, nullable)
    The Kana varation of the individual’s last name (Japan only). Also available for accounts where [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `stripe`.

  - `individual.last_name_kanji` (string, nullable)
    The Kanji varation of the individual’s last name (Japan only). Also available for accounts where [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `stripe`.

  - `individual.maiden_name` (string, nullable)
    The individual’s maiden name.

  - `individual.metadata` (object)
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

  - `individual.nationality` (string, nullable)
    The country where the person is a national.

  - `individual.phone` (string, nullable)
    The individual’s phone number.

  - `individual.political_exposure` (enum, nullable)
    Indicates if the person or any of their representatives, family members, or other closely related persons, declares that they hold or have held an important public job or function, in any jurisdiction.
Possible enum values:
    - `existing`
      The person has disclosed that they do have political exposure

    - `none`
      The person has disclosed that they have no political exposure

  - `individual.registered_address` (object, nullable)
    The individual’s registered address.

    - `individual.registered_address.city` (string, nullable)
      City, district, suburb, town, or village.

    - `individual.registered_address.country` (string, nullable)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `individual.registered_address.line1` (string, nullable)
      Address line 1, such as the street, PO Box, or company name.

    - `individual.registered_address.line2` (string, nullable)
      Address line 2, such as the apartment, suite, unit, or building.

    - `individual.registered_address.postal_code` (string, nullable)
      ZIP or postal code.

    - `individual.registered_address.state` (string, nullable)
      State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

  - `individual.relationship` (object)
    Describes the individual’s relationship to the account. Also available for accounts where [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `stripe`.

    - `individual.relationship.authorizer` (boolean, nullable)
      Whether the person is the authorizer of the account’s representative.

    - `individual.relationship.director` (boolean, nullable)
      Whether the person is a director of the account’s legal entity. Directors are typically members of the governing board of the company, or responsible for ensuring the company meets its regulatory obligations.

    - `individual.relationship.executive` (boolean, nullable)
      Whether the person has significant responsibility to control, manage, or direct the organization.

    - `individual.relationship.legal_guardian` (boolean, nullable)
      Whether the person is the legal guardian of the account’s representative.

    - `individual.relationship.owner` (boolean, nullable)
      Whether the person is an owner of the account’s legal entity.

    - `individual.relationship.percent_ownership` (float, nullable)
      The percent owned by the person of the account’s legal entity.

    - `individual.relationship.representative` (boolean, nullable)
      Whether the person is authorized as the primary representative of the account. This is the person nominated by the business to provide information about themselves, and general information about the account. There can only be one representative at any given time. At the time the account is created, this person should be set to the person responsible for opening the account.

    - `individual.relationship.title` (string, nullable)
      The person’s title (e.g., CEO, Support Engineer).

  - `individual.requirements` (object, nullable)
    Information about the requirements for the individual, including what information needs to be collected, and by when.

    - `individual.requirements.alternatives` (array of objects, nullable)
      Fields that are due and can be resolved by providing the corresponding alternative fields instead. Many alternatives can list the same `original_fields_due`, and any of these alternatives can serve as a pathway for attempting to resolve the fields again. Re-providing `original_fields_due` also serves as a pathway for attempting to resolve the fields again.

      - `individual.requirements.alternatives.alternative_fields_due` (array of strings)
        Fields that can be provided to resolve all fields in `original_fields_due`.

      - `individual.requirements.alternatives.original_fields_due` (array of strings)
        Fields that are due and can be resolved by providing all fields in `alternative_fields_due`.

    - `individual.requirements.currently_due` (array of strings)
      Fields that need to be resolved to keep the person’s account enabled. If not resolved by the account’s `current_deadline`, these fields will appear in `past_due` as well, and the account is disabled.

    - `individual.requirements.errors` (array of objects)
      Details about validation and verification failures for `due` requirements that must be resolved.

      - `individual.requirements.errors.code` (enum)
        The code for the type of error.
Possible enum values:
        - `information_missing`
          The requirement associated with this error is missing critical information. The associated error reason provides more details.

        - `invalid_address_city_state_postal_code`
          The combination of the city, state, and postal code in the provided address could not be validated.

        - `invalid_address_cmra_address`
          The address you provided appears to be associated with a mailbox or virtual address service, which we can’t accept. Please update your address to proceed.

        - `invalid_address_highway_contract_box`
          Invalid address. Your business address must be a valid physical address from which you conduct business and cannot be a Highway Contract Box.

        - `invalid_address_private_mailbox`
          Invalid address. Your business address must be a valid physical address from which you conduct business and cannot be a private mailbox.

        - `invalid_address_registered_agent_address`
          The address you provided appears to be associated with a registered agent, which we can’t accept. Please update your address to proceed. If you believe this is an error, you can submit a proof of address document for review.

        - `invalid_business_profile_name`
          Business profile names must consist of recognizable words.

        - `invalid_business_profile_name_denylisted`
          Generic or well-known business names aren’t supported.

        - `invalid_company_name_denylisted`
          Generic or well-known business names aren’t supported.

        - `invalid_dob_age_over_maximum`
          Date of birth must be within the past 120 years.

        - `invalid_dob_age_under_18`
          Underage. Age must be at least 18.

        - `invalid_dob_age_under_minimum`
          Person must be at least 13 years old.

        - `invalid_product_description_length`
          Your product description must be at least 10 characters.

        - `invalid_product_description_url_match`
          Your product description must be different from your URL.

        - `invalid_representative_country`
          The representative must have an address in the same country as the company.

        - `invalid_signator`
          We could not verify the professional certifying body of this document.

        - `invalid_statement_descriptor_business_mismatch`
          The statement descriptor must be similar to your business name, legal entity name, or URL.

        - `invalid_statement_descriptor_denylisted`
          Generic or well-known statement descriptors aren’t supported.

        - `invalid_statement_descriptor_length`
          The statement descriptor must be at least 5 characters.

        - `invalid_statement_descriptor_prefix_denylisted`
          Generic or well-known statement descriptor prefixes aren’t supported.

        - `invalid_statement_descriptor_prefix_mismatch`
          The statement descriptor prefix must be similar to your statement descriptor, business name, legal entity name, or URL.

        - `invalid_street_address`
          The street name and/or number for the provided address could not be validated.

        - `invalid_tax_id`
          The provided tax ID must have 9 digits

        - `invalid_tax_id_format`
          Tax IDs must be a unique set of 9 numbers without dashes or other special characters.

        - `invalid_tos_acceptance`
          The existing terms of service signature has been invalidated because the account’s tax ID has changed. The account needs to accept the terms of service again. For more information, see [this documentation](https://docs.stripe.com/connect/update-verified-information.md).

        - `invalid_url_denylisted`
          Generic business URLs aren’t supported.

        - `invalid_url_format`
          URL must be formatted as https://example.com.

        - `invalid_url_web_presence_detected`
          Because you use a website, app, social media page, or online profile to sell products or services, you must provide a URL for your business.

        - `invalid_url_website_business_information_mismatch`
          The business information on your website must match the details you provided to Stripe.

        - `invalid_url_website_empty`
          Your provided website appears to be empty.

        - `invalid_url_website_inaccessible`
          This URL couldn’t be reached. Make sure it’s available and entered correctly or provide another.

        - `invalid_url_website_inaccessible_geoblocked`
          Your provided website appears to be geographically blocked.

        - `invalid_url_website_inaccessible_password_protected`
          Your provided website appears to be password protected.

        - `invalid_url_website_incomplete`
          Your website seems to be missing some required information. [Learn about the requirements](https://support.stripe.com/questions/information-required-on-your-business-website-to-use-stripe)

        - `invalid_url_website_incomplete_cancellation_policy`
          Your provided website appears to have an incomplete cancellation policy.

        - `invalid_url_website_incomplete_customer_service_details`
          Your provided website appears to have incomplete customer service details.

        - `invalid_url_website_incomplete_legal_restrictions`
          Your provided website appears to have incomplete legal restrictions.

        - `invalid_url_website_incomplete_refund_policy`
          Your provided website appears to have an incomplete refund policy.

        - `invalid_url_website_incomplete_return_policy`
          Your provided website appears to have an incomplete refund policy.

        - `invalid_url_website_incomplete_terms_and_conditions`
          Your provided website appears to have incomplete terms and conditions.

        - `invalid_url_website_incomplete_under_construction`
          Your provided website appears to be incomplete or under construction.

        - `invalid_url_website_other`
          We weren’t able to verify your business using the URL you provided. Make sure it’s entered correctly or provide another URL.

        - `invalid_value_other`
          An invalid value was provided for the related field. This is a general error code.

        - `unsupported_business_type`
          The business type you provided isn’t supported in this country.

        - `verification_directors_mismatch`
          Directors on the account don’t match government records. Update the account and upload a directorship document with current directors.

        - `verification_document_address_mismatch`
          Address on the account doesn’t match the verification document. Update the account and upload the document again.

        - `verification_document_address_missing`
          The company address was missing on the document. Upload a document that includes the address.

        - `verification_document_corrupt`
          File seems to be corrupted or damaged. Provide a different file.

        - `verification_document_country_not_supported`
          Document isn’t supported in this person’s country or region. Provide a supported verification document.

        - `verification_document_directors_mismatch`
          Directors on the account don’t match the document provided. Update the account to match the registration document and upload it again.

        - `verification_document_dob_mismatch`
          The date of birth (DOB) on the document did not match the DOB on the account. Upload a document with a matching DOB or update the DOB on the account.

        - `verification_document_duplicate_type`
          The same type of document was used twice. Two unique types of documents are required for verification.

        - `verification_document_expired`
          The document could not be used for verification because it has expired. If it’s an identity document, its expiration date must be after the date the document was submitted. If it’s an address document, the issue date must be within the last six months.

        - `verification_document_failed_copy`
          Document is a photo or screenshot. Upload the original document.

        - `verification_document_failed_greyscale`
          Document seems to be in grayscale or black and white. Provide a full color photo of the document for verification.

        - `verification_document_failed_other`
          The document could not be verified for an unknown reason. Ensure that the document follows the [guidelines for document uploads](https://docs.stripe.com/acceptable-verification-documents.md).

        - `verification_document_failed_test_mode`
          A test data helper was supplied to simulate verification failure. Refer to the documentation for [test file tokens](https://docs.stripe.com/connect/testing.md#test-file-tokens).

        - `verification_document_fraudulent`
          Document seems to be altered. This could be because it’s fraudulent.

        - `verification_document_id_number_mismatch`
          Tax ID number on the account doesn’t match the verification document. Update the account to match the verification document and upload it again.

        - `verification_document_id_number_missing`
          The company ID number was missing on the document. Upload a document that includes the ID number.

        - `verification_document_incomplete`
          Document doesn’t include required information. Make sure all pages and sections are complete.

        - `verification_document_invalid`
          Document isn’t an acceptable form of identification in this account’s country or region. Ensure that the document follows the [guidelines for document uploads](https://docs.stripe.com/acceptable-verification-documents.md).

        - `verification_document_issue_or_expiry_date_missing`
          Document is missing an expiration date. Provide a document with an expiration date.

        - `verification_document_manipulated`
          Document seems to be altered. This could be because it’s fraudulent.

        - `verification_document_missing_back`
          The back of the document is missing. Provide both sides of the document for verification.

        - `verification_document_missing_front`
          The front of the document is missing. Provide both sides of the document for verification.

        - `verification_document_name_mismatch`
          The name on the account does not match the name on the document. Update the account to match the document and upload it again.

        - `verification_document_name_missing`
          The company name was missing on the document. Upload a document that includes the company name.

        - `verification_document_nationality_mismatch`
          The nationality on the document did not match the person’s stated nationality. Update the person’s stated nationality, or upload a document that matches it.

        - `verification_document_not_readable`
          Document isn’t readable. This could be because it’s blurry or dark, or because the document was obstructed.

        - `verification_document_not_signed`
          Document doesn’t seem to be signed. Provide a signed document.

        - `verification_document_not_uploaded`
          Document didn’t upload because of a problem with the file.

        - `verification_document_photo_mismatch`
          ID photo on the document doesn’t match the selfie provided by this account.

        - `verification_document_too_large`
          Document file is too large. Upload one that’s 10MB or less.

        - `verification_document_type_not_supported`
          The provided document type is not accepted. Ensure that the document follows the [guidelines for document uploads](https://docs.stripe.com/acceptable-verification-documents.md).

        - `verification_extraneous_directors`
          Extraneous directors have been added to the account. Update the account and upload a registration document with current directors.

        - `verification_failed_address_match`
          The address on the account could not be verified. Correct any errors in the address field or upload a document that includes the address.

        - `verification_failed_authorizer_authority`
          The account authorizer is not a registered authorized representative. Refer to [this support article](https://support.stripe.com/questions/representative-authority-verification) for more information.

        - `verification_failed_business_iec_number`
          The Importer Exporter Code (IEC) number on your account could not be verified. Either correct any possible errors in the company name or IEC number. Refer to the support article for [accepting international payments in India](https://support.stripe.com/questions/accepting-international-payments-from-stripe-accounts-in-india).

        - `verification_failed_document_match`
          The document could not be verified. Upload a document that includes the company name, ID number, and address fields.

        - `verification_failed_id_number_match`
          ID number on the document doesn’t match the ID number provided by this account.

        - `verification_failed_keyed_identity`
          The person’s keyed-in identity information could not be verified. Correct any errors or upload a document that matches the identity fields (e.g., name and date of birth) entered.

        - `verification_failed_keyed_match`
          The keyed-in information on the account could not be verified. Correct any errors in the company name, ID number, or address fields. You can also upload a document that includes those fields.

        - `verification_failed_name_match`
          The company name on the account could not be verified. Correct any errors in the company name field or upload a document that includes the company name.

        - `verification_failed_other`
          Verification failed for an unknown reason. Correct any errors and resubmit the required fields.

        - `verification_failed_representative_authority`
          The authority of the account representative could not be verified. Please change the account representative to a person who is registered as an authorized representative. Please refer to [this support article](https://support.stripe.com/questions/representative-authority-verification).

        - `verification_failed_residential_address`
          We could not verify that the person resides at the provided address. The address must be a valid physical address where the individual resides and cannot be a P.O. Box.

        - `verification_failed_tax_id_match`
          The tax ID on the account cannot be verified by the IRS. Either correct any possible errors in the company name or tax ID, or upload a document that contains those fields.

        - `verification_failed_tax_id_not_issued`
          The tax ID on the account was not recognized by the IRS. Refer to the support article for [newly-issued tax ID numbers](https://support.stripe.com/questions/newly-issued-us-tax-id-number-tin-not-verifying).

        - `verification_legal_entity_structure_mismatch`
          Business type or structure seems to be incorrect. Provide the correct business type and structure for this account.

        - `verification_missing_directors`
          We identified that your business has directors that have not been added to the account. Please add missing directors to your account.

        - `verification_missing_executives`
          We have identified executives that haven’t been added on the account. Add any missing executives to the account.

        - `verification_missing_owners`
          We have identified owners that haven’t been added on the account. Add any missing owners to the account.

        - `verification_rejected_ownership_exemption_reason`
          The ownership exemption reason was rejected.

        - `verification_requires_additional_memorandum_of_associations`
          We have identified holding companies with significant percentage ownership. Upload a Memorandum of Association for each of the holding companies.

        - `verification_requires_additional_proof_of_registration`
          The uploaded document contains holding companies with significant percentage ownership. Upload a proof of registration for each of the holding companies.

        - `verification_supportability`
          We can’t accept payments for this business under the Stripe Services Agreement without additional verification, as mentioned in the [prohibited and restricted businesses list](https://stripe.com/legal/restricted-businesses).

      - `individual.requirements.errors.reason` (string)
        An informative message that indicates the error type and provides additional details about the error.

      - `individual.requirements.errors.requirement` (string)
        The specific user onboarding requirement field (in the requirements hash) that needs to be resolved.

    - `individual.requirements.eventually_due` (array of strings)
      Fields you must collect when all thresholds are reached. As they become required, they appear in `currently_due` as well, and the account’s `current_deadline` becomes set.

    - `individual.requirements.past_due` (array of strings)
      Fields that haven’t been resolved by `current_deadline`. These fields need to be resolved to enable the person’s account.

    - `individual.requirements.pending_verification` (array of strings)
      Fields that are being reviewed, or might become required depending on the results of a review. If the review fails, these fields can move to `eventually_due`, `currently_due`, `past_due` or `alternatives`. Fields might appear in `eventually_due`, `currently_due`, `past_due` or `alternatives` and in `pending_verification` if one verification fails but another is still pending.

  - `individual.ssn_last_4_provided` (boolean)
    Whether the last four digits of the individual’s Social Security number have been provided (U.S. only).

  - `individual.verification` (object)
    The individual’s verification status.

    - `individual.verification.additional_document` (object, nullable)
      A document showing address, either a passport, local ID card, or utility bill from a well-known utility company.

      - `individual.verification.additional_document.back` (string, nullable)
        The back of an ID returned by a [file upload](https://docs.stripe.com/api/accounts/object.md#create_file) with a `purpose` value of `identity_document`.

      - `individual.verification.additional_document.details` (string, nullable)
        A user-displayable string describing the verification state of this document. For example, if a document is uploaded and the picture is too fuzzy, this may say “Identity document is too unclear to read”.

      - `individual.verification.additional_document.details_code` (string, nullable)
        One of `document_corrupt`, `document_country_not_supported`, `document_expired`, `document_failed_copy`, `document_failed_other`, `document_failed_test_mode`, `document_fraudulent`, `document_failed_greyscale`, `document_incomplete`, `document_invalid`, `document_manipulated`, `document_missing_back`, `document_missing_front`, `document_not_readable`, `document_not_uploaded`, `document_photo_mismatch`, `document_too_large`, or `document_type_not_supported`. A machine-readable code specifying the verification state for this document.

      - `individual.verification.additional_document.front` (string, nullable)
        The front of an ID returned by a [file upload](https://docs.stripe.com/api/accounts/object.md#create_file) with a `purpose` value of `identity_document`.

    - `individual.verification.details` (string, nullable)
      A user-displayable string describing the verification state for the person. For example, this may say “Provided identity information could not be verified”.

    - `individual.verification.details_code` (string, nullable)
      One of `document_address_mismatch`, `document_dob_mismatch`, `document_duplicate_type`, `document_id_number_mismatch`, `document_name_mismatch`, `document_nationality_mismatch`, `failed_keyed_identity`, or `failed_other`. A machine-readable code specifying the verification state for the person.

    - `individual.verification.document` (object)
      An identifying document for the person, either a passport or local ID card.

      - `individual.verification.document.back` (string, nullable)
        The back of an ID returned by a [file upload](https://docs.stripe.com/api/accounts/object.md#create_file) with a `purpose` value of `identity_document`.

      - `individual.verification.document.details` (string, nullable)
        A user-displayable string describing the verification state of this document. For example, if a document is uploaded and the picture is too fuzzy, this may say “Identity document is too unclear to read”.

      - `individual.verification.document.details_code` (string, nullable)
        One of `document_corrupt`, `document_country_not_supported`, `document_expired`, `document_failed_copy`, `document_failed_other`, `document_failed_test_mode`, `document_fraudulent`, `document_failed_greyscale`, `document_incomplete`, `document_invalid`, `document_manipulated`, `document_missing_back`, `document_missing_front`, `document_not_readable`, `document_not_uploaded`, `document_photo_mismatch`, `document_too_large`, or `document_type_not_supported`. A machine-readable code specifying the verification state for this document.

      - `individual.verification.document.front` (string, nullable)
        The front of an ID returned by a [file upload](https://docs.stripe.com/api/accounts/object.md#create_file) with a `purpose` value of `identity_document`.

    - `individual.verification.status` (string)
      The state of verification for the person. Possible values are `unverified`, `pending`, or `verified`. Please refer [guide](https://docs.stripe.com/docs/connect/handling-api-verification.md) to handle verification updates.

- `metadata` (object, nullable)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `payouts_enabled` (boolean)
  Whether the funds in this account can be paid out.

- `requirements` (object, nullable)
  Details about the requirements for the account, including what information needs to be collected, verified, or reviewed, and by when. After a requirement is collected, verified, or reviewed, it is considered resolved. Most requirements can be addressed programmatically, however, some must be completed through a form or challenge using the Stripe Interface. [Learn more about handling requirements](https://docs.stripe.com/docs/connect/handling-api-verification.md).

  - `requirements.alternatives` (array of objects, nullable)
    Fields that are due and can be resolved by providing the corresponding alternative fields instead. Many alternatives can list the same `original_fields_due`, and any of these alternatives can serve as a pathway for attempting to resolve the fields again. Re-providing `original_fields_due` also serves as a pathway for attempting to resolve the fields again.

    - `requirements.alternatives.alternative_fields_due` (array of strings)
      Fields that can be provided to resolve all fields in `original_fields_due`.

    - `requirements.alternatives.original_fields_due` (array of strings)
      Fields that are due and can be resolved by providing all fields in `alternative_fields_due`.

  - `requirements.current_deadline` (timestamp, nullable)
    Date by which the fields in `currently_due` must be collected to keep the account enabled. These fields may disable the account sooner if the next threshold is reached before they are collected.

  - `requirements.currently_due` (array of strings, nullable)
    Fields that need to be resolved to keep the account enabled. If not resolved by `current_deadline`, these fields will appear in `past_due` as well, and the account is disabled.

  - `requirements.disabled_reason` (enum, nullable)
    If the account is disabled, this enum describes why. [Learn more about handling verification issues](https://docs.stripe.com/docs/connect/handling-api-verification.md).
Possible enum values:
    - `action_required.requested_capabilities`
      The account has been disabled because its requested capabilities require action.

    - `listed`
      The account has been listed.

    - `other`
      The account has been disabled for another reason.

    - `platform_paused`
      The account has been paused by the platform.

    - `rejected.fraud`
      The account has been rejected for fraud.

    - `rejected.incomplete_verification`
      The account has been rejected for incomplete verification.

    - `rejected.listed`
      The account has been rejected because it is listed.

    - `rejected.other`
      The account has been rejected for another reason.

    - `rejected.platform_fraud`
      The account has been rejected by the platform for fraud.

    - `rejected.platform_other`
      The account has been rejected by the platform.

    - `rejected.platform_terms_of_service`
      The account has been rejected by the platform for violating the Stripe services agreement.

    - `rejected.terms_of_service`
      The account has been rejected because it does not meet Stripe’s terms of service.

    - `requirements.past_due`
      The account has been disabled because requirements are past_due.

    - `requirements.pending_verification`
      The account has been disabled because requirements are pending verification.

    - `under_review`
      The account has been disabled because it is under review.

  - `requirements.errors` (array of objects, nullable)
    Details about validation and verification failures for `due` requirements that must be resolved.

    - `requirements.errors.code` (enum)
      The code for the type of error.
Possible enum values:
      - `information_missing`
        The requirement associated with this error is missing critical information. The associated error reason provides more details.

      - `invalid_address_city_state_postal_code`
        The combination of the city, state, and postal code in the provided address could not be validated.

      - `invalid_address_cmra_address`
        The address you provided appears to be associated with a mailbox or virtual address service, which we can’t accept. Please update your address to proceed.

      - `invalid_address_highway_contract_box`
        Invalid address. Your business address must be a valid physical address from which you conduct business and cannot be a Highway Contract Box.

      - `invalid_address_private_mailbox`
        Invalid address. Your business address must be a valid physical address from which you conduct business and cannot be a private mailbox.

      - `invalid_address_registered_agent_address`
        The address you provided appears to be associated with a registered agent, which we can’t accept. Please update your address to proceed. If you believe this is an error, you can submit a proof of address document for review.

      - `invalid_business_profile_name`
        Business profile names must consist of recognizable words.

      - `invalid_business_profile_name_denylisted`
        Generic or well-known business names aren’t supported.

      - `invalid_company_name_denylisted`
        Generic or well-known business names aren’t supported.

      - `invalid_dob_age_over_maximum`
        Date of birth must be within the past 120 years.

      - `invalid_dob_age_under_18`
        Underage. Age must be at least 18.

      - `invalid_dob_age_under_minimum`
        Person must be at least 13 years old.

      - `invalid_product_description_length`
        Your product description must be at least 10 characters.

      - `invalid_product_description_url_match`
        Your product description must be different from your URL.

      - `invalid_representative_country`
        The representative must have an address in the same country as the company.

      - `invalid_signator`
        We could not verify the professional certifying body of this document.

      - `invalid_statement_descriptor_business_mismatch`
        The statement descriptor must be similar to your business name, legal entity name, or URL.

      - `invalid_statement_descriptor_denylisted`
        Generic or well-known statement descriptors aren’t supported.

      - `invalid_statement_descriptor_length`
        The statement descriptor must be at least 5 characters.

      - `invalid_statement_descriptor_prefix_denylisted`
        Generic or well-known statement descriptor prefixes aren’t supported.

      - `invalid_statement_descriptor_prefix_mismatch`
        The statement descriptor prefix must be similar to your statement descriptor, business name, legal entity name, or URL.

      - `invalid_street_address`
        The street name and/or number for the provided address could not be validated.

      - `invalid_tax_id`
        The provided tax ID must have 9 digits

      - `invalid_tax_id_format`
        Tax IDs must be a unique set of 9 numbers without dashes or other special characters.

      - `invalid_tos_acceptance`
        The existing terms of service signature has been invalidated because the account’s tax ID has changed. The account needs to accept the terms of service again. For more information, see [this documentation](https://docs.stripe.com/connect/update-verified-information.md).

      - `invalid_url_denylisted`
        Generic business URLs aren’t supported.

      - `invalid_url_format`
        URL must be formatted as https://example.com.

      - `invalid_url_web_presence_detected`
        Because you use a website, app, social media page, or online profile to sell products or services, you must provide a URL for your business.

      - `invalid_url_website_business_information_mismatch`
        The business information on your website must match the details you provided to Stripe.

      - `invalid_url_website_empty`
        Your provided website appears to be empty.

      - `invalid_url_website_inaccessible`
        This URL couldn’t be reached. Make sure it’s available and entered correctly or provide another.

      - `invalid_url_website_inaccessible_geoblocked`
        Your provided website appears to be geographically blocked.

      - `invalid_url_website_inaccessible_password_protected`
        Your provided website appears to be password protected.

      - `invalid_url_website_incomplete`
        Your website seems to be missing some required information. [Learn about the requirements](https://support.stripe.com/questions/information-required-on-your-business-website-to-use-stripe)

      - `invalid_url_website_incomplete_cancellation_policy`
        Your provided website appears to have an incomplete cancellation policy.

      - `invalid_url_website_incomplete_customer_service_details`
        Your provided website appears to have incomplete customer service details.

      - `invalid_url_website_incomplete_legal_restrictions`
        Your provided website appears to have incomplete legal restrictions.

      - `invalid_url_website_incomplete_refund_policy`
        Your provided website appears to have an incomplete refund policy.

      - `invalid_url_website_incomplete_return_policy`
        Your provided website appears to have an incomplete refund policy.

      - `invalid_url_website_incomplete_terms_and_conditions`
        Your provided website appears to have incomplete terms and conditions.

      - `invalid_url_website_incomplete_under_construction`
        Your provided website appears to be incomplete or under construction.

      - `invalid_url_website_other`
        We weren’t able to verify your business using the URL you provided. Make sure it’s entered correctly or provide another URL.

      - `invalid_value_other`
        An invalid value was provided for the related field. This is a general error code.

      - `unsupported_business_type`
        The business type you provided isn’t supported in this country.

      - `verification_directors_mismatch`
        Directors on the account don’t match government records. Update the account and upload a directorship document with current directors.

      - `verification_document_address_mismatch`
        Address on the account doesn’t match the verification document. Update the account and upload the document again.

      - `verification_document_address_missing`
        The company address was missing on the document. Upload a document that includes the address.

      - `verification_document_corrupt`
        File seems to be corrupted or damaged. Provide a different file.

      - `verification_document_country_not_supported`
        Document isn’t supported in this person’s country or region. Provide a supported verification document.

      - `verification_document_directors_mismatch`
        Directors on the account don’t match the document provided. Update the account to match the registration document and upload it again.

      - `verification_document_dob_mismatch`
        The date of birth (DOB) on the document did not match the DOB on the account. Upload a document with a matching DOB or update the DOB on the account.

      - `verification_document_duplicate_type`
        The same type of document was used twice. Two unique types of documents are required for verification.

      - `verification_document_expired`
        The document could not be used for verification because it has expired. If it’s an identity document, its expiration date must be after the date the document was submitted. If it’s an address document, the issue date must be within the last six months.

      - `verification_document_failed_copy`
        Document is a photo or screenshot. Upload the original document.

      - `verification_document_failed_greyscale`
        Document seems to be in grayscale or black and white. Provide a full color photo of the document for verification.

      - `verification_document_failed_other`
        The document could not be verified for an unknown reason. Ensure that the document follows the [guidelines for document uploads](https://docs.stripe.com/acceptable-verification-documents.md).

      - `verification_document_failed_test_mode`
        A test data helper was supplied to simulate verification failure. Refer to the documentation for [test file tokens](https://docs.stripe.com/connect/testing.md#test-file-tokens).

      - `verification_document_fraudulent`
        Document seems to be altered. This could be because it’s fraudulent.

      - `verification_document_id_number_mismatch`
        Tax ID number on the account doesn’t match the verification document. Update the account to match the verification document and upload it again.

      - `verification_document_id_number_missing`
        The company ID number was missing on the document. Upload a document that includes the ID number.

      - `verification_document_incomplete`
        Document doesn’t include required information. Make sure all pages and sections are complete.

      - `verification_document_invalid`
        Document isn’t an acceptable form of identification in this account’s country or region. Ensure that the document follows the [guidelines for document uploads](https://docs.stripe.com/acceptable-verification-documents.md).

      - `verification_document_issue_or_expiry_date_missing`
        Document is missing an expiration date. Provide a document with an expiration date.

      - `verification_document_manipulated`
        Document seems to be altered. This could be because it’s fraudulent.

      - `verification_document_missing_back`
        The back of the document is missing. Provide both sides of the document for verification.

      - `verification_document_missing_front`
        The front of the document is missing. Provide both sides of the document for verification.

      - `verification_document_name_mismatch`
        The name on the account does not match the name on the document. Update the account to match the document and upload it again.

      - `verification_document_name_missing`
        The company name was missing on the document. Upload a document that includes the company name.

      - `verification_document_nationality_mismatch`
        The nationality on the document did not match the person’s stated nationality. Update the person’s stated nationality, or upload a document that matches it.

      - `verification_document_not_readable`
        Document isn’t readable. This could be because it’s blurry or dark, or because the document was obstructed.

      - `verification_document_not_signed`
        Document doesn’t seem to be signed. Provide a signed document.

      - `verification_document_not_uploaded`
        Document didn’t upload because of a problem with the file.

      - `verification_document_photo_mismatch`
        ID photo on the document doesn’t match the selfie provided by this account.

      - `verification_document_too_large`
        Document file is too large. Upload one that’s 10MB or less.

      - `verification_document_type_not_supported`
        The provided document type is not accepted. Ensure that the document follows the [guidelines for document uploads](https://docs.stripe.com/acceptable-verification-documents.md).

      - `verification_extraneous_directors`
        Extraneous directors have been added to the account. Update the account and upload a registration document with current directors.

      - `verification_failed_address_match`
        The address on the account could not be verified. Correct any errors in the address field or upload a document that includes the address.

      - `verification_failed_authorizer_authority`
        The account authorizer is not a registered authorized representative. Refer to [this support article](https://support.stripe.com/questions/representative-authority-verification) for more information.

      - `verification_failed_business_iec_number`
        The Importer Exporter Code (IEC) number on your account could not be verified. Either correct any possible errors in the company name or IEC number. Refer to the support article for [accepting international payments in India](https://support.stripe.com/questions/accepting-international-payments-from-stripe-accounts-in-india).

      - `verification_failed_document_match`
        The document could not be verified. Upload a document that includes the company name, ID number, and address fields.

      - `verification_failed_id_number_match`
        ID number on the document doesn’t match the ID number provided by this account.

      - `verification_failed_keyed_identity`
        The person’s keyed-in identity information could not be verified. Correct any errors or upload a document that matches the identity fields (e.g., name and date of birth) entered.

      - `verification_failed_keyed_match`
        The keyed-in information on the account could not be verified. Correct any errors in the company name, ID number, or address fields. You can also upload a document that includes those fields.

      - `verification_failed_name_match`
        The company name on the account could not be verified. Correct any errors in the company name field or upload a document that includes the company name.

      - `verification_failed_other`
        Verification failed for an unknown reason. Correct any errors and resubmit the required fields.

      - `verification_failed_representative_authority`
        The authority of the account representative could not be verified. Please change the account representative to a person who is registered as an authorized representative. Please refer to [this support article](https://support.stripe.com/questions/representative-authority-verification).

      - `verification_failed_residential_address`
        We could not verify that the person resides at the provided address. The address must be a valid physical address where the individual resides and cannot be a P.O. Box.

      - `verification_failed_tax_id_match`
        The tax ID on the account cannot be verified by the IRS. Either correct any possible errors in the company name or tax ID, or upload a document that contains those fields.

      - `verification_failed_tax_id_not_issued`
        The tax ID on the account was not recognized by the IRS. Refer to the support article for [newly-issued tax ID numbers](https://support.stripe.com/questions/newly-issued-us-tax-id-number-tin-not-verifying).

      - `verification_legal_entity_structure_mismatch`
        Business type or structure seems to be incorrect. Provide the correct business type and structure for this account.

      - `verification_missing_directors`
        We identified that your business has directors that have not been added to the account. Please add missing directors to your account.

      - `verification_missing_executives`
        We have identified executives that haven’t been added on the account. Add any missing executives to the account.

      - `verification_missing_owners`
        We have identified owners that haven’t been added on the account. Add any missing owners to the account.

      - `verification_rejected_ownership_exemption_reason`
        The ownership exemption reason was rejected.

      - `verification_requires_additional_memorandum_of_associations`
        We have identified holding companies with significant percentage ownership. Upload a Memorandum of Association for each of the holding companies.

      - `verification_requires_additional_proof_of_registration`
        The uploaded document contains holding companies with significant percentage ownership. Upload a proof of registration for each of the holding companies.

      - `verification_supportability`
        We can’t accept payments for this business under the Stripe Services Agreement without additional verification, as mentioned in the [prohibited and restricted businesses list](https://stripe.com/legal/restricted-businesses).

    - `requirements.errors.reason` (string)
      An informative message that indicates the error type and provides additional details about the error.

    - `requirements.errors.requirement` (string)
      The specific user onboarding requirement field (in the requirements hash) that needs to be resolved.

  - `requirements.eventually_due` (array of strings, nullable)
    Fields you must collect when all thresholds are reached. As they become required, they appear in `currently_due` as well, and `current_deadline` becomes set.

  - `requirements.past_due` (array of strings, nullable)
    Fields that haven’t been resolved by `current_deadline`. These fields need to be resolved to enable the account.

  - `requirements.pending_verification` (array of strings, nullable)
    Fields that are being reviewed, or might become required depending on the results of a review. If the review fails, these fields can move to `eventually_due`, `currently_due`, `past_due` or `alternatives`. Fields might appear in `eventually_due`, `currently_due`, `past_due` or `alternatives` and in `pending_verification` if one verification fails but another is still pending.

- `settings` (object, nullable)
  Options for customizing how the account functions within Stripe.

  - `settings.bacs_debit_payments` (object, nullable)
    Settings specific to Bacs Direct Debit on the account.

    - `settings.bacs_debit_payments.display_name` (string, nullable)
      The Bacs Direct Debit display name for this account. For payments made with Bacs Direct Debit, this name appears on the mandate as the statement descriptor. Mobile banking apps display it as the name of the business. To use custom branding, set the Bacs Direct Debit Display Name during or right after creation. Custom branding incurs an additional monthly fee for the platform. The fee appears 5 business days after requesting Bacs. If you don’t set the display name before requesting Bacs capability, it’s automatically set as “Stripe” and the account is onboarded to Stripe branding, which is free.

    - `settings.bacs_debit_payments.service_user_number` (string, nullable)
      The Bacs Direct Debit Service user number for this account. For payments made with Bacs Direct Debit, this number is a unique identifier of the account with our banking partners.

  - `settings.branding` (object)
    Settings used to apply the account’s branding to email receipts, invoices, Checkout, and other products.

    - `settings.branding.icon` (string, nullable)
      (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) An icon for the account. Must be square and at least 128px x 128px.

    - `settings.branding.logo` (string, nullable)
      (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) A logo for the account that will be used in Checkout instead of the icon and without the account’s name next to it if provided. Must be at least 128px x 128px.

    - `settings.branding.primary_color` (string, nullable)
      A CSS hex color value representing the primary branding color for this account

    - `settings.branding.secondary_color` (string, nullable)
      A CSS hex color value representing the secondary branding color for this account

  - `settings.card_issuing` (object, nullable)
    Settings specific to the account’s use of the Card Issuing product.

    - `settings.card_issuing.tos_acceptance` (object)
      Details on the account’s acceptance of the [Stripe Issuing Terms and Disclosures](https://docs.stripe.com/docs/issuing/connect/tos_acceptance.md).

      - `settings.card_issuing.tos_acceptance.date` (integer, nullable)
        The Unix timestamp marking when the account representative accepted the service agreement.

      - `settings.card_issuing.tos_acceptance.ip` (string, nullable)
        The IP address from which the account representative accepted the service agreement.

      - `settings.card_issuing.tos_acceptance.user_agent` (string, nullable)
        The user agent of the browser from which the account representative accepted the service agreement.

  - `settings.card_payments` (object)
    Settings specific to card charging on the account.

    - `settings.card_payments.decline_on` (object)
      Automatically declines certain charge types regardless of whether the card issuer accepted or declined the charge.

      - `settings.card_payments.decline_on.avs_failure` (boolean)
        Whether Stripe automatically declines charges with an incorrect ZIP or postal code. This setting only applies when a ZIP or postal code is provided and they fail bank verification.

      - `settings.card_payments.decline_on.cvc_failure` (boolean)
        Whether Stripe automatically declines charges with an incorrect CVC. This setting only applies when a CVC is provided and it fails bank verification.

    - `settings.card_payments.statement_descriptor_prefix` (string, nullable)
      Default text that appears on statements for card charges outside of Japan, prefixing any dynamic `statement_descriptor_suffix` specified on the charge. To maximize space for the dynamic part of the descriptor, keep this text short. If you don’t specify this value, `statement_descriptor` is used as the prefix. For more information about statement descriptors and their requirements, see the [account settings documentation](https://docs.stripe.com/get-started/account/statement-descriptors.md).

    - `settings.card_payments.statement_descriptor_prefix_kana` (string, nullable)
      The Kana variation of `statement_descriptor_prefix` used for card charges in Japan. Japanese statement descriptors have [special requirements](https://docs.stripe.com/get-started/account/statement-descriptors.md#set-japanese-statement-descriptors).

    - `settings.card_payments.statement_descriptor_prefix_kanji` (string, nullable)
      The Kanji variation of `statement_descriptor_prefix` used for card charges in Japan. Japanese statement descriptors have [special requirements](https://docs.stripe.com/get-started/account/statement-descriptors.md#set-japanese-statement-descriptors).

  - `settings.dashboard` (object)
    Settings used to configure the account within the Stripe dashboard.

    - `settings.dashboard.display_name` (string, nullable)
      The display name for this account. This is used on the Stripe Dashboard to differentiate between accounts.

    - `settings.dashboard.timezone` (string, nullable)
      The timezone used in the Stripe Dashboard for this account. A list of possible time zone values is maintained at the [IANA Time Zone Database](http://www.iana.org/time-zones).

  - `settings.invoices` (object, nullable)
    Settings specific to the account’s use of Invoices.

    - `settings.invoices.default_account_tax_ids` (array of strings, nullable)
      The list of default Account Tax IDs to automatically include on invoices. Account Tax IDs get added when an invoice is finalized.

    - `settings.invoices.hosted_payment_method_save` (enum, nullable)
      Whether to save the payment method after a payment is completed for a one-time invoice or a subscription invoice when the customer already has a default payment method on the hosted invoice page.
Possible enum values:
      - `always`
      - `never`
      - `offer`

  - `settings.payments` (object)
    Settings that apply across payment methods for charging on the account.

    - `settings.payments.statement_descriptor` (string, nullable)
      The default text that appears on statements for non-card charges outside of Japan. For card charges, if you don’t set a `statement_descriptor_prefix`, this text is also used as the statement descriptor prefix. In that case, if concatenating the statement descriptor suffix causes the combined statement descriptor to exceed 22 characters, we truncate the `statement_descriptor` text to limit the full descriptor to 22 characters. For more information about statement descriptors and their requirements, see the [account settings documentation](https://docs.stripe.com/get-started/account/statement-descriptors.md).

    - `settings.payments.statement_descriptor_kana` (string, nullable)
      The Kana variation of `statement_descriptor` used for charges in Japan. Japanese statement descriptors have [special requirements](https://docs.stripe.com/get-started/account/statement-descriptors.md#set-japanese-statement-descriptors).

    - `settings.payments.statement_descriptor_kanji` (string, nullable)
      The Kanji variation of `statement_descriptor` used for charges in Japan. Japanese statement descriptors have [special requirements](https://docs.stripe.com/get-started/account/statement-descriptors.md#set-japanese-statement-descriptors).

  - `settings.payouts` (object)
    Settings specific to the account’s payouts.

    - `settings.payouts.debit_negative_balances` (boolean)
      A Boolean indicating if Stripe should try to reclaim negative balances from an attached bank account. See [Understanding Connect account balances](https://docs.stripe.com/connect/account-balances.md) for details. The default value is `false` when [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `application`, which includes Custom accounts, otherwise `true`.

    - `settings.payouts.schedule` (object)
      Details on when funds from charges are available, and when they are paid out to an external account. See our [Setting Bank and Debit Card Payouts](https://docs.stripe.com/docs/connect/bank-transfers.md#payout-information) documentation for details.

      - `settings.payouts.schedule.delay_days` (integer)
        The number of days charges for the account will be held before being paid out.

      - `settings.payouts.schedule.interval` (string)
        How frequently funds will be paid out. One of `manual` (payouts only created via API call), `daily`, `weekly`, or `monthly`.

      - `settings.payouts.schedule.monthly_anchor` (integer, nullable)
        The day of the month funds will be paid out. Only shown if `interval` is monthly. Payouts scheduled between the 29th and 31st of the month are sent on the last day of shorter months.

      - `settings.payouts.schedule.monthly_payout_days` (array of integers, nullable)
        The days of the month funds will be paid out. Only shown if `interval` is monthly. Payouts scheduled between the 29th and 31st of the month are sent on the last day of shorter months.

      - `settings.payouts.schedule.weekly_anchor` (string, nullable)
        The day of the week funds will be paid out, of the style ‘monday’, ‘tuesday’, etc. Only shown if `interval` is weekly.

      - `settings.payouts.schedule.weekly_payout_days` (array of enums, nullable)
        The days of the week when available funds are paid out, specified as an array, for example, [`monday`, `tuesday`]. Only shown if `interval` is weekly.
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

    - `settings.payouts.statement_descriptor` (string, nullable)
      The text that appears on the bank account statement for payouts. If not set, this defaults to the platform’s bank descriptor as set in the Dashboard.

  - `settings.sepa_debit_payments` (object, nullable)
    Settings specific to SEPA Direct Debit on the account.

    - `settings.sepa_debit_payments.creditor_id` (string, nullable)
      SEPA creditor identifier that identifies the company making the payment.

- `tos_acceptance` (object)
  Details on the [acceptance of the Stripe Services Agreement](https://docs.stripe.com/docs/connect/updating-accounts.md#tos-acceptance) by the account representative.

  - `tos_acceptance.date` (timestamp, nullable)
    The Unix timestamp marking when the account representative accepted their service agreement

  - `tos_acceptance.ip` (string, nullable)
    The IP address from which the account representative accepted their service agreement

  - `tos_acceptance.service_agreement` (string, nullable)
    The user’s service agreement type

  - `tos_acceptance.user_agent` (string, nullable)
    The user agent of the browser from which the account representative accepted their service agreement

- `type` (enum)
  The Stripe account type. Can be `standard`, `express`, `custom`, or `none`.
Possible enum values:
  - `custom`
  - `express`
  - `none`
    Indicates that the account was created with [controller](https://docs.stripe.com/docs/api/accounts/object.md#account_object-controller) attributes that don’t map to a type of `standard`, `express`, or `custom`.

  - `standard`

### The Account object

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
```