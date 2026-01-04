# Invoice Payment

Invoice Payments represent payments made against invoices. Invoice Payments can be accessed in two ways:

1. By expanding the `payments` field on the [Invoice](https://docs.stripe.com/api/invoice-payment.md#invoice) resource.
1. By using the Invoice Payment retrieve and list endpoints.

Invoice Payments include the mapping between payment objects, such as Payment Intent, and Invoices. This resource and its endpoints allows you to easily track if a payment is associated with a specific invoice and monitor the allocation details of the payments.

## Endpoints

### Retrieve an InvoicePayment

- [GET /v1/invoice_payments/:id](https://docs.stripe.com/api/invoice-payment/retrieve.md)

### List all payments for an invoice

- [GET /v1/invoice_payments](https://docs.stripe.com/api/invoice-payment/list.md)