# Delete a value list

Deletes a `ValueList` object, also deleting any items contained within the value list. To be deleted, a value list must not be referenced in any rules.

## Returns

Returns an object with the deleted `ValueList` object’s ID and a deleted parameter on success. Otherwise, this call raises [an error](https://docs.stripe.com/api/radar/value_lists/delete.md#errors).

```curl
curl -X DELETE https://api.stripe.com/v1/radar/value_lists/rsl_1MrQSwLkdIwHu7ixWOGS5c8M \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe radar value_lists delete rsl_1MrQSwLkdIwHu7ixWOGS5c8M
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

deleted = client.v1.radar.value_lists.delete('rsl_1MrQSwLkdIwHu7ixWOGS5c8M')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

deleted = client.v1.radar.value_lists.delete("rsl_1MrQSwLkdIwHu7ixWOGS5c8M")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$deleted = $stripe->radar->valueLists->delete('rsl_1MrQSwLkdIwHu7ixWOGS5c8M', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ValueList valueList =
  client.v1().radar().valueLists().delete("rsl_1MrQSwLkdIwHu7ixWOGS5c8M");
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const deleted = await stripe.radar.valueLists.del('rsl_1MrQSwLkdIwHu7ixWOGS5c8M');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.RadarValueListDeleteParams{}
result, err := sc.V1RadarValueLists.Delete(
  context.TODO(), "rsl_1MrQSwLkdIwHu7ixWOGS5c8M", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Radar.ValueLists;
Stripe.Radar.ValueList deleted = service.Delete("rsl_1MrQSwLkdIwHu7ixWOGS5c8M");
```

### Response

```json
{
  "id": "rsl_1MrQSwLkdIwHu7ixWOGS5c8M",
  "object": "radar.value_list",
  "deleted": true
}
```