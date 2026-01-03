# Create a file

To upload a file to Stripe, you need to send a request of type `multipart/form-data`. Include the file you want to upload in the request, and the parameters for creating a file.

All of Stripe’s officially supported Client libraries support sending `multipart/form-data`.

## Returns

Returns the file object.

## Parameters

- `file` (object, required)
  A file to upload. Make sure that the specifications follow RFC 2388, which defines file transfers for the `multipart/form-data` protocol.

- `purpose` (enum, required)
  The [purpose](https://docs.stripe.com/docs/file-upload.md#uploading-a-file) of the uploaded file.
Possible enum values:
  - `account_requirement`
    Additional documentation requirements that can be requested for an account.

  - `additional_verification`
    Additional verification for custom accounts.

  - `business_icon`
    A business icon.

  - `business_logo`
    A business logo.

  - `customer_signature`
    Customer signature image.

  - `dispute_evidence`
    Evidence to submit with a dispute response.

  - `identity_document`
    A document to verify the identity of an account owner during account provisioning.

  - `issuing_regulatory_reporting`
    Additional regulatory reporting requirements for Issuing.

  - `pci_document`
    A self-assessment PCI questionnaire.

  - `platform_terms_of_service`
    A copy of the platform’s Terms of Service.

  - `tax_document_user_upload`
    A user-uploaded tax document.

  - `terminal_android_apk`
    Android POS apps to be deployed on Stripe smart readers.

  - `terminal_reader_splashscreen`
    Splashscreen to be displayed on Terminal readers.

- `file_link_data` (object, optional)
  Optional parameters that automatically create a [file link](https://docs.stripe.com/api/files/create.md#file_links) for the newly created file.

  - `file_link_data.create` (boolean, required)
    Set this to `true` to create a file link for the newly created file. Creating a link is only possible when the file’s `purpose` is one of the following: `business_icon`, `business_logo`, `customer_signature`, `dispute_evidence`, `issuing_regulatory_reporting`, `pci_document`, `tax_document_user_upload`, `terminal_android_apk`, or `terminal_reader_splashscreen`.

  - `file_link_data.expires_at` (timestamp, optional)
    The link isn’t available after this future timestamp.

  - `file_link_data.metadata` (object, optional)
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://files.stripe.com/v1/files \
  -u <<YOUR_SECRET_KEY>> \
  -F purpose=dispute_evidence \
  -F file="@/path/to/a/file.jpg"
```

```cli
stripe files create  \
  --purpose=dispute_evidence \
  --file="@/path/to/a/file.png"
```

```ruby
Stripe.api_key = "<<YOUR_SECRET_KEY>>"
file = File.new("@/path/to/a/file.jpg")

Stripe::File.create(
  {
    purpose: "dispute_evidence",
    file: file
  }
)
```

```python
stripe.api_key = "<<YOUR_SECRET_KEY>>"

with open("@/path/to/a/file.jpg", "rb") as fp:
  stripe.File.create(
    purpose="dispute_evidence",
    file=fp
  )
```

```php
$fp = fopen('@/path/to/a/file.jpg', 'r');

$stripe->files->create([
  'purpose' => 'dispute_evidence',
  'file' => $fp
]);
```

```java
Stripe.apiKey = "<<YOUR_SECRET_KEY>>";

FileCreateParams params =
  FileCreateParams.builder()
    .setFile(new java.io.File("@/path/to/a/file.jpg"))
    .setPurpose(FileCreateParams.Purpose.DISPUTE_EVIDENCE)
    .build();

File upload = File.create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const fp = fs.readFileSync('@/path/to/a/file.jpg');
const upload = await stripe.files.create({
  file: {
    data: fp,
    name: 'file.jpg',
    type: 'application.octet-stream',
  },
  purpose: 'dispute_evidence',
});
```

```go
stripe.Key = "<<YOUR_SECRET_KEY>>"

fp, _ := os.Open("/path/to/a/file.jpg")
params := &stripe.FileParams{
	FileReader: fp,
	Purpose:    stripe.String(string(stripe.FilePurposeDisputeEvidence)),
	Filename:   stripe.String("file.jpg"),
}
upload, _ := file.New(params)
```

```dotnet
StripeConfiguration.ApiKey = "<<YOUR_SECRET_KEY>>";

var filename = "@/path/to/a/file.png";
using (FileStream stream = System.IO.File.Open(filename, FileMode.Open))
{
  var options = new FileCreateOptions
  {
    File = stream,
      Purpose = FilePurpose.DisputeEvidence
  };
  var service = new FileService();
  var file = service.Create(options);
}
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