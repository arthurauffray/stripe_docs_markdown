# Coupons

A coupon contains information about a percent-off or amount-off discount you might want to apply to a customer. Coupons may be applied to [subscriptions](https://docs.stripe.com/api/coupons.md#subscriptions), [invoices](https://docs.stripe.com/api/coupons.md#invoices), [checkout sessions](https://docs.stripe.com/docs/api/checkout/sessions.md), [quotes](https://docs.stripe.com/api/coupons.md#quotes), and more. Coupons do not work with conventional one-off [charges](https://docs.stripe.com/api/coupons.md#create_charge) or [payment intents](https://docs.stripe.com/docs/api/payment_intents.md).

## Endpoints

### Create a coupon

- [POST /v1/coupons](https://docs.stripe.com/api/coupons/create.md)

### Update a coupon

- [POST /v1/coupons/:id](https://docs.stripe.com/api/coupons/update.md)

### Retrieve a coupon

- [GET /v1/coupons/:id](https://docs.stripe.com/api/coupons/retrieve.md)

### List all coupons

- [GET /v1/coupons](https://docs.stripe.com/api/coupons/list.md)

### Delete a coupon

- [DELETE /v1/coupons/:id](https://docs.stripe.com/api/coupons/delete.md)