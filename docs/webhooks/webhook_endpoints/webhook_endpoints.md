# Webhook Endpoints

You can configure [webhook endpoints](https://docs.stripe.com/webhooks/.md) via the API to be notified about events that happen in your Stripe account or connected accounts.

Most users configure webhooks from [the dashboard](https://dashboard.stripe.com/webhooks), which provides a user interface for registering and testing your webhook endpoints.

Related guide: [Setting up webhooks](https://docs.stripe.com/webhooks/configure.md)

## Endpoints

### Create a webhook endpoint

- [POST /v1/webhook_endpoints](https://docs.stripe.com/api/webhook_endpoints/create.md)

### Update a webhook endpoint

- [POST /v1/webhook_endpoints/:id](https://docs.stripe.com/api/webhook_endpoints/update.md)

### Retrieve a webhook endpoint

- [GET /v1/webhook_endpoints/:id](https://docs.stripe.com/api/webhook_endpoints/retrieve.md)

### List all webhook endpoints

- [GET /v1/webhook_endpoints](https://docs.stripe.com/api/webhook_endpoints/list.md)

### Delete a webhook endpoint

- [DELETE /v1/webhook_endpoints/:id](https://docs.stripe.com/api/webhook_endpoints/delete.md)