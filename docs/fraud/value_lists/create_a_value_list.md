# Create a value list

Creates a new `ValueList` object, which can then be referenced in rules.

## Returns

Returns a `ValueList` object if creation succeeds.

## Parameters

- `alias` (string, required)
  The name of the value list for use in rules.

  The maximum length is 100 characters.

- `name` (string, required)
  The human-readable name of the value list.

  The maximum length is 100 characters.

- `item_type` (string, optional)
  Type of the items in the value list. One of `card_fingerprint`, `card_bin`, `email`, `ip_address`, `country`, `string`, `case_sensitive_string`, `customer_id`, `sepa_debit_fingerprint`, or `us_bank_account_fingerprint`. Use `string` if the item type is unknown or mixed.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/radar/value_lists \
  -u "<<YOUR_SECRET_KEY>>" \
  -d name="Custom IP Blocklist" \
  -d alias=custom_ip_blocklist \
  -d item_type=ip_address
```

```cli
stripe radar value_lists create  \
  --name="Custom IP Blocklist" \
  --alias=custom_ip_blocklist \
  --item-type=ip_address
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

value_list = client.v1.radar.value_lists.create({
  name: 'Custom IP Blocklist',
  alias: 'custom_ip_blocklist',
  item_type: 'ip_address',
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

value_list = client.v1.radar.value_lists.create({
  "name": "Custom IP Blocklist",
  "alias": "custom_ip_blocklist",
  "item_type": "ip_address",
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$valueList = $stripe->radar->valueLists->create([
  'name' => 'Custom IP Blocklist',
  'alias' => 'custom_ip_blocklist',
  'item_type' => 'ip_address',
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ValueListCreateParams params =
  ValueListCreateParams.builder()
    .setName("Custom IP Blocklist")
    .setAlias("custom_ip_blocklist")
    .setItemType(ValueListCreateParams.ItemType.IP_ADDRESS)
    .build();

ValueList valueList = client.v1().radar().valueLists().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const valueList = await stripe.radar.valueLists.create({
  name: 'Custom IP Blocklist',
  alias: 'custom_ip_blocklist',
  item_type: 'ip_address',
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.RadarValueListCreateParams{
  Name: stripe.String("Custom IP Blocklist"),
  Alias: stripe.String("custom_ip_blocklist"),
  ItemType: stripe.String(stripe.RadarValueListItemTypeIPAddress),
}
result, err := sc.V1RadarValueLists.Create(context.TODO(), params)
```

```dotnet
var options = new Stripe.Radar.ValueListCreateOptions
{
    Name = "Custom IP Blocklist",
    Alias = "custom_ip_blocklist",
    ItemType = "ip_address",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Radar.ValueLists;
Stripe.Radar.ValueList valueList = service.Create(options);
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