# Bank Accounts

These bank accounts are payment methods on `Customer` objects.

On the other hand [External Accounts](https://docs.stripe.com/api.md#external_accounts) are transfer destinations on `Account` objects for connected accounts. They can be bank accounts or debit cards as well, and are documented in the links above.

Related guide: [Bank debits and transfers](https://docs.stripe.com/payments/bank-debits-transfers.md)

## Endpoints

### Create a bank account

- [POST /v1/customers/:id/sources](https://docs.stripe.com/api/customer_bank_accounts/create.md)

### Update a bank account

- [POST /v1/customers/:id/sources/:id](https://docs.stripe.com/api/customer_bank_accounts/update.md)

### Retrieve a bank account

- [GET /v1/customers/:id/bank_accounts/:id](https://docs.stripe.com/api/customer_bank_accounts/retrieve.md)

### List all bank accounts

- [GET /v1/customers/:id/bank_accounts](https://docs.stripe.com/api/customer_bank_accounts/list.md)

### Delete a bank account

- [DELETE /v1/customers/:id/sources/:id](https://docs.stripe.com/api/customer_bank_accounts/delete.md)

### Verify a bank account

- [POST /v1/customers/:id/sources/:id/verify](https://docs.stripe.com/api/customer_bank_accounts/verify.md)