# Payment Records

A Payment Record is a resource that allows you to represent payments that occur on- or off-Stripe. For example, you can create a Payment Record to model a payment made on a different payment processor, in order to mark an Invoice as paid and a Subscription as active. Payment Records consist of one or more Payment Attempt Records, which represent individual attempts made on a payment network.

## Endpoints

### Retrieve a Payment Record

- [GET /v1/payment_records/:id](https://docs.stripe.com/api/payment-record/retrieve.md)

### Report payment attempt canceled

- [POST /v1/payment_records/:id/report_payment_attempt_canceled](https://docs.stripe.com/api/payment-record/report.md)

### Report payment attempt failed

- [POST /v1/payment_records/:id/report_payment_attempt_failed](https://docs.stripe.com/api/payment-record/report-payment-attempt-failed/report.md)

### Report payment attempt guaranteed

- [POST /v1/payment_records/:id/report_payment_attempt_guaranteed](https://docs.stripe.com/api/payment-record/report-payment-attempt-guaranteed/report.md)

### Report payment attempt informational

- [POST /v1/payment_records/:id/report_payment_attempt_informational](https://docs.stripe.com/api/payment-record/report-payment-attempt-informational/report.md)

### Report a payment attempt

- [POST /v1/payment_records/:id/report_payment_attempt](https://docs.stripe.com/api/payment-record/report-payment-attempt/report.md)

### Report a payment

- [POST /v1/payment_records/report_payment](https://docs.stripe.com/api/payment-record/report-payment/report.md)

### Report a refund

- [POST /v1/payment_records/:id/report_refund](https://docs.stripe.com/api/payment-record/report-refund/report.md)