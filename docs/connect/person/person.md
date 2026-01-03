# Person

This is an object representing a person associated with a Stripe account.

A platform can only access a subset of data in a person for an account where [account.controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `stripe`, which includes Standard and Express accounts, after creating an Account Link or Account Session to start Connect onboarding.

See the [Standard onboarding](https://docs.stripe.com/connect/standard-accounts.md) or [Express onboarding](https://docs.stripe.com/connect/express-accounts.md) documentation for information about prefilling information and account onboarding steps. Learn more about [handling identity verification with the API](https://docs.stripe.com/connect/handling-api-verification.md#person-information).

## Endpoints

### Create a person

- [POST /v1/accounts/:id/persons](https://docs.stripe.com/api/persons/create.md)

### Update a person

- [POST /v1/accounts/:id/persons/:id](https://docs.stripe.com/api/persons/update.md)

### Retrieve a person

- [GET /v1/accounts/:id/persons/:id](https://docs.stripe.com/api/persons/retrieve.md)

### List all persons

- [GET /v1/accounts/:id/persons](https://docs.stripe.com/api/persons/list.md)

### Delete a person

- [DELETE /v1/accounts/:id/persons/:id](https://docs.stripe.com/api/persons/delete.md)