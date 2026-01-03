# Retrieve a file

Retrieves the details of an existing file object. After you supply a unique file ID, Stripe returns the corresponding file object. Learn how to [access file contents](https://docs.stripe.com/docs/file-upload.md#download-file-contents).

## Returns

If the identifier you provide is valid, a file object returns. If not, Stripe raises [an error](https://docs.stripe.com/api/files/retrieve.md#errors).

```curl
curl https://api.stripe.com/v1/files/file_1Mr4LDLkdIwHu7ixFCz0dZiH \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe files retrieve file_1Mr4LDLkdIwHu7ixFCz0dZiH
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

file = client.v1.files.retrieve('file_1Mr4LDLkdIwHu7ixFCz0dZiH')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

file = client.v1.files.retrieve("file_1Mr4LDLkdIwHu7ixFCz0dZiH")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$file = $stripe->files->retrieve('file_1Mr4LDLkdIwHu7ixFCz0dZiH', []);
```

```java
Stripe.apiKey = "<<YOUR_SECRET_KEY>>";

File file = File.retrieve("file_1Mr4LDLkdIwHu7ixFCz0dZiH");
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const file = await stripe.files.retrieve('file_1Mr4LDLkdIwHu7ixFCz0dZiH');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.FileRetrieveParams{}
result, err := sc.V1Files.Retrieve(
  context.TODO(), "file_1Mr4LDLkdIwHu7ixFCz0dZiH", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Files;
File file = service.Get("file_1Mr4LDLkdIwHu7ixFCz0dZiH");
```

### Response

```json
{
  "id": "file_1Mr4LDLkdIwHu7ixFCz0dZiH",
  "object": "file",
  "created": 1680116847,
  "expires_at": 1703444847,
  "filename": "file.png",
  "links": {
    "object": "list",
    "data": [],
    "has_more": false,
    "url": "/v1/file_links?file=file_1Mr4LDLkdIwHu7ixFCz0dZiH"
  },
  "purpose": "dispute_evidence",
  "size": 8429,
  "title": null,
  "type": "png",
  "url": "https://files.stripe.com/v1/files/file_1Mr4LDLkdIwHu7ixFCz0dZiH/contents"
}
```