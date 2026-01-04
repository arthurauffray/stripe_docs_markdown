# Advance a test clock

Starts advancing a test clock to a specified time in the future. Advancement is done when status changes to `Ready`.

## Returns

A `TestClock` object with status `Advancing` is returned upon success. Otherwise, this call raises [an error](https://docs.stripe.com/api/test_clocks/advance.md#errors).

## Parameters

- `frozen_time` (timestamp, required)
  The time to advance the test clock. Must be after the test clock’s current frozen time. Cannot be more than two intervals in the future from the shortest subscription in this test clock. If there are no subscriptions in this test clock, it cannot be more than two years in the future.

```curl
curl https://api.stripe.com/v1/test_helpers/test_clocks/clock_1Mr3I22eZvKYlo2Ck0rgMqd7/advance \
  -u "<<YOUR_SECRET_KEY>>" \
  -d frozen_time=1680199613
```

```cli
stripe test_helpers test_clocks advance clock_1Mr3I22eZvKYlo2Ck0rgMqd7 \
  --frozen-time=1680199613
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

test_clock = client.v1.test_helpers.test_clocks.advance(
  'clock_1Mr3I22eZvKYlo2Ck0rgMqd7',
  {frozen_time: 1680199613},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

test_clock = client.v1.test_helpers.test_clocks.advance(
  "clock_1Mr3I22eZvKYlo2Ck0rgMqd7",
  {"frozen_time": 1680199613},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$testClock = $stripe->testHelpers->testClocks->advance(
  'clock_1Mr3I22eZvKYlo2Ck0rgMqd7',
  ['frozen_time' => 1680199613]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TestClockAdvanceParams params =
  TestClockAdvanceParams.builder().setFrozenTime(1680199613L).build();

TestClock testClock =
  client.v1().testHelpers().testClocks().advance(
    "clock_1Mr3I22eZvKYlo2Ck0rgMqd7",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const testClock = await stripe.testHelpers.testClocks.advance(
  'clock_1Mr3I22eZvKYlo2Ck0rgMqd7',
  {
    frozen_time: 1680199613,
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TestHelpersTestClockAdvanceParams{
  FrozenTime: stripe.Int64(1680199613),
}
result, err := sc.V1TestHelpersTestClocks.Advance(
  context.TODO(), "clock_1Mr3I22eZvKYlo2Ck0rgMqd7", params)
```

```dotnet
var options = new Stripe.TestHelpers.TestClockAdvanceOptions
{
    FrozenTime = DateTimeOffset.FromUnixTimeSeconds(1680199613).UtcDateTime,
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.TestHelpers.TestClocks;
Stripe.TestHelpers.TestClock testClock = service.Advance(
    "clock_1Mr3I22eZvKYlo2Ck0rgMqd7",
    options);
```

### Response

```json
{
  "id": "clock_1Mr3I22eZvKYlo2Ck0rgMqd7",
  "object": "test_helpers.test_clock",
  "created": 1680112806,
  "deletes_after": 1680717606,
  "frozen_time": 1577836800,
  "livemode": false,
  "name": null,
  "status": "advancing"
}
```