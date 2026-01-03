# The Confirmation Token object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `expires_at` (timestamp, nullable)
  Time at which this ConfirmationToken expires and can no longer be used to confirm a PaymentIntent or SetupIntent.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `mandate_data` (object, nullable)
  Data used for generating a Mandate.

  - `mandate_data.customer_acceptance` (object)
    This hash contains details about the customer acceptance of the Mandate.

    - `mandate_data.customer_acceptance.online` (object, nullable)
      If this is a Mandate accepted online, this hash contains details about the online acceptance.

      - `mandate_data.customer_acceptance.online.ip_address` (string, nullable)
        The IP address from which the Mandate was accepted by the customer.

      - `mandate_data.customer_acceptance.online.user_agent` (string, nullable)
        The user agent of the browser from which the Mandate was accepted by the customer.

    - `mandate_data.customer_acceptance.type` (string)
      The type of customer acceptance information included with the Mandate.

- `payment_intent` (string, nullable)
  ID of the PaymentIntent that this ConfirmationToken was used to confirm, or null if this ConfirmationToken has not yet been used.

- `payment_method_options` (object, nullable)
  Payment-method-specific configuration for this ConfirmationToken.

  - `payment_method_options.card` (object, nullable)
    This hash contains the card payment method options.

    - `payment_method_options.card.cvc_token` (string, nullable)
      The `cvc_update` Token collected from the Payment Element.

    - `payment_method_options.card.installments` (object, nullable)
      Installment details.

      - `payment_method_options.card.installments.plan` (object, nullable)
        Installment plan selected for this PaymentIntent.

        - `payment_method_options.card.installments.plan.count` (integer, nullable)
          For `fixed_count` installment plans, this is the number of installment payments your customer will make to their credit card.

        - `payment_method_options.card.installments.plan.interval` (enum, nullable)
          For `fixed_count` installment plans, this is the interval between installment payments your customer will make to their credit card. One of `month`.
Possible enum values:
          - `month`

        - `payment_method_options.card.installments.plan.type` (enum)
          Type of installment plan, one of `fixed_count`, `bonus`, or `revolving`.
Possible enum values:
          - `bonus`
            An installment plan used in Japan, where the customer defers payment to a later date that aligns with their salary bonus.

          - `fixed_count`
            An installment plan where the number of installment payments is fixed and known at the time of purchase.

          - `revolving`
            An installment plan used in Japan, where the customer pays a certain amount each month, and the remaining balance rolls over to the next month.

- `payment_method_preview` (object, nullable)
  Payment details collected by the Payment Element, used to create a PaymentMethod when a PaymentIntent or SetupIntent is confirmed with this ConfirmationToken.

  - `payment_method_preview.acss_debit` (object, nullable)
    If this is an `acss_debit` PaymentMethod, this hash contains details about the ACSS Debit payment method.

    - `payment_method_preview.acss_debit.bank_name` (string, nullable)
      Name of the bank associated with the bank account.

    - `payment_method_preview.acss_debit.fingerprint` (string, nullable)
      Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

    - `payment_method_preview.acss_debit.institution_number` (string, nullable)
      Institution number of the bank account.

    - `payment_method_preview.acss_debit.last4` (string, nullable)
      Last four digits of the bank account number.

    - `payment_method_preview.acss_debit.transit_number` (string, nullable)
      Transit number of the bank account.

  - `payment_method_preview.affirm` (object, nullable)
    If this is an `affirm` PaymentMethod, this hash contains details about the Affirm payment method.

  - `payment_method_preview.afterpay_clearpay` (object, nullable)
    If this is an `AfterpayClearpay` PaymentMethod, this hash contains details about the AfterpayClearpay payment method.

  - `payment_method_preview.alipay` (object, nullable)
    If this is an `Alipay` PaymentMethod, this hash contains details about the Alipay payment method.

  - `payment_method_preview.allow_redisplay` (enum, nullable)
    This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow. The field defaults to “unspecified”.
