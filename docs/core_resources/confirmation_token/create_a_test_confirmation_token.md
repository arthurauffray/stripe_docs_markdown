# Create a test Confirmation Token

Creates a test mode Confirmation Token server side for your integration tests.

## Returns

Returns a testmode Confirmation Token

## Parameters

- `payment_method` (string, optional)
  ID of an existing PaymentMethod.

- `payment_method_data` (object, optional)
  If provided, this hash will be used to create a PaymentMethod.

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
  Payment-method-specific configuration for this ConfirmationToken.

  - `payment_method_options.card` (object, optional)
    Configuration for any card payments confirmed using this ConfirmationToken.

    - `payment_method_options.card.installments` (object, optional)
      Installment configuration for payments confirmed using this ConfirmationToken.

      - `payment_method_options.card.installments.plan` (object, required)
        The selected installment plan to use for this payment attempt. This parameter can only be provided during confirmation.

        - `payment_method_options.card.installments.plan.type` (enum, required)
          Type of installment plan, one of `fixed_count`, `bonus`, or `revolving`.
Possible enum values:
          - `bonus`
            An installment plan used in Japan, where the customer defers payment to a later date that aligns with their salary bonus.

          - `fixed_count`
            An installment plan where the number of installment payments is fixed and known at the time of purchase.

          - `revolving`
            An installment plan used in Japan, where the customer pays a certain amount each month, and the remaining balance rolls over to the next month.

        - `payment_method_options.card.installments.plan.count` (integer, optional)
          For `fixed_count` installment plans, this is required. It represents the number of installment payments your customer will make to their credit card.

        - `payment_method_options.card.installments.plan.interval` (enum, optional)
          For `fixed_count` installment plans, this is required. It represents the interval between installment payments your customer will make to their credit card. One of `month`.
Possible enum values:
          - `month`

- `return_url` (string, optional)
  Return URL used to confirm the Intent.

- `setup_future_usage` (enum, optional)
  Indicates that you intend to make future payments with this ConfirmationToken’s payment method.

  The presence of this property will [attach the payment method](https://docs.stripe.com/docs/payments/save-during-payment.md) to the PaymentIntent’s Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete.
Possible enum values:
  - `off_session`
    Use `off_session` if your customer may or may not be present in your checkout flow.

  - `on_session`
    Use `on_session` if you intend to only reuse the payment method when your customer is present in your checkout flow.

- `shipping` (object, optional)
  Shipping information for this ConfirmationToken.

  - `shipping.address` (object, required)
    Shipping address

    - `shipping.address.city` (string, optional)
      City, district, suburb, town, or village.

    - `shipping.address.country` (string, required for calculating taxes)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `shipping.address.line1` (string, optional)
      Address line 1, such as the street, PO Box, or company name.

    - `shipping.address.line2` (string, optional)
      Address line 2, such as the apartment, suite, unit, or building.

    - `shipping.address.postal_code` (string, required for calculating taxes)
      ZIP or postal code.

    - `shipping.address.state` (string, optional)
      State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

  - `shipping.name` (string, required)
    Recipient name.

  - `shipping.phone` (string, optional)
    Recipient phone (including extension)

```curl
curl https://api.stripe.com/v1/test_helpers/confirmation_tokens \
  -u "<<YOUR_SECRET_KEY>>" \
  -d payment_method=pm_card_visa
```

```cli
stripe test_helpers confirmation_tokens create  \
  --payment-method=pm_card_visa
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

confirmation_token = client.v1.test_helpers.confirmation_tokens.create({
  payment_method: 'pm_card_visa',
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

confirmation_token = client.v1.test_helpers.confirmation_tokens.create({
  "payment_method": "pm_card_visa",
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$confirmationToken = $stripe->testHelpers->confirmationTokens->create([
  'payment_method' => 'pm_card_visa',
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ConfirmationTokenCreateParams params =
  ConfirmationTokenCreateParams.builder().setPaymentMethod("pm_card_visa").build();

ConfirmationToken confirmationToken =
  client.v1().testHelpers().confirmationTokens().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const confirmationToken = await stripe.testHelpers.confirmationTokens.create({
  payment_method: 'pm_card_visa',
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TestHelpersConfirmationTokenCreateParams{
  PaymentMethod: stripe.String("pm_card_visa"),
}
result, err := sc.V1TestHelpersConfirmationTokens.Create(context.TODO(), params)
```

```dotnet
var options = new Stripe.TestHelpers.ConfirmationTokenCreateOptions
{
    PaymentMethod = "pm_card_visa",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.TestHelpers.ConfirmationTokens;
ConfirmationToken confirmationToken = service.Create(options);
```

### Response

```json
{
  "id": "ctoken_1Ow71CL4FhS6zgoxWjxc7sfr",
  "object": "confirmation_token",
  "created": 1710871450,
  "expires_at": 1710914650,
  "livemode": false,
  "payment_intent": null,
  "payment_method_preview": {
    "billing_details": {
      "address": {
        "city": null,
        "country": null,
        "line1": null,
        "line2": null,
        "postal_code": null,
        "state": null
      },
      "email": null,
      "name": null,
      "phone": null
    },
    "card": {
      "brand": "visa",
      "checks": {
        "address_line1_check": null,
        "address_postal_code_check": null,
        "cvc_check": "unchecked"
      },
      "country": "US",
      "display_brand": "visa",
      "exp_month": 3,
      "exp_year": 2025,
      "fingerprint": "jbGyCKrSRsFpOBWP",
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
  "return_url": null,
  "setup_future_usage": null,
  "setup_intent": null,
  "shipping": null,
  "use_stripe_sdk": true
}
```