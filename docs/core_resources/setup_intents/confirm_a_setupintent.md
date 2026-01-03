# Confirm a SetupIntent

Confirm that your customer intends to set up the current or provided payment method. For example, you would confirm a SetupIntent when a customer hits the “Save” button on a payment method management page on your website.

If the selected payment method does not require any additional steps from the customer, the SetupIntent will transition to the `succeeded` status.

Otherwise, it will transition to the `requires_action` status and suggest additional actions via `next_action`. If setup fails, the SetupIntent will transition to the `requires_payment_method` status or the `canceled` status if the confirmation limit is reached.

## Returns

Returns the resulting SetupIntent after all possible transitions are applied.

## Parameters

- `confirmation_token` (string, optional)
  ID of the ConfirmationToken used to confirm this SetupIntent.

  If the provided ConfirmationToken contains properties that are also being provided in this request, such as `payment_method`, then the values in this request will take precedence.

- `mandate_data` (object, optional)
  This hash contains details about the mandate to create

  - `mandate_data.customer_acceptance` (object, required)
    This hash contains details about the customer acceptance of the Mandate.

    - `mandate_data.customer_acceptance.type` (string, required)
      The type of customer acceptance information included with the Mandate. One of `online` or `offline`.

    - `mandate_data.customer_acceptance.accepted_at` (timestamp, optional)
      The time at which the customer accepted the Mandate.

    - `mandate_data.customer_acceptance.offline` (object, optional)
      If this is a Mandate accepted offline, this hash contains details about the offline acceptance.

    - `mandate_data.customer_acceptance.online` (object, optional)
      If this is a Mandate accepted online, this hash contains details about the online acceptance.

      - `mandate_data.customer_acceptance.online.ip_address` (string, required)
        The IP address from which the Mandate was accepted by the customer.

      - `mandate_data.customer_acceptance.online.user_agent` (string, required)
        The user agent of the browser from which the Mandate was accepted by the customer.

- `payment_method` (string, optional)
  ID of the payment method (a PaymentMethod, Card, or saved Source object) to attach to this SetupIntent.

