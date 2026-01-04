# Create a portal configuration

Creates a configuration that describes the functionality and behavior of a PortalSession

## Returns

Returns a portal configuration object.

## Parameters

- `features` (object, required)
  Information about the features available in the portal.

  - `features.customer_update` (object, optional)
    Information about updating the customer details in the portal.

    - `features.customer_update.enabled` (boolean, required)
      Whether the feature is enabled.

    - `features.customer_update.allowed_updates` (array of enums, optional)
      The types of customer updates that are supported. When empty, customers are not updateable.
Possible enum values:
      - `address`
        Allow updating billing addresses.

      - `email`
        Allow updating email addresses.

      - `name`
        Allow updating names.

      - `phone`
        Allow updating phone numbers.

      - `shipping`
        Allow updating shipping addresses.

      - `tax_id`
        Allow updating tax IDs.

  - `features.invoice_history` (object, optional)
    Information about showing the billing history in the portal.

    - `features.invoice_history.enabled` (boolean, required)
      Whether the feature is enabled.

  - `features.payment_method_update` (object, optional)
    Information about updating payment methods in the portal.

    - `features.payment_method_update.enabled` (boolean, required)
      Whether the feature is enabled.

    - `features.payment_method_update.payment_method_configuration` (string, optional)
      The [Payment Method Configuration](https://docs.stripe.com/api/payment_method_configurations.md) to use for this portal session. When specified, customers will be able to update their payment method to one of the options specified by the payment method configuration. If not set or set to an empty string, the default payment method configuration is used.

  - `features.subscription_cancel` (object, optional)
    Information about canceling subscriptions in the portal.

    - `features.subscription_cancel.enabled` (boolean, required)
      Whether the feature is enabled.

    - `features.subscription_cancel.cancellation_reason` (object, optional)
      Whether the cancellation reasons will be collected in the portal and which options are exposed to the customer

      - `features.subscription_cancel.cancellation_reason.enabled` (boolean, required)
        Whether the feature is enabled.

      - `features.subscription_cancel.cancellation_reason.options` (array of enums, required)
        Which cancellation reasons will be given as options to the customer.
Possible enum values:
        - `customer_service`
          Customer service was less than expected

        - `low_quality`
          Quality was less than expected

        - `missing_features`
          Some features are missing

        - `other`
          Other reason

        - `switched_service`
          I’m switching to a different service

        - `too_complex`
          Ease of use was less than expected

        - `too_expensive`
          It’s too expensive

        - `unused`
          I don’t use the service enough

    - `features.subscription_cancel.mode` (enum, optional)
      Whether to cancel subscriptions immediately or at the end of the billing period.
Possible enum values:
      - `at_period_end`
        After canceling, customers can still renew subscriptions until the billing period ends.

      - `immediately`
        Cancel subscriptions immediately.

    - `features.subscription_cancel.proration_behavior` (enum, optional)
      Whether to create prorations when canceling subscriptions. Possible values are `none` and `create_prorations`, which is only compatible with `mode=immediately`. Passing `always_invoice` will result in an error. No prorations are generated when canceling a subscription at the end of its natural billing period.
Possible enum values:
      - `always_invoice`
      - `create_prorations`
      - `none`

  - `features.subscription_update` (object, optional)
    Information about updating subscriptions in the portal.

    - `features.subscription_update.enabled` (boolean, required)
      Whether the feature is enabled.

    - `features.subscription_update.billing_cycle_anchor` (enum, optional)
      Determines the value to use for the billing cycle anchor on subscription updates. Valid values are `now` or `unchanged`, and the default value is `unchanged`. Setting the value to `now` resets the subscription’s billing cycle anchor to the current time (in UTC). For more information, see the billing cycle [documentation](https://docs.stripe.com/docs/billing/subscriptions/billing-cycle.md).
Possible enum values:
      - `now`
        Resets the subscription’s billing cycle anchor to the current time.

      - `unchanged`
        Keeps the subscription’s billing cycle anchor unchanged.

    - `features.subscription_update.default_allowed_updates` (array of enums, optional)
      The types of subscription updates that are supported. When empty, subscriptions are not updateable.
Possible enum values:
      - `price`
        Allow switching to a different price.

      - `promotion_code`
        Allow applying promotion codes to subscriptions.

      - `quantity`
        Allow updating subscription quantities.

    - `features.subscription_update.products` (array of objects, optional)
      The list of up to 10 products that support subscription updates.

      - `features.subscription_update.products.prices` (array of strings, required)
        The list of price IDs for the product that a subscription can be updated to.

      - `features.subscription_update.products.product` (string, required)
        The product id.

      - `features.subscription_update.products.adjustable_quantity` (object, optional)
        Control whether the quantity of the product can be adjusted.

        - `features.subscription_update.products.adjustable_quantity.enabled` (boolean, required)
          Set to true if the quantity can be adjusted to any non-negative integer.

        - `features.subscription_update.products.adjustable_quantity.maximum` (integer, optional)
          The maximum quantity that can be set for the product.

        - `features.subscription_update.products.adjustable_quantity.minimum` (integer, optional)
          The minimum quantity that can be set for the product.

    - `features.subscription_update.proration_behavior` (enum, optional)
      Determines how to handle prorations resulting from subscription updates. Valid values are `none`, `create_prorations`, and `always_invoice`.
Possible enum values:
      - `always_invoice`
      - `create_prorations`
      - `none`

    - `features.subscription_update.schedule_at_period_end` (object, optional)
      Setting to control when an update should be scheduled at the end of the period instead of applying immediately.

      - `features.subscription_update.schedule_at_period_end.conditions` (array of objects, optional)
        List of conditions. When any condition is true, the update will be scheduled at the end of the current period.

        - `features.subscription_update.schedule_at_period_end.conditions.type` (enum, required)
          The type of condition.
Possible enum values:
          - `decreasing_item_amount`
            Schedule the update when the subscription’s item amount decreases. This can happen when changing to a cheaper price or decreasing the quantity. This condition gets met if a subscription changes from a shorter billing period to a longer one and the resulting price is cheaper in the long term (for example, if the monthly price is 10 USD but the yearly price is 100 USD).

          - `shortening_interval`
            Schedule the update when the subscription’s interval is becoming shorter and no other changes to the subscription’s items are made. For example, this applies when changing from a yearly to monthly pricing interval.

    - `features.subscription_update.trial_update_behavior` (enum, optional)
      The behavior when updating a subscription that is trialing.
Possible enum values:
      - `continue_trial`
        Continue an existing trial when updating a subscription.

      - `end_trial`
        End the trial when updating a subscription.

- `business_profile` (object, optional)
  The business information shown to customers in the portal.

  - `business_profile.headline` (string, optional)
    The messaging shown to customers in the portal.

    The maximum length is 60 characters.

  - `business_profile.privacy_policy_url` (string, optional)
    A link to the business’s publicly available privacy policy.

  - `business_profile.terms_of_service_url` (string, optional)
    A link to the business’s publicly available terms of service.

- `default_return_url` (string, optional)
  The default URL to redirect customers to when they click on the portal’s link to return to your website. This can be [overriden](https://docs.stripe.com/docs/api/customer_portal/sessions/create.md#create_portal_session-return_url) when creating the session.

- `login_page` (object, optional)
  The hosted login page for this configuration. Learn more about the portal login page in our [integration docs](https://stripe.com/docs/billing/subscriptions/integrating-customer-portal#share).

  - `login_page.enabled` (boolean, required)
    Set to `true` to generate a shareable URL [`login_page.url`](https://docs.stripe.com/docs/api/customer_portal/configuration.md#portal_configuration_object-login_page-url) that will take your customers to a hosted login page for the customer portal.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `name` (string, optional)
  The name of the configuration.

  The maximum length is 256 characters.

```curl
curl https://api.stripe.com/v1/billing_portal/configurations \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "features[customer_update][allowed_updates][]"=email \
  -d "features[customer_update][allowed_updates][]"=tax_id \
  -d "features[customer_update][enabled]"=true \
  -d "features[invoice_history][enabled]"=true
```

```cli
stripe billing_portal configurations create  \
  -d "features[customer_update][allowed_updates][0]"=email \
  -d "features[customer_update][allowed_updates][1]"=tax_id \
  -d "features[customer_update][enabled]"=true \
  -d "features[invoice_history][enabled]"=true
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

configuration = client.v1.billing_portal.configurations.create({
  features: {
    customer_update: {
      allowed_updates: ['email', 'tax_id'],
      enabled: true,
    },
    invoice_history: {enabled: true},
  },
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

configuration = client.v1.billing_portal.configurations.create({
  "features": {
    "customer_update": {"allowed_updates": ["email", "tax_id"], "enabled": True},
    "invoice_history": {"enabled": True},
  },
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$configuration = $stripe->billingPortal->configurations->create([
  'features' => [
    'customer_update' => [
      'allowed_updates' => ['email', 'tax_id'],
      'enabled' => true,
    ],
    'invoice_history' => ['enabled' => true],
  ],
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ConfigurationCreateParams params =
  ConfigurationCreateParams.builder()
    .setFeatures(
      ConfigurationCreateParams.Features.builder()
        .setCustomerUpdate(
          ConfigurationCreateParams.Features.CustomerUpdate.builder()
            .addAllowedUpdate(
              ConfigurationCreateParams.Features.CustomerUpdate.AllowedUpdate.EMAIL
            )
            .addAllowedUpdate(
              ConfigurationCreateParams.Features.CustomerUpdate.AllowedUpdate.TAX_ID
            )
            .setEnabled(true)
            .build()
        )
        .setInvoiceHistory(
          ConfigurationCreateParams.Features.InvoiceHistory.builder()
            .setEnabled(true)
            .build()
        )
        .build()
    )
    .build();

Configuration configuration =
  client.v1().billingPortal().configurations().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const configuration = await stripe.billingPortal.configurations.create({
  features: {
    customer_update: {
      allowed_updates: ['email', 'tax_id'],
      enabled: true,
    },
    invoice_history: {
      enabled: true,
    },
  },
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.BillingPortalConfigurationCreateParams{
  Features: &stripe.BillingPortalConfigurationCreateFeaturesParams{
    CustomerUpdate: &stripe.BillingPortalConfigurationCreateFeaturesCustomerUpdateParams{
      AllowedUpdates: []*string{
        stripe.String(stripe.BillingPortalConfigurationFeaturesCustomerUpdateAllowedUpdateEmail),
        stripe.String(stripe.BillingPortalConfigurationFeaturesCustomerUpdateAllowedUpdateTaxID),
      },
      Enabled: stripe.Bool(true),
    },
    InvoiceHistory: &stripe.BillingPortalConfigurationCreateFeaturesInvoiceHistoryParams{
      Enabled: stripe.Bool(true),
    },
  },
}
result, err := sc.V1BillingPortalConfigurations.Create(context.TODO(), params)
```

```dotnet
var options = new Stripe.BillingPortal.ConfigurationCreateOptions
{
    Features = new Stripe.BillingPortal.ConfigurationFeaturesOptions
    {
        CustomerUpdate = new Stripe.BillingPortal.ConfigurationFeaturesCustomerUpdateOptions
        {
            AllowedUpdates = new List<string> { "email", "tax_id" },
            Enabled = true,
        },
        InvoiceHistory = new Stripe.BillingPortal.ConfigurationFeaturesInvoiceHistoryOptions
        {
            Enabled = true,
        },
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.BillingPortal.Configurations;
Stripe.BillingPortal.Configuration configuration = service.Create(options);
```

### Response

```json
{
  "id": "bpc_1MrnZsLkdIwHu7ixNiQL1xPM",
  "object": "billing_portal.configuration",
  "active": true,
  "application": null,
  "business_profile": {
    "headline": null,
    "privacy_policy_url": null,
    "terms_of_service_url": null
  },
  "created": 1680290736,
  "default_return_url": null,
  "features": {
    "customer_update": {
      "allowed_updates": [
        "email",
        "tax_id"
      ],
      "enabled": true
    },
    "invoice_history": {
      "enabled": true
    },
    "payment_method_update": {
      "enabled": false
    },
    "subscription_cancel": {
      "cancellation_reason": {
        "enabled": false,
        "options": [
          "too_expensive",
          "missing_features",
          "switched_service",
          "unused",
          "other"
        ]
      },
      "enabled": false,
      "mode": "at_period_end",
      "proration_behavior": "none"
    },
    "subscription_update": {
      "default_allowed_updates": [],
      "enabled": false,
      "proration_behavior": "none"
    }
  },
  "is_default": false,
  "livemode": false,
  "login_page": {
    "enabled": false,
    "url": null
  },
  "metadata": {},
  "updated": 1680290736
}
```