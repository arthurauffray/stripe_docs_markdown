# Login Links

Login Links are single-use URLs that takes an Express account to the login page for their Stripe dashboard. A Login Link differs from an [Account Link](https://docs.stripe.com/docs/api/account_links.md) in that it takes the user directly to their [Express dashboard for the specified account](https://docs.stripe.com/docs/connect/integrate-express-dashboard.md#create-login-link)

## Endpoints

### Create a login link

- [POST /v1/accounts/:id/login_links](https://docs.stripe.com/api/accounts/login_link/create.md)