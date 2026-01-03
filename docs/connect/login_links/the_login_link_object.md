# The Login Link object

## Attributes

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `url` (string)
  The URL for the login link.

### The Login Link object

```json
{
  "object": "login_link",
  "created": 1686084879,
  "url": "https://connect.stripe.com/express/acct_1032D82eZvKYlo2C/F44eiGHh5sEV"
}
```