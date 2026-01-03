# Promotion Code

A Promotion Code represents a customer-redeemable code for an underlying promotion. You can create multiple codes for a single promotion.

If you enable promotion codes in your [customer portal configuration](https://docs.stripe.com/docs/customer-management/configure-portal.md), then customers can redeem a code themselves when updating a subscription in the portal. Customers can also view the currently active promotion codes and coupons on each of their subscriptions in the portal.

## Endpoints

### Create a promotion code

- [POST /v1/promotion_codes](https://docs.stripe.com/api/promotion_codes/create.md)

### Update a promotion code

- [POST /v1/promotion_codes/:id](https://docs.stripe.com/api/promotion_codes/update.md)

### Retrieve a promotion code

- [GET /v1/promotion_codes/:id](https://docs.stripe.com/api/promotion_codes/retrieve.md)

### List all promotion codes

- [GET /v1/promotion_codes](https://docs.stripe.com/api/promotion_codes/list.md)