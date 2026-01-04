# Cards

You can [create physical or virtual cards](https://docs.stripe.com/docs/issuing.md) that are issued to cardholders.

## Endpoints

### Create a card

- [POST /v1/issuing/cards](https://docs.stripe.com/api/issuing/cards/create.md)

### Update a card

- [POST /v1/issuing/cards/:id](https://docs.stripe.com/api/issuing/cards/update.md)

### Retrieve a card

- [GET /v1/issuing/cards/:id](https://docs.stripe.com/api/issuing/cards/retrieve.md)

### List all cards

- [GET /v1/issuing/cards](https://docs.stripe.com/api/issuing/cards/list.md)

### Deliver a testmode card

- [POST /v1/test_helpers/issuing/cards/:id/shipping/deliver](https://docs.stripe.com/api/issuing/cards/test_mode_deliver.md)

### Fail a testmode card

- [POST /v1/test_helpers/issuing/cards/:id/shipping/fail](https://docs.stripe.com/api/issuing/cards/test_mode_fail.md)

### Return a testmode card

- [POST /v1/test_helpers/issuing/cards/:id/shipping/return](https://docs.stripe.com/api/issuing/cards/test_mode_return.md)

### Ship a testmode card

- [POST /v1/test_helpers/issuing/cards/:id/shipping/ship](https://docs.stripe.com/api/issuing/cards/test_mode_ship.md)

### Submit a testmode card

- [POST /v1/test_helpers/issuing/cards/:id/shipping/submit](https://docs.stripe.com/api/issuing/cards/test_mode_submit.md)