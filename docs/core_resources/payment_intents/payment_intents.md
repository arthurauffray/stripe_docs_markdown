# Payment Intents

A PaymentIntent guides you through the process of collecting a payment from your customer. We recommend that you create exactly one PaymentIntent for each order or customer session in your system. You can reference the PaymentIntent later to see the history of payment attempts for a particular session.

A PaymentIntent transitions through [multiple statuses](https://docs.stripe.com/payments/paymentintents/lifecycle.md) throughout its lifetime as it interfaces with Stripe.js to perform authentication flows and ultimately creates at most one successful charge.

Related guide: [Payment Intents API](https://docs.stripe.com/docs/payments/payment-intents.md)

## Endpoints

### Create a PaymentIntent

- [POST /v1/payment_intents](https://docs.stripe.com/api/payment_intents/create.md)

### Update a PaymentIntent

- [POST /v1/payment_intents/:id](https://docs.stripe.com/api/payment_intents/update.md)

### Retrieve a PaymentIntent

- [GET /v1/payment_intents/:id](https://docs.stripe.com/api/payment_intents/retrieve.md)

### List all PaymentIntent LineItems

- [GET /v1/payment_intents/:id/amount_details_line_items](https://docs.stripe.com/api/payment_intents/amount_details_line_items.md)

### List all PaymentIntents

- [GET /v1/payment_intents](https://docs.stripe.com/api/payment_intents/list.md)

### Cancel a PaymentIntent

- [POST /v1/payment_intents/:id/cancel](https://docs.stripe.com/api/payment_intents/cancel.md)

### Capture a PaymentIntent

- [POST /v1/payment_intents/:id/capture](https://docs.stripe.com/api/payment_intents/capture.md)

### Confirm a PaymentIntent

- [POST /v1/payment_intents/:id/confirm](https://docs.stripe.com/api/payment_intents/confirm.md)

### Increment an authorization

- [POST /v1/payment_intents/:id/increment_authorization](https://docs.stripe.com/api/payment_intents/increment_authorization.md)

### Reconcile a customer_balance PaymentIntent

- [POST /v1/payment_intents/:id/apply_customer_balance](https://docs.stripe.com/api/payment_intents/apply_customer_balance.md)

### Search PaymentIntents

- [GET /v1/payment_intents/search](https://docs.stripe.com/api/payment_intents/search.md)

### Verify microdeposits on a PaymentIntent

- [POST /v1/payment_intents/:id/verify_microdeposits](https://docs.stripe.com/api/payment_intents/verify_microdeposits.md)