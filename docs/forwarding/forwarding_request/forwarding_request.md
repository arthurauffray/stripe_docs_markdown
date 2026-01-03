# Forwarding Request

Instructs Stripe to make a request on your behalf using the destination URL. The destination URL is activated by Stripe at the time of onboarding. Stripe verifies requests with your credentials provided during onboarding, and injects card details from the payment_method into the request.

Stripe redacts all sensitive fields and headers, including authentication credentials and card numbers, before storing the request and response data in the forwarding Request object, which are subject to a 30-day retention period.

You can provide a Stripe idempotency key to make sure that requests with the same key result in only one outbound request. The Stripe idempotency key provided should be unique and different from any idempotency keys provided on the underlying third-party request.

Forwarding Requests are synchronous requests that return a response or time out according to Stripe’s limits.

Related guide: [Forward card details to third-party API endpoints](https://docs.stripe.com/payments/forwarding.md).

## Endpoints

### Create a ForwardingRequest

- [POST /v1/forwarding/requests](https://docs.stripe.com/api/forwarding/forwarding_requests/create.md)

### Retrieve a ForwardingRequest

- [GET /v1/forwarding/requests/:id](https://docs.stripe.com/api/forwarding/forwarding_requests/retrieve.md)

### List all ForwardingRequests

- [GET /v1/forwarding/requests](https://docs.stripe.com/api/forwarding/forwarding_requests/list.md)