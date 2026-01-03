# Accounts

This is an object representing a Stripe account. You can retrieve it to see properties on the account like its current requirements or if the account is enabled to make live charges or receive payouts.

For accounts where [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `application`, which includes Custom accounts, the properties below are always returned.

For accounts where [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `stripe`, which includes Standard and Express accounts, some properties are only returned until you create an [Account Link](https://docs.stripe.com/api/account_links.md) or [Account Session](https://docs.stripe.com/api/account_sessions.md) to start Connect Onboarding. Learn about the [differences between accounts](https://docs.stripe.com/connect/accounts.md).

## Endpoints

### Create an account

- [POST /v1/accounts](https://docs.stripe.com/api/accounts/create.md)

### Update an account

- [POST /v1/accounts/:id](https://docs.stripe.com/api/accounts/update.md)

### Retrieve account

- [GET /v1/accounts/:id](https://docs.stripe.com/api/accounts/retrieve.md)

### List all connected accounts

- [GET /v1/accounts](https://docs.stripe.com/api/accounts/list.md)

### Delete an account

- [DELETE /v1/accounts/:id](https://docs.stripe.com/api/accounts/delete.md)

### Reject an account

- [POST /v1/accounts/:id/reject](https://docs.stripe.com/api/account/reject.md)