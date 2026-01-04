# Cash Balance Transaction

Customers with certain payments enabled have a cash balance, representing funds that were paid by the customer to a merchant, but have not yet been allocated to a payment. Cash Balance Transactions represent when funds are moved into or out of this balance. This includes funding by the customer, allocation to payments, and refunds to the customer.

## Endpoints

### Create or retrieve funding instructions for a customer cash balance

- [POST /v1/customers/:id/funding_instructions](https://docs.stripe.com/api/cash_balance_transactions/create_or_retrieve_funding_instructions.md)

### Retrieve a cash balance transaction

- [GET /v1/customers/:id/cash_balance_transactions/:id](https://docs.stripe.com/api/cash_balance_transactions/retrieve.md)

### List cash balance transactions

- [GET /v1/customers/:id/cash_balance_transactions](https://docs.stripe.com/api/cash_balance_transactions/list.md)

### Fund a test mode cash balance

- [POST /v1/test_helpers/customers/:id/fund_cash_balance](https://docs.stripe.com/api/cash_balance_transactions/fund_cash_balance.md)