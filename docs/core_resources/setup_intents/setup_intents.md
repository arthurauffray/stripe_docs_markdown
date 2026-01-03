# Setup Intents

A SetupIntent guides you through the process of setting up and saving a customer’s payment credentials for future payments. For example, you can use a SetupIntent to set up and save your customer’s card without immediately collecting a payment. Later, you can use [PaymentIntents](https://docs.stripe.com/api/setup_intents.md#payment_intents) to drive the payment flow.

Create a SetupIntent when you’re ready to collect your customer’s payment credentials. Don’t maintain long-lived, unconfirmed SetupIntents because they might not be valid. The SetupIntent transitions through multiple [statuses](https://docs.stripe.com/payments/intents.md#intent-statuses) as it guides you through the setup process.

Successful SetupIntents result in payment credentials that are optimized for future payments. For example, cardholders in [certain regions](https://stripe.com/guides/strong-customer-authentication) might need to be run through [Strong Customer Authentication](https://docs.stripe.com/strong-customer-authentication.md) during payment method collection to streamline later [off-session payments](https://docs.stripe.com/payments/setup-intents.md). If you use the SetupIntent with a [Customer](https://docs.stripe.com/api/setup_intents.md#setup_intent_object-customer), it automatically attaches the resulting payment method to that Customer after successful setup. We recommend using SetupIntents or [setup_future_usage](https://docs.stripe.com/api/setup_intents.md#payment_intent_object-setup_future_usage) on PaymentIntents to save payment methods to prevent saving invalid or unoptimized payment methods.

By using SetupIntents, you can reduce friction for your customers, even as regulations change over time.

Related guide: [Setup Intents API](https://docs.stripe.com/payments/setup-intents.md)

## Endpoints

### Create a SetupIntent

- [POST /v1/setup_intents](https://docs.stripe.com/api/setup_intents/create.md)

### Update a SetupIntent

- [POST /v1/setup_intents/:id](https://docs.stripe.com/api/setup_intents/update.md)

### Retrieve a SetupIntent

- [GET /v1/setup_intents/:id](https://docs.stripe.com/api/setup_intents/retrieve.md)

### List all SetupIntents

- [GET /v1/setup_intents](https://docs.stripe.com/api/setup_intents/list.md)

### Cancel a SetupIntent

- [POST /v1/setup_intents/:id/cancel](https://docs.stripe.com/api/setup_intents/cancel.md)

### Confirm a SetupIntent

- [POST /v1/setup_intents/:id/confirm](https://docs.stripe.com/api/setup_intents/confirm.md)

### Verify microdeposits on a SetupIntent

- [POST /v1/setup_intents/:id/verify_microdeposits](https://docs.stripe.com/api/setup_intents/verify_microdeposits.md)