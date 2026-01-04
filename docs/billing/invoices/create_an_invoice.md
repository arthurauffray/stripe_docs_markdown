# Create an invoice

This endpoint creates a draft invoice for a given customer. The invoice remains a draft until you [finalize](https://docs.stripe.com/api/invoices/create.md#finalize_invoice) the invoice, which allows you to [pay](https://docs.stripe.com/api/invoices/create.md#pay_invoice) or [send](https://docs.stripe.com/api/invoices/create.md#send_invoice) the invoice to your customers.

## Returns

Returns the invoice object. Raises [an error](https://docs.stripe.com/api/invoices/create.md#errors) if the customer ID provided is invalid.

## Parameters

- `account_tax_ids` (array of strings, optional)
  The account tax IDs associated with the invoice. Only editable when the invoice is a draft.

- `application_fee_amount` (integer, optional)
  A fee in cents that will be applied to the invoice and transferred to the application owner’s Stripe account. The request must be made with an OAuth key or the Stripe-Account header in order to take an application fee. For more information, see the application fees [documentation](https://docs.stripe.com/docs/billing/invoices/connect.md#collecting-fees).

- `auto_advance` (boolean, optional)
  Controls whether Stripe performs [automatic collection](https://docs.stripe.com/docs/invoicing/integration/automatic-advancement-collection.md) of the invoice. If `false`, the invoice’s state doesn’t automatically advance without an explicit action. Defaults to false.

- `automatic_tax` (object, optional)
  Settings for automatic tax lookup for this invoice.

  - `automatic_tax.enabled` (boolean, required)
    Whether Stripe automatically computes tax on this invoice. Note that incompatible invoice items (invoice items with manually specified [tax rates](https://docs.stripe.com/docs/api/tax_rates.md), negative amounts, or `tax_behavior=unspecified`) cannot be added to automatic tax invoices.

  - `automatic_tax.liability` (object, optional)
    The account that’s liable for tax. If set, the business address and tax registrations required to perform the tax calculation are loaded from this account. The tax transaction is returned in the report of the connected account.

    - `automatic_tax.liability.type` (enum, required)
      Type of the account referenced in the request.
Possible enum values:
      - `account`
        Indicates that the account being referenced is a connected account which is different from the account making the API request but related to it.

      - `self`
        Indicates that the account being referenced is the account making the API request.

    - `automatic_tax.liability.account` (string, required only if type is account)
      The connected account being referenced when `type` is `account`.

- `automatically_finalizes_at` (timestamp, optional)
  The time when this invoice should be scheduled to finalize (up to 5 years in the future). The invoice is finalized at this time if it’s still in draft state.

- `collection_method` (enum, optional)
  Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this invoice using the default source attached to the customer. When sending an invoice, Stripe will email this invoice to the customer with payment instructions. Defaults to `charge_automatically`.
Possible enum values:
  - `charge_automatically`
  - `send_invoice`

- `currency` (enum, optional)
  The currency to create this invoice in. Defaults to that of `customer` if not specified.

- `custom_fields` (array of objects, optional)
  A list of up to 4 custom fields to be displayed on the invoice.

  - `custom_fields.name` (string, required)
    The name of the custom field. This may be up to 40 characters.

    The maximum length is 40 characters.

  - `custom_fields.value` (string, required)
    The value of the custom field. This may be up to 140 characters.

    The maximum length is 140 characters.

- `customer` (string, required unless from_invoice is provided)
  The ID of the customer to bill.

- `customer_account` (string, optional)
  The ID of the account to bill.

- `days_until_due` (integer, optional)
  The number of days from when the invoice is created until it is due. Valid only for invoices where `collection_method=send_invoice`.

- `default_payment_method` (string, optional)
  ID of the default payment method for the invoice. It must belong to the customer associated with the invoice. If not set, defaults to the subscription’s default payment method, if any, or to the default payment method in the customer’s invoice settings.

- `default_source` (string, optional)
  ID of the default payment source for the invoice. It must belong to the customer associated with the invoice and be in a chargeable state. If not set, defaults to the subscription’s default source, if any, or to the customer’s default source.

- `default_tax_rates` (array of strings, optional)
  The tax rates that will apply to any line item that does not have `tax_rates` set.

- `description` (string, optional)
  An arbitrary string attached to the object. Often useful for displaying to users. Referenced as ‘memo’ in the Dashboard.

- `discounts` (array of objects, optional)
  The coupons and promotion codes to redeem into discounts for the invoice. If not specified, inherits the discount from the invoice’s customer. Pass an empty string to avoid inheriting any discounts.

  - `discounts.coupon` (string, optional)
    ID of the coupon to create a new discount for.

  - `discounts.discount` (string, optional)
    ID of an existing discount on the object (or one of its ancestors) to reuse.

  - `discounts.promotion_code` (string, optional)
    ID of the promotion code to create a new discount for.

- `due_date` (timestamp, optional)
  The date on which payment for this invoice is due. Valid only for invoices where `collection_method=send_invoice`.

- `effective_at` (timestamp, optional)
  The date when this invoice is in effect. Same as `finalized_at` unless overwritten. When defined, this value replaces the system-generated ‘Date of issue’ printed on the invoice PDF and receipt.

- `footer` (string, optional)
  Footer to be displayed on the invoice.

- `from_invoice` (object, required unless customer is provided)
  Revise an existing invoice. The new invoice will be created in `status=draft`. See the [revision documentation](https://docs.stripe.com/docs/invoicing/invoice-revisions.md) for more details.

  - `from_invoice.action` (string, required)
    The relation between the new invoice and the original invoice. Currently, only ‘revision’ is permitted

  - `from_invoice.invoice` (string, required)
    The `id` of the invoice that will be cloned.

- `issuer` (object, optional)
  The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.

  - `issuer.type` (enum, required)
    Type of the account referenced in the request.
Possible enum values:
    - `account`
      Indicates that the account being referenced is a connected account which is different from the account making the API request but related to it.

    - `self`
      Indicates that the account being referenced is the account making the API request.

  - `issuer.account` (string, required only if type is account)
    The connected account being referenced when `type` is `account`.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `number` (string, optional)
  Set the number for this invoice. If no number is present then a number will be assigned automatically when the invoice is finalized. In many markets, regulations require invoices to be unique, sequential and / or gapless. You are responsible for ensuring this is true across all your different invoicing systems in the event that you edit the invoice number using our API. If you use only Stripe for your invoices and do not change invoice numbers, Stripe handles this aspect of compliance for you automatically.

  The maximum length is 26 characters.

- `on_behalf_of` (string, optional)
  The account (if any) for which the funds of the invoice payment are intended. If set, the invoice will be presented with the branding and support information of the specified account. See the [Invoices with Connect](https://docs.stripe.com/docs/billing/invoices/connect.md) documentation for details.

- `payment_settings` (object, optional)
  Configuration settings for the PaymentIntent that is generated when the invoice is finalized.

  - `payment_settings.default_mandate` (string, optional)
    ID of the mandate to be used for this invoice. It must correspond to the payment method used to pay the invoice, including the invoice’s default_payment_method or default_source, if set.

  - `payment_settings.payment_method_options` (object, optional)
    Payment-method-specific configuration to provide to the invoice’s PaymentIntent.

    - `payment_settings.payment_method_options.acss_debit` (object, optional)
      If paying by `acss_debit`, this sub-hash contains details about the Canadian pre-authorized debit payment method options to pass to the invoice’s PaymentIntent.

      - `payment_settings.payment_method_options.acss_debit.mandate_options` (object, optional)
        Additional fields for Mandate creation

        - `payment_settings.payment_method_options.acss_debit.mandate_options.transaction_type` (enum, optional)
          Transaction type of the mandate.
Possible enum values:
          - `business`
            Transactions are made for business reasons

          - `personal`
            Transactions are made for personal reasons

      - `payment_settings.payment_method_options.acss_debit.verification_method` (enum, optional)
        Verification method for the intent
Possible enum values:
        - `automatic`
          Instant verification with fallback to microdeposits.

        - `instant`
          Instant verification.

        - `microdeposits`
          Verification using microdeposits.

    - `payment_settings.payment_method_options.bancontact` (object, optional)
      If paying by `bancontact`, this sub-hash contains details about the Bancontact payment method options to pass to the invoice’s PaymentIntent.

      - `payment_settings.payment_method_options.bancontact.preferred_language` (enum, optional)
        Preferred language of the Bancontact authorization page that the customer is redirected to.
Possible enum values:
        - `de`
          German

        - `en`
          English

        - `fr`
          French

        - `nl`
          Dutch

    - `payment_settings.payment_method_options.card` (object, optional)
      If paying by `card`, this sub-hash contains details about the Card payment method options to pass to the invoice’s PaymentIntent.

      - `payment_settings.payment_method_options.card.installments` (object, optional)
        Installment configuration for payments attempted on this invoice.

        For more information, see the [installments integration guide](https://docs.stripe.com/docs/payments/installments.md).

        - `payment_settings.payment_method_options.card.installments.enabled` (boolean, optional)
          Setting to true enables installments for this invoice. Setting to false will prevent any selected plan from applying to a payment.

        - `payment_settings.payment_method_options.card.installments.plan` (object, optional)
          The selected installment plan to use for this invoice.

          - `payment_settings.payment_method_options.card.installments.plan.type` (enum, required)
            Type of installment plan, one of `fixed_count`, `bonus`, or `revolving`.
Possible enum values:
            - `bonus`
              An installment plan used in Japan, where the customer defers payment to a later date that aligns with their salary bonus.

            - `fixed_count`
              An installment plan where the number of installment payments is fixed and known at the time of purchase.

            - `revolving`
              An installment plan used in Japan, where the customer pays a certain amount each month, and the remaining balance rolls over to the next month.

          - `payment_settings.payment_method_options.card.installments.plan.count` (integer, optional)
            For `fixed_count` installment plans, this is required. It represents the number of installment payments your customer will make to their credit card.

          - `payment_settings.payment_method_options.card.installments.plan.interval` (enum, optional)
            For `fixed_count` installment plans, this is required. It represents the interval between installment payments your customer will make to their credit card. One of `month`.
Possible enum values:
            - `month`

      - `payment_settings.payment_method_options.card.request_three_d_secure` (enum, optional)
        We strongly recommend that you rely on our SCA Engine to automatically prompt your customers for authentication based on risk level and [other requirements](https://docs.stripe.com/docs/strong-customer-authentication.md). However, if you wish to request 3D Secure based on logic from your own fraud engine, provide this option. Read our guide on [manually requesting 3D Secure](https://docs.stripe.com/docs/payments/3d-secure/authentication-flow.md#manual-three-ds) for more information on how this configuration interacts with Radar and our SCA Engine.
Possible enum values:
        - `any`
          Use `any` to manually request 3DS with a preference for a `frictionless` flow, increasing the likelihood of the authentication being completed without any additional input from the customer. 3DS will always be attempted if it is supported for the card, but Stripe can’t guarantee your preference because the issuer determines the ultimate authentication flow. To learn more about 3DS flows, read our [guide](https://stripe.com/guides/3d-secure-2#frictionless-authentication).

        - `automatic`
          (Default) Our SCA Engine automatically prompts your customers for authentication based on risk level and other requirements.

        - `challenge`
          Use `challenge` to request 3DS with a preference for a `challenge` flow, where the customer must respond to a prompt for active authentication. Stripe can’t guarantee your preference because the issuer determines the ultimate authentication flow. To learn more about 3DS flows, read our [guide](https://stripe.com/guides/3d-secure-2#frictionless-authentication).

    - `payment_settings.payment_method_options.customer_balance` (object, optional)
      If paying by `customer_balance`, this sub-hash contains details about the Bank transfer payment method options to pass to the invoice’s PaymentIntent.

      - `payment_settings.payment_method_options.customer_balance.bank_transfer` (object, optional)
        Configuration for the bank transfer funding type, if the `funding_type` is set to `bank_transfer`.

        - `payment_settings.payment_method_options.customer_balance.bank_transfer.eu_bank_transfer` (object, Required if type=eu_bank_transfer)
          Configuration for eu_bank_transfer funding type.

          - `payment_settings.payment_method_options.customer_balance.bank_transfer.eu_bank_transfer.country` (string, required)
            The desired country code of the bank account information. Permitted values include: `BE`, `DE`, `ES`, `FR`, `IE`, or `NL`.

        - `payment_settings.payment_method_options.customer_balance.bank_transfer.type` (enum, optional)
          The bank transfer type that can be used for funding. Permitted values include: `eu_bank_transfer`, `gb_bank_transfer`, `jp_bank_transfer`, `mx_bank_transfer`, or `us_bank_transfer`.

      - `payment_settings.payment_method_options.customer_balance.funding_type` (enum, optional)
        The funding method type to be used when there are not enough funds in the customer balance. Permitted values include: `bank_transfer`.

    - `payment_settings.payment_method_options.konbini` (object, optional)
      If paying by `konbini`, this sub-hash contains details about the Konbini payment method options to pass to the invoice’s PaymentIntent.

    - `payment_settings.payment_method_options.payto` (object, optional)
      If paying by `payto`, this sub-hash contains details about the PayTo payment method options to pass to the invoice’s PaymentIntent.

      - `payment_settings.payment_method_options.payto.mandate_options` (object, optional)
        Additional fields for Mandate creation.

        - `payment_settings.payment_method_options.payto.mandate_options.amount` (integer, optional)
          The maximum amount that can be collected in a single invoice. If you don’t specify a maximum, then there is no limit.

        - `payment_settings.payment_method_options.payto.mandate_options.purpose` (enum, optional)
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

    - `payment_settings.payment_method_options.sepa_debit` (object, optional)
      If paying by `sepa_debit`, this sub-hash contains details about the SEPA Direct Debit payment method options to pass to the invoice’s PaymentIntent.

    - `payment_settings.payment_method_options.us_bank_account` (object, optional)
      If paying by `us_bank_account`, this sub-hash contains details about the ACH direct debit payment method options to pass to the invoice’s PaymentIntent.

      - `payment_settings.payment_method_options.us_bank_account.financial_connections` (object, optional)
        Additional fields for Financial Connections Session creation

        - `payment_settings.payment_method_options.us_bank_account.financial_connections.filters` (object, optional)
          Provide filters for the linked accounts that the customer can select for the payment method.

          - `payment_settings.payment_method_options.us_bank_account.financial_connections.filters.account_subcategories` (array of enums, optional)
            The account subcategories to use to filter for selectable accounts. Valid subcategories are `checking` and `savings`.
Possible enum values:
            - `checking`
              Bank account subcategory is checking

            - `savings`
              Bank account subcategory is savings

        - `payment_settings.payment_method_options.us_bank_account.financial_connections.permissions` (array of strings, optional)
          The list of permissions to request. If this parameter is passed, the `payment_method` permission must be included. Valid permissions include: `balances`, `ownership`, `payment_method`, and `transactions`.

        - `payment_settings.payment_method_options.us_bank_account.financial_connections.prefetch` (array of enums, optional)
          List of data features that you would like to retrieve upon account creation.
Possible enum values:
          - `balances`
            Requests to prefetch balance data on accounts collected in this session.

          - `ownership`
            Requests to prefetch ownership data on accounts collected in this session.

          - `transactions`
            Requests to prefetch transaction data on accounts collected in this session.

      - `payment_settings.payment_method_options.us_bank_account.verification_method` (enum, optional)
        Verification method for the intent
Possible enum values:
        - `automatic`
          Instant verification with fallback to microdeposits.

        - `instant`
          Instant verification only.

        - `microdeposits`
          Verification using microdeposits. Cannot be used with Stripe Checkout, Hosted Invoices, or Payment Element.

  - `payment_settings.payment_method_types` (array of enums, optional)
    The list of payment method types (e.g. card) to provide to the invoice’s PaymentIntent. If not set, Stripe attempts to automatically determine the types to use by looking at the invoice’s default payment method, the subscription’s default payment method, the customer’s default payment method, and your [invoice template settings](https://dashboard.stripe.com/settings/billing/invoice).
Possible enum values:
    - `ach_debit`
      ACH

    - `acss_debit`
      Canadian pre-authorized debit

    - `affirm`
      Affirm

      If set, the Subscription `collection_method` must be `send_invoice`.

    - `amazon_pay`
      Amazon Pay

    - `au_becs_debit`
      BECS Direct Debit

    - `bacs_debit`
      Bacs Direct Debit

    - `bancontact`
      Bancontact

      If set, the Subscription `collection_method` must be `send_invoice`.

    - `boleto`
      Boleto

    - `card`
      Card

    - `cashapp`
      Cash App Pay

    - `crypto`
      Crypto

      If set, the Subscription `collection_method` must be `send_invoice`.

    - `custom`
      Custom

    - `customer_balance`
      Bank transfer

      If set, the Subscription `collection_method` must be `send_invoice`.

    - `eps`
      EPS

      If set, the Subscription `collection_method` must be `send_invoice`.

    - `fpx`
      FPX

      If set, the Subscription `collection_method` must be `send_invoice`.

    - `giropay`
      giropay

      If set, the Subscription `collection_method` must be `send_invoice`.

    - `grabpay`
      GrabPay

      If set, the Subscription `collection_method` must be `send_invoice`.

    - `ideal`
      iDEAL

      If set, the Subscription `collection_method` must be `send_invoice`.

    - `kakao_pay`
      Kakao Pay

    - `klarna`
      Klarna

      If set, the Subscription `collection_method` must be `send_invoice`.

    - `konbini`
      Konbini

      If set, the Subscription `collection_method` must be `send_invoice`.

    - `kr_card`
      Korean card

    - `link`
      Link

    - `multibanco`
      Multibanco

      If set, the Subscription `collection_method` must be `send_invoice`.

    - `naver_pay`
      Naver Pay

    - `nz_bank_account`
      NZ BECS Direct Debit

    - `p24`
      Przelewy24

      If set, the Subscription `collection_method` must be `send_invoice`.

    - `pay_by_bank`
      Pay By Bank

      If set, the Subscription `collection_method` must be `send_invoice`.

    - `payco`
      PAYCO

      If set, the Subscription `collection_method` must be `send_invoice`.

    - `paynow`
      PayNow

      If set, the Subscription `collection_method` must be `send_invoice`.

    - `paypal`
      PayPal

    - `payto`
      PayTo

    - `promptpay`
      PromptPay

      If set, the Subscription `collection_method` must be `send_invoice`.

    - `revolut_pay`
      Revolut Pay

    - `sepa_debit`
      SEPA Direct Debit

    - `sofort`
      SOFORT

      If set, the Subscription `collection_method` must be `send_invoice`.

    - `us_bank_account`
      ACH direct debit

    - `wechat_pay`
      WeChat Pay

      If set, the Subscription `collection_method` must be `send_invoice`.

- `pending_invoice_items_behavior` (enum, optional)
  How to handle pending invoice items on invoice creation. Defaults to `exclude` if the parameter is omitted.
Possible enum values:
  - `exclude`
    Always create an empty invoice draft regardless if there are pending invoice items or not.

  - `include`
    Include any pending invoice items, and create an empty draft invoice if no pending invoice items exist.

- `rendering` (object, optional)
  The rendering-related settings that control how the invoice is displayed on customer-facing surfaces such as PDF and Hosted Invoice Page.

  - `rendering.amount_tax_display` (enum, optional)
    How line-item prices and amounts will be displayed with respect to tax on invoice PDFs. One of `exclude_tax` or `include_inclusive_tax`. `include_inclusive_tax` will include inclusive tax (and exclude exclusive tax) in invoice PDF amounts. `exclude_tax` will exclude all tax (inclusive and exclusive alike) from invoice PDF amounts.
Possible enum values:
    - `exclude_tax`
    - `include_inclusive_tax`

  - `rendering.pdf` (object, optional)
    Invoice pdf rendering options

    - `rendering.pdf.page_size` (enum, optional)
      Page size for invoice PDF. Can be set to `a4`, `letter`, or `auto`. If set to `auto`, invoice PDF page size defaults to `a4` for customers with Japanese locale and `letter` for customers with other locales.
Possible enum values:
      - `a4`
      - `auto`
      - `letter`

  - `rendering.template` (string, optional)
    ID of the invoice rendering template to use for this invoice.

  - `rendering.template_version` (integer, optional)
    The specific version of invoice rendering template to use for this invoice.

- `shipping_cost` (object, optional)
  Settings for the cost of shipping for this invoice.

  - `shipping_cost.shipping_rate` (string, required unless shipping_rate_data is provided)
    The ID of the shipping rate to use for this order.

  - `shipping_cost.shipping_rate_data` (object, required unless shipping_rate is provided)
    Parameters to create a new ad-hoc shipping rate for this order.

    - `shipping_cost.shipping_rate_data.display_name` (string, required)
      The name of the shipping rate, meant to be displayable to the customer. This will appear on CheckoutSessions.

      The maximum length is 100 characters.

    - `shipping_cost.shipping_rate_data.delivery_estimate` (object, optional)
      The estimated range for how long shipping will take, meant to be displayable to the customer. This will appear on CheckoutSessions.

      - `shipping_cost.shipping_rate_data.delivery_estimate.maximum` (object, optional)
        The upper bound of the estimated range. If empty, represents no upper bound i.e., infinite.

        - `shipping_cost.shipping_rate_data.delivery_estimate.maximum.unit` (enum, required)
          A unit of time.
Possible enum values:
          - `business_day`
            The delivery estimate is in business days.

          - `day`
            The delivery estimate is in days.

          - `hour`
            The delivery estimate is in hours.

          - `month`
            The delivery estimate is in months.

          - `week`
            The delivery estimate is in weeks.

        - `shipping_cost.shipping_rate_data.delivery_estimate.maximum.value` (integer, required)
          Must be greater than 0.

      - `shipping_cost.shipping_rate_data.delivery_estimate.minimum` (object, optional)
        The lower bound of the estimated range. If empty, represents no lower bound.

        - `shipping_cost.shipping_rate_data.delivery_estimate.minimum.unit` (enum, required)
          A unit of time.
Possible enum values:
          - `business_day`
            The delivery estimate is in business days.

          - `day`
            The delivery estimate is in days.

          - `hour`
            The delivery estimate is in hours.

          - `month`
            The delivery estimate is in months.

          - `week`
            The delivery estimate is in weeks.

        - `shipping_cost.shipping_rate_data.delivery_estimate.minimum.value` (integer, required)
          Must be greater than 0.

    - `shipping_cost.shipping_rate_data.fixed_amount` (object, optional)
      Describes a fixed amount to charge for shipping. Must be present if type is `fixed_amount`.

      - `shipping_cost.shipping_rate_data.fixed_amount.amount` (integer, required)
        A non-negative integer in cents representing how much to charge.

      - `shipping_cost.shipping_rate_data.fixed_amount.currency` (enum, required)
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

      - `shipping_cost.shipping_rate_data.fixed_amount.currency_options` (object, optional)
        Shipping rates defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).

        - `shipping_cost.shipping_rate_data.fixed_amount.currency_options.<currency>.amount` (integer, required)
          A non-negative integer in cents representing how much to charge.

        - `shipping_cost.shipping_rate_data.fixed_amount.currency_options.<currency>.tax_behavior` (enum, recommended if calculating taxes)
          Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`.
Possible enum values:
          - `exclusive`
          - `inclusive`
          - `unspecified`

    - `shipping_cost.shipping_rate_data.metadata` (object, optional)
      Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

    - `shipping_cost.shipping_rate_data.tax_behavior` (enum, recommended if calculating taxes)
      Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`.
Possible enum values:
      - `exclusive`
      - `inclusive`
      - `unspecified`

    - `shipping_cost.shipping_rate_data.tax_code` (string, recommended if calculating taxes)
      A [tax code](https://docs.stripe.com/docs/tax/tax-categories.md) ID. The Shipping tax code is `txcd_92010001`.

    - `shipping_cost.shipping_rate_data.type` (enum, required)
      The type of calculation to use on the shipping rate.
Possible enum values:
      - `fixed_amount`
        The shipping rate is a fixed amount.

- `shipping_details` (object, optional)
  Shipping details for the invoice. The Invoice PDF will use the `shipping_details` value if it is set, otherwise the PDF will render the shipping address from the customer.

  - `shipping_details.address` (object, required)
    Shipping address

    - `shipping_details.address.city` (string, optional)
      City, district, suburb, town, or village.

    - `shipping_details.address.country` (string, required for calculating taxes)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `shipping_details.address.line1` (string, optional)
      Address line 1, such as the street, PO Box, or company name.

    - `shipping_details.address.line2` (string, optional)
      Address line 2, such as the apartment, suite, unit, or building.

    - `shipping_details.address.postal_code` (string, required for calculating taxes)
      ZIP or postal code.

    - `shipping_details.address.state` (string, optional)
      State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

  - `shipping_details.name` (string, required)
    Recipient name.

  - `shipping_details.phone` (string, optional)
    Recipient phone (including extension)

- `statement_descriptor` (string, optional)
  Extra information about a charge for the customer’s credit card statement. It must contain at least one letter. If not specified and this invoice is part of a subscription, the default `statement_descriptor` will be set to the first subscription item’s product’s `statement_descriptor`.

- `subscription` (string, optional)
  The ID of the subscription to invoice, if any. If set, the created invoice will only include pending invoice items for that subscription. The subscription’s billing cycle and regular subscription events won’t be affected.

- `transfer_data` (object, optional)
  If specified, the funds from the invoice will be transferred to the destination and the ID of the resulting transfer will be found on the invoice’s charge.

  - `transfer_data.destination` (string, required)
    ID of an existing, connected Stripe account.

  - `transfer_data.amount` (integer, optional)
    The amount that will be transferred automatically when the invoice is paid. If no amount is set, the full amount is transferred.

```curl
curl https://api.stripe.com/v1/invoices \
  -u "<<YOUR_SECRET_KEY>>" \
  -d customer=cus_NeZwdNtLEOXuvB
```

```cli
stripe invoices create  \
  --customer=cus_NeZwdNtLEOXuvB
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

invoice = client.v1.invoices.create({customer: 'cus_NeZwdNtLEOXuvB'})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

invoice = client.v1.invoices.create({"customer": "cus_NeZwdNtLEOXuvB"})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$invoice = $stripe->invoices->create(['customer' => 'cus_NeZwdNtLEOXuvB']);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

InvoiceCreateParams params =
  InvoiceCreateParams.builder().setCustomer("cus_NeZwdNtLEOXuvB").build();

Invoice invoice = client.v1().invoices().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const invoice = await stripe.invoices.create({
  customer: 'cus_NeZwdNtLEOXuvB',
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.InvoiceCreateParams{Customer: stripe.String("cus_NeZwdNtLEOXuvB")}
result, err := sc.V1Invoices.Create(context.TODO(), params)
```

```dotnet
var options = new InvoiceCreateOptions { Customer = "cus_NeZwdNtLEOXuvB" };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Invoices;
Invoice invoice = service.Create(options);
```

### Response

```json
{
  "id": "in_1MtHbELkdIwHu7ixl4OzzPMv",
  "object": "invoice",
  "account_country": "US",
  "account_name": "Stripe Docs",
  "account_tax_ids": null,
  "amount_due": 0,
  "amount_paid": 0,
  "amount_overpaid": 0,
  "amount_remaining": 0,
  "amount_shipping": 0,
  "application": null,
  "attempt_count": 0,
  "attempted": false,
  "auto_advance": false,
  "automatic_tax": {
    "enabled": false,
    "liability": null,
    "status": null
  },
  "billing_reason": "manual",
  "collection_method": "charge_automatically",
  "created": 1680644467,
  "currency": "usd",
  "custom_fields": null,
  "customer": "cus_NeZwdNtLEOXuvB",
  "customer_address": null,
  "customer_email": "jennyrosen@example.com",
  "customer_name": "Jenny Rosen",
  "customer_phone": null,
  "customer_shipping": null,
  "customer_tax_exempt": "none",
  "customer_tax_ids": [],
  "default_payment_method": null,
  "default_source": null,
  "default_tax_rates": [],
  "description": null,
  "discounts": [],
  "due_date": null,
  "ending_balance": null,
  "footer": null,
  "from_invoice": null,
  "hosted_invoice_url": null,
  "invoice_pdf": null,
  "issuer": {
    "type": "self"
  },
  "last_finalization_error": null,
  "latest_revision": null,
  "lines": {
    "object": "list",
    "data": [],
    "has_more": false,
    "total_count": 0,
    "url": "/v1/invoices/in_1MtHbELkdIwHu7ixl4OzzPMv/lines"
  },
  "livemode": false,
  "metadata": {},
  "next_payment_attempt": null,
  "number": null,
  "on_behalf_of": null,
  "parent": null,
  "payment_settings": {
    "default_mandate": null,
    "payment_method_options": null,
    "payment_method_types": null
  },
  "period_end": 1680644467,
  "period_start": 1680644467,
  "post_payment_credit_notes_amount": 0,
  "pre_payment_credit_notes_amount": 0,
  "receipt_number": null,
  "shipping_cost": null,
  "shipping_details": null,
  "starting_balance": 0,
  "statement_descriptor": null,
  "status": "draft",
  "status_transitions": {
    "finalized_at": null,
    "marked_uncollectible_at": null,
    "paid_at": null,
    "voided_at": null
  },
  "subtotal": 0,
  "subtotal_excluding_tax": 0,
  "test_clock": null,
  "total": 0,
  "total_discount_amounts": [],
  "total_excluding_tax": 0,
  "total_taxes": [],
  "webhooks_delivered_at": 1680644467
}
```