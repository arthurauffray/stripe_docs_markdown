# Create a value list item

Creates a new `ValueListItem` object, which is added to the specified parent value list.

## Returns

Returns a `ValueListItem` object if creation succeeds.

## Parameters

- `value` (string, required)
  The value of the item (whose type must match the type of the parent value list).

  The maximum length is 800 characters.

- `value_list` (string, required)
  The identifier of the value list which the created item will be added to.

```curl
curl https://api.stripe.com/v1/radar/value_list_items \
  -u "<<YOUR_SECRET_KEY>>" \
  -d value_list=rsl_1MxxosLkdIwHu7ixNiiD01Kj \
  -d value="1.2.3.4"
```

```cli
stripe radar value_list_items create  \
  --value-list=rsl_1MxxosLkdIwHu7ixNiiD01Kj \
  --value="1.2.3.4"
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

value_list_item = client.v1.radar.value_list_items.create({
  value_list: 'rsl_1MxxosLkdIwHu7ixNiiD01Kj',
  value: '1.2.3.4',
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

value_list_item = client.v1.radar.value_list_items.create({
  "value_list": "rsl_1MxxosLkdIwHu7ixNiiD01Kj",
  "value": "1.2.3.4",
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$valueListItem = $stripe->radar->valueListItems->create([
  'value_list' => 'rsl_1MxxosLkdIwHu7ixNiiD01Kj',
  'value' => '1.2.3.4',
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ValueListItemCreateParams params =
  ValueListItemCreateParams.builder()
    .setValueList("rsl_1MxxosLkdIwHu7ixNiiD01Kj")
    .setValue("1.2.3.4")
    .build();

ValueListItem valueListItem = client.v1().radar().valueListItems().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const valueListItem = await stripe.radar.valueListItems.create({
  value_list: 'rsl_1MxxosLkdIwHu7ixNiiD01Kj',
  value: '1.2.3.4',
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.RadarValueListItemCreateParams{
  ValueList: stripe.String("rsl_1MxxosLkdIwHu7ixNiiD01Kj"),
  Value: stripe.String("1.2.3.4"),
}
result, err := sc.V1RadarValueListItems.Create(context.TODO(), params)
```

```dotnet
var options = new Stripe.Radar.ValueListItemCreateOptions
{
    ValueList = "rsl_1MxxosLkdIwHu7ixNiiD01Kj",
    Value = "1.2.3.4",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Radar.ValueListItems;
Stripe.Radar.ValueListItem valueListItem = service.Create(options);
```

### Response

```json
{
  "id": "rsli_1MxxosLkdIwHu7ixxvA1yKiZ",
  "object": "radar.value_list_item",
  "created": 1681760074,
  "created_by": "API",
  "livemode": false,
  "value": "1.2.3.4",
  "value_list": "rsl_1MxxosLkdIwHu7ixNiiD01Kj"
}
```