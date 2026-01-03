# Application Fee Refunds

`Application Fee Refund` objects allow you to refund an application fee that has previously been created but not yet refunded. Funds will be refunded to the Stripe account from which the fee was originally collected.

Related guide: [Refunding application fees](https://docs.stripe.com/docs/connect/destination-charges.md#refunding-app-fee)

## Endpoints

### Create an application fee refund

- [POST /v1/application_fees/:id/refunds](https://docs.stripe.com/api/fee_refunds/create.md)

### Update an application fee refund

- [POST /v1/application_fees/:id/refunds/:id](https://docs.stripe.com/api/fee_refunds/update.md)

### Retrieve an application fee refund

- [GET /v1/application_fees/:id/refunds/:id](https://docs.stripe.com/api/fee_refunds/retrieve.md)

### List all application fee refunds

- [GET /v1/application_fees/:id/refunds](https://docs.stripe.com/api/fee_refunds/list.md)