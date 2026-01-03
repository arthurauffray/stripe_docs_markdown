# Update a card

If you need to update only some card details, like the billing address or expiration date, you can do so without having to re-enter the full card details. Stripe also works directly with card networks so that your customers can [continue using your service](https://stripe.com/docs/saving-cards#automatic-card-updates) without interruption.

## Returns

Returns the card object.

## Parameters

- `address_city` (string, optional)
  City/District/Suburb/Town/Village.

- `address_country` (string, optional)
  Billing address country, if provided when creating card.

- `address_line1` (string, optional)
  Address line 1 (Street address/PO Box/Company name).

- `address_line2` (string, optional)
  Address line 2 (Apartment/Suite/Unit/Building).

- `address_state` (string, optional)
  State/County/Province/Region.

- `address_zip` (string, optional)
  ZIP or postal code.

- `default_for_currency` (boolean, optional)
  When set to true, this becomes the default external account for its currency.

- `exp_month` (string, optional)
  Two digit number representing the card’s expiration month.

- `exp_year` (string, optional)
  Four digit number representing the card’s expiration year.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `name` (string, optional)
  Cardholder name.

```curl
curl https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts/card_1NBLeN2eZvKYlo2CIq1o7Pzs \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
```

```cli
stripe external_accounts update acct_1032D82eZvKYlo2C card_1NBLeN2eZvKYlo2CIq1o7Pzs \
  -d "metadata[order_id]"=6735
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

result = client.v1.accounts.external_accounts.update(
  'acct_1032D82eZvKYlo2C',
  'card_1NBLeN2eZvKYlo2CIq1o7Pzs',
  {metadata: {order_id: '6735'}},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

external_account = client.v1.accounts.external_accounts.update(
  "acct_1032D82eZvKYlo2C",
  "card_1NBLeN2eZvKYlo2CIq1o7Pzs",
  {"metadata": {"order_id": "6735"}},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$externalAccount = $stripe->accounts->updateExternalAccount(
  'acct_1032D82eZvKYlo2C',
  'card_1NBLeN2eZvKYlo2CIq1o7Pzs',
  ['metadata' => ['order_id' => '6735']]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AccountExternalAccountUpdateParams params =
  AccountExternalAccountUpdateParams.builder()
    .putMetadata("order_id", "6735")
    .build();

ExternalAccount externalAccount =
  client.v1().accounts().externalAccounts().update(
    "acct_1032D82eZvKYlo2C",
    "card_1NBLeN2eZvKYlo2CIq1o7Pzs",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const externalAccount = await stripe.accounts.updateExternalAccount(
  'acct_1032D82eZvKYlo2C',
  'card_1NBLeN2eZvKYlo2CIq1o7Pzs',
  {
    metadata: {
      order_id: '6735',
    },
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.BankAccountUpdateParams{
  Account: stripe.String("acct_1032D82eZvKYlo2C"),
}
params.AddMetadata("order_id", "6735")
result, err := sc.V1BankAccounts.Update(
  context.TODO(), "card_1NBLeN2eZvKYlo2CIq1o7Pzs", params)
```

```dotnet
var options = new CardUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Cards;
IExternalAccount iExternalAccount = service.Update(
    "acct_1032D82eZvKYlo2C",
    "card_1NBLeN2eZvKYlo2CIq1o7Pzs",
    options);
```

### Response

```json
{
  "id": "card_1NBLeN2eZvKYlo2CIq1o7Pzs",
  "object": "card",
  "address_city": null,
  "address_country": null,
  "address_line1": null,
  "address_line1_check": null,
  "address_line2": null,
  "address_state": null,
  "address_zip": null,
  "address_zip_check": null,
  "brand": "Visa",
  "country": "US",
  "cvc_check": "pass",
  "dynamic_last4": null,
  "exp_month": 8,
  "exp_year": 2024,
  "fingerprint": "Xt5EWLLDS7FJjR1c",
  "funding": "credit",
  "last4": "4242",
  "metadata": {
    "order_id": "6735"
  },
  "name": "Jenny Rosen",
  "redaction": null,
  "tokenization_method": null,
  "wallet": null,
  "account": "acct_1032D82eZvKYlo2C"
}
```