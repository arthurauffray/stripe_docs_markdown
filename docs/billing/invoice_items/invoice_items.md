# Invoice Items

Invoice Items represent the component lines of an [invoice](https://docs.stripe.com/docs/api/invoices.md). When you create an invoice item with an `invoice` field, it is attached to the specified invoice and included as [an invoice line item](https://docs.stripe.com/docs/api/invoices/line_item.md) within [invoice.lines](https://docs.stripe.com/docs/api/invoices/object.md#invoice_object-lines).

Invoice Items can be created before you are ready to actually send the invoice. This can be particularly useful when combined with a [subscription](https://docs.stripe.com/docs/api/subscriptions.md). Sometimes you want to add a charge or credit to a customer, but actually charge or credit the customer’s card only at the end of a regular billing cycle. This is useful for combining several charges (to minimize per-transaction fees), or for having Stripe tabulate your usage-based billing totals.

Related guides: [Integrate with the Invoicing API](https://docs.stripe.com/docs/invoicing/integration.md), [Subscription Invoices](https://docs.stripe.com/docs/billing/invoices/subscription.md#adding-upcoming-invoice-items).

## Endpoints

### Create an invoice item

- [POST /v1/invoiceitems](https://docs.stripe.com/api/invoiceitems/create.md)

### Update an invoice item

- [POST /v1/invoiceitems/:id](https://docs.stripe.com/api/invoiceitems/update.md)

### Retrieve an invoice item

- [GET /v1/invoiceitems/:id](https://docs.stripe.com/api/invoiceitems/retrieve.md)

### List all invoice items

- [GET /v1/invoiceitems](https://docs.stripe.com/api/invoiceitems/list.md)

### Delete an invoice item

- [DELETE /v1/invoiceitems/:id](https://docs.stripe.com/api/invoiceitems/delete.md)