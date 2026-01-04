# The Connection Token object

## Attributes

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `location` (string, nullable)
  The id of the location that this connection token is scoped to. Note that location scoping only applies to internet-connected readers. For more details, see [the docs on scoping connection tokens](https://docs.stripe.com/terminal/fleet/locations-and-zones.md?dashboard-or-api=api#connection-tokens).

- `secret` (string)
  Your application should pass this token to the Stripe Terminal SDK.

### The Connection Token object

```json
{
  "object": "terminal.connection_token",
  "secret": "pst_test_YWNjdF8xTTJKVGtMa2RJd0h1N2l4LE81ZEdIalZ6NlVuMUdjM3c3WkRnN0ZYRHZxRURwTXo_00gNK2DWAV"
}
```