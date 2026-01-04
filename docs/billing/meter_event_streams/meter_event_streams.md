# Meter Event Streams

You can send a higher-throughput of meter events using meter event streams. For this flow, you must first create a meter event session, which will provide you with a session token. You can then create meter events through the meter event stream endpoint, using the session token for authentication. The session tokens are short-lived and you will need to create a new meter event session when the token expires.

## Endpoints

### Create billing meter event stream authentication session

- [POST /v2/billing/meter_event_session](https://docs.stripe.com/api/v2/billing/meter-event-stream/session/create.md)

### Create a billing meter event with asynchronous validation

- [POST /v2/billing/meter_event_stream](https://docs.stripe.com/api/v2/billing/meter-event-stream/create.md)