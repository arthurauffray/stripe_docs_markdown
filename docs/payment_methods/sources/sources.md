# Sources

`Source` objects allow you to accept a variety of payment methods. They represent a customer’s payment instrument, and can be used with the Stripe API just like a `Card` object: once chargeable, they can be charged, or can be attached to customers.

Stripe doesn’t recommend using the deprecated [Sources API](https://docs.stripe.com/docs/api/sources.md). We recommend that you adopt the [PaymentMethods API](https://docs.stripe.com/docs/api/payment_methods.md). This newer API provides access to our latest features and payment method types.

Related guides: [Sources API](https://docs.stripe.com/docs/sources.md) and [Sources & Customers](https://docs.stripe.com/docs/sources/customers.md).

## Endpoints

### Create a source

- [POST /v1/sources](https://docs.stripe.com/api/sources/create.md)

### Update a source

- [POST /v1/sources/:id](https://docs.stripe.com/api/sources/update.md)

### Retrieve a source

- [GET /v1/sources/:id](https://docs.stripe.com/api/sources/retrieve.md)

### Attach a source

- [POST /v1/customers/:id/sources](https://docs.stripe.com/api/sources/attach.md)

### Detach a source

- [DELETE /v1/customers/:id/sources/:id](https://docs.stripe.com/api/sources/detach.md)