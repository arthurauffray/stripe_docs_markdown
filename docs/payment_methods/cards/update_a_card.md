# Update a card

Updates a specified card for a given customer.

## Returns

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

- `exp_month` (string, optional)
  Two digit number representing the card’s expiration month.

- `exp_year` (string, optional)
  Four digit number representing the card’s expiration year.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `name` (string, optional)
  Cardholder name.

```curl
curl https://api.stripe.com/v1/customers/acct_1032D82eZvKYlo2C/sources/card_1NBLeN2eZvKYlo2CIq1o7Pzs \
  -u "<<YOUR_SECRET_KEY>>" \
  -d name="Jenny Rosen"
```

```cli
stripe bank_accounts update acct_1032D82eZvKYlo2C card_1NBLeN2eZvKYlo2CIq1o7Pzs \
  --name="Jenny Rosen"
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

result = client.v1.customers.payment_sources.update(
  'acct_1032D82eZvKYlo2C',
  'card_1NBLeN2eZvKYlo2CIq1o7Pzs',
  {name: 'Jenny Rosen'},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

payment_source = client.v1.customers.payment_sources.update(
  "acct_1032D82eZvKYlo2C",
  "card_1NBLeN2eZvKYlo2CIq1o7Pzs",
  {"name": "Jenny Rosen"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentSource = $stripe->customers->updateSource(
  'acct_1032D82eZvKYlo2C',
  'card_1NBLeN2eZvKYlo2CIq1o7Pzs',
  ['name' => 'Jenny Rosen']
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CustomerPaymentSourceUpdateParams params =
  CustomerPaymentSourceUpdateParams.builder().setName("Jenny Rosen").build();

PaymentSource paymentSource =
  client.v1().customers().paymentSources().update(
    "acct_1032D82eZvKYlo2C",
    "card_1NBLeN2eZvKYlo2CIq1o7Pzs",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customerSource = await stripe.customers.updateSource(
  'acct_1032D82eZvKYlo2C',
  'card_1NBLeN2eZvKYlo2CIq1o7Pzs',
  {
    name: 'Jenny Rosen',
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CardUpdateParams{
  Name: stripe.String("Jenny Rosen"),
  Customer: stripe.String("acct_1032D82eZvKYlo2C"),
}
result, err := sc.V1Cards.Update(
  context.TODO(), "card_1NBLeN2eZvKYlo2CIq1o7Pzs", params)
```

```dotnet
var options = new CustomerPaymentSourceUpdateOptions { Name = "Jenny Rosen" };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Customers.PaymentSources;
IPaymentSource iPaymentSource = service.Update(
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
  "metadata": {},
  "name": "Jenny Rosen",
  "redaction": null,
  "tokenization_method": null,
  "wallet": null,
  "account": "acct_1032D82eZvKYlo2C"
}
```