# Event Destinations

Set up an event destination to receive events from Stripe across multiple destination types, including [webhook endpoints](https://docs.stripe.com/webhooks.md) and [Amazon EventBridge](https://docs.stripe.com/event-destinations/eventbridge.md). Event destinations support receiving [thin events](https://docs.stripe.com/api/v2/events.md) and [snapshot events](https://docs.stripe.com/api/events.md).

## Endpoints

### Create an event destination

- [POST /v2/core/event_destinations](https://docs.stripe.com/api/v2/core/event_destinations/create.md)

### Update an event destination

- [POST /v2/core/event_destinations/:id](https://docs.stripe.com/api/v2/core/event_destinations/update.md)

### Retrieve an event destination

- [GET /v2/core/event_destinations/:id](https://docs.stripe.com/api/v2/core/event_destinations/retrieve.md)

### List event destinations

- [GET /v2/core/event_destinations](https://docs.stripe.com/api/v2/core/event_destinations/list.md)

### Delete an event destination

- [DELETE /v2/core/event_destinations/:id](https://docs.stripe.com/api/v2/core/event_destinations/delete.md)

### Disable an event destination

- [POST /v2/core/event_destinations/:id/disable](https://docs.stripe.com/api/v2/core/event_destinations/disable.md)

### Enable an event destination

- [POST /v2/core/event_destinations/:id/enable](https://docs.stripe.com/api/v2/core/event_destinations/enable.md)