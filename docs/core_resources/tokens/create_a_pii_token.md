# Create a PII token

Creates a single-use token that represents the details of personally identifiable information (PII). You can use this token in place of an [id_number](https://docs.stripe.com/api/tokens/create_pii.md#update_account-individual-id_number) or [id_number_secondary](https://docs.stripe.com/api/tokens/create_pii.md#update_account-individual-id_number_secondary) in Account or Person Update API methods. You can only use a PII token once.

## Returns

Returns the created PII token if it’s successful. Otherwise, this call raises [an error](https://docs.stripe.com/api/tokens/create_pii.md#errors).

## Parameters

- `pii` (object, required)
  The PII this token represents.

  - `pii.id_number` (string, optional)
    The `id_number` for the PII, in string form.

```curl
curl https://api.stripe.com/v1/tokens \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "pii[id_number]"=000000000
```

```cli
stripe tokens create  \
  -d "pii[id_number]"=000000000
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

token = client.v1.tokens.create({pii: {id_number: '000000000'}})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

token = client.v1.tokens.create({"pii": {"id_number": "000000000"}})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$token = $stripe->tokens->create(['pii' => ['id_number' => '000000000']]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TokenCreateParams params =
  TokenCreateParams.builder()
    .setPii(TokenCreateParams.Pii.builder().setIdNumber("000000000").build())
    .build();

Token token = client.v1().tokens().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const token = await stripe.tokens.create({
  pii: {
    id_number: '000000000',
  },
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TokenCreateParams{
  PII: &stripe.TokenCreatePIIParams{IDNumber: stripe.String("000000000")},
}
result, err := sc.V1Tokens.Create(context.TODO(), params)
```

```dotnet
var options = new TokenCreateOptions
{
    Pii = new TokenPiiOptions { IdNumber = "000000000" },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Tokens;
Token token = service.Create(options);
```

### Response

```json
{
  "id": "pii_18PwbX2eZvKYlo2CzRXgwN3J",
  "object": "token",
  "client_ip": "124.123.76.134",
  "created": 1466783547,
  "livemode": false,
  "redaction": null,
  "type": "pii",
  "used": false
}
```