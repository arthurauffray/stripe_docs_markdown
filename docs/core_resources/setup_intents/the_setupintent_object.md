# The SetupIntent object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `application` (string, nullable)
  ID of the Connect application that created the SetupIntent.

- `attach_to_self` (boolean, nullable)
  If present, the SetupIntent’s payment method will be attached to the in-context Stripe Account.

  It can only be used for this Stripe Account’s own money movement flows like InboundTransfer and OutboundTransfers. It cannot be set to true when setting up a PaymentMethod for a Customer, and defaults to false when attaching a PaymentMethod to a Customer.

- `automatic_payment_methods` (object, nullable)
  Settings for dynamic payment methods compatible with this Setup Intent

  - `automatic_payment_methods.allow_redirects` (enum, nullable)
    Controls whether this SetupIntent will accept redirect-based payment methods.

    Redirect-based payment methods may require your customer to be redirected to a payment method’s app or site for authentication or additional steps. To [confirm](https://docs.stripe.com/docs/api/setup_intents/confirm.md) this SetupIntent, you may be required to provide a `return_url` to redirect customers back to your site after they authenticate or complete the setup.
Possible enum values:
    - `always`
      (Default) This SetupIntent will accept redirect-based payment methods. `return_url` may be required to       [confirm](https://docs.stripe.com/docs/api/setup_intents/confirm.md) this SetupIntent.

    - `never`
      This SetupIntent will not accept redirect-based payment methods. Payment methods that require redirect will       be filtered. `return_url` will not be required to [confirm](https://docs.stripe.com/docs/api/setup_intents/confirm.md) this       SetupIntent.

  - `automatic_payment_methods.enabled` (boolean, nullable)
    Automatically calculates compatible payment methods

- `cancellation_reason` (enum, nullable)
  Reason for cancellation of this SetupIntent, one of `abandoned`, `requested_by_customer`, or `duplicate`.
Possible enum values:
  - `abandoned`
  - `duplicate`
  - `requested_by_customer`

- `client_secret` (string, nullable)
  The client secret of this SetupIntent. Used for client-side retrieval using a publishable key.

  The client secret can be used to complete payment setup from your frontend. It should not be stored, logged, or exposed to anyone other than the customer. Make sure that you have TLS enabled on any page that includes the client secret.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `customer` (string, nullable)
  ID of the Customer this SetupIntent belongs to, if one exists.

  If present, the SetupIntent’s payment method will be attached to the Customer on successful setup. Payment methods attached to other Customers cannot be used with this SetupIntent.

- `customer_account` (string, nullable)
  ID of the Account this SetupIntent belongs to, if one exists.

  If present, the SetupIntent’s payment method will be attached to the Account on successful setup. Payment methods attached to other Accounts cannot be used with this SetupIntent.

- `description` (string, nullable)
  An arbitrary string attached to the object. Often useful for displaying to users.

- `excluded_payment_method_types` (array of enums, nullable)
  Payment method types that are excluded from this SetupIntent.
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

- `flow_directions` (array of enums, nullable)
  Indicates the directions of money movement for which this payment method is intended to be used.

  Include `inbound` if you intend to use the payment method as the origin to pull funds from. Include `outbound` if you intend to use the payment method as the destination to send funds to. You can include both if you intend to use the payment method for both purposes.
Possible enum values:
  - `inbound`
  - `outbound`

- `last_setup_error` (object, nullable)
  The error encountered in the previous SetupIntent confirmation.

  - `last_setup_error.advice_code` (string, nullable)
    For card errors resulting from a card issuer decline, a short string indicating [how to proceed with an error](https://docs.stripe.com/docs/declines.md#retrying-issuer-declines) if they provide one.

  - `last_setup_error.code` (string, nullable)
    For some errors that could be handled programmatically, a short string indicating the [error code](https://docs.stripe.com/docs/error-codes.md) reported.

  - `last_setup_error.decline_code` (string, nullable)
    For card errors resulting from a card issuer decline, a short string indicating the [card issuer’s reason for the decline](https://docs.stripe.com/docs/declines.md#issuer-declines) if they provide one.

  - `last_setup_error.doc_url` (string, nullable)
    A URL to more information about the [error code](https://docs.stripe.com/docs/error-codes.md) reported.

  - `last_setup_error.message` (string, nullable)
    A human-readable message providing more details about the error. For card errors, these messages can be shown to your users.

  - `last_setup_error.network_advice_code` (string, nullable)
    For card errors resulting from a card issuer decline, a 2 digit code which indicates the advice given to merchant by the card network on how to proceed with an error.

  - `last_setup_error.network_decline_code` (string, nullable)
    For payments declined by the network, an alphanumeric code which indicates the reason the payment failed.

  - `last_setup_error.param` (string, nullable)
    If the error is parameter-specific, the parameter related to the error. For example, you can use this to display a message near the correct form field.

  - `last_setup_error.payment_method` (object, nullable)
    The [PaymentMethod object](https://docs.stripe.com/docs/api/payment_methods/object.md) for errors returned on a request involving a PaymentMethod.

    - `last_setup_error.payment_method.id` (string)
      Unique identifier for the object.

    - `last_setup_error.payment_method.object` (string)
      String representing the object’s type. Objects of the same type share the same value.

    - `last_setup_error.payment_method.acss_debit` (object, nullable)
      If this is an `acss_debit` PaymentMethod, this hash contains details about the ACSS Debit payment method.

      - `last_setup_error.payment_method.acss_debit.bank_name` (string, nullable)
        Name of the bank associated with the bank account.

      - `last_setup_error.payment_method.acss_debit.fingerprint` (string, nullable)
        Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

      - `last_setup_error.payment_method.acss_debit.institution_number` (string, nullable)
        Institution number of the bank account.

      - `last_setup_error.payment_method.acss_debit.last4` (string, nullable)
        Last four digits of the bank account number.

      - `last_setup_error.payment_method.acss_debit.transit_number` (string, nullable)
        Transit number of the bank account.

    - `last_setup_error.payment_method.affirm` (object, nullable)
      If this is an `affirm` PaymentMethod, this hash contains details about the Affirm payment method.

    - `last_setup_error.payment_method.afterpay_clearpay` (object, nullable)
      If this is an `AfterpayClearpay` PaymentMethod, this hash contains details about the AfterpayClearpay payment method.

    - `last_setup_error.payment_method.alipay` (object, nullable)
      If this is an `Alipay` PaymentMethod, this hash contains details about the Alipay payment method.

    - `last_setup_error.payment_method.allow_redisplay` (enum, nullable)
      This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow. The field defaults to “unspecified”.
Possible enum values:
      - `always`
        Use `always` to indicate that this payment method can always be shown to a customer in a checkout flow.

      - `limited`
        Use `limited` to indicate that this payment method can’t always be shown to a customer in a checkout flow. For example, it can only be shown in the context of a specific subscription.

      - `unspecified`
        This is the default value for payment methods where `allow_redisplay` wasn’t set.

    - `last_setup_error.payment_method.alma` (object, nullable)
      If this is a Alma PaymentMethod, this hash contains details about the Alma payment method.

    - `last_setup_error.payment_method.amazon_pay` (object, nullable)
      If this is a AmazonPay PaymentMethod, this hash contains details about the AmazonPay payment method.

    - `last_setup_error.payment_method.au_becs_debit` (object, nullable)
      If this is an `au_becs_debit` PaymentMethod, this hash contains details about the bank account.

      - `last_setup_error.payment_method.au_becs_debit.bsb_number` (string, nullable)
        Six-digit number identifying bank and branch associated with this bank account.

      - `last_setup_error.payment_method.au_becs_debit.fingerprint` (string, nullable)
        Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

      - `last_setup_error.payment_method.au_becs_debit.last4` (string, nullable)
        Last four digits of the bank account number.

    - `last_setup_error.payment_method.bacs_debit` (object, nullable)
      If this is a `bacs_debit` PaymentMethod, this hash contains details about the Bacs Direct Debit bank account.

      - `last_setup_error.payment_method.bacs_debit.fingerprint` (string, nullable)
        Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

      - `last_setup_error.payment_method.bacs_debit.last4` (string, nullable)
        Last four digits of the bank account number.

      - `last_setup_error.payment_method.bacs_debit.sort_code` (string, nullable)
        Sort code of the bank account. (e.g., `10-20-30`)

    - `last_setup_error.payment_method.bancontact` (object, nullable)
      If this is a `bancontact` PaymentMethod, this hash contains details about the Bancontact payment method.

    - `last_setup_error.payment_method.billie` (object, nullable)
      If this is a `billie` PaymentMethod, this hash contains details about the Billie payment method.

    - `last_setup_error.payment_method.billing_details` (object)
      Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.

      - `last_setup_error.payment_method.billing_details.address` (object, nullable)
        Billing address.

        - `last_setup_error.payment_method.billing_details.address.city` (string, nullable)
          City, district, suburb, town, or village.

        - `last_setup_error.payment_method.billing_details.address.country` (string, nullable)
          Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

        - `last_setup_error.payment_method.billing_details.address.line1` (string, nullable)
          Address line 1, such as the street, PO Box, or company name.

        - `last_setup_error.payment_method.billing_details.address.line2` (string, nullable)
          Address line 2, such as the apartment, suite, unit, or building.

        - `last_setup_error.payment_method.billing_details.address.postal_code` (string, nullable)
          ZIP or postal code.

        - `last_setup_error.payment_method.billing_details.address.state` (string, nullable)
          State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

      - `last_setup_error.payment_method.billing_details.email` (string, nullable)
        Email address.

      - `last_setup_error.payment_method.billing_details.name` (string, nullable)
        Full name.

      - `last_setup_error.payment_method.billing_details.phone` (string, nullable)
        Billing phone number (including extension).

      - `last_setup_error.payment_method.billing_details.tax_id` (string, nullable)
        Taxpayer identification number. Used only for transactions between LATAM buyers and non-LATAM sellers.

    - `last_setup_error.payment_method.blik` (object, nullable)
      If this is a `blik` PaymentMethod, this hash contains details about the BLIK payment method.

    - `last_setup_error.payment_method.boleto` (object, nullable)
      If this is a `boleto` PaymentMethod, this hash contains details about the Boleto payment method.

      - `last_setup_error.payment_method.boleto.tax_id` (string)
        Uniquely identifies the customer tax id (CNPJ or CPF)

    - `last_setup_error.payment_method.card` (object, nullable)
      If this is a `card` PaymentMethod, this hash contains the user’s card details.

      - `last_setup_error.payment_method.card.brand` (string)
        Card brand. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `jcb`, `link`, `mastercard`, `unionpay`, `visa` or `unknown`.

      - `last_setup_error.payment_method.card.checks` (object, nullable)
        Checks on Card address and CVC if provided.

        - `last_setup_error.payment_method.card.checks.address_line1_check` (string, nullable)
          If a address line1 was provided, results of the check, one of `pass`, `fail`, `unavailable`, or `unchecked`.

        - `last_setup_error.payment_method.card.checks.address_postal_code_check` (string, nullable)
          If a address postal code was provided, results of the check, one of `pass`, `fail`, `unavailable`, or `unchecked`.

        - `last_setup_error.payment_method.card.checks.cvc_check` (string, nullable)
          If a CVC was provided, results of the check, one of `pass`, `fail`, `unavailable`, or `unchecked`.

      - `last_setup_error.payment_method.card.country` (string, nullable)
        Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you’ve collected.

      - `last_setup_error.payment_method.card.display_brand` (string, nullable)
        The brand to use when displaying the card, this accounts for customer’s brand choice on dual-branded cards. Can be `american_express`, `cartes_bancaires`, `diners_club`, `discover`, `eftpos_australia`, `interac`, `jcb`, `mastercard`, `union_pay`, `visa`, or `other` and may contain more values in the future.

      - `last_setup_error.payment_method.card.exp_month` (integer)
        Two-digit number representing the card’s expiration month.

      - `last_setup_error.payment_method.card.exp_year` (integer)
        Four-digit number representing the card’s expiration year.

      - `last_setup_error.payment_method.card.fingerprint` (string, nullable)
        Uniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.

        *As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card—one for India and one for the rest of the world.*

      - `last_setup_error.payment_method.card.funding` (string)
        Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.

      - `last_setup_error.payment_method.card.generated_from` (object, nullable)
        Details of the original PaymentMethod that created this object.

        - `last_setup_error.payment_method.card.generated_from.charge` (string, nullable)
          The charge that created this object.

        - `last_setup_error.payment_method.card.generated_from.payment_method_details` (object, nullable)
          Transaction-specific details of the payment method used in the payment.

          - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present` (object, nullable)
            This hash contains the snapshot of the `card_present` transaction-specific details which generated this `card` payment method.

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.amount_authorized` (integer, nullable)
              The authorized amount

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.brand` (string, nullable)
              Card brand. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `jcb`, `link`, `mastercard`, `unionpay`, `visa` or `unknown`.

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.brand_product` (string, nullable)
              The [product code](https://stripe.com/docs/card-product-codes) that identifies the specific program or product associated with a card.

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.capture_before` (timestamp, nullable)
              When using manual capture, a future timestamp after which the charge will be automatically refunded if uncaptured.

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.cardholder_name` (string, nullable)
              The cardholder name as read from the card, in [ISO 7813](https://en.wikipedia.org/wiki/ISO/IEC_7813) format. May include alphanumeric characters, special characters and first/last name separator (`/`). In some cases, the cardholder name may not be available depending on how the issuer has configured the card. Cardholder name is typically not available on swipe or contactless payments, such as those made with Apple Pay and Google Pay.

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.country` (string, nullable)
              Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you’ve collected.

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.description` (string, nullable)
              A high-level description of the type of cards issued in this range.

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.emv_auth_data` (string, nullable)
              Authorization response cryptogram.

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.exp_month` (integer)
              Two-digit number representing the card’s expiration month.

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.exp_year` (integer)
              Four-digit number representing the card’s expiration year.

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.fingerprint` (string, nullable)
              Uniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.

              *As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card—one for India and one for the rest of the world.*

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.funding` (string, nullable)
              Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.generated_card` (string, nullable)
              ID of a card PaymentMethod generated from the card_present PaymentMethod that may be attached to a Customer for future transactions. Only present if it was possible to generate a card PaymentMethod.

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.incremental_authorization_supported` (boolean)
              Whether this [PaymentIntent](https://docs.stripe.com/docs/api/payment_intents.md) is eligible for incremental authorizations. Request support using [request_incremental_authorization_support](https://docs.stripe.com/docs/api/payment_intents/create.md#create_payment_intent-payment_method_options-card_present-request_incremental_authorization_support).

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.issuer` (string, nullable)
              The name of the card’s issuing bank.

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.last4` (string, nullable)
              The last four digits of the card.

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.network` (string, nullable)
              Identifies which network this charge was processed on. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `interac`, `jcb`, `link`, `mastercard`, `unionpay`, `visa`, or `unknown`.

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.network_transaction_id` (string, nullable)
              This is used by the financial networks to identify a transaction. Visa calls this the Transaction ID, Mastercard calls this the Trace ID, and American Express calls this the Acquirer Reference Data. This value will be present if it is returned by the financial network in the authorization response, and null otherwise.

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.offline` (object, nullable)
              Details about payments collected offline.

              - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.offline.stored_at` (timestamp, nullable)
                Time at which the payment was collected while offline

              - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.offline.type` (enum, nullable)
                The method used to process this payment method offline. Only deferred is allowed.
Possible enum values:
                - `deferred`

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.overcapture_supported` (boolean)
              Defines whether the authorized amount can be over-captured or not

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.preferred_locales` (array of strings, nullable)
              The languages that the issuing bank recommends using for localizing any customer-facing text, as read from the card. Referenced from EMV tag 5F2D, data encoded on the card’s chip.

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.read_method` (enum, nullable)
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

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.receipt` (object, nullable)
              A collection of fields required to be displayed on receipts. Only required for EMV transactions.

              - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.receipt.account_type` (enum, nullable)
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

              - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.receipt.application_cryptogram` (string, nullable)
                The Application Cryptogram, a unique value generated by the card to authenticate the transaction with issuers.

              - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.receipt.application_preferred_name` (string, nullable)
                The Application Identifier (AID) on the card used to determine which networks are eligible to process the transaction. Referenced from EMV tag 9F12, data encoded on the card’s chip.

              - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.receipt.authorization_code` (string, nullable)
                Identifier for this transaction.

              - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.receipt.authorization_response_code` (string, nullable)
                EMV tag 8A. A code returned by the card issuer.

              - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.receipt.cardholder_verification_method` (string, nullable)
                Describes the method used by the cardholder to verify ownership of the card. One of the following: `approval`, `failure`, `none`, `offline_pin`, `offline_pin_and_signature`, `online_pin`, or `signature`.

              - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.receipt.dedicated_file_name` (string, nullable)
                Similar to the application_preferred_name, identifying the applications (AIDs) available on the card. Referenced from EMV tag 84.

              - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.receipt.terminal_verification_results` (string, nullable)
                A 5-byte string that records the checks and validations that occur between the card and the terminal. These checks determine how the terminal processes the transaction and what risk tolerance is acceptable. Referenced from EMV Tag 95.

              - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.receipt.transaction_status_information` (string, nullable)
                An indication of which steps were completed during the card read process. Referenced from EMV Tag 9B.

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.wallet` (object, nullable)
              If a mobile wallet was presented in the transaction, this contains the details of the mobile wallet.

              - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.wallet.type` (enum)
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

          - `last_setup_error.payment_method.card.generated_from.payment_method_details.type` (string)
            The type of payment method transaction-specific details from the transaction that generated this `card` payment method. Always `card_present`.

        - `last_setup_error.payment_method.card.generated_from.setup_attempt` (string, nullable)
          The ID of the SetupAttempt that generated this PaymentMethod, if any.

      - `last_setup_error.payment_method.card.last4` (string)
        The last four digits of the card.

      - `last_setup_error.payment_method.card.networks` (object, nullable)
        Contains information about card networks that can be used to process the payment.

        - `last_setup_error.payment_method.card.networks.available` (array of strings)
          All networks available for selection via [payment_method_options.card.network](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-payment_method_options-card-network).

        - `last_setup_error.payment_method.card.networks.preferred` (string, nullable)
          The preferred network for co-branded cards. Can be `cartes_bancaires`, `mastercard`, `visa` or `invalid_preference` if requested network is not valid for the card.

      - `last_setup_error.payment_method.card.regulated_status` (enum, nullable)
        Status of a card based on the card issuer.
Possible enum values:
        - `regulated`
          The card falls under a regulated account range.

        - `unregulated`
          The card does not fall under a regulated account range.

      - `last_setup_error.payment_method.card.three_d_secure_usage` (object, nullable)
        Contains details on how this Card may be used for 3D Secure authentication.

        - `last_setup_error.payment_method.card.three_d_secure_usage.supported` (boolean)
          Whether 3D Secure is supported on this card.

      - `last_setup_error.payment_method.card.wallet` (object, nullable)
        If this Card is part of a card wallet, this contains the details of the card wallet.

        - `last_setup_error.payment_method.card.wallet.amex_express_checkout` (object, nullable)
          If this is a `amex_express_checkout` card wallet, this hash contains details about the wallet.

        - `last_setup_error.payment_method.card.wallet.apple_pay` (object, nullable)
          If this is a `apple_pay` card wallet, this hash contains details about the wallet.

        - `last_setup_error.payment_method.card.wallet.dynamic_last4` (string, nullable)
          (For tokenized numbers only.) The last four digits of the device account number.

        - `last_setup_error.payment_method.card.wallet.google_pay` (object, nullable)
          If this is a `google_pay` card wallet, this hash contains details about the wallet.

        - `last_setup_error.payment_method.card.wallet.link` (object, nullable)
          If this is a `link` card wallet, this hash contains details about the wallet.

        - `last_setup_error.payment_method.card.wallet.masterpass` (object, nullable)
          If this is a `masterpass` card wallet, this hash contains details about the wallet.

          - `last_setup_error.payment_method.card.wallet.masterpass.billing_address` (object, nullable)
            Owner’s verified billing address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

            - `last_setup_error.payment_method.card.wallet.masterpass.billing_address.city` (string, nullable)
              City, district, suburb, town, or village.

            - `last_setup_error.payment_method.card.wallet.masterpass.billing_address.country` (string, nullable)
              Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

            - `last_setup_error.payment_method.card.wallet.masterpass.billing_address.line1` (string, nullable)
              Address line 1, such as the street, PO Box, or company name.

            - `last_setup_error.payment_method.card.wallet.masterpass.billing_address.line2` (string, nullable)
              Address line 2, such as the apartment, suite, unit, or building.

            - `last_setup_error.payment_method.card.wallet.masterpass.billing_address.postal_code` (string, nullable)
              ZIP or postal code.

            - `last_setup_error.payment_method.card.wallet.masterpass.billing_address.state` (string, nullable)
              State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

          - `last_setup_error.payment_method.card.wallet.masterpass.email` (string, nullable)
            Owner’s verified email. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

          - `last_setup_error.payment_method.card.wallet.masterpass.name` (string, nullable)
            Owner’s verified full name. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

          - `last_setup_error.payment_method.card.wallet.masterpass.shipping_address` (object, nullable)
            Owner’s verified shipping address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

            - `last_setup_error.payment_method.card.wallet.masterpass.shipping_address.city` (string, nullable)
              City, district, suburb, town, or village.

            - `last_setup_error.payment_method.card.wallet.masterpass.shipping_address.country` (string, nullable)
              Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

            - `last_setup_error.payment_method.card.wallet.masterpass.shipping_address.line1` (string, nullable)
              Address line 1, such as the street, PO Box, or company name.

            - `last_setup_error.payment_method.card.wallet.masterpass.shipping_address.line2` (string, nullable)
              Address line 2, such as the apartment, suite, unit, or building.

            - `last_setup_error.payment_method.card.wallet.masterpass.shipping_address.postal_code` (string, nullable)
              ZIP or postal code.

            - `last_setup_error.payment_method.card.wallet.masterpass.shipping_address.state` (string, nullable)
              State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

        - `last_setup_error.payment_method.card.wallet.samsung_pay` (object, nullable)
          If this is a `samsung_pay` card wallet, this hash contains details about the wallet.

        - `last_setup_error.payment_method.card.wallet.type` (enum)
          The type of the card wallet, one of `amex_express_checkout`, `apple_pay`, `google_pay`, `masterpass`, `samsung_pay`, `visa_checkout`, or `link`. An additional hash is included on the Wallet subhash with a name matching this value. It contains additional information specific to the card wallet type.
Possible enum values:
          - `amex_express_checkout`
          - `apple_pay`
          - `google_pay`
          - `link`
          - `masterpass`
          - `samsung_pay`
          - `visa_checkout`

        - `last_setup_error.payment_method.card.wallet.visa_checkout` (object, nullable)
          If this is a `visa_checkout` card wallet, this hash contains details about the wallet.

          - `last_setup_error.payment_method.card.wallet.visa_checkout.billing_address` (object, nullable)
            Owner’s verified billing address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

            - `last_setup_error.payment_method.card.wallet.visa_checkout.billing_address.city` (string, nullable)
              City, district, suburb, town, or village.

            - `last_setup_error.payment_method.card.wallet.visa_checkout.billing_address.country` (string, nullable)
              Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

            - `last_setup_error.payment_method.card.wallet.visa_checkout.billing_address.line1` (string, nullable)
              Address line 1, such as the street, PO Box, or company name.

            - `last_setup_error.payment_method.card.wallet.visa_checkout.billing_address.line2` (string, nullable)
              Address line 2, such as the apartment, suite, unit, or building.

            - `last_setup_error.payment_method.card.wallet.visa_checkout.billing_address.postal_code` (string, nullable)
              ZIP or postal code.

            - `last_setup_error.payment_method.card.wallet.visa_checkout.billing_address.state` (string, nullable)
              State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

          - `last_setup_error.payment_method.card.wallet.visa_checkout.email` (string, nullable)
            Owner’s verified email. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

          - `last_setup_error.payment_method.card.wallet.visa_checkout.name` (string, nullable)
            Owner’s verified full name. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

          - `last_setup_error.payment_method.card.wallet.visa_checkout.shipping_address` (object, nullable)
            Owner’s verified shipping address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

            - `last_setup_error.payment_method.card.wallet.visa_checkout.shipping_address.city` (string, nullable)
              City, district, suburb, town, or village.

            - `last_setup_error.payment_method.card.wallet.visa_checkout.shipping_address.country` (string, nullable)
              Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

            - `last_setup_error.payment_method.card.wallet.visa_checkout.shipping_address.line1` (string, nullable)
              Address line 1, such as the street, PO Box, or company name.

            - `last_setup_error.payment_method.card.wallet.visa_checkout.shipping_address.line2` (string, nullable)
              Address line 2, such as the apartment, suite, unit, or building.

            - `last_setup_error.payment_method.card.wallet.visa_checkout.shipping_address.postal_code` (string, nullable)
              ZIP or postal code.

            - `last_setup_error.payment_method.card.wallet.visa_checkout.shipping_address.state` (string, nullable)
              State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

    - `last_setup_error.payment_method.card_present` (object, nullable)
      If this is a `card_present` PaymentMethod, this hash contains details about the Card Present payment method.

      - `last_setup_error.payment_method.card_present.brand` (string, nullable)
        Card brand. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `jcb`, `link`, `mastercard`, `unionpay`, `visa` or `unknown`.

      - `last_setup_error.payment_method.card_present.brand_product` (string, nullable)
        The [product code](https://stripe.com/docs/card-product-codes) that identifies the specific program or product associated with a card.

      - `last_setup_error.payment_method.card_present.cardholder_name` (string, nullable)
        The cardholder name as read from the card, in [ISO 7813](https://en.wikipedia.org/wiki/ISO/IEC_7813) format. May include alphanumeric characters, special characters and first/last name separator (`/`). In some cases, the cardholder name may not be available depending on how the issuer has configured the card. Cardholder name is typically not available on swipe or contactless payments, such as those made with Apple Pay and Google Pay.

      - `last_setup_error.payment_method.card_present.country` (string, nullable)
        Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you’ve collected.

      - `last_setup_error.payment_method.card_present.description` (string, nullable)
        A high-level description of the type of cards issued in this range.

      - `last_setup_error.payment_method.card_present.exp_month` (integer)
        Two-digit number representing the card’s expiration month.

      - `last_setup_error.payment_method.card_present.exp_year` (integer)
        Four-digit number representing the card’s expiration year.

      - `last_setup_error.payment_method.card_present.fingerprint` (string, nullable)
        Uniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.

        *As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card—one for India and one for the rest of the world.*

      - `last_setup_error.payment_method.card_present.funding` (string, nullable)
        Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.

      - `last_setup_error.payment_method.card_present.issuer` (string, nullable)
        The name of the card’s issuing bank.

      - `last_setup_error.payment_method.card_present.last4` (string, nullable)
        The last four digits of the card.

      - `last_setup_error.payment_method.card_present.networks` (object, nullable)
        Contains information about card networks that can be used to process the payment.

        - `last_setup_error.payment_method.card_present.networks.available` (array of strings)
          All networks available for selection via [payment_method_options.card.network](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-payment_method_options-card-network).

        - `last_setup_error.payment_method.card_present.networks.preferred` (string, nullable)
          The preferred network for the card.

      - `last_setup_error.payment_method.card_present.offline` (object, nullable)
        Details about payment methods collected offline.

        - `last_setup_error.payment_method.card_present.offline.stored_at` (timestamp, nullable)
          Time at which the payment was collected while offline

        - `last_setup_error.payment_method.card_present.offline.type` (enum, nullable)
          The method used to process this payment method offline. Only deferred is allowed.
Possible enum values:
          - `deferred`

      - `last_setup_error.payment_method.card_present.preferred_locales` (array of strings, nullable)
        The languages that the issuing bank recommends using for localizing any customer-facing text, as read from the card. Referenced from EMV tag 5F2D, data encoded on the card’s chip.

      - `last_setup_error.payment_method.card_present.read_method` (enum, nullable)
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

      - `last_setup_error.payment_method.card_present.wallet` (object, nullable)
        If a mobile wallet was presented in the transaction, this contains the details of the mobile wallet.

        - `last_setup_error.payment_method.card_present.wallet.type` (enum)
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

    - `last_setup_error.payment_method.cashapp` (object, nullable)
      If this is a `cashapp` PaymentMethod, this hash contains details about the Cash App Pay payment method.

      - `last_setup_error.payment_method.cashapp.buyer_id` (string, nullable)
        A unique and immutable identifier assigned by Cash App to every buyer.

      - `last_setup_error.payment_method.cashapp.cashtag` (string, nullable)
        A public identifier for buyers using Cash App.

    - `last_setup_error.payment_method.created` (timestamp)
      Time at which the object was created. Measured in seconds since the Unix epoch.

    - `last_setup_error.payment_method.crypto` (object, nullable)
      If this is a Crypto PaymentMethod, this hash contains details about the Crypto payment method.

    - `last_setup_error.payment_method.custom` (object, nullable)
      If this is a `custom` PaymentMethod, this hash contains details about the Custom payment method.

      - `last_setup_error.payment_method.custom.display_name` (string, nullable)
        Display name of the Dashboard-only CustomPaymentMethodType.

      - `last_setup_error.payment_method.custom.logo` (object, nullable)
        Contains information about the Dashboard-only CustomPaymentMethodType logo.

        - `last_setup_error.payment_method.custom.logo.content_type` (string, nullable)
          Content type of the Dashboard-only CustomPaymentMethodType logo.

        - `last_setup_error.payment_method.custom.logo.url` (string)
          URL of the Dashboard-only CustomPaymentMethodType logo.

      - `last_setup_error.payment_method.custom.type` (string)
        ID of the Dashboard-only CustomPaymentMethodType. Not expandable.

    - `last_setup_error.payment_method.customer` (string, nullable)
      The ID of the Customer to which this PaymentMethod is saved. This will not be set when the PaymentMethod has not been saved to a Customer.

    - `last_setup_error.payment_method.customer_balance` (object, nullable)
      If this is a `customer_balance` PaymentMethod, this hash contains details about the CustomerBalance payment method.

    - `last_setup_error.payment_method.eps` (object, nullable)
      If this is an `eps` PaymentMethod, this hash contains details about the EPS payment method.

      - `last_setup_error.payment_method.eps.bank` (enum, nullable)
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

    - `last_setup_error.payment_method.fpx` (object, nullable)
      If this is an `fpx` PaymentMethod, this hash contains details about the FPX payment method.

      - `last_setup_error.payment_method.fpx.bank` (enum)
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

    - `last_setup_error.payment_method.giropay` (object, nullable)
      If this is a `giropay` PaymentMethod, this hash contains details about the Giropay payment method.

    - `last_setup_error.payment_method.grabpay` (object, nullable)
      If this is a `grabpay` PaymentMethod, this hash contains details about the GrabPay payment method.

    - `last_setup_error.payment_method.ideal` (object, nullable)
      If this is an `ideal` PaymentMethod, this hash contains details about the iDEAL payment method.

      - `last_setup_error.payment_method.ideal.bank` (enum, nullable)
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

      - `last_setup_error.payment_method.ideal.bic` (enum, nullable)
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

    - `last_setup_error.payment_method.interac_present` (object, nullable)
      If this is an `interac_present` PaymentMethod, this hash contains details about the Interac Present payment method.

      - `last_setup_error.payment_method.interac_present.brand` (string, nullable)
        Card brand. Can be `interac`, `mastercard` or `visa`.

      - `last_setup_error.payment_method.interac_present.cardholder_name` (string, nullable)
        The cardholder name as read from the card, in [ISO 7813](https://en.wikipedia.org/wiki/ISO/IEC_7813) format. May include alphanumeric characters, special characters and first/last name separator (`/`). In some cases, the cardholder name may not be available depending on how the issuer has configured the card. Cardholder name is typically not available on swipe or contactless payments, such as those made with Apple Pay and Google Pay.

      - `last_setup_error.payment_method.interac_present.country` (string, nullable)
        Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you’ve collected.

      - `last_setup_error.payment_method.interac_present.description` (string, nullable)
        A high-level description of the type of cards issued in this range.

      - `last_setup_error.payment_method.interac_present.exp_month` (integer)
        Two-digit number representing the card’s expiration month.

      - `last_setup_error.payment_method.interac_present.exp_year` (integer)
        Four-digit number representing the card’s expiration year.

      - `last_setup_error.payment_method.interac_present.fingerprint` (string, nullable)
        Uniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.

        *As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card—one for India and one for the rest of the world.*

      - `last_setup_error.payment_method.interac_present.funding` (string, nullable)
        Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.

      - `last_setup_error.payment_method.interac_present.issuer` (string, nullable)
        The name of the card’s issuing bank.

      - `last_setup_error.payment_method.interac_present.last4` (string, nullable)
        The last four digits of the card.

      - `last_setup_error.payment_method.interac_present.networks` (object, nullable)
        Contains information about card networks that can be used to process the payment.

        - `last_setup_error.payment_method.interac_present.networks.available` (array of strings)
          All networks available for selection via [payment_method_options.card.network](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-payment_method_options-card-network).

        - `last_setup_error.payment_method.interac_present.networks.preferred` (string, nullable)
          The preferred network for the card.

      - `last_setup_error.payment_method.interac_present.preferred_locales` (array of strings, nullable)
        The languages that the issuing bank recommends using for localizing any customer-facing text, as read from the card. Referenced from EMV tag 5F2D, data encoded on the card’s chip.

      - `last_setup_error.payment_method.interac_present.read_method` (enum, nullable)
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

    - `last_setup_error.payment_method.kakao_pay` (object, nullable)
      If this is a `kakao_pay` PaymentMethod, this hash contains details about the Kakao Pay payment method.

    - `last_setup_error.payment_method.klarna` (object, nullable)
      If this is a `klarna` PaymentMethod, this hash contains details about the Klarna payment method.

      - `last_setup_error.payment_method.klarna.dob` (object, nullable)
        The customer’s date of birth, if provided.

        - `last_setup_error.payment_method.klarna.dob.day` (integer, nullable)
          The day of birth, between 1 and 31.

        - `last_setup_error.payment_method.klarna.dob.month` (integer, nullable)
          The month of birth, between 1 and 12.

        - `last_setup_error.payment_method.klarna.dob.year` (integer, nullable)
          The four-digit year of birth.

    - `last_setup_error.payment_method.konbini` (object, nullable)
      If this is a `konbini` PaymentMethod, this hash contains details about the Konbini payment method.

    - `last_setup_error.payment_method.kr_card` (object, nullable)
      If this is a `kr_card` PaymentMethod, this hash contains details about the Korean Card payment method.

      - `last_setup_error.payment_method.kr_card.brand` (enum, nullable)
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

      - `last_setup_error.payment_method.kr_card.last4` (string, nullable)
        The last four digits of the card. This may not be present for American Express cards.

        The maximum length is 4 characters.

    - `last_setup_error.payment_method.link` (object, nullable)
      If this is an `Link` PaymentMethod, this hash contains details about the Link payment method.

      - `last_setup_error.payment_method.link.email` (string, nullable)
        Account owner’s email address.

    - `last_setup_error.payment_method.livemode` (boolean)
      Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

    - `last_setup_error.payment_method.mb_way` (object, nullable)
      If this is a MB WAY PaymentMethod, this hash contains details about the MB WAY payment method.

    - `last_setup_error.payment_method.metadata` (object, nullable)
      Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

    - `last_setup_error.payment_method.mobilepay` (object, nullable)
      If this is a `mobilepay` PaymentMethod, this hash contains details about the MobilePay payment method.

    - `last_setup_error.payment_method.multibanco` (object, nullable)
      If this is a `multibanco` PaymentMethod, this hash contains details about the Multibanco payment method.

    - `last_setup_error.payment_method.naver_pay` (object, nullable)
      If this is a `naver_pay` PaymentMethod, this hash contains details about the Naver Pay payment method.

      - `last_setup_error.payment_method.naver_pay.buyer_id` (string, nullable)
        Uniquely identifies this particular Naver Pay account. You can use this attribute to check whether two Naver Pay accounts are the same.

      - `last_setup_error.payment_method.naver_pay.funding` (enum)
        Whether to fund this transaction with Naver Pay points or a card.
Possible enum values:
        - `card`
          Use a card to fund this transaction.

        - `points`
          Use Naver Pay points to fund this transaction.

    - `last_setup_error.payment_method.nz_bank_account` (object, nullable)
      If this is an nz_bank_account PaymentMethod, this hash contains details about the nz_bank_account payment method.

      - `last_setup_error.payment_method.nz_bank_account.account_holder_name` (string, nullable)
        The name on the bank account. Only present if the account holder name is different from the name of the authorized signatory collected in the PaymentMethod’s billing details.

      - `last_setup_error.payment_method.nz_bank_account.bank_code` (string)
        The numeric code for the bank account’s bank.

      - `last_setup_error.payment_method.nz_bank_account.bank_name` (string)
        The name of the bank.

      - `last_setup_error.payment_method.nz_bank_account.branch_code` (string)
        The numeric code for the bank account’s bank branch.

      - `last_setup_error.payment_method.nz_bank_account.last4` (string)
        Last four digits of the bank account number.

      - `last_setup_error.payment_method.nz_bank_account.suffix` (string, nullable)
        The suffix of the bank account number.

    - `last_setup_error.payment_method.oxxo` (object, nullable)
      If this is an `oxxo` PaymentMethod, this hash contains details about the OXXO payment method.

    - `last_setup_error.payment_method.p24` (object, nullable)
      If this is a `p24` PaymentMethod, this hash contains details about the P24 payment method.

      - `last_setup_error.payment_method.p24.bank` (enum, nullable)
        The customer’s bank, if provided.

    - `last_setup_error.payment_method.pay_by_bank` (object, nullable)
      If this is a `pay_by_bank` PaymentMethod, this hash contains details about the PayByBank payment method.

    - `last_setup_error.payment_method.payco` (object, nullable)
      If this is a `payco` PaymentMethod, this hash contains details about the PAYCO payment method.

    - `last_setup_error.payment_method.paynow` (object, nullable)
      If this is a `paynow` PaymentMethod, this hash contains details about the PayNow payment method.

    - `last_setup_error.payment_method.paypal` (object, nullable)
      If this is a `paypal` PaymentMethod, this hash contains details about the PayPal payment method.

      - `last_setup_error.payment_method.paypal.country` (string, nullable)
        Two-letter ISO code representing the buyer’s country. Values are provided by PayPal directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

      - `last_setup_error.payment_method.paypal.payer_email` (string, nullable)
        Owner’s email. Values are provided by PayPal directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

      - `last_setup_error.payment_method.paypal.payer_id` (string, nullable)
        PayPal account PayerID. This identifier uniquely identifies the PayPal customer.

    - `last_setup_error.payment_method.paypay` (object, nullable)
      If this is a `paypay` PaymentMethod, this hash contains details about the PayPay payment method.

    - `last_setup_error.payment_method.payto` (object, nullable)
      If this is a `payto` PaymentMethod, this hash contains details about the PayTo payment method.

      - `last_setup_error.payment_method.payto.bsb_number` (string, nullable)
        Bank-State-Branch number of the bank account.

      - `last_setup_error.payment_method.payto.last4` (string, nullable)
        Last four digits of the bank account number.

      - `last_setup_error.payment_method.payto.pay_id` (string, nullable)
        The PayID alias for the bank account.

    - `last_setup_error.payment_method.pix` (object, nullable)
      If this is a `pix` PaymentMethod, this hash contains details about the Pix payment method.

    - `last_setup_error.payment_method.promptpay` (object, nullable)
      If this is a `promptpay` PaymentMethod, this hash contains details about the PromptPay payment method.

    - `last_setup_error.payment_method.radar_options` (object, nullable)
      Options to configure Radar. See [Radar Session](https://docs.stripe.com/docs/radar/radar-session.md) for more information.

      - `last_setup_error.payment_method.radar_options.session` (string, nullable)
        A [Radar Session](https://docs.stripe.com/docs/radar/radar-session.md) is a snapshot of the browser metadata and device details that help Radar make more accurate predictions on your payments.

    - `last_setup_error.payment_method.revolut_pay` (object, nullable)
      If this is a `revolut_pay` PaymentMethod, this hash contains details about the Revolut Pay payment method.

    - `last_setup_error.payment_method.samsung_pay` (object, nullable)
      If this is a `samsung_pay` PaymentMethod, this hash contains details about the SamsungPay payment method.

    - `last_setup_error.payment_method.satispay` (object, nullable)
      If this is a `satispay` PaymentMethod, this hash contains details about the Satispay payment method.

    - `last_setup_error.payment_method.sepa_debit` (object, nullable)
      If this is a `sepa_debit` PaymentMethod, this hash contains details about the SEPA debit bank account.

      - `last_setup_error.payment_method.sepa_debit.bank_code` (string, nullable)
        Bank code of bank associated with the bank account.

      - `last_setup_error.payment_method.sepa_debit.branch_code` (string, nullable)
        Branch code of bank associated with the bank account.

      - `last_setup_error.payment_method.sepa_debit.country` (string, nullable)
        Two-letter ISO code representing the country the bank account is located in.

      - `last_setup_error.payment_method.sepa_debit.fingerprint` (string, nullable)
        Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

      - `last_setup_error.payment_method.sepa_debit.generated_from` (object, nullable)
        Information about the object that generated this PaymentMethod.

        - `last_setup_error.payment_method.sepa_debit.generated_from.charge` (string, nullable)
          The ID of the Charge that generated this PaymentMethod, if any.

        - `last_setup_error.payment_method.sepa_debit.generated_from.setup_attempt` (string, nullable)
          The ID of the SetupAttempt that generated this PaymentMethod, if any.

      - `last_setup_error.payment_method.sepa_debit.last4` (string, nullable)
        Last four characters of the IBAN.

    - `last_setup_error.payment_method.sofort` (object, nullable)
      If this is a `sofort` PaymentMethod, this hash contains details about the SOFORT payment method.

      - `last_setup_error.payment_method.sofort.country` (string, nullable)
        Two-letter ISO code representing the country the bank account is located in.

    - `last_setup_error.payment_method.swish` (object, nullable)
      If this is a `swish` PaymentMethod, this hash contains details about the Swish payment method.

    - `last_setup_error.payment_method.twint` (object, nullable)
      If this is a TWINT PaymentMethod, this hash contains details about the TWINT payment method.

    - `last_setup_error.payment_method.type` (enum)
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

    - `last_setup_error.payment_method.us_bank_account` (object, nullable)
      If this is an `us_bank_account` PaymentMethod, this hash contains details about the US bank account payment method.

      - `last_setup_error.payment_method.us_bank_account.account_holder_type` (enum, nullable)
        Account holder type: individual or company.
Possible enum values:
        - `company`
          Account belongs to a company

        - `individual`
          Account belongs to an individual

      - `last_setup_error.payment_method.us_bank_account.account_type` (enum, nullable)
        Account type: checkings or savings. Defaults to checking if omitted.
Possible enum values:
        - `checking`
          Bank account type is checking

        - `savings`
          Bank account type is savings

      - `last_setup_error.payment_method.us_bank_account.bank_name` (string, nullable)
        The name of the bank.

      - `last_setup_error.payment_method.us_bank_account.financial_connections_account` (string, nullable)
        The ID of the Financial Connections Account used to create the payment method.

      - `last_setup_error.payment_method.us_bank_account.fingerprint` (string, nullable)
        Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

      - `last_setup_error.payment_method.us_bank_account.last4` (string, nullable)
        Last four digits of the bank account number.

      - `last_setup_error.payment_method.us_bank_account.networks` (object, nullable)
        Contains information about US bank account networks that can be used.

        - `last_setup_error.payment_method.us_bank_account.networks.preferred` (string, nullable)
          The preferred network.

        - `last_setup_error.payment_method.us_bank_account.networks.supported` (array of enums)
          All supported networks.
Possible enum values:
          - `ach`
          - `us_domestic_wire`

      - `last_setup_error.payment_method.us_bank_account.routing_number` (string, nullable)
        Routing number of the bank account.

      - `last_setup_error.payment_method.us_bank_account.status_details` (object, nullable)
        Contains information about the future reusability of this PaymentMethod.

        - `last_setup_error.payment_method.us_bank_account.status_details.blocked` (object, nullable)
          Contains more information about the underlying block. This field will only be rendered if the PaymentMethod is blocked.

          - `last_setup_error.payment_method.us_bank_account.status_details.blocked.network_code` (enum, nullable)
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

          - `last_setup_error.payment_method.us_bank_account.status_details.blocked.reason` (enum, nullable)
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

    - `last_setup_error.payment_method.wechat_pay` (object, nullable)
      If this is an `wechat_pay` PaymentMethod, this hash contains details about the wechat_pay payment method.

    - `last_setup_error.payment_method.zip` (object, nullable)
      If this is a `zip` PaymentMethod, this hash contains details about the Zip payment method.

  - `last_setup_error.payment_method_type` (string, nullable)
    If the error is specific to the type of payment method, the payment method type that had a problem. This field is only populated for invoice-related errors.

  - `last_setup_error.type` (enum)
    The type of error returned. One of `api_error`, `card_error`, `idempotency_error`, or `invalid_request_error`
Possible enum values:
    - `api_error`
    - `card_error`
    - `idempotency_error`
    - `invalid_request_error`

- `latest_attempt` (string, nullable)
  The most recent SetupAttempt for this SetupIntent.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `mandate` (string, nullable)
  ID of the multi use Mandate generated by the SetupIntent.

- `metadata` (object, nullable)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `next_action` (object, nullable)
  If present, this property tells you what actions you need to take in order for your customer to continue payment setup.

  - `next_action.cashapp_handle_redirect_or_display_qr_code` (object, nullable)
    The field that contains Cash App Pay QR code info

    - `next_action.cashapp_handle_redirect_or_display_qr_code.hosted_instructions_url` (string)
      The URL to the hosted Cash App Pay instructions page, which allows customers to view the QR code, and supports QR code refreshing on expiration.

    - `next_action.cashapp_handle_redirect_or_display_qr_code.mobile_auth_url` (string)
      The url for mobile redirect based auth

    - `next_action.cashapp_handle_redirect_or_display_qr_code.qr_code` (object)
      The field that contains CashApp QR code info

      - `next_action.cashapp_handle_redirect_or_display_qr_code.qr_code.expires_at` (timestamp)
        The date (unix timestamp) when the QR code expires.

      - `next_action.cashapp_handle_redirect_or_display_qr_code.qr_code.image_url_png` (string)
        The image_url_png string used to render QR code

      - `next_action.cashapp_handle_redirect_or_display_qr_code.qr_code.image_url_svg` (string)
        The image_url_svg string used to render QR code

  - `next_action.redirect_to_url` (object, nullable)
    Contains instructions for authenticating a payment by redirecting your customer to another page or application.

    - `next_action.redirect_to_url.return_url` (string, nullable)
      If the customer does not exit their browser while authenticating, they will be redirected to this specified URL after completion.

    - `next_action.redirect_to_url.url` (string, nullable)
      The URL you must redirect your customer to in order to authenticate.

  - `next_action.type` (string)
    Type of the next action to perform. Refer to the other child attributes under `next_action` for available values. Examples include: `redirect_to_url`, `use_stripe_sdk`, `alipay_handle_redirect`, `oxxo_display_details`, or `verify_with_microdeposits`.

  - `next_action.use_stripe_sdk` (object, nullable)
    When confirming a SetupIntent with Stripe.js, Stripe.js depends on the contents of this dictionary to invoke authentication flows. The shape of the contents is subject to change and is only intended to be used by Stripe.js.

  - `next_action.verify_with_microdeposits` (object, nullable)
    Contains details describing microdeposits verification flow.

    - `next_action.verify_with_microdeposits.arrival_date` (timestamp)
      The timestamp when the microdeposits are expected to land.

    - `next_action.verify_with_microdeposits.hosted_verification_url` (string)
      The URL for the hosted verification page, which allows customers to verify their bank account.

    - `next_action.verify_with_microdeposits.microdeposit_type` (enum, nullable)
      The type of the microdeposit sent to the customer. Used to distinguish between different verification methods.

- `on_behalf_of` (string, nullable)
  The account (if any) for which the setup is intended.

- `payment_method` (string, nullable)
  ID of the payment method used with this SetupIntent. If the payment method is `card_present` and isn’t a digital wallet, then the [generated_card](https://docs.stripe.com/api/setup_attempts/object.md#setup_attempt_object-payment_method_details-card_present-generated_card) associated with the `latest_attempt` is attached to the Customer instead.

- `payment_method_configuration_details` (object, nullable)
  Information about the [payment method configuration](https://docs.stripe.com/docs/api/payment_method_configurations.md) used for this Setup Intent.

  - `payment_method_configuration_details.id` (string)
    ID of the payment method configuration used.

  - `payment_method_configuration_details.parent` (string, nullable)
    ID of the parent payment method configuration used.

- `payment_method_options` (object, nullable)
  Payment method-specific configuration for this SetupIntent.

  - `payment_method_options.acss_debit` (object, nullable)
    If the SetupIntent’s payment_method_types includes `acss_debit`, this hash contains the configurations that will be applied to each setup attempt of that type.

    - `payment_method_options.acss_debit.currency` (enum, nullable)
      Currency supported by the bank account
Possible enum values:
      - `cad`
        Canadian dollars

      - `usd`
        US dollars

    - `payment_method_options.acss_debit.mandate_options` (object, nullable)
      Additional fields for Mandate creation

      - `payment_method_options.acss_debit.mandate_options.custom_mandate_url` (string, nullable)
        A URL for custom mandate text

      - `payment_method_options.acss_debit.mandate_options.default_for` (array of enums, nullable)
        List of Stripe products where this mandate can be selected automatically.
Possible enum values:
        - `invoice`
          Enables payments for Stripe Invoices. ‘subscription’ must also be provided.

        - `subscription`
          Enables payments for Stripe Subscriptions. ‘invoice’ must also be provided.

      - `payment_method_options.acss_debit.mandate_options.interval_description` (string, nullable)
        Description of the interval. Only required if the ‘payment_schedule’ parameter is ‘interval’ or ‘combined’.

      - `payment_method_options.acss_debit.mandate_options.payment_schedule` (enum, nullable)
        Payment schedule for the mandate.
Possible enum values:
        - `combined`
          Payments can be initiated at a pre-defined interval or sporadically

        - `interval`
          Payments are initiated at a regular pre-defined interval

        - `sporadic`
          Payments are initiated sporadically

      - `payment_method_options.acss_debit.mandate_options.transaction_type` (enum, nullable)
        Transaction type of the mandate.
Possible enum values:
        - `business`
          Transactions are made for business reasons

        - `personal`
          Transactions are made for personal reasons

    - `payment_method_options.acss_debit.verification_method` (enum, nullable)
      Bank account verification method.
Possible enum values:
      - `automatic`
        Instant verification with fallback to microdeposits.

      - `instant`
        Instant verification.

      - `microdeposits`
        Verification using microdeposits.

  - `payment_method_options.amazon_pay` (object, nullable)
    If the SetupIntent’s payment_method_types includes `amazon_pay`, this hash contains the configurations that will be applied to each setup attempt of that type.

  - `payment_method_options.bacs_debit` (object, nullable)
    If the SetupIntent’s payment_method_types includes `bacs_debit`, this hash contains the configurations that will be applied to each setup attempt of that type.

    - `payment_method_options.bacs_debit.mandate_options` (object, nullable)
      Additional fields for Mandate creation

      - `payment_method_options.bacs_debit.mandate_options.reference_prefix` (string, nullable)
        Prefix used to generate the Mandate reference. Must be at most 12 characters long. Must consist of only uppercase letters, numbers, spaces, or the following special characters: ‘/’, ‘_’, ‘-’, ‘&’, ‘.’. Cannot begin with ‘DDIC’ or ‘STRIPE’.

  - `payment_method_options.card` (object, nullable)
    If the SetupIntent’s payment_method_types includes `card`, this hash contains the configurations that will be applied to each setup attempt of that type.

    - `payment_method_options.card.mandate_options` (object, nullable)
      Configuration options for setting up an eMandate for cards issued in India.

      - `payment_method_options.card.mandate_options.amount` (integer)
        Amount to be charged for future payments.

      - `payment_method_options.card.mandate_options.amount_type` (enum)
        One of `fixed` or `maximum`. If `fixed`, the `amount` param refers to the exact amount to be charged in future payments. If `maximum`, the amount charged can be up to the value passed for the `amount` param.
Possible enum values:
        - `fixed`
        - `maximum`

      - `payment_method_options.card.mandate_options.currency` (enum)
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

      - `payment_method_options.card.mandate_options.description` (string, nullable)
        A description of the mandate or subscription that is meant to be displayed to the customer.

        The maximum length is 200 characters.

      - `payment_method_options.card.mandate_options.end_date` (timestamp, nullable)
        End date of the mandate or subscription. If not provided, the mandate will be active until canceled. If provided, end date should be after start date.

      - `payment_method_options.card.mandate_options.interval` (enum)
        Specifies payment frequency. One of `day`, `week`, `month`, `year`, or `sporadic`.
Possible enum values:
        - `day`
        - `month`
        - `sporadic`
        - `week`
        - `year`

      - `payment_method_options.card.mandate_options.interval_count` (integer, nullable)
        The number of intervals between payments. For example, `interval=month` and `interval_count=3` indicates one payment every three months. Maximum of one year interval allowed (1 year, 12 months, or 52 weeks). This parameter is optional when `interval=sporadic`.

      - `payment_method_options.card.mandate_options.reference` (string)
        Unique identifier for the mandate or subscription.

        The maximum length is 80 characters.

      - `payment_method_options.card.mandate_options.start_date` (timestamp)
        Start date of the mandate or subscription. Start date should not be lesser than yesterday.

      - `payment_method_options.card.mandate_options.supported_types` (array of enums, nullable)
        Specifies the type of mandates supported. Possible values are `india`.
Possible enum values:
        - `india`

    - `payment_method_options.card.network` (enum, nullable)
      Selected network to process this SetupIntent on. Depends on the available networks of the card attached to the setup intent. Can be only set confirm-time.
Possible enum values:
      - `amex`
      - `cartes_bancaires`
      - `diners`
      - `discover`
      - `eftpos_au`
      - `girocard`
      - `interac`
      - `jcb`
      - `link`
      - `mastercard`
      - `unionpay`
      - `unknown`
      - `visa`

    - `payment_method_options.card.request_three_d_secure` (enum, nullable)
      We strongly recommend that you rely on our SCA Engine to automatically prompt your customers for authentication based on risk level and [other requirements](https://docs.stripe.com/docs/strong-customer-authentication.md). However, if you wish to request 3D Secure based on logic from your own fraud engine, provide this option. If not provided, this value defaults to `automatic`. Read our guide on [manually requesting 3D Secure](https://docs.stripe.com/docs/payments/3d-secure/authentication-flow.md#manual-three-ds) for more information on how this configuration interacts with Radar and our SCA Engine.
Possible enum values:
      - `any`
        Use `any` to manually request 3DS with a preference for a `frictionless` flow, increasing the likelihood of the authentication being completed without any additional input from the customer. 3DS will always be attempted if it is supported for the card, but Stripe can’t guarantee your preference because the issuer determines the ultimate authentication flow. To learn more about 3DS flows, read our [guide](https://stripe.com/guides/3d-secure-2#frictionless-authentication).

      - `automatic`
        (Default) Our SCA Engine automatically prompts your customers for authentication based on risk level and other requirements.

      - `challenge`
        Use `challenge` to request 3DS with a preference for a `challenge` flow, where the customer must respond to a prompt for active authentication. Stripe can’t guarantee your preference because the issuer determines the ultimate authentication flow. To learn more about 3DS flows, read our [guide](https://stripe.com/guides/3d-secure-2#frictionless-authentication).

  - `payment_method_options.card_present` (object, nullable)
    If the SetupIntent’s payment_method_types includes `card_present`, this hash contains the configurations that will be applied to each setup attempt of that type.

  - `payment_method_options.klarna` (object, nullable)
    If the SetupIntent’s payment_method_types includes `klarna`, this hash contains the configurations that will be applied to each setup attempt of that type.

    - `payment_method_options.klarna.currency` (enum, nullable)
      The currency of the setup intent. Three letter ISO currency code.

    - `payment_method_options.klarna.preferred_locale` (string, nullable)
      Preferred locale of the Klarna checkout page that the customer is redirected to.

  - `payment_method_options.link` (object, nullable)
    If the SetupIntent’s payment_method_types includes `link`, this hash contains the configurations that will be applied to each setup attempt of that type.

  - `payment_method_options.paypal` (object, nullable)
    If the SetupIntent’s payment_method_types includes `paypal`, this hash contains the configurations that will be applied to each setup attempt of that type.

    - `payment_method_options.paypal.billing_agreement_id` (string, nullable)
      The PayPal Billing Agreement ID (BAID). This is an ID generated by PayPal which represents the mandate between the merchant and the customer.

  - `payment_method_options.payto` (object, nullable)
    If the SetupIntent’s payment_method_types includes `payto`, this hash contains the configurations that will be applied to each setup attempt of that type.

    - `payment_method_options.payto.mandate_options` (object, nullable)
      Additional fields for Mandate creation.

      - `payment_method_options.payto.mandate_options.amount` (integer, nullable)
        Amount that will be collected. It is required when `amount_type` is `fixed`.

      - `payment_method_options.payto.mandate_options.amount_type` (enum, nullable)
        The type of amount that will be collected. The amount charged must be exact or up to the value of `amount` param for `fixed` or `maximum` type respectively. Defaults to `maximum`.
Possible enum values:
        - `fixed`
          The amount is the exact amount that will be charged.

        - `maximum`
          The amount is the maximum amount that can be charged.

      - `payment_method_options.payto.mandate_options.end_date` (string, nullable)
        Date, in YYYY-MM-DD format, after which payments will not be collected. Defaults to no end date.

      - `payment_method_options.payto.mandate_options.payment_schedule` (enum, nullable)
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

      - `payment_method_options.payto.mandate_options.payments_per_period` (integer, nullable)
        The number of payments that will be made during a payment period. Defaults to 1 except for when `payment_schedule` is `adhoc`. In that case, it defaults to no limit.

      - `payment_method_options.payto.mandate_options.purpose` (enum, nullable)
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

      - `payment_method_options.payto.mandate_options.start_date` (string, nullable)
        Date, in YYYY-MM-DD format, from which payments will be collected. Defaults to confirmation time.

  - `payment_method_options.sepa_debit` (object, nullable)
    If the SetupIntent’s payment_method_types includes `sepa_debit`, this hash contains the configurations that will be applied to each setup attempt of that type.

    - `payment_method_options.sepa_debit.mandate_options` (object, nullable)
      Additional fields for Mandate creation

      - `payment_method_options.sepa_debit.mandate_options.reference_prefix` (string, nullable)
        Prefix used to generate the Mandate reference. Must be at most 12 characters long. Must consist of only uppercase letters, numbers, spaces, or the following special characters: ‘/’, ‘_’, ‘-’, ‘&’, ‘.’. Cannot begin with ‘STRIPE’.

  - `payment_method_options.us_bank_account` (object, nullable)
    If the SetupIntent’s payment_method_types includes `us_bank_account`, this hash contains the configurations that will be applied to each setup attempt of that type.

    - `payment_method_options.us_bank_account.financial_connections` (object, nullable)
      Additional fields for Financial Connections Session creation

      - `payment_method_options.us_bank_account.financial_connections.filters` (object, nullable)
        Filter the list of accounts that are allowed to be linked.

        - `payment_method_options.us_bank_account.financial_connections.filters.account_subcategories` (array of enums, nullable)
          The account subcategories to use to filter for possible accounts to link. Valid subcategories are `checking` and `savings`.
Possible enum values:
          - `checking`
            Bank account subcategory is checking

          - `savings`
            Bank account subcategory is savings

      - `payment_method_options.us_bank_account.financial_connections.permissions` (array of enums, nullable)
        The list of permissions to request. The `payment_method` permission must be included.
Possible enum values:
        - `balances`
          Allows accessing balance data from the account.

        - `ownership`
          Allows accessing ownership data from the account.

        - `payment_method`
          Allows the creation of a payment method from the account.

        - `transactions`
          Allows accessing transactions data from the account.

      - `payment_method_options.us_bank_account.financial_connections.prefetch` (array of enums, nullable)
        Data features requested to be retrieved upon account creation.
Possible enum values:
        - `balances`
          Requests to prefetch balance data on accounts collected in this session.

        - `ownership`
          Requests to prefetch ownership data on accounts collected in this session.

        - `transactions`
          Requests to prefetch transaction data on accounts collected in this session.

      - `payment_method_options.us_bank_account.financial_connections.return_url` (string, nullable)
        For webview integrations only. Upon completing OAuth login in the native browser, the user will be redirected to this URL to return to your app.

    - `payment_method_options.us_bank_account.mandate_options` (object, nullable)
      Additional fields for Mandate creation

      - `payment_method_options.us_bank_account.mandate_options.collection_method` (enum, nullable)
        Mandate collection method
Possible enum values:
        - `paper`
          Mandate customer acceptance was collected using a paper document

    - `payment_method_options.us_bank_account.verification_method` (enum, nullable)
      Bank account verification method.
Possible enum values:
      - `automatic`
        Instant verification with fallback to microdeposits.

      - `instant`
        Instant verification only.

      - `microdeposits`
        Verification using microdeposits. Cannot be used with Stripe Checkout, Hosted Invoices, or Payment Element.

- `payment_method_types` (array of strings)
  The list of payment method types (e.g. card) that this SetupIntent is allowed to set up. A list of valid payment method types can be found [here](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-type).

- `single_use_mandate` (string, nullable)
  ID of the single_use Mandate generated by the SetupIntent.

- `status` (enum)
  [Status](https://docs.stripe.com/docs/payments/intents.md#intent-statuses) of this SetupIntent, one of `requires_payment_method`, `requires_confirmation`, `requires_action`, `processing`, `canceled`, or `succeeded`.
Possible enum values:
  - `canceled`
  - `processing`
  - `requires_action`
  - `requires_confirmation`
  - `requires_payment_method`
  - `succeeded`

- `usage` (string)
  Indicates how the payment method is intended to be used in the future.

  Use `on_session` if you intend to only reuse the payment method when the customer is in your checkout flow. Use `off_session` if your customer may or may not be in your checkout flow. If not provided, this value defaults to `off_session`.

### The SetupIntent object

```json
{
  "id": "seti_1Mm8s8LkdIwHu7ix0OXBfTRG",
  "object": "setup_intent",
  "application": null,
  "cancellation_reason": null,
  "client_secret": "seti_1Mm8s8LkdIwHu7ix0OXBfTRG_secret_NXDICkPqPeiBTAFqWmkbff09lRmSVXe",
  "created": 1678942624,
  "customer": null,
  "description": null,
  "flow_directions": null,
  "last_setup_error": null,
  "latest_attempt": null,
  "livemode": false,
  "mandate": null,
  "metadata": {},
  "next_action": null,
  "on_behalf_of": null,
  "payment_method": null,
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
  "status": "requires_payment_method",
  "usage": "off_session"
}
```