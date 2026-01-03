# Create a Customer Session

Creates a Customer Session object that includes a single-use client secret that you can use on your front-end to grant client-side API access for certain customer resources.

## Returns

Returns a Customer Session object.

## Parameters

- `components` (object, required)
  Configuration for each component. At least 1 component must be enabled.

  - `components.buy_button` (object, optional)
    Configuration for buy button.

    - `components.buy_button.enabled` (boolean, required)
      Whether the buy button is enabled.

  - `components.customer_sheet` (object, optional)
    Configuration for the customer sheet.

    - `components.customer_sheet.enabled` (boolean, required)
      Whether the customer sheet is enabled.

    - `components.customer_sheet.features` (object, optional)
      This hash defines whether the customer sheet supports certain features.

      - `components.customer_sheet.features.payment_method_allow_redisplay_filters` (array of enums, optional)
        A list of [`allow_redisplay`](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay) values that controls which saved payment methods the customer sheet displays by filtering to only show payment methods with an `allow_redisplay` value that is present in this list.

        If not specified, defaults to [“always”]. In order to display all saved payment methods, specify [“always”, “limited”, “unspecified”].
Possible enum values:
        - `always`
          Use `always` to indicate that this payment method can always be shown to a customer in a checkout flow.

        - `limited`
          Use `limited` to indicate that this payment method can’t always be shown to a customer in a checkout flow. For example, it can only be shown in the context of a specific subscription.

        - `unspecified`
          This is the default value for payment methods where `allow_redisplay` wasn’t set.

      - `components.customer_sheet.features.payment_method_remove` (enum, optional)
        Controls whether the customer sheet displays the option to remove a saved payment method."

        Allowing buyers to remove their saved payment methods impacts subscriptions that depend on that payment method. Removing the payment method detaches the [`customer` object](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-customer) from that [PaymentMethod](https://docs.stripe.com/api/payment_methods.md).
Possible enum values:
        - `disabled`
          The feature is disabled.

        - `enabled`
          The feature is enabled.

  - `components.mobile_payment_element` (object, optional)
    Configuration for the mobile payment element.

    - `components.mobile_payment_element.enabled` (boolean, required)
      Whether the mobile payment element is enabled.

    - `components.mobile_payment_element.features` (object, optional)
      This hash defines whether the mobile payment element supports certain features.

      - `components.mobile_payment_element.features.payment_method_allow_redisplay_filters` (array of enums, optional)
        A list of [`allow_redisplay`](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay) values that controls which saved payment methods the mobile payment element displays by filtering to only show payment methods with an `allow_redisplay` value that is present in this list.

        If not specified, defaults to [“always”]. In order to display all saved payment methods, specify [“always”, “limited”, “unspecified”].
Possible enum values:
        - `always`
          Use `always` to indicate that this payment method can always be shown to a customer in a checkout flow.

        - `limited`
          Use `limited` to indicate that this payment method can’t always be shown to a customer in a checkout flow. For example, it can only be shown in the context of a specific subscription.

        - `unspecified`
          This is the default value for payment methods where `allow_redisplay` wasn’t set.

      - `components.mobile_payment_element.features.payment_method_redisplay` (enum, optional)
        Controls whether or not the mobile payment element shows saved payment methods.
Possible enum values:
        - `disabled`
          The feature is disabled.

        - `enabled`
          The feature is enabled.

      - `components.mobile_payment_element.features.payment_method_remove` (enum, optional)
        Controls whether the mobile payment element displays the option to remove a saved payment method."

        Allowing buyers to remove their saved payment methods impacts subscriptions that depend on that payment method. Removing the payment method detaches the [`customer` object](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-customer) from that [PaymentMethod](https://docs.stripe.com/api/payment_methods.md).
Possible enum values:
        - `disabled`
          The feature is disabled.

        - `enabled`
          The feature is enabled.

      - `components.mobile_payment_element.features.payment_method_save` (enum, optional)
        Controls whether the mobile payment element displays a checkbox offering to save a new payment method.

        If a customer checks the box, the [`allow_redisplay`](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay) value on the PaymentMethod is set to `'always'` at confirmation time. For PaymentIntents, the [`setup_future_usage`](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-setup_future_usage) value is also set to the value defined in `payment_method_save_usage`.
Possible enum values:
        - `disabled`
          The feature is disabled.

        - `enabled`
          The feature is enabled.

      - `components.mobile_payment_element.features.payment_method_save_allow_redisplay_override` (enum, optional)
        Allows overriding the value of allow_override when saving a new payment method when payment_method_save is set to disabled. Use values: “always”, “limited”, or “unspecified”.

        If not specified, defaults to `nil` (no override value).
Possible enum values:
        - `always`
          Use `always` to indicate that this payment method can always be shown to a customer in a checkout flow.

        - `limited`
          Use `limited` to indicate that this payment method can’t always be shown to a customer in a checkout flow. For example, it can only be shown in the context of a specific subscription.

        - `unspecified`
          This is the default value for payment methods where `allow_redisplay` wasn’t set.

  - `components.payment_element` (object, optional)
    Configuration for the Payment Element.

    - `components.payment_element.enabled` (boolean, required)
      Whether the Payment Element is enabled.

    - `components.payment_element.features` (object, optional)
      This hash defines whether the Payment Element supports certain features.

      - `components.payment_element.features.payment_method_allow_redisplay_filters` (array of enums, optional)
        A list of [`allow_redisplay`](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay) values that controls which saved payment methods the Payment Element displays by filtering to only show payment methods with an `allow_redisplay` value that is present in this list.

        If not specified, defaults to [“always”]. In order to display all saved payment methods, specify [“always”, “limited”, “unspecified”].
Possible enum values:
        - `always`
          Use `always` to indicate that this payment method can always be shown to a customer in a checkout flow.

        - `limited`
          Use `limited` to indicate that this payment method can’t always be shown to a customer in a checkout flow. For example, it can only be shown in the context of a specific subscription.

        - `unspecified`
          This is the default value for payment methods where `allow_redisplay` wasn’t set.

      - `components.payment_element.features.payment_method_redisplay` (enum, optional)
        Controls whether or not the Payment Element shows saved payment methods. This parameter defaults to `disabled`.
Possible enum values:
        - `disabled`
          The feature is disabled.

        - `enabled`
          The feature is enabled.

      - `components.payment_element.features.payment_method_redisplay_limit` (integer, optional)
        Determines the max number of saved payment methods for the Payment Element to display. This parameter defaults to `3`. The maximum redisplay limit is `10`.

      - `components.payment_element.features.payment_method_remove` (enum, optional)
        Controls whether the Payment Element displays the option to remove a saved payment method.  This parameter defaults to `disabled`.

        Allowing buyers to remove their saved payment methods impacts subscriptions that depend on that payment method. Removing the payment method detaches the [`customer` object](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-customer) from that [PaymentMethod](https://docs.stripe.com/api/payment_methods.md).
Possible enum values:
        - `disabled`
          The feature is disabled.

        - `enabled`
          The feature is enabled.

      - `components.payment_element.features.payment_method_save` (enum, optional)
        Controls whether the Payment Element displays a checkbox offering to save a new payment method. This parameter defaults to `disabled`.

        If a customer checks the box, the [`allow_redisplay`](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay) value on the PaymentMethod is set to `'always'` at confirmation time. For PaymentIntents, the [`setup_future_usage`](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-setup_future_usage) value is also set to the value defined in `payment_method_save_usage`.
Possible enum values:
        - `disabled`
          The feature is disabled.

        - `enabled`
          The feature is enabled.

      - `components.payment_element.features.payment_method_save_usage` (enum, required if payment_method_save=enabled)
        When using PaymentIntents and the customer checks the save checkbox, this field determines the [`setup_future_usage`](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-setup_future_usage) value used to confirm the PaymentIntent.

        When using SetupIntents, directly configure the [`usage`](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-usage) value on SetupIntent creation.
Possible enum values:
        - `off_session`
          Use `off_session` if your customer may or may not be present in your checkout flow.

        - `on_session`
          Use `on_session` if you intend to only reuse the payment method when your customer is present in your checkout flow.

  - `components.pricing_table` (object, optional)
    Configuration for the pricing table.

    - `components.pricing_table.enabled` (boolean, required)
      Whether the pricing table is enabled.

- `customer` (string, optional)
  The ID of an existing customer for which to create the Customer Session.

- `customer_account` (string, optional)
  The ID of an existing Account for which to create the Customer Session.

```curl
curl https://api.stripe.com/v1/customer_sessions \
  -u "<<YOUR_SECRET_KEY>>" \
  -d customer=cus_PO34b57IOUb83c \
  -d "components[pricing_table][enabled]"=true
```

```cli
stripe customer_sessions create  \
  --customer=cus_PO34b57IOUb83c \
  -d "components[pricing_table][enabled]"=true
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

customer_session = client.v1.customer_sessions.create({
  customer: 'cus_PO34b57IOUb83c',
  components: {pricing_table: {enabled: true}},
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

customer_session = client.v1.customer_sessions.create({
  "customer": "cus_PO34b57IOUb83c",
  "components": {"pricing_table": {"enabled": True}},
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$customerSession = $stripe->customerSessions->create([
  'customer' => 'cus_PO34b57IOUb83c',
  'components' => ['pricing_table' => ['enabled' => true]],
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CustomerSessionCreateParams params =
  CustomerSessionCreateParams.builder()
    .setCustomer("cus_PO34b57IOUb83c")
    .setComponents(
      CustomerSessionCreateParams.Components.builder()
        .setPricingTable(
          CustomerSessionCreateParams.Components.PricingTable.builder()
            .setEnabled(true)
            .build()
        )
        .build()
    )
    .build();

CustomerSession customerSession = client.v1().customerSessions().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customerSession = await stripe.customerSessions.create({
  customer: 'cus_PO34b57IOUb83c',
  components: {
    pricing_table: {
      enabled: true,
    },
  },
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CustomerSessionCreateParams{
  Customer: stripe.String("cus_PO34b57IOUb83c"),
  Components: &stripe.CustomerSessionCreateComponentsParams{
    PricingTable: &stripe.CustomerSessionCreateComponentsPricingTableParams{
      Enabled: stripe.Bool(true),
    },
  },
}
result, err := sc.V1CustomerSessions.Create(context.TODO(), params)
```

```dotnet
var options = new CustomerSessionCreateOptions
{
    Customer = "cus_PO34b57IOUb83c",
    Components = new CustomerSessionComponentsOptions
    {
        PricingTable = new CustomerSessionComponentsPricingTableOptions
        {
            Enabled = true,
        },
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.CustomerSessions;
CustomerSession customerSession = service.Create(options);
```

### Response

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