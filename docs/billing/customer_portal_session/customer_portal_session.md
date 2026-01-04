# Customer Portal Session

The Billing customer portal is a Stripe-hosted UI for subscription and billing management.

A portal configuration describes the functionality and features that you want to provide to your customers through the portal.

A portal session describes the instantiation of the customer portal for a particular customer. By visiting the session’s URL, the customer can manage their subscriptions and billing details. For security reasons, sessions are short-lived and will expire if the customer does not visit the URL. Create sessions on-demand when customers intend to manage their subscriptions and billing details.

Related guide: [Customer management](https://docs.stripe.com/customer-management.md)

## Endpoints

### Create a portal session

- [POST /v1/billing_portal/sessions](https://docs.stripe.com/api/customer_portal/sessions/create.md)