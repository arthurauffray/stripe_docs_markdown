# Plans

You can now model subscriptions more flexibly using the [Prices API](https://docs.stripe.com/api/plans.md#prices). It replaces the Plans API and is backwards compatible to simplify your migration.

Plans define the base price, currency, and billing cycle for recurring purchases of products. [Products](https://docs.stripe.com/api/plans.md#products) help you track inventory or provisioning, and plans help you track pricing. Different physical goods or levels of service should be represented by products, and pricing options should be represented by plans. This approach lets you change prices without having to change your provisioning scheme.

For example, you might have a single “gold” product that has plans for $10/month, $100/year, €9/month, and €90/year.

Related guides: [Set up a subscription](https://docs.stripe.com/docs/billing/subscriptions/set-up-subscription.md) and more about [products and prices](https://docs.stripe.com/docs/products-prices/overview.md).

## Endpoints

### Create a plan

- [POST /v1/plans](https://docs.stripe.com/api/plans/create.md)

### Update a plan

- [POST /v1/plans/:id](https://docs.stripe.com/api/plans/update.md)

### Retrieve a plan

- [GET /v1/plans/:id](https://docs.stripe.com/api/plans/retrieve.md)

### List all plans

- [GET /v1/plans](https://docs.stripe.com/api/plans/list.md)

### Delete a plan

- [DELETE /v1/plans/:id](https://docs.stripe.com/api/plans/delete.md)