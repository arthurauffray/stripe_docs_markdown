# Cards

You can store multiple cards on a customer in order to charge the customer later. You can also store multiple debit cards on a recipient in order to transfer to those cards later.

Related guide: [Card payments with Sources](https://docs.stripe.com/docs/sources/cards.md)

## Endpoints

### Create a card

- [POST /v1/customers/:id/sources](https://docs.stripe.com/api/cards/create.md)

### Update a card

- [POST /v1/customers/:id/sources/:id](https://docs.stripe.com/api/cards/update.md)

### Retrieve a card

- [GET /v1/customers/:id/cards/:id](https://docs.stripe.com/api/cards/retrieve.md)

### List all cards

- [GET /v1/customers/:id/cards](https://docs.stripe.com/api/cards/list.md)

### Delete a card

- [DELETE /v1/customers/:id/sources/:id](https://docs.stripe.com/api/cards/delete.md)