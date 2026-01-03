# The Account Link object

## Attributes

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `expires_at` (timestamp)
  The timestamp at which this account link will expire.

- `url` (string)
  The URL for the account link.

### The Account Link object

```json
{
  "object": "account_link",
  "created": 1680577733,
  "expires_at": 1680578033,
  "url": "https://connect.stripe.com/setup/c/acct_1Mt0CORHFI4mz9Rw/TqckGNUHg2mG"
}
```