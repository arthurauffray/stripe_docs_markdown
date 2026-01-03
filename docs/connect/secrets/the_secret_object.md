# The Secret object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `deleted` (boolean, nullable)
  If true, indicates that this secret has been deleted

- `expires_at` (timestamp, nullable)
  The Unix timestamp for the expiry time of the secret, after which the secret deletes.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `name` (string)
  A name for the secret that’s unique within the scope.

- `payload` (string, nullable)
  The plaintext secret value to be stored.

- `scope` (object)
  Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.

  - `scope.type` (enum)
    The secret scope type.
Possible enum values:
    - `account`
      A secret scoped to an account. Use this for API keys or other secrets that should be accessible by all UI Extension contexts.

    - `user`
      A secret scoped to a specific user. Use this for oauth tokens or other per-user secrets. If this is set, `scope.user` must also be set.

  - `scope.user` (string, nullable)
    The user ID, if type is set to “user”

### The Secret object

```json
{
  "id": "appsecret_5110hHS1707T6fjBnah1LkdIwHu7ix",
  "object": "apps.secret",
  "created": 1680209063,
  "expires_at": null,
  "livemode": false,
  "name": "my-api-key",
  "scope": {
    "type": "account"
  }
}
```