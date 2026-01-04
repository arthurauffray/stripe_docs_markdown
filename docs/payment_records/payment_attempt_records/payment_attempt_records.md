# Payment Attempt Records

A Payment Attempt Record represents an individual attempt at making a payment, on or off Stripe. Each payment attempt tries to collect a fixed amount of money from a fixed customer and payment method. Payment Attempt Records are attached to Payment Records. Only one attempt per Payment Record can have guaranteed funds.

## Endpoints

### Retrieve a Payment Attempt Record

- [GET /v1/payment_attempt_records/:id](https://docs.stripe.com/api/payment-attempt-record/retrieve.md)

### List Payment Attempt Records

- [GET /v1/payment_attempt_records](https://docs.stripe.com/api/payment-attempt-record/list.md)