Possible enum values:
    - `always`
      Use `always` to indicate that this payment method can always be shown to a customer in a checkout flow.

    - `limited`
      Use `limited` to indicate that this payment method can’t always be shown to a customer in a checkout flow. For example, it can only be shown in the context of a specific subscription.

    - `unspecified`
      This is the default value for payment methods where `allow_redisplay` wasn’t set.

  - `payment_method_preview.alma` (object, nullable)
    If this is a Alma PaymentMethod, this hash contains details about the Alma payment method.

  - `payment_method_preview.amazon_pay` (object, nullable)
    If this is a AmazonPay PaymentMethod, this hash contains details about the AmazonPay payment method.

  - `payment_method_preview.au_becs_debit` (object, nullable)
    If this is an `au_becs_debit` PaymentMethod, this hash contains details about the bank account.

    - `payment_method_preview.au_becs_debit.bsb_number` (string, nullable)
      Six-digit number identifying bank and branch associated with this bank account.

    - `payment_method_preview.au_becs_debit.fingerprint` (string, nullable)
      Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

    - `payment_method_preview.au_becs_debit.last4` (string, nullable)
      Last four digits of the bank account number.

  - `payment_method_preview.bacs_debit` (object, nullable)
    If this is a `bacs_debit` PaymentMethod, this hash contains details about the Bacs Direct Debit bank account.

    - `payment_method_preview.bacs_debit.fingerprint` (string, nullable)
      Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

    - `payment_method_preview.bacs_debit.last4` (string, nullable)
      Last four digits of the bank account number.

    - `payment_method_preview.bacs_debit.sort_code` (string, nullable)
      Sort code of the bank account. (e.g., `10-20-30`)

  - `payment_method_preview.bancontact` (object, nullable)
    If this is a `bancontact` PaymentMethod, this hash contains details about the Bancontact payment method.

  - `payment_method_preview.billie` (object, nullable)
    If this is a `billie` PaymentMethod, this hash contains details about the Billie payment method.

  - `payment_method_preview.billing_details` (object)
    Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.

    - `payment_method_preview.billing_details.address` (object, nullable)
      Billing address.

      - `payment_method_preview.billing_details.address.city` (string, nullable)
        City, district, suburb, town, or village.

      - `payment_method_preview.billing_details.address.country` (string, nullable)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `payment_method_preview.billing_details.address.line1` (string, nullable)
        Address line 1, such as the street, PO Box, or company name.

      - `payment_method_preview.billing_details.address.line2` (string, nullable)
        Address line 2, such as the apartment, suite, unit, or building.

      - `payment_method_preview.billing_details.address.postal_code` (string, nullable)
        ZIP or postal code.

      - `payment_method_preview.billing_details.address.state` (string, nullable)
        State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

    - `payment_method_preview.billing_details.email` (string, nullable)
      Email address.

    - `payment_method_preview.billing_details.name` (string, nullable)
      Full name.

    - `payment_method_preview.billing_details.phone` (string, nullable)
      Billing phone number (including extension).

    - `payment_method_preview.billing_details.tax_id` (string, nullable)
      Taxpayer identification number. Used only for transactions between LATAM buyers and non-LATAM sellers.

  - `payment_method_preview.blik` (object, nullable)
    If this is a `blik` PaymentMethod, this hash contains details about the BLIK payment method.

  - `payment_method_preview.boleto` (object, nullable)
    If this is a `boleto` PaymentMethod, this hash contains details about the Boleto payment method.

    - `payment_method_preview.boleto.tax_id` (string)
      Uniquely identifies the customer tax id (CNPJ or CPF)

  - `payment_method_preview.card` (object, nullable)
    If this is a `card` PaymentMethod, this hash contains the user’s card details.

    - `payment_method_preview.card.brand` (string)
      Card brand. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `jcb`, `link`, `mastercard`, `unionpay`, `visa` or `unknown`.

    - `payment_method_preview.card.checks` (object, nullable)
      Checks on Card address and CVC if provided.

      - `payment_method_preview.card.checks.address_line1_check` (string, nullable)
        If a address line1 was provided, results of the check, one of `pass`, `fail`, `unavailable`, or `unchecked`.

      - `payment_method_preview.card.checks.address_postal_code_check` (string, nullable)
        If a address postal code was provided, results of the check, one of `pass`, `fail`, `unavailable`, or `unchecked`.

      - `payment_method_preview.card.checks.cvc_check` (string, nullable)
        If a CVC was provided, results of the check, one of `pass`, `fail`, `unavailable`, or `unchecked`.

    - `payment_method_preview.card.country` (string, nullable)
      Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you’ve collected.

    - `payment_method_preview.card.display_brand` (string, nullable)
      The brand to use when displaying the card, this accounts for customer’s brand choice on dual-branded cards. Can be `american_express`, `cartes_bancaires`, `diners_club`, `discover`, `eftpos_australia`, `interac`, `jcb`, `mastercard`, `union_pay`, `visa`, or `other` and may contain more values in the future.

    - `payment_method_preview.card.exp_month` (integer)
      Two-digit number representing the card’s expiration month.

    - `payment_method_preview.card.exp_year` (integer)
      Four-digit number representing the card’s expiration year.

    - `payment_method_preview.card.fingerprint` (string, nullable)
      Uniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.

      *As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card—one for India and one for the rest of the world.*

    - `payment_method_preview.card.funding` (string)
      Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.

    - `payment_method_preview.card.generated_from` (object, nullable)
      Details of the original PaymentMethod that created this object.

      - `payment_method_preview.card.generated_from.charge` (string, nullable)
        The charge that created this object.

      - `payment_method_preview.card.generated_from.payment_method_details` (object, nullable)
        Transaction-specific details of the payment method used in the payment.

        - `payment_method_preview.card.generated_from.payment_method_details.card_present` (object, nullable)
          This hash contains the snapshot of the `card_present` transaction-specific details which generated this `card` payment method.

          - `payment_method_preview.card.generated_from.payment_method_details.card_present.amount_authorized` (integer, nullable)
            The authorized amount

          - `payment_method_preview.card.generated_from.payment_method_details.card_present.brand` (string, nullable)
            Card brand. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `jcb`, `link`, `mastercard`, `unionpay`, `visa` or `unknown`.

          - `payment_method_preview.card.generated_from.payment_method_details.card_present.brand_product` (string, nullable)
            The [product code](https://stripe.com/docs/card-product-codes) that identifies the specific program or product associated with a card.

          - `payment_method_preview.card.generated_from.payment_method_details.card_present.capture_before` (timestamp, nullable)
            When using manual capture, a future timestamp after which the charge will be automatically refunded if uncaptured.

          - `payment_method_preview.card.generated_from.payment_method_details.card_present.cardholder_name` (string, nullable)
            The cardholder name as read from the card, in [ISO 7813](https://en.wikipedia.org/wiki/ISO/IEC_7813) format. May include alphanumeric characters, special characters and first/last name separator (`/`). In some cases, the cardholder name may not be available depending on how the issuer has configured the card. Cardholder name is typically not available on swipe or contactless payments, such as those made with Apple Pay and Google Pay.

          - `payment_method_preview.card.generated_from.payment_method_details.card_present.country` (string, nullable)
            Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you’ve collected.

          - `payment_method_preview.card.generated_from.payment_method_details.card_present.description` (string, nullable)
            A high-level description of the type of cards issued in this range.

          - `payment_method_preview.card.generated_from.payment_method_details.card_present.emv_auth_data` (string, nullable)
            Authorization response cryptogram.

          - `payment_method_preview.card.generated_from.payment_method_details.card_present.exp_month` (integer)
            Two-digit number representing the card’s expiration month.

          - `payment_method_preview.card.generated_from.payment_method_details.card_present.exp_year` (integer)
            Four-digit number representing the card’s expiration year.

          - `payment_method_preview.card.generated_from.payment_method_details.card_present.fingerprint` (string, nullable)
            Uniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.

            *As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card—one for India and one for the rest of the world.*

          - `payment_method_preview.card.generated_from.payment_method_details.card_present.funding` (string, nullable)
            Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.

          - `payment_method_preview.card.generated_from.payment_method_details.card_present.generated_card` (string, nullable)
            ID of a card PaymentMethod generated from the card_present PaymentMethod that may be attached to a Customer for future transactions. Only present if it was possible to generate a card PaymentMethod.

          - `payment_method_preview.card.generated_from.payment_method_details.card_present.incremental_authorization_supported` (boolean)
            Whether this [PaymentIntent](https://docs.stripe.com/docs/api/payment_intents.md) is eligible for incremental authorizations. Request support using [request_incremental_authorization_support](https://docs.stripe.com/docs/api/payment_intents/create.md#create_payment_intent-payment_method_options-card_present-request_incremental_authorization_support).

          - `payment_method_preview.card.generated_from.payment_method_details.card_present.issuer` (string, nullable)
            The name of the card’s issuing bank.

          - `payment_method_preview.card.generated_from.payment_method_details.card_present.last4` (string, nullable)
            The last four digits of the card.

          - `payment_method_preview.card.generated_from.payment_method_details.card_present.network` (string, nullable)
            Identifies which network this charge was processed on. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `interac`, `jcb`, `link`, `mastercard`, `unionpay`, `visa`, or `unknown`.

          - `payment_method_preview.card.generated_from.payment_method_details.card_present.network_transaction_id` (string, nullable)
            This is used by the financial networks to identify a transaction. Visa calls this the Transaction ID, Mastercard calls this the Trace ID, and American Express calls this the Acquirer Reference Data. This value will be present if it is returned by the financial network in the authorization response, and null otherwise.

          - `payment_method_preview.card.generated_from.payment_method_details.card_present.offline` (object, nullable)
            Details about payments collected offline.

            - `payment_method_preview.card.generated_from.payment_method_details.card_present.offline.stored_at` (timestamp, nullable)
              Time at which the payment was collected while offline

            - `payment_method_preview.card.generated_from.payment_method_details.card_present.offline.type` (enum, nullable)
              The method used to process this payment method offline. Only deferred is allowed.
Possible enum values:
              - `deferred`

          - `payment_method_preview.card.generated_from.payment_method_details.card_present.overcapture_supported` (boolean)
            Defines whether the authorized amount can be over-captured or not

          - `payment_method_preview.card.generated_from.payment_method_details.card_present.preferred_locales` (array of strings, nullable)
            The languages that the issuing bank recommends using for localizing any customer-facing text, as read from the card. Referenced from EMV tag 5F2D, data encoded on the card’s chip.

          - `payment_method_preview.card.generated_from.payment_method_details.card_present.read_method` (enum, nullable)
            How card details were read in this transaction.
Possible enum values:
            - `contact_emv`
              Inserting a chip card into the card reader.

            - `contactless_emv`
              Tapping a contactless-enabled chip card or mobile wallet.

            - `contactless_magstripe_mode`
              Older standard for contactless payments that emulated a magnetic stripe read.

            - `magnetic_stripe_fallback`
              When inserting a chip card fails three times in a row, fallback to a magnetic stripe read.

            - `magnetic_stripe_track2`
              Swiping a card using the magnetic stripe reader.

          - `payment_method_preview.card.generated_from.payment_method_details.card_present.receipt` (object, nullable)
            A collection of fields required to be displayed on receipts. Only required for EMV transactions.

            - `payment_method_preview.card.generated_from.payment_method_details.card_present.receipt.account_type` (enum, nullable)
              The type of account being debited or credited
Possible enum values:
              - `checking`
                A checking account, as when using a debit card

              - `credit`
                A credit account, as when using a credit card

              - `prepaid`
                A prepaid account, as when using a debit gift card

              - `unknown`
                An unknown account

            - `payment_method_preview.card.generated_from.payment_method_details.card_present.receipt.application_cryptogram` (string, nullable)
              The Application Cryptogram, a unique value generated by the card to authenticate the transaction with issuers.

            - `payment_method_preview.card.generated_from.payment_method_details.card_present.receipt.application_preferred_name` (string, nullable)
              The Application Identifier (AID) on the card used to determine which networks are eligible to process the transaction. Referenced from EMV tag 9F12, data encoded on the card’s chip.

            - `payment_method_preview.card.generated_from.payment_method_details.card_present.receipt.authorization_code` (string, nullable)
              Identifier for this transaction.

            - `payment_method_preview.card.generated_from.payment_method_details.card_present.receipt.authorization_response_code` (string, nullable)
              EMV tag 8A. A code returned by the card issuer.

            - `payment_method_preview.card.generated_from.payment_method_details.card_present.receipt.cardholder_verification_method` (string, nullable)
              Describes the method used by the cardholder to verify ownership of the card. One of the following: `approval`, `failure`, `none`, `offline_pin`, `offline_pin_and_signature`, `online_pin`, or `signature`.

            - `payment_method_preview.card.generated_from.payment_method_details.card_present.receipt.dedicated_file_name` (string, nullable)
              Similar to the application_preferred_name, identifying the applications (AIDs) available on the card. Referenced from EMV tag 84.

            - `payment_method_preview.card.generated_from.payment_method_details.card_present.receipt.terminal_verification_results` (string, nullable)
              A 5-byte string that records the checks and validations that occur between the card and the terminal. These checks determine how the terminal processes the transaction and what risk tolerance is acceptable. Referenced from EMV Tag 95.

            - `payment_method_preview.card.generated_from.payment_method_details.card_present.receipt.transaction_status_information` (string, nullable)
              An indication of which steps were completed during the card read process. Referenced from EMV Tag 9B.

          - `payment_method_preview.card.generated_from.payment_method_details.card_present.wallet` (object, nullable)
            If a mobile wallet was presented in the transaction, this contains the details of the mobile wallet.

            - `payment_method_preview.card.generated_from.payment_method_details.card_present.wallet.type` (enum)
              The type of mobile wallet, one of `apple_pay`, `google_pay`, `samsung_pay`, or `unknown`.
Possible enum values:
              - `apple_pay`
                Apple Pay is a mobile payment service by Apple.

              - `google_pay`
                Google Pay is a mobile payment service by Google.

              - `samsung_pay`
                Samsung Pay is a mobile payment service by Samsung Electronics.

              - `unknown`
                The wallet provider is unknown.

        - `payment_method_preview.card.generated_from.payment_method_details.type` (string)
          The type of payment method transaction-specific details from the transaction that generated this `card` payment method. Always `card_present`.

      - `payment_method_preview.card.generated_from.setup_attempt` (string, nullable)
        The ID of the SetupAttempt that generated this PaymentMethod, if any.

    - `payment_method_preview.card.last4` (string)
      The last four digits of the card.

    - `payment_method_preview.card.networks` (object, nullable)
      Contains information about card networks that can be used to process the payment.

      - `payment_method_preview.card.networks.available` (array of strings)
        All networks available for selection via [payment_method_options.card.network](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-payment_method_options-card-network).

      - `payment_method_preview.card.networks.preferred` (string, nullable)
        The preferred network for co-branded cards. Can be `cartes_bancaires`, `mastercard`, `visa` or `invalid_preference` if requested network is not valid for the card.

    - `payment_method_preview.card.regulated_status` (enum, nullable)
      Status of a card based on the card issuer.
Possible enum values:
      - `regulated`
        The card falls under a regulated account range.

      - `unregulated`
        The card does not fall under a regulated account range.

    - `payment_method_preview.card.three_d_secure_usage` (object, nullable)
      Contains details on how this Card may be used for 3D Secure authentication.

      - `payment_method_preview.card.three_d_secure_usage.supported` (boolean)
        Whether 3D Secure is supported on this card.

    - `payment_method_preview.card.wallet` (object, nullable)
      If this Card is part of a card wallet, this contains the details of the card wallet.

      - `payment_method_preview.card.wallet.amex_express_checkout` (object, nullable)
        If this is a `amex_express_checkout` card wallet, this hash contains details about the wallet.

      - `payment_method_preview.card.wallet.apple_pay` (object, nullable)
        If this is a `apple_pay` card wallet, this hash contains details about the wallet.

      - `payment_method_preview.card.wallet.dynamic_last4` (string, nullable)
        (For tokenized numbers only.) The last four digits of the device account number.

      - `payment_method_preview.card.wallet.google_pay` (object, nullable)
        If this is a `google_pay` card wallet, this hash contains details about the wallet.

      - `payment_method_preview.card.wallet.link` (object, nullable)
        If this is a `link` card wallet, this hash contains details about the wallet.

      - `payment_method_preview.card.wallet.masterpass` (object, nullable)
        If this is a `masterpass` card wallet, this hash contains details about the wallet.

        - `payment_method_preview.card.wallet.masterpass.billing_address` (object, nullable)
          Owner’s verified billing address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

          - `payment_method_preview.card.wallet.masterpass.billing_address.city` (string, nullable)
            City, district, suburb, town, or village.

          - `payment_method_preview.card.wallet.masterpass.billing_address.country` (string, nullable)
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

          - `payment_method_preview.card.wallet.masterpass.billing_address.line1` (string, nullable)
            Address line 1, such as the street, PO Box, or company name.

          - `payment_method_preview.card.wallet.masterpass.billing_address.line2` (string, nullable)
            Address line 2, such as the apartment, suite, unit, or building.

          - `payment_method_preview.card.wallet.masterpass.billing_address.postal_code` (string, nullable)
            ZIP or postal code.

          - `payment_method_preview.card.wallet.masterpass.billing_address.state` (string, nullable)
            State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

        - `payment_method_preview.card.wallet.masterpass.email` (string, nullable)
          Owner’s verified email. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

        - `payment_method_preview.card.wallet.masterpass.name` (string, nullable)
          Owner’s verified full name. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

        - `payment_method_preview.card.wallet.masterpass.shipping_address` (object, nullable)
          Owner’s verified shipping address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

          - `payment_method_preview.card.wallet.masterpass.shipping_address.city` (string, nullable)
            City, district, suburb, town, or village.

          - `payment_method_preview.card.wallet.masterpass.shipping_address.country` (string, nullable)
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

          - `payment_method_preview.card.wallet.masterpass.shipping_address.line1` (string, nullable)
            Address line 1, such as the street, PO Box, or company name.

          - `payment_method_preview.card.wallet.masterpass.shipping_address.line2` (string, nullable)
            Address line 2, such as the apartment, suite, unit, or building.

          - `payment_method_preview.card.wallet.masterpass.shipping_address.postal_code` (string, nullable)
            ZIP or postal code.

          - `payment_method_preview.card.wallet.masterpass.shipping_address.state` (string, nullable)
            State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

      - `payment_method_preview.card.wallet.samsung_pay` (object, nullable)
        If this is a `samsung_pay` card wallet, this hash contains details about the wallet.

      - `payment_method_preview.card.wallet.type` (enum)
        The type of the card wallet, one of `amex_express_checkout`, `apple_pay`, `google_pay`, `masterpass`, `samsung_pay`, `visa_checkout`, or `link`. An additional hash is included on the Wallet subhash with a name matching this value. It contains additional information specific to the card wallet type.
Possible enum values:
        - `amex_express_checkout`
        - `apple_pay`
        - `google_pay`
        - `link`
        - `masterpass`
        - `samsung_pay`
        - `visa_checkout`

      - `payment_method_preview.card.wallet.visa_checkout` (object, nullable)
        If this is a `visa_checkout` card wallet, this hash contains details about the wallet.

        - `payment_method_preview.card.wallet.visa_checkout.billing_address` (object, nullable)
          Owner’s verified billing address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

          - `payment_method_preview.card.wallet.visa_checkout.billing_address.city` (string, nullable)
            City, district, suburb, town, or village.

          - `payment_method_preview.card.wallet.visa_checkout.billing_address.country` (string, nullable)
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

          - `payment_method_preview.card.wallet.visa_checkout.billing_address.line1` (string, nullable)
            Address line 1, such as the street, PO Box, or company name.

          - `payment_method_preview.card.wallet.visa_checkout.billing_address.line2` (string, nullable)
            Address line 2, such as the apartment, suite, unit, or building.

          - `payment_method_preview.card.wallet.visa_checkout.billing_address.postal_code` (string, nullable)
            ZIP or postal code.

          - `payment_method_preview.card.wallet.visa_checkout.billing_address.state` (string, nullable)
            State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

        - `payment_method_preview.card.wallet.visa_checkout.email` (string, nullable)
          Owner’s verified email. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

        - `payment_method_preview.card.wallet.visa_checkout.name` (string, nullable)
          Owner’s verified full name. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

        - `payment_method_preview.card.wallet.visa_checkout.shipping_address` (object, nullable)
          Owner’s verified shipping address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

          - `payment_method_preview.card.wallet.visa_checkout.shipping_address.city` (string, nullable)
            City, district, suburb, town, or village.

          - `payment_method_preview.card.wallet.visa_checkout.shipping_address.country` (string, nullable)
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

          - `payment_method_preview.card.wallet.visa_checkout.shipping_address.line1` (string, nullable)
            Address line 1, such as the street, PO Box, or company name.

          - `payment_method_preview.card.wallet.visa_checkout.shipping_address.line2` (string, nullable)
            Address line 2, such as the apartment, suite, unit, or building.

          - `payment_method_preview.card.wallet.visa_checkout.shipping_address.postal_code` (string, nullable)
            ZIP or postal code.

          - `payment_method_preview.card.wallet.visa_checkout.shipping_address.state` (string, nullable)
            State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

  - `payment_method_preview.card_present` (object, nullable)
    If this is a `card_present` PaymentMethod, this hash contains details about the Card Present payment method.

    - `payment_method_preview.card_present.brand` (string, nullable)
      Card brand. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `jcb`, `link`, `mastercard`, `unionpay`, `visa` or `unknown`.

    - `payment_method_preview.card_present.brand_product` (string, nullable)
      The [product code](https://stripe.com/docs/card-product-codes) that identifies the specific program or product associated with a card.

    - `payment_method_preview.card_present.cardholder_name` (string, nullable)
      The cardholder name as read from the card, in [ISO 7813](https://en.wikipedia.org/wiki/ISO/IEC_7813) format. May include alphanumeric characters, special characters and first/last name separator (`/`). In some cases, the cardholder name may not be available depending on how the issuer has configured the card. Cardholder name is typically not available on swipe or contactless payments, such as those made with Apple Pay and Google Pay.

    - `payment_method_preview.card_present.country` (string, nullable)
      Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you’ve collected.

    - `payment_method_preview.card_present.description` (string, nullable)
      A high-level description of the type of cards issued in this range.

    - `payment_method_preview.card_present.exp_month` (integer)
      Two-digit number representing the card’s expiration month.

    - `payment_method_preview.card_present.exp_year` (integer)
      Four-digit number representing the card’s expiration year.

    - `payment_method_preview.card_present.fingerprint` (string, nullable)
      Uniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.

      *As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card—one for India and one for the rest of the world.*

    - `payment_method_preview.card_present.funding` (string, nullable)
      Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.

    - `payment_method_preview.card_present.issuer` (string, nullable)
      The name of the card’s issuing bank.

    - `payment_method_preview.card_present.last4` (string, nullable)
      The last four digits of the card.

    - `payment_method_preview.card_present.networks` (object, nullable)
      Contains information about card networks that can be used to process the payment.

      - `payment_method_preview.card_present.networks.available` (array of strings)
        All networks available for selection via [payment_method_options.card.network](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-payment_method_options-card-network).

      - `payment_method_preview.card_present.networks.preferred` (string, nullable)
        The preferred network for the card.

    - `payment_method_preview.card_present.offline` (object, nullable)
      Details about payment methods collected offline.

      - `payment_method_preview.card_present.offline.stored_at` (timestamp, nullable)
        Time at which the payment was collected while offline

      - `payment_method_preview.card_present.offline.type` (enum, nullable)
        The method used to process this payment method offline. Only deferred is allowed.
Possible enum values:
        - `deferred`

    - `payment_method_preview.card_present.preferred_locales` (array of strings, nullable)
      The languages that the issuing bank recommends using for localizing any customer-facing text, as read from the card. Referenced from EMV tag 5F2D, data encoded on the card’s chip.

    - `payment_method_preview.card_present.read_method` (enum, nullable)
      How card details were read in this transaction.
Possible enum values:
      - `contact_emv`
        Inserting a chip card into the card reader.

      - `contactless_emv`
        Tapping a contactless-enabled chip card or mobile wallet.

      - `contactless_magstripe_mode`
        Older standard for contactless payments that emulated a magnetic stripe read.

      - `magnetic_stripe_fallback`
        When inserting a chip card fails three times in a row, fallback to a magnetic stripe read.

      - `magnetic_stripe_track2`
        Swiping a card using the magnetic stripe reader.

    - `payment_method_preview.card_present.wallet` (object, nullable)
      If a mobile wallet was presented in the transaction, this contains the details of the mobile wallet.

      - `payment_method_preview.card_present.wallet.type` (enum)
        The type of mobile wallet, one of `apple_pay`, `google_pay`, `samsung_pay`, or `unknown`.
Possible enum values:
        - `apple_pay`
          Apple Pay is a mobile payment service by Apple.

        - `google_pay`
          Google Pay is a mobile payment service by Google.

        - `samsung_pay`
          Samsung Pay is a mobile payment service by Samsung Electronics.

        - `unknown`
          The wallet provider is unknown.

  - `payment_method_preview.cashapp` (object, nullable)
    If this is a `cashapp` PaymentMethod, this hash contains details about the Cash App Pay payment method.

    - `payment_method_preview.cashapp.buyer_id` (string, nullable)
      A unique and immutable identifier assigned by Cash App to every buyer.

    - `payment_method_preview.cashapp.cashtag` (string, nullable)
      A public identifier for buyers using Cash App.

  - `payment_method_preview.crypto` (object, nullable)
    If this is a Crypto PaymentMethod, this hash contains details about the Crypto payment method.

  - `payment_method_preview.customer` (string, nullable)
    The ID of the Customer to which this PaymentMethod is saved. This will not be set when the PaymentMethod has not been saved to a Customer.

  - `payment_method_preview.customer_balance` (object, nullable)
    If this is a `customer_balance` PaymentMethod, this hash contains details about the CustomerBalance payment method.

  - `payment_method_preview.eps` (object, nullable)
    If this is an `eps` PaymentMethod, this hash contains details about the EPS payment method.

    - `payment_method_preview.eps.bank` (enum, nullable)
      The customer’s bank. Should be one of `arzte_und_apotheker_bank`, `austrian_anadi_bank_ag`, `bank_austria`, `bankhaus_carl_spangler`, `bankhaus_schelhammer_und_schattera_ag`, `bawag_psk_ag`, `bks_bank_ag`, `brull_kallmus_bank_ag`, `btv_vier_lander_bank`, `capital_bank_grawe_gruppe_ag`, `deutsche_bank_ag`, `dolomitenbank`, `easybank_ag`, `erste_bank_und_sparkassen`, `hypo_alpeadriabank_international_ag`, `hypo_noe_lb_fur_niederosterreich_u_wien`, `hypo_oberosterreich_salzburg_steiermark`, `hypo_tirol_bank_ag`, `hypo_vorarlberg_bank_ag`, `hypo_bank_burgenland_aktiengesellschaft`, `marchfelder_bank`, `oberbank_ag`, `raiffeisen_bankengruppe_osterreich`, `schoellerbank_ag`, `sparda_bank_wien`, `volksbank_gruppe`, `volkskreditbank_ag`, or `vr_bank_braunau`.
Possible enum values:
      - `arzte_und_apotheker_bank`
      - `austrian_anadi_bank_ag`
      - `bank_austria`
      - `bankhaus_carl_spangler`
      - `bankhaus_schelhammer_und_schattera_ag`
      - `bawag_psk_ag`
      - `bks_bank_ag`
      - `brull_kallmus_bank_ag`
      - `btv_vier_lander_bank`
      - `capital_bank_grawe_gruppe_ag`
      - `deutsche_bank_ag`
      - `dolomitenbank`
      - `easybank_ag`
      - `erste_bank_und_sparkassen`
      - `hypo_alpeadriabank_international_ag`
      - `hypo_bank_burgenland_aktiengesellschaft`
      - `hypo_noe_lb_fur_niederosterreich_u_wien`
      - `hypo_oberosterreich_salzburg_steiermark`
      - `hypo_tirol_bank_ag`
      - `hypo_vorarlberg_bank_ag`
      - `marchfelder_bank`
      - `oberbank_ag`
      - `raiffeisen_bankengruppe_osterreich`
      - `schoellerbank_ag`
      - `sparda_bank_wien`
      - `volksbank_gruppe`
      - `volkskreditbank_ag`
      - `vr_bank_braunau`

  - `payment_method_preview.fpx` (object, nullable)
    If this is an `fpx` PaymentMethod, this hash contains details about the FPX payment method.

    - `payment_method_preview.fpx.bank` (enum)
      The customer’s bank, if provided. Can be one of `affin_bank`, `agrobank`, `alliance_bank`, `ambank`, `bank_islam`, `bank_muamalat`, `bank_rakyat`, `bsn`, `cimb`, `hong_leong_bank`, `hsbc`, `kfh`, `maybank2u`, `ocbc`, `public_bank`, `rhb`, `standard_chartered`, `uob`, `deutsche_bank`, `maybank2e`, `pb_enterprise`, or `bank_of_china`.
Possible enum values:
      - `affin_bank`
      - `agrobank`
      - `alliance_bank`
      - `ambank`
      - `bank_islam`
      - `bank_muamalat`
      - `bank_of_china`
      - `bank_rakyat`
      - `bsn`
      - `cimb`
      - `deutsche_bank`
      - `hong_leong_bank`
      - `hsbc`
      - `kfh`
      - `maybank2e`
      - `maybank2u`
      - `ocbc`
      - `pb_enterprise`
      - `public_bank`
      - `rhb`
      - `standard_chartered`
      - `uob`

  - `payment_method_preview.giropay` (object, nullable)
    If this is a `giropay` PaymentMethod, this hash contains details about the Giropay payment method.

  - `payment_method_preview.grabpay` (object, nullable)
    If this is a `grabpay` PaymentMethod, this hash contains details about the GrabPay payment method.

  - `payment_method_preview.ideal` (object, nullable)
    If this is an `ideal` PaymentMethod, this hash contains details about the iDEAL payment method.

    - `payment_method_preview.ideal.bank` (enum, nullable)
      The customer’s bank, if provided. Can be one of `abn_amro`, `asn_bank`, `bunq`, `buut`, `finom`, `handelsbanken`, `ing`, `knab`, `mollie`, `moneyou`, `n26`, `nn`, `rabobank`, `regiobank`, `revolut`, `sns_bank`, `triodos_bank`, `van_lanschot`, or `yoursafe`.
Possible enum values:
      - `abn_amro`
      - `asn_bank`
      - `bunq`
      - `buut`
      - `finom`
      - `handelsbanken`
      - `ing`
      - `knab`
      - `mollie`
      - `moneyou`
      - `n26`
      - `nn`
      - `rabobank`
      - `regiobank`
      - `revolut`
      - `sns_bank`
      - `triodos_bank`
      - `van_lanschot`
      - `yoursafe`

    - `payment_method_preview.ideal.bic` (enum, nullable)
      The Bank Identifier Code of the customer’s bank, if the bank was provided.
Possible enum values:
      - `ABNANL2A`
      - `ASNBNL21`
      - `BITSNL2A`
      - `BUNQNL2A`
      - `BUUTNL2A`
      - `FNOMNL22`
      - `FVLBNL22`
      - `HANDNL2A`
      - `INGBNL2A`
      - `KNABNL2H`
      - `MLLENL2A`
      - `MOYONL21`
      - `NNBANL2G`
      - `NTSBDEB1`
      - `RABONL2U`
      - `RBRBNL21`
      - `REVOIE23`
      - `REVOLT21`
      - `SNSBNL2A`
      - `TRIONL2U`

  - `payment_method_preview.interac_present` (object, nullable)
    If this is an `interac_present` PaymentMethod, this hash contains details about the Interac Present payment method.

    - `payment_method_preview.interac_present.brand` (string, nullable)
      Card brand. Can be `interac`, `mastercard` or `visa`.

    - `payment_method_preview.interac_present.cardholder_name` (string, nullable)
      The cardholder name as read from the card, in [ISO 7813](https://en.wikipedia.org/wiki/ISO/IEC_7813) format. May include alphanumeric characters, special characters and first/last name separator (`/`). In some cases, the cardholder name may not be available depending on how the issuer has configured the card. Cardholder name is typically not available on swipe or contactless payments, such as those made with Apple Pay and Google Pay.

    - `payment_method_preview.interac_present.country` (string, nullable)
      Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you’ve collected.

    - `payment_method_preview.interac_present.description` (string, nullable)
      A high-level description of the type of cards issued in this range.

    - `payment_method_preview.interac_present.exp_month` (integer)
      Two-digit number representing the card’s expiration month.

    - `payment_method_preview.interac_present.exp_year` (integer)
      Four-digit number representing the card’s expiration year.

    - `payment_method_preview.interac_present.fingerprint` (string, nullable)
      Uniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.

      *As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card—one for India and one for the rest of the world.*

    - `payment_method_preview.interac_present.funding` (string, nullable)
      Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.

    - `payment_method_preview.interac_present.issuer` (string, nullable)
      The name of the card’s issuing bank.

    - `payment_method_preview.interac_present.last4` (string, nullable)
      The last four digits of the card.

    - `payment_method_preview.interac_present.networks` (object, nullable)
      Contains information about card networks that can be used to process the payment.

      - `payment_method_preview.interac_present.networks.available` (array of strings)
        All networks available for selection via [payment_method_options.card.network](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-payment_method_options-card-network).

      - `payment_method_preview.interac_present.networks.preferred` (string, nullable)
        The preferred network for the card.

    - `payment_method_preview.interac_present.preferred_locales` (array of strings, nullable)
      The languages that the issuing bank recommends using for localizing any customer-facing text, as read from the card. Referenced from EMV tag 5F2D, data encoded on the card’s chip.

    - `payment_method_preview.interac_present.read_method` (enum, nullable)
      How card details were read in this transaction.
Possible enum values:
      - `contact_emv`
        Inserting a chip card into the card reader.

      - `contactless_emv`
        Tapping a contactless-enabled chip card or mobile wallet.

      - `contactless_magstripe_mode`
        Older standard for contactless payments that emulated a magnetic stripe read.

      - `magnetic_stripe_fallback`
        When inserting a chip card fails three times in a row, fallback to a magnetic stripe read.

      - `magnetic_stripe_track2`
        Swiping a card using the magnetic stripe reader.

  - `payment_method_preview.kakao_pay` (object, nullable)
    If this is a `kakao_pay` PaymentMethod, this hash contains details about the Kakao Pay payment method.

  - `payment_method_preview.klarna` (object, nullable)
    If this is a `klarna` PaymentMethod, this hash contains details about the Klarna payment method.

    - `payment_method_preview.klarna.dob` (object, nullable)
      The customer’s date of birth, if provided.

      - `payment_method_preview.klarna.dob.day` (integer, nullable)
        The day of birth, between 1 and 31.

      - `payment_method_preview.klarna.dob.month` (integer, nullable)
        The month of birth, between 1 and 12.

      - `payment_method_preview.klarna.dob.year` (integer, nullable)
        The four-digit year of birth.

  - `payment_method_preview.konbini` (object, nullable)
    If this is a `konbini` PaymentMethod, this hash contains details about the Konbini payment method.

  - `payment_method_preview.kr_card` (object, nullable)
    If this is a `kr_card` PaymentMethod, this hash contains details about the Korean Card payment method.

    - `payment_method_preview.kr_card.brand` (enum, nullable)
      The local credit or debit card brand.
Possible enum values:
      - `bc`
        BC

      - `citi`
        Citi

      - `hana`
        Hana

      - `hyundai`
        Hyundai

      - `jeju`
        Jeju

      - `jeonbuk`
        Jeonbuk

      - `kakaobank`
        Kakao Bank

      - `kbank`
        KBank

      - `kdbbank`
        KDB Bank

      - `kookmin`
        Kookmin

      - `kwangju`
        Kwangju

      - `lotte`
        Lotte

      - `mg`
        MG

      - `nh`
        NG

      - `post`
        Post

      - `samsung`
        Samsung

      - `savingsbank`
        Savings Bank

      - `shinhan`
        Shinhan

      - `shinhyup`
        Shinhyup

      - `suhyup`
        Suhyup

      - `tossbank`
        Toss Bank

      - `woori`
        Woori

    - `payment_method_preview.kr_card.last4` (string, nullable)
      The last four digits of the card. This may not be present for American Express cards.

      The maximum length is 4 characters.

  - `payment_method_preview.link` (object, nullable)
    If this is an `Link` PaymentMethod, this hash contains details about the Link payment method.

    - `payment_method_preview.link.email` (string, nullable)
      Account owner’s email address.

  - `payment_method_preview.mb_way` (object, nullable)
    If this is a MB WAY PaymentMethod, this hash contains details about the MB WAY payment method.

  - `payment_method_preview.mobilepay` (object, nullable)
    If this is a `mobilepay` PaymentMethod, this hash contains details about the MobilePay payment method.

  - `payment_method_preview.multibanco` (object, nullable)
    If this is a `multibanco` PaymentMethod, this hash contains details about the Multibanco payment method.

  - `payment_method_preview.naver_pay` (object, nullable)
    If this is a `naver_pay` PaymentMethod, this hash contains details about the Naver Pay payment method.

    - `payment_method_preview.naver_pay.buyer_id` (string, nullable)
      Uniquely identifies this particular Naver Pay account. You can use this attribute to check whether two Naver Pay accounts are the same.

    - `payment_method_preview.naver_pay.funding` (enum)
      Whether to fund this transaction with Naver Pay points or a card.
Possible enum values:
      - `card`
        Use a card to fund this transaction.

      - `points`
        Use Naver Pay points to fund this transaction.

  - `payment_method_preview.nz_bank_account` (object, nullable)
    If this is an nz_bank_account PaymentMethod, this hash contains details about the nz_bank_account payment method.

    - `payment_method_preview.nz_bank_account.account_holder_name` (string, nullable)
      The name on the bank account. Only present if the account holder name is different from the name of the authorized signatory collected in the PaymentMethod’s billing details.

    - `payment_method_preview.nz_bank_account.bank_code` (string)
      The numeric code for the bank account’s bank.

    - `payment_method_preview.nz_bank_account.bank_name` (string)
      The name of the bank.

    - `payment_method_preview.nz_bank_account.branch_code` (string)
      The numeric code for the bank account’s bank branch.

    - `payment_method_preview.nz_bank_account.last4` (string)
      Last four digits of the bank account number.

    - `payment_method_preview.nz_bank_account.suffix` (string, nullable)
      The suffix of the bank account number.

  - `payment_method_preview.oxxo` (object, nullable)
    If this is an `oxxo` PaymentMethod, this hash contains details about the OXXO payment method.

  - `payment_method_preview.p24` (object, nullable)
    If this is a `p24` PaymentMethod, this hash contains details about the P24 payment method.

    - `payment_method_preview.p24.bank` (enum, nullable)
      The customer’s bank, if provided.

  - `payment_method_preview.pay_by_bank` (object, nullable)
    If this is a `pay_by_bank` PaymentMethod, this hash contains details about the PayByBank payment method.

  - `payment_method_preview.payco` (object, nullable)
    If this is a `payco` PaymentMethod, this hash contains details about the PAYCO payment method.

  - `payment_method_preview.paynow` (object, nullable)
    If this is a `paynow` PaymentMethod, this hash contains details about the PayNow payment method.

  - `payment_method_preview.paypal` (object, nullable)
    If this is a `paypal` PaymentMethod, this hash contains details about the PayPal payment method.

    - `payment_method_preview.paypal.country` (string, nullable)
      Two-letter ISO code representing the buyer’s country. Values are provided by PayPal directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

    - `payment_method_preview.paypal.payer_email` (string, nullable)
      Owner’s email. Values are provided by PayPal directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

    - `payment_method_preview.paypal.payer_id` (string, nullable)
      PayPal account PayerID. This identifier uniquely identifies the PayPal customer.

  - `payment_method_preview.paypay` (object, nullable)
    If this is a `paypay` PaymentMethod, this hash contains details about the PayPay payment method.

  - `payment_method_preview.payto` (object, nullable)
    If this is a `payto` PaymentMethod, this hash contains details about the PayTo payment method.

    - `payment_method_preview.payto.bsb_number` (string, nullable)
      Bank-State-Branch number of the bank account.

    - `payment_method_preview.payto.last4` (string, nullable)
      Last four digits of the bank account number.

    - `payment_method_preview.payto.pay_id` (string, nullable)
      The PayID alias for the bank account.

  - `payment_method_preview.pix` (object, nullable)
    If this is a `pix` PaymentMethod, this hash contains details about the Pix payment method.

  - `payment_method_preview.promptpay` (object, nullable)
    If this is a `promptpay` PaymentMethod, this hash contains details about the PromptPay payment method.

  - `payment_method_preview.revolut_pay` (object, nullable)
    If this is a `revolut_pay` PaymentMethod, this hash contains details about the Revolut Pay payment method.

  - `payment_method_preview.samsung_pay` (object, nullable)
    If this is a `samsung_pay` PaymentMethod, this hash contains details about the SamsungPay payment method.

  - `payment_method_preview.satispay` (object, nullable)
    If this is a `satispay` PaymentMethod, this hash contains details about the Satispay payment method.

  - `payment_method_preview.sepa_debit` (object, nullable)
    If this is a `sepa_debit` PaymentMethod, this hash contains details about the SEPA debit bank account.

    - `payment_method_preview.sepa_debit.bank_code` (string, nullable)
      Bank code of bank associated with the bank account.

    - `payment_method_preview.sepa_debit.branch_code` (string, nullable)
      Branch code of bank associated with the bank account.

    - `payment_method_preview.sepa_debit.country` (string, nullable)
      Two-letter ISO code representing the country the bank account is located in.

    - `payment_method_preview.sepa_debit.fingerprint` (string, nullable)
      Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

    - `payment_method_preview.sepa_debit.generated_from` (object, nullable)
      Information about the object that generated this PaymentMethod.

      - `payment_method_preview.sepa_debit.generated_from.charge` (string, nullable)
        The ID of the Charge that generated this PaymentMethod, if any.

      - `payment_method_preview.sepa_debit.generated_from.setup_attempt` (string, nullable)
        The ID of the SetupAttempt that generated this PaymentMethod, if any.

    - `payment_method_preview.sepa_debit.last4` (string, nullable)
      Last four characters of the IBAN.

  - `payment_method_preview.sofort` (object, nullable)
    If this is a `sofort` PaymentMethod, this hash contains details about the SOFORT payment method.

    - `payment_method_preview.sofort.country` (string, nullable)
      Two-letter ISO code representing the country the bank account is located in.

  - `payment_method_preview.swish` (object, nullable)
    If this is a `swish` PaymentMethod, this hash contains details about the Swish payment method.

  - `payment_method_preview.twint` (object, nullable)
    If this is a TWINT PaymentMethod, this hash contains details about the TWINT payment method.

  - `payment_method_preview.type` (enum)
    The type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type.
Possible enum values:
    - `acss_debit`
      [Pre-authorized debit payments](https://docs.stripe.com/docs/payments/acss-debit.md) are used to debit Canadian bank accounts through the Automated Clearing Settlement System (ACSS).

    - `affirm`
      [Affirm](https://docs.stripe.com/docs/payments/affirm.md) is a buy now, pay later payment method in the US.

    - `afterpay_clearpay`
      [Afterpay / Clearpay](https://docs.stripe.com/docs/payments/afterpay-clearpay.md) is a buy now, pay later payment method used in Australia, Canada, France, New Zealand, Spain, the UK, and the US.

    - `alipay`
      [Alipay](https://docs.stripe.com/docs/payments/alipay.md) is a digital wallet payment method used in China.

    - `alma`
      [Alma](https://docs.stripe.com/docs/payments/alma.md) is a Buy Now, Pay Later payment method that lets customers pay in 2, 3, or 4 installments.

    - `amazon_pay`
      [Amazon Pay](https://docs.stripe.com/docs/payments/amazon-pay.md) is a Wallet payment method that lets hundreds of millions of Amazon customers pay their way, every day.

    - `au_becs_debit`
      [BECS Direct Debit](https://docs.stripe.com/docs/payments/au-becs-debit.md) is used to debit Australian bank accounts through the Bulk Electronic Clearing System (BECS).

    - `bacs_debit`
      [Bacs Direct Debit](https://docs.stripe.com/docs/payments/payment-methods/bacs-debit.md) is used to debit UK bank accounts.

    - `bancontact`
      [Bancontact](https://docs.stripe.com/docs/payments/bancontact.md) is a bank redirect payment method used in Belgium.

    - `billie`
      [Billie](https://docs.stripe.com/docs/payments/billie.md) is a payment method.

    - `blik`
      [BLIK](https://docs.stripe.com/docs/payments/blik.md) is a single-use payment method common in Poland.

    - `boleto`
      [Boleto](https://docs.stripe.com/docs/payments/boleto.md) is a voucher-based payment method used in Brazil.

    - `card`
      [Card payments](https://docs.stripe.com/docs/payments/payment-methods/overview.md#cards) are supported through many networks, card brands, and select Link funding sources.

    - `card_present`
      [Stripe Terminal](https://docs.stripe.com/docs/terminal/payments/collect-card-payment.md) is used to collect in-person card payments.

    - `cashapp`
      [Cash App Pay](https://docs.stripe.com/docs/payments/cash-app-pay.md) enables customers to frictionlessly authenticate payments in the Cash App using their stored balance or linked card.

    - `crypto`
      [Stablecoin payments](https://docs.stripe.com/docs/payments/stablecoin-payments.md) enable customers to pay in stablecoins like USDC from 100s of wallets including Phantom and Metamask.

    - `custom`
      Custom payment methods are user-defined payment methods that Stripe doesn’t process. You can’t use them in PaymentIntents or SetupIntents.

    - `customer_balance`
      Uses a customer’s [cash balance](https://docs.stripe.com/docs/payments/customer-balance.md) for the payment.

    - `eps`
      [EPS](https://docs.stripe.com/docs/payments/eps.md) is an Austria-based bank redirect payment method.

    - `fpx`
      [FPX](https://docs.stripe.com/docs/payments/fpx.md) is a Malaysia-based bank redirect payment method.

    - `giropay`
      [giropay](https://docs.stripe.com/docs/payments/giropay.md) is a German bank redirect payment method.

    - `grabpay`
      [GrabPay](https://docs.stripe.com/docs/payments/grabpay.md) is a digital wallet payment method used in Southeast Asia.

    - `ideal`
      [iDEAL](https://docs.stripe.com/docs/payments/ideal.md) is a Netherlands-based bank redirect payment method.

    - `interac_present`
      [Stripe Terminal](https://docs.stripe.com/docs/terminal/payments/collect-card-payment.md) accepts [Interac](https://docs.stripe.com/docs/terminal/payments/regional.md?integration-country=CA#interac-payments) debit cards for in-person payments in Canada.

    - `kakao_pay`
      [Kakao Pay](https://docs.stripe.com/docs/payments/kakao-pay/accept-a-payment.md) is a digital wallet payment method used in South Korea.

    - `klarna`
      [Klarna](https://docs.stripe.com/docs/payments/klarna.md) is a global buy now, pay later payment method.

    - `konbini`
      [Konbini](https://docs.stripe.com/docs/payments/konbini.md) is a cash-based voucher payment method used in Japan.

    - `kr_card`
      [Korean cards](https://docs.stripe.com/docs/payments/kr-card/accept-a-payment.md) enables customers to accept local credit and debit cards in South Korea.

    - `link`
      [Link](https://docs.stripe.com/docs/payments/link.md) allows customers to pay with their saved payment details.

    - `mb_way`
      MB WAY is a payment method.

    - `mobilepay`
      [MobilePay](https://docs.stripe.com/docs/payments/mobilepay.md) is a Nordic card-passthrough wallet payment method where customers authorize the payment in the MobilePay application.

    - `multibanco`
      [Multibanco](https://docs.stripe.com/docs/payments/multibanco.md) is a voucher payment method

    - `naver_pay`
      [Naver Pay](https://docs.stripe.com/docs/payments/naver-pay/accept-a-payment.md) is a digital wallet payment method used in South Korea.

    - `nz_bank_account`
      [New Zealand BECS Direct Debit](https://docs.stripe.com/docs/payments/nz-bank-account.md) is used to debit New Zealand bank accounts through the Bulk Electronic Clearing System (BECS).

    - `oxxo`
      [OXXO](https://docs.stripe.com/docs/payments/oxxo.md) is a cash-based voucher payment method used in Mexico.

    - `p24`
      [Przelewy24](https://docs.stripe.com/docs/payments/p24.md) is a bank redirect payment method used in Poland.

    - `pay_by_bank`
      [Pay By Bank](https://docs.stripe.com/docs/payments/pay-by-bank.md) is an open banking payment method in the UK.

    - `payco`
      [PAYCO](https://docs.stripe.com/docs/payments/payco/accept-a-payment.md) is a digital wallet payment method used in South Korea.

    - `paynow`
      [PayNow](https://docs.stripe.com/docs/payments/paynow.md) is a QR code payment method used in Singapore.

    - `paypal`
      [PayPal](https://docs.stripe.com/docs/payments/paypal.md) is an online wallet and redirect payment method commonly used in Europe.

    - `paypay`
      [PayPay](https://docs.stripe.com/docs/payments/paypay.md) is a payment method.

    - `payto`
      [PayTo](https://docs.stripe.com/docs/payments/payto.md) is a real time payment method

    - `pix`
      [Pix](https://docs.stripe.com/docs/payments/pix.md) is an instant bank transfer payment method in Brazil.

    - `promptpay`
      [PromptPay](https://docs.stripe.com/docs/payments/promptpay.md) is an instant funds transfer service popular in Thailand.

    - `revolut_pay`
      [Revolut Pay](https://docs.stripe.com/docs/payments/revolut-pay.md) is a digital wallet payment method used in the United Kingdom.

    - `samsung_pay`
      [Samsung Pay](https://docs.stripe.com/docs/payments/samsung-pay/accept-a-payment.md) is a digital wallet payment method used in South Korea.

    - `satispay`
      [Satispay](https://docs.stripe.com/docs/payments/satispay.md) is a payment method.

    - `sepa_debit`
      [SEPA Direct Debit](https://docs.stripe.com/docs/payments/sepa-debit.md) is used to debit bank accounts within the Single Euro Payments Area (SEPA) region.

    - `sofort`
      [Sofort](https://docs.stripe.com/docs/payments/sofort.md) is a bank redirect payment method used in Europe.

    - `swish`
      [Swish](https://docs.stripe.com/docs/payments/swish.md) is a Swedish wallet payment method where customers authorize the payment in the Swish application.

    - `twint`
      [TWINT](https://docs.stripe.com/docs/payments/twint.md) is a single-use payment method used in Switzerland.

    - `us_bank_account`
      [ACH Direct Debit](https://docs.stripe.com/docs/payments/ach-direct-debit.md) is used to debit US bank accounts through the Automated Clearing House (ACH) payments system.

    - `wechat_pay`
      [WeChat Pay](https://docs.stripe.com/docs/payments/wechat-pay.md) is a digital wallet payment method based in China.

    - `zip`
      [Zip](https://docs.stripe.com/docs/payments/zip.md) is a Buy now, pay later Payment Method

  - `payment_method_preview.us_bank_account` (object, nullable)
    If this is an `us_bank_account` PaymentMethod, this hash contains details about the US bank account payment method.

    - `payment_method_preview.us_bank_account.account_holder_type` (enum, nullable)
      Account holder type: individual or company.
Possible enum values:
      - `company`
        Account belongs to a company

      - `individual`
        Account belongs to an individual

    - `payment_method_preview.us_bank_account.account_type` (enum, nullable)
      Account type: checkings or savings. Defaults to checking if omitted.
Possible enum values:
      - `checking`
        Bank account type is checking

      - `savings`
        Bank account type is savings

    - `payment_method_preview.us_bank_account.bank_name` (string, nullable)
      The name of the bank.

    - `payment_method_preview.us_bank_account.financial_connections_account` (string, nullable)
      The ID of the Financial Connections Account used to create the payment method.

    - `payment_method_preview.us_bank_account.fingerprint` (string, nullable)
      Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

    - `payment_method_preview.us_bank_account.last4` (string, nullable)
      Last four digits of the bank account number.

    - `payment_method_preview.us_bank_account.networks` (object, nullable)
      Contains information about US bank account networks that can be used.

      - `payment_method_preview.us_bank_account.networks.preferred` (string, nullable)
        The preferred network.

      - `payment_method_preview.us_bank_account.networks.supported` (array of enums)
        All supported networks.
Possible enum values:
        - `ach`
        - `us_domestic_wire`

    - `payment_method_preview.us_bank_account.routing_number` (string, nullable)
      Routing number of the bank account.

    - `payment_method_preview.us_bank_account.status_details` (object, nullable)
      Contains information about the future reusability of this PaymentMethod.

      - `payment_method_preview.us_bank_account.status_details.blocked` (object, nullable)
        Contains more information about the underlying block. This field will only be rendered if the PaymentMethod is blocked.

        - `payment_method_preview.us_bank_account.status_details.blocked.network_code` (enum, nullable)
          The ACH network code that resulted in this block.
Possible enum values:
          - `R02`
            Account Closed

          - `R03`
            No Account, Unable to Locate Account

          - `R04`
            Invalid Account Number Structure

          - `R05`
            Unauthorized Debit to Consumer Account Using Corporate SEC Code

          - `R07`
            Authorization Revoked By Consumer

          - `R08`
            Payment Stopped

          - `R10`
            Customer Advises Originator is Not Known to Receiver and/or Originator is Not Authorized by Receiver to Debit Receiver’s Account

          - `R11`
            Customer Advises Entry Not in Accordance with the Terms of Authorization

          - `R16`
            Account Frozen, Entry Returned Per OFAC Instructions

          - `R20`
            Non-Transaction Account

          - `R29`
            Corporate Customer Advises Not Authorized

          - `R31`
            Permissible Return Entry (CCD and CTX only)

        - `payment_method_preview.us_bank_account.status_details.blocked.reason` (enum, nullable)
          The reason why this PaymentMethod’s fingerprint has been blocked
Possible enum values:
          - `bank_account_closed`
            Bank account has been closed.

          - `bank_account_frozen`
            Bank account has been frozen.

          - `bank_account_invalid_details`
            Bank account details are incorrect. Please check the account number, routing number, account holder name, and account type.

          - `bank_account_restricted`
            Bank account does not support debits.

          - `bank_account_unusable`
            Bank account has been blocked by Stripe. Please contact Support.

          - `debit_not_authorized`
            Customer has disputed a previous payment with their bank. If the `network_code` is R29, please confirm that Stripe’s Company IDs are allowlisted before attempting additional payments.

          - `tokenized_account_number_deactivated`
            Bank account’s tokenized account number is invalid. Please use a different account.

  - `payment_method_preview.wechat_pay` (object, nullable)
    If this is an `wechat_pay` PaymentMethod, this hash contains details about the wechat_pay payment method.

  - `payment_method_preview.zip` (object, nullable)
    If this is a `zip` PaymentMethod, this hash contains details about the Zip payment method.

- `return_url` (string, nullable)
  Return URL used to confirm the Intent.

- `setup_future_usage` (enum, nullable)
  Indicates that you intend to make future payments with this ConfirmationToken’s payment method.

  The presence of this property will [attach the payment method](https://docs.stripe.com/docs/payments/save-during-payment.md) to the PaymentIntent’s Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete.
Possible enum values:
  - `off_session`
    Use `off_session` if your customer may or may not be present in your checkout flow.

  - `on_session`
    Use `on_session` if you intend to only reuse the payment method when your customer is present in your checkout flow.

- `setup_intent` (string, nullable)
  ID of the SetupIntent that this ConfirmationToken was used to confirm, or null if this ConfirmationToken has not yet been used.

- `shipping` (object, nullable)
  Shipping information collected on this ConfirmationToken.

  - `shipping.address` (object)
    Shipping address.

    - `shipping.address.city` (string, nullable)
      City, district, suburb, town, or village.

    - `shipping.address.country` (string, nullable)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `shipping.address.line1` (string, nullable)
      Address line 1, such as the street, PO Box, or company name.

    - `shipping.address.line2` (string, nullable)
      Address line 2, such as the apartment, suite, unit, or building.

    - `shipping.address.postal_code` (string, nullable)
      ZIP or postal code.

    - `shipping.address.state` (string, nullable)
      State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

  - `shipping.name` (string)
    Recipient name.

  - `shipping.phone` (string, nullable)
    Recipient phone (including extension).

- `use_stripe_sdk` (boolean)
  Indicates whether the Stripe SDK is used to handle confirmation flow. Defaults to `true` on ConfirmationToken.

### The Confirmation Token object

```json
{
  "id": "ctoken_1NnQUf2eZvKYlo2CIObdtbnb",
  "object": "confirmation_token",
  "created": 1694025025,
  "expires_at": 1694068225,
  "livemode": true,
  "mandate_data": null,
  "payment_intent": null,
  "payment_method": null,
  "payment_method_preview": {
    "billing_details": {
      "address": {
        "city": "Hyde Park",
        "country": "US",
        "line1": "50 Sprague St",
        "line2": "",
        "postal_code": "02136",
        "state": "MA"
      },
      "email": "jennyrosen@stripe.com",
      "name": "Jenny Rosen",
      "phone": null
    },
    "card": {
      "brand": "visa",
      "checks": {
        "address_line1_check": null,
        "address_postal_code_check": null,
        "cvc_check": null
      },
      "country": "US",
      "display_brand": "visa",
      "exp_month": 8,
      "exp_year": 2026,
      "funding": "credit",
      "generated_from": null,
      "last4": "4242",
      "networks": {
        "available": [
          "visa"
        ],
        "preferred": null
      },
      "three_d_secure_usage": {
        "supported": true
      },
      "wallet": null
    },
    "type": "card"
  },
  "return_url": "https://example.com/return",
  "setup_future_usage": "off_session",
  "setup_intent": null,
  "shipping": {
    "address": {
      "city": "Hyde Park",
      "country": "US",
      "line1": "50 Sprague St",
      "line2": "",
      "postal_code": "02136",
      "state": "MA"
    },
    "name": "Jenny Rosen",
    "phone": null
  }
}
```