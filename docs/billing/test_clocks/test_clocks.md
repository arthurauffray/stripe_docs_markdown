# Test Clocks

A test clock enables deterministic control over objects in testmode. With a test clock, you can create objects at a frozen time in the past or future, and advance to a specific future time to observe webhooks and state changes. After the clock advances, you can either validate the current state of your scenario (and test your assumptions), change the current state of your scenario (and test more complex scenarios), or keep advancing forward in time.

## Endpoints

### Create a test clock

- [POST /v1/test_helpers/test_clocks](https://docs.stripe.com/api/test_clocks/create.md)

### Retrieve a test clock

- [GET /v1/test_helpers/test_clocks/:id](https://docs.stripe.com/api/test_clocks/retrieve.md)

### List all test clocks

- [GET /v1/test_helpers/test_clocks](https://docs.stripe.com/api/test_clocks/list.md)

### Delete a test clock

- [DELETE /v1/test_helpers/test_clocks/:id](https://docs.stripe.com/api/test_clocks/delete.md)

### Advance a test clock

- [POST /v1/test_helpers/test_clocks/:id/advance](https://docs.stripe.com/api/test_clocks/advance.md)