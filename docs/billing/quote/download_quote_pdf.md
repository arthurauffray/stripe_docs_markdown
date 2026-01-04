# Download quote PDF

Download the PDF for a finalized quote. Explanation for special handling can be found [here](https://docs.stripe.com/quotes/overview.md#quote_pdf)

## Returns

The PDF file for the quote.

```curl
curl https://files.stripe.com/v1/quotes/qt_0J1EnX589O8KAxCGEdmhZY3r/pdf \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe quotes pdf qt_0J1EnX589O8KAxCGEdmhZY3r
```

```ruby
body = +""
Stripe::Quote.pdf("qt_0J1EnX589O8KAxCGEdmhZY3r") do |read_body_chunk|
  body << read_body_chunk
end
```

```python
# Assumes that your http client is 'requests'
resource = stripe.Quote.retrieve("qt_0J1EnX589O8KAxCGEdmhZY3r")
stream = resource.pdf()
# Buffer all the content
content = stream.io.read()
```

```php
$output = '';
$resources = $this->service->pdf("qt_0J1EnX589O8KAxCGEdmhZY3r", function ($chunk) use (&$output) {
  $output .= $chunk;
});
```

```java
Stripe.apiKey = "<<YOUR_SECRET_KEY>>";
Quote quote = Quote.retrieve("qt_0J1EnX589O8KAxCGEdmhZY3r");

final InputStream stream = quote.pdf();
final String body = StreamUtils.readToEnd(stream, ApiResource.CHARSET);
final StringBuilder sb = new StringBuilder();
final char[] buffer = new char[DEFAULT_BUF_SIZE];
final Reader in = new InputStreamReader(stream, charset);

int charsRead = 0;
while ((charsRead = in.read(buffer, 0, buffer.length)) > 0) {
  sb.append(buffer, 0, charsRead);
}
System.out.println(sb.toString());
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');
return stripe.quotes.pdf('qt_0J1EnX589O8KAxCGEdmhZY3r', (err, res) => {
  if (err) {
    return err; // Handle error/callbacks as needed
  }
  const chunks = [];
  res.on('data', (chunk) => chunks.push(chunk));
  res.on('error', err);
  res.on('end', () => {
    // Handle chunks or any callbacks as needed
  });
});
```

```go
stripe.Key = "<<YOUR_SECRET_KEY>>"

stream, err := PDF("qt_0J1EnX589O8KAxCGEdmhZY3r", &stripe.QuotePDFParams{})
body, err := ioutil.ReadAll(stream.LastResponse.Body)
```

```dotnet
StripeConfiguration.ApiKey = "<<YOUR_SECRET_KEY>>";

var service = new QuoteService();
var stream = service.Pdf(QuoteId, this.pdfOptions);
var content = new StreamReader(stream).ReadToEnd();
```

### Response

```json
{}
```