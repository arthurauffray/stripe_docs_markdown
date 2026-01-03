# Transfers

A `Transfer` object is created when you move funds between Stripe accounts as part of Connect.

Before April 6, 2017, transfers also represented movement of funds from a Stripe account to a card or bank account. This behavior has since been split out into a [Payout](https://docs.stripe.com/api/transfers.md#payout_object) object, with corresponding payout endpoints. For more information, read about the [transfer/payout split](https://docs.stripe.com/docs/transfer-payout-split.md).

Related guide: [Creating separate charges and transfers](https://docs.stripe.com/docs/connect/separate-charges-and-transfers.md)

## Endpoints

### Create a transfer

- [POST /v1/transfers](https://docs.stripe.com/api/transfers/create.md)

### Update a transfer

- [POST /v1/transfers/:id](https://docs.stripe.com/api/transfers/update.md)

### Retrieve a transfer

- [GET /v1/transfers/:id](https://docs.stripe.com/api/transfers/retrieve.md)

### List all transfers

- [GET /v1/transfers](https://docs.stripe.com/api/transfers/list.md)