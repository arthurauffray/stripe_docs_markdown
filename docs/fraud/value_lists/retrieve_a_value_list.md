# Retrieve a value list

Retrieves a `ValueList` object.

## Returns

Returns a `ValueList` object if a valid identifier was provided.

```curl
curl https://api.stripe.com/v1/radar/value_lists/rsl_1MrQSwLkdIwHu7ixWOGS5c8M \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe radar value_lists retrieve rsl_1MrQSwLkdIwHu7ixWOGS5c8M
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

value_list = client.v1.radar.value_lists.retrieve('rsl_1MrQSwLkdIwHu7ixWOGS5c8M')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

value_list = client.v1.radar.value_lists.retrieve("rsl_1MrQSwLkdIwHu7ixWOGS5c8M")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$valueList = $stripe->radar->valueLists->retrieve(
  'rsl_1MrQSwLkdIwHu7ixWOGS5c8M',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ValueListRetrieveParams params = ValueListRetrieveParams.builder().build();

ValueList valueList =
  client.v1().radar().valueLists().retrieve("rsl_1MrQSwLkdIwHu7ixWOGS5c8M", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const valueList = await stripe.radar.valueLists.retrieve(
  'rsl_1MrQSwLkdIwHu7ixWOGS5c8M'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.RadarValueListRetrieveParams{}
result, err := sc.V1RadarValueLists.Retrieve(
  context.TODO(), "rsl_1MrQSwLkdIwHu7ixWOGS5c8M", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Radar.ValueLists;
Stripe.Radar.ValueList valueList = service.Get("rsl_1MrQSwLkdIwHu7ixWOGS5c8M");
```

### Response

```json
{
  "id": "rsl_1MrQSwLkdIwHu7ixWOGS5c8M",
  "object": "radar.value_list",
  "alias": "custom_ip_blocklist",
  "created": 1680201894,
  "created_by": "API",
  "item_type": "ip_address",
  "list_items": {
    "object": "list",
    "data": [],
    "has_more": false,
    "total_count": 0,
    "url": "/v1/radar/value_list_items?value_list=rsl_1MrQSwLkdIwHu7ixWOGS5c8M"
  },
  "livemode": false,
  "metadata": {},
  "name": "Custom IP Blocklist"
}
```