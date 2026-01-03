# Events

Snapshot events allow you to track and react to activity in your Stripe integration. When the state of another API resource changes, Stripe creates an `Event` object that contains all the relevant information associated with that action, including the affected API resource. For example, a successful payment triggers a `charge.succeeded` event, which contains the `Charge` in the event’s data property. Some actions trigger multiple events. For example, if you create a new subscription for a customer, it triggers both a `customer.subscription.created` event and a `charge.succeeded` event.

Configure an event destination in your account to listen for events that represent actions your integration needs to respond to. Additionally, you can retrieve an individual event or a list of events from the API.

[Connect](https://docs.stripe.com/connect.md) platforms can also receive event notifications that occur in their connected accounts. These events include an account attribute that identifies the relevant connected account.

You can access events through the [Retrieve Event API](https://docs.stripe.com/api/events.md#retrieve_event) for 30 days.

## Endpoints

### Retrieve an event

- [GET /v1/events/:id](https://docs.stripe.com/api/events/retrieve.md)

### List all events

- [GET /v1/events](https://docs.stripe.com/api/events/list.md)