- `payment_method_data` (object, optional)
  When included, this hash creates a PaymentMethod that is set as the [`payment_method`](https://docs.stripe.com/docs/api/setup_intents/object.md#setup_intent_object-payment_method) value in the SetupIntent.

  - `payment_method_data.type` (enum, required)
    The type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type.

  - `payment_method_data.acss_debit` (object, optional)
    If this is an `acss_debit` PaymentMethod, this hash contains details about the ACSS Debit payment method.

    - `payment_method_data.acss_debit.account_number` (string, required)
      Customer’s bank account number.

    - `payment_method_data.acss_debit.institution_number` (string, required)
      Institution number of the customer’s bank.

    - `payment_method_data.acss_debit.transit_number` (string, required)
      Transit number of the customer’s bank.

  - `payment_method_data.affirm` (object, optional)
    If this is an `affirm` PaymentMethod, this hash contains details about the Affirm payment method.

  - `payment_method_data.afterpay_clearpay` (object, optional)
    If this is an `AfterpayClearpay` PaymentMethod, this hash contains details about the AfterpayClearpay payment method.

  - `payment_method_data.alipay` (object, optional)
    If this is an `Alipay` PaymentMethod, this hash contains details about the Alipay payment method.

  - `payment_method_data.allow_redisplay` (enum, optional)
    This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow. The field defaults to `unspecified`.
Possible enum values:
    - `always`
      Use `always` to indicate that this payment method can always be shown to a customer in a checkout flow.

    - `limited`
      Use `limited` to indicate that this payment method can’t always be shown to a customer in a checkout flow. For example, it can only be shown in the context of a specific subscription.

    - `unspecified`
      This is the default value for payment methods where `allow_redisplay` wasn’t set.

  - `payment_method_data.alma` (object, optional)
    If this is a Alma PaymentMethod, this hash contains details about the Alma payment method.

  - `payment_method_data.amazon_pay` (object, optional)
    If this is a AmazonPay PaymentMethod, this hash contains details about the AmazonPay payment method.

  - `payment_method_data.au_becs_debit` (object, optional)
    If this is an `au_becs_debit` PaymentMethod, this hash contains details about the bank account.

    - `payment_method_data.au_becs_debit.account_number` (string, required)
      The account number for the bank account.

    - `payment_method_data.au_becs_debit.bsb_number` (string, required)
      Bank-State-Branch number of the bank account.

  - `payment_method_data.bacs_debit` (object, optional)
    If this is a `bacs_debit` PaymentMethod, this hash contains details about the Bacs Direct Debit bank account.

    - `payment_method_data.bacs_debit.account_number` (string, optional)
      Account number of the bank account that the funds will be debited from.

    - `payment_method_data.bacs_debit.sort_code` (string, optional)
      Sort code of the bank account. (e.g., `10-20-30`)

  - `payment_method_data.bancontact` (object, optional)
    If this is a `bancontact` PaymentMethod, this hash contains details about the Bancontact payment method.

  - `payment_method_data.billie` (object, optional)
    If this is a `billie` PaymentMethod, this hash contains details about the Billie payment method.

  - `payment_method_data.billing_details` (object, optional)
    Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.

    - `payment_method_data.billing_details.address` (object, optional)
      Billing address.

      - `payment_method_data.billing_details.address.city` (string, optional)
        City, district, suburb, town, or village.

      - `payment_method_data.billing_details.address.country` (string, optional)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `payment_method_data.billing_details.address.line1` (string, optional)
        Address line 1, such as the street, PO Box, or company name.

      - `payment_method_data.billing_details.address.line2` (string, optional)
        Address line 2, such as the apartment, suite, unit, or building.

      - `payment_method_data.billing_details.address.postal_code` (string, optional)
        ZIP or postal code.

      - `payment_method_data.billing_details.address.state` (string, optional)
        State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

    - `payment_method_data.billing_details.email` (string, optional)
      Email address.

      The maximum length is 800 characters.

    - `payment_method_data.billing_details.name` (string, optional)
      Full name.

    - `payment_method_data.billing_details.phone` (string, optional)
      Billing phone number (including extension).

    - `payment_method_data.billing_details.tax_id` (string, optional)
      Taxpayer identification number. Used only for transactions between LATAM buyers and non-LATAM sellers.

  - `payment_method_data.blik` (object, optional)
    If this is a `blik` PaymentMethod, this hash contains details about the BLIK payment method.

  - `payment_method_data.boleto` (object, optional)
    If this is a `boleto` PaymentMethod, this hash contains details about the Boleto payment method.

    - `payment_method_data.boleto.tax_id` (string, required)
      The tax ID of the customer (CPF for individual consumers or CNPJ for businesses consumers)

  - `payment_method_data.cashapp` (object, optional)
    If this is a `cashapp` PaymentMethod, this hash contains details about the Cash App Pay payment method.

  - `payment_method_data.crypto` (object, optional)
    If this is a Crypto PaymentMethod, this hash contains details about the Crypto payment method.

  - `payment_method_data.customer_balance` (object, optional)
    If this is a `customer_balance` PaymentMethod, this hash contains details about the CustomerBalance payment method.

  - `payment_method_data.eps` (object, optional)
    If this is an `eps` PaymentMethod, this hash contains details about the EPS payment method.

    - `payment_method_data.eps.bank` (string, optional)
      The customer’s bank.

  - `payment_method_data.fpx` (object, optional)
    If this is an `fpx` PaymentMethod, this hash contains details about the FPX payment method.

    - `payment_method_data.fpx.bank` (string, required)
      The customer’s bank.

  - `payment_method_data.giropay` (object, optional)
    If this is a `giropay` PaymentMethod, this hash contains details about the Giropay payment method.

  - `payment_method_data.grabpay` (object, optional)
    If this is a `grabpay` PaymentMethod, this hash contains details about the GrabPay payment method.

  - `payment_method_data.ideal` (object, optional)
    If this is an `ideal` PaymentMethod, this hash contains details about the iDEAL payment method.

    - `payment_method_data.ideal.bank` (string, optional)
      The customer’s bank. Only use this parameter for existing customers. Don’t use it for new customers.

  - `payment_method_data.interac_present` (object, optional)
    If this is an `interac_present` PaymentMethod, this hash contains details about the Interac Present payment method.

  - `payment_method_data.kakao_pay` (object, optional)
    If this is a `kakao_pay` PaymentMethod, this hash contains details about the Kakao Pay payment method.

  - `payment_method_data.klarna` (object, optional)
    If this is a `klarna` PaymentMethod, this hash contains details about the Klarna payment method.

    - `payment_method_data.klarna.dob` (object, optional)
      Customer’s date of birth

      - `payment_method_data.klarna.dob.day` (integer, required)
        The day of birth, between 1 and 31.

      - `payment_method_data.klarna.dob.month` (integer, required)
        The month of birth, between 1 and 12.

      - `payment_method_data.klarna.dob.year` (integer, required)
        The four-digit year of birth.

  - `payment_method_data.konbini` (object, optional)
    If this is a `konbini` PaymentMethod, this hash contains details about the Konbini payment method.

  - `payment_method_data.kr_card` (object, optional)
    If this is a `kr_card` PaymentMethod, this hash contains details about the Korean Card payment method.

  - `payment_method_data.link` (object, optional)
    If this is an `Link` PaymentMethod, this hash contains details about the Link payment method.

  - `payment_method_data.mb_way` (object, optional)
    If this is a MB WAY PaymentMethod, this hash contains details about the MB WAY payment method.

  - `payment_method_data.metadata` (object, optional)
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

  - `payment_method_data.mobilepay` (object, optional)
    If this is a `mobilepay` PaymentMethod, this hash contains details about the MobilePay payment method.

  - `payment_method_data.multibanco` (object, optional)
    If this is a `multibanco` PaymentMethod, this hash contains details about the Multibanco payment method.

  - `payment_method_data.naver_pay` (object, optional)
    If this is a `naver_pay` PaymentMethod, this hash contains details about the Naver Pay payment method.

    - `payment_method_data.naver_pay.funding` (enum, optional)
      Whether to use Naver Pay points or a card to fund this transaction. If not provided, this defaults to `card`.
Possible enum values:
      - `card`
        Use a card to fund this transaction.

      - `points`
        Use Naver Pay points to fund this transaction.

  - `payment_method_data.nz_bank_account` (object, optional)
    If this is an nz_bank_account PaymentMethod, this hash contains details about the nz_bank_account payment method.

    - `payment_method_data.nz_bank_account.account_number` (string, required)
      The account number for the bank account.

    - `payment_method_data.nz_bank_account.bank_code` (string, required)
      The numeric code for the bank account’s bank.

    - `payment_method_data.nz_bank_account.branch_code` (string, required)
      The numeric code for the bank account’s bank branch.

    - `payment_method_data.nz_bank_account.suffix` (string, required)
      The suffix of the bank account number.

    - `payment_method_data.nz_bank_account.account_holder_name` (string, optional)
      The name on the bank account. Only required if the account holder name is different from the name of the authorized signatory collected in the PaymentMethod’s billing details.

  - `payment_method_data.oxxo` (object, optional)
    If this is an `oxxo` PaymentMethod, this hash contains details about the OXXO payment method.

  - `payment_method_data.p24` (object, optional)
    If this is a `p24` PaymentMethod, this hash contains details about the P24 payment method.

    - `payment_method_data.p24.bank` (enum, optional)
      The customer’s bank.

  - `payment_method_data.pay_by_bank` (object, optional)
    If this is a `pay_by_bank` PaymentMethod, this hash contains details about the PayByBank payment method.

  - `payment_method_data.payco` (object, optional)
    If this is a `payco` PaymentMethod, this hash contains details about the PAYCO payment method.

  - `payment_method_data.paynow` (object, optional)
    If this is a `paynow` PaymentMethod, this hash contains details about the PayNow payment method.

  - `payment_method_data.paypal` (object, optional)
    If this is a `paypal` PaymentMethod, this hash contains details about the PayPal payment method.

  - `payment_method_data.paypay` (object, optional)
    If this is a `paypay` PaymentMethod, this hash contains details about the PayPay payment method.

  - `payment_method_data.payto` (object, optional)
    If this is a `payto` PaymentMethod, this hash contains details about the PayTo payment method.

    - `payment_method_data.payto.account_number` (string, optional)
      The account number for the bank account.

    - `payment_method_data.payto.bsb_number` (string, optional)
      Bank-State-Branch number of the bank account.

    - `payment_method_data.payto.pay_id` (string, optional)
      The PayID alias for the bank account.

  - `payment_method_data.pix` (object, optional)
    If this is a `pix` PaymentMethod, this hash contains details about the Pix payment method.

  - `payment_method_data.promptpay` (object, optional)
    If this is a `promptpay` PaymentMethod, this hash contains details about the PromptPay payment method.

  - `payment_method_data.radar_options` (object, optional)
    Options to configure Radar. See [Radar Session](https://docs.stripe.com/docs/radar/radar-session.md) for more information.

    - `payment_method_data.radar_options.session` (string, optional)
      A [Radar Session](https://docs.stripe.com/docs/radar/radar-session.md) is a snapshot of the browser metadata and device details that help Radar make more accurate predictions on your payments.

  - `payment_method_data.revolut_pay` (object, optional)
    If this is a `revolut_pay` PaymentMethod, this hash contains details about the Revolut Pay payment method.

  - `payment_method_data.samsung_pay` (object, optional)
    If this is a `samsung_pay` PaymentMethod, this hash contains details about the SamsungPay payment method.

  - `payment_method_data.satispay` (object, optional)
    If this is a `satispay` PaymentMethod, this hash contains details about the Satispay payment method.

  - `payment_method_data.sepa_debit` (object, optional)
    If this is a `sepa_debit` PaymentMethod, this hash contains details about the SEPA debit bank account.

    - `payment_method_data.sepa_debit.iban` (string, required)
      IBAN of the bank account.

  - `payment_method_data.sofort` (object, optional)
    If this is a `sofort` PaymentMethod, this hash contains details about the SOFORT payment method.

    - `payment_method_data.sofort.country` (enum, required)
      Two-letter ISO code representing the country the bank account is located in.
Possible enum values:
      - `AT`
        Austria

      - `BE`
        Belgium

      - `DE`
        Germany

      - `ES`
        Spain

      - `IT`
        Italy

      - `NL`
        Netherlands

  - `payment_method_data.swish` (object, optional)
    If this is a `swish` PaymentMethod, this hash contains details about the Swish payment method.

  - `payment_method_data.twint` (object, optional)
    If this is a TWINT PaymentMethod, this hash contains details about the TWINT payment method.

  - `payment_method_data.us_bank_account` (object, optional)
    If this is an `us_bank_account` PaymentMethod, this hash contains details about the US bank account payment method.

    - `payment_method_data.us_bank_account.account_holder_type` (enum, optional)
      Account holder type: individual or company.
Possible enum values:
      - `company`
        Account belongs to a company

      - `individual`
        Account belongs to an individual

    - `payment_method_data.us_bank_account.account_number` (string, optional)
      Account number of the bank account.

    - `payment_method_data.us_bank_account.account_type` (enum, optional)
      Account type: checkings or savings. Defaults to checking if omitted.
Possible enum values:
      - `checking`
        Bank account type is checking

      - `savings`
        Bank account type is savings

    - `payment_method_data.us_bank_account.financial_connections_account` (string, optional)
      The ID of a Financial Connections Account to use as a payment method.

    - `payment_method_data.us_bank_account.routing_number` (string, optional)
      Routing number of the bank account.

  - `payment_method_data.wechat_pay` (object, optional)
    If this is an `wechat_pay` PaymentMethod, this hash contains details about the wechat_pay payment method.

  - `payment_method_data.zip` (object, optional)
    If this is a `zip` PaymentMethod, this hash contains details about the Zip payment method.

- `payment_method_options` (object, optional)
  Payment method-specific configuration for this SetupIntent.

  - `payment_method_options.acss_debit` (object, optional)
    If this is a `acss_debit` SetupIntent, this sub-hash contains details about the ACSS Debit payment method options.

    - `payment_method_options.acss_debit.currency` (enum, optional)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
Possible enum values:
      - `cad`
        Canadian dollars

      - `usd`
        US dollars

    - `payment_method_options.acss_debit.mandate_options` (object, optional)
      Additional fields for Mandate creation

      - `payment_method_options.acss_debit.mandate_options.custom_mandate_url` (string, optional)
        A URL for custom mandate text to render during confirmation step. The URL will be rendered with additional GET parameters `payment_intent` and `payment_intent_client_secret` when confirming a Payment Intent, or `setup_intent` and `setup_intent_client_secret` when confirming a Setup Intent.

      - `payment_method_options.acss_debit.mandate_options.default_for` (array of enums, optional)
        List of Stripe products where this mandate can be selected automatically.
Possible enum values:
        - `invoice`
          Enables payments for Stripe Invoices. ‘subscription’ must also be provided.

        - `subscription`
          Enables payments for Stripe Subscriptions. ‘invoice’ must also be provided.

      - `payment_method_options.acss_debit.mandate_options.interval_description` (string, optional)
        Description of the mandate interval. Only required if ‘payment_schedule’ parameter is ‘interval’ or ‘combined’.

        The maximum length is 500 characters.

      - `payment_method_options.acss_debit.mandate_options.payment_schedule` (enum, optional)
        Payment schedule for the mandate.
Possible enum values:
        - `combined`
          Payments can be initiated at a pre-defined interval or sporadically

        - `interval`
          Payments are initiated at a regular pre-defined interval

        - `sporadic`
          Payments are initiated sporadically

      - `payment_method_options.acss_debit.mandate_options.transaction_type` (enum, optional)
        Transaction type of the mandate.
Possible enum values:
        - `business`
          Transactions are made for business reasons

        - `personal`
          Transactions are made for personal reasons

    - `payment_method_options.acss_debit.verification_method` (enum, optional)
      Bank account verification method.
Possible enum values:
      - `automatic`
        Instant verification with fallback to microdeposits.

      - `instant`
        Instant verification.

      - `microdeposits`
        Verification using microdeposits.

  - `payment_method_options.amazon_pay` (object, optional)
    If this is a `amazon_pay` SetupIntent, this sub-hash contains details about the  AmazonPay payment method options.

  - `payment_method_options.bacs_debit` (object, optional)
    If this is a `bacs_debit` SetupIntent, this sub-hash contains details about the Bacs Debit payment method options.

    - `payment_method_options.bacs_debit.mandate_options` (object, optional)
      Additional fields for Mandate creation

      - `payment_method_options.bacs_debit.mandate_options.reference_prefix` (string, optional)
        Prefix used to generate the Mandate reference. Must be at most 12 characters long. Must consist of only uppercase letters, numbers, spaces, or the following special characters: ‘/’, ‘_’, ‘-’, ‘&’, ‘.’. Cannot begin with ‘DDIC’ or ‘STRIPE’.

        The maximum length is 12 characters.

  - `payment_method_options.card` (object, optional)
    Configuration for any card setup attempted on this SetupIntent.

    - `payment_method_options.card.mandate_options` (object, optional)
      Configuration options for setting up an eMandate for cards issued in India.

      - `payment_method_options.card.mandate_options.amount` (integer, required)
        Amount to be charged for future payments.

      - `payment_method_options.card.mandate_options.amount_type` (enum, required)
        One of `fixed` or `maximum`. If `fixed`, the `amount` param refers to the exact amount to be charged in future payments. If `maximum`, the amount charged can be up to the value passed for the `amount` param.
Possible enum values:
        - `fixed`
        - `maximum`

      - `payment_method_options.card.mandate_options.currency` (enum, required)
        Currency in which future payments will be charged. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

      - `payment_method_options.card.mandate_options.interval` (enum, required)
        Specifies payment frequency. One of `day`, `week`, `month`, `year`, or `sporadic`.
Possible enum values:
        - `day`
        - `month`
        - `sporadic`
        - `week`
        - `year`

      - `payment_method_options.card.mandate_options.reference` (string, required)
        Unique identifier for the mandate or subscription.

        The maximum length is 80 characters.

      - `payment_method_options.card.mandate_options.start_date` (timestamp, required)
        Start date of the mandate or subscription. Start date should not be lesser than yesterday.

      - `payment_method_options.card.mandate_options.description` (string, optional)
        A description of the mandate or subscription that is meant to be displayed to the customer.

        The maximum length is 200 characters.

      - `payment_method_options.card.mandate_options.end_date` (timestamp, optional)
        End date of the mandate or subscription. If not provided, the mandate will be active until canceled. If provided, end date should be after start date.

      - `payment_method_options.card.mandate_options.interval_count` (integer, optional)
        The number of intervals between payments. For example, `interval=month` and `interval_count=3` indicates one payment every three months. Maximum of one year interval allowed (1 year, 12 months, or 52 weeks). This parameter is optional when `interval=sporadic`.

      - `payment_method_options.card.mandate_options.supported_types` (array of enums, optional)
        Specifies the type of mandates supported. Possible values are `india`.
Possible enum values:
        - `india`

    - `payment_method_options.card.network` (string, optional)
      Selected network to process this SetupIntent on. Depends on the available networks of the card attached to the SetupIntent. Can be only set confirm-time.

    - `payment_method_options.card.request_three_d_secure` (enum, optional)
      We strongly recommend that you rely on our SCA Engine to automatically prompt your customers for authentication based on risk level and [other requirements](https://docs.stripe.com/docs/strong-customer-authentication.md). However, if you wish to request 3D Secure based on logic from your own fraud engine, provide this option. If not provided, this value defaults to `automatic`. Read our guide on [manually requesting 3D Secure](https://docs.stripe.com/docs/payments/3d-secure/authentication-flow.md#manual-three-ds) for more information on how this configuration interacts with Radar and our SCA Engine.
Possible enum values:
      - `any`
        Use `any` to manually request 3DS with a preference for a `frictionless` flow, increasing the likelihood of the authentication being completed without any additional input from the customer. 3DS will always be attempted if it is supported for the card, but Stripe can’t guarantee your preference because the issuer determines the ultimate authentication flow. To learn more about 3DS flows, read our [guide](https://stripe.com/guides/3d-secure-2#frictionless-authentication).

      - `automatic`
        (Default) Our SCA Engine automatically prompts your customers for authentication based on risk level and other requirements.

      - `challenge`
        Use `challenge` to request 3DS with a preference for a `challenge` flow, where the customer must respond to a prompt for active authentication. Stripe can’t guarantee your preference because the issuer determines the ultimate authentication flow. To learn more about 3DS flows, read our [guide](https://stripe.com/guides/3d-secure-2#frictionless-authentication).

    - `payment_method_options.card.three_d_secure` (object, optional)
      If 3D Secure authentication was performed with a third-party provider, the authentication details to use for this setup.

      - `payment_method_options.card.three_d_secure.ares_trans_status` (enum, optional)
        The `transStatus` returned from the card Issuer’s ACS in the ARes.
Possible enum values:
        - `A`
          Attempts processing performed; Not authenticated/verified, but a proof of attempted authentication/verification is provided.

        - `C`
          Challenge required; Additional authentication is required.

        - `I`
          Informational only; 3DS Requestor challenge preference acknowledged.

        - `N`
          Not authenticated/Account not verified; Transaction denied.

        - `R`
          Authentication/Account verification rejected; Issuer is rejecting authentication/verification and request that authorisation not be attempted.

        - `U`
          Authentication/Account verification could not be performed; Technical or other problem.

        - `Y`
          Authentication verification successful.

      - `payment_method_options.card.three_d_secure.cryptogram` (string, Required for Import 3DS)
        The cryptogram, also known as the “authentication value” (AAV, CAVV or AEVV). This value is 20 bytes, base64-encoded into a 28-character string. (Most 3D Secure providers will return the base64-encoded version, which is what you should specify here.)

      - `payment_method_options.card.three_d_secure.electronic_commerce_indicator` (enum, Required for Import 3DS on all networks except Cartes Bancaires)
        The Electronic Commerce Indicator (ECI) is returned by your 3D Secure provider and indicates what degree of authentication was performed.
Possible enum values:
        - `01`
          **Mastercard variant:** Attempt acknowledged.

        - `02`
          **Mastercard variant:** Fully authenticated.

        - `05`
          Fully authenticated. The customer likely proved their identity to the issuing bank.

        - `06`
          Attempt acknowledged. The customer, or the entire issuing bank, is not set up for 3D Secure. Or the issuing bank is experiencing an outage.

          **Mastercard variant:** Acquirer SCA exemption.

        - `07`
          **Mastercard variant:** Fully authenticated recurring transaction.

      - `payment_method_options.card.three_d_secure.network_options` (object, optional)
        Network specific 3DS fields. Network specific arguments require an explicit card brand choice. The parameter `payment_method_options.card.network`` must be populated accordingly

        - `payment_method_options.card.three_d_secure.network_options.cartes_bancaires` (object, optional)
          Cartes Bancaires-specific 3DS fields.

          - `payment_method_options.card.three_d_secure.network_options.cartes_bancaires.cb_avalgo` (enum, required)
            The cryptogram calculation algorithm used by the card Issuer’s ACS to calculate the Authentication cryptogram. Also known as `cavvAlgorithm`. messageExtension: CB-AVALGO
Possible enum values:
            - `0`
              HMAC

            - `1`
              CVV

            - `2`
              CVV with ATN

            - `3`
              Mastercard SPA

            - `4`
              American Express SafeKey 1

            - `A`
              AV-CB

          - `payment_method_options.card.three_d_secure.network_options.cartes_bancaires.cb_exemption` (string, optional)
            The exemption indicator returned from Cartes Bancaires in the ARes. message extension: CB-EXEMPTION; string (4 characters) This is a 3 byte bitmap (low significant byte first and most significant bit first) that has been Base64 encoded

            The maximum length is 4 characters.

          - `payment_method_options.card.three_d_secure.network_options.cartes_bancaires.cb_score` (integer, optional)
            The risk score returned from Cartes Bancaires in the ARes. message extension: CB-SCORE; numeric value 0-99

      - `payment_method_options.card.three_d_secure.requestor_challenge_indicator` (string, optional)
        The challenge indicator (`threeDSRequestorChallengeInd`) which was requested in the AReq sent to the card Issuer’s ACS. A string containing 2 digits from 01-99.

        The maximum length is 2 characters.

      - `payment_method_options.card.three_d_secure.transaction_id` (string, Required for Import 3DS)
        For 3D Secure 1, the XID. For 3D Secure 2, the Directory Server Transaction ID (dsTransID).

      - `payment_method_options.card.three_d_secure.version` (enum, Required for Import 3DS)
        The version of 3D Secure that was performed.

  - `payment_method_options.card_present` (object, optional)
    If this is a `card_present` PaymentMethod, this sub-hash contains details about the card-present payment method options.

  - `payment_method_options.klarna` (object, optional)
    If this is a `klarna` PaymentMethod, this hash contains details about the Klarna payment method options.

    - `payment_method_options.klarna.currency` (enum, optional)
      The currency of the SetupIntent. Three letter ISO currency code.

    - `payment_method_options.klarna.on_demand` (object, optional)
      On-demand details if setting up a payment method for on-demand payments.

      - `payment_method_options.klarna.on_demand.average_amount` (integer, optional)
        Your average amount value. You can use a value across your customer base, or segment based on customer type, country, etc.

      - `payment_method_options.klarna.on_demand.maximum_amount` (integer, optional)
        The maximum value you may charge a customer per purchase. You can use a value across your customer base, or segment based on customer type, country, etc.

      - `payment_method_options.klarna.on_demand.minimum_amount` (integer, optional)
        The lowest or minimum value you may charge a customer per purchase. You can use a value across your customer base, or segment based on customer type, country, etc.

      - `payment_method_options.klarna.on_demand.purchase_interval` (enum, optional)
        Interval at which the customer is making purchases
Possible enum values:
        - `day`
          Use `day` if you expect one or more days between charges.

        - `month`
          Use `month` if you expect one or more months between charges.

        - `week`
          Use `week` if you expect one or more weeks between charges.

        - `year`
          Use `year` if you expect one or more years between charges.

      - `payment_method_options.klarna.on_demand.purchase_interval_count` (integer, optional)
        The number of `purchase_interval` between charges

    - `payment_method_options.klarna.preferred_locale` (enum, optional)
      Preferred language of the Klarna authorization page that the customer is redirected to
Possible enum values:
      - `cs-CZ`
        Czech - Czechia

      - `da-DK`
        Danish - Denmark

      - `de-AT`
        German - Austria

      - `de-CH`
        German - Switzerland

      - `de-DE`
        German - Germany

      - `el-GR`
        Greek - Greece

      - `en-AT`
        English - Austria

      - `en-AU`
        English - Australia

      - `en-BE`
        English - Belgium

      - `en-CA`
        English - Canada

      - `en-CH`
        English - Switzerland

      - `en-CZ`
        English - Czechia

      - `en-DE`
        English - Germany

      - `en-DK`
        English - Denmark

      - `en-ES`
        English - Spain

      - `en-FI`
        English - Finland

      - `en-FR`
        English - France

      - `en-GB`
        English - United Kingdom

      - `en-GR`
        English - Greece

      - `en-IE`
        English - Ireland

      - `en-IT`
        English - Italy

      - `en-NL`
        English - Netherlands

      - `en-NO`
        English - Norway

      - `en-NZ`
        English - New Zealand

      - `en-PL`
        English - Poland

      - `en-PT`
        English - Portugal

      - `en-RO`
        English - Romania

      - `en-SE`
        English - Sweden

      - `en-US`
        English - United States of America

      - `es-ES`
        Spanish - Spain

      - `es-US`
        Spanish - United States of America

      - `fi-FI`
        Finnish - Finland

      - `fr-BE`
        French - Belgium

      - `fr-CA`
        French - Canada

      - `fr-CH`
        French - Switzerland

      - `fr-FR`
        French - France

      - `it-CH`
        Italy - Switzerland

      - `it-IT`
        Italian - Italy

      - `nb-NO`
        Norwegian - Norway

      - `nl-BE`
        Dutch - Belgium

      - `nl-NL`
        Dutch - Netherlands

      - `pl-PL`
        Polish - Poland

      - `pt-PT`
        Portugese - Portugal

      - `ro-RO`
        Romanian - Romania

      - `sv-FI`
        Swedish - Finland

      - `sv-SE`
        Swedish - Sweden

    - `payment_method_options.klarna.subscriptions` (array of objects, optional)
      Subscription details if setting up or charging a subscription

      - `payment_method_options.klarna.subscriptions.interval` (enum, required)
        Unit of time between subscription charges.

      - `payment_method_options.klarna.subscriptions.next_billing` (object, required)
        Describes the upcoming charge for this subscription.

        - `payment_method_options.klarna.subscriptions.next_billing.amount` (integer, required)
          The amount of the next charge for the subscription.

        - `payment_method_options.klarna.subscriptions.next_billing.date` (string, required)
          The date of the next charge for the subscription in YYYY-MM-DD format.

      - `payment_method_options.klarna.subscriptions.reference` (string, required)
        A non-customer-facing reference to correlate subscription charges in the Klarna app. Use a value that persists across subscription charges.

        The maximum length is 255 characters.

      - `payment_method_options.klarna.subscriptions.interval_count` (integer, optional)
        The number of intervals (specified  in the `interval` attribute) between subscription  charges. For example, `interval=month` and `interval_count=3` charges every 3 months.

      - `payment_method_options.klarna.subscriptions.name` (string, optional)
        Name for subscription.

        The maximum length is 255 characters.

  - `payment_method_options.link` (object, optional)
    If this is a `link` PaymentMethod, this sub-hash contains details about the Link payment method options.

  - `payment_method_options.paypal` (object, optional)
    If this is a `paypal` PaymentMethod, this sub-hash contains details about the PayPal payment method options.

    - `payment_method_options.paypal.billing_agreement_id` (string, optional)
      The PayPal Billing Agreement ID (BAID). This is an ID generated by PayPal which represents the mandate between the merchant and the customer.

  - `payment_method_options.payto` (object, optional)
    If this is a `payto` SetupIntent, this sub-hash contains details about the PayTo payment method options.

    - `payment_method_options.payto.mandate_options` (object, optional)
      Additional fields for Mandate creation.

      - `payment_method_options.payto.mandate_options.amount` (integer, optional)
        Amount that will be collected. It is required when `amount_type` is `fixed`.

      - `payment_method_options.payto.mandate_options.amount_type` (enum, optional)
        The type of amount that will be collected. The amount charged must be exact or up to the value of `amount` param for `fixed` or `maximum` type respectively. Defaults to `maximum`.
Possible enum values:
        - `fixed`
          The amount is the exact amount that will be charged.

        - `maximum`
          The amount is the maximum amount that can be charged.

      - `payment_method_options.payto.mandate_options.end_date` (string, optional)
        Date, in YYYY-MM-DD format, after which payments will not be collected. Defaults to no end date.

      - `payment_method_options.payto.mandate_options.payment_schedule` (enum, optional)
        The periodicity at which payments will be collected. Defaults to `adhoc`.
Possible enum values:
        - `adhoc`
          Payments will be made ad hoc

        - `annual`
          Payments will be made annually

        - `daily`
          Payments will be made daily

        - `fortnightly`
          Payments will be made fortnightly

        - `monthly`
          Payments will be made monthly

        - `quarterly`
          Payments will be made quarterly

        - `semi_annual`
          Payments will be made semi-annually

        - `weekly`
          Payments will be made weekly

      - `payment_method_options.payto.mandate_options.payments_per_period` (integer, optional)
        The number of payments that will be made during a payment period. Defaults to 1 except for when `payment_schedule` is `adhoc`. In that case, it defaults to no limit.

      - `payment_method_options.payto.mandate_options.purpose` (enum, optional)
        The purpose for which payments are made. Has a default value based on your merchant category code.
Possible enum values:
        - `dependant_support`
          Transactions are made for dependant support reasons

        - `government`
          Transactions are made for government reasons

        - `loan`
          Transactions are made for loan reasons

        - `mortgage`
          Transactions are made for mortgage reasons

        - `other`
          Transactions are made for other reasons

        - `pension`
          Transactions are made for pension reasons

        - `personal`
          Transactions are made for personal reasons

        - `retail`
          Transactions are made for retail reasons

        - `salary`
          Transactions are made for salary reasons

        - `tax`
          Transactions are made for tax reasons

        - `utility`
          Transactions are made for utility reasons

      - `payment_method_options.payto.mandate_options.start_date` (string, optional)
        Date, in YYYY-MM-DD format, from which payments will be collected. Defaults to confirmation time.

  - `payment_method_options.sepa_debit` (object, optional)
    If this is a `sepa_debit` SetupIntent, this sub-hash contains details about the SEPA Debit payment method options.

    - `payment_method_options.sepa_debit.mandate_options` (object, optional)
      Additional fields for Mandate creation

      - `payment_method_options.sepa_debit.mandate_options.reference_prefix` (string, optional)
        Prefix used to generate the Mandate reference. Must be at most 12 characters long. Must consist of only uppercase letters, numbers, spaces, or the following special characters: ‘/’, ‘_’, ‘-’, ‘&’, ‘.’. Cannot begin with ‘STRIPE’.

        The maximum length is 12 characters.

  - `payment_method_options.us_bank_account` (object, optional)
    If this is a `us_bank_account` SetupIntent, this sub-hash contains details about the US bank account payment method options.

    - `payment_method_options.us_bank_account.financial_connections` (object, optional)
      Additional fields for Financial Connections Session creation

      - `payment_method_options.us_bank_account.financial_connections.filters` (object, optional)
        Provide filters for the linked accounts that the customer can select for the payment method.

        - `payment_method_options.us_bank_account.financial_connections.filters.account_subcategories` (array of strings, optional)
          The account subcategories to use to filter for selectable accounts. Valid subcategories are `checking` and `savings`.

      - `payment_method_options.us_bank_account.financial_connections.permissions` (array of strings, optional)
        The list of permissions to request. If this parameter is passed, the `payment_method` permission must be included. Valid permissions include: `balances`, `ownership`, `payment_method`, and `transactions`.

      - `payment_method_options.us_bank_account.financial_connections.prefetch` (array of enums, optional)
        List of data features that you would like to retrieve upon account creation.
Possible enum values:
        - `balances`
          Requests to prefetch balance data on accounts collected in this session.

        - `ownership`
          Requests to prefetch ownership data on accounts collected in this session.

        - `transactions`
          Requests to prefetch transaction data on accounts collected in this session.

      - `payment_method_options.us_bank_account.financial_connections.return_url` (string, optional)
        For webview integrations only. Upon completing OAuth login in the native browser, the user will be redirected to this URL to return to your app.

    - `payment_method_options.us_bank_account.mandate_options` (object, optional)
      Additional fields for Mandate creation

      - `payment_method_options.us_bank_account.mandate_options.collection_method` (enum, optional)
        The method used to collect offline mandate customer acceptance.
Possible enum values:
        - `paper`
          Mandate customer acceptance was collected using a paper document

    - `payment_method_options.us_bank_account.networks` (object, optional)
      Additional fields for network related functions

      - `payment_method_options.us_bank_account.networks.requested` (array of enums, optional)
        Triggers validations to run across the selected networks
Possible enum values:
        - `ach`
        - `us_domestic_wire`

    - `payment_method_options.us_bank_account.verification_method` (enum, optional)
      Bank account verification method.
Possible enum values:
      - `automatic`
        Instant verification with fallback to microdeposits.

      - `instant`
        Instant verification only.

      - `microdeposits`
        Verification using microdeposits. Cannot be used with Stripe Checkout, Hosted Invoices, or Payment Element.

- `return_url` (string, optional)
  The URL to redirect your customer back to after they authenticate on the payment method’s app or site. If you’d prefer to redirect to a mobile application, you can alternatively supply an application URI scheme. This parameter is only used for cards and other redirect-based payment methods.

- `use_stripe_sdk` (boolean, optional)
  Set to `true` when confirming server-side and using Stripe.js, iOS, or Android client-side SDKs to handle the next actions.

```curl
curl https://api.stripe.com/v1/setup_intents/seti_1Mm2cBLkdIwHu7ixaiKW3ElR/confirm \
  -u "<<YOUR_SECRET_KEY>>" \
  -d payment_method=pm_card_visa
```

```cli
stripe setup_intents confirm seti_1Mm2cBLkdIwHu7ixaiKW3ElR \
  --payment-method=pm_card_visa
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

setup_intent = client.v1.setup_intents.confirm(
  'seti_1Mm2cBLkdIwHu7ixaiKW3ElR',
  {payment_method: 'pm_card_visa'},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

setup_intent = client.v1.setup_intents.confirm(
  "seti_1Mm2cBLkdIwHu7ixaiKW3ElR",
  {"payment_method": "pm_card_visa"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$setupIntent = $stripe->setupIntents->confirm(
  'seti_1Mm2cBLkdIwHu7ixaiKW3ElR',
  ['payment_method' => 'pm_card_visa']
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

SetupIntentConfirmParams params =
  SetupIntentConfirmParams.builder().setPaymentMethod("pm_card_visa").build();

SetupIntent setupIntent =
  client.v1().setupIntents().confirm("seti_1Mm2cBLkdIwHu7ixaiKW3ElR", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.confirm(
  'seti_1Mm2cBLkdIwHu7ixaiKW3ElR',
  {
    payment_method: 'pm_card_visa',
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.SetupIntentConfirmParams{
  PaymentMethod: stripe.String("pm_card_visa"),
}
result, err := sc.V1SetupIntents.Confirm(
  context.TODO(), "seti_1Mm2cBLkdIwHu7ixaiKW3ElR", params)
```

```dotnet
var options = new SetupIntentConfirmOptions { PaymentMethod = "pm_card_visa" };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.SetupIntents;
SetupIntent setupIntent = service.Confirm("seti_1Mm2cBLkdIwHu7ixaiKW3ElR", options);
```

### Response

```json
{
  "id": "seti_1Mm2cBLkdIwHu7ixaiKW3ElR",
  "object": "setup_intent",
  "application": null,
  "cancellation_reason": null,
  "client_secret": "seti_1Mm2cBLkdIwHu7ixaiKW3ElR_secret_NX6phB7HbSmlkpqzKZ3Bxr7uXFRf9Jg",
  "created": 1678918571,
  "customer": null,
  "description": null,
  "flow_directions": null,
  "last_setup_error": null,
  "latest_attempt": "setatt_1Mm2cBLkdIwHu7ixdEp1VkXJ",
  "livemode": false,
  "mandate": null,
  "metadata": {},
  "next_action": null,
  "on_behalf_of": null,
  "payment_method": "pm_1Mm2cBLkdIwHu7ixGoOfZSsV",
  "payment_method_options": {
    "card": {
      "mandate_options": null,
      "network": null,
      "request_three_d_secure": "automatic"
    }
  },
  "payment_method_types": [
    "card"
  ],
  "single_use_mandate": null,
  "status": "succeeded",
  "usage": "off_session"
}
```