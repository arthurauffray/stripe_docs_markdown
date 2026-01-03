# The AccountToken object

## Attributes

- `id` (string)
  Unique identifier for the token.

- `object` (string, value is "v2.core.account_token")
  String representing the object’s type. Objects of the same type share the same value of the object field.

- `created` (timestamp)
  Time at which the token was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.

- `expires_at` (timestamp)
  Time at which the token will expire.

- `livemode` (boolean)
  Has the value `true` if the token exists in live mode or the value `false` if the object exists in test mode.

- `used` (boolean)
  Determines if the token has already been used (tokens can only be used once).

### The AccountToken object

```json
{
  "created": "2025-01-01T00:00:00.000Z",
  "expires_at": "2025-01-01T00:00:00.000Z",
  "id": "4242",
  "livemode": true,
  "object": "4242",
  "used": true
}
```