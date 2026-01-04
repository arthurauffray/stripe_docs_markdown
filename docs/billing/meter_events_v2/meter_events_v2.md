# Meter Events

Meter events are used to report customer usage of your product or service. Meter events are associated with billing meters, which define the shape of the event’s payload and how those events are aggregated. Meter events are processed asynchronously, so they may not be immediately reflected in aggregates or on upcoming invoices.

## Endpoints

### Create a billing meter event with synchronous validation

- [POST /v2/billing/meter_events](https://docs.stripe.com/api/v2/billing/meter-event/create.md)