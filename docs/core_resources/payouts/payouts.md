# Payouts

A `Payout` object is created when you receive funds from Stripe, or when you initiate a payout to either a bank account or debit card of a [connected Stripe account](https://docs.stripe.com/docs/connect/bank-debit-card-payouts.md). You can retrieve individual payouts, and list all payouts. Payouts are made on [varying schedules](https://docs.stripe.com/docs/connect/manage-payout-schedule.md), depending on your country and industry.

Related guide: [Receiving payouts](https://docs.stripe.com/docs/payouts.md)

## Endpoints

### Create a payout

- [POST /v1/payouts](https://docs.stripe.com/api/payouts/create.md)

### Update a payout

- [POST /v1/payouts/:id](https://docs.stripe.com/api/payouts/update.md)

### Retrieve a payout

- [GET /v1/payouts/:id](https://docs.stripe.com/api/payouts/retrieve.md)

### List all payouts

- [GET /v1/payouts](https://docs.stripe.com/api/payouts/list.md)

### Cancel a payout

- [POST /v1/payouts/:id/cancel](https://docs.stripe.com/api/payouts/cancel.md)

### Reverse a payout

- [POST /v1/payouts/:id/reverse](https://docs.stripe.com/api/payouts/reverse.md)