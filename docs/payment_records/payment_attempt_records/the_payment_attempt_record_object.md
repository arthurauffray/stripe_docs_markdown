# The Payment Attempt Record object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `amount` (object)
  The amount you intend to collect for this payment.

  - `amount.currency` (enum)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `amount.value` (integer)
    A positive integer representing the amount in the currency’s [minor unit](https://docs.stripe.com/docs/currencies.md#zero-decimal). For example, `100` can represent 1 USD or 100 JPY.

- `amount_authorized` (object)
  The portion of the requested amount that has been authorized to be guaranteed by the payment provider.

  - `amount_authorized.currency` (enum)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `amount_authorized.value` (integer)
    A positive integer representing the amount in the currency’s [minor unit](https://docs.stripe.com/docs/currencies.md#zero-decimal). For example, `100` can represent 1 USD or 100 JPY.

- `amount_canceled` (object)
  The portion of the requested amount that has been canceled by the user, or that you no longer intend to collect.

  - `amount_canceled.currency` (enum)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `amount_canceled.value` (integer)
    A positive integer representing the amount in the currency’s [minor unit](https://docs.stripe.com/docs/currencies.md#zero-decimal). For example, `100` can represent 1 USD or 100 JPY.

- `amount_failed` (object)
  The portion of the requested amount that failed to be collected.

  - `amount_failed.currency` (enum)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `amount_failed.value` (integer)
    A positive integer representing the amount in the currency’s [minor unit](https://docs.stripe.com/docs/currencies.md#zero-decimal). For example, `100` can represent 1 USD or 100 JPY.

- `amount_guaranteed` (object)
  The portion of the requested amount that has been guaranteed by the payment provider.

  - `amount_guaranteed.currency` (enum)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `amount_guaranteed.value` (integer)
    A positive integer representing the amount in the currency’s [minor unit](https://docs.stripe.com/docs/currencies.md#zero-decimal). For example, `100` can represent 1 USD or 100 JPY.

- `amount_refunded` (object)
  The amount that has been refunded to the customer on this payment.

  - `amount_refunded.currency` (enum)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `amount_refunded.value` (integer)
    A positive integer representing the amount in the currency’s [minor unit](https://docs.stripe.com/docs/currencies.md#zero-decimal). For example, `100` can represent 1 USD or 100 JPY.

- `amount_requested` (object)
  The amount you initially requested for this payment.

  - `amount_requested.currency` (enum)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `amount_requested.value` (integer)
    A positive integer representing the amount in the currency’s [minor unit](https://docs.stripe.com/docs/currencies.md#zero-decimal). For example, `100` can represent 1 USD or 100 JPY.

- `application` (string, nullable)
  ID of the Connect application that created the PaymentAttemptRecord.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `customer_details` (object, nullable)
  Customer information for this payment.

  - `customer_details.customer` (string, nullable)
    ID of the Stripe Customer associated with this payment.

  - `customer_details.email` (string, nullable)
    The customer’s email address.

  - `customer_details.name` (string, nullable)
    The customer’s name.

  - `customer_details.phone` (string, nullable)
    The customer’s phone number.

- `customer_presence` (enum, nullable)
  Indicates whether the customer was present in your checkout flow during this payment.
Possible enum values:
  - `off_session`
    The customer was not present during the transaction.

  - `on_session`
    The customer was present during the transaction.

- `description` (string, nullable)
  An arbitrary string attached to the object. Often useful for displaying to users.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `payment_method_details` (object, nullable)
  Information about the Payment Method debited for this payment.

  - `payment_method_details.ach_credit_transfer` (object, nullable)
    If this is a `ach_credit_transfer` payment, this hash contains a snapshot of the transaction specific details of the `ach_credit_transfer` payment method.

    - `payment_method_details.ach_credit_transfer.account_number` (string, nullable)
      Account number to transfer funds to.

    - `payment_method_details.ach_credit_transfer.bank_name` (string, nullable)
      Name of the bank associated with the routing number.

    - `payment_method_details.ach_credit_transfer.routing_number` (string, nullable)
      Routing transit number for the bank account to transfer funds to.

    - `payment_method_details.ach_credit_transfer.swift_code` (string, nullable)
      SWIFT code of the bank associated with the routing number.

  - `payment_method_details.ach_debit` (object, nullable)
    If this is a `ach_debit` payment, this hash contains a snapshot of the transaction specific details of the `ach_debit` payment method.

    - `payment_method_details.ach_debit.account_holder_type` (enum, nullable)
      Type of entity that holds the account. This can be either `individual` or `company`.
Possible enum values:
      - `company`
      - `individual`

    - `payment_method_details.ach_debit.bank_name` (string, nullable)
      Name of the bank associated with the bank account.

    - `payment_method_details.ach_debit.country` (string, nullable)
      Two-letter ISO code representing the country the bank account is located in.

    - `payment_method_details.ach_debit.fingerprint` (string, nullable)
      Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

    - `payment_method_details.ach_debit.last4` (string, nullable)
      Last four digits of the bank account number.

    - `payment_method_details.ach_debit.routing_number` (string, nullable)
      Routing transit number of the bank account.

  - `payment_method_details.acss_debit` (object, nullable)
    If this is a `acss_debit` payment, this hash contains a snapshot of the transaction specific details of the `acss_debit` payment method.

    - `payment_method_details.acss_debit.bank_name` (string, nullable)
      Name of the bank associated with the bank account.

    - `payment_method_details.acss_debit.expected_debit_date` (string, nullable)
      Estimated date to debit the customer’s bank account. A date string in YYYY-MM-DD format.

    - `payment_method_details.acss_debit.fingerprint` (string, nullable)
      Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

    - `payment_method_details.acss_debit.institution_number` (string, nullable)
      Institution number of the bank account

    - `payment_method_details.acss_debit.last4` (string, nullable)
      Last four digits of the bank account number.

    - `payment_method_details.acss_debit.mandate` (string, nullable)
      ID of the mandate used to make this payment.

    - `payment_method_details.acss_debit.transit_number` (string, nullable)
      Transit number of the bank account.

  - `payment_method_details.affirm` (object, nullable)
    If this is a `affirm` payment, this hash contains a snapshot of the transaction specific details of the `affirm` payment method.

    - `payment_method_details.affirm.location` (string, nullable)
      ID of the [location](https://docs.stripe.com/docs/api/terminal/locations.md) that this transaction’s reader is assigned to.

    - `payment_method_details.affirm.reader` (string, nullable)
      ID of the [reader](https://docs.stripe.com/docs/api/terminal/readers.md) this transaction was made on.

    - `payment_method_details.affirm.transaction_id` (string, nullable)
      The Affirm transaction ID associated with this payment.

  - `payment_method_details.afterpay_clearpay` (object, nullable)
    If this is a `afterpay_clearpay` payment, this hash contains a snapshot of the transaction specific details of the `afterpay_clearpay` payment method.

    - `payment_method_details.afterpay_clearpay.order_id` (string, nullable)
      The Afterpay order ID associated with this payment intent.

    - `payment_method_details.afterpay_clearpay.reference` (string, nullable)
      Order identifier shown to the merchant in Afterpay’s online portal.

  - `payment_method_details.alipay` (object, nullable)
    If this is a `alipay` payment, this hash contains a snapshot of the transaction specific details of the `alipay` payment method.

    - `payment_method_details.alipay.buyer_id` (string, nullable)
      Uniquely identifies this particular Alipay account. You can use this attribute to check whether two Alipay accounts are the same.

    - `payment_method_details.alipay.fingerprint` (string, nullable)
      Uniquely identifies this particular Alipay account. You can use this attribute to check whether two Alipay accounts are the same.

    - `payment_method_details.alipay.transaction_id` (string, nullable)
      Transaction ID of this particular Alipay transaction.

  - `payment_method_details.alma` (object, nullable)
    If this is a `alma` payment, this hash contains a snapshot of the transaction specific details of the `alma` payment method.

    - `payment_method_details.alma.installments` (object, nullable)
      Installment options that a buyer selected, if any.

      - `payment_method_details.alma.installments.count` (integer)
        The number of installments.

    - `payment_method_details.alma.transaction_id` (string, nullable)
      The Alma transaction ID associated with this payment.

  - `payment_method_details.amazon_pay` (object, nullable)
    If this is a `amazon_pay` payment, this hash contains a snapshot of the transaction specific details of the `amazon_pay` payment method.

    - `payment_method_details.amazon_pay.funding` (object, nullable)
      the funding details of the underlying payment method.

      - `payment_method_details.amazon_pay.funding.card` (object, nullable)
        the funding details of the passthrough card.

        - `payment_method_details.amazon_pay.funding.card.brand` (string, nullable)
          Card brand. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `jcb`, `link`, `mastercard`, `unionpay`, `visa` or `unknown`.

        - `payment_method_details.amazon_pay.funding.card.country` (string, nullable)
          Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you’ve collected.

        - `payment_method_details.amazon_pay.funding.card.exp_month` (integer, nullable)
          Two-digit number representing the card’s expiration month.

        - `payment_method_details.amazon_pay.funding.card.exp_year` (integer, nullable)
          Four-digit number representing the card’s expiration year.

        - `payment_method_details.amazon_pay.funding.card.funding` (string, nullable)
          Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.

        - `payment_method_details.amazon_pay.funding.card.last4` (string, nullable)
          The last four digits of the card.

      - `payment_method_details.amazon_pay.funding.type` (enum, nullable)
        funding type of the underlying payment method.

    - `payment_method_details.amazon_pay.transaction_id` (string, nullable)
      The Amazon Pay transaction ID associated with this payment.

  - `payment_method_details.au_becs_debit` (object, nullable)
    If this is a `au_becs_debit` payment, this hash contains a snapshot of the transaction specific details of the `au_becs_debit` payment method.

    - `payment_method_details.au_becs_debit.bsb_number` (string, nullable)
      Bank-State-Branch number of the bank account.

    - `payment_method_details.au_becs_debit.expected_debit_date` (string, nullable)
      Estimated date to debit the customer’s bank account. A date string in YYYY-MM-DD format.

    - `payment_method_details.au_becs_debit.fingerprint` (string, nullable)
      Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

    - `payment_method_details.au_becs_debit.last4` (string, nullable)
      Last four digits of the bank account number.

    - `payment_method_details.au_becs_debit.mandate` (string, nullable)
      ID of the mandate used to make this payment.

  - `payment_method_details.bacs_debit` (object, nullable)
    If this is a `bacs_debit` payment, this hash contains a snapshot of the transaction specific details of the `bacs_debit` payment method.

    - `payment_method_details.bacs_debit.expected_debit_date` (string, nullable)
      Estimated date to debit the customer’s bank account. A date string in YYYY-MM-DD format.

    - `payment_method_details.bacs_debit.fingerprint` (string, nullable)
      Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

    - `payment_method_details.bacs_debit.last4` (string, nullable)
      Last four digits of the bank account number.

    - `payment_method_details.bacs_debit.mandate` (string, nullable)
      ID of the mandate used to make this payment.

    - `payment_method_details.bacs_debit.sort_code` (string, nullable)
      Sort code of the bank account. (e.g., `10-20-30`)

  - `payment_method_details.bancontact` (object, nullable)
    If this is a `bancontact` payment, this hash contains a snapshot of the transaction specific details of the `bancontact` payment method.

    - `payment_method_details.bancontact.bank_code` (string, nullable)
      Bank code of bank associated with the bank account.

    - `payment_method_details.bancontact.bank_name` (string, nullable)
      Name of the bank associated with the bank account.

    - `payment_method_details.bancontact.bic` (string, nullable)
      Bank Identifier Code of the bank associated with the bank account.

    - `payment_method_details.bancontact.generated_sepa_debit` (string, nullable)
      The ID of the SEPA Direct Debit PaymentMethod which was generated by this Charge.

    - `payment_method_details.bancontact.generated_sepa_debit_mandate` (string, nullable)
      The mandate for the SEPA Direct Debit PaymentMethod which was generated by this Charge.

    - `payment_method_details.bancontact.iban_last4` (string, nullable)
      Last four characters of the IBAN.

    - `payment_method_details.bancontact.preferred_language` (enum, nullable)
      Preferred language of the Bancontact authorization page that the customer is redirected to. Can be one of `en`, `de`, `fr`, or `nl`
Possible enum values:
      - `de`
      - `en`
      - `fr`
      - `nl`

    - `payment_method_details.bancontact.verified_name` (string, nullable)
      Owner’s verified full name. Values are verified or provided by Bancontact directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

  - `payment_method_details.billie` (object, nullable)
    If this is a `billie` payment, this hash contains a snapshot of the transaction specific details of the `billie` payment method.

    - `payment_method_details.billie.transaction_id` (string, nullable)
      The Billie transaction ID associated with this payment.

  - `payment_method_details.billing_details` (object, nullable)
    The billing details associated with the method of payment.

    - `payment_method_details.billing_details.address` (object)
      The billing address associated with the method of payment.

      - `payment_method_details.billing_details.address.city` (string, nullable)
        City, district, suburb, town, or village.

      - `payment_method_details.billing_details.address.country` (string, nullable)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `payment_method_details.billing_details.address.line1` (string, nullable)
        Address line 1, such as the street, PO Box, or company name.

      - `payment_method_details.billing_details.address.line2` (string, nullable)
        Address line 2, such as the apartment, suite, unit, or building.

      - `payment_method_details.billing_details.address.postal_code` (string, nullable)
        ZIP or postal code.

      - `payment_method_details.billing_details.address.state` (string, nullable)
        State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

    - `payment_method_details.billing_details.email` (string, nullable)
      The billing email associated with the method of payment.

    - `payment_method_details.billing_details.name` (string, nullable)
      The billing name associated with the method of payment.

    - `payment_method_details.billing_details.phone` (string, nullable)
      The billing phone number associated with the method of payment.

  - `payment_method_details.blik` (object, nullable)
    If this is a `blik` payment, this hash contains a snapshot of the transaction specific details of the `blik` payment method.

    - `payment_method_details.blik.buyer_id` (string, nullable)
      A unique and immutable identifier assigned by BLIK to every buyer.

  - `payment_method_details.boleto` (object, nullable)
    If this is a `boleto` payment, this hash contains a snapshot of the transaction specific details of the `boleto` payment method.

    - `payment_method_details.boleto.tax_id` (string)
      The tax ID of the customer (CPF for individuals consumers or CNPJ for businesses consumers)

  - `payment_method_details.card` (object, nullable)
    Information about the card payment method used to make this payment.

    - `payment_method_details.card.authorization_code` (string, nullable)
      The authorization code of the payment.

    - `payment_method_details.card.brand` (enum)
      Card brand. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `jcb`, `link`, `mastercard`, `unionpay`, `visa` or `unknown`.
Possible enum values:
      - `amex`
        American Express.

      - `cartes_bancaires`
        Cartes Bancaires card.

      - `diners`
        Diners Club card.

      - `discover`
        Discover card.

      - `eftpos_au`
        EFTPOS card in Australia.

      - `interac`
        Interac card.

      - `jcb`
        JCB card.

      - `link`
        Link card.

      - `mastercard`
        Mastercard.

      - `unionpay`
        UnionPay card.

      - `unknown`
        Unknown card brand.

      - `visa`
        Visa card.

    - `payment_method_details.card.capture_before` (timestamp, nullable)
      When using manual capture, a future timestamp at which the charge will be automatically refunded if uncaptured.

    - `payment_method_details.card.checks` (object, nullable)
      Check results by Card networks on Card address and CVC at time of payment.

    - `payment_method_details.card.country` (string, nullable)
      Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you’ve collected.

    - `payment_method_details.card.description` (string, nullable)
      A high-level description of the type of cards issued in this range.

    - `payment_method_details.card.exp_month` (integer)
      Two-digit number representing the card’s expiration month.

    - `payment_method_details.card.exp_year` (integer)
      Four-digit number representing the card’s expiration year.

    - `payment_method_details.card.fingerprint` (string, nullable)
      Uniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.

      *As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card—one for India and one for the rest of the world.*

    - `payment_method_details.card.funding` (enum)
      Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.
Possible enum values:
      - `credit`
        Credit card.

      - `debit`
        Debit card.

      - `prepaid`
        Prepaid card.

      - `unknown`
        Unknown funding source.

    - `payment_method_details.card.iin` (string, nullable)
      Issuer identification number of the card.

    - `payment_method_details.card.installments` (object, nullable)
      Installment details for this payment.

    - `payment_method_details.card.issuer` (string, nullable)
      The name of the card’s issuing bank.

    - `payment_method_details.card.last4` (string)
      The last four digits of the card.

    - `payment_method_details.card.network` (enum, nullable)
      Identifies which network this charge was processed on. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `interac`, `jcb`, `link`, `mastercard`, `unionpay`, `visa`, or `unknown`.
Possible enum values:
      - `amex`
        Amex network.

      - `cartes_bancaires`
        Cartes Bancaires network.

      - `diners`
        Diners Club network.

      - `discover`
        Discover network.

      - `eftpos_au`
        EFTPOS network in Australia.

      - `interac`
        Interac network.

      - `jcb`
        JCB network.

      - `link`
        Link network.

      - `mastercard`
        Mastercard network.

      - `unionpay`
        UnionPay network.

      - `unknown`
        Unknown network.

      - `visa`
        Visa network.

    - `payment_method_details.card.network_advice_code` (string, nullable)
      Advice code from the card network for the failed payment.

    - `payment_method_details.card.network_decline_code` (string, nullable)
      Decline code from the card network for the failed payment.

    - `payment_method_details.card.network_token` (object, nullable)
      If this card has network token credentials, this contains the details of the network token credentials.

      - `payment_method_details.card.network_token.used` (boolean)
        Indicates if Stripe used a network token, either user provided or Stripe managed when processing the transaction.

    - `payment_method_details.card.network_transaction_id` (string, nullable)
      This is used by the financial networks to identify a transaction. Visa calls this the Transaction ID, Mastercard calls this the Trace ID, and American Express calls this the Acquirer Reference Data. This value will be present if it is returned by the financial network in the authorization response, and null otherwise.

    - `payment_method_details.card.stored_credential_usage` (enum, nullable)
      The transaction type that was passed for an off-session, Merchant-Initiated transaction, one of `recurring` or `unscheduled`.
Possible enum values:
      - `recurring`
        Use `recurring` if the off-session payment occurs at regularly scheduled intervals (for example, as part of a monthly subscription).

      - `unscheduled`
        Use `unscheduled` if the off-session payment does not occur at regular intervals on a scheduled date (for example, an automatic account top-up when a balance falls below a minimum).

    - `payment_method_details.card.three_d_secure` (object, nullable)
      Populated if this transaction used 3D Secure authentication.

    - `payment_method_details.card.wallet` (object, nullable)
      If this Card is part of a card wallet, this contains the details of the card wallet.

      - `payment_method_details.card.wallet.apple_pay` (object, nullable)
        If this is a `apple_pay` card wallet, this hash contains details about the wallet.

        - `payment_method_details.card.wallet.apple_pay.type` (string)
          Type of the apple_pay transaction, one of `apple_pay` or `apple_pay_later`.

      - `payment_method_details.card.wallet.dynamic_last4` (string, nullable)
        (For tokenized numbers only.) The last four digits of the device account number.

      - `payment_method_details.card.wallet.google_pay` (object, nullable)
        If this is a `google_pay` card wallet, this hash contains details about the wallet.

      - `payment_method_details.card.wallet.type` (string)
        The type of the card wallet, one of `apple_pay` or `google_pay`. An additional hash is included on the Wallet subhash with a name matching this value. It contains additional information specific to the card wallet type.

  - `payment_method_details.card_present` (object, nullable)
    If this is a `card_present` payment, this hash contains a snapshot of the transaction specific details of the `card_present` payment method.

    - `payment_method_details.card_present.amount_authorized` (integer, nullable)
      The authorized amount

    - `payment_method_details.card_present.brand` (string, nullable)
      Card brand. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `jcb`, `link`, `mastercard`, `unionpay`, `visa` or `unknown`.

    - `payment_method_details.card_present.brand_product` (string, nullable)
      The [product code](https://stripe.com/docs/card-product-codes) that identifies the specific program or product associated with a card.

    - `payment_method_details.card_present.capture_before` (timestamp, nullable)
      When using manual capture, a future timestamp after which the charge will be automatically refunded if uncaptured.

    - `payment_method_details.card_present.cardholder_name` (string, nullable)
      The cardholder name as read from the card, in [ISO 7813](https://en.wikipedia.org/wiki/ISO/IEC_7813) format. May include alphanumeric characters, special characters and first/last name separator (`/`). In some cases, the cardholder name may not be available depending on how the issuer has configured the card. Cardholder name is typically not available on swipe or contactless payments, such as those made with Apple Pay and Google Pay.

    - `payment_method_details.card_present.country` (string, nullable)
      Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you’ve collected.

    - `payment_method_details.card_present.description` (string, nullable)
      A high-level description of the type of cards issued in this range.

    - `payment_method_details.card_present.emv_auth_data` (string, nullable)
      Authorization response cryptogram.

    - `payment_method_details.card_present.exp_month` (integer)
      Two-digit number representing the card’s expiration month.

    - `payment_method_details.card_present.exp_year` (integer)
      Four-digit number representing the card’s expiration year.

    - `payment_method_details.card_present.fingerprint` (string, nullable)
      Uniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.

      *As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card—one for India and one for the rest of the world.*

    - `payment_method_details.card_present.funding` (string, nullable)
      Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.

    - `payment_method_details.card_present.generated_card` (string, nullable)
      ID of a card PaymentMethod generated from the card_present PaymentMethod that may be attached to a Customer for future transactions. Only present if it was possible to generate a card PaymentMethod.

    - `payment_method_details.card_present.incremental_authorization_supported` (boolean)
      Whether this [PaymentIntent](https://docs.stripe.com/docs/api/payment_intents.md) is eligible for incremental authorizations. Request support using [request_incremental_authorization_support](https://docs.stripe.com/docs/api/payment_intents/create.md#create_payment_intent-payment_method_options-card_present-request_incremental_authorization_support).

    - `payment_method_details.card_present.issuer` (string, nullable)
      The name of the card’s issuing bank.

    - `payment_method_details.card_present.last4` (string, nullable)
      The last four digits of the card.

    - `payment_method_details.card_present.network` (string, nullable)
      Identifies which network this charge was processed on. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `interac`, `jcb`, `link`, `mastercard`, `unionpay`, `visa`, or `unknown`.

    - `payment_method_details.card_present.network_transaction_id` (string, nullable)
      This is used by the financial networks to identify a transaction. Visa calls this the Transaction ID, Mastercard calls this the Trace ID, and American Express calls this the Acquirer Reference Data. This value will be present if it is returned by the financial network in the authorization response, and null otherwise.

    - `payment_method_details.card_present.offline` (object, nullable)
      Details about payments collected offline.

      - `payment_method_details.card_present.offline.stored_at` (timestamp, nullable)
        Time at which the payment was collected while offline

      - `payment_method_details.card_present.offline.type` (enum, nullable)
        The method used to process this payment method offline. Only deferred is allowed.
Possible enum values:
        - `deferred`

    - `payment_method_details.card_present.overcapture_supported` (boolean)
      Defines whether the authorized amount can be over-captured or not

    - `payment_method_details.card_present.preferred_locales` (array of strings, nullable)
      The languages that the issuing bank recommends using for localizing any customer-facing text, as read from the card. Referenced from EMV tag 5F2D, data encoded on the card’s chip.

    - `payment_method_details.card_present.read_method` (enum, nullable)
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

    - `payment_method_details.card_present.receipt` (object, nullable)
      A collection of fields required to be displayed on receipts. Only required for EMV transactions.

      - `payment_method_details.card_present.receipt.account_type` (enum, nullable)
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

      - `payment_method_details.card_present.receipt.application_cryptogram` (string, nullable)
        The Application Cryptogram, a unique value generated by the card to authenticate the transaction with issuers.

      - `payment_method_details.card_present.receipt.application_preferred_name` (string, nullable)
        The Application Identifier (AID) on the card used to determine which networks are eligible to process the transaction. Referenced from EMV tag 9F12, data encoded on the card’s chip.

      - `payment_method_details.card_present.receipt.authorization_code` (string, nullable)
        Identifier for this transaction.

      - `payment_method_details.card_present.receipt.authorization_response_code` (string, nullable)
        EMV tag 8A. A code returned by the card issuer.

      - `payment_method_details.card_present.receipt.cardholder_verification_method` (string, nullable)
        Describes the method used by the cardholder to verify ownership of the card. One of the following: `approval`, `failure`, `none`, `offline_pin`, `offline_pin_and_signature`, `online_pin`, or `signature`.

      - `payment_method_details.card_present.receipt.dedicated_file_name` (string, nullable)
        Similar to the application_preferred_name, identifying the applications (AIDs) available on the card. Referenced from EMV tag 84.

      - `payment_method_details.card_present.receipt.terminal_verification_results` (string, nullable)
        A 5-byte string that records the checks and validations that occur between the card and the terminal. These checks determine how the terminal processes the transaction and what risk tolerance is acceptable. Referenced from EMV Tag 95.

      - `payment_method_details.card_present.receipt.transaction_status_information` (string, nullable)
        An indication of which steps were completed during the card read process. Referenced from EMV Tag 9B.

    - `payment_method_details.card_present.wallet` (object, nullable)
      If a mobile wallet was presented in the transaction, this contains the details of the mobile wallet.

      - `payment_method_details.card_present.wallet.type` (enum)
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

  - `payment_method_details.cashapp` (object, nullable)
    If this is a `cashapp` payment, this hash contains a snapshot of the transaction specific details of the `cashapp` payment method.

    - `payment_method_details.cashapp.buyer_id` (string, nullable)
      A unique and immutable identifier assigned by Cash App to every buyer.

    - `payment_method_details.cashapp.cashtag` (string, nullable)
      A public identifier for buyers using Cash App.

    - `payment_method_details.cashapp.transaction_id` (string, nullable)
      A unique and immutable identifier of payments assigned by Cash App

  - `payment_method_details.crypto` (object, nullable)
    If this is a `crypto` payment, this hash contains a snapshot of the transaction specific details of the `crypto` payment method.

    - `payment_method_details.crypto.buyer_address` (string, nullable)
      The wallet address of the customer.

    - `payment_method_details.crypto.network` (enum, nullable)
      The blockchain network that the transaction was sent on.
Possible enum values:
      - `base`
        Base

      - `ethereum`
        Ethereum

      - `polygon`
        Polygon

      - `solana`
        Solana

    - `payment_method_details.crypto.token_currency` (enum, nullable)
      The token currency that the transaction was sent with.
Possible enum values:
      - `usdc`
        USDC

      - `usdg`
        USDG

      - `usdp`
        USDP

    - `payment_method_details.crypto.transaction_hash` (string, nullable)
      The blockchain transaction hash of the crypto payment.

  - `payment_method_details.custom` (object, nullable)
    Information about the custom (user-defined) payment method used to make this payment.

    - `payment_method_details.custom.display_name` (string)
      Display name for the custom (user-defined) payment method type used to make this payment.

    - `payment_method_details.custom.type` (string, nullable)
      The custom payment method type associated with this payment.

  - `payment_method_details.customer_balance` (object, nullable)
    If this is a `customer_balance` payment, this hash contains a snapshot of the transaction specific details of the `customer_balance` payment method.

  - `payment_method_details.eps` (object, nullable)
    If this is a `eps` payment, this hash contains a snapshot of the transaction specific details of the `eps` payment method.

    - `payment_method_details.eps.bank` (enum, nullable)
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

    - `payment_method_details.eps.verified_name` (string, nullable)
      Owner’s verified full name. Values are verified or provided by EPS directly (if supported) at the time of authorization or settlement. They cannot be set or mutated. EPS rarely provides this information so the attribute is usually empty.

  - `payment_method_details.fpx` (object, nullable)
    If this is a `fpx` payment, this hash contains a snapshot of the transaction specific details of the `fpx` payment method.

    - `payment_method_details.fpx.bank` (enum)
      The customer’s bank. Can be one of `affin_bank`, `agrobank`, `alliance_bank`, `ambank`, `bank_islam`, `bank_muamalat`, `bank_rakyat`, `bsn`, `cimb`, `hong_leong_bank`, `hsbc`, `kfh`, `maybank2u`, `ocbc`, `public_bank`, `rhb`, `standard_chartered`, `uob`, `deutsche_bank`, `maybank2e`, `pb_enterprise`, or `bank_of_china`.
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

    - `payment_method_details.fpx.transaction_id` (string, nullable)
      Unique transaction id generated by FPX for every request from the merchant

  - `payment_method_details.giropay` (object, nullable)
    If this is a `giropay` payment, this hash contains a snapshot of the transaction specific details of the `giropay` payment method.

    - `payment_method_details.giropay.bank_code` (string, nullable)
      Bank code of bank associated with the bank account.

    - `payment_method_details.giropay.bank_name` (string, nullable)
      Name of the bank associated with the bank account.

    - `payment_method_details.giropay.bic` (string, nullable)
      Bank Identifier Code of the bank associated with the bank account.

    - `payment_method_details.giropay.verified_name` (string, nullable)
      Owner’s verified full name. Values are verified or provided by Giropay directly (if supported) at the time of authorization or settlement. They cannot be set or mutated. Giropay rarely provides this information so the attribute is usually empty.

  - `payment_method_details.grabpay` (object, nullable)
    If this is a `grabpay` payment, this hash contains a snapshot of the transaction specific details of the `grabpay` payment method.

    - `payment_method_details.grabpay.transaction_id` (string, nullable)
      Unique transaction id generated by GrabPay

  - `payment_method_details.ideal` (object, nullable)
    If this is a `ideal` payment, this hash contains a snapshot of the transaction specific details of the `ideal` payment method.

    - `payment_method_details.ideal.bank` (enum, nullable)
      The customer’s bank. Can be one of `abn_amro`, `asn_bank`, `bunq`, `buut`, `finom`, `handelsbanken`, `ing`, `knab`, `mollie`, `moneyou`, `n26`, `nn`, `rabobank`, `regiobank`, `revolut`, `sns_bank`, `triodos_bank`, `van_lanschot`, or `yoursafe`.
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

    - `payment_method_details.ideal.bic` (enum, nullable)
      The Bank Identifier Code of the customer’s bank.
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

    - `payment_method_details.ideal.generated_sepa_debit` (string, nullable)
      The ID of the SEPA Direct Debit PaymentMethod which was generated by this Charge.

    - `payment_method_details.ideal.generated_sepa_debit_mandate` (string, nullable)
      The mandate for the SEPA Direct Debit PaymentMethod which was generated by this Charge.

    - `payment_method_details.ideal.iban_last4` (string, nullable)
      Last four characters of the IBAN.

    - `payment_method_details.ideal.transaction_id` (string, nullable)
      Unique transaction ID generated by iDEAL.

    - `payment_method_details.ideal.verified_name` (string, nullable)
      Owner’s verified full name. Values are verified or provided by iDEAL directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

  - `payment_method_details.interac_present` (object, nullable)
    If this is a `interac_present` payment, this hash contains a snapshot of the transaction specific details of the `interac_present` payment method.

    - `payment_method_details.interac_present.brand` (string, nullable)
      Card brand. Can be `interac`, `mastercard` or `visa`.

    - `payment_method_details.interac_present.cardholder_name` (string, nullable)
      The cardholder name as read from the card, in [ISO 7813](https://en.wikipedia.org/wiki/ISO/IEC_7813) format. May include alphanumeric characters, special characters and first/last name separator (`/`). In some cases, the cardholder name may not be available depending on how the issuer has configured the card. Cardholder name is typically not available on swipe or contactless payments, such as those made with Apple Pay and Google Pay.

    - `payment_method_details.interac_present.country` (string, nullable)
      Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you’ve collected.

    - `payment_method_details.interac_present.description` (string, nullable)
      A high-level description of the type of cards issued in this range.

    - `payment_method_details.interac_present.emv_auth_data` (string, nullable)
      Authorization response cryptogram.

    - `payment_method_details.interac_present.exp_month` (integer)
      Two-digit number representing the card’s expiration month.

    - `payment_method_details.interac_present.exp_year` (integer)
      Four-digit number representing the card’s expiration year.

    - `payment_method_details.interac_present.fingerprint` (string, nullable)
      Uniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.

      *As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card—one for India and one for the rest of the world.*

    - `payment_method_details.interac_present.funding` (string, nullable)
      Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.

    - `payment_method_details.interac_present.generated_card` (string, nullable)
      ID of a card PaymentMethod generated from the card_present PaymentMethod that may be attached to a Customer for future transactions. Only present if it was possible to generate a card PaymentMethod.

    - `payment_method_details.interac_present.issuer` (string, nullable)
      The name of the card’s issuing bank.

    - `payment_method_details.interac_present.last4` (string, nullable)
      The last four digits of the card.

    - `payment_method_details.interac_present.network` (string, nullable)
      Identifies which network this charge was processed on. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `interac`, `jcb`, `link`, `mastercard`, `unionpay`, `visa`, or `unknown`.

    - `payment_method_details.interac_present.network_transaction_id` (string, nullable)
      This is used by the financial networks to identify a transaction. Visa calls this the Transaction ID, Mastercard calls this the Trace ID, and American Express calls this the Acquirer Reference Data. This value will be present if it is returned by the financial network in the authorization response, and null otherwise.

    - `payment_method_details.interac_present.preferred_locales` (array of strings, nullable)
      The languages that the issuing bank recommends using for localizing any customer-facing text, as read from the card. Referenced from EMV tag 5F2D, data encoded on the card’s chip.

    - `payment_method_details.interac_present.read_method` (enum, nullable)
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

    - `payment_method_details.interac_present.receipt` (object, nullable)
      A collection of fields required to be displayed on receipts. Only required for EMV transactions.

      - `payment_method_details.interac_present.receipt.account_type` (enum, nullable)
        The type of account being debited or credited
Possible enum values:
        - `checking`
          A checking account, as selected on the reader

        - `savings`
          A savings account, as selected on the reader

        - `unknown`
          An unknown account

      - `payment_method_details.interac_present.receipt.application_cryptogram` (string, nullable)
        The Application Cryptogram, a unique value generated by the card to authenticate the transaction with issuers.

      - `payment_method_details.interac_present.receipt.application_preferred_name` (string, nullable)
        The Application Identifier (AID) on the card used to determine which networks are eligible to process the transaction. Referenced from EMV tag 9F12, data encoded on the card’s chip.

      - `payment_method_details.interac_present.receipt.authorization_code` (string, nullable)
        Identifier for this transaction.

      - `payment_method_details.interac_present.receipt.authorization_response_code` (string, nullable)
        EMV tag 8A. A code returned by the card issuer.

      - `payment_method_details.interac_present.receipt.cardholder_verification_method` (string, nullable)
        Describes the method used by the cardholder to verify ownership of the card. One of the following: `approval`, `failure`, `none`, `offline_pin`, `offline_pin_and_signature`, `online_pin`, or `signature`.

      - `payment_method_details.interac_present.receipt.dedicated_file_name` (string, nullable)
        Similar to the application_preferred_name, identifying the applications (AIDs) available on the card. Referenced from EMV tag 84.

      - `payment_method_details.interac_present.receipt.terminal_verification_results` (string, nullable)
        A 5-byte string that records the checks and validations that occur between the card and the terminal. These checks determine how the terminal processes the transaction and what risk tolerance is acceptable. Referenced from EMV Tag 95.

      - `payment_method_details.interac_present.receipt.transaction_status_information` (string, nullable)
        An indication of which steps were completed during the card read process. Referenced from EMV Tag 9B.

  - `payment_method_details.kakao_pay` (object, nullable)
    If this is a `kakao_pay` payment, this hash contains a snapshot of the transaction specific details of the `kakao_pay` payment method.

    - `payment_method_details.kakao_pay.buyer_id` (string, nullable)
      A unique identifier for the buyer as determined by the local payment processor.

    - `payment_method_details.kakao_pay.transaction_id` (string, nullable)
      The Kakao Pay transaction ID associated with this payment.

  - `payment_method_details.klarna` (object, nullable)
    If this is a `klarna` payment, this hash contains a snapshot of the transaction specific details of the `klarna` payment method.

    - `payment_method_details.klarna.payer_details` (object, nullable)
      The payer details for this transaction.

      - `payment_method_details.klarna.payer_details.address` (object, nullable)
        The payer’s address

        - `payment_method_details.klarna.payer_details.address.country` (string, nullable)
          The payer address country

    - `payment_method_details.klarna.payment_method_category` (string, nullable)
      The Klarna payment method used for this transaction. Can be one of `pay_later`, `pay_now`, `pay_with_financing`, or `pay_in_installments`

    - `payment_method_details.klarna.preferred_locale` (string, nullable)
      Preferred language of the Klarna authorization page that the customer is redirected to. Can be one of `de-AT`, `en-AT`, `nl-BE`, `fr-BE`, `en-BE`, `de-DE`, `en-DE`, `da-DK`, `en-DK`, `es-ES`, `en-ES`, `fi-FI`, `sv-FI`, `en-FI`, `en-GB`, `en-IE`, `it-IT`, `en-IT`, `nl-NL`, `en-NL`, `nb-NO`, `en-NO`, `sv-SE`, `en-SE`, `en-US`, `es-US`, `fr-FR`, `en-FR`, `cs-CZ`, `en-CZ`, `ro-RO`, `en-RO`, `el-GR`, `en-GR`, `en-AU`, `en-NZ`, `en-CA`, `fr-CA`, `pl-PL`, `en-PL`, `pt-PT`, `en-PT`, `de-CH`, `fr-CH`, `it-CH`, or `en-CH`

  - `payment_method_details.konbini` (object, nullable)
    If this is a `konbini` payment, this hash contains a snapshot of the transaction specific details of the `konbini` payment method.

    - `payment_method_details.konbini.store` (object, nullable)
      If the payment succeeded, this contains the details of the convenience store where the payment was completed.

      - `payment_method_details.konbini.store.chain` (enum, nullable)
        The name of the convenience store chain where the payment was completed.
Possible enum values:
        - `familymart`
          FamilyMart convenience store chain.

        - `lawson`
          Lawson convenience store chain.

        - `ministop`
          Ministop convenience store chain.

        - `seicomart`
          Seicomart convenience store chain.

  - `payment_method_details.kr_card` (object, nullable)
    If this is a `kr_card` payment, this hash contains a snapshot of the transaction specific details of the `kr_card` payment method.

    - `payment_method_details.kr_card.brand` (enum, nullable)
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

    - `payment_method_details.kr_card.buyer_id` (string, nullable)
      A unique identifier for the buyer as determined by the local payment processor.

    - `payment_method_details.kr_card.last4` (string, nullable)
      The last four digits of the card. This may not be present for American Express cards.

      The maximum length is 4 characters.

    - `payment_method_details.kr_card.transaction_id` (string, nullable)
      The Korean Card transaction ID associated with this payment.

  - `payment_method_details.link` (object, nullable)
    If this is a `link` payment, this hash contains a snapshot of the transaction specific details of the `link` payment method.

    - `payment_method_details.link.country` (string, nullable)
      Two-letter ISO code representing the funding source country beneath the Link payment. You could use this attribute to get a sense of international fees.

  - `payment_method_details.mb_way` (object, nullable)
    If this is a `mb_way` payment, this hash contains a snapshot of the transaction specific details of the `mb_way` payment method.

  - `payment_method_details.mobilepay` (object, nullable)
    If this is a `mobilepay` payment, this hash contains a snapshot of the transaction specific details of the `mobilepay` payment method.

    - `payment_method_details.mobilepay.card` (object, nullable)
      Internal card details

      - `payment_method_details.mobilepay.card.brand` (string, nullable)
        Brand of the card used in the transaction

      - `payment_method_details.mobilepay.card.country` (string, nullable)
        Two-letter ISO code representing the country of the card

      - `payment_method_details.mobilepay.card.exp_month` (integer, nullable)
        Two digit number representing the card’s expiration month

      - `payment_method_details.mobilepay.card.exp_year` (integer, nullable)
        Two digit number representing the card’s expiration year

      - `payment_method_details.mobilepay.card.last4` (string, nullable)
        The last 4 digits of the card

  - `payment_method_details.multibanco` (object, nullable)
    If this is a `multibanco` payment, this hash contains a snapshot of the transaction specific details of the `multibanco` payment method.

    - `payment_method_details.multibanco.entity` (string, nullable)
      Entity number associated with this Multibanco payment.

    - `payment_method_details.multibanco.reference` (string, nullable)
      Reference number associated with this Multibanco payment.

  - `payment_method_details.naver_pay` (object, nullable)
    If this is a `naver_pay` payment, this hash contains a snapshot of the transaction specific details of the `naver_pay` payment method.

    - `payment_method_details.naver_pay.buyer_id` (string, nullable)
      A unique identifier for the buyer as determined by the local payment processor.

    - `payment_method_details.naver_pay.transaction_id` (string, nullable)
      The Naver Pay transaction ID associated with this payment.

  - `payment_method_details.nz_bank_account` (object, nullable)
    If this is a `nz_bank_account` payment, this hash contains a snapshot of the transaction specific details of the `nz_bank_account` payment method.

    - `payment_method_details.nz_bank_account.account_holder_name` (string, nullable)
      The name on the bank account. Only present if the account holder name is different from the name of the authorized signatory collected in the PaymentMethod’s billing details.

    - `payment_method_details.nz_bank_account.bank_code` (string)
      The numeric code for the bank account’s bank.

    - `payment_method_details.nz_bank_account.bank_name` (string)
      The name of the bank.

    - `payment_method_details.nz_bank_account.branch_code` (string)
      The numeric code for the bank account’s bank branch.

    - `payment_method_details.nz_bank_account.expected_debit_date` (string, nullable)
      Estimated date to debit the customer’s bank account. A date string in YYYY-MM-DD format.

    - `payment_method_details.nz_bank_account.last4` (string)
      Last four digits of the bank account number.

    - `payment_method_details.nz_bank_account.suffix` (string, nullable)
      The suffix of the bank account number.

  - `payment_method_details.oxxo` (object, nullable)
    If this is a `oxxo` payment, this hash contains a snapshot of the transaction specific details of the `oxxo` payment method.

    - `payment_method_details.oxxo.number` (string, nullable)
      OXXO reference number

  - `payment_method_details.p24` (object, nullable)
    If this is a `p24` payment, this hash contains a snapshot of the transaction specific details of the `p24` payment method.

    - `payment_method_details.p24.bank` (enum, nullable)
      The customer’s bank. Can be one of `ing`, `citi_handlowy`, `tmobile_usbugi_bankowe`, `plus_bank`, `etransfer_pocztowy24`, `banki_spbdzielcze`, `bank_nowy_bfg_sa`, `getin_bank`, `velobank`, `blik`, `noble_pay`, `ideabank`, `envelobank`, `santander_przelew24`, `nest_przelew`, `mbank_mtransfer`, `inteligo`, `pbac_z_ipko`, `bnp_paribas`, `credit_agricole`, `toyota_bank`, `bank_pekao_sa`, `volkswagen_bank`, `bank_millennium`, `alior_bank`, or `boz`.
Possible enum values:
      - `alior_bank`
      - `bank_millennium`
      - `bank_nowy_bfg_sa`
      - `bank_pekao_sa`
      - `banki_spbdzielcze`
      - `blik`
      - `bnp_paribas`
      - `boz`
      - `citi_handlowy`
      - `credit_agricole`
      - `envelobank`
      - `etransfer_pocztowy24`
      - `getin_bank`
      - `ideabank`
      - `ing`
      - `inteligo`
      - `mbank_mtransfer`
      - `nest_przelew`
      - `noble_pay`
      - `pbac_z_ipko`
      - `plus_bank`
      - `santander_przelew24`
      - `tmobile_usbugi_bankowe`
      - `toyota_bank`
      - `velobank`
      - `volkswagen_bank`

    - `payment_method_details.p24.reference` (string, nullable)
      Unique reference for this Przelewy24 payment.

    - `payment_method_details.p24.verified_name` (string, nullable)
      Owner’s verified full name. Values are verified or provided by Przelewy24 directly (if supported) at the time of authorization or settlement. They cannot be set or mutated. Przelewy24 rarely provides this information so the attribute is usually empty.

  - `payment_method_details.pay_by_bank` (object, nullable)
    If this is a `pay_by_bank` payment, this hash contains a snapshot of the transaction specific details of the `pay_by_bank` payment method.

  - `payment_method_details.payco` (object, nullable)
    If this is a `payco` payment, this hash contains a snapshot of the transaction specific details of the `payco` payment method.

    - `payment_method_details.payco.buyer_id` (string, nullable)
      A unique identifier for the buyer as determined by the local payment processor.

    - `payment_method_details.payco.transaction_id` (string, nullable)
      The Payco transaction ID associated with this payment.

  - `payment_method_details.payment_method` (string, nullable)
    ID of the Stripe PaymentMethod used to make this payment.

  - `payment_method_details.paynow` (object, nullable)
    If this is a `paynow` payment, this hash contains a snapshot of the transaction specific details of the `paynow` payment method.

    - `payment_method_details.paynow.location` (string, nullable)
      ID of the [location](https://docs.stripe.com/docs/api/terminal/locations.md) that this transaction’s reader is assigned to.

    - `payment_method_details.paynow.reader` (string, nullable)
      ID of the [reader](https://docs.stripe.com/docs/api/terminal/readers.md) this transaction was made on.

    - `payment_method_details.paynow.reference` (string, nullable)
      Reference number associated with this PayNow payment

  - `payment_method_details.paypal` (object, nullable)
    If this is a `paypal` payment, this hash contains a snapshot of the transaction specific details of the `paypal` payment method.

    - `payment_method_details.paypal.country` (string, nullable)
      Two-letter ISO code representing the buyer’s country. Values are provided by PayPal directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

    - `payment_method_details.paypal.payer_email` (string, nullable)
      Owner’s email. Values are provided by PayPal directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

    - `payment_method_details.paypal.payer_id` (string, nullable)
      PayPal account PayerID. This identifier uniquely identifies the PayPal customer.

    - `payment_method_details.paypal.payer_name` (string, nullable)
      Owner’s full name. Values provided by PayPal directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

    - `payment_method_details.paypal.seller_protection` (object, nullable)
      The level of protection offered as defined by PayPal Seller Protection for Merchants, for this transaction.

      - `payment_method_details.paypal.seller_protection.dispute_categories` (array of enums, nullable)
        An array of conditions that are covered for the transaction, if applicable.
Possible enum values:
        - `fraudulent`
          The payer did not authorize the payment.

        - `product_not_received`
          The payer paid for an item that they did not receive.

      - `payment_method_details.paypal.seller_protection.status` (enum)
        Indicates whether the transaction is eligible for PayPal’s seller protection.
Possible enum values:
        - `eligible`
          Your balance remains intact if the customer claims that they did not receive an item or the account holder claims that they did not authorize the payment.

        - `not_eligible`
          This transaction is not eligible for seller protection.

        - `partially_eligible`
          Your balance remains intact if the customer claims that they did not receive an item.

    - `payment_method_details.paypal.transaction_id` (string, nullable)
      A unique ID generated by PayPal for this transaction.

  - `payment_method_details.paypay` (object, nullable)
    If this is a `paypay` payment, this hash contains a snapshot of the transaction specific details of the `paypay` payment method.

  - `payment_method_details.payto` (object, nullable)
    If this is a `payto` payment, this hash contains a snapshot of the transaction specific details of the `payto` payment method.

    - `payment_method_details.payto.bsb_number` (string, nullable)
      Bank-State-Branch number of the bank account.

    - `payment_method_details.payto.last4` (string, nullable)
      Last four digits of the bank account number.

    - `payment_method_details.payto.mandate` (string, nullable)
      ID of the mandate used to make this payment.

    - `payment_method_details.payto.pay_id` (string, nullable)
      The PayID alias for the bank account.

  - `payment_method_details.pix` (object, nullable)
    If this is a `pix` payment, this hash contains a snapshot of the transaction specific details of the `pix` payment method.

    - `payment_method_details.pix.bank_transaction_id` (string, nullable)
      Unique transaction id generated by BCB

  - `payment_method_details.promptpay` (object, nullable)
    If this is a `promptpay` payment, this hash contains a snapshot of the transaction specific details of the `promptpay` payment method.

    - `payment_method_details.promptpay.reference` (string, nullable)
      Bill reference generated by PromptPay

  - `payment_method_details.revolut_pay` (object, nullable)
    If this is a `revolut_pay` payment, this hash contains a snapshot of the transaction specific details of the `revolut_pay` payment method.

    - `payment_method_details.revolut_pay.funding` (object, nullable)
      the funding details of the underlying payment method.

      - `payment_method_details.revolut_pay.funding.card` (object, nullable)
        the funding details of the passthrough card.

        - `payment_method_details.revolut_pay.funding.card.brand` (string, nullable)
          Card brand. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `jcb`, `link`, `mastercard`, `unionpay`, `visa` or `unknown`.

        - `payment_method_details.revolut_pay.funding.card.country` (string, nullable)
          Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you’ve collected.

        - `payment_method_details.revolut_pay.funding.card.exp_month` (integer, nullable)
          Two-digit number representing the card’s expiration month.

        - `payment_method_details.revolut_pay.funding.card.exp_year` (integer, nullable)
          Four-digit number representing the card’s expiration year.

        - `payment_method_details.revolut_pay.funding.card.funding` (string, nullable)
          Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.

        - `payment_method_details.revolut_pay.funding.card.last4` (string, nullable)
          The last four digits of the card.

      - `payment_method_details.revolut_pay.funding.type` (enum, nullable)
        funding type of the underlying payment method.

    - `payment_method_details.revolut_pay.transaction_id` (string, nullable)
      The Revolut Pay transaction ID associated with this payment.

  - `payment_method_details.samsung_pay` (object, nullable)
    If this is a `samsung_pay` payment, this hash contains a snapshot of the transaction specific details of the `samsung_pay` payment method.

    - `payment_method_details.samsung_pay.buyer_id` (string, nullable)
      A unique identifier for the buyer as determined by the local payment processor.

    - `payment_method_details.samsung_pay.transaction_id` (string, nullable)
      The Samsung Pay transaction ID associated with this payment.

  - `payment_method_details.satispay` (object, nullable)
    If this is a `satispay` payment, this hash contains a snapshot of the transaction specific details of the `satispay` payment method.

    - `payment_method_details.satispay.transaction_id` (string, nullable)
      The Satispay transaction ID associated with this payment.

  - `payment_method_details.sepa_debit` (object, nullable)
    If this is a `sepa_debit` payment, this hash contains a snapshot of the transaction specific details of the `sepa_debit` payment method.

    - `payment_method_details.sepa_debit.bank_code` (string, nullable)
      Bank code of bank associated with the bank account.

    - `payment_method_details.sepa_debit.branch_code` (string, nullable)
      Branch code of bank associated with the bank account.

    - `payment_method_details.sepa_debit.country` (string, nullable)
      Two-letter ISO code representing the country the bank account is located in.

    - `payment_method_details.sepa_debit.expected_debit_date` (string, nullable)
      Estimated date to debit the customer’s bank account. A date string in YYYY-MM-DD format.

    - `payment_method_details.sepa_debit.fingerprint` (string, nullable)
      Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

    - `payment_method_details.sepa_debit.last4` (string, nullable)
      Last four characters of the IBAN.

    - `payment_method_details.sepa_debit.mandate` (string, nullable)
      Find the ID of the mandate used for this payment under the [payment_method_details.sepa_debit.mandate](https://docs.stripe.com/docs/api/charges/object.md#charge_object-payment_method_details-sepa_debit-mandate) property on the Charge. Use this mandate ID to [retrieve the Mandate](https://docs.stripe.com/docs/api/mandates/retrieve.md).

  - `payment_method_details.sofort` (object, nullable)
    If this is a `sofort` payment, this hash contains a snapshot of the transaction specific details of the `sofort` payment method.

    - `payment_method_details.sofort.bank_code` (string, nullable)
      Bank code of bank associated with the bank account.

    - `payment_method_details.sofort.bank_name` (string, nullable)
      Name of the bank associated with the bank account.

    - `payment_method_details.sofort.bic` (string, nullable)
      Bank Identifier Code of the bank associated with the bank account.

    - `payment_method_details.sofort.country` (string, nullable)
      Two-letter ISO code representing the country the bank account is located in.

    - `payment_method_details.sofort.generated_sepa_debit` (string, nullable)
      The ID of the SEPA Direct Debit PaymentMethod which was generated by this Charge.

    - `payment_method_details.sofort.generated_sepa_debit_mandate` (string, nullable)
      The mandate for the SEPA Direct Debit PaymentMethod which was generated by this Charge.

    - `payment_method_details.sofort.iban_last4` (string, nullable)
      Last four characters of the IBAN.

    - `payment_method_details.sofort.preferred_language` (enum, nullable)
      Preferred language of the SOFORT authorization page that the customer is redirected to. Can be one of `de`, `en`, `es`, `fr`, `it`, `nl`, or `pl`
Possible enum values:
      - `de`
      - `en`
      - `es`
      - `fr`
      - `it`
      - `nl`
      - `pl`

    - `payment_method_details.sofort.verified_name` (string, nullable)
      Owner’s verified full name. Values are verified or provided by SOFORT directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

  - `payment_method_details.stripe_account` (object, nullable)
    If this is a `stripe_account` payment, this hash contains a snapshot of the transaction specific details of the `stripe_account` payment method.

  - `payment_method_details.swish` (object, nullable)
    If this is a `swish` payment, this hash contains a snapshot of the transaction specific details of the `swish` payment method.

    - `payment_method_details.swish.fingerprint` (string, nullable)
      Uniquely identifies the payer’s Swish account. You can use this attribute to check whether two Swish transactions were paid for by the same payer

    - `payment_method_details.swish.payment_reference` (string, nullable)
      Payer bank reference number for the payment

    - `payment_method_details.swish.verified_phone_last4` (string, nullable)
      The last four digits of the Swish account phone number

  - `payment_method_details.twint` (object, nullable)
    If this is a `twint` payment, this hash contains a snapshot of the transaction specific details of the `twint` payment method.

  - `payment_method_details.type` (string)
    The type of transaction-specific details of the payment method used in the payment. See [PaymentMethod.type](https://docs.stripe.com/docs/api/payment_methods/object.md#payment_method_object-type) for the full list of possible types. An additional hash is included on `payment_method_details` with a name matching this value. It contains information specific to the payment method.

  - `payment_method_details.us_bank_account` (object, nullable)
    If this is a `us_bank_account` payment, this hash contains a snapshot of the transaction specific details of the `us_bank_account` payment method.

    - `payment_method_details.us_bank_account.account_holder_type` (enum, nullable)
      The type of entity that holds the account. This can be either ‘individual’ or ‘company’.
Possible enum values:
      - `company`
        Account belongs to a company

      - `individual`
        Account belongs to an individual

    - `payment_method_details.us_bank_account.account_type` (enum, nullable)
      The type of the bank account. This can be either ‘checking’ or ‘savings’.
Possible enum values:
      - `checking`
        Bank account type is checking

      - `savings`
        Bank account type is savings

    - `payment_method_details.us_bank_account.bank_name` (string, nullable)
      Name of the bank associated with the bank account.

    - `payment_method_details.us_bank_account.expected_debit_date` (string, nullable)
      Estimated date to debit the customer’s bank account. A date string in YYYY-MM-DD format.

    - `payment_method_details.us_bank_account.fingerprint` (string, nullable)
      Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

    - `payment_method_details.us_bank_account.last4` (string, nullable)
      Last four digits of the bank account number.

    - `payment_method_details.us_bank_account.mandate` (string, nullable)
      ID of the mandate used to make this payment.

    - `payment_method_details.us_bank_account.payment_reference` (string, nullable)
      The ACH payment reference for this transaction.

    - `payment_method_details.us_bank_account.routing_number` (string, nullable)
      The routing number for the bank account.

  - `payment_method_details.wechat` (object, nullable)
    If this is a `wechat` payment, this hash contains a snapshot of the transaction specific details of the `wechat` payment method.

  - `payment_method_details.wechat_pay` (object, nullable)
    If this is a `wechat_pay` payment, this hash contains a snapshot of the transaction specific details of the `wechat_pay` payment method.

    - `payment_method_details.wechat_pay.fingerprint` (string, nullable)
      Uniquely identifies this particular WeChat Pay account. You can use this attribute to check whether two WeChat accounts are the same.

    - `payment_method_details.wechat_pay.location` (string, nullable)
      ID of the [location](https://docs.stripe.com/docs/api/terminal/locations.md) that this transaction’s reader is assigned to.

    - `payment_method_details.wechat_pay.reader` (string, nullable)
      ID of the [reader](https://docs.stripe.com/docs/api/terminal/readers.md) this transaction was made on.

    - `payment_method_details.wechat_pay.transaction_id` (string, nullable)
      Transaction ID of this particular WeChat Pay transaction.

  - `payment_method_details.zip` (object, nullable)
    If this is a `zip` payment, this hash contains a snapshot of the transaction specific details of the `zip` payment method.

- `payment_record` (string, nullable)
  ID of the Payment Record this Payment Attempt Record belongs to.

- `processor_details` (object)
  Processor information for this payment.

  - `processor_details.custom` (object, nullable)
    Information about the custom processor used to make this payment.

    - `processor_details.custom.payment_reference` (string, nullable)
      An opaque string for manual reconciliation of this payment, for example a check number or a payment processor ID.

  - `processor_details.type` (enum)
    The processor used for this payment attempt.
Possible enum values:
    - `custom`
      A custom processor.

- `reported_by` (enum)
  Indicates who reported the payment.
Possible enum values:
  - `self`
    The payment was reported by self.

  - `stripe`
    The payment was reported by Stripe.

- `shipping_details` (object, nullable)
  Shipping information for this payment.

  - `shipping_details.address` (object)
    The physical shipping address.

    - `shipping_details.address.city` (string, nullable)
      City, district, suburb, town, or village.

    - `shipping_details.address.country` (string, nullable)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `shipping_details.address.line1` (string, nullable)
      Address line 1, such as the street, PO Box, or company name.

    - `shipping_details.address.line2` (string, nullable)
      Address line 2, such as the apartment, suite, unit, or building.

    - `shipping_details.address.postal_code` (string, nullable)
      ZIP or postal code.

    - `shipping_details.address.state` (string, nullable)
      State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

  - `shipping_details.name` (string, nullable)
    The shipping recipient’s name.

  - `shipping_details.phone` (string, nullable)
    The shipping recipient’s phone number.

### The Payment Attempt Record object

```json
{
  "id": "par_4sdDKj23235s",
  "object": "payment_attempt_record",
  "amount_authorized": {
    "currency": "usd",
    "value": 1000
  },
  "amount_canceled": {
    "currency": "usd",
    "value": 0
  },
  "amount_failed": {
    "currency": "usd",
    "value": 0
  },
  "amount_guaranteed": {
    "currency": "usd",
    "value": 0
  },
  "amount_refunded": {
    "currency": "usd",
    "value": 0
  },
  "amount_requested": {
    "currency": "usd",
    "value": 1000
  },
  "created": 1730211363,
  "customer_details": null,
  "customer_presence": "on_session",
  "description": "computer software",
  "livemode": true,
  "metadata": {},
  "payment_method_details": {
    "billing_details": null,
    "custom": {
      "display_name": "newpay",
      "type": "cpmt_125kjj3hn3sdf"
    },
    "payment_method": "pm_5j23kjksibjlks",
    "type": "custom"
  },
  "payment_record": "pr_5RV730PrHyAEi",
  "processor_details": {
    "type": "custom",
    "custom": {
      "payment_reference": "npp2358872734k"
    }
  },
  "shipping_details": null
}
```