# Transfer Reversals

[Stripe Connect](https://docs.stripe.com/docs/connect.md) platforms can reverse transfers made to a connected account, either entirely or partially, and can also specify whether to refund any related application fees. Transfer reversals add to the platform’s balance and subtract from the destination account’s balance.

Reversing a transfer that was made for a [destination charge](https://docs.stripe.com/docs/connect/destination-charges.md) is allowed only up to the amount of the charge. It is possible to reverse a [transfer_group](https://docs.stripe.com/docs/connect/separate-charges-and-transfers.md#transfer-options) transfer only if the destination account has enough balance to cover the reversal.

Related guide: [Reverse transfers](https://docs.stripe.com/docs/connect/separate-charges-and-transfers.md#reverse-transfers)

## Endpoints

### Create a transfer reversal

- [POST /v1/transfers/:id/reversals](https://docs.stripe.com/api/transfer_reversals/create.md)

### Update a reversal

- [POST /v1/transfers/:id/reversals/:id](https://docs.stripe.com/api/transfer_reversals/update.md)

### Retrieve a reversal

- [GET /v1/transfers/:id/reversals/:id](https://docs.stripe.com/api/transfer_reversals/retrieve.md)

### List all reversals

- [GET /v1/transfers/:id/reversals](https://docs.stripe.com/api/transfer_reversals/list.md)