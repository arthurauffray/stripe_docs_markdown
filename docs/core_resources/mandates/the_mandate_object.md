# The Mandate object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `customer_acceptance` (object)
  Details about the customer’s acceptance of the mandate.

  - `customer_acceptance.accepted_at` (timestamp, nullable)
    The time that the customer accepts the mandate.

  - `customer_acceptance.offline` (object, nullable)
    If this mandate is accepted offline, this hash provides details about the offline acceptance.

  - `customer_acceptance.online` (object, nullable)
    If this mandate is accepted online, this hash provides details about the online acceptance.

    - `customer_acceptance.online.ip_address` (string, nullable)
      The customer accepts the mandate from this IP address.

    - `customer_acceptance.online.user_agent` (string, nullable)
      The customer accepts the mandate using the user agent of the browser.

  - `customer_acceptance.type` (enum)
    The mandate includes the type of customer acceptance information, such as: `online` or `offline`.
Possible enum values:
    - `offline`
    - `online`

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `multi_use` (object, nullable)
  If this is a `multi_use` mandate, this hash contains details about the mandate.

- `on_behalf_of` (string, nullable)
  The account (if any) that the mandate is intended for.

- `payment_method` (string)
  ID of the payment method associated with this mandate.

- `payment_method_details` (object)
  Additional mandate information specific to the payment method type.

  - `payment_method_details.acss_debit` (object, nullable)
    If this mandate associates with a `acss_debit` payment method, this hash contains mandate information specific to the `acss_debit` payment method.

    - `payment_method_details.acss_debit.default_for` (array of enums, nullable)
      List of Stripe products where this mandate can be selected automatically.
Possible enum values:
      - `invoice`
        Enables payments for Stripe Invoices. ‘subscription’ must also be provided.

      - `subscription`
        Enables payments for Stripe Subscriptions. ‘invoice’ must also be provided.

    - `payment_method_details.acss_debit.interval_description` (string, nullable)
      Description of the interval. Only required if the ‘payment_schedule’ parameter is ‘interval’ or ‘combined’.

    - `payment_method_details.acss_debit.payment_schedule` (enum)
      Payment schedule for the mandate.
Possible enum values:
      - `combined`
        Payments can be initiated at a pre-defined interval or sporadically

      - `interval`
        Payments are initiated at a regular pre-defined interval

      - `sporadic`
        Payments are initiated sporadically

    - `payment_method_details.acss_debit.transaction_type` (enum)
      Transaction type of the mandate.
Possible enum values:
      - `business`
        Transactions are made for business reasons

      - `personal`
        Transactions are made for personal reasons

  - `payment_method_details.amazon_pay` (object, nullable)
    If this mandate associates with a `amazon_pay` payment method, this hash contains mandate information specific to the `amazon_pay` payment method.

  - `payment_method_details.au_becs_debit` (object, nullable)
    If this mandate associates with a `au_becs_debit` payment method, this hash contains mandate information specific to the `au_becs_debit` payment method.

    - `payment_method_details.au_becs_debit.url` (string)
      The URL of the mandate. This URL generally contains sensitive information about the customer and should be shared with them exclusively.

  - `payment_method_details.bacs_debit` (object, nullable)
    If this mandate associates with a `bacs_debit` payment method, this hash contains mandate information specific to the `bacs_debit` payment method.

    - `payment_method_details.bacs_debit.network_status` (enum)
      The status of the mandate on the Bacs network. Can be one of `pending`, `revoked`, `refused`, or `accepted`.
Possible enum values:
      - `accepted`
      - `pending`
      - `refused`
      - `revoked`

    - `payment_method_details.bacs_debit.reference` (string)
      The unique reference identifying the mandate on the Bacs network.

    - `payment_method_details.bacs_debit.revocation_reason` (enum, nullable)
      When the mandate is revoked on the Bacs network this field displays the reason for the revocation.
