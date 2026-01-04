# Invoice Line Item

Invoice Line Items represent the individual lines within an [invoice](https://docs.stripe.com/docs/api/invoices.md) and only exist within the context of an invoice.

Each line item is backed by either an [invoice item](https://docs.stripe.com/docs/api/invoiceitems.md) or a [subscription item](https://docs.stripe.com/docs/api/subscription_items.md).

## Endpoints

### Update an invoice's line item

- [POST /v1/invoices/:id/lines/:id](https://docs.stripe.com/api/invoice-line-item/update.md)

### Retrieve an invoice's line items

- [GET /v1/invoices/:id/lines](https://docs.stripe.com/api/invoice-line-item/retrieve.md)

### Bulk add invoice line items

- [POST /v1/invoices/:id/add_lines](https://docs.stripe.com/api/invoice-line-item/bulk.md)

### Bulk remove invoice line items

- [POST /v1/invoices/:id/remove_lines](https://docs.stripe.com/api/invoice-line-item/invoices/remove-lines/bulk.md)

### Bulk update invoice line items

- [POST /v1/invoices/:id/update_lines](https://docs.stripe.com/api/invoice-line-item/invoices/update-lines/bulk.md)