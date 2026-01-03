# Confirmation Token

ConfirmationTokens help transport client side data collected by Stripe JS over to your server for confirming a PaymentIntent or SetupIntent. If the confirmation is successful, values present on the ConfirmationToken are written onto the Intent.

To learn more about how to use ConfirmationToken, visit the related guides:

- [Finalize payments on the server](https://docs.stripe.com/docs/payments/finalize-payments-on-the-server.md)
- [Build two-step confirmation](https://docs.stripe.com/docs/payments/build-a-two-step-confirmation.md).

## Endpoints

### Retrieve a ConfirmationToken

- [GET /v1/confirmation_tokens/:id](https://docs.stripe.com/api/confirmation_tokens/retrieve.md)

### Create a test Confirmation Token

- [POST /v1/test_helpers/confirmation_tokens](https://docs.stripe.com/api/confirmation_tokens/test_create.md)