Possible enum values:
      - `account_closed`
        The bank account has been closed. Refer to the customer to collect a new mandate.

      - `bank_account_restricted`
        The bank account has restrictions on either the type or the number of payouts allowed. This normally indicates that the bank account is a savings or other non-checking account. Refer to the customer to collect a new mandate.

      - `bank_ownership_changed`
        The destination bank account is no longer valid because it has been transferred to a new bank or to a new branch. A new mandate with the updated account details has been submitted on your behalf and you will be notified when it is accepted.

      - `could_not_process`
        The bank could not process this payout. Refer to the customer to collect a new mandate.

      - `debit_not_authorized`
        Debit transactions are not approved on this bank account. Refer to the customer to collect a new mandate.

    - `payment_method_details.bacs_debit.url` (string)
      The URL that will contain the mandate that the customer has signed.

  - `payment_method_details.card` (object, nullable)
    If this mandate associates with a `card` payment method, this hash contains mandate information specific to the `card` payment method.

  - `payment_method_details.cashapp` (object, nullable)
    If this mandate associates with a `cashapp` payment method, this hash contains mandate information specific to the `cashapp` payment method.

  - `payment_method_details.kakao_pay` (object, nullable)
    If this mandate associates with a `kakao_pay` payment method, this hash contains mandate information specific to the `kakao_pay` payment method.

  - `payment_method_details.klarna` (object, nullable)
    If this mandate associates with a `klarna` payment method, this hash contains mandate information specific to the `klarna` payment method.

  - `payment_method_details.kr_card` (object, nullable)
    If this mandate associates with a `kr_card` payment method, this hash contains mandate information specific to the `kr_card` payment method.

  - `payment_method_details.link` (object, nullable)
    If this mandate associates with a `link` payment method, this hash contains mandate information specific to the `link` payment method.

  - `payment_method_details.naver_pay` (object, nullable)
    If this mandate associates with a `naver_pay` payment method, this hash contains mandate information specific to the `naver_pay` payment method.

  - `payment_method_details.nz_bank_account` (object, nullable)
    If this mandate associates with a `nz_bank_account` payment method, this hash contains mandate information specific to the `nz_bank_account` payment method.

  - `payment_method_details.paypal` (object, nullable)
    If this mandate associates with a `paypal` payment method, this hash contains mandate information specific to the `paypal` payment method.

    - `payment_method_details.paypal.billing_agreement_id` (string, nullable)
      The PayPal Billing Agreement ID (BAID). This is an ID generated by PayPal which represents the mandate between the merchant and the customer.

    - `payment_method_details.paypal.payer_id` (string, nullable)
      PayPal account PayerID. This identifier uniquely identifies the PayPal customer.

  - `payment_method_details.payto` (object, nullable)
    If this mandate associates with a `payto` payment method, this hash contains mandate information specific to the `payto` payment method.

    - `payment_method_details.payto.amount` (integer, nullable)
      Amount that will be collected. It is required when `amount_type` is `fixed`.

    - `payment_method_details.payto.amount_type` (enum)
      The type of amount that will be collected. The amount charged must be exact or up to the value of `amount` param for `fixed` or `maximum` type respectively. Defaults to `maximum`.
Possible enum values:
      - `fixed`
        The amount is the exact amount that will be charged.

      - `maximum`
        The amount is the maximum amount that can be charged.

    - `payment_method_details.payto.end_date` (string, nullable)
      Date, in YYYY-MM-DD format, after which payments will not be collected. Defaults to no end date.

    - `payment_method_details.payto.payment_schedule` (enum)
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

    - `payment_method_details.payto.payments_per_period` (integer, nullable)
      The number of payments that will be made during a payment period. Defaults to 1 except for when `payment_schedule` is `adhoc`. In that case, it defaults to no limit.

    - `payment_method_details.payto.purpose` (enum, nullable)
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

    - `payment_method_details.payto.start_date` (string, nullable)
      Date, in YYYY-MM-DD format, from which payments will be collected. Defaults to confirmation time.

  - `payment_method_details.revolut_pay` (object, nullable)
    If this mandate associates with a `revolut_pay` payment method, this hash contains mandate information specific to the `revolut_pay` payment method.

  - `payment_method_details.sepa_debit` (object, nullable)
    If this mandate associates with a `sepa_debit` payment method, this hash contains mandate information specific to the `sepa_debit` payment method.

    - `payment_method_details.sepa_debit.reference` (string)
      The unique reference of the mandate.

    - `payment_method_details.sepa_debit.url` (string)
      The URL of the mandate. This URL generally contains sensitive information about the customer and should be shared with them exclusively.

  - `payment_method_details.type` (string)
    This mandate corresponds with a specific payment method type. The `payment_method_details` includes an additional hash with the same name and contains mandate information that’s specific to that payment method.

  - `payment_method_details.us_bank_account` (object, nullable)
    If this mandate associates with a `us_bank_account` payment method, this hash contains mandate information specific to the `us_bank_account` payment method.

    - `payment_method_details.us_bank_account.collection_method` (enum, nullable)
      Mandate collection method
Possible enum values:
      - `paper`
        Mandate customer acceptance was collected using a paper document

- `single_use` (object, nullable)
  If this is a `single_use` mandate, this hash contains details about the mandate.

  - `single_use.amount` (integer)
    The amount of the payment on a single use mandate.

  - `single_use.currency` (enum)
    The currency of the payment on a single use mandate.

- `status` (enum)
  The mandate status indicates whether or not you can use it to initiate a payment.
Possible enum values:
  - `active`
    The mandate can be used to initiate a payment.

  - `inactive`
    The mandate was rejected, revoked, or previously used, and may not be used to initiate future payments.

  - `pending`
    The mandate is newly created and is not yet active or inactive.

- `type` (enum)
  The type of the mandate.
Possible enum values:
  - `multi_use`
    Represents permission given for multiple payments.

  - `single_use`
    Represents a one-time permission given for a single payment.

### The Mandate object

```json
{
  "id": "mandate_1MvojA2eZvKYlo2CvqTABjZs",
  "object": "mandate",
  "customer_acceptance": {
    "accepted_at": 123456789,
    "online": {
      "ip_address": "127.0.0.0",
      "user_agent": "device"
    },
    "type": "online"
  },
  "livemode": false,
  "multi_use": {},
  "payment_method": "pm_123456789",
  "payment_method_details": {
    "sepa_debit": {
      "reference": "123456789",
      "url": ""
    },
    "type": "sepa_debit"
  },
  "status": "active",
  "type": "multi_use"
}
`