# The MeterEventSession object

## Attributes

- `id` (string)
  The unique id of this auth session.

- `object` (string, value is "v2.billing.meter_event_session")
  String representing the object’s type. Objects of the same type share the same value of the object field.

- `authentication_token` (string)
  The authentication token for this session.  Use this token when calling the high-throughput meter event API.

- `created` (timestamp)
  The creation time of this session.

- `expires_at` (timestamp)
  The time at which this session will expire.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

### The MeterEventSession object

```json
{
  "id": "<AUTH_SESSION_ID>",
  "livemode": "false",
  "object": "v2.billing.meter_event_session",
  "authentication_token": "token_12345678",
  "created": "2024-06-01T12:00:00.000Z",
  "expires_at": "2024-06-01T12:15:00.000Z"
}
```