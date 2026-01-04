# Authorizations

When an [issued card](https://docs.stripe.com/docs/issuing.md) is used to make a purchase, an Issuing `Authorization` object is created. [Authorizations](https://docs.stripe.com/docs/issuing/purchases/authorizations.md) must be approved for the purchase to be completed successfully.

Related guide: [Issued card authorizations](https://docs.stripe.com/docs/issuing/purchases/authorizations.md)

## Endpoints

### Update an authorization

- [POST /v1/issuing/authorizations/:id](https://docs.stripe.com/api/issuing/authorizations/update.md)

### Retrieve an authorization

- [GET /v1/issuing/authorizations/:id](https://docs.stripe.com/api/issuing/authorizations/retrieve.md)

### List all authorizations

- [GET /v1/issuing/authorizations](https://docs.stripe.com/api/issuing/authorizations/list.md)

### Approve an authorization

- [POST /v1/issuing/authorizations/:id/approve](https://docs.stripe.com/api/issuing/authorizations/approve.md)

### Decline an authorization

- [POST /v1/issuing/authorizations/:id/decline](https://docs.stripe.com/api/issuing/authorizations/decline.md)

### Create a test-mode authorization

- [POST /v1/test_helpers/issuing/authorizations](https://docs.stripe.com/api/issuing/authorizations/test_mode_create.md)

### Capture a test-mode authorization

- [POST /v1/test_helpers/issuing/authorizations/:id/capture](https://docs.stripe.com/api/issuing/authorizations/test_mode_capture.md)

### Expire a test-mode authorization

- [POST /v1/test_helpers/issuing/authorizations/:id/expire](https://docs.stripe.com/api/issuing/authorizations/test_mode_expire.md)

### Finalize a test-mode authorization's amount

- [POST /v1/test_helpers/issuing/authorizations/:id/finalize_amount](https://docs.stripe.com/api/issuing/authorizations/test_mode_finalize_amount.md)

### Increment a test-mode authorization

- [POST /v1/test_helpers/issuing/authorizations/:id/increment](https://docs.stripe.com/api/issuing/authorizations/test_mode_increment.md)

### Respond to fraud challenge

- [POST /v1/test_helpers/issuing/authorizations/:id/fraud_challenges/respond](https://docs.stripe.com/api/issuing/authorizations/respond_to_fraud_challenges.md)

### Reverse a test-mode authorization

- [POST /v1/test_helpers/issuing/authorizations/:id/reverse](https://docs.stripe.com/api/issuing/authorizations/test_mode_reverse.md)