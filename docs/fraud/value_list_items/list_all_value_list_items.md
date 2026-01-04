# List all value list items

Returns a list of `ValueListItem` objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` items, starting after item `starting_after`. Each entry in the array is a separate `ValueListItem` object. If no more items are available, the resulting array will be empty.

## Parameters

- `value_list` (string, required)
  Identifier for the parent value list this item belongs to.

- `created` (object, optional)
  Only return items that were created during the given date interval.

  - `created.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `created.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `created.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `created.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `value` (string, optional)
  Return items belonging to the parent list whose value matches the specified value (using an “is like” match).

  The maximum length is 800 characters.

```curl
curl -G https://api.stripe.com/v1/radar/value_list_items \
  -u "<<YOUR_SECRET_KEY>>" \
  -d value_list=rsl_1MxxosLkdIwHu7ixNiiD01Kj
```

```cli
stripe radar value_list_items list  \
  --value-list=rsl_1MxxosLkdIwHu7ixNiiD01Kj
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

value_list_items = client.v1.radar.value_list_items.list({
  value_list: 'rsl_1MxxosLkdIwHu7ixNiiD01Kj',
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

value_list_items = client.v1.radar.value_list_items.list({
  "value_list": "rsl_1MxxosLkdIwHu7ixNiiD01Kj",
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$valueListItems = $stripe->radar->valueListItems->all([
  'value_list' => 'rsl_1MxxosLkdIwHu7ixNiiD01Kj',
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ValueListItemListParams params =
  ValueListItemListParams.builder()
    .setValueList("rsl_1MxxosLkdIwHu7ixNiiD01Kj")
    .build();

StripeCollection<ValueListItem> stripeCollection =
  client.v1().radar().valueListItems().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const valueListItems = await stripe.radar.valueListItems.list({
  value_list: 'rsl_1MxxosLkdIwHu7ixNiiD01Kj',
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.RadarValueListItemListParams{
  ValueList: stripe.String("rsl_1MxxosLkdIwHu7ixNiiD01Kj"),
}
result := sc.V1RadarValueListItems.List(context.TODO(), params)
```

```dotnet
var options = new Stripe.Radar.ValueListItemListOptions
{
    ValueList = "rsl_1MxxosLkdIwHu7ixNiiD01Kj",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Radar.ValueListItems;
StripeList<Stripe.Radar.ValueListItem> valueListItems = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/radar/value_list_items",
  "has_more": false,
  "data": [
    {
      "id": "rsl_1MxxosLkdIwHu7ixNiiD01Kj",
      "object": "radar.value_list",
      "alias": "custom_ip_blocklist",
      "created": 1681760074,
      "created_by": "API",
      "item_type": "ip_address",
      "list_items": {
        "object": "list",
        "data": [],
        "has_more": false,
        "total_count": 0,
        "url": "/v1/radar/value_list_items?value_list=rsl_1MxxosLkdIwHu7ixNiiD01Kj"
      },
      "livemode": false,
      "metadata": {},
      "name": "Custom IP Blocklist"
    }
  ]
}
```