# Retrieve a value list item

Retrieves a `ValueListItem` object.

## Returns

Returns a `ValueListItem` object if a valid identifier was provided.

```curl
curl https://api.stripe.com/v1/radar/value_list_items/rsli_1MxxosLkdIwHu7ixxvA1yKiZ \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe radar value_list_items retrieve rsli_1MxxosLkdIwHu7ixxvA1yKiZ
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

value_list_item = client.v1.radar.value_list_items.retrieve('rsli_1MxxosLkdIwHu7ixxvA1yKiZ')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

value_list_item = client.v1.radar.value_list_items.retrieve(
  "rsli_1MxxosLkdIwHu7ixxvA1yKiZ",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$valueListItem = $stripe->radar->valueListItems->retrieve(
  'rsli_1MxxosLkdIwHu7ixxvA1yKiZ',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ValueListItemRetrieveParams params = ValueListItemRetrieveParams.builder().build();

ValueListItem valueListItem =
  client.v1().radar().valueListItems().retrieve(
    "rsli_1MxxosLkdIwHu7ixxvA1yKiZ",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const valueListItem = await stripe.radar.valueListItems.retrieve(
  'rsli_1MxxosLkdIwHu7ixxvA1yKiZ'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.RadarValueListItemRetrieveParams{}
result, err := sc.V1RadarValueListItems.Retrieve(
  context.TODO(), "rsli_1MxxosLkdIwHu7ixxvA1yKiZ", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Radar.ValueListItems;
Stripe.Radar.ValueListItem valueListItem = service.Get(
    "rsli_1MxxosLkdIwHu7ixxvA1yKiZ");
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