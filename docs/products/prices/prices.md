# Prices

Prices define the unit cost, currency, and (optional) billing cycle for both recurring and one-time purchases of products. [Products](https://docs.stripe.com/api/prices.md#products) help you track inventory or provisioning, and prices help you track payment terms. Different physical goods or levels of service should be represented by products, and pricing options should be represented by prices. This approach lets you change prices without having to change your provisioning scheme.

For example, you might have a single “gold” product that has prices for $10/month, $100/year, and €9 once.

Related guides: [Set up a subscription](https://docs.stripe.com/docs/billing/subscriptions/set-up-subscription.md), [create an invoice](https://docs.stripe.com/docs/billing/invoices/create.md), and more about [products and prices](https://docs.stripe.com/docs/products-prices/overview.md).

## Endpoints

### Create a price

- [POST /v1/prices](https://docs.stripe.com/api/prices/create.md)

### Update a price

- [POST /v1/prices/:id](https://docs.stripe.com/api/prices/update.md)

### Retrieve a price

- [GET /v1/prices/:id](https://docs.stripe.com/api/prices/retrieve.md)

### List all prices

- [GET /v1/prices](https://docs.stripe.com/api/prices/list.md)

### Search prices

- [GET /v1/prices/search](https://docs.stripe.com/api/prices/search.md)