# The Payment Method Configuration object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `acss_debit` (object, nullable)
  Canadian pre-authorized debit payments, check this [page](https://docs.stripe.com/docs/payments/acss-debit.md) for more details like country availability.

  - `acss_debit.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `acss_debit.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `acss_debit.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `acss_debit.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `acss_debit.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `active` (boolean)
  Whether the configuration can be used for new payments.

- `affirm` (object, nullable)
  [Affirm](https://www.affirm.com/) gives your customers a way to split purchases over a series of payments. Depending on the purchase, they can pay with four interest-free payments (Split Pay) or pay over a longer term (Installments), which might include interest. Check this [page](https://docs.stripe.com/docs/payments/affirm.md) for more details like country availability.

  - `affirm.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `affirm.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `affirm.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `affirm.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `affirm.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `afterpay_clearpay` (object, nullable)
  Afterpay gives your customers a way to pay for purchases in installments, check this [page](https://docs.stripe.com/docs/payments/afterpay-clearpay.md) for more details like country availability. Afterpay is particularly popular among businesses selling fashion, beauty, and sports products.

  - `afterpay_clearpay.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `afterpay_clearpay.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `afterpay_clearpay.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `afterpay_clearpay.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `afterpay_clearpay.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `alipay` (object, nullable)
  Alipay is a digital wallet in China that has more than a billion active users worldwide. Alipay users can pay on the web or on a mobile device using login credentials or their Alipay app. Alipay has a low dispute rate and reduces fraud by authenticating payments using the customer’s login credentials. Check this [page](https://docs.stripe.com/docs/payments/alipay.md) for more details.

  - `alipay.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `alipay.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `alipay.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `alipay.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `alipay.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `alma` (object, nullable)
  Alma is a Buy Now, Pay Later payment method that offers customers the ability to pay in 2, 3, or 4 installments.

  - `alma.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `alma.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `alma.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `alma.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `alma.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `amazon_pay` (object, nullable)
  Amazon Pay is a wallet payment method that lets your customers check out the same way as on Amazon.

  - `amazon_pay.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `amazon_pay.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `amazon_pay.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `amazon_pay.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `amazon_pay.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `apple_pay` (object, nullable)
  Stripe users can accept [Apple Pay](https://stripe.com/payments/apple-pay) in iOS applications in iOS 9 and later, and on the web in Safari starting with iOS 10 or macOS Sierra. There are no additional fees to process Apple Pay payments, and the [pricing](https://stripe.com/pricing) is the same as other card transactions. Check this [page](https://docs.stripe.com/docs/apple-pay.md) for more details.

  - `apple_pay.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `apple_pay.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `apple_pay.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `apple_pay.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `apple_pay.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `application` (string, nullable)
  For child configs, the Connect application associated with the configuration.

- `au_becs_debit` (object, nullable)
  Stripe users in Australia can accept Bulk Electronic Clearing System (BECS) direct debit payments from customers with an Australian bank account. Check this [page](https://docs.stripe.com/docs/payments/au-becs-debit.md) for more details.

  - `au_becs_debit.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `au_becs_debit.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `au_becs_debit.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `au_becs_debit.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `au_becs_debit.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `bacs_debit` (object, nullable)
  Stripe users in the UK can accept Bacs Direct Debit payments from customers with a UK bank account, check this [page](https://docs.stripe.com/docs/payments/payment-methods/bacs-debit.md) for more details.

  - `bacs_debit.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `bacs_debit.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `bacs_debit.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `bacs_debit.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `bacs_debit.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `bancontact` (object, nullable)
  Bancontact is the most popular online payment method in Belgium, with over 15 million cards in circulation. [Customers](https://docs.stripe.com/docs/api/customers.md) use a Bancontact card or mobile app linked to a Belgian bank account to make online payments that are secure, guaranteed, and confirmed immediately. Check this [page](https://docs.stripe.com/docs/payments/bancontact.md) for more details.

  - `bancontact.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `bancontact.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `bancontact.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `bancontact.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `bancontact.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `billie` (object, nullable)
  Billie is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method that offers businesses Pay by Invoice where they offer payment terms ranging from 7-120 days. Customers are redirected from your website or app, authorize the payment with Billie, then return to your website or app. You get [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) of whether the payment succeeded or failed.

  - `billie.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `billie.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `billie.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `billie.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `billie.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `blik` (object, nullable)
  BLIK is a [single use](https://docs.stripe.com/docs/payments/payment-methods.md#usage) payment method that requires customers to authenticate their payments. When customers want to pay online using BLIK, they request a six-digit code from their banking application and enter it into the payment collection form. Check this [page](https://docs.stripe.com/docs/payments/blik.md) for more details.

  - `blik.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `blik.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `blik.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `blik.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `blik.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `boleto` (object, nullable)
  Boleto is an official (regulated by the Central Bank of Brazil) payment method in Brazil. Check this [page](https://docs.stripe.com/docs/payments/boleto.md) for more details.

  - `boleto.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `boleto.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `boleto.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `boleto.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `boleto.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `card` (object, nullable)
  Cards are a popular way for consumers and businesses to pay online or in person. Stripe supports global and local card networks.

  - `card.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `card.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `card.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `card.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `card.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `cartes_bancaires` (object, nullable)
  Cartes Bancaires is France’s local card network. More than 95% of these cards are co-branded with either Visa or Mastercard, meaning you can process these cards over either Cartes Bancaires or the Visa or Mastercard networks. Check this [page](https://docs.stripe.com/docs/payments/cartes-bancaires.md) for more details.

  - `cartes_bancaires.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `cartes_bancaires.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `cartes_bancaires.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `cartes_bancaires.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `cartes_bancaires.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `cashapp` (object, nullable)
  Cash App is a popular consumer app in the US that allows customers to bank, invest, send, and receive money using their digital wallet. Check this [page](https://docs.stripe.com/docs/payments/cash-app-pay.md) for more details.

  - `cashapp.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `cashapp.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `cashapp.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `cashapp.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `cashapp.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `crypto` (object, nullable)
  [Stablecoin payments](https://docs.stripe.com/docs/payments/stablecoin-payments.md) enable customers to pay in stablecoins like USDC from 100s of wallets including Phantom and Metamask.

  - `crypto.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `crypto.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `crypto.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `crypto.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `crypto.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `customer_balance` (object, nullable)
  Uses a customer’s [cash balance](https://docs.stripe.com/docs/payments/customer-balance.md) for the payment. The cash balance can be funded via a bank transfer. Check this [page](https://docs.stripe.com/docs/payments/bank-transfers.md) for more details.

  - `customer_balance.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `customer_balance.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `customer_balance.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `customer_balance.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `customer_balance.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `eps` (object, nullable)
  EPS is an Austria-based payment method that allows customers to complete transactions online using their bank credentials. EPS is supported by all Austrian banks and is accepted by over 80% of Austrian online retailers. Check this [page](https://docs.stripe.com/docs/payments/eps.md) for more details.

  - `eps.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `eps.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `eps.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `eps.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `eps.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `fpx` (object, nullable)
  Financial Process Exchange (FPX) is a Malaysia-based payment method that allows customers to complete transactions online using their bank credentials. Bank Negara Malaysia (BNM), the Central Bank of Malaysia, and eleven other major Malaysian financial institutions are members of the PayNet Group, which owns and operates FPX. It is one of the most popular online payment methods in Malaysia, with nearly 90 million transactions in 2018 according to BNM. Check this [page](https://docs.stripe.com/docs/payments/fpx.md) for more details.

  - `fpx.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `fpx.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `fpx.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `fpx.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `fpx.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `giropay` (object, nullable)
  giropay is a German payment method based on online banking, introduced in 2006. It allows customers to complete transactions online using their online banking environment, with funds debited from their bank account. Depending on their bank, customers confirm payments on giropay using a second factor of authentication or a PIN. giropay accounts for 10% of online checkouts in Germany. Check this [page](https://docs.stripe.com/docs/payments/giropay.md) for more details.

  - `giropay.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `giropay.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `giropay.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `giropay.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `giropay.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `google_pay` (object, nullable)
  Google Pay allows customers to make payments in your app or website using any credit or debit card saved to their Google Account, including those from Google Play, YouTube, Chrome, or an Android device. Use the Google Pay API to request any credit or debit card stored in your customer’s Google account. Check this [page](https://docs.stripe.com/docs/google-pay.md) for more details.

  - `google_pay.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `google_pay.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `google_pay.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `google_pay.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `google_pay.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `grabpay` (object, nullable)
  GrabPay is a payment method developed by [Grab](https://www.grab.com/sg/consumer/finance/pay/). GrabPay is a digital wallet - customers maintain a balance in their wallets that they pay out with. Check this [page](https://docs.stripe.com/docs/payments/grabpay.md) for more details.

  - `grabpay.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `grabpay.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `grabpay.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `grabpay.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `grabpay.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `ideal` (object, nullable)
  iDEAL is a Netherlands-based payment method that allows customers to complete transactions online using their bank credentials. All major Dutch banks are members of Currence, the scheme that operates iDEAL, making it the most popular online payment method in the Netherlands with a share of online transactions close to 55%. Check this [page](https://docs.stripe.com/docs/payments/ideal.md) for more details.

  - `ideal.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `ideal.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `ideal.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `ideal.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `ideal.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `is_default` (boolean)
  The default configuration is used whenever a payment method configuration is not specified.

- `jcb` (object, nullable)
  JCB is a credit card company based in Japan. JCB is currently available in Japan to businesses approved by JCB, and available to all businesses in Australia, Canada, Hong Kong, Japan, New Zealand, Singapore, Switzerland, United Kingdom, United States, and all countries in the European Economic Area except Iceland. Check this [page](https://support.stripe.com/questions/accepting-japan-credit-bureau-%28jcb%29-payments) for more details.

  - `jcb.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `jcb.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `jcb.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `jcb.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `jcb.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `kakao_pay` (object, nullable)
  Kakao Pay is a popular local wallet available in South Korea.

  - `kakao_pay.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `kakao_pay.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `kakao_pay.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `kakao_pay.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `kakao_pay.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `klarna` (object, nullable)
  Klarna gives customers a range of [payment options](https://docs.stripe.com/docs/payments/klarna.md#payment-options) during checkout. Available payment options vary depending on the customer’s billing address and the transaction amount. These payment options make it convenient for customers to purchase items in all price ranges. Check this [page](https://docs.stripe.com/docs/payments/klarna.md) for more details.

  - `klarna.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `klarna.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `klarna.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `klarna.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `klarna.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `konbini` (object, nullable)
  Konbini allows customers in Japan to pay for bills and online purchases at convenience stores with cash. Check this [page](https://docs.stripe.com/docs/payments/konbini.md) for more details.

  - `konbini.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `konbini.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `konbini.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `konbini.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `konbini.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `kr_card` (object, nullable)
  Korean cards let users pay using locally issued cards from South Korea.

  - `kr_card.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `kr_card.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `kr_card.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `kr_card.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `kr_card.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `link` (object, nullable)
  [Link](https://docs.stripe.com/docs/payments/link.md) is a payment method network. With Link, users save their payment details once, then reuse that information to pay with one click for any business on the network.

  - `link.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `link.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `link.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `link.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `link.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `mb_way` (object, nullable)
  MB WAY is the most popular wallet in Portugal. After entering their phone number in your checkout, customers approve the payment directly in their MB WAY app. Check this [page](https://docs.stripe.com/docs/payments/mb-way.md) for more details.

  - `mb_way.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `mb_way.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `mb_way.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `mb_way.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `mb_way.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `mobilepay` (object, nullable)
  MobilePay is a [single-use](https://docs.stripe.com/docs/payments/payment-methods.md#usage) card wallet payment method used in Denmark and Finland. It allows customers to [authenticate and approve](https://docs.stripe.com/docs/payments/payment-methods.md#customer-actions) payments using the MobilePay app. Check this [page](https://docs.stripe.com/docs/payments/mobilepay.md) for more details.

  - `mobilepay.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `mobilepay.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `mobilepay.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `mobilepay.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `mobilepay.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `multibanco` (object, nullable)
  Stripe users in Europe and the United States can accept Multibanco payments from customers in Portugal using [Sources](https://stripe.com/docs/sources)—a single integration path for creating payments using any supported method.

  - `multibanco.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `multibanco.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `multibanco.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `multibanco.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `multibanco.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `name` (string)
  The configuration’s name.

- `naver_pay` (object, nullable)
  Naver Pay is a popular local wallet available in South Korea.

  - `naver_pay.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `naver_pay.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `naver_pay.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `naver_pay.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `naver_pay.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `nz_bank_account` (object, nullable)
  Stripe users in New Zealand can accept Bulk Electronic Clearing System (BECS) direct debit payments from customers with a New Zeland bank account. Check this [page](https://docs.stripe.com/docs/payments/nz-bank-account.md) for more details.

  - `nz_bank_account.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `nz_bank_account.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `nz_bank_account.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `nz_bank_account.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `nz_bank_account.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `oxxo` (object, nullable)
  OXXO is a Mexican chain of convenience stores with thousands of locations across Latin America and represents nearly 20% of online transactions in Mexico. OXXO allows customers to pay bills and online purchases in-store with cash. Check this [page](https://docs.stripe.com/docs/payments/oxxo.md) for more details.

  - `oxxo.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `oxxo.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `oxxo.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `oxxo.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `oxxo.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `p24` (object, nullable)
  Przelewy24 is a Poland-based payment method aggregator that allows customers to complete transactions online using bank transfers and other methods. Bank transfers account for 30% of online payments in Poland and Przelewy24 provides a way for customers to pay with over 165 banks. Check this [page](https://docs.stripe.com/docs/payments/p24.md) for more details.

  - `p24.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `p24.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `p24.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `p24.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `p24.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `parent` (string, nullable)
  For child configs, the configuration’s parent configuration.

- `pay_by_bank` (object, nullable)
  Pay by bank is a redirect payment method backed by bank transfers. A customer is redirected to their bank to authorize a bank transfer for a given amount. This removes a lot of the error risks inherent in waiting for the customer to initiate a transfer themselves, and is less expensive than card payments.

  - `pay_by_bank.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `pay_by_bank.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `pay_by_bank.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `pay_by_bank.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `pay_by_bank.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `payco` (object, nullable)
  PAYCO is a [single-use](https://docs.stripe.com/payments/payment-methods#usage local wallet available in South Korea.

  - `payco.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `payco.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `payco.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `payco.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `payco.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `paynow` (object, nullable)
  PayNow is a Singapore-based payment method that allows customers to make a payment using their preferred app from participating banks and participating non-bank financial institutions. Check this [page](https://docs.stripe.com/docs/payments/paynow.md) for more details.

  - `paynow.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `paynow.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `paynow.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `paynow.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `paynow.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `paypal` (object, nullable)
  PayPal, a digital wallet popular with customers in Europe, allows your customers worldwide to pay using their PayPal account. Check this [page](https://docs.stripe.com/docs/payments/paypal.md) for more details.

  - `paypal.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `paypal.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `paypal.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `paypal.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `paypal.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `paypay` (object, nullable)
  Customers can pay with PayPay online or using the PayPay app.

  - `paypay.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `paypay.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `paypay.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `paypay.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `paypay.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `payto` (object, nullable)
  PayTo is a [real-time](https://docs.stripe.com/payments/real-time.md) payment method that enables customers in Australia to pay by providing their bank account details. Customers must accept a mandate authorizing you to debit their account. Check this [page](https://docs.stripe.com/payments/payto.md) for more details.

  - `payto.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `payto.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `payto.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `payto.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `payto.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `pix` (object, nullable)
  Pix is a payment method popular in Brazil. When paying with Pix, customers authenticate and approve payments by scanning a QR code in their preferred banking app. Check this [page](https://docs.stripe.com/payments/pix.md) for more details.

  - `pix.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `pix.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `pix.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `pix.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `pix.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `promptpay` (object, nullable)
  PromptPay is a Thailand-based payment method that allows customers to make a payment using their preferred app from participating banks. Check this [page](https://docs.stripe.com/docs/payments/promptpay.md) for more details.

  - `promptpay.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `promptpay.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `promptpay.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `promptpay.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `promptpay.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `revolut_pay` (object, nullable)
  Revolut Pay, developed by Revolut, a global finance app, is a digital wallet payment method. Revolut Pay uses the customer’s stored balance or cards to fund the payment, and offers the option for non-Revolut customers to save their details after their first purchase.

  - `revolut_pay.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `revolut_pay.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `revolut_pay.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `revolut_pay.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `revolut_pay.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `samsung_pay` (object, nullable)
  Samsung Pay is a [single-use](https://docs.stripe.com/payments/payment-methods#usage local wallet available in South Korea.

  - `samsung_pay.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `samsung_pay.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `samsung_pay.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `samsung_pay.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `samsung_pay.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `satispay` (object, nullable)
  Satispay is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method where customers are required to [authenticate](https://docs.stripe.com/payments/payment-methods.md#customer-actions) their payment. Customers pay by being redirected from your website or app, authorizing the payment with Satispay, then returning to your website or app. You get [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) of whether the payment succeeded or failed.

  - `satispay.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `satispay.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `satispay.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `satispay.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `satispay.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `sepa_debit` (object, nullable)
  The [Single Euro Payments Area (SEPA)](https://en.wikipedia.org/wiki/Single_Euro_Payments_Area) is an initiative of the European Union to simplify payments within and across member countries. SEPA established and enforced banking standards to allow for the direct debiting of every EUR-denominated bank account within the SEPA region, check this [page](https://docs.stripe.com/docs/payments/sepa-debit.md) for more details.

  - `sepa_debit.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `sepa_debit.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `sepa_debit.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `sepa_debit.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `sepa_debit.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `sofort` (object, nullable)
  Stripe users in Europe and the United States can use the [Payment Intents API](https://stripe.com/docs/payments/payment-intents)—a single integration path for creating payments using any supported method—to accept [Sofort](https://www.sofort.com/) payments from customers. Check this [page](https://docs.stripe.com/docs/payments/sofort.md) for more details.

  - `sofort.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `sofort.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `sofort.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `sofort.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `sofort.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `swish` (object, nullable)
  Swish is a [real-time](https://docs.stripe.com/docs/payments/real-time.md) payment method popular in Sweden. It allows customers to [authenticate and approve](https://docs.stripe.com/docs/payments/payment-methods.md#customer-actions) payments using the Swish mobile app and the Swedish BankID mobile app. Check this [page](https://docs.stripe.com/docs/payments/swish.md) for more details.

  - `swish.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `swish.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `swish.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `swish.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `swish.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `twint` (object, nullable)
  Twint is a payment method popular in Switzerland. It allows customers to pay using their mobile phone. Check this [page](https://docs.stripe.com/payments/twint.md) for more details.

  - `twint.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `twint.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `twint.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `twint.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `twint.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `us_bank_account` (object, nullable)
  Stripe users in the United States can accept ACH direct debit payments from customers with a US bank account using the Automated Clearing House (ACH) payments system operated by Nacha. Check this [page](https://docs.stripe.com/docs/payments/ach-direct-debit.md) for more details.

  - `us_bank_account.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `us_bank_account.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `us_bank_account.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `us_bank_account.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `us_bank_account.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `wechat_pay` (object, nullable)
  WeChat, owned by Tencent, is China’s leading mobile app with over 1 billion monthly active users. Chinese consumers can use WeChat Pay to pay for goods and services inside of businesses’ apps and websites. WeChat Pay users buy most frequently in gaming, e-commerce, travel, online education, and food/nutrition. Check this [page](https://docs.stripe.com/docs/payments/wechat-pay.md) for more details.

  - `wechat_pay.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `wechat_pay.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `wechat_pay.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `wechat_pay.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `wechat_pay.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `zip` (object, nullable)
  Zip gives your customers a way to split purchases over a series of payments. Check this [page](https://docs.stripe.com/docs/payments/zip.md) for more details like country availability.

  - `zip.available` (boolean)
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method’s capability is active.

  - `zip.display_preference` (object)
    Whether this payment method should be offered at checkout.

    - `zip.display_preference.overridable` (boolean, nullable)
      For child configs, whether or not the account’s preference will be observed. If `false`, the parent configuration’s default is used.

    - `zip.display_preference.preference` (enum)
      The account’s display preference.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

    - `zip.display_preference.value` (enum)
      The effective display preference value.
Possible enum values:
      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

### The Payment Method Configuration object

```json
{
  "id": "pmc_abcdef",
  "object": "payment_method_configuration",
  "acss_debit": {
    "available": false,
    "display_preference": {
      "overridable": null,
      "preference": "off",
      "value": "off"
    }
  },
  "active": true,
  "affirm": {
    "available": false,
    "display_preference": {
      "overridable": null,
      "preference": "off",
      "value": "off"
    }
  },
  "afterpay_clearpay": {
    "available": false,
    "display_preference": {
      "overridable": null,
      "preference": "off",
      "value": "off"
    }
  },
  "alipay": {
    "available": false,
    "display_preference": {
      "overridable": null,
      "preference": "off",
      "value": "off"
    }
  },
  "apple_pay": {
    "available": true,
    "display_preference": {
      "overridable": null,
      "preference": "on",
      "value": "on"
    }
  },
  "bancontact": {
    "available": false,
    "display_preference": {
      "overridable": null,
      "preference": "off",
      "value": "off"
    }
  },
  "card": {
    "available": true,
    "display_preference": {
      "overridable": null,
      "preference": "on",
      "value": "on"
    }
  },
  "cartes_bancaires": {
    "available": false,
    "display_preference": {
      "overridable": null,
      "preference": "off",
      "value": "off"
    }
  },
  "eps": {
    "available": false,
    "display_preference": {
      "overridable": null,
      "preference": "off",
      "value": "off"
    }
  },
  "giropay": {
    "available": false,
    "display_preference": {
      "overridable": null,
      "preference": "off",
      "value": "off"
    }
  },
  "google_pay": {
    "available": true,
    "display_preference": {
      "overridable": null,
      "preference": "on",
      "value": "on"
    }
  },
  "ideal": {
    "available": false,
    "display_preference": {
      "overridable": null,
      "preference": "off",
      "value": "off"
    }
  },
  "is_default": true,
  "klarna": {
    "available": false,
    "display_preference": {
      "overridable": null,
      "preference": "off",
      "value": "off"
    }
  },
  "link": {
    "available": true,
    "display_preference": {
      "overridable": null,
      "preference": "on",
      "value": "on"
    }
  },
  "livemode": false,
  "name": "Default",
  "p24": {
    "available": false,
    "display_preference": {
      "overridable": null,
      "preference": "off",
      "value": "off"
    }
  },
  "sepa_debit": {
    "available": false,
    "display_preference": {
      "overridable": null,
      "preference": "off",
      "value": "off"
    }
  },
  "sofort": {
    "available": false,
    "display_preference": {
      "overridable": null,
      "preference": "off",
      "value": "off"
    }
  },
  "us_bank_account": {
    "available": false,
    "display_preference": {
      "overridable": null,
      "preference": "off",
      "value": "off"
    }
  },
  "wechat_pay": {
    "available": false,
    "display_preference": {
      "overridable": null,
      "preference": "off",
      "value": "off"
    }
  }
}
```