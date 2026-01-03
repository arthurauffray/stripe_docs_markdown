# Create a file link

Creates a new file link object.

## Returns

Returns the file link object if successful and raises [an error](https://docs.stripe.com/api/file_links/create.md#errors) otherwise.

## Parameters

- `file` (string, required)
  The ID of the file. The file’s `purpose` must be one of the following: `business_icon`, `business_logo`, `customer_signature`, `dispute_evidence`, `finance_report_run`, `financial_account_statement`, `identity_document_downloadable`, `issuing_regulatory_reporting`, `pci_document`, `selfie`, `sigma_scheduled_query`, `tax_document_user_upload`, `terminal_android_apk`, or `terminal_reader_splashscreen`.

- `expires_at` (timestamp, optional)
  The link isn’t usable after this future timestamp.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/file_links \
  -u "<<YOUR_SECRET_KEY>>" \
  -d file=file_1Mr23iLkdIwHu7ixQkCV3CBR
```

```cli
stripe file_links create  \
  --file=file_1Mr23iLkdIwHu7ixQkCV3CBR
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

file_link = client.v1.file_links.create({file: 'file_1Mr23iLkdIwHu7ixQkCV3CBR'})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

file_link = client.v1.file_links.create({"file": "file_1Mr23iLkdIwHu7ixQkCV3CBR"})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$fileLink = $stripe->fileLinks->create(['file' => 'file_1Mr23iLkdIwHu7ixQkCV3CBR']);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

FileLinkCreateParams params =
  FileLinkCreateParams.builder().setFile("file_1Mr23iLkdIwHu7ixQkCV3CBR").build();

FileLink fileLink = client.v1().fileLinks().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const fileLink = await stripe.fileLinks.create({
  file: 'file_1Mr23iLkdIwHu7ixQkCV3CBR',
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.FileLinkCreateParams{
  File: stripe.String("file_1Mr23iLkdIwHu7ixQkCV3CBR"),
}
result, err := sc.V1FileLinks.Create(context.TODO(), params)
```

```dotnet
var options = new FileLinkCreateOptions { File = "file_1Mr23iLkdIwHu7ixQkCV3CBR" };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.FileLinks;
FileLink fileLink = service.Create(options);
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