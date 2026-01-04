# Create a payment method configuration

Creates a payment method configuration

## Returns

Returns the payment method configuration object

## Parameters

- `acss_debit` (object, optional)
  Canadian pre-authorized debit payments, check this [page](https://docs.stripe.com/docs/payments/acss-debit.md) for more details like country availability.

  - `acss_debit.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `acss_debit.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `affirm` (object, optional)
  [Affirm](https://www.affirm.com/) gives your customers a way to split purchases over a series of payments. Depending on the purchase, they can pay with four interest-free payments (Split Pay) or pay over a longer term (Installments), which might include interest. Check this [page](https://docs.stripe.com/docs/payments/affirm.md) for more details like country availability.

  - `affirm.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `affirm.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `afterpay_clearpay` (object, optional)
  Afterpay gives your customers a way to pay for purchases in installments, check this [page](https://docs.stripe.com/docs/payments/afterpay-clearpay.md) for more details like country availability. Afterpay is particularly popular among businesses selling fashion, beauty, and sports products.

  - `afterpay_clearpay.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `afterpay_clearpay.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `alipay` (object, optional)
  Alipay is a digital wallet in China that has more than a billion active users worldwide. Alipay users can pay on the web or on a mobile device using login credentials or their Alipay app. Alipay has a low dispute rate and reduces fraud by authenticating payments using the customer’s login credentials. Check this [page](https://docs.stripe.com/docs/payments/alipay.md) for more details.

  - `alipay.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `alipay.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `alma` (object, optional)
  Alma is a Buy Now, Pay Later payment method that offers customers the ability to pay in 2, 3, or 4 installments.

  - `alma.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `alma.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `amazon_pay` (object, optional)
  Amazon Pay is a wallet payment method that lets your customers check out the same way as on Amazon.

  - `amazon_pay.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `amazon_pay.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `apple_pay` (object, optional)
  Stripe users can accept [Apple Pay](https://stripe.com/payments/apple-pay) in iOS applications in iOS 9 and later, and on the web in Safari starting with iOS 10 or macOS Sierra. There are no additional fees to process Apple Pay payments, and the [pricing](https://stripe.com/pricing) is the same as other card transactions. Check this [page](https://docs.stripe.com/docs/apple-pay.md) for more details.

  - `apple_pay.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `apple_pay.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `apple_pay_later` (object, optional)
  Apple Pay Later, a payment method for customers to buy now and pay later, gives your customers a way to split purchases into four installments across six weeks.

  - `apple_pay_later.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `apple_pay_later.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `au_becs_debit` (object, optional)
  Stripe users in Australia can accept Bulk Electronic Clearing System (BECS) direct debit payments from customers with an Australian bank account. Check this [page](https://docs.stripe.com/docs/payments/au-becs-debit.md) for more details.

  - `au_becs_debit.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `au_becs_debit.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `bacs_debit` (object, optional)
  Stripe users in the UK can accept Bacs Direct Debit payments from customers with a UK bank account, check this [page](https://docs.stripe.com/docs/payments/payment-methods/bacs-debit.md) for more details.

  - `bacs_debit.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `bacs_debit.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `bancontact` (object, optional)
  Bancontact is the most popular online payment method in Belgium, with over 15 million cards in circulation. [Customers](https://docs.stripe.com/docs/api/customers.md) use a Bancontact card or mobile app linked to a Belgian bank account to make online payments that are secure, guaranteed, and confirmed immediately. Check this [page](https://docs.stripe.com/docs/payments/bancontact.md) for more details.

  - `bancontact.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `bancontact.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `billie` (object, optional)
  Billie is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method that offers businesses Pay by Invoice where they offer payment terms ranging from 7-120 days. Customers are redirected from your website or app, authorize the payment with Billie, then return to your website or app. You get [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) of whether the payment succeeded or failed.

  - `billie.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `billie.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `blik` (object, optional)
  BLIK is a [single use](https://docs.stripe.com/docs/payments/payment-methods.md#usage) payment method that requires customers to authenticate their payments. When customers want to pay online using BLIK, they request a six-digit code from their banking application and enter it into the payment collection form. Check this [page](https://docs.stripe.com/docs/payments/blik.md) for more details.

  - `blik.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `blik.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `boleto` (object, optional)
  Boleto is an official (regulated by the Central Bank of Brazil) payment method in Brazil. Check this [page](https://docs.stripe.com/docs/payments/boleto.md) for more details.

  - `boleto.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `boleto.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `card` (object, optional)
  Cards are a popular way for consumers and businesses to pay online or in person. Stripe supports global and local card networks.

  - `card.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `card.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `cartes_bancaires` (object, optional)
  Cartes Bancaires is France’s local card network. More than 95% of these cards are co-branded with either Visa or Mastercard, meaning you can process these cards over either Cartes Bancaires or the Visa or Mastercard networks. Check this [page](https://docs.stripe.com/docs/payments/cartes-bancaires.md) for more details.

  - `cartes_bancaires.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `cartes_bancaires.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `cashapp` (object, optional)
  Cash App is a popular consumer app in the US that allows customers to bank, invest, send, and receive money using their digital wallet. Check this [page](https://docs.stripe.com/docs/payments/cash-app-pay.md) for more details.

  - `cashapp.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `cashapp.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `crypto` (object, optional)
  [Stablecoin payments](https://docs.stripe.com/docs/payments/stablecoin-payments.md) enable customers to pay in stablecoins like USDC from 100s of wallets including Phantom and Metamask.

  - `crypto.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `crypto.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `customer_balance` (object, optional)
  Uses a customer’s [cash balance](https://docs.stripe.com/docs/payments/customer-balance.md) for the payment. The cash balance can be funded via a bank transfer. Check this [page](https://docs.stripe.com/docs/payments/bank-transfers.md) for more details.

  - `customer_balance.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `customer_balance.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `eps` (object, optional)
  EPS is an Austria-based payment method that allows customers to complete transactions online using their bank credentials. EPS is supported by all Austrian banks and is accepted by over 80% of Austrian online retailers. Check this [page](https://docs.stripe.com/docs/payments/eps.md) for more details.

  - `eps.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `eps.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `fpx` (object, optional)
  Financial Process Exchange (FPX) is a Malaysia-based payment method that allows customers to complete transactions online using their bank credentials. Bank Negara Malaysia (BNM), the Central Bank of Malaysia, and eleven other major Malaysian financial institutions are members of the PayNet Group, which owns and operates FPX. It is one of the most popular online payment methods in Malaysia, with nearly 90 million transactions in 2018 according to BNM. Check this [page](https://docs.stripe.com/docs/payments/fpx.md) for more details.

  - `fpx.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `fpx.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `fr_meal_voucher_conecs` (object, optional)
  Meal vouchers in France, or “titres-restaurant”, is a local benefits program commonly offered by employers for their employees to purchase prepared food and beverages on working days. Check this [page](https://docs.stripe.com/docs/payments/benefits/fr-meal-vouchers.md) for more details.

  - `fr_meal_voucher_conecs.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `fr_meal_voucher_conecs.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `giropay` (object, optional)
  giropay is a German payment method based on online banking, introduced in 2006. It allows customers to complete transactions online using their online banking environment, with funds debited from their bank account. Depending on their bank, customers confirm payments on giropay using a second factor of authentication or a PIN. giropay accounts for 10% of online checkouts in Germany. Check this [page](https://docs.stripe.com/docs/payments/giropay.md) for more details.

  - `giropay.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `giropay.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `google_pay` (object, optional)
  Google Pay allows customers to make payments in your app or website using any credit or debit card saved to their Google Account, including those from Google Play, YouTube, Chrome, or an Android device. Use the Google Pay API to request any credit or debit card stored in your customer’s Google account. Check this [page](https://docs.stripe.com/docs/google-pay.md) for more details.

  - `google_pay.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `google_pay.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `grabpay` (object, optional)
  GrabPay is a payment method developed by [Grab](https://www.grab.com/sg/consumer/finance/pay/). GrabPay is a digital wallet - customers maintain a balance in their wallets that they pay out with. Check this [page](https://docs.stripe.com/docs/payments/grabpay.md) for more details.

  - `grabpay.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `grabpay.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `ideal` (object, optional)
  iDEAL is a Netherlands-based payment method that allows customers to complete transactions online using their bank credentials. All major Dutch banks are members of Currence, the scheme that operates iDEAL, making it the most popular online payment method in the Netherlands with a share of online transactions close to 55%. Check this [page](https://docs.stripe.com/docs/payments/ideal.md) for more details.

  - `ideal.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `ideal.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `jcb` (object, optional)
  JCB is a credit card company based in Japan. JCB is currently available in Japan to businesses approved by JCB, and available to all businesses in Australia, Canada, Hong Kong, Japan, New Zealand, Singapore, Switzerland, United Kingdom, United States, and all countries in the European Economic Area except Iceland. Check this [page](https://support.stripe.com/questions/accepting-japan-credit-bureau-%28jcb%29-payments) for more details.

  - `jcb.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `jcb.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `kakao_pay` (object, optional)
  Kakao Pay is a popular local wallet available in South Korea.

  - `kakao_pay.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `kakao_pay.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `klarna` (object, optional)
  Klarna gives customers a range of [payment options](https://docs.stripe.com/docs/payments/klarna.md#payment-options) during checkout. Available payment options vary depending on the customer’s billing address and the transaction amount. These payment options make it convenient for customers to purchase items in all price ranges. Check this [page](https://docs.stripe.com/docs/payments/klarna.md) for more details.

  - `klarna.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `klarna.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `konbini` (object, optional)
  Konbini allows customers in Japan to pay for bills and online purchases at convenience stores with cash. Check this [page](https://docs.stripe.com/docs/payments/konbini.md) for more details.

  - `konbini.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `konbini.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `kr_card` (object, optional)
  Korean cards let users pay using locally issued cards from South Korea.

  - `kr_card.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `kr_card.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `link` (object, optional)
  [Link](https://docs.stripe.com/docs/payments/link.md) is a payment method network. With Link, users save their payment details once, then reuse that information to pay with one click for any business on the network.

  - `link.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `link.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `mb_way` (object, optional)
  MB WAY is the most popular wallet in Portugal. After entering their phone number in your checkout, customers approve the payment directly in their MB WAY app. Check this [page](https://docs.stripe.com/docs/payments/mb-way.md) for more details.

  - `mb_way.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `mb_way.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `mobilepay` (object, optional)
  MobilePay is a [single-use](https://docs.stripe.com/docs/payments/payment-methods.md#usage) card wallet payment method used in Denmark and Finland. It allows customers to [authenticate and approve](https://docs.stripe.com/docs/payments/payment-methods.md#customer-actions) payments using the MobilePay app. Check this [page](https://docs.stripe.com/docs/payments/mobilepay.md) for more details.

  - `mobilepay.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `mobilepay.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `multibanco` (object, optional)
  Stripe users in Europe and the United States can accept Multibanco payments from customers in Portugal using [Sources](https://stripe.com/docs/sources)—a single integration path for creating payments using any supported method.

  - `multibanco.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `multibanco.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `name` (string, required unless parent is provided)
  Configuration name.

  The maximum length is 100 characters.

- `naver_pay` (object, optional)
  Naver Pay is a popular local wallet available in South Korea.

  - `naver_pay.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `naver_pay.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `nz_bank_account` (object, optional)
  Stripe users in New Zealand can accept Bulk Electronic Clearing System (BECS) direct debit payments from customers with a New Zeland bank account. Check this [page](https://docs.stripe.com/docs/payments/nz-bank-account.md) for more details.

  - `nz_bank_account.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `nz_bank_account.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `oxxo` (object, optional)
  OXXO is a Mexican chain of convenience stores with thousands of locations across Latin America and represents nearly 20% of online transactions in Mexico. OXXO allows customers to pay bills and online purchases in-store with cash. Check this [page](https://docs.stripe.com/docs/payments/oxxo.md) for more details.

  - `oxxo.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `oxxo.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `p24` (object, optional)
  Przelewy24 is a Poland-based payment method aggregator that allows customers to complete transactions online using bank transfers and other methods. Bank transfers account for 30% of online payments in Poland and Przelewy24 provides a way for customers to pay with over 165 banks. Check this [page](https://docs.stripe.com/docs/payments/p24.md) for more details.

  - `p24.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `p24.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `parent` (string, required unless name is provided)
  Configuration’s parent configuration. Specify to create a child configuration.

  The maximum length is 100 characters.

- `pay_by_bank` (object, optional)
  Pay by bank is a redirect payment method backed by bank transfers. A customer is redirected to their bank to authorize a bank transfer for a given amount. This removes a lot of the error risks inherent in waiting for the customer to initiate a transfer themselves, and is less expensive than card payments.

  - `pay_by_bank.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `pay_by_bank.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `payco` (object, optional)
  PAYCO is a [single-use](https://docs.stripe.com/payments/payment-methods#usage local wallet available in South Korea.

  - `payco.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `payco.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `paynow` (object, optional)
  PayNow is a Singapore-based payment method that allows customers to make a payment using their preferred app from participating banks and participating non-bank financial institutions. Check this [page](https://docs.stripe.com/docs/payments/paynow.md) for more details.

  - `paynow.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `paynow.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `paypal` (object, optional)
  PayPal, a digital wallet popular with customers in Europe, allows your customers worldwide to pay using their PayPal account. Check this [page](https://docs.stripe.com/docs/payments/paypal.md) for more details.

  - `paypal.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `paypal.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `paypay` (object, optional)
  Customers can pay with PayPay online or using the PayPay app.

  - `paypay.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `paypay.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `payto` (object, optional)
  PayTo is a [real-time](https://docs.stripe.com/payments/real-time.md) payment method that enables customers in Australia to pay by providing their bank account details. Customers must accept a mandate authorizing you to debit their account. Check this [page](https://docs.stripe.com/payments/payto.md) for more details.

  - `payto.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `payto.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `pix` (object, optional)
  Pix is a payment method popular in Brazil. When paying with Pix, customers authenticate and approve payments by scanning a QR code in their preferred banking app. Check this [page](https://docs.stripe.com/payments/pix.md) for more details.

  - `pix.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `pix.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `promptpay` (object, optional)
  PromptPay is a Thailand-based payment method that allows customers to make a payment using their preferred app from participating banks. Check this [page](https://docs.stripe.com/docs/payments/promptpay.md) for more details.

  - `promptpay.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `promptpay.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `revolut_pay` (object, optional)
  Revolut Pay, developed by Revolut, a global finance app, is a digital wallet payment method. Revolut Pay uses the customer’s stored balance or cards to fund the payment, and offers the option for non-Revolut customers to save their details after their first purchase.

  - `revolut_pay.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `revolut_pay.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `samsung_pay` (object, optional)
  Samsung Pay is a [single-use](https://docs.stripe.com/payments/payment-methods#usage local wallet available in South Korea.

  - `samsung_pay.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `samsung_pay.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `satispay` (object, optional)
  Satispay is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method where customers are required to [authenticate](https://docs.stripe.com/payments/payment-methods.md#customer-actions) their payment. Customers pay by being redirected from your website or app, authorizing the payment with Satispay, then returning to your website or app. You get [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) of whether the payment succeeded or failed.

  - `satispay.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `satispay.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `sepa_debit` (object, optional)
  The [Single Euro Payments Area (SEPA)](https://en.wikipedia.org/wiki/Single_Euro_Payments_Area) is an initiative of the European Union to simplify payments within and across member countries. SEPA established and enforced banking standards to allow for the direct debiting of every EUR-denominated bank account within the SEPA region, check this [page](https://docs.stripe.com/docs/payments/sepa-debit.md) for more details.

  - `sepa_debit.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `sepa_debit.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `sofort` (object, optional)
  Stripe users in Europe and the United States can use the [Payment Intents API](https://stripe.com/docs/payments/payment-intents)—a single integration path for creating payments using any supported method—to accept [Sofort](https://www.sofort.com/) payments from customers. Check this [page](https://docs.stripe.com/docs/payments/sofort.md) for more details.

  - `sofort.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `sofort.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `swish` (object, optional)
  Swish is a [real-time](https://docs.stripe.com/docs/payments/real-time.md) payment method popular in Sweden. It allows customers to [authenticate and approve](https://docs.stripe.com/docs/payments/payment-methods.md#customer-actions) payments using the Swish mobile app and the Swedish BankID mobile app. Check this [page](https://docs.stripe.com/docs/payments/swish.md) for more details.

  - `swish.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `swish.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `twint` (object, optional)
  Twint is a payment method popular in Switzerland. It allows customers to pay using their mobile phone. Check this [page](https://docs.stripe.com/payments/twint.md) for more details.

  - `twint.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `twint.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `us_bank_account` (object, optional)
  Stripe users in the United States can accept ACH direct debit payments from customers with a US bank account using the Automated Clearing House (ACH) payments system operated by Nacha. Check this [page](https://docs.stripe.com/docs/payments/ach-direct-debit.md) for more details.

  - `us_bank_account.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `us_bank_account.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `wechat_pay` (object, optional)
  WeChat, owned by Tencent, is China’s leading mobile app with over 1 billion monthly active users. Chinese consumers can use WeChat Pay to pay for goods and services inside of businesses’ apps and websites. WeChat Pay users buy most frequently in gaming, e-commerce, travel, online education, and food/nutrition. Check this [page](https://docs.stripe.com/docs/payments/wechat-pay.md) for more details.

  - `wechat_pay.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `wechat_pay.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

- `zip` (object, optional)
  Zip gives your customers a way to split purchases over a series of payments. Check this [page](https://docs.stripe.com/docs/payments/zip.md) for more details like country availability.

  - `zip.display_preference` (object, optional)
    Whether or not the payment method should be displayed.

    - `zip.display_preference.preference` (enum, optional)
      The account’s preference for whether or not to display this payment method.
Possible enum values:
      - `none`
        Use the parent or default setting.

      - `off`
        Don’t offer the payment method to users at checkout.

      - `on`
        Offer the payment method to users at checkout.

```curl
curl https://api.stripe.com/v1/payment_method_configurations \
  -u "<<YOUR_SECRET_KEY>>" \
  -d name="Buy Now Pay Laters"
```

```cli
stripe payment_method_configurations create  \
  --name="Buy Now Pay Laters"
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

payment_method_configuration = client.v1.payment_method_configurations.create({
  name: 'Buy Now Pay Laters',
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

payment_method_configuration = client.v1.payment_method_configurations.create({
  "name": "Buy Now Pay Laters",
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentMethodConfiguration = $stripe->paymentMethodConfigurations->create([
  'name' => 'Buy Now Pay Laters',
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PaymentMethodConfigurationCreateParams params =
  PaymentMethodConfigurationCreateParams.builder()
    .setName("Buy Now Pay Laters")
    .build();

PaymentMethodConfiguration paymentMethodConfiguration =
  client.v1().paymentMethodConfigurations().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentMethodConfiguration = await stripe.paymentMethodConfigurations.create({
  name: 'Buy Now Pay Laters',
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PaymentMethodConfigurationCreateParams{
  Name: stripe.String("Buy Now Pay Laters"),
}
result, err := sc.V1PaymentMethodConfigurations.Create(context.TODO(), params)
```

```dotnet
var options = new PaymentMethodConfigurationCreateOptions
{
    Name = "Buy Now Pay Laters",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.PaymentMethodConfigurations;
PaymentMethodConfiguration paymentMethodConfiguration = service.Create(options);
```

### Response

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