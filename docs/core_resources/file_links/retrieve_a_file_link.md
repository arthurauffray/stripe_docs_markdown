# Retrieve a file link

Retrieves the file link with the given ID.

## Returns

If the identifier you provide is valid, a file link object returns. If not, Stripe raises [an error](https://docs.stripe.com/api/file_links/retrieve.md#errors).

```curl
curl https://api.stripe.com/v1/file_links/link_1Mr23jLkdIwHu7ix65betcoo \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe file_links retrieve link_1Mr23jLkdIwHu7ix65betcoo
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

file_link = client.v1.file_links.retrieve('link_1Mr23jLkdIwHu7ix65betcoo')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

file_link = client.v1.file_links.retrieve("link_1Mr23jLkdIwHu7ix65betcoo")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$fileLink = $stripe->fileLinks->retrieve('link_1Mr23jLkdIwHu7ix65betcoo', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

FileLinkRetrieveParams params = FileLinkRetrieveParams.builder().build();

FileLink fileLink =
  client.v1().fileLinks().retrieve("link_1Mr23jLkdIwHu7ix65betcoo", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const fileLink = await stripe.fileLinks.retrieve('link_1Mr23jLkdIwHu7ix65betcoo');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.FileLinkRetrieveParams{}
result, err := sc.V1FileLinks.Retrieve(
  context.TODO(), "link_1Mr23jLkdIwHu7ix65betcoo", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.FileLinks;
FileLink fileLink = service.Get("link_1Mr23jLkdIwHu7ix65betcoo");
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
  "metadata": {},
  "url": "https://files.stripe.com/links/MDB8YWNjdF8xTTJKVGtMa2RJd0h1N2l4fGZsX3Rlc3RfaXVoY2hrUnJPMzlBR3dPb01XMmFkSTVq00yUPLFf3h"
}
```