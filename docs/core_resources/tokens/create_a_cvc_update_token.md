# Create a CVC update token

Creates a single-use token that represents an updated CVC value that you can use for [CVC re-collection](https://docs.stripe.com/docs/payments/accept-a-payment-synchronously.md#web-recollect-cvc). Use this token when [you confirm a card payment](https://docs.stripe.com/docs/api/payment_intents/confirm.md#confirm_payment_intent-payment_method_options-card-cvc_token) or use a saved card on a `PaymentIntent` with `confirmation_method: manual`.

For most cases, use our [JavaScript library](https://docs.stripe.com/docs/js/tokens/create_token?type=cvc_update) instead of using the API. For a `PaymentIntent` with `confirmation_method: automatic`, use our recommended [payments integration](https://docs.stripe.com/docs/payments/save-during-payment.md#web-recollect-cvc) without tokenizing the CVC value.

## Returns

Returns the created CVC update token if it’s successful. Otherwise, this call raises [an error](https://docs.stripe.com/api/tokens/create_cvc_update.md#errors).

## Parameters

- `cvc_update` (object, required)
  The updated CVC value this token represents.

  - `cvc_update.cvc` (string, required)
    The CVC value, in string form.

```curl
curl https://api.stripe.com/v1/tokens \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "cvc_update[cvc]"=123
```

```cli
stripe tokens create  \
  -d "cvc_update[cvc]"=123
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

token = client.v1.tokens.create({cvc_update: {cvc: '123'}})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

token = client.v1.tokens.create({"cvc_update": {"cvc": "123"}})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$token = $stripe->tokens->create(['cvc_update' => ['cvc' => '123']]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TokenCreateParams params =
  TokenCreateParams.builder()
    .setCvcUpdate(TokenCreateParams.CvcUpdate.builder().setCvc("123").build())
    .build();

Token token = client.v1().tokens().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const token = await stripe.tokens.create({
  cvc_update: {
    cvc: '123',
  },
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TokenCreateParams{
  CVCUpdate: &stripe.TokenCreateCVCUpdateParams{CVC: stripe.String("123")},
}
result, err := sc.V1Tokens.Create(context.TODO(), params)
```

```dotnet
var options = new TokenCreateOptions
{
    CvcUpdate = new TokenCvcUpdateOptions { Cvc = "123" },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Tokens;
Token token = service.Create(options);
```

### Response

```json
{
  "id": "cvctok_1NkWsu2eZvKYlo2CFDm6ab7X",
  "object": "token",
  "client_ip": null,
  "created": 1693334608,
  "livemode": false,
  "redaction": null,
  "type": "cvc_update",
  "used": false
}
```