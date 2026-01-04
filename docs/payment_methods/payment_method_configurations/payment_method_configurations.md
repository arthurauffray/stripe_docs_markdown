# Payment Method Configurations

PaymentMethodConfigurations control which payment methods are displayed to your customers when you don’t explicitly specify payment method types. You can have multiple configurations with different sets of payment methods for different scenarios.

There are two types of PaymentMethodConfigurations. Which is used depends on the [charge type](https://docs.stripe.com/docs/connect/charges.md):

**Direct** configurations apply to payments created on your account, including Connect destination charges, Connect separate charges and transfers, and payments not involving Connect.

**Child** configurations apply to payments created on your connected accounts using direct charges, and charges with the on_behalf_of parameter.

Child configurations have a `parent` that sets default values and controls which settings connected accounts may override. You can specify a parent ID at payment time, and Stripe will automatically resolve the connected account’s associated child configuration. Parent configurations are [managed in the dashboard](https://dashboard.stripe.com/settings/payment_methods/connected_accounts) and are not available in this API.

Related guides:

- [Payment Method Configurations API](https://docs.stripe.com/docs/connect/payment-method-configurations.md)
- [Multiple configurations on dynamic payment methods](https://docs.stripe.com/docs/payments/multiple-payment-method-configs.md)
- [Multiple configurations for your Connect accounts](https://docs.stripe.com/docs/connect/multiple-payment-method-configurations.md)

## Endpoints

### Create a payment method configuration

- [POST /v1/payment_method_configurations](https://docs.stripe.com/api/payment_method_configurations/create.md)

### Update payment method configuration

- [POST /v1/payment_method_configurations/:id](https://docs.stripe.com/api/payment_method_configurations/update.md)

### Retrieve payment method configuration

- [GET /v1/payment_method_configurations/:id](https://docs.stripe.com/api/payment_method_configurations/retrieve.md)

### List payment method configurations

- [GET /v1/payment_method_configurations](https://docs.stripe.com/api/payment_method_configurations/list.md)