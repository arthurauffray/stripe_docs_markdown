# Delete a test clock

Deletes a test clock.

## Returns

The deleted `TestClock` object is returned upon success. Otherwise, this call raises [an error](https://docs.stripe.com/api/test_clocks/delete.md#errors).

```curl
curl -X DELETE https://api.stripe.com/v1/test_helpers/test_clocks/clock_1Mr3I22eZvKYlo2Ck0rgMqd7 \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe test_helpers test_clocks delete clock_1Mr3I22eZvKYlo2Ck0rgMqd7
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

deleted = client.v1.test_helpers.test_clocks.delete('clock_1Mr3I22eZvKYlo2Ck0rgMqd7')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

deleted = client.v1.test_helpers.test_clocks.delete("clock_1Mr3I22eZvKYlo2Ck0rgMqd7")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$deleted = $stripe->testHelpers->testClocks->delete(
  'clock_1Mr3I22eZvKYlo2Ck0rgMqd7',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TestClock testClock =
  client.v1().testHelpers().testClocks().delete("clock_1Mr3I22eZvKYlo2Ck0rgMqd7");
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const deleted = await stripe.testHelpers.testClocks.del(
  'clock_1Mr3I22eZvKYlo2Ck0rgMqd7'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TestHelpersTestClockDeleteParams{}
result, err := sc.V1TestHelpersTestClocks.Delete(
  context.TODO(), "clock_1Mr3I22eZvKYlo2Ck0rgMqd7", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.TestHelpers.TestClocks;
Stripe.TestHelpers.TestClock deleted = service.Delete(
    "clock_1Mr3I22eZvKYlo2Ck0rgMqd7");
```

### Response

```json
{
  "id": "clock_1Mr3I22eZvKYlo2Ck0rgMqd7",
  "object": "test_helpers.test_clock",
  "deleted": true
}
```