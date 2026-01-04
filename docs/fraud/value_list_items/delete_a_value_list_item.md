# Delete a value list item

Deletes a `ValueListItem` object, removing it from its parent value list.

## Returns

Returns an object with the deleted `ValueListItem` object’s ID and a deleted parameter on success. Otherwise, this call raises [an error](https://docs.stripe.com/api/radar/value_list_items/delete.md#errors).

```curl
curl -X DELETE https://api.stripe.com/v1/radar/value_list_items/rsli_1MxxosLkdIwHu7ixxvA1yKiZ \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe radar value_list_items delete rsli_1MxxosLkdIwHu7ixxvA1yKiZ
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

deleted = client.v1.radar.value_list_items.delete('rsli_1MxxosLkdIwHu7ixxvA1yKiZ')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

deleted = client.v1.radar.value_list_items.delete("rsli_1MxxosLkdIwHu7ixxvA1yKiZ")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$deleted = $stripe->radar->valueListItems->delete(
  'rsli_1MxxosLkdIwHu7ixxvA1yKiZ',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ValueListItem valueListItem =
  client.v1().radar().valueListItems().delete("rsli_1MxxosLkdIwHu7ixxvA1yKiZ");
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const deleted = await stripe.radar.valueListItems.del(
  'rsli_1MxxosLkdIwHu7ixxvA1yKiZ'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.RadarValueListItemDeleteParams{}
result, err := sc.V1RadarValueListItems.Delete(
  context.TODO(), "rsli_1MxxosLkdIwHu7ixxvA1yKiZ", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Radar.ValueListItems;
Stripe.Radar.ValueListItem deleted = service.Delete("rsli_1MxxosLkdIwHu7ixxvA1yKiZ");
```

### Response

```json
{
  "id": "rsli_1MxxosLkdIwHu7ixxvA1yKiZ",
  "object": "radar.value_list_item",
  "deleted": true
}
```