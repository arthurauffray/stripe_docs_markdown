# Tax IDs

You can add one or multiple tax IDs to a [customer](https://docs.stripe.com/docs/api/customers.md) or account. Customer and account tax IDs get displayed on related invoices and credit notes.

Related guides: [Customer tax identification numbers](https://docs.stripe.com/docs/billing/taxes/tax-ids.md), [Account tax IDs](https://docs.stripe.com/docs/invoicing/connect.md#account-tax-ids)

## Endpoints

### Create a Customer tax ID

- [POST /v1/customers/:id/tax_ids](https://docs.stripe.com/api/tax_ids/customer_create.md)

### Create a tax ID

- [POST /v1/tax_ids](https://docs.stripe.com/api/tax_ids/create.md)

### Retrieve a Customer tax ID

- [GET /v1/customers/:id/tax_ids/:id](https://docs.stripe.com/api/tax_ids/customer_retrieve.md)

### Retrieve a tax ID

- [GET /v1/tax_ids/:id](https://docs.stripe.com/api/tax_ids/retrieve.md)

### List all Customer tax IDs

- [GET /v1/customers/:id/tax_ids](https://docs.stripe.com/api/tax_ids/customer_list.md)

### List all tax IDs

- [GET /v1/tax_ids](https://docs.stripe.com/api/tax_ids/list.md)

### Delete a Customer tax ID

- [DELETE /v1/customers/:id/tax_ids/:id](https://docs.stripe.com/api/tax_ids/customer_delete.md)

### Delete a tax ID

- [DELETE /v1/tax_ids/:id](https://docs.stripe.com/api/tax_ids/delete.md)