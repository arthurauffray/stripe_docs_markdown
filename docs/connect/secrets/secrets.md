# Secrets

Secret Store is an API that allows Stripe Apps developers to securely persist secrets for use by UI Extensions and app backends.

The primary resource in Secret Store is a `secret`. Other apps can’t view secrets created by an app. Additionally, secrets are scoped to provide further permission control.

All Dashboard users and the app backend share `account` scoped secrets. Use the `account` scope for secrets that don’t change per-user, like a third-party API key.

A `user` scoped secret is accessible by the app backend and one specific Dashboard user. Use the `user` scope for per-user secrets like per-user OAuth tokens, where different users might have different permissions.

Related guide: [Store data between page reloads](https://docs.stripe.com/docs/stripe-apps/store-auth-data-custom-objects.md)

## Endpoints

### List secrets

- [GET /v1/apps/secrets](https://docs.stripe.com/api/apps/secret_store/list.md)

### Delete a Secret

- [POST /v1/apps/secrets/delete](https://docs.stripe.com/api/apps/secret_store/delete.md)

### Find a Secret

- [GET /v1/apps/secrets/find](https://docs.stripe.com/api/apps/secret_store/find.md)

### Set a Secret

- [POST /v1/apps/secrets](https://docs.stripe.com/api/apps/secret_store/set.md)