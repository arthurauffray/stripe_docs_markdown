# Transactions

Any use of an [issued card](https://docs.stripe.com/docs/issuing.md) that results in funds entering or leaving your Stripe account, such as a completed purchase or refund, is represented by an Issuing `Transaction` object.

Related guide: [Issued card transactions](https://docs.stripe.com/docs/issuing/purchases/transactions.md)

## Endpoints

### Update a transaction

- [POST /v1/issuing/transactions/:id](https://docs.stripe.com/api/issuing/transactions/update.md)

### Retrieve a transaction

- [GET /v1/issuing/transactions/:id](https://docs.stripe.com/api/issuing/transactions/retrieve.md)

### List all transactions

- [GET /v1/issuing/transactions](https://docs.stripe.com/api/issuing/transactions/list.md)

### Create a test-mode force capture

- [POST /v1/test_helpers/issuing/transactions/create_force_capture](https://docs.stripe.com/api/issuing/transactions/test_mode_create_force_capture.md)

### Create a test-mode unlinked refund

- [POST /v1/test_helpers/issuing/transactions/create_unlinked_refund](https://docs.stripe.com/api/issuing/transactions/test_mode_create_unlinked_refund.md)

### Refund a test-mode transaction

- [POST /v1/test_helpers/issuing/transactions/:id/refund](https://docs.stripe.com/api/issuing/transactions/test_mode_refund.md)