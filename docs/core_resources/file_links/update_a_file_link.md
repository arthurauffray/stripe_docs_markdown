# Update a file link

Updates an existing file link object. Expired links can no longer be updated.

## Returns

Returns the file link object if successful, and raises [an error](https://docs.stripe.com/api/file_links/update.md#errors) otherwise.

## Parameters

- `expires_at` (string | timestamp, optional)
  A future timestamp after which the link will no longer be usable, or `now` to expire the link immediately.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/file_links/link_1Mr23jLkdIwHu7ix65betcoo \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
```

```cli
stripe file_links update link_1Mr23jLkdIwHu7ix65betcoo \
  -d "metadata[order_id]"=6735
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

file_link = client.v1.file_links.update(
  'link_1Mr23jLkdIwHu7ix65betcoo',
  {metadata: {order_id: '6735'}},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

file_link = client.v1.file_links.update(
  "link_1Mr23jLkdIwHu7ix65betcoo",
  {"metadata": {"order_id": "6735"}},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$fileLink = $stripe->fileLinks->update(
  'link_1Mr23jLkdIwHu7ix65betcoo',
  ['metadata' => ['order_id' => '6735']]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

FileLinkUpdateParams params =
  FileLinkUpdateParams.builder().putMetadata("order_id", "6735").build();

FileLink fileLink =
  client.v1().fileLinks().update("link_1Mr23jLkdIwHu7ix65betcoo", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const fileLink = await stripe.fileLinks.update(
  'link_1Mr23jLkdIwHu7ix65betcoo',
  {
    metadata: {
      order_id: '6735',
    },
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.FileLinkUpdateParams{}
params.AddMetadata("order_id", "6735")
result, err := sc.V1FileLinks.Update(
  context.TODO(), "link_1Mr23jLkdIwHu7ix65betcoo", params)
```

```dotnet
var options = new FileLinkUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.FileLinks;
FileLink fileLink = service.Update("link_1Mr23jLkdIwHu7ix65betcoo", options);
```

### Response

```json
{
  "id": "link_1Mr23jLkdIwHu7ix65betcoo",
  "object": "file_link",
  "created": 1680108075,
  "expired": false,
  "expires_at": null,
  "file": "file_1Mr23iLkdIwHu7ixQkCV3CBR",
  "livemode": false,
  "metadata": {
    "order_id": "6735"
  },
  "url": "https://files.stripe.com/links/MDB8YWNjdF8xTTJKVGtMa2RJd0h1N2l4fGZsX3Rlc3RfaXVoY2hrUnJPMzlBR3dPb01XMmFkSTVq00yUPLFf3h"
}
```