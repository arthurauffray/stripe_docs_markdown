# The Test Clock object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `deletes_after` (timestamp)
  Time at which this clock is scheduled to auto delete.

- `frozen_time` (timestamp)
  Time at which all objects belonging to this clock are frozen.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `name` (string, nullable)
  The custom name supplied at creation.

- `status` (enum)
  The status of the Test Clock.
Possible enum values:
  - `advancing`
    In the process of advancing time for the test clock objects.

  - `internal_failure`
    Failed to advance time. Future requests to advance time will fail.

  - `ready`
    All test clock objects have advanced to the `frozen_time`.

- `status_details` (object)
  Details on the current state of the Test Clock.

  - `status_details.advancing` (object, nullable)
    Details on the Test Clock when its `status` is `advancing`.

    - `status_details.advancing.target_frozen_time` (timestamp)
      The `frozen_time` that the Test Clock is advancing towards.

### The Test Clock object

```json
{
  "id": "clock_1Mr3I22eZvKYlo2Ck0rgMqd7",
  "object": "test_helpers.test_clock",
  "created": 1680112806,
  "deletes_after": 1680717606,
  "frozen_time": 1577836800,
  "livemode": false,
  "name": null,
  "status": "ready"
}
```