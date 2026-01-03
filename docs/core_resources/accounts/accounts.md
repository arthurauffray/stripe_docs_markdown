# Accounts

An Account v2 object represents a company, individual, or other entity that interacts with a platform on Stripe. It contains both identifying information and properties that control its behavior and functionality. An Account can have one or more configurations that enable sets of related features, such as allowing it to act as a merchant or customer.

The Accounts v2 API is generally available for [Connect](https://docs.stripe.com/connect/accounts-v2.md) and supports the [Global Payouts](https://docs.stripe.com/global-payouts.md) public preview.

## Endpoints

### Create an account

- [POST /v2/core/accounts](https://docs.stripe.com/api/v2/core/accounts/create.md)

### Update an account

- [POST /v2/core/accounts/:id](https://docs.stripe.com/api/v2/core/accounts/update.md)

### Retrieve an account

- [GET /v2/core/accounts/:id](https://docs.stripe.com/api/v2/core/accounts/retrieve.md)

### List accounts

- [GET /v2/core/accounts](https://docs.stripe.com/api/v2/core/accounts/list.md)

### Close an account

- [POST /v2/core/accounts/:id/close](https://docs.stripe.com/api/v2/core/accounts/close.md)