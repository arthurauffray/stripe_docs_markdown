# The Customer Session object

## Attributes

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `client_secret` (string)
  The client secret of this Customer Session. Used on the client to set up secure access to the given `customer`.

  The client secret can be used to provide access to `customer` from your frontend. It should not be stored, logged, or exposed to anyone other than the relevant customer. Make sure that you have TLS enabled on any page that includes the client secret.

- `components` (object)
  This hash defines which component is enabled and the features it supports.

  - `components.buy_button` (object)
    Configuration for buy button.

    - `components.buy_button.enabled` (boolean)
      Whether the buy button is enabled.

  - `components.customer_sheet` (object)
    Configuration for the customer sheet.

    - `components.customer_sheet.enabled` (boolean)
      Whether the customer sheet is enabled.

    - `components.customer_sheet.features` (object, nullable)
      This hash defines whether the customer sheet supports certain features.

      - `components.customer_sheet.features.payment_method_allow_redisplay_filters` (array of enums, nullable)
        A list of [`allow_redisplay`](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay) values that controls which saved payment methods the customer sheet displays by filtering to only show payment methods with an `allow_redisplay` value that is present in this list.

        If not specified, defaults to [“always”]. In order to display all saved payment methods, specify [“always”, “limited”, “unspecified”].
Possible enum values:
        - `always`
          Use `always` to indicate that this payment method can always be shown to a customer in a checkout flow.

        - `limited`
          Use `limited` to indicate that this payment method can’t always be shown to a customer in a checkout flow. For example, it can only be shown in the context of a specific subscription.

        - `unspecified`
          This is the default value for payment methods where `allow_redisplay` wasn’t set.

      - `components.customer_sheet.features.payment_method_remove` (enum, nullable)
        Controls whether the customer sheet displays the option to remove a saved payment method."

        Allowing buyers to remove their saved payment methods impacts subscriptions that depend on that payment method. Removing the payment method detaches the [`customer` object](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-customer) from that [PaymentMethod](https://docs.stripe.com/api/payment_methods.md).
Possible enum values:
        - `disabled`
          The feature is disabled.

        - `enabled`
          The feature is enabled.

  - `components.mobile_payment_element` (object)
    Configuration for the mobile payment element.

    - `components.mobile_payment_element.enabled` (boolean)
      Whether the mobile payment element is enabled.

    - `components.mobile_payment_element.features` (object, nullable)
      This hash defines whether the mobile payment element supports certain features.

      - `components.mobile_payment_element.features.payment_method_allow_redisplay_filters` (array of enums, nullable)
        A list of [`allow_redisplay`](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay) values that controls which saved payment methods the mobile payment element displays by filtering to only show payment methods with an `allow_redisplay` value that is present in this list.

        If not specified, defaults to [“always”]. In order to display all saved payment methods, specify [“always”, “limited”, “unspecified”].
Possible enum values:
        - `always`
          Use `always` to indicate that this payment method can always be shown to a customer in a checkout flow.

        - `limited`
          Use `limited` to indicate that this payment method can’t always be shown to a customer in a checkout flow. For example, it can only be shown in the context of a specific subscription.

        - `unspecified`
          This is the default value for payment methods where `allow_redisplay` wasn’t set.

      - `components.mobile_payment_element.features.payment_method_redisplay` (enum, nullable)
        Controls whether or not the mobile payment element shows saved payment methods.
Possible enum values:
        - `disabled`
          The feature is disabled.

        - `enabled`
          The feature is enabled.

      - `components.mobile_payment_element.features.payment_method_remove` (enum, nullable)
        Controls whether the mobile payment element displays the option to remove a saved payment method."

        Allowing buyers to remove their saved payment methods impacts subscriptions that depend on that payment method. Removing the payment method detaches the [`customer` object](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-customer) from that [PaymentMethod](https://docs.stripe.com/api/payment_methods.md).
Possible enum values:
        - `disabled`
          The feature is disabled.

        - `enabled`
          The feature is enabled.

      - `components.mobile_payment_element.features.payment_method_save` (enum, nullable)
        Controls whether the mobile payment element displays a checkbox offering to save a new payment method.

        If a customer checks the box, the [`allow_redisplay`](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay) value on the PaymentMethod is set to `'always'` at confirmation time. For PaymentIntents, the [`setup_future_usage`](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-setup_future_usage) value is also set to the value defined in `payment_method_save_usage`.
Possible enum values:
        - `disabled`
          The feature is disabled.

        - `enabled`
          The feature is enabled.

      - `components.mobile_payment_element.features.payment_method_save_allow_redisplay_override` (enum, nullable)
        Allows overriding the value of allow_override when saving a new payment method when payment_method_save is set to disabled. Use values: “always”, “limited”, or “unspecified”.

        If not specified, defaults to `nil` (no override value).
Possible enum values:
        - `always`
          Use `always` to indicate that this payment method can always be shown to a customer in a checkout flow.

        - `limited`
          Use `limited` to indicate that this payment method can’t always be shown to a customer in a checkout flow. For example, it can only be shown in the context of a specific subscription.

        - `unspecified`
          This is the default value for payment methods where `allow_redisplay` wasn’t set.

  - `components.payment_element` (object)
    Configuration for the Payment Element.

    - `components.payment_element.enabled` (boolean)
      Whether the Payment Element is enabled.

    - `components.payment_element.features` (object, nullable)
      This hash defines whether the Payment Element supports certain features.

      - `components.payment_element.features.payment_method_allow_redisplay_filters` (array of enums)
        A list of [`allow_redisplay`](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay) values that controls which saved payment methods the Payment Element displays by filtering to only show payment methods with an `allow_redisplay` value that is present in this list.

        If not specified, defaults to [“always”]. In order to display all saved payment methods, specify [“always”, “limited”, “unspecified”].
Possible enum values:
        - `always`
          Use `always` to indicate that this payment method can always be shown to a customer in a checkout flow.

        - `limited`
          Use `limited` to indicate that this payment method can’t always be shown to a customer in a checkout flow. For example, it can only be shown in the context of a specific subscription.

        - `unspecified`
          This is the default value for payment methods where `allow_redisplay` wasn’t set.

      - `components.payment_element.features.payment_method_redisplay` (enum)
        Controls whether or not the Payment Element shows saved payment methods. This parameter defaults to `disabled`.
Possible enum values:
        - `disabled`
          The feature is disabled.

        - `enabled`
          The feature is enabled.

      - `components.payment_element.features.payment_method_redisplay_limit` (integer, nullable)
        Determines the max number of saved payment methods for the Payment Element to display. This parameter defaults to `3`. The maximum redisplay limit is `10`.

      - `components.payment_element.features.payment_method_remove` (enum)
        Controls whether the Payment Element displays the option to remove a saved payment method.  This parameter defaults to `disabled`.

        Allowing buyers to remove their saved payment methods impacts subscriptions that depend on that payment method. Removing the payment method detaches the [`customer` object](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-customer) from that [PaymentMethod](https://docs.stripe.com/api/payment_methods.md).
Possible enum values:
        - `disabled`
          The feature is disabled.

        - `enabled`
          The feature is enabled.

      - `components.payment_element.features.payment_method_save` (enum)
        Controls whether the Payment Element displays a checkbox offering to save a new payment method. This parameter defaults to `disabled`.

        If a customer checks the box, the [`allow_redisplay`](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay) value on the PaymentMethod is set to `'always'` at confirmation time. For PaymentIntents, the [`setup_future_usage`](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-setup_future_usage) value is also set to the value defined in `payment_method_save_usage`.
Possible enum values:
        - `disabled`
          The feature is disabled.

        - `enabled`
          The feature is enabled.

      - `components.payment_element.features.payment_method_save_usage` (enum, nullable)
        When using PaymentIntents and the customer checks the save checkbox, this field determines the [`setup_future_usage`](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-setup_future_usage) value used to confirm the PaymentIntent.

        When using SetupIntents, directly configure the [`usage`](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-usage) value on SetupIntent creation.
Possible enum values:
        - `off_session`
          Use `off_session` if your customer may or may not be present in your checkout flow.

        - `on_session`
          Use `on_session` if you intend to only reuse the payment method when your customer is present in your checkout flow.

  - `components.pricing_table` (object)
    Configuration for the pricing table.

    - `components.pricing_table.enabled` (boolean)
      Whether the pricing table is enabled.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `customer` (string)
  The Customer the Customer Session was created for.

- `customer_account` (string, nullable)
  The Account that the Customer Session was created for.

- `expires_at` (timestamp)
  The timestamp at which this Customer Session will expire.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

### The Customer Session object

```json
{
  "object": "customer_session",
  "client_secret": "_POpxYpmkXdtttYtZQYhrsOJZ2RCQ9kCqqXRU6qrP5c4Jgje",
  "components": {
    "buy_button": {
      "enabled": false
    },
    "pricing_table": {
      "enabled": true
    }
  },
  "customer": "cus_PO34b57IOUb83c",
  "expires_at": 1684790027,
  "livemode": false
}
```