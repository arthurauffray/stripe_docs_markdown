# Payment Method Domains

A payment method domain represents a web domain that you have registered with Stripe. Stripe Elements use registered payment method domains to control where certain payment methods are shown.

Related guide: [Payment method domains](https://docs.stripe.com/docs/payments/payment-methods/pmd-registration.md).

## Endpoints

### Create a payment method domain

- [POST /v1/payment_method_domains](https://docs.stripe.com/api/payment_method_domains/create.md)

### Update a payment method domain

- [POST /v1/payment_method_domains/:id](https://docs.stripe.com/api/payment_method_domains/update.md)

### Retrieve a payment method domain

- [GET /v1/payment_method_domains/:id](https://docs.stripe.com/api/payment_method_domains/retrieve.md)

### List payment method domains

- [GET /v1/payment_method_domains](https://docs.stripe.com/api/payment_method_domains/list.md)

### Validate an existing payment method domain

- [POST /v1/payment_method_domains/:id/validate](https://docs.stripe.com/api/payment_method_domains/validate